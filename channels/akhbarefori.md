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
<img src="https://cdn4.telesco.pe/file/DWOw1fVnu9-oT9hLaH8nzZ9yw8HjzLKd6S9ZDBVuc5cynjVP4qvMj2MRaHeEMwV811ml-4HIRDBYYKwGm8WdrgMyCisOx58zpBYIAMS-vlGiCBJU-iN1p4sERNTFHWS5wQ539VZdGeMkdQftGm8ZpLchFewXzBMxx7eI7aIo_1RUCw9jOCDxKuZkxXB0-KQOsvgi8QwKT5j1KVznupxhii0mMXoZEq9YrwPeXNOCc5X3u6OYGC5KIji2plJ6j89q0OMcgUfzwTHHLx0wg8H62oQUzh3hCLrV5BCfX98CUnXEA9Tn64kPYu53iD7UEac-0J-cgECpCi3xuTqMeOZx9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.22M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 10:20:44</div>
<hr>

<div class="tg-post" id="msg-680498">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f12f75205e.mp4?token=be3nSY7sWOPCApxtCjBvilv0EWE6AuqoLoRAgZV8R-epgcjIL0_UWUOJwRR-Fj5YnSGKpswnM9PbEXTSxsCeZHAn0_uwAuOSiFE_Ao8p7Rr2V21tN8RY8fXPYLk8PN92nOmedB_zI0SQT2NKAEfMu6OVlsl9yf7lfaiIG8WiSmNS4r-Jcc2OBZTVaht_UvxwYurXsknfqLZEF0SSSvEdQY-fN07_7R7HPSXgQgblEoqWI5IAsafXBo4dww9xKfF0u7Y0jJwnaEISuLGX6064dQfhQgRo2VcsDAJ7L3vGFXXPh6f0jR9mU7lcjDXCnLxDLhuJmWWTK8-7M2TMi8OLKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f12f75205e.mp4?token=be3nSY7sWOPCApxtCjBvilv0EWE6AuqoLoRAgZV8R-epgcjIL0_UWUOJwRR-Fj5YnSGKpswnM9PbEXTSxsCeZHAn0_uwAuOSiFE_Ao8p7Rr2V21tN8RY8fXPYLk8PN92nOmedB_zI0SQT2NKAEfMu6OVlsl9yf7lfaiIG8WiSmNS4r-Jcc2OBZTVaht_UvxwYurXsknfqLZEF0SSSvEdQY-fN07_7R7HPSXgQgblEoqWI5IAsafXBo4dww9xKfF0u7Y0jJwnaEISuLGX6064dQfhQgRo2VcsDAJ7L3vGFXXPh6f0jR9mU7lcjDXCnLxDLhuJmWWTK8-7M2TMi8OLKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قطار مغناطیسی چین در ۵.۳ ثانیه به سرعت ۸۰۰ کیلومتر رسید
🔹
مدل آزمایشی ۱۱۱۰ کیلوگرمی قطار مغناطیسی چین در آزمایشی روی مسیر یک‌کیلومتری، تنها در ۵.۳ ثانیه از حالت سکون به سرعت ۸۰۰ کیلومتر بر ساعت رسید.
🔹
این آزمایش همچنین موفقیت سیستم ترمز اضطراری را نشان داد و قطار پس از رسیدن به سرعت ۸۰۰ کیلومتر بر ساعت، در کمی بیش از ۲۰۰ متر متوقف شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/akhbarefori/680498" target="_blank">📅 10:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680497">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/akhbarefori/680497" target="_blank">📅 10:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680496">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: من به ایران اعتماد ندارم، من آخرین کسی هستم که به ایران اعتماد می‌کند، آنها دائما به من دروغ گفته‌اند  رئیس‌جمهور آمریکا مدعی شد:
🔹
ما در حال حاضر کنترل کامل تنگه هرمز را در اختیار داریم. آنها کنترل آن را ندارند؛ ما کنترل کامل را داریم.…</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/akhbarefori/680496" target="_blank">📅 09:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680495">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2685de5d44.mp4?token=LB3VkCIA1Vo3bjeOddbpjph_1nGxM3ksGBTEmZpp6FBYT6Kp1FcLYubVBJcZPHzYtLchgUZNbTlxYcsM_OaFkabnnqNQ81_jtVELUNs62WHW6-65nGXcAklGertEKKh0PNeERxT-_jtxrEDrRYl5Nu3cLr2tplbhP8h-08p2FRPGa8TtdVUqXXlWya0Ptvs_lmPx6Myg80ffj1O-vjRxWQzURtYjGLY5jGvMP0V7l7xs4pFjjzRb0wV0usx37tcrLKnhQcjJ8shsMm305oVpnET9Ka4WLAwLXgEv0H4FRI-yDz4-LtPcHeKLhEn0vWrUkf3AXTzPi4TwG4daRyZHmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2685de5d44.mp4?token=LB3VkCIA1Vo3bjeOddbpjph_1nGxM3ksGBTEmZpp6FBYT6Kp1FcLYubVBJcZPHzYtLchgUZNbTlxYcsM_OaFkabnnqNQ81_jtVELUNs62WHW6-65nGXcAklGertEKKh0PNeERxT-_jtxrEDrRYl5Nu3cLr2tplbhP8h-08p2FRPGa8TtdVUqXXlWya0Ptvs_lmPx6Myg80ffj1O-vjRxWQzURtYjGLY5jGvMP0V7l7xs4pFjjzRb0wV0usx37tcrLKnhQcjJ8shsMm305oVpnET9Ka4WLAwLXgEv0H4FRI-yDz4-LtPcHeKLhEn0vWrUkf3AXTzPi4TwG4daRyZHmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون استقبال از زائران امام رضا(ع) در مسیر پیاده‌رویی زائران به سمت مشهد در موکب هیئت قرار و کانون فرهنگی سلام
@Heyate_gharar</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/akhbarefori/680495" target="_blank">📅 09:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680494">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ba5nZrCMotMlu5BKBqk1QsersaDNcLBkqSNQY-g2UoTW-R5YjmEbaLeKFoiAp1IcMhB_g-cJMahKTHAFqio4Nm1rcVbO3LJyWZuglq7N75j8NobC516m46uBmWKEafoWV_YmI38DzgFbb5jH-2A5SgQbqICkxxPZivi0eIB1A-ebf9WRsIkegJuD3WraAYZ0O35guNsTdZ2EEXVsSvdZAvj12tfUHYls08-grDDwpmG7Ixb1YBA0TN3LLgP03MkLF7Y8FiZfTEM8gB8KTKMs3lNW7T3gRxP-JWBl3_y2FkTMmAnGZVrkYgYFCsEMVMmQktiL9BAPwjDKuq1IXTHtwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ، آخر هفته در زمین گلف خود در بدمینستر، در کنار یک سامانه پدافند هوایی کوتاه‌برد AN/TWQ-۱ اونجر (SHORAD)، گلف بازی کرد #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/680494" target="_blank">📅 09:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680493">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDgusxUAH8YLKqUHCTRyrdS5ljdUJPWRpmkkR51zj7pbPKF_-yTfLN2ZOfLifYO_W2dm3bLiw7TarU9dMnXG4ZEpxhOs1TdiurAMjwjYl2AR-UmbI0lkhnyvM7UFl7LhvTmIRobdK6-kuxFecOV1zyRfn5bAznIy_JF1G07hZUNT4B73RK9CVu9ci6z1FrJK9BtBz8A263_-vmZdyC92KU0rv5kJCnrdGvXoBcLOl4k3ncY3loItCaZ_rDm9hntth86dvBbTbDNOTQWhYTrwWIn19UwWN6KmH5F2r2bkMH1m1P7N_bbZLOX-nTgyrUBLs5dkBjpS5T4tPW-RANbehA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار مصرف همزمان مکمل‌ها
🔹
کلسیم جذب آهن را کاهش می‌دهد و زینکِ دوزبالا هم روی سطح مس اثر می‌گذارد؛ برخی مکمل‌ها را نباید هم‌زمان مصرف کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/680493" target="_blank">📅 09:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680492">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
حمله پهپادی به اربیل
🔹
الجزیره از اصابت ۴ فروند پهپاد به استان اربیل در اقلیم کردستان عراق خبر داد.
🔹
به گفته این شبکه این حملات تلفات جانی نداشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/680492" target="_blank">📅 09:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680491">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qi_NY2HxA4V7Y4iYdq4k6jJ5Z2ijE5oeXyBeSiCBHPxDqKdQmk71bHSNQB1HYVi4E1DTKaOJ0kefl-rPeIwYiUzGMQzLAhh1gH3OEJPVstifkq-FEW_XHQAqJ6i3rMU8RSoSXo658O4jhwyUvuL5Ig3vaxgpo0jhkdbN7z-LE66f2ihPf6SFVOhJQWM1JXIfh41kP_tLipODZ1mv_Z5mfXxeu5yLIYqftcoIIhcy-srOszfLOgjpW2UlHs7CDgTqPVS3A0o0Fcp2TvG0u1HHNYLrM0y_26jQ3Zyhqm4SsFf3AvFg-o8KYlNNdzD7A0vxy9BSOZmcVgh_WHnbL2MFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت تتر ۱۸۷,۸۷۸ تومان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/680491" target="_blank">📅 09:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680489">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqBkdZHnuILTHWZ2PEAtIp7hcxxJGe_57OH5CD4YyL8C6PGINeURH5cs2xye2KZvx2BiFSYk0T7CkV-fJqjidKu-H2IzebTv6iAP8OZlUNzAI2QlO6j4Lkw3wX0hDRoYowJCe5cI2TQy3e6Jbs4luW84yHyZdv_7FRd66-1HVKQjxCQu2rTmHV-DUXc9iE2qfv6NNKz2PytEo9AUloEo9zq_830xY6QCAfc-f3RBW_JuP9x0oBlRwAJ8HqtCKrQDKEkEJWi6TS5D8vYC5Kij-fJI68nhBUvVbcTr_sUywQg4dAKTVKhfGGid89dvlcmYVNwjUE2fP7Gpv_Jj-mg2AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مردم مونته نگرو هم به جوامع متنفر از رژیم صهیونیستی پیوستند
🔹
پایگاه خبری عبری زبان بوحل در گزارشی در این رابطه اعلام کرد، رویکرد ضد اسرائیلی مردم مونته نگرو آنقدر گسترده شده که رهبران جامعه صهیونیست مقیم در این کشور را نگران کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/680489" target="_blank">📅 09:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680488">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5zmpkY3wqADoyU4nwEtsziNFYQEfN5z7mUOG0q5oLeuqHJaNhgd1S_F3kDc43wcyPsjkiJtL-SMuxf-uq0Ovs60ERFZVTKaFFCXXysP7JBc0yuUnwsoq5VoIOfavEmxIu1HrM21m4YIutLLzFGfPhXlN0ziicVAGh60twjW6OqBCGus32OCih4kcNqDrRxo07VcZ2w98eHptSALTqxQ0b4P6Mer53Qj5keTPzyvifPA2j6KRrud8DjVw0pr9x0OaWPDFqkbbMwaAzyVFoAG9_hLclnvlxwRFfB1A0ysE23bBN8QcLvrowpfgait9K_6KHvB_5EGUHfqqEcOfIgVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برچسب انگشتی، پایش مداوم داروی پارکینسون از طریق عرق را ممکن کرد
🔹
پژوهشگران یک برچسب نرم برای نوک انگشت ساخته‌اند که بدون نیاز به باتری، میزان داروی «لوودوپا» را در عرق بیماران پارکینسون به‌طور مداوم اندازه‌گیری می‌کند. این فناوری می‌تواند به پزشکان کمک کند تا دوز دارو را به‌طور دقیق‌تر و شخصی‌سازی‌شده تنظیم کنند و بیماران را از بستری‌شدن در بیمارستان بی‌نیاز سازد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/680488" target="_blank">📅 09:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680487">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1d40c15cc.mp4?token=EmM1KNh9aSQvj3up_pm5g_WYNQZZzxdVTzjFFGXJ1Vie7Iw_RoeAYMN0IIcj9GQcLTO7cLE_Anrn7yI3kA-B5bPuog_N8eUlwdvdPx6Pc6li1UAZh17eV0vyT3DJ9IQabfSoGMMw3hABKgEpWCjxSUqYeWNicy8wHgA3kZBdnqPWMfNJzmoG4jYfsvdOXir2KQmJXdA0Ewk9X1I7PvNNDJEUWcVPdFyfibKjziq3ph_4ZPVprUaZL1uFSYfi_1Ez_Tp1X9zjN2rhVJid3soR8sLmV8aKb683us2On07ShJKPYqd461DnZBTg9-9Ap4faR7PTYi885wZJFgwp6sSgVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1d40c15cc.mp4?token=EmM1KNh9aSQvj3up_pm5g_WYNQZZzxdVTzjFFGXJ1Vie7Iw_RoeAYMN0IIcj9GQcLTO7cLE_Anrn7yI3kA-B5bPuog_N8eUlwdvdPx6Pc6li1UAZh17eV0vyT3DJ9IQabfSoGMMw3hABKgEpWCjxSUqYeWNicy8wHgA3kZBdnqPWMfNJzmoG4jYfsvdOXir2KQmJXdA0Ewk9X1I7PvNNDJEUWcVPdFyfibKjziq3ph_4ZPVprUaZL1uFSYfi_1Ez_Tp1X9zjN2rhVJid3soR8sLmV8aKb683us2On07ShJKPYqd461DnZBTg9-9Ap4faR7PTYi885wZJFgwp6sSgVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله توپخانه‌ای رژیم صهیونیستی به ارتفاعات لبنان با گلوله‌های فسفری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/680487" target="_blank">📅 09:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680486">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
هشدار سازمان غذا و دارو: با توصیه هوش مصنوعی دارو نخورید
🔹
حتی دارویی که برای یک بیمار کاملاً مناسب است، ممکن است برای فرد دیگری به دلیل تداخل دارویی، منع مصرف، حساسیت یا شرایط خاص بالینی نامناسب و حتی خطرناک باشد. بنابراین نمی‌توان یک پاسخ عمومی تولیدشده توسط هوش مصنوعی را معادل نسخه یا توصیه دارویی شخصی‌سازی‌شده تلقی کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/680486" target="_blank">📅 09:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680484">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
جاده چالوس به سمت مازندران به‌دلیل ترافیک سنگین یک‌طرفه شده و تردد از مسیر شمال به جنوب تا اطلاع بعدی ممنوع است؛ سایر محورهای ورودی مازندران نیز ترافیک سنگینی دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/680484" target="_blank">📅 09:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680483">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed5443e66.mp4?token=SHsLuOwgdJEajbMj6E02j7C4A6hBDWQuKvPqMNWTt6Gf_Y4obi5H-m07VfOtgAUEKkSLcwFipc3OQLUovQjSEwcBUFyLjDYdu1N-8_ndXC1J_qIqib482fEf4STFFWlyApAUwTABsF20maTje3v6fbD2cy8CsiP9y9hOjcTBwsZ9CZGI_b3hKcmbY72pcS82iDzotZiiriSzj3phTMQifnTKCu5T0cuNrd2K10Lnsw0Yzd0o36t9uQU9L6_9-PblUkSOO5H3arJZ6UzrP5Hdje_NQFV8o52O8u5muPsASrDmbJ7Mv05CbK0D_e2mSeWjmY0Lf9mX_G2JdXgByiqJDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed5443e66.mp4?token=SHsLuOwgdJEajbMj6E02j7C4A6hBDWQuKvPqMNWTt6Gf_Y4obi5H-m07VfOtgAUEKkSLcwFipc3OQLUovQjSEwcBUFyLjDYdu1N-8_ndXC1J_qIqib482fEf4STFFWlyApAUwTABsF20maTje3v6fbD2cy8CsiP9y9hOjcTBwsZ9CZGI_b3hKcmbY72pcS82iDzotZiiriSzj3phTMQifnTKCu5T0cuNrd2K10Lnsw0Yzd0o36t9uQU9L6_9-PblUkSOO5H3arJZ6UzrP5Hdje_NQFV8o52O8u5muPsASrDmbJ7Mv05CbK0D_e2mSeWjmY0Lf9mX_G2JdXgByiqJDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعداد کشته‌های زلزلهٔ کلمبیا به ۲۲۴ نفر رسید
🔹
تعداد کشته‌شدگان زلزلهٔ ۷.۴ ریشتری دیروز در کلمبیا به ۲۲۴ نفر رسیده است. کلمبیا این زمین‌لرزه را «فاجعهٔ ملی» اعلام کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/680483" target="_blank">📅 09:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680482">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
خورشیدگرفتگی کامل در راه است/ روز در کدام نقاط زمین شب می‌شود؟
🔹
چهارشنبه این هفته، برای اولین بار در دو سال اخیر، خورشید گرفتگی کامل در بخش‌هایی از گرینلند، ایسلند، شمال اسپانیا و شمال شرقی پرتغال قابل رویت است و برای دقایقی، با ناپدید شدن کامل خورشید،…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/680482" target="_blank">📅 08:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680480">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
عراق اقدام کلمبیا در به رسمیت شناختن حاکمیت اسرائیل بر بلندی‌های جولان را محکوم کرد
🔹
وزارت امور خارجه عراق تصمیم کلمبیا برای به رسمیت شناختن حاکمیت رژیم اسرائیل بر بلندی‌های جولان اشغالی سوریه را به شدت محکوم کرد و افزود که این تصمیم هیچ اثر قانونی ندارد…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/680480" target="_blank">📅 08:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680479">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ade0fc751a.mp4?token=sJyfWrWG7n6jXADmwSidMJgNFMpOPPTi4Ogl8ob52T87N9hatRlaiYxGh9oWk1rfI9WKjmiOrUgN_hbkELpRs3eWYJRmC0vJpxuOtvD8fT1l4LwwceKnmRxSsbPBV3_remYLv-cNjBYNZ42uwq4_eQq_XhVzMEBIIeZIzprOIPgctfctjUnQkn1A59KULT3N8oxslwcD2DWdr0PcNK-V-8fWA8i4qC6dxinhODeHZIV1ehZxzedIv9l2ZrePjNaagM3tpBPKwWVES4DhFscBWgXKdHBq8VtUx39thqekjdvEHzEM31k8R3-hxAwIqwfepqrwwVFWaYC5BQv39Wb5NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ade0fc751a.mp4?token=sJyfWrWG7n6jXADmwSidMJgNFMpOPPTi4Ogl8ob52T87N9hatRlaiYxGh9oWk1rfI9WKjmiOrUgN_hbkELpRs3eWYJRmC0vJpxuOtvD8fT1l4LwwceKnmRxSsbPBV3_remYLv-cNjBYNZ42uwq4_eQq_XhVzMEBIIeZIzprOIPgctfctjUnQkn1A59KULT3N8oxslwcD2DWdr0PcNK-V-8fWA8i4qC6dxinhODeHZIV1ehZxzedIv9l2ZrePjNaagM3tpBPKwWVES4DhFscBWgXKdHBq8VtUx39thqekjdvEHzEM31k8R3-hxAwIqwfepqrwwVFWaYC5BQv39Wb5NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردم مراقب خرید طلای آبشده باشند
رئیس اتحادیه تولیدکنندگان و صادرکنندگان طلاوجواهر:
🔹
برخی به دلیل کارمزد کمتر اقدام به خرید طلای آبشده می کنند که به دلیل نامشخص بودن عیار آن، خطراتی به همراه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/680479" target="_blank">📅 08:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680477">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
وزیر خارجه رژیم صهیونیستی: تا زمان جمع‌آوری تمامی سلاح‌ها از غزه، رفع تهدید و پایان حکومت حماس، بازسازی نوار غزه آغاز نخواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/680477" target="_blank">📅 08:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680476">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: من به ایران اعتماد ندارم، من آخرین کسی هستم که به ایران اعتماد می‌کند، آنها دائما به من دروغ گفته‌اند
رئیس‌جمهور آمریکا مدعی شد:
🔹
ما در حال حاضر کنترل کامل تنگه هرمز را در اختیار داریم. آنها کنترل آن را ندارند؛ ما کنترل کامل را داریم. تنگه هرمز مال ماست.
🔹
شاید در مقطعی آنها دست به کاری بزنند و آن وقت نابودشان می‌کنیم. اما در حال حاضر، ما در موقعیت بسیار خوبی قرار داریم.
🔹
ما با کشوری روبه‌رو هستیم که ۵۰ سال قلدر خاورمیانه بوده است. اگر دقیق‌تر حساب کنید، در واقع ۵۱ سال است، درست است؟ ما چهار سال است که می‌گفتیم ۴۷ سال. اما آنها دیگر قلدر خاورمیانه نیستند/ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/680476" target="_blank">📅 08:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680475">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9061d1aea.mp4?token=UOisl5nO1qZoZl4lFDivWDM9QAppXFtiqSprelu3_psNJgBvIP-Bxj-C5tdAqTocoU33h7aZCckvPaJOmvns5v022HhD10gxvGKK6blpAqRoPPPuNY2qMOwDig2gOWK7R35BrxaZznrEoAsMHcnyQDfnFNGvxoZHGiM5eIH4bFfg-1RVIbJyfNv5qu7AEsJbW5cAtXQYnI-p-GitHX2bBv6yK6MHp_eIe2e_Yt8See4uUVvOd8tGWD4xivFDgOys1SWpepJJOYI6LwHgl0ms0sIk__y69dvKp6qmPR4HgGuvo4qEYF11e3nN7c0yD7Ej2-pYutzmY6o8FrgCY20icBtkACU0JFxX9tQwKWscpumLgE4rd2ro85_nswCiNj66VREe_RXXviIc5vLQA-lbSTV5OqaP4J-Bwx5a3Ny-M1brW9MFQ7roaiPPwyqffOmY_lKgwfjkHUZV7qdtPEdQ_bw0TlBqzU_ATyEGVyN7tbD6gGch2eVlGPvSNSAXd04ev-U0AcULbl2zQXRRZ9NY1-uHB7uZkwtbr7cCG4akrJSzKCut2Z9_zeqR2Lt5tYkk78cQ3Da-ZEujr8SMKfyJtHe-9nSuFxiAtWBXqxSz8SAlvjEaBgaHZLv6mO0AONaJXmj9IFmHb0Czu5hFxkYqdtb0-yQEwAmcEz8NUD0EhAM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9061d1aea.mp4?token=UOisl5nO1qZoZl4lFDivWDM9QAppXFtiqSprelu3_psNJgBvIP-Bxj-C5tdAqTocoU33h7aZCckvPaJOmvns5v022HhD10gxvGKK6blpAqRoPPPuNY2qMOwDig2gOWK7R35BrxaZznrEoAsMHcnyQDfnFNGvxoZHGiM5eIH4bFfg-1RVIbJyfNv5qu7AEsJbW5cAtXQYnI-p-GitHX2bBv6yK6MHp_eIe2e_Yt8See4uUVvOd8tGWD4xivFDgOys1SWpepJJOYI6LwHgl0ms0sIk__y69dvKp6qmPR4HgGuvo4qEYF11e3nN7c0yD7Ej2-pYutzmY6o8FrgCY20icBtkACU0JFxX9tQwKWscpumLgE4rd2ro85_nswCiNj66VREe_RXXviIc5vLQA-lbSTV5OqaP4J-Bwx5a3Ny-M1brW9MFQ7roaiPPwyqffOmY_lKgwfjkHUZV7qdtPEdQ_bw0TlBqzU_ATyEGVyN7tbD6gGch2eVlGPvSNSAXd04ev-U0AcULbl2zQXRRZ9NY1-uHB7uZkwtbr7cCG4akrJSzKCut2Z9_zeqR2Lt5tYkk78cQ3Da-ZEujr8SMKfyJtHe-9nSuFxiAtWBXqxSz8SAlvjEaBgaHZLv6mO0AONaJXmj9IFmHb0Czu5hFxkYqdtb0-yQEwAmcEz8NUD0EhAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای زائران رضوی در مزار رهبر شهید انقلاب، در شب شهادت رسول اکرم(ص) و امام حسن مجتبی(ع)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/680475" target="_blank">📅 08:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680474">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
«توافق مکه»؛ نام پیمان سه‌جانبه نظامی ترکیه-عربستان-پاکستان
🔹
همزمان با برگزاری نشست سران ترکیه، عربستان سعودی و پاکستان در جده، گزارش‌ها حاکی است که پیمان دفاعی سه‌جانبه‌ای که قرار است امروز میان این سه کشور امضا شود، به طور رسمی «توافق مکه» (Mecca Agreement)…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/680474" target="_blank">📅 08:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680473">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
هشدار آبگرفتگی محلی، و سیلاب در حاشیه و بستر رودخانه‌های مازندران
🔹
مدیریت بحران مازندران با اشاره به هشدار سطح زرد هواشناسی اعلام کرد که خانواده‌ها از اسکان و توقف در حاشیه و بستر رودخانه‌ها و مسیرها خودداری کنند.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/680473" target="_blank">📅 08:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680470">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e163d5cec.mp4?token=eJ9fMa2anCaTa7c-7gC8BlLXgO-h5j_JzwveON-NPnApRrsdVOY7gjau9gsjOZ4v2B34uzlWbMncZJzRlooIeUwznJ2YX3hM1Qar459LI85NYu3it3Ss6e222qIykkW6H8OEOA6VP1KtN6rRm8R1PTIdr64sCTKM6MMVWL585bBtVlujroRBcZp1KNv36vWWeQhCEY7AoI7S1jV-cbCDIDABM3GhkNXUWSLG_jsMFcc1zOYxe2GLwzZ85XBhBN3lEmQdvpxGC6xLArb_6qaCugLfBCaKmAOdBNVm8D45Ut8sqL1oysdvDb02Hp23GjBWAYWE9vBHC15e9NtkGT--Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e163d5cec.mp4?token=eJ9fMa2anCaTa7c-7gC8BlLXgO-h5j_JzwveON-NPnApRrsdVOY7gjau9gsjOZ4v2B34uzlWbMncZJzRlooIeUwznJ2YX3hM1Qar459LI85NYu3it3Ss6e222qIykkW6H8OEOA6VP1KtN6rRm8R1PTIdr64sCTKM6MMVWL585bBtVlujroRBcZp1KNv36vWWeQhCEY7AoI7S1jV-cbCDIDABM3GhkNXUWSLG_jsMFcc1zOYxe2GLwzZ85XBhBN3lEmQdvpxGC6xLArb_6qaCugLfBCaKmAOdBNVm8D45Ut8sqL1oysdvDb02Hp23GjBWAYWE9vBHC15e9NtkGT--Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزنامه‌نگار و مفسر سیاسی آمریکایی: مردی که خودش را در کنار جورج واشنگتن و قهرمانان جنگ آمریکا می‌دید در یک خودروی آشغال پنهان شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/680470" target="_blank">📅 07:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680469">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e17cd8159.mp4?token=PkNkjExrRoS3USkb_7mO4n0jEm33ZF2gHsOn7H0DtDzd6sTeoaYXopWtexeWnJT5whuBaGJAXh_m8rVbkNSfSTE_p2SFs7eQ5-mb_ITnfH1ynKD3jEilVkSr0-2aaMNGlazG1hnfNxygxDA9biFFXnKK0TtKodYzhW7PrCVgX_K8Pqwtz-uJrm7ENaC6nBxk505R_hxxdsrIFGKOTQjxSQqj5mMq8D_FT4g8ePlRrXCBnNyNpKcoeZnMAlewSA6YazH3a2gOXQZVmUuvr3EMMSK_vaCFxA2VEkmRgHiaN_sHy4BDCYQ2tzEVm1KSjMbAmvcWB4Oefw1P_8r_AIrOLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e17cd8159.mp4?token=PkNkjExrRoS3USkb_7mO4n0jEm33ZF2gHsOn7H0DtDzd6sTeoaYXopWtexeWnJT5whuBaGJAXh_m8rVbkNSfSTE_p2SFs7eQ5-mb_ITnfH1ynKD3jEilVkSr0-2aaMNGlazG1hnfNxygxDA9biFFXnKK0TtKodYzhW7PrCVgX_K8Pqwtz-uJrm7ENaC6nBxk505R_hxxdsrIFGKOTQjxSQqj5mMq8D_FT4g8ePlRrXCBnNyNpKcoeZnMAlewSA6YazH3a2gOXQZVmUuvr3EMMSK_vaCFxA2VEkmRgHiaN_sHy4BDCYQ2tzEVm1KSjMbAmvcWB4Oefw1P_8r_AIrOLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش کاربران خارجی به مخفی شدن ترامپ در کامیون آشغال
📲
🇮🇷
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/680469" target="_blank">📅 07:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680468">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQNuVJ-elCdEjts9ONdEEAdnDdjMBF0vSX-T_6b75kobWu_GDZNa7Vsrs-ZREv-belWu6ekOIixwexQdeWXJZqCsGNQubm-ps9mA9MgbHn6Xi2oeF9Trs5Mw3et1e3C6DvYmCuepQ9ud0FLNfXMJLquVLfxG3OKyhz4STm5IoewwCtUouNk-OLhgljIb6Wi3qYz-ViihjOCc-_WmMbqugIH0RAqmLzSyDr1WPPBhrsH4GPfyQ0BmbQSY7dz1Vn9zEjFHrTca6lZqKveNS_xsYYCOlP426APw11BmGiLN9S3OGtsigqYu2wN-A1AP92gN1GJrE8AarCtEg1BbZUVgMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو: کوبا باید کاملا با آمریکا هماهنگ باشد
وزیر خارجه آمریکا:
🔹
کوبا تا پیش از پایان دوره ریاست‌جمهوری دونالد ترامپ، وارد آینده‌ای کاملاً متفاوت خواهد شد.
🔹
واشنگتن خواهان آن است که کوبا کشوری امن و باثبات باشد و در هماهنگی کامل با آمریکا زندگی کند.
🔹
این کشورها حدود سه تا پنج سال زمان نیاز داشتند تا به وضعیت کنونی خود برسند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/680468" target="_blank">📅 07:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680465">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
پنتاگون پس از یکسال تایید کرد که بر اثر حملات آمریکا به یمن در سال ۲۰۲۵، حداقل ۱۵۰ غیرنظامی کشته و ۲۵۰ نفر زخمی شدند.
📲
🇮🇷
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/680465" target="_blank">📅 07:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680464">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
واکنش کاربران خارجی به مخفی شدن ترامپ در کامیون آشغال
📲
🇮🇷
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/680464" target="_blank">📅 07:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680463">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAtlFrZK6ER2_WB8_sfDxgBd4XlvAId--W6hwV4E81dtjRTnxPCtAkPmX0QCfDedS45kSsv65FcXYUSvifTi5tiOMCtijJbNfkRncyX8ce99LHWcI1qcbdv7-BSNeK7Kke3SDq09CCoU52GMK_ZPetoo8xN18Zm6Rgsco7uUIG5OCV-d0XGvTs0yIFgKm3ydnJu5zLFlrXeF_1ohbNbdrhXt9WJgsIYFZR5gnymiCUjjgfHMQNjJ85wfc4jdOpQiMqM0VDmGVnfG1gFV_RJFip9Lyy3482hfc7LIPvJ6mGbwkga4Zxnhj5MKUgndSEXt-2XXcZcrDoshmutXHvujXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۲۱ مرداد ماه
۲۸ صفر ۱۴۴۸
۱۲ آگوست ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/680463" target="_blank">📅 07:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680462">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbERKI8qK_pZjKx6k9AoNjPDeR5OE29GI-TAxz1pvV2dEm5GuT0BPwqQwmdKNlWyLTsmeY_PV00MY1SwEWKcJF_NC4nzZgmJWKrVO5OrP36i3iV73Dvpx0ao3QBBV-xYzuXerD5Vztise4pBkBgrF6aXxmmMhAe7BOLzDUgsV9RimHr8webABRtK9MHejSfQZn5D-xtYd18I8H_mlzJ-6ph5M4jiiNMdOegBcJ_AVY3X5vy_PIQbiFkP2dpb0bYEEUhD8PuSvLuL-IeU2vh50VfuNcTmkfzxKCzG7UGhusBE_64UxJrCut0u9Tfe2nCDdroysdMScpoeAuEPs7aKWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادامه‌ی حملات توپخانه‌ای رژیم صهیونیستی به غزه، اردوگاه البریج
🔹
منابع خبری فلسطین از حملات توپخانه ارتش رژیم صهیونیستی به مناطقی در شرق محله الزیتون در شرق شهر غزه خبر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/680462" target="_blank">📅 02:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680461">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
وقوع آتش‌سوزی بزرگ در نزدیکی فرودگاه شارل دوگل پاریس
🔹
آتش سوزی منجر به بسته شدن ۲ باند فرود و تعلیق فعالیت های آن شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/680461" target="_blank">📅 02:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680460">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
طبق گفته برخی منابع انفجار یک تانکر سوخت در خیابان‌های اربیل، مرکز منطقه کردستان عراق تا الان علت آین اتش سوزی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/680460" target="_blank">📅 01:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680458">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a75ee87df.mp4?token=HwIgBuHoMRNVDSOssAzAuDXpnvB2RriB11J8FLWhcTj-gGGQhOBubZT9J67nSpgPvP4WKzeMDVYwkC11wfsHed1K53VxZ-0gjUvUsifMcTB-B-TmpVgxozcTjJL7KeX09Lq6Xowc60t2tx8iCkJaP-A9eKm0A7pEfzWlJ_qjg34UZ_FC7xkiiMoRQkmLfxShrcU0erw0ZBdsES6hZMx3vzA1ehN82xcwn6j52JIv1IP_WBH_G6D39DRZD2eqGJbQlOL4lxXw-5dMKzRlV3VF1PNFhw4YW0qzft2TOcqZspWopvTEQSZVB0pOxbCKlqMiElEC-LjLRhdVoM6IVkUQTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a75ee87df.mp4?token=HwIgBuHoMRNVDSOssAzAuDXpnvB2RriB11J8FLWhcTj-gGGQhOBubZT9J67nSpgPvP4WKzeMDVYwkC11wfsHed1K53VxZ-0gjUvUsifMcTB-B-TmpVgxozcTjJL7KeX09Lq6Xowc60t2tx8iCkJaP-A9eKm0A7pEfzWlJ_qjg34UZ_FC7xkiiMoRQkmLfxShrcU0erw0ZBdsES6hZMx3vzA1ehN82xcwn6j52JIv1IP_WBH_G6D39DRZD2eqGJbQlOL4lxXw-5dMKzRlV3VF1PNFhw4YW0qzft2TOcqZspWopvTEQSZVB0pOxbCKlqMiElEC-LjLRhdVoM6IVkUQTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر نزدیک از آتش‌سوزی گسترده‌ای که در مرکز استان اربیل، در شمال عراق، رخ داده است
🔹
گزارش‌ها حاکی از آن است که یک تانکر حامل سوخت در این آتش‌سوزی شعله‌ور شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/680458" target="_blank">📅 01:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680457">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f5bc3a1c.mp4?token=o6XEOKg3d27qM_G9uev2G8_ePT_oORllUpX9K2X1TiT3NjLudwusNq81N8FHOrIiYO5BLqABxcVAbTDAIaOHyCEgzK7sMV9UA1jWVnL2kSELPX0u-5Oa75DSb9hH-K4Ow2sOaJBtgFakAQTaf94sxgw8mEu4DvRIZZSUcGwwLwYsg-ZVxh_p-D_PoJt9pjiHfyD2V-VXjHPqwvk1lNojzaOywZUtnphSXh2tuSrs7RyCq0O70TQQIGN5XtPOZ1v4fB8NsJTMNVRDZHLOJ00lzjZclQirKyKNZ_Tzq0SxNumX2XV7h6OMJTEAeEUVvjZCs5-ZsHRf4x1K_2vtbZo6bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f5bc3a1c.mp4?token=o6XEOKg3d27qM_G9uev2G8_ePT_oORllUpX9K2X1TiT3NjLudwusNq81N8FHOrIiYO5BLqABxcVAbTDAIaOHyCEgzK7sMV9UA1jWVnL2kSELPX0u-5Oa75DSb9hH-K4Ow2sOaJBtgFakAQTaf94sxgw8mEu4DvRIZZSUcGwwLwYsg-ZVxh_p-D_PoJt9pjiHfyD2V-VXjHPqwvk1lNojzaOywZUtnphSXh2tuSrs7RyCq0O70TQQIGN5XtPOZ1v4fB8NsJTMNVRDZHLOJ00lzjZclQirKyKNZ_Tzq0SxNumX2XV7h6OMJTEAeEUVvjZCs5-ZsHRf4x1K_2vtbZo6bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع آتش سوزی بزرگ در اربیل عراق
🔹
علت حادثه مشخص نیست.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/680457" target="_blank">📅 01:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680456">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5171ee4322.mp4?token=PNP5eQpDWG5ZJaC2aCLMtnsx3CAAKfYd3uHOUFUHRrP7hBP24Frp1fIaMdHyUPNGkWNRKRV2cBKCQkj6eUWTzNzHau5OOsorDCECf46qbpamzT3iq99ZIOI_VFYMgBe7TWjmH903JeYi6b5EGjfWq6MJbT-Pq72zCOhd7uD6Murm8KwcMROxL-gan7nIV5XnG4dNVK7v5ts6sFZp5IgyrbH3TRuASzXVj93ZGeN5-EwJ77yAviAUHMpH2TPT6QNVAaeG6SwYlK6OyU_ys-fNs6mSbUyyja8ii5X2lg9dNMfKM927lqNeqHspX6IyuWUoKsU0QVppss_E3jJyrwpU4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5171ee4322.mp4?token=PNP5eQpDWG5ZJaC2aCLMtnsx3CAAKfYd3uHOUFUHRrP7hBP24Frp1fIaMdHyUPNGkWNRKRV2cBKCQkj6eUWTzNzHau5OOsorDCECf46qbpamzT3iq99ZIOI_VFYMgBe7TWjmH903JeYi6b5EGjfWq6MJbT-Pq72zCOhd7uD6Murm8KwcMROxL-gan7nIV5XnG4dNVK7v5ts6sFZp5IgyrbH3TRuASzXVj93ZGeN5-EwJ77yAviAUHMpH2TPT6QNVAaeG6SwYlK6OyU_ys-fNs6mSbUyyja8ii5X2lg9dNMfKM927lqNeqHspX6IyuWUoKsU0QVppss_E3jJyrwpU4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع آتش سوزی بزرگ در اربیل عراق
🔹
علت حادثه مشخص نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/680456" target="_blank">📅 01:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680455">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-q5aft8N8AggG0ih-WwRg05oUuvuQK2pNX8cmTebvQXsB3QoflhIQAsV93-cwYwe2_M1wAb0LWwXzsyQGDaVg6QZqRE0RbBp3JTpNl2RyOohAOo7pj7P0IWcfBUGVRJfU5gl2HBSj6mCOowstJF0t-hbKD5Yh0pykI9DuhrZ_Gd_F0QtKMECeijtaoRHVvXth_H6tM4joOWeWSZ0MKrfrm-R1TgAU7Ix5ulI5vQNcpf53WX5pchr80nIAWrLoMrFOrAoc8MqaqveMfViE-8--MUJYzLMNJxw3chw-rlE_Dti6ncZQE_r_h9MffQ_3EPW6OG2Vi_pZh9MCiZmw6sEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر آمریکایی: کاش رئیس‌ جمهوری داشتیم که بزرگترین جوک و مایه تمسخر تمام جهان نباشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/680455" target="_blank">📅 01:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680454">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04361bf871.mp4?token=uAtZP8vB6bABoBAHTXncd0NGig_HYQD5qkz_ZWRTH6z14Ivq9hOKVwvjj0AanNPPqbdxDDJOZ8NXiEqxnxHzxBPQBLpoOkrai62DDQ6r8ptvOPexCsBp_Pr6tLAyzZa9xHHIypnqqOziWn9sgb__SjskCInPb5bJC5T2WgpeeaSrCCm8BXdYPbtiv8aAhZhYRL99iZkQkqigUJie5OPY9_Ri6_mO9v5WMGbrRW4phDJgccTFWsKviho0uuN72qvFQ8rHHCiVh6y4WuiAU2ngyxq_Noop6HJuat-sBElLJT8YFxbpsx2fXZyOhseV465IM-BujQOmy4zu6LTW9HvdFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04361bf871.mp4?token=uAtZP8vB6bABoBAHTXncd0NGig_HYQD5qkz_ZWRTH6z14Ivq9hOKVwvjj0AanNPPqbdxDDJOZ8NXiEqxnxHzxBPQBLpoOkrai62DDQ6r8ptvOPexCsBp_Pr6tLAyzZa9xHHIypnqqOziWn9sgb__SjskCInPb5bJC5T2WgpeeaSrCCm8BXdYPbtiv8aAhZhYRL99iZkQkqigUJie5OPY9_Ri6_mO9v5WMGbrRW4phDJgccTFWsKviho0uuN72qvFQ8rHHCiVh6y4WuiAU2ngyxq_Noop6HJuat-sBElLJT8YFxbpsx2fXZyOhseV465IM-BujQOmy4zu6LTW9HvdFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دمام‌زنی زائران مشهدالرضا(ع) در خیابان‌های منتهی به حرم مطهر رضوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/680454" target="_blank">📅 01:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680453">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
اخبار غیر رسمی از انفجار در منطقه سیده زینب (س)
🔹
منابع عربی از شنیده شدن صدای انفجار و تیراندازی در منطقه سیده زینب (س) واقع در جنوب دمشق خبر می‌دهند.
🔹
تا این لحظه گزارشی از ماهیت این رویداد منتشر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/680453" target="_blank">📅 01:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680452">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPzaGxNajwcm_Y0JhuKcHKBzBrhxWES2iDxN2RFC89Oq_L4tpB818Vk7qpx_KzwFCpu7K_p-33hb0qzq5PZ7dYBMlJMD1xyZTK3f3_nkksLeS8eMYfRSE2xj40nuCDBMrP53lA4BwFXyAZTgtWehMUgZXwettixfX5DviDPGmX0FCxntDcqCk4emK9BIsoU--y-qThGjOxreTZYuc8O8xRFyUzMEBugeEEtTrHYAh0x1fX11T8dBKa7Ge9sHZdRmIDkI_4SmEgnqGVKjQXwZRHZZkYCl6cmbrFf4py8qrI3_FU6m0182WVuaYQ0GdQk_xb-lgAcekJKRG5ogzpCOtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر ژئوپلتیک آمریکایی: توازن قدرت در خاورمیانه به‌طور دائمی علیه آمریکا تغییر کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/680452" target="_blank">📅 01:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680451">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
حملات توپخانه‌ای اسرائیل به مناطقی در غزه
🔹
منابع خبری از حملات ارتش رژیم صهیونیستی به مناطقی از شهر خان‌یونس در جنوب نوار غزه گزارش دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/680451" target="_blank">📅 01:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680450">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95c3772001.mp4?token=WK0lvIkscEJ8ug4Fd5pzzP0au9cYhUuh0y8L81_o-D0N2TeXQ7dwkjS85eTpHlDctHmwVUZ9ziwsn6wnKYTuFFzBitZhms8PHRsEYf4KQKtbbLy4bwYwe6DEQhr3-QjOEsIrZdIbdSvA8CTU21qVKTYpBkOhAvGKIjr8A52ixrvWCdKHgcQLZCVk8nHbxVbtbfv20WAVrvmsXQGguSsTxv20FvvUEBIYwmvb-K24Y1wBukhJ2EY1AVK5Dp7uJvBHu95yPOHDnbBINjUb5G2FqA4N19KQ6h9KNGHZeHOtATeaam8NZr0zo2ItZ7PGZCuj1RIe2rUvzGMHObtEtmTXwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95c3772001.mp4?token=WK0lvIkscEJ8ug4Fd5pzzP0au9cYhUuh0y8L81_o-D0N2TeXQ7dwkjS85eTpHlDctHmwVUZ9ziwsn6wnKYTuFFzBitZhms8PHRsEYf4KQKtbbLy4bwYwe6DEQhr3-QjOEsIrZdIbdSvA8CTU21qVKTYpBkOhAvGKIjr8A52ixrvWCdKHgcQLZCVk8nHbxVbtbfv20WAVrvmsXQGguSsTxv20FvvUEBIYwmvb-K24Y1wBukhJ2EY1AVK5Dp7uJvBHu95yPOHDnbBINjUb5G2FqA4N19KQ6h9KNGHZeHOtATeaam8NZr0zo2ItZ7PGZCuj1RIe2rUvzGMHObtEtmTXwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر صهیونیست: نمی‌گذاریم غزه بازسازی شود
🔹
«گیدئون سعر» وزیر خارجه رژیم صهیونیستی با بیان اینکه یک سال است که غزه بازسازی نشده، گفت که نابودی تمام سلاح‌ها در این باریکه یکی از پیش‌شرط‌ها است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/680450" target="_blank">📅 00:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680449">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3b82593b.mp4?token=iRyBsajB1p7PNKUI6AeLCeYyeUOBMz54DAG6JQ8untjNQjcHUjG2LDu4911qaH2oRgKtiIR2DdTflAkSc_AU1ToFsYOj-m0EbfIY_OR1iUtvNitoaUxnV8xXoa_cBeI6uNy6Dr4XeI3OatjHpA7KKmI7b5ReZw5yNxFjs5X5WxGpO8oOnqpxjB4ae_ftYaADYmBpESrlWU3u2blgFK6shaB0mXQJzeViXqkS2ATgNeV_RPEBoPnah-R73_VMOEYFockylAhaQK3TsAsrRCq9gVk3uw7aUaevGqlyPPCoyJEXk-mjUu364_Blwb1AdXyWt40Dcx_dB7MtK4fuBsD9qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3b82593b.mp4?token=iRyBsajB1p7PNKUI6AeLCeYyeUOBMz54DAG6JQ8untjNQjcHUjG2LDu4911qaH2oRgKtiIR2DdTflAkSc_AU1ToFsYOj-m0EbfIY_OR1iUtvNitoaUxnV8xXoa_cBeI6uNy6Dr4XeI3OatjHpA7KKmI7b5ReZw5yNxFjs5X5WxGpO8oOnqpxjB4ae_ftYaADYmBpESrlWU3u2blgFK6shaB0mXQJzeViXqkS2ATgNeV_RPEBoPnah-R73_VMOEYFockylAhaQK3TsAsrRCq9gVk3uw7aUaevGqlyPPCoyJEXk-mjUu364_Blwb1AdXyWt40Dcx_dB7MtK4fuBsD9qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شلیک یک سرباز روسی که با استفاده از یک سیستم شلیک همزمان، به یک پهپاد اوکراینی که در ارتفاع پایین پرواز می‌کند
🔹
این سیستم مستقیماً بالای کامیون‌ها نصب شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/680449" target="_blank">📅 00:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680448">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f933dd533.mp4?token=p4oBf9Ba0XFNhVOhpvZUJOnCVL34PIbOVVvhO1iQFfNTucUf4BHzOI6lgIhj955Xah0RaViWW6R174glOZxLXEuAKfrikk23NGnEE5ErBJmfFLpYrn5DhZTYDf_BfCEYrn9FtYT7HI34VvzTnx_7nhf-GyZY9sB2wdJ_Ec6161_LGdh3O91eWxMG1Yc8hptSxNfZ3EY_zmal6vY3CSVrpZF44mJm8PJ39hLKfTQyiCUR-ai6_pXDrmoDtvmrNkJmtRoyDq4AwudyGxlByxWidXdydh-lGW5T7fAoPa86EdHj1DNQn7IKdPdNhr1ummphTXSKSN4TAyxmy2IkjSVYvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f933dd533.mp4?token=p4oBf9Ba0XFNhVOhpvZUJOnCVL34PIbOVVvhO1iQFfNTucUf4BHzOI6lgIhj955Xah0RaViWW6R174glOZxLXEuAKfrikk23NGnEE5ErBJmfFLpYrn5DhZTYDf_BfCEYrn9FtYT7HI34VvzTnx_7nhf-GyZY9sB2wdJ_Ec6161_LGdh3O91eWxMG1Yc8hptSxNfZ3EY_zmal6vY3CSVrpZF44mJm8PJ39hLKfTQyiCUR-ai6_pXDrmoDtvmrNkJmtRoyDq4AwudyGxlByxWidXdydh-lGW5T7fAoPa86EdHj1DNQn7IKdPdNhr1ummphTXSKSN4TAyxmy2IkjSVYvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پارسال همین شب‌ها؛ خادمی سردار شهید تنگسیری در حرم رضوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/680448" target="_blank">📅 00:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680447">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27b1027df.mp4?token=P-cVOjHBWyYs3UQ-d3wqAUmMBaJXs_IfnGeWMnygTEv1HENUshZt7i_KJ13gQpZxkMjARDYNFiYOiKXE87L08FBNcKLfO2u2IUZh4zVAL6UIl3AGlqNW4OuDpXQ14-S1QlJHTtX4NwNrhq8QhqQePzs3TxgeDN4PoJJjvZNAWIP5RFg-zztaA0W7kdiDTIraqqlO8SYi_63zFpUtyemfufSU4AK53Wugs_uZS9rOOWOOcwW0eyPbKZr_C6xigHVOolOhvXfpR01CPM3O7-MDAABTBf-7vM0HM9I9A8jdb-OBe-HwwHL2cvJHmM3lhKOc832StTU7inal4hs4faSo9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27b1027df.mp4?token=P-cVOjHBWyYs3UQ-d3wqAUmMBaJXs_IfnGeWMnygTEv1HENUshZt7i_KJ13gQpZxkMjARDYNFiYOiKXE87L08FBNcKLfO2u2IUZh4zVAL6UIl3AGlqNW4OuDpXQ14-S1QlJHTtX4NwNrhq8QhqQePzs3TxgeDN4PoJJjvZNAWIP5RFg-zztaA0W7kdiDTIraqqlO8SYi_63zFpUtyemfufSU4AK53Wugs_uZS9rOOWOOcwW0eyPbKZr_C6xigHVOolOhvXfpR01CPM3O7-MDAABTBf-7vM0HM9I9A8jdb-OBe-HwwHL2cvJHmM3lhKOc832StTU7inal4hs4faSo9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ترفند گاز خونت را مثل روز اولش کن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/680447" target="_blank">📅 00:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680446">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
درخواست محرمانه عربستان از یمن برای پایان درگیری
🔹
در پی ضربات موثر انصارالله به مواضع ارتش و مزدوران سعودی در یمن، ریاض در پیامی محرمانه به هیئت مذاکره کننده یمنی ابراز داشته که خواستار پایان درگیری و بازگشت به توافق سال ۲۰۲۲ ریاض-صنعا بوده و این درخواست را به هیئت یمنی منتقل کرده است.
🔹
این درخواست با مخالفت مقامات انصار الله روبرو شده است. صنعا پس از دریافت پیام عقب نشینی ریاض از مواضع خصمانه اخیر تاکید کرده است که به دنبال دریافت تضمین‌های جدی و واقعی برای تامین منافع ملت یمن به ویژه در مورد پایان محاصره، دریافت غرامت و پایان دادن به مداخلات عربستان در امور داخلی یمن است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/680446" target="_blank">📅 00:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680445">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
پاکسازی در موساد؛ ضرورت امنیتی یا تسویه حساب سیاسی؟
شبکه المیادین:
🔹
دستگاه جاسوسی رژیم صهیونیستی در مقطع کنونی با بحرانی چندلایه مواجه است.
🔹
بحران کنونی موساد، با برکناری دو مقام ارشد این سازمان، فراتر از کنار گذاشتن چند مسئول اطلاعاتی است و به ماهیت رویکرد امنیتی این دستگاه مربوط می‌شود.
🔹
فاش شده است که موساد در طرحی برای ایجاد بی‌ثباتی و تغییر ساختار سیاسی ایران، از شبکه‌ای از عوامل و نیروهای داخلی و همچنین نیروهای کرد در مناطق مرزی استفاده کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/680445" target="_blank">📅 00:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680444">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8e4ebf62b.mp4?token=FlGi4qYQYwAjshmdnKVcu7ffNJnYeoB2dz5sSDWGvC7h83LM4ElJUeEejDOwO005eqiMHh-18ftjV3ucXJcZMg0iHikiVkEMm02cOfzcSLNFsptenHlBmLtCLbGkD_RzodaS1PrXrMzxmA6rNlphMpGyMLYQd_tK93EcN8RqSdvaKXKVsjhlz6LM4u2SvB6x_QvGKstF_whK3obkET3nc53qzY7JwnRPTsQ9lrypWQy79WQDKk-HrxocmnfmFNsYAjHFg1joBBK3LnL__bqsFiIEhaw4S8IvZ8p4aqLIjDScU0NPpexiqDBOYMnUAdp9THEBSqfnB3zdxxLmLX16JX3LRAwDtM1_piD4GzA3__S_-hwreb_LrBdQ-tmGF2x2Q71Q-GHv3mW5iqLez3WaBE04Qr0Fyk7z3TTcu3W8Kq-Vps9VMQiw-bV8jqer7yliuMyoFs3vvipEHlgaBzOY6d-Xs9gaxx2A0lk77Vcf8PZFYd16ROUQx7I0BHRzxznkgLpMTd4BWFpyfDns8pXjkzXrw0TwpkWcKzMTzPrIS8lArPQk_u3dJBCLKAd6U5jCzO72AlY69VPzZvkvblpWPbIHKjuysuSROaFLEKs6vS4fxpxuevAq8zi48724xTCBFC3B7Potn7m0gqe85eAWqfdBuL9mFbGF5ghzu3ANzOk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8e4ebf62b.mp4?token=FlGi4qYQYwAjshmdnKVcu7ffNJnYeoB2dz5sSDWGvC7h83LM4ElJUeEejDOwO005eqiMHh-18ftjV3ucXJcZMg0iHikiVkEMm02cOfzcSLNFsptenHlBmLtCLbGkD_RzodaS1PrXrMzxmA6rNlphMpGyMLYQd_tK93EcN8RqSdvaKXKVsjhlz6LM4u2SvB6x_QvGKstF_whK3obkET3nc53qzY7JwnRPTsQ9lrypWQy79WQDKk-HrxocmnfmFNsYAjHFg1joBBK3LnL__bqsFiIEhaw4S8IvZ8p4aqLIjDScU0NPpexiqDBOYMnUAdp9THEBSqfnB3zdxxLmLX16JX3LRAwDtM1_piD4GzA3__S_-hwreb_LrBdQ-tmGF2x2Q71Q-GHv3mW5iqLez3WaBE04Qr0Fyk7z3TTcu3W8Kq-Vps9VMQiw-bV8jqer7yliuMyoFs3vvipEHlgaBzOY6d-Xs9gaxx2A0lk77Vcf8PZFYd16ROUQx7I0BHRzxznkgLpMTd4BWFpyfDns8pXjkzXrw0TwpkWcKzMTzPrIS8lArPQk_u3dJBCLKAd6U5jCzO72AlY69VPzZvkvblpWPbIHKjuysuSROaFLEKs6vS4fxpxuevAq8zi48724xTCBFC3B7Potn7m0gqe85eAWqfdBuL9mFbGF5ghzu3ANzOk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: ایران عضو بانک بریکس می‌شود
رئیس‌کل بانک مرکزی:
🔹
مهم‌ترین نتیجه همکاری‌های کشورهای عضو بریکس، تاسیس بانک توسعه نوین (بانک بریکس) است که کشور ما نیز به زودی عضو این بانک خواهد شد.
🔹
همکاری‌های خوبی بین کشور ما و هندوستان در زمینه‌های پولی، بانکی و اقتصاد دیجیتال آغاز شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/680444" target="_blank">📅 00:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680443">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
ادعای وزیر انرژی آمریکا درباره صادرات نفت در تنگه هرمز
وزیر انرژی آمریکا:
🔹
میانگین هفت‌روزه نفت خروجی از تنگه هرمز در حال حاضر به نزدیک ۹ میلیون بشکه در روز رسیده است.
🔹
میزانی از نفت از طریق خطوط لوله و تاسیسات صادراتی ارتقا یافته‌ از منطقه خارج می‌شود.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/680443" target="_blank">📅 00:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680442">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Amq3TYxnD71vXd83DZc5UHPvDoLVwccrf8MHOP7an1qHYGtu6N59Ea9o5RovnU_STOBkNUJ27hN8CrJF9ub_qBLO_LBRYuLCcWMxibNSKENY71OSk6lOvJmm1M8SylZZKqsmfDV5SYomN4BrDore_7GoSQbmgPLKfXo8cO8xXAY4COCtu0qyg_JOSwRgiBJZWOJe4NCwoj72utGuaXpsnH7K4kYaqNKaH2yugC2jI-ReWT84bOpP0_ttGl2mKtl6gxZXAMJE4tDFpuG9K73PpOEQ2PHm8pTsZAzKIIrumBZv1Ojqzvi6lGffXB225zm01fiDIZudfjcCan4LYsT1Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/680442" target="_blank">📅 00:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680441">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
فرماندار شهرستان قشم، پرواز هر نوع بالگرد آمریکایی در محدوده شهرستان قشم را تکذیب کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/680441" target="_blank">📅 23:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680440">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRNwf8HAC-njTNSoYsHxSZZcapowxgf_r67SVy8lFupd26d1U3tExnWJyFxhujrT6aeG_1iiKItrkSjLC0cfBWGKCERXguz5YpaJvVG3lOUjcRp5mb7AcZ2b-Ly8oHVv_CnPGFNtHvVvni_U9opzKNqOSWNkz5gn42DVYNHfhoUP1bSvVJSzNbz2IiqttunB7ifAnwgLhYlrKsdKb_D4MpKmMAPjzX8QmHHgKM8Xlz4Z85F6ahgT5X2z9RS80iX1bgUexy6ysRiFQ2-TboAjdqTLeMqABsGFwQ5ynUE17Pq5uaRtEf9Pe2DErGP5XR05m30TIz9sSjQCZHoLzFaOAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع خبری از حمله‌های هوایی، توپخانه‌‌ای و تخریب خانه‌ها در نقاط مختلف جنوب لبنان از سوی رژیم صهیونیستی خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/680440" target="_blank">📅 23:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680439">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ویدیویی از دیدار وزیر کشور پاکستان با رئیس‌جمهور پزشکیان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/680439" target="_blank">📅 23:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680438">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PubGat7UsvIYF7q5N8seiPobqCL8p6Jg2QHDh6iVZtT3SH0lpEb1zuMnJyGOn4SYMEHw_mtfEeYhcxK9uJxVGI8rAZ-qULw4fpkk4m4Kd07OuFzIGWjXpYXWi8EPtthUCmwY9NAMaT33ruzXgU0vaDvnY20klg2yDO4IWqPvIv9wbw_GeiNzoPWJl_EqLKosWv7W8NUabrL0xe6RAZSQdyhmfjI1H5Tp7Hd8116HyW7bofywf-n1XkK-98xHBU-lCnPyL7JIN2fRq6rbBv62cQlwyQQpofHhtQjL-JlCa0tBPm_MJJEtgpB_VVX6666Y-C3TfKEVT86eKLrv2uVKRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آتش‌سوزی مشکوک در نزدیکی فرودگاهی در واشنگتن
🔹
رسانه‌های آمریکایی از آتش‌سوزی در نزدیکی فرودگاه اسپوکین در ایالت واشنگتن آمریکا و توقف فعالیت در این فرودگاه خبر می‌دهند.
🔹
آمریکایی‌ها تاکنون علتی برای این آتش‌سوزی مخابره نکرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/680438" target="_blank">📅 23:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680437">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgYkK3MDz99iKf-qyckGGS3qhtvT88W8PSw0Y9xJLfMGqzQvAbKSLsFV26pWa-oVdXeTyOmYHRet6GjOOui1N6SM3vBwlm82icnx59CTR6_bRi09IiXBaYwCAM7yWETEIrJvXW4n4G6-U3fFrbBcyL5jxvXHqJwf9yqZSyRMh0dHE8yXT5QS6keUYUZMWoHb_D4czkYZPcd8Imk-eAc0MWsMrEyE2QhMTIAxrR_8wLpycr4_Id50eHJH3L0ngpT9Q1zMMwrJJmvQYmKlDAV4iIPcyna4g41Up7_dIkRvc96ukgfnCU_kX2-N9yLubM-NBH3MYOssfyxbYLNo5UqiZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار فعالیت سامانه بارشی جدید؛ تداوم موج گرمای شدید در یک استان
کارشناس هواشناسی:
🔹
سامانه بارشی جدید از روز چهارشنبه در چند استان کشور همراه با رگبار، رعدوبرق و وزش باد شدید آغاز می‌شود، همچنین موج گرما تا روز جمعه در استان یزد تداوم خواهد داشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/680437" target="_blank">📅 23:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680436">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
حمله هوایی رژیم صهیونیستی به جنوب لبنان
🔹
شبکه المنار گزارش داد که جنگنده‌های رژیم صهیونیستی دره الحجیر در اطراف شهرک دیر سریان را بمباران کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/680436" target="_blank">📅 23:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680435">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMfrp02HC8psO1WI13fupOZH1Eoz6G4vQrYOU5C20iuZAF_z08RgLpfzi35mhQodL85n-Haz0nSulkqzlaRjTWGmNIqpg8jMrm7fL0Eii9fKxwGAhvRwx2uceTN1HLJGfgR2b-3wFNWz9DDPzpeFRPRzvfoN3fYkakC4aOG2LRCY2sdEkp-SAluSNO6IBybZduS4YH-GCO5qaGK_WWgxsD121MkvUOY3IrGfUMbD9WraTe0FzkB-oLhurTr34CA5EtHtIzjsBR0JCAKmsWKrmtXnTIAM4bW8BKdthfXsKZK_GeoeFB7xk16WnIDos_2GiFGQS0SGI-bm7dQU8aHDDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه بقائی به آمریکا؛ آیا جهان در حال بازگشت به دوران «غرب وحشی» است؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/680435" target="_blank">📅 23:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680434">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
سردارنقدی: تولیدات موشکی و پهپادی ما تمامی ندارد
🔹
ما بیش از نواخت شلیک موشک‌های بالستیک تولید می‌کنیم و به دست رزمندگان اسلام می‌رسانیم. در حوزهٔ پهپادی نیز قابلیت تولید ما بسیار بیشتر از نواخت شلیک است.
🔹
اگر جنگ چند سال هم طول بکشد، باز هم موشک‌های بالستیک…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/680434" target="_blank">📅 23:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680432">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b5981ac86.mp4?token=kc51Et97SxnEeoz0DsEINHVmEByflJbVMJkQH1s1Q32e3tX5wj1OhDUffdCY0iOKydK6LLO4Gd_Q-32kZ9UyCDKNfVgZ-K5piMON2uGt9p9KulXl_EPl3BO81uYWmTr4BuNpagWfrrpCM6NsNwi_h20WUWoe-VxvJgUmq1zdXgwcyKozLRfxG4UIfU3rr1W-lvIz2ReDGeT0kdXhLGATtyNkYIHX5dO7r8BGk9WQPVFgigMYVgsNLr_3puAZEBqRE9xLw2T8hEsKq1IPDC5rAA-Rgik7MODrLgmknZC2JqmssMyKODi23jQr8ccKYXIg5uNciGhzuVSg1hSj7uKqKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b5981ac86.mp4?token=kc51Et97SxnEeoz0DsEINHVmEByflJbVMJkQH1s1Q32e3tX5wj1OhDUffdCY0iOKydK6LLO4Gd_Q-32kZ9UyCDKNfVgZ-K5piMON2uGt9p9KulXl_EPl3BO81uYWmTr4BuNpagWfrrpCM6NsNwi_h20WUWoe-VxvJgUmq1zdXgwcyKozLRfxG4UIfU3rr1W-lvIz2ReDGeT0kdXhLGATtyNkYIHX5dO7r8BGk9WQPVFgigMYVgsNLr_3puAZEBqRE9xLw2T8hEsKq1IPDC5rAA-Rgik7MODrLgmknZC2JqmssMyKODi23jQr8ccKYXIg5uNciGhzuVSg1hSj7uKqKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت سالروز شهادت امام رضا (ع)| حاجت‌روا
🔹
صداهایی از جنس امید؛ روایت شما از کرامت و نگاه ویژه امام رضا (ع) در زندگی.
🔸
الوفوری را دنبال کنید
👇
#حاجت_روا
@Alo_fori</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/680432" target="_blank">📅 23:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680431">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSJ6VPfK7UN7zgJuArVzchuabRlG9W-m2dIRyluHQR1iZ6n9MVE9btCwGDKz9hHJsVZvcZbMtloYHDEFHQ4iXZVa6_XGbWejXbQeWOkXfghZ6Nm4G2nbEy30TDqYbFCgZgYXoYeXgO-Tili5_sgaEht_BlL2-0snI-SwQ44INTUT4OUyeQBQt_3y_WENNvtm-dYwFU7xPmWdeqmPkqpYdlUppbY_u5cYweNb2sV4i3IgaqPrtyoOd_6m0b2sMxDSbKdQHzN-tw9mLy5ULJAX-7QZGBabhyBK3q8IOW0AjisG94VjXXmGONCXkUWJ2GzJ9McYpwfbkydabIiT10dAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ری اکشن جالب یک مخاطب به رفتار دیوانه وار ترامپ
🔹
بزار ببینم‌ درست متوجه شدم ؟
🔹
ترامپ صدها دختر دانش‌آموز را کشت، سربازان آمریکایی را کشت، صدها نیروی نظامی زخمی کرد، قیمت بنزین را سر به فلک کشید، ذخایر موشکی ما را مصرف کرد.
🔹
همه این کارها برای این بود که در نهایت به ایران اجازه دهد کنترل تنگه هرمز را به دست بگیرد؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/680431" target="_blank">📅 23:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680430">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/823f7565ed.mp4?token=qBrBToiMtckkbJTe1WucKYwWb-c6_a0m8S14fibkedCBJVPVhTE17pczTVJAcRtcdJ5DFoOXShOgqDLH7shmPV1bRbPoEZfbTXqrk5M119xEJ41I1EPw1D4Ty9OrFAuJSZeWfpFHWKgOqBWaIpWJUkZavtRn00c3AlUFjoECyZzdDj8jX9vzvDoAeeXP390kxxQUYruxsGVS3f-BvyEv3tOaZ4JTb52IKiC8vlO7XWsuRF8tcjntumq2Hm_7yLviwuvz-lATMZxwAqmwId2EZvAUfuS9rEccJFT1LvEh_8EMzEsbEJQBODRP4llCjWo7m66r-keoK03zSirONqTSQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/823f7565ed.mp4?token=qBrBToiMtckkbJTe1WucKYwWb-c6_a0m8S14fibkedCBJVPVhTE17pczTVJAcRtcdJ5DFoOXShOgqDLH7shmPV1bRbPoEZfbTXqrk5M119xEJ41I1EPw1D4Ty9OrFAuJSZeWfpFHWKgOqBWaIpWJUkZavtRn00c3AlUFjoECyZzdDj8jX9vzvDoAeeXP390kxxQUYruxsGVS3f-BvyEv3tOaZ4JTb52IKiC8vlO7XWsuRF8tcjntumq2Hm_7yLviwuvz-lATMZxwAqmwId2EZvAUfuS9rEccJFT1LvEh_8EMzEsbEJQBODRP4llCjWo7m66r-keoK03zSirONqTSQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی: پیروزی ما حاصل حضور مردم در میدان و نفوذ در جهان بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/680430" target="_blank">📅 23:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680429">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5tYcpeTkLQKidzLjfUnfKiTMiCpL14x2rYKjM7qgU3MX1xnO5S-OKnfSjB0bMEfEGIdF1M2PgKhaFlxWQRyC8N60ocCqqdeTYqPCauTEMtJSX5r31qhKR783xYEYtFnuwHs-FvNem7w4lDEi4ptEppwuKKVIaD3oLmMzKJaQ-0Hf5UD5C_gta4ITGDrLINT2fHXzu2aXLJcVqRyKqofcGVm9g9Kk_LxSKa-A76_8GGhWOBkmu8bP3ISeBlxmF00Et3snZWMlGSzCcLkZscQKsLZs81bUhfJuTZbuZfGIUYdIQnKttjAcbm4LAD2-Y4aTAdHirMqk19zt-3sLhTYXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست اینستاگرامی رونالدو برای ازدواجش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/680429" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680428">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔹
اگر فرصت مرور همه خبرهای امروز را نداشته‌اید، جذاب‌ترین‌ها در دسترس شماست
🔹
🔹
محسن رضایی شروط بازگشایی تنگه هرمز را اعلام کرد
👇
khabarfoori.com/fa/tiny/news-3237163
🔹
ترامپ چگونه در یک عملیات مخفی از ترکیه خارج شد؟ | فرار با کامیون غذا
👇
khabarfoori.com/fa/tiny/news-3237044
🔹
عکس های خانوادگی حمیدرضا رجب زاده مداحی که به قتل رسید
👇
khabarfoori.com/fa/tiny/news-3236968
🔹
محاصره دریایی از جنگ هم بدتر است و باید بشکند
👇
khabarfoori.com/fa/tiny/news-3237132
🔹
بشار اسد به اعدام محکوم شد
👇
khabarfoori.com/fa/tiny/news-3237066
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/680428" target="_blank">📅 23:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680427">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/200c140ffa.mp4?token=N6q7YURVHJiRh1spcRxhVzS13_chJRXwT2VSXfst-LjYwy2JoUptc4dtPaCrc2kCreQV_CaROk0zH6sbb4wfNW9sUuPPpsLDBAFNAR9_zjmE_ITSzuWSwQ997i3OQBzlv2-HsZt2602yx_VuT_ax-jFWBdD-FNYKIbCfPWBu3GVb50krVk857jRKhDtcsD19VMK0o8AnCrT0FKKb66ynDJNKVlcAzv3LITUPjpsnzImxy7GxQ_XADsw7i7JjelzEoPWEqPnKFLVkB2VXXIOQIcr_BljDZo42q2kFESVgJ_fXAbXcF5HI87jFVyuxpW44C4TAPZNIf3um6rlZIcV8TE4guupp_crFavs_aOgBI7jLGOsi3wlz4j7GE-BQ54N9QW6IbX1x3KVzWP7vd6QwAFWeclwux2fpoTkQ4sGcjhw3z-OL45kZObxrNF4Vy-vVoknRRWdBqbci1DGPGia3uQmS4g7RpMmw3Xq0iGHzzbT4hYwvsFU_0sOGulop1RLOM0hpUSfk8ytKAKk_X1f8E-5eVASGuuE1sVdzB9JzLClqX2Iy_L7cBrntp0WAwLotGve__N62BVEcq-GkGX8NK1DFGMJi-zCh8KAk0-v4-euAsiwwTgnxcpelOTV5lnlL0N8aF86jc3z4aP2qm5-4QVNajrBXsrLVAyCyAmaw4i8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/200c140ffa.mp4?token=N6q7YURVHJiRh1spcRxhVzS13_chJRXwT2VSXfst-LjYwy2JoUptc4dtPaCrc2kCreQV_CaROk0zH6sbb4wfNW9sUuPPpsLDBAFNAR9_zjmE_ITSzuWSwQ997i3OQBzlv2-HsZt2602yx_VuT_ax-jFWBdD-FNYKIbCfPWBu3GVb50krVk857jRKhDtcsD19VMK0o8AnCrT0FKKb66ynDJNKVlcAzv3LITUPjpsnzImxy7GxQ_XADsw7i7JjelzEoPWEqPnKFLVkB2VXXIOQIcr_BljDZo42q2kFESVgJ_fXAbXcF5HI87jFVyuxpW44C4TAPZNIf3um6rlZIcV8TE4guupp_crFavs_aOgBI7jLGOsi3wlz4j7GE-BQ54N9QW6IbX1x3KVzWP7vd6QwAFWeclwux2fpoTkQ4sGcjhw3z-OL45kZObxrNF4Vy-vVoknRRWdBqbci1DGPGia3uQmS4g7RpMmw3Xq0iGHzzbT4hYwvsFU_0sOGulop1RLOM0hpUSfk8ytKAKk_X1f8E-5eVASGuuE1sVdzB9JzLClqX2Iy_L7cBrntp0WAwLotGve__N62BVEcq-GkGX8NK1DFGMJi-zCh8KAk0-v4-euAsiwwTgnxcpelOTV5lnlL0N8aF86jc3z4aP2qm5-4QVNajrBXsrLVAyCyAmaw4i8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر مقاومت کردید، آن وقت قلّه را فتح خواهید کرد؛ کاری که از بعد از زمان رسول خدا تا امروز انجام نگرفته، این کار، کار شما است.</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/680427" target="_blank">📅 23:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680426">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6cb1de1d.mp4?token=sVebvM-9EC_flIl8QVR82ATAEA-VRLyvopagglCPjK7abpNSQ8lznKdwZWs94T6AjX_j7CZIva37QH08dlJIouqkXaNi73L9jRC8DSTnFM0TGuo43mpQo4hydp47l0pUllG07D-tb6tuyQm3wsN32sZhnkEOxXlobwGsPOIsdxMYhaO1tZlhVIYZaUkDGHn9bpr3WxpUI0XUyI4Xc7T1Zmf-GdnlwO8_P6GRX5OaquEHui_z6odkwcVaDgPnZITQM-c2EJJnv7FpT9924PGkkZCVG7PhoH_WSZVrAZL-P62jdvLIaaSvGn_OieYFe_RteK0i4gI845CP9SqeeNvpnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6cb1de1d.mp4?token=sVebvM-9EC_flIl8QVR82ATAEA-VRLyvopagglCPjK7abpNSQ8lznKdwZWs94T6AjX_j7CZIva37QH08dlJIouqkXaNi73L9jRC8DSTnFM0TGuo43mpQo4hydp47l0pUllG07D-tb6tuyQm3wsN32sZhnkEOxXlobwGsPOIsdxMYhaO1tZlhVIYZaUkDGHn9bpr3WxpUI0XUyI4Xc7T1Zmf-GdnlwO8_P6GRX5OaquEHui_z6odkwcVaDgPnZITQM-c2EJJnv7FpT9924PGkkZCVG7PhoH_WSZVrAZL-P62jdvLIaaSvGn_OieYFe_RteK0i4gI845CP9SqeeNvpnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی، مشاور عالی فرمانده کل سپاه پاسداران: سپاه باید آماده عملیات هوشمندانه در خاک دشمن باشد
🔹
هر موقع اقتضا کند و فرمان صادر شود، باید بتوانیم عملیات را به خاک دشمن، به سرزمین‌های دشمن بکشیم و دور از سرزمین خودمان بتوانیم عملیات انجام دهیم.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/680426" target="_blank">📅 23:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680425">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afac585917.mp4?token=XMXi0ot4nFFVWGMwUKb7JlKhfesa8wxW4kO08LFPAaikqTC2bbQ6QRzVDNdM-fbJ9j-ejmEfbnanjOg0pS66iIBaUpENV6Gj8zyFDpXXnBz7fk0qICL58X14-ZGPHD09TwWUAF9bDRHWi6kL1DRjhjlACYvc7tj3I8GynUkHhUjZusctqDCOpjG0ahi8D-YmtVjPZJjAnoUBG6ghTllOS-NB11jnnNz8Pb3OcYWB9b3MqUjfpMGeSSTkSy6_BhUAkavQXPSgzpA1gUBZ1aZBJLX9yYy57-13UUBFaxANqABWL_lrvebajSGHTcCA9VWenMQV-_biS54H4siVqO2pC6h8ch2rXpaZXDLp5WBh4OIVouJsyamklnoyrobLQf2K1r_2-ADfwF8Ksl7Vt-pbPx0ba8ZJvQWxKCxcWT7vMh6qD7Wbw4iGsLwL5CStP0H5Fc0F8Mga-jw0H4lodIq4VN5h91NwpMMFixy_oKkOmSYbl2yf7yJYd4ubQwvVL1C91TFvwmospd4PVBpJF92Ot4NTihxt7uhCHwcQimhyOSKB2GIlr4eVrxp51I95Obx6bxXHN3MoMOWljLLVSF4W9cD-T-T7W4IlAteQKk-wFcbmv6i89mPZ6g8lPEb0kJC3K3Dx-nUT2FKwc3e7Opa0XmOeqJJ6a0SN6lC6ELCSRiU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afac585917.mp4?token=XMXi0ot4nFFVWGMwUKb7JlKhfesa8wxW4kO08LFPAaikqTC2bbQ6QRzVDNdM-fbJ9j-ejmEfbnanjOg0pS66iIBaUpENV6Gj8zyFDpXXnBz7fk0qICL58X14-ZGPHD09TwWUAF9bDRHWi6kL1DRjhjlACYvc7tj3I8GynUkHhUjZusctqDCOpjG0ahi8D-YmtVjPZJjAnoUBG6ghTllOS-NB11jnnNz8Pb3OcYWB9b3MqUjfpMGeSSTkSy6_BhUAkavQXPSgzpA1gUBZ1aZBJLX9yYy57-13UUBFaxANqABWL_lrvebajSGHTcCA9VWenMQV-_biS54H4siVqO2pC6h8ch2rXpaZXDLp5WBh4OIVouJsyamklnoyrobLQf2K1r_2-ADfwF8Ksl7Vt-pbPx0ba8ZJvQWxKCxcWT7vMh6qD7Wbw4iGsLwL5CStP0H5Fc0F8Mga-jw0H4lodIq4VN5h91NwpMMFixy_oKkOmSYbl2yf7yJYd4ubQwvVL1C91TFvwmospd4PVBpJF92Ot4NTihxt7uhCHwcQimhyOSKB2GIlr4eVrxp51I95Obx6bxXHN3MoMOWljLLVSF4W9cD-T-T7W4IlAteQKk-wFcbmv6i89mPZ6g8lPEb0kJC3K3Dx-nUT2FKwc3e7Opa0XmOeqJJ6a0SN6lC6ELCSRiU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان فرار مخوف شرور مسلح در عملیات مشترک پلیس
🔹
معاون مبارزه با شرارت پلیس امنیت عمومی فراجا از دستگیری شرور مسلحی خبر داد که پس از شلیک به یک شهروند، با تهیه گواهی فوت جعلی تا مدتی با هویت جعلی در ایران زندگی می‌کرد اما سرانجام در عملیات مشترک پلیس امنیت عمومی و پلیس فتا دستگیر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/680425" target="_blank">📅 23:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680424">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/894ec0af40.mp4?token=OCCQ4SAfLLehi9No90ijJBMo-gdSOv2cs2Uliflp8BxxhkQgs8zCJLNpcYJfjRypptPg2Eck4qN0ePT_tbdj85pGnnx81fgzfN-cMlzgv9pI25__i-drhKuyKtSvauWWicbw0XAURKNixj7ho0vTq6gew7M_1qe7Z4Gn2fiiq6WkoKlW-WzBi4PSAU2yZD5MFW1kklcWLASb2u4bJQf0zll0SpHLH5tPmjQrPDvMB5RJVltNMc33j-am4UgvOA2le8MOM_oI0Yu3AgUVU3gLGuCMwVKu2B1eMCLXF739be83_xVbk83RcIQEfNS79r060xwIRaMbD8FWbSvfQLcMyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/894ec0af40.mp4?token=OCCQ4SAfLLehi9No90ijJBMo-gdSOv2cs2Uliflp8BxxhkQgs8zCJLNpcYJfjRypptPg2Eck4qN0ePT_tbdj85pGnnx81fgzfN-cMlzgv9pI25__i-drhKuyKtSvauWWicbw0XAURKNixj7ho0vTq6gew7M_1qe7Z4Gn2fiiq6WkoKlW-WzBi4PSAU2yZD5MFW1kklcWLASb2u4bJQf0zll0SpHLH5tPmjQrPDvMB5RJVltNMc33j-am4UgvOA2le8MOM_oI0Yu3AgUVU3gLGuCMwVKu2B1eMCLXF739be83_xVbk83RcIQEfNS79r060xwIRaMbD8FWbSvfQLcMyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی، مشاور عالی فرمانده کل سپاه پاسداران: سپاه باید آماده عملیات هوشمندانه در خاک دشمن باشد
🔹
هر موقع اقتضا کند و فرمان صادر شود، باید بتوانیم عملیات را به خاک دشمن، به سرزمین‌های دشمن بکشیم و دور از سرزمین خودمان بتوانیم عملیات انجام دهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/680424" target="_blank">📅 23:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680423">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
عراق اقدام کلمبیا در به رسمیت شناختن حاکمیت اسرائیل بر بلندی‌های جولان را محکوم کرد
🔹
وزارت امور خارجه عراق تصمیم کلمبیا برای به رسمیت شناختن حاکمیت رژیم اسرائیل بر بلندی‌های جولان اشغالی سوریه را به شدت محکوم کرد و افزود که این تصمیم هیچ اثر قانونی ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/680423" target="_blank">📅 23:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680422">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7f7e509f.mp4?token=M7NqNZ-YSbeAbRefxL5ueJBGK_rcmEupbiCZQWvi48mzzGM11sFo9Ita-TlDzI31vd4r6IcAwu-4hjQ5PQTxCAgch837BUSSoqIuHYrToMbjNqVspbleVTK8hp_pKwx7_H2J9cEltdcDVAj0a9zWAtzrH4SZUthha5RictyxcDhh9c7tAFl4sTT3SKR6uJeNg_Bp8nDXYK22wKimi9CDEStWbBeynMSqdz8SgZkxHqnGiHOLFKtx7HY_hpKrW0OuJh6EcZLbZLq0IsTOKiPZUuqQUwviMoRQNuawpLlSUDmOkJhy8zseNU1-zBzoutVtFcdWxTrnzvuxj8q-6p-wpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7f7e509f.mp4?token=M7NqNZ-YSbeAbRefxL5ueJBGK_rcmEupbiCZQWvi48mzzGM11sFo9Ita-TlDzI31vd4r6IcAwu-4hjQ5PQTxCAgch837BUSSoqIuHYrToMbjNqVspbleVTK8hp_pKwx7_H2J9cEltdcDVAj0a9zWAtzrH4SZUthha5RictyxcDhh9c7tAFl4sTT3SKR6uJeNg_Bp8nDXYK22wKimi9CDEStWbBeynMSqdz8SgZkxHqnGiHOLFKtx7HY_hpKrW0OuJh6EcZLbZLq0IsTOKiPZUuqQUwviMoRQNuawpLlSUDmOkJhy8zseNU1-zBzoutVtFcdWxTrnzvuxj8q-6p-wpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی: تشییع رهبری اگر در نیویورک و لندن هم انجام می‌شد، میلیون ها نفر شرکت می‌کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/680422" target="_blank">📅 23:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680421">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ده ها کشته و زخمی در میان مزدوران سعودی در حملات ارتش یمن
🔹
سرتیپ یحیی سریع سخنگوی نیروهای مسلح یمن از حملات موفق موشکی و پهپادی به مقرهای مزدوران عربستان سعودی خبر داد.
🔹
نیروهای مسلح یمن با تعداد زیادی موشک بالستیک و پهپاد، محل تجمع، انبارهای تسلیحات و مقرهای فرماندهی مزدوران سعودی را در منطقه المخا در هم کوبیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/680421" target="_blank">📅 22:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680420">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
روایت نیویورک‌تایمز از راز نخستین آتش‌بس ترامپ با ایران
🔹
روزنامه آمریکایی نیویورک‌تایمز در بخشی از گزارش مفصل امروز خود (سه‌شنبه) درباره نحوه تحول و تکامل تاکتیک‌های نظامی ایران در جریان جنگ رمضان به ارائه جزئیات جدیدی درباره یکی از عوامل موثر بر تصمیم دونالد ترامپ برای اعلام آتش‌بس دو هفته‌ای  با ایران در فروردین‌ماه پرداخته است.
🔹
جزئیات ارائه‌شده در بخشی از این گزارش حاکی است سرنگونی جنگنده اف-۱۵ئی آمریکایی بر اثر شلیک آتش نظامیان ایران در ۱۴ فروردین‌ماه (سوم آوریل) یکی از دلایل تصمیم ترامپ در این زمینه بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/680420" target="_blank">📅 22:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680418">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/839e31ae75.mp4?token=Ne3FdtNMZT3OCu0gpKJvBX-Y_6kWtHtJTXqgSJ6sjtVUqkTdw9QNm3XFVqeDtDEViUHANMmsPvoZz6k7X7sw5boVH8R3b2ZNsZSzb_CG8QKO5wF0OPvSmQ_0W-A9I7I64APvnUHbUVUhzJobf5gsM70HTMNggAyPzThGSicd1xSMLJnEJMo47RFCaKuzvnJ1QQy0y7V-f7Y9_jvtE4o_OaYVIhCSUWM0pd6sNapZrReR-xneF4HHjNJEyn7arHJlzb_QJEz_wv8HyZa6-DLXwN3xpsX3CDx7B7RW2TgdHZ-GeuaeaW8y5NC3hZisXDwxAHRGtwU34ovMIf4rSYY0wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/839e31ae75.mp4?token=Ne3FdtNMZT3OCu0gpKJvBX-Y_6kWtHtJTXqgSJ6sjtVUqkTdw9QNm3XFVqeDtDEViUHANMmsPvoZz6k7X7sw5boVH8R3b2ZNsZSzb_CG8QKO5wF0OPvSmQ_0W-A9I7I64APvnUHbUVUhzJobf5gsM70HTMNggAyPzThGSicd1xSMLJnEJMo47RFCaKuzvnJ1QQy0y7V-f7Y9_jvtE4o_OaYVIhCSUWM0pd6sNapZrReR-xneF4HHjNJEyn7arHJlzb_QJEz_wv8HyZa6-DLXwN3xpsX3CDx7B7RW2TgdHZ-GeuaeaW8y5NC3hZisXDwxAHRGtwU34ovMIf4rSYY0wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردارنقدی: بعد از جنگ، جمهوری اسلامی طرفداران زیادی در دنیا پیدا کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/680418" target="_blank">📅 22:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680417">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
برخی منابع از وقوع ۲ انفجار مجدد در مواضع مزدوران سعودی در مأرب یمن خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/680417" target="_blank">📅 22:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680416">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
۲ مقام آمریکایی: ایران تنها در یک روز آمریکا را به شلیک ۵۰ پاتریوت مجبور کرد
🔹
۲ مقام آمریکایی امروز در گفت‌وگو با نیویورک‌تایمز خبر داده‌اند که تنها در یک روز از ۵ روزه نبرد میان ایران و ایالات‌متحده، آمریکا مجبور به شلیک حدود ۵۰ تیر موشک پاتریوت شد که هر کدام حدود ۴ میلیون دلار قیمت دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/680416" target="_blank">📅 22:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680415">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdcee01ee6.mp4?token=p2JEipN9UR7EiIQz_bkzBofpCRGr3SLvGaudgO584uJLe1O1mL8rQCg-mS1tLBcinbki6QmxIX4cvfTJiWbu6RQnHDRpNOjfUUm-NXN2Q7-ZmMzF9iEBJVihmGA4xGkc3UEDp1nLi9UORgCdcHiUtxwcPsJU53vA7O72sdvjcVOsBuZeQ6ZIfsUqQrygH0Tbbmr89uIX1xCUZ4gki471eumwsiPuQ2J_bZay3zfkOKo9aRJLX_w6VwYb5e9Rs6xAa1oJO9UhiEw-ZjIGR5-vhukUgOAdDxETXLsyGYQNp7iZaCYCRfRzjbkfGCCG1IWYwFTK4DDCcfa89V-86EEPLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdcee01ee6.mp4?token=p2JEipN9UR7EiIQz_bkzBofpCRGr3SLvGaudgO584uJLe1O1mL8rQCg-mS1tLBcinbki6QmxIX4cvfTJiWbu6RQnHDRpNOjfUUm-NXN2Q7-ZmMzF9iEBJVihmGA4xGkc3UEDp1nLi9UORgCdcHiUtxwcPsJU53vA7O72sdvjcVOsBuZeQ6ZIfsUqQrygH0Tbbmr89uIX1xCUZ4gki471eumwsiPuQ2J_bZay3zfkOKo9aRJLX_w6VwYb5e9Rs6xAa1oJO9UhiEw-ZjIGR5-vhukUgOAdDxETXLsyGYQNp7iZaCYCRfRzjbkfGCCG1IWYwFTK4DDCcfa89V-86EEPLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی: آن‌چه ما را برای جنگیدن متمایز می‌کند و دشمن آن را ندارد، ایمان است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/680415" target="_blank">📅 22:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680413">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NFklQHzTPMdfSIq_qYSPhQt76emKEFzBW8gkIzHwOdazk-MoYz2L3KqqjMDbZxF6nJ1r_nLBQ979uNEIcO6tSeSTy36YAGpnNDppTNYUYMPNZwktasui_fE_8E4Ol793RoRVad9IXAphu5JNaqKGEE2rbxjukrvjSG1UUxm3YuTYUWt-CYC-ZRKqhMSK1pXHWkymVoW5XAhPfJRZNjg2BOPTALU4IXM-UGBykJcqb1K1vQqmc9bxL96iZWoKCGMD3-FJLU3vw43Xzd1RL0ccYBgym7ZwEgbyQYXnagzUTqwrGYE1ofwDI6F1pZqGmtRcLC90iqAAYucBT_5gp-ydPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hI4xUoIC5rcaVK-TbW2nBtZ2y4V6Dt225etlvYlgYrckNV1HXdkD48YGtVDQxoNIGDZivrkDNR4SMjZboKMIIejUxoqRkHwREVGRSP1qftr4sqlCSEubv5Nfgu8zukVMjK-JmcVlkPFB14LOyXe4XnQnqXBWU6u6IiCAv4oWj2aixDltoka-31GsjnsCaqsMKpxqTHUajHbvYNEgbIr1R3-NDMJUn31uq9PNdafu3kMwk9hRfI_e08rptoSyPM2Cf8Bi3vauZsjC2b8B7F0ykjbyvtQeLbGiyk6NXPY450zYlAZ53-uGvmRrMi_f-4YVATk2aUKL8g6TkgVH1oOEIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/680413" target="_blank">📅 22:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680412">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbEKAjbRrWHblzm81dc7YAS0R1W1WthYO3gvtuWqSmWqg_O2EhIkxzOHlIO2kCnnVYDiERet9lRM_2r64WULqgqZCbiUIeoK5C3bRBoo7CwScro51KUrrWs2V4x_zNsIOXUSAuM72U2Mc10JO9HHeVkIdqv331UXnvnfR_1JEhmhehM-BXhzE5p75Cl54hbVnt9Mc3zsVRySBN_ixA1kxfvqZP9jM3tLsqHFlipOY8TINLw7HggpCssNOz_g65crFBoajj93eknRdcgpFJrE6W9gLH5EC6Vr2Fti51sdvAcObB2bBCTYW0ieWCWqGBbNBsBBQR3eaymjqIzv_ykdJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/680412" target="_blank">📅 22:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680411">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c873ad6ef.mp4?token=OrXCrQZd0R4tqU1W1WSH4qABLvqllMym-DLZHPHXMYsHkC6UZuA7BCCFnSbH3gjs8Av_MRwfgyALYV7k7S4GK55JzsoduMgV3b5RzY9cFi3UFOa45eC8w06-g1-5WcK8nrX1rDShU-Dog1sCiXrbqq5jgy9CA0VfYU-MWQ8lXx-xQHagIGU1yzGiNVLc_BMThFVXAabM_6ylrva8fbueSFWMTckNTEZzHM2wwOwOw5qkt1BfU-iY0LfFxp1oupc1syUEOuPyVuhM2TAI-WIBWi2PZ9XlJovrU_uFf2uCl2THACjbQB_PXHq2VcUulrSxiaRh4amuyzhdrIMS3TFO6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c873ad6ef.mp4?token=OrXCrQZd0R4tqU1W1WSH4qABLvqllMym-DLZHPHXMYsHkC6UZuA7BCCFnSbH3gjs8Av_MRwfgyALYV7k7S4GK55JzsoduMgV3b5RzY9cFi3UFOa45eC8w06-g1-5WcK8nrX1rDShU-Dog1sCiXrbqq5jgy9CA0VfYU-MWQ8lXx-xQHagIGU1yzGiNVLc_BMThFVXAabM_6ylrva8fbueSFWMTckNTEZzHM2wwOwOw5qkt1BfU-iY0LfFxp1oupc1syUEOuPyVuhM2TAI-WIBWi2PZ9XlJovrU_uFf2uCl2THACjbQB_PXHq2VcUulrSxiaRh4amuyzhdrIMS3TFO6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی: آن‌چه ما را برای جنگیدن متمایز می‌کند و دشمن آن را ندارد، ایمان است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/680411" target="_blank">📅 22:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680410">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
حسین پاک، کارشناس جبهه مقاومت: رژیم صهیونیستی هنوز نتوانسته بر تأسیسات مقاومت در منطقه علی‌الطاهر تسلط پیدا کند/ صهیونیست‌ها با آتشباری و حملات شیمیایی به دنبال کشف ورودی‌های این تأسیسات هستند/ ۷۷ روستا در جنوب لبنان تحت اشغال است و ۵۵ روستا به‌طور کامل از بین رفته‌اند/ صهیونیست‌ها برای کشف ورودی‌های تأسیسات علی‌الطاهر، فناوری‌های جدیدی از جمله سنسورهای حرکتی به کار گرفته‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/680410" target="_blank">📅 22:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680409">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1527d44c1e.mp4?token=eiM2NshewFeHT-0Me72whNAROugD3WGMQhWcdpphZNIR6YIR8VdSY5lF43153ZQdiHVcZvXdJsjePVLxABAj9Gf9XewxF8MEcMgWh9cfHlKgraTr8PBg7okAuXvalL1-AyJ5brL_eSpTj3rOHY6Z6_BlUfP5HgTFuvi1HCOPzEpkH39Z8BGX5HAFwluUZyJHOjuDuvA922f5YYjVqPE59jAgP9Ia5zdIZk-PH2XwYzuI2wAA6BhpMIesHyQtWtCu7_zh8K5LlZWLtuZbsOpWFStwfyrZpvPFiBPAwcn5y4R2uEC9SgZVAl_SenArIjx8m2m1CoMLXGaP7zmf1mX23g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1527d44c1e.mp4?token=eiM2NshewFeHT-0Me72whNAROugD3WGMQhWcdpphZNIR6YIR8VdSY5lF43153ZQdiHVcZvXdJsjePVLxABAj9Gf9XewxF8MEcMgWh9cfHlKgraTr8PBg7okAuXvalL1-AyJ5brL_eSpTj3rOHY6Z6_BlUfP5HgTFuvi1HCOPzEpkH39Z8BGX5HAFwluUZyJHOjuDuvA922f5YYjVqPE59jAgP9Ia5zdIZk-PH2XwYzuI2wAA6BhpMIesHyQtWtCu7_zh8K5LlZWLtuZbsOpWFStwfyrZpvPFiBPAwcn5y4R2uEC9SgZVAl_SenArIjx8m2m1CoMLXGaP7zmf1mX23g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی: همه تسلیحات نظامی ما بومی هستند
🔹
ارتشی که الان ما با آن می‌جنگیم صد برابر بودجه سالانه نیروهای مسلح ما بودجه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/680409" target="_blank">📅 22:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680408">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc9565fe8c.mp4?token=VKCn7j4cMQyWWu3WGrP8htIup3U3xwHyXPjxuSLacZA7zDB5gZdbIWrOU0D9fP1JtY3tSd5rnuYGRA7n2BfsoPaq7X5I6BncekYbxTGqGfyksBC8ZSqAeT3LkYW0tyOD9rmG-NJtjHiAetqgYBdSI0depxiYxA03-pavjm8C_cZ3JGp-66NSVVVIMPbUA8bLd1OR7Vj-z32fvl9wQlv32hZTPBVZ1CLwFmg7wfobUpA_eJrDPj29dpNcQbDH4wtNGQxnvmBXw78Yi7w2fRqr9k-XzziMtHJj-ZhElnbI1kIR2Lje-vyVTslq6Nz7GDGn4_RqXzliNKARQcZCXh7_Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc9565fe8c.mp4?token=VKCn7j4cMQyWWu3WGrP8htIup3U3xwHyXPjxuSLacZA7zDB5gZdbIWrOU0D9fP1JtY3tSd5rnuYGRA7n2BfsoPaq7X5I6BncekYbxTGqGfyksBC8ZSqAeT3LkYW0tyOD9rmG-NJtjHiAetqgYBdSI0depxiYxA03-pavjm8C_cZ3JGp-66NSVVVIMPbUA8bLd1OR7Vj-z32fvl9wQlv32hZTPBVZ1CLwFmg7wfobUpA_eJrDPj29dpNcQbDH4wtNGQxnvmBXw78Yi7w2fRqr9k-XzziMtHJj-ZhElnbI1kIR2Lje-vyVTslq6Nz7GDGn4_RqXzliNKARQcZCXh7_Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان عقیدتی سیاسی فراجا: در صورت حفظ یک جزء از قرآن کریم، اضافه خدمت سربازان بخشیده می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/680408" target="_blank">📅 22:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680406">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ایران فقط نیم ثانیه به خلبان جنگنده اف ۱۵ سرنگون شده آمریکا، فرصت هشدار داد
نیویورک تایمز:
🔹
در آوریل ۲۰۲۶، ایران یک فروند اف ۱۵ ایی آمریکایی را بر فراز جنوب ایران با یک موشک زمین به هوای دوش‌پرتاب سرنگون کرد.
🔹
به نظر می‌رسد ایران از با استفاده از پهپادها برای ارائه موقعیت مکانی، سرعت و جی پی اس  به فرماندهان ایرانی در هدف قرار دادن آن  جت کمک گرفت.
🔹
خدمه هواپیما قبل از اصابت به هواپیمای ۶۰ میلیون دلاری، تنها حدود نیم ثانیه فرصت هشدار داشتند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/680406" target="_blank">📅 22:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680405">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2wKvtFLLupv-aR8EVHitUPpRWpGiPiuu9JFZdyuNGVkhAgmA10lU7l91v4_YSiv1JxRNKekaqIGugnEAJlTOVVL5XNzBoW-tC1ql6M6XcpZfoMJkvbdf2ua41cc8EMBwM9YTq0KECLbCEVrqNBFolhYuXxZkkw1ESeMm33ReI6mplN327X4CXYB1tzCK6f9CM5Um618gqKaNnycmKe3MRHOn2rpx0jIOLiGB_MRUTWaEYo3RKLfkNujUAVuh1iludOQ-Sr-OHboc6ERPxCQWNtLLJwSFQDhROH5lPvc_sweKIXpQ_OriXSsSQmNmnB-kjcvFYzKMe3UeySY9GSQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از انفجار در منطقه بنی‌حیان در جنوب لبنان منتشر شده که تحت کنترل ارتش اسرائیل (IDF) قرار دارد
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/680405" target="_blank">📅 22:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680404">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd1944e2df.mp4?token=HMglYr3pTIUGR6iumiBLPGQGTVOHg5bGlDRU5gxBnpBfW_OhJoNehAGGtzosVj2R8Bh89CNNrMlbsvfFKKqOSiUwv4015w4_TFdeVaZsPmj82_YLxdYLl3viR1wQ7OxYm3We8-as9aN5UCkSwVcys5XdZKqCEadrLth2sy-vcBbXqceESqqlHp7m-xtBHlkBgpcab9VJwUOW4iWRSkxHS4k0o8Hx9Z00HMs8kEVd6kgFeAbPjlImIwFfFBTzg3ecqt6iN8oF9yOa0Kb12iYiv6qeUMMd_rQoSdNcrKSA_prWsfjTVGhj65JmgNNXsaW1FV0Tzhbvj9K7NlE_nseNWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd1944e2df.mp4?token=HMglYr3pTIUGR6iumiBLPGQGTVOHg5bGlDRU5gxBnpBfW_OhJoNehAGGtzosVj2R8Bh89CNNrMlbsvfFKKqOSiUwv4015w4_TFdeVaZsPmj82_YLxdYLl3viR1wQ7OxYm3We8-as9aN5UCkSwVcys5XdZKqCEadrLth2sy-vcBbXqceESqqlHp7m-xtBHlkBgpcab9VJwUOW4iWRSkxHS4k0o8Hx9Z00HMs8kEVd6kgFeAbPjlImIwFfFBTzg3ecqt6iN8oF9yOa0Kb12iYiv6qeUMMd_rQoSdNcrKSA_prWsfjTVGhj65JmgNNXsaW1FV0Tzhbvj9K7NlE_nseNWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در سالروز شهادت پیامبر(ص) مدینه سیاه‌پوش نمی‌شود
🔹
هم‌زمان با سالروز شهادت پیامبر اکرم(ص)، مسجدالنبی مملو از زائرانی از سراسر جهان است؛ اما در مدینه خبری از مراسم عمومی سوگواری، نوحه‌خوانی و سیاه‌پوش‌شدن اماکن نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/680404" target="_blank">📅 22:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680403">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
زلنسکی: برای خاتمه جنگ با روسیه طرحی ارائه کرده‌ایم
رئیس‌جمهور اوکراین:
🔹
پیشنهادهایی را برای طرحی با هدف پایان دادن به جنگ با روسیه به مذاکره کنندگان آمریکایی ارائه داده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/680403" target="_blank">📅 22:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680402">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jklkQvmSAzAJ4JRY32MPL1ZojZr1T6E-yi-3ruD21nr5IDlOM87QL6pkN8GRbeYc19jwet4or9T9AaX73JnhWI68jVMGl5ykvPs_y5bRRzsHCCl0lZpzKYgkJjTCR4JoaT1uNXsmM2Ff91dLXemUw50Pd6cGUEbuscQZt6qqakeYBgFfBSZR88dU9pzdful3Bj8NUi2qJFdyK7BZmPpLsHXjILl_kNXmSknzuvniFpJGBFHr8MFtsmQGplU-0riO88R4JZrc08UwIaKPMKzoHq5zqubOgefTuJl0qmrfP4mlsimZIVnwUUtab7GE_CgdTP_lNl4X4LOMRRHFukSrUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صبر فقط تحمل سختی نیست؛ گاهی یعنی ایستادگی در برابر چیزی که دوستش داری
🔹
امام علی(ع) در حکمت ۵۵ نهج‌البلاغه، صبر را دو گونه معرفی می‌کند: صبر بر آنچه انسان از آن ناخشنود است و صبر در برابر چیزی که به آن میل دارد. گاهی دشوارترین صبر، نه تحمل رنج، بلکه کنترل…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/680402" target="_blank">📅 22:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680401">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
شرط سنگین رامین برای پیوستن به فولاد
🔹
طی ساعات اخیر شایعاتی درباره پیوستن رامین رضاییان به فولاد خوزستان مطرح شده اما پیگیری‌ها نشان می‌دهد که این بازیکن هنوز قراردادی با باشگاه خوزستانی به امضا نرسانده است.
🔹
رضاییان در مذاکراتی که با مسئولان باشگاه فولاد خوزستان داشته، خواستار قراردادی به ارزش ۲۰۰ میلیارد تومان شده. رقمی که مورد موافقت باشگاه فولاد قرار نگرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/680401" target="_blank">📅 22:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680400">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/badcdc31e6.mp4?token=G-stGWTJlHvxCRU7gvqFj6NHBWSwPZdcx7eMGleI1ptQNcqKLRGTNVZLndy4JreWIux2g_s_teDleJl8G4HcWrC76lC2veex63hIBIh5s-8sB5sv0TtbFmrUrhfJggQcXdw7F1hRm5zYikP1iFD8LVL5lmCM6TtvWXfgweCPUacazh2OL6uwpiBPDNs4AaeD-p9W7H6sXzefQTOUYa_1lPDJV4ez_r0u0Idnfz1laomKKW1GZCwHYOMYPtMelM6dMPHacm_WdzyBdGSf0LU-nbDLN7muZ3FOT1LYU2qoglCM_cEBVCHQnSgKA_tq0R-HgBz6KG7HcWb3cg4R3nUazA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/badcdc31e6.mp4?token=G-stGWTJlHvxCRU7gvqFj6NHBWSwPZdcx7eMGleI1ptQNcqKLRGTNVZLndy4JreWIux2g_s_teDleJl8G4HcWrC76lC2veex63hIBIh5s-8sB5sv0TtbFmrUrhfJggQcXdw7F1hRm5zYikP1iFD8LVL5lmCM6TtvWXfgweCPUacazh2OL6uwpiBPDNs4AaeD-p9W7H6sXzefQTOUYa_1lPDJV4ez_r0u0Idnfz1laomKKW1GZCwHYOMYPtMelM6dMPHacm_WdzyBdGSf0LU-nbDLN7muZ3FOT1LYU2qoglCM_cEBVCHQnSgKA_tq0R-HgBz6KG7HcWb3cg4R3nUazA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان و سیل شدید در استان ژجیانگ در شرق چین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/680400" target="_blank">📅 21:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680399">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e120af53ce.mp4?token=BVgtLO_4lObQteagdJ1vQBv99JzL9n0W0NhaLTPWdhYI-9JdSFExeFhB88Lj8Vz9vuKYdwvVA1m7pGOA2bKySkvrxeBHIoaDk-TmQBC6jrWE_CYRu9COkJsdIXyfVnJ0YNxfhsd-S-aWVnJX_gcVd5xdF7UN7AQdJ_5p5U9C2YbyADiLLOzgc7ah9quX-igPYRkkvZ3_HcAXn_eg1SdLA5SyIGWkeVbAZzZlfgQzEdn2UUdY5z59oP7zjDThIaiwAQ41OUHmZoFc8nxSR6AEk76TBv4s0WAYMhWJFXfEXzWJvIK45-g4p-BEdid9he3n8iJHn03llfFWr7cELmIVvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e120af53ce.mp4?token=BVgtLO_4lObQteagdJ1vQBv99JzL9n0W0NhaLTPWdhYI-9JdSFExeFhB88Lj8Vz9vuKYdwvVA1m7pGOA2bKySkvrxeBHIoaDk-TmQBC6jrWE_CYRu9COkJsdIXyfVnJ0YNxfhsd-S-aWVnJX_gcVd5xdF7UN7AQdJ_5p5U9C2YbyADiLLOzgc7ah9quX-igPYRkkvZ3_HcAXn_eg1SdLA5SyIGWkeVbAZzZlfgQzEdn2UUdY5z59oP7zjDThIaiwAQ41OUHmZoFc8nxSR6AEk76TBv4s0WAYMhWJFXfEXzWJvIK45-g4p-BEdid9he3n8iJHn03llfFWr7cELmIVvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبر تکمیلی گروگانگیری
🔹
در ادامه این عملیات، پس از رهایی فرد گروگان، مذاکرات با گروگانگیر در دستور کار تیم تخصصی رهایی گروگان قرار گرفت. نیروهای تخصصی نزدیک به دو ساعت با این فرد مذاکره کردند و تلاش شد وی بدون درگیری خود را تسلیم کند.
🔹
در ادامه، زمانی که…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/680399" target="_blank">📅 21:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680398">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlO0kYrZdBudTzU2pZ1iBDoejnO0vAVt75vSywgl0WLzVOhQ-MC6EIq93RgWOa8K7O0d5qPkRNslnNJZMC3s7_9q1gvgmbOU-zn4fO20hv0jHAS3LTaxHGcdlZVQ16EklLEy9TY1IbSrNbwgmsJDrG9-nosyRIS3uPH2RMselt_KBe0uCnYTIH8yMoGHVredvxpMe815jHrTyOcJQ7Ma46K7cUiyviroVM6M771T1qj5ea104DWMSB944zHBrLpvxWzish_ILGCxYrIe0Paah56LGn4wq5r8Ags_j5c2j5DkvpzsYBykYKMS9mMp1QlvZwoCQOPOCrDbcfS0blr2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آموزش آنلاین، رکورد قبولی تیزهوشان را زد
🔹
آمار قبولی‌های مدارس استعدادهای درخشان نشان می‌دهد دانش‌آموزان تام‌لند در آزمون‌های ورودی پایه‌های ششم و نهم، بیشترین تعداد قبولی را به خود اختصاص داده‌اند؛ آماری که از حضور پررنگ دانش‌آموزان این پلتفرم در میان پذیرفته‌شدگان مدارس تیزهوشان حکایت دارد.
🔹
تام‌لند به‌عنوان یک پلتفرم آموزش آنلاین، امکان دسترسی دانش‌آموزان به آموزش‌های تخصصی را از طریق اینترنت فراهم کرده است و نتایج آزمون‌های امسال، از موفقیت گسترده دانش‌آموزان این مجموعه در مسیر ورود به مدارس استعدادهای درخشان خبر می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/680398" target="_blank">📅 21:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680397">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08b561de50.mp4?token=GqEfnug59RcdMPiwHlmzorblcnHnllIGtHs440pajJsTDCqxFpYrCdBJA8-2wmm6dJTaF6yClvonV3Zt4lipmuhPp3FwyJHnpD6ToQ-1DlassJX_J53ITVdPVmD9T863DKtU47bE3F20awWDaVrkDLnDR8FpFB3WQOltfjiUmwoEShtmA45p-z9NBOI2ToFQnP4S5N9SkMXn34-IgZ9esRoGR3rukj1bp3e_ZQYpOVQ56GOyOuzC7jqWwSYqNUt3tCW8a6MhJ559DZ0qaiB_yyXAL2P5_cfe7-ymVU_Szw_PiA-W96lcbu25ezirv5vvbnL82pPypJz6bPUgT6j-_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08b561de50.mp4?token=GqEfnug59RcdMPiwHlmzorblcnHnllIGtHs440pajJsTDCqxFpYrCdBJA8-2wmm6dJTaF6yClvonV3Zt4lipmuhPp3FwyJHnpD6ToQ-1DlassJX_J53ITVdPVmD9T863DKtU47bE3F20awWDaVrkDLnDR8FpFB3WQOltfjiUmwoEShtmA45p-z9NBOI2ToFQnP4S5N9SkMXn34-IgZ9esRoGR3rukj1bp3e_ZQYpOVQ56GOyOuzC7jqWwSYqNUt3tCW8a6MhJ559DZ0qaiB_yyXAL2P5_cfe7-ymVU_Szw_PiA-W96lcbu25ezirv5vvbnL82pPypJz6bPUgT6j-_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: بر تعمیق روابط با پاکستان در همه زمینه‌ها تاکید داریم   رئیس‌جمهوری در دیدار وزیر کشور پاکستان:
🔹
اهتمام مقامات پاکستان برای همبستگی و تقویت روابط و مناسبات با ایران ارزشمند است
🔹
بر تعمیق روابط با پاکستان در همه زمینه‌ها تاکید داریم
🔹
وزیر کشور پاکستان:…</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/680397" target="_blank">📅 21:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680396">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
یمن خطاب به سعودی: به‌جای گریه و زاری، محاصره ظالمانه علیه مردم یمن را متوقف کنید
عمر البخیتی، سخنگوی دولت تغییر و سازندگی یمن:
🔹
ارتش یمن در اعمال ممنوعیت تردد بر کشتیرانی سعودی کاملاً جدی است و این موضع غیرقابل بازگشت است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/680396" target="_blank">📅 21:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680395">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در پالایشگاه نفت الزاویه در پی حمله پهپادی ناشناس
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/680395" target="_blank">📅 21:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680394">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
حمله یمن به کشتی حامل تجهیزات نظامی در باب المندب
🔹
منابع یمنی خبر دادند این کشتی تجهیزات نظامی متعلق به عربستان سعودی بوده که هدف حمله قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/680394" target="_blank">📅 21:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680393">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRPVpJchX7_-ndHYyNFnMNDaeiDFfJ9SL0iSIJSWRhvZgPnqeKUIprQ-MXc0Qt1p1Ek1V6W5L6RRYohRo7zdNTEpaVtYq4QurT1HbvxCMdCaPAtwhJnHvzJfYL0cAc1MWEwhUbVfUs2HEyKM_XgJgiCuJpyqjDEeVrMZXuZZMUD2widiJjCtbiygigtfy0G7icT4mkrW68t6FqU60E0a5TKEC1SQ1jKeWHPph8OMdajxZQEZKQ45Wc0yVNIwFaXboSIVEgDDgBw-9tixG3RR-9n3J5MqAPbWAC4isrJQG7qLMxS7yZObEbCdDVse-aKBIGyy7Uf27ZwEIfygBCTuEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/680393" target="_blank">📅 21:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680392">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf53473d10.mp4?token=XSzVfKjWuSZDrupirnmg0Z5PlExXlbFHQ5GTTYFG0RVdB5hd0JQ529KDEvpuaxzWSudcIKIDSvmxvJ92riyDOTz0zZcZaKAfRTZlT0Jg0lN81QPdnaQgs1bihPLQ1pC-EG5IP07U68oTujIat_eHXmpWbTWPQmVLjcrIA9ot9o0oxT5lHsriYOiNxnqTq39B_OcJSg_azYh8r-3X-gDWqBhVHEX-7fiW1rz1phYDjudiCMO_NQQTJlhMfWE39ciOJfdJs0dQU8fi-5VHf2xrIqc-eyoLweqYldawHqF1u_CjLV1CKNrk9Sq7NHdvzNDOU1_kvCEMB1T-FNBntac3Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf53473d10.mp4?token=XSzVfKjWuSZDrupirnmg0Z5PlExXlbFHQ5GTTYFG0RVdB5hd0JQ529KDEvpuaxzWSudcIKIDSvmxvJ92riyDOTz0zZcZaKAfRTZlT0Jg0lN81QPdnaQgs1bihPLQ1pC-EG5IP07U68oTujIat_eHXmpWbTWPQmVLjcrIA9ot9o0oxT5lHsriYOiNxnqTq39B_OcJSg_azYh8r-3X-gDWqBhVHEX-7fiW1rz1phYDjudiCMO_NQQTJlhMfWE39ciOJfdJs0dQU8fi-5VHf2xrIqc-eyoLweqYldawHqF1u_CjLV1CKNrk9Sq7NHdvzNDOU1_kvCEMB1T-FNBntac3Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی سلامی گوشی را دست معاون رئیس‌جمهور داد و مشکل یک چوپان را پیگیری کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/680392" target="_blank">📅 21:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680391">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
روایت نیویورک‌تایمز از نحوه انطباق حملات ایران با تاکتیک‌های جنگی آمریکا
🔹
نیویورک‌تایمز نوشته حملات ایران که منجر به کشته‌شدن سه سرباز آمریکایی در اردن شد، نشان می‌دهد که هم‌زمان با رو به اتمام رفتن موشک‌های رهگیر پنتاگون، مهارت‌های جنگی ایران با چه سرعتی ارتقا یافته است.
🔹
این روزنامه نوشته ایران با ادامه جنگ علیه ایالات متحده به دشمنی ماهرتر تبدیل شده و یاد گرفته است که چگونه هم‌زمان با گسترش میدان نبرد به اکثر نقاط خاورمیانه، از پدافند هوایی آمریکا بگریزد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/680391" target="_blank">📅 21:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680390">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWP51GiyobBmkXSwu3818zo0IXruRu7IeF_LxLY4MJCBqiyQQt4UUJJJ8IIg2hFgP7Vu9LbfnsFFMWCpgi7wMSv2UpnrZyhk8TGQNcCeTiyNh5ZJlOe8GxLv0wvAfnOpva258piNoXRTDw4GaJfKxh9Umt364uZgH0DlzHIe8Vwo30zh782YVayhtJTTQtcvwRzttHrpbj82mQVVyPR3Uz3gAFOmMZOBE4CwoW8U0Sglpbm7xKR3zDez37v-1nmmjoLCDclYmJHKdHplhp-TG2mH7QrLeRKzYBtEcezhlSXFfjvKkOpU08ew3afjAaWT14dhhC7G1aVf_a5faNthzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برخی منابع از وقوع ۲ انفجار مجدد در مواضع مزدوران سعودی در مأرب یمن خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/680390" target="_blank">📅 21:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680389">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMWi65xW8nDPG3LVWACd_hicXnl0pSk7cTQYSxznTm7WfUbWuRRmia1DFl_lCb3fThqYHoYqMfEAixEf2y2P2gh7hws18D3QDR7TJpfYZP1r9jFaemeUGyslHUDnlyuWrYXvE_yTLZj-V2Vz_XAKumGnjqmbpZfQOQrx2yqD8EbYsRzxqiXABoZruiPDGOC3e7O3_3rwMQH0oxRaQ2VfkyU0bK5QSTD1lEvruexGrwSwq3zME5WYgn_EBpYwM8-5rHVhEnnmv2KN1QwT__ky7pGXeXBjG7q2c4Z-v-uJAS2MLafNmKSiAYnlNXWYQo6bhpgJ0PcV5wND5hU6IZgQ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیتی از ادعای مبنی بر اینکه
جت سلطنتی امارات امروز صبح به تهران سر زد و بعد از ۱ ساعت ماندن، برگشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/680389" target="_blank">📅 21:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680388">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
تعداد کشته‌های زلزلهٔ کلمبیا به ۲۲۴ نفر رسید
🔹
تعداد کشته‌شدگان زلزلهٔ ۷.۴ ریشتری دیروز در کلمبیا به ۲۲۴ نفر رسیده است. کلمبیا این زمین‌لرزه را «فاجعهٔ ملی» اعلام کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/680388" target="_blank">📅 21:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680384">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gIedKX-VQZRPcfwnAhw0MLAkDQdvSdriS712corFRh6tEk_vlXOYbjxHua1VH-7M28Z3XnRj9g3S4ZsVhU6hJe4s0oIKbSppNa_5ZR2BgQAXi1EkUWgGq_15tM5VCZN9-sv-EY1bXVZsg20hgcJLjxwTfoYx6VtxKFbn3oSnpjxP516SA4CznPE4UrTT2G08vhEFt-zurKbTNhU5hcM5pw8ze5EiO21Av3RaZzyczhMitdhT9FHL-Bb7Iz032Frbixpd_v0-BxCw7xx5a-rdEGe4Namp2-i6VA2zri4lXuVpoq3IMcVH38TJYPCUYOKngx3RYJ4h-npjuUJNc1RgwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rpGNOYrUI3TV-Cs_jmm7deYprTIm-aw3qULm5d_0cdEBLxASe4sqo37OFaZah8jDk2s8Q9oR0lKmK7wwbLTQE140xz7k4PmC9knCOsJoU1bW5ptfrg4Dy-f74b2sL1G7pRyxkMcthFbVjzKwflFsZA52gF9zRjfJOpAIQUU8uLxlRQRGTofvYNq0zSaNaVAyKi092f-bZjxqH72ZfyeEIghxc9gXEPzkNIr0EYhHUZoOrx-jSPD3T5aPTN2k5U414ZsZSrC5M87OupQlQi_uQD7DT4OFDHX-2mBmD3TF1-ZiK_10zOz2C2pFMWj3Dpf0g-1YEg-ZOYr-VbHIh5Xqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tFY0tMYaJj8WgxJvD1ILFXtxaYUumpLvMaE56jWQ3gORy6wlgzlnogByascjhNf-zMf29ICPZ1MigGWuFw7C88S2RyDs3SEd2XHBfaEYV2yPdlwQ34TqddzZ6d0cvMbAAUjXCBaaRnRMNXb49LQouFTDg2yHBbNcsAJZt_zG0JsrW5kF4k-thdPzVObketezmunWPN4Yf_q3Nr4VwpnGeDujx0DQEfcg8gWG0meEXXGsykFQjaX1Vaw6ky8_mwCz0P48qJ2spON9fB8-zYQC651hPxShpRw3wngek81_Pemj3EGnzJEqMYSgyvEaNq08wlN0x-Fo2snRzN6xQBW2Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vM01Djdtu3AI1sFDCezcG3GD6VeOz8nK29oy-tnFcumwQZ0amlfXlO3ywhUlxv9ab7QMXsdglSVlnxCUv_jpVilq4xyqJfsn8PTNhg3lo-pVQWiWwBO04o4g8hdXZBVG-8-ZXis431fntx5MYbTPfoIe8fiOsHaAfHdutWJXaedNHaE0QxoocBD9HJNhblG6tmbPl4jZp5gdw1s77ed8jHm4ZKlNS9JYPpbSihTBlgybkZ7z4qyOTloI63rAhNtguAcvZaIHwFK9VbTtn_MRdfcOkq4lsv-eZhQzvVeR37vRsAHXBY4LzxxBGmcp-7VCP1jO3dvX07L2DLClxoW9aA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/680384" target="_blank">📅 21:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680379">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LksJWJORMcrPZm7p_DNMYEExqw_zytqqT3IIc1G6-BD6-6gBpQJMQNlGeTwlDlveP9rKKOvZ7y0CuPEd2coLIai7T_mdJylFA0b-0ixrfhONq-YJRL7PNOYq4vzOY-GFBoPCGYnp4wMIFEQ5dqfmhPd3JANuMyJxNlAQd-A307lj2sWwDft87Xx9IuRnZNUIxj35Z2oHQO-1DnF3eJzNkBDe3tXjtMOMJXUVzEah9QcSRXTDV57T_kmvbiDri6I1UedQJlAOxBFrm7QJPRA4BXq9P4zgyD0-SYYqNEkGe5-qYuPV804tpKBtkg56rc9BwNyuRiNkxo1omGtM25QZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبی که ماه کامل شد
🔹
کارگردان: نرگس آبیار
🔹
ژانر: درام، عاشقانه، جنایی، مهیج
🔹
بازیگران: الناز شاکردوست، هوتن شکیبا، شبنم مقدمی، پدرام شریفی و…
🔹
خلاصه داستان: فائزه، دختری جوان از جنوب تهران، عاشق عبدالحمید می‌شود؛ عشقی که در ابتدا آرام و ساده به نظر می‌رسد،…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/680379" target="_blank">📅 21:02 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
