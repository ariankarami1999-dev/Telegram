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
<img src="https://cdn4.telesco.pe/file/hOTE7QUM6m_9PsZfirNGW4AHVt4kHsZ40Hu_7J9ERg3khoOu4G8cMub_OiuTMtgQoCcCJJ6hXhwuVm__dDRQz3smlnFMjOF9zXqDSdTvORhGXNdlZWKmRlqJEqY9TDLYP5peIhGkTCzqENcLGGJUxHLnTCe8j-GuzpiFxLlhX8pfdGh3F0CbfGjyEN6bC79Wo472GyW_BRY7-ktDrVt08X23S5nVI4l7QMNVLauFZZGgaZqqNyKQZPEd_u4QCpIwTTz9uHtCxta3t08jnibATlEYJkvCUymtV1t2lOHb0fVkILMNqPVkC09Et1oT-YL8dRr3xIo8AHQBBMesnSop6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 424K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 08:26:15</div>
<hr>

<div class="tg-post" id="msg-25410">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWguu9UU-Ll0EyXY0O2akFAK1KJkVhjcKuKy_EwQd8yM95_jQzlt0jVXVfJqi2sVwB3GGTafhu0g1cw2dS2tYyM_VoYwKHFArgw44oauNhHE3jlhy8U4YqEU8T68bxK_xSfcD9RlvSMzt7Fg9DrxA283NXeRooI8VKGOukAXdCna-VuxZ3wC96--vDqyYIIwbiddRQ-d6K9Q3tykDqrVy5eacmbvodDyBFD6-8eFD6SBy4XK4duG2BTxstEvhMd10r0dKlUUE360m9SyCjEIFC0hCq3zcP-0gzdbzihG3YI0LKfG1o5UabzG-smgP3eLfxaF_mOxW3drRw4cfjV7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/25410" target="_blank">📅 03:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25409">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nbf3L-WYiMBbsJARhkm7wmeUp9I1AKDTp9_0Rj5ERb__PvIPdEnjh08IKyXJPpDfXbQcOnSGO2xkyf8G0FmE1HIaHxRDkMrGGUtTFtAsrq5ErNhCyPBN574pddNuK7N9M_OA5DmIxg_ZcDYfh1qVeb7sruHfkd3rCnbJxXCF0sCYHk4Xwxyc4k0H73cX_p-EwqmpHtd9VgvN_7ePSuYXuh-eCqOZgWWZ4W4OVpu_8jTD0CgARkJ19iRXAgNA5XxngpbpFiTOFkDF6sdxmmXfb5d87zVYujzuuwvkjPpRTSKJy-aGOesk8kn37UgH1ujdWMV8_LxYw6r0xaisV4WiYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#نقل‌وانتقالات|نشریه آاس اسپانیا: بردلی بارکولا ستاره تیم ملی فرانسه تصمیم نهایی‌ اش رو برای پیوستن به بارسا گرفته و درصورتیکه لاپورتا با ناصرالخلیفی به‌توافق برسد این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/25409" target="_blank">📅 02:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25407">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=VhzmHr4Nls9wkGaCsr5M7XTwtbDL_FdFA3mzcGPNNc1t0g_dI2ivriILkh8EzgRjZJIQFvRjf3gnll_6WpHDLfw_MAQAFgGLf1XG41t5cMwdSv3Ah8NikFHo9hRTfU_w4veO1OGJY6e-y5cq12CaKCls9YwrhGtC1KF5p6yYQZc-CFli1a2GEQOX0MgDKF-smJt5Pgld6lCH8gl_Tw-N6X1pgcupWNYwZUTwin9TMoRk7hwZlg5swkOkyBD0chxY9buPdaft--VG5cXOmFpT8U3QsDIlV9rIVlGWJ8ppv-ZhfApxGaPIL787RS8BxnJEpRARZbVO0ZJn9LrLky-kWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=VhzmHr4Nls9wkGaCsr5M7XTwtbDL_FdFA3mzcGPNNc1t0g_dI2ivriILkh8EzgRjZJIQFvRjf3gnll_6WpHDLfw_MAQAFgGLf1XG41t5cMwdSv3Ah8NikFHo9hRTfU_w4veO1OGJY6e-y5cq12CaKCls9YwrhGtC1KF5p6yYQZc-CFli1a2GEQOX0MgDKF-smJt5Pgld6lCH8gl_Tw-N6X1pgcupWNYwZUTwin9TMoRk7hwZlg5swkOkyBD0chxY9buPdaft--VG5cXOmFpT8U3QsDIlV9rIVlGWJ8ppv-ZhfApxGaPIL787RS8BxnJEpRARZbVO0ZJn9LrLky-kWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/25407" target="_blank">📅 01:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25406">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSpuMgmbkm7GTXcCPF93jgZ_L66O9lQl3pMLPzD-KEl44ELFfHCZydQ_y3qkdKRnSlC2HAb7EoZYBP_D_pNeFuJ2g4HqAelj7J-g5EKN70Zm513Etg3urFi4DTr7ktUwvdcdEizb_cKRJQnbWsk7ST5OgYKDn64wzquy1iR8U6nZCAjHtzLKtQyJo-4REb3eqb-EACiKPmjt0OF8YYpZotrfNXj43RKJ4_TZ5QTZrdUjUTZkbIZmhTQs6u2gv2Hh8vI1E9u-j-oIibEG0j4lQ6pf3NnwaJLRFWuVfKLOHEUxxhTUxFqDQOF5rxzYxOU004fF_V6ojbEFwYYic6LnSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/25406" target="_blank">📅 01:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25405">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lzgyp31Wcyd0OnmCHIGmo78U9UYF8x6MHG_XfV3U3LpGmH7cFUbBTB7EvZ67t5r1YfbFJpIFkNNmKPxZoOjcOhzbjNqQ7zDhOIsWYBUwoIDbr3UzMcodwZZULHfsSk7KtYXeU-W5q3q2kpjITY5vYAfGc6aDHPD6GHUG6A06StCOABP4nMIfxcwoYn943mVVCXxo2HZtYBRobfkQoMTnYtEly-WMGILCRu8SCABSm87HiP8Hr782exuYamdOlP8Agemtxdmc7fr96Q3DObXiBNwwdHlpPpDHopIhhkvhalif7CXSzHY98gjnUv0FWDlk1P52Fr9Qnuet6s0wb2dolA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/25405" target="_blank">📅 01:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25404">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzZXCDF0_QMzXJe4WiwuPDz5JE6UGuxcMe3ohlQbr_1U9IYwEvSrMhofKMnFYV21GdhhY8yUYbiWzTus2XsV9zsDusoACGy02_cvvJ-veFffN5zsSD8vQ3CyBwzz8QTlxKAs-zJrJNXV-30MZcMmLbjDT2bhuqCHqa7vGpJ7SXZH0GUuIEnl3b63qRikMAdq-jH00p2IMvnMtjDbkkHNiXJmSoa5Rd_ByKIAV_8fSXL-0BTYb_EuasE15tVFWvF5JIrrWbxzgkD-JkDoeJDmYoWdtN2LlCset-pDOr0dmyR7UBYL-_x-4PVVI-I7584cuPQEA2a10GYK9Pm6LoMv2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌بامداد‌فردا؛
از نبرد انگلیس مقابل وایکینگ‌ها تا جدال مسی و یارانش با سوئیس
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/25404" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25403">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQgvXUZGDtq8f0Iyz4QpwlALcMjZwC41j-YdumBrdpdX-ofekd7JBi8xQtJQQFk1ycnGuslzjsi8Fh54qgVS3oPh1HylfzTi6upD9hd7YkUDDyQY6mCwSDE8W-hPO0QhHDZaQy9pNxhvC7X0FMMW3ElZJE3DOIAnTijzRxS-0YjFeKyhmPNs2bLam1-5iYuR-Hue9kACCDWU_k0W3u2zL10WbUyMXQodQJTXmigtSf6LvdXjQ54JYeu9QuMRTyJji3HiUVWuyB-S9YN7Eij15uLtt6UJH4qqNzgEWQVKSv3EyskA3jUkyXinAtYdVAGyON-h5ZmPaHw8W7PZSZBwkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دیدار‌ دیروز؛
سومین صعود تاریخ لاروخا به‌نیمه‌نهایی جام‌جهانی با گلزنی مجدد میکل مرینو
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/25403" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25402">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AKehVAcFzWjHW4dpkiWf_WO4jCLolAysnK2HEi-Q2DmZyR5UspgtCpe-NXi-Of1qGUMrXNQZFqAl8RlCxgmoGJL4gXIRAJqhL0OFgyN5C5nteDVqHHrsXjdWBT590GMWKpFZQ139nvEEVUb1P24A9PvNRnD7ZrJOTwJKEJq6DloeeFTbHtJQ4_Sn2DSjvExH_-_I0fzU8UR1x-66Kui7AODtJGd_vG00rKVcwQdTQGkl3PKdKS0_hBacwYeh9Z9QO6OlaGVkBhOrH9CYSpbtkzuDtkMCnFtSlLiExu8JmKXhwM4ktznTWXBDz_NfJaU5PUgn2_p3I9Fhe9gssW-fYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توچنل‌بتمون‌هرشب‌داریم به دهن سایتارپ سرویس میکنیم
💥
ماهیچ‌فروش‌فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/25402" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25401">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKeBVCt5h1jliEAd0ese7tmPt5ogxGuYq6I9YGOum-x0bC76eKeCQtYrlRUSzUfnbH78wM-F8s3zrwvI_NL747pBQp60pMg0UTLZKTxfQa3oMOPRPjAT6qa9GlK1-9wDUBRdUFUIQSgiqYppPVsMsKU-FnNoN6pGqNa4TJB0rg9OeKxinee-_o89rGivKZI1-gTsTLMYjFrZERe5qSoSqMoholZSuTQwPo8QmF9rHVD5ihJzwMtSZ-JhyuDw1zbws-6ygW3xBPD8njjKstcRaq73FVAVmBmhG-Ynfk-tOsr6tW0iYByTmI_5TwnibjNfj6nu2XtqoZsVRw9QWN-0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/25401" target="_blank">📅 00:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25400">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1yT2uz2ZZs2ZAOUCSBabcnN4fj_MPtQHO7SoxZED-7BFRsd681xtaMpMobgopTeCN6x2IBg97K8TxpPz0grnJw_wFFwn2DJuHnVhDb_LPwH6nhQoq6QZJRf2nXkMlgjbenf_KJKWAv7FsopGicaGlwgjiiAvVk6GYg7IXy_YiNbc8FbG7sajSWD1NO3bkyiFvTJhbqOd4dE44mvfMfnL8SMVkPovPxtYohWz4gFuMdKhznHdvy-Jt9gNRZeC6pchAYW38LqYCJkk6tJCGQJ-JNlHd-q6vAq8HbLcXXEYpWB8lPPUFBh9IYV5bxTcc1JZFSjX9GASRR4iWr_p-66gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دو تیم اسپانیا
🆚
بلژیک؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/25400" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25399">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7G1V4OsRS2w5l2i2gMa5V95OhXYBHn2BUC4fPS4ghNVqyxGOGLuUcTlsgDxocFZXynS85JzWy3q1CwxgHdQ5jYEAM6Ih4nwiQkU7l7cWQwdsuin7d464x2MVzCidte23of9FPshv1TU-Sqg_Z2x6aPUqRnenpOfzH0YMm8mnpT9a1WO0OlqyUO80yRVQDz2fOpt_lFhETk8R89STd-Lsl1_W0_8IulJRtp5cgf0S7uPB3p1kr0WNtZywbMExaTG5-83oEeu6kIzUB2yjPJTQ6htxxMSirMUhiBBN7v8bwRCwwjkEzSSGpCMyynCql5q90X4QHY0f5k-MC-Mr8f35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/25399" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25398">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIX5c4QIgqOxQaKphC5SFr9J6eP9Enwkh_S7xK2vXNTOwrRXoQsWRHCDHGY-cTeaZ5K9G1OKh7j--4hJ5zuTmxB3vPalIb7sdVXbe9qEPUAYlYkJJ7xHckjRsM46M9i7Ybyame_pfrKrafc2_arQOkEoUch0obpwq2jppadPWris5Cl6b1yrPQV9n2tVT10RUREMNebsWfgtXiXmiPnYHz6wq66XAPZFnC90nh1wpf4NkHhj5QDJAn-Bs9hPl8QnKvskcs9J7XEf8jnVWIVjGLkCiZRvXWeM6Rijrajd2Nw5f4LVZzcdabYA2tWdpiMhp4fAzsfPES2pIbhAUYH6cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛
صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/25398" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25397">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2Rc4CtwFINz-euCeStzljOLei7JlRtRLJQy7ge6qtqlUHVV3eNJjkMFSKCJPKutWBzxy2AQq7brXFP6Rb04nsiT4ofFjZGNZVrxICHWAjqXyZIwbLbf5gyUt-kHRybDGMJTe8INOG3pic8ZzVGfHZgZqTa62RerBe_x1BJKwasbwrsTkShYrPF1x34J8jUhCWtg-jRgrcCxUGuGUMbh5p9_W6OryKsthmzZtNOAlWgke4ivnxGn6cidaKtzhofGVLBhosfeas4dDlBQaaTAPCP9DiMwUMcL4ekBDljxpHRmFqAghWSeknsDqoM64NGZBWpFXhNs83kBVrbSK-Cwtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25397" target="_blank">📅 00:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25396">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndqQ9imSJ1dVHsy4BHOBmfGh52gb1wER99d_qMZBXUM_JLcqqaK7bBLa_zX1FqmIbYnqrTmLPDI0GMs9Rl96af-yly6QXAAX1oNABqW_yUKi4ZBFAiC5BVliUoSSTviR8bTHiThb4vAFfQWY99YrMglA-KMYkavFllxpDZ5tCIsvEKQ75XKsT8DJvIxQ22aKQ3Ahh5lSOHytKZ5c9TQC-uiYewq8XRWiV6UCal0KDA8Ujq27Qxw-67y80JhgcNFhb2kXNIE41GikHk7YMk2r_Akj0slRlUtmbIkZVT83KqRU-bYoBR9j2e3C5s_nWfsPajy0boSGgqVy8M_gMW4IGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/25396" target="_blank">📅 00:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25395">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCyI3h7CdSXfOTanNHzaZY1vvirSOjzbMekUVFQuTzdIepP_62jUKjS8Uqo-C30fLyxMMDHjDRGP3B_EerMDXSR4DhbnUOhqgYSB0zuWgOwcTivsHGby7uJtpJfdQpi3Akye31vKQC1xCXSnq6BkDpwIKMFhFiykNQcH5MJx0On3ed_SQzEFBc2zTkjkwWDKKrF1bnRejw6pSXwlRdN_xh6nDHJJVwD1_U7gzvdHwCCknNnuefhG4Z1UhwlVxzaNAVRSTfUt7k0rUmLSrPGO9NjUtBlUwQED1_s0M_QZ0QK705ed7bRe4vvmEHg66EbTEzx7KHNumYZcCroxurVU7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25395" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25394">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdkfdgH8VDVZKikJAGS-tHqza0NX_LbEIQr7ShnkVqf8Jc4i3W9aKpEFkDKUQ-Xzs4DIvcF5C4LGOiiH5NpyZxSDVeL5oKLbnZ1czBeQMrIUiz2j49YF8mgktRMslaCBS8psWqWkSnU-GIJhvYtxs6fZvWxrzcOZzoEsOGIamMIltM83aEhtF1mm5crlci68Okj8usmlHYpSsN1CrHSJyHV3zx706qfIgxxnBEd-BnrlmXqaQW95TosMiKv9sz7Jq_JBISCyx7G-GsXiol7waX1GSFJ8KaHnq_e-2xaXqLIb8h9ViCtimUVduuk4tzZzXEqXCY0FwPbsD3dKmIXQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25394" target="_blank">📅 23:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25392">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKafCsAWx3Jk4qCe3vjb6UoCDXsNx_rGIaxBsYmwHFIG5N25a0FH-zmQ80GDgZ6qnq7Y_d7bIrvsXtkbOwNczPByhTm1ye0K01upuLDQOpznIE68SKMRWGbvkQLRdx28La9Vn54JtHGI6z-gwjJcMz2rzbxFkDsBvAK_fx1ynYCd_QwcA54cdKpK-vaW31XBbkKWraPBTiZjjSA_P3jIblM974NySBZ7e0s-P0i8KlJyfRhEsuljz6XD74SkXXNRcVgCeUUtzDSIMd05xnIX9GDCCuY6gXbrdkiVgzJlIzLHHb813i__ZUSYiVObLYsuBxA2HOxTs8wwDKvysPLL4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bL4m_RTOwkpu_diztFnW9lf4yvcOIqSbcRzoH1qx4lur01djzBuD0TO2jJ6t0P9U7t7UNjR0pHpZrFP1wsOBxh8yAsHZxjq4si7A9XWQ3MHy9IO-viM_aDsFuAAAcXN0YKIPAnTrbQRG4py0L6btaP3q4c7songFaq0n_9u-GnR-d_7poI6oivQ6tLE5GfzO-3rGEf8h_JnyU5Elplfhi6GEor-hezxpcGo_15oTzz5BRexm_znCX2QwfTmGXjBLeVziuIkw6qc_9WJaQISzxG55prRc8CigvsSvTj6iCgPNwKas0Bec-Oqt0j1Pbecc5_8IuWsnwcKLpxGyXtm3fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25392" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25391">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLWXykUQGfzj9sACsoCI0DIjk7Ayu9RB4M83ktoAWZ_wkU9H-DCOVGLSX0_PNaJXDfvfDKav3fSV6fPbS3efBnM_uKY088JHvojlA0YfNzXlQkTnyS7VcJJoPVh__PW-sqA6ss63z-XSXjMU3O8yyx_DKxiUAiKG2kkOq-dViRUeLjhuN-JqgIbhc_1nlQM9XqQk60mKFg_W-K4Mat0zzGPYxeYU-AuK3hVAu1to43H-IH9x0M8w1Ix1ylI7igvWiZ4cAqlo1awZXASdyIRC6EVOjGnbJmVCvP-6v5akr465L09MoKoB_cc7a4flIcSfHAEuWvipNxtU8qLRDjkHDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25391" target="_blank">📅 22:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25390">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTemXLV_bWU54sQCvmTXJk9ozAiBjZ9mkbeeolUfzsMLjklG3lYNWVUF0-PPDS_bLZ_P7MwRYyD8LbRfiGUalxiLQBuocWkWSjW8aZiruGT1GJXwT7-liHpJwYixy3ZuWQOENFpEcP3_UjDtO7X6HjKQA7KfQNLjNp1IkT2U2htIXnOvow8XL_6BnOYM4WDBnhh_cUYiQVMhuC1cKP7ElNCsXgtj498dJENqsDIwMncjQ-FZy-xdTssqkrDNDjnkWWJ1l3tPXY-jkyfglo0f8bUuoJu2XNTXEUh84LQ9KWgvPvk0EzTDbo19em1r2hRUyE7TdEJi95QHhSVCtGiYwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25390" target="_blank">📅 22:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25389">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzTfmTIhSPNQ0sAQ9yGrDQeuGWTsd_6X1AjF-2xNLYr2MZvTviMUmsvL9CwQfWHj4_0Y-7YLHz6kNvy4PXM6ovQPIUpM5YkF0Ck5LX0bCXFKxj9bMT-smEgIxo-eX3MIqvI-ubg-LIAqbgj2jU3fTQU3kdzXQErQQRzg8_RFBoFffn-oaAXaBBFh_OczACg5hjwnZqqOLk51nbXKb-_z5pW6jGff96szsEI8-4jAkJ0FDBIIatWdoCmTlFOV0ZZYaHhp1LOZpuybs6PvZPNQQYJTjeHrkpXrQQtx1X2yXu19OJZeEY3uLAneR-HMqh3owNx4Nhr3nBg4SXRecEm8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/persiana_Soccer/25389" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25388">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3JFmogo_WIjTYSXCEe2fIfzgw1XPlKdDNPy9BmOL1qjgO4Sdl1if2fDFZkh67BLNWRY-QK3Bi0Ybi-Rrs5PFdCaZGwQc12LHOWuCWLard6YctdcxZFWGiwtNGCcjZvkuAPiFQKGLpvrMdjxi_NFT8BfW9-VyPcaRBcxl3Aze_tan0FQdNoUuPhTIH5qLxed2Kzi9FwrOxlfFAM9DmgRdidvYHo2wdHXrCMVefrNyL6nrCTJzSVOg0rTE9W90fGtF_Jkxb0vjeZ_ngqcuL63LqAYHiua48mAFi7pJGN7Z11rEba6d3f16Qgr0WZxsL9cb2oFRnhOqHC1JjX3liN6pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/persiana_Soccer/25388" target="_blank">📅 21:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25387">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYhNRHXxI-R2a-p66VfCr4qcgcvuqjT_OT8s0Mo6KollsL8IlYuQlDY4AnHghVlWVVMulXG8WVtumtNaO06j6hhimjtQ3rHvv9A9Ma0CznajVOhx07FTUN74TbMhebP-7fYDXoH0m3CHCvWErOCepl7lDK_qvYnp6LfYp3X6YLv0CznUczCy2sa_0VrOM0KsZTd90iRVWiJjana7iSU_ZVXw4WeTrki_MJpLUdsCIMS7MlszhBufUMJE1jjHKGsNae5xBaXKmooIyvAJAp_ZO1hEI3RO-u3Jpettr8nWeKy8jMI3qFPjlnBSuWK2lfIOy4e8_tbIkBRwkNO43W-4FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تایید شد...با اعلام رومانو؛ کریم آدیمی ستاره دورتموند با عقد قراردادی 5 ساله به بارسا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/persiana_Soccer/25387" target="_blank">📅 21:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25385">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bRheRWbXZaVNtwmufKtFgMRJ2iOR3r_y0x1-9HHt9FOqCXlHqCDREyqZFdLWkXB1g9gk6vvgHWsrFCPIRVvDYqe2bmqdo-eookibACccIsl8DAOXuA08XDiIJ5ZaCIBn4KUn50vv37fKZCznI8kg0b3yfBrliYjOQ7pAoqPhHLdZZyziqMfCE0xKaN4hMqUEQ--m6Ob6WE0BwEacxS64-vu1vCFxdwAUozo5ddi1IXJameIuv21eM5Rfan-k4RPYrJK9RShqj79SXDEsmsUXkro2LZXnK1br6wLctfg1upEvi2a5YL6QlPn-p1NVb00ZiZKVpDho3OhnVYS4R8W0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWjRwW99JfXDa-p_hzOx4786H0qlFfU52BC7QcUNJGf65A3d4cWRTvD5kr0XPFszV4BzQQm1QAK3XkupmdOa2tWqVQebFeqpJHjLvm3MWE2xAx4a3Unh_i1Yvmebozj3Ul1VL5CgwsQynkMDM2bv_7XlL67pQawI3yJjXdcMLmcGacnjPvxafJUzBFhlrozorIxyqvQP3ILM5ibgMiS_jEm7VVgvUoMDuT2nq4AxPTLPyVSZ1aPJ_Nleezn_QRK2THIopl5emogII59NLhDttmdJqIOY-P-HeRElO7GHzfr5wE_enQ3D559FMlEs56uv6qpZjNPquhDWs15mGMJo5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25385" target="_blank">📅 21:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25384">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVGLBt7DnDRg7x0kzIU_qQUhgD1RYDRDAebx7NbM1tzIAYLBi3pPrjFcv8nEjVLg7whLiH_jrdnDZaUTDXzwASkMzPAQaI-4ydCCtCK3MBu6O-XXKwnaQlKfAYe6lgPE6Z3pBxat0wn8ww59_ExJU0SxATW2YK4MpYLlWxVX23pwEcVn_VheRyWUvAgA7DlC4oeHBSYTMn4ZMhrvVro0YYshY1LIoLERftTq7ZYlWmZoOPTMzGuNmS0ULuxF7a5sFKjMIFmBKflJDGWbn3IN4fkUn13MNzBE9tOm7nn2wjYawEKWFXgChLiD9vW1-BwpJ7_NMq-tnLXEXqlDI3Vg-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ رقم قرارداد ابوالفصل جلالی سال اولش 55 میلیاردتومان‌ثبت‌شده‌است و سال دوم 70 میلیارد تومان بدون آپشن. در ازای هر 5 پاس گل 10 میلیارد تومان به رقم قرارداد او اصافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25384" target="_blank">📅 21:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25383">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEDFvtInPwnHZHnWzbVScXl56lzWagmsX6B4jPve7nR-JrMJiDxVvozFRM7ppi1qheFnLwAG_vx3NxSSB4AiGZ_hsYNA1PI5v3B5KqRQ9pu43AFFwRqRoItPGveSJrTM0jmEUGtXbVIZK-e2bW7rkcyzqcNmtJ2lcyCBkyPsEskniaUTaPKMKUO-BX2LaH4X9_1iwTxdNmqH7T-8oPs9c4Qg2VVc9A0hDQ2m92Ax2-XsqUypmr0qKsrNqeNebT0B5TIsQe0KQi1h3raKsww5dxUkamvKFqJjIgCdM9zzkOKUpoj2ylmRPPSfiBzDdb0lcXyPCjIs73fM1bKkftqhCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
#تکمیلی؛ رامین رضاییان ستاره فوتبال ایران یک پیشنهاد دیگر از المریانیزدریافت کرده. درصورتی که با یکی از این باشگاه‌ها به توافق برسد با پرداخت 200 هزار دلار به باشگاه‌استقلال قراردادش روباآبی‌ها فسخ خواهد کرد و راهی لالیگا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25383" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25382">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Enf8z0b1r6nL1cbtxMt1_X9-mgIKtIx4ULac3gELDZjjTeJmBNleEPyTHJMglOQ1fvwwgad_9lGClZ1CfQxTcnV4EsLyZn-mtNWV9UitBWlyf5s0YvVXnqK3yrOc740UnntFVtAh4JoYXCJlO3-nr6uTQmm3mjxaWqsYCu7FMRnub1WXNRHjfO3kXTcGWiupiwsCpQmXanyNO7tNyj-jD_UBWGgZohPiXaIW3LoGIG4YMae-IbcanyG--n8fac7FXKLygWH3w8K3RPnYETDcOXYwALkqjlVjlt19yBYANklT4BohdiPIQgRS_g99ok1RZhACxfd_Gm7aYNwr8aMFTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری #اختصاصی_پرشیانا؛ انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25382" target="_blank">📅 20:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25381">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWR3VOLOE-Dv0Ht8UvT00DXfTa3aN95tf8UJzVL5tFb1y2ObflZVGqh9SSrXdvS14z4b1WDzV8kPyAH4yO6XUceQDsbkgWW2a1kvUYyf5H1DYQPVDYp632_t5DhkrQ6i3Lm90sGEM_tZ08dQRu4SYEcl-jxK3rSpBPvNozLfDWp4t1zlJrNZ8dopHQOK21WTpzUc17RnqIW1vF9UcsluSjP3i_nlaUcoT_8tWaqfXzQATx9vRMQIf7O1ZuwcCrC8pmMRCfox5hq59j7rjof_QPyOvhgZkXlCBwSy2ezFBVIwLOTU9Y-uqvlh7hLNZ4eORJHRSauDpGauZtB493RuSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری
#اختصاصی_پرشیانا
؛
انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت کنه و درصورت صلاح دید کادرفنی با او قراردادی دو ساله امضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25381" target="_blank">📅 20:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25379">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXTArRShgcIv6NI1dKcf_yOzFXqiVlkvVlcevjIg9fWQLUornK1VzPpVVLlvDc41Lcu32-tdGo7MgGINqSb6MxDfJJpuUgITupC6sD-KptjSukKZoxfpyjnpHJSkJSOeJrWA8SLm-9QuIyyqo7AIJMRMz6Hb26Rkahd8InM7EM3ujNxFIm4nQDEtB1J15Zj4pz9X_xBrnVZbZhfAYjrP6tZmVaqt1Rb6YTOqkQL22QjYbjiFzvx52nGWHnZUhXNabUvuEz3TdZF7Ux5lYfelAqIpxBe8iomdzK7BCvacWjsJD0JKV0DCNjhZqCHzjpT_iz7U13_zCKv4ENsv05xU-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25379" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25378">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdJmA-pjvzZkZ7WYWKW2ONEbSpzhutNG5p2q9AgHkuH3pM87kqwqGCvBYOmUCqXtXoZWihSwbQMFD6xFrlrZLY3tWoBm42lR_QQLrK9QNCuv41enla6pJ6ppMkaHh1MJqLubwYtPEUoRAPNO5OJyLi2zKc4NGLCd409QNTURPPuJlL2QLXFeludIRuHE5tB46KVrGkEchMI2JeqkFEnIX7wZKb4clkJzOGOzBwyaF0qndgS5KUmjs4WIm1nHgjTZlI1YL_XCAWzVChN05ZmdKe1Al68sbxqmF6zagP9LW9Q-0ThBG89wDxxHeTINxWzxV_zCKsPPQ0sCwxqgTILi6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25378" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25377">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PO35uAQeUNpOOKbyQTPO-pyouQ6Q6j3Z-BQaqEzww7vN9z0LnDV5N8aO-icv9TJLLbrHEcyaRwsh-0nsa2-XTkfkfjkri4LAkHO8wghcj9ubxjAKuBxrAKqaQvkp46h6jLHl3dXYoM4brLuiwICD2EDgAWHRwCMCZ5Zf5zrqvKDQysTfEhvzObM9zORVBW6OyP2gG9ZwJlXVluplmuCDu7-RouwM60QwIDQggss3jLcyPUya0IS03BXytKt7aob5d_ecO4Ty7b0RbsxL2lzH2WXcQkM3hzZcMW69m_h5aqMQ_cVTKqJctAUhJdAU5wG7cPyBVnBEPaREXybN_bgoZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پیش‌بینی خودت را ثبت کن!
🇧🇪
بلژیک
🆚
🇪🇸
اسپانیا
🎁
۵۰۰ دلار جایزه
بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، مطابق قوانین سایت تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه.
👇
انتخاب شما کدام است؟
🇧🇪
بلژیک یا
🇪🇸
اسپانیا؟
🤖
برای ثبت پیش‌بینی روی لینک زیر کلیک کنید:
https://t.me/betegram_bot?start=p5_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/25377" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25376">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1bgWzt56rOE7X4iNnEx78lAT53FZ_GiyvESv4xn66LvcuQvYIdZ9zxu1GluOqyyIIZ1pUMeklGJp72I838ZmH2H5X3RgEajBB0yCwxT_XN3n7JTPynADUyPZAOyxH0wCeJTJ1HVEt1SJ_Y6sQwuJMcp2yd9CsWWDCIlIMPrCOKHt8Ld4C96Z69eZ4FABjtbeBKhegdl5RRQH6hH1wDKw_16le0T8VRjDRWTjhmDkGCzd3CLoJ4s1blnd2vf9bQVmNMnxYf7prlAGHY_pkQJOAhj0JADlQYzP-dz3IKLKxFaAemXL4DbKzNd2F43tyJ8b1Qro1ri3l1e0eBYZzsbsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باتوجه‌به‌صحبت‌های ایجنت حسین نژاد؛ با اینکه مبلغ بندفسخ قرارداد این‌بازیکن 8 میلیون دلار ثبت شده اما باتوجه‌به‌اینکه تنها یک فصل از قرارداد حسین نژاد باقی مونده به احتمال فراوان با دریافت سه‌میلیون دلار رضایت نامه‌اش صادرخواهدشد. سه میلیون دلار میشه چیزی…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25376" target="_blank">📅 20:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25375">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iv_2rzaxkxg2hQ3Smnudb0Us3gyAMnmRiolx4pE8LDDnHtbKYmEz6Alc6cOY_2jLthittR78QLsR1kg4vFDE-pDWtRQLHMVXj05iVq1c2rMeQOQsohlZ-K394jZoyaxmmBTBICiv0T_m8CbMsMaK-WESul1hck0Z4BGJr05MAFlgEVICz-8INAtJYVksYegBtH043ecZM4c6OLnpGvWf706D5n1ssK2Fh8OiOaoyU23b36VdlbLDaJbkbH22M4V4CbTOCWuZzvBc8PYdfyCmRKqvVJ3b9uD1Wl4xNGlwyiFDI7PQI0Th83oYHCJkFHSL9O0z2d1WoO5nPbEqj0n1bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
🇩🇪
#فوری؛ سران بارسا برسر انتقال کریم آدیمی به جمع شاگردان هانسی فلیک با سران بورسیا دورتموند به توافق کامل و نهایی رسیده و به زودی از خرید جدید خود رونمایی خواهد کرد. جذب آدیمی ربطی به پرونده جذب الوارز آرژانتینی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25375" target="_blank">📅 19:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25374">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pw94XRp8NVRqRcrQI3SEzEFdiEACnq2W-thb2hGahFU3SVQsO33AWVQFZhGiWdS22XOwse4T9MpiC5jCsLHlLJ0QRKvvbXMIRZhRzB8LFn9NzNRLEqd-PlI4ZG2oJYrDnrD1Tcddq2E66cuFoOJf7Ao8b6r7T5P5n5WYxekAeffACXKB7cOAPM9kCw4W-gx_7KuqxcaDnKf6gmmrg-Sf9MoV6_5tDdLB4Fzz72t9GcfyME6eayMC2PQGaqO66yaLyWvrF-nEEOYIMHNCBiOfCBVIFj8N_ZRHAKXBaK40MqgpAs6-oOZD-pCKPaqS3YgItN8fmM2HtxHzUVv7YCsv_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ ظرف 48 ساعت‌آینده "تایکشنبه" تکلیف نهایی دانیال ایری و پرسپولیسی‌ها مشخص‌‌میشود.باشگاه نساجی برای صدور رضایت نامه 500 هرار دلار خواسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25374" target="_blank">📅 19:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25373">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=OzglsWC7wZCM04muDKoiiOsAU0ppXuH6-VHRAQvV6ABDRrB3ckizIRZ3k_urHBsPztcrQ3E-qhirpO8ox1kvrQZswMTIgG1aEfPSDEi9OJO6sRTqQ_yFUNMbvFuS-zYzhh5fKfJJtnG2F-Ypl6jZOpW0EXAUn-zjuBjrDx6_x52jiOQDMkEPreE79E1KfrqsA_AtQge2_4e3tENrfDG_3DKmVOteY-r9uvHn47Wlbh2FFcG-RhG_NEiN5WAUW-oOLGlkKCKswrFuTYxmxQOa1uD3ER4_eXzwBG-4KvsoAkTE-E6X780ciNO7hHg7NCxinH0VoHhe1d4-2-PKnimeuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=OzglsWC7wZCM04muDKoiiOsAU0ppXuH6-VHRAQvV6ABDRrB3ckizIRZ3k_urHBsPztcrQ3E-qhirpO8ox1kvrQZswMTIgG1aEfPSDEi9OJO6sRTqQ_yFUNMbvFuS-zYzhh5fKfJJtnG2F-Ypl6jZOpW0EXAUn-zjuBjrDx6_x52jiOQDMkEPreE79E1KfrqsA_AtQge2_4e3tENrfDG_3DKmVOteY-r9uvHn47Wlbh2FFcG-RhG_NEiN5WAUW-oOLGlkKCKswrFuTYxmxQOa1uD3ER4_eXzwBG-4KvsoAkTE-E6X780ciNO7hHg7NCxinH0VoHhe1d4-2-PKnimeuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین فیروز کریمی در برنامه دیشب شبکه جم‌تیوی‌اسپورت درباره مربیان فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25373" target="_blank">📅 19:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25372">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WI6CI1n5HzvC6VMzUvkWoK7v9GtM3m9XZ1oZNlYu39v387CMOYYGJsIUjWz69T3E3b7ErlyLhrBveqHimYmV6qEQ0mosBRkF3-tnxo6WY61nBU1vWswRdACKAIzcI9RUz3v18o73R-Oi3xq-da3D-5QPmcfYzHJwpu4et8RDysrjDvXWmqVRH3eC833MMjQTh2ZND7jamAReu10bCdGbnoZSSLRMsTq2OX1yL704EaOpkVV1XndYAcJMHC0VpQ7otu4MFyowA7zK-1DbdizzS-sXyRSNpsYmQUElBhtyi_ZBPMtCpOf905PeMbPF7jsF29VKw4mJqYzZ64POMf97qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25372" target="_blank">📅 19:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25371">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMX__QZlTTXlv3dTotpxWC_99xBJ-go_Tz8P31EXWV4XOhPHffJlPMmCme0mLaMvQfupAhitOGTVz1Gp3JVmPitisi-4tKVq15e1OFxLat22PDRM8585I1de6aVEn5OamcI-YAS2wlIeREJhf7N6q7lbv1XeAr0MsvyZLQbSDl5AZ8XhrKiJ4kG7upCpN5sOtBM7Spqe9JRGuX9C9ndp5AswRTt_dWH8t3aWCxDGFNsWkfrSfDFDlvSG5ZsfcxvEoq-BNpj9XwHycgfH10d0Wryu3pxEl9fyagfN784H_3alTvak1t36Nxd4rZQwjbDyPtZSkDCmfIeSy1q-bTZe4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برترین‌گلزنان‌تاریخ‌جام‌های‌جهانی؛ رقابت برای شکستن رکوردها همچنان ادامه دارد، اما فعلاً لیونل مسی با۲۱گل در۳۱بازی در صدر جدول برترین گلزنان تاریخ جام‌ های جهانی قرار دارد. کیلیان امباپه با ۲۰ گل در تنها ۲۰ بازی، تنها یک گل با صدر فاصله دارد و جدی‌ترین مدعی…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25371" target="_blank">📅 18:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25370">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbC80gD5tTs0TqCqYVpVY0p5DnCIcs0MTc1UfP7ARsFqFXypKcPky8tHgERbzSO3GNc2zUsowNGdVuB6gyEyuGL8PIwbQysVIe17KyxcqiFTkceLkavDOfKOM8Vc1mHdC6hd4b12aOXawQflv0zyRjTjHfrIQqaeCdAmSkzCNMbtkX2DqGySek1RX_Ldrs3CG7nr5EtImYz8AeIp1wgnaYP3l02iNl-2RTAaa5DswslQ0pULY3J0XIiOV9238tVMDQpgiAQvYQebb-8pWg8jjSY5naayVEyissBgywMY3-bbtChylUtCy1DMzbHzuHB-HIJbQsvBKgewnV7NLC2k2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25370" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25369">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auXbF4AE5nFQjCT_qE46gSTaSthgW2veYLuINSi9XWqqJhLlPJYEkKpoRJD9yKR2FrYJSHm46judFP2pvHUQAUu8tKWikOlVzYYgf9t13nvcfFPfvI9Bv7aZYduSc14qeHVBANdkJPuloKAj6wP2SdFlRpRyJA74rFSx7_7XtKnmPE7Pjbgw16gK_-rwatgotuW0UsaaEDMsBssaCM8o23l5oItfL3zDIvmngiNN58E7esd1_sQVzMf-Bisyo8pgO4he0aA2BOEMRWOoWrGvhbmrvuv6eAp0fISKAAsH60-yhrDZvTEhN5eOvprNJoWM4oAI5it1LjlkumrMv_GbVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25369" target="_blank">📅 18:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25368">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDk0CvNNPMi5Yqq8CToa_D4YEAI0vO6TecWPpEL3i9-zpyvW-KStaTcfT2pn29wvxG09S15fonzFpAgua35x4vYeRB9H6na2nkYoLPJyqMLq16V8cQztCaZf1bDoKzVH2a8gEzAIoM3ApK0lhNA9kRTt0cJc1k9uOLTv1US4EKhJb5lvCpuBqIbco-Rs_5sQEvjfLk8wfGIIYQbUvPzN8OSgI9PV8Pw5wdweams-_82nBgwHrXHyYmkxdW5IxKSGJUmTy0W-_wDOle2gJuBGQLgxv1AYB4czpIMKjPKesgGdxpM4lAKhcDZtcy4NlVx6UkD7iQRu8h2v7ochI4OdsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توماس‌توخل‌به‌بازیکنان تیمش گفته در هر زمانی نیاز به رابطه داشتن‌میتونن با پارتنراشون برقرار کنند که جود بلینگهام بیشترین رابطه رو این مدت با دوس دخترش داشته که باعث شده بلینگهام غبراق‌تر وارد زمین بشه و برای این تیم در جام جهانی بدرخشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25368" target="_blank">📅 18:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25367">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UciHYaSEb5XUdhS7MvnuZAu9p-z1xwTz8mYf2HKc5VkiTIUG7W9whEZGfUqHI14eIYcoU6wYtCinQ3XKrR0cy-gPczIdeimCEIIh70RMl8VPxxZUAf8NI22AvOFS2jk77Sri3aXusIrjZbYZFTspw76K1MxdTbbkirQnphe-ozYmoPqL8093c0Yg9WeHC37ACa0askxaO8YnhqwFgIcXwR3DW46Tzs7pOSsPTv478odPs_bcYBRTqrUxyDkrgBmyaP__i0bAhG2HM3NHpwTK5VG9ZHod7UzFk53ylLU_T8o-QWKNdycCdh6JflblJaJQy1rjlQixzxlGCpqorqfQ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25367" target="_blank">📅 18:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25366">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1WYML-m-anAWZnOYeyNK9zxkltfAAN1uJ04jskoPkrPXmV_fE9BQe_jkKRGpbsR2p1o1-cN_CLajfcRmh7Bdly9MmgOU3FBisyF857Am_jT6g6LQOZg7XozG_OH5015PZMP8EPVeP7klpxHuIPY3Cy2q7hwJLw78Hfs-5vkWrgIEiWmsYH6BODzwtf1ki0b9D7apYGoiR6vlNAQxwwY0E13B3ZFwcx3Mo9ZepDMeHe9Vi_sjDTKRoEk0wHJjzBxgTqZ3TC1AsJ3bhpyU1yFLwLK1kI_PpoDM1v_tCBefcJfYlZSJmB2PJ7Lk0tALl-RNHfefNW-oyjJD9kaE6oWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
به احتمال فراوان جام باشگاه‌های جهان 2029 درکشور قطر و فصل زمستون برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25366" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25365">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLge25IDVKAFHVPuzGlvHneUXedFZDYmAv7CTrbUIN4O-95r1rjzUYq0JQ_noF5CZKEKo7oXKr6L85kFNP5H0D3MBl19YuAj402a2KbySXMPhEXfBIFUjisxev2pP7qH3i76XvLNQzODV1oP5-cAbmJETNbp2gL_jhcTpNtyJExif3-XwE47WkfTNuwWekEL-mqa0aBAIxccWN44OU0Rr6NUPzwhT81oBVYFHNXWuME3PUVSylOeJ_QvzQoFvFtwVm4cq0Zd9AfCEW5MD5SKnIIQnnvOR0bHD4-AKrR5-78Js7vYuzroPlNnvm0Ls1pbLSbeY8-kInrriSBQ23lziw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعدِ بازی، امباپه بازوبند کاپیتانی رو از مانیان گرفت، بازوبندی که خودش بعد از مصدومیتش به اون داده بود؛ الکی نیست بهش میگن دیکتاتور.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25365" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25364">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RiZq3u4yfJFqe_S7Pm5D4Z4MNk3moLCT7WsgvC9Pl8g_-MDvBtP3HCcqO7uvYe9xVcmw83vBZVXAqxUesae6wBwU29cJQLwL2LflUhr-U80KGkVDNMJoHD477P_eBos28vwpi-DDiLLjylTMc1rpSqPI6bhy5cCRf7Dwq6vd3sRkmhlQVMTyieZqSq0tRzk87gT3sMGv8OMWQzMcapQ4WPPRstwE3f6bc4s6KbKm2ESQXmvTOvkgthe-fok0m6qpz2ykd_5rfN0ZVnTJwYvLJZyMXR7aNFoy81Eh7pdL-i6LkOZRDg4S0YA0TtP1GiUR_7Guf9jWv0tCj5TOgRYDUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
دیدار فوق‌حساااس
اسپانیا
و
بلژیک
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
▶️
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای، مطمئن و درکلاس جهانی پیشبینی کنید!
برای ورود به‌سایت‌فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25364" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25363">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lj1Ts68BTTjjyRqwlAa6dLs4nLtMELUM78vKENcfcU5_q1ubIePTGELmJL9iP0MEAtqhYcHHg41xdS9Dr1p67ba0Baj-wZQ3IBFI_DUszQ75dqBdFgaB4ayH5ltEz0tvDHrzdMJ1G0ydFh1HvDAk_ty171ZA4HjAm0ypyV9TyKIMXyx41jxEsHw6WPguoL30xChaxmKNdqvyZHhO5lEzCs_1pRu8Frlug_SzjgcL7fBpB1pgGJz-1UxB_P9CpqchhSE5tM1xDxhEH0dmRtrtADL85MbgZDKhTH43uJQrgTlqMB9IFfgBFA1H12b8PGQIm7xhk7w-KRsNttr8zaqR4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#تکمیلی؛ فرداشب‌فرصت دوهفته‌ای باشگاه استقلال به‌محمد محبی به‌اتمام‌میرسه و این بازیکن درهفته پیش رو تصمیم‌نهایی خود را خواهد گرفت. تابه‌این‌لحظه آفر رسمی از باشگاه های خارجی برای ستاره تیم ملی در جام جهانی ارسال نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25363" target="_blank">📅 17:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25362">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3adp-9xE8Eo-br6chlQ_917-Ao9dKG8Y3Hinz4AcZuSjU6Y22WLUUIWh6jPBV2ppAxW_tARKbd4ZbZH4yWjiUfGRC09jPkAuFjx0GxmoOsCvI9Clz8S1s_mGpB7nRrJkHOFNLAEBEshV6y6IDGo8tcfyvQ08nuA_ubyuDNQoqcYRfzrhWp-_F3Z0TbfeeFmJ17Eltu13MLoiqhwrMw_Bvr78EwQUG9djyl_kbx_PA0odZG-Ukz8TXwYWhuP10b25dOx4JMR_IJ3lp4wa3ev5vzFxkdoLgyaSRm7KAxA0LGprNkbTPXg2jfZQK6a6n0EhUFdYJo2caI77PwH09Kn8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇮🇷
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال امروزصبح باردیگرپیگیر جذب محمد محبی شده که این بازیکن ملی‌پوش از طریق مدیربرنامه‌اش به مدیریت‌آبی‌پوشان گفته‌بزودی‌برای‌انجام مذاکرات نهایی به‌ساختمان‌باشگاه خواهد رفت. محبی گفته اگه تا20 تیر آفری دریافت نکنه…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25362" target="_blank">📅 16:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25360">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCp9FLzQirYjTpsn_1SiEV0YMYIr3eE26TDQ4kx5i0feYNAHCsh29DIbzJk_zC2sQ40SOxYu27gT4oWGw7URM-tpLb1KVk522AwGPgVy6OBkWD-smcnJuDR5RU-kkww-U3_18TTNHQCFWvbN24nJeXW8Q8935i8mzxBj5J8LEJIvPSVNeR3wqnIixt6HmvNOKjy9gyQwLGErIEp7HvQuga1VYZLi9tPioNiFP27xzI1lTB2HGFDN73ZbM5PeAfR1XuwSTw0bE1CIi99w4ejnlSRNCIHfFPvLvDI2If5jT4iHQ8fh24rhvL5UPuy8ck5mJhEuF1qIusltAuC9zbsmig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
مدیریت تیم استقلال بعد از این ایمیل وکیل ایتالیایی که امروز به‌باشگاه داد مذاکرات رسمی خود را با گزینه‌های مدنظر شروع کرده و با مسعود محبی مدافع میانی 21 ساله خیبر خرم‌اباد نیز وارد مذاکره شده تادرصورت توافق نهایی با او قرارداد امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25360" target="_blank">📅 16:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25359">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jo1WK3ZLQkAdXwq_0KxE7udu-pAU_ozQXLc61ivXdDlSNEjlgUaRr4m2IfsPFPCp-ZChPndMVR41qYIctpLB8JT50GYZGVCMblOTSH7ZbEuFissQwy1dNUI-KtoQu7DbQhXxOsFWBkoCrwomGeyDUfpBcjWCyA_OUPF0e1BG8HUB53aHH39oMRtQNhvFcYrKsSYflN7n4yf3pY1c0PgbyGjmacwizDzz_jq-oi6v2-JHkxr7n9mA_EaIQy4WEWTzsvJBTP15kippaCbR_AbtJd4IfnlK3XJYtCLHh94OeBelrJRL8h8HY74Fs13J8tBTAHMOFKVsn8LUUjWcCNpNpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی که در یک دوره جام جهانی +8 گل به ثمررسانده‌اند؛ امباپه و مسی به لیست اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25359" target="_blank">📅 16:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25358">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇵🇹
10سال‌پیش‌درچنین‌روزی
؛پرتغال‌باشکست دادن فرانسه میزبان تو بازی که رونالدو مصدوم و تعویض شد موفق شدن به اولین جام تاریخ خودش برسه.
🇵🇹
رونالدو درباره‌اون‌بازی‌تاریخی:اون‌روز با اختلاف بهترین روز زندگی من بود هیچ جام یا افتخاری برای من به اندازه یورو بردن با پرتغال ارزش نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25358" target="_blank">📅 15:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25357">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPQ7CemUHIysqOlBa6s91v2gCuT6nehkvkt1nQxKa0WpSrbfPieEjZBHE3WdXS9nQquRq0AcNwXFxaDueiTUng0M7NZdm6bFyjCJH-5MsyZdJ-4T8_a4b1zsxskDx_OoAzk-8wNXxN-zcneSlAJ7W3sjk3zw9id6Q7xyi0BaqlA-gIkkmFAzPyQLvOAHFkucHipF8hJ9HBwoP-iD6p78clhkSaY3yeGsfd4aY5iUbyglM32SjACeyo1xDu7a0yizHeyw3_XG61j1ju6g5QmuXPm21Gev_vYedByGFMpfi8d_BoMS7AEWlhASZC6h0zbenO05Sc0_r-dPhAF30kwdZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25357" target="_blank">📅 15:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25356">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=bMErL3Ul2KrD5O5DkfEeR1jQsUC3xBsrTzIKODDif-yA4etHVl15gypqc_CURZDNJcpf9Nm6inLrDzUFOhEojZltqngwkucr2p8oAMoxE7hj7JXu3XTrPV_KnmqAwT7Tq3LTBKYpLBaxK_i6YiB7qKS9Lyk10wBAcDjl4F_1s88opytBRJO1agQ3RZpYZAfYy9jyIPhE97V9Ih4r97eGEs69wqVjNrBiwAV61Uo7X0KLemIgOEAN3GPAbZK9X9Wb_7Ny_0NdzNqfABgkkuIqwJnFQAsEIpUuOgQJ9lqK4zHy7rv75gB0qRIF8wbVPqR3xVwNYriA-wNqlRWP1kP6Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=bMErL3Ul2KrD5O5DkfEeR1jQsUC3xBsrTzIKODDif-yA4etHVl15gypqc_CURZDNJcpf9Nm6inLrDzUFOhEojZltqngwkucr2p8oAMoxE7hj7JXu3XTrPV_KnmqAwT7Tq3LTBKYpLBaxK_i6YiB7qKS9Lyk10wBAcDjl4F_1s88opytBRJO1agQ3RZpYZAfYy9jyIPhE97V9Ih4r97eGEs69wqVjNrBiwAV61Uo7X0KLemIgOEAN3GPAbZK9X9Wb_7Ny_0NdzNqfABgkkuIqwJnFQAsEIpUuOgQJ9lqK4zHy7rv75gB0qRIF8wbVPqR3xVwNYriA-wNqlRWP1kP6Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
ویدیویی‌ازکریس‌رونالدو
🆚
لیونل‌مسی که به پر بازدیدترین ویدیو چندروزاخیر دراینستا تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25356" target="_blank">📅 15:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25355">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=ra4Y0yqtS7GEsXs1fUL4dNp3k86JHwwNlSHRCyet9r-vXA0SFeT3mEnRIor98uLqSf24YQsj6VHmeUqGRynZJKGOim5efZvpRj0Uh3FSnCWFN4Zaj5P_MrQkzcr0WETaA33fGm6kWT-Fy6Lzk1WWYIcc7O-i3juDxTW5cwTbDJ_lo2n0-Anm3aJPjx7a8rvf_x4fs__3IzKESWzNTTsEYmbqxynXB2qnf3jCihwXRJoNYPpKnYH6GIM15c7gqLrRA8lCzYKCFUj8QMHbzQxXE41d-vB1zHkD4nnxvJHwhiIfzHOgmYzTchXpBgf5mS0znB6jFW_Myc2fnLsEoqTkpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=ra4Y0yqtS7GEsXs1fUL4dNp3k86JHwwNlSHRCyet9r-vXA0SFeT3mEnRIor98uLqSf24YQsj6VHmeUqGRynZJKGOim5efZvpRj0Uh3FSnCWFN4Zaj5P_MrQkzcr0WETaA33fGm6kWT-Fy6Lzk1WWYIcc7O-i3juDxTW5cwTbDJ_lo2n0-Anm3aJPjx7a8rvf_x4fs__3IzKESWzNTTsEYmbqxynXB2qnf3jCihwXRJoNYPpKnYH6GIM15c7gqLrRA8lCzYKCFUj8QMHbzQxXE41d-vB1zHkD4nnxvJHwhiIfzHOgmYzTchXpBgf5mS0znB6jFW_Myc2fnLsEoqTkpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25355" target="_blank">📅 14:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25354">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8-i1d5YpeF88D_d7bcrWVu1brubiepSDn-msANik5N0B4brEuUbbYpE1NQpQgk-Ju-6dYgSSLExeq_f7ngLC3VKVpGnP35G23HkvbUUMtk7VcgbaER76oBD01NX9E6NMBorgguPCmY7N6n1FibTmBamjJhdooWO1MpxbYhSAjxmBAM1eT5D59yxKJQp2gv27V0Kq9L-JH56Vb60rA14kyIsN6YFlx389wAUux2Iev8t1M59WsieArnZVGxi6MsmMcjgAs9dE6ylYnfN1BSUioVc_LCx-nCNTT45hH-As-y8OfcaHnCLjbwqef-8g9MwUZf9iexBXR9nLKLvHx5TPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
ابوالفضل‌جلالی‌مدافع‌سابق استقلال با عقد قرار دادی دو ساله رسما به باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25354" target="_blank">📅 14:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25353">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlDmD7rWKLtYR0YRTJjD0t1bEpV34TfQDIq1iZ4bZlqFiz4Z08qe0VDXhHsgwJLPSDEk121DPdl_hSZPJniMMaEa3wduQhYrnQOJUQ2Fb5W7IU6hY7T_UdgcAS8jN4Iz2lYA-MyKCtaEYJUlJU5YQHtt6LoyReOfdWfONGH9PML-fRAbmyqMtmPpKFOj4JVxcEMZ2a9KzwZ8JRICI22fv_zSW1FgyIaMMYBkiEIsLtrQGB8zlFGo7ox88BpjIElPy2eYZqU2M4j9-fq1m7RqiGlw8IHrvAQ0MC5jNagcW5dNHHpljEGc3IdLMXt_T9RVkQV764jBZZMyPTs2_MC90A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25353" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25352">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGnG1NsyRe-dDfLuSXDchpSqMaurdc-EOtntV-gXmbEkSB6xr0IlR_wadJdhmQ7msb1xdKp8AHu6kjKLcGrOnhtqTmmU-n2lkc8TReEqOCSKgsEggae4B4Cpg1wQAJzwc1Bcc_UI1HP5IEEM1k2kw184QRSrUlGKlmqkMyzRte9tDABKU3DSpg8bTQKAF_ssHTvqw28vmbAecglwyGhbpuPYGGbQsvLdi-5EcDGMwo1UG2sxsMu_WpzCkb6TdrQF40mnqwZUwwaLS3_quhjl3cKBoLegi49K--BM1lFqpFd07K64IkS6p4NrZPgUxl0AiFDf8uifPhCVbg8Bljfa2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
نماینده اوستون اورونوف به مدیریت باشگاه پرسپولیس اعلام کرده یا رقم قرارداد این بازیکن رو برای‌فصل‌جدید افزایش بدهید یا با فروش اورونوف موافقت کنید. مهدی تارتار هم در این باره به پیمان حدادی گفته اگه با ترابی ببندید مشکلی با فروش اوستون اورونوف ازبکستانی…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25352" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25351">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrEQQ7MFdYAHIrVQAkruhqwEx2Tsu9UdpaegWLjBOdaJIFeLcIqGlmiJjZFyNqNsNUibN_vU3OG4kiYawRCS-gNcCBAj6xsySORC05dtOJ_Q-HM4jKxRPESK3umyVMalK24hdgC9UBfN1gS4Ju7fs5GS2D7xO9VGoADhgpQynSEP4lxsyDE5MY7V8Px8WgexUVVaRJqWcRED2kDD08f4ek55VGB-bEl07H1swrAF0bRImrw4LJHdfVJdZOQnM54WDjYFZ36z5bFcUeZVzI0sXcyEIKE8l3oJb52pt2q99t5A-c-QJE37u5ES5cT998OYqoS0BnhKA3qRwzYK8N_ufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25351" target="_blank">📅 14:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25350">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaQyZG4w0b5KCVqToD-d2UmrEEhKdGzvngCcpkKgUO2HcinXQ5yJ5OLvRPkjAR_bNjqU27NgIWmLapnEdjq3P1-oJqyygrY81snN0CHimvZrJCMvJ2DMQcFsY1idnMYDB_Si3qWuBsm8JH7KxwDS7KoT0I7WLKSZZGyxXGmneWRgOacIQgzHfO4UCwH5ebSeaQuhwrtvLwye_teK3Vtbtg9xSG84q2wLu0q96EBp6lbjys_bAMgwvGkJbWuWsjW9-656G3SAzlsbOQpK1glF_GZ2RqJuPwU7Y4cVhjrYvaj5DqYbRsHn6-usJvpRPs5vYd0e-Jf7VBKSEA3NrSpKyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25350" target="_blank">📅 13:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25349">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2vtYYV1JSNRzJEEct0uCo0RhNxYvmNoPYopcYEjKOKEq_W6PpRz04wyS08pwn1pHDrtiWWfP-K5boqhYqYDNf06yiMu6iuYLGcVX11JMRFU6EzGRIgeJkksjnX6Dac-FPB3_ZkSZyxqKd_fttRo_kgwiruOqCP0G2oBFqYJzsjH3jHpwSyvf8VBHAWFhaoG8L_u3az6r2jgzMI82DjypwlHypIEaxKwbXuk5PnMabolfjmZQLWaiK4KOuuB4HDN9tYg1Su_lvMzaqNoCRMyyn1dgGQxLeGxKUG3ozgpQJZx4gNbadzMYHmH5oguE8HoRF4OVmbHsYsFdynztml0Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25349" target="_blank">📅 13:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25348">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCUaKxoQ-ThcwyfsXRmUQhrxCg_nNEOYKCXz_T2bdtAEBppXrYLfDhT_8M2_klZFcKDkrbjKoA7K1OpLosa4zp-QAtr4gNDDpKDb5__AZJKYq6kT7fUyZKyYpn2DF9ItqCFxstD4B7nFIDaIid_o5mCR57tjJpjZ3X9COJjaqvANFsmt_j-Q5KU0z_PpHN3_8K7UATs3y2e2AvsJ88bu3ZMUy67EmbL3X37K2sloW4ntP581Z8ZWzCl8PQ7asRGuVQZEdEIi7K4S4Pw4NHLlV8G4F53Wm6v1gPVqEW8fA3qQD9ZyjwHMxpvEQ6dC_1rhw8y4KjxzCyVpDzJsj8ipvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25348" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25347">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnLmJDam3j06fMmeDcePxbTIpARQN9pbbxagju90rExAgzeEfRIks9VFWmkMWXB7SPbhzasMisLCW7WEOM9OMG7s3cRGaeXqRDhCH2OPuqcI4mzfCO37xa-QLLG6HbJ6nEPANEh4iaDdmD4KQrou_MZwE7cPN8b3sFtQaWhvUWdGwLoUQyRCN5cLMCwkkDG4l8BJGfvCOAIzxnL301uqOwxb0INBv85P4z1jv3D78M59rc0fR418BKNrp7O3KVtvYEhb0qm7OWzdiyJ56JzKPrQB4da1wSaD2e58sLUGfQBsxyi9t7NjLNLZj2oWeUy3-VLaROD83brzUjTeq4bnQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره استقلال ازباشگاه الشارجه امارات که سرمربی‌آن‌مورایس‌است پیشنهاد دریافت کرده اما به مدیریت باشگاه استقلال اعلام کرده درصورتیکه کادر فنی آبی‌پوشان به‌سبک‌بازی او اعتقاد داشته باشند به قراردادش با آبی‌ها…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25347" target="_blank">📅 12:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25346">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">📱
اینستاگرام دراقدامی‌عجیب، قابلیتی اضافه کرده که با آن بقیه می‌توانند از عکس‌های شما برای ساخت تصاویر هوش مصنوعی استفاده کنند! اگر اکانت شما پابلیکه این قابلیت هم به‌صورت پیش‌فرض فعاله؛ به این‌صورت آن را خاموش کنید که مشکلی پیش نیاد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25346" target="_blank">📅 12:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25345">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2h28qo5M8HvXWHek2zXPJDQk3p9b65NHrnrGzVIpDBHNk5cRYQQAfOLWDPnpB8uUrK9LUAhxeFYXIJKN1YPmdbC7CZo_V0YnJSyk94oHjqKn6DXdbQHHSVQhjz0Gv42jHFIngEyc3wtCmW8tTrcZtkUVsHe1nUPWLfgc9Re6oNyRCBT-MUvmPzPjzKxf1Nvmwk21ch67VYlYLZBuxNaRhU2tN1lc58a69LP9zGO5PNz9CUvUJouJCKHYgX3Buqf-pFfwGfooiuOWXDRvSHS2n8e-aJbSzeBF5-oR3yZJSqZzIqDswTd4Y7e6gtOJ_ezGFXd3JquZ00njUgnIjgkPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25345" target="_blank">📅 12:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25344">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bG0EdagVYoP29EeTsy_di6TIzAR7lf5xByPPsQ2NrSrF8MlWZe3mHmYy366QDHFrjw4drvXPmLTs45ZbLN1PDZsIYoczxy4CXcowCpZV_vKuVKZ-H4xKASwkalE_kaXHnEYyu8_RBkmthfryNHiuO1UifsFSMCD5iHwWptsoGLkqhYisEcWKAN00o2QSczSab5Q5UiSI1VllJIyIMLKdZuWbwqB-jiln0-TEj4DWGaZRU0-oEX9fckNy8w-DjiGyWhbWxDejgi13NHlYTtcE8LAyIonq90cmtrMxTB5p0TBYlXOFg-u6Ox58OOfQfj2AmCE-1ulWtB8XmvnTezba7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25344" target="_blank">📅 12:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25343">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c669eea570.mp4?token=ObdzqMQNfXX6ynu_M-hQwCPuOHaowRz7sF6n2cPTdWoKqbvoJpLD92pSCPxLtB-dmAdO1sPnfV5ZylB4H2sNdQFEz6C0rubIrQRyG_d4vPnAKCYjtkOKsINirFK8WVfg-TABURT_7CTSUt2QLDC5UAGwHwbyZVS6Bh11LXd8cLKcCoRVaHnrQupuI0b5IKOSg9si04OB5O_eFBpIkmXBcSv6RRIfk6pHGBJY-VOLfJ94DVO8T-GLHXCm9UvELLRlRZLllKatxYI86cOdTtWZFV9HzY-Mo4acAwDsjhSVk6WZChdkz_8NK6NMcoa86mIpwEGD7BbPUPkALdMvgdeoLIqmgiRviq9DzIrjR6k79k4CqnfbU01j71OLRkxgEoLVWRaygpLfNKgqciClhOaeo0Z8ad5k1hSsKQ9SsYIrYiAhGY-3A1JMO6yzSxciZKxiQMEMwNX_b3O-ewpsJq6aqvPt3mRsHHKOWAFQqZWsHt01xyzSDQrDXFchQfTEQKvP_nOEoDLhyHS5twcyp6yxMkom7C5g66pYI14FI_46s-snsI2vkOPwHAOWQVUf8u8Ms9yrA7vEDUON2cnzCoyjwV-48TYIyJU1RSa9NtsRQVpKCT3cknbMSMK9lhTLJ56maZ2q0aAMI7uNaLRc44LVGLP2M6aCMiJnY_ZK7j25Ngs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c669eea570.mp4?token=ObdzqMQNfXX6ynu_M-hQwCPuOHaowRz7sF6n2cPTdWoKqbvoJpLD92pSCPxLtB-dmAdO1sPnfV5ZylB4H2sNdQFEz6C0rubIrQRyG_d4vPnAKCYjtkOKsINirFK8WVfg-TABURT_7CTSUt2QLDC5UAGwHwbyZVS6Bh11LXd8cLKcCoRVaHnrQupuI0b5IKOSg9si04OB5O_eFBpIkmXBcSv6RRIfk6pHGBJY-VOLfJ94DVO8T-GLHXCm9UvELLRlRZLllKatxYI86cOdTtWZFV9HzY-Mo4acAwDsjhSVk6WZChdkz_8NK6NMcoa86mIpwEGD7BbPUPkALdMvgdeoLIqmgiRviq9DzIrjR6k79k4CqnfbU01j71OLRkxgEoLVWRaygpLfNKgqciClhOaeo0Z8ad5k1hSsKQ9SsYIrYiAhGY-3A1JMO6yzSxciZKxiQMEMwNX_b3O-ewpsJq6aqvPt3mRsHHKOWAFQqZWsHt01xyzSDQrDXFchQfTEQKvP_nOEoDLhyHS5twcyp6yxMkom7C5g66pYI14FI_46s-snsI2vkOPwHAOWQVUf8u8Ms9yrA7vEDUON2cnzCoyjwV-48TYIyJU1RSa9NtsRQVpKCT3cknbMSMK9lhTLJ56maZ2q0aAMI7uNaLRc44LVGLP2M6aCMiJnY_ZK7j25Ngs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوهی‌های‌بامزه هاشم‌بیگ‌زاده با حسین ماهینی دو مدافع‌چپ و راست سابق استقلال و پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25343" target="_blank">📅 11:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25342">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ek10WvszrH1dbgsOYMXB3X2I2hUWlnueIqYZ387SkuDBkiQQyU_xAnuvEBM8joUgd3ZTSSVe4VxowAuMedW6H1vuw9qejA3oIMlzXBdcjAnQ6jw6vwfP8hosTY1sTLSGE1BIiv1FES-qD4n5SrwpuceLO1togHgjTAddJT68h3pdN4XRJe1Kyk1VqmrQzXYWQSOeUuciSlcrS8Tbn3JR0O7ky1rGgXWxc2K9rry1QEmXjGF04Gl6O56fO4uzNuFABAgkiNif0AoPPTFaOh7nC5Tc7uMRHumepR9AzTyH57blWUsgswKTxJwcySZs7z9FBAPn-k1SzvW60daUQfnWvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25342" target="_blank">📅 10:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25340">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saPF6TzayQ9YKUDe0f8G0zs565J6W0GAI9FCvtBNX4cbYpxGSvFBmlZ8LoKubxdwnII2qbq1lrn68pKrKSTC7A2jF8nQQHhz31P3RRva3l5lgaVUg8HqmM9z0jAZt2iUZWicWQcttZzfhvajzPZkKMRLHdvnLTtTZTqa7wCyWrupSp9siA3VlpuN-0c9k8Fnn12Zxs0fZt9K5ZZUjHkAaLqs2oP4enCvVuZBymLwlKRZcXrQWGUshMe3ejGqu9aa9cD_APku2qJSpHcOYvF0GAb8eiJzTWOmGG0pT7MOGVbb386yTOGobClFRv7w2YUGjQhKwH6ZABC14fGp-KFRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی جدید پرسپولیس بعداز منصرف کردن پوریا شهرآبادی برای‌رفتن‌به استقلال؛ ساعتی قبل با دانیال ایری مدافع 22 ساله تیم نساجی تلفنی صحبت کرده و از او خواسته بافشار به‌مدیران نساجی کمک کنه تا رضایت نامه اش رو صادر کنند…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25340" target="_blank">📅 10:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25339">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZreysyOM9dkmw7m2S74vI94hU21xVqS4U8OCobT06bNO6s1xJp34m68T8TQ4NWrMf1fldu5P7EYb5uQpGkgdw9Gi1bHtIDBmRsLG0RE899DSrofnqIU_mhVo8G39qchPgazXciifzMzL021DD5wHL23BVYzB1mvTx9XsfGTRfiTR46fEOUIhlzpfGiEZD6VqAUKGO_7xK-AYvDfpSUiVmspiEE8I8ZRHagaPu-vtDRu3m4pAU3X55s2NULwarm6ka8ogBwC6YDojVLIbOQBh0wuTj2-v8WldNOQK_COX-uVtgf7a97FBS1zTHptk2zKJ6DmKtoRZgyCXUKVHLVTLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«وزینا»همبازی مسی میشود؟ براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25339" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25338">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45277758ee.mp4?token=jyvzqusGqtnVn_uiQqozPonO00_5tqmnZV4fxEvjv1P-RWOSDBpBiBEAFf1eE_XiIw_mhU-Vr9jTI1rsIpuLaDI0LCqY_RauALOGUZd27FbT0bstjyw_7tfTxXFx60aipBP2XhHyi3LZyZ7oA4Z8u5T6407JgohRNNLim-SU92MROhLA4Pqty_tcg03RLAknAb2-gEesvP4FOC6ZqHGcRQljd4DFQe5FUela4-zOmOqaDmb1j1oUjXvVSLDmApEedDQsjPpU9Q8f2K49S3IhZaFu4LUk8Ho0eA0oztfTYjhyC7iG5u5TLWxVqxfg1DQYs-aBtP3uYP7T0wB0FkQCIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45277758ee.mp4?token=jyvzqusGqtnVn_uiQqozPonO00_5tqmnZV4fxEvjv1P-RWOSDBpBiBEAFf1eE_XiIw_mhU-Vr9jTI1rsIpuLaDI0LCqY_RauALOGUZd27FbT0bstjyw_7tfTxXFx60aipBP2XhHyi3LZyZ7oA4Z8u5T6407JgohRNNLim-SU92MROhLA4Pqty_tcg03RLAknAb2-gEesvP4FOC6ZqHGcRQljd4DFQe5FUela4-zOmOqaDmb1j1oUjXvVSLDmApEedDQsjPpU9Q8f2K49S3IhZaFu4LUk8Ho0eA0oztfTYjhyC7iG5u5TLWxVqxfg1DQYs-aBtP3uYP7T0wB0FkQCIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه نویی بعد از دیدار برابر مصر: خدا سر ناسازگاری با ما داره. شایدم خدا داره من رو می‌کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25338" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25337">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ty3H8-K8dngIsixXl6nzUHN1H2KyQRw1s8JkHRl7ypA5jXYx7S5SpWpxx0GCKaD2tQylHD_Bi2t9_xuLzF_TF2ek56ItQ4ElEkRqd0EbCXtL3jDyAOr1jhSRKKjWzfI3klJ_zKyYZB5yNs8Tddu4cCiOa-79oX5fRnUAfg3p4HmZ1xiHbU62u9l5G-D2dqOxt8RRyXWA5TJAoj0esal61z5XXZxVICvgVaJr0G_menjyAMAMRbXP2341EAiePOsxgzpi6BVw96OxxUn-Hmd1Q18US6USwaiLxTyQRZVR8NMndE0k6PTM5GWfDb9ckN1lrV3v5HdTUpekbWmQrr7s6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی
⚽️
⚽️
اسپانیا
🇪🇸
✖️
🇧🇪
بلژیک
⏰
امشب ساعت 22:30
🚨
ورزشگاه سو فای
💰
در صورت پیش بینی اشتباه مسابقات جام جهانی ،
5️⃣
میلیون ریال فری بت دریافت کنید
🔥
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
🔊
همین الان وارد شو و فرصت را از دست نده!
📩
Winro.io
معتبرترین سایت ایران
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr19
📩
@winro_io</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25337" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25336">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohXDDgKZMPdVIe9a59_DG0JX9jkN6Neh4_KWecED2AOmtATO83fAecX5pRR1e56d8tSOrdf_Gp0RrGUhnHV0HYDx9fIGwMANrdKnqXaNEeyhV8T_00ddyvwnL9LL43BJSBp44vs6MIJJttkytYHB7D49YDmlpC587ejCc4dj3LcftW_Lytza6cqPD6D13yC9W4Du9kCTepbHMuqJGeqFjoje6rAfo0bY5BZ57QIktB0W29IcaI2TWo-S1j6g0YLjQWJu4QmCISXngiintzDc4A3xPksfFPLGlNxkqQZuIWVPZ0lzR_TbyiaV-dyiRlvgyypsoJ9YZ9uY72TZM3sEKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دوستان میگن امکان داره مشکل سربازی مهدی ترابی برطرف شود؟ باتوجه به عقاید او و همسویی‌اش‌بااین‌نظام بله یه تبصره‌ای همچون تمدید معافیت تحصیلی پیدا میشه و خدمت سربازی او تا یه مدتی به تعویق خواهد افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25336" target="_blank">📅 10:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25335">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4G6YtaS2UdAIs3xe2NCjqRYgkp9tOV5oJepOhDUHf__b1XU1l7bhEK-86oXWQRHOLxH_eGOkRrI5UdwU8nLm9PH2Z8m9fK775JLfe5angVCVGfTzG6FIyTQyU0LSlZZqVWBWVz0Uc4Ncsxtd0P4O6dchp7hzqodgxJW2hBSCVK2NUBpMl0c2d7pzyfm4NuuN-IYAjNusvxBhS2EVbLCNMu0HBpQ8TSGGcPX2lbdXI0tmiPPKt8P3D2ZWEvlrVl2I5v50oqwRZM9FU56MWQnjy4NewxNZOMZDSjEV_BzXixfwtD4HGdFburJhAIYIfqKYqceevKVWpO3fcwgqeOrFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
ابوالفضل بابایی و سروش رفیعی دو بازیکن دیگری هستند که بااعلام‌رسمی مدیربرنامه‌هاشون در ترانسفر مارکت از جمع سرخپوشان جدا شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25335" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25334">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEMpHAXIAw8EN0Dy0W6PzfSF4GARgYHyQU37PCqnbn9HL7QZShOlSh7yRJVTCVsXVMyZzqMmhIDdOEY0_OaIIKO1kkxnJ_wl1M2m_QEIrNpy5zVDyHLWF8rHFImUBveHQFRxV0Dg8-aO-pGcdX-ZuLFseaKmIhAl3sw9OLFBZB0lJpQn51BxYW1y56vr9CPDx2SYYNc2VzAdSDFs3QC6MywjNLKc3dPulSkRjQa4IbHq2stwPhOQ-Dkl6N4EaR_lqD2phgga7T6CW7E_8Pecnj2FoQesCP-Q49Pvq6qnHcGFE_dXtWeshO2IhWUTrDRBFKS1320rGQLgZUBkHi1d2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25334" target="_blank">📅 08:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25333">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLrvsYQpTNloi7OS96TgYgrh1JqgWH4PGZrTj80B4GVdkLCUKJ3BqYNBFFx6DQ6Dqvum14LIJyESvbK2_hZD4G9H34QsFlwHX8baavLc0d9zd3ZAM5kul8iCVOwv1mFFd6C8w2fdQarLmHOFhujeHxNAAA08mv8U8GWv4U_VbwETsiIHYl_wDpbPXGqJx_4Q_EoJP67a9skHJkeXpEb4tI9XuYIBYN9RNBicpTsuiBVqmW0wr2_PuhBG17zUnr8p4_0x7F9St5-jC5DpGqlQAYAqvzIedlpHBlUL_VJyaf7jXDToHUMww_XcdjGBxU-m6i3x9vdPvnKs6ipSCj5Zkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25333" target="_blank">📅 08:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25331">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m-vhRM3Sck2i_dMVL6qDk6yEgNZCEVseter0535Yy-53SQ5StpJJJtihljFkyxbzy0MRMu7-AQcfuQGu7uLTSwO8rtcjsJQU8rOz9VQtbCASGVflZVSVgQ7Ku9GDliWU12GyK_6e7aZk5bFvKqWI8nCXglfZ4l6dwlAJ_tFEFQR77DUgDUxtnOY-bFIee2Ve2dvQXdht5IVpqFNiQPh_P52epLYjPogV3bQuA6hGJDr-MOU_ZmsLd-0e1QTmsPr7KJlOg_MbLDZKuN7PJZwK9ZcGYOm4Da9VuMBM4DcupMDJ_qwBEPSQCXOqP3eyrJ-4vtEg4ST4XAFtVPEi4AcTJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dTesUDS9C7bwkITYdZUsAJiiSPteAkCFUS55Vch_SfaaVz8z1ldCFKY5tPePkSBdPT9j2pW2k53uqlK4ubTHwxhgYmAwylhiHI5NE7B3AmE4L9Es8RGp-EfQQ9jEZ74O1gG8EuRBaS9-NRfv2z6jzWqrtKqClsb0ttJJNmzgjTMCMFxadDD0J_L_2B1kQmseEDYW_ldaKbQueKt8MWSVHGiUMaLwil9VAOphuQ3jipPonUs05TEeLwcfyR7OO7NyuoeVgzeE9GrQrMLx0EIlcr0ZzRL6yww4g7akqwdWlXxGwReweAaRNw3MTf3osZZNWo1HKys0nol6irPNRsrqBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم؛ 10 سال پیش درچنین شبی؛ تیم ملی پرتغال با کاپیتانی کریس رونالدو به اولین قهرمانی خود در رقابت‌های یورو 2016 شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25331" target="_blank">📅 02:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25329">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AIfbIZfysYrobFiLcLNjWicT6jFVuREibGM0el6xhOsgcEyUqQzkswRYeUmB084j_8BlNWWRx2aNNhVZ5m-a1IEYuHWGkiaAf0-ycFSuF4Kh_ySI4ekZPe6k22qjUsFjdDgUVOo7Q7feHZy7Gm8wiuPgzonSIhLifjuIoW2-G4diPQaij8a7n7QIfTDlPzgfluN4-OsWSHB0xlhKSLc9zO7tKxiBASupGEKOApao6I8ZypMb3_5Ju6XxQyX6GwyA-emJHoPK6w4XW6-LF4l7XBo3JBRSbhsfFyAuIwHW58SdKYK62dBUUot9Th5NI8l5OYEKZjwqhIhn_3kf6DQRUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ors1kTDb6fhNf_AJwWhwQeAE4NMPrcd2HG64dnaZph9kYIy6kkgTYkAdEwNMZD_M79fcAmzvB_H0LhBGBXa-y0ZywwEWY05B8mBjQ1p7eiM9qv0acTHssB47QN0fsd4IjwjgqEwBVUmhhJbAPLOhg7OW9-Pbmm_lrPedwBBsOBMY554QTH33kL6KGT3Gn2sldTt_Py-XeHnd6WDthAIwm12rVJiLC2tz56AqM62VFuO3ICje8qkHHdfFoI8OdTfe3DquUYAVrOJwCC3txNVNa_6sfo1kt-jVj2ttChFO8QpOo2ajzD8kw-5JgVaKHNshiBqVDhx8h68rOHwmm3K3Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی‌زیباوالبته تلخ در وصف کریستیانو رونالدو کاپیتان پرتغال بعد از حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25329" target="_blank">📅 02:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25328">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_poaITwYcYuttne0ExJCneXpjMh4YnlJb0AUOe2Y-oKcW_6sPU10wqveysekEc8BGGb7Ba9kXTf95mPyuC8JUFMLFUy4gigOjOLETxcbvKYnNaalvwV4fXfcnptCB1k9rdy3CJXw9vdFoYxhpyPDnrGG__vNFkzyBtsJZuuirG9oc8iS3EafricpbHuk-CcxvwgCf_TUrtgu-3SO10_B5tY2wk-dBoXfIvT8V1rXrMoeoouK_7aWzrGGmTO6bmx8Ht8COznX7EiePTxaP9ud6erY_4kr2C-ehkLi20Ci_TqjF6ZuRU8o8A_gQxkLAfXKMhi8iyaU9Yvif-L4LOZLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25328" target="_blank">📅 02:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25327">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDq37YOXhTo2TNl0WqfJzITvCYQF-sI_cYgk7pOS06XmOMqkzdHOq-KncoxP-YEXDj9UFLglkuJM9smjHkCKDKFzbz3t6kvTleZoPABNZOso6r9qh8m7nimFqZYHNYVHEne08lxVdEWMwU6W73LfzF1tHCGibJfJAviutD1vaRP8k4dNaHLJiMCdqLqBcLBtmnLoNrITEcOIWhwnhZkJvfDX_sIAj5IvkONZS7Jq8MlEaEWQuj0qzubpUauSy0taCNLRxXVTwk6ObeY4t2zcDbkZaSpwa-ciMvyv7Yxhu8HBRCJ87HlSGe1z9RgJrBDpcTan-nwzs6HSiTtz79RksA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25327" target="_blank">📅 02:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25326">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X320ohKfugexIbWQ5VtCAgLCpfzvJnfpdaJl_1jsPELqUB24IM65GQg5bB55LhqlMgVd8GarFbVVAbJFZueHj6dEva6ew6Pdx-MyvQiEBVJxUMJBpgK7zTwwrTz6G2CHIyRAk_mZTSUmtkeWTBr-i0fvVVPh3N6lCuUbGRI5CYDt2pVQdnxS43mGyK3jUb4yIPlRRdlNlvJf6HmmsvOuncAPW0af6IxoEHBOarZNNYZ8GmaivlcNORWJJ4Y02VKAzGKOwVOAspVRHEKGbhNqdoF88Yx4aJicO3TzoFXSBavpaFsKrIvyEtp0RophyMTNICJLpu0CiXJ6bnQURwuyLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25326" target="_blank">📅 02:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25324">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BHWaB9-QdpnyGgCbOn4C2XdhE-WCcyIOIm9p6rdVnM2DO-7WGgKshjVi4utu4rxHUA52wkro2UK9ZGx9pcLVpAH5xbNeTqTqfgLfh4optCFcdcmjA3rYRaZ2a7Kxv4IruiFRe4_e1FbJ1hhKoiW6-6jwMv20PffZmHgs6a58OrYQmTKSAXfdqE_EJFpUyNYBbVBT9I6FxmZkvtj58gTJzGuoaK8GSNBRyBr96TsxzxyVPNhk2swO4j-_kg_wRw2HNDEVyC8wWDm54hSQMym_sCGfZfjBG2fNNwovOAATpT-GRQWvRNO_GtwiPzye8G0waW4dH-Qmnz6JxSpDq7vYzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsZyemUv-sLZ9WT298iAtj49KTmeNJRNOOH_mbGF-5XTMIqSie3Fa-RtF8Aayo7Y2mV5NTqCuC0dOiDD31-02-cpc0ZrOPHa2csSlzmwl7LW1yc8ppXn7de31dREKpjG5uKVNSUWOwDEWMUawOcAz7qQIUyDEQl4YOPK7gS2EAZyb4o_sKm5Hj1qwX9lk9FtA3BnY9Tvr1jDfXvVKIw4nG9JZztX1-Ci36Z3wPvtH-R4r7hxI2soYqRKs_J5MP0NMDsjJfK5f752I2Sn2J_HDEUEEJf4FTgxsRr3MzfN6zq9VuSNQe5D7sTMRep5xdo3xVSjBH73611P_u3LTOgD8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25324" target="_blank">📅 01:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25323">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-90fn37_zpggmMb3zedq83lr8BrAioYXplY5oecuVqXTCydEFI4kaFCvcKjvXqQbbLoLouetGeLVSD5LnjvcPw-o8cnwLdBZqSXQ3e_JIx8w0MZsjmS0yXxgDr7JsnJPyfSwIWvq17T6ngyVw1AAFKr5S9kjlrGlknn0TsXhZIH8QbiKVPCfViFMZpexuVq3mSqoZUtadhvQMsmNeRTyWtCex6cTWwjEe7-mshdLWiy0t_1Qn6LxF-zUs_7f-dHE8j6nl18E03o_FJY8Wcu35ZQCeadkz7nwuffdyKoLaJ6q2RcnCcQ35SDCRaPhbaud-eb6V0047v3GdIQUB-Ubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
جدال‌اسپانیایی‌ها با یاران دی‌بروینه برای رسیدن به فرانسه در نیمه‌نهایی جام‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25323" target="_blank">📅 01:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25322">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAhXcfT7UHpgElRx0lr3dMhS8_mMLX5F6zK0Z_M0Uvt9LUH_byxdXRwy_qJLszsYguAabgU5UuqE6JwQzpf3YmOvN8BO7-sBGmA6YDeepBtLBTrr_0tJGx_0ObE61LAfJ6S9veCIoVOxXLyz1DQr-s3ictPeDqy2nrR4dDJ5J3QSPBqr2iCheB6xFWTcwhlvUY7VJazBQf7RwicxbsYNnUI3TaJqdq5W2aI2YLSStkB2PFjeLuatHz3GNVB7VHafBIjfOgPdGwoOpLVA7DOLmXq7QUHCrx5EqOg_a2bZ46Kqu0hWdBVUyPDss58AgavJAulOkJuRqqu8eFDSLQH-eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
برتری شاگردان دشان مقابل مراکش با درخشش همیشگی کیلیان امباپه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25322" target="_blank">📅 01:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25321">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhZRfTBsjVxgFL17BYY7FgqojD21BTPabQyX8y6IciktCg1ql4KxFZFsKiXneTK5R2c_FNU7Kiy6ChuKDghdoBKHW9kMKOtsA0JgZCTFAeZHeu7rI7S7n29WLywpYToiKCRUVLmdk7_EEN0z3F0RwUJtqewaNkFJqS1rODlu6vZbAPSURYFESx7ukWxt1-jFwvSQpBETU9SoyKl1s2ALa6VyH5XhRBZEjYWQSf67Kjd7p8dAyrbSYlbvgeN9hJ6k2vLklvO6UZAk_24cwmr4_4s75-AlSsJlSv08ZF8gxwR3BK9jUWCCLWfxENqx-9jjV5KgcMmPYaOyUrljcWPsmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ مدیریت باشگاه پرسپولیس بعد از عقد قرارداد با ابوالفضل جلالی و پوریا شهر آبادی از آن‌ها خواسته هیچ مصاحب‌ای مبنی بر عقد قرارداد قطعی باسرخپوشان دررسانه‌ها نداشته باشند تا زمان انتشار پوسترشون‌توسط باشگاه؛ بخش رسانه ای هم پوستر رو اماده کرده و بزودی…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25321" target="_blank">📅 01:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25320">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gI3rPL3z11wybMYfIQpVoO9mvagSR50Ut9vvLCqLGMKyAoiAP9khM1nU0yDwKyL05O1oLx-yQ7yxIHL3_14-WW410tYxWLtH85lBq8oGSAM_G9lS7Bl4b30KvN5J70OMW1Z44Yu-sKBMUAZEiqCN7Fv2qsYhH-eNLm5GQNz7YHCluqFYnuT1Ml853Jm8EzbOL6o2Eir3mMpX1anh7u_X0RQ_NxVqIA3nOyN3HDgU2BS42Hys7uBnI1Fu-i3seWNdE8NdmfhNidwaO5KqDsFa0ryIjR3dgzfFnroZsO3QzWlrPKCkAFvUhzhZnA_8ao-Xca-2gs2zIAH96UPZaPAeyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25320" target="_blank">📅 01:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25319">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzzRYdb-InqXBZep_bKuhsGZy98ArcmCfvO2dm27iQIN1qsT94_9fW2LymCAD54-SMUNyI1fPyNoKVqdn_eF4KxSDqsSQ85wyl5aoB5E2uNyqwHUfTDNBnWcH2KL93CTyWzlMtyEG9vVUiEdQ_DXEw6Gne2hi3geBooXjgktuFSGVP3iggWswFpzwofl-hKiVcpAkm2eKpJYtV0tNjvja7sN7PCGNfqhPnVqUkO9kd6-WsbDNXfVXI97nRN4ShbOMSYBXMemzmy-TYfBtEOxDQdIuZYAOZO0wQcdrMPA-YgEjtM8u29KiQ5PSlJi02Q2L6Y7ZciHBPswcsozukgEzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25319" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25318">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2548666d77.mp4?token=jw02Fdv6trdry02wXVtHvDbhH-HPNBTRLcdOlWS-mrdVZ4BbJGpzfos6gHhlFc1v_9dbGDeA7dAk4Vpvqx0KquCWhQ-owmmkTCci8KhKIOAv2eUleUYRuer30mAGA8WE4Fhd0BJnvpgK8CDdC-0waGM0sb084UDjvQbm0pInuBtcfmStKVe24VDK3JyLOM93lebmXynjLe20nPQpJJSsqi-hV7Uo3Xo9rjsEFGTMJg1nj_FmID2VpKCbf531ua9X6KuvlGx_ep-PRsvc2lEBWUmm7ObPdorEiF9EF9IQjO-7ZQmyM6FPn0bHEfm-NacR16GR0rXP25TV0ve7dP4-Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2548666d77.mp4?token=jw02Fdv6trdry02wXVtHvDbhH-HPNBTRLcdOlWS-mrdVZ4BbJGpzfos6gHhlFc1v_9dbGDeA7dAk4Vpvqx0KquCWhQ-owmmkTCci8KhKIOAv2eUleUYRuer30mAGA8WE4Fhd0BJnvpgK8CDdC-0waGM0sb084UDjvQbm0pInuBtcfmStKVe24VDK3JyLOM93lebmXynjLe20nPQpJJSsqi-hV7Uo3Xo9rjsEFGTMJg1nj_FmID2VpKCbf531ua9X6KuvlGx_ep-PRsvc2lEBWUmm7ObPdorEiF9EF9IQjO-7ZQmyM6FPn0bHEfm-NacR16GR0rXP25TV0ve7dP4-Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
شما حتی خارج از زمین‌بازی‌هم لایق احترام هستی آقای کریس رونالدو؛ شخصیت بینظیر و قلب بزرگی که داری رو هرگز فراموش نخواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25318" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25316">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f822cfdb19.mp4?token=ZSF6u4px_aCikv_NPeQ9kpQ3yqJvk_ywyWnChtH59UqBhggXZxO3CGdJb4NswvtDI0jzslnFRdtdX0EX6Tqjv2MPZUdBpfl-ynbSSYje4kqryHgFnUoKnCYd6eYW5YYPmA6LiTTuxo3K6e-pL5hl7Y5rifC0oD7hV5nwgPcGnDMoqM-6Zo742ERfMctuzfH2vVNmYGPLy7dlI6BWzFedhdY97Wi1y4vAfxSeQnUnITheHZHzU5t-YZ8CBh5Y1AuZ3qVgI-8S0FxRsNJoSj-Z2L-C-7z0YVrmLD_TghPI_u0PMa5T6bSjPU2yYGxMoc4IdmUfRbyr1ZDVS-_k9NbpHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f822cfdb19.mp4?token=ZSF6u4px_aCikv_NPeQ9kpQ3yqJvk_ywyWnChtH59UqBhggXZxO3CGdJb4NswvtDI0jzslnFRdtdX0EX6Tqjv2MPZUdBpfl-ynbSSYje4kqryHgFnUoKnCYd6eYW5YYPmA6LiTTuxo3K6e-pL5hl7Y5rifC0oD7hV5nwgPcGnDMoqM-6Zo742ERfMctuzfH2vVNmYGPLy7dlI6BWzFedhdY97Wi1y4vAfxSeQnUnITheHZHzU5t-YZ8CBh5Y1AuZ3qVgI-8S0FxRsNJoSj-Z2L-C-7z0YVrmLD_TghPI_u0PMa5T6bSjPU2yYGxMoc4IdmUfRbyr1ZDVS-_k9NbpHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25316" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25315">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c42773d2.mp4?token=TUS5G0xjhVA08RxZneJbC6qozFIaMxTh4ZqvWe3twhKWxoIyXwWPVJCVVVSm1wjpGAcxBy5D8j3w8RY135ildOud49FFz6uL5yAgrfRSiAlfqf81HVxY3bEE4ivxFB4bvG4eCNlbgC0_MoyPVy2M2B6F8R9HVJt0jIa91hSvo5SyS9VD-XcyGoVt4WVC1yQ2M2VhhXAOw_mbsdaHCkNvjEGkQMEagycoaDCid9dgv2eAfex4PH4Wt2fyrrsYP9Q6jBM_nHSD8yeerAQPKzSOwp1i_e3ivnwuL8Bm_zP84b6oDp-mTWpT9U8Srii-BzOgahHhspixYOO4oMeTuwIQZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c42773d2.mp4?token=TUS5G0xjhVA08RxZneJbC6qozFIaMxTh4ZqvWe3twhKWxoIyXwWPVJCVVVSm1wjpGAcxBy5D8j3w8RY135ildOud49FFz6uL5yAgrfRSiAlfqf81HVxY3bEE4ivxFB4bvG4eCNlbgC0_MoyPVy2M2B6F8R9HVJt0jIa91hSvo5SyS9VD-XcyGoVt4WVC1yQ2M2VhhXAOw_mbsdaHCkNvjEGkQMEagycoaDCid9dgv2eAfex4PH4Wt2fyrrsYP9Q6jBM_nHSD8yeerAQPKzSOwp1i_e3ivnwuL8Bm_zP84b6oDp-mTWpT9U8Srii-BzOgahHhspixYOO4oMeTuwIQZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25315" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25314">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzPuMgl9a0cWsdrxvvETgkVr-_j_U3-bvRNMvMg-DXNG8H9QKiPxR5EMisipnuL-NbHhE3U4y6peVe2s--mRS19uSaUQ7Da7nhrWPf_OOh9kbPCjOItF6RTTxnPfTplnwnXeE5WJ1Ax_QODm2jfObSwXf1LJpjwxLqsqu7h7URQZnpEzLlLWt7wvxEBP1DpHFn8JM_crfRRpildkG6fGz9cXr8sEL_51lPzVUlGlm9PHfOsBzz2BBRQtNiN0cK6t54y9Wvboe5g0WhpgaxohS6SjQ6TQlHpi1GRMyjOoWPVQPHMNPT-xcsI6FCQxwtA4pEenL7GKE4gxPeIAGaKH9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25314" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25312">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfOCQZ6MAYpTmXME_Z8qjJ-rRr7m0bRyFHlsrTbXSymoM1i3zpXLWpSpkSMSlvjtyokh5Y67Wa27A3aqGAFPdnhIHin1LSSbPROcOBoKR24exJJv4L9tgLRQKab3_L60vflKJ34ziVrj_6E4aqUCHAE2OOiBzNflQcbV6L5a2hdA9HscaJizcNOO30x91eDWRO3hqvG83JNfqi7hKrpfX1ejN_28whWylmtiMdgcQdst8WZ_ub5agnp4d-lVIJXFnssJvcy9qcw66lPgx84uTj2VmC14NIPhDHOzvsX5q4F26F9z9HCKGv9-FVCZlqDtlC2XGwlPeoCuaz5gyUm2ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25312" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25311">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=Mxv1jV1ik0bUgOaHAt0Zzd3_5lZ-8zz1ytWaWgGcYgkwCKqpAQYkX9EQMmHCwkna5Lgtb0XKzso0f-nGjIUFu2NXMU0PaAWgqe-hndInyPlXmL-kb0QXBwSRKirP4XLURSnNtUU_DwkcPNXwn0HOB-FSVjiuvWMfHOQuiBXZcOCNJyRqB9rvCbk7Z_B-NE9oiPZ6IJRPuwQ8nwH6GBwd9bjZMOGgh8kGhcbT8GodDkhLTEKIYnvauw38E03dKSoBv59TQro-qFkDkSgdmQbbnAyD2B3sFEyRUSiOL20vsBO4v71qVdz4ea6x5luUOWRzADaty1r2dTdxcMlcDXqSww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=Mxv1jV1ik0bUgOaHAt0Zzd3_5lZ-8zz1ytWaWgGcYgkwCKqpAQYkX9EQMmHCwkna5Lgtb0XKzso0f-nGjIUFu2NXMU0PaAWgqe-hndInyPlXmL-kb0QXBwSRKirP4XLURSnNtUU_DwkcPNXwn0HOB-FSVjiuvWMfHOQuiBXZcOCNJyRqB9rvCbk7Z_B-NE9oiPZ6IJRPuwQ8nwH6GBwd9bjZMOGgh8kGhcbT8GodDkhLTEKIYnvauw38E03dKSoBv59TQro-qFkDkSgdmQbbnAyD2B3sFEyRUSiOL20vsBO4v71qVdz4ea6x5luUOWRzADaty1r2dTdxcMlcDXqSww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌هشتم نهایی‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم فرانسه - مراکش؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25311" target="_blank">📅 00:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25310">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVCfS5-F8sXfNtwwhCr8QxyRZYgbiQVwPqMVSr8sHwVS-nHbH3rw3peYJa3mEMFkM580kTIKdiNzyaJY7q_Mw-GFl1DWr8X9W1-R7Rp_zfEg5tTaQJCMjGcREi9eNqJawOiK0Cy_gGSgW0-9oyL1jlcfZwoJ44fdQyKI5WrV5srqIVI7nmMZf_1B-ktRT8454OHyMPVF1sneDXr_8Ujlzj506Ind-bJSFt2UqdVP_EhXlOE9Zo-XJ_SGBLeLrLcnxBY_3ANdG4C-u8o5HGTxbR0eollZjzw8iO4NDxboPs-kNQCuHhGPbkNVMolqijRW65Cc5B5tqqB2rf5nsFupdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌گلزنان‌تاریخ‌مقدماتی جام جهانی در آسیا. علی دایی با 35 گل زده در صدر و سردار آزمون با 29 گل و کریم باقری با 28 گل در رتبه دوم و سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25310" target="_blank">📅 23:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25309">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hST4afyBdS9iJW1T7EAUnCpTD7JbQ9M95B87Bdm8Raw2byTb3ko_fWrKT_TH5dmYwHwxh99aHYElJqQvd0Qx_ydeBdWthFOutP_ly_P0rwVm8Ame0JFZzZojzWe52kgmT09d0iKK9k6o2BZkQTYdNgqyFd6vlUECajcsH_TPjqrrh-MmfTgxZdcyXmXIfRSUdxgyvuGtuTTAvGKcCctWJj1wZdM6I4YVd_g4yj61-lxV1pVsk-yd4wdlOqUVv4K8dF8cEZGDVZ4_Uw56wQAkGu0M71EyLmI5XdzJysTaKWLjdi6Bk4qssAO3DUVwkHX2GGq8wz8tqHBTXVrQVMOfYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ترانسفر مارکت؛ باشگاه پرسپولیس برای جذب پوریاشهرآبادی20ساله؛ سهیل صحرایی مدافع راست جوان‌خود + 500هزار دلار حدود 90 میلیارد تومان به باشگاه گل‌گهر سیرجان داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25309" target="_blank">📅 23:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25308">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qkt-n35lGgldylhJsnJsbZ5HkTfbvO5DTy5ZRmGECfEmnBXfY1A9hFpN8UFGuaSYjQdRc4CQ6s20lWUG7NceZIf7NXrvPh5UIaTIOZkaal4gtyi51PtQQnF6O7bH50tIuJS4Qco2Yvw8g5j7zrpaeLxNwkIGIXir1rpBucoqkxBe0ys0G1C3UpCPRojw3O3LppKoZ948atRubPlfYyqS0V-VZckf_2m6rXf9PUVvA5zLj89eJZh0_ZRJlcx3yrjKjqGLhshCKKXg6nrOzZYF3ijGdDo6bExsPLdGg9Llx4KXJioZaDR7SKM0SaI_Vmhze3KD_0QXt0s-MnR-EhVvsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛ میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/25308" target="_blank">📅 23:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25307">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqHn4F0AU6PEQjTUkgn_r6mzJ9o-ezpz9g_Wxsu7V1s62fGabqSzhLv-0xvVP3LY9BVPpFkFbDur4uO7pnTDlQ4BlNahVZ9oTOqjwEFX_MBBEuR83boGqTRrbCLy4w-Q8vpuhMIQYh6T34CzWQGwGG1rfe2DBKpyrMHBcl7j1NNM_52XUCJGkrBXhkSBB_H8lbZP08hLJkHKGe7MaChj6SjB0uny0vDLbdAMBC-w86EoCYCj_HpFEfkvIhJOuI-yz5EqjXyU0RhOzWmfb-nzDdyeP_VE4JGe5t6p5xS5IeuGXRHXRcDnfduA8D35ov6YlnXBEuRqR3TUmK9dJuQfiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی دو روز پیش پرشیانا
🔴
پوریا شهرآبادی مهاجم جوان گل‌گهر با عقد قرار دادی چهار ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/25307" target="_blank">📅 22:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25306">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3-U0_EsKR8KHiZGefvaf3QEF5e_MPoizuc9RIyZF3dDyq8BDNyxr6Tpj7sfoiegSxjFXcabw6klTgTnCDLciJuJN2XR2Sza-hrR23Rkjy_eOJ_nAXf2A9ZMeihlxETlDJ5-lwDRRZxGuK4KM7cIuVc3eNsyYnSP24AdtY98jFJhNWNQw3NeosVSmPnGc3QzfpFrwcrhYyV9ZpxSZIQzdiStN2kFIAX8xUyunGgEOJ1Z3lnRiFNzArik14T1JxiYf4xuqmfzLKrU259kmzDZ1k20K1kOcVxExgkxWPcRYbsEDTq33ZaFqAvyRpQrmrmSlzQKG3J_Fm5Ylw8xhs8NRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/25306" target="_blank">📅 22:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25304">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KUOgN93o2C60JSktqmK3X4DyakmoWfLCJUdXE69PmbS2ZYc5TQ_d94VQO3KpUbGWffe66BuGW6uA6d-Tv8i7zY_jm9ZU-9LC6U1_va-QRZz_bKkqtvHYSrOSvNns_n58POnO-Xka_h6FCOmN_Hwppp3aVS6Drc1LzID2_yIO5L7Cd5cbZ91fPd8-wMW7panQtceMbWARiIlXDMUg4EwqKxLQ9f7pWuJH0auaagY4jLXdwjKLeGdb2_lPN9cAwFbqmAqc4ILeAYlLfLYLvmhXFJJcDvRP9OVighpAjZfAlVPzxHmU1PkJGZOCB0FIQx-5qIP08AWnAGaWEtrmxdh3QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g_c5BTrfSDopLODA4DM6atWjY_SiuuB0oq0bsilY_wZWUJikrZFhurgQqfOHiUsyl7uHeufW_dVy9EKbyvwChtOthebyHDHQPMS0odZd-jqcihFzeQir58UQA4q4z_QRMPwxGrErXQLQo_ASF7YCR3x-zk5r5ijzLGKQeyMIsSdE5AIrMt_MipRWiEX2MFDrralRDhRZLkhsf-0fTAyrcYYYMUTiOgKnCd6Z6VahT5YtIACwRYNNtPYFaY3AjOhg2UVmeNTXWcYI12Oog12NMqbo0YHU2Cbx5fM_xeN4o5DHItC-4ON2Um7sE4dh8aKX6MjBqahkofzAJBzaCIKgVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ازترکیب دوتیم‌فرانسه-مراکش در جام جهانی 2022 فقط 9 بازیکن همچنان در این دو تیم باقی‌موندن. بقیه‌خداحافظی‌کرده‌اند از بازیهای ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/persiana_Soccer/25304" target="_blank">📅 22:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25303">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l84L5zAOlbYVSNyGh5XYpZoPIRLgPrBX5EQySPeY5XEkTPEws-YG0QxqoboFzFOOUfSZykyQmtjfMUZES6_QrSbdpyXLiDPngVQKfFkrhK33z9_-CMIHk33w-Y97U_sDHsW48AUWGx4Kjly1NcgT5wpjAVpvbbsolTkGdcVvXKCUW3U0Z5MCr-_5gWtX7tSL6fEuQ3HdBaqws1w5ZtVrPdYIE7XhVHR5Iv-_i3EBpMgBRlW9PF7erkt6WuoLt20zbRCmgZzJ9RE4MuuC-J6z7O2rxmP70xP_2Qxptd9QkKhVcxB9oE6T8STH-C06svwKJp12fhPW-pz2JAWZ8C9aKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/persiana_Soccer/25303" target="_blank">📅 22:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25302">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhxCv_QdqOkNU2Z6wpSDV_-UVYto-R3buRq1djkmjpX512FeGHsnxGg5zHqZSgvE7EJ9Uz0Sf3zgzrajcyrXfRjGSxX-2XphnF4W-9NfrFBLfLn_qcEVkkhLYP8wy7bb2o9jK6Xsmaps3M_oQPHwRCg9QMPIkoC7CgSmBSAOgWxwxSEAYTxyM93QpJhmQBa-0_f_ZprKjLmJW5JG5A_aulAg1lpzv-5d9qXI0MDSa4YJKMITKhg_DGo9osNzWJSlcII1tKgjymb929F9o-IKf1m8JEZXkRrEbbpSQtvaAYEVrQ1B0PhWbKkq9gsr0Yn2msAWXNdSM_KkcYhJdRg6CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جلسه‌مدیران باشگاه پرسپولیس با مهدی ترابی و نماینده اش شروع شده است. تا ساعات آینده تکلیف ترابی با مدیران باشگاه پرسپولیس مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/persiana_Soccer/25302" target="_blank">📅 22:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25301">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzWBJUFqEWo4bTtmM5Wl8fcAWakvn2VtDw8Cxm9awVI0kPKI5XWaF2B-SMdRrqRaLcomQIoNCuvlJdpQLSFyatGIf822gupQkszf0gAcsihYr2ye6ig2R29NXYHFIXVQDOx-uflHp9loLYTUWOr3kR617k0vcUyHQRdh2nti44D2t3KKdXUkTDRyOgaYfmK05Xcia7cEsZTSjpUnaws3sLNF2LddhLAuLK4UiEkgBLfD9y7-EKR8G_o0jZcqHvKCI-VLsLUN8ZerMUvA0b1rUSmvHnXBwNfvonPs_zi79kTz2DZRXoS-eU69FJ6bhzNUBniQ1yrhhmsSr25NN99m3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیدارامشب‌ دوتیم‌‌ ملی‌ مراکش
🆚
فرانسه در ¼ نهایی جام جهانی رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/persiana_Soccer/25301" target="_blank">📅 22:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25300">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_nkjkviq4U20mlHXlyTmvHf8NCUcFR4uLE_xd4Cew9bUJDSd4mIeLsrKsa4r-wZFPhoiwbm8mpb_BYy_QqMmVu_cv69TN7DE07LvqjsnUift-0hHc17hrUzjnlMzBUIMvRiDPV7RzQ9TDG_c2tdDWFplJwFRlz_gmT8d4Y48L4bHT45FZ4GkaH91MaCMv2xLBRLGtBu9ym4v3QEoLvaQJsfRkmva2SoYL76jXalXr0VD9DSIYnUe_Iw_XdIFUxT_vfx4Blwc5U1wi1YoIJtocKb_u-SHAG5FTOdGnJCfCq9mLZ-qkUJMWkZmJa-FLC3iW3T96ZzdJdtWVHN_qntlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25300" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25299">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrI7PJ6LI5pkaZjJJIWQHf9jFjWvTelce_xgMHxG2wtyJTCIWXNwvtl8Qgu_KVvRKnTaSm8gmJ79wSackJVpeoKdVdhWH5x9CVPQir08Hs0UPV71aD6EbjBReKWkcL1l2a1PxXOkxtyGZpxBAiTa77ekbM2eTgzQeFebL4KVng8_c52sd7r2jqTYY9uU4JDycmDhRpljfrkEXwcjpuxZ-3gOZcmcuwJYb1Yl7Ta2gRCFUxfps8YfKPYHs5l1Eug2fSAYgZF4vduEtu3nUwe0O_HSQ-XCvfWJ8d9kZfKSh8iGg5iZhVKpFlN92C2a1By-uoBHDKZx-0ejO-DXAUUDEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25299" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
