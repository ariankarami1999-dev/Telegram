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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 15:33:43</div>
<hr>

<div class="tg-post" id="msg-24806">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c080f226.mp4?token=egvHbA8jf-Is_m_Q5GkvcqDhkKtOfy6wJgPdQlddHiAdoV1wqjngo02yn9E0Dix8ZF-lnIwkmuLik_d6AHwx9G_gdQCDGhycP8ecxE1vkFqCd_F9r2b52ELfnkcpOkeqdmNWCTbNtzliv5Npq32Yh_p5FIlnM7LEGAqKlbUltUm5fhxOgMaPbiEBGhnRhQVi6QGF7z_vB3HOAna-b0mXIf2aLZ_BPTwt_fmk_t1ivwS8y5t7g1WKp7yzezli86Q1KEQ0EgpOB4vlzPQURjNrXxGzlFdc2-_w7m6AasmY8tRt-znuOskTF4KjQpoWN3ZPlhPs8xdwtNnrRwBgmGW3qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c080f226.mp4?token=egvHbA8jf-Is_m_Q5GkvcqDhkKtOfy6wJgPdQlddHiAdoV1wqjngo02yn9E0Dix8ZF-lnIwkmuLik_d6AHwx9G_gdQCDGhycP8ecxE1vkFqCd_F9r2b52ELfnkcpOkeqdmNWCTbNtzliv5Npq32Yh_p5FIlnM7LEGAqKlbUltUm5fhxOgMaPbiEBGhnRhQVi6QGF7z_vB3HOAna-b0mXIf2aLZ_BPTwt_fmk_t1ivwS8y5t7g1WKp7yzezli86Q1KEQ0EgpOB4vlzPQURjNrXxGzlFdc2-_w7m6AasmY8tRt-znuOskTF4KjQpoWN3ZPlhPs8xdwtNnrRwBgmGW3qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/persiana_Soccer/24806" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24805">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6n0uLxmmVZ74ca0Wp4Au7_R6Am_fgl9GJv98NLKZL8tR2A8auH7k6_tB9dfv7G8d38WvIU99OikuR_PC-_s8Tk2aYTQWGUzXJT7za27T_5zeFeVtkIHyEJ1k6OTheiukvWvtIdf_NApb1u9OUJokqXgCMe7xE7MZlpew7Fyajnp4O58AOGk77cNVh2ou4roh6GuyzducRGXBXZuWQEUEZdNP8kNoFxPTGCR_QC_XKHcuKvIcIwJf4tCrGGvgRSAI8O0Q7FsbMrTM9eoGItlw5KeHIHzimvwLo5i_oi_-FHvMHEYTODhOSyCYiDucsqkwsVbS7lgeSdtabqj_DKcDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل در یک فصل در تاریخ فوتبال:
🇦🇷
لیونل مسی فصل 2011/12: 82 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین فصل 2025/26: 72 گل
🇵🇹
کریستیانو رونالدو فصل 2011/12: 69 گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/24805" target="_blank">📅 14:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24804">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/24804" target="_blank">📅 11:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24803">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyrSigv_HDdjmkwuaLRJVFhZ5nThInxClJe1K1IZm9STjtV0ICfsT6dheX-cSVcBGuirIVJZ6GVDhlE7sNzifCtOeEJjgihueFXShiBKSoFy0Fy7vPQlY26TkxVeiI8w9I-Dfs7FLtWA-Ea8POxDx0PVyr6lzyMWG_Xd7FdSSYspdXzIEJSArEeKJt3o441ZWI9DWph2g8EXLaCtXrI6HCwr8VEm1Vh0k1PReBU8ZnzWa0lmXMXIAlOQBSpFLJBjN5dN8wYXBDZxWvBJfOILqNAgcnKvvaJSUhkZtKuSLtkMKbyrcsVgpnoI5UW399otOzZoyOlR0eHiAkMHLHOKaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
ظرف‌چهار پنج روزگذشته بارها اعلام کار انتقال دراگان‌اسکوچیچ به‌باشگاه پرسپولیس نهایی و تمام شده و فقط‌پوستر رونمایی و اعلام‌خبررسمی آن توسط باشگاه باقی مونده اما یه عده تکذیب میکنند اماامروز خبرمیزنن‌که اسکوچیچ سرمربی پرسپولیس شد. زمستون هم بعنوان اولین…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/24803" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24802">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/24802" target="_blank">📅 08:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24801">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8EgLi-0D4KBTNr5nWn3i-qkuCwLCkCcOa_5PHDqe0r3IBu9YKr9Kk5kSglZphEvYgB3bkAfqlGMrQtxpP8ERgSYxtvBbUY8JxZQ1Kufw5r-Ek18FynpI4poH-T4rdLbk3tKYvOU__AnZTgAb6Cyet6PuZ2NhcOcAtwJ5zHoaMw9N5xkb-QVknndpq85yRshitYkru7RjGFg8T7TQZhJuaHOhobxejCfqUB66D4HI-xwnDtrWBdJUFZFRkTUbU4gpMnwzcIA_n010V1KfmJ5Seq03M0qFZv0IOMZ6iz1b0XJ1W4WPP85TS9N8kW0akH_0nN3qAZssloF8AINcEzY2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان چهارمین روز مرحله یک‌شانزدهم نهایی؛ آمریکا هم با شکست دوگله بوسنی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/24801" target="_blank">📅 08:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24800">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVx4mGPuQ6VLm0fXVPxMijLd_LwjXpEJyYT_do0MqmMrJiXguyrs8fuZjH7I61zm-rS1juiqxN702lSguJxRvzPovimALRSgj3V4MOxmjxx2QCxTxslm59wuOBhieD19Sr9P9cfe-ydscVtY8_WMEm6YcL66R4KBGWj2zXn9m6v6hH35ofi3MxQuCy2FjhluLQZg_Eec1iBzcEjXmBm8_NcFsu7KrKiz6DUARjmkQHLOzUe82owl8sprFL75S4NZAmQ0SN5nS9Mf2Ak1taHrXGcSum1l0fQqlFfoDzfia8U0QMcKl69T8AaywnMwiVQSGOqfYYrRDgFbIioHNkSvKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله ⅛ نهایی جام جهانی که در حال تکمیله؛ بازی‌ها داره مرحله‌به‌مرحله جذاب‌تر میشه.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24800" target="_blank">📅 08:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24799">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-_YS1f924PRXZJMro_kvNM9NpVdoJpgux0C5Z7PzxR0Ri9jKM2KFTjEsj-Ga-gPVlIzqCW3DB2lpT1e_AoBuOjui2xz6cfPJNxMsFBGZcqwo608DDkpXYgJcoEO7R3zljoqoW_LlOohw6imzm6TNKJGxLYNlWgmLvKQyoWSdwTjmQdh41MYbWEEof2BX79PLfrzZ21kAIJiA2cvXJiJDSWgQL1ZcXqXcKlN2VqNZl4wTT1eOLxfrzZtEB-gh4bzccnSCbwmBB8XJnuEUdGGRdyFzd2qz_7jCp5Vn6JOrZVsdLc2gQFztjDMxITEwH2dW8EldywsOgNtqZyNUzsx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24799" target="_blank">📅 02:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24797">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24797" target="_blank">📅 02:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24796">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIokwPS7kSuo16nvDGQjCT8HwY7-vuHGJPnnMe5awpEqLrQjZKZ1pR4gU3AlCQmXJ6e8qH4J1wi4m0Fd2mz4iMdmXr5AIRxoBY_hrGNozCr8JZZRmkMOS5Qs-HscDJ18BuoZO5biNT9Qs0CAFwqhZkyQr101qX6m9945blee6xSzHXkzw1YQmLBT5n1Q3TDg5q6Z499NJAr1b1GX-_HBQMZemFCHEoh05YMUa21cdcXKqTBFvBuHw-QVR2ikkw7-8NqmCVkOPH2NOEJ2ZgYgtMIuSfmSbJQcpltrJni96YD4_AlUGfhBij0UaZUWhqYHCYsv8xPnDRPNL_fkBTeQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم نهایی جام جهانی؛ صعود سخت و دراماتیک شیاطین‌سرخ‌اروپا مقابل یاران سادیو مانه در سنگال؛ بلژیک به معنای واقعی کلمه مرد تا برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24796" target="_blank">📅 02:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24794">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9G5DZyrdAlP_F7Qt4sNiZqHS0O0V4PfN-Rnb6mF9vfvfaiZMmeVew4CETXb2k8_fNP_x58RBNse5-01RqiuYAnM8hiHIXLjr45wcqXWRDfJf051ff8cIkfTy614Vyf4eoMpHTSM_HB6CjHghz5VTbfeQb6m8R9aM-6NbqPD32L-ajiC8rI199_nHKcLxZOb0_EbvC4q3ZXVXc1zwaJ4za_nZqbbjS-xxCatRRwRmv-vXE_riDngg5abjhlxebzPXqXKpYh8HBS4RQwsbt9WJXv3wohiP0cehVMtugRZ5BraWzfH3gZT37Y_jGXzSPmr0MVlWalof2oHPjKGfgIrrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24794" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24793">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDAupG5wP883gbffodbhRc-GQ0FH0mSn3xPxNLDvPWdPsg9K1R8cZq88dgcDPtowwUQeNy69j5d00RPW6XQZivELgOpl-2-tzPdkAP1RRj8W6BBYOBpyKnoPVWZHcMyjjSxQgr7hOyWiU1p-bOwuwWF2y32jO5iak375EDogaDCzbwFNiJ7LTQMQPYPBAPtG5tN8s1QNn7XOkTA7J_oOmnvwBJF3kTXKIGiK3EBlLspxGoOkrbteIc5rXchGIIfjjrUuidAtPbIkBzu4DFQMJ322a9q321I4cIlPyZfpFTadCLaEuIRR7IGanz58sogTkcdTRkeyibUC2NSzKLVyGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از درخشش‌ادامه‌دار امباپه درفرانسه تاصعود دشوار انگلیس و بلژیک به دور بعد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24793" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24792">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/24792" target="_blank">📅 02:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24791">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uf_vswQvMJfRyR2Lqtfoqhtx1vD1JXju9dtXoIF0l4XZTRp9efh-7-3yqjo3f9XFQpe8luLrPoF7l1-9_MdwN3KL2978FfQwFD_pwbnejfl6KmxyzNxDNZGwGTFYamaTfkjxflPIlML6mikr45gBcIMdqxsE_s4bIBCi2AWzLVRPE6sV6TpRW0OeRj89RBf9nIZq7J2El5n-CFchrubhVibCkJd_B3tcp8lyEVC3jJMtWMPguBF81_UlPQpSbUb2LeodhN4lxvqpLrrRXBIK_GqEKwjbkWRMwpNhmjIHDyh0DU3PA_xn_CF6dxa8VtD6BhXoqClu05Rf6ICh-6Xwog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عامل‌اصلی‌کامبک‌زدن‌بلژیک و مساوی کردن بازی برابرسنگال رو میتونید در تصویر مشاهده کنید. باید ببینیم در وقت‌های اضافه بازم به بلژبک کمک میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24791" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24790">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBQbv9sAN2GxVTbqNtjx2zgbGo-sKGGvgVRByH5pHR6jNHtDHnHIagraAIKmAauas7fWRstL83weFDEWuzN6yvCY7A1lFLpGE6DHKtn3_qL8R5MIUgSZ6rLOFdKmKB8-fuCZ66Mqe0ry_dO-9CoypJU7Vv2cJJ8fMdtrD4eeG8V5Q_qF24LpXnXJgrfLGCTYm4wd046MByK9TH3LtuRGKlTH2fSz8cALm4ScXrCL3EcaJkESevBJcILdPkgAUIsY1hTSlZoBUruCfnWCOVPeMajg2_RZbgZCKUXCJ4e7wlbskfpUbfWQKwgQArD25_k-btcH5IgQJeZGUSaf7Hs9Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
میزبانی بی‌نقص و خیره‌کننده مکزیک دررقابت های جام‌جهانی 2026؛ سال بعد همین موقع‌ها خبر میاد که جمعیت مکزیک دریک‌سال گذشته چند صد هزار نفر افزایش یافته است. اوضاع خیلی خیطه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24790" target="_blank">📅 01:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24789">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7ul91UFSyINwoTYKKR5X1u9p-HsjLjVA8k6bJVaj7tq8cF6wH7d3J7YCGCIeGOMxU_0hCEzwh0qPwKoIlpTg9vxZeGm0zR94P4KfkCqKQpLDKoYiCa9U67Z2XBNqu16FP3sf9l_sZrCZw7P7lxNagOxcTxOiZEWHSs8AhX4xgR9gkCBDNl3Nm9V_uqbVRlmY3oheLxg9fbJTZpCBBnZ5HjSjehI67plV0J2yZfssf4lsk447cG24Oy9feWTsObvAhLsrVIH0Gtc4B2fI4JYxF2Z8IF7hny2x5GZu_WZNiHGUAFFp9RdLJAXnmuV_FLsTHSWS2f5CPQY0WYxLExuug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعداز این‌پستی که زدیم گویا بلافاصله به غیرت بازیکنان بلژیک برخورده و در فاصله تنها سه دقیقه کامبک زدند و حالا بازی دو بر دو در جریان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24789" target="_blank">📅 01:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24788">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy8PnP7gG0nDb6HTT_pfu3WR-x2yOnuByrJzqUEdZznCPPz4mqLipQt1CE2rA04QvZ73u85TkCts5nrMxdV6LnAXj9fhjBcUL01hGcOnX1vNuVR6dj-pozWZ7CXXaSkORxBI2UlaUoqHyzOdIIrOpChWUsQW2cgktQS2HfYlvScyyVRDpgfLrlcY82l05WKk_h6AyXULOEJpWXDCRwNR-_rapAlneoIc1X-Sc5zgBHnx8KcEN5yb-sbO1gF7VLKFfIbJUT55DUykV4OXgfgjlmptpAx_2KLLYE6yKCAZ0F8vMrPcTzYv47XTLDR-wZtA6TolSiXSWvoHikfKjorqmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضع تیم‌ملی‌بلژیک رو می‌بینید؟ قلعه‌نویی داره از چی افتخار میسازه؟ از حذف‌شدن در «آسون‌ترین گروه‌ممکن». ‏سرگروهش‌هم‌درحد سید سه گروه‌های دیگه هم‌نبود.نیوزیلندیکی‌از ضعیف‌ترین تیم‌های کل جام. ‏جای مواخذه داره تقدیر می‌شه ازش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/24788" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24787">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzOkaN0WD0ZfIuvuFJOxJsdN4H1k-TSFgDN6Ihgizf2ICD3PgigN828hIM7gH6NT6TG38l7Bw5nhn7fN-8R5jhTjgWof2_WWF1oyd6BXL3LeYIQg4QYNncuaDBIFrHAPB8ib7IXsUgedSvts-_2pFmk-Uq0UKzGkurVrZ7AJwp01L2RRLuZqESMGwsMJjLCaH-_Kg0QvKYi3jCWEAPXuQ_Ixd-kUujZCOnE4Ap5wiHGLlDdkozDz4R_RloJSQ7fN5BuEVhvx9rvTSsTDpkWC9g9mwoV-CDVFr3lXdS0zoMs_dSumbf5ouqhxzzszXjU0jhT8n6RXFbkjmUhl9K6FDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24787" target="_blank">📅 01:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24786">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24786" target="_blank">📅 01:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24785">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RD21yl0lRgSEUGoc7j5XX644JB10mTdlV73V9tOHQtyWas-Qz5EZ3wCuKlgfZocs0OUjLVUd6eUx-1rtiPt7SulCDrGyLMaB-s8XjH0kz2YfKHSEn9qPk1RG7NLFK5YiiTS31Upoxo8th9UcrN8tXZacE-C4cCXyDKdDgPqwbNGGiO6RzD7dlUYSDLb2JLhE6GGbAg0V0I-5icxM8-1prrhGhVipeRiP37VnDSZXESWId9HbehjE9AyGgERyY_l6EUFUe2KJyFgzyoBHgFSmvW50IF30jrDcsO7zKvia9q49VVvpiVZFiVJav96Dyx54n5VYKmyeZAnkfZA8ouO85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24785" target="_blank">📅 00:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24784">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsuwdhKTk6awCxIv-2uOhh59lYfTSRd8ZMOk1zxAAThXcN7yavTzHr8lujP33PriakNycoReYg4FtaxRC9_nHJPqnhuDgAHiIkk4qJu40LWIRBqyCgNkgZUYS2i7sGd4on9RiMGHreYBnSL1xGoyhU98xm9z_X7UAa5sxWah2jYYhaBk8nYqyWilzjlXOo1w-Xq3b4nzlJlr3j0kp0s3jeTK9F6ZhrL21kC3RILjLCufQBwAx0P_U3PBK2U-pkKlppzGpnsVAxsfoSVeMk42L5UrQNv4eeLdBssD_djYyuK1Lkpe0qSM96fzETX3VppdykT46XwvmUiLm8mDnALnBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24784" target="_blank">📅 00:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24783">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=EzSunUTRtyZgXwl4j72g_1Ly1g0qi5j7BdVF5Dmep8Jhcpue8qBMYfyLStqpPwoSxjHq9t7-vf1MUBv4C54Gb47xWpSSBVzRBJ8JY6A5f9Fc6I6Zj-uhdy3wWpSsplTYsL2tX10MWpFGl3sMQkZd0_vZDgLh38_EyMSsGW-JaQB4cvmnro7AKksaiSIdMR9KCqbald1R8xbqbhKs1xXkgFGjPQdBAUVOPIO3kb81ZkPrdgrDg5fbo1akTnhVXEZ_vGs0X4WHa2z4a3xeOpWwx7zX5d8wmFsqBeJrFro_h7eCk3LMwxDzgznntLEXCWNpsQY2mgHDt45g4UKHIj2rHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=EzSunUTRtyZgXwl4j72g_1Ly1g0qi5j7BdVF5Dmep8Jhcpue8qBMYfyLStqpPwoSxjHq9t7-vf1MUBv4C54Gb47xWpSSBVzRBJ8JY6A5f9Fc6I6Zj-uhdy3wWpSsplTYsL2tX10MWpFGl3sMQkZd0_vZDgLh38_EyMSsGW-JaQB4cvmnro7AKksaiSIdMR9KCqbald1R8xbqbhKs1xXkgFGjPQdBAUVOPIO3kb81ZkPrdgrDg5fbo1akTnhVXEZ_vGs0X4WHa2z4a3xeOpWwx7zX5d8wmFsqBeJrFro_h7eCk3LMwxDzgznntLEXCWNpsQY2mgHDt45g4UKHIj2rHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24783" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24782">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQQA4p1MBoimqsJRiz5fMRWp8rXm83bLyX__c3AtD5C0sy-OoYyVPhxCydO3dQNsGaMDJBFmfmtpKUbgOKTmdqA7i9KH_Z6GTk6_rXuBFoicOXCLSEUbHwOK2HiiOsG252feYB91_y_b2vILIxdJ4wGAQOqyejWGAjJ2vqsG5VJvOqLnPFTvEUXRl4PDHaaXSb8PeljuqN8YVEg8ROVx9XylyqlYv6IADSRRCMIANNE3Jexw95Q58C7QtnWxrDufKZhw8ihmJaaoDvnH9M4_uND542V8qgVDlHD43aJNv-X2HO_5bBQOk6m34QIL5KqPMQMSJBYeZKXey3cDQsjTTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24782" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24781">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtwMX4nBEH1UGxjZR-Bg5lxijg0UCsyxw9-PWrfz_8uSN9uIsVJj8_Ul3Con6g7WN1rRaGsgk8ZiVpACSPbd3FGZfTQZ-DYMnsQHlz489Y4BxkrqTKxz0hTZoykCv_4Blg0ZBlSK-IoxyT1zZ7k7cKsG0sgAWAqXZhIOZ5FuTNx2vEvolH79pOhcupfJeWFclyr0IfgZKbAHHGFBqFUiAw-tf9K4UV04PHhnbtGMKDsA_yK1UUg-Jt18W2XrrFsJWFs7FjrVfpMlgnLt1GGgiZqaaBrLg_YXZBGx2Ubwn-flC8le2PNK0EzePwKYFRoopbUscdjbq3cDRak19yDpvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛ مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24781" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24780">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slTuALv7HQzCUIle_GL0D6gqJ0IIu_VZTdt6fGgFMXUU__Ta8bX1aQ10-LkkromuYBnyql0eJDbZ8MQNpVZTaxtN8XOR-G8rSrnz2cS8ua4DLGvIZLTsJFZOMeut6VpQrxngp_zdOo1UIwGjiuMSf1_TzKxqj-HPRbuxDcAM6Ci0D0hf1oDejPSPWzEM9A6rGprI6lt53nI1lM29Ha6bMwNxMszLEtl4kEmgvIPxvFZoUcfA8wbbc91WDoqZYTyl2R-GvcojPmfc9hGEozvuI_v-S5o1zz1K6KtTNAtKw6DBCV5TJ5Rco5kqqjnNKStLc5n9m-BxhiDoK71BGv4T7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24780" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24779">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32137f795e.mp4?token=lu2YIFyxZCRXpW0qWEp_P7InATZKbw9ZptJGha5c51lHsNFJOnBZtDzrg7N_XVtnTAoHUQR7dMuIbD7JFz3zfBFbUbZ9goCp1WCe2jLVSj0TRrO_rjUmPMdJwfh656o_VbTjwEddINaCEGKFqRhXzBj5SsDHUTTBGqwEwOd7Y2aUTcJAxjcxzdtNz9OAOTEeg1fOJTj5TPjJXNq_O7OwMG5xcMacwgydUGIAEVQSvJRZe9juXrtFdfSLm7Mf-GirrkuJTfT6NTo7W2h2z8-QQuUsd9xk1lZoRyvLlluzeGOxJzlBzh3lJsMF95YIHb4UEWhwcdXUS3_PVkKL7dkTwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32137f795e.mp4?token=lu2YIFyxZCRXpW0qWEp_P7InATZKbw9ZptJGha5c51lHsNFJOnBZtDzrg7N_XVtnTAoHUQR7dMuIbD7JFz3zfBFbUbZ9goCp1WCe2jLVSj0TRrO_rjUmPMdJwfh656o_VbTjwEddINaCEGKFqRhXzBj5SsDHUTTBGqwEwOd7Y2aUTcJAxjcxzdtNz9OAOTEeg1fOJTj5TPjJXNq_O7OwMG5xcMacwgydUGIAEVQSvJRZe9juXrtFdfSLm7Mf-GirrkuJTfT6NTo7W2h2z8-QQuUsd9xk1lZoRyvLlluzeGOxJzlBzh3lJsMF95YIHb4UEWhwcdXUS3_PVkKL7dkTwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شوخی جالب هوادار تیم ملی با امیر قلعه نویی و شجاع خلیل زاده سرمربی و مدافع تیم ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24779" target="_blank">📅 23:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24777">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0SQRgaMeKySqFXbxbiTchrQVY8zfbyLhpXx7nxbvKivKWaSYfZAhT0e7SYLo21n2SOEobwpqAz9vYWyvEr11xJKP81FzUPq70CpErUgZh4p0VlVc2kXBlGP50T68gjNsZ3tJS6b8u5TBov483GEJjcI8ud6bwD7Rd3lAPJZ144IOP363lBZRD-DfJUKjcu9ODPf8s--PrmujxzvWqxAEQ1ycz90u_H6eerPjPYr2oMS0sBI3DTHqeKXHKI-XPvKSDLb5Mjd91hlW6I8S9-m80QL3_VM7u_5sDDIh1I6BoLSL4BFjEa6aDBBoMfDZadoDjZpIbqTklcqfdeLmV-Qqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون: نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24777" target="_blank">📅 23:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24776">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون:
نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24776" target="_blank">📅 23:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24774">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310289702f.mp4?token=US5acUWfg6fvlmEM42xhxvsrVNjEYfG2_VjoqbrCoNk9_WGeZsvvcuGNkrDRA7C55UctzXcUNCnzcCu8meKaIhEFcWZ8kHKD8i7xU2pmkmfrGID1oX2vzDydYU3hAjVg0R1Mknpr_BjwdXHYoavvTJyqVNoiHgJv48spO88pZz8C4QKjbkdO0wBBabT314Lp0g7gWJvZ_90OeQuwU2dFMT-SG67utZIUpSL2wx97XdweJgTIHMKprq0b_LDmaVFsSCct-7O8PP9Xlgc2uFbu9pYcwUYlR4OMzpIyX-OyQ2lsUbJUL9CS5pFGXyEe5K8bIk48YXuUU0mJrsZruaspLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310289702f.mp4?token=US5acUWfg6fvlmEM42xhxvsrVNjEYfG2_VjoqbrCoNk9_WGeZsvvcuGNkrDRA7C55UctzXcUNCnzcCu8meKaIhEFcWZ8kHKD8i7xU2pmkmfrGID1oX2vzDydYU3hAjVg0R1Mknpr_BjwdXHYoavvTJyqVNoiHgJv48spO88pZz8C4QKjbkdO0wBBabT314Lp0g7gWJvZ_90OeQuwU2dFMT-SG67utZIUpSL2wx97XdweJgTIHMKprq0b_LDmaVFsSCct-7O8PP9Xlgc2uFbu9pYcwUYlR4OMzpIyX-OyQ2lsUbJUL9CS5pFGXyEe5K8bIk48YXuUU0mJrsZruaspLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛
مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24774" target="_blank">📅 22:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24773">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Me3X4oa4GkoXHeYxDKS9SEd0Cf5G-jcFhJITk6gXs2-yrEzkVtUEyaFMuTnA6zUskPyuX_DRZnq54m9S3wud-Jt8qHfRj1ArJUiyTFfVlhxwGx0KLmtj4D5K5u-k53aEU_6ZicZtKRiDXQxAd9yPXpNf-n1kyzdbjWCeka9cQAxOC4XY8AxDJhgKuRwo3plHrhprisFF9pOcqJyQoT7iyhBoWJCTOL02St5tJe55NCBW_mZtEB44bwJt7HIfZ-Gv09FdAa4HtYqfuDTERzA-Fw7Mj51Xqy0RCWB_4a44gj-hD00YPqoY1F_P67-ceEJ1umYpFiC71qcEuLZZmGWeTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇧🇷
این داداشمون کل بیخیال تماشای بازی برزیل مقابل ایسلند شده و کلاهدفش‌از اومدن به استادیوم یه چیز دیگه بوده که تو عکس مشخصه دیگه:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24773" target="_blank">📅 22:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24772">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeIfSAE4rU1IkQp5AEZZuAYbPM8CleTqMf12yEYUYAJS-0tHD_x214BKc7dbQvKyRKXa0CHuHJBLOt8XAqoOW-Cby54ilWR-FmZyWrYHPF_9DnIkes3Wtu4NhlPas8FW9RayRe2i7uvmAXoHSCkUNf2pAwG9VOsKsGFROBlwVX4eJHTsDqdshTwn8hJGTgpdxrWRZGMAuc9VzK4xLj9F-YM0o6c7VMqtqdu5ixuRivzidqZfVaY0St08t9lIFUE2N4weJrDtuJ1L3ndgkviWlbRASkO_XT1nLMBw7u0cxjLi2SpHh9maUWtoshQPIiMaH34hUPmmvlfPFAe2Z3y9dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبراختصاصی دوهفته‌پیش پرشیانا؛ یاسر آسانی ستاره البانیایی استقلال ساعاتی قبل به تهران رسید و در تمرین امروز عصر ابی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24772" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24771">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=HTb9cSCcNBFEK9M4dlJ0kv8vOnp9UP99mtO3tmh3nkZQxlHCatc_KsBZLrx34q-fKD5R19SUQHB-5WSzMnLiGeTcwBYH5UtOrgdb5aZHl7scmPSDRgxAxlho8peAufxvG-94RMd1u5xrDRr9pVyU6uK3Z7PYDrlXImudFYV4wtObqYrG-a_1QaIp8RTtvTenS-QQI9LOWu9zI2u86at9e4bAD2b3WW8dnVqE0EO5iAlxcAgCUQO3EGktQG5FrrHgpL3jFRM2-_aLLFMMyh-6dILWEGaQecSqpmTT4-zQTGV9enEAkzTGSG1m3NpZ28hTC_QlYIa_J95PvEk0qXCXdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=HTb9cSCcNBFEK9M4dlJ0kv8vOnp9UP99mtO3tmh3nkZQxlHCatc_KsBZLrx34q-fKD5R19SUQHB-5WSzMnLiGeTcwBYH5UtOrgdb5aZHl7scmPSDRgxAxlho8peAufxvG-94RMd1u5xrDRr9pVyU6uK3Z7PYDrlXImudFYV4wtObqYrG-a_1QaIp8RTtvTenS-QQI9LOWu9zI2u86at9e4bAD2b3WW8dnVqE0EO5iAlxcAgCUQO3EGktQG5FrrHgpL3jFRM2-_aLLFMMyh-6dILWEGaQecSqpmTT4-zQTGV9enEAkzTGSG1m3NpZ28hTC_QlYIa_J95PvEk0qXCXdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24771" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24769">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=GStvEuOvnP1hFZ9zkH49Lwo3y55XcfnKEHjvWYQp7vGfjhhCx_cgAKAPMuXxfdlRpgkI2Ch_NkOk-2xJVUudyl5l-BVC8qteBzGO9LMnJILjJ8eI3_yDZmLk0e2geQmba4o-hlNCl0qKb2ccFVw-ChzMFipxxI_XD8u3eN4t3Pi3kxBCS6DWwi6UMGafkF_2MhxNDMBKh0J2AeYaeCuFEF7OkL9glYiDZHRF7FYPUE2ob9-P4GpSM0M0EjfCQ5kIldWqYrdddzYzVpT4DP0SLrkCOrGGiCgElyngJgaTn9GhmRfB6yg88bFfWzMHj5h8VjmubRihBvDznzyKZI48PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=GStvEuOvnP1hFZ9zkH49Lwo3y55XcfnKEHjvWYQp7vGfjhhCx_cgAKAPMuXxfdlRpgkI2Ch_NkOk-2xJVUudyl5l-BVC8qteBzGO9LMnJILjJ8eI3_yDZmLk0e2geQmba4o-hlNCl0qKb2ccFVw-ChzMFipxxI_XD8u3eN4t3Pi3kxBCS6DWwi6UMGafkF_2MhxNDMBKh0J2AeYaeCuFEF7OkL9glYiDZHRF7FYPUE2ob9-P4GpSM0M0EjfCQ5kIldWqYrdddzYzVpT4DP0SLrkCOrGGiCgElyngJgaTn9GhmRfB6yg88bFfWzMHj5h8VjmubRihBvDznzyKZI48PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هواداران تیم‌ملی‌آرژانتین میگن: آلمان داره تقاص این فینالو پس میده؛ جاییکه این دو صحنه به راحتی میتونستن سرنوشت قهرمان جهان در سال 2014 رو تعیین کنند اماسرنوشت جور دیگه ای پیش رفت ولی حالا آلمان بدترین روزهای تاریخش رو در جام جهانی تجربه میکنه. تیم ملی المان بعد از قهرمانی در سال 2014 در سه جام‌جهانی متوالی به ⅛ نرسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24769" target="_blank">📅 21:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24768">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOS-Nj54uKMsC89cbB6ZM-4Moka2xOz2ggJQs7lv44a13PBI3qNK2fLSPxL1uWjBcHy_9wSaM_WJ_k2uyvUtfkQaeT0VznrSIdVpLBZqYL0bnsh5bgHDvuyOfwwjOQZZoP3QCPQsy45AuZ5JX3ElIyd7tJyLwGKOLxv-hFD_Oi0KLe0GFnPUtIqMMUj_n7qNdVjuvge-n1hkYVIL84NBM85bMjoEYTjsfiWgf2R1l6oiZ09v1o47EGOx7buUkafYywmXSpofQnE8iHHkzZEAwFDY8emDqBD0q6XY6b9VLwC9zhma9sSivoSIZOZsZZKPU80yG7dh-9Xj4Ks8zBB6wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24768" target="_blank">📅 21:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24767">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7TMxiQfuy-GbvLVbgxaE3-as3LWppioKmO9d-xeYBvTSGNzK3WyS6lJASeIgfqMJk9WTQC4DjavRkZeiXEWzYihBDVZG8g17CRl-WeJA_cZxFUHpFL2XUjpoXlmld0txCjPGDnHts7GBEe3pa1gpDKhUB4yZ27baw-h-pDRcF5QY0xQmsv5NsokfznIrgo6V4RWizNrqZoEiAvKbUfBQd1DpgqS6p4oG5fgyWyRX38AOOL4pmGHXaA6M86d5VmgLuvXA_wnbHg8YxRjI0iOkbsAeB6v325oHRuN3pFaQsME8lboURKatR_a3M8wvgRcQGP3gB9zmrfChVbaN6AMxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه‌بان31ساله کنگو درنیمه اول دیدار امشب باانگلیس سه‌سوپرسیودیدنی و نمره فوق العاده 8.3 دریافت کرد... باید ببینیم نیمه دوم هم میتونه مقابل فوق ستاره‌های انگلیس مقاومت کنه یا نه. بازی نیمه اول با برتری یک بر صفر کنگو به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24767" target="_blank">📅 21:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24766">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mjx8rKLxEzw7TJrQQDYcEXPtvnYzxz7JeuFzEulVkduGSxOgjfFLji5I7M0ub2L2MeP7sokAAzRWvntZ9hyFRgUZoPpd0Mz6OkXcGGqJb0QQUzIo2iyxrMRU8Lkh0PdoP_JQZlMAswsyzsvuK1PNGx7YTUBvd0l3BO2hR5aCd89ao5i5Ajw5PnohuMRaFhMhroIqCNMluy7E2WnrMif_iZXfntLeNLsTwzDbs9ytA95G28NlQvlVt1aEwTFNjmp2wxThlVkz_N9nLaIc2TptYf2pw1iSpTWB5xe6R8J3izowvJFsgGan7N_ovbhE36h14nKrZngWwWOd-Gst-1VtSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24766" target="_blank">📅 20:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24765">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=rpO9xJTMoQA31mOHN2Lz2YcoCyNmsdxlwukjvqNfuhbg6KqOha6Yb3CEEJdQbyNdnWj_LnycV0nyhFnQblX2fAyXu80dqw63EUJhI2FV8cQCzZ2uBuToNzPKaLIUmmLx-KQmKlUDEpq6WbeIijuapUPsfutHMvN7nlWb6tFny01lAl-Wb_Ae3ohZ1kNOep2YHbkJmp2lG0LDnIisvA9pKUquZ6Y2hS1nM-9MiCejBWOSWkryW4_iNOFWuwefZt72ygHF2q2Ghl0Um8w639n_Rh3XwJU3S33o4Uzqnjx5V4wkv_eBXtDAcu7WZCZ1-YfZUf4B8K7WGNAxX7BYbmvP-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=rpO9xJTMoQA31mOHN2Lz2YcoCyNmsdxlwukjvqNfuhbg6KqOha6Yb3CEEJdQbyNdnWj_LnycV0nyhFnQblX2fAyXu80dqw63EUJhI2FV8cQCzZ2uBuToNzPKaLIUmmLx-KQmKlUDEpq6WbeIijuapUPsfutHMvN7nlWb6tFny01lAl-Wb_Ae3ohZ1kNOep2YHbkJmp2lG0LDnIisvA9pKUquZ6Y2hS1nM-9MiCejBWOSWkryW4_iNOFWuwefZt72ygHF2q2Ghl0Um8w639n_Rh3XwJU3S33o4Uzqnjx5V4wkv_eBXtDAcu7WZCZ1-YfZUf4B8K7WGNAxX7BYbmvP-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش:
تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی می‌خواد کجاش بزاره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24765" target="_blank">📅 20:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24764">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toKkD3d5V6Cz2kMLbnqhUJVHa0H0dk-_269BneEZKbw4BhwT9nyIFu71uJRZcM0gnrFSWtQKCM6eFeZCh0WXGhn35PG7qixLQlyQFSsUJcb8sjJnTeSe1hja3d9JOYfBxu9w4lrkfv7FlHmc_vkiv2YsT62bhYIQLpfxRzacGqmjtTcMlMQ9rcpHIpR7uW7oxdFnChFu_0corqGXAnlfLVPj29-z6ZdVabBx1Fx3gbZZfpxE9DNjWm_wcwYls_sZtgHoRWO87dkYPMCJwAnLxcMRHZPcATNQoTSsxGQvtYEXs1DeSWMv7_s42-k3wV7-37fQdU8zKGUsP93wqwGY-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره تیم‌ملی‌مراکش در اوج روزهای سختش دوست‌دخترش او رو رها کرد چون گفته بود که اسماعیل نمیتونه یه زندگی لاکچری در اختیارم‌بزاره. بعدیمدت میگذره و سایبری‌باقراردادی نجومی به بایرن مونیخ میپونده که دوست دخترش بهش پیام میده و میگه من روببخش…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24764" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24763">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=fFUv1pmvDqnsJpm2QPOHbmM6TbhTyKlv0Wmo4aFOHtQlit4qwZRuoCgSgze5i2XLgN0TfZ51M6PcZBivwX2QyDhGij74SASIRjoKAPoroMIJA7yuQva1Cp5rBsEKBPvvekXu45CEK4eUJphVeSUIBBu6XgY0AvCNiraETTM3eAfurJcszJ-4EE8z-ZMVWv5SAoaNgTACrWDpvASXcC_riuMnZZMQQU3TQsfM36mDDq4m76VKSxDU3Jh_oLS0mxIhdbT2ZIC8HwwoYX0bCOBge497LszHvoARw-X5u63TkL3yabg42X5nraH-hI5xtfd8wb5BCBVHojTHPreyW1T7Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=fFUv1pmvDqnsJpm2QPOHbmM6TbhTyKlv0Wmo4aFOHtQlit4qwZRuoCgSgze5i2XLgN0TfZ51M6PcZBivwX2QyDhGij74SASIRjoKAPoroMIJA7yuQva1Cp5rBsEKBPvvekXu45CEK4eUJphVeSUIBBu6XgY0AvCNiraETTM3eAfurJcszJ-4EE8z-ZMVWv5SAoaNgTACrWDpvASXcC_riuMnZZMQQU3TQsfM36mDDq4m76VKSxDU3Jh_oLS0mxIhdbT2ZIC8HwwoYX0bCOBge497LszHvoARw-X5u63TkL3yabg42X5nraH-hI5xtfd8wb5BCBVHojTHPreyW1T7Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24763" target="_blank">📅 19:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24762">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozIA4sLYzbfQIZUHW2dkzIxSRDut7ELpm2yHR6w4zeE470BotpPEuaTdirYnnWAX5TF_Vwsfmfhd0gcsJuSVvuti_DLEbGELNT1s-rI3lKxNTISEmbuOqG9UfQbTPOsVNqSrvEvxD-PRCMANVCD2JlVkRf0OrWgHrJy70Q7_u5HETp6TppIOeBb3ZcpgKg-NdcXZfJgIH_-Jo7S8aU0dY7bUZwBDAxRyIA_ilI876NK2KiXrZ4Tb2tGYo_z1OAGfwDgGGaCyL9w9pPCpnidQulXEufxJGb_9udmGsXYT-SAF3nw9yDAGNjnvh1y8XZYo-Ig26atHuOvLgjWEjOgcRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوستر باشگاه پرسپولیس برای اوسمار ویرا به‌مناسبت‌جدایی‌او از جمع سرخپوشان؛ همانطور که وعده داده بودیم پوستر دراگان اسکوچیچ هم آماده منتشره و بزودی توسط باشگاه منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24762" target="_blank">📅 19:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24761">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=nMkZi7hKbpAmh3J5lfjMCnONXxuADSzw093RwR3IzRE6p-3_4AMO9lOtqUbJXEah5gEg9qm7hLs2kTWws3JISrEkD3hO4vamyALuBXFOfPBqzJauQlq-lsk3-CsFBOLXoeml4MHUzwy0e5yAcuAJt9vVvORaBrXbIgRzU8y3AQD2YjFalC5ZH6U5Z0EU5h2oFurThIBFtuB2z5YMeFilJof69nCcArK5l2PFyp4fxexMbCN4oL7WXfIKFcfzuFlYyrbqTI9lDGXocYS7tmaA6JOLr5Z4bKL7IbGh8hIZY4-aXze7mgv7wtMB0avmR65o2LSYVI7f1KiddEywwdNJvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=nMkZi7hKbpAmh3J5lfjMCnONXxuADSzw093RwR3IzRE6p-3_4AMO9lOtqUbJXEah5gEg9qm7hLs2kTWws3JISrEkD3hO4vamyALuBXFOfPBqzJauQlq-lsk3-CsFBOLXoeml4MHUzwy0e5yAcuAJt9vVvORaBrXbIgRzU8y3AQD2YjFalC5ZH6U5Z0EU5h2oFurThIBFtuB2z5YMeFilJof69nCcArK5l2PFyp4fxexMbCN4oL7WXfIKFcfzuFlYyrbqTI9lDGXocYS7tmaA6JOLr5Z4bKL7IbGh8hIZY4-aXze7mgv7wtMB0avmR65o2LSYVI7f1KiddEywwdNJvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم ملی اسپانیا:
«من اصلاً دلم نمیخواهد که‌همه ورزشگاه‌ها تشویقم کنند! هیچ نیازی ندارم که در همه استادیوم‌ها تشویق شوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24761" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24760">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hir6g2UZK1Dvrm1KNC08wAnYRMKZy2WqN-B35WwGp6_UNnfGfV-5BBKMB0NsiPGHK-8Z9JzvLZJhC9ECXJAD-rSgclAD1fD8y4ARxRSARgWfcFTBCoc2i1CF4RqlwuzBk9g7f7jJpeo0g6NfWXYVaXr3fvT3-uOeoEMlZm4GVRW2kyOl91jvGv1PqFSg-CtBkJ6brUsGTo_5mvhB0eY5z_1fP8wOhxg8sACEMEw1eoNlH9-lZ6TUEerRO9ESVvjLTjJdzH3NY7x2gIPOGBPCMuM4f_7amf6b3UcQ6XyAlYyZTAJajL0QuvmUkS0l4ap3_yY7Lx7FNZdfBjCEG2G8GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24760" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24759">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMt2BVvC3-i91paWNJcSRm7x6Ir981Vp9v-ZdJATW4l1AB774MoMaOE4-XGqV4h4bvoGmc6-g6_tNX2pp73hu7aeVWHK5hLQ2laqngzu-wND07VEbK_v-v6m0ES76HBIL6E3kaJ97Z2Xi3_fOED0MNm50493qx4Q0kGGS9cqqmyiHF_VuQgze0erqgEbbXlsEIA7jDhGe3EPFfB0jJLy3sZV4jXH5LMRH5ggVXFpBNtfKW4Fi_EI9-qwMyDWd2Yghzy_xIJ_ljHsk9H_sL4kttjv5tvebO35Lqv0a-tiIJ7S75DXuc22EVON-1WYwvk6-6IU2D7Rk0APZKfmRPspDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24759" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24758">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvxQbkw_CfzBWBqXU-sB_4iUPWCLRaoykZqIcCcxbLNCJd5GcEha8mg-DrU6xrV4adaEzuVH-RkXqQIQ1n7kdI7WC1i7MQ6Q6TvlfpBG-Sw0HJs7U9wYK2AGS3fOh7iZZ4oXC9Dg330Oh40t2INsX-5LSj3Mj5Hs1p7rES42R4kC18EImFDj7LdbAyKFX4RLqxyp87Dc5i85Q5U0XAzRajJC7bw3ATrOhyco9UrvmPqh0ealuCOpzLvefjIG1oMkIB9myGjctFxR5btB25hxO6uBJS8HHYyRLs1tLq9S9XOozY8utaMTuwECHC_6Mz6ZVGrwi3DThmqJyn6P6R68gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24758" target="_blank">📅 18:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24757">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRvw0a63JRkFI4q6Ct__YcZENG7UDU87WzFJ-gPW11rC4vAOUsiWn7cMxtVmBrC8-T7kA_HGkT4qJUwQCeqKN0Y_J1kRXc40AHPeaTayrcQ8wEfprvVh6G--yUDgp_eRNzyut9A2N0h-JyOmJB0G5uQts_GRJOdaXI_SHyYH7z2-KyoyDn3b3j1v5d3ptJMRtFNEetruPp3rkRa9m-0bh0N4dUrJBU79XEzEM0S9lVW9jhKl2UiVwkj8lQta57bG1zpjTBKu6QFR90bm5-ypwkmjEVUp6dRBUHbjTrn81lnQFXiklu6StBNzMlJDdOfigmP8CMD0jtfSPWXWlA-4vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی
؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24757" target="_blank">📅 18:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24756">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUfEiVZA7O2jlAfrZxEnuRClqwMx7fhoSAC29b80vdY_RZklOqecddpeN0mM23np6CcGZ_-4h_3IRfw98TH0SZePumTlZpWezQAmCDRBSq8lUpCb7cOyg6gLVYAVAQL7EU7ym-snWgP8y1P5lcycjgIk0hfsTKGZBN7DM-6TDOg_T3bXwdQHnu4WNOL12e4Dons260XhjRYY4G6Ho6-FyzWU8H-_TTBBinuRdk4pOdlhHg__gAhW94DLMrr1z8F0huPsnZnqP8uX_OCChXwtK_PbRr30DXltrrQ4QCYH25llYfIymeewfPNeX3rhJLvnxgYNW3XrUspoU1k5o8b78A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24756" target="_blank">📅 18:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24755">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjZm6IbtvjNiebxNRcEik9dYW4a2H7exJCST0IFRCvFVieKa0TP7OjI2O3peEKPAh4hqI_yUFBBWUw5AfjVWs6JzmiYz2dtZWusocxKx7MwRMlYfqLzX2Q0WzLY7bQu64sV9M4DJdirzmPmBC_-M1ey70zRzXbxBtI4VMyr2mYIztD3Uq_pKycahtVzlDjZFGZmWjGMHAYTpWlDChR3q3ppco2EDO7DcSw9Ol0G9RP53J9sUr4LhyWSfdKvkxtTqZ2pcf1rXZ8v4cz4vgMbQR-bTrdMziW8sfhItHhiQBLiQ_iubIdERtolfIADGdvcG8R72xsB6xkS9tuWxvvcpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌رسانه‌پرشیانا؛ اوسمار ویرا دقایقی قبل رسما قراردادش رو با باشگاه پرسپولیس فسخ کرد و از جمع سرخپوشان پایتخت جدا شد‌. بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24755" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24754">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=pf0E4HT5hk6fcarpEdA9ZAOqjqxl6jXAIZj1KtqejDExfBwDU3erEIG2EBm6elGECRZq3u7MV1aEe8Q8QObg0kJqEgDXSctVEquBaPrlUrJkk7qqda7rrIYdXQpORA6zTNrkKn8esKrIMFbX4WFW7m731bIlSd2ktLxFhhLUQoqhrSPyO3xSfU_gml8EjqK9OJmyH_9S18me0Bvf3Igj-29YU8AW5I1CXXENGuR11yXXhascerMBAXu4u2dpP7l35sKj8vNWt6XxHij-mBOO6-NXOAg41ttiVoVUQIJLSvc70JNx1UXJUXLeq9rpIwUYGIf0NADOpObazZYAio5jkguTKMLWFD4tR-7BZlcWzPAsQLb_eTFykeP_7E5_ksDa0EtOJxoJnqEzrw252aD6ZYdUUZgrBlxlLnGBXiX-7OktoT4lkG5lQ4lcMkTwTZZrWThTw-jVjZMPiz2tx_sq0KhZo4LXYEkol_RZESYo7iAnVG17eOnw6e6KJ1zqJ4zcz-lxb4NByiY_Cuq-v73VJWI7M1VfWvVX1j6POuc8Y-j-AVhScOBFlkRmIZF715d6kxjb6GvGYH4oBovmysEEptJKeeIWbDqPbuDEznL7TW59QMbJmdglRt2y7VSIEaKblxKUxpIWLxlhwcUofkCtaYS2S9Lx0JVqC5nTED9XNKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=pf0E4HT5hk6fcarpEdA9ZAOqjqxl6jXAIZj1KtqejDExfBwDU3erEIG2EBm6elGECRZq3u7MV1aEe8Q8QObg0kJqEgDXSctVEquBaPrlUrJkk7qqda7rrIYdXQpORA6zTNrkKn8esKrIMFbX4WFW7m731bIlSd2ktLxFhhLUQoqhrSPyO3xSfU_gml8EjqK9OJmyH_9S18me0Bvf3Igj-29YU8AW5I1CXXENGuR11yXXhascerMBAXu4u2dpP7l35sKj8vNWt6XxHij-mBOO6-NXOAg41ttiVoVUQIJLSvc70JNx1UXJUXLeq9rpIwUYGIf0NADOpObazZYAio5jkguTKMLWFD4tR-7BZlcWzPAsQLb_eTFykeP_7E5_ksDa0EtOJxoJnqEzrw252aD6ZYdUUZgrBlxlLnGBXiX-7OktoT4lkG5lQ4lcMkTwTZZrWThTw-jVjZMPiz2tx_sq0KhZo4LXYEkol_RZESYo7iAnVG17eOnw6e6KJ1zqJ4zcz-lxb4NByiY_Cuq-v73VJWI7M1VfWvVX1j6POuc8Y-j-AVhScOBFlkRmIZF715d6kxjb6GvGYH4oBovmysEEptJKeeIWbDqPbuDEznL7TW59QMbJmdglRt2y7VSIEaKblxKUxpIWLxlhwcUofkCtaYS2S9Lx0JVqC5nTED9XNKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برسی‌کامل‌ودقیق‌شدیدترین‌مصدومیتهای مرحله گروهی جام جهانی 2026؛ عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24754" target="_blank">📅 16:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24753">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=hWxzV82FSfxYPT3JrBMldImyz8hwXa8JZkTAKBrK6gZCEv_KZKwdI1Nf-OS8kakrfpkeyqL58E8IfjnY8AlUify81dnp-JI2Qnbwtv0HqOTW7ZCR7gs8Re8NP5BYJgamtlrfA2eeixpldWEx9LQYN_iwcz8zPb_SQcoEyySw1qtwE_DkohSUq-I1AqfRVXQZYZ9sdJvJVJg43YRoCqXesSncNJDv_cMTYFbY5vy8NEiYamPJjNQeXDDo6yWvqdRl-zbLyl230pny_CtUFmnBxqqqskH5gJzBld0JdDVupdystH_AP8RBY495q6_NN77PPpJhObQ9Km5-QNQTmxF0RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=hWxzV82FSfxYPT3JrBMldImyz8hwXa8JZkTAKBrK6gZCEv_KZKwdI1Nf-OS8kakrfpkeyqL58E8IfjnY8AlUify81dnp-JI2Qnbwtv0HqOTW7ZCR7gs8Re8NP5BYJgamtlrfA2eeixpldWEx9LQYN_iwcz8zPb_SQcoEyySw1qtwE_DkohSUq-I1AqfRVXQZYZ9sdJvJVJg43YRoCqXesSncNJDv_cMTYFbY5vy8NEiYamPJjNQeXDDo6yWvqdRl-zbLyl230pny_CtUFmnBxqqqskH5gJzBld0JdDVupdystH_AP8RBY495q6_NN77PPpJhObQ9Km5-QNQTmxF0RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌فیروزکریمی‌درباره‌مراسم فدراسیون برای استقبال از شاگردان‌قلعه‌نویی: اس چه تقبالی؟ خودِ فدراسیون از این کارش خجالت نمیشکه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24753" target="_blank">📅 16:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24752">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk1nX_XWP-FvkUbzHFDpV6rYjLL6wUDQ_5Doa6RRJWZ6bGiDle18VR9B9RorILGnyqbfWtSIKfBtDs7xSQn0Y3QEXsaItz6xjOslgxbAyFiu1eePvM1iyC9sSjqa9KYUc6vfNFHvLH-VVlP1_7KTLh8aBQfDOUfWumogE8LV9pAfxrnWL4A0WQ3xHHAJK6A6Ok4zmM2EF-Tg2C0PBQLOYQ9HHhcsikGNwrDjo6GBLJZLkm6l-ueOY_CZC9-_qSFB3zFIAM0LZMlh0XZn_qXhoj0zBLjRg6yhWFMQe3bmxFyOgRKCmLLUB6IGoVW5V-lUPk5oeVdSwFVNiMuzKK8HEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24752" target="_blank">📅 16:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24751">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=ueIci-j0DVJOwU19tV7OVvwJh-59sC3mkMz8g_LULsqq6XTAG1ze8f1cSFGoWVnvkcYjokqwOzGHTxtqxJ4PBnlGOnZXYyagMfGQsdcycdw5Zw2jw_RxMcE224oO_d1Ms0NnX9WA7b-GysmFO8YawBx_Xq8BjUi9_C2Vm4m7Qsxm7KMkhU3HMomS6SSK2Ay3jllDawC-ULAPANS7L2gmgF1JqMWIFdGSzaTR5MW9ljZT_XNz5bL-bg9VqTBH5IuR2vlUqEeftorvVVOwDkS6fGtKQaa6dPkGKIo2Db2NibvrU3V9jxngevWwUvq9xRyfHr_cJwpd2ITxP9HP_Hms2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=ueIci-j0DVJOwU19tV7OVvwJh-59sC3mkMz8g_LULsqq6XTAG1ze8f1cSFGoWVnvkcYjokqwOzGHTxtqxJ4PBnlGOnZXYyagMfGQsdcycdw5Zw2jw_RxMcE224oO_d1Ms0NnX9WA7b-GysmFO8YawBx_Xq8BjUi9_C2Vm4m7Qsxm7KMkhU3HMomS6SSK2Ay3jllDawC-ULAPANS7L2gmgF1JqMWIFdGSzaTR5MW9ljZT_XNz5bL-bg9VqTBH5IuR2vlUqEeftorvVVOwDkS6fGtKQaa6dPkGKIo2Db2NibvrU3V9jxngevWwUvq9xRyfHr_cJwpd2ITxP9HP_Hms2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نقل‌انتقالات
|شهاب زاهدی مهاجم سابق آویسپا فوکوکا به تیم‌جوهوردارلتعظیم قهرمان فصل گذشته مالزی پیوست تافصل آینده در لیگ نخبگان بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24751" target="_blank">📅 15:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24750">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‼️
دیگه وقتی سرمربیت اینجوری بهت تعظیم میکنه فقط یه بازیکن ساده نیستی؛ کیلیان دیکتاتور
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24750" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24749">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=O-9fO55A5VX7EQfC7FhCRQ5Zr8PmoOr5NcfH75Zh4jeVdFq9UCI76Ob-OT42MNhIIQ5l67SvmbnGDA77nEap5mbpylExJ11ynQNbIPe4AYCEcupgtdngNEUNC_n7rsxqlGeON5E-yj917kvC97eq3Qx-mtny69hTcnIg31f6C5GC8aHkgpR14RkzmPaaohqQOby8kbh-_oleNxZFEHT3oLbbsPhJdvld1bfR6sn7pssFtvZgxZR7HOjS6O2Mqc6w4Voj5h07oLKTOMic-FuhcLvOeMETUbC3DMQRvzLiHcRhXm6hhgQp-ltG_ZCAmFFCfeFB6JbnCVZpMq-N06Wu6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=O-9fO55A5VX7EQfC7FhCRQ5Zr8PmoOr5NcfH75Zh4jeVdFq9UCI76Ob-OT42MNhIIQ5l67SvmbnGDA77nEap5mbpylExJ11ynQNbIPe4AYCEcupgtdngNEUNC_n7rsxqlGeON5E-yj917kvC97eq3Qx-mtny69hTcnIg31f6C5GC8aHkgpR14RkzmPaaohqQOby8kbh-_oleNxZFEHT3oLbbsPhJdvld1bfR6sn7pssFtvZgxZR7HOjS6O2Mqc6w4Voj5h07oLKTOMic-FuhcLvOeMETUbC3DMQRvzLiHcRhXm6hhgQp-ltG_ZCAmFFCfeFB6JbnCVZpMq-N06Wu6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یه‌فلش‌بک بزنیم به این صحبت‌های مهدی طارمی بعد از دیدار ایران - ازبکستان در کاپ کافا: اگه تو جام جهانی پنالتی برای‌مابگیرند من نباشم کی میتونه توپ رو گل کنه. جز من هیشکی نمیتونه پنالتی بزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24749" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24748">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiFuO9abAREGC36-Jl-TAALd6dgG_D4mn4SZrxGmc03UBfz7XUsn_9RVYvJ1tpkSmTX-h05VUciLx4esyrqpEauEEvHX4Gpnk03lhvSD5TCWsVEAVc4z6QTHk6IZ0tZvQ_TrLEaCJ5p7irQgwzdhzrQaZxqkBO1Aoev9askvsTE5e-qVtGKRJmuvVQjp5DMj6DI8Jbyg4CI1jlU0cBAV5VodInCRGW3DU8byUUWoGQALSv1T659bNukFS7h36Dt-lD-rADUabNBgOnigTdlvWDAxgym3qWpFILXv5Gr36zCoZFpX1ZzXdpMMYrEgTJWxi3s0WrGcrJKqQZ9y9GG26w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرمربی اکوادور که خیلی عکسش از لب گرفتن از همسرش بعد برد جلوی آلمان وایرال شده بود، بعد باخت جلو مکزیک استعفا داد. اونوقت فدراسیون ما برای‌حذف‌از آسون‌ترین گروه مراسم استقبال میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24748" target="_blank">📅 14:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24747">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juuK3g27bLKcqQ-n1hu9wGr0knsi4Vvy8sNsYDNYGI2rW59I4WHZiQ84m_8J4CVa3Pok1tVVPExKpFRF6C_l6-MtyzJsk199OgsELKk2PUSZpTA1tS-ttwz6cigClvENrKNyH-mjo4_KudYU1Y_K5ym35UnftpUCWmzFX5y2D3B6DaA_BZlHFI58CDen6Dq1oqwn3CntUB3ttgnCC8BFBf5B005EoVs-w5avz8VIWBPB-aJUmeg6ikc9R-tjX11NKAJF6JTBd9BNrZZOdxL2AHXdHoWCgS5mkWIFRnts6viVmKuINNH4_EuBTKBxMsVYZG9cJ5N5smwVK3FWz6gT8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24747" target="_blank">📅 14:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24746">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngP91lS63NDvvoOHSsM2XsTmpEj2ZcrklmzIn6qT3KtW6ctwdVjJMMVryAZRUtieADpbjTEhx35eEpPijGOWWvwFrGmCXJUg_fIsuK0gvbEkzYTOB3AT1Y0aq8hyhsJcIGQNjA4UGqdPJFq0SxTWQdgz8Os4fqR9pcFgv2Uh1sYNfvfKEnQuMeVCmVxUGKwT3ey5JwkD8LqPGrnps8EX_4TnBMPZEeAkWDgS1LYhEdGjNLbbD9uPtCPwQENV52owN-1p65mUwaDYv0xQzbr8-sN7y-nICKw7W98ZDBeYN0nXtSsYNxm2xF2LGpT4GNDTjWQq0mw_g_ukkMj8l_cR7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان با باشگاه دورتموند بست.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24746" target="_blank">📅 13:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24745">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxH0MMkUCIozEEDT2b3QV5zubdJYjl-nrBhTa5e_WN0vu6A85Ns4YDnz1ji9ybbtU8r90vf5n6qCQDh67Esli5L6yziRKeq_6OCbeUe9LhDXtMNs2IsGo6XhpwEWkeZjljBojDo_4YPebjUqofNet3yUEjuJe-c9uKo3fI8ifGDBkfJQp-Vb8GuUULQRTbuzXDyfzTeSNOJ4EwNO3uHtDLT4uKHZEme-Hg28v6oiwolQZGTleC4uT-8o-UJdp66O0RTE2ssbWrbtAAoQzJFtcbjGVjp50bnPekaf1k3i8-hz7BW4ILcBmPzYQMcD65cGFkjKYR13uYUopFKjPgH_gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه‌بان تیم تراکتور از شهریور ماه سربازه و احتمالا راهی سربازی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24745" target="_blank">📅 13:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24744">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=WkVCueCKs2v6B-HsdH9TPegw5a0SxqGZJUSGJG2UW0OOiAyP4r1HrHevAtc1yuuhZWa-r7DTLc_OD8eUREcySBkCYXLs0VauiLLaGlNLbRyzFCHMDRDpfxQRBj3JsZcfCulQLCmSRRPJRBhapvxB1V1WHDt8GPESOeFkXeiIs2bfha-h6QtWT7BoM8uzJskTSb9eOn2_hnTVTf1nrl5nr3rYDmrgTeGhi5Y9l5f-KSjELGpWSLfgpbn4VrKcqiBc9MvEj_it5UyIqUA0r-U29yjl6q4Tv45TeSWTpvXquoyKm3jRpXqLCq_ztONqO_DBH7Xf9XDRXHuPYnwla-shSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=WkVCueCKs2v6B-HsdH9TPegw5a0SxqGZJUSGJG2UW0OOiAyP4r1HrHevAtc1yuuhZWa-r7DTLc_OD8eUREcySBkCYXLs0VauiLLaGlNLbRyzFCHMDRDpfxQRBj3JsZcfCulQLCmSRRPJRBhapvxB1V1WHDt8GPESOeFkXeiIs2bfha-h6QtWT7BoM8uzJskTSb9eOn2_hnTVTf1nrl5nr3rYDmrgTeGhi5Y9l5f-KSjELGpWSLfgpbn4VrKcqiBc9MvEj_it5UyIqUA0r-U29yjl6q4Tv45TeSWTpvXquoyKm3jRpXqLCq_ztONqO_DBH7Xf9XDRXHuPYnwla-shSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاویر ارناندس ملقب‌به‌چیچاریتو که در تیمایی چون منچستریونایتد، رئال مادرید، بایرن لورکوزن و وستهام بود، از افتخارات میشه به دو قهرمانی لیگ جزیره، یک قهرمانی سوپر جام انگلیس، قهرمانی در جام باشگاه های جهان و قهرمانی در جام کونکاکاف اشاره کرد، وی به دلیل طلاق از همسرش به شدت از اوج خود دور ماند و دچار افسردگی بسیار شدید شد و در نهایت سن 36 سالگی از فوتبال خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24744" target="_blank">📅 13:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24743">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntN-Toaqkz-GGLacphfF6JSIoiZNES-Gi0gO52a2kesr7EQEKv9Ao1g3ckqe_6tBSXVBDypdWB9ZCzsgwkhiDRkVDUziBUQko7udagHQxI9EoofA62lnRe15XcDD7_4Uxa5193PoR97xFwAhTQA30kO-wAp7QJcaS8Tut15grFstbSTge801bqu77QWgQwk_RhUHFZuWrx7J18LmUUYMJioaYbWr4Tp7ZuH-7mPIYM4mx5TTs-pVqki7VDKh-YLe62S5AOhWk3hRJtbi-nzHn85dT_qdAmse1OxiGOa3pZRAWru7blGWUfRMCehXosrppYONh_jeBnUU6Yq_ctJr7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24743" target="_blank">📅 13:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24742">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dc4MQvrIB3GRoWVpFUhEdR9UAthPxwirreGergTiR5lZiUzp_NDyXxRKpB4pFCOpYASJmzbqHvmT-7kekTAGBKM4OR0J6PVHQGP6gGFjrAaM5nPXemLzkRC6Ob0LZX3VMXgoKTpw9ZImBOptlsOnj1wxEt8QQLKcvJ_D7rgqh7BGGYJixO1f2T5VPNae5IKHNQQFiARcfTcA7crwHwl_QoadN2wh3OiqH-EyGQgd4pE9n0P9YNyu13MLwHSItzm60iTfebhbeM0EJCbJBr0IxGnFRqUD8kK0ALabB0KvpjQRYqVDCBx2J2c16hmG6nA5tNTKYdgely5Fj6EdkLSisA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره مراکش در جام جهانی ۲۰۲۶ و بازیکن‌باشگاه‌پی‌اس‌وی آیندهوون که اکنون در آستانه انتقالی بزرگ به بایرن مونیخ قرار دارد، مسیر همواری را برای رسیدن به این جایگاه پشت سر نگذاشته است؛ او در ۱۴ سالگی به دلیل اضافه وزن و عدم آمادگی فیزیکی با…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24742" target="_blank">📅 12:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24741">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=IEXJWcpkrZ4Q9eZY72sFwo3EDu5PhicP4CxaaIgnxi8ape2nEiqmr2sq1rn3UdKXfQ3vV0qXkBUdn7SlErh9tLWuTgXo7Svx9xShLy7oJ__Bse6iUE6fAtskIp2o0gn1Qeuhbz_uWx4UfgYtPEX5_EAHpBD9UIZeY_mLRvZVsaNshTiR7U8bl2ZHW38k4CzXpxj1Ow9QMYMN9rl3bkYK8HtI3VwQvYEeeAOnyJ4mU4D47El2bIr1hZOQNBJrTtOcYQndRclG5nmNPwh_h0m08sCxh-zQViiauWwYTmiO2iGx7qTOmVLW3nYH5WuHudp7xoKZP1KbjAamPPSE1egszw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=IEXJWcpkrZ4Q9eZY72sFwo3EDu5PhicP4CxaaIgnxi8ape2nEiqmr2sq1rn3UdKXfQ3vV0qXkBUdn7SlErh9tLWuTgXo7Svx9xShLy7oJ__Bse6iUE6fAtskIp2o0gn1Qeuhbz_uWx4UfgYtPEX5_EAHpBD9UIZeY_mLRvZVsaNshTiR7U8bl2ZHW38k4CzXpxj1Ow9QMYMN9rl3bkYK8HtI3VwQvYEeeAOnyJ4mU4D47El2bIr1hZOQNBJrTtOcYQndRclG5nmNPwh_h0m08sCxh-zQViiauWwYTmiO2iGx7qTOmVLW3nYH5WuHudp7xoKZP1KbjAamPPSE1egszw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ته این داستان شد عزت یا آزمایش ژنرال؟
امیر قلعه نویی سرمربی تیم ملی در جمع مردم تیخوانا در زمان خداحافظی: خیلی دستاورد بدست آوردیم، این عزتی بود که خدا بهمون داد؛ وی پس از بازی با مصر گفته بود گویا خدا دارد من را آزمایش میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24741" target="_blank">📅 12:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24740">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWiq3hvQO8L6I2WBbJ9QYYmvpTPSaIUrEGSrymaI9Sfs860thK1QRRnAklGU5IaUaOPRlB0ho0Ap3GTYZQjzpYfcYX1fOdI5J2hXHVsi0gceSX5uY_ELjTReJbKM-EUjIid25SsBOqhxWe5P00RFekRbdJZk_PCX_BoN3bhJxpzFEx0wMMkbAVPaIegVyOWJZawdfxKZgUgo9xUcpjZwnuzJOnoSs0gThf8Y5Lfp4zHfoacDs2kJqEScSnlQWPSBssg1jQidcXjvb4yGZ-Fvb4L5OFo28iQKEAghwcwXNnKE-tIX4GpuS3zud-xZYSPNVeK2jNj5Id19l635LEgwDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فابریزیو رومانو: ماتئدس فرناندز که علاقه زیادی به پیوستن‌به‌منچستریونایتد داشت در نهایت با عقد قراردادی‌چهارساله به تاتنهام پیوست‌‌ فرناندز بخاطریونایتد پیشنهاد رئال مادرید رو رد کرد اما به یک باره با رقم فوق نجومی سر از تاتنهام دراورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24740" target="_blank">📅 12:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24739">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/er6crecKGSUlR1VdCm49rT_d2J_UVMM9p5PXiIuW8JyXMU_TvsQcTaoF5gZsk6psN-LzX-F8Pq0FYFbYi9lF1B4y7HX5Xhr2cBs0KN3sAcOOSMMOqKlwL3YZ5q0OS3deZxFceRmTt61XIpnemvRTeU6Yui91SyoXHNUm-Iv5ULP-sE5rU9n0gqILPs855F-Ejq-CD9eeeGPYlfHj8RmLT0ftkli7m6YHL5DniJ_lorfcoGONPKRPgCuJt0GCDfIgUrcqUpceohKIKeZLvnfIY1FNi_bMWx3PdWcXeuohHKmV4Ht5RxzPZMiACcmTM30qShQFbKEP5JzuBfz8nvNGtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ سال 2016 دقیقا در چنین روزی؛
باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24739" target="_blank">📅 12:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24738">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVb3-gWZEiuzf-XE0q7AJlF_VB8o7goPTkLmQ1cZGfWq6e2V4i0gWih4yzkYk1JI5dusqJBnInEYau3raMgg6eBStxXDaK_3EyLK-1nAeMiw7tUuafeJ0oekS7K1lwuRApH-b8nmXmfq9tn2xDWKshF_21rPly6YH-jF4VViFTgfotzmwQRZOSDeazVlA48ZiNc5tdf2dJlO88jjbFNBvVSRp_RW9zDowpx3Jpy_yHG1UpRhg8BkRdqbMDhjxzXS9dt-FZFvib1ja5TLgXjf_iWx3a2FA6__BIXWPPbw4SILsptZpVaPuZWnf8wKZeTtE1BJ2SOqQY5J0vp5HkE9eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت:
کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24738" target="_blank">📅 11:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24737">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcaXIvHOfP64R4Z394ahEHwlhP6eDh10cpW6nCmfjOnVYZlFXw1SJOSC7Ghic1mDdZFumitAReJjYTRP6sf3q-cjqv1k46oUwdDQBPx5sPWvU8m4VOgyqwT5upnR8fZl8pCxy8wsOe7JgshjWIAhZjNE-OI7xaMz2oj2VGdVRwchJ1B3XCnnPUyXvOJ9R0YhTxr1TOlCHceEbGsshPDDf2UxgCxb0nQ2s8MIURp_hhh1uck2xYe39-APtvJUJ4P1yqiZs4lT9jErTVR94TeE7BNXAJ-ln05DqU6hXlEF-Jrh2v-NuYF0GtBYZZVmvqSPp-niLD6FgcYCF7pdAGHmGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24737" target="_blank">📅 11:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24736">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=jdrpf9e1lAmj45Z4xQXZPdTsKjAUmQivPc-gPsIX_pTBtlhtUynJBfQwl3ugchYTIfvbDmqG3KEEoFs-KA3NGJ1D6eQfgi-WpBb_6ONBLo2L8yOKlMMo8w1aHNDuoSOjIm9eUJXSy9EKV5FB7XnFZApXTbm6Jcga74QaegBid2hQcf7oiAyAvaHGb-15iPtFSBRn18HR40LdpXfue327PDz1VVE2AST3Vt5a-_QfSe7XKsmYVrVlsHzpvfaYVsnJ7RX3Hjp8vlDhOMOyRAk2B6vYyUj53hohWSbnNHt21UFa0glEefF2SZIW0C_5oOPGO_uUMN51QDICLlABuUnJSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=jdrpf9e1lAmj45Z4xQXZPdTsKjAUmQivPc-gPsIX_pTBtlhtUynJBfQwl3ugchYTIfvbDmqG3KEEoFs-KA3NGJ1D6eQfgi-WpBb_6ONBLo2L8yOKlMMo8w1aHNDuoSOjIm9eUJXSy9EKV5FB7XnFZApXTbm6Jcga74QaegBid2hQcf7oiAyAvaHGb-15iPtFSBRn18HR40LdpXfue327PDz1VVE2AST3Vt5a-_QfSe7XKsmYVrVlsHzpvfaYVsnJ7RX3Hjp8vlDhOMOyRAk2B6vYyUj53hohWSbnNHt21UFa0glEefF2SZIW0C_5oOPGO_uUMN51QDICLlABuUnJSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه‌جدید آقای‌امیرقلعه‌نویی، سلطان اعتماد به سقف بعد از حذف از جام‌جهانی با یه ادیت عالی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24736" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24735">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=YaLLXuweapK6a8rrzqB2DIkqfFlpndVLj4DI6td3sY5ojRe6ujtoCXJlh53DX0txAEF1Crm_XB2wb3j8OS_BJ_dLXlfSfeNSaNXpV5Ux424QOPK58QOb9EnsQXMhL1a2T8dXrZ62rsAcpnPl3V-wjDXRddFtxuD2uF4ns8BxXRkIKUtNbfl9P02wF4NlDbsr6Nc1dItChVI2KKRgCirL5YvQWEuFQU6d9_q7t6V3RHaPp9mbHCEUf2gIfm0N8lc-Mz7TFJQPW0nUU6AWq6D1YqMqkYQ8NYGGw3TILZ_5f3VsRSZQEloRK-HaFW6vxEa5PS_OU-tovEJJ6OwjIcFPPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=YaLLXuweapK6a8rrzqB2DIkqfFlpndVLj4DI6td3sY5ojRe6ujtoCXJlh53DX0txAEF1Crm_XB2wb3j8OS_BJ_dLXlfSfeNSaNXpV5Ux424QOPK58QOb9EnsQXMhL1a2T8dXrZ62rsAcpnPl3V-wjDXRddFtxuD2uF4ns8BxXRkIKUtNbfl9P02wF4NlDbsr6Nc1dItChVI2KKRgCirL5YvQWEuFQU6d9_q7t6V3RHaPp9mbHCEUf2gIfm0N8lc-Mz7TFJQPW0nUU6AWq6D1YqMqkYQ8NYGGw3TILZ_5f3VsRSZQEloRK-HaFW6vxEa5PS_OU-tovEJJ6OwjIcFPPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
منصف مثل سید مهدی رحمتی
؛ ارزیابی حضور هشت ساله کارلوس کی‌روش روی نیمکت تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24735" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24734">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBxJhuqbscbErq_QUq0Wf0dPpxmZTEwwp7DdwVaORrm_9cJdm0prkHKnfjnM2p0Y3H43ETBMvXoNAqJRyS-AH_vGFDz44oul3iD78uTCFdVd_ax4JG01VdTy3QlKfqb4yWi2lC9qb9pwx7rycj4Y4YENcU59Oj0FIKfe8qS5ZxauP5S3_rPcbNA9oEkTjphyhuKjjeYeJhqHVAm6R48VVgGfHfqImyvVKMLnTenhCs7fuZyekQrwa0ItFmoQrYW0-zYChIGRTQ1ctYWJGUxOnqMzKD_FMClmbluYmKUbKykAWFvAc5TD8DyBfdB74550cG6mcJMk6ZVuOrbHRvlSMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24734" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24733">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkUsnTUNKiRf_mF66gIRfyoCndLyhHf0xgOu3xfEjwz3iyb6yPFKuZRLuSLij_l9HQZRr9Kwwn5NEpOydPan7jrRpKxJZeHYibWMCD-K8VgRTR30hB8G3FGNiUU0M98DBR7cB_58CkrTZOdUrQs3nvPxsPGE4gAS7X9cTvBm5aFk_SB6RL1_v5FFRafg4fuQCmxRalGFlHwRvAorMeU-flt7L14IhKRS-AhgOhrFL6JrJZN_jXvuEIgIYKa4WylfSaLEnm_KfJlqUFODVMgarkFxKrQnMi6Y_6m1_g1h4aYZZqI7O6y2tkkMdTUMfy1AzuGhZKSzeP1FIRZYz2sWQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24733" target="_blank">📅 10:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24732">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=RK21w8khq40SnuaHUw2JIOWqzarr3p5zc-E1li8sARvCql3LeDZP5WuGv6wDXB9-CaINPXR4-ydXlGXaLeLWupKXqTONwP29FrINLjylizk469CqZnXjodU66jOrKugsNgIRnqu9T9N0MiGd4HH0I1Pwfdf9Dhsmh892LYZ_rzLlLzFoDvlJo_r1Nz-H57viNlDLrs3fSofUOQ6OdZg4Wt11-Rn9dQuiQ94pPj6OD9b42g7AflJcn1yRV236q_60W3mSMqU6fnN2LMB6170wxD2B01g__Nj3udzoLRpx7jKqE5nwFmQQuTp-Mil4nnfBRebKsfE3qDSEZviWsMBG5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=RK21w8khq40SnuaHUw2JIOWqzarr3p5zc-E1li8sARvCql3LeDZP5WuGv6wDXB9-CaINPXR4-ydXlGXaLeLWupKXqTONwP29FrINLjylizk469CqZnXjodU66jOrKugsNgIRnqu9T9N0MiGd4HH0I1Pwfdf9Dhsmh892LYZ_rzLlLzFoDvlJo_r1Nz-H57viNlDLrs3fSofUOQ6OdZg4Wt11-Rn9dQuiQ94pPj6OD9b42g7AflJcn1yRV236q_60W3mSMqU6fnN2LMB6170wxD2B01g__Nj3udzoLRpx7jKqE5nwFmQQuTp-Mil4nnfBRebKsfE3qDSEZviWsMBG5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24732" target="_blank">📅 10:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24731">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=dKqmeggRgt2mjPJ2GPiTYTMPXPWtQnmkjQuCEYHjGmJAfrY2SPYrUov0pKqC2ztbiWGpG8vekhTUghj0A4OZISTZGDzqh6dg2Z40kVLMLhb4jQH2Se3uLnc-Dfkb09W8Xq8xRveVCk3Mvo23J6gv6MfleJnLiZloSvlzAsVftdcyoB_3A6sFKB2VeTbWtD0MfjAmYm2LWDdQgfioDb680bWKQ6aU6ZR1ngJcVJ4lmKNmWSaXMvZY1K3re4nPHKgqOgovjH1aXTjJcNmur-NFbMfscDj4wIOmu90SdfynxcNDe31IDRdpL99Z8sGBPz8IazonUtqkILlAgg6U8zSAFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=dKqmeggRgt2mjPJ2GPiTYTMPXPWtQnmkjQuCEYHjGmJAfrY2SPYrUov0pKqC2ztbiWGpG8vekhTUghj0A4OZISTZGDzqh6dg2Z40kVLMLhb4jQH2Se3uLnc-Dfkb09W8Xq8xRveVCk3Mvo23J6gv6MfleJnLiZloSvlzAsVftdcyoB_3A6sFKB2VeTbWtD0MfjAmYm2LWDdQgfioDb680bWKQ6aU6ZR1ngJcVJ4lmKNmWSaXMvZY1K3re4nPHKgqOgovjH1aXTjJcNmur-NFbMfscDj4wIOmu90SdfynxcNDe31IDRdpL99Z8sGBPz8IazonUtqkILlAgg6U8zSAFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فوری
؛بااعلام‌دولت؛
سه‌شنبه ۱۶ تیر ماه استان تهران تعطیله. همون چیزی که قلعه نویی گفت اتفاق افتاد و یک هفته تعطیل شد. شنبه و یکشنبه و‌ سه شنبه تهران. دوشنبه کل کشور. پنجشنبه مشهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24731" target="_blank">📅 09:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24730">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyxUi_CnihVje2nQNWa9etDQ--f9lOPYYJTBUBdkwe1H8GXF18zVNzlK1X9WZWyBHjEaBleefOVxQjoSA_Pb7T_SEnQwN2limUskFcPSPJzOxJ5h7-z31OJByTs6J-aMM1o2-6qQa0mrDzqd1EpQ6JkAb9_1ZPav0hX0pw7Z2JNzev82DDYNIjQQ9BkJgczEJa3CuASL1jNzNJzup-pxfm6qNu_2wsHueXO54Ac53KznigLWPuyLN3IIJj7ViHYyl4cwkYS-n5C3QXY0ypfX7BjIZJ7OWZPzvpFggBQN6TmmGAcgz1_uEVTohBRuGUqFAA7aRALtj36f29dvxxcAwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ فرانسهِ دشان حریف پاراگوئه در یک هشتم نهایی جام شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24730" target="_blank">📅 09:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24729">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCEllxQzRNmDQVBkWVFntfL6Bw0FzKY2hmldfGM4mAjalxN9MusGytUteR-2I6_UdgtcW-HQrlPr_fEHCEu-xMPC8bbKgnkPzOts52SDwjt_P-DykeD7qhfIXIk5dOYQTKxxvjowY29PfnTZZeoNfmPzqx8XSePA0u1a1hqq9ty2PYafIH_4WS7CGYLl9wmw3Gj33TGUyfjrw-ng42p0u0j7PLTiLiiPawKHjF0ktnTFBF_cO1S9wge2xgKf0dtFDNsDx4MW1L5ggJkg9mvu3-f9DYY2D1ez6sYtwHir20dSFFeoiIs6BHeQB674qIXiyaISvIhG9xL5dHrnSTXzEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ اوسمار ویرا برای عقد قرارداد سه ساله با باشگاه تراکتور خواستار مبلغ 5.5 میلیون‌دلار برای‌ خودش و اعضای کادر فنی اش شده. درصورتیکه مدیریت باشگاه تراکتور با این درخواست موافقت کنند اوسمار راهی تبریز میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24729" target="_blank">📅 09:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24728">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZZeCi71H89dW0A9itdMYeWJvvzPy1oggwF-icsaeJKlecTQNjSWoCJT8Rm8pp32teiaE5spLH5K_uTbozBNrTon_FHvRUTbAmqOvk5KEd_Pka116l99K-pbyvk2g6cvhBbEI5l6wxyTycUM-MmIjmPCJueA3k4imGLzjUQeE79NH8F6EQvlkD3qCh51w2qLmvKM2AO2LJ0OqrTFETqqteMoghlS3XaXu-3cQAWh9dpZp4ywp-Z4llJAM17YirUk0c9SE9_2I2t9ZKWjB2TO8FCq1qfFMc05s9O3_Tm2LHAjvnxAhnHTTcphi80MjRIVjqeUy92CuBJ6cqSJsx1_cQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24728" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24727">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCxwwW59e24d9xsCQ1btf55yi0Gf5Ud2pGu2EJljUUxoH9oTo78KYtZgfhVZ3IDlk9ft-GtBiQtAqvCH5wsqAw_8B54cWbROrwOVgplpBmpkV28NNYIUyCGwxYfvQYg8tXpNh79CRGlx3gBZvlHDbWKSZmFfa3l2mHeFrhz_qMYdbj7y-Mg07fRDJVl7gGRZDtE-KPWHRnA7Srl9H0WtSxj9Pk9mo2a7UBHRaRMIjLIEcqOMyNcV8tRaCWTOYI3QvbyH8dK2fsA8HVL2oaHL3u4ZLW6VEnJSEdBYqz0inceoiySERsY8R3z0cbzc-06RQK6NQSi89wydr1RnDP7L6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24727" target="_blank">📅 02:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24726">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛ از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24726" target="_blank">📅 02:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24723">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=l0V4Y2UWe9Niudy8_EyIHTdxWp9_olw_JpbgGAJp3XnB5AKRY-l-lQlkjBha8RzskFEUJhYfL76d2_ggbC5RXgi3UXyze8BB61k2DZTI0o9TMWYAvvYu4jJVGZcOgac5Ql1pPHJ5TlFlvVq4wUoAd1c_XnDrX-SJp27dsWdWy-yXoEF4jVDHkKJLJHvSsR2QaLrfOMDpqi-98ahipQaAFrBC8jH_YxxwrqXFqO03J7HDb12hm9dwcj2EBP-Usv_sHP771fvOuWMSXbOjVDd-sy4gIoxAg8BYCJvMUOSl69Fi7me7DMa_UNp4-XiM1kq-oYTECTqH1749aLVip0NDgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=l0V4Y2UWe9Niudy8_EyIHTdxWp9_olw_JpbgGAJp3XnB5AKRY-l-lQlkjBha8RzskFEUJhYfL76d2_ggbC5RXgi3UXyze8BB61k2DZTI0o9TMWYAvvYu4jJVGZcOgac5Ql1pPHJ5TlFlvVq4wUoAd1c_XnDrX-SJp27dsWdWy-yXoEF4jVDHkKJLJHvSsR2QaLrfOMDpqi-98ahipQaAFrBC8jH_YxxwrqXFqO03J7HDb12hm9dwcj2EBP-Usv_sHP771fvOuWMSXbOjVDd-sy4gIoxAg8BYCJvMUOSl69Fi7me7DMa_UNp4-XiM1kq-oYTECTqH1749aLVip0NDgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇵
اشتباه مرگ‌بار و فاجعه‌بازیکنان‌تیم ژاپن در بازی شب‌گذشته‌مقابل برزیل که باعث حذف این تیم شایسته از جام جهانی شد؛ با گزارش عادل ببینید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24723" target="_blank">📅 02:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24722">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8i_txbnpOPTzVjjMo8jKC59FRaMWLrcrjROqmDUKT9-LMErJKMHJ4c9ntjqQXvPc9-4EDdD6hUlxqKFb8W4RqW4XQbjC7NeBzQ71rqPmo_6zmh8G5uE0gsvm6m1WcTJaVszC9tA8W9Ct4es0YjTqEwA-90b59Aqr9rTrd_mQu8KWi2IpcTk_gH-wPynVC5c4RB4gQKE95ME6ZwbYvgRcPK30SKKLNu-j688zjZcUUrhlWmm9ZpT6vbpvDEqvfroW8juFtu4tr1WEn8NMs33xktovQH4_9Qy0l_Jj6H8Mw4NAfhH2WV2zkOpLsWQvVhDc7mMRnpxNCuVeP3Hr-ugtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعداز آسانی؛ منیر الحدادی نیز چراغ سبز نشون داد: تاابتدای هفته‌آینده با خانواده‌ام به تهران برمیگردیم. بااستقلال قرارداد دارم و به آن متعهدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24722" target="_blank">📅 01:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24721">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=bQavtn_-CbyeaVWrc1YmBirooYidvRaSxgZxDkEpd2MQV7H-T27u8Juumn8JNk-wA9eZcCAJsS9RCtDlyX-9dcl-OWtCaTZ15EuRAYNMC3MD0qY4548aMnPBYGXGO3fm0le-jnfLyMBDd_2wn06Shvbc7vVPlZE_dDaA18XT1aWUBb4pUQVN5n7zUQkIga_cdeDG-GaEqZatGujpY_TIWONyREVhS-dheZz8EtQ0hE0Iu3vX59YgWUDbZ0Mhxml2lUZ5nkbA6McKJjJaxrUqg__0-hEVt90CKW_55Lg4IZGSkWzSWVqYrYgHOX3wWe-vduvQERW00F31qkZTvAfQVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=bQavtn_-CbyeaVWrc1YmBirooYidvRaSxgZxDkEpd2MQV7H-T27u8Juumn8JNk-wA9eZcCAJsS9RCtDlyX-9dcl-OWtCaTZ15EuRAYNMC3MD0qY4548aMnPBYGXGO3fm0le-jnfLyMBDd_2wn06Shvbc7vVPlZE_dDaA18XT1aWUBb4pUQVN5n7zUQkIga_cdeDG-GaEqZatGujpY_TIWONyREVhS-dheZz8EtQ0hE0Iu3vX59YgWUDbZ0Mhxml2lUZ5nkbA6McKJjJaxrUqg__0-hEVt90CKW_55Lg4IZGSkWzSWVqYrYgHOX3wWe-vduvQERW00F31qkZTvAfQVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستان عجیب ازدواج و جدایی محسن مسلمان ستاره سال‌های نچندان‌دور باشگاه پرسپولیس: دو تا خونه و ۱۱۴سکه‌به‌نیت ۱۱۴ معصوم توهمون سال ۹۶ دادم رفت! دیگه هیجوقت سمت زن گرفتن نمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24721" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24720">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgO1ZNvsxBXT4rEltpNYHh1_RHJdISPXPgMaoEKks8U2y47vQnCL8GOH76KWBfyWIrY4XQdBWbb8sKB6Os6LlMW0j-doC4Dddof_PPDQV1_Y-rGWv_DIj_nOmMOH-wwGCHXpNZwWu81VNquX29yhABPq77XsneGPZEhFSdzrdzoXaMNTKa9MjqloT1BcMFk_dsd1WAQIrxHQVniOLZIp-UtQopR_EsjxlYtYNGme9ZtsmSKYitusEMmOoLQMcI-X2gG-XnF8rQSs5MGcPyjeYF0uVsndC1MaFvo0qPuVQEv3ZhCbPMd20-udyDxsv-jCgNkYpUBbr2jDvOYrTXulfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نشریه بیلد: هری کین اگه با بایرن مونیخ قراردادش رو تمدید نکنه مقصد بعدی او قطعا بارسا خواهد بود اما الان هدف اصلی بارسا جذب آلوارز و هدف کین تمدید قراردادش با باواریایی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24720" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24718">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwYlizcJjxHVKnxB3loeYUBTVgzEQj6TaX3LfwokDSduys4QojwkplMCondL974dopR_24A5ds7I-eIZEITnXBjoyNil0a-1iHAsqDhvPAZIi-AaWyNK--6P8StK2OWxTMaN4brvO5_RMDBs_7Ty4wRFJE7YVClAaYsg5OJEk7Jb1EXck8X-s63MJPH0gEL8mkct7XhejgDfJiIVhdcSPIAje2s3sqqHhN3-hIng0KOUJSxKXVPDUUGUJAy0rI3kL3n6RTCZ8lNsG-Uz-kl_WobnH2ZYCjpqLDNP4lgiJ_v_RhlNOH7sQ0bxXVYcV7e36tpxAiNL-yaV4CrN-MsCQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
نشریهESPN
: علیرضا فغانی باعملکرد فوق العاده خود در رقابت های جام جهانی به اصلی ترین گزینه فیفا برای‌‌قضاوت بازی فینال جام تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24718" target="_blank">📅 01:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24717">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikpDUxfu10y_h9zX0ph7rrq37LTfdQFYFGtrfdN8SI6H7TlUj8KVMuVPvS_IiCUrUDT_bLmRB4oFNDOPE9Uutt9NPp8ZDpIvMk60X8FNNB9_iWNUHf85X1qshc88HsgrJR6ULagor4tu-u19WQwICHaJVMswgFoF4Cqco_6w9T8AF8P10iJ6Wg-KDxNYIXxHTfDfVhw0WL7_erEvyB27P48uAHRChhuP34B2cvByPIPc-K-lkG4HQ6GkOzj1O7LsCh18y9lRbUVv0NyA88qq29WslQtMm0dEFFLbNfN4ezynOlsnmFG7RmPNp9jZPUzte36BN6ctdlm79TSazA7xQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24717" target="_blank">📅 01:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbrPDVzPhG7ca51HwWQKL6keppIru0Xublm7nw6vJRCebXX3GcxXtI16Ro0UDH1tbpy4lHBk11f2lS0CZLYmRAaVOQHZYRXJsPqo2F36Sv3xvGl93aMNFnyfY8GEVz6yA_bcJrPf-E_MDGRdEOLgSHoP11R218rWWdkVoMktdQ3BtKpC7iNTIBvoHL7z0oKzqJqoVhPXAK6YkIRRkMfq0REy-BfuntT-_BZJ1fAXRPtXrmmBni7tFMhs__5kfsZaPK6MeFM50QRHuNBI3tZbRzgP-6miztvUuZfeixTQb9dGQjn2TFMDhn9H7WM5UaFR2ikh3Zpad0HYBDbmigqRrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جیانی‌اینفانتینو رئیس‌فیفا تو دوهفته گذشته 24 مسابقه رو تو جام‌‌جهانی از نزدیک نگاه کرد و بیش از 50 هزار کیلومتر رو در یک جت خصوصی گذروند.
‼️
براساس‌برآوردهای بی بی سی، تاثیر آب و هوایی سفر جت اینفانتینو در این دو هفته با انتشار سالانه گازهای گلخانه ای حدود…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24715" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24714">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlSWSmygPaTxfItPbpohgN13H6lp3zV-jLFIYky59UlFDpLyILnUNCCEmowxbcv6NBSq5R3NAqqfwgcPV0zfWuDDiEqgKPYwNYujexY4FgMbeCMSZEfXh5IMwv4XujoUapnwD7gokoSdl9zierrxBhX69FKQR9coW4NtiGaO2t7YTEua4KGegT0DPumsWBGQM3CFOMCrJUqmRyOGq-n1s7iKVKYuZQJA1DAABQLnD4SKmewxiuVaJUQF2PjwEhqEdlCpze-Tq62st_SDfjm2vqKzPdZylgXOQRu90C425jvZ6-v-O4EQWMCCKLLCxLzTHyFAstlUafkTBU5768p6ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24714" target="_blank">📅 00:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24713">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F--1q_dT83T7YjCqRiFbnlcC0qlGoy_Y8R6QZYlWDrtoUxAijE6JP9iQqRRTafVK3ZWyJKiy9P0BNzaBe4b42WJ-jbeGZoGMjx9BiMlMLkUtZh8Z7ppdG0WGbuDYLGo3XnO3pZz8aH1Yvg9zEcsLkLMmU_XrjhNgrfqdlbuJRWY1ZxlUYCxCRjuKu3C9OcLFVPrBGQ8wTEO2V7bmNQ93bw2xAUWYIeLl6y48ZbnSHafKvvtsr7gb_HFcG1i6d4jnXGd8eN9AYum9yNLIS-SsUp0zz10wNzLl88Gu93nISGsyi6ugd2R895k74KloRq5CjndY5ZeSO9pBdcUgvNXooA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24713" target="_blank">📅 00:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24712">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mr4FW8mOPEuwIPs3cULmvcdNJTiLQwePsWx42mexP5-sX7aA370Wh3djcU-CsDV5SA5TKAsvTx54XCqGXcueR4okg_me6GwpTlbYH8ztQecroy-MKXMZrnvB8ztQox1vNtJVQYhmZDuG-ZmJh0o-LHqu5xX-Bf3cQcsS-P8gPYrSkz_o8_YktUC8XK2yDRsavDlLsbFu55jOlK0A-MYtyogtiVEzwX_SrRluLmeGrv3jkRoZ-loSsepVXq6xpX6tGM2Tra5W3G9_F0FBgULVnXU0DcFXJX0WYiJPPJu_9PmLSsIk2FPKYPjEI3F_csho-cjISul12t4XuVom9yOmww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24712" target="_blank">📅 00:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24710">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoK5KEHp3uJeMYzvuRja3Aozh0FjZnD6KHLMTxsiFIO6CoBMHDaWpWiO8wMrbv6m1m4aRMye5EiRlnQdOmwXTly9n7md81dp-yrmm--I8VaRU4tfCec5j4NDl2E9_kWGeHSAm0i_IBZBsacFdjJdAqNfyX5kE4GilPyygyH4K0HL0c1GFUqtujMPiGXg0OrSoFi2YQPTEHs2bdOVhMAijsRXbO4h-WDBEWVmw0Se6AnKtWQhW4pRVIXeVPn--JnK1WrxvNTtA-nqySGfZMl2V0PedHWglmEfNDvwkkOpxVAXhE47gWXaRVmri77jxhdiVF3VwJW5VE9Zm88gr6TXaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛
از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24710" target="_blank">📅 23:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24709">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXgf3i3zmmgP49DIft4_0iufCbRQnW8EVCXM_pmmTPJmtwq8IsI5Hdl2a4QM53VFtVWqwgybgidWjq5OHk2zNsQPdCdo_EGOO2apGJ6G1pr-uWPHX0cIeW2gBMkjcVOb5dvS3Up5MeoU0zfLXKkaP0dQ4CqEfWQNaJQzNp_TmFrso9xU1gWK6RXNstM0Vj6F-10KilegD2v6vjcePLkYiqQe1YEx65OuPYyM2ejhk_6EMmyX2wYfumh9TRStGA7m-nSQv5zMCAlMs_BjVPoykPASk_mv6qIGGRfhYKXY_xvWziBynfrJMKF2RfdzeLjTh_guGKtR8IrTC9IG4ZzDDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
از وداع زودهنگام هلند و آلمان با جام‌جهانی تا برتری بزرگ نروژ با گلزنی هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24709" target="_blank">📅 23:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24708">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUtv3gZYtuUIvI_X8lJUIt_wGcAtRcEVaJCZULH8RtSzDwZFFmg3WM9E1PTQzxt04GzbdiC03xWwinHOoArWdUcMTWvTC85vs5T1WTMMPY1nhT7iAod-jQiIXcURRRGQfFoB3P67RDSQQ6V9uocQYt2si-32lZFsjksGZ5G9cVNvIVB-SnEcAhaLSBEj2chhRhpALlbkMqXwztoYTVp0AXxuUybukRnPQNVnt7mV28f4FL3uzi7Jl5oXP12WjS12ezMnpyn2_5GToAMEmbJEKt9QXCSPuviP18zPU_u2M-Aqyl5w5uJ-625LS8lBpH4xhIDQ2oG7Mrm6m1_u1PckxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
مقایسه جذاب عملکرد بردلی بارکولا و لامین یامال دوستاره‌پاریسن‌ژرمن
🆚
بارسلونا در کل دوران حرفه‌ایشون؛ بارکولا بسیار علاقمنده که بعد از رقابت های جام جهانی از PSG جدا و راهی بارسا بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24708" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24707">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGSUm0AoZwfy52CVroI_RKa_3f0jVN5sfGMzEYLCcg-xpLZI4As2-gp4PGAIyYLr9Hu3QZYKCx11pyqW8hPP_DibOA90BfL8c90oAjg5zc8q4lTUOwULqBCoM88fd4_Ct0Ap-6Xc4FUfXY3RdHUr6ZpKUTL4hjRCpXz0BH3glnlt3isp1goBJrIyrTJQzkNHTfwCCm0C4-jED1oX7Rzb1Cp71Hm5XRg77sICDnRnVRlkoK24XE2jnCrtyo2M5WuL5Z7opQeUKCphwNRCvZakrbE_0hwh60ysTcZKgP3wz5q4DcE28OGWXaBB3prOMBi9DcH3IEgUk6ERTog72_IBfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نروژ باگل دقیقه 86 هالند ساحل‌عاج‌رو شکست داد و حریف برزیل در یک هشتم جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24707" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24703">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VqVLvEJTTyPYNRpaUU4VD6scMhUHEuFqcDDPVLMJPWGNLRna3657USsJ9_b_Nd8UN6NdwdtiRm7UxiVlkD-kkwE7wNBOq6soByn7Z3qGs3vlz_s1V1yMIdu2ZX_uUfkT5ZsYwTwYRwyMEwSRK21IGAtbHY3Ls_yOTz4bk0t6NKCpl9JtU5DjVVo3lepvIMk77GYSint4tIfPS2m7mu2Rbzyhl4a8NyVTHOw3ZiwQp8PKS-dYG4cVCzm8yGrRh8i-1t8ZxxeMEe_PhHurGQE3fvxhevPmq9OaCbn3S30LLVuHX_Vv6uXHRiZtzpT8hxPl_WI2FK1caCpvn63BjG5n5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pwpZ3ba8UBgFK5UB22aNhDQRhjnz1hSNX6ujpaQY4ORpgTBVyv_iy-ANEnk0uLA8s_LecZY9jfvbFtrHy3MWgbNCZP-mC99dEVaKerQ63k9lIPPGSaVZvVEu65g4EA1Mk2rvuM5ujg246P4Fywjuv1kzUTiLcUhZ4WBQ-OoWX-BrXl5-6vxreRWRZN8HpffeClH-NGFsx9fVWOuYdRxQcRaexs0nb9FhZU595k1TtoKivEf4pYZCNOMq9wD-e0MLiIzeGjiMJiLcQiZSHGdZpUkqud5NrM7yFwDbIGLUH_G6g1nJ6gYMtvAACDOk3MoDpJHx48ORWj880nVH_EJaJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدی
د
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24703" target="_blank">📅 23:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24702">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jM1Vs4opctxNrs4TtQmeFBTpa6kV0w_XB-xt4aEvT7cAuAZ3KwKWzZ7BahaNk9GTEjw_YYhO5OAJDvIhgi9R-1xW5d4wDKSWWKSUDj9LGppPVf9bDSmmK7rMgaUViS68BfC66cMltivjD6dJl8Kz3TniE782u6NCGV_5UXVLwKCwPkIyLEtBU4YYtV56rdNM6j5uwbjpyOzRGwDqoE6YzTrlZqQIZXYXPwyHVN0ZQzHe0QHvCzwOKEJwGo4hDblfGV-cMIClTVscfqwkj7iXsmRCvFknoG5P_FtLZtOmsRVSkRhYjMp4GP_kq6Q4U7lrwVJ1dUTjpVcUDlSKfCrE4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24702" target="_blank">📅 22:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24701">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VU2YoFSbsSZMF7t4uxHAnf-fOR-2zacsokqk8nIOuLaCSbsYXcFckMXGBN20tnjaljs9exfz772o7V_bwQbDU1_55KfERJAn8KKnOzFWOTtvPLjn5qniJgXhTZhdG6aYJi3YQ1jx6X7Q_Hkk9Ue_WiKHpDkgUp-yC-a5biwgts1EojRuVGYLfUpv28qVlHyg7VOEvZYntbWluzariz2V7yCk2a2KtS_xg6bIg_eK4fsuyF2rsN-GHnADfMJSI5qsjti-DZn7nQSBMNVgBVAKkndB14XTvdnVnDwOzzP09b44ae3Iw-KAy2KodzKi8J4URlB40NqD1zm_QNd8znMl4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/24701" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24700">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLskZzpZdsHm16oZF8GTiLxKPW3GbI7PfP7wS9RHNpV6Ukivx1Ma_bOpE5ktTkIAQcV3E3y67X12ia61Px2uJvnI2TGD3HFRbvrW9bGjFRIS8dLLxgnhhLIxfMXq-O7u4ZcSz0KPXL5zlb84eHMkLIAvz5xQKIKrvA5zfuE3jJJdT0JHTAgm1vR2gZfsrQSDJNmWjJH9wgLOlGfaH1_Pfh5M302ZMDvHwiguJlU4CQ23OiUoH_AhpqHXX3iwOMCngX8CG_kelD-Vsm2gc-fjD9Zsrv9r1MRn62_rkGhuLsXw3Y2wt2LcvDOGXj2iG4sLSIwPkfviE_JJEuKPSAGTtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇴
سوپرگل‌دیدنی نروژی‌ها در بازی امشب مقابل ساحل عاج در یک شانردهم نهایی؛ چه کاتی برداشت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24700" target="_blank">📅 22:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24699">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxkVEB8AnT1EFBVN9ra45YfLUI0jNaStIgCQ8LoVAcxA5en4bVuZpXWeWCxn7tKH6KoqZsPr4qNk1_PRaZbRnNdHmX06z4hX1_UtpA91BDEApqGoxJXyX4d38oUqsVk7oWOcAVz7LcGxR5nOY_-hM_aHOWAcLXDpamMLvoQgQgBgftkvFzrKm3fbN0TnmV43-A2hl6mz5OBz1S_dU5aDMhMxJnG66h4G3VRU1BMOTduZwLv05TMYrX95TQOiztaSfiwVPkMNqRc_NAbiaMp4JuN7dO2k6Q5KjUZGuGI5rIpxB7l9m88tlpBvFFw0wXkpksFeMPRFI-mV7evuIBLWng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/24699" target="_blank">📅 22:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24698">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_pgu6dhL5iU-sDG4dY4xF5FYSusxb6SMPk5MB3dKARFpSBudnR_-d1PcIV8xNdMiehPyAZw-t-JbOEqOLEFePgCgZj4aTqpQcc0TrVLU6kIQU-KVlttvHdMDrDuP0ti4ILFeZZ3F82A4i5t45dVe9AgScYi0U813H7K-R7fnoMeZGtI5hydpyHUFDQbLp89QrRxn_7rsBbI63g8rvXDNLk2rwIaVJNaXfR6A9kmd-DU0bSz3KpyNaLowv02Qz1CTAqpBTRmFU56XTxRUixvW6FhIk08LJA2i4rFdMFZDn7t2GBpihdFiUt4nm8aBXzfqMPNJAWm4gWE9qAV6x0efA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی در ویژه برنامه امشب جام جهانی اعلام کرد بنا به دلایلی پیوستنش به تیم پرسپولیس منتفی شده و فصل بعد نیز در تراکتور خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/24698" target="_blank">📅 22:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24697">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=hvXQM-nEK7W3LlC3_fV5_64CRHosZCImYiu8qPFxF-VR6SVbseA5blvD_KmbqLvUNIAVaLzsGWoWSBDWgxYHpRUn15eXJgwF0xLq5QaZmaDIj0v5BayngIH_mAi6q3w3YtDmn70NaQv0JIewiacnKMP8tnXxTqD7lmnu2Uv0kx0J6oFHn-SifbUTYZ_iq3aJc3eT904na4th9nhGXbjhkJ2a18s2dl2jz-RZ7azrU5HG--Irz2gNfr56DheWUzqwMrzFcsEIvls-cPLfwMX4PA9sARecoA1mG8Ar56cShFlb4g7UZ0cVz_-K9KXLaAbzHpk1KWhrKbXSq41nQXtWPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=hvXQM-nEK7W3LlC3_fV5_64CRHosZCImYiu8qPFxF-VR6SVbseA5blvD_KmbqLvUNIAVaLzsGWoWSBDWgxYHpRUn15eXJgwF0xLq5QaZmaDIj0v5BayngIH_mAi6q3w3YtDmn70NaQv0JIewiacnKMP8tnXxTqD7lmnu2Uv0kx0J6oFHn-SifbUTYZ_iq3aJc3eT904na4th9nhGXbjhkJ2a18s2dl2jz-RZ7azrU5HG--Irz2gNfr56DheWUzqwMrzFcsEIvls-cPLfwMX4PA9sARecoA1mG8Ar56cShFlb4g7UZ0cVz_-K9KXLaAbzHpk1KWhrKbXSq41nQXtWPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اون‌بازیکن‌تیم‌ملی‌هائیتی‌که‌کارش‌هندونه کاشتن و فروختنه، وقتی میفهمه من رو کلین شیت مراکش بت زدم: این چه سوپرگل برگ ریزونی بود که زدن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/24697" target="_blank">📅 21:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24696">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UD8oiMb4-Rwvz6pimo3f-DTzZZS1uLwG4gUU900q3po2ji-WswG45GcLy8Cvp8FFhsiPtH8emjgMpR_HCyPAnVSfMzMgndDr-xi3hSmbWFpRFywp_Cl-FQhA0lZQzdaevhvrbt5y4sQVFKHp8TrfoDByqpmnpmdMAP9INsrYl7VV6BvT2_Vw-1lLKtAV_kPP0KdhefJURWdjpG-XHv8cQWkH1Oq0Zx2ifoZkJOV_BSsU7kgXNM81Y52vinq_g9vABwP-M_n6UwpE3SPcA7uWE7QMZcqWammmMuf9wdhaOuMXLbdR1Kt8YMq0j6yqoDuB3amgmuX4zIVozJSE3pRp1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=D5js5q0FzO4H_KS0jDKKqwe-Qsynj3-bM-WV_GfnXWTxmjSvoZMsb7TQfgfY-vKn0MOurda9bbetPods3DWVV_jNm9rq-5UT8ffUx_ykfFcL-hFa813gzNxL-0ltqSMSdNaVYpXn0s5rU5woaJBHNcCbJsyX_qoV-cMVAE0PHdRGQaBuy1QwvCgjrTXlEDeRVWOlPM7s1Gz9XGM4mybjxs_azIAlyNDUKZLzLrth721-9vIBhMNPygE0Ns1GsZ10Dy59KqZV8KNOrZifsshHPCYMiDJXokRIgCdWfsHCQMCVY5V8Gcg-3_qaoPQwWotvIcA2pQvKp_yT9MfcG6QkJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=D5js5q0FzO4H_KS0jDKKqwe-Qsynj3-bM-WV_GfnXWTxmjSvoZMsb7TQfgfY-vKn0MOurda9bbetPods3DWVV_jNm9rq-5UT8ffUx_ykfFcL-hFa813gzNxL-0ltqSMSdNaVYpXn0s5rU5woaJBHNcCbJsyX_qoV-cMVAE0PHdRGQaBuy1QwvCgjrTXlEDeRVWOlPM7s1Gz9XGM4mybjxs_azIAlyNDUKZLzLrth721-9vIBhMNPygE0Ns1GsZ10Dy59KqZV8KNOrZifsshHPCYMiDJXokRIgCdWfsHCQMCVY5V8Gcg-3_qaoPQwWotvIcA2pQvKp_yT9MfcG6QkJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛ از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/24695" target="_blank">📅 21:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24694">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=PMH4VIanJ4Z3bgTBqRg-4j4L7Dp8sHo2zIx9c6w7vWz2sYu_TukOprlrFEB_2eJUqY36j56ER0Q_21pGs-bM2drfI5e-wap1bvOsKq9BSiWn_5vnDs-17lOhlICQlcaJKGRno9yYHpJBr8MJ4e9Rldun4hIcNDutSW1NgpqZ-Adi1vPdwpR54XArlXrcPBTOSp845MVpypAcus3SUjLXvYF14mEUjAv3QuSY4hk-GQWDgenJE8IBwTZy_NlcpOHq4bR-RdCKO_rAXhcAZWFMMeppVIAUQH9_myj_xRfV72bp0XWs1DTh8jzRW2GefEQD603rKIIN2u3RCxbAnDz35A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=PMH4VIanJ4Z3bgTBqRg-4j4L7Dp8sHo2zIx9c6w7vWz2sYu_TukOprlrFEB_2eJUqY36j56ER0Q_21pGs-bM2drfI5e-wap1bvOsKq9BSiWn_5vnDs-17lOhlICQlcaJKGRno9yYHpJBr8MJ4e9Rldun4hIcNDutSW1NgpqZ-Adi1vPdwpR54XArlXrcPBTOSp845MVpypAcus3SUjLXvYF14mEUjAv3QuSY4hk-GQWDgenJE8IBwTZy_NlcpOHq4bR-RdCKO_rAXhcAZWFMMeppVIAUQH9_myj_xRfV72bp0XWs1DTh8jzRW2GefEQD603rKIIN2u3RCxbAnDz35A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/24694" target="_blank">📅 20:58 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
