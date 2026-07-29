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
<img src="https://cdn4.telesco.pe/file/fNSKPssqGp-J022MFKOn5rqRsVxQHl1yuOtd7MXhLLqKrMZSt1y1C5rHiigsUaoh7ju0inEvlGOTLPwvkWfKTJGMw7YaKuCzQcpiFRqNQKW_58wj3b2kZ0H5vC6JkkSCsL-wHa-tvJJqxUZXuKLRhN4JQKVcwM3Nwze4HWh1I7as4e4EZFZl_oTvdZQEsMyZFEcaURr77igvhKkOg393_1d6Gf7VCHzkQsxSGuviq3Ar19EdS95pFgcexWsjAPfLCuHE-_E4ng1yPFxL0uTfIrlCqYdZX0idBW2I7PdRar2MZD5SHT-dPU2IJ889UIwJZYJucetctHuUnskSu06AZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 221K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 16:32:15</div>
<hr>

<div class="tg-post" id="msg-81478">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZk1Hb0oj8sJO_Mx-VUKTX_sXnIIKjERU12iK9mpcRmMSrd-GlOPXep8rY5ExfrBYw06wqox1rbag9BEtQZ0jkYHaOT4IU8AOqDwDGV7G77UDoel24Up1_5RyYvAr8HddwTxkGz1CKDiriVFY1h-cPd5XQmDOlwxMCXqRRSFFXxhj-eJqaoqwogGhKeUMtTLty86gJNGGiTr_bKQo4z9i2OG1mYqxfVpwnktANUe6KrrvYImGCJ_a6jFgkkZpNKAWME4l8214AP1X4z0fmCZFv8O73DTh49mUcgRHyADxWlLY87GOegWVItSXUNmNaeq1L8hyfe32ppzedR4cI4_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/funhiphop/81478" target="_blank">📅 16:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81477">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ: ضربه سختی به ایران خواهیم زد‌‌.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/funhiphop/81477" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81476">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">منابع نزدیک به سپاه میگن در نتیجه حملات دیشب عربستان و آمریکا در عراق، تا این لحظه دست کم ۵نیروی ارشد حفاظت اطلاعات سپاه کشته شدند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/funhiphop/81476" target="_blank">📅 15:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81475">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/funhiphop/81475" target="_blank">📅 15:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81474">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/funhiphop/81474" target="_blank">📅 15:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81472">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDl-nxz31RY4sekxZvBCxbWLzrbPApDauf5_-2kHU-5Y0ryALsC6H8SuZbBEjqjz9tAy2cmxH0PiSb3IBobqYm4uhFFUs_Fo1D_oJhSZu4Rd0jcluHUYQLVUiUXKves3e2LwKedE8lhz6TVhMUEpXRvAV7NuL6hOozyuVEPJefXVI8fcQDVMKyvGcokkPBWRfY1DFUgTyY1pDgg-pYeICIy9tIClKdL0hBGJX6O3cdcNYTq6cdKHgbzUcUnOjMEu6OQ-ODm7p2VXJ22Sn-BlOGAT8tNJ3371MBfRY4L7Hbojwcw3mm8EvIJLEKvz8mEP3sapN0jpAWFKRa438Zoo5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس نمیدونه چرا این پست انقدر ری اکشن "
🤣
" میگیره.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/funhiphop/81472" target="_blank">📅 14:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81470">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kum7VWVCAZiZyyD59WjVptejfvxTt1eUqFsxcgI32qCpg9jO5FwGSCiUOCVbV_-PRe91MWX7SLaD6eY8bPdv-bjfZDG2Yho18fscw1L0ZDbdgVUoljQoU2z2JoiRllI5qh-ZT1tGkMPbdnteA3bua7-agvRqNFW_vChY6izX0yEOPhBSnV3DznblkwZkqZR-OCgWyJMoulKLIi_L8IwRr7CshrdB0i2eWImLjQT7pURApF63HxSkNNX7wdDUL-dkSGBGj6y4QGIERl8r2Qo5llggHezTfrdgu658I_WriYNOXgiv69qtnGV5h6xEH4lx65pT3FU3wQ3vQlHznuUq-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p4z7cFiTeUMXLabEMA5SXt_cQotARivdn3cpeEJMOeg3S_iBmZcTwnWLTVuiwHSepa88F7yRFwc6Yel1i3cQJgrfd3LPHpBcna4gk4XaQlWpLkLUmMlA_BeNat_rf6V3lXdG2JqZuuWKdGAjladFADk4PCTxeP8j0aOmT7ZQpMwnRmsfKyRIGvSwKuLKslq0RrDNPy-SK4RNYxR-2SrOmj1wwhh__Q_CTKtRoKHzhlcl5QZwYJ0BES5hqntysehIECxbAEBH0p360XtYu8oi8ZNuY4UlMosgfQCJUMiICXNgYSREdEvl61Jpiayqz0Ck_tOANV0yJ0WiWZbK1MPE9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پینترست چرا تبدیل به کرج شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/81470" target="_blank">📅 14:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81465">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اگه این با سپاه همکاری میکرد که الان همه تو صف اعدام بودیم</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81465" target="_blank">📅 13:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81464">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81464" target="_blank">📅 13:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81463">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دلار 193
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/81463" target="_blank">📅 13:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81462">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG4Pl1c0zP6QUl9OhppNoEnf6F6fdaXWgM4fW4K5dqyMw6fcpw518-vksHU9bOOEzlxeT9BshU2f5hEEUgfTOFBCV0zyD6pHWt84ux-pB4R6JCxnac2_8utIuz9SRQaaRakH4scHFWmwzgUlsVQkgy7n-zFd4loOCKICPefbymVuQugd-zisiGypf9Lstz2ateZca4R8XCDvWWik7zAZ7McX4ZBp_0u62J7icCcCffcmtc83kEoBsbDdn12bMxRx8uKS4CJK8BUjfzL9oMv_TqvPm0cHnvmRsG-glMsvTFTsOCdP-nBI9Eh8c64r5Mo3y2aN8Z2Q0eS9SNth-7fpdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پیشرو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81462" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81461">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBFaiatpi7OFEpgd7rWtvZ22aJrmCe6wbvsQjj3ctbr9U4P5Ns4vz0HpM8nQtYfHzyGAdnhCQJGvXnlBVTIf_6KnOun3r7s6Vvmkw-b5kaRPQFDQGnyR9EGbpll5FJYaZS2Q0DfEgvY0MLobCiieP_O1Yj2YwjugGGCJar5subyV5DtUu_Oo7SERHBGQqtlMa7iVK8tw7Len2k5tHd5EoNHD7XzhNxTcKuHLsmfNlCPvBlSBEvDxXnyhLsyruf8dqC-z_ui7urM6ddyTLWdtc4NiVnj2p9zZG9FW1JYddVEccNiyHTiTmzt8_5Sugw4djlZBw-XlldJIWtvAyWzqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اتلتیکو مادرید
🇪🇸
-
🇪🇸
ختافه
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
چهارشنبه ساعت ۱۹:۰۰
🏟
ورزشگاه سرو دل اسپینو
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اتلتیکو مادرید در ۶ بازی اخیر خود مساوی نکرده است.
✅
ختافه در ۴ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳ گل در هر بازی بوده است.
🧠
تحلیل خوب، آغاز خوش‌شانسی است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r7
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81461" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81460">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">از الان تا ۶ سال آینده هر اتفاقی بیوفته ربطش میدیم به جلد مجله اکونومیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/81460" target="_blank">📅 12:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81458">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">هدف یدونه پایگاه آمریکا تو اردن بود فقط
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81458" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81457">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تروخدا اسرائیل باشه تروخدا این یهودا خیلی راحت نابود می‌‌شن بوم بوم تلاویو اسرائیلی‌ها مجبور می‌شن از دریا فرار کنن تروخدا پدافنداشون ته کشیده ۸۵۸۷۴۳۹۹۴۴ نفر ازشون مفقود می‌شه کلا اندازه یه استان ایرانن ۹ میلیون جمعیت دارن کلا تروخدا تروخدا اسرائیلو بزن سردار
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81457" target="_blank">📅 01:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81456">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ببینیم از لپ لپ اسم کدوم کشور درمیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81456" target="_blank">📅 01:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81454">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1P-jHLxqAqESux3Mlgz_UUo1cRr4nJFP4JuJd6i6WQrWLYj7LktWhXub0NAbzovyePXlh9ENamE6aLR-zyR_lm1_nflHtJXVwsfuXQGbs9GMWZaxf5tq-d0eeqDoqgJkshP-9ChBNAhwV0O1VSNb6XWLUMfQn5z98kZA6yUHEpEo_w-YDUmcOmvm1FxFYcmyWzGU6OYBimaIovG-2uVP8janqurh_UxguWfZVNECWWYpZJ3TepXs4f7mUXwSgX0FeGfx6JExpbjWz6_RArRt1yZseFLlrZuztpF0cvmWCeaoxpSiTp-SbezS363meG9ujZ-A1x3YlP4is-O6ANqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/81454" target="_blank">📅 00:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81453">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Orsd9WHhucG3uH2dR6yyilDnVkxL1UDR7U922C4N5hHqmqhvmY_a0ZsPnefSQwWzkyD7cjXjGCbT0zexJDYKoJKyN8nJYURlvXlTQ5-Jxyl05zxddsSIVIGGI2mv2TKbMEOFBX8G-EPvvqcFmdhmU0_Q9gK1al13tnh0M0mmui-kHgYdzrx4JPWZ_yT2SHOGcVh_wiuMRhQMxejB2qT1Ed0GVqrEV6S6wT_ZVRU0ZMXSTNh5Xs_LbEHgQ2AnArcnrgKK4Uel6gxsMytjwDNI9B7BZrM2xnUYlWSFkK028Ik5PwsXbFgLd0_nZp0xSU60jVGrFEaYrksp0iRCfMZTfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم" تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81453" target="_blank">📅 00:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81452">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdfDv4SEstWKVn4oQCim5YZX8ZU8Zm8gpaq0M1uh7d2x1vW6zPfmvghbChes-5iR5uub-QGV2PnYSaXh3SMHRM84Z7dJihwOekBz48a0UkyTtYE8VtdPc3SMC-qDuTGuU16G0WRaROSGQXNJsd_2Q9GqEaVwvo_n_17pOezmApX-QVN0oSqgVNwQ3fh3dRVwIZWsN8Jdz_l6gyO2zP_iJ6CR2Cno2KGbWJr6f-utSSohb-srNZE1cbcbXgTYNmA-5ZtMc0u8XW36iObHQnH8LcjyB5GSWB222r61lipv3lQXb4HnWXmqHDVJ1TX6Jzb202-7IaTHo0U9K8mCQp2a7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم"
تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/funhiphop/81452" target="_blank">📅 00:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81451">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">#رسمی
داریوش ترک کردهههه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81451" target="_blank">📅 00:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81450">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvetXyuaYJBn2LR8cmxvn8Zolxm63BEt7sgn8cG6DDQ23hlxZEwQsPkmPTgdtHtVtLXqeMoFwyIYVbg_fd5SE7B_VvC_-FY06y2j8FFH6EcwzNp5bbF4crn6ECApqItfhO3el1teUsk9Zv5RbJQn5iI1Aq7CevDHPTXzQ7q4qT4EVkNc-gtZ2HCSvm4frFHv15Ea4gdmwciT50S8cZ7vH5HmaSh4_Jt4kEX7_IsEuv94ciGqYyT5F9zKh670u8u-4_f8oyjg4voYSoswhPLCMRPxUtuAyIGIgq6qbNVYuZiU4-w1Ngm7H5dPjb0ApADweukEF7wWfK5L1pBBMgaTDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم یادبود لیندزی گراهام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81450" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81449">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یعنی جدی عملکرد ترامپ رو تو اوردن نفت از ۱۲۰ دلار به ۷۵ دلار تو دوماه ببینی و باز از گرونی نفت بعنوان یه موفقیت حرف بزنی نیازمند خیلی کصخل بودنه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81449" target="_blank">📅 23:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81448">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz8lONVKIPB8szW8wugzURwf-HzFe2z-32Izj4-bSEUTIblhMzNjAL2tqUqMqmDrenNW8rWBkKyEaj6kcK1Vj1tuHeozozv_rC1SMRzObeNPCwY99YZDVb2hTprFkWoxyfFELHVb5Fehu_D9GIxz6qtspEh5xeDO8euNa1zvuDY6DXcF0JHly_02BVHNtDaN420P10rJfSk29OHSVzq-bqAmyu6TN-_5e69ndETmk25kMgg_5AXDmLp95FtFQU80GjMxrUW2Fn_Yy8xGwV16Wl27C8WN5Kys6n3jjBeqytrVy7BrfY2BbJLnntiCnrS9naOFKlYYj8hZvagn4XT0qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا سکته کرده، اما اعلام کرده که حالش خوبه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81448" target="_blank">📅 23:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81447">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">قالیباف: دنبال بهتر کردن
زندگی
مردم هستیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81447" target="_blank">📅 22:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81446">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVxZskpReW_JAtOyCabbaWFobgHGhxQ9Nngcux6ynvkv8Z70tGzC1dmnfkf51IqJPWYkTtpm_sZwn7vdA5ynkqoTUwBMfIPj-IumrBqDHMwgW9DJaP9CR2fWWDXZ5QS0Am6NUiPTp6TvaNdotd5kl1scBuJFhC5E1uROsg3T6zCJ7MJ4Ww4GWZC_cFRNvdfnDQcnsbwwIB5XSgORtU9MdRysyDww4aGjlHNn236gF5KPQxCGQiIXSQ494387c3FdQ5P1cjVDcXbrT1CUAqbLucbOgsuQcR2iuLpgkB7qV0IY1XjqlfrwIRIaqm2lWDeb4_WknSAthmiD2Dr80EeNZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعفری دوباره منیجر حصین شده، هم پرایم حصین هم شایع با جعفری بود، با هر کدوم قطع همکاری کرد بگا رفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81446" target="_blank">📅 22:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81445">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromApexNet Shop | اپکس نت شاپ</strong></div>
<div class="tg-text">🏳
سرور مولتی لوکیشن ویتوری موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر نامحدود 90 روزه - 45000 تومان
🟡
سرور 20g - کاربر نامحدود 90 روزه - 95000 تومان
🟡
سرور 30g - کاربر نامحدود 90 روزه - 135000 تومان
🟡
سرور 50g - کاربر نامحدود 90 روزه - 225000 تومان
🟡
سرور 80g - کاربر نامحدود 90 روزه - 360000 تومان
🟡
سرور 100g - کاربر نامحدود 90 روزه - 430000 تومان
🟣
همچنین سرور تست موجوده حتما قبل خرید از ربات سرور تست دریافت‌ کنید و بعد اگر راضی بودید خرید کنید
✅
🟣
برای خرید از ربات زیر استفاده کنید
⬇️
🤖
@ApexNetShop_bot
🟣
برای ارتباط با پشتیبانی و مشاوره با آیدی زیر در ارتباط باشید
✅
👨‍💻
@mehdi_splus</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81445" target="_blank">📅 22:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81443">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rPeeUdkAP44SntcDhFG1mNB5Q_-uDuYL2GGpkd0zM7gt2JSLP8tQVzNi-XPASxg__nDFYp1UxMTehAnDwBv_uJmRFP8hDMgHGn8XGW1JGNBHsgk5-R5sgFiHbPTtlRa5t5vhouqTn30ZPWaTeVEO1_584kD-RAB2QtEx8eqTKgh2lN9iWwXjBm5EL-LMQUWGHb7ao1r6txfCDMkc67xGIaAJvKxWZc9XHlzzEG8U4atTC_ZRtwyYsnI1WJXv1dr0Tnkg1jVVf0_04CcnUA-fJJ76xqkkBsNM5PxCyaUJOOO29QGz5PX7eGccyEQlpBGs0OY4EjJLoXO0UCsm7WJqxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EqLXB13y6hzcwaMVeHrDzo6juqW7xGoArnIxJgx2wIGpj7y2X8bB66zo-RLpVH1ENAqjitZrd7xXns5y18lbEI0QdT-jYw08rbBy0-MPk7gDu5UjFO3IPLm6eE2sjbdiPWn-GdVoDfewOS2rAGP5jOAbCGtUn-BAUuJUB2gD6KCGXXjqtXrtGyHIaYtAUcoCk1jySQW7ge0O3QS9KziZNBtu_x1JlMoJhT1fAyYMGVu0r0L7N-StzwzIGfBy-YSt8TiaHFUPagKjnmV9RG-ZrthrdIgpyuc-OLWY2Lo17s5LynFmAiXRmyaTsYxfzEbrHxu0aBOD1nJ5oJ1m6PYyKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استوری های نوید و بامداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81443" target="_blank">📅 22:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81442">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=BLRs43IgKliAhv1HfqeiEId56zsziQ_sJ68XsfQks_79mJWQmpPHp_12nNzFnD9cQEYs4Fq0Api6i93UCQbyQ0LmwBtdBH4FgNYvfXMk43jKn8rSvGgZ2XK1ljSH7F0ERHU2PBEu0a93UtKyW7iUfrun1Kx2N9ZIZSRsAIO5SfCTDWLmVM0FOJibeKX5Si-ZeXUiFszAlXwaz8l5n2yxwhDn-NZu9e40bPot7t_MnRKG08_l23RpJVynlrenko_B0h73uJR_cUQ1WV-zHKN4R8AJaPJHVI5Xayzoc1YeEE7GWn_sDgQHROxt6gZHeb-01Xj7SfVyeW_1JnC7zxi9wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=BLRs43IgKliAhv1HfqeiEId56zsziQ_sJ68XsfQks_79mJWQmpPHp_12nNzFnD9cQEYs4Fq0Api6i93UCQbyQ0LmwBtdBH4FgNYvfXMk43jKn8rSvGgZ2XK1ljSH7F0ERHU2PBEu0a93UtKyW7iUfrun1Kx2N9ZIZSRsAIO5SfCTDWLmVM0FOJibeKX5Si-ZeXUiFszAlXwaz8l5n2yxwhDn-NZu9e40bPot7t_MnRKG08_l23RpJVynlrenko_B0h73uJR_cUQ1WV-zHKN4R8AJaPJHVI5Xayzoc1YeEE7GWn_sDgQHROxt6gZHeb-01Xj7SfVyeW_1JnC7zxi9wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار کودک‌کش تروریست صهیون:
آقا جلسه‌ی خیلی خفنی با ترامپ داشتیم، وقتی می‌گم خیلی خفن یعنی خیلی خفن دیگه، ما تقریبا سر همه برنامه‌ها و اهدافمون به اشتراک رسیدیم، از جمله همینکه ترامپ مارو پاره کرده که ایران سلاح هسته‌ای نخواهد داشت و یه سری چیزای دیگه که من گفتم و جاش نیست اینجا بگم زشته جلو جمع.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81442" target="_blank">📅 21:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81440">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hgNK35cXi5iod8D_SmHNKsZlNF5kxKxZpoFAMWJ_q-WSecusBFmrNEtVeFFcV5YBfNpwWj8ddmZzVz7rt5iDYHxfjQl03ojPX8FlC_K6J6bGpj5udOc035tU78hgeX_sffNMT29DXbfxiKqlJSjEd-FPK30H74JOus82bDcASvMlA_LBS9xzVnf62s-WJp7-qhJR1YM9Bf1FRs-zdhN5GBWA_1--kuMHZ2j3wzQIGej9ePuXWPkvhzk12-AED4ur966eXtnh3_c4I9ugXmThi1sYMvAXGkR_HueFWH7yl0OdzPi7i9KeMn9hYwHNewTYdl5mNFHmYBnXBu5oX7tFsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IuO7k4OQEx9DROVK14yFDQpTdF52QLOAOj8XeL-v6F4sDwyRlaU-R9aQJQtAIyos2gODCJQqh1ooZF-Fl6RL_g8n7VDoJWyY8sCY2wMZeRg3IBrC9aoT_azdMbFqLCJtN1PBjuOJ1m8ZKwNKIzl6sLvLBODdldipveqC6SBV87ecsDLcsT4tFUBkdkW5kzp7XFp39CJDoWPFUfjsUr6Lr0yoYnXHVGd3WILcyrxhKm-TKpkj5WhOD6iIGtTI5DO3DE_nyNURIE-kw6BCQWq2ecsUdb_BaviB2XKlTKbfBZavKE_M_ejpqKrdXhVH4x8ge2KYk3b_DdjPlgORNGtMEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کوکوریا قیافه دلافوئنته رو تتو کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81440" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81439">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkCvnjQatX2wVBlINlfJvUItkT7HgWj6WwjZFk4iB1-fPH09CIBqpzXco4aSwEXRVBtkZrVNqnb7kqetkuZqKHOJy-sT-TF7RU3l0hYWtqoMRPvNvh2P-IW6wFSmR4LetCx5hU_cpS_yOogCxDA_f71H1uC6A8kYD9C9Hn2xVN29UftoUniZpgxo7wWU2c_jhkwwrCNy5aMQgfNHSsSMggwrH5Wa6lr0uSQKiau1zWymyuZ9_gKk06pVL_0xAQqwn3zI-v0-YB2P1hKC50ABuohf3jKjXHXV5FRqlhBipaK9THHseyW7-63bh_DrQe3y1jkyu8UkttI4lU0_BqJCBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماممممممممم
😂
🤣
🤣
با هوش مصنوعی فیلم سوپر زن رونالدو رو  درست  کردن  اصلا ببینید پشماتون‌میریزه
🔞
یجوری داره میده انگار  ۲۰ ساله توی پورن هاب داره کار میکنه دهن سرویس
😂
😂
ویدئوش رو اپلود کردیم بات برید ببینید بدردتون میخوره اخر شبی
تماشای  ویدئو کامل
https://t.me/CONFINGMeliShkn_bot?start=3126b54d70f9</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81439" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81438">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بعد از اتفاقات دیشب شماره مادر سام صابری رو گیر اوردن براش فیلم سر بریدن فرستادن گفتن سر سام رو داریم میبریم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81438" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81437">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شاهزاده قراره با بی‌بی نتانیاهو در مراسم ختم سناتور لیندسی گراهام دیدار داشته باشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81437" target="_blank">📅 20:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81436">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-xRfCRvxBvEzd59zQHe8szenQ1eTSsIfQT3r-e921M2YmMl5_8zSk746CDpFtoBC-m7_YM4t-B7diNHIHIpuItYpz_DJsWGwNeDsuvHAxAXkXady9RKNfulnybzjovjmOgcvQoDgPwfy5j5knQRMYEuCqqeDrxINZkUJDzCwBdL74vE81C12DI4QbKgl0PLMQ3mRC7hBS0ro77TKJaXP-Jj7K27UqUh51jYlbxhzR4QAYKO35ocDb6xkv0wSgUrEkqViKicakK9ZClli6TkkGghsVGCjz2T9VzqMUfgIjknlsLUVuZSZgllf0fZv49U_brEipoT3lzHS9ZamfBwRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه گذشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81436" target="_blank">📅 20:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81435">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Numb 1 - Madoro</div>
  <div class="tg-doc-extra">numb</div>
</div>
<a href="https://t.me/funhiphop/81435" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81435" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81434">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtlcMQH8x-TWT-M9kBkxYk4na2YsYh2VWQelZcDy6H3fW049HoTZSs1dWBifHetbNuuqNP7MNazkcl-jzErffoBSSfTJlkZbAGuRf-Ag67wmB1q2iAbVg32_WZ9v8_zPySTyEF-NzWiWMSL1l7OtVHfAvDtb8SNSp7KbuWHS4Kr_kxt1X5RGOVzUgl2FqHZSBK7x2T4Zhit40n2Pe4noubRTvBm0un-9bHP5RyU6vnUoKTg9VLBaR1_YtgeWKqeF1NZTmC4tN5So-38N_rZ7SfKDTtoIY--AzgowG1xEGrKPftMYhJNHgwr2u7so-q_K072HElQOWSTI1wV_LrAcsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ جدید numb به نام مادورو منتشر شد
📺
Telegram</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81434" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81433">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">این که ترامپ دوساعت قبل جلسه با نتانیاهو میاد میرینه به نتانیاهو یعنی یه کاسه ای زیر نیم کاسس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81433" target="_blank">📅 20:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81432">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfHISNKfYUhZ9uSZEvgdS3vPZzj9Myc0YkDIFLHhWUbWc2RcsvBIOwqSZUdmomySYR5vlPS1BNtoND1crdsDzgY0NyAQhtYH_T2Mc2Bgr9NTHX9pFuQMQ4Wy7kBEwj8QLTAetzet-XDX1xyg91CqpMzUg1Ez_UXoNq4ZdgD3uGtlqiT4TTxm1eJ2Tu1MgOeeygvrTL4unJpH_MBKM54u17MnY27rE3yrE4F4WqCHD_h9O9g3iONdBqAyWi7WGAszvbCaCDzG8uQ3W5yo68oMM7eOW5x6PN28MQKwbl2XqgIDL502Nj58B-qlwWq3LLex7DpWHyPlxrlwwrzoZL6PQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یارو تو فصل یک عشق ابدی رفته صداسیما
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81432" target="_blank">📅 20:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81431">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQU3S2-Sdrv8oyd2YGfFOqW42J-h0FIvbLaVFiM67rlPCalMM8tltgNYHwWO8i-bb-6fR-MJHeKTaOhp4ijq7eU-3M8OXJgSPI5PrEGpRqFSTwoOEhJU-cayNXVjskRxx4wr4cE30ZP2jfON5fgrhnHRL15cW2Zs5Id2GWNP-Z16SeMD_wQBkw3NvRCFFvRhLKoPLNfQ__G8U-fhFZPdqcCdSYaANlaDeYrVs4_b2AUhWiULQjw_k80pBEHUCg1gRFXcuDEKdfAZXPYDpDB7oCNE_mUuuOnVTIgWX3creru2OtxkmevInpOVXrA4BAw6M56rlmom-x499vCf7ispsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو و دو تا از طرفداراش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81431" target="_blank">📅 19:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81430">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjQdTCDHXhBsFfBv3T8xGKZrx1u5N7j8ONjLiVyzCz2ZW8WPIoh_nL4IFfGLfOHJXCoxkBxpKKRawTdfDQdmXl59YVZLj61-3LnA3zhvn1gPS-RJ9aLxbhKNY2X9ahzVs5yJg4CHIi3aK2RHm8r4FeVa2yIAFnolCjWoF63Qxji_HW4nYDZMo1V-A5mXrERFzekWHziJd057fdMlBZ5WoSxCwvA1mHZbVJXYlFID3wDgCl1fn2-CpxGgpl7_ZOXlI5bpjJC_B5zTXBiqxHbhTz4LPWAynlHD0ZF4b155Y5Cchg_G3cpWTpVgn6xROQ47GrDtml1kKMy7KE40mIeJBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ فصل جدید لیگ جزیره
🔥
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81430" target="_blank">📅 19:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81429">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5lIL-zhyMEgpJPstJYEnTbK2TH8thXYA21dTmK8BfRaeHJwns4iP0KV5Dy8RNbffQcyKR_DebjWlSHXbAOQ6G304cwkX4yPgiMmXLtbM7shSxshdujnae8KVGdmhhMreJ5ed4z1p_V7EK1wlGVTDLr2yquzJ3RbXbqeFi6BPEwvoZgQjoq771uCDgnzMAu__8KQjthV12dNjwZoTgfibqQzYaU9tbDeKFLvow636V0cRwXxm9t3UvHHzalO_KkV30PzNZHrSYTP8iR0KZ086ZGEKMKWMppnHgeC2y8Pab4d8t0CxfdHYPF-cuLwVeIqPyR6YG_AAtrB2c6cSSYQkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی بگم از طنز ماجرا کم میشه
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81429" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81428">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWSM2XsGZYwSj3MiW0I-8AE4c8znzw531IyxZzBdGdl5ujs1ouKSrUTMyIfgGcDGZ9cmdnsTriEMNkYkS1mTqcGW2Gc5R89f9y6RdmW43N06J4Og_nv1lgPKPxiG_Se5qx0wwBv8rhX4kBf6sjr5cf9lzICNgU8bOh2h5WcfCF4feJXn8Sw5RBrBGxsX-ZV0R2RsUSOHoZ0or_SHpTUJt1JyUzqHfJEudeog7SOfeikbuPCNkEOy783yzrp-bNZ0uGd2BrWZSJD5Ar80s3nPoURuNKMOVJyrV_vU8cCyCwNGJtJvGNrUrXxSTn_6Hn9Lu3DLje1_CTaFfR5iwWS0Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رئال مادرید
🇪🇸
-
🇪🇸
لگانس
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
سه‌شنبه ساعت ۱۹:۳۰
🏟
کمپ تمرینی رئال مادرید
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
رئال مادرید ۳ بازی اخیر خود را برده است.
✅
لگانس در ۳ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر رئال مادرید ۳ گل در هر بازی بوده است.
🧠
برد، همیشه عدد نیست، گاهی آرامش است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r6
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81428" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81427">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81427" target="_blank">📅 17:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81426">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">به گفته ایران اینترنشنال,
قائم حسینی ، امیرحسین ملکی
و
علی دشتی
از معترضان پرونده‌ی میدان علیخانی اصفهان، به زودی قراره اعدام بشند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81426" target="_blank">📅 17:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81425">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81425" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81424">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toRqdm4hHBnSJtfvGGvVVxSTKUxrIGhd6xWkvdVHCZckxJsoWKZFrHYnslnaBMedMD0wFyuJKgbrA2ge2TO8lmlTAeSVkxjEvESGEis50x0NtkVyxRDvIMByYLJ6tkP_zDM_P0jwMwgBoAqaedR2GrLyaylD871Q-he6oCmJyrBnx49v_iyod4vGwE_tnrkZbT12etda_pHcBY3iQSxdgR4-3b5fk5wRpciZd1rMcQYOVJ3cE1Uv5V8j5BHhZc05TwsCCK4R19dyfHp_xdCxglvuqx0NCMxZ89nEIESxEgaZJZPLAtSS04thXma-m1_HYiVLrpC_KN1IarLFMeVs_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو خود سایت کارزار، کارزار را انداختن برا بسته شدن کارزار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81424" target="_blank">📅 15:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81423">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اینطوری که روز به روز اطلاعات جدید تری نسبت به زیرساختایی که از ایران زدن و زیرساختایی که از عربا خورده میاد، فکر کنم آمریکا رو فقط در جبهه کری خونی با AI شکست دادیم که اونم ترامپ اشتراک طلایی گرفته داره همونم ازمون میگیره</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81423" target="_blank">📅 14:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81422">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سخنگوی دولت: در طول جنگ ۴۰ روزه ۲۳۰ میلیون متر مکعب از ظرفیت تولید گاز خود را از دست دادیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81422" target="_blank">📅 13:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81421">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">از سر شب تا صبح ۱۰ ها موشک میخوره تو خاک کشور
اما به اندازه ۵ دقیقه اذان صبح کشته نمیده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81421" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81419">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u62toKgEu5yLENQtDpSIGLUzobHeXmowzRVY6vH_K4lGUrpotHfvbf47vS4FPQhHg1cUac5eIirn8Iks7UlxwYuMSd1eHjg-GN6gAeqEqX3TYhnsfmq7CQJFKm2XwuaLITN1a65f_ZWrJLv3Wu_nmdg8R7yuEB1a52aUfKmOqqJKrS74MmTcOG3BSR_Y43RYclxVZ1Ze8MDLFbApnQQwnlTYdky-qebpzBEMF6I-sLzLtoi1kJ3Qwzt0rpYQjEL43UlLYJGNpOOTgTLv2YUamqf3nPGrS4PZKsg-97toXGjKTGi2HYWa1KtXO0M-qjnpsoUfnmUf5FcqSwooMNgC4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fcBhKJ9iNlWVdl-cPTz11lAr6I9SdjOJNcr3lzrXErcKgZ4vJ1abdfroNU2x3G2MZKL2HpAbXXit8kdvpk0I3uenQ8tT1HlaoOcT9WE8wo_aQuZyddfgkJznE9DfCt0zJ5iTdr-IBP6XpwHfiE_E_yBLuqAdjDTwpQShu8BAey1eyejZ_NbbbfIf3WZm2CLnG2MySlRtbyG2a32e8JmCkYuxQ4LZoOGFvhyuPaWD3f0lAkVizKjNW4MrZBLwmmxsFbIY4NEDxu58NYWH_6ljOO-pX2SJT1AHKvhPhlLzT7y8ZhOZgh8XAOkTK6BG3fSdbdUVoEcfFuCVwpudQM2SBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی دیگه از پیش بینی های اکونومیست درست از اب دراومد.
زلنسکی با دوربین کنار یک کشتی ایرانی که داره کالا حمل میکنه، و یک پهپاد هم بالاسرشه
چند روز قبل اوکراین با پهپاد یک کشتی ایرانی حمله کرد.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81419" target="_blank">📅 13:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81417">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtKIg_Lrj-g0fSu85xrbR2Tz10sFvwpnl9_9nZ_eveb7ah5kB_ogPpbfAFl0oc-WqOlFdFz__g4fJJYzJ-C76EBtaExWPlwQYm-AE3AbO5utwemqsFrF6OWJBveeEpWeGGFchKTYTNKlpmNrLe98IwtcLoxCeaGhqIdFqJpmbaSMJtiniELqquRgdHwZmbjg41NU7rsDGdsDO9pSfegCPV1W3hmzfnUogZL-9-A-v6jVMOsqNf8EFw3qg-5KujBhp8gvbukkcurV-k1eNtIlP0z9pgN7OFO8enVPrDvHMbiQHlnJPrKevFpOupR9ZAgtrjNbbEOJyQQR1aJEdY5K3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f171036de.mp4?token=eXgw6g5r1PM4fcjSxM166ulQkiGOapvqA_XvgEjbgTd5x2q6DOeR5FjrCmnPa-Mk0sRkvsicT-7fDwm2F1oZSidZQf5OXQH_uf5eEnbz_IAQzl9fr1_3Fp6plcqMgkA_aJfQ1QCAxuHu_aVtq2elwFQdP9akhI18hCDe2nAYRq1bKci5kIyod3uE5RkqFJKLQ1rVz61F47hOu39oXonO_yuDkUR0x_ZC5B7h_HO3z2_mQUAG25j4OLgbfX1w7-EY_2-zpjYuv1C261fWqaTahATw8_yRf0zsJ-pk6wz1atKNGYKPMAI7UeGA_uSfxBRoYT1a-y-gblMRUz6fpMchFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f171036de.mp4?token=eXgw6g5r1PM4fcjSxM166ulQkiGOapvqA_XvgEjbgTd5x2q6DOeR5FjrCmnPa-Mk0sRkvsicT-7fDwm2F1oZSidZQf5OXQH_uf5eEnbz_IAQzl9fr1_3Fp6plcqMgkA_aJfQ1QCAxuHu_aVtq2elwFQdP9akhI18hCDe2nAYRq1bKci5kIyod3uE5RkqFJKLQ1rVz61F47hOu39oXonO_yuDkUR0x_ZC5B7h_HO3z2_mQUAG25j4OLgbfX1w7-EY_2-zpjYuv1C261fWqaTahATw8_yRf0zsJ-pk6wz1atKNGYKPMAI7UeGA_uSfxBRoYT1a-y-gblMRUz6fpMchFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طقه پوبون رو زدن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81417" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81416">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0nRhjF9wQtddwELH8-F9nPg1pY08bVSQdINE9N62pXAN1adJiIVk8sSzTHiVcPB3yctii0AGc0mAyZkyg31fd4yPlVNkiMeda4_dyIAhHrz9tKhldlxMyJH8Ob1QVLAXxuIxfphmixAG_yY__5oXoFRktC9Z0J699qHTQ_KHnCfnHFpN3R0-xW2uXUtnlE5pG8yAKZJnbdmYRqwTwWOdoXtguZH9hzNv3o9HT3E05Pf3R8Wnz_nYtHC3j1UCNlLAKxUB805K95b7uAVk3cSswoMgx96GzxM9FyoBSRMfXEoHizwlBs3bDE7wUi1raXD_px4YN4QrbwISjzesqMfPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رئال مادرید
🇪🇸
-
🇪🇸
لگانس
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
سه‌شنبه ساعت ۱۹:۳۰
🏟
کمپ تمرینی رئال مادرید
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
رئال مادرید ۳ بازی اخیر خود را برده است.
✅
لگانس در ۳ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر رئال مادرید ۳ گل در هر بازی بوده است.
🧠
برد، همیشه عدد نیست، گاهی آرامش است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r6
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81416" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81414">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce9ff43bec.mp4?token=maZxplDPuc_pZEDmDQUHJ42U_jezcZ6YTA_C3s48jYcLEoBWKVNzp49Lu7JP04aQ9xmKBhI6MIEVKK_KNPEbjrDKor5QJG6bTrrd7fngvHM5HCGhi6BFYvrJIPinLJFc7Cm3b2N1mXvJNL4deKrhgMlBt8AcTTXiZXAnJibZvdUK4-1yf5cd6fxMGjy8vfUwvH1y2_sW_P8jlaiFkqnjpjhXJPRgCkrE9n-jAq8fDz5jS9YzRH0hOH8NpxlZyEYUhntI48KbFu0xNog1kHjOdHgVQCP7tSbm35f2JTNNhxYDk-5BsJCZqQrbBezO571El-bEtNXrIDpp25JvzyuxoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce9ff43bec.mp4?token=maZxplDPuc_pZEDmDQUHJ42U_jezcZ6YTA_C3s48jYcLEoBWKVNzp49Lu7JP04aQ9xmKBhI6MIEVKK_KNPEbjrDKor5QJG6bTrrd7fngvHM5HCGhi6BFYvrJIPinLJFc7Cm3b2N1mXvJNL4deKrhgMlBt8AcTTXiZXAnJibZvdUK4-1yf5cd6fxMGjy8vfUwvH1y2_sW_P8jlaiFkqnjpjhXJPRgCkrE9n-jAq8fDz5jS9YzRH0hOH8NpxlZyEYUhntI48KbFu0xNog1kHjOdHgVQCP7tSbm35f2JTNNhxYDk-5BsJCZqQrbBezO571El-bEtNXrIDpp25JvzyuxoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی گرامی کار قبلیت چی بوده؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81414" target="_blank">📅 11:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81413">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مگه نمیگفتن هر زمستونی یه بهاری داره هر شبی یه روزی، خارتو گاییدم چرا تموم نمیشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81413" target="_blank">📅 10:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81412">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AemLBZryeCZOLbQRZA5E380j79xyRlcVLKWeoquAWHkdPMeIZVvZVooFh44qe_NJ4ltQ3JRvra72oSdurztW_TuakHPk1QG3MHLBoUgV0icJxwZhZ1P33PqVKB5ZqGNxtYWEuzoQ2WMy_Kw2W0XozVqXxsX9zVvdjcK-HofFqP2cwjQzf1lbTT5Rj8ZA6aa-vCEKSrmHwbWrxZn1IX6MpY0oTOLpXdR2QB_-X99AyRJ2_I-AZOccbUQUxy7QGd4ouvOrI4qQzzghsDzpY4-8sQpR1ZWkrKj2xOOk8GHkjxlbT201neFothk3xIxiaIBUx56DdCjVUnyiGB8_R8xVrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81412" target="_blank">📅 10:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81411">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تروخدا فرزاد قدیمی رو قاطی زیرزمینیا نکنید، فرزاد اونقدرا هم کیری نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81411" target="_blank">📅 08:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81410">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبرگزاری فارس:  هر سه نفر اعدام شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/funhiphop/81410" target="_blank">📅 05:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81409">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خبرگزاری فارس:
هر سه نفر اعدام شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/funhiphop/81409" target="_blank">📅 05:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81407">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">از میدون صدای الله اکبر میاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/funhiphop/81407" target="_blank">📅 05:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81401">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">درگیری گسترش پیدا کرده میگن با ساچمه چن نفرو زخمی کردن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/funhiphop/81401" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81400">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اقا یسری گزارشایی رسیده که مثکه مردم و نیروها درگیر شدن و فعلا بچه ها اعدام نشدن
تایید و تکذیب نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/funhiphop/81400" target="_blank">📅 04:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81399">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مخم کار نمیکنه نمیدونم چی بنویسم
فقط میتونم بگم تسلیت به خونواده داغدار و ایران عزیز
شبتون خوش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/81399" target="_blank">📅 03:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81398">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6CppP71Yzv8kXJEd6OtA48LEnK_5kqYzN0oVIC4gzaldbYf_kTmdWgaZ4ySydQ1gjFwaMvX7jUj-dEIR41uOabVlf3_PQL_qSg-QSm3lKlQMs9wp6nSj_9ie6qVNM0AQKtq3_s-toCvzqOOIMNkJIJ9Wxi440YBCINveoxO2U_XT-r4OLIFxu4KorOvq46n4SGolTlfg9vNKKF11S1U2LYecD6JrGmiiARRkX83aNP5MF2fi5hfbxLurgDaphvCac6kN8Yw6V9cgCk1oZAhyezqdo7RcjXDBRfcxiWtWfBtLoZyXJ47LefZwwY7jDy4onb1Bl4RNLD_4bfQbBjCGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپشنی به ذهنم نرسید کسمادرت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/81398" target="_blank">📅 03:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81397">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اذانو زدن
🖤
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81397" target="_blank">📅 03:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81396">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oB8mFuR0qJiMOziwzyOh07D5BW19kDlvvqxe26J8a3VvE4Nyyvx0pEHcMiUeW0A-u33juAPrWIe6aaKNfxrqI3wTsShzIdRLLvAGgaoSFmfvjwSnh0ubsQv2pi0H3EQF22Xe40Ja037fMyu4QvAPxctS06iZZVIJttZg-4FQ-F2lPbqzcSCA36cK6hohbrL0J6f6sq32Yfaj4IaNR3C4_DNaJsIIZ97oCl9Fa0MCJ8my-RVyiTBG-F8WxzrOdaA7Njq9tuKKffqvn12OUlCPN0FlYD5AVyxpLQvS56Q6a5u3h9Gra2jcgU3rOR_vNnZUjngg4sUs3MIiyEZRFhdMgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/81396" target="_blank">📅 03:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81395">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اذان صبح امروز اصفهان ساعت ۰۳:۴۲ به افق محلی است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81395" target="_blank">📅 03:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81392">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e358934688.mp4?token=adHyNaKLqUqLajuYbvuzhPSxSKrzGbx1z5UCJdOUTTmc2AsprP2-R6YjI7c3AH3ArgoitoDMzLDWUrwsFkN7dz9N6trHq2SP3Xj8INF523DfP6f5YA_bL48m7jpP-nxBGtj05gNaLASGYGtrm8Xi6Y640bxxoLtqecmHlJD7uLuRdsSJr98IrPE3XIHt_EpKy0N7_ChqLCj5217heOMpEj-tX5HoutwfGbkgv6T20C1cpOlbVZkK_T6pa6j_hfmbDqaIBTPGti2uzx7X8_ql8Bl41etX_Ay_ZLp2disFrVmUfjVRRgN4wEPf3Mu_12Mkn0bjR72Veyd2qq4rl0Jqjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e358934688.mp4?token=adHyNaKLqUqLajuYbvuzhPSxSKrzGbx1z5UCJdOUTTmc2AsprP2-R6YjI7c3AH3ArgoitoDMzLDWUrwsFkN7dz9N6trHq2SP3Xj8INF523DfP6f5YA_bL48m7jpP-nxBGtj05gNaLASGYGtrm8Xi6Y640bxxoLtqecmHlJD7uLuRdsSJr98IrPE3XIHt_EpKy0N7_ChqLCj5217heOMpEj-tX5HoutwfGbkgv6T20C1cpOlbVZkK_T6pa6j_hfmbDqaIBTPGti2uzx7X8_ql8Bl41etX_Ay_ZLp2disFrVmUfjVRRgN4wEPf3Mu_12Mkn0bjR72Veyd2qq4rl0Jqjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81392" target="_blank">📅 03:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81390">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">معترضین بازداشت شده با اسکورت شدید مامورین برای اجرای حکم وارد میدان علیخانی شدند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81390" target="_blank">📅 02:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81389">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64626deb37.mp4?token=NDFXDZVkgV_9d99CW-GN9ThWxnwnjdQojUFAAnglvPORsgh3DgqSD3uCF0DOI6Ktl_n5Qp-MA7Vg_VcWFnaO1nSM6mYxfP22Vdrg9l4DsyJbdbHQVilQgfFlRPVb-mXrxGn6AYMyqOiQcnLydkXkUpbwQDO4UObOE98pDcM590UZI7y-EJsZ93410oHf4dkGv9-WNcRSTeQmzPDyehDSCkQCkMRZiQN-kwSaY2Y7kWAgpd7ctNSnhCsco-zGp3eQHNcyZsJ_BJE0wvfQf5LCXBPFjUqCgRTcPQaZCmepDOEvWc6lNinboo0KiGTGfH5zi5frfWBamMmJued6hC7keg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64626deb37.mp4?token=NDFXDZVkgV_9d99CW-GN9ThWxnwnjdQojUFAAnglvPORsgh3DgqSD3uCF0DOI6Ktl_n5Qp-MA7Vg_VcWFnaO1nSM6mYxfP22Vdrg9l4DsyJbdbHQVilQgfFlRPVb-mXrxGn6AYMyqOiQcnLydkXkUpbwQDO4UObOE98pDcM590UZI7y-EJsZ93410oHf4dkGv9-WNcRSTeQmzPDyehDSCkQCkMRZiQN-kwSaY2Y7kWAgpd7ctNSnhCsco-zGp3eQHNcyZsJ_BJE0wvfQf5LCXBPFjUqCgRTcPQaZCmepDOEvWc6lNinboo0KiGTGfH5zi5frfWBamMmJued6hC7keg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس‌از اطلاع رسانی کاربران توی فضای مجازی، جمعیت میدان علیخانی اصفهان هر لحظه در حال افزایشه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81389" target="_blank">📅 02:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81388">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEE_0COIfRwfDzvTNrxGSjkl6_4Hq6SgAiBRpDC_6LdlijjsGLr0GImwBdZYYEDsRfEfgRL-8h6XTc_riAy6gAnJ7slELYXAfmIomUXigLlNRSMwDiR-BCNoy9xGH67JfCPWnILBn4IszDYIZ-Gu_dtybmlBx8_RBmm3kuaPDT3vg8BY-354bZdI_4FwVaANRUPXZwHRTuqJkBnZvNrRRouXaPLLXGEMlDDsWScTGVEE65ES-upbOmlWR6q_RO5xYwoN6DHwoC1N0v_RfcMXSPcslyUz6b_Memv8yUbhMh3_rCDJPk30_kxOxtRfBqfQeYddS_outUk5DhP2B6pPZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این لیست کامل ۱۲ نفر از بچه های معترض اصفهان هست که ۳ نفرشون قراره در ملأ عام اعدام بشند
۲ نفرشون هم در تاریخ ۲۸ تیر اعدام شدند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81388" target="_blank">📅 01:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81387">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjnSei5ZZj5EF7qRQyLwa-bwIckcbDSKquMxI0X5HTxHvStLSiv62kO10DUCbfA0gzwTFILbhKMJagygCN1kf5slk-Dnv2M-DnD3hS-0kCBAdReJa7fNnrCufraxrh8ofi6ptx5ldX2fHYQHa02phENA4B9HjSke-ZKJtGBXbKLE01WeM7qcn5PoY9Z01HoHp5yfXtKxEZyG8JC8Parso9ZDiKEfZiNXLX-Zv4qegz7XuezT9cpEyRf4892aQa4GCyc7OXUw4_AcE_F4R2N8YqyDiMtyJCcA3VlkLBawr3JoEnmGBGWJzILbRlpbQU_5OdYGryssG27kbcV3B09INA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بنرو تو میدون گذاشتن.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81387" target="_blank">📅 01:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81386">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نیروهای امنیتی رژیم تو میدان علیخانی اصفهان جمع شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81386" target="_blank">📅 01:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81385">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hto5TwUp_i2RGE9z7hYDKfS6nuX35oyGzdN_LMEUfP2L0lf8QRTjR_pYh9G5vn3MYLsKvz7eRR2QPKDpmxdyIXboSxR6lSYENuuTNypNoeFVVEqIi09JqvGC5Cb_F2Ly6Xq9uLY4N0sBZ3g-egbJccOdPKIRBTxcUHvA5RuzCmo2nuG2T93rQNR5D-kVTzoIkdQJcJN2hIo60bvaglxIQoB0qRzn-bm5Odt3MQHiJp2_DQtvc6-wYn18z3vW2m8PGAQuf8z9WUjGIpSiHLzZouv9s395kJcqM7VcP32MLUhuNzUZwyhfFfWpHAXeFhGXk1hSLrJjC-kwvH7K-Mywag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای امنیتی رژیم تو میدان علیخانی اصفهان جمع شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81385" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81384">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">از این ادمینمون فریب که شاتای پستاش تو جنگ ۱۲ روزه تو کامنتاس از ۱۸ دی خبر نداریم  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81384" target="_blank">📅 00:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81383">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5qv_CNmMJXe84fCUPZx4-iIXkJWOoHSNnLMWZHpGUwdY59GV3IreMKs_RUm_7jQKseKVSK29rGTU4U7l0HnZUGOIXeaJJ2mJ7d9GQm49w4fHXhyGTL3HugMuyfXCNSywRazDZZMabur2dWCy32JjhvvyIyS0a4aHETRWvWsDz8O43hE_WA8F21M3Ni1wiPhJUU__bDpfjx_z3DXIk1xQsDi-P90ZSefpjSzRXniZvlJbvd60ORAh48AgCb-8K8t6T7ISE_UYj4_BGe14c7eXrFqcXPpxV0EfxKCDdoOKPqi2e1v3Ro86kTr7L8PbjKZ7McecDLYluOET_HPWppjkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی این دوس دختر علی سورناس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81383" target="_blank">📅 00:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81382">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTfRiUkiPQXDcEgkWiHbtQmZvASlLdSz4I9rNMm6grLd9HfKohoLVsYeOzJFrV78tOL6R90MoRbiGCKdPSnoZiG3m7KqzfFrkKDV-E555Le-eHbUA5qmmV7_O_lFMDQnZSGVCU6zducIgX5O3za1JsZDWj1FsEpIhCw41_Il0hhXZ8vdk4EkkMzk-UQW-bO8GySHbkXysu1FQ0vnT55kt7KU2ywExnXyh8QUo9Nyl_lVMjd9eo5PvxuCzH0cBL65C58mZ51QxF5TpFiK6VOoEnEJbzaQpRTHF4CgoUpybfXG8ZvM-ymZ18tpNt-qMg72nRbIke_yr42C5Jw9gx8XkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری، از معترضین دی ماه در اصفهان، متاسفانه فردا قراره در ملأ عام اجرا شه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81382" target="_blank">📅 00:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81381">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVdZ6gbhCmSNc4jCNkl-fblec_S1Vaph3PFT-CedSr9XLA4K5sjYsLKLXQZ5R-2d0K-u7L3kv8g7uC75s8j0uudm5NF_LYRLTDzTOkgyWAYdg7MxKGB5fAXM7nfRsTVpqE05TlQdMG3BOt9T-30aBrnRVB8EUHmi2kLGApZi_fLjlaIaUqHvEtyF1MsCuNVlEIvRGTd19d2FKz1ZKAXG4XMLPz94negSDtQd2ZhRfKdZ1LVoMRadbtYn7aHgrkdYZ5tWyjoTpWqux-uWdTx7bN2c5ak8iZUNmhw9Xxwl2W2aHIQ_MC_1FN6K9LJGPfbTUnyjX6aOR0ni5o3Vvr8q2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81381" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81380">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gouSOfwWLIn-_jjA6ujO_BCAKDmmEgF5QeqwaDI4-5Bb9AUmBPpFF7euzGsm3LjS9oGs3vomg2aS_DIXyY8knyaj00qI0FnQ4KokwZhmsPOE_XGv4RaUK7QE500t2OZ3x-WIQ2nqTFBnieGmN8CsiMUHWOpxzCg4207zSKtGzl-lopKbsAoA-qqhM7sOA2X3ftJNBk3jBRH6Ltv5jaoOUlAtjCkhWtMcDL5DT4P_AHgazeB93MJnV9_sDASkVK8zgtboZ8dv1Wq71iWb2BWhDLmcZ4KVXrpOaD2XHE_SjG_o6X25mGg1F4LbbqiX5fdE43rMaXTCb8zhWmHjK1EXGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراد ویسی بالا باش داداش کلی تحلیلِ نکرده داریم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81380" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81379">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjEf2QNj2W5FYe1B5eXoXT3ubJu7rf_T8SrgwXvTDowU4S-G6-qO6MCOaMtfzy4lKOaJ-t7u8z6ur3ee6WSUQB3w1LSNqM_lF_4aT03x68Lb6FqingJ3DWEZcrDct4AvJxVSK2Ny9nt0bvjb2IjlOOd22hPGyD4GHHsE4BMb8rifuOdS5KPfs7xh2-fZZTX9ocZ_oJWf5M0HnlaWOeCsJ_6QQ9bwGM3X00YcFxLRBs0SktYFhLrJEOfek1hlplzRWHYuu4QztCJvX5XZnQ4bJUUsnY_hq8HTdhmbMpfx-Ev8NpObz97X_cZR0tJBNTdLH2F4edys_YBtVUJmdfptPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید فرزاد قدیمی به نام زل منتشر شد.
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81379" target="_blank">📅 22:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81378">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نوشته تابلو توی عکسو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81378" target="_blank">📅 21:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81377">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmGnujEV1sHDcsSkq24fbwyeSOqnmubplF2kh35UtCREtEjXuGD_SQJI6pWNzNueBa-o83rfRi1WefSW51OVdNl-mElNY1uo2SeTd7WmyHwgzJIgNjMsM75F8xn2B9epXD-zooITyQkf12EeQwGlAeNYG7kgoU9uhib6TOhPdmYT7Khst5gRvzldivJzn9_Qu717uoLpdl60Kp1a27iJ5jTBgsSp9r4fqXi2Pw76917E9u651UkFyjJgFAIMUbJguflRhRDSShWMsdvne6_UXFUmcR4-SEY48zVw33WLdKqYHo_w1fsdfWAvZahjSEQByqyD1B9I5gA1jOYizHiRog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکا وقتی غیرتی میشن:
Gay rat
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81377" target="_blank">📅 21:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81376">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ea_WksGMdlLH-TMQ77EEZZr0T08OgDb5RrbcjN8-gPmN0rWA1LTvqPPmKzwLrdeo6G5sBcbtRVLXsZ_50S1EUOfG-Nilo-pepTAuMbawq7SSO3ig4igb4fwNO3cfwO-BGgwwwChoasxD4AE-N1TojoQjRo5rmORmxhvp2WhNa0Tcay6ljdewI9QMOcfXL7KbGdFEGL1Zv0Dmeyjt9M-fnTWGVgMGOBUwkni1IdMstd2t-TC4vI3M8kr7FcRjXFYMeQG68tX1wfuUMs-IExitBDDQ7tSvpVkRPCyabBqw6L-LlbbMnoOqf1mvDnj7sIUK77qF2garkN4jnMakuv9Opw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81376" target="_blank">📅 21:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81375">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q342Zxi5_8w8hvrNMxE6dR0cx-UBs0Yf4QUz_UADWgMvZb1a7wLdNcneG9RhArUaKskTpXb6QV9CB7kD4mKiI6OQGYGM4Q4sUV8fA5_M5mWR0d2tFZmB9DC1_MGuQQGA7JaEmEKVg-uZ6T3MmmYrVYTM0aa6ooBXulbuoe8x3iN-gh95YmTh6TDHGcNSCTVCqVEz9maQl78Aadz939zsXf8Gw7x01xWDbiJvznsO4H9fd104mQNCgIeEzn-W0tu4bql8ru6XucqNW_7VG3S-HyFsKP-zAmlHyypVoE0SfhBcq3ERFYTvdgtVujkNV9Te8yMZcJ1FM4-ZVPtGzQVAww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81375" target="_blank">📅 20:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81374">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qmMaXalDPczSndtDMwI-mCi4g-Ic3Krh6_xui5gvDpEGJZtBHAsJXvAPmkRGpFpcRREIJHx2W3NhEuJGFKvusV4Vu_16PZLtDmQqMUgAuDOHfPFkuGcNrwR4JHi40Rf4c2Zg34sOGL40pvB4Q5wEXIM877UB0FxDnfnlyOm3tMkl9oAYm4TjLYXks5V_0eLi5cm3cF-xoGoeMjSgSJo5C6-jksobQabh9Xri4iEe2DSLAsyrCZMUiJROpCnvuzdqR9nMOI97OTsaKULS5oAm3N7SPckyyMZoq8tYO9lgGVMoP1p3vAWRYMs79HCKQa9tTwamyQ2QbtVHHL3T5EAJzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81374" target="_blank">📅 20:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81373">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3HspX69U3KfDY95AVEJP5EaNvIfRaCCKWNX5PqWKNY3w6lgjNsUxXRrIFaOLLKDAEI0Ax3AhuRerEXDPtN-9NHAmP9kKhoUTva7PZjCELhv3288yNIWSLbvCyUqXFjccrAs664k7lw1WaO8s0QSJ7L3x4yHvKSNOUkC3o3-1vMoyVb5H59ac1LSwX18-4bcuHnuwzh8G3wTuoDsqvWWfojGSWbX2JIu_B1in9KhSm4kh5XQKnLMZNaB_ZdtGJRZlZXhsTN16fnOp7IXt1BUYappQftyv-l6lv835u7tv7x436zKDn1WUPeqAJnat0TIxiUL-2IynTTNPns3K9ql6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام پسر
خلاصه‌ی مصاحبه‌ی جدید ترامپ تو هواپیما که همین الان پخش شده
عجب حرفایی زده کولاک کرده این بشر
👏🏿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81373" target="_blank">📅 20:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81372">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnJzbDAxuamer2ejuDqYKhGDB8fogVutTvhwLnSH683rcaPU3Pwqg9_gXuMD5LZYBXknRNNwSGhCAmGU-HftEZC6dC025N7rDXgHGxEvDmM3yODNZdBpl6Jepeo5IdfmboOzmyJ2mFUYK3-0E5-Qf0zU5hqCODxYaz0zcgACtg8Ja1bN46mMRfcddR5bGIlibhnD2pUTZIcnrRAFfmvrOQVz3ftlxFDRn6cQxjKunGrp5viomoEgSAZU5WGofu91chAme1hkQvz-CgugqWdiSQ1S7x78pi7pt2R6pfexNuPIB9OGKihPCnq30mGIF5F-OS-QvhRuuSHZGYoSmJ3zKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81372" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81371">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خ
دونالد ترام به شبکه‌ی ۱۲ اسرائیل گفت که آمریکا درحال حاضر «گفت‌وگوهای بسیار عمیقی» را با ایران انجام می‌دهد، اما اگر این گفتگوها موفقیت‌آمیز نباشند، ما به اقدامات نظامی بسیار قوی بازخواهیم گشت.
زمان زیادی به دیپلماسی نمی‌دهم؛ یا این روند به سرعت پیش خواهد رفت و تنگه باز خواهد شد، یا اصلاً اتفاق نخواهد افتاد.
تصمیم به توقف حملات آمریکا گرفته‌ام، زیرا همه کسانی که در مذاکرات با ایران دخیل هستند، به من گفتند: "خواهش می‌کنیم شلیک نکن."
ایرانی‌ها شدیدا می‌خواهند به یک توافق برسند و با توقف حملات موافقت کردم، زیرا هیچ چیز برای به دست آوردن و هیچ چیز برای از دست دادن وجود نداشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81371" target="_blank">📅 18:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81370">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQH3C-Ape5cBOD5x95N9uGulgYblONDI_XnR38u7de5Z9Eq4w0XGNzfLrw2KeitcnKPg6tCbiTlVeVtXb7DEJlTG3jJBIythqm47lcB2jzvA-ssEE9AXGHA0isOUEwaNwtHx5URie6kBp3n71jStJlWYe9_-G1QlxqsPtEETDepLjYv7IAxYMM1U05KHsuhrCA6gA7-IkFHrkTKOV9DlGqsxFO03cCndke6W6FD-M6a5CqAMyUzuO7-YHDoEflHrE6NMUwbLsfQtTxYkuwjoILAS_vz-mbucRLSDEx1nz_6cabAITEiY5I_yc3YDa7ykMHQkTIUSdkoqSfed67ScFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندروتیت
دوباره به جرم تجاوز به کودکان، پورنوگرافی، قتل، قاچاق اعضای بدن در میامی
دستگیر
و راهی
زندان
شد تا بهش بگن کصمادرش چه رنگیه.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81370" target="_blank">📅 18:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81368">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RpnrOHWvASwB1ZTBfk8LShUr81FOcQgUVjZPsPiv_TJC7AzQGt1W1nalYQNRu_hgbt8uHxjIHVEFF8mjuBrJxZIMAKkMzKDIysgZugqz8ro5zTUySm5mkmQIjdEFVgoea9CoPuSUNbeRrPUJD5C_mJXsIw3C77dCx8blHMdsR9_AQoMuyCGqIYZc_kkDRWHaK2_U0C9H7gligpiaEiJHDQDWVltkzUA5bdTs9af9M1tJchrfforRTieW2nhXmxGSrWvm3FospLMT8kx9LP3b7ugFF-1vmQPOu0jac_O-M6lle_kJCeMjr_lDbkX_VZvDeLkM6sbuRBtjrwxhYu4H0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y68biFNh4Sh0mOYFVfFgK7k_XZx6RMXWFSjGcVxXQ1aHLjepe_j3KbZqGOo1Aa6tpOH0w-rDVRPRYNGGt7L7ls2zYX7__f0eCTeU0wDB3euHFtqzBW1T8igIZYroMw0g8d3LI6PZs0Ajtsuvb_tMpbabD4QaztyJjvMv3oNirFCo4PlkeyJXNiwrF_zwgqnCLDmQbEdZiOCPa-PKJmmWDNW34HSRbFqBRvUkoxfHFGthJZcYEHQZ9_ulo2MUsryDTcRTXbqG8T74l8Vi5GCLymUHYrILPuzPYyrWt1nW4Poo40VWDcVAjzhSIW1SLciFrNEjeL7BpqRza0t2lniu8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رومرو درحال رقابت با صدفه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81368" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81366">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کانال ۱۲ اسرائیل :
بنیامین نتانیاهو با چندین پیام مشخص در دیدار با دونالد ترامپ حاضر شده و قصد دارد تأکید کند که جمهوری اسلامی، به‌عنوان یک هدف راهبردی در آینده، باید از میان برداشته شود؛ زیرا آن را منشأ شرارت در جهان می‌داند.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81366" target="_blank">📅 18:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81365">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=d3jbavxm7ZYHR-hbCl-Vih7icpxTmR72XKZ1bHB3b9G2asBilx5LXyPAjCSzqEP-BDrbRVsFUN1KY-47G5WS--r0Gq9n-8_aRrW9i1WNkJLn62lhknrfF5-Y_RStmVTu32cG-xmhYkQl_-Uvi724ypXUfhtlXJwawFg-nlfFMkxX4LtXkz5vHVW2DtwJ-bxitN2XePwl6VTyFye1e_BPLQ_dCD7m9GwboUn_4DCdPe_CwXkULrvqa0zQfq6tY06OmzJbUkJ4km7dIFwneCPulVoHzCYuSpq9iaWE1TubNR2WrHvCXRjBZBAlhf4_eG5xGJysgK-TMVjQoGHZsnCuig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=d3jbavxm7ZYHR-hbCl-Vih7icpxTmR72XKZ1bHB3b9G2asBilx5LXyPAjCSzqEP-BDrbRVsFUN1KY-47G5WS--r0Gq9n-8_aRrW9i1WNkJLn62lhknrfF5-Y_RStmVTu32cG-xmhYkQl_-Uvi724ypXUfhtlXJwawFg-nlfFMkxX4LtXkz5vHVW2DtwJ-bxitN2XePwl6VTyFye1e_BPLQ_dCD7m9GwboUn_4DCdPe_CwXkULrvqa0zQfq6tY06OmzJbUkJ4km7dIFwneCPulVoHzCYuSpq9iaWE1TubNR2WrHvCXRjBZBAlhf4_eG5xGJysgK-TMVjQoGHZsnCuig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی پور:
من فرزند رسانه ملی هستم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81365" target="_blank">📅 16:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81363">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKCMqBzcE29YYn6KiJB_QbCCwAapaa173tt0erRmYImiSci-_DQF8kTVrzboXUHBXuTn3IKTx7dxRSli8KCjoQe57KsSptoB82cLzOMTfRmnArtUvWYAwPWOTXOBUkVG922IBBgNzBJxaZpTCupmL4sRif-p5Zm4WH9vgQmlRqeQ4Jv7Tq07gK45vD6ajh04BQQvMLxUFjDLoZ-SbbhWKsVPfjxo41wVYXkcrLl_-y6Dj2xZchPeLbv6X6R5yaOon853tYJ_YSZBUaZJK8v7wuT4VNzMBvrp9dXdIezTqy_9Qkxx2JhLrPr_oFHC3BfvG9kVemS5FnJt7J_QxiwMxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام از این جا سیگاریا برام بخرید لطفا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81363" target="_blank">📅 16:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81361">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfUiRRkmF9NjFElbBLcSNuianErnfg1_sxAaW0u5ztEd1EmrVkgQxX-DMiYcnDLnuywcqEbnmkTOQETIIx0VJOykgL4RO9X_kJ4JzzQOX6xkiAKGSxy0v0V5vaungPxvGYLDfI1HL_c-u4bbU0veiAqh9JTtdJNKJClU2UAf6SY_E7G4GoztrSkeBEQS-nVZkbiSO0VtwO6giKzVO16jV8j0lestK_j94x5-mwWu2P0wKuMIKYR3PsjFAUuHp3pdJGv3q2KFoQerygKK97uD9psgeZbqHGbumlR05Wk5sZbcnJ_V0zeviJ-cghfEf_eehn3aaCFJNgXOkes3I-P8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کاش پنج هزار تا استارز داشتم همشو روی عکس شما میزدم بانو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81361" target="_blank">📅 15:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81360">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تو 5/5/5 تنها کاری که میتونم بکنم خوابیدنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81360" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81358">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81358" target="_blank">📅 14:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81357">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1yqTD4lasrn1eequO3G1oQ9x_O-ekMSxIEVcgvXrZhu36pzQyWPiAIO2XISz7gefQNbRN6KXysBys-IbgA97nl4PEOm5kZiVQUBavZrNKZtskqO2SInYaWZvhoVxHp_Q0Pe789oCIJfwk8AARfVbpmev_q8y9YVTW1tMVvuIhYjJY91N2c3oDE_LqGOODMvpZkBiC_Vb034_TsK46GgWuXJJZh3mIKUR2wT710YtObvOD0V3ycj2lhTTNiSAuwIaLnNyu0jyBMlQTFIZO60W8rbls4V-WbvHwFSBVLOm6vFj3G-kJajQzNYchGftTG9Ki_XNJw_Uy3UL73vh8p02A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81357" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81356">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spms7TTFQZKImF8sLPWOA5KWib-YrMETAjQtFk72jcor_ohRkrWlUmV96cwXePHIz0n_9c3VSOXyWKPUqX3BPSgJUU78UpMEdxtwElfJ86h0wsqXGtMPRWNU4c2e4r241IljW6S4ol3aSZYa3wUdRPok_AEOvt0NZmVYinxk9g9djorVRNkwIKVhsCxRmGun8og_p0W9gpba8t8h84kOUvUecdwyM69UukoTP_EF8aMW8T3kHF34Qkr72bxrQMxO4b0CAcGOkI8mqH_N6xQ9idOx3h-_d9GUmwr1L_iGNydZY8VcwmBp7nENw0sckN7NeHL7XMeWXZ21huV_t6-2WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81356" target="_blank">📅 14:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81354">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81354" target="_blank">📅 13:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81353">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81353" target="_blank">📅 13:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81352">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGZNcX7KRIm6t4vLmucVHSXZ3xtEAjKayZhIryAGqDtp3YTsMzYJ2owZB_iqMFep9WHZrUmoGMt9YfrfDiz8cIrxo80nzRZ-WSr93h5qME0Lhuqcgy4siZyZMzGhZiJhC5GWCn_ZfnQXPQmc2YLa2mvCtN3lPViSWo96LwAOq4bpEtjmbpb3Eik35bdu_6Q2V7BQechH2EcukzmMi51OhrT91Fhh_eNT96Vx9bsl5YbVujpzLCkPOe9q6njUhUJSj2pSEADBmXilimw65p3q0_KFIOxoikMbRCyG3SPpDjAGz8a2kRHnV-KqApoPm3LVgq3LYtnfSVRdoHjDN8dD6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی خدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81352" target="_blank">📅 13:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81350">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTuXZqhM4DL_6l11BMjnUsbympDF73anl4gitFQYuQfnAOpd1iSqMJtYwwCP9YYPbur48YZSCerJvnhV8oKIosahdAUGNzKZgcr6eaCXTbBaJlsW-2sYcDAjBEtk-TnP-AdMFQxbe4Pw2YPARXA2wRvqIf7WnlnRfoHrwd9ElMhrhTISi8vVuM5s68aneE3NYOnZ4jWubZotG81V7Hn5trP3iJu64D1dHYRo-MJdBtqrTfF0J8jncvU_nGzuO-VVal2PlvJWsMIceJTzAQ2Fkymg1FIPrGR3v_FTYlMlPDgCUZhZQi4-tVp4Hs5cTh1ioC2qD_8G2ghIiN_2FEbjHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد دیدن این عکس حس میکنم تهی منم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81350" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
