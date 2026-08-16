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
<img src="https://cdn4.telesco.pe/file/djbIAeR2SgH0QLY90ep8InQ7S2x7dTt7vaf_Hd-HMmhSscdnBW5BfC4NoNUSKPvBdhwvqIILWFpVpype44retZSXUP-l0ki5J8aLZjlzHvcDk2t7Bcwy656O9lFQJT4hzJP96DDam0LdYPoV5GVhFQHrQtqI9CTL9OC8Jxy6XBQZf6O4wWLLdBsFxWUpTrbihJ8TY_6Dvt28k5uFD81sGVsSmK19bIdlDuDuaAQ3GA640CBurIiBkQjllf7pU-6GkdusZiEGhfFyDeX491J7XFkfugg_6ntBAuIu-LoDR9ftQ6v7bi8nWt2PhsCmw6kc_k1edCcizgizQ7QSnYfQNg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.15M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 17:44:02</div>
<hr>

<div class="tg-post" id="msg-681700">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3056fea164.mp4?token=KCMQWUQR5QRO6rBpob79hHJAehw4Wrh1OtkxkhGha3qu2u8lTGJ4aZdC6aAT3lImRObu2jLMpDZE_Kxwid3fkn5rhJdcD6-tDPvncEoTbFk2FwJN9aNkH3ByFpuK6gk1tx_MsGhgA5yYbS7wZbIewbnzZUusG-UBo3tXb7mBkySQt0_qJoZYy71NJYsEa2TEHxPSwZZzZq_-ronn92v3K5vnhBvWZfVEfT3e0v9ucr2FgualjFsvPB2IVyikN_Wb-abfGhYTFWluAPagJlw-Etp7L9_TGHcQCXgt-CzCTBbcbWalv5xvFFCQ3XC6vbYB16yOv7cQO-1tTCmuDB9D0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3056fea164.mp4?token=KCMQWUQR5QRO6rBpob79hHJAehw4Wrh1OtkxkhGha3qu2u8lTGJ4aZdC6aAT3lImRObu2jLMpDZE_Kxwid3fkn5rhJdcD6-tDPvncEoTbFk2FwJN9aNkH3ByFpuK6gk1tx_MsGhgA5yYbS7wZbIewbnzZUusG-UBo3tXb7mBkySQt0_qJoZYy71NJYsEa2TEHxPSwZZzZq_-ronn92v3K5vnhBvWZfVEfT3e0v9ucr2FgualjFsvPB2IVyikN_Wb-abfGhYTFWluAPagJlw-Etp7L9_TGHcQCXgt-CzCTBbcbWalv5xvFFCQ3XC6vbYB16yOv7cQO-1tTCmuDB9D0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هزاران مهاجر مراکشی تنها دو هفته پس از هجوم گسترده قبلی، دوباره تلاش می‌کنند وارد منطقه سئوتا اسپانیا شوند
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال کنید
👇
@AkhbareFori_Ar</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/akhbarefori/681700" target="_blank">📅 17:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681699">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
آکسیوس: میانجی‌ها همچنان پیام‌ها را میان واشنگتن و تهران منتقل می‌کنند، اما پیشرفتی نیست
آکسیوس به نقل از منابع آگاه منطقه‌ای:
🔹
میانجی‌های پاکستان و قطر همچنان پیام‌ها را میان واشنگتن و تهران منتقل می‌کنند، اما پیشرفت ملموسی حاصل نشده است.
🔹
پاکستان ارزیابی‌هایی خوش‌بینانه‌تر از واقعیت ارائه می‌دهد تا این تصور را ایجاد کند که روندی رو به پیشرفت وجود دارد؛ تصوری که می‌تواند به شکستن بن‌بست کمک کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/akhbarefori/681699" target="_blank">📅 17:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681698">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9stw2HyypcjOkY1UwUk-wRj3jYeaQAj5_iREQcW7yZ8hFk9x_AHeTZRU482Myk2hxHFH1o9_0CFFqmSRyvXxxsNH3he53sksnKOo1OEHgY7QcFze23qDEHzStvrNBYvsGefAlGtgWAE7nIS9Zq5nr6M9Qimy3Kg30sLaTUeiK_9w_5oP04D83SHeR8Q8A_hMi5Bd1IRT7sl2d0B0XgTY3U206X5DwGqZ1z031TQyHdDMq8Yu56DiA7BOUxhac1NHJymNh6JD_EWVbzNM13PfYIVkjC12OzDSBfTtNty04VuzJTaTIL543ayAtiNK-bXQqbC0FkwMYS1gThodJQbEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پای کار «خاک ایران» / ۱۰
🔹
رکوردشکنی بانک کشاورزی در پرداخت قرض‌الحسنه؛ رشد ۶ برابری در سه سال اخیر
🔻
مبلغ تسهیلات قرض الحسنه پرداختی بانک کشاورزی با جهشی چشمگیر از ۷۰ هزار و ۵۴۶ میلیارد ریال در سال ۱۴۰۱ به ۴۱۳ هزار و ۸۸۳ میلیارد ریال در پایان سال ۱۴۰۴ افزایش یافته که نشان‌دهنده رشدی ۶ برابری در سه سال اخیر است.
🔻
این بانک در چهار ماهه نخست سال ۱۴۰۵ نیز با پرداخت ۱۷۱ هزار و ۲۲۶ میلیارد ریال تسهیلات قرض‌الحسنه، روند رو به رشد حمایت از متقاضیان این تسهیلات را تداوم بخشیده و ۶ برابر نسبت به مقطع چهارماهه ۱۴۰۲ افزایش عملکرد داشته است.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/681698" target="_blank">📅 17:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681697">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bybh-GGMrqUD_nqIWDUqQeoqtYEAyRvrgYiWgqwojGte5o_ZHw-QBzh7O2NdaRDq2J-o_-g8Syq7VqO_b-OjW5PGwUHgB4NOv5vl-PYuewv2w2xG0YvF_TosfTZ8yodQEAyAuU8sMareLtsgL1osXYqkS0FteU5WJIqwMPu-Ltc2V9K1MglbqkOWaIvbPntJfK2-ZlmIamhO0GJs7mUgeesyuD1TC50wv50cWff7toQLD0kRJJx1JPSZCibHW-9zeSHGQqyWMAVCx8hhSzNFdcFFH2TXVjqB-IjtSQNZBJPkR4YaSH0mtxXWibJZN5coZlgBmYEEozH7VF2w5381mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از گوشی جدید ۶۶۰۰ نوکیا که از سری کلاسیک خود الهام گرفته
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/akhbarefori/681697" target="_blank">📅 17:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681696">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
بیداد کارت‌های بازرگانی اجاره‌ای؛ ۲ میلیارد دلار ارزی که تبخیر شد!
«سلیمی» عضو هیئت رئیسه مجلس:
🔹
کارت‌های اجاره‌ای بازرگانی بیداد می‌کند و ۳۵ درصد تعهدات واصل نشده ارزی مربوطه به دلیل همین کارت‌های اجاره‌ای است؛ سؤال این است که چرا دولت برای اجرای این قانون ورود نکرده است؟
🔹
قوه قضائیه حدود ۳۰۰ کارت اجاره‌ای را کشف کرده که به میزان ۲ میلیارد دلار است و این مسائل نیازمند توجه جدی است و باید با این مسئله برخورد شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/akhbarefori/681696" target="_blank">📅 17:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681694">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCCfeS0YsNBzyqOowkU2QWFaAGH1dhvwWWI1Y6r8d2qDgY0hqBFSvb1DAtQfnVkN8Sb00FHWUXOy1z4gJ80PMUTPKWjYy1IdJQS2U0ghdOzRlj627l8q-UaYqTMrsJlJHoBym2D8ZjD-34Fa9NzLJuCApMchWKvq_shUWF-ZkADeZqeZzawsAtBoy44FIFzIP2nL9kVO-V5UnKKEAX0uOVQHar06d3q8RvSPiaxd_WY_sOhFjljlgYdTgYyXB0Kb7dTnrjrjreSxlQu3eK72aZP_nGOvfdbY2eKxyFEW1MozmNIJtbniQGLoFp8qGUHDhB4wgCZKiDzC9BFdl6b8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین بازارهای سهام جهان
🔸
آمریکا با ارزش بازار ۶۹.۸ تریلیون دلار، با فاصله‌ای چشمگیر صدرنشین بازارهای سهام جهان است.
🔸
پس از آمریکا، چین با ۱۱ تریلیون دلار و ژاپن با ۶.۷ تریلیون دلار در رتبه‌های دوم و سوم قرار دارند.
🔸
نکته قابل توجه این است که از ۱۲ بورس برتر جهان، ۶ مورد آن در آسیا قرار دارند که نشان‌دهنده سهم بالای این قاره در اقتصاد جهانی است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/681694" target="_blank">📅 17:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681693">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای رادیو ارتش رژیم صهیونیستی: ارتش در حمله‌ای در خان یونس، یک فرمانده گروهان حماس و در نصیرات، یک فرمانده جهاد اسلامی را هدف قرار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/akhbarefori/681693" target="_blank">📅 17:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681692">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/101ad9a6f4.mp4?token=WQFKA3FuZ0LIqTCCiRr30vECHRNcA1J3y5Ewv7303CYZVwHtgXd7iV6tKZyG2qRxpNlgHijYQOgk5jx1o8ciCtYcL74uKsHB6mPIA2iZVGsHNFsFK5srZJsQ1L39bBEApHNpeOfE2Ui8pLBQjXC3RJq_6vmQ1RdwJeRELiKPSvuIe3BAQR4uwLK3fDEdulSrUKrEOrkcrFy_oJszbRa6SJXmIFeI0ug1TnjrmNn16llpXl3wrYQdR6rv7baa0sPUHOHv-mu38TCEtxTQfeI3cNKKT88E1uXmXu6ISC7GP8nGcLRXJk5tzTeapKLvKE-26bB4gbdBNnRjFLc6di4vng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/101ad9a6f4.mp4?token=WQFKA3FuZ0LIqTCCiRr30vECHRNcA1J3y5Ewv7303CYZVwHtgXd7iV6tKZyG2qRxpNlgHijYQOgk5jx1o8ciCtYcL74uKsHB6mPIA2iZVGsHNFsFK5srZJsQ1L39bBEApHNpeOfE2Ui8pLBQjXC3RJq_6vmQ1RdwJeRELiKPSvuIe3BAQR4uwLK3fDEdulSrUKrEOrkcrFy_oJszbRa6SJXmIFeI0ug1TnjrmNn16llpXl3wrYQdR6rv7baa0sPUHOHv-mu38TCEtxTQfeI3cNKKT88E1uXmXu6ISC7GP8nGcLRXJk5tzTeapKLvKE-26bB4gbdBNnRjFLc6di4vng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت تصویر پلنگ ایرانی و توله‌اش در پناهگاه حیات‌وحش «کم‌کی» بهاباد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/681692" target="_blank">📅 17:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681691">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-r1drCl_2veJOrMZFAW7Iy-d1BePSyuzJI0IR8YuP0hhZzA51Y7-5zBgeVdnLKclGYbW3lYQ1dSL_VKnTL2XRMFko4JidHniaKPkCrCa72QdMJlm24cIDHZbkAv1b1Myz1smIsJO5II1gX4U4zJgi-2sgS9IoPzOG0QOG_xOApiFFoZYZyCV2wgGccnOlJPtlnvCRxjfJLuxjxjDpRbYJ5Z-DYrKk2LXJERo91RyXfSeq_u648Z8CrXxG6IvZE_1gvJCmTV3xtpi88794BymsGF48F0vwGLZ_1ojbKyExoSAyymaraMSLR2i0kH4A_susU2WzyKhTQ0xaWopTyGug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
داماد ترامپ با سران حماس دیدار می‌کند
🔹
جرد کوشنر داماد ترامپ با حضور میانجی گرانی از مصر، قطر و ترکیه، با نمایندگان حماس در قاهره دیدار خواهد کرد.
🔹
در همین رابطه، شبکه تلویزیونی سعودی «الحدث» مدعی شد که جرد کوشنر داماد و فرستاده دونالد ترامپ رئیس‌ جمهور آمریکا، با نمایندگان حماس و با حضور میانجی گرانی از مصر، ترکیه و قطر دیدار خواهد کرد./ مهر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/681691" target="_blank">📅 16:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681690">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c1975151.mp4?token=imgW3RoHBOTXdDhYa4F-jgNabKbVgmEl2D1ZhSkDoDa_28_GsKdjs62k9i1KcXG37joqLIkKY0KoPoOH84tcvhzj9Cmjsm72VmlKioycxgjUl7MwUP6DIYSj7INAIa4lUqBV2B6uS2w39ulUvKYVk0OAope8QiuyqY2rVo4m36bGaKxC3TF-5VyNql29GUJRVvsQ-jpB_3DIcx7BVmXi9Hdf6iRmxzI7li2v9-NOaw36wWBvpjlSaqsdREQ6HcNypkCm75k60WD1JaUYDH3J9wsFWpPwPtpxvjEniHrXPvQNwXIFMxoDZyXiGoDYSqamC8c6wssAgS1S9PBe9AffUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c1975151.mp4?token=imgW3RoHBOTXdDhYa4F-jgNabKbVgmEl2D1ZhSkDoDa_28_GsKdjs62k9i1KcXG37joqLIkKY0KoPoOH84tcvhzj9Cmjsm72VmlKioycxgjUl7MwUP6DIYSj7INAIa4lUqBV2B6uS2w39ulUvKYVk0OAope8QiuyqY2rVo4m36bGaKxC3TF-5VyNql29GUJRVvsQ-jpB_3DIcx7BVmXi9Hdf6iRmxzI7li2v9-NOaw36wWBvpjlSaqsdREQ6HcNypkCm75k60WD1JaUYDH3J9wsFWpPwPtpxvjEniHrXPvQNwXIFMxoDZyXiGoDYSqamC8c6wssAgS1S9PBe9AffUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دردسرهای تسلا در هندوستان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/681690" target="_blank">📅 16:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681689">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
تیزر قسمت سی‌ودوم از فصل پنجم
🔹
در این قسمت تجربه‌ نزدیک به مرگ دو خانم نوجوان با محدوده سنی ۱۰ سال به نام رضوانه که در حین تمرین سرود بر مزار شهدا روح از بدن جدا و توسط ۴ فرشته به آسمان عروج کرده و با رؤیت و دعای فرد سبزپوش با شکافی بر فرق سر، به جسم باز می‌گردد و خانم ریحانه که بخاطر سرماخوردگی شدید در حین استراحت در منزل، روح از جسم ایشان جدا و تجربیات جدید و شنیدنی را درک می کند؛ نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گران
: رضوانه عرب نظرگاه/ ریحانه رشیدی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/681689" target="_blank">📅 16:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681688">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس مرکز رسانه مجلس: جزئیات طرح مقابله با نفوذ بیگانگان هنوز تصویب نشده است.
🔹
دادستان فیروزآباد: اخبار ربایش کودکان صحت ندارد/ تشکیل پرونده قضایی برای منتشرکنندگان اخبار کذب
🔹
خبرگزاری رسمی عربستان: هشدارهای حملهٔ هوایی در جازان فعال شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/681688" target="_blank">📅 16:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681687">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/220b7dc3df.mp4?token=W_FNeq9GOQ7hAgSlgT9foVC2zcAUKTDHpPTRNEhPGNdjLnA9D-0mzmmLyHHzxH6XB4S5dJUM1Pymfu31krh6xz7iOQutumNkAj7iIqe45jYcCa2CfNlFRIvSZWUlvsxytHqNu-vmIEwZjDyXPs6wAWtsCjlxS3Ymj9K0CR39HMwbCHo5t5jV8NLAI63-71O_JnB5LpaPeoAcc5Q6GFhJsewxJnY_KGl0BzpELj4DOWDvtAvkRVVJwp8vH57z9yL2qu_c1bzB9IziymjET4xDCPwVAS8f4URtL97US5Ke2C7Cl4fTHSWofvf1khGslXGtCkh7BIRZko9KsNLfeiYDlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/220b7dc3df.mp4?token=W_FNeq9GOQ7hAgSlgT9foVC2zcAUKTDHpPTRNEhPGNdjLnA9D-0mzmmLyHHzxH6XB4S5dJUM1Pymfu31krh6xz7iOQutumNkAj7iIqe45jYcCa2CfNlFRIvSZWUlvsxytHqNu-vmIEwZjDyXPs6wAWtsCjlxS3Ymj9K0CR39HMwbCHo5t5jV8NLAI63-71O_JnB5LpaPeoAcc5Q6GFhJsewxJnY_KGl0BzpELj4DOWDvtAvkRVVJwp8vH57z9yL2qu_c1bzB9IziymjET4xDCPwVAS8f4URtL97US5Ke2C7Cl4fTHSWofvf1khGslXGtCkh7BIRZko9KsNLfeiYDlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مراحل ترمیم و پرکردن مجدد دندان آسیاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/681687" target="_blank">📅 16:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681686">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a78839f85b.mp4?token=Y-HR6-1QuykEcA9y992bvr2udcL79dTKCgqvS5yQ1Rl1mCRRlZaJ_y9IFtPt38VvftDKykC9ksN0g6G0cVcxrmmnkZCwUEYzx7485ArB2mDM1GmZhMw-kowDYUcHFRrlrbFLkXAOBT34NOT7pblEqt4YoVtSbtrHux3rrh2COuC0vNQxSZGXACTgTu7OY0g1LP3i7cDeQYB7sVklyeo1aO3IQIiQKUUUGGpGnbFyivog6w0VnvH-ulX3ZdZ0cFz8so7SmU_ES_9SBNBDWmh2W31yHK2fDk9-iHmEC36WpnjMtI70qMKq0Bnc51dJ7RJeTO_bB2rMymv1y4L26Df5wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a78839f85b.mp4?token=Y-HR6-1QuykEcA9y992bvr2udcL79dTKCgqvS5yQ1Rl1mCRRlZaJ_y9IFtPt38VvftDKykC9ksN0g6G0cVcxrmmnkZCwUEYzx7485ArB2mDM1GmZhMw-kowDYUcHFRrlrbFLkXAOBT34NOT7pblEqt4YoVtSbtrHux3rrh2COuC0vNQxSZGXACTgTu7OY0g1LP3i7cDeQYB7sVklyeo1aO3IQIiQKUUUGGpGnbFyivog6w0VnvH-ulX3ZdZ0cFz8so7SmU_ES_9SBNBDWmh2W31yHK2fDk9-iHmEC36WpnjMtI70qMKq0Bnc51dJ7RJeTO_bB2rMymv1y4L26Df5wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وام گرفتن همیشه راه نجات نیست، اگر می‌خوای وام هوشمندانه بگیری این ترفندها رو از دست نده #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/681686" target="_blank">📅 16:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681685">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس هیئت نظارت بر انتخابات شوراها: انتخابات شوراها ۲۴ مهر برگزار می‌شود.
🔹
دانشگاه شریف: حکم اخراج رضا دالمن، دانشجوی اخراجی برای اجرا به دانشگاه ابلاغ شد.
🔹
یکصد و پنجاه و سومین حراج شمش طلا ۲۷ مردادماه برگزار می شود.
🔹
احتمال شنیده‌شدن صدای انفجارهای کنترل‌شده در خمین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/681685" target="_blank">📅 15:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681684">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
تداوم حملات موشکی و پهپادی یمن به محل تجمع مزدوران عربستان
🔹
خبرگزاری رسمی یمن (سبأ) امروز به نقل از یک منبع نظامی خبر داد نیروهای مسلح این کشور باز هم خسارات سنگینی به مزدوران عربستان سعودی وارد کردند.
🔹
این منبع می‌گوید نیروهای مسلح یمن در جریان حملات پهپادی و موشکی، محل تجمع مزدوران سعودی را در منطقه «المخا»‌ و استان «مأرب» هدف قرار دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/681684" target="_blank">📅 15:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681683">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2feda353eb.mp4?token=gZant8ZYvcAXIk-rNwTaFd0iVwgV3NAFUfO7hY_g3Bsa7cMKpneFZvBcNIT6ndliGYdiD1hpTjHONUAvzrY8ynLFcYvKwySIupkv-iR_u_jjtEUSkrQDiqz9wZ5VoqZtxNFAJPEhk9onA8Z80s0R7tpFh7xeVCNJq6BvxlT6squakBnrpApN6OXE_eIeiNquXRxWfunM33J42PTVckM4QGSKwnVSTaiO95SKsvcIY_9p5Xk94OLxEQNoTST2TswfxMcmczZfnUe1OgvwYouVnjUWYMoKPrhB02fF6kWvuUP282nfB8hOWn47vOOeA6gKR-G0UPUEbyYHeJkfvDKtGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2feda353eb.mp4?token=gZant8ZYvcAXIk-rNwTaFd0iVwgV3NAFUfO7hY_g3Bsa7cMKpneFZvBcNIT6ndliGYdiD1hpTjHONUAvzrY8ynLFcYvKwySIupkv-iR_u_jjtEUSkrQDiqz9wZ5VoqZtxNFAJPEhk9onA8Z80s0R7tpFh7xeVCNJq6BvxlT6squakBnrpApN6OXE_eIeiNquXRxWfunM33J42PTVckM4QGSKwnVSTaiO95SKsvcIY_9p5Xk94OLxEQNoTST2TswfxMcmczZfnUe1OgvwYouVnjUWYMoKPrhB02fF6kWvuUP282nfB8hOWn47vOOeA6gKR-G0UPUEbyYHeJkfvDKtGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرمانده کل ارتش خطاب به ترامپ جنایتکار: غلط میکنی می‌گویی تنگه هرمز برای آمریکاست
سرلشکر حاتمی:
🔹
رئیس جمهور جنایتکار آمریکا می‌گوید که میخواهد تنگه هرمز را بخشی از سرزمین جنایت، اعلام کند، شما خیلی غلط می‌کنی! او بعد از آنکه واکنش‌ها را دید، اعلام کرد که شوخی کرده است.
🔹
شوخی این حرف هم، غلط زیادی است چراکه اینجا ایران است و حافظانی دارد که قلم پای شما را خواهند شکست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/681683" target="_blank">📅 15:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681682">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8ab5c22b7.mp4?token=IO_nQRYZq-czv9Q3Z9YBNr96n1EXYNIlYmttDpVx11TASMGa4IbX_OdnNyBb6PiMRptmf47sM68S6tIzGF5WC8oikoBNhMziamP8VxwJWTu_lJL6PrAamjbMqU0rpsrTKL0z9yPZ3KU8QuzJADNFWN22Gh0hQTR08vGF2OyeC_Tev7HqQctW14qT32NPTNJz8Z_IwxHPWlZ4bTUj2lcVyfcq6_RPDl1iRxYTN2dvnvriv2W5jb5WAwFEq39_1TjggMpczejIGiKQbYAH6Ay-Kb3NldivML8lnUVXmUZB9FNOOe08zrWhSeAsJ0NDSDKn2_LxcR6bTttZqUh6jvAdtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8ab5c22b7.mp4?token=IO_nQRYZq-czv9Q3Z9YBNr96n1EXYNIlYmttDpVx11TASMGa4IbX_OdnNyBb6PiMRptmf47sM68S6tIzGF5WC8oikoBNhMziamP8VxwJWTu_lJL6PrAamjbMqU0rpsrTKL0z9yPZ3KU8QuzJADNFWN22Gh0hQTR08vGF2OyeC_Tev7HqQctW14qT32NPTNJz8Z_IwxHPWlZ4bTUj2lcVyfcq6_RPDl1iRxYTN2dvnvriv2W5jb5WAwFEq39_1TjggMpczejIGiKQbYAH6Ay-Kb3NldivML8lnUVXmUZB9FNOOe08zrWhSeAsJ0NDSDKn2_LxcR6bTttZqUh6jvAdtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله خونین با چاقو به نگهبانان بیمارستان مدنی کرج!
🔹
فاجعه در ساعات غیرملاقات؛ همراهان یک بیمار که قصد ورود با زور و خارج از وقت قانونی به بیمارستان مدنی کرج را داشتند، پس از ممانعت نیروهای حراست، با چاقو به نگهبانان بی‌دفاع حمله کرده و آن‌ها را شدیداً مورد ضرب و شتم قرار دادند!
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/681682" target="_blank">📅 15:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681681">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guaUGByhkayXSkNUR9bCeZXWE4xmIQytPoglNkr_5iVTdjzcB3SJn78TG5kuVnwKIzNnsDmDY-FsZQ6tEW3KUKF3DQNdPwMKFR1aHREgKRxHoXcNuQgokA9uP2AsnF3tCZMDwq2ZvwFugWIas6SemllsmDQWrtD9yMr_LtbpU9p0FC6JBaRQwG_4gH0C_Ck4fxR5CdGZJJegz1gE64h3mYPOgQQx8kxwDZizK8d6HncL8YJpT4dRSeTVuCAw-rKw9q_if07og8d4osvJHEZjvMgDA0tw-3k-kpo2od3VxLmv2l9dywOXnODHw21B8WK3RfLWkP7L4bsJyDvDxKBrIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاوش ماه بدون دخالت انسان ممکن می‌شود
🔹
ناسا قصد دارد سه ماه‌نورد کوچک را به ماه بفرستد که تنها یک دستور دریافت خواهند کرد: خودتان بین یکدیگر تصمیم بگیرید که چگونه یک منطقه از سطح ماه را کاوش کنید.
🔹
این سه ماه‌نورد حدود دو هفته را صرف نقشه‌برداری از سطح ماه به ‌عنوان یک گروه خودهدایت‌شونده خواهند کرد.
🔹
هیچ انسانی نیز قرار نیست هر حرکت آنها را تایید کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/681681" target="_blank">📅 15:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681680">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
چرا خاموشی‌ها دقیقاً مطابق جدول زمانبندی اعمال نمی‌شود؟
معاون برق و انرژی وزارت نیرو:
🔹
برنامه اعلام شده از طریق سامانه برق من یک برنامه احتمالی است و در صورت بهبود شرایط شبکه، خاموشی پیش‌بینی شده اعمال نمی‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/681680" target="_blank">📅 15:21 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681679">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFwV-n9tVSM3TZSZZzZmHxSoAjg7iKAuAJ7181zIKy2Pn_7s-3nc_sO6_9AbPtVgtxyouDpN2ew3UJMBCujDrcjwHHgx4qAv_jLXVWjGerHP4uZx-tK9FAxLf9acPN-Clm_dQ284uB1_k4Ied5SerqFuWnJS43NzON_Dff-WHnoIpPuaAp79wDp5iQo6v_HEches4pMq-wQmdQaADWmSARZ8SS0oyFCZIHppoMDGgWPDRx2zGEP0XPCzH1F12Rp_pGo97mRW4B3muN2Yh-XZn1xLnIjE3bOlXZH0-Upa4TJsO0F6BDBjNvwb8UKD_ZOfJ1iU7oyz9Jmxi72w7zWmaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویژگی مشترک ۱۵ میلیون ساله؛ میمون‌های بزرگ همگی مثل انسان می‌خندند
🔹
پژوهش‌های جدید نشان می‌دهند که میمون‌های بزرگ مانند انسان‌ها از شدت خنده کنترل صوتی خود را از دست می‌دهند. تحلیل خنده‌ی اورانگوتان‌ها، بونوبوها، گوریل‌ها و شامپانزه‌ها حاکی از وجود ریتمی منظم و هم‌فاصله در انفجارهای صوتی آن‌هاست. این ویژگی مشترک احتمالا از نیای مشترک انسان و این گونه‌ها که ۱۵ میلیون سال پیش می‌زیست، به ارث رسیده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/681679" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681678">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما مهم‌ترین عامل گرانی مسکن در ایران چیست؟</h4>
<ul>
<li>✓ تورم</li>
<li>✓ دلالی و سوداگری</li>
<li>✓ عدم نظارت جدی بر بازار</li>
<li>✓ افزایش تقاضا و رشد جمعیت</li>
<li>✓ کمبود ساخت‌وساز</li>
<li>✓ نگاه سرمایه‌ای به مسکن</li>
<li>✓ افزایش قیمت مصالح</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/681678" target="_blank">📅 15:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681677">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بورس انرژی از عرضه بنزین سوپر در معاملات ۲۸ مرداد با قیمت هر لیتر ۸۹ هزار و ۷۰۰ تومان خبر داد.
🔹
پزشکیان: در روش‌های آموزشی باید به معلمان و مدیران مدارس اختیار و آزادی عمل بیشتری داده شود.
🔹
سوریه پروازها به مسکو را از سر گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/681677" target="_blank">📅 15:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681676">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f46c059e4f.mp4?token=mxKyNGVuD4AC4DMxDpJnk4sxQEB0sDh0wGcUr6XpsWOcuBGehn8zjwZR5LIWW-OKTCbydUCbSzDTlJELfgrBVCS62p3gZZR_8Kss-tJhcsAvZz3VCFak5sXLPP16qFKX6Itmls3JoDc5LiMD59oG8v958Gzms-dpf_TScSlz0lgsdYz67-8eANmnI8ApNTJTZ3RxfE2h9kI0ppFmR8Vhi4p2jNaj0BNzTwHXqEgGofyOjNMOyMAcga8VRBoREiyotov4tRBOB0N4v1Gm3BUJvKpk0TGdt-9993H0C9KnXkgMeTdw0mUT090c6HH9XVCC58dGGujxozLlILEcTVThGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f46c059e4f.mp4?token=mxKyNGVuD4AC4DMxDpJnk4sxQEB0sDh0wGcUr6XpsWOcuBGehn8zjwZR5LIWW-OKTCbydUCbSzDTlJELfgrBVCS62p3gZZR_8Kss-tJhcsAvZz3VCFak5sXLPP16qFKX6Itmls3JoDc5LiMD59oG8v958Gzms-dpf_TScSlz0lgsdYz67-8eANmnI8ApNTJTZ3RxfE2h9kI0ppFmR8Vhi4p2jNaj0BNzTwHXqEgGofyOjNMOyMAcga8VRBoREiyotov4tRBOB0N4v1Gm3BUJvKpk0TGdt-9993H0C9KnXkgMeTdw0mUT090c6HH9XVCC58dGGujxozLlILEcTVThGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون وزیر نیرو: به دلیل سنگین شدن بهای برق در بازه‌های دوماهه، در دستور کار است تا دوره صدور قبض‌های برق به یک ماه برسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/681676" target="_blank">📅 15:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681675">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/325c72fcbd.mp4?token=gFV5WOFpaROccu37vjJ6tA2lmWBbOHrEqpOCKurarDHwgyvkg91B_fHMEG7UBE6L0IawsyW1CyM9O4OrhXkRUMG3SLbXZlaS1PXkd5rKXpqFWHXTEYOOmXUKu22NCNGyijLeobx6mDykDlubWiJA8D9Z6fX7lvgEEvSqeqebmH_XYa0l0Pf2leFZPBJLZ8kYRCjTBOCDX1f0G0vY_DHE9BZEj98PXKUnigyoF-GzNSn0V12bc6l9GhqrUUCN4OaSDR8VHNCDf9NwK_gyy9v0u5Yllk-bEpFaM940Z2HnIF0HrzYYnxIp1AZw3d61fUPUuqv4aufM66fAmNgHdXl5LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/325c72fcbd.mp4?token=gFV5WOFpaROccu37vjJ6tA2lmWBbOHrEqpOCKurarDHwgyvkg91B_fHMEG7UBE6L0IawsyW1CyM9O4OrhXkRUMG3SLbXZlaS1PXkd5rKXpqFWHXTEYOOmXUKu22NCNGyijLeobx6mDykDlubWiJA8D9Z6fX7lvgEEvSqeqebmH_XYa0l0Pf2leFZPBJLZ8kYRCjTBOCDX1f0G0vY_DHE9BZEj98PXKUnigyoF-GzNSn0V12bc6l9GhqrUUCN4OaSDR8VHNCDf9NwK_gyy9v0u5Yllk-bEpFaM940Z2HnIF0HrzYYnxIp1AZw3d61fUPUuqv4aufM66fAmNgHdXl5LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای چین‌های یکدست این ترفند رو یاد بگیر
🔹
یک‌ترفند کاربردی برای علاقه‌مندان به خیاطی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/681675" target="_blank">📅 15:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681674">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeYsuUd8gxym14whn0amBGLbkKfN7ud7j1oFyFGNNYeoZeoWzW0nJ_w0bnCJNf7qznhEAVePu6d6aCMoBlvrFw4Fy5Tde9zhMtjHNDRFAZwBalMHQdcrB_uDnTb3ECXDSnAoKGPafbMvBBD2S05VwkXuihiGvsyD1EsDk4DbpsTIfiFypn4ENSuz87rNNVoc1n1rFSzPaYxzqXqBrUJ-Z5I3yBh6w6shLEqBOZos3WrqFz05BO9QDYlS3rJ5JdVfObcdc7fMjOEL1WhsiddvjpBQRzMPrDylssWo5axFr2lhRDDYic57ZpHYpXWJzQpFyWacLarT5ZVLtN-tzO28WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماینده مردم قروه و دهگلان در مجلس:
زمان بازنگری در ممنوعیت واردات ۴ قلم لوازم خانگی رسیده است
🔹
محمدرسول شیخی‌زاده، نماینده مردم قروه و دهگلان و عضو مجمع نمایندگان استان کردستان، با انتقاد از ممنوعیت واردات چهار قلم لوازم خانگی، این سیاست را شکست‌خورده دانست و گفت ادامه آن علاوه بر محدود کردن بازار و افزایش فشار بر مصرف‌کنندگان، درآمد رسمی مرزنشینان را کاهش داده، قاچاق را گسترش داده و درآمدهای گمرکی و مالیاتی دولت را نیز کاهش داده است.
🔹
ممنوعیت واردات لزوماً مانع ورود کالا نمی‌شود؛ بلکه مسیر ورود غیررسمی و قاچاق را هموار می‌کند.
🔹
از نیمه اردیبهشت، میزان واردات رسمی چهار قلم لوازم خانگی حتی از مسیر کولبری، ملوانی و ته‌لنجی صفر شده است.
🔹
محدود شدن تجارت قانونی مرزی، بخشی از درآمد رسمی مرزنشینان را کاهش داده و فشار مضاعفی بر معیشت آنها وارد کرده است.
🔹
ممنوعیت واردات باعث شده مردم به کالای باکیفیت و متنوع دسترسی کمتری داشته باشند و هزینه تأمین کالا برای خانوارها افزایش یابد.
🔹
وقتی واردات از مسیر رسمی انجام نشود، دولت از درآمدهای گمرکی و مالیاتی محروم می‌شود.
🔹
ادامه ممنوعیت واردات، بیش از آنکه به نفع تولید و مصرف‌کننده باشد، در عمل به ضرر هر دو تمام شده است.
🔹
زمان آن رسیده است که ممنوعیت واردات لوازم خانگی جای خود را به یک سازوکار شفاف، هدفمند و مدیریت‌شده بدهد.
🔹
این سازوکار باید ضمن حمایت واقعی از تولید داخلی، مسیر قاچاق را محدود کند، درآمدهای رسمی دولت را افزایش دهد و امکان استفاده مرزنشینان از ظرفیت‌های قانونی تجارت را فراهم آورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/681674" target="_blank">📅 14:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681673">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
تخلفات پلتفرم‌ها در فروش اینترنتی دارو
رئیس سازمان غذا و دارو:
🔹
‌سازمان غذا و دارو برای جلوگیری از فعالیت یا برخورد کلی با پلتفرم‌های فروش اینترنتی منع شده است و اجازه برخورد مستقیم با این پلتفرم‌ها در همه موارد به ما داده نشده است.
🔹
امروز برخی پلتفرم‌ها با تخلفاتی از جمله گران‌فروشی و عرضه داروهای خارج از فهرست مواجه هستند.
🔹
وزیر بهداشت نیز درمورد این موضوع نامه‌ای به رئیس‌جمهور ارسال کرده است‌.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/681673" target="_blank">📅 14:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681672">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjSfyY17bJQYk8nCGuBcKCgtxxkqPNrd4kckhVG8EqWPxHd4SJChYCQ4ZMD6Pl6VaAzuLrYydfl9yuIAngEiTFpY-dRY8af6xUuzJPTm9DxM1exI64lCAqhg2dLT98xnNWAgaecZRgdb5Krt_XIXD8lO5ep-K-bfKagtazpTexPiiY3I9M3PWwtRp-QdAzmj-QmGj9w8u-VHWng_oxDVPPsx0rctDWB9k5Viweb33exHQNHhMJemibZQjR7H6TvUJ86cQDE7jn_hRoEHI7Y2TAzNkGeOK364VLLVtB1F2AWXY8H9QxMe7G_Uv1WlpxACVFMSrMdppjh9GHZtQSUMfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسلح‌ترین ارتش تاریخ جهان را به زانو در آوردید
فرماندهی سپاه پاسداران انقلاب اسلامی:
🔹
فرمانده کل سپاه با تقدیر از شش ماه جهاد رزمندگان اسلام تاکید کرد: شما در گرمای سوزان جنوب، سرمای ارتفاعات شمال و زیر آتش سنگین دشمن با عملیات موفق آفندی و پدافندی، مسلح‌ترین ارتش تاریخ جهان را به زانو درآوردید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/681672" target="_blank">📅 14:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681671">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
چراغ فرودگاه قشم دوباره روشن شد
مدیر فرودگاه بین‌المللی قشم:
🔹
پس‌از وقفهٔ ایجادشده در پی شرایط موجود، از چهارشنبه پروازها آغاز می‌شود./ فارس
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/681671" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681670">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
اولین تصاویر از جانی بی‌رحم چهارراه گلزار کرج  #اخبار_البرز در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/681670" target="_blank">📅 14:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681669">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6f2d67a9.mp4?token=nzAt14TgpLugKHdjxIXHjJcan3xHbxWyJ4Ur8m1KkhRF3XwqLKyN1ZYr6zwFPEfXDtHq_F561VleMQIOCzW34uGhJQv0huXWWzavKejbW3ry3kOxjIGR_w-3QkHdEy3khQ0sSFHH5WccMZGvfOTb1hWrRS00ltZ1ePN7-UbImRCwO-ev7sFFyqb89hDPbdPbjSbzxsT_QlknBSvBa9q4a6vQ1_0ngk7Pk0eU_xwYfgEqoM5SHEarUwozavVfdUpMIDx1fzN7WT4a_eApit4ZusQ_HcVnC9jpl5K3hoiqCA6gUC9ArcfzqyaF6c353CAoZfcejC7xTNWTaPgYjwskEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6f2d67a9.mp4?token=nzAt14TgpLugKHdjxIXHjJcan3xHbxWyJ4Ur8m1KkhRF3XwqLKyN1ZYr6zwFPEfXDtHq_F561VleMQIOCzW34uGhJQv0huXWWzavKejbW3ry3kOxjIGR_w-3QkHdEy3khQ0sSFHH5WccMZGvfOTb1hWrRS00ltZ1ePN7-UbImRCwO-ev7sFFyqb89hDPbdPbjSbzxsT_QlknBSvBa9q4a6vQ1_0ngk7Pk0eU_xwYfgEqoM5SHEarUwozavVfdUpMIDx1fzN7WT4a_eApit4ZusQ_HcVnC9jpl5K3hoiqCA6gUC9ArcfzqyaF6c353CAoZfcejC7xTNWTaPgYjwskEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استانداردهای دوگانه برای «حقوق زنان»
🔹
برای ایران: تحریم، فشار، تیترهای داغ
🔹
برای صهیونیست‌ها: سکوت مطلق
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/681669" target="_blank">📅 14:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681668">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
هر آمریکایی متجاوز به ایران را بکشید یا تحویل دهید، ۵ میلیارد تومان پاداش می‌گیرید
طرح جدید ارتش که توسط سرلشکر حاتمی فرمانده کل ارتش اعلام شد:
🔹
پنج میلیارد تومان پاداش برای کسی که هر آمریکایی متجاوز به خاک و آب ایران عزیز را بکشد یا به واحدهای ارتش تسلیم کند.
🔹
همینطور اگر هر زن ایرانی، یک آمریکایی متجاوز را بکشد یا دستگیر کند، مبلغ پاداش دو برابر یعنی ده میلیارد تومان خواهد بود./آوش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/681668" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681667">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
مصوبه مجلس: ۳۰ سال زندان برای پیشنهادات سیاستی یا تقنینی یا اجرایی به نهادهای حاکمیتی و دولتی که برخلاف مصالح اساسی نظام است یا آرای مردم را ‌به نفع گروه یا جریان خاصی جهت‌دهی کند/ انتخاب
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/681667" target="_blank">📅 14:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681666">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f83e2233c4.mp4?token=Rz1-3PGQUFhlfAF0Qv2Io3uFMDrCVna4v8JQAIPByR_47VL06imxaHo2niq2kaGUMKIbpeh-FXueWPvL1K0EedDHU781urO5JUlFid6Bwy29JeBpJ2JubJqUFPdLsntYY-_3GTQrDuXbJ3AJ_6OT1AMCkqn6fg2SkWdFgR7GnPlMrjVHyk3rhx9Lv2hQpQ6eKsfIsAV1PvTLRcJ1NsgZkR_69JYbpjgfKlu7D17lPlHfxfXFAJWhYzdukzYLoH_xEZ8itdy0aesHzvuP6JAac71hP3VQoSZ2e9MoQT1xJiHv-ew_8e0J6huXCGymmL6gqu-zKj9LKab6rvN1ZkP6CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f83e2233c4.mp4?token=Rz1-3PGQUFhlfAF0Qv2Io3uFMDrCVna4v8JQAIPByR_47VL06imxaHo2niq2kaGUMKIbpeh-FXueWPvL1K0EedDHU781urO5JUlFid6Bwy29JeBpJ2JubJqUFPdLsntYY-_3GTQrDuXbJ3AJ_6OT1AMCkqn6fg2SkWdFgR7GnPlMrjVHyk3rhx9Lv2hQpQ6eKsfIsAV1PvTLRcJ1NsgZkR_69JYbpjgfKlu7D17lPlHfxfXFAJWhYzdukzYLoH_xEZ8itdy0aesHzvuP6JAac71hP3VQoSZ2e9MoQT1xJiHv-ew_8e0J6huXCGymmL6gqu-zKj9LKab6rvN1ZkP6CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بحران کشتیرانی در راین آلمان به دلیل کاهش شدید سطح آب
🔹
سطح آب رودخانه راین در آلمان به دلیل خشکسالی طولانی در اروپا به شدت کاهش یافته و کشتیرانی را در آستانه فروپاشی کامل قرار داده است. در برخی نقاط، سطح آب به تنها ۸ سانتی‌متر (و حتی در شب به ۶ سانتی‌متر) رسیده است، در حالی که عبور کشتی‌های باری نیازمند حداقل ۴۰ سانتی‌متر آب است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/681666" target="_blank">📅 14:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681665">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd2127aec.mp4?token=lTKPB9sbhSNQXX112g5yDwykmSlcnP7G3_DomL-zFkA9SPG6O_T43PIPoIMOehBdRPjWJJqOifg-NoJ2ulpvX98fGcrmN8_6oUk7Z-mr-u4YI1zXl2AxStk87SnEeUR-BVlFes5V5GvITPjoD-2FoK2whC0zz-z1LbvaJbglVGLjn9q0x_RSzv4iVgID_85__6H9UKVLkhaRYjgt9wx4d7endtcT6ZWpKhRIxi92yUJzNhgSPNF1dn2wOMPEM-I0iDAxkXt3uIr7xk-iHbT0U0TG3wR0v7_Kba6-VSLxiSf40bxgPIIk_BAgS-3dIQffgG59RbnE8365U-jRkQTSgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd2127aec.mp4?token=lTKPB9sbhSNQXX112g5yDwykmSlcnP7G3_DomL-zFkA9SPG6O_T43PIPoIMOehBdRPjWJJqOifg-NoJ2ulpvX98fGcrmN8_6oUk7Z-mr-u4YI1zXl2AxStk87SnEeUR-BVlFes5V5GvITPjoD-2FoK2whC0zz-z1LbvaJbglVGLjn9q0x_RSzv4iVgID_85__6H9UKVLkhaRYjgt9wx4d7endtcT6ZWpKhRIxi92yUJzNhgSPNF1dn2wOMPEM-I0iDAxkXt3uIr7xk-iHbT0U0TG3wR0v7_Kba6-VSLxiSf40bxgPIIk_BAgS-3dIQffgG59RbnE8365U-jRkQTSgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوال عجیب خبرنگار از رئیس‌جمهور: نوه‌هایتان به شما نمی‌گویند کاری کنید که مدارس مجازی شوند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/681665" target="_blank">📅 14:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681664">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
قالیباف: ما در بُعد نظامی و سیاسی جنگ پیروز شدیم
🔹
امروز ما در یک جنگ ناجوانمردانه‌ هستیم که در رأس آن آمریکا و رژیم صهیونیستی قرار دارند، اما ملت ما شجاعانه، مردانه و خالصانه ایستاد و جنگید.
🔹
بنده به‌عنوان برادری که به جزئیات کار آشنا هستم با همۀ وجودم می‌گویم که ما در این جنگ هم در بعد نظامی و هم بعد سیاسی به معنای واقعی پیروز شدیم.
🔹
تفاهم‌نامۀ بین ایران و آمریکا سند افتخار و پیروزی در راستای تثبیت پیروزی در میدان دیپلماسی است.
🔹
البته معتقدم که مردم ما حس این پیروزی را به گونه‌ای که اتفاق افتاده، حس نکردند و در برخی موارد نتوانستیم این حقی که مردم داشتند را به درستی ادا کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/681664" target="_blank">📅 14:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681661">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316b3b1377.mp4?token=DPyDJIJzvBeukyZZNoHgPw3DOFtgzAFbovbdPXGNkDxX4hkh85g_mWF89O5l3xobtNF80L84AGCEcZRHMF22_dFp-j99wbQqi7KHXbrlSDA46qwoQpxnwFTHdZ8Q1lmKSF51RGcKAgA_uDkW59U24jAyCQXmijgwPPJRTZ6RgY2E9PbTS8aReIjI5oE6Fg3bcegydrhhGx65hwWT0JFG2U5G8F_g37PNGhjJhlRsQpN4HIXxAuULBlfRwzkgJP2L-6gghZfJSljTVrKryuKASNFjxV9H4rD2dsBTs8nNQIEex_PQeciMcgIPoTRgXSNJOOxX-Af1DxGZXX4i5DRWGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316b3b1377.mp4?token=DPyDJIJzvBeukyZZNoHgPw3DOFtgzAFbovbdPXGNkDxX4hkh85g_mWF89O5l3xobtNF80L84AGCEcZRHMF22_dFp-j99wbQqi7KHXbrlSDA46qwoQpxnwFTHdZ8Q1lmKSF51RGcKAgA_uDkW59U24jAyCQXmijgwPPJRTZ6RgY2E9PbTS8aReIjI5oE6Fg3bcegydrhhGx65hwWT0JFG2U5G8F_g37PNGhjJhlRsQpN4HIXxAuULBlfRwzkgJP2L-6gghZfJSljTVrKryuKASNFjxV9H4rD2dsBTs8nNQIEex_PQeciMcgIPoTRgXSNJOOxX-Af1DxGZXX4i5DRWGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ایده استایل شیک برای خانم‌های محجبه و خوش‌پوش #فوری_استایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/681661" target="_blank">📅 14:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681659">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
امید به‌ زندگی در ایران به ۸۰ سال رسید
وزارت بهداشت:
🔹
امیدبه‌زندگی کشور به ۸۰ سال رسیده درحالی‌که سال ۱۳۵۷، ۵۵ سال بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/681659" target="_blank">📅 13:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681658">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
مصوبه مجلس: ۳۰ سال زندان برای پیشنهادات سیاستی یا تقنینی یا اجرایی به نهادهای حاکمیتی و دولتی که برخلاف مصالح اساسی نظام است یا آرای مردم را ‌به نفع گروه یا جریان خاصی جهت‌دهی کند/ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/681658" target="_blank">📅 13:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681657">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfae86d8e4.mp4?token=uqsh7FTCgkTee_VErxSBJ0qQoxYRybFsu_IfZRdOHi8K18lKVc7skpfU5bV4da9EfgIOGZKUn73ut5_bzV7yAIBRfAix14SQExoBEWyIJvRhrAKKRFbzGcECa6qmbOMWuwaZ5M2bFqjDn7jc9dzZ2AY4dNDUN62GPZgx6ST_11Dl1LJQR0Dv4Iht9gv-02ML9yi1NQ406le2n1kT-Q58WALNxUWP-nwLKTclxambTw7zUcHrZz72t0CssUiW7TQ4ZRbMvHd4xoqbNvLdrDbcEOf0LPEDdyJhIB-dpQOy96cfRwL_lkzxZ8fGerJO_nnvUknyB86yxx2B1OmBUT6jOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfae86d8e4.mp4?token=uqsh7FTCgkTee_VErxSBJ0qQoxYRybFsu_IfZRdOHi8K18lKVc7skpfU5bV4da9EfgIOGZKUn73ut5_bzV7yAIBRfAix14SQExoBEWyIJvRhrAKKRFbzGcECa6qmbOMWuwaZ5M2bFqjDn7jc9dzZ2AY4dNDUN62GPZgx6ST_11Dl1LJQR0Dv4Iht9gv-02ML9yi1NQ406le2n1kT-Q58WALNxUWP-nwLKTclxambTw7zUcHrZz72t0CssUiW7TQ4ZRbMvHd4xoqbNvLdrDbcEOf0LPEDdyJhIB-dpQOy96cfRwL_lkzxZ8fGerJO_nnvUknyB86yxx2B1OmBUT6jOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض سرباز نیروی دریایی آمریکا به شرایط ناوها
🔹
یکی از سربازان نیروی دریایی آمریکا با انتشار ویدیویی، از شرایط ناوها انتقاد کرده و با لحنی طعنه‌آمیز می‌گوید: «بیایید عضو نیروی دریایی شوید!»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/681657" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681656">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf64a1bb97.mp4?token=MMH1qs8c3EHqUks-l4TEnwmz7NI0ruJNlgNNKG3EjhDSBaQn7VXgEcWi8q78ajkKDNTzL9fpb9d9nWyMcwQuPO6i00KTwnT4TRaKKYkImFvH0nk84auttPsj81Szd12wUjzYak_3MRx7ugFU94pJT-5hM0WJdul6I4twtCPHV85dbfBjoCINXIYlDk75EwyceSRarNYGdGkCgfPlepkE8fUWSD-qaiA2i1POVAoIOWZFhr66tW1G8jCrf5c50Vwe8cSm9evSEeVTyA9VW3tD4hi6vQwWagJkkHlfW5c0WLMr1Nuon2YFojKTiF2efY0-zt5XdrFVXWy3NpL41Li3PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf64a1bb97.mp4?token=MMH1qs8c3EHqUks-l4TEnwmz7NI0ruJNlgNNKG3EjhDSBaQn7VXgEcWi8q78ajkKDNTzL9fpb9d9nWyMcwQuPO6i00KTwnT4TRaKKYkImFvH0nk84auttPsj81Szd12wUjzYak_3MRx7ugFU94pJT-5hM0WJdul6I4twtCPHV85dbfBjoCINXIYlDk75EwyceSRarNYGdGkCgfPlepkE8fUWSD-qaiA2i1POVAoIOWZFhr66tW1G8jCrf5c50Vwe8cSm9evSEeVTyA9VW3tD4hi6vQwWagJkkHlfW5c0WLMr1Nuon2YFojKTiF2efY0-zt5XdrFVXWy3NpL41Li3PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متیو مک‌کانهی ۴۰ دقیقه ملکه زنبور را در دست گرفت
🤯
🔹
متیو مک‌کانهی برای فیلم جدیدش، ۴۰ دقیقه ملکه زنبور را بدون آسیب زدن به آن در دست نگه داشت تا هزاران زنبور دورش جمع شوند و این صحنه بدون جلوه‌های ویژه ضبط شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/681656" target="_blank">📅 13:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681655">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81159e939.mp4?token=PfY3ybtddM_L0iEzzKapkFXVrkYtFLz89khHsAGuMJuBgSeN6bIGV2rU2Bw4q98mM7oVOkq6IMg7DZRrLp7AxJArBXWSHFo96MYPz0hl3ZNVnyJ-9TjfgJNF8mBQo3y-dUL8ebTkmQCPwSsgeBwCHii51asPumXyhD1OBdjVwUKGN3BC08TJQglyBOu1mSeIhJzGqI5XEw4SPlwsOSaJdQ9hAHqGhnT7g_9AHNjtdMVGB4a6bSWecs6ojf0tqoAxQYNPCUTZB7qbD10Br7lMLd7wCtnlRwEr1hrcBA5eXP50m6FA_X1IL7JIwFh60qzv-mhHoG77d-Id7MIyf0qfIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81159e939.mp4?token=PfY3ybtddM_L0iEzzKapkFXVrkYtFLz89khHsAGuMJuBgSeN6bIGV2rU2Bw4q98mM7oVOkq6IMg7DZRrLp7AxJArBXWSHFo96MYPz0hl3ZNVnyJ-9TjfgJNF8mBQo3y-dUL8ebTkmQCPwSsgeBwCHii51asPumXyhD1OBdjVwUKGN3BC08TJQglyBOu1mSeIhJzGqI5XEw4SPlwsOSaJdQ9hAHqGhnT7g_9AHNjtdMVGB4a6bSWecs6ojf0tqoAxQYNPCUTZB7qbD10Br7lMLd7wCtnlRwEr1hrcBA5eXP50m6FA_X1IL7JIwFh60qzv-mhHoG77d-Id7MIyf0qfIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت اندیشمند برجسته آمریکایی از ۳۰ سال نیرنگ و عملیات آمریکا علیه ایران؛ از ترور تا جنگ اقتصادی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/681655" target="_blank">📅 13:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681654">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ادعای اکسیوس: ترامپ از طریق بارزانی با سپاه تماس می‌گرفت
ادعای اکسیوس:
🔹
مقامات دولت ترامپ کاری غیرمتعارف انجام دادند؛ آنها مذاکره‌کنندگان ایران را دور زدند و مستقیماً با رهبری سپاه تماس گرفتند.
🔹
فردی که آنها برای کانال ارتباطی انتخاب کردند، نچیروان بارزانی، رئیس منطقه کردستان عراق بود که چیزی داشت که کمتر کسی دارد؛ اعتماد رهبران ایالات متحده و سپاه.
🔹
بارزانی در طول جنگ ایران و عراق در ایران زندگی می‌کرد و در دانشگاه تهران تحصیل می‌کرد؛ او به زبان فارسی مسلط است و روابط شخصی با بسیاری از اعضای ارشد ایران، از جمله اعضای ارشد سپاه پاسداران دارد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/681654" target="_blank">📅 13:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681653">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e64d209d9f.mp4?token=jmUQioUHzSF5mP9kTmfeux5LiNBhzB5n7hLfRQbgf0f6t_nnyC__JhvRPsd4SyzzMUd1w1vZ0SmytWji6Jkzkj3Lkkd3-MRo1DmFaVMeoEXUHjS8HXSYfHnaPsIag9kFOwJoxlFuw5OIHfv2oXLmjz8zwudXB9aoGa_9cXdd-HAQGnmyhpSS15GcFwfwenOxBGGGO7bpv0LdV8wfoqC7N5P2hxWobl-2BiZqBhzLx4Iu2IabQuFbr48APr20kDKPQDIphjNR22hZCLxz4BNLNdCzfzU7v7GBTIMWmgZz_KVWdvibPIIj5q0TFCsYRinDlY9S0cvcOum5z1ZJSq8fvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e64d209d9f.mp4?token=jmUQioUHzSF5mP9kTmfeux5LiNBhzB5n7hLfRQbgf0f6t_nnyC__JhvRPsd4SyzzMUd1w1vZ0SmytWji6Jkzkj3Lkkd3-MRo1DmFaVMeoEXUHjS8HXSYfHnaPsIag9kFOwJoxlFuw5OIHfv2oXLmjz8zwudXB9aoGa_9cXdd-HAQGnmyhpSS15GcFwfwenOxBGGGO7bpv0LdV8wfoqC7N5P2hxWobl-2BiZqBhzLx4Iu2IabQuFbr48APr20kDKPQDIphjNR22hZCLxz4BNLNdCzfzU7v7GBTIMWmgZz_KVWdvibPIIj5q0TFCsYRinDlY9S0cvcOum5z1ZJSq8fvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنجال در اوگاندا؛ بازسازی دوران استعمار
🔹
برخی از گردشگران سفیدپوست در اوگاندا با پرداخت پول به افراد محلی، خود را روی تخت‌های آهنی حمل می‌کنند؛ اقدامی که یادآور دوران استعمار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/681653" target="_blank">📅 13:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681652">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
مصوبه تازه مجلس؛ حبس برای ارتباط با رسانه‌ها و نهادهای خارجی
🔹
مجلس با ۱۸۳ رأی موافق طرح مقابله با نفوذ سرویس‌های اطلاعاتی و نهادهای بیگانه را تصویب کرد.
🔹
طبق این طرح، مصاحبه یا ارتباط با رسانه‌های آمریکایی و صهیونیستی یا رسانه‌های تأمین‌شده توسط آنها می‌تواند مجازات ۶ ماه تا ۲ سال حبس داشته باشد. ارتباط با سفارتخانه‌ها و نهادهای غیرایرانی نیز بدون اطلاع‌رسانی و مجوز کتبی وزارت خارجه ممنوع شده است.
🔹
این طرح همچنین برای برخی اقدامات تحت اشراف سرویس‌های بیگانه، مجازات‌هایی تا ۳۰ سال حبس در نظر گرفته و رسیدگی به جرایم آن را در صلاحیت دادگاه انقلاب قرار داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/681652" target="_blank">📅 12:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681651">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21c4c920b9.mp4?token=EN51qq6RTdJMbDZdB0c51hGkXAC0JQhYjEJyT2SB2Hs4Qzign1uT1FnsNWHVyxIPvcsTZw2QPnLNWSX8mIUa687Rh3qgBlTgpCLKjemXssL-zFPukvTX6k1bm4_L2b6SmkjyZuVYot1jQsnh3kmiKaFnF0-_cMn9107SpDU4d0KfRlPlZsPAyVi8vsXCgi8TjrExZ4VbKk14c_YjLLNmOcH6Y9lp8RJPFEuqGzz7Xni3DUct-iIFiQMQGs31PKCZFA8r81izQBmch6F9cYRs3zgV75bkCfn1ceyHewLhzxFdtXK05DdOKnX_gfoSBKwND3aoGjHn3tJq2RUWptEpUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21c4c920b9.mp4?token=EN51qq6RTdJMbDZdB0c51hGkXAC0JQhYjEJyT2SB2Hs4Qzign1uT1FnsNWHVyxIPvcsTZw2QPnLNWSX8mIUa687Rh3qgBlTgpCLKjemXssL-zFPukvTX6k1bm4_L2b6SmkjyZuVYot1jQsnh3kmiKaFnF0-_cMn9107SpDU4d0KfRlPlZsPAyVi8vsXCgi8TjrExZ4VbKk14c_YjLLNmOcH6Y9lp8RJPFEuqGzz7Xni3DUct-iIFiQMQGs31PKCZFA8r81izQBmch6F9cYRs3zgV75bkCfn1ceyHewLhzxFdtXK05DdOKnX_gfoSBKwND3aoGjHn3tJq2RUWptEpUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۴ مدل گره با طناب که می‌تونه به کارتون بیاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/681651" target="_blank">📅 12:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681650">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crScds7K8kVjul8dksYGSXikdN5atQYi2wfOJysp5mJCi4QPWNrCJBy6DiFQ_YyIsQZ38EgKX7ZT2_KRG7w9WUsKgE4yXaprKksLHq4pL-pE-k1KwMAPXbiepwgInyM3-cfjtHSYtSs2AJIqUjf2uYN8ulDimNS-VBD0heTHHCzTppJFywz6_AeT9lht9ro7WGYF78l9bTci9OE3PuS9DGpBa3f6zSSlmab7yb0b3eFKto5ibD2kE2wESQyTXhylSVI9PdgwrOGSzv4wS3RZT0h90kCx-edNJ5hLAiBN8gwQO7aw5XYDyNS8AXvUoWPYqPU5xwfYjJ6NhFhB4u9eWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_خودرو
| قیمت روز خودرو های بازار کشور؛ امروز ۲۵ مرداد ۱۴۰۵
🔹
بازار خودرو ۲۵ مرداد را صعودی آغاز کرد و بیشتر خودروها گران شدند، اما رشد محدود قیمت‌ها نشان می‌دهد بازار هنوز با یک روند صعودی قدرتمند فاصله دارد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/681650" target="_blank">📅 12:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681647">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gASj4qe2PWCfYgAOhMQCQyrEmvMW8WlHgLF3mnqp9HRn6WND_z7xcqVZqWRx2Ql2GBpaJHxX2PbExKbJd52NjT_ZVLPQ7ixOzNzJX5PCxxYtiDFWojj89UNUQQZLxLjVHU3TqrGBP9dfMTI1Z2Jml2Lq8AFAbQx95XHB-wMpAS-Nlar6JXV6umRCAVUaK-3BGWGexU-JIZpvMxVQMQ_EUhgCZO761rk8nOZb9hegrudsUlLuKh3dD4U7QpQlJd1ig07I3m5p3M4VfgR0i2BuIDblElv7NGBUHhqafbr651XI4Wx_wF7-Q0BXNTm6Pvyle-a_0MMx7LhvfaUS8TEb5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امارات برای حمله زمینی آگهی استخدام سرباز داد | کشوری که یک تیم فوتبال نمی‌تواند جمع کند چگونه می‌خواهد بجنگد؟ | ماجرای «سربازگیری» ارتش‌ شیشه‌ای
🔹
وزارت دفاع امارات متحده عربی اخیرا با انتشار فراخوانی گسترده، از نیاز خود به جذب نیروهای تازه برای پیوستن به نیروی زمینی ارتش خبر داده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3237916</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/681647" target="_blank">📅 12:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681644">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MA-mZjex3CkQbHbDlf5q4bimuVRhjfqegDhRf-MeA3fWDHgbGQ-jqyLw6GWOj__AKRRJ_2Zgb_wJ1_ONumSBHLifGwHcNo8RGOjzakP5JxIJGXL7d6U9fwn6lF6XTcGyhhDLIJOt7vLbCEmp8lmaFyFMBNzMgISvFnzj0AGjCrMHE2YmUrEAXMU12LL0Hz-7aYP-NJPD9UGtB8fkuUh8ibB5wP3FPQ47ade7EYWHhlyBaHHUT4752JF6fr4iVkNBber6EfeLU1mL8hXXx3_BF5ynUBUneA5N-EJu6nnbATuJaNOYqoUlCbmPRyNdqPOeUUcPkLq4oTdnURo1ODSo1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jogdAYpvk_5T1X2vRUJ3aY0qNHI2BkDpn2PYnyqgGKQ6s8dHLp4bDRcqxDiZxSIDm9cu1if8owo7uttB7RWtHcQh6XKQBS4y3MAS1rPNPoh_j45XoTacH0YrpxDeKz3t_OnYPxDZKKNdR3Q13KMpMVPcuMRnz8hcb0ktUbhQdD1KzxZ8mxsQb34eKDUQu3d0fj-4oibDFuuXtAfA3v1eUqThxs1qWnbzAa2DVGjDjaBT1iF8kYUANLsdZtKH9FZpYiO6f33Xb-rtay6gMIUCmctLOD4cTZHiuGRRkXCmdICsRRHeN-Ak-FvGLAC4UVW7vJCTb6x07L1mg3Gnt2IM3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LFmXE5End3GrHvY2TYN8OkDhuAl9-1e8jJQ4JA_v_oSK8hp33CCPR-DMQ1TIbaBf_DutMCS1lX6aJqenSmqTIxEVlB_Qpyx8RM0Z2aatNwwm03IxthYy9-B--0FeGhUowgaezekWwu5zTBmpUgk4ghGtaxb05UOotiCQFSIsLVveApW-CtTCem8wQiT8OCKxfvqQffW-EHBd32b6iPuCtUvh4jGYF0hbO6L9fHhgsdK1sQb9Zn1597n8MKALa4XNT3olIi2TbY526Wvc8BprEBa18tZ63QRF4iBO6NEXS3KejKoOQdPg7HwDtp3SOqR4P6BmGvEymnbn3Mio0Cmimg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
انفجار گلکسی S26 در جیب صاحبش؛ کاربر راهی بیمارستان شد
🔹
یک کاربر در هند مدعی شد گوشی سامسونگش پس از داغ شدن شدید در جیبش منفجر شده و باعث سوختگی شدید و آتش گرفتن لباسش شده است.
🔹
مدل دقیق گوشی هنوز تأیید نشده، اما تصاویر باقی‌مانده احتمال گلکسی S26 را مطرح می‌کند؛ سامسونگ هند تاکنون واکنش رسمی نشان نداده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/681644" target="_blank">📅 12:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681643">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک اقتصادنوین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNlZmEhp6jMzY0RKEKeeXRJ9rSWPnoV8E3tf2i4u_LBOeSyOJ4bgPBjGV11PTAEKhvL-Bex7HC9nkdtshMfiEmTMnUr8MLSaE3uybgEcvNu2UGj96_KqjUHbjWZL_TYulyAAnVfqKNkHG1KGcHdt5rbEa2sLTq-8x7DMacrANUrCZctfxEeCP5NoLx1jo_5SEP8xc4HaMyPQhV3q-mTj10QD7-J1306E_QSe6OyomY_ei5HLQ-Z5I8888WW_EL9_pJnpytOTpnnICwndGBVojmxnTr5CQBVZRLgy0a2yvGz2X1uyzKjbGenAA6iPCdfqtoN92N_-UsCcsJv1DwNTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
«هم‌پی» اقدام پیشتازانه بانک اقتصادنوین برای رفع موانع تولید
🔹
بانک اقتصادنوین همزمان با بیست‌وپنجمین سالگرد تاسیس و با هدف تامین حقوق، تامین مواد اولیه، تامین برق و کمک به فروش اعتباری تولیدکنندگان و فعالان اقتصادی، از طرح پیشتازانه «هم‌پی» رونمایی کرد.
🔻
اطلاعات بیشتر :
https://enbank.ir/s/mfa9aC
☎️
02162740
🌐
www.enbank.ir</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/681643" target="_blank">📅 12:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681641">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e240d557c.mp4?token=PgddS8GS3lbpmXkm6siq9ioVSWCSPRu9NpERVBtYJzCrPfvvP3WV7rR8zlQaD_jVp2iKGW9ucixjeJKCSED0kmxUqh2dKntZj8eU4afC3Ry8DxQkOp_uCTfTKlqsfq9RUEz6VgqwOgaJFpoF4V6vy4gL8nRpgakNvvBRTy00M2vYvVVTzCOuQJKDbWQNPCJS4LbfAer3ToSjoTz7_4hpIwUAMAGGeJ6VO_nfyjC69HFTyS9-Ko3Vdh6FX34Wd6HwDUIOzMkmpieXujjcI8tAR9R0rupaOI2K5VnRGvaVpzhbrzSdBZJBrRWKdAagwc8SmlfQCfVWmzBZHVvbuv7axnLMrvnjheerTo5Q-8cpyqd7wRrlI34Hj1Wyhlh2XjkEx9CpUMBKRDdGtTR6NRJ6a9hcRuqiF3l7blmKXIKW6akweqgFdDzLqKetpCO-0sjIFDjIt79QJ3rLrzThRGHGaaRC7FNceClMLuAQ9piUIR4hco5nc3DJjdnTMlro20glOVSZsBhKndPSZBv_O6vJ8QHaJiHhOqvvDRZs46087-e0ZM43o1-n0FX0JCG1ap14AF_1V2RM6rXpzoNLZRR14UcS5YS0MQS89_WQvqN22QJEtW3KaACbu8gnPNraCZxREEdVHLR3UsolO5F8eaYH56DItJ9-tDVF_TUr-mSpaYM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e240d557c.mp4?token=PgddS8GS3lbpmXkm6siq9ioVSWCSPRu9NpERVBtYJzCrPfvvP3WV7rR8zlQaD_jVp2iKGW9ucixjeJKCSED0kmxUqh2dKntZj8eU4afC3Ry8DxQkOp_uCTfTKlqsfq9RUEz6VgqwOgaJFpoF4V6vy4gL8nRpgakNvvBRTy00M2vYvVVTzCOuQJKDbWQNPCJS4LbfAer3ToSjoTz7_4hpIwUAMAGGeJ6VO_nfyjC69HFTyS9-Ko3Vdh6FX34Wd6HwDUIOzMkmpieXujjcI8tAR9R0rupaOI2K5VnRGvaVpzhbrzSdBZJBrRWKdAagwc8SmlfQCfVWmzBZHVvbuv7axnLMrvnjheerTo5Q-8cpyqd7wRrlI34Hj1Wyhlh2XjkEx9CpUMBKRDdGtTR6NRJ6a9hcRuqiF3l7blmKXIKW6akweqgFdDzLqKetpCO-0sjIFDjIt79QJ3rLrzThRGHGaaRC7FNceClMLuAQ9piUIR4hco5nc3DJjdnTMlro20glOVSZsBhKndPSZBv_O6vJ8QHaJiHhOqvvDRZs46087-e0ZM43o1-n0FX0JCG1ap14AF_1V2RM6rXpzoNLZRR14UcS5YS0MQS89_WQvqN22QJEtW3KaACbu8gnPNraCZxREEdVHLR3UsolO5F8eaYH56DItJ9-tDVF_TUr-mSpaYM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دریا همینطور که بخشنده است بی رحم هم هست
🔹
این دو جوان هرمزگانی ۵ روز در دریا سرگردان بودند و بنزین تمام کردند که صیادان بحرینی آنها را پیدا می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/681641" target="_blank">📅 12:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681640">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
برداشت وجه از خودپردازها رایگان نیست
🔹
با بخشنامه بانک مرکزی برداشت وجه نقد از خودپرداز بانک‌ها به میزان نیم درصد مبلغ برداشت کارمزد خواهد داشت.
🔹
حداقل کارمزد پرداختی برای برداشت وجه نقد ۳۰۰ تومان خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/681640" target="_blank">📅 12:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681637">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2-C5YOgFbaydNapVETho3elUP2Pe0HDlic3lt_7u-3lV7X58-s3RTSks-7PSgDwFB-iyVA86AJeQ2yHpwh_P0naei5hNz4U_abQx0Slm1SbqR2OoUkvDC0HNKVA_N5snLIi0t_2C9Kh1BwbUVsVJ7nbYB1iOYFGkwIBpsqE-JNUJ5yM5yKPfiPLtR4AzmJn9oipP4j8-5RW_Q0rakV3Q1H5BK1TDOY41nN8PP_CAzwLDCtmvO--gM87KeIi7K2Sn2CXbY_w71fCoT8E7T_kUjZEdkS0YsW47bSdNT9iwFff4ENL63ipEsgpgn2ElA4ZXBFvkgjMcMaATHaoP1KIXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ksyTorQbzj2A42CBTnt82BA9jj-RHanim3wDmWdWD1dChHo5lXJ6VNLU3Rdu_4e3RFSEriD0-5pqTgsgKUmlt5uQWyTkgS6hU6yLZOZ0SsH8deq1rz2Hs22AR0teyZ-oGTwbcNzhR2msvYII-M4XSWdpQwmurZG13vXzE__XOZx4B1wF8lyEN35hmSmhu5CrS93rmWG8Yogny8ChZ_TfPs7WETJpRg8cxsDCaAFl3l31r_SVL-QAe5WMxKj8Mbx8fWKo0Hrs6ao-KF2TI9kegCRK8Gsb3YMcx-pmV9B8XdKywhZLqD1XJYF_IPcU8OKOpoHcRwfUGEZmx7wqC5AWYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بینی‌مو عمل کنم، خیلی کیوت میشم!
🔹
فقط بینی نیست، وقتی عمل زیبایی از سن کم شروع میشه، خیلی وقت‌ها بعدش یه ایراد جدید پیدا میشه و دوباره نوبت تغییر دادن یه جای دیگه‌ست.
🔹
انگار این روزا بعضیا تا وقتی چند جای صورتشون رو عوض نکنن، باور نمی‌کنن خوشگلن!
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/681637" target="_blank">📅 12:23 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681636">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bb740b035.mp4?token=aAUDJLOOie-sQmKohDrv3phd-agO7noQs8GoySrVuDMhf3RhMBANQakvfVp8U3j-8AyOn3V1lsKtBoiXJarmyOd1RiBF4ul9m6x6JyqOe7AKkgOCbsV4WrLDKNDapcKEF0JvEQ7cQQOB6spyg6OBE1mdseqhAkY-0N4QaGb-3JdObnAEqVG2eLELIlCInmS3nBXcJjG3C0qciiBY_BVL3eGwmhduC7AtqFp6P5lfky4zKXm9wZDFkOjS1quxlI2O9lXMNoZ3eec-33hKKHDGRTfCKWVbAcq1CwKR8t7FGAlEtbcs5G9aY2VaLyiRDdTMLKhDgzgrYmoyyVCoNEtL0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bb740b035.mp4?token=aAUDJLOOie-sQmKohDrv3phd-agO7noQs8GoySrVuDMhf3RhMBANQakvfVp8U3j-8AyOn3V1lsKtBoiXJarmyOd1RiBF4ul9m6x6JyqOe7AKkgOCbsV4WrLDKNDapcKEF0JvEQ7cQQOB6spyg6OBE1mdseqhAkY-0N4QaGb-3JdObnAEqVG2eLELIlCInmS3nBXcJjG3C0qciiBY_BVL3eGwmhduC7AtqFp6P5lfky4zKXm9wZDFkOjS1quxlI2O9lXMNoZ3eec-33hKKHDGRTfCKWVbAcq1CwKR8t7FGAlEtbcs5G9aY2VaLyiRDdTMLKhDgzgrYmoyyVCoNEtL0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداداد عزیزی: علی دایی خیلی خودخواه است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/681636" target="_blank">📅 12:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681634">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
این دفعه اگر دچار اضطراب شدین، کارهایی که همیشه انجام می‌دین رو برای یک لحظه رها کنین #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/681634" target="_blank">📅 12:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681633">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84417c6223.mp4?token=O9TNNfdh8hqaJi-jEM5FAMV5-hGqJu4OFktTDCMJK7mhsM-jGYCc0ADDf_QLejo-oxQsiEBXU9aagOGxLCiAJfFE1n6qy5aov7omN7mQeOjS3Tn9NkaFrYgq2IKF8O23_-xW0BlfkIIWnTBSWTVCabsSb5jI6-udesN5xRTQQdbU2k9kcJw9fFueFD2x92vwRlxvc6-5qPCLClTUuyDsKFY8AFNOwTPqFv8aiKERtHwmW3GqxAihP_5q5YnRxJZXo_BVKZuwgdrOi2mRqgB5jiLEOXR9GI0tc8-ghoJKB2qo1MK05nlPF95oLSmgT_nyXqZE0e45ox1wj3kCaUTOQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84417c6223.mp4?token=O9TNNfdh8hqaJi-jEM5FAMV5-hGqJu4OFktTDCMJK7mhsM-jGYCc0ADDf_QLejo-oxQsiEBXU9aagOGxLCiAJfFE1n6qy5aov7omN7mQeOjS3Tn9NkaFrYgq2IKF8O23_-xW0BlfkIIWnTBSWTVCabsSb5jI6-udesN5xRTQQdbU2k9kcJw9fFueFD2x92vwRlxvc6-5qPCLClTUuyDsKFY8AFNOwTPqFv8aiKERtHwmW3GqxAihP_5q5YnRxJZXo_BVKZuwgdrOi2mRqgB5jiLEOXR9GI0tc8-ghoJKB2qo1MK05nlPF95oLSmgT_nyXqZE0e45ox1wj3kCaUTOQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔧
دیگه برای هر کار کوچیکی دنبال تعمیرکار نگرد!
دریل و پیچ‌گوشتی شارژی ۴۷ تکه؛ همه ابزارهای ضروری رو یکجا داشته باش!
💪
✅
موتور قدرتمند و شارژی
✅
مناسب باز و بسته کردن انواع پیچ
✅
ایده‌آل برای سوراخ‌کاری چوب، پلاستیک و فلزات سبک
✅
همراه با ۴۷ قطعه کاربردی
✅
سبک، خوش‌دست و قابل حمل
✅
مناسب منزل، محل کار و کارهای فنی
🔥
قیمت قبل: ۲,۲۹۸,۰۰۰ تومان
💥
قیمت ویژه: ۱,۸۹۸,۰۰۰ تومان
🚚
ارسال سریع به سراسر کشور
💳
پرداخت درب منزل
🎯
ارسال رایگان در صورت پرداخت آنلاین
👇
برای سفارش و مشاهده جزئیات، روی لینک زیر کلیک کنید.
https://memarket24.ir/product/fast/35160/180124/</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/681633" target="_blank">📅 12:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681627">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1278d5aaa1.mp4?token=Zw73ruFppjQ3cFbjgdkIRe1DsaMrbqeaJKKrOeEGMNkkbxO5cd7ASJGIT_8eN2E7zWeJJ7gzQUpmrO0r2oBBmdI1sIQoTRkepIA9BfkthaGcnzfHhmL6KfQ7MDTfgVC3LYE2JMbNED9brQOGzPQ83oP6ODVQBLX2xThMxvn1pmG77Kiim5aU6mLybm9ZWr1u6jEWfiKJLgHvVB0850IM7EZ3ZNzlobS8F_CUgL4DrtmvO0TjafqgPwjtAnQEm2jX-WLcWCiSZw3xvo0rBCMbey2XV7lncTZ2vz4NCJgJ5gRM3REGzeWhvde-ZxXkkxh5U3bW6ZqSlKm1dwC2RYI6ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1278d5aaa1.mp4?token=Zw73ruFppjQ3cFbjgdkIRe1DsaMrbqeaJKKrOeEGMNkkbxO5cd7ASJGIT_8eN2E7zWeJJ7gzQUpmrO0r2oBBmdI1sIQoTRkepIA9BfkthaGcnzfHhmL6KfQ7MDTfgVC3LYE2JMbNED9brQOGzPQ83oP6ODVQBLX2xThMxvn1pmG77Kiim5aU6mLybm9ZWr1u6jEWfiKJLgHvVB0850IM7EZ3ZNzlobS8F_CUgL4DrtmvO0TjafqgPwjtAnQEm2jX-WLcWCiSZw3xvo0rBCMbey2XV7lncTZ2vz4NCJgJ5gRM3REGzeWhvde-ZxXkkxh5U3bW6ZqSlKm1dwC2RYI6ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
من تاریخ سرزمینی هستم که بسیار کوشیده‌اند راز پایداری‌اش را دریابند #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/681627" target="_blank">📅 11:36 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681626">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWeImGOewfM4I4nXEMlRQJs7YXN_9oBTUvSoixxzKzQiHt2tiTa2lzRZGEvXzhe4tMgGpKkmPZp5a2PCL5TMokJ33vK_Aja3U5hh90iLyt-jrC3Tp3N1fp4hbRiODhiWN97dOgPu3R2lpoR2s4MSE104stYniMDXMGjIojVEA6b-87u5esyhyycfhrNBvCINiUo0w5uP2HZlWqvvQ2YszERLX5O4lUyFLVGr_pt-heLWPyEp_gvsZhr2DgryHpNCLPEex6QmjtVZGGqlcZMNmLPIBhzHDMJS04WVb_b41qp6YTSXlDJJnapW02uwdc1N52w2Zp2sy_42KWsJVqkMqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۴میلیون نفر در سنین فعال ازدواج مجرد هستند
🔹
همراهان گرامی خبرفوری؛ برای شرکت در این پویش کافی‌ست یک پیام صوتی حداکثر ۱۵ ثانیه‌ای ارسال کرده و از دلیل تجرد خود برایمان بگویید.
🔹
برای حفظ حریم خصوصی، صدای شما تغییر داده می‌شود و هویت‌تان به‌صورت ناشناس باقی می‌ماند.
🔸
روایت کوتاه شما می‌تواند بازتابی از تجربه‌های متفاوت مخاطبان در این زمینه باشد
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/681626" target="_blank">📅 11:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681624">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
کارمزد ساتنا و پایا هم با دلار بالا رفت
🔹
کارمزد پایا ۳۳ تا ۶۰ درصد افزایش یافته و به ۴۰۰ تا ۱۲ هزار تومان رسیده؛ سقف کارمزد ساتنا نیز ۵۰ هزار تومان شده است.
🔹
کارمزد کارت‌به‌کارت تا یک میلیون تومان ۱۱۰۰ تومان و برای هر میلیون اضافه، ۳۵۰ تومان بیشتر محاسبه می‌شود.
🔹
پیشتر رئیس‌مجلس گفته بود که افزایش نرخ ارز نباید بر بسیاری از کالاها و خدمات اثرگذار باشد؛ چرا که اساساً ارتباطی با ارز ندارند./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/681624" target="_blank">📅 11:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681620">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4ti4o1szYVrgNiWHn6KLVyPkufnRfXIHKf9VzrH8Muap1FyK7rxfVp8sNZob_oYS_wo3UwiuQOLcdwtlaLWtOht_NXHGxcKDtUQJpPZ0bj8An4bMLv9ywKc5-igcRkGghA8rm7m9zDNJIcGGu6-ChkeQA4GxkXMqzM-q4YYPQi--5OH-pHKEkJv2rJo1w_rxfkREuPuvY3W8sOG4m3XFwkeQWVF2oIDDw1_2oA5br7kFFd5AIOw5I0ACdW9DbQGRm0kDZth1rX4tU_JlF9Td-KSOl0FClP-7CNGPZEbdAxgnVyVauQoU4lL-csJvTpm-FRhAmw8MRqZx0MUkqQxpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا بیشتر از غرامت متفقین از آلمان، از ثروت ونزوئلا اخذ می‌کند!
فرانسیسکو رودریگز، اقتصاددان سرشناس ونزوئلایی-آمریکایی:
🔹
به گفته یکی از اعضای کمیسیون دولتی ونزوئلا، آمریکا تاکنون در سال جاری، ۴.۷ میلیارد دلار از ونزوئلا بابت هزینه حمله به این کشور دریافت کرده!
🔹
که معادل ۳۲٪ از صادرات نفتی ونزوئلا در همین مدت است؛ برای مقایسه، آلمان بین سال‌های ۱۹۲۴ تا ۱۹۳۱، ۱۳٪ از صادرات خود را به‌عنوان غرامت به متفقین پرداخت کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/681620" target="_blank">📅 11:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681619">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e99e81e0.mp4?token=HN97xzxZCf85gD2dxVYqvcxCELV8DGM2raN9kvv47kagqsxd_kOGnPyb_TlTVqmog2EUI74MfQez_MNU5swsIBIfzVZ-rKJZY0NEqdspxpJq3Dr9UGKBhgjaIbXLRbVMSKvv40aMq-azNrzzRmxRKjLh2SPUhrBCDmNcdT59ZgAnCKE2Gp-YrTNOFqFesRu_VmDIfo2C5sY4vDxvJSULBn4YjCBchNq1TSUR7lB4znts8QOuhMdj39L4S2GHFYwQG-UfqTDIvhAMBKQXBbmZlfAT6_tdRqP913ZQbM8VkaR5LYQD4KGJUq3rvH4LA7uNr3aoCYZtlgi0OwjIGn_MB4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e99e81e0.mp4?token=HN97xzxZCf85gD2dxVYqvcxCELV8DGM2raN9kvv47kagqsxd_kOGnPyb_TlTVqmog2EUI74MfQez_MNU5swsIBIfzVZ-rKJZY0NEqdspxpJq3Dr9UGKBhgjaIbXLRbVMSKvv40aMq-azNrzzRmxRKjLh2SPUhrBCDmNcdT59ZgAnCKE2Gp-YrTNOFqFesRu_VmDIfo2C5sY4vDxvJSULBn4YjCBchNq1TSUR7lB4znts8QOuhMdj39L4S2GHFYwQG-UfqTDIvhAMBKQXBbmZlfAT6_tdRqP913ZQbM8VkaR5LYQD4KGJUq3rvH4LA7uNr3aoCYZtlgi0OwjIGn_MB4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشی جدید Honor با دوربین رباتیک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/681619" target="_blank">📅 10:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681618">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UW1-dD9v9zlz-jWnAzUIYvNsEds2DGR_qXMAZitiLOBvd6xNC-B7yPvMlK15MLfMWBvkzYkzU8btynY9LC63ECKtDUKLS5tRcmZlSFVd38mWH_qOTrtSNKiiZUBPtP_bEIpbrRSiusjQzIDDTOShAWHQpFE8InUwnTYUno5yKy8gWM5t4FtMU1l1lDdo0fSePKSvRFL5FvETQzz0-tqX8MX95EXkXtODWUiN4DEouazOmF_LC6gYsiEzJd7L_t3mKiOIfNK_dp2FDIPTH0p1jvdeCgQdK4fqARodrwymRg0soQ_A9CeYf5G3fyX5hPrRQnS6AZoxxJ0b6thOCjC2Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری متفاوت از کودکی رهبر معظم انقلاب اسلامی در آغوش رهبر شهید ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/681618" target="_blank">📅 10:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681615">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6702fd240b.mp4?token=i88V5ZHyfXEiTvUGmBKoRha3hySTCmUYONZGqb6optyiw-tLtNaERXEYlk7IqorYRDjfp7ibh20uaaN77nTrg0Us9z1SJbPFmZ79EqmfTHJQmMF_zKWj3jhlQxGHy_n0zWxnz_ZfePugQkVteoYNTWUpzJgD7GFFSC1Dm8k2Mqo4koH-o8t5xPcjHdmurs5zoqBpxy0NuBREVDZBvIDqjgs3j_IkPp2zssOwrL6wVKejrJ7v5CBcZFOF5KuNMSvNr6t1hMeAajPybgyqaH_ZN7-s3TgTjIiB9LEe14j2ud8_aXuY5FawIXtfgXH1U-QyZ4dAiFD3NKM_vqupYpu26Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6702fd240b.mp4?token=i88V5ZHyfXEiTvUGmBKoRha3hySTCmUYONZGqb6optyiw-tLtNaERXEYlk7IqorYRDjfp7ibh20uaaN77nTrg0Us9z1SJbPFmZ79EqmfTHJQmMF_zKWj3jhlQxGHy_n0zWxnz_ZfePugQkVteoYNTWUpzJgD7GFFSC1Dm8k2Mqo4koH-o8t5xPcjHdmurs5zoqBpxy0NuBREVDZBvIDqjgs3j_IkPp2zssOwrL6wVKejrJ7v5CBcZFOF5KuNMSvNr6t1hMeAajPybgyqaH_ZN7-s3TgTjIiB9LEe14j2ud8_aXuY5FawIXtfgXH1U-QyZ4dAiFD3NKM_vqupYpu26Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوشمزه‌تر از این لقمه پیتزایی برای  دورهمی و‌ مهمونی‌ها نداریم
🤌🏻
😋
مواد لازم برای ۱۰عدد لقمه:
🔹
هات‌داگ ۳ عدد
🔹
قارچ ۸ عدد
🔹
نصف یک عدد فلفل دلمه ای
🔹
پنیر پیتزا به مقدار لازم
🔹
نون لواش دو تا سه عدد
🔹
نمک/زردچوبه/پاپریکا/فلفل‌سیاه/آویشن به مقدار لازم #آشپزی
🇮🇷
…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/681615" target="_blank">📅 10:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681614">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCCd995w6KfBL8GR8sHKl1guUZ6mcMjURfDnwxWhGLYCalKk-i8kiEm8l5dBjYKEhBcDNCgLYExBTLyvAzrPk4D6KwlAKrfjbVxp18yUHR8gsunv6GDwuevlYh6f7thfv5IzlngysvmVCS16FLyzD58wB5xscYYLLfog3SAXy49ysRVWP_UmXVJspuqR4zx978cW5Y3JOy44Yo5xfOEhpw8uXdqJnir6DPv-IchsHDH7kWwQ989drX2etrXmj71s2SquzmmgERBsHv6gX9msOA_uQHSqBh_lICKYRpSlvzr9DG4zqnL67SasgYX-wBFXNFr395gToVB2qWprI-NKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طراحی زیست‌بوم جدید تأمین مالی برای اقتصاد فرهنگ و هنر
🔹
صندوق پژوهش و فناوری توسعه فرهنگ و هنر با دریافت مجوز از صندوق نوآوری و شکوفایی، با هدف تأمین مالی، سرمایه‌گذاری و تجاری‌سازی کسب‌وکارهای فرهنگ، هنر، رسانه دیجیتال و صنایع خلاق راه‌اندازی شد.
🔹
این صندوق با سرمایه پایه ۱۰۰ میلیارد تومان و مشارکت نهادهای دولتی و بخش خصوصی، قرار است حلقه اتصال میان ایده، سرمایه و بازار باشد و کسب‌وکارهای خلاق را از مرحله شکل‌گیری ایده تا توسعه و ورود به بازار همراهی کند.
تولید محتوای دیجیتال، بازی‌های رایانه‌ای، انیمیشن و توسعه پلتفرم‌های نوآورانه و فناورانه مرتبط با فرهنگ، هنر و رسانه دیجیتال از جمله حوزه‌های مورد توجه این صندوق هستند. همچنین کاربرد فناوری‌های نوین، از جمله هوش مصنوعی، در توسعه کسب‌وکارها و محصولات فرهنگی، هنری و رسانه دیجیتال  مورد توجه قرار دارد.
🔹
سیدصادق پژمان تصریح کرد: این اقدام با هدف حرکت از حمایت‌های بلاعوض به سمت تأمین مالی مولد و پایدار و تقویت نگاه اقتصادی به ظرفیت‌های فرهنگ و هنر شکل گرفته است.
#صنایع_خلاق
#اقتصاد_فرهنگ
#فرهنگ_و_هنر
#اقتصاد_خلاق
#سرمایه_گذاری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/681614" target="_blank">📅 10:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681611">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efd2fb41c.mp4?token=o2uoYI3ZsA4RdudLb1odCvjciOEXYCGKp7QPfhQKPEHMcuW_wKXo6wywm9pT6oQlIcrGdeoI75PDrh6QlM2Mp7smXWXSfFYBmk-Z29VOHFkFrUzMhzB8OVeBivWFXYNC2zMh9pvvX5_7c5tm3u-cveeeC1axy32CWW39e-ItqBl10sGC-2qJ2ClL3u-osgi7r6IuMxPNxxf8P902p8o9YccIvsjZwqyPKBO2p4uOXRWShXFuukfmxgP3jkYe5oInv8x2fwWl8do4ZcN1x9iNNFKQ1ytyWOQr8OON9_r_yb0ZvcIPVvzDssQmIqfMtE6O11PtK-_awebRu5ZqCJzhpXVb_Ap2eXVG-gY4i8AUtvgbIcdXIaRErdAdqJMs8pxWamcPutltmNq7feE_hY2jrYWqZwKi5rB9xsyYzbnBBbGX8EqAD9gGZR3oL4UuErz7iufM0Tqjs0Nf2RoWD5GkIkecnUfesr5wEgNJ6vgHO2eTsg6IZvy1HdZfcTs_ZGN5dRjTrd0ghvG1D4suLG6MJe5vWEDsVmRJ0JJbx0LtW4YjxPB0BCpTmjUts2ZMI4UC8KHjShVNDi8SIzCh21GGkaoDdVuM9s1GwvMlGMuEMSx0fLDp-Kz6xthkKSiwr78DKvINXgTnH_-hEVJRyrBCrja5-OnVzBojXYp4L-LAQkY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efd2fb41c.mp4?token=o2uoYI3ZsA4RdudLb1odCvjciOEXYCGKp7QPfhQKPEHMcuW_wKXo6wywm9pT6oQlIcrGdeoI75PDrh6QlM2Mp7smXWXSfFYBmk-Z29VOHFkFrUzMhzB8OVeBivWFXYNC2zMh9pvvX5_7c5tm3u-cveeeC1axy32CWW39e-ItqBl10sGC-2qJ2ClL3u-osgi7r6IuMxPNxxf8P902p8o9YccIvsjZwqyPKBO2p4uOXRWShXFuukfmxgP3jkYe5oInv8x2fwWl8do4ZcN1x9iNNFKQ1ytyWOQr8OON9_r_yb0ZvcIPVvzDssQmIqfMtE6O11PtK-_awebRu5ZqCJzhpXVb_Ap2eXVG-gY4i8AUtvgbIcdXIaRErdAdqJMs8pxWamcPutltmNq7feE_hY2jrYWqZwKi5rB9xsyYzbnBBbGX8EqAD9gGZR3oL4UuErz7iufM0Tqjs0Nf2RoWD5GkIkecnUfesr5wEgNJ6vgHO2eTsg6IZvy1HdZfcTs_ZGN5dRjTrd0ghvG1D4suLG6MJe5vWEDsVmRJ0JJbx0LtW4YjxPB0BCpTmjUts2ZMI4UC8KHjShVNDi8SIzCh21GGkaoDdVuM9s1GwvMlGMuEMSx0fLDp-Kz6xthkKSiwr78DKvINXgTnH_-hEVJRyrBCrja5-OnVzBojXYp4L-LAQkY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت خداداد عزیزی از روزهای سخت زندگی‌اش!
🔹
ساندویچ نان و رب خالی می‌خوردم؛ به‌همراه پدرم دم حرم دستفروشی و گچکاری کردم..
🔹
برنج و مرغ تنها یک بار در سال و دم عید می‌خوردیم!
🔹
چلوکباب نخورده بودم و نمی‌دونستم چیه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/681611" target="_blank">📅 10:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681610">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-text">از سوی رهبر معظم انقلاب برگزار می‌شود
📢
مراسم بزرگداشت چهلم «آقای شهید ایران» در تهران، قم و مشهد
🗒
دفتر رهبر انقلاب اسلامی به مناسبت چهلمین روز تشییع و تدفین پیکر آقای شهید ایران، با صدور اطلاعیه‌ای از برگزاری مراسم بزرگداشت رهبر شهید حضرت آیت‌الله‌العظمی سیّدعلی حسینی خامنه‌ای در تهران، قم و مشهد خبر داد.
متن کامل اطلاعیه دفتر رهبر انقلاب اسلامی:
🏴
بسمه‌تعالی
▪️
هم‌زمان با ایام چهلمین روز تشییع تاریخی و تدفین پیکر مطهر آقای شهید ایران، مراسم بزرگداشت آن رهبر عظیم‌الشأن و خانواده ایشان از سوی حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، رهبر معظم انقلاب اسلامی، در تهران، قم و مشهد برگزار می‌شود.
▪️
مراسم‌های بزرگداشت قائد شهید حضرت آیت‌الله‌العظمی سیّدعلی حسینی خامنه‌ای به این شرح برگزار خواهد شد:
📍
تهران؛
🗓
سه‌شنبه ۲۷ مرداد، از ساعت ۱۷ تا ۱۹، در شبستان مصلای امام خمینی(ره).
📍
قم؛
🗓
چهارشنبه ۲۸ مرداد، پس از نماز مغرب و عشاء، در حرم حضرت فاطمه معصومه سلام‌الله‌علیها.
📍
مشهد مقدس؛
🗓
پنجشنبه ۲۹ مرداد، همزمان با شب شهادت امام حسن عسکری(ع)، بعد از نماز مغرب و عشاء، در حرم مطهر رضوی.
👤
از مردم قدرشناس ایران برای حضور در مراسم بزرگداشت رهبر شهید دعوت به‌عمل می‌آید.
🔻
حضور پرشور و گسترده عموم ایرانیان و دلدادگان امامَین انقلاب در مراسم بزرگداشت چهلم قائد شهید، بیعتی دوباره با رهبری معظم انقلاب اسلامی و تأکیدی مجدد بر ادامه راه آقای شهید ایران خواهد بود.
🇮🇷
دفتر رهبر انقلاب اسلامی
💻
Rahbar.ir
|
📲
@Rahbar_ir</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/681610" target="_blank">📅 10:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681606">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a82e403547.mp4?token=q86v07cfONIWkbHUB43PK4hXPsN6ly3upUHgNKYJjZuI5Kh34K2vG59skejMqWDDMFGRNKbzCT6PfrBS4BVro5l9fkZVUvDaMbb4ooxA9v4cA9E9XUKISyixzMxSqalY0oOg1QAAnD6cXc38oBzQwL08SGtg606gyr_u7bNT136pJdD_ktg6w1VsN-BbT756y3UqIUUpQjU2PYHb86OXh1191dWnfCGM1E2TfeWm4I6kSb4OjagaeAwTx40ChDuTmQFdk48jIcWgh1XGOgp3fJBno8MXb6zdg4VPotWJwuCmFfTNkwX-LbWk75As1AhVd8k88bwsfVdwmrkvI5M-cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a82e403547.mp4?token=q86v07cfONIWkbHUB43PK4hXPsN6ly3upUHgNKYJjZuI5Kh34K2vG59skejMqWDDMFGRNKbzCT6PfrBS4BVro5l9fkZVUvDaMbb4ooxA9v4cA9E9XUKISyixzMxSqalY0oOg1QAAnD6cXc38oBzQwL08SGtg606gyr_u7bNT136pJdD_ktg6w1VsN-BbT756y3UqIUUpQjU2PYHb86OXh1191dWnfCGM1E2TfeWm4I6kSb4OjagaeAwTx40ChDuTmQFdk48jIcWgh1XGOgp3fJBno8MXb6zdg4VPotWJwuCmFfTNkwX-LbWk75As1AhVd8k88bwsfVdwmrkvI5M-cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راننده خودروی مرگ چهارراه گلزار کرج اعدام شد
🔹
«شهرام صادقی» که در جریان کودتای آمریکایی-صهیونی دی‌ماه پارسال با خودروی پراید ۷ مأمور فراجا را زیر گرفته بود، پس از شناسایی، دستگیری و محاکمه، سحرگاه امروز اعدام شد.  #اخبار_البرز در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/681606" target="_blank">📅 09:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681604">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b569333b1b.mp4?token=JZyg-u5B2IF3FgLwm1SMY2Tsd-56uZl3MPH_o7IbNPwkRkz4vt86KrZwYDhUsl5w_t-7X4XAL2y2e0_FTAKzdp3V-kCb7PaDYwQ4m2F657qDxss6Ctp8W4wC5eIhpwxn322rj0pJ_5Di4HTFx4EQfhDR5Wu3niFMotwMYHitxqoOeHYfwtk3LaOQDiEvmIspIruP6bsiLV_LOHVstcL1DHyj0rpg5rniwgveOtZ2ULSssOjLvIYz-f6tt6W4dedEn2KL49EuX-PLn8H7Y4XdXl2TE6djI-s9580SO5YydUZ_yBvwMENgUHhnBMZ-ZduFEbYEdlAKme2U446iBgVBrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b569333b1b.mp4?token=JZyg-u5B2IF3FgLwm1SMY2Tsd-56uZl3MPH_o7IbNPwkRkz4vt86KrZwYDhUsl5w_t-7X4XAL2y2e0_FTAKzdp3V-kCb7PaDYwQ4m2F657qDxss6Ctp8W4wC5eIhpwxn322rj0pJ_5Di4HTFx4EQfhDR5Wu3niFMotwMYHitxqoOeHYfwtk3LaOQDiEvmIspIruP6bsiLV_LOHVstcL1DHyj0rpg5rniwgveOtZ2ULSssOjLvIYz-f6tt6W4dedEn2KL49EuX-PLn8H7Y4XdXl2TE6djI-s9580SO5YydUZ_yBvwMENgUHhnBMZ-ZduFEbYEdlAKme2U446iBgVBrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت تصویر گربه پالاس؛ یکی از کمیاب‌ترین گربه‌سانان ایران
🔹
تصویر گربه پالاس، یکی از کمیاب‌ترین و ناشناخته‌ترین گربه‌سانان ایران ثبت شد؛ گونه‌ای که هنوز اطلاعات دقیقی از پراکنش و وضعیت جمعیت آن در کشور وجود ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/681604" target="_blank">📅 09:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681602">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
امتحانات دروس تابستانی دانشگاه‌ها حضوری شد
وزارت علوم:
🔹
امتحانات دروس ارائه‌شده در تابستان ۱۴۰۵ دانشگاه‌ها و مراکز آموزش عالی باید به صورت حضوری برگزار شود و برگزاری این امتحانات به شکل مجازی ممنوع است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/681602" target="_blank">📅 09:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681597">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfDLM_uM38dKv9RdY7nzHhwfdcIwl12umEkwbDjZfGuOhQ01Ebr8U-x-LXpnBpP1sX4RRatgd245EKRXjNF4vAfqaRpXi1fiIi03teQlhC9zxBkSVJLDCvQL5MMhpWEHxvDYAfknIJeY5TB_sLAb0Z7g0hpFWYaoW55nv7PgxDsEZIJzua2QVVgFBOJCDXG6RFCoqxY04yuLgoheBhV3Iyuab1_rawSbAojzRHLA41eKdUFUlUFycq0eqSNj8udVFThtTJQfT61G5f6vFotFr_akXoz74JaAzVN2SUdU8yPPQopC_qgvmKDSZLoG1XM2Amww3_ZLHb2THFmZj4ScoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربردهای سرکه برای تمیز کردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/681597" target="_blank">📅 09:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681596">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c06bc234b5.mp4?token=lrgUd0CMitDy8OZv93Ria_6GGxukb-OWX5FDXZcNN5wnKcxxmLlDDx-yKXoBR9e6nImFvJ06TlNUZf0eOBXsYmOT-73biHQD6czd9gSe8tk2gR4xyq9bpw38q779UukRfM3qw2BHQpmMN2onroowpvnbbMm88Vvi1WZ1axx6cZZa_hnwRwYOexVjKa_6hoORpW5uEw9YueLzY2WvfSnhPSiWpH7K8wbhlbiTJ8nDoq2D59ZcAwq_VQls7X_2WkAkmp6tXq9-HGpYIYixBKNwhL1jzWGj6GWWNueF5OFnl5uEgyJXN64NoLd7lrqElIKd3tFEtvUu5JaoEp8nFzcVDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c06bc234b5.mp4?token=lrgUd0CMitDy8OZv93Ria_6GGxukb-OWX5FDXZcNN5wnKcxxmLlDDx-yKXoBR9e6nImFvJ06TlNUZf0eOBXsYmOT-73biHQD6czd9gSe8tk2gR4xyq9bpw38q779UukRfM3qw2BHQpmMN2onroowpvnbbMm88Vvi1WZ1axx6cZZa_hnwRwYOexVjKa_6hoORpW5uEw9YueLzY2WvfSnhPSiWpH7K8wbhlbiTJ8nDoq2D59ZcAwq_VQls7X_2WkAkmp6tXq9-HGpYIYixBKNwhL1jzWGj6GWWNueF5OFnl5uEgyJXN64NoLd7lrqElIKd3tFEtvUu5JaoEp8nFzcVDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرداخت وام ۴۰۰ میلیونی برای اسقاط خودروهای فرسوده
🔹
رئیس هیئت عامل سازمان گسترش و نوسازی صنایع ایران با اعلام آغاز اجرای آیین نامه جدید نوسازی خودروهای فرسوده از هفته آینده، از پیش‌بینی وام ۴۰۰ میلیون تومانی برای دارندگان این خودروها خبر داد.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/681596" target="_blank">📅 09:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681593">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d327e215b7.mp4?token=sZKkmaA4qLQR18IVSv2EHNMDr_pmTp1QaDfoWNPqxisGRIxkIdU2OnU3x-9raEoFZ9MdoV8mgPTKlBPNojigZrfNLL5sXnPshGZouwbZBSjaBrpTPqxXn9f-CBJCTRdlNDTEtHMYmjMP6zIkdOgua4zPwG66iDEzrUjrtDGrqAKnn633q5Uvd4WFOkjtJuqFvdFU8Q6H_Czp9G95rK6KqBkb87-k-yZAkPjhLXmiOx_VHl7le_PbX_Z5yhtG3VK9msUA7S7ZktCB3GIZdvNGKrF5a5n_vmESiwvCrp45PQUeldsjXx-ztlocR88B7vnGk9n674V69IjjBcoLSVt8hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d327e215b7.mp4?token=sZKkmaA4qLQR18IVSv2EHNMDr_pmTp1QaDfoWNPqxisGRIxkIdU2OnU3x-9raEoFZ9MdoV8mgPTKlBPNojigZrfNLL5sXnPshGZouwbZBSjaBrpTPqxXn9f-CBJCTRdlNDTEtHMYmjMP6zIkdOgua4zPwG66iDEzrUjrtDGrqAKnn633q5Uvd4WFOkjtJuqFvdFU8Q6H_Czp9G95rK6KqBkb87-k-yZAkPjhLXmiOx_VHl7le_PbX_Z5yhtG3VK9msUA7S7ZktCB3GIZdvNGKrF5a5n_vmESiwvCrp45PQUeldsjXx-ztlocR88B7vnGk9n674V69IjjBcoLSVt8hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روسیه: به نقطه سوخت‌گیری اوکراین در منطقه خارکف حمله کردیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/681593" target="_blank">📅 08:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681592">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad21162ec0.mp4?token=KzRTCy67dW5tPpkhqOlvHG1ehTSiqqAMUSab7O19l9-Xj1eraZPmI7ox5BE3qwK_DSy0m1r0_pDQwCs1Z74jTkLneujQLqXeHQXFYc__i9hLj6MlFRF2hOtO2Nk9QC_cKPdzhWJzfmFqK1zIbFAv6Z5uocapiuDWrcK_tqpxmo3fB0bGn9vIehGF6FWH_Ndnfexmmm9NSmJB1i9FReLSfeE0SWkw7rxFQOl6Gewkb4jQpYl091fhD3G8PCVH_Jff42ZVrUY0pGUV947vX3hfAQqSzzAGdV5JNPVvoDQJWifXV52FFevdMx4cvv0z_WO0M1JTzQd6k4GST3gn2FW2Fg5bWCdLwG1qPHzv_F-6uobb1vX3yZpGnV_finxswdWo6XS4WkxwJ5y5P7x4ZMsJK2km9doRvn8lIB1q-cnuvhqTsf0DAViBNs95wZ5WiWVHZqSDinu3pXyqxp7EIEuOT-UK3GNh2uPfFBDedmcFqSyUVJkmTfpAFxDABLHSWk-27_Nq4AyHTakFIHdgi6DfGUBimcuC42ETn47MhjKYiPhC2NjxXcZSlvZ_yt8Ewn9wxfOzd2VqlrihY06zI3Gz2SozcLZGesngSyRm98S7wyNMcCAVrEuTAnJ5NjAaZVccHOnM3yqYqtBiyoam0JczLCZCDU_xYuhqK_JAXRCy3os" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad21162ec0.mp4?token=KzRTCy67dW5tPpkhqOlvHG1ehTSiqqAMUSab7O19l9-Xj1eraZPmI7ox5BE3qwK_DSy0m1r0_pDQwCs1Z74jTkLneujQLqXeHQXFYc__i9hLj6MlFRF2hOtO2Nk9QC_cKPdzhWJzfmFqK1zIbFAv6Z5uocapiuDWrcK_tqpxmo3fB0bGn9vIehGF6FWH_Ndnfexmmm9NSmJB1i9FReLSfeE0SWkw7rxFQOl6Gewkb4jQpYl091fhD3G8PCVH_Jff42ZVrUY0pGUV947vX3hfAQqSzzAGdV5JNPVvoDQJWifXV52FFevdMx4cvv0z_WO0M1JTzQd6k4GST3gn2FW2Fg5bWCdLwG1qPHzv_F-6uobb1vX3yZpGnV_finxswdWo6XS4WkxwJ5y5P7x4ZMsJK2km9doRvn8lIB1q-cnuvhqTsf0DAViBNs95wZ5WiWVHZqSDinu3pXyqxp7EIEuOT-UK3GNh2uPfFBDedmcFqSyUVJkmTfpAFxDABLHSWk-27_Nq4AyHTakFIHdgi6DfGUBimcuC42ETn47MhjKYiPhC2NjxXcZSlvZ_yt8Ewn9wxfOzd2VqlrihY06zI3Gz2SozcLZGesngSyRm98S7wyNMcCAVrEuTAnJ5NjAaZVccHOnM3yqYqtBiyoam0JczLCZCDU_xYuhqK_JAXRCy3os" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گربه‌ای که ۳ بار زنده موند و نجات پیدا کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/681592" target="_blank">📅 08:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681590">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
نمونه‌ای از غذای در حال سرو در آبراهام لینکلن
🔹
یک ملوان حاضر در ناو جنگی آبراهام لینکلن، تصویری از غذاهای سرو شده در این ناو را برای یکی از اعضای خانواده‌اش ارسال کرد و گفت که این غذا شامل مقدار کمی از همه چیز موجود بود، نه غذاهایی که به طور شخصی انتخاب…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/681590" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681586">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0297adfe5.mp4?token=lu9cvvBbqI0If1_dZJm1v97dDeMRpqfM_lQ9x1IHpO2jbZpmSSDf79o2GKjheu56j8r9BzPEbxLpgK4tASquXEw72y81zH8Fa-Edaw2sS6ktIw6tt6Z6bb1ahmQ65sRmWc_IOnBMPQFIcaUjYatkzaD9l85F28gkK9qE16zGmjNg64ZKEshPuJ6UwgnUQVAvWWSAwuls02VBAq8WdDixAnA7awoSEUNCjkh9m23gkdy60alfo_u-eKJl8sWIVWS8u1FPXSgJQZxEytZCRsXrtfSAXFYlZOFzCEzyQ-6qstAG2aKH70kefQzVdus8Gtjc35XDS8u-GUBOadFJKCN0nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0297adfe5.mp4?token=lu9cvvBbqI0If1_dZJm1v97dDeMRpqfM_lQ9x1IHpO2jbZpmSSDf79o2GKjheu56j8r9BzPEbxLpgK4tASquXEw72y81zH8Fa-Edaw2sS6ktIw6tt6Z6bb1ahmQ65sRmWc_IOnBMPQFIcaUjYatkzaD9l85F28gkK9qE16zGmjNg64ZKEshPuJ6UwgnUQVAvWWSAwuls02VBAq8WdDixAnA7awoSEUNCjkh9m23gkdy60alfo_u-eKJl8sWIVWS8u1FPXSgJQZxEytZCRsXrtfSAXFYlZOFzCEzyQ-6qstAG2aKH70kefQzVdus8Gtjc35XDS8u-GUBOadFJKCN0nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرین کامل عضلات شکم بدون زمان استراحت/ بدون نیاز به تجهیزات در خانه #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/681586" target="_blank">📅 08:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681584">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSbk6Lvtto7IX180-r34H6xyBgeoMreW06y30kwjILwxlS6Yl7TuKefwr0hcGrwfMuREmTmofrs2v0BZJflTe-XDMJSa4OklPBs6_TrkvWiM0KnZH8FjqmVKOIbr3O5pkvk54mUyI-_O6p8v7zmVlh2w8e7e8mD7D5-heRchuB6xKdUCM1-hwnJsB3i5Ay-WBSML4TmnzuxMLcQhMvfp3v4FDHNeakQsqJxtdAbqPxw33B14iHF9GQAp9TeJS6XXqoP1vHRleIwG8glp9y_fRy5BXrZmZ4paaZyRS36CkgOrz8G6PrOdaFJI17K0snBbxkYIrFwjBwK5e02GgX2YvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دانشمندان با تلسکوپ جیمز وب نوع جدیدی از اجرام کیهانی با نام «ستاره سیاه‌چاله» کشف کردند
🔹
اخترشناسان MIT نوع جدیدی از اجرام کیهانی را شناسایی کردند که ظاهری شبیه ستاره‌ای غول‌پیکر به اندازه منظومه شمسی دارد، اما رفتار آن شبیه سیاه‌چاله‌هاست. این جرم ۱۰۰ میلیارد برابر بیشتر از ستاره‌های معمولی انرژی ساطع می‌کند که علت آن وجود یک سیاه‌چاله فعال با جرم ۱۰۰ هزار برابر خورشید در مرکز آن است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/681584" target="_blank">📅 07:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681579">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کالابرگ سرپرستان خانوار دارای رقم انتهایی کدملی ۳، ۴، ۵ و ۶ شارژ شد
.
🔹
فردا؛ آغاز توزیع کارت ورود به جلسه آزمون های سراسری و دانشجو -معلم
🔹
هیات حماس برای بررسی تثبیت توافق غزه وارد قاهره شد.
🔹
آغاز پروازهای مسافربری میان روسیه و سوریه پس از ۱۸ ماه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/681579" target="_blank">📅 07:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681578">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSn1NHVnyWVukU6CCGgDCLtGQNRgBSvMPEj9WOPDkTMYwT_yg2ZzKY3X8ULFuIFg3S-yvk58l5zZNm-4dfcS4lXiCAVN6FErdjXnzdUBMjsoaJOo0sqV-KDTuyzQs5Fr2zIwcgF1h6_UsFqK5Wyb2h97-HoweeDirSvTqc1gV9A7tPqVOskV7OHEP-kgL5ly6wW1BOTezU9iMrnPn1XJDUU2pNQnzrpTaSDGAHo5CX8hboy8Ayq_TD1iFAj23AC98Svvo1aEUcvrpC_MqQ6NvtBuXenCHklDaUcAIFXfX8Gj2a9gGg-pg464nyrh0ox4W0iqHWx-6ggz_ladRp1tGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راننده خودروی مرگ چهارراه گلزار کرج اعدام شد
🔹
«شهرام صادقی» که در جریان کودتای آمریکایی-صهیونی دی‌ماه پارسال با خودروی پراید ۷ مأمور فراجا را زیر گرفته بود، پس از شناسایی، دستگیری و محاکمه، سحرگاه امروز اعدام شد.
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/681578" target="_blank">📅 07:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681577">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-CxuO33JGdSNX7og1PqbawKVF2wX-TOsxBfQ52N06Z1gE0O84CqjJ1HJHFntOEzeSTQZfBqQ0aQ8ZH81wr32JU0HIV49-_3OYme9uQn7zN7wc6USDM11XEvXiUvx6xGC_zqfjWMxn88dtrZTbbaRSyDYEaMavDgAKJykUTs63kUrD8Y8YmsmnLjD3r5eEzJlGDadCVBZ-8I0Z1YuQ2OfMTPsdRp6-HXO2pl09OHfY5Uie7s0ZlJ00xwbqL8HxylWAEpW03OS2y66Ez54N18AoZwdclMnGgd3e8tIVTB73RTC-PhgW7QUn9vpXEinItOBkGCmrvRbs2b2ajgs7baTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۲۵ مرداد ماه
۳ ربیع‌الأول ۱۴۴۸
۱۶ آگوست ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/681577" target="_blank">📅 07:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681575">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hx_sRBI3zx1qj7FtU4nvNHS47pSzs2NdCKTFou6sHPxnyEa8kDxWrqkdnu5LgXrL3gU29uYizJpaUvR3MQv3m4EsbNk-eacWGWgVCf97PcFVBDCerwlJzfH0tIN2qBtBZN-cXtzTQcBnYzvJT4LqcbpxJwIbWG7T8gWQBNeLvoi95v50VFeUqEH5SG_ezZu-kmBpoOgnex01OGiiYCGWB5MYo7o48KX3ewvsJ_xoF8p0PfZX4B3-4wW8KvFdOyaQv_sqjvIenHsvfcrNaI-vfGXTEiIICjDXceQbkgntT6qAwsj35jLXIXTUfsGPIAFhqiB7b6Uw6-BGdxX-u1tngw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
اگر دانشجو هستید یا در ۶ سال گذشته از دانشگاه فارغ‌التحصیل شده‌اید، از شما دعوت می‌کنیم در این نظرسنجی علمی درباره کنکور و قبولی دانشگاه شرکت کنید.
⏱️
زمان پاسخ‌گویی: حدود ۱۰ دقیقه
🔒
پاسخ‌ها کاملاً ناشناس و محرمانه است.
پاسخ‌های شما به شناخت بهتر تجربه‌ها و دیدگاه‌های افراد درباره آموزش عالی کشور کمک می‌کند.
برای مشارکت در نظرسنجی، لطفاً وی پی ان خود را روشن کنید.
🔗
لینک نظرسنجی:
https://harvard.az1.qualtrics.com/jfe/form/SV_6MsiAUIGfXgJZQy</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/681575" target="_blank">📅 02:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681574">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eM1iI2fxmr39AhFDbugaofArTnM3tlBVTBIYoNVwgC0sXbZ-POqyaIwqhIo6UWHow0g69afxCnwGKuwsXp7xjzT6F5TUwOxsFJ7lxXLjYSlJK-VUsrKduX6rwJzfzLqQ9fWtfc6tAu1P3ViNW0VF60ds4h7eTbG9SXXWEUroeI5U-Be88hNuypx-8mgoh5Zdd1h5vMOlUzBoxwJuo4CMcRcjxHRe3n69sXumfg3RlkSH36k-w9pCddw6OHiSZ18VmAP23G8iBezI9bfYWrP-WfIQ3Y6m5H1d0AyYGRBouNjrufa8B_CUBqjrWr-Wz_4SyxvejFteLUhrms3eceyuJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان تروریستی سنتکام نقشه‌ای را منتشر کرد که در آن، نوار غزه و کرانه باختری اشغالی به‌عنوان بخشی از اسرائیل [اراضی اشغالی] نشان داده شده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/akhbarefori/681574" target="_blank">📅 02:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681571">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSt2o1H-ZtKNxamatR3HZKr3bJgcIiZn-bmAYPHGRrSoZWv-gMq3sLQ9Ax3pQrLWnjoek5Jb4Vquo40LzO-8TbsoUdMIOYDrVJcd8fUc483nsRAkMwTRnng3Mk1zt-xtG_OpImsy3Frqcf4HyQgdV9ou7CFp1qm-FHvxkseAFBhAp_uw2BoPxpWrySsjUxXkJ_KMZ-LNNjOy3lQtLapfwzu3mY3WMHfALCaE2ZejcOK1-7qGJy_d_JSeXm1xChBg919EH68XRzIsMaFG7nl50tmEQxS2lSeaAEH0Fmq8nMKak9rcZ59KkDwbAhNRcAgw7917uNSdsH53YVmSNXgGNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمسخر ترامپ بعد از فرار با کانتینر حمل آشغال مواد غذایی از ترس تهدید ایران همچنان ادامه دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/akhbarefori/681571" target="_blank">📅 01:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681570">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fI8p9x_INacqvzcbLTzbGGgww11k7rEdTqfQi7A2qGq4q6-9llXj4huGkqFvzwgkeJDWDkvCE4_46nmfpTD4FeWi3YytqwpZ03NSwEt_Z05ca2ayBD8IEp1nbljz-Z3eRzMetmb8vqb772TobCRohFV4hmrOBPSSVhM30dGw1DxAOt1VgYD_1U-vqMdX8bBFtBksJUOJTsU1Cq_L4cZmudMzPgjjoDsOcXVrEkMSdEmWaflSEdFxSn7VXEsEMXvndokGNN_gF6SQAZGGMZ6uWn-LwucOTfqzTA1aWt25WD4VJKDm6OnARPixHvgBk3Sw1U1O35XLA4p4AQiKCM7caA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابراهیم عزیزی: رئیس‌جمهور آمریکا باید نگران امنیت خودش باشد
رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس شورای اسلامی:
🔹
رئیس‌جمهور ایالات متحده به‌جای ادامه تهدیدهای بی‌پایان درباره تنگه هرمز، باید نگران امنیت خود باشد.
🔹
ممکن است شرایطی پیش بیاید که خودش مجبور شود برای حفظ امنیت، در یک کامیون حمل مواد غذایی پناه بگیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/681570" target="_blank">📅 01:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681569">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c2a870060.mp4?token=AtsmykZ0ehqvkFBRA88pWAlw5H-HlyBP8-e_dA7jqOdpkTUGsPw3CbxYtJFkSX9lL2ETD5QZIRr_E_2yv28ByFXrTAywxGPt8XvOUmkKt64asE9gWV5M9jjJdFxfWgWQgzc7W3YdBOgB9-Le-mEUmpe8xhgTCepTat_aDdl_3VTHUC3rlv7ZiFEE8Vmhk1ZP_Fj_-WivcsNmpix_9qlXnu54Dd_37wNs4_wkv0TFMdAAqVNuL8EUJMxqakvmNucMMwG_c0XLan02Pmw1ufl_3H2gIq2lzG0XBKzzvWS8_nEeB4AO8r5EVfrpi1cUjs8jdNtxkUuY1Gy9MenBEbyb-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c2a870060.mp4?token=AtsmykZ0ehqvkFBRA88pWAlw5H-HlyBP8-e_dA7jqOdpkTUGsPw3CbxYtJFkSX9lL2ETD5QZIRr_E_2yv28ByFXrTAywxGPt8XvOUmkKt64asE9gWV5M9jjJdFxfWgWQgzc7W3YdBOgB9-Le-mEUmpe8xhgTCepTat_aDdl_3VTHUC3rlv7ZiFEE8Vmhk1ZP_Fj_-WivcsNmpix_9qlXnu54Dd_37wNs4_wkv0TFMdAAqVNuL8EUJMxqakvmNucMMwG_c0XLan02Pmw1ufl_3H2gIq2lzG0XBKzzvWS8_nEeB4AO8r5EVfrpi1cUjs8jdNtxkUuY1Gy9MenBEbyb-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فارس: روز گذشته ویدیوهایی از برخورد تعدادی از عزاداران در مشهد مقدس منتشر شد که در آن چوب‌هایی به سمت هم پرتاب می‌شد
🔹
این فیلم‌ها بلافاصله با آب و تاب فراوان در رسانه‌های ضد انقلاب دست به دست شد و به نادرست القا کردند که این درگیری در صحن حرم مطهر امام…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/akhbarefori/681569" target="_blank">📅 01:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681567">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a538aeadb9.mp4?token=X9T8xy4i8yeyAa-7VmBexS4HPDZv9-3NXgF5sg3Lgdp2TJw4BLyO611eMJgJGwRoqWe0b4PlZL13E7kzjegUYrJDxzRbQY94qktOV9Irk-FLBjmiwyaud4lpN_HHAn1wt5xuoZD0BUNcI_756rbqMPnQQRIanZ4ribp9esJAAPbnVoTReflmPACQ79OEDSmayvj3oBhq_ZRJD072aRWUUgvRnDW1vgoEl-8ssfOKAsxOAcvc_PB52l1-3VHiWxPXWtynVDPAOGtlzFNuDgJYGScmlqNmcWz7Wnq1QhmoZXu9nG20MipG08aDmnGSlDG-i4NyDV0wUrnAIqnXJNZkbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a538aeadb9.mp4?token=X9T8xy4i8yeyAa-7VmBexS4HPDZv9-3NXgF5sg3Lgdp2TJw4BLyO611eMJgJGwRoqWe0b4PlZL13E7kzjegUYrJDxzRbQY94qktOV9Irk-FLBjmiwyaud4lpN_HHAn1wt5xuoZD0BUNcI_756rbqMPnQQRIanZ4ribp9esJAAPbnVoTReflmPACQ79OEDSmayvj3oBhq_ZRJD072aRWUUgvRnDW1vgoEl-8ssfOKAsxOAcvc_PB52l1-3VHiWxPXWtynVDPAOGtlzFNuDgJYGScmlqNmcWz7Wnq1QhmoZXu9nG20MipG08aDmnGSlDG-i4NyDV0wUrnAIqnXJNZkbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه سبز شدن چراغ‌های قرمز حرم امام حسین(ع)بعد از دو ماه عزاداری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/681567" target="_blank">📅 01:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681566">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-poll">
<h4>📊 کدام طرح بنزینی دولت را بیشتر می‌پسندید؟</h4>
<ul>
<li>✓ طرح اول: قیمت فعلی؛ توزیع بنزین تا سقف ۱۲۱ میلیون لیتر، سپس توقف عرضه</li>
<li>✓ طرح دوم: سهمیه‌بندی بنزین بین خودروها؛ مصرف بیشتر با نرخ آزاد</li>
<li>✓ طرح سوم: سهمیه بنزین برای همه مردم، با امکان انتقال و خریدوفروش</li>
</ul>
</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/681566" target="_blank">📅 01:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681565">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
سومین طرح پیشنهادی دولت برای بنزین چیست؟
🔹
سقاب اصفهانی، معاون رئیس‌جمهور و رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی: در این روش سهمیۀ بنزین به‌جای خودروها به مردم اختصاص داده می‌شود؛ چه خودرو داشته باشند چه نداشته باشند.
🔹
روزانه حدود ۳۰ میلیون لیتر به حمل‌ونقل عمومی و تاکسی‌های آنلاین و غیرآنلاین اختصاص داشته می‌شود تا قیمت آن‌ها تغییر نکند.
🔹
تقریبا ماهی ۳۰ لیتر به هر فرد می‌رسد و امکان انتقال و خرید و فروش آن وجود دارد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/681565" target="_blank">📅 01:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681564">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
دومین طرح پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
🔹
سقاب اصفهانی، معاون رئیس‌جمهور و رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی: در این روش ۱۲۱ میلیون لیتر تولیدی روز بین خودروهای موجود تقسیم شود و هرکس بیش از سهمیه بخواهد باید بنزینش را با نرخ آزاد بخرد؛ تقریبا مشابه روشی که قرار بود در کرمان اجرا شود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/681564" target="_blank">📅 01:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681563">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d76db735.mp4?token=h11cBVkYhz2fridAWe8ZGLarGeTV9147KsJlO_bWNlNrzqJMcKn3fQge0k1gbpjjUv7AeoubII6MpvBLhO418Iekhq9Nptq8QiYRXdXK2_ES2duVtLE09VW1-sEOSEHvf34eNVOrEo-vL5FmVWRfl5tzkBG_qpPHBgqkc4bv0mFi0svA2cJs8fj9_swwBTIKjoydrZ4BtPvPCVBNhACCEgLASZGjtkk_s2fB3k_rVAlQuk3L7Ght7X3sJqUtFbCdx8UtT-5PTNsJXiFpA9kw2W3eKctLUYW9A8NZS4roL-5gAQPRYMTaq-ZSfr6Lpvqz3T0fdgx2rFHtSVOusR1yjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d76db735.mp4?token=h11cBVkYhz2fridAWe8ZGLarGeTV9147KsJlO_bWNlNrzqJMcKn3fQge0k1gbpjjUv7AeoubII6MpvBLhO418Iekhq9Nptq8QiYRXdXK2_ES2duVtLE09VW1-sEOSEHvf34eNVOrEo-vL5FmVWRfl5tzkBG_qpPHBgqkc4bv0mFi0svA2cJs8fj9_swwBTIKjoydrZ4BtPvPCVBNhACCEgLASZGjtkk_s2fB3k_rVAlQuk3L7Ght7X3sJqUtFbCdx8UtT-5PTNsJXiFpA9kw2W3eKctLUYW9A8NZS4roL-5gAQPRYMTaq-ZSfr6Lpvqz3T0fdgx2rFHtSVOusR1yjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طرح اول پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
🔹
سقاب اصفهانی، معاون رئیس‌جمهور و رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی: در این روش قیمت بنزین تغییر نمی‌کند اما بنزین تا میزان تولید ۱۲۱ میلیون لیتری در پمپ‌بنزین‌ها توزیع شود و وقتی تمام شد، نازل‌ها خاموش می‌شود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/681563" target="_blank">📅 01:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681561">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTJZ40_d0pLzdRqcuv4GJ-cRX022sy2s4BoOFkoFLQV_wHIGq63sfd56AIQCW41fji9aL2XqdCZiDPt6mkw7syBFaAUbGiEYINmjVBNFxwcHUP0E8QRhxKvLbRInudyOuSWtUOzCIryxQJ1icR_SfRor3oHXbgDmV88ixO41fw-F3BmdL-ZR8O8EZi8GjOJWG-SStfR1ARPZF40oOkg1NgoJX5HZWMc4tG30Iyqwqxs-6Bg7nkjcMUQjnJy6QlpT3eYi-J0X047KnlGI-othi6CQgv1jqEOtJagaU6-2M98RbC-ct1TM_1tNvXWBVg2TSp9yl6VnvOU3naSexbIvdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌بی‌سی: کاهش ذخایر استراتژیک نفت آمریکا به حدی رسیده که نگرانی‌هایی را درباره آسیب‌دیدن مخازن و توان عملیاتی آنها ایجاد کرده است
🔹
ذخایر دارای یک کف در حدود ۱۷۰ میلیون بشکه است که پایین‌تر از آن، «محدودیت‌های سلامت ساختاری حفره‌ها و زیرساخت‌های پمپاژ، مانع از برداشت‌های بیشتر می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/akhbarefori/681561" target="_blank">📅 00:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681558">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUf7SUnzKmx53O0jib3OJdvOL5Dw-lJBeKQAts2cDRE1TQAm3M_gau18wNu8w427rjUY5qet5ZtaZXjRxFJeXTPq_uR2sPNgNLdRhkoe_joCgeE206EvtC29r7MJVWXALgYt1YO0N8Bmo2uoMinrySAsQyYryJoUCSCAnpJSbHH9RniXKgv5C_YnFMuGfWD8kVXHua0VYWkf-D14of051eO8CKaU5Ap9GpkGyNjf6hh40N071Pz4KfjCcPV141Yz7wepc_bS1a4qizgSF3BrG4mIV3CDHluwcnW3u8VhZVEzfZaeILIjcwZDzEwTabe0HIERf2pSY2OQK_RTWx9DXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ کلاهی با شعار «ترامپ ۲۰۲۸» بر سر گذاشت و نوشت: پیروز خواهیم شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/akhbarefori/681558" target="_blank">📅 00:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681557">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe93a20077.mp4?token=jSoaG4WBy_3DjosVzLtvBS-mTeM-oycyZQ1NOVIuPcbPNQoCEehF0ZmbQL_1wB5GpimnKukrDbW0NWLRK05TsRy1ZVOcJJ-rZZg05G5Vt8jilkBbiCc0Uv4q1cFHSWA-CUIuBk-DOGWFnkERGGOjoo3NZErwmI_kkmzJCbkx2TsbQc5LQDQ2hgKIFJbRKTN1Z-WUGMM1by-GHehLF6hX0MeiA9SnnMYsJOoCu8dVey7VXEdNmqWDHYI5FmJCrqkzjAjVENP9gPFpK3Njc0o31sUDtMlAuuRZt4dnSeKhPITletA8GdzFTfU56hidS_Gf8Ro8LIb4WeMjUXw4HSPdtZBzDiCSlEsXPC5VQnIeJt_DggmjgF5zwx6RfTLXSXMOIY2GrY8bnGa9_U75-PYXcRZyi-TqAZ0GRvIrQdNRCXZ_xmf0dVndS9ppKm2W_ujp1x9PMUFnycz9ArfsrPb9bv_D9oIbzhvmgpUxbxU_MTBIawaiQ68GD6toB0NhsUi0pSvqTftoqUcWXBVH9YJ8EU5R6WPSwwTKHIt_EYaxB6jhg4jqfbGndfwxZKSyi7L8KS2AYr_YNcMTI9y_oIf2_Ut0EQgl2Ukm2fBaWsmI6s8A6Q_33GPMW_Y8EIAd0fP8amNrQfDhBKyvxRET3XmNXWClKxkK6AZRXNzR_2f0GSk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe93a20077.mp4?token=jSoaG4WBy_3DjosVzLtvBS-mTeM-oycyZQ1NOVIuPcbPNQoCEehF0ZmbQL_1wB5GpimnKukrDbW0NWLRK05TsRy1ZVOcJJ-rZZg05G5Vt8jilkBbiCc0Uv4q1cFHSWA-CUIuBk-DOGWFnkERGGOjoo3NZErwmI_kkmzJCbkx2TsbQc5LQDQ2hgKIFJbRKTN1Z-WUGMM1by-GHehLF6hX0MeiA9SnnMYsJOoCu8dVey7VXEdNmqWDHYI5FmJCrqkzjAjVENP9gPFpK3Njc0o31sUDtMlAuuRZt4dnSeKhPITletA8GdzFTfU56hidS_Gf8Ro8LIb4WeMjUXw4HSPdtZBzDiCSlEsXPC5VQnIeJt_DggmjgF5zwx6RfTLXSXMOIY2GrY8bnGa9_U75-PYXcRZyi-TqAZ0GRvIrQdNRCXZ_xmf0dVndS9ppKm2W_ujp1x9PMUFnycz9ArfsrPb9bv_D9oIbzhvmgpUxbxU_MTBIawaiQ68GD6toB0NhsUi0pSvqTftoqUcWXBVH9YJ8EU5R6WPSwwTKHIt_EYaxB6jhg4jqfbGndfwxZKSyi7L8KS2AYr_YNcMTI9y_oIf2_Ut0EQgl2Ukm2fBaWsmI6s8A6Q_33GPMW_Y8EIAd0fP8amNrQfDhBKyvxRET3XmNXWClKxkK6AZRXNzR_2f0GSk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قبل و بعد از لوکیشن‌های فیلم Terminator2/ فیلمی که هنوز بعد از ۳۰ سال کم نمیاره
🔹
جان کانر قراره آینده بشر رو نجات بده، اما یک ماشین از آینده برای کشتنش برگشته. خوشبختانه یک ترمیناتور دیگه هم هست که این بار مأموریتش محافظت از جان شده!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/akhbarefori/681557" target="_blank">📅 00:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681555">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPv8a1ac_TS2RtZ2zlqmh10PlOaA39yNO_TiN7Z2jm1ZpxiZG-mrkKB6W8_SXwbJLcFXOlV9T6mWtZtM9TZh3XrhI2yrNqf2U55wMgVlPavhUNXAAdhm6myj2ceW1ImRXBsF7CtL8QuQEQOxkfdtZLNsiDfKBaaxSSUSxCBOzO45c90LuflgDJtO78Vr9WO5sHN9duCnPVqP_dysaXtE9E-JXYaOCQz-Gz6__t69lvVvYdbfgp4qjJXQ-remZP9WMJMp-VwQbll9wFPnmQ9psloyDXZQcS6rX9EowJT-lOG8VxY4s-Hn1svMeRrZzMNzXjhvBKyNE_oc0Ebecs5b6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/681555" target="_blank">📅 00:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681554">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔹
اگر فرصت مرور همه خبرهای امروز را نداشته‌اید، جذاب‌ترین‌ها در دسترس شماست
🔹
🔹
اسارت ۳ خلبان ایرانی پس از سقوط جنگنده‌ها توسط نیروهای قطری
👇
khabarfoori.com/fa/tiny/news-3237866
🔹
سه طرح جدید در پمپ‌بنزین‌ها؛ بهترین روش سهمیه‌بندی بنزین کدام است؟
👇
khabarfoori.com/fa/tiny/news-3237983
🔹
کارمند اخراجیِ اینترنشنال: هدف اسرائیل تجزیه ایران است؛ چه جمهوری اسلامی باشد چه حکومت شاهنشاهی
👇
khabarfoori.com/fa/tiny/news-3237989
🔹
طلاق مخفیانه بازیگر مشهور فاش شد | پایان بی‌سروصدای یک رابطه طولانی
👇
khabarfoori.com/fa/tiny/news-3237659
🔹
شغل این مداح مشهور طرفدارانش را شوکه کرد
👇
khabarfoori.com/fa/tiny/news-3237906
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/681554" target="_blank">📅 23:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681553">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9f8143e5.mp4?token=G8HFU-R7vAVSTiLf3FWjz-ASawl_xJGzAJlHJQsMwpKInvX0Fcn3m94RbYUo9AuAL-4qX7lwjU1FvHgJA94GokeS8Yoj9zAbD1CWHAuY0AZka8a3KF5bxLkzNP1EMQTnSJ2ifAQKkbxGRXYmGDkzAwocw2nPtpsbz8zfdjcn66CB3UfT1MnOOJXqwfzReOOcGla1StQJzNJ7wghA3J77B3lIxVnQjd78MPMZq7_1oO4Gpw3HfKWoS9VKwLIbH30x0V5W9yDEptNQaR4qf4xKFe8UxP_fTj5e74y5zeL-gAHDieN1tM2rcUU2llJA-pHsiZzAjnDPwm_9hC2zubf_Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9f8143e5.mp4?token=G8HFU-R7vAVSTiLf3FWjz-ASawl_xJGzAJlHJQsMwpKInvX0Fcn3m94RbYUo9AuAL-4qX7lwjU1FvHgJA94GokeS8Yoj9zAbD1CWHAuY0AZka8a3KF5bxLkzNP1EMQTnSJ2ifAQKkbxGRXYmGDkzAwocw2nPtpsbz8zfdjcn66CB3UfT1MnOOJXqwfzReOOcGla1StQJzNJ7wghA3J77B3lIxVnQjd78MPMZq7_1oO4Gpw3HfKWoS9VKwLIbH30x0V5W9yDEptNQaR4qf4xKFe8UxP_fTj5e74y5zeL-gAHDieN1tM2rcUU2llJA-pHsiZzAjnDPwm_9hC2zubf_Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمایت از تولید داخلی مسئولیتِ ماست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/681553" target="_blank">📅 23:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681552">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
طلای جهانی دوباره خیز برداشت
🔹
طلای جهانی پس از یک موج اصلاحی، خط روند نزولی را شکسته و دوباره نشانه‌های قدرت خریداران را به نمایش گذاشته است. این فلز گران‌بها پیش از رسیدن به محدوده ۳۶۰۰ دلار مسیر خود را تغییر داد.
🔹
اکنون ۴۱۴۷ دلار مهم‌ترین حمایت طلاست؛ حفظ این سطح می‌تواند پایان اصلاح و آغاز یک موج صعودی بلندمدت را رقم بزند. امروز طلا در محدوده ۴۳۷۵ دلار بود که ۱.۱۸ درصد نسبت به روز گذشته رشد داشت./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/681552" target="_blank">📅 23:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681549">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dddeac06e.mp4?token=lshtcS4dS5zCVpgsu1xQRkpgXCOKM_zmzLYyExTl5AH13zj9M1mDzDQ6WhqJR-9qitQHOXJarMuk9nJL7-zNR37XmoI1q1EXn5YHDYuy34iYwhHzuRkPdxzh-NZ3tpyBVpk_ROksDlHpRDn-f5VbKjbhAqNNtGmigfFsKDFOvT16JUbq9WsIKcj1WiWC4jObWX5yh9ERnsWAT_Qv6XCM0fIJY0ZRLhfWsBVcjjZKRYFF4qfJCDikmyH-2HvPJ-I9d5BVS8GXyKIDVXKFm9_Agqt0VwMSOU653JeMSzHo_fAZOPAR0M5l-kfZqlc4MR39HKzHZ6wLC1qViO757z5STA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dddeac06e.mp4?token=lshtcS4dS5zCVpgsu1xQRkpgXCOKM_zmzLYyExTl5AH13zj9M1mDzDQ6WhqJR-9qitQHOXJarMuk9nJL7-zNR37XmoI1q1EXn5YHDYuy34iYwhHzuRkPdxzh-NZ3tpyBVpk_ROksDlHpRDn-f5VbKjbhAqNNtGmigfFsKDFOvT16JUbq9WsIKcj1WiWC4jObWX5yh9ERnsWAT_Qv6XCM0fIJY0ZRLhfWsBVcjjZKRYFF4qfJCDikmyH-2HvPJ-I9d5BVS8GXyKIDVXKFm9_Agqt0VwMSOU653JeMSzHo_fAZOPAR0M5l-kfZqlc4MR39HKzHZ6wLC1qViO757z5STA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیوه خاص مدارس ژاپن برای تربیت نسل آینده؛ تربیت کودکانی با مهارت‌های واقعی زندگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/681549" target="_blank">📅 23:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681548">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xx_XLi2tgD1sBRXUvicM738ditdRnv4spvUvqnKh8RK7yYhXAdz0cZSeTfX-7uv9UlVICatSAOeY5pgl3Hg06Ilpddk3wwAi6NspQL-8ho8v8CXMWQ3rTLyNCJniGhOndV6gkg2QBaE9w9ZXmF2QicSNHX8fk3T6dAa-WgFKCoJdt-b8Fb5kEcZe0kTwqfoZotJTCC7DHo5Of5vbwLlthpULfCunTwS7On4nAOZYQK5-nWFopPUk3Vwa8i_36dIDXBXKxvrqa-7iC7Inu9e3oOmaeneGCF6o3xL54d07W2xMaSoWKAzFxFsGUxg1SLEaiTfF4LxLifQ4L2QWcgQhLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارین پالسی: بله، جنگ ایران واقعا شبیه ویتنام است
فارین پالیسی:
🔹
ترامپ، دوست دارد اشاره کند که جنگ کنونی و درگیری ویتنام شباهت کمی دارند زیرا با وجود لاف اولیه‌اش مبنی بر اینکه کارزار ایران در عرض چند هفته به پایان می‌رسد، به طور غیرقابل مقایسه‌ای کوتاه‌تر از جنگ دوم است.
🔹
با این حال، برای هر کسی که امروز آن را مرور می‌کند، سخت است که تحت تأثیر این نکته قرار نگیرد که این دو جنگ چقدر با یکدیگر اشتراک دارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/akhbarefori/681548" target="_blank">📅 23:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681546">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb1b618029.mp4?token=HvCRN7-zeKRHR9R01wnyZBvMX9peuzpgDx-VM3RxZrYfblWubErRqWfQNkpR3JYVtrqGWh4aJk3UXixny5z_dLJVRdGEw6bCetHhIE4ZZGpKJEm6Q2t-72PFsCYYyRyfpX07gvIBoD7jUrkjZ-PCQe8B3cvLbaNy8bGVfIyHV3IjTOcqIoef9rOVpH2KBoh9uvkM6GWlYA6aYaYyLCNWnz706XYEc_iQAylVqhA8vSfPrzh7yDLeAzvpg2IHwiRHXttitsxcLx5s7h9D3Me209wEIqxq5ntOIhZvzPCRytW4fKaWo1PodTpT4FT93ZzWb6AQNwQ_Qp7gRZ1uhhq1fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb1b618029.mp4?token=HvCRN7-zeKRHR9R01wnyZBvMX9peuzpgDx-VM3RxZrYfblWubErRqWfQNkpR3JYVtrqGWh4aJk3UXixny5z_dLJVRdGEw6bCetHhIE4ZZGpKJEm6Q2t-72PFsCYYyRyfpX07gvIBoD7jUrkjZ-PCQe8B3cvLbaNy8bGVfIyHV3IjTOcqIoef9rOVpH2KBoh9uvkM6GWlYA6aYaYyLCNWnz706XYEc_iQAylVqhA8vSfPrzh7yDLeAzvpg2IHwiRHXttitsxcLx5s7h9D3Me209wEIqxq5ntOIhZvzPCRytW4fKaWo1PodTpT4FT93ZzWb6AQNwQ_Qp7gRZ1uhhq1fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غول روس در راند اول علی اکبری را ناک اوت کرد
🔹
در مبارزه اصلی برای کسب کمربند قهرمانی سنگین وزن ACA علیخان واخایف غول ۲ متری روس و شاگرد سابق بوایسار سایتی‌یف در همان راند نخست توانست امیر علی اکبری را ناک اوت کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/681546" target="_blank">📅 23:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681545">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ورود هندوانه و خربزه ایران به عراق ممنوع شد
سید رضا نورانی، رئیس اتحادیه ملی محصولات کشاورزی ایران در
#گفتگو
با خبرفوری:
🔹
عراق هر ساله به بهانه افزایش تولید داخلی برای ۲ تا ۳ ماه واردات محصولات جالیزی ایران را ممنوع می‌کند.
🔹
امسال نیز از ۲۰ مرداد ورود هندوانه، خربزه، خیار، گوجه‌فرنگی و بادمجان ایرانی به عراق ممنوع شده است.
🔹
باتوجه به مخاطرات جنگی در حوزه خلیج فارس، کشورهای کویت، بحرین و عربستان واردات میوه و تره‌بار ایران را ممنوع کردند که این امر منجر به خسارت به صادرات ما گردیده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/681545" target="_blank">📅 23:22 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
