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
<img src="https://cdn4.telesco.pe/file/C8mdvrnepZewpqBIVOgnhrZ_eJI9jRG4D03fKEnqKY-EZeXUzVBWOe4s9alUCZ6r9ps46iim00Ep6h4-NGqzGobqt1AnARsZZ2KP6tti0z0YMXcu2xY8PC4ylW35YyzzVQGLF6MFnSYKYrrz4EvC14IT45-IWi8HW5grbl77g4rMsrLPprUU54g6BbA7n78OLrfacsUHh1cJbr1_WrfLQohkEhBkji3YyWvkosDVwIoxnkwdJdTVZGE9hp7Cl-l2HbpQB573BLBRpzP45Alp1KJsVxAkwJ39QKLW_z5VqZ2lDBLtBOe4DrLmxe5XnhIE8Z3NhfL_DRGMtHqgI8PMxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 482K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 15:29:19</div>
<hr>

<div class="tg-post" id="msg-30059">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUxcqUNZwEM5ZN_AHoZTZMD6AoW-ctJE0CDzafLzSX2aUHSFH0Ubc6GtCGZYv0ruezYefl-ufhkVBcDE7bvgaB4DebZOXu3yt1jtbss8x1j_QoX-u0qMHjaWm5enlhSy1NqMu05ux3Ff60RDxWv6k4bdsG5PIMK-6N8DyMWjKvKjX6mQ1x8edk7OGNmBmyw_zeWA1gzlbkFYJCpRgBRhoBWd-KIsAr-F-XAbx7ht6W36qU43oMOWLFQrK27b7TGC0E2irJEtT6qSG674axWzQyniPPXqpcYoDzg-lt96G-_pyV_Pdt7Gf6BsQk-uTTLCpx_3K6wd2-9ue7Xx7nSUHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
👤
خبرنگارت: بین کریس‌رونالدو
🆚
لیونل مسی انتخاب‌توکدومه؟ مارسلو: کریس‌رونالدو تا ابد. بنظرم بهترین بازیکن تاریخ بدون تعصب کریس رونالدوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 608 · <a href="https://t.me/persiana_Soccer/30059" target="_blank">📅 15:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30058">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C907D7I9pc6lrtQVwRWz9fla8xVDNG99Ww9uZt4qZiJnwYJm16a3T_EmiTjXDvQVXcLmmAYYK9zYbg815j4MfB7GioRUbb9kSaCBPpaCkR4gASI0Y_wQOVyku_UdkYcR1v4P7paVITiA9RawzmM2DYQr7YK7wOPibA_7lUVKbJ8Gzhnb7AWJJ0C-ipm0TEdQjkelm7M4IXAhyjGqFdoDiaBejOmCaBqSNNhgzWU1dlHeYDOxGbZ9YKmHAE9Gk3YhAmGuq-AzBrzIO1cLUSZNbYPep2DOO91a4nx4vEZVIswszdhTmGpiIokzMTwurdPHNsZ34n8O8tJ_iQkGpLXTsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس امروز مدارک جدیدی درباره قرارداد یاسر آسانی به کمیته استیناف ارائه کرده و قراره تا اواسط آبان حکم این کمیته اعلام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/30058" target="_blank">📅 14:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30057">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKS77uwWB9J97UPMoe3x49gxP41GlQZnGWSJSUQ4aO07Xh53-xVVAoABvFyloYkBMULO834NKO9pa_clSNCbpO4WOIXQ74U_RHdMHwL5ajnitFgeMOGOWNkyAfJb2n8DEqu5jh_eBKYPXrq-wOgnqAngK5B8DNDz-h3YZFUVoqwiY9k-W3EF4qfA3-5z6bIhWit2C7sDwiQ0FjYHvm1GZwCQ8oYscvB7acn1LptYU8GbcaNWN1OzwPn0CWErQv3jKLpTM9V5NQUIyUtiu_w8bMeIIQT3sG7R4FLUQaSParB5v3LCe4AOyLSeJ5J25-T175VmNlPWrE8tGceJnIQ6hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیانیه‌رسمی‌کمیته‌انضباطی‌درباره شکایت باشگاه پرسپولیس از یاسر آسانی و رد شدن این شکایت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/30057" target="_blank">📅 14:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30056">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGxUWbHA-B6Id5-eN2mQYk-KmpTdYfdsj7QYosevC3redE5dPcxz8xCNcojzHAo5AwErNp7IHcFaKdP7BXxIMwhKKB2eL8cOYa3wf8rnsxYvpJko5I3MyXsL_quFWat6WyEveRYDUBMa7vxSp92wCneFdZS3WXzAAsO5pdE4NRO68ps-8awDjDYMdsyHfehUCBIstQEBlJBP75hsBJnZdJXHBp5plZtIf4IeC3DL3Iy6BG5ibyKJIQFhUgMcNXZyr0ZOqQ4tAX8q1QJ0Js_wRPs_mKeWtKxHTg3vU2yLDD6V4jgRLFol2XpgV8tIjACyg_1rod2_DYLx8BNBlBE2Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛مهدی‌تارتار سرمربی پرسپولیس در دوهفته‌اخیر بارها به مدیریت این باشگاه اعلام کرده بود بین امیر جعفری مدافع چپ گل گهر و ابوذر صفر زاده یکی رو جذب کنند که انتقال جعفری حدود 100 میلیارد تومان برای سرخ‌ها هزینه در برخواهد داشت اما انتقال صفرزاده به شکل…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/30056" target="_blank">📅 14:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30055">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
🇫🇷
در پایان بازی شب گذشته بایرن مونیخ که با هتریک مایکل اولیسه همراه شد بعد بازی ستاره فرانسوی باواریایی‌ها حسابی سورپرایز شد. نیمارجونیور کیت‌خودش رو برای اولیسه فرستاد و باعث‌شد‌ بالاخره اون هم یه بخندی بزنه و چند جمله‌ای با خبرنگار صحبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/30055" target="_blank">📅 13:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30054">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMjFKqg-w-F_aIXryynWc1qpQtJ5n5ugAW85QdJc2j5-iyTUaQbiKdZvEbXkeWaGSKVjRRI-7gAwribqzLmjviOGyv7gm_qY-g1NPhx2sWWM9lCdC1Do_Q8JOxzc3i8N8ru2h86apkcPJlH4p9QYPyOtaSeVDJ7wiau1ZGr9BTvARFL7dgnhqSEvAzLT017b1CUaQ84pVewvMbRnpSFDxMKi_MUWYKCZtQ4tC57BoMJ9Q7kKWdo0lI83gl_0hzeMPPXfOHkjVBT8e3xGrfAukxo0keZLeppMObzj4E8fuTuYmnQmQRNDq7OEKvlnuB7VXEFL-Ll6nzRf2H6lGpyxDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇱
وسلی اسنایدر سه گنجینه گرانبها از تاریخ حضورش در تیم هلند را برای مزایده گذاشت! توپ نقره‌ای جام جهانی ۲۰۱۰؛ مدال رتبه سوم سال ۲۰۱۴؛ توپ بازی هلند-برزیل درمرحله‌یک‌چهارم نهایی ۲۰۱۰
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/30054" target="_blank">📅 13:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30052">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjvawPDppa5ezPEVDuBkp8chimq26JO-XRMVZqyZ30reRuWp1zjT6V35YVGIMqRms3zwv4rBJ-stKWugebnLlJxjZrwt3r0UxspAMkkjD-sytsl6Bo3kZDuruGB7LAPzGYjOf29ItoJ8e8Y62St-uEx0xqSagl48smOEATkgJ6wVHOdy_EeJ2azfDJeOsRLmv1vr_90Ku5B4qbeBQ_dPJXqJzP04PuPiE-mZ9qfF2q3juch382jvzn52DMA_SE36zybjOyjxAV2qd43f4wJFSSRNqTsihl_0STBsGN10ylejKTEYtqjiqZO86dtQmGwFEvIubyTeOUs7w--Ie98OQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5ef3d951.mp4?token=eSRhY-UZHAhV3fotEePrZUy6BbcQZRgHvcjuyV2izLXzroqMRYIN6hkd36_QUq0-QvYak_ABFYgUxBvyksm7d3AgvLbPHTQiNqUQ1AuOQ_r2iyhsF7yrPIyic3qaXJILT0bDrHt_btZa1TdqUPczmSjI9HHOgdNR_5wTfLkLJPNnUcimDaVNml0xU2eNn3MZ9fxYxwgeKykMsV2bla0aAJxnijcxtn5gG330-G30lWAQpFGNoyfm-yqvsDVDaPTkuIQL6q7jtSVx11yTXhSQoR0YbM8lD-mz-SuQNrSwXFG_OkoYxRIZdWPXJMN4iqvzvjWX2y__40G0B4UO8Kduvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5ef3d951.mp4?token=eSRhY-UZHAhV3fotEePrZUy6BbcQZRgHvcjuyV2izLXzroqMRYIN6hkd36_QUq0-QvYak_ABFYgUxBvyksm7d3AgvLbPHTQiNqUQ1AuOQ_r2iyhsF7yrPIyic3qaXJILT0bDrHt_btZa1TdqUPczmSjI9HHOgdNR_5wTfLkLJPNnUcimDaVNml0xU2eNn3MZ9fxYxwgeKykMsV2bla0aAJxnijcxtn5gG330-G30lWAQpFGNoyfm-yqvsDVDaPTkuIQL6q7jtSVx11yTXhSQoR0YbM8lD-mz-SuQNrSwXFG_OkoYxRIZdWPXJMN4iqvzvjWX2y__40G0B4UO8Kduvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇫🇷
در پایان بازی شب گذشته بایرن مونیخ که با هتریک مایکل اولیسه همراه شد بعد بازی ستاره فرانسوی باواریایی‌ها حسابی سورپرایز شد. نیمارجونیور کیت‌خودش رو برای اولیسه فرستاد و باعث‌شد‌ بالاخره اون هم یه بخندی بزنه و چند جمله‌ای با خبرنگار صحبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/30052" target="_blank">📅 13:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30051">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iI4H9mX3KYUktM4XxgxR3aJVLKxatbMilwWlijKE85PPGoL6x9cxAwHTpxaItORQfdM6KG3mxWQPp4xaEIXvRNP06kuYLmATUMWFkfLb1Av21rjvp_KiGCCq_J4HWWUWpCvnIrdxW1UZ_1zRtDh6n0K7T3zleEKe8VMpiuM6LIalgjMWbVL6S6NqeuFjUZVeerSanaNzuyhqTxrFovh3w_Iz75g-iY0KtpKE4gPORQ3bEhM0D2CiYN9WI6VZlJ7W5UBz7v1LI_cIxsU8zIr3M9bw_j1RSVlJgKIKEVtCn1o7uLP_Fj_9kvXzRUhO58HrWQneoKA8GSIWhzG4JFIfsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
هایلایتی‌ازعملکرددرخشان کریم آدیمی وینگر فوق‌العاده سرعتی‌ بارسا باپیراهن این‌تیم؛ آبی‌اناری‌ها برای جذب آدیمی تنها 20 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/30051" target="_blank">📅 12:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30050">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6111cc9977.mp4?token=hjJ_J6a0UdRd7DecaKceJAb2H7VZeva6t1ou6p6f-Gc7ribSfgb9H1qvfSJr_peXWE33CUibjxcU9Qs7SJgyIgYUQ0HJc29YQIyERu8BtBF8g9CXu8Fqic4nTa91T5y1Uj-Zr8Jm8My7mBlWwexL7Y2eNjAhuC280Qkpqi0EReu2Sk0A-CX3ycTbtPLDyguN2SucDvnAIbo8ng9Evp732oZ1qS6wuOZ6jVplqCdaKykmgK8nEerj24sER49tzkA4iWU0sMe3PxJDtogsN1ocyqRBZsi_HDIzWDvZ7WHhWxo_bkuggxEWA4a2K_s6zshKdya8upTjCXRBhacuEKTjhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6111cc9977.mp4?token=hjJ_J6a0UdRd7DecaKceJAb2H7VZeva6t1ou6p6f-Gc7ribSfgb9H1qvfSJr_peXWE33CUibjxcU9Qs7SJgyIgYUQ0HJc29YQIyERu8BtBF8g9CXu8Fqic4nTa91T5y1Uj-Zr8Jm8My7mBlWwexL7Y2eNjAhuC280Qkpqi0EReu2Sk0A-CX3ycTbtPLDyguN2SucDvnAIbo8ng9Evp732oZ1qS6wuOZ6jVplqCdaKykmgK8nEerj24sER49tzkA4iWU0sMe3PxJDtogsN1ocyqRBZsi_HDIzWDvZ7WHhWxo_bkuggxEWA4a2K_s6zshKdya8upTjCXRBhacuEKTjhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
سوپرگل‌دیدنی‌فرانسیسکو ترینکائو ستاره الاهلی بعنوان بهترین گل هفته لیگ عربستان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/30050" target="_blank">📅 12:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30049">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlgwwVSknJefbxru4lAWI5GxVBr-NPlHfjsGDcX5chIg3_gqL5Nqmn2rulDSKEmSjF93y9kpeAmjU2VcaL8__Cg7tQsrHbRm69sZ6BWq4epAT3O7_j0erMcBkMw0alGoJQCC700rdu2yo_xdgAOavAs3IDOmbUs7__9LgJGO1LpmY8NKC86ESWJ-L-Z6B5R9TE2liBFoWs15OJn1TeSXvWDzI_w32-D2wQ52KrYeT6hVWCb7y7XSRPDtLGWjl31s85jMjwMdWzVI4od2hkuR_madZMXMntD9CLJ6KjjhJpTeyrSLNZrqp84FhGoThgqT8M7wNktu7Nz25xTODWoClA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آندرانیک تیموریان دستیار قلعه نویی در تیم ملی بعد از سه سال کار با او از کادرفنی تیم ملی جدا شد.
طبق شنیده‌ های پرشیانا؛ در صورت موافقت سهراب بختیاری زاده آندو به کادر استقلال اضافه میشود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/30049" target="_blank">📅 11:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30048">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVH8cgpkgihcvu8smJ1TGjDwEiJgSwIjJMsgDSXsIZ_2cP_wsiFXYn5oM2RPOb1hM580O5lkk-fJWtQhtlbI6jSLH2Wsgj_Vg4JNXPQCp6YFj35UXkVmEymfXPHyOilJt4-4Q9B8aapkd7YpXII6DE9tD-Ic5F23HGdLivDWJQeQkrEc-T-sB30g0cSs-rKZ2z5aZ4Z2l00gOVZll9cVjuOQ9lk8qxCSHZfUdgz8ffvwIH8rgwHB-mvylLvSNVI0yrMDcSAKh3EgeVAmozIrwjrymLoeryy9eqovwr6Act9GYBjGF-i8pqyW6niEFPuh9o9SFsEm3cjRadnztskISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جالب یونیون برلین بعدِ گل هفتم بایرن؛ کاش این پسر 19 ساله بارسلونا دهنشو ببنده! کین و اولیسه امروز واقعاً روی فرم هستن و ثابت کردن که شایستگی قرار گرفتن تو جمع مدعیان توپ طلا رو دارن. واکنش اکانت بایرن مونیخ هم ببینید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/30048" target="_blank">📅 11:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30047">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kChq9aAdsNXQjX7QmuQ09hXMi6lGo9Epf2CjtsvD092rWn7uY_qGiN9AMDwCq9HgoCQYPHeiR2aEJ72WScbUOX5LCnGViIA1BxbTBOlxU9CBl0hctniT-VtMVamaAqvXCu6b1Pr0o-VP2yKpHco0pHSzmIt8JERsGNIprYaCUcXITIrJD5zEk-HAItmWUrK5gWaL3qreKFiUbA0OiQd1c4DOhm7hApNrUojvZq3IKlXbtPv7zquoawZa9fzGZCAWuRGiZQReIfu_f93CIMJ09wd62wfXML2rPQu_R7oPSm037Z294Lwu6Fj1RN3kYepeuKe7y88HORo0Y6zqrOqp5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
یه فلش‌بک بزنیم به زمانی که ژوزه مورینیو سرمربی‌پرتغالی‌رئال‌مادرید برای اینکه خشونت بازی پپه را کم بکنه. فرستادش با تیم زنان تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/30047" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30046">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Joc4HbUX4dC7Rtsqbc1QaDKQ5b5Zk3qemOaBE2nDlVz9K9pEurVUp-94Fv1je-mSSXNcUUsqneDEzkW0G0OK23oysoU59N3Z3izI_4bwhnlO4uhD1IftdooKc229kap4wrtFdao0BRmpQvPLbHdTnZnZ1sigbBzlQQLKkUnxRuSzXZZqjEqo04E1oUUoT0NelgjLlNOPNiRmt5dtDv_ptowLMP_58E2_I5WgJIRU9WiJQEKvEsoexMgSBoo4t4LIC7Icg72XV2P_dI-CuHAsIFFgtUIYe9CU9jc7utdAAGwrcULTKRe9N4130a_H5wj_gjP-x4rT6JqpfGg8OLpCcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کری سنگین مارسلو ستاره سابق رئال مادرید: خودم به تنهایی اندازه بارسلونا، چمپیونزلیگ دارم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/30046" target="_blank">📅 10:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30045">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIX4MF9cOxZ_iHRv3ZZgztHudlRXQioMHp3AzT4M4jfRUgxdndoBUPYgwtaHPYSO2fEMzz_Msa9NT02tNL02Fnm5ciOQGVMqJC998fO1t3ny20kYdyBLozmS2XDkd71qlAZtYGPEfZ7w5EpVyUVRhaZHXjWN6k_AQ0Anx45IqpK6gi7r9dpvWuBjpkKY-__72s15WalrwX3WMwDgLuD_w9WVTEigYOPuuxnBoyo1a1XbdA_Y6pYkqk0lAfRHdW-YP-Ow15muG-y53Z-ZT56rSiwESOYNc-4ZQ6gHR6yGphpiMdOMNXEUcCcqjuxwiCsdNK5OvYqLBeXu8ARctzwiFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌تعدادفصل‌های‌الکس‌فرگوسن و لئو مسی برای رسیدن به 49 جام در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/30045" target="_blank">📅 10:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30044">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUQiYyBFnGTJUyEPFo2XtKTLXJxNfqBybd9h8A2qxyjMSq5uq3fGfeVzPVkEBYYPjAiT-APbMU4pWiK_9TbuSIaZK9e5iZiTHfLUlqOgTtmu9obz2DikTvixzuhCjwcrVNbqJ30TTdJ9vhRXE5nQTK8yfsxj70uFvTaVaqcBkRO9aqPtM9nXaI0PcQjZgD4W3ma1sO6245TBGmSAEK1wmbPVvshJI8gT-KKyvlB7GDTcbpNkyx6hdP7QTS8p7LGC-iupbmYvBolyGmlNY0nCrHMFqIjf9xX0MpMD-dP9P_ZLIv6FVbYpvbU0fKuf7JWjk7_KcNOTFzknMDneUeQ5AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🏆
لالیگا اسپانیا
⏰
شروع بازی ساعت 22:30
⚽️
سویا
⚽️
🆚
⚽️
بارسلونا
⚽️
💯
اولین واریز، اولین برد بزرگ
شروعی هیجان‌انگیز با
🤩
🤩
🤩
🤩
هدیه خوش‌ آمدگویی ورزشی تا سقف 250 میلیون ریال
🖥
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با روش های ارزی و دلاری
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
باهرواریزی
🤩
🤩
🤩
هدیه ورزشی شرط‌بندی میکس دریافت کنید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r28
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/30044" target="_blank">📅 10:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30043">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a5244f7f.mp4?token=vQ7yeBS2-jAzgamBPr0nws3maSsvAPt3UQkjW-hozqsBPqVivwlXpUPjsnRMOPNzDavlxXpSXO1LcqLdqkACXXRhb4gpXNf3LCLpwPqji6LJqp_vgVnNcc8OhPQ4reVSQP6t2WFVuGCW6aoGCBSv2VJE8poK8OYU-0IOt7tfUZJE7vJWIFSeqdKti8rTOlr5FSxO3BIFuFcaiqt1qFhQuGrhMtNkTFFqonFmShFDcdy3OyXbhQR5h_jpyVhoAznKKTnhUvqsURi6XMO3nMuUZ4LOpLtfyRDoGaMEmr-TvsOnOFIs5wU8YRnqhvh3XNAuu8F2lMdm8Ij-DwYQVXAO0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a5244f7f.mp4?token=vQ7yeBS2-jAzgamBPr0nws3maSsvAPt3UQkjW-hozqsBPqVivwlXpUPjsnRMOPNzDavlxXpSXO1LcqLdqkACXXRhb4gpXNf3LCLpwPqji6LJqp_vgVnNcc8OhPQ4reVSQP6t2WFVuGCW6aoGCBSv2VJE8poK8OYU-0IOt7tfUZJE7vJWIFSeqdKti8rTOlr5FSxO3BIFuFcaiqt1qFhQuGrhMtNkTFFqonFmShFDcdy3OyXbhQR5h_jpyVhoAznKKTnhUvqsURi6XMO3nMuUZ4LOpLtfyRDoGaMEmr-TvsOnOFIs5wU8YRnqhvh3XNAuu8F2lMdm8Ij-DwYQVXAO0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین واکنش امید عالیشاه به فحاشی ناموسی خداداد: وقتی گوش دادم. دچار شرم نیابتی شدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/30043" target="_blank">📅 10:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30042">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIhv2dx0Fw3NnbWqO-9bnW80jnel5UaHzLQztHKppzKzNFgZcWkQ1XLpLMHm3sOiP2aLS-Ons-bMUfzh__02eVCiYq0keDQ2csFCXeuCyix3ZTG_lRsPJd0g9Moley2VgezsVzv_mPB8wjzHUk-sA68rjgyh1kZtyJXBnTJDbf6MUbHBSstVr0vr4-PhXKN9E_HibExP-TMw0jI3M07a0s3812nOhmP6uTGGgws_QiFmElPV_Na6o8BV3z5-REuElrVSIn4e9dOkpzx8O2nqQQg-zhBsUvROv-yTAx9K8DHo6YYGnkoJRgv_DSZg289pBOVmF51gTJ5Ba4ccYZ6agg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
🇪🇸
🇧🇷
ادعای نشریه NC اسپانیا:
باشگاه رئال مادرید بار دیگر مذاکرات رسمی خود را برای جذب عبدالله اوزان ستاره 17 ساله مراکشی برای رقابت با وینیسیوس جونیور ستاره کهکشانی آغاز کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/30042" target="_blank">📅 10:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30041">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwgYD3HdLxrwn5dE04TIYsQSndIZZKVpyzEZI_ZhoDCJwyuvTAA0U7vNojxcxR_H9FowBDHUe_o02jUFr0RUTxW6DfqN2-EOrAfSMxanqP1vYaNJ_AtPOIfekcN6EPeaBDQsmqAgJ4m-HLG6NGJLCVO3nXxru1PN2Mk34anKTIB7uAW0AoRYC4k91kSZka8uiEM1JkssmnCpQvSEPbYdElMXNVpmJyZ95iLJWzNeCdf9rJHl3PdB4GTpNnYGD23PJNWJEFPfvQ0SfwWjurbQQ56-nSvL_SPK68TsfxW89wj2ky8zvKfmuAp6MgzCn6L6LJBNEPjRlWjddd_BqDdq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
یکی از مدیران باشگاه استقلال: محمد خلیفه و حبیب‌ فرعباسی دو‌گلر تیم‌استقلال هستند و فعلا هیج برنامه ای برای جذب گلر جدید نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/30041" target="_blank">📅 09:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30040">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjlVuBBMMW1HgTiugD0sDRvq-m9ZPkHV8Khk7-jOgVWN2DIH4OO75hnih2A01WmxdlFA3vow91TXdIWjvOcNHZZaNzJvY8Q-WZRBc0TX6_Wb64FWPeO8mlgHhEE1DtVQRdPUTrUQmg57hLdG__fOw1SiwjIgUnKXSlHV3M6rVnAcDG7uiA1E2qKDMHZLL_A90MXHc2TUsl1r7Ub3ENSulbAKOMkn0wSkGTj6efPyDjeFU9hhpMm7-LEMVq46jLNjkmULSqmaEXN4v-q7qs0BEWSOllziWZCFnYGXG4u1m5SSQY8q8LTiezxXDcutpCj-CjSHl1XlhjI7wDfGpI1XJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ محمد قربانی ستاره‌الوحده امارات امشب دربین دوستان نزدیک‌خود گفته از وضعیتم در الوحده راضی‌نیستم و نیم فصل یا با پرسپولیس قرار داد میبندم یا استقلال؛ هرکدومشون‌پول رضایت نامه ام رو پرداخت کنید مشکلی برای عقد قرارداد ندارم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/30040" target="_blank">📅 09:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30039">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135cc26708.mp4?token=MGwvazXaOTO0J1gWrJAXAsaSDn6GB_X3f9KXtPLCmXSGFeUah1t8WSkPfpfewpm98C8JXXYqdOZrs7UgQ6lXymQ0ZRBdKNfGSH2PQd4d69C4XcqgWhVtDcAPioTWEIozlDMkmEWIBpIYvBxUFci6_qDV04QZLOmOyy7CQiLdhHhysWXh1nHV9X8AlGqrvR736HoDXlb6i-OfWAMU6T_Z0ldEg6E9TxCGOB7iBsz7gtT51Z4GbtOyaM68AqfJ2-9NRFu80XEPprhe1bHH4aiIAeTfXiXaClGUnXdttOWObn5wqESXc_t3EXY1u5UxEP9YNLrh-79e2tOEicFBTPQnuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135cc26708.mp4?token=MGwvazXaOTO0J1gWrJAXAsaSDn6GB_X3f9KXtPLCmXSGFeUah1t8WSkPfpfewpm98C8JXXYqdOZrs7UgQ6lXymQ0ZRBdKNfGSH2PQd4d69C4XcqgWhVtDcAPioTWEIozlDMkmEWIBpIYvBxUFci6_qDV04QZLOmOyy7CQiLdhHhysWXh1nHV9X8AlGqrvR736HoDXlb6i-OfWAMU6T_Z0ldEg6E9TxCGOB7iBsz7gtT51Z4GbtOyaM68AqfJ2-9NRFu80XEPprhe1bHH4aiIAeTfXiXaClGUnXdttOWObn5wqESXc_t3EXY1u5UxEP9YNLrh-79e2tOEicFBTPQnuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌سنگین مهران مدیری درقسمت سوم مرد سه هزار چهره درباره فرهنگ سازی تو جاده چالوس!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/30039" target="_blank">📅 09:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30037">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac719facd.mp4?token=FRaXTZF80vi6sUqFqsil-_uSLEM2iwPY0klFe23UF3UH5n9IpUX2LCBNpK0j1JvKjBaTUog1YZqCTj2jNms8yHXrJQx8u_Ak_MRkHFeYXktPtXrzfsh8OXL9UGnGpBAVRx4jYRLTsHfdPHANH3dqY3aUIT3C2q_PmJ94EYSGM5c4eSTFphtp_0uRVTj6Khk9DCpbarcIuv2RUUbQO6uTm1eFbI2ua1KHoyab7SQ9_syaQ252q5lds5A0niumVzOT8rrNXVCKdstrC_eGuMeuywDKvqPkIZaNffvAx3vBJFDeTsdGwdDRkDzZWh2LudN82tnFHcZthRo6nvCZG_v2fKR2_T8LfUKZj6erO4_ePUjOhFGIkQ8yMUowRFUPSBz6hLj1sZrDxQ05YbkkBKtwuFp_6TDjfKWKuDsx7J5RI-6BhU7IQS-9bcZtb5PLm2LTj4M25GGKU4otO5ly4OJtuJPx-wodGeCamrzIU6vNq2ranBCel6I01kQLXYewINv4DirZa8Iz_rNB-02QVVQ2bFgqlvlg2TU7xvAFa3qmYqr06TLttzvCW_AcF0SmZApfEzzeyeONLGTPFiY3tFMn-Z8Htv43vxpFYy48DxYABdYS4w2c_jDqYwrvpaB9wzHqWxnWMlabMEX9tWkIpoemhrKl8WmXawF2nTZMaJiv62k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac719facd.mp4?token=FRaXTZF80vi6sUqFqsil-_uSLEM2iwPY0klFe23UF3UH5n9IpUX2LCBNpK0j1JvKjBaTUog1YZqCTj2jNms8yHXrJQx8u_Ak_MRkHFeYXktPtXrzfsh8OXL9UGnGpBAVRx4jYRLTsHfdPHANH3dqY3aUIT3C2q_PmJ94EYSGM5c4eSTFphtp_0uRVTj6Khk9DCpbarcIuv2RUUbQO6uTm1eFbI2ua1KHoyab7SQ9_syaQ252q5lds5A0niumVzOT8rrNXVCKdstrC_eGuMeuywDKvqPkIZaNffvAx3vBJFDeTsdGwdDRkDzZWh2LudN82tnFHcZthRo6nvCZG_v2fKR2_T8LfUKZj6erO4_ePUjOhFGIkQ8yMUowRFUPSBz6hLj1sZrDxQ05YbkkBKtwuFp_6TDjfKWKuDsx7J5RI-6BhU7IQS-9bcZtb5PLm2LTj4M25GGKU4otO5ly4OJtuJPx-wodGeCamrzIU6vNq2ranBCel6I01kQLXYewINv4DirZa8Iz_rNB-02QVVQ2bFgqlvlg2TU7xvAFa3qmYqr06TLttzvCW_AcF0SmZApfEzzeyeONLGTPFiY3tFMn-Z8Htv43vxpFYy48DxYABdYS4w2c_jDqYwrvpaB9wzHqWxnWMlabMEX9tWkIpoemhrKl8WmXawF2nTZMaJiv62k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌مهدی‌مهدوی‌کیااسطوره فوتبال ایران و باشگاه‌پرسپولیس‌درباره‌پیشنهاد 2.5 میلیون دلاری باشگاه چینی داریان که به آن پاسخ منفی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30037" target="_blank">📅 00:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30036">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIFBKtHTRDs7aU_1KvoqQSHF1cacWu8hNvj_Ez7UcKXU3Tr_3rZ7NprCr6hxGoFwnMw728UBI16-b8QDde_7d5b8Ktq-XUtLnsQ9fWHt0tynxnC2jz-yrF_Ift4-tTw5IDBirpNRYFzJTf8LTdie-7WmXKhd5yeSdPcWJs3ByTB2gU2XdYeYaOTnwP2eFE5wbqfGQRkerY4Hdh0RvCToF-CGoqmNTW65Y9zTZYd8orzvmsQGrr5AcB_OC6mUwCisAn4ZhBrylyn6khvvcgVLNjVYPpfxXR21VWVlrsgtFFOsGGXfJCeVTJA3l0NhowCF7x0KRuJV27GNJpErWsEGdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ دوئل‌تمام‌عیار یاران دیبالا vs لائوتارو مارتینز برای صدرنشینی در رقابت های سری‌آ و مصاف تماشایی شاگردان فلیک با سویا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30036" target="_blank">📅 00:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30035">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJoSAL7CgUIDvFGkkEZpKgCyoB36xI9zqzvn07ESZbMXAFY437U8L_ZjZpzt8g1Wyod788l8H0vXBLb5L7ZA8izwSHiCeXAtuBJBxZA-7SnHuNaSLaxg07zFhfnIQT7kbdemhhGY9qNcua_YrMmA7b4gTTeYBfgV76BYESI9zMWA6yJj1ht8jyDYewczJx4VT3g1g13Og2i04_m9KRw22PKHmtH0jFNVXifzBiaQk-BHRiMjgGS3BH-vIAVfvU-jiqhC4kD9riOoJwhh_d9y17iFHCoq-5awVNJXEK9u69PtUGIe9Q9N3bZQEECLjpwXTkFUa7QuuNu9NfaIbSjMig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از نمایش ناامیدکننده یاران ژابی تاجشنواره گل‌مونیخی‌ها درشب هتریک اولیسه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30035" target="_blank">📅 00:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30033">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
#تکمیلی؛بهداد اقبالی مالک‌جدیدتیم چلسی: از کادرفنی‌حمایت‌کامل‌میکنم و هرچقدر نیاز باشد برای این‌تیم هزینه‌خواهم کرد تا به قهرمانی لیگ جزیره و لیگ‌ قهرمانان‌ برسیم. به هواداران قول میدم چلسی رو درآینده‌نزدیک به جایگاه‌اصلی‌اش برمیگردونیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/30033" target="_blank">📅 00:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30032">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUTi5mX67TmHAhdSa8VRDnECWQniUkGU11hY8us44zKkBFjAqNQSMH4EfkbqKMWIIcfbOL38zqKzd3uNy5qOY10EWjHs0xM4DuvT_V3J0wjlrNSN3IT7gTJxXQiqzS77yL6OzK-S5MYm8a63PiuOi-qk5mfttrd7ru-aQEiu0lTJ2ksIdSZaqE1HyUTAuM5IM_GC16Fsi9-vIRoeS0Nj3hDIzW60N7FwdPHFkzqJyBO6sdOXuZErXxNxuxwaugN4YvKQsczN4RJM1DmfLfu-I-MxiRsUavCQ2QOQuGUPEJvaUczG0BRmrHBxWGKPXF1Zxcn8bC9lKNClBxmDsYQjQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال: دوس دارم در چمپیونز لیگ به رئال مادرید بخوریم. برای‌الکلاسیکو 3 آبان بی نهایت انگیزه داریم و میخوایم یه نتیجه تاریخی رقم بزنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30032" target="_blank">📅 00:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30031">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی…</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/30031" target="_blank">📅 00:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30030">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hr3Vkaj6wMggIBRphdxrOXBGo0ygUHnRQCv60AlgJUcLteWWe6Eu18I-niG8lUeyJgnpB-1PsBMEcmFtw5UCDfyIy4Y8i9RM3PjO_bq3vlJr69P3_wbjBV3yh0I6sZH3Q0-6HAn_35stO1jZr75EKn-wxpnOylRHOR5R4lSLH8x9V87dkpCZwIViKYYgRqDiGtNrszoiUpCcUn3RZbrcbPuVRxYIAhNSMZt5l_b3zAzJgp98TAYduG86IQriDfXgugX0OFqIjkHBOn71aWopvD3HeT0veEaiimNk3mbDvfAs0SUJf2lVAZNuD9dq09q7z6bBDU9iizL5sfxSf7C8aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سهم‌یک‌امتیازی‌یحیی و علیمنصور از هفته هشتم لیگ‌برتر عراق: دهوک‌مقابل المینا به تساوی یک بر یک رسید. الطلبه هم با الجولان 2ـ2 مساوی کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30030" target="_blank">📅 23:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30029">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rY3yhPGSOuYqPbSll4_o8XNtzbg9od_eROi5c1YKkPwmVABHyOk82pivbHXDrfoSO7z9xi0WFqoR5Mn_FEpKKEh7eSkGy4oUFuTactw1wWBAynHQTf9HNPDZVhfLIuz5N9IV_A4ENJ6gcJMVAN7PAa8vXdtUjyVNRxi1VzngnCgmgAJB00GH_EpJeuFneSmcqKHq-LoZo7t5eQCof4MHLHDr1Nv--zsAko4mcYvw1_SZPnC4OHbmVeBQs2jPEj_0Nv_W5e_YVvgaSF_5wPx1HgEHcx8HBMlLvZXGLkDNsrUJlMVEDrmVWzJL1slh68FsFoPeZm7c3FnF-6r2_AOfww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج دیدارهای هفته اول لیگ برتر بانوان؛ استارت پر قدرت استقلال، پرسپولیس و سپاهان با برتری قاطع مقابل حریفان در ایستگاه اول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30029" target="_blank">📅 23:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30028">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5df38636e.mp4?token=BO8pDdt3oUbUPvNduNTpaJ18cOKKh2b8k6yfQn_dZcxz6GOQ8nOlNAhDkPCVIWRB5HJ_VVOgkrFDO21aKXokIKQD_f7xEvisTaztTdqkfukTcXRvFCXJfQNzyjh7jR7tYWeeVAlo_0pkdPXJqfJeKC5H-P08gPy_EXv-9i8ulLNtNMA4SfQLXTy4MQqmtaHKW1RrzJtFRjW6QCaSqtyXcEQIjxcro3ghEbj9tsOD7QRUAdlBMR89Khqvc1tXBDu9wXFIa4eQZY-PgPM7CWq1mZt-A-lz2WzNE1n_8KjjboCKL0e0KoR0D5h5luGQLk3AOD8qGi8XXAqcgvOUqfU2Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5df38636e.mp4?token=BO8pDdt3oUbUPvNduNTpaJ18cOKKh2b8k6yfQn_dZcxz6GOQ8nOlNAhDkPCVIWRB5HJ_VVOgkrFDO21aKXokIKQD_f7xEvisTaztTdqkfukTcXRvFCXJfQNzyjh7jR7tYWeeVAlo_0pkdPXJqfJeKC5H-P08gPy_EXv-9i8ulLNtNMA4SfQLXTy4MQqmtaHKW1RrzJtFRjW6QCaSqtyXcEQIjxcro3ghEbj9tsOD7QRUAdlBMR89Khqvc1tXBDu9wXFIa4eQZY-PgPM7CWq1mZt-A-lz2WzNE1n_8KjjboCKL0e0KoR0D5h5luGQLk3AOD8qGi8XXAqcgvOUqfU2Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نحوه وام‌ گرفتن درایران به‌اینصورته که میبینید؛ تیکه‌سنگین مهران مدیری به وام های کلان بعضی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30028" target="_blank">📅 23:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30027">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4323ee05c8.mp4?token=q2JV-5K57btPTJ5NC_ItcAcx5fc5Yg_DKPboBa_1LrS6dhfRKmEZKhq9-t1hY6gxJPCfHJC2uMxgL3EjCv_uhV3Lb9KgRUx5Fa9nhLM_8W1fPSANSDAR15rc_qMayPZvhQIz5KNsHJoC_j_lNP3of4H-qYrLKaWKgw_lcISaZVFuJQBgI09hbTqCComTGY3txOJ9OjfxZnneNMU6xQkz-gq50aekFsOQbkxT94WPK6aWpWusJ-bX5g7tkVgNqZkAQIb9Iaqt7gfwp9qbvs8EWMn2ykuIfB4NlDX5a86t3hHq9O9mvrwHfhLb9GHIKoqmDMe6Q7kmMndYBtOO9HUlWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4323ee05c8.mp4?token=q2JV-5K57btPTJ5NC_ItcAcx5fc5Yg_DKPboBa_1LrS6dhfRKmEZKhq9-t1hY6gxJPCfHJC2uMxgL3EjCv_uhV3Lb9KgRUx5Fa9nhLM_8W1fPSANSDAR15rc_qMayPZvhQIz5KNsHJoC_j_lNP3of4H-qYrLKaWKgw_lcISaZVFuJQBgI09hbTqCComTGY3txOJ9OjfxZnneNMU6xQkz-gq50aekFsOQbkxT94WPK6aWpWusJ-bX5g7tkVgNqZkAQIb9Iaqt7gfwp9qbvs8EWMn2ykuIfB4NlDX5a86t3hHq9O9mvrwHfhLb9GHIKoqmDMe6Q7kmMndYBtOO9HUlWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
ویدیو باشگاه ماخاچ قلعه روسیه از شاهکار تماشایی محمدجواد حسین‌نژاد دربازی شب گذشته؛ تکنیک‌ و آگاهی محیطی حسین‌ نژاد خیلی بالاست سریعا هم تیمی‌اش رو در موقعیت گل قرار میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30027" target="_blank">📅 23:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30026">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eV7aAd2uP5jYYxmO3QM1wp1q5m5U-1ZwYJSS-kPwdpEOqdmnltUTRXTYJBbuxYulveV6BuBa7qHjabW1HPEL7pcTDtOISEnj_ozVo3UI-J5sm_DHAEgM9S0pHa_Ib6sCYi00pkjdXUklj32ttHpM-ALEUh9K_t67f3XnuwpuRFqkly5Q-qtJZfsu__hjhIa2DcedURb-VlMvSu-Xh6yBsPZfmL-Ul24fxZTNgpLAhTrZ7gruns2vbeSAxavG8oUKzBTay0-jAh_bwsHZARPQBrJwotUXlDqOSzhD8VoEndNDEFfPPwGMuJmOrF4GNm6Qvz9GM4dRlkxS5TVd7HGT9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ بااعلام مدیربرنامه‌های داکنز نازون؛ بازگشت‌این‌بازیکن 31 ساله به جمع آبی پوشان منتفی شده و این بازیکن به مدیریت باشگاه استقلال اعلام کرده علاقه‌ای به بازگشت به لیگ برتر ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30026" target="_blank">📅 22:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30025">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU3BG6Uu8eu_d9gH5W5nL4MJSAErKUZVodlaZVIjXZpjPyxFIr0NVAEFI82QGhY2rzZp3R3mwx-bwzzJ1NplgSYLSsBHGMJqmoV2oBHrenWue-J-rS0UZRc2euQo4XBkdFzjm9FTpIJTgPRzXhU31wV2v0MeZo1Q5nMmipdo8Rf_eeHv4Q4O0Z1earP5omW0lz95DnL3NT3OYW7JwfRwn0zSh-iZ-ZFFwx3uZxgejgG37GqT81vyVaDf_p-QMflXaeDQFK705KiXSXvE8PibBjlz9gOo2l7Z7Wwtd6yrYBro02B2f6-MZHG4CQAioZNooPA5Ds07X8eNfLednt_9xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه‌اتلتیک: جی‌جی گابریل ستاره 15 ساله منچستریونایتد تصمیم‌نهایی‌خود را گرفته و بزودی با عقدقراردادی 10 ساله به رئال‌مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30025" target="_blank">📅 22:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30024">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmDF-LTdqdE50ZLjzzpxKVr9GsRN5KBNzDOCnHITbU2qygY-KhiMh_nPYUkYwQaN-cuaH07BeMNh2SS4G2OtUqaJN3sr9xk2oOAxMAS-2mQizAlepuxvvB0-m7xNP_dDW0xIjaYNOyWzD9hrgBFJjj-HX8Z_JHxdipjlVYnq--1GpIrUcJEqB-4kF1eKtwFOgT_aiIgaRGALttD4sL563qzCmEgKl8tjsW70zzGjE7Pu5FTyGh1fMlTe37nPH1v9Lha4Q37lXiE4cQDKpgjyrBBhlEfl_i4sqVjg0y8bt40bn73qoUAPRF6Wq8GBcpe6uWUlj-mUrHfOgf9V7QOPvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30024" target="_blank">📅 21:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30023">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyVJP9Tnzv3M3ksfoA00wejTXgjI06wTuF86BKBwHJ-EpF67h8dABUbxYy9COXQeCAqXsaeccfhFa6jvy8pfOYq_6XpY54fdfwPdXx-qk9PiQwMDIVC_7_0LwIWdfdFsLMXeWvObW8q4IOTefFkQwioohZynkuQcmJ-W67-LILNwqsCxHQVe8--dljGkl_6J97ueRpiE7DHLIUadXXzOzDaNZEm1a8FgLiXWMitDr1ZCLUQJOs3JAOGrwhX05biUG9mBu06Ads3UUUE-5wiGzAlxdgOsnLIEoifKFww0rvOe25UU-ScODr5ljJOZRFTPVW5KcbyMcFpdgHdJK75BvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
خورخه ژسوس سرمربی تیم ملی پرتغال؛ کریس رونالدو اسطوره پرتغالی 41 ساله تاریخ رو برای فیفادی پیش رو به تیم ملی دعوت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30023" target="_blank">📅 21:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30021">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AITz_6TGvlAxlaf-YEJtBkFUrBEl601HUxxLKcjpIBJuRjhFp8JkspHFuMErX9xxbPXNBiLgdmlarctP88UIXRsGwsgi0HZn4qHzxOpNoWs7IW8viHUL1tDe4SLbPgS4sFwXT_Qt9zyC5Qq1zEl4l5EdJT3ALazgo9L7pBSYjj73-ae1OmFzRuJDbNaO7GbMB69A33GkYUlZ30Zr2NPjqbwEEVt-BdRAeIGEO5hhrk2uQr_0-1Ljq_gDKKUxwuNP8wyrDcvJntwVmNHIHgifFqRGjXx1tV1nkoz3u7D9teCZTW0DfNMqJjZ3dOirsd3awYtOm5Pqgd7oHmzDdE2JPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30021" target="_blank">📅 20:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30020">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🟡
👤
سه‌سال‌پیش‌درچنین‌روزی؛
حین ورود رونالدو همراه با بازیکنان النصر به‌تهران این حماسه تاریخی و فراموش نشدنی توسط مردم خونگرد ما رقم خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30020" target="_blank">📅 20:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30019">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWi7m8AN0vDxUhS3o-2Mg3B-rjSo4xDYJpMCyKKNWU-ixsx_tEosoXDtT_HM8CWq64Qom3II5CA3IGJZ7uI3QY0OI9fokY7UBwHDa3JzaWlr7onfwy1vjcGIg16yKHNRHbKQsObm6RFdCiBvtkt5IuOCimTuLPZFhIUSMk2ig5toYBQt387RUUgXRViUgEBOl-_ZtbTU-lXuQo42Wm7YPcGwnHrkKUc29JEPOzMtbDLWBDx9ssA8L4bWq1F5DWF2UGe6KHm7IKDj8lIrTvxTh2emEOuSafjOG1LE2cxEF8bkj3DBf5UrUjKEgMHTn0OCY5NOpmCeC21iR1XaWXtZWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری عجیب‌وغریب علی فروتن از سکانسی که باعث توقیف کامل برنامه فیتیله‌‌ای‌ ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30019" target="_blank">📅 20:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30018">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIKnJZk6N2VWB63MRQyO2HMrDLigdtgXZkMFLDezM32fmbyC4sI1c2zUF2p6mPbQphFyNwoJzvjuzkDfmaj_cD5Eis7OPrd3JAT5t0JPbPOIWevSqoj35RlLokdA4mX07jYxCa2W6Q9O5Fv3KSX_NUHgLfef1oywUZkxSlpf167JTYb01TcIiaP3QORURu4yp-5wKjdNgAKZamxieEVd4FGCuHAEy0AxtAJk8Qn7XwWNYakt4eeUcugUTEIDz7TF7voXsl_PUbNe2C3KhNl6RcyAMIQTUwT_sojP9VvDEc48Td0F7lFEisGoD4RxWyR56Ulbfxq7Z3feTU0jN9rr1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
فدراسیون‌فوتبال‌فرانسه؛ طی ساعات آینده زین الدین زیدان رو به عنوان سرمربی جدید خروس‌ها تا پایان رقابتای جام جهانی 2030 معرفی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30018" target="_blank">📅 19:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30016">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QRRAKVbeTt6r2hL8aE0ocUW_HB0nd7GWASO3rJ_AMpJ1pUeSSUiNl4IGNAkicvj7_bYGZlAdHje29DVlS8uABfyxH2VM4hkTlxm99SGUhpJfmGUawLxgi8H16iEwUwKJspJyvrroaWMi06SUpw4PXj_ZXfLnyD3phhJql76aizxnqNi74qPSaWG7pwDf8GFHHRlauZ-Y2-JoqpDgfdOv0RxYklzdnB1Rzd9QZc7lwFOf5qgw9UlHBCyFf-PtUX8rp8C8NMzcNz_l1r9qaoutckyoPYpmuxIA3VLCMBSMg97e1mcTQ0lJJQKOTRzrfrfOmz5u-HdBLIdNfZqG6Qh89A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rwTx5DBKkSTqsTTCDe-TNnreJPkUgTluGv0Q0kLy7yh04znAEm9KYthihWnBGhHsqh6sVmMZnfOksSPxOFVgvRG7EhXfGU7wOgO_jpYBcf30TjQYiHNeLDvvHlZadYqTAMd5l8X3nsoHBDxRoJ5JcBmRHIS2WwHhyQ5LMwmw_-p8Tykl0w6ib-YXG4iZSQI2PC_xqjDktMcQFl4CPKIwEZkRn65lNIFfamAJRRYxUnBqDrlfHGaT230r2qRBq5Vvrllw5NS_dV6uYLjxqaM6bodxv9iqv7UCozWSzBdRZQs1uPLkssXeGafNUFwUeW2zoC-dokGcdwR0zNoK2Tun7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نوزدهمین‌دوره‌لیگ‌برتر فوتبال زنان از فردا رسما آغاز می‌شود. رقاب‌هایی که به‌نظر می‌رسد با حضور تیم‌های اسم‌و‌رسم‌دار زیباتر از همیشه دنبال شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30016" target="_blank">📅 19:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30015">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a036b864e0.mp4?token=cNyJ-r9oQPmlZ7G9f_XpfZwhhh26KpRnMFbtDFexIfH4R77p_INUsQa-a5r8CuSR84jL6E_OhgA8vdILFaa19PB-8w_BujmLvSXjhbDZiAQ2zza66wqRDeDe_mBsC-dtG1ix1khvFNLjVrY1JrEgM5ZnSOxO_0YoNn4VHRS9lgGgpMaqlWelDL8pVIwrT3zAhZnc9BdjplApRWzCNQDbNsmzxG1Dz2yUWMbVfaUp_Qf5FicziUsBNZNrANo2ijKfNERTTKw6zQi72y-wfIGG3gAedrUth7w_zbvjv_L8S3agNHduzzYlAuHGI8o80I0gMPKHnyGOIY1OHRgdce42RT7ZOJO--TYNRbLiloOglFTfFo9L6vGe3FRUQ5ax50clgjQVSRwtxKj6iGAO47z9hlnBFCDNOCFSID2tUgdHUI9ruE0sNXzxAm_HtzKe71kchDKByNmlUiQg3EiOj9qYsnmV1CJJHbkamlvOIuBd3pr90Gg19F-K4aVL0Jvpno856yztfB4RnVbqBplo4k1vB4K0PZr6HRaWKDJSF7sn4NLX-5Og0dVMkn9nkdmhHSFEd2QQEUMbwDqIfVq3xLvxRBdcL9Ep_dIeXA-Kpivl2QfEJDSDteVlF7qgU2nreO1TyK8XUCdvpLaYDp3jcPt8nMMB9z7727IpLLQ3KZB3nF4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a036b864e0.mp4?token=cNyJ-r9oQPmlZ7G9f_XpfZwhhh26KpRnMFbtDFexIfH4R77p_INUsQa-a5r8CuSR84jL6E_OhgA8vdILFaa19PB-8w_BujmLvSXjhbDZiAQ2zza66wqRDeDe_mBsC-dtG1ix1khvFNLjVrY1JrEgM5ZnSOxO_0YoNn4VHRS9lgGgpMaqlWelDL8pVIwrT3zAhZnc9BdjplApRWzCNQDbNsmzxG1Dz2yUWMbVfaUp_Qf5FicziUsBNZNrANo2ijKfNERTTKw6zQi72y-wfIGG3gAedrUth7w_zbvjv_L8S3agNHduzzYlAuHGI8o80I0gMPKHnyGOIY1OHRgdce42RT7ZOJO--TYNRbLiloOglFTfFo9L6vGe3FRUQ5ax50clgjQVSRwtxKj6iGAO47z9hlnBFCDNOCFSID2tUgdHUI9ruE0sNXzxAm_HtzKe71kchDKByNmlUiQg3EiOj9qYsnmV1CJJHbkamlvOIuBd3pr90Gg19F-K4aVL0Jvpno856yztfB4RnVbqBplo4k1vB4K0PZr6HRaWKDJSF7sn4NLX-5Og0dVMkn9nkdmhHSFEd2QQEUMbwDqIfVq3xLvxRBdcL9Ep_dIeXA-Kpivl2QfEJDSDteVlF7qgU2nreO1TyK8XUCdvpLaYDp3jcPt8nMMB9z7727IpLLQ3KZB3nF4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بابک مرادی هافبک سابق استقلال: واقعا دوست دارم زودتر بمیرم. خسته شدم از این وضعیت!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30015" target="_blank">📅 19:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30014">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/595b48aa31.mp4?token=sfygSFtmHque8PN44bwQhRpD4ufaJjZDOx3O_TmVl9hc7Rk0FjDTfG2h61h5zroh_7oG3DVaO8mLjNNw1yT2gXf7gnky43tbcPvhoQjEpdBfH2qixGCrcch7DL_h-9hp1_sA7MPkoJ5epNiuff0KvqT66I8Kow-46V3TRTZBLYbM6Tyk6qZUm6XvuVfZmc787rl_UBbrwaupmDOGVKf3advPP6ygFfZeSbGm6ZvVOw5Lx-SK8QdKclt9Ph_llVSfZtQkY9BnBTnGJbf7KSvwa8CkaObsD-M60HDb6yEwGfst2PTI6Fm_-EiAdMqTwY8UQE7IBgiNudPjK67WRlx76bWxd9iGYsrKDRvRmztYq1P6b8S6U_3A3LHvG3mY3DxGCLl00LlJhFW0iI37t2KCpJHtQA2sTmd3EyfGuqKhYYW-dk_aRYT20PZuQt0BzoHQDn5dhwH9yZ8boBSzb6AWSbub_erk4rQ0WNL--8kbwFZORaGPQpnCLrn_UjCQotzeEg3mbB3IcZxpYXJFzCbi9dl63GflpWpXetCxBX59yVz-RfePhPJ8YEAuQQxs9NB1BOhrF5MGnq2sE4aAPNcNMHlyvIt7TTirvoS07H93hgkeBWv1uv8PsUIZvhKCjSwD9HZ4yaLRKgoxD70HKdl3YVkbPZVAy88GSaK8-Gk1hAM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/595b48aa31.mp4?token=sfygSFtmHque8PN44bwQhRpD4ufaJjZDOx3O_TmVl9hc7Rk0FjDTfG2h61h5zroh_7oG3DVaO8mLjNNw1yT2gXf7gnky43tbcPvhoQjEpdBfH2qixGCrcch7DL_h-9hp1_sA7MPkoJ5epNiuff0KvqT66I8Kow-46V3TRTZBLYbM6Tyk6qZUm6XvuVfZmc787rl_UBbrwaupmDOGVKf3advPP6ygFfZeSbGm6ZvVOw5Lx-SK8QdKclt9Ph_llVSfZtQkY9BnBTnGJbf7KSvwa8CkaObsD-M60HDb6yEwGfst2PTI6Fm_-EiAdMqTwY8UQE7IBgiNudPjK67WRlx76bWxd9iGYsrKDRvRmztYq1P6b8S6U_3A3LHvG3mY3DxGCLl00LlJhFW0iI37t2KCpJHtQA2sTmd3EyfGuqKhYYW-dk_aRYT20PZuQt0BzoHQDn5dhwH9yZ8boBSzb6AWSbub_erk4rQ0WNL--8kbwFZORaGPQpnCLrn_UjCQotzeEg3mbB3IcZxpYXJFzCbi9dl63GflpWpXetCxBX59yVz-RfePhPJ8YEAuQQxs9NB1BOhrF5MGnq2sE4aAPNcNMHlyvIt7TTirvoS07H93hgkeBWv1uv8PsUIZvhKCjSwD9HZ4yaLRKgoxD70HKdl3YVkbPZVAy88GSaK8-Gk1hAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
#تقویم
؛ چهارده سال پیش در چنین روزی؛
کریس رونالدو فوق‌ستاره‌پرتغالی‌رئال مادرید این گل استثنایی رو در دقیقه 90 به تیم منچسترسیتی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30014" target="_blank">📅 18:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30013">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUnPuzIftZFsLye0LEsI-4LuCHN1QmhRb0rkjr6T4ephGOO1oTlh7yvkFWzigHeUi9mp0fYn6FNutnkgpIcyHpe5FCWSvBJdsNK8fYlbqoJJ7bSxe6a7anvu_gIZzKpdJAkql-5dnpobGItnhZUX0iBAfAJUJfgxwdsSh-P0JhjyEsbxwVjGF5Whv1sD8ZbM2c9YLC03Rm9reje8Bfyk3Wks8t-CIcnA5HgnQ45j_2zsDDfQ-8qGNavoMx_OpKiVse8KfZwNFAiIJuGjmfjLhSF5alPEVInKoUowq3kWJabBQpNzeb8q-32SJTEeh-XQwXUvz62lO3ip-EvmExgoCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
#تقویم؛ سال1999میلادی درچنین روزی؛ تیری‌ هانری اسطوره فرانسوی باشگاه آرسنال این سوپرگل تماشایی و استثنایی رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30013" target="_blank">📅 18:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30012">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdbXCl9GjqDhllNmAGLJGSqD-1SywTaMFqsw7_5zFZ8LXmA0Nhsq5FfQwvJyovpKoGWSr_YrjGp4KKGm7yuLhX7dYlIp-PLYyUORqL0yIB9Lw2QZPo4JPr0baF-g3dl4oRV83eEJ6wXIw4mJvQta4LuMItVhW38QWOfh10dbGYor_xMLpQ_3QLJgSw09NwgRgFm4TjQb96cJZb738EkBSdoUIjB_CVudR6OZ9L5kkTq1_TrPnZBnrJ0bBtvb2uEh5r4etzLxVVuGZvEIVP5w1f1aRpLZtJWwxZOfOMzTgC9YcdSh-wAmlzXl1XQ1HtElJ4ju6bKAG5fVI2GLs5KJyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛ تنها خروجی استقلال در نقل و انتقالات نیم‌فصل محمدرضا آزادی مهاجم  27 ساله آبی‌ها خواهد بود. مدیریت استقلال درنیم‌فصل 7 خرید خواهند داشت که جذب قایدی و حسین نژاد اصلی‌ترین اهداف هلدینگ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30012" target="_blank">📅 17:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30011">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2GeHS20Zsk2CATjWeynR6vOwlmuVJ5tzAydx8I3EZs7Cw-kFAitx8kECXUKR0j0QQzUCpZLWZXfNffvfh7-_A0GqT0gy26zV_VfWN-U1BPf-jIZjog2yCcQP7oo1k0zNxFZa-zGsQxTS3XFduYxpVht2Tg1xnlG_J4yzbOKW3GWLPzm1wH93WR8Sll59wNPm4BVt9Ytcz3t3SujxYAx1k20S5WgMGp8vBS-6PqThw7CRCXdB_qUTaMIgX0ZrxFWgXYpP0DB9iN4M_7g5EDgrdC3cd3eYwwuYkR4muP02uUGIYLRUGVdSTDGgtCxwAyPQK0lNM-uqiNOrEbbleMnLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلزنی آلیسا لمن برای تیم‌فوتبال بانوان یوونتوس در هفته گذشته رقابت‌های فصل سری‌آ ایتالیا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30011" target="_blank">📅 17:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30010">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9586b8df2a.mp4?token=Msv8obm8o7SWN-f0KetvZWpqdhdSVS-Q66SQqFbRaX-PKiyWn2XKc_OCuqz9uSe7ty2IqMQ7rty1AMSIGMVkD_N56B6F1uNwYeXI1KQdkmcSVdtAKnWgOgKzGE0nHlvF-p7kJLKqadH7wTwikAXZiqxI41Y8RzMU-DvU1khuSLWKjqOTgdcW0Mi7eQQo2PJ58LtYFcSML_IDGHSBPVZcmsZzlaqItVsVxphsqHGcCYc201JExXZ-lAKHo68QLr1C1h89dp-wpesAD20pUbOQ8BhBGVv43azY5Mhg78cIsMXmCATE6OZlxqf-7SE6ggYJ13q6EkGTxcmY-cmkICFvpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9586b8df2a.mp4?token=Msv8obm8o7SWN-f0KetvZWpqdhdSVS-Q66SQqFbRaX-PKiyWn2XKc_OCuqz9uSe7ty2IqMQ7rty1AMSIGMVkD_N56B6F1uNwYeXI1KQdkmcSVdtAKnWgOgKzGE0nHlvF-p7kJLKqadH7wTwikAXZiqxI41Y8RzMU-DvU1khuSLWKjqOTgdcW0Mi7eQQo2PJ58LtYFcSML_IDGHSBPVZcmsZzlaqItVsVxphsqHGcCYc201JExXZ-lAKHo68QLr1C1h89dp-wpesAD20pUbOQ8BhBGVv43azY5Mhg78cIsMXmCATE6OZlxqf-7SE6ggYJ13q6EkGTxcmY-cmkICFvpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🔴
#تقویم
؛ سال1999میلادی درچنین روزی؛
تیری‌ هانری اسطوره فرانسوی باشگاه آرسنال این سوپرگل تماشایی و استثنایی رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30010" target="_blank">📅 17:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30009">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgDW85xd6QNjiMDXY6nfWrwYB-rs7beYNWOHb51dkc9XlaAP7bJRYojTeV8KWovoGdFyHkSCCxRi6sUzFXQsFYydkssFfapjc84LSEZYDst7TSUxVzzgTM_LceKh_AvGQBZukPZqbX9ga5oO3pCbZaeTP8QRe2PR5Jdb17_4L1lVjd1ifIPGIPAt_n7Qv7mGRAHqv0xOoHV7_irO80sOeRtp8Kp3ru7j0oNUIUenbg83XzwlHwwuvAvUAMnswQOCKqx-NGmOS9WPDc-xF5R7kusMF_58pMEj3YgLbZeRtXbkM5VlLv1hpBu197kf1Y30Iqy-gMVfUrruC1qc3L-C8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30009" target="_blank">📅 17:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30008">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656a3bfd79.mp4?token=IBxWb720vDv1GjU0HohMRYHrD9B3EQcwUF_efB3Gp1zSCY8lVFoCbOC8ObljK-392-BYYwtP6XFtixmu2kxZc3uINVr4Jqvs_hdl0xAr7PrubSTYdekDf3plKv1m0lPIShtcxqXBnGK1so9-6dBdg4qzDGrInFDXbHJubSvXf0IbwL46SWCa6JBkJEqX3JyNMBLlCzzRrsemx5CE9gKMp2UaavPw4Q3-MahSrXIqtQYAgTkLsM563hONTMAFm-4B0jEN0HNs-QbVP6xYnpV6KBhVC_2kbgM6IGohtLtSjSS4fooeXXFEgZ0av2sh7lIk2tY6bJKyscCd-L2R2OjQNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656a3bfd79.mp4?token=IBxWb720vDv1GjU0HohMRYHrD9B3EQcwUF_efB3Gp1zSCY8lVFoCbOC8ObljK-392-BYYwtP6XFtixmu2kxZc3uINVr4Jqvs_hdl0xAr7PrubSTYdekDf3plKv1m0lPIShtcxqXBnGK1so9-6dBdg4qzDGrInFDXbHJubSvXf0IbwL46SWCa6JBkJEqX3JyNMBLlCzzRrsemx5CE9gKMp2UaavPw4Q3-MahSrXIqtQYAgTkLsM563hONTMAFm-4B0jEN0HNs-QbVP6xYnpV6KBhVC_2kbgM6IGohtLtSjSS4fooeXXFEgZ0av2sh7lIk2tY6bJKyscCd-L2R2OjQNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروزصبح‌یکی‌از بزرگترین دوهای ماراتن ۱۰ کیلو متری کشورمخصوص دخترا تو بوستان ولایت تهران برگزار شد که‌ چندین هزار دختر توش شرکت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30008" target="_blank">📅 16:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30006">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bkA5YyDb1jvRSuo0FdSLSWPZpE_auhXa25cK5zlYfwUFj5Ns67CdtLYxZUOJPrgm1-Xq_GZPOxlXuEOZ4HQqNU4TrgNQz2v2cB09HUoe2p7gvGETBe1nxIrom20z6KGN6ynOfPtV6-9vBET1zSOxIIIo5x8lYNmXpQ7MiF7UF7KJWo0SW6EG7_aufhoMgCXmU2BAxDKsBMwpjZq_6mdxGrO5W00McroKki1o-Uds26rNEQBOAn3OKQa452X-LToAaDkBM8YbqfvOpOpeG_43Be0dWHVWkPnxz6h3eXsgSB1EATBireiwOcGMsQ9vGutrOOpFex83wMvYbZuf4JZSiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L7yW0yBsmyOsJMYIKu-0jqNEgZ1joy4KLDbq1Up4_drfxOyZNBW_jjCAhJpSCebHOgak5CEA7C0m8nLO9c3Jxh5YsaQQ3206o7fHiZArBW4jx6tVI01O4A8DE_-Vai_OgsDH9f4duQOcT034UK6JTWngr3ITmuGsySXIlMesaZylFi5vZEhhI3chWbfW_L8clGyTgwmHCs3C6TdaYhWaoIgC4yua4MLL6YR9KcTvqYyYpSJqc4H5jRU183qplroaMRKaqSOnFYYu80PFJ5s0IeH-J8eQMMV4jOU3KOYaLFzCPl0yguPRgd9UgNJSfayko9AJFu_BYZl9DyWbNKraQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚫️
#فکت؛ السد قطر تیم 78 میلیون یورویی آسیا امشب بعداز 22 مسابقه نتونست‌گلی به حریف بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30006" target="_blank">📅 16:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30005">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DreWb63YR3JZg4Z1CHuUPi6CJ_JATE93N6zG07BhZV2gyBu0ogw77aW4Ygf1y3FIDn193qZ_YSqLX1vZHnlVT4FRQ8GB_Jc9Yx7tzWj0GFenyTCKBcys2rwAhpX5vC1Ls9lfPwXSqnUzpnOMCrCBHWTx4keDjAlevlDWoYkSeijV4yEYpPDHQZnU4CLAFiowt_YtENWkCvY9DvYSM4_1lf23FCFGWNmH7iM7mL5m1ZvtO87QQiDA_SQYCyvmQILdNvA68tlTfV_6HXBEpr0YppO9c88GOyo4qX9wkt2dCU4zckiQaE9GXhKM_iswfihOeHT_OqsGVNGuf4Bx97aGwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#نوستالژی؛ یادی کنیم‌از مصاحبه قدیمی کارول سلیکو، همسر سابق کاکا و علت جدایی‌اش از او:
‼️
کاکا هرگز بهم خیانت نکرد او همیشه با من خوب رفتار میکرد و خانواده‌فوق‌العاده‌ای به من داد اما من خوشحال نبودم چون یک چیزی کم بود. مشکل این بود که او برای من خیلی کامل…</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30005" target="_blank">📅 16:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30004">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQKmaMPuzunZIZ8lJMoOkRx1Ar_g4TLxNm9VwDWsDem0ABTeLFO7chh8VZuKAXn243zP5vVY7hzl40xM9PTdz9EcS5yx60fQMhNrC9D_CxS7dYKbxmHnchk3KU2Dn-71j57yL9tO4amUAtyuYzfPKhnAe8BcfZ18yDlBLi5SZIKDS6ww8REkr2DgaV_LnUpsZoJDmsnJnuJen4Sea9fCWzHJI-ey7Ia_hzApv4zVhry_1qA8U77oA4XJj6Mph0JlFPtfozHrXVeAO13BhqLNn2CRHhJ2v6WBilOhexbWAwROF1lWEwdoACa6AG-IjwBz_EGD2ocoC1DUMwLg-qGmZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30004" target="_blank">📅 15:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30003">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yzhw--h7uix4EPJjouc4mOP0bPw1bLh4ze6b39xkx9dVMMx72cVzqY8LIuktoJJydTnbreOnUZusyWimsPM7aFtpJK__dIGo3M34zal46mbSCE6qeT5gr-da1NKSYSXBvrdlyI9-4qE2uprVJl6iXYdyVHKPTQrkZjbC7Z4V1ZnKHCc9GxUjX0JGAI_4FSIp0qpteYQh-pZK4m7_CMGRxKj6SotIYlSjkAy7MruUIKmUl47NLXvlWlFmQ5bBgye7MC6eNCi-TxtLQSY9Q6JFaWxfps2rfP-r_47SYkbyHB0khNrdEtAoK9mtpf6xX8UwNejvHmGCuSC2CPOyTidbMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مدیریت پرسپولیس طی روز های آینده و تا پیش از نیم‌فصل‌قرارداد اوستون اورونوف ستاره 26 ساله‌ازبکستانی خود راتاسال 2030 تمدید خواهد کرد. توافقات بین طرفین انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30003" target="_blank">📅 15:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30002">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jc8J8HD6PEfHHrRJRxbRqh3ZJ80B7tXf53jX75rLoGXTbwJZm1QL3uZq66zj-R2qOMeHH6fgiR1DN2uhk7PBaPGlyABGZhTw9bvVJfMlVMZCfFjCachxgjP8348z6R7aE4XEuKhAItfR0fL6fm8_QbBHa5Qgplmk2jyt92x9YZUSU47eY4p7viFtB0BPfwIjM0yTFGsHaiKIFBtZkt5DLen-SMdNDKh6Ysfh4ri0nPD0SC_xzG8m7I4Nex9B_fYH5XycJNbLh7q6LsFmNg6X8Yu2QvcRMhKjIx_oVoAsCVIkQHqBvhSsb21IlhdfpPT2h2GtQxv2KvyKQJbiP3v5kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ نشریه ESPN: فدراسیون فوتبال پرتغال داره تلاش میکنه که کریستیانو رونالدو راضی شه در یورو 2028 نیز حضور داشته باشه و در پایان این رقابت ها از دنیای بازی‌های ملی خدافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30002" target="_blank">📅 15:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30001">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c60e1877.mp4?token=DEV5mX3vcfJQshWE1JksoPXeDL5P73FMPEXIuM9-lF889vZ2mz6jvob1rRSb4Ptlnui-EwYkHRLZ_pCibwAhx7850qvXxskw_Q_lmt3EuJQGkFoKEyXg6-FNTrgbdZfc7tl6Mtd5f9I0CJFzxSybDIen7QOPJR3Kf0O1POY_6ZWjKgJgPThyzKGJ6U6Z4Gg0Wl0T1gs7xe_C9J0mRTpi8iwOYPb8n-16p_b4liheJIyNM3CsS6XjNwa2wu12efDEJaJaaX5ckZ0jF5XwZKZ8O807Rbkd4xq4Ycc3YUT4DphgKd_0qvRNvquOEDUVLQ3OTNo1fXz-h6wKw-6kYbotTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c60e1877.mp4?token=DEV5mX3vcfJQshWE1JksoPXeDL5P73FMPEXIuM9-lF889vZ2mz6jvob1rRSb4Ptlnui-EwYkHRLZ_pCibwAhx7850qvXxskw_Q_lmt3EuJQGkFoKEyXg6-FNTrgbdZfc7tl6Mtd5f9I0CJFzxSybDIen7QOPJR3Kf0O1POY_6ZWjKgJgPThyzKGJ6U6Z4Gg0Wl0T1gs7xe_C9J0mRTpi8iwOYPb8n-16p_b4liheJIyNM3CsS6XjNwa2wu12efDEJaJaaX5ckZ0jF5XwZKZ8O807Rbkd4xq4Ycc3YUT4DphgKd_0qvRNvquOEDUVLQ3OTNo1fXz-h6wKw-6kYbotTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارسلو ستاره‌برزیلی‌سابق رئال مادرید: حاضرم تمام پنج قهرمانیم تو چمپیونزلیگ رو بدم تا فقط یک قهرمانی جام جهانی با تیم ملی برزیل داشته باشم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30001" target="_blank">📅 15:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30000">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqw-CBxQRzuQtk4QUnfoOOTFR9KHWUcDBcVAXcp6sGWiF1wudYbS0vB1lK6kiZ0liEj3exVW1cN5cZeSWO5r3UqbE6OAPBXPuzB-xM7N4u1284WhKdgIoTpn81aS0Cmb2goKDU5kjWrPjX92QShGiQW1dG80S6WZIhEsEqf6CvGT6pD-vg35RL8Bi-45QFJSW6EA5J30pmnwOvRbkwlNpGzaTD8BxHYxrhdunUoUoO0ECwPzCR7e2C4diOI9CBPCqL4IqAO9BJ5X0e824NwVBzj3X3VG1fpOto1TDragKO8nVQ2JGKSmlhxTzbg1_dpoZ1d58pdDsbgrkUk-vgliRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
#تکمیلی؛ امیرقلعه‌نویی سرمربی تیم ملی به فدراسیون فوتبال گفته علاوه بردستمزد 100 میلیارد تومانی‌اش برای جام‌ملت‌های‌آسیا؛ درصورت قهرمانی تیم ملی در این رقابت‌ ها 300 میلیارد تومان پاداش خواسته و از مهدی تاج درخواست کرده که تمام این بندها رو در قراردادجدیدش‌بافدراسیون…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/30000" target="_blank">📅 14:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29999">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZO34q64wdXV-lmIPlYzBTvcs8ZCfkfppHCEtIqaFjm3LkUzzepvKdMPCU8LLzh13G_Lmd70oX5JdlgJPwIU3Up6_C3AP4XEmF3h7xkxczEOwlJdKtwm6tidD2x0IMXUtFkfJjO3iDnn2a1Y3ARTFEum2AJ6xrsBIm655HfZNJBhg_8l1S4Ox_N_RvwTfByyaYY2MeC2hVSbYpKgj23-5PF2cCoPB-AX-Fc8xZgJzmpnV4yo3u1zOuhpMqkgOAIyJ4VkgubcRv1ajNVqFkwwFao_LyzBg7qYWIal_gp9qWMUGr7DCxtcT--NYC07Vyy8UBrw0Iv7BgiiY-pQ9rxqEWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔵
👤
عملکردفوق‌العاده درخشان تیم منچستر سیتی انزو مارسکا در فصل جدید در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29999" target="_blank">📅 14:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29998">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2vAvmuMPDEHMmTygWWr8UofMfORJAJkqdjhFWd4E58q-CxrbugGzX-J5QDpUsTv9weUumUrclJSRpYYV4PIyUAW2L7XyFyTWHGNDXuztzaxflXQKrPiI9TsyCTqrlaNCmt1RlZ1q_DemlG5WWOoh55feYqFOkW7a9ZilGQ6AuQu5SdAl-uhacFNZzoeHOOjdEAZfWPpbcX7g_KjbqcxhtkajWVAX2U_DzzypkoyG3KKmpwPcI7VCW7OAzw9LT4A5jHIfH9NWJaW5GioOqCc170bBEoD3aBKR73TGfjfUSlxaPfbMKZ_84QZsOEAIrW7Ru4DxMv7vzn-UkM0025-OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/29998" target="_blank">📅 13:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29997">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe8697aa22.mp4?token=ts2yMpukq8kfWnbre40LsGAm9G8AF3O_NoefURBGT96xRUjpqx-lh2tYxjOs25Tau93k5b9jWGpURATtE919dbdWfBq_R_jFjMT0weY5gbBZIosS6pj4WLyXtnPP92k_jEt3plCCHVHWh-RbYSYx4aWg8_pP8m-wA95hJSQeUb5qb9Lz7VW5S1iEQ9khtvhTMZ9D9OxlZ5cxgNEVApwX6UM5y77kOhVhYSxiI__syG39g58J-mBafW1mt4IRT5HjlXdN8b1MEaCvQhhglfHVmwp-tPKd6LeFRh7e7xwgWJ2cRKKcTq9CKFodOpMYwVl9T4VeSxWwW_8d69slmhwjSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe8697aa22.mp4?token=ts2yMpukq8kfWnbre40LsGAm9G8AF3O_NoefURBGT96xRUjpqx-lh2tYxjOs25Tau93k5b9jWGpURATtE919dbdWfBq_R_jFjMT0weY5gbBZIosS6pj4WLyXtnPP92k_jEt3plCCHVHWh-RbYSYx4aWg8_pP8m-wA95hJSQeUb5qb9Lz7VW5S1iEQ9khtvhTMZ9D9OxlZ5cxgNEVApwX6UM5y77kOhVhYSxiI__syG39g58J-mBafW1mt4IRT5HjlXdN8b1MEaCvQhhglfHVmwp-tPKd6LeFRh7e7xwgWJ2cRKKcTq9CKFodOpMYwVl9T4VeSxWwW_8d69slmhwjSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🔴
#تقویم
؛ 15 سال پیش در چنین روزی؛
نانی ستاره پرتغالی منچستریونایتد این سوپرگل دیدنی رو در رقابت‌های لیگ جزیره به چلسی و پیتر چک زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29997" target="_blank">📅 12:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29996">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQr7Yb7f2-tycbJpE63DisbyyeqJ_rckOxrBsi-BzOQZKeU0I0Bnka1ecQEUH_68ZiZRphNmSLpyEuNcbMt_yS9E2Xqt3eN9l5KOk3bezDoobJNJyJssglPBurMGIHhjkTedy8wTAhSV1-ye5yLv7aqFSnplsr5fm3Ff-Zae2xN2EbHk2_bm74rYtXlaJ8yLUE1E6Ffw_7WI2sKNSWFdQzGAY8fnbkTggftlqO08UStrUCrDY_U3AsmMhcRvTGqXyWe2GqOvcN6eC89mf4T0wiqrWE4FPDWNW7hWS77efTlcOl1g1C07tGbqGXODioVeq48zPCxpDScxuSGp7jqheQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب پشم ریزون و استثنایی فوق ستاره‌ هایی که همگی‌موافقت‌ خود را برای‌حضور در مسابقه خدا حافظی کارلوس توز از دنیای فوتبال اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29996" target="_blank">📅 12:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29995">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkWqscfjoiskgipBnm6kCgsIbAHb-uwDv8cvV1HyLKMq6rT6Ob5tElAZW6QEiWgjeO3wq4iKmp8KMx9UYzjIDUGB5gS861rmtiBOtFMd4XnHo-IjjIHvJFJeN9F4udJ17RWdcMDzthO3gYaDxPz0o07FBM8h8H5Tuy1P6okbroj85fyHkqHR6JoOgxRLkte6Ru2Tprtu88_7EtRAJjOH2OtkgemR7cdx8_-eQ4YNrPjte-11kEtF7wJR8eXQnNznWWqSRCLGPZtnEMbYEHq7LAelgbWE5v0c0kBG1WvVkpc5pU-9EIJp9oSZmNv2gnOOiW2WeXwgEiu9uvwFaVVc2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برنامه دیدارهای معوقه هفته هفتم لیگ مشخص شد؛ سه‌شنبه 21 مهرماه دربی‌اصفهان برگزار میشه و چهارشنبه 22 مهرماه راس ساعت 17:00 بازی خیبر خرم آباد و پرسپولیس تهران برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29995" target="_blank">📅 12:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29994">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f8f92a53.mp4?token=FcUMq8uOWa7dw-V2DG3ufzKYjaojCDg8PgePMK9YM2QLxPspubtMFJpBR0RmuQKkJigrwHP6lSLC02NQNLucOxpTl307aIpxwEDEHxz0med4k5DtBbSNfzbmrUO0cLHM20q7W7h6HmcEEr8Sm4GPHKYGQubGWnvmoNl4aD0xPWQfbtMfC0G5SVtucjuvKjobBLARqIgNq-gA5-5ngCWjZaJOD3ng07xDkHmxbF4d0pT1X3AFqrw9wK9xwgTWcWPqTs6fKJXqmVRJxidGQVBnFX48FZn4puL6mFZavtDTv6sh_zXjqVDCn4knjQ3EtiLDGjg5XlhqHzHmyPD2C6bzCl7-80g2MTKTRzWiAMN4wh4UuPngrC-II4FexoRAnhtRdyFPJ_XYppP-47hUgsVmd9qmkzzQoYIsDmqmMNVj5YNt0LBWLWs9zbNG_ApEWuDof50F8KP6du6NJH6WqegTwvCP11C1AGHVDNq5fTHzJr6eHhoRSmZJ35DJhDE5ZTMcrI9UhrOHTq2m1HqJP7j1VfPIHZdC9iMIDjJycusOCn7qDo0R-NH3T3kL4IunskSyneeAxVimQuFGeDcRjMexDHAwzYbbsDzOKSQNK5KopLeb2zXk0y4d2ZhsKp-ZUnz_dh8i_5Xrn3NBm4XVhkv27-pslc6HbhzLrffMrtsjt88" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f8f92a53.mp4?token=FcUMq8uOWa7dw-V2DG3ufzKYjaojCDg8PgePMK9YM2QLxPspubtMFJpBR0RmuQKkJigrwHP6lSLC02NQNLucOxpTl307aIpxwEDEHxz0med4k5DtBbSNfzbmrUO0cLHM20q7W7h6HmcEEr8Sm4GPHKYGQubGWnvmoNl4aD0xPWQfbtMfC0G5SVtucjuvKjobBLARqIgNq-gA5-5ngCWjZaJOD3ng07xDkHmxbF4d0pT1X3AFqrw9wK9xwgTWcWPqTs6fKJXqmVRJxidGQVBnFX48FZn4puL6mFZavtDTv6sh_zXjqVDCn4knjQ3EtiLDGjg5XlhqHzHmyPD2C6bzCl7-80g2MTKTRzWiAMN4wh4UuPngrC-II4FexoRAnhtRdyFPJ_XYppP-47hUgsVmd9qmkzzQoYIsDmqmMNVj5YNt0LBWLWs9zbNG_ApEWuDof50F8KP6du6NJH6WqegTwvCP11C1AGHVDNq5fTHzJr6eHhoRSmZJ35DJhDE5ZTMcrI9UhrOHTq2m1HqJP7j1VfPIHZdC9iMIDjJycusOCn7qDo0R-NH3T3kL4IunskSyneeAxVimQuFGeDcRjMexDHAwzYbbsDzOKSQNK5KopLeb2zXk0y4d2ZhsKp-ZUnz_dh8i_5Xrn3NBm4XVhkv27-pslc6HbhzLrffMrtsjt88" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از کاشته های دو ضرب در محوطه جریمه حریفان؛ همه خراب کردند تا اینکه بالاخره یه نفره یه بهترین شکل مملکن دروازه رو باز کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29994" target="_blank">📅 12:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29992">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRpmF3zJTDLrSHsWj4STM-W0uP1_CJi5NpTF9sEKvPTkOTqD181TbC7Cn29EtBh8nv4yaHKyX1A4TdH-ycCbDDvnvWaIbE65SEMPpA-AGcVj4cBma3hjys5IsOPmY2GS_H2SJL1JCB-ZY2uTCtmz6YNDTPfioRmQQtWFw_BPFrPjU7ZvVtAOVFN1HpI1baf0VQIZJxMNpC6E-43dKv4V-FpMpJBGt-A2YPtI7Lfwg-mcrLW6n4VW4wXuQUIke6n9YVMdm1Dh0WsszeuV1LOQ-QLu7s-B2DbpKTd_wpvgX4L02q63zYlbD04_VlJum7iLqJmNGTI8VWKKRUAVh7dJOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29992" target="_blank">📅 11:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29991">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d818795d1f.mp4?token=dT2wfmVJ1AMeq1woUyOCmlxNnczm5CBeqiluI7n4SoRZbQswrfl-EOrkx0PhNcG_7UEEVXFYtKDl1Q_QZs9HBmf8rmJRBo40YMZdaDiWVVrOtWjveCC6AhjHgwCSCaMmRIZ2292ErZlvU1o8BVTPYPFzSnjJlU9tKAa-_JQynMQSHr9RVfik0Gw43duRBbJUlXdnh3mNypRjaoCp8PN_UWbmpERLElLzrtWH9qWeRM-UACSac-0TOaWzoRoyswH4DJh0evDAzMXcnViysunGV48M_IBau5tLaL1vYJ53Kn3SgUmJDhkzWYvBzC-j7mHCUKI8ivuCKNETL6Ve2Za7zban9kM1NkjDhpSf-3bssS0cJ68uhEyVsj1srDcBqoRc9vQZXxxtN33Oo9Gk_TJhOr_C9S0UIUOiBltA7BBpMbMluGkMUL0XqB6z7B0byCieLbaDvowVoC7XekyFZmoREMsqU1ZEXTbHGWu0sVHkOelTFWSNfCAT_BaEQdakwZZzscQEBGbvqnSByhrlElWU5HJb4_tpc6gOhLNvueJ8tB9pVROMUcKD1SMn7MdgbRbgdAhT560AvQG5keDXAPG85fMvuyvS8-G3MOFmGpmzJ7F2Xff64e50HwScAm3UeauF6v1snTUA5vHuRymhEiNH3yPpDzII07vYCzVq8RsFTDM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d818795d1f.mp4?token=dT2wfmVJ1AMeq1woUyOCmlxNnczm5CBeqiluI7n4SoRZbQswrfl-EOrkx0PhNcG_7UEEVXFYtKDl1Q_QZs9HBmf8rmJRBo40YMZdaDiWVVrOtWjveCC6AhjHgwCSCaMmRIZ2292ErZlvU1o8BVTPYPFzSnjJlU9tKAa-_JQynMQSHr9RVfik0Gw43duRBbJUlXdnh3mNypRjaoCp8PN_UWbmpERLElLzrtWH9qWeRM-UACSac-0TOaWzoRoyswH4DJh0evDAzMXcnViysunGV48M_IBau5tLaL1vYJ53Kn3SgUmJDhkzWYvBzC-j7mHCUKI8ivuCKNETL6Ve2Za7zban9kM1NkjDhpSf-3bssS0cJ68uhEyVsj1srDcBqoRc9vQZXxxtN33Oo9Gk_TJhOr_C9S0UIUOiBltA7BBpMbMluGkMUL0XqB6z7B0byCieLbaDvowVoC7XekyFZmoREMsqU1ZEXTbHGWu0sVHkOelTFWSNfCAT_BaEQdakwZZzscQEBGbvqnSByhrlElWU5HJb4_tpc6gOhLNvueJ8tB9pVROMUcKD1SMn7MdgbRbgdAhT560AvQG5keDXAPG85fMvuyvS8-G3MOFmGpmzJ7F2Xff64e50HwScAm3UeauF6v1snTUA5vHuRymhEiNH3yPpDzII07vYCzVq8RsFTDM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دقیق و برگ‌ریزون عادل از پاداش 20 هزار دلاری مهدی تاج و دار و دسته‌ اش سر پیروزی شاگردان کی‌روش مقابل ولز درجام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29991" target="_blank">📅 11:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29990">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGgZ21ed9_hag8jRU9rFH-8eKIB1LtmmsjJLwtUWlTKthr_DAOabMthT44pA3kJYWDTc1H9ufmBAw6qfPCDNjS-Og4Wnfjyb98PVhYUcmZZJcL2LQ4oZrlv8oRh1ID-ZydQ6rRT7aqGj0sy5k16eANirRfuqlLYhE9L1XgV3CDTMukQmScHKIbNbQpvNnZNoqMc4YgXObt0NK-Nasqr6vYM0jfsGSO_tqtXdmhXVJ4tPAdOc0Q5eDnhHzk5-Dv8qWsaLOuIDD26_8xYl5BYLxCwj1pp7zf97kmt4SsGGNXyCEX7V1yus2GM63G6NlY8oNe6YKeendNEu6tDYj51zKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیمار جونیور
🆚
رافینیا دیاز با پیراهن بارسلونا؛ رافینیا همین امسال به تعداد گل‌ های نیمار در کل دوران حضورش در بارسا میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29990" target="_blank">📅 11:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29989">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqcneMB5g128BU3hiLOK02w03-N2cUefetaDY4LhjZoVhZMA5fnmCatOxTTpU76INFVj5iZ6ImsyCUBuUppdzJDNym4S0VEFYs6b2V5lPo46b41VcqqYbOM07E94LNfigQOX4sN6pEDh2TDWvB0CqUkbEHXteQEACq8-hE2lIVA6ppJdad4nfsmvCQdjg5lMGOMVS1LkcKdzQmroHEL9LwdgyJvySlPUbFbmiafWvVaGOhcv2La7wgsgL01kADWLP5iYiwpIeZeSACH0q8EUv_vt1P1I8silHNZBqXeIk8OzObxAaDXSZUYMrxwIp5tqPFjK3e_HlDCukOuwuvMSjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
برترین‌گلزنان‌ پنج‌ لیگ معتبر اروپایی تا پایان رقابت‌های این‌هفته؛ رافینیا دیاز با اختلاف در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29989" target="_blank">📅 10:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29988">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGPguQk8HHniDd0DT6R3BiATffDmAZ_oOvYKfenbfv314ywqFaNCz5qK6mKZVIC6oYRA9sj0nUh7NaJY6UOKmUGmOd4rlYHfiOapB8yXyJCTsRHouViH71uHF-YqhKss3Lr6NZ2IJJG-GowSloUIg93r_4putGSaqu41NyMDmKh6U_QsSHxuPRJFGKLbvRNY92d30Al6nTjre6IGgGWSQkuJpGQqIe7mQElcULaPzBZFpqaUcxCClyfjGkriFTVZeYjdFaqlJVtjIVz6c_jaeC8yXl81SPQWeNBvuh2rHYtwehTzYQlWlRJ1L6aLrv7pNYvI-oR1-iC1qdfBQyTVXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناسان AFC؛ سعید سحر خیزان رو بهترین بازیکن دیدار امشب استقلال
🆚
السد انتخاب کردند. سایت فوتموب‌هم بانمره 8.9 لقب بهترین بازیکن این مسابقه رو به یاسر آسانی ستاره البانیایی آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29988" target="_blank">📅 10:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29987">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d749b5d59.mp4?token=VeP9DzVZEwLPdQ69yIUzX9JQcbDSdGqi-CTyuuICL1rwaIA4ape6pxxp2wOmE4drEEMlQi_6u-NdrGD51W1HIgH9qiPczMgSMtg8O_xcWY6bS18GYmZOs9ixXmkNu4sWwjaeawiS35d-L7usfEr93pJckAjC4UqOIVEes8dJEf0b3zH8Wg0C9PdVc1kjxV6jJck7pvkGprnoe-V_db6exbTqR6m5rWVgDP5OP6uY_oF1Rt-yrMCPCAj1vx6FmbqsYxHwUyV-X8kF_ZuMxPXJiYi4qC8IRYnH5PXVHniFWd-LSqHBk0imeyrfdZ1_DtSA3YboBSUG4UN6qoG6r220GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d749b5d59.mp4?token=VeP9DzVZEwLPdQ69yIUzX9JQcbDSdGqi-CTyuuICL1rwaIA4ape6pxxp2wOmE4drEEMlQi_6u-NdrGD51W1HIgH9qiPczMgSMtg8O_xcWY6bS18GYmZOs9ixXmkNu4sWwjaeawiS35d-L7usfEr93pJckAjC4UqOIVEes8dJEf0b3zH8Wg0C9PdVc1kjxV6jJck7pvkGprnoe-V_db6exbTqR6m5rWVgDP5OP6uY_oF1Rt-yrMCPCAj1vx6FmbqsYxHwUyV-X8kF_ZuMxPXJiYi4qC8IRYnH5PXVHniFWd-LSqHBk0imeyrfdZ1_DtSA3YboBSUG4UN6qoG6r220GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی مثبت 18 مجری‌صداسیما روی آنتن زنده؛ طبق آماربببنده‌های‌صداوسیما از سال گذشته تا کنون به یک دهم‌تبدیل‌شده. مثلا یه برنامه تلویزیونی زنده شاید روی هم50هزار ببننده‌داشته‌باشه تو ‌کل ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29987" target="_blank">📅 10:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29985">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a52708609.mp4?token=pcgVf9jxHyjivavkE7ZFSKK2E2pJHnKyFu3u78CEvS8u9NcV_cv7PEZdz6Z8Ko1s_RBvWR9AZb_18npD_2J1x0QRc6WAk_BG8q22aBm3kJ5tWhW6EHv8E5BpLoJWzAWhC-zIQYKqi_qYPtQRMtNIaRxZ--ya-up1ZF5xbFFSYhpgCGgjOUj1Fy8oR13P3wGRwC__retVnRkOBg7teJ-SVi8sY6RnlIeT3KGS8Ycix4y5fkD3B6u3F5F-xPYyE4RFE39am1nQ0iI5hOaRBhb2NuHyB2JuIoi0ZmDQm1uOYZZFFycmPf7jP6WbtkWuT27qlS37AWgUexbn4TOoVkM-BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a52708609.mp4?token=pcgVf9jxHyjivavkE7ZFSKK2E2pJHnKyFu3u78CEvS8u9NcV_cv7PEZdz6Z8Ko1s_RBvWR9AZb_18npD_2J1x0QRc6WAk_BG8q22aBm3kJ5tWhW6EHv8E5BpLoJWzAWhC-zIQYKqi_qYPtQRMtNIaRxZ--ya-up1ZF5xbFFSYhpgCGgjOUj1Fy8oR13P3wGRwC__retVnRkOBg7teJ-SVi8sY6RnlIeT3KGS8Ycix4y5fkD3B6u3F5F-xPYyE4RFE39am1nQ0iI5hOaRBhb2NuHyB2JuIoi0ZmDQm1uOYZZFFycmPf7jP6WbtkWuT27qlS37AWgUexbn4TOoVkM-BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
محمدجوادحسین‌نژاد که جدایی‌اش از ماخاچ قلعه در نیم‌فصل قطعی شده امشب از نیمه دوم برای تیمش به میدان رفت و با اینکه بازی رو سه بر یک واگذار کردند نمره خوب 7.0 دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/29985" target="_blank">📅 09:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29984">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFwYEqkLrc_-PBj6rKfw4Dl-Jt5d4T7hmp2DHg5w4iPcH6AOFAAsGExqDDzsXocJ-SwIwcy7G9MT1uGWZaSqE4HXYTlt3X1QBHYZL841VRNVu7_r_zvz1DcaW5JixMjMu1-X3RSxVpQzd06F_TV3lxXB5V02rO60eZXNrnw0_V_8TZ_-_2T7FAA4Be_tLRLIdB0tMV-cvRamq3thgrvX4vAAEtbJgwSSqKQQ_T4ZM-QArTTxKs1M3OM22pbr-AqLxGWhEfglEaENiCKVyRb0VIJZiqC0NGu7ylzTMJxS7e7d_qvGH8gaPloNvCri3himnZHb8vUTSQ3mkFthALqrtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
امباپه‌ستاره‌رئال:
اگه‌میتونستم یه بازیکن رو به رئال مادرید بیارم کریس رونالدو رو میاوردم. او در این سن هم میتونه موثر بازی کنه. اگه به رئال مادرید برگرده قطعا میتونیم یه زوج خطرناک تشکیل بدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/29984" target="_blank">📅 01:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29983">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDLiTDGySAF3LdMv0-Qm-oZgl9L5KRlhiNBv9KD3zT3uqx7Je2Xky3i23OnzIssGw4DqSe2n1SakmeNWgCntqothtLOEnExH27S6gk8b-r-jxu1lWaESnp44BCnOmNDp6KLhsAYhtCvjt-kj4_uIMVmlq9WKS7t799w0O3lZzLHGpyLHkLBROghbrLlpvWyCZni1Zr54hU-q6U1s-MPdbGGjsk9Kv0-sWpMTh5Q118gKdz5fmTt8py5cERkcIk-GaArWnDtjZVRQ1i2RbIvDOdO_nT7JdSOlrwIlDCytjrHdN6dGTXMwYpbnFM-GbOnJwrvK1DYMbYrzvEgd3L5HJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛ فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/29983" target="_blank">📅 01:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29981">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kr0UZOb5M68Huhe3wP9WlnZ1Dkre0V5Xw8nx5a1qU35MZFh7i7d5PUrMji92TckEIFZGidFXbuQHauI57mmcha-6eVH3bT7gb5A2Wq7lgAlazNT91RBVnWxizADwwDezdA8jO0EC1uPKzgvG_a8IuTxhYEKZkM6cRZqJMQzw7CgDGtaYQnqLD1cIcBlIR7EFbqpDS9M3lJDw1GLgsIHR9N0zOkys2iq_a53Z9g_dHRS2Ung3-EqkWP3y0_601b7XqnCwUS8ln-MVAKqBay7py7evdvZ7Rr2iKDnC9v4MBTAV98pIiujQYcPh7gasfmt4vNgkv4yREeQ1CPA6oQ4u3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛جدال آلونسو و شاگردانش با برنتفورد برای بازگشت به کورس صدرنشینی لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29981" target="_blank">📅 01:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29980">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVEdo8htK9kXzImnxi5EZ5LODPxaRReZ3Ob52rV2ALrLloXHFalWkK6_lNiERETITGEix4yAcuTv0YPk6iJL6Z4lOo9dGNFMcvK4jzM2_aJ4JodOFdS355hhqPU2ptbKZQtsG8_E94ZVLRmdkgXNlR1E3xBNautWuiN3OdGGvC2T1RYS_z8nhPg2Z-G_68EVbCQcD20-O1D9h9CuzcoHJCD4C2gTY_GuhZPUJSAru7pODzvkieW1gxalGtg-zvP4y4dAJBvaEMUc4tcNz5aUQlpcY2BL3VuyjOwAaPqUHhwAct4wCGCgiDT5kbp8yLL8RITrlnDEM9IzeVpetXqz1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازچهل‌‌نهمین‌قهرمانی مسی افسانه‌ای تا برد پرگل یاران اسپالتی در آغاز لیگ‌اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29980" target="_blank">📅 01:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29978">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">📊
عملکرد بازیکنان رئال‌مادرید درفصل‌جدید؛ امباپه با 8 گل‌زده و 2 پاس گل برترین بازبکن کهکشانی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29978" target="_blank">📅 00:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29977">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAXz7YAOyXcriSOTvsgUphLZ9mBJCg_G5nrsOisidcnE1ykssVqzrpcsU1mBML8xd0FPSUsUf91YfrT7Z48OcRhIzO6sCOZMGIc2qYVMHx7VVGI8xX_t0CnjiO1XLrAHwJHi38h7Et4K18qWXxAXSsoxLvfPwRj8qJ5Wm5ZiRd9FqEnYB-3TF_QrX3MJmoH5fKcKzyImjjBqIji6bYgOq95eej-IPOzBX0JRPByFoFqEwuF1IGCF0uihuAw-hV-yLq3SReVGR_rfK5PiVsZ2TmG-74OOGJ1WS1ITFPG5Y1pouqvvrooD_l2j08-8bOhhw56bxDS4ywZEDIfVqAxhdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29977" target="_blank">📅 00:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29976">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WW1mzqA1ZifNLitxgmY5isg0RCIjnATkQLSi3pQJ8g3CPdnkUYfnuZ3h7huKGa1TFX-_0vLeyp7scmlvu-GTdq0D89h37yiZbG3wx685jUSVa9E-0BcEAWJ0x3sQCH-39CC_hHMu2CiUqgJRrvFNx70X4_fxIphDFNeMDBOxe3u5jAh8SzeQah35tjqINjcemhMhjRkGlN8vdMegVJoi37HAunCg551Gof7I2hDNjd2W0G9ueWLfk_q-ycBabgZKJ0wq_POVdj8C_DY17Do-2k_M9wiHR9RdRuRUNs1HnXQsTrGO1VHr7Shtj7DnCgA_bG0LR9sQZCWy7r752Y27jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌ امروز؛ رویارویی صیادمنش و لخ‌پوزنان با کریستال پالاس در هفته اول لیگ اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29976" target="_blank">📅 00:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29975">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3PwncXkRbIDRB6l0BIYyvbv8GsDB3PXnDWQsu2F5rwnNM-DWiw-vR_l-jawVrasEGhA2j-z43oH1X9ZzNgwkDM4nzXoE9Y9kYY6DqugRYBJ2wwM8tvNm1Xit4NQg-GmMy9iV0bedycn3uw6F03hz_-db431EaNsMlq6LW_XbEsDNbdTqazruD-MjYKt3PSm1zIIEM4gkv4GVdNaiPGb-imcsZie6g1H1fQ5SvGPvDseYrGNQGAXf5L4w1R2-4ttvEZNnz4Rv9GSfoDJCKM6FTEJ3mphvVxqBqj3mj6VjuD7zdia9Ve7c2k-UVN4zAFjat4An5OL_jNRGvikyN5Tsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این پست برای رفقایی که بدنسازی کار میکنند؛
ویتامین‌ها و مکمل‌های‌مهم برای وررزشکاران در کنار یک تمرین خوب برای ساختن یک بدن حرفه‌ای.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29975" target="_blank">📅 00:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29974">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-hMVSAAfXW4LmcyfZeQDQr90_gUla-a0mLXcdWHdLxHh_C_1dNQUMGXjaX_k66zdmghiIzJy7P_f2X1XL0iQKuyvg6G8elECfb0pJHch4tKiVjc0VOWyc9nDT5sPd-bw6tgBHOD_nAxHYQGSQ17RO9XWkDoXR4nfwRqTOD4eoJ_8IgwRZ8eTa7SmHeD1RX07FrG99DbsFHWmQfLI3kTI7oQ3t5Ra9WIaKrmLPd2nhY_THC7L1VLjr-qTQhmjoXVaWapkgWXFgU8-KN6-Ag0Hk7nJHSNZh__Nc6y0hBkGqSWQWlfEew6-zingav7wSGgJ52creNr64e6MBx9lwYTEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/29974" target="_blank">📅 23:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29973">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2b4BIDXvZn0RDFM_1YRNcc4WImL1sGQApMOcyjtDaUs4vL2JaLPVDHkEpdh2fQR_kH_E7BA-FL2wRT5YU7aa3pQ98gaaqHOvSKlWdTG8PwKIbpXd3Jm1dthgBlBQZMSHPMy1xcO3ot1wqLx9GtSYZrxo1sMnjEX_56-k2Q3CRYfQ_LtHbF-6pJd_GjRVlQ6wwumDclu0019ouP1XNqPIROyGDMXwrtTeeDOcP_yQyOQGPTT_sfVTrxB5mQyAARPmP8fPtWMI63N9stJyk8JBvw2eYPkLR3AeGsQzYp0l8Fws6CcmMiOw55_fNDtUC2UWqjYSlT3rVdrcTQJkSy_tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریهESPN
: درصورتیکه‌هانسی‌فلیک امسال تیم بارسلونا رو به‌قهرمانی لیگ قهرمانان اروپا برسونه لاپورتا قراردادش رو سه ساله دیگر تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29973" target="_blank">📅 23:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29972">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UejY9I_kEAyC1jWxfp8JXAXFBi3CDFDr4Z76E1IWHnLMer6OOW7RZff6AXy5P0GVLefVs1Frt9yqlpZrSbEe7Bjakd-C63fl-1_kia3yNZHRbNJHneFDigAzlTIHnhTLnGkqLMY4lOYz3-2hvriPqa2W3kgu0rWN3V5JlGAI119VYhLZMX_KmeQ0fnxbn3-cjmPfmqwMdc5uJhUnYsRdWiD75wCssSlGMXvhSa2p-9osdtYUyqN8lTkd3HsCi9Lig3fEIafWZSXAQMZDfjap957abuiAmE4K_oRFL2rWnCNWlIaqK9sgWDPbEz5KGE7yUo_D2KOE6P8-Ss1M4ImE4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نوزدهمین‌دوره‌لیگ‌برتر فوتبال زنان از فردا رسما آغاز می‌شود. رقاب‌هایی که به‌نظر می‌رسد با حضور تیم‌های اسم‌و‌رسم‌دار زیباتر از همیشه دنبال شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29972" target="_blank">📅 22:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29971">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRFQqP-WDiS6pKGj_eykvOlsun4jPCkZTF0hC4fACTyQv6tfR5LZNbceH9S9rdcjbUSMRgGSV5yscjA74VtW_yilPfLAD2DWpfpG-0MDdGtwVn4n01etbq5i-vvXafJKY2DlKzr_dqbNe1R7LMJ1FpwL5339qKXxfoXxVwUwh7ZN6HYJCOg92UQadxq9T-0mVH5CElC9Khb8bUpfiVWZirSRrHuGjOJ10yVW6I0FtT1xGWGfwLp9t8vxvdAJ9Nk1joAx-i8OBJYj12GlGwSk3dpdKaRHmz0J4auV-7WLgBxtWwinhpR58fDfeitq7SZgGTzsIzvstw13Sb94kPZyxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29971" target="_blank">📅 22:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29970">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGjwaA1UUHaIe5fczscUXjfgAyoidqUNE_RH22mZXiqLDPYBZ5m19xrv2tWwk4bFD3icjef4pyOc03gbQx2s-bk8AqylnJUEXN0vNlmgSGcwI_20zZJdSVDv1WI9nV1FzxTZrTRCcFYw4tcSMUU_uSgdcNWgVLGRKdC6Xi-c1GL58RlFssnQDsd0_sYB-YvRTfNcgJP5tWE4pyFTmoTQfTwauflHk49oeI5n9xQQZuGKyzngCczVKs6ZAv6-B6hBxtvJzmPmmPxH1hnHBWEVDUIa2xmJoZSiI3H0L47Mm-mzP3HHYfeIVA0BfmaEjX6Mfgb3hgxFm9phqmRQe8oePw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
بعد از پایان مسابقه اینترمیامی مقابل کروز آزول که باقهرمانی‌یاران لئو مسی همراه بود "چیرو" فرزند سوم لئو مسی درحالیکه بعد بازی لئو رو بغل کرده بود،به پدرش لئو گفت: بابا بوی بدی میدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29970" target="_blank">📅 22:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29969">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372ce8a577.mp4?token=i80JwbcQrXEJZiPSqtJJDAymoOhebM5y0Szc2cdaOE1S52Fn-llbagXqfy-BKdrZzf4kn44srwyAKqoQm6Yde3NuuI7MU7jU_6UQtT7k9wBzaeqQLznAoDYQS524B6zFjriOA2p-FZ2VIsDAR_7M6gmOLeJvi6L-_XJC1MnjHMu-7PA9jZchpcCsO6xzo4zer5CcRmWXIuQKCqcvd2SLS4V_4hFVVKOmDWf4eMypph-SLkK6l1kWcDKNAGCrLQQmDAQW1oSlssqp5xFjUq_YOQlwCpw3EtxmaZ7wRwDnFQE5h4PRF-HoMaSmoZqYgedGuFtifI5eQ0iR6FQVfP9-aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372ce8a577.mp4?token=i80JwbcQrXEJZiPSqtJJDAymoOhebM5y0Szc2cdaOE1S52Fn-llbagXqfy-BKdrZzf4kn44srwyAKqoQm6Yde3NuuI7MU7jU_6UQtT7k9wBzaeqQLznAoDYQS524B6zFjriOA2p-FZ2VIsDAR_7M6gmOLeJvi6L-_XJC1MnjHMu-7PA9jZchpcCsO6xzo4zer5CcRmWXIuQKCqcvd2SLS4V_4hFVVKOmDWf4eMypph-SLkK6l1kWcDKNAGCrLQQmDAQW1oSlssqp5xFjUq_YOQlwCpw3EtxmaZ7wRwDnFQE5h4PRF-HoMaSmoZqYgedGuFtifI5eQ0iR6FQVfP9-aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
بعد از پایان مسابقه اینترمیامی مقابل کروز آزول که باقهرمانی‌یاران لئو مسی همراه بود "چیرو" فرزند سوم لئو مسی درحالیکه بعد بازی لئو رو بغل کرده بود،به پدرش لئو گفت: بابا بوی بدی میدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29969" target="_blank">📅 22:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29968">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f4c8fa49.mp4?token=mdCsvyYwBtvmRHoQ2ovOgL6VGK6Kb1m_tfWXZSVsP6ez75PD7tUtL8jpp9ceLjk03iF8eXruP48zPf3Ni7gePszZ9yYUkC6jkyte8kjIdQ2_sdwGD_SYenDC-z9MXWapwOQKaadWh0cxZ6ioIJMFLc4HLu37koimgJysQ4BrhQQk3dpQ8_8JcM17PkQk_c5gaBvGOj03qYQY-Rvq7JxW7tYBy5Xf39-Sh8bjVrunX8i3_DGTU6OeqXtJdjskx0-0JhDywwI8p_VOAbA1ixicS3S4ieda3XB2Ew-y3heqxRxkjnnbIGQAUKnDgTl6DU8CMtrm08SSpZK-bw9MS0wOZ7N5or-ZSNyIUFeFKqktZgsQhxOFkNe64mqrLykoJWxTkEZDfyLNNRZEQoZ04eTtqcrinYnaXktNAZGC4esB5HrTEvHFtwN8b0uoyKc7isdBGBaOF49U6r3ODXzlQJytwPf--Hnfk6EeRvRiFQiqd36vuKDuRNufy___pT8eYrwyNoxQR5RIHiMbs0wHsUu88vhsmygLh5bTTTnKbfkjviV1i2zUOom2Ww73OmG5DoUc-gk5tLUTYa8asihUf27NUBRv5_qdke-cQUjPhEB36hhnDAHFFLerfHW8HBZQlxEQcHOtmTiAL9nIb1XMdu7vzniQDZ9eEWWTBxycwig2QKU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f4c8fa49.mp4?token=mdCsvyYwBtvmRHoQ2ovOgL6VGK6Kb1m_tfWXZSVsP6ez75PD7tUtL8jpp9ceLjk03iF8eXruP48zPf3Ni7gePszZ9yYUkC6jkyte8kjIdQ2_sdwGD_SYenDC-z9MXWapwOQKaadWh0cxZ6ioIJMFLc4HLu37koimgJysQ4BrhQQk3dpQ8_8JcM17PkQk_c5gaBvGOj03qYQY-Rvq7JxW7tYBy5Xf39-Sh8bjVrunX8i3_DGTU6OeqXtJdjskx0-0JhDywwI8p_VOAbA1ixicS3S4ieda3XB2Ew-y3heqxRxkjnnbIGQAUKnDgTl6DU8CMtrm08SSpZK-bw9MS0wOZ7N5or-ZSNyIUFeFKqktZgsQhxOFkNe64mqrLykoJWxTkEZDfyLNNRZEQoZ04eTtqcrinYnaXktNAZGC4esB5HrTEvHFtwN8b0uoyKc7isdBGBaOF49U6r3ODXzlQJytwPf--Hnfk6EeRvRiFQiqd36vuKDuRNufy___pT8eYrwyNoxQR5RIHiMbs0wHsUu88vhsmygLh5bTTTnKbfkjviV1i2zUOom2Ww73OmG5DoUc-gk5tLUTYa8asihUf27NUBRv5_qdke-cQUjPhEB36hhnDAHFFLerfHW8HBZQlxEQcHOtmTiAL9nIb1XMdu7vzniQDZ9eEWWTBxycwig2QKU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌انگیز و نوستالژی از تکنیک برگ ریزون نیمارجونیور در دوران حضورش در بارسلونا. اونقدر خفن بود این پسر ویدیوهاش تموم نمیشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29968" target="_blank">📅 22:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29966">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxsB9nkjt8ZMjxAFaiyc5yZhmFrLeX3ka2IOWHI5IACByKGVWi4LHEWhXmA3vYxVsQa6CGFQxJXgb92njKnKyRxsh3tK2r7uzYE194aefob7Ys3MIXNjfdwlfk1MqaGppazDyqs2AqHQCHiuCpLNEELH9e8gGuYmMVShJp3Fhi__cMf66ma5luhUpaEsQCnxaO3qQ0PyhWE7YMuN8QsLKDTGlRjqXenSGJ6REruVT2FfSVisLXLcCMullD_dE4gZJ8SaleJteuIT88g2SjGPcn7U5SCyR5oMdQfIHGwEdWOIw74moTfEtl5DPzcGO3yJt78lXevPmHaY5PWXNhhW7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام سخنگوی باشگاه النصر عربستان؛ کریس رونالدو فوق‌ستاره41ساله النصر در نقل‌وانتقالات نیم فصل قراردادش رو با باشگاه النصر فسخ خواهد کرد و از این باشگاه عربستانی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29966" target="_blank">📅 22:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29965">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNJyUfO0yb2AYkwT-NmzqE0Y015zzRzZTpruBW-7f-t2wsGwcJzC-a61xvxf-kyeht_qMe2PV87PrBjKORhHJo35Txmm1Xo4cpCycEkvBbWd9ICoVVcWMOsUhcgvneu6g5W5IQHmET6rKrTth6Qt64xe2Oe3oAsLYBQlI4GSQLngYVfVMEqksriOuwEMEyZQbyOZ2CnjRmW4zXyz9Zs2N1TM2wzR_C73Smz_B3DvtkKqI9vtg7BhVc4Tc1YbYq-04UsYjqvIODV0N9LMdu1iloPYjNWbYXA1ECMili2RFujS_6tmTXhJdf_CM93UGFbQvgNZnZowLeEML_AHaWyo9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تفکیک‌تعدادقهرمانی‌ستاره‌هایی‌که‌بیشترین تعداد جام رو در کل دوران حرفه‌ایشون بدست آورده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29965" target="_blank">📅 21:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29964">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bim9FnrYfDJcnnu5bzHbHAHo8qdlXVWGPzdoTv728cfZEmGW4FcD4GY3K9LNQn2WvQIrG5RzWkJVY7jBNGz5nB3Pd91GUzeHd5gaoyLtf07Yil71KiVHvu3htDICUccvvWhArZswZJr-Ray9Vo9s18QnMb8doNzgGTuSF8iu4p3Q7rv07TRwJod79dKTifg2tEIdyBR6bFgGftAAIfZYTe0yadUWn-zwryHpyIHVhj3-xWdNGzz5Gphf3E3HE3MHa1hA0SSLtFffuMRZV7_w76yHs8stcXK21LgcaNJiPmWXGiiYbTg-1gUVVaNlQlCrNlD-j95xRKUsTPCXtfTKhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29964" target="_blank">📅 21:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29963">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uB3SR_O558KsN7UeNmSgutbbXXSVKe14CswYDCBc5g10ZSe6sLFF6q9tXenwn9ncvDxq1Oq-tLMi00PcGTIOM-JrdNUreKqcj5ko2umbemjCGHeCU6uH02w3AlT7dx8zx57OsE2qkSRxTVTNlXUaW9yqnPBkTXx8k4M8AR-7X0grTP3bq8uCJh5x9ao5qnH1I1LVwXHKtIDc97DdrZyVWFo5iCmJ5Vk7d5VWD5mNTlI7pnj34NV2cfBE3Pw0lrjvl9Ws7ErIWleD9rQttbmAe9iOi9VfvwtzpbUJSW7vOpng9Vr76jhxlgGFeaSKp-1ZLplumSzROdJUuTkz08b5Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
علیرضا بیرانوند دروازه‌بان ملی‌پوش تراکتور قبل از اعزام به خدمت از تیم تراکتور آفر تمدید قرار داد سه ساله‌دریافتی‌کرده. درصورتیکه بیرو به‌این آفر پاسخ منفی بدهد بعداز خدمت بازیکن آزاد به حساب خواهد آمد و به هر تیمی که بخواهد میتواند برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/29963" target="_blank">📅 21:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29962">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNj3wI4G9ajvfB7mLzUUD97YucZTCgTFzpiupbAH4_z0l5jWTnGJC7tVFcqJhz9Mwom--ydjJCZLiOSAT8e56hx93QZwvNxcp_NN6ZrpWrYHpkcNXaptKg5QlbS-Q-flGGbP5izXlZePlWJJBy6nTDp_p-eJWHmUE92OnrVMNFB6BTzZNSp2zekbzSvWeIxvG3HGHOi2Bq0VmrbJGq-epzaewgf0v5LgQEckCv0cl4lmxEXP4x5vP1RvJUoLNzEVv3Tnm7pE9XCyToGrYQv03mj0Z4_n5YlmGSLGNzINc9_zRZ843_8mY_MqVvGy_1h6DcCWZv1U_3qgzH12yOnxRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه میلان بعد انکونکو؛ ساموئل ریچی ستاره جوان خود را با قراردادی قرضی تا پایان فصل به کومو داد. ایجنت ریچی پارتنرشه که خبرنگار شبکه ایتالیایی DAZN نیز هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29962" target="_blank">📅 20:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29961">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T12r44gwfZo920TqXaexXkvzegEbPR1IRcnmJP6-fNAIbPUTmG3WlzZe61iHO5UvUTgfzkrGiCrwR6BDLDY3nuwl-u29CvqbVa6NTrI0wnWBDUw8SRgttslRu3obwJt66xf5reoYzlzT40aS7LmygylndU3zMvTQu5ZxzwAdlgdIi3rcBktLVDE38jzylVaQu5uX8WVk8fA6mi8ZYSeOXXZlc4tb42biC0jXBBvzFe6tvSmG_os5z5ntoFP12e1VXtniKtY2SUDLqrvHu3c806Xo22-XMhb9--9GawXPqfF_FGQ9zpAahD2sT3WSEg-ub1vG5q78UT8Wt5Rk2FGiVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگهداری درست از کنسول بازی، عمرش رو بیشتر می‌کنه! اگه داری این‌نکات رو رعایت کن و قدرش رو بدون. الان‌شده‌حدود 300 تومن. دوهفته‌دیگه 400.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29961" target="_blank">📅 20:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29960">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdgfJCGD9J0thaOwRKazGesbfthxtnWpJGEMCI1PXQyS7V-3JUyyY61q9V-jJnNOjyVl1p3N4YV0vDDvINLMxmhupI6S5nXYzStWfsQOR52SF3DXeAVXYE5RlJX8lI-MByolGB6EOI_GkaCDNBAHE139mJvwnPIC6ynvhWyfRwEBJLht0jvO8ElLNVkEhEp-vfUZU41dDMYYYkhW2ODPcQpCkDKV4sVJpa46D3AamFODZnEv5AuSj69TU_dXnRmxNzNSgwThR28ZuQClDJqDumEc2eI2Fu5gRi-QHEp3K0pQq_d1n3NbfvcifS6ZvbMSyaDxTnNBzeTq9Xig5KXJUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه‌اتلتیک: جی‌جی گابریل ستاره 15 ساله منچستریونایتد تصمیم‌نهایی‌خود را گرفته و بزودی با عقدقراردادی 10 ساله به رئال‌مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29960" target="_blank">📅 20:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29959">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfTSADjvqyDO_hS-_m5QruOf4hPhE7FekqZqBt8_95ayScQHT75FDjjrg3D4padHWlGGuREkiVpawmWJQ_OfWKI9XR3iBY_ML5JXK2MjUOL2c0skeA6oAY7yRDNQAle3i8nUoG1KV9rJa1AJlIkuty4p4sa7uTZxG_mZGRf7MtRquCdyu0Jr1OXf5LGXpMJUW9B22leF0WvHFTItIwkvh7D4S6xVyqBq9__RQIRubOrVY-ZhncWXjS4kIuGOWU0klIGyMJot0emqJV5IyxxQpSSBcfWwD7WvBH-XEh7meziIwWMqPY2PoJRLCpOG5cmVuPskiweqmrnLwwbrY72MUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بازیکنان رکوردار بیشترین تعداد جام در کل دوران‌حرفه‌ایشون؛ لیونل مسی با 49 جام بااختلاف پر افتخار ترین بازیکنان تاریخ مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29959" target="_blank">📅 19:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29958">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q05U9kbxys5Lm7ZFvjZ_0ufYF2O4nIyy7KzXjyz6uPdiYw9tB0j13BbKulSjNmXDExcOK3fz7J7tw82hGa2N5e2mBIu--4nwz3iFUlzpTLTt04etGPUvN5Mv47o4Rq9j6-pmm7Zmj3BdOF0b9nNosm42f18XTZfnjIxXoHlOmF05qxviUJ0h_kIbtNt5Gw50iwdY9tr1wR8R_DNRG9g1recXGA_1INEzQjS8tKGATIK5W77e21065dcwgYFFL-cpQ3NYD1L4-WEt7JJuovrAm5TPliPWBCCig-o6ryUeVu7TwhAUphaBHQHesoxDYBld2cbrvlPXKK2GBvrR-mAuyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیریت باشگاه استقلال قصد داره در پنجره نقل و انتقالات نیم فصل قراردادی‌ جدید به‌مدت سه فصل دیگر با یاسر آسانی فوق ستاره آلبانیایی خود امضا کند. آسانی از طریق مدیربرنامه های خود موافقت خود را برای بستن قرارداد جدید با آبی پوشان…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29958" target="_blank">📅 19:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29957">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_w-ykDJ4y8AnIgWQs7tMysg4YA6bdwUYT_nT2V7xfye0xsbQBRle_rPp_rDiNX2wfM9BpeedMRJlrjplFckLtKXldqjEc8f0wf45oieomXodyjdDzPiRLNdLXCoAvAeLNtzcF4NIEmRhPhGy4k7bSUdF22o9Xz3f6ziVVNPjRvnlHvIqYT4Gsc2FWBctOLsrKqdw40O9VvVR6dBt1YYD6BhoyPPYZ11krKNA-WhQ6TLXzkeP7HoWPeVWaF3imfq_64ZxXvlfuA10NcMo8bxlauxd_auAOZGRYQ-Rgxx4U203kyt4Y5NN2TonxEnYH8reAS-6WBPCXaDLwh7cdWngQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه پرسپولیس میخواد درپایان جام ملت‌های آسیا برانکو ایوانکوویچ‌سرمربی‌سابق سرخپوشان روبعنوان مدیر فنی این باشگاه به جمع سرخ پوشان برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29957" target="_blank">📅 19:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29956">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J38zcvl6bx4wbaauuN08zs1cm7soHGBR_XbfU1L4MXjlK1FUG73wKG-kGGe2XYKw-tJ-xf3iEjFbkU0PKWCY0mJ-Fue_iMBVOOKNi0eh1ek4fuVdWUWvZUyOGgYC-XDdCBgU4EvH7zdeJI_t96GykG9BEtUtFf5tCfpqnc5iWblOhE3GixW4H7EwdSGg6t8deMzvdUcEq8BJG65PIPlvriSs8s1aHUH9e47qkpPpYWmSlVgVoELijW5lBBaycSgYMfaqfo2ZzbqNned0cTbA_UO4SzMMg2MVCzTuZdKRC5lCOegB1oCb1bYZTVa2VakBDxzwE-PLCSw8_UXo994hQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرد پرافتخار کروات روی نیمکت امارات؛ زلاتکو دالیچ سرمربی‌سابق تیم ملی کرواسی با قراردادی سه ساله هدایت تیم ملی امارات را بر عهده گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29956" target="_blank">📅 18:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29955">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ln3JK31ydQvDXUvecr3l07W6yD_Edq44RHhG5AAU3VdRoQ7WRhX6_dRPliaLsI6_CghDZVxGjCuDI-6qjZbS44GCI-57WWCPt7nqjyk4lUqtw_OGSMEjLVFvyvHnth2vT5zKW0whgBY6UeOsjsZqgF0-hk6TCwtEb3gpYUJng2V7NqcUGtJzHUaRK6OxbAdQt-LqjRBrb1O-M_Hmy1kRH6Bg0BsRfRpUklHHj9_neMKeKZ2-JleXf7Wlx0L3p0AIqaC7nnVW3INHLhj9TTRXIDfu0hbeKVQFjbjb6s4QD05xRdL-Po_NEUdgLut2hs6SpM_s7LTpZD8zL5xh60CIHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
ارزش باشگاه‌های لیگ برتر ایران براساس آخرین اپدیت سایت ترانسفر مارکت؛ پرسپولیس ارزشمند ترین تیم این فصل لیگ برتر ایران لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29955" target="_blank">📅 18:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29954">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7c4dede4f.mp4?token=pHSMHs-a9eTQAhDAdtK3B819jd3IejNUxi_OgpU85kGLV5H01BHGSJAeLCq1fIihbh_q8M7ydipHU1tHnszl6edXurNYafY1BUfH6mEhhiZ85p8kD2uGZU14KL7nU_5LbFt6tPYn1xLiRxJC_9ef87tT0XzR0_EIj1wpyRhBiEumdkGJ62uA2yznCQ9YcvBav_kQkcC-6Kmn5VgtfmoAjEKTiQb-2BdOyu-GaRAmzYwG-atYFoqTYZxM7PrT-gee5oQF2pN1TOAZI67Jr3FYIQo5xLyJFO0tiYCN0CYsXZSzXyUI4PQGgD3YEm9ZH34wkkCYzevQ8964RoJLaVSeuYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7c4dede4f.mp4?token=pHSMHs-a9eTQAhDAdtK3B819jd3IejNUxi_OgpU85kGLV5H01BHGSJAeLCq1fIihbh_q8M7ydipHU1tHnszl6edXurNYafY1BUfH6mEhhiZ85p8kD2uGZU14KL7nU_5LbFt6tPYn1xLiRxJC_9ef87tT0XzR0_EIj1wpyRhBiEumdkGJ62uA2yznCQ9YcvBav_kQkcC-6Kmn5VgtfmoAjEKTiQb-2BdOyu-GaRAmzYwG-atYFoqTYZxM7PrT-gee5oQF2pN1TOAZI67Jr3FYIQo5xLyJFO0tiYCN0CYsXZSzXyUI4PQGgD3YEm9ZH34wkkCYzevQ8964RoJLaVSeuYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری عجیب‌وغریب علی فروتن از سکانسی که باعث توقیف کامل برنامه فیتیله‌‌ای‌ ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29954" target="_blank">📅 18:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29952">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWGDqvS5L0FL18RfTDFXKzjqaR1Y0tpJDDf-VBauC5DDcUI7yBvvaHHVnH-9dNZRsWfk6xV17D6zyf7wHYVtmylaAvC888QRjEBBTHhGtOX79_QeWCOh1MnQw9QYSd8cCznXc-cFuCCn0vdnroEU9Eo8leKfCQuTQe9XBXSXpBmPUG2UHSikvrVRi9QddaC5ePzlNjP5n0cjPMjTkuNY7bwuOdBnieyLZK-qAXPFKDhEELeIsF-o2FuYDvSTXK4QkFio3sUOUF57Ree7PO1bHOWLK1eLXts4bwJdrzzFIAI6wvwlC26tF9SiscZxopbG2PNansKqL9jEcEQrn1Q8oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29952" target="_blank">📅 18:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29951">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlBTLLIzPSoWvBNtH-Ig8x95DSxJoujlLbkum721hkI6hJXkL8MoWAHsVwLpoSBMNIyp5grsN3fVACmQhqik1tWa2_kl5ekn9HSxkM9q-nT39N8qIZICOnCxadVvXMYCMyocyuF2T-w3Y9Pv5JevZMTo4xWwenXgR5aQxs4TJ7sclejnxVc5mZgJE2BqF7EhhaU6snswcN_OuAT1LBHvyvqQ5675XjDi_UlXqQ6Mk220nSz6Ku7-DFnkHvingT0TVY_eEirEzTWAtJDMqJnbdYGs3TS1TqrGV0qNFJj-OpxxvBAuee4Sgv_tsT77tV96uU2z46oNh-CpSj6bZLWU0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌سوپرجام اسپانیا
؛ بارسلونا و اتلتیکو روز 13 بهمن‌ساعت 23:30 به مصاف هم میرند. روز بعد همون ساعت رئال باسوسیداد بازی میکنه. برنده این دوبازی مسابقه فینال سوپرکاپ رو برگزار میکنن که روز 17 بهمن ماه ساعت 23:30 برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29951" target="_blank">📅 18:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29950">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrttanpmy8EQNUzzLJujAJ145Xr9YdHR-gNiaTvVVRPl84AkOirGSdAQgTzaVDJs58c3R2ZoZsZXJ75ZmBt3nuEPPsfnTGbSQ_F3HoGCA6kpY8Mz86MD5vru_sCljMdrPP8O8T6KE1SBAbqAxpUQTnOhnixR2zWxwF9gZiD79iDZ7I-DN8Q0oTIoRelRaVGM67zkNdruwCvPzFpJ9LzV-I-7J2v_sHCvVu78XtVGyxxNrrflB3Bs7hkvtgtSFLL6xT2uNdPojZTD9EuMPmQxJAzfmU7RAYxG_QDB6hRk1HVgb4ySKD2zqs97HTnTS5QKfM-P-U0Ur9iWi2O0ZqdCAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌پیگیری‌های‌خودراانجام داده و در تلاشه تا علیرضاجهانبخش رو نیم فصل به این تیم ببره. جهانبخش از اول دی ماه سرباز خواهد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29950" target="_blank">📅 17:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29949">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5HzLJDtqn0H-lQaVCz8260GcS9fywmIcJnt22V6EPmOqlJ03IbDTy38vcPsMp0nTmQDSE8VJmWIJYtKG4-qS7XqaNHr68Mc9yDYgv8wg8Z_tI1XNYkCnRhJuXy27LYcjXFaVNUKnJJf707Eq2IN8gqUt1oHGObkgi5eB2FrkS1lnGhhtSOmVsG_fJUHMLbcvk19EfIN5jqMzYgN26eBDV2V51WSAVPW9mE0jtLFURhbKnKZ2YzqCF17tNAv3Uhz-8Powiv-QCeZUtNtHJgloQ40ER_qxd-Q7QqxQVYXcy0wEH04iTU3cx_IsIYxAg6qwAD44D_7HkrfwQFsQ4d8Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29949" target="_blank">📅 17:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29948">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sR7_jYziTu1tIKpNyYfNlwAeymDqr0Sw8Qz-KCMKXWRET8obsSPybOBmn0M69agqTDdgF4HQPns9vP8sKuzexLlOJBLJz-LUV2rs8xxSQJlz7MuK284Pf65OCRUkgNsInrVak6nPtRdBD_Ywg7yPM3Yr1hlxO74hwLSpD3Kvf932bqm_CS3hl5PjGKogTc2T7Fy8W-_sGttIiQc--xU2EKgzlZzffdF0WSjlgG2JwLZh7YGFZaCZzjeabJrF46MjUBvDmOlvXXMOKmKl94sqNjyEULglucqoCFgF-w9duSRJWyHxTOp81EgNGtSrXVfrk1pw7ALeVW87a1ZNRKqwtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بااعلام کادرپزشکی باشگاه استقلال؛ حبیب فرعباسی دروازه بان مصدوم آبی‌ ها به دیدار شانزده مهر با تراکتور در هفته هشتم لیگ برتر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29948" target="_blank">📅 16:41 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
