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
<img src="https://cdn4.telesco.pe/file/OcA9oU9QPTndMhxsxWOTHCWJ3bZrVdUZ5TrO6Hw4XQysfrmOCnhntcXrMhTkC6Fl8wbodEgL7Y3hExvjtJQ7lbIqUG6pFNOmGNHc6XsEIAB4pwJ5O3BCBAt63X5crSFWwIYWVrRFSaqf4PpuTSsRWEoGEx_-a8P2_8Wds8A3i-NK-5PBaDrUfV_KgBRohoSK3jbOnushSuB2yj-7chp7JqIX5m1UtKsS27Xg7igjtHL3GTk3x8NdAkj3N63LukTd0Uiinz3lSpWvSq1BtPe_2RVkXQhkSs9DeIsSIHX_H76QA9UShyZEQgC3qSLJ2c4_TWAVajQQpAnGxH-QRHMDUg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 585K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 11:00:43</div>
<hr>

<div class="tg-post" id="msg-26533">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f10IkFTZeAnG0mQW9KqpyZWCcyHI557L3hPbGBSpdaL0hB8Xs5W1KzTb8jvqEfqx4ayPhp9YjkZLSSgHXJt2X3nA1xxL6t2hHmLhraFTkc4131Cv_Xo1HsiWTJX3m02l0-OzYYOnW0wiInvXosq-RQJX4odDkbsx7WvXhtUYVIhGr_lj-FVN81zFz8_zweL9A60905vC_9gdTw-KLBBcL-OAY2GGoQ8bny1XoGk9ExIGXKfkM_Eh5f0N07a0SRZrWc-W4WL3aKDVGFKffwu0BURKJHFnleX0F4svzOnneB70jByud3cySovsdaPJgLHjPdjZHF1gqbFrogGaNj9U9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مصوبات جدید سازمان لیگ فوتبال در مورد نقل و انتقالات در فصل آینده رقابت‌های لیگ‌برتر:
‼️
افزایش لیست بزرگسالان هر تیم‌لیگ‌برتری از 20 بازیکن به 21 بازیکن؛ افزایش لیست زیر 25 سال هر تیم از دو بازیکن به پنج بازیکن؛ افزایش سهیمه لیگ برتری هرتیم‌از 7 بازیکن…</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/persiana_Soccer/26533" target="_blank">📅 10:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26532">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4_2XYAWcZ6-9bsLS50OGFaaQVpEr_QXGe4L8djHhp5jf49KotNjj3xlOb6aduNSfalLai7VfNg9FGXO8d7LTdfqUOVR7MQNBHC7b3MKYsdbX5-Jovz8zNkzvttgcw48R8Xp_aGzlXXFSL71n__COuGxuaoJgPVNafELt2x72N1PgBl31GSLxnXmcygMDNCD4gT-vS7bzfjONF7xeBq0vbaavsGckLG5b2BtZQq5uxHCFVfK8D6QotcIC0NXMlMlcRCJR90SwT_i8PKHiAdR5joMneqft86RJrDtDtY5DQP_jDfTiS_7fgo4EoUhhNTtLG-rvCLfWbupjGu538cmaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/26532" target="_blank">📅 10:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26531">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWwuJTUf98mouHzKY_GVZ_-IvaWVMs5S6bE1iYKjUi1qulLhdGtkLmz7vmIycghjTBAt2tZNIRYx6PeHcbyHAPO32Fu0X81Q56qqGpJuQMk8EiLnq8NRevfwJbVTAsnm58pPVeY5EhKVW_rz19BwPhYV7HCIFkuFILbgGuuG4FrdHvs2Ex8JEz-DdcSL5mXqu1dumDlDUM9H_MwGgKekjjAW-iH5_vPHZOXyeKV_tQHzWWjhS_zIj6UO1pe8kwEbLVBTWCZYq8A3GYupmYG0XFnCsj60NYrLbByMkPKwdqD_fgTF1TFHFlf_Vmf5aZ5gwuk4DSytooypq_pKAPAnSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه‌بدونید بعداز زلزله ویرانگر بم، باشگاه رئال مادرید اونجایه‌مدرسه‌فوتبال‌تاسیس کرد، استادیوم و مجوعه ورزشی ساخت و درنهایت بخاطر فساد و پارتی‌بازی‌مسئولین و فرزندانشون داخل این مدرسه فوتبال، کلا منحل شد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/26531" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26529">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=LwxnxGFrKzPXjFJNzA-PaFTGSEOmfz9TKivi64Hh8yK2SsH_4qqP9b5P7aevZJat5igMqvQeDkteeH-PT-LGnL5Z_ElebWotjzX707UwFawZLBu8MJ-_dZDnpLjVNMQyoMuZM5Y-lPHjI3_82PZJ6dwGcOt6P63ImnyA7jBmdTKB3pJHPTVPvm_2G4BOlmvAm4x7HnaGCtvrC2C-PNTUUCTuPpD3Ahhjv3QQ-Ad9wW9jmb-IBv-EOR4biL9EwpnvhAXvE-3Soq9dGwOtry4UXSZWYYXutDhSkvrkf_7hlvN63loU2CuWjrsVvHnk38OHOYf6DQiuyWInCMKN9pm-NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=LwxnxGFrKzPXjFJNzA-PaFTGSEOmfz9TKivi64Hh8yK2SsH_4qqP9b5P7aevZJat5igMqvQeDkteeH-PT-LGnL5Z_ElebWotjzX707UwFawZLBu8MJ-_dZDnpLjVNMQyoMuZM5Y-lPHjI3_82PZJ6dwGcOt6P63ImnyA7jBmdTKB3pJHPTVPvm_2G4BOlmvAm4x7HnaGCtvrC2C-PNTUUCTuPpD3Ahhjv3QQ-Ad9wW9jmb-IBv-EOR4biL9EwpnvhAXvE-3Soq9dGwOtry4UXSZWYYXutDhSkvrkf_7hlvN63loU2CuWjrsVvHnk38OHOYf6DQiuyWInCMKN9pm-NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی نوستالژی و خاطره انگیز از تقابل جذاب نیمار نوجوان مقابل رونالدینیو در لیگ سری‌آ برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/26529" target="_blank">📅 07:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26528">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9X6gOLn6kpt-86pKG3WWbLK13wG3ZgGS96-El9WGsaMYr8P9QLLdEm0wnIQ7OCBBUF4IcVCnobRkrk--nnCfOZ7pUKLJy7OOyfGWGXCf1cgJh1tmNeyBn8q5qgvXwVc5qMozy4PxaxoahnDV_kL767V62-sfbR15fjjqupi3t0B1RQtO_fPAVJZo6E9DM2Wtci4S4UDtnLzC_a3m4FCxLHHYAmNt35x39K4p9OPv7B-11H34jOKNEmH2bdtMgmOVpooV5m66Auby57VoEEXfAiguMrmZRRjySTt29BzzZvfYoPPcrfsSVdLM5UpHsHWK6_qFG4ddSQ02rXiDHyjmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/26528" target="_blank">📅 01:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26526">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWW3GF9MWkjS4dPreOUBx3gyp2rJh2CzbvbykEucx6f0A-u7dfDf2HYgelLMODa5kOl9GN2Kkngkx659mMVty18KZH_eLmNd-FoeofBQ5a-fFATsJI5d3GcBNEp0AfOHnDQ_KchmsepeEzIJZLOxAKGX4q5IcaGSoA3Lq_AAtLc7csaRnDbVr9NSzXIFoGo_PmpZkKs8PN97X4LGFZagM7r3HzhTd7My0wVCdT7dCCi4I2bJ2-fokuNX4336z-0uo63zBjS90wDSybWzuPyBi4qgJW1lmvMrM10r0U6PW32E9hYvTrh-O2npUE-GdYM5BsCneJ8pFdwCHDAUN6vOXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ جذاب دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی شاگردان آندونی ایرائولا برابر ساندرلند در آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/26526" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26525">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlbe0LozYbzoGYxo9d4gxRQOpFnISs5buboi1oDCcjGE48dy6ZWtxQzX83uqYKXAsQqfaRxDLYdltci9_-AlIt4b3nCtiqrYligbIxijkIbOq3JGu0ETY24fev23-sGKJtYfebJF8bLjIk-3M7MVR9B_JQl9iBskfp9o0F9XBEsph14KG7mXZEpAj9jyY3S41_EtIwkSgtvpQbHbqghMQwysCcyDoqtpGi-vUqO3U8KTktJev1HLQHsJaAn0HwaY_tKtlO7U0koYjI1465uvCMFP-aveujf1-akagHoBbYiS_fTYWeRYCYLmhmQIfhX5pxjOZzv3hLcQF9ADu-XQpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
توقف روسونری مقابل سلتیک و برتری‌ماخاچ‌قلعه‌درحضورکوتاه‌ حسین‌نژاد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/26525" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26524">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvQ5Gz_3tBlyImysuBTtGrz0h4qzim1kQZNHfN187S_07R4Deb0Y1snYQ6WKKpP9OS4LQBIPoh-0xTZ593bOfFfmA5CfFG3YBvyLvfoLZsaCujC_K1Qh9KXDeuW_6V2D6tVqAXlvh9jfIGXuGb3_vIs9nwifRgE2Qd2xYOwbz2A6gaTJnXs_DSJdlKiph8o_GCsJZ3d7aoPMpS8gkKrd3kk_e1xnHdbIfsz4K1EiEWty9EdYfCkACezl8_BlRZhwAc4yDce52uLLURhwys-0Qj9LY1etS3WZ8ExFEaY5qTWiuVt5PbSGN5bQQVW8xEOhlzTSgsW1x5mu89aBuk9oxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/26524" target="_blank">📅 01:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26523">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgWqhqSaGo-LfI3qw5FM6-oJ-nQkrqvzt0vB_9qnnwVzpwAZ8YVB2U-Zp-jNP1j6UvXhIFgiH6hNQETBwrmEMHiA8ENYPDljpmVi2RtAXRDd9OvIXBvC2AYYF6ozxkwID5BlswDCt2hVg9ETWMxUJz3VczYnlS4DLJ_iXcTnTs0bAtZhn3jyQWbTf9X4vXn7F4pCBXi0Cetz-C8K__TV4djt6hs-yfS-37X1c9Z0tjkz_FaVnq0yQ4I4yOnX7SZJrfs4qgAM1WdgKMfX944M4JuHY3sPUO-qcSRnRYShHVQ_AlRu5TwDkLHm1Sq4B55149VTMFwhpzt8rfsioo_Lew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
یکی‌از مسئولان سازمان لیگ؛ خبر فسخ قرار داد رامین رضاییان با باشگاه در سازمان لیگ رو تایید کرد. بدین ترتیب اگه پنجره باز نشود و رامین بخواهد قرارداد جدیدی با تیم استقلال امضا کند تا نیم فصل مجوز بازی برای آبی پوشان پایتخت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/26523" target="_blank">📅 01:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26522">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9gPe1-SD9TcaKDeboOb-ZCmQdBISlIC-en0zloiPu4Le8xW-NOxTh0NroLnSy5dUa_QmFariyrQKctyzPSQBoDkwuTViFmPhPaVX-4wjBE_ugWplrwfKjQWChAaRWUivTpNI7DmUBak-7mmNK_3vAfBb18fmHPqXwIQ3ZFTnj2gzztUv6g-Nldtj_wJPLcFJnB1VgC3HZgqSDMofPMca5KqxFHi-M9FfzEIEifvABDdiCbppRZb-Vzx_4bjzBPcdxTGyGNO34AgZweH8kf46Pi6SykBzisSKjJrKD-6gt-xgQz4I02A-bEkD3c4ktaj_0VUTGiAXpwt36swDBoPpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/26522" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26521">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=uIPzfpxm1PWNsPu79RRefZHyZC8CcVv1vLiZBbJEeTYAtm6AB0Kml8cG3DB6fzEJ6pPsg4HrN-fxKwQzJ4ETgT-aAt5-v3u_JJn6xgUIehT3JS6Nj4wYIDg4Utrtj_RdOS-RcT67t37GKxwrgLqMgNBjxQNerkwJ9vMqhvIU9Ekh_GdntNWIbR7iecQMEfmkn-uKtTzcu5YyI2xxgU2eEbHEEtQwt3hRz5LtoL8kOgvxoi8Zh71hzEZjx-maQ2JBlxUYCjWkbVF7tYW55i2DUa7zb4xQaMoqnbrbcne8cPPFtdlt3Zur4zIfU4SSaANceT2HaWo8lX3_k1MTkMEeVjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=uIPzfpxm1PWNsPu79RRefZHyZC8CcVv1vLiZBbJEeTYAtm6AB0Kml8cG3DB6fzEJ6pPsg4HrN-fxKwQzJ4ETgT-aAt5-v3u_JJn6xgUIehT3JS6Nj4wYIDg4Utrtj_RdOS-RcT67t37GKxwrgLqMgNBjxQNerkwJ9vMqhvIU9Ekh_GdntNWIbR7iecQMEfmkn-uKtTzcu5YyI2xxgU2eEbHEEtQwt3hRz5LtoL8kOgvxoi8Zh71hzEZjx-maQ2JBlxUYCjWkbVF7tYW55i2DUa7zb4xQaMoqnbrbcne8cPPFtdlt3Zur4zIfU4SSaANceT2HaWo8lX3_k1MTkMEeVjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/26521" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26520">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv7ZOnse_drPBq3lgUoPsgu-OMSsxRbcnBud81ixO7SFgEwbFNebKHENpLsXEpX-vupVKj4o0EnbMcY84FoaDy15zWYtC15E_T2cMLKGE68oTabyODekoU4hfNWJ0ZIXRHDa9B5dKeBkbM21ziGwSO1bafMbCB8TjRcLsvTnjjLxf0hwJny61AQvwBtkqPjiAdu1AVV_FA8xnSHN_3yF7DwDkzXFc6uFdJWEiVHKtEFWoJRouIPg_A3ko_uIH7tgaWJKAjnTHBxlHXaHgjeKflP6tjOgl-nyM3K9QWLNEMzxd0yvb_BHhljE_VnxrxWmd391Lp0d3kggLa4bOV4vFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
👍
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/26520" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26519">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aidk2iBT0I0yxrZeTc4IfHGIPV_cUMRVrewmJlYM07zj0iczcRISIFowSTK1d15pACP9i0MRyIRQc383fShyZoPfhLTTNrRsTnAHZxtMGh9pqzrjdGkKPYdN9a-OARCt95NWwWLJL6EXMWNcX-5WDQ5AOnuoOuZLHSYuYOyptusYKeC6MBG2XjpDCwO5bhi81gZUi5F8V2QAD8OXnFot1Xjya5Ktozusd1NKk3YOEGzcVRmoj9wRPowi3NvdMRRU42XJ_vnp6yxCu83iPYcGCqtXAgRqeFG_NswpEfzxL5_uIulk1d9BbOHgINGdLjI2oWizFYOhDmgb2xpRIeie_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛بعداز رونمایی‌از محمد خلیفه؛ اگر اتفاق‌خاصی‌ رخ ندهد باشگاه‌ استقلال کار های انتقال مهدی گودرزی ستاره جوان خیبر هم نهایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/26519" target="_blank">📅 00:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26518">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuW2fPiJ33hgQFWZzkSRbl0DHaQdIyxjMVCvsKkGArrq9n15FecW4i_7AG9WsV6iSR-Say0vEbaoMLEoJ3TrKVkaYZWQctC93VnJmmvzeqpnJXggDel_nKbLx5TqZ4hfdl9WOjjHhC0KFoNQwTIdWxMckq5qrcG2wdg6MiM_iN8iE8YMLYpshrNce7hmCH1Pz44TamzDYJY3RSakElU-ySz7vtWzBkcZK4wqiMcClcyvymC6-mu4d2061gzxqSczgLXtBxzFQF1q2kR8Q45gKDnuT25F4OBO56lpiw1onNUndihjnt63efG9mpWMAWP_dHi0TYqP3dnEFtffBlwmjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رونالدو و جورجینا هم به این‌شکل در تدارک گرفتن عروسیشون هستند؛ این چه سمی بود اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26518" target="_blank">📅 00:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26517">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDBAcHEqAo91YxDi238AxWj_twwFPZjsQ8lQlbO0MGuUQ5WB6S4IA_c1lJDyxKQoLPNrPM8FD6QcG9Gl23xvtlgoPzmDXO3kWqBGJefXHI1sblCjukph675nZNlcxPZH34dtQv4sAxgHUjnOpIDmCnCA5eR4FgWzfQKaiL5VerT8dSJYUiMGtHSVP5kZ1W-IikB6GsSdYpj0JL7zvV6tSUnmRdYO6F52gdXf6jEogJApu2M422LqTEu5pqP_LrMoHYxb0PkxpUkH_bIO-QQ31Ql9Ve0Nudt0TZIK6xksxlXRzkKgQLWRh98_aZNJPKsfWH5IID3dVf4dQ2X15CxCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌ازدقایقی‌قبل‌با مدیربرنامه محمد مهدی محبی و خودِ بازیکن تماس گرفته و در تلاشه که زودتر این بازیکن قرارداد رو امضا کند. به محض امضای محبی در کانال خواهیم گفت. دو تیم پرسپولیس و اتحاد کلبا بر سر این انتقال به توافق رسیده اند و فقط امضا محبی…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26517" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26516">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAMgDTbw4OJ_rFYZiZeDAZSsS3xfc5HWGNV3GvC3Qo-mZrT3BMPOUFkkxIjsn7jBPWdJha2bahi7qC8SRB1s4hut5daQ03IjF3jl33fx4FMEZ-v-R93eslrHFMRMkE-RJm6m4SJoWkQwOZWaO87IPmUui9k1tNTpX5BPh71V_opTa7TAua27LhFOLa_ghDXlEXOog_Jl7VSV8fQneNB23c_DIFf6sgnzUFdM-zbGoxeYZh7slgBNOPa4fjjKU4Vv7hDYNEE-CGTcSve6vCGmgiqwB69gJpU9ggHrRI6kP1K7Cfexqf7PRUoJZ-507-xd0xXtZVGbck8xwSlAfa3GPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
"هبا عبوک" اکس اشرف حکیمی که دنبال ثروت اشرف بود و بعدفهمید که همه چیز بنام مادرشه، بایک‌شاهزاده قطری که 2 میلیارد دلار ثروت‌داره رسماواردرابطه شده. هبا و شاهزاده تو جریان جام جهانی 2022 با هم آشنا شدند، زمانی که هبا هنوز همسر اشرف بود هم دنبال ثروت اشرف…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26516" target="_blank">📅 23:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26515">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUQ1qCL8jNAG744ZxELh92aMe4P9L97d6vrzk2SHkvtLb_bIfYU10jheDbZkOglF1oryquX4NcFVXsgn_eu2A-rOi82lwOFvBl6y8u2Y7wktsVD1SEZvMD-64C64_X8A60KtB1HRYYblgAFfVHFRH48lGpeDitfnrI5ZDhsPhH2Y9wjv7TukNd_S8Z_SB7DDtmLzIFdbROZLij3HNzEHJVjhSZWqYBD8GzggNml1SWYOomKCFYTHx8WQxVL32D34ULL_IoefNxw1LJT0BsJCEBV4kexXjnt9hLUVX1TBvzgZyESBGnx9QySAUjKdurUxh3LRnvAo0wOxBPVVtcVOHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی:
باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26515" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26514">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5E7eNKT2qIVvi5dNfSDtnp1NXaWvAZNlGr2wWg8HXRpNAIWgf8tyvr4irtG0B-EgeVillD1R44ic8r-I6EfeIQ4pRzT4Ph7bma--ea6z3UP2BTjTcVT1dACLZhb2ZQCrjs-lGm4_IAq9tM5tabNVkJe-Mf367vwLtgeh2sgD-cd66YN7cY-PCREsB49IPA6YavucuPvidsM9Xn16vsgwpuYELpIbebq_5bsZybs_4V6JxvSwz5AjkKsiFjlXnPDrlgcfYjRpBLYXe6JRBCFbo3YX19H8oIOy_KWKaAmuyHJ1GWOoO359Sdrfeu6tukJ4iv36RnFS5dSc-KSfpR3pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#فوری؛ نشریه ESPN: یان دیومانده ستاره 19 ساله تیم لایپزیگ باعقدقراردادی شش ساله رسما به باشگاه رئال مادرید پیوست. باشگاه بزودی پوستر رونمایی از وینگر جدید خود را منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26514" target="_blank">📅 22:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26513">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By9ATaF82wq-bqytN7YlJJ_9Dq81MopwtIz2tUDz3xY2B9Gee_WhxNi2taDbJRj-u4cvAbzTXmAzCvxk8qjjQO5arpSjXGGewvARGzegqzE3-XKEbRLLEOtQdi0KriQ_HpnhVNMXA-U5udXbsf5Ip5nGFdXet1Y9nH3VukvrGE6TxvGC33nnce1cT0So52XXB7o3mKHnLoR6hbtmJXYsAR-58cN-5AvDF1HFVik-XZsHYlG__2d1tAsmZf6sH7tpHAhvaIZRl4retrOR1DALLLWQi0Z5ka2qQYKQcB18yhbCE07JR_BofJGH8Ylmqd2NggquNff2xVqDyU5bopL70Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین پیگیری‌ های پرشیانا؛ قراره که امشب حدود ساعت 23:00 محمد محبی قراردادش رو با پرسپولیس امضا کنه و رسما پرسپولیسی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26513" target="_blank">📅 22:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26512">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t38KPbavUbvzIRjEkIhTFQkYwzTU622JmZWR2iBu3KKxp3en7DQbbEiuWFzF0cPV6PmKRTICF6ARmK5Hk8aLNVpOs1ayxVFh-p8ZPpOAB3Egi9belCIfvlLhwNEg6_pCWkYoLVcpcr6nPbFCZTVhiDJcSXl4NEihL4Z5G0S1kjTLDKEKGFxNasvGToxuauq--L8kr4OMdjKEsCfdPdjjbvjlWDg41UViG2-RH-seDL6ttBi2UhJJxVMhYil17qZLWXM_8c70AtENTqcwlW7em7JGv6qWxDjnF4mU5rV18gC6c5Rj_4jc7An0v1Hy8gltGmzsug5dhpPZV_f7B1W8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال ایران عالیه؛ مدیریت گل گهر ساعت 2 با جواد نکونام جلسه داشتند، ساعت پنج به سید مهدی رحمتی زنگ زدندکه‌بیاد داخل جلسه، چند دیقه پیش هم خبرش‌اومدکه‌با رحمتی 3 ساله بستن تموم شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26512" target="_blank">📅 22:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26511">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmOaMaI_EGthyf3RM6rUWLPtBAjlt9_F-XHgiQTpJyAlB1Vg84iASYe1PCM9Ed3PGlUmhdbT3igYKInPvlH7HB5nt74lri1oLA12AkLFzB46eZgBQMqy_l0-4TnL0mGuUYbndmeg5_J1o9L9bZkwWpcxfIY8zWrsFNzC5zK3XtUNqKqrw-Fk0HbseHLpD3yvfGp7nBfUhP_iEFHDpJ32kIL5pvRpk6mDOKiX5r7EbeCuh66az43xcceG35fX3jlmqP1O3Hx2EqSIC7fjMvb_mzZKXdBD_4sUBLyBW8O8ul72ec1Z3CBiqa_DARD6a2MxqhCcx_-l4nTAzaoD_ZzOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26511" target="_blank">📅 21:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26510">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8Sc-6RmjIvzPyeIXXk-sFoczMWuu21r7bvpLquGn4k-DzcJ8ZfShKVDoMKdk-OZPVs86JxzNkLZJG-4-ckPXHj0oaBgIprO45nwV50SDSxvtsK0cUAPPjilwhNSqpVrSknzGjNipuyL5wM1h9FEzZV2b4ZQFuvy9twDW-fI1KF2_8FdSRtMlVn_rh9OW7GV30D9CFUsmwGSHgpWp8w0eU9fGvDhEjZJVxjl1NOMynQlhXH8ZVs_Qq3PeKY8u9j0ypAl8DL91pXtyMPdHE5WM7eYytwkUASzH3qLdEQsvs9EGHMtbpXNJWDhoPSZe7GaWfzJdGP-8vC7MNb7TN0lGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26510" target="_blank">📅 21:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26509">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2v648g7XBLlOqyf33MAqZt0SIemMiqPrM3ps9BNx_eHqZnnHqL8gOE2rBz1AMFCHg-pHWggFM6dr0D2EYkVEKP8yRKhxKpUNxvXgkQFAmxfAcdj8cUSyex0nSSF3a8buJGioiioD16nqV4AbLNkzmtNz5-xjtBJm1TFNbILR-Oo7Kz_7UXr8d4HJ_lwAnTrr0HrY8JaycHd3NS2JdAZweCscZqQBWGIpWWehs_L-3K6cuaZfOVWTiuwAr5kiCV_raw59w87hfDW4yZPaCQCJo70Qla_tTTK8vELARvJ7ROjbT-acY3AXQ5moS_QJV4ef-Codms0R8mwIY7d_aKWsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26509" target="_blank">📅 21:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26508">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVQGAksTKQ1E8TPXj0_Do_X1frdx5AJUONaE5Xx61560V_yYFgjwN9KheVJNA90K_0b7vx1Zwvr167jPNXSSpKKQQ0KXUnbip8_zVStW6Wmks7qGyROfO9u0TjQpfY6YJ0JA-_RiDt865f5RoAxu0w17y_GoxotcedUk018P5myaZfpI9Vx_iUUPTT1kiOUiSCKbE63-MNj_HjNIpOIaz_sHDYG7-y_tmDOwJFFxOOST0thjgw4fZdlBZ8_7mC-HAZfNlXUKKf_hu4rmlXSkH8M0_YsAz63s-s3UL7Z4HU0qjLgmEu6D1Qejo94zniPWQUJ107f6y-YCbbIIbPAvow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/26508" target="_blank">📅 21:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26507">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smz0PI0c5HKvLc7bO4R5RJvg56gs5sicfisVgEmIllco5AjOGrPJ-GgZY-8_Ce2KxfYkwnU06Oq2Ul-PvYz1VATLfdLzt6nO8oxeeKcGCYPJr3RGxeWNbVENLVJ3fYik10a6uUC7k37nX8uRNFPWC74bS4Tqm58Ycm1xpgxUObiKPmM32WaJC0ew7pWSy5JsqJk9eWVovRDtgRVM424-rMMCyUSKdW2q0eizwh2GXXMcXbhaUgGnz_2kyAwrAyT1Qs3pZG_TdrAb8TYmhX0TN5-ZmcdKqAzxLMAjSl9LI66mZUX45hpK5-kIEC2Jg7CafhuoB6FN-AJsueJp8dO6bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخ آغاز رقابت‌های فصل‌جدید پنج لیگ معتبر اروپایی؛ تنها سه هفته تا شروع لالیگای اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26507" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26506">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qqyf4EKDs4MqWd5WzfZdW3W5vcYrOgp-yxlUuCC3z2eXaNC7-chpa4_4rOhSZZgfof1TDYHJXooQEg5w08Pz0SK3SqhTwU7LnJoa5L2j_ck16xxpLygYUmVUjOFI_IR-5G3RSM4VHxXv2HbMxsFVZXMSZ9DIqjFKAx0PeNyr_OqKsvyHAtzahsu6CYX7DtK13TQT_MTqKP7fgPYmxLJU8Bso0cH_r4E-Po9qE-IHa3QhkVbfTkGcLhmLJamynyGDgteVjhZ7YoIbpLtwdECIDXqfVuDWuAVyMSeUMYz0gtFXcNnVi4GaeFanLxlK7p7MZSLjy8aouYNawdQMAywdnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسکای‌اسپورت: کارانتقال یان دیومانده به رئال مادرید نهایی شده و طی ساعات آینده کهکشانی‌ ها 115 میلیون یورو به تیم لایپزیگ پرداخت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26506" target="_blank">📅 20:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26505">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luTPWpcPnLqr4mz2nn08iGYe0sacM31lPslM-zx2jHYVT8ZRaAtQHdUptiYYB4mDpTTgCTeSFwG_DCOdY0ZG-CkayVtMQV3goStGJ73n2XOhpDwGm5zJZHT6IPJhaPNZRiGcGvcHKGGmRAsvoT9_ja2RJiH48wdxZyx5OYTzFbp1bBOowyU54spYOj1vpzng1X9o-WYwPjDdVdUgWPLUxTa2-VX7H0mQ1NFZQvEEqlEcka6WqV5WbpTsb95UjsEMLo3e7F1sJ8Z_xFdRfLxEhMAdYL97i1dXgLpmk6iaZUWg_f2sst4g7rUAEIhOGkBKTkY9dKv-vPjWgjsZzKExjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26505" target="_blank">📅 20:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26504">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAxjVksORu4ZryNskFloRwiLWCKB13fYEgg_QiXtISAxAs8rmWXxETmdGsd-K-JZeDqcVU9zrpIEaEGh4AzdhKbxcvthLm1d_PAYUmWg4jRUoBYEJZEhKeRCfN0zeNYPSL6mLyeLHupciEfFmGifGc6dDeY5qpzZ0JD3eQtyuehPMtedy0nMg6t1NmxreaHSubHjFKHgrJ_DqlPw4hSIcDcmctcV5boLo3zn-W_yUwS9ScvfT_VQsxivSs3i1BOvUDQLxnqPa0clzhm_ssR7B06Og13mbNe7ELF5FF6QHWsO-J4viexCyhj3VFymSB5D56uC6Qw6nlWGlOY9tM1Ypg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/26504" target="_blank">📅 20:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26503">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HN6j_B590iqREK5-qNI_jn3wGrn9JyJRFCpPF0EvzUSbvM5cToDLc6vZusSa3kGW0pR1SOs6liMSjvq6fHayI1zdDmsEfvzHWdmieWF7Nzda-7WPpmwjoD8AZQ1BLqfg-6YGfT4VkWD459MP65KJ_7soXdU6h0FpoWnxsXZx2uhHuGupaEPXjpy-tP50qwTDTaPnnoYjcyqL42LbKl1O5AGA6De0J1WzVvG39ZH8Xe8h4ut1XVxB91Fbf4HJpDTkEUk2LJGfPK9oeZcPhqNfeYjYfUWFBHT44BvDlP__5A43aBr22OfodhGnTQgqS4tkAJydh6Hu6mOZJh76lEZ0nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/26503" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26502">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=KQ-mvvCU-l6rwY0XIoR3LHp8A-ONA5I4jNEpvLzsgoh8G4fT_UDcFY0nFh8ckermAXDQluVkhdUxfMXFXpp_OXbWOJc-sEpysatvL9U48D7qp--pwB1DQgoA3YKokQYKx2OumgXzz4-UlPDQBEjCn2kb4XOv5KSAV6uj1ZMTFlWMfNSVz6PtcFPY-JW6lWhSrjxmru1BHAT1uyPJ_XeJgppvl0aRuTmF3M70vOCJq_oZWkZ2gbCs336OuOGLE1xodV3Xr2Jk5_7Q0ISPnz3I68D3aMGXMD95hHiGnSBhICBl7Wh0wy6ePGmnXxk-ODFyfiYcoSU_9lkNIbhnqJTyrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=KQ-mvvCU-l6rwY0XIoR3LHp8A-ONA5I4jNEpvLzsgoh8G4fT_UDcFY0nFh8ckermAXDQluVkhdUxfMXFXpp_OXbWOJc-sEpysatvL9U48D7qp--pwB1DQgoA3YKokQYKx2OumgXzz4-UlPDQBEjCn2kb4XOv5KSAV6uj1ZMTFlWMfNSVz6PtcFPY-JW6lWhSrjxmru1BHAT1uyPJ_XeJgppvl0aRuTmF3M70vOCJq_oZWkZ2gbCs336OuOGLE1xodV3Xr2Jk5_7Q0ISPnz3I68D3aMGXMD95hHiGnSBhICBl7Wh0wy6ePGmnXxk-ODFyfiYcoSU_9lkNIbhnqJTyrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26502" target="_blank">📅 20:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26501">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iy64FGMCR0OMFK8MoE8bLxm77OGaQfm-oUZKkV5MO-3ytpCaN4Gt2H8b2YvpqPYQmUzbOS1tqohgYihfPg9Z2hxqpka5JQ8J7p_2NTm0-1u-vYriovzPDFbPa-SSac59XxtwS5YQs3aRJYNLTMO7oib_7O-Dus2jOKxsykmbUIfrTdjJ5G4qR6ZN4re1dovAb95KAAtl_E1VV8nhLJRfEOxd8vJlzwoas1gMIaM74cEIfP5HFUpI0Zsz1OWTGoHf-nfRNb_odxdJmD1tPhGo2T8IfZ9GoCvssEVd58veuFyYHuxOuFGcLSZPIY1FKCpReHc9tPjqjWj1_svAf_an1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ یاسر آسانی دقایقی قبل برای‌دریافت مطالباتش و مذاکره با آبی‌ها برای تمدید قراردادش وارد ساختمان این باشگاه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26501" target="_blank">📅 19:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26499">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pq7B59ss8MtuzMnjRgN9xPf_2n_xjxw7FKiLJD4dmYkLqYZHd-1n1veIDyRE8Ca_jMO6GdtRcvKYFmBG7p0Y4RelXgUIk7-UpYTlDXIWH7pzwBEeJGN546iBM7lhBPP4AJByH-OrhOeYA0MdaWvw_dXQSRcVVFgWstKN542uxHtS2nlBp79oSf50l8H_xzhoDtk3jdJz_2-I07fs_iGwCoLzmQP_nhdwFDAsAnCGIyFuIY-M1KnD-ddkS7vsNvVZmBt5MCpB0s35govNGJMx6q-j-xrps99sFynF8wiAJpmZ_64T8TTUvaqZwceDaF7VxUi_Q7swR6doUK3wAI1jAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#اختصاصی‌پرشیانا #فوری؛رونمایی از تنها آفر اروپایی‌فعلی محمد محبی ستاره تیم ملی ایران
🔵
باشگاه لخ پوزنان سه روز پیش آفری دو ساله به ارزش 1.8 میلیون‌دلار به محمدمحبی داده. رقمی که برای هر فصل 900 هزار دلار به‌ شمار می‌آید. باشگاه استقلال نیز آفری‌سه‌ساله…</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/26499" target="_blank">📅 19:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26498">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujP6i54xA_dqwHrwqePbYNfxCNzKrztmnYrVLjnBJ93Y2qPUcaiO9VSbAFpFu_9iEuE2Yu00F-5EjwYOutps-1jU2ePXCPf8Q7sfBuiwalca5TryAKdc_1_60wxTZXRHK0-9pCdgk02Wu2iZWqacMFJTfcEKYgjCNiNoQrYnXMuTPFDDz0TeIBMYp12rOcmrjgosGSk8GoBUQ-uervfqF4CcKA-H8V7wTvAJRcG0_iig4HZevMS6jFi_q6oCPV2Kt-5qcaPkFMxslP2iIbrsO3t725uOvTuuYyYFfWEHLFhRIwmm5y9qPF1_AkE1CJMYMK4OZBz8maJQ2RBVepx11w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/persiana_Soccer/26498" target="_blank">📅 18:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26497">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=iSn1WxMoQgu-gNgsOZw9xUprBNBgLKYJScLyhB2_pe3WEwcO35g_MhR9S9t9akO_WRxYu0ojYkdnCKjfWUNctqQBkBGK-ifgrknh99yuzpkBUv8_KYeaNVgLqbfTyW5VEVQ45Vzm3CT00sPm81iONgUTJ0RoF3B_OB9VTSozXI-U3K5i-jWtkaI_N9ciKKrow3wuuUX2mTKuGKw1y0stQUEvTYw0B6mU4w-u-aWMThZtR83_dEQhBFQ1Vk5Jde7i8zLBPVAvMKkJ4FGSFZT1cf-8cruWWZeLfi_1hEmBrRygLJOUWoQM6h6HdEp8ZUJ4CfUJ7sKziDD1ALDTchM8SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=iSn1WxMoQgu-gNgsOZw9xUprBNBgLKYJScLyhB2_pe3WEwcO35g_MhR9S9t9akO_WRxYu0ojYkdnCKjfWUNctqQBkBGK-ifgrknh99yuzpkBUv8_KYeaNVgLqbfTyW5VEVQ45Vzm3CT00sPm81iONgUTJ0RoF3B_OB9VTSozXI-U3K5i-jWtkaI_N9ciKKrow3wuuUX2mTKuGKw1y0stQUEvTYw0B6mU4w-u-aWMThZtR83_dEQhBFQ1Vk5Jde7i8zLBPVAvMKkJ4FGSFZT1cf-8cruWWZeLfi_1hEmBrRygLJOUWoQM6h6HdEp8ZUJ4CfUJ7sKziDD1ALDTchM8SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام سانتی آئونا فردا باشگاه رئال مادرید انتقال یان دیومانده 19 ساله رو نهایی خواهد کرد و هفته اینده نیز به شکل رسمی از او رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/persiana_Soccer/26497" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26496">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTClkEKCBvQKjWGNIlx88S4weQMe-mTxkZwQlOq9qRRMPF2L47F9hAGpnCZNRVApV7R3_ZJrAXwABk5FyXzOS5uhA0n4bjxsqOObwrBCqaKBvIA4MHRCrt1fMwzoktMILgmD_VXz5xjqwfRF2TIaVa5rQ5y22cUbhXbPJqfsDp1LpL_XdWBKiARH5nf5f-HYhV3iv7_T04DPdrnbrYt-wxmIvSnX1Ht09SCwUuvTntG4j_9d-PBLVUwj7L2aOfNKpa8YC8jv3QnEiEIyJm_BZcaZqn8OxJ8Z0FafzFNuNbzyzp69Js-SwBmqeKC70VvvpiDMuxSd9DFeu_ziCt-gng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛اگر اتفاق عجیب و غریبی رخ ندهد؛ محمد مهدی محبی تاساعات آینده قرارداد سه ساله اش رو با باشگاه پرسپولیس امضا خواهد کرد. لطیفی فر هم صبح رضایت نامه‌اش صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/persiana_Soccer/26496" target="_blank">📅 18:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26495">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d8219701.mp4?token=FUCEHyDy0WPeqp1NcH9-zm4gFgE8ofAL17Gl6rAi4WWszfTQO2aythF9M_hxXrIAlqm-ksf7oWUVJ60AqT7rPuDBXGqO80No3JfDwo7pec4HrYGePw9NdlSQMLJ-8gAmPlvcckTdctBNds0z-SisteWDggf_eCwy-CAil4FxwUSEMR2jJ1_bXt8ZgpwuhXHUORgrc3vaIZj1yfmbzuaSaXS_RmfP7D4HTTgbQgLxJhVMgZcq9PodV4FD517LhOD-r2BBD5hiWhzZ_5gdOupTaVD5qScsYC1E5b0I0KdELjPoVRHUvEzvYPWCK0chn5FEYqHP9pz9_DNdiaywH8dQ1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d8219701.mp4?token=FUCEHyDy0WPeqp1NcH9-zm4gFgE8ofAL17Gl6rAi4WWszfTQO2aythF9M_hxXrIAlqm-ksf7oWUVJ60AqT7rPuDBXGqO80No3JfDwo7pec4HrYGePw9NdlSQMLJ-8gAmPlvcckTdctBNds0z-SisteWDggf_eCwy-CAil4FxwUSEMR2jJ1_bXt8ZgpwuhXHUORgrc3vaIZj1yfmbzuaSaXS_RmfP7D4HTTgbQgLxJhVMgZcq9PodV4FD517LhOD-r2BBD5hiWhzZ_5gdOupTaVD5qScsYC1E5b0I0KdELjPoVRHUvEzvYPWCK0chn5FEYqHP9pz9_DNdiaywH8dQ1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/persiana_Soccer/26495" target="_blank">📅 18:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26493">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Id0S3thhSebgDKJcVt-ALsBWDYHlfKsZrEDo8r_0-jTZEd_KYj_cxBPsgks0I6mEm3S8zQdBX4-9HxQ-bZP1rRqqGutNzCktnG2c4iq7tcLOhbFSGflQiPcOjf6Z9L7ongLwUv6k7a0JunyUKfJuZ5zzJyF0JW_WifuTUekbkLY2cIbAcNaZCeg4Q0-PAvFT_Al_cVLDjoDPWHwszoz9L51t0II3l4egSGIiF3F3h2HnvL5zLc74hXIZphzca3XerFr9BlTvTZWQJd6L0TkXuPMb9f4olkLyJEdAuFeIpvtidUbJ83sGmi0jg89g2Qp1q2E3-7dT5h3VOI6wQXF7sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2x39ISWciiU3nstuzwSRkhzEt0I8MdRX31mzx5E8k78j_y8KgHeT8YuvWMRkJKqaR30fGF2jP0MvoLYwDMpYst0DuTE1qqOs4pIie2Nz2FvR-o4nNAt70-YyhN_2YQ7FpSi_FiaqbEJG3XfR_quSeSP_hyfePEuKuBAILOVgjfd_eiHupEoGZOTxINC4S91HMg2EbK4vKl0evd_OWTAA8gb8tk1n8aQVDk3qFx78bh2sNm1EYkxqeR8oPAsgmpNFkyR0WsvBn0KQ6XgvBQXF881UDNRmdyBx7aVY1qBz5_xpnOTPUZFMFUVS3C6P_vJ6OafzlECPV6PY30pYkVDJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال درسن خیلی کم اولین جام جهانی دوران حرفه‌ای‌اش را تجربه کرده است و اگر همه‌چیز خوب پیش برود، این شانس را دارد که در شش جام جهانی دیگر هم بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26493" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26492">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLUx9cuQFZIICz8U0WtwMOxKiNJjxUqWMDSzBYF7ZjUsF2SdO5uNvJTOmLQEF-F_kFK2xM30WCTWmAa4vq1fgP0_r36KrAOPP2rsRr6xE4O0bC2ptr6b6lS7gpdecihvIHmF2_mCNm2dPVznS0XW8Y-iYRP_OWFFB1VYHJEQeAm40APS5EUqe0Yu9FP1rcpvWJP7lUVsD02Vsei0wkpzO2QXAWUXR-ml61JdQp1bVLM__WqsPRncNmNtGk4POa1Cf4zRb7WMgSbKimGKOLjkS9sUfNAjgd7koD-pA61FNUPpt1C5mWbNJxfaPeDfmTlpqXbalZ16Be0gtdSNwbw9EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ طبق‌شنیده‌های‌رسانه پرشیانا؛ یاسر آسانی شب‌گذشته‌با منیر الحدادی ستاره‌فصل گذشته استقلال ویدیوکال گرفته و ازشرایط آروم ایران برای او توضیح داده. منیر به یاسر آسانی گفته دو پیشنهاد دریافت کرده و اگه با یکی از این دو باشگاه به توافق نهایی نرسه احتمال…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26492" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26491">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1sy_4wGkCBtlbpxIi6knE8bEQHgtytILKwOng6_bSf1pF8VcnKSfGVPVAozky--4QEj_AACaCvgD12ObrR9Tuuqtc5NdcoBLTupXPc6y1h-k2OYuYT_I_5qDs7wOonY2dl4PsgQnYpDKVM1u-zU5GKT_7c68sgCRa1dc7XEs1zjHPNg-IsoKs81BlA33kPTUNMPpWVldlBIV_0tfZrTN9-Yl4w_2m-KKItlypvHpKgXaM7dHCA7LaHBCr_cfKolL8bg2QyAtF6doFEMefyTicDOT7hj9Lk5FyM4A6iv3vkhNCjNKXTfAOyfrdlTp6KpSZmukuaHgpYIlASsQaHaZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26491" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26490">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0V3Rafwi3uFAwJbo2kR9mJ817_qAudo5OkLYCjSO96FwMzz-r3sNbbL6ULNrrMzjjUKg5pkBjert7TSM4HsQDtT8nYjx4ElsLl-9Ut4xi0tLQBYIe84ruG5ZObIk61d6w0Z5GOd4JzBz8UnT0eE6NhL5T7rfOG9h2YvcyOgCte4i-m42e9ZA_jQQ8b8XKTqDaTIVgLXwO84yh2AMt9_Y-9Mneovnn_YMQ7kimeF_m-vBoyv73jATLjZW-IuQgF0lX2m_YIbNR9-rVnDs20nBKgV8L-mHnbl_cxt-aRqqrD3wSiXicYVuJdIDzLBf4nWpOdf4WtVPy0QqpT9trkT3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری: باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26490" target="_blank">📅 17:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26488">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knFP9ixW4JvyHiFvyNvPa8sb-u1f9FY_r2Y-ljFO6Xi8A9g2HF2SjQ8eNh_jURWurKJTaNP2lTMOBxTT-n8PYqtScM9i7AM6SI0AP6mnjfumDp8Di-wafNutJlfGjLPqMFAxFixqm2zAtTTFlRVQDvGz8QN631jGEvtoCs1fyydFhvUT-jZh5d4N0GttdGHLwYlHBz7h-n4zwT6JVpJh87RvAsbG5dzuyyhm8ZjF5TNRSu3yk0YETcWSNob20sU1NrQkd0aZaoDYrfrpB1oSE4xwl8SC8dQC9b2m8K1W5HL-82FTS9O9EvvupRvKFYrg9xtqG66oGTsxEqakWNL7zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پرشیانا به عنوان اولین رسانه؛ یاسرآسانی‌بجای‌سوپرلیگ‌ترکیه به پرمیرلیگ ایران‌برگشت؛ بااعلام‌باشگاه استقلال ستاره آلبانیایی آبی ها دقایقی قبل‌رسما وارد تهران شد و از فردا در تمرینات آبی پوشان پایتخت حاضر خواهد شد.  پ.ن: یه بنده خدایی رفته…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26488" target="_blank">📅 17:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26487">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26487" target="_blank">📅 16:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26486">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSMVCoE6PrXa4Ls9N2wA0cNYc0tMF40J7OhSQkd9D732swVQ6mxTsn2Etvbda-F8PRsb6EOTnTOeofnqjiimXSCt4ttbvPjXDff3VVNBQ588LdquJT22NA9nvOg1bOPejoqj0wL4AdjYHTapqiosWi2zXHtxuVgPSqP39L0d0UamA4obNp9Sshu98m8Ji8RtgjLFMejbzVggcSPhkiKtUphP0WIyFzhf02MfWGmqZkjFEkRGtqI5eU5akV0Jw-OApL1YrNPFPUL9AMT6q7f8RS-SQfrXeD-Zm54QEjNd8RlUuwgjkyzGd3_tcHgLT7jjSEq1WT-d4ko5cev_uQTpQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26486" target="_blank">📅 16:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26485">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrgsSw1uS3s1Q3KjKUXAUcJ0p497VOjhRHO7iiKHCmAotvNjHIMlRAZGSrnf7jcML_g0ahH-jMibkSU2DcEfu4GSvF6gzoQObz_K1yqb-lpbiPBgicx2YdzUucn9sNj_DytFQqBr_YCH-bhNC-YQqFxH_28ghN-nnSRArTQLgvBhQQ6037a4t2GZMsBLGImG7ggOK_AiwCsemKmJA4wEFWDiRfCqRZKBGR-fvkGDtXcjOnDRnV3x717c10BCgjLH02zUJ2OnKtXHaIRhMDlXxQMGDz3bANpoBOwcxBtrKgQeB1zC_eCjgqzHj4qcRaU0G-BLzuMIyE9SYCFUF_e6nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
🇨🇮
بعد از علاقه یان دیومانده به پیوستن به رئال مادرید و مثبت‌پیش‌رفتن مذاکرات بین طرفین؛ باشگاه‌پاریسن‌ژرمن از خرید این فوق ستاره پیشمون شد. بزودی کارهای‌انتقال‌رسمی دیومانده 19 ساله به برنابئو توسط مدیریت رئالی ها انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26485" target="_blank">📅 16:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26484">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=iTYDIqV07z025bkMMfJQnrc7wq5DH6jYfLzx3_q7XFCaPtlbj0pNqAZwghq3_crl6StKXxqas0MTnqq4yRt_lq0TfA_ONLRtz_4uS-0OcRZfbF4R0oC2V_BbXfEe_XOikL1141TkbjNPCE3TitASEO_knvsng5EkVA3LH6sYd9XstAQzvbNZCBNQifg2XYDTI6dEMSPmT3XORp6fKJ64TLcmLYZ9WqUBbHkM98va4e8GJwd2pXDlkVcqdTwjU5bioJPpEUQy84Ftc1NQ4lnmb56Fxoo2f0yWZRq0vHbW78ytOIadyE18TBC0SOb56lUJDP2KxTRqlP-m8CXFBRdXx0FUib6eRF2-tiydK_bzbViZf7vjHGuV6I4oiAjQOKJdHLTK0EEuy4EiBz-gRcistcXF4wkAe5KWt0qvXGGlLTnoHeFmC2At8CSwSMF49x9SKoKPBc_yzOZeW50n9NMLRm-oVZCQgZzSmGr8jfypryWaJ6IZ_Kamr4TWAjtfqkLFqo_ZTMfI8tzCmELUnqms_pvqSnJRQJNlYw2vxVCE5mZJICBFOIQug6RKKyNui6uzlLfr7JJemeLMG-M7UVQUdVdcQ0rRr5KXmBFicvQcvymNb2z6QQyX12yMrEatu-1yGpEjLJ39wbqMhERX4tvriB_SkX1Z7iErTZIdaGVE-Zo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=iTYDIqV07z025bkMMfJQnrc7wq5DH6jYfLzx3_q7XFCaPtlbj0pNqAZwghq3_crl6StKXxqas0MTnqq4yRt_lq0TfA_ONLRtz_4uS-0OcRZfbF4R0oC2V_BbXfEe_XOikL1141TkbjNPCE3TitASEO_knvsng5EkVA3LH6sYd9XstAQzvbNZCBNQifg2XYDTI6dEMSPmT3XORp6fKJ64TLcmLYZ9WqUBbHkM98va4e8GJwd2pXDlkVcqdTwjU5bioJPpEUQy84Ftc1NQ4lnmb56Fxoo2f0yWZRq0vHbW78ytOIadyE18TBC0SOb56lUJDP2KxTRqlP-m8CXFBRdXx0FUib6eRF2-tiydK_bzbViZf7vjHGuV6I4oiAjQOKJdHLTK0EEuy4EiBz-gRcistcXF4wkAe5KWt0qvXGGlLTnoHeFmC2At8CSwSMF49x9SKoKPBc_yzOZeW50n9NMLRm-oVZCQgZzSmGr8jfypryWaJ6IZ_Kamr4TWAjtfqkLFqo_ZTMfI8tzCmELUnqms_pvqSnJRQJNlYw2vxVCE5mZJICBFOIQug6RKKyNui6uzlLfr7JJemeLMG-M7UVQUdVdcQ0rRr5KXmBFicvQcvymNb2z6QQyX12yMrEatu-1yGpEjLJ39wbqMhERX4tvriB_SkX1Z7iErTZIdaGVE-Zo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26484" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26483">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEslSlSUyXl1HZe3byeAbJ6vbj6AZF44u5ANk0YWTCZv0-UzIOdHqAn1lkbOuGPXf_lrc8DFYk6cAaNsGqOh5IGgmPEPuMC8MawbbuMdzpddS5NE_orgn6YfHbjJx67dYzM1Ekrxc8AvOj8Ok9lXQmiG6DGjudj8qImtqzsv-lhRBQIVfI8qGsTGPqifqULnj3F2dhIb9x-5uh8EGxjnvE237Tqklm-TqDQ5_xscOG6So31agj13t06bf-42v58biLhrrWrOyVd3CkkgAj6t62-bWEOPolHud2EOE6f9xG_vqMp5566PHR1fsIFy2x-TnRaaeTxb65xbtyb8OHvVBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد زکی‌پور برای عقد قرارداد دو ساله با تیم تراکتور به توافق نهایی رسیده و بزودی از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26483" target="_blank">📅 15:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26482">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWKz5_BUEhgX1hbGEu7otCV3Ifd2tWzJSe_2wG5xn6c044pxSJ0uG2NN1tvqcGxV54FGgxgxiUQuUeqAoBiVmnfgmkw4YzaGzFmwDbQcJsrV-1MBc3QyNVJuqO6BNRgl3hIUF8SUJhqGs6HgLnJML5yu6HktDKQ_4paqiW4FgucxKMDsXDQROr_LkM92tXkhuN3hQ5MetJqA5dmK55hURbfseUNhHi2U6DJH-AzNHkWwJU-DvCj1q1gzSF7lTxYA7klaBD_2y3RH4KOtYaNQtZHCwhzbZXBhDqNyqrgbF437Z60qt5pfW1lV0BtoxEaejNQYi1dsAknFc-GVVChTMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یعنی نژاد پرست تر از سیاها نداریم. 99 درصد سیاهای پولدار فقط بادختر سفید تو رابطه میرن. اگه نژاد پرست نبودن این آمار باید نزدیک 50 درصد بود. نژادپرستی‌فقط‌واسه‌بقیه بده. واسه خودشون خوبه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26482" target="_blank">📅 15:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26480">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fh856jCNt0w1Qeb3Gq-0VhlnCKve5IwLVMyGt730-cS0uLZEDYv8Hh8aL_4NaazrhqXe-n1CqJnlb8HR45YAO-h-aZbla8o5yCwzoir0CKyvR5Bzr_pyMiw2GYvLk4552I4UK2XN5yqqJ4YvZ74i566Vr3-JWersd8sdOOTwoWMHSNEz5jjCIvIbAcMlw_29TGHf5SElBevPjEDKVQyAKXCxr-v_PPkMwIgdesHGX-I-r2DIGJQqgfKznp4P4gfljwpMNd38EiiZ5fh3RLhMq_pCCmSFsq8DMUGoCfNv-z2xdZwfsMd9VQxuzRD91kR4wI-JvdAHNS9ghc5Zv0xsJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا و پس فردا هوای گرمتر از نرمال میشه و دیگه بعدش برای یه دوره طولانی کاهش محسوس دما و دمای خنک‌تر از نرمال برای اکثر نقاط کشور داریم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26480" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26478">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVLJSslgx2sQjDiFJRGbeOH6u3nY6mZnWMwEuPIvp_3IBbermgdJHwmsVPnfJi8wBj0cRy-Hkpx9mu95eirSgOTrkF9Z0TJI4N8qkkN5t-b7HBqqarirS2UsHYg1vdcRS98vwkTwynIZU21wTOoDuUlcmvYLSV5NSBY7HKRbJIw6wiQrlXcpkKPEpI9pyDb_BVhjB2EXw03nVYUkcKppy3xa5rLPw0rCfF31r-zhX7ljfdAA4iKOo_79j6eiSWKW7Khu2dhM2RYbLH7ye6wODO4tSfRq0Lq7p0ecSeloc95EGMLUuSXJWQQVn_ZKQJAed4Ji_qhTfHaxeOlw2MXIvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇨🇮
#فوری؛ خوزه‌فلیکس دیاز: باشگاه رئال مادرید بزودی باپرداخت115میلیون‌یورو به لایپزیگ یان دیومانده ستاره19ساله این‌تیم رو جذب خواهد کرد. تمام توافقان بین سه طرف انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26478" target="_blank">📅 14:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26477">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lw9w_lKVGmGpHIRM_f9CwmMvyrj3s22Az6nERT_HNBlmltx7h_NUxDmoqAwMQgppYekX87fsdsOFEg9zk4QqSQkX6yFp3HTbHX6NVRuORT79yjaDl-iP2nsiZ_y854YrPuwzLf6pZ3yUgCYnM18pftkU8fG-LumLYGImETslDihxzleUTsyslcWlP89QWedRAKr9tT25rQuNy7dK1joRW862pPCzW6g6wRKffyKPv4kz9jnbjbuEmwgDnZ9Qh07y8MzIk8ELK7hb43S3S1HONeu3L78bMzzKyKZr_hE7OqB_CK3lCqjGIF3gxb-Kwtjbyp_oHWFExVrnPZjOerpnPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26477" target="_blank">📅 14:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26476">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faCqaCWorJVUUMeDJAkcP5AdYaosUVBSvEQykRlBprx9tWWSYmeh3ExdVxxCvQLfwVa8hRUGb-JJIU1zzNVGYDXeIT5ySf__z3pjBvi_d1fL1ROXQ8EiUkZeUQH2fNxvHIQbklJOAEx1iBJO9gFZHwHcohOQkRjsRC9YN6h72ibc4urs7OPjQJmq8kUDRrCONFRRv1O4OWoWYnhF0E8tdiptLlpEMDsvp2woglvjsr-Pqlc6yCURTYwlEFVZIn7j9YP1KPoERuwk7o6IZ6nUGgthJo3fBLYQqceXdO9GVZDe0kjJaVryXBaTLsahYVpUnKUd5e9y_IiQlUpN4CR_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26476" target="_blank">📅 14:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26475">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=C7MlH-F_1Jl4EMSD77vyLwfw2Q2VFprRrjfnXw3wijvTQeZNVozghlsyN2f66DsEibzqr302XRZBtuSZYGgDMTAmoOmVbTYtdIQNz_JFcUqsur9kogqyW8QrqugdOaHt3kjISwogzKk_PP7iGSRbg72SqBhCeaaRYZ0FSfUW7czg7n_H-75KF4WInXa4Tk1X1g22fPghPY35Bd_WNuoMbGF_RhR_6GD8e4FCl5sVt6Ig0cfEslTrDr1Fpfx7-9U1qrSOGkewXxtNJKWaOSI7EbhVoQtgCKMFffMpSsD6LpeH6urJL01E1tIYWbJ8zlkijQm2mgjpDeXiDNNzmPSz7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=C7MlH-F_1Jl4EMSD77vyLwfw2Q2VFprRrjfnXw3wijvTQeZNVozghlsyN2f66DsEibzqr302XRZBtuSZYGgDMTAmoOmVbTYtdIQNz_JFcUqsur9kogqyW8QrqugdOaHt3kjISwogzKk_PP7iGSRbg72SqBhCeaaRYZ0FSfUW7czg7n_H-75KF4WInXa4Tk1X1g22fPghPY35Bd_WNuoMbGF_RhR_6GD8e4FCl5sVt6Ig0cfEslTrDr1Fpfx7-9U1qrSOGkewXxtNJKWaOSI7EbhVoQtgCKMFffMpSsD6LpeH6urJL01E1tIYWbJ8zlkijQm2mgjpDeXiDNNzmPSz7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شکیرا به بچه هایی که توی اجرا جام جهانی‌ اش بودن قول‌داده‌که میبرشون مادرید باهاشون اجرا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26475" target="_blank">📅 14:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26474">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxGrx5yHJozFdKpPf_PtU-xI9I88w8OCIf_zM768sXD5lyQWa2QixGtx70x6WFRGJtXQJY99Ho2K9M30jLFK25LXuez6BA8GMc3G_h0p-uxk96Jz2zQ9s8RzvKOqdoJdeUfIVz_LruEo2zGD0D6LL-NtBksihmMTSI7bSqu1CnVui4S4sySa4rW1fNAkRCCB04eN1xZu6uCKGpos8BcoIQ2nzJxpeQC29zKILFbEUDqP4F8VYgVDEjumb5Xe8g_VZnxCLK68OeyTSm0VQsIGScw4tFk1f6eypWzBdl321ArYB1BMwXBt-CnTvsrDqQnDi63u9Th5PhTlefraqeRSKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد زکی پور و آرش رضاوند هر کدوم به ترتیب 20 و 15 میلیاردتومان‌به‌باشگاه‌سپاهان تخفیف دادند و در جمع طلایی پوشان زاینده رود موندگار شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26474" target="_blank">📅 14:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26473">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfWmfWF6mPiTk4hY3HEFpQXi90N6lc9pO4xcm3mQtETPl0zVm9xkJ1v31kFuvl8aefJ_iy0eIaQ8P6qE3xjMl6YN8iD0NSRnR8RG14Jvn17ZpH3OOcbXO8nmA_ZEjemTLq1dptS5LLZGRX8JHDX7HIQClIWRthzqBc-Z05dnv4nb68EeWYxkXHsicXhcDiEBwhEV2Gf4rBQTpy5ZmCHcBKTzguI8QJLcnazmFhJ5RfON6gcY0cKxBq-5az5iraPyX8s5RSMKRxAKYFGQ50LhSgklvyrhjHRxwMOV9qI4GIC5l1tKgRQNMaxWbWHyXHqvjhbUtHVn3HRlKx3K_3svdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26473" target="_blank">📅 13:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26472">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCASJW_ainmoUYysB8q0Snoki6UUwoEpSYetI8VKHnKg9j6htZqN8gtCSiAYdL1yNDpU5XV3hR9afG30DVXS08usBirPIE9p1L2rxGbZOaQuOoGD3u286Bh_7DGxqBsUgBA9xK7jlWugv574826GZcRsCnkD0fScIMkRMInWfjgc0URayN85ZG6YCi2PdsvK8BK1e8mMitO6UQTfC66uwHvMV3i7lv_5B2D21G_4oDWh_hzX_Er2nal7bmKo0JdRXTeFZ0kCs_MBvdmj4fYowseEJdFRQq4nF4p-njbbfYAakj9sGluwp59sXjDJU4WqF2yljMVl438zhjnv5xfazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26472" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26471">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVuXT8R7CIh9ktgsBH9h6B4afbw3ZNhzsBxRv_uelzOZ48yLWnCAyIMKTkJRxUN7vg_KC6Oe6Aj5dNTw-bgCWeDw75_WaCxPdHSsoiyt7QkVgmBJqNfcveShtKIjX3MJJTRi5I6G2bL90h3J0DI_hR_wIM7jhwzZ6AXhJyMJ49miwayqvHJPXNbOJm35D4IzWoBm-1Tr39kzE7py7y6yWjFNBpMuWrkC57sgWowMpA684npKPtmhbzmMFHjCK1tYtu8oF0O8W9srN0uN2Qo_o6GHsHozFlx6QIrONpFci0_7fn0KQGzz0b7UcLTYjNmUQu5ziBjsqyiuQImJqB2LEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم! آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26471" target="_blank">📅 13:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26470">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ey3mfPJovvb9UEo6KWMpdm4dEYOtnp0v6dF40eGo4oo9N8baAeBbL0ytz5PEh3deIZvBgGS9o4ZqdBFSaTaebF_Qn_zZXf5IMzgK7Zr_D-djQ7kZwIVVC7biY_a6FCz2pbSzlrN5VZixr7dizsfIRiFawhiLIlfRmLhvttymevxt84ozT2PzaMsHed2ziazp9cbblhXQ6NZuO_LJoYR15o-V5T-1HTcoEdHnWfU6-_1BOZ6GFXDcIVsUwXbWUrGQXfpc-HZwLnkbCsNq1GTudi__n4lKhlrBvWvQEqQh61CNQ6BjYL8Mui84lY43kaZarC4FUHvpbb4mb52c00iscw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26470" target="_blank">📅 12:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26469">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOvz-6RRfWa80A5eyH0IcJnpjewLIPmFHEATbYu7dsvycWsg_fJYdW8jl8M1seHcgPKM9sqVW-Q60Yc2SHpePbL9djNwsn-2R_4TEMCFqD-bip_CYU6ic1J6hDpPFgNMCP13rEuHDihvXHqzMG5O_NtFC658ZIdlekOK7FnIDryzPG5LqUAL9aYR0Cy8iHUQX_efjZSTw61kHvuVJExaxSNqKYSwLliatOgB9OpLlqiO5wQfgblswNLintAHOC7ertBPjuTulyAUdz8rwdAfgUTKlON8p2hE7qs1gRNoPyQPFIm2LYUmYMvotM7AY7oWDLmb2LGccxMFEbcSi-fJXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26469" target="_blank">📅 12:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26468">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8915MuapInyc5ZlnhOyuWAcNJGOKJiS9WFugQ85bfDInHGNkCAOO9vHRx0_f3mYareom5cRtyYQZq3oKtxL4JYZHLehYQ0k98lkAq0OcF9QaXKAi7Md9jRfY9xnGsUSV4imIB-kKmr6iimU3KKIl24zvgTQrOXJ4EZ0Rpi2gHnEb94g4AO-xilA5X8pY72Rbj7ODkzEWq2IxpxGG5V5jWXrYoUp2BtM02isTGVpYgCPFWjCzxjFd-HoNz-ZaXngaG0Rpc5uY09YSi7mWdVjoRAj7FByxpbyR5g8KUesbP5aSSoHJxfEhAo-RezvVpfs8QrHPPKSRZCz7X5I-zysHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دلیل اینکه باشگاه تراکتور هنوز از محمد مهدی محبی رونمایی نکرده رضایت نامه 1.2 میلیون‌دلاری‌اوست‌که اتحاد کلبایی‌ها تعیین کرده‌اند. تراکتوری‌هادر حال مذاکره هستن تا رقم رو کم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26468" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26467">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRSXVGRuiGGzoxS8C8g6SqeT8zEsgyYQG024xykHqii4WzUJTGIwHpNRq7t8neSnnQVpx4jpbvcax8vb-exDt2gOgQvd1Om3Hg-B4yNXR8GxCzqXPD3bq7eSW76rUiYPiYw-QvkQAM2SKnn3V2tfq1_yehce6zHc85BTq0Aeff6XnwZugfHvBUDE4pgSOu5lMbzesNbp4e1h1kreZm6zEahccjCGLklIv0VKmtiiTikuIlXvOvJtKLUidN3qgJ453_uCNuAR9ZlWvKyXa-9Pq9pU1Cplsiy5iUeYspcdkFkL4VAE7vE4vTzO6gT6Thm2m8XKCMwz8Fywg4eQFIxDqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26467" target="_blank">📅 12:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26466">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ik6IP9KEFnWVKdOmRkKkyI4HPwYEvvKREcMFE1fT195Oocr9CNh3HMb1c8H_FfdQ8Bw8xJCg9IxQyx2RFU2n7cI2xJ5XLA_0JhaH1QSh56q8_6RFtJJvr0oiGWsv0VAV6wAZvpZc3MjbbELh9g6nsT_fB00MmZqfM04KtHFCLG3R6-31QLvja9xWap4GvneXhRJVkeW1aVMO-aq56pgJnP-5kqXPKfb8ugKFh7jrlU343MqmVcSqd5uT-RPLZdfvUNCNOwUpOXRtGFiWICvrZdDAVDiojlSyN1Ku1eNXLcCeXI811RE1hdZsbJWvpa0Wtzu4Vc8qj2wclmxoM5zpMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26466" target="_blank">📅 12:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26465">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5ofHFwc40EcUl5PWSBq26WxsTFIQFfS0P4UfAFPHjwTehvVZeK5kZ29IvAjymlJZcxIvpsc_VRQkDKwX3IEwo7WK6ckZGRxiSIUMAksA1VYhRpDLyIRImc6vChIoLW7Vy6Sa1URGq4I6uwelXIEgLvY80YZHQ38J73hZvWhhvcXWWxF4fwqaqARxquliQV0aOO_iNUH3HODSVctp7tpXp8tdDaA4tSQA4wkfZRBFg0-FRxQZJ7Ra150niTn7d8qm6bgNYcSVD1d5WpwrQcnlR-9EgU7UDZq4Ie4qKCXOqB92pHhi1rUI-63NHnGya5ETJNqTpjFPzkSnem8RhCjcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو برای چهارمین سال متوالی پردرآمدترین ورزشکار سال 2026 معرفی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26465" target="_blank">📅 12:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26464">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=CLQxcEy1XADi0FrGjoxX_XIBf54m2QzlO_sKp4HLKr8u9cqvPWaVmPg8ttRLPvyTJYY3uW1YDhyBQLjIBzS1nBAI1T5wLYayPzYrzIfNVIS_QH1Yn2_kA6zPnjW4weJD8tgpt87QWrRikqciFLksRWIikxbSggdornCq5Ow0hCiDyvmdt8ZzDg0WPEDCqaPYSWQ25kF6H2uUpPEQvqYi2OOQtEQczOwZg7GVDFB7QtIQfalCpl2dSKFYfvb6saYj1un5HLENW8HecfdcnPrzurZZsOnviyFAFja7s2s1F5-qQfJhlcjDWccja6s42hQZK8L5EbqddEBSYhkwbapPaKxCrL0c_XipHOQ6jHZg59Uy5PTFXifjCtOLrVgeHTClzjCnnkglA7gR31KDcEqvxKZBDABLwVandn-xgBiX1GOlsg6hyA8fVN615Qxey5DUSZc8xjZQRAxNWKTcKKtd2FzPy4y09aoPqSXT2VU_qgSHrfyGidsaVvT2GvdR9bj3dl-bgecm5R-eS21o0Nm_nVIIOXg_BfdRvZL-0waA-MZXT4W3g5atMFGrAG8R34nny-XEUjorlXkh2Ct7N86-dN-Q25oWlinqgeNf7D5WkNsbS5RXSfU6RgbqFifjmKkiJPFX6d1qNirIBAJGovt28Lk9ZLPUXnzcGJXoVzQRYzU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=CLQxcEy1XADi0FrGjoxX_XIBf54m2QzlO_sKp4HLKr8u9cqvPWaVmPg8ttRLPvyTJYY3uW1YDhyBQLjIBzS1nBAI1T5wLYayPzYrzIfNVIS_QH1Yn2_kA6zPnjW4weJD8tgpt87QWrRikqciFLksRWIikxbSggdornCq5Ow0hCiDyvmdt8ZzDg0WPEDCqaPYSWQ25kF6H2uUpPEQvqYi2OOQtEQczOwZg7GVDFB7QtIQfalCpl2dSKFYfvb6saYj1un5HLENW8HecfdcnPrzurZZsOnviyFAFja7s2s1F5-qQfJhlcjDWccja6s42hQZK8L5EbqddEBSYhkwbapPaKxCrL0c_XipHOQ6jHZg59Uy5PTFXifjCtOLrVgeHTClzjCnnkglA7gR31KDcEqvxKZBDABLwVandn-xgBiX1GOlsg6hyA8fVN615Qxey5DUSZc8xjZQRAxNWKTcKKtd2FzPy4y09aoPqSXT2VU_qgSHrfyGidsaVvT2GvdR9bj3dl-bgecm5R-eS21o0Nm_nVIIOXg_BfdRvZL-0waA-MZXT4W3g5atMFGrAG8R34nny-XEUjorlXkh2Ct7N86-dN-Q25oWlinqgeNf7D5WkNsbS5RXSfU6RgbqFifjmKkiJPFX6d1qNirIBAJGovt28Lk9ZLPUXnzcGJXoVzQRYzU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
یورگن کلوپ بایک‌شرط‌هدایت تیم ملی آلمان راپذیرفت؛ احترام به حریم خانواده‌اش. او تأکید کرد اگر این مرز رعایت نشود، بدون درخواست غرامت یا حق فسخ، تیم را ترک خواهد کرد و این مأموریت را آخرین چالش بزرگ دوران مربیگری‌اش می‌داند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26464" target="_blank">📅 11:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26463">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sD4tAQKKqGyvuvl7ofE-Gh_dC_gmBXvkQFui0talEuSX6n1H0zBjAI3-jPXT1Q1mLVaGS_oC0fBDkylClQlzVdX7GpvFv8i_2stuc6hnjgkhmT79tGPDFF_X4ms6auZ55hP5NrXbSuwJ8qjbshVO9yciD1Jw65MH__HweDC6Zd4zI8QRvhc_Y-UEphtRqnwfvrENkcPtzxDw7BPzvsHLCYkvECBDzP_7NaKLBLbJpaD7xUVPZ14txlXGn5ultPufpei11SKGK9b9mMJctOkuMhGrRcsnKC0jwJRsv02-mGP6GqhFEHvtEyNzLFrRsUoB-C5geFPhNOZE09hF-LqG-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26463" target="_blank">📅 11:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26462">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJZkhpPXu5kuyrK_pGaFqPGFdfQAOO2AQX0uGYEan5cwgbTmzlo_lsYOAENegWDIMK3eEqekRMjwUe6iU1Ykak40Nz66UIf0851eF2um6MPfRADP6OtIqaNFsvVaWt3Xkcz4VH5t2o2PYzdhPQ1TBIH3bL7w1uelHEyBx-tODwBKT6yC0WjBAFjOoEy_gNB56ywh5Ox5PCPGVrdlaT84f34nMR5-KM8iO40qY9Tji6paVxik6sUO2YRtCzrEFG8epVB-JAR7rmxN_XdAFyY264s5cp8ue4oKx9XUlK986g_F2QbFZt6RfJ9A0vNgYRX27T9p1-c9VvKdPtSS3rfQiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26462" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26461">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9m1AT3rURFZOHrFdukHw3jbO8u_BrALdSyWEq4SAYcPgc4jJkeN2TFxJ6bAy7KtCcZGnhrYuCrhJ-nLA0DmgE0efCd0kwVIQVJAzJmKD1ADfM9hg23VeMugp_Jw1Bp8OdQM_clBWMbKqTlWwNJFnZUoNxNEWeE6QhOkWvorNfehjypc1cG0aQeLN3eY-N6gKO_bqrHPnuazm9ZSP1coO2lXts6B597b3Qz-o4ioYaOHpFIcmFtUDHs7Q_r_ADUZ7nPQU8HdUxeJKqr8t5OpdEt-E_qGqFFWGqFMiVu021R_GMmPsf-_HximSnl8edPw6ioyzVLwKgirOXRgmHxA5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
گل‌های‌دیدار بامداد امروز اینترمیامی
🆚
شیکاکو فایر؛ تقابل دو ستاره سابق بارسا در یک قاب. سوارز دبل‌کرد، لواندوفسکی هم اولیت بازیشو انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26461" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26460">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOT6uDmBz_VizYP59r_9P632IOu5AJq7uE7D87EQpcklAxbNvqxChMfD3EPzFS5VDmxhGuIqp_PAE8aCPOGIjk7K09zkmtKK_J-JySCzEg3o4QF7GCJ1nxGTjIrFOqHGvnHRtA0v4V8AzJpQ1YejhEO1CUQ_aqw6EJg5LKbUouD92CvfQYrKVBBDi2ZB3HAG-JIH_4yrYIrF-WDRjCqPkR2uxFTTjNmj6ueWqGmoZ0NBeyaE7WQZii4FMd7GoKIwFCTiApcXP3zL_Qz5rYDz12R7sb9-8OkIB_rC_MRhBmw1KWZ_zQrLDFfo2IGaOe1XpNZG62KNIF0itu6an47QFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
5️⃣
میلیون‌ریال‌فری‌بت‌مخصوص بازی سلتیک و میلان
🎁
🎰
با ثبت حداقل 10 میلیون ریال پیش بینی در بازی سلتیک و میلان ، در صورت پیشبینی اشتباه 5,000,000 ریال فری بت هدیه بگیرید .
⚽️
سلتیک
🟢
✖️
🔴
میلان
⏰
فردا ساعت 17:30
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr3
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26460" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26459">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaMrdqyDFNxxyRw8WLvbIE--FEuU2CJbGY1hU2cVIL5bWKsXdrXXbtoHFJC3kbSkfdqq0rs-yaYVjgFJR98yFwppITOLgAqCjLLbbpRQgK1ON_vFSeSxPljcfK_LhxSnFa34Ob5LDBA3M0bsWiOuAWUG0A1CEXXwt7inv9DfiJInr1-obu2MUteujOjFpZiizRADR5HqGMZhH2V_pKRElxiIMvZwfuMlhdB8AW7Q6Jfb-JefVAmmCZq3ntWNFK1JZfIAEPcEHIPaxxUEue1ggilRpbZ7aBSOeG0_DIHauPt5Ml40xLWMY_q9CDScDX3rFMJZrAKqZoSZajhiqQOYoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26459" target="_blank">📅 11:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26458">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MC5ERNaB3RfuHhR03gaOjyGU7vcbQhMHCLSdxhgxCx9BjgnvrgDk3zj42VNPJnTutrRfszEAGQOx22zFb1Ny1UIGe-AqdWCZo8mFC65-gBdYC1g4c0yEXFTUxrCU2SAPKCNTg85QsXiuJrdyD8vb0-dQBNG9u-jg8bPV9WUTa1U6Km53ObXBs4gbaPy0vGyfvu-AUPdJI4hu7WiohZj2zsP17uJ6qJrr-uRoD1jIBcImTY5f0MXG69eMvCZCfDufHuwc9bU2RVk1jBWnyUt_CjVDypgX-uLOZb3MC5Z-sESoLN0T-N1ImST0zUHZnG-kD-a_CkOCTWHdQ7J-acaWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26458" target="_blank">📅 10:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26457">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OltHJ15lPFlZhieAoi-2PkES7wynEsekWPBW6R6T1fju1hLyF0RJGHhnUNynQn_Cqub_Mes8RYv0bbpfgVppsShKvCflkIwzWHHSqXVxY0a2wUVeMTvORkjeZRvwS14bYfK-akZwoJ8Wmkr_StFZU6NwbfU0WSQP2qEpwkaOJfFFlWwwdBNw9MGQUAyfWxR6qESOzIG9evcxGsK7RbJJ4iODjoEz7jGtj1WaqhUmC6eVlOjYFJPvKBveCj3McOvQAnpW_aY24XDvk2dJpgkP1UOtVZ1vHmmAEan2MIZ5OkhNQt9Nby8TGx2dNks-0wZNfDEHI1jybTpFRnbwtNvLnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
هایلایتی‌ازعملکرد خیره کننده یان دیومانده ستاره ساحل عاجی لایپزیگ در فصل گذشته رقابت ها که در آستانه پیوستن به رئال مادرید قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26457" target="_blank">📅 09:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26456">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=ImDno2RdNet72-LKnq8tuyfOwR0pwWMh0zAv8dgudBU_eBoeW6k4IDmb5FQ3rZx_pNAuaquAzPWd_tw0aUziqnWcX823k2d4fEs5CM7QCAiQaRjBtUaJcclkvuu5HI2cAR89g54xKF-B6_sykJRObo2X76K_linA4rZ2wCyzEb0WEYTDx2Jcno51LUTiV5FJZGCO0K7m2IIisB77ne2Edwz5YlOvh-9-ByTO0RrZduRykK-izHgU2BHJ24tmDy-WjuXFN6nzr5F0eBnPgiAIlbx7nB0eU8BnDDAc8rknR1ufY6JFkHQnlkb-yrcN0rDIMqh8HMnNVk3yKgVwMRB7aS3OB4u3aUs2MFTgwV8nNkU2ureL4mEL10_4XgWg__5FF4QHfweHFcyqr6mAk_7fq4FuhsrrKhOHljyRJZAv1Y5_4SR4oDpka906nZwpp9WGfquXudbj6sUWJp8Tw2JOaAGaQB6vs_K9VfA3VXa-zaQQ0YRQlieWlxW1jN2-cIFoTbLgtagguE4aGFxPa2OQ-I6ufp4g5LbGn-Gnjn8jj0tCpUcxJdAIlWtL5c8QOWs4761NxeSLwtQiShi7UfErEnLmhaOMnleR4pxV1QtEMJrdLhFkV9zuXGQSiVzKNzrpbr-0ueV0MXaGLrKacvngOG-59NYLcatt8TIiISFu00Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=ImDno2RdNet72-LKnq8tuyfOwR0pwWMh0zAv8dgudBU_eBoeW6k4IDmb5FQ3rZx_pNAuaquAzPWd_tw0aUziqnWcX823k2d4fEs5CM7QCAiQaRjBtUaJcclkvuu5HI2cAR89g54xKF-B6_sykJRObo2X76K_linA4rZ2wCyzEb0WEYTDx2Jcno51LUTiV5FJZGCO0K7m2IIisB77ne2Edwz5YlOvh-9-ByTO0RrZduRykK-izHgU2BHJ24tmDy-WjuXFN6nzr5F0eBnPgiAIlbx7nB0eU8BnDDAc8rknR1ufY6JFkHQnlkb-yrcN0rDIMqh8HMnNVk3yKgVwMRB7aS3OB4u3aUs2MFTgwV8nNkU2ureL4mEL10_4XgWg__5FF4QHfweHFcyqr6mAk_7fq4FuhsrrKhOHljyRJZAv1Y5_4SR4oDpka906nZwpp9WGfquXudbj6sUWJp8Tw2JOaAGaQB6vs_K9VfA3VXa-zaQQ0YRQlieWlxW1jN2-cIFoTbLgtagguE4aGFxPa2OQ-I6ufp4g5LbGn-Gnjn8jj0tCpUcxJdAIlWtL5c8QOWs4761NxeSLwtQiShi7UfErEnLmhaOMnleR4pxV1QtEMJrdLhFkV9zuXGQSiVzKNzrpbr-0ueV0MXaGLrKacvngOG-59NYLcatt8TIiISFu00Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛باشگاه‌لایپزیگ رسما اعلام کرده که برای‌ فروش یان دیومانده 130 میلیون یورو میخواد. خبرنگاران نزدیک به او نیز میگن یک بازیکن بزرگ از رئال جدا میشه تا شرایط جذب دیومانده فراهم شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26456" target="_blank">📅 08:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26455">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇦🇷
با‌اعلام‌رسانه‌های آرژانتینی؛ لئو مسی اسطوره آرژانتین و کاپیتان اینترمیامی در روزهای اخیر پای چپ‌‌خودش‌‌رو به‌مبلغ 880 میلیون دلار بیمه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26455" target="_blank">📅 08:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26454">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rt0bBnOOoZ8VbIMVT8jP2bEl-Op6iR-HXR6oJDMzO7Rs8XLp24B6AQvZgD6G4XoWaceCvolZ4WifWToJ9p1ZgJ7-I4x1rbJZiYXRTz9WEqUfW4T67yCD0dcHYBcmow74t2qNZPkAtw9eVQCVWc1nZxcq5WP-NksC8nUlfSE-09dYEvBifmnazLaYv1soH9TvNOtjHAV79t_MTpHDSjzNY928lo9bD68l2XXDi8frmommjEimicf9SoAiRV8QRAX81NtKOTXzVpaJoC8ORVq5EiKjd4n2xN0NjKcGALTL3uL1msVNP-FC7TdgXEuNg_1UzLJpu_66IcLrOG3CP2H_hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
مسابقات دوستانه باشگاهی و آغاز فصل جدید برای محمدجواد حسین‌نژاد و اللهیار صیادمنش در روسیه و لهستان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26454" target="_blank">📅 08:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26453">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3AYZnpcIOaVFCrbzZtbp5L-8V_mIzImh7QcsZ1Ui-YAHfdBs1MbrA5gSvW8aBPmEMMKK6fMa7NgMxwX-E6bwgb2OLh-0dq3hI_JuEDiMqukHaTwWlajypK-XHJz_TN_2Ux6iLLcfpUDNlGtZDMMyc8BHwmQ70OGDaOLnx_cWJc1cC8MdXPaoFgnyOWU4m5ONmydmxc-9mTQbGJ8Xa5D-Lvf5bscmsO319glELwmazeAoDt7Eqezmc246u-hNVTqTNBDSkL5fqhCAZ7wJVBOb_Z_ilWI_XZzUE4dKosV5HCefTMcPdBQbY2BR_sJYhXnnBvDDjdltpxIDQY7CgcBtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو: باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26453" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26452">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DckQQRBmZtdPJ1nWWObGL39D3DAuS9TJOZOXLMzyB8E77lr0U8g-QpwGYOZ64P0vMptWwSt4qxOrSaTjOAR0w8NsdlOdJH3gUncuDYOdrjHn0cm0Gko3KlNilL7WFXLiTYe6Ithc3IlAv_-1C1GsDfZDloQBGecUbV7Qk2-nIhWGR25LqSNk5Rvm6z842jkcQSGeg1ltPGXpQLLgQmXb029LcYzroiXgaoiFj6FYvErbGa8d-uH47kFnXxORCtOZr5tl2KuOKVmfzAwY3yMUPCagM8pGtBdeouQ2JHcPxAHt3InSjMHCnr4Jizwjv3fHy1rnJew7JwCny-7BF00NDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو:
باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون یورو میخواهیم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26452" target="_blank">📅 00:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26451">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7Vth1jqle-iUveYNqhI4r9aOWhkLxA1uN26a1YamTDkz_4pa-0oLCcpJ9xzJv5SvwKi6MFFVQY8HV16iKcME6OqkObARXsqHRwPptYN_itC_5V9uyxw65BWZj7X6iDvuNnd5PVXJZKcLz6JP0iHQcRaxw-jI2buvyWwewWhkD1ce1sFps7hir1qUoGvIpdaO-ux1In6Ssw-wtyIRiE6Cp2QXwZ92IDjApccMEtfrjUUZzW2RzXjflw5PVqb-o_yDIAxRIjdiEBO6GtFZuJ16Cq2PebNs3t7aRJslAAH3HlEkb-BqSEJrGQ-AR6zc2ze_C8Yf8OMrW5d4pCgRU51Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26451" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26450">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8Y_DJrNOGGeoq4Q2m_zAuF1QlSBJ_Tk0Zku4TpO0-NOP1t-ZU960R9FKhC9JQCL6BqE-ZPAReMVjwDv88IdIjxpkzDiTuC2UqYKHCgz6T7FG278Da1JoCZAQpg-2TUQ37vvFoO0Cme8h-Pf1sR2XS3N_GcYynGmqow0Y_cmPtAhjmKKc45RdD1rOtfqGvqFb5hmEaBWt2ZS7i1V3qJiRvpOcp3jpLwiNOE5qaxW2pYmeTduWQ1g2SFLOH4gMGL4kxaUBDvbMV8t1yp3-tbpGGylB7JIAqIDx9c1lEa0Ro9c8JPMvI1qnqyy5dfDcggTWi_Uv9EFva7u1R3XJFPhug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26450" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26448">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVyS8z6F-fRvH3hJCNYIdmWqY_kPXYNsim7QgPRiNNQGxFNJ-bS3ECG54LBeMW00iH6dcgKvcGny4BLtEF9o8YkzE60t9A7UXCTPJIoTO_IyUM4uhquVl-UT0B6AGVS97ao7pdA-y3gv8GrYzFAAVPlslk5deECeL8m9765IoFa1CenxDCyLWtC1i4KHs52YqIL8m3lqM_tiVCO9HFpeM3mUldwn-EefsskdxNkzg5-lWfLvrl3HvekMCE8ytWEJcdu770G_w_Yc-aUTAMMWyOT_ZUKldOhj0OXlKfQ0Fp-a7mnbXC89EZ38oljaWWesIi9iheJfeKm1F51AEJ8bBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26448" target="_blank">📅 00:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26447">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sppU2PGm94XunUz2BoNLGbxL6dIJlUndknPbHu7N4OnKoqzkpsdyTXnjCn1f9zOHft1O-VJ3IuLwdR2Ld8MBgLNVN77veN91WBJXIbAJS2qxQNy_cfxcQ98QQjU1Lfl5rTlglpHaYanAZHkMvRgRwNv9kUz41gGlCXtX4yppJB_tYOEYDKM6klaq1y5Msg4uUdt6H8D3RK-8nTCGK_suU6SAj21OWv1nxxB0tZwWNTRvTLmE7UNZa3-f4pWwWU___-BSYSPXii5DHqrhfPNmdNt9cnTabDLVdC0xCw80SFOiksfnM5lY4EYNhmqyoTZ8BwvCYZFTaAUPRLCnkQENmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26447" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26446">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkKnKf3oxzaJIQfwyicwfSSFASTT-ztGcAFWNHunVm7sjTvZrgVepX1NVzOvhQyPo-XPqSLw-GnGBnt7omDJt3zfPaK34ZZKPKIV2xegpOcA41pcZsTRWEnmryFimG2UjkPtE96iBa5PxYvIhVIiDj-tLFdc4bdRguBYTae-BM1TkNj68REnSnHc_uDWk_aSzkHUsKkfSi7t8hrKDTufn_cJnoP38WaKnBm1UBQvt7_eiKJgUV3xHwFHuiyVOJ2lVYU59HbrQAtgdoLwRjx9skkYfB8AQPuXpSx2kes2_-A9towfXG7HD_Wm2ed7d6Ry99JvWvWF7J9F6v-cBywTAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26446" target="_blank">📅 00:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26445">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyoKJoUbopC5IYuOESuUAJ3wivkIBIGB-Epkqdc3TEm5-cSfOYhwURbmuKi-p3TkCyGLTwO7wT3kSb519l3RZB3Qn8pi4xYSCyeMV36y0wxoC6IydFuptEtFv-OgffEwT-3EBRDTvEEcqk0WuC4LIqj1MXkYEtjv3ReuDAj5Ip98MOhOCHUJ9JYEKanGU2RCof80r36S7PAF2mMMwUp91Ye1ANtHX_9EGm0iuTkIQWFXBNTL-YqriN05nvvHwFIIJy1z9MzF9l95X9y8g0_LifuAvlIWo8fguGj9G4InTkBK1X8blbiciszOHpuw2r7Jv_QtUCf4vW8MZFJVL824xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26445" target="_blank">📅 23:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26444">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCplWESrzSVzdtWzyVjtTqy6jtnqzyAOemuFcuGLnq25ijzmafRiJNhqyffjbhGsdNPgxTH4Mt0NcYdR8ti76fm4pkffZ9W_MSfqeUvLqIhzAdOds7VplxazpCM1ucmJTL-kph617KwVI0zBkYMXEQ5AjvY6ZP0Oz859FpOfppaVX6YjBJ3JPlsWAHHOeBNbBFywJ5NSRAAiuelzEgXTOulpbqsmWq0y0h-jgfDC44JLMMoDgAdV4UaF7GW5y5rR0ansHyIOgsZpLs9M6nb5R7J5Ttp85PN_gUW9RUz04rHJBosgc16dA_1ikX_ON2AT5PQ64sZmfESND9u9hKRy4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🇮🇷
بااعلام ایجنت درترانسفرمارکت؛ رامین رضاییان ستاره 36 ساله‌استقلال رسما ازجمع آبی‌ها جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26444" target="_blank">📅 23:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26443">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnHUM5khkb0ZE1dKiTuXloH1XoWmzpmr8oMXnbZ-RJD_l5lBYAyPoHy5liRJovix57TA9Pi-31EE5lMB_J84-tEr6xJX1bqDbL-vf-UphpF_bxZYTqO1zKI6fD98B3qbHZCFjrARYg7tsQQ1wSSi3tDqpCIvGJTvQWaIg2TeAWnZhf-MIdKcj_7AV778LPUMQAOdxUG6j5s0UszBYd0ZYgXHT6N5ON3o6lwzyzlXmie79gDc1hQWggHFJV8Es5HHEhDGOww21Bx4wI5TFB05L8vg2Bd8n1ueyuSqsYWV3LzClgtF92_GnupBrV8MKLVsXhXx8kv7I5nQ08goN8e3lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26443" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26442">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGQCiQSrhtoZM40L9W2pylAPWh3DxG46Ua_tV9CQTJrGAMz7BxeFIBbbX__3lYwOS96SJrVzGP5ctHzNzjpr8jN49HdImm218zU8Q-5dbfTQauqEy86mFaX3qSm_FY1BR6HAilmJzoetlzQA2ABPspPW6-ZmFNGHJ-FmYZAhpjyuzXzdbjOIgiB8h3dfz8PSZoL52lXoDeqy20RWXaOetKFXQlxPOd7SNk1hZdkyLdx0FIDDUjNUzBGk0saTQ_-5WRKQs29Hz5sjmAGPncGtpgTuopsSd3Y4MbYbIaQ1Fu8lBVlTceX_IoVNGR-E0Nrp9NpEE7Ilu-F7tWQ1l0edHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق اخبار دریافتی پرشیانا از مدیریت‌باشگاه‌پرسپولیس؛ فردا رضایت‌نامه دانیال ایری و کسری‌طاهری‌توسط‌‌نساجی برای سرخپوشان پایتخت صادرخواهدکرد. محمدرضا اخباری و پوریا لطیفی فر نیز دراین‌هفته رونمایی میشوند. اما برای پست دفاع چپ‌هنوزتوافق‌نهایی حاصل…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26442" target="_blank">📅 23:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26441">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eq_Ys5NLGQfz8V1P3bhNiEBGUSQwZ-YQ1eQuULEW_IlypXdnJu6enMUg4c9rJJuqgvjXkDcquY2qUXFEX4YFSeks7-IoeTWFTMdkgTNs7W3zZkXpc_CXeDTNIgBDEFEIfL8L61pTrh6uFMIayNReVM7wGsDtETlxE3V7J_XBpJloTPoLlPVnACkMvV9bi2-jOjtWVbNOEbLCzo2ndA4nWglOE8mFv5vZ8Ks7SsF-HlCHFFYTbC1FmhROx0vJwvqy8qUaBF54kZTse25tcbGMcXU0eJAdzwhNywgP2SAb0MNrlqJ1it1Zaxnkw99MHEXqRLlNoPdCVYv5JgrLMRE8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
افشاگری جالب زلاتان ابراهیموویچ:
وقتی میخواستیم‌بریم‌استادیوم برای‌دیدن بازی فینال سوار هلیکوپتر شدیم و باید اعتراف کنم که از ترس خودم روخراب‌کرده‌بودم که یهو یادم اومد اگه سقوط کنیم هانری هم میمیره و این از استرسم کم کرد. با خودم میگفتم زلاتا‌ن نگران نباش تو بمیری‌ هانریم میمره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26441" target="_blank">📅 22:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26440">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=ZY3004BLDJQ3BziP2qR2-lrKVgzH-me1Nq_iNXzV_2OUQaEjp3lvLVKmmqHedZzZrs29YSrEliCnn_1OoK7VYRzI9pRdc8NjoO4WRYJG25Cjg2a0z5OYIab0QEwzzs48z5WRlQwd1D3dmDsDn86lZlrlinLoF2BYhSYOcNaXTsE7Y-127ewdh8mtEPAFTok5wfM8FNBt4Fi1ibl0I0EyB3LAPzpSbb8iSKlKSkX_1pnavx1NLTufKicUZkgA1_7rQ8Cg7avmcJgm44H5S1CaJmnbAyHUbMAqIoJFJEGlHZ5SSjMnKboH8I_yUX35muipcT5Q7kPYbXMzVLhD8tU4Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=ZY3004BLDJQ3BziP2qR2-lrKVgzH-me1Nq_iNXzV_2OUQaEjp3lvLVKmmqHedZzZrs29YSrEliCnn_1OoK7VYRzI9pRdc8NjoO4WRYJG25Cjg2a0z5OYIab0QEwzzs48z5WRlQwd1D3dmDsDn86lZlrlinLoF2BYhSYOcNaXTsE7Y-127ewdh8mtEPAFTok5wfM8FNBt4Fi1ibl0I0EyB3LAPzpSbb8iSKlKSkX_1pnavx1NLTufKicUZkgA1_7rQ8Cg7avmcJgm44H5S1CaJmnbAyHUbMAqIoJFJEGlHZ5SSjMnKboH8I_yUX35muipcT5Q7kPYbXMzVLhD8tU4Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26440" target="_blank">📅 22:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26439">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9MzgqGeny8HaDBChClJFxAYsYf2ywAJgI5_ma4Ac0X_qtIPcLnagv5Z0eTMjfspDLDhyvQwBeXG25dE9cMWlmekLsqbMqS_lamurXfcotnVyAphDe4sueXHWg67XV98fA3gPihDrUQ16HiJ3XWfYPIvqpi8eEdCbDiC8Glu0mJ7hGEzMeqND4tepexNPwKDdqa72Jab1VhIhm5E-ipE7rSW7a_0bdDqVoiGJMSgF1KkCpat_mUKv15y8QfQzEb1PKjpVTepj9uYGrUDVc-H8OdqUwOZt2uWc0Yd3dC4-WSLiRwm7q5yPegfzt4A7BPuCnI_5EOW6a9pET4eF2Olug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
دیوید اورنشتاین: رئال مذاکرات‌رسمی خود را برای جذب رودری ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی آغاز کرده‌است. سران باشگاه رئال مادرید از جذب رودی اطمینان کامل دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26439" target="_blank">📅 22:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26438">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nl9pDkifAjzD1PvaEAM5qLR4QM59-3tG_c7cQsSFaNZT5Qo_c0m6mU2T3TmSsvn61nZzE5f1PBVNT2o-SMEg6tLUE4yr2mZW9MMsZo9iGr204Pj25gsA8E4OambrRrMAETGOVQ722Ch2NmDOLauqk1mr4Oh_lpkEyiGVJyDpYMCiyIZiZOGjzdincZXzaPUHndPfmj1Q5GmH9OAvYEKrKlUmubFS_JG9I91lXryv_K74GbE0sLF1do88RVWwksTm1uKH5GoVIywqnRl-Gmi2B7loaKW0PYgc5Sf5-3wtya3fdfgjLRCVvC6AB_kCZ-r35QnRSo0DtRu5Sl1CnV2j9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باشگاه رئال مادرید با رودری ستاره تیم ملی اسپانیا به توافق کامل رسیده است و حالا فقط توافق به منچسترسیتی برای‌این انتقال باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26438" target="_blank">📅 21:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26437">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWM2Q33zY0ZgkNWR2x14ZqSxa9T7hSFzJ-4ZyUvBKZK7myyRP4fpaPVzD2AvSQaG8W2I5F3iIrMgKDFNcXFLBmW6qswXDXOZHLuy30FUdJVVp1bgUwTSvTTUPiW-A4rBjphjCjZzOzDSgf2lQqVeGUxQ6i6lJgf2agfH5btFIJBA6p6yjIvNqyDwGE0N2S0bxgz5Nz4h930ryO9yfG6omOBTBGxBuwoC9qsGWogqP0BVrl6kmprwj77_otq9wYgMwVOTcUZAOkwrIFfClCgRS-DlCrVpFlPJTOZv44UKhipg1XNQ70YELTuZ2-wLhawpiIW1gegyjmthknsY6BiA4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26437" target="_blank">📅 21:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26436">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJF7UILhRTEEPyhV5dWOPSWF_y0k6dJr1n7EPicfcPr9SN8imCfJMLsl_lg99R0b2gl4IfFftZ9-uedAvdS-C8nNpNhZwMKhKL2LbP3Z21sUjiYJbVdglZNCJp1p4yIA1yMLkGWzc1LQ9Wl2pjj_nmKEGheuSp9436dp-yskRIeHXgZAMqm4dbHeJ84tFJWaiOHfmUwaZx2M_POh0BqHOuYCrbNcSXgIzgnLlLwOeeltYeUW_eE5KkkF3qS_dG6WcsFcm3aaAPO7bB2BctgbCTgA8fUPSD0uQC0eJDeyhfj3LwmOaj35Z7TjcBDEu42HNfU3lbLzTLnzrvzaaSiKog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26436" target="_blank">📅 21:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26435">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=vFCybF9bEWfog-JS_jttT3cDtMd8EWTIoiVnmdD-TSAFl7d3RR6gIBqbSx0LELOStD17afiJFwAt953uSaYKPvOoZrLYEvKTHFpIX3Irq1eg8q5VClvUpfMCxo1dK7ZNc_vmVOzoh5Ncjm5NHtQ2sFECPbjlg2b9f1kvGOYDN-uY9qrzsSUVupp-YvU2gXUgqClNJlFKSEnrqRzhYLEAqt5ePjYYfHE32_2zK9g4fN7vi8oj9ElJKYXBQo2eb_g2pbTyOrYhkHlFExFSGB5UJpSw1OIOC1AcmnCUQPQRRTzBHfNEypUSZdfRVj5TVlYpflsYQioSC95uvd4LJWcF7zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=vFCybF9bEWfog-JS_jttT3cDtMd8EWTIoiVnmdD-TSAFl7d3RR6gIBqbSx0LELOStD17afiJFwAt953uSaYKPvOoZrLYEvKTHFpIX3Irq1eg8q5VClvUpfMCxo1dK7ZNc_vmVOzoh5Ncjm5NHtQ2sFECPbjlg2b9f1kvGOYDN-uY9qrzsSUVupp-YvU2gXUgqClNJlFKSEnrqRzhYLEAqt5ePjYYfHE32_2zK9g4fN7vi8oj9ElJKYXBQo2eb_g2pbTyOrYhkHlFExFSGB5UJpSw1OIOC1AcmnCUQPQRRTzBHfNEypUSZdfRVj5TVlYpflsYQioSC95uvd4LJWcF7zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/26435" target="_blank">📅 21:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26434">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3g_jaH0X1oJLtezib7gMm0AdLSrRHrnaI_EZEqbFvanvNLY6spRdvRdHCJw9Jelc5BsdRsdnh0ZXoBKC5Y5AvuwpSFd9bQrIFJcg04lLwfAswpbjAkpzVjN_y4tN7bp3oU_bSvY_-280tZkeFv7WvTwbXE5HvCoypGH2gVVuL2CWcVfK43yy39rbjBwXCvhfk81_X1eA-dmHqCI3egy5n63Jj2HsNAwDapbV8HM1TyRt44rwEXTsnNyMdZxaLZ6qi1nqTypOuZbYaq_Av57SRJrWxelnzUUmYPSCpT9o7xqQZphr9zuKqTm854Gn7DBqGUPSe_pRDRMZa_6enaJOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
#فوری
؛متاسفانه‌خبررسید اکبرعبدی بازیگر سینما و تلویزیون دقایقی قبل در سن 66 سالگی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26434" target="_blank">📅 21:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26433">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvTFD-I9GAY84L-B07qnsXuN-12YMdwQrqkNOYHlfDpQeMs8DcYncVCao5Ap8FbJJnURRgiQEvcyvDNPxPqVZmsxt2Hzjtp-aupfC9L0odnWEppl_Hy5FJ-BfdIxP8xhSwb0ZTAluEXDbgnMsOvzvKr6aPtldm8B5_ktD0-xtO1jE8p_Qx6ZHLzedbBRXsYR-3WJYcoCa2dcD0Mmm0DWEyS1Z6-iMrGo2aebn6o6fIrJM4g6phkQHpcDQoScVPoMfPlH4IIfLW4Xq7mE2je-xUT1lqT1MTfCwuMV6qc3mHkBICfl6vOx35PNHrPbR9YWFD-GxuBcUVmYkEQiYxLMKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه سپاهان با احسان محروقی مهاجم 27 ساله و گلزن تیم فولاد خوزستان واردمذاکره‌شده تادرصورت توافق نهایی با این‌بازیکن‌قرارداد امضا کند. محروقی پیش تر مدنظر تارتار نیز بود که با موندن سرگیف در پرسپولیس قید جذب ستاره فولادی هارو زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26433" target="_blank">📅 21:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26432">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsArYh4Q7nEMbsSSzgHmebzODqFWaaObeFGQhIJpxmVvksolWZbClKiMMkXeEgzwX3CtdXAxsjijnxMM0P1v2vuiDZLo5JTBUEHMhYahIjA1USIzIQlFszR65s2wQuSk3XmyQBlWjajVgSKuHcd_NEAeIHHU8EJz7fMotBWf0G6EyTzMwjfYQT_5fUL1nIYooinFTexHScNmo-ROuGcpPE2YkMPzCDlKtKhTP2T-KCx18HdvJVMEQkBHb0HwDTTIcj0qw2OstKiK2hyl_DsJVvrIhaTa88azncNxzflSNkofisUn5zO7BoCMHIlV1iVIJkLOEQYnl78CqPNVyXPoOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چلسی‌ که۳۸بازیکن‌تواسکواد خودش داره "بزرگ ترین اسکواد لیگ‌جزیره" و فقط میتونه ۲۵ بازیکنش روتو لیگ‌برتر ثبت کنه مکسنس لاکروا رو هم خرید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26432" target="_blank">📅 20:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26431">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWTGSWRurDL_MlUJ3NgjGJB0WgShYBz3UY5-BlBfik3bjAW9xHEXMLZdcxkx7FqZhdw5zV-AJqOns4Gyh_aZubbii9kG5zumjb3XwAvDD5W9GGOcNzqvoz1PhSN1IgtV5OcTDa_ibzJ_sc0QzJ9e7sBtHcdsot1rVWAy9xABXj4ojhLwUbGiuhgWlG3JETE7yjIfh6DBHq28wVPoglxalK_RKIzjdEIahmglli5YcSbJDlGW18sl-yeoGST3sBWI5HqQ8xK5bCXtYJSKPNVklKF2fIZQBmtqjuI-6h2l1vn26o3srnYQUd_L2Oq7txDFqr-d7-rJqdWOleAmT9EqKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهایی‌که از نگاه رسانه پرشیانا باشگاه پرسپولیس به زودی آن‌هارو رسمی و نهایی خواهد کرد: محمدرضااخباری، دانیال ایری، پوریا لطیفی فر، امیر جعفری، کسری طاهری، آلن هلیلوویچ کروات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26431" target="_blank">📅 19:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26430">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJcxnxIWuhLB6ugXAUUVuSHHNrZYTz5oP2y2gGlpEZeIjy5HloVErH_w_YW7_5SaIez8E5_KyWdp69N3VmnZO73Q5Y1zt3GF0rMHqW7IZGcAULUvT0reRQ0ApkU7mnu1WTcR_T31v6T3gkO46aChZ039SBmZkSk8qK14Apd_cCU1Pf7DIdmYzDB3Fj1L6rAVo0fMO_OqDsOSlPNbJY0WrmTFemlNC2zpg4AbEhMn8f9P-tE_UONlF3aips3TrqZKbGOm5hY4PWvtcmwD78UsdqI6A6E5im7O0f3trZ8g5LHI8JRLb-DHllooqmsW50aChL2tSp24QmSByy188XXNxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26430" target="_blank">📅 19:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26429">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXojG7UzBXnIyVjEDlwMH77fjbk_Zr_t0_41ziNJl4O66Rj5aD8WZyYLW8xMVgrl-lWz558UjVSQ7yRY5OkxT5m40pizb0KnOOXPs81YqKv0Q6_tKcIb4faDDtS6xJamIyB_3UOjwy_0qNIpPsIVHpE862ggSZlIDMaHHYYwBQUwUFQjZFCqVLZlMP5AEwORc8zGXdaFZBVJFVz5ntwr0soLy6-mtNOIbj_v3MTsP2M-6F1spo_G8FFkXQ3mKOy5eRt-u77deJAy72Bfw-n2oQ9pdmzGj5WgjzaE7Ws_p66EbNYHXLN3TIOJb9unY8TDGvH5paVxEZrWeGGIRfSr7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ادعای‌رسانه‌های‌ایتالیایی؛ آندره‌آ پیرلو اسطوره باشگاه آث میلان بزودی با عقد قراردادی تا پایان جام جهانی 2030 سکان هدایت‌تیم‌ملی‌ایتالیا رو بر عهده خواهد گرفت. استراماچونی هم دستیارش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26429" target="_blank">📅 19:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26428">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKL1MoyBDRnAPd0ABll8GNAISN2y7yIzS6Tv3rgulTVBj8RqChBK4qj0qVub2f1Ms1OWPj5NsXyKUPn0L8U8SP7Ee39JDWTChIMmCrFCDHn7Mv9TsE8UjBE6QHIPjIJYKRGOJA0TaA_Tn2pJ_wrhpgHnn2CwimTS8-RqnpgCx3S2JL6KY4opUFv-Pz5ggzfgoYVievCY5GxGJltptJSAuiIQyy39MWaXyUI_P4EipZe2jrdtNLrGOprrvJBs-dJdZh2Lmnb9oyTSObfvGaZeaY-jt2ITtnMzOJJFvD6Oz_9gMrXpICKch38SJmedDoK2-6dbrrMGt9g1bzNIGDaEXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
#تکمیلی؛ بااعلام‌ایجنت محمد محبی در ترانسفر مارکت؛ ستاره تیم‌ملی با اتمام قراردادش با روستوف روسیه رسمابازیکن‌آزاد شد. محمد محبی پیش‌از جام جهانی به باشگاه استقلال قول داده بود درصورتی که آفر اروپایی دریافت‌نکنه به استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26428" target="_blank">📅 19:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26427">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHbvcTBg_WZ8Db7VGxCoTGYBGgBSflYAbsjpnXi_d6ToOQ5xmWsqxYxOcaRPoZPfki4s3tyJ_wCEIozSyCD_Ujt7aMukDb1RKCkkjDLn5G5rILUptHXZXqUgFsxwarnVVe_W7Ljm8tfU5eYKN7DSv2f7HGxRhnso_CRBmCNJwYVEXlD3iq26dK7miVYzkKmsaX2MKrBP3pUa9kfBFHKuah98kxeyMb1JIe_bi0n7erQeQZPC97Pd9j45dTrORTTmxqeFE-E1VyQQxsfreNEFQkmymGVvW9s_NaeOvhqIkHS2KvzTx47cpjq0jM_7kJ3V2jhHyk626FyHQbY5aHUGJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رونمایی از کیت دوم تیم بارسلونا برای فصل جدید رقابت‌ ها؛ بارسایی‌ ها دوست داشتید؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26427" target="_blank">📅 19:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26426">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8uATSjHFSxOwXkCsiNdqkagpJO73VekV6IrwVy133s7tH4Li6kk3a977FfD35T7SQnGGQHZPN5mBjdoKQ3LRMpKDAcUWOV2DTl_BQ2S1sI4CJnqCBhunyY0GVjJwIEFY6ylOBZwsK4yWcRkbJ9aIqp4pW4g16o70Ho7af8NKUhaLOd5pb7-0GsQGzE5subZhe44mH2yOfSqia2LAvO04Yj_lKoW7d8RaVqfzHWQu2-GxI5TmyadkFGrlKjsSKIG7zvLsgZPUgSrfcMYvhs1ux34aQzxI66SjE79Ts6FgvC8_7V4FMQdjjLQ31G-RAMbyV-4BXy1tvX61ix6dnaDwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خب سهراب یه نفس راحت کشید؛ با اعلام باشگاه منچستر سیتی قرارداد فیل فودن ستاره 26 ساله سیتیزن‌ها تا سال 2030 تمدید شد. الهلال اگه میخوادش باید 75M€ فقط هزینه بند فسخ کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26426" target="_blank">📅 18:45 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
