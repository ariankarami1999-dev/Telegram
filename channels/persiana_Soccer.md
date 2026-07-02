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
<img src="https://cdn4.telesco.pe/file/F1dfKESAjAemtbSeg455lqDthi_uu8Sv7zOHVzes2MYBco25llZ6V52_JhjEBXRbxIH-ExbRFAYpNg_RzzYorGzVPPW5fqdXNgz_WrIcUKUEKDqfKF1Jx2PTGnsmt7cmis3qD71IFCaqI3JTjKgatYhu3rrWsjXFV0QFpUwNnnlqOfTS3OpeukYbaHpRgGJ4qx6M8gC5BDbu74k7i1FfNVc97SyiaXn8xz6K1llL3eiNbGZ08yVa3V2v7IvvRrc5UQgaWATUjlfWadVydeXIvhnVn4T5P28iNlUS0c0oOtS9VFyIszuDKdbTzE8YOthZa-I1AjQ9OY0a99_fzlEUbQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 359K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 13:10:54</div>
<hr>

<div class="tg-post" id="msg-24804">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=otiOJRiz9Sswf40YAiP8eJJLk1-BVE2oSADagtMXJ_n4VPV4kDvjhP3Uj9BYhfK2xsAqfDLKadgAaJ0fztxVcQrMZv1779u2nW5yBCnIGPZYCZ1QLaDtjroshAmqBRqSu_9bg9xPxaDOWASODuuA8AEWT14QfA8KKpceWmcHBs2t909ag1tpHuoz-KJDdHGcEE_7KU9dkeGv1KRPx29lZriFhaLyBRxzdN2g-hVoAhWZvm9HLjaT4OxxX1ysMlgUkXXXcq8x8QEgBr6qthzg2Fvll9QiwRL0R7J1h0JI6B_C0kQaSj-HjYAo2eLLoyMSz4eAoDkk2OrXz6ypnYL0gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=otiOJRiz9Sswf40YAiP8eJJLk1-BVE2oSADagtMXJ_n4VPV4kDvjhP3Uj9BYhfK2xsAqfDLKadgAaJ0fztxVcQrMZv1779u2nW5yBCnIGPZYCZ1QLaDtjroshAmqBRqSu_9bg9xPxaDOWASODuuA8AEWT14QfA8KKpceWmcHBs2t909ag1tpHuoz-KJDdHGcEE_7KU9dkeGv1KRPx29lZriFhaLyBRxzdN2g-hVoAhWZvm9HLjaT4OxxX1ysMlgUkXXXcq8x8QEgBr6qthzg2Fvll9QiwRL0R7J1h0JI6B_C0kQaSj-HjYAo2eLLoyMSz4eAoDkk2OrXz6ypnYL0gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/24804" target="_blank">📅 11:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24803">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyrSigv_HDdjmkwuaLRJVFhZ5nThInxClJe1K1IZm9STjtV0ICfsT6dheX-cSVcBGuirIVJZ6GVDhlE7sNzifCtOeEJjgihueFXShiBKSoFy0Fy7vPQlY26TkxVeiI8w9I-Dfs7FLtWA-Ea8POxDx0PVyr6lzyMWG_Xd7FdSSYspdXzIEJSArEeKJt3o441ZWI9DWph2g8EXLaCtXrI6HCwr8VEm1Vh0k1PReBU8ZnzWa0lmXMXIAlOQBSpFLJBjN5dN8wYXBDZxWvBJfOILqNAgcnKvvaJSUhkZtKuSLtkMKbyrcsVgpnoI5UW399otOzZoyOlR0eHiAkMHLHOKaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
ظرف‌چهار پنج روزگذشته بارها اعلام کار انتقال دراگان‌اسکوچیچ به‌باشگاه پرسپولیس نهایی و تمام شده و فقط‌پوستر رونمایی و اعلام‌خبررسمی آن توسط باشگاه باقی مونده اما یه عده تکذیب میکنند اماامروز خبرمیزنن‌که اسکوچیچ سرمربی پرسپولیس شد. زمستون هم بعنوان اولین…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/24803" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24802">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=vjq8zW-Nozhl1HL4pDUMCkVko4oHoLRUo7IiDK_G9AN599Hv5GEX2WjdyYSnorcAI6hHeBGZKzx9uw-M55xdVipGRj8bIBXOGOoz2wCAJSIck6GJ4Byx7WGeRCel7laXtNcSnguiFfVqaqY50OD5RcQn-973rurESKBo3y6UFxoq-Cz3BfKJ4bpA-QJuNS1H-QDB2zSqR_97uYQkWVLgt7hJYy6Q6LptPZV-Jytii7ELoKGjcS650xrCdIkGePo7IY2xkwtGnQYF6GyzfpVxFfm8S-FtGbuzQMkqpBxi6UuaSdKNkKTyOY470BeIbec-qISgxC_RSGGDQAspCIOBTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=vjq8zW-Nozhl1HL4pDUMCkVko4oHoLRUo7IiDK_G9AN599Hv5GEX2WjdyYSnorcAI6hHeBGZKzx9uw-M55xdVipGRj8bIBXOGOoz2wCAJSIck6GJ4Byx7WGeRCel7laXtNcSnguiFfVqaqY50OD5RcQn-973rurESKBo3y6UFxoq-Cz3BfKJ4bpA-QJuNS1H-QDB2zSqR_97uYQkWVLgt7hJYy6Q6LptPZV-Jytii7ELoKGjcS650xrCdIkGePo7IY2xkwtGnQYF6GyzfpVxFfm8S-FtGbuzQMkqpBxi6UuaSdKNkKTyOY470BeIbec-qISgxC_RSGGDQAspCIOBTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
آقای تونی‌کروس عزیز؛ مگه تو چند نفر بودی که بعداز رفتنت نه آلمان روز خوش دید نه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/24802" target="_blank">📅 08:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24801">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8EgLi-0D4KBTNr5nWn3i-qkuCwLCkCcOa_5PHDqe0r3IBu9YKr9Kk5kSglZphEvYgB3bkAfqlGMrQtxpP8ERgSYxtvBbUY8JxZQ1Kufw5r-Ek18FynpI4poH-T4rdLbk3tKYvOU__AnZTgAb6Cyet6PuZ2NhcOcAtwJ5zHoaMw9N5xkb-QVknndpq85yRshitYkru7RjGFg8T7TQZhJuaHOhobxejCfqUB66D4HI-xwnDtrWBdJUFZFRkTUbU4gpMnwzcIA_n010V1KfmJ5Seq03M0qFZv0IOMZ6iz1b0XJ1W4WPP85TS9N8kW0akH_0nN3qAZssloF8AINcEzY2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان چهارمین روز مرحله یک‌شانزدهم نهایی؛ آمریکا هم با شکست دوگله بوسنی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/24801" target="_blank">📅 08:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24800">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVx4mGPuQ6VLm0fXVPxMijLd_LwjXpEJyYT_do0MqmMrJiXguyrs8fuZjH7I61zm-rS1juiqxN702lSguJxRvzPovimALRSgj3V4MOxmjxx2QCxTxslm59wuOBhieD19Sr9P9cfe-ydscVtY8_WMEm6YcL66R4KBGWj2zXn9m6v6hH35ofi3MxQuCy2FjhluLQZg_Eec1iBzcEjXmBm8_NcFsu7KrKiz6DUARjmkQHLOzUe82owl8sprFL75S4NZAmQ0SN5nS9Mf2Ak1taHrXGcSum1l0fQqlFfoDzfia8U0QMcKl69T8AaywnMwiVQSGOqfYYrRDgFbIioHNkSvKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله ⅛ نهایی جام جهانی که در حال تکمیله؛ بازی‌ها داره مرحله‌به‌مرحله جذاب‌تر میشه.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/24800" target="_blank">📅 08:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24799">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-_YS1f924PRXZJMro_kvNM9NpVdoJpgux0C5Z7PzxR0Ri9jKM2KFTjEsj-Ga-gPVlIzqCW3DB2lpT1e_AoBuOjui2xz6cfPJNxMsFBGZcqwo608DDkpXYgJcoEO7R3zljoqoW_LlOohw6imzm6TNKJGxLYNlWgmLvKQyoWSdwTjmQdh41MYbWEEof2BX79PLfrzZ21kAIJiA2cvXJiJDSWgQL1ZcXqXcKlN2VqNZl4wTT1eOLxfrzZtEB-gh4bzccnSCbwmBB8XJnuEUdGGRdyFzd2qz_7jCp5Vn6JOrZVsdLc2gQFztjDMxITEwH2dW8EldywsOgNtqZyNUzsx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24799" target="_blank">📅 02:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24797">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=TmkWmg97gcR9lvLMj8nOZrffaIoqXC1YzWQJR8e5uBnyDCtgqcp3oV9c12nJI61z71pzEgkszKhC03DTbYV-wjIbz4HH3MPY2lL9R0SAhpPXtTEPgBLnaLTpfjnA5XdpTX0DB8MaRhIsM7NfKqyotQMH7Ux8rGGZDhhr6aB0eFrIpIT8ET70nT_Qcbf2ZFEmkWvyXzWNg0Jv1k06qYx-gseIJGMa0WK12GjK8XapEROslpYVmxqnYp6Aa7XmNHpx_pSyBJuWnQUAepbKEw0PrGNn0oh7vwmW_jPQrCbNfQ7Fehu8b9QzMfiNbR2fZ1X6nPhBZLalBhYVxqY7W5_3LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=TmkWmg97gcR9lvLMj8nOZrffaIoqXC1YzWQJR8e5uBnyDCtgqcp3oV9c12nJI61z71pzEgkszKhC03DTbYV-wjIbz4HH3MPY2lL9R0SAhpPXtTEPgBLnaLTpfjnA5XdpTX0DB8MaRhIsM7NfKqyotQMH7Ux8rGGZDhhr6aB0eFrIpIT8ET70nT_Qcbf2ZFEmkWvyXzWNg0Jv1k06qYx-gseIJGMa0WK12GjK8XapEROslpYVmxqnYp6Aa7XmNHpx_pSyBJuWnQUAepbKEw0PrGNn0oh7vwmW_jPQrCbNfQ7Fehu8b9QzMfiNbR2fZ1X6nPhBZLalBhYVxqY7W5_3LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/24797" target="_blank">📅 02:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24796">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIokwPS7kSuo16nvDGQjCT8HwY7-vuHGJPnnMe5awpEqLrQjZKZ1pR4gU3AlCQmXJ6e8qH4J1wi4m0Fd2mz4iMdmXr5AIRxoBY_hrGNozCr8JZZRmkMOS5Qs-HscDJ18BuoZO5biNT9Qs0CAFwqhZkyQr101qX6m9945blee6xSzHXkzw1YQmLBT5n1Q3TDg5q6Z499NJAr1b1GX-_HBQMZemFCHEoh05YMUa21cdcXKqTBFvBuHw-QVR2ikkw7-8NqmCVkOPH2NOEJ2ZgYgtMIuSfmSbJQcpltrJni96YD4_AlUGfhBij0UaZUWhqYHCYsv8xPnDRPNL_fkBTeQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم نهایی جام جهانی؛ صعود سخت و دراماتیک شیاطین‌سرخ‌اروپا مقابل یاران سادیو مانه در سنگال؛ بلژیک به معنای واقعی کلمه مرد تا برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/24796" target="_blank">📅 02:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24794">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9G5DZyrdAlP_F7Qt4sNiZqHS0O0V4PfN-Rnb6mF9vfvfaiZMmeVew4CETXb2k8_fNP_x58RBNse5-01RqiuYAnM8hiHIXLjr45wcqXWRDfJf051ff8cIkfTy614Vyf4eoMpHTSM_HB6CjHghz5VTbfeQb6m8R9aM-6NbqPD32L-ajiC8rI199_nHKcLxZOb0_EbvC4q3ZXVXc1zwaJ4za_nZqbbjS-xxCatRRwRmv-vXE_riDngg5abjhlxebzPXqXKpYh8HBS4RQwsbt9WJXv3wohiP0cehVMtugRZ5BraWzfH3gZT37Y_jGXzSPmr0MVlWalof2oHPjKGfgIrrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/24794" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24793">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDAupG5wP883gbffodbhRc-GQ0FH0mSn3xPxNLDvPWdPsg9K1R8cZq88dgcDPtowwUQeNy69j5d00RPW6XQZivELgOpl-2-tzPdkAP1RRj8W6BBYOBpyKnoPVWZHcMyjjSxQgr7hOyWiU1p-bOwuwWF2y32jO5iak375EDogaDCzbwFNiJ7LTQMQPYPBAPtG5tN8s1QNn7XOkTA7J_oOmnvwBJF3kTXKIGiK3EBlLspxGoOkrbteIc5rXchGIIfjjrUuidAtPbIkBzu4DFQMJ322a9q321I4cIlPyZfpFTadCLaEuIRR7IGanz58sogTkcdTRkeyibUC2NSzKLVyGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از درخشش‌ادامه‌دار امباپه درفرانسه تاصعود دشوار انگلیس و بلژیک به دور بعد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/24793" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24792">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXFVjwGllAuGsrL3myMggUX3ZmcurWFNU-7yfEMnX5ihxY10Ns0xobHzclhWBHY-71huCcyz9yVnqyKTS3lJsE2Tu0LPskq7FLgtnwZwFJ2GoLZX_1NC9ESAa9FF5q6s6ua-AKmrtuX_oA6c0IwIcI6vRj5CRxgu9d8TiMdZcVcNPDZIe7h7swYSAyP21qhIbrj2X--J1IS4i-oKICNf222Exb4FH16Ha9BBaTZiTVZlMZXfUYg4Mt07VjLQleyck18mBPwi7nVgtMvOYiXWFRmFJ5LemJhfZEeaIx-7PmV1KfhOHkAOr0kvgha2R10riUYzOPH6ODiGBPfQWPh14A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
باهر1میلیون‌
🅰️
🅰️
🅰️
هزارشارژ اضافی بگیر
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی بگیر
🤩
🤩
🅰️
کش بک بابت هر باخت
✅
این بونوس ها بدون
#قیدو
شرط و نامحدود هست
.
💵
با بت اینجا همیشه به سمت سود حرکت کن
🔼
⌛
پشتیبانی 24 ساعته
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a10
@betinjabet</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/24792" target="_blank">📅 02:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24791">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uf_vswQvMJfRyR2Lqtfoqhtx1vD1JXju9dtXoIF0l4XZTRp9efh-7-3yqjo3f9XFQpe8luLrPoF7l1-9_MdwN3KL2978FfQwFD_pwbnejfl6KmxyzNxDNZGwGTFYamaTfkjxflPIlML6mikr45gBcIMdqxsE_s4bIBCi2AWzLVRPE6sV6TpRW0OeRj89RBf9nIZq7J2El5n-CFchrubhVibCkJd_B3tcp8lyEVC3jJMtWMPguBF81_UlPQpSbUb2LeodhN4lxvqpLrrRXBIK_GqEKwjbkWRMwpNhmjIHDyh0DU3PA_xn_CF6dxa8VtD6BhXoqClu05Rf6ICh-6Xwog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عامل‌اصلی‌کامبک‌زدن‌بلژیک و مساوی کردن بازی برابرسنگال رو میتونید در تصویر مشاهده کنید. باید ببینیم در وقت‌های اضافه بازم به بلژبک کمک میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/24791" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24790">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBQbv9sAN2GxVTbqNtjx2zgbGo-sKGGvgVRByH5pHR6jNHtDHnHIagraAIKmAauas7fWRstL83weFDEWuzN6yvCY7A1lFLpGE6DHKtn3_qL8R5MIUgSZ6rLOFdKmKB8-fuCZ66Mqe0ry_dO-9CoypJU7Vv2cJJ8fMdtrD4eeG8V5Q_qF24LpXnXJgrfLGCTYm4wd046MByK9TH3LtuRGKlTH2fSz8cALm4ScXrCL3EcaJkESevBJcILdPkgAUIsY1hTSlZoBUruCfnWCOVPeMajg2_RZbgZCKUXCJ4e7wlbskfpUbfWQKwgQArD25_k-btcH5IgQJeZGUSaf7Hs9Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
میزبانی بی‌نقص و خیره‌کننده مکزیک دررقابت های جام‌جهانی 2026؛ سال بعد همین موقع‌ها خبر میاد که جمعیت مکزیک دریک‌سال گذشته چند صد هزار نفر افزایش یافته است. اوضاع خیلی خیطه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24790" target="_blank">📅 01:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24789">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7ul91UFSyINwoTYKKR5X1u9p-HsjLjVA8k6bJVaj7tq8cF6wH7d3J7YCGCIeGOMxU_0hCEzwh0qPwKoIlpTg9vxZeGm0zR94P4KfkCqKQpLDKoYiCa9U67Z2XBNqu16FP3sf9l_sZrCZw7P7lxNagOxcTxOiZEWHSs8AhX4xgR9gkCBDNl3Nm9V_uqbVRlmY3oheLxg9fbJTZpCBBnZ5HjSjehI67plV0J2yZfssf4lsk447cG24Oy9feWTsObvAhLsrVIH0Gtc4B2fI4JYxF2Z8IF7hny2x5GZu_WZNiHGUAFFp9RdLJAXnmuV_FLsTHSWS2f5CPQY0WYxLExuug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعداز این‌پستی که زدیم گویا بلافاصله به غیرت بازیکنان بلژیک برخورده و در فاصله تنها سه دقیقه کامبک زدند و حالا بازی دو بر دو در جریان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24789" target="_blank">📅 01:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24788">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy8PnP7gG0nDb6HTT_pfu3WR-x2yOnuByrJzqUEdZznCPPz4mqLipQt1CE2rA04QvZ73u85TkCts5nrMxdV6LnAXj9fhjBcUL01hGcOnX1vNuVR6dj-pozWZ7CXXaSkORxBI2UlaUoqHyzOdIIrOpChWUsQW2cgktQS2HfYlvScyyVRDpgfLrlcY82l05WKk_h6AyXULOEJpWXDCRwNR-_rapAlneoIc1X-Sc5zgBHnx8KcEN5yb-sbO1gF7VLKFfIbJUT55DUykV4OXgfgjlmptpAx_2KLLYE6yKCAZ0F8vMrPcTzYv47XTLDR-wZtA6TolSiXSWvoHikfKjorqmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضع تیم‌ملی‌بلژیک رو می‌بینید؟ قلعه‌نویی داره از چی افتخار میسازه؟ از حذف‌شدن در «آسون‌ترین گروه‌ممکن». ‏سرگروهش‌هم‌درحد سید سه گروه‌های دیگه هم‌نبود.نیوزیلندیکی‌از ضعیف‌ترین تیم‌های کل جام. ‏جای مواخذه داره تقدیر می‌شه ازش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24788" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24787">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzOkaN0WD0ZfIuvuFJOxJsdN4H1k-TSFgDN6Ihgizf2ICD3PgigN828hIM7gH6NT6TG38l7Bw5nhn7fN-8R5jhTjgWof2_WWF1oyd6BXL3LeYIQg4QYNncuaDBIFrHAPB8ib7IXsUgedSvts-_2pFmk-Uq0UKzGkurVrZ7AJwp01L2RRLuZqESMGwsMJjLCaH-_Kg0QvKYi3jCWEAPXuQ_Ixd-kUujZCOnE4Ap5wiHGLlDdkozDz4R_RloJSQ7fN5BuEVhvx9rvTSsTDpkWC9g9mwoV-CDVFr3lXdS0zoMs_dSumbf5ouqhxzzszXjU0jhT8n6RXFbkjmUhl9K6FDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/24787" target="_blank">📅 01:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24786">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=EmlbztiqbRDAeU639CDgApIvQAtyyd8WVlekkIloQIiI7pD-9R1W7AitoSAb8yx_OZeWSVQgwaDLZhqywX6Jj6pnckc05Mf96xmUjV5UwEx-AXQJipz74ZVcXaXFsZpIVbq1ph3P29tnROO_LbfZyPiz10VBWyRJqgS4k7XHtmufnqfCLR9G9bbdnPWm0eMVV_XQL4kjC6OPuEeYZXnDKOjqjNFnT8t8vF9vUZPFDpT3aHeqTyVpeJ6lajM7nRFd1qHDHVcE0tmKuOGOz9kaR8y1JPjGk337ouekea_-abq5eENX-ntzClH2cfRlYSWOqOBxAKgBmI9hlM4_VfEZtyOPW_ilcHukP67Z41eXiQOOAk08ShFvkZ0dg_C2nAuH-b6dahn7bC27BscBxc7SYylIBapL0_NVqX6aKJa6gQ-AmiOVbgsPiBdpM4jjE2UtCXCZmkznx2PgV7j8ipVKwQDmIRWtTRnxiDTxsJnWEK09Tf61ijmk5SLXT6AXu-EeDflPCm2GG_Navv6ag8k63NY6fG07nU7iJqrKJKjcVry4oi0W9BWYURV0sCEzv0POdCiiOdmzaBXdRh8aYzAILF6U-gc0xOt5VJZ-x4HYMBV8CzawJaXyu1CEw9r9Qo8a7XyK2L_gQ2AFDnFUXkYq8_ELdAzgYC0uN2jM3Yl0Vxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=EmlbztiqbRDAeU639CDgApIvQAtyyd8WVlekkIloQIiI7pD-9R1W7AitoSAb8yx_OZeWSVQgwaDLZhqywX6Jj6pnckc05Mf96xmUjV5UwEx-AXQJipz74ZVcXaXFsZpIVbq1ph3P29tnROO_LbfZyPiz10VBWyRJqgS4k7XHtmufnqfCLR9G9bbdnPWm0eMVV_XQL4kjC6OPuEeYZXnDKOjqjNFnT8t8vF9vUZPFDpT3aHeqTyVpeJ6lajM7nRFd1qHDHVcE0tmKuOGOz9kaR8y1JPjGk337ouekea_-abq5eENX-ntzClH2cfRlYSWOqOBxAKgBmI9hlM4_VfEZtyOPW_ilcHukP67Z41eXiQOOAk08ShFvkZ0dg_C2nAuH-b6dahn7bC27BscBxc7SYylIBapL0_NVqX6aKJa6gQ-AmiOVbgsPiBdpM4jjE2UtCXCZmkznx2PgV7j8ipVKwQDmIRWtTRnxiDTxsJnWEK09Tf61ijmk5SLXT6AXu-EeDflPCm2GG_Navv6ag8k63NY6fG07nU7iJqrKJKjcVry4oi0W9BWYURV0sCEzv0POdCiiOdmzaBXdRh8aYzAILF6U-gc0xOt5VJZ-x4HYMBV8CzawJaXyu1CEw9r9Qo8a7XyK2L_gQ2AFDnFUXkYq8_ELdAzgYC0uN2jM3Yl0Vxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی:
همش فیک بود
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24786" target="_blank">📅 01:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24785">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RD21yl0lRgSEUGoc7j5XX644JB10mTdlV73V9tOHQtyWas-Qz5EZ3wCuKlgfZocs0OUjLVUd6eUx-1rtiPt7SulCDrGyLMaB-s8XjH0kz2YfKHSEn9qPk1RG7NLFK5YiiTS31Upoxo8th9UcrN8tXZacE-C4cCXyDKdDgPqwbNGGiO6RzD7dlUYSDLb2JLhE6GGbAg0V0I-5icxM8-1prrhGhVipeRiP37VnDSZXESWId9HbehjE9AyGgERyY_l6EUFUe2KJyFgzyoBHgFSmvW50IF30jrDcsO7zKvia9q49VVvpiVZFiVJav96Dyx54n5VYKmyeZAnkfZA8ouO85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24785" target="_blank">📅 00:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24784">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsuwdhKTk6awCxIv-2uOhh59lYfTSRd8ZMOk1zxAAThXcN7yavTzHr8lujP33PriakNycoReYg4FtaxRC9_nHJPqnhuDgAHiIkk4qJu40LWIRBqyCgNkgZUYS2i7sGd4on9RiMGHreYBnSL1xGoyhU98xm9z_X7UAa5sxWah2jYYhaBk8nYqyWilzjlXOo1w-Xq3b4nzlJlr3j0kp0s3jeTK9F6ZhrL21kC3RILjLCufQBwAx0P_U3PBK2U-pkKlppzGpnsVAxsfoSVeMk42L5UrQNv4eeLdBssD_djYyuK1Lkpe0qSM96fzETX3VppdykT46XwvmUiLm8mDnALnBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24784" target="_blank">📅 00:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24783">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=QsRv-H6mO4toL-ghXl9wTCvL_RyMAo14Dx7u8ywM0QV_f42hdE4tWkLX8GSgr6kDZPuIu-igepc8D0G2yIYNv0Mo9EdhqaXX7bN8nXBt1ZZ9zOYY51K92b_0Wp-_AfZmYsAHa05lJgz70DxovaneDZMV_oAGRtx-_AtliwMlXEiC9str59--qpxdDXngkXMWaa3-2qAmoqHM8iQCfZEuTpeefEB7iCCIguqMsFe-FfP8veFmqGxqBSslfbTDU70CVBfGIfnkhldWoxBpONDlHOWKFK47iwNVSo04165HWYi7uvcIQhDNiZZxdjuW8fFSC9xnydKh6x6S-3jehXBMLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=QsRv-H6mO4toL-ghXl9wTCvL_RyMAo14Dx7u8ywM0QV_f42hdE4tWkLX8GSgr6kDZPuIu-igepc8D0G2yIYNv0Mo9EdhqaXX7bN8nXBt1ZZ9zOYY51K92b_0Wp-_AfZmYsAHa05lJgz70DxovaneDZMV_oAGRtx-_AtliwMlXEiC9str59--qpxdDXngkXMWaa3-2qAmoqHM8iQCfZEuTpeefEB7iCCIguqMsFe-FfP8veFmqGxqBSslfbTDU70CVBfGIfnkhldWoxBpONDlHOWKFK47iwNVSo04165HWYi7uvcIQhDNiZZxdjuW8fFSC9xnydKh6x6S-3jehXBMLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24783" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24782">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQQA4p1MBoimqsJRiz5fMRWp8rXm83bLyX__c3AtD5C0sy-OoYyVPhxCydO3dQNsGaMDJBFmfmtpKUbgOKTmdqA7i9KH_Z6GTk6_rXuBFoicOXCLSEUbHwOK2HiiOsG252feYB91_y_b2vILIxdJ4wGAQOqyejWGAjJ2vqsG5VJvOqLnPFTvEUXRl4PDHaaXSb8PeljuqN8YVEg8ROVx9XylyqlYv6IADSRRCMIANNE3Jexw95Q58C7QtnWxrDufKZhw8ihmJaaoDvnH9M4_uND542V8qgVDlHD43aJNv-X2HO_5bBQOk6m34QIL5KqPMQMSJBYeZKXey3cDQsjTTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/24782" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24781">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uq0OF0aqoF0u3Y26MXkMPc69awtM8o_I-eeVvKCxVzImwLgvLDh_v7hOmWyxAo1TQA3SMlwZjuZGIPmxlrWlgUiLGeyFKyDczSVDbgkr-ZKI7kRdqs8L4fc0FAzYTniUwnBDwB0SRzRyIEtugUn4VlvK5Au61cOdba2P6MIUzvjog3aimhEtPx0CyT3_gC2Glu2x3PpUNp5N3g0OuI9em50j6MPgwUuZocPI3ycXUEOzDNlOkx1yRB50l639xiEG_oYCRf6YgB56vA7Nciflk5ruwIJVyYgSaovLQm5h_5RQxTZ7FS8K3NDR9GGc6wr-JaPwve2_vLO-PZhYM-FRdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛ مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24781" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24780">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG2zpmwWv75m9wMrsQ2dyNpsY-3p95ltzZhKGqa0Mk5xsZm_mYLATDMVk0BgaLigvNvoO20yER9kf7M2t-z_thCdj94wbTAmVdOqouIajUvFNc-68M7OFo6pLjWuGAzkooub3XWsBVGA9Z-cNKWh5fkORr8N164yQ6CqohGdNFD4HBBsOq0hu6nvZAJH8oz2RVNXTLhIyFn7thRdDMdJJay9S_FVAyxOrq8OggU5oYmS-5TbZe4Ys0Td0SRYT_0Pn9FEfamOJx4sy9J3UyY72a_rlyCoHPyo5DCIX_b60HM3geXOt_iMuS7RUILEwZitQynJNnOf1obxoXahl3tRsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
پيش بيني رايگان ورزشي در لينك زير
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24780" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24779">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32137f795e.mp4?token=fdWvoevqIsrGGPIL6UDXYXL_avMlTn6wjH_GP-qTq4M4haHRVOeDf-4hZQ3khsa-0YvhqmGZp7LGwHi_CYGShXo4kZpXfKMIsrmRTQLshKrQnMOM0mLi4kBEdyWHDV_o8TLWIZZO_Tx9s2sdoFe0jM0mtAWQ61e0XgluYs_8UYpeGCiQZfulttb1f4bgkWOKBKIGno3DIfZqd-9gR_2rCwNNjUYayAlpNt44G1kyb8uENBNH4UqYZTzljZgCXKIVF46DmnRUjnKqaVEaP4l0V86fQ0ZVpLu8UFD2A9smJWm0FNCc8ee8CLJ-pvQJ6jRKqmCB7RO3w7TNLz2XYCURvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32137f795e.mp4?token=fdWvoevqIsrGGPIL6UDXYXL_avMlTn6wjH_GP-qTq4M4haHRVOeDf-4hZQ3khsa-0YvhqmGZp7LGwHi_CYGShXo4kZpXfKMIsrmRTQLshKrQnMOM0mLi4kBEdyWHDV_o8TLWIZZO_Tx9s2sdoFe0jM0mtAWQ61e0XgluYs_8UYpeGCiQZfulttb1f4bgkWOKBKIGno3DIfZqd-9gR_2rCwNNjUYayAlpNt44G1kyb8uENBNH4UqYZTzljZgCXKIVF46DmnRUjnKqaVEaP4l0V86fQ0ZVpLu8UFD2A9smJWm0FNCc8ee8CLJ-pvQJ6jRKqmCB7RO3w7TNLz2XYCURvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شوخی جالب هوادار تیم ملی با امیر قلعه نویی و شجاع خلیل زاده سرمربی و مدافع تیم ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/24779" target="_blank">📅 23:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24777">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZVSFDj-DOetaa-ZldjqyDFNOiGgHrFsNTewQsI742cW81DA9AxqeP5FQ8pFknQ2cGYAKVLT2jkFTNnfoYxv-o2PBCGUPqvaDGudxtH-uhnbdEkf82sBVJb08XpVZUThLhCwHHIrTXamrWvO5I0DQijZqy8Jtdnv6HW07uJMlR_9amEcIW3ibxkRmAj2op77dTlRFF2H-K-Dbcpl6IZN2Ll-gKh4QyuOGP8EwZQZ1vC-IDuJSA-7Vw0rED_Tl-LGeKdqi5IMiba32YsrL_w7XuFmgEpkVtYr8OeWaA6KpRj1i5uGWs0IIXg9amJ_x_fuYRDp1Q_E92UmTLetiX4Suw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون: نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24777" target="_blank">📅 23:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24776">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون:
نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24776" target="_blank">📅 23:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24774">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310289702f.mp4?token=AAWg2G4crSyxYCRkk1S3sUpv5zE7ZATe710ObiVlxoOecQkHL98h3tASXFzYo06YH_kn0tX2ouL9x-9TskwlQ96XSAk1RNpt92Uunh4PGpN2L9ExNu85RIVGUGKTaemE518E6IgvaDewTfVZlbhTcGzXfYCktPzvOTCsFLxv-xo6U-2cTGr-kYxNxlcSs2fJFEI4tj_iuK9tad8ER7nDS7xFhMBkcvlOFFNW7_HhaMhWVh_i0rjoJvMd3PisjLVj6yfawz-IDcdFHkefXB4Hbgo4RVN8mo1bwX736fJ0Lm-qiX6K0oBj9C0TjxWaYsc4-FBu6TJWrGo-jblx5Zb8ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310289702f.mp4?token=AAWg2G4crSyxYCRkk1S3sUpv5zE7ZATe710ObiVlxoOecQkHL98h3tASXFzYo06YH_kn0tX2ouL9x-9TskwlQ96XSAk1RNpt92Uunh4PGpN2L9ExNu85RIVGUGKTaemE518E6IgvaDewTfVZlbhTcGzXfYCktPzvOTCsFLxv-xo6U-2cTGr-kYxNxlcSs2fJFEI4tj_iuK9tad8ER7nDS7xFhMBkcvlOFFNW7_HhaMhWVh_i0rjoJvMd3PisjLVj6yfawz-IDcdFHkefXB4Hbgo4RVN8mo1bwX736fJ0Lm-qiX6K0oBj9C0TjxWaYsc4-FBu6TJWrGo-jblx5Zb8ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛
مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24774" target="_blank">📅 22:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24773">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chffal9BZWhaN2e2ONkYwH_10OfviGhanIfU8cZPBXbkXIS3sIx2IOYeN1pqUWEh1im9qlQN6NSXv4wh0ZyYDgo_9vZn8I6L_BSiZWFXP2AdRanfUs8flxqUpGjMQ_0o-stlSZwr98mnYjJXaQRETnwY1np_F9ys2LCVeuxDrKLM0EIi9ZPnXug7myeH_nBStVaaRZzh-CbrPidU7_PoYNVaKuBnN7svXxheqfENWCa28caSZyuCnOa9oMau4lZIe-a_OvohENotzHkBkEgFs8cuL_1mwV5MkUpGiwMp_FBzaRRpYJbtHITzv_i1_CCJGFFRvEy7_GjKyg_K_HdFLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇧🇷
این داداشمون کل بیخیال تماشای بازی برزیل مقابل ایسلند شده و کلاهدفش‌از اومدن به استادیوم یه چیز دیگه بوده که تو عکس مشخصه دیگه:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24773" target="_blank">📅 22:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24772">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdcnwjliI6VibGR_QixqpUBtx1b8PNB8VEOn0nFXfHVi_C0Pw6fq4buMkPDjrBfZGXjQSP4-XYwNcqZlU1m2qNJyDfpEtrWRiZhPeSWi4injZjI6OSEMqZH5nL0D6mRd4wicsF-DJEXCyCDlrXZHgyVcEgU7TuqVaYT7nWNK371I4hQgY9KgKFL-OYlYML0ueZiYcUCOczt9fg3EgNG0shUCrAd-GcFCOYaTbZLJNapZNy8MDGq_9WkDoqP-C_qY-Tuf3Zz3-D8Uw9IgnHNq481KUPGTfGVVVfx_gl1Tfe51QP-e7S5XlIO3qVgjwcyjty25wL5vtGUD9c0KkVUkUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبراختصاصی دوهفته‌پیش پرشیانا؛ یاسر آسانی ستاره البانیایی استقلال ساعاتی قبل به تهران رسید و در تمرین امروز عصر ابی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24772" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24771">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=tR-xIu73aHVzqI3twYp-qd8Rv0CuUFLoV7UvBqH8reJxBi2xvV2dSbxtm-TkR6m-RLUrdROxn76HQEw5uWILFa5kL-xjd29F6qOBGTlkjJcERwzX3AAn4kSOtd7M44HmEHWqgfeZv73JVssOI0AKbXUHs8pKRnvTIhJ8k9aolc8efMhFB-CmyRkjU25IUIed6QnmCDBKKjAzKpCly6AO67Ptf9G-Sf0oQT_Du010ize8gEPjJb5fnZlPJEIVo9nRTi1E0NAp-o8a8waXRg49uxcPOXrollUZjVLdAIoCfhCtJkgRgCKCMVKmjI3Pf1Ej-DCgfHPKCD6plniJGJ3D_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=tR-xIu73aHVzqI3twYp-qd8Rv0CuUFLoV7UvBqH8reJxBi2xvV2dSbxtm-TkR6m-RLUrdROxn76HQEw5uWILFa5kL-xjd29F6qOBGTlkjJcERwzX3AAn4kSOtd7M44HmEHWqgfeZv73JVssOI0AKbXUHs8pKRnvTIhJ8k9aolc8efMhFB-CmyRkjU25IUIed6QnmCDBKKjAzKpCly6AO67Ptf9G-Sf0oQT_Du010ize8gEPjJb5fnZlPJEIVo9nRTi1E0NAp-o8a8waXRg49uxcPOXrollUZjVLdAIoCfhCtJkgRgCKCMVKmjI3Pf1Ej-DCgfHPKCD6plniJGJ3D_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24771" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24770">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y41u8Na6joIZiy7qN7acdUNzg1cYVghRaWt7-NnzrTezxm-0hqZ9xSor_HOy1SP0Ys8jqFAm0FKs2HtKWzpNhJPP9wcwaj8I_QoxP4vAYFQpfXyBseyJ8NN0mlM_t3kxEtzGV6OrKws1OGQwlS_uMeTUvqusu10JL1uNiEsMq9NzclVfxvT8I2-bwXOc3EBkgxL8iGaicxZ4S8cPPiI6nqecjUAaXzhRwcN93xlYw9W8HV10vqMwocVCIOXsLcXiVqRN5bfH0OdvUCS_KXTQx-mmeUL_CdYxlaoynzEiGc_E9syhCRaqqZhAS77bNJdBKGQPHvugS6W8eqXStG8fmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
😐
پشماممممممممممم
❌
❌
❌
مکزیکیا بعد از صعود کلا کارای عجیبی کردن که یه بخشیش قابل پخش تو چنل نیست تو رباتمون گذاشتیم:
دختره رو، بدنتش رو در میاره نشون میده به همه.
🔞
مشاهده کامل فیلم
دیدن فیلم
/start
https://t.me/nod_ppbot?start=d3c61e4fde78</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24770" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24769">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=TGCq0tp7smRROy3u8aYs2UoTc36v-MRJbmihxLV6vggHNFy4zA2xdyQKak9V_FQydfgsqLCxhNxumfh3tQjHkq1wRX5lHDZHjf6jxOoeQmOA2RBjjCYCAocVOFtwr43DWJVm3XChnIWxIYTDY3LevxwmjehSqtg9pLLwsntbSxyocJE0Uf_PksxIuOUwbmm5yrksEvpLhLFhKtqM551Q1rNV3Hinb7JgZOrH-m2KdM2ysmCGBoLRbDeoIf1CU4gefvxizGc-c5agoz6DBMw1-lnmuW8d7oUuJ9P-Laoh66I_EkLi6259APBixOYLVMzeTI4MDZeiO5Tdq6V-fz9AYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=TGCq0tp7smRROy3u8aYs2UoTc36v-MRJbmihxLV6vggHNFy4zA2xdyQKak9V_FQydfgsqLCxhNxumfh3tQjHkq1wRX5lHDZHjf6jxOoeQmOA2RBjjCYCAocVOFtwr43DWJVm3XChnIWxIYTDY3LevxwmjehSqtg9pLLwsntbSxyocJE0Uf_PksxIuOUwbmm5yrksEvpLhLFhKtqM551Q1rNV3Hinb7JgZOrH-m2KdM2ysmCGBoLRbDeoIf1CU4gefvxizGc-c5agoz6DBMw1-lnmuW8d7oUuJ9P-Laoh66I_EkLi6259APBixOYLVMzeTI4MDZeiO5Tdq6V-fz9AYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هواداران تیم‌ملی‌آرژانتین میگن: آلمان داره تقاص این فینالو پس میده؛ جاییکه این دو صحنه به راحتی میتونستن سرنوشت قهرمان جهان در سال 2014 رو تعیین کنند اماسرنوشت جور دیگه ای پیش رفت ولی حالا آلمان بدترین روزهای تاریخش رو در جام جهانی تجربه میکنه. تیم ملی المان بعد از قهرمانی در سال 2014 در سه جام‌جهانی متوالی به ⅛ نرسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24769" target="_blank">📅 21:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24768">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pe8YMnkYhvqshWV48IdTMHF-6d5K5oDsWsKlj5x-ufjO3QAax6bNwZgqH0Zzv1OTawX6zd0r6Tm7TQG1ky5l-e_wbKEA_iTNeu-1_1R-OSeAet1Yx9FwKUQMa0500f2fRok6eKVS4ZvukevI4kRXhS7jCHijhv-TspRkWClsrujCAjsZke6JLkd_S8xRgpaNqkLI0havNMynEBSDrFg5K8JbN3T-RxRGzaYEv15LGA9EzeTkqb8uu5Fu3DiDz8q9LWKwBVtaqJUpYqYl_qX4AkexlWlhsVWy1zXx_ri2W2hzuJDzNbbOeP1--hEh7uTuEqe6nQU_mYmlpnMyColJvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24768" target="_blank">📅 21:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24767">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8W7HI8l7WuH4wS1p14hkyfH96uR08FaftZNeZ0TojyWnzgic0MhRbxUJgPbwgqFf4aL-0l6kBBSRrhe_oAfhdg88VDBGsCK2ebnf4-FKLd7LY1QK41SXbNkUtcO39NkCS2LOK54Q_sKdBpG3FcoOO1bz5P0S20CFgM5riQs3Xu0mMJXaFwHGdBmMQENl6Dg2vNMVIuLtrOJOqgQeBm69s0N0mwo1rSsMKZnze9gpgIuenkFY9wDTHx2AchfaWIK0YnH193Bfa0gIa9HfC1f5P75iaxSNXI1ZwirGn7iz8Tx5V8XWC5pVNdrNDnCXLerhO_O542Zh__c45_5uqWTtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه‌بان31ساله کنگو درنیمه اول دیدار امشب باانگلیس سه‌سوپرسیودیدنی و نمره فوق العاده 8.3 دریافت کرد... باید ببینیم نیمه دوم هم میتونه مقابل فوق ستاره‌های انگلیس مقاومت کنه یا نه. بازی نیمه اول با برتری یک بر صفر کنگو به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24767" target="_blank">📅 21:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24766">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3QnjxeGOy0EPzNGzRgxWlCVp52lOhwxvb85FL3k8I-c_yr3xAMfKWgJKAYg88U6Vv3nLUoGtK7KXCID--N3gLXu7Kgim2MRMxdzeUvH7kOvyRsjQBnOzSGIYF49V3dDVtaWXqFqQkDi7wj_3G3cfla47VW6pE4J71MWil4u_X3JoLLYnQgLQMxKrAEyBB9vi5ZqSMcBdSv9D39m-ONajY2sImIX6jtSYpfDZciYu-N6rKKsAFDGSGlxZN-gLne3wT61SjhISvdrZL49NHY08Qd_tLvyI0FSRQcyoOtYI5fUze4L-DTHSQbcqDjEX9t9q-1HtvaIJ4JiDjfrzQe8Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24766" target="_blank">📅 20:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24765">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=nMxHrKIEHNGD_LH2SKnlDbNBIdlunIw97NCJXKvx_Bnrgv_vYMSCzwZXMQxwgoyIhZ0YTa79D4CBmPBbmfhG18lQVeCcXSR9yxJ2D-jdEk-HvguU6iKhvD0Hxlw8Mn0RBQj3fCz9tjyd_UoQQSiwZyEvWjoeoIfkhSs7_z1TWS545mjc8v2XDhSQXsEFZO5xXtOK5O26AP21_x5GL10hogYC0IDKctUeRivFHRX-vm-MtFDNPeiKUK-tFnFQvkaf-Z6ijmXF8ptkML3uboquoVzo6HVjMQDfB99hr4vEUxOiItDlXUkwB69bIXEhoRmRwZSowDL7n58FA_no4SUaqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=nMxHrKIEHNGD_LH2SKnlDbNBIdlunIw97NCJXKvx_Bnrgv_vYMSCzwZXMQxwgoyIhZ0YTa79D4CBmPBbmfhG18lQVeCcXSR9yxJ2D-jdEk-HvguU6iKhvD0Hxlw8Mn0RBQj3fCz9tjyd_UoQQSiwZyEvWjoeoIfkhSs7_z1TWS545mjc8v2XDhSQXsEFZO5xXtOK5O26AP21_x5GL10hogYC0IDKctUeRivFHRX-vm-MtFDNPeiKUK-tFnFQvkaf-Z6ijmXF8ptkML3uboquoVzo6HVjMQDfB99hr4vEUxOiItDlXUkwB69bIXEhoRmRwZSowDL7n58FA_no4SUaqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش:
تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی می‌خواد کجاش بزاره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24765" target="_blank">📅 20:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24764">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3BY2_8jgPkdtpW2nvuR1SAjmxgeCJbXMfxphTa9pdXXQ-hiPI3SEmX0OVLU1dUngmL5uP8SM8inHR6YhHxlX9DULaV40t0hhZ_TP0wuEVov6q3J_4JTtGNokfLv7k-_B0HjWUS_hFpFcO-cFAGIxNXp-LnQTiLyEAA0ebCr5CrRbMblZcHYcJKCQWEPJTBtCSsqnvGT7mnzDmkEnpo6nUhbP3PSPLQlT4538Moe48ge1YMlzpb9FS8N_rr9EJz0vRVkU5ZYgrWWXnGLYiwa66kU3GFw1DRs7ac9HH5zOQgjt9Z_kdGkgbm3LIRYxNzrQ83liq6Ewnq3Nhw8rTawAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره تیم‌ملی‌مراکش در اوج روزهای سختش دوست‌دخترش او رو رها کرد چون گفته بود که اسماعیل نمیتونه یه زندگی لاکچری در اختیارم‌بزاره. بعدیمدت میگذره و سایبری‌باقراردادی نجومی به بایرن مونیخ میپونده که دوست دخترش بهش پیام میده و میگه من روببخش…</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24764" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24763">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=Vgg7iNnSUNs6cETT4wAhpBTB5FjpU0NHLhnUk5F_puRkfNMl-zaTkx66yuiiYy5FhPqn1tEnDvWT3t35elI-yyv6hzFsSHe2_5f9kfNJlbGwTCS8ngD4hOldft8sDJGjY7xZR6cX9trooVaCcMPajNTflUbm-qJkvkjJktEkOy-7D7_prrdEV4Y_u5DsmPa9MaV19Q7F8Nny9XFtzyWNAiZteAZVQy085zS29I0NBVgu3Si3fpwgymDYXRgI0gtLLVfoW8ZbNNvCuRge2qda489xjYVtPuFwOab9OriHVC4__U9zKnRTqFNq_w4UEbOgIDqet56jK3EbKsIpbRkbRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=Vgg7iNnSUNs6cETT4wAhpBTB5FjpU0NHLhnUk5F_puRkfNMl-zaTkx66yuiiYy5FhPqn1tEnDvWT3t35elI-yyv6hzFsSHe2_5f9kfNJlbGwTCS8ngD4hOldft8sDJGjY7xZR6cX9trooVaCcMPajNTflUbm-qJkvkjJktEkOy-7D7_prrdEV4Y_u5DsmPa9MaV19Q7F8Nny9XFtzyWNAiZteAZVQy085zS29I0NBVgu3Si3fpwgymDYXRgI0gtLLVfoW8ZbNNvCuRge2qda489xjYVtPuFwOab9OriHVC4__U9zKnRTqFNq_w4UEbOgIDqet56jK3EbKsIpbRkbRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24763" target="_blank">📅 19:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24762">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-VfGZXtDQUXKYwzsE1AT1b0dNJNYpKTpQ-z6uhp2RCJlRcfFINIydOHu-M8qbJaKC_XPiT5fylY5ivvdQLL-bD6Uz1puPvSbbKJOnRsV377RuQtpLqUueayA-qjA4b22eMQgINFmlD7OX6dgg_znFk_wyE8YlehdgLhxJ-RilVsLR4nhg-9ozRSpAicKJdwEGrLHlgbhZAbB-XAzsaaLZgCamJ0LFNvCzuao3-rGEHGGmNjyPnKe3mgUHtobKP68vzlV-23Dily2lp9g8s1FTVJCpR8fxgQ-Yy5l-Goa8AHPwPiRZualDBC629j-v_GT4DEyKPK0PihnaW3rRthkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوستر باشگاه پرسپولیس برای اوسمار ویرا به‌مناسبت‌جدایی‌او از جمع سرخپوشان؛ همانطور که وعده داده بودیم پوستر دراگان اسکوچیچ هم آماده منتشره و بزودی توسط باشگاه منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24762" target="_blank">📅 19:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24761">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=f6GIDqOcGHGmcqSQTeaA5WnNN5rnNFllxdMLpNo6GIE_HqjPtNX7R8vnX_C1JcQEhkU0TOHoapREMRD4715VSpPn8gL_9-QNwyttvXXDpNJIWvHdRLvy6UpzVzs4gusm1HjX2DdCBwlKpgivCRifMebyPYXGWcBe3do9zE32z1xnoTz0SsXS1YXrINa3dCa7k62kZg0zwPBwpbinK1JtZiWdOq7Tg_nEeGU7aZ-FvFU1mXmdd_e19YqVvtis-BlA2KziMUyOFZk7T0J6ssWY4-6i57GHvLMD9-588f7INUDO5QW1Sd97yczp4A27Mx3B7Jr9K1UgKma8E8SDkaCgTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=f6GIDqOcGHGmcqSQTeaA5WnNN5rnNFllxdMLpNo6GIE_HqjPtNX7R8vnX_C1JcQEhkU0TOHoapREMRD4715VSpPn8gL_9-QNwyttvXXDpNJIWvHdRLvy6UpzVzs4gusm1HjX2DdCBwlKpgivCRifMebyPYXGWcBe3do9zE32z1xnoTz0SsXS1YXrINa3dCa7k62kZg0zwPBwpbinK1JtZiWdOq7Tg_nEeGU7aZ-FvFU1mXmdd_e19YqVvtis-BlA2KziMUyOFZk7T0J6ssWY4-6i57GHvLMD9-588f7INUDO5QW1Sd97yczp4A27Mx3B7Jr9K1UgKma8E8SDkaCgTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم ملی اسپانیا:
«من اصلاً دلم نمیخواهد که‌همه ورزشگاه‌ها تشویقم کنند! هیچ نیازی ندارم که در همه استادیوم‌ها تشویق شوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24761" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24760">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAKESvXV47l2YrTxjsAp-hNE7yX0OJFc2AHgDzrMdlpOeQzFv0iU_1A6WcODuM9A8yeXmT5OCdrHFOTnLjpZGxi9aVHce1F-C6eIUdwtzzcbctaC66u7eupaaIuk9Kbj4pSZNNq-DSF8oTmDCmsTFTnxc8aCvXPl_jugnF82KdGkjaGfLv0bqm5kbnTW2oUC_2KbYbaCiqrltOwTSuIwmOdfbXU-puJif9F32ilWUxhO6HfGcYVLBvkGLi3ax_-_Nhgko911hLRD2cXMXytZzQIIn5RgK2xuD5AOuWf_V30S2wCYf38dP64QFfDyiP3eIJi_L_88oepikJlv7KJlJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24760" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24759">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yae8k7G8Mi1vg2efGXxKFWqJ6U3bzuHigcDMa1dlCAHqLvDB4pIKPhlwws9zMwAtBoFP-AUnltBzCLwvnjTEu4lbpTMH-xZxWGTDiGgc4SmsQHJxWB8ip6ixCMljubGmzEi1rX5viM6TiLC04DP1O-ukxEMug1i3D-czBx1UgOmqJNXNHb4JNJd_WOl0dvo4UYhj2qubeqXXhBXHlJ3txjvDNFIb1N4gy445MzU9mVEB311CrOH7SVLuimfOmH7i8z5eov_TdmwmZRoNGWwYWBTMPGjSmnduMiViTOROjfycFFRILssSm3NDeQQiIpEkdT_JgGWlsmNOvr2d7M3KGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
مسابقات جام جهانی 2026
🏆
🔥
⏰
شروع ساعت   20:30
🔥
20% شرط هدیه ویژه شارژ ارزهای دیجیتال
💳
امکان شارژ با درگاه پرداخت
🎲
آپشن های متنوع با ضرایب بالا
🎁
10 درصد فری بت به ازای هر بار شارژ
⭐️
برداشت زیر 15 دقیقه دلاری
🔥
همراه با درگاه‌
#ریالی
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
https://halvirox9371.bar
✅
کانال تلگرامی
#رومابت
10
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24759" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24758">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpDc5ma5P3uKh_HLdiL7iYoG4L0z-ulrZeom7bJRmQ-rAMd9HYNI-2NN3WT_NirzkA0dtwT67_6MqAEbLtxJCy2hdJ9vjBZZTbv58TZF2O68kNENFesa6FIdRBuDAf0NH05L2f_2XDXH_G2FGYSj9rjf5i9XVMtUwQw2MALY4XmzK45mO_DI9uhezswnIeY-0YD_yztVUhQzSabCRjrHXK_95v8k29W5NvS1wYnC5iaidZq_N00XWusP8dJbS6nTWW2cCcLtuGLtdGZXzskLiD2Q2vayn1ebrtr7NLao6iPg2XIar2G1mKHpVcSv-mfBE33naqknHBGKLqsWPah-Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24758" target="_blank">📅 18:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24757">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhpANXbSVNyHG_RGjMYlpPTjbm4HNUbG7DJyjn6WCO8xfO_NyknjpBrfcUHRI5OweEdl37CrrajD8n3isKVd5egwefMODtvoHxwsTG6v4pXcRrkY7RH7NjlsbMSVdOcGpIy9BVbubC2Gd8IdrUw0LHuSb1NHbKM2GoBIjk9wYFpCDkCtf3CXhkVoaJ65MuoZ1Y5vDyQSyTzZhGSki_FbHxREnCI6jZurQT3H4poVRXDf91wx44uDEtyWOf-B_PqZTAiTZoRCXTOIGRwpIB1upsqW3uwETVsge8QPtPKKmyR24GbWk8svTLRs8xrc00ahuOYVQXGYotx3kuOPPXBJQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی
؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24757" target="_blank">📅 18:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24756">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bo9qxkz_gjDshzKzbOWmtGO0LRfnNqW5GatpsKXkQ02M3ZQAXlETE3BrSi8CFo5_7wrYXZvmYwIWBz3SUDf0X8t88nHpUfUrzsOfctKeFf7lJa3DtGlgqxDlHKKS5YyVepgCStKODsvdnl7Rz0T3tkJfNXNyCNzxs3zISFOqO-U9UhgWKrTrruBKOnY-LOKcuOQyIEF-6aSJ6eYyCeyGjeT5q9JwgXm5eyETrF3CX_OSSXI0LxIuhNgWATyIp_VOR9Us9ZwTssTZZVSNDzeGhRiiRZ-Yq5oM4arYY_c1Hb1yvPKxdQnUp9-cTMfzgIURx98Stqf0oBy1xzBw_cWg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24756" target="_blank">📅 18:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24755">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qo6AjUsIp7XksmtO7O_qsQEVeGrCEOFSQmW_SCL6hAEvCNkng_PQyu6q0BvbUb-DQiZa1EXPXurRQLWEzmWdyjtNOd3SoNklPrNQgHuVtX_QM7B3ulL6uVEafirXI-TgFfKCDMe-Fm3slEPImclTWsekcMvEALii2uBZfOshy-Om9b8ArNCXUodmRMGSxgFHb6eIDHGvk6rPEGR3mOik7maoSNE4Qw5e8FixIua_k6_2PJgiyhO3Wh1-oBKQ5HzeLt91xIpufN86FZsoz6cdxEgpXs4dT7XM3yi78SbZ20iFqGHqrBF_F4OmGhZZnKvDI-d8jOl1_44a7aJS5nDZVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌رسانه‌پرشیانا؛ اوسمار ویرا دقایقی قبل رسما قراردادش رو با باشگاه پرسپولیس فسخ کرد و از جمع سرخپوشان پایتخت جدا شد‌. بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24755" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24754">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=VW4YZj43jCqhU0Tpvr_PKMfrC1-Wg0fk665wC9WeDwe2CS7fGj7plTowFHms2ffGcJVp91grJFEtABMBXJSK8rB7a-4zGh8T-Grd36OdxuA6keWOogwBxADEejRGTOHvVGVYqYynFbLA_emNtqCrmxhk_2bbyzwDSIBwFMCpY7Ox4pOIRs2oMQMN8sE8gtx3HU0tusgMC89bn_ROyEsgWE0sKGvHk06VW3-0xzjvQhefG1CJSsEIPC4cXWcqn313zPrWAw0w6MvRjxxf1ifx46B7F-dDui3sjpXjr18ZJV53Fg8FrVJ3IYBhSi1_NM_PxEh3xxasuDrfr0mNoCVD-18rSX8ZN0HJTVkXKMIVbdzRWzKDbhDYN6JSKWk8fElpSF5gcRQWUd3LdC9piDbWkuRhnxRAmzwyi_YfmLRzTT0hHkPC0iNjea8LrYrDwH_d7nFnkPltnqpCsYUBbe0NXjLNmRaZNsGkgf36trRNn1DSbl6XyFofrwF-fIf7CwQVpqQxrIajdKbMD8J_K4o1IruGnmxrAcmhnaA_DL7nxKIjALuSmwgFg237WltRyboqqeXACIjEqEHZGMH6g7NNjpatyXj23A-2cFz1-GtJ9GmjJy_KGrvT91j0kX7P8-1F6XmkTNLsF-dECz3DwAT31XVDXP6hAjb6uICemGQnSgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=VW4YZj43jCqhU0Tpvr_PKMfrC1-Wg0fk665wC9WeDwe2CS7fGj7plTowFHms2ffGcJVp91grJFEtABMBXJSK8rB7a-4zGh8T-Grd36OdxuA6keWOogwBxADEejRGTOHvVGVYqYynFbLA_emNtqCrmxhk_2bbyzwDSIBwFMCpY7Ox4pOIRs2oMQMN8sE8gtx3HU0tusgMC89bn_ROyEsgWE0sKGvHk06VW3-0xzjvQhefG1CJSsEIPC4cXWcqn313zPrWAw0w6MvRjxxf1ifx46B7F-dDui3sjpXjr18ZJV53Fg8FrVJ3IYBhSi1_NM_PxEh3xxasuDrfr0mNoCVD-18rSX8ZN0HJTVkXKMIVbdzRWzKDbhDYN6JSKWk8fElpSF5gcRQWUd3LdC9piDbWkuRhnxRAmzwyi_YfmLRzTT0hHkPC0iNjea8LrYrDwH_d7nFnkPltnqpCsYUBbe0NXjLNmRaZNsGkgf36trRNn1DSbl6XyFofrwF-fIf7CwQVpqQxrIajdKbMD8J_K4o1IruGnmxrAcmhnaA_DL7nxKIjALuSmwgFg237WltRyboqqeXACIjEqEHZGMH6g7NNjpatyXj23A-2cFz1-GtJ9GmjJy_KGrvT91j0kX7P8-1F6XmkTNLsF-dECz3DwAT31XVDXP6hAjb6uICemGQnSgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برسی‌کامل‌ودقیق‌شدیدترین‌مصدومیتهای مرحله گروهی جام جهانی 2026؛ عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24754" target="_blank">📅 16:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24753">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=PFgfKbL0AAdiiwWdZ4Ao3bi8XHV3wanfSFjtD6bG34yYKR8QvyzhGP8sCinkeQMhk59PKeIY5iqA_D6onh_6HjQqQiKKHABI6ryOWsRn8VsOQtD0eKD_byBMT6cWUKB-M2_lyJXDV2QVxhlHnHB7CZ8FD1bzleXTMNuycPp6IuuepspmeJP923n_LXiRR3Xt3esU_iQygEOqIRa7thY4Kg4QyB4xtCkAFfo5So7BTND_sGxm5QVo99aSYoeZgNs8W3eNRwlAQdFGGfvLKv8TNonwFxUDQr3RvT_PnV2VxryakexmFS87WTrkTeqRZvjf6kmeVRn-g0WiMffKVaakGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=PFgfKbL0AAdiiwWdZ4Ao3bi8XHV3wanfSFjtD6bG34yYKR8QvyzhGP8sCinkeQMhk59PKeIY5iqA_D6onh_6HjQqQiKKHABI6ryOWsRn8VsOQtD0eKD_byBMT6cWUKB-M2_lyJXDV2QVxhlHnHB7CZ8FD1bzleXTMNuycPp6IuuepspmeJP923n_LXiRR3Xt3esU_iQygEOqIRa7thY4Kg4QyB4xtCkAFfo5So7BTND_sGxm5QVo99aSYoeZgNs8W3eNRwlAQdFGGfvLKv8TNonwFxUDQr3RvT_PnV2VxryakexmFS87WTrkTeqRZvjf6kmeVRn-g0WiMffKVaakGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌فیروزکریمی‌درباره‌مراسم فدراسیون برای استقبال از شاگردان‌قلعه‌نویی: اس چه تقبالی؟ خودِ فدراسیون از این کارش خجالت نمیشکه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24753" target="_blank">📅 16:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24752">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lu4ZAWZbqpMF0kiXKJxw_J3mBRj19koGp9-rBv5roIKlMZyuqKER2b2Tam4TRs_g-XHOog2XcOQuSPnsD4J5F9yK2ZOEu1Bghgtrg9wFAVVu8cxNN66XHyl4HNeqrT4qi9I1k-HCZPxSj4EgJbQ7vUSWhJVpXdNmNS9PD6-ombCfdWnUWzo1-Q3D3ZBAgiquPXdhs1Y17u7z2v8AxXeCgv4iy5VO6x1Et6qfz_DVh2VJ6l0cRhlBOwryLZjVJr2Fm_Gl9beS96TnmpmRjNYfbdnEJF3HK-uz1DLkoDEwAOLJzjpcdxKWw6FVaEHR9-ChAq30rDFlOGw_Pw7jvfH7BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24752" target="_blank">📅 16:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24751">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=r-QjLhIT6p2_Mg6fzd3p1qp1eYu5YWWQdbFw1_fIeob7nLBi0wV_V7HVEiIlsZ3tjRORJHbfDZDqXeLpzEYNxy1ppqL2PBphE2meN2cAqmz19kEcMRCwRX6QhjNWQIsjfyQgsm-Et1G83x_PSwGR0oraIfJwl00y2s2Xw8JYNzs2pG4qoir_8zz_-iIT8Aq7av1ezrAspRFi6d1gkPJxIGepufOfYFUJWwVMZhF16DVl1TqSxkX3y5mExlf-jZvpgD3Vi9Kq4ECSXMNnCH-lQymPCmWq-c7IdqhrnOkeYCtxdmX9eGPZ4JK2dh43hobJxglwW_1ZbXvqapwO5wb51w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=r-QjLhIT6p2_Mg6fzd3p1qp1eYu5YWWQdbFw1_fIeob7nLBi0wV_V7HVEiIlsZ3tjRORJHbfDZDqXeLpzEYNxy1ppqL2PBphE2meN2cAqmz19kEcMRCwRX6QhjNWQIsjfyQgsm-Et1G83x_PSwGR0oraIfJwl00y2s2Xw8JYNzs2pG4qoir_8zz_-iIT8Aq7av1ezrAspRFi6d1gkPJxIGepufOfYFUJWwVMZhF16DVl1TqSxkX3y5mExlf-jZvpgD3Vi9Kq4ECSXMNnCH-lQymPCmWq-c7IdqhrnOkeYCtxdmX9eGPZ4JK2dh43hobJxglwW_1ZbXvqapwO5wb51w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نقل‌انتقالات
|شهاب زاهدی مهاجم سابق آویسپا فوکوکا به تیم‌جوهوردارلتعظیم قهرمان فصل گذشته مالزی پیوست تافصل آینده در لیگ نخبگان بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24751" target="_blank">📅 15:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24750">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‼️
دیگه وقتی سرمربیت اینجوری بهت تعظیم میکنه فقط یه بازیکن ساده نیستی؛ کیلیان دیکتاتور
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24750" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24749">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=VJ-6vDuSKiInFhxeUsJj6c507Z9FKB9MGDE67fRfG4DtCUJmTVTr_gZGL98PmaeY9oAOKX29hhMZVMqjfQIy32f-91conMs8-Zdax7cT3m9MoyKfxjXHjkBoD7SSFrdrypbqQVMghU2MhiLuwhmlJGogrt6ZODAf2EbOu6Wn76ED-JVg92pqAUkidRSFa0oSxNMwoQn2YE0pbeWQeFQ9zJ4zeUjQ3NYJLhZGmPdIWErdDKjo73AWD1qMpuDDCjQo3gS6eW1gM9GjqkddJWXfk2uE8Clo7ZwbBxS96Fku2qRbg287sAAmFf8VaimeQPYUKcJY6akaVruOpuV5wCTLPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=VJ-6vDuSKiInFhxeUsJj6c507Z9FKB9MGDE67fRfG4DtCUJmTVTr_gZGL98PmaeY9oAOKX29hhMZVMqjfQIy32f-91conMs8-Zdax7cT3m9MoyKfxjXHjkBoD7SSFrdrypbqQVMghU2MhiLuwhmlJGogrt6ZODAf2EbOu6Wn76ED-JVg92pqAUkidRSFa0oSxNMwoQn2YE0pbeWQeFQ9zJ4zeUjQ3NYJLhZGmPdIWErdDKjo73AWD1qMpuDDCjQo3gS6eW1gM9GjqkddJWXfk2uE8Clo7ZwbBxS96Fku2qRbg287sAAmFf8VaimeQPYUKcJY6akaVruOpuV5wCTLPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یه‌فلش‌بک بزنیم به این صحبت‌های مهدی طارمی بعد از دیدار ایران - ازبکستان در کاپ کافا: اگه تو جام جهانی پنالتی برای‌مابگیرند من نباشم کی میتونه توپ رو گل کنه. جز من هیشکی نمیتونه پنالتی بزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24749" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24748">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORaMQrFlvzRxjivIJz4eJ92aANxUCTuGlp7_GLa1VfSpZ_aPXwedr_mF6INHpiE0SZ8RImdsFgYRWlrezY4RtE-__iqM6YJNMfzvqpa57upluaPgv_AJjND1I4hFbXLtDY_puUGkvmmeTRxvcSx1c7OYJPL2-5BJUm4Br5L8KA3iEwvh1iAFnnpU6_CTDis06f9F9Lu4u8TcHo0SbROy6g3u2l-xDYCQV9a6xQTWpOC6En8JatxGkycchjC3d1fApc3QZ5ZHy1QGbgXfs8IncgX4j9cVfyYcC-uW5X2X2f7c4cacEuK52c7ePL6WF_XSUpIpbyMctglnxViVnP7kPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرمربی اکوادور که خیلی عکسش از لب گرفتن از همسرش بعد برد جلوی آلمان وایرال شده بود، بعد باخت جلو مکزیک استعفا داد. اونوقت فدراسیون ما برای‌حذف‌از آسون‌ترین گروه مراسم استقبال میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24748" target="_blank">📅 14:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24747">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rt2sinys58nebIAdapD90DOn8C_dJ57EgmmErawNUSFRLaEDtpSnr13FoyCmGl-co_siQDQ2-JkhDiRaEwd-9C0qfFyP3DSdhNlbD7p_ghUMaNQp3hccu4_wAeYketzZBwNQUtjYJdlR5YX8drzynamAth0fW_lk018bGs8-tshiirf3orOMx461h9g3JwD5lCEQF4uSXcgGN5RAoh1m0QYVEUeKcbJrZQNHQxMXNJRZfDAIvwvQlQZ4aUD9YTmLnzXvTQTSA7r6PnydHbjsVjgDg_Z9bXVjzmLWcqD-o1VxkakATjg4x0k9kHnsAyD2rtxMMFycNC8arvxI5hQmLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24747" target="_blank">📅 14:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24746">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWuGxn4n-Wx5EnIoOnL6rKz4tdGhszv0OnkYbF6e7WyQjUrcnzl7NgxRuvMLbGXsrfM0_IevJU8LqjV34SDOvmbYJJy3nYbRb-lqRpeBOkl5gl8cul0Q4vlJ6zRrLK4YElSkheL6kY7OYg2ln-dkVFBhwgRKwjWjstPWYwI3iB0CCf69Sz2XVbQtHMrvU9QDO7-GyjFhMuT3PlbyTBGrHjgC_hin326HQFoJU16JnycFdTYX0xWLdzFQNl0xWIOUN7Q-wpN-sZORrxrBECwjfZvI_2rnon37oHq_W57ha7O8iKvDGjuJ7S1tb3YNn9bTOHQj8lVDkE2TwdPZ2n9mug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان با باشگاه دورتموند بست.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24746" target="_blank">📅 13:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24745">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4FleL2-zxbqrzXTZboU1_59Ac-y2RFxg9rNwWUwdryjWe-YC7VxbbyvvkVXSlGPWUVxULa11045ukrdbWiwoKkpVTn-QbZDKh968Q97bnTh3_A8ct8FFkQAkpNPyDxHramYJPp7l9IRjUz1h31srNf_58AI8KUcH4t-ztmP6IKSvY-radctS_Ny-vevQ6tyb_DmPcEVtItPwYZ05Pr6nvP_qQMM-RqOIgEzdKo1FYAmPwMkqUCVpW5aeeO02qx_3ztVFBw3yLcLpD0sQgK1L_2nypP6qDeWqatS4_GEEq6HZwqV1m40zmIq-ZZmVcWfxiosA4wz95erTzj14TV6KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه‌بان تیم تراکتور از شهریور ماه سربازه و احتمالا راهی سربازی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24745" target="_blank">📅 13:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24744">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=Xa86LrZJen9JGcI6dF2h1F55601cY-tzE6nk2LjOQmAjmC-_cCtnWYyyMk1DpGCu3Or3ljOsAxqSlKd_dSgjoRPWlmgts_-sB-n53gy7pQkuEIsgyNi8uHQjDo5PkziKWSGZbEV4lpqECH07ZXMQgyRJxAJ9wJf8JX21VlZYsk2o89DZwvnrXxm3mFt4FYHlh6RMY59K0ctN0vGpG-amfOHYv0pMLyRPWbOdKLVucAQtbakaFXHPHdpW7WtgsOj7A6BjYCDAFnTswyHMJe4l3j9e08gNwhMflbVwlB5UK8IBkck-RyxoXqFJnU2tIRXb4PeCFNQu7p7k6qxsnE8PWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=Xa86LrZJen9JGcI6dF2h1F55601cY-tzE6nk2LjOQmAjmC-_cCtnWYyyMk1DpGCu3Or3ljOsAxqSlKd_dSgjoRPWlmgts_-sB-n53gy7pQkuEIsgyNi8uHQjDo5PkziKWSGZbEV4lpqECH07ZXMQgyRJxAJ9wJf8JX21VlZYsk2o89DZwvnrXxm3mFt4FYHlh6RMY59K0ctN0vGpG-amfOHYv0pMLyRPWbOdKLVucAQtbakaFXHPHdpW7WtgsOj7A6BjYCDAFnTswyHMJe4l3j9e08gNwhMflbVwlB5UK8IBkck-RyxoXqFJnU2tIRXb4PeCFNQu7p7k6qxsnE8PWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاویر ارناندس ملقب‌به‌چیچاریتو که در تیمایی چون منچستریونایتد، رئال مادرید، بایرن لورکوزن و وستهام بود، از افتخارات میشه به دو قهرمانی لیگ جزیره، یک قهرمانی سوپر جام انگلیس، قهرمانی در جام باشگاه های جهان و قهرمانی در جام کونکاکاف اشاره کرد، وی به دلیل طلاق از همسرش به شدت از اوج خود دور ماند و دچار افسردگی بسیار شدید شد و در نهایت سن 36 سالگی از فوتبال خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24744" target="_blank">📅 13:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24743">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0xVFRAFgoeHmP0WguE0ay24zYom72R-XGFnc4MVxGESCoone3b987AmTQ-n_518Lk0mUv8tdg5Y5OD8SHIToxDMnt-2WlSH9anPp6uYzvK1g8Jna5rtDVq7J6n3b4nrPzlYPZK3aoeY_wqmpcmWd1WQQytwuOjQiEebsq9pnHjMTvLajvkOl-zZzRCHwIlcVmmeW70FMxhMNL30LzaMpkqpujtj68A2MaCmRkDnkyPMrukYEa5xOPywIzigGEZpohhP9rhsoKZEQex0tuiimW52KObkzZw8cc-HBBVER7AZqPM8TZxDEEHWUomM2EywG76xICzvBlOXdIswA_LZ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24743" target="_blank">📅 13:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24742">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ej4zeeCEoiWVTSG7rWtqQzg3xm-LNmaOUG_0t1iR5dJqRXrZaGkzlzHqinheQ_dh8ej2gMLbGaMgDeaXtuvtKkKla7xdsQFuE3jYaPVmhKbwhF4xbcQQukc85ENsHdTWCEGnXXSeUewWQwmFPVtWyazDI1vfaYNKpj3y5yksJ6w9kMuOvEe8DPPlniB9C_YyzCUjibrK35HwWW0fv7LQ0oJS9BpNxfPJB47jp8R34fXh47sNeF8E1CvGvknolJv77K7XAIFR9emMra8V6rXcuvwQkGJOPLk3X9J0nocsrihH3dIKa9RHl1VrpHtdS1HmoA6KOZta_rhuHlmJkuNeXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره مراکش در جام جهانی ۲۰۲۶ و بازیکن‌باشگاه‌پی‌اس‌وی آیندهوون که اکنون در آستانه انتقالی بزرگ به بایرن مونیخ قرار دارد، مسیر همواری را برای رسیدن به این جایگاه پشت سر نگذاشته است؛ او در ۱۴ سالگی به دلیل اضافه وزن و عدم آمادگی فیزیکی با…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24742" target="_blank">📅 12:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24741">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=qhuwNLD3v4Az0F9Zde5fY0q1080aCZfselB40Xy4Vv_wBJL2ffW2gW7pgeE-BVmJiiqmHlq8exh5jhtS6EkeJLSCbK6AzdC-dhJjXxvyDwTooGhEU4o-0CNUYPhfRrJUznR6sel66KTfroSc7dTi_CgYzNMaY2uDls9u8WSKAMUmR5WO-200NmmXvmb0kMhjqpXUCDLhouNPycWoSPeP-iZ_fXwBoP_t5L3xqc52fzo4tylz70LFpSu3LH4QtsJP4LwVJRQ7xbGBlNaX06OoEwk7TBhk9P6wd2-eV-BEVWIcb5TT88IG0qhk2GF6LHoLAz-jUEiJyAC4kyZAaimZAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=qhuwNLD3v4Az0F9Zde5fY0q1080aCZfselB40Xy4Vv_wBJL2ffW2gW7pgeE-BVmJiiqmHlq8exh5jhtS6EkeJLSCbK6AzdC-dhJjXxvyDwTooGhEU4o-0CNUYPhfRrJUznR6sel66KTfroSc7dTi_CgYzNMaY2uDls9u8WSKAMUmR5WO-200NmmXvmb0kMhjqpXUCDLhouNPycWoSPeP-iZ_fXwBoP_t5L3xqc52fzo4tylz70LFpSu3LH4QtsJP4LwVJRQ7xbGBlNaX06OoEwk7TBhk9P6wd2-eV-BEVWIcb5TT88IG0qhk2GF6LHoLAz-jUEiJyAC4kyZAaimZAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ته این داستان شد عزت یا آزمایش ژنرال؟
امیر قلعه نویی سرمربی تیم ملی در جمع مردم تیخوانا در زمان خداحافظی: خیلی دستاورد بدست آوردیم، این عزتی بود که خدا بهمون داد؛ وی پس از بازی با مصر گفته بود گویا خدا دارد من را آزمایش میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24741" target="_blank">📅 12:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24740">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbdW3CPXwlCo02kZHroBhFTiXD9-capf6Qt10OInaw0x5RAy4pZurmQWBZvOKe2NLj8ezfcQMIM9zHGPCG_HowPv9ijR0eXET66i-QJ5JCMzpOtokq0a-8loBCampVg9ZcrfCGzFs7S7QH2TaOxjgdmRAezfEXovlrx5vjQVY8_xaP7fH44fNDmxE-lQBF3oEp_r6kVimVYjM59v9Smm7jEsKlftAKkW8Bkh7hYvI2b8t-mgF5TCK0mqnFvUQTbNqMXF1ziHevNlnnKYvJkrVGRPE49D6W5j5sx5OrpwpyC6s2IN5jwEIF3b_GLmTOeRlQ6IwbSljOG2js3NtoQH2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فابریزیو رومانو: ماتئدس فرناندز که علاقه زیادی به پیوستن‌به‌منچستریونایتد داشت در نهایت با عقد قراردادی‌چهارساله به تاتنهام پیوست‌‌ فرناندز بخاطریونایتد پیشنهاد رئال مادرید رو رد کرد اما به یک باره با رقم فوق نجومی سر از تاتنهام دراورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24740" target="_blank">📅 12:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24739">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdr0pOjS-HQ3vQCevNd7worrDSAj6Tzp4_OU62IwPSTDGB9VbKS-LxbfjI_yqg3PTZhIgfYc1nwyBzbfU3X7CS3-1uL1pKDyEPbIj-8sG7Tv1yHWCx9GXdGkeI4FpPVVbVtco-kPMb8tDPqaVGcIRgQg1857kGI4T2B2o4blpmnaHLv33ucisIeZIT7moR7n1lR1hsZ1vgaxl2zfYgUTU3W2g0HaYiUYAjAKAQmSBu7sHcfF_gMFsx9cndZtvv_F4jRc0amzbHtcpYlcDpoOX0bYDm1mskKrPVdS-FflnD1RQloiB49kE51qb5PlL-sk3wen0SF7yUnL2hIfv6HhiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ سال 2016 دقیقا در چنین روزی؛
باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24739" target="_blank">📅 12:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24738">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8GyeSy0gIXVDWel2kKqur48ZJc5MOGJTp2eRWY2A5k2OxCn5ECbkktkPmXLpyrPg4ArrWG5CK-GmQCunupmX4yd2G92LP3YM5xEjWzReOy5TAjAlatqF_g_oEedKl9IEz2OMzHLgX5ezmLc3MLBP6BLQFB6tHZxaN3i4zieeqOjM39FpGs0aN88j-AlJ2-f4tiAdvI69sK5v4RKzadIKfFEvDCDe6WGWQELIrDWzvc3k-xofrFSKvzzCcmXF4HEn7v2TT3Kz8i-qR5SkCS_wLvnw4d0jfmL13qrTjtI1dBJ21O6pjXbkFqyjM5SsHOIgEKT1F5FmkLhJ-iDiCDwFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت:
کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24738" target="_blank">📅 11:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24737">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApnVnAMQCnxroSZRsnqz3mpg_u3WoU4KAAZv43C1KcnAH9nX0PH6OLlgla8wWZUXD2LGMfb3KPNpkU-isNmO6MZtl5xmUYO0ZRGxA5iaXH4R87xafEHmWkNDMfI-7RO1NUwnQxn0Ev8-w0tAtMxQG83URZXtZmnq-P4rpYUAbLpq62EYmLwKmd1HSXV43Cq1U7TF8e8-Ed6i4HSvRbJqArbVgVtcFP5YQymkh8Bt4z6pxlzBaoQIfzKGH8iUpu41OFSNhH1hBuLHJR3478Ann51sMtsEJzA53hviBhifjkoUHn_Ui8T9-iWSJGbPcC38bXG5Trdk2QseTTgrrAzLdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24737" target="_blank">📅 11:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24736">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=Xd6t_Tbr3zkQOQCV003xkZAaxXyOToFbkMPSuGM9xwBaEY2zGv1QMuPIIHC5gx0Lmoe4lw8hWg39Gs-Tn2UQFqlROPDhRgEKqaS7pKjBvFk_gZS9N3vcE6COvQF_cbEPA81SgVYvOzzznnvyfaB9EfS3gPVS8JpmIhckId5yVvhqihqWO99yyQMkERnS8w0b0AhNKW6g17CPiWIMn0WYHIDMnk_mAYURlDoIizvh_IXNWL-mEfRaqgEYmPrTgDY-eHX6op8VjoC0MdyhzUZBwxWXAsxqel8TjEIHCkjF12jVjxtHbVmBt0L9sr1i6KNbifPK51BSpV0g9yexW0AQFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=Xd6t_Tbr3zkQOQCV003xkZAaxXyOToFbkMPSuGM9xwBaEY2zGv1QMuPIIHC5gx0Lmoe4lw8hWg39Gs-Tn2UQFqlROPDhRgEKqaS7pKjBvFk_gZS9N3vcE6COvQF_cbEPA81SgVYvOzzznnvyfaB9EfS3gPVS8JpmIhckId5yVvhqihqWO99yyQMkERnS8w0b0AhNKW6g17CPiWIMn0WYHIDMnk_mAYURlDoIizvh_IXNWL-mEfRaqgEYmPrTgDY-eHX6op8VjoC0MdyhzUZBwxWXAsxqel8TjEIHCkjF12jVjxtHbVmBt0L9sr1i6KNbifPK51BSpV0g9yexW0AQFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه‌جدید آقای‌امیرقلعه‌نویی، سلطان اعتماد به سقف بعد از حذف از جام‌جهانی با یه ادیت عالی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24736" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24735">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=kQCg_DBb-tC6_RIwyrBZCtM5vCiZ2hUJ__HuqFNuw9_DXFuYamvXBJ4R-SDMxs3hOUi15wzkNsffH0gSNMI85ry66nyINH8kQCFXCggSZk1-fuPHGrfm7yeH83KkN_k11fFG5nxAb-J6Tu2VcxbLX3tDACcpMW2jeySpUaTqpx3yZQ8fQxDIFICa3MMlRyuYsWs3MucFDcikIkgppZiYQDEA1Db45OgahkHDrvpxkPQ20BbSSZWYwiP6CCc7bBHPybd7J-WEDd4MWR-Wbm_w3OhSQD4iOfJXBOtB9HHIvXL_2nGkHInH2QnZv9LEZnJo_4ITJHDEbT5LDdlscnO83A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=kQCg_DBb-tC6_RIwyrBZCtM5vCiZ2hUJ__HuqFNuw9_DXFuYamvXBJ4R-SDMxs3hOUi15wzkNsffH0gSNMI85ry66nyINH8kQCFXCggSZk1-fuPHGrfm7yeH83KkN_k11fFG5nxAb-J6Tu2VcxbLX3tDACcpMW2jeySpUaTqpx3yZQ8fQxDIFICa3MMlRyuYsWs3MucFDcikIkgppZiYQDEA1Db45OgahkHDrvpxkPQ20BbSSZWYwiP6CCc7bBHPybd7J-WEDd4MWR-Wbm_w3OhSQD4iOfJXBOtB9HHIvXL_2nGkHInH2QnZv9LEZnJo_4ITJHDEbT5LDdlscnO83A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
منصف مثل سید مهدی رحمتی
؛ ارزیابی حضور هشت ساله کارلوس کی‌روش روی نیمکت تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24735" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24734">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UW388i8nrN85L_yk8S7-ZqcYAuoArq_EbbCS8E-gaXP4P2tIPpnFz8Nu1tRdiZZ8yhbeDl22QX92HbX_LeDGkW4nwRcLZVFUAe1YClsk5AjnkvMeMBmx0nkPP7O188AHTXX4LBN0CtNwbtdNImEaFhBRgArMXp8R8o04RJ2tmBbX17hrNUqmuwnFfGRNeRv8KQ58fK9KTwYbKaA8xwlDmzjaCYMYSrJqMTCTFhfd2JbeIYkJfTNvcpyDgiRD6FwqtaX7GPNYzAc3ZZrZqMlRm2foILLFIXfX_PKWgSCVzviWFG2dGwHG2HIK5pYibNuYpLHLEYSqH7qF0_ILgD4jCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
توصیه میکنم بازی های جام جهانی رو فقط توی سایت بت اینجا پیشبینی کنید
🅰️
📌
اینقدرنتایج‌امسال‌عجیب و غیر قابل پیش بینی بوده که ما تصمیم گرفتیم به شما کمک کنیم:
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی بگیر
🤩
🤩
🅰️
کش بک بابت هر باخت
✅
این بونوس ها بدون
#قیدو
شرط و نامحدود هست
.
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r10
@betinjabet</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24734" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24733">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etnhn-GegPCk7Uq0mBQQMBObxGzqKTmakXCRB7np7CxSHCGIhVhtzwQVZPtle_InKR-Lcu-Sf1ES8BKA_trQCy19q4ODJkdubsM5G591lcgCgULzYumHo4jjVuT3FZh6Vh2gNIh2eJGLMbcrucoh_lruO74j7K0N2gFJEAqPJFMtfsz7fWmDoCvVHKs6doTCnvoQ1Dt4QYl-o5HMy-X1Td03lDepdzR6t_hZQwv65YzjtADCRR5GuoT1MB-E_0rJYVhauYHADc1k-Fnczc2wJ3iZnQfwenMEuZGeXLewPEgiKLk98F4hR5z3oeu_1B4cKRvQldHd847ETq44M9i35w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24733" target="_blank">📅 10:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24732">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=LfGh4Qb1FgqQNSpSlaYeWAfRr7nu1zKXAicytrcfpCBZdPzQv6AF0QqeNv4x1ZscP4XPnDYefeUPShGG0QFMecWBpcrJZuu0_R-zsEKV15fTOj1jYELYIwMUHmZ_H_2PzmRbMPZLVK_J3OGp5efsJtGi-ovUYX04Ce-kbRq71d_kyeyAwd4z1nGzCFEOgXsfzVtP0mQQfM-Gw-Ow5SenGIokd9cw9WI0ew-M4S-_6CiLAYJMG7D59WwZFYS0Y4JZIQu3wgYkoOz-fRZ3fIxyZ4X92YsLlWG3UPAXffMcGX1RWPFkMy4HybuvIGnMPlqXIcWih6tPymjlvQYNEX1AoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=LfGh4Qb1FgqQNSpSlaYeWAfRr7nu1zKXAicytrcfpCBZdPzQv6AF0QqeNv4x1ZscP4XPnDYefeUPShGG0QFMecWBpcrJZuu0_R-zsEKV15fTOj1jYELYIwMUHmZ_H_2PzmRbMPZLVK_J3OGp5efsJtGi-ovUYX04Ce-kbRq71d_kyeyAwd4z1nGzCFEOgXsfzVtP0mQQfM-Gw-Ow5SenGIokd9cw9WI0ew-M4S-_6CiLAYJMG7D59WwZFYS0Y4JZIQu3wgYkoOz-fRZ3fIxyZ4X92YsLlWG3UPAXffMcGX1RWPFkMy4HybuvIGnMPlqXIcWih6tPymjlvQYNEX1AoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24732" target="_blank">📅 10:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24731">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=HKPTS-ZpHyb4kwzKGtBdwZgIM0gdPI_6js1VBfKXZXtQ14pMnR6jQRGXYYX8Bye7Q8tIbjsZ_kZvjbAZsqNNod8epCZwCETCYTeIiHGzU7FnQMGASkKCj0m00RU53gks8BSGRctoDG0lsNw9XegGtRjfZ9lGqOPk0_CUz8iaVDtmHSGkMM5r2tFZzKzRc8-tqGGhYzLvgWbKnwHS1gJ2lHWJuoTJ34QdCRlwsVF_Ta7BkudI514CWRy6i8qY7GJ6qs8Rxe8WD277klou3T49QcdWa4D79Uisw9l5LvgOt8UJzsECxsdI5zigz5wGaLJSfgEUZZ7-Y-TMHm7rArh5dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=HKPTS-ZpHyb4kwzKGtBdwZgIM0gdPI_6js1VBfKXZXtQ14pMnR6jQRGXYYX8Bye7Q8tIbjsZ_kZvjbAZsqNNod8epCZwCETCYTeIiHGzU7FnQMGASkKCj0m00RU53gks8BSGRctoDG0lsNw9XegGtRjfZ9lGqOPk0_CUz8iaVDtmHSGkMM5r2tFZzKzRc8-tqGGhYzLvgWbKnwHS1gJ2lHWJuoTJ34QdCRlwsVF_Ta7BkudI514CWRy6i8qY7GJ6qs8Rxe8WD277klou3T49QcdWa4D79Uisw9l5LvgOt8UJzsECxsdI5zigz5wGaLJSfgEUZZ7-Y-TMHm7rArh5dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فوری
؛بااعلام‌دولت؛
سه‌شنبه ۱۶ تیر ماه استان تهران تعطیله. همون چیزی که قلعه نویی گفت اتفاق افتاد و یک هفته تعطیل شد. شنبه و یکشنبه و‌ سه شنبه تهران. دوشنبه کل کشور. پنجشنبه مشهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24731" target="_blank">📅 09:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24730">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRT4bhbNTsoWeADkdFQGXqAUadln_MHohDiuU7xUSdBDM-GaWmwe8R-00fuyChhx1xouSNrGzrTsYZFTRBbtePYnPJcDYUuU7P2lPADmLG-R78hEPzoPwSwlViIqK92avRSktSJh7qVk9gFnQOp78OPnIpFlHCx3vprZLGHc2SFlIe37zM3gPYkMdHl-GNmh4JyQIuD5zutwJs1OwBjzDeC2aoYhjEHkKnFAsd3WrOProW3jJT6OHNeD6ErYpPHjx0aOMMmljKSmBAcQ1W2jpHPpPSfso5ydGQmYM3GN0ME9D1RIk58_SnI-1f3yzxW49MPhUmXe9hh7xf2057FlTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ فرانسهِ دشان حریف پاراگوئه در یک هشتم نهایی جام شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24730" target="_blank">📅 09:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24729">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlLnG1bNhiQl3qiPfKlKQsIonb-GJmVXTGAjffZecdY2ysDQlg6HgjJ5JRmGSwVB1-WA_xNyJuY0JTmm06xRZ9IJrCUSh5sJokew4X_JTUJBzl6Tj4OeHC6Jwf0SFYhfGkuhtTDU9lCXtSj94YZtULu8wtytP1lFoRTnHjUAWgJVD_PXJJqwtciX_B6BjsPfeRi4HaYnx8LqmALw1UF9Md1_3sUHNX4gzUYxZd2oGPjqjgkPjAtbyECvqp8NXcCZithvLzAXkJ8X22G5j-iifF4mbo4UFgA8Jv6Z7g7VfzeePi-pLNqbL6LpUaJOmknLSst4jDsG9WuV-5PtoIdQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ اوسمار ویرا برای عقد قرارداد سه ساله با باشگاه تراکتور خواستار مبلغ 5.5 میلیون‌دلار برای‌ خودش و اعضای کادر فنی اش شده. درصورتیکه مدیریت باشگاه تراکتور با این درخواست موافقت کنند اوسمار راهی تبریز میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24729" target="_blank">📅 09:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24728">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LO9Frbu75wZNuBlBCwFF4zRBu-qp5Ebf5HZzw4njup7LFL_OAzfdkRDBcdBDawZpHHAkPXI5IexN_arISKXIt4Gl2z7ucNLrsZvH0ahupNq6v8sgMwytlmcYqPOlyxpqyuhK0nQEvzMvbNx-w3wOcTU4xKRWVLww4pd15mteUwQv91j2EI3jRrqSfGToQP2cAncw6ZUn8ovTB4tMUb84fff3mr1uw2EFSWYOHaPpxVXYG5c77IviaihJxlfWK58Tv_blFTKwaBY8fa2AjDzaspQcz9YpzN7ORNVhfAat2-a0pR6H6MZCYQbySgCM_4mwVmDRVztlFxIEWuNqQPcVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانردهم نهایی جام جهانی؛ خروس ها با درخشش کیلیان امباپه قاطعانه راهی مرحله بعدی شدند. گل‌های این دیدار دیدنی رو مشاهده کنید.
🇸🇪
سوئد
0️⃣
-
3️⃣
فرانسه
🇫🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24728" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24727">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDD4bwVVhGqSHCB3QCDcX4tUtPspigKJzhAlFyhojZnrM0uVxSeHLVteSbjFXh74v4su3I460J8k-foOBOSjuoDoHMzox7qmoxh1Eh-n_ZOmVk-KuoX7GBukV-9rroMeEwL5xpUcGokCKa-KC2ihLbSv1iuELJ4yowsr3swj0V7MBtOJ8E0UGVcb_XWRFnYzAzTIWB1rfOpPdr-SlIYqSABdq5mUTjy9UOo7dEoc7EfgeleyXi9OqRBsgHSaSwKqWszGi0595ty7QE02ewzsxhqhGuoDxQLM6WkmV2rPJvwCRwXVf0O5_LbL14d1LSwEGEqMrafppdcOn1RNoAAM0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24727" target="_blank">📅 02:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24726">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛ از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24726" target="_blank">📅 02:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24723">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=hxOrpy9BzFKlWS0tORModOx-1TCTOrM7uB5hZWLgrNGGrTkDp4YrIbpDCR5db_MqGOsu00kzrlNIMcAsajeg0yp2Z0PGe-pHs2dp2hucHTv2h4grVYL4qoQq_wxNjZw3Nva91rVjwfVuKM8kX2s2xkyCIF1KBUz4wA1NCgk4CQn1tOVeJN73e6geEveOuuudMU6VxtPXuHC_BB2rofqDGoUROBQWt5GI23oJGt5mBAO4UOULh5mxIc-u4LjGSNLiHEPvTkrKaKpp7uoE5WN-6BdMTKEnT_er2WD_YWHC-VG4OxE1P62RCmQa0EBr4K0rsRU-AmFQns-WwpPN3c5kPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=hxOrpy9BzFKlWS0tORModOx-1TCTOrM7uB5hZWLgrNGGrTkDp4YrIbpDCR5db_MqGOsu00kzrlNIMcAsajeg0yp2Z0PGe-pHs2dp2hucHTv2h4grVYL4qoQq_wxNjZw3Nva91rVjwfVuKM8kX2s2xkyCIF1KBUz4wA1NCgk4CQn1tOVeJN73e6geEveOuuudMU6VxtPXuHC_BB2rofqDGoUROBQWt5GI23oJGt5mBAO4UOULh5mxIc-u4LjGSNLiHEPvTkrKaKpp7uoE5WN-6BdMTKEnT_er2WD_YWHC-VG4OxE1P62RCmQa0EBr4K0rsRU-AmFQns-WwpPN3c5kPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇵
اشتباه مرگ‌بار و فاجعه‌بازیکنان‌تیم ژاپن در بازی شب‌گذشته‌مقابل برزیل که باعث حذف این تیم شایسته از جام جهانی شد؛ با گزارش عادل ببینید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24723" target="_blank">📅 02:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24722">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djIiMrib_QApJD6QRxFVSFPUZEIju21VT9CzCxIvsH8QxgcKSrAi6AGYHSPeVbGVbrk61vjgyrjm3xmyJ7ZCIbAJMbFr36xOtv7NwuhsE-4NZ6_kltqoy4nOhDSFrZ6ItuuAez0Qgrrq17dKx7xCE2eltn_28lPHfhdbE1wdLip8si7cCxV_8tsLmv_FKnKBFbhSvhX95o2FPTCSct5Kj6RywraGxu6fgchUTpVuXJ821q6GMHEnZC0UKyONX0vPHuo7sC4_lOUZaTrDYP32LJT0HxSPUe9f_XQzz5FMGRbxzlVHFHrsXxQ763j6P6gV6yxzSnvwEVwUwyxIstJz4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعداز آسانی؛ منیر الحدادی نیز چراغ سبز نشون داد: تاابتدای هفته‌آینده با خانواده‌ام به تهران برمیگردیم. بااستقلال قرارداد دارم و به آن متعهدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24722" target="_blank">📅 01:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24721">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=Qyy9vQkJ32f7WKUM8ti5VMxUQGoLQRjcKL9qIFhrq9jGkesw6XC7CmqtYb5b9clKhlPMr4g1HXdGb5NT_YrEeB1LLH8z0C6NlwTu7vjC_6YwpO5TQ5ept0laTWFrpzesbiWIZ9IdEH4tYcbWvj94Qic1ksu-XFdOzIOTW1Qfj2D_REaYcVQesmkHg0B2L3NCJoxOF8rbSCh1_mlOuxnLociHylgJZR9Dh53tmSIudhi3YkdgPEx_34aDCPikVVH7ggI1gO71ApRouo3UIDKr-mG0apvGAOoh3FiwpeC1u-ov0AG8uHACa5trehVmtutbxR2jvmF8CNED3JbamZQJRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=Qyy9vQkJ32f7WKUM8ti5VMxUQGoLQRjcKL9qIFhrq9jGkesw6XC7CmqtYb5b9clKhlPMr4g1HXdGb5NT_YrEeB1LLH8z0C6NlwTu7vjC_6YwpO5TQ5ept0laTWFrpzesbiWIZ9IdEH4tYcbWvj94Qic1ksu-XFdOzIOTW1Qfj2D_REaYcVQesmkHg0B2L3NCJoxOF8rbSCh1_mlOuxnLociHylgJZR9Dh53tmSIudhi3YkdgPEx_34aDCPikVVH7ggI1gO71ApRouo3UIDKr-mG0apvGAOoh3FiwpeC1u-ov0AG8uHACa5trehVmtutbxR2jvmF8CNED3JbamZQJRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستان عجیب ازدواج و جدایی محسن مسلمان ستاره سال‌های نچندان‌دور باشگاه پرسپولیس: دو تا خونه و ۱۱۴سکه‌به‌نیت ۱۱۴ معصوم توهمون سال ۹۶ دادم رفت! دیگه هیجوقت سمت زن گرفتن نمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24721" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24720">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rI5VOUwjRLHMg_bR-DW6pCYDf1lD1YhmSzQp2FvBudVym-re1jamcfQr6CtF2TFkwPsHaHhrXTj3TolDv0NNGkj_nAYHyGJeyf_OcR7oaxyi2xc_7-hC7HCYcb9hfoi3W9pir_U1lLI387KeLOZSKZzXmDANmdUQzy3kdOIWOhBIK0JNcN8rWYnu_I8AJa_BcwPgUPusDY_3cVQSMlcbbIOJ5Xk6bCAQxzWs_fC9ADStqdkQMQIUA59Vs9KC4JAYsySSH4OeSV4BcXsEbfwbZKHeOBMuZyxNsxRyF4x-CJBvZLSrlddBOFzYvO5x3D6b7ARPteEp0Kuim05BXqvXtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نشریه بیلد: هری کین اگه با بایرن مونیخ قراردادش رو تمدید نکنه مقصد بعدی او قطعا بارسا خواهد بود اما الان هدف اصلی بارسا جذب آلوارز و هدف کین تمدید قراردادش با باواریایی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24720" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24718">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5E9MCF7hgK7bMCOtHnJ2sg97Wy8dCuYLC7jDu2qmqCZEogd3N0qIUyNQRk2-4TvQC26s9-DWJ1AyJRfDj3RyRclhsEvgYich4vJimJd_dZE21VpDD6Usgw5391TP1BH4SKCbEXwZTmEal4Bg0QGuT_5N9DAwVeJrq0uiGfREXYwZHOIBUBavQb8NsH2TwNE8p7pLuixJKprB2gAqsDrsao4ipcvxj53iYICa6LIuzPPoVJmZtrI3WafRdTz8_C1oHAkyeUctzzVE4FIuv_uOzmKcDdyJ38BejhK3rq9jlyWwz1N1lBcu09o0hHI3wzaTwT0I23fAIKFOUANby4oCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
نشریهESPN
: علیرضا فغانی باعملکرد فوق العاده خود در رقابت های جام جهانی به اصلی ترین گزینه فیفا برای‌‌قضاوت بازی فینال جام تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24718" target="_blank">📅 01:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24717">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH3w9wSlBnoFVDkZrUbs4s6FafaHi2G5YYphTTwNE1vRE6hHcuFnEeocLoJqrS604eNO1iw3TPdHQRnwF7ON5fxgZhHH0c456tgluuagk2rLfYhT8IEvSBdS-qzIH3qcYnRaI0ssHIKF1XnS38Zlo2KdPVuEZmcSK7SBM8BH6oxYEr8syKAr48FuQmbnnwx7cTPDebp-qEJBnAtXQYEmBPMRBbg7h_jKruqIOVNuHsojqPxDVJ9xv7Q0FWUhuA5p-THXNWrVPAghsIoBfa8OaEJFVmkfmZDn3vC1rtnPcXD6uFQ1Od83v2_Tv-0Pc3EwE4NLjGgMbesR9bGRRidiFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24717" target="_blank">📅 01:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24715">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bh_DibFnO3d4iojnsAFmDh51ySYs9h6AE7w7cpCZod_DgjwszKiqVuKceEnj-Xuzk2jfUWJJtonvnoVIIu7SYNYEFiec6W_fnHa-8jokqNi1Tb9e8hLdMirog8EU6a4oOQKvovbbRY6tLHFDxmg2eFyhqfbrsSwyKmrOXYwJy85s1jeddfBRRUbO9ZxsDLg89XumGlHrDLL0G-jXnYy5DfXymmErGNWU2sIDGvohZ4oxuuOh7AkHbO0isz5QIaJ3hItfgE5lWfghrHXpmirD_ia-YLAb-i3cHfbiArUIaSjwfl3pfb9TmDAgmIYG6BGjkiU0MxWmK3YFuAw_opSArA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جیانی‌اینفانتینو رئیس‌فیفا تو دوهفته گذشته 24 مسابقه رو تو جام‌‌جهانی از نزدیک نگاه کرد و بیش از 50 هزار کیلومتر رو در یک جت خصوصی گذروند.
‼️
براساس‌برآوردهای بی بی سی، تاثیر آب و هوایی سفر جت اینفانتینو در این دو هفته با انتشار سالانه گازهای گلخانه ای حدود…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24715" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24714">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-lX1aXcsmkjsgMVaLp4E56LoE4Sxm9m3Q4NGUf7_QpQiApZHOhFQPJv3iNIDsO-0EqCqOdVVmPWICc71v-K-ElMntvi6IFNlPyyXlVckuoBYNj8OJMvCJNskG9BVWalpHnCDAFcjLlHDqHBa_ktB2EGgfflri66OX2rTps9IznMgAOuJdpyDuA24F72CTK-XLo3T4Rc8s_-uvV1j9Ti6mHXG9VtZgZE3TM-fqCXNwulQ9CgEaHNr1YiNuy361epZADzVbXTnjxUDI6Iz6YBpYEWYcXBVt1yjjoRIQ3RYTp_S3Fb07jNe_n28JOm4lq0kdakpHnQtjKu8poG_f7WHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24714" target="_blank">📅 00:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24713">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o33MCnVfFhbSws4ut4rxW0r0fZfPmw-D0jK2fitiAhdB2N7UFW2Yguhducks0Gxsr_drzPa1upO2uIMxWh-VlNbdSgUa784D0MObuMga3YXouxPdF2-jz0670-thudMj_Do9LCW9-rpjVAA8jN4MKB5CJaoKQIzxBM2UH9GkUeH3fTgf-Ih3o2Tge7uAj3bXod_7X4b_REzvbcIcCIactb2kDXAR0frISVjOQnCOcPXXXtWpv56sVuC9MXHSaSxWH1HtZdpmtRRG7aFlKWGgMCHmCPb_95-PuEXHKhXP3yxg9iCkSjVuDlHgqlcAHPggrcMQR4jmZKA0kTPwZjvaKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24713" target="_blank">📅 00:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24712">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2dZ5SWN2IX5gLrSoRH4n0Ladbcs_gf65joMKxrpdlUEJaMR16h04moehd9kVZcCa6oY9zFz4sChtFJp6cPPu_N6-5-l9PlDuSq3phkSQ-u8VrMgPZsUYUm9vIoWaIpZoPeLQICqI3WwOokcirVAuo4bFuhbtb-oJnSbZz9xWbtxAuQNRNq1y4G11Dk1mRQ6ZCNO8hXI8jtR65rWO4XT2vss6pDk0WidmQBRy7lcHGO-2Ibebqqe-JQCZl6n2FDwr9L0W-NtmU4dyPI4YpVM98OWrETmbb0rZ_V9u2ZdoKgYJW2HMwrM86v7Q0wragS4BWPkVbqvMqdhDttQbpfUJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24712" target="_blank">📅 00:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24710">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fITED4O1AifjRUPlFVfu15JoKhAi3kwtJ5a1w3QHz0MCU-XVFcECUAdNgq0o8oMvYx34bne-GAav2m3IRUKuCkEp1B91uFwkc-Mum44aqTRVAJB-cVD4Z0Amx6VSvMoOYlIVTfdxmY1w3CrZBV8qBlpPgtGNgkh-7zJR3zHBcz4MfuOdym5e40eR9wzNvLZht2XmCDE5AunYFvF6x3cHMV-pwfZTSJnCD0meiZNbU5gwOXImuznadx5KELXNrSuMGxtBj6tikHj5z1LeZyEEGZlki7YMzy9W21GW1xuojSDsTWq5ORtIYxY5e0E3X6qjbaNPVmQrCQlceM918NMO8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛
از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24710" target="_blank">📅 23:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24709">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OW4g_IsQpvaRwjuusjIP7CV1al-W88XzWlsivLS0G6CsY81YarsPW2ZJyAqywphEqPMkrqv2sSj4zEBHcOgsVD5vH573XjWrIB1L014wyeqIcXm6gd8XMjpORaovusaIce0NKV2vQN__t0_9AatcxrJ-_ioeB89800nkkvpeWOmPMf9OV4tlR4FpOWwAiUDOvVBS-QrTtJasWxfO2wPTOve9zEoMBw9z6UkTZ3uhr4-PbH8emIAT6JkOjzHp5blppyCXcoHRg4IazbsEl11GSduPKB5m17eDklZcIxZpCT8iyOyV0qztTxvnIZikH3WDtcLpOYHfZqdgrY80HHUQjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
از وداع زودهنگام هلند و آلمان با جام‌جهانی تا برتری بزرگ نروژ با گلزنی هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24709" target="_blank">📅 23:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24708">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udZOKnFWPOWnp8Hgwlpl8Mh1uS9_96tRS9sF9YRVQPLF_VKOqR403BhooveB-wsUIfMKrderUUoipA6zeDulckoQpsFJVuUgPYfESQbaD1mTeTFJktD6n26EF1-XocJA5snvwudeFXQPG29_eYUfsYtzxvGm0P8iHGT2pTKaD_mUChcNXttEtgqITazSrNWJeoF6hbrEDXBZP-t7EWzMdn-hdgYDaUExPuadvMG_58hfyqP5BAruzNW30ZQ0-piyxsPssCbJntvqPfC2VJh3pj_4Cc-FGrOeRFtVajdvM6LOmk9Ix6FdB1TuzOpzJ3Lb-WmX57bI6J3VD6qI-y8Qng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
مقایسه جذاب عملکرد بردلی بارکولا و لامین یامال دوستاره‌پاریسن‌ژرمن
🆚
بارسلونا در کل دوران حرفه‌ایشون؛ بارکولا بسیار علاقمنده که بعد از رقابت های جام جهانی از PSG جدا و راهی بارسا بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24708" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24707">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnyPzk85kcLoSy5r1wyPwVROo8GL5d2ZCNavDX9ZMGInC85sjTQIFYcBa_N0P3mDWdX-UTHBOTWw8Tu2JYZ8O47hi0SqvqrKCce3JVpEsdw35J8GmXpbpc3e78lCf6SyUJHnDY_z9d7hDdMe2nYhJUvXeQ5V3S_Sia__yTBMMpkaRczURB5GgLtEpagwEk5gMKkkK6hcBaMIAXgNH1SeFfstxEK5o5T1l115imORKCN8J4rimcBnOjQCSEEjySFOhbNgNEq53HRkIMRIyNU9Wg_nnkj9MfYEwHWoQvUmwg2C1dY_k_oF6rJu-NSQFq-ciM_omuyrvOoFCEv99x9Gqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نروژ باگل دقیقه 86 هالند ساحل‌عاج‌رو شکست داد و حریف برزیل در یک هشتم جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24707" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24703">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J1DFBFixQbF047Mrc4LO_0rnIiCnbm4P-u28m7u89PMbo04RtavwEiYX9-zsGEoJm_alE658I7ri-fsREJR69uKj-ARhHrWaacfi5sN2ex46huPlGl_Dn4cKJcNjiHGvek_NH3yrju5Qn429cy3SbYAqNvDdE0FuvfdBUwIoyC-BBGWXJc42rwAuxtqybvSzLhwy3VnFVaULpj1GsCf1012FOp_CqJyHLLli8n4sNjwB627V9EMtVw5fT3ef0FteX30D_RCjAq3DDJ-kRY_8JqyTAQJp28T0eFnNpUnH4drRjPV4AWyWblxmF2S6kJPPZ1BUV-Y74ovqKYYh0pRyjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r8KoBRKwtPvYnK3xmwCO2cx1X1_PNK2fHQDAZuoMXtxsGZ2YIEZmxyBmQXlPG151xai7iFWGwWswzVJBZdzm-Rr1iKWmVeJDMGRXyEGv9JNVPyTNb0bPkoqhfO28R6-qqE5vj61NLx1XLT2NSBth61t9WmSUwh3ndwypVLYzQYYgHSV0nPdLJTW-6NyVdKcweqRnaxHbPWsXL7AYxRX0TwufajH1QtvavMzt711bQ4-eini6JkbeHVd6sgk1wO7VCrCXOETetme_XjwlHTd1coicRc3e78Z0e62IOoHXjIRqjQcGasdze4J_X1uRNWZuN9sNVMB5NiMvbnvDGnssDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدی
د
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24703" target="_blank">📅 23:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24702">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbWZ6vyb6zy-sCsanwhERFBdCWu9Nun-UAMIEIPM2vHCllcL4HP32jhzAVXbg62oVW-9hnBmS6YP-z00_4gt2evGy6E25OIjPdLaE_HbzcdzKIvEEnZ8ewbaSdd4csU3EF3e5e2Q-lcct03tdohd4x5CldZD1j0avIHar4PmUgI8Ump3x8-mHemzWj6-LEccPSul6g6QksHiGANHLtifo8MZXGEecO3ZQjWie5CQ_xozwRPWW2tNCx0ZC3GERyZ4cFohm5nrPRCzrKF7TjbBuBuiukqZdQo-byzKzUhOW9e1nlM58Btuj8OKhR48rK2FQ8QVdQ41K3z9ASKzhWFf5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24702" target="_blank">📅 22:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24701">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsNL22X0tcfiLGvMiIj5XASzOF6rbNebpsWRJ0UeoVA6161L0CKvQFXPeO7oaFCLxH16dI2CfaWM97lxGJxdgui2qrW81d1XoUTaztpCZKBqHogzZ52Ii-ADrl1WMRr08O1TuYbERrDktXDKtiNYI-dcxzOIdHUnVAypaM7Xqjhi3TumxmK-OEWvL9t_IZw4X2nfUAnno8zIcBjWVhEh9aiF4uAsjr7sg-qvbmPyWMcI5f6W1npjAx7wLOqS0Se7UvBUkoUdZ6g3A9U_neMYUIoYZIHu_c9vYF5Qj4e2r7UERaWoa4l4UBCYUTfqjjW5hplr8BS0t-EK7o6v_Xo5eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/24701" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24700">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGr5PqvpYNZ7qYL_IBcXbGueHpA3IGtJFFBavEH5nbV9yEz9iDYb-MjUtTXfQRSSIjY1RoUgQjY0t0eoC5UKrbKdoF2O-nS3Exco8DZZVtJzFKa8L29qeBg1JCKsLTcZM0P7zQZDy5mthC_hym0eBbI4XwCN-Mba4J3ZsNFUKq6gOezhHf0glVuQK6d5qEcrQQwOrb9EK2_66bSoNKoexCgsnOUxsOOOB-3jABGLzl5kFE9DUL0vztKh5Eik2u_PpsZ2zFTuNeFJMdL4NRgC7JNC971GT5cZWsL__uHL_8F8Ea3IwDd6ib0cU8m_MQ1BTl-Ok1wdr--vn3nC4mx9sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇴
سوپرگل‌دیدنی نروژی‌ها در بازی امشب مقابل ساحل عاج در یک شانردهم نهایی؛ چه کاتی برداشت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24700" target="_blank">📅 22:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24699">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISaCstL3Iy6qavtvFBaoPbLjarWJzsfQ9C1kTRJa9wQixMOcPRwBWkXkhWSm77A66_GMpfBjMNVC5m6ic_LKZdn70YNfkKxeloqfqHkOTu6UV-jY7Jlq8vjEPvMm9-Fyfqe3wAjTznqBWy28IgcdzeRW5ONb4yi_mOnBKW4Tm6-FOUXWbhGPmVWdZeW3dDABM95EyNNkqdsNA_xEKV1rQDHyJAUSj4Qw1qfX7AEcpPKSzBmKLTpENKmXc8HCnnz3wGBktsF0w2kap-gewRv8JgJYisO5B1uc6mK-4sAEdmV5-tkNCPcF2uSfKljJ7Mjgmt8ZZ-nVc13t4bMOMCscOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/24699" target="_blank">📅 22:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24698">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7eCLTe01fPTblID63QRzgFpwFYeBMXD6Lw8WVMIw8PGEqau68R-E7FEpnbX2WcdByteyUqRpkJRmgiR3D1uDn1uWykpHS1nxsRipp-iXOeE0VOiqBoRi-t2b8tf8iUoUW6ViJnv1m6YsWvfCV-ZWxDOxz_SOmcSWYT3gHr2v1sweJdBvq9BE2meYahOj_bcj6PULf2W7CvMxiHwzCzURHs0cLnfyrr6kV9cu5vtj5h9YTe1Ls9W7pMtzFwlxNuTk6E-XWPedUP1Mcs3TcZI6PJRj1yZW7g-GLrHx_-GpI8JexLSBacbgBgIdqTlwp-6POzA5OIStWdLUGRDSQx8Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی در ویژه برنامه امشب جام جهانی اعلام کرد بنا به دلایلی پیوستنش به تیم پرسپولیس منتفی شده و فصل بعد نیز در تراکتور خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/24698" target="_blank">📅 22:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24697">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=QoMWdhsQ7DdSazmdyIVTcOoI4paoNeshOqD-9toOPa4kxjc9Cx6EbjxpwTGjBxpUhwITvKsZVab1rpIdMb30KWJ4Px-zrQ737yilFxQpZTPzCh8Az64IcZPTnDxKbtvwwD0FIhn7E5dV6G3JW9oIShDY-Wq076WrA_cDnKCzcznHcMgFd_GFqnEcMuwQTHRNWwMFY9z87KO2myMxXvDBVROvcbRV_qFPbW8RL4NMAoYQEF7j-W0L0NeVk1gB_Tn3bf_Bg42-4zJ5LiuFZf90rMR4ACO43pf6bSrEu700esye2133nPvlPLZRRcPQ1CeFqV94nbj9hMGl7pB5nIKsgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=QoMWdhsQ7DdSazmdyIVTcOoI4paoNeshOqD-9toOPa4kxjc9Cx6EbjxpwTGjBxpUhwITvKsZVab1rpIdMb30KWJ4Px-zrQ737yilFxQpZTPzCh8Az64IcZPTnDxKbtvwwD0FIhn7E5dV6G3JW9oIShDY-Wq076WrA_cDnKCzcznHcMgFd_GFqnEcMuwQTHRNWwMFY9z87KO2myMxXvDBVROvcbRV_qFPbW8RL4NMAoYQEF7j-W0L0NeVk1gB_Tn3bf_Bg42-4zJ5LiuFZf90rMR4ACO43pf6bSrEu700esye2133nPvlPLZRRcPQ1CeFqV94nbj9hMGl7pB5nIKsgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اون‌بازیکن‌تیم‌ملی‌هائیتی‌که‌کارش‌هندونه کاشتن و فروختنه، وقتی میفهمه من رو کلین شیت مراکش بت زدم: این چه سوپرگل برگ ریزونی بود که زدن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/24697" target="_blank">📅 21:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24696">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/masxbuqs5csJy2eaIaQJZMGAkpbAdy-otwxUPeOFMjfpiYTAdsYIny6i-O05shyrMzKM91LaEjPuce5F-Qe0OvZZVtvzDKGGLG-dm_Qn-lOGw-WOO8Yp-45jqTHd_Mx0-n_R0GGqR1HYUnc895gQ7Q4EgfEvJaqo0Tej-i48u1BjJoV4A4pwgL5rUVybvd7UbanH4yyzWit16ooNic6waWChSVsuIVllxOHGcGd1Q3cxOfmZQFt78t1rMjkaDCzGzM-6665LuEUkDq2zscY_MJhLImhEZEdM9EyWhAbsZGpfR8FnuWpMOP7ELdIII7-rKHfitjD8Y4Hz4qimUhF8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لامین‌یامال:
شانس تیم‌ملی اسپانیا برای قهرمانی درجام‌جهانی‌بسیار بیشتر از بقیه تیم هاست. فرانسه بسیار ضعیف‌شده و تیمی نیست که بخواد ما روتهدیدکنه. هرچند بازی دیگه با اونا داشته باشیم باز هم با اختلاف میبریمشون؛ ضمن این‌که تو عکسه هم خبرنگاره سرشوخی رو با سپهر حیدری هم بازی کرد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/24696" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24695">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=HxggdeM8MktIZ4XwTI_O6NyzmxUzMruvPT3LMB5HMW21Qw7XCKCUJ25wQcZ7cqMXcM2RYl_6KrW1hxAhxfo9Me2RxEvfwGau5MIE_3aquZ_ZUG2UPP10hSqy59Rob8HzmFE9q7qXsjkR11y7aF2ozXHSh5WB84u9YUAHKehrxnGWLUHNMOrn_8c4BDC1cnihKCNHMegvaTci-Ihxy3Re7YgKGTpzPCZVhzHw2A3qOWeZvOgeAo0-AWMdy41J0gzhZuna3bHML_L40Q2gnkQDjnw9xbaiovjIt0yi05NHPjh3pHlmIC2UOTCA6kr61GAq8c4qxSpk1K-wYhAqyejZrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=HxggdeM8MktIZ4XwTI_O6NyzmxUzMruvPT3LMB5HMW21Qw7XCKCUJ25wQcZ7cqMXcM2RYl_6KrW1hxAhxfo9Me2RxEvfwGau5MIE_3aquZ_ZUG2UPP10hSqy59Rob8HzmFE9q7qXsjkR11y7aF2ozXHSh5WB84u9YUAHKehrxnGWLUHNMOrn_8c4BDC1cnihKCNHMegvaTci-Ihxy3Re7YgKGTpzPCZVhzHw2A3qOWeZvOgeAo0-AWMdy41J0gzhZuna3bHML_L40Q2gnkQDjnw9xbaiovjIt0yi05NHPjh3pHlmIC2UOTCA6kr61GAq8c4qxSpk1K-wYhAqyejZrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛ از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/24695" target="_blank">📅 21:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24694">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=Q4MZvEFYbjrS5aDwcuIpdHEnautjYS-ZJlvhENno6fRY-IioBMSBe63MnvLxCzW7wo_5vJbSPMzb2MjTzX8ZbMxzt1MPQsBbKtj0wpuMy998woVSAqw0V9PPO3AmP-r7g3oCO-YGbvYlRANRmTa0NLqxL03iq3cWjh-TKKhvl7XI9Wmyl-YBTYL_z2SfflNgeT946OfVWLPZ44mz98PAWN4rI_ghkxQBcvZXAwwQ15RnxlbdruP7fBhjxNnlWKRbJ85DoAbsE7CjkZjumoTwCAQJppfThc7t88FRfitXqysOjlQKQT6-1tfXu0plVgc1uRcGtMlPSgf0jEMgPqR3qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=Q4MZvEFYbjrS5aDwcuIpdHEnautjYS-ZJlvhENno6fRY-IioBMSBe63MnvLxCzW7wo_5vJbSPMzb2MjTzX8ZbMxzt1MPQsBbKtj0wpuMy998woVSAqw0V9PPO3AmP-r7g3oCO-YGbvYlRANRmTa0NLqxL03iq3cWjh-TKKhvl7XI9Wmyl-YBTYL_z2SfflNgeT946OfVWLPZ44mz98PAWN4rI_ghkxQBcvZXAwwQ15RnxlbdruP7fBhjxNnlWKRbJ85DoAbsE7CjkZjumoTwCAQJppfThc7t88FRfitXqysOjlQKQT6-1tfXu0plVgc1uRcGtMlPSgf0jEMgPqR3qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/24694" target="_blank">📅 20:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24693">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LThDLiHFJSSTRADOIxUpfFQg-R8NeE7eD7nPN9_a0aF47OsCx6zaTyFYahFT_PiGK5b0utn1nek8lNb2FJ3gQBpEbxmusUM4G8exxfXpEhRoaUoP4g2GFASZZWUQCd4MVI67zLJI6VjNivDs7MBGp0b8N2EDKFe2Pu0vEjkVZvgteEUgipbgf0lGRx8tLw_ZztexJO5iwV67sKV8MvaGsMygJqZEUeLS3FkSCKq2x0c4-cPxXdBL0GAIMpzc56i__FeQ81fdwEhQ62DTjMW7kKsTBSTjxQkb2hI9CbpKv2ide2tvYsiHF3ZVejN5oIa6x_z26bcPkzCgF1Pdd2jJGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور که پیش‌تر خبر دادیم؛ یاسر آسانی ستاره آلبانیایی استقلال بامدادفردا وارد تهران خواهد شد و در تمرینات آبی پوشان پایتخت شرکت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/24693" target="_blank">📅 20:52 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
