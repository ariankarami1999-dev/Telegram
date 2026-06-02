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
<img src="https://cdn4.telesco.pe/file/Jx89lhYv5oG-8bZc6YxvVyFZS09K52PAJ0wE6dVsAmjr3E-OJQf95fRsheSoai4WNlYJxQSQe6m5onuPjOaQ8WwCn5AVAYyOnucHM79zGQ3mZOZzCBGgylDSv3U2nP6NoP6WbE_uGDb_Q3kS46THm_OsqvEjMygqjoG61IT3L_gz8uSPcF3-ITxILdFumLwKLGonrj0tg8DJRHxAZ3cAX3N01MkhSzkmQTBXAybUfq0gATpNVKxgzDB7m7BcAeqHnsKUioIbTMBEDVOvgaou9W5t0rs2birIqdF6FjvGob_1inBAyimuA4_JUbxq1B0IYJA-LMqgMOEXF417OHLlhA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.04M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 03:37:39</div>
<hr>

<div class="tg-post" id="msg-655363">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQR5onQ1wNHOXcc9m8af_7rEixxvN3iDnvNwV_gXS1cNNt_YbnuwKDs90U5RUgnQP3jPQOlXR3fyeKTeKN1j-NxgdxlAYRFKnJc3UhcZxUm5-SNFROFkBfHdd-UUx_GTWPPh98uLKYIllrI0ndZh1ddV4E2CCHZafY3EemdcthEZGhP-L7_wsj61NzyMc7FnwzrXbGD_JV0SrmXYROU9aZHnrWniaBm1FRTKDm-JVutXaT2yqYcE8sEtuXlTTNxES1fv-PSwae7blvvLeeVvDObmN9xG7rMbsO9Bsta93Q72zWJYtOqHEEdE1HNecxYgWVX7mT55xfSVGNACnql_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
دریافت ویزای کاری و اقامت دائم استرالیا و اروپا برای انواع مشاغل و حرفه
✅
مشاوره کاملا رایگان و بدون هزینه
✅
تضمین دریافت ارزیابی شغلی از استرالیا
✅
دریافت کارت اقامت اروپا در کمتر از 6 ماه
✅
پرداخت چند مرحله‌ای (اقساط)
با 19 سال سابقه موفق در امور اخذ ویزا و اقامت دائم استرالیا و اروپا.
✨
برای دریافت مشاوره رایگان لینک زیر را باز کنید:
https://persianmigrant.com/فرم-مشاوره
☎️
02196862626
🌐
persianmigrant.com
-
www.bmcvisa.com
@PersianMigrant</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/655363" target="_blank">📅 00:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655362">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdRM8JtxVHziTs2dd-VAYWJ1gw_u63fYAOsQO9qHoD1s-paHgaQ31JlcoOK4aKUOuhOfzhpJ3YaODH8A_vccMDmR0rGEmFnF8Jl2avCgucTohybCGqz9LsvhMb11aGUq3yMZxF9_NH3ih_lOCTHsJqAlUSHczyjZ4Zb_QqWN1H60CcOWTMUIbcxAT2P2bopF9eomZTHk3hUkifXbBc7FrQN_AmVqT9u9Fs7pCS_TueSkUydL60OcDAhc0o_xlUJGoCB41WU2po1XIcygJsz_-m9VF_5-IpPl6UcxLNG7fBjkQ3ZhTob3XzIBUaOfCQCCJ9LKXU456whYSxJs0l0Eog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/akhbarefori/655362" target="_blank">📅 00:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655359">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pk1eowzb6y5Ho4RQschlUbaJlP1CRj0xlHK8JozubORzt8O5waDbRx_4cKav4PdPrW6y0UUj8mHJA3R4g71rdMNRKxXlmzhzlIn34W64E4aK5aq4eQhjVxExKHRSAvaYaPPj66-xJ4v1iyn3jGALy8dkmvg5YVK8GIBMKnl8p2NSOqTExNwIGI_2APDhW9I4yvTjVL8ceH1GHjkgsjxClIwqcrZYJq2rQ8uW7nIlCOKMdVVJd6FYErzsmiJ5F8--tNxfi-HdUND-wU3G5jP3qhrW6gwTzET0emcsSl4sPXMQ4yDuXIshsag2S3xH62j7SCkPCRzdJcAjCvSKpx6Z0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بدن در هنگام خواب چه اتفاقی را تجربه می‌کند؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/655359" target="_blank">📅 23:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655358">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
شروط حزب الله برای پذیرش آتش‌بس با رژیم صهیونیستی
حسن فضل‌الله، عضو فراکسیون حزب‌الله در پارلمان لبنان:
🔹
حزب‌الله و نبیه بری، رئیس پارلمان لبنان، مواضع یکسانی را در خصوص آتش‌بس اتخاذ کرده‌اند.
🔹
طرف آمریکایی در تماس‌های اخیر خود پیشنهادی مطرح کرد که بر اساس آن حزب‌الله حملاتش را متوقف کند و در مقابل، «اسرائیل» نیز از هدف قرار دادن ضاحیه بیروت و بیروت خودداری نماید؛ پیشنهادی که حزب‌الله آن را غیرقابل قبول دانست.
🔹
با اصل «آزادی عمل رژیم صهیونیستی در حملات تجاوزکارانه به لبنان» قاطعانه مخالفت کردیم و  چنین چیزی هرگز نمی‌تواند بخشی از هیچ توافقی باشد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/655358" target="_blank">📅 23:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655357">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBz6CkTsSQHCs7cuW4xxuI35eo-MUdq0iN6Kv2rNRl_hVjMwlZHeB5lH-561SRH7xEh3jVJdmQtc7S81Kon_7PEPatnL1maSH6_1U24YqbaRTBoi76xN1GEphJHBIKtJIT6BkKwrhyxQAoRzmsf9a9GQ38VulU80yrL2AIEfs1dS_lpp2GbTqQMImD_rLM2VXbctDzLUAL53eI853WEI48GfNEHWGCIyPhdjF2dt8WXTnEVsnCcU7RQ-p6U_aDhq-1uVaUktFSxVuEeDXJsejJ9_HDRH3DBWDHRxvSqZPW6LdWzEKc1zqa81Ja23GE-yIwm3WiSpdfCMCGIrrO313Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسپانیا دوباره ترسناک شده است | بازگشت لاروخا به جمع مدعیان جهان | لاروخای جوان؛ ترکیب مرگبار استعداد و فوتبال مالکانه + ویدئو
🔹
تیم ملی اسپانیا بار دیگر در آستانه جام جهانی قرار گرفته؛ تیمی که حالا نه فقط با خاطره نسل طلایی ۲۰۱۰، بلکه با ترکیبی از استعدادهای جوان و تجربه قهرمانی اروپا، یکی از مدعیان اصلی جام جهانی ۲۰۲۶ محسوب می‌شود. اسپانیا پس از سال‌ها نوسان و ناکامی در جام‌های جهانی، اکنون دوباره به نقطه‌ای رسیده که بسیاری از تحلیلگران از آن به عنوان «بازگشت لاروخا» یاد می‌کنند.
معرفی تیم‌های جام‌جهانی؛ اینجا درباره اسپانیا نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3218741</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/655357" target="_blank">📅 23:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655355">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60a5f71e6e.mp4?token=ARoQ5u60LzrLRNyk1BU078yIYrGD_ZhNJO5htF0MbgSCmL2Mfbk0j1H1vv9F_Nj6_aNFr_TlOl_q_yqtextZbdYfpLdkxi4nf0kFd8-u9eKXKHmT7A-9rnRCIR2Vg2GOoxtP-7Na8Rai8SOkPbRzI36YcBSLe8LNXRCimM5FJqaxyTj9Aa9fkln-Pqr-NQxgKmiHlsAi3Qb7eA8nrgztxGO29PqfJ78azmtlNNktPjrl9-h6RqOptFyepWHdaovrcVactCKnnuwFzgsUXqx4le5PyORJXlSxHd7QcpKbIjqHcPqLBGYGxcro9vbv_P6YPkFT2F_EPjpWq45ahndnJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60a5f71e6e.mp4?token=ARoQ5u60LzrLRNyk1BU078yIYrGD_ZhNJO5htF0MbgSCmL2Mfbk0j1H1vv9F_Nj6_aNFr_TlOl_q_yqtextZbdYfpLdkxi4nf0kFd8-u9eKXKHmT7A-9rnRCIR2Vg2GOoxtP-7Na8Rai8SOkPbRzI36YcBSLe8LNXRCimM5FJqaxyTj9Aa9fkln-Pqr-NQxgKmiHlsAi3Qb7eA8nrgztxGO29PqfJ78azmtlNNktPjrl9-h6RqOptFyepWHdaovrcVactCKnnuwFzgsUXqx4le5PyORJXlSxHd7QcpKbIjqHcPqLBGYGxcro9vbv_P6YPkFT2F_EPjpWq45ahndnJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروی دریایی سپاه کشتی «msc. sariska» با مالکیت دشمن امریکایی صهیونی را هدف قرار داد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/655355" target="_blank">📅 23:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655354">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔹
خبرهای داغ امروز و امشب را از دست ندهید
🔹
🔹
ادعای ترامپ درباره موافقت نتانیاهو برای حمله نکردن به بیروت و موافقت حزب الله برای توقف تیراندازی ها
👇
khabarfoori.com/fa/tiny/news-3219643
🔹
مشاور احمدی‌نژاد: حال او خوب است، نگران نباشید
👇
khabarfoori.com/fa/tiny/news-3219653
🔹
چرا همسر این فوتبالیست مشهور همیشه صورت خود را می‌پوشاند؟
👇
khabarfoori.com/fa/tiny/news-3219630
🔹
وضعیت میرحسین موسوی و زهرا رهنورد پس از بمباران پاستور
👇
khabarfoori.com/fa/tiny/news-3219593
🔹
تازه‌ترین تصویر از چهره تغییر کرده حسین فریدون
👇
khabarfoori.com/fa/tiny/news-3219567
🔹
ویدئو‌های جذاب را در آپارات ما ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/655354" target="_blank">📅 23:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655353">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eH5EOLrMx_cnB87okhz2nBTVe4DXFkW0kgIVMn23eA6tuLP7anVXZDsCGsm9Rl5OjvYm8A1m93avtpu8jIhg3tCz0MR8DpuXjvNS_vJ_SNebBEkcgc14gbhRIEF6ixqOmKFfmbTluV2RjLceNy3J12GhNE-CXYMXcttiV3MhIGFY_vOMJu6zFwuTZv6nk-ifwh0tXLntdug5hn8O4UTgWbxUM7ypS1XUp4H6RWzdDGXQCct8458wKUPRNSlAl-5AK39JKRwxRgSHXrHb8CXqT-axAL-tkvvdIwbdg_-jvKyA7qbxMvlAr53iwuyYPHDhGmg9_nIsiYYmtJ2HG6-0ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین قیمت طلا و سکه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/655353" target="_blank">📅 23:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655352">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
حاجی‌صادقی: نباید به دشمن اعتماد کرد
‌
نماینده ولی‌فقیه در سپاه پاسداران:
🔹
آنچه دشمن را در همه صحنه‌ها شکست داده، حضور مردم در میدان و ایستادگی ملت ایران بوده است.
🔹
مذاکره زمانی قابل قبول است که در تعارض با این دو اصل نباشد و در امتداد همان مسیر حرکت کند.
🔹
حتی اگر مذاکره‌ای صورت گیرد، هدف آن آشتی با آمریکا نیست، بلکه احقاق حقوق ملت ایران است و جمهوری اسلامی هرگز از اصول و مبانی خود در مواجهه با دشمنان عقب‌نشینی نخواهد کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/655352" target="_blank">📅 23:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655351">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPjLp_6SFV4oGmnPnaw61TrkL3mF7J6X9Ulk2vL6MCZn2ojggTweQe08L1nZc6obRLv2oYywX8RgMEWk6syMIIT2ZsPdnG2KmR1uWWQw5EniNIIoSjRbhNO7N8AV1ACBJjBWbZpTgtDxgRP-aUxc3Gj57bojYyy4kQODzGoyBqwFJ3VnwXGzsGZne_iibkaT1gp_r-ZXHqTEORlKApRjtEFWcyKVp65PVIb6jteLe_jEg5GZPUpZwR3BsdBfGOQErBE2EXHR5XJA01ImR8rFmOq8Or2bWAafZ5cHQf7JIhezt35FKyNuuWF0Gw6oF7wKQgsLZHhxL0t-BrBvEHQI9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر کمتر دیده شده از رهبر انقلاب آیت الله سید مجتبی حسینی خامنه‌ای
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/655351" target="_blank">📅 23:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655350">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gvstcg3CLtcZKk1W_LiJwCpBvPIjtGeABrteaLW57ntjeeEyaQ-1cYxiGtxn_IP5I_LCl_cxv46EBdX3WdoLo9kYkmWQLeX9Co7Oyjd0XS0QP4Xx9FUYAZsAEpxwuObCHHSphROw8Y9qzJAdktdBkIo9jgzVvgiNxd62Y-X3NqE7_M-EOMLulLuVSVxoTtK7MVQBUGjjKuQJ_6PFt7nzHvCx2R76E_K_5gmw-mGuXfG-iUIMqMkzqz30vhawf9OMnilxHyuUBbUrR9s0X9d2nLK66B89K-S0ENGf640oeS6B0LjCwVmwr2h12Ko81vuuwD0jOXMgUYfClPKQ3me3Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بزرگ‌ترین آپارتمان چاپ سه‌بعدی اروپا در ۳۴ روز ساخته شد
🔹
بزرگ‌ترین ساختمان آپارتمانی چاپ سه‌بعدی اروپا در فرانسه تکمیل شد. این مجتمع سه‌طبقه با ۱۲ واحد مسکونی، تنها در ۳۴ روز چاپ شده است؛ فرآیندی که در روش‌های سنتی بیش از چهار ماه زمان می‌برد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/655350" target="_blank">📅 23:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655349">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBPf7pg2HWZjhdbMka3fMnTAYDxYbYnnX2THBNyAM0UhSDyVqfNWjVuOzCVjQGogvlOAV6W2ug7jGlWDQvG1xGhtmleK4oZOhEPHM-LKfWImGZLe37FpcZUF81ljFmNiOj_kyyw1pPoIaGgW0I0vEUlbI6-CF-bkQL8prNp5Os7fN32hs1acli8VJe9028XBVUU5_9WFseFVJTbd4WNdy1DWjQ6EoB4S0fI3OC5A8nX9BgPYH3JZBusATpM-rhMyPrsBr8oYhqWs3xqBTc3kS1YBlaf_vz0bVEfiMm4x2EFSzYMTE19LTN96efF1lztEOPT5Vqjeck0UT9dIdbk5zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WillPayThePrice
#هزینه_خواهید_داد
با یک کلیک به ویراستی خبرفوری بپیوندید
👇🏻
https://virasty.com/r/BWcv</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/655349" target="_blank">📅 22:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655348">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMCyQBhc18J-qM-H5SJXmes6OUgb7SqIHyv2mH-_RllUSxf95aWeN2nsQyVg-xH33-wsQvNF9XUQiwFSyGS5M79N9xDmsi99Y8YJDmdAs9T-61VIk6d13aAWrY2607d1SNxFSRBHWbs3fwmHX2CG2BtdkhGqy-m0BTXBFMUs_edvtp5ahlRf-5iFEB7ayrMowD2kZNrGaIWSbKkI0kVt07endyuMu5CW2xQBPAFUa4VUEmL_C6Ku7m23x7kLV3ja3-y18lHE8b4lsjIGb5ovTy5L9g_Z4_tTFeu8rwe5b4wM7wFXOw2Fo_qwe_DlEch5ZlnVO7XN8Mf8SKbU5jOZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام سردار قاآنی درباره باب‌المندب و شرارت جدید صهیونیست‌ها
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/655348" target="_blank">📅 22:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655347">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
سفارت لبنان در واشنگتن: دولت لبنان در دور کردن لبنان از تشدید تنش‌های بیشتر موفق عمل کرد
🔹
ترامپ به سفیر ما اعلام کرد که نتانیاهو با آتش‌بس موافقت کرده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/655347" target="_blank">📅 22:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655346">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ترامپ قمارباز: ناتو درباره ایران به ما کمک کند
🔹
رئیس جمهوری آمریکا علی رغم عدم مشارکت ناتو در حمله به ایران، بار دیگر از اعضای این پیمان خواست درباره تهران به او کمک کنند.
🔹
ترامپ روز دوشنبه به وقت محلی در گفت و گو با شبکه سی ان بی سی نیوز افزود: متحدان ایالات متحده در ناتو «باید وارد عمل شوند و به ما کمک کنند» زیرا آنها بیش از ایالات متحده به نفتی که از تنگه هرمز عبور می‌کند، متکی هستند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/655346" target="_blank">📅 22:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655345">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شیخ حسین انصاریان: حضور میلیونی شما در مهمونی کیلومتری غدیر امسال ضربه ای کاری تر به دشمن سست و نحیف خواهد زد؛ ان‌شالله
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/655345" target="_blank">📅 22:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655344">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
راهکار طب سنتی برای کاهش عطسه و خارش گلو در فصل بهار
🔹
حدود ۵ گرم گل بنفشه و ۵ گرم شکرتیغال را در دو لیوان آب ریخته و روی حرارت ملایم بجوشانید تا یک لیوان از آن باقی بماند. دمنوش باقی مانده را صاف کرده و شب قبل از خواب بنوشید.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/655344" target="_blank">📅 22:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655343">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
استقبال گروه‌های مقاومت از تصمیم ایران برای تعلیق مذاکرات با دشمن صهیونیستی
🔹
گروه‌های مقاومت فلسطین با انتشار بیانیه‌ای، موضع اصولی جمهوری اسلامی ایران مبنی بر تعلیق مذاکرات آتش‌بس با محور «صهیو-آمریکایی» را ستودند و از آن حمایت کردند.
🔹
گروه‌های مقاومت، این اقدام تهران را پاسخی قاطع به سیاست‌های تجاوزکارانه رژیم صهیونیستی و حامیان غربی آن دانستند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/655343" target="_blank">📅 22:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655342">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBenelli Motor Iran</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vh35EG5GCVR0lXDFKgRTVmfBJJaNwXHDPePw1Tp8bHwC6X2DzLsnEpeq2r5F9z2GgovYv-Z0kEXgJzHj_myY8Kcuw_B1woEttT60pgOXUGiupiuOYZykRHzYEfBELKbthX_If18UM0mjNsTjjsaET4fsV7v6r8ef1qWbDCzoVOtsHKaR5XDfI39V1O2yLrTcO1HiPnk3_tIAvpVr476mVLsq0km8fr-Nf74azwHJj_Wkfd68vQbdsA_Q_iVugrtriz_Blm1Cx56eANKdMDmyR89xoOqmBI0i2LKRW0vEYbaM3a0QqQOzRqFmC8TdSILGEoEMe_yYtrDQt2-EMGrbZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎖️
موتورسیکلت کی‌وِی K249N
موتورسیکلتی که لذت یک سواری هیجان‌انگیز را به شما هدیه می‌دهد.
🔹
249 سی‌سی
🔹
چهار زمانه، چهار سوپاپ
🔗
برای مشاهده قیمت و سایر مشخصات فنی، روی لینک زیر کلیک نمائید:
https://l.nikrun.com/og2
🏍️</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/655342" target="_blank">📅 22:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655341">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مقام اسرائیلی: در حال حاضر به بیروت حمله نمی‌کنیم اما نیروهای ما در جنوب لبنان خواهند ماند
🔹
دو نیروی سپاه قم در انفجار پرتابه‌های باقی‌مانده از جنگ رمضان به شهادت رسیدند
‌
🔹
برخورد مرگبار قطار با ۲ عابر در شیرگاه
🔹
عراق پروازهای خود به بیروت را متوقف کرد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/655341" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655339">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 62</div>
</div>
<a href="https://t.me/akhbarefori/655339" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه شصت‌ودوم
رائفی‌پور:
🔹
0:03:00 اشاره به ازدواج حضرت علی در تورات
🔹
0:14:20 رفتار پیامبر در مواجه شدن حضرت زهرا (ص)
🔹
0:18:00 بی آبرویی عاقبت حسودان در دنیا است
🔹
0:28:30 دو رازی که حضرت محمد به حضرت زهرا(ص) فرمودند
🔹
0:39:50 اولین شخصی که وارد بهشت می‌شود
🔹
0:55:10 تذکر خداوند به پیامبر در مورد قرآن
🔹
1:07:30 نشانه‌های ظهور برای برخی از افراد قابل درک است
#دعای_ندبه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/655339" target="_blank">📅 22:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655338">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
بن‌گویر به نتانیاهو: وقت آن رسیده که به ترامپ «نه» بگویید
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/655338" target="_blank">📅 22:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655337">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gjtd0X_hyBKQQ3T9bb4WGJxtuLHMffCmOZyf0gUGoiENltdDsuU5chTFPiTSF5UEVC0cqBTCdhK2-zPKSsvf8U-lbHXTY_OPe6lfTLj99nnCZhl8eqxcCBbv0OfhWzddbHelK5pO2d9fkCuGHogWoM5bjWogNHzSurF-udHHIviWeKfEXniHIF__HiK6UUSdOVtekD_oGy0yhNJRcjq_l1OsBvz9kzmr5eoLwQdUrL9OmmmLScZS14w39JXYi_-AJJESPoJpXIk8n4tBODxQmZWBecNBWpRWzCkHldQy3zESOhbad1pJwRSKmnHdv33WwaPZPT56n0IE4P7Magk51w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارغ از نتیجه مذاکرات، به هیچ عنوان اتفاقات تلخ اسفندماه را فراموش نخواهیم کرد؛ منتظر باشید؛ خون رهبر شهید، مسببان این عمل را در خود غرق خواهد کرد
#WillPayThePrice
#هزینه_خواهید_داد
با یک کلیک به توییتر خبرفوری بپیوندید
👇🏻
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/655337" target="_blank">📅 22:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655335">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
فرمانده نیروی زمینی سپاه: برای مقابله با هرگونه تهدید و نبرد زمینی در آمادگی کامل هستیم و سطح آمادگی امروز حتی از آغاز جنگ تحمیلی سوم هم فراتر رفته است
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/655335" target="_blank">📅 21:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655334">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVYGivUKBxfKrzTtZexho4XsTnNhYdaO4TPNAtOZX-FCDHzn9qczuv0R1NKpAA7ncxJPrXMG5jF8F4_9t83hPk_1cLJv0rDnuamaxCQFAwhFQfsg59qBbHKDZlbuySjWUcviMk-DoxPACSHishyJAlSnR2I55qf0REQ3dc13nKT8oByBOcep35s2fasOII5L2Zke2WqLVFNDUHJndi7yA9K48KyE9sc19SejGItGH0Yq_JuyDAliUNTeT55ISZbS3KsLK6rxZT16Www7Y0xB-gfzktq9EhKPI_X24zDkoR3mL8utouwx-_NS26DvQz7CklkszTGuq1Z1fFL8RYYrCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار خودرو؛ بزرگ‌ترین بازنده احتمالی توافق ایران و آمریکا
🔹
کارشناسان معتقدند بازار خودرو می‌تواند یکی از اصلی‌ترین بازندگان توافق احتمالی ایران و آمریکا باشد.
🔹
کاهش انتظارات تورمی، تقاضای سرمایه‌ای برای خودرو را به‌ طور محسوسی کاهش می‌دهد؛ موضوعی که به باور برخی تحلیلگران، تاکنون عامل حدود ۵۰ درصد از رشد قیمت خودرو بوده است.
🔹
از سوی دیگر، توافق می‌تواند مسیر آزادسازی واردات خودرو را هموار کند. دولت نیز با هدف کاهش ناترازی سوخت، تمایل بیشتری به واردات خودروهای باکیفیت و کم‌مصرف نشان داده است.
🔹
در یک سناریوی خوش‌بینانه، قیمت دلاری خودرو در بازار ایران حتی می‌تواند تا یک‌سوم سطح فعلی کاهش یابد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/655334" target="_blank">📅 21:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655333">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">تنها رمز پیروزی</div>
  <div class="tg-doc-extra">ostad_shojae</div>
</div>
<a href="https://t.me/akhbarefori/655333" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
پیروزی فقط دست خداست و فقط به واسطه‌ ملائکه رقم می‌خورد
۱. امداد ملائکه در جنگ چیز عجیبی نیست؛ چرا که تمام زندگی ما با قدرت غیب رقم می‌خورد.
03:45
۲. پیروزی فقط از جانب خدا و فقط به‌واسطه ملائکه رقم می‌خورد.
05:20
۳. پیروزی، در سازش با دشمنِ بدعهد نیست!
07:15
۴. قواعد پیروزی فقط در دست خداست؛ به خدا اعتماد کنیم.
08:30
۵. امدادهای غیبی خدا:
_خوار شدن دشمن در چشم مومنین
_ بزرگ شدن مومنین در چشم دشمن (ترس در دل دشمن)
_ کوچک شدن مومنین در چشم دشمن (مغرور شدن دشمن)
09:58
۶. ویژگی مومنان: افزایش ایمان در رویارویی با اجتماع دشمنان
15:10
۷. غیب دائماً در کنار ما و در حال امدادرسانی به ماست.
16:22
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/655333" target="_blank">📅 21:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655332">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
خبرنگار کانال ۱۳ اسرائیل: در دفتر نخست‌وزیری سکوت حاکم است و اینکه رئیس‌جمهور آمریکا عملاً اداره اوضاع را در دست دارد، باید برای همه نگران‌کننده باشد
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/655332" target="_blank">📅 21:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655330">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_76QNzAvqgmXV6m0jN-beOrfFHucrhHxFl98BI5p_Ytu4Xyvr_Eidmqbzw3lPg5pGDG57IxgaXPDMrwK4nyBm7TLfTpQBdU0B5QDBDKVU0U8gs_GoPMaK8z4Sqi87Ox48T0sI9jCl4ifvGZ_hsllZUhjmGhCJd8V2W01tAkcFSnZJ_Z6fQbqqmjUphzehBujyiyaiijF42WEhPIQ3tEsl82PD5iJwdfLGOtpV9WRVdAzdcgvxG76ObxtO-GELlFZZDjMc4BdsHzCOYClxCM5vTn-iovnQgiEWV4CvVPUS5S6C_AxZU71IOdzNdgUlLzgvlDBPb7E6WOL4fbHCGmzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ متوهم مدعی شد: من تماس بسیار سازنده‌ای با نخست‌وزیر اسرائیل داشتم و هیچ نیرویی به بیروت فرستاده نخواهد شد، و هر نیرویی که در راه باشد، قبلاً بازگردانده شده است
🔹
همچنین، از طریق نمایندگان بسیار عالی‌رتبه، تماس بسیار خوبی با حزب‌الله داشتم و آنها موافقت…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/655330" target="_blank">📅 21:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655329">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQAgL2HXllyCdsGCjf_9YLkVarRMDwlfYFImEaPzNNk9wTB7XTZ8ww_WubkIp8-YmkKvJM2vzvSNjMVReomOFK-S5faCRh_n9XXtd7NgAZIfVHLt0bTwx1q_euZCCec35ZJoB-PfyALoPmfPY4qYrvjCAyRbWA6kdmmvw8vx3kmZBXZxkqW3-OwZoMd99bu_AR-60hjzb0hqN03RQ9diVseLU3UICE-vVlNfBTk1wzAN26EvRpaaG0V5_45Ap6h67F7hs4JFAvI1SmW4vAU37rDt2haXtLXt3nGqGvH2VmPph7iYOXnu5uKKA-GEoZ8HxezuyB37Jy_NG916xQ3AsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
اعلام برنده قرعه‌کشی برگشت پول 10 خرداد
🎉
تبریک به برنده خوش‌شانس،
•
آقای غلامرضا رضائی
کافیه بیمه‌تون رو از
اپلیکیشن بیمه‌بازار
بخرید تا وارد قرعه‌کشی روزانه بشید.
✅
شاید این‌بار مبلغ بیمه‌ شما تا سقف
۱۰ میلیون تومان
به حسابتون برگرده!
⏳
فقط تا ۲۰‌ ام فرصت داری
❗️
📲
نصب کن و تو قرعه‌کشی شرکت کن
👉
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/655329" target="_blank">📅 21:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655328">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgdaZ1v6Cv1gO6xOCCeaD67ZXd0A_SywV3RTmutGfoSHDHu2cDzxGlfuRDmCVCAiVEEmnf9gxw05ACUKUVcOquoSZSNhhrvVBTRpkeX7uUe0SugQ6Y9hA6L5_VLWpbGCm1jc40uIT32Gvx1xH8d04tGMkIUd3orOVbQIO5lEyq6egXygQxfYEZMsQkSIMilDJ0j3PPnjNytOg9prAlYOPpyYA6QaT95tar8KLz_lemwqyo7f6xw-RFIVoTX-5giq-bUyPvI2VGzAdUMXmYdlTenI7hFGCUFjQiOTqcPXsczDIiWd0e0tbN8BEDlFzdziji5u8rugIno9raf7KTmlmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ اعلام کرد که حملات رژیم صهیونیستی به بیروت متوقف شده است
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/655328" target="_blank">📅 21:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655327">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ادعای دونالد ترامپ در واکنش به احتمال فروپاشی مذاکرات صلح با ایران: «راستش، برام مهم نیست اگر این مذاکرات تمام بشود» #Devil
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/655327" target="_blank">📅 21:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655326">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltPKdDDVern8HIE7RvP26BZ37FywhrVf3-uIt4Ot5yqAw63HhU-qWXxqrRmGLSWkInxd54owzXCyw6736IWkp_qrK3JHLoMpwcoRKlFqWTUMFQVsUQAq_lqSZD1ptjjYaFE24VDL6BH7cFUOptcAl5H0XyzWGVrgR_tNCUmFlVMPku2O4ZXFB8nRERjC5s92FyT79kEQ0Kne3FVLaIYaqDoWUR7_ZCwtEZBsmPd0LPbMfwMwfzjyMuysSAuPxwdPPWBvhoj0BwPYGzjklUzI7f2ehvSsk0W5eLyUO1ItVTImkfqFT5QKytZBAPD0ZRM7QGk8ParkC4_OBqghgKEj0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ولایتی: بمباران ضاحیه ونقض آتش‌بس عجلۀ رژیم جعلی برای پایان دادن به تاریخ نحس خویش است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/655326" target="_blank">📅 21:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655325">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
هشدار برای توجه بیشتر به اعمال، حق‌الناس و سبک زندگی
🔹
00:24:30 مشرف بودن به گفتگو و رفتارهای اطرافیان در حالت کما
🔹
00:31:35 حال خوب من با التماس دعاهای پدرم و صلوات‌های خانواده‌ام
🔹
00:41:15  ورود به تاریکی مطلق همراه با ترس و اضطراب
🔹
00:46:30 همهمه بین انسان‌هایی با ظاهری سم و دم دار
🔹
00:52:00 لحظه سخت برگشت روح به جسم
🔹
00:57:20 به حسابرسی در آخرت اعتقاد و باور نداشتم
🔹
00:59:00 تغییرات رفتاری تجربه‌گر بعد تجربه
🔹
قسمت چهارم، (ورود به مردن)، فصل چهارم
🔹
#تجربه‌گر
: سید ابوالقاسم احمدی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/655325" target="_blank">📅 20:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655324">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMcaWGUGlc6oVuBa8jyOmpEo2uKal73EVTQ5WHOu0loDkMWWuRFzHzhY8S628QPCiNSsSgRfdtlInWEwBHMXygCynYKQTOxTmz4gal9oPDob4hNy7wK7xdu0DeBlQsRF0qmq389_91PVo7kCRlTih0a9PeB_R7vEWziXhXxnMZw76ZXM9hWzryUhXh1SL8gtfCSNYK0mmpWqjqX5ADF2Xgen8iQ28adVrnoyxbHP3TSan5kMv-sKodCGEBqstcCXJ6x-9GcdmGlRHJuftbYCBZarSACdL1_2tS8RWkRHZqrTSthN20zXArqxynxOx4cJ60pyqamxno7tB6OdFuFqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت خارجه در خصوص نقض مستمر آتش‌بس توسط رژیم صهیونیستی و آمریکا
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/655324" target="_blank">📅 20:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655323">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ترامپ ادعا کرد اگر گزارش‌ها مبنی بر تعلیق مذاکرات ایران با آمریکا درست باشد، «اشکالی ندارد»
🔹
فکر می‌کنم ما زیادی حرف زده‌ایم
🔹
این به آن معنا نیست که ما برویم و شروع به انداختن بمب کنیم، ما فقط سکوت می‌کنیم؛ محاصره را حفظ می‌کنیم/انتخاب #Devil
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/655323" target="_blank">📅 20:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655322">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhA42wMxanCW6maaqe0LLewLipTOXFgq9V4wmtEQzdwzMjYbH8qbYc3Rt-_a9N4-S82jdMytlWZuNAky-10xC9T9FS01qdgJsF8EpxqIMOddDhF733AH7RHHfS_TOnWkFqO42Ft5o8wY90uaHdMFLjqJ1UcSuoJCxN_fMPZ8sp8xiU4PZOPEs_4RsAIszbuZl_ADMXz4doveIh9O1wRH738KXpWRlbEL-XVsAC10rmg8eMxUHwZGV-7Hlw3p4PY9kufgi2D281iajqsErzD2oYFQ2zaSbv-4jN4zdR6SupTP5Q-4XFSI2zTV7mQOh0hW_C7uKinsE_cCa0o8iSWNMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕
بیش از ٣٠٪ کاهش وزن با داروی جدید داروسازی دکتر عبیدی
اپلیکیشن تخصصی «مان»
با همکاری داروسازی دکتر عبیدی، با استفاده از دارودرمانی زیر نظر پزشک و ارائه روش های ساده برای بهبود کیفیت زندگی، توانسته برای بیماران خود
بیش از ٣٠٪ کاهش وزن
به همراه داشته باشد.
آمپول لاغری زیکورپا (ZCorpa)
به‌صورت تزریق زیرجلدی هفته‌ای یک بار استفاده می‌شود و مصرف آن باید همراه با رژیم غذایی کم‌کالری ، ورزش منظم و زیر نظر پزشک باشد تا نتایج مؤثر و پایدار حاصل شود.
📌
فرآیند درمان به صورت کاملا آنلاین در اپلیکیشن
«مان»
و تجویز دارو تنها با تشخیص و تجویز پزشک انجام خواهد شد.
🔻
مشاوره رایگان با پزشک</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/655322" target="_blank">📅 20:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655321">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1Xve8rmvR6phGsfs8uyGIeoZ-ifXQbpAohN7RC25_GZoljKHplPsUCcUhblqZe2zmwdaK0lK7pqxwfx2rzeXUEzK1OQaC2vlNlg2rnRjlg5n8dTjy_8I-hEAwl6eRD2kZF4VzUJSckAJS6rVEpk8VUUIZ_q9IfZV1j4cDAvfQX79cMcxHu_-0lltBMnxRxeKXosfinkjqiXN8U0AvjMZ0405gG0nFz72UBeBeenKSNrK-_yarVmLrD5G117mrFrlVFmZxXTfrYLKirEu2hI2HsDopw6cOdo4DEbXAJADiwUUUtTwKXMTtyPX77Fw-LY-luGEt8nYmRFo0tl44v7yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کفایت مذاکرات
🔹
بر اساس اخبار منتشر شده تیم مذاکره‌کننده ایران در واکنش به تداوم حملات و نقض آتش‌بس از سوی رژیم صهیونیستی روند گفت و گوها و تبادل پیام ها از طریق میانجی‌ها را متوقف کرده است. گفته شده که توقف تجاوزات در لبنان و پایبندی کامل به مفاد آتش بس از شروط اصلی بازگشت به مسیر مذاکرات به شمار می رود. در همین حال ایران و جریان های مقاومت اعلام کرده‌اند تا زمان تأمین این مطالبات گزینه های میدانی و راهبردی خود را حفظ خواهند کرد. گزارش‌ها همچنین از بررسی اقداماتی نظیر تشدید فشار بر مسیرهای راهبردی دریایی از جمله تنگه هرمز و باب المندب خبر می‌دهند.
🔹
هفتصدوشصت‌وچهارمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/655321" target="_blank">📅 20:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655320">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ادعای شبکه کان اسرائیل: حمله به حومه جنوبی (بیروت) به دنبال دخالت آمریکا به تعویق افتاد/انتخاب
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/655320" target="_blank">📅 20:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655319">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ادعای شبکه کان اسرائیل: حمله به حومه جنوبی (بیروت) به دنبال دخالت آمریکا به تعویق افتاد/انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/655319" target="_blank">📅 20:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655317">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DSHRdeexpF32jgHrzvWW5SGBC0vDHyC7TFZiPQeCMu5u50xhb0K0_PLAkaybVCyNzbWgwWZAHf1tw4nzUdfNqm2e8WCCw3ztzr5ay7X3OY3Ql1weFavc_WoMfeSYIrYRK_ELaXtok0w8PFezWx9z90UIMG0F2drrNLduQPVDcBiYdthtwASwfvI1cXMlHgPAU5CrLXRwT2bJzCmWDs9B2kMVMYkY7iUKtcB1oLUPL3TtUpJZ5r3y9ls_IcZxXhQHtGDA3z8ZV_Nui2Q4MX9Gae4iFbBjt-OrWVbuwXkdzU1sCOBnom8H8WMHAboJPRoKBa-0jbvewsrvM3oQwKyPXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gs8iYfECbliXxwy5BX6YdiYAEZ3S0JcxKKbOt3xHCvHXukaaRajNJtBzXdBWuhLOiT9BkfMIsRrzD6sgzrKhvqb_LNGLwNhRsnzVGGcWdGZ44K4Pu1fS_u_r1OOSoGgh_E3_PGNfU7BCKb93SiqfcKMVEbxuEzngMAKfTgA3yjxpbs499FLLKAS-IwzZnjOsqL8XlaM7bD_rK1tU1-HbVTiIO7ozpPNJSQ0YposPTS7-ijtL0tGUPEOkvFS-veeW-WeBPdi2MAiSKxiEVLh0AxQECcXM1ULzY4wHyp9CljnOxUTELWlhCxf6cpiFyF9k1wIUEyherYF6L5NPen2EIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📚
نام کتاب: ته کلاس، ردیف آخر، صندلی آخر
🖋
نویسنده: لوئیس سکر
🔹
اگر فکر می‌کنید مدرسه فقط جایی برای درس خواندن است، «ته کلاس ردیف آخر صندلی آخر» نظرتان را عوض می‌کند؛ روایتی طنز، صمیمی و پرماجرا از نوجوانی، دوستی و روزهایی که هرگز فراموش نمی‌شوند.
🔹
این کتاب به نوجوانانی که می‌خواهند کتابی روان، سرگرم‌کننده و درعین‌حال تأمل‌برانگیز بخوانند به شدت پیشنهاد می‌شود.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/655317" target="_blank">📅 20:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655316">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/082de9a0a2.mp4?token=d-T7_QRlQ8zUv0cLKRZSDfZG4gPdGCwqav5KqBAP2g2oO6F28-f1HItLiGcpjObLThfBdEjqGuTzar4UKAGL-sg9MLnMIO-uVRkvl6zkdDSytFgUHes24mOAukjAbvr0oeT7-K9lqUZ2iGQ5uCJUB40Y8liYdacrJG-NWq-QhTn2i9019_-yz9vEF5pjfaMzpeYgWEVqBcNOnH6hrIIMYjyFBJfpYkB_v3fmWNXBT5gAqjNqTpuyHQwgGcdoR_ZbCxqYxQVsV4SE9-jARkKCuxIDC5oGTPK_Vudc0OiNcPg79bN3LJ3oKqfzIW5eYgRARJah6KRZ3IhQwaoOjpcdqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/082de9a0a2.mp4?token=d-T7_QRlQ8zUv0cLKRZSDfZG4gPdGCwqav5KqBAP2g2oO6F28-f1HItLiGcpjObLThfBdEjqGuTzar4UKAGL-sg9MLnMIO-uVRkvl6zkdDSytFgUHes24mOAukjAbvr0oeT7-K9lqUZ2iGQ5uCJUB40Y8liYdacrJG-NWq-QhTn2i9019_-yz9vEF5pjfaMzpeYgWEVqBcNOnH6hrIIMYjyFBJfpYkB_v3fmWNXBT5gAqjNqTpuyHQwgGcdoR_ZbCxqYxQVsV4SE9-jARkKCuxIDC5oGTPK_Vudc0OiNcPg79bN3LJ3oKqfzIW5eYgRARJah6KRZ3IhQwaoOjpcdqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شری بیگز، نماینده کنگره خطاب به منقدان جنگ ایران: ایران نباید سلاح هسته‌ای داشته باشد و ترامپ آمریکا را در اولویت قرار می‌دهد؛ اگر این کشور را دوست ندارید، بروید بیرون
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/655316" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655315">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
شبکه ۱۲ رژیم صهیونیستی: نتانیاهو و ترامپ طی تماس تلفنی در حال مکالمه درباره مذاکرات و  اتفاقات اخیر در لبنان و ایران هستن
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/655315" target="_blank">📅 20:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655314">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ادعای ترامپ موهم به خبرنگار ان‌بی‌سی نیوز در مورد ایران ادعا کرد که در مورد گزارش‌ها مبنی بر تعلیق مذاکرات از طرف ایران چیزی نشنیده است #Devil
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/655314" target="_blank">📅 20:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655313">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ادعای ترامپ موهم به خبرنگار ان‌بی‌سی نیوز در مورد ایران ادعا کرد که در مورد گزارش‌ها مبنی بر تعلیق مذاکرات از طرف ایران چیزی نشنیده است
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/655313" target="_blank">📅 19:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655312">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U27Pkvdl1Xj7Apxho_nUkTZvKk502f8LYK6b4ByO0J2ZW3iS0GXoIojo5qqMTq2No9D4-GWVertzUNyb_lrGPTKMtEojB3jcgIn5sVtbDcBf_LZgBDWlezty0xuztubWEQp3jhRDXdSYmCYR9na6z16Dntwn6ZSqz5WucImrJ7wFagyoJxrLTifqPC1lIuJSUHImR-3iWChlHHHpG7FlSUB8vp8LN4OV9FAve6GrkRK8olmvp7A2lYYEJMJ0Qji2GG3Q7DOgpmgDgAZOg5K1_1H19EVGBh1hPZxyZRap1XHpyVLX_aOdYlSMkCYayV0kKsszWw4raMVB1b3hCgc2pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت پرده خبرهای جعلی درباره مقامات ایرانی چیست؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/655312" target="_blank">📅 19:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655311">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
معامله‌گران آمریکا شرط بستند؛ ۵۳ درصد احتمال توافق با ایران تا آبان
بازار پیش‌بینی Kalshi:
🔹
معامله‌گران به ارزیابی احتمال توافق ایران و آمریکا پرداخته‌اند. آن‌ها شرط بسته‌اند که شانس حصول توافق تا پیش از نوامبر ۵۳ درصد باشد. آن‌ها همچنین احتمال توافق تا پیش از اکتبر را ۴۴ درصد و تا پیش از سپتامبر را ۳۰ درصد برآورد می‌کنند.
🔹
معامله‌گران همچنین در حال ارزیابی زمان بازگشت تردد در تنگه هرمز به حالت عادی هستند. بازارها در حال حاضر نشان می‌دهند که احتمال بازگشت به حالت عادی تا پیش از سپتامبر ۵۰ درصد، تا پیش از اوت ۴۱ درصد و تا پیش از ژوئیه ۲۳ درصد است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/655311" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655310">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
گفتگوی تلفنی وزیر امور خارجه با مسئولین پاکستانی
🔹
سید عباس عراقچی وزیر امور خارجه جمهوری اسلامی ایران در تماس های تلفنی جداگانه با محمد اسحق‌دار معاون نخست وزیر و وزیر امور خارجه پاکستان و فیلد مارشال عاصم منیر فرمانده ارتش پاکستان در خصوص تحولات منطقه ای و روندهای مرتبط با آتش‌بس گفتگو و رایزنی کرد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/655310" target="_blank">📅 19:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655309">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSBObIkW0qkZ0UBYyG3atzCtToEP5pXpJ0jDBx9xu9-HFVOgVXUDAQcy0kaRO_JULzPLIm7sVgYgglme4qXUGSeBFhi40hcxVtNTjR1taFlTV69mPSZwwjVthCQv3_nQyBYEG0FghkUl4vUrPRFrrzZeP0_Od_aZBYX37S4AoXQT2v92LQdikpe2WkDuI3927L_ewAYW_rOBuGP_Dfv7A0YV1PSTFsO1DI4Qi7fzOw4zniLWQ5NiDnEiV7vPITnA3MGH_sQnfHyvYwuBPAMVixJBwZCEF4ZIGerPqsvtlU7ztyEcnAWGIOEO8XRsLUV9ppEZa1zXH4oSiswVhR-Fpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حساب سازمان اطلاعات سپاه: هرکه باد بکارد، طوفان درو می‌کند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/655309" target="_blank">📅 19:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655308">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FivfXs0NLR8yS5zoL9vjZZJjJiTFl8P1Ccpi6DDYwSF5zhLfCBq8kHhx5UQF6YZybncQJIIGl_cHjnhmtwJ9N714JQs8XLkwJnPS2G0YxvAouk6yQYUHj0a2sC8UKRDTYqAQu2a-nhzfEmZliTiubwsy_rl3aRJhnX2o3rLz6uHoN0gsvVRFoGvPOl9rY4qJ7vjCcyPx5-oaFS-INekQojNSddlbzcNBMZWYznwLwKfFrWKJT_MXWmOba4NkN6v2ESiIwXWK6xbPSILJK8Yh8O9dsa7GrW71knDZep1IMhIIWTJhe1i6Byt-snm-AYtz1jMKo3bVDaoE9AbA1x9naQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رضایی: صبر ایران حدی دارد/ ‏تنگه هرمز تحت مدیریت ایران است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/655308" target="_blank">📅 19:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655304">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8qazJoglHK4eBxV5BWJxpwdN6nJcEoOD5iub8K-wdF60cBeA9pzFXD0Jotqjt2c_HzK_9YBUkWvpODzy2V1rURWIsopVpka89evCQa27ZjYwgYZg6StkP_6s_3XvUbwjmQWbGLQ4Fsfyo1CipaLvf9z_2XUZyzc5oUCNu5JC98H4dwB3vanJCQI04xhcbeKFRkhgEPxUcRDuF7bZgrHxN1Jl1sUqhdVb1wi6bEZLIHCZc51rJUUVFsrzlhYf6BkKKXYyuY_E2i9ozcNIrlIahnOcNGUUvT2m50NGTsrLRFRJS7MsmemnOKNEM7nRk0uaD4DEbYtq__eXwlvXhQsCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf574d3d4a.mp4?token=iTADf2YQ2OkYAW6PW9SSiQfHCe7p-pWH34NiyS2AO2ETpvTEVwzyakbnZDS1vXWt9yYWAZp5FSwZhcvtmLzeJ5SXT21f52CPvrTRqS9HSUa2P-PTAw90kMnTqu5rTyPuiUhnStSIOuwzDXCEDNHAngRfHsKV2-iZmFGCYS6H-hY8SpbgPxL4Lvy-f33WLbizhHNdePFosS3myE7mMfdUMJu8yKHTzvWfxFTo6IaANuSxuHA6ciH5wDHKtchb_k35SMR0ODL3KgJU6oa-i4ksRGI6PP6m-po3K18A0_DD7GtPJ6usU1cX8bIgY_baMufTA6Xz6kCZj3d-Jw_N-p2Mcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf574d3d4a.mp4?token=iTADf2YQ2OkYAW6PW9SSiQfHCe7p-pWH34NiyS2AO2ETpvTEVwzyakbnZDS1vXWt9yYWAZp5FSwZhcvtmLzeJ5SXT21f52CPvrTRqS9HSUa2P-PTAw90kMnTqu5rTyPuiUhnStSIOuwzDXCEDNHAngRfHsKV2-iZmFGCYS6H-hY8SpbgPxL4Lvy-f33WLbizhHNdePFosS3myE7mMfdUMJu8yKHTzvWfxFTo6IaANuSxuHA6ciH5wDHKtchb_k35SMR0ODL3KgJU6oa-i4ksRGI6PP6m-po3K18A0_DD7GtPJ6usU1cX8bIgY_baMufTA6Xz6kCZj3d-Jw_N-p2Mcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله وحشیانه ارتش اسرائیل به ساختمانی در نزدیکی بیمارستان جبل عامل در صور هدف گرفت که باعث تلفات و خسارت به بیمارستان و اطراف آن شده است
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/655304" target="_blank">📅 19:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655302">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">امکان سرمایه‌گذاری در صندوق طلای «ریتون» به ویپاد اضافه شد
ویپاد، دیجیتال‌بانک پاسارگاد، در ادامه مسیر توسعه فراگیری مالی، امکان سرمایه‌گذاری در صندوق طلای ریتون (با نماد بورسی ریتون)  را فراهم کرده است.
صندوق طلای ریتون، گزینه‌ای مناسب برای سرمایه‌گذارانی است که با ریسک‌پذیری متوسط و نگاه بلندمدت، به دنبال بهره‌مندی از ظرفیت‌های بازار طلا با هزینه کمتر و به‌صورت غیرمستقیم هستند.
مشتریان ویپاد می‌توانند پس از ثبت‌نام در سجام و دریافت کد بورسی، از بخش خدمات پیشنهادی وارد گزینه «صندوق طلای ریتون» شوند و «صندوق سرمایه‌گذاری طلای ریتون» را انتخاب کنند.
ویپاد که توسط داتین توسعه یافته، تلاش می‌کند دسترسی به فرصت‌های سرمایه‌گذاری را برای طیف گسترده‌تری از هم‌وطنان تسهیل کند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/655302" target="_blank">📅 19:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655301">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
هشدار قرارگاه مرکزی خاتم‌الانبیا به ساکنان سرزمین‌های اشغالی
سرلشکر خلبان علی عبداللهی:
🔹
نتانیاهو در ادامه شرارت‌های خود در منطقه، ضاحیه و بیروت را تهدید به بمباران نموده و برای ساکنان آن هشدار تخلیه اعلام کرده است.
🔹
با توجه به نقض مکرر آتش بس توسط رژیم، در صورت عملی شدن این تهدید به ساکنان بخش‌های شمالی و شهرک‌های نظامی در سرزمین‌های اشغالی هشدار می‌دهیم اگر نمی‌خواهند آسیب ببینند منطقه را ترک نمایند./ تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/655301" target="_blank">📅 19:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655300">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZqfMtSkl0dprZjNcPEG10p-XEHpk5_GGFxZLprIvxixL38E_MkPcc7dGoI9EHLKHlSyGNhouxfy0Oj59gOlfL5845L_7nYMDll44Y69yWKuuPeJoApTjbPVguef05-tmWK1w-5F-O0mvgpr0ttK-1ZHi_HWBKnPWi5iRNzXc9yKkRlqYvi81o6w2Lc9hzI-T9iW_MsjCxyRnPiGNvSYc_tLCcK6k-A9NdAyMM2wdCTJ1iUAS6CRHGlF9GJI_fYMsNgWLtPRNTIzViG9rSp805CNufTnUAOQ6gK1l8T0TKpivPlLbkNSXznGBnIyhgUIKb2w6_XbHbiXiCelKnvE3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/655300" target="_blank">📅 19:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655299">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
گفتگوی تلفنی وزرای امور خارجه جمهوری اسلامی ایران با ترکیه و قطر درباره آخرین روندهای تحولات منطقه ناشی از حملات تجاوزکارانه رژیم صهیونیستی به لبنان
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/655299" target="_blank">📅 18:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655298">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
گفتگوی تلفنی وزرای امور خارجه ایران و فرانسه
🔹
وزیر امور خارجه جمهوری اسلامی ایران طی تماسی عصر امروز دوشنبه با وزیر امور فرانسه در خصوص آخرین تحولات منطقه ای، تجاوزات رژیم صهیونیستی به لبنان و پیامدهای این اقدامات تجاوزکارانه گفتگو و رایزنی کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/655298" target="_blank">📅 18:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655297">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe9be0f41.mp4?token=dcYoOWIIAEGIF_LMVzGsp7ctwbbojUBnGXwGj3XPopYQ3HQRf_Xbrm4G4N32NbJsTCQgLw65If3jO5jrWGNWukCHxcsh4HxQ05I7vYS-qHb567KbqnG2ii3Ogv87UU2939QH8f15UqHvyp3hivULH_Af7-G94md9XPEbeqmOMYs7P4VBcI7m27DrvE5oSL1Tq8-f111XvnQLMD93My-Q2mJnts1TVFrn3i2LiwUIXjP66AIWrd0_JJ8-Ctg0Ox3x8MXm_fb5liV_f_rfmjV5Mc6_zLaUYqF6ImM46LuG5WgxKpZNIaFcYtLPx9IFmHdhsX2Fsq6gdcrm44yOK7KLvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe9be0f41.mp4?token=dcYoOWIIAEGIF_LMVzGsp7ctwbbojUBnGXwGj3XPopYQ3HQRf_Xbrm4G4N32NbJsTCQgLw65If3jO5jrWGNWukCHxcsh4HxQ05I7vYS-qHb567KbqnG2ii3Ogv87UU2939QH8f15UqHvyp3hivULH_Af7-G94md9XPEbeqmOMYs7P4VBcI7m27DrvE5oSL1Tq8-f111XvnQLMD93My-Q2mJnts1TVFrn3i2LiwUIXjP66AIWrd0_JJ8-Ctg0Ox3x8MXm_fb5liV_f_rfmjV5Mc6_zLaUYqF6ImM46LuG5WgxKpZNIaFcYtLPx9IFmHdhsX2Fsq6gdcrm44yOK7KLvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواپیما پس از ظاهر شدن کلمه «بمب» روی بلوتوث، در میانه پرواز بازگشت
🔹
در پرواز یونایتد ایرلاینز به اسپانیا، یک نوجوان دستگاه فیت‌بیت خود را «بمب» نام‌گذاری کرده بود که باعث هشدار امنیتی شد. هواپیما به نیویورک بازگشت، مسافران دوباره بازرسی شدند و پرواز بعداً با خدمه جدید ادامه یافت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/655297" target="_blank">📅 18:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655296">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c5ca40c9.mp4?token=u63pRXEYX_SWhqIJjVWv1ODOZOZogZN_GdHUEr15u2M0Ej6QWSFHJ3xVblh76ULijOW1nwJQCi2Sh96Fx6f2WlNO3mLDxIgjfL-_Oqb8Jz8Dnc2EPOW8sUnKHfJCsw8DQ5PpV8rBClbKjdEZcAaqjapXateGDlfUEwAhCCGJ6EENC8yt1_AdwqZgg4fM2SRiF4LBqck2QzvJ8wiF8L55rpA8OljZSP5U420C4N951sop3u3XQHCHWuPqwLrdpx_fF6dE36ZTUtA7XpDSDEdJym1xdf_JYQADBIZ-xDw9AiEMAbKAEK-ekz-6odb0fYGjhfx6MnLiyyH4asR9pWIdDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c5ca40c9.mp4?token=u63pRXEYX_SWhqIJjVWv1ODOZOZogZN_GdHUEr15u2M0Ej6QWSFHJ3xVblh76ULijOW1nwJQCi2Sh96Fx6f2WlNO3mLDxIgjfL-_Oqb8Jz8Dnc2EPOW8sUnKHfJCsw8DQ5PpV8rBClbKjdEZcAaqjapXateGDlfUEwAhCCGJ6EENC8yt1_AdwqZgg4fM2SRiF4LBqck2QzvJ8wiF8L55rpA8OljZSP5U420C4N951sop3u3XQHCHWuPqwLrdpx_fF6dE36ZTUtA7XpDSDEdJym1xdf_JYQADBIZ-xDw9AiEMAbKAEK-ekz-6odb0fYGjhfx6MnLiyyH4asR9pWIdDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساعاتی پیش، جنگنده‌های اسرائیل بیمارستان جبل عامل در شهر صور در جنوب لبنان را هدف قرار دادند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/655296" target="_blank">📅 18:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655295">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/328f576871.mp4?token=o31haD21_SK0cqRFcJpm8ScK3OdhLrsKZ_NGW_kQmIU4kSZzv3YSJVp2WYy4S1dy49JUQg_97-zdW9qxD_MJv-Co0xwtTRc66Y20EqwBlEeBZd74y4DvCRSRi5N_S-dO304AeqinOO7Bi1TTZDvaxey93sRqcRICEEiv6_de-IS7qXGWYcaBhFMteSpjqmWug0sChXzuir5AfzulV_YIuuy-Mgp6BX9PNpWvsVS31HBLwB2Ltr2jD_q_21XLxQmbSABKqEEtqh4VdjRPAlo22kc0hmcZCXZ8OYRGwkP7shrGJnQj6QORebKi6Yz8qHJLOWqJ17KMMKaw-ogb_Ml9nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/328f576871.mp4?token=o31haD21_SK0cqRFcJpm8ScK3OdhLrsKZ_NGW_kQmIU4kSZzv3YSJVp2WYy4S1dy49JUQg_97-zdW9qxD_MJv-Co0xwtTRc66Y20EqwBlEeBZd74y4DvCRSRi5N_S-dO304AeqinOO7Bi1TTZDvaxey93sRqcRICEEiv6_de-IS7qXGWYcaBhFMteSpjqmWug0sChXzuir5AfzulV_YIuuy-Mgp6BX9PNpWvsVS31HBLwB2Ltr2jD_q_21XLxQmbSABKqEEtqh4VdjRPAlo22kc0hmcZCXZ8OYRGwkP7shrGJnQj6QORebKi6Yz8qHJLOWqJ17KMMKaw-ogb_Ml9nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پروتئین‌های کوچک کینزین عامل ایجاد شادی شما
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/655295" target="_blank">📅 18:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655294">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f56rBLsEffiKZ6H4bOm567oMahE3dpU3BvCr1UdGQykv82m3v8DboQ6Lx2ydRmNWh9ndlYKmCNyemCKE1BWGlr11xQzyfqt5fE7zksqTv_gku0NvuFm4xNErrRe94ZsKrI2-h9hMpKSCNS-PudGRSBD_dhIrDb5CcZEoUIQlvSx92WOFKzNyBNbn-F6idOROOup1_LqO-lptyjDIC2Qi0jmSaRluNNTDRsNgJCVRUv8Ul8dERwRTRd3SX_RwpNCiRl7QKARAGzKsYcmKqQPjBNiYiDMnm6QX_9V3CZlJa5x9DOldgUYn1WdbLj8-EdPv9xtVkc6Iua84pGehio7Abg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هوش‌مصنوعی معمای ۸۰ ساله‌ای را حل کرد که ریاضیدانان نتوانستند آن را حل کنند!
🔹
برای اولین بار، مدل‌های محرمانه OpenAI معمایی را حل کردند که ۸۰ سال ذهن بزرگ‌ترین ریاضیدانان جهان را عذاب داده بود.
🔹
ریاضیدانان پس از دیدن راه‌حل پیشنهادی هوش مصنوعی، از همان ایده الهام گرفتند و گام‌های بلندی در مسیر حل مسائل بزرگ‌تر و فراتر برداشته‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/655294" target="_blank">📅 18:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655293">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
شبکه ۱۲ تلویزیون اسرائیل: مسئول روابط خارجی سازمان جاسوسی موساد در پی تغییرات مدیریتی
🔹
سقوط بازار سهام آمریکا از بیم از سرگیری جنگ
🔹
پرداخت ۵۰ درصد از مطالبات گندمکاران به زودی
🔹
گفتگوی تلفنی وزرای امور خارجه ایران و بلژیک در مرود مورد مسائل منطقه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/655293" target="_blank">📅 18:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655292">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKinTYxbCYqKlVcjRc7lLOll0UniVHjZGwqLcK1WsZPYvOZ-UPCWL1FuSKRmaKI7qyx-w15UF-b6YYa869wbuQU7xiIpCLCOcgms7XYzzbxWcYSyZ-8rF3es9yIq73nnWx9jqmcffxDlt5DfA4Evb5PmdTpB5j-uC6oG0CiGc_FN4l_WyuPV4le9XnOcaNXoFARm6Z3ljzEn9i3HMfV-bWB4x5V0Q4eArkYNh-nJfClHXwRhA6n0ewneA3B09-6bTrH7drXYV6EOQnpnOaXNNRCZhmOY8a41kUGLX52ZG951kfmtQh2zAc4Xb0v8ANosRt1n2YBNiThVUKZJMhcK0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با پیگیری استاندار آذربایجان شرقی محقق شد؛
افزایش محدوده تردد خودروهای ارس‌پلاک به استان‌های شمال و شمال‌غرب کشور
با پیگیری استاندار آذربایجان شرقی و طی امضای یک تفاهم‌نامه، محدوده تردد خودروهای دارای پلاک دائم و موقت منطقه آزاد ارس، علاوه بر استان آذربایجان شرقی به سطح استان‌های اردبیل، گیلان و مازندران افزایش یافت.
متن کامل خبر
👇🏻
https://t.me/araspres</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/655292" target="_blank">📅 18:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655291">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5hD37MpOjTWww7FcacfEgELIS511aBybEcU61KRK7worNzU7mq_hs5K5H66pw_jNA65YHwLA0wmtyKl0ru-SUDYp2Cpu2WjA_oyyVWeW3-zyFtoMNdnVQorE_JrfbF_jU6-fj_ABu1c5v_Ek2GgTLkFJHY9KGzOOYYKoXyB3hI8lhb3bOzm1wDkaGxRSTg-3aMsD7Zxi8HKCyvNG1nSc36tAJOsbMiIL9PkWrOGUt9bBC1wBAI35HWSwPivSwlpYiB9MAESyh6wGbNmab8RhDdme8mLveihDPyBCtUMXK0RZ0vwpGojY_fqaU9pMCf3DiydX4eHBUyeX7hJ4R89EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنکور الکترونیکی می‌شود؟ / بهای شکستن مدادها؛ زنگ خطر تجربه ۳ کشور در برگزاری آزمون‌های مجازی
🔹
در سال‌های اخیر قدم برداشتن به سمت کنکوهای الکترونیکی در برخی کشورها آغاز شده است. اما آیا ایران شرایط برگزاری کنکور الکترونیکی را دارد؟
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3219186</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/655291" target="_blank">📅 18:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655290">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTDBIAxPeyqkgSJZgMfKJeQn7C1zh8ZH-Mj8OvUsJOAC7xI27sP9jXP-D8A2UMDxPrMRwjuGwKn32djU8z1zKSO9R3xESeduGKmIX_qQKVlEnfd130fcbLA4fy3J67_hGhU1qmwogBfQPLLXBmZDu4ZbDHRCMdrTVxzcAQ2B9MfFQK4gCxWt8Nk-bZe6-Oao0JLJdwhM4Dcz1X8IPcbnsgyhhKQExlSN11KGSp4t9suoYHKup0GtGD2A_kGNydlAmdL4Dy_7ABWh-XTLu8n44msUNuMsLl-Nx0e-qinKc5R3g_BrhpMHihCwxOMZtzJgqoNiNUz2oiiZmz5ITSpYDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصابت پرتابه ناشناس به یک کشتی باری در خلیج فارس
🔹
مرکز عملیات تجارت دریایی بریتانیا مدعی شد که یک کشتی باری در حین عبور از خلیج فارس، هدف یک پرتابه ناشناس قرار گرفته است. این حادثه در فاصله حدود ۷۴ کیلومتری (۴۰ مایل دریایی) جنوب‌شرقی بندر ام‌قصر در عراق رخ داده است.
🔹
بر اساس این گزارش، پرتابه به سمت راست (سمت بندر) کشتی اصابت کرده و باعث انفجار بزرگی روی عرشه شده است.
🔹
مرکز عملیات تجارت دریایی بریتانیا برای
دریافت جزئیات بیشتر درباره تلفات احتمالی یا میزان خسارت، با کشتی در تماس است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/655290" target="_blank">📅 18:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655289">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTp_KsV-IUokfrQphSddC5ZmKN9oNLcAeu2E7N6XCX2I4MvzbEAUTt7cxaQM1bzOkGrGSopFc48f3LSh_tuLF3LV3cj7G-GvQfihUIQImdXchEyrju9LoHRc2uv7MrbwBoa_s3kK0GQ47zsbkjgttGXkdl56HpaxPReZLfPdAo_ELZ0EMFoZHVVM2Wn8del0jhVMj2dj-J5Te5nyMPlO6copdj8HJ17mw4Adsf2a6bU16ANYkqFG73xl5UMmgFYibx_-hzEjl55PHz3fiHFFWVD4kdpucgb4Ry70MNB5xmQcEwcmHUDB8Zhnun-BJLX6F-o6h7TwLP9zWBMQv1Ymbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گوهرشاد بیگم؛ بانوی دانش، معمار فرهنگ
🔹
گوهرشاد بیگم، بانوی نامدار تیموری و همسر شاهرخ، از تأثیرگذارترین زنان تاریخ ایران بود. او فراتر از یک ملکه، سیاستمداری هوشمند و حامی بزرگ فرهنگ، دانش و هنر به شمار می‌رفت. با پشتیبانی از عالمان، هنرمندان و معماران…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/655289" target="_blank">📅 18:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655288">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnapp | اسنپ</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDQugKOLkAXT_K3_1Up_qlajr8itou2Vcxd4IBtR6cbYojoMc6_bFnyYH2OULxEcmLFy5DP-twCdvscG-XnU4IviMRiIdGo36HpNlLC0_a2T0ID-TGfWDaXpLWySIoXeRYCq_POyeWvRHjYlBmiJMkTEZohlyrtNBSMUYceQKDBEXJko7eYjZ5Z0o-d4cA5DnEBtM5bvphTw97yJlVrlSBwkGacEGOI4mbIUotf5yX386w1LXnEmJi9SDF1HhjwL4Dxs4b6AYEAsVK1CtTwE4yKzdb-xWqGkT0iZR1KUnzFGdE1f4bkNJH0aSz9mTAaP-bqf8WbKz4u5lY3MgIzhGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
اشتراک اسنپ‌پرو
یه انتخاب هوشمندانه برای
صرفه‌جویی بیشتر توی هزینه‌های ماهانه‌
است. تخفیف‌های هیجان‌انگیز و ارسال رایگان سرویس‌های «درخواست خودرو»، «غذا»، «سوپرمارکت»، «فروشگاه» و «دکتر و دارو» از مزایای این اشتراکه.
🔥
🎯
اگه هنوز اسنپ‌پرو نداری، کافیه وارد سوپراپلیکیشن اسنپ بشی، روی سرویس اسنپ‌پرو بزنی و با خرید اشتراک مورد نظرت هوشمندانه سود کنی.
🔗
خرید اشتراک
@Snappofficial
✅</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/655288" target="_blank">📅 18:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655285">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
سخنگوی ارتش رژیم صهیونیستی: ما به حمله در سراسر لبنان از حومه جنوبی بیروت تا صور ادامه خواهیم داد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/655285" target="_blank">📅 17:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655284">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سوء‌تغذیه در کودکان؛ ۳۰۰ هزار نفر مشمول حمایت می‌شوند
احمد اسماعیل‌زاده، مدیرکل دفتر بهبود تغذیه جامعه وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
طرح امنیت غذایی کودکان سه سال است که انجام می‌شود و امسال بودجه این طرح حدود ۲.۵ برابر شده و حدود هشت همت برای این کار از طرف دولت بودجه گذاشته است.
🔹
براساس این طرح کودکان مبتلا به سوءتغذیه که دارای پرونده در مراکز بهداشتی هستند یا به مراکز بهداشتی مراجعه می‌کنند، شناسایی می‌شوند. یارانه امنیت غذایی برای این کودکان به حساب سرپرستان خانوار واریز می‌شود.
🔹
این عدد سال گذشته چون بودجه کمتر بود برای دهک یک تا پنج یک میلیون و ۳۰۰ هزار تومان و برای دهک‌های شش و هفت فکر می‌کنم ۶۵۰ یا ۸۰۰ هزار تومان بود که امسال این مقادیر افزایش یافته است.
🔹
تعداد کودکان تحت پوشش با توجه به افزایش بودجه نیز افزایش یافته است. امسال قرار بود که تعداد آنها به ۳۰۰ هزار نفر برسد؛ درحالی که سال گذشته ۱۸۰ هزار نفر تحت پوشش این طرح بودند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/655284" target="_blank">📅 17:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655282">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ol1d_J5nXjgn_J3204jhJwRwC1qabcEUxyxt-KiVv9vLJSJvBsY7ro7dMsiSRvLRR75iI3KwKu1S8YmindhVaS-iV0BetgSI-yxhYz2Tmtt5Ji4VC3QxcrqKVNF4igSw2tgia-hTZnSa8w14G-cgnYbExen9920JaTjtBCM2wA8W-NtxQmV-ax0yWocfC4Bg5OrDS82VO7ould4saXwQY0L_5R2NFrsuACUwosnmlHxHij9qpQNl1yybTDY9RA5XwssC-PuwCMg7Cd7d615xuxkEXpLQu4HmgM24XC9QgzCsgHyf69YZd2bn6c1QITksdYxDLTy-_Yb7DrMpw8T-bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌱
در پناه ِ غدیر، در کنار یکدیگر هستیم
🔹
در یازدهمین جشنواره مردمی اطعام عید غدیر همراه ما باشید...
🔸
با اجرای: مژده لواسانی و امیر مهدی باقری
🔸
با کلام: حجت الاسلام برمایی
🔸
با حضور: حسین حقیقی
🔸
با نوای: کربلایی علی اکبر حائری
✨
وعده ما: ۱۴ خردادماه از ساعت ۱۹ هم‌زمان با شام عید سعید غدیر در خیابان فدائیان اسلام(بین چهارراه نخریسی و چمن)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/655282" target="_blank">📅 17:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655281">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
برافراشته شدن پرچم عید غدیر در حرم مطهر امام علی(ع)
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/655281" target="_blank">📅 17:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655280">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ارتش اسرائیل برای ضاحیه بیروت هشدار تخلیه صادر کرد
🔹
ارتش رژیم صهیونیستی در فرار رو به جلو، مدعی شده اگر حزب‌الله به حملات خود ادامه دهد، صهیونیست‌ها هم ضاحیه بیروت را بمباران خواهند کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/655280" target="_blank">📅 17:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655279">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
وزیر آموزش و پرورش: امتحانات نهایی احتمالا بین ۱۳ تا ۲۱ تیر برگزار می‌شود
🔹
تاریخ قطعی برگزاری این امتحانات بعد از تایید مراجع ذی صلاح اطلاع رسانی خواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/655279" target="_blank">📅 17:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655278">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
نماد کشورهای مختلف در جام جهانی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/655278" target="_blank">📅 17:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655277">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIuGbD3D-Jke6G4JMHIZgoBbkLoc03Jp0qaJAhwlYbdvGT45VHjeajVSYPXskyN1b_cNi-4vHUHSUPP4VmaZhYAioixwe-vJZrKIY8l6XLT9MZqsNGN9CcL_ywHnHYeulZ6m_Uvk04Fi1FTWpvX98LGVGbR29seZgVAwzhebc7j8m0AFekpfQ2xQzv52XPrt1AvRSjaFyEwd8Dpzig5ktDBhz0CmlLPfrD4XopzNUAXfkk0z7nzdlpcbKsLrBsejYQgl0bXJ2u0dm_39oWd_Zeuflk-UgAfXmAJybSdNve34m8gkZenR8Vtq8Bmvwf26futC8_AzPe4k_BX2RuL7Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای فاکس‌نیوز از آخرین مطالبات ترامپ از ایران
🔹
ایران باید بپذیرد که هرگز سلاح هسته‌ای یا بمب نخواهد داشت.
🔹
اورانیوم‌های غنی شده توسط ایالات متحده شناسایی و نابود خواهد شد.
🔹
تنگه هرمز باید فوراً و بدون دریافت عوارض باز شود.
🔹
ایران باید همه مین‌های دریایی را جمع‌آوری یا منفجر کند.
🔹
محاصره دریایی ایالات متحده برداشته خواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/655277" target="_blank">📅 17:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655276">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79b1982b32.mp4?token=M_uSqUE40YymWAkJF2cN3T3Lg7kWAFpiodzL2mt4a3Z-FZDN8L-m9du9acP27mtqerVgbC1NVoBGzsFbBOadh1DlZvBBplkGSNKmCgIA6gq46l4uv1MoWctuFqJwiaNWPXmsrGWPAuIGFu8QAarq4jIJFljnNCYNIBWFdsqFyjpJRcBoQrz4Tb2SxeFPknlb3GZb3FH_bfki2pELn1pGt_-SvX3Cwi0RzV6e-nrl-x8l_r-7hEdGAihQraAr1L1PIst26Q6lczZhavybtpR7HyyYiL7xFqem5dnjjIBj3ZQbeJkG0k2tqo1_bk3UAwTMPHa5KbDgZ9wD_2lSaY_WpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79b1982b32.mp4?token=M_uSqUE40YymWAkJF2cN3T3Lg7kWAFpiodzL2mt4a3Z-FZDN8L-m9du9acP27mtqerVgbC1NVoBGzsFbBOadh1DlZvBBplkGSNKmCgIA6gq46l4uv1MoWctuFqJwiaNWPXmsrGWPAuIGFu8QAarq4jIJFljnNCYNIBWFdsqFyjpJRcBoQrz4Tb2SxeFPknlb3GZb3FH_bfki2pELn1pGt_-SvX3Cwi0RzV6e-nrl-x8l_r-7hEdGAihQraAr1L1PIst26Q6lczZhavybtpR7HyyYiL7xFqem5dnjjIBj3ZQbeJkG0k2tqo1_bk3UAwTMPHa5KbDgZ9wD_2lSaY_WpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارخانه تولید مواد آتش‌بازی، خود صحنه آتش‌بازی شد
🔹
منطقه ساحلی سالینا در کشور اروپایی مالت امروز صبح بر اثر انفجاری مهیب در یک کارخانه تولید مواد آتش‌بازی لرزید؛ انفجاری که ستون‌های متراکم دود را به آسمان فرستاد و به املاک،‌ ساختمان‌های اطراف و خودروها خسارت وارد کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/655276" target="_blank">📅 17:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655275">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69515842e1.mp4?token=ctIzZe405wRx3WI_Y4xPNTaBnu2AoSTaGe7TH2_SDu-DLaixf2mV0eU2-uwVJE4doZmzl9aTTLdjN_ZLQW5IXMIpoVg3nFAGO0V4uvOYNfjLBmmcmkLMRUkWIz5JuVOLhvChJu8hkZ8iR7im1QIvSWtlhAX8IEj-CY3unVIHJ4IGMHrQDQvLHQ9NWAuY314OzUaPMoqcGdDePjE-SX2OlNbm7OtxhTVq8FHRmmx6oVPDnwENoXOEbyr5pJmG2rZWl1IMZlCS-XnYuw29cVLEuSknyrrjy5grJyTlPdNcOxdsSmZl9AzgVYpDQXi_ZYZ97OL9U09E4s9YGtwJmJGUlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69515842e1.mp4?token=ctIzZe405wRx3WI_Y4xPNTaBnu2AoSTaGe7TH2_SDu-DLaixf2mV0eU2-uwVJE4doZmzl9aTTLdjN_ZLQW5IXMIpoVg3nFAGO0V4uvOYNfjLBmmcmkLMRUkWIz5JuVOLhvChJu8hkZ8iR7im1QIvSWtlhAX8IEj-CY3unVIHJ4IGMHrQDQvLHQ9NWAuY314OzUaPMoqcGdDePjE-SX2OlNbm7OtxhTVq8FHRmmx6oVPDnwENoXOEbyr5pJmG2rZWl1IMZlCS-XnYuw29cVLEuSknyrrjy5grJyTlPdNcOxdsSmZl9AzgVYpDQXi_ZYZ97OL9U09E4s9YGtwJmJGUlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در جنوب تل‌آویو
🔹
یک حریق گسترده در منطقه‌ای واقع در شهر ریشون لتسیون در جنوب تل‌آویو به وقوع پیوسته است.
🔹
تاکنون جزئیاتی از علت بروز این حادثه یا میزان خسارات احتمالی منتشر نشده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/655275" target="_blank">📅 17:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655274">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMTr04A7eqjVJkTXjoIwo46i50MyEREVUxISxghWE1kvlrWCYAT8JepLAWfQHu1MCeGiK7JvRyfZPSA8hk1H_fJcXouM8f7-WC3Ae-_pdZ7_dY9oe4FiEeI_WLN7lyAwE9Mgz7vw14hkQchr8go7cW1jIJgRCGGZHsfvrUeFBfrvlWIL171zKn1JoDZ5J9nllPX0xDaIc-QTks-XlnF3wfRJ6KNuflHtZDDnMpXnYerWU-B1Rj0BUIQ4EAu-62pAWS8MFwCnUBu8hlXXPd3380g1goFJCM4k0kMXZpuvPX9uuM3nvMvQo-z138_ULicVyDJ9bCLw5uUDxDX5zQpF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فوری/ ایران تبادل پیام با آمریکا را در اعتراض به جنایات صهیونیست‌ها متوقف می‌کند
🔹
با توجه به تداوم جنایات رژیم صهیونستی در لبنان و با عنایت به اینکه لبنان جزو پیش‌شرط‌های آتش‌بس بوده است و هم اینک این آتش‌بس در همه جبهه‌ها از جمله لبنان نقض شده است، تیم…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/655274" target="_blank">📅 17:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655273">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
داروهای حیاتی و کمیاب را از کجا تهیه کنیم؟
محمد هاشمی، سخنگوی سازمان غذا و دارو در
#گفتگو
با خبرفوری:
🔹
در اجرای سیاست‌های کلان نظام مبنی بر تسهیل واردات و پایداری تأمین دارو، کارگروه ویژه تأمین کالا با هدف مدیریت فرآیند واردات هماهنگی با گمرک و بهبود حمل‌ونقل تشکیل شده است تا موانع موجود در مسیر ورود داروها به کشور برطرف شود.
🔹
در شرایط حاضر داروخانه‌های منتخب دولتی و بیمارستانی به عنوان کانال‌های مطمئن و جایگزین برای توزیع داروهای حیاتی فعالیت می‌کنند.
🔹
همچنین شهروندان می‌توانند برای استعلام لحظه‌ای موجودی دارو و یافتن نزدیک‌ترین داروخانه دارای اقلام مورد نیاز از اپلیکیشن تیتک استفاده کنند که این سامانه حتی در زمان‌های اختلال فنی نیز به عنوان راهکار جایگزین عمل می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/655273" target="_blank">📅 17:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655272">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwkmyKRdcFMdX3zmwAPJ249OyJlMGXVIYxOst31cJZu6rvQX0rVLYvki82-pC7LjKGTP7hrgPxFxFr-WJe7_uBt_OKjXa3YtsMAx88lROAOsltZVXwqp8asrKZhz2R1labNO1g79gM-HmQMRLfbl2q17hPZ7xl-7BTgxrsV6X1MWMfN5gQh1KNP7CuTKynkgx-6X1tA09p8TFwbmGQqs27FKoZYkjZh8t7HQTfCE96t5bAsQk61vM8947tFiMGQK28IL92hJQDZYLDQiY25DoSg8nUK8RL-71Y0Vkf8fUL8DnVNjT55TDbh00oCEUDBtunWREdvDZMZnnlNr-02jTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کانال ۱۲ رژیم: دادگاه عالی اسرائیل به اختلافات پایان داد و به‌طور نهایی انتصاب "رومان گوفمن" را به عنوان رئیس آینده سازمان موساد تصویب کرد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/655272" target="_blank">📅 16:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655271">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06ff15d4f.mp4?token=stLO-1jJI62xgjK_GwW3hdg4nV8y0JUj3EWvOv2hnkZpRVprK8Ep5oBtQnLaUyjDlZm_zItdm3QuTB6fV6EjforThrKjMzZVaVyHe_xwRiFMZs_RwOuaktdV1K9Mp7sgR7hIX4tlmCj_7t3P1vB__bEaaJtBuNaeqmx7NnQBCIfgBF3PfHups5YKjh5tVI7pjUrQ8ooBedsLEm5qCN2VnYHWcElBamKQjYItUf1IcwnWkgJtIPm6qgJNSC0TbUuwsg4cg3i2BIL8uWttuVXnduDji-SPlUIgPHGBUk3WHbm4fvoffLOLazqegg_iydjov7bdlbMeHudzR_BYYmdK_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06ff15d4f.mp4?token=stLO-1jJI62xgjK_GwW3hdg4nV8y0JUj3EWvOv2hnkZpRVprK8Ep5oBtQnLaUyjDlZm_zItdm3QuTB6fV6EjforThrKjMzZVaVyHe_xwRiFMZs_RwOuaktdV1K9Mp7sgR7hIX4tlmCj_7t3P1vB__bEaaJtBuNaeqmx7NnQBCIfgBF3PfHups5YKjh5tVI7pjUrQ8ooBedsLEm5qCN2VnYHWcElBamKQjYItUf1IcwnWkgJtIPm6qgJNSC0TbUuwsg4cg3i2BIL8uWttuVXnduDji-SPlUIgPHGBUk3WHbm4fvoffLOLazqegg_iydjov7bdlbMeHudzR_BYYmdK_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی: مردم آمریکا برای گذران زندگی، پلاسمای خون خود را می‌فروشند
الیزابت وارن:
🔹
مراکز اهدای پلاسما در سراسر آمریکا شاهد صف‌های طولانی از شهروندانی است که از طبقه متوسط هستند و تنها برای بقا به این کار روی آورده‌اند.
🔹
بسیاری از این افراد درآمدهای حاصل از فروش پلاسما را صرف هزینه‌های حیاتی مثل خرید خواربار، سوخت خودرو و بیمه اتومبیل می‌کنند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/655271" target="_blank">📅 16:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655270">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ede4f9d1e7.mp4?token=Ca3rmb1rLPBeXpefKmbKvV8iES0qgwl0KTREPifheidlrpGYeKKAqXPeqJpSyc3VJwHCrHp3A0UJghfPoSF_uFMGhXnX1Wycu62E8loZHLs8KQ93MniThfXIOY0ZoYkWH_DXlPe98qmcXx3GdAQZdhodrkmvrI6K9lBIFpein8yJ7n1Pm0bxXmZv0NI_17mwIIKqRakJ4TqP7EyGny9QC0rGgCJJzhhPx4JwRv0gilFLTiZy4WEH_BT9xcaA3jxD4o5KgYYbn1BHQUpp9Qk2c3bo9QRVijnGm-acLjBDmqsQkTAQ-npBltZRH1nhfMqtuSro5IQFU1H7IeWaQ-0-PjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ede4f9d1e7.mp4?token=Ca3rmb1rLPBeXpefKmbKvV8iES0qgwl0KTREPifheidlrpGYeKKAqXPeqJpSyc3VJwHCrHp3A0UJghfPoSF_uFMGhXnX1Wycu62E8loZHLs8KQ93MniThfXIOY0ZoYkWH_DXlPe98qmcXx3GdAQZdhodrkmvrI6K9lBIFpein8yJ7n1Pm0bxXmZv0NI_17mwIIKqRakJ4TqP7EyGny9QC0rGgCJJzhhPx4JwRv0gilFLTiZy4WEH_BT9xcaA3jxD4o5KgYYbn1BHQUpp9Qk2c3bo9QRVijnGm-acLjBDmqsQkTAQ-npBltZRH1nhfMqtuSro5IQFU1H7IeWaQ-0-PjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راشاتودی: آمریکا سوخت‌رسان‌های خود را تا پایان سال ۲۰۲۷ در بن گوریون نگه می‌دارد
راشاتودی:
🔹
۶۰ فروند سوخت‌رسان نیروی هوایی آمریکا در فرودگاه بن گوریون و ۱۶ تا ۱۸ فروند دیگر در ایلات، رامون پارک شده‌اند. آمریکا قصد دارد آنها را تا پایان سال ۲۰۲۷ در آنجا نگه دارد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/655270" target="_blank">📅 16:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655269">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y204ofiDKIUixYivhRBnyXIpl3lphdallBZzsS6AU_20NrEL58jfWw9gjhQQRS247jVePbxI8kSHggdkyiMwq6UQG-y8--QbH_P_MWCTKkEOg3a5Iao4H9bC_TSSC-MSEDM0RA3thGIU3tXKbxPkrlkc0oSPT2GPzoaQ93stAcc2Bg5aeQ19H9hSCHWn8tvkoSa2JYTfdlwk3pYwDhpQ980WyAwHaQiOGRDWM6zfG1CfzZHDBDgqqmSvSbfrJFgJiJC6nRvOYDWCZrmB_llwEppQYmtFnARQSJe7WFwUkJtBrmrOsAdLShDl76WZWhFReOxCVbrlb3OBySQ0IVbeag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای باراک رواید: اسرائیل، آمریکا را مجبور به پذیرش حمله به بیروت کرد
آکسیوس، به نقل از یک مقام آمریکایی:
🔹
تلاش ناموفق روبیو برای آتش‌بس در لبنان می‌تواند واشنگتن را وادار کند تا به اسرائیل اجازه دهد به اهدافی در بیروت حمله کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/655269" target="_blank">📅 16:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655267">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
فوری/ ایران تبادل پیام با آمریکا را در اعتراض به جنایات صهیونیست‌ها متوقف می‌کند
🔹
با توجه به تداوم جنایات رژیم صهیونستی در لبنان و با عنایت به اینکه لبنان جزو پیش‌شرط‌های آتش‌بس بوده است و هم اینک این آتش‌بس در همه جبهه‌ها از جمله لبنان نقض شده است، تیم مذاکره‌کننده ایرانی «گفتگوها و تبادل متون از طریق میانجی» را متوقف می‌کند.
🔹
توقف فوری عملیات تجاوزکارانه و وحشیانه ارتش رژیم صهیونیستی در غزه و لبنان و ضرورت عقب‌نشینی کامل رژیم از مناطق اشغال شده در لبنان توسط مسئولان و مذاکره‌کنندگان ایرانی مورد تاکید قرار گرفته و تا زمانی که نظر ایران و مقاومت در این زمینه تامین نشود، گفتگویی در کار نخواهد بود.
🔹
همچنین، جبهه مقاومت و ایران عزم خود را برای انسداد کامل تنگه هرمز، و فعال کردن سایر جبهه‌ها از جمله تنگه باب‌المندب، به منظور تنبیه صهیونیستها و حامیانش در دستور کار قرار داده‌اند./ تسنیم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/655267" target="_blank">📅 16:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655266">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249ee45c8a.mp4?token=WWOSyOMNbZuRhVi48Hz7M6WGlwgAJT7VK2BlC1cB3nxBJsaQQ5DOfbtvC50g3iWc0r-MQ4tgd_H5cpSqmfPNkCgMCTU3W4hrc9pTkVNPXZPXSkSZKfBv6-fV0jqAdTZ2cE5VO8L558RgWBXyHbtFoJvJOr0jqjr77mUOGTm58gPpRMGENQP5SJ2OCHaFoI6aroAJ1ELvcue7z6nCJzkIWK-9LuIzEBdRFmwwEAlv7bIsSzawqeXjQqqFCP8ptAynO2sn_3PVXfrb_8F546E_m3w5ROW7kd6NLUyDdvZFihvTb6XKfw150HgcMpqaTBwc-YvhT-ZHjVZeGdw7yzHQgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249ee45c8a.mp4?token=WWOSyOMNbZuRhVi48Hz7M6WGlwgAJT7VK2BlC1cB3nxBJsaQQ5DOfbtvC50g3iWc0r-MQ4tgd_H5cpSqmfPNkCgMCTU3W4hrc9pTkVNPXZPXSkSZKfBv6-fV0jqAdTZ2cE5VO8L558RgWBXyHbtFoJvJOr0jqjr77mUOGTm58gPpRMGENQP5SJ2OCHaFoI6aroAJ1ELvcue7z6nCJzkIWK-9LuIzEBdRFmwwEAlv7bIsSzawqeXjQqqFCP8ptAynO2sn_3PVXfrb_8F546E_m3w5ROW7kd6NLUyDdvZFihvTb6XKfw150HgcMpqaTBwc-YvhT-ZHjVZeGdw7yzHQgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار در یک نفتکش با پرچم پاناما در آب‌های سرزمینی عراق
🔹
سی جی تی ان از انفجار در یک فروند نفتکش غول‌پیکر با پرچم پاناما در آب‌های سرزمینی عراق خبر داد.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/655266" target="_blank">📅 16:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655265">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
انفجار در یک نفتکش با پرچم پاناما در آب‌های سرزمینی عراق
🔹
سی جی تی ان از انفجار در یک فروند نفتکش غول‌پیکر با پرچم پاناما در آب‌های سرزمینی عراق خبر داد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/655265" target="_blank">📅 16:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655264">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
قیمت کله پاچه پرواز کرد/ هر پرس پاچه گوسفندی ۳۸۰ تا ۴۰۰ هزار تومان
🔹
بهای یک دست کله پاچه در بازار به دو میلیون و چهارصد هزار تومان رسیده است؛ در حالی که فقط پنج ماه پیش، هر دست کله پاچه یک میلیون و چهارصد هزار تومان قیمت داشت. هر پرس پاچه گوسفندی (شامل دو پاچه) بین ۳۸۰ تا ۴۰۰ هزار تومان، مغز گوسفندی ۳۰۰ هزار تومان، بناگوش ۳۴۰ هزار تومان و زبان ۴۴۰ هزار تومان قیمت دارد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/655264" target="_blank">📅 16:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655263">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4902b84e17.mp4?token=H4iTPUAGzPIkbzOmiCq8KcavmKa2CQ4g36aRxJJblW19qJ1OvaO8DthkcRqZVBvxJvdjTqOgkf9DoAqe9DfwcfEwNlbutFQ8A0rvqT3JrCVEeUYpyNB872YUZ9pM9TtTtUs-8i1m-bLpKSr1ciYGzgYi4BsRmNvym3hsTksbcBGxk0tHe74N_golc5z3Detu6UEl1fNmue8Meuhxk9QSnzQ60Ph8yHDL_P629R20HETwl-emQPEN-Iqm7bz1HRQsUuC-_xiqvCCNbM-kRwjZcv0rIDV6f1L0W9VUTsyHmzlWh4QmAVt52vo9wqhZ10QUzaDm004gAE5-RulYPN-dbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4902b84e17.mp4?token=H4iTPUAGzPIkbzOmiCq8KcavmKa2CQ4g36aRxJJblW19qJ1OvaO8DthkcRqZVBvxJvdjTqOgkf9DoAqe9DfwcfEwNlbutFQ8A0rvqT3JrCVEeUYpyNB872YUZ9pM9TtTtUs-8i1m-bLpKSr1ciYGzgYi4BsRmNvym3hsTksbcBGxk0tHe74N_golc5z3Detu6UEl1fNmue8Meuhxk9QSnzQ60Ph8yHDL_P629R20HETwl-emQPEN-Iqm7bz1HRQsUuC-_xiqvCCNbM-kRwjZcv0rIDV6f1L0W9VUTsyHmzlWh4QmAVt52vo9wqhZ10QUzaDm004gAE5-RulYPN-dbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی عجیب ماشین
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/655263" target="_blank">📅 16:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655262">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7FAHOwhNe8UD_qKy1zZWXyuJnj67o97eauyaei6395dLbCgJt4zc1fZ8p51A8jp3OoYCB0gl_vhpaBHjYP48Fi6oHIDFPBJVEIoLZD54ye-29QSP7gBGMKSOwIwFGUgrIHL65aIwKhAIxnYsD9iHQNhtIzV1wMBNjLTQOhd-bE-bdXxslIMvcPkNKm-qH9oVxfpKCXulH24CTZg8nVlwheSnh-oGFJPWsosK_GXEPkus-1LfjyIvm2f_h1dsM4ntui0xhZk2xmYQu91qfLXM_rUMU1PIaW5x2SvnVYMl3cJstinXztFOdAysfVUXSeyljFti1sEmsXtoUP2tcduOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو هیات‌مدیره و معاون فناوری اطلاعات تاکید کرد:
✅
«ردبانک» محصول نوآورانه بانک شهر برای ورود به نسل جدید خدمات مالی و هواداری
🔀
حسام حبیب‌اله، عضو هیات‌مدیره و معاون فناوری اطلاعات بانک شهر، از ورود رسمی «ردبانک» به بازار خدمات مالی دیجیتال خبر داد و این محصول را گامی نوآورانه در مسیر توسعه بانکداری هوشمند، یکپارچه و متناسب با سبک زندگی کاربران توصیف کرد.
🔀
به گزارش روابط عمومی بانک شهر، به گفته حبیب‌اله، صنعت بانکداری در سال‌های اخیر با تحولی جدی در انتظارات کاربران مواجه شده است؛ به‌گونه‌ای که دیگر نمی‌توان بانکداری دیجیتال را صرفاً به ارائه نسخه الکترونیکی خدمات سنتی محدود کرد. آنچه امروز اهمیت دارد، طراحی تجربه‌هایی است که در عین برخورداری از دقت، امنیت و کارآمدی، با نیازهای واقعی، الگوهای رفتاری و حتی علایق کاربران نیز هم‌راستا باشد. در همین چارچوب، بانک شهر با تکیه بر ظرفیت‌های فناورانه خود، «ردبانک» را به‌عنوان یک نئوبانک هواداری با رویکردی متفاوت طراحی و به بازار عرضه کرده است.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/655262" target="_blank">📅 16:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655261">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUHnRcbjYRdUt6gFfbpFk6PC58g9wfRv0cRZbj4UcgGgtmhc9bQiaoyocVAyUJxZzUq-vGTN9qBhfGLYNWYMS7AMmLJDxAIBfEDSDzC-51e564uW5DuMzir2oj0t7ZhDPsOeCA0WSFjUG89TOWdRF3xl6doPXxxg6b8meD5kC6V6Wd5MhivcEc19WGkbmGENKtHN-7-mV2Z88fAjWXusRhSkJ5CNh3OM646j3GLieOPL2O8TuAmrHAvD-5XF5WjJBSHJqbh3xRaZ4Y3lmuwjS4AIp5VrfStGpwofaH4lvIizOKfWAIHVz_QGLIKsFtfjjdg4n99L6pstPm0ZtadQrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای وزارت امور خارجه عمان: ما هدف قرار دادن کویت را محکوم می‌کنیم و حمایت خود را از اقداماتی که این کشور برای حفظ امنیت خود انجام می‌دهد، ابراز می‌کنیم
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/655261" target="_blank">📅 16:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655260">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
پزشکیان: نقض مکرر آتش‌بس در لبنان، تداوم آوارگی شهروندان لبنانی و حمایت‌های سیاسی و نظامی آمریکا از اقدامات رژیم صهیونیستی نگران‌کننده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/655260" target="_blank">📅 16:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655259">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تامین اجتماعی ۵۰ تا ۷۰ هزار میلیارد کسری بودجه دارد
فضل‌الله رنجبر، سخنگوی کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
اصلاح ۱۲ ماده از قانون تامین اجتماعی در دست پیگیری است که برخی از مواد مرتبط با تقویت بنیه مالی سازمان تامین اجتماعی در کمیسیون مصوب شده و برخی هم به کمیته‌های تخصصی ارجاع شده است.
🔹
۵۰۰ تا ۶۰۰ هزار نفر از بازنشتگان کشوری از مزایا یا بهره متناسب‌سازی حقوق ناامید شده‌اند و بی‌بهره مانده‌اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/655259" target="_blank">📅 16:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655258">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZVTgejgTIiJSwQu1T0MAsO0uF_rP_IBHU3zXutwJ3ExporBqi70_GKN5QePzfHgS-PBLleXlm8M8fWRfnQf6aiGVa6iy_lXXgKIAxEBYAcBiGkYzAUQ1qjdhkXrgujUoVmpRdRCS9U6jiVp-D-WY1tuvAmon8O3z9I5H7KMaeRCV8XEvL9lILTaMkM7Oo83XKA6PLlUFWbWLvuokeUhgC8ZV9AcDmKgCtzSu-8BM27TOFhykP12Z--P670pROcEbUQ-zyKT1W_MzcRRNgKTA1iCr-NV_pexhan6PWbawBfmH3FuOxdNkqaO2ec0jWNkrUP8g1iAuEUv-WjZEObWZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای سنتکام: ایران پایگاه آمریکا در کویت را هدف قرار داد
🔹
شب گذشته در ساعت ۱۱ شب به وقت شرق آمریکا (صبح به وقت تهران)، نیروهای ایالات متحده با موفقیت دو موشک بالستیک ایرانی را که نیروهای آمریکایی مستقر در کویت را هدف قرار داده بودند، رهگیری و منهدم کردند. همچنین هیچ‌یک از نیروهای آمریکایی در جریان این حمله آسیب ندیدند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/655258" target="_blank">📅 16:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655257">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03336c5a7f.mp4?token=Y2WK-DR_DAGJzuAQ0GFeOUv33nXxj20C-jVSVqVS85opIGEz_D9wYew_z_MZBBUVuy_4sZXU7rmgBIa2z_tkxQjXMWgu9IiB1YSD_2rcMCdPh_vraugMhRa0NsiOQF29aof4Rha6c9ghvxLJ4hVicL9obUzV-MTx0QkDINHOBMAZLqjO8xn4Zjghd69hcGARMSoG6v8NHfpM7mwbU99oTikLUlBCJ25rvaVWjFxhnhfy7cfkC5tC2NRaWjF4AkQoThburyOc0eWj-R7PrOPr7XpOXL3ajm4VIF-bYL7a0xxTNvz6KtX-c2IOkJD0Dr3f3YVJKfPYewcANwpDPKFd7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03336c5a7f.mp4?token=Y2WK-DR_DAGJzuAQ0GFeOUv33nXxj20C-jVSVqVS85opIGEz_D9wYew_z_MZBBUVuy_4sZXU7rmgBIa2z_tkxQjXMWgu9IiB1YSD_2rcMCdPh_vraugMhRa0NsiOQF29aof4Rha6c9ghvxLJ4hVicL9obUzV-MTx0QkDINHOBMAZLqjO8xn4Zjghd69hcGARMSoG6v8NHfpM7mwbU99oTikLUlBCJ25rvaVWjFxhnhfy7cfkC5tC2NRaWjF4AkQoThburyOc0eWj-R7PrOPr7XpOXL3ajm4VIF-bYL7a0xxTNvz6KtX-c2IOkJD0Dr3f3YVJKfPYewcANwpDPKFd7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور سرمایه‌گذاری حرفه‌ای انجام بدیم؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/655257" target="_blank">📅 16:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655256">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIB5jKnWkdThs-liWv-oN3n6-mlFK1-7k3gL3griX5BXrdVo8X1024ZVnYrk7krdNsN8oHtFANWDjbVCA3J5RsXICQY2B7iPGNXmlem6_vy5-LS2DH5VlY750iLzn3gdX6XWv7ta0ZH5S6JknzUed3gaG5C4VsVgcLFi1Y9Fab2TnKeKCxz3dXDc8R_mPGjjcZE86fnCx_2klbnDywGwbQsOJOrvJUHcUqi8fDCW2gsZWTQhVCXXCzE0YyZNW1Vu8dyosfSxSntZy5dWUkVflqdZflwv_Hs3ssW1gB-VAwiNiWy-rXt7ryOHXXn4CAvlATO8W7AD6R76rFBA6YcFTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
چرا رقبایتان همیشه جلوترند؟
چون از قدرت خبرفوری استفاده می‌کنند.
✅
تبلیغات در پربازدیدترین کانال‌های خبری
✅
پوشش همزمان سراسر کشور و استان‌ها
جای شما خالی نباشد.
همین حالا پیام دهید
👇
👇
👇
@newsadmin</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/655256" target="_blank">📅 16:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655255">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMp6s-kCaHJDoaWmj8GfKTcCuXIZ1R23KvQi3ZSzzBQwQKsWED6dlkPvshf-GyxqsxzhFXbEhH8vdiAFItIAsaQ8tErlT--bfEevqxd3OChJqfk98WdicZuOnEFJYxhSye2cqQfoXw1HRNMDlYV4u8M-echbefeBXLM4NP_SEyQsR0f0FlYnR_4OmfAJ_-VhRnaQ-63RyBgzkoluuN2001t9rWZmF1IP2M0ycZlJM-I6buQqTIWq2d3E2rUAMs3xIGVabdV5bMYEY33JJPCUBPWugvl67YOTJNfICtpB8tNWNWGfxSa3C_LXchtWZO4y4lBaTdVK0n5gLUNropnDGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جهش ۲۳ درصدی هزینه‌های درمان و ۲۰ درصدی لوازم خانگی
🔹
بررسی جزئیات تغییرات ماهانه قیمت‌ها در اردیبهشت نشان می‌دهد گروه «بهداشت و درمان» با ثبت تورم ماهانه ۲۳.۱ درصدی در صدر جدول افزایش قیمت‌ها قرار گرفته است.
🔹
پس از آن، گروه «اثاث، لوازم و خدمات مورد استفاده در خانه» با تورم ۲۰.۳ درصدی بیشترین رشد قیمت را در میان گروه‌های اصلی کالاها و خدمات مصرفی به خود اختصاص داده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/655255" target="_blank">📅 15:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655254">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/350197d19c.mp4?token=fEa5On1AEf2-G1BGhjb81rhHa7I19Loj233CsiwkWOH0Mpc7m1m2wjwVqB-hJo1nV_cNpX_SVLJbypj-9FmCeNDIOmeY-lVrMFQ5spZXCym9sn2OPs9nvfFzmzgCjTpwcPkYoy5TdVU1HLxoXIrrU789yz4pSzTyqvAKd0iqXb0acHnPojKQ28G-Gb5fUNTNFGfcgE1W2TJGOJ1sVgVqcWL1jkquFl7S_-en-kIFsUIoN5JQPQl_L2IPonUX_e7K6jgMu1iQHEegi6F85TGkyQiJmcMBZGa-A5qYKxxZ_FuVpVyQX7SuZxGmotzVWI-3F0NMmbfRRE6NHov_noGGkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/350197d19c.mp4?token=fEa5On1AEf2-G1BGhjb81rhHa7I19Loj233CsiwkWOH0Mpc7m1m2wjwVqB-hJo1nV_cNpX_SVLJbypj-9FmCeNDIOmeY-lVrMFQ5spZXCym9sn2OPs9nvfFzmzgCjTpwcPkYoy5TdVU1HLxoXIrrU789yz4pSzTyqvAKd0iqXb0acHnPojKQ28G-Gb5fUNTNFGfcgE1W2TJGOJ1sVgVqcWL1jkquFl7S_-en-kIFsUIoN5JQPQl_L2IPonUX_e7K6jgMu1iQHEegi6F85TGkyQiJmcMBZGa-A5qYKxxZ_FuVpVyQX7SuZxGmotzVWI-3F0NMmbfRRE6NHov_noGGkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عکس خیره‌کننده آرتمیس ۲؛ غروب زمین از پشت ماه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/655254" target="_blank">📅 15:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655252">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmo9h1ctN4HB46VN_k_KiHaLMqNEeGoDVrdOgatEie7qgqo2GJNv1gMmbjNQLFfEgaJ8fMq4yoBQBgxR5pMpdHXwgfSxEmj2-hfWHbNjwfkDB998VhiJ1PJ3Vj3Ws23yWmPw3M37KYioADsYX_BLv3Y1z6qv2_Qh4QYUwmps7TtAacsISwAG7v3YpOzA2Hh96vPf9TUtlWFfwI6VfPIbD6dwbJHohBWGD9kYFsPUaefBSaOYoOnL6bB9llDeFY230bNdvzmkAppya7Us3SKnENYmNtSEMhE_mrTTUZlF-4sA7F1Dqs9nHg4JMmrqsnvGxBYFI_XTIrHvtdBJkFyRBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فهرست تیم ملی ایران برای جام جهانی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/655252" target="_blank">📅 15:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655251">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYuRfsoy28KB733EhqzZvfPsUFSEr2QYnsssgOgBBmVGV-VA4jCcP9b9abtqR05nqrhcjqZLldPTAvmzVXgZvgWBwveWKEu3NrttMOQGUmVUYeK9Jaou7Dj5kB8p3VHuPOAi6RgXRebemTxkP-dlFdVZ3hPQASdTPr_2vhwfKkh553MthS4DZm_DSQjfms-I263RMJKZAyc_9hP35OMOHghqCW9d35aWZ85ATDUimL8A1JYGy1icpJglldavEPDhG4RU3UOArDnWaSmZuuEx490IxEJIF2R3sRt5TTa2YFBYC8K2uk5qJK006FnZ9Ktwu4LUrAL4W19Fcvb-5PT-Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میانگین قیمت بنزین در آمریکا ۴.۳ دلار شد
🔹
جدیدترین داده‌های انجمن خودروی آمریکا (AAA) نشان می‌دهد میانگین قیمت خرده‌فروشی بنزین در سراسر آمریکا به ۴.۳۳۶ دلار برای هر گالن رسیده است.
🔹
بر اساس نقشه منتشر شده، ایالت‌های غربی آمریکا از جمله کالیفرنیا، واشنگتن و اورگن همچنان بالاترین قیمت‌های بنزین را تجربه می‌کنند.
🔹
در حالی که بخش عمده‌ای از ایالت‌های جنوبی و مرکزی مانند تگزاس، اوکلاهما و لوئیزیانا در زمره ارزان‌ترین بازارهای سوخت قرار دارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/655251" target="_blank">📅 15:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655250">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYxVi-ThRkBqZqMVM15EdDAVVYVjTKa7whKehKqFFDKMt-vtnLy-wwcexuOzUa4JfA8b01Qm2OCCFFKpjQKc7XlWCDqycT7Eh0TNqHjtSxzLCRwTyE2hYz8XZMb-8AEaeIspN9Cpx8Udi9aJjsW4yY-srxStDHiYKLcEP3tmt9libcrYZuOz_v-28DpxH1OEi6NiAUWrIMwAjHjvViDoewVkxpFR1TeON6OBgWWQXiJP2wObzZxmKWbBrP3oplEcaR4SxiLdKjof8GocNLfVoqIz09kTATk0Q_CDbYVPl4_hgg_jrkX9woOhoSD7vUsqsZvBf-nfEsiJVTG6qWYoaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گنج پنهان در کشوی خانه‌ها؛ موبایل‌های قدیمی از معدن طلا ارزشمندترند | یک موبایل چقدر طلا دارد؟
🔹
گزارش تازه‌ای که با استناد به داده‌های سازمان ملل منتشر شده، نشان می‌دهد تلفن‌های همراه قدیمی و وسایل الکترونیکی بلااستفاده می‌توانند به منبعی بسیار ارزشمندتر از معادن سنتی طلا تبدیل شوند.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3218959</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/655250" target="_blank">📅 15:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655249">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42b90681b9.mp4?token=RLjjeGhrdJuXZ6wa1qmhYygtzzPoAam8okeEMlRV_FHX5jYCDDeDGB_yffbyoKuMO9cdDG6Z3_jK9RVob9afJiN9YZvYVMLb3wCxUTxXTg8JzbNN3es8fXY5Cg1oFAzrpcRWv3IZvAROcGMS7OFFX-QzFMN_R8TJBMToW5eR2Ng0D5VoOuvmpNday6LkM4pgxhntMI689HIs7zaRLnJkrnC_SmItTf1n1vqBn-ykM0F9dGEPh6qGDBqRwtkeP6J8PqjOF697UJa5koRpFztOKD8XLh-JDwReeiN9Yf_DWv0Sq0Oa5ll6WUkW6DXnL-bxoWCUsFOR3Z77SqQ-YM5wCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42b90681b9.mp4?token=RLjjeGhrdJuXZ6wa1qmhYygtzzPoAam8okeEMlRV_FHX5jYCDDeDGB_yffbyoKuMO9cdDG6Z3_jK9RVob9afJiN9YZvYVMLb3wCxUTxXTg8JzbNN3es8fXY5Cg1oFAzrpcRWv3IZvAROcGMS7OFFX-QzFMN_R8TJBMToW5eR2Ng0D5VoOuvmpNday6LkM4pgxhntMI689HIs7zaRLnJkrnC_SmItTf1n1vqBn-ykM0F9dGEPh6qGDBqRwtkeP6J8PqjOF697UJa5koRpFztOKD8XLh-JDwReeiN9Yf_DWv0Sq0Oa5ll6WUkW6DXnL-bxoWCUsFOR3Z77SqQ-YM5wCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین با موفقیت مجموعه‌ای از ماهواره‌های شبکه چیان‌فان را به مدار پرتاب کرد
🔹
این پرتاب، ششصد و چهل و هفتمین پرتاب برای موشک‌های سری لانگ مارچ بود. برنامه چیان‌فان شامل استقرار یک مجموعه ماهواره برای ارائه ارتباطات پهن‌باند و انتقال داده است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/655249" target="_blank">📅 15:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655248">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
اسرائیل‌الیوم: قانون انحلال کنست در جلسه عمومی تصویب شد
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/655248" target="_blank">📅 15:27 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
