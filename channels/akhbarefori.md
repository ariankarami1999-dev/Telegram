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
<img src="https://cdn4.telesco.pe/file/sUmA3nd-B89jWW6HDwhHZo0ihHyuxftv5_fAebwwIAJvMmSCMjgr3nm42K229HPhRQX9QImlxeBf8fIW3OPmhm9bmcnpuw3sunaf7ewvfBLo19oonOvDpMyHuidhRw0CywTbwZ0xgO-cIjeOjJCfGnRVNev_k1AJWm2GE2teaiAEXDpsf9IKvGIZgNiVrSvFqBgfrn5G1B99mi-u6ZoImfT-vcrof1t-k1yslbapWGHkQA1WR3enu9II8tyP7T4rNL3cBlVDwLu6ytZ_anZmWTjqqM7QFhD5xJ8YF2d689jcaU8P_Uin06lMm-Mt87FzwvyrJYeK5TYY6M9ZoL3R-Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.98M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 01:50:47</div>
<hr>

<div class="tg-post" id="msg-692160">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
رد درخواست رفع محاصره ایران از سوی آمریکا
منبع آمریکایی در نشست با هیئت ایرانی در نیویورک:
🔹
آمریکا درخواست ایران برای رفع محاصره را نپذیرفت. فرصت‌های دست‌یابی به توافق محدود است. اختلافات و موانع بزرگی همچنان میان دو طرف وجود دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/692160" target="_blank">📅 01:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692158">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTeO6R3vy3D47rC0CAMlNPvB9ntPQJxmwJOly_OAIRdUJAKuv86AinUfa5yAOpzip8xI89xcMrQuDe_HJEDhsHA8vyavuGgDxDfVhf93L02BXhJcP2zx4eh6ZLC3Qg3S78HbzBD80z1hZtzOj2ZdOseMfZT1XsDtuwhQ6FrSzYJ7DxctBiAn_yQLobPQi4tCa16k5WIferlcKTeDtsZg2X7j_VgOO0BTRLz0njLH-_A_NUiv4d_VYV861kuPPG30xrqapjdoL1a-3asnC6If3t1_pv4omTTwFyqOgeS3VePivPf0wpRwqwBDO8Ruq9mLjoq4O-yH4VLHw2fPkgLccA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هواپیمای حامل رئیس‌جمهور و هیأت همراه برای شرکت در مجمع عمومی سازمان ملل وارد خاک آمریکا شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/akhbarefori/692158" target="_blank">📅 01:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692157">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
دقایقی قبل صدای انفجار در حوالی جزیره قشم به گوش رسید. به نظر می رسد صدا از سمت دریا بوده و اصابتی در داخل خاک جزیره قشم صورت نگرفته/ ایرنا
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/akhbarefori/692157" target="_blank">📅 01:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692156">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c26154995.mp4?token=PA2tPFMf9oNE-w4MPOajFQv7TuwBmVYKNRSMzKIpO6XG-1-OWM0qmYLhmDZW_opQfZP4c0bTbaY3hnS2izcmXGX2v-LMIip-2KIFL8ss6Fiv8KSVo_nYPEo4Uo6yuhmz3kyBoFjQE64ras0vdFsbTgVdus-QXWYw6rHH_4Yl6SELv7gVkeIlbr0I_GQlgZJm-eQ8CCeC4ZPKdkw2BrdK-cI4Vmc6-U39d1qVDZZVKXPuNpCKGjLLXs6NGaLiA9sRn9xYs3hN5yZ_Fmv94cRlGXz1_15SEBXXWa6ftMI5XZdlX1ZYfwV1ccnXZGCrcVmrpu20U9otHvvmiLP0KQCxbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c26154995.mp4?token=PA2tPFMf9oNE-w4MPOajFQv7TuwBmVYKNRSMzKIpO6XG-1-OWM0qmYLhmDZW_opQfZP4c0bTbaY3hnS2izcmXGX2v-LMIip-2KIFL8ss6Fiv8KSVo_nYPEo4Uo6yuhmz3kyBoFjQE64ras0vdFsbTgVdus-QXWYw6rHH_4Yl6SELv7gVkeIlbr0I_GQlgZJm-eQ8CCeC4ZPKdkw2BrdK-cI4Vmc6-U39d1qVDZZVKXPuNpCKGjLLXs6NGaLiA9sRn9xYs3hN5yZ_Fmv94cRlGXz1_15SEBXXWa6ftMI5XZdlX1ZYfwV1ccnXZGCrcVmrpu20U9otHvvmiLP0KQCxbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔧
هرچی برای تعمیرات لازم داری، یکجا داشته باش!
🛠
آچار بکس
۴۶ عددی مدل Phunda
💪
مجموعه کامل و کاربردی برای تعمیرات و کارهای فنی
🏠
مناسب خانه، خودرو، کارگاه و استفاده روزمره
📦
۴۶ تکه در یک ست جمع‌وجور و کاربردی
🔥
قیمت ویژه: فقط 1,498,000تومان!
📌
دیگه برای هر تعمیر کوچیک دنبال آچار نگرد؛ این ست رو دم دستت داشته باش!
خرید از سایت
👇
https://memarket24.ir/product/fast/27006/180124/</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/692156" target="_blank">📅 00:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692155">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
‌هواپیمای حامل رئیس‌جمهور حدود ساعت ۱۷ به وقت نیویورک و ۳۰ دقیقه بامداد چهارشنبه به‌ وقت تهران وارد فرودگاه بین‌المللی جان‌اف‌کندی می‌شود
🔹
این پرواز عصر امروز پس از سوخت‌گیری و توقف کوتاه در الجزایر به‌ سمت شرق آمریکا حرکت کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/692155" target="_blank">📅 00:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692154">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رشیدی‌کوچی، نماینده سابق مجلس: صداوسیما را از یک رسانه معتبر به رسانه‌ای بی‌اعتماد تبدیل کردیم
جلال رشیدی کوچی، نماینده سابق مجلس:
🔹
صداوسیما را از محل بزرگی که می‌توانست برای مردم محل اعتبار و اعتماد باشد از دست دادیم.
🔹
ون گشت ارشاد در خیابان نبر که زن و بچه مردم را به زور و با استرس داخل ون کنی؛ اینگونه کسی با حجاب نمی‌شود؛ حرکتی بزنید که مردم امیدوار شوند‌.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/692154" target="_blank">📅 00:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692153">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01252d1672.mp4?token=ZJ9zclHJ5lVbv-Ys6rwd243zQadm1DHukq-O4BPTwk9avC-F1A40HyMw3OVWWmHTI_s9-SDRIaf1Kks_Hkv0_NVvE8IA4-i-VJPpC83uEHB__uQIpYfkvcNjRxM4nqXAwPVuQYYbaxb9dwJnhjsmeUxIcHfSpRx1QBjvnOQgPvqvsl4uyWKeCVia9DeAD2iLCuyaKJZAV4A0e9r4_44XHleSxcmJX0Nanv1hgrpA1eYuDG7JZ8WGUbixTJkGh8lcOogvCRUgTsE5xfXccCd2TpWEnlJ3Nr-bp6kbVC2deQu9QRevtQb2dmSn8aUIhVMyWJfC7h5UBD6Qtb03JR-WEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01252d1672.mp4?token=ZJ9zclHJ5lVbv-Ys6rwd243zQadm1DHukq-O4BPTwk9avC-F1A40HyMw3OVWWmHTI_s9-SDRIaf1Kks_Hkv0_NVvE8IA4-i-VJPpC83uEHB__uQIpYfkvcNjRxM4nqXAwPVuQYYbaxb9dwJnhjsmeUxIcHfSpRx1QBjvnOQgPvqvsl4uyWKeCVia9DeAD2iLCuyaKJZAV4A0e9r4_44XHleSxcmJX0Nanv1hgrpA1eYuDG7JZ8WGUbixTJkGh8lcOogvCRUgTsE5xfXccCd2TpWEnlJ3Nr-bp6kbVC2deQu9QRevtQb2dmSn8aUIhVMyWJfC7h5UBD6Qtb03JR-WEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشف یک مورد مشکوک
🔹
پس از پیدا شدن یک کیف مشکوک در نزدیکی مقر سازمان، تیم خنثی‌سازی بمب آمریکا اقدام به مسدود کردن خیابان کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/692153" target="_blank">📅 00:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692152">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff7ba5922.mp4?token=lcSH23rHm2evZxcZ-UiBmr1V5ChpYgfr-bZwbWNcMdeoMkDpNKT96SzkBY-9B-3P5X6tVhdJVTV6RPC5JixXOO6_clZd8aC__0hj7FnrarJJgU0UtxuNCdgJarF4c-q8ESDtnYYdoOsHAgej-QRPMNGER71HngXnScYRn8el9pqu7MORZkWRIs5oGiiXV2gfVVxVJ6fL0JKDAOMLssbq_4HQQlzzr16QLWavp2Db8MnRnZb42dL2UWqDhvnOKNE0DYJUGD0-rzff2i0aFdUvk8-xAXe0hg9rPIpvTwEYySWXStz4DCg0BuEjsMbCGdzCccPXy6wQUkhR9MFnGspv_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff7ba5922.mp4?token=lcSH23rHm2evZxcZ-UiBmr1V5ChpYgfr-bZwbWNcMdeoMkDpNKT96SzkBY-9B-3P5X6tVhdJVTV6RPC5JixXOO6_clZd8aC__0hj7FnrarJJgU0UtxuNCdgJarF4c-q8ESDtnYYdoOsHAgej-QRPMNGER71HngXnScYRn8el9pqu7MORZkWRIs5oGiiXV2gfVVxVJ6fL0JKDAOMLssbq_4HQQlzzr16QLWavp2Db8MnRnZb42dL2UWqDhvnOKNE0DYJUGD0-rzff2i0aFdUvk8-xAXe0hg9rPIpvTwEYySWXStz4DCg0BuEjsMbCGdzCccPXy6wQUkhR9MFnGspv_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرایند شگفت‌انگیز سیناپتوژنز؛ اتفافی است که در لحظه یادگیری در مغز رخ می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/692152" target="_blank">📅 00:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692151">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
سرلشکر صفوی: باز شدن تنگه هرمز در مقابل پذیرش شروط ایران است؛آمریکایی‌ها مانع توافق با عمان در مورد تنگه هرمز هستند
🔹
نه‌تنها تنگه هرمز به حالت قبل برنمی‌گردد بلکه باب‌المندب هم به قبل برنمی‌گردد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/692151" target="_blank">📅 00:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692150">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ترکیه: پرواز ایرلاین‌های ایرانی به ترکیه همچنان برقرار است؛ محدودیت اعمال‌ شده برای ماهان به سایر شرکت‌های هواپیمایی تعمیم پیدا نکرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/692150" target="_blank">📅 00:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692149">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkneNiMJ5jM6fQbawYkaHPjMAowmv6ClPD0Bs_gx2gBULODY1anPBZ_aWekJDKNSHTPmpQ_NPhrpBDVabUtHe9PT-oy8yVY8rgQ7VsPtyyci6faflmGOXkPb3yyCTZpDlAFY5YBe3qUM1A3_1cpauHRsvyi5uH7H0SEjTU8Cl_y3o7hjdtStCS1Rcop4NXBhkTW_qo7PhJMdbLPpb-QbkncYCQxyKo_AIFAbtE7FKdtm7uZLQqj9N4ysAP_N4HzxTA88KEgW3Nu30y3itcXrEOxPPqrBYbp_fSgB3fZLvSA0cX3WU3_PwaiBmoT7w1fUJ-zMyvyZzhq2Ok6cx7HkwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/akhbarefori/692149" target="_blank">📅 00:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692147">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb8e6abc3b.mp4?token=G2Mh_Yb9mGz937GjhRNrO1e_8d6gPUCmlrfTt5xsFGMpM22I2ifqSXQIZw_qZXj_8DLjL-1C6AzucYKyvluPGH53Ikrdy261WPuYVWPAWVRAk2GGz6gGhZzEjAToZiIcqydAaRUNNl_sz2VbIk01wDFJEzuiCKWTA85gJj4uf5XrSl3wMcumDKxNyybanFlx-4aUhNVYbemKdYStBzoZqJvEILJpgjiMQrTrjsGy2TsWYLKS7QCIzD65Vz4H_cBXHUEeqQSbKn43tUwiruK8FhH4hlaP0laYQvWEIOukgcaWZxgRhaJ7t1AqUy-cNZbL2-jlq64J-MK5I_XNzRgdTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb8e6abc3b.mp4?token=G2Mh_Yb9mGz937GjhRNrO1e_8d6gPUCmlrfTt5xsFGMpM22I2ifqSXQIZw_qZXj_8DLjL-1C6AzucYKyvluPGH53Ikrdy261WPuYVWPAWVRAk2GGz6gGhZzEjAToZiIcqydAaRUNNl_sz2VbIk01wDFJEzuiCKWTA85gJj4uf5XrSl3wMcumDKxNyybanFlx-4aUhNVYbemKdYStBzoZqJvEILJpgjiMQrTrjsGy2TsWYLKS7QCIzD65Vz4H_cBXHUEeqQSbKn43tUwiruK8FhH4hlaP0laYQvWEIOukgcaWZxgRhaJ7t1AqUy-cNZbL2-jlq64J-MK5I_XNzRgdTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: ما به دنبال جایگزین برای حکومت ایران نیستیم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/692147" target="_blank">📅 23:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692146">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
جلال رشیدی کوچی، نماینده سابق مجلس: آقازاده‌ها به شرکت خارجی می‌گویند فاکتور را بالاتر بزن/ هزینه‌اش از جیب ملت پرداخت می‌شود
جلال رشیدی کوچی، نماینده سابق مجلس:
🔹
آقازاده‌ها از اسم پدرشان رشد می‌کنند. بیزنس‌های پدر را از طریق آقازاده‌ها پیش می‌برند برای همین از نظر مالی بزرگ می‌شوند.
🔹
آقازاده پول را از سایرین می‌گیرد و در سودش شریک می‌شود و می‌گوید پدرش امضا کند. مگر می‌شود پدرش نداند؟ خودش را به ندانستن می‌زند.
🔹
با بعضی از آقایان صاحب نفوذ برخورد داشتم. شک نکنید پشت پرده یک سری اتفاقات می‌افتد.
🔹
آقازاده از شرکت خارجی کالا را می‌خرند و می‌گویند فاکتور را بیشتر بنویس. در واقع، پای ملت فاکتور کرده است.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/692146" target="_blank">📅 23:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692145">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
حملات موشکی عربستان به شمال یمن
🔹
منابع یمنی گزارش دادند عربستان در این حملات، مناطق «مران وحیدان» و «الظاهر» در غرب استان صعده را هدف قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/692145" target="_blank">📅 23:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692143">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc9f35f8e.mp4?token=BIkDBFCkZjtRqWhL8LZhJd3UIrYRPtsHGWCf_zbQ1qgI1T-2JoGyWyrZodn3rUNU7Yew9Q2-snEfiVdUEALCZs2-QXLKfVCbbphpJzbdpA1x5vyG1dKVFFmH5Bg2eaiRMZxUks67ygT-HSiQ7qOzK3SCEZPxtSiUwIaavVYe_TdmjS4QR5qTDDIavvWqaRF5vhVdvRgGVxaRdTNde0TJGvWw-xyOQzcQM2G-rdwoqTJRI4wapKMGt908EH8VzOnZ6nG_6y0EtioMXV1wV0yoPO92sfyoq9Rwh8L2qBH02IsRvIdKXHdtSdzzya49OiJ6lu5dw9a8-MzIujS56L_WuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc9f35f8e.mp4?token=BIkDBFCkZjtRqWhL8LZhJd3UIrYRPtsHGWCf_zbQ1qgI1T-2JoGyWyrZodn3rUNU7Yew9Q2-snEfiVdUEALCZs2-QXLKfVCbbphpJzbdpA1x5vyG1dKVFFmH5Bg2eaiRMZxUks67ygT-HSiQ7qOzK3SCEZPxtSiUwIaavVYe_TdmjS4QR5qTDDIavvWqaRF5vhVdvRgGVxaRdTNde0TJGvWw-xyOQzcQM2G-rdwoqTJRI4wapKMGt908EH8VzOnZ6nG_6y0EtioMXV1wV0yoPO92sfyoq9Rwh8L2qBH02IsRvIdKXHdtSdzzya49OiJ6lu5dw9a8-MzIujS56L_WuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش اختصاصی شبکه ۳ از وضعیت مردم غزه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/692143" target="_blank">📅 23:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692142">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/197e752b37.mp4?token=MG6VKjGRuq_tg41BM0c1c_NoAZYqMUYLa5FDzvDm02yw-22MkuzcTlJEYLUKkWAUtEHkqpZaYlHg0hcpbE_laK1whC1EAy9OOc4e1qMPDc2ANQ2ApMYQvStWAdaUlp-7xrAU46_1VBVXGNGq1FUl0xA66R1El0fn86LbMNRfGPO92BkdBNtfadvzl8GqF2nBzfasYD_yNYyNc7-VtudmDrssU7lPriOgmO99giwIwwrRvlSPK7fqT-eBh-8UQIAw69-gWpf-DVMzhMNtxJmrRt5W5Acx7SIVtJbPEpqZfQ3GOugo5fD1loYDff0549NxYw9JpWQJKxGz0hdXLm06fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/197e752b37.mp4?token=MG6VKjGRuq_tg41BM0c1c_NoAZYqMUYLa5FDzvDm02yw-22MkuzcTlJEYLUKkWAUtEHkqpZaYlHg0hcpbE_laK1whC1EAy9OOc4e1qMPDc2ANQ2ApMYQvStWAdaUlp-7xrAU46_1VBVXGNGq1FUl0xA66R1El0fn86LbMNRfGPO92BkdBNtfadvzl8GqF2nBzfasYD_yNYyNc7-VtudmDrssU7lPriOgmO99giwIwwrRvlSPK7fqT-eBh-8UQIAw69-gWpf-DVMzhMNtxJmrRt5W5Acx7SIVtJbPEpqZfQ3GOugo5fD1loYDff0549NxYw9JpWQJKxGz0hdXLm06fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عامل ترور شهید کاک درویشی چگونه عملیات تروریستی را اجرا کرد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/692142" target="_blank">📅 23:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692141">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ادعای
لارنس نورمن، خبرنگار مشهور وال استریت ژورنال: امکان بازگشت به تفاهم‌نامه اسلام‌آباد وجود دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/692141" target="_blank">📅 23:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692140">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gy8wKfNgUsIi_Oka3JeAbl20-qk5d00lEczPlVY9mGLVcS3M3H7iY0DdtZ5-j3gY_TwjAioAInfrVwVaCFEvlhhjL7XbB3VR6BOoqIESF_ebXTHWzZsa0vHGWpcefxsFrFccFzMQLdv-PSU-ooMej31KWMLnyFb6Xvj2mMy-hp5ehgI00qwCeoBPpiOQrKUM0ElGqsfu1x4WeTyCz1C-IEsY21Bhbw0HMo5hMsyJSsUqDoiDZ2na0XeBuUWaYR_lMDsKNV-Si-Af78oVFUwdSxgLBils3lHUye7mvAdSzsTlQlaiGDTe5wyEVHSP0RBD7XYggfjWqkIdT6ltREwpvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسپری کلاژن‌ساز خانگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/692140" target="_blank">📅 23:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692139">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
قیمت گازوییل در بلژیک به بالاترین حد رسید
🔹
با اعلام وزارت اقتصاد بلژیک، قیمت گازوییل در این کشور با افزایش بیش از ۳ سنت، به ۲ یورو و ۵۰ سنت در هر لیتر رسید و رکورد تاریخی جدیدی ثبت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/692139" target="_blank">📅 23:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692138">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ادعای واشنگتن پست به نقل از مقامات آمریکایی: پایان جنگ با ايران، اولویت اصلی کاخ سفید است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/692138" target="_blank">📅 23:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692137">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پیشنهاد رشوه ۳۰۰ میلیاردی به رشیدی‌ کوچی؛ مصاحبه کن خودروهایم را بفروشم!
جلال رشیدی کوچی، نماینده سابق مجلس:
🔹
بنده خدایی یکبار اصرار کرد و سوار ماشینش شدم. گفت این پول( ۲۰۰ تا ۳۰۰ میلیارد تومان) را از من بگیر و مصاحبه‌ای کن تا بتوانم تعدادی از خودروهایی را که خریده‌ام، بفروشم.
🔹
این فرد حتی کیسه ورزشی حاوی یورو را به من نشان داد، اما قبول نکردم.
🔹
وقتی داشتم پیاده می‌شدم به من گفت که این پول را از من نگرفتی، اما همین را خرج رد صلاحیتت میکنم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/692137" target="_blank">📅 23:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692136">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ادعای خبرنگار الجزیره: فضای دیدار ایران و آمریکا مثبت گزارش شده و یکی از میانجی‌ها نقش مهمی در این روند دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/692136" target="_blank">📅 23:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692135">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gN5OtQAKcgeFB21JXzbU9bcH_Xy6U_V2y3BjfKRVWv8Mptx2-0vpq9uUV4mY2Dc6_HeWX0As9IvpkIje86HJGKN7xlY8ZwJERuQEH3AwDmnK-MBDLVhrbofS5YBliZ8ar4wsdur710rFYx1_8xRqAxlqgtjz7uLsC65ikHsPTVcjuqgntjMJyY_Zj5R_TgDBi_TrPkt4Sq4NNfWD_NglRuP72eOIQbHTsLUBfV6u3EvzGX_vk7fphCzd-Fos-kC5_hFXf4EwFi13Bf2OBOSDVVkttXdlRO2WHl8aHSk5hl2wpTCk7olg6y4rdad5KxcHBY3_bGhBZVe4pBVFhIN1jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تتر ارزان شد
🔹
بعد از تایید دیدار عراقچی و ویتکاف توسط صداوسیما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/692135" target="_blank">📅 23:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692134">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee8d463a5.mp4?token=hGi8urZM6pL3Ycokbl2vt-OJh8c3Yhok_Po141__4m6QSZ4dqQEy5UU4WO7wuPmGSYazUzaCaFLrgtRWaGeGE11N3ohIQfNXEzo2iJvbUk7Q4Msixv9aATYzb9uIno012vZSUvgfdcyYb-qqF1zW7RY5HdV4yWsg0KSiYlxJ-rVhtOcLfD0OSX-oIhDtmdX99TXvIXILs9dOhBYk8v1E1p5O6D6iBmznGQKAdgQfGXZhCEo_8MmY8TE0uvxplrhjM92LMTpLoRc6R2pDMXf8-rT0IVJfuyaorogyutMp76Li9Dnt3cu05F5qkX0tJakL1TucsGtT8qdajFo9eG5GTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee8d463a5.mp4?token=hGi8urZM6pL3Ycokbl2vt-OJh8c3Yhok_Po141__4m6QSZ4dqQEy5UU4WO7wuPmGSYazUzaCaFLrgtRWaGeGE11N3ohIQfNXEzo2iJvbUk7Q4Msixv9aATYzb9uIno012vZSUvgfdcyYb-qqF1zW7RY5HdV4yWsg0KSiYlxJ-rVhtOcLfD0OSX-oIhDtmdX99TXvIXILs9dOhBYk8v1E1p5O6D6iBmznGQKAdgQfGXZhCEo_8MmY8TE0uvxplrhjM92LMTpLoRc6R2pDMXf8-rT0IVJfuyaorogyutMp76Li9Dnt3cu05F5qkX0tJakL1TucsGtT8qdajFo9eG5GTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستیار رئیس بانک مرکزی در امور ارزی: حتی وقتی خودروی لوکس با ارز ایرانیان خارج از کشور وارد می‌شود، بر بازار ارز داخلی اثر منفی می‌گذارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/692134" target="_blank">📅 23:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692133">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔹
خبر و بیشتر از خبر را هر روز و هر شب در وبسایت خبرفوری کلیک کنید
🔹
🔹
یک احتمال شوکه کننده: ترامپ و پزشکیان در نیویورک دیدار می‌کنند؟
👇
khabarfoori.com/fa/tiny/news-3247135
🔹
علت توقف پزشکیان در الجزایر حین عزیمت به نیویورک چه بود؟
👇
khabarfoori.com/fa/tiny/news-3247214
🔹
واردات خودروهای کارکرده آزاد شد؛ آیا قیمت خودرو پایین می‌آید؟ | چه خودروهایی امکان ورود دارند؟
👇
khabarfoori.com/fa/tiny/news-3247143
🔹
افشای هویت همسر علی ضیا
👇
khabarfoori.com/fa/tiny/news-3247124
🔹
افزایش کالابرگ برای کم‌درآمدها | دولت پولش را از کجا می‌آورد؟ | با ۳۰۰ هزار تومان قدرت خرید چقدر دوام می‌آورد؟
👇
khabarfoori.com/fa/tiny/news-3247101
🔹
خبرهای منتخب را لحظه به لحظه اینجا دنبال کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/692133" target="_blank">📅 23:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692132">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
گلایه نماینده مجلس از عملکرد ضعیف سازمان محیط زیست
عبدالغفور امان‌زاده، عضو کمیسیون کشاورزی مجلس در
#گفتگو
با خبرفوری:
🔹
درباره حمله به نفتکش‌ها و نشت مواد نفتی در دریا، در شرایط جنگی انتظار اقدام مؤثری از سوی سازمان محیط زیست وجود ندارد، چراکه این سازمان حتی در شرایط عادی نیز در حوزه محیط زیست عملکرد ضعیفی داشته است.
🔹
آبزیان و محیط زیست دریایی پیش از جنگ نیز به دلیل بی‌توجهی به اصول زیست‌محیطی آسیب دیده‌اند و در شرایط جنگی امیدی به جبران این خسارت‌ها نیست.
🔹
سازمان محیط زیست به‌عنوان نهاد مسئول قدرت لازم را دارد اما عملکرد ضعیفی داشته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/692132" target="_blank">📅 23:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692131">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
واکنش ستاد کل‌ نیروهای مسلح و قرارگاه مرکزی خاتم‌الانبیاء به لفاظی‌ ترامپ
🔹
اظهارات خصمانه و تهدیدهای مکرر رئیس‌جمهور آمریکا علیه ایران که با سوءاستفاده از تریبون سازمان ملل متحد جهت موجه جلوه دادن تجاوز، ایجاد ناامنی و راهزنی در جهان همراه شده است، پیش از آنکه متکی بر واقعیت‌های میدانی باشد، صرفاً ابزاری برای تبلیغات داخلی است. این‌گونه سخنان، نشان‌دهنده بن‌بست راهبردی آمریکا در تجاوز علیه ملت ایران است.
🔹
ان‌شاالله رئیس‌جمهور محترم جمهوری اسلامی ایران، پیام ملت شجاع و نیروهای مسلح قهرمان و اقتدار ایران قوی و شکست‌ناپذیر را در مجمع سازمان ملل متحد به گوش جهانیان خواهند رساند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/692131" target="_blank">📅 23:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692130">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca005a23e0.mp4?token=EKBCIAw6_XLbcoIh1r7UzrJgnwndJhMKXHeIUZAnMxDtyKYxTuQ4rN_y3yfPnKL3ef3HKd8WeDFh4v7V-P680Aucc-94D5Omsr0IYD3D4q4a8P8xOtRzeJR-UAW0WnWXSZq5CEFX287CgRnnQrDJBM6mV6H0OS6k3VOf95nLYJwaz68ChwTT9K0upDlRqj1dDG44FNy_1LT3mJJPdYE_y_wveefv5C3CdU4O1FpQrSozPbhW3B9HzqCoUa8eKr3K1h4EMLCiHW0ga-Cgepumih4EXknyq7KfLhfd8-Wv8yxFaQ1QLMp0s4m_iomPqKILkp3JS8vz9CEnW3ToZkzRJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca005a23e0.mp4?token=EKBCIAw6_XLbcoIh1r7UzrJgnwndJhMKXHeIUZAnMxDtyKYxTuQ4rN_y3yfPnKL3ef3HKd8WeDFh4v7V-P680Aucc-94D5Omsr0IYD3D4q4a8P8xOtRzeJR-UAW0WnWXSZq5CEFX287CgRnnQrDJBM6mV6H0OS6k3VOf95nLYJwaz68ChwTT9K0upDlRqj1dDG44FNy_1LT3mJJPdYE_y_wveefv5C3CdU4O1FpQrSozPbhW3B9HzqCoUa8eKr3K1h4EMLCiHW0ga-Cgepumih4EXknyq7KfLhfd8-Wv8yxFaQ1QLMp0s4m_iomPqKILkp3JS8vz9CEnW3ToZkzRJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی از هر قشر و دیاری برای وطن به میدان می‌آیی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/692130" target="_blank">📅 23:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692128">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5526a3ee7.mp4?token=syJi0A3fUQ0RCZiEZU1PBzsEexBrs_XC6L41lO0pZbIFBfXQ_wffIHqdN8PO38ntLFLpGP6JNCjJCYlK_bx2oU1rjk_AKfwiDEas1Ej_jk1v_-9FJbzVpchs7Tiptfzu-3MfwVsas02vfROWEhWiCMpcHB86kz5CpkM1Kc1jXhoKAg-MW4RTDTBWwlMon-m6f4N9WeobpSK00mjE79-rp4hSfC353I0sU_VwhAoIpLfc7NK4n97ZQ-V6bMg6SwzOF0K2xdZ6dahEiCD523JqfAJJ9KVs_qpmg-4AwrdsB06tcUAj3-MuwaEHiSbJcBk9O91gHQls41k6HElEIS84iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5526a3ee7.mp4?token=syJi0A3fUQ0RCZiEZU1PBzsEexBrs_XC6L41lO0pZbIFBfXQ_wffIHqdN8PO38ntLFLpGP6JNCjJCYlK_bx2oU1rjk_AKfwiDEas1Ej_jk1v_-9FJbzVpchs7Tiptfzu-3MfwVsas02vfROWEhWiCMpcHB86kz5CpkM1Kc1jXhoKAg-MW4RTDTBWwlMon-m6f4N9WeobpSK00mjE79-rp4hSfC353I0sU_VwhAoIpLfc7NK4n97ZQ-V6bMg6SwzOF0K2xdZ6dahEiCD523JqfAJJ9KVs_qpmg-4AwrdsB06tcUAj3-MuwaEHiSbJcBk9O91gHQls41k6HElEIS84iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ درباره ایران: یا ما به یک توافق خواهیم رسید، یا این موضوع به سرعت و به طور کامل به پایان خواهد رسید
🔹
این موضوع آنقدر سریع به پایان خواهد رسید که سرتان گیج خواهد رفت.
🔹
مسئله ایران با پایان انتخابات میان‌دوره‌ای به پایان خواهد رسید، و احتمالاً حتی قبل از آن.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/692128" target="_blank">📅 23:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692127">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
تهدید دوباره ترامپ برای حمله به کوه کلنگ
🔹
رئیس‌جمهور آمریکا در جلسه با سران کشورهای حاشیه خلیج فارس گفت که ایالات متحده آمریکا ممکن است مجبور شود «کوه کلنگ را منفجر کند.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/692127" target="_blank">📅 23:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692126">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
تکرار ادعاهای ترامپ درباره تنگه هرمز
رئیس‌جمهور آمریکا:
🔹
ما شبانه و گاهی هم در طول روز، اما بیشتر در دل شب ۲۵ تا ۳۰ فروند کشتی را اسکورت می‌کنیم.
🔹
این محاصره و کنترل، قوی‌ترین چیزی است که تا به حال کسی به چشم دیده؛ ما نامش را "دیوار فولادین" گذاشته‌ایم.
🔹
حالا حجم نفتی که از تنگه هرمز عبور می‌کند، از زمان آغاز درگیری‌ها تا به امروز به بالاترین حد خود رسیده است.
🔹
ما آینده خاورمیانه را به مراتب روشن‌تر خواهیم ساخت. موضوع ایران و وضعیت موجود، به محض پایان انتخابات میان‌دوره‌ای حل‌وفصل خواهد شد؛ چرا که پایان دادن به تهدید هسته‌ای ایران، هیچ ربطی به موضوع انتخابات ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/692126" target="_blank">📅 23:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692125">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cf60d7e4a.mp4?token=jAtYqMhR8lfBW4L8EwgfgT1VYP8SbQAPXqZblbDOXSWXrxUs1cIEXJEq3As7cG2FTkuNiydVrLighE1AFn1TY2ZrY_gmDIaA6QE_CWds5mBEJg9cO9VAEWhcoCoXQ_PTZK30ijNhJaRvgO5BTJgThU7n9BlLhhz0YNm88sJYZOH5tQOP-W981f8l7G0Uae1WYBtG3OhOOJra26QtdpMR-L82sxAODl2pU7hliwi4x5tz6eemzRc_y56eu2vle2kKMs5KP4metS9s4NBQqbFZKe_fFYO56bbCg3JWBrl1Zc3hO8c_L2FPnlXoaPaAspSmxKgMD06KGBVDSo1KbR7Ilg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cf60d7e4a.mp4?token=jAtYqMhR8lfBW4L8EwgfgT1VYP8SbQAPXqZblbDOXSWXrxUs1cIEXJEq3As7cG2FTkuNiydVrLighE1AFn1TY2ZrY_gmDIaA6QE_CWds5mBEJg9cO9VAEWhcoCoXQ_PTZK30ijNhJaRvgO5BTJgThU7n9BlLhhz0YNm88sJYZOH5tQOP-W981f8l7G0Uae1WYBtG3OhOOJra26QtdpMR-L82sxAODl2pU7hliwi4x5tz6eemzRc_y56eu2vle2kKMs5KP4metS9s4NBQqbFZKe_fFYO56bbCg3JWBrl1Zc3hO8c_L2FPnlXoaPaAspSmxKgMD06KGBVDSo1KbR7Ilg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ درباره ایران: استیو و جرد امروز جلسه‌ای بسیار سازنده با میانجی‌گران ایران داشتند. خواهیم دید چه اتفاقی می‌افتد
🔹
فکر می‌کنم دامنه حرکت زیادی برای آنها برای انجام توافق وجود دارد. این چیزی است که از همه می‌شنویم.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/692125" target="_blank">📅 23:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692124">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
‌
هواپیمای حامل رئیس‌جمهور حدود ساعت ۱۷ به وقت نیویورک و ۳۰ دقیقه بامداد چهارشنبه به‌ وقت تهران وارد فرودگاه بین‌المللی جان‌اف‌کندی می‌شود
🔹
این پرواز عصر امروز پس از سوخت‌گیری و توقف کوتاه در الجزایر به‌ سمت شرق آمریکا حرکت کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/692124" target="_blank">📅 23:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692123">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e4ea7a67.mp4?token=W7kdcHz_ygiowoFTkBjACE6Ti5itBcPn8DcoyerSgBt7NHFI_9v-FmclgKTt3RDitTUnWqoNPFzikYF42W0PT-y9sYUZEr_wvGuPIhUxQIJsgZgTt8K08ZtWk-RfLcc38mBBMJQZlNlRF6TQUtwil5zMWeNCGeB10NeYpCjgoEePilz16LMPCPigRI8ABKXDaE53hep5jyE8RmlcmQIyvB1xsu_AIKKik5cHAR5xjdJ70YeqM1nE0_YteL-EmEFQJUnM5fo8SIvXgoEuVn1AiLQoFHpqD0hei8xGHeGViQGT5Qv0duaGeNQU5EdmkhgGAl5Sy-RSLUqGst5c_0TDwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e4ea7a67.mp4?token=W7kdcHz_ygiowoFTkBjACE6Ti5itBcPn8DcoyerSgBt7NHFI_9v-FmclgKTt3RDitTUnWqoNPFzikYF42W0PT-y9sYUZEr_wvGuPIhUxQIJsgZgTt8K08ZtWk-RfLcc38mBBMJQZlNlRF6TQUtwil5zMWeNCGeB10NeYpCjgoEePilz16LMPCPigRI8ABKXDaE53hep5jyE8RmlcmQIyvB1xsu_AIKKik5cHAR5xjdJ70YeqM1nE0_YteL-EmEFQJUnM5fo8SIvXgoEuVn1AiLQoFHpqD0hei8xGHeGViQGT5Qv0duaGeNQU5EdmkhgGAl5Sy-RSLUqGst5c_0TDwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: چه پیامی برای پوتین دارید؟
🔹
ترامپ: جنگ را متوقف کنید.
🔹
خبرنگار: و اگر برعکس باشد؟ یعنی تشدید کنید؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/692123" target="_blank">📅 23:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692122">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
اولین مصاحبه محسن نامجو در ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/692122" target="_blank">📅 23:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692121">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ادعای ترامپ: یک مقام آمریکایی با هیئت ایرانی دیداری سه‌ساعته داشته که به گفته او خوب پیش رفته است
🔹
برای ایران یا عظمت و شکوفایی بالقوه وجود دارد، یا نابودی.
🔹
در یک حالت، نابودی است و در حالت دیگر، عظمت بالقوه. ایران می‌تواند یک کشور بزرگ باشد/ خبرفوری…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/692121" target="_blank">📅 23:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692120">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رشیدی‌کوچی، نماینده سابق مجلس: مشکل من با جبهه پایداری این است که به اعتقادات و سرمایه اجتماعی کشور آسیب می‌زند/ رأی پایداری، همان رأی جریان اصولگرایی نبود
جلال رشیدی کوچی، نماینده سابق مجلس:
🔹
جبهه پایداری درصد کمی طرفدار دارند؛ ۴ تا ۵ درصد.
🔹
اگر بخواهیم ببینیم جبهه پایداری چقدر رای دارد باید لیست آن را در شهرهای بزرگ ببینیم که نگاه مردم عموما سیاسی است تا معیشتی، طائفه‌ای و رفاقتی.
🔹
رأیی که پایداری‌ها در مجلس آوردند برای پایداری‌ها نبود؛ رای جریان اصولگرایی است.
اصلاح طلبان هم آدم‌های محبوب و مقبولی نیستند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/692120" target="_blank">📅 23:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692119">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f15f225b.mp4?token=lqh22xNdDZSmK_I66q0J5FVpculEJ8gb5wz7j_crF1Lf7rdE6Z55FtYaWP5iYZztaUGlLNObDMNnIJub2lz2TWeQ3mRSFy0bS1y0j_mQnBFFN5BHb1Mp2T0Uq2in3mIVoxKeK4NOAKD0eI9PpWnTeDCHX90J70KkmqbafR9wzKlsLT4gBPlYBXbYFn0aBJPOiqOBe3OJbYffHZKCzWOLM6B3OYG8O4Z2ZzKPmOiT8l6r7S8FpJoG1ThneTB9SgFMnaMjR3wagn_griAL1f91XY9UWNwtZ_yirZtISxLxNnVe8UunB70aqTRxKFIl7ihr7LivAv6rgp1-JnXNoyNedQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f15f225b.mp4?token=lqh22xNdDZSmK_I66q0J5FVpculEJ8gb5wz7j_crF1Lf7rdE6Z55FtYaWP5iYZztaUGlLNObDMNnIJub2lz2TWeQ3mRSFy0bS1y0j_mQnBFFN5BHb1Mp2T0Uq2in3mIVoxKeK4NOAKD0eI9PpWnTeDCHX90J70KkmqbafR9wzKlsLT4gBPlYBXbYFn0aBJPOiqOBe3OJbYffHZKCzWOLM6B3OYG8O4Z2ZzKPmOiT8l6r7S8FpJoG1ThneTB9SgFMnaMjR3wagn_griAL1f91XY9UWNwtZ_yirZtISxLxNnVe8UunB70aqTRxKFIl7ihr7LivAv6rgp1-JnXNoyNedQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیگه برای همیشه حاضرید...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/692119" target="_blank">📅 23:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692118">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
روایت سرلشکر رحیم صفوی از سوابق رهبر معظم انقلاب در جنگ
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/692118" target="_blank">📅 23:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692117">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953d4f15e4.mp4?token=g6UEUuL-b2KMNZcBYwdeBLzGcQrIKRnxTmxxi8GMNfJeT05vf2I4v1NEWV6TlUDbt8G53efYrCNd-ZVmim1nwJU-AzmXt0nQV3z3xNB9vwt_Vvnp6JqwwnXpz-4W6rFnsLxCY7IVXFdb0JTZdqzT_8MDpVnzAOb1wtAUSOVV4-fctcHdTc7m2JQOvggnFbSYQ8xHy3VFlJiQBceF2W62yctDd9nRTuTyqR2gJ_D2qYQImatBeLDlj7RvstjJpYp-aKdONgnkFkBvxPW6RFj99mj6_dWkUCfX4SeHggKuKI3tOzARoDQmFg7MOd7-eJT4BwISvgZi-yJVTxYAC66QOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953d4f15e4.mp4?token=g6UEUuL-b2KMNZcBYwdeBLzGcQrIKRnxTmxxi8GMNfJeT05vf2I4v1NEWV6TlUDbt8G53efYrCNd-ZVmim1nwJU-AzmXt0nQV3z3xNB9vwt_Vvnp6JqwwnXpz-4W6rFnsLxCY7IVXFdb0JTZdqzT_8MDpVnzAOb1wtAUSOVV4-fctcHdTc7m2JQOvggnFbSYQ8xHy3VFlJiQBceF2W62yctDd9nRTuTyqR2gJ_D2qYQImatBeLDlj7RvstjJpYp-aKdONgnkFkBvxPW6RFj99mj6_dWkUCfX4SeHggKuKI3tOzARoDQmFg7MOd7-eJT4BwISvgZi-yJVTxYAC66QOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشارکت مشاغل مختلف در رژه بزرگ جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/692117" target="_blank">📅 23:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692116">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">گذر از دجال-جلسه سوم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/692116" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
دوره‌ گذر از دجال
جلسه‌ سوم:
تفسیر زیارت عاشورا
🔹
زیارت عاشورا «منشور نجات از فتنه دجال» است و در واقع تقابل با یک جریان مخفی شیطان‌پرستی است که ریشه در بت‌پرستی باستان داشت.
🔹
زیارت عاشورا، یک ساختار عملیاتی شامل پنج پایه برای پاکسازی وجود و پیوند با نور الهی است.
🔹
۱)
سلام، دعوت از ملائکه:
با سلام دادن به اولیاء الهی، در واقع فرشتگان رحمت و خیر را به زندگی خود دعوت می‌کنیم.
🔹
۲)
لعن
،
تضعیف اجنه شیطانی:
لعن، تیراندازی به قلب ظلمت است، این کار باعث ضعیف شدن قدرت اجنه و شیاطینی می‌شود که از دجال حمایت می‌کنند.
🔹
۳)
برائت، پاکسازی ژنتیک و روحی:
ما با گفتن «برئتُ الی الله»، از آن بخش از وجودمان که ممکن است با «ژن قابیل» یا صفات دجالی آلوده شده باشد، اعلام بیزاری می‌کنیم تا خدا ما را از صف دشمنان بیرون بکشد.
🔹
۴)
عهد و بیعت
: عهدی است که زائر با امام حسین(ع) می‌بندد تا در جبهه حق باقی بماند.
🔹
۵)
دعا:
مؤمن از خدا می‌خواهد در مسیر حق ثابت‌قدم بماند و در قیامت از شفاعت امام حسین علیه السلام بهره‌مند شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/692116" target="_blank">📅 23:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692114">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1lNN5B09I-pejGgqjSwaJzZwhlSNzpVxY6PSauDjMitQ-ipSDNpYfC5_Mr1hytdvJRVFKm5AUv8md5FAtPa-qVrxTPjHaWDuQJ2lHFD8qBizbxTNRBJxl8FRM1P7mf2WWgchuixEz4VuafCvMjyZURiRUdM9nLsIj2olpkxivGScWdGhrkgbCP6vbOSB3tvwFaWygn6VJWgMsC2zWANRlNZVqVE0xDj7rhL6sHpBDCwYC8Gs3fRcZ6TGaGIBN9ARpsVNsSkLopfQr0CHQD31SonmCHg6dGmCfCulVfsEb-stuXd2Vdo_Mu2WmOI1ze2mHOhtwcWT72kIyabL51YoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنگ مدرسه در میناب با حضور معاون علمی رئیس‌جمهور و جای خالی ۱۶۸ دانش‌آموز شهید نواخته می‌شود
.
🔹
معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور، به نمایندگی از رئیس‌جمهور و هیئت دولت، با حضور در میناب و ادای احترام به شهدای دانش‌آموز، آیین زنگ آغاز سال تحصیلی را در مدرسه «شجره طیبه» برگزار خواهد کرد.
🔹
زنگ آغاز سال تحصیلی جدید در میناب، امسال در حالی به صدا درمی‌آید که جای ۱۶۸ دانش‌آموز شهید این شهرستان در میان نیمکت‌ها خالی است؛ دانش‌آموزانی که روزی پشت همین نیمکت‌ها می‌نشستند و امروز یادشان در مدرسه‌های میناب زنده است.
🔹
این آیین با حضور مسئولان، فرهنگیان، دانش‌آموزان و خانواده‌های آنان برگزار می‌شود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/692114" target="_blank">📅 23:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692113">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ادعای ترامپ: یک مقام آمریکایی با هیئت ایرانی دیداری سه‌ساعته داشته که به گفته او خوب پیش رفته است
🔹
برای ایران یا عظمت و شکوفایی بالقوه وجود دارد، یا نابودی.
🔹
در یک حالت، نابودی است و در حالت دیگر، عظمت بالقوه. ایران می‌تواند یک کشور بزرگ باشد/ خبرفوری…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/692113" target="_blank">📅 22:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692112">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4916435f1.mp4?token=F6F8DKlSZsgxVUQCu9YNsCy3SdJRPqzZjCZYaKzxjrj-JwgD5bBaXM1yPtaKy-qzkRn6JWOmBvLkWdODrU2Mmq9W9XF-ujpO7k74LpdUBxwUtDRNCuv1lJbm5VIVHCgZnn4j4Y1dOQd8af4tq01uyXM4EHS9wPNeq4ekyiJxTdRmjJhuVpJTEj9K3yJffGHTgVZKXEzUr2i0cHgcYzcH_hlcRgJcWAVn3KpeLhi8-eoNiuJo4_W0xTK1Az8TYWkmQIha7I31G4fsY0GHmQzYm1RdnrSiOHw4fMCSSa3DXOQoyWiwHbQCPk-uAYigjhx57kxwU_SYSg5NlFnlN4PDOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4916435f1.mp4?token=F6F8DKlSZsgxVUQCu9YNsCy3SdJRPqzZjCZYaKzxjrj-JwgD5bBaXM1yPtaKy-qzkRn6JWOmBvLkWdODrU2Mmq9W9XF-ujpO7k74LpdUBxwUtDRNCuv1lJbm5VIVHCgZnn4j4Y1dOQd8af4tq01uyXM4EHS9wPNeq4ekyiJxTdRmjJhuVpJTEj9K3yJffGHTgVZKXEzUr2i0cHgcYzcH_hlcRgJcWAVn3KpeLhi8-eoNiuJo4_W0xTK1Az8TYWkmQIha7I31G4fsY0GHmQzYm1RdnrSiOHw4fMCSSa3DXOQoyWiwHbQCPk-uAYigjhx57kxwU_SYSg5NlFnlN4PDOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات یک جانبه گرایانه مکرون درباره تنگه هرمز: تنگه هرمز نباید به عنوان ابزار فشار استفاده شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/692112" target="_blank">📅 22:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692111">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3722928a6.mp4?token=hzijz2FMgO-lv5rdodJFMbST9YmKA30mxki1CTNW5FBD3G2FgP1oRPf4cdRg0d5ZNS9r-9H2Z5YG87OLXIuB5haIVVFwQeDT2dwA_OKkIKFAsB8uaGkKM1E4aZEoz1QTKQH4e0i4xN0fTBWaeRuUrdPLq9PlpW0VzLAkgjQlsveq3MFypRic7eNZhROfVEv5Tq10RgUd40O3zCOyuQdAjs7Nui9gyusi8ntFsBN2OBMi8ZPBF2LRpR4j4SJ2-VF8b_M99q3zjWJh3rSej0GSLKuMSxp0enuTidLwl7zPvIDThzXsLuyeQzOw-0VrjH6_Oq76CKiUNCxln8akjC3bUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3722928a6.mp4?token=hzijz2FMgO-lv5rdodJFMbST9YmKA30mxki1CTNW5FBD3G2FgP1oRPf4cdRg0d5ZNS9r-9H2Z5YG87OLXIuB5haIVVFwQeDT2dwA_OKkIKFAsB8uaGkKM1E4aZEoz1QTKQH4e0i4xN0fTBWaeRuUrdPLq9PlpW0VzLAkgjQlsveq3MFypRic7eNZhROfVEv5Tq10RgUd40O3zCOyuQdAjs7Nui9gyusi8ntFsBN2OBMi8ZPBF2LRpR4j4SJ2-VF8b_M99q3zjWJh3rSej0GSLKuMSxp0enuTidLwl7zPvIDThzXsLuyeQzOw-0VrjH6_Oq76CKiUNCxln8akjC3bUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت سرلشکر رحیم صفوی از سوابق رهبر معظم انقلاب در جنگ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/692111" target="_blank">📅 22:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692110">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
سرلشکر صفوی: آمریکا می‌خواست تنگۀ هرمز را باز کند اما تنگۀ باب‌المندب هم دچار مشکل شد
مشاور رهبر انقلاب:
🔹
یکی از اهداف آمریکا تسلط بر نفت ایران بود اما ایران حالا جریان نفت دنیا را کنترل می‌کند.
🔹
روسیه و چین علاوه بر حمایت‌های سیاسی در زمینه‌های دیگر نیز بصورت جزئی به ایران کمک می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/692110" target="_blank">📅 22:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692109">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWgYYC7nrj8Xz8nVcwPaFE7cz-M-ZmVQ7LEVwVGKuQzhOgGFaOp27nP6LZpcnoLr-SN7-sHVVh4_yCL0OFlCdNe9plmvbXlEUdH4GJLfOlk9RjApIbWtUO-DM7ve_QrEibiN1xfKSPddpkvjeYn_s7Fjwql7N_P9Qi4kb0f_N3eXJYGNKVSQ13vllVPJP2JQY0Y8fckg-D6eOdnJQn8x7KJOCzwifi8-0ftaI04ziPsCUTb8FBawQk6_kY42Sdl7dBlzaTU1col26DLJjyeNogcw0Y8ssPBwCXQad1BjnAkTYpbZqfxENPzbmL42_X8LIYePAiCCvq1q3vfc6dLZig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | جشن فرشتگان
🔹
همراهان گرامی خبرفوری، شما می‌توانید با ضبط یک ویدیوی کوتاه از دانش‌آموزان خود با لباس فرم مدرسه، در این پویش شرکت کنید .
🔸
از کودکان خود بخواهید این جمله را بیان کنند: «کودکان شهید میناب؛ ما راهتان را ادامه می‌دهیم.»
🔸
ویدئو های خود را به آیدی زیر ارسال کنید
👇
#جشن_فرشتگان
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/692109" target="_blank">📅 22:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692108">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65559c7c2c.mp4?token=qgODm5iA5mTWeCYjlcJMPhhizaeAvRhS_Ph1kjaQ04fPMZaanhFdKLYQSLk0fS89I090zXTUhirbeicSyQFWVvo0oqBT7bsGR-kHcO6QGQlkOOmqyHcjiFNyolqCYCy70Fgqr7M8x_VJzQsYJPkC1RQgTf5rAgUZsJVWVCWigV6V4HXyIPSsYyPRiYyN0oPb7F1BrC0lXnBkGo8EjYbjfpPJqQCizWaS8WqA2WDiXRVE_zsBskD1NA0Lc7CaCM43BSetEJnjP7ILmZq6UIQVuNSQe3AQpMgSYIBK2slibhUDJz7KbAKAzkg5-Z4kI5MJ0jeFOCXbtbJNKsPBrcf3zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65559c7c2c.mp4?token=qgODm5iA5mTWeCYjlcJMPhhizaeAvRhS_Ph1kjaQ04fPMZaanhFdKLYQSLk0fS89I090zXTUhirbeicSyQFWVvo0oqBT7bsGR-kHcO6QGQlkOOmqyHcjiFNyolqCYCy70Fgqr7M8x_VJzQsYJPkC1RQgTf5rAgUZsJVWVCWigV6V4HXyIPSsYyPRiYyN0oPb7F1BrC0lXnBkGo8EjYbjfpPJqQCizWaS8WqA2WDiXRVE_zsBskD1NA0Lc7CaCM43BSetEJnjP7ILmZq6UIQVuNSQe3AQpMgSYIBK2slibhUDJz7KbAKAzkg5-Z4kI5MJ0jeFOCXbtbJNKsPBrcf3zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دنیای عجیب مورچه‌ها از زاویه‌ای دیگر
🐜
😁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/692108" target="_blank">📅 22:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692107">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
خبرهایی از ساقط شدن جنگنده دیگر سعودی در یمن
🔹
یک رسانه عراقی خبر داد که نیروهای مسلح یمن موفق شدند جنگنده اف-۱۵ دیگر سعودی را ساقط کنند.
🔹
نیروهای مسلح یمن هنوز بیانیه‌ای در این باره صادر نکرده‌اند./ فارس
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/692107" target="_blank">📅 22:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692106">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJefAvC_lucYv60zwfhcnQ2r6VCRxzGLURUPwPOoneVk4gYme7Yv4MWNMRKq6r_MiBoow3d8L0EjwMb_9rfxWnj-B6bAskNGd-yahzCgq1MtjPVU0uFviXb8XXlS4UmyzyX6qHiCA1uPWlMWxCexICjb0G4_YcO_wcv5EOMrxMu1PCPOVB8LlsmvDeANeWFLdaOtCY7SQJ4Z5HA551wR0O_jGwSQ6X80OVrdXcSJV9axD26rEaYYRKYHj6uSXtX5aBwb7tNWj7o8LbOtqqcD24BOQDu7N41eWHXYBdeDq4MOG0PJlHdPjR7i_R0Ehw0twhXRmEga-CjMbUDyJVNoGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز درباره ایران در سخنرانی سالانه مجمع عمومی ملل متحد: آن‌ها قلدرِ خاورمیانه بودند، اما دیگر قلدر نیستند
🔹
از همان روز نخستِ ورودم به عرصه سیاست، موضعی تزلزل‌ناپذیر داشته‌ام: هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست یابد. #Devil…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/692106" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692105">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3809b30f8.mp4?token=MaPyPV3GUDzP0lYX7nu5p36loN8pvn6esmgwUqRbfE7jTz44qs8TaaTQcbxzXwZb6VwsJOGuxMBCYsUlA3LItyoRaPeD-2I_fFWM3rDC_JVBW8A2VRUQW-Yjw8BHdXjsz1F9a20EGDuUiQ6hSavh_KNSE0u5YofB4Nmx4aWRQR1Nxq0w9jWvojAQo0imUv76zNbDmguQtLGGLy_4bfnXgqMOkkwud6Jw9htCdcOcw5KOMZD6OBiIuIVfrM0of7oyD2zNn-e05t4IVHlE9ZMkEok8v0s8sfCP5TEdMs01mKXa1ZIauySC-guk7V-sNn7YZJBZwl1tD6kSYeFItX_Kyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3809b30f8.mp4?token=MaPyPV3GUDzP0lYX7nu5p36loN8pvn6esmgwUqRbfE7jTz44qs8TaaTQcbxzXwZb6VwsJOGuxMBCYsUlA3LItyoRaPeD-2I_fFWM3rDC_JVBW8A2VRUQW-Yjw8BHdXjsz1F9a20EGDuUiQ6hSavh_KNSE0u5YofB4Nmx4aWRQR1Nxq0w9jWvojAQo0imUv76zNbDmguQtLGGLy_4bfnXgqMOkkwud6Jw9htCdcOcw5KOMZD6OBiIuIVfrM0of7oyD2zNn-e05t4IVHlE9ZMkEok8v0s8sfCP5TEdMs01mKXa1ZIauySC-guk7V-sNn7YZJBZwl1tD6kSYeFItX_Kyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور دختران و زنان در رزمایش ۳۱۳ هزار نفری جان‌فدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/692105" target="_blank">📅 22:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692104">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پشت‌پرده هزینه‌های انتخاباتی؛ از پرداخت ۹۰۰ میلیون تومان برای همراهی یک چهره تا شام‌های هزاران نفری از زبان رشیدی‌کوچی، نماینده سابق مجلس
جلال رشیدی کوچی، نماینده سابق مجلس:
🔹
بعضی نماینده‌ها بابت هزینه برای رای آوردن از شرکت‌ها و سازمان‌ها کمک می‌گیرند.
🔹
کل هزینه انتخاباتی من در سال ۹۸ مبلغ ۱۲۵ میلیون تومان شد در حالی که آنطور که گفتند یکی از رقبای ما فقط ۹۰۰ میلیون تومان پرداخت کرده بود که یک نفر کنارش عکس بگیرد.
🔹
یکی دیگر از نماینده‌ها پمپ بنزین اجاره کرده بود که هر کسی آنجا می رود هزینه بنزین پرداخت کند .
🔹
یکی از رقبا بطور متقن هر شب ۲ هزار نفر را به مدت ۱۰ روز شام می داد.
🔹
مخالف با تبلیغات نیستم؛ با این مخالفم که شفافیت در این موضوع نیست و فردا چگونه میخواهی پس بدهی؛ بالغ بر ۶۰ تا ۷۰ درصد نماینده‌ها اینگونه هستند‌.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/692104" target="_blank">📅 22:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692102">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d2c9a9d6d.mp4?token=mfATQ3-TTafatJ3-kMRb3X-1TSuYkdAlqvP1pgBfj79iVKBEVvzwZ38S2hHzjcE04boNBa26WIt1jA--_cJz743uIWEVpBhZyFGtsv7rhpIBSRCiR-8jS3JRxrAeVCfU-AY4UOc6bOsAPpXeTaNQ7bV0Tz5jut5O66_bhgJpBPQ64lxrKWDahs9iSgvwF4naa8TnHwWbxBeNI4mY64Gg6z6xCQABJG4T254HjEfG1kSQh6027NjPB9Pl-1LS4S3GltAtmMLWc0_APyAzkpCKL2L2khMBQo18Uj5w1_iqOR5M5fhKZiyoFh9sbDqpTjLZOV40ZoTWwPZx0MsU3TqtDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d2c9a9d6d.mp4?token=mfATQ3-TTafatJ3-kMRb3X-1TSuYkdAlqvP1pgBfj79iVKBEVvzwZ38S2hHzjcE04boNBa26WIt1jA--_cJz743uIWEVpBhZyFGtsv7rhpIBSRCiR-8jS3JRxrAeVCfU-AY4UOc6bOsAPpXeTaNQ7bV0Tz5jut5O66_bhgJpBPQ64lxrKWDahs9iSgvwF4naa8TnHwWbxBeNI4mY64Gg6z6xCQABJG4T254HjEfG1kSQh6027NjPB9Pl-1LS4S3GltAtmMLWc0_APyAzkpCKL2L2khMBQo18Uj5w1_iqOR5M5fhKZiyoFh9sbDqpTjLZOV40ZoTWwPZx0MsU3TqtDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میوه کاکائو رو دیده بودید؟
🍫
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/692102" target="_blank">📅 22:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692101">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gP-a48Lt-sMgZF_Ip9vszcnRcErLAJEOBEoYu1uPBF16wlynIm6wzyQp99q_y2keJi0LotMV7JuCmfAL9RFPy63AXMwZ8lLpQSTAeqI4vHmhSNpWCSqgLPXlSeFV10hRs73h9lN56YN5E1kZKYVCXxut7PMz3tiSEyjiGPZMALA-7pqiuRtrq_oYdP5MW3nDOPkLj6aTupec5YMd5eLM3i_m_5wiSnCcu1Dm_mKj-SUzaXFB9OFBalxkIdu614p10kZa752hZop6K0Q2cuMTChkkrZiYx05TlaT_GYTGaoKBGDv-8bRib1hzz0jpYwXEdu91LWMcps0YCRmyaDDnpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از سخنرانی رهبر شهید انقلاب در چهل و دومین مجمع عمومی سازمان ملل، در دوران ریاست جمهوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/692101" target="_blank">📅 22:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692100">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
مدیرعامل شرکت ارتباطات زیرساخت: طبق برآوردها حدود ده درصد از پهنای باند کشور از استارلینک رد می‌شود
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/692100" target="_blank">📅 22:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692099">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a2d3d3b9.mp4?token=UdCpsi1jQ7P5Lljq3iblHCKNw7RdpM68-4KBl_hob_s6g2OO3_c239q0JvEi66ym8P2QNq7a22pO0VhHiDMQBMS0ZlAekpM3W-TfO5muOofrLqQsahMKOEgL9tcnvy8f7qaP4O_tivuy8ExC9dWZC9RvjqOSGWiK4D0U2XI_UlXH70S4hTEcGEpsb1A0LP0z3s1LUrCqv7b3ZYRrQTDxu1J0s8IDG30QNVjiS9reBw5OOZcsEt1CB7taDWETD9ofyZ-NEziQvvBrJ3wfpze0wjTkpBH8SP3WB-DPAc7DchyGkKQymNbvxiL5ukCw2fN3g35XHpTdSRBjXFSueyAJQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a2d3d3b9.mp4?token=UdCpsi1jQ7P5Lljq3iblHCKNw7RdpM68-4KBl_hob_s6g2OO3_c239q0JvEi66ym8P2QNq7a22pO0VhHiDMQBMS0ZlAekpM3W-TfO5muOofrLqQsahMKOEgL9tcnvy8f7qaP4O_tivuy8ExC9dWZC9RvjqOSGWiK4D0U2XI_UlXH70S4hTEcGEpsb1A0LP0z3s1LUrCqv7b3ZYRrQTDxu1J0s8IDG30QNVjiS9reBw5OOZcsEt1CB7taDWETD9ofyZ-NEziQvvBrJ3wfpze0wjTkpBH8SP3WB-DPAc7DchyGkKQymNbvxiL5ukCw2fN3g35XHpTdSRBjXFSueyAJQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری وزیر نیرو در صحن علنی مجلس: اگر حملات نبود در صنعت برق مشکلی نمی‌داشتیم
علی‌آبادی، وزیر نیرو در صحن مجلس:
🔹
در اثر حملات آمریکا ۴۲۰۰ مگاوات برق از ظرفیت برق کشور از چرخه خارج شد.
🔹
برای امسال تلاش کرده بودیم که نه تنها برق خانگی را پایدار نگه داریم، بلکه به صنعت هم برق بیشتری بدهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/692099" target="_blank">📅 22:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692097">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رشیدی‌کوچی، نماینده سابق مجلس: نماینده‌ها محلی شده‌اند، نه ملی/ دغدغه بسیاری فقط این است که برای دوره بعد دوباره رأی بیاورند
جلال رشیدی کوچی، نماینده سابق مجلس:
🔹
یکی مثل من حرف که می زند درس عبرت برای بقیه می شود؛ خانه نشین‌مان می‌کنند.
نماینده‌ها عموما محلی هستند و ملی نیستند.
جای سوال دارد چرا نماینده ها اینقدر ساکت هستند.
🔹
نماینده‌ها به فکر رای برای دور بعدی خودشان هستند؛ واقعیتی است که هر کس منکر شود دارد سر خودش را شیره می‌مالد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/692097" target="_blank">📅 22:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692096">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
خبرهایی از ساقط شدن جنگنده دیگر سعودی در یمن
🔹
یک رسانه عراقی خبر داد که نیروهای مسلح یمن موفق شدند جنگنده اف-۱۵ دیگر سعودی را ساقط کنند.
🔹
نیروهای مسلح یمن هنوز بیانیه‌ای در این باره صادر نکرده‌اند./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/692096" target="_blank">📅 21:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692095">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
دریافت نخستین سیگنال رادیویی از یک سیاره فراخورشیدی
🔹
اخترشناسان با استفاده از آرایه رادیوتلسکوپی MeerKAT در آفریقای جنوبی، برای نخستین‌بار انتشار امواج رادیویی از سیاره فراخورشیدی Beta Pictoris b در فاصله حدود ۶۳ سال نوری از زمین را شناسایی کردند.
🔹
پژوهشگران می‌گویند این سیگنال‌ها احتمالاً ناشی از شفق‌های قطبی و برهم‌کنش ذرات باردار با میدان مغناطیسی سیاره هستند؛ این کشف به‌تنهایی نشانه‌ای از وجود حیات فرازمینی نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/692095" target="_blank">📅 21:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692094">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
استیو ویتکاف از صحبت درباره دیدار ادعایی با ایران که حدود یک ساعت پیش انجام شد، خودداری کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/692094" target="_blank">📅 21:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692093">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
مسکن زیر سایه جنگ | هر متر مسکن در ۱۵ ماه دو برابر شد | چرا جنگ قیمت خانه را کم نکرد؟
🔹
بازار مسکن تهران در یک سال و سه ماه گذشته، برخلاف انتظار اولیه، نه‌تنها با کاهش قیمت در مناطق آسیب‌دیده مواجه نشده، بلکه در تمامی مناطق ۲۲گانه شاهد رشد قیمت بوده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3247147</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/692093" target="_blank">📅 21:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692092">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1o4V3krQKna7F7yH3kJ8W0wsiy4n-KQHEdF81Cmy3kVUVKkzeIg7lyLB59SDhhwpQdWjl-INEg_t-09ioC9rqSgiKP_6P-_kMNt8Fq1e-0t6uFSIRCteCn_oEpEKoX_HCK8HBkUwzifG8tL_09AIuQ2orws4HsuIDv3Xez4ScWx8nOLYQiOkqSScgCRXmjmHirGDFPFgQfmmXckNFCpAgUXhVbvtWoLbUR6NPkYAcq1KWnMxt-eNblPdNA27kqB3sSL_p09TbWzcNLnD3MZXYRKXsw6n-tSaDqSHbk0zi0CXonVa5PqdaUqwdKVBbumaOTyYK7wg1_gu-q95PJh1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز درباره ایران در سخنرانی سالانه مجمع عمومی ملل متحد: آن‌ها قلدرِ خاورمیانه بودند، اما دیگر قلدر نیستند
🔹
از همان روز نخستِ ورودم به عرصه سیاست، موضعی تزلزل‌ناپذیر داشته‌ام: هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست یابد. #Devil…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/692092" target="_blank">📅 21:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692091">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/269f77218a.mp4?token=PJppo1sV82xTlgHyf7kp0-DXMwPiPh5ksJ3W46KzXk1oD860W5UpP0TTm7jP1Mg3Pcn4tm9RnTBpxTTj5BOf3WKhjcRayGlL9yESEpICk23n-fxKP3l-547IH2aveqXnVM2KblDYU0G-V6M97bb8o_b8cV1h8-d2zQObVTuV9UZ98Sap5sqLZBCkY6NE6-m2iZQ4laiNn9JVlXfxdGkQrV7yFbZOFdPrnvXLm4bYApEsqOnzKSGe8eBNmdximhqR6dmf6PwZlYaXvAxmnM1obM-EZMBEukf0_2iC7WLEtAHLJzuOF3Msm2M7rYBtPHY0dpMMUynSRZcV2fe1fjqz2CdW3Or_xwYhZyF9LRhjVLZnqgC6xDMfxjdslJ6JUYqjs66pj9F4qVXzPcs4wMVjy3rxnkvETuNItQCRWQG-OvmuKV1gONEgSucDBBxS3Z4EveYSPAWRl0UlOFnm5CLLy4--AlW4x25Gp0zIf6K_o604yopsv2mNQt0pzaZMjyY0gXYcXA4fJiwpXh5lgla21F_gDtP2FBKUHcNLIyJzuNWsje1VpAWRAkYfVErRfkbxAjG5EmKfRi83E6tFEq2Vyblk8nTCX-H25HNH7AcNTL6S0H-Zx_NJ7IfLPWyx4ItMEbX47UmvyCluOuojDYm3IrkPZ2HEcy_K9tBHHG2L7rM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/269f77218a.mp4?token=PJppo1sV82xTlgHyf7kp0-DXMwPiPh5ksJ3W46KzXk1oD860W5UpP0TTm7jP1Mg3Pcn4tm9RnTBpxTTj5BOf3WKhjcRayGlL9yESEpICk23n-fxKP3l-547IH2aveqXnVM2KblDYU0G-V6M97bb8o_b8cV1h8-d2zQObVTuV9UZ98Sap5sqLZBCkY6NE6-m2iZQ4laiNn9JVlXfxdGkQrV7yFbZOFdPrnvXLm4bYApEsqOnzKSGe8eBNmdximhqR6dmf6PwZlYaXvAxmnM1obM-EZMBEukf0_2iC7WLEtAHLJzuOF3Msm2M7rYBtPHY0dpMMUynSRZcV2fe1fjqz2CdW3Or_xwYhZyF9LRhjVLZnqgC6xDMfxjdslJ6JUYqjs66pj9F4qVXzPcs4wMVjy3rxnkvETuNItQCRWQG-OvmuKV1gONEgSucDBBxS3Z4EveYSPAWRl0UlOFnm5CLLy4--AlW4x25Gp0zIf6K_o604yopsv2mNQt0pzaZMjyY0gXYcXA4fJiwpXh5lgla21F_gDtP2FBKUHcNLIyJzuNWsje1VpAWRAkYfVErRfkbxAjG5EmKfRi83E6tFEq2Vyblk8nTCX-H25HNH7AcNTL6S0H-Zx_NJ7IfLPWyx4ItMEbX47UmvyCluOuojDYm3IrkPZ2HEcy_K9tBHHG2L7rM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شروع سال تحصیلی جدید
در چهارشنبه امام رضایی
🗓
💚
🔹
پویش سراسری «مهر رضوی»
قرائت صلوات خاصه امام رضا(ع)
📿
🗓
در نخستین چهارشنبه امام رضایی
سال تحصیلی از حرم مطهر رضوی
🔹
همزمان با مدارس سراسر کشور
🤍
به نیابت از امام شهید و شهدای
دانش‌آموز جنگ تحمیلی دوم و سوم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/692091" target="_blank">📅 21:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692090">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c556986398.mp4?token=c9kcYM2cpOMJshlb3SBekrhXIRSdaq31QkzfgZszNvdHGFIVnK5QyL7ZMvdrPRM6tJj1kDy--jZXmxCrWhTqb_05HtUWnrf8ljPs0ipvggFRGuMf2GVzV1bzvE4l7MTsVIPvE3f3KZUp6Y-rW2pEDjgoOYNoXzDSdL_MMUVXt0gFU_SQ8t0AvfWe8DDDjT9KW6frxrsJsN0mtQWI3hkmQZTOpunjhkZBfPKYhdcHCQQlweFyaXU8YkkOsrd5RDCLSgaDXxkMoepYCcsrGU1eJYXLlwrkJuQt7TIW6jVvNO2DkyWeYg6_w5K82GHKWXG8ubEI5iEjhhni11a5lmw7YEgya0iDOcFetpGmh6r8jY2n0DvK3mxk9uUV_Vecf1MezYPW4EmWZmdYIdvBoZmwQo7we51_K-6qGUUia1iCHzs_BriN-X3t136mIoyt0METiPBtf5Riqh5tAPPGda86JnhbSAMOzcIWVoR7RnW78T6vSlL3xcO7nzm-rNDDflirPYGVdrdhC-amdyx9mO7rWgGZDQP6AV-6WdwCYn5Sf_AVH-DSilQKjtXlcsZGZgWTvyoCcbH8VTkjH0kZ9iaVripZnIShxI7IwS6HhhxNiOUhIweYaQfnMLakX4A0aWMJtl9_nO-Lsdi4h-2P2dRHekBNAnTp8G1nwPgI-rbk2mc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c556986398.mp4?token=c9kcYM2cpOMJshlb3SBekrhXIRSdaq31QkzfgZszNvdHGFIVnK5QyL7ZMvdrPRM6tJj1kDy--jZXmxCrWhTqb_05HtUWnrf8ljPs0ipvggFRGuMf2GVzV1bzvE4l7MTsVIPvE3f3KZUp6Y-rW2pEDjgoOYNoXzDSdL_MMUVXt0gFU_SQ8t0AvfWe8DDDjT9KW6frxrsJsN0mtQWI3hkmQZTOpunjhkZBfPKYhdcHCQQlweFyaXU8YkkOsrd5RDCLSgaDXxkMoepYCcsrGU1eJYXLlwrkJuQt7TIW6jVvNO2DkyWeYg6_w5K82GHKWXG8ubEI5iEjhhni11a5lmw7YEgya0iDOcFetpGmh6r8jY2n0DvK3mxk9uUV_Vecf1MezYPW4EmWZmdYIdvBoZmwQo7we51_K-6qGUUia1iCHzs_BriN-X3t136mIoyt0METiPBtf5Riqh5tAPPGda86JnhbSAMOzcIWVoR7RnW78T6vSlL3xcO7nzm-rNDDflirPYGVdrdhC-amdyx9mO7rWgGZDQP6AV-6WdwCYn5Sf_AVH-DSilQKjtXlcsZGZgWTvyoCcbH8VTkjH0kZ9iaVripZnIShxI7IwS6HhhxNiOUhIweYaQfnMLakX4A0aWMJtl9_nO-Lsdi4h-2P2dRHekBNAnTp8G1nwPgI-rbk2mc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رشیدی‌کوچی، نماینده سابق مجلس: از این مجلس چیزی ندیدم جز اینکه چند تندرو به قالیباف و پزشکیان حمله کنند
جلال رشیدی کوچی، نماینده سابق مجلس:
🔹
مجلس امروز با نیازهای کف جامعه هیچ همخوانی ندارد.
🔹
این مجلس بعد از چندماه بازگشایی طرح مقابله با نفوذ را آوردند؛ طرحی که آخر آن هر کسی حرفی بزند یک برچسبی به عنوان نفوذی به او بزنید.
🔹
من از این مجلس چیزی ندیدم غیر از اینکه چهار نماینده تندروی خوش مغز، جنگ طلب و بی کله به آقای قالیباف و پزشکیان فحش بدهند.
🔹
قرار است با رسایی پیاده رویی برویم و ببینم مردم نظراتشان چیست.
🔹
از نود درصد مجلس چیز خاصی ندیدم و ده درصد دیگر حرفی می زنند که بیشتر نمک روی زخم مردم می پاشند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/692090" target="_blank">📅 21:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692089">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f2b162769.mp4?token=SOhzttq0ZgrZe4ENptNzA83whvMwoUfgKOjCGZsD3l1zpiQ8t5QZp0lXK2xaK75QcF2gXyGen7kPOekvDQXoeRJ6BiSaXPsffylTrT93dtJE4CRc28yWJnKzXdgxBcRrUjlF6cvjA9eWm8xxlpRhzdlHivppwb23rjoSfyLFH5E_OpE6Ie-c64sj7dFqeBvq8DQ1DQLrfYjdGXnM6AMEc1bGTnsnxh2ojxZtqjt-yzY5Mx-rVQpz1YDeaXrat_k1ts3-LHqpnJGuFv17MO_80TpyFeP4-fqw8n7E7_vuTecVg5Z-iKoT8Npj21R_3K2QosnBiYUQlSmwMSKFHC888jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f2b162769.mp4?token=SOhzttq0ZgrZe4ENptNzA83whvMwoUfgKOjCGZsD3l1zpiQ8t5QZp0lXK2xaK75QcF2gXyGen7kPOekvDQXoeRJ6BiSaXPsffylTrT93dtJE4CRc28yWJnKzXdgxBcRrUjlF6cvjA9eWm8xxlpRhzdlHivppwb23rjoSfyLFH5E_OpE6Ie-c64sj7dFqeBvq8DQ1DQLrfYjdGXnM6AMEc1bGTnsnxh2ojxZtqjt-yzY5Mx-rVQpz1YDeaXrat_k1ts3-LHqpnJGuFv17MO_80TpyFeP4-fqw8n7E7_vuTecVg5Z-iKoT8Npj21R_3K2QosnBiYUQlSmwMSKFHC888jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ درباره ایران: آن‌ها قرار است در آینده‌ای بسیار نزدیک، جلسه دیگری داشته باشند #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/692089" target="_blank">📅 21:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692088">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bE25v3SUE90C3NNoT38k1W2mHEa4f6gJfCmbLnioYRXyVuiS7yfG7AyoMich53b3koWZ-JwtD_ytg2mBLD0Zje-nnu4aSDfA-DUyr0LUPz-9QQG7uX9zWphH8hyYyOldK5zp6XnbMLSjwgXfLBrsmey_P8_C0vYMeTe4oNPxlmIa8NHkBXjz5cRAwD3df3RVwKCKFIxFcI-oeyf7g7AWHsmfeGs6itc6j1GLJiv8Pp1lYwxzo8MwxjBl1d5VNpNnekha4dmw75C6j9q_vzYKlSUSB16XPvKdWBcUHRHsLYHe0GDdoVUmON1xQJ6gzeuQ0T2VlTHasIs5K1VYYeZGEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از ساعت ۲۴ امشب پروازهای تهران به بغداد و مسقط لغو شد  سخنگوی سازمان هواپیمایی کشوری:
🔹
از ساعت ۲۴ امشب به وقت محلی، فرودگاه بغداد پذیرش پروازهای ایرانی را انجام نمی‌دهد و به همین دلیل در حال هماهنگی و رایزنی هستیم تا پروازهایی که مقصد آنها بغداد است، به…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/692088" target="_blank">📅 21:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692087">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ادعای ترامپ: یک مقام آمریکایی با هیئت ایرانی دیداری سه‌ساعته داشته که به گفته او خوب پیش رفته است
🔹
برای ایران یا عظمت و شکوفایی بالقوه وجود دارد، یا نابودی.
🔹
در یک حالت، نابودی است و در حالت دیگر، عظمت بالقوه. ایران می‌تواند یک کشور بزرگ باشد/ خبرفوری…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/692087" target="_blank">📅 21:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692086">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ترامپ مدعی شد: مذاکرات ما با ایران تا به امروز ادامه دارد و من معتقدم که با آنها به توافق خواهیم رسید #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/692086" target="_blank">📅 21:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692085">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lt4TOLOQZcqFeOPgN_kIhtNEcXH3z7OpE4OFNC_cHA5rQY7v_ea6-GZ2h2AowAEctIQQyZv6NefC0MP0aVNgACSxLedjWO1NXtxbjupaQ7n3u86E37-YKMHh1fa1tfcoZMzK6i90VATNo2TD32gwTAxU7piM5vMc0GFAlqtsa-jzBLDGaWz4VIijA1huXmIYEDd3aiR8UnZmm2rhVaNQ6OmwuLCjsC6jdbKxOBg2QsQjM-D51iDCHq11K95T-hTSYpK7pRL-2cDAth3KmtOJdKST8n5IxOdM7ifYzvwoxJR1Itzv_3nP_3IvxYckoYSwpHmLn6UPyZeBPpxW8FjFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: هیئت ایرانی هنگام سخنرانی ترامپ درباره حملات آمریکا به تهران از مجمع عمومی سازمان ملل خارج شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/692085" target="_blank">📅 21:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692084">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3e521a07c.mp4?token=dMLTpoz6Vtp2RSEQJ4405KC_nUvH8jquGwX521JGjqAUsXJuMuKMNsOzncGWRePisXEnjMFXPc8IIjdWKDQrWga6NS1LA-K6iwc8pmx0lyi8ih-hVtIGCyLVJpCjGrM9b9GB_aw-DNW_qYBmsPa2FuYbtfKgcHsf9Rl03cYmcUvy3woamPp_Qk_mXgkzzjH39KVB3Y0VkUFncd65NqxLdpTIwuk85Ek31rHtMEuZGKled-GhCSep7sut7O3gjWdDy40UGVVSoadnvaCrLtwH2G9Bpd5pqANbgtm8xDoXiLZ59meTmzesaeNrh5l0oA9MscH_WnsCTTD3JEWU3HNtxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3e521a07c.mp4?token=dMLTpoz6Vtp2RSEQJ4405KC_nUvH8jquGwX521JGjqAUsXJuMuKMNsOzncGWRePisXEnjMFXPc8IIjdWKDQrWga6NS1LA-K6iwc8pmx0lyi8ih-hVtIGCyLVJpCjGrM9b9GB_aw-DNW_qYBmsPa2FuYbtfKgcHsf9Rl03cYmcUvy3woamPp_Qk_mXgkzzjH39KVB3Y0VkUFncd65NqxLdpTIwuk85Ek31rHtMEuZGKled-GhCSep7sut7O3gjWdDy40UGVVSoadnvaCrLtwH2G9Bpd5pqANbgtm8xDoXiLZ59meTmzesaeNrh5l0oA9MscH_WnsCTTD3JEWU3HNtxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجیب ترین خوراکی دنیا در کشور فنلاند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/692084" target="_blank">📅 21:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692083">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
مدیرعامل سایپا: ۶۰ هزار شاهین تحویل دادیم؛ حتی یک دستگاه هم نفروختیم
🔹
علی شیخ‌زاده، مدیرعامل گروه خودروسازی سایپا: «در یک‌ سال‌ونیم گذشته نزدیک به ۶۰ هزار دستگاه شاهین تحویل مشتریان دادیم، در حالی که حتی یک دستگاه شاهین هم نفروختیم و تا پایان تعهدات نیز امکان فروش این محصول را نداریم.»
🔹
او با اشاره به حجم بالای تعهدات گذشته گفت: «در مقطعی حدود ۵۰۰ هزار ثبت‌نام برای شاهین در سامانه یکپارچه وجود داشت؛ رقمی معادل حدود ۱۰ سال ظرفیت تولید این محصول.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/692083" target="_blank">📅 21:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692082">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رشیدی‌کوچی، نماینده سابق مجلس: چرا موضوع موتورسواری زنان را این‌قدر پیچیده کردیم؟/ با یک اصلاح ساده قانونی، این مسئله قابل حل است
جلال رشیدی کوچی، نماینده سابق مجلس:
🔹
معاونت حقوقی رییس جمهور خیلی نمی‌خواهد بالا و پایین کند من میگویم شما یک لایحه برای اصلاح قانون بدهید که صدور گواهینامه برای مردان و زنان به عهده نیروی انتظامی است؛ یک کلمه «و زنان» میخواهد اضافه کنند.
🔹
عده‌ای خشک مغز می‌نشستند که وقتی با آنها حرف می زدم، غصه می‌خوردم و گریه‌ام می‌گرفت که چرا این همه سال در این مملکت این افراد مسئولیت داشته است.
🔹
استدلالهای احمقانه‌ای برای موتورسواری زنان داشتند که اگر بگویم مردم عصبانی می‌شوند؛ مثلاً می‌گفتند خانم‌ها اگر پشت موتور گاز بدهند، مانتو به پای آنها می‌چسبد و برهنگی آن مشخص است. خب احمق الان مانتویشان را هم در آوردند
🔹
بعضی از این آقایان دین را هم بازیچه دست خودشان کردند.
🔹
شما زمانی باید گشت ارشاد را جمع میکردید که کسی خون از دماغش نیامده باشد؛ بعد از آن همه آسیب و اتفاقات چه ارزشی دارد؟
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/692082" target="_blank">📅 21:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692081">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
یک مقام ارشد در کاخ سفید به الجزیره: هیچ دیداری در برنامه رئیس‌جمهور ترامپ با ایرانی‌ها وجود ندارد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/692081" target="_blank">📅 21:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692080">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
سخنگوی سپاه: درباره گمانه‌زنی‌ها پیرامون «کوه کلنگ» نظر قطعی نمی‌دهم، اما اگر آمریکا قصد حمله به هر نقطه‌ای از کشورمان، چه کوه کلنگ و چه غیر از آن را داشته باشد، با قدرت تمام پاسخ خواهیم داد
🔹
ما اهل تبلیغات هالیوودی نیستیم و اسرار نظامی خود را فاش نمی‌کنیم؛…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/692080" target="_blank">📅 21:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692079">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ادعای ان‌بی‌سی: کوه کلنگ هدف اول آمریکاست
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/692079" target="_blank">📅 21:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692074">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kV7FyTNN4ouqKXH8y5Iov4YHVTjfCb3IAIIlqSh8hABKU0JMwIwNP22tJx07AEjNgXrRroIpgw7Q5GdTCl2Vmbzlm7wJdrbgqWLJ9UXsXeYGw65ZTZuh1mGB8uVZ3uHcc4l4cmISpS7ouKLDu6FDC3kc5j9syD9l_O0o0Z9QbckLpyw6NjxNXTtgQo5GccUdGI8jCUKo6D5IvC9rXTZOCrvE13WssyPUWL_IcjzjocD2jpZqXJHS3Xz9UUNCb7xRzejMXLLeL5igAtBzWiWeTWRZOHelHceOoYcjvBuSgDXYITmT14g-qAtCcMvbmi4QIwZuNUsfV2lZtDPC5vYFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dBqbGAVxO8z_g_bfK96ywQr4CiqKJuekSLWeffXEN529FwvKdoUzjLvORwYNpI7BHJM3BACiWpHhL5b0_CIz5q-bFaRjaGO2631Vm4xBb52_cGt_CQqlef7ykiRLoW1nzyz4a3alHqfVVW5yncamvPFNmAbRnyFNvASIOr8VmtXaGaVjBL4fwXZLySDSX8AswGgnA_-Cgm5AUp-2_70fNMIBHoihcZ_Jm1tcfRxeqL7XlfMH2-Fasc-LKOv-GnKeZSbUwo5CSb6KJbOmsOQs0vfGTEq2f5QtHxpuv0QJ-ppU5iW-oytTFiwHUNTgZuzRIGyeRd5yD5rRNBX63dhZEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RlWaVwveRNSXLUGMuxFX5Wd_i3xozC5rPOb0nHsJpx3Rw41jXLKr3fjh5wCpsU65bJZFH0vcsMWhc8RBrqOc-j9vfbCmsF6-BqRrMTdEvprsQ8D7-yk9WC9edvVmLBED3FnKR3Vy7Nx0dTWEy_4d76t7QqYkFW4FfXm_V_9wuF-Js_C2PSrYfN-c9zn9q765oo9aPux4gi7uLl49hxnQ-_EgmXgJQ1Qsl2-6vHEdveth4Tv-eDenvjfemZRiqQuqsbq1zam8Ja4f_fiMKftWc24wP-X0WjvUgtuqvdlbraWw9oVkkJZyTG8HRIKfMCaMYDiE11QBafq3R1hpOxj4MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GRJCE6ZN-AkFq8y50jpD-i4vpoFEhjNBZiSksVusbnFU30n6nFNJb5pcIrZFHLnbKtEGj3veSeihgLLIKt30Hy9BwsRBhVFMPYRCboy7nGm8KfSkUB6N0VvtaLIIAx3sPz2dNZnZxvBnZD55_SLRfljI-jKgfyIzGkld6QJXzCTeYOIxcbo6cI5oXu1OxvsJAc_mn9lxxuIojry_MWQAHYxho-DE2mJKWCO-DYWOOWYaG-Oa2akCWcTZO_e2xrmRVQVzvdxKdEdRunIiLt-Oivde7G3CwqoZJ_ZqvbgZWMt_-c-QTy5Mb-3H7nr6O53gLDvYOp67vB6fKEb8jIQf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A1TAS3ZE5XasLbSauNaL_Jr34qZgFyQUI6YPb_9ff2m97RKYbh9RKgiHz6V4JPk9QIcT3ZjkTSaRTn0XgiGWHegUE-woxEtDK8HAp870Ywr_zBAecAYCs1Chl_r7xjCExM_6PTP6BS_mASP2OCGdYSGzU35taL8wspHbj3tlgAVOv25nSPtk6K8dSUXG4-mZSoG_Jj4rsTu7hdYnc2lKLKRzUq3lC48MCtoLpjan1IBQJccVlnrdO6uCo9-516Y6aMTMHGAS0tg1NA-hbhqDZhzhTY7m09PZVLBjXAzaAXp4jmxqGOAY4bC2v6Sdz-wqgx08JFRpMQTRGEd-j2vBEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند ترفند کاربردی که ممکنه به دردتون بخوره  #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/692074" target="_blank">📅 21:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692073">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbiklf_4d9vN_iKXKWybQwdJ7qJEwYqFvYoyZy0HuWpw3ylv4leKaZkllbvNBR9kYIzkY7dpaUs-X3sxvcYqE7UKgo3fQ-Q4re5er1TBfjDC7Rsls5jTblOivb3HeDd6lWtHogRvGRRfVgTEctngMuC_lXxSyiWrScGSrdLfRadxwsUTWTMmXDXrE_o_sjHz9eO25_iTaKfbrdIiOnKXyFgHlC2ZQDPNcDHPzVfcdzMxit8xuJ7ijaXm8i5Ce6S0wmo6W7CrWeRiobsWXSeEPfOAMdsQ_Z9JNNwkYfO09XW_HB9Bbdl8czG3LQBZ6BsPAjUq4HyeX0_Rat7r9xTNcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از ساعت ۲۴ امشب پروازهای تهران به بغداد و مسقط لغو شد  سخنگوی سازمان هواپیمایی کشوری:
🔹
از ساعت ۲۴ امشب به وقت محلی، فرودگاه بغداد پذیرش پروازهای ایرانی را انجام نمی‌دهد و به همین دلیل در حال هماهنگی و رایزنی هستیم تا پروازهایی که مقصد آنها بغداد است، به…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/692073" target="_blank">📅 21:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692072">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd129974b3.mp4?token=TnORMdYknVzP9K6d1xnWB-22mpNnTrZkx7J82w_R7kXv9gWZNTRKlfKC_hw-fBlQ_L2dFoi5N1-Q8G94bAYmGbwnPwZb15Cqa_4HbQ0Qdxe_p3fYKd18j__BpKWZhvU8eLqBHSsm7eN3Wqc2WdjBKRJe4AFjDjxmYl7UwUpJSzDj9KcR6TJXfLxcVSJZmE0pnpS7AqSmoyYDD0w-0QHzbd8H9_xWIVvIa1oL2gTgOfnD4eX57Gzdc7fgeRNhBQHM-8teBkz8MFNJtCEFaMBxP4ZyHDGT47bF4Z9379tmETU9xfzith2S2IqoWzjUriqv6Kn9FpcU1cLUYOmc_Tc8qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd129974b3.mp4?token=TnORMdYknVzP9K6d1xnWB-22mpNnTrZkx7J82w_R7kXv9gWZNTRKlfKC_hw-fBlQ_L2dFoi5N1-Q8G94bAYmGbwnPwZb15Cqa_4HbQ0Qdxe_p3fYKd18j__BpKWZhvU8eLqBHSsm7eN3Wqc2WdjBKRJe4AFjDjxmYl7UwUpJSzDj9KcR6TJXfLxcVSJZmE0pnpS7AqSmoyYDD0w-0QHzbd8H9_xWIVvIa1oL2gTgOfnD4eX57Gzdc7fgeRNhBQHM-8teBkz8MFNJtCEFaMBxP4ZyHDGT47bF4Z9379tmETU9xfzith2S2IqoWzjUriqv6Kn9FpcU1cLUYOmc_Tc8qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۲۵ سال بعد از ۱۱ سپتامبر یکی از فرماندهان میدانی القاعده و داعش، سوار بر کادیلاک و با گارد حفاظتی وارد نیویورک شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/692072" target="_blank">📅 21:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692071">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEKGhJ3HkOXspyMydriZ09_5pImPyWDoe2gHEDlgqXJoes8A1m8kDMv1Mc9CFBfK-QA1HYxQwth55Jv7H2Gto5PVC-HxwLViU62tz_CCxk2EMYRPVv4QD-r5uqpLav7LWhfOz-PlkQtgsVL1ok0iLeShrqEyk2erOSXDSYqWTt33DQqBikzf24ms1ms_B450j-Ek1D_RBq2OX2Yk85rxHS8SGgzljZAjsZ-86jzYGvsSVqwSWNwSDP-4nvvb2gB4GKduFSKQmzdmK-BVskVZ2SNNkaTg5cnu-zqw1HRAhRcITDBNpIH9ciZ-CTUeg_UFY6-kd8c3b0LyiD3hx1WJWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">THEIR STYLE, THEIR STORY.
هر نسلی، استایل خودش را دارد ...
40% OFF
GERAD Kids & Juniors
تخفیف طلایی | روزهای پایانی
Instagram.com/geradofficial</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/692071" target="_blank">📅 21:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692070">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
از
ساعت ۲۴ امشب پروازهای تهران به بغداد و مسقط لغو شد
سخنگوی سازمان هواپیمایی کشوری:
🔹
از ساعت ۲۴ امشب به وقت محلی، فرودگاه بغداد پذیرش پروازهای ایرانی را انجام نمی‌دهد و به همین دلیل در حال هماهنگی و رایزنی هستیم تا پروازهایی که مقصد آنها بغداد است، به سمت فرودگاه نجف هدایت شوند.
🔹
سایر پروازهای خارجی از جمله استانبول طبق برنامه و روال معمول انجام خواهند شد و در حال حاضر مشکلی برای انجام این پروازها وجود ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/692070" target="_blank">📅 20:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692069">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromعشقه ‌🎒(Seyed Hashemi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSmZGWydWN-_2wOS7QrinBKsJqwBPJ5KB2cqu_ukK43jcnliGj1ObiAV428OW4ybzgePUvWtuEYtyXCz2TuzRqQ0vMqWR1tYaLz922lVPllSbhpMDj1GHVs9ig8AccEKF8quWpQuQMegrwEwYfNZM1SjkyMvNqmAWg32frW5Mdp4PQ7GfaizyueVmmmXviLImRrWOsjlyWIMq9owVESNM9oQVWiq2_P7F0JcmneKic5dPPkvM0LacoB3DOPVh0pdl9l5LJMDqGN92jj1QI3uXZPEluW1L1KTow24-yw-PfD3_PnfzCe26Gey0n4cFHnJwtag4t8k_WI-dwki8ysh6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلسفه تأسیس سازمان ملل بعد از جنگ جهانی دوم این بود که کشورها از موضع برابر با هم برخورد کنند و استقلال سیاسی همدیگه رو به رسمیت بشناسند!
حالا این دلقکِ تروریست، رسما در سخنرانی سازمان ملل، یک کشور عضو رو که از قضا جزو بنیانگذاران هم هست، تهدید به نابودی می‌کنه!
حقوق بین‌الملل؟!
اینجا قانون جنگل حاکمه</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/692069" target="_blank">📅 20:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692068">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14321ab2e.mp4?token=I66N_K7weY4l6fDN5V4QBYae-_0Lul0X1wOHHkoKm9_Zkkl0pcEHhYKMBzwdMbTADGnlkEg7IqKJFSDdCvJsrVlVdJjbDy3nus1apz-QcGwIFka7lFVVpWMxwDG8ASeH0ihWbHj7la8NRsDjreLVFz3-zqS3OwrpR54VckXdFgAPQ8dc2cXzztv3ai9Iv24yroZ0CitwMlxTpLi0MqGGY_0GgtE2KTlF84J_a1tWKTMdUENu6NUZFcqtxZ44ezhcZ8uO_Xd7kKE9xpSBJYq77RnZ8ptMfIZETSykcePVqRduQ2jBSXfdVJYpURub_bz0i33NohySpmZ-MTGBC522ejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14321ab2e.mp4?token=I66N_K7weY4l6fDN5V4QBYae-_0Lul0X1wOHHkoKm9_Zkkl0pcEHhYKMBzwdMbTADGnlkEg7IqKJFSDdCvJsrVlVdJjbDy3nus1apz-QcGwIFka7lFVVpWMxwDG8ASeH0ihWbHj7la8NRsDjreLVFz3-zqS3OwrpR54VckXdFgAPQ8dc2cXzztv3ai9Iv24yroZ0CitwMlxTpLi0MqGGY_0GgtE2KTlF84J_a1tWKTMdUENu6NUZFcqtxZ44ezhcZ8uO_Xd7kKE9xpSBJYq77RnZ8ptMfIZETSykcePVqRduQ2jBSXfdVJYpURub_bz0i33NohySpmZ-MTGBC522ejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای کارشناس شبکه سه: با توجه به شواهد منطقه، احتمال اقدام جنگی آمریکا بر علیه ایران زیاد است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/692068" target="_blank">📅 20:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692067">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افزایش ۲۳ درصدی قیمت پوشاک/ قدیری: ۳۵ تا ۴۰ درصد بازار پوشاک در اختیار کالای قاچاق است
سعید جلالی قدیری، دبیر اتحادیه تولید و صادرات نساجی و پوشاک در
#گفتگو
با خبرفوری:
🔹
واحدهای بزرگ صنعتی پوشاک پس از جنگ با کاهش ۲۵ تا ۳۰ درصدی تولید مواجه شده‌اند و با تورم ۴۶ درصدی، قیمت پوشاک حدود ۲۳ درصد افزایش پیدا کرده است.
🔹
حدود ۳۵ تا ۴۰ درصد بازار پوشاک در اختیار کالای قاچاق است و ۶۵ درصد بازار از تولید داخل تأمین می‌شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/692067" target="_blank">📅 20:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692065">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lV3Zdkt14OC3p0mtao1ysQV3LPrE_OKzDPWaVoaPb9cdtC8dq2F630J-ClR3Xj5ANWRhrnlTd8kdKHrJSM-WRHkAweeY3nYP2U_S_YXUSHAaCn5c4H4JAMeHMYbk0K5unCB9hpoFsGf1gd_CKglRNmA8KSeAoOOjkO4FuBpNIpZF-i8H5QEX6DzOZ-9WJDc7PwHQIul2cCsqb-Oj5qCAmyOSnudq6elckpI9_mgmhZhzH-1llRZq5OWpq-i2vtkwaOmk5VtEGYmcvY3dNdPjvWduk2q7gx-N4vkvYjArwwl9gDlEdFnoV95ysds8PqN6set7GZ-CxwiwSDKEiCFCtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اختلال در عرضه نفت عربستان؛ انتقام سخت از اروپا
🔹
تعطیلی خط لوله «شرق-غرب» عربستان در پی یک حمله، به لغو تخصیص نفت خام به اروپا برای ماه اکتبر منجر شده است.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3247212</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/692065" target="_blank">📅 20:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692064">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0EK2ndxQWP8dgyOmNtpLfDKWYvP1aiAXjRRH7uMpWh-SARzLDrZm72IU6JNB0IbMADpr9UIi_QpXo1uVoCSKWNzy-qok7QD2EyQZSrYZEqjCCxum1TBkjX8lz42p4CPma6b7gfOVXwJJ2-FtWT1Ih5EJX42ZK-v723dd08sU5DHxJlm-JC5x1bS9XfjpBTlOaV2PS0sMLLPsQnLRG0hRNa07-Hqulx3KZvYTNlApaGA_fcXQflwYLYt7hU6pnEceRuCpzVc85Q64c6XxK3NQ6QkJ859kP2v5GjOXBPMofGTTBSxJs-GrAvhYshrr6Khz9db94k9hNEVIBp9u4PUPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازتاب «جان‌فدا» در رسانه‌‌ی آمریکایی رویترز: تجمع نظامی جانفدا تهران را پر کرد
🔹
مقامات دولتی ایران گفته‌اند بیش از ۳۱۳ هزار نفر در این رزمایش شرکت کرده‌اند. در این رزمایش نمایشهایی از پهپادها ، سیستمهای ضدهوایی و سایر تجهیزات نظامی را در بحبوحه درگیری های مداوم ایران با امریکا و اسراییل را به نمایش گذاشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/692064" target="_blank">📅 20:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692063">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ترامپ مدعی شد: مذاکرات ما با ایران تا به امروز ادامه دارد و من معتقدم که با آنها به توافق خواهیم رسید
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/692063" target="_blank">📅 20:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692062">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fITJ8zwI8NjeV4-_GOsY7Xo4YtNt7IhahEU6cnGVDkeB5S2FdeBu_Dr6VnXAgYARBHqhbek0vOAOqJ8ohQ9JU5-gVF7W5wB2L2tbwDMn9MxRO1Gd_5HAQfULn9RoeopeQbk-X3_AVwrAUwdjMFRa3BgUCuu20P5zu2-xSrXM1xNYhc-YLLiVQaLck4w24ikxYx4W6JAW1SQ8L1CvrsuDGsUDHsi7d_SDEK7ekhvZ-wz6jg0BJikpMgVS2Rtfi6lPLR6utsLIkogjHgT1Tdfd_uMWDhJWMW7u5Xk-U04WQEg5BixOzdCdLi_-JxBfuSkpWh-PVWZtjSE4EMzzgJKPCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش مصرف اینترنت در اینستاگرام
🔹
با فعال‌کردن گزینه Data Saver از مسیر Settings → Data usage and media quality، می‌توان مصرف اینترنت اینستاگرام برای بارگذاری عکس و ویدیو را کاهش داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/692062" target="_blank">📅 20:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692061">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">17-2 Ane Manaee (1404-02-02)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/692061" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه هفدهم؛ بخش دوم
حجت‌الاسلام امینی‌خواه:
🔹
تجربه‌های نزدیک به مرگ، تلنگری برای بیداری دل‌ها. تجلی افعال حیوانی انسان در قالب چهره‌ حیوانات! [00:00]
🔹
مرگ، یعنی کندنِ انسان از تعلقات؛ یا اختیاراً دل می‌کنیم، یا به جبر خواهند کند [07:21]
🔹
تجربه‌ نزدیک به مرگ "ایمان"؛ روایتی از نشانه‌های باطنی، شهودی و شفاعت حضرت عباس علیه السلام [10:22]
🔹
"خوشمان نمی‌آید"؛ آغاز انکار حقیقت و تبعیت از هواست و عاقبتش "کرهُو ما أنزلَ الله"! [15:34]
🔹
تحلیل تاریخی-قرآنی، در تطبیق محتوای سوره مبارکه "محمد" با شناسنامه بنی‌امیه و نفی نگاه ابوسفیانی به دین [19:19]
🔹
تفاوت مؤمن و منافق؛ یکی قرآن در دل، آن یک قرآن بر سر. یکی مشتاق وحی، آن یک درصدد تمسخر و طعن [22:48]
🔹
انحرافِ نگاه منافقان به پیامبر (ص)، با زدن برچسب قدرت‌طلبی، ثروت‌جویی و زن‌بارگی به حضرت! دلالتیست بر «عَلَىٰ قُلُوبٍ أَقفَالُهَآ» [27:29]
🔹
تقوا نور هدایتگر و واکنش صحیحِ دل است به خیر و شر، و سرمایه‌ای برای پاسخ درست به نیازهای انسان [36:18]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/692061" target="_blank">📅 20:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692060">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b56d2c94b8.mp4?token=gMRd2cWHL6vVhkUhnbK6fK6bvHs5MVO-w4gaApRAJmk2Bq0AAcvRXIAGHRkdOjWZiOzNGItEZNOBAblruqLYKfJO0zbqHEcaVLmrDllyb6tGoHzS0suk1XbJn3b5gDC3V7OyJgGsgQu3QGUdJX-5S0cheOFYCJOrqOL-_l5mDBcUy0qpnsZpZpn-1WsKY_fuDTTX6GM9vRBTpJ9Oej8Og83uLE5O8dfqgmnFrNwfoUu_qEfyv2r5kXb8u7ZL5t2jqEaP4lXmk3rGxXv3_YHyZ5OxwTIFMBdwByQc19JKfLZ25xxzsRQCSbTrbKsE_IvzxFYrDEdIVEQXisFGAjW8h7JhHEwRLT5ao49PGbz0R7MC6wsdSQpg_DTEmm5aXYNoD3x7CbFKhom4DIIQVbNOXimCEoPeyxUsfyt9dMEGI3GA_MpKxH0wYhAYOEdBC9y3C93bS6pUX2Z80KeqQk4FsLsKBg-_ogy1KeFZhIJyEZGx_fSPoZI-MjD6GnkPsmRBI1cbHQYBkT5GJ01SEhj1IGP0BQ4zB6XfHkGEJgd_7oDUNgMi04p4RZ-onMED1K98jwq3FXJOl0mF2PgeXSUNbFnwSpACXB4ZtiXPA60BXwcFrXf0OxHzBPxg38j8Uzt7uUA7AVa0PkWy-FMD0JmAsHzM3NZxLSoS4qSKRd0UNpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b56d2c94b8.mp4?token=gMRd2cWHL6vVhkUhnbK6fK6bvHs5MVO-w4gaApRAJmk2Bq0AAcvRXIAGHRkdOjWZiOzNGItEZNOBAblruqLYKfJO0zbqHEcaVLmrDllyb6tGoHzS0suk1XbJn3b5gDC3V7OyJgGsgQu3QGUdJX-5S0cheOFYCJOrqOL-_l5mDBcUy0qpnsZpZpn-1WsKY_fuDTTX6GM9vRBTpJ9Oej8Og83uLE5O8dfqgmnFrNwfoUu_qEfyv2r5kXb8u7ZL5t2jqEaP4lXmk3rGxXv3_YHyZ5OxwTIFMBdwByQc19JKfLZ25xxzsRQCSbTrbKsE_IvzxFYrDEdIVEQXisFGAjW8h7JhHEwRLT5ao49PGbz0R7MC6wsdSQpg_DTEmm5aXYNoD3x7CbFKhom4DIIQVbNOXimCEoPeyxUsfyt9dMEGI3GA_MpKxH0wYhAYOEdBC9y3C93bS6pUX2Z80KeqQk4FsLsKBg-_ogy1KeFZhIJyEZGx_fSPoZI-MjD6GnkPsmRBI1cbHQYBkT5GJ01SEhj1IGP0BQ4zB6XfHkGEJgd_7oDUNgMi04p4RZ-onMED1K98jwq3FXJOl0mF2PgeXSUNbFnwSpACXB4ZtiXPA60BXwcFrXf0OxHzBPxg38j8Uzt7uUA7AVa0PkWy-FMD0JmAsHzM3NZxLSoS4qSKRd0UNpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رشیدی‌کوچی، نماینده سابق مجلس: مثل آدم گواهینامه موتور را به زنان می‌دادید!/ گشت ارشاد و ماجرای مهسا امینی نتیجه یک تصمیم اشتباه بود
جلال رشیدی کوچی، نماینده سابق مجلس:
🔹
گشت ارشاد کاری کرد که آن اتفاق افتاد و ماجرای بنده خدا خانم مهسا امینی پیش آمد.
🔹
فیلترینگ ایجاد کردند و ماجرای مافیای فیلترشکن درست کردند.
🔹
تنها نماینده ای که گفت به زنان گواهینامه بدهید من بودم.
🔹
اگر آن موقع گواهینامه می‌دادند الان زنان قانون شکنی نمی‌کردند که بدون گواهینامه سوار موتور شوند و نیروی انتظامی نگاهشان کند.
🔹
قانون در این باره اشتباه بوده است؛ مثل آدم خودت گواهینامه می‌دادی که امروز نگویند ما مجبورشان کردیم .
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/692060" target="_blank">📅 20:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692058">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c38a2196b2.mp4?token=RrneymVz3Z6gSragagQXDppPmY4MAkoNc-lbgFWUQFybEwg8ACh_a9Bf_zs2q4g_lb8d_G3a3ml_e5rB11VwDdRMpA-hRYcnTjPV9GdUV5O6KL-M6P_V4khTzzzV1H0o6NW6hmiKwyfZNVTGUwUdoXtdp2SAeOBXIb9KxQSnQIwY9b6IKSfAo6-RtnvLAAv6pBaUG4d0oqA9IyTGXZ3PtmIvaYkHyxZLSEfjOwh-LxIzV7nxKtFbR83JGJngKzrWQZxY6H7lhsfEpC8-k1mBzL7H0UP5vTZL7Ci4biloB1en09Sqm4N4hWTDoklmf-wx6JzTrH4pb1FY_O32QkXQSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c38a2196b2.mp4?token=RrneymVz3Z6gSragagQXDppPmY4MAkoNc-lbgFWUQFybEwg8ACh_a9Bf_zs2q4g_lb8d_G3a3ml_e5rB11VwDdRMpA-hRYcnTjPV9GdUV5O6KL-M6P_V4khTzzzV1H0o6NW6hmiKwyfZNVTGUwUdoXtdp2SAeOBXIb9KxQSnQIwY9b6IKSfAo6-RtnvLAAv6pBaUG4d0oqA9IyTGXZ3PtmIvaYkHyxZLSEfjOwh-LxIzV7nxKtFbR83JGJngKzrWQZxY6H7lhsfEpC8-k1mBzL7H0UP5vTZL7Ci4biloB1en09Sqm4N4hWTDoklmf-wx6JzTrH4pb1FY_O32QkXQSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۲۵ سال بعد از ۱۱ سپتامبر یکی از فرماندهان میدانی القاعده و داعش، سوار بر کادیلاک و با گارد حفاظتی وارد نیویورک شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/692058" target="_blank">📅 20:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692057">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc71aef13c.mp4?token=K1vUAxc8KV5JQfWJzO_Ipet4rrUnZ1xsnk9jc6Xo2hUQXAzCsx5E0n2RsuhNm-fUY3PbQPiTXtMQXdlddfPhICjMBQZc84bUCUIiCRvpoa5zXjCzYNQQNvPHQaHEiyZQry6sbzlBg5oh5ijYoe35nG01P2wEutvEycjAnbpKJ5lvB0s_jKjoH2YBsxhiaN9ImObdwKuL7XI92BPveM0Lb6b032hXyO4vP9gh23EK_OCHIFzbGB7mlEudcPg3FpNGPL9kMMO-aPavl5hBYR2dowL6Z2zaWjyrEnjmLoG1rH4YUHEJ6gqAoB6yj8jW72FUYAhjdvHwxmCa9f8iw1KHmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc71aef13c.mp4?token=K1vUAxc8KV5JQfWJzO_Ipet4rrUnZ1xsnk9jc6Xo2hUQXAzCsx5E0n2RsuhNm-fUY3PbQPiTXtMQXdlddfPhICjMBQZc84bUCUIiCRvpoa5zXjCzYNQQNvPHQaHEiyZQry6sbzlBg5oh5ijYoe35nG01P2wEutvEycjAnbpKJ5lvB0s_jKjoH2YBsxhiaN9ImObdwKuL7XI92BPveM0Lb6b032hXyO4vP9gh23EK_OCHIFzbGB7mlEudcPg3FpNGPL9kMMO-aPavl5hBYR2dowL6Z2zaWjyrEnjmLoG1rH4YUHEJ6gqAoB6yj8jW72FUYAhjdvHwxmCa9f8iw1KHmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
سرمایه‌گذاری را از همین امروز شروع کن!
✨
🪙
خُردخُرد پس‌اندازت را به نقره ۱۰ گرمی تبدیل کن و برای آینده‌ات سرمایه بساز
📈
💰
💎
نقره ۱۰ گرمی خاتم‌چی؛ شروعی کوچک برای یک سرمایه بزرگ
🚀
🤍
https://t.me/khatamchii
☑
ثبت
سفارش
و
مشاوره
خرید
:
📱
09120715100
☎️
02122477938
خرید
از
وب‌سایت
:
🌐
Khatamchi.com
▪️
@khatamad</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/692057" target="_blank">📅 20:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692056">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اگر قصد خرید دستگاه بدنسازی یا تجهیز باشگاه داری
👇
👇
🏋️
می‌خوای باشگاهت رو تجهیز کنی، ولی نمی‌خوای سرمایه‌ات یکجا خرج بشه؟
حتی به صورت از دم قسط و با کمترین پیش پرداخت ، باشگاهت رو راه‌اندازی کن.
✅
قیمت‌های مناسب و رقابتی
✅
۱ سال ضمانت کامل
✅
۱۰ سال خدمات پس از فروش
✅
تحویل حداکثر ۱۴ روزه
خرید و تجهیز بیش 300
محصول باشگاه
(مشاوره رایگان )</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/692056" target="_blank">📅 20:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692055">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf7dd0c45a.mp4?token=dnewg-smQ9yH04_DJvxTpURR-XUBABpsfIrIQsJfznBmJMetwZvtcWo8_Y2akhuBTpTIN_a6qW8Zldd6KLDseWfTKIgTMFv5H3qcgbyzIucMXMBCTgf32PDV5iZesa0KRrpprKZ9l_9fjkkxuM0Z12i8aQSW5ZSLhgdaQtKysw--MIuP3bMM3hYH43izymJCjLlIHLv0P7xS7mRHrLZIWHZq8p37pzQYQ_Ge7cmbz7rXRqVD-U7uSSH6uosiImJ0kjrNHIx-H0v1PTnZhcRqnPp0gN4wNFD4cLbzS8BK-nWWBCodjCuYeL0C-Y3twIk29rm9DJ3eJapRPHQw0Wk6IoR4wHJMdEBmUDwe506y7CVTLctzyUhu2HQMCM0JnOO2bLiBNQWcn2JTs954TpCZSbMqcmsMwgreO8o3zRvPVMXlX_zReSS97wTBzAuBAdJNisBvwbMluBqA5kOD11LNGs6jjRNvVDxH7zmvkzwex4-7yJIJftbA7SzwIqs4jf-GxnhXVYMb-dWMUJLEwvvFj0k2mE5Zt3wj50rhRWg1OR1H4REUye363WHA4WEwnO8WZmSZRL-Lld194tldWkzJ6rrRZw7FfIgi9dSgSkllcC5n1uNUTd8HRb_6nhiY1c1VPvGOyrV0qB6MYrSOGopXfGiTiA5qq8D9fjJgJhl-VzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf7dd0c45a.mp4?token=dnewg-smQ9yH04_DJvxTpURR-XUBABpsfIrIQsJfznBmJMetwZvtcWo8_Y2akhuBTpTIN_a6qW8Zldd6KLDseWfTKIgTMFv5H3qcgbyzIucMXMBCTgf32PDV5iZesa0KRrpprKZ9l_9fjkkxuM0Z12i8aQSW5ZSLhgdaQtKysw--MIuP3bMM3hYH43izymJCjLlIHLv0P7xS7mRHrLZIWHZq8p37pzQYQ_Ge7cmbz7rXRqVD-U7uSSH6uosiImJ0kjrNHIx-H0v1PTnZhcRqnPp0gN4wNFD4cLbzS8BK-nWWBCodjCuYeL0C-Y3twIk29rm9DJ3eJapRPHQw0Wk6IoR4wHJMdEBmUDwe506y7CVTLctzyUhu2HQMCM0JnOO2bLiBNQWcn2JTs954TpCZSbMqcmsMwgreO8o3zRvPVMXlX_zReSS97wTBzAuBAdJNisBvwbMluBqA5kOD11LNGs6jjRNvVDxH7zmvkzwex4-7yJIJftbA7SzwIqs4jf-GxnhXVYMb-dWMUJLEwvvFj0k2mE5Zt3wj50rhRWg1OR1H4REUye363WHA4WEwnO8WZmSZRL-Lld194tldWkzJ6rrRZw7FfIgi9dSgSkllcC5n1uNUTd8HRb_6nhiY1c1VPvGOyrV0qB6MYrSOGopXfGiTiA5qq8D9fjJgJhl-VzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی مطهری: علی لاریجانی چند ساعت قبل از شهادت، افطاری مهمان پزشکیان بود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/692055" target="_blank">📅 19:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692054">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08dd8bdd37.mp4?token=ewmMzFkurw9mGoG6WCZ3H1FxpjszLlie3CXfZAu_7je2XE3JYoj1gww5BhXGqJijnLFzBXQOAAIGzJ5bt9dflqDBhCoEdW7IIwdnMOrc8cpbzWKBLCi_sK_Z2SIleBsJawmddD3ztK9MdeR31vZAxdBoAWMyFa7IaN_17eTZIKj62mUeDGvcWxGMn-OVyRPDN4ZjBpfy4FqPjcLtCXAW6SvmLX0rNS9IrNHmK7Z5WfFGgpR-aMDPvgoQA9_pDFthbexDQAxneeyNlVF-SGpWIocF0kYV5lBWYHXgqNtW5MLYc6M4zfiuaGLlFp7PlmsRga-hSknNc3pnTyuqafgjKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08dd8bdd37.mp4?token=ewmMzFkurw9mGoG6WCZ3H1FxpjszLlie3CXfZAu_7je2XE3JYoj1gww5BhXGqJijnLFzBXQOAAIGzJ5bt9dflqDBhCoEdW7IIwdnMOrc8cpbzWKBLCi_sK_Z2SIleBsJawmddD3ztK9MdeR31vZAxdBoAWMyFa7IaN_17eTZIKj62mUeDGvcWxGMn-OVyRPDN4ZjBpfy4FqPjcLtCXAW6SvmLX0rNS9IrNHmK7Z5WfFGgpR-aMDPvgoQA9_pDFthbexDQAxneeyNlVF-SGpWIocF0kYV5lBWYHXgqNtW5MLYc6M4zfiuaGLlFp7PlmsRga-hSknNc3pnTyuqafgjKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از فردا ساعت کاری کشور تغییر می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/692054" target="_blank">📅 19:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692053">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a50921ed.mp4?token=SvEyZebcOUfyq48VP1338gmdDiYKyo4jcULsZfcg-jj7C0NcljT6AtDFAYGzgef9ZdDMG4ZKakOtreWdeSN3vRsLPYYS8bQANAJiQATS6CdzxsAP5NL7ndgVYsBpCwWUoR89RMWqt3QjUyIIcT6-2XxNRCNpTltkehMaHuR81jIzXOAJ0isNRzBhU-fDjtyxxKHF8TeMykW0IVuwziv5q2mv60nnOwdS1TsOWOLnxFRR2UCX3RlWtvntzpiwjc6Bvne_jkCIxvQ7_F84o9HmnhoDElF-p7MSMddBsSAwxHy5a6eMBhqd9721iYSdTP4sN6L3J8zfDtWzp6enM5SyiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a50921ed.mp4?token=SvEyZebcOUfyq48VP1338gmdDiYKyo4jcULsZfcg-jj7C0NcljT6AtDFAYGzgef9ZdDMG4ZKakOtreWdeSN3vRsLPYYS8bQANAJiQATS6CdzxsAP5NL7ndgVYsBpCwWUoR89RMWqt3QjUyIIcT6-2XxNRCNpTltkehMaHuR81jIzXOAJ0isNRzBhU-fDjtyxxKHF8TeMykW0IVuwziv5q2mv60nnOwdS1TsOWOLnxFRR2UCX3RlWtvntzpiwjc6Bvne_jkCIxvQ7_F84o9HmnhoDElF-p7MSMddBsSAwxHy5a6eMBhqd9721iYSdTP4sN6L3J8zfDtWzp6enM5SyiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیئت رژیم صهیونسیتی در جریان سخنرانی اردوغان، رئیس‌جمهور ترکیه در مجمع عمومی سازمان ملل، سالن را ترک کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/692053" target="_blank">📅 19:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692052">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
روبیو، وزیرخارجه دولت تروریستی آمریکا: درست است که قیمت بنزین بالا است اما اگر ایران سلاح هسته ای داشت، قیمت سه برابر می شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/692052" target="_blank">📅 19:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692051">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
استیضاح میدری، وزیر کار تصویب شد
🔹
در پی یک جلسه پرتنش چهار ساعته، نمایندگان استیضاح‌کننده احمد میدری، وزیر تعاون، کار و رفاه اجتماعی، از توضیحات وزیر قانع نشدند؛ به این ترتیب، طرح استیضاح میدری تصویب شد و برای بررسی در صحن علنی مجلس ارجاع خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/692051" target="_blank">📅 19:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692050">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mauIdanrkM4OriTpXJTxM29tJgZblgFoPbp-eC7jv0lpo7cJycIEk2ppXoUbVlA0RmATtYorCVIhuzRPSMauq7qZj-GDuUF8_21b-Cc8vxEHQAjNU4WZNdKI7BDq0f1VYEScOhwSKJsgoXvodni1A-7hKwBwUxKBipHWLP3kjHVqlT4pFfWQaq0yjmPO7EB8nAsxCDyXx9FgygHEj2nelWDanoIZXUOEJ_yEtKfyFFyZ3zpBY3PltvNQEiqPktO8EQHF3dCS6plrRNwHMvIp8pvlFD7PkD7dDx8dthCiA8b0NCvPHbUsLOOLo1gAY6xrdA3yQ5Iz7ODH1F2EM-8g7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای مصالح ملی
🔹
مسعود پزشکیان امروز در میانه جنگ ایران و آمریکا راهی نیویورک شد تا در مجمع عمومی سازمان ملل حضور یابد و مظلومیت ملت ایران، جنایت‌هایی که رخ داده و بی‌اعتمادی‌ها به آمریکا را برای دنیا بازگو کند. همزمان سخنگوی سپاه با بیان اینکه مذاکره به معنای سازش و صلح نیست، بلکه صحنه دیگری از جنگ است گفت که اگر مصالح ملی ما در این است که در کنار جنگ، مذاکره هم داشته باشیم، باید مذاکره کنیم. آمادگی صددرصدی برای جنگ، به معنای نفی مذاکره نیست.
🔹
هشتصدوشصت‌وهفتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/692050" target="_blank">📅 19:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692049">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Olk5_RJe1DU8H5ktss1e-89gJV0H_gt4kbHcHy6xI7m_1lEX2YF6b7a6QoE6MmTwS2QzH8nmX-7HGJx_XdlUdIcGVW4jiRR9gLTsOL41C3S87RcAxF145gRahR9iCRy-doxrAmVLBD5J0BpdZfJ9OtHa02JXEF_MGCZPcWWWoW5N7u-CVVA_KP2IOdw6J053GW8w139U4hQR2P6DDijG1tmD6gc-yg1uZJ1vHuf8bURMXoSDBZG1GkYDC6Fnp9Hw1XUOp_3AJrRR3EH32YjvF6HQf7W98Jk1JmyPghnSAbDNpfTpD-ImuXQYIlg9g85UHgXttB26eiL_3csY9Yzm5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تهران پرچم‌دار مهر
🔹
همزمان با روز پرچم و آغاز مهر، ابرپرچم‌های ایران در ۲۲ منطقه تهران به اهتزاز درمی‌آیند.
🔹
این رویداد با مدیریت سازمان زیباسهری شهر تهران با هدف گرامیداشت نماد ملی ایران، تقویت هویت شهری، ایجاد شور و همبستگی میان شهروندان و پیوند نمادین گستره پایتخت با یک پرچم برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/692049" target="_blank">📅 19:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692048">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
سخنگوی سازمان غذاودارو: کارهای واردات ۲.۸ میلیون دُز واکسن آنفلوآنزا انجام شده و مردم باید چند روزی صبر کنند تا وارد کشور می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/692048" target="_blank">📅 19:27 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
