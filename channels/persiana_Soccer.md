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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 09:53:06</div>
<hr>

<div class="tg-post" id="msg-24803">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyrSigv_HDdjmkwuaLRJVFhZ5nThInxClJe1K1IZm9STjtV0ICfsT6dheX-cSVcBGuirIVJZ6GVDhlE7sNzifCtOeEJjgihueFXShiBKSoFy0Fy7vPQlY26TkxVeiI8w9I-Dfs7FLtWA-Ea8POxDx0PVyr6lzyMWG_Xd7FdSSYspdXzIEJSArEeKJt3o441ZWI9DWph2g8EXLaCtXrI6HCwr8VEm1Vh0k1PReBU8ZnzWa0lmXMXIAlOQBSpFLJBjN5dN8wYXBDZxWvBJfOILqNAgcnKvvaJSUhkZtKuSLtkMKbyrcsVgpnoI5UW399otOzZoyOlR0eHiAkMHLHOKaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
ظرف‌چهار پنج روزگذشته بارها اعلام کار انتقال دراگان‌اسکوچیچ به‌باشگاه پرسپولیس نهایی و تمام شده و فقط‌پوستر رونمایی و اعلام‌خبررسمی آن توسط باشگاه باقی مونده اما یه عده تکذیب میکنند اماامروز خبرمیزنن‌که اسکوچیچ سرمربی پرسپولیس شد. زمستون هم بعنوان اولین…</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/persiana_Soccer/24803" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24802">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/24802" target="_blank">📅 08:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24801">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8EgLi-0D4KBTNr5nWn3i-qkuCwLCkCcOa_5PHDqe0r3IBu9YKr9Kk5kSglZphEvYgB3bkAfqlGMrQtxpP8ERgSYxtvBbUY8JxZQ1Kufw5r-Ek18FynpI4poH-T4rdLbk3tKYvOU__AnZTgAb6Cyet6PuZ2NhcOcAtwJ5zHoaMw9N5xkb-QVknndpq85yRshitYkru7RjGFg8T7TQZhJuaHOhobxejCfqUB66D4HI-xwnDtrWBdJUFZFRkTUbU4gpMnwzcIA_n010V1KfmJ5Seq03M0qFZv0IOMZ6iz1b0XJ1W4WPP85TS9N8kW0akH_0nN3qAZssloF8AINcEzY2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان چهارمین روز مرحله یک‌شانزدهم نهایی؛ آمریکا هم با شکست دوگله بوسنی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/24801" target="_blank">📅 08:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24800">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVx4mGPuQ6VLm0fXVPxMijLd_LwjXpEJyYT_do0MqmMrJiXguyrs8fuZjH7I61zm-rS1juiqxN702lSguJxRvzPovimALRSgj3V4MOxmjxx2QCxTxslm59wuOBhieD19Sr9P9cfe-ydscVtY8_WMEm6YcL66R4KBGWj2zXn9m6v6hH35ofi3MxQuCy2FjhluLQZg_Eec1iBzcEjXmBm8_NcFsu7KrKiz6DUARjmkQHLOzUe82owl8sprFL75S4NZAmQ0SN5nS9Mf2Ak1taHrXGcSum1l0fQqlFfoDzfia8U0QMcKl69T8AaywnMwiVQSGOqfYYrRDgFbIioHNkSvKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله ⅛ نهایی جام جهانی که در حال تکمیله؛ بازی‌ها داره مرحله‌به‌مرحله جذاب‌تر میشه.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/persiana_Soccer/24800" target="_blank">📅 08:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24799">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-_YS1f924PRXZJMro_kvNM9NpVdoJpgux0C5Z7PzxR0Ri9jKM2KFTjEsj-Ga-gPVlIzqCW3DB2lpT1e_AoBuOjui2xz6cfPJNxMsFBGZcqwo608DDkpXYgJcoEO7R3zljoqoW_LlOohw6imzm6TNKJGxLYNlWgmLvKQyoWSdwTjmQdh41MYbWEEof2BX79PLfrzZ21kAIJiA2cvXJiJDSWgQL1ZcXqXcKlN2VqNZl4wTT1eOLxfrzZtEB-gh4bzccnSCbwmBB8XJnuEUdGGRdyFzd2qz_7jCp5Vn6JOrZVsdLc2gQFztjDMxITEwH2dW8EldywsOgNtqZyNUzsx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/24799" target="_blank">📅 02:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24797">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/24797" target="_blank">📅 02:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24796">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIokwPS7kSuo16nvDGQjCT8HwY7-vuHGJPnnMe5awpEqLrQjZKZ1pR4gU3AlCQmXJ6e8qH4J1wi4m0Fd2mz4iMdmXr5AIRxoBY_hrGNozCr8JZZRmkMOS5Qs-HscDJ18BuoZO5biNT9Qs0CAFwqhZkyQr101qX6m9945blee6xSzHXkzw1YQmLBT5n1Q3TDg5q6Z499NJAr1b1GX-_HBQMZemFCHEoh05YMUa21cdcXKqTBFvBuHw-QVR2ikkw7-8NqmCVkOPH2NOEJ2ZgYgtMIuSfmSbJQcpltrJni96YD4_AlUGfhBij0UaZUWhqYHCYsv8xPnDRPNL_fkBTeQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم نهایی جام جهانی؛ صعود سخت و دراماتیک شیاطین‌سرخ‌اروپا مقابل یاران سادیو مانه در سنگال؛ بلژیک به معنای واقعی کلمه مرد تا برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/24796" target="_blank">📅 02:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24794">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9G5DZyrdAlP_F7Qt4sNiZqHS0O0V4PfN-Rnb6mF9vfvfaiZMmeVew4CETXb2k8_fNP_x58RBNse5-01RqiuYAnM8hiHIXLjr45wcqXWRDfJf051ff8cIkfTy614Vyf4eoMpHTSM_HB6CjHghz5VTbfeQb6m8R9aM-6NbqPD32L-ajiC8rI199_nHKcLxZOb0_EbvC4q3ZXVXc1zwaJ4za_nZqbbjS-xxCatRRwRmv-vXE_riDngg5abjhlxebzPXqXKpYh8HBS4RQwsbt9WJXv3wohiP0cehVMtugRZ5BraWzfH3gZT37Y_jGXzSPmr0MVlWalof2oHPjKGfgIrrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/24794" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24793">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDAupG5wP883gbffodbhRc-GQ0FH0mSn3xPxNLDvPWdPsg9K1R8cZq88dgcDPtowwUQeNy69j5d00RPW6XQZivELgOpl-2-tzPdkAP1RRj8W6BBYOBpyKnoPVWZHcMyjjSxQgr7hOyWiU1p-bOwuwWF2y32jO5iak375EDogaDCzbwFNiJ7LTQMQPYPBAPtG5tN8s1QNn7XOkTA7J_oOmnvwBJF3kTXKIGiK3EBlLspxGoOkrbteIc5rXchGIIfjjrUuidAtPbIkBzu4DFQMJ322a9q321I4cIlPyZfpFTadCLaEuIRR7IGanz58sogTkcdTRkeyibUC2NSzKLVyGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از درخشش‌ادامه‌دار امباپه درفرانسه تاصعود دشوار انگلیس و بلژیک به دور بعد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/24793" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24792">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/24792" target="_blank">📅 02:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24791">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uf_vswQvMJfRyR2Lqtfoqhtx1vD1JXju9dtXoIF0l4XZTRp9efh-7-3yqjo3f9XFQpe8luLrPoF7l1-9_MdwN3KL2978FfQwFD_pwbnejfl6KmxyzNxDNZGwGTFYamaTfkjxflPIlML6mikr45gBcIMdqxsE_s4bIBCi2AWzLVRPE6sV6TpRW0OeRj89RBf9nIZq7J2El5n-CFchrubhVibCkJd_B3tcp8lyEVC3jJMtWMPguBF81_UlPQpSbUb2LeodhN4lxvqpLrrRXBIK_GqEKwjbkWRMwpNhmjIHDyh0DU3PA_xn_CF6dxa8VtD6BhXoqClu05Rf6ICh-6Xwog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عامل‌اصلی‌کامبک‌زدن‌بلژیک و مساوی کردن بازی برابرسنگال رو میتونید در تصویر مشاهده کنید. باید ببینیم در وقت‌های اضافه بازم به بلژبک کمک میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/24791" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24790">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBQbv9sAN2GxVTbqNtjx2zgbGo-sKGGvgVRByH5pHR6jNHtDHnHIagraAIKmAauas7fWRstL83weFDEWuzN6yvCY7A1lFLpGE6DHKtn3_qL8R5MIUgSZ6rLOFdKmKB8-fuCZ66Mqe0ry_dO-9CoypJU7Vv2cJJ8fMdtrD4eeG8V5Q_qF24LpXnXJgrfLGCTYm4wd046MByK9TH3LtuRGKlTH2fSz8cALm4ScXrCL3EcaJkESevBJcILdPkgAUIsY1hTSlZoBUruCfnWCOVPeMajg2_RZbgZCKUXCJ4e7wlbskfpUbfWQKwgQArD25_k-btcH5IgQJeZGUSaf7Hs9Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
میزبانی بی‌نقص و خیره‌کننده مکزیک دررقابت های جام‌جهانی 2026؛ سال بعد همین موقع‌ها خبر میاد که جمعیت مکزیک دریک‌سال گذشته چند صد هزار نفر افزایش یافته است. اوضاع خیلی خیطه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/24790" target="_blank">📅 01:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24789">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7ul91UFSyINwoTYKKR5X1u9p-HsjLjVA8k6bJVaj7tq8cF6wH7d3J7YCGCIeGOMxU_0hCEzwh0qPwKoIlpTg9vxZeGm0zR94P4KfkCqKQpLDKoYiCa9U67Z2XBNqu16FP3sf9l_sZrCZw7P7lxNagOxcTxOiZEWHSs8AhX4xgR9gkCBDNl3Nm9V_uqbVRlmY3oheLxg9fbJTZpCBBnZ5HjSjehI67plV0J2yZfssf4lsk447cG24Oy9feWTsObvAhLsrVIH0Gtc4B2fI4JYxF2Z8IF7hny2x5GZu_WZNiHGUAFFp9RdLJAXnmuV_FLsTHSWS2f5CPQY0WYxLExuug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعداز این‌پستی که زدیم گویا بلافاصله به غیرت بازیکنان بلژیک برخورده و در فاصله تنها سه دقیقه کامبک زدند و حالا بازی دو بر دو در جریان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/24789" target="_blank">📅 01:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24788">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy8PnP7gG0nDb6HTT_pfu3WR-x2yOnuByrJzqUEdZznCPPz4mqLipQt1CE2rA04QvZ73u85TkCts5nrMxdV6LnAXj9fhjBcUL01hGcOnX1vNuVR6dj-pozWZ7CXXaSkORxBI2UlaUoqHyzOdIIrOpChWUsQW2cgktQS2HfYlvScyyVRDpgfLrlcY82l05WKk_h6AyXULOEJpWXDCRwNR-_rapAlneoIc1X-Sc5zgBHnx8KcEN5yb-sbO1gF7VLKFfIbJUT55DUykV4OXgfgjlmptpAx_2KLLYE6yKCAZ0F8vMrPcTzYv47XTLDR-wZtA6TolSiXSWvoHikfKjorqmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضع تیم‌ملی‌بلژیک رو می‌بینید؟ قلعه‌نویی داره از چی افتخار میسازه؟ از حذف‌شدن در «آسون‌ترین گروه‌ممکن». ‏سرگروهش‌هم‌درحد سید سه گروه‌های دیگه هم‌نبود.نیوزیلندیکی‌از ضعیف‌ترین تیم‌های کل جام. ‏جای مواخذه داره تقدیر می‌شه ازش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/24788" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24787">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzOkaN0WD0ZfIuvuFJOxJsdN4H1k-TSFgDN6Ihgizf2ICD3PgigN828hIM7gH6NT6TG38l7Bw5nhn7fN-8R5jhTjgWof2_WWF1oyd6BXL3LeYIQg4QYNncuaDBIFrHAPB8ib7IXsUgedSvts-_2pFmk-Uq0UKzGkurVrZ7AJwp01L2RRLuZqESMGwsMJjLCaH-_Kg0QvKYi3jCWEAPXuQ_Ixd-kUujZCOnE4Ap5wiHGLlDdkozDz4R_RloJSQ7fN5BuEVhvx9rvTSsTDpkWC9g9mwoV-CDVFr3lXdS0zoMs_dSumbf5ouqhxzzszXjU0jhT8n6RXFbkjmUhl9K6FDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/24787" target="_blank">📅 01:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24786">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/24786" target="_blank">📅 01:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24785">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RD21yl0lRgSEUGoc7j5XX644JB10mTdlV73V9tOHQtyWas-Qz5EZ3wCuKlgfZocs0OUjLVUd6eUx-1rtiPt7SulCDrGyLMaB-s8XjH0kz2YfKHSEn9qPk1RG7NLFK5YiiTS31Upoxo8th9UcrN8tXZacE-C4cCXyDKdDgPqwbNGGiO6RzD7dlUYSDLb2JLhE6GGbAg0V0I-5icxM8-1prrhGhVipeRiP37VnDSZXESWId9HbehjE9AyGgERyY_l6EUFUe2KJyFgzyoBHgFSmvW50IF30jrDcsO7zKvia9q49VVvpiVZFiVJav96Dyx54n5VYKmyeZAnkfZA8ouO85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/24785" target="_blank">📅 00:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24784">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsuwdhKTk6awCxIv-2uOhh59lYfTSRd8ZMOk1zxAAThXcN7yavTzHr8lujP33PriakNycoReYg4FtaxRC9_nHJPqnhuDgAHiIkk4qJu40LWIRBqyCgNkgZUYS2i7sGd4on9RiMGHreYBnSL1xGoyhU98xm9z_X7UAa5sxWah2jYYhaBk8nYqyWilzjlXOo1w-Xq3b4nzlJlr3j0kp0s3jeTK9F6ZhrL21kC3RILjLCufQBwAx0P_U3PBK2U-pkKlppzGpnsVAxsfoSVeMk42L5UrQNv4eeLdBssD_djYyuK1Lkpe0qSM96fzETX3VppdykT46XwvmUiLm8mDnALnBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/24784" target="_blank">📅 00:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24783">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/24783" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24782">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQQA4p1MBoimqsJRiz5fMRWp8rXm83bLyX__c3AtD5C0sy-OoYyVPhxCydO3dQNsGaMDJBFmfmtpKUbgOKTmdqA7i9KH_Z6GTk6_rXuBFoicOXCLSEUbHwOK2HiiOsG252feYB91_y_b2vILIxdJ4wGAQOqyejWGAjJ2vqsG5VJvOqLnPFTvEUXRl4PDHaaXSb8PeljuqN8YVEg8ROVx9XylyqlYv6IADSRRCMIANNE3Jexw95Q58C7QtnWxrDufKZhw8ihmJaaoDvnH9M4_uND542V8qgVDlHD43aJNv-X2HO_5bBQOk6m34QIL5KqPMQMSJBYeZKXey3cDQsjTTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/24782" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24781">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uq0OF0aqoF0u3Y26MXkMPc69awtM8o_I-eeVvKCxVzImwLgvLDh_v7hOmWyxAo1TQA3SMlwZjuZGIPmxlrWlgUiLGeyFKyDczSVDbgkr-ZKI7kRdqs8L4fc0FAzYTniUwnBDwB0SRzRyIEtugUn4VlvK5Au61cOdba2P6MIUzvjog3aimhEtPx0CyT3_gC2Glu2x3PpUNp5N3g0OuI9em50j6MPgwUuZocPI3ycXUEOzDNlOkx1yRB50l639xiEG_oYCRf6YgB56vA7Nciflk5ruwIJVyYgSaovLQm5h_5RQxTZ7FS8K3NDR9GGc6wr-JaPwve2_vLO-PZhYM-FRdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛ مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/24781" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24780">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzljHlNgf5e0XuD1bRDMiQ002qG9R4N1l2BqFv35ZBMtD72yE6hsFlZQkcsvxTXFYN3FWPOQX6D0-XdsdhIsPcI39tqBye3b-R1H-XvFQZmf7D0-qfL-KQCsMwAZ9KcxG2njFrpYg5GGroHiVKnu0McrDIvYwb6Auyu1YnL7iWY0hOXI2-5W4K-Y6ClAC4Cw7IhjE1KjyeS8-AeDlQgKVc1kKLMhjbS1QZX6HWJl9s2W96MWNrqc0ymR5MX9G7uv4uXReeY4KlfXpsjPcWup_waBv_KG52D-jW4_zS-MKid9LjpC9HtBaOICzSdHa3_dbSz0byij6RZhW2e5jLeONg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/24780" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24779">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32137f795e.mp4?token=brhhSj0MjkvtSQS5rjBtM9Pt9joyDZ5CDmGHcCr5Jm-IUQHoez7IrR8H6ejIRU4ImvZgseZiwp-opa8pBuyTy3DzJlM7M9hR1WyIItcTTPEg9NFaNirpK-64CLgw9HPlCcwqbZpkUZDjqAGE8UiXRHnvibMQFuITIrCa8CkNzoLa3sA45Ak4jGtRTg4RAOb857N_puCSxYonHHXqdd8oxmKJGzAb0FAaC1E7Ujs6V_eJaOOEVeVrDE9CPmXuwthM0k6i-yZFpfr5ZVSBD2Byd8A59SwhPWN-G2-6zQJbfxY-GAAqycWFll0gdylIzrPQhb2UG5u2x31oYh17dBJJSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32137f795e.mp4?token=brhhSj0MjkvtSQS5rjBtM9Pt9joyDZ5CDmGHcCr5Jm-IUQHoez7IrR8H6ejIRU4ImvZgseZiwp-opa8pBuyTy3DzJlM7M9hR1WyIItcTTPEg9NFaNirpK-64CLgw9HPlCcwqbZpkUZDjqAGE8UiXRHnvibMQFuITIrCa8CkNzoLa3sA45Ak4jGtRTg4RAOb857N_puCSxYonHHXqdd8oxmKJGzAb0FAaC1E7Ujs6V_eJaOOEVeVrDE9CPmXuwthM0k6i-yZFpfr5ZVSBD2Byd8A59SwhPWN-G2-6zQJbfxY-GAAqycWFll0gdylIzrPQhb2UG5u2x31oYh17dBJJSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شوخی جالب هوادار تیم ملی با امیر قلعه نویی و شجاع خلیل زاده سرمربی و مدافع تیم ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/24779" target="_blank">📅 23:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24777">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBfuZRWkCKR3Yk55pzczwGFmKKywRPn6nOOh6VvAjWbRgnv8OLJZFunk1P7G24hytcHet70lS81HcS3V2j25xkHNVhNe4JPyivTgebIaPmr0frz7mN_C42WxPe8Xp4AAirdY9J0j9LRHmcs8s1zw9QUQtWWcl9JmL1m6lRbS7CL4bSFcLzKnx515JoC3b9gO_2atv1ocFaxcgk7JfCrgfRhRlzG8rAcjTnfJdhZziWLwNyinNJO3baaQBJqQ6rQSRl-YKGhB0KtSNCbP-h5SjJpUCdjMIpXQBzb-85zD7SpZ030Pmzi5oopzNnpTyr_jBDjtkoOSrtpZJa8TS54Vew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون: نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/24777" target="_blank">📅 23:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24776">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون:
نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24776" target="_blank">📅 23:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24774">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310289702f.mp4?token=Tb4WSiQM8fmgWUNTYQG0y_NcXLZK9UkXjvXtgo_6RRFTzKv6FZXybY-RIADN63T7Vcy_VGzryk9Xeh77RPHn-JWcnicyA9ybhN7j7Tr3oDmdkmX_ua0v38-03O6NoYtU3TpGBCgjCrAOFax473rOFRbtdj3y4BUhdTU_n0vWb66EzHuYWTOg7jrG6Y_S-EvRRTNXZu1d1ZmcqeKmcT7AACJF_IriHHGZ2SXDpDP810MXbzH24VryofJqrgnZd3V50iA9qeKCo_YHlQuODnOqlopA1PD-i4ep4m9EL_CXdV6jVHnqRextmEnNbegLmKxT3bdSjuNdMDSeRMkKKCDuKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310289702f.mp4?token=Tb4WSiQM8fmgWUNTYQG0y_NcXLZK9UkXjvXtgo_6RRFTzKv6FZXybY-RIADN63T7Vcy_VGzryk9Xeh77RPHn-JWcnicyA9ybhN7j7Tr3oDmdkmX_ua0v38-03O6NoYtU3TpGBCgjCrAOFax473rOFRbtdj3y4BUhdTU_n0vWb66EzHuYWTOg7jrG6Y_S-EvRRTNXZu1d1ZmcqeKmcT7AACJF_IriHHGZ2SXDpDP810MXbzH24VryofJqrgnZd3V50iA9qeKCo_YHlQuODnOqlopA1PD-i4ep4m9EL_CXdV6jVHnqRextmEnNbegLmKxT3bdSjuNdMDSeRMkKKCDuKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛
مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/24774" target="_blank">📅 22:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24773">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skw_O-0YYijwIrX7_THhlZAjTthf6D0Z8BDErUiBqbsZteE7ejs57bWtANtcKeBKm1dwWLpjrmQKY45IPvmEeVtCB3hYGWTLpAAzL1j0_vYpNXdSCZvWw3zMZEXwJnYR554G9T-8Ak8KQrqDeHsFjWXoUfsVtmaaAZcOD81fHI8DXRX_LTesACMxrteHzBHS-tgQXA3iiZOl-fOiA_b0dWQWB18aWgj98MWp9Jh-8MivPkGBsYpUYVFXs2mofQVJpSATTiiKenLrzX4fg7W0F615y14bNfx0-Sj5o44nw-IZlNkfb1-yl01O09TOQSfiOEGntv_tQD_6s-YFFOmAOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇧🇷
این داداشمون کل بیخیال تماشای بازی برزیل مقابل ایسلند شده و کلاهدفش‌از اومدن به استادیوم یه چیز دیگه بوده که تو عکس مشخصه دیگه:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24773" target="_blank">📅 22:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24772">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdcnwjliI6VibGR_QixqpUBtx1b8PNB8VEOn0nFXfHVi_C0Pw6fq4buMkPDjrBfZGXjQSP4-XYwNcqZlU1m2qNJyDfpEtrWRiZhPeSWi4injZjI6OSEMqZH5nL0D6mRd4wicsF-DJEXCyCDlrXZHgyVcEgU7TuqVaYT7nWNK371I4hQgY9KgKFL-OYlYML0ueZiYcUCOczt9fg3EgNG0shUCrAd-GcFCOYaTbZLJNapZNy8MDGq_9WkDoqP-C_qY-Tuf3Zz3-D8Uw9IgnHNq481KUPGTfGVVVfx_gl1Tfe51QP-e7S5XlIO3qVgjwcyjty25wL5vtGUD9c0KkVUkUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبراختصاصی دوهفته‌پیش پرشیانا؛ یاسر آسانی ستاره البانیایی استقلال ساعاتی قبل به تهران رسید و در تمرین امروز عصر ابی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24772" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24771">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=bojUQdaZRuMG4Y4-zj7aWhMimrGrXKWrX84hjL7zOgLmgwgl4TqFUZWC2hnKC3hN-tUOJ8XwqE0-WyFzYkfEhmMaAmOJMimhTZmcHnra8hkZYivIMTpvwMtE-rKwcUQu1TyxekUvlPMsf8mOcpQ7FW6nZ_ahePAmo82hc-U1HHlMqESoBb4mnNsZxSY4qZa6-BRWBXZ1dIMrICAwMb-jLrcAP3S4TpLZBnPx-h1Sew5Ic25BtqaacYtL1dkOc1_ne6RXn9d_VHdr64_ZhtM2bubrst1kGeBmxxSBh04c_ZJquhszw9uuXRZJ9JW0T733F3bol3JgLPObwGhd6-8YvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=bojUQdaZRuMG4Y4-zj7aWhMimrGrXKWrX84hjL7zOgLmgwgl4TqFUZWC2hnKC3hN-tUOJ8XwqE0-WyFzYkfEhmMaAmOJMimhTZmcHnra8hkZYivIMTpvwMtE-rKwcUQu1TyxekUvlPMsf8mOcpQ7FW6nZ_ahePAmo82hc-U1HHlMqESoBb4mnNsZxSY4qZa6-BRWBXZ1dIMrICAwMb-jLrcAP3S4TpLZBnPx-h1Sew5Ic25BtqaacYtL1dkOc1_ne6RXn9d_VHdr64_ZhtM2bubrst1kGeBmxxSBh04c_ZJquhszw9uuXRZJ9JW0T733F3bol3JgLPObwGhd6-8YvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24771" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24770">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMGvz7j3Wiy5YbvrbLfmN2MRaenPN3dG9iGL9GtA2GnfiNdEeOPfzehaArN6DJpY72fVyV6wBuaT6_RcuFysCbTaQgC3Z9TJTVLikW51O3Ry395kkvqeBWJDfrk9aLLxL9siSOb0jCBiNzjjhnU7DGxGzSKg-fmCbfYxDYTh-25i5vLXTfc6re1SQ4gaN9COke0RYMRD4mxlnffeji2OyRs7zb8hT3VshZFMcDUcb5C9pVC6ZSrZEdiYJU08EWcMdLyGVaZuiJq_Upfvml-C8itJFBWfv3E68g7zruspXSvVeqDl-ZPRbR4g9f5GprrC5aEHsrFRLBs0IJO-P37DvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/24770" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24769">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=O6vUx_rxoX1t0fSFqoqauoLYoZjtV4MIBuwB2dW4uVJPY7gohM-4o673ZIawaZhB8Yv6RFzdA2twxfJlLBuXV9SGAaA13PlbJJrLqA44x5CiKzsXIqperb2JCz7bFFEcBOnp9KDTg8YM6esttjDjCNpwEk89lWPLCCKoUvYGsnDoeTWSe3q47sgrl2ZVPCaDlbv6X5cM8Us0KTs4fHBJR8m4bLIH5NQ4mhFKKrol06NW5WDEDcQLL0ZxEu92ouKxMp7W_wW98M5VuNoAIkyZda_20ZROavo5AzXhJDbf9Ay2_6yFO74-5RjSghNtPWE8S5B6laPajRBlZDj94ME2vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=O6vUx_rxoX1t0fSFqoqauoLYoZjtV4MIBuwB2dW4uVJPY7gohM-4o673ZIawaZhB8Yv6RFzdA2twxfJlLBuXV9SGAaA13PlbJJrLqA44x5CiKzsXIqperb2JCz7bFFEcBOnp9KDTg8YM6esttjDjCNpwEk89lWPLCCKoUvYGsnDoeTWSe3q47sgrl2ZVPCaDlbv6X5cM8Us0KTs4fHBJR8m4bLIH5NQ4mhFKKrol06NW5WDEDcQLL0ZxEu92ouKxMp7W_wW98M5VuNoAIkyZda_20ZROavo5AzXhJDbf9Ay2_6yFO74-5RjSghNtPWE8S5B6laPajRBlZDj94ME2vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هواداران تیم‌ملی‌آرژانتین میگن: آلمان داره تقاص این فینالو پس میده؛ جاییکه این دو صحنه به راحتی میتونستن سرنوشت قهرمان جهان در سال 2014 رو تعیین کنند اماسرنوشت جور دیگه ای پیش رفت ولی حالا آلمان بدترین روزهای تاریخش رو در جام جهانی تجربه میکنه. تیم ملی المان بعد از قهرمانی در سال 2014 در سه جام‌جهانی متوالی به ⅛ نرسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24769" target="_blank">📅 21:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24768">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NohYysrKe_jhMTpMC-vVWKNT3qX6AcPcGOIZm7e-uJpghJ9TZ02RAwgdFJ9aS4T77Zi6M-4DM_-CV8wW-bBVPjP5qtbxf3SBkC45KBLv_T4SqXaxPX2tOfL8Idul-UWhBTW3j-LWe4SsT-TM-lmdRXViZ-Rm5vNfIS2lfOzcDKnIvZAzylIDf9S5DNzmKzyvoCk4HcXkF-6Mum67YtQE2Hg0vMjOkAqK8QXHc0FwnY-fdWDLWufa5aaDsjqMfl5aLL6wa_vC_pxJ8-Zqya_aYoEterENb8B1oIywUMJnPU_jokptLgkbCP0IzyDUEE-cRs7uY5yQI4_v7vEO3KvS-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24768" target="_blank">📅 21:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24767">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/st2N67UV9yjgIZ-OQrC3e5DS6UbdIe_glcnuZmMFRr3-RRhber0bO5AhGw3EUFFvHmOtubYaZ1S4XzkJjqhtHpvyZCoKwlBtbX1Xx9N7V54YWwKdbX0xXJx7RhzNWXDs0vKDnW87zSeJ9Q2UQ3O-QQ7K15O7LuKtUzKhwMDV35pJB8MD-4SQxbayl4fQxDwTjVx2n2kLUXCtQ4RByTdCpg8bM1Ww6skva1FHbN3ZkkemsDmfnRSCkUGDKY5whD5Toeb-Bu1Eh9RUOZXioRuRErqqeGYZHAUsZzo0TQeT2QSwrHDtNO99-eYck1GH7OxstXZgMiUPnxl17O-REkdUNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه‌بان31ساله کنگو درنیمه اول دیدار امشب باانگلیس سه‌سوپرسیودیدنی و نمره فوق العاده 8.3 دریافت کرد... باید ببینیم نیمه دوم هم میتونه مقابل فوق ستاره‌های انگلیس مقاومت کنه یا نه. بازی نیمه اول با برتری یک بر صفر کنگو به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24767" target="_blank">📅 21:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24766">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flfNJEP0b7C352A8YIXO9K_n7qUaMhOLJwx_01laffxaGb32hRzN00CmaIkzqeN_xyjwFXD0wQcubXV-b1TtjLtjhF-XYNu-JKo5pcgN253ouGVVxt9uvg-JU6dg3VVLRDsF7A9f4R2Ltsg8QMQBW9Ks1FjtB9EMuYYHugPENqjNKtQXCppS6VQ1qRp_-etroNHo3y7uRgxsFr7AMoVU0sXdnqTZGCUWh5BeRr3v15JGlvWaEYyenk6AvHV0GEBjYp_PhYtFqfXY5fGQKeeR7dDRGbbXyBhSdaWfWFolpFa8MKGPCuAl7oksatUeJ2NHTQmyF6KEHkaRDcNF6-Zh3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24766" target="_blank">📅 20:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24765">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=nhNIT0sNPY3UaFkDtTfk5HAiPe30qjSvemImNMNPQ-jth1GalzeInhdesva8X9bE0Cz7tuD3LJh44k93qSMjQ1IxC22lKKOKK1sei50BNU7enLCoMhTikXMYIow3SUk0dN5ISKJ1_y2a4rtNNb74p0JeZ2C-qsC_jBfKN-YRJA8P_VMdW3TKfkScjXyNQMjMKb9rA8VAcF-G72WnQoZmI9hBTr_2OJyVjKpSYQuKTEM_fVh8DRcaRwQtfpJOdnaB2VjZqjMn41qL_TRFLu-gT1K12h5lDxWBZRXwVbq5tnHuu184mmNmhOV_SD0VA1IQgu5bfKBzZDFgJk4gh6UEYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=nhNIT0sNPY3UaFkDtTfk5HAiPe30qjSvemImNMNPQ-jth1GalzeInhdesva8X9bE0Cz7tuD3LJh44k93qSMjQ1IxC22lKKOKK1sei50BNU7enLCoMhTikXMYIow3SUk0dN5ISKJ1_y2a4rtNNb74p0JeZ2C-qsC_jBfKN-YRJA8P_VMdW3TKfkScjXyNQMjMKb9rA8VAcF-G72WnQoZmI9hBTr_2OJyVjKpSYQuKTEM_fVh8DRcaRwQtfpJOdnaB2VjZqjMn41qL_TRFLu-gT1K12h5lDxWBZRXwVbq5tnHuu184mmNmhOV_SD0VA1IQgu5bfKBzZDFgJk4gh6UEYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش:
تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی می‌خواد کجاش بزاره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24765" target="_blank">📅 20:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24764">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJO7r1aCtoIBKJKuzxeRjnHIChtHp10LGJ_EU1u5bndLjoSDr4q7nPTHplQ6TjnzKbNVWv6nvRLn3pIOxIRxvD9Eoy4cN0ITyoj5yAs3GCoPBY63GHapHlY-lb7h55SWCmJWh_OPTBCGR_kuTqmO7-QHBxR-xajdmBJHNXAJleXUQVfj5iPwwnDoPDi6ZUoYOrVr3oVYnqByV6zD8_kjEHhVec5nmdMluj3ro5Tqr9B2Wo4Y_n0OjZ17x8dinoLiiMqacZCjl4uz2_nWarwpwgsg-iprahGCcsfw48LkT99V73oJ37KsFhiohnKThNzIdWNjhWK49nZin928OJx-Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره تیم‌ملی‌مراکش در اوج روزهای سختش دوست‌دخترش او رو رها کرد چون گفته بود که اسماعیل نمیتونه یه زندگی لاکچری در اختیارم‌بزاره. بعدیمدت میگذره و سایبری‌باقراردادی نجومی به بایرن مونیخ میپونده که دوست دخترش بهش پیام میده و میگه من روببخش…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24764" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24763">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=sEWAptTYnn3239O8AGfZdvEWOkMwcl82iZ2bL3wtNC0F1wh_T7tczjuww0Q_KT9DJLT0eBW8CseRhYY3J_jKNTSDUEhtlxnCR8njzmk96H1p6-cnMfhlutqLsKgxibn6r74yJI5OOfpqDqtaggqaYcet7TvU6crYl5oP_B75mlu_6c5dXY6sby0dU8P0k6qK8A7kkUcefCx_htuuauJb-LLa1pV23M4r__lPCd3Hew9Mh3YwoHqxntp7Wow3Eivir3Scu9sYhiyhlE3wu66a0ruLWgStefKHteyDcbvff093uuz22wvqvjvKsrsP9R0tKzD3mXH08gde3G5dTQO_tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=sEWAptTYnn3239O8AGfZdvEWOkMwcl82iZ2bL3wtNC0F1wh_T7tczjuww0Q_KT9DJLT0eBW8CseRhYY3J_jKNTSDUEhtlxnCR8njzmk96H1p6-cnMfhlutqLsKgxibn6r74yJI5OOfpqDqtaggqaYcet7TvU6crYl5oP_B75mlu_6c5dXY6sby0dU8P0k6qK8A7kkUcefCx_htuuauJb-LLa1pV23M4r__lPCd3Hew9Mh3YwoHqxntp7Wow3Eivir3Scu9sYhiyhlE3wu66a0ruLWgStefKHteyDcbvff093uuz22wvqvjvKsrsP9R0tKzD3mXH08gde3G5dTQO_tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24763" target="_blank">📅 19:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24762">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMYqkIhtZquMGsXR8VEn_wbMWq-x5NorvfaJLwq_dMwOg1VLeEUDbshlGbTuh94z4m3m9lb1We0wuZQynOoI73bw0WK3lmLSO0DJuP-eJQF4-Nhn89-WgH5ezw2gafZuRkENHz99pRBKQeXpbFsBmjTJ8P4f6OMBmU8ewtS7R9iDgpMLfz-54vXJYdxrdOCyCMC1hLlosvk3-IjvUZCmLwSHF3Qex34T7pAyhopyqYmJzsxBo1LeolutLpgkXO11dCDO9F97FHQdpUnGBZ_NudrQZKPpvGufely1AMMXWpyoudyJdUs4wvfWgMoUjW2jhUvBqGuByxvdOKX0vXd5eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوستر باشگاه پرسپولیس برای اوسمار ویرا به‌مناسبت‌جدایی‌او از جمع سرخپوشان؛ همانطور که وعده داده بودیم پوستر دراگان اسکوچیچ هم آماده منتشره و بزودی توسط باشگاه منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24762" target="_blank">📅 19:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24761">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=fzOvs1SJQlD1SrjM5Zhq_kS8ZjUZwdnsmgw0ZFWXovSnXcFOafOOGvCMNfeS7p-1C9Tr64vMiFJiaLWDrFgSbUXsewVVrh6wxaUeJRgyA2J2h4_Yd15TxbV-e_HL8JNG2CYeZCRbnvwgvflPTwD9hZRijKndKLTdLEJ9mLW_eoPPVTzj86G1EOm-1mOAC1HDCJJ5K4PzpChlSwDZ90UmX-feFeAD7v9My3Atbp6WOZyfULQzpWL0hpn5yQyBIfo2bPy33fYujE6knMf3ps-S8fkx_rpvG7B3wvwD7Beok1q_mR-ulcUMi-o2IcF9muX-v7YU-gjUSLx_TaxUUTj2pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=fzOvs1SJQlD1SrjM5Zhq_kS8ZjUZwdnsmgw0ZFWXovSnXcFOafOOGvCMNfeS7p-1C9Tr64vMiFJiaLWDrFgSbUXsewVVrh6wxaUeJRgyA2J2h4_Yd15TxbV-e_HL8JNG2CYeZCRbnvwgvflPTwD9hZRijKndKLTdLEJ9mLW_eoPPVTzj86G1EOm-1mOAC1HDCJJ5K4PzpChlSwDZ90UmX-feFeAD7v9My3Atbp6WOZyfULQzpWL0hpn5yQyBIfo2bPy33fYujE6knMf3ps-S8fkx_rpvG7B3wvwD7Beok1q_mR-ulcUMi-o2IcF9muX-v7YU-gjUSLx_TaxUUTj2pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم ملی اسپانیا:
«من اصلاً دلم نمیخواهد که‌همه ورزشگاه‌ها تشویقم کنند! هیچ نیازی ندارم که در همه استادیوم‌ها تشویق شوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24761" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24760">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTubfoEo6U2T18bfHiSDchIC_s7N0s2ubP3bEfAKsAAsEb_k3EOy2r9nwrPQQxlRxj82U_PT-kP4g0WMemqRNm-Gw--lvWu_rFyb3ITXzrmr34OIP5zs4nfZZVEiTXSJQRBJffak6X4Tl_x9bFcuiK1htt2Phq9OE52fnqPUzj35XGWUF_Rof7Pgk8gt-ITSZuJGZpNHb2653EoSLCSvG6pbGHAAP5ZyRxxcWxC1p7zcy4aQh4IR0fAfFQJY5lebHoY_e5WmPyB_2UF-NLX3GBUrnFeDDnPot9JirTSnFIulA0nQTTKzyOyNmPoXLmpwKdC4T3NcsF-4JOQJOuizuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24760" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24759">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZESOFswJX7LxRSDGe2onzRg7l-tfV2P996H84Mml-E6yIiSYy7bvNJbo2SX_h2BTDIWEvyWpItzOzs9yvzzWj8KanUZ0dFWJIVPMk12torCCEHhE65O-bDgkNmLKvTvwOwPBn45BE6OqP1wrV6ETlqzgPT_ITBTBdzEXLHF7-1epRRd0ZDt8eXV5q737lkRe_aJfFLoxUE1DwxGcHLXJk4ThtSE8BHsMprQqMN7HTVWd9jTEi4KcCYcCQL-wQJOgfMvr-0G4_NdXfPhI2bS_ryxBEXUKzqFg8JOvqXpxUQCTu2E91ksHtcP8BKDc7nSkCquUbEFvSJFYjPEwTkTRVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24759" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24758">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6ccBKfqrWgdoXSonld28hgz8WTYt00P23c769RHyQ8Ese-4UtpezbAsohtzaBucvnnRAmduAfFVq8imG85XRJaERp3IJrdsyUKY6Bv286V31jYXZQgTGX75SDXpKnPXp2LsnFg8HkY7QbmrUBURVMCt4MDC6kZ9PGx4Ae6lQejwgmFQq814R35ciAU-e78Yl713DxSHmYZ2iFrrla1POBkhjVBECvAa45ryAd2m7IS1szIZOHRwHOHKrAKhwFZizmZa7xcGVu4zZs8MWMUQ1pvm-_EJLlzwAkYjNLrshhmrUG2KJ5VqN2o_yW7RsiA9colhFhmAQswmDeGCedfriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24758" target="_blank">📅 18:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24757">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuMsApIx7XW8mU8bP3IuzIeBvGPNJ2HvTn9rVShkRgl2_Cj35eJw-0ggpulGcrT9iBwYEkbZcZCCWUpv5sQFF76aH-exSikpEASccWqMZaL2LXg--A7gr4_aHlBVRMdzYi--oeSCUIBuvb6JAAjASzvsmwEo5--weP5zCFRywu_o2Ha074As8jZ21fdSKsv16QRqD7efiFfWH2BNMev1LsRpIlZc1YTYQNm9cYhDNY3RKejj3yjDrOcTye3txZ9_-Y7UJupB4ebW3qjJfnuxoo1xpO4QP7P3ABDFshK-mz-IfO7TMDg4N1OJWliuAlcixSXXz_a9d9wrxMCLNOgUkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی
؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24757" target="_blank">📅 18:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24756">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4LRfWK5HI9hA2H7NNmwtYg8oE9m_jjWXc6N1tijKV89O6vFy_h1Zsayd9UGLdpGgoNIYN2sKKEY5YRSB3_0P8ju5jbPlpxIFtsEi8jKhrvyJ8vm3UUYTocIB_7jS7TJlN4JBLypgnEay6Z2ctm_WrmmMCb6OYW6Wy79-c833lyB3brXLk2VelLYwE1Fokj9q7_NXkZT_pbQOPwr2BA_Iu98wUC7q8fChy9F8JrYNf7bbst22luAx_7iho8x3lP_zEl-nDO6xx2Uv4p1EYavM764pdKlpXIS2HB1j1XwCotbLzsvBRDMKI852AQAQDHPw5EJe_rh5ZUAlbFioUMQqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24756" target="_blank">📅 18:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24755">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Slyfof0zmGGfp7IH9TKvwV4hgg6wbkvhfDCaI3HZoxM1SIvwNm7LTIfNisqbNEhHxciPL1xamOxE_3r0wHlcPc66JlNWUilOJIc9v_-uIvnHnhQt5s_ThXMb7TJ7J7Wd1xQuFnXQE80CL-SCVqYsQ8b0XSjz-vLDjUbVjZ-PHzAyRWn2TxJnB0ewGVYPYRdztP8dSGliMUI2Hz1MmHgIOaSNqsNStkA9mGNei68J3S_BHkggP952Aumpr7ARruXbT6ttrP7CCQIuGKqWOCqseroivggvAMsK3JJaW7EKRUL4qAssMl5fuojazAO28yJ-cThTl9H4O8ydOW0Ff8px8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌رسانه‌پرشیانا؛ اوسمار ویرا دقایقی قبل رسما قراردادش رو با باشگاه پرسپولیس فسخ کرد و از جمع سرخپوشان پایتخت جدا شد‌. بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24755" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24754">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=apillDo5-dCLXsZfTo9q3Lpw_fk66LKlAAxex5_DF8r6bRdLevteSFZKRJkP6WrQYdR2wD-TIFuZbv66m9o_wKsxc5A8yvMs-rRbMIIsZHyWqkbcCEAlM9SyIy2WmZt8LRATWKzSgRLY5mjI4nMcSU4MIjG5eXdcpoAqhSlK3lXyV8fhypFpiWF7L_D6pJxp0dOX9044sZJctbrBZxb0cW_kOBLB1330Z9gxaGvTlJ7Q8MroabAnTG1YoGtx9ftAbT9VpY-vdFQ-iv82feAstUxgXkCDS2bMXCnnWE_-BQPkKGvtFDe9IqNKy2UUy6AkR6KA_6v5amnjc3u_zg4SZZ7r0C5Mit_Bx9SwhMJEEw4BN7lK1hxS57Icdmp0TMKK2yyblpZAFgutX8qcXDME0TKozfXKhzUcTZkG-GAvA-xWrizoh9JZOG5JBb2y2iPxpu8VcmFQATxF0lONzVTk5wn0CYAoE9PfIKLDxvTEQs3kzOjMOZTYdCwhir8KbXboaaR5HBHeAMXuGTAEC6QfoIh27e6xFSe-7n5WRg7GKYprC8Mc3ZCQGGQeQV4dxPSIBJ3UTFRrEQEeyQMtetnjQUIZyD8d9_QgZRZHz31UEWPzOid1zP0BGyRYtR1WXNLa5D_dPo_F_iaulCJQda1VJZFd-V4SjBW2-FjJ9xBOG5U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=apillDo5-dCLXsZfTo9q3Lpw_fk66LKlAAxex5_DF8r6bRdLevteSFZKRJkP6WrQYdR2wD-TIFuZbv66m9o_wKsxc5A8yvMs-rRbMIIsZHyWqkbcCEAlM9SyIy2WmZt8LRATWKzSgRLY5mjI4nMcSU4MIjG5eXdcpoAqhSlK3lXyV8fhypFpiWF7L_D6pJxp0dOX9044sZJctbrBZxb0cW_kOBLB1330Z9gxaGvTlJ7Q8MroabAnTG1YoGtx9ftAbT9VpY-vdFQ-iv82feAstUxgXkCDS2bMXCnnWE_-BQPkKGvtFDe9IqNKy2UUy6AkR6KA_6v5amnjc3u_zg4SZZ7r0C5Mit_Bx9SwhMJEEw4BN7lK1hxS57Icdmp0TMKK2yyblpZAFgutX8qcXDME0TKozfXKhzUcTZkG-GAvA-xWrizoh9JZOG5JBb2y2iPxpu8VcmFQATxF0lONzVTk5wn0CYAoE9PfIKLDxvTEQs3kzOjMOZTYdCwhir8KbXboaaR5HBHeAMXuGTAEC6QfoIh27e6xFSe-7n5WRg7GKYprC8Mc3ZCQGGQeQV4dxPSIBJ3UTFRrEQEeyQMtetnjQUIZyD8d9_QgZRZHz31UEWPzOid1zP0BGyRYtR1WXNLa5D_dPo_F_iaulCJQda1VJZFd-V4SjBW2-FjJ9xBOG5U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برسی‌کامل‌ودقیق‌شدیدترین‌مصدومیتهای مرحله گروهی جام جهانی 2026؛ عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24754" target="_blank">📅 16:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24753">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=DljB20HthAO4w399M-VZdq9tHlcoRdAAzuvbmntqlp-EZZ0Jke92FSroH-XkJTmU6RSjjwRZGQ9zBZqHkaIVAM8br_b-laZbJTg_K653I__TA2oEE5QxS32XCuLiKS40wrJc9B6bJv1La_88zpQHSjldoQKxrYzW_E8O4VA7pkMUkCUjLwYXB7es0ZAGAvX8-PKY1i783FohERdxsASEIf10TIRfoMRsMv3ZgQpnNAg7oOYI659sj4onQDGDhFGIu11VzzXMIq2neT-ztiiuTYINhKPM8NRjidDCJxA9T4tTyKK1JcXCle9Uixmd7t5xebT6RzQGABjZr-8C4XANpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=DljB20HthAO4w399M-VZdq9tHlcoRdAAzuvbmntqlp-EZZ0Jke92FSroH-XkJTmU6RSjjwRZGQ9zBZqHkaIVAM8br_b-laZbJTg_K653I__TA2oEE5QxS32XCuLiKS40wrJc9B6bJv1La_88zpQHSjldoQKxrYzW_E8O4VA7pkMUkCUjLwYXB7es0ZAGAvX8-PKY1i783FohERdxsASEIf10TIRfoMRsMv3ZgQpnNAg7oOYI659sj4onQDGDhFGIu11VzzXMIq2neT-ztiiuTYINhKPM8NRjidDCJxA9T4tTyKK1JcXCle9Uixmd7t5xebT6RzQGABjZr-8C4XANpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌فیروزکریمی‌درباره‌مراسم فدراسیون برای استقبال از شاگردان‌قلعه‌نویی: اس چه تقبالی؟ خودِ فدراسیون از این کارش خجالت نمیشکه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24753" target="_blank">📅 16:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24752">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkEOAIiKCpKlGWDUhQKSQCAV1Q1JyAbXI7httDt1Xg2VhX5IetPaggo0-VeYe1-63DyIqQ5kXeOV30dSErgDoF9hcDWokQWlN9HW7yuhhF9FvTGruV8NuHY7ldhshKiuyx_mt8dyNF2iieCthzDnN8-tbzHkhRzDzyzMrfZN7CMiYVNaxO29VyTVSHzdQj3u78px-0XmfLmhfghxGWlhJgM6g3UIDJ1vehUaMwGleRL0J3JUiBbMvQNhLOScbgNqxS_IVVUATZVsDWQUodX4bSlNAjS9l89dRONfFFvGFvq1qyqd3QsSlrcilgIE4caRtK540TIV8SeG-ZZjA0NZbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24752" target="_blank">📅 16:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24751">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=al6s4nBYT3zB0BFr0KUXGUj4JUYUpzX6Dktb6r0OjCmWbKe_cA6hhOVuRqe5WeqqapgOlVL4aLzcIkWIsgRnzt4a9h_p_FhqFeOWzLFaDoKXRfR6aKWLPNSLDEau4uPXWYv0RHWo0wL4j_6m-vCXsTY_3oQSihSANSqWn-g_x3wqeWl2DNSNKt1KqvZleBFxcRHOJDm_5L9en7PwUQTtFYFewqQubPs67AQjCDHxlz-0e7VC0ES1AAcCVHJo1BaqcNTHLGZkuZhuXxucWg0Q5atNbsIhm3yslNvd8XHaNnD91iRFVG0LD9cIeqjjhm4HlbvqXLfrT-YQIRQXnvyOYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=al6s4nBYT3zB0BFr0KUXGUj4JUYUpzX6Dktb6r0OjCmWbKe_cA6hhOVuRqe5WeqqapgOlVL4aLzcIkWIsgRnzt4a9h_p_FhqFeOWzLFaDoKXRfR6aKWLPNSLDEau4uPXWYv0RHWo0wL4j_6m-vCXsTY_3oQSihSANSqWn-g_x3wqeWl2DNSNKt1KqvZleBFxcRHOJDm_5L9en7PwUQTtFYFewqQubPs67AQjCDHxlz-0e7VC0ES1AAcCVHJo1BaqcNTHLGZkuZhuXxucWg0Q5atNbsIhm3yslNvd8XHaNnD91iRFVG0LD9cIeqjjhm4HlbvqXLfrT-YQIRQXnvyOYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نقل‌انتقالات
|شهاب زاهدی مهاجم سابق آویسپا فوکوکا به تیم‌جوهوردارلتعظیم قهرمان فصل گذشته مالزی پیوست تافصل آینده در لیگ نخبگان بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24751" target="_blank">📅 15:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24750">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‼️
دیگه وقتی سرمربیت اینجوری بهت تعظیم میکنه فقط یه بازیکن ساده نیستی؛ کیلیان دیکتاتور
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24750" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24749">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=HpoDLoY3Af2rr0wB3oeHLyTGJrD7141LzkQmci35Czk1-d9WoJAyq8DqVZ9lybxcPQqmPAgZn2vqXgF6B37TcQiwYN6BuRO_Ls7hWXj9dPDYscAPOBfSprXbrOBy73hIUKM7iPT4BCGMhHbgzR5UWNymgipXrhsVouQ959Q6TNYWyhzYpWByCx-bCjM71L4o9eWXYJTbZ59HHUbZQALdVdjuux8U3Pn25Uuk9rMIognFAo1h5IdrKdi5sjEImfoAKj_wAW_bCmhOCDFkNoPT8Y9LmZ_ndlqj7XM4dPaj9v-Md128fj9P6i8EVYQdbUxKzI66NFVQO7bkwcdW10IJ_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=HpoDLoY3Af2rr0wB3oeHLyTGJrD7141LzkQmci35Czk1-d9WoJAyq8DqVZ9lybxcPQqmPAgZn2vqXgF6B37TcQiwYN6BuRO_Ls7hWXj9dPDYscAPOBfSprXbrOBy73hIUKM7iPT4BCGMhHbgzR5UWNymgipXrhsVouQ959Q6TNYWyhzYpWByCx-bCjM71L4o9eWXYJTbZ59HHUbZQALdVdjuux8U3Pn25Uuk9rMIognFAo1h5IdrKdi5sjEImfoAKj_wAW_bCmhOCDFkNoPT8Y9LmZ_ndlqj7XM4dPaj9v-Md128fj9P6i8EVYQdbUxKzI66NFVQO7bkwcdW10IJ_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یه‌فلش‌بک بزنیم به این صحبت‌های مهدی طارمی بعد از دیدار ایران - ازبکستان در کاپ کافا: اگه تو جام جهانی پنالتی برای‌مابگیرند من نباشم کی میتونه توپ رو گل کنه. جز من هیشکی نمیتونه پنالتی بزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24749" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24748">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIW3jDuUZs9BrLKjByglbxcO3lMP2yFUAfiBH1QqC5MaZd-f3QcwFp18OFupOxe5eELXclLyzDhVqNZpfDKdvs-U5WJwh75uA_PS8-iv1m6cWKsOPQZAUrISNMeZpYnGmXYM8QvBfclujAe8Bz3aZoulMVRmTmY4EgPRCGwMJHsimaazI-8HAQO8nGJ4R1VnzTW7D0gUwpxmlnQcHIV-ZLPySpVsgz2UtUFI6KKvipiXQMRez4Be-Nty6a8VHdpQi7egQV7kkINUDbQSu8mpJKti_IZhbXjFGNo9obbjMRB8EYGpKAwy6b7fnxuGQKwvnPWmMW0q5hLUlrePeYxG-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرمربی اکوادور که خیلی عکسش از لب گرفتن از همسرش بعد برد جلوی آلمان وایرال شده بود، بعد باخت جلو مکزیک استعفا داد. اونوقت فدراسیون ما برای‌حذف‌از آسون‌ترین گروه مراسم استقبال میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24748" target="_blank">📅 14:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24747">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWUBM6hsMxatR8KhtTqlt97uyWy4dGLw63T-rmB_FE9xeFnZ85RsMJRxVkFN3579CHIDOIJEAvqZTFY08bPFYTLNeownfpjqhGM7c90pfpB39y1A3groQhpPwbEVWt4bRlN9NY7y6eyX7_5WmlfAdX1pk_HXOONnPDZInqafeJQP1rPAYsDf4benRK4cVrXxu6TlrgkVwvyy-itH4LJRiizJQmvfVzgB5fOpbD9y2iBleGOeilv57Fm7wZ1e0230wj3HR8rWiwH9VNC7pPETknEf9Nx9ZBv9UhxYVLW60KT6T6CPEVM4PwZzZ41Oa1WTtAlcrPcY0oG5eQQ3tpMNNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24747" target="_blank">📅 14:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24746">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSZ3smKB6aPbJAULJ2OcQCj7LAG2Ok8mGH6yqD9IkfQOL2GCukcZKA5e6KxjpS3pV2r90GZGV9iLs9KBS48hQKVM9Fi8DJv98-FBgivGKh5XF_sUHU4aJ2A4nYafzbvkG-O20V86GaQs_Z9ljUYdLLkp6JOezm7sxIV74KweQT5IKv3lXe94-G0BB7Guht0yFUzqESllSRl0EE9g2oNdtYMfmyVWolUPOP3fX_8L9p5k7d8jmT-T1tawzueF3uIxLZZ8cf7OMtp5e_hO8kNAJrBbYAV9NoeFCEWtQi4GAd9fQh6vlV-7p6qgeSxluB_W9LcwLvjrvXUcPm7bYTqqdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان با باشگاه دورتموند بست.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24746" target="_blank">📅 13:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24745">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAonupSh1nm12O4ijKK-wbYkFQCWRDeGmRTepS-kk9RzUqX0DZNrtWPW14B7m6hwZfLxjHTdgBjHSomwAJUGKcWx4IA8K2SrXru6cROk959v3RKD3w50Mr7DhkeSoMUt5bGDfNydv6zHy3kVs1qyfNjJr6a8ED6gMaLiXOgFJ35M6e1OoTaYb6XhtxFuh-5Q_yyAAE8Pkt8XeLtaZM-KDHatiGDB9cO5biqHwpCRoZgtnBQBWofhuOz5oy3T8mO_Dko2bFrDxZkucNRCxKFxeXYTzdZ2CdNzJQrQeHvTojqy0uoJZIhG5UJdwHNQzrn9_cjZUaPR3hcA7vtVxKOTXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه‌بان تیم تراکتور از شهریور ماه سربازه و احتمالا راهی سربازی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24745" target="_blank">📅 13:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24744">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=tfI5dfqH_SmakmYI04xpcqK2ImdxbdN_J0yv5bEO3yhKaCqEPMKlPBbxJxiM8d7nP8rHNaOjWMbq29gRb4j-LCyCHTZuxLnVecTQUvWY4uGQ5-rkuzvlZRu287eryS4ys_LT6Uc1AVd6z9mLV1JxTXV7In0h47f32YZi0YZM2Wklv7suJGhUumPH31dCtOBy8KwmnBDKWgt17Bz7welSMT-LNLWf-172kTnHcQCOYG7h9LwG466NDE4Abpx36X_-pPTyTWdqRP1dS9jfYUjjzaIAkJU2MndlZN7HSzMOXDx4dUorg3IVPj7QubA_9MOGmAYoAJDL5sbUDcO8qKY2ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=tfI5dfqH_SmakmYI04xpcqK2ImdxbdN_J0yv5bEO3yhKaCqEPMKlPBbxJxiM8d7nP8rHNaOjWMbq29gRb4j-LCyCHTZuxLnVecTQUvWY4uGQ5-rkuzvlZRu287eryS4ys_LT6Uc1AVd6z9mLV1JxTXV7In0h47f32YZi0YZM2Wklv7suJGhUumPH31dCtOBy8KwmnBDKWgt17Bz7welSMT-LNLWf-172kTnHcQCOYG7h9LwG466NDE4Abpx36X_-pPTyTWdqRP1dS9jfYUjjzaIAkJU2MndlZN7HSzMOXDx4dUorg3IVPj7QubA_9MOGmAYoAJDL5sbUDcO8qKY2ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاویر ارناندس ملقب‌به‌چیچاریتو که در تیمایی چون منچستریونایتد، رئال مادرید، بایرن لورکوزن و وستهام بود، از افتخارات میشه به دو قهرمانی لیگ جزیره، یک قهرمانی سوپر جام انگلیس، قهرمانی در جام باشگاه های جهان و قهرمانی در جام کونکاکاف اشاره کرد، وی به دلیل طلاق از همسرش به شدت از اوج خود دور ماند و دچار افسردگی بسیار شدید شد و در نهایت سن 36 سالگی از فوتبال خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24744" target="_blank">📅 13:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24743">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajXK645QtmV8iScg56FtSIKFEtYY7efztgvL166x3PO6vboachpoLoZJHMjxmujI_BuacYo-cQzZkBmlD2RjSM4oBhok9hsjt-M6GjazHfGyUptDlLhEjxrmakqduxSlNl0zjb07RpjlHiFKbG4-k9Lpgv-WD2bt5D7S8MKyCOhHeAkhSL_zdLfHlmEsPHzr5mCqjfC_0w1VlRQvAxGzQr9a2_UbgBAZsh076LB5vOHHKj8tWR204nrK8RTlcMsEiNcI6CCJM2mZ45pHsTpSkh-nT5Qz_wdAPt7V832uN4lz-ZbnJp4q-tbNv9T-xPFNAwR1sc51V7iXed8E5g_UXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24743" target="_blank">📅 13:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24742">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFhC8cdBZzIXqjTesjEeH0FKxrf6gF5QhLY_WQcbSImrQ34KofLvHL-OinD2KVHaUvOUR_bN1g0l5WenjPekf2rpNRTYC74jvzRP3zEqzqVpzYwlI2en-ToImujgQjFhU8lKGp8SomPxX3-rWtxy5oVj-ESfRizTwQ9r2-jEnX1L89tMNA1TP8Fizc0nokN4-piaFV259yKt_P5c3l4VXa1LxPoHn4UHs9-q8G0dcEtbS-ZY9h7YhkfJm2lcKgHfk1stgfOMnyykeIo0-XORyM5x9R4ENjxo4WzhCj64Uev6X_hGrJcQnBh7AcxvUVvmpWC-xdVVIK7Y3XCf2-YL_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره مراکش در جام جهانی ۲۰۲۶ و بازیکن‌باشگاه‌پی‌اس‌وی آیندهوون که اکنون در آستانه انتقالی بزرگ به بایرن مونیخ قرار دارد، مسیر همواری را برای رسیدن به این جایگاه پشت سر نگذاشته است؛ او در ۱۴ سالگی به دلیل اضافه وزن و عدم آمادگی فیزیکی با…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24742" target="_blank">📅 12:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24741">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=FnD1jxMBEBS-ilwLhS1Ex0_oeDoG6hGLNY7Olm0ZbuNiITkJzSLFLvtttToSUfOBP_ECfKpouVKNysxeNJD7r7SNvZv0gPXtQfI7WbtX4q1fodP4ZT-A8wwRtHZJu9aHRC0ydCqHd9yB5OMt2ZsUNp5rJjl2NWLwW1iLd6jEr-HsdgTUtNwJxy_oUgQI2CeMjTfwQYZ9nlroidze1tSo4TqV-S-jshLF2DLBOMDb-TV3NmXIXH9PAekmTcJ2705oLOpt8WpKgiG7g9LbxfFgXGfCqTwjt9hO1huQbblc9TAVD76Wyu6a46ZqfuDwRCuKvjZlNoUjRkyY0l939TXqMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=FnD1jxMBEBS-ilwLhS1Ex0_oeDoG6hGLNY7Olm0ZbuNiITkJzSLFLvtttToSUfOBP_ECfKpouVKNysxeNJD7r7SNvZv0gPXtQfI7WbtX4q1fodP4ZT-A8wwRtHZJu9aHRC0ydCqHd9yB5OMt2ZsUNp5rJjl2NWLwW1iLd6jEr-HsdgTUtNwJxy_oUgQI2CeMjTfwQYZ9nlroidze1tSo4TqV-S-jshLF2DLBOMDb-TV3NmXIXH9PAekmTcJ2705oLOpt8WpKgiG7g9LbxfFgXGfCqTwjt9hO1huQbblc9TAVD76Wyu6a46ZqfuDwRCuKvjZlNoUjRkyY0l939TXqMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ته این داستان شد عزت یا آزمایش ژنرال؟
امیر قلعه نویی سرمربی تیم ملی در جمع مردم تیخوانا در زمان خداحافظی: خیلی دستاورد بدست آوردیم، این عزتی بود که خدا بهمون داد؛ وی پس از بازی با مصر گفته بود گویا خدا دارد من را آزمایش میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24741" target="_blank">📅 12:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24740">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJ7LQcAfu7ZtopVhGVYuBnqdtw2sNQYTYpup2UPqWvgUyJCEpDbhTrk_DsyScSUNuPCQXASkSvdMLcKbX1WTCXlT5MXhmul_LhcdzK4-Zzsm_qPYl1jVCqH2L1xrhDcw8pwwph5grHKyUe2iftp4y1E_bRwrtBX12Pc_g7RasMPfO83kb2-6Fkw35fhqXg9ZuKJUd3WbZ2Vg6Xa93ocxNJGXKrT_W-z-tgZLRi3Qz7JXCqSEJvXiqxhQS5qUFsDICZmA2rIbosMRSdbh4bOHTi2aHYgvFZtpb7yydmYOQjbnzk0d4iOOuI9AxZHIVJQkQi_IEk58Nq7Wcg83us99zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فابریزیو رومانو: ماتئدس فرناندز که علاقه زیادی به پیوستن‌به‌منچستریونایتد داشت در نهایت با عقد قراردادی‌چهارساله به تاتنهام پیوست‌‌ فرناندز بخاطریونایتد پیشنهاد رئال مادرید رو رد کرد اما به یک باره با رقم فوق نجومی سر از تاتنهام دراورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24740" target="_blank">📅 12:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24739">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-Fzueujk7yrjTLRHmGtKWp6266bxCnkblG_SXfcBuyo0a2KaOiyvxgCnF8fiZ69b4kOsFR_3aJOQC54-hOm5hHpJ6duizExMLVNBmTDViMOXGvrcpoRWmqTsuInv-E8MC15YeCgthYaNnIB0lum-XTaHm8n370F6s569kqMG2kBD0s8mxIDWolTB1G7sh0hEA0VyIrWdZPZqNyohdnxy1ORPbdd7daRG7SDW_nCRtFI1IErQlXlMlCqnP8cnxc0LrQQsV5doNHEMcGYM7cuVKxWpH8Bz4t-a2noi8xkhL8n1gQmQ66W3rURnKtfcxDp0WgLr538TE8y1OIb55v9lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ سال 2016 دقیقا در چنین روزی؛
باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24739" target="_blank">📅 12:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24738">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WG1GPLDGgQUj4lVwXjH_pg7sKVNTK695Sykl3RPhQMpditGxTuOUtsvfic2MNIm0Go0Ex2VU3mnEZmqRVqyRbfbp1t1g4SxK4i6Od9NkTt5PX9KpTCiFeweXzFG6eJtWIAp75BkfEgoGJ_NiB7_xyAzia1ZTmlLGnY-7Td40G6Ct25V-KQVVOdGPEuG4vzE3Ma_1nGLIEwwWZR1cQ7AQNxGlXRu5JXbl1JRCgc0yoHdS77lHOptRKEkrxqBsCV_B3om88YTE-zHIVHehm0KGWwqNm8qR5qMFYFrTAfTOYAO0hfUSvwOtTeZ4HlwpV-M50ollPjIua6qwtZv20V1Q-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت:
کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24738" target="_blank">📅 11:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24737">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjUY-bhmdd81A6Mwu0VB1_7Yp0LMZ6qFIbphUHXViZJEbZtmAG90_eKk1gfU1fUGgQbv1TY2VvRg6qANmhOKqRruEvyjpCudxgkpw1BhugSwtk9xcS-YUjcm-KMmfCkrX-lunyNqk4ivISShh9M-dXGSAFDOGEDFYTZOA0h_NuXyyv0jDzqiPXBqrWBe58oJfBoIPZ_YI_etDXwAKy5WKUZpaVOjAK6uX6w-W9bLA7TVnnu2AISy-VhRbRtzpCuOBHXpif6KAr7yugeuEFMP5CgnxxcDW6_u_34nHLGyzDy4zzOljqZ4qlAH_zLwPTofjXou6uRmqMBnw-dzUH-V2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24737" target="_blank">📅 11:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24736">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=DWSE-vQObAV6R5UR7CVXAdbM2EkCjUiU0FTzu9lfxT1CLV3tPJnnjFtz9brbguq2v65xNwWCvCXDtTgTHKpz0QLCi6k8BjbxQ2Q5Gqck9Vne1wknSLYBeUX2bcXlDxVM0qFMBa53rLUeN28W-UFYgDQKmtV849j5mrwI7aB_ZtZwfyspIl8JggCdhUXAZHHu3ItKZmiWC85nxL_jYGLG1D1NRKbKvR165uqS4USMYeuIiqCZYu2cRsnwVvOSRRcwM-nGNefxUmsVxszMXAXxVK45WtGpDyOjPozLhGp0_wCoXRaruzXMT5CQZ3HEKakcTGF7A8LnEmYxvQsB13r7Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=DWSE-vQObAV6R5UR7CVXAdbM2EkCjUiU0FTzu9lfxT1CLV3tPJnnjFtz9brbguq2v65xNwWCvCXDtTgTHKpz0QLCi6k8BjbxQ2Q5Gqck9Vne1wknSLYBeUX2bcXlDxVM0qFMBa53rLUeN28W-UFYgDQKmtV849j5mrwI7aB_ZtZwfyspIl8JggCdhUXAZHHu3ItKZmiWC85nxL_jYGLG1D1NRKbKvR165uqS4USMYeuIiqCZYu2cRsnwVvOSRRcwM-nGNefxUmsVxszMXAXxVK45WtGpDyOjPozLhGp0_wCoXRaruzXMT5CQZ3HEKakcTGF7A8LnEmYxvQsB13r7Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه‌جدید آقای‌امیرقلعه‌نویی، سلطان اعتماد به سقف بعد از حذف از جام‌جهانی با یه ادیت عالی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24736" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24735">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=AHAZiAnyR8eoNc8zVkwJk1IyQtsI7d9X5pguOQVJarUEURcRXgoaoyEJuvB_GHA-79nV5VW2wrMWg97MJ_KBVbrgNLimQVRfHzm_B8FrNpv1ZXkpTxcFc82UTqh-8fi7rPND3UIBSeWpBQltWYxKxuzXD_NRxqSinEVFJE6i3u3DU8vUusV4QWUWs_4wjfG4tTFIrIFY6DW_faxeNAZoX-JJzV3T-o4YDeilKvFXELybXcDzowGNHdIW2Gvn18qF8gBYlPi2CX6gjl434oBbZv9U1wAt9pAPCt1oAtAUDyy6oi2VIUOSGjZBS1fsESYBhe36EEm7ngfWO32aUXKWZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=AHAZiAnyR8eoNc8zVkwJk1IyQtsI7d9X5pguOQVJarUEURcRXgoaoyEJuvB_GHA-79nV5VW2wrMWg97MJ_KBVbrgNLimQVRfHzm_B8FrNpv1ZXkpTxcFc82UTqh-8fi7rPND3UIBSeWpBQltWYxKxuzXD_NRxqSinEVFJE6i3u3DU8vUusV4QWUWs_4wjfG4tTFIrIFY6DW_faxeNAZoX-JJzV3T-o4YDeilKvFXELybXcDzowGNHdIW2Gvn18qF8gBYlPi2CX6gjl434oBbZv9U1wAt9pAPCt1oAtAUDyy6oi2VIUOSGjZBS1fsESYBhe36EEm7ngfWO32aUXKWZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
منصف مثل سید مهدی رحمتی
؛ ارزیابی حضور هشت ساله کارلوس کی‌روش روی نیمکت تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24735" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24734">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U61scDi-yO4BcBoYLvgWrJpdaQUoohh5u2498YPQPGyg2d7zppUUYhF6ULObn54jQwhmBhwYJDhhYN4oUYpzamUhsvLS8vDg1RmQ9rjkvd6aYjv8jCjwg8H-8oAvKjxhX8ChbRwYaqKozIvW8nh0HuCr7UNNKNU4ySJqt8x4_56PljM8wWoCMZuk-VigsuWn_BMfuCjP6inXEdJXlW15xVAyUFIkpAIXHIavy86klBwSnJOrFXKsmJ24awW6zpOxSb3u7SzJVUbD9AaBboO0UvRxR3pW6xOLnDRbAp69VF86ncp6nHvUBM8IV3sfiPjl6UXJCc9_s6l0pbo00quRmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24734" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24733">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o07e9JcAH2VMi-tkJGKHCj5GctZpafiJT1FKs32pYJw5jkpEDRNAeHWwEZLeP-QewYmu14aK6jT9y26pKPFZ787kLig1CZnhiYJIWOMl1driDnzouuFBECxtpmJBNoeZ0GT32Bhxfw-hthXu20F-BpNC4DV0ZsEjyJC3ffo7jUzAdwO8gABkhdyn2feWjz9caHqcRYNYzpuyZKsZJOTb2H2jLmW0KKvzUYjP20ls1Fbg6WTu_QVyetDcWY_TeuYJzSwwCMZfiGW3SQrIo2FWDsCw6iq7P-ykGztEqyCSvDDovO-8JpKRXvZqbG3V-v7LNGj6wCRSWL8c1pM2wo5mUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24733" target="_blank">📅 10:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24732">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=knlJC7asaJenm06RYGNYvX8rugjRP8LALp6T76HUCdSC2RumCi4iTYHOKGSL68p0EeQyf5ZADwOepmkOaXWGOy7EUvK8qZWhfs_OktdKvkHY2CyaXAOl4pOjoMjMtNtH26IIrGbD-CPPBIEhFiyXbGHxu5ubHu-Afrbx8eJOkM6_ZYl9zRVY0Aepk5jRMShNyk0AFzq0OSKD_ru3pd3HHlZcsk7UsdusH0s6iCsXqcRdAh927es2_ThCKTAPscS7UEgpCgVQKLQ8Qa75e8AtyUacLiMdqd0txICgOtASghSz6w2abRBBkj9dbAnVkQjSataFOjmm6fWaDhMNywm-_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=knlJC7asaJenm06RYGNYvX8rugjRP8LALp6T76HUCdSC2RumCi4iTYHOKGSL68p0EeQyf5ZADwOepmkOaXWGOy7EUvK8qZWhfs_OktdKvkHY2CyaXAOl4pOjoMjMtNtH26IIrGbD-CPPBIEhFiyXbGHxu5ubHu-Afrbx8eJOkM6_ZYl9zRVY0Aepk5jRMShNyk0AFzq0OSKD_ru3pd3HHlZcsk7UsdusH0s6iCsXqcRdAh927es2_ThCKTAPscS7UEgpCgVQKLQ8Qa75e8AtyUacLiMdqd0txICgOtASghSz6w2abRBBkj9dbAnVkQjSataFOjmm6fWaDhMNywm-_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24732" target="_blank">📅 10:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24731">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=dwBHqK81MRxiRDO1U8vormfEyFnzDyLBzSUb7xTRGHT2jlN3XdhL5_Ivuyfvl3Nhvf-7PFNk1B68HRgirVUUJ1qJlHuyaEAKRm6EPrHGk7UmBGbLgxl4EcR8e9Hi7WftTmh960aXyyLg7InsQZdNWqNNL2eOwKcs18XaRhj8dS6ET0r-05NZijpxe-Nt7eC80fY0M7GhY7KkkdLuW4Ihv_IiDz37zB4UWpdFGMl19pcFWu02dUcEtmoIxUxcXTMUrZ416qN6dPD9RUmJRA5lQd4kYNcfbv5vpu_RzYqB1NT5_UKsXrlEgUIZzA7UjBGCe6genHAB0ovZ2dfrPZDMOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=dwBHqK81MRxiRDO1U8vormfEyFnzDyLBzSUb7xTRGHT2jlN3XdhL5_Ivuyfvl3Nhvf-7PFNk1B68HRgirVUUJ1qJlHuyaEAKRm6EPrHGk7UmBGbLgxl4EcR8e9Hi7WftTmh960aXyyLg7InsQZdNWqNNL2eOwKcs18XaRhj8dS6ET0r-05NZijpxe-Nt7eC80fY0M7GhY7KkkdLuW4Ihv_IiDz37zB4UWpdFGMl19pcFWu02dUcEtmoIxUxcXTMUrZ416qN6dPD9RUmJRA5lQd4kYNcfbv5vpu_RzYqB1NT5_UKsXrlEgUIZzA7UjBGCe6genHAB0ovZ2dfrPZDMOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فوری
؛بااعلام‌دولت؛
سه‌شنبه ۱۶ تیر ماه استان تهران تعطیله. همون چیزی که قلعه نویی گفت اتفاق افتاد و یک هفته تعطیل شد. شنبه و یکشنبه و‌ سه شنبه تهران. دوشنبه کل کشور. پنجشنبه مشهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24731" target="_blank">📅 09:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24730">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHnk5t-eQk0xfs-QRDM8kJE3YB_fX1TARTvMCBqFGMTMgGPxBHpzjrU4NLhvUOesyR6o0x_AmYLnDjxFRjz9jan2vKcHYDctBnJlVpaW5-0ocKcwdJinljN5oPgdGq-nceveL4jd_wrjqB6iBM2TIjyiHLfIYJH0mOhqSxtRl4w60DVmSN2MR4PIRbhBVXw79uXj15DLKTqU3LpGQPeDhcNBf-WFsFxxbwX55m_oJxu-INfo7UQ0zy2a57OzzwsBYDvtTHGZ3jvm2P4ORkmTk2zj68LNVxOY9aUoGVme5nLYyPSMCJMP7X8lc3s595qlZWuG1FKAekpo8Mxkz8F-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ فرانسهِ دشان حریف پاراگوئه در یک هشتم نهایی جام شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24730" target="_blank">📅 09:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24729">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMHUyNQaIZOK-AjNNoBFhyLiYfOgQ0590X12BvHyzngDmQ9gvNOkfi_tiNKlz-0M48kVyQx_7gc_Z7Cxhq9Ml3NhhSMSkNoFRIyRevU_-ASTNOB7CF_84QLq7InqLrfOVht5aLR9nEPNHLQEXeH5yYkA0O8tZZyu0Rj7Y3y8xbSlMFYPGs9y921WleP4QV3T-Qi2DC69iT_b74elPMAzDm-6jBbiNzBXso7e-U6kChhpCJTwOD7eThyGmM89L-YBhI8Izm5eUMJyVToq22y2LMo4rv3Sym2s8aY5uBb33_k5_q3hrXZoI64GFJfJR0pJhfG3dyv5GLXKoLiQ9Ws2NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ اوسمار ویرا برای عقد قرارداد سه ساله با باشگاه تراکتور خواستار مبلغ 5.5 میلیون‌دلار برای‌ خودش و اعضای کادر فنی اش شده. درصورتیکه مدیریت باشگاه تراکتور با این درخواست موافقت کنند اوسمار راهی تبریز میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24729" target="_blank">📅 09:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24728">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dt7ZXEq4CF_dci4bdmD6ElmClDNRfwFSMp3ASvHxCjP_JcksvsSzS5d88Dj4wb5MLdTJMv7nSQPIRvmmTDUrsqzBA8CW75Mw6f8z1czNYqZfCN2chEB7QcDZEc260YzQlNFui4NcEJt_tM7y4bk-kcMaFPSotOiaDfV3Jb68C6LjjMNHBwCWozTolu0CWSm0Gs8zyqDOyHR2Z6u12S5pN9boNXM71G1z4IgglrlyxhQCZuYKu8zNZg2nJB1SzYyLyTK9CL_NgHskQGcwjF9MTcnAs-eBikEusW4CEFXgDbr0KCDZsnP_fe71w9MHJZtBI0ol4C0AQFFPga1v7ZiNuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24728" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24727">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFfMRiBGhY5RIrMoXJPY5KxMchD-CzMEJLwUGwd9xXSNKlSHLAw1xFHm1Em7KvLdgwCi2T4eAYiviuKm8sNwWhQ6ie3j7dwfWIU4rfaDX6GJMapKBsRNrhKrKyroHYv4_dc0_fEmbVC4p6NecNqBheJo7DGN6cvmIm2hs3dfEnsJzLEnLH0_UglZtPbvjPFE0a84kYoB8hvk_i23C5P62KWMeBIL2RjuxQemDCUXrpYjiywfONspYb7HyvNbf03bJ-ceN7MRWoXKddeXrWJgK6kpMBB5_tg_MysTkWCVtKhrIYfv5A5k1-s-3olN5nSEzfXOYcpHijV9HA6h-misGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24727" target="_blank">📅 02:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24726">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛ از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24726" target="_blank">📅 02:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24723">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=KERhETG0mj7Cm8cJga3CgsPdQHUlGkCyThp2aM57HPQ4W1DWB51s9TerdniRwNDIOXpg3ivvUZKaPugk8KZHuuOTWEijmqIgJXY6NT7U1EadPdxpIaqqQsiY7LSPtgQYXfFGIbbHXR_9RbFL3MSmzmJklifu8559r_6jtegc3ROPQQm_zaISWSah9QjRrqJy-9cWs8DzzTspBu3Bqzp_ws27jD63INFvh0kDKv4caLomZS-E9OAhSQJJzhtU2R56KFYkhu1em38wfBpn7hbiiPJX1IffCjnN1nnUe5FGWiCmt_DivQU9Ww92QT2yJelSg1PFRQpvzbGrRCUqBmeMkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=KERhETG0mj7Cm8cJga3CgsPdQHUlGkCyThp2aM57HPQ4W1DWB51s9TerdniRwNDIOXpg3ivvUZKaPugk8KZHuuOTWEijmqIgJXY6NT7U1EadPdxpIaqqQsiY7LSPtgQYXfFGIbbHXR_9RbFL3MSmzmJklifu8559r_6jtegc3ROPQQm_zaISWSah9QjRrqJy-9cWs8DzzTspBu3Bqzp_ws27jD63INFvh0kDKv4caLomZS-E9OAhSQJJzhtU2R56KFYkhu1em38wfBpn7hbiiPJX1IffCjnN1nnUe5FGWiCmt_DivQU9Ww92QT2yJelSg1PFRQpvzbGrRCUqBmeMkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇵
اشتباه مرگ‌بار و فاجعه‌بازیکنان‌تیم ژاپن در بازی شب‌گذشته‌مقابل برزیل که باعث حذف این تیم شایسته از جام جهانی شد؛ با گزارش عادل ببینید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24723" target="_blank">📅 02:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24722">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDh_ViVPJ5avcys_9SASD3JPVoG5EqC2yl65bnFcjS5zF8NLtyVQGiOxdXRWwmEJYSWuRhsJTNT1ieWOeDxCKmCKzJOeDrzlQ9kdZuQbPNm2g3I5fIocyXfwo2aaPQr2YAHyouyEJ6ymWfBUS2dNWS-BIvKxk49uqUzQfwjrk1bOgceaIE4cQ2uGpE6kc2h5_2OLAo564nS_x_X7DCcEL1NBiOIE_fm_blhv_gZkI3KgHvTIky_IUQdO_gsOwhuO6EHY3OMn40H-bhEL8LVbxLSSiMSJNCSyq_v9SJg34oMBGpLgtRlqnEM_oGEPIqxh53Z_6H0MX1VCJqoJrLJHgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعداز آسانی؛ منیر الحدادی نیز چراغ سبز نشون داد: تاابتدای هفته‌آینده با خانواده‌ام به تهران برمیگردیم. بااستقلال قرارداد دارم و به آن متعهدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24722" target="_blank">📅 01:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24721">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=niM7XQGR7bJS5r5BfDTE64kpjyAzk6G7aCkZ1QhvEKs4ZAQ93LfPVK8j68UGyylY8yNSEG6oCaiR7xt1NaXdX7O9xoit7R9c1c18h1iM95NMvR42wxFFR2HjB3NnjIa26dSQ0U-ZkIYgOsy43bs9DAfT3NufubdgFle9KU51ahVTU5qgOP--5EqvYaAF_k8X7Cc8iLZX6kvQVh8Bh6a1WQoAyYo6o4dS0oJe_cNyxvN6I2zRq6lUEDUR7U6iGZjZswLHyCMud6Z0n9rsEkH1h_dNyCEAxyJG9F5KB_uE2_89OKv4fP3DXThyyYPoleyNyumvmsDHX6ZTPr7NG3e_Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=niM7XQGR7bJS5r5BfDTE64kpjyAzk6G7aCkZ1QhvEKs4ZAQ93LfPVK8j68UGyylY8yNSEG6oCaiR7xt1NaXdX7O9xoit7R9c1c18h1iM95NMvR42wxFFR2HjB3NnjIa26dSQ0U-ZkIYgOsy43bs9DAfT3NufubdgFle9KU51ahVTU5qgOP--5EqvYaAF_k8X7Cc8iLZX6kvQVh8Bh6a1WQoAyYo6o4dS0oJe_cNyxvN6I2zRq6lUEDUR7U6iGZjZswLHyCMud6Z0n9rsEkH1h_dNyCEAxyJG9F5KB_uE2_89OKv4fP3DXThyyYPoleyNyumvmsDHX6ZTPr7NG3e_Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستان عجیب ازدواج و جدایی محسن مسلمان ستاره سال‌های نچندان‌دور باشگاه پرسپولیس: دو تا خونه و ۱۱۴سکه‌به‌نیت ۱۱۴ معصوم توهمون سال ۹۶ دادم رفت! دیگه هیجوقت سمت زن گرفتن نمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24721" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24720">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k90nOnY6brYHJGagFE8jlOpHDt2tYBU6S7PA_NZQQsxVwrIhvnJmei_norxLY8mrsGdeljwHsPda6ChqxxwNtTpEsl7xvNbKQT7PCwgLn0YSrTPK_sumJUxUYcH_9bWLpSyTS-ItozflA2Z6zXBMaEKsnNnc7oukFkNlzzCdhO_W2hCmvjSAVvTgsGqfft2fiqxWpA2zZ81l0FoJUh8K-BtFlT1lHj-zV4M-Pg6p_d9ds-ikJAseWRfpyOossPkwFQKfGT_uT2n5wIeBT0lCBtzAbYhZTf8Mc8omv4bxD-XmLLsOtsZaYQkLRuuVRyLBrI3AndG4GERfTOK1TmA3_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نشریه بیلد: هری کین اگه با بایرن مونیخ قراردادش رو تمدید نکنه مقصد بعدی او قطعا بارسا خواهد بود اما الان هدف اصلی بارسا جذب آلوارز و هدف کین تمدید قراردادش با باواریایی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24720" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24718">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBVZMWWpNDIXHC7EKgzsL56wWCo64a0UXIpqv2S1pp0uH-XPohKElm9nScInoqUG2qJ5we_OK0pVR9o1FrxgmWsA1gDhxBHZNdWf76zpwbibtIuBKAbWg_Vsg1TZRXgOhlYZaSn_KJ2871J3kdTD0RMkp4LNUOiTmr8O3zrKiZ8LNgxxXo7JYst_PFmWFAqjU0afcvircwEwtsgcmKGDUa6NtugGpUOJTaZAhKyAH-m8J43x-rFH7mur13AGeqyjmWHllEhJnm600fSD7IdZPkM_UYS6UPynJZlBrzHGvqtafS0b1p0Srp03AO3ZUfiAAifPzF9Ka1HZ02XFX7-hXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
نشریهESPN
: علیرضا فغانی باعملکرد فوق العاده خود در رقابت های جام جهانی به اصلی ترین گزینه فیفا برای‌‌قضاوت بازی فینال جام تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24718" target="_blank">📅 01:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24717">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zsi-PoD5sioiTLkvs5e-PgMN0asomwMrNGIU1G2kwEf1x8lWez8X8WvTnCytHDw_ujhWBRJxi8GsW_Rpzwp8QOjCka6eLJx7TBKuw9kd5m5qraaLsJEiYKGhJqyExxzQlHtouVkRzYroe4CVZ9taa7JgBnquhhV69GaZjeTDSueoX1hPyFSpQCzZT5d2kvVZNv5S-rr8Sru5ubbTrzwWq_30xtSYCiTwZotmfllcMqmGOR-mkCxDR7TNiXYHi0gOjVDs_SLT-QrR2ViCretMuTKPm1zUkjmxZM0BNnS3GGSNDA9JjpT1GAQNBbSGPjKlIynR4ym4tIBnmV61T8lgjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24717" target="_blank">📅 01:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24715">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2-DaCb4Mgr5qPUa_QQL0g6nmSDUChBf7m_ykZYXK17ky_6KEx42ORKL_aKPofWnt8rGm_zPtYFEG6jso00R9UUqlj2oiVtUxBwnS9W7GzTU0euNm0wqmuNrHrBY5viOTTtTqv1FMpEDvWHC9MJeSdqUjSiz2lOIhLKDW-Lmng6BhItqTcnWJz7ls7bxH-zROJOitScxwO2jvcEzkaecbxVexW4aThg2QRcWiQiTKaqBjAp-9AlUAxG_Y0_FmCBdLwNc3aVwO_y3brBnN0GrfWp0JSGP-P9l2nljf5kPWsqerQikDmiq0NmoMWHoLn2Ucn1KxA1Or0j52iCwKWlB1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جیانی‌اینفانتینو رئیس‌فیفا تو دوهفته گذشته 24 مسابقه رو تو جام‌‌جهانی از نزدیک نگاه کرد و بیش از 50 هزار کیلومتر رو در یک جت خصوصی گذروند.
‼️
براساس‌برآوردهای بی بی سی، تاثیر آب و هوایی سفر جت اینفانتینو در این دو هفته با انتشار سالانه گازهای گلخانه ای حدود…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24715" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24714">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hj3TNMLJZ6ijGIG_SiVfreeZhzV0eiEvsPomGSu9efyVcnWD-hoGUsRBztFTXLZE5HjopXGuJjt0cUtXpP-8jnrMnmoEVWtr1HyphQA7MdBrOaiWe-cJ5G4H6kUzgUtXbSVce2RZSxjjkGqbXHMnnI_GUzgx2B4jgWYprkUp6QDmh6LcU5Wdakj6pOOgsjMBlEGePqllu7U9d3N8uEmYL-yONO5QZjC35s1AXDmj7e5oBJQzOn_LWSuHovPHqyCOBV4wxrTvEph9DxzEoA0YaqzlQo3wsj-RM-EzGaLYS8AOgJ7n8dbSIFO73gKWZFlqLQYjL9--OS1Yih12Fs3a6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24714" target="_blank">📅 00:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24713">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjvNExn2XHMv6FmRFi6ot60klX_MqoZebrPwowVlXYVVdwkOP-SY80vKimMMcWpMi41CvM6pCR8L-wYJTC96B_FI18U0U4Nse090LOdGl6Gv0_yB_mNg7TYWdrpmMgkjSClfDR0aDsohrxExYDAbxPF6p0f95Yn-uOhNFzdlu5uWLB0Mr20iVPA_W-PDRwWlivnuvf4Nml3Do--g85CMZDuLDcjmYi53ytxvS7HdxrzYhTYpT7DpwYeEhVshSZbn3gH7dMOM747EmaygUpOs3ZLuVtr9dpV58HN8ZPEYCHdTwG49m5J9q68EqqLSgPnBwjorq8htoLpuHSqHIL3ReA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24713" target="_blank">📅 00:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24712">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zh0Svrii1LORYYME55FkSLDTwH1N6fxSHw_R4Fvn0dubGxCa2lh0ht_xsXeZEvtqqz5BYCQunDWdrIuSpne1ZQxBvJk6dhe3zV2WHZp0bZBsPNke0UCUtERu6jkfXIql8gi4gcoF6Haar_aiOO0WhkG8N1AtnN3nA12B5cLxA3gHMi2fX4YZisyH0yewP0YVdO8nY_jpYraZS-e8I8NKSMAaGQUAELXUOjhbeL21jwacFLFgkbPkLQPjCIweevihaKkMf0SgRY9wE7yu4g13kwuBfmEzClLytk7AwvzxclevHAHJaO7u39p5SPtktnWBJE_AacS_-p80xhD7U1qQVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24712" target="_blank">📅 00:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24710">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtR3OC-eaqVCX0gafu9pNNLgJ3ZzefSJfjeqdHebJb0xAsn2_qj38_J2WHz2P1hvM7dyazc9hHLzc8Hc_km73NiJcKLC2RwOx9Z3ptpMzcJ3rUDYGSGpyW47rLWaRqrnHVTiGcYNJv_Wk1f_3PWLl_N0dBK1djshO2GC14A6E3CuU_YlBali-6eM8vPk4FjuXfxcp3LHitEgHwu5lcx4LJsWthV4mxH663K92sNTv-Y9FGw0xBkzhhZbhffOAqMSYo5-RS6CEO9Do8z_-sVhjEYTQgI5Lnn-QWpLEgIbQ1FWPjgaCtWpkNnxG9fDLmlcY-YusPLh6iH_W_KE0x7hDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛
از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24710" target="_blank">📅 23:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24709">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvmLeOGppxNaxVNt-RkD3QXxMqPXHQ7XMsdiJEycYo-P7Rb2kUnB5qg4a4FXXxB3i74IGLb6K1pUBWO7j1b60NomUaFGBtjW-4Zs_nyKh4cxB9WP096qDE5J3zfyUUcggoF6hAt_VFWzhf_cyfIY8eADJoCyGguKEcwBJZ26scoD_FZTasIbjrE7MpNFuQ2dC6bRS0whtQ78PxijJctC0QS2qoDn2F9gKsGZDE-I9KkajjYzCm7JgdKIoR1rfsNXDUeyThJ8KaD-AW6tyOxxlHALNy4Omdr1mDspy8GCuifnnG9dtura-8Pt7pwdhOYUHIyyknf-Qb8TozVO-jXqsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
از وداع زودهنگام هلند و آلمان با جام‌جهانی تا برتری بزرگ نروژ با گلزنی هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24709" target="_blank">📅 23:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24708">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9skqyEh_pAjAtl1zxK-icG7etHL7EASpyAYu2wywtlOap7H8nTsoch-CRdpr74ng8il599NGFcRVIFAasZwHe3_5HemM1dP-Lxd-vVD8mvYA2K9TPFjaVPwNq2KpQ58pD8tMHytkhHHhEwH0_QB5bRrUghKHX_HOGjq2FIjUgiCpQ6JyV6UQxTyAxM74-n37i8N8kZlpFzZXNHcH-p2Su7FPA0WRP20E2nnOO5HITRzN2mj6SRwNBzLEuOP2UEL-1tI0jrOJi2h5PZjYcgXkSddzWuf8BVGbZusqWpoWSzSkMXrBJsaJnwTPop99cgjt1Pw9ztC2BFIfOKQurgMmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
مقایسه جذاب عملکرد بردلی بارکولا و لامین یامال دوستاره‌پاریسن‌ژرمن
🆚
بارسلونا در کل دوران حرفه‌ایشون؛ بارکولا بسیار علاقمنده که بعد از رقابت های جام جهانی از PSG جدا و راهی بارسا بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24708" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24707">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/af6zyMzyvPO9-R5ljXVpGfYYa4ft5_OVezjZnUSt8jvsLbRerh6mXpsnfTsWePTOu0pB-5nCvjBmAUlXmW7Ly5RzHqx5IJz8FLy3msv0x1d3UyQmLdPlZnpTgLSw3zqo6nzmcSa5ck67thOzW7Uh3dwmEu8c7nwrSwUfKvYlCUVhS6bu21NVXb5AFogX7KmHxswZ2nIEWNrQ1xzzn-OxLRM0TF3Y13XiENdDvp7P8GlBykz3cFdZjWi79PLdOBGMtKgx0X_307-jR-zRn7SLmKFTonz_JmCDG312IIfAAGSkvIgDJPOQjeMSuBMfqpmdv6C7CVOV88ltiVNBDcYWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نروژ باگل دقیقه 86 هالند ساحل‌عاج‌رو شکست داد و حریف برزیل در یک هشتم جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24707" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24703">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iq35Bjzllv1XCPvLWKPnmUG6BZ9Au-vkU3QVuCOxgVZJ0C2KqVdrdhhaoIAwdenenPE2kUGIGQyRGFsZUkFpH0xgV9vs-WBM2RjLh7QQLt8ofKkVxhbpUt6aGIb59B2LVQ3DLUXxZoSO7jq5p7rp4-I-bt6_-kjKljNQVgGngQCrtztaBO_SS292Qnhh7z9iccxsgPAvXR78_3MMRmmKcEBvb27BnZDVwAF3NZYJJQT3m14JigD91A68aalYGr8Vm02oLR0h2OuZf2BoBYGnqX4nWCoHv-4MDh2zITFAoX9rwsDgr6Zn5xP796WQIz5pELcJV-f91oOWGwETSS13KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q_aV3yzjdhi6g-6n2WxeQguhjpraKqMgz_7zAh4jY8LQgy--vSEApC7GwV8GA6V8h__xAMYNSLRh8NC1r--ObcMmBe6CPxSRjxmsJbYP88u5CA0gMRtbNjxEAkJaCeCqt1BLw8ysAz--dvS_qnCGqjTpBjd_kOzmaX9S_ZW-VSNsxhDGaosRWoLM-J4vnO_WwVSuygKOMa2axEvmkcRl_bVyVlenrIBDaXbIPO7FKV90G_FnHtdSIl7GLDgO4aWF0O7bgJxCMWBwaSSa2OhN7xBm8e4du63t96gHsHd9DvEuKaq-Sge743NJH7cHbuXy_1YPYf4zYZwjPE8srrUIGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدی
د
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24703" target="_blank">📅 23:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24702">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRPIeIRQlmpX4cGjaa_z2Yr1t9H5EcFLw1239lxslzb0_OKz_v60iVJWurt4dwmeUx50dL9CsDFfgcsYFw8SknBWvkfgd70KPLCZH3zTlgLJMQfyGcCetFaVCkzMXSVAtmuLAepaR1Lflz9Mdd9j_8QbEy050Pg8SqcmCDOpdadDv7HKKfHrX846go8VUH536DTLXrj83oy3eOsSeGyqG2-vXPRlbgrC7-EoY9heLLaMrv7A4UzNSiDBFUmhDzgX7hLgxbdnLIGjh5gjDlDO7hSU-BB6v6Nh1mhiK8vOVehW2BE8kMMRGswV1a8kZ2mLItambGSkzb8WpigE0FU8Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24702" target="_blank">📅 22:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24701">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIxak3R3lR4FOrTYPlgYFnIKTvn0o5enwGulZ4O6j5OzARsoWyu3Yk9XQyPBXHGNfH9vDQIVM3jqWVxwFPYnRDTT6dp71ZBNfxdIYAVA7aopnJDOtd94G6lYzTMmX_CGLQLySSCo3JXEFiIBWsZvbWMqN0wKLiG83s6d9pphWrb6kOkH7Iuba6BWQ80fG7JRB-POUcMDEHDs8eJSuHYd8AeKBFYaJylqESxaG1ZOw9FLGHV2n2QdfyTJF8FowkFUdwCXt9ipUmfb67XMBZ6WOFFfx8wrOM2fDvhFsBbEGCFQbc87xFhgQvZSjyTkucFXrlUZ6P65EoSWAyM4Yd5XXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24701" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24700">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfAuFmTHTk2FDUYnXAUUyt9asNvGBvd2tgxEyp8nBen52x4OrvmMnkxdvgsijLn4MfS4DcZq0hOUE0AjmYFddvHZPz7DNdy_tzoD7l2alcHG1wkXue6rN-uCy1OvMlFGAMAiLY6kLBNPBPAS8DnpAVyq6W0Zn5DHqDEEn1W3QNSnX1FWaXFwvVr46i5g9u-pJirUiyrbS-YBwnjj3HyCBpACeU--pjOAokE-WKQgi7PCKS_kJAjbmYa0GXA4vWYKJOHiiFZzWG3B_IaMKhGt2tFwwLNy4QwAQsJyaMNJYQHtKfoZ5FxAVPgp1f-Eh4edA0DBDHTkdNATDblj3NlQHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇴
سوپرگل‌دیدنی نروژی‌ها در بازی امشب مقابل ساحل عاج در یک شانردهم نهایی؛ چه کاتی برداشت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24700" target="_blank">📅 22:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24699">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbPB4TnzQd-q0qtfwpzL00pQqioUDJb4eGxvzSk302JIj8AxArRASVvIieYoY50piYus6Wzolw0EqnDLxEOAPuKnieUuct6mTayJoLJdtCao-Ys-gX-F8-Nl_70wdvbUQ9GHEKHIsVbgJW27CZv8nPdIueUrnNNbAI_cnps2aXXxokSKrD71BeP1LnNFuUdsFT16434pY_tBD331_xyyCnn_XIwCJ97MrE6p35v5SVu2YgNkh4wXYVn0zDPR8FdZde7GDFLyAy4WxPdg7PlGwJ8dvGJ5pWKq4Yrzr8185QtCySNhEpjVmh2ZG8aTXKYgRzEdtL84jgVlllz9CXDPpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/24699" target="_blank">📅 22:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24698">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUJyQR-B41jHoWtlDkFb3YbbgODuao_T2KSBRFMJ4C2i8llyUB0wgrUsAsyt-_gmYU_ePdAgn57_JSoCULIem-a169_HPS4Z7uQ8EUDQmveSf9tX3dh9jIbTB9XC-pxEkitVHFf_Yb_ngHPOFQNt3KeyL5VToss-DTxOA6Tjx5MSNTHB1JaHvoW90we_vOVczZciLTymeELsgf5CQyrOqqqoaH0vbqqk0260T4VqLnYkECfMRLdBnXwfClVYNe55KPJCECdFxHlhCbvplEx60zOP-bOg0dDQCOCeNPqH1_fEUfrg1gRpoX3YMgerkNDTkL1IBUn55YdQWyzRm__1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی در ویژه برنامه امشب جام جهانی اعلام کرد بنا به دلایلی پیوستنش به تیم پرسپولیس منتفی شده و فصل بعد نیز در تراکتور خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/24698" target="_blank">📅 22:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24697">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=tjvUztpDce-aULfqzJjBTxKip7Wv5CwjIpYQox-lIWh0Or7a5uMSKMyNXrve9x28WaMrEReJTzW-fYeS5FImVl5oRIHU0RZeytzHntaG2ADyK1gn968ICnL8abCFcErIWorOBYOvpOisOMsx8dO0iO_ycKWeR7VAsZocs7I4mPwcshlCRFRCJ2zfJs8DB9OFtyOhks7H_LCiwBk_Jj1nfbF-EDnlnZ1YS_kFSdVmqN6kMch574LJZyo95IScMz37M-r4iWb0oz2FQ1s9MpLYHiCIywHyH7Z40l3k44FTh14wfQUZdTMNVV-9HF6DZ5BbSf20FSNYk16Toug4xhyxFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=tjvUztpDce-aULfqzJjBTxKip7Wv5CwjIpYQox-lIWh0Or7a5uMSKMyNXrve9x28WaMrEReJTzW-fYeS5FImVl5oRIHU0RZeytzHntaG2ADyK1gn968ICnL8abCFcErIWorOBYOvpOisOMsx8dO0iO_ycKWeR7VAsZocs7I4mPwcshlCRFRCJ2zfJs8DB9OFtyOhks7H_LCiwBk_Jj1nfbF-EDnlnZ1YS_kFSdVmqN6kMch574LJZyo95IScMz37M-r4iWb0oz2FQ1s9MpLYHiCIywHyH7Z40l3k44FTh14wfQUZdTMNVV-9HF6DZ5BbSf20FSNYk16Toug4xhyxFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اون‌بازیکن‌تیم‌ملی‌هائیتی‌که‌کارش‌هندونه کاشتن و فروختنه، وقتی میفهمه من رو کلین شیت مراکش بت زدم: این چه سوپرگل برگ ریزونی بود که زدن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/24697" target="_blank">📅 21:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24696">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kN_QMbWhkxCXjVe7VWB_yFP__WJdt9ZuD7cx48YuyQ3WNm9wVb1serG3YiHVkxBdDS4rJCckx6YHWk9q-E3MR54Z4R4gykf97fJTRuDn-H8BQprD0WyVHz9R-_1XHGQ9-PZTPJmy20qwPzmanLRfntuumzr1G7Kt_z2sqhul2NRN-guuxehDUDHuqlFHpOHQ23IvFvUVtvhtNR8iOVP1JYwU1tSiYDhaAxe18BOUYMTct1eccBnLPfTehZy6Q99bUTcU9OtsdhUT8NjQ4aAuCNJe2QB1KDwAxQpoIdPYooBpCSbuIezmU_OoG5lygZs2oP6-eo7g_sWSx4xJqhVp6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لامین‌یامال:
شانس تیم‌ملی اسپانیا برای قهرمانی درجام‌جهانی‌بسیار بیشتر از بقیه تیم هاست. فرانسه بسیار ضعیف‌شده و تیمی نیست که بخواد ما روتهدیدکنه. هرچند بازی دیگه با اونا داشته باشیم باز هم با اختلاف میبریمشون؛ ضمن این‌که تو عکسه هم خبرنگاره سرشوخی رو با سپهر حیدری هم بازی کرد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/24696" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24695">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=d7mHdDWqBC6MYHURxXjbEoGpXld2UP5sho5iYPgjVDZ8mTik-xpdsHWFSFGSgJE4QB_vK51wBn_vb2Dq6bH0vqxpHUObJ1tBcsRELKXoGDtwpWNA6zN81hnrYQ-iK1P58aMnkegt8ru-mp_CbYgu5W-pukLOls1s-GjhE0-bgMbfZR8TrW1GUi1D_MuNfhoRw6_oLPgzsezCEbtPW7TUQoC8BJQvZo1nE3GgjY8nLNaKJ2QMQiT3joOV7SFJFqnqjPddCGN86GKBYdqYPekY_QbyOfFWS1-q9KA-KSLNTW4yha93Vcox_XfN34R8_nplmHfr7ALrjvwBXsnRkNleug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=d7mHdDWqBC6MYHURxXjbEoGpXld2UP5sho5iYPgjVDZ8mTik-xpdsHWFSFGSgJE4QB_vK51wBn_vb2Dq6bH0vqxpHUObJ1tBcsRELKXoGDtwpWNA6zN81hnrYQ-iK1P58aMnkegt8ru-mp_CbYgu5W-pukLOls1s-GjhE0-bgMbfZR8TrW1GUi1D_MuNfhoRw6_oLPgzsezCEbtPW7TUQoC8BJQvZo1nE3GgjY8nLNaKJ2QMQiT3joOV7SFJFqnqjPddCGN86GKBYdqYPekY_QbyOfFWS1-q9KA-KSLNTW4yha93Vcox_XfN34R8_nplmHfr7ALrjvwBXsnRkNleug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛ از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/24695" target="_blank">📅 21:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24694">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=RytvG2t_5XOUrIpf4TL4-AU3jlayTkqJdgD9UtxE_QF6rp0SAZ1gUOYeMHto2Kg8oZlFTxYcT-O_Wjrt9yFG-TAF4aZQXXrLfNOBaEimb1BqR8_q0HCttjtd-8YEfA9IOslPvICQ5jG1Iqum8vK6i9Z-MevYfhLd0vQTyOPiozBAzqqhvMx-iq3scoWPJ0EW8fHVG23G5R5ymUfW4lOD2ZO_gCiReBZ6RaV0g4T0K5TpS525RhJB3XEtAL8b8JxUUzochnERFChZJPx60ZX8dp6ghKHtV8172enmjoRAuNYoCrbDj3QWwrztkC0wIO0z7o0L_aWJNnfmfthnf3nftQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=RytvG2t_5XOUrIpf4TL4-AU3jlayTkqJdgD9UtxE_QF6rp0SAZ1gUOYeMHto2Kg8oZlFTxYcT-O_Wjrt9yFG-TAF4aZQXXrLfNOBaEimb1BqR8_q0HCttjtd-8YEfA9IOslPvICQ5jG1Iqum8vK6i9Z-MevYfhLd0vQTyOPiozBAzqqhvMx-iq3scoWPJ0EW8fHVG23G5R5ymUfW4lOD2ZO_gCiReBZ6RaV0g4T0K5TpS525RhJB3XEtAL8b8JxUUzochnERFChZJPx60ZX8dp6ghKHtV8172enmjoRAuNYoCrbDj3QWwrztkC0wIO0z7o0L_aWJNnfmfthnf3nftQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/24694" target="_blank">📅 20:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24693">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3qKdp3MXAsni4n2RZYRkK9om-XJStiWAdxE1-EEUl5xRJ3lxcs-wG2Gv0glEPrvcGcBUvE05LwnZ83uvS_FTaqVOLbZOaLZU4oOaLDREiRyOorGg2e8w1ji5XWB91NbXTuNqXDo7mHc8y4O9gCy1Q70umhpB0jtepUAHvqOYaSaSrfO1VOsf6wwze0VYkr1WUINiFi6x2wqy-sQB_w8OBJamMDNOv5TnViEkzV9xAOnI8GjQjWZ1ghqnHO1ZjpP92QF47_Wm7fz7a5OtB0B978QHHPWYLxI_m9Gp1CBIhZ41slWiK-KdvPERCiXcMgxypUCBZ-eCxtPt4BhHya2_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور که پیش‌تر خبر دادیم؛ یاسر آسانی ستاره آلبانیایی استقلال بامدادفردا وارد تهران خواهد شد و در تمرینات آبی پوشان پایتخت شرکت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/24693" target="_blank">📅 20:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24692">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYmCa-vexyoTgyghiRy20GR6gT9QP0kzFPEnHlPjHMbTe5Vm6nuI2ItMXbreokwNecIeHHUs458-7PpV6dqTGk11EyrZ19WSCXVx5j4vfGPt2miDwY1DxP8gWyd2vf7PV-f7NpABulCH92KG2Jc4iVQgvTJ7Tweum1pQn-7QAJyMMcM6208eLxB6c8orfRLZ2Wvk-tOHoYO4POcdYbtqPmlKF3N-7ahPS4L5xED6TUG8LAjE8NUeaow-PbXHHqYs5M336Y5JdQcFl0h17tnGI9ACuFaW1iWcEjtE6eAXvuCauWd4kgwp9sanA-2bFQum1_QvzwbsTEZIUrVZ46oTyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فلورین‌پلتنبرگ: سران‌منچستریونایتد با ماتئوس فرناندز برای عقد قراردادی پنج ساله به توافق کامل رسیده و حالا توافق با وستهم باقی مونده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/24692" target="_blank">📅 20:18 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
