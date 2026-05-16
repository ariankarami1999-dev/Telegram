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
<img src="https://cdn4.telesco.pe/file/O2aWxPgh7A7l5-Le1oZrswqIGfq0EJpX4L_19Un-TS8jEGgbrnB4db_N1hAkJKdc12JlO8ziGQNnhLvBF3tQwDD6fRFEENQgy9I5m3TLC-iNZ_5PbL8neuZ3FRoiIQ4VyHjMaEW1uWPF3OPYgiyonr-5AOFSYeuZNLEyHKKc4025N_fiZsu5wq_HWvexJ76vX7GCST9YzmnMpgvZ0ylkbaFU7f_B_pZrzSD5f4XiNwDM4nOsL6HnyxJzWPDJu1DF81sLLWmpjovfbJraWiQCCZNUHUAKtgwYSwOrQsDnNFZiDX8jaZwd5e-aC8V1zx-srMfs8AQdkR48GfT57TubXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 953K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 20:18:30</div>
<hr>

<div class="tg-post" id="msg-120439">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
معاریو: ترامپ در آستانه چراغ سبز به اسرائیل برای ازسرگیری حملات است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/120439" target="_blank">📅 20:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120438">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
کاخ سفید : همه گزینه ها در مورد ایران تو اختیار ترامپه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/alonews/120438" target="_blank">📅 20:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120437">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ادعای سی‌ان‌ان، به نقل از منابع آگاه:
در دولت ترامپ نظرات متفاوتی در مورد چگونگی برخورد با ایران وجود دارد.
🔴
دولت ترامپ و مقامات پنتاگون بر حملات هدفمند اصرار دارند، در حالی که دیگران از دیپلماسی حمایت می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/alonews/120437" target="_blank">📅 19:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120436">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/042ae6010a.mp4?token=Z_q84IpNlAaAk4sjuhxmDxX1G5iZtEak5k_N1uzWPnAQi8GXBMKUlA81w8XtDvVUAAbOKYsYzvBXDH7dzeRTNh_dDzf75tGUzEAjrxrf6rJnU4Yy8p9I-in7koIyCNhAbzSoga6s9svDNZUtta-V_gaSJcV4wTWxi-d9bxsX07Qpa4zGVGLWEqL84_c7xvtkLsQKIyo429882I123WA1Sej7HnYOOVbf7ClxR7VGjni8m5FMDdKDGL5x9oJ_D6MUgXzWev0Ja3SBJ_09S2aaQob1sz7z0x9hE4wC2Rq-YziGTfqtYEq0BSHsoQduEA4Xt4JhRbSHq-q-S-QMf60QTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/042ae6010a.mp4?token=Z_q84IpNlAaAk4sjuhxmDxX1G5iZtEak5k_N1uzWPnAQi8GXBMKUlA81w8XtDvVUAAbOKYsYzvBXDH7dzeRTNh_dDzf75tGUzEAjrxrf6rJnU4Yy8p9I-in7koIyCNhAbzSoga6s9svDNZUtta-V_gaSJcV4wTWxi-d9bxsX07Qpa4zGVGLWEqL84_c7xvtkLsQKIyo429882I123WA1Sej7HnYOOVbf7ClxR7VGjni8m5FMDdKDGL5x9oJ_D6MUgXzWev0Ja3SBJ_09S2aaQob1sz7z0x9hE4wC2Rq-YziGTfqtYEq0BSHsoQduEA4Xt4JhRbSHq-q-S-QMf60QTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت جنوب لبنان دقایقی قبل ، پس از حملات اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/alonews/120436" target="_blank">📅 19:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120435">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRY-MA60g_DNNgVhriLOhBP9PiXDremonAsrHlfOwxkEbJp6hSP92mI21CEaSOEQCJ8ZbQz3LZX3j9vjYQVSPp3AW01gX50ZohIJTy-ZUkzbuxY3laTxx4WX6SQYcis54OpzhhF4NbMxY5T9xdM9c617RzKwCwKh2hgu6v1uTEFJK7SHPc74Mj1GkJm1zk2snk-np_045IhXj3C6ANVOS272gdcwyoK6MoHnvFVnai07xJ6kmLwuVLJSMSSG-k-0SEzH2YklApnQ-Qezq88S9KR4G8IClPTDzEQgg-SfNqkX5hWN23v2C7T5eh1gNE0R7I3h2kssQX1Yt730dX0dUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده دائم روسیه در سازمان‌های بین‌المللی مستقر در وین، موضع چین در قبال قطعنامه ضدایرانی بحرین و آمریکا در ارتباط با تنگه هرمز را تایید کرد و گفت «روسیه هم همین دیدگاه را دارد»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/alonews/120435" target="_blank">📅 19:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120434">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
هیمتی رئیس بانک مرکزی: با قدرت، شتاب تورم را کنترل خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/alonews/120434" target="_blank">📅 19:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120433">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e1bb05efa.mp4?token=J-S8XyFfE7mqnlI52zG-Wfa5JCj-Htv4iaDRVUUEVf-5qunv11TK9I3vzLhjFX2WBCFKB6hc474X9uixFPJFJKR3_L4IdvO2l6eNLwxrNZPgVhtew4Pl_yjw-0OjamY1KImDdSxYxNum0tF8bWP8idIt7DHHKWAKTMUWveVBSIOkschBlJ5DkrDRrbRWrzplHC4SsVCE014hfsLDOsOLkaK8LXNHrZJKjGbBknv3ctwqy5mi8cSfaW6whoss5WxJR1O6ldMWlo24PofyRW_g-jbf8NdfeY2lwfhTvR0SxdKA62qZm5EUrYXbVZiMM_5YRZPqcOwCJMNrSafzux5wcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e1bb05efa.mp4?token=J-S8XyFfE7mqnlI52zG-Wfa5JCj-Htv4iaDRVUUEVf-5qunv11TK9I3vzLhjFX2WBCFKB6hc474X9uixFPJFJKR3_L4IdvO2l6eNLwxrNZPgVhtew4Pl_yjw-0OjamY1KImDdSxYxNum0tF8bWP8idIt7DHHKWAKTMUWveVBSIOkschBlJ5DkrDRrbRWrzplHC4SsVCE014hfsLDOsOLkaK8LXNHrZJKjGbBknv3ctwqy5mi8cSfaW6whoss5WxJR1O6ldMWlo24PofyRW_g-jbf8NdfeY2lwfhTvR0SxdKA62qZm5EUrYXbVZiMM_5YRZPqcOwCJMNrSafzux5wcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز ایران یه نفتکش حامل ۴۵۰ هزار بشکه نفت رو به دلیل نقض قوانین جدید تو تنگه هرمز توقیف کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/alonews/120433" target="_blank">📅 19:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120432">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
کامران یوسف خبرنگار رسانه پاکستانی اکسپرس نیوز: سفر اعلام‌نشده وزیر کشور پاکستان به تهران، بخشی از تلاش آخر برای حصول توافق بین ایران و آمریکا است.
🔴
نقوی از معتمدان نزدیک فیلد مارشال (فرمانده ارتش پاکستان) است و یک ماه پیش نیز او را در سفر سه‌روزه‌اش به ایران همراهی کرده بود.
🔴
با توجه به اینکه ترامپ پس از سفر پکن به واشنگتن بازگشته و در حال اندیشیدن به گام بعدی است، سفر وزیر کشور پاکستان حیاتی تلقی می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/120432" target="_blank">📅 19:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120431">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
شبکهٔ ۱۴ اسرائیل از شنیده‌شدن ۲ انفجار در الجلیل غربی خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/alonews/120431" target="_blank">📅 19:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120430">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJFjnRshuoHqMVWIYa6Yd5I-HHVv1TGp7KSbfmdfbkesNjaJzuzZc_EU9QnipgW7sgMENn26r39YaEP4wsbnWotcPkpLb7G91-7kDr72mx_AQjFh8dMun_gAkB0Tg4aCLG3cyMsP8rRIgJ6k04N8M15uMGOI0dZYIEFPqiAK2rdnLsFj0ePTJUUsypRTLhieedLzuMTVhETFOig7npuAbjHC7Q5tvPQOVcDWvv-PjH2-doOkxjIEqNeBAcAXxFMWUAb2V_MAsoIJYX0gVQMoWp1Izo007DLmYHL1ZInhd0DH1Y_apxSLGmwMLTmpqSZW0NwMSN_asueXzXvW75tZ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تلگراف : مقامای ارشد دولت ترامپ از امارات خواستن تو جنگ علیه ایران بیشتر وارد عمل بشه..
🔴
حتی صحبت از حمله به جزایر ایرانی تو خلیج فارس هم شده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/alonews/120430" target="_blank">📅 19:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120429">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
حماس: جنبش حماس یک دور انتخابات برای انتخاب رئیس خود برگزار کرده اما نتیجه در دور اول مشخص نشده؛ دور دوم بعداً برگزار خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/alonews/120429" target="_blank">📅 19:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120428">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
وزیر بهداشت مستعفی در بریتانیا عزم خود را برای نامزدی جهت جانشینی استارمر اعلام کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/120428" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120427">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
به گزارش آناتولی، دونالد ترامپ، رئیس جمهور دولت آمریکا  در گفتگو با رسانه‌های فرانسوی درباره مذاکرات با ایران مدعی شد: آن‌ها علاقه‌مند به دستیابی به توافق هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/alonews/120427" target="_blank">📅 19:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120426">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
اولیانوف دیپلمات ارشد روس اعلام کرد که مسکو نیز همانند چین، پیش‌نویس قطعنامه آمریکا و اعراب درمورد تنگه هرمز را مناسب نمی داند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/120426" target="_blank">📅 19:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120425">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
گسیل ترابری نظامی آمریکا به منطقه طی ساعات اخیر افزایشی بوده اما نکته مهم خاموش کردن سامانه و عدم ذکر مقصد در پروازهای اخیر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/alonews/120425" target="_blank">📅 18:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120424">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
العربیه: طبق گفته منابع آگاه پاکستانی، در بحث تنگه هرمز، پیشرفت‌هایی حاصل شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/120424" target="_blank">📅 18:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120423">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
مدیر روس‌اتم: عملیات بتن‌ریزی و آرماتوربندی ساختمان‌های واحد دوم نیروگاه هسته‌ای بوشهر در ایران از سر گرفته شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/120423" target="_blank">📅 18:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120422">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
حملات ارتش اسرائیل به لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/alonews/120422" target="_blank">📅 18:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120421">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a616414a5.mp4?token=FqFSF8OAXDXxpFP2wqRIl75bNIbbAemXZvMX-K590cR8h1APhlpipPiDduPUYTBPNsUMKaB6xJhRI4dhbNIthDBG-bs0g1kwcgiZpnCshBS-mNnDlXUmRbyx1DiUqFS8p2CW25Yfm7Tf1pOpcl9x2I-_C0zXLm_z3A6xZyqwqOwN4ATNMyofaOBzG6fgyH-j6SEfboGf5Zhn7Dt_8LGQHkuS9lpJLAyRfy9zwdWFkeHJuWMSd0NZzZ2HPS_Zmfhi-oR4csdKfNF5NDdiEa2XuB9I5O3MqSIMfyNCMwsyb1jE8Kb7agAuJrf57lLReuPVfAZRxEHeeJuUhrZvkqW6tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a616414a5.mp4?token=FqFSF8OAXDXxpFP2wqRIl75bNIbbAemXZvMX-K590cR8h1APhlpipPiDduPUYTBPNsUMKaB6xJhRI4dhbNIthDBG-bs0g1kwcgiZpnCshBS-mNnDlXUmRbyx1DiUqFS8p2CW25Yfm7Tf1pOpcl9x2I-_C0zXLm_z3A6xZyqwqOwN4ATNMyofaOBzG6fgyH-j6SEfboGf5Zhn7Dt_8LGQHkuS9lpJLAyRfy9zwdWFkeHJuWMSd0NZzZ2HPS_Zmfhi-oR4csdKfNF5NDdiEa2XuB9I5O3MqSIMfyNCMwsyb1jE8Kb7agAuJrf57lLReuPVfAZRxEHeeJuUhrZvkqW6tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت عجیب و طوفانی توچال
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/120421" target="_blank">📅 18:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120420">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssdvGskLDJuddeCXMKkYnvfcwX87Ib2cRf2b7E6l6qNObC2f43Opx-xfChtYjRzuI8X5eWliiSTTeZqBaOtoDByQFfFkMbU4S5yvmMzjtoWCiUJjEtoFiwK28AuvlMg8MQazvrohhYFlGXV6pykQK1uLv5-n8b7q6J1xUbegitfGUGawqo0RmnEFXQDmXekhDDlgg_SWcFzRaNfllSPeJzQNiDJRckIKxxZKnm0Xxd8Eb5IxzhirVzqYhciQFCl3P0HkClCH-hrnpdU9JqnStpwGft5u4TwgEUpv3aqkB3UJZOK7dU9-oK4rC90YxEuAipA-BkI23moCOBXe1fs-ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری صداوسیمای جمهوری اسلامی، روز شنبه ۲۶ اردیبهشت در گزارشی اختصاصی اعلام کرد که «چند کشور اروپایی» به‌دنبال انجام امور اداری و دریافت «تاییدیه» از تهران هستند تا بتوانند شناورهایشان را از تنگه هرمز عبور دهند.
🔴
این خبرگزاری با اشاره به گزارش‌ها از عبور موفق نفتکش‌هایی از چین، ژاپن و پاکستان از مسیر تعیین شده از سوی جمهوری اسلامی، تاکید کرد که این عبورها با «اجازه نیروی دریایی ایران» انجام شده است. صداوسیما نام این «کشورهای اروپایی» را اعلام نکرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/alonews/120420" target="_blank">📅 18:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120419">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
امتحانات خرداد دانش‌آموزان پایه‌های هفتم تا دهم اصفهان غیرحضوری شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/120419" target="_blank">📅 18:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120418">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaYHiQNCqefEctnXIVmrjcDqtKU4pcIO3L70b8QhO3-lIRC_5Zuyn2FtZdHOGsQMS9CyAa85uU5c2Xgws31b2Y8fI5fjZ7luCTtskuLkFS0EIZrFNv-EsvOEfs7WlQrSqrih3vRRVvv2kzkXl8GqFTtVyE44cH4h5kKqGoo89tPet0XlbB80LfTCO0iwRJWEHex-1Iakl-F7q_NKt9Zjr7Fq5b6KQ2WjUht0l8w5YH4_WknpU4k_nxq8PWMqlkkGYOz-xyB9nxPYHi0aPQQZjZTVoNoabmyUH_3Kgfd08NaowWBfxex_sNeshkuA0m4WEPA2kUts0zmQBMrMLfrKDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
کویت تصویر تسلیم شدن چهار پاسدار را منتشر کرد!
🔴
کویت با صدور بیانیه‌ای جمهوری اسلامی را به حمله به جزیره «بوبیان» با قایق‌های ماهیگیری  متهم کرد و اعلام کرد نیروهای سپاه پاسداران قصد خرابکاری داشتند؛ یک نظامی  کویتی در درگیری زخمی و ۴ تن از عناصر وابسته به سپاه دستگیر شدند.
🔴
چهار پاسدار احتمالا نیروی قدس با دیدن اولین اسلحه دست طرف مقابل تسلیم شدند !
🔴
دو سرهنگ، یک سرگرد و یک ستوان‌یکم.
🤔
عملیات آغاز نشده لو رفت و تسلیم شدند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/alonews/120418" target="_blank">📅 18:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120417">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
هم اکنون گزارش رسانه های عربی از تحرکات بزرگ نظامی در سراسر خاورمیانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/alonews/120417" target="_blank">📅 18:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120416">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
رویترز: به گفته دو منبع آگاه، در داخل کاخ سفید هیچ تلاشی برای متقاعد کردن ترامپ به خویشتنداری بیشتر در پیام‌هایش درباره ایران صورت نگرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/120416" target="_blank">📅 18:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120414">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UavQQgsYzKXAbQDGHe1Qf2c2oGNbIyN4eI46PjHjK2I-OrKfaJx06JeAEwkETAafl2fVcCZexBFFzRLgDtM3a1iCciy_LDOOsr8y84-xDrDDZzFZt4TpFNQ1yI4nv5rpW5uNzN225qzvOxUrmkODSzIexJTGhVzDNF_malYnmeEDgH7GG_VL60PSc7TlvQ7tzuvlRT6tLUCfXG2ptBIPrcXR5gHT0A9zZf3UpMxW03buYkpJ81Y4bynrH-s3pUvnlYHUcbsvuPIFWeSmo9ACa8fAgq3GdRiXeF9Jnmr-u_SIqt2gRZCrpmYFmrhTpihhfv0BS0U85XB9Kv2fhPahcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a9GtgCsZ4VGIM9LKQFTdwm_EyorZs2RhNjen8l0bzaezEVOtzlSCzznBQFjVzqBks09HbwWjOjNw2quX4VkKIDb23jPA_dndqPBvcZRMyWPtWzOETE-CIjhljv2G1ZWy2f5JxIykzwxbD1Vw9qBEzFpNw62_AzRj9gpdj40AhRZ119L34Dy2x7Yl8mYoHv3IENASNUBdM7AVJ-0cQ1XkQBJdTXN25vLi7jxRiPGxVYNXDpQkxAETNIuXGUgVP5MWoeD0V_XNc-9MLHUFnUYWj4c1aIidfGOU4k_vfbAZwh4wbhx9UTUmBKqjqsxuJdCyaICFUOGq7bp2V5zH5nWM2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله‌ی‌ نیروی هوایی اسرائیل به المنصوری، جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/alonews/120414" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120413">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
حماس تأیید کرد که عزالدین الحداد، فرماندهی از تیپ‌های عزالدین القسام، در حمله هوایی هدفمند اسرائیل شب گذشته در شهر غزه کشته شد.
🔴
گروه ادعا می‌کند علاوه بر همسر و دختر الحداد، چندین غیرنظامی دیگر نیز در این حمله کشته شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/alonews/120413" target="_blank">📅 18:24 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120411">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87b8f05fcb.mp4?token=K9dEJie0QzA3lKTdC1v3nEqEMcrIecHl9Mi4iD1g5hTU73JYMR3j84xUO3sdVxsyKn9nAtkL8-JQrXrsfk1xCbXlkfYD6MxXsDw2Gq-YHGE8Cm5tImcMY8XUzynDk4obKudpv6EpQgneg9lZ8fs-mklpRPLVlwRRtAtr4XGmCVnEAkqICMLlNsh_5NUY4r5gO350R4ankFf3vD17n9Sbfwv1W4EjY-o1Pq_WVs506XJnaHwZTFs467W_oDP53jniQGV3B0X2DKy5WzMCRB6ZP1MIp-P_QpQsAeJgfUXmXhQLJcAEa477IW99nq3cB3SwLs1ySCtGqq6o0ICe4Hcu_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87b8f05fcb.mp4?token=K9dEJie0QzA3lKTdC1v3nEqEMcrIecHl9Mi4iD1g5hTU73JYMR3j84xUO3sdVxsyKn9nAtkL8-JQrXrsfk1xCbXlkfYD6MxXsDw2Gq-YHGE8Cm5tImcMY8XUzynDk4obKudpv6EpQgneg9lZ8fs-mklpRPLVlwRRtAtr4XGmCVnEAkqICMLlNsh_5NUY4r5gO350R4ankFf3vD17n9Sbfwv1W4EjY-o1Pq_WVs506XJnaHwZTFs467W_oDP53jniQGV3B0X2DKy5WzMCRB6ZP1MIp-P_QpQsAeJgfUXmXhQLJcAEa477IW99nq3cB3SwLs1ySCtGqq6o0ICe4Hcu_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر جنگ، پیت هگستث، دریانوردان گروه ضربت ناو هواپیمابر USS Gerald R. Ford را پس از بازگشت به پایگاه نیروی دریایی نورفولک از یک ماموریت تاریخی ۱۱ ماهه، خوش‌آمد گفت.
🔴
ویدیوی اول از USS Gerald R. Ford (CVN-78) است و ویدیوی دوم هگستث را در حال خطاب قرار دادن نیروها در USS Bainbridge (DDG-96) نشان می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/120411" target="_blank">📅 18:16 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120408">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کرملین : پوتین با رئیس امارات متحده عربی درباره ایران گفتگو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/120408" target="_blank">📅 18:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120407">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oj6iYgAMu25TD2LDZWqum0IOAXaJLXFg_tc-hzL-VPNZpMW7pyJBU5QT9j84zRK3X80APtrBawtBEO1GAtLmRV-vNo1VeDii_miAWbred2iTNWRF-oFeOQZHnbjXGiE76V8nLBPzfQrHMzM2eOtpZ_j9999ZKgMAU4l0MSuwdpy65_xmGA0fHTDPpBrjJDUTX2ED1lk2yLRry5MTCla9f8EF4t37SgSFrmvpX6L35EyUuCXJFWZeG-WbJz6HmdMDFaHtDZZhfzngizPDuJGwkRIz1pzrZvwht7sNpM4JwHSUodkHTOvswns7sNCBjLdFhxmgmvh4CGfndP5Naz-J8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال:
بازی نداریم! ببین قراره بعدش تو موضوع مورد علاقت چه اتفاقی بیفته!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/120407" target="_blank">📅 18:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120406">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ویدیویی از ورود وزیر کشور پاکستان به ایران
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/120406" target="_blank">📅 18:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120404">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDvq0GgTXB8kgnS6qrtH9SNlGOaZc3b0OQJW5F0v4vr7E2a8DIorZUOpHrxbA0XX3Dry7ZR59dCHZxa4UEl7rfs2RFHXHxzIO69RyKei7xVkKF3hRJQhdsX00H0vTe9evakwvqp4cgg6j_x2Tdeo2LI9qXhYenvghU-C3bvPD4nNkkXIobqbvyxIhQFH2kCS_ocr7sz4f3Rm_btTtFKmQT16UF9Ak8KPo8fBIlgq8T23RBrw3x8Aax6eNjImMsM5OEOqxwhU9pXAsqYMbczxqO0O5aJ3RbDJk_7FF4SjmOJje9ulWzxcQWPFErT3UtqjP7Il3T940mbqOjTGklovPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e829d87678.mp4?token=XXynBzPnBKuCXcBrXgvrG-5zCDf3Ham9G9KXtb6H_H107m5mM7BKQ1ReSRFNUVz9DoBYeyHEWOsURgbYm12Z3b5aSAMIg1Ka-nur_JYmWWQ5UcIs8lelQ39UKY255-r6ofyyKTjFBiPVAmTr_fYFdFd-9Mq6N6sSssKfFyiiCJ1yA8uikSAqDJKhfAlw1FnbRCIHsvG1i4FvWb1r1Dr0URehEvWhx4FGMCkUwLhkiD_dGpDLfrRMKSP_nz5oLhlvqQ27WgGf0R4J-l1cW7odq5AbvRqs0gf1oUKAqH68IexuCZ3P9RZqjL0sdphdWw5IgadbcJsTryk-pZW1TfefDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e829d87678.mp4?token=XXynBzPnBKuCXcBrXgvrG-5zCDf3Ham9G9KXtb6H_H107m5mM7BKQ1ReSRFNUVz9DoBYeyHEWOsURgbYm12Z3b5aSAMIg1Ka-nur_JYmWWQ5UcIs8lelQ39UKY255-r6ofyyKTjFBiPVAmTr_fYFdFd-9Mq6N6sSssKfFyiiCJ1yA8uikSAqDJKhfAlw1FnbRCIHsvG1i4FvWb1r1Dr0URehEvWhx4FGMCkUwLhkiD_dGpDLfrRMKSP_nz5oLhlvqQ27WgGf0R4J-l1cW7odq5AbvRqs0gf1oUKAqH68IexuCZ3P9RZqjL0sdphdWw5IgadbcJsTryk-pZW1TfefDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چند طرفدار فلسطین از برج ایفل بالا رفتند و پرچم فلسطین را از طبقه اول آن آویزان کردند.
🔴
شش نفر از این افراد توسط پلیس دستگیر شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/120404" target="_blank">📅 17:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120403">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgNQ90du7wv7TIUtMMAyYbi0yTABNNBmqyCvtoGUZK5jUHUIGeLrSAgpRkYpPIbN-EtIB_bxGp6dmQv6w0AeiMf9Af7qadsI3yp8PyusrKBKz7wQ1dPwHQ4vkch7m6R87jmGy81jbqui10HACY8gsv_E9lgEotfYu0rnoB_Un5UvJQ7oUEX_orx3ZjdPcUnpDFpft1ufC3EQ1gq7L6HUbB1ge3yeLvGMpU4PWIxBz3vy8Hsp06dozI04LUu-GlKMjwCqeCNpJvXL7nI3Sk_EBXTF_d35wuMBawHiYYUzxY5fkxbAygGQI5VIdS3XGiqMcePdh5R8to_WRN7cS4VqIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاول دورف، مالک تلگرام: دبی دوباره شلوغ و پر ترافیک شده
- از همین الان دلم برای آتش‌بازی‌های ایرانی تنگ شده، حداقل شهر رو از آدمای زودباور خالی می‌کردن
- پدافند اماراتم زیر اون حجم آتیش خیلی خوب کار کرد
- با مالیات صفر درصد، امنیتی بهتر از اروپاییایی داریم که نصف درآمدشونو مالیات میدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/120403" target="_blank">📅 17:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120402">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d65uil_jDNmDBm8nVsyUg9I3S6ClnyfI8q42yVvgnZMl_MyJhjW9E_OQuSmWxv2v6JhRsl_jFUI1UDSfhqr0anRfBaXl_7CuyTKFGuYwooH8lDzwljpmSwCnwyCIdDvMtec69b5IAp5xWOp7v5fHrQY-wAvZz0gOmt3Pj99uUG88n96Hsdbh9ZxG_m1E2zlpjBYzEYc3EGU6IoNb8mhPxRSPY_5QWky4EdDZFc6A-QkXbA7JHZA8rnfglmKdw9wpGywa5DTsM5wHwUD2O7YK1b8AFXhluRZs2l4PI8YVqNAWj9-GM0UR9p1p70j8UfsnLZEk_jBMF9q-FcoUjFT_RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمب موسی
😁
فروش کانفیگ وی توری
🔐
گیگی 195.000 تومان
☄️
گیگی 220.000 تومان
☄️
🔥
سرعت موشکی
💎
( پنل مشاهده حجم در ربات )
لوکیشن ترکیه
برای خرید ربات رو استارت کنید
BOT
📎
@WinstonMarket_bot
PV
✉️
@mosadeveloper
CH
📣
https://t.me/winstonservice</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/120402" target="_blank">📅 17:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120400">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72181fb229.mp4?token=UYbmPPHW7muiPVlsIbw5NB66hcTyiRbH9Nf2pYKLuJZKQQenz83YIixoNPEI6QSTM5KInvz0nMeQvmPcUe7GZyXpTiVIYYA7jwIAWNWdEH56CRH4lk1xFy2RqRXk9qeqeDlF9ca3dwN3hVmOVRv-r952W4_VXs_sqxx59q6_AJDLavC6YSEuFIMi2wbZJuh2nM64UzuoG0Q0SF9Daymc3mwkVPNJU8v_Qd8TmoRe4lLEmVSmh9YuWuQTHcucVbxcGn1M4z5cRxKv-bdf7_Yz0BUcgMCxhBzPZvH5U5NBalpABTNQT8Eu0EtpaOw6iMbilMRwFyMiKWzXBPYJZEurHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72181fb229.mp4?token=UYbmPPHW7muiPVlsIbw5NB66hcTyiRbH9Nf2pYKLuJZKQQenz83YIixoNPEI6QSTM5KInvz0nMeQvmPcUe7GZyXpTiVIYYA7jwIAWNWdEH56CRH4lk1xFy2RqRXk9qeqeDlF9ca3dwN3hVmOVRv-r952W4_VXs_sqxx59q6_AJDLavC6YSEuFIMi2wbZJuh2nM64UzuoG0Q0SF9Daymc3mwkVPNJU8v_Qd8TmoRe4lLEmVSmh9YuWuQTHcucVbxcGn1M4z5cRxKv-bdf7_Yz0BUcgMCxhBzPZvH5U5NBalpABTNQT8Eu0EtpaOw6iMbilMRwFyMiKWzXBPYJZEurHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از حملات به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/120400" target="_blank">📅 17:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120399">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزیر نفت عراق: ۱۰ میلیون بشکه نفط در ماه گذشته از تنگه هرمز صادر کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/120399" target="_blank">📅 17:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120398">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ویدیویی از ورود وزیر کشور پاکستان به ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/120398" target="_blank">📅 17:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120397">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
هم اکنون بمباران در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/120397" target="_blank">📅 17:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120396">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfJcM-StishnlLusKaRqSrbkIzd91Sim8jIpY0sIpiqTZxKsdx6WBtKhbXttG44_1TDtCyhSbu4ZTOMhGGwhVt7wI1OAPMkkvVYu0OKZXYvJX88IQ7r2i9fuZ3ytrP6EpLfkSqyHFfzeva6Di608Otzd3pSrgnAbKZhRULEpXUETSWKtB-0uc_Pa1jb26kM4aO7_vt3cNGIbDzRlS6AvvObQUGS-5EuNJJ-xrFgkTdFVdY5VtToRiZDPEzK1YLKG7NZWX6KC_bURt1BpGwPWqntv7M7Jj3qjDCLPEpKb9Kj4-dxZir9vpsgqlgvKMpFnYH_rfKvyS21Z8YXqVGcQnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آدرنالین خالص
🔥
💥
سلتیک در آخرین بازی فصل مقابل هارت به برتری ۳بر۱ رسید و قهرمان اسکاتلند شد
🚫
هارت رقیب مستقیم سلتیک بود و با یک تساوی هم میتونست قهرمان بشه اما با گل دقیقه ۸۹ مائدا قافیه رو باخت
@AloSport</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/120396" target="_blank">📅 17:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120395">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc03da9d9.mp4?token=vV3IPTD-ngCIxMsptpKyj3LNFHrgw4tBnspmE1HcmR8mAudWZnAIswdST63spHRBEcSis1p89XppyEHTK82vj8BKHjGCrEd2yNJ49vRw_8y1mCY3C39d5kFTkeTUIniiv0fnpKPGwKrKD2q35OsdAOURcZs8N6v-sm2PsuUGNVwoxhYW6kEgYarMnds2Lja4fhzRk-VlhVjBdvc3EsqC05-7tt0p0Mb_u9MnmQHJq1vJQ-lIw4feNAlXvIHiq8jWyJLe97oRCkhfMIwN1vLeNxgiGh8wiBn4HgKHDQun3zGx7Pjkfzbc2wI7Wr_6-LQdPzcnNbKwhM_PIls2ldWFNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc03da9d9.mp4?token=vV3IPTD-ngCIxMsptpKyj3LNFHrgw4tBnspmE1HcmR8mAudWZnAIswdST63spHRBEcSis1p89XppyEHTK82vj8BKHjGCrEd2yNJ49vRw_8y1mCY3C39d5kFTkeTUIniiv0fnpKPGwKrKD2q35OsdAOURcZs8N6v-sm2PsuUGNVwoxhYW6kEgYarMnds2Lja4fhzRk-VlhVjBdvc3EsqC05-7tt0p0Mb_u9MnmQHJq1vJQ-lIw4feNAlXvIHiq8jWyJLe97oRCkhfMIwN1vLeNxgiGh8wiBn4HgKHDQun3zGx7Pjkfzbc2wI7Wr_6-LQdPzcnNbKwhM_PIls2ldWFNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
به گواهی تاریخی هاشمی رفسنجانی، خون کودکان میناب و تمام قربانیان جنگ ایران و آمریکا به گردن علی خامنه‌ای است.
🔴
هاشمی رفسنجانی: «نظرم آن بود که باید مسائل با آمریکا را حل کنیم. با آقای خامنه‌ای یکی دو ساعت بحث کردیم، ولی به نتیجه نرسیدیم.
🔴
من گفتم: ما حرف دیگری به شما نمی‌توانیم بزنیم، فقط مساله‌ی ما هست و خدا؛ بالاخره روز قیامت از ما می‌پرسند این همه ضرری که این طرف (به مردم ایران) هست، اگر این‌ها را شما به عهده می‌گیرید من دیگر حرفی ندارم.»
🔴
علی خامنه‌ای گفت: «بله جواب خدا با من».
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/120395" target="_blank">📅 17:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120393">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBYHGYi2AF1O-CxtVPaW7E9pdbaUx1Uae-XbVix15s7jpAgtEKcv0dlNdeizvKf6dA8Ifngky2vb6xuJ6iL5P3yDvL8OaRTZotdZFS9XA3bDnHy3A3nY-IaAU9uSRVTNdkcKObxeD0sDUZUZRcaQYckH4lYbQsk3Wu0q_2rGGMWObJItVOsbKpmBrgHlPEd4v0s64-AH-wCHPuNQj_Wor5YlWHjLTcJ9MY7DfqADTXfiNhuj4ci0HMrlv71BbQ-mJdk1tQOTyE4xtBAIcE0BkEymuGwChLmfUqi4O05doT1pSIdNsClFxRNCVFUBPpO8is2xmEWiwQok9GhbFxulZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZp77g-BCL29K2aIznR0ySz2wqOhCJBAq6KBLaQVlCHqMeyC17z8kGXuzo0mxKmQ74hwxHC9T6RtINQzDFxa3m6sf2Cqj-7I_mDoMAc0g6YKkbU5TGCpfnf7u2Z8wHbxqcw68zefUDB25tjg-QaIHGRB1v50i7bxrsTD9g4qPmbHQC-ILMu9n7Lm7njwJubxV2K1yYgYCu9-jZR-QDjkxjcAq4l3Eb83AN4ohCcfbGxthc-OqilCG2Mmtr_HXWrJoTIrswopXEUkdw3PZVDgbiZU4F1lD8OSKpp2vvqR5PL8fXczfvHu1j9r2rioC5pGgNfe9Xxywf59KomFNy6OEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله‌ی‌ نیروی هوایی اسرائیل به المنصوری، جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/120393" target="_blank">📅 17:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120392">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
تا امروز، ۷۸ کشتی تجاری تغییر مسیر داده‌اند و ۴ کشتی غیرفعال شده‌اند تا اطمینان حاصل شود که قوانین محاصره رعایت می‌شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/120392" target="_blank">📅 17:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120391">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4aa4bf95d.mp4?token=NYsWY2XtRkxcZV6WJiXDHZpUE5rSWClFbc2JS9zsZZpwb292UGF-LjYGAjrmxHMN0dZENv-Es2k5ehr8mq6fKvlFK31NlrQH_vt4fWNEhw08Ba56b6qqe2-EsSg2F2XL_n5O_Z4GP_uQrdEGWsjOBGmtNynwrKN1hMcdHCo4EtkI9kcLmv6L8-XLTy5prihLoiZ18VioS07Rir56A4enSBMlM-1m2_MF7Cu3zYPqGsmeX_PTae6BaFyDM6Ir5x7nVXHkibW8N5vG5xU-fM33_RMetL1ctcUNRcG6r6mjfgcA0e8TAn3b4loZaBcHcbrTX943N-KmfRSYHBkJzxFrIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4aa4bf95d.mp4?token=NYsWY2XtRkxcZV6WJiXDHZpUE5rSWClFbc2JS9zsZZpwb292UGF-LjYGAjrmxHMN0dZENv-Es2k5ehr8mq6fKvlFK31NlrQH_vt4fWNEhw08Ba56b6qqe2-EsSg2F2XL_n5O_Z4GP_uQrdEGWsjOBGmtNynwrKN1hMcdHCo4EtkI9kcLmv6L8-XLTy5prihLoiZ18VioS07Rir56A4enSBMlM-1m2_MF7Cu3zYPqGsmeX_PTae6BaFyDM6Ir5x7nVXHkibW8N5vG5xU-fM33_RMetL1ctcUNRcG6r6mjfgcA0e8TAn3b4loZaBcHcbrTX943N-KmfRSYHBkJzxFrIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عارف: ما از حق حاکمیت خود در تنگه هرمز گذشته بودیم و اجازه دادیم از تنگه‌ای که متعلق به ایران است تجهیزات نظامی که قرار بود علیه ما استفاده کنند، عبور دهند؛ دیگر این کار را نمی‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/120391" target="_blank">📅 17:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120390">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d4552dff5.mp4?token=NgCjgjoqx8zkGmzCkHe9R_duzT1gFqGkjtn32hFyil4-YMou9pM3Zx2wXOhWjxvitc4tNAAz5u5ExqVZ9PROVaPzMs6l0W-UdhftbdnwR5uldUjUJDfeiveVqN6xefKGHJecfHTmaT2gkZBIniLu5eVbSX_MHTJJtyZP9dcnzaV5N6TZ9u64nkwsCsPnNDtzF2tfCLhxIF4Pd951aSmGeIqVlFFR8QVvcSs-_qn26XrqQ5Ygqn8bTxHBoixwreZsJ5VCj5-NKykFuTiv9ifMSm89x04RETQJ5xnkLnhW1y_Q5pgGsyOnY3rtmDUr9BF77rRsfmIA7g2vrj8LETGHfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d4552dff5.mp4?token=NgCjgjoqx8zkGmzCkHe9R_duzT1gFqGkjtn32hFyil4-YMou9pM3Zx2wXOhWjxvitc4tNAAz5u5ExqVZ9PROVaPzMs6l0W-UdhftbdnwR5uldUjUJDfeiveVqN6xefKGHJecfHTmaT2gkZBIniLu5eVbSX_MHTJJtyZP9dcnzaV5N6TZ9u64nkwsCsPnNDtzF2tfCLhxIF4Pd951aSmGeIqVlFFR8QVvcSs-_qn26XrqQ5Ygqn8bTxHBoixwreZsJ5VCj5-NKykFuTiv9ifMSm89x04RETQJ5xnkLnhW1y_Q5pgGsyOnY3rtmDUr9BF77rRsfmIA7g2vrj8LETGHfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دفتر ریاست جمهوری تایوان:
جمهوری چین یک کشور دموکراتیک مستقل و دارای حاکمیت است.
پکن هیچ حقی برای ادعا نسبت به تایوان ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/120390" target="_blank">📅 16:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120389">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
رسانه‌های رسمی ایران: کشورهای اروپایی در حال گفتگو با تهران درباره تنگه هرمز هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/120389" target="_blank">📅 16:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120388">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d1bd4ff3.mp4?token=PQ9J1tQ0bpgIdH1t-Qt4_8-7A5dSl938JBkdFPkg-jWdR1c6Ck41QXRuGOR7lBEvidhsCXf9XXaacyeF6jVbNyXKdqSRRQcNheMfzx-DZUsBmpe6yy_S3RVO0KrHf_x9Lis21zn418b9quH9GzHnATzaJpYqNeXRcrdOW5TdFlc4vT-HwrwPzVh5V_VSKx5gJLByQaiVQRcd592T2K1aBQWCRAkPzB_spWfN3KMXsxa0TRVOOagD97PvihbssUAqqY4OOeFEncpZbp9oFnE3UxxzY-R9ivuX1xa0QdPH-CKJgT8wZxElQlwkhdLf4JUGlLCZxXf5wkhnuwInDJVgCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d1bd4ff3.mp4?token=PQ9J1tQ0bpgIdH1t-Qt4_8-7A5dSl938JBkdFPkg-jWdR1c6Ck41QXRuGOR7lBEvidhsCXf9XXaacyeF6jVbNyXKdqSRRQcNheMfzx-DZUsBmpe6yy_S3RVO0KrHf_x9Lis21zn418b9quH9GzHnATzaJpYqNeXRcrdOW5TdFlc4vT-HwrwPzVh5V_VSKx5gJLByQaiVQRcd592T2K1aBQWCRAkPzB_spWfN3KMXsxa0TRVOOagD97PvihbssUAqqY4OOeFEncpZbp9oFnE3UxxzY-R9ivuX1xa0QdPH-CKJgT8wZxElQlwkhdLf4JUGlLCZxXf5wkhnuwInDJVgCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تهران کنارت، جدیدترین فیلمیه که بعد از جنگ توی سینماها اکران شده
حجاب به طرز قابل توجهی کنار رفته و در تیزر رسمی فیلم، خواننده زن یعنی سوگند داره میخونه!
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/120388" target="_blank">📅 16:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120385">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j67wNco8zL6J57O4G2YiLRrdNM_8UXayEI9KYUXugroXmF2e70xY0E6LxkWAttdiqqbb54khJfGfuYjLONak19AXSMpOPKZpSE2bNuPYz4a1A_lwG7u0CZXaTKbuBuwrdsvE8TMN-fjEun0KK5-1O4SVqrSQdLw5x183e-19-dRoDKWYg-Vg6Wu9wZMPsBwcKfPziqIKAtcoGJj9nYukrz6NVrfNzP4_T8awS5tpp--4hJ2C8xca6yNoB_xdXRTiXFeh7HCcmdgHGldhplFBYl_IHwOOj1DQ_H8GOVxZss1JhZRWf5f7XfSY4_t4L8rbvVkVp7OUp20mXTqgS5fosw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uyzNZYbJL6SeWMnTC4fQ1OQc5AxdyelGJOQcpvhXCBaY60Uz53epK9BPwi99toqMYzqCK06_yiY3GTAuRUPBOfqi5jXFu4rJ5Kmyt5cm-kmq92LVv4m9qOSFBAq_AsXaE1JSayk71Mnzc_lW8s7KE-sCoQh8fVeXGq8gm3dLy7kJ0MwzAha5LDfqTE4thT9cqalHBH4R2s_kVQias0-AVbSDaviob1monZ9BCysdsbArLYZoY52ed9k0y76JegT8lynzz5JfGEs5fwaDfviS0mf4X63AawKwgsRmlXM9v7nXJB_O3pz7ZwbKkxSLwUE6do-qui_MXnRnVt5dPkMilg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e-_QdWvPJs5YDMX8VWviNm4k2vtbZi2OcH1IXqsCq41FhRoOqiB4f_XDEUQEuSKLMDFVQX253w4BaNT7s5l5F6Nt2ERs2dqA9tR1XijbzvKxtDnva9TMD8P4ml7sIR1mKo2fYuMusaMzkKFRims6wDM6hPTGu3__xQMqB-lTyeImOk7OMi2YRTAoU5SQdoadT2_G-F97Ycq7HZXOvO5zLGtQN3ztD84OrgwS6Teb934XZeae8S8a4cdUgSsYQOKZUV2koh_z2n1HdeArP_8chy68I-CSi3oLHdInSmbWlNuzruzd4bPtC62dmabUWqOjZMewBYbpkbNHT7e8-XSvbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭕️
شب گذشته در بسیاری از برنامه های صداوسیما، مجریان با تفنگ حاضر شدند.
🔴
نظرتون رو در کامنت حتما بگید
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/120385" target="_blank">📅 16:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120384">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
منابع رسمی پاکستانی به الحدث: اسلام‌آباد به دنبال قانع کردن تهران و واشنگتن به «انعطاف» در مذاکره است.
🔴
اسلام‌آباد به دنبال ادامه روند میانجی‌گری با تمام «جدیّت» است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/120384" target="_blank">📅 16:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120383">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mx4rUCO777iVtD5akuXwdJfS12WR0U7e1Zyf7WVXoxXM_vUww_M21c0JXHbTseNyAWeYVkJeajeDsCNN9PnvbFkDAlv5J_q9Z9G9VOcvgiUmeWO9-9OEY2yniuxmDb827oJFCtfPhKVeb7Oyz0n6iZxL6rDR39nD57cDpHCgI4UWJggzWiNc68zoT41LT1qlz1meskwFptng8zTMfXk7asGXJXgx8_Mz1IUilKGnfPFpPvRBjQPUG739ifmpFkd6a65zOogd9-MU5ZKLYtAma_YTXsh4ACE3NNjlt_3KDsj89j0mV6ZbJGRjf5Cv4vn9u0OqKLZGKH5_02hf5E4R-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قطعی اینترنت وارد روز ۷۸ام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/120383" target="_blank">📅 16:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120382">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5b602b82.mp4?token=PWinXQMQ2KuQ-JrCgRfOOCXCWwJ_Dh0FXJ5eRO4GAaGNWz59dGaLC3a8ntMCt-Zh3Ka3-QHdWBeNHlNKFgR4pvwbbhl714czaWWJabWii2qkKBMxLjFOsDI2h0jlOtknMBa8sD45KOM_6ncRye5-xAAe2v9NyZ2wVlWePepXJQO607hRaGclbTZCGM055izOeWe_kIx2etCV1reYQqMSQj5KAr2aAABsPfItOyZJ3aXT324_oBdVeGeRn61cnyeGDC2oaa1fEY-2lYPcKvMXChVBlYc9OffkGrtxJodVjxHdxG0-D9x0d4ALhUovoKS8kc2txvCX3muWAaUlRAQZbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5b602b82.mp4?token=PWinXQMQ2KuQ-JrCgRfOOCXCWwJ_Dh0FXJ5eRO4GAaGNWz59dGaLC3a8ntMCt-Zh3Ka3-QHdWBeNHlNKFgR4pvwbbhl714czaWWJabWii2qkKBMxLjFOsDI2h0jlOtknMBa8sD45KOM_6ncRye5-xAAe2v9NyZ2wVlWePepXJQO607hRaGclbTZCGM055izOeWe_kIx2etCV1reYQqMSQj5KAr2aAABsPfItOyZJ3aXT324_oBdVeGeRn61cnyeGDC2oaa1fEY-2lYPcKvMXChVBlYc9OffkGrtxJodVjxHdxG0-D9x0d4ALhUovoKS8kc2txvCX3muWAaUlRAQZbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو منتشرشده توسط ارتش آمریکا از عملیات کشتن ابوبلال المینوکی، نفر دوم داعش در نیجریه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/120382" target="_blank">📅 16:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120381">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04afd7993a.mp4?token=DAMti7uvu3QHDDFD4Uu1S5s2EmitkKaqB8G1e51LxMlEYE5TVFpdQY-JZhS1bZsIFleG89WqEnnHwtjc4haecJP9atA98N1X78RLeCDhoOEBOwZTnJLEoYmtYoC66Sh-EfVfxGeE7fgvbkFTSpf0gAhFyc7KwQ-RC-ymtedB-FK4-PcqdCA9SQpbFMfl0PoPUgAm8X84z3sknUoPqyQk8JigZLHRXHXVSK4Zqej3cTMm8_XPI3e_QzHtLfuRiMLdpxfeWRO8cYP2N9VWlKiBLgp_mRfpaoFqY8yfptR2vCQkQZTcCJNmng0A7rosgtXj_odwKshJsL7ZoOnyL0n3xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04afd7993a.mp4?token=DAMti7uvu3QHDDFD4Uu1S5s2EmitkKaqB8G1e51LxMlEYE5TVFpdQY-JZhS1bZsIFleG89WqEnnHwtjc4haecJP9atA98N1X78RLeCDhoOEBOwZTnJLEoYmtYoC66Sh-EfVfxGeE7fgvbkFTSpf0gAhFyc7KwQ-RC-ymtedB-FK4-PcqdCA9SQpbFMfl0PoPUgAm8X84z3sknUoPqyQk8JigZLHRXHXVSK4Zqej3cTMm8_XPI3e_QzHtLfuRiMLdpxfeWRO8cYP2N9VWlKiBLgp_mRfpaoFqY8yfptR2vCQkQZTcCJNmng0A7rosgtXj_odwKshJsL7ZoOnyL0n3xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از عجایب روزگار اینه تو مراسم بزرگداشت فردوسی نوحه پخش کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/120381" target="_blank">📅 16:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120380">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256a5b96d9.mp4?token=nFA61o59H7UYQbX2XeRhCQQWwGOZIrbLGmwMhMsTTl-KXulwFhbxbO33nDosw-lJL87JQ_OhVBczm6GQx9hwgGr7PdGehrjaY1WpmYQwYXYxUR9BhxRLWIeJgrki47MLrZfjQiVrmex3FFc1U1DecgQzKOUCcOQIoombvJDgN1fHDQwP6iHUex-TyQfJSQmr_iWzwfJpZJTPaPPRy6XO0anYoIRjnC81cuM4SdS7GsKw2H_C99JLfNQQEofXpIXPRiw7eXZQiB_f_wBJB1JMF_nuVKETe6kCLtFrytg33onaCq_T1UbE-ItFQMmWj9YtcVXrX7CLMbWjWC2zK5o3SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256a5b96d9.mp4?token=nFA61o59H7UYQbX2XeRhCQQWwGOZIrbLGmwMhMsTTl-KXulwFhbxbO33nDosw-lJL87JQ_OhVBczm6GQx9hwgGr7PdGehrjaY1WpmYQwYXYxUR9BhxRLWIeJgrki47MLrZfjQiVrmex3FFc1U1DecgQzKOUCcOQIoombvJDgN1fHDQwP6iHUex-TyQfJSQmr_iWzwfJpZJTPaPPRy6XO0anYoIRjnC81cuM4SdS7GsKw2H_C99JLfNQQEofXpIXPRiw7eXZQiB_f_wBJB1JMF_nuVKETe6kCLtFrytg33onaCq_T1UbE-ItFQMmWj9YtcVXrX7CLMbWjWC2zK5o3SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شلیک رگباری در پخش مستقیم صداسیما
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/120380" target="_blank">📅 15:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120379">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsMnvoBljQPIWfG3zp54CXziMUiup46vJXuZqMJyDaRsw-1ldUcwSSNsZN1GjGg35p50rjIw6sROXrRGTxRJY6-TfxUrqUtkpPuXyyeimwT14StycbVrN_KSdP-eOQYN5aaLuX6nKEb_kuq8iJAI70CEfWPguj5S2YHIwhpLS5SKB8tQ6ky2bnkOv4bg1NKnCXxG4Uyaz063Ako1Fi6_Ct9sy4Pwba8C4U1stamiZA_lAPU0hSmWsJ-_ATaaNZu8bwlg8PrxNo5dHEJROR_s7J49zVMygtyWbfATUyRD9y68OJxmApJ1sj3Gbk4wQNATvT9AZRhzJrGJsEBOmfZcyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اردوغان:
مطالبات ما روشن است. ما اف-۳۵ ها را می‌خواهیم
🔴
همکاران ما به تماس‌های خود با همتایان آمریکایی‌شان ادامه می‌دهند و امیدواریم نتیجه مثبتی به دست آوریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/120379" target="_blank">📅 15:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120378">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnocWhzMiJoZfZ9kyfuEveNWO8aA5xHkJGNPW8wrTObWfVXAlP9n1bQKdl-32KJIlRmrWTuQROhSSxEFpvrPOsXc8rrFgQ3LITVjNQ6TazFeAF8S4xEt67tJusyQq72K3gWAQGCP-ZLCO7UJ0rE9OY4f37ncOPTv_GUH2xzmPJsK-ftpdqAZEdSDesw1CaeLJgFV1BkevZ5ZUA3Q-CEiumm1ENnaCOWgn3GKA7s4Hwwo1vIVslemLEwgmPh-Jk-wk1J6FGWXhSzAonrWrhwPJhbEl8nQS1VJT6A_TTIrt5f0xBg5I_2INATxiMiL9z_18jukSMXsomk1Xv5_YXM7xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۰۹.۲۶ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/120378" target="_blank">📅 15:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120377">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری/شبکه ۱۲ اسرائیل :
اسرائیل در حال آماده شدن برای یک جنگ چند روزه یا چند هفته‌ای با ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/120377" target="_blank">📅 15:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120376">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⚠️
توجه
⚠️
بچه ها فیلترینگ خیلیی شدید شده همین الان که اینترنت دارین حتما جوین بشید و از کانفینگاش استفاده کنید که موقع قطعی خیلی به کارتون میاد
⏬
https://t.me/+WgqzouUHJ1U3OTY0
https://t.me/+WgqzouUHJ1U3OTY0
https://t.me/+WgqzouUHJ1U3OTY0</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/120376" target="_blank">📅 15:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120375">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
جاده چالوس از فردا به مدت ۴روز مسدود می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/120375" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120374">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
دقایقی پیش وزیر کشور پاکستان برای دیدار با مقامات ایرانی، در سفری از پیش اعلام نشده وارد تهران شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/120374" target="_blank">📅 15:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120373">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2GBFJN0ytOepQBeSgIR1fCnrERTQ-V1WMevbomIIOuM2XYlYysqOiOxesRHQSZ6lmpmPuBN4iT8wnX1MgocDQrf-tL48Vl4autfVwLFZpwksP4Zt7D6NjDP8F7-PGmlN7fqjZ2LPqEClN4sXfIB9Ac8hta4hobG8sBO4KcJSDE9yLUvpTdCA-K8kh8AuBJc6kUdqP9QporxCBNHouTbH1XrAcVFtZ2eLnElhvJpGNnhq7TsaDrpl6R0KmjK_L_UpPIecFqB7E06mlKfKMt8e7gSRwQV4Oy0x_3h0d-7dM6L3SBuLLbdEB316R2lDrpBDnNkqf8DiNYRcED4v7I7IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مخبر: این خویشتنداری همیشگی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/120373" target="_blank">📅 15:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120372">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل اعلام کرده است که حملات به سایت‌های زیرساختی حزب‌الله در چندین منطقه در جنوب لبنان را آغاز کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/120372" target="_blank">📅 15:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120371">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
دقایقی پیش وزیر کشور پاکستان برای دیدار با مقامات ایرانی، در سفری از پیش اعلام نشده وارد تهران شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/120371" target="_blank">📅 15:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120370">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس :
یه سیستم طراحی کردیم که رفت‌وآمد کشتی‌ها تو تنگه هرمز رو با یه مسیر مشخص کنترل کنیم و به‌زودی هم اعلامش می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/alonews/120370" target="_blank">📅 14:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120369">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
به گزارش کانال ۱۲ اسرائیل : ترامپ بزودی با اعضای کابینه خود جلسه اضطراری برای پایان دادن به اوضاع ایران برگزار میکند ، حمله و تقابل سوم قریب الوقوع و بسیار نزدیک است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/120369" target="_blank">📅 14:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120368">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
الجزیره: وزیر انرژی امارات می‌گوید خروج از اوپک یک «انتخاب استراتژیک مستقل» است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/alonews/120368" target="_blank">📅 14:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120367">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
از دقایقی قبل سوپراپلیکیشن بله با اختلال مواجه شده و کار نمی کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/alonews/120367" target="_blank">📅 14:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120366">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdMXzPeXP7c-9wgefCABkwnw2Vso4_h9BL3_i3ZiisM-TMhWX_uOCSFcvgU7rawsgbfVinZvSUEl63oDYhsv132ygsOnDrLYYBeXjYseOgdK3nVrVpOQHkWNGPl3sUo031cDR85QiCku_PI5BHc6Sboq9JfiutsiAFyHa5FI2VIyTWlSjaOG7dZfept_DY6MYoaWkIHowqTBMbn8QQYH7qfoSaXFjj9GchwJf6pY4pxDgtVE-DqphDpUitt0mUB6RT1t2HuIpyctwpQxNaNDQh7urbLXYFMnIXy014KmV7D2VvtpDfrVqXRqFY7vHzXxkCwEOtU8BGWNPKgwBWvsPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فارس مدعی شد: یک نفتکش غول‌پیکر چینی که از تنگهٔ هرمز عبور کرده بود، خارج از خط محاصرهٔ آمریکا رویت شد.
🔴
این نفتکش پیش از آغاز مذاکرات رئیس‌جمهور چین و ترامپ درحال عبور از مسیر تعیین‌شدهٔ ایران در تنگهٔ هرمز در کنار جزیرهٔ لارک دیده شده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/120366" target="_blank">📅 14:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120365">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOwH0iuGkgXCwiYSx5BWLvn4bVKL7MHY1AypwAHP387lWCeASEW24H6e9pfQIixxr0bmr46Y6pqYaNw_FgICv6UX28r-XdZ09wamP9U7yxGL2XZL4kb0kidjvU6OaLHOiF9iyyPBIScVPbank_-C0I7qtyS3NSvlhdqMrZjVumbYXDHVPkM54nIh51fv94dbMDCBMG2OuPHP1V0BujkIk87CMB0zGkCUpEYR5nRkQ70xAVJZLy5x2FgHz4AQWfwyr6jl2Bp-5E_3pKtRTvGP_z434oyV8eUjvT_Bu-xF-IgbzuI9Za5HzafTbnvqUvTaocXKU64FXKxvGkCa7SZTOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناو شارل دوگل فرانسه، خروجی خلیج عدن - ورودی دریای عرب دیده شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/120365" target="_blank">📅 14:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120364">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
فرماندهی کل نیروی دفاعی بحرین : برای حمله احتمالی جمهوری اسلامی، تو آماده‌باش سطح بالا قرار داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/alonews/120364" target="_blank">📅 14:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120362">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
فوری / شبکه فاکس نیوز: ارتش آمریکا درحال آماده شدن برای دور جدیدی از درگیری های نظامی در ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/120362" target="_blank">📅 14:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120361">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
امارات مدعی شد: خروج از اوپک و اوپک‌پلاس نشانه اختلاف با شرکا نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/120361" target="_blank">📅 14:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120360">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
یک مقام مطلع نظامی به نورنیوز: در صورت وقوع جنگ، اهدافی که قبلاً مصون ماندند این‌بار در تیررس‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/120360" target="_blank">📅 14:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120359">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سی‌ان‌ان: مشاوران ترامپ خواهان پایان فوری جنگ هستند؛ فشار اقتصادی رای‌دهندگان را نگران کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/120359" target="_blank">📅 13:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120358">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
مهاجرانی: نگاه دولت به اینترنت دسترسی برابر برای همه شهروندان است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/alonews/120358" target="_blank">📅 13:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120357">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزارت دفاع اسرائیل می‌خواد برد جنگنده‌های F-35I رو بیشتر کنه - DefNews
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/alonews/120357" target="_blank">📅 13:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120356">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c1198d606.mp4?token=DJkwlSBVW9hjWcs9Dv2WGky4D_9kjqFcsXI3Ikw73wPehaN_XIhOpDds7nSlr1M3Vg_f813cgaluwyJf4rfn2Nu2_Ct2oqbr7WjtheUdOM0JHEKyVcSidxRxka_pWiy2tUjGl7_yfeKanuRi8o28rMJDuWPOneBVHPO90T17hoenteiXLOJBMqIDiSBbuBQtuDrcyUK_gcYXJ3uQFK7Hs7hYanmIAXj0x-K8tGtTFGzQNBjUCYklJoRI_uQlqC3u5Y8ugVBpjCatjYDyV7vJXoXEdsfk5uO8hzd0vQgqepmT_LDp7BjdK128DJ2JfmkLsFV5CFJq0nFYXR8prySwzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c1198d606.mp4?token=DJkwlSBVW9hjWcs9Dv2WGky4D_9kjqFcsXI3Ikw73wPehaN_XIhOpDds7nSlr1M3Vg_f813cgaluwyJf4rfn2Nu2_Ct2oqbr7WjtheUdOM0JHEKyVcSidxRxka_pWiy2tUjGl7_yfeKanuRi8o28rMJDuWPOneBVHPO90T17hoenteiXLOJBMqIDiSBbuBQtuDrcyUK_gcYXJ3uQFK7Hs7hYanmIAXj0x-K8tGtTFGzQNBjUCYklJoRI_uQlqC3u5Y8ugVBpjCatjYDyV7vJXoXEdsfk5uO8hzd0vQgqepmT_LDp7BjdK128DJ2JfmkLsFV5CFJq0nFYXR8prySwzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های جدید "MiG-29" سوریه رسماً رفتن تو عملیات و دارن برای دفاع از حریم هوایی سوریه پرواز می‌کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/120356" target="_blank">📅 13:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120355">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
یک مقام ارشد اسرائیلی در گفتگو با کانال ۱۲ اسرائیل: تل‌آویو در حال آماده شدن برای یک جنگ چند روزه یا چند هفته‌ای با ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/120355" target="_blank">📅 13:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120354">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ: ۵ بار با ایران نزدیک توافق شدم، ولی روز بعدش زدن زیرش
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/alonews/120354" target="_blank">📅 13:24 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120353">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
حدادی، عضو کمیسیون صنایع: گران شدن خودرو توجیه فنی ندارد/قیمت‌ها باید به قبل از جنگ بازگردد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/120353" target="_blank">📅 13:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120351">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/120351" target="_blank">📅 13:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120350">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVarzesh+plus | ورزش پلاس(K_B9)</strong></div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/120350" target="_blank">📅 13:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120349">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل : عزالدین الحداد فرمانده گردان‌های القسام، همراه با محافظ‌هاش ترور شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/120349" target="_blank">📅 12:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120348">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
وزیر جدید نفت عراق، باسم محمد، اعلام کرد که عراق در ماه آوریل/نیمان ۱۰ میلیون بشکه نفت خود را از طریق تنگه هرمز صادر کرده است.
🔴
وی توضیح داد که عراق قصد دارد با سازمان اوپک همکاری کند تا تولید و ظرفیت صادرات کشور را افزایش دهد و افزود که بغداد هدف دارد به ظرفیت تولید روزانه ۵ میلیون بشکه دست یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/120348" target="_blank">📅 12:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120347">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سنتکام به نیویورک تایمز : کشتی‌های ایرانی رو با ماهواره و چند روش دیگه ردیابی می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/alonews/120347" target="_blank">📅 12:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120346">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
منابع پاکستانی: سومین کشتی گاز مایع قطر با عبور از تنگه هرمز در کراچی پهلو گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/alonews/120346" target="_blank">📅 12:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120345">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
قطارهای چین به ایران سه برابر شد
🔴
با وجود محاصره دریایی آمریکا، قطارهای باری چین به ایران از هفته‌ای یک بار به هر سه تا چهار روز یکبار رسیده‌ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/alonews/120345" target="_blank">📅 12:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120344">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سخنگوی وزارت کشور: از نمایندگان مجلس توقع داریم در اظهارنظرهای خود در موضوعات مختلف بیشتر دقت کنند؛ انسجام ملی باید حفظ شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/120344" target="_blank">📅 12:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120343">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e175bcbc6c.mp4?token=mhrpRBS8HulmpY4YvfDVhnzBf7f25r8q-whK0jk4jqzFLlp6jw2jzmnUmKuSNNW90zu-azM-PqN7HFCE-T8lXKvyS0oCnbHRzZyg9bBTXOBmQHO5mXu5VPSk9Psw6AkfKU2y0WolXv4b45L3x4gQcM7fy5oS4sJgbbJjyBx5DNQ16lYlbxDbUhL6X27yENUThEx8HDxbmN8yQTN2VoJKTwQJz3c54kXowSihtMx1-Ev2cCHxD9026Y55zxw_HsN6BIFaK2B0r3zhWa-tc2qX3nPA2WplHEeNARiPnXrwMZv7SxonbvGkC4PTZPzqMConJ3bsFnyiQKrSZBPeK-CnVg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e175bcbc6c.mp4?token=mhrpRBS8HulmpY4YvfDVhnzBf7f25r8q-whK0jk4jqzFLlp6jw2jzmnUmKuSNNW90zu-azM-PqN7HFCE-T8lXKvyS0oCnbHRzZyg9bBTXOBmQHO5mXu5VPSk9Psw6AkfKU2y0WolXv4b45L3x4gQcM7fy5oS4sJgbbJjyBx5DNQ16lYlbxDbUhL6X27yENUThEx8HDxbmN8yQTN2VoJKTwQJz3c54kXowSihtMx1-Ev2cCHxD9026Y55zxw_HsN6BIFaK2B0r3zhWa-tc2qX3nPA2WplHEeNARiPnXrwMZv7SxonbvGkC4PTZPzqMConJ3bsFnyiQKrSZBPeK-CnVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: نام افرادی را که در نزدیکی اورانیوم های غنی‌شده ایران هستند، می‌دانیم. پنجاه درصدشان اسمشان محمد است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/120343" target="_blank">📅 12:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120342">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQPFfMyRnlpLOS1j4Wrwct1KtUIs5si9waQcyif0X7izPLuNfbjtXNyLYXDX51JbNcyaOOGmSQ-egrX6f_8oN9PkKKCtLd_6pr7k8EySTznZXZbfLSDTStOfj_fCpcxqKWhHSbhSvVTs3ReqEI_hSD7oRFES-ilSRu2YyckXnUsN2IojyVtn1RqhLaxjA46tIHT2ciuSmQyzcy84yW9_tphEMSW5c6SXO6sHhPNmmD_GNIi0kxb5Gw9-FwBVZ2DuU8EXeuqZydM5vGFMo202WQexejYWPV0MxpsMLjIUUYxnjIVsVl1z-aOYYhqDsILR8l1We-jxTOgbP7Sho8d8GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پراید هم رویا شد ...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/alonews/120342" target="_blank">📅 11:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120340">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rren5iiHYOJYbtp7jtTkeIbVavWYri2_BMfq0VSG26vrC5_V5k1aBQ_zBpwvzx8OWha50R0Q2PHv_h8LWGdawuU_vMFeqhum2ph5QggMVnnfuN_F_e34IELhQgEoAP5dn5KupjCG_eyzJRdSeSvJuKp4NtOOND57LguYuXJH64VxPaWUfZsj3SoMNTeAIJ6bASFzIRMdAsAMF2Oa_UDodin9o-4VjheBogHYuIS3st1jjgewgNEH9GuiRFTIZODD4xBqSL6-mYAEB4M-fmjwyse_SQvC0qN765kx430cQ-S7ruoYvSgc_HJFA0Jw403B3xzOKJ6NLziJxfXhdfnexg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cvN9LQx38hFP9rg2BojBw72HWkLpr1ZtN0ol8WZIXM-1nnu9uCJ5rpaz0EmzezV2N7di3GTusbSNJv-17WfGiCSxeqNcEytvKd_W5FUt6TRFQAgVP9EDK3Tibf5j7BKzDN5853JvnzvSireIlso5x4HYypbE7iYV7m2LHbmh9x851b_L22a27IGTYcyuO2zXqbaAUYRxVznaddIq6V8TtR5DpBgNzn8POdI2B3rfnNfOQQNdHxuc6lPsLVKuyGoHcWgcOgFwpG64GqbDnEg8VY6JypjX3aMU3Hw6wqzv_H0oU2OVj2G8RvHk4Xr2EncF9l7Zm9MrDYVmICx8vZCYdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ارتش اوکراین بامداد امروز با استفاده از پهپاد های خود حمله‌ای به یک کارخانه شیمیایی در منطقه نوینومیسک انجام داد که این کارخانه به طور فعال مواد منفجره را برای صنایع نظامی روسیه تولید می‌کرد و همچنین کارخانه صنایع فلزی متالیست پلاس در نابورژنیه چلنی روسیه نیز مورد حمله قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/120340" target="_blank">📅 11:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120339">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O20O1L1WsWwfF3Mjc3dtPTMVvqDSBHBP7EtwiAP1DkMV6Ps_hpmo4IGBUpxESfOLzFc2qsnFXf_K517ZkZIZA98OjveZiDtsf4J-ZtEw26HeRWMSIWab4qalExO8siefUrGbUJlbcOaC_dSZl89g6n3m2onhjRT5hXcmJAgGZnwrr8Fk0kcGWD3Z_tEcjMkBRJQP22v0PHaa30OPl5MZMe4wn0VcXxscyRzOw1jQB2bTzJCg9SAbGo3aoA3AtaMZI7gf2d-2Q7fCmhmu_dt-NSFy4EF7nv-l31VXELDjb3R8ybXF4zfAi6u5ccWKYtoQlaeoHTJDTS_fnMDmoOF0iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تایوان به ترامپ و چین پاسخ داد: ما تابع پکن نیستیم
🔴
پس از آنکه ترامپ بعد از دیدار با شی جین پینگ گفت دنبال استقلال تایوان نیست، تایپه پاسخ داد: «تایوان یک کشور دموکراتیک، مستقل و دارای حاکمیت است و تابع جمهوری خلق چین نیست.»
🔴
این پاسخ نشان میدهد تایوان نمیخواهد در معامله بزرگ واشنگتن و پکن، فقط به یک کارت مذاکره تبدیل شود. ترامپ با احتیاط حرف میزند تا با چین وارد درگیری تازه نشود، اما تایپه هم میخواهد روشن کند که هویتش را با سکوت دیپلماتیک دیگران تعریف نمیکند.
🔴
برای پکن، این جمله تحریک‌آمیز است. برای واشنگتن، یادآوری دردسرساز است. چون هرچه ترامپ بخواهد پرونده تایوان را آرام نگه دارد، خود تایوان نشان میدهد حاضر نیست استقلال عملی‌اش زیر سایه توافق‌های پشت پرده کم‌رنگ شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/120339" target="_blank">📅 11:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120338">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">قیمت استثنایی گیگی
2️⃣
2️⃣
2️⃣
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
ضریب و این چیزا…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/120338" target="_blank">📅 11:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120337">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/120337" target="_blank">📅 11:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120336">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ls958bHLXTVKGAaBhohke8KDEPSfFTzQRzipA6iFAlZVc-RKwRN27Gl3L-HUGhDdBDvzabZwO7_fGDIK1_lSJ24Fq68BixkSZeUj1o2BOLf6a4Opmxj7upkt-xlFb1A1BsgM5789oBLz02NSNYK39mphRuYK2n2UEXO-7jSOBKbQxqHGggIUWQ4ecWpPIYaV0xy31ywWT02sSoFYvhFn5cbxIQnK6l8gpZl2HWQIqTmFv7gBH0CwyPd9eHWhNjPN9lpcdUavZ9J0eiLwtLrKi-rAgUJaPaDC46n1CrrBrDma30tSVXVu6M-tfdag7BrH1bHnOS2wNojWQ-U-gR4meQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دوستان این تبلیغاتی که پائین کانال نمایش داده میشه کلاهبرداری هست و توسط خود تلگرام انجام میشه و از دست ما خارجه
🔴
به هیچ عنوان اعتماد نکنید چون سرمایتون میره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/120336" target="_blank">📅 11:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120335">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
انفجار ناشی از امحای مهمات در دزفول
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/120335" target="_blank">📅 11:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120334">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2mhTc-JUgbIrorzKoMYvfhtP_N6rGJOO85-7610FcCNN81iJZhDVKHltUF3pNtj0YTShts9Rn5usmfvF3UdyCY6lX6gyU8fnszZJ6nVZSC-5nfI2VcWEL8KL20kRVPTDBVxCWJ2ctzfpcSf7CGvUPwCki9I5Um_Qtyf4ITKRs59mheWmEl3pwfbT4WEYYj1csGZiyuPGt-1Jq7GlCJP5DsHFosNNLk697jz0tG-aveb6B2MMET4dzCGtbbzOAHsf0krmFlq8JuJ-8cpdbjULJ-jSMnh_3QS0_EZbKc-YJVCufC0gPHlg299e3ZKog8uHsPBcVczwGlnV9rdZTu_GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی گیگی
2️⃣
2️⃣
2️⃣
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
⭐️
@Napsternetiran_bot
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🔶
@Napsternetvirani</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/120334" target="_blank">📅 11:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120333">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ارگان رسانه ای وابسته به سپاه نوشت: وزارت اقتصاد طرح مدیریت تنگه هرمز از طریق بیمه را پیگیری می‌کند تا امکان مدیریت بر تنگه در پساجنگ مطابق حقوق بین‌الملل فراهم شود و برای ایران آورده اقتصادی نیز داشته باش
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/120333" target="_blank">📅 11:16 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120332">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
الجزیره: برق کوبا پس از خاموشی گسترده دوباره وصل شد، اما بحران انرژی همچنان ادامه دارد
🔴
برق در سراسر کوبا روز جمعه پس از خاموشی‌های گسترده دوباره برقرار شد، اما بحران انرژی این کشور با کاهش شدید ذخایر نفتی همچنان ادامه دارد.
🔴
شرکت ملی برق کوبا اعلام کرد که پس از قطعی برق در ۷ استان از ۱۵ استان، «سیستم برق ملی دوباره برقرار شده است»، با این حال قطعی‌های برنامه‌ریزی‌شده ادامه دارد و نیروگاه‌های قدیمی هنوز در دست تعمیر هستند.
🔴
وزیر انرژی، روز چهارشنبه اعلام کرد که ذخایر نفت کشور «تمام شده است». کمبود انرژی خشم عمومی را برانگیخته و شهروندان هاوانا با کوبیدن قابلمه و ماهیتابه اعتراض خود را نشان دادند.
🔴
کوبا کاهش انرژی را ناشی از تحریم‌های آمریکا می‌داند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/120332" target="_blank">📅 11:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120331">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
آسوشیتدپرس: بازگشت ناو هواپیمابر جرالد فورد به پایگاه پس از ۱۱ ماه مأموریت
🔴
وزارت جنگ آمریکا اعلام کرد پیت هگست، وزیر جنگ، روز شنبه در پایگاه دریایی نورفولک در ویرجینیا از ناو هواپیمابر جرالد فورد و ۴۵۰۰ ملوان آن پس از ۱۱ ماه مأموریت استقبال می‌کند.
🔴
این ناو ۳۲۶ روز در دریا بوده که طولانی‌ترین استقرار یک ناو هواپیمابر آمریکایی در ۵۰ سال گذشته و سومین رکورد از زمان جنگ ویتنام است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/120331" target="_blank">📅 11:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120330">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
کپیتال اکونومیست: قیمت نفت به ۱۵۰ دلار در هر بشکه خواهد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/120330" target="_blank">📅 11:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120329">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
نیروی هوایی اوکراین اعلام کرد: 269 پهپاد از 294 پهپاد پرتاب شده توسط ارتش روسیه را شب گذشته سرنگون کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/120329" target="_blank">📅 11:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120328">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
نیویورک تایمز گزارش می‌دهد که نیروهای نظامی آمریکا "در حال آماده‌سازی برای دور دیگری از حملات هستند... این بار با شدت بیشتر. این حملات ممکن است از روز دوشنبه آغاز شود. اهداف نظامی بیشتری از ایران در نظر گرفته شده است که شامل زیرساخت‌ها نیز می‌شود."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/120328" target="_blank">📅 11:01 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
