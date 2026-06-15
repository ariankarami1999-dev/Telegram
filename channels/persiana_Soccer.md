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
<img src="https://cdn4.telesco.pe/file/hpFo2wrsVScXtoLNBn4KgqatEA8M7NqeZ3xD9aaDmuo5kRVjzTjZ3u2Bg0i1aN9pxpQFX0w_3cLK_Fz2mO8xB4kncKvmG_JajoJ4ZRzVLoFbdr_KTR5dLLgu7kB_wpCdBKwgdtB342-rqcijAR_0NFfPB7Zi_cxfTYB2BnQkpk3-Knnn0Z6mmbcUN73u-Mi35dJaLbzpmy3HZtMsRreqwPQwHTaJGiBIL9MYVpm8qs2EP18mAQTPd4nbS0sO3W8h-14PberAHR3Ja3rj7zVTel388fxbDpficzBVu7JwYCH108nYLAB6MHThSCNpCHR59FvHy6orjsgpqFB_JWXCjA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 297K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 01:29:10</div>
<hr>

<div class="tg-post" id="msg-23559">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NY-YiFV5uv8VHNp24N_yDoZ8YDCdt6lmE1pHW_MxwGXeoLComDtbbuAdhc5hN0xQZof5zZApdeVLK7n6eF1ZYVHWbM9b5lJ45Slw_bX0Bs947hrzyiZ2EGMfEME_QC1qdeVFg0_r4Nf4ekm7fJaCNYtkBzB3FlQbrMyvwi6lGTwGZPqIVigldVyL7w4c88gMF9P_4hxYS6Rw3P3UT994aiItRGRuXmjEgJYCzU0XIjfUOjbvOtmmsRGo2j9NYrsbu-OyPHe8iB3CcPcTzwbFxlJXEIDnLBS6ACA0dMSAiD4-PLHML6f6dEZpgmaApKoaEn_SujnizD1Ou6A6mUpB7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وزینیا دروازه‌بان 40 ساله تیم کیپ‌ورد، قبل از بازی اسپانیا و کیپ‌ورد فقط 50 هزار دنبال‌کننده در اینستاگرام داشت و بعد از درخشش در این دیدار و انتخاب بعنوان بهترین بازیکن زمین؛ تنها چند دقیقه پس از سوت‌پایان بازی، آمار دنبال‌کنندگان او سر به فلک‌کشیده و به…</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/persiana_Soccer/23559" target="_blank">📅 01:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23557">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTZQLiKvLvE1o_h2TTt5NIyjVrUiYoLoR1P7y40DcovcqM94-JkXfIc6ONw5zp53b9pXQBZOigskxiO331uNf41nzaG_RwmT44uZqJLFRvoDiQ_DXK4uwXFd8HoV4Z021NOweC3BBZQx6T-l45ZIUoHBt3WXO46my1OLqFoHt88jyJeGx3RAI853tO8vulb3_PlCZc10Lc9KMnhTDh4rU-DstebM_-iwa6NmBfeEP2WN2j3JjBKj8adSH9ALg3fPiRwb3PTDWzZfSFRGcRoARSqLl1VuEDwFzElFkyWSoWPct5elfbPIyNc7rG4n7Ec0p5h-1kK1e-Gg_AFrm3Dqqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از مصاف شاگردان قلعه‌ نویی با نیوزیلند تا اولین قضاوت علیرضا فغانی در تورنمنت در جدال حساس فرانسه و سنگال
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/persiana_Soccer/23557" target="_blank">📅 01:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23556">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmXMmC34yHRsObCFUP84faIh1ziuThjAzwmv51IvL0fKWZqU-T0qZJYIMwrvfPpphFoOlp2GXmiP96M4GLEdSbROlKVfSqP5d4uftHbCTNZk9PlqhkSQHq6qXau4-QXqxEjlP6zgoplbTCVy7XH6sf-fLmtvdu56yzmz7Hy_MGGwnhTtFtUpnbk1WsLsujlMB-TE3N2lu4fBd5Wl9QleqynfHGqfifb33Jo9RMqDiPzZbF7kRadslvQwstvSR8u7Aqh4tFlHz6eB1IHkFXHxqtoECIcj1KEFJoHNVahCntvrC4zX6XeO4Q0ai25xmFL2cESgKITXgbGd9GLdJAsZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌‌ دیروز؛
از آتش‌ بازی سوئدی‌ ها بادرخشش ایساک و گیوکرش زوج خط حمله خود تا توقف‌غیرمنتظره‌اسپانیا و بلژیک مقابل حریفان خود
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/persiana_Soccer/23556" target="_blank">📅 01:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23555">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11adede3d.mp4?token=be-ibwKYnpFR-JNTfjdCgY5L_KsoURmAw-bEd0cQPUwDpRa49omlx8q6PO3yvcW8nfQffjv5zas4we9LvyDJJluKVTAw3XOvMoWh3Kz6X_jEImBuEbbSLGXDSENBQgNvVA1ODUiu7S3gsN9ZVSRImrV-SaDSqjekyky53ZQapI3KHt9a8JVvuY3hGONAaN95U0BZlsT38mxKRtl_mJjvW18cvu2RJmNGP6ZsMGKNSccd0l2nPG1Y1pOzVhBvkwF-qW03erR7v2DDQLNl9OFg6_dYi6Cq0gyRQoMQJhWlN5lGtY0XYJgz7m0n2F57tKQ0EgAaJDAx-uqwBz5jCAc-uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11adede3d.mp4?token=be-ibwKYnpFR-JNTfjdCgY5L_KsoURmAw-bEd0cQPUwDpRa49omlx8q6PO3yvcW8nfQffjv5zas4we9LvyDJJluKVTAw3XOvMoWh3Kz6X_jEImBuEbbSLGXDSENBQgNvVA1ODUiu7S3gsN9ZVSRImrV-SaDSqjekyky53ZQapI3KHt9a8JVvuY3hGONAaN95U0BZlsT38mxKRtl_mJjvW18cvu2RJmNGP6ZsMGKNSccd0l2nPG1Y1pOzVhBvkwF-qW03erR7v2DDQLNl9OFg6_dYi6Cq0gyRQoMQJhWlN5lGtY0XYJgz7m0n2F57tKQ0EgAaJDAx-uqwBz5jCAc-uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
نمایی‌ازاستادیوم‌سوفای‌درفاصله‌کمتر از ۴ ساعت تاشروع بازی دوتیم ایران
🆚
نیوزیلند در جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/persiana_Soccer/23555" target="_blank">📅 01:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23554">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a904e7169f.mp4?token=NsroHd7jdlmY4cXAV-I4T7HiVrItJO_ifkp612kiC82tOe5cfJmsdwHsdfrVzny7OLb05VbnTFAibaAdyNCFvPaqgf8g-8_EIzILif9DF1U3sUUIOTtlxfhQ6vP5UoXoIocG7yaECN0WG6s8KSADeDo9ODFkB2bzfVlhrajFKpJEV0hBv5eXXLtNonmQIc6yg-dnGxI_exvpLcJ6c2YVRvDFFp46dzUtzf6IfW15b-OSvlS87lR0SXKdirEAOVnkUB7-7oagf3MuIZh9g-oPGMandN-SEslJa9nSZ2XYi_bEU_anyEaO3x-y5xIyYXNYgHGvr9x1wi3ozYve6hXvBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a904e7169f.mp4?token=NsroHd7jdlmY4cXAV-I4T7HiVrItJO_ifkp612kiC82tOe5cfJmsdwHsdfrVzny7OLb05VbnTFAibaAdyNCFvPaqgf8g-8_EIzILif9DF1U3sUUIOTtlxfhQ6vP5UoXoIocG7yaECN0WG6s8KSADeDo9ODFkB2bzfVlhrajFKpJEV0hBv5eXXLtNonmQIc6yg-dnGxI_exvpLcJ6c2YVRvDFFp46dzUtzf6IfW15b-OSvlS87lR0SXKdirEAOVnkUB7-7oagf3MuIZh9g-oPGMandN-SEslJa9nSZ2XYi_bEU_anyEaO3x-y5xIyYXNYgHGvr9x1wi3ozYve6hXvBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
🇪🇸
دین هویسن دفاع اسپانیایی باشگاه رئال مادرید و همبازی‌سابق‌سردار آزمون درتیم رم: سردار همیشه به من می‌گفت باید بیام ایران و ایران کشور قشنگیه. مطمئنم ناراحته که در جام جهانی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/23554" target="_blank">📅 00:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23553">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1GSzYDwk-I2tLn-_tAQyVrsS-_PSwf-RMlAijjBXRh9dlHp6P0y7X5h7sL9fVLPBRLpYk_60rkbPwePvXnxOy39OqfwuG9YArGnq7ffdeVPgFCsT4jPq05CAebCUrcMGPSQOtTk_KRRQjoywKtVPpsUONT2uyQiLq8lUNe8Dr5rmuqWZ-dR8fDh3jETxUkne4fH4yXClC-cnWBDhbKNBkOWceyD2ww7r-TO_FuiziXYKQY-NJc66s0WxFtxfrAvv9kYnuKLsmFlCS_zsJ0WovN9_ryGZcLedajM2Qk6lVfNhIhcccOs9dQaK34o32x8wTCyfS-z53swN7mEvNwPcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه‌بنده‌خدایی امروز برای اینکه 85 هزار دلار ببره 1 میلیون دلار روی‌پیروزی‌اسپانیا مقابل کیپ‌ورد توی Polymarket شرط بست و الان همه‌ی پولشو باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/23553" target="_blank">📅 00:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23552">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYfYQfqvRWEeXSpLuUPG_BMcscimss_VtHjWpn2NIygT3JZS67ZIxb0U9UUh-OkGp2ZvMnoBAeBMYcNQ0C8rv0YmalwYu806-DoDYDJIFvFRlCd-yG-RNZToVMub-e8HjS24hPwqUggkbelhtYairIezklwGD0e7ZuCg0z47SsvY188AcoEED_eC6aEZMvvJ3ao6gAQrFVHBiBhqEcYvoTp_smyIrHCtd2ATTIPACRXIzSZCeM3hHwOPhtYC6q-lkxObYR18bQw8xvmQYuAoNhCnHI72sf44xDF5_dF_DQvxKJ4UJLjanxqzEun0D0FHthcSw4nyyO2sVznB5NfdAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇬
🇧🇪
این‌هوادار تیم مصر پیش‌بینی کرده امشب مصر بانتیجه سه بر یک بلژیک رو میبره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/persiana_Soccer/23552" target="_blank">📅 00:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23551">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DACk_ws_y-WAe5in1Q7LfI7o0SoOLYJ94m3nB4pak5RRvtk6xCNl9UUlPF4gS5-p7yT-12EvYL95bUu-8YYU-4tYWA0q1xkZ7X6yIusStC-wB7P6qhrk5yWFW3-iiXB4gcKnj1Udc8plJ5Z-Oo89tjOazrvO-tfVwYzB4DO7dbJY7g-h3H8cIaHRz_If7DYg3zS5EXgchFWGAuEjX72ngh0RZeklRf78HGX45691hr37pPzycVMq7Fv5PwWgSn_GrLOB4Nwaix-3W9CxHf9JJYyrwVZIzX4xPb41QIwG7iU90nGgnFrFko40qiMrrNjF7xZ_DOSx-8uG94F1P2XKaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ همان طور که دیشب هم گفتیم؛ نماینده کسری طاهری مهاجم 19 ساله روبین کازان امروز صبح با باشگاه پرسپولیس جلسه داشت...اما طبق‌‌ استعلامی که از مدیر برنامه این بازیکن جوان گرفتیم هیچ قراردادی بین‌طرفین امضا نشده است.
🔵
جلسه‌نماینده طاهری بامدیریت استقلال…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/23551" target="_blank">📅 23:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23550">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRcEZk4XWCVjQzoqW3IPuiwa0LUhv1_XjUuiKWKG5gZjQCOxGCPnJs4JpJFN-4oAoz4b_A0J2Zpyh6IVadXxziZxwuU0jp-TCQI-ph0qidBxtOV4SSINjutIEsjS7TDN7CpRL5REsw75oyI6qAd1wwc6oEbPPS67a3atHnM-PHrSgtp7Q6nQjzri6e9lccy8bZ-8jT-8EdeB2NFn-Z78CXC3b9NJma-TU0VX-fDh6D4QbyZF6bAJfuZlUn5sG7MzxaNoOyhM1qWQzU6Wvtfzc_2ZOhF4AiyYGlZrVIbzFLOz1ApaDdOvlUZjWMsRAJ1qEDG2GMJJ_I3krWzl_iWSjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇸
تیم ملی اسپانیا در جام‌های جهانی اخیر:
2014
: تنها یک بردمقابل استرالیا و حذف در گروهی.
2018
: تنها یک بردمقابل ایران و حذف در یک هشتم نهایی.
2022
: تنها یک‌بردمقابل کاستاریکا و حذف در یک هشتم نهایی.
2026
: توقف‌در‌بازی‌اول مقابل کیپ ورد. دو بازی بعدی مقابل عربستان و اروگوئه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/23550" target="_blank">📅 23:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23549">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDbxfnurTr5WKCQR4lrzO6dWFI3iIqNI6etyjri8ugvpkRxjIWKPeXDATd1vtrbyQUFVJi5cC81H6MwABboyxLB74KmBEnnkx-AaLvUNEl9mWrvvZjDocJhB1pUxSUU3l0f73wrVBfcfqFR7PVw19orSpV2qaCE9IkBLzOg2F0iZkb7lFcGwIxukXWl6ep20aAF2g9ZctMDM6uowQiyUxlAHOZr4ykBHVxyqMopnfqt3QSHv4L8kb1n2xmW7M7vV-lm6WuFn3YQWdwsFtXIsNNT5sqzDMGz39Nefv6jo2yX4cQv6W82yozHapC61NAfU1b-8wyCqqx0a4oQwyI05lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل‌های دیدار امشب دو تیم هلند
🆚
ژاپن در هفته اول رقابت های داغ و جذاب جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/23549" target="_blank">📅 23:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23548">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HuT3-SP__YUkE12czcuzL81wPjfjSF6gtrbrRGhwgZWF7LESwDjWPBW6MzSpV5inYh9mTAEqkl6N8CuV0kfrn-OHamwUlPfnJBmcQkTUnDVd-K0Dwblfo7WafuUJwSzJTwEY4eSFrNUY_hDNQu7YDhGiQf7XXqL6CYIzYsxpo58GM48wUqekdY_Q-X7Rx4IQfAScJWzQiiDobjQJwnTA9vTORqoQiu3W4WvcAPK8rPu5I8MsjZgb9Kj_WdZInBVs-TcNezzIQ_xgyaEPQkDx62DPaqNwfG_w-oyhbP32LCOURt9_GUgi8YXfIK4RZfUc0PLbIFl3rWM9rqJdkERzJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی‌ایران‌روبا‌کمتربن‌ریسک‌دررومابت پیش‌بینی‌کن.
⭕️
⚽
ایران
🟢
نیوزلند
💳
حسابتوبرای‌این‌بازی در
#رومابت
با ارز دیجیتال شارژ کن
🅰️
🅰️
🅰️
شارژ اضافی بگیر
✅
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
همراه با درگاه‌
#ریالی
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
25
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/23548" target="_blank">📅 23:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23547">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392bb7bb0d.mp4?token=JmOn8EGw5ahD4v1HxiLR9rdAZIwAAu662-g6l-lWsxzCZJ3xIKn3eoxNP3HlXSesOz1BDxtT9J0z61pVrg_JsvV4J-Iepb-6OsYefW7c8q0gir_kVR3aAD5jOsDhZFYLrreKy9-SI8tRY7qFfyTZpyyxPEHUxl0fILszrWwzZ5AsxGBXvtBh8wZgKaFZjLsbZLLwso2Auqdyr_Ee8QnIAZsEmoyJ7EmPEUk344p4U07QOMx4AbDrZEAZM3gUZrvZWN480ybpNMZYM73iHoSEZ_X0nqMA8vxO18GEGuUjvEWeTydTf7NkwpvjUsYwDGMN9PuyBWzURBfmYgTPDpO980kMUs-GvYGo4Qh8BpfxF6xMJ-vKSSMC5-G_CCoerqD0MY9DIICJmUNRh4-6lNzUBtu3LfYRTYT7UZjwPLzNaI-9KfPsXbfNNK7jnw6r7tJMzdl4Kptr6KZIpbw4HbfjfA-Co-HS68O4aQZDUF_zlQZIRqFFM9Gy2Z24IhDtSqMOcFEIvP0HrPSnuekIgCRAEUhNo4ZHBrZjJZh_OEqityg0WXLdrRfxUCWDWJOzHtpAgzfk0dxhKXQNgA4VUMCCgd3GIQd6EfNZfV3vIYEGFYM4ESea9XHTakkHkCk9UI0BCoCbTuAc4z_9j-H1xc0dyERQPiMEI7m8vnGgBXy2jYU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392bb7bb0d.mp4?token=JmOn8EGw5ahD4v1HxiLR9rdAZIwAAu662-g6l-lWsxzCZJ3xIKn3eoxNP3HlXSesOz1BDxtT9J0z61pVrg_JsvV4J-Iepb-6OsYefW7c8q0gir_kVR3aAD5jOsDhZFYLrreKy9-SI8tRY7qFfyTZpyyxPEHUxl0fILszrWwzZ5AsxGBXvtBh8wZgKaFZjLsbZLLwso2Auqdyr_Ee8QnIAZsEmoyJ7EmPEUk344p4U07QOMx4AbDrZEAZM3gUZrvZWN480ybpNMZYM73iHoSEZ_X0nqMA8vxO18GEGuUjvEWeTydTf7NkwpvjUsYwDGMN9PuyBWzURBfmYgTPDpO980kMUs-GvYGo4Qh8BpfxF6xMJ-vKSSMC5-G_CCoerqD0MY9DIICJmUNRh4-6lNzUBtu3LfYRTYT7UZjwPLzNaI-9KfPsXbfNNK7jnw6r7tJMzdl4Kptr6KZIpbw4HbfjfA-Co-HS68O4aQZDUF_zlQZIRqFFM9Gy2Z24IhDtSqMOcFEIvP0HrPSnuekIgCRAEUhNo4ZHBrZjJZh_OEqityg0WXLdrRfxUCWDWJOzHtpAgzfk0dxhKXQNgA4VUMCCgd3GIQd6EfNZfV3vIYEGFYM4ESea9XHTakkHkCk9UI0BCoCbTuAc4z_9j-H1xc0dyERQPiMEI7m8vnGgBXy2jYU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ماجرای شیر نگه داری علی اکبری قهرمان بوکس چهان در خونه از زبان خودش در گفتگو با ابوطالب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/23547" target="_blank">📅 23:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23546">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d02367735.mp4?token=aNSyPsoYP83v7B5xSwdpr9elWEVcBUIJwpuxs9YKOV1y2unVCXWhbqAoKjH7xfQ-SVZJrIwOAG166kOTUKlq1UqJAYrKyzj5-W5KyzLp1sZzKdC0-qEur83gBfTn-E3qFUioin1udodyttU7f3-lgr5jQvkCMnPOA79d63Auf_IWpD7uVbDT0e29Hy4KRSbSeOtWIoonRSKlrwOuLa26B2uNs3AeDhWlyZ1G2EVMuNp5ooN6ESx7aakdxqV5ZyrkFv7dH5f03HFHl28bv0PCaXCBMt5o5Q5PiTD3a_VLQoIQJ4byMz_fxHQq5vWH1Zf4k2ADgQQLp4yhOupfp-ASaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d02367735.mp4?token=aNSyPsoYP83v7B5xSwdpr9elWEVcBUIJwpuxs9YKOV1y2unVCXWhbqAoKjH7xfQ-SVZJrIwOAG166kOTUKlq1UqJAYrKyzj5-W5KyzLp1sZzKdC0-qEur83gBfTn-E3qFUioin1udodyttU7f3-lgr5jQvkCMnPOA79d63Auf_IWpD7uVbDT0e29Hy4KRSbSeOtWIoonRSKlrwOuLa26B2uNs3AeDhWlyZ1G2EVMuNp5ooN6ESx7aakdxqV5ZyrkFv7dH5f03HFHl28bv0PCaXCBMt5o5Q5PiTD3a_VLQoIQJ4byMz_fxHQq5vWH1Zf4k2ADgQQLp4yhOupfp-ASaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
وزینیا دروازه‌بان 40 ساله تیم کیپ‌ورد، قبل از بازی اسپانیا و کیپ‌ورد فقط 50 هزار دنبال‌کننده در اینستاگرام داشت و بعد از درخشش در این دیدار و انتخاب بعنوان بهترین بازیکن زمین؛ تنها چند دقیقه پس از سوت‌پایان بازی، آمار دنبال‌کنندگان او سر به فلک‌کشیده و به نزدیک دومیلیون نفر رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/23546" target="_blank">📅 22:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23545">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r77AD4hT-Kr-P6RfRG4i1jEUHncgWm7UXSuGsXNMU2O8gzwN_lEe-_2eE_kg2MZxtv04y8dDdwBBpcwqzgB-sOakhtB01fUlc10qYMhNaLN0vxSaJGGo36-65nNE88dJjMSBndHUQBZc2VuegxjnpHCA4mjKv41usibg4oO38l4Xr8uqSU5cBY7rTKYodmm2sR8OaROL2qBeHIuYuhAl58OcTaf5MxIZMaEO2FVGGzWn5fMf5Sh5HxyfUzRelVosCktctvYYMx3Kdue_pfiy2IGi7mocvHYWQzZ6-Ld-y__WrQqXAv_CYpXW0rm0qUmVzNq8zlYZZ_UukLW7-pwM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دریک رپر معروف کانادایی یک میلیون دلار روی قهرمانی آرسنال تو چمپیونزلیگ شرط‌بندی کرده.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/23545" target="_blank">📅 22:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23544">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAX8K-N88EKee8bUJDptTjx26kLXNQ1F4OMD2U8c19lUuvef-kydmQRQOOPUfyoZHZ6gHZiTI5AWLJ2J_Khdb_29ijMbI0mePuuKsgtmjlzfis3BY8PnH6zaujYgNJYlaxLurkKKl3aF8wiOzGbGJ1_eXrWdva418gQFAY33NLirh3baefixDqgcEsU3z9NDTN9v8hDNFhmWoCIAK6seEaOGaVKQBzgCl9h_wysaMHbT6N_GOOJyXBCj_49PNONOJv86T2tl43DmmSyDY4XOzPOm-aIqfL825UI7LTVVj7Y6WQ3ZGwMjZthjQOVlwYQdba7ReI_GnU54SwvR2JN-Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
جلسه‌نماینده کسری طاهری با دوعضو هیات مدیره باشگاه پرسپولیس دقایقی‌قبل به پایان رسید؛ ایجنت طاهری به باشگاه پرسپولیس رقم مدنظر این بازیکن روبرای عقدقراردادی ‌چهار ساله اعلام کرده و منتظر پاسخ‌نهایی مدیران این تیمه. جلسه با تاجرنیا حدود دو ساعت دیگه درسعادت‌اباد…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/23544" target="_blank">📅 21:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23543">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSWOPGWbqjirD9fQTq3_BgTiNKzCR7lKrx079rNyVDMtbaZiN1kOYnPfUwlXGR-WMWYwcl6CVXPorY3IAhRmMEbfSEke8WacOeQRGSBQ-uSpru3SMAHc6rLQnMu0i-jn_BVuwzxOGkMhckaSQviBfev_hjzDUYP4sth38SvZuortZqjyw5mXycwsJZzB_ptFfpICo9cl07p1t5KXCpjRchkGE4hm9wiUGxdyrh5sid-alEs8yybxUJVaNVn76JQ068Cd9CjpCkXevt2zZAL2VdyiClVpkiMEWK4PIgmRoBPOAJgj0VgaPoSya4vqBQw6GpmTG6HZILmROD81U7ELxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026|توقف لاروخای پر ستاره مقابل کیپ ورد در شب درخشش خیره کننده و استثنایی دروازه بان 40 ساله این تیم گمنام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/23543" target="_blank">📅 21:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23542">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5WHDCeybKb-d2ORaw2UKyKNAwDamk58VjWD6PfsV1tCsv-VzwggTm4UeaHT0pOJ2aeHr7E3nr0653Ui224HUXBLvJV8mu7eLzSrvXZ6OszFghYnXjniLcORGuSxeQq6OheAmkQIh2MVsTQX-i4cb4xtOaXXTMGQsLqO_Ft11z9ApO5tn0C0sQNzSLhJqQGfOPr_SEGN5NI1lS9ztjZERqa6aru2r-1o6ttFQpyWse5Lc_25MO4Z-gGpp2Ii6dhPOlGscxyjQdOKKwLRD_Q_eIVNcR8IN4sQEk4DVcPZPR5Rrrpjj_dDupTHlxwbL61N_ax3saG0H0s9muavi9UQpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026|توقف لاروخای پر ستاره مقابل کیپ ورد در شب درخشش خیره کننده و استثنایی دروازه بان 40 ساله این تیم گمنام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/23542" target="_blank">📅 21:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23541">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGdVmIE6k6nZM3cHrKZnLwvGTE2iF8OIpo5bNNHu9BSidoEwzKVktBNl1S6BHoDEi832ieJOTO3rOIH-5ySehW_LKbBDsnqrjnlGCrxivQ2FkjpY-8ON2mTUgprsIecG9soYPbDnNIqctvRZxoRdNhVC5bXFshjPKgDCGYXdjxdzJkpBRMqZnkbyeilJP-VcLQYo98UyJ9jPvY7G46ZT0alT2xWuUby7VwbpNwIV0iby8dfVpMpu_HszX965TCGQ0sVaqkQn5I-l2yLytnbeV2irOVLYkhfEpGMKNdOonOzQFb3CQS_xlbAZRgNNicS3acWBL2EdYIVQMf5J_kB8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درو‌ازه‌بان کیپ ورد در نیمه‌اول دیدار با اسپانیا 7 سیو موفق داشت و مانع باز شدن دروازه‌ اش شد 40 سالشه و ارزشش تو مارکت تنها 50 هزار دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/23541" target="_blank">📅 21:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23540">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYlR7UKMB_0ITmaUslJ_uVdc700ZBFDvqLpyE-EhttkOHp1u_KdtIxAsPYm4u571wa3EOIFxJvyWGb7LsfKcBo3AtpsHQSwvIcwY7sXvI1EN9U_Tbunv_DKejMexZML0RYYLS185414voyp6DU-CQuWT6swBhGnybJHzfPhOUvSO7JZ9k_WUpHH59GtrC6SvblzWcU2qtamhLvnqhKvmEhSZM0tHF7L0tm2MoaCBHAHrnMWvrYkYhtxN12uMRuEkZ1Y9ysbLWaAD7cpxVMrqVESqOUGIHqNPf77ZXxKOlJRsMzHFkb3qlC2q4aApWNMAcNiTXJL6Y-TWbdYdFEwjhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
برنامه‌دیدارهای هفته‌دوم و سوم تیم ملی والیبال ایران در لیگ ملت‌های والیبال؛ هفته اول تموم شد که یک برد و سه باخت برای شاگردان پیاتزا حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/23540" target="_blank">📅 21:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23539">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEilwdkjl51lsPP-uzFDbry3otMBWD5CwD7LpBjSBxtEgzOA_VG3AZP5Roy4ks2QWSdwSHjCyuHdStqgOTu0cF-L7NrceAozFN8w8qdINzK3RJQBJOmZKJT5Nlm68RaXVTIFpQX5gpmaGfIGfkYQFEMcP03zmkTcTQngXnZsOlw-OTCE8AkslMUQGliLjiiBtyol1Vb5weEA-J43ZYeB4fqsJIUb7ebrG-vHyqk6_-UmiZl5FFBTYeUqAETaV0GlS2Za0hj-oA70VZOv1x3Xfi5Bzz3aaImxFVOwaNWI2baK3oXlkB1hu_T4Kezy_rxwqShdgDfkQMX9nxmdkxYqNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی جالب و متفاوت‌از خرید مارک کوکوریا مدافع تیم جدید رئال مادرید توسط فلورنتینو پرز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/23539" target="_blank">📅 21:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23538">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnapp | اسنپ</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2w9s3TWBrh7HJKzm5uf5g6dN2wT8nr082DaQK6QwCt02thB8VYRViMm5YnYgnjqWpKgVyBXlOxAaL4cVr_2CAjKXxRwj9oMjik16WNTsK-OmzVswrb-34Gcl8yGvvDV8GEEn6aZp9NBwk1gewfdQ8yXUU1j96QyGVsnqqT_TVfZp9QPHkkBPZxo6XOxRNKp_LIHmZYmBGmU9NwwtcHahLG2g_g_kyQQT_jckf2HSxQKBZuLWo9Mu6XNEJbcUr03gxWsp50QYWLRKIEQCmC6E4gUjxm2RR1GkgkbcRZoN-STYCbB7NOasNmxWPgHiw_gUK3q2N--M43p6AVrb-yuVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران - نیوزلند
نمونده.
🇮🇷
⚽️
🇳🇿
⭐️
با پیش‌بینی این بازی، هم
۲ برابر امتیاز
می‌گیری و هم وارد قرعه‌کشی
Apple Watch 11
می‌شی.
⌚️
‌
🔥
با جمع کردن امتیاز این بازی، یک قدم به برنده شدن موتور، توپ طلا، PS5، iPhone17  و ده‌ها جایزه‌ی هیجان‌انگیز دیگه نزدیک‌تر شو.
🛵
📱
🎮
‌
فرصت رو از دست نده و همین حالا پیش‌بینیت رو ثبت کن
👇
🔗
روی
«
لینک
»
بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/23538" target="_blank">📅 21:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23537">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaA3VK3-h81mDlIMTzMR4Qmm_52o9sWRppq2H3SIKb9jq-V4noueUinMGwz3VF4VBKzVth0CHm7_bHdzM0GrANY1_dNtH7LAogOHcWwB8ooLSX09YmpwW9KPhMsIPP4NYJdQfzWh5BxS2SZhkfSYZJiJy4k7E60qQ8r5_PNvnu76Ap4BPCv9qENPG9XZK5OlTeiodUGMDCcj9Ve4b1leI64AJskCYOU829CZLZW2pJQSkpDRNTopSSFmEPspFqxtjrDAFiKqUEAutazf8fJdEDGDNrt5Acu6--AyRlfsPFK1BVJ3xgWZMNlksjx_hbVAm22vgTF2nCyAtioH28WILg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛
فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/23537" target="_blank">📅 20:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23536">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBpxpjp1lPVcrgs9ag1uTl9bQxkQSQpvUrZUWq_7eTSzkdVXixV6u0VjRL8SBRxiQZqTGtlujxpS6-Pywngf1xSnLCJThxSTpLBfh-g5u84LoGd7sBookAyuVWv7aFaCvklraW-doWpW0oixlkCUkdpUuiDzBkP8oSpM-VWTIPzL2UplcHUhe2eGDZSp3Pv5wa8NjBDConIRcvI-M14opPXeLUpp-q94UUplanRmVHtAjwzpyIxEHxMia6YFYEqJDn_-qPqvTygqgHNsfeKMeznA40-SwExVUt97PTOtaEpeT6VyNQijV8kZlxksFz79VHiWuck0aI05nv_YDbdoCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ از آغاز کار ماتادورها در جام‌جهانی تا دوئل تماشایی یاران دیبروینه و صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/23536" target="_blank">📅 20:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23535">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JalBprcOBHgKKR90JAhPVUZ8NFh7hm_a5OLp5HoxtSoixTmSBj9erXx-te1Kf3nC3g2uSdWgp2bN_ZaRyN_BxA9B3WwOJVnXL9_BT9hX-dlUL59n1nCkn0eI6x1BXfacofL6yZe3S2LYLoWkfp207PUGWInKOAdUAeLTdFJCPKMrKI-aNJq5bYooRePJTZIYaEoiyglQ2XTpHYUQK3pGQYihrPJZ6ToKxpJd1OBUjBDnIRdEcRvty_TrgW3BOUzzwh-hyj8oLqXrZoCytRP8yCbT52DeO1dVgf_FxvBcT31KEvWVd9jdbgZUkKmu046_JEw8Qoz0VCFO2hVvDwXPlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نتایج‌اولین‌دیدارهای ایران در ادوار مختلف جام جهانی به‌بهانه‌دیدار بامداد فردا با تیم ملی نیوزیلند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/23535" target="_blank">📅 20:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23534">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a3e86a106.mp4?token=MzdmYdoDjb4QBNCTeoqD0GkYTfrWd5rBdkEYt7AT7I-VPFZSw9ZNu5dYYwpcLoatR-HnS3a01Z9FZEOw_1fnwSi4VMrJutYX6ubSKeUr1CJFCTDpsbDDcn8yv_KvieeLDYkBjDuTuY1L9IzMNY0zRPeKPVdIZRoETplXDlqif3UYCJoAmGnf4_9CNEeM2MB9-SSqL6Wvybd29LhqEmV539Ul1KL-cY7MgDNo_CVPvS54Gtc2LGOFbjliNz0JIixSTk_Myd_RF7csd8SgmeNFCVds8N_SOxjsz35HRf7y6yNX9fCI1J-X952zHSprCTQ62nIuBq54FMlDfn19TXx81Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a3e86a106.mp4?token=MzdmYdoDjb4QBNCTeoqD0GkYTfrWd5rBdkEYt7AT7I-VPFZSw9ZNu5dYYwpcLoatR-HnS3a01Z9FZEOw_1fnwSi4VMrJutYX6ubSKeUr1CJFCTDpsbDDcn8yv_KvieeLDYkBjDuTuY1L9IzMNY0zRPeKPVdIZRoETplXDlqif3UYCJoAmGnf4_9CNEeM2MB9-SSqL6Wvybd29LhqEmV539Ul1KL-cY7MgDNo_CVPvS54Gtc2LGOFbjliNz0JIixSTk_Myd_RF7csd8SgmeNFCVds8N_SOxjsz35HRf7y6yNX9fCI1J-X952zHSprCTQ62nIuBq54FMlDfn19TXx81Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
بعداز پائولو دیبالا؛ دین‌هویسن دفاع رئال مادرید هم درویژه برنامه‌عادل‌فردوسی‌پور حضور پیدا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/23534" target="_blank">📅 20:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23533">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poLikZygiVCX6Wnh0Zbcn5M8AyrZStHytmZYiFYX_Pc_y84YSuul9Yd_aFXPm7zB5zSKGqC3Cbrw_N1qtmlBuwm7VMlIAsHX_LFOzz8is1Li4KTzTwAtWeBqND-Ajxw89aKk-0tmzLURMZ8jVCE_vW0EX2uQDDXYLYLMfAsHL3WOaWYf0_8lx6fN9XOWRqzgsKhu8KASSvlsrjtben7bdOEars3-UzElWrcJ4WQdb-4apITMk0UzLDJmzfXfLc5slO3GC0Nm-KydFYQwRTB7bPhslDmaC2JxYu8fay82SXTEdIZC6vY-i4W9XMbidYhZLWX7YX4PHG4YqMflPY8rIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عادل فردوسی‌پور: مشکل‌پرداخت مطالبات یاسر آسانی توسط مدیریت باشگاه استقلال برطرف شده و طبق اطلاعات دریافتی ما این بازیکن فصل اینده‌نیز با پیراهن استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/23533" target="_blank">📅 19:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23532">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEkvueTGZYa0guDtlW4Hu0oXvojMPkskcLXmmzWV5rDhjyfWhnQ14b67_SM1AQw_Ls0Lr7LiczPLuwUwOSPsWyMcic-FXvVNLi2OkbGSJAJAMMMmqC8wU6csjAT8C0QUoYgpfHaQdMZ3ofW1oT1pwDQq-ccmLIUmpB3R7VpaAmNHbvPIc4JXtvUIXVV4IrURxUElRE0MvGgeFhkNhg_g10e7AdbOaDL0S0ecWgC3i9OpBvxaZAN4zfty0xVV9KQqD_Y6BLSrDWCPlvsP7EN_nRnFkzUvvumKl2hStgQjk3fVX6JCNoAzRF10w7u4cpll3zYQusF5kC65wzGuPX-8Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رفقای‌گل‌لطفا تو این نظرسنجی که تو کانال دوم گذاشتیم شرکت کنید. اگرم دوست داشتید اونور هم داشته باشید محتوای جذابی خواهیم گذاشت.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/23532" target="_blank">📅 19:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23531">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnQAi1bPegS6jWNykF0JgLO_eyz84V5wj8l8uKC1tXnO7KnOfUbtNQ-5e0ya85shKdztBQI3VUYHoAPIMogiyWLXKmxjjjKHVtV0uupg_Pz-mrPi_A8sv72oOwEZkX-crz9p4HakLhj1tT2GFHcwkf9ErVboy5rvypLJEj2PoEQo7xlVWlpxEKORVoO4_Ch6e852fR_B5G38wU3kPfidlDVRy-2gg71anPDd-ccULhGR5ZVgEYX3lvFCzoi6-oYvenB9nLonSmOWUoFtrXqWxWGURfXrD4LR_ID5k4IlTRjMp_c5aPXs8oJN_WGK1bdOrUqyYPvlSosAnecGLMOYHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین‌نژاد، محمدقربانی،احمد نوراللهی، کسری طاهری، رضا غندی پور، مهدی قایدی محمد محبی، محمد مهدی محبی بازیکنانین‌که‌احتمال به لیگ برتر برگردن بسیار زیاده. اللهیار صیادمنش هم آفر خوبی از اروپا نگیره احتمال بازگشت…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/23531" target="_blank">📅 19:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23530">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23b2efb67a.mp4?token=sRSDQLdQS_TKT7K2-snJ-fT079ysor1Ik3eZOB79fuuMbkGESAyNdUevjYpVUNdQQtPgMKQG-hiIJpJtlufVmUBE1yVDrf8SnlXjP5Dh2XA7WbnbmtljutHLrVS8aX89PJCEHlOuF9zNV-PLsHiG05PMNgdWHitFHvzt0djP1fL7KCbW94lDdoDO34NsE24tG0U1I2d5OPv1oeylyChLYbuBVeTZLOcjFmYncpLHY9mEoepjVOS5hT2UOsK63hrkPpRWMW8_Zv4umpjZPmTv09WMaNKnnckYb16mhpXaQ1vVR4fajoP9P9uysxO-EBEgPiZXSZkQJsa5q_dO65HhuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23b2efb67a.mp4?token=sRSDQLdQS_TKT7K2-snJ-fT079ysor1Ik3eZOB79fuuMbkGESAyNdUevjYpVUNdQQtPgMKQG-hiIJpJtlufVmUBE1yVDrf8SnlXjP5Dh2XA7WbnbmtljutHLrVS8aX89PJCEHlOuF9zNV-PLsHiG05PMNgdWHitFHvzt0djP1fL7KCbW94lDdoDO34NsE24tG0U1I2d5OPv1oeylyChLYbuBVeTZLOcjFmYncpLHY9mEoepjVOS5hT2UOsK63hrkPpRWMW8_Zv4umpjZPmTv09WMaNKnnckYb16mhpXaQ1vVR4fajoP9P9uysxO-EBEgPiZXSZkQJsa5q_dO65HhuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی جالب و متفاوت‌از خرید مارک کوکوریا مدافع تیم جدید رئال مادرید توسط فلورنتینو پرز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/23530" target="_blank">📅 19:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23529">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxfD6HlSOiVkpGzkANnlOFD5X5eWe9RzWh9Fptt1nGeh8D8dZcsgRSpwaM1tiOUHwNto6paYu6BnET1xB2oBvOeb2ersQz5njs02Fayx26fdnNPLkimzx308ZI64y1HPKnlR8sEPLmrclViVr1ZNDoFoGcgWOkrQtx8bUYL_k86TGfI55lGJbTY8QrbmYJblmg62ta0WRlcXtSB-6EH11SNvim_49hOvaocAztOKxRsd5iqhQyLclnOrnxet6GUs4yqJbQhdxkcvf63JUiNJOxuTdJPrpM61oQM6tGLfaF8ymk4M0V5A-gkequyC3KBmBzUsJPfoXIS5kQXUv8n_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تایید شد...باتاخیر چندروزه باشگاه استقلال امروز صبح مطالبات معوقه یاسر آسانی رو پرداخت کرد تا مشکلی برای ادامه فعالیت ستاره آلبانیایی ها آبی پوشان پایتخت برای فصل آینده بوجود نیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/23529" target="_blank">📅 19:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23528">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIr-zISJJhGRNBWRq6j7z-Kum9mwY34Raki-s0GPyWfsKIgfvnGCXuzS0TlKsviKLWWKepLp9F2gGi2PZ4hOgh8Ual0u4BDdjterscB6eh30BoHKPofcrBC6gegOeGCFX7z7emsMGKfdHY06A3nMfe1-dR2izjYXwajHeWwn-8V2xiB2mPHDwbLiL3auX4ERJfKkifxdeEtXzX8u5aItnRkYrvdaP3cWLW1kcIjmVNa--iRDHuBB1rFCaUCTotT16xhGIps_3iYPN2RS52s67oKCT0owEJTHMYuFP9c05Nfx95LsblfIxZ3BI_x6UCrDDwBN-aZLFiKr--kMfgBQNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
بدن فوق العاده کریس رونالدو در سن 41 سالگی و آماده برای رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/23528" target="_blank">📅 18:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23527">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKDgGZBiRd8cvfGxl7CHf4zX4mbX3Q9LC9KF2rRqWmP2xkptgfU5yDLKn60kiDcTDg3gISvxP-ph6YOO91E0J5Lo_XidHn8e1KU-LTlwFwhELr1ksHh9LsmztQjkx7oLX7-YFOyd-y5DONqirQy_LK3PUFGl7MdxBb4aWHqTxmnRE9JUjcSh7K-2NolCqFyB9HpAS3wXhLX9WYO2hxbr9hoHePc2egLCTb54j-Wmy3KpKCMTinhjPZtTXtEmPMo2yENjF6UBZTvRi9kYUcbfKEaIRNy7wC94IVxhaUXpp4Xw6Cr30WPGzQRJPU7AGVjFOjC91ofJocQNR5daugI54Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
#تکمیلی؛ال‌ناسیونال: یوشکو گواردیول مدافع کروات 24 ساله منچستر سیتی با رئال مادرید به‌توافق شخصی دست یافته و حالا توافق نهایی بین دو باشگاه رئال مادرید و سیتی باقی مونده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23527" target="_blank">📅 18:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23526">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d57c883d.mp4?token=mQu__s4jT7T0qaOzuu3_h5FL4dfx1RPXP8i1kEKfHs-zzDUqr4-G0tiP12uTc0oIytprYiAluUpj-Lel2IzLuZL-iOmFKggadd0sELB9-dSbqisSFbXGeCkzXFyXn9AklL9GA2ojmmoYmC1KBpgRbMIBCn0XFKPenDmCX79oogrKbhBA2CUfjUnM3tqnZ9OUaLQcNzJ58etPOcdUPXcmu6Hi5NGWv-149ev8XpLK7uORk6l2PKvl9IYh-V2XdQBerl--J8Wv3NOnb-PQeOWJ6FyZhhX4i27j3KrDe-kraJC8xIr8bhX6czRebZNEQuXmmtg__7M54IlBOnWv_CCXAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d57c883d.mp4?token=mQu__s4jT7T0qaOzuu3_h5FL4dfx1RPXP8i1kEKfHs-zzDUqr4-G0tiP12uTc0oIytprYiAluUpj-Lel2IzLuZL-iOmFKggadd0sELB9-dSbqisSFbXGeCkzXFyXn9AklL9GA2ojmmoYmC1KBpgRbMIBCn0XFKPenDmCX79oogrKbhBA2CUfjUnM3tqnZ9OUaLQcNzJ58etPOcdUPXcmu6Hi5NGWv-149ev8XpLK7uORk6l2PKvl9IYh-V2XdQBerl--J8Wv3NOnb-PQeOWJ6FyZhhX4i27j3KrDe-kraJC8xIr8bhX6czRebZNEQuXmmtg__7M54IlBOnWv_CCXAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
برادر از 4 سال‌پیش‌تاالان‌داره مینویسه؛ سرمربی تیم‌ملی‌ژاپن با همون‌استایل خاصش همچنان میتازد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/23526" target="_blank">📅 18:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23525">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-nbenO_QxqIskf2QKi85qx5Eb506rPKunWpbq8WavMPwocmPboqFfndMO6keb1rjLZ2c4yVEwxfb-5wG2f1tb_IA2Ph05An1uKS8wS37exozMF-JfrDR7_ScnCVXtOfIMmMokaiblKzeslyWr2JqkpgNMsNX3oos0bX1LQKSvr1VCQSM4czfzxQcB_i-fClRCXQLA6VFVf0uP3qk7cXjYw0aAQEHdjE07HkYgh7CucfYL9dbzG21GT909QHYSe7pcfr9SwUP6TGvKKOX9hTOzbpqAwjehMkODAihEWRq7fIdlquuPvShK6_M7tlqHoGfeeFuO3tLW8sjSjF-wKbYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعداز پائولو دیبالا؛ دین‌هویسن دفاع رئال مادرید هم درویژه برنامه‌عادل‌فردوسی‌پور حضور پیدا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23525" target="_blank">📅 18:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23524">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bca14044.mp4?token=ZOfds2_nxORnZ3rYVSGsoyjl5zCY2xigsEP_adEeGx_V1YRStLYnjEIHkmtoPqWHRg81Zf8Z5KXvwqkZazn0tgquemVcdGfbtTgFuRnJAFwRUNtcITS0I6BonrUqCK3exT8OoKd6EiX0sfLQy1p79JrXJfRUOvzFrMOUMBdq0U1l5ARIgqB5Eehex7hBI6f7BqGsIffw_hqQqiJO9eqPynJAuzxiZFJh8j2aMsFGKHRMtekryRBEUzkymPRG53ydcWswLizQM0J_33yYpz4DZuLffgtdCHvUluMcmPerPIbGrweRt1jhSaSd8WuReS_pYz7AY-Y6TvVkgakzE6qlsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bca14044.mp4?token=ZOfds2_nxORnZ3rYVSGsoyjl5zCY2xigsEP_adEeGx_V1YRStLYnjEIHkmtoPqWHRg81Zf8Z5KXvwqkZazn0tgquemVcdGfbtTgFuRnJAFwRUNtcITS0I6BonrUqCK3exT8OoKd6EiX0sfLQy1p79JrXJfRUOvzFrMOUMBdq0U1l5ARIgqB5Eehex7hBI6f7BqGsIffw_hqQqiJO9eqPynJAuzxiZFJh8j2aMsFGKHRMtekryRBEUzkymPRG53ydcWswLizQM0J_33yYpz4DZuLffgtdCHvUluMcmPerPIbGrweRt1jhSaSd8WuReS_pYz7AY-Y6TvVkgakzE6qlsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇹🇷
آردا گولر ستاره تیم ملی ترکیه پیش از آغاز بازی با استرالیا خطاب‌به‌هم‌تیمی‌هاش: یالا ما ازشون قویتریم؛ بیاید این رو از دقیقه 1 بهشون ثابت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23524" target="_blank">📅 17:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23523">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7SqEzQzlun5vfmiGYlhgJ3OUaaY65E1dS2rFONcpcii0vLczrGp10cpb7-5SVPuh19oKX4oD4Q7VtE4Llv5V_Vhjz1UM9UXzTLVKPJdzkiaJ-vUhpTSS-wm-VLBReMu2A5oqMIzKM3mH56SdW_nNrUhqhrJl4GWyaUatcpZo62qnsDECkWRFDh48ns-g0832N8lPCNoNDVGZD88q6ccwuRmFt4VGCD97GQFFyKFwYbfNsxQF47w_uHhGWRBSrZeJMrQLCuzcBE_xtlP8xPf4PXxoBsx8rDyTSdWON7OsaQX-elLrBTxHUkzzLsLsNr0iPJ6KEu_G2WzwPmuDaDIbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23523" target="_blank">📅 17:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23522">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vk-BuEWiqlqvUpEekMzKL_a2t_kDXylWXIfU1i95FKElbVU7UaCbKtiD24GcYRaghpNITnc5r6ngDLQfY9CH-B19uzRyg0lbiA5OvbDcQ7_LdJ1ZpMuRgWI3ARiZY5vNDwlRmlROPSPgdYSHNyMClA7Hx2yDKjBhLAIXWL1mfX-dgpRP-UfzPTQvJn3K6lyNnD4fc1VYzZxj9nIvnk9J2uh0pktfDiljHxnsHL-2W_RRTRovLwp4jkBjPl19gAaYhtsn-1XtEmiFBZr7RGsGCjtZpAg6-gpT5T3SmunpM7Q1zuCmMgFKdMroTcqlqyub7Pjt68uQqkDJFpai-FNd6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23522" target="_blank">📅 17:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23521">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiuljDd4_36nRimsfwQb55t2W_kxwIvW70LHX6cxr-2eCK2F1zVNDDl4KM19DWRzbivoTFR4unViJ62BvaIZTr0pOcta8hd0uonFfyOTX1o3uF-8Y9yJ9Is7LJKqEL-rIyOBj6b-9Z9rUfUrIL-_ggxxlvmPnOlECt0M68vr8c2bFRrFNBXTA8jHM1PM-jDgBzay9-7iwGTsaT9hQdkVZmHjBltr1O9VxFHuzn_f2drXZtYK9AsovBwmXL5tgzJqgBJJhBTP3uQP4iSNjqjbJEeTL7gLK0m4YB0jvqSuqxozk9Qye_iU5vN3QCoGPb3hClxAnDrzWbiHpS9KZgG15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل‌های دیدار جذاب امشب دو تیم ملی آلمان
🆚
کوراسائو در هفته نخست رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/23521" target="_blank">📅 17:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23520">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7870ebb64.mp4?token=EsmmYgGe1VBUwZ4QZenRwz41KUuYPPcRBkmVkFYp5ZFpVKbAThne2lkhMyUmMqdpqMxL10KPUoeqjF5U_4EsKE54BwENuqnUgyxUR_2-UrmNCgY2VoMk3wpaHGagMN1jRG4J8Cyy5Mik_Ol_A0ioNTKliBaBRGJfvRLRulq3FQWlEiQCsiSz2DtE2BBObgf0RhMEIerIc-b9sG1s2LJd9zUleruWzLQCs3P_hUXaw7D5RaARGaiyL0WqpsXOHWjFDHmDzFVR_YJQNOK9EkHhmHC5OSceZOGN5Zue2bv74Fh-3pMUomuOAGnEe4cT2qmw1jP8zAbwWVwJL_SNwOLKer5WhA-d18awO0QHeLRFG3xld_exRSTcJIQQVfGd_kw_7IYgDGCSSQ4Q3gMNmuRBLkWN0ogbcaAfeW9UG0FhpIW32jBAHZbBzi_F3nU-AFZdBJy55oEbMGpYfr9iqdY-IblLw_hkM_axlcUTMEQadcJlAk4oaWsvtlrfe6KaICPxe0T-54t-bwAnPtU1iGgLiVqZIYCJGsvz3haVCfrnThWG0aw21Go3Sd50In0HT6KAFJbc8BbX12GDlNGSkZEY4o4l89LZtpCl4_60R-aDCeTfncZtVTWXHWeV0m2vyQuKkTg2Cw9daMRHR_AEv_et0EngF5MJfUpar0BugVI_Ucw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7870ebb64.mp4?token=EsmmYgGe1VBUwZ4QZenRwz41KUuYPPcRBkmVkFYp5ZFpVKbAThne2lkhMyUmMqdpqMxL10KPUoeqjF5U_4EsKE54BwENuqnUgyxUR_2-UrmNCgY2VoMk3wpaHGagMN1jRG4J8Cyy5Mik_Ol_A0ioNTKliBaBRGJfvRLRulq3FQWlEiQCsiSz2DtE2BBObgf0RhMEIerIc-b9sG1s2LJd9zUleruWzLQCs3P_hUXaw7D5RaARGaiyL0WqpsXOHWjFDHmDzFVR_YJQNOK9EkHhmHC5OSceZOGN5Zue2bv74Fh-3pMUomuOAGnEe4cT2qmw1jP8zAbwWVwJL_SNwOLKer5WhA-d18awO0QHeLRFG3xld_exRSTcJIQQVfGd_kw_7IYgDGCSSQ4Q3gMNmuRBLkWN0ogbcaAfeW9UG0FhpIW32jBAHZbBzi_F3nU-AFZdBJy55oEbMGpYfr9iqdY-IblLw_hkM_axlcUTMEQadcJlAk4oaWsvtlrfe6KaICPxe0T-54t-bwAnPtU1iGgLiVqZIYCJGsvz3haVCfrnThWG0aw21Go3Sd50In0HT6KAFJbc8BbX12GDlNGSkZEY4o4l89LZtpCl4_60R-aDCeTfncZtVTWXHWeV0m2vyQuKkTg2Cw9daMRHR_AEv_et0EngF5MJfUpar0BugVI_Ucw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
پیش بینی 4 بازی امروز و بامداد فردا رقابت‌های جام جهانی؛ ببینیم چند تاش درست از آب درمیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/23520" target="_blank">📅 17:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23519">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc271fde7.mp4?token=gfWhsRJd30sAhVUavkBAmjCW59yaBbHX8oqhc1ze_4wmnRS-hWWo-IR8Au5hHaeqqbd-2UO6NGRFoCgoJT4-MqXC1vUdWsPlHKla1IThOpilANptmqJxrXHMn57HJybNv64rKIDKS0GxfbaIn488b1Ups4FTqQv54aOCHbkxSPfEW1bkSKQNRKVMl_CiMsqJY01IzWY6pXfVQoQ6C08FLdxqdJo316AytnQdbU4h1Lb5-BLk0QwbnBsag_-qIjABoFbds5THxRTCVQtfHDY1iRL7BSIS-uENWivZT_2lQto0CbfluJvmqog6Q3pngqNmeq-MM-f946cjHnjHYxY3Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc271fde7.mp4?token=gfWhsRJd30sAhVUavkBAmjCW59yaBbHX8oqhc1ze_4wmnRS-hWWo-IR8Au5hHaeqqbd-2UO6NGRFoCgoJT4-MqXC1vUdWsPlHKla1IThOpilANptmqJxrXHMn57HJybNv64rKIDKS0GxfbaIn488b1Ups4FTqQv54aOCHbkxSPfEW1bkSKQNRKVMl_CiMsqJY01IzWY6pXfVQoQ6C08FLdxqdJo316AytnQdbU4h1Lb5-BLk0QwbnBsag_-qIjABoFbds5THxRTCVQtfHDY1iRL7BSIS-uENWivZT_2lQto0CbfluJvmqog6Q3pngqNmeq-MM-f946cjHnjHYxY3Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
تو نشست خبری شب گذشته ایران - نیوزیلند یه لحظه ارتباط مترجم با امیر قلعه نویی قطع میشه برگاش‌میریزه‌به‌مهدی‌طارمی میگه‌این داره چی میگه طارمی داره میمره از خنده‌فقط‌جلوخودش رو گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23519" target="_blank">📅 16:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23518">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9720dcdd27.mp4?token=QpAw4of-SDgAPWlpg_I-s7FN6fx9f3z9RkhTFzADEm4CWVtf6ndZ7V0Ij9b5wc4C6_GTVgUIAtAu0FIZt0oFI93z6wGIehR8xZCzMtp8ZEdrOtfeCBgbHJXEk7F3lAgb2xDFy9Zf6ZNTgP4762Buo8isr5yRQvjusJHJ0_eFpo22AvrRTSE_mZ_Uo-2oZwmb0iPMxCsq0Cv6vi-XiSdpsUjHdFBSLbMl4-xQpx-heZz-4p75eGM7Z_bRYwLkom7Ss8ndHrQ7ZE8m78rZ8LMHbIO09wmk6ptAejIqs0OleLpDoNfrqwSD5DT0GnsKzVDgtYMIHAmwCDKB2NGR6hokBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9720dcdd27.mp4?token=QpAw4of-SDgAPWlpg_I-s7FN6fx9f3z9RkhTFzADEm4CWVtf6ndZ7V0Ij9b5wc4C6_GTVgUIAtAu0FIZt0oFI93z6wGIehR8xZCzMtp8ZEdrOtfeCBgbHJXEk7F3lAgb2xDFy9Zf6ZNTgP4762Buo8isr5yRQvjusJHJ0_eFpo22AvrRTSE_mZ_Uo-2oZwmb0iPMxCsq0Cv6vi-XiSdpsUjHdFBSLbMl4-xQpx-heZz-4p75eGM7Z_bRYwLkom7Ss8ndHrQ7ZE8m78rZ8LMHbIO09wmk6ptAejIqs0OleLpDoNfrqwSD5DT0GnsKzVDgtYMIHAmwCDKB2NGR6hokBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روایت ژائو کانسلو ستاره32ساله تیم‌ملی پرتعال وباشگاه‌بارسلونا از تراژدی تلخ و سنگین زندگیش که در سال 2013 مادرش جونش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/23518" target="_blank">📅 16:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23517">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1W6_zUXMSHrqpxndpl04QlPOeW-NYwmlmm7jT7VFH4I-XY1ddgA9_UodBM9NaZPCOtUfTqcobfdpEM-MRnxOfyb7mWhR6cMWyz3cMXcMhkcxI8BbjpENsdzvv-Vplq9yIBhg8U502epya5SSezfkXxlr51adz6xP0tDy00YQpx9Ae26ulXcBc3xs5_uRWcS1cOATgXHUNUBjuggiwIh1LmtAxi1uLr4D12KXr27NGhV3FFczFJgwsXBGz3U6DBL6RVMo4Xa4o9wKvvhupsD1S3EbIwmnT-jEYr2o1eYhHBikyjyP-vhJ8pvdHwVuNaMp5l2QdjFPgLTSYx3WU1DsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک‌کوکوریابازیکن‌سابق‌چلسی‌ومحصول اکادمی بارسلونا به رئال پیوست؛ وضعیت باشگاه بارسلونا:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23517" target="_blank">📅 16:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23516">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOKaGLNnBvA4XwAOkXaZDSMIiN7mHFkLUyDelAqioJIy4g1vRHix3i8HCtCCbzS6JkPkDiBJFMRbfD5pEE5eBBmMlINmB2N_s0LJcHPztDhzoY1euqULlz85xPmnzVY7piG4h41F6fMKQ8EwWmn8aMYqLwCI2VvmQMG9bsog4lRRe4mNzituPtFuuHtyduTvocJ-Gplei0031sAg3xDJLr37JUOJccllcGLS_gbVbFPzoBHjZn9KqQBcQq2ya6dS3-b5lbM-e1f5jtVzzyJesyCvmA0p7QYKzPsAkePQU5F7AZNsa837nbDugY4VYCVTEJzEki61LXZy1eU2og02Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/23516" target="_blank">📅 16:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23515">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1jHAk6aUPfL3Boed0WQbA3CVMCUStgBIwkeBh7Rk02miUg78wVbRNuFeR5BhbpyWcERsmlVPM-HFskQklHmFQUNlriT23TOaUqIsigd1HlxO8ksEIgZ0ASycLeR6kaMw-nuMpa8iE--XhiYhGCRgUA7QYPPFlXj6dD8udWbmQDJJvt-czbYgWL1J8_47xRMt0HPbhBnPqczWjle2avsrtws93hU4KBsDAP4LH1ZIpoAALoDAZeBt9XhcHmPXYQC54XndF-9jT498UNlQJL2eAN3E74YUlb7mMO3P19CWOCVHVGypGe0mvvSty1SUhnWLaM21xBX1TrDRjmxy9jiNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23515" target="_blank">📅 16:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23514">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvRzW44_d5YsJWaztBNwtZvbo1GXVpvmmTpicb9A4uMJxDAp3vpazn1Lhk9j7xr13pRauIFxVXGQewKZr6Ky5cdh3hTb_rTjXhPOIXIJZVqKFbmKCoO5xIxa8-KMLsZkAa6gE7fBmdQ6wrsbKiNXwNW8FW6NAQoEbGkwBqrmM4TeujAxIuuhpGarRadlIjidjjW1_i3FDw8EL0fTESoxH9m966lB509lxXOyXXT_YgN5k3GMft6PJ1k1OXr9KQ7IyyoMAyd40L3LNtz4A187P5UnUb7gFrNh1RUWjTe0DmHlvgK1se7VjFdX7TKbz89SqHmIZUvTtUPPzLySso-W3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
اوسمار ویرا سرمربی پرسپولیس: بارها به مدیریت باشگاه گفتم‌که‌به‌قراردادم به این تیم پایبند هستم و به محض آروم شدن شرایط کشور به تهران برمیگردم. لیست بازیکنان‌مدنظرم‌رو‌به‌مدیریت‌دادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23514" target="_blank">📅 16:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23513">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZSn6aF9BQfhIstdqx_RAdR_oW0MvKuYlcmv_oW3ccZSnd3vTmswU4p2fW8CwbZG-nRZPGho0zQYEO0n38YRaC1s7EnJE968HHYbI9DB1eDSDBuHhx3mn8AshCXzm9QMyu4lbV3cTdoG3sewZQ41TTwWrAIFtbIKVfir-R7HUFsd47bFND28pmILBzrEk9ItDA8plNFpD-XmtLDDT7G6GBF4AequJzzVnmLpn2dcaPflHQWbsSMQxYIhfgbesuXtegwOi0mF2y7IPPc3QrlPAfcdjiwRY65CVrJOw8kfWfYLM1jOBHSuNtMMdBnNuBX0VnXbUe8lykGV6Uyq28ei4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دایانه تومازونی‌اعلام‌کرده به ازای هر گلی که برزیل توی جام جهانی بزنه، یه عکس کاملا برهنه از خودش میده بیرون و اگه برزیل قهرمان بشه، با همه بازیکنان تیم برزیل یه دور می‌خوابه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23513" target="_blank">📅 15:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23512">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6831beb90.mp4?token=p_xvxCptUcgem_3a6J_MKu85bVWGtd18pcB88asn0ygH43eMv7qfJc6K_BgbZeeYWT8te1055M7DKlR2e1JvtJ4Hwv2SPHpsJb5hVW2uhx0z6N5WKQCIc9qH-LRe6TeQhr7gzeCZGnYI_EPGWcl6qkrbQJSyQAK7UlqQ-aSSyvTVtvhQBGdNJgglExozFDyx1EfI4SZwATDTREmK9y-lra_KELZIwYad_B31KcglH2IKwJ31j-59jvJwzPwRzf8zCgvWJcQlHjcFdjS7mY2DBzV4ls2mLYROx0Fco4a7ZOPhlPTXn4U5pPzfV6tJkCrDDnGoycK_tx7QQ4hQvzj-hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6831beb90.mp4?token=p_xvxCptUcgem_3a6J_MKu85bVWGtd18pcB88asn0ygH43eMv7qfJc6K_BgbZeeYWT8te1055M7DKlR2e1JvtJ4Hwv2SPHpsJb5hVW2uhx0z6N5WKQCIc9qH-LRe6TeQhr7gzeCZGnYI_EPGWcl6qkrbQJSyQAK7UlqQ-aSSyvTVtvhQBGdNJgglExozFDyx1EfI4SZwATDTREmK9y-lra_KELZIwYad_B31KcglH2IKwJ31j-59jvJwzPwRzf8zCgvWJcQlHjcFdjS7mY2DBzV4ls2mLYROx0Fco4a7ZOPhlPTXn4U5pPzfV6tJkCrDDnGoycK_tx7QQ4hQvzj-hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
این بخش صحبت‌های ابوطالب در برنامه‌ دیشب درباره اظهارنظر رهبر کره شمالی که گفته بود عاشق لئو مسیه و دوست داره آرژانتین قهرمان شه عالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23512" target="_blank">📅 15:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23511">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea5e91b256.mp4?token=DFw6TJb6luF--kC_MwwXxMFhiI3AZwxPXlS1yRRXq-TRSLbGMpDT4To3HTaDT2k3b_5IYhOoz115XaYzS0YGLLTDD5G-g_PaqnTXcNK_EJyLpeuH-dFQ2BfKQHnTkt3RehYLbkfs9QZoofOcSaHuXISlo88GKco0CBwGoNzL_IuOAknfF3KwrZ5gzcLqhfnqaDAJ0LR3-BAhdc5LIuZM7FEf_vbGeB7rZ13vkICOqtuHtIUdBWtSVphBZMj3EXc9mI2NfT2WHj732rEqCNxgouu3xZCnmfxMTv4ihmh1a5YkbzvX9zLNm5ip5mqvcRAvuk3y2GQX6uW1kxpT79gdng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea5e91b256.mp4?token=DFw6TJb6luF--kC_MwwXxMFhiI3AZwxPXlS1yRRXq-TRSLbGMpDT4To3HTaDT2k3b_5IYhOoz115XaYzS0YGLLTDD5G-g_PaqnTXcNK_EJyLpeuH-dFQ2BfKQHnTkt3RehYLbkfs9QZoofOcSaHuXISlo88GKco0CBwGoNzL_IuOAknfF3KwrZ5gzcLqhfnqaDAJ0LR3-BAhdc5LIuZM7FEf_vbGeB7rZ13vkICOqtuHtIUdBWtSVphBZMj3EXc9mI2NfT2WHj732rEqCNxgouu3xZCnmfxMTv4ihmh1a5YkbzvX9zLNm5ip5mqvcRAvuk3y2GQX6uW1kxpT79gdng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
همسر کوکوریا مدافع‌چپ جدید تیم رئال مادرید هستن که در مصاحبه ای گفته سال‌ها رویای پیوستن شوهرش به رئال‌مادرید رو درسر داشته و حالا بسیار خوشحاله که این‌اتفاق مبارک براشون رخ داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23511" target="_blank">📅 15:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23510">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwCfCPvy4K25XZ-og4GpaBfKpvp9EOjX5tb_yetlvBQtDE7dtnBmdG5yDvIiEWUj9OTv_wJMlJhXtX_-F6HwEDF4sKR8MQaHGdtRYq9czBqmtLTbkDToIY9B-EK_8lcw1BLdX6sB1PQ-JUOimyYYKjoEgPQBt_zDvcVZNmDeD9RILHIHeIGbNX4We8e3jdTGH1utTAWSJXacgJd-onwDBid_6R81V0tawxzVAj7yLxEVQ0c5sgi3-qn_54vbPjmAQDmQb-yCfR7YBVLn7fsrc4xKW-zSOOY20HQM5PQi5BshTV2LQkI6Ol7UaLuHJYCyJTQjGH-LsUWfz-HG5roUcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رتبه‌بندی‌شادترین‌کشورهای حاضر در جام جهانی ۲۰۲۶؛ مطابق معمول ایران اون پایین های لیسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23510" target="_blank">📅 15:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23509">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSFsY46WE7K9DtHMJsccXhE108lfDJN8qIg0gg-SIQ6Bi9X7B2HHx4LNSujJnct3URNiMdEPKAbtsY3xq1yLOh3XB0-2AEDyVC7xb_qKtsJHnqW4F4AG5XLwowMJheHND64UyYnEwhqyFl_osC16CQPZE9jKRnvmscqmx6rde09tqogNIlBv_GWLg-nkgjj_aDqCGo_MfhnGOpYG2eixEM9qT0K6CG6-cs0sw9WyQzxVpOWdE3m2zRRRLp1Vo-rKdw6yYtQbsEvS13KzPaSKR95D_MZUJzFAEgNn6OE2aIWoLDMXFxujlT12szhSYtWREuRlvzodXragNq98qTDCdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ نیکو اشلوتربک مدافع ملی پوش 25 ساله بورسیا دورتموند آمادگی خود را برای عقد قرارداد پنج ساله باباشگاه رئال‌مادرید اعلام کرده و درصورت توافق دوباشگاه احتمال این انتقال زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23509" target="_blank">📅 15:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23508">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7ff7752d7.mp4?token=vL3JEG7bjEZW1-urP8ttHpHCiXUeYPZ43-eUhE751hy8VxovOiW2jIfcr4fOE-6CBU4bvuEWvcbm6doNhQHrzMSvY8gWEgIePbXktK9ZcH0uOC5lBtBx2MIDgKH25GcRrbkVw5Fq4aee2HxV8rYGbQ33fvj--lLTgFWDw5IfgYZ_M8tlcfFhEeCJ2LmOu-QAMhDxuuopp0TeKmyis53f-yJCNW95agCKOOn4yOpypzv98C3-PkUiUBvVrMl0xH7oOONrAfa1JiNfKperrCHnEfmlJ5MjZrfX53F15AgfHe0b3L-9JOdzpvgRJL789VRFw7iMyrLHPP40f57Z_vuiRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7ff7752d7.mp4?token=vL3JEG7bjEZW1-urP8ttHpHCiXUeYPZ43-eUhE751hy8VxovOiW2jIfcr4fOE-6CBU4bvuEWvcbm6doNhQHrzMSvY8gWEgIePbXktK9ZcH0uOC5lBtBx2MIDgKH25GcRrbkVw5Fq4aee2HxV8rYGbQ33fvj--lLTgFWDw5IfgYZ_M8tlcfFhEeCJ2LmOu-QAMhDxuuopp0TeKmyis53f-yJCNW95agCKOOn4yOpypzv98C3-PkUiUBvVrMl0xH7oOONrAfa1JiNfKperrCHnEfmlJ5MjZrfX53F15AgfHe0b3L-9JOdzpvgRJL789VRFw7iMyrLHPP40f57Z_vuiRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شیث‌رضایی درمصاحبه باابوطالب حسینی: همه روابطم باخانم‌هااسلامی بوده! دروغ تو کارم نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23508" target="_blank">📅 15:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23507">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0743550e2.mp4?token=DqjGC0PsO-Sxd1oqvSgpTJob6_T33R2N5Nmze5U6c_W432Zno1HQOhwsVN1M46bd92ZAYfHYgx6RTs4Pf5sgGgT_ml-FU3lfGT7EPva6mlEEESNNuY2oA8Ipe1-Ny4__hCCxg28gjGRolkPFJ_zvsGz4Ze1KdJwIAKzGDb3RhTc8L3E8WcI1Q92g3WiRlhawnFV58nIR7u17IBy6gnwlLO2WT3ffH7LiPQ9gIfHWJyH0N-55TSXoj5m1t6L2qdhks8Ih9oz4jEX6T2zTT_Eb1VHjFND-7AG5nBuCUPK8T339vk9ehkJpUTElB_ImANX518j1xG13CaQJk5y10i_85b5fgy5O2qZC30O4U1fNgs-RzhkSG8Y6tmLdeLIlH8CHXd_VUb1l7vSxwnbEYT3Nlw-_morx9x9YFDwiucn63dBd3EmMNTjB-tRBq6XHBFg9O6K1NEYS1ALHa7rK4SCWD447wrgtxwG6F4pzf8l58uvpYYahjPNHaS21ckgel7t0hHHPEgefbgU4s1iZTZ5VhycLc8wQrmP9Ejjtvfl7aD2oLGG9p7Y0_6TCdloFi4GbOH4NQ484Ih0SqxN39UZuYqDZ8tYt2-5UrqGl7y5YN-hpvHy6iAOadqxTYcZCTNrtS_qfCELnmmnvAIrkjDPAIrDYf4jH3yaCUVhkpJ_R5d8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0743550e2.mp4?token=DqjGC0PsO-Sxd1oqvSgpTJob6_T33R2N5Nmze5U6c_W432Zno1HQOhwsVN1M46bd92ZAYfHYgx6RTs4Pf5sgGgT_ml-FU3lfGT7EPva6mlEEESNNuY2oA8Ipe1-Ny4__hCCxg28gjGRolkPFJ_zvsGz4Ze1KdJwIAKzGDb3RhTc8L3E8WcI1Q92g3WiRlhawnFV58nIR7u17IBy6gnwlLO2WT3ffH7LiPQ9gIfHWJyH0N-55TSXoj5m1t6L2qdhks8Ih9oz4jEX6T2zTT_Eb1VHjFND-7AG5nBuCUPK8T339vk9ehkJpUTElB_ImANX518j1xG13CaQJk5y10i_85b5fgy5O2qZC30O4U1fNgs-RzhkSG8Y6tmLdeLIlH8CHXd_VUb1l7vSxwnbEYT3Nlw-_morx9x9YFDwiucn63dBd3EmMNTjB-tRBq6XHBFg9O6K1NEYS1ALHa7rK4SCWD447wrgtxwG6F4pzf8l58uvpYYahjPNHaS21ckgel7t0hHHPEgefbgU4s1iZTZ5VhycLc8wQrmP9Ejjtvfl7aD2oLGG9p7Y0_6TCdloFi4GbOH4NQ484Ih0SqxN39UZuYqDZ8tYt2-5UrqGl7y5YN-hpvHy6iAOadqxTYcZCTNrtS_qfCELnmmnvAIrkjDPAIrDYf4jH3yaCUVhkpJ_R5d8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی زلاتان و هانری، اسپید رو دست میندازند؛ این دلقک نمیدونه ایبرا خودش ختم این کاراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23507" target="_blank">📅 14:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23506">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_8FWKM2Z5cekxPVXCHvpRZUj_T2gc2dvFrwXKwkaVq5r1gWQRdSYYV5alEsoUWgKoxlfRjQNVYU6WEaEcWjvXiqSyPoOTBaaleF4z-2pRrGB6OgJKs6Ai1V_pG1KnF6iTUbaM7SvG9EOjPDy5yrzeytoarlo6uRO1-Gc8g635FZED7CBcGME9F6ileYWDdOk7LHJjnyNz8cMsF5bJLhK9CKGF2q1aXwDD-LHWLM7EDK-0YGFeyrvoY5ZEZsZbI3lCtXGA7hL73VBGyfjZBTu90Pa9R1TAubxK-IfYcoPDRlbBfzskeZ18Qoass7AKaQZw1SBvxP_vxZlw0PyqJ-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ نماینده کسری طاهری تا ساعتی دیگر بامدیریت باشگاه پرسپولیس در محلی خارج از ساختمان باشگاه‌جلسه‌ای برگزار خواهد کرد تا تکلیف نهایی این‌مهاجم‌با سرخپوشان‌پایتخت مشخص شود.
‼️
آخرشب نتیجه نهایی جلسه رو خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23506" target="_blank">📅 14:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23505">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dqz7m9l78AId_8qjJnQrMCAdN2OKtcd9sOOIRCAwke_33ncW-71ynOYmKBfhnG6PwSvFahzeXXvhWJ3ZNH6J-LIsxF-5SVhgfAN7Vssr-nwY4aXJaZB9JCR0R4S08NcOnDtfOTDvIIgH_v2ek8Mis8Aw_2wGiuSiVuIQYBrHBMwA-1In6YLOzfFjxxG-3WeVzepvfAhlXdAWxcVtJeqVpfSNEe962mNPJaxzPJ514ZWPAu49HTRxxLdVCjtLG7SZft1d4tJK3CJ3u0V-XuTfzsXtgptY55PKdoJU5d6tj3F0DJSUw2B3hobbcSxKhuMfUoGj64Vq25zCRYpEw2ndMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خرید غافلگیر کننده کهکشانی‌ها؛ مارک کوکوریا مدافع چپ تیم ملی اسپانیا و باشگاه چلسی با عقد قرار دادی پنج ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23505" target="_blank">📅 14:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23504">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358a407b96.mp4?token=d9sUX9txbKxU_aIIVWpl5gVo_zzbKt5U8ZnZG0lGHaQO1mNDbWk-vCz-0c2vHjIH9r6oS1D_029N4acTeCJJkyrn7TLOieaAWAXmgRBeK7L6_IGfMOS_j0mW8Gijllfow21x33CTDV7xzak82MkbseAZdcfNkd6ibSv9Zja-HEJN1d2ph78sR0cqynbAicR0r5FUPN9W4sKatxBuv795Gnpd-Biwfz-vyZhBKX2EUSk4y2KokmiIG6cpLVV-XVBGICM5vrYDHm7IwW5ESzDmoTX7e25f6TtMIVrnXpO9ruNBQD3gxKFvbnYfj08kYVH1u7LRWAKUFpWEAxb7i8EWNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358a407b96.mp4?token=d9sUX9txbKxU_aIIVWpl5gVo_zzbKt5U8ZnZG0lGHaQO1mNDbWk-vCz-0c2vHjIH9r6oS1D_029N4acTeCJJkyrn7TLOieaAWAXmgRBeK7L6_IGfMOS_j0mW8Gijllfow21x33CTDV7xzak82MkbseAZdcfNkd6ibSv9Zja-HEJN1d2ph78sR0cqynbAicR0r5FUPN9W4sKatxBuv795Gnpd-Biwfz-vyZhBKX2EUSk4y2KokmiIG6cpLVV-XVBGICM5vrYDHm7IwW5ESzDmoTX7e25f6TtMIVrnXpO9ruNBQD3gxKFvbnYfj08kYVH1u7LRWAKUFpWEAxb7i8EWNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
احسان‌محمدی‌مدیرکمیته‌مسئولیت‌های اجتماعی می‌گوید بخاطر اتفاقات سال 1388؛ تیم ملی فوتبال ایران دیگر در هیچ مسابقه‌ای سبز نمی‌پوشد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23504" target="_blank">📅 14:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23503">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PTf4j7M-kHv3oIrJ6wb0ZCKT-YMy-zukXXfDOFWzRY8GsTsSnZWK3eYl8KdH8jGj25yZOkpmyOrWvAIO5RNOQG9A7zyPy_h1DorT5hWIsoGCAYZwQLN0875eQ3asPlvxh8Odw5Cvsmq81H5H_AhlNuU5LspGoPhRqBwHytSjmR33i6f0GjC9Vxrt1OD_PXEfcwg-SlnpG33TpszFVPdo1pzG2hn56i-QPO2lMquRP6iIhWhbCSep7KKTCaTeAcIUk6Y7KjEv0qLxzWeUofg0GG0SR0n7sIapKabtVKmWH0msjh4FlH5z1eAXdBAbGTP-7vI_e4G0tr-3I5kFMoU3KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی های جذاااب
جام جهانی فوتبال
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
⚽️
🔥
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
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای،مطمئن و درکلاس جهانی پیشبینی کنید!
برای ورود بسایت فیلترشکن خود را خاموش کنید!
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
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23503" target="_blank">📅 14:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23502">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d283cc080.mp4?token=fc_ZXJLvS5al-GZHUwniYXYltltdplMOLaSsWyQTGhLTVnEUIglVik_0luj8QFiU1nDdLRNpHnrRitqiY703wTW3lRo4ht_-4GseqQibpTwHtUbhKmSrNWifdGHPzZ0B5Io60N3KiHiUhr5s3FrJqaOMwsmn1xWIpf6GFD7cFdQIJJHvetK9dJWdHvmTxEhGSUR6nvS4SGDCrJGGiom0FEsqJ9xKs3aR1T_atBgToelfw6R95VWQBJTcTeBGOJ6V3uQyR6pW_x3hbwgATBfv0THUbsJSzGBLz_285-ZLZN9Mt9CdkAo3Empw2YjXUUAT_Hk15Ms1IBxmdmPl1kLXUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d283cc080.mp4?token=fc_ZXJLvS5al-GZHUwniYXYltltdplMOLaSsWyQTGhLTVnEUIglVik_0luj8QFiU1nDdLRNpHnrRitqiY703wTW3lRo4ht_-4GseqQibpTwHtUbhKmSrNWifdGHPzZ0B5Io60N3KiHiUhr5s3FrJqaOMwsmn1xWIpf6GFD7cFdQIJJHvetK9dJWdHvmTxEhGSUR6nvS4SGDCrJGGiom0FEsqJ9xKs3aR1T_atBgToelfw6R95VWQBJTcTeBGOJ6V3uQyR6pW_x3hbwgATBfv0THUbsJSzGBLz_285-ZLZN9Mt9CdkAo3Empw2YjXUUAT_Hk15Ms1IBxmdmPl1kLXUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
فوتبال‌فراتر از یک‌ورزش؛
بازیکنان‌آلمان برای دل گرمی دادن به‌حریف‌به‌سمت آنهارفتند و از تلاششان قدردانی کردند. کوراسائو باوجود شکست، اولین گل تاریخ خود درجام‌جهانی را به ثمر رساند و حضورش دراین‌رقابت‌ها را به یک دستاورد تاریخی تبدیل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23502" target="_blank">📅 13:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23501">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YviEv75x1XmuZOJwl3Z-GDLqqji1RkI0Q0QlWa-21PlzJ8LOsnW0F5iaPTZxuKNUIR-2b8S2WHAQmvVEzmtn9LOPxCLUspc7syx4-O-eXav6fARvxO6snwNaPkwBnqUGm1rDDXF5z4nBKUwpzGkpkXtO5ZCYB3VCvGFhc-knaPsqHAGUvU44UY73zN7c6cO9xV_86yXM2XCRtc76mVVSs2J7MHxzfvWXOFAjcnlgBVERsGYS_MjonkcespmYhzGryD7YDZqdL7kITY9ZwFmexIo8fVxKeokJQErqJK_xaoluWAncDY94YsFH7eP9ZHhuPpUevbLE-x02D6PfJh4bKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به‌بهانه‌عقدقرارداداحتمالی آموریم بامیلان یادی کنیم از این‌توییتر‌که نوشته:زنان باقاعدگی،بارداری و یائسگی دست و پنجه نرم می‌کنن، مردا چی؟ یکی از فن‌های یونایتد هم گفته: ترکیب 343 روبن آموریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23501" target="_blank">📅 13:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23500">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxCQoIQEoiwzsIf7C_rEJ_snRLjAhE4YhO6Mf8qj4f3j3_mAk9_dujZ0GkI-p1FYvfvlrntV45Y8HK2ThspA32gZrCBcpXWfsHGR01aK9vfvLtwKTDf5vSG4EvazJT8TEXPe028Rt8-tb8dwUzB2QkAGqWGCMhccgdTOPMCTLL7K_IDXKjsjjsvkO_SqavgHt4jZN_qBUtbjERGVOlFAExG2efzMMwZV61BxbfiisTlmYeN7D8n4BOOYsqAfU4Jq8MPRHRXW9FtezwekCX-zFGNBUxjaQFxiY1mJWaFUeQo-p58U9209hV-pnxOLwglaX_u_EaoXBsdLNGVfl3K86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیفا درسایت‌خود رسما اعلام‌کرده که تا به امروز 19 هزار نفر از زنان سه کشور میزبان باردار شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23500" target="_blank">📅 13:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23499">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165e001c95.mp4?token=B3A6M32qRJ1k_OGJcnLsBzztW8St1gtxoo_cNANrN32TnuRJsf-byUDbpNF9uZwIo0hjRpzLs7OWm4YVeJ_C1nJLU1FRLcu1_SY9xCSm_W8NY7kNGm687-8Hxd9ZLZCmn41mNbdkpOI5i9NdoX1GANB_JFUFIgzo4Ok2fo69Dyu6SiKpajJGLLOC4qjpAtN-gV-HInpvlI1cm5fazvyLKCkxHTJbN2ZJqjrbQqS7mos837TUl7vXdhvoDSo0HKKQGwKfjHH8d3VgMrmKGs66q0DgKjMdpHeHijMYIUXzF5MN0KmG8kYU9swoqH5Lz8TtzzSd6zatsqO7_Xonfwx5xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165e001c95.mp4?token=B3A6M32qRJ1k_OGJcnLsBzztW8St1gtxoo_cNANrN32TnuRJsf-byUDbpNF9uZwIo0hjRpzLs7OWm4YVeJ_C1nJLU1FRLcu1_SY9xCSm_W8NY7kNGm687-8Hxd9ZLZCmn41mNbdkpOI5i9NdoX1GANB_JFUFIgzo4Ok2fo69Dyu6SiKpajJGLLOC4qjpAtN-gV-HInpvlI1cm5fazvyLKCkxHTJbN2ZJqjrbQqS7mos837TUl7vXdhvoDSo0HKKQGwKfjHH8d3VgMrmKGs66q0DgKjMdpHeHijMYIUXzF5MN0KmG8kYU9swoqH5Lz8TtzzSd6zatsqO7_Xonfwx5xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد سیانکی گزارشگر:
امیرمحمد رزاقی نیا هافبک ملی پوش تیم استقلال که الان مسافر جام جهانی شده رو من کشف کردم و به فوتبال اوردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23499" target="_blank">📅 13:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23498">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUd5eDsZzsZOXcTAgOuCHS_aXI6EJPhYwfuOYRSDuPulkulB9Qd0KR3u-KtRQy0A2Sx2yNOa9GvViIzs_ekFtXn6Sxji7L1xwV8QiZ6MzdbIKYyXWjVB-HSWid5T20GuKlut_AAadUS5RxbNZQskMLIIeaLOGMwhEvqsG4WUX3L4JTnrb4g9Z5W-G1NoFjozAfYX6pfaTf-6gvKB3KIVBsDks5hxQCDFP5WjLYCptCJoPt3yE5622ZrhBKqJ29JHvSb07hxGbRe2XXjqd59aZLFcipobV2PYWfXXgSImXXZIAN7YGcqOzuZSzLOH45dCN0XE4Shmkt6hgJrSmDL-BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
#نقل‌انتقالات
|اسماعیل‌ سایبری هافبک تهاجمی جوان مراکش‌باعقدقراردادی 5 ساله به بایرن مونیخ پیوست. هزینه انتقال 55 میلیون یورو اعلام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23498" target="_blank">📅 12:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23497">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXUTzxLjzGSQG2Mhprma1FSBN4zqRgBUg58wlAD8hajXBZyjx8k66tnPz3uVleCeYbdJhbj-bS1Rss-3qgCHALmlXF3g36w_hJMSRMutTCNlVAQ-FJHPMqXBktYz2yDYuzULYfEcdd1zadf8tuUuzXqBC95KUBJUf-DUXGCkGW9lXLY8uYMyAqEeU7iPzuyOlTvY2PVC5QpDb8PscnqP3zmEAdSkehZYIRtnJCBSGeJWUpO8DRUzdvjYrp_Qw71fLdkju2_GMk6bmIJTMDjAiQWaJfv7ilwW35XEG0Br9RA6_F60Vh3oAin2-4xje2stzbu7E0Orjz7bW2IzuHjAQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رفقای‌گل‌لطفا تو این
نظرسنجی
که تو کانال دوم گذاشتیم شرکت کنید. اگرم دوست داشتید اونور هم داشته باشید محتوای جذابی خواهیم گذاشت.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23497" target="_blank">📅 12:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23496">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-WK9AcCZw8EiCJAkZelH6uIZlIyBpUPNrFMeDYoWwReIjTm8XIC9pqq_ZVcsuwd6F5BgJGqOboCnJHnlQXvDZMc8b2smPyrG9WyIehdKwNIEpVC__YKkotJUc_XkaQKY_iDedmKvUKDqCk3v2uyehaEWaphBfsk-VfuhhRI_iKG1PgYwO2QhUYktxSd193U0LafrLwNZhoVZD91CSwGnqUFMUgHdtS6hZPlVlNjzdv-5YlFVNS88Q1fLMTFq4egbg8kBtG7Qxbo2I9FfH8iVTv0ftP12aYRLIjr0k7RzOSovjj_QA2_RrKn_6iKaY8OYtGoryBE5rjTE0Z_uqkg2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
تو نشست خبری شب گذشته ایران - نیوزیلند یه لحظه ارتباط مترجم با امیر قلعه نویی قطع میشه برگاش‌میریزه‌به‌مهدی‌طارمی میگه‌این داره چی میگه طارمی داره میمره از خنده‌فقط‌جلوخودش رو گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23496" target="_blank">📅 12:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23495">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2c7e5ef1.mp4?token=TgAN0dQVZGkrbq4wOSiFyuIQjv46PzTNUCTHlJMZhkntxGTaPc14qU93Lytw001cDBWAJGqBa3lseC52wAcTyD2WBHW5q_MtV77RLUie_hH729KYz1ekKWIV07b7iq8Do10TwJ4wKOEmc3G_X_d1vcfGJtOWQZjaImG_rsVMV_xFKEwdzVJDbDlt7IeRFwCpiF72hJkdayaEWnBVKNeoPuxciXFRngmVUfWSmEu2FKcIXpIs41A5bfxbv2PbHfpLPttBHw9ATOtG97zhVySx9Y9VX0wj8BDu-KV-owxdMo5IwKr0r58Kv2ylRq2UmJHVViu81X8FtfvY-vzb2if3yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2c7e5ef1.mp4?token=TgAN0dQVZGkrbq4wOSiFyuIQjv46PzTNUCTHlJMZhkntxGTaPc14qU93Lytw001cDBWAJGqBa3lseC52wAcTyD2WBHW5q_MtV77RLUie_hH729KYz1ekKWIV07b7iq8Do10TwJ4wKOEmc3G_X_d1vcfGJtOWQZjaImG_rsVMV_xFKEwdzVJDbDlt7IeRFwCpiF72hJkdayaEWnBVKNeoPuxciXFRngmVUfWSmEu2FKcIXpIs41A5bfxbv2PbHfpLPttBHw9ATOtG97zhVySx9Y9VX0wj8BDu-KV-owxdMo5IwKr0r58Kv2ylRq2UmJHVViu81X8FtfvY-vzb2if3yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ از آغاز کار ماتادورها در جام‌جهانی تا دوئل تماشایی یاران دیبروینه و صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23495" target="_blank">📅 12:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23494">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKbaDW2NbO28v1aHO14MY9YA1LpQc90ETpEs_OQEWQMSkCAPLM4_Ul9cdUVzJ83wENYucldq0dE4t1m6oFhL10zhUs4ePVytb25eoClblIVWDfMKHQG-xiK_If8oxkQGiyJ5aMRtyE1I05vJSx8OwNJy5BKR_DHQnlbFv_WU5eXkdBEQljGiCQ8UPdFksBCrcDIO9cyT6Ko1anHn1Zxct8oyJMx9RbxYz4gZ1vnpNRjrcwnBWy8LB-NiBfsuVr1nem2uD_AbMXdd9xOLyXHo1ex3I6RiSGhMRsl8WbopRcj1EgNvTbcznSlJR0FKxj63cqYs1NdPRrst5vUBZGfUoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اروپا هنوز راه شکست دادن ژاپن را پیدا نکرده! سامورایی‌های آبی ازسال ۲۰۱۹ تاکنون مقابل تیم‌های اروپایی شکست‌نخورده‌اند؛ از آلمان و اسپانیا گرفته تاانگلیس و هلند. بزودی تماس سرمربیان بزرگ تیم‌ های اروپایی با ژنرال برای آموزش راه شکست ژاپن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23494" target="_blank">📅 11:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23493">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWbphzP3__Qq5Y5zvxL8qj4x4_egyKZBNPdgAz4OPeCMHuJm7JI3p8JaruQ07DBnWtYc8gpaHlCWycya-X_wajfP06GeEUlMRnM3DKgrFFdE-h9fuLkTXDLLV5YmY6xa1thnJo8kP4kZyLb-mpGoF_cuo81uI_1KSCAQFW4EtvpRytiWUPxC1TB6ao3JZfEujbtAAWXHXfPwBY6y-ATU1jw-oYz-eB4Kf4qmAdzMoziKCjcxOBk_ek17xwKGigJ8lRE-lF5TX1G1xQ9Ov4OzI47ZHq8I1UIsBmxjPPTz9whzcRwVCQTWjXWZUX8W8AlU1Qqbv0Rm-q5J3U-HU21vmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
طبق اخبار دریافتی پرشیانا؛ چهار باشگاه فولاد، استقلال،ملوان و خیبر باارسال‌نامه‌ای‌به سازمان لیگ خواستار برگزاری رقابت‌های جام حذفی بعد از اتمام جام‌جهانی‌بصورت‌فشرده در دو هفته اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23493" target="_blank">📅 11:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23492">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_poyb5oxvT1PA-gw_HHiCF1Vaysuapi3BIOSgWyebEPTDGbe1bDTXGN2PP5sYxUopOw2UOiaQV-2cS5OZ2Xl4yc3ppMtucav3ars1aOaKHaeld9q5OlpfMShGm6EpMamzBodTThqejPFhIgcDhoPVAx2oRO2yTBnL8zPNSQH-BX8P5uKjhAkTvEiVwYIKmSYbYIKAx1FHqNjlF3xuVzcp_-MZWejTT5Sm1lt28VCRVNkvRMIFuLqdA-qojK9Ryf_UeGKLy24bOHyoVRANlcuzZ28qepKaUM_W1SCRzDHHf6uzD_hnbrbJEZQZd7cqIJpmEf9I1uHKPPIjDTI0P4vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ نماینده کسری طاهری تا ساعتی دیگر بامدیریت باشگاه پرسپولیس در محلی خارج از ساختمان باشگاه‌جلسه‌ای برگزار خواهد کرد تا تکلیف نهایی این‌مهاجم‌با سرخپوشان‌پایتخت مشخص شود.
‼️
آخرشب نتیجه نهایی جلسه رو خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23492" target="_blank">📅 10:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23491">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5ti58eesorDv5EmHgDFVX00Ea4ZfG6u4dv6DB6aYuYHNt3QSqWG9ZdaG0auCAYaidb4jw8rdCNdi-32gATU6BoG8nNmmqI6ahQqJEnGiqGIT4c58KFLymbrxY5JUAoRizCZ029gSCxJ4aycuT4Dk3NnGGTouel1VY8JkNjd6ASMwkC4r8JM71Poip6kP6svaVM-0-6UsRRdTq76FGbHwkCt5GHiITeDlHHYK_pROijYeERVsiMKxc3sD3w6cgG8ORMxxWp4_tKv1th0EuZcvMT6lDohdfqUxnrb_MrWBdhfN8jJjjDoF6qKlm9lna3sbQv1vWj7gxheLMJHI0oZLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23491" target="_blank">📅 09:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23490">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQ7hLADVgXo3z5C4oScRyVdxUeVHTSXl5p4ITLmMaihWUviidCNxMMK3FmrK5i55wRc6QcvhUVekOMyF6FNRW6H1OF1lKmyMNGCaU4yIMa23HJpxBZ6FpPV2bTtYUWLnngbbpZowHUHokAkR2Q6AT6S_OV7_Qaai2vFj4B6322HpMo6u_TpQS3ZlRd6BPfqr1JBHLjSZ4rW4pI7Smjw5t2yG93cyxsZWxfbL84I9tpR3xcGBq9CiPX99hevb1rVSiUexHmlYr6TNSXg6K7KjN5fok4wLi0LV4PQvawkkhX9cad3cNXbbtiEH_O9F78ETSbzHVHVfegY2hESBiK41gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
طبق شنیده‌های پرشیانا؛ مدیر برنامه کسری طاهری فرداصبح‌و‌عصر بامدیریت دو تیم استقلال و پرسپولیس جلسه‌ای مهم برگزار خواهد کرد تا مقصد نهایی کسریِ 19 ساله برای فصل بعد مشخص شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23490" target="_blank">📅 09:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23489">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f1c70aec3.mp4?token=k1Eo-PvGOKD_nIAaHe6mCiWF7QPcA-aIwLHgGeB5fwGKwIcoNudT9DuA_hITuqYl-mbSt4sOTxkX2c7NrxW4Y7jRgVIIwbYJN09Uj4TyyJVV6bB-C4AubnRzhJ7alsOb74SYuzexGrBtzAGqSOE8fnHhjiAiIWWN2J7eqBYGnhSgoD-itRUH8XM2dZsjzIfC_8Ju90nRVSNcRf8siv6n64vpgA-KGkkiC6_zs3v1eoud3L2Y_werGNDqAJFIaxUDV_WsjKkzsldMrBpyMcz05XF3k9_h5Ryn9xI5C6xWZXGXqRK9QVGQjpKG0vZ7uLd8IymL_PYO8MPvToMEkIsjXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f1c70aec3.mp4?token=k1Eo-PvGOKD_nIAaHe6mCiWF7QPcA-aIwLHgGeB5fwGKwIcoNudT9DuA_hITuqYl-mbSt4sOTxkX2c7NrxW4Y7jRgVIIwbYJN09Uj4TyyJVV6bB-C4AubnRzhJ7alsOb74SYuzexGrBtzAGqSOE8fnHhjiAiIWWN2J7eqBYGnhSgoD-itRUH8XM2dZsjzIfC_8Ju90nRVSNcRf8siv6n64vpgA-KGkkiC6_zs3v1eoud3L2Y_werGNDqAJFIaxUDV_WsjKkzsldMrBpyMcz05XF3k9_h5Ryn9xI5C6xWZXGXqRK9QVGQjpKG0vZ7uLd8IymL_PYO8MPvToMEkIsjXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
مهمون‌های ویژه بازی هفته نخست آمریکا مقابل پاراگوئه در رقابت‌های جام جهانی 2026 رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23489" target="_blank">📅 09:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23488">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f0fa31c5.mp4?token=ESbxcIGn4RS9mwLxedhkaTI12kAMkORorzgYs4UG5939c0nfwSIM7bBOuLzorzJ6rpawz0Pm32GjuCU0zaFH5bOnLaoafWvpq5_avhIvkogTA9G6Vbgrbw0PJgung-l2mAisAOaxUseznckeLBpIgRDWcxCW7zLHe16OY0SwEGpVeSDvzQv2sFMPKnbYfsUXVLIXH6knbDpaw7eRXxxKwr7GJFT143NkUfUnhzf4kZ3fdTq4jSm3VMinQYDFaUESgbkDvL6mLajEnwBV1Oj6cpTvnH9zDM3YdYp2PNtIKnJQdlcDhmtnH0ZZm01svt-oy8ZvZiTxEiOD3-vKMId0Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f0fa31c5.mp4?token=ESbxcIGn4RS9mwLxedhkaTI12kAMkORorzgYs4UG5939c0nfwSIM7bBOuLzorzJ6rpawz0Pm32GjuCU0zaFH5bOnLaoafWvpq5_avhIvkogTA9G6Vbgrbw0PJgung-l2mAisAOaxUseznckeLBpIgRDWcxCW7zLHe16OY0SwEGpVeSDvzQv2sFMPKnbYfsUXVLIXH6knbDpaw7eRXxxKwr7GJFT143NkUfUnhzf4kZ3fdTq4jSm3VMinQYDFaUESgbkDvL6mLajEnwBV1Oj6cpTvnH9zDM3YdYp2PNtIKnJQdlcDhmtnH0ZZm01svt-oy8ZvZiTxEiOD3-vKMId0Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌محمدسیانکی‌درباره‌درآمد گزارشگری؛ سیانکی: هر ۶ ماه یک‌بار ۴ میلیون‌برام واریز میشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23488" target="_blank">📅 09:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23486">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZCX6c31-AOBiMxRp_S0vNsN8KPHQ6h7LtOoDXz8jIUXgdBcxtBQEm0KsY8NvGY0KFdyBi3lPIyvuvEOftYcBsbGFEkirfW2CSTx3k5NSNJ9XLA5wFisekJnwA5ozaYx8sGHydCUopPSsZwPGf6RhD8eD-5WYQh6q6ErGMv36Mw2BCe-73dhdMAg3MQ2rTUuV2dfht-mhXswhOd7WoUYn9fj8a0hoLBkPAaMeCMsf1eugTiIUb73upnsziLGTdBb7VLvix6SQwAtpZypc_5pJZyep0gWgVfvX60EvUg2rc7lRqPtGGZzJxdWCpoQGFxaNWgc_yXNLRx6CHlXZtVQFWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3i-AJwkFN0W7-yJwauq0c8I8sOu4qZeKo5xYQj3vr-cJsdNs6oayfekzer86Rq6sphDXvyolapp3Rv8uA1NwNgoGeQeNJIH4etW-IfmTc_AP11iS9PhjQct-RPst8C0zpoBQYGlyGy9chewPen7MXi0Z0I1208W3O0ivr5xDYpgMZyx4K1bjo8r4DAK8G4JWiPC3xQLtpTBfvrr75AgYHCJKoHgL1sJm6Z9SViH3J9Ub7mCCKPhT361wY6Yj-Le6Ez7JHGxp9lsZBGlM4Yc4kswOtekstYvx7eY7fX2ZAyOtUkvhBLnSEM0Gd8MMDkhlfb_vrdmK_BJsPFNKi-vyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ از آغاز کار ماتادورها در جام‌جهانی تا دوئل تماشایی یاران دیبروینه و صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23486" target="_blank">📅 09:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23484">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiWvvU9GKuQESUKyXwq1rzZzB4KbfpmmP4d1K-y8gzkAI49IYIYWb3911HwXBb7HoSckZ3MyuRG8_0_rl9nFwclvWJOfYkqmZRApKr3-texBoWWNYbvUZFLU-D6iwSVcCkc_oCHGEXCCvvA5SzY1ZSCbYYCooqxhvn8NycauWmub0aD9-LiPbo_HRIAbF4uzYefBkpx2WZyKNLxo4EeBs2ZibG0TbEQ4T8HfT8mBSZobuBY_of27JjbvjQnY6HDFgJBEjNnkomv8KMzOqT6fgyP0Wi1_aX4Svg3MTkwtYO3bpRn9wYM0ZMlMBSes0mM8ao57FeHo8BFQ2J1sENbgWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
هفته‌چهارم‌لیگ‌ملت‌های‌والیبال؛ کامل شاگردان روبرتو پیاتزا کامل نشد؛ سومین شکست ایرانی‌ها در لیگ ملت‌های والیبال در چهارمین بازی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23484" target="_blank">📅 03:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23483">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkvmZhRSJhmGjzDNNMpOS-k5RrW7lMDB9I5DdaDRntRSToTjeLT9tFNIz4ENUYdwsp0LjglGeT2kJvCQ-LsGxY49hrAN6Iz2jtQd0hSVcazoGkZrB6x9G500m_w8XH-Y3eig7qLHGua1VEjLG5DSZ5AMuamXfyuMOow6g0eDGqlkyoqIYWIkhU8VsCLXk0240wzm9yY6eCbcP2cAwIPhVCwO0uZbaoGIgChK91XG72RjBD12hloRolTsm2G_0qELVxuLvuR6MDCdDw0-urMeWWA6jEwZOBBJEKocrkmBI1WsRisAocuQLTOiqaGAwX9048OOn05EviD-59KEnpiofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نماینده انزو فرناندز به سران رئال اعلام کرده که این ستاره آرژانتینی بسیار علاقمند به پیوستن به‌این‌تیمه و حتی‌حاضره دستمزدش کاهش دهد تا بعد جام جهانی شاگرد مورینیو شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23483" target="_blank">📅 02:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23482">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVe0VKNu_fGp3BlK1YeFDblVBGoTFcSE13FXQF_0jbcu3ZpeL266uPtvtZXalphListTd0EPQQfPB-rNmVk4UoglkfYgakzh4FiSfQEDiR-GFppFxSPgfPyIiiehvF8C3c6dAoAenAXIl43lDaxRryXdyaH1YvID3TwURc0kxpZW8QLuCqaM0szNBH3VwLV1ZRhgq0Ht7BpyL4gTLmwuhiGUpY4KOZgZAHxYyfz4mvpz44xpvrI6ybd5KLexLHSL9e3U_bvZE4q6jjCWDHb9ZPuVbrcnsUPNiycQOInybzS150mJTtqwav35wDvr87dosiTiISLHq8MoqiSAA5Zkmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف لاله‌ های نارنجی مقابل سامورایی‌ها در گام اول رقابت ها؛ نماینده آسیا به شاگردان کومان باجی نداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23482" target="_blank">📅 02:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23481">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hG3MBtJ-Bh_xUEgrPUGyMdW6paCmUwNLx3l5xppOovBn7a_4BbdVA22kAcItkzhuwjgwOrHlHS4q7jA1MfYSSP8dCU03Du6pA14mk7u51VlWC4p4trv3XgMVWlF0BxiQT2HrRU8Jf-Jup7iTP-OJv5lMwqOED9uJOc3DmE1kK0dBqqt7nySVMFMvXbuLG2XBIXS3Yyo5EDRtKswgjl6EY8jkUWSHJfsrBIdHggu2Vf4PfhIqwVcQ5x3Kk4_QjVsh1vfXkZWBmjgqOEklA7bAGBflZ4-drlJ7t4Xd2fCLx9_gZt88FhQroylJWuvGZ2EZ_8nxxVaTsE45uqBOlmaFSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از آغاز کار ماتادورها در جام‌جهانی تا دوئل تماشایی یاران دیبروینه و صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23481" target="_blank">📅 01:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23480">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMTLwV8xB3a9jdGqyYznnAvLFpyzUwvD2Siov0SERy6EMftAe1wVSNqGgxADv_Qj_3NQCdL68hyT6s5053mxpycPWoedJMowh-vzyDDwl59Wu2x8NXnIe_KTsyOki7qDy9Aa9oN-NkZXLT-g8t_9ArsODlowFfsKnSdHfUqCkq5tUgtxCHCgDYSbWOjwUrw7Zy76VdsW16ariwjkgbvG5GFB_lRjDpOLM0Wil6xepUv-UNGfaYq7Y1KIKhCNwSATcem1DbGZYRdME-dUPjzDR8xfZ_yOeYvu0bD8ikv_xyVBob8RNJOm-0lod_Jp35aKxd5akb3sk4sKQ0OtePmsNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
‌جشنواره‌گل‌ژرمن‌ها درشب دبل هاورتز و تقسیم‌امتیازات درجدال هلند
🆚
ژاپن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23480" target="_blank">📅 01:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23479">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9b859a0a.mp4?token=pdajCq9PBfODZwMf7d7-LKjYbPRW9kTFgypRfXY-WlmHh84DEqUz0Oc7hRsmjUb0F_2z5jkaOUoyTVxHKahuR7zlYwhMkeXrF5jZ3BSIsnUF_Ft4v-e8A_1Gb-3HOwlqzvhUT-G2n9W-u4zib4U5QbvorKXCB_kpsDS4icAIGbzewueqHyOzcWafc1f8sHyL-vG9flV3F4zaazP658ni1AXyKhnimjRofsUPPUrEwqPxvfKZuZaEXpQWFnAeTlua3Ji55Dw1Td-R0n41u3R_RFh5xgT8nGk0B8Wlfy57AvHe5n6jGxaLtmhSba7yPF_mqXiSIb-TETbWeMY0eHLNHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9b859a0a.mp4?token=pdajCq9PBfODZwMf7d7-LKjYbPRW9kTFgypRfXY-WlmHh84DEqUz0Oc7hRsmjUb0F_2z5jkaOUoyTVxHKahuR7zlYwhMkeXrF5jZ3BSIsnUF_Ft4v-e8A_1Gb-3HOwlqzvhUT-G2n9W-u4zib4U5QbvorKXCB_kpsDS4icAIGbzewueqHyOzcWafc1f8sHyL-vG9flV3F4zaazP658ni1AXyKhnimjRofsUPPUrEwqPxvfKZuZaEXpQWFnAeTlua3Ji55Dw1Td-R0n41u3R_RFh5xgT8nGk0B8Wlfy57AvHe5n6jGxaLtmhSba7yPF_mqXiSIb-TETbWeMY0eHLNHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌محمدسیانکی‌درباره‌درآمد گزارشگری؛
سیانکی: هر ۶ ماه یک‌بار ۴ میلیون‌برام واریز میشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23479" target="_blank">📅 01:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23478">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف لاله‌ های نارنجی مقابل سامورایی‌ها در گام اول رقابت ها؛ نماینده آسیا به شاگردان کومان باجی نداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23478" target="_blank">📅 01:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23477">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OysJWlHRsYN1OlJo10S5ZPkg2A9lXAMZbxaXN4nxSZ_KV9hsHpX7AixvrJ5Jn7IyQ7uJs3hGTv7vyRUD2BA8fdcMwLUBmn0X8VrUl3Dk7wxSKPLG0zyTCUI9P6_fDX15xxdLr3xA0wikFU0YLrRgjbQOmcwzf3ut5Cmb7npfJnAVDYV5nZnJXxkIiy9UjO-X9IqC_WHcHPxLjs8-8R-U9I4XnEDKfL5aR0_xrXVhwwOeYLmTGfrRqr8AoBvar6R_NZwuScPUF11sAjqeP0I0qgBglQ5nGtBpf13N_2ShErdf3dSNVmBML0iDBIICpO16DK6X5WslwZK2VPpx5lbaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی؛ شماتیک ترکیب دو تیم‌ملی‌هلند
🆚
ژاپن؛ساعت 23:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23477" target="_blank">📅 01:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23476">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78498ffe8b.mp4?token=GHqpWm27dnPKhiX3nfXz7dz7aP44seUYbUwb8OtIvtyCaiAwmiktmXK17sKqI99VsQWxQVxkxGw7DmM-BeB2iIMLpWtbIDBTrX_118YydHOdbA9FMlnpoYC3RRzI_TGfVd6pokYZUSNJkwVUlK6GWrjwkJf8-7hdiGC0cyPFYcwMttyYTihw0YbcoKpC_ADJN8N_ypGXou_dRLithl0SC4s9rnxcP8PaoleWwkORtYxVq0p_9MzYjpH4s0yFHTJcKkeLylQzC0748SyfSESCt7J_wYmi22st4I57wq8Q5moKBh_my9fc1F_kkLKVWxkC7zNIHex31kHVk-DwpQbIAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78498ffe8b.mp4?token=GHqpWm27dnPKhiX3nfXz7dz7aP44seUYbUwb8OtIvtyCaiAwmiktmXK17sKqI99VsQWxQVxkxGw7DmM-BeB2iIMLpWtbIDBTrX_118YydHOdbA9FMlnpoYC3RRzI_TGfVd6pokYZUSNJkwVUlK6GWrjwkJf8-7hdiGC0cyPFYcwMttyYTihw0YbcoKpC_ADJN8N_ypGXou_dRLithl0SC4s9rnxcP8PaoleWwkORtYxVq0p_9MzYjpH4s0yFHTJcKkeLylQzC0748SyfSESCt7J_wYmi22st4I57wq8Q5moKBh_my9fc1F_kkLKVWxkC7zNIHex31kHVk-DwpQbIAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
عادل‌فردوسی‌پور در ویژه‌برنامه امشب جام جهانی به این‌شکل‌جواب صحبت‌های میثاقی رو داد: اصلا حرفات ذره‌ای برای هیچ کسی اهمیت نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23476" target="_blank">📅 01:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23475">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fa8e48e0d.mp4?token=cMwM3KDhqICWRXhLMmGG0Wi5xDSRzdg6-Srbmgj4Z-3q95V6PDGnbQPzLltfzlYe7m3TbqfUDB17SsUejO3_7rr-EmHHeyhsMzfndSeqd9J9GWPfA8bUOeaapBzKGV4vgwzvVV4IbqCSMPFJMEXtMkEWRDwWS9K5N5B51QD8zDkn3vJ-PGD5ANjsuJUKwXq6uaPOL5kWelOqkYS1DgdHynxWWBUIx8Cj0hqrBuuo9yDsWK1xAwVYafwh9bqRAHd0YDEaMyLBLsXdWG4HWd_kEyDIc04ac-8wJb7R8gkOzx_qFr45r881Bsvw5McnORFB88Ccw2PPafvYBJfPDPkjWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fa8e48e0d.mp4?token=cMwM3KDhqICWRXhLMmGG0Wi5xDSRzdg6-Srbmgj4Z-3q95V6PDGnbQPzLltfzlYe7m3TbqfUDB17SsUejO3_7rr-EmHHeyhsMzfndSeqd9J9GWPfA8bUOeaapBzKGV4vgwzvVV4IbqCSMPFJMEXtMkEWRDwWS9K5N5B51QD8zDkn3vJ-PGD5ANjsuJUKwXq6uaPOL5kWelOqkYS1DgdHynxWWBUIx8Cj0hqrBuuo9yDsWK1xAwVYafwh9bqRAHd0YDEaMyLBLsXdWG4HWd_kEyDIc04ac-8wJb7R8gkOzx_qFr45r881Bsvw5McnORFB88Ccw2PPafvYBJfPDPkjWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اسپویل‌ازصحبت‌های‌امیرقلعه‌نویی سرمربی تیم ایران بعداز دیدارفردامقابل نیوزیلند در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23475" target="_blank">📅 01:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23473">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vg4dRCQLMVP6Xg1GZ0UwRzGMi2uI8xtHWBXwBe3HnxUNjQRG03nlfks8FpSJZGF8-b84ifNWKC6JmV-NZGFT41tlAtogsI73_JnmPvNxQtyWBKHbs6_uwr5VM_aikCrsbKJpAm72Fre0CdQOBbfR3JLuVLlqQB6IQgETwJd2PqiMf3T9K2dWOh4uKcmHOQ8MESoC-l1ewBTbRSVQuXwoGYDI41DqilkApSvr_M9nKoQQwYpsl1h9sc-VIi92IsAS1DOfYqwfXqlMAlF5muHOnO-CIvnu60wLhrBtp4D4YlhdRQ-O37P82j-3GVsMpCUkpXAosY8Cn0J5cSvxCeUNsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ نخست‌وزیر پاکستان رسما اعلام کرد:
🔴
خوشحالم که اعلام کنم توافق صلحی بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شد؛ جنگ در تمام جبه‌ها پایان یافت، مراسم رسمی امضا روز جمعه، ۱۹ ژوئن، در سوئیس برگزار خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23473" target="_blank">📅 00:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23472">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noN2ji8mkW5izvylnsqwzbbqjQX99edPYpBDqgGFKSKPydMkg2_HRO8CPrJhpWCcS3Nhn6VOU75pqEc4h0p-b2iSnCsUD68nHHN5BW7VT5sGEbnRi8DBCrelXzz6my_NXsUodJDi1SuhFhPandh1mToG5ywCK-oNCvqFs1pbmW73g4VdPypV1oM9sFzvgexQ9Tgtjod-wjthTvnbB3NEA0Az0DhzHcbvDeUzqkn4J0TxbjFrFjlOqW_O-tAWtBuyiR6NjwYSZOlCT19nBQmO7VLZPPh7fU76jfBo-AiZSJCR-2sK8ky7nWkjkJa7Z3CunooFfgE5wix1XKV_jIZ-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇷
#فوری؛ گویا دقایقی‌قبل توافق میان ایران و آمریکا رسما امضا شد. ترامپ درگفتگو با وال‌استریت ژورنال: بزودی بیانیه‌ای صادر خواهم کرد تا موافقت ایالات متحده با توافق با کشور ایران را تأیید کنم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23472" target="_blank">📅 00:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23471">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZ72HUn7ryWhAdTTc1St4kAIU_8astvh33-WEkJLyCX7EEXmRY2ezqsXMk-4Q6__1-gY1EPQeWODdt7kseioJhXdl3mREbLMm65F7AoMRUZ0pzSouuGWVijheVicYGE-BB35iHEa81ZSxhkqC5ZbFovYO67KtdlFcsorfdSUeCuOXEjeBbHLLFyBTzoCMOm48lKms0r7ZWDgHzRY8r8bSw8kkCzubWZeacKTDEnyN5vgXZNfXj14f72qQSJnT8xnf46sWPpBXxHZBUK6HI0CjNfhcpwCuhhhri3c6Fv8glrmeDzuJ4BgP-dNroBpYtLF9lJ5pefRfHn_YnLT12BZOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
انزو فرناندز در گفتگو با ESP: به سران چلسی اعلام کرده‌ام که برنامه‌ای برای موندن در این باشگاه ندارم و قصد دارم راهی باشگاه رئال مادرید شوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23471" target="_blank">📅 00:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23470">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Joqw95UXlh94M002NxSrmhMVNhKjmtglb6fHtMf2OR2h_imZ6zQAt4xcRCkhqQ4owi6SOA7DaSjTXQfXWtmeJQ4XUuC2K2TEtK0HUWqw3ZmdWjqtvPB1sWmKLwVis_LbIlTkAXLYJVniaBEceYvMc-qzlZIoYQWl_V9ff8EZjDHlSOFZDpj8NqbKCkxTvQtnKEEAbZynhD6fs2rYy30w0rviKYCU8HO30IwydOGTcN98jXXW00C5BcLzVTXYjcQS7y5I1gLihPVDz20aLdNoNirckLoTfw50xL-A_vNFVV09LSYWce24oPB_ITEKoO9eLf_KL5eVV7XVa9e_jPh9Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#تکمیلی؛ رومانو: روبن آموریم تموم شروط باشگاه میلان رو برای سرمربیگری پذیرفته و گفته با هر شرایطی حاضره به این تیم بیاد. سران میلان هم گفته خب باشه بزار حالا ما بریم دورامون رو بزنیم اگه گزینه بهتری پیدا نشد با تو قرارداد میبیندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23470" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23469">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdKKbsWFlL0CPTQ4vfg1Zrn0tZwr0L2sbyxDMAltbFdC407oiZmp_h4sCPZqYnSrbytKXlmquk8O-xGu2-kweRG_zt892TfrL6TwaxT8I-K0JrZG1j6qHpg12VuRERwaREqA9aeEf_woWCURkcO6einzpogEGp82zGCXg2w6YHKrvNuUoP3k5xISpZkDNlN3zWLJiBahSQV1NVbT9eBlA7klRiZcHplZITNESh9QMlawMzE7xQBEyIPvMslDZuevONybtvIfE-QE8wanehIVm7NdSK_WsWjD1nnUpTLu2ts1VNHR7xmLMT1rfZ-Qz5WdBApdnpHBsYFf67gtUGtuPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
طبق شنید‌های موثق رسانه پرشیانا از نزدیکان کسری طاهری؛ روز سه شنبه کسری طاهری بایکی‌از دو تیم استقلال‌ و پرسپولیس قراردادش رو امضا خواهد کرد اما فعلا رسمی منتشر نخواهد شد. همون روز سه شنبه ببنده درجا همینجا میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23469" target="_blank">📅 23:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23468">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_RrYXUPlBkgD2Uh9gSu2u-anLio6-IliQmVQGaRtfZ3aefLDQm9w-9Nua3bPVVUrQw6On6KS1Um-ewJtNjgf8Si4Oq_nniraGRS1e5wSwhmYAzNKYoBPvYSbBFkLq3PjTud6vZeLoKwae9USF9Z6mxiLMZFnFva26rYv3dUaNDO-ZOgE2u_QSe3MvFtmNY_bLhZTCA8NeJb_RcVC6vbxXNS9qXQ9TMrDGc7Nl8N6PKKbHiiEdaO1D9FcXI9KZgmlLiVfOANrDooE-UxYVtugD_uE88wyCRCiybdpJ5tyUjyVFw0j2SdRITDmlW4j3mI5ca-KmnTW2KuxuswOMaUsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تاریخ‌فراموش‌نمیکنه بچه جون؛ یه زمانی برای یه صندلی اینجوری داشتی خواهش و التماس میکردی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/23468" target="_blank">📅 23:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23467">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvNK2pUNgEW4wCsc_wKIbM-EnO1qso1q1W0MIFfm4VqABbqausFoGpC6HIMkckY_Tf2Y0h7Wx3XU74uArFqvKshUXv3ukzKCuoizGyXHLZdL-jbB31KcwXYS1JRUFr_vX-aMdp4yBtawphHEctWFM6CQoCjbHO395wMLbvLI5Bi76ELQQUf1lvfSwtwvTVXRqvDj7t9NkZRjnE1_b2SzhTOB2MLt32i6LvRtQvVtOu9fa33gopVg-jwCigkUTaRULpS6D8BO01S8M3n8fvECi9XBb3PCRDnrRtzjVKljbG6My7CZ7KAxs-aRGa8ivqFnhqZrrf82tV4N70zg9Wfrmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین‌نژاد، محمدقربانی،احمد نوراللهی، کسری طاهری، رضا غندی پور، مهدی قایدی محمد محبی، محمد مهدی محبی بازیکنانین‌که‌احتمال به لیگ برتر برگردن بسیار زیاده. اللهیار صیادمنش هم آفر خوبی از اروپا نگیره احتمال بازگشت…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23467" target="_blank">📅 23:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23466">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeb4ab3ec6.mp4?token=C0xGQMY4q_BeCMxPSmMcVvr4EPzVmoG62tVladn7f3CQ4QvFGWy6Ij7Dz39XPepaYtdlfEJvq5YUTE7ZnNPw6gfQ47RH1hDwoEOpsEAMLrc6m3ryvy4fHTu0P51tvmNOcnN2K8E33upcb43OPyOQJFC5814o3nVYeGeXZglaT5RwxTdZhN8L67RT1aUf3aaZ1zAkEyYYAgpuRZFGP63ohXkdQH-AhkKI3I6Bwa3H4yPhT6_5I16CTlM24mAWuy_-aCqds78uUr-7Ddlc7GXtJl9PCMaZ-nzAB3qtbAa8kIp4VbQvHmUxv6dvdqo5Q-U4A7Jpavidev900Np3JaxEZwxiWxk0ZwYz-L1VJ_EhgVzp5hmbaAJHDbwDZE8hMkrHjhBodQDo-AF6Zg9MxkFgtNN396wGSI3mg7sHlZesQZTHM35yXxPaKFi3y3wp2IY5ZwECDouf33I87-S2ZJpuHAjernjWEXZaWQYbuXN1EiWVmqUoW4-GqOmUFybUdi0H9n0WTW1pspeYPr1i5fjVVb636W0RpKLStXzGeggYpXEZWgdjSzzydrdNDdALh0q-e_itmzsTQsoXF7OQdqcsFuobhGqIN4m4kDHUNGY6sy0YK_jmTLIEwW1e_RtqTsyfaKAU6JjZuWQPEvZ74ntmn34q7dnMjW79AhXI5vr-WkI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeb4ab3ec6.mp4?token=C0xGQMY4q_BeCMxPSmMcVvr4EPzVmoG62tVladn7f3CQ4QvFGWy6Ij7Dz39XPepaYtdlfEJvq5YUTE7ZnNPw6gfQ47RH1hDwoEOpsEAMLrc6m3ryvy4fHTu0P51tvmNOcnN2K8E33upcb43OPyOQJFC5814o3nVYeGeXZglaT5RwxTdZhN8L67RT1aUf3aaZ1zAkEyYYAgpuRZFGP63ohXkdQH-AhkKI3I6Bwa3H4yPhT6_5I16CTlM24mAWuy_-aCqds78uUr-7Ddlc7GXtJl9PCMaZ-nzAB3qtbAa8kIp4VbQvHmUxv6dvdqo5Q-U4A7Jpavidev900Np3JaxEZwxiWxk0ZwYz-L1VJ_EhgVzp5hmbaAJHDbwDZE8hMkrHjhBodQDo-AF6Zg9MxkFgtNN396wGSI3mg7sHlZesQZTHM35yXxPaKFi3y3wp2IY5ZwECDouf33I87-S2ZJpuHAjernjWEXZaWQYbuXN1EiWVmqUoW4-GqOmUFybUdi0H9n0WTW1pspeYPr1i5fjVVb636W0RpKLStXzGeggYpXEZWgdjSzzydrdNDdALh0q-e_itmzsTQsoXF7OQdqcsFuobhGqIN4m4kDHUNGY6sy0YK_jmTLIEwW1e_RtqTsyfaKAU6JjZuWQPEvZ74ntmn34q7dnMjW79AhXI5vr-WkI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جوادخیابانی وسط‌پخش‌زنده سرودملی آلمان رو خوند خداداد از خنده کم مونده که پخش رو زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23466" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23465">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی2026|جشنواره‌گل ژرمن‌ ها مقابل تیم کم نام و نشان کوراسائو؛ شاگردان ناگلزمن در ایستگاه نخست رقابتا حریفش رو هفتایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23465" target="_blank">📅 22:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23464">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mu679wWu5oqxIJPTQ_plnd3L4Kcy-BcP1-UdbosEfA8aZnPS6An30bbsQ-mJgRUz4fc8g4NUvrx4oJjHHlNZcjWrZXZ2LHWm2NBR9wfSiYqAdBdIUN-vJTitsCPVY3ji0iPipbfNTOEAS3ZEYyZzVgA1uYDw4DHxzAi2p_zBUng6QZGxyumSarY2dDj3jhcaAuxR9k1dT7FS91sgchNwumHtgZGlL0haCvEYeNRQ4P3u3gc1YIS-9FGnHNkJ_s-JABksbW5bOaX37Yi9iWekW2-7zXno1dvtJUmAfZPXiBZ6YIveTi1Rc5vASzAsrKw1Ye56YRFYRZc0A0cMUwUu4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23464" target="_blank">📅 22:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23462">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fw1C7haUjm8PAk9M31pOfS9u9V7XV6tmyG0RBkc8LDRvTtDwgn8K2a016r_TfreowIoWwWbSE_b7L3cxJTUSFb4CfghNbmyYQo3GseaEZB1bpm_3Oefh0wzTJwxwTFMznLZV2NmP1vX6pF849HdBdaSb9dIrGx7NFSE7sCIQ5Fbj1HUeeheQCdtLaeoiYGDXqBzeOGnaEgE8AoR1m_DL86uHzvl_HN_YjRcM1TeI1bNz4WT48Ge_JlYdNz0Q2HaHhJ_hcNO6si3N1NV2gJUjIMBkg8DjkroHwT7iEliTYOfBccHvTCLtKIiMOJQXb_n5ONvCQKeLUS5MWqXUtFw8cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qh0DD3T-N5hYiHOYU4G7k4aSj8bRbkyL66mCfza3xeOnwQ2fsy5sT_qet_K-NAzk-dpVBWZ0qMAzACEicRHFPr8XkEjfkXv6so53Xg92mVF3Wv_-ifrYItMcQSFc86WIs59UwikCUynqSZcz2C1xQOHrFmYC1p6wWHpWX553CaNS52_iv4Y-zpWfrWX7hyaYAmPNnBsgDwd0F2-Bwj4STghWXxngY8NpA0-sn64itdci07253ZK3IZz6i1_QAKLiwmdgICGa9K1YwLOgn2yXpUZYckN2QRgTCHUXpVOjwxaUFI_dsuo6r4qji37joXtOZg95toH6dYibbRdfAhsORg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول جام جهانی
؛ شماتیک ترکیب دو تیم‌ملی‌هلند
🆚
ژاپن؛ساعت 23:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23462" target="_blank">📅 22:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23461">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwScRGVlm27oO1vvnqPDQhj7d2Nls0UYyOjzKHmhrMsbT6xc47ThPTiYtXWlh_mMCemCsBh5v1g64MWeYjmwLnftU2OIYR0huX8v0sXRenwLus9kkwSYQcx6MOM5uwlmAhu7YeHwBmHMUnvSDSJIio8_OvvlgNeyAmQdIv-U7jANB0vcYCKdvD9WX5sL1kQRnM4pvX7ZHeqZ7fi6oGVjXLLVMopmdYRN_0hABTK1mc_RL-4NY7ho6CKg4GBfKL886wmGpS0fHTIT-iqydILu24pMuUnUCwNd8NHQLNqZpIjrZgtLa9AdAHbpDRj2ocfgqi9l2ADTK8mUTBzONuWGiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین‌نژاد، محمدقربانی،احمد نوراللهی، کسری طاهری، رضا غندی پور، مهدی قایدی محمد محبی، محمد مهدی محبی بازیکنانین‌که‌احتمال به لیگ برتر برگردن بسیار زیاده. اللهیار صیادمنش هم آفر خوبی از اروپا نگیره احتمال بازگشت…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23461" target="_blank">📅 21:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23460">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dfc0bbc1b.mp4?token=MCo19Ixqm-_3c7rlkrvizy5UTORwOIJDwEeRHscazpLVc3v3bV8-IzpXLnIux5aRLvvVa_4mhTlZSgibvJA8oUmi0JC02f1m3gOGBAccpaX7rS12bxq2dwdQsKhOxDNJeDHfCp57tTOOVLumJH7fQhUT0ObBZGozWLpjbRXT3n1lzX-XOpexGXB-Mev3mmWMCadADhDCwHdogZlQljUrhUd-ZQ49L67G9rjoHy7zVWO5FqMeTmtqfOYq_WEvhFC2IGwPIsB6jxzj8RZEKYDUYOWCe5fjwsTGfbSa3XvCNx2g3hOG5CjyZwRTJDRCzqMJn33RscXjTFt3ds-mWQGrug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dfc0bbc1b.mp4?token=MCo19Ixqm-_3c7rlkrvizy5UTORwOIJDwEeRHscazpLVc3v3bV8-IzpXLnIux5aRLvvVa_4mhTlZSgibvJA8oUmi0JC02f1m3gOGBAccpaX7rS12bxq2dwdQsKhOxDNJeDHfCp57tTOOVLumJH7fQhUT0ObBZGozWLpjbRXT3n1lzX-XOpexGXB-Mev3mmWMCadADhDCwHdogZlQljUrhUd-ZQ49L67G9rjoHy7zVWO5FqMeTmtqfOYq_WEvhFC2IGwPIsB6jxzj8RZEKYDUYOWCe5fjwsTGfbSa3XvCNx2g3hOG5CjyZwRTJDRCzqMJn33RscXjTFt3ds-mWQGrug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های ابوطالب‌حسینی به بعضی از مجری‌های بیهوده،دلقک و بی‌خاصیت صداوسیما فعلی مملکت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23460" target="_blank">📅 21:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23459">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRCuj9jE85SdfIDn1uJMBvhYk2gbhPOuqyShttUx9LGm41O-5grMb8rdAM4AMcttmJcb5mFEb4Sg3b3SZkNWc-HvHLrTI7aWG8bvGXGAAjWfz3hpeQEnljT7dljAUpvmtscGWP5WhEECDE5g3NADTbFIQdO3nIdaBEtgEdudc0T3ofAZh9PdBuLb2d3ePHhI2O7ID2R9fqsyYacUIuX9-EJpijSizcbxbrYQHDsMRfu9R1CPlpJfe4sSs5e0JA48ukg4umU-NRKo-utmFANNPHAnD0lHmBjbZsrv6TNFolSqYiK6MHXmk_6EJofiSJwo-0ZtZxy1mm3RQ_Ui2um2Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل اصلی‌ اینکه اکثر بازیکنان ایرانی خارج از کشور علاقه دارند به لیگ برتر برگردن اینه که چون شرایط کشور خاصه و ممکنه در هر مقطع از فصل جنگ بشه و بازیکنان‌ خارجی تیم‌هاشون‌رو ولکنن برند لژیونرها قصد دارند با رقمی بسیار نجومی تر از دستمزد فعلیشون در باشگاه‌هاشون…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23459" target="_blank">📅 21:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23458">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8PCFhrll0ZqXGe-xfpc73bwotr2zfZTbSz_zDgVFKbVz4Vp-D4Kn9ys3bkMR3sVEirZ9F_jBjlVSIoxULW30n6aOGqRGFxw4Epkngs_LkO65Vpqv7vke87FBHobUvU70MlnyEs9GsivVfXfABaPK8ZUk_pPsKnIBLAZ6qgUMZTwGq0iBQaUvD9qrHa_tNCWEtmeUPuaZRhw8G43X_0KHsVK9HEvPT5Oa0XYfZiUcgp5yJ5NoPmtOTgxMRgUVAearYwnocKSGC6H2C68Z98wuJYpn335Kz9kNpzzcAp4b3q-rZwELgW05NHeaIqjlKhG8iIWZ1SzULncxuXJ-y74Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌اخباردریافتی‌رسانه پرشیانا؛ اولویت اول رضا غندی پور مهاجم 19 ساله الوحده امارات دراین‌تابستان پیوستن به باشگاه پرسپولیس است و درصورتیکه کادر فنی سرخپوشان روی این بازیکن نظر مثبت داشته باشد جذب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23458" target="_blank">📅 21:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23457">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UW3GBwoiSpqjGPHC2-Hx6CyK8Adh4g3deGHglm9iZhKz6RebX2eZgQ9QbeF9yEI5t7HhIf2MTCtnSOmkYclSL8lnC9Hu4iAxDe7dmzISMoGhdvNDu6E_mcAdS8-9BG8ntbycS-TMYRlmmwIQK4AT561oMuVwzEU9CF-FJgssJkf6Necb_iXadUrU35idhp8_DMm2LH88hz0AF-XtKRYAPx036MPLfQDqOFSoDPAIE8JuvrjvyLxnHE5L6DmGWcGukM5r-o53XqHUFYl5zkWdAoeAE3h8Q1VU4QASl55odRN6YIMEUliBsPffXQS9fQXN2OOeUd2f3lhg4O5x-3460A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23457" target="_blank">📅 20:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23456">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIG3jrz9-HtNre3vB_cY1GzUsgEllcbudl6eNyL1yJTzrRAgiEC8-oCCg_B7gF3vvY18RbPw2XFEt-Y791HYXhSFBexiM7sDAju4SpqYKOcYjEdRGsVWaWURc5vFgyqV2GEOEfbd441qOEza8c_8kDsd49g6eBX45LeolLeBcCoH7-wU24zQUpk8TwJVYwt-nF2t42zk5Sg1PNJTziyOs37_5y0pjeYIAyuUZDfmhWCbRTCmkLXIT2t1FC-mXclgETd4oATQ4zTpi5WLDS1Q9WZUJaMWlV-VAVrmP6g_g7KealY-G56YwsSW0aAFS_t_JsueRiBcte-5Pp3-2tue3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چهار خرید باشگاه رئال مادرید در این پنجره تا اینجای کار؛پرزبرای جذب‌کوکوریا 50 میلیون یورو به تیم چلسی‌پرداخت‌کرد.درحالی کوکوریا جذب شد که اکثر رسانه ها خبر از اومدن کالافیوری میدادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23456" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23455">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bd12ea167.mp4?token=ViMAVFAvcO4QmP3V_jcMllF9T4McRZgx1fspMJb3CFLOPrakDVQympT5ifPN9_m-48HilJ71PFN5XDI237lIfIIr4_gLeCqEgPKPufl4AXIXGEnWVx9AqM_XS3LqcGVzafBWG44XTQPfZs0WJZG_kjUyoQSwNalh7hf7IOpJXbNn_qVR9zMZ6Gl4O7Zcn53kf82ZErFklR8QRl9JEXfYjLT6WT-pFoGRMzPhLza1cy1TsXGcjwsxTLYJMs9yRXs_g9GO5I0ko1RRvaej5SMkuLeTuF5u4oVYdF8_YmPYVMuZBAEre6xWnxbKpMiXKre9jTvDcnag5XbHI3kkxL7JWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bd12ea167.mp4?token=ViMAVFAvcO4QmP3V_jcMllF9T4McRZgx1fspMJb3CFLOPrakDVQympT5ifPN9_m-48HilJ71PFN5XDI237lIfIIr4_gLeCqEgPKPufl4AXIXGEnWVx9AqM_XS3LqcGVzafBWG44XTQPfZs0WJZG_kjUyoQSwNalh7hf7IOpJXbNn_qVR9zMZ6Gl4O7Zcn53kf82ZErFklR8QRl9JEXfYjLT6WT-pFoGRMzPhLza1cy1TsXGcjwsxTLYJMs9yRXs_g9GO5I0ko1RRvaej5SMkuLeTuF5u4oVYdF8_YmPYVMuZBAEre6xWnxbKpMiXKre9jTvDcnag5XbHI3kkxL7JWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شهاب زاهدی درباره عینک خاص‌ش در برنامه عادل و عزیزم گفتن‌های عادل به شهاب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23455" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
