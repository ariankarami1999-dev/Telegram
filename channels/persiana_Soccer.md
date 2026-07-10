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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 02:22:22</div>
<hr>

<div class="tg-post" id="msg-25409">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nbf3L-WYiMBbsJARhkm7wmeUp9I1AKDTp9_0Rj5ERb__PvIPdEnjh08IKyXJPpDfXbQcOnSGO2xkyf8G0FmE1HIaHxRDkMrGGUtTFtAsrq5ErNhCyPBN574pddNuK7N9M_OA5DmIxg_ZcDYfh1qVeb7sruHfkd3rCnbJxXCF0sCYHk4Xwxyc4k0H73cX_p-EwqmpHtd9VgvN_7ePSuYXuh-eCqOZgWWZ4W4OVpu_8jTD0CgARkJ19iRXAgNA5XxngpbpFiTOFkDF6sdxmmXfb5d87zVYujzuuwvkjPpRTSKJy-aGOesk8kn37UgH1ujdWMV8_LxYw6r0xaisV4WiYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#نقل‌وانتقالات|نشریه آاس اسپانیا: بردلی بارکولا ستاره تیم ملی فرانسه تصمیم نهایی‌ اش رو برای پیوستن به بارسا گرفته و درصورتیکه لاپورتا با ناصرالخلیفی به‌توافق برسد این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/persiana_Soccer/25409" target="_blank">📅 02:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25407">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/25407" target="_blank">📅 01:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25406">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSpuMgmbkm7GTXcCPF93jgZ_L66O9lQl3pMLPzD-KEl44ELFfHCZydQ_y3qkdKRnSlC2HAb7EoZYBP_D_pNeFuJ2g4HqAelj7J-g5EKN70Zm513Etg3urFi4DTr7ktUwvdcdEizb_cKRJQnbWsk7ST5OgYKDn64wzquy1iR8U6nZCAjHtzLKtQyJo-4REb3eqb-EACiKPmjt0OF8YYpZotrfNXj43RKJ4_TZ5QTZrdUjUTZkbIZmhTQs6u2gv2Hh8vI1E9u-j-oIibEG0j4lQ6pf3NnwaJLRFWuVfKLOHEUxxhTUxFqDQOF5rxzYxOU004fF_V6ojbEFwYYic6LnSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/25406" target="_blank">📅 01:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25405">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lzgyp31Wcyd0OnmCHIGmo78U9UYF8x6MHG_XfV3U3LpGmH7cFUbBTB7EvZ67t5r1YfbFJpIFkNNmKPxZoOjcOhzbjNqQ7zDhOIsWYBUwoIDbr3UzMcodwZZULHfsSk7KtYXeU-W5q3q2kpjITY5vYAfGc6aDHPD6GHUG6A06StCOABP4nMIfxcwoYn943mVVCXxo2HZtYBRobfkQoMTnYtEly-WMGILCRu8SCABSm87HiP8Hr782exuYamdOlP8Agemtxdmc7fr96Q3DObXiBNwwdHlpPpDHopIhhkvhalif7CXSzHY98gjnUv0FWDlk1P52Fr9Qnuet6s0wb2dolA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/25405" target="_blank">📅 01:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25404">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzZXCDF0_QMzXJe4WiwuPDz5JE6UGuxcMe3ohlQbr_1U9IYwEvSrMhofKMnFYV21GdhhY8yUYbiWzTus2XsV9zsDusoACGy02_cvvJ-veFffN5zsSD8vQ3CyBwzz8QTlxKAs-zJrJNXV-30MZcMmLbjDT2bhuqCHqa7vGpJ7SXZH0GUuIEnl3b63qRikMAdq-jH00p2IMvnMtjDbkkHNiXJmSoa5Rd_ByKIAV_8fSXL-0BTYb_EuasE15tVFWvF5JIrrWbxzgkD-JkDoeJDmYoWdtN2LlCset-pDOr0dmyR7UBYL-_x-4PVVI-I7584cuPQEA2a10GYK9Pm6LoMv2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌بامداد‌فردا؛
از نبرد انگلیس مقابل وایکینگ‌ها تا جدال مسی و یارانش با سوئیس
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/25404" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25403">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQgvXUZGDtq8f0Iyz4QpwlALcMjZwC41j-YdumBrdpdX-ofekd7JBi8xQtJQQFk1ycnGuslzjsi8Fh54qgVS3oPh1HylfzTi6upD9hd7YkUDDyQY6mCwSDE8W-hPO0QhHDZaQy9pNxhvC7X0FMMW3ElZJE3DOIAnTijzRxS-0YjFeKyhmPNs2bLam1-5iYuR-Hue9kACCDWU_k0W3u2zL10WbUyMXQodQJTXmigtSf6LvdXjQ54JYeu9QuMRTyJji3HiUVWuyB-S9YN7Eij15uLtt6UJH4qqNzgEWQVKSv3EyskA3jUkyXinAtYdVAGyON-h5ZmPaHw8W7PZSZBwkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دیدار‌ دیروز؛
سومین صعود تاریخ لاروخا به‌نیمه‌نهایی جام‌جهانی با گلزنی مجدد میکل مرینو
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/25403" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25402">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/25402" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25401">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKeBVCt5h1jliEAd0ese7tmPt5ogxGuYq6I9YGOum-x0bC76eKeCQtYrlRUSzUfnbH78wM-F8s3zrwvI_NL747pBQp60pMg0UTLZKTxfQa3oMOPRPjAT6qa9GlK1-9wDUBRdUFUIQSgiqYppPVsMsKU-FnNoN6pGqNa4TJB0rg9OeKxinee-_o89rGivKZI1-gTsTLMYjFrZERe5qSoSqMoholZSuTQwPo8QmF9rHVD5ihJzwMtSZ-JhyuDw1zbws-6ygW3xBPD8njjKstcRaq73FVAVmBmhG-Ynfk-tOsr6tW0iYByTmI_5TwnibjNfj6nu2XtqoZsVRw9QWN-0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/25401" target="_blank">📅 00:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25400">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1yT2uz2ZZs2ZAOUCSBabcnN4fj_MPtQHO7SoxZED-7BFRsd681xtaMpMobgopTeCN6x2IBg97K8TxpPz0grnJw_wFFwn2DJuHnVhDb_LPwH6nhQoq6QZJRf2nXkMlgjbenf_KJKWAv7FsopGicaGlwgjiiAvVk6GYg7IXy_YiNbc8FbG7sajSWD1NO3bkyiFvTJhbqOd4dE44mvfMfnL8SMVkPovPxtYohWz4gFuMdKhznHdvy-Jt9gNRZeC6pchAYW38LqYCJkk6tJCGQJ-JNlHd-q6vAq8HbLcXXEYpWB8lPPUFBh9IYV5bxTcc1JZFSjX9GASRR4iWr_p-66gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دو تیم اسپانیا
🆚
بلژیک؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/25400" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25399">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/25399" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25398">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/25398" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25397">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2Rc4CtwFINz-euCeStzljOLei7JlRtRLJQy7ge6qtqlUHVV3eNJjkMFSKCJPKutWBzxy2AQq7brXFP6Rb04nsiT4ofFjZGNZVrxICHWAjqXyZIwbLbf5gyUt-kHRybDGMJTe8INOG3pic8ZzVGfHZgZqTa62RerBe_x1BJKwasbwrsTkShYrPF1x34J8jUhCWtg-jRgrcCxUGuGUMbh5p9_W6OryKsthmzZtNOAlWgke4ivnxGn6cidaKtzhofGVLBhosfeas4dDlBQaaTAPCP9DiMwUMcL4ekBDljxpHRmFqAghWSeknsDqoM64NGZBWpFXhNs83kBVrbSK-Cwtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/25397" target="_blank">📅 00:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25396">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndqQ9imSJ1dVHsy4BHOBmfGh52gb1wER99d_qMZBXUM_JLcqqaK7bBLa_zX1FqmIbYnqrTmLPDI0GMs9Rl96af-yly6QXAAX1oNABqW_yUKi4ZBFAiC5BVliUoSSTviR8bTHiThb4vAFfQWY99YrMglA-KMYkavFllxpDZ5tCIsvEKQ75XKsT8DJvIxQ22aKQ3Ahh5lSOHytKZ5c9TQC-uiYewq8XRWiV6UCal0KDA8Ujq27Qxw-67y80JhgcNFhb2kXNIE41GikHk7YMk2r_Akj0slRlUtmbIkZVT83KqRU-bYoBR9j2e3C5s_nWfsPajy0boSGgqVy8M_gMW4IGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/25396" target="_blank">📅 00:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25395">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCyI3h7CdSXfOTanNHzaZY1vvirSOjzbMekUVFQuTzdIepP_62jUKjS8Uqo-C30fLyxMMDHjDRGP3B_EerMDXSR4DhbnUOhqgYSB0zuWgOwcTivsHGby7uJtpJfdQpi3Akye31vKQC1xCXSnq6BkDpwIKMFhFiykNQcH5MJx0On3ed_SQzEFBc2zTkjkwWDKKrF1bnRejw6pSXwlRdN_xh6nDHJJVwD1_U7gzvdHwCCknNnuefhG4Z1UhwlVxzaNAVRSTfUt7k0rUmLSrPGO9NjUtBlUwQED1_s0M_QZ0QK705ed7bRe4vvmEHg66EbTEzx7KHNumYZcCroxurVU7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/25395" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25394">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdkfdgH8VDVZKikJAGS-tHqza0NX_LbEIQr7ShnkVqf8Jc4i3W9aKpEFkDKUQ-Xzs4DIvcF5C4LGOiiH5NpyZxSDVeL5oKLbnZ1czBeQMrIUiz2j49YF8mgktRMslaCBS8psWqWkSnU-GIJhvYtxs6fZvWxrzcOZzoEsOGIamMIltM83aEhtF1mm5crlci68Okj8usmlHYpSsN1CrHSJyHV3zx706qfIgxxnBEd-BnrlmXqaQW95TosMiKv9sz7Jq_JBISCyx7G-GsXiol7waX1GSFJ8KaHnq_e-2xaXqLIb8h9ViCtimUVduuk4tzZzXEqXCY0FwPbsD3dKmIXQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/25394" target="_blank">📅 23:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25392">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/25392" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25391">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLWXykUQGfzj9sACsoCI0DIjk7Ayu9RB4M83ktoAWZ_wkU9H-DCOVGLSX0_PNaJXDfvfDKav3fSV6fPbS3efBnM_uKY088JHvojlA0YfNzXlQkTnyS7VcJJoPVh__PW-sqA6ss63z-XSXjMU3O8yyx_DKxiUAiKG2kkOq-dViRUeLjhuN-JqgIbhc_1nlQM9XqQk60mKFg_W-K4Mat0zzGPYxeYU-AuK3hVAu1to43H-IH9x0M8w1Ix1ylI7igvWiZ4cAqlo1awZXASdyIRC6EVOjGnbJmVCvP-6v5akr465L09MoKoB_cc7a4flIcSfHAEuWvipNxtU8qLRDjkHDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25391" target="_blank">📅 22:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25390">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTemXLV_bWU54sQCvmTXJk9ozAiBjZ9mkbeeolUfzsMLjklG3lYNWVUF0-PPDS_bLZ_P7MwRYyD8LbRfiGUalxiLQBuocWkWSjW8aZiruGT1GJXwT7-liHpJwYixy3ZuWQOENFpEcP3_UjDtO7X6HjKQA7KfQNLjNp1IkT2U2htIXnOvow8XL_6BnOYM4WDBnhh_cUYiQVMhuC1cKP7ElNCsXgtj498dJENqsDIwMncjQ-FZy-xdTssqkrDNDjnkWWJ1l3tPXY-jkyfglo0f8bUuoJu2XNTXEUh84LQ9KWgvPvk0EzTDbo19em1r2hRUyE7TdEJi95QHhSVCtGiYwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25390" target="_blank">📅 22:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25389">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzTfmTIhSPNQ0sAQ9yGrDQeuGWTsd_6X1AjF-2xNLYr2MZvTviMUmsvL9CwQfWHj4_0Y-7YLHz6kNvy4PXM6ovQPIUpM5YkF0Ck5LX0bCXFKxj9bMT-smEgIxo-eX3MIqvI-ubg-LIAqbgj2jU3fTQU3kdzXQErQQRzg8_RFBoFffn-oaAXaBBFh_OczACg5hjwnZqqOLk51nbXKb-_z5pW6jGff96szsEI8-4jAkJ0FDBIIatWdoCmTlFOV0ZZYaHhp1LOZpuybs6PvZPNQQYJTjeHrkpXrQQtx1X2yXu19OJZeEY3uLAneR-HMqh3owNx4Nhr3nBg4SXRecEm8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25389" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25388">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSBuxVQfUESnZCcy-WgBVwSbtrhUAJtL8vjwWkGV5KGKCGNdgvlgYJ-YZMcl3f8yVoGZklPXpG_ATQzKXFTlLfwmqLoMKb7qsZANOh11KTXhVz969B0ZzdbEkirb7Ia0zJRK7z0UVf5Qfk_jJGH9k8oZ9bxjZjRTtfhaWI1b3U5n3lkvVJbICv_FbW3yy2JkRiHVQDf3YORUFzVMz8w7zUKMc58JcxbVXBoh2iBeF6xijCuqPQ3WJ2CxzeYQWXDv-BekEs_Da6sDbTorSDsiJaMGI9p5vkINoFW-eV1GMbz4MT2FxMiDPei3Nq4i5vpR5PLxAFH4gGShlJN-O3PSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/25388" target="_blank">📅 21:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25387">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufft5Q8ZM8-GqqCcqtsclwukPbgzEesMhMAwD0YXLgsomgHN2qVtr5W_5L_EHsYQtGKKw-kTi8dHS-ofY5aPerbI0QAKh6g7FIRGAk_gGEtfjiy28Je40OtE9tedx7zT69mOPfsJWpYcdqqeJNFPOPrvSksv9jydNxrhk9Y54ybFjbhMZp3FsbCRStEm8Ln9tudwzUpYFe6ytRIMlu1DllperYuv9nB25ozf6HkR4Yqu9t8h8zRlSCPzEMIzAtt0Ewe8EQJzZ8UgHWLgjeUtQMweNO848NpXl0EX2E-1ZTIz3JBgzSoAPPN-lir88mTdDGc8ReyqeJrlMOqvGFxXwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تایید شد...با اعلام رومانو؛ کریم آدیمی ستاره دورتموند با عقد قراردادی 5 ساله به بارسا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/25387" target="_blank">📅 21:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25385">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZzt836uC8z3LxsTSr7B9NEIcMsvCaLr8LbVtTDSqw3NTBR89DSTPfIJ3-1A3v0EIn9n2YbsPsCbFsn_3_DKm6i4CwIASrzqzKixIUpAujfkZq84Cq8QeJFi_bEGUIv3p7Wq-Q8RkgGM3ZkVMwAHmYlDWcZroABqYJb9LnsCID1mZOxgQjpgwaBBBJbcmUlAdIat2tiTj9kfVDVG0bAoU0IV-pnGTxeMfVLQ4UXUZPN7WC_xqoKe7CewQBKSg8vwyq25Cj6dzD61FiiKSaPB9A9r2yUI15oXo4WIZUCeAEMrdz5qI1ndoBkLf9YfkNAIID7fnDh1ZzW3EE1sL695xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OAI-RxJP9fZJ-p0CowfFzfxyC8RLrWQDxsTPlvWHoGNNXK2qQ__kpxscsVxKlecXLhyqEwq7sWLR5LdEq-jhvKUaAmS4cGqg7wjCbuffw5YBRZt7GPJhP-TBA6Bq6ANYqFQXkcoSl-BA6mDLH1HAVNTLugSTZMXJ_n_uk8258CfMfhuVkESgE5nzeDhjD0OlDcDfv-WL6EjRzaQyOlEVUUQGx2Qzh9C5A-luIjROwRX_Go0eVx-wh0sn-kMM63gaHoPrWRMyZa-NA5JhElEkIPK5ERt95MJIkWDzJgNQJLStGjgXFR7k_v82sOyCE_hxwh18Bq_ZITFPD4AJgC9Hbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25385" target="_blank">📅 21:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25384">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FeRyeWZCgB0Kx9LRF5gBPFiPyVmz8xgC-bd6YfJGdGs-42h3hxb7KbMm6FunuGCpDm4KaER1TOWVGhOSgciE6j7Qu9f9CX5X9t94HZUEVBzClbIPRowrOP46VASW-zg-mmr6bGVkubvLsU4eAAQr1JjUh1puXGf5BPnwSAL1RPg1qUWelN8ix8EkSUfVMY-w1bpVJGDbiPUllPp-U6jH-xEFQUDtu5BeaUpxnGe4rZJshKM2RATPjVyEw75KKnPGWii5frPh7FsqzvU3ctsRUJxv1PHNPkX4gQyiRsJcZ-mXx8qd-CnVCiWdpJk_Gthe3ITPcWC0IT9kD9sIgWFvTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ رقم قرارداد ابوالفصل جلالی سال اولش 55 میلیاردتومان‌ثبت‌شده‌است و سال دوم 70 میلیارد تومان بدون آپشن. در ازای هر 5 پاس گل 10 میلیارد تومان به رقم قرارداد او اصافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25384" target="_blank">📅 21:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25383">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eikViAduk2hjcAJ2wjoYKLhSM50TOl4ba3CPSZdwjmhqaUypdmDn66ElxUz949_fQSE4SPl8TZlXFi2KlKVM72Kc76i2sYJBtop2C7-VBgFx94nfK86U_49UzsEUbFi_h4ahPsHaojCFd0BCHIv2tcC2LyODpmfRHUJWeDZiR8axDG1Cqy7M_Z0lMJU3qhe2N3cuI4lttlJGOevRL9isetRVkeLxvBr8xb9zg7KEQtjBKhEijcwC5VbMLg5Y6ZBT9SKRFN40dcuUDZkJj5xS0rU0nQBA5OJDBKMVMpNoH57l2s6y-ReXv8eWB4CWaX1EhQve6ed395Cg9bw3TA4jyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
#تکمیلی؛ رامین رضاییان ستاره فوتبال ایران یک پیشنهاد دیگر از المریانیزدریافت کرده. درصورتی که با یکی از این باشگاه‌ها به توافق برسد با پرداخت 200 هزار دلار به باشگاه‌استقلال قراردادش روباآبی‌ها فسخ خواهد کرد و راهی لالیگا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25383" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25382">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkh27UkcljpyEveHkaPwsuGS61McFc15WZHHM-OtXVt7pSBgYv5SxrON_H-8x3LuclzgTG8LsHoVrHjl2hFBTZuHbSCY2KSo2Sp2LQweFGOs2NAcWJrdMxq4jjv6fB-Wo3bFln9zaWBjHv2Pk1UU0D8QGwEBvvrP7tZoZPU0jkKr7E5iknMq4SbUOaumATAYHWCIyQKwJt0zpFcFw0txjObjc-1twoG4h3UOcY7mpnq0inrJFkYWituzgqakfeIu5wkhaZa-LsSqq2VVEvMkDslTtLdnwNbEl6phWGE1ylSvswBzcoIwNw1z9BCU4i3XtM6CuaoIf45CfCh94EiekQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری #اختصاصی_پرشیانا؛ انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25382" target="_blank">📅 20:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25381">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5RCeMRQ6tTWcQrQRQF51l6CIHtC6ghQpHEev-olpDMnW5RnoYY5q5zOsKYoNGOIVcLcRJjs2SjtmxPA8mLVyRNlbIhICGZK7d0UF8LGSN2_tP9HqbUTxqNYS-n8noRrChl8qlIJl8WRkumaKiR3X7bujZW6O1ZTGg7BYzQQ4m9emP3iyZAs1MVFqL1Puzvi30PUmhARW5dznY8vMCn26UfVw6JKiGY6FQkHRkrbP4f4fV6VYAg1K9_M1DpwLWxEsqY4I5rCkuW-Ia-MHSsxSpkwi7w3dG7q2toX6EXmBxm3At18dEP72QmmUHJemVmGZTH62teo7imDoCzH5kuWyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25381" target="_blank">📅 20:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25379">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j36jjgj4PPL5Ww6S6UxA3biZSh93hHWzrUM5-nNS3Ltihv0V1cMtA95U219TjYLXal16b_RwlwTgHxsRj7AxlsgkH_PjPVpAOhjxQIY1vXu5rQrpNUxRJH07hadsKzBNSfWLzo9Njn5DEW3w2310EAFAiFPNAUR9jF4MKiOxENbL2gUPHfpo0ud_QBzcf_v1MP5GBqukqgdx-fXOpuNf9xjOvYx9333lA7K0gjKaFYHkW2Wd06o8AHmIldeXx80Whbb03HmO4pouhyvSMm01Toxa6G-ooWP182UbCxWJAOWpKy5LWuK4Rw2-npejDo5x4ILS8wmCYkiM1OkGQxw1IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25379" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25378">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOikVaYFOi6yuqIEOO_Ipvz6ap-WoWfT-ZY8bHln4XtiP824tuOzZAN_0MKUH8WwbBI04fgJt4_dlY1gzV14RADB1pRU6QF2E0fnaykouaaf0odgLvWuZJ8iiHHYm1BfAGRmu3iZ_wqB7v6ZqdJPijx42mxr88_OBLAHTa7pp1tb8v13vmxQULFMnABi_E04ldienaU9fp8RUw9v21NqSs2ogXQ24S6_AXJHxR7z2Z8LyuhWXgSMRjMQQRNR9asc9-mDtvGua6Bvtmq-aqQutSRHYmIXY1nwFJbhhOn7w6rCS994bNuoevYBmDnppa-5l4N8PRv8E8hzjy8PFPTS5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25378" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25377">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GN-sbaKCwwR13ZsoSjDa58zyzZk3158z9oSgN03UDUAPeAoF5cCnRlX3gGqukH2CViWn1lj0DwbxHI9MHlWWH3FYydKihPHEu_ESwDQQnoL1PcWKgMbUx-a6Luq2G416qGSwHwn6Oc0mdG0MbzMrlOBglzaKoySUJFBVhFyUPOaabto9pUcF9iy3_-bkeA4xv1HamyIuvU16ISMsoAa8OanG7pNqzpx-AL35pr-3zNwbPvVnkkX881vDCSniSHeYPx4GF8pOW4umv2gROQlUa0Ag9SDW-EpCKaLV9WAKdhcCab3tdVN9w3JzVvpUNTDaj2V9F8dPlUG7U12BGN0iDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/25377" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25376">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-3kD0FtAv-US1-Q0DgEGWZHTabFceGsvbvEE0bEcUKD6-Cr-nwLO6PELane4YFOgUZEEYw3vPQVlPhee69lWCL7HPnt8HhDMU8Oz-Z71YnbpGO8thU2pe3D4f14QegQk6C9c5sVuDpbp6ktYCEexJdQDnj43TLKZEwdipHzh-G3yh-DwEb0IFeD8wmhlWs56D7RshlZSLuHkCpxMvez70FQF7uhNqlnP46qZ4icsAqiAkDAlu_qIrLypDo6StwBHXglFoaR-PkLWmZXxSta7kGS8-M7KDrVSZTwj2rPizoGsiHQY-oLDblOZsf4Q9PWP7nG7SamqV9a86AY6Ble-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باتوجه‌به‌صحبت‌های ایجنت حسین نژاد؛ با اینکه مبلغ بندفسخ قرارداد این‌بازیکن 8 میلیون دلار ثبت شده اما باتوجه‌به‌اینکه تنها یک فصل از قرارداد حسین نژاد باقی مونده به احتمال فراوان با دریافت سه‌میلیون دلار رضایت نامه‌اش صادرخواهدشد. سه میلیون دلار میشه چیزی…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25376" target="_blank">📅 20:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25375">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVIGE5-vwYS6TLtXEE7vgu9qqOl4bOSB96a8Pfyn9Jo1JuQfpK2lYnwRNrvayDddezNgSK9pjuPTyRjLM9EGdwwcKCgWEWvdgRMaj-7HviH-Da2xeLgdxYfy_kn2YLHlGWBzTetPfBwmSZTBOYSSvg4cMc1_ZNt9zjPdMvJaMCrJGTqcj1zhRIwdwmJ01SWz7YJp_Hn_DOcN09-ixPKwl-KO2UWpJx5I6cVZb9hAZW5rUYVcJ5mKyF5y93wadmKh-LcFDrzCNTct9mOsXNQTyzc2zIyBA9L4GpMPm3NdMsxxUXS0keLG4Vq-h_cx604zBhXiJ7jr06Bu2L8tLUnmTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
🇩🇪
#فوری؛ سران بارسا برسر انتقال کریم آدیمی به جمع شاگردان هانسی فلیک با سران بورسیا دورتموند به توافق کامل و نهایی رسیده و به زودی از خرید جدید خود رونمایی خواهد کرد. جذب آدیمی ربطی به پرونده جذب الوارز آرژانتینی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25375" target="_blank">📅 19:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25374">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5DXgNDqSkA_utCkV2wHaeg4GTzYlnyynSAmYh2gevMQhxgHwXPHIOv0R-IArE1Yl9MMiMehM_6An95jE2OYvySpx3478HyEZqDHrDAoNwQFRIJOfADC9F_XjJR6XXNTcBs2EiR2P0c2jkPuFXT7gRZF1JIYECdwQ3ruHyoBrjNxmL5Zs2EP3ff-g-V_DPvPg3Ec5My2FrOCbrraLsE3ZAyvDp3By2BYzEMq9zLaCFL4qxfvfiXAmM6ePcgd42XzqtwsNQERu4tdcPZOXr_-3pCljKtg4maCv_dI2Qgz-kK_c8Sq3SuDAORXjdT5AnRNQUohJevLvP3pTt28aEvAmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ ظرف 48 ساعت‌آینده "تایکشنبه" تکلیف نهایی دانیال ایری و پرسپولیسی‌ها مشخص‌‌میشود.باشگاه نساجی برای صدور رضایت نامه 500 هرار دلار خواسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25374" target="_blank">📅 19:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25373">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=bW8L1mdYEapygJqF5cpMpA6i-CWCU5LUYOD65eYQs7varhxt_DfOLXGfvzeXefJ6vT8WF0dBIFPBd8PgfUyGOcBgJ_2AgdvGRP4lyoWyIKSx3pt7A44LiuQepG_K2vV0mjhrEuwav0iaSk8-fhXZSDuiM2DRMrGSdo2r8_VVCxhLnKO6195grrzOch3ryUi7S3NJxsHf7CkFx8ps5zRqqhpwHSEaTj0CSbkrFquStzGLt3o8XvboZs89m6qX0qLKOnlBEIv97h7XoYqQt2mwEF6O77S7RoBKkWnDw75_-gTFl8Y_v84a3-OZpwlzdX7Gh5RJP-Cs5EfeEGXe2c3Sqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=bW8L1mdYEapygJqF5cpMpA6i-CWCU5LUYOD65eYQs7varhxt_DfOLXGfvzeXefJ6vT8WF0dBIFPBd8PgfUyGOcBgJ_2AgdvGRP4lyoWyIKSx3pt7A44LiuQepG_K2vV0mjhrEuwav0iaSk8-fhXZSDuiM2DRMrGSdo2r8_VVCxhLnKO6195grrzOch3ryUi7S3NJxsHf7CkFx8ps5zRqqhpwHSEaTj0CSbkrFquStzGLt3o8XvboZs89m6qX0qLKOnlBEIv97h7XoYqQt2mwEF6O77S7RoBKkWnDw75_-gTFl8Y_v84a3-OZpwlzdX7Gh5RJP-Cs5EfeEGXe2c3Sqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین فیروز کریمی در برنامه دیشب شبکه جم‌تیوی‌اسپورت درباره مربیان فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25373" target="_blank">📅 19:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25372">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WI6CI1n5HzvC6VMzUvkWoK7v9GtM3m9XZ1oZNlYu39v387CMOYYGJsIUjWz69T3E3b7ErlyLhrBveqHimYmV6qEQ0mosBRkF3-tnxo6WY61nBU1vWswRdACKAIzcI9RUz3v18o73R-Oi3xq-da3D-5QPmcfYzHJwpu4et8RDysrjDvXWmqVRH3eC833MMjQTh2ZND7jamAReu10bCdGbnoZSSLRMsTq2OX1yL704EaOpkVV1XndYAcJMHC0VpQ7otu4MFyowA7zK-1DbdizzS-sXyRSNpsYmQUElBhtyi_ZBPMtCpOf905PeMbPF7jsF29VKw4mJqYzZ64POMf97qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25372" target="_blank">📅 19:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25371">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwK7K6DOzcMcq28L6KiXnMULl57aKH4vSMPzkpsxXRX8n1AItr62V4-89nJgY6QE1nilZiIJqoRxFKxAXrF_DSQnhOPVpW4KH5qu2_YgjbfV-Al6CkQq-JhzKxhL7JuIK7Bf16ojE1RJXdF7yfIYOtPEF0kzViqDUdGUrlrtGZk_LgdthJmyna0TuiDzBX_BjX4vu20NOOjw-dj9AxZqPkBQyUBZ_zRQbmBl3zulAX7gheTuhB4-wb-ixuxLQjrpIFpTNNiPw-3lqDBXRq562tKd3zXlbReyumAKDjht5L7A76pI_rI1v7pDe6SBRs29LOWanHSM00h3pambCiqqHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برترین‌گلزنان‌تاریخ‌جام‌های‌جهانی؛ رقابت برای شکستن رکوردها همچنان ادامه دارد، اما فعلاً لیونل مسی با۲۱گل در۳۱بازی در صدر جدول برترین گلزنان تاریخ جام‌ های جهانی قرار دارد. کیلیان امباپه با ۲۰ گل در تنها ۲۰ بازی، تنها یک گل با صدر فاصله دارد و جدی‌ترین مدعی…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25371" target="_blank">📅 18:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25370">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ayp2Myav9T3Si3LUw9vhGh4cfnIxNE3nM0K3dtKbrOZC5oa14v5Xa8X4W6xpapDZ9q4Ryuh8sPGmpOiJGyxpPtuKckjiR934OxMcZUyPHHICUWpVX8VmUTJkgyOm2mGCK51iJ5EbGwJ5HSyYCjYJSkgqFU98gN3VHG7WoZVTddm27uH5iezhW0hTbNr5YtFJtLNLiX074bE_k655bD3vvPiFuC71TN6owpNIW0e7idrC2Ywy52pprUyhLk15XVYPB0fsppowrXlIgSwSDDhmlDT5yTW1JAwMuRXClf4sVZp2KRLMfswfNnOO2Ju-yrjKGV1J8X8Oqh08mTkWFksh3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25370" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25369">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJJcd9X0raVxVXzPVYUiUXhnNh0LBX8yak3GQUYhsi9uxNkUtU_pwEaT-08umZLC2a2ChSb1EHHDQr7zs1yj1v0wJ-82vO5MdA9UGrIa07-4_AD0AhczEnLOVXLUFqDBChJYiM4kAhLbPEnGnnO5I8sBSoos6paIqr7lzHneu2ifLyY-Uw1uFoDeOrayt7Srh7GJYhB9bWbg_YzxFXNwCwZmjB9O1v2ySK9FGe17Z0LT8XFriixDZcW6iNfyoDP2q2BcnsBGsZoTdBQWbwPwn6f2maYcLDwXZj4ADO9P2DSMSDyyC50gLC_q34XDuVzAMylSVUv246wN81DJNx_s_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25369" target="_blank">📅 18:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25368">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/En0_X5MH3YlPVJesQNMHnTf-07Wsd6QYaOTtDJV__MPI8uDCh7Kz3YeVQ2BJS-jPBxfinpeLcJJgVYz3Pyko3oEJN9SJaKmIfuvA2rRdC6KGX6yw4cpuRf50NwvrghdcqSsNBJ6riqQEIOPUBFzE-yszoFM9pe9W58eYYu7OgFqBEKHf0AL13eE9HQsS6QjkMJ9IMA-afaTMKXoUi3nraKoR9vhmYLyVJtGxacMcNGY40D8xvc7Yn7lHlPbfdIS60v2H-rmlEJs-wX9TGuvaO4UqTwFxqJK1t0mGzmT1pUlFa2wxHyUEPqwEySp4f0WpYEorRHnajeZ0sz4Qfi8qfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توماس‌توخل‌به‌بازیکنان تیمش گفته در هر زمانی نیاز به رابطه داشتن‌میتونن با پارتنراشون برقرار کنند که جود بلینگهام بیشترین رابطه رو این مدت با دوس دخترش داشته که باعث شده بلینگهام غبراق‌تر وارد زمین بشه و برای این تیم در جام جهانی بدرخشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25368" target="_blank">📅 18:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25367">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_y-xQXnHkcCQGHUndcyacerhoYQc8e-7B4b2ZGeBuxnD6Er--RNtoyOvSukSSOWZ4rxNKBnyTGWFYFsz22BfZ49Dcwq4b3mX204GtR5yP9qES6D0E_Re1BYztMk5ntqZGLT9hMl2vsvv5E8Q6J6o0xzM-E7sh-TbjLeWOTqjnxV6l80mWN5Ciumqhp7WoMpStUuLYm5YolFmLLQF4t6YuTNz6aykCQHnsIgZrdAhYP1gPbc2BxjlpGmduDfzvzfVazV-HQxrTZee0uj2xheN5DAnv0Hkd5NTX2vsus0BbXk7BshsaNe6_Cec5jZV-MMI8fhUb9vT5B_eGmkgyDxLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25367" target="_blank">📅 18:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25366">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5Ex2twCBwInOIutuOC_aeP0I9qCViSAHSF8Oh3UDnREb-59IQqsNBNq_BA75_v1fT8e8ivjGDIumHgoX_DgnMNpB5MSBi5m6GRb8WjczvUm99YgqtPRLNpE8td2MoIxYOYn1N_B5qsKSjw2-6wnmreU_8e5Nt77cnLspZlJ3B9axnAWBQPAhfWktHq1D-Q-TrEFCTxh1jwXl2PGbaBO4Gt9xkn_MbIekSTeS0tNCryX658y7yKzWd77fbo2BGV8V41ohDgeUSTR0r6pK_4eHW6MvuI4J6KmB4dCb3_gmWE8qT_Y7fVv2GaKvtYhPP3RZvWkYhYm57vYvHOxnuaizg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
به احتمال فراوان جام باشگاه‌های جهان 2029 درکشور قطر و فصل زمستون برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/25366" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25365">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUhH4iB6yOF05uRij1-sOF3K-GoTpN7TSex6xF5VCLPdcIU5WjFU3uEJxTI1NdrOU3xhsgkm_WD2alYSVDXR_AMn7ShZ0FPHSx4m2T2qhTMgIj8-d6a1VWKFs13gEpYdcjGb8pxOuS2G80556WtOQAopY4rnO4XOuiBkWrtaEIXKePJQhbXpeBpouBDFgWMzqcvn40cbNLMkJPApKFRYgleMrXbjFnQcrH7O0PxoI_-am56Ztrr_BinGyCXP7wc_TLqnPgSKQc9085a5m9zuzzrIbkBC43G84H9sNyGcGikqHcF3IDnW_LiibXUuEwv3X6RwrwBRr3ypU_zMGu6uoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعدِ بازی، امباپه بازوبند کاپیتانی رو از مانیان گرفت، بازوبندی که خودش بعد از مصدومیتش به اون داده بود؛ الکی نیست بهش میگن دیکتاتور.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25365" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25364">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xh1P5X_Zj6z1XRmOSfToMLLzbgtSjpw7gfjuqu6s_KN6d6j_aAmrBWAAPDh3nzw9chz4AE7C5OgrHTjkLqCXclKysmg4qVzxEzYbCVVGVk4-Q8n3-UtEOe5LWJLzQxjoLF-wSNE-SUgpNgIfs4GWluRgGioPW771XpaK9zwH_lMgqRvns6iUCuafvEsdNyKgd6-kTI1j8erRIRUMNtv498HRgSlKL76m8DBr_17C4vg7HjtxMXE9vnWjAfjvSj5sqwCC5m2qN9G9xvQY2IYs2CwHMj0OeAameZaG4fRrRdunG7mdAgsO4KJ_Auqj4P_feip2_kkRN_i69Isf5VJdrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25364" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25363">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pto2LfDc2qBOiOZGWsbvV6eP9c-iWZ0tChIV6sjDRmPz2rp20nlN3ENvUDP3i1mJtJIuZe4bqnjcejh4ZdlPK0bAM3r5zEVD0IOesNxGW1i6ulF5zRn7iCZs87_Ef80-70C5jh_QhepbhzCm3ktR_PsBFQxQ792dFqi6D9CwLLTYnkwZtD4_Kw5VmsqYUoGDQVf70m26GsU00GrXT4b6N6CnZu4mDjYldwOv_WVevu6-q5c5EJpvJYFyqePSFgbF8CN9Ml8Fdzu1eePAWSJkar59hcIDwDyWluuSxs53JgnInD42h_D98UavQ-KZahVMleGYEUlwADH4jwjiJN7Rtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#تکمیلی؛ فرداشب‌فرصت دوهفته‌ای باشگاه استقلال به‌محمد محبی به‌اتمام‌میرسه و این بازیکن درهفته پیش رو تصمیم‌نهایی خود را خواهد گرفت. تابه‌این‌لحظه آفر رسمی از باشگاه های خارجی برای ستاره تیم ملی در جام جهانی ارسال نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25363" target="_blank">📅 17:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25362">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2Zq1agiaS2V1N00AHWN4T5n3bQjBVyHGcD7a4-BLKkA7MPDbyG7sdL0UZGz--fFI4alxUx8Z0_jvrVQ_6E6OZ9VrqzUCDqfU4qT9izPRrVxMrD2a0k0rDWAsWc2GmbTEkXEI57Pjn4sybZky8jL7gAPm4LiKPXB9J99sgy3BvrhB8b8xwaTsshVYQXkj8RJOu-njn4jz3YOBELJ4tkVW5qyIJnSiPoyvrTMIWOX9TGu89ow7khyYJ5tb8OiYVgwtkBa14WYrMGcSjRxhfYXrGmxLR-sNdwM3A7N3f8tv_-y-dk5sAT82YT6OcsrXZGkip8UWn8ab664H87s5OEuJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇮🇷
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال امروزصبح باردیگرپیگیر جذب محمد محبی شده که این بازیکن ملی‌پوش از طریق مدیربرنامه‌اش به مدیریت‌آبی‌پوشان گفته‌بزودی‌برای‌انجام مذاکرات نهایی به‌ساختمان‌باشگاه خواهد رفت. محبی گفته اگه تا20 تیر آفری دریافت نکنه…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25362" target="_blank">📅 16:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25360">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXOqQklAJIop6XDLP9FlOFkgQwzFeHVyX0tLv8eXJF8loAeVCs5xqKHhGRDhbEmftP64Xt9bdwKxU0VgwM11PxMrL8xla8GygSIfllb5K1GILyTd-fGOqSuBHKr-vaYyNptwRqyJjRZp4pXLz9ONt5718tsgM3Z3kx4NAv5n2mA2a3vAtx3NyqBAr44Lskxm-2DBxOyqn2B_ujgdJE6myPPJJuxW7m8OxRZLDE831jNZpk-hcNlNENbmzdVaswG_06u5vkJr9URN98L1JhX32w_JCVk2xbBLSZvgMpWdSP26wNP0Lc6mYd9oppOKwblsvfEpzODjcLhFnx4uUNvMnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
مدیریت تیم استقلال بعد از این ایمیل وکیل ایتالیایی که امروز به‌باشگاه داد مذاکرات رسمی خود را با گزینه‌های مدنظر شروع کرده و با مسعود محبی مدافع میانی 21 ساله خیبر خرم‌اباد نیز وارد مذاکره شده تادرصورت توافق نهایی با او قرارداد امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25360" target="_blank">📅 16:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25359">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6zPI26e2tsOgMN_4hQiqZJubgKzzA_Iq293GlMGtWN0qqUhYU7hDROnFL5PJBIQ5sdLszifApmLspb8rV28SHXmRpBMyRG4m9xoVEEu9o9ntPF3AifwrRTscdPhvdQLdP0ALNztGLMxUfCitZ6Juqrkh2bqhyn0yop2-d_W3o_Zwyx_w9z1h6x-JUbuzU8hV-mEBPHki5OnDuBCEw_fwicXg94x5BraBoihfn9I0PZ-6NKs8anFxiPc7DH0slmIHajCxTD61etD1QEidWIi390wRuromZXvuYOGG-kshzJDpTGzOOkJRad3PM7d0Y1MiN0tJ2UH1NuZ7QGr-u6mQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی که در یک دوره جام جهانی +8 گل به ثمررسانده‌اند؛ امباپه و مسی به لیست اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25359" target="_blank">📅 16:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25358">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇵🇹
10سال‌پیش‌درچنین‌روزی
؛پرتغال‌باشکست دادن فرانسه میزبان تو بازی که رونالدو مصدوم و تعویض شد موفق شدن به اولین جام تاریخ خودش برسه.
🇵🇹
رونالدو درباره‌اون‌بازی‌تاریخی:اون‌روز با اختلاف بهترین روز زندگی من بود هیچ جام یا افتخاری برای من به اندازه یورو بردن با پرتغال ارزش نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25358" target="_blank">📅 15:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25357">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBjj2WgVFhXOZkrvKA9M0zNxcdU926_KJOcuqzv4NYuj_mBd_9fUqkEyUSWEEGTO7bhUynMdYAzNFdTud7WDNh0WDHp62TCH04K6C0BcQD6EC6GtwcCtRkOIwyKUy8eysooLD-NFAhRlMee3f6tkoSSz7_d45UBB2lmXAVwA50zDrgUCxYiveM9XNqOxR_s9oHGZiBiqomDmvgUEv-kuHOXNThDTiN_-bAIHblxGxHVJ2U9kiE68HUqkPQd4TgJonTXxztF_iG-X52r3Y7wFJyAWMJfBgpnaPzihDX3QrI2umHFXAT3KbIrk301bCmLQIQBDwyCLoFjeWoags8UGBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25357" target="_blank">📅 15:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25356">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=fQLrksOIE0M3IJw-o7Q_UM2n84C8-k6VW67zObdswVK0jDeePzpHEmMXOYU9kV71OkFsHM_IUv-RVnRrHBAQh-VQKdQTFFnKyi4FAlX1h70eKAr6gc8H92GZI-85tPPhvg7iJ-VlJHyXMArcn4OrEgZizuVcL-9CaTMsyirScTJ03pgptO-GwRaHXjJmKiznGKM_uGdHlwPvT13b6msIzTL_Z20V57uUnLb8ALBqCjSEllvBSEpewBVTmXfsAaUS6pT4RJUmR70cTgysJzvm2_xkXrrEAWa2n47M5Z4El-emZjG3eedYJsEOdjliJxO_DzICLxb8ll41mzu7NXFtsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=fQLrksOIE0M3IJw-o7Q_UM2n84C8-k6VW67zObdswVK0jDeePzpHEmMXOYU9kV71OkFsHM_IUv-RVnRrHBAQh-VQKdQTFFnKyi4FAlX1h70eKAr6gc8H92GZI-85tPPhvg7iJ-VlJHyXMArcn4OrEgZizuVcL-9CaTMsyirScTJ03pgptO-GwRaHXjJmKiznGKM_uGdHlwPvT13b6msIzTL_Z20V57uUnLb8ALBqCjSEllvBSEpewBVTmXfsAaUS6pT4RJUmR70cTgysJzvm2_xkXrrEAWa2n47M5Z4El-emZjG3eedYJsEOdjliJxO_DzICLxb8ll41mzu7NXFtsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
ویدیویی‌ازکریس‌رونالدو
🆚
لیونل‌مسی که به پر بازدیدترین ویدیو چندروزاخیر دراینستا تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25356" target="_blank">📅 15:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25355">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=tmz_8WzCAf9HLLfJheSrszeMFpobbwjebRqYHs9DuNLB_IBdei3P_VOGCWt0RZfAGT1RmYbAUdyHSGbP4lSJecxdfuFoo3-yqb6PsQTvQkeiqHDz0yk1xg6Na9bHhhUO2eelEvoEJXUllS__MzQtQ-iuSbK9lo74OKjxPVncSTSaf8Gp6DKndTrsBL57tAG1SMHwuBglWs3mJJ16z5ofNyj2z916otBXmAs-BI10SHa3Oh2U-EdQZEpcwmErzWRBq8rJVhKfQr90Wrz1UQd3rOms-Or__n1vOuf6-vALYrk_IiJFIy61xRjtx0RgAm-4DM5oegZ6YLyv0f16mOa0mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=tmz_8WzCAf9HLLfJheSrszeMFpobbwjebRqYHs9DuNLB_IBdei3P_VOGCWt0RZfAGT1RmYbAUdyHSGbP4lSJecxdfuFoo3-yqb6PsQTvQkeiqHDz0yk1xg6Na9bHhhUO2eelEvoEJXUllS__MzQtQ-iuSbK9lo74OKjxPVncSTSaf8Gp6DKndTrsBL57tAG1SMHwuBglWs3mJJ16z5ofNyj2z916otBXmAs-BI10SHa3Oh2U-EdQZEpcwmErzWRBq8rJVhKfQr90Wrz1UQd3rOms-Or__n1vOuf6-vALYrk_IiJFIy61xRjtx0RgAm-4DM5oegZ6YLyv0f16mOa0mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25355" target="_blank">📅 14:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25354">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoIZnC3ZZ6_F1rQ-r4CT84HAVdOZZj-7RCg6GtcFMdJ15gBZMt8vJFZCkifRuePJUoVOSsrd8-YrXB1um_dfvQoPVGr0NmOijzawEBZ4lwJoQFvhpGH004cFB_hITa0k8k4RNUB683ABCrHg0BZA8EDe4P7eSHOToYI_5SqTmFj8lChdQFjeL6wlDc3aR33ld1ZpUwzpU_TTDYj43jfjn9V0hCYJ5qTDF26z5nUBIvSJl313CO2G7xsRWzBAGPb8H07swBA6rGPJqSqqm0dQydU6k17Pgaa2nTNyIhxxaY1XuE1orKizvuWs0IUyAW3w2CpgwYIlyjZkOw_5H3w2Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
ابوالفضل‌جلالی‌مدافع‌سابق استقلال با عقد قرار دادی دو ساله رسما به باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25354" target="_blank">📅 14:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25353">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KScaszO5VLm9O7uVWCJph6l85Fgnb0OnbZCcdJ3BbqWOGnihoY9IrTMi78T-OuMaCTs49OY4WvljbGLx6zmhenpG0h4R0i6oQMBX0TRIAduLEPjVbWJ-R3RIaxiRUmVtNsUXHQyfyEDI2GURDkDIIrntRxJ5t8H5KtGYEw0SRrV-vtB7NM79RxOj_do-ZnD4uRVBPZ2U3HwDpWeVLJ7UcOyzjjXHej9j4Fo5cNhgqEXcZEnLLGepIr5BnnL2M9cje1S92WGVJOva_1_uIjnJZLAKDI2A0emWLRyORgCQXEsN1-wV4MAH44T4PBcq76KLbRMkeLJHjIDN4pssb5TMTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25353" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25352">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYv0rGXclodHeuUUZAs2tEqqiCicIYJt7_66v48bQdDVQVjiXOeN9lvq1oz8tRhnJCq1WXx8H6CplQM5Gt7D8d7X-e6opqTZvYV52sGcDGMmujr8ucbIlZWU4YR1EQxWeUv96EBKsB5kzI8FTxtXdy0VKEldWb6c4qIEl5KC2avvbWqrwMEN2J0cLaVoaZp1AQ7o6wj-Y_PiHlvTPm7LOVZmbXmDPw0-c2CByunmFuUp36OOBVwsPuZJtzg1f4PiPZKd0LKPEGnvxP0IVLnb_5tc3nlEJWqGgzzxwLTkTNlGyRJ-ziTgFXQJf1077H5DvbJawFC29SUml6c0WsAE2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
نماینده اوستون اورونوف به مدیریت باشگاه پرسپولیس اعلام کرده یا رقم قرارداد این بازیکن رو برای‌فصل‌جدید افزایش بدهید یا با فروش اورونوف موافقت کنید. مهدی تارتار هم در این باره به پیمان حدادی گفته اگه با ترابی ببندید مشکلی با فروش اوستون اورونوف ازبکستانی…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25352" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25351">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uh9gnDfUBnnBryVuzkmxQLuCbbxTof0LcagyboiqBf3qRSeSpGjPGJRbTcvuVVsEb9CFg8sBHP9yf_dRi3pdtktNv_sf_U3J7u_03fmcsi-LUZOQEERKneGzbHkIJhiA0CNcKhmCtshngcWPrclEC3yIVdFqavFzD3gKNFUMbc66OmycGyONOCnNIvnaJRXBAAsNzy0oME8MAvFxwo60IAD3n2CyLB9cYqPQqbtfEpdnyhaKQcOtf-xeyNN_NOaXj9rE7OlUwUKl4cZLyJgg-U0Sa6_dqb8DUeE-WXLcYe4ELAMadWK99EePOHIQ0QIYbRXsjDRSfnkvB2iyUQCLgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25351" target="_blank">📅 14:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25350">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3YLruSXhspkkKd16ZRz5eWQEoagXjqRhRqdEFegf7NdRapbHjTV1L7EOnQg9Ugf4l3xTQvoIlefVl0gx9THT72kfrE5WGg_Or0Us4VkFOxQDALB3ypMOYMuZhk80R5ZQhDaEy6EHHmIW-BH6A8w-oa-EewHmomvnCmNb4VU8uNa2u96igG1SxvBhc6rcSuPEUCTxTmKq3vq1ujObzX2oNNa81Bp8rFw4IIEIfyHlS0hsHQm_4RiHD9MZjE-r2QdtCSF0h2k6DH0s6yzsYGdmVLtFmd7-wBD75ba0yuJVxetaxgSP3A_qdrbOsIvaeel6bdGfj7sChx4rpNhngHaOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25350" target="_blank">📅 13:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25349">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9_WsaXd6szsc4279aOletGVRV6i4BSygxzwCt95YdbXeX36jXe_ChWWI62cLZLba6ABcnYBo0kuHPvAQ641c8_0FsXc4zLYCaVYjoYGwxizdE_HsxY0m73kAlUxpNsu03DrB_U-7wZwH09oCmHMfIHJKb26fXLWzdumec1KJjMZb7xoPV62j5mmAh8fAQVvRinEfcqEFGc4INrf7hXOjBE3a2RK65z7efaF03A7erMtvTdD3GuDDrtoM9q3dsjS1j3V_ZlEEIJBjQE216tl-5C1sZIqw8O7IZvxcE5y1Ekum15A_vJoWOLItioL7-knnM1BJw7YrFOqBArKqwlGiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25349" target="_blank">📅 13:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25348">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBodr33dD5nZT0B9LqlFoiCXEM_5z_Q-mUxt-XrjqrZf2ke_ne8tUuggKxiXsXpSP_ZJ-cEeqZgt0yPLK5InKF_YJtvuueXDeEPcnyB3ZG0Zm7jmvoShgYT53eaPRoGjmkz18TaaBmwhAdFlkqpSsGV0fGFZgKYOZYvNlf_6mffqV6-pt5CWFB7HuQ3L15c6kdYKkyZ4VeggH2o_d9bfRi6f7EM2145wxjYqghjTca_dpQ8kN4okl4PU1stQS23R8ndSA6zfl4IAHqqVQKVXKsfs25ktjItHM8f40s5GkgL1QNEfSWAr1yQen8XXoEJ9Agrn0-LWugLOTF4F6HtOZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25348" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25347">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m95AUHlFgZOx8Xp95qyYj3eMshwdDoYRczmFmbVzybsn9Z9w3M4Vjnydy6D84BDnFU3bznCKXgqMp-WNRCV5e9f3CMEx8kzc75ApZUJUDBS_zQeOtrxZjRVLK8eH-6L0SxGRWZgDrcDj2aCJvetfuc1_06elRwFssLgEc-SHkCPHxaUcPvb2Jlx8aomNcLU2Cl3ooc0LNjwhgliaBOc3O3FxkxPJi6TfA_w7fpgXUyuIyEMkMh1uKcxD3cC-XWBFU3U0XdL3PhTP2Ygy0f_snvxfx0KkTERF_rHzUoA4iBW_-8Xbj6cMBXd-ShQox3pAo34Tm8JNPvcZBeWng5rzEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره استقلال ازباشگاه الشارجه امارات که سرمربی‌آن‌مورایس‌است پیشنهاد دریافت کرده اما به مدیریت باشگاه استقلال اعلام کرده درصورتیکه کادر فنی آبی‌پوشان به‌سبک‌بازی او اعتقاد داشته باشند به قراردادش با آبی‌ها…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25347" target="_blank">📅 12:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25346">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">📱
اینستاگرام دراقدامی‌عجیب، قابلیتی اضافه کرده که با آن بقیه می‌توانند از عکس‌های شما برای ساخت تصاویر هوش مصنوعی استفاده کنند! اگر اکانت شما پابلیکه این قابلیت هم به‌صورت پیش‌فرض فعاله؛ به این‌صورت آن را خاموش کنید که مشکلی پیش نیاد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25346" target="_blank">📅 12:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25345">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1uu-1nxePqi5m66w9NHpIO9AqLFKtjpTczU_4ueQ2skmizjkdz7Mah8aBrzj4VwPCxyANfgIt54elXNiWHQ7Izvd-5Vm1dr_6_fwwxjFGzokUCSyiaI-kUWXWVv2x5CpRdgDLq3u77dwUWJGEyC0dHi2_Onhrv2egKgPK_tOXL7EtsbbWLDc6i6OYsR7UV2zcgbo5ZJUWdb7soc6F_Dqna0JlhiRAXfwQfUh9ans6AaiIFOy93gsHlMWYh9HQE5-jlyK2XYvVpeUzZxvRBNYqpnnPkfB4A94TQoGppIRYD4OXx3QIRlZoV61mxInnPjxnrdkdikJ0XlkvfV4ko4zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25345" target="_blank">📅 12:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25344">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJc1L9TauCRf0RwaxnEkEKbxAq3mO5J27TiVPl6wCSHafBJgxcx4mUWiKRTrjJIaEfHucNSf16uZ77BuP2mckey7SJm3Vje_r3lQxs8OGqrQvjpXZW2X4_Q3OAQBh-ohVWGXYP92pmo5Vgi6wB6JGKTzQlexBGDK5uT5kTUjfpSv9u8RMpHGapoyqSPg1gYYCERzX9sj5t9uJKIPO7sP_woA55CW4nNrG8_1-jKg3KsfGiTPvRtdyKLNsJI63hBKjVx3WpL0xqwWcgp3PPb97fRIIwzkcgD9tScnXc3lQEW34wvc5setHbJvJsSPc8Om3yRRauyxOyVMP880CIC2Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25344" target="_blank">📅 12:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25343">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c669eea570.mp4?token=PfMqKS_QXS_mOvUnlb82JIVoHgJ86ZvE7WJI3uTBEePpfVIAWR2fYZNsx4o2E8oW1tSMdapA4sXMDspqsM1C2NGDEe0NEtzONsCBnXaR3JbGvPgpsBLUnbz5OfNb8sdwS2rHdg3Kj-NiRy1NhBN951N9FJvTO8yw_QxNUGxBA9o2dQbGVp_Dh0HjSZq32wtBmBZ2gSUP3QmajjlcZQZ5BmM8m8_FJyS5QfDN5FxK2x33vv8dq3XfLFhgAv-dwKk0H4ZgkyZnHFBy5DJEAn7rDSLuBRkdszjyrzlC5F5KAxYPcPijQnyQgQTr_ERh2RPn496ayovIuZeEt6DIOVzLAWek33BsNIAjhba07kjnpyZiZ24VPfQhKzMQFdWqYt1YtxpV9PGNuhQtwnM3N0hwF94WYzkmGcHytf1MSlusCJ5EJA7vO1es1P1csHRrlM7CdTrTIkAcnuKiGIp_gyPzCL7HohoCz0mm3WrjR7-ngaX9mCCk5WaAntuN2n0qWSIBWo9GWCXF7Vnwuwhhqi9WHc6mVeBcDFbBGLS8NtcTC3l4zqxJqRdKecKf03DKRGbyQqioMgsAWZ44rjvrzYZKkfUh_m_4p5XREMWILntLK9g8LdhpSFQHuOCwDU2wedpAB9okC4PK8Hhctb5etO3orovIE0WtxgBj_AGT4MMZLyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c669eea570.mp4?token=PfMqKS_QXS_mOvUnlb82JIVoHgJ86ZvE7WJI3uTBEePpfVIAWR2fYZNsx4o2E8oW1tSMdapA4sXMDspqsM1C2NGDEe0NEtzONsCBnXaR3JbGvPgpsBLUnbz5OfNb8sdwS2rHdg3Kj-NiRy1NhBN951N9FJvTO8yw_QxNUGxBA9o2dQbGVp_Dh0HjSZq32wtBmBZ2gSUP3QmajjlcZQZ5BmM8m8_FJyS5QfDN5FxK2x33vv8dq3XfLFhgAv-dwKk0H4ZgkyZnHFBy5DJEAn7rDSLuBRkdszjyrzlC5F5KAxYPcPijQnyQgQTr_ERh2RPn496ayovIuZeEt6DIOVzLAWek33BsNIAjhba07kjnpyZiZ24VPfQhKzMQFdWqYt1YtxpV9PGNuhQtwnM3N0hwF94WYzkmGcHytf1MSlusCJ5EJA7vO1es1P1csHRrlM7CdTrTIkAcnuKiGIp_gyPzCL7HohoCz0mm3WrjR7-ngaX9mCCk5WaAntuN2n0qWSIBWo9GWCXF7Vnwuwhhqi9WHc6mVeBcDFbBGLS8NtcTC3l4zqxJqRdKecKf03DKRGbyQqioMgsAWZ44rjvrzYZKkfUh_m_4p5XREMWILntLK9g8LdhpSFQHuOCwDU2wedpAB9okC4PK8Hhctb5etO3orovIE0WtxgBj_AGT4MMZLyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوهی‌های‌بامزه هاشم‌بیگ‌زاده با حسین ماهینی دو مدافع‌چپ و راست سابق استقلال و پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25343" target="_blank">📅 11:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25342">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgIdha440K396-p_Gtj1BslNGQDJpORN74wf5oMCnjh-CO26xfvUAZMEcqhpEqQmIvpX9QuiY3BPy1p2koeHkujbAqMWgfFqkNBD9JyDq7b3eWGXZY4fJLVAZY5-WUOz-HT1GqhEdypcBe8-73-Ae6JX-xUXtZl8RGTWT-dOuToWCnIP6i3SnXc6-jxe_h-IAeL6noU1AtN9EG1pQVAEQdsO1B6q9_YfBjLYgPvybasA8VgA0qS_qj79RFrj0OeOfmEU0Oj_SaBG4DJS_SW1qwTzVTP2ia387HJan6NVO5czgnx5i9sEcTPyihcD-Lb2rVVCaHRN4D4CkWpPHd-EPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25342" target="_blank">📅 10:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25340">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryfopupo7DmWg2lwFT1stkMPiGPAaB244gH65aL1W7p0sb-hc0ytAdXEdfgM_ChXufVH6Ub8tLWwG_mlaTB3qfjS0-OK4zMRZof7-5j8B40LznTon1bvzCYbZ7DcBvP1GHWkbsIr4o8Yh0ls0hLXpQmIX9sN3l5Yd4WeFAZZbU_AxnNuGL43H7aBWhcNGgvDN1TUlCascOM7vBL7XwJTjCX1GdXW7RS1fmXnYJWqf_-eNBomDhxxJ7L7TsZhKVrc1UgCqJzPWHMyKM6meZuvdtehFNydTWmrhjb3bhtKjk45clr16oXeM9jFI6QUw9yGFO2nvXAFh2GmqYiAJIOiKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی جدید پرسپولیس بعداز منصرف کردن پوریا شهرآبادی برای‌رفتن‌به استقلال؛ ساعتی قبل با دانیال ایری مدافع 22 ساله تیم نساجی تلفنی صحبت کرده و از او خواسته بافشار به‌مدیران نساجی کمک کنه تا رضایت نامه اش رو صادر کنند…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25340" target="_blank">📅 10:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25339">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uG0L5420qL0AMB9Oms3VekQiS57Pg5KpAEm_qVEGd6UBoWRA9W69HW_yIONMjHa3GTZhjY1x5iWTKobJ9FldyUJKbubglQVwnLwu7ynJ3fFDQASFw79LTyTcEDtrUN0iP6wBx9oCv_pNb1qqrdyRNTInzVz_-MrxshRDqSWzvtUeni-wS1JuDUlj-LLd4ZIzwUeHQhlzsKW22a4jCBL-k54moRPMq9U-H4VugdW_Ntup3wvSJyYobjfWJ2yjXDcHx4tAHXXB5ENvuMw1lWyUigVIDsoytRjPeuCw5QdzWc77XayEdxQRmPvosgxjKsxlMuoqFYy5m7XL1PteuO2qjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«وزینا»همبازی مسی میشود؟ براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25339" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25338">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45277758ee.mp4?token=ocp34WYazyKUpOGv6_qc6_WcmH2TxyQAhqkIH7lxmKUgrRj9TVeW4yqk7JQrLXLbYSVNEFD7tcGPIoxz31t2bfvo-elrsgapj6igwWkBkJe0WOeTDeL67mwuujSdCtro1dtND_fhrTbtI6uLXba8twJOQsfbrZG2lu6hHX8gvjnQLjDKZLV4FaFzhZSJC6abuPX66-f41RKqCAPuJMw-AG5xkuQoumMGheq0q63G7-E1VucCuSKPNau_AuJwv1jpLQHxRJQLrrCp0a4vjs-iQoVrpwuttJp-tpg10FSW654k_GrkbbM8UofCsVLNA3YBDkKMbwuAvliwnXDxD5dPoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45277758ee.mp4?token=ocp34WYazyKUpOGv6_qc6_WcmH2TxyQAhqkIH7lxmKUgrRj9TVeW4yqk7JQrLXLbYSVNEFD7tcGPIoxz31t2bfvo-elrsgapj6igwWkBkJe0WOeTDeL67mwuujSdCtro1dtND_fhrTbtI6uLXba8twJOQsfbrZG2lu6hHX8gvjnQLjDKZLV4FaFzhZSJC6abuPX66-f41RKqCAPuJMw-AG5xkuQoumMGheq0q63G7-E1VucCuSKPNau_AuJwv1jpLQHxRJQLrrCp0a4vjs-iQoVrpwuttJp-tpg10FSW654k_GrkbbM8UofCsVLNA3YBDkKMbwuAvliwnXDxD5dPoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه نویی بعد از دیدار برابر مصر: خدا سر ناسازگاری با ما داره. شایدم خدا داره من رو می‌کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25338" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25337">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbAIdN4jdXNzI5FS_XRJQL4RLJ5jcLRvkdGOj_Z3cNsjH5fBy73hKvbNryeUNiHAQ3KOcicavSMfeDJZEqFNGFwgc4-QiMqeLeMUbv9xLRBO11kLS2-6Q6i86HZ7dbX9Issls4LymFTiy6eL_xdJBRazb-OIYZ3jRBvs2cJxwAX6bKsXA3YJAb6JKITer2y7ox4H5c0ZhTIRKpYlhpayYS6fubmDJXyiLJBqMvO_JJfUCCYtMWf464nYt2pnMmc9voQPfMQxzT6UzhnpduqS6zN4rXQ90W4DAHmr4y37CgdmnAj6HKsZJpqX8Mo71eWyr1cHV0ao4p7I0FK4_MjFHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25337" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25336">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mp0z4hNzFBqKxHcRYxXm2LhX5q5DitzV3q91WK-nhd1JhAc7mLl6IWl8xMCd163Kbj1mbQM6RAKnCzv1qljGxfHUGTAL4vUBioIGHcHPDKytLX0c4cD_aD0T4LNrRA2tHyxoCMwujVRiM6jLPye04q4DVWZyLNwUeX6kY-RefqlQ1haihW0ejG1v22zTkrdmAbNPLUqD91-5FHzzxOXRyBQU3DCmgsKq7oKDQlPkmMINJm-zrCQA2VuoQQzMY1o47fPczm93UaOsU0mOYs2tO4j-3zYnbKLLwbRwKAvg0wCHCFA_q5lz3rqvBpzXkHKXquwLWxyxpAUx9uzWqoqH4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دوستان میگن امکان داره مشکل سربازی مهدی ترابی برطرف شود؟ باتوجه به عقاید او و همسویی‌اش‌بااین‌نظام بله یه تبصره‌ای همچون تمدید معافیت تحصیلی پیدا میشه و خدمت سربازی او تا یه مدتی به تعویق خواهد افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25336" target="_blank">📅 10:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25335">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cE6yW2pbC4kIaYjEltvu8MWM1LXutW3u0vJUvkMKhNH9A5qJ2gfbiKTcHaBE5NYSJ1l7XlOy5UfVbBPwyDHqXdJdxNFroHSeDv7z2HrvBPPuOOpP--2Z98SxClPOJ_-qRJs3LfUwO-fwagLDox5zHpb7s5edLFuPx26XIRjozuABEptHTQYmWdrUnhU4hwj8KnZbrHdo4hbbE0MsixFMkOB2z9nEOx7ApUg0XdmXvoWBXO3YzSlIo8o3d6uQ-sNrsffif7-s_wlTDG198NTAwcUcOCpHKoVmxgQlhK3p5p4Ys3VQqiXzHwG11yVSyNESv-yL7x58ic1XJXb3cTsPhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
ابوالفضل بابایی و سروش رفیعی دو بازیکن دیگری هستند که بااعلام‌رسمی مدیربرنامه‌هاشون در ترانسفر مارکت از جمع سرخپوشان جدا شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25335" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25334">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgAlPsuvJy_ZbNKfS0a9fDzZ_MncHotQwc3OiTdx9Y9WxJts-DHa8PGccglCc3nhO4_doYOKBiwPG0uSaDrdLg2djVN9ArVZfZYjIwvicyf9OjITdzncpt2jj6-hmbcryoO96dQLoHniEb5PId_2Hlqp9KX0-nOKOaORfVSXq0C_-nTSRG5Eus_Ef4tPFVX0cm8K7ohWXVI1UqdssovDK3WPncY9EvOosWjdxhllVdAR_7php9YZm99bDTNn8poAglMtVquEZCB5rOqd_xyuZ6lekCQSVfZWNyBNbCmCzSwxM2g9spdT_LMvHD8h_OVm4DCUejMpYOp4EdbwrKYy2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25334" target="_blank">📅 08:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25333">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oe4Fzx8U_22_ARScIsQf9sE5EmErv8jR2nZKNlG-LIuJywA0ogeO9BVumDaAB1iDqy-qAHdu9pAGqVacoaoAcAnwv8rd8SiguhDhpXux9RjaPvmPNaZpq7ZxMe3337VcsKS7HLdShqb-dgu_bc-E-YNQotvo6nMU3yVmUNzc4OCGa6jQmnxpuKVzr2UYIQixIk4XLSFqwLYDNqosP_IITU4IxM9l5hR4Tcya0cvDyu3zS6J-8Nu8d6Ag3_0V6LjIUavjro50bJttMrBrvT8-XzixIKAZ1BS43-mwbmS8JYvjbH474OOneIbNM_lTQpc9U8Gx9MDtvn2cZZBg8MevrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25333" target="_blank">📅 08:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25331">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JkeFyNx24sfM3lBCTttguVIG3TWfzkUGQH8_KnXC0M54W2lOx-gZNhRgFstu4ni5TWXoVmdS7G_FWR42XF8XD6kd-kzy2_EnJwHZI4_2YeFaepie1u-bscesy21lsYOWeUZ6bRQS8ZKFSYdMbHo7HXhe-S9eh5jwBxr0nEjQ8Vo9BTPEHuL23tYnsp7jOmVTzNcg4229baulmpwc6apB_KT5QXYZUS-acsxstRr_z955urCX_J6pP4ztxTz1_Xnrt-GHCkq_rMwLHqOttABNpQD_o-qrqk8pkMrqDYGnKKTG5ggt_QcXol9FKFnIiEqQdYi16iEKIMT8NrWNPpNO1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CPuXZuePUJBetDGiIGL34fvTbbV354lXNFWKj9YKS7dh3KFjDRh84DQGd-zOk2IX5SKf17lklsf4dZpJ4syFxx2o9OXEQhLkVTxKigIOH7tzO4aZQE06I_eGl3y15NVuIxS9whl17PaO6Q8uF1osJQIEXl5HnEJ8TBapjExWTRQCoOBlDkpViZvMQDXKDP-s-7fiGWw78kMDX3q6XgZTTrqrHpxR4bQSWF2IStCNhcqWyed5cH7Yy-IkffnzfOmozoOTrHGcKgyA5K9-5zEBqZUiv1PXzXDAuFVmC1Xc8IdlEXQYKhpk60ShTVhyDAbHHpg8S9vqGM7iiDs8RPjg3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم؛ 10 سال پیش درچنین شبی؛ تیم ملی پرتغال با کاپیتانی کریس رونالدو به اولین قهرمانی خود در رقابت‌های یورو 2016 شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25331" target="_blank">📅 02:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25329">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uBPkXC-LHBsfxKwT8-ujkv2wu2sJptoAnnckEMSlNwrc7_sdhGSbdLQ6DNA6ULcH0XTI4K47P_Cze4lnnBT1RrjppMFGyb1Be5rhy_PxdZ0lNdW3AHkebF6vy1B8PJZtama7DNcLtDRq2YTiAc_4BLH6TWpPicc-vK6i7S4I-F0ZseNjMnl-lwRjhvJhf2OL9q3QTDab1WNsZpab23R7U06gG_3PHeRYBAUEGpVlAgd0xRrDnbvDDYu7p2XWcoefHlCYhuCpn-5cfIliCkp3LIu2hC5Wjvqc3-dR8VSYKhzLiYsGfMjVyKe4XdbIULR_6Zk9tVHZ00CSpwzk0da1TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J-ACoTkf3fhFWDITlCigymQKY6VidgLuHQwdPI6JogsVOICYfy6iOTTHWXt_MmXwOG3u_3J8XBvuVCUrKsYIG2Je8lYDcErWOgs6bX9nnBWn6tjCe4NU041oCS-I6rpEz2ikQbh7rRn4nX2wyemIqoChPDl7E7XoqPUrNHjTEzlqtTP9FyQq-R4r2GGTTruuhwKYTIGbbZUTwzKEiHctVianWlvsfuuqcnX3R6nBn8oEpDll-k3shedRJQXelWWTGagfUwwb3g7Cu94e8vXfKmfInwyZoQKZjek9R8K9iarWAMVn45LTRe-K4BScELgb70YHeprXt57Wk70tSgRkeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی‌زیباوالبته تلخ در وصف کریستیانو رونالدو کاپیتان پرتغال بعد از حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25329" target="_blank">📅 02:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25328">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWCB-8R6qM6jftfab2zdDIZgBMFhnh3eBlgaeX5gNWIUHh-6kBA_P0k379i1cKyRCzRAUeLlWqhsLjECQ1dMblvQot44fXCtp65qxHp3DKP2QXfwPYmbGmX1Nl7rSwuCIqg84D5_ARMsrDfUibU_wkPOtE0OIArfK0eHXuUS2yaB3BDrp0BH7hpnK-KLnneFOlhPqakQgXbAENscxFK7ZGxxSlR6EiEGNeAKFFKgXKTnZJ_6jSMJaiXreTErcRKoeVHvzj0CwHLx31tjNt9lbBhVjThAry--e8j9cOkoPQsFP_cRsrQIUHqyPZTwkHAvnnLc7d9e82FSJy194vwrqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25328" target="_blank">📅 02:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25327">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIth2RqfprBLubFANR9fCBSDScuj8xcelnRxUMogwQs52DBKoNSDNtFEZpRSbnroHdwFmrm8QvNT5JWKs4QyKLlr4uJoujih9AVQOXEHF2eul6ywvEXWk5VL_0lAgOf-hGtMYFfgKZoi6554phfYygbzOF0yFGCYgM7Ng_o_l5RjwSC-wfcAdYLeyUBIarHCyWZyAjGNMQ2bnvQl_9g7Zw8XeLaRtwBuqhsouGRqyzYsLAjFVVZ-LXRAdIFOqQpL8r6jzROPPmYk9QR_y6iGQKbZ2BG-G05iya7y5OuhV_s_Z4SzXasmSlqtXkEVAIhMa55cQ5N6j4HFlO6DXccz3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25327" target="_blank">📅 02:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25326">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGoFPKZaqyRRSZ7r9bujVTh9k69m6CXTgZzabW6gRL-sk-qvFQz5y3g5SSEUWAYuZ_Zpm_8LtZq2p7DydhgVw4u9y6-H2DugWhy_SShdk83FaVSlNzLG2Zd3cV2494KyY-kfewb6aQReFWcaoqn9Cdu_RGu6ytOuYGZD-HSt2ACnXYQTkSdiSXkhmpPCI7yvB3qBALYc4zLRvig_Zzd_ypIsPUR9NTraO2ugX5x9qPoM3F1ovsPB4vr3AwvkM_Z56L1jO9HCCA101M4lQNXKOQ0AqQLcDZ48IAP9_TKNpzK9ktyxEV0fNEvOQeSeit8RVS8oyQ-BaDan8aCbXnUP0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25326" target="_blank">📅 02:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25324">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WAcWExmzhDKivdcvWwkGMq3_D1Ld2_FHUjR4dpX0QovlX8-N0Xok2MfjZh9c5rzZZdtwtFequheUeq3cJ-NbghuaFnYf3pKlMcN_CukFttStIm5_3B1Pv8aXp5GMoB2hMlyh9MYj9XDJHzjsQsH4xsFkDercXC09I4fkvjQSPzPW-ihu3p3cSnYiKY7u2R6p39U3dgBXe-8SEHRoX4F-K5l029-jv4gq2jFTbgNyLtei3VVwLXHw8K2KflIH2ZVZiNf3CT0__RJTpCuyffK8hMi31fUDs9WEm_MkAuYanSzFwgDzZz76mGVm9NqRl2mkjPx2o0uu_ihShXaWM-Wf7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mE5alZ-Z3uZnM_BQoZPWJ3HXHQnZqkFx8OfAwshp_2ogoGUgT6EbFR-p3lW-R9YIZy7uV7mEuWS7eLow-A6ZWfJHfskTBukpcTJP2FhR-iHMwnlztIwQNU9qEnBvljrrD4qc4AGKW1rP6TlN2hNNK6mSXDxaBZCE6JQ3XwOCL0HpbFpSZtVHXITnRJttaKX-EVVqQ-OxAJh3nodHPJ6a9A-5K_cM7uZL8Cw_w7H98Pb5QWyq9_5MHQ4q2-vN3IX8bdPmURZouyknFbZCk9_yFvGd5OrH_aeTKKwBr1EOiGTlg5140qj07kwe0-XlPioQcFYrzlprxT2MTUoK31rglA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25324" target="_blank">📅 01:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25323">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLkR-z0YygoluIuZl-EhRDM-T518iMMKkhm6jVDiRcTZlFD053LTh7YVw41QHHe7I-DpwzZpoeDOVC1qop50fzeK-rMAKaApA1E65HPtw1V2qac0KrM4Z8mAP6T2J9EhgPkhJXhgSDifdJLrnc5UyJyTv-KavZ3H2gzwoG7xiibWBb7BPRktL0Gn67j6Zb4IO_ny9GS92c1dWFCmeeVfcshE9EASupSUSRNxicuHgGqadIetS-IBXseuoPAwwFBpBDYq4hwpR33UUw_E-nYVrRRePlIznwGqRX0VnnY-vhxQu067dVia3TlLdGFNGcgVNvLYFha-jSAuCvsBu31TdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
جدال‌اسپانیایی‌ها با یاران دی‌بروینه برای رسیدن به فرانسه در نیمه‌نهایی جام‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25323" target="_blank">📅 01:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25322">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsGSZyQasClWfM0eBziWxsUhZTAfKKZZfXMn7fXTl91MOPAmWpQdzee_YqdZnoPIyZcNfEc_i5Zi6vlZ3aXWvC87Yd4ZjdeyckEtadLf0ie2RYGRDIHaKE-SCk-jndrSAiUrWP4si74XeoYEdLaxYJsvT-xg7ftSIvPmK9rpC9lFDi29O3c-7tflPmKu_OH-lR6quPwhwxL5yUBxsXEfqcc0M6jmrgFPTiF-lN6Bh_nGLh1nwombE8k3mq8PQLMU-QpCIH7JpEgtGW8ypAdM1A7dudc4MxY-ymz8MHP_qUaNz8ShSRAWADAw1GRzsFpRAQTDatgclZPAM-qgCAJyjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
برتری شاگردان دشان مقابل مراکش با درخشش همیشگی کیلیان امباپه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25322" target="_blank">📅 01:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25321">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3KR5xkifSHfJ2X29Xj440PmO7mh6Ry3nXxMD8jYE76La2-MBJ3IrAkKURJquXkkdFXnGq-SzauoIV__rUSisuVFF559Bw-OuQkHVVjflEZAObewdxHUfwnZDiqEBRkhtjPrJ8BTirQcLtSaawulKx3UctPzlRybTMt_lixZamuoN3kYegCOCaB14ulIlabziHxhP5PrZAE1Sg4J9pXqH-tKmtbdsATIjENbxFU3t0rq8E-VZp9c42h1_yfeb0NVg0FFYns3LDYHAHRtajNsnovEhKDrXmW3y0O56-zavRbU97ItdjQzw0126yZt0rdkAeZ8YnC_ZzJoQm4yeHv9OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ مدیریت باشگاه پرسپولیس بعد از عقد قرارداد با ابوالفضل جلالی و پوریا شهر آبادی از آن‌ها خواسته هیچ مصاحب‌ای مبنی بر عقد قرارداد قطعی باسرخپوشان دررسانه‌ها نداشته باشند تا زمان انتشار پوسترشون‌توسط باشگاه؛ بخش رسانه ای هم پوستر رو اماده کرده و بزودی…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25321" target="_blank">📅 01:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25320">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7vTqj5fvBoULGZADxEHcZh2GbmWXFLUPqBAQL5t1RBtXmGyszi7H8kXrat2DGDB52vXNOG8lPvsyGpnvmZ4Ups7KxFb5lVs8SgTPKQDEFV3BraUayTCpMnjtWY4rrmbuz0WGrzQLV8VZtzZ6VeEyeZ7jUs2h95HWetab37zVr9mmNxSoeUtkwjMYO8FeExiZ5ThplgsxcqcHF6UvPI-jTo-orbd0CHY84HsiNEpdjg3T8RqxSbVoVmX-jSc93rA6G3hIABH2fsjFkCp4wR6i9Ur76qNNkd1fG-yMAcJioSmO4Hqr9tOyPN7Omv_f2vNbpGdcu5rYiY9H9RI6Pq9Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25320" target="_blank">📅 01:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25319">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMv-gMZOjkj-eIW8hEVdUQ-s2_gpA1uNtMqVEr2MuGGxq6DxzwyiYT-uOo2b4ZzmpycBgMEeZXD17BGuH9R1EZ-0vtjClnueZm_BV1pw5Uy6OOUJI-hHXhFKbHwICZSt5qJHXqJltrmJrrlNlQjVZD7prPXf3sSh0esCm5ef0OkrBD7gU-1CYQJEb2EuSR9JeH76sowFX2xX18bm0-lzj_ZaKMXk4apLdhXVjEhcafu5mo1FmM5E7XImql8SgXsk3rMj7uwmx7I1fHNzL4aa3uB-yOmzUBgZnZc0rKfs1kFD2oH1eMJMx0t1FYfRTtOEXsYCdTJ27T_Z5RH9REx8Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25319" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25318">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2548666d77.mp4?token=nJfmeyoUqnFf8q7apylGDRf4Yu9w_BjNUsy9iRnxuKZW_4prrBESBa8reO2-HWwYObsQh1GcI3zb5-WM2oRmeHs292swwmQ3Kpz1AhQZmon5bIu8s_JPsLehuTGLRy2RHhfT74u7eO8jCcrcr46uhAbd1FD5O1oyQNSBno8m7OHdZgfFHVCCJOp4Ci4u8V5aQG-nozm8k2tfiuF6AtXUdKfIP8Rx66l8Y-KAjtLtqg2TWqc1qUWMKvlKsJoAyR_qcaSfVik3pX8K7GBqTvvzGqkJE9reRKsvmLi5LgN3Wsvg-YroL5MPTfE7MuF7iurdzXvgr0F-z0XfATQNjLpgPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2548666d77.mp4?token=nJfmeyoUqnFf8q7apylGDRf4Yu9w_BjNUsy9iRnxuKZW_4prrBESBa8reO2-HWwYObsQh1GcI3zb5-WM2oRmeHs292swwmQ3Kpz1AhQZmon5bIu8s_JPsLehuTGLRy2RHhfT74u7eO8jCcrcr46uhAbd1FD5O1oyQNSBno8m7OHdZgfFHVCCJOp4Ci4u8V5aQG-nozm8k2tfiuF6AtXUdKfIP8Rx66l8Y-KAjtLtqg2TWqc1qUWMKvlKsJoAyR_qcaSfVik3pX8K7GBqTvvzGqkJE9reRKsvmLi5LgN3Wsvg-YroL5MPTfE7MuF7iurdzXvgr0F-z0XfATQNjLpgPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
شما حتی خارج از زمین‌بازی‌هم لایق احترام هستی آقای کریس رونالدو؛ شخصیت بینظیر و قلب بزرگی که داری رو هرگز فراموش نخواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25318" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25316">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f822cfdb19.mp4?token=abZhRVl1_tUS2Jy6WrFtSiNgsUM10xLCczW_9N-cewNogte8y8Rsu9pmtbgTGSfuiC2YNo5VUh5AQp5mg7rKVGX55nkl2V4a-ZzSqkKlpYw0Udt9EVSLaxWwvegTu_mORGTROpqwPt2nF6kYn9RpQCEJUiujRpA7V0orJoPeIjghlLs62b-U1njkLQUWuCrzP-T5U0kBVJuGuQtJ9ZbVVFBcIVvm1cuiKmR8nDcXeLgVDrmvxmjiClkaUXu0GdtDlWivGyEWDjo7MMAB2XgnnV6g3XoF4lI1OSyzb3KB71xH7Gtk33Jf3veBN4nxP2Qa62EW1KObP-kMOELSliPS0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f822cfdb19.mp4?token=abZhRVl1_tUS2Jy6WrFtSiNgsUM10xLCczW_9N-cewNogte8y8Rsu9pmtbgTGSfuiC2YNo5VUh5AQp5mg7rKVGX55nkl2V4a-ZzSqkKlpYw0Udt9EVSLaxWwvegTu_mORGTROpqwPt2nF6kYn9RpQCEJUiujRpA7V0orJoPeIjghlLs62b-U1njkLQUWuCrzP-T5U0kBVJuGuQtJ9ZbVVFBcIVvm1cuiKmR8nDcXeLgVDrmvxmjiClkaUXu0GdtDlWivGyEWDjo7MMAB2XgnnV6g3XoF4lI1OSyzb3KB71xH7Gtk33Jf3veBN4nxP2Qa62EW1KObP-kMOELSliPS0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25316" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25315">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c42773d2.mp4?token=ZfEdSoUi27nIeki-WZKU8xeb7TdoNA9sVp08ylCMZjrltE9Adjp3kiV7IMBEeKoNTBu7ftGVo82-B4IpnE5mjfgjpnD595KV0wIHZU1rs-lr1jYlxf8q1iW6C9QK_QAUqAu9t4oXC5lZH1f5b1BTujI6TofXP9XVS0j9UdZTgtdK2ew5aT1StMBz9FeIil2ZlpqQEy2o3hPEyCPJRawgxDdCO7LNoXi5HBDk1fdZFHXLdKu8sd5ektMFJsm1PpgQN16fj4wSShNGqqPBlQ1EIrUq0Z9q5QJrRlx4AoJlPxi2MxgrUZh5t3VLigNr57ZqWGZ-R9xPGQCdn55C0d1QaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c42773d2.mp4?token=ZfEdSoUi27nIeki-WZKU8xeb7TdoNA9sVp08ylCMZjrltE9Adjp3kiV7IMBEeKoNTBu7ftGVo82-B4IpnE5mjfgjpnD595KV0wIHZU1rs-lr1jYlxf8q1iW6C9QK_QAUqAu9t4oXC5lZH1f5b1BTujI6TofXP9XVS0j9UdZTgtdK2ew5aT1StMBz9FeIil2ZlpqQEy2o3hPEyCPJRawgxDdCO7LNoXi5HBDk1fdZFHXLdKu8sd5ektMFJsm1PpgQN16fj4wSShNGqqPBlQ1EIrUq0Z9q5QJrRlx4AoJlPxi2MxgrUZh5t3VLigNr57ZqWGZ-R9xPGQCdn55C0d1QaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25315" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25314">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLrNk1p0MmFQxVPW5fBxZJxvpKmk3uiEjI0rp43SOsBGRr5map-HcYvf-Nd-tQpUiIBzKkaMjRQWcWyQwfAZgvwgBPS2lPZ3IJseDYzWBhu-K6N0BByNPN6_evDK2n0oVvEd497xOV9AM34Cp5dyUuKSVjq49gJpf-wljMsx5FJMjs88ZtdVm1DF6NKAQpVulp_i8o5HSagUo5DvXgFlCCS0HvDDD-5khQIvbugz09-GJNVVDJDFVLfBqvDYo0LLvGW6tw7QHI9jOESNBuDO0bS_x_-qm1Pfj97DFupcwzHoKkLqD3xtz0YLQhqkdcHQZj9atmv9MDQ3LiF4DUvaOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25314" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25312">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfOCQZ6MAYpTmXME_Z8qjJ-rRr7m0bRyFHlsrTbXSymoM1i3zpXLWpSpkSMSlvjtyokh5Y67Wa27A3aqGAFPdnhIHin1LSSbPROcOBoKR24exJJv4L9tgLRQKab3_L60vflKJ34ziVrj_6E4aqUCHAE2OOiBzNflQcbV6L5a2hdA9HscaJizcNOO30x91eDWRO3hqvG83JNfqi7hKrpfX1ejN_28whWylmtiMdgcQdst8WZ_ub5agnp4d-lVIJXFnssJvcy9qcw66lPgx84uTj2VmC14NIPhDHOzvsX5q4F26F9z9HCKGv9-FVCZlqDtlC2XGwlPeoCuaz5gyUm2ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25312" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25311">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=v5HAkptJSZMPCW2cKl8O4a7cYF0gzQ_RS2vGEJtzzrgxIwwFcC3xnrxbMwy26LLPa-0Vk4x_vI_tUSsPLZkH4HK1CaooDhi7YHF07E_DrdQU6ae1gtXTyoBQM4b9uE9FS97WM-nWY21vGM9akmi-hHA4-XM97UnBG9ZE_SmnGdldRr2_0r4i7LlUuokApw19XDnQXhfA-Gks8aq5h14cXId8Aa3b6qKobyYUMW2vnNScyuqFpjoNMVACJ1c_r2EhssZxudFTX2TRvQeatUHySoRV6Z7YAoBEGNa0GdgfBCwIBeQuySuFdiayAT0ZXs5WXSQ4AixjUt_NkRz0M07xAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=v5HAkptJSZMPCW2cKl8O4a7cYF0gzQ_RS2vGEJtzzrgxIwwFcC3xnrxbMwy26LLPa-0Vk4x_vI_tUSsPLZkH4HK1CaooDhi7YHF07E_DrdQU6ae1gtXTyoBQM4b9uE9FS97WM-nWY21vGM9akmi-hHA4-XM97UnBG9ZE_SmnGdldRr2_0r4i7LlUuokApw19XDnQXhfA-Gks8aq5h14cXId8Aa3b6qKobyYUMW2vnNScyuqFpjoNMVACJ1c_r2EhssZxudFTX2TRvQeatUHySoRV6Z7YAoBEGNa0GdgfBCwIBeQuySuFdiayAT0ZXs5WXSQ4AixjUt_NkRz0M07xAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌هشتم نهایی‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم فرانسه - مراکش؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25311" target="_blank">📅 00:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25310">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vK0GG8xLAqZAdZfq0GHycniBFcA-gmrDSSSI3F9JIeGRDECqDvz_kkve9-trbz0VVVpZTx2_3XUApIb1yNlNQw0v6YvYjSnlW0U6lZ5c5r4fU1J-_iZ2be3XJToKhX-Y-FF-V5J9Li14bjqst4ITuZYoNnXMZL3AoO4NH8axGHRjbrmfM2LxEubdGXvSO8pDbKZHCVcfA7LPfsL8j1PT2m55xUvXfFvyGEItKm2lxSOkcKoXZV2AQApSM7mvktYhnmcR5NevL-4OzxEKZGBI42PqOZFHKE4lmz1Q8vaBvjrJhDDidNUkIT2YzrLRQgGi0qQkp_l5iB44hVXH5IJP1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌گلزنان‌تاریخ‌مقدماتی جام جهانی در آسیا. علی دایی با 35 گل زده در صدر و سردار آزمون با 29 گل و کریم باقری با 28 گل در رتبه دوم و سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25310" target="_blank">📅 23:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25309">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6RkUttTcHpNCoAxr4iwZKLjTEBIue3yfsxda9XqC-yruIFcMLpCFAP5_w8nf8NvWzTkB2jIUEjJFRb8XAkN-Sv7DDB-hI274mKA1eqGFQi1U4x413b6nko37UbJc1gYaepiaTY62mcKphZ0bux5i5Vh1Tww8n9ALDHX4ExlmRD7S9gmIFuzjbdMqZ_VLlmLOotZfzE0ddRlDIpuXMWxUh5M8DGEUBquSvyHyjfeJcN9YeeFfGAFghWUh9fAAQB1Ebx12TYEufalR5VE_wmYFR0wk2-pRfub1sEThDxVTCuicr505bqRE8zN6WETbEr9VMcHcTjqJYazThxVYbCJbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ترانسفر مارکت؛ باشگاه پرسپولیس برای جذب پوریاشهرآبادی20ساله؛ سهیل صحرایی مدافع راست جوان‌خود + 500هزار دلار حدود 90 میلیارد تومان به باشگاه گل‌گهر سیرجان داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25309" target="_blank">📅 23:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25308">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXIf08-Lg5rvSYC6SlYmvLdVMWF5HuSrxhhrXcNWRPpb_nnE_iXS8wIsw8IBri8oIx7Yg4v-KH6g8ohGPcIJj2W4c1AixWcjLFF0hqATz1Uouo93P8VhThv0gC_B_lmEW-7KsuG044rHE7WqFwxUyviBgt3B8zz-bJsg9KJ_yJIediEnl3jttvAwd6yatUZELN4MRxbZgC0e-iGVac2TfkhJS2UrS5OxzYvEQ3COa0gLe5JkiMZZ3pOr8AjoW7UHqwbvcHd9Zc11jff2T3DcXfdCH-A6A00bmzWIOXuKR36LdPYG_Y1w7FdjFi22iUYnfbGxHd_4jTWcmrjuKfYApg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛ میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/25308" target="_blank">📅 23:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25307">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSWmwQvLRVAPvxJBzqjfAftyPNPizNZLqn5SI0A2lw_ATMFYrRliHFfp4VKKBdVrkAjaImUxuHv4f3AlPFeDPuNiqROl2b1zuS4f7zT32HO7JnvRogiaSAy5hIbNCqI7T19rfp59TpJ1W5oeZzUlp25H5WozbnCx9_u43h_IO24TZ5PNrYCIORWanobwBNy8K9TMBzGUE9nocWYDL5T1XyAJhBf058dA-aAjPhJY5ITnPKwuz5ZxJcIjDmRaWf_NFXBTaXLNfd4iqLigsgpEzhzVjJV7vmlgyd6VOrhchIxlc08pEhUwuKH-sQozyGdl7Emr02lYUcfZEfhwo9TMWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی دو روز پیش پرشیانا
🔴
پوریا شهرآبادی مهاجم جوان گل‌گهر با عقد قرار دادی چهار ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/25307" target="_blank">📅 22:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25306">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZYIioReoC4NeRt1tDOYkjmUx4xcSkme6PEN6tV0U8O2TZ93PokaCDx2VZ7u9ZTAWTa8SipXVUU75q5mVxpqc5buGsU8JXnada2ADb8VS8GvgBZ_VloeSQLRfcZb_EMEVWLoxMjE0MlIqV1p_anwyusqZuBx-6lxU047LFUrXUnJ40UdtfUs4jmWpXYjEtb8tABK3ufbAy21GgRxaQKMWr5BZN5Qy-vb15dIEUnNrUckkFOnDWEKMu9cswA7KIf_SOmB_hNg2IQaScET8i8UbTs-NNudloEV3uIQiOWJzdbaS5ukhLfxcldmdw4eOEOhRTZei0Cq73tFmIWapSFIJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/25306" target="_blank">📅 22:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25304">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hwaykuAoTlJXYZ71klWE_N94xXvobRSLpuhKARYlnDgZI0icZK4xb-rqbzqIUWYb4HPzuLJuJdj2hn1d32OOCTLzBdmqsGAYPKNEOXh6usCTv-FC5l73yeIoKtWJZUEZ3UWWdxkUmC6MY0naeh5liYlWEKfVoyC0aN-a2-bpK3ig7nVT2ssMft3O8AXS0f6iXmqaAdYu8PSyNcvFg_wLiUQVEHUVFTIwHcj5L3tNfpqzMB4fliOVLQzxBF__TsC-PhYtpWA76uIp2LRvLRAOg3aX53L4PW0ISKY-y5a6zTdHsD9Wzbwqze6GxdoSR73GCySO-9Q97EcdJz6kb2rH0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PUO1SSM-kWfwJOjPGThFYSSqvsDVSn-31ruUKH6O0jdMhEIYlUrCdXlAbya97Ol66w-b-o6J-Fl1vUOpok9aQqvTW2YMZra2O1f8c_0ILtAMytLLW6ROEc_7-d6Fdj2fMw5PLCFDK5779kuCKGvFKkyZEt03zXrMh3G9oYfToZyaYTxXxftZYZ2wnD50q4EnRbZWxSFKobS9SSf8SlSKqLOh0MfvK6S66LfRGA-vZzxwPnqKWzHnK95o6qWuT_WmHaKL5VTu8w1UiXBpB_kVxdMIoqZiervQqzDTE8vYKyxP1J2vJXzqJ-c2Ckg5bBv5VCL670PSrunz-fkUnrIm2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ازترکیب دوتیم‌فرانسه-مراکش در جام جهانی 2022 فقط 9 بازیکن همچنان در این دو تیم باقی‌موندن. بقیه‌خداحافظی‌کرده‌اند از بازیهای ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/persiana_Soccer/25304" target="_blank">📅 22:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25303">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmMPW2rPZ1EO_dQI0tnkx2I2VdMigee9HmbTfdv_G7T10ROOedVep7gxM_8na-FAnGglxMj7UU871zfnRp5jMsr2WaCZYm0HNWOD_p48_kko4WYA3RWZgYFRFEvp0_K4PlkOfjPgKwKpMG9hJvspGhAPtlhNx5wHDb6B_4tt9Dm4pZPq6FPW7KbFG2HxRS39u_XCxlbdLp5Uc-RymA5FnN_pPxNQbm7zHg3puGLHoS35_8PAly2DySKj43GUEMFc-tqBdALyOP4mdATqDxmERkQBvSjKEmn0ktwtOZq8S01wgrY95vc-1B_cNIKOBZXgHBI_uwD4a2LEiDhwqtveVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/persiana_Soccer/25303" target="_blank">📅 22:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25302">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RneXyl9_qZSYS-wKQzqHw5sNPl6YHpAMCG8Vx6AA6gIRhxiij_A0e06n5CPUZ-QqUEAB-Y-1pYIFMAaoZ5eR77nDO1SnSQY0Ne0HUJtrLbfKCdIrCxLqVS2aZpuNCMhMzCD0vuYUqNjkVbQzxjL1lBG9FCXem0kuLYJdpy4Z-tWAo8Ftt9zT_H6OXa9jsPdYLuB3xJgCnhmgpV0i0w5MC2H65qqAIOR_HVPriM6lRKyasxVUDLDXDTAEptpXkWEhnk5Rr_5WWcchBfVyoN8JdPI64cYGPXnKpzLKKC0_WcALjCUjnnRWIA6bIdbg01WxcA1qFdx97tYKkWxznC25GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جلسه‌مدیران باشگاه پرسپولیس با مهدی ترابی و نماینده اش شروع شده است. تا ساعات آینده تکلیف ترابی با مدیران باشگاه پرسپولیس مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/persiana_Soccer/25302" target="_blank">📅 22:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25301">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0SqTOP63YeS_NhDwZXqQINGFsS1eJxZoinUKu-cWXKihGPtzyDgo4OVyUaw4L-g9nmFYXdVsQbnXMUeRXSRR-MMid4Q61kVLBrpI0a6f4-DQDqNmTYBWx0T5JGYxbyd67Xj-o4a-oUyKrtJOgAxyAYP3a_euuNwJUfDXwAnj8Zu6Hy5wEowbbBx552gdefuhiZ9btHfa27dbxX0VNrihaxcFi9TTSI59vrTIcWuA2UPnThClfHtWxpb43skuBlWs-qlBprQpXU8hhE_adwc7wNVvMZmgczTk58Ss8cunPYjrUPHrNkUkDJHw7sB2TtVwUoirSVXK7lEBo_HTaAauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیدارامشب‌ دوتیم‌‌ ملی‌ مراکش
🆚
فرانسه در ¼ نهایی جام جهانی رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/persiana_Soccer/25301" target="_blank">📅 22:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25300">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JS02sTjxk0DlstR7R5wRzPkahl4ZLahqMbbwjVWxq-Lx9JUkjUAtAWOyurAntuMIcWU-me78Esyg2sQmVWctY98yUBLrfbpwQDqV4upsC8niK_9M8KHf01qk1txJCtnlfMsIaC-e-OwXJpsPdFhxYhV-gyV0Z44MWmLWp4JYuOkgIrYKGj6ws-PscmlEzCl9Me2xTGAmy6j1Rt83EsBAwm02oXmIsg-zyk6A4WZJy3egAAzeT112EzT4DtSQdSiGCXY31xfb6CFfhenzlBYS9VBJhuq_cLn5DZ2_DoUMqSc88HSQcdrNBp6N4scr7GRqlIMuplSQufhk-W9vnWIU0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25300" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25299">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lw-AiqKjt5heXjQAZSmqbAGTpZg-6FtBrf8gEfjBRREp6tcyk-D8wkkWZIBs_E1qRfyxEV9LvT0RUqmCBmKEzokjJWLmCo1icsMj6eHr1S44ICXeImgPLjKkp5Q_oDMOH36y17n06dsjbgJaED15cntO78gXGUglYhhiYRy3q7gjg9g02Fq9JaTvtbmvFyrEp7-Ji1hhNNaDHt_8SvDw0T4gR7cOL9DU7hl8BsTs-haST2D8jsIi1wPJ7pZWCR6kQBLgYPd1EHJRiiVDIw-045qr4gFroMF2aagbjQga1fTpbtdgN60Q8vDHyJN2LxV4xh2OyKOxlqtLCCneYseNWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25299" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25298">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By-bw67x4bgFnAvrUU3H1e3kn2XnWNQYtc6X7jKc3RUVw-FLqRXtaQU2eZ0xXJfiq1s-1P8vhvmcj2Hhdew3ClotuEfVVzSajGOAm7pJck0j9Vx3HMETAWWfWjXp-4lG4xSPLRqUBFM5z_kKNtA7ybkIB3HvGkWFaFpdQ15r1IneEXO-n4Qo3r6TJxB5q6eHGVbQEeYtFaaV_60qIra2Tvyyi57-XaHuNJh4B89eMfturo9vIza75fOtizIaSF3__CTUE1kAx6PGxh0Y_jUsBZlAQTlRlNNlBU2tGSGt2N0_EQAnZXdbnM7EvzOo9i0jW3cGb87qFUucF1V3GCMNrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
مراکش
🆚
🇫🇷
فرانسه
فکر می‌کنی کدوم تیم برنده می‌شه؟
👀
🎁
۵۰۰ دلار جایزه
بین تمام افرادی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، طبق قوانین سایت تقسیم می‌شود.
👇
همین حالا پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p4_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/25298" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
