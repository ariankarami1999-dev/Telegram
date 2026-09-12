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
<img src="https://cdn4.telesco.pe/file/ptBShGFRi0UIXwwbdd_hUY48Ph30WOmpWBSHiu3f4jxbcQLMH4DlLtYZKbpejm1Sk-5I6ZqbtCQ23reWQwAl3NOdR642i3VnDTfYOVryr5PYP1E130DitS6x7PjZMdlou_ySGJ-2QYAa3AKJxy6OmhUvhBsrUzbufTk70umJ9uDf-zIop-HwsvOu6iFMQEFutmWHcHbHEZu5del1bl2DG8qcsWl5dQr0q0r0wgWK_2DEL0kbXPZaFYd0SaBwod5HC0laoOZxhbsVFD9nORZ-Z2xciPFvnZYUgF2uRtttjyk4ibjBhlep4Fc67pQNdVv2aL5jxDrxpgTshHx4aCMGLg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 529K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 14:30:57</div>
<hr>

<div class="tg-post" id="msg-29595">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wslx7AzbYttC3dSRHXvfdcnJ3MEMxHIzgcMdyA0utFHPS_T4EiG6J_jRrFJTFoOANjjVADS_xiTJYq9aq3RLiZnvGK8ko2eygSY1to6foiFE2ziy-c5gMPxJ4GsVjrr_CjIyDO4t3FehOOgcOpVH2f0sT5evy3uTg-wwkaGMYZr_03K4sJIEsG3mMoLLpXfHgxym8GCaQJepO7_MMr87qhiWVi8szMqcM8mmfopJjMZEht7jZgEznPix0VMsm4YqWchCNGEQBxrqFSaZWqZGR_TE0iAkzzza3Zi8CpvmFzTll80Eq8X4GEhtB8nd3N6B0kGP4FdGEFSCCW3F7jsYpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌ویدیواز اول تاآخرش‌سم بود از دست ندید؛  مهدی توتونچی تو برنامه‌شبکه‌ورزش نادر محمدی رو اورده بود رو آنتن زنده بهش میگه شنیدم میکل آرتتا دنبالته که تو روبرای آرسنال بگیره نادر هم کلا ویدیو کال رو قطع میکنه. بعد توتونچی میگه آخیش! پست ریپلای شده رو هم…</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/persiana_Soccer/29595" target="_blank">📅 14:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29594">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozhCqX3sUhxnPBG20FYBiYuZ1ebUdK6nIsSgseC378L3CyEmTkPyIF8I4Qw3LXO7X3Tfzn6jVig5CUL6KopqFx5_-kyE-CSlA0MPGabCYJJUY44xajgpXAJDXTseptzRZb3-eyc7TiSXG5bY1ezI7bG46YuYEr3uNjoaPeSWh0K1efYrne85YmAW21IOUvYizp6TZ-pE575zlE93601jRRyubL0Io5okIZDKPP1ipdqZWj6BuPtSGUPElJ12hfTDyGgC1CLJRNNd2xUuPZB8kQ3WN4KCnHpRWszyzqh6vNmaoRxELxpXOCDMH0tSY-eibsA1vv24sSJKl21huzPanw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🟡
🇧🇷
طبق گفته رسانه‌های معتبر عربستانی؛ ریچارلیسون ستاره 29 ساله تیم ملی برزیل و سابق تاتنهام در دو راهی النصر و الاتحاد قرار گرفته و به احتمال‌زیاد راهی یکی‌از این‌دوتیم آسیایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/29594" target="_blank">📅 13:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29593">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ro9Ddol6i9_wtX_6TXdieVrYSOeb9TtIJzlCtE-IFc5Zcro2N_yvf9GV_0ti-8qCmOK71uApI1DsWaLl6xQZ5AE7u2t7xN1D1tNkLLbtdZYNUyt9yav0zecDe7L-LOa9ZI5-JrRBCmhJ-pDA8TiPDhZ0lCGQquloeNqUUwh8B-dC1IprmiAFreqL5rTwmUwHfgkjCogc3cdTzuitRdpU5dvQQarlvUscjAl2pOcivgx_3rK-cNCHH9lI0YCC88DAdFMvclSktvgVQTn7sGv4XWIZimn6n3jsRyHabI5c817gXBwb1rKXUZBDd7P_8BaLxcW8dVeLRU4auf2j9cLkug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بااعلام‌پزشکان باشگاه تراکتور؛ پارگی رباط صلیبی مهدی ترابی تایید شد و این بازیکن 32 ساله رقابت‌های این فصل لیگ برتر رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/29593" target="_blank">📅 13:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29591">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره جوان اسپانیا و دوست دخترش همراه با کاپ قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/29591" target="_blank">📅 13:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29590">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tp6OZ-673UuICAPbrKiuyvp0hG_bSkjFTjdhMLI31fiSaIo4A0s96EIEssjzu4gurk6tdupFWqmdzl4qP-g7VeXOoqAdAnrLmlTMriG65Y-pP-gioWzqtOCqegBRg1dSidHmL2QSDo1lreuwHcMTJOt3bcMD2nRYfKWIsOr_6L1Y7kPv-9pfLA4MfRv0D-ylDWNmmvRoZZ-mExYASIv1nx9ThFYUJmck5iIknqVEkmToaXe6Og75QbRDkfwmJ03iQk5e_WjeejgpkU8Z0y99InduU1JGn7zUKJNm_dZ3bQNQ_wJLfPerrBpfvlJJUcvyUOhPwHn8XjhTrvd8VNYYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
باشگاه پیکان از باشگاه استقلال به خاطر استفاده کردن از جلال الدین ماشاریپوف در تقابل اخیر دو تیم به کمیته انضباطی فدراسیون فوتبال شکایت کرد.
‼️
باشگاه‌پیکان‌مدعیه‌نام‌ماشاریپوف فصل گذشته از لیست استقلال‌خارج‌شده و با توجه بسته بودن پنجره نقل‌و‌انتقالاتی آبی‌پوشان،…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/29590" target="_blank">📅 13:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29588">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU4LJ3XxWVKRQs4DMGlWNRyQp6kN3BWG_dWNcMb2mps3_1YBP18x7pD373IQvwW6S7F_FpNq2My1XyEkg9wYin3CiXgYSMqeOLadT7St55zT0n8yF1bgeYJL-SGwdttafK4RmX_qa9MRXGmKWYONroum6dGkW5A4kMEU1ocLV3Rf1i_eeZECce0Cq5Opv_2d6mb7i95VqgizRBogoBINMRJ0GvVRlS2VYCYbnpNTzr32wFUA_hH6eK9Wdvyy2dTxAbiedhzE_GW-5kXxSTjK7-rwbqa5nQajOl4iOH39S6nVemJRoO1sjyB3igBOL-YteXm_XAyyeTnB6g6XLMlmgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
معیارهای رای‌دهی به توپ طلا؛ عملکرد فردی؛ نمایش بازیکن در طول فصل و لحظات مهم و تاثیر گذار؛ موفقیت‌های تیمی؛ جام‌هایی که تیم به دست آورده و میزان تاثیرگذاری بازیکن درکسب آنها؛ بازی جوانمردانه؛ رفتار،احترام‌وشخصیت‌بازیکن درزمین‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/29588" target="_blank">📅 12:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29587">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLWaTYQ_temNHsVC0XaxGGsnLgqeRlf9cKkJtLE1mNZXPya7WuRbEcolxtpaHmB_cNH1tUCcao0KYKUFz03xF0rkDHjCn5qaLd7mIRKx4klZCPKmI13aHofTR0a6Y-gUKu6DvYss1Ymg1lu-fV9MdshVirNY_Hfi4_8A510kMX-GpViUrGUZ45xWTcj4dAsv9uVfCCCE2qLnGnwaJ8dSJFILjnr7-dqomYlgh4MznoC7rTXcGgvvCZenUzNLmqUx788HvmouO7e7GdikGqrIjO0u7sQVk7IMTZgNQ-rI9wWSq1WJupAweFxKApjuAAiJZ9Ksl3LoIRiV1rgsZC-loA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
برگاتون بریزه؛ امیر قلعه نویی سرمربی تیم ملی که تاپایان جام‌ملت‌های‌آسیا در تیم ملی موندنی شد درخواست دستمزد ماهیانه 15 میلیارد تومان از فدراسیون‌فوتبال داشته و شرطش برای موندن روی نیمکت تیم ملی در جام ملت‌های آسیا این بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/29587" target="_blank">📅 12:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29586">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3e03b999.mp4?token=CyGcEBUbhZ6VbY7GcAd4TQW8mHQMMcyBtvbccK5fsZFj9KGY3nz-oxEQKm_izEXJ_3xsVRhxDQM8LRQrwbxYPgXoLU_b7DHAZaWVTWQ67BAHlA5jYNoMaohQlZEQJjQfjJ_zvz6cXSAAo9TINBnm6wZcpXB8U3N8AK64LHvCmDMimnIkuXw9ffby7ATE7NI-LRU_zOSsdbc1Xj5ZAwNfHGrttoBpdDdeoh8EqL86TvfoLQs4aYRoFSWlEyzugANhOU6z3DFVJV4jqgsnJ_aYcJN0xZi4FAIQaHv0p1dq3EE0A5dpfBBnj83mfCCkLHnXIcAtYpTE6YzhB1NiyEO6sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3e03b999.mp4?token=CyGcEBUbhZ6VbY7GcAd4TQW8mHQMMcyBtvbccK5fsZFj9KGY3nz-oxEQKm_izEXJ_3xsVRhxDQM8LRQrwbxYPgXoLU_b7DHAZaWVTWQ67BAHlA5jYNoMaohQlZEQJjQfjJ_zvz6cXSAAo9TINBnm6wZcpXB8U3N8AK64LHvCmDMimnIkuXw9ffby7ATE7NI-LRU_zOSsdbc1Xj5ZAwNfHGrttoBpdDdeoh8EqL86TvfoLQs4aYRoFSWlEyzugANhOU6z3DFVJV4jqgsnJ_aYcJN0xZi4FAIQaHv0p1dq3EE0A5dpfBBnj83mfCCkLHnXIcAtYpTE6YzhB1NiyEO6sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تقویم
؛26سال از این‌خوشحالی عجیب و غریب محسن رسولی ستاره 19 ساله سایپا گذشت که با یک حرکتش روی آنتن زنده شبکه سه فوتبالش نابود. بعد چقدر بازیش خوب بود این پسر. یه لحظه نتونست خودش رو کنترل کنه شورت ورزشی رو آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/29586" target="_blank">📅 12:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29585">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrQRO_gazYn-vkH540jSTgT6JiolnGh6d1q5XfJBQ4UuytgjskqsjkQwCOjzEY0KO4WA5zyv6E9Go2JgoO6tcPIeahH9yWyc_Y2xFSdYFjnM17h7TmamkbdYf8ij-VMCZkWK93VXMk_Vz_t6ipWLddw71uw8e4vJUcOaDWiXFYhxpAlMF-QPdUrhJF989DKGR6UZmtnjOkJ4ixZXYOELNX5NEUypOAN6T5x3f9bLjBnZ4kKUL-GcaGDgujMKsaSwZhvHZMqaZHGyq3IH8hOFVflk7Ci57VRAn7Y_YCPuYqiTO1ph-bc7QrhFgkq7ws_flvw7Jm6DNJ8sr0SzGayiiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در نیمه‌نهایی جام ملت‌های والیبال آسیا؛ فردا تیم ایران ساعت 10 صبح به‌مصاف استرالیا میره و ساعت 14 نیز ژاپن به‌مصاف کرهای‌ها خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/29585" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29584">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkgeN6Tt0kVQbDGm2QjSgLP_63RwC7u26ce0yc72PzQwi5WeJwBcPOQQe91pA_tiJoLN94PlULhnUbJ2jh3x_zR_C-1hispNO_g8O2V32Dv7EcHZwHxFlGfrXQQBxivKLky8T9OxsAVNhH_L4JzTbkOi21X3M18sICKzzjxxa708Fi1eKLvd9FvqJtnXxUFTtTYhQa1NGkDk9y0xcNF9nYg1_D1QSid-ArhmLUF1nKGh3zICmrQVlKXFfjv68V-jpmBHfzeQZY0r6kT3yD8sUxNa8P3S9sblOLQaJI7i45tmgvHd7QMU73R9czvM2jdpvy0wy5YR2rZ9AVjQ6sdnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
باشگاه السد قطر حریف‌هفته‌اول استقلال اعلام کرد برای تمرکز رو لیگ ستارگان قطر و لیگ نخبگان آسیا از رقابت‌های جام حذفی قطر انصراف داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/29584" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29583">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsSaVroKEIw1IRiaUpfA_SwEFbYhdygIfoocuT6K37AMa_LdBbJvMxjhDop_utRGvGtA3LBFbwInRzU5xDhc_yAchr_C9ikjDwSVgicYik32hbhTnKVqDka4e7zC9OhwOkCC7jLiFhV8v0KOqooiWoOhWYtpezlkMQdYt2f0sFzHueFJdHJB9WgUK5-PCDEWv2_LJ3lKfIY-pKQ4umZnbpA6CuSihJvc-CBO_NvYF2j6D9G5q2pe5yw8BR7mrhcX_NZ2vHJWVAKJihXgXeV4HKkegsnt_p2xKm8KmJ9EXnQmkabuvkPzxuJsyIgNTHEX8eK26EPjOkbIqA8YJ3g2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
‼️
از تحلیل و آنالیز تا پیشبینی رایگان
از مسابقه و چالش  تا همفکری و گفتگو در مورد رقابت های ورزشی
❤️
🪂
هیجان ولذت پیشبینی در کنار بت بازهای باتجربه و تیم حرفه ای پین بت
❤️
🤝
همین حالا در کانال پین بت عضو شو تا در مسیر موفقیت کنار یک تیم آنالیز حرفه ای به سود و موفقیت برسی
❤️
🤩
آنالیز دقیق رقابت های ورزشی
👟
چالش های نقدی
📝
گروه همفکری
🧤
ارائه فرم های  رایگان روزانه
🔗
https://t.me/+IxmGEx4ep9A0MzQ6
🔗
https://t.me/+IxmGEx4ep9A0MzQ6
🔗
https://t.me/+IxmGEx4ep9A0MzQ6</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/29583" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29582">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‼️
فرانکو ماستانتونو ستاره آرژانتینی رئال مادرید که مورینیو به پرز گفته بود اعتقادی به سبک بازیش نداره و قرضی اون رو به‌فیورنتینا دادند امشب برای تیمش درسری‌آ هتریک کرده و نمره خارق العاده 9.8 از سایت فوتموب دریافت کرده است. ماستانتونو در پایان فصل به جمع کهکشانی‌ها…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/29582" target="_blank">📅 11:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29581">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q61EO23ehm85PDzLctmXoZOtMvJ799ou2nTqW_X-Zb129aGBVm4fI2lCNac_5s8PwAYCK8TnIST5IdJkU15DXNd9XikaGcE_cWx9bU64LBx9Dr_yYCRR4dwcrZ6a51aQhYxEdcoCMbHltATGinP2ytaWF_syAEwJxB7Kv1QLgSnX9nCs6lSRb0CwMABEu7QqhinBRyychMF2cm29ehfcSnZTgT83M3NKOl8kjsHeV4D6O56n37UnyKnSR77JCQwcMOdkFcNetANVJyF4G6Pn4KmtKEL7rnk308UkurNwjAsC0NZk_dH4nJsIQAR44IFQlry6ktZQSeDT56aE-qFhxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
47 سال‌پیش درچنین روزی؛
اریک آبیدال ستاره سابق بارسلونا به دنیااومد و با این تیم به دو قهرمانی ارزشمندچمپیونزلیگ رسید. آبیدال سال 2011 هم به بیماری صعب العلاج خود غلبه کرد و بزرگان بارسا در شب قهرمانی این‌تیم در UCL بازوبند رو به‌بازوی این بازیکن بستن و آبیدال جام قهرمانی رو بالای سر برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/29581" target="_blank">📅 11:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29579">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af01699be1.mp4?token=V6eqGspiwv_9UCzO2dKJEDa0AwBfnrZ_BFjQAFpS0AvhQp3Mu04ce8lRWlnlqrQV7Pb2nCPplp_WnhxoTq1NvETiCL7QdK4BK5I-5kup3ti3hzi7xXbqQJ1_cDJiZTtw7onzdNI5FavcH9b1tZgw81_dZ92Q2eVyAxdB5su2h6ctbxD_mQMOq-IhCOoCthIeksAAUkefrg-bHB3MhfNW3065M1gGLkYaUiVzO9F-BWAVy_dtE26URabaUAQT7Fjkgz45FNCnM-QOxXsjIA6M6J24MpU8ZdSfMLLJPnlAG006XqIDndg9Lb8Lh2DCo3GxV9jy5Y3-JEl7upaLtooQChCblxZmBHW4N9bHONuQ4NZjhJizs0fu3Zu4vv0sS2bwITliJh3iatvsCJVCTdgBUScmVGx_7FAgsTWg83cw5vl3yxddJDwsYtgv-3f7-DwIqy9XwJ29qrl6B8S2uoNW7AeYhFIa70gXpNWvEjnRlzNFN5A28yIqCw8kEPuID4ZB4u0sBCHt0y_nv_o3LNOHboVQlehydzbIaF5SezsGZct-VZV3yvKhV1C0dDGaxLg3KXPR2GfMR_3nAc1f9e_8paEyO7OZPR8yO2NBQwu8TNHYHDDSnicbWPqo6ZRsGXyhZAf7vpDmpj_nMpzOqAFAk4lorGtfwjVEtFQbvP028Cc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af01699be1.mp4?token=V6eqGspiwv_9UCzO2dKJEDa0AwBfnrZ_BFjQAFpS0AvhQp3Mu04ce8lRWlnlqrQV7Pb2nCPplp_WnhxoTq1NvETiCL7QdK4BK5I-5kup3ti3hzi7xXbqQJ1_cDJiZTtw7onzdNI5FavcH9b1tZgw81_dZ92Q2eVyAxdB5su2h6ctbxD_mQMOq-IhCOoCthIeksAAUkefrg-bHB3MhfNW3065M1gGLkYaUiVzO9F-BWAVy_dtE26URabaUAQT7Fjkgz45FNCnM-QOxXsjIA6M6J24MpU8ZdSfMLLJPnlAG006XqIDndg9Lb8Lh2DCo3GxV9jy5Y3-JEl7upaLtooQChCblxZmBHW4N9bHONuQ4NZjhJizs0fu3Zu4vv0sS2bwITliJh3iatvsCJVCTdgBUScmVGx_7FAgsTWg83cw5vl3yxddJDwsYtgv-3f7-DwIqy9XwJ29qrl6B8S2uoNW7AeYhFIa70gXpNWvEjnRlzNFN5A28yIqCw8kEPuID4ZB4u0sBCHt0y_nv_o3LNOHboVQlehydzbIaF5SezsGZct-VZV3yvKhV1C0dDGaxLg3KXPR2GfMR_3nAc1f9e_8paEyO7OZPR8yO2NBQwu8TNHYHDDSnicbWPqo6ZRsGXyhZAf7vpDmpj_nMpzOqAFAk4lorGtfwjVEtFQbvP028Cc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداوسیما روز به روز داره خفن تر میشه! شبکه دو یه کارشناس اورده داره از خاطره قدیم میگه میگه کارتون میذاشتن زیر کونشون فیلم رو میدیدن.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/29579" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29578">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRzSBBelcyInq5OiG7OxLv9nwaA8XNWaIPxjGEpFcCpOVChQcJNjP9vUU9-bfUHS0UhSo7xLr-45jpU0Wsj8GjkiyZ19-qMe25TJCbkxiT_doqpJ7JzkfBruRMljDMwkCDY0YAQhgcD63dpuH1NJYMWYyYAU9n_CYgySN2sPlr8VXeplkuGFicSooKldAM-T7H3xTEi48ZDJEp5KzI721e27VgKiGBPf77xFXfxtCblKGpNCTGNgRJjINjcdKbYx6HuqMEulwCgvIbpK4yBQ_JRWDa0rodRyb4l0NDz6emPT_nsD-MLwToSsxazW_xbQlJKMr78Txf48XdnoUlKcSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌نویی‌قبل‌از دریافت‌پول‌های هنگفت
🆚
قلعه نویی بعد از دریافت پول‌های هنگفت از دولت! شاید شما فراموش‌کرده‌باشین ولی‌تاریخ که الزایمر نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/29578" target="_blank">📅 10:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29577">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJl-Yx-w2lPAd4Qgl05V_2JzeMgwBcQ8TE2rXT2v1-s5lecKuLWWi8G7ROOBNo4VoDqA8vow-1rhX6BMeqUlLuWJY4noqNO-lqJG904u0GEvSoHWL15k2N0o2wCs2KHaNOZB1rdvBTbTCfb3TUoQ6cBhSqaNUKeRJdzJhXgDIK2UtLhq2KfT8ozejbSZqdghUL_nfbrLlBJw7XNUp33Qnx680dGsh9JoCvQhoPVeE9kiI3FPWkqxrx5zmefADrAk6v6nkehw8oHiMgnG_UdKw7JPJHUOrPejNIzRvxhWVgJ5GYgfFA_sBU4nJtjIdm8oBQq6857LK2KoOM7iVUA1AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
باشگاه پیکان از باشگاه استقلال به خاطر استفاده کردن از جلال الدین ماشاریپوف در تقابل اخیر دو تیم به کمیته انضباطی فدراسیون فوتبال شکایت کرد.
‼️
باشگاه‌پیکان‌مدعیه‌نام‌ماشاریپوف فصل گذشته از لیست استقلال‌خارج‌شده و با توجه بسته بودن پنجره نقل‌و‌انتقالاتی آبی‌پوشان، حضور مجدد این بازیکن در لیست بازی با این تیم غیر قانونی بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/29577" target="_blank">📅 10:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29576">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6157fe5afb.mp4?token=TM7oyf3MnSBsQHpr6NyLdlEPC4jdW_W7RtR8EgoICjqwGjqZSqL3JAXFvtRsJgyqyO8keUGQyq7gReGb2EMBlKIIQ3bFt923CdnZt-xMFW73KJCTQUsAD0W6RPOAL8NtBHB-q1KfgLeypC7hfndbpqaxzrOGmAG1CX4k7R1gpzqmlYqxpP8VUvmSB9wtReTFnxlegMse8IA2eLj1b2EGADTTgBznYMb_LqCLIT-8o0g9GrUuq1zYHs-up52mAUiN3NeKh7rbJvgNiznMKm7WDBd1Jyn4vTZNWHvM6Tm9lREDyjfPNwtfAa9dFJZtxNLyioFcBCQnb4xbJNFyiArjgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6157fe5afb.mp4?token=TM7oyf3MnSBsQHpr6NyLdlEPC4jdW_W7RtR8EgoICjqwGjqZSqL3JAXFvtRsJgyqyO8keUGQyq7gReGb2EMBlKIIQ3bFt923CdnZt-xMFW73KJCTQUsAD0W6RPOAL8NtBHB-q1KfgLeypC7hfndbpqaxzrOGmAG1CX4k7R1gpzqmlYqxpP8VUvmSB9wtReTFnxlegMse8IA2eLj1b2EGADTTgBznYMb_LqCLIT-8o0g9GrUuq1zYHs-up52mAUiN3NeKh7rbJvgNiznMKm7WDBd1Jyn4vTZNWHvM6Tm9lREDyjfPNwtfAa9dFJZtxNLyioFcBCQnb4xbJNFyiArjgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
دوس‌دختراسپانیایی کیلیان‌امباپه ستاره رئال مادرید در فیلم جدیدش بنام "Drawn Together"
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/29576" target="_blank">📅 09:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29575">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2108b760c.mp4?token=icymlgxKw765QXKPxZBY24ahcS1lsJ8Zn5hRIxUQlpYKNnZ_P1b5QzulNu7sIdCPbNt31-QQLt6R8RcriKunS8KqJuRjsNs_-aRnBJjqPVqYYZy8pQWfInpwSWF1nk5ukDM5eF1fhNYan87jD28QZvw0AGZTwOoe8CqSRhrcyu8f84tC5WLaojMf0POy3PFGe-5bhufBd4BoPfZIiBMBMOU6jeZDj1XZsrxG6oJ_ZMAWi7ZzEHSsHPxaBLn89FuKaQmH4ijK_SIolVOu9r5yiyLjkOQi6Ia1E9YVlOIXNaoDpUANZ5qLSvUzkGf6boMEdHp81RdFsmkUaHaTgS4qaZ09l1XyW2l0dd7ugAXseWbRdTfblIB3UBafWeXvANSwLyymJQE5TA3-PgoS-hQ1xO645RFF4vHHGu29iQevXpMqa_DqFpGFD5wyesN-ilFsPDZjE_o2V8fE33LpPoQG4yqhcRSVy7Hetr-WT4YMr4pUtPFQAwLjR1t8AKR3xo762HeL_kgsShfZRTqcwTDej4v1tXPfJIKlML__u25UPf2yN96OMbW_G0eZlJhdlCZS6YYca2avmOSRThkZ6hUiPVzRkKIOZH9IH5_81ApHYnew5GxFKuDnQKX7YFL7T5LAvAAqZG0pqHk23Tye9vYePfWGdTfbwO9mgy_QQtW1CCE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2108b760c.mp4?token=icymlgxKw765QXKPxZBY24ahcS1lsJ8Zn5hRIxUQlpYKNnZ_P1b5QzulNu7sIdCPbNt31-QQLt6R8RcriKunS8KqJuRjsNs_-aRnBJjqPVqYYZy8pQWfInpwSWF1nk5ukDM5eF1fhNYan87jD28QZvw0AGZTwOoe8CqSRhrcyu8f84tC5WLaojMf0POy3PFGe-5bhufBd4BoPfZIiBMBMOU6jeZDj1XZsrxG6oJ_ZMAWi7ZzEHSsHPxaBLn89FuKaQmH4ijK_SIolVOu9r5yiyLjkOQi6Ia1E9YVlOIXNaoDpUANZ5qLSvUzkGf6boMEdHp81RdFsmkUaHaTgS4qaZ09l1XyW2l0dd7ugAXseWbRdTfblIB3UBafWeXvANSwLyymJQE5TA3-PgoS-hQ1xO645RFF4vHHGu29iQevXpMqa_DqFpGFD5wyesN-ilFsPDZjE_o2V8fE33LpPoQG4yqhcRSVy7Hetr-WT4YMr4pUtPFQAwLjR1t8AKR3xo762HeL_kgsShfZRTqcwTDej4v1tXPfJIKlML__u25UPf2yN96OMbW_G0eZlJhdlCZS6YYca2avmOSRThkZ6hUiPVzRkKIOZH9IH5_81ApHYnew5GxFKuDnQKX7YFL7T5LAvAAqZG0pqHk23Tye9vYePfWGdTfbwO9mgy_QQtW1CCE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هایلایتی‌خاطره‌انگیز و دیدنی از عملکرد گرت بیل در تقابل با بارسا در فینال کوپا دل‌ری فصل 2014
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/29575" target="_blank">📅 09:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29574">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‼️
گئورگی گولسیانی مدافع میانی سابق پرسپولیس و سپاهان درسن 35 سالگی از دنیای فوتبال خدافظی کرد. او بزودی در لیگ برتر مربیگری میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/29574" target="_blank">📅 01:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29573">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOou2xPAxJAdgwiCditfb4IuTuKyqX7qED4lSZSFvo_b6esmNdiFaRRmMufSd0aF-EOAijjgV74gzT4eEzXyUA6UWnznxfkgyS9Qo4d99q89nF28XuQ01Hh0htEbzXKL_g9BnlWScXY33kn8UqbVjJmqVwyu15K6HyxLLslWNCjjUK1y2z3o1uN6pyaKaUOGeWG41DYymSRUh2YmisYSl0as2kx1_4PYkdToTYgjrix-PHhraJOyXsAQ4cBp6ZafhAl8GAeYEE3sZToNJZUijEmwpii3GI3_QqJCJ_cvFpMq3UD0bSOW7GtgTa0McDGQxFiR5AMslkXYb2nqrYWmZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نادرمحمدی تو روسیه‌تبدیل‌به‌یک‌سوپراستار شده و هرکجا میبیننش دارن باهاس عکس میگیرند. همین روزاس رومانو بزنه: نادر جون به آرسنال هیر وی گو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/29573" target="_blank">📅 01:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29571">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tV-Zf6wghRrYkqEA5oLJIuHPHyc8J-opyhc2Mg6wfHeSe2TCTn2PptPAC-aeKXmi63zU6aHQr3NmDipw114Z8-jCOkgNFmZVULR7d1ImfQUkj1UKOfcwSaVfhN_00VoZldE5JGlcKtJMke48F_B3P4Og1FIIAWFR_L75yVmN0axZkRshulqlvp3sdFE2Yb8c8Hs7IApXYccgefnlXBFIq4PrZN_VbMGoGamZ3StZTo_dzOR0xltXwzxc0ELTUmLAN1lWx5DycJje9ujIE94PcHNsf76OwEvJrRBPmFFuVcuAZcp9oxkzEU6vmGI7hrKaDlyejOxXVppAMlH4P18t3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین گلزنان ایرانی در تمامی مسابقات در سال 2026؛ سعید عزت‌اللهی با دوازده گل زده در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29571" target="_blank">📅 01:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29570">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJlLXXDdgsYXq3WLDOBDqJmmRMjblQjcLF8tgIsm-W3bw7cshcNLI8xHc_aA323VLWN7j1dzAnE49GBmBTV-4cCJk53RxWiiOCXSkclv2TKxaVjp0c1ZijRZ5Xhg1Ks93-bBncRKwZ6v95afAIiwzbQ5dnzdmszGIZqHbwW3h3X7pdyIRAVncFCL0648vBQmgij0PABwyWDV8hZeSCCAMT0YVUqimmJentIUYExu639TPNOXKSoCkupE1sBUB8uIIhkgd3dj1vWn1sEUPrNgvZcOCgVhOTC1JwfLS9R25lgSgAPHW_EPptqGzCPYnk8PifeM1Q088gyIU80kyJDW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری زاده و نکونام سرمربیان استقلال و تراکتور به شدت علاقمند به جذب شهاب زاهدی در نیم فصل هستند و حتی صحبت‌هایی باخودِ این بازیکن داشته اند و به احتمال زیاد زاهدی در نیم فصل به لیگ برتر بازخواهد گشت و راهی یکی از…</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29570" target="_blank">📅 01:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29568">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5UdUGFHq1NlZ5I8iiFZufH3CngdNoy4usS1pRs8Vj9WCb3xOqGUe5h-OgLyM_KAsu9e6Gci9qJMHXXCqyFgei3ygpWk6R8xDkDnmkn1cyvNAJSUaCBOAgC_Y3F7zJbMnaX3rU4FE6CW0-Avdw-EX2Jkp7aiei-0QawfEusGLxsQYJNztyKH0FiWnQqGxWMAL-EmGcj2f0pgfD2izXOhddA35sP28_fEhRgFCKcfm-yMg3hNoL2JYUbRhanAYCt7JFI0HjA53S23J7jYc9bPeByyIx4sh4lN9tK8wr1SGMAyqCSGINuEyxcWbmdFjHCQByAZo3V_pD9QuvS8SRbv6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ فرانکو ماستانتونو وینگر آرژانتینی ۱۸ ساله رئال مادرید، با قراردادی قرضی بدون بند خرید دائمی به تیم فوتبال فیورنتینا ایتالیا پیوست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/persiana_Soccer/29568" target="_blank">📅 00:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29567">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFauMRYdqDDLKZ5ahs6zfxg11sni3OjyNRd5nrGOPHhl9YiVsFOTQXMafANUTLEYf-X2kkYbNDISKskGkXZLixMScsytN3FX6zjPquQfsKvYLND_rs0Ggap0MeNchbqGz_EBynaGrCTjzxmK2qRLMT6kjbSgZPcfgG8cyacNfKP1bSgOBJE7WMqZ3iN_Xm25U1dI8bX60sho1R4AtxGvhwojCbMdF_3qZb3hh6mnTYyTXOgP67-caI2D5ZP2kngmlRb2Ti2PKbyAEPOsw1vqq9k6TBGbEQu559KpJf32ccp-e1yEiiW-8kSR1hAFkw6YtkykL3iYwiJH3W7XtGP4Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اوستون اورونوف در جدید ترین پیغام خود به مدیریت باشگاه‌پرسپولیس گفته اگه کادرفنی به سبک بازی او اعتقاد داشته‌باشد حاضره به‌زودی با حضور درساختمان‌باشگاه قراردادش‌رو تاسال 2030 با سرخ‌ها تمدید کنه اما اگه تارتار علاقه‌ای به ماندن اورونوف نداشته باشند…</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/persiana_Soccer/29567" target="_blank">📅 00:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29566">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a6b08f6a.mp4?token=vIf-4jUKP5L77flBDCN1g-cfDWnbmJQKMvu2JpgDYnX5BCUOHhvA1zHxtgEftbm-_ilSMzyiKGlrguG_U1x6BvdN_H9BDOWaR8gsXZukFw_3p0gjyL40L7jpvB3eJBHgABWrh0cFtJYgycJjsy2T4NjcPq44PciRZN1Oe7CMVJs5sX_3whqzqLpyjo-8aEIuzluPASu7ED86I4L2IZI0kUC6RedNHjs2jWb-93wrTxeuhdRupOVPefB4MZ4T64UmOt-1fpvZh-wB9UcJXkSRCasnwV74pnM1p9-3NOB3zguBAWFC6N48IAfNsflCO_LICU4N4JqcRHJJutXpIetsSoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a6b08f6a.mp4?token=vIf-4jUKP5L77flBDCN1g-cfDWnbmJQKMvu2JpgDYnX5BCUOHhvA1zHxtgEftbm-_ilSMzyiKGlrguG_U1x6BvdN_H9BDOWaR8gsXZukFw_3p0gjyL40L7jpvB3eJBHgABWrh0cFtJYgycJjsy2T4NjcPq44PciRZN1Oe7CMVJs5sX_3whqzqLpyjo-8aEIuzluPASu7ED86I4L2IZI0kUC6RedNHjs2jWb-93wrTxeuhdRupOVPefB4MZ4T64UmOt-1fpvZh-wB9UcJXkSRCasnwV74pnM1p9-3NOB3zguBAWFC6N48IAfNsflCO_LICU4N4JqcRHJJutXpIetsSoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌مهران‌مدیری‌به‌گرفتن وام‌های‌کلان در قسمت دوم جدید سریال جدیدش بنام «مرد سه‌هزارچهره»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/persiana_Soccer/29566" target="_blank">📅 00:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29565">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiNT8Cr1K9GVlWsfOhOLrs2vXSGcgb8FNjYPZEjbQD8AQveFuQiFNMDyxDLNP653p0780iB7hFuxOLAjZtmL1SNdxmppEnX1UhDyW5dWFRDNVpUGmymjfBgezyiN93N8Z7xQsn1e3ozscYMILeNHcCOQdPjJ-XfJ5B8kQ0Obpwzh_dt5sRGsQOizplG7CwpCWWIo4MFvPLMs-3rIKDHsMPeSnigiO7xePFVLnmT2Z4KgCM8qWYSsytdyu--tRvSDJXtNHZ4y1K12VRkXv5mKkABOCYpJDvnBIsI853zCYqupURVbmNmofeWvpEUvdaASmQHeXjjL4ZB9TuKnecU8AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛ از جدال توپچی‌ها با یاران گرانیت‌ژاکا تانبرد رئال‌مادرید با رایو وایکانو در خانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/29565" target="_blank">📅 00:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29564">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2KcstaYvgNQHLDjTuHLjqsBfQTr74tAWNDL6qZwg7Y1tPwFh4HiMuFj7pld3OuoJ9ee3_0mfzZY_tGnSgXWDk4RzwR1quvdsxvJIFQ7hE81KSAWHlpSZblSzjJNteiELY-uu50lXn-7tBveUSGyZ3cyp0Y8kEXrSgDapEbW8PAgxyQVONAbeL1Vds0MxtyyVKeJQyj2bUEgg6BHNaTI9nl8qCOQVRR44VQmxbj4bRoRSsMhVzEUZSLxsZw7QuvRhLRXzL4H0fOlzpHeiuEm3TwP6UjFRwe19Z_Fme7CMUrgX7tgoSvD51cC5EQFPpztMmodcACMCmVB41j9zC_cDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
شکست شاگردان مورایس برابرالوحده‌وبرد اتحادکلبا با پاس‌گل سامان قدوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29564" target="_blank">📅 00:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29563">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_QWutbpepxJyLbnOUchn24IbFeQlAIZlcjOYTS2eXTziS1b0km0CM68xOcr4eBzqPUUP3-Om7od_O07JmkQUQe_QZlEtNtmEZZVgyh1Ocj_vNDe-iVd38zTR8Xu2ZXH-i3VL7TvH0gS_72ZrxAeQDvUqrHjFSYmIJ9SKbCEj1EJ4g7ygFqn5RwIFUtp4EdEFutpJe0XnmMtgQ0nsbWw5ebeZjOrLaM5hixqGmtZmxe330w30DuHAekKrRVJUPFttriD0qqlyCRckbOZdnWidUZ88MB8n_TsrNS7rP01mLoQW8-_q5uI-cMNRJJ82FYZDP3zYE3ABTLqG8NVChIQRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه بیرانوند بالاخره باز شد؛ گل اول استقلال خوزستان به تراکتور توسط رستمی در دقیقه 54
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29563" target="_blank">📅 23:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29562">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRTsBLqgiZXq9H_1BuAHtP0NUGJhlCQMffVjQg5CnffeDZBQvmyoZh29JWeziBjGpQ1aoY5EkT8svbyQtXP8dZaBL2ElyycZ4v_0swvrvSnwXVEPmL_2UvfaLPGnE-PtTD9s8B23BgcWb-K65tLdU5VNKVCuz2d7Xm3oX-5gyHFVYIs7OvxmquW9fQx4ZeiDIvF1Yt60xoA01GMjv39m38XcwnZO3BNN9BQcMDBTPJU-Ts3duK4XWaymcCKTP8H66_C6nGnGSW4LlkHaROQ4_UW4rRM9f2LYFGzyalAxvbT0BkQPJxwb2ZpQhc9cHbNMA9pOfn0glatSDkdy0u2uPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رقم دقیق قراردادی که نظری جویباری و محمود رضا بابایی با فابیو کاریله امضا کردند 1.2 میلیون دلار بود که بعدش یکطرفه فسخ کردند. حالا 40 روز فرصت دارند که با این سرمربی برزیلی برای پرداخت یه مبلغی توافق‌کنند درغیراینصورت کاریله به‌فیفا شکایت میکنه...…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29562" target="_blank">📅 23:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29561">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3j0T1z7SrsER1IuFjOhDaN5_6HKp91CJPW59lAkl7MMlnuIy1O9X-TNRo_ib6lDc50lZ6g7QpQv5pWcJe0KhMztTycZ6N4f3HCBCPMxq1Dp_COBJBhVox0d8FF-ynvalSXcxxzC8uN0ulJpsDsucf08v0kn5B8xhMjfesdt2QqTsfFRDqYPY1XbdI3iZQorD3ntx1608qf7MJimq0uRBmxrZWyFuqwkTVkb_pIVmaqwwdG11KUXoRLuG-wEqXypbdRL-CZA7NfG5RFKxoKWRXy3wIFv9GvO_t8C4Li-BK4aGhOuBRHqXbkknFHFebtcD89Sk1CPgQdbq0eTcRDPIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد فوق ستاره‌ های فوتبال جهان که اصلی ترین نامزدهای‌کسب‌جایزه‌ارزشمند توپ طلا 2026. امشب‌بایرن‌مونیخ بازی داره ببینیم کین چه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29561" target="_blank">📅 23:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29560">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNslKD5psAmSz1BV-5X-zx3x3G8QtIg3wQ1BEZWYL-QguMFAVjLw0j4JTYmG8Mpd_5j4AZym70cbFhucpgFvUuzLYGzDy-dFVBe-0MbKC87LrmYkcy2pybehVXwIjCoPrBZ71_DBu7HBDWODLVhhu06vswJ5XPuwE--NzCLmykU-x5auMT3slqruLOnkiSINW4tnAQDPKgqsZrvCz_F5fMxP7cnYsm1WE1N6GJhdRBCD8I-CFYjGD9FcESrJtTCwflmu0BdHdPxsLkmkVa3GGohm1cNaLVnGm2FGPVjE1GZksYCow6XnJPglgxSN0kZM_oeJN6F4GJ91mAWEWm5oIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29560" target="_blank">📅 22:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29559">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZtLxwkyA8L1Q7eWpzaFRCV1fqsOyakyZZg6F3eqHBgiGFn7P2FRJstjevhuHJ55m8UzjIkJ2SVq_sgWk4yeDbGUou5B0nOqWmlqC_a7DE3E3o698coEz7lS5-iHJMBpXjj92aaj9VhJ_nQTj9o2se5xjQgxUhycS8JW4PUJL9JyTHoVMCtnAT-U7FEFnAB442P0Ila1NO28KnL4AMAWyNejYpNFPZogGNei3LSOh2aqP_Cu7HInhl_jmLkg-n3At3Ac3St1rX0c6RZRrYaEKtZSQ5TJbJInZx_zoYJL3sbKfSQvhIg88lZEoJ4ako3NuW90ruyyR2Ze20J6nGLWrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق‌اخباردریافتی‌رسانه پرشیانا؛ در کنار جذب‌بازیکنان‌جوان‌لیگ‌برتری؛جذب محمدجواد حسین نژاد و مهدی‌قایدی دوهدف اصلی‌هلدینگ خلیج فارس درنقل‌وانتقالات نیم فصل لیگ برتر خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/29559" target="_blank">📅 22:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29558">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6e36c4c43.mp4?token=ZfotQ9svWF425OlK2n4tK2oDO5YTgLHrYeCTjcIhKx1-iKWquN_eGB4qEfaDSSn59R0c0Dv4S4M-0x9kp6sBOGpAXKuoPcQtNrtzv-MWs99yTJDiOXrAAKNTztmnJAHShAt4JIz7fpm5ZeDFCo9COnhPl0e0pJZ4VBu1wKVSGSz0kUX-AyyiWFRMzR9AMnXIA9wlOyVpF61pQDcfQOa2-vM1mbBID-5kTH4Xa26Wum5G0_L6lri99LoqcIqPCfdIIQxpzHvANNhFbAhuYoTNZfdm8gz9HA9VN1-E7_T6S_tLWLksRR9DP3ValxYdqM16LY8q-Fl6BI_4uKG8Ull59A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6e36c4c43.mp4?token=ZfotQ9svWF425OlK2n4tK2oDO5YTgLHrYeCTjcIhKx1-iKWquN_eGB4qEfaDSSn59R0c0Dv4S4M-0x9kp6sBOGpAXKuoPcQtNrtzv-MWs99yTJDiOXrAAKNTztmnJAHShAt4JIz7fpm5ZeDFCo9COnhPl0e0pJZ4VBu1wKVSGSz0kUX-AyyiWFRMzR9AMnXIA9wlOyVpF61pQDcfQOa2-vM1mbBID-5kTH4Xa26Wum5G0_L6lri99LoqcIqPCfdIIQxpzHvANNhFbAhuYoTNZfdm8gz9HA9VN1-E7_T6S_tLWLksRR9DP3ValxYdqM16LY8q-Fl6BI_4uKG8Ull59A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
صحبت‌های‌انگیزشی‌رونالدو دررختکن النصر دربازی این هفته این تیم؛ نمایش یک کاپیتان واقعی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29558" target="_blank">📅 22:29 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29557">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQMBP5IS5B-53duFQFYTCZfVhwvU1l4-nbaQd8VhrkwxxxBCR-zFcgzAnmVTceF-I2iOpv641LCHR17c4OmIT_1ZkVn-xMQtnfbvhm9ydrXtHRoW90JC-AdTrodrMBcCj-Qtxa3fTESnUZa9O7XDx7kWKde-y4qdRmCWi6gWIjquRCOl8oUXjswUfbfoWiQ-B-BLOosw8slwG-Fh2m-du6hsguv-6b2VvNk7BfzPNyLyZdz-g9Ykiepg6WuZQR5A2zUbgCDVdwK79kv6vnWHnDWETIGVmVAydQKq1QYexB2YJcB7_YVQQtf_D7U3po3mQj2uqB5TqfDN3cGyhAaHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هانده ارچل: من از بین تیم های اروپایی طرفدار منچستریونایتد هستم. علاقه من به یونایتد به زمانی برمیگرده که کریس رونالدو در آن حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/29557" target="_blank">📅 22:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29556">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOibS_dwLo0JPUYaNsaJcq8_dBhVsUr8rbE9bTdZ3PlE0kPkrHMSpSa9rM7w9CflBGgjYVfsMDM9W4aXDpu-Kxp6yYgAncBi2cBc62PWA2PdkBjnsbkLfdklCQzxIpkQuWTeBUEEZ8w0NOYM2L9LNdNCVi0AHGMt058DlZss3jUaQ_wbDtnpnsq7B2yjGYT7PhdJ8FsUBaZJSPCPPpfis7jCw9dBOxSHN5zdT_EvE7ZbaUSR-GkbCjoX5Lt8nu8RPRV_y-fF5s1KYNib8oVO_BPMF59IRMp0e-nRZdPp5d2D1IcJn19Bq1wOCGgBQkqzfV5hXhuIPLoZV5anywUErw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/29556" target="_blank">📅 21:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29555">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpW9omjGKI-mFKZZM4EBkf8SbiFIseP6h1Bg5pcpu_CHQ352FaSy4CaxMuE0SYTzkwqo8AkObmteTIUcF5_RfMrl9-Yqe_ss8iNPIEQtU4qokVotLwrYc7iNH7PqkxwPMnU4JyNi7ZgQg0J-McOO-C0AvY1w4mQbus8uc7MikIUxVVa8l-Lc6bpZ_5orGBGnlIJTup1y4_Tsxn04VJZEF7HiEAUmC80u_91zm30XgLb7NZGihFT1jdkeJGrzEQk9Ca391FEtLfBx-weeqnQgzmeIHVJ_C6IVHs-0ua8beLq4VkilyLpfgmD45hwVnSvOLUft4A8vRAI_McrV-D3azw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص آخرین وضعیت اوستون اورونوف در پرسپولیس‌دیروزتوضیحات‌کامل رو دادیم. در این حد بمونید مهدی‌تارتارمیخواد اونقدر نیمکت‌نشینش بکنه که خودِ اوستون اورونوف درخواست جدایی بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/29555" target="_blank">📅 21:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29554">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e054a17dd3.mp4?token=c1Ug8p8h849xvTknusIF2GG8VJKK1_O15BWjQm-UgXhrUqx0DG73xJCZcElnRzEuGu2195T9T-_qXIMH5xsWr8l10UJCndNHjs0rqzv66aUdQGAJ8MvuZH6GDEQ1k6aQXHomJEHVzxfw-QiTwEkakc74kE0ipi0iu5lLetJ0WHcFb-g8Gcp8pbdnorlVztm3Ra_wZlB3LJeqI1rrsowL4NjGr0139Yp6r_qxY1LLjwfU8zxaG1gVLHbOdQWWVgLJFdK8gxTMewaNu4iYdR_41d-ZHJOlEq2CcA_h4ZaDxzNuTTYUAtssnkKdUCD6-SPIz7UJmrBGbFkEoYSq0lVF4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e054a17dd3.mp4?token=c1Ug8p8h849xvTknusIF2GG8VJKK1_O15BWjQm-UgXhrUqx0DG73xJCZcElnRzEuGu2195T9T-_qXIMH5xsWr8l10UJCndNHjs0rqzv66aUdQGAJ8MvuZH6GDEQ1k6aQXHomJEHVzxfw-QiTwEkakc74kE0ipi0iu5lLetJ0WHcFb-g8Gcp8pbdnorlVztm3Ra_wZlB3LJeqI1rrsowL4NjGr0139Yp6r_qxY1LLjwfU8zxaG1gVLHbOdQWWVgLJFdK8gxTMewaNu4iYdR_41d-ZHJOlEq2CcA_h4ZaDxzNuTTYUAtssnkKdUCD6-SPIz7UJmrBGbFkEoYSq0lVF4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمایت‌مجدد مورینیو از وینی با یک ضرب المثل جالب: "تو فقط به درخت‌هایی سنگ پرت می‌کنی که میوه دارن. به درختی که هیچی بهت نمیده که سنگ نمیزنی. به درختی سنگ میزنی که پر از میوه‌ست."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/29554" target="_blank">📅 21:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29553">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac2a8bd0b.mp4?token=nfrkPKhOYs9a0qVfPOA4W1zLfpuwTXPSTB5J5LKpx2wVs4mQU6XVt8k_3S7-k3oz1C9bjy3GdRDEkSRBdRRzg19l5mxtN9UV3hPwqwInfRVubrH-D1Ejt4Dz-dQ7UVCcmGww8bB6Pj8K4XhmvYu28o96pQrGq-4VlUJeYJ_6IKpsJdlcj9oQ1NkEw0YV4o2yAGGrqfYLZwik-LVY1Wge3gFm9MPjWLNq_gYPmVyXPTjYcI8tX5q0wPMFld3B_jQreI8-Ndiplt_6w68HdVV14Q0bowS8wYQmpxfYxtwOFXGkhYWbUqdkZaKNaGwUo2NmI_kYINPdyhAkr98hgyufzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac2a8bd0b.mp4?token=nfrkPKhOYs9a0qVfPOA4W1zLfpuwTXPSTB5J5LKpx2wVs4mQU6XVt8k_3S7-k3oz1C9bjy3GdRDEkSRBdRRzg19l5mxtN9UV3hPwqwInfRVubrH-D1Ejt4Dz-dQ7UVCcmGww8bB6Pj8K4XhmvYu28o96pQrGq-4VlUJeYJ_6IKpsJdlcj9oQ1NkEw0YV4o2yAGGrqfYLZwik-LVY1Wge3gFm9MPjWLNq_gYPmVyXPTjYcI8tX5q0wPMFld3B_jQreI8-Ndiplt_6w68HdVV14Q0bowS8wYQmpxfYxtwOFXGkhYWbUqdkZaKNaGwUo2NmI_kYINPdyhAkr98hgyufzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌زیبا‌وتماشایی‌ازدفاع‌های‌جانانه مدافعان برای گل نخوردن تیم‌هاشون در مستطیل سبز
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29553" target="_blank">📅 21:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29552">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSY4el_nTO_vcoZG3J3_XhULPmg-_EebZfABHt70bHJQRAdbISs6wKmAvt3WLG0GCqdfySu09TqiHu_tz7IxOXYpSlztyqNODDt-_FE_UD4aK-a_ePm6NzxTYK-jXGR_vwAhzduJ_708HwwVDOZRkW9EX3fo2t362Ly3o1y0tEivDgsr1SsG2rs0RKnu65XyYetIOyGqV2pv1ctWJoFV_6kQm02385P_X6L8o0K2krAfliMfCmPKP-b7lKKUiUdJh0dNuCnU6pJgUS-vZMa1b7iXJBIrqTOM1wrTEVP4u_ZtCYv_vEfOUW4v8alWY7ig-jxRF1A88qENiW0COSwREQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته پنجم لالیگا اسپانیا
🇪🇸
سویا
🆚
والنسیا
🇪🇸
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29552" target="_blank">📅 21:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29551">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6TJuf-Cx4kNW-_aVimvbMA9BqRii8a0HfnllPlqzA_achQpDPNTNyanW8Wf13dSKwGzSXUROL7T2uY0-OT8fwOqQvhwkB_Y8_0nZDty5Rmz8iY3FPQxYG6GkXuBXxBvLQ7GsVZYg19xcct1GBQZM7yXm9N78vNr2f0rWAulilDa2lQ-t9XKecE6Vm1YUgDTDD8izaipLJgJxzvDtX2EdzrrvDFH5nk5-gSP-eVaDBeCUWyJMMBqHPNMRd2wGE7oY_wuuEpAOLXpvgjq4Gup-qWVx9ggNDJVU2owibF4oXB6kef3mPJ3BjUTM833B0G4CXen-wWuXaaddg4R8Vu_qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روشنک‌مسئول‌مسابقات‌لیگ‌برتر:
بعد از فیفادی و بازگشت تیم امید به ایران بین هفته هشتم و نهم بازی‌های معوقه هفته هفتم را برگزار خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29551" target="_blank">📅 20:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29550">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‼️
کارشناسی داوری دیدار استقلال و پیکان و دیدار تراکتور و استقلال خوزستان با مارک کلاتنبرگ: بنظرم باید برای پیکان پنالتی اعلام میشد. هر دو گل تراکتور به درستی افساید گرفته شد و گل‌آبی‌ها هم سالم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29550" target="_blank">📅 20:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29549">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4FXCy8Gfmqog2QaW3IKRzHRaGtWpkwMShyxDwLxUH6S1733BSjCSez4dohYW_ftAHPyHnHF-F0XAfq55Ufs94mLb4ZBNFOpCH_HXdy7UDjyuHpMYA8ha_R0L3stO-FOw5DV028_pR4XPpkmwV_ObW96sktefceh9M0dQA6c7GKIyzXzqW5VJpdmQSeedxb4Eo3RyuTCnlnzHiG2cQ6oARLP0Sb_kmjFtrpt5TXa1FdTMTyG4M8ECGngk-awZcLZopzwWLd7lnXv2E-rRIlpPdKWwyGiC9QUGuwRgYu2_a_BnFuTeTF48ZsJWMtoU2516Hg_pjC_sENb46zT-pRalg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
نشریه‌فوربس‌گفته کریس رونالدو هر پستی که تو اینستاگرام میزاره3.3میلیون‌یورو که با پول خودمون میشه حدود  910 میلیارد تومان پول میگیره. در بین تمام کابران و سلبریتی‌ها اون بیشترین درآمد رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29549" target="_blank">📅 20:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29548">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tseDpxZ8VKoYKtg-kPeEzBIagYoXPoyrBQVq4AqL0-vOsxMcl4_LZ_yJYBi93RumLb2BsXI7H0c8mb3Re1hMpD38VwA3xK3Wl0Y-a1P97BaRqVp3GKDYrosb_a4cVP1b8icq1I0r5GvIJruumxpPMM7b4R4Ap480Gn3FXWoJ56bSdtuyROSgGnoFKGwacnQLL0_ScpnaQP_ZjUCGJjyAVxR3QonURwsperGJn4O3xZ7y8pCbptzUlzRwgpyjyBhl4YCFLIUCqUTPz3mI18GF7GiOP8NV774hXOC2teplYYY9NKJ6oCAlG8TTsmWYuGX5hR_FQaQXEo3VtSnyTpXfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
#فوری؛ فابیو کاریله سرمربی برزیلی به فیفا نامه زده و اعلام کرده من پیش نویس قراردادی باشگاه استقلال رو امضا کرده‌ام و درخواست غرامت میلیون دلاری کرده! گویا پرونده استراماچونی دو به وسیله جویباری و محمود بابایی راه افتاده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29548" target="_blank">📅 20:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29547">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vg73U5CGEmk11wwxukTvsqaL0_RQ58tIp9xcH2CbFeWwChHOU8TtZuaYwuS0545pje34XKxkBELUjH7JYLOX0igCQI-K2Af9_Aw-gHzNCUuDMGNiLMQiSho-IJzCpza12OZjLm53VQi_UDALYz2GrLIcmXYTMH2NCq9Y0yUS5Ul4MZ6Sc4bxZb2MboZAnEA6cj9mh_dn1Ng5zIwp1SbdN5ktLMdDkXzEaySNMiddlgH6jYS8_wBknvNOQFx6Y5x0OwvAIt2ivi6711rkRMREhE9Ja3-VbzYOTASPHCPFU2P-j3wGtOt01m5ywOsVhj5wU2fOQ82Yhjw5f1_zfibDmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز فوق‌ستاره 29 ساله بارسلونا با به ثمر رساندن شش گل و یک پاس گل در چهار مسابقه بعنوان بهترین‌ بازیکن‌ماه رقابتای لالیگا اننخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29547" target="_blank">📅 19:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29546">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXW1Tu70QeFR1iSTfAaiACzHJ_g7Zryi36xaM_Xqbc8uD_JlYUA2Cl6n6hkgLT1b15HrtnvhTRKisbY8qkB_2aT1vYhj_LJDG5jUL4xaLgEg0jjlh2I_symNqfARmWF3eQ_aiIEpBW4ASbqDGX3r6b2k-yxp7meCD69lUihYchg707saHTRayWEjzKYCgh1n06QE9XUkQE03WqkHOULF2Qrz0vFvG0rb7eWu9ny-OJtkDzo3CCpk5gWab-E2KIVS9ufaZZudGDxF8X1aJkKgGnirGTBqQ38U0nhGNoIlHfUTvjhPuneufBUUKZR7CIxNBcfmedyuNQZbGNmo8cG3VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
‼️
علی نظری جویباری مدیرعامل باشگاه استقلال: هیچ خطری باشگاه استقلال رو در پرونده کاریله تهدید نمیکنه، قراردادی که برای فابیو کاریله فرستادیم امضا نداشت و فقط سربرگ باشگاه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29546" target="_blank">📅 19:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29545">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgC3n5Zpd5g-4zbhx4KXC3TNOzLAyyjFe6p1Wn4BTStfFkgAGIIH3MIsruoPI6-6lZmgbt3iIk0yWktYWMv8Irmk5n1Iwp_w2WNJ9ebj2Sps9kr8hUU5gAk7ayNdfKSKZXwZTLEVo0hb5m6lTvJV22epEKi5qchQMQToqZWU7OVdOAFYoVMCYS094Vn4k8naugC1EZ_LLfQeNzn9e6w1ObZfD5GWPSjC3kR-jH8wzgzvklTL1dpJSH4OOaGzZx_PiWCmB51lvNSuEv0ZLiJCC8ONkWfw911B5Lj8iK_HOMmrAQ1ufrJ1aKl9rQwJRkfV27NhdtkG8BsmGjWdUN17ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
گئورگی گولسیانی مدافع گرجستانی سپاهان بزودی قرار دادش رو با طلایی‌پوشان فسخ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29545" target="_blank">📅 19:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29544">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzYnJ77m9SwJ-ZJGeOR2Tg2azaoEmCgsRZr1wGH6p2E0p_gHNqpDKj1IEer-NLPAxBU6jxULY12JGirV2_k-3K52mZdGEwmzUG5L3yz4Hqquzi1TJLGo_b-2I1D_JPfHA_2fWWA4dtJI8gqIQB0bQ91GmIE6JC2m0yyWz-obKWBBdZNi0VIdTpF2Hk413rZZ7lmExKEzkBDlj2UftUwAbjymqGHOSW8i7Znix_tL9f9RRN1wCn3yZ_QJnz6wlUWNMc89meHol0P9-VQ2G7CZzSaZoj6iTmLnWAO52TmqtSka5Q34V82Lx95fC04tN2WZ5mFRJoApWzuUdi9iaYrM5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریهESPN:سسک‌فابرگاس و میکل آرتتا دو گزینه‌نهایی‌فلورنتینو پرز برای‌فصل آینده رئال مادرید درصورت عدم قهرمانی در این فصل با مورینیو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29544" target="_blank">📅 19:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29542">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaxcjMdHCybd0JMMB_CocShk0M20zcfGqNdOnvCrAPADNjQxO2aGEUZMtXHmXVP_LwA9Nqhl1b-aGSNXP8EpwjegfGVp5UuiVKbh_lPu7cL31V3BFAdKQxAeFeMBUkET3D4gnrYiCqr5xndiLi-zcsHInN8wEOAKUjoJ7pVEttEKXCkUeDVyqhqJC26CsxNWMZJdL4S31l131ssztlWdSD5q5ByJ_L-CUnRR8bj0_okYFlu4ipSasjd3EaMivuuOJgCIqcIq1BzMZI-bNKEZviOaydesJSvarRSo5PafJoFRsK-sNNAI_k-dY6UnZSQ6ra0rkZMJ-SZvL-3jzy1qkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فکت برگ ریزون؛ تیم فوتبال بایرن مونیخ  12 سال و 9 ماه‌ست که در مرحله گروهی دور رفت لیگ قهرمانان اروپا در خانه شکست نخورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29542" target="_blank">📅 18:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29541">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP2Q4YfIQynAdJB0B-XtJFbHGb5bW-sj3rXAKEG57K-jN0qCjHpS-7qfD8kGoh63W32d2yEv25_zFge6_hAAS2QO-IGsPelpx2lomqrdSndQAqGC9MXOF4JaXdZ1H2ns3xPoXu-aE046CuqpeidqEPf2ZeZ_lO_ip_noio_uUnUyFqy6HDwmjQE1BzwAmvN86moc62O1y08d1SpHJKIecp_VtolZscvglbdgAn5Plh4q5LtwGfP4u-GIOaVyxjorqpEtmNl8q_rRMplrhzHc8cqhzkPxjS8Zye89a8wr8X8JfkJDS2Y2H7c5cc0ytehMuqvh5RXHb3WBgvRX3o7Xpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
#فکت؛ ازشروع‌فصل‌گذشته رقابت های لیگ قهرمانان اروپا تاکنون‌آرسنالِ‌مدل‌میکل آرتتا در وقت معمول "۹۰ دقیقه" متحمل شکست نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29541" target="_blank">📅 18:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29540">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBNKSc6Hd6ZylpIbk4LDvAoiEC7psCAPk5Wl5jGRLDry1yLNcO0ImNTh9iHsQfOBkd1JHHRawC8uGhSgO3MXLaNnTjjzf1LZVbCZy_ZL8MMd5194lq41y7ROOlJ9f9H5xAL2MI9ckHQoFg1zgVbgkG9wlXNsxjizdHzffBVLUFWXcU0w4Xmgcyv596GbDzlqCfSl3vQaRGhLQJBGt4t6QK05Hq4zJrI2jVvYeeNdkpt8KquZxtoujWnSVeii3BLzEuKOjK-I7QArbYHONGK8rxyLFBKNF3gXcQVemLMOwCXizk6Aw2XDF5RSJKO2QkXHaPwopcE7-qHM48dzFY2qZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در نیمه‌نهایی جام ملت‌های والیبال آسیا؛
فردا تیم ایران ساعت 10 صبح به‌مصاف استرالیا میره و ساعت 14 نیز ژاپن به‌مصاف کرهای‌ها خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29540" target="_blank">📅 18:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29539">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57bb43418d.mp4?token=AUFEpWiT1nXasc1gCFEY5O7FM3xli7hoenfEhP5OyCagh9OBd0tW20-ISKtUOmlLDJAtJL1oEupcTgegO4LCJkwuwGHCujbRBMmT5Pga23GdPqzpGPrFGK6oAdsIp9uf7_Ra0vYiVeR4ZFiQk976u3WEv13FTCijFbr-OfwZIPpqH4ddVQLxzeWpgOkaGoEdYT4Vndeu9n10OMXs-1nOq7BxloBML7J07lxI_t5tyyhShxi-X-hytFJ-G1P2icd4Y4FlDK2gb9-45W7gLIclh0vaveb3QVvdE1mSCuzmCe0YUxDHtv84pfcBPbBhnd_GQsrIYmOEgxMxlnM0l-_SNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57bb43418d.mp4?token=AUFEpWiT1nXasc1gCFEY5O7FM3xli7hoenfEhP5OyCagh9OBd0tW20-ISKtUOmlLDJAtJL1oEupcTgegO4LCJkwuwGHCujbRBMmT5Pga23GdPqzpGPrFGK6oAdsIp9uf7_Ra0vYiVeR4ZFiQk976u3WEv13FTCijFbr-OfwZIPpqH4ddVQLxzeWpgOkaGoEdYT4Vndeu9n10OMXs-1nOq7BxloBML7J07lxI_t5tyyhShxi-X-hytFJ-G1P2icd4Y4FlDK2gb9-45W7gLIclh0vaveb3QVvdE1mSCuzmCe0YUxDHtv84pfcBPbBhnd_GQsrIYmOEgxMxlnM0l-_SNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌زیبا‌وتماشایی‌ازدفاع‌های‌جانانه مدافعان برای گل نخوردن تیم‌هاشون در مستطیل سبز
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29539" target="_blank">📅 17:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29538">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwBjM2XuuyqRtympqjaJgR-0NPKJ6XRhN6mkI8OmE72ezKIC2VlEnRekMkqjSv4PYjMDneboyVt1FDJ7I0T4kr6l0may_8vlCOkf7VRpq5let1VkkzKD5odEi-NDwWHegCpuEdRymlcsURkYbG1xFB6aw6Y8KqhvsViFP07cCMZUUJ8B1AMCRxxDWy8lp8y1FDPAADY_b4VSTjaFkLw63QzsA5K0U5nY-BhoiMYeoAFx67ac8FLtTv2m9pxbqIaJxfqhQr4BsIxI-pybXv5_SAep1X3OdpUGuSnMl_3FLM-lZq8QLf37IClF2sUcXvoIKvTo4gZzAnSfvsGSN6EWJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌مهره‌های‌هجومی‌استقلال
🆚
پرسپولیس؛ تیم مهدی تارتار تاپایان هفته‌ششم لیگ‌برتر با دوازده گل هجومی‌ترین تیم لیگ بوده اما استقلال سهراب بختیاری‌ زاده هم عناصر هجومی خوبی دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29538" target="_blank">📅 17:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29537">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8dddf4f36.mp4?token=CdyBquaifLGzmm6XnjVwrddyPqc21Y1vzbE8pHxqSe3yb1iArdDPyScTaGOaZ2LlNfvaJ42sIBVNwETvd4GsU7pRDBFJtXYMfXu3niqSj8Lh1-T2OI0bjuQ8N7X7roN8fA1VQ69a77E8ypvliWvjrFqv9hewshM2PUPwxex9G9MNPTwB9Jm8ZlEQHR8fdtJFzGlMCXGEiLJh6zAaLEqMjXd13Y_B4a-v71i5-A-mkpCGhTos5pQEE7A3m9Tk5Wqice0W1R0z1NvWvIF6751tSsjlKJANG84Z_JWzZW1DrRYgchiCiTa4GxH_WbKWJtcBWeh77I-qeizgxwV26zNF9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8dddf4f36.mp4?token=CdyBquaifLGzmm6XnjVwrddyPqc21Y1vzbE8pHxqSe3yb1iArdDPyScTaGOaZ2LlNfvaJ42sIBVNwETvd4GsU7pRDBFJtXYMfXu3niqSj8Lh1-T2OI0bjuQ8N7X7roN8fA1VQ69a77E8ypvliWvjrFqv9hewshM2PUPwxex9G9MNPTwB9Jm8ZlEQHR8fdtJFzGlMCXGEiLJh6zAaLEqMjXd13Y_B4a-v71i5-A-mkpCGhTos5pQEE7A3m9Tk5Wqice0W1R0z1NvWvIF6751tSsjlKJANG84Z_JWzZW1DrRYgchiCiTa4GxH_WbKWJtcBWeh77I-qeizgxwV26zNF9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گلزنی دوباره شهاب زاهدی در بازی امروز جوهر داراتعظیم دررقابت‌های‌لیگ‌برتر مالزی؛ این نهمین گل زاهدی در تمام مسابقات برای این تیم مالزیایی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29537" target="_blank">📅 17:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29536">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFSS5c09ZBwuO2ve_xawZPmlyCMWHE66DLrCqL0JgAL4rsrbXoiuz5gM7toXWdzkitpt8QEQIHSBuuIvWmY7MrsVhYE0gzNXtSMi33_iHHQ8MmXC_mioYgpQR4ap_w-5fIANmpMKQXxrMPCkSvveyo1h3JRQ4FmCZ73FQTNAbyrtMY-0VdbpCPyjWw3-5f5xacTjJyptJQMt0GHSMAvJWedUVQD5kqfVrkqO7FqZXKu1Zt9dOlr9K9K7HKYWK8hBpVjDq6AG6ZG3Dp7u3HZGuwsavusF0MXpboLC2KlK1UikCO4yeVwGovxOFQPSppNqky4IzWO26XPkax6Q-l1IGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه کامل دیدار‌های امشب هفته نخست لیگ قهرمانان اروپا؛ از آتش‌بازی آبی‌اناری‌ها در نیوکمپ تا پیروزی ارزشمند آرسنال در ایتالیا وبرتری لیورپول و پاری‌سن ژرمن مقابل رقبای خود درگام‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29536" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29535">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFreexE0WqW5djYX7ex-gH6PDilVaHiIdO_EXhLOpzV1foJCFq3SnZtQ_TFdc-76WhIoDye3dFNz1U94w6bg4VwlSgkAuVTrw1OJM1gSVN-xeePF8d6cRHdJhLN2CaaGlw3FgkkTd_ZBqzyCHERxFIbUD1B1386Bao0_KhxY0jxW8yppMFUZrXCAasuhykIkMzhlDB_w0mrPDPfYimvZPqC6yAshdDE60f7TBRgJtKFjxhrKmj9G6q4RmgtfM82m99AiBy1SWyH4e_w2ui4XeoPeIw39_sqcbHVyy_m98Ay5yQSI8V81GK6E6_kcEGg6t4dKzDDLI7jZUpxcRtR24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کار انسان دوستانه یاسر آسانی با خرید یک خونه برای یکی از هواداران استقلال از زبان وریا غفوری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29535" target="_blank">📅 16:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29534">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJTg_4JWhJMutSF9juR6v-Rx5cLiBDQtajl6fzgShEY-VxBE1hG32VPMKd66p_3TGE2Uw5f2rG_uZkoZNtwebfd1iUdpwVFBzIPY9lp4oCaf5T8gM8COxceDj5IB3YPdJVJqGDiiHcSriw3YD2AZnA1tJ0q-25IrYPkjFtYEpyuvdufZS7nK-ujz6CYUzaTCn5Z6s4kSshwJTt4zCY0YLJfBNsjc6Cr4Nu1T4tMASS557iRJ5oScfs4BSYVhuyazv3ppJsletOkmRS6t1nEDpriyns3-I0qoGximX53FmL7xy63_T0hMq73PjsVyQwBl6gjculXUYZyhDXbn0d8lDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به گفته کارشناسان؛ علت اینکه فوتبال محبوب ترین ورزش‌جهانه‌اینه که شبیه‌ترین ورزش به زندگیه و دیشب یکی‌ دیگه از این اتفاقات افتاد. دیکتاتورها وقتی سقوط‌میکنن که خیال میکنن دراوج قدرتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29534" target="_blank">📅 16:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29533">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQEHSIGQh0yonWPhUzrLjLdL8qCbrSSwfKIx_6VHp6l4WdA-VzHad3Wbp6dptdzFiKPHZKtOeqWCZZABIoAHJx7sdNw4X42e7MxtrzihI7YtmfiG-TOjpgWSnmdaZ_XhadxRojcCMXBJLgCB_-0tIJYiTr24tPhglFHF7Vk4nf5GElMK-R-MX1YiRNnnB9ch5KgGDfl6_Q8zOJPukjEO6hgJ3rEufnD9Pew3KV5zOeoGbAVq6gVxByFkG6D2WeH1FLQ7PlGyNFR_ng1jJrBQpj1qB7gzJdNfMX49irbgZYnk6wulH_mxgovptPfFZUbrPrTMyO8Nfk1l_eLrF1Xx_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#تکمیلی؛ سران باشگاه بارسلونا به این نتیجه رسیده‌اند که میکل‌آرتتا سرمربی‌آرسنال مناسبت ترین گزینه جانشینی هانسی فلیک در سال‌های آینده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29533" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29532">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcOnzwTubvczbZKDNId8hvVMbURi74q4ontiv4FzGyQmURXi4PFsR7mhvuPv_lzDR2GLaIZ3bHHGdBbMCJoDBGgef6eV16wWjeU1i4Scv-iHjZzpkmpSU8JXVj7V6K40aqm_Ayw93xmvMm2Equyu7uzdYKV9Pg2sR_4NhuEWrsRekK-gCxAjgXUmJhQcVkcH_OsYKUjeKkQ_Yf3I3OMEa6aAbHxKXLLyy-hdWbCUy6AdkadyXptpc1biVsMWwB4vLo2i-gpSfl28-5Pa_qSURzpiNthP8_b5wzf0raP3CEvm8VpJbWj9z_tMQ4XIO3rjRQHCjWG_v_7hkotwZW9eJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ بارسا در لیگ قهرمانان اروپا؛ رافینیا و فرصت تبدیل شدن به بهترین گلزن تاریخ بارسا در چمپیونزلیگ، بعد از لئو مسی افسانه‌ای.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29532" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29531">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnJw2w4DJtno8WyGWS2NHq2uvpo05Qh6Xic535DCJWWqYXKzm8Drd1jAYm0Y7guJ09Jrmzh178tTukf4OSwviEA0py6_wsPe4ucWmcG-xRM1FGJh4_O1y3chc9Jh0P3XCeCOJoYyA7wbiZGOxwGMkcyviADrBaz2jd8DkLPjvAkFDtJPL1TRGupvCm1pON2Tm9ELC_DOwMkSDPkqEh8JKHgVSjH9QGhTaF1gt2IPUnuUFFcvGjXufTJdKAtXx0QDirLfO96v6Cuh7e_rqt5Z4nzhuUcGJcI_5kMq1L0IdxyfjrFCF-4JFhK0eEmjQR1kBbTkNaiiZ9Isf08DsF3byg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
هفته چهارم سری آ ایتالیا
🇮🇹
ونتزیا
🆚
فیورنتینا
🇮🇹
⏰
ساعت ۲۲:۱۵
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/29531" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29530">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlZ3m7HcstAgGq6u2zIswX5Ocnw4_VaRKoQl0I-Hx5liFrRXGmQT9pROxMVGJ-NcQ6aYCdjQFcR9Ddo9af3ZC1N1QftKhcbu_68YGL5tgNz1WK4uFXHsar9HpH6pnmE0h8riHe4ZEB_l5o9Sz-ouzpNJydSJxsSnJwBsRh5bdCL5Kay5uQTjdHgaAlzNu7pnr8-h8fNV9FLaL_S6i1zaoLy510nTfASg0Nae8w37YS6M0e387qQYNT2RdTUOy0wyVfd202bmruCrDLaEChKwOE8wgwn_nxmL-eFhtUldpMdkKXCCE8y8EO11sYsVmxCSigbNdssxSKYR6qKMNk9Aag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛مهدی‌تارتار سر مربی پرسپولیس به کادر مدیریتی سرخ‌ها اعلام کرده درصورتی‌که محمد عمری تمایل به لژیونر شدن داشته باشه با جذب عباس کهریزی ستاره جوان و 20 ساله آلومینیوم مشکلی با جدایی عمری نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29530" target="_blank">📅 15:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29529">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQ0RoWd-uja-3y3E3UU3aXBOfuBRlqlD5I6dHEYD30MX6ll5bpIkTtZUhx_9KrySE89BxcWMKYP_PTDTc7TFHyoJNvlUbWgiE-jPyC9mo-q5VBTujmWhci2e276rWCTcvLIW9salSUz7HhxVuMU9Ere_c77XcJLVRF4G8SFOM8K321tjkz2-pZy5JF3fKeWx_OZRtSOaJKmabcTb2UhazjXO0LZniN5ib5fKp16IZwNFZak6AMsqeIx1AJd8-sUbNMY8KM1r39I5LG4-FTHurWTgTnlu58cUuCqTHyJPnct42ECKzCWhnt7j2tOJ2tklGf5QtzK9KBPzDI67vARo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیکه‌سانچزفلورس سرمربی کهنه‌کار تیم آلاوز به عنوان برترین سرمربی‌ماه‌لالیگاانتخاب‌شد. سانچز در دو سال گذشته بارهابااستقلال مذاکره کرد اما بر سر مفادقراردادبه‌توافق‌نهایی نرسید حالا با درخشش در آلاوز بالاتر ازفلیک و مورینیوشدبهترین‌سرمربی ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29529" target="_blank">📅 15:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29528">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzboc6U4X11RlH3G5ZhtQjv5EgX1joUiAsrTcFja88QW5-4DD2u1q_xotxVUk4JqR1LfNbQw-cZjf9whNZAQLhit92Iq5bbM1N67h90PLnlQntaqtsL65TdzPjR9d01pezB1H6I1iYIQ8pv_il-dFZtEFztGHmRISFd-ERcycGdz-AqfYMK7uD4BS_STvBp5dODAl1ITmcz0pavHDM1eLGpOEDfP6xxVUlk-Pik_FpUw9Z90GqrmxkpJ4aiGwiUUPjzDkLweIs9ouMkBk1_vaPc0_i8vX-d61vsnDlrJhPXjBdSeOVoPv88ruXaC1FmfmsfHuW_bw43AdT5IUYH2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ صالح حردانی مدافع راست تیم استقلال بعد از دیدار با آلومینیوم به تمرینات آبی‌ها بازخواهدگشت و کنار گذاشتن او برای همیشه توسط کادر فنی آبی پوشان صحت ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29528" target="_blank">📅 15:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29527">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU-16LJajKqUzJ2QQgHb9jVqa33w2Pvcvpxs0HE1DBnyrUTSQrRZE-9r2cWqCps-6wLZRYyf6HoWt49sBudEHl64PPvzvGtG0Q1NEwvdX4HsNd-S1te2BqM6afjLu655lobu-EghEvuoHJ_JFLcmtb__Yo79Bjfga592sm1sU6_WtaDNTwsSbi2z9vZK5Bg61ZqQu-ErUy2d5a4naJ0EJOM5b0yUbf2p587wz9dxdqrl00UnkCEsrgIwRGPrjzewmz9YXOycYTmgP6sSyGdUY49PGzZfexHu4NUbgzEOeZfgnDyNvIgiWNtKFYVBX5SkVBwTNn4SDwMCN_NM6oZHEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛مهدی‌تارتار سر مربی پرسپولیس به کادر مدیریتی سرخ‌ها اعلام کرده درصورتی‌که محمد عمری تمایل به لژیونر شدن داشته باشه با جذب عباس کهریزی ستاره جوان و 20 ساله آلومینیوم مشکلی با جدایی عمری نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29527" target="_blank">📅 15:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29525">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyPy33Fsj0bR8V0MqfsAAMGhhCxkDQIAIKe2Y3KMKBpGRH3SkdVVBbEh6myOxxx65ODO6Mw_eiqbFrGg6ERx6bF1QmkydVa7XOEHV_Ct8tJk-OTG1WV1fxG4ZMHShR8vkNSZc35Ym6c64oAmsEU6ynazlipw2jwRImCwop5QKfeDenlvTN8S2zdfEFhwwCBMDSBpuq4sUSJLj6mJX4ZgodfdEnoWjbrll_lt_yjzo9mrKoZP5vIxcDzFH9-9aoyOSzEQCMi0Q5j2ruxcqguRkbvpChchhcP8636cweFU5RX3ASehYdBy6e__IBLh9PTkGub4n_ZamLxTC0C4KQccVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات؛ یاسر آسانی ستاره آلبانیایی استقلال مشکلی برای دیدار با السد نخواهد داشت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29525" target="_blank">📅 14:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29524">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mANIbmGYlzqhhtt-Eo__bErBTUtF78pJP3oD7O6YneD7vJslWQvRYLRG_YiroDJqLIPkeRt_WOZMkWR4N3MqwpVdWXGM90dZdfFNNU_l85meZCBpnBoUbOb0R39_wzDhu6nTJd5DVu9BEhEyF-fGDJOQgdj_QR_7DUK-Joe5OTNRCZTE409g6Bdbp2EtJ8KOsKJPV_vXlUFJsIhhJORPNXQUI3NUzJDX7o58VvTRWQzRqxgtuGq8FGjCcFnW9O8zG5qVWTx_iPfotAP0SvhuS5w9AehoKjBL-Uij6UXeodnS2yXIpRfiDxaOemXNOn4_rMD1xfb9Qv5OyY-36xN2tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رئیس‌باشگاه‌فنرباغچه:بااستعفای‌اسماعیل کارتال مخالفت‌کردیم و اجازه‌جدایی به او نمیدیم. حین بازی دیشب یکی‌ازهواداران یه‌بطری میزنه توسر کارتال که باعث ناراحتی او میشه و بعدبازی‌میگه استعفا میدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29524" target="_blank">📅 14:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29523">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KO7_OcyjEyuv_WlbJtdpvIV3Rl7mnMxuA__lOHG5D36lL9sdmExsyD0Uo2G_DabJjbiNjV5-uHcPDoSrcjY4rjzxFs63Hlvbam7a_Lbtlriu6CTqH_ngCUNjn4c7GfOfxP7CwPGAsvy_inCRv31KHNQqUEtGKxnMaxRs5P0b8NocBQOG45lSP2QRxEL2YQ7nDosB64KeXNPh67AXzkPKgVTbvuKa0E_sQIRozLhCqE00GcsXVBAZpXBOe6KqQ8RvJpXCNx7rV1_iXP3B1Vk_cvTNCq03ZsPYq0llnfVDGlUhFOlX92ooOM1xBptlv6P6qblPh7nwbyC4YB29HcixzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستر رسمی باشگاه اتلتیکو ناسیونال کلمبیا برای خامس رودریگزخریدجدید این‌باشگاه. قرارداد خامس یکساله و به ارزش 1.4 میلیون دلار امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29523" target="_blank">📅 14:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29522">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpHDeUlAYs6iNMgoEdLKK4lfP70QwSj6qLDar_CmCQVMdmn4jSEoMGtWJ0UfRaRGtxesB5tOlS5P_6l7rHFhPwZvC13-Bq-Csxvic7-cTIa1fGlE6xCZYG_049HpatksiGXN8HWtev_XG_RVSs3tOgNPfueJAXvqLkqcerEVNUIlxiGZTTZIpZrIIavT7jsdxjGq1BjGz9ulJHdqc9_iKcLa9oQTFjg8aXZPD_PG70qwtbkyd8gcLQfMtkUIRy1u1gOVu4BXwjBUQqS6LWJGvb-uAgDgd_xBpdXvmnGSvKZNAXaClajv2KDp044JOF9Fnh8lns6Crj0_XFkq1pNNpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
🇧🇷
#تکمیلی؛ مدیران باشگاه بارسلونا بزودی مذاکرات خود را برای تمدید قرارداد رافینیا دیاز فوق ستاره برزیلی خود تا سال 2030 آغاز خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29522" target="_blank">📅 13:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29520">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LgAVOBXXUMMmd9zGEOP5RanC57-QjIkKIFshTcNrOfEpFBvq4cUdaZi6BdBinkYNgII_LZdewEaNTZMuL-Aw9F72E8jZOzYoJt8VaMLezf52uhNiNpN5cUjW__iN6t4ZLb3GCcMbGrXtWUj30bOGFH_1CqPTxTeCZcZsLbetbdB-vNeHMd89uWi8K_kqXcTdZKbazzUOB0cwLsHIcx_ZkspHqL2nNssJTnzPv196S94x319serHT_BmynIcz157Njw43RYaGSBW-8isJ2FIeaiH6lnJWohZI_zuvWyNvXHR-fC1VKdcgMR_vXBNHnE-Q2wbg1K-9ZcGamK8JJXdOHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LXlqcjOp5qP9DTo7eRUqdEWHa8gNm2y2RESIDLRFQ7ynuCjKzFcpoi5aZIUR0S0i60Rsi_M3G6t4svOwHylLCdnysR98QEcjUJzudZgDn0hvqCB_jgGafgqyKCiXqMlmL6sHS7F4m1tn6NAXlXbZSQ6aRmWVbbk_otGbchwEEtbx4RqTbRsuQylX0Tm3_JvnvIS3RsMvx3o_bVKA175ZEApEJl-WI6K6BPKxRBySNrWmJCZOz0IsUmh4wwr9VTsMeSpa6aPKTIZlDweipSV2nD1ipmjRFWxwMu9I9one8qD76azun6v1qpN0mwI41t_pVQENcQUzCwpDRt7CAQn6jA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇺
دوخبرنگار شبکه TRT SPOR که پیش بینی کرده‌اند امسال بارسا قهرمان UCL میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29520" target="_blank">📅 13:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29519">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWvsgLzT5LUXfzh1s46JpZ7dyLqpAvwHxywCCo7b0do8TW_7kTuBq3J5pk_5F_Csfwl0vpPOB3GYBtw2axirpaZtc6xeVnsj1LEpNtSqMfzJ0AgJydAt59xVQeUF2mKjzrDAv5F1NyCqB9rKyDjzdqgODwtmygFAOlH9dPeV5NSt1GgyPxWGr_Q97dD_bCHPlVwyVNuF18v4ibeGa07xFXLE6cwFFIww_FtZWzgHg4ufj-guV0tEdENSLGT2ypsuPAnZQtR_BVWkUfl5QtKN16fGNBQw9h8oq3ikARkVp_Clf40cG11jCSpsIUytB_rPWQx2Uh3DLMvy1SIpZmK41g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇴
🇨🇴
خامس رودریگز کلمبیایی باعقد قراردادی یک ساله رسما به اتلتیکوناسیونال کلمبیا پیوست. دستمزد یک‌فصل خامس رودریگز 1.4 میلیون دلار امضا شده. خامس دیروز درآستانه‌حضور درسری B ایتالیا بود که دستمزد باشگاه کلمبیایی بیشتربود و پاسخ مثبت داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29519" target="_blank">📅 13:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29518">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCXLjhbT7gJJl787-4hXHJaGyJg-dlfcffleRkmlQFX739yb1Hr-dutYfKhwlZF07naHvijFazMGzPpA99jONOhs-hzED6xHdnhM-32r1FhDr862XDT-ouU-IgJbkna6htuUk2Tft5upxm6lB5K5XAqB25exSdhOdfGgLJ6eql7j9BakWoArYpS7vMz5bUcH7zTwqrpOwEy0bseyHtX3MJYTNV_9BoA3gT1LkeXsblnto_2702VB-hYLtRWblAkSUH5uKZoeU1t2QRBeAlsZSkCyNmtgbikECu6154gpBLm6YJfBCvUJfp8iBVFUYltiD0cPPm6UxTUMKZGGmNktIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی دیدار دیشب استقلال و پیکان از نگاه نشریه متریکا؛ یاسر آسانی بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29518" target="_blank">📅 12:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29517">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‼️
نجات دروازه‌ برگ ریزون آنتوان گریزمان در بازی این هفته تیم اورلاندو سیتی در لیگ MLS آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29517" target="_blank">📅 12:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29516">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDmdYhRHCixq7M0inx8faGeX5FpsqbsTV-3IeGnMv-I8fe6tB4XQZ_AYM2c09r6PeuU8cIUAUC7mCtmLUIFD5iDcA_W2jqCSWGaliX81Aq3K3GZqFeeAfxjq0GCakSnBfXscxd5I3PNvmp8GKma1CNpixGrIYnLm9UrMXGa5mqKg5dd-C2PVC29IsF8d8CZuhdSMBrAEyJYTnJetkF6iFUSkyTEs38eVbrB5bFCUB4PsOPFds8hG_upK2LGv2rTQfVV4pYChL69lX6_JzWoTFDxFY2x_Ri318_-G2I8vcIKwD7CXtSMDKaY1nJgne39syRBPZCPsB7e9s8YW6_lO9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
بعدازتساوی‌مقابل آاس رم؛ اسماعیل کارتال از هدایت تیم فنرباغچه استعفا داد و اعلام کرد دیگر هیچوقت به این باشگاه باز نخواهد گشت. کارتال هر بازیکنیکه میخواست رومدیریت‌براش جذب کرد اما نتایج ضعیفی در همین ابتدای فصل کسب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29516" target="_blank">📅 12:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29515">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxdkPCGuF8L55agRGDt__HVn1Fww8bYDRngg7ZYCJfTyUO9LlyVuGVRTTE_NaDVvHdM1HbMqUp-mqVwCKuAW1W3rO3LYejsXK5SgE19ozOWMYPrM31iV4cghJPK8CPb1qt0zCgGgkHj1CdkymBekJQm1jDKX5mgSPfsHKeG86OBC77mYtqOG90sU0iJcL54xB0zSHAicJe6h07RFFaKIHCqA6lL3AuQEedbUb1nq0KPp7IgwilOdUZRmflBW7boHXzJCkowl88GqwoMk5mhLheGkAIVXc8B1PegPEJzA_GQoDSihIWq5-eTwen8dpz0V6wuA7j5GAHGYTsE1EFTeoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
🔴
#تکمیلی؛ باشگاه خیبر خرم اباد به دلیل حضور مسعود محبی در تیم‌ امید خواستار به تعویق‌ افتادن بازی‌این‌تیم باپرسپولیس شده بود که مدیران سازمان‌لیگ با این‌درخواست موافقت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29515" target="_blank">📅 12:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29514">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‼️
دو گل آفساید تراکتور در بازی امشب با استقلال خوزستان که طبق گفته کارشناسان گل اول به اشتباه مردود اعلام شد و در شرایط سالم گل شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29514" target="_blank">📅 11:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29513">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMU3iOw-hklMjwHAQ0-EWlqYa7fRZsWJU1Mud08t_Fm3Es9CP11RUtfPBpKR_TwJYzRJrdHFMTIivblr43hILKpw6FFAW9x1w9eNnPbSXkjFd2TtKjqxNGy3XreGS0ImPrGOB4yBtGktsFf8kUYOw_ve0e3q_SD1nfvNQ1MUKYwLbaHZionklcT6JSbfdQibZ-PLOm3Mi2U9GDAHOm7ZYBUL-OJXpCi9fAx1Y8AU8WSIkyLProyEevN727DxTiwxaZfkMtipIXrpbdiWOTSKsykha6cAhq57qscIsGn6lK2NVH3wNoJ3UfUG9qNJEwQ0LwsFWQc9mdK0Q562kU7X1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
ارلینگ هالند ستاره منچسترسیتی:
یه صحنه تو بازی ما با پورتو هست که روساریو داره باسن منو می‌گیره. دیدن عکسش قراره واقعا جالب باشه.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29513" target="_blank">📅 11:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29512">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsXwH-E43KoVSjE_W3lyA4r1rVUiB-3kPz_3B5hEQzXKmSsPsmKZucgt-nzNuueLUtrmzsPMJDsq9kudGqYKUel66N-mzqGvtxrO_O4OaJL_r7mE7Ridqjoq9HZJm525knjJusSMj2Vr3Qp2OFqqLp-uogIVefVlWaTjiVetZofKlgrN19LMgeTApPdUQ6mSoDGQroeOSc3kQ_lLhPT4Mz8MEdV6awrPyYgqc8i1EtUsSIW9K_uhRb7U3DhcS-kZ3UiS4WJs-cCcm4lX7dOz-wNJAezKwSftxqfXvO08LLqhz7DL-vpMm5tG7LCCTyPwFuwFWdaxvqEYo0ifdjFfXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دی‌پائول به لواندوفسکی در حاشیه دیدار بامداد امروز میامی و شیکاگو: تو دیگه کی هستی احمق؟! من‌دوتا کوپاآمریکا و یک جام‌جهانی بردم. تو چی؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29512" target="_blank">📅 10:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29511">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEIIX68a_KXc37ozuc3x0Bi-jkJsqMZOLfP3z77PMobGJymk-aO9gwcAGQ1X63GVeZ2uCeVerXx36E5RzD7_GXCB3_5b1CLG9OAGV8coefVLw_jnK9mgxYFCmPHFtdPnKZf2AZaBRoFJYgDtD3VJe6JzU8VabIzH5wSpPGSB1O664LvmCE3zn4BIilcXRW0-NmjyEO1tQz5-Q3ijzR5Tc2-vZdjSZNU2clI1ieWYBHa4WL_U4vEReBIeTFMgVwiIi-FhnXFkUQYmuDraS2qciujyk8iZpmX_P1gGKhVi8SBedKeTkekzu4V7uyPFdEIgU63RMMfsu6iLF-_J-y71Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تونی کروس:
اگر کریستیانو رونالدو سال 2018 رئال مادرید رو ترک‌نمیکرد ما پنج بار متوالی قهرمان لیگ‌قهرمانان‌میشدیم؛ لیونل مسی قابل احترامه ولی بنظرم رونالدو بهترین بازیکن تاریخ فوتبال دنیاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29511" target="_blank">📅 10:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29509">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad4501227.mp4?token=Q4Z1A0GuTGysqaiYwqV8pRXxh1mp6B_hlWXwevkbUbNStyjqE57ounUkGSn_AZNOGoAVs6gsG9O6ulWtdOkEBP95g_yl1MSXtolJyIPv6S1t-m_tPcuatSAxanTJnjJLMXLvJ7mBYTX64x-SZPWR7LMWv6vRv17NNJE2unMOpJH-0OUgTi0DpxaRkBGDD7TETXfy-WyV9KL5427edDP-PQXt-hMQCpx2ZCn4nFHCuBB7iAwYPjx86Gr8xXtqBb7175ltNK9DCJ7ynqBseFFWFnCrCO4wXaJ-y_E4a1M_9VHR-Ldr9o-EGqeRPTo7wrAPJWdABXPkOciFYr6CCLCvUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad4501227.mp4?token=Q4Z1A0GuTGysqaiYwqV8pRXxh1mp6B_hlWXwevkbUbNStyjqE57ounUkGSn_AZNOGoAVs6gsG9O6ulWtdOkEBP95g_yl1MSXtolJyIPv6S1t-m_tPcuatSAxanTJnjJLMXLvJ7mBYTX64x-SZPWR7LMWv6vRv17NNJE2unMOpJH-0OUgTi0DpxaRkBGDD7TETXfy-WyV9KL5427edDP-PQXt-hMQCpx2ZCn4nFHCuBB7iAwYPjx86Gr8xXtqBb7175ltNK9DCJ7ynqBseFFWFnCrCO4wXaJ-y_E4a1M_9VHR-Ldr9o-EGqeRPTo7wrAPJWdABXPkOciFYr6CCLCvUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب سسک ‌فابرگاس سرمربی جوان و موفق کومو درباره بارسلونا مدل هانسی فلیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29509" target="_blank">📅 10:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29508">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de5e1c9532.mp4?token=NQ54wrYqLt3O3jOPN60rNsO5GKdfOnZXHzuDfQJnVIxux0inCgMJBVAeLMm0Q0Ls760cSwio9LVDPQmphD6RWykM2Y7pu0Tmu2TT7AWW-tiRUyIDOa7edOYKyaXkKxLGpJeZExDuo57VA2aP9gIwJk_MDz--Rp80yOmwX_Kh2ZWVhLD3xGZ9Wx1NXRIZyCOLaxsSkYZFga_XhX0BmJw4R2OU04xVPMOaZqXhrVbMODowOb4uYZkpKBmKBQ2pGyU0c7fYwyr3BnT3wSvnRWAr1Ol0n9ur_uLeYFO58GZwUSuyaJRP2G4lr3NyKgZo3H1CjupXt6RKp6wi42E9Ikfu1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de5e1c9532.mp4?token=NQ54wrYqLt3O3jOPN60rNsO5GKdfOnZXHzuDfQJnVIxux0inCgMJBVAeLMm0Q0Ls760cSwio9LVDPQmphD6RWykM2Y7pu0Tmu2TT7AWW-tiRUyIDOa7edOYKyaXkKxLGpJeZExDuo57VA2aP9gIwJk_MDz--Rp80yOmwX_Kh2ZWVhLD3xGZ9Wx1NXRIZyCOLaxsSkYZFga_XhX0BmJw4R2OU04xVPMOaZqXhrVbMODowOb4uYZkpKBmKBQ2pGyU0c7fYwyr3BnT3wSvnRWAr1Ol0n9ur_uLeYFO58GZwUSuyaJRP2G4lr3NyKgZo3H1CjupXt6RKp6wi42E9Ikfu1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از واکنش دوسرمربی بزرگ دنیا پس از پایان رقابت‌های‌جام‌جهانی 2026؛ یکی نایب قهرمان جام شد و دیگری‌از آسون‌ترین‌گروه‌ممکن‌صعود نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29508" target="_blank">📅 10:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29506">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ec53e2096.mp4?token=ll7-scGeuOwkrX6CSPmGPk8piF3FpXyI657VfMB0XA3iFcWekDRzSCnDQ3Y58TeNwOTWWC-f1cco7iIGtyBs-4QshNljusi_fiAUN4-_UQP1JGtGlpEnBfdnzdfMG3WHyP6PbbgR7ZSi2DRmGqyY2ifoNceYDvCE_X_v5g8pr44JZEFcGdUt-ThpPyJeYpwR3ta8sQyEUN9hC9JUbqQt2FiFEZDmFCU6BKPAl7zCFHZKGgtokOxioC2EdzOAdYzJcGzQ2RXNp46W9FdVgmk--im0tOTkO_afDlddWLovXMiIvBdoI_QB_X8L1z-uDrTHVm4hntohTDr5G0zmeYQOUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ec53e2096.mp4?token=ll7-scGeuOwkrX6CSPmGPk8piF3FpXyI657VfMB0XA3iFcWekDRzSCnDQ3Y58TeNwOTWWC-f1cco7iIGtyBs-4QshNljusi_fiAUN4-_UQP1JGtGlpEnBfdnzdfMG3WHyP6PbbgR7ZSi2DRmGqyY2ifoNceYDvCE_X_v5g8pr44JZEFcGdUt-ThpPyJeYpwR3ta8sQyEUN9hC9JUbqQt2FiFEZDmFCU6BKPAl7zCFHZKGgtokOxioC2EdzOAdYzJcGzQ2RXNp46W9FdVgmk--im0tOTkO_afDlddWLovXMiIvBdoI_QB_X8L1z-uDrTHVm4hntohTDr5G0zmeYQOUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عرفان‌کرمی گزارشگر دیدار تراکتور
🆚
استقلال خوزستان: گل عارف رستمی به بیرو بسیار شبیه گل ده سال پیش کاوه رضایی به این دروازه بان بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/29506" target="_blank">📅 10:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29505">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59654769b7.mp4?token=SIh_5W0cleBsjg92qzwhAl6vFIfnGrk0I_HrtzdRLNDtTz-VRQsDS6ylZ8GAPoIEtiskFqb1YYUOAqUgDrseyWveCjmbSoyUJBiNpL0y1LKa7Qai34Y8CUDpHE3AJFAnBoMT23OvBsOdxbkdBFi7HwJWC2b5mRiqyIOv82Q8eqn3U5wZbObn_Ri3xahnacfXpXfNv5VO7__a8Pl_tZg6jd2-BHKAPyypksfIA7h3euN-COjEYJpIzhkJtVJTkpQtGqyokk7MX71Hk9ILyAKksWddy7CDYJXSaDojzdO2LrUMWqs89izKiITxfBYgExUk06_l21J3bVyAzVkYWrsXKTim6c0OxaI1jzfFfoIXgJYvgnnLQGQAT8zvGuuYJEeA0R_85-NkxXbwiXJPpLxnJtMBhdBnX4x8PRGxCvQYG0FrBYHCmFSh2cB1wHgMoXNvQFL19OaQij4EkSoT2pYfuPSu_-ivfoHVCxNbNtzGCgj7u5SzyaOqDEUGBwiwnTwlMaOexQgtPOszfTjDcDHoydb-M3IJMG1Skb0SSy8d3XC6ZOpyWITSlw_l6nh7ffzN0Xpy-IuNDIv9n0sAva1lC5yekTxf5LmhL4AhKxr_zz3qb0aIQh0mdmgbC0P52wJfp1iWlosTHdZrW2iQ0J5HkRLhZ5IZEk-G_kvgITauH3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59654769b7.mp4?token=SIh_5W0cleBsjg92qzwhAl6vFIfnGrk0I_HrtzdRLNDtTz-VRQsDS6ylZ8GAPoIEtiskFqb1YYUOAqUgDrseyWveCjmbSoyUJBiNpL0y1LKa7Qai34Y8CUDpHE3AJFAnBoMT23OvBsOdxbkdBFi7HwJWC2b5mRiqyIOv82Q8eqn3U5wZbObn_Ri3xahnacfXpXfNv5VO7__a8Pl_tZg6jd2-BHKAPyypksfIA7h3euN-COjEYJpIzhkJtVJTkpQtGqyokk7MX71Hk9ILyAKksWddy7CDYJXSaDojzdO2LrUMWqs89izKiITxfBYgExUk06_l21J3bVyAzVkYWrsXKTim6c0OxaI1jzfFfoIXgJYvgnnLQGQAT8zvGuuYJEeA0R_85-NkxXbwiXJPpLxnJtMBhdBnX4x8PRGxCvQYG0FrBYHCmFSh2cB1wHgMoXNvQFL19OaQij4EkSoT2pYfuPSu_-ivfoHVCxNbNtzGCgj7u5SzyaOqDEUGBwiwnTwlMaOexQgtPOszfTjDcDHoydb-M3IJMG1Skb0SSy8d3XC6ZOpyWITSlw_l6nh7ffzN0Xpy-IuNDIv9n0sAva1lC5yekTxf5LmhL4AhKxr_zz3qb0aIQh0mdmgbC0P52wJfp1iWlosTHdZrW2iQ0J5HkRLhZ5IZEk-G_kvgITauH3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
مصاحبه جالب و عجیب و غریب مایکل اولیسه ستاره فرانسوی بایرن مونیخ در پایان بازی دیشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29505" target="_blank">📅 09:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29504">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cea298e80.mp4?token=asn926-ra3avJxkzhxcL4Ro8EvAr4tlaP0zcy1QGgTCnvBk3E2Ex50v5WL9VP_U5LIbAXU2G_mF8WN6WvwyoaAun5WSuuJ09R3qzyfxzDfAyyCkyZ0hrBl_4JyKqGkpVZqF9LL40AM6HkWhFsHJOmUvyecOXJxVHbpojNci43QiKIcQlcMfDyTs-eKftzTw5jiauZHjFNWWMWs42MLU18NZW0Gj6d6iN-sEn-WHyQbCuEHsbTZOeVo9_RYcnBuJMgknfU5sCELV4ihUq700HQxn2okEf9T4qFvuaIV39R6CIriguZTEzhR3MHvkaERm7T9f65k0ywXEeRge3ymqAgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cea298e80.mp4?token=asn926-ra3avJxkzhxcL4Ro8EvAr4tlaP0zcy1QGgTCnvBk3E2Ex50v5WL9VP_U5LIbAXU2G_mF8WN6WvwyoaAun5WSuuJ09R3qzyfxzDfAyyCkyZ0hrBl_4JyKqGkpVZqF9LL40AM6HkWhFsHJOmUvyecOXJxVHbpojNci43QiKIcQlcMfDyTs-eKftzTw5jiauZHjFNWWMWs42MLU18NZW0Gj6d6iN-sEn-WHyQbCuEHsbTZOeVo9_RYcnBuJMgknfU5sCELV4ihUq700HQxn2okEf9T4qFvuaIV39R6CIriguZTEzhR3MHvkaERm7T9f65k0ywXEeRge3ymqAgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته هفتم لیگ برتر؛ کار بزرگ خوزستانی‌ها با بردن تیم جوادنکونام؛ تراکتور بالاخره در هفته هفتم تسلیم شد؛ نخستین شکست‌پرشورها در فصل جدید.
🔵
استقلال خوزستان
1️⃣
-
0️⃣
تراکتور تبریز
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/29504" target="_blank">📅 09:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29503">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95470742c3.mp4?token=Nq8bkpFyHCBN6-Ut4EHrNrG3O53AQWItq17WZwVJKCVe2DpOMjZzPJARak9VyHCtzrGVB9F7ka0VHZmTw74SE7ysO5t5uneTMvkm2pvMAIXXAxgKv3_CZQtSlicJdrY8gD_e6Ep-8urer5TJcNz3s00ZdOEcxP3KMLC_aUU6Z_belPDhdrqJDgGGAY5mHwEGHC4xwMjODshlfMt09AmFul9LsseV-nZ8eeKKsrZokvJ0hJXSyHH4_A8rGvswdHdNk3xBvyta9RlrrzP9mHgArjKjUt59jb70wHE1ZCZ9SZXFpk3QaXHzzKeSvfDuwjJiodTsz0dsxLo7ja_URudC9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95470742c3.mp4?token=Nq8bkpFyHCBN6-Ut4EHrNrG3O53AQWItq17WZwVJKCVe2DpOMjZzPJARak9VyHCtzrGVB9F7ka0VHZmTw74SE7ysO5t5uneTMvkm2pvMAIXXAxgKv3_CZQtSlicJdrY8gD_e6Ep-8urer5TJcNz3s00ZdOEcxP3KMLC_aUU6Z_belPDhdrqJDgGGAY5mHwEGHC4xwMjODshlfMt09AmFul9LsseV-nZ8eeKKsrZokvJ0hJXSyHH4_A8rGvswdHdNk3xBvyta9RlrrzP9mHgArjKjUt59jb70wHE1ZCZ9SZXFpk3QaXHzzKeSvfDuwjJiodTsz0dsxLo7ja_URudC9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇫🇷
درپایان‌بازی‌بایرن؛ خبرنگار از اولیسه میپرسه میگه حالت‌خوبه اولیسه میگه‌نمیدونم، خبرنگار میگه حست‌چیه دوگل خوشکل زدی؟ بازمیگه نمیدونم من همینجوری فقط شوت زدم توپه خودش رفت تو گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/29503" target="_blank">📅 09:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29502">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdsZ54b4zftffgU-JeB-KyHBRCGhtXXaquV_YWFBKF62Ft5ykjbrqRH6D7Xko7wx6-ZPTVFTOOaI0nhH1Y8ftnab8-SxUkp3qiFl5-15Eorchwoq3NF2aliL0dwtRJzikC1dxRokOn7FMQzGOg4CN99g0-lLng0-yyDhLUiWjB4MvRjPyaXsj4-1lcA4triUxFLLLiPTCC3q6QYyLxf2j_sxcpvp3iD29GL2iPYaQRgVQqGbKeXuCNsphHgRYgrm89K1leuzJRioX0n489xU-UUMLfEwBmttGrZnojK936ScWpPLgWhMxehXeHUumflNleM754y3osjZ4oXS7yXfqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
بعدازتساوی‌مقابل آاس رم؛ اسماعیل کارتال از هدایت تیم فنرباغچه استعفا داد و اعلام کرد دیگر هیچوقت به این باشگاه باز نخواهد گشت. کارتال هر بازیکنیکه میخواست رومدیریت‌براش جذب کرد اما نتایج ضعیفی در همین ابتدای فصل کسب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/persiana_Soccer/29502" target="_blank">📅 02:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29500">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a82a62e0d5.mp4?token=EnMP3BC1a8djsij1UDjgdk5KupHe4JPD0yH_zOt05aQrijJTxv1PJ8MuMBb3LZczyZa6LzWEfGT-1w0j49SZpJeRLpfkG7K10LoDItbvfBp7biYKPoHvwEeYgwa4SD9Py8NohqTELTEPiHd1PY0iONvgdV9YOAZz31gNNGMlmqUsWSm3b6xSQyZfYbr7AHGGBaE1__PdswDTKWD_E2o1BwXZiT8b1ilrX9fKutJXdGEBrK7_wji_e1S6w8pFUS67SJtmikRJI5Gf9BPlYysZpf-sWSZezCVvw8zdyIcXAHCrjR4xIdGMaxeQormq8Un58ixHsg2EwlCkbDucVVtLOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a82a62e0d5.mp4?token=EnMP3BC1a8djsij1UDjgdk5KupHe4JPD0yH_zOt05aQrijJTxv1PJ8MuMBb3LZczyZa6LzWEfGT-1w0j49SZpJeRLpfkG7K10LoDItbvfBp7biYKPoHvwEeYgwa4SD9Py8NohqTELTEPiHd1PY0iONvgdV9YOAZz31gNNGMlmqUsWSm3b6xSQyZfYbr7AHGGBaE1__PdswDTKWD_E2o1BwXZiT8b1ilrX9fKutJXdGEBrK7_wji_e1S6w8pFUS67SJtmikRJI5Gf9BPlYysZpf-sWSZezCVvw8zdyIcXAHCrjR4xIdGMaxeQormq8Un58ixHsg2EwlCkbDucVVtLOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
گل‌های‌دیدنی‌بازی جذاب و یکطرفه امشب بایرن مونیخ
🆚
بودو گلیمت؛ حتما ببینید از دست ندین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/persiana_Soccer/29500" target="_blank">📅 01:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29499">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7SIAIF4WmOyIc-OGWj2psG1s8IsyyxWZ_M4DLaq3A1U_qpL1XSgmyqfNySHG9L78lWot3OGdKWCrKFuSgnwjraKruClCCVsFvhXb4zmeFyf3sujDMnP-wIenlanh0Ie6_yCtPgunyMzgKDsSi3mMMaZqAQyUexWAv9AMFp1tjFxHFFP8P_cIwF_659SGnAbnHTmap5uPO-ppDxMcKbw4xdgWz-Df1-HcNhbaLPAIoQLeKR0MTD4RDJRyXZccLozBQ4JvqERZ5QgeS2BQf8fSKXQtJVH50tpC_9DXgjxjE-Sl0LkS1J5kMAvvhE8_z_kCkztDl9jq6pMli7PG8K_6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمد عمری دیدار باذوب‌آهن رو ازدست داد؛ با اعلام پزشکان باشگاه پرسپولیس؛ رباط داخلی محمد عمری ستاره25ساله‌سرخ‌ها دچار کشیدگی شده و به احتمال فراوان حدود 4 الی 6 هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/persiana_Soccer/29499" target="_blank">📅 01:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29498">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwDFrXzLy7rRYA0QQWdLm7WXvFCEo87AVaZe2wyBifOewAl3MzJuYPeb3IglS3JA7uBWXjpPQsHy8dOHq2Eyu8FGA1qJ1KyQvuce7sf6GwBlhR5uZGegGRfcR6M-0nyie8TF9ULzCVyZib6iZv7e-zqfDjs45sUigCBufa9FToCrTvgkulopoKvPpuKj-Hv-5VIewIadkLRJPcRq8z6r8GGGiISFCT82H63qIOg_9sHoAltYAMbkIW2N3LCWDoyZpQnVJDRN2y960D_njaL-bPoB5Lqh3dj0_97jEExeTqi2ywBUzmanA063QRA4TWpODpQrOr_-AABNxBePZHMt9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌کامل‌دیدارهای‌هفته‌اول لیگ قهرمانان اروپا دریک‌نگاه؛ برگاتون‌بریزه دراین 18 مسابقه 69 گل به ثمر رسیده‌شد که یکی از یکی خوشکل تر و خفن تر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/persiana_Soccer/29498" target="_blank">📅 01:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29497">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8wquZO6f5uA8NBRNhO3FiUamkowbrDEwhyli0sQFIzlnFWLmgfCCG-7BXHbu4TrIzG7T_p65jBo49PFnuJ28WhLXxAWGNrKD5m_W_UoD1nIfOImkta5Cf4ed9O-KMXlWouLElyjXnuq5ZCE6PegGpBEXjYqGNdQxlldU0Vs4fAnJiW9uF7AAwQX-w6vAGdsuTAERAWBoxpOaPxFw_8pCYVzH9Dz6YqFkmOh6My8ADZ_MgW1prN_i6p4H8kVmpNEiA-61RQYBU5HWQptL6HGwz4R_wj4dXgfh623GgO7HLiFedORplaRSk2VNiMloQRGrutP2Fq3DjMXjWG52NXW0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛ مصاف یاران محمد قربانی با تیم ژوزه مورایس در هفته پنجم لیگ امارات
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/29497" target="_blank">📅 01:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29496">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyvAr9cPuvZWYqlReAojS34bmNGzhjwGvs9gmO616lWomb6bBNXayw0Kgr6zlZ8Jl36-TbsIoygbyY9eVjH5jvgelwkAD3_t7mmp4PLWvL5NAjupKcwq-lmscHk65m0_4Tq-DXrjwaQ6kqgbNpInwjm0EEY2JUIEkIa0rnyXOGGyIjlr0-TmXBsxxFKjiPid6hpgX1YoYRBFkUpYTVJAmjUYS9_mZda9rJTNr1IaS0u81E-bxYktGDQdm8nKugOUxsFdRh_DO0_ToGp6wWHfQRprbu0FJ6qDyaTELbVeaJ7MDfw9UneztkBGVVL-TEGUhuQJP6RMhd8HZLjHE_AwBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از برد آبی‌ها با تک‌گل آسانی تابرد قاطعانه‌بایرن‌مونیخ و من‌یونایتد درگام نخست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/29496" target="_blank">📅 01:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29494">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">📊
نتایج‌کامل‌دیدارهای‌هفته‌اول لیگ قهرمانان اروپا دریک‌نگاه؛ برگاتون‌بریزه دراین 18 مسابقه 69 گل به ثمر رسیده‌شد که یکی از یکی خوشکل تر و خفن تر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/29494" target="_blank">📅 00:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29493">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇪🇺
نتیجه‌دیدارهای شب‌سوم هفته نخست لیگ قهرمانان اروپا و جدول رده بندی رقابت‌ها؛ آتش بازی باواریایی‌ ها و شیاطین سرخ مقابل رقبای هم نام و نشان خود و پیروزی کومو؛ اولیسه باز هم درخشید و داغ فلورنتینو پرز رو تازه کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/29493" target="_blank">📅 00:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29492">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_PXHj1DuQetqNfCxHW_7wFRO2USI8984AN_Jh0VRtaxqs_5z5WQf6HIRQKqr2GmfzisQk0fci9s21dKNX5oFA_xi5WoZUfmvlPCnuYXosgXMfTrwmciNPz_oJnnPccYRFQFC1kcW1yfJ4LvnQqX_viqqW2DVoPuEgS2ZhfV0AlZJD9Fr8zxv779j34kwJYQlbxjG_HDHRlD1IdWqk--Nrqwstkt_Rg78f2RWsAjCQNqAPjbp5Gcs4CvwB7QGnQPMrrVbw9x5ycyrAvX0WcHmOC4TziBfW4A5MLktj60zOKtDGeQPqQ7fEGwIC1QLiGzC2gIG71wTpz0nMIVLzL-cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه‌دیدارهای شب‌سوم هفته نخست لیگ قهرمانان اروپا و جدول رده بندی رقابت‌ها؛ آتش بازی باواریایی‌ ها و شیاطین سرخ مقابل رقبای هم نام و نشان خود و پیروزی کومو؛ اولیسه باز هم درخشید و داغ فلورنتینو پرز رو تازه کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/29492" target="_blank">📅 00:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29490">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oz3iIItaAlyDKjeWfCqQjqai2WDD6xKNfakK51MeOlHwgPhG-W2VkEz9vAOCO-yZjt1Cghmq0iLNh7TaxvhIDMWF43Q1h3hfSu1Ns7I4IbX4qiKy5SSW2zNktPD5wV8NhlpFcFb-Q_sFe3aWhAkR_Cb19QUri8EB7196RRYODVIN8gs_J0yJCP9soC6_txsQT8n-LE4xJSnGNFOYYQGlAeqObRTqnS5Q5rU_hj7JcjzoqEw8tKK6osZgOQcwLru8ZrZNv7QIRU47KbZWzZMzhcB_bp6UtsHQTy1SE-FsHvlKSkvVhMuvTx2jebEKa0mLo4zQ--PHWwnSohCjKdipng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kyKgBYNoGk06L3qVkCoDTppn4aObzkOCmOg5tCSYVHKdVEiUdbGodUzlA0-E78Z_BMGyujjVCScrzeaQ8ndSRkTeE0SQOuoKS4dC0MTfLJBQbXT1SucAR1p83jrImJ-qWoKEjzVwzURGYZtpzcPf2yj022rs_LxKGGAHQ5nSinlt_1LJSwzGwiZduQ5LQf5D0Ru28oNJQI0rnRzmhB3xVjRLcSDWKlaWoOZ5SPMQ0Ae7aDO4AoCCPifMgeCWyHSgChoY-qewqCwp-YtP9S0FdbCwamoCcE4zoN-Dkn5LOWJ0XXaCBO7oDxfsqgLrGMs-V34qTNk2JpxI59vM_9a5fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز؛جدال آبی‌ها با پیکان و نبرد یاران کمپانی باپدیده‌نروژی‌فصل گذشته چمپیونزلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/29490" target="_blank">📅 00:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29489">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‼️
نادرمحمدی تو روسیه‌تبدیل‌به‌یک‌سوپراستار شده و هرکجا میبیننش دارن باهاس عکس میگیرند. همین روزاس رومانو بزنه: نادر جون به آرسنال هیر وی گو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/29489" target="_blank">📅 00:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29488">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjF4pj6ACmGN8vWfZfjlETrCh0PoruArm4PQyomzKSyCWLAcCPUh9IMgZxvAnEGpwMh5YiWcvLyYLwy01NoTWdeG-QYh0f-afQxHO50DeYyZFYMXKVkn7gPGOdPb3IUo1lb9PQIo0gdfldvVkeJ3KkuZQX3EFOxOAOSRWv-T_4nRi8NEva4ElA_zF84t30saffQmRp2o98h4ortsUR7CSgD4Al9q-8DeqG0T_t2Fe60FD0D8s5kIq_MimOuscoghGUgjdyDQ1vcrsYxCKZMEiW7xvkG-3dpd1s4kp8STzW_6yAB4eaG0JTMxIPl8M1DVfFdAR4nRoEokCVSRMaD7lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هواداران باشگاه فنرباغچه بعد از شکست این تیم مقابل تیم بشیکتاش خواستار برکناری اسماعیل کارتال از هدایت این باشگاه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/29488" target="_blank">📅 23:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29487">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lT2AVLHgMbx_67b2N_u_P3IIpUPTojzlro32CnCFvqTGHkUBfp2a64ptYV9r-PYhGTgvv-d1UXwJdKoh05Mokf8yYCMnm1Jot3JSwJY5aHg6eWHV6bVXHUKLgZeb6bQYaQG2Inhmb73sHPQnV19IOMVp5U7LViOj6rZEQWrmPkD2kZoOcGkO8H9evjbIhG3J_V4b1qDX4_gIItzcWrC17CYrFdMslrBsVSFNqYNo8lsQgVfscgJtZNLkrtiIIghsxKiMtTROyPqDL4jg-CdklLZsLDCfEbVXVpk3zOkJP6V29X4WcAT5g2MxdB8S3IlzaxFbUfdqTT4TOtMn6her1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تقابل جذاب دو فوق ستاره سابق تیم ملی برزیل رو؛ فلیپ کوتینیو از نیمار جونیور برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/29487" target="_blank">📅 23:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29486">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4qSUf4MH080MWceR9obXEy9F6GPkbZ4vrx7vQDifCm5j0V6NozcAulbFvmrvS-tHBqG79iUFvLxDXN1Iqk7WDHZdoDJdRzcERY_KEZtcGShx1DAKIIQuSqwo6mdr9SSNfRfRfzL0cpGAq7R0-iXVZz6s00v_hw2LsaKy_6ww0nnDADhNxGRmevW3Him6zJSMmOifABRwbFrWatnzjut03MecDW5HN3JmABwDziUQC1VgCMD0eiYbvGw9evIj_IPL3A-oTKs4WnUTMA73HsoorxC5a4kI4RvqPzFTIcx8FrReKV89u8SRJLYCsmWx03VBbgVo8Ulbq5b5X3U6ksYng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مکالمه و پیامک هم گران شد! از فردا ۲۰ شهریور تعرفه بخش قابل‌توجهی از خدمات ارتباطی افزایش پیدا میکند؛ آنهم تا ۴۵ درصد! برای مثال سقف تعرفه هر دقیقه‌تماس تلفن ثابت با موبایل از ۶۲.۵ تومان به ۹۰.۶ تومان رسیده است. عالیه. همینو کم داشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/29486" target="_blank">📅 23:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29485">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkoZTZlBWpo3wfhFyp0k866kdPKF9bYJKRuHbhc8U-GxY9v0fWyDviVZQnWFyW-X5WO43mY8vDRtZDWX4z95LMjgrLpyLtJQ7dHOPKKTxBtfs7YD8n90aYBhYfdkUyYS_azWDC8qT7b_YlcBjTQH43YhGXVCiIRvQPJlVknPwkYaC83x6jeV8zA9Zvc8SCdjvl8SUiLMbM6iwpNQWAJF0vEZs_JYdHVuafz7EcauS8adfvKnQ9ORlWue_udUZ49a3dNanstwp_4g1nFkNaDHIMnwjJuZePC0OorYZsvIj4FkkOWTiJw8GzgRgVoyd8Iax2ngBIcGDA06Yg-arAWh8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌ گفته رسانه‌های عربستانی؛ همسر مارتینلی ستاره‌الهلال که دندونپزشکه رایگان دندونای 50 بچه عربستانی که از فن‌های الهلال بوده رو درست کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/29485" target="_blank">📅 23:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29484">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGY-l5AiKiUeL6EXpf5gnN1P5Pv1NOyh_l6ls1QBT_E5YzMQkhU5SXjvYt9zrdbGjGzvrAgrtnzNsK6bKWEpj4JSIn2TEg-y6cdT4s5RqxX3YP9zL_wjwGIHgdT5c8hYYTBXFdUJLyQhGIC-vXfxP4l0fOnuAWO14fY-itoEG3TkZF9tubPT8rfTBLvTMwS58Zc2ximYT6IjMLiu4pdbzzLFeN-J52YyzF6zfIg4NTF0qQ2w18C2lylFkHCSBLkQ8n8wjlWIWqsmS3oHfal2yX0JLBHDO35KFkDbxqYCeB-vm1Q8j4O-m4xOt_y0uoaTOLPI48x5XbX_VhFvD8qVOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇳🇴
#تکمیلی؛ باشگاه منچسترسیتی انگلیس برای‌فروش ارلینگ‌هالند ستاره‌نروژی 26 ساله خود در تابستان سال‌آینده 200 میلیون یورو میخواهد. از بین دوباشگاه بارسلونا و رئال مادرید هرکدوم این مبلغ رو پرداخت کنند بند فسخ هالند فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/29484" target="_blank">📅 22:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29483">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJTZ1XD8Es9Tu016F1BLIEaytYNXEsxLKSmwntm1B90BRe-_suiriR7eLPf3yaXtsEkq9GDH4R5Q7_lNiR54cTdI8393a4mtTGG9-m3-cJeI9uzKxuUNcRtXn78JQjUJ7KDuOrpQN5fqAIp1uCW9szhaDX0orf7-B2jPOyF4oDGioT7I1mK5vLBIb4GDMMiqJMJEyQaqgMW_ku_BtrL6jft9qDdHE0yyGtA13ielKIPzyhg8NcnIg03QuEr64B4BJxcDWI0bNMXChV-T3u0ViSLUhtfhpHY7jI5NZM_BcvIcwpXWw-9WttaIHRIHl33HHJaWDSVOFmf4AYepvXdp4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌ شنیده‌های‌ رسانه‌ پرشیانا؛ فرشید سمیعی مدیرعامل‌سابق آبی‌ها درتماس با علی تاجرنیا رئیس هیات‌مدیره‌تیم استقلال‌آمادگی خود رابرای بازگشت به استقلال و پذیرفتن سمت‌مدیرعاملی آبی‌ها اعلام‌ کرده و به تاجرنیا اعلام‌کرده درصورت‌بازگشت تموم مشکلات حقوقی آبی…</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/persiana_Soccer/29483" target="_blank">📅 22:41 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
