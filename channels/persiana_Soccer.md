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
<img src="https://cdn4.telesco.pe/file/LHOFFhiazTWK7cVhJgmWtwL7gCMmVeMTDmPvPB-VYMQQ7oprYo_Q2SlDuiiRLKtY_r2jl1H0ylOKDqHnXkk0HyUJGCCZqkosH_Nl4lbMknjVER8kTbcMojyFiecAbosRqZ3lK7H5v18s-tASzdgmoK0vGp8RraI78Qi3nJhOZfPN5tt3VgTuv7Qb_Ce9q5lmObkDnmKNPCvh7rZUFGMIUEm3XxxOqiqL1mVp7Zm7RWRH57TV6iXBrsnsOeiZjgbTkzkgQ4HrEF9EHPzk-F5d31LHjy7lyV-HR61llYsSYbg952r7sK3zv33pG9sALRdUqVqdlqiffxyc94mWCBEYPA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 618K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 08:27:22</div>
<hr>

<div class="tg-post" id="msg-27032">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huvTI1lTJ5T0fa5iHuckWZP5AJEIR2hSOPVg1RjkgFJbvG5QxYJO-NokWhKRjtrClIG4YYNiINFVlGofcWDyI75_hJvqfjKTG8yFq3SVt6E70U858U0Xk1LA1n2y8UjZwQIW7W5kRxyMW41LHEC2hfIwNHVwAUHQtvxPpO2r0_gapbEu2u-mLqN2ciU0bsxBCHUEx51F0BGxQWwe1fE6k0HU6FbZfMYGX2ieAk69ZOJDaVzKef6ZgBaPOUF5C7_P2bJq-6hZF8zgqBrFExsTPnLRjWewFlgyUm3RXvgcZESjmLdr1110ZEd9Ee-qb8gjHZnnoZaA1oLM5uj04b0Flg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
درخشش‌ادامه‌دار سوارز در میامی و شکست عجیب شاگردان ایرائولا مقابل لیدز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/27032" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27031">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e2aeddb1.mp4?token=jHYJZAC_1OxYHmCSWa24VX_2eK1a785YF-_a1bk_HPCPDLCx8QiM8LpII1Y7Lx9NY-1Z6KXvI0h_6geGhbSebHa5bsg867uurO4GwP_omdyrYmmWcAZh1C3VFbYcaJUQcFHR_UxZ9vuvh46g0KKtVQ-WSpKBwDmeZCXot4lUO6AABMaU0XaFZwKbRYZhipFv67qzQnKIJVpMFUOU79QaDMXRu3wHOCk7dTDr3ssz-wI9MulUDJ1i2_2xpLZQwgnF0b9NjIaF7TU0zdMcELOjFUG5W9PjaS1N-U5P5zPrxphCBC9r4c8-PcShUuZl-ts163vEACAL456ABtsNESfOwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e2aeddb1.mp4?token=jHYJZAC_1OxYHmCSWa24VX_2eK1a785YF-_a1bk_HPCPDLCx8QiM8LpII1Y7Lx9NY-1Z6KXvI0h_6geGhbSebHa5bsg867uurO4GwP_omdyrYmmWcAZh1C3VFbYcaJUQcFHR_UxZ9vuvh46g0KKtVQ-WSpKBwDmeZCXot4lUO6AABMaU0XaFZwKbRYZhipFv67qzQnKIJVpMFUOU79QaDMXRu3wHOCk7dTDr3ssz-wI9MulUDJ1i2_2xpLZQwgnF0b9NjIaF7TU0zdMcELOjFUG5W9PjaS1N-U5P5zPrxphCBC9r4c8-PcShUuZl-ts163vEACAL456ABtsNESfOwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛ با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/27031" target="_blank">📅 01:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27030">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODVKBsvp33LVPzlWNvBejbR28J0kJvnIb8nfSCVfLG8t4f3NgIb220AQ2zEE6N3JeUfS9jlv469b-ZUemeHA2-L1aGA78SjxxlAnfJInAoRrwruJkVwLzWMZEhJE796jYjHMWAZJIIeqIVqId47i89N94u9xX0cOVXalckTg2qqiQOSzR9qlOq5bTiq9AeGeOlYTt26aX8rCWcK2hIg7arpCi00L9MspHiOZwnWg1TqwVYXdMukK_CVfRa_RoKF7IsjAohPhzghyY03lAfWq7dwLPpGmL2y7k_iSMbo1pJCxmINRK9zgZam4485xVWmNAUJ5wZ_wXYM_G0-lwEzVdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
آمادگی فوق‌العاده لوئیز سوارز در 39 سالگی؛ تو بازی بامدادامروز اینترمیامی‌این‌گل خوشگل رو بثمر رسوند. کاسمیرو هم‌که‌گفته‌بود اومدن‌اینترمیامی که به مسی برای بردن جام‌های بیشتر کمک کنم تو اولین بازی اش برای این تیم در دقیقه 34 گل بخودی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/27030" target="_blank">📅 01:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27029">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMXV3VYGb73K0vFtmL5Pf57-jq0226FVbi76ZNbTMaWQlcWkIDYzixccL_rdZw6NU350YjmWNUg-xA6Q0Vle2f5X5JTRRYmhKYDsfIgCvVylemSA9OnhYSxHkWLBvqnEGnlanVjkc9HH7k7wCAGG2CzH5i_idOpExpon9Sv5lJ--HzhqMslkkARaIgLqKtOrKbzDizAw6bFNw0tnLLYwp5oQODygrL_sxXmM11tA0eb0aRs6I9wkbbObl52auCWGsJ1m2xQdRA8j9saRNLARdB8UCf6NeaPwUdwlERgtoYuwaR1V3YXWUo7qmUTDdAUTszH9FBAQCXGZIS0nPbqX7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطورهفته‌پیش‌ازتغییرات مدیریتی باشگاه استقلال خبر  دادیم و امروزهمه رسانه‌ها این خبر رو پوشش دادند. حالاطبق اخبار دریافتی رسانه پرشیانا؛ مالکان باشگاه پرسپولیس درپایان‌نقل‌وانتقالات قصد دارند تغییراتی در مدیریت سرخپوشان ایجاد کنند.
🔴
طبق‌شنیده‌های‌مو…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/27029" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27028">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJo9enwt4zy58rIfDVqfnXv3kl7voNMgPrEsI2ERojZtXbn3__8m3DSrF4UOpYszAh3yBo1goNI0Uq1xZXD8md_5vwzitfS6b-Mvt2ljkIR7_ecJV0NuWGRHot9DtBTKyzmFI5ADPswA6LaydP-4m1B9QJFQjh4Hw5nJrnpcqHTEfYbXBHudv9jvALFKWMq_IcPXQ3p5oqdgQcHMgkLX3sLs3drSes4dqI8lBG_gNHGOdZC4vMFuL-YrnYZW2Y9iTaVGFJ7Oo-rgl15YqDnDD2Rz8d3tfZ_DHXwLGQYYxVxVelVVaTb2_lJo6R5Gf3noUuD-a76IaK1wHCpLcRYE8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/27028" target="_blank">📅 00:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27026">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0AKEHVxaRhZK1UUZdxNVs9PBb5MRaz-cujCXOlLZ4c_PttON8vJHaZ0nwyaUyan4rAe7eEg7L4nopTAAqrpEnbGzIhtPHgZK2h8bTykdurj6j-Yz0HyGLJHTYfCGQBUR68aESYpYhpQtDFGDVkfOw7aCga-qKRW19QXpv5Ut-DULw2c-Qux6vFcj1zMD9CvFN50DNwj1Id5TAtD8RkMVp2bn_XGaDo3b4lMxbKvixP2v1gfRu-SZQpRALdf7OISaLWEZTPAoBW4S5UxTjHbHyPpMbqPPxSzngnrfG3Kqss7qc1gybwZ2a_6xeku9nsmDpPkYhZ1FsEv2tGGu8mJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شروع‌رویایی‌پرسپولیس‌ِ تارتار در پیش فصل؛ پنج مسابقه، پنج‌پیروزی، پنج کلین‌شیت؛ امروز هم باشش گل تیم ترکیه‌ای ارزروم رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/27026" target="_blank">📅 00:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27025">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mes7OGWkTAMIN169w8KBJG_sh4houu5KyWO7pexV3zsVnD25Dhtm_IotW8iiNWpBT-4ci8TUT0x1g-mrrjC__v9fmFdmesykSow9GL3X3xlXXjZWLmip43UUJBN8MjHplBVJ-TfKTIkUF8QU5GRNWaGLOk6v6X_cGymsngeBkWgeFhtnD-Io7dmWt-QhwYqcEa4B0pERhR6JlT00tu4c5vmDmZ7kRcMJ0lJWEBO3Ow6O3dCxDHkXmk7iOvMunjuQQFFKdpQ34GNsXLL3vtzZaxcNwiezEfcvx4VGIojzfFYcuHRwU8FUalyJuFC1i0y9Mj-G-HSqZfdwjZQTjnYz-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
الهلال برای جذب رایان، استعداد ۱۹ ساله برزیلی باشگاه بورنموث و تیم‌ملی‌برزیل آماده آغاز مذاکرات شده و این انتقال را بعنوان جانشین احتمالی مالکوم دنبال‌میکند. رایان جوان یکی‌از استعدادهای آینده‌دار فوتبال برزیل به شمار میرود و درسال ۲۰۲۶ باانتقالی به ارزش ۳۵ میلیون یورو راهی تیم بورنموث شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/27025" target="_blank">📅 23:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27024">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrNzNh6bV3tJJcOW60H0j7U9q01LECRyOK85_LUZ1WU8MLoOCotjh1GKdtMu3MQaA2zzWTm9IUkiFHtPblVy-XbdLH6mJTGjSYy_69HDkKVtMSuOdulPw0N_s7v-BMaNeak9AxQ68UB9Lqeh4ZvIgHF0FG3BwzFFHmBZ5JHWOKUNTEuwCl9SBCue9vkw8yLsgEXKTETkuuYSCEIwyEc-i8_t-zt8tlj-phr8wDv0v2nE8ZD7rq5X2uqEt-PP0EBuYncR20XtuF5wvHSmrLIfwWbiSFQ-ng9TfvCbqUQX56QJLkVdgXiV8BDnCStPvn-r98N4Dq81b7_FsS3RQc8jIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ پیمان‌حدادی‌مدیرعامل‌پرسپولیس فردا بامدیریت باشگاه فولاد خوزستان جلسه خواهد داشت تا آخرین تلاش‌های خود را برای متقاعد کردن فولادی‌ها برای‌فروش ابوالفضل رزاق پور ستاره چپ پای این تیم به کار ببرد. گزینه دوم امیر جعفریه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/27024" target="_blank">📅 23:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27023">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGo9NwkkDziBUxWOOigOqedvpCTetYt1SPhSLAi7Sy1d_OtDEOB-_xLA6OFmq-aufafP6ig8wfIcGzKC5SqKU8M6DH0Xm_yIAdPK2mhIjMuDv_q5e4TeXD5gUXhkQDFrwzosk5tmhxfvBOyjmny0iqMmTpQUi4pybpkWT5LWDnYsxtJHrG5Uy-nQ0NurlY3tnQOlDIG8J5y8QkCLZk3k4mLaBefhw7gKpDBLA97lNABzhcuwYOBe0YYP6xB7lv5ztVdrpsw4Bukc4c_b23BsX3FYmPXqV2VNmcK6gZgdX4gjvbaTGQMFyvHmEQKMYgporijzk6X7xfOSHl32Ni4WPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ حمید مطهری به مدیریت باشگاه فولاد خوزستان اعلام با هییچ رقمی ابوالفضل رزاق پور رو به پرسپولیس نخواهد داد. مدیریت فولاد به پرسپولیسی‌هااعلام‌کرده بود اگه‌مطهری اوکی بدهد این‌بازیکن رو با دریافت 80 میلیارد بهتون میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/27023" target="_blank">📅 22:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27022">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMMKvOvdjzx80lvPNdW8CVDcDMz1ELu288W9WSclaAoTxdWoVe6H-sMn_FU77sjpGJVPmjeFffflNY1dno2gWSGYVedX5L-qKke_d7x6_Yii0JbH2sVIplGomTBR2iibL8NCb7oNEzfkMLUmDN6RQEJQl0sz0neWy2utXW_yga5tpR_6zotFanGoKTFBR2F1XSZBCjMFw8rkcF9KW6o-Aqw_yBakY6zBgtxp_eNbv465tkX3T2S9G8Q1LmFaZ2zOErVNSCm6DolBTIy_Y9MnkEKh3f2Oze9cc0SnuIu-sXlQV3EpnN6hvVQxto2labNI7wtNlGBje67Zap1p6TlNNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دادگاه‌عالی‌ورزش "CAS" روز سه‌شنبه پیش رورای نهایی‌خود را درخصوص‌پنجره نقل و انتقالاتی باشگاه استقلال خواهد داد. اگر رای مثبت باشد فیفا پنجره رو بازمیکنه. اگرهم رای منفی باشد این پنجره نیزبسته خواهد ماند و با شروع نقل و انتقالات نیم فصل پنجره آبی‌ها توسط…</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/27022" target="_blank">📅 22:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27021">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hi-IfJfrN77ghCOQbMKxdwoSqsd-h8TiZrsW9Ssi__f-9dbn5XZo6_NeBeg9Uxi1MnujX3N72B9Dsc2M_Rx__UC-dWljzMIHSDL3utsKpwzILWf5v6_BLMamDW-KL5N08L1KSPbMvEllea84qPhEPsjNfqbkjgjg-FqOPvteV3enYIKg68WIaqpmszeks-LG34jPHkgNxt_vtr5HSdW1SSdN7GgOtT0RcoeYVD8OBj8ZlZrkOJ25G40TYnlISSb2pjK68yzdTh0jXDzrEeHkJFk8DaPTpoq5rPiG-7i6akee83khSQKoa6PkHnD74llC-hJVE-8qvWl9RIgrwMn37A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
این‌روزهااینستاگرام رو باز میکنی، همه نفری یدونه‌مجلس‌عروسی‌واسه‌رونالدو و جورجینا گرفتن؛ ولی این یکی واقعا تمیز و زیبا بود. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/27021" target="_blank">📅 22:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27020">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjGulgGRZquHXDPRWDXxV-vMy9xOcXzfe4CFT6FgmPY7KXpK1OejKL1DDFowRGjpLXIkplUFMweVQP2_a1D4Gj5qKsyZ4EdDrnwEu5pYIrFTTqgBGp_TxyTBeez-cYIjSd8kutWJRDEqn2kqKF_X1kISWphvWdw3Ki5EzDk2Vjt35cgoakkm8UnVJDT5_sU85F-zER2qm_hHYIjdXuOY39Cb7SYt0lgszXcKWbo_zMez7I6CottSMxaDcGtTdGIpajLUXEKhPamY10WaDBXFT_JkRzgq0M6OzVj2OMK-15B-vUk75C8rlClsUIdFMoLQpEyoZVnb0PjAvmEd-GW6pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌رقم رضایت‌نامه یادگار رستمی وینگر 22 ساله خود را 50 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27020" target="_blank">📅 21:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27019">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=qP88JUVm2HEFcLuoUx6otWffHwSbFiP5udcLdCjK-5EDWAzWlDo9Qy0Rmftlyr4PIYzBh63MpuWrshZBCTnVigqbHXIQbh03yuxDCrqGt8MdkLi6Ykw66dK716lxkwTXSJdIDqhNnmuHjb2wdOpJqVtG4Ls_wEDaIOAtgxjrq1jmFYFyM40V2vEQ0yufjg0Ztb7_Q_JTBnI1V-No-uUwNUx-TDgOvC73AbN2W_Ab6uP_-Ix5WOqF_ORGaWUrpPgKIdtoB1GQO-ERtz8_-_vaRt3ycCfeQ7a6BTXVlkMtM7qbqaW83ywUQ7bXwRhVyOTuxE5zQ4fcSe-ffHRDwsrpKoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=qP88JUVm2HEFcLuoUx6otWffHwSbFiP5udcLdCjK-5EDWAzWlDo9Qy0Rmftlyr4PIYzBh63MpuWrshZBCTnVigqbHXIQbh03yuxDCrqGt8MdkLi6Ykw66dK716lxkwTXSJdIDqhNnmuHjb2wdOpJqVtG4Ls_wEDaIOAtgxjrq1jmFYFyM40V2vEQ0yufjg0Ztb7_Q_JTBnI1V-No-uUwNUx-TDgOvC73AbN2W_Ab6uP_-Ix5WOqF_ORGaWUrpPgKIdtoB1GQO-ERtz8_-_vaRt3ycCfeQ7a6BTXVlkMtM7qbqaW83ywUQ7bXwRhVyOTuxE5zQ4fcSe-ffHRDwsrpKoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
این‌روزهااینستاگرام رو باز میکنی، همه نفری یدونه‌مجلس‌عروسی‌واسه‌رونالدو و جورجینا گرفتن؛ ولی این یکی واقعا تمیز و زیبا بود. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27019" target="_blank">📅 21:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27018">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRML64vNqrdwk_xGQgEF6CQhv9oWzTsMjmk9xwYNmti65FtA4wpiK3PQjcnTX-WH3dkizz_ZVZkzXKMRhDBcvv-GVCIPxYKo1_Vq5SLpN9X8T6frO2JFjbjjxfqL96PLVTv6_sEeoBgj09PHL4vF_jDfRp7Z5LHLufYr3yFMNd-pjh5dSqvxHToEPkxlTBAR0svmLX-FPD6LCA97Sq2ydLXGS7lzT_d314wNN9wsUiBG1oNhhPM8uaNhf61APvTgbwkNSAZWph5Ldj4aqITmYwCkvWtp0lBn2IVqpL4GkwdGf7fB6yCzICvqMVtA8t1-NdhVaJjqqJMhbFAlUQT1NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه گل گهرسیرجان‌رقم‌رضایت‌نامه امیرجعفری مدافع چپ 24ساله‌این‌باشگاه رو 70 میلیارد تومان اعلام کرده است. مهدی تارتار بشدت دنبال جذب این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27018" target="_blank">📅 20:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27016">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nu2Hw68RqogfcpuztEdpHZ7B6kMoq1Bl8Jz660q_QQNTPbUR-wCcUWDi_BctUH0Um9FtwhjUKoC3mVe5HiVoJfWk27WxhtJWRIUOWVEPfv0K2u2tqik6N8HbrKD8puVUDgjcw-ASwwF5oi1xEZHCQg3M9zePYh_VsDBt9HvXE95kCbldtTjUIS8fpxbqiCHu1QIAtKH1OPyTKO6gR3vaCQ3clKgwWBz3GG-sI1t8GPRbaxadONuEGA90aei2W11VwI-4nXRKqSXde_0WQkVAsDUbSuVVsBM6fQB2eW9BLF3KGt2sC_fxTWpBYq_MTdbIwgrzH2Pmwv5FDblANRQ_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق صحبتی که با یکی از نزدیکان محمد جواد حسین‌نژاد داشتیم این‌بازیکن‌هم‌آمادگی خود را برای بازگشت به لیگ برتر اعلام کرده و به احتمال فراوان راهی یکی از دوتیم پرسپولیس یا استقلال میشود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27016" target="_blank">📅 20:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27015">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtnqiEvNMF0c5X7eslOduDPgGqj_R_1pX0MaO8qV_elNJ6jV069I5GWHcr2f-z_aQ2CkJXyoqBCK7YNnmEf7WV0QlU3KBUD7D5GjKq8LN7Hub-Q_Q2LfF5eqr7FQOqr6GhnxVpSSPDiD_n8S6-ipRaC41OxEy-FxrhN4iaIj3fXiHeWhVW7mm99G34oXkn0JubKxGakJFwfOrW3mf2Z4pP66fsFXl2S3_FIIzDKmzwRMonA_zaaYnS-ypWnyKG7YPic0VstxGNfuaBAqFBNmtqofOh37Qh5ebAn5Tn41xw20Kdrd1Z4Q7JxeYTK5b1sf6PXDjb0H4ovIcaXewlHi5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو درحال‌آماده‌سازی مراسم ازدواج با جورجینا رودریگز برای هفته آینده در مادیرا است. این‌دونفر در کلیسای جامع فونچال رسما ازدواج خواهند کرد و سپس جشن‌ها برای مراسم پذیرایی بسیار خفن به هتل پنج‌ ستاره و لوکس ساوی پالاس منتقل می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27015" target="_blank">📅 20:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27014">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-lrXivIsqZPFGKxIlb6qUQrn5kwcO1cNSfUk1ZkJbom7CuHlnQgHV0NTrQjT7x4aT6T_3liigQRPo0dyQaCt3xYkzItqTMxBhICChGEdR0aF1mGkLzBSQXpNdyIpsXsXREi32wpqjQrdtV9Ed73yOIy3XYIpLLkth7BfDI7S8EpX-CNt384ErxKC8ENOcgT722PuwW24tRUhaffXth8beFD7Sz6dFob1cYyNqgnaUU-iSJ5onNIfLjuS802nX4lOaDly0EyfL5vWalUk2Wat5fWOX1sNb-bau__YgcocPpQ0FNnNWGdKslGTuWMUfoh_2_IxDjyuMZ1pJnOpkiJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
ترکیب‌پرسپولیس برای دیدار دوستانه امروز ارزروم اسپور؛شاگردان‌تارتار فردا به‌تهران برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27014" target="_blank">📅 19:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27012">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5f5546ea.mp4?token=K4UMRLRL-C1BR9Y3Umzf7BNyUITxkGzC9fiAV0uS16Dkkk7uMDJjBzu6xKOGfNcWynDfY7oa99RLRt5NPlATPk2v_7d2C4ZX9UlKCiF5a9KloNEd7ybLj_v6uluSbeD0EHeFOJY7BqueqZi0ew6jpRlB2nr8QryBbEugSTNRTVG3nH8QaInn9e8W0Y5AtfHnHoMn22RETrTJj0f7SPUuHrmLN03ZxCw9z3KD5bGjA737fEuUXh1CK0NAejj4nSEIqGefNi6dRkdS27J4-ZjEaCS6MT67V8pH9Xmtk5XNUsIL1yKTdmUzcPyYUJsyacMxJjHxRtCqore__woNX34snQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5f5546ea.mp4?token=K4UMRLRL-C1BR9Y3Umzf7BNyUITxkGzC9fiAV0uS16Dkkk7uMDJjBzu6xKOGfNcWynDfY7oa99RLRt5NPlATPk2v_7d2C4ZX9UlKCiF5a9KloNEd7ybLj_v6uluSbeD0EHeFOJY7BqueqZi0ew6jpRlB2nr8QryBbEugSTNRTVG3nH8QaInn9e8W0Y5AtfHnHoMn22RETrTJj0f7SPUuHrmLN03ZxCw9z3KD5bGjA737fEuUXh1CK0NAejj4nSEIqGefNi6dRkdS27J4-ZjEaCS6MT67V8pH9Xmtk5XNUsIL1yKTdmUzcPyYUJsyacMxJjHxRtCqore__woNX34snQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عشق و حال مهدی قایدی ستاره ملی پوش النصر امارات با پسر کوچولوش میلانِ عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27012" target="_blank">📅 19:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27011">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJXBfn1CLg5xBsWn6hlEcc8sdTEV0sZmiX-XhQlWsyPim49hZ3RoQ5VdfAGwlMin-65Ci76fDc2RQLn_2FfbHFYOaykJ-FobIlmnmgFYVM9QhhhXijF7MN0Vx0hT321fps4HU1305HyB7Jw-mY5red8gyexF0hnYsL_bpmZjRRdAkKNIU2fXrZpGpTQ89v8XclKiJmLy2uVg8YE23K10Mmo-i_I6Q7KDNT-F1qf2vYoabXwtLe68KGoQczUnRf6Fglx74AJ8TonsWnUsczQRJCpvZM-AtMBJbU7v6uNqOo7PgKqUZ9tcY-tJ18WfwXh0fIhy6SyDJVvg_V6sKFJKdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ایجنت مهدی لیموچی ستاره 26 ساله سپاهان امروز باردیگربه‌پیمان‌حدادی اعلام کرده این بازیکن اماده‌عقدقرارداد باباشگاه پرسپولیس است و درصورتیکه‌سرخپوشان بتوانند رضایت نامه او رو از طلایی پوشان بگیرند لیموچی سرخپوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27011" target="_blank">📅 19:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27010">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeCMp1KmcGY8NcfIV_fK4F5u_r8401-Kk6xZpf_0_zj1FTl7knjKkf_ippvkS2HPHLHoV1_RVBY6o1cEYIS_Tcbf3Bg5Gy5Y42FMhVJYTeJztHzpMeLwDq-MvQe1FhZI_M873VaTlrP-xNdF42EghcpRktMM1apc7U8yKBiuzRcnSFxrHuXfW7lHT_Wdw1E3q1MDZ05JVh8FvuRXpf_pYRrpGyDxptgS1qUHazMxeEGEM634WXdvpZbjqstFd2U7kxrXYSFhlx44EVJyMLEchu758OC2UYScztp9thP_-wrIqACjSO2go-CkSgG94bvOaEYICKUjCB-QRnuibi0QiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مریم ایراندوست سرمربی‌ سابق‌تیم‌بانوان ملوان عصر امروز با قرار دادی دو ساله سرمربی تیم بانوان استقلال‌شد حالا زهرا قنبری کاپیتان تیم پرسپولیس به مریم ایران دوست بابت سرمربی شدن تیم بانوان استقلال تبریک گفته و گفته خوش برگشتید انشالله فصل خوبی در باشگاه استقلال…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27010" target="_blank">📅 18:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27009">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tP1BeqBaOZi4K38FRHenY_tVHHseW6PKJS73Yd4mUB3O_gIBnAH3pCJHG5C6Y6dnuEbfTRuRTZPPmi3D8z5i2lWs2cAhkRh_aSKM-QcmU_2MbYYMFYecErjTrtUbwWWJoypvCz4xPVoVeEySyHRGYbuTYLzjCIj9Fk_Nmg49_Jqu-vd5uImnQi7FogNiI8XovghDmv7DpJahOCm01iCE52bVLgHxkOIRuiEzC7n5ovcnxiYs0J_51JKQuUo2aIFGMkTKiUc8hPGivYAKz-COr4JHHbwm18Y7QWroddg-LXldmLZ2qBvxVZEnpFnsOe7Js97Q2WtRUUETao_NPgMoIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
ترکیب‌پرسپولیس برای دیدار دوستانه امروز ارزروم اسپور؛شاگردان‌تارتار فردا به‌تهران برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27009" target="_blank">📅 18:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27008">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
در فینال مسابقات لیگ ملت‌های والیبال لهستان تویه‌بازی‌سخت و نفسگیر موفق شد آمریکا رو 3_2 شکست بده و مجددا قهرمان این رقابت‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27008" target="_blank">📅 17:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27007">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7il336NRPpXbyHYYBpkWOJz2FB0RUzPyF50hQo-fyNlgHYX9qUZftBarh6tHhYQBq2vERuWP-Ne2abCYWcqyxgtvGXd3TuspKHT_NgmhDF9NENelFXTeX9uILUmUW1W3VRg2H30ubvqsqhivbCLeQ2qpjKDfKwrprAcx03PwkTrnbfjNH_uZSmt9NG2vkZkBH14Bs6E5gloLGQDLFUIEwuzbkzYFo3XbGeZzwf-xdPlc1rlEaGkqlbXnER-10x1hE3MnZz5sjekcuXh4oPAlptVmAMePyvWyQDKdJx39UiRkzPPZyRs6wo0TDHc8Zlu5YhsIuCwztLyy5QzPcz-KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رده‌بندی‌لیگ‌ملتهای والیبال؛ اسلوونی با شکست ژاپن به مقام‌سوم رسید. تیم ملی والیبال اسلوونی با پیروزی برابرژاپن دردیدار رده‌بندی‌لیگ ملت‌ها 2026 به مقام‌سومی و مدال برنز این مسابقات دست یافت تابرای نخستین بار روی سکوی این رقابت‌ها برود.
🏐
ژاپن
1️⃣
-
3️⃣
اسلوونی…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27007" target="_blank">📅 17:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27006">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40435b41c.mp4?token=aTMEICLJtDH9DFbAvBCrRwQY6yFuoUkar3RM6LsZM3fYtF_bEwVaxG8eUuhAA92lfY8s5_0jD3xTVLtCd3yOASl1oho6sN08LDWUrDdVzyI4SuRFDQ-k5ISKB9VOwYAMYsFRGrCtz5Pd0OIFMW6Qh6qKeiXzTdK21Z9uqoPKLHDrIaWP-VLa9iEOffkqKEiSgznKpaaQQCZ0mJv3gtH050rUFTvZJPtxEdwIrR7ckEbJudA-HB7cFUlZuIbS6uIp2A6tFfzDVBHmeCv2xjWG6SrX1PbXnh_lYhXRQPN8v1dyi_3Y-Iwsm3Fv63hQBOKnThrtlzHHyrj7VuC7c88lpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40435b41c.mp4?token=aTMEICLJtDH9DFbAvBCrRwQY6yFuoUkar3RM6LsZM3fYtF_bEwVaxG8eUuhAA92lfY8s5_0jD3xTVLtCd3yOASl1oho6sN08LDWUrDdVzyI4SuRFDQ-k5ISKB9VOwYAMYsFRGrCtz5Pd0OIFMW6Qh6qKeiXzTdK21Z9uqoPKLHDrIaWP-VLa9iEOffkqKEiSgznKpaaQQCZ0mJv3gtH050rUFTvZJPtxEdwIrR7ckEbJudA-HB7cFUlZuIbS6uIp2A6tFfzDVBHmeCv2xjWG6SrX1PbXnh_lYhXRQPN8v1dyi_3Y-Iwsm3Fv63hQBOKnThrtlzHHyrj7VuC7c88lpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه 3 بازی دوستانه‌امروز رقابت‌های باشگاهی؛ پیروزی اینترمیلان و دورتموند و شکست چلسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27006" target="_blank">📅 17:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27005">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWMqrd7NjMuoNTynUp7lxBNWN7HwdAU2OPamPfZJyjBOreBKXOoVqcu_YmvvbwF5VHvkFbnn6CXtCrXuxApc-QPb6SHLh-vWZAMPxo79bhPJ1aY3C4JKIcUee5297DPvofAUxaj5N5vfQWtVyap6MGoA0OJwEtLWsrkXYiKMDY5qNlQFpEDOYbZdIp3n-cJmrNTM0o09fz9QZDxhbDOUy9mRGlFWru_FXjCJoJ3VTYw6UZdp1aCIAOHp0XGnHVaTtzJmvOcWbSg9qvSihH6kbqHlmUlIL6kgHaBYikIAeEDbCJzA6tY3FtSynSgojgLUJacfbxPBH7q55ZSsMkZEhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27005" target="_blank">📅 17:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27004">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suQ3-q0Qx8xJ0qBMWZUzTPjQkXBe_XT1pPtS2buayryq9YbJnWcCDj3oPq6jiObc4F_hS-e_5j38te8aO-Rg9GrJWQ-obDjY6VWXoq8pi0OpRpSELcp9jPSwm-LaNGy5xUUu7cP1seL-iXv2LraQAzqlo7U25MZBE6bcsMVBtPEVx2DMMFImw2DYdkELL8TxtLaTwU2vfUPUr6gyRajHHRvuepXKtWsjx-PA3X4vBf3lIQA8vKyC09zh_sU5aq7uejH7l5tB-3gXM8Sfx0iLTSWyjUylTszp6e7LZhE_7XV_7Wk04oPzEqr0D9rnPmx4IhpwcFC7u9jXGl9t2qD1WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛ با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27004" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27003">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gb60syzutHYf_LIFRRNfrYosUkQMjUOdGygNQzooXjJjSwtk_z-HLetduX9SwcYHQS7_yFmhrtGY63oSZf_twGgvrmkzC-CLmpD4Op4NgOrL-ecDummP4zT98HWtMV7cvO6qPg7wBy8lclZMKGGLPD1SEtHEuH8NpFyGAzL7jYviPE-2t97U4Qd538ej9J_ymFJep-FM-1yIPwAoFSs-FiuZ7260u7q3ST6xUROwEUwpUCJc7-Ro-eBIyAeX0k_RVX7G3ZYR9eSgLo92XUCPmaie_-wyEOPKAX4Kpt-YtRwoGTXCziNtRRD_99aLJ6ioPN4a8-V99EdOCZl-TdwBVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ سید مهدی رحمتی سرمربی‌گلگهر ساعتی قبل در تماس با مهدی گودرزی شاگرد سابق خود در خیبر به او اعلام کرده که پنجره باشگاه استقلال باز نخواهد شد و قید عقد قرارداد با استقلال رو بزند و راهی تیم گل گهر شود.
‼️
رحمتی پیش‌تر نیز مانع حضور…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27003" target="_blank">📅 16:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27002">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlmPw9jeHSLC-WcaYBm19hmevwkjdXY8qkGX_Y3i9o-HL6vPXBBHHVxGi7sLHXuzUK9vzK8qQbbXGdHiXbZoK4Y9aZYy3gfk-RdycjzUgMjzRpnqZUGuO-UZa9IiBQ0MBPnT6fwgoDqrq2X64KpQmMMhUZ8rBzjagxHuunBMcUMMLDJ8YJd8tTDBZApJcukDOsWCZ1GyM3DzW1t_NlixHZgPgZY0rz6oUpADsxOiXs-jHbMIGHtDldO4UTvsygWLTzdG9_59pOTM8Kxn-Cm7Hdghr0f0blAaw6m4KTcasp1Mde2OeIDQJQ6QCefdzUpFXuutr0lM0lIaOaINoyxmgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💰
گران‌قیمت‌ترین بازیکنان در فوتبال زنان
🥇
آلیسیا روسو - آرسنال ۱,۸۰۰,۰۰۰ یورو
🥈
خدیجه شاو - سیتی ۱,۳۰۰,۰۰۰ یورو
🥉
الکسیا پوتیاس - لندن سیتی ۱,۱۵۰,۰۰۰ یورو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27002" target="_blank">📅 15:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27001">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTDNcPC55xa3RzZtmDxAyxZgOf9hX_Srpv_JVKpiLg-WGp-FJSN7IFVDTr8ZWt-16mVrOFjlIZvEZpMhTmGtOCw6OP85sGbx9w2HTiZ0C3JHXf2ajapcdTMgHjUzATglpGUNpFFrgi8z3XAykGKralLsDpIEz91CRW95ADdQZW5evVI8zhUE65uDKOQeKMftiNo-pvl9ZupXgjnMNv0AjmhF2t1Nj-ubx0ugeT2o5Vwg2yNK7avePlzO3C9UxbkA8bXy8JA7XQ7RzexnzLCYCwzhEIKvkqsh2nnx5stNbwQD9kQzzfrJtUN62MQJ1lHQXGPI-mm5wskp9m10k7jt-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27001" target="_blank">📅 14:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27000">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lp9nLHpIPhYJxCh5Bj9mvGk6ELrofafm1cq-vbbGTE01k3i5B1fGidTN2pc9vxqqEQmvhS28r-lDodMgso8xHGP3cFgQPM5PrJgvNKTZeJuim4QsKen14u0gZn3GV4CehRNSlXyrP40mqRxvZAul9i0WMmpq_XutU8kPjs84_4WcWKgQe9kSWlXbM7DMrI9wCZAOEIdCeJEZelxr9tt_9ItbiGm29ptSbZda12iFLG0R1qB4_UduA8OTHsEga-xVp8N4J7TIVoyCfVgi5W24uO0X4JNy7dz-huDTKaRKBuUaYeC-gCJbV8NRawgO3Yn5ZqMubLy7TgaJzxCd1h2TzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇱
دبل دیدنی لواندوفسکی مهاجم 37 ساله جدید شیکاگو فایر دربازی بامداد امروز این تیم در MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27000" target="_blank">📅 14:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26998">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CPywgJl4AXlkBKlO9vCsKscbGDP1Xj-SQlZuyhnjSmtx8r1pdfkdUyn6tTWrLhn839BR495fT9b_-PqLrO1yN9WDnFpqp0ZrSd3tbWSViE6dvqus327bj_nBsMlmya2kUOdZQQ7R3U_IkyYyJT0zUprmrtxMzFvhPZF8AfoJoxcZ1_Ccj4COujImkbGwzqF_4Lm_5WtetSQhneexraSaArlquEpifp56BTTfIoUHpKyLUnKQ1ucqxY2B8zJNLnEYupTW5hX33qfjddcBUeKh47zHAhAAD6zW6HS64CJKA7vsy08_H-FpBzQLaCmNASpbjWywnCl6j6Xg2_IRBopppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mCaFHizyCYbDyB7059VA0AS6eoxVTVb2fHJfM4CXVLg6_eE9rfHMg7YKa9WGGOGeZgMxDm6CzcDHGIQmz5fz5Ltse-HY6hPxbTQA8kIEEflBfXuaPppOO6asrJmjYZU2EuXv6ne3OYeAW4eyiyQUWyuM97V5W87Ec9T3iGayGaLhTFti7ir7ZrDStCYrbQBzu2xtLWYM9hBw4GooxFmUlcaQXUIfbZN70_DDAsNZ7C8umoLt60fV9mri0InWWGb9ZAoMbAlmylIrfUGx1nL7gJdMXFt6FHFyZ40am4DJS6GeEVAW5rcyJmuQsCELKUv0CmXWPPMR7teCuEHPvxU-hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
کریس رونالدو و جورجینا میخوان‌؛ مراسم عروسی خود را بعد از مسابقات جام جهانی در جزایر مادیرا در شمال اقیانوس اطلس بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26998" target="_blank">📅 14:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26997">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDjI2zW1drL50oMAt12zluMJsnpT61iV3j8KLAwZ6RhiAChPCldC_AABKU0c9dYxTCwJ3JuBVPpEfS2UlvRaQZELsVrZ5cyq7Fmvh_UC0-tcYaALitj3kUFNTBdajP5yNH7jr7C6SqC1SYncokVGkK6ShEDKgrsenPRb5ZKN0Gq-sKHAi6rzodu2D93Yo4Qxc_F8bFW3R8rTHFIH_aNUj-USbxYSFFDLqA-S47xfwJpgZPIiQjRW2bu19khnHJ-IPZmIzoKzxSiyh0_LtN0RhnbUhEpJch37Nc7LpICJ43ll92vVIJNx61EyJq2a3r-n7K3h7i1_DiaBD63uhsjp1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اینم از توضیحات کوکوریا: خیلیا بخاطر مدل موهام منو مسخره میکنن اما دلیل بلند بودن موهام پسرمه که اوتیسم داره، این تنها راهیه که میتونه باباشو از بین بازیکنای دیگه تشخیص بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26997" target="_blank">📅 13:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26996">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QP8RKHHMHs4iwx5G59ANnqYE6lbIwos2f5mLf9C12i_-Ni4dZBMr7UPIlpPkNlBFKUaCwUiPVwc1a_j-An67RqjZt5un8u-NMgVMEYKxsPcflCwLB8fc2ELOIAD1QlxfYOB84m7Z2FhCU0qNRqhNU3lclfJ-0wWbtEPEow0midPIwGvRVfbUQZ-y15uWltRkrjebE0Dnww99OqNiij_G4pz9Y6Kgpu5Gcv6-R0vMYMHZNtojH2yLpPNrLd2BIiOv3XsoeyvyoQP9meV00QOCFFjC13Egf6eqVu5pWZHxkYVlntBLFGpWRgpHGc4oXAxDwpgqPh3mfkB1duaVzmLq_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرویس‌نیشیموتو بازیکن تیم‌ملی‌والیبال ژاپن که باعث خنده خود او شد؛ یه لحظه تعادلش رو از دست داد. بازی فینال هم ساعت 15:00 شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26996" target="_blank">📅 13:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26995">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71a95e55dc.mp4?token=VCwxrZtqkn_aCeGzsFDVMOiQkMpWWItU7KUGLuOfxK6UV68CA_fii18rqfDeBTgwFC-_OO2zHyKF7sTopwLuF-ZCkDa4qVhTbpVEfy2iruzo3zYgjZqjcCuctveyNc1KTBsV40IosFSomrqU8bxCHbfB9_fEuKuencp9fcpetvaEidSSUhMrq3Ggui_gMAANKSuHZOy4Ssqaw50nk6-kZGT7S-aYNysoGfXci5pEB01wHG_pO-3aome_DrMjkGmcmzaFfVNfj2UyXKLCYsw2647uB59_0U5CZrTgG-0nDJMYq3hyyFOsOiMWiZVVUcO_RFyq-Y7ehQuwnUm2oCaVkRf8NeJWUMxQlYJTNqr9idb0nrIA6vqePMksljdPP_dGjkLXLDcz4QWmrUarVQ2wYS9keNo0QeTG260sizeHTDYhxBJat9UG8qx0sExHrwWkDfNH0Mx77AyWJAGTggs7e6EUcX3pN5OX9KGdCa6LCw6mfVjseICqgQrI0j8EnIs6uDH9hPxLpiI-hGHR2XNcmjyVuYdgQQ5_yGF205U1HpGRhuS_4tlvBabWnq_WWzdibp-eTny-XKI5Sm7mRIVtxGmDkRvVmSGrA-hDnbR_EgWi3GODg_12zEwNOpzWXCU8aYJ8lZb3goXwRH7szxZdSFAmX9Ol3-T-da5sXm_lmCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71a95e55dc.mp4?token=VCwxrZtqkn_aCeGzsFDVMOiQkMpWWItU7KUGLuOfxK6UV68CA_fii18rqfDeBTgwFC-_OO2zHyKF7sTopwLuF-ZCkDa4qVhTbpVEfy2iruzo3zYgjZqjcCuctveyNc1KTBsV40IosFSomrqU8bxCHbfB9_fEuKuencp9fcpetvaEidSSUhMrq3Ggui_gMAANKSuHZOy4Ssqaw50nk6-kZGT7S-aYNysoGfXci5pEB01wHG_pO-3aome_DrMjkGmcmzaFfVNfj2UyXKLCYsw2647uB59_0U5CZrTgG-0nDJMYq3hyyFOsOiMWiZVVUcO_RFyq-Y7ehQuwnUm2oCaVkRf8NeJWUMxQlYJTNqr9idb0nrIA6vqePMksljdPP_dGjkLXLDcz4QWmrUarVQ2wYS9keNo0QeTG260sizeHTDYhxBJat9UG8qx0sExHrwWkDfNH0Mx77AyWJAGTggs7e6EUcX3pN5OX9KGdCa6LCw6mfVjseICqgQrI0j8EnIs6uDH9hPxLpiI-hGHR2XNcmjyVuYdgQQ5_yGF205U1HpGRhuS_4tlvBabWnq_WWzdibp-eTny-XKI5Sm7mRIVtxGmDkRvVmSGrA-hDnbR_EgWi3GODg_12zEwNOpzWXCU8aYJ8lZb3goXwRH7szxZdSFAmX9Ol3-T-da5sXm_lmCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
۱۲ سال پیش در چنین روزی
؛ منچستر یونایتد و رئال‌مادرید درمیشیگان به مصاف‌هم رفتند که ۱۰۹,۳۱۸ تماشاگرشاهد این بازی بودند. این‌بازی هم چنان رکورددار بیشترین تماشاگر در طول تاریخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26995" target="_blank">📅 13:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26994">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e3f4f0e8.mp4?token=LQiuCHNvb2RBVqioEPOVBcKtprV5SGkgdKEGTiEaPK6nfbyxeDT6OZ3jipIp0GktgUCQH9FA9vfjOp3CW8WX8gJ83c_viAThj7OcKjwMz88Y-qq_sJaKKcPQrP5MhmJqfkKqBqTqgnvLma71LM9O6ugm_lvYE1ozHo6HSFUIYRrPi2ke896bv2dFadTzi-UUCrOg8tEBNQMkqSyHGVgJLm5STvTsGUWWrJrKO1Ld6jwKNLfw2mQLApiTlt_u9DPPRo78vFHQfq_BCZWsSzrlEaiePWabcq6D-gJGu1a8U8LkTxLjUELhiZEpmawdnGYb9PFeX-MBCiKPmpvCufTC0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e3f4f0e8.mp4?token=LQiuCHNvb2RBVqioEPOVBcKtprV5SGkgdKEGTiEaPK6nfbyxeDT6OZ3jipIp0GktgUCQH9FA9vfjOp3CW8WX8gJ83c_viAThj7OcKjwMz88Y-qq_sJaKKcPQrP5MhmJqfkKqBqTqgnvLma71LM9O6ugm_lvYE1ozHo6HSFUIYRrPi2ke896bv2dFadTzi-UUCrOg8tEBNQMkqSyHGVgJLm5STvTsGUWWrJrKO1Ld6jwKNLfw2mQLApiTlt_u9DPPRo78vFHQfq_BCZWsSzrlEaiePWabcq6D-gJGu1a8U8LkTxLjUELhiZEpmawdnGYb9PFeX-MBCiKPmpvCufTC0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
رسانه‌های‌ مراکشی: منیر الحدادی تاکنون دو آفر باشگاه‌های مراکشی، دو آفر باشگاه‌ های برزیلی و یک آفر باشگاه‌ های قطری رو به‌ دلیل پایین بودن رقم قرار دادش رد کرده است. بالاترین دستمزد رو باشگاه استقلال ایران به او میداد که فعلا راضی به بازگشت به ایران به…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26994" target="_blank">📅 13:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26993">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XezlMsPINut5WgkCLkPQ21uOOBdiQancF1TGyrCR0n2-HC2opYEFlW1aK7WunI7nPBVM3seBcOej1D-OzH3d9CLrI6MQdCMy5Rw0kM6hzhQPP-v1sYl16c1iiCZHAfoybDfOMoOH3CTiZz4V8iwVy4Yrq4ys-dy3llsakbWCoMSUGcmXbww52Mur5TMYzIZtUSrKNdCES2mXiPpl5A2wXaS_Gtare5jtwrBvmjuh6UFr6LXkH08uBRFGJeYBpmUqvLnzEH-azIjn5MgyO4jy2XBFZ23WT2SGDKS3mXSUQER9hnbAhtb9oMvSKgYmGrYieW7B8MY6yIBfJZ-aP98EUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
دوران اسپانسرهای شرط‌بندی روی سینه پیراهن‌ های لیگ برتر انگلیس به پایان رسید. از فصل جدید، تیم‌های لیگ‌برتردیگر اجازه ندارند لوگوی شرکت‌های شرط‌ بندی را روی جلوی پیراهن مسابقه درج کنند. این‌قانون‌فقط شامل اسپانسرهای روی سینه است و سایر همکاری‌های تجاری همچنان مجاز خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26993" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26992">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSUfSfYiRhSKt_6xThMTXAKEsSGuUfqmztwD6lMK6gGzjE-LD9NxMgNVLgjPLkr0f2uu4cLSx8LUI3cgkSW_xoklyN1RScL92s6oXluGb4DQv77sRiGvKHwAUGDSSTJV-6yzCuvZ0u6x2ViETDsa_Q7I5cAaayrrDLk71GX4Pi-8YkXMMSsjdtmpKd3RBe6TYks_Frs_ttltjKyh8MJx6SN9iWvx1S3uOOY7tN1VQqrhs_ac7DVUR1v1pA2wj0AUTnG_27S7sgPGgK1w7Pzyez_Ck_GiFWDoa3kSYJt1zIeediNWaKEGiCN2KCreDFSVdRULEi_qOnyfk08ZFpUKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔵
#تکمیلی؛بااعلام‌رسانه‌های اسپانیایی؛ فران تورس بزودی قراردادش رو با بارسا فسخ خواهد کرد و با عقد قراردادی چهار ساله راهی PSG میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26992" target="_blank">📅 12:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26991">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKuZwRjc89gCgwm_HK47ecVqg498Z-9UeUWrCckfhJ0QV8gnCnSnGG8MhN4911ievxw9z--ziu-GRvzlJtZoITQBju4KMUhcfRxcZ3NJT7qDH4kN7E5zst6Aw51JOwdMiu05oDOPir7ASIVByWiV7-jGamwO_TgUz_PH8F2Hj4usQcbcpxrwhJQ7KdcNBX7AtiFXBdincZ3TD03Zh_f_0VxwnUc-UEm3My0cv0ZoLsnYrYtuOIwV_wrnaD3pbjE38Q2GgayO83yp0M4Avg3hmHCblAyoS-T5BEIyObgVeemG35v4BXs5Jz_ECnSxdhl7jUS0DmsqSzbgRvnzkivxgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26991" target="_blank">📅 12:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26990">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdofmu1Tnu4tS1-2gStyKLk78GlRF7zTILJRg-_2vEbzYcnhbuZJTdyV20zRSNaRUUIxGMXxGa9ZWH9hudVBISDdlmIxGuEPtqMFZorPMlAC_0qgfNQm-Xhdy26GxZA7RUn6IivjHhTPLFSGTGa6MvRk_f9Kol4YOWX5lu-S_T3v0XKMiRzsjbpvNlo4on1SQZzoNA6D3hQJcDaKM3iB8IgH9MMYWxZ7GvIVq8G5y7iRA1xZydCSn4iddOw8igWAJPJXEUkYAr1vGrQGsXOo5CLiqOumzBSm6vLBzxTacrLt6MTJLAU-8W3npR_ZGIuZftxpMSlKRD_8FtG9Fu3t2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیج بارسا اومده صحنه سجده حمزه عبدالکریم بعد گلش‌رو استوری کرده و دقیقا تو همون استوری تبلیغات یه‌برند مشروبات الکلی رو هم انجام داده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26990" target="_blank">📅 12:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26989">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f58235729a.mp4?token=n_oHd7JeKOKIwaf1_KzhWHubmVePKkYBuKSDmlHRt2o3D8_rZvMLj28BOratuSdWTiuct_Bq-SKdIK5IE7aqFZXwTG7mJfDAFQdiRLuTjiuttt0yBrjPsXL76ZqTxLBeCKe4LpUqsT9qDaZrUxcHsRH5NWmRGIbKZcqXbdOXqutGMEfuelHY1uSGFw2szAcIvdlYcOZInIuG_K8WcghbwSdnp32g8JvySup9ZfOGPWj2W_WgQTZmWHIA0EKAyXDlOQv_Xc__Hk9CbnInrTM_ZASjzlt1O4rMlkgoNXz8375iMZjD8xfLQ_AEQEjO2slvLu0_yk7mLY9bFFYTUDEHDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f58235729a.mp4?token=n_oHd7JeKOKIwaf1_KzhWHubmVePKkYBuKSDmlHRt2o3D8_rZvMLj28BOratuSdWTiuct_Bq-SKdIK5IE7aqFZXwTG7mJfDAFQdiRLuTjiuttt0yBrjPsXL76ZqTxLBeCKe4LpUqsT9qDaZrUxcHsRH5NWmRGIbKZcqXbdOXqutGMEfuelHY1uSGFw2szAcIvdlYcOZInIuG_K8WcghbwSdnp32g8JvySup9ZfOGPWj2W_WgQTZmWHIA0EKAyXDlOQv_Xc__Hk9CbnInrTM_ZASjzlt1O4rMlkgoNXz8375iMZjD8xfLQ_AEQEjO2slvLu0_yk7mLY9bFFYTUDEHDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس باردیگر در تماس تلفنی به مدیریت باشگاه اعلام کرده نیازی به حضور تیوی بیفوما و دنیل گرا ندارد و این دو بازیکن رو در لیست مازاد سرخ‌ها قرار داده. اورونوف، سرگیف و باکیچ 3 خارجیکه تارتار سبک‌بازیشون رو پذیرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26989" target="_blank">📅 12:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26987">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436452afaf.mp4?token=ZiCbsiJcPUBqMhzAJeazdiv9mw9a9R6N2wTSHap2XxhmZwXiRjxRRQhIWKTepfxcfcPX6StAvxMgoN1eNkbuA5eG6NjDVJ1jeKFexj_ba3zDRwzbrK1I70ybXO0zGuPNXFB0QO_6lctjzZ85IJft8IUOqPHAZQvj4_SljjYSEta9DK8pfPSQMrIMATCgRv7rakU20LhV76-7yEG1_z-nyKfOckkop65-dPdowhgcbYy6pPgEZUzS1dSZ39xkg7s7B-96FGN6tSz_lD99DxT2_rvTMeF20Jjj463BDZrSsykp-68Q0ILugQHFmmMIiDg0EE3ERmbm1b2NqCO8oxqang" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436452afaf.mp4?token=ZiCbsiJcPUBqMhzAJeazdiv9mw9a9R6N2wTSHap2XxhmZwXiRjxRRQhIWKTepfxcfcPX6StAvxMgoN1eNkbuA5eG6NjDVJ1jeKFexj_ba3zDRwzbrK1I70ybXO0zGuPNXFB0QO_6lctjzZ85IJft8IUOqPHAZQvj4_SljjYSEta9DK8pfPSQMrIMATCgRv7rakU20LhV76-7yEG1_z-nyKfOckkop65-dPdowhgcbYy6pPgEZUzS1dSZ39xkg7s7B-96FGN6tSz_lD99DxT2_rvTMeF20Jjj463BDZrSsykp-68Q0ILugQHFmmMIiDg0EE3ERmbm1b2NqCO8oxqang" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
برنامه بازی فینال و رده بندی لیگ ملتای والیبال؛ فردا ساعت 15:00 مسابقه فینال برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26987" target="_blank">📅 11:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26986">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9LbR0P1OExvy4EXKKPWFnimUZMt4s4yb4o4A0R37Zu47ExWkWHVbcIr38YtED-01uZTaWQGABzoNaZ-9tkPY8Ti3YswuXV_smz1Zc_l4VsLpsdMzqLclJxGnffK9H5RrjwYEZxouw9Dk96bOtOmYR5dBJaV4xr-agUcugovPrd2_3F5fU27667a9mbK-cac6-QCvBEgHmZAWafekQdPBx4yjymQWgZ1-J6AnVQ5NcUEwIU68itFfQwxETY-L0KBUS5LRBDIUZe-iAfacl34751dJUAc-oZSnX1xAflwrijtaVRhMhwN2trSGog6Q7NUeemLqsIdSZMXvSbLgBT_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوری از دیوید اورنشتاین: وینیسیوس در حال تصمیم‌گیری برای خروج‌رایگان در ۲۰۲۷ یا پیوستن به آرسنال درهمین‌تابستان است. آرسنال تمام منابع مالی رافراهم کرده و بازیکن به این ایده علاقه نشان داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26986" target="_blank">📅 11:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26985">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZ3EfO6TyY8da0zjuFEnH1cQsG8pJZEpqulFHLW1NoN7-FZqNKQ2i6lKBRmHDTnrJsAEm0XiknX-VelLbA4ykcQztEW4qmBUyJsK9re1b5DtJbWVpCMH9dFZ0_tLF8iEkNiHTp3BkcMuqWWtH6t7r_bynz6t0N5KXHEJ-Frge9NejajcC9vKeFypivdFHBqh44zKxF6ttCCh04o11iCDE_BoNJITEl6eFnmV-TtoSIb10v2J89IglOpsYHdwYOe2NHlvaQJ9Onc6IbIiRvir0V_9E2ThAhxWqMLIHq-lp31IHAICt_4GAPbVssXzfp39LZcxC0OhmI2YFk4yoSIYTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیر برنامه‌ های داکنز نازون: قرارداد نازون با‌تیم‌استقلال درفیفا فسخ‌نشده و باشگاه بخواهد این بازیکن به تمرینات تیم استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26985" target="_blank">📅 11:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26984">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12920f454e.mp4?token=ixsfrHmPJUIELMc6tnmi_G4mYurmZLFu_mv6nUyYP5-xjA3zn0SaZIcYHs5IOjuTPLv9_pq2ctKtRorp2I2u3flUIOyeALsIjNyzbE2-WBeDr377MTtxi3e2mV9XwarVEB2oAu3D-Uayuyut5Bhm7ME5h7LKP9PtxNfCzumkA3ubpEmIYJ9hApO5y5jAbhjRiI7v1iWU3c6F8qXvJ9GXZWYoM1sLKHRWCqkCriJSQ6pqnLkc3SQ1_0nWYfTpWiNcuxHMUz9O0RbT2q_yFm8i-0yg_3B4nBXwosbrPv1h9lVOlV1ydwY-SmT0ZRAf84mcKjjVoX9ACVutrlp1r-RsZGgm1iSLoMEn3wkvOC0FzynozBu1hJNCVO4rEyCOiVymB-Az8jn5EP0-qOn72LN1Wi_n0YTeu46UBFgTyFQNtY-MeI-tyb35ePN3IR6Th97xchyrHfmoVWFgnGwdrolJ0M4gj-v0tTS_7Jjjae3dGw1e5viy6aalzF9dlqpzFAiBP4A1fDCFDLyFow01zgmHqD-SxQFj-GAZtcq8RaO9GaqXKoA5tlZQ0vcZZcvG4ljRZFAltlsLtfEFqbEeUsP-HJ74OOH31UeFJbKjjAty5i4SFKVNlQsxPwfAWHSIX957BLVT1Ybx_HrClsfYniaPDy5aKcmvpjlMD1QJE7TlWgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12920f454e.mp4?token=ixsfrHmPJUIELMc6tnmi_G4mYurmZLFu_mv6nUyYP5-xjA3zn0SaZIcYHs5IOjuTPLv9_pq2ctKtRorp2I2u3flUIOyeALsIjNyzbE2-WBeDr377MTtxi3e2mV9XwarVEB2oAu3D-Uayuyut5Bhm7ME5h7LKP9PtxNfCzumkA3ubpEmIYJ9hApO5y5jAbhjRiI7v1iWU3c6F8qXvJ9GXZWYoM1sLKHRWCqkCriJSQ6pqnLkc3SQ1_0nWYfTpWiNcuxHMUz9O0RbT2q_yFm8i-0yg_3B4nBXwosbrPv1h9lVOlV1ydwY-SmT0ZRAf84mcKjjVoX9ACVutrlp1r-RsZGgm1iSLoMEn3wkvOC0FzynozBu1hJNCVO4rEyCOiVymB-Az8jn5EP0-qOn72LN1Wi_n0YTeu46UBFgTyFQNtY-MeI-tyb35ePN3IR6Th97xchyrHfmoVWFgnGwdrolJ0M4gj-v0tTS_7Jjjae3dGw1e5viy6aalzF9dlqpzFAiBP4A1fDCFDLyFow01zgmHqD-SxQFj-GAZtcq8RaO9GaqXKoA5tlZQ0vcZZcvG4ljRZFAltlsLtfEFqbEeUsP-HJ74OOH31UeFJbKjjAty5i4SFKVNlQsxPwfAWHSIX957BLVT1Ybx_HrClsfYniaPDy5aKcmvpjlMD1QJE7TlWgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇱
دبل دیدنی لواندوفسکی مهاجم 37 ساله جدید شیکاگو فایر دربازی بامداد امروز این تیم در MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26984" target="_blank">📅 11:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26983">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fdd524d5.mp4?token=Zggm6QbOIBHgocokerjK_4B9vAUIHHi5Hj0TIFGZAmm0f74hTs6v39gjmJTSLXU_TICC1yQksvSAGk5sdTas0sQZZRmGaSu-bzS8rKAvLUSFa8eCCGJ5dXg98K0klGD54nwX8_9hgf3PlkQInTSoUdeFwgUeOFIhF9kBD1_nGqRbNd0NcnVzGRI7QN27h37k2lsTuOPYQceqT9iE-5DrGpt6lMBHDapmAVEvpoSWW2LJQdRC2tIr1ZRi5QA-L6ZNT0qsJqHNY-7CApvWfxftWTpH2P3G-8I7veJxI6B3hePv2BWTwOHAxpAihoPsRTxtI8DYdto_BqGxJIJAVeHgnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fdd524d5.mp4?token=Zggm6QbOIBHgocokerjK_4B9vAUIHHi5Hj0TIFGZAmm0f74hTs6v39gjmJTSLXU_TICC1yQksvSAGk5sdTas0sQZZRmGaSu-bzS8rKAvLUSFa8eCCGJ5dXg98K0klGD54nwX8_9hgf3PlkQInTSoUdeFwgUeOFIhF9kBD1_nGqRbNd0NcnVzGRI7QN27h37k2lsTuOPYQceqT9iE-5DrGpt6lMBHDapmAVEvpoSWW2LJQdRC2tIr1ZRi5QA-L6ZNT0qsJqHNY-7CApvWfxftWTpH2P3G-8I7veJxI6B3hePv2BWTwOHAxpAihoPsRTxtI8DYdto_BqGxJIJAVeHgnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاسمیرو بعد از پیوستن به اینترمیامی: اومدم به لیونل مسی کمک کنم که جام‌های بیشتری رو برنده بشه؛ برادر در بازی اولش برای این تیم امریکایی:  @Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26983" target="_blank">📅 10:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26982">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKwYJQIGnJl12oqfnvmYxjYhkIp0SWTgwZPWbcka3LKHaP6m4S4xrs5kY9O4K-cTEHS91NijXifCZp4Bh73QLQODd9e3AvaVMiHwVGA3BR0w-EbkAhxTm6120WL926bcfLw0GVEsn7dwXtLnwxrwfkf-cXsH8EXNZ5jKRHFydb01zG7YlQIMLAlEmh_Qg4cl7iLiMvsKtVS7LG-bNu6uc0Eq1n6qI8Qv-wWDA47BkeYT68lOEEr4Ez_p2mXqyA-RcibLaknkV5Cw6_WYwZBsC0_e18qBtm8nEyKKm4a_wrXK-Lp-k13iigQCQp55O-emRoXa37hXdgkdoNbWPkQ_BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
شایدباورتون‌نشه ولی‌این‌دراز فقط ۱۸ سالشه!
‼️
«جونگکوچ ماچ» بسکتبالیست اهل استرالیا با ۲۲۹ سانتی‌‌متر قد، درحال حاضر بلند قد ترین جوان دنیاست و عکس‌هاش‌این‌روزها حسابی‌وایرال شده. حالا بخش جالب ماجرا اینجاست که پزشکان گفتن ممکنه از اینی که هست بلندتر هم بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26982" target="_blank">📅 10:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26981">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ffde0543e.mp4?token=h0xYqb5RQPWnUQT9SFhijNjp1C5K0hvYBGyg_a_pNlCypuB5dwz5rPKIKpVVqTk2IUi5vMakBdA-a9l9fxeAEt72xQ1sMKWMC8UfrtlJoFPJK_Xp193l73jzpWbMUxXnJTdh4ZTsdnK6YwTJTZwle4r7E3NEIqtl4hy3mlcZuh-a_WJYkE_sJCtkVtfMqeY2gPnH7ENUENh3qJGXePKRMC-Fwe8LIhn28IrRHtEnHaIVI0z1fyLU-wYPU4mBs4ferNqBoaU_XvCGNDrEBfJYEGSxJUyU8GssBXFvsd8qxDZyOJPkwe-wOkbXG9LevYB041t69Qc7--tT76JB2EKs4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ffde0543e.mp4?token=h0xYqb5RQPWnUQT9SFhijNjp1C5K0hvYBGyg_a_pNlCypuB5dwz5rPKIKpVVqTk2IUi5vMakBdA-a9l9fxeAEt72xQ1sMKWMC8UfrtlJoFPJK_Xp193l73jzpWbMUxXnJTdh4ZTsdnK6YwTJTZwle4r7E3NEIqtl4hy3mlcZuh-a_WJYkE_sJCtkVtfMqeY2gPnH7ENUENh3qJGXePKRMC-Fwe8LIhn28IrRHtEnHaIVI0z1fyLU-wYPU4mBs4ferNqBoaU_XvCGNDrEBfJYEGSxJUyU8GssBXFvsd8qxDZyOJPkwe-wOkbXG9LevYB041t69Qc7--tT76JB2EKs4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟡
محمد نوری کاپیتان سابق پرسپولیس ملقب به جمله معروف و تاریخی "هرگز نرسییییدن بهتر از دیر رسیدن است" با عقد قراردادی یک ساله بعنوان سرمربی جدید صنعت نفت آبادان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26981" target="_blank">📅 10:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26980">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qr-MlHcZoHURs3YRxyH4_q7qfCtR5azhDFAM392zFo5bsweCCpEK3-B5NgOLdB5Peyk15S-8U2DfB2N9E1ltsAy4quVF3YjRfjUfY3rWq0looXYva2CowNOGi4iAzHDrBmf8NRP6VPcIVZcEtjoHgxAtDDWoszu7aNaAVs_sr7vfQyUZdclwRkkTNo3lBYvjHbLOpB55PTmcOZmFZ54xBNwOpkEbFepjax_quzybS7m5gvHGReAAVmXFb-iHkEGXWMZbrdGyMFk10YHzPGi3FFoqlL0hin0tXUOOUubmzesloUiT2d5rzVYw7OKPCw4DL_OELA-B3siMpfmDj7E_Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
رکوردداران بیشترین‌تعدادبازی درجام حذفی:
🔴
محمد نوری: ۶ تیم با ۴۷ بازی
🔵
محمود فکری: ۳ تیم با ۴۵ بازی
🔵
مهدی رحمتی:  ۶ تیم با ۴۱ بازی
🔴
مرتضی فنونی‌زاده: ۲ تیم با ۳۹ بازی
⚪️
پژمان نوری: ۵ تیم با ۳۹ بازی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26980" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26979">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSYNsWexuQDpeYho_iNrvcvQNvVIMm5z_nC6Q9lT-jpFiOCrCDJxboYg06oDELmEQKhLLqdWaM3U5SX8gGHFDtVvr1bq5HPChbYeWQH-CI_sU2GB16cpjKKU238HrzGfqzs2_4SGxFrA2fmkBShUwDNXZgThTu7yDCdX7Yfepx6Za1yr0TJQgiY1joncJHqlsOPJnVvMPBMmIJ2WT7QGinf4jUieGx9CgKuMfKktBmd69DNti55b6ZItDGaQGllCB_q68L-qQ3IWL7aeif-TlbeB7V1dmn32cO5ILdycCMOkNt8JAnkFNu0JrpXiQ3o6_JFgcMqI7DqSiap8b5qJDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تمام‌برنامه‌های‌هوش‌مصنوعی مناسب برای تولید محتوا در اینستاگرام؛ یه جایی ذخیرش کن به کارت میاد. برای دوستانتون هم بفرستید استفاده کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26979" target="_blank">📅 02:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26978">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHUnYN2RUxZEVr2DbvbcadudPtwPzu3BbSOoAUKQ5JtvsSPjX3yFKL5luNH19QLCLfNfAbrWXIrJ3jPVR-989TbdnbyZSL09jZfS_Fpjc-rdJYbT54UxCd0PY1ZaW3kwLboaOMQiHXXibORf1090rNjeL4iu3qXGADDCRy9FGvOQrT5-I2JIYu0O1lm5H9fl0TytRmdq9sAgfDt-M6dBiuqWcPK3e4natgMzeGNoRD7yvm-fWQbtkVMzjUTX7-bVMp9pQHloBwBISEiyihNC8cw7k5Fyr8SgaRm1rcKUCDkjgT2-LvkfGW6KH1iRKWLmJPsbCEvmv7u9sx6dm9S5xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه دپورتیوو مونیسیپال پرو که به خاطر بدهی های سنگین در آستانه ورشکستگی بوده و به لیگ آماتورکشور پرو فرستاده‌شده‌بود در یک حرکت خلاقانه کیت خودش رو به ۱۰۰۰ قسمت تقسیم کرد و هر قطعه بین ۲۵ تا ۱۵۰ دلار برای گرفتن اسپانسرینگ به حراج گذاشت. جالبه بدونید تمام شرکت‌ها محلی و حتی هوادارصاحب‌کسب و کار به طور خودجوش اسپانسرشده و باشگاه‌رو ازورشکستگی نجات دادند وقراره این باشگاه به لیگ برتر پرو برگردانده شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26978" target="_blank">📅 02:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26976">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqgKIOr8kSoEomWmxoCNNTKzJyldAQjlV9nqBO4CF9MZcpNc-gMCdMbPpKY6B9lFrYsXq9mAQ3I8myOo_0zjT-ACS0cNOil2x3iryN-0ArmYVuQzC7FTmLvulZaStuogx5DYQeSuxMorx8R5gSqZLztN9qkzBSNjus9BkLT3CRYvjD8_Pp39GxTWSOSSCdbNvmErwZOt8AHbNy-5WuuWF8wkqf8WR-Q1u9V_ZKk-49rZ0qzUC8G3pgPAwXijry8pX0ZwAUPwGScpgCbT8-exsewvekjRrKjqmCi8oyzxK9XbzCGSaw9BY_CD6n-QsceaRZtSGXf-NLX9CBjIDlSkQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
بازی‌ میامی‌ برای بازگشت به صدر و دوئل‌لیورپول‌ولیدز در اردوی پیش‌ فصل!
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26976" target="_blank">📅 01:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26975">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoPh_tDjeA6Ja5kokNDH0aVK4-TAe-5c3RXJYYqELs_hDowDOYNFwHlC_oEffj0R_dovEtW0ey57TG9wD9JYr0dm9sj9Oc10Aw7-lY49snqgtEzOe3GhXuQcy2lVJ__pDuMIzOBboPqVCdbHCUH2Zk6g5CF5CG9JMOXCo6eSbIKfhiin2BmxVMsFX_92RAYE40I28N0pkm543kEy2huDFwPNSmHt5Abgz8CJQgZCMVc-0cVP28IqngmwdALRwzyaAOKVESCwK4FQWtesbAr-K0LDTFhxYFbmndnN_A6aOmGUl6LIuPA6ydyGaTxbMnJ4u5D40KrMY25ItlpiGe737A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برتری لخ‌پوزنان با سوپر گل صیادمنش تا توقف رئالی‌ها برابر یاران دخیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26975" target="_blank">📅 01:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26974">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGz2cCpEOnk-qvAMXvBZryjH6w1g_PrlPSPWvIdkH20VfOvzyD2qL2MUfF7QBwwqeWzCzDbDf129EhePZBbV-GN8eJ2QOmSYMmKLwc2VCPkYrDBNidYWQcBYGowDZtfWfQi7VrnLkB_WiENSl_1q31Y_AcWH2MdRNKTmkv7gJgXrnB0yDPNKA__OttN5OWVTDQz_jdoLDpbrnL1NRSg11Z1NJInH0XzannUfDZLOIDxImFQ0YERDgmMk0Oorr-5Ys1tsxGgKg5jpljwLtlmL0-LbBpePLFL3cltwDPOf0WGH7Y-swmCzX5p6aFjKBGpHhd8PKC-pVk1DcMh6tGdmgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26974" target="_blank">📅 01:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26973">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hp0_VqdBc33CseRE66J36wUzZjNK7fNK1rzL5Q4AnBE-qeVaEBeKPj1fm19CKY7pqS322r3kwjwTBarXVoJsHhshCKK_6Qc7YRMgNPEBxfYAI1ewyKcqpOs66Lku40WCytAOzk0xPL6vlZ-WvzYcdPEI3Us2UhQFWe_8jMnp5bdInH7fzvBcYY3PvwU1hbBHgvQz9gegVdy0aPTwcY-8TTYkitBrqmZgKK553_DUedssFfL5dN-sgwCSi68ikpLPdjBwlrNufbKYjjf6C1guEEybxlCqBM2vsplFxBgIn7a6WQ07sPqb_hEBg5lGxAnNG6Er4sI6NbkaU8ZibqqeSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
داکنز نازون مهاجم سابق استقلال: دوست داشتم درتیم‌استقلال بمانم امامدیریت هیچ علاقه‌‌‌ای نشون نداده. بارها گفتم برام بلیط بگیرید تا بیام اما باشگاه هیچ پاسخی به درخواست‌های من نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26973" target="_blank">📅 00:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26972">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n014dVIvyoH7XxPVAyi_vxRcIShPXlc1ttJHTXfEJzcgbzF_G9j11I8eD-TCh3BbRz-Ynqp4Rc_xSjXnGOPRgRHf6MfWEqrO0PSVRYU-es7QHhavzrBDJBN7VS2Jt7RwWUlR_geAHwyrXSRDjPOF-H_PMXrewcxIvJxF4Qfh_MUEsPuSabm1GwC10R2zYWnXb3ge-j6mbN8lOqxzD_aVA2HbHOKEcdoOs3T1gUEMqOsKDZe_HXDppO-cQhZUAlxmXO5jBRcMSjwN2zkkbjx2_0BY8DJYhmpttfKJ3On23yhkbBAvLMrVgKyZxYpLwxy6Jpb3qZN-M7UOIyDYjJ2ghQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محسن بنگر کاپیتان سابق پرسپولیس در کنار دخترخانمش؛ دخترخانوم بنگر دانشجوی رشته دندان پزشکی دانشگاه روسیه هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26972" target="_blank">📅 00:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26970">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjmj3dd22IPL2XL0JyzPc5NtZhuR_Cm-ISHISt-pclMrVHHqVFBnse23P_ThlkOn3LO4ugXNg0tzLgB2fdevBIJ9Kuh91RibuZ2v6vZo0qpLf6fjGxTPBq6vGQyfIQtW2KZy5ZXRgH_hh6dxhSvJAi7MsLVMnbF2XQzXHyC-Eu8v2RrJGK5v_JPnvZW-N6Bq4w6c0tcxV3ezAHM72Hwhe2GXl9Sc6TwmWzyMXfEZieWE98AaQycumVUAtRxJI73GpHPvIzsiOHt4HrGxwWr6UKhtaHmaGIVeBV6qQKt61Ph6HwRgP4mjbndWjrqlBTaXut_wwv9BCqzgV29gBDJaiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aeJ_UOdLU5C-dXCdDpGzhRcxgNwVJVGSaowWEyGzz2dODHS4YoVqmL-CZYc74YQWrfS-xGKE7dRBKe71rZ-0-rcwwKPhzlZ6knpVGayQnt6TKXhQu-agp50mZ_lOCs10qAT5rZomTjnqik5f09VxD4bP8H6fnRKIitRzqaM51LA3hS--dBMuL5PlIq3FMvfIuKIHWzCvlm10QslIGAE11LnUHtLr1m5O9U8aelRkdJNuepKOO3-Vc0ZwnXHldIBOXyfWYZAMgRR571FZnKDKweElqv-Ydbs33XM5dM9UhlzWj8tdARDq68JviVLioPQpSDWNwSfNa2ZchtygsevBUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
دریابنگر دخترخانم 20 ساله محسن بنگر: از بین بازیکنان ایرانی سبک بازی محمد جواد حسین نژاد رو بیشتر از بقیه بازیکنان حال حاضر میپسندم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26970" target="_blank">📅 23:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26969">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQEf2GuoXwg1Zq2vZX8GTEv2Y7hk1sspCiaawei09zBUXAkzDulK1Ei91n43BI28QP63fnIqfu6A6hkz4xhzhCVd3YDsObyTEcsmEaEavFC3SxXYt1YYNoficK6uZycnitcMQkDyZzXnZfB5QP9OInHqTv5dnwnbPFQlKqvRf5FzCg4-mRZzyix1zRm0mDSCPNiUAJRIE72Z-nWKrvCU_ysouY-PFH-_DN5RNXXBEyfC1oth2tANiHMxdmwURvvDstZTBSZGQtEOf1826cpb0U_yvvDaVZsp8SUhbTNDOxIE8XYcd19mlHCeKKCVU1a0CG29kJYAeWEyHcjHLT-5KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام مدیربرنامه‌های داکنز نازون؛ این بازیکن قراردادش رو با باشگاه استقلال فسخ کرد و‌به‌شکل رسمی از جمع آبی پوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26969" target="_blank">📅 23:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26968">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSBkaULvG9osNPk0wCNoAwqhkmDM0rtN4srT_VX5tW5t8GjQhCX2aCRVBEahmpeeY61mC4t6YkEx4I4dNise8Lj-ULg6UEVixuUBry_yYCNmjr7kcmZiDRdpn_0UhwmKEhTNNHOF7HkpWjojWtFc-wEGVkGjgE3-2wvNvO5XSQRffcGLxvTJ_R7RABSro0OSlqMv4_WRVEGss7y4kRg7zFDfXvlRDuy9wI-Khw9JdxZ6ao5kGC4BoNOhD7QqvP-3jTcVteV3UQH-QV-xmvlC6lasbBPfWdx9JgTx1jAjv6sxFjs1v-GhSyMBAEFF_MzG2me0IdwXf60ngo38tQI0jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌های ما از باشگاه پرسپولیس؛ علیرضا اشرف مدیررسانه‌ای سابق‌پرسپولیس‌بار دیگر به کادرمدیریتی‌سرخپوشان پایتخت بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26968" target="_blank">📅 23:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26967">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgQyF3nIqJC1skIivLoRxJ6MFOmKf6YRlQ9QrR2Jm5Hp1D9Cyk8tsl0gKb3R4XtmjP1iJ_7rB2SJ1qRxgb0wtwNdtskHvm5UVso5rQ8NFZGj9r3n5d11aYA-P4eikLD8m23Fcs5y2MuXK22hFurYeJ-sczsY-5DAbDwglvq3Cz8MkHkq5my_uHu9WsnJUNcXXtg1V_O11LU7o6nXVNB0QWhm9C45dKzlrTei_YgX_UxMgLRE6JSy2i3ZwHiRVwBbTdiCZZwWYnJiTudGuMTQUhCTScFRRPNbL-QTPMzJjkr0S7lAz7uDGHTN7fkWQvuJO7OlbC3cqlfboh11OE4WuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26967" target="_blank">📅 22:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26966">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWZ-qM79DvDGmF2K7rxLVY2T0LsWZBpbU_VPpmNseA8x_Wvq_K5TaYtGREoIASaf-Cw7F2MCKl6BXjB7fhtmYXmRHxSFZcap8FO3epBe1Me_0049LVTIQgSJYqcIoVtvT6wkRjTX_jCYMuntK5f6mWSSeK8O280zej283_uw2chasDmu8sjU8jiYZpHHnXU5VQHnpKM4pxn3BNu9S7IposKIkaOYOfYk_7XMVJxw_BqFl_kx0FZTMLfMCUU_vZ1_CQ0fQ7XfvWDsSr1UlYWKyJ57fLy3NTMVFZ8uJjTR618TMqwDRYNhU8T3LnRUQdotQS-MAUWDBTwl9FoSeS9bag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف‌شایعات‌مطرح‌شده؛ باشگاه استقلال تابه امروز هیچ مذاکره‌ ای با آنتونیو آدان دروازه‌ بان سابق خود نداشته و برنامه ای برای جذب او تا نیم فصل در صورت بسته ماندن پنجره آبی‌‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26966" target="_blank">📅 22:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26965">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LT-YFOz-ube5BhWTUObWaF1U1NBxXVWo94nT1623sotxsqxepMewPIx3glMLieisC1Xl7Lj6AIM2DENIUJHhAMyYuVGpFXA2oV-6-84_ozaomLI1YJjPz5bRTKdJJyFnyAtInGlMu_ZoeIfyi3KAUvqTMHTNmUSKMoVEesPn9br7YEbT7bxVXRxGCGaqGlMs_1S10HnyK5JgJyjis9TZBD2Wrfh64fgHvokffHVUWeId3N2erc-BIiS5P3DkOjKXeBYA7eowxhW0CQYiCERfw-YyH_VWilejRndO53N9bRNJfmWBBOD5zCIr06GS_yrcv-q5126dITEUjGUsKGcBIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
تایید شد...زهرا خواجوی دروازه‌بان تیم ملی بانوان ایران و سابق باشگاه گل گهر با عقد قرارداد تا پایان فصل به‌تیم‌بانوان پرسپولیس پیوست. همچنین زهرا قنبری مهاجم تیم ملی نیز سرخپوش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26965" target="_blank">📅 21:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26964">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xq616MmeTyxd49GBOXIMzZRJJiTqXY7bvjWKGKR5iyXZKLQxYxXXN0SQlTjPvsWzvFE0peQDeYQIa5OQBCmn8DVLk8if9M9sHGift4Y4gyRpGby23tUBUZLJgHVOL58WxCn_u3Vt1oKiUfUs-ZxPDfINzBt01BqdD2GjUyRoF7vDCLlqX5KPq3l8lI5FKPuuQwJGIMfk0VUK1ElJ3BZZ2CoFz8M5DROeyNoGYsXGIZcRASDXewGo9pg6rG_jSBNhFwxy63JGuoBP63L2eWKnilbveBkoTQ2ymV5OpBYVYcstna-MzSYwTqlsyZS4nZ5_HhCn4hAukrvQeIGCmi1hsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدید
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26964" target="_blank">📅 21:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26963">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_CXDsjTrv0robB2hkFutww2UueILbrMqy6VRDXX1oKuBWV__LIknUIkW8SNj1eYC3FvnVEsuHameBVjMElavOW1t98Exy4jJlpO59LRLkdYOVtPIL0ENAqE8QFp_lxxRFyNg7vVdXQHWjylWFDV_Id7LJGBhMANZ6STXlAxTMY6XXFdFzNQu3wggqMKIc4OWb55yWSijCpveiua6pjlV8vXVM_SMGO7MUs-eyQxESLfUDGDnD8iGNQNVxakBPHouU87_V88l45VF1juyGsck3gIjmrXz4OxqdoRtEG_3-Q_A0KXSW0Ar59EaWsMYMkZp0unTxwbT7NbOwoXYQaL1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه 3 بازی دوستانه‌امروز رقابت‌های باشگاهی؛ پیروزی اینترمیلان و دورتموند و شکست چلسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26963" target="_blank">📅 21:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26962">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuSyWG6BylscJby6qRIC_BchDDfu-c2g-o9jA8SFFszMyPAOA3BiVyo728ZIhRC2vwZivuw2Bsp_vN5S5h2_YhP0vm7BRE7yelV3Kh3Hjs1cjzmWlb4cB8qMdvNsjnKmFDyBYYYzA3wiNbHQ9j0LY5yZd-zi6oroDInOz5UqDWPW9ychvD02zSbeje-Zdxw28LAFOzXZhqvk7a40Gdyk-rCIxWUe4lQUcIcZBhBpB18dQsbut2lUE2lpra8y8BxkiZAwJ5yRA0xANpiKXx3vosNy-q0WjeJ_x1YJxsO7sNjL4iVT2K0FIHER-ZTmiHxab6sPx-K6N2U1r7I4BhwQYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
چیواله وکیل ایتالیایی‌باشگاه استقلال: روز دوشنبه یا سه‌شنبه هفته‌آینده دادگاه عالی ورزش رای نهایی‌خود را درباره پرونده‌باشگاه‌استقلال میدهد. ما مستندات رو کامل‌به‌فیفا و CAS ارائه‌کردیم و بسیار امیدوار هستیم که پنجره باشگاه استقلال باز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26962" target="_blank">📅 21:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26961">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8FIt3g4VxfmP6m0n7REv_wuNAbC6ZCMSHuBDUYWUNJSL0eKY9Za4B9exbXUqf493El79cR1G4SNcQQOSWsnMlCIMZvl6ie8dbBACAYHCNowyjBJaKOB6IhQqPtvudpeybnNwCC2XbE0IAqipLvupWytX2vqK2xhpMO3x77Z9D-zR-Vbn9V7VU6bKSIrAXuMbhsJU94jBQIrPTF4N9nj2Bw-pDtBTz51el9WS-sREj6KoFKWOSt7sse29JbbBtcbIcHm1zbMIxfURnGP0dZgtKvF0azem3yk9WYNFPSvDmoI06jOe-5PC3uqNGLn9bpZw0HpQXEFNZ2ewH-ryRY9eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌ های رسانه پرشیانا؛ مدیریت باشگاه پرسپولیس امروز مذاکرات رسمی خود را با عثمان اندونگ مدافع میانی 26 ساله اخمت گروژنی آغازخواهدکرد. اندونگ سنگالی علاقمند به بازگشت به‌ایران و پیوستن به باشگاه پرسپولیس است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26961" target="_blank">📅 20:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26960">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFtt0HAUDDuajEppEZGrmPRRKZwFhi0FrjvX0xPWHa2tco2CIj288wimVKtWOS6u4ltunf-5wMj8GzCaOXjOzPvl5Xl1RL26D_bcDzIfdiOLiPAH04zqQ_APQwCt1GZ8ao9sWcBqQO81gwzZs-O-ZvVa6HMZHsiZVFOOhUQr0Zj_YPi_zxWQdeKBImOsNeBFrrAvf9tG-fEX24uTnXr05NgzmCWttZYaBfbrsFSXaDfpkpuv4rCkHFhSL2-mqibSDzWeFeXd8lj899ayR8YkdCfWyRJwOT12_l6mHHhhPWZh2wp4G2oU-JLNhk_7ddjLGhBsjppV5WL3DBE3r4LtKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26960" target="_blank">📅 20:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26958">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb2a69728.mp4?token=GOxx6WvThqkCLV3J_iuh3933Awoxv8kdFS4mK03UMM-eqLfVLTwTkbYrVo6zSlN4ZzH0YgRCoL_g7zX7zZLTpdd5Ykb8-UZQFB8U9jKcvrTLc_PjgRnpc1ykVg8u28XyvBJJcw997nvay61P1X2YVvmkUy56VYI_l26B2qbEFb5eVGwboo908d92pkLEjNMZkv3FjdcA8edPR5W_JeMTjagfNkwLBqqAX2waMfCL_Xq5VusF6l8DNExheaqmlMzkgD8WtJlDzV8lME42jgn2gAvUsYKI7GNuP8UwPrUNVZ4mh03HzA1EqoS_hk7Htj7WSEf3XCgI0nrO3dQw1oJpX3p0Gv4KlDUblULL8cvJDjahroqj66hgDzX6Jvg7VMyvdItcAjOnw4ABUO_x5U5MLj03dSWswAMQYYnb3_wa8Fkq9_nuzdTvnsKiyGE0swG3Nap1N6JKgG_86yg5J_icykRHIKdbeR-bmbWc4X42zUpFjTxma7SCjkLIp29TIKDNQJNRhNYvJEr9TdSujB5VgwcBkiMSyH9wbJgzVEVL42IALXNEsw1rF3F27Q97dxqgNFthac515ZFSgg_yZmkzXhl4c6xlmtqP1n6lDm0z1TDI-RirfwHTiQFqkY-tavw6G2cXgEYixck0RLfIISyefmt4R4fPkcRNfF011iMLfU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb2a69728.mp4?token=GOxx6WvThqkCLV3J_iuh3933Awoxv8kdFS4mK03UMM-eqLfVLTwTkbYrVo6zSlN4ZzH0YgRCoL_g7zX7zZLTpdd5Ykb8-UZQFB8U9jKcvrTLc_PjgRnpc1ykVg8u28XyvBJJcw997nvay61P1X2YVvmkUy56VYI_l26B2qbEFb5eVGwboo908d92pkLEjNMZkv3FjdcA8edPR5W_JeMTjagfNkwLBqqAX2waMfCL_Xq5VusF6l8DNExheaqmlMzkgD8WtJlDzV8lME42jgn2gAvUsYKI7GNuP8UwPrUNVZ4mh03HzA1EqoS_hk7Htj7WSEf3XCgI0nrO3dQw1oJpX3p0Gv4KlDUblULL8cvJDjahroqj66hgDzX6Jvg7VMyvdItcAjOnw4ABUO_x5U5MLj03dSWswAMQYYnb3_wa8Fkq9_nuzdTvnsKiyGE0swG3Nap1N6JKgG_86yg5J_icykRHIKdbeR-bmbWc4X42zUpFjTxma7SCjkLIp29TIKDNQJNRhNYvJEr9TdSujB5VgwcBkiMSyH9wbJgzVEVL42IALXNEsw1rF3F27Q97dxqgNFthac515ZFSgg_yZmkzXhl4c6xlmtqP1n6lDm0z1TDI-RirfwHTiQFqkY-tavw6G2cXgEYixck0RLfIISyefmt4R4fPkcRNfF011iMLfU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
پوستر رسمی باشگاه لخ پوزنان لهستان برای اللهیار صیادمنش مهاجم جدید و 24 ساله این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26958" target="_blank">📅 20:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26957">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEmyY-I5Pfoic2VrVootaLRnt4r8O1M6M2wFoEIitB9eIKFQnxsFtVPUL0_EamQgQUP74EztcIQybSzLop1bJFo6HDcBz1tDmK2A1pH3vEXDnWAgplLq-68Ux3RFM4tdVmy_sdHFKLCiiQF6QGHmmk59gR6bsQwZ0qL2mhCz3eAshVMZKRUW6LVh-5fDVB_yDT0fWOMHHjLb9E391RfohAM1j2Q_5Cqhr1qAtaffWcj_C1gbNKbknCuXyLh-naJQUNz85Wnnl0cDDkmBvNIiU9jQY5s4c7BlN-FyY8-H4gbXwCNKFfWHRCwXJdHEJRv9_N3fUdgNiiRAm6vIogG7rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
هایلایتی از عملکرد خیره کننده فابیو آبرئو مهاجم 33 ساله انگولایی مدنطر استقلال در سال 2025.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26957" target="_blank">📅 20:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26955">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q8nF3_QpvxfQRd-cR8z7Z3lJC2ZOa_BdpYwKbJ6bYoGAa-mU5Spyo2-bKzEWKWolXNc4vNfxAlGme99jJOHUeVSQDpSvjwe2xpuf8uBUbEa58fxHSBp973sKlDapsvlr-7DG5f1_9BnxFL5kAkKslEM4Lk1HGmE8l6zWg83tkWYqGN3YezV_7PJH7PLBGHLWpIAOD0jccnTXJIY3D9irldQ8OJJnIVMowl0Y927BMWKGzuzKcLHEWHJQ0vIOJw9jbf63SVfFtk6FBStKeKj9BT6HQcZgTVbvwPNmvOnBFtlBxurNkI7golhhaea5w3m1f_a78hBxbQRfQWoD406SNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gG2AXsRE3GjCb9ftNCUm63FwTvN1t7cwmoWSurfQUC84DpzNOWtHA2ta_bGtw-ZAXE2app7NIEGXSwUZXDan0E78n06fjmZ1-JxH9_ww94alJzKL1HyYoxc2hMP8_j944VHdJkyA08C-IWRgZU1Ra_IldSfNyTvkxrhPtd-S4ILe6yCwcjgXt321chHzw7_k_VB4c3-FaCsrw_DH2xQOtCwulenf6bZ-f4ZFeOo2hYvPtEmXZJNIrRHGoYLSli70G1AKNj2br-HAXJhi2W0ncm2Ukvl0DhemhsPaqGCw6Z72X8KhQ4xaCdUYmhlYFipz0PaSHZDR_oX3rUx19ps6fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📍
برسی تموم اپراتور های اینترنت در ایران. این‌‌ پست‌رو ذخیره‌کن و برای دوستات بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26955" target="_blank">📅 19:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26954">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQ6yi8nQXxBkVqlSLtbVIPMorN0wqe6rrVPD-h0JRprwana556L0pXa9TseKqp9ZufJYGDD_pdnPouUQtcAulS9FbfA0K1awDjv5DO7EVz2GUvG-eSPYCqTIpirih3H1Vza4a-DCcWQKad103oob3bZaGg4vEzw3Cvdf-OQsHtLdj8LVh9nsUpgMZSCiGR_g1s-5Cu0v_nI5-MVgMYhXho2bqn3Mu-uT-RjA2weKOYAp6ZYoxlPG4-U_LbkQVj23rmYTQGJgw11uCJQXDuSCdDSeHSdX4-GH8T0GGPp1VdQFujFeoePPWwLBtvylW6mAQexiwbFFJ_hxeKPvkPPnDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌ ملی‌والیبال‌ آمریکا در نیمه نهایی لیگ ملت‌ ها بابرتری‌سخت و نفسگیر سه بر دو مقابل ژاپن به فینال رقابت‌ها راه پیدا کرد؛ ژاپن بالاخره باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26954" target="_blank">📅 19:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26953">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjoTfS8AIpk98T3zqJ6nxyMkPGdxC778FFZ8obBF-8D_R4KN_-JK9X0IKxWSfkUmOhyvklptHK7XPI3hTzMpOiEn_gVFdDjP1sdZCekAiBud_akKCqTzK21UtOY7TbSB4T_HC1uZyrfimWYlzPCzNGEX3z0FbThyS7vctqaoAF-Jstxn_mYAShchkXAt9AdwTgtIJxbpe30kZPStR53RAYFYoU7iDLDNphupjmyVX0Z5e4D9MvUkeqr1PshWqCzyotnCjOK2LBAFNBGRIw5KNFwh1xevatC5zgOrAjQvDfEtDSrf9sd9h_LS2xU08T3C6bY9hLlxNkEkxsghRjspYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مهران احمدی هافبک تهاجمی تیم استقلال به دلیل مصدومیت دیدار هفته اول با مس شهر بابک رو از دست داد. باتوجه به این رقابت های این فصل بسیار فشرده‌تر از فصل قبل برگزار میشه‌. اگه‌دوره‌بدنسازی‌خوب انجام‌نشده‌باشه دهن بازیکنان لیگ‌برتری سرویسه‌. هرسه روز…</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/26953" target="_blank">📅 18:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26952">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf02af4598.mp4?token=h5dz3E8NrUWMEK-iT4paNcFdSH6QVQBgbKWQqoZC2PEACMxrNf2P9r5kxUT770CtWuubbHyFYRpwgnE6jMFgAoJTNyjDUgLKxTj4JxM0A6nAQlXbu7j9WkjbEKeyeJGGmgdj-zFLg-OtZOdza64fZrzTM8pof-iASkkQcxCr2u7l3DzTVMUt7R5sWehbamHnYMOxuyXYk45KZ6XgzFXAiSevatshcVPafl_XdrjUtMbMbCWyu1vqdxiNL-xBaQEuoazzFg-SyNVTQMwejC1S9Q1gy2kz1Y1eU_2X-Dm8U8VKwHGTqPeO0dVsRrQYSqMunvBdDsFcH_Gp1BI8Tuy_tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf02af4598.mp4?token=h5dz3E8NrUWMEK-iT4paNcFdSH6QVQBgbKWQqoZC2PEACMxrNf2P9r5kxUT770CtWuubbHyFYRpwgnE6jMFgAoJTNyjDUgLKxTj4JxM0A6nAQlXbu7j9WkjbEKeyeJGGmgdj-zFLg-OtZOdza64fZrzTM8pof-iASkkQcxCr2u7l3DzTVMUt7R5sWehbamHnYMOxuyXYk45KZ6XgzFXAiSevatshcVPafl_XdrjUtMbMbCWyu1vqdxiNL-xBaQEuoazzFg-SyNVTQMwejC1S9Q1gy2kz1Y1eU_2X-Dm8U8VKwHGTqPeO0dVsRrQYSqMunvBdDsFcH_Gp1BI8Tuy_tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌ ملی‌والیبال‌ آمریکا در نیمه نهایی لیگ ملت‌ ها بابرتری‌سخت و نفسگیر سه بر دو مقابل ژاپن به فینال رقابت‌ها راه پیدا کرد؛ ژاپن بالاخره باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26952" target="_blank">📅 18:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26951">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3Y7TGkxDvA164wjrSbwFDfVORl7X5XCVxI9aXZfh75Ih91vz6wT_CHHJY2hvh06Z0A4ycp1UDXNX3FOSqQw347EYQ5gpldhzxfzIpoeE6Z2PtvBuh_n2D8r-Y0oa4zdFlJ2AZ5CubunElulG0Q9MbvmJwqk2GB2DS8C87iM9vLyA9pz9oECKCgFIE_HaaXac_9oZugxdVLkxE-AwZ_P_P2HQtkk64IAHp5CxRTvKTPoH3lT6sax-sMgJIeTWts27OU6YdX_Xr7-3rDbalK8Jh7_FS4DXFBbCO04aule_nv-G3Nk4iUZFyISnagXPgorq_CErImZLsXOJVHZsxeg6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/26951" target="_blank">📅 17:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26950">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab908f0eb.mp4?token=tuLaHHSBqGLFoe4PtEscICLSitaHJVPRz5FTrreapKjO3ftLno9SqgWJjgwkTJremf1-1JPmhzxbQDXW9YFde0Yp7WrOWUWLcCAUIwURCf8hGCt4OVcI5TOzr2Vxbm4kvBMPocEXwwrZFGbxQx2L6JDO6q8hdIqeudmzj8CMm2Ub88MloD0ogrQy3Ika2V5ZEctla6YSZMnoDVFvBdMrj5RdyIXULNmkonuspemz8jvNYZ4fpjSxUUlNHz5NFtnfGrx4VXRncNX1dPRa8zhIOz-Ds80iynPIL3fPg1jzd1a2Sqf7PHQpecXaymZSich2DWugiDvPrzUFc2aVOV5L-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab908f0eb.mp4?token=tuLaHHSBqGLFoe4PtEscICLSitaHJVPRz5FTrreapKjO3ftLno9SqgWJjgwkTJremf1-1JPmhzxbQDXW9YFde0Yp7WrOWUWLcCAUIwURCf8hGCt4OVcI5TOzr2Vxbm4kvBMPocEXwwrZFGbxQx2L6JDO6q8hdIqeudmzj8CMm2Ub88MloD0ogrQy3Ika2V5ZEctla6YSZMnoDVFvBdMrj5RdyIXULNmkonuspemz8jvNYZ4fpjSxUUlNHz5NFtnfGrx4VXRncNX1dPRa8zhIOz-Ds80iynPIL3fPg1jzd1a2Sqf7PHQpecXaymZSich2DWugiDvPrzUFc2aVOV5L-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی بدنی خیره کننده احمدرضا عابدزاده گلر سابق تیم ملی و سرخابی‌ها در سن 60 سالگی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/persiana_Soccer/26950" target="_blank">📅 17:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26949">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXWqbt8CkTM5JIvgiwoev3DYBYbyNwOOw02ZiRI3onD4nVjNiX9eQy9QjQuJSY_p_5-3-mPJXNcnBmdOzhHfApkphOupyrjjn88EgUBUXBDOib9di068Qog---N_BGWHlnqh2c_tABUS1_XcYesit_4Cev3P5krmdGamviW6VXpREmaWIkUFd4cLFYJj5sYw67Fcr0wIEyFV8-2vyvQQ-q08w3pakIqqas_UolFVrymdoOJA-qAeZVyBKAwVy9W8nr4Vkhb1FmLF-cwjuyR7-TDjvYeahlbwuprUV--_2Ox6g5klHr1mIxW59SPw2rB9xN0MXQXaV7rByJ0cuK-raQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛ از مصاف شاگردان ژابی با تاتنهام در استرالیا تا بازی رئال مادرید برابر فیورنتینا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/26949" target="_blank">📅 17:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26948">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N81Y3U4G4dLu2l5ZWT4TF8OE2Kyhd7O9ssHyFa4AThiq3lYQ4cXsRtQwGFo0jlMMFfpQrThVfvWCiXWm2pXUVj1PVwKNMXqRVUrP0Nsq2Qt7IsqfsDSGCpLUzTk5TbfKMsqeBXUAUFgKA5EqXUwIRUbPs1UsMQ1qjqmhfrfVYGzVjjl0CDWrROfvU8ShJMroRnoB-yVcvQhIP-LXq6_Q8y7Xogl-y2t2lGknU-I5HyW9kStULtWKlZPYWq5XdNlJv6M0I_6ZP8bhyJUOGgLnQuLtpX9BJUG5zq81_R_SaqR0Zx1oM-Zw-GxmTmPvmgITfoi5Ivb7Q_Xv0F7jwLpBQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس باردیگر در تماس تلفنی به مدیریت باشگاه اعلام کرده نیازی به حضور تیوی بیفوما و دنیل گرا ندارد و این دو بازیکن رو در لیست مازاد سرخ‌ها قرار داده. اورونوف، سرگیف و باکیچ 3 خارجیکه تارتار سبک‌بازیشون رو پذیرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/26948" target="_blank">📅 17:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26947">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0hQDyrVogHIs4F62Q6-egecHysB-BPRt9hR43HbGtOtIB6AziyiL_TnrGSuhhe7BhrGdd2ETiASMwJa3OlW5szKnJZGrB9Nysy4WwPeihXYQemaAxNJ06tJktAWgj4J4Ns8DNiUScXVvHu6pl0ZrFGdhu4oI8b4B2fHb9tL1EhKEp_Qy2SaITh-mNnOACmwXnPkZQ55ZTIYb9VOeIRSo10jHgZW5t-ziaWAspI5WQ18ZHpbxlSJG-dfY5HfRlB3k4YYWUh9Zwu82hlevFRUHualoELt6C-RaW5FpIYDGZeQwYknmUN0HEdGwjCCdlx-MnmfcUojJVI_Ak_IbT3uxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛ اسپورت: PSG این هفته از فران تورس خریدجدیدخود رونمایی خواهد کرد. تورس به لاپورتا اعلام کرده هیچ علاقه‌ای برای موندن در بارسا نداره و میخواد شاگرد پدر زنش در تیم PSG بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/26947" target="_blank">📅 16:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26946">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9oK5RXW_OUrH3x6XXa7k-ToFvcdHDROVD3swRHvGUjYLPbUmxCb0oOvwo-dRBNn6WFAlmFi6OcBWLvz7TI-hdpU5V2uekKUl5A_lxdiZPjFiYfaqU5sVO43W8KqMieoGzfh93xifRaSBnDB2Tu8ocuvwsOPSGUYawhqn9OVx-bq-qIKn_cPBMMG0HoRbIPyWS8M1zSlC26b3_pVZwVQW-X_vWZoaw4OZmSvo7dD148-hGURtNSfZO-xffSjM0l8gQYIktq8IexZ271Iz_xXpgf1fhzCfv2mFOr1YgSMV_kU8bzNLeYinP3modLHbE_LZ7cA40mZGEAmvzm7ZFd9hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/26946" target="_blank">📅 16:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26945">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psKLfoo-FtJwAFrVbovmE_eS_f4JPIMA9LVgQCN9jZwmXUqNobGLoVoKdZN8n-R78P3DOf4S_q1zhGFBVv0-ol95jfYQJFgyA8WOht41QvjGUNsVePhreC9W9GmAseLBC7WRQpRdoVWuwexPBep3ifsXQ6g2A2G69Gv3nbZRFLJiIsWgBIiBbdghVpY7j_3dOzG0xsd0WEAPvZwwiEiCh5h2s0OcZfgy9VZ7tfx-M1PuXj3ggJosimiZuG4gengJT0ZzG2HGEIrzRZquA4zDTchRjbDRU6ahM19M311-yHV_uraldjtWY_G0r5dEbed7tzFHL0G2khIALX3y6IHLUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/persiana_Soccer/26945" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26944">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQEheb6fXjGAz9eCkEoh9nbTiXu15gX2tZLqHepVDe2nB_XKWzmaxCCZF93RUN48APjZLQ4N5c8yJKoOZvfTpU5zP_kRHp1csn7MI1A2EMkqy5Rblm8lWOhdDzgodFKrybXRXHWg1UgEITkpcKamTlj9WysY2GJEtyQG9hkwJ3nNcZT4-8cQPeES_cYr1atxw3rQe23qZdB64GfiBaiArdQrjOYvPav8bA5fG4UMTysy1mWLjeSWQW1S8XaNasOsQfkrl8cxAvy3KL0JB6ZVQm0bRddOjaGzNv6XhlKM6cqukhYJZ-HaK_xuzXwtSpTmqI9ABgKn0TYMrPkFaNsSFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های‌رسانه پرشیانا؛ فردا جلسه‌ای مهم بین‌مدیران‌دوباشگاه خیبر خرم آباد و استقلال بر سرانتقال‌مهدی‌گودرزی و مسعود محبی برگزار خواهد شد. مدیریت استقلال به این بازیکن اعلام کرده که با ماقرارداد ببندید و تا نیم فصل در تیم خیبر بمونید. قراره فردا تکلیف…</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/persiana_Soccer/26944" target="_blank">📅 15:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26942">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqpgQdpDx6qU8aynoZnYs0mlRdy9PUVmzZufQmOcZhMgoEaQNtEZJRDhun4YiVC4hXzXrtWdyMR3Icr4-3ThQxVa1ZDtrOAu5QNsfS1ZhozrY6KUKGyB0K43S6N9NN84jXqxAbrSjpgGX-3iMFTovYZOCOzAsCCOtcdO9UeEQkn3SH9uXbZbauaNEHkjuv3btRvUMnrXHLWhwTMRsFh0_buUaeH2G6bGZbDTQ58GAZCDxI6pzLEuimqVrqjSbBit8JPenwVQlvPkDx12x_pMu5lZ4jkaAmooARURqMXTPiVhE2BnNGLjkRdKvQSosr-6OuwrSrHVhAfR1WDKw3YDqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c22a2b9700.mp4?token=A6Ke3ZcVayiEff4rWJ2K26OLCzkl5OzZxt4fN5y6iloD9QsnUKK6j9X7NFmKLpiDPsR_O-CESWtIpDGrb7Q7F1QkiimJXvL_shFYwEUt6vZhGjIFPasxBBbAJThiRv72nyNOwco9IMZLmwPKlOJh9meTc9Yh0z4ymDpjA_DjpAmfGtg3c-YrXg_WgQ5rEtfKXakidVFUIKCjrpT0DCGKvNMGwYlFXVJNPZwta_GyMEjSy1ywEH9t2BvVB8nnBoSu3_zx7Ihzn9azX-LurUXl2UCpApajnc1lr1Ya82qHijSAJljdbA2r-s3hJhnPVfkd1Ra0yc6WerFYzp3_YtXljQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c22a2b9700.mp4?token=A6Ke3ZcVayiEff4rWJ2K26OLCzkl5OzZxt4fN5y6iloD9QsnUKK6j9X7NFmKLpiDPsR_O-CESWtIpDGrb7Q7F1QkiimJXvL_shFYwEUt6vZhGjIFPasxBBbAJThiRv72nyNOwco9IMZLmwPKlOJh9meTc9Yh0z4ymDpjA_DjpAmfGtg3c-YrXg_WgQ5rEtfKXakidVFUIKCjrpT0DCGKvNMGwYlFXVJNPZwta_GyMEjSy1ywEH9t2BvVB8nnBoSu3_zx7Ihzn9azX-LurUXl2UCpApajnc1lr1Ya82qHijSAJljdbA2r-s3hJhnPVfkd1Ra0yc6WerFYzp3_YtXljQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/persiana_Soccer/26942" target="_blank">📅 15:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26941">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1f8c0281.mp4?token=RsT22jNlD49PCJCDBYiPG_t44elDNftfM5FaDQOkAmh2nbZ7St_rn0qmsAj75pfKWHnMEeux4TE3ydwByqsRWoaN9ihCZNvo8BK_c3652gZfsMk8qEniyhnpZFegf1F0CgZwKlMt0fPfVLLTPK_iKTrdnTJpkeXHrJWmQ41KZ9Q4egAqHZGdOexoRkEKrxj41oQ0oylMscNHf3AZxbW8ExUEDGcfPcXqEVww6SQL1hcRiQEd5QZdduXMX2qAOA4NwESGX9IImwO6v4aXe4wVQOuftrcLXgX0B7nr7J9HwMyR6k7-6ic73Thk6GBDO8vW6Jj4rONwf11bFEAMhKd-ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1f8c0281.mp4?token=RsT22jNlD49PCJCDBYiPG_t44elDNftfM5FaDQOkAmh2nbZ7St_rn0qmsAj75pfKWHnMEeux4TE3ydwByqsRWoaN9ihCZNvo8BK_c3652gZfsMk8qEniyhnpZFegf1F0CgZwKlMt0fPfVLLTPK_iKTrdnTJpkeXHrJWmQ41KZ9Q4egAqHZGdOexoRkEKrxj41oQ0oylMscNHf3AZxbW8ExUEDGcfPcXqEVww6SQL1hcRiQEd5QZdduXMX2qAOA4NwESGX9IImwO6v4aXe4wVQOuftrcLXgX0B7nr7J9HwMyR6k7-6ic73Thk6GBDO8vW6Jj4rONwf11bFEAMhKd-ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپ بسیار سمی که صداسینا پخش کرد اینقدر سطح ریدمان بالا بود که از آرشیوم حذفش کردند.
🔴
از سر راه کنار برید ایرانیا رسیدن...
🔴
علی بیرو توی دروازه یا که نیازمند
🔴
کنارش شجاع و کنعانی میشن پدافند
🔴
تنگه ی هرمز ما تو دستای سعیده
🔴
شوتای قدوس و رامین مثل خیبر شکن…</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/persiana_Soccer/26941" target="_blank">📅 15:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26939">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aegDHXD9ZBRBqjLj2qEK93-mQlRxWbUVS6Vj7YrgqeFj4qCrnWBHhbRVjLCJsBPXddQQF5XDfETSuHUya1otf3PFaMWE6zRFJwoZEWIEdaiiGTl2aQjJqa-iul_0josUD9QtMp-MhoYmAd95Kggu8t7ieW-zA42zcxR78otoUhQsojWZuoIWmDAg6RaARYm_1RYQmJCuotMcn807tUa0wpX_zZytxNrWiQvPcOZ31k_tVPFkdYoorxecstZB2sGN5B17Xv0Q0isz6fyjpsOJEqL2hk_KWvlxNaWkcLzmhb8Ql7wvhw0USLdd5mxxYDTkVgPHDvWNWOd5-D0Q9UVROA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l059O7TOfKHJdDv8DsPu-maP6crRrY36youECHM3_NiScD9sIvJwYF4HWjwZtRdsKJRHZla9DeSdrniHYNDAbUCYB_g87YvYzvV8H9OZkMkHxrKnROiUHUsUIMTm2hBgzUl3EvoD-snH-3Is-7pblGH-Hj0_6lbXajynOKaWDPj3Bc-g6ln5PYf0QZ4lc6W53xhl8WFx1YhsAT8VLgtdVCMt4unntPweBMZntGR6sAr3WKQfeXGqoLww-BygmVB1nglqMxz9HSAltRXpGlo4qAvzKd-ksQ2fEPriG-LeOk_fQ82N1vHV7prIx-FNeHvJOpN8H-bTAl1wg5zKleI_1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/persiana_Soccer/26939" target="_blank">📅 14:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26938">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wjn1kmKl7-1bgWpmSv9-EVnIoeS8MiRk9OGN9KTWzy6KDbUfrIEs9jR0FrEpH1R83dMNTzYVTivsWy8xZP93CJanyDi6TKbf9I0UrIpQGEi2SSihoZO9Rp52_PXTkvjObGqAg9zbbC8s4vLWy-DJ7YnDVuaBC67wx5ysNbUWZZm5DMkUP4AyEig6jJtujgrPUI7i3GaeWTkjU7J2sgSGO8dO3hGmELX1g_02sGgUeiQQsv6C4H15vQMi3nUUVRDym9jXoSqfMFZPhIH7HkJY_UpaM942FOR6S4Yge_SFJMoq7Z3pHIRzxzTarSICUuehiw1Vi1kxKq1RMg1VxpATQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
پست معنادار و تامل‌برانگیز رسانه رسمی باشگاه خیبر خرم آباد با استفاده از اعداد تاریخی 18 و 19
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/persiana_Soccer/26938" target="_blank">📅 14:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26937">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cdcb5398e.mp4?token=MyevwxToEw_GUo_cQ1S-PRW8mkJUu1aKWPiZ1igiCTtVbfHsyKmT7Z62t5ukhEoklf6ca_e4oRm8hyOebYPWE6fFhqnRKnbTj-6Vhdm0Mv5qqg2BQqky--KsOQHiqkIRrGC8Uvn-rL4ACcQDiYl7xUm-BGNsneireP4tprPKilO7aKgzcgkWFIxA6rNkb4-k6BHSZCaVS4ED5s0f_1YPkgG1LeistJweKSlr6nERtHFDlEFJDcvtTJdO-T7v86OhtC7InNJIDs8smgDhJhJhHmrINf9TD4fIcXsq1Im1ktpC2UoPNOJWnq7x80raso0RtzN_9KodJcPFHryK2qESWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cdcb5398e.mp4?token=MyevwxToEw_GUo_cQ1S-PRW8mkJUu1aKWPiZ1igiCTtVbfHsyKmT7Z62t5ukhEoklf6ca_e4oRm8hyOebYPWE6fFhqnRKnbTj-6Vhdm0Mv5qqg2BQqky--KsOQHiqkIRrGC8Uvn-rL4ACcQDiYl7xUm-BGNsneireP4tprPKilO7aKgzcgkWFIxA6rNkb4-k6BHSZCaVS4ED5s0f_1YPkgG1LeistJweKSlr6nERtHFDlEFJDcvtTJdO-T7v86OhtC7InNJIDs8smgDhJhJhHmrINf9TD4fIcXsq1Im1ktpC2UoPNOJWnq7x80raso0RtzN_9KodJcPFHryK2qESWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خیلیامیپرسن‌دارایی محمدرضا زنوزی چقدره که هرچی خرج میکنه تموم نمیشه. این ویدیو رو ببینید متوجه میشید. امکان کز خوردن پشماتونم هست.
‼️
طبق‌گفته‌خطیبی؛ زنوزی قبل از تراکتور خواسته بود استقلال رو بخره که سلطانی‌فر بهش نداده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/persiana_Soccer/26937" target="_blank">📅 14:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26936">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Du_pN8l87BqOR0S23eTlyLV8GKRR-L-IXGjfndUbTaVKJ37cXcnFO19bFegcPYo9KlTGMXYYpWqghS-rFX5yb_ZWmlo_4cU8aU7k8AUYdK-no7yJLA0GCFxML_uBrfBK75NY6dKoBaNQzAG_RVQzmIbWrwd8fHh5quIVJ6adJdOuh2LBmDGe1dwR7gGtgOXuSwfMZqReOCYSfjUR7snHM5wXn166a9Gj9xH7tuoGFKFPyNj6FOsNndLWvUXGnTvTbas3Ogr7bMKjVIGem4e8l3fkqkMVlP8oHtOr9D1N9nc9adqt8lsgA_R0vkBSEayZNUGs-Ui6NrWH6fQsPHdslg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/persiana_Soccer/26936" target="_blank">📅 13:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26935">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9-hp4SIP3naSXq_fTyxXhg58kyiab5dcjiwi2bTThF79CIpfDdQY2LAqIfyKnUiE3QSmDktshdjXFhiQCNQoExie7mhfkBoYeyiMWU7jlJstDxaT50iY-Q97qj2Uipt0LMsyswKUES3Y6fdYyz4m77G3FTNxaw32YxNoR8hR4NiYn4P7lNYYjXCWQDDOMMueKa-SfEjq4CF67_zi9Ee953yE0drqhddrdKEok47CwTHajtYNfmO7_Fc2JxHXFKzWo2bWAISDQuszi4zZrKFA6xjp4LjZ-KCoxEdDZgSJO66nqV4yTobQThf1xkI_eKIVczphQXGWiFnXQbirOVohw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/persiana_Soccer/26935" target="_blank">📅 13:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26934">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glSXkIR9pKSAACZbvwv2WsERaONopmFGn_UZEFejPMG-RBM4EUEyTopLl81kD5A4qgBYZZyk3VmaojicS7g6WPLnhl-DqQre0JLNiGLfLQW-73_JkG5SfH4inKkphQdCnPTOBGPht7Ns29ooFoMyH9QhiLdZTS4YI6Y2py_7fJr0QxgnP3m9O8SnBH4BKN2YTmp1zl5tDhmWjzhOrdNe1ispd9AlpTz-lrUKRZ2Iri8iTDWxvL5MK1Y-hp4Xv4_fMliC1A-faHSoBs1r4HTwxI4d-CkDXoyYpwsCgCMfgwEuSG1QlHTyhxpM9bm32_nHosXIQ8oLpLoQbHaCHxoTzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/persiana_Soccer/26934" target="_blank">📅 13:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26933">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHBtHO_2U6M3_13akA3JoBpKqiqJZ_DoO-_9p1GGhpu9WkmdSxzHFSm0xUrUxuZovEWqiSQ2RqPxPDCZ-zVyfvZoKY1YWZBBXE5ja0FDJXhAYQUw4LtB7iHS2WQtF-3JpbDFYiaMQa-Oy5yMDb6VAu3NVhXoH0uCiZy6JAYG4MZ35NbxRle64lzv3uQphWW6bgD9FIrKRf7m_frPiX1VjZo7PgPl6QUVzUVjpwG7-mtJgg8SXuAFj-tVA53b9Mnht5ju02g_vQOIhy0-vBSF7-FINZ90S3GKSY9uKRt-sdDo5GrNZ_XAgQZFTXtZm5-guNnLVZAIC21AmZ3XDocmkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/persiana_Soccer/26933" target="_blank">📅 13:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26932">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1b0yFw7gLR1LDvJn4omNYuiBKPklIztD2xYYbwGe5e0BYAgyZdLFjEbaNMVpm9n5_yD_3b8BSSuJHZ329xnLHdVxcubeBZDpfnoqc9d-5kkP3YiiGSvANfP5hbjgMB_GeJ5DXeITfRfqaidSVzxCHBaO6rvLThEYy1kuMrq7hHgQPTNPu1WphTIz740ywe3XQWqQEZTGdDdiQ-578-hAjF5cfb2P8F1WnOQT9c7uWo9rf0dJ-rjBAq3qVeeMQS5eih3YFchqYro2nq8sy8pOAGmZDkbQhb0auJhtwUVuDaD7LElsPUza0jav7xV0UKJpdZCCzhGFnm0rvaRHPgsZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره 22 ساله تیم ماخاچ قلعه روسیه پیشنهاد تراکتور رو در رورهای اخیر رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/persiana_Soccer/26932" target="_blank">📅 12:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26931">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXaFp9AF45mY1M956j6qDHZryrYHwmLPhtbPOhwF6I7O-CbKIhA8MmMXMBNG0AEsFeta7TzZENUqlWv3VqQ72naEp73bruhzlckjwgDtuRAOuoznS6WC6n4gAGzGM1yEjq8btekgoLATP-6WvyXIwGSPTTMzs0nrDYRSh-usV3ZsXe583q8MYjHrITWQGIT6re9PCx43HErG_mBdBwvYfF0rgAI29-Jzn2T0g984vtB-LNzl1kT_d_xgCtqJNIxkc9mqhYROggopOBvKDctqBodlhE4NxektcBukWQVA3kV1sGEuSmr2zR1LRX9gdl6lUDa7JxP9HGWWNQbdvTcGdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
نشریهESPN:فلورنتینو پرز قصدداره درآمد باشگاه رئال مادرید در این پنجره رو به 400 میلیون یورو برسونه. تا حالا 200 میلیون یورو بابت فروش بازیکنان‌آکادمی درآمد داشته و به‌سران آرسنال گفته اگه‌وینیسیوس‌جونیور رو میخوایدباید 200 میلیون یورو هزینه کنید. اگه توپچی…</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/persiana_Soccer/26931" target="_blank">📅 12:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26929">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U_IkKnZIQCtU-9_yWOautAeeAI2iSrEnkZQhE_r9Ng7O_RmcWiLpTgA9Z4j9tJ6hc9ixRen0Q-qOtKagM7ron45jlLbph0ZtJUoygwQXuAKtN5lrUW8HHmc-sNOl_Nsv7k3WLXjzfGofQbzin8oAgS6l0leSZepVe0z7umvCVxcC4hPEg0YPi5WGY86b5hAt4GU3nOE-XnZ-kYgjZrOSDnc1FKFbjEOeZ5Jwe7ohCF-gy1R-sYT5siysZ534k6isivRZ6LJrbgVTLO42asHLnlEf5-6eyzv2Hp0704Bt03O0xngWgGDudry1hM_9Er9JXwuCL64Id7urpZzoS48Z0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0ng3BmioMnF5WtvpXP3Wp_V6JMfPlTXIBAZPqM-4DP0yKvwipwPD49IDkJEf34D1CPJ34eCJqTRclwzZxORuikrws1Kapl6xu7uzk6rpBAj0_zJIWlur4SQJeIu2PXxoNmf3kj11P897CZRT03D22PomYa6hBwWk0DXIQkGLWfpdDZsSECFujNz2_5_W6SIAoQVE9guCaEgnfjJP_UXUiwA10dW8Z3wtf_oDZs-VD9YxDV6uh9ny1Q0H1kH0bCdyU59G8JMS1XTY20AAZG-nEz1XusMpWoIjYVMmQ5E4jMgdVBeCv3X4P3jGhKuRY1-l_QalbjzZAUyJiYs3jh0eg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لیست کامل ورودی‌وخروجی‌های دو تیم رئال مادرید و بارسلونا دراین پنجره تا به امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/persiana_Soccer/26929" target="_blank">📅 12:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26928">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGKm55srSDUzak-itB7P3nm6d_Cm9LD0aEWc5tlc9p8Qy81XUSfGzTDM_ClnuJ9rgDwXyAoamraEcL_ixvX6jHYwJcZQekiYmf-uyP9OEnV6H03BrT_NPDmr_7amumGRQP5J5oJYedf695MzWYTUbKrLx6aXJqKoGj3EzuuCYjmEezZKp9FgyAHi-0knX3p-BMC4rSwBM7ViteDcnZ9elc65w95AgGAtv68IrFyFuX61WvwdqZ5-Zj13DoKokiOF7miwuOGbwgu0C3bZE8qHx0xoedWosqVaUoER9WxBEgZpoAQOhX2Ci5KupqQTvUa_x5pG5luHs6K9WApyZgcL4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
در فاصله دو هفته تا شروع لیگ برتر؛ مهران احمدی هافبک‌تهاجمی‌استقلال دربازی دوستانه امروز آبی‌ها مقابل فولاد از ناحیه کشاله ران مصدوم شد و ممکن است دو الی چهار هفته دور از میادین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/persiana_Soccer/26928" target="_blank">📅 11:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26927">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">📹
هایلایتی از عملکرد خیره کننده فابیو آبرئو مهاجم 33 ساله انگولایی مدنطر استقلال در سال 2025.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/26927" target="_blank">📅 11:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26926">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGGjrGglSVBTihODujnjnisLl2-3-KpU-UJKKGwxCZroXb8_L4K-Nta6FQXIvdL_g5_a-iyWziE4cqrmlT2nvXqyOV8ln5RNury63JJBahnbaB2jCmG-sKf7adU-tQ4Z6ZM-FMcMtcYipYhfxJQVna3fXfKh2dRQLLwyaKbYSpluj_zvSpi7qBVjV_ilPjhqJiYmxvryVnLu76Q3FNSxviAQEAHEFzoT0P5-RHZu6EbuHWmAwu3txf74x9Tmw53ZNKcfXFipeom-Nc73m6bj_zzm6KrSHaIcXn2Yf1qBK-UHaKCiHQ0H6jUs-KGvfn_Z1HmIo32wdLhZPRV94V8PUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
زندگی رو لامین یامال 19 ساله میکنه که تو این‌سن جام جهانی برده، تو تیم بارسلونا بازی میکنه، حقوق بالا داره و صبح تا شب با دوست دخترشه نه جوون بدبخت ایرانی که از بعد هجده سالگی باید به فکر سربازی و کار و قسط و کوفت و زهرمار باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26926" target="_blank">📅 11:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26925">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bykCFW8kRYNa4dZ1fZZurgjk36AkY9mb__Sl9g6VFNtL6nOlbIYIpnkL513FDxPTa5hLO1PgYKgHMgjNccR00kxWqBSHuKYMVF4e5n1eBFVvVpa-IkTv1egmHBTYy1mImOX7Ss2IKMg5qiRzdzkWypVG5J-SSmt5pX8stD7QvI4ixA50BKXgFeJoma2NLtc4xQJRiWyfIP6IU4ChwxpJtoC5jD6FimnvY0gdUPv90xB_4UAWvL1-e8Fp_rhwdyf6Mc8j1NjXsdmuZhCmcQz8Xa-847dBPPGY3iqwHdLbdGMsilGtj7mhFXFdM9wGfWPyUhzsz4OHIKpcRlUVxIm-Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛
با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26925" target="_blank">📅 11:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26924">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jI89zspHFxI4v80M5383RXNf6PbxcYSzDo_Nqrb8WYFy4owvi49FSy67b_SGLyvXB32LcPyqROrFjfZZVtA-Te1ZzMogxkugOZZ636vRTgMxExgh2CmcwTIRGKh4QlxWVNUhDm8Qo6SCodeKIRQ-u4r93XvdIKBuqeizgT3OQDre2rsDMx9uMr4RJT4JYK9uC5-PIklgWaD78XDFZtsE5YusmUZ9rVbigRXD76ou1t3l1FPuhPDQKcgG0axEz4elfOyDpIrz284_SRGrmfvyo0msfa5vf1mfSvYiTPIJhuA4CQyt3tAgKtevwdaHeNg8iJTeV0VtntH_4X50wRZT3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/persiana_Soccer/26924" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26923">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99893fb77f.mp4?token=P0j4PAXLECrNwg1spxznVecbK4h-eAaVPevB-9iti-atFAUP7dehXMd1W9kDWmMB0Yos5FE-lbKFmdV879CFAcCAW11Qiji-BJCa5EB-MA_Xq6mm0cdm8FVOdLCKfM13y_JRV1rhOTGxjFdwCz2WDJikyHhONxodyvZasHJdRKPy5_jxJFb3hou3HM7vACel34juJpzrmVRqxKV8MMp_OG9fGCQQ5Gd4RLSWonJfcls4XRHoWMVyV86lnqfaEsSjIqVPhgCAt049u2ICb9d5AzQ6HwF3Z82rENTu5_Lz69_FKjs3n_3zgqIToWbHH9fsSGoC2GNKaJxeWm9h8OhRBwCbHFZVSw_7Zma9-92aK0-Cb7FXPcT9PTJZuaQioHVtWzkl1kP-8Ufoq_oHs9oizlYWKNDYeMPPfdSrzEuzZc5kWNhHoHzA8WACD_xfxedLTYns7nexqHEDN67B4d9lTZme8LsaR2i8R8l94a0Hwxtm41G_xGzoYrW_VxNOQOhiEzWBgadTFf0wmS0JmTBvIGWVVRnS3NSPchlLNEWFNiOCU13a1JfUkV26o_Aw1PNcWqo8LI7Q_hvsBw3vNCuLtfcsfbpRYKecnlkR7xOMExhHmwJOTM0G-3nJ7HUTYx9_wZse6c7Mku7jMhtKR1O-x-RP_sSNrV5foPQuMuyBRTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99893fb77f.mp4?token=P0j4PAXLECrNwg1spxznVecbK4h-eAaVPevB-9iti-atFAUP7dehXMd1W9kDWmMB0Yos5FE-lbKFmdV879CFAcCAW11Qiji-BJCa5EB-MA_Xq6mm0cdm8FVOdLCKfM13y_JRV1rhOTGxjFdwCz2WDJikyHhONxodyvZasHJdRKPy5_jxJFb3hou3HM7vACel34juJpzrmVRqxKV8MMp_OG9fGCQQ5Gd4RLSWonJfcls4XRHoWMVyV86lnqfaEsSjIqVPhgCAt049u2ICb9d5AzQ6HwF3Z82rENTu5_Lz69_FKjs3n_3zgqIToWbHH9fsSGoC2GNKaJxeWm9h8OhRBwCbHFZVSw_7Zma9-92aK0-Cb7FXPcT9PTJZuaQioHVtWzkl1kP-8Ufoq_oHs9oizlYWKNDYeMPPfdSrzEuzZc5kWNhHoHzA8WACD_xfxedLTYns7nexqHEDN67B4d9lTZme8LsaR2i8R8l94a0Hwxtm41G_xGzoYrW_VxNOQOhiEzWBgadTFf0wmS0JmTBvIGWVVRnS3NSPchlLNEWFNiOCU13a1JfUkV26o_Aw1PNcWqo8LI7Q_hvsBw3vNCuLtfcsfbpRYKecnlkR7xOMExhHmwJOTM0G-3nJ7HUTYx9_wZse6c7Mku7jMhtKR1O-x-RP_sSNrV5foPQuMuyBRTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
چند تا از شوت های روبرتو کارلوس رو ببینید، زمانی که فوتبال از کسب و کار و پول دور بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26923" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26921">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQXAIrdyKLTDnQOtUApBWklXeQR5hi46hPdiaeTf4OPdNby15N0RT_5fq8JSLIQ-ogKtn-2q4SMXRKeb8gNdQ7stm3w89gE5RpXK7Ir57QqxzT9SnT2vLdpupaWdZFcneeuXlD8-ioJ-xziYq9Bu0j0gB1FMzYQhDjjy0WAxcUPtBbixhbMr9rqYFqUwBfGqEK-adL3sKbesyDGQe8ZONdwsWyNUKqv4xXIiaXNixfh1SiSN-y3G-CQmeqME3t5r1_sNnuJQoWdxA_mfliQj1C5n1uz_IxCNvzUksSeoRgilBngFNlf_Gz-DgviZgFmuaxr1_QjC2A0FIh0EJr3oIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
ماتیس یایسله سرمربی 38 ساله الاهلی‌که فصل گذشته این‌تیم به‌دومین قهرمانی آسیایی خود رساند باعقد قراردادی چهار ساله به تیم نیوکاسل پیوست.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26921" target="_blank">📅 10:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26920">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aS9u8QKxGZjXjbn-JZYXqJrb726_7taeLv3V9ZEPkcVJi7DQvCEfQH5NhoWhE9BSjP-FFTd149weXW-k6HrTKI1U1TjeiEYiu2hgcqLmgd_3z6rUaKF-LKt21qiWuHxlxdJRoZ2GZuQ2pvpiU8xxs6o6oWiTHg-ttKa_W8RGO8Omo4MdqIxN0Nec1MzjTSRwYh9Lv_a1F8z58N3tw7rbCWfug1CSL-VNGPCOhHtz8I0OSCn4PBk4izogd_adVNv8UFL32h3yKetWnRjrzz14ZTPdylqMHA9HAc34Og_7USZ6lLhgGEvfM54ZMotjsJdaMpzuuFb0cLJmyjei90Nnkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/26920" target="_blank">📅 09:49 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
