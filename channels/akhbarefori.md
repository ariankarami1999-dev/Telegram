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
<img src="https://cdn4.telesco.pe/file/h3iGs57JPlXd8JFw4KYoHB4JV9MJn-8cqWkcvL18Y3gfA2ZoQtlay8ceD83V2Z_W7zBr4JP8R8jWN2kLuN5LxD4jYdFst6T9Wk8p0oolRIwv_JHoDSNAQNL57V8PB3i7Pl5uwgBUJHVFyitnjtQ7nBa1thoTjNT5oeNE5ZeoIFMANeoLjlsTDl7svl180DJWTLh0N-jYgHuFRQ4y0TB9vHhOkVjGq2b7pqc0fKI8nAyn5eNJ1WgMJ4KBnxpMhKFGVYvzeNK6Fw8N5kyXZPGnkP4CxKmDT6bVOe4vofgfOZYO64Px06QGC6lQ4MIYhzyf5uGFaqeS_FuXK72Otu9vZw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.36M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 20:36:45</div>
<hr>

<div class="tg-post" id="msg-696447">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_tLrH7hidC-GSKdfckinbmG1ljp0EoMfcTqKPnTQ7oxO2X0uhYpjykOopMcgUz2j1MF14gVB9a1YOgnoBCgEZ_2iLCL8bTfYi7YmuGt33JPGZPrYgZY_8uNTquL0JqzV8D8xQMzf1wZK32dXqNrPHEzXp3JAHBYoItESGiclNVHd9UZ28Xa08OzVnQmz7pA1BLylVOfjhuiLYEFPNxJQkEyzSHMZBuJao-9aotd46ncsdJue3Wg7JT20hYNNS4UPSHFj-tFVy5cEcokPzsY7LwDx-PkNX_eRK4HOIxcKoFjBhXv90cIchYS5ZS_N9lUovm2cup2ubAoYcFefA8ehw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسل‌کشی اسرائیل در غزه؛ آخرین آمار قربانیان
🔸
از ۷ اکتبر ۲۰۲۳ تا کنون، دست‌کم ۷۴ هزار  فلسطینی در غزه کشته شده‌اند؛ یعنی به‌طور میانگین از هر ۳۱ نفر جمعیت غزه ۱ نفر شهید شده است.
🔸
در همین بازه، بیش از ۱۷۵ هزار فلسطینی زخمی شده‌اند که بسیاری از مجروحان با آسیب‌های شدید و پیامدهای بلندمدت جسمی روبه‌رو هستند.
🔸
از زمان آغاز آتش‌بس در ۱۰ اکتبر، ۱,۴۶۰ فلسطینی کشته و ۵,۱۱۶ نفر دیگر زخمی شده‌اند؛ آماری که نشان می‌دهد حتی پس از اعلام آتش‌بس نیز تلفات انسانی در غزه ادامه داشته است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/696447" target="_blank">📅 20:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696446">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c60bb30fe.mp4?token=nondNUY8kEmOuuXZuUu_6Kq4uuy2TCcGEO1UvE1amVD7NUjlyTUfaO_rvfDgDzfTfKZgkv3p4Vm7CPrJY37dcpz2nU1BjfouIGUkxsRQjJTkadXTQjV7Jwp0bJm4I91k9q6YonVdyS3G3hQiPxI5EKgXEUfRAK6wVWse96yGKGl6YEB6GNXAk_1yJzQR9EzpX7v7tPvQSvCCrvnMrLDJxOcD5CREFYYXvure8KguwiGy4XWaX_XV0Hq7U0bJwgCHGaL4FCEplTwTAZPWQcI6mIfOiHMndhJa1MmK_3RGKhhD4fT4BaomUHSkkG7LpGHJ3RDh5SPfQJhi9f7ai1-M7WChMGEjcWutCw5Ge1ligqtyXh0YIXKTZ7r-UyMF7rT7KpUa4CgmixsFBaiiK4f7sNM_1HIN__n6AxXUGBOaIdOj5Cxvskncjz7SM9nDvLw-veSvDFEyAKI8gVfxbXYLXXYGI4ObTCFsJsWl6LOYyQkscndLfEAaNrnWtxVSkTmnHvF-Rpwb9-6_GfzggYCWJy01A8V8K6GhBIMCGSu5Vj4EBwwQmtI8aXjwNCR2LEGVwupcnFUFs6X9n2MQWfEsM0kigr2xwou_3G_05Vy5juc-YLxVT67K2O0naI1i_lhAoIyKeyPHEMfAElHwWgNq3UFptGoLjuQPnRIM-bj2Qg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c60bb30fe.mp4?token=nondNUY8kEmOuuXZuUu_6Kq4uuy2TCcGEO1UvE1amVD7NUjlyTUfaO_rvfDgDzfTfKZgkv3p4Vm7CPrJY37dcpz2nU1BjfouIGUkxsRQjJTkadXTQjV7Jwp0bJm4I91k9q6YonVdyS3G3hQiPxI5EKgXEUfRAK6wVWse96yGKGl6YEB6GNXAk_1yJzQR9EzpX7v7tPvQSvCCrvnMrLDJxOcD5CREFYYXvure8KguwiGy4XWaX_XV0Hq7U0bJwgCHGaL4FCEplTwTAZPWQcI6mIfOiHMndhJa1MmK_3RGKhhD4fT4BaomUHSkkG7LpGHJ3RDh5SPfQJhi9f7ai1-M7WChMGEjcWutCw5Ge1ligqtyXh0YIXKTZ7r-UyMF7rT7KpUa4CgmixsFBaiiK4f7sNM_1HIN__n6AxXUGBOaIdOj5Cxvskncjz7SM9nDvLw-veSvDFEyAKI8gVfxbXYLXXYGI4ObTCFsJsWl6LOYyQkscndLfEAaNrnWtxVSkTmnHvF-Rpwb9-6_GfzggYCWJy01A8V8K6GhBIMCGSu5Vj4EBwwQmtI8aXjwNCR2LEGVwupcnFUFs6X9n2MQWfEsM0kigr2xwou_3G_05Vy5juc-YLxVT67K2O0naI1i_lhAoIyKeyPHEMfAElHwWgNq3UFptGoLjuQPnRIM-bj2Qg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امروز عربستان سعودی در محاصره جبهه مقاومت است!
🔹
کارشناس مسائل غرب آسیا «یمن اکنون به یک مکتب و الگو تبدیل شده است. عربستان سعودی بخاطر یمن، از شرق و غرب در محاصره جبهه مقاومت قرار دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/akhbarefori/696446" target="_blank">📅 20:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696445">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ادعای
فرانس اینفو: به دلیل کمبود جهانی سوخت ناشی از جنگ علیه ایران، فرانسه ۱۰ میلیون بشکه گازوئیل از ذخایر خود آزاد می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/696445" target="_blank">📅 20:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696444">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromعشقه ‌🎒(Seyed Hashemi)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f62cb6159.mp4?token=Ew6wulCH6ZI1h4-8VXzSB-0DSbhVDet9bqsE3jBZmVrN1QYU54lWdA9qbbVSTRwcukuKEWBOvJVnkvqKuFykjNHY7oMZXvNGsiX7sZ5sfCgNU0ogKvR9tfOXV4Yi_mGbIBhn8F2SRNbNwhPhFSX6RjemjVIVo0rTcDTNSDp4QM-nqc_7smk-WQpbH5K6HWEbsnU_dE3UAh6ZNP7rQ51HtK69RbZhoe34ExUbYv6iMy9_O4OINcwzJY2-F5EZipK2UNrWf9SfAJSRngTdOQIwyR5YLMyQsC26IysKpDCVJK26O88EeXMsO8fck3rtm4iWSJkYUB9SmXZyNc_Sv7ubsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f62cb6159.mp4?token=Ew6wulCH6ZI1h4-8VXzSB-0DSbhVDet9bqsE3jBZmVrN1QYU54lWdA9qbbVSTRwcukuKEWBOvJVnkvqKuFykjNHY7oMZXvNGsiX7sZ5sfCgNU0ogKvR9tfOXV4Yi_mGbIBhn8F2SRNbNwhPhFSX6RjemjVIVo0rTcDTNSDp4QM-nqc_7smk-WQpbH5K6HWEbsnU_dE3UAh6ZNP7rQ51HtK69RbZhoe34ExUbYv6iMy9_O4OINcwzJY2-F5EZipK2UNrWf9SfAJSRngTdOQIwyR5YLMyQsC26IysKpDCVJK26O88EeXMsO8fck3rtm4iWSJkYUB9SmXZyNc_Sv7ubsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۷۸ سال جنایت،
۷۸ سال کشتار،
۷۸ سال نسل‌کشی!
آره همه‌چیز از ۷ اکتبر شروع شد!
‌</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/akhbarefori/696444" target="_blank">📅 20:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696443">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c9fd2bd4e.mp4?token=XgVOUn9DIoM5Aj8j7nN1XdEQAAReVPSfSxJpC21iMDh5SouuRTV5guOgkBxqGutdmLlC26Rr-_84-TRXcubyeKP_9-oWfl63pz43Tlo-TiuC75H7qej9_MK_i-t-C7g9eoU_qqVSg8q5MyuSIVJwPvRRCer4DAf6sdxU84YR6jPQWN__Iww2-7lmFAD_qFBzlwZ-Nce_zkCjP-3obCX8LXjsJ_31vZFNUF77wX1KsM9e1MmZThZg9FGtQuCawC2YlMc-Th-3N3NP50pgCQH2JLn1t4IBrpUYdacIqyPgok9pH7ULcWY6MLJdIZBHYKyNCAkszSRgBrMjISQY1FZ5tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c9fd2bd4e.mp4?token=XgVOUn9DIoM5Aj8j7nN1XdEQAAReVPSfSxJpC21iMDh5SouuRTV5guOgkBxqGutdmLlC26Rr-_84-TRXcubyeKP_9-oWfl63pz43Tlo-TiuC75H7qej9_MK_i-t-C7g9eoU_qqVSg8q5MyuSIVJwPvRRCer4DAf6sdxU84YR6jPQWN__Iww2-7lmFAD_qFBzlwZ-Nce_zkCjP-3obCX8LXjsJ_31vZFNUF77wX1KsM9e1MmZThZg9FGtQuCawC2YlMc-Th-3N3NP50pgCQH2JLn1t4IBrpUYdacIqyPgok9pH7ULcWY6MLJdIZBHYKyNCAkszSRgBrMjISQY1FZ5tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از وضعیت تأسیسات آرامکو در شهر رابغ عربستان
🔹
آرامکو علاوه بر ۱۰ پالایشگاه در شهرهای مختلف عربستان، ۵ پالایشگاه نیز خارج از این کشور دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/akhbarefori/696443" target="_blank">📅 20:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696442">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعای بلومبرگ به نقل از دو منبع آگاه: آمریکا به سعودی‌ها اعلام کرده است تا زمانی که جنگ علیه ایران ادامه دارد و تردد کشتی‌ها در تنگه هرمز مختل است، نیروهای زمینی خود را وارد یمن نکنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/696442" target="_blank">📅 20:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696441">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfdf8301ec.mp4?token=s51j0h17GfVF_QYCp4o-hLCV-uQ8SDKRBqxlvrT0SAWnnunXbWXBrmNJkg0etw_gyAsO6EqEU0rwGNNS09HVAqd9ofT_C4IEoKcoTkTV76I34woCNW-FRslbUTWOZuAmzDhZ0HlyoCMUdEWIJpGlHvnCweDwui9yHCe8_2Ghi58BfWwgle-jES68LaO70KQF42gh-dJ39jP6hujZyE-1tyjP6gjeQAmpf9888xCJbrxOnjvUxH6Ul0w7HweMCV34gsuxn6w6ICkRdriJ-6CNEyJPDhsWMUIF5pZ1DwQP3TTY2dtncK9QWbWBNaqpCcA_yTqEuvZDwtTqEFvR5-v9sl5pGxf1OQh7D7Buq1p1fhT_JnS5R8TOxcHbIO8E_Hnila8zyRvDRr0YoXKfb_7hZZsYRznbNfpCaQjypbLC-9vg9Np7yoMQAvqfBUZtRsO1b2a0yXkB8HiIVjhH1h8Fhi4F6b-Vrn9_IMDqppYfdWojTZZFt5Bs8_szE6ySIUsFAkDg0vILMuEg9iK8b04qbPG39dgQ8UlIh9tVFvvaHTikeDJ1_G8uF12MDz7xJqZuna6HVt6MO6IVJURUj5zq6WHd1z3v_6BkFJ4xMEj9YLPgO_YMfQmYw6thvyvsvknfk6LUZVuLkaRsySsThN9_e1aE3Mjthf4i25ebeWsVM3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfdf8301ec.mp4?token=s51j0h17GfVF_QYCp4o-hLCV-uQ8SDKRBqxlvrT0SAWnnunXbWXBrmNJkg0etw_gyAsO6EqEU0rwGNNS09HVAqd9ofT_C4IEoKcoTkTV76I34woCNW-FRslbUTWOZuAmzDhZ0HlyoCMUdEWIJpGlHvnCweDwui9yHCe8_2Ghi58BfWwgle-jES68LaO70KQF42gh-dJ39jP6hujZyE-1tyjP6gjeQAmpf9888xCJbrxOnjvUxH6Ul0w7HweMCV34gsuxn6w6ICkRdriJ-6CNEyJPDhsWMUIF5pZ1DwQP3TTY2dtncK9QWbWBNaqpCcA_yTqEuvZDwtTqEFvR5-v9sl5pGxf1OQh7D7Buq1p1fhT_JnS5R8TOxcHbIO8E_Hnila8zyRvDRr0YoXKfb_7hZZsYRznbNfpCaQjypbLC-9vg9Np7yoMQAvqfBUZtRsO1b2a0yXkB8HiIVjhH1h8Fhi4F6b-Vrn9_IMDqppYfdWojTZZFt5Bs8_szE6ySIUsFAkDg0vILMuEg9iK8b04qbPG39dgQ8UlIh9tVFvvaHTikeDJ1_G8uF12MDz7xJqZuna6HVt6MO6IVJURUj5zq6WHd1z3v_6BkFJ4xMEj9YLPgO_YMfQmYw6thvyvsvknfk6LUZVuLkaRsySsThN9_e1aE3Mjthf4i25ebeWsVM3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحقیر ۱۲ سال آموزش در ۴ ساعت/ کنکور چگونه انسان‌ها را «ناقص» و «کامل» می‌نامد؟
🔹
سنجش شایستگی انسان‌ها در یک آزمون ۴ ساعته، باگ بزرگ نظام آموزشی است؛ الگویی که در آن برای اثبات «کامل بودن» یک فرد، حتماً باید مجموعه‌ای از افراد «ضعیف‌تر» یا «ناقص» شکل بگیرند تا رتبه‌بندی خروجی کنکور معنا پیدا کند./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/696441" target="_blank">📅 20:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696440">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
منابع عبری از شنیده شدن صدای انفجار شدید در حیفا خبر می‌دهند
🔹
تاکنون منشأ این صدا اعلام نشده است./ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/696440" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696439">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ادعای العربیه به نقل از یک منبع ارشد: تلاش‌های میانجی‌گری میان واشنگتن و تهران با بن‌بست مواجه شده است؛ تنگه هرمز دیگر اولویت واشنگتن نیست
🔹
پیشرفت مذاکرات به پاسخ ایران به مطالبات ترامپ درباره توانمندی‌های هسته‌ای این کشور بستگی دارد.
🔹
واشنگتن از ایران می‌خواهد بپذیرد که به توسعه توانمندی‌های هسته‌ای خود ادامه نخواهد داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/696439" target="_blank">📅 19:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696438">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3TpcxMWfuvLByospwCAI0FzKihNRsDOYE4sXugSMiCxODL2rtGCRgSZTCxPIeCVl70_co4QWzx1yTNgYkqcHX2pJVszak_NdLDNLhElgzOeLQxpqJ2GRm_o5jiV2BQVNYe2Spd1IZ5rpS0XH0atVLAHlIJTz-5DSvx2II9hLW-S3bNQw0i8pE0qjI9XdKVHgBB5BQE4dkp3ooCCUFHsVAgasI1UkBODdnsGunq0FXS2rH_m4Oy9Qx2-N03TG_p_s19ayWOW2_Cwu7YXmo-lgFQJ_bfox5tTtUzNr1iLC2jt0BbnnY3DSy5J2wElJYzcmCzvskX-brL2gzfycWd_5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهمترین شورت‌کات‌های ویندوز
❤️
🔹
فقط یک دقیقه وقت بذار، از امروز سرعت کارت دو برابر میشه.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/696438" target="_blank">📅 19:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696437">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJ7Q6ziL0-9-tecBTFfoe-nsbZPcr8pzQuJbEU5YqzAEmVp0r9a3_iEaSTVDCc4zJXcVC0iGEdrSGvpULpNXa531TTG2joidwRAIu0yBpAG-kS82J-UGfE4_aamHWo3QZVPskZD1U5WE6nN12vW7lZP31odxE7nUlV--gCGXxGBZ5Qrx2BZrBL-D56sOhDgTEgfA0QmfmpexuppHpgA8vKBShshrPZGs5pzVKgHtUczwzrLlmA8fk2pzhFPmGmUx48Hft7Z5nmBTeJq_aN465iU3IGeiVJp65oc9EL79fKlRprVdYxX-wCHsSAGk_YCMLi5-SSS0TnBSeLXIzOF4gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تا آخرین نفس
🔹
مسعود پزشکیان، رئیس جمهور در دومین رویداد توان افزایی هوشمند گفت: دشمنان مردم ایران اعم از آمریکا و رژیم صهیونیستی، به دنبال ایجاد اختلاف در داخل کشور و زمین‌گیر کردن ما هستند. تا آخرین نفس تلاش می‌کنم کشور از وضعیت کنونی، سربلند خارج شود. اگر شما جوانان تلاش کنید، هیچ مشکلی نیست که نتوانیم آن را حل کنیم و باید با تلاش و کوشش ایران را به جایگاه اصلی خود برسانیم.
🔹
هشتصدوهشتادمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/696437" target="_blank">📅 19:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696436">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
رکورد نفتکش‌زنی در تنگهٔ هرمز شکست
رویترز:
🔹
تنها در یک هفته اخیر ۱۳ نفتکش در تنگهٔ هرمز هدف حمله قرار گرفته و ۷ نفتکش هم پس از هشدار از ادامه تردد در هرمز منصرف شده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/696436" target="_blank">📅 19:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696435">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
رهبر انصارالله یمن: ایران در حال نبردی بزرگ برای مقابله با دشمن اسرائیلی و آمریکایی است
🔹
رژیم سعودی در ترور شهید عماد مغنیه نقش داشت و از همان ابتدا از تلاش‌ها برای ترور دبیرکل حزب‌الله نیز حمایت می‌کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/696435" target="_blank">📅 19:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696434">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
وقتی تسمه هیدرولیک پاره شد و مکانیک‌هم پیدا نکردین چکار باید کنید؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/696434" target="_blank">📅 19:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696433">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
احضار سفیر فرانسه در تهران به مذاق الیزه خوش نیامد
ادعای وزارت خارجه فرانسه:
🔹
ما سفیر ایران را به دلیل کمپین انتشار اطلاعات نادرست در رابطه با اعتراضات دانش‌آموزان احضار کردیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/696433" target="_blank">📅 19:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696431">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcjRj5VkPiODkUSjc0YUKdFgadigiaExEgxG-sYM2a6Jl5WrRIlN0XDT8hzaQagFfodIe2AV3TkAA8m745M0768Och8BBcVrxOSk1IoNbvI33bePpMCVqf0rvIFSGYDObiiPA0osFZqxP36J3volOB5HVNB_caA-Xvwxuiz6djiuGvoQnlWi8C-TK11UOx2rmQnkdCg4kJlfbaIczdwSXe47iWUPEZ7zWnzbMH5jVqNhuiyNjcOpiIYNe0LmAXjh4z_ImX33HEKPEYvbBVtUtriExMBmpZOxggaKuuVCcewXzocQsF5_1NNlZbIqsQRzeDTdiiKM0fO_RiNs98tJCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهانه تراشی تازه ترامپ
رییس جمهور آمریکا:
🔹
دیگر تنگه هرمز قیمت بنزین را بالا نمی‌برد، حملات اوکراین به پالایشگاه‌های روسیه باعت افزایش قیمت بنزین شده‌ است
#کمیک_فوری
#Devil
@TV_Fori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/696431" target="_blank">📅 19:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696430">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Irf9JbEaiQoabpzjpZ2KdvIgeXJ0GJ66Tvmopw7fkqv6Jjo54dtcLmf1rL_j_S0ljn1QBDcV0EodAddI0qiHlJ5Ppf1qy5RJkShVle1331RkFvhhzLFh51lon1lSVci-AqqLzKqwX8gmQ28eisroP6t6be-uWAF4fQjEGWIHgIfeTzUh0MM5m2g4KL-s5LPZpMhmC9PEEKeb75S-j0oPdfJmJHfzOMOdmGw_7poBsXVfV1jDzNUygfT-jFuiUCCCZtrOB8PwimZyKL9rAzk7U3GRlYqUjVIrBvgzG-M0kyLqFeAHEJS1Ik49-veeySvpnp2O5_aEBk4-GOk8AxRwAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میخک و کلی فایده سیو کن یادت نره!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/696430" target="_blank">📅 19:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696429">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ds1R3Cu-hIh4acP1lH18qv4Ny8MICcixuXPP04BKQLsrhbLqk7k7IbVaFnahRHsDG7p47JeU6JbqJlb2E15IUeM5wwfheSYLUcKQ8gQkVWQNYFs797XgT1L-r_dKvsWG95qUZbKOfINC35IQmtXbS1tFW7tYh0C2t9vN3MWcf_52duVdmPlzb2BxlipRfIlj4xjM5hb0Y_BE2gePrpoZ4_l6FWMEzqhr-bPwMhzp6OICAr1tok_U7gk2KJsIvcW5suTzlzWMn-znROCZKDXT8kzntssCcsjLCLZwKbMVBOJ5E6q3__SACdTO60GpGp5ojnc65kYTJXjJTLmvtnJbSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌گلد: خرید، فروش، تسویه و تحویل طلا در تمام دوره فعالیت در دسترس بوده است
🔹
وال‌گلد اعلام کرده از ابتدای فعالیت خود تاکنون، سرویس‌های خرید و فروش، واریز و برداشت وجه و تحویل فیزیکی طلا را در دسترس کاربران نگه داشته است، حتی در دوره‌های اختلال اینترنت، نوسانات شدید بازار و تعطیلی‌های غیرمنتظره.
🔹
بر اساس داده‌های منتشر شده توسط وال‌گلد، در این مدت به درخواست کاربر
بیش از ۸۰ هزار میلیارد تومان تسویه
و
بیش از ۱۰۰ کیلوگرم طلا
به‌صورت فیزیکی تحویل داده شده است.
🔹
وال‌گلد همچنین در صفحه «
وال‌گلد شفاف
» وضعیت سرویس‌های اصلی خود، از خرید و فروش تا برداشت وجه و تحویل فیزیکی را نمایش می‌دهد تا کاربران بتوانند وضعیت دسترسی به خدمات را به‌صورت شفاف بررسی کنند.
🔹
در بازار آنلاین طلا، دسترسی به دارایی فقط به امکان خرید محدود نیست، امکان فروش، دریافت وجه و تحویل فیزیکی نیز بخش مهمی از تجربه کاربر و نقدشوندگی دارایی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/696429" target="_blank">📅 18:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696426">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1d8a91ad7.mp4?token=AAw1BqQ6Jhl3x2gad8AMHGPkIctIsYdnZqyLmRmoGsY6Ab6BRQcofxXL8XOWkrX7TWNFmEaBF0b9qW0X1upCgRiAuUfaATXTnx9o4sOUnwdV7lQsxRF30p4VIUUrMnlFwnXubPdAH7nXF8aCZ2L-mNY3qNOeTVIwEx7HPd4UDoCpDvHaWuDEhA6n7jcnKNzyzdUVQUWpYozy52dYNNRrOAAOHKpAChwWwA1_Lf--qxuXl9sen0j_31_BqJFy2DZStxuV77XqZ7yoDHM5up6SHgOuiZZkRUa6zKIuifUVq5pBb4qAVaYSD2SOEtcilBUdqnCu0-mw6zu_5T-_af0dlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1d8a91ad7.mp4?token=AAw1BqQ6Jhl3x2gad8AMHGPkIctIsYdnZqyLmRmoGsY6Ab6BRQcofxXL8XOWkrX7TWNFmEaBF0b9qW0X1upCgRiAuUfaATXTnx9o4sOUnwdV7lQsxRF30p4VIUUrMnlFwnXubPdAH7nXF8aCZ2L-mNY3qNOeTVIwEx7HPd4UDoCpDvHaWuDEhA6n7jcnKNzyzdUVQUWpYozy52dYNNRrOAAOHKpAChwWwA1_Lf--qxuXl9sen0j_31_BqJFy2DZStxuV77XqZ7yoDHM5up6SHgOuiZZkRUa6zKIuifUVq5pBb4qAVaYSD2SOEtcilBUdqnCu0-mw6zu_5T-_af0dlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجسمه
"
شاه ظالم" در پارلمان اروپا رونمایی شد!
🔹
مجسمه طلایی و برهنه دونالد ترامپ با عنوان «طاعون نارنجی» و نام دیگر «پادشاه ظلم»، اثر هنرمند دانمارکی ینس گالتشیوت، در پارلمان اروپا در استراسبورگ به نمایش درآمد و واکنش‌های متفاوتی داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/696426" target="_blank">📅 18:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696425">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gqhq_sY5EqLeiGKeSAeh_zunSjTKHcZQFZIAozEXShMImuiZ76bNa0OxFLwRmRCdpeqtH4IwNLpBaRfDhLdMueXL286ZQW4w75bw4fsUGN26lNBKIQ6mt4TxD205e9H0EKkAIaiZiQhfWKjJwAAddzdVl57bTfcPMJD9zMEHGLDpLeSc6oarpXyWmJ9zW9ZFuUUYQd4Hh_iT38RnoN9D_Z2utfQqd99T03hzDm8Bn00b9JbPRJAJwrJ7CAKe4-9N3_Vqm5aDBOHLMVKeo-nFqpeUYf-8Jh9lqQA7thYbvia_HjUsCJdgQ2hx8FfZF_2XRCqg7spH6fo3BbMBiC_MyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویتامین‌ها و مکمل‌های مهم برای ورزشکارها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/696425" target="_blank">📅 18:32 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696424">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
امارات استفاده کشتی‌های ایرانی از بنادر خود را ممنوع کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/696424" target="_blank">📅 18:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696423">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل پنجم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
،
چله "چهارم"
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
|
محمد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
،
شنود
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/696423" target="_blank">📅 18:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696422">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ادعای بلومبرگ: سوریه قرار است به مسیری جدید برای صادرات نفت خام عراق تبدیل شود و امکان دور زدن تنگه هرمز را برای محموله‌های نفتی فراهم آورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/696422" target="_blank">📅 18:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696421">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6ZAZT1lPQQdk4n37CEiBvXpJgk5WXmoutc8scm34gTxEvah0oqeuBaz4Ic8LUqxe3d-0MSJFzKx3S31zBCFvPXWPLrQjBvhUotWctAISA-zVYzofHfi16mbnvHA8WrNTNg-VYyyLdJ0cl0L_7b1x0jBJr6wjOx1UYCLyg7AS5s9BMUMJpvWDHgf0whf1NXINrp0HV3NQocmRSH6-uVw6DfCg0Ds4BVaIaufEie5Z-0ZE7C9AIkm5ehSkQeu0fCAr9rzDHbayLuqrQSM1wdYbZ3NA4mY3XKoknaE4b3xYaYfloNHF6hH1TtxIeLG5VkuJyCFuitCb_u-grGSzEJylQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
از پرداخت نقدی خلاص شو!
دیگه لازم نیست موقع خرید بیمه ثالث، هزینه رو درجا پرداخت کنی.
با بیمه‌دات‌کام می‌تونی همین امروز بیمه ثالث بخری، هزینه‌ش رو تو
۱۲
قسط
پرداخت کنی.
✅
بدون هیچ چک و سود و کارمزدی
✅
و بدون حتی یک ریال پیش‌پرداخت
برای خرید بیمه ثالث با
اقساط ۱۲ ماهه
، از لینک زیر اقدام کن
👇
🔗
bmeh.me/kfd715
🔗
bmeh.me/kfd715
🟣
بیمه‌دات‌کام؛ موتور جست‌و‌جو و خرید آنلاین بیمه
@bimehdotcom</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/696421" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696420">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFAKOOR | فکور صنعت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jbf4_BR9VP_yTa6XzlyEbs2WenYEQP0QKOE4ImaT4BI-uCJowdaWI-u2fjM9CTj56HMTPENcdjOlMeNK-zU5v-ExrWTA7tpBnbA4UgqnvgKwE9Ur2e9iyKdEODyDQzuzbQ5TCjdj8fvMv6PvsnBT_5b-RFiSSjf0nMRMU0tFLjlzh5k3V5R2tcCUTgHzT8Ru4g0RF_q4BFWybzW72fv5sYtibKvn3V9UhlMEw3IJ1NsKacpgPDr31L23-2cDSR-ZdAwqJpSReyMh24341gh_lddK5hjZphAcpemF1horQY3o5SLZTnYHRpAg7omZAmGgV6O4aX8OTW2_Fzv3lFLbQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فکور» ۲۱ مهرماه عرضه اولیه می‌شود
🔹
عرضه اولیه سهام شرکت مهندسی فکور صنعت تهران با نماد معاملاتی «فکور» روز
سه‌شنبه ۲۱ مهرماه ۱۴۰۵
در بازار دوم فرابورس ایران انجام خواهد شد.
🔹
در مرحله نخست این عرضه،
۷۰۰
میلیون سهم معادل یک درصد از کل سهام شرکت به روش ترکیبی و به سرمایه‌گذاران واجد شرایط عرضه می‌شود.
🔹
قیمت ارزش‌گذاری هر سهم ۳۵۴۴ ریال و حداکثر تعداد سهام قابل خریداری توسط هر کد معاملاتی ۸.۷۵۰.۰۰۰
سهم تعیین شده است.
🔹
در مرحله دوم نیز حداقل ۲ میلیارد و ۱۰۰ میلیون سهم معادل ۳ درصد از کل سهام شرکت
به سایر سرمایه‌گذاران به روش قیمت ثابت عرضه خواهد شد.
⚙️
@fakoorsanatgroup
🌐
www.fstco.com</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/696420" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696419">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2205a259.mp4?token=cOVwl-gxDpJ-n7C9cFH4q_zz088Bq_6drD4i-AdBj6-nqTerONBudF7ENe1xvsJc8QUkl20fprE0HB7wBpaq7Qm9X0lmuUuKn0qx7pDdZaZ71p2OdlD20uGsuGf9ICzk4pNZLeFijb3MZ9_n4ftVgxO2VGRw3BoisRV26vBAB7doK3UGLCWniOchHK_OeG_fL8p0L7jscqXnthFg2VN5uFhGVS42tLjCy7ZKm00YKIAKJV-k1OC_wy0z-sXA0iDvh8xkiWfrnqnw5YwrxAaWHvWJRiuoOwQ9zhAXlUKwAC98DFf5RS1EK4H1U6mMYG1MLKwG3CNCO6TPFcXPNp7CUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2205a259.mp4?token=cOVwl-gxDpJ-n7C9cFH4q_zz088Bq_6drD4i-AdBj6-nqTerONBudF7ENe1xvsJc8QUkl20fprE0HB7wBpaq7Qm9X0lmuUuKn0qx7pDdZaZ71p2OdlD20uGsuGf9ICzk4pNZLeFijb3MZ9_n4ftVgxO2VGRw3BoisRV26vBAB7doK3UGLCWniOchHK_OeG_fL8p0L7jscqXnthFg2VN5uFhGVS42tLjCy7ZKm00YKIAKJV-k1OC_wy0z-sXA0iDvh8xkiWfrnqnw5YwrxAaWHvWJRiuoOwQ9zhAXlUKwAC98DFf5RS1EK4H1U6mMYG1MLKwG3CNCO6TPFcXPNp7CUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
می‌دونستین بستنی بهترین درمان برای گلودرده؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/696419" target="_blank">📅 18:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696418">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
رهبر انصارالله یمن: ما سند داریم که رژیم سعودی به اسرائیل کمک مالی کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/696418" target="_blank">📅 18:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696416">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxIWsxYqkWrLw-fjmcbzG3pjTggxy9H-KrPhlyD00mk-TWO6IeNYKb-aWp9Wfk_A4EH1uK34dsQn99s30WrTEdyHXeia8-5Bby66pookiu63Rb1WvGX4bPCegMXQCDU8zWSEmWI9mmAvMnyXz7i_-QoodRJj3XqvjxfYlT126Ol42eCW9plK9MgBSVSU0NNfmZMMRurznPudKB1KWTHefQBTp0djT1DF644HobJc1jDXSxGFumvQ3exTqZ5VYLjBhsL70O0VPYrGGHfihQ6xQitODjqTcee38KRL7MoO08xi-gYCI2FL8JwgDVXa5-6uYMfFdcqJVeDOzMU7p1of_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقدیر همراه اول از افتخارآفرینان علمی و ورزشی ایران
🔹
باشگاه نخبگان همراه اول در طرحی ویژه از جمعی از قهرمانان علمی و ورزشی کشور تقدیر می‌کند.
🔹
مشمولان این طرح شامل اعضای تیم ملی المپیاد نجوم و اخترفیزیک ایران با ۵ مدال طلای جهانی، ۳۰ نفر از رتبه‌های برتر و تک‌رقمی کنکور سراسری و مدال‌آوران کاروان ایران در بازی‌های آسیایی ۲۰۲۶ آیچی–ناگویا هستند.
🔹
هر یک از این افتخارآفرینان یک سیم‌کارت دائمی ۰۹۱۲، مودم پرسرعت 5G و یک سال اینترنت رایگان دریافت می‌کنند.
🔹
این اقدام در چارچوب برنامه‌های باشگاه نخبگان همراه اول و با هدف حمایت از استعدادهای برتر، توسعه دسترسی به فناوری‌های نوین و ایجاد شبکه‌ای از نخبگان و آینده‌سازان کشور انجام می‌شود./ تابناک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/696416" target="_blank">📅 17:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696415">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای نتانیاهو: ما ماموریت را تکمیل خواهیم کرد و همه کسانی را که در حملات ۷ اکتبر شرکت داشتند، پاسخگو خواهیم کرد
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/696415" target="_blank">📅 17:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696412">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-dB5rzbccgxHhN1afG3bdWQ0NSy2-eLP3pi4x2EAnky7lutKVR8vS6hM--JYjIoVcE7r76Cz3bN1-rCQX2gKLDqtGEnZcvQtaUs-siM19SDtuQHjv3I62SITVpptMas9ODEQ95p3W5jbVglRHguTD2ey9aXrHubQl-VNeZc6i8U1TqaZHsxvzq8TrcJjDe_saDzKKVsx_TKdSfgO8j5u_INrkepSHiK0joMbtraaCQax85ghQFEIoonmLhTeKamunnvuknJhspxVVmSYpXxcM2CSONR6mtGW-sa0qWFOuM03JWQ1l6g8q0OWsljTVg8SjclzAuec1lxRi2LSZeh7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سبزیجاتی که سلامت شما را متحول می‌کند
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/696412" target="_blank">📅 17:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696410">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e761de150.mp4?token=UFiErfs7EYGy3BRnjyg4wHF2o3bXTj8gUR8JuSUSC30wQTONMUVTv2LJZLyvo2dkjlJ3Pccu6LF3Lnr0afM9xpiy_WUnEdN7-RYU9RJT1sjSsY12aLwVsm94LpheGjuYl9FVcnUUb_fUJ2IxLEbgvQ0d86jODh20xLWjM29HkKo4MEmviR8BDXT0Ew-a7mJ0mHocZUDIDP3DYjUzvyYjoGXLgwsRK2Dwr4NKrgDqLBkTKlUvdaRvfWjfsgkNjzzlyS3_Xyc2ODDUZ3kSHHD3Ug9a1oNI3dnRu8f551lrezoGW6aHyLG5spe-s4ehdX3PN7OjBjm5pkEwuM6TwSD1S0D-DyQxTUunQyck0Gi3-YJapHrOg8xlBbSvzxV4gU3DiMKggdQ2K_IHDLdVoX5G-bzgVypF_pZ5D_7ply_bJap2y8sQe4-387992HbMhvVI_uMw5cWcuHhhjcWs9ktS0M4WFQMD0NPrqoq0n_8S18AJYRR171R6IbfOznKIPwC31D8KcK344KmXzyCSBJfs10yWlai4r7aR1e_oDc3KCjhC_8YSnlnpdGB3G8pv1zZ8movsta2GGiQSGvpHP5aBxnVRqXS0RkwHy_3KCm-IyHFl3zESELAdxZ2rOAO0AtMyT36qtqLKhf01LcCjOHsQLBfbkP_sveMMpFYeskYLQ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e761de150.mp4?token=UFiErfs7EYGy3BRnjyg4wHF2o3bXTj8gUR8JuSUSC30wQTONMUVTv2LJZLyvo2dkjlJ3Pccu6LF3Lnr0afM9xpiy_WUnEdN7-RYU9RJT1sjSsY12aLwVsm94LpheGjuYl9FVcnUUb_fUJ2IxLEbgvQ0d86jODh20xLWjM29HkKo4MEmviR8BDXT0Ew-a7mJ0mHocZUDIDP3DYjUzvyYjoGXLgwsRK2Dwr4NKrgDqLBkTKlUvdaRvfWjfsgkNjzzlyS3_Xyc2ODDUZ3kSHHD3Ug9a1oNI3dnRu8f551lrezoGW6aHyLG5spe-s4ehdX3PN7OjBjm5pkEwuM6TwSD1S0D-DyQxTUunQyck0Gi3-YJapHrOg8xlBbSvzxV4gU3DiMKggdQ2K_IHDLdVoX5G-bzgVypF_pZ5D_7ply_bJap2y8sQe4-387992HbMhvVI_uMw5cWcuHhhjcWs9ktS0M4WFQMD0NPrqoq0n_8S18AJYRR171R6IbfOznKIPwC31D8KcK344KmXzyCSBJfs10yWlai4r7aR1e_oDc3KCjhC_8YSnlnpdGB3G8pv1zZ8movsta2GGiQSGvpHP5aBxnVRqXS0RkwHy_3KCm-IyHFl3zESELAdxZ2rOAO0AtMyT36qtqLKhf01LcCjOHsQLBfbkP_sveMMpFYeskYLQ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پلیس فتا: فریب تخفیف‌های وسوسه‌انگیز و فروشگاه‌های جعلی را نخورید
🔹
بررسی اعتبار فروشگاه و حفظ اطلاعات بانکی، راهکار مقابله با کلاهبرداری‌های سایبری است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/696410" target="_blank">📅 17:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696409">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Klma1Zp51_naL8ovXZBFmNyOUQOTTqMI58i1vSFxDHu-Xzeg0o9yjpopiCmH8yA_KH1yhJl0A7YeATMvtitttqRNBQogfPsKPN_rTXeh_9zTnoVWP1gBsK0wDCFHzF6l0knlvS0GQw46rpHRrxwczkNubT0hztdD8tIpw6CeORlOsuvnBXcjviaYnD4OXjBjHu7N3uLDR9jaD4XrGMVI4RdJSd3hvsuu_s1pSnsgcjNkFv8HcxcsMcyFPcf36yng_YCNBS21sND7iITD0rNCxktuPUo6OdTBt12IusJI_F68R6A8fqEsFNvD5QS2mQg6Vf6OojmDx6mWtdFY-dahAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ملّی‌گلد داده‌های ۱۵ روزه تسویه و تحویل خود را منتشر کرد
۱۲۶ هزار درخواست برداشت، ۶ ساعته در «ملّی‌گلد» تسویه شد
🔹
ملّی‌گلد در گزارشی اعلام کرد که در ۱۵ روز نخست مهر ۱۴۰۵، ۱۲۶ هزار برداشت موفق ثبت کرده که میانگین زمان تسویه آن‌ها ۶ ساعت بوده است.
🔹
در همین بازه، ۱۷ کیلوگرم طلای فیزیکی به ارزش ۴۲۵ میلیارد تومان در قالب ۱۸۲۰ درخواست در ۲۸ استان تحویل شده و کاربران ۸۷ هزار خرید انجام داده‌اند.
🔹
تیم پشتیبانی نیز به بیش از ۲۱ هزار تماس و ۲۳ هزار چت پاسخ داده؛ میانگین انتظار تماس ۴۷ ثانیه و چت ۷ دقیقه بوده است.
🔹
ملّی‌گلد همچنین اعلام کرده که تمام الزامات اتصال به سامانه ناظر بانک مرکزی را گذرانده و به این سامانه متصل شده است.
مشروح خبر
khabarfoori.com/fa/tiny/news-3250699
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/696409" target="_blank">📅 17:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696408">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
رهبر انصارالله یمن: آل‌سعود نقش ستون پنجم استکبار را ایفا کرد
🔹
عربستان دوشادوش آمریکا و اسرائیل برای نابودی حزب‌الله تلاش می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/696408" target="_blank">📅 17:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696407">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
معاون سیاسی وزیر کشور: شعام هنوز تصمیم جدیدی درباره انتخابات شوراها نگرفته و تاریخ‌های اعلام‌ شده برای برگزاری انتخابات واقعی نیست؛ هنوز هیچ تاریخ مشخصی تعیین نشده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/696407" target="_blank">📅 17:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696406">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
کاخ کرملین گزارش‌ها درباره دومین مورد احتمالی طاعون ریوی در سیبری را رد کرد/ العربیه
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/696406" target="_blank">📅 17:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696405">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e059daafd.mp4?token=amqswYB0gCDtGFe9LnTxJCdTMkn5UzC7wJBz1npMmKtiQsn1zBt-skjCgVLmt_aQcm5d4PdcHosAsI-CfdBmyK1He_Y03VyAQTZ2Qs0isihQ7MSLQ1skyZDJZcl3H8_uuyeb4CybTEzG2gFf3sEauGCIVIG5aC2BN3zWmwDrmUI-r8MbSq4fVih8WDbZhbTRvOSmQnDXLL6X-sYE1EpJ87QO1WC3RK-U5bgEA9rQGncTtgJSMZBxxASfupcdrTpV0zrUWq_s471sXExSAB40WE5O-fJRT_VbzgSNHlPUt9iNnfie55hPYL5ixaYaM6mDa2p_34lbED9COEn--d9NbE4az8YreSa1BtiMG7l2uuil8f_PTL-PMYH16R6EAb9qjm9aV_EvkbLl1lw8tg-BMkaRYXLGV889nTNPOe-9Y-MSTsi5Odjua-1vjwiD7QVtCVZSp5z16lQ_RpKA3AaIo_zlrQFJQnGxc7bq5ztxT4D1RwmL6X9R6ymSJ5JkjIr5MMmNJbRw-osaeWVc47-Vi5RJTKs4gquAaULKfk_O8wxTfsd0JxxpfzA7ZkRAM6Wc9C99HqXLqkEOMqqUEFeRROeWLBudt54x8OqU1w8acZYm_v4doEc3TfGKNZO3Fxc5f3oebV6hg5_eozmWIelxm5KysyKotPEI78cxYkzNxtU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e059daafd.mp4?token=amqswYB0gCDtGFe9LnTxJCdTMkn5UzC7wJBz1npMmKtiQsn1zBt-skjCgVLmt_aQcm5d4PdcHosAsI-CfdBmyK1He_Y03VyAQTZ2Qs0isihQ7MSLQ1skyZDJZcl3H8_uuyeb4CybTEzG2gFf3sEauGCIVIG5aC2BN3zWmwDrmUI-r8MbSq4fVih8WDbZhbTRvOSmQnDXLL6X-sYE1EpJ87QO1WC3RK-U5bgEA9rQGncTtgJSMZBxxASfupcdrTpV0zrUWq_s471sXExSAB40WE5O-fJRT_VbzgSNHlPUt9iNnfie55hPYL5ixaYaM6mDa2p_34lbED9COEn--d9NbE4az8YreSa1BtiMG7l2uuil8f_PTL-PMYH16R6EAb9qjm9aV_EvkbLl1lw8tg-BMkaRYXLGV889nTNPOe-9Y-MSTsi5Odjua-1vjwiD7QVtCVZSp5z16lQ_RpKA3AaIo_zlrQFJQnGxc7bq5ztxT4D1RwmL6X9R6ymSJ5JkjIr5MMmNJbRw-osaeWVc47-Vi5RJTKs4gquAaULKfk_O8wxTfsd0JxxpfzA7ZkRAM6Wc9C99HqXLqkEOMqqUEFeRROeWLBudt54x8OqU1w8acZYm_v4doEc3TfGKNZO3Fxc5f3oebV6hg5_eozmWIelxm5KysyKotPEI78cxYkzNxtU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای هر کاری از کدوم هوش مصنوعی استفاده کنیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/696405" target="_blank">📅 17:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696404">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
رهبر انصارالله یمن: آل‌سعود نقش ستون پنجم استکبار را ایفا کرد
🔹
عربستان دوشادوش آمریکا و اسرائیل برای نابودی حزب‌الله تلاش می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/696404" target="_blank">📅 17:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696400">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b60783ba4b.mp4?token=GOBco2xHq95WIIIeiKkA1T3XKTDta233oDv-aJB_sd8ctC5C9n4yUwseUapkdt13VQz76nuyGc2s2Sm28mYitthrhi22z3DcJBohn6yAVH1FfGGKdJ0WCM8Hj7UZWB2F5TB7niYG6JKW_2r3Y3UJpW1XtaM5yRitORu-2t-FrG_JZLOU1t2DRpgzySMlYg_p4Erd0aI1cwAVtcF2aKVXECCS_4PtoqqJJbZy3H47lN19lzmPJvyXkVAtxU8zNcRn-70QlWj69iUu4sXo-CuHox-s2jnl15L-ZGiLeyYzrIArnMcBVAQ6SGaDPXC4b9b64SAh9Uk8ZjJfOLDSIkXm8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b60783ba4b.mp4?token=GOBco2xHq95WIIIeiKkA1T3XKTDta233oDv-aJB_sd8ctC5C9n4yUwseUapkdt13VQz76nuyGc2s2Sm28mYitthrhi22z3DcJBohn6yAVH1FfGGKdJ0WCM8Hj7UZWB2F5TB7niYG6JKW_2r3Y3UJpW1XtaM5yRitORu-2t-FrG_JZLOU1t2DRpgzySMlYg_p4Erd0aI1cwAVtcF2aKVXECCS_4PtoqqJJbZy3H47lN19lzmPJvyXkVAtxU8zNcRn-70QlWj69iUu4sXo-CuHox-s2jnl15L-ZGiLeyYzrIArnMcBVAQ6SGaDPXC4b9b64SAh9Uk8ZjJfOLDSIkXm8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماهواره هنوز هم ممنوعه؟
🔹
اگر در خونه یا محل کار، از ماهواره استفاده می‌کنید، این گزارش رو به هیچ‌وجه از دست ندید!
#قانون_متروک
@TV_Fori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/696400" target="_blank">📅 17:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696399">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/286dd422b7.mp4?token=dgaKB-TwauyyPCtRBl3f0KjsTYUJOWnGGyo8Gl71XS7Coc50NjeGrtjSNuYgKjmtcyNKT5z2vZD-PcETELsmABt65uhh4YajaejQZbWoQiKdzf0q9kuyDPQ6tGEmCikiKjDaNaY3GyKT9Q8Gm3KI21q-JsV1BqIZqYqyDw6fBZ0lbq7vIuwX9qmQfAAlfmfbTD42J6VX-E2E-kA-_nrwrTsEs41tyuPrQ4AhtQfPk4hiDw8p_zWj2-EUqRkrd-_mIBtkpZq6CHUbSXipYZenn4N3-TOWam6LdbDUVVD7W4xtLDunMKxC-icS0nRtBgH5Fw3BCIHrv1KU4bOW67n4NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/286dd422b7.mp4?token=dgaKB-TwauyyPCtRBl3f0KjsTYUJOWnGGyo8Gl71XS7Coc50NjeGrtjSNuYgKjmtcyNKT5z2vZD-PcETELsmABt65uhh4YajaejQZbWoQiKdzf0q9kuyDPQ6tGEmCikiKjDaNaY3GyKT9Q8Gm3KI21q-JsV1BqIZqYqyDw6fBZ0lbq7vIuwX9qmQfAAlfmfbTD42J6VX-E2E-kA-_nrwrTsEs41tyuPrQ4AhtQfPk4hiDw8p_zWj2-EUqRkrd-_mIBtkpZq6CHUbSXipYZenn4N3-TOWam6LdbDUVVD7W4xtLDunMKxC-icS0nRtBgH5Fw3BCIHrv1KU4bOW67n4NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">​​
♦️
کد پستی رو چطور پیدا کنیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/696399" target="_blank">📅 16:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696398">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
وقتی زیردریایی آمریکایی «حامله» می‌شود/ ابتکار متفاوت و دیدنی جوانان ایرانی در یک انیمیشن جذاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/696398" target="_blank">📅 16:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696396">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQ9dUuwrCrapBp3triJAd_9fCv_Yd-fh6caY16aGi95g5Q1joh-CND3tSWkPST_i6jNG-6-TJB-3-qZCz8YXrwjZ-H__uDviaob0xPHb9cfsqiJZTf6f6dTBPluwQNVdIuSgkjEPhMsO01v2t2Mwk53sNpkc0a4howEp10ss1l23HmGvRXZtarPC93q1ry1xEecjshDCLHWvb2JG06S4C-2lOrREyY7znuoeX7vCpxK7-irOzfPMwTHhOKPZ0lhM3TNppi7yOFuLPMqvWPsCT2Y_eynI03oibuH_FMaX2HmiyeDoTFOf3DMJ9axmKcthJYfEz84uoUlowKKLqysskQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ: بذارید ایران، لس‌آنجلس و سن‌دیگو را با بمب اتم نابود کند #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/696396" target="_blank">📅 16:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696395">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_UFcyx12CoB2LOwN08ujhxedS1qutczj7g_LZl8RaBmA3m2YHn3yEtzDNbtw1txgKppAJP8gL24Uvk50Ldxa-OOAc7vRT9-qwmQ3pYJiCIC5Nhp8JtWKdqSySSzN-qT3X066sauIsq4YFgV1yZQe3vrS-gSMXu6JJ4Uw8w8mZHFETel027GnZfQmg1Ise8UjhqhBk1Xy5kV3qMzpUaIgU1E2Kfm83ZWpJme19UpCKSv1pn82QSOfzFnlwK9CSlj9Y_F9-3NpTPQ21a47EHjaCJhUlnX8uGW0_yie1e_4Ch8AGYkP7ejzl8FD1PZkV51WRzztJq5k4Zm3OsRIdkyVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری؛صفِ وام
🔹
درحالی که تسهیلات ازدواج و فرزندآوری برای حمایت از خانواده‌ها در نظر گرفته‌شده، گزارش‌های متعددی از عدم واریز به‌موقع این وام‌ها به دست ما رسیده است.
🔸
چنانچه شما هم ماه‌هاست در صف انتظار بانک برای دریافت این تسهیلات مانده‌اید، روایت خود را در چند جمله کوتاه برای ما ارسال کنید
👇
#صف_وام
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/696395" target="_blank">📅 16:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696394">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61ba14c07b.mp4?token=BYHjpRFd5i6i6XCNJ9Az8S9-gNO7koxzKHBtdN0S6CbK7jNj-RRLg8kl3NyMohHqZ2jbtCUrEE3XrSfLPo9XDlEzhdwZlOjtPFWmRQypBuF3vOOiq_RBLxtEdu4reCJD9RnANcKMdGdqUwsLtxyPR1-xoG6cxe-RWhGcWJrNK-_oTh6mdNywRTpfZqMVan6E0eq9xZiOop7n1K5S_UccJ_WysyAcmS040mg_i9kGIODk_yIx6YA1Jfe5UUzoZ7EgHUq8cZxkm4Sb7FdiAcsx3WuSQr0IWYYIAw5b7qSNfhzTkEl0Ge73OlKbb7p2qtbJaaPb2rQeIjIe2uatbZ8_QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61ba14c07b.mp4?token=BYHjpRFd5i6i6XCNJ9Az8S9-gNO7koxzKHBtdN0S6CbK7jNj-RRLg8kl3NyMohHqZ2jbtCUrEE3XrSfLPo9XDlEzhdwZlOjtPFWmRQypBuF3vOOiq_RBLxtEdu4reCJD9RnANcKMdGdqUwsLtxyPR1-xoG6cxe-RWhGcWJrNK-_oTh6mdNywRTpfZqMVan6E0eq9xZiOop7n1K5S_UccJ_WysyAcmS040mg_i9kGIODk_yIx6YA1Jfe5UUzoZ7EgHUq8cZxkm4Sb7FdiAcsx3WuSQr0IWYYIAw5b7qSNfhzTkEl0Ge73OlKbb7p2qtbJaaPb2rQeIjIe2uatbZ8_QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کمک‌های اولیه؛ مهارتی که می‌تواند یک زندگی را نجات دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/696394" target="_blank">📅 16:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696392">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZXWps5vV-YxgRXifnc1kitXCVvp12nmT1IQhSZ5DPL0jqrIRShUulNaxkKYktNrAR96vuOLAUqCHeA0lGqa5WTZjdcrJS6bqOlbDDs19VSzb3f5UUbDQpVDbk3mBpdMvz5Gfr_m7FiRmJr212Ct0Lv1bCu5LVv9fr1zne_aDWotSSFzpr8cNJyf5eF9ioH8Dc6H9DrnZL01fGbzbzJl8H9UUAzelYsIy2UF2SQP7oxdqbhnfSWXmFxVCQKfAAOOAOkeqb6AyB-vKGECZkCxV_N7zRzfi2qu-f8b5KK-qGHNTfJLwYdl5p_gkL908qLHwtUfAwrJIgmbBx4EbQQqp9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RY4s5YKZE_sYdy68S_X1qZs165DGtcGhGk-gBCLy1s0jU4ahjbH_T8b92xflzIB9Y6QBbFmmbzBKgie-qQDs4L46xQ13jI7kO_Ne6TuUgOqEqNAej8UKkxx0oPXMbu4Ox33SIgRZ-3YG57sUGLF4atw3BVEK3kfX38KI-Tt92RBgscIbREMt7Kf_UzW3Zjlqw0I9R0D997zExLIUcTag3yHv73NmKwbdD-_zHCB1oeyVCMUTxLxzHj7feL8JZd1ZGcrem5JWm6Wvt30Vw1NMoeWIYTXQzF3f353Ny_wZbJLZ5pGjlrY_KxQu7jV6xntg13mkyoKiDot_6YIW8fkAZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ترمز نقدینگی کشیده شد؛ سد آخر در برابر ابرتورم
🔹
براساس اظهارات اخیر رییس کل بانک مرکزی، رشد ماهانه‌ی نقدینگی در شهریور ۱۴۰۵ به ۱.۳ درصد رسیده، این رشد ماهانه کمترین رقم از دی ۱۴۰۳ تاکنون محسوب می‌شود. رشد نقطه‌ به ‌نقطه‌ی نقدینگی نیز از اوج ۵۶.۴ درصدی در خرداد به ۵۱.۶ درصد در شهریور کاهش یافته است.
🔹
رشد نقدینگی در شش ماه نخست سال جاری ۲۱ درصد شده، این در حالی است که رشد این متغیر تورم‌ساز در نیمه نخست سال گذشته بالاتر از ۲۲ درصد بوده است. به بیان دیگر، با وجود شرایط جنگی و فشارهای ارزی، سرعت خلق پول امسال اندکی کمتر از سال گذشته بوده است.
🔹
سه اقدام سیاست‌گذار پولی در کاهش شتاب نقدینگی نقش داشته است افزایش نرخ ذخیره‌ی قانونی بانک‌ها، اعمال سخت‌گیرانه‌تر کنترل مقداری ترازنامه‌ی بانک‌ها و کاهش استقراض دولت از بانک مرکزی و اتکا به حساب‌های پشتیبان بوده است. اهمیت کاهش رشد نقدینگی در زمانی که زمزمه بروز ابرتورم در کشور به گوش می‌رسد، دو چندان است./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/696392" target="_blank">📅 16:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696391">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
۷ خرجی که ثروتمندان هیچ وقت انجامش نمیدن! #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/696391" target="_blank">📅 16:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696390">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXzf1wcQaOkbTWv-Kwz_MEYn0i0PGPY30LZoRwOw118PWoM_VgnwL1zqjKa097RgQ9Bd5--m__6Ag8nsryM8e6phthCi3mHn019oldgMg3wu60jP7vEf5gkN__rHzzWA6MZwFVRK1ZvhZoytzQr_B8XiLl4zpL8ef0eppdof18JaGYLv_oPDNRkgM0OJl8FIaGkSQP7xMYUy5yIcwehtbKJXdmFIamgiPcd6gd6ccLV1Nwz6TRL3I93sj4i0h_lqlDZpFKX2C7e_odigXg01csGv0F5UCUVYmMNp7AHSUnWc6E37AV9KGvZsJTG4e-Qy6n-5eXoeYBDji98X3Ze8pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کارنامه مالی شش‌ماه ابتدایی ۱۴۰۵
🔹
شش‌ماه اول سال برای بازارها یکسان نگذشت، بورس با رشد بیش از ۹۲ درصدی صدرنشین شد و در مقابل، انس جهانی طلا ۲.۷۹ درصد افت کرد، در حالی که بازار داخلی طلا مسیر متفاوتی را طی کرد.
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/696390" target="_blank">📅 16:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696389">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee74ed68c7.mp4?token=cgm0oWFpixNxE0lGbyl-AMUt4SGzKze0AOKXDF-2NQOYx7kP47v9uZgxxokEODrvFTImNXe5BYkxkwOLIIdvMN8iDmUhZ4pbqLx05BmIxpA6Os58YMEePIUr3Q0wpzJiOl8P2YZOkPOIKAaMVhPwrwMvqoBoSmSkcS7dzMJ5OSCUKAYZOaIc9qufrr57SUW0Kc4VKBdWLM2WU963C5veKBsCbLWsWr41vvGzcPTjTE6Y9SQXBcivutiSWnb7JZwQJ6hn84iAOQoL9Zk1Z1roLsIAxd3mFyjNfF77gQKvoF_PJ23MaTdho647APPWaQn0s8HPTaORFiq_sg7938tNAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee74ed68c7.mp4?token=cgm0oWFpixNxE0lGbyl-AMUt4SGzKze0AOKXDF-2NQOYx7kP47v9uZgxxokEODrvFTImNXe5BYkxkwOLIIdvMN8iDmUhZ4pbqLx05BmIxpA6Os58YMEePIUr3Q0wpzJiOl8P2YZOkPOIKAaMVhPwrwMvqoBoSmSkcS7dzMJ5OSCUKAYZOaIc9qufrr57SUW0Kc4VKBdWLM2WU963C5veKBsCbLWsWr41vvGzcPTjTE6Y9SQXBcivutiSWnb7JZwQJ6hn84iAOQoL9Zk1Z1roLsIAxd3mFyjNfF77gQKvoF_PJ23MaTdho647APPWaQn0s8HPTaORFiq_sg7938tNAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نجمه جودکی، مجری سابق صداوسیما که سال‌ها اجرای برنامه‌های تلویزیونی را برعهده داشت، این روزها فعالیتش را خارج از قاب تلویزیون دنبال می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/696389" target="_blank">📅 16:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696387">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsH8k4znQzXRQO798YAioY5YsoTNq-Y3L-nlDYsMS-sYm-0-8tx8Wv0Zqe49_MTLmYumyegEiCGWPjcGESDEzmxr2mHmjpc9VEP-ma9Dnu3BfWZTy5z-ej0nTCltEcydCRZO0RBTiQgKE0JfByLeLweY8MTsquv8YCuFUzZtY8NTSnFcNSxunlmC4kMnpcEVpzg7akhKhi-r97AQnthwT6ClkQQc_gAtZ1S2a9rgnjTuFGdPpG0ew_qQrm7BlWIl3EVWetzmBqcGW7A8sIyKPaqC-AcEiJFqLpR1j3gMeblFEGE6wc29Xn39OzfAi_V8n3bodSw78f0UyzMHJalykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان افزایش قیمت محصولات ایران‌خودرو در مهرماه ۱۴۰۵ نسبت به لیست قیمت شهریور ماه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/696387" target="_blank">📅 15:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696386">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
امکان فاز جدیدی از جنگ وجود‌ دارد
احمد نادری، عضو هیئت رییسه مجلس شورای‌اسلامی:
🔹
شروط‌ خود را به واسطه قطری‌ها به آمریکا منتقل کردیم و آمریکایی‌ها اعلام کردند که شروط ما را نمی‌پذیرند و شروط جدیدی اعلام کردند که مورد توافق ما در ایران نیست.
🔹
بارها اعلام کردیم که مذاکره هسته‌ای نمی‌کنیم و ما بر سر تنگه‌هرمز و منافع ملت ایران مذاکره می‌کنیم و اینکه گفته شده مذاکرات در بن‌بست است، مقصر آمریکا است و امکان فاز جدیدی از جنگ وجود دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/696386" target="_blank">📅 15:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696385">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
آیت‌الله جوادی آملی: گاهی برای باران ضجه لازم نیست؛ عدل دستگاه قضا کافی است. عدل را جاری کنید
🔹
این بازی‌های گران‌کردن عمدی را کنار بگذارید، این معاملات ارزی عمدی را کنار بگذارید، کارهای عادلانه انجام بدهید، حکم عادلانه انجام بدهید، این بیش از باران چهل روزه برای شما نافع است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/696385" target="_blank">📅 15:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696384">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6fd5d605a.mp4?token=PEOsnsvXJOyap1hqCAPgq2juVq8M24A7qdZI10hzA1AQOwMvci3mm1YzZxCjJWBy1yEtDc3b71Rg8xWnlwTHU31g-CUKtmYs45XYTpjjqa4lsBuZZDeOjxw87_sM14pQYZsICBhuYVtsrIwQLt_tJRa7nTI0juztkbrNobppp6zwfeDJ0c-LuAge8cDPotRl-BuEhbUhOGvG5JSlbirP1E-JIlVk3_Cr6WCfmBJmwmHAQ8NGMuvSZHGNys43RU8EwjdoeASqTl4lNIQ9XJNcQM3LV8XiqmsQXz6e8xHroe-4Yix2szK5chlqA7H5uR2RJkHelNw4rlYQkvWTUlK6Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6fd5d605a.mp4?token=PEOsnsvXJOyap1hqCAPgq2juVq8M24A7qdZI10hzA1AQOwMvci3mm1YzZxCjJWBy1yEtDc3b71Rg8xWnlwTHU31g-CUKtmYs45XYTpjjqa4lsBuZZDeOjxw87_sM14pQYZsICBhuYVtsrIwQLt_tJRa7nTI0juztkbrNobppp6zwfeDJ0c-LuAge8cDPotRl-BuEhbUhOGvG5JSlbirP1E-JIlVk3_Cr6WCfmBJmwmHAQ8NGMuvSZHGNys43RU8EwjdoeASqTl4lNIQ9XJNcQM3LV8XiqmsQXz6e8xHroe-4Yix2szK5chlqA7H5uR2RJkHelNw4rlYQkvWTUlK6Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماهی‌ای که راه می‌رود! این ماهی عجیب با لب‌های قرمز به‌جای شنا کردن، با باله‌هایش روی کف اقیانوس قدم می‌زند!
👣
🐟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/696384" target="_blank">📅 15:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696383">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
افزایش اعتبار کالابرگ به روزهای آینده موکول شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/696383" target="_blank">📅 15:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696382">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
وزیر علوم: نتایج نهایی کنکور نیمه دوم آبان اعلام می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/696382" target="_blank">📅 15:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696380">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
سفارت آمریکا در موسکو از یک مورد مشکوک به طاعون ریوی در منطقه ایرکوتسک خبر داد که به مرگ یک نفر منجر شده است و از شهروندان آمریکایی خواست روسیه را ترک کنند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/696380" target="_blank">📅 15:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696379">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e2e017639.mp4?token=RhKY4oQeN_tUDMhSsbDT9JYgzBaPG7G7xr6grD5sSL86KsO8FqqBUK4Nt1hRpb7sW4M128uvOH788d-ntfFXOMt_HuhXzwMRqLoBqXaMKiqgw814yW5mQu7V6-BxaMdYmqH_8muWesDdfrYSE9FFRsxqWxBMsLn3DUzJVTlg_LKsexhE8eDoVHSamzvpKfxpuL7HFKJS_LwhSvu_m3eYwMPknOgMfiN88WAwlmU6oFbd66gvL7Ajw19F-EcTXeBp0WuFrOnU25k1cbA3eAe8P7YjIxZU8x2rL-zYsLBPco6bX6JALVc4pYIeRddDXrUZBYTCvRKusRNUuJv9cuPtvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e2e017639.mp4?token=RhKY4oQeN_tUDMhSsbDT9JYgzBaPG7G7xr6grD5sSL86KsO8FqqBUK4Nt1hRpb7sW4M128uvOH788d-ntfFXOMt_HuhXzwMRqLoBqXaMKiqgw814yW5mQu7V6-BxaMdYmqH_8muWesDdfrYSE9FFRsxqWxBMsLn3DUzJVTlg_LKsexhE8eDoVHSamzvpKfxpuL7HFKJS_LwhSvu_m3eYwMPknOgMfiN88WAwlmU6oFbd66gvL7Ajw19F-EcTXeBp0WuFrOnU25k1cbA3eAe8P7YjIxZU8x2rL-zYsLBPco6bX6JALVc4pYIeRddDXrUZBYTCvRKusRNUuJv9cuPtvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فلش کوچک کنار علامت بنزین در داشبورد ماشین، معنی‌اش چیه؟ #حواست_هست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/696379" target="_blank">📅 15:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696378">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
کالابرگ دهک‌های پایین اضافه نشد
🔹
بنابود رقم کالابرگ دهک‌های پایین از امروز اضافه شود؛ اما پیگیری از وزارت کار مشخص کرد، رقم اضافه شده تا لحظهٔ انتشار خبر واریز نشده است؛ علت این مسئله به نتیجه‌ نرسیدن این مسئله در دولت است./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/696378" target="_blank">📅 15:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696377">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d235cc55b5.mp4?token=Uq6vrcfdrDUn5f4kwjA_AhKix6-Le8Ij-MvhVJaKZPvn1aGH5vOxI9nIBD-3XSxUzFuHE3of0SsbOEn7hPnhuNP5n3uraInKOIOlzM6ztxfstFbccw_FiWimR_dGMmoZeST3a9IVaaEMeSq7nubsKwXFK04QBs0r-1iOVn7ZtRULonGwBh2FlyqgGv2HWVu63vJqTWw8i9TV9HNyS8omuwUZi7DzDPdCs6ed5rxr1WMAErtjaMFHr2EeCHLwbBwge4YNMqLsEbrzOxgWgMBuR3GnnoRFjPltFfAxS_HaH_tnNWmfvoCX9ZSbeWfXabxg11zCBgmqa6TB1rSD7h3wXawutLgrQ6R6teYvQlhfJd5aNalNUX2pX2qt7meuhjPgDMp5WFvLVkmXtJc1IiDqbwL5XsxiELiN1SseIbbhKcJvXnUQjl2xOLPwLzIhKuiMyZLq0MQ1Y9qH3wA6o9WXEmMm32_SEVqWFplBg-0xRmb7h-PS0eupNiXEnCmzPAVJ_jJlssT8ecwT7uspSygIeK4oJ_uq6QdyH_r6SybYd4nLQHwFI7oQDdwFc7KMcLFvoH-6UhtmxaJtbHjUYPhVlAXdB6W1ghu9WE-wCd7CPb66geKlpxzqm7kFF2hFBWQ2-5LTVX8sbYT-nZSlVR8q2Kvj8CPfHxqCLcI1kyOZGUE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d235cc55b5.mp4?token=Uq6vrcfdrDUn5f4kwjA_AhKix6-Le8Ij-MvhVJaKZPvn1aGH5vOxI9nIBD-3XSxUzFuHE3of0SsbOEn7hPnhuNP5n3uraInKOIOlzM6ztxfstFbccw_FiWimR_dGMmoZeST3a9IVaaEMeSq7nubsKwXFK04QBs0r-1iOVn7ZtRULonGwBh2FlyqgGv2HWVu63vJqTWw8i9TV9HNyS8omuwUZi7DzDPdCs6ed5rxr1WMAErtjaMFHr2EeCHLwbBwge4YNMqLsEbrzOxgWgMBuR3GnnoRFjPltFfAxS_HaH_tnNWmfvoCX9ZSbeWfXabxg11zCBgmqa6TB1rSD7h3wXawutLgrQ6R6teYvQlhfJd5aNalNUX2pX2qt7meuhjPgDMp5WFvLVkmXtJc1IiDqbwL5XsxiELiN1SseIbbhKcJvXnUQjl2xOLPwLzIhKuiMyZLq0MQ1Y9qH3wA6o9WXEmMm32_SEVqWFplBg-0xRmb7h-PS0eupNiXEnCmzPAVJ_jJlssT8ecwT7uspSygIeK4oJ_uq6QdyH_r6SybYd4nLQHwFI7oQDdwFc7KMcLFvoH-6UhtmxaJtbHjUYPhVlAXdB6W1ghu9WE-wCd7CPb66geKlpxzqm7kFF2hFBWQ2-5LTVX8sbYT-nZSlVR8q2Kvj8CPfHxqCLcI1kyOZGUE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معمار شگفت‌انگیز طبیعت
🐦
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/696377" target="_blank">📅 15:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696376">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bf0bcb3a0.mp4?token=hgT-cm2yWeza8g_HSBaUjZTSnTXWq7AnFoNtrz31hs86pIQRn3gHt-Q5VLOcR5xDOu928nnN7wRwfPFTdrziiD75dQDXUH0QxcSmhBIintS_fpiyNXmvaM_70_SYGwSXDD-5qmT4J4lCx0RDRNT5Wr-A4JkLl-R8zbu18Je4ctxEoMPjP7NaWrba4NSm1zlmPe_BvVNoq_TrCPgel3PPOWFSQn5xmm0sXfefd_yCvhTKIJmqhKR29gQZ_hcmFTpxFMhDPWmWASY5AWuOVxmpynCpvq5RW6xwcvG2eW7wAqXIO1uk5fWEUPqmIP4g1ER5QCCyjs9Yqh-5UG6vsxHJkBuwotE-RrQz58TpZ1H0rr52jUvo4OmI3sFbHWVVFTBoYn2-yNAVq5WtVklG1QB3n3743CkqZ6J6pV3sVI4iP97X0q5Yh8IeMJOSfDjAFc6pu8NfeMa9EAWjXxC5D60L55vTH03Je0Ptm-QHTbtXFEFbiesRJzgoQOl3vktqyxsnfl5jZRKL4nG9r3cOmYNmMNlR3_6s8LSVnuwlAIGIx6gMyfmUG5nLmWIaDfHtdue8Qt_vgCWNy2Q0qxGS3O9CUoViuC6CxT3Gb29T1SQKrvS-OGU1x_ZlRWhbKVoKXTuNGnswdiuHNM46xFlIAWiQZpGrmWEa5Swg-w78djA8C3o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bf0bcb3a0.mp4?token=hgT-cm2yWeza8g_HSBaUjZTSnTXWq7AnFoNtrz31hs86pIQRn3gHt-Q5VLOcR5xDOu928nnN7wRwfPFTdrziiD75dQDXUH0QxcSmhBIintS_fpiyNXmvaM_70_SYGwSXDD-5qmT4J4lCx0RDRNT5Wr-A4JkLl-R8zbu18Je4ctxEoMPjP7NaWrba4NSm1zlmPe_BvVNoq_TrCPgel3PPOWFSQn5xmm0sXfefd_yCvhTKIJmqhKR29gQZ_hcmFTpxFMhDPWmWASY5AWuOVxmpynCpvq5RW6xwcvG2eW7wAqXIO1uk5fWEUPqmIP4g1ER5QCCyjs9Yqh-5UG6vsxHJkBuwotE-RrQz58TpZ1H0rr52jUvo4OmI3sFbHWVVFTBoYn2-yNAVq5WtVklG1QB3n3743CkqZ6J6pV3sVI4iP97X0q5Yh8IeMJOSfDjAFc6pu8NfeMa9EAWjXxC5D60L55vTH03Je0Ptm-QHTbtXFEFbiesRJzgoQOl3vktqyxsnfl5jZRKL4nG9r3cOmYNmMNlR3_6s8LSVnuwlAIGIx6gMyfmUG5nLmWIaDfHtdue8Qt_vgCWNy2Q0qxGS3O9CUoViuC6CxT3Gb29T1SQKrvS-OGU1x_ZlRWhbKVoKXTuNGnswdiuHNM46xFlIAWiQZpGrmWEa5Swg-w78djA8C3o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا رشته دانشگاهی بر برند دانشگاه مقدم است؟
محمدمهدی محبی، روان‌شناس:
🔹
دانشگاه محل تحصیل ۴ ساله است، اما با رشته‌ای که انتخاب می‌کنید یک عمر زندگی و کار خواهید کرد. اگرچه برند دانشگاه در برخی استخدامی‌ها مؤثر است، اما اصالت با انتخابی است که مسیر شغلی و حرفه‌ای شما را شکل می‌دهد./  تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/696376" target="_blank">📅 15:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696375">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
مقام ارشد ایرانی به رویترز: هیچ مذاکره‌ای میان ایران و آمریکا درباره برنامه هسته‌ای تهران در جریان نیست
🔹
آمریکا ابتدا باید شروط تهران را بپذیرد تا موضوع هسته‌ای قابل مذاکره باشد.
🔹
به‌رسمیت‌شناختن حق غنی‌سازی ایران از سوی آمریکا خط قرمز تهران است.
🔹
پیشنهادهای آمریکا درباره برنامه هسته‌ای ایران با مطالبات تهران در تضاد است.
🔹
ایران هرگز از حق خود برای غنی‌سازی صرف‌نظر نخواهد کرد، اما جزئیات غنی‌سازی می‌تواند بعداً مورد بحث قرار گیرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/696375" target="_blank">📅 15:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696374">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d380be51.mp4?token=pP1Z7LKgSVHN2yOgAmmVcipMEjkG1_9i3Zmx4c-8THyF5c726yOjnqkalJMo4N7HAZUYJta3oxSyat2qZOuNkI3wwuC08pswI3wHbcdU29nJlGxFhfALiVNQBNLiJQIgFqLNHsanZ2ZGJ5ZoAFM0xn4O7lHAszLAAkX1FH14vu0ynrovejg9Plt_5XOgQ3riGDoe6FEorp987Q7GIR6XPZ8GMW9Duwc-2ADuJiCCBE-tYAFBL4iD6mlS1ZlIjfWfAfPBDIT5dAu-g6_O-h3Z9nOJTu6SeghvxrJAJPtZ8leUSMxH_JWAnFHNgiZasWlqUR20MtX2l5R1VnC6t56_Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d380be51.mp4?token=pP1Z7LKgSVHN2yOgAmmVcipMEjkG1_9i3Zmx4c-8THyF5c726yOjnqkalJMo4N7HAZUYJta3oxSyat2qZOuNkI3wwuC08pswI3wHbcdU29nJlGxFhfALiVNQBNLiJQIgFqLNHsanZ2ZGJ5ZoAFM0xn4O7lHAszLAAkX1FH14vu0ynrovejg9Plt_5XOgQ3riGDoe6FEorp987Q7GIR6XPZ8GMW9Duwc-2ADuJiCCBE-tYAFBL4iD6mlS1ZlIjfWfAfPBDIT5dAu-g6_O-h3Z9nOJTu6SeghvxrJAJPtZ8leUSMxH_JWAnFHNgiZasWlqUR20MtX2l5R1VnC6t56_Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صاعقه شبانه بر فراز برج ساعت مکه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/696374" target="_blank">📅 14:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696373">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
مدیرعامل شرکت ملی پخش فرآورده‌های نفتی: با اجرای نرخ سوم بنزین، مصرف ۱۲CNG درصد افزایش و مصرف بنزین ۳ درصد کاهش یافته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/696373" target="_blank">📅 14:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696372">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ta4yZkCLErz_46ektoAr_RpBnXCOGqlW1vIcFHAL3WpePdoqVJr0isjpLl_EEJI0eMolrjpT1vED88oMm5ilHN59RjaLiIq3Rbm2UouGegYtXrXzhI43HjFViU4yvWymNEwAF_nQomFK5yoJHz-6o6qRe0JCmuAo-dW1n_E06qwSJ4wfue6yHx6etyRjVDS_8q0I5jpMLGPkDYzhapW8xCZW0vI5QJ6Sslfw8sc1ZsCKKGoCkupGUywfQTYSZeMlLNTGA45IxLKRQGVYk5j-BW_L7ddp5PUylH8933t1mg0_J2NbcaC-L361yH4u2VTnqBkRsvq1bI3ycwdirRompQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
متکی در اتحادیه بین‌المجالس جهانی: به‌زودی حکم قصاص قاتلان رهبر شهید صادر می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/696372" target="_blank">📅 14:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696371">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
پزشکیان: نیاز باشد برای صرفه‌جویی مجموعه‌های فرهنگی و ورزشی تعطیل می‌شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/696371" target="_blank">📅 14:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696370">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOTKYiPoTEpsi0X7f6ym5yBLRMVgdeSrY9Kb5R27YXMQmB0Rx_2Y7Ab1Ms4F8Dd0a5GoIjOEBcK5D_bZFsD_RGYh86A8jyXWqHo26j5kwEVQOAIaPvMnviUTcXJ3Bz-4PglcbJcPNGjkr2IIOJMIY6ftNqjsK2xpvS26Nbj1TxrgTBJDDb_1BrwctApaNaYuYhcAidY6EcVOqc3O8dghN0IXKV675-5PRNYRMv2PqoEit5t37BcZ7dyse59TfNj5dOQCC8tRENUjc7Zlyt-GE0X7Oa4I9tYikA76pnc58wnVL-GwzuCF2zDj9utMyE9WgnAFNb8_JT_7Y6Y-n_CH1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکسی از کنکور که در رسانه‌های خارجی وایرال شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/696370" target="_blank">📅 14:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696365">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xv5x9CeM76utk8aMxQgcJHZHGJnJ7X06gesmcYF73bl_lFwSwGXj3MAoLN58YdCejpi8vfIFBw4Lmo9r8IfNz_8S9DOokEn3B5WDFq4SbTTywNkNBD-UqaZZgx9SBgpK5Zwc9wlHbR6W5_eIubom-HEoaZffVMetm7XpmSfoJthBA9NqmOoOFQNxewnZyKsAIa0QTOr8X5x0075Giul1oymey7GZMfcwoN0miu2W4LwXYVJsJiE4DjXnhLtj3xDa_QOVroV5VS9wS2CJXo7m8bJl-KNo2pHOQk_3bMu-DZcZBBboHiJoqf7L9nyCimXmH_t9Ugeg97HeZX6UZ6F16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h-w-EudWUPi3cPu4KXeaixnFrxdean9jF1BfGwDuly6s0mnDx2LNAIOZ7NrP1R4V7aWvVT1DDjuFQ_47-szjvNdXux8XDxO9Jb9HG8xkdN0P1GZUIFxhcHV3X8Fd-CMgVBpXH-xvuF-TwxHD7aOqWM5AHnrnSV13zlOIuTKZTvpnz2z2hiGvXcDwCuBP_BrJcWpLPleM0unj1nidrQBYVvBTCR0zoKZ00Pc42awDvxpwXZbiKce7DYem09fHFCyLtolbRw5Zpr2X9_C4WBpLutVgYP1vUySgliE27qG6r5WwiggqAf2KsrZR1ScWGffNAtxSTtY5JflcRVPl8ziA6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hUuB-cCqFGnRb5lBtqZRfTpjW8tXX9NkpihzCF69PgpUU5a_TlpAQF-K-Tmq8aRE4HUasjBolGyM5fpuaLNBLMEDdS84sxalImEtVxiRjLjqiLVejAb8gOKalfgf_QKvYWuCaGu-Oa9AERE7YeC4fSshZVYPOh-LFdfkdllCY5MWXxRUCi88XMbkR6a4cHc3CEBXgjMt6srz4-m6ynZeovg5NqjkAI6aeb8PoJZzQfdwLfMd--0MfpR0qSS05BhcGNyLmJgIIkqcLR8G612m97Wan1MwfMNC_l2QN8iAHtI5vq5p92oPKBjDrpxt8gK56NvnTl7XJowM2ttNPiS39A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EFSKYVrXc-96Zlzsxq8oU-fC-z0QCuNSh5C3zt3A0XfqWVh4cQaO2YivDOAlQaWoVPv05kpohIMoYgUhxFKh3YAiNE3UUq2NR9XvWmqRB1Dhw8bS3V_sKpSexWMKpx0di6gtRXM0fV4zAHQ94fU8RUUIr9Ar0kfs8ac1uUeZSvhG9ARbxe5E14GRqYMIvBm9H39Qmg6Fk604CmRWOwiRaFUeZgB7JUM3t2WtWoNlzZ4oZRXUD-1Qw65ZK8Nzwwb_3083gidnu08y1kjzTDNF0erSiVB_MzJFTQF1zIZWfybmjO0DEfo_fJUBAk6HjhxH5bOoTQyfJoaTRM0BcxFuHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o-ixahc85BNDnmXetBoPoT0So9s8tf3H1GVsjaEjwH0K-w4ttcK-3XYD-X4mHqasAoBFVnyYE2hzdV0akT-12CfPAruwh4t7XFGHG0uvFuAlZH0svd2P7bdSMImR1jTv1wF1NB8ffDqbnDhCsm73Q4Itui-sLCD1lt6L2P50H6qzKzFhs0HReiO6FxuxW30OltqcOx42Uq2VVOOELyZkXkjysn0AwlpmOD_oeZzaujFVkAfJDNkCcnB5pnsB4jy8UbwoZE-b-f_iMvI22HE6XPcFPBCfrd-5yWIPEAPMHq0qiJitIQ5dDPCovQ25QteRUXtQmm5TcHyWpE_E3N94Gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
در پاییز امسال با ترکیب رنگ‌های محبوب و شیک سورمه‌ای، متفاوت‌تر از همیشه تیپ بزن #فوری_استایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/696365" target="_blank">📅 14:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696364">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4021c26655.mp4?token=NI_LG2_OgjsMPkRwGeKcs4PNTy4DIU4MKoA0tleQxb0EH8rueB0gtkgqWDX3jnBwUNcLcecaxpL2iw-Vh_Y9hPjo_ROiduztGVUDzD3fUSbx3N0alz6El6pUMulC7Yfttve0zypMxXTx5eCiFmoIYj6dibgWNsOkl_S9yRpFxS0cuyYuKRDaj9s4XPvPNNJyqW1BijA3DLd7GWS-9U3mDgazj6NoHHyLMJ6V2FVCzaWJrPp10VUy5vZHJaKemfaIsU1lv_YPZv197Px5Vznq-jz4jEl6DiV48SLKSEveWQna8dtMpY1yfgA04dhFHikXySmFGlUXMMZRlBWrkHEZJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4021c26655.mp4?token=NI_LG2_OgjsMPkRwGeKcs4PNTy4DIU4MKoA0tleQxb0EH8rueB0gtkgqWDX3jnBwUNcLcecaxpL2iw-Vh_Y9hPjo_ROiduztGVUDzD3fUSbx3N0alz6El6pUMulC7Yfttve0zypMxXTx5eCiFmoIYj6dibgWNsOkl_S9yRpFxS0cuyYuKRDaj9s4XPvPNNJyqW1BijA3DLd7GWS-9U3mDgazj6NoHHyLMJ6V2FVCzaWJrPp10VUy5vZHJaKemfaIsU1lv_YPZv197Px5Vznq-jz4jEl6DiV48SLKSEveWQna8dtMpY1yfgA04dhFHikXySmFGlUXMMZRlBWrkHEZJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراگیر شدن اسلام در بریتانیا
🔹
می‌خواستند اسلام را از بریتانیا حذف کنند اما اکنون ۱۰ درصد کل جمعیت بریتانیا مسلمان هستند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/696364" target="_blank">📅 14:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696363">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
سخنگوی ارتش: از ابتدا این فرض در نظر گرفته شد که شاید درگیری سال‌ها ادامه داشته باشد، بنابراین تسلیحات لازم برای یک جنگ طولانی را داریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/696363" target="_blank">📅 14:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696362">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما مهم‌ترین دلیل احساس تنهایی در جامعه چیست؟</h4>
<ul>
<li>✓ استفاده زیاد از فضای مجازی</li>
<li>✓ ضعف حمایت‌های اجتماعی</li>
<li>✓ افزایش فشارهای اقتصادی</li>
<li>✓ کمبود اوقات فراغت</li>
<li>✓ چالش در روابط عاطفی</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/696362" target="_blank">📅 14:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696361">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
سردار نقدی: مسیرهای غیرقانونی را در تنگۀ هرمز مسدود می‌کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/696361" target="_blank">📅 14:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696360">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
سردار نقدی: مسیرهای غیرقانونی را در تنگۀ هرمز مسدود می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/696360" target="_blank">📅 14:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696359">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a86cc6136.mp4?token=KAYJsubaJWtG0QTsqiKVc8CsVsMkfFWHfGTAPrPVTw-sI8OMfnDOPgUC9CIG5ZOPfO-nymlGxjg4bO2Uw41O1mAeIUfYXWzg_5e7cAJ_Fli44chpHfHRBPrivRAXOE3_k1E5sG6PhaDLOJjCBK0Ghez-hxwDs37j9cN6sdamWijcObjKczvQzIqIR2IiPemRMWMJfy2_DVHKyVhJcCw9Sg7nC-PVzXf47x16hGDuQ6CE5tNrDoQRsvfcMmhVbZlr5LLTCh2wOLZcknQmN1ge7OQ6O0QYiKBns2UNj3hlJHG5WN7Nue2SGu1jmqf5nCyh4oI1xFbaIZ5lJFSKeqIxbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a86cc6136.mp4?token=KAYJsubaJWtG0QTsqiKVc8CsVsMkfFWHfGTAPrPVTw-sI8OMfnDOPgUC9CIG5ZOPfO-nymlGxjg4bO2Uw41O1mAeIUfYXWzg_5e7cAJ_Fli44chpHfHRBPrivRAXOE3_k1E5sG6PhaDLOJjCBK0Ghez-hxwDs37j9cN6sdamWijcObjKczvQzIqIR2IiPemRMWMJfy2_DVHKyVhJcCw9Sg7nC-PVzXf47x16hGDuQ6CE5tNrDoQRsvfcMmhVbZlr5LLTCh2wOLZcknQmN1ge7OQ6O0QYiKBns2UNj3hlJHG5WN7Nue2SGu1jmqf5nCyh4oI1xFbaIZ5lJFSKeqIxbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آستین پلیور قدیمی را دور نریزید؛ با یک ترفند ساده به دمپایی گرم تبدیلش کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/696359" target="_blank">📅 13:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696358">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
طالبان بادبادک‌بازی را در هرات ممنوع کر
د
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/696358" target="_blank">📅 13:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696357">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیتنا | CITNA</strong></div>
<div class="tg-text">📌
مدیرعامل
#رایتل
: شایعه ورشکستگی رایتل صحت ندارد/ زیان انباشته رایتل طی دو سال اخیر به صفر رسید
مهدی فقیهی، مدیرعامل رایتل در گفت‌وگو با سیتنا:
🔹
شایعات منتشرشده درباره ورشکستگی رایتل پس از انتشار آگهی واگذاری
#سهام
کذب است.
🔹
این آگهی در راستای اجرای سیاست‌های کلی اصل ۴۴ و قانون برنامه هفتم منتشر شده و رایتل طی سال‌های اخیر سودده بوده و زیان انباشته آن طی دو سال گذشته به صفر رسیده است./
#سیتنا
برای مشاهده جزئیات کلیک کنید
💬
CitnaNewsAgeny
🎞
CitnaNews
📷
Citna.ir
🌐
@Citna94</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/696357" target="_blank">📅 13:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696356">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
قالیباف: دشمن به‌دنبال ایجاد ناامنی در داخل کشور است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/696356" target="_blank">📅 13:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696355">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead6407763.mp4?token=OhOIs61HhiIMXUqFkjcFhHJGp4jd-P9oGFJfsY36POdKMYwTUKY1u-3AKJHEFAJmLIBVTESVwRIF7mqo5fBBOgvRutDNSWzLLYfsrvPgLH3zKMcK6i-07e126Ydx43AoFnRxTRNomre9KWv7N0wq3UNSxNiuRVPRv1qoZ5U-R9spTZFW6itkLwS9vGucjSk4lKyvC3RUu0IH-FDCAobHpd2jRL-DeS8mG5F6Q4ZPTWI9rSSR_NLDIh8E1wTFSlmxloywx_Q4rNGDSObYS1JQbycwnr9TGcNKUJK5SAAJjnPpwuOB08yXkiJkhFLVkafdzvZ1G8aHyukHfp7fFyPhcoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead6407763.mp4?token=OhOIs61HhiIMXUqFkjcFhHJGp4jd-P9oGFJfsY36POdKMYwTUKY1u-3AKJHEFAJmLIBVTESVwRIF7mqo5fBBOgvRutDNSWzLLYfsrvPgLH3zKMcK6i-07e126Ydx43AoFnRxTRNomre9KWv7N0wq3UNSxNiuRVPRv1qoZ5U-R9spTZFW6itkLwS9vGucjSk4lKyvC3RUu0IH-FDCAobHpd2jRL-DeS8mG5F6Q4ZPTWI9rSSR_NLDIh8E1wTFSlmxloywx_Q4rNGDSObYS1JQbycwnr9TGcNKUJK5SAAJjnPpwuOB08yXkiJkhFLVkafdzvZ1G8aHyukHfp7fFyPhcoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعضی فایل‌های حذف‌شده ممکنه در بخش‌هایی از حافظه گوشی باقی بمونن و باعث پر شدن فضای ذخیره‌سازی بشن
📱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/696355" target="_blank">📅 13:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696354">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/838bc63ccd.mp4?token=Mde3e04GDjCO-9HwQYBrKK6G4avQAksMw_cwO4rla68o1qGqqX4Fn2JHYuXtwVvoDD6LQvcMDymELElDK90_HGURbKHPSLbzFsuI8rr5DH3lqqVHrddlleaZBObxoAhKHvyysiHl3ebFmdNUHyH4ZINzQEa18AGawgwqqhK25x1HF5tCcOwQ161r7TvNwP5QAj9yRh1uzdqqKM4Is0OTP77PIZpotS79yxgrNtZ5xFfod5vBhjfjIM-iGRjXQflbPXxIXOzVVyrPXwOcjHH-8gK3D_UT69kNuib4zRmv4G4YQmbaBIAONCZxqib4QGqJ2rFhHo2WCr9Fsd8lPBTjJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/838bc63ccd.mp4?token=Mde3e04GDjCO-9HwQYBrKK6G4avQAksMw_cwO4rla68o1qGqqX4Fn2JHYuXtwVvoDD6LQvcMDymELElDK90_HGURbKHPSLbzFsuI8rr5DH3lqqVHrddlleaZBObxoAhKHvyysiHl3ebFmdNUHyH4ZINzQEa18AGawgwqqhK25x1HF5tCcOwQ161r7TvNwP5QAj9yRh1uzdqqKM4Is0OTP77PIZpotS79yxgrNtZ5xFfod5vBhjfjIM-iGRjXQflbPXxIXOzVVyrPXwOcjHH-8gK3D_UT69kNuib4zRmv4G4YQmbaBIAONCZxqib4QGqJ2rFhHo2WCr9Fsd8lPBTjJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از شعله‌های آتش که در تأسیسات نفتی خریص، متعلق به شرکت سعودی آرامکو، در حال گسترش هستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/696354" target="_blank">📅 13:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696353">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
فایننشال تایمز: حقوق ۱۰۰ هزار دلاری برای عبور از تنگه هرمز
فایننشال تایمز:
🔹
کاپیتان برخی نفتکش‌ها برای عبور از تنگه هرمز تا ۱۰۰ هزار دلار حقوق ماهانه و ۵۰ هزار دلار پاداش هر سفر دریافت می‌کنند.
🔹
ملوانان عادی نیز تا ۶ برابر دستمزد معمول می‌گیرند؛ با این حال، عبور از هرمز همچنان با خطر جانی همراه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/696353" target="_blank">📅 13:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696352">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/909fcb1fa7.mp4?token=R1iAEbqJStELVyMZuDHPRB4i2FsWOI2fMmMV1aORaE9ptti8HYM5Ko7NornuOkGhZcvoMsFO9LsZSZQ2xZnu9U78Ruqvb5VUYy5BqJhLr1XKh3d5JQmeYFMHD7IFYKXMUa7X7qe4c8_zKt1RsMzQVgKzhAK5qXD26w5bbFZOvTK8-mSXXKbEp2s-D1Jt8jtUk9Qj-I8IYjyDIFmiTen4Hkg6twr8NcX5Y-Y6L9nJ9F_u7QgzH5OCxoRe6YftH3qRB84LC5lDmIQ3wzv1EVuAXWy6Ng8o7b7PMwvw97eYa9Gvh5q0XMy6ggbsHAHI37FtT4E61DNiuRtjMw58Ro9Ezw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/909fcb1fa7.mp4?token=R1iAEbqJStELVyMZuDHPRB4i2FsWOI2fMmMV1aORaE9ptti8HYM5Ko7NornuOkGhZcvoMsFO9LsZSZQ2xZnu9U78Ruqvb5VUYy5BqJhLr1XKh3d5JQmeYFMHD7IFYKXMUa7X7qe4c8_zKt1RsMzQVgKzhAK5qXD26w5bbFZOvTK8-mSXXKbEp2s-D1Jt8jtUk9Qj-I8IYjyDIFmiTen4Hkg6twr8NcX5Y-Y6L9nJ9F_u7QgzH5OCxoRe6YftH3qRB84LC5lDmIQ3wzv1EVuAXWy6Ng8o7b7PMwvw97eYa9Gvh5q0XMy6ggbsHAHI37FtT4E61DNiuRtjMw58Ro9Ezw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه‌گویی نتانیاهو درباره ایران: کشورها حتی آنهایی که به ما حمله می‌کنند، به آرامی و پنهانی می‌گویند: «آنها باید سرنگون شوند. آنها ما را خفه می‌کنند.»
🔹
ما مطمئن خواهیم شد که آنها سرنگون شوند. آنها سرنگون خواهند شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/696352" target="_blank">📅 13:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696351">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
برخورد پلیس با شهردار سن‌دنی فرانسه در میان اعتراضات دانشجوها و دانش‌آموزان
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/696351" target="_blank">📅 13:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696349">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yv6fQIWjRuQIRgb54PYnHTyI90IZzBZ2HCtJA8I1c940zBIwtwSOU_pRBljtXrBcFij5pN6-ERyZbeZi5rGEYUoIAYSrY7x4jwE3X6tD2BVBup3MkTl4OskFqh03Z93fla8fXLStqU2mIO5YC8jjaIRKNkvBH3Da5DlO3X_IGXdMiHUNHaDUCwSnQwLfxf7dbHE1bnVgpEEq79WisMu4xbrqoI87HRT51PSzC0Qqkzuv-cc4onv5zGENNBy93yVIO10mwGw3h3uLPUaA5GVaWZxO0f27IQq9bKX3ByVlMv923p5eiOsWdM3yth6vJVgNFwCAGlKkcUBPNtQi1pWcJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oivmM-mLWa7cKt3VRCuUN45j5x1u0NLOE-cc53ntMGFm-puXaa_nxNh8mxTkkkTa6del9MnLMBlT8NF2Qy0PUgfgXPlHWzkrrShCbqbd5fYOlQS1zRRvlFR129-kc-9eePj9D_EgF_NEBbb6RdCi50e3b-eDgggaB67A3FC__1uiksW2fkBa0b7ImE0c-NV6y031UeWr5LXgYEasdF0tvy1AiIVMwNnOUsY4-PoxAJh9w6U2iG_oUNrMKRoeljeyl4eOpe0Px2Ya-lWbtpOmOdFhKj2br2zSAmvmEHv763M8clbEeDLWJHmBsrsvGExLjj5XhKtFgBdLeLY3ho6XHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اطلاعیه یک تئاتر قبل از نمایش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/696349" target="_blank">📅 13:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696348">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKMC</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f8505024.mp4?token=FWtSuZDjO1mXFZT_aoKsK2CpMs6aczwvMtPM9iJtWZCEj25mLWMVHuynrWQjHmv2TPdd7lOyLYYcdXdWF4HwNdVDheIvlarjFWSDMSPFFvMPXaBk4sE52ZJO4pWznv1Z2Akmn-BqIZVhoEtN4TUhYJkPf04NICTksU0uJVCs6aGVvGDMt6ekAK3ijWRqXzzy9L5Uc5jQ9WJazi8QtQO0l1Kxv-YAeIJJtVhjd6yq8-0UgoYAIm_rE7qI1e0lSYOz559CPXozmqCBnxL5yuy6Ijh54kFc4vPlWQvRzrJDEQB54xUZjhHqFJLDQSrlFJ5awrgfUs-Yl0UNecgVMFGaAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f8505024.mp4?token=FWtSuZDjO1mXFZT_aoKsK2CpMs6aczwvMtPM9iJtWZCEj25mLWMVHuynrWQjHmv2TPdd7lOyLYYcdXdWF4HwNdVDheIvlarjFWSDMSPFFvMPXaBk4sE52ZJO4pWznv1Z2Akmn-BqIZVhoEtN4TUhYJkPf04NICTksU0uJVCs6aGVvGDMt6ekAK3ijWRqXzzy9L5Uc5jQ9WJazi8QtQO0l1Kxv-YAeIJJtVhjd6yq8-0UgoYAIm_rE7qI1e0lSYOz559CPXozmqCBnxL5yuy6Ijh54kFc4vPlWQvRzrJDEQB54xUZjhHqFJLDQSrlFJ5awrgfUs-Yl0UNecgVMFGaAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودروسازی؛ مسیری که امروز پشتوانه ما است.
تولید در کرمان موتور ادامه دارد؛ خطوط تولید فعال‌اند و مسیر تولید با ثبات، استمرار و اتکا به توانمندی‌های داخلی دنبال می‌شود.
تاریخ ۱۴۰۵/۰۷/۱۴
#kermanmotor
#kmc
#کارخانه
#تولید</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/696348" target="_blank">📅 13:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696346">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/361f5d3fb8.mp4?token=Gda6hDigCuQdqAvf0_FcSZiDZp9UrcjsHjHS1JQJQnzYC-u7Xjm8Q4E5ZFWPdUs93tMxGwLOB4Eot4adJhCu4JTjZiciigOH3uyfnwfdC_q24-sS-98srBXcAHl-rmVUmCYBnDyMuLvOXALbCdu_GejlUSNH4rwVR152_-RRWY5-E_9Wd7MzbDZirsFHRrwITGdK1mgUl9t-ZYRecgL2Sp5hgojoL8n7LEjfGyF27_E7JspaOul4TSTCmKBrQLmxNPGb1m8P-OfOfVaHm1jTHhkgqzMXv3EoQklJNPGrVo9-AcvV8vzdMXiYu7GyGJfmzvB8PCxrkIX0-6gXaNk6uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/361f5d3fb8.mp4?token=Gda6hDigCuQdqAvf0_FcSZiDZp9UrcjsHjHS1JQJQnzYC-u7Xjm8Q4E5ZFWPdUs93tMxGwLOB4Eot4adJhCu4JTjZiciigOH3uyfnwfdC_q24-sS-98srBXcAHl-rmVUmCYBnDyMuLvOXALbCdu_GejlUSNH4rwVR152_-RRWY5-E_9Wd7MzbDZirsFHRrwITGdK1mgUl9t-ZYRecgL2Sp5hgojoL8n7LEjfGyF27_E7JspaOul4TSTCmKBrQLmxNPGb1m8P-OfOfVaHm1jTHhkgqzMXv3EoQklJNPGrVo9-AcvV8vzdMXiYu7GyGJfmzvB8PCxrkIX0-6gXaNk6uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به اهتزاز درآوردن پرچم فلسطین در جریان اعتراضات دانش‌آموزی در فرانسه
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/696346" target="_blank">📅 13:32 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696345">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f70bd7ae4.mp4?token=hm6m5VxS7QWVYgOkVPMe8xEF79TBbB_uoviuoLrqPyh0A9mecoLjCUJ2DSheaPxCN8pv9k4rg4hzt_kWsX7hCIG7xUGjsJqdHorb_cEuaQeayX2AclLZuougGyL8CezZqX-22-IGFZJyzkykxhb2KD4Zs_dwqIuQfQJIHA5jv61gvlns1-Fuj6kOfmy6qbFYP6mAuJt5sJYWAfpsfVu32_gIk4IJ32xTZCLzODrJXWGbA6ZZTLf154ZjHNMoFdalnT6qwmCXaWVYshQza0WPiwYmryyrlmR9ik5vOWoNAf7JXLHbCQUkmSCkyNAGJho80ge2kbTKOI6vM2tF8MFxvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f70bd7ae4.mp4?token=hm6m5VxS7QWVYgOkVPMe8xEF79TBbB_uoviuoLrqPyh0A9mecoLjCUJ2DSheaPxCN8pv9k4rg4hzt_kWsX7hCIG7xUGjsJqdHorb_cEuaQeayX2AclLZuougGyL8CezZqX-22-IGFZJyzkykxhb2KD4Zs_dwqIuQfQJIHA5jv61gvlns1-Fuj6kOfmy6qbFYP6mAuJt5sJYWAfpsfVu32_gIk4IJ32xTZCLzODrJXWGbA6ZZTLf154ZjHNMoFdalnT6qwmCXaWVYshQza0WPiwYmryyrlmR9ik5vOWoNAf7JXLHbCQUkmSCkyNAGJho80ge2kbTKOI6vM2tF8MFxvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازنشر به‌مناسبت سالروز عملیات طوفان‌الاقصی در هفت اکتبر
رهبر شهید انقلاب:
🔹
طوفان‌الاقصی درست در وقت خود اتفاق‌افتاد و نقشه‌های دشمن را بر باد داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/696345" target="_blank">📅 13:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696344">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d7e34da8.mp4?token=Pkr1BRhXcPhHOJaRtRjVr4VEoAvsBaJeJPGd1as-WSFhR-loTd06pNPv4-cJJhUcLqLkT-144dKIp57UcQHSA1BuKk31jDMbxQdoC9pvxPPeNhQ-8p--xfCtxH_Z5_sOfKUyt0Wob_L30cUTfL4wuFfjZ5FUbNGyzlRy23bpgW9R3i_pqtDCU28-m_9uG7cUqqd_yMp-MvjLuJmaPYL_2D7hIUAqK6LSPY8xmEzYnSClzseJ2azHBWEKi8Wx49nXykAnE9CLfU8P8oqGi2XCZDaCRgzVFbFXUXX5sImZ8QqolNRZEKwxtZ8wgReCUP03ISpxVPUQfNcKC0czrbsqiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d7e34da8.mp4?token=Pkr1BRhXcPhHOJaRtRjVr4VEoAvsBaJeJPGd1as-WSFhR-loTd06pNPv4-cJJhUcLqLkT-144dKIp57UcQHSA1BuKk31jDMbxQdoC9pvxPPeNhQ-8p--xfCtxH_Z5_sOfKUyt0Wob_L30cUTfL4wuFfjZ5FUbNGyzlRy23bpgW9R3i_pqtDCU28-m_9uG7cUqqd_yMp-MvjLuJmaPYL_2D7hIUAqK6LSPY8xmEzYnSClzseJ2azHBWEKi8Wx49nXykAnE9CLfU8P8oqGi2XCZDaCRgzVFbFXUXX5sImZ8QqolNRZEKwxtZ8wgReCUP03ISpxVPUQfNcKC0czrbsqiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علت اصلی کبد چرب چیه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/696344" target="_blank">📅 13:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696343">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKRDKtli6QdfNXSqX2Fsd3PCjYtZhnyW70WTAlOBYP-FgiNLF1wiyVpkm-tpszx0gFNOdKcSiRHcuXBgNllJFf3EE_AR0sOghwKw3S4dt8bP-XEokraOiSzZiviMJQOAYant2wzKTn-vx4e7hJUeZTNWVEniKIxMY-Inlb775g7htjkvIhFaFP47h3JKTDrXnPqmQ74DMOlVgQPWqRJwPXhLp-h15YrsK0EmW8uNQw-IDrCDCsEltJc-nmX1UEOfViS8I3b4DtiDz8cH4CqgE5qmw7wg9Hodlkzg8fGBqzF-q_i-BbV3QSWblHJQbe_XaiS_nNik6w9R2Km0sFTUWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پک ویژه سوغات رضوی
یک هدیه معنوی و ماندگار از مشهد؛ ترکیبی از عطر، مهر، قاب‌فرش و تسبیح رضوی برای کسی که می‌خواهی یاد حرم را با خودش داشته باشد.
🤍
داخل این پک:
🌸
عطر گوهرشاد — ۸۵۰,۰۰۰ تومان
🕌
مهر تربت مشهد — ۱۸۵,۰۰۰ تومان
🖼
قاب‌فرش ۱۵×۱۵ — ۱۵۵,۰۰۰ تومان
📿
تسبیح رضوی — ۲۰۰,۰۰۰ تومان
جمع قیمت اصلی: ۱,۶۳۲,۰۰۰ تومان
🔥
قیمت ویژه پک: ۱,۳۹۰,۰۰۰ تومان
📩
سفارش:
@gharar_order
قرار؛ تجلی هنر و ارادت
@ghararshop</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/696343" target="_blank">📅 13:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696342">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udCrOBeRGuX0Ffqj_QTU96VuZlmos47h0FV7k9yvRRgg0suVtF_VdaZ6d2VQCIoSgyey2_sOGxRW7Y6foNDk19WDBqFmDoRX9Ws44v_v-TIxzZ4GaLqi_ffBVUE903bt85Smxk-ylhSd4YmmyUYKApNe1_PRmtIAK5S4Xnm9xPxei1AyeOwohofBr0iTakK4toOyCZUJyiLrtYcYJtxa8RSPO0_KFeC6gxK9J9K9Fx_tLuLNT9lrE__u_ZvK6lwVAju_dg1nOihwb7ElLjdDuMIzVn0N8r-a5r2FWW_gtUGG4pGmGk_9vioesKhi4LbcP9yaaXylaEc5pf_KHL1Qdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین خطابه مجلس به سرپرست وزارت نفت
🔹
فراکسیون نفت و گاز مجلس در نخستین مکاتبه با سرپرست وزارت نفت، بر لزوم بررسی عملکرد برخی شرکت‌های نفتی و نظارت بر عزل‌ونصب مدیران شرکت‌های تابعه تأکید کرد/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/696342" target="_blank">📅 13:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696341">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjbghXOIH6-ts_b8_FgcfLjLHG0m1EujpnwUVLn6_aHxAAUuKaZRTKMdtgrHGKlPVw6Nopu1YigbTduMznQuNlk4dYFL_zNfXQuO4PF_MgmZMkYq56DtluMvNSP-5icYkBecz3rJ2Rp9nKBogLPNL9FBPa-Hnw9E4n1WyixxzJcU1xQCbuHRKeLdg0Ns1yU-M5zj4GMzAXs8ZM3nG1Dk3lho566J9bZ6_0Lo8Tc66yIuBn8W3yzIZNN-SwfcLZvzT31GrEqLLqfqyrmy7Rp2l0ZmuMXhfC9I4AwZLmpCAxZWRFK1nUYyhgOR9LNFlb1QvJ_DwrXOI-cnwAeHL-cJMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسایی با ۶۰ شکایت و ۲۵ قرار مجرمیت   کاظمی، سخنگوی قوه‌قضاییه:
🔹
بیش از ۶۰ فقره سابقه شکایت در این خصوص وجود داشته و ۲۵ مورد قرار مجرمیت و قرار جلب به دادرسی نیز وجود داشته است.
🔹
حکم ۱۰ ماه حبس حمید رسایی به اتهام نشر اکاذیب، در دادگاه تجدیدنظر تأیید و قطعی…</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/696341" target="_blank">📅 13:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696339">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGGKjfYjv5hA2QT8-0xLUwNhp4MYft-fpjeuTaeLoHyYuc07Dq5qXh3w4b51Dg--FG8PxWISy7RGFsQpbFwQIPcPoKYzcWr2qJv6jdkrrwqZiernUyh-Jn2pPru0z3maQbaPGUC7MlFBXckRsiTMvQWyrCUQuWc3imp5rjERoV7QCMJBn-s5qRwkoMLCXnQsEM2aVSeYnyAZdXpvzeYJMpXYaklEzbOkwcbLgeEHJxPEAGbPR775WNc92LWlbs989Ufjyi3RC0foNJJkXLA9VTO9AB52LPR07EQ68kRBtHTeiioizspOOvp8AIb0USMk-2gNYnDnigGQbSQN-P1wMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی انواع گوجه فرنگی ها
😨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/696339" target="_blank">📅 13:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696338">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wArVLxneWrAX4ttZ8DthecQG3w5rplSAAfKS-f70FunW_Yb8jqtcgN53RwE5eFaipxWpqJ8MJ20BAqSI303rmPaVj9Bpiezs_nYq92wJ0rFKanwU5_ZDC7AzkU-oaD-8k6ZhiscmVsq69_Dyiq-2Ay_pChcD3vETvXZucAlT6XiYjej8gYeTdwR9V8oTBGcjmvwjKTdQte0Q-qayqRaGuNDMtzvEb86U31zEf2Zj4ajFkYrNOOjVG-lvK0L27KmQ8gQt8V6Vm_2oIC5KqkX_jaUrDTBCzfe4pIqZMeeJqASXSp0plxVeB80tsWUIsZ5-xF3FGFiW78UC82zoNJaNrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هرگز اجازه ندهید کسی به شما بگوید که این ماجرا از ۷ اکتبر شروع شد!
به توییتر خبرفوری بپیوندید
👇
https://x.com/akhbare_fori/status/2107764403290394935?s=46</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/696338" target="_blank">📅 12:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696337">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118a1b3ccb.mp4?token=C79egTW_Iounx3eeJDTTWFS-9YK0zgxH_jRqssPfD5koaXKRxXlduEHvmJQ7RRYeOvJ-JFdJF7CsXyW4AMKCOVMJKbaiQWS-Nzne9qOwyAsIip_V5Picy7B8r9-N4dFLhP-LnS-ZnGTj3-bkYvuDqwxTVKL9g4-N9Mwxl1zaA1Ea5OL1nsCmwC2m9Z_EOD-PyYv7dnpK6UtKIWhvXdEqaDHEm7jzFkLfWpKWqIcT5OYhfWT_c7I--pqrN811gDTDVmIl2ntNbGLG25XmNRwV07hRtqTM4u_GxaigLpd2p1OczV3N1IQi14lAnk_IPEjYCD-vIjUjbdTh7JLGZZ-_HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118a1b3ccb.mp4?token=C79egTW_Iounx3eeJDTTWFS-9YK0zgxH_jRqssPfD5koaXKRxXlduEHvmJQ7RRYeOvJ-JFdJF7CsXyW4AMKCOVMJKbaiQWS-Nzne9qOwyAsIip_V5Picy7B8r9-N4dFLhP-LnS-ZnGTj3-bkYvuDqwxTVKL9g4-N9Mwxl1zaA1Ea5OL1nsCmwC2m9Z_EOD-PyYv7dnpK6UtKIWhvXdEqaDHEm7jzFkLfWpKWqIcT5OYhfWT_c7I--pqrN811gDTDVmIl2ntNbGLG25XmNRwV07hRtqTM4u_GxaigLpd2p1OczV3N1IQi14lAnk_IPEjYCD-vIjUjbdTh7JLGZZ-_HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور: گاهی فراموش می‌کنیم خدا به ما دانش را داده‌است که مشکلات مردم را حل‌ کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/696337" target="_blank">📅 12:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696336">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
یک تالار در قم به‌خاطر عدم رعایت حجاب توسط همسر علی‌دایی در آن‌پلمپ شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/696336" target="_blank">📅 12:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696335">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/696335" target="_blank">📅 12:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696334">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d94d6ebf0.mp4?token=R97-bFhW25ITFFILtaDaWjVQ3Ws8oO8IbjGRNjAm6rkN0jkeK3sujxD2RjBkoyeubNHxY5LayMYmvhHiie4-d0l6BzYJKbItECABUT0zS9j0R-nrePO0IIQs5pzCTREG9OVaVa4-meVHSRGAC4iFYLPgkBxx1s8loNNg-GOpfgPU0u_UVprD_Qayr11oXPEZPiXSUXh1oWvAaua8rclM39mqxL4QuAAgCHyxqn6H-C7h1y86gdTYKqRKiKgV0cV6Xp2_3ag6F7omctYz5axMaVB9GeFmR97u215k82zWHCtrLUgGLiqAJDHGJ9ak6uMyvUDq9Z-a_gPMSSoAOaI6Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d94d6ebf0.mp4?token=R97-bFhW25ITFFILtaDaWjVQ3Ws8oO8IbjGRNjAm6rkN0jkeK3sujxD2RjBkoyeubNHxY5LayMYmvhHiie4-d0l6BzYJKbItECABUT0zS9j0R-nrePO0IIQs5pzCTREG9OVaVa4-meVHSRGAC4iFYLPgkBxx1s8loNNg-GOpfgPU0u_UVprD_Qayr11oXPEZPiXSUXh1oWvAaua8rclM39mqxL4QuAAgCHyxqn6H-C7h1y86gdTYKqRKiKgV0cV6Xp2_3ag6F7omctYz5axMaVB9GeFmR97u215k82zWHCtrLUgGLiqAJDHGJ9ak6uMyvUDq9Z-a_gPMSSoAOaI6Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر مکمل را چه زمانی مصرف کنیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/696334" target="_blank">📅 12:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696333">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLOlnNttd4oL4Af7EwUZAAhkdnkOEwcZcXhDC5Mog01KeEpsn7FTwvIATHfT3J0VEgO_Ck8eEA-lwFCH9xImFcuASalXq4RX7FT9VWLfCMp_E2JQDtjqsGtUQt2hoUb3Yvs9mnCoKif-XeFkBnJscphinoGcAqJgXgx518Bs8Fiseh14DXMhiLaGxTiXw-lWos_IROPbjFeDzeDlwcvr30BUE9YQdArrRLaFgMPmBR0T6zklrledffKu0_ZLr836w5ly7_opaYosyYiQJq0i4J6MR1ULzCXomGb1aUbOT-dD1QHHXcaDHbAMMbfO5OkJhtNcGrcyAYiH2yzfqR-w_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای زهرا عبداللهی خبرنگار پارلمانی: یک نماینده مجلس در ملک مسکونی بدنبال زیرخاکی بود
🔹
اسناد موجود است. خانه در بستری تاریخی قرار داشته است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/696333" target="_blank">📅 12:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696332">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ادعای وزیر خارجه آمریکا: ایران نتوانست از چندین فرصت برای رسیدن به توافق با ما در مورد برنامه هسته‌ای‌اش استفاده کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/696332" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696331">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
کالابرگ ۳ گروه شارژ شد/ افزایش ۳۰۰ تا ۵۰۰ هزار تومانی بودجه ۳ گروه از خانوارها در کالابرگ
🔹
سرپرستان خانوار با رقم پایانی کد ملی ۰، ۱ و ۲
🔹
خانوارهای تحت پوشش نهادهای حمایتی
🔹
خانواده‌های نیروهای مسلح
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/696331" target="_blank">📅 12:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696329">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ادعای وزیر خارجه آمریکا: ایران نتوانست از چندین فرصت برای رسیدن به توافق با ما در مورد برنامه هسته‌ای‌اش استفاده کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/696329" target="_blank">📅 12:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696327">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUd2qpugJbXF53pP_XHLE6f4qkFTPXxNzyXKYFQAnc41dlygYYyapOnxxBct5eFbZB8RTV9Dd5B_qjPfyWbhw2fNwTKymwds5RImRwCCcH5fDqptjcNLL14bPxZAeOUwGGjZsN9mqLv51S-ftp2UdlOAHlntEpKDzN3ucFU1_IBDqkqepm8esVHQ0Wh8BA4XBoLSOlnERG--LIdoU60hcR05bmdgR9LCZU3WO4qve2_uIg1Ato2Q8C0E-fsCEUPxLvAMsAalnnrhTxZYlBqhJJ0gYBWL46R0vv5FHQoXjRYfvnfByDnu1a8cPY1gsNXn-H0MP2fXhOmRrOiy_Z9iEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمار ۵ ساله واردات خودرو کشور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/696327" target="_blank">📅 12:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696326">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7yk30JV70fiBXEZRaA-a3Axi98MvAZAP6n3XRjI8UUHLC3TCfZwGLJz24gWNC8vchIPj4wtS1uQsXD9aGkmSoeQdtzpudKmDWYSL7sTPZ37iR8s9HFgAZ6xEx7n2T-D0IkTZf7BzIK2WNUMOn0pMrUTJQF1_4smjlyqHzN9VBz6d0CWLc8SZjDQLf7gBn9tP8w_nndIacJ-B2kg7AA7QnoXmws5MA2wCNykdAy9UUzoYomDJpY2f5i4eB_6VOk4R3Y50p0xPsu0uahwjRuG4d4ZgAKHBK2REi4t_0zApPnwbH-Z_PnGHDKPcxpSZ7buykukUCMTgik-tTXvszfMHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زاگرس دارو در آستانه تصاحب «شفادارو»
🔹
عرضه بلوک مدیریتی ۹۰.۵۲ درصدی «شفادارو» با ارزش پایه حدود ۴۰ همت، در حالی انجام می‌شود که نام «زاگرس دارو پارسیان» با نماد «دزاگرس» به‌عنوان خریدار احتمالی مطرح شده است.
🔹
حدود ۲.۴۵۵ میلیارد سهم «شفا» با حداقل قیمت ۱۶۲ هزار و ۸۳۰ ریال عرضه می‌شود و در خرید شرایطی، حدود ۱۰ همت باید نقداً پرداخت شود؛ رقمی معادل ۱.۷ برابر ارزش بازار دزاگرس.
🔹
فروش شش‌ماهه نخست ۱۴۰۵ دزاگرس با رشد ۲۹۴ درصدی به حدود ۷.۱ همت و سود خالص سال گذشته به حدود ۱.۵ همت رسیده است.
🔹
«شفا» مالک شرکت‌های مطرح دارویی و پخش از جمله دانا، اسوه، جابرابن‌حیان، کیمیدارو و پخش رازی است و خرید آن می‌تواند زاگرس را به یک گروه دارویی یکپارچه تبدیل کند.
🔹
با این حال، دوره وصول مطالبات حدود ۲۸۰ روزه زاگرس، تأمین مالی معامله ۴۰ همتی را به مهم‌ترین ابهام تبدیل کرده است.
🔹
اگر تأمین مالی معامله به‌درستی انجام شود، خرید «شفا» می‌تواند نقطه عطفی برای دزاگرس و زمینه‌ساز شکل‌گیری یکی از گروه‌های بزرگ خصوصی صنعت دارو باشد.
🔗
متن کامل خبر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/696326" target="_blank">📅 12:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696325">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6dc58491e.mp4?token=qBVfotvz8N8P1WCj5V7P0pJuH-t9AJ40QFCcooVQKBV78rE36bPuDQ1vIe7itZj48I0Rdm905qINVSCjEXy17mIL929vZaj0wm4SRZnTjpKkF6ahA1VAnZiaDZrpoQkEq-ss6Nvgt-mL1umlCOR-c0qZpAxOjwhdu13rRH43vRdNNUx-D9vmHMBm57k18ibVQ0Z1wxjx6vD63oMRxe9oLxjJSs0z15PJi3P5_6V-ZEkT3_Yf--MR1xGympJ32icT34LmJAQPE24E47R6LOgw9lUroWt1Y9G1bEkH9YlKtTZO0mwDRqpyPgkWGcwXiXYQGKkFD-GBDDTGygpmVFEMjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6dc58491e.mp4?token=qBVfotvz8N8P1WCj5V7P0pJuH-t9AJ40QFCcooVQKBV78rE36bPuDQ1vIe7itZj48I0Rdm905qINVSCjEXy17mIL929vZaj0wm4SRZnTjpKkF6ahA1VAnZiaDZrpoQkEq-ss6Nvgt-mL1umlCOR-c0qZpAxOjwhdu13rRH43vRdNNUx-D9vmHMBm57k18ibVQ0Z1wxjx6vD63oMRxe9oLxjJSs0z15PJi3P5_6V-ZEkT3_Yf--MR1xGympJ32icT34LmJAQPE24E47R6LOgw9lUroWt1Y9G1bEkH9YlKtTZO0mwDRqpyPgkWGcwXiXYQGKkFD-GBDDTGygpmVFEMjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک ایده ساده و مهندسی که کارگران بهش نیاز داشتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/696325" target="_blank">📅 12:01 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
