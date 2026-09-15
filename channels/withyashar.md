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
<img src="https://cdn4.telesco.pe/file/Z6u8tFFKjPUP4SdhHMyHCQUbms-jhdMQeiF1An0pjehJvQJOGHWYZ4Mox9uxGLgIM3XFqfWvm0n22LG0bQVRTZSy9ZeUrccdWwjmL99on8HtvF3hbhgIxA1HMPuBkuwNg7EnCJEpRF1jskD4egaDKcfEt2sYb90FKMbAdQi9qIDU3IoBG92VDkvTj0UmFpVn9UlbKJiCdbAm6pq-DVRKFOP0JG_MuhVWBDCcJZbriuaBck3pd2vVXtvXLUdz4dcNWn-kUeyuG5ZBovMbIILuMzCM5fWbpo--TvAeqJzIr0YXdHW_Cr-k54CoIIyO6f9Q68oDt5L3YhSRMLKxKajmvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 451K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 23:14:42</div>
<hr>

<div class="tg-post" id="msg-23213">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c693031947.mp4?token=rxcJYgO1qLEX2lYogPZDkqSAlPd5mPgruFSShJMRmhsJa0t5abGb8Ju1FvOXOOFq8qoWsQzOa1SZUP5297fTuvC8VheKKnl4fmUkQrx9Zf2VKjdNMymTIPt-bItZfeIJ49gKjWRXlhqB6QJg7WCMeNI0SYmspkMfyANeqPFkjOA52cSZf6Y-avzZobQaX3GgBY8_6MwbqPkTodzmcfx1GNzJr4Lhnpn2Sh_2P489bg5sFJS8hVvDVRaOlpHtliZ_0NomK__FMJDtRgnVkOeD2xBOAWTBspFHY9WPYs1X3tiWWyRTSDGM_2I4vtTdgUkV5TVvjiVfhBM-LPfnQ4wFCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c693031947.mp4?token=rxcJYgO1qLEX2lYogPZDkqSAlPd5mPgruFSShJMRmhsJa0t5abGb8Ju1FvOXOOFq8qoWsQzOa1SZUP5297fTuvC8VheKKnl4fmUkQrx9Zf2VKjdNMymTIPt-bItZfeIJ49gKjWRXlhqB6QJg7WCMeNI0SYmspkMfyANeqPFkjOA52cSZf6Y-avzZobQaX3GgBY8_6MwbqPkTodzmcfx1GNzJr4Lhnpn2Sh_2P489bg5sFJS8hVvDVRaOlpHtliZ_0NomK__FMJDtRgnVkOeD2xBOAWTBspFHY9WPYs1X3tiWWyRTSDGM_2I4vtTdgUkV5TVvjiVfhBM-LPfnQ4wFCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام:
یک فروند بالگرد
MH-60 سی‌هاوک
از عرشه ناوشکن موشک‌انداز
یو‌اس‌اس رافائل پرالتا (DDG-115)
در حالی به پرواز درآمد که این ناو در چارچوب اجرای محاصره دریایی آمریکا علیه ایران در
دریای عرب
فعالیت می‌کند.
تا امروز
۱۵ سپتامبر
، نیروهای ما مسیر
۱۰۳ (
۲ کشتی فقط امروز )
کشتی تجاری
را برای اطمینان از رعایت مقررات محاصره ایران تغییر داده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/withyashar/23213" target="_blank">📅 23:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23212">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رسانه های عبری : ساعتی پیش، فرمانده یک گردان از کتائب القسام شاخه نظامی
حماس
در
رفح
شهری در
جنوب نوار غزه
و در مجاورت مرز
مصر
، ترور شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/withyashar/23212" target="_blank">📅 23:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23211">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/withyashar/23211" target="_blank">📅 22:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23210">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رأی امروز سنای آمریکا برای پیشبرد CLARITY Act شکست خورد.
این قانون قرار بود چارچوب مشخصی برای بازار رمزارز آمریکا ایجاد کند و حدود اختیارات SEC و CFTC را تعیین کند. شکست رأی به معنی رد دائمی قانون نیست و امکان دارد نسخه اصلاح‌شده آن دوباره در سنا مطرح شود، اما فعلاً مسیر تصویب متوقف شده و
ابهام مقرراتی در بازار کریپتو ادامه پیدا می‌کند
؛ موضوعی که می‌تواند در کوتاه‌مدت فشار منفی بر بازار ایجاد کند.
@WarRoom</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/withyashar/23210" target="_blank">📅 22:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23209">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e060275b19.mp4?token=D2hE6sayxLa67rMcIqtB4odReEcO-83QY2Jd8Io1rhQu36VX2CrPaId744981wBUa-UwYleL96TbbthJ6mOmo10RQWXxtW32xenBjPj_wq5m6ZctVqvhTzZSSKZZeUjGjcpIluzCoYOoAeW533ragUeAPR_zty2YDF7ePxA9WjYwksi2brfBYIlMlY4FWcTc6XMkaKpEaudv04OunzKWkypCn-AuuXzQr96RsgGGazr-hYtdZxPeNpE9Laa_B0Vv2f2oUiNBPXd8TzSIrEx0M0fio4vwzpRrMhcsYohOujDer8wmFqG_oWuY2leHNis31XhLIc1xqcCdPVDsD4Ehwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e060275b19.mp4?token=D2hE6sayxLa67rMcIqtB4odReEcO-83QY2Jd8Io1rhQu36VX2CrPaId744981wBUa-UwYleL96TbbthJ6mOmo10RQWXxtW32xenBjPj_wq5m6ZctVqvhTzZSSKZZeUjGjcpIluzCoYOoAeW533ragUeAPR_zty2YDF7ePxA9WjYwksi2brfBYIlMlY4FWcTc6XMkaKpEaudv04OunzKWkypCn-AuuXzQr96RsgGGazr-hYtdZxPeNpE9Laa_B0Vv2f2oUiNBPXd8TzSIrEx0M0fio4vwzpRrMhcsYohOujDer8wmFqG_oWuY2leHNis31XhLIc1xqcCdPVDsD4Ehwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : هیچ هدف‌گیری‌ای داخل شهر مکه مکرمه صورت نگرفته است. دو پایگاه هوایی در نزدیکی مکه قرار دارند: پایگاه هوایی ملک فهد در طائف و پایگاه هوایی ملک عبدالله در جده. هواپیماهای جنگی سعودی از این پایگاه‌ها برای انجام عملیات و بمباران در یمن پرواز…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/23209" target="_blank">📅 22:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23208">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فعالیت پدافند هوایی در استان آذربایجان غربی، واقع در شمال غرب ایران، در پی گزارش‌هایی مبنی بر فعالیت پهپادها در این منطقه.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/23208" target="_blank">📅 22:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23207">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/23207" target="_blank">📅 22:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23206">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ادعای یک فعال رسانه‌ای و سیاسی : امروز اطلاعاتی مبنی بر حمله قریب الوقوع آمد و ساعت ۱۱ظهر به تمام مراکز نظامی دستور تخلیه فوری داده شد. آمریکا بخاطر مسائل مختلف از جمله پیوستگی و وحدت تنگه های هرمز و باب المندب تحت فشار است و نتانیاهو نیز نقش تحریک کننده را بر عهده دارد. دشمن درپی ترور مسئولان عالی رتبه است
@WarRoom</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/23206" target="_blank">📅 21:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23205">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ائتلاف نیروهای سیاسی کردستان ایران برای ۲۵ شهریور فراخوان اعتصاب سراسری داد: این ائتلاف همزمان با چهارمین سالگرد کشته‌شدن مهسا ژینا امینی و آغاز جنبش «زن، زندگی، آزادی» از مردم در سراسر ایران خواست روز چهارشنبه ۲۵ شهریور با بستن مغازه‌ها و بازارها و خودداری…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/23205" target="_blank">📅 21:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23204">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5mMjKxZfC4iVThZSTR_WWU-anMKUpOLeXrqUuvjbh5dL3qXkNCravE37pztuohA14ABLVhYf02QHmghnKax9_2pWBGiUoRFlgczELK4c3V57A9xMDIDb2uarZ1GeHcYfFaLcdvNVBGoquUtfNrm3TvD9BGD4gsXKYWwqG1g-JhZuB1m4jpCTcMNRUeMours8Wv6QX4zx4TxGIAKwQJEV_u4qiXfyBdf1z7t0dIWKmADtIL4YMJZV26zC19RGVjkdoRVjAi7OlNVvzmQQ5CgZJgAEym9V2CyeDLTqod_ZyK3Wfpr36RhMnm3hhqjCPBPNA39MBuJionZTN_fABtGiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت وارد کانال ۱۰۹$
📈
شد
@WarRoom</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/23204" target="_blank">📅 21:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23203">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خبرگزاری کان اسرائیل: موساد و ارتش اسرائیل از طریق سنتکام، اطلاعات بسیار گسترده حساسی از حوثی های یمن را در اختیار عربستان سعودی قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/23203" target="_blank">📅 21:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23202">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zh4PlPRL97jxbCRxqzKpyjK9u5lmVs1uHSTyPsTAso1U8mJWxJsh5K_6oAR0MJmfD2Tr_GZtRAoZEiXyImdoQcyfViskHeAaZntzF7babLjYZOEGF8C-XYmumRWykBtXTzntcoqTuh3ht0Es1RyY3Beh5mWep5t9_wlRLcCMr1PG_lUo8KSewVmL208x6WUs9ZwuqDkqaXS956vXNJrjTNMC3wFgFrB9VSMIouhlq7LPOYsSyPUK7xfi2GE0VrGf6e2C_Dve55wkQeuGN4QcV8RvU5EuAqotwvmK8TifpkzGGYwCT1FLaKzYZjE7NrNJRN5eK_yQC2l90FwUd-7UGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان:
در قراردادی که آن را «مشکوک‌ترین قرارداد تاریخ نفت ایران» دانسته،
۸۰ میلیون بشکه نفت
پس از توافق اسلام‌آباد به چهار تراستی
علی بایندریان، روح‌الله رضوی، محمدهادی مومنین و حسین شمخانی
واگذار شده است. کیهان می‌گوید این چهار تراستی
سابقه بدهی جدی به وزارت نفت
داشته‌اند و طبق مصوبات شعام و وزارت نفت، نباید پیش از تسویه بدهی سهمیه نفت می‌گرفتند. ابهام دیگر،
فروش اعتباری و حساب‌باز نفت بدون مشخص بودن تضامین و مسئول ریسک وصول مطالبات
است. همچنین حدود
۸ درصد تخفیف
برای این معامله در نظر گرفته شده که به گفته کیهان، با توجه به حجم نفت، ارزش آن به
چند میلیارد دلار
می‌رسد و یک رکورد تاریخی محسوب می‌شود. کیهان همچنین از
درخواست نهادهای نظارتی برای ارائه مستندات درباره نحوه واگذاری، شرایط فروش و تضامین
خبر داده و خواستار ورود فوری
بازرسی دفتر رهبر انقلاب و سازمان بازرسی کل کشور
به این قرارداد شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/23202" target="_blank">📅 21:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23201">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سخنگوی گروه تروریستی حوثی یمن، یحیی سریع:
هواپیماهای جنگی سعودی در ۲۴ ساعت گذشته، ۵۲ حمله هوایی با استفاده از هواپیماهای "F15" و "تایفون" که از پایگاه‌های خمیس مشیت و طائف پرواز کرده بودند، انجام دادند. این حملات وحشیانه، بدون پاسخ نخواهند ماند.
@WarRoom</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/23201" target="_blank">📅 21:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23200">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خبرگزاری واپو:
دولت ترامپ در حال آماده‌سازی یک فروش تسلیحاتی به ارزش ۲.۸ میلیارد دلار به اسرائیل است که شامل ۴۰,۰۰۰ بمب ۲,۰۰۰ پوندی (۲۰,۰۰۰ بمب MK-84 و ۲۰,۰۰۰ بمب BLU-117) به علاوه ۲۰,۰۰۰ سر جنگی نفوذگر I-2000 خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/23200" target="_blank">📅 21:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23199">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سروان تیم هاوکینز، سخنگوی سنتکام، امروز سه‌شنبه ۲۴ شهریور به سوران خاطری از بخش فارسی صدای آمریکا گفت: «می‌توانم تأیید کنم که قایق‌های کوچک ایرانی اخیراً تلاش کردند یک شناور بی‌سرنشین سطحی آمریکا را تصرف کنند، اما پس از واکنش قاطع نیروهای سنتکام در این کار ناکام ماندند.»
سخنگوی سنتکام تصریح کرد که این شِهپاد «همچنان تحت کنترل عملیاتی ایالات متحده است.» «شِهپاد» سرنامی است که از حروف نخست عبارت «شناور هدایت‌پذیر از دور» تشکیل شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/23199" target="_blank">📅 20:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23198">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">باراک راوید، آکسیوس:
یک مقام آمریکایی گفت ارتش آمریکا و کشورهای حوزه خلیج فارس، عبور روزانه و در طول ساعات روشن روزِ نفتکش‌ها از تنگه هرمز را آغاز کرده‌اند و دیگر مانند ماه‌های اخیر، عبور نفتکش‌ها فقط در ساعات شب انجام نمی‌شود.
همچنین
ارتش آمریکا روز دوشنبه
دیروز
دو قایق کوچک ایرانی را منهدم کرد
؛ پس از آنکه سپاه پاسداران انقلاب اسلامی تلاش کرد یک شهپاد نیروی دریایی آمریکا را که در حال گشت‌زنی در تنگه هرمز بود، تصرف کند
@WarRoom</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/23198" target="_blank">📅 20:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23196">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b49ca62412.mp4?token=C03kF2lJ0tg3-iLaPm37DNufWtsOOcmYo6vdwJVmplo2uegtSvt5RJq_ogY-Gt1nD7q-VCPMKwP1eO9OrWLKsrLLJ5EogS2FjpMlFPqbcs7J6jC2NpQPoiHuVG2WErL1K4705Qm_soCFBQVzZzE1yXYJYdB5SmVGrCXxDfmMhfDyvoj9Ou-YdpVg_9riCDOi15vOdhDAmJgRydZAju0Fl5URc5_ER8q2M9C9NNZDCRWWBX2x9_M5DbYOW9kcbQ2IUektthptw_lEzY8KopiBQvStyVtroItyQwWrC4npARoB4b3q9JDPzhO_7imcshU8LkSCHQVw8WjzdTJPhef-giPgt4bDBpqQrFMHjLxvoPE15K5dwesLP9l-SuexNt4mVJk66kPX1leWInQWPHvhjXtlqaiadKgJjkgojsM0SQJeuTS2c8Qd8m6gIVZsxoO8enQN_GHxwZkakZ1qhcP_jnZNEE9WZ-ZS8eIfTivtsUL26Do-mRGKECo3Sz4jdmUOPMZ0WDSfRuIMa7ymCYIt1vjiamO5yWAw1NlO0pTsvbt09O2y0RxZk-4hYHju8lJvu-ep5DD_fjYWIqchj978Okjdi16C5jTF7uQnsxygG14ev-8Jx25E0kId8Fk_zTyjTszXn_Y-vU8AJ9oucpcqpk3q7uf0Dv3iFQI7e3XRCVk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b49ca62412.mp4?token=C03kF2lJ0tg3-iLaPm37DNufWtsOOcmYo6vdwJVmplo2uegtSvt5RJq_ogY-Gt1nD7q-VCPMKwP1eO9OrWLKsrLLJ5EogS2FjpMlFPqbcs7J6jC2NpQPoiHuVG2WErL1K4705Qm_soCFBQVzZzE1yXYJYdB5SmVGrCXxDfmMhfDyvoj9Ou-YdpVg_9riCDOi15vOdhDAmJgRydZAju0Fl5URc5_ER8q2M9C9NNZDCRWWBX2x9_M5DbYOW9kcbQ2IUektthptw_lEzY8KopiBQvStyVtroItyQwWrC4npARoB4b3q9JDPzhO_7imcshU8LkSCHQVw8WjzdTJPhef-giPgt4bDBpqQrFMHjLxvoPE15K5dwesLP9l-SuexNt4mVJk66kPX1leWInQWPHvhjXtlqaiadKgJjkgojsM0SQJeuTS2c8Qd8m6gIVZsxoO8enQN_GHxwZkakZ1qhcP_jnZNEE9WZ-ZS8eIfTivtsUL26Do-mRGKECo3Sz4jdmUOPMZ0WDSfRuIMa7ymCYIt1vjiamO5yWAw1NlO0pTsvbt09O2y0RxZk-4hYHju8lJvu-ep5DD_fjYWIqchj978Okjdi16C5jTF7uQnsxygG14ev-8Jx25E0kId8Fk_zTyjTszXn_Y-vU8AJ9oucpcqpk3q7uf0Dv3iFQI7e3XRCVk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر از نفتکش الگایا که ادعا شده در اثر برخورد با مین‌های سپاه منفجر شده
@WarRoom</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/23196" target="_blank">📅 20:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23195">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ادعای رسانه های عربی حامی رژیم ج.ا : رهبران ارتش‌های ایالات متحده، اسرائیل و کشورهای عربی، جلسه‌ای مخفی درباره ایران برگزار کردند. @WarRoom</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/23195" target="_blank">📅 20:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23194">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aP4vG0EnF67pE7xeRfyyozpv-Ln49-bPLiXX52aI0Eh05zloFdmNQJZsD5ZH2Szf9esT-uZgSzaS4vepBceKAsx1Ese8ah4RJGXqNcQBYeqeO9bSHezxiHvugg4G9FgX1U14vxi29vqLBXNxMU1g6kcSWjy_27Gn6_3Mil-ECGcpQDWP22nWFHJcDd8dG-NcJ4L6KdTxrndEuwYKLHElMw6hlQOJWvYbH_q-Fljl7CpsbfNFFvqdt5Iuh1dOzbYLFZpAWxQ6tB695E8s24ID70LKqGuNdC5B3l-GOaM0I_XTRAxlPCe-FrfGoGlVPlzYP3aj-1Toq19TtzQ8PYSiRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت دوباره به کانال ۱۰۸$
📈
وارد شد
@WarRoom</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/23194" target="_blank">📅 20:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23193">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وزارت دادگستری آمریکا: دولت آمریکا برای مصادره حدود ۶۱ میلیون دلار رمزارز مرتبط با درآمد حاصل از فروش غیرقانونی نفت ایران اقدام قضایی کرده است. طبق شکایت دادستانی ناحیه جنوبی نیویورک و اف‌بی‌آی، شبکه‌ای از شرکت‌ها و آدرس‌های رمزارزی با عنوان Entity A بیش از…</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/23193" target="_blank">📅 20:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23192">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ادعای رسانه های عربی حامی رژیم ج.ا :
رهبران ارتش‌های ایالات متحده، اسرائیل و کشورهای عربی، جلسه‌ای مخفی درباره ایران برگزار کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/23192" target="_blank">📅 19:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23191">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f106a591ad.mp4?token=MWUREE4wM0poQ9CdVvOFuW_fU7173GRgCB6NfWBx_8mRRF4lN7GIJ2AdzbGLVU7_wr3AmKmPb751pzPLWivBc_wHlDi-IcdrQi1d0pGPWchP361D7RSXabI0ktNpGkOOfT_0h4JbSd1NlNTRkwEZgUVdsy8DYuq3daIbNyW_79DFCUVbgjn1_Tbh7_HKLSJHMHac1qLrRWBPugOv7gCQil3CnBcYVh-W_1z5HaNmS-IMWhVa60nT2eqLizNErinoIBswbNQRBxKrufXJJmgENr91FsOx5D0dAK9zc5t3UTqcSxkfR7w4HyGqUkxvOoBssGqJC3gM7GtvpwqoI9EYcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f106a591ad.mp4?token=MWUREE4wM0poQ9CdVvOFuW_fU7173GRgCB6NfWBx_8mRRF4lN7GIJ2AdzbGLVU7_wr3AmKmPb751pzPLWivBc_wHlDi-IcdrQi1d0pGPWchP361D7RSXabI0ktNpGkOOfT_0h4JbSd1NlNTRkwEZgUVdsy8DYuq3daIbNyW_79DFCUVbgjn1_Tbh7_HKLSJHMHac1qLrRWBPugOv7gCQil3CnBcYVh-W_1z5HaNmS-IMWhVa60nT2eqLizNErinoIBswbNQRBxKrufXJJmgENr91FsOx5D0dAK9zc5t3UTqcSxkfR7w4HyGqUkxvOoBssGqJC3gM7GtvpwqoI9EYcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشات حاکی از این دارد مخفیگاه‌های مظنون به داعش در صحرای سوریه امروز بعد از ظهر توسط هواپیماهای A-10 نیروی هوایی ایالات متحده مورد حمله قرار گرفتند. این اولین حملات هوایی شناخته شده پس از ماه‌ها است.
@WarRoom</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/23191" target="_blank">📅 19:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23190">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یک فروند هواپیمای بوئینگ ۷۳۷ متعلق به شرکت هواپیمایی سپهران که از مشهد عازم کرمانشاه بود، پس از برخاستن اعلام وضعیت اضطراری کرد و به مشهد بازگشت و به سلامت فرود آمد. علت گزارش‌شده برای این حادثه، مشکل در یکی از چرخ‌ها هنگام برخاستن و احتمال آسیب‌دیدگی موتور…</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/23190" target="_blank">📅 19:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23189">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b83c064733.mp4?token=C9uzWfOQDE9XhWpcEJZmuSNC9WVKl-zwg0iquUIa0Y8G4Xbcm-vwH1I0K6sSCp1rkfKenII-O5uOj7lCG3XxE_een32pWuv7cRaoE0BeT1Yk24AK3ubZ8g2GoWt6iRUjnKW8FQccfttNptktwN0R8D8j4x0lMkp_f0SJVwg44moJBBOPElfTGl_0ruJPrIgCfVhEgZl2ybrmD7bFStbgDK3uoZOjv2sKN1-n7hI4MWds7OvaMJFeCLbTyPubOIXx2_hbEzQoSytfKT_VpfMUHzjqFqv9K-HQVjn__o5CIO-tQWZfkMb0kJsTRrLx4dd0hyBdCMx0FmvHyn6EPoxEkFHrV2OcsL2jp0U1OQjeB9bQfZgA_qaf_G4ED0PtYBgQhbgImv8meLV22t9vqnYU0kQS5sQXSB4o0mpbA0py2jcKxpdoM_LZ0_y7yQOK6vwgd96xbp3kTHZoWdaK_ziPSs8h3d5qAKJoi3PygqG74uPVag_i6Bub3K63XJ-Zs0vIvNXamQqMt_yt0q2BR5lEBTb3s3xofwG1oRE9-Qq14djTUKSHpdRogtlzHxBcptLaUFE_kdW-gESTZYqvu4G3aVpN4fkDHTfuEd26Gk7TwBWpVkzbQrn3pxC1DrpizbAIdha9y-RnkMvTaCWYCorFd4o0bNBULi4uZmPETU_IU_4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b83c064733.mp4?token=C9uzWfOQDE9XhWpcEJZmuSNC9WVKl-zwg0iquUIa0Y8G4Xbcm-vwH1I0K6sSCp1rkfKenII-O5uOj7lCG3XxE_een32pWuv7cRaoE0BeT1Yk24AK3ubZ8g2GoWt6iRUjnKW8FQccfttNptktwN0R8D8j4x0lMkp_f0SJVwg44moJBBOPElfTGl_0ruJPrIgCfVhEgZl2ybrmD7bFStbgDK3uoZOjv2sKN1-n7hI4MWds7OvaMJFeCLbTyPubOIXx2_hbEzQoSytfKT_VpfMUHzjqFqv9K-HQVjn__o5CIO-tQWZfkMb0kJsTRrLx4dd0hyBdCMx0FmvHyn6EPoxEkFHrV2OcsL2jp0U1OQjeB9bQfZgA_qaf_G4ED0PtYBgQhbgImv8meLV22t9vqnYU0kQS5sQXSB4o0mpbA0py2jcKxpdoM_LZ0_y7yQOK6vwgd96xbp3kTHZoWdaK_ziPSs8h3d5qAKJoi3PygqG74uPVag_i6Bub3K63XJ-Zs0vIvNXamQqMt_yt0q2BR5lEBTb3s3xofwG1oRE9-Qq14djTUKSHpdRogtlzHxBcptLaUFE_kdW-gESTZYqvu4G3aVpN4fkDHTfuEd26Gk7TwBWpVkzbQrn3pxC1DrpizbAIdha9y-RnkMvTaCWYCorFd4o0bNBULi4uZmPETU_IU_4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : مردم شریف ایران، شرایط ایمنی حمل‌ونقل کشور به‌شدت نگران‌کننده شده است. در بخش هوانوردی، گزارش‌هایی از اختلال سامانه‌های ناوبری گزارش شده همچنین بعد از‌جنگ اکثر سامانه های راداری نابود شده اند و از ترس حملات خاموش کردن عمدی ترانسپوندر برخی…</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/23189" target="_blank">📅 19:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23188">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbcfdfe8fd.mp4?token=MwJosyodoNzJQZ4QNy0E2bLF2J-jMcUpeEqw5foyEfvBFiO5PdKBQqwTJHUN41S_qtv3-AoK9A4Da35SlNH_RNB3UiJgCGFvUyIUta-kIQYBr063_IEkm0vP3Hi74NnD8sEW8guLcE4k_gYcK9CIvVc8fEVD3lxIXbTpuDDFUGgTio0TqFgVwD9WZbEU_cFl2UC6hLwJOjFb4vIlqLb-tsnhIzCaJMGhhxnMPqf1cwvGvywDwCBLnIM760GBwzNe26_uRxyyH05Lla1g3RoeEWGSFzNI4vyzhia2WcRvkbk3H7O7jKV2aJWsFgDXzI6Biul55-AgP7xilS9CfRWYOlSRnHQLUeIjmo8GTpPrPYpxzoYkWvT9k297Lsad_PXD0haK86vA_onGLvFea8no8gq0cFmExCavbjYFc_7PAdVV5PeVqRpPY2lBgnINML7IRLjxI01ZPfAlP98_PX3P-eTaki_79eKUk_30Q6l5Nfh5Y8ktZAqJo1MoIq_dL9QqfLGFmxfetPVL3o3lzrN1sg2MtOk-bdzWTf73IdO3-LpdTukqKXgPgmem7VixPLnbLDXUMpYkuxpp7p3Ix9TLzTcmBu65OMIzHYMg4kgklJhq3FcEJoAw9n7UyV2KHy6j_Cnvv7XL_x43UZOLjbefGxu3J56Zg7-wRARKSugkl_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbcfdfe8fd.mp4?token=MwJosyodoNzJQZ4QNy0E2bLF2J-jMcUpeEqw5foyEfvBFiO5PdKBQqwTJHUN41S_qtv3-AoK9A4Da35SlNH_RNB3UiJgCGFvUyIUta-kIQYBr063_IEkm0vP3Hi74NnD8sEW8guLcE4k_gYcK9CIvVc8fEVD3lxIXbTpuDDFUGgTio0TqFgVwD9WZbEU_cFl2UC6hLwJOjFb4vIlqLb-tsnhIzCaJMGhhxnMPqf1cwvGvywDwCBLnIM760GBwzNe26_uRxyyH05Lla1g3RoeEWGSFzNI4vyzhia2WcRvkbk3H7O7jKV2aJWsFgDXzI6Biul55-AgP7xilS9CfRWYOlSRnHQLUeIjmo8GTpPrPYpxzoYkWvT9k297Lsad_PXD0haK86vA_onGLvFea8no8gq0cFmExCavbjYFc_7PAdVV5PeVqRpPY2lBgnINML7IRLjxI01ZPfAlP98_PX3P-eTaki_79eKUk_30Q6l5Nfh5Y8ktZAqJo1MoIq_dL9QqfLGFmxfetPVL3o3lzrN1sg2MtOk-bdzWTf73IdO3-LpdTukqKXgPgmem7VixPLnbLDXUMpYkuxpp7p3Ix9TLzTcmBu65OMIzHYMg4kgklJhq3FcEJoAw9n7UyV2KHy6j_Cnvv7XL_x43UZOLjbefGxu3J56Zg7-wRARKSugkl_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
«من فقط به اظهارات رئیس‌جمهور ایران، رئیس مجلس و رئیس بانک مرکزی استناد می‌کنم که گفته‌اند اقتصاد کشور در وضعیت بسیار وخیمی قرار دارد. او به همکاران و همفکران تندروی خود در سپاه پاسداران و همچنین مردم ایران هشدار داده بود. ما شاهد سقوط ارزش پول ملی و تورم سرسام‌آور بوده‌ایم و به‌طرز باورنکردنی، در کشوری که سومین منابع بزرگ انرژی جهان را در اختیار دارد، حالا مردم با صف‌های سه تا چهار ساعته برای دریافت بنزین مواجه‌اند، زیرا ایران مجبور است سوخت خود را وارد کند. بنابراین، فروپاشی اقتصادی به دلیل محاصره امکان‌پذیر است. ترکیب محاصره، به‌علاوه ماه‌هایی که صرف شناسایی و ترسیم شبکه‌های موجود در سامانه پرداخت کرده‌ایم، به ما اجازه داده تا فشار بر آنها را افزایش دهیم و من معتقدم این فوران‌های خشونت‌آمیزی که از سوی آنها شاهد هستیم، نتیجه واکنش یک حیوان زخمی و به‌دام‌افتاده است.»
@WarRoom</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/23188" target="_blank">📅 19:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23187">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">امشب میخوام بیام تویتر اسپیس (x)
و با همه شما لایو حرف بزنم بیارمتون بالا شما سوال کنید و … اگه نمیدونید چیه دقیقا مثل کلاب هاوس است ولی در پلتفروم اکس
x.com/yasharrapfa
ساعت دقیق رو کمی دیگه اعلام میکنم ، شما کاراتونو بکنید آماده بشید</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/23187" target="_blank">📅 19:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23186">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آژانس بین‌المللی انرژی اتمی:
ایران در جریان هفتادمین کنفرانس عمومی آژانس به عضویت کمیته عمومی (General Committee) این کنفرانس انتخاب شد.
این انتخاب در جریان نشست سالانه آژانس در وین انجام شده است.
برخی گزارش‌های ایرانی می‌گویند این انتخاب در یک رأی‌گیری مخفی انجام شده، اما جزئیات رسمی رأی‌گیری هنوز منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/23186" target="_blank">📅 19:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23185">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اسکات بسنت امروز اعلام کرد آمریکا فشار مالی علیه ایران را تشدید می‌کند و از افراد در سراسر جهان خواست اطلاعات مربوط به شرکت‌ها، بانک‌ها و اشخاصی را که به ایران برای دور زدن تحریم‌ها یا انتقال پول کمک می‌کنند، به خزانه‌داری آمریکا گزارش کنند.
بسنت گفت افرادی که اطلاعات قابل اقدام ارائه دهند، صرف‌نظر از محل زندگی یا محل کارشان، ممکن است واجد شرایط دریافت پاداش مالی باشند. این اقدام بخشی از
Operation Economic Outcast
است که هدف آن قطع «راه‌های مالی» باقی‌مانده برای حکومت ایران و شبکه‌های وابسته به آن عنوان شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/23185" target="_blank">📅 18:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23184">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyxwd4Jkm0c5qX0DioPAkMhnY0Y1m1DYVFc7D1LqDaxnCqZyxK9wxOVgGvPrTfZ0MgAPXKVGjVk672BtXFRqbIEtUAcxD2VeiQ8iRjxaoZX2OpyYRBjX8KP0GOzMA_0mzw3JsLBcFbaEbT2xc4efrvUY_xCv-Jiv-jTkwbQzvNLRKvVbCXmxwXwO-MEfvmaI8g4iaemBQtgPObUr7b4gAmMLqUPVK0NgMw3ZqSZHx37jgE4qJo7oRkZCAo6Mg_prNOV4QWUMj1cr-Q80cU8ama1sym4XbbhwAOZslFmCUBa3w2WIZThJbX-TkGJts-ffJZQxZ3vV4Ag9iKmFe-lZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون آتش سوزی محدوده پیروزی/محلاتی تهران
@WarRoom</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/23184" target="_blank">📅 18:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23183">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سنتکام : آمریکا و اردن رزمایش دوسالانه «Eager Lion 2026» را امروز ۱۵ سپتامبر در فورت کارسون، کلرادو آغاز کردند. بیش از ۲۰۰ نیروی آمریکایی و اردنی در این رزمایش دو هفته‌ای حضور دارند و تمرین‌ها بر
پدافند هوایی، امنیت دریایی، مقابله با تروریسم، جنگ سایبری و واکنش به بحران‌ها
متمرکز است. این نخستین‌بار است که آمریکا میزبان رزمایش Eager Lion می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/23183" target="_blank">📅 18:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23180">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fff5fc67b.mp4?token=k_1DZ3SH_mQAG3Q18zi-LAR8dZVLjKhWfq3S4eWkKFQbmJSRQc8HlP5-9TS_JLnT_5ld-vwWNyKRAJt_-3AlLP2sMHULzvbe-bWCIbWmeQOtnGi_8s7ZYgYAgnb8P5zpCQ82gveYnUHczw3nexFS2rZ5oICDwemC0Kzf7MxVBnMOICQ9H9EzzjG5E4QMyZ2zxwChMkJiJcwT4SmYabLc3QseV85CXgUxlGuh7F5oOUXmJQC6KRMgew7noFVuK1aFpr0_y5ZQvkENGnBqPjGzwJpi_PT6Hrmlgubpb5W7RAOtkEq58iuiJCgz-a4pDFUfgWXbD1VBVEiR-T5AHSi9dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fff5fc67b.mp4?token=k_1DZ3SH_mQAG3Q18zi-LAR8dZVLjKhWfq3S4eWkKFQbmJSRQc8HlP5-9TS_JLnT_5ld-vwWNyKRAJt_-3AlLP2sMHULzvbe-bWCIbWmeQOtnGi_8s7ZYgYAgnb8P5zpCQ82gveYnUHczw3nexFS2rZ5oICDwemC0Kzf7MxVBnMOICQ9H9EzzjG5E4QMyZ2zxwChMkJiJcwT4SmYabLc3QseV85CXgUxlGuh7F5oOUXmJQC6KRMgew7noFVuK1aFpr0_y5ZQvkENGnBqPjGzwJpi_PT6Hrmlgubpb5W7RAOtkEq58iuiJCgz-a4pDFUfgWXbD1VBVEiR-T5AHSi9dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏لحظۀ ترور یوسف گرگیج امام جماعت حامی حکومت در زاهدان
@WarRoom</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/23180" target="_blank">📅 18:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23179">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وزارت دادگستری آمریکا: دولت آمریکا برای مصادره حدود
۶۱ میلیون دلار رمزارز
مرتبط با درآمد حاصل از فروش غیرقانونی نفت ایران اقدام قضایی کرده است. طبق شکایت دادستانی ناحیه جنوبی نیویورک و اف‌بی‌آی، شبکه‌ای از شرکت‌ها و آدرس‌های رمزارزی با عنوان
Entity A
بیش از
۱.۵ میلیارد دلار
از درآمدهای فروش غیرقانونی نفت ایران را دریافت و منتقل کرده‌اند. دو شرکت هنگ‌کنگی
Blessed Trust
و
Hexa Whale
نیز از حساب‌های خود در صرافی
بایننس
برای انتقال بخشی از این پول‌ها استفاده کرده‌اند؛ وجوهی که به گفته آمریکا در نهایت به دولت ایران و شبکه‌های مرتبط با
سپاه پاسداران
منتقل شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23179" target="_blank">📅 16:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23177">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خبرگزاری آکسیوس به نقل از مقامات آمریکایی : نیروهای آمریکایی در واکنش به تلاش سپاه برای توقیف شناور بدون‌سرنشین آن دو قایق ایرانی را در نزدیکی تنگه هرمز هدف قرار دادند. این حادثه نشان می‌دهد رویارویی مستقیم نیروهای دریایی آمریکا و سپاه در هرمز همچنان ادامه…</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/23177" target="_blank">📅 16:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23176">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اتاق جنگ با یاشار : در درگیری امروز گزارش شده از دیدبان اتاق جنگ ,  ۲ قایق تندرو سپاه که از اهالی کرگان(میناب) بودند(اکثر این اهالی با حکومت هستند و پاسدارند) عصر امروز هدف حمله آمریکا در تنگه قرار گرفتن ۱ جسد پیدا شد و ۳ نفر  دیگه فعلا تا این لحظه نگارش این…</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23176" target="_blank">📅 16:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23175">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59afb2fe58.mp4?token=dDzMjvTfuiSVDP3iMONR7t-DRVM9LbeT7hZ01AC9eWh5MDe94Htab8I8m7ccjjTKVr9Y-L6iuQOBOq-2bVpuhhm7sCX2BFNjBtW0JbKwiqPNT2Hkw1jMe9l99lx-OUpBlPSvagAzr1rtEq4t6YaPW3S6sT4oqBaULnYtquh0_Ii1KnpcwpikBGiFdjnf-a3HrRsj3V_sC_dn-9tdS4f_R56eH_hKameQxwa0am4HoC-YB81znESTixk5vm6-UXaG5YcwLPtu6QsmWhxjG6gpdgstrB8K5wrZxGNPWG2PyowgJo2U9ITcSR7QEXzdjrQSro4kwj9lo3C9FiqLFwBnlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59afb2fe58.mp4?token=dDzMjvTfuiSVDP3iMONR7t-DRVM9LbeT7hZ01AC9eWh5MDe94Htab8I8m7ccjjTKVr9Y-L6iuQOBOq-2bVpuhhm7sCX2BFNjBtW0JbKwiqPNT2Hkw1jMe9l99lx-OUpBlPSvagAzr1rtEq4t6YaPW3S6sT4oqBaULnYtquh0_Ii1KnpcwpikBGiFdjnf-a3HrRsj3V_sC_dn-9tdS4f_R56eH_hKameQxwa0am4HoC-YB81znESTixk5vm6-UXaG5YcwLPtu6QsmWhxjG6gpdgstrB8K5wrZxGNPWG2PyowgJo2U9ITcSR7QEXzdjrQSro4kwj9lo3C9FiqLFwBnlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاملترین نسخه و با بهترین ترجمه و خواناترین زیرنویس فارسی از گزارش ویژه «۶۰ دقیقه» شبکه CBS درباره عملیات نجات افسر تسلیحات یک فروند F-15E آمریکایی که پس از سقوط جنگنده در ایران، حدود ۵۰ ساعت در خاک ایران مخفی ماند و در نهایت طی یک عملیات ویژه نجات پیدا کرد.…</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23175" target="_blank">📅 15:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23174">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وزارت جنگ آمریکا برای نخستین بار به‌طور رسمی در گزارشی به کنگره تأیید کرد که یک جنگنده رادارگریز اف-۳۵ ارتش آمریکا در جریان مأموریت بر فراز ایران، هدف آتش قرار گرفته و آسیب دیده است؛ موضوعی که پیش از این تنها به‌عنوان فرود اضطراری یک فروند اف-۳۵ اعلام شده بود
@WarRoom</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/23174" target="_blank">📅 15:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23173">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شایعه شده است که فردی در هتل اسپیناس، واقع در بلوار کشاورز در مرکز تهران، کشته شده است.
یک «منبع آگاه پلیس» در گفتگو با خبرگزاری دولتی مهر، ضمن تکذیب این ادعا، افزود: «پلیس هیچ‌گونه گزارشی مبنی بر وقوع حادثه در هتل اسپیناس دریافت نکرده است.»
@WarRoom
یاشار : خبر‌های از این دست فقط برای گمراه کردن افکار عمومی هست نظر من فقط باید روی اعتصابات تمرکز بشه ! با دقت بگردین از روی ساعت  انتشار ببینید این خبر از چه رسانه هایی پخش شده و از کجا سرمنشأ (قدیمی ترین پست و اولین ) گرفته و بعد بایکوتشون کنید.</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23173" target="_blank">📅 15:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23172">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">حقیقت یاب اتاق جنگ (از سری خبر های فیک ادمین های بیسواد تلگرام) : در دوره هخامنشی، به‌ویژه از زمان داریوش بزرگ،
دَریک سکه طلای هخامنشی
و
سیگلوس سکه نقره‌ای
بود و این دو، نظام پولی دوفلزی هخامنشیان را تشکیل می‌دادند. اما «شِکِل» داستان قدیمی‌تری دارد:
شِکِل در اصل یک واحد وزن در خاور نزدیک باستان بود
و ریشه آن به زبان‌های سامی باستان بازمی‌گردد؛ این واژه بعدها در سنت‌های مختلف، از جمله عبری، به‌عنوان نام یک واحد پول نیز به کار رفت. حتی «سیگلوس» هخامنشی نیز از نظر نام‌شناسی با واژه شِکِل مرتبط دانسته می‌شود. بنابراین اینکه بگوییم
«شِکِل نام واحد پول هخامنشیان یا یک واژه ایرانیِ هخامنشی بوده» دقیق نیست
؛ این واژه ریشه‌ای بسیار کهن در خاور نزدیک داشته و امروزه نیز نام پول اسرائیل است
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23172" target="_blank">📅 14:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23171">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25a166b96b.mp4?token=lkcSj2L_DTWyBiKq7_L45-ub3gVUwPNHMsV5YMHghv5eKq4W-OP2irhi1WlSHkLeOch_h-6qvVzfTclzT-BSrWsFubKBzLzTjpn9Won9On82Q44qTHYUnK9UkgaCAcU1uV6zELSFVpdvVlWd4iJJEy_-wrliAZVGwDxxog2urtOgFUPBDfC7ycmjHnR37_Jl9VhQ6opGg3S2sTR2Fjyp7l1tRmC6xmGShBpfABi9OwUneFq7sdmnXPiVz8Jp0wb_5OWT3HaCzlV5PgT6uCP6OhySr0HubqsJe64HHPfGHiTrxGXKRd5MwgxqpK2kVzqOeNIgX8nnCDtnrPHjTVx_GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25a166b96b.mp4?token=lkcSj2L_DTWyBiKq7_L45-ub3gVUwPNHMsV5YMHghv5eKq4W-OP2irhi1WlSHkLeOch_h-6qvVzfTclzT-BSrWsFubKBzLzTjpn9Won9On82Q44qTHYUnK9UkgaCAcU1uV6zELSFVpdvVlWd4iJJEy_-wrliAZVGwDxxog2urtOgFUPBDfC7ycmjHnR37_Jl9VhQ6opGg3S2sTR2Fjyp7l1tRmC6xmGShBpfABi9OwUneFq7sdmnXPiVz8Jp0wb_5OWT3HaCzlV5PgT6uCP6OhySr0HubqsJe64HHPfGHiTrxGXKRd5MwgxqpK2kVzqOeNIgX8nnCDtnrPHjTVx_GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افشاگری حسن قشقاوی، سخنگوی کمیسیون امنیت ملی مجلس از پیشنهاد همکاری ۵۰۰ میلیارد دلاری جمهوری اسلامی به ترامپ!
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23171" target="_blank">📅 14:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23170">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea5de76aae.mp4?token=o6Ou1kah2ZQAxLZ8dI9XAkyaFTl8zNeWRUJkse_YD_lw_8q1rX01nNacoQVWCIF5mHGbwRLLUc9-NQk3gWGlBKwec92QatKek72dPH0sIyrBQjXC-6Gtv6gGYnb1FL7VSacENB0WCQprKpmtMzzDGIxRaawGdROKp9Eo6oHEHBJyWd0SWYsYnWKJMnoS2yTcNjod8MvRznJj7-UMwYx2_cDP52N4eNQY3ridOaWIJpBC373DJFskXe0dgJfYiz7-3Unvq65gQSotKnt-yCftM1ebvFZETIvv7nO5ckHfoCCzTKNeicmjvBK4CWOrg2nEpLC4MQLSeVFMPFS7gVOt5xA9IUq0oE-B4nDpQwC3Qx8GTCpo2vX1Z8S9Rm6ugcwobLgdzcdB3tAEFjpQ6u0mFIngJx20mR3voDDTxeo9Q_oa9Yq-6NMMq40ILrj7jOLyGe-xn7COyGj15qkDWEKEFIz2c-OPdSl5z1Nliguz-6SV-FGRsL4bR1SW43nk7uUnosZSlBlVsjNo1oXhTMQgH_5crFBz-avo8rwY-omi2mfCWNPrhLxnxX-HIwYIXtfZicb4BDVmpUnN7exR5icOL60b0lE6AhJCJKK80eguzX4Gd4m5Pq-EmGGTtyBJ1COdiUf3hnj7gP-fMGLTTqE2vt1N4fD68sjD-VRK3MRNP7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea5de76aae.mp4?token=o6Ou1kah2ZQAxLZ8dI9XAkyaFTl8zNeWRUJkse_YD_lw_8q1rX01nNacoQVWCIF5mHGbwRLLUc9-NQk3gWGlBKwec92QatKek72dPH0sIyrBQjXC-6Gtv6gGYnb1FL7VSacENB0WCQprKpmtMzzDGIxRaawGdROKp9Eo6oHEHBJyWd0SWYsYnWKJMnoS2yTcNjod8MvRznJj7-UMwYx2_cDP52N4eNQY3ridOaWIJpBC373DJFskXe0dgJfYiz7-3Unvq65gQSotKnt-yCftM1ebvFZETIvv7nO5ckHfoCCzTKNeicmjvBK4CWOrg2nEpLC4MQLSeVFMPFS7gVOt5xA9IUq0oE-B4nDpQwC3Qx8GTCpo2vX1Z8S9Rm6ugcwobLgdzcdB3tAEFjpQ6u0mFIngJx20mR3voDDTxeo9Q_oa9Yq-6NMMq40ILrj7jOLyGe-xn7COyGj15qkDWEKEFIz2c-OPdSl5z1Nliguz-6SV-FGRsL4bR1SW43nk7uUnosZSlBlVsjNo1oXhTMQgH_5crFBz-avo8rwY-omi2mfCWNPrhLxnxX-HIwYIXtfZicb4BDVmpUnN7exR5icOL60b0lE6AhJCJKK80eguzX4Gd4m5Pq-EmGGTtyBJ1COdiUf3hnj7gP-fMGLTTqE2vt1N4fD68sjD-VRK3MRNP7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ:
راستش را بخواهید، عمویم احتمالاً بهترینِ تمام دوران بود؛ او ۴۱ یا ۴۲ سال استاد دانشگاه ام‌آی‌تی (MIT) بود و به عنوان یکی از درخشان‌ترین افراد شناخته می‌شد.
بنابراین، اگر به «نظریه وراثت» (یا قدرت ژنتیکی) اعتقاد داشته باشید، من هم از چنین توان ژنتیکی‌ای برخوردارم. من که معتقدم؛ ژنتیک در من وجود دارد. من از هوش مصنوعی هم سر در می‌آورم.
ربات‌ها قرار نیست کنترل امور را به دست بگیرند. هوش مصنوعی قرار نیست بر بقیه جهان مسلط شود. کل این ماجرا یک فریب و حقه است.
@WarRoom</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/23170" target="_blank">📅 14:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23169">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کانال ۱۴ : نیروهای دفاعی اسرائیل در حملات دقیق و هدفمند در
خان‌یونس و شهر غزه
، دو عضو ارشد شاخه نظامی حماس را از بین بردند. بر اساس اعلام ارتش اسرائیل، این افراد در
تولید و توسعه تسلیحات، برنامه‌ریزی حملات علیه نیروهای اسرائیلی و بازسازی توان نظامی حماس
فعالیت داشتند و این اقدامات را نقض آتش‌بس می‌داند.
همچنین در روزهای اخیر، ارتش اسرائیل اعلام کرده بود
محمد عبدالرحمن الیزوری، فرمانده تیپ خان‌یونس حماس و عضو شورای رهبری این گروه
نیز در حمله‌ای هدفمند کشته شده است؛ حماس نیز کشته‌شدن او را تأیید کرده ، او در برنامه‌ریزی حمله ۷ اکتبر نقش مهمی داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23169" target="_blank">📅 14:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23168">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : هیچ هدف‌گیری‌ای داخل شهر مکه مکرمه صورت نگرفته است. دو پایگاه هوایی در نزدیکی مکه قرار دارند: پایگاه هوایی ملک فهد در طائف و پایگاه هوایی ملک عبدالله در جده. هواپیماهای جنگی سعودی از این پایگاه‌ها برای انجام عملیات و بمباران در یمن پرواز می‌کنند. طی روزهای گذشته نیز شاهد تحرکات هواپیماهای جنگی سعودی از پایگاه هوایی ملک فهد در طائف به سمت یمن برای انجام عملیات بمباران بوده‌ایم. از سوی دیگر، شهر جده از نظر تقسیمات اداری در منطقه مکه مکرمه قرار دارد، نه در محدوده خود شهر مکه. بنابراین هنگام انتشار این اخبار، باید میان «شهر مکه مکرمه» و «منطقه مکه مکرمه» تفاوت قائل شد.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23168" target="_blank">📅 13:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23167">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23167" target="_blank">📅 13:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23166">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دیدبان اتاق جنگ : یاشار پرسنل برج مراقبت امام و معراباد اعتصاب کردن از دیشب تمام پروازا تاخیر دارن هنوز پروازای داخلی رو باند نشستن
مثلا پرواز مشهد به زاهدان باید ساعت ۹ صبح میپریده هنوز رو بانده
@WarRoom
رسانه های رژیم بدون توضیح : در پی تاخیر در تعدادی از پروازهای روز گذشته و نارضایتی مسافران، دادستانی تهران در راستای حفظ حقوق عامه به موضوع ورود کرد.در همین رابطه با موضوع تاخیر پروازها و بررسی آن پرونده قضایی تشکیل شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23166" target="_blank">📅 13:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23165">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یکی از رهبران حزب دموکرات کردستان: یک راکت در داخل اردوگاه حزب در منطقه بالیسان، شمال اربیل، سقوط کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/23165" target="_blank">📅 13:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23164">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نیروی دریایی سپاه : تنگه هرمز مسدود است و همچنان تحت کنترل هوشمند نیروی دریایی سپاه  قرار دارد یک تانکر نفتی بزرگ به نام «EL GAIA ال گایا» پس از برخورد با مین‌های دریایی در حین تلاش برای عبور از منطقه ممنوعه در جنوب تنگه هرمز، منفجر شد. تلاش‌ها برای مهار آتش…</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23164" target="_blank">📅 13:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23163">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">هواپیمای دولتی با شناسه پروازی «IRAN06» یک مقام رژیم جمهوری اسلامی از تهران در فرودگاه ریاض، عربستان سعودی به زمین نشست @WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23163" target="_blank">📅 13:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23162">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آسوشیتدپرس: بحران جدید بر سر محمد اسلامی
: ایران رسماً اتریش را به دلیل جلوگیری از ورود محمد اسلامی، رئیس سازمان انرژی اتمی ایران، به نشست آژانس در وین محکوم کرده است. کمیته شورای امنیت با مخالفت آمریکا حاضر نشده معافیت سفر اسلامی را صادر کند. روسیه از اعتراض ایران حمایت کرده و تهران این اقدام را نقض تعهدات اتریش به‌عنوان کشور میزبان نهادهای سازمان ملل دانسته است.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23162" target="_blank">📅 13:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23161">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5yd6lOlvPnZjQxbdvaBKWhmkyeBmzEnTZy9-uzCsidQicKawOMACBFsNGBw3iAw7jwPqqViYLkZyWQqH9BLEh5VN2pFT-hutp_7UpD3zU-Ur8qzfEXzGI4t3K-WqE5s68k1jQAr5Jju9UWkcN2eQEWJIF60lzFxFuEaDWUyIeYYnteJexRmXRr6GRnnOqyBs_BDfoPJftXfexz8EgLtitoIpSUaCAgsh08-Jo9riXBMhVzdYis-dhBBcxUi8s_pHpZfQA-WrZyixWChjdxNTdxfiIAU3AKSY5ArPn7KMBhrw7S27IIcqP8fRCuXi5enLbJNjb0Xtq8BnFdAGjjK2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:  گزارشی‌در‌دست بررسی درباره هدف قرار گرفتن یک کشتی با یک پهپاد در تنگه هرمز دریافت شده است. @WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23161" target="_blank">📅 12:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23160">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:
گزارشی‌در‌دست بررسی درباره هدف قرار گرفتن یک کشتی با یک پهپاد در تنگه هرمز دریافت شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/23160" target="_blank">📅 12:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23159">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc00b8f8cd.mp4?token=YrV28CLSJiSYDQenrXeFTUYNLv1Y9bljjhG-MYbrbdNqwAHxzf_QaCjySLYpJsgvNsJE09BGotV-dvYhISXKB4jeSDRxQnApsiHU3phBbi4Xo95R1q0VXpFzaHtBd0e7Pnl0jG4uEGUuXnTBWzEpxQe3Z4Oi6HnPqGgexxakW0T_CVAXn3pUWbNn2MI_RURfbV2bU5RngQvgNSaCwjZQ8UFzKV4naRrqW9mFfqHmo26QCg-DKnqkMKbQ_ak8SyJI-CiXOYQzTBc8kTb3UMArUBKv_oXam1SnpaiFnWerFiL1_oNaQWyxSahkhiV8DFEJp_y3sCS2kGG6nemSz3BPxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc00b8f8cd.mp4?token=YrV28CLSJiSYDQenrXeFTUYNLv1Y9bljjhG-MYbrbdNqwAHxzf_QaCjySLYpJsgvNsJE09BGotV-dvYhISXKB4jeSDRxQnApsiHU3phBbi4Xo95R1q0VXpFzaHtBd0e7Pnl0jG4uEGUuXnTBWzEpxQe3Z4Oi6HnPqGgexxakW0T_CVAXn3pUWbNn2MI_RURfbV2bU5RngQvgNSaCwjZQ8UFzKV4naRrqW9mFfqHmo26QCg-DKnqkMKbQ_ak8SyJI-CiXOYQzTBc8kTb3UMArUBKv_oXam1SnpaiFnWerFiL1_oNaQWyxSahkhiV8DFEJp_y3sCS2kGG6nemSz3BPxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیچ‌کس متوجه نشد که
یک ساختمان کامل در جزیره ابوموسی ایران کاملاً منهدم شده است.
تصاویر ماهواره‌ای مربوط به
۹ سپتامبر (۱۸ شهریور)
نشان می‌دهند ساختمانی که پیش‌تر سالم بوده، اکنون کاملاً از بین رفته است
@WarRoom</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/23159" target="_blank">📅 12:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23158">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/555689f2d1.mp4?token=qeCCJd8fyOsaGQBLVYJEU6Q2dxWywwB6LIDORuzDio9tEDUwHjO6p88Z7aXGdQXOJwcFxmux-hLbhTLr9J30SkulV4_5aw7DngVqLhtUCvCqUtHEfpu8uJRBmJFmACF1enlEzdtMNUa2L2UwEACG9CJPh7MURDphXI6QFfzruoM7dcQTnhw3WA5BcupQhlblPdg8LP4hX_MlS110J-nw4apVeiTEfO-LjwB70-C7bMPsWW9zqhyVpFogxscIMN1sUpJ8wYS7VfZq3eCwWDOaU3Sm3oU3uRovodbqLXr8qqlUEAFv6zjs9no3GkTkYep8TW2ZQfUQqEH_n2fjVC8fuzQeM8uorEwnjGnURzrvV19esZoDB1cj6l1aQlwRjC3ilS17SlmlbinZcFSgqBmvPfHKQPlTn_5wLRzTOrOmY_YOzsH_sB94pUIrIn17nzh5xqRWSLUsCszsEyDDEfkplNmaIXYZhOh5bgUsrJA1WmyMS9qG9DpZ_AwMAjO8M00iBPg1mvuRhZB0MbNtQIQJiyQNSud7S8yKvrdgFI2H7O30a2ZBpry2E-cfSdR5zges9lH48abU-f77mg_4-UrTh7ePwWF3Zi4-0hHoZk--jtmksqy7LHN_3QHotglwc2dfgYjvcuzH_62sWXO1Bhu0eTHLpRt1Wihx7ilKNKNMrSE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/555689f2d1.mp4?token=qeCCJd8fyOsaGQBLVYJEU6Q2dxWywwB6LIDORuzDio9tEDUwHjO6p88Z7aXGdQXOJwcFxmux-hLbhTLr9J30SkulV4_5aw7DngVqLhtUCvCqUtHEfpu8uJRBmJFmACF1enlEzdtMNUa2L2UwEACG9CJPh7MURDphXI6QFfzruoM7dcQTnhw3WA5BcupQhlblPdg8LP4hX_MlS110J-nw4apVeiTEfO-LjwB70-C7bMPsWW9zqhyVpFogxscIMN1sUpJ8wYS7VfZq3eCwWDOaU3Sm3oU3uRovodbqLXr8qqlUEAFv6zjs9no3GkTkYep8TW2ZQfUQqEH_n2fjVC8fuzQeM8uorEwnjGnURzrvV19esZoDB1cj6l1aQlwRjC3ilS17SlmlbinZcFSgqBmvPfHKQPlTn_5wLRzTOrOmY_YOzsH_sB94pUIrIn17nzh5xqRWSLUsCszsEyDDEfkplNmaIXYZhOh5bgUsrJA1WmyMS9qG9DpZ_AwMAjO8M00iBPg1mvuRhZB0MbNtQIQJiyQNSud7S8yKvrdgFI2H7O30a2ZBpry2E-cfSdR5zges9lH48abU-f77mg_4-UrTh7ePwWF3Zi4-0hHoZk--jtmksqy7LHN_3QHotglwc2dfgYjvcuzH_62sWXO1Bhu0eTHLpRt1Wihx7ilKNKNMrSE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات بسیار بزرگ‌تر از یک حمله تنها فقط به خط لوله نفتی شرق-غرب عربستان سعودی به نظر می‌رسد. تصاویر ماهواره‌ای اکنون
آسیب قابل‌توجهی در ایستگاه پمپاژ شماره ۹
را نشان می‌دهند و در ایستگاه پمپاژ شماره ۸ نیز نشانه‌هایی از آسیب احتمالی دیده می‌شود؛ هر دو ایستگاه در امتداد همین سامانه حیاتی خط لوله قرار دارند. اگر آسیب‌های اضافی تأیید شوند، عربستان سعودی با آسیب به
چند تأسیسات حیاتی در طول یک مسیر واحد
مواجه است. ممکن است این خط لوله برای چند هفته عمدتاً از مدار خارج بماند و برآوردها زمان تعمیرات را
۳ تا ۵ هفته یا حتی بیشتر
اعلام می‌کنند. این وضعیت فشار بر توانایی عربستان سعودی برای انتقال نفت خام به
ینبع و دیگر زیرساخت‌های صادراتی دریای سرخ
را افزایش می‌دهد؛ آن هم در شرایطی که مسیرهای جایگزین از پیش با محدودیت‌های شدیدی مواجه هستند
@WarRoom</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/23158" target="_blank">📅 12:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23157">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏خبرگزاری رژیم فارس، با استناد به سندی که خبرنگارش رویت کرده، گزارش داد دولت در چهار ماه نخست سال بیش از ۳۴۰ هزار میلیارد تومان از صندوق توسعه ملی برداشت کرده؛ رقمی بالاتر از سقف ۳۳۰ هزار میلیارد تومانی تعیین‌شده در بودجه. برداشت دولت از صندوق توسعه ملی در چهار ماه نخست سال گذشته ۱۰۳ هزار میلیارد تومان بود و در مدت مشابه سال جاری بیش از سه برابر شده است. صندوق توسعه ملی در چهار ماه نخست سال ۲۰ درصد بودجه دولت را تامین کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/23157" target="_blank">📅 11:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23156">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ua203pqVCSnni1pX17AuLAO1dN7d-I2evAvGbutKH-iKMMgY6gatoanWYnzxd-nViAuyk9da2KSgybdHDM73uajMqvqobLYJ7GNWkr850XIOu39TAOm1G9JJLJ_g2lDIp01QgqGjB7bDWIhxAJ5kMlWHr6UpuJxG9AX22wLNxw_fzcnKn5wt2bTOrbSXCa6xV5O530EzXs_BTbwQheo0GRWb0K9WbTbUPaXaL287g_LpnqjRuPuHFh7r0b1CaU4EKMq_tOduo3_YFVRNuaOZwmlLJoxaHfPAOorXyASWAMwpwjEM0LFMELLW6XdZBPFpxGb6ZfAeQZ_SfJp34p3LPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای دولتی با شناسه پروازی «IRAN06» یک مقام رژیم جمهوری اسلامی از تهران در فرودگاه ریاض، عربستان سعودی به زمین نشست
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23156" target="_blank">📅 11:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23155">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">استاد بزرگ شطرنج ،نتانیاهو: ‏شرایط برای سقوط جمهوری اسلامی فراهم شده و جهان هم حاضر به همکاری است‌. @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/23155" target="_blank">📅 11:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23154">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjKZQBtnUCJrMFZuWLXt2wk2xY1chtNGejnWbcVU_kUacYv5U6HnWCJuadUcE065PyRuac-4jcmG_rEj0-SjTQoMV6kCjtYvaDtt_yV1uw8DdlflvA7nPXFQxSKW47K048gM46foVcrFHXGQwfZIyzMVlMDrygDMo-Qd1uYPC3VsYyP63GfPs7PfZze7-8nkt-Ycg-27e9eGvf5an2E4Rqdty3xU4B5wg8hYygg99FcWsldMcBJZb-nWud7p8cmUMAVNbBd7qcdoqIq02Bxx2eYDuwJ6zUS8HiKinm4qNBaS5It7cp4AV5BxLHWKDQwZaKxTMvmNo12EnZiITSyYOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهاجرانی، سخنگوی دولت: امیدواریم نیازی به تغییر سهمیه‌های اول و دوم بنزین نداشته باشیم
, تولید داخلی بنزین حدود
۱۰۰ تا ۱۱۰ میلیون لیتر در روز
است، در حالی که مصرف روزانه کشور حدود
۱۴۰ میلیون لیتر
است و برای تأمین این کسری باید منابع لازم برای واردات بنزین فراهم شود. اصلاح نرخ سوم بنزین قرار بود در زمستان انجام شود، اما به‌دلیل شرایط جنگی به تعویق افتاد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23154" target="_blank">📅 11:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23153">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcWwonfu_zMcR8z8eL-6pP8H-An3S49hcJnWyRFQDUGI_FoPgUwadVIqcjfmrwZZHhw8LmaB4NOCb72SXBtbPvkKJtegH7ltb8XSMzv3NZE8ihZHox7f-5VnccPYmwDhJ1VrkILlqsI7CQgZMH7u-ttFb2vZRWg8k1d4IgMqm-e5PTECDFB-vjxe6q7PNMD7F4fiCB8kqtsnpdHKx1KHhhf2XrjyRsVTsduhp7_JRSjjraFAY3IUU_fgf2ujQj7Mrikll61qtzK8LLvoniZEZdCsz0Mt6ZdZBHD0SxyER6Qu2Qv8giGNgppj5_qv-FpudzX-WbF8B5lOmRq4QzN80g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هویت خلبان جنگنده‌ اف۱۵ که در مصاحبه با ABC نام مستعار براوو معرفی شده بود، مشخص شد؛ او
سرهنگ دوم جاناتان دبلیو بات (Lt. Col. Jonathan W. Bott)
است
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23153" target="_blank">📅 11:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23152">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">رویترز ـ نفت دوباره صعود کرد:
قیمت برنت امروز حدود ۲ درصد افزایش یافت و به
۱۰۷.۵۵ دلار
رسید؛ نفت WTI نیز به
۱۰۳.۲۷ دلار
رسید. عامل اصلی، نگرانی از ادامه توقف خط لوله شرق–غرب عربستان و تشدید حملات حوثی‌ها عنوان شده است. این خط لوله حدود
۴ میلیون بشکه در روز
ظرفیت انتقال به ینبع دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23152" target="_blank">📅 10:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23151">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آمریکا برای نخستین بار تأیید کرد که تسلیحات نظامی در فضا مستقر کرده است.
دکتر تروی مینک، وزیر نیروی هوایی آمریکا، اعلام کرد این کشور اکنون دارای «تسلیحات کنترل فضایی مستقر در مدار» است که برای حفاظت از نیروهای آمریکایی و متحدان این کشور در برابر اقدامات خصمانه طراحی شده‌اند. مینک از شناسایی این سلاح یا افشای قابلیت‌های آن خودداری کرد و گفت حفظ محرمانگی برای تداوم اثر بازدارندگی آن اهمیت دارد. مینک همچنین گفت آمریکا اکنون
سخت‌افزار آماده پرواز
برای رهگیرهای فضایی در اختیار دارد که به‌عنوان بخشی از سامانه دفاع موشکی «گنبد طلایی» در حال توسعه هستند
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/23151" target="_blank">📅 03:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23150">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رئیس ستاد نیروی هوایی آمریکا، ژنرال کنت اس. ویلباخ، به TWZ گفت پهپاد رزمی MQ-9A ریپر نیروی هوایی آمریکا در جریان عملیات «خشم حماسی» به ۸۶۰ هدف حمله کرد. وی همچنین اعلام کرد در طول این عملیات بیش از ۱۳ هزار «هدف نظامی» مورد اصابت قرار گرفت؛ ۵۰۰ فروند هواپیما بیش از ۱۰ هزار سورتی پرواز (مأموریت پروازی) انجام دادند که میانگین آن بیش از ۲۵۰ سورتی در روز بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23150" target="_blank">📅 03:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23149">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا، اسکات بسنت: در چارچوب «عملیات طرد اقتصادی»، وزارت خزانه‌داری به هدف قرار دادن و مختل کردن فعالیت کسانی که حمایت‌های مادی، فناوری یا مالی لازم برای تداوم فعالیت‌های تروریستی رژیم ایران را فراهم می‌کنند، ادامه خواهد داد. وزارت خزانه‌داری هیچ‌گونه حمایتی از این رژیم را تحمل نخواهد کرد و همچنان به شناسایی، افشا و منزوی کردن عوامل و پشتیبانان جمهوری اسلامی ادامه خواهد داد
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23149" target="_blank">📅 02:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23148">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رویترز: حمله جدید حوثی‌ها به عربستان باعث شد مذاکرات هرمز به تعویق بیفتد
: حوثی‌های مورد حمایت ایران روز دوشنبه حمله جدیدی به عربستان انجام دادند و سپس هم‌زمان کشورهای عرب خلیج فارس دیدار برنامه‌ریزی‌شده با ایران درباره پیشنهاد مدیریت تردد در تنگه هرمز را به تعویق انداختند.نه ایران
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23148" target="_blank">📅 01:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23147">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23147" target="_blank">📅 01:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23145">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lp3k2ZiQWxfYrMd09bZMIkEP_8qgH3uw29TQbEwqccGfJSE2LfxR1KUpmmXmIRvyudMTVpfZ0NMW3UyBxgdQRdY55_46rc_w7Cy4y8uENxs0nry_toSXvgyU8ed9x20DtRM13bJeve7Byndm5iMsCOQHgiDq8N1eS5jTjnFNr_iAP-5NPSQQ9NI_vlkRxdAuCoLWbKocVDwioAaOVtkbenww6hgdZGgvYu8sGHO5Cm4tjDalObXMKOAo4-CH3F6ExyBsudoXu-0Pk5gDbvlsFemXVrLBiTOnwXrenmi5-C1kRwLG7yrfdKoGiQLfx6wRbjNbTxM04e3fU2tUswYxXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JfCAbuEzIcRZz9UKD1q_p8LpdEWRMheTqiSxz3Dp7HgbYBFzAAvppWb0tUN_uN_W2o6DaL_hG6ZHXbsA7DP3tNiNmjzETBGa7pRlNWZIJgnVT_bZ8aKRKtacj0Z6bRZuQd4pq7VcYdUzLv85LnSy8Gy8lQVaPtzxrKuffuJ1b34qkGRtyQzdIsI4vlEw9aNn5aqxuE2kJZguO_ymvXUZrl6bcDwIhU0x4EF2Xk-oqkBWpoEN-pC0riD-WPetAbgJiMJz4cMAsjX5ArSCHP2ihvnUGeg3jhWqznjPbjQGvxICnwTUaHpWg5inz6zuzStLJ0Vi64g2SuMXey-EN15MAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فقط ببینید من اینجا تو دایرکت با چه  حرومزاده هایی طرفم. نگاه کنید، عکس رو فرستاده، اسمش ساواکی، عکس پروفایل شیر و خورشید هم گذاشته. بعد عکس رو دابل چک کردم مال ۲۰۲۴ تویه سایت چینیه… که بیان منو بعدش خراب‌کنن !!!
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23145" target="_blank">📅 01:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23144">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">محسن کج بند ، دبیر شورای عالی امنیت ملی :
تا زمانی که شرایط ایران برآورده نشود، هیچ مذاکره‌ای با آمریکا انجام نخواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23144" target="_blank">📅 00:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23143">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzQUaGNITb6mws4uTWv2tDP7ehNOBPIfUfpdVtxPq6jIKdb-8KAZB6yD3NRK664cYP6ZHT0PZvJ71yzkBtY4odcnZMB7aB8KyGnbcdw_U0Oulo-6H7HZ5oonNtT3-Awm_Ux-WmT50xfhczITeuJBoEFv4YppJCUKE65_82fwu6MFllZ8t2-VcfVJtBuaqgFYkaelsUGrkDK8MsOLRjVviXs5aeBf18QYxx6BXBgIezlfwvJw2mGmJb1vV46OaE2Uaxb1ty6KKb17EbMpXauwjfr3--sNIH9n_-mzkdNRpO5Ohx1oRrZx3DS9M4igWWOLdegDi7bTKgA3teIwOygr2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ در‌تروث
:
من متخصص افشای حقه‌ها هستم و همین الان دارم یک حقه دیگه رو هم افشا می‌کنم؛ اینکه هوش مصنوعی قراره دنیا رو در اختیار بگیره، همه‌چیز رو ببلعه و نابودش کنه و ربات‌ها قراره وارد شهرهامون بشن و همه ما رو از بین ببرن.این حتی از ماجرای «روسیه، روسیه، روسیه» یا حقه تغییرات اقلیمی هم عجیب‌تره.ممنون که به این موضوع توجه کردید!
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23143" target="_blank">📅 00:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23142">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">استاد بزرگ شطرنج ،نتانیاهو:
‏شرایط برای سقوط جمهوری اسلامی فراهم شده و جهان هم حاضر به همکاری است‌.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/23142" target="_blank">📅 00:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23141">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اتاق جنگ با یاشار : در درگیری امروز گزارش شده از دیدبان اتاق جنگ ,  ۲ قایق تندرو سپاه که از اهالی کرگان(میناب) بودند(اکثر این اهالی با حکومت هستند و پاسدارند) عصر امروز هدف حمله آمریکا در تنگه قرار گرفتن ۱ جسد پیدا شد و ۳ نفر  دیگه فعلا تا این لحظه نگارش این…</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23141" target="_blank">📅 23:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23140">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نفت به کانال ۱۰۵ دلار
🔻
وارد شد !</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23140" target="_blank">📅 23:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23139">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حقیقت یاب سنتکام: ادعای سپاه پاسداران مبنی بر اینکه یک نفتکش با پرچم پاناما در تنگه هرمز با مین دریایی برخورد کرده،
کذب است
. نفتکش «اِل گایا» ماه گذشته بر اثر اصابت یک موشک ایرانی از کار افتاد و سپس این آخر هفته، در نزدیکی سواحل عمان، بار دیگر هدف یک پهپاد ایرانی قرار گرفت. اکنون یک شریک منطقه‌ای در حال یدک‌کشیدن این نفتکش است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23139" target="_blank">📅 23:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23138">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e138586742.mp4?token=LBE44pM7POaO7HJYMJRSZmXx114YrbDeJVh82WDzHwxcnfKM3sa46sevUw6C3YzyplWc-sykt47VERMto07v0XbYcHk2A1eOUPiPgNxvM5INPZx1bCGMIeTKjCQMBnIZAPiIGr0idJuAevaPHEPACq1IghlNBVXSl34C7gpl36viVteDwGEAA5ZLOgoCvB0o2NMAaB3zwEeMJGYkh3Az3iTyXJOyA88yuyeeQ54iXujZ0JFtrPWqXIC57pk_gJOzjpJMsQxbFRVBkZsNikpWWhPWcqGZeNjSFZ1HpXMUd7i73K7zgz-LWsyN_OUsHoEC1EaOMD4uLwcUvllDpaRYdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e138586742.mp4?token=LBE44pM7POaO7HJYMJRSZmXx114YrbDeJVh82WDzHwxcnfKM3sa46sevUw6C3YzyplWc-sykt47VERMto07v0XbYcHk2A1eOUPiPgNxvM5INPZx1bCGMIeTKjCQMBnIZAPiIGr0idJuAevaPHEPACq1IghlNBVXSl34C7gpl36viVteDwGEAA5ZLOgoCvB0o2NMAaB3zwEeMJGYkh3Az3iTyXJOyA88yuyeeQ54iXujZ0JFtrPWqXIC57pk_gJOzjpJMsQxbFRVBkZsNikpWWhPWcqGZeNjSFZ1HpXMUd7i73K7zgz-LWsyN_OUsHoEC1EaOMD4uLwcUvllDpaRYdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فریدالدین حداد عادل
، برادر زن مجتبی
:
سید مجتبی با همسرشان فرار از زندان را به طور کامل تماشا کرده بودند
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23138" target="_blank">📅 23:26 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23137">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏ کادو عروسی برای داماد در یمن @WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23137" target="_blank">📅 22:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23136">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4ccf5e55.mp4?token=tkQoRpEBLjKQGHLwSX4ds3PYxsKu6Zg8rn_n66EMGi4u9VEmnoOB3X4shC-x16n39GibJ_HopRaUw6DnGPh8AoMgBdgmFPWcPguKfU_cTlq7nUBte66LSikU-d_twRxn_u1LS2eSSnXdCLuLhC_qoWpsdfkQHx6vqkoJtvHmnuO3mKIqr5EUq-IxjJ8O30Y7deinz3YAP3N8ANazoDhLBvfoQBaX8ld10I7P_S4QvgiW8CUYZNIr69t6FToI2z_CGRcwgoMURGYkOXNKnhbVFzonPCFFVXpeD_kMcQofDlMsoq-QobBZdAhGZj1rk8o1j3a3YQZks0GPv_zNoyeec2u64f4Khj49hgKvVmmZmH4LpyroMx0SxYdTHZpRbuWdBOQ2aJbjzozmQcWE9Wdnm84BjnQ0vT-7T6HxsuA1DOVYJwzBx8f23Kz6-wlX4JsGHE3HQhkrbtzV2qp2tVwHiszOQmtfq5h_ijcOajp3by5D0Mu2g1CfPBoWZTSbwCdkOou03eNJ743FQDLNXqkBCwG5_j_CX4L6hZxXBKnkXbaJV-AbcXLCv54oCSalSWB4OkOj0L_gwnlojQR3KEHNl_Nx9U7TjYYcNCO5Y8vv9kxyeXc6n4owVOPQrlvfHT6a68zNIcAZFSSG1mKYQSbblmfv4Cc52lQJtOXwkFftEL4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4ccf5e55.mp4?token=tkQoRpEBLjKQGHLwSX4ds3PYxsKu6Zg8rn_n66EMGi4u9VEmnoOB3X4shC-x16n39GibJ_HopRaUw6DnGPh8AoMgBdgmFPWcPguKfU_cTlq7nUBte66LSikU-d_twRxn_u1LS2eSSnXdCLuLhC_qoWpsdfkQHx6vqkoJtvHmnuO3mKIqr5EUq-IxjJ8O30Y7deinz3YAP3N8ANazoDhLBvfoQBaX8ld10I7P_S4QvgiW8CUYZNIr69t6FToI2z_CGRcwgoMURGYkOXNKnhbVFzonPCFFVXpeD_kMcQofDlMsoq-QobBZdAhGZj1rk8o1j3a3YQZks0GPv_zNoyeec2u64f4Khj49hgKvVmmZmH4LpyroMx0SxYdTHZpRbuWdBOQ2aJbjzozmQcWE9Wdnm84BjnQ0vT-7T6HxsuA1DOVYJwzBx8f23Kz6-wlX4JsGHE3HQhkrbtzV2qp2tVwHiszOQmtfq5h_ijcOajp3by5D0Mu2g1CfPBoWZTSbwCdkOou03eNJ743FQDLNXqkBCwG5_j_CX4L6hZxXBKnkXbaJV-AbcXLCv54oCSalSWB4OkOj0L_gwnlojQR3KEHNl_Nx9U7TjYYcNCO5Y8vv9kxyeXc6n4owVOPQrlvfHT6a68zNIcAZFSSG1mKYQSbblmfv4Cc52lQJtOXwkFftEL4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ کادو عروسی برای داماد در یمن
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23136" target="_blank">📅 22:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23135">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFQGLp2pTDKB3jlOqQ_cspvy5w2i-UwHWCXUL3066jXy443Ax5dZjPabGvItpoDdpV_tAox1z-PXdckXQIDeyIRbCxJRYb7FuCW_jITk8UnvdCs3XUQw0FPyheeW7p4n_vIJ_h_-ht5EG9rrikZKEIUJi9cXvCW1Raqy7Yp--h5xaRKaLPf5VQl4Cs7DN8yuH9j0qoxpab3TO3uJvcAaE0DeAr7dDjQKcn9h3QUz66M-MXp4StDtLyAkkbrsJaIwFcsJAOhiomDfEp9ph_8B3So_ZeE8F3Syqdjvr8jzbGdAxekD0x4WvAbnXpPnI2SKkp0DoRQnxlxQNrhfSnDaKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه :
تنگه هرمز مسدود است و همچنان تحت کنترل هوشمند نیروی دریایی سپاه  قرار دارد
یک تانکر نفتی بزرگ به نام «EL GAIA ال گایا» پس از برخورد با مین‌های دریایی در حین تلاش برای عبور از منطقه ممنوعه در جنوب تنگه هرمز، منفجر شد. تلاش‌ها برای مهار آتش بی‌نتیجه بود و آتش به طور کامل تانکر را از بین برد
پیش از این، از خطرات عبور غیرقانونی در این مسیر، هشدار داده شده بود
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23135" target="_blank">📅 22:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23134">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا تحریم‌های مرتبط با ایران را علیه بانک «وی‌تی‌بی» (VTB) روسیه اعمال کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23134" target="_blank">📅 22:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23133">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نخست‌وزیر بریتانیا در حال بررسی درخواست عربستان برای حمایت نظامی در برابر حوثی‌هاست»
طبق گزارش، درخواست ریاض شامل کمک برای
دفاع از زیرساخت‌های نفتی عربستان و جلوگیری از پیشروی حوثی‌ها به سمت باب‌المندب
است. بلومبرگ می‌گوید برنهام در واکنش اولیه، با
اعزام مشاوران نظامی بریتانیا به عربستان
موافقت کرده؛ اما این به معنای ورود مستقیم نیروهای بریتانیا به جنگ یا آغاز عملیات رزمی نیست.
@WarRoom
حقیقت یاب اتاق جنگ : نیروی دریایی سلطنتی بریتانیا از قبل در منطقه حضور داشته و در عملیات‌های دریای سرخ نیز ناوهای بریتانیایی مشارکت داشته‌اند ولی خبر
اعزام ناو بریتانیایی جدید مطرح نشده ایت و جعلی میباشد</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23133" target="_blank">📅 22:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23132">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فاکس‌نیوز: حوثی‌های یمن طی سال‌های اخیر یک
شبکه مالی چندمیلیارددلاری
ایجاد کرده‌اند که به آنها اجازه داده با وجود تحریم‌های آمریکا، منابع مالی لازم برای ادامه عملیات نظامی خود را تأمین کنند. این شبکه شامل
قاچاق نفت ایران، کنترل و بهره‌برداری از بنادر و گذرگاه‌های تجاری یمن، شبکه‌های حواله و انتقال پول و استفاده از رمزارزها
است. بر اساس این گزارش، حوثی‌ها بخشی از درآمدهای خود را از مالیات و عوارض اجباری بر کالاهای وارداتی و فعالیت‌های اقتصادی در مناطق تحت کنترلشان به دست می‌آورند و از شبکه‌های مالی غیررسمی برای انتقال و پنهان کردن درآمدها استفاده می‌کنند. حمایت مالی و لجستیکی ایران نیز نقش مهمی در حفظ این ساختار داشته و این شبکه اکنون به یکی از منابع اصلی تأمین هزینه‌های نظامی حوثی‌ها تبدیل شده است
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23132" target="_blank">📅 21:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23131">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1KWm0m-zAkmbIxEgl0oqoCwswvadVAJf-T1d1eaTYfihN95fD7GBO2BRjF_EBsEfsSn4QmpiHuzbwOGOlxbhwxWgnFVgpw3LICjf0zNl7bnYGWhWhZDcvucXy6ml3wKd2P2TGSXjQMIB3UU24D_NTDABWFoX5-UTZjllGxt_7A7MvAsEF7enUZ_1Y0NyS-QkJb2WHcmGC4sxEjFfuygmGuv-zllykX3jv-7BiX7UKzioo4Eok7AQ3m3PGNSlUIEDvx2YwkKvnlrQFv0seZZfx3PnAzJkyG4Vj6JRkDePUrOo9-lihWqNysom57PxoiL3XGbAp_8B9BB6djEf90apA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : قایق سپاه که تو سواحل جاسک هدف قراره گرفته بود رو معلوم نیست چرا از زیر اب در اوردن و دارن میبرن جای نامعلوم، ی طرفش کاملا متلاشی شده
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23131" target="_blank">📅 21:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23130">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzAZReGJVvdsqzrE4knouQ7TUUfeJ7YmBAGKetGPbK_T5vUGIPCXNW_sJR3oNbmZXQUeh5d6G2MmBg4No1DIpBmZE_dZqs1-mZ5cqK55uywDyz0D3PeAForReDpSbgSI2XoVvuvwP5XBedsbjXohsPr1gIBof1cQqR2SI1dhkXFso_i1zDK1PunsQOTtCzrzVwRKwe3rufP-jKr_QBvpM7IzyIRNFxwtJNJ_mXqe2C1l3Nr_LdEMnVPHterCCq1xXbBYqNtGDbm3rLruF_-SJMThVny78nqhlo6fjTu2c9tFU-E30ULCQKsdOOvd20k2VpVpYurKk-krCsJKaqk6iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به هلاکت رسیدن
امام جماعت مسجد محمد رسول‌ زاهدان
با نام
یوسف گرگیچ
توسط افراد ناشناس
گرگیج امروز کمی قبل از کشته شدن در مراسم تشییع شهدای امنیت سپاه پاسداران حضور داشت و این تصویر مربوط به آخرین مصاحبه وی است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23130" target="_blank">📅 21:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23129">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرنگار العربیه: هم اکنون نیروی هوایی اسرائیل شهرک کفرتبنیت در جنوب لبنان را بمباران کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23129" target="_blank">📅 20:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23128">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بعد از این خبر نفت رو به پایین شد هم اکنون ۱۰۸$  @WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23128" target="_blank">📅 20:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23127">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏نیروی هوایی عربستان سعودی تصاویری از حملات هوایی علیه اهداف حوثی‌ها در یمن منتشر کرده است. @WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23127" target="_blank">📅 20:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23125">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اتاق جنگ با یاشار : در درگیری امروز گزارش شده از دیدبان اتاق جنگ ,
۲ قایق تندرو سپاه که از اهالی کرگان(میناب) بودند(اکثر این اهالی با حکومت هستند و پاسدارند) عصر امروز هدف حمله آمریکا در تنگه قرار گرفتن ۱ جسد پیدا شد و ۳ نفر  دیگه فعلا تا این لحظه نگارش این خبر مفقود هستن
ترامپ در روز های اخیر چندین بار تاکیید کرد که نیروهای آمریکایی روزی بیش از ۲۰ قایق تندرو سپاه را منهدم میکنند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23125" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23124">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGn7o1jD3nh-ujalAkCgiF5YTN--02pBx_lDIWsUszSrnzlb8H55tMnlaxibtipDQ4NY5Y_ZGyOxK_iJSMJ3vZmrHOdN_xoPhVgbBifPRgHZn7J_ge0MsdKr8teUfzLqc2CDstl51LB4CQo1DKTpvKQ7VhLespbNvQrrXen-JQoe8EnSoJysptpu3TGyJ2xnR4sgOvk-OafO4X5xQly0b9r7bIaEfSeTGKlkQMOObXXVzQPcqE2Sh4tm10B8Ya2ypvg8QIELtjrT6rYdh2l-lbyiTPiuBZTZ8S5DCmah6Q4PhhhhC9skjhhMZzaUhc_cP5kJ53pPV9xRimIp2dULPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث: «نفت در حال عبور از تنگه هرمز است. کشورهای جهان که هیچ کمکی به ما نکرده‌اند، باید و خواهند داشت که پس از پایان این
درگیری فریبکارانه
، هزینه‌های آمریکا را جبران کنند. ما در این ماجرا بسیار بیشتر از آنکه برای خودمان اقدام کنیم، برای دیگران انجام می‌دهیم؛ همان‌طور که نسل‌هاست این کار را انجام داده‌ایم.»
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23124" target="_blank">📅 20:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23123">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ka_vnVW_rnQT4-R9AEVKXcaK6MUL889aHlNB9A7N90Ofnc8pkbMjYn8X4czhv2xTsFbNlBjVpgDS8vPwWddglrHh08h4ckj6feB0AQg0BMG4DFYHPdwVrh8dTu2GK3WjjcnXwlLJahyA9p1FAAX6tbxsonoJj3w7xb9ZvCnezeV4FUzqNul-D6JoR8tW1zCau1BHbhZRqpHVnysZZf4RX0sFRyySpjqAE8xufuFbzOA0D41_Z_p2MKznijIvv3OORJNpHM5aIZlXW4aHlr8O2datZH9z24o_wN54DZXcaCiHfwxXsI2PwKpZyBWb_74sn1nH2oLmwDJVN3mCrOI-JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث : «به‌تازگی گزارشی دریافت کرده‌ام که نشان می‌دهد ایالات متحده در حال تولید
پیشرفته‌ترین و ممتازترین تسلیحات
با نرخی بی‌سابقه در تاریخ کشور است. این تسلیحات هر روز به نیروهای ما در خاورمیانه و مناطق دیگر تحویل داده می‌شوند. کارخانه‌های صنایع دفاعی ما به‌صورت شبانه‌روزی فعالیت می‌کنند و هم‌زمان، به‌طور میانگین هر شرکت در حال ساخت ۴ تا ۵ کارخانه بزرگ و کاملاً جدید است. تمرکز اصلی این تولیدات بر
سامانه‌های پاتریوت، سامانه‌های تاد (THAAD)، موشک‌های تاماهاوک و دیگر سامانه‌های موشکی استاندارد
است؛ تسلیحاتی که همین حالا نیز تعداد زیادی از آنها را در اختیار داریم.»
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23123" target="_blank">📅 20:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23122">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5WUVqHwWpAGpljoZoynn4dQXCbK8LqYNhC0HDb-GiJ5xaipRkHWqwkZQhJm7xIyOpRByeimfjgy2Sn3oCK7urgxA4qMNFY997p85cmL_rOoKCQjuMCIhhPTOLiA9KMOXENgP_ycuR6hD2onko7H967oS6qchshFbZNEL8hKaGr2l9RNh9ty6ovKJIIQ7iH1Uh3CAQPX6JT37O26_BT0Zy4FBHdzboBVtYgcdUVxkSmCOyGkuDQYYGuYYtq2VnjAHBQpRkel-yEh4B9ONgroZq-dBh2ymkOicipTxD3_xyIZo52qV4pFR7Rt_JOguqDzAwcyay3D_JmWnX4FXhT5KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند هواپیمای E-11A متعلق به سیستم‌های هشدار اولیه و ارتباطی، از پایگاه الامیر سلطان به سمت عراق در حرکت است. همزمان، یک فروند هواپیمای P-8A برای عملیات شناسایی دریایی در حال پرواز بر فراز خلیج عمان است. همچنین، سه فروند هواپیمای تانکر در حال سوخت‌رسانی هوایی در آسمان امارات و خلیج عمان هستند. علاوه بر این، یک فروند هواپیمای MQ-4C در حال انجام مأموریت‌های شناسایی و نظارتی بر فراز خلیج فارس است.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23122" target="_blank">📅 19:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23121">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnqBCbIF-k92lgSqVAs_rkC_pZxY4GXSY2fBfkfb-FNOjZFKQ54zzFDcZWKxmgUddRQ33eKLN6TuKr3ziPapLiD_PAphLitinErqIgLEs4yPudvPiml0tlD1eY6oq_2zQNFcuNDU4nWvkAQ-CUFqgDG_DaFMQd5Zr3P0kiuFBypSWPd345Cq5HC0QlfZhOGNETRAU5nBMHsZGOKhrgvSz4FtgvQmdC1x1Q_T5Pg5dTB24P7TOT2VCSNIPuaKlnZAh6nrGXBzwFbJ7mCFeaVqR12IUV-XARlXQ0WnPhAdVBOiMaXHXyLQ6Clb6QGrWCAZ6D0o3GclnFzCNHyTaVilNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقت یاب اتاق جنگ : این عکس امروز توسط ادمین های زرد تلگرام با عنوان جعلی تصویر ماهواره‌ای سنتکام از قایقهای تندروی سپاه منتشر شده بود.
این در اصل تصاویر ماهواره‌ای گوگل ارث مربوط به ۱۸ فروردین ۱۴۰۵، یک روز پیش از آتش‌بس اولیه جنگ ۲۰۲۶ ایران است، دو فروند قایق تندرو را نشان می‌دهد که به‌صورت نسبی میان درختان در جزیره خارک پنهان شده‌اند. این شناورها احتمالاً متعلق به نیروی دریایی سپاه پاسداران هستند.
لوکیشن : 29.261371, 50.318697
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23121" target="_blank">📅 19:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23120">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بعد از این خبر نفت رو به پایین شد هم اکنون ۱۰۸$  @WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23120" target="_blank">📅 19:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23119">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا، اسکات بسنت: وزارت خزانه‌داری عملیات «طرد اقتصادی» را آغاز کرده است تا تمام شریان‌های مالی حکومت ایران و تسهیل‌کنندگان آن را قطع کند. به همین دلیل، من فراخوان جدیدی از افشاگران منتشر کردم تا اطلاعات خود را درباره افرادی که به اقدامات تروریستی ایران کمک می‌کنند، ارائه دهند. از هر فردی در سراسر جهان که درباره این شریان‌های مالی اطلاعاتی دارد: این فرصت شماست. اگر اطلاعات قابل‌اقدام و مفیدی برای وزارت خزانه‌داری دارید، ممکن است واجد شرایط دریافت پاداش باشید؛ مهم نیست کجا زندگی می‌کنید یا چه کسی حقوق شما را پرداخت می‌کند. اگر چیزی دیدید، گزارش دهید.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23119" target="_blank">📅 19:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23118">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsPyx-KvdXEDwLqZFvolOhNDweo1d4RfVZOKzXAJdD_3YzVxkKGmVC7FFWjnoG4rhXsndg30xA5n3XVp0lk-2b1VBKDcuLAMFm3-a56wkhlYBEEbJ2zbapdFWRS4lkLtKsEIIJeBPiOZWujNsMa-hK-WzYE7qNq_6YERX7efxFqO79-kJHLXPSa7SnkR98VBHHxr7CZK-d_X964WuTZeGxnEutLfiYpVlCN43G284PBf61JU34iIxzKeQeUQ_eTFsj9PhcfShQm7fAUP1Q61tkiBTGSnmXT2-I9lTmQdbZZ4UU_ZI5HhpBNwCNtvyRdgDAvyiGjbOqFgLyG3tBkRUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: کشور در حال فروپاشی ایران می‌خواهد
سریع و به‌شدت
به توافق برسد. من تعیین خواهم کرد که آیا ایالات متحده آمریکا تصمیم به ورود به مذاکرات خواهد گرفت یا نه؛ مفهومی که ما نسبت به آن
روی گشوده داریم
. از توجه شما به این موضوع سپاسگزارم!
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23118" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23117">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ در‌تروث : اوکراین و روسیه موافقت کردند حمله به زیرساخت‌های یکدیگر را متوقف کنند ، افزایش قیمت گازوئیل بیشتر ناشی از جنگ روسیه و اوکراین است نه ایران.‌‌ @WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23117" target="_blank">📅 19:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23116">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4424213714.mp4?token=YAbLDa1kOk5vnW4wA4r0xpD_ZuOQ-kWOFp4o0vlEYXx0xjGLo3fBEXe655F-h3JMMyIlqCy95ZG3zI7DJBo01UyMeMkVezOeD0XJpEyCpAbPW2pUes_lwvYnizRgF0Wiq41yewXGMJ-PJCdUUgJ1bcbZm6MjS01ULJLPlwgbU1aW6_qcnGP9f-47ZXOj2C5U0d8cPmUShQSU2G3DqJAWNeaFBZguklfqP874YdGjfGUgJESTuBI-p9y5qrIFQR8f11vxYmapY9SbwB7J5dWp8LuEYLySxzaxer4h2SpWs1Hjs5HhB_dc_UKda3twKoiaDWcHI6WFRzmy4crNvKwtfSSuC40czugVt9qaWlbjE0bNxbDPgxHiz6gC48PSXx_2rRCdXFvtXdb-0izW-l3ojgg_3fCNIoExCOKJQ6s-0eJaZCl_deG1nRJW8AcggxeC2LPpuvLT5vfRQx0MbXDNH_cW4aGfoNBEzXzyl3osKDL2GF4YTj5znNcB32FFgN068evPZ6JVtSuSL1x-q8IIiB98pHXXJNCPTjmOloBkw2t8Ujx2yvjXp_zZ9OnFbfh6yWfCousCEQp_Ke4ksaWorxNPd3GFrX4QZlmkAfsLxsXDDEF_EPthIdfIq_6cQ3DgQqC_LVR0Z6qRfR0av7t0aI7bYxlXSFHTW4AZkVvn4X8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4424213714.mp4?token=YAbLDa1kOk5vnW4wA4r0xpD_ZuOQ-kWOFp4o0vlEYXx0xjGLo3fBEXe655F-h3JMMyIlqCy95ZG3zI7DJBo01UyMeMkVezOeD0XJpEyCpAbPW2pUes_lwvYnizRgF0Wiq41yewXGMJ-PJCdUUgJ1bcbZm6MjS01ULJLPlwgbU1aW6_qcnGP9f-47ZXOj2C5U0d8cPmUShQSU2G3DqJAWNeaFBZguklfqP874YdGjfGUgJESTuBI-p9y5qrIFQR8f11vxYmapY9SbwB7J5dWp8LuEYLySxzaxer4h2SpWs1Hjs5HhB_dc_UKda3twKoiaDWcHI6WFRzmy4crNvKwtfSSuC40czugVt9qaWlbjE0bNxbDPgxHiz6gC48PSXx_2rRCdXFvtXdb-0izW-l3ojgg_3fCNIoExCOKJQ6s-0eJaZCl_deG1nRJW8AcggxeC2LPpuvLT5vfRQx0MbXDNH_cW4aGfoNBEzXzyl3osKDL2GF4YTj5znNcB32FFgN068evPZ6JVtSuSL1x-q8IIiB98pHXXJNCPTjmOloBkw2t8Ujx2yvjXp_zZ9OnFbfh6yWfCousCEQp_Ke4ksaWorxNPd3GFrX4QZlmkAfsLxsXDDEF_EPthIdfIq_6cQ3DgQqC_LVR0Z6qRfR0av7t0aI7bYxlXSFHTW4AZkVvn4X8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: سیاست ما روشن است: ما به تخریب زیرساخت‌های تروریستی در «منطقه امنیتی» در لبنان ادامه خواهیم داد و به رفع هرگونه تهدید علیه دولت اسرائیل ادامه خواهیم داد. به دشمنانم می‌گویم: اگر تاکنون درس را نیاموخته‌اید و تصمیم بگیرید که دوباره به ما حمله کنید، ضربه‌های سنگین‌تری را متحمل خواهید شد. کارهای بیشتری برای تکمیل باقی مانده است و با کمک خداوند آن را به پایان خواهیم رساند.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23116" target="_blank">📅 18:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23115">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gebkAeKgHktZZIGcFsXFHijnjz9qt5GGkPMYIcjXJJppaH6ctOqr-qnG70pJ9eJ3IabdjqzAWyMhYyg7FUYuSAFlMW27RG7YPEFjHVA8lublBdDZ2x417ZHy1cQGv1j_nE7o147YJjU3ZlZ_9gm5M2_wdcr9v8GKejYS6FlqoA4_VtmMzgt_XGuhvk-X1z44ID9rd9dtu9kmS-ujAoq7rkkFc0smruNf-Dw2TaAMRWPofhJJMutwkv1N3Hlv7VPSALBdbRDHJKFIe1mGEIWKyzVsxCsMhgROZIKmt73f-7IV6kq3yp_eTpJ4zXsg882yhZYyJ_Rw4Z3AKXotgM8vKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ
در‌تروث
: اوکراین و روسیه موافقت کردند حمله به زیرساخت‌های یکدیگر را متوقف کنند
، افزایش قیمت گازوئیل بیشتر ناشی از جنگ روسیه و اوکراین است نه ایران.‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23115" target="_blank">📅 18:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23114">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7da56100a.mp4?token=fG5nf8OANfmUnS5wZJu-OHoTyMo7EC0VY-bJh2Abtyza_TvcEG80tddIs-oIlLatPM74bYe5axHSeAxEq5gisqVOgyw3ZedqPJAGIRkdO9o7N7n6txBwf4tG3zKGXDUe8w4s3LjGg8c9qNJxG_SMzl7expL9b1XHKZV7XFAU8LWY4ikrRY7tIZP_BdlO8CFfA50J3PpuQS_JX6dtikmJgZsJTPwVJ1TigmaKC4TvLgM2XCJE0Mc26l7TWKs1_dgDf1KHp5u63jVmfi7Io3GSYIErM_VhGosHVe9lXAzLG4KvTsSOvpe87Xn8m9ROPq4MUJL2Y8rvo7RPOV_aBVnQsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7da56100a.mp4?token=fG5nf8OANfmUnS5wZJu-OHoTyMo7EC0VY-bJh2Abtyza_TvcEG80tddIs-oIlLatPM74bYe5axHSeAxEq5gisqVOgyw3ZedqPJAGIRkdO9o7N7n6txBwf4tG3zKGXDUe8w4s3LjGg8c9qNJxG_SMzl7expL9b1XHKZV7XFAU8LWY4ikrRY7tIZP_BdlO8CFfA50J3PpuQS_JX6dtikmJgZsJTPwVJ1TigmaKC4TvLgM2XCJE0Mc26l7TWKs1_dgDf1KHp5u63jVmfi7Io3GSYIErM_VhGosHVe9lXAzLG4KvTsSOvpe87Xn8m9ROPq4MUJL2Y8rvo7RPOV_aBVnQsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون آتشسوزی در بازار متل‌قو
@WarRoom
یاشار : حتما به بی‌بی مشروب تقل دادن شاکی شد</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23114" target="_blank">📅 18:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23113">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گزارش ۲ انفجار در جاسک و چابهار
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23113" target="_blank">📅 18:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23112">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzusnyWnu40XTJ4ej5n9hvczQLhKUMrDQoEsb-Ola5d9qfXIRSUAA7nvKt8IvjeWFxrEfg5tAcumL8Pyl8cMjZeB7jdozdKd_ne09A8W-m95pLAxymOnJmAr6FyGJs2G82UsWOg0DSdHohZM63xQRhzgVoA5PYLBDF3D_8uwkczjyQPVFkQteQzzL3jxgJarSsKBI3rUDHR9I-JiSQGLU5ppFO_bIZ1Nk9KBZ7hHHkiZ4-FH_wySNFRriXhl-UFTqMuK181NQSUyqKOpz4MeenO936kJ6wNTToWa-MxBS8SmIpGnch5FKHk-xLv9_3MEEC7yuDCY1lH2rL0FqnuLtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: تنها چیزی که هوش مصنوعی به آن برای کنترل یا ایجاد «چارچوب‌های نظارتی» نیاز دارد، یک رئیس‌جمهور
قدرتمند و باهوش (با ضریب هوشی بالا!)
است، و ایالات متحده آمریکا چنین رئیس‌جمهوری را آن هم به وفور دارد! دولت ترامپ جلوی افراد فعال در حوزه هوش مصنوعی را که کارهای بد یا بالقوه بد انجام می‌دادند گرفته است؛ افرادی مانند داریو (آمودی، مدیرعامل آنتروپیک) که حالا وانمود می‌کند یک «فرشته کوچک و بی‌عیب‌ونقص» است؛ و ما به این کار ادامه خواهیم داد! ما همین حالا هم
قدرت‌های گسترده کیفری و نظارتی
بر این شرکت‌ها داریم! یک توطئه
بیمارگونه
علیه هوش مصنوعی و مراکز داده در جریان است و تنها کسی که از آن خوشحال است، چین است.
هرکس هوش مصنوعی را ببرد، برنده خواهد شد!
ما از چین و همه دیگران جلوتر هستیم و به این روند ادامه خواهیم داد. نظریه‌پردازان توطئه، خیانت‌پیشگان، خائنان و افشاگران،
مراقب باشید!
از توجه شما به این موضوع سپاسگزارم!
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23112" target="_blank">📅 18:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23111">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7-cU7QPyHq0auN54r7qIADW0dwX4Nbf8qrQnL8c6A_yrVRUGdI8FAhr44aFOPCq6T-XPfQh1UF2Zc3XhfHf4MIcQP7kvLDl48pDy4_QPW_GSrGk0A8wLTeOhYj8MoMI3jVG1Tmi65sVTZ7zxQq2WB49sdwSh94kjHhLHdt-oqcxL-qA3H-Uv3ouR5lTkn26KiJT3Xm6zNH3r9XjKErAqwmggKzT55Y6GA1ypKZxx-SrDrV96KwnvDKhPBwsUgoF-1VyPmhxJMdiu01BQf-UcLXdxHnFVYRsh91v52RXYc1uBpnKuLFgZco_ta5D7M-VFZY7XQdq_8tbmIRVThyqJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت برنت رسیده ۱۰۹.۲۰$ با نمودار هفته های اوج جنگ برابرشده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23111" target="_blank">📅 18:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23110">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تنگه دعوا شد ، ۵ صدای شلیک/انفجار
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23110" target="_blank">📅 17:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23109">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وزارت خارجه چین روز دوشنبه ۲۳ شهریور گزارش‌ها درباره ارائه تصاویر ماهواره‌ای به جمهوری اسلامی پیش از حمله موشکی ۱۷ شهریور به پایگاه موفق‌السلطی در اردن را «بی‌اساس» خواند و رد کرد. مقام‌های آمریکایی گزارش داده بودند که جمهوری اسلامی پیش از این حمله، تصاویر…</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23109" target="_blank">📅 17:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23108">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">لحظاتی پیش دفتر نتانیاهو اعلام کرد: نتانیاهو هفته آینده به آمریکا سفر خواهد کرد @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23108" target="_blank">📅 17:11 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
