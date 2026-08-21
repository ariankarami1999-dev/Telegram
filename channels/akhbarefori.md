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
<img src="https://cdn4.telesco.pe/file/ifTA3EiV27UZq8zQLvkvwN_B6JfnNmcpm9BqRhbCQk263Kg817kKbsaVE_zuGZxLTxPz5W9e9xQVG9xNn3_bYYk_kItSCjYsuYcMdEc0g2Q5n6jS78zjsLW0Fv7IXaaXCEXcrYre5qyWPrGcWxQkYJQ5Qjoi8xAJs_Ony4DE_CPiNtmq0pb6RR9j1ceQxG-5m5-CS1KHcUt-MDWIHQ7pOsfWgHyM7nEWl3UwmYV290nQuREmorGJTUxMT2sIGbDHIPzZKooqRvVw-s6XCOBnhUm5brmVZtc7ZoOXr7QSd3Wk8W4BOEJ8wQH6ZKPTjDj33hvEih3Q_DvRagMA_ll5fw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.12M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 00:16:19</div>
<hr>

<div class="tg-post" id="msg-683202">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcB_90slyn734zRDCEsP-5UBnrt7cdZJIof_UiMZORoO42t2AFTTU7ce_Lm3HDpIwm0axbxeoxr9ee4vKotyMIPNgwIsBkAxYvD3GnAw6v0FAKfBQIuBBz5M7guGMtvKZQVlfeDuLgmgnoStU64R3k43iUNLFLLenFtHKsQa8s8EoqnHOuxrU1rDmbTVamzoMFPDBZ9i9F2ijXc3Jfz_0AIBp8w237Ls_lB-qmg-ZF328Ig3vyukAtV6mKei1dIYX0caDUrWL99lJUKr2YeSU7ZYVZXSWTi-6rx43sEKxXc9Z12oISbna9nBL7bSLzMOgYLNjcUm5QaiVGfGEN1rAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/683202" target="_blank">📅 00:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683201">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
ترس ناتو از حمله ایران به بلغارستان
👇
khabarfoori.com/fa/tiny/news-3239213
🔹
ماجرای جمع آوری کمک مالی برای پسر و عروس معصومه ابتکار برای ماندن در آمریکا چیست؟
👇
khabarfoori.com/fa/tiny/news-3239408
🔹
کار به پیک پیاده در ایران رسید / درآمد ۲۲ میلیونی بدون موتور و بنزین!
👇
khabarfoori.com/fa/tiny/news-3239303
🔹
حرف‌های جنجالی شاکی پژمان جمشیدی در حضور ترانه علیدوستی
👇
khabarfoori.com/fa/tiny/news-3239280
🔹
اظهارنظر جالب یک روحانی: در هیچ روایتی نیامده که صدای داریوش حرام است
👇
khabarfoori.com/fa/tiny/news-3239216
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/akhbarefori/683201" target="_blank">📅 23:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683200">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d311a6232.mp4?token=vYtSI6mJXnuFvtr38SMLXql0ZQ-FGhGr1Xq_L-hIsrXSi3qc7N-VgeEAh5SUmQlLX1xtNoMEYDNyGgTXihaBdEOZOqdNyil9y0i8Se-P-W0agBKmY5l_pD_jFmn0DkgNbT_TJlQpR6KX7V7c4XC-9dz8DCJF0nZjNcQeB2FXMtMV7SAxFgrUaLpSFVcjb4rej7iRGC69TkqhiCVerP6vBD46WMgsZx-acgNrAsi7O05v-SNPyJBXl4k2jf9Yh0MjLFyniglNjclvAkefSCpkdqiG3u6nFNF6DShpQIhApVxGMPZOzSbFjq22APDIl_rYHmOTFb6x1cg3sV5dyI2qbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d311a6232.mp4?token=vYtSI6mJXnuFvtr38SMLXql0ZQ-FGhGr1Xq_L-hIsrXSi3qc7N-VgeEAh5SUmQlLX1xtNoMEYDNyGgTXihaBdEOZOqdNyil9y0i8Se-P-W0agBKmY5l_pD_jFmn0DkgNbT_TJlQpR6KX7V7c4XC-9dz8DCJF0nZjNcQeB2FXMtMV7SAxFgrUaLpSFVcjb4rej7iRGC69TkqhiCVerP6vBD46WMgsZx-acgNrAsi7O05v-SNPyJBXl4k2jf9Yh0MjLFyniglNjclvAkefSCpkdqiG3u6nFNF6DShpQIhApVxGMPZOzSbFjq22APDIl_rYHmOTFb6x1cg3sV5dyI2qbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض مادران آمریکایی به کوتاهی لباس دختران؛ ترند تازه پوشش کودکان در آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/akhbarefori/683200" target="_blank">📅 23:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683199">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpMbngukxT8JBuEN39xhBRrkljzv8g8Km-ISDcKg2dURYFBGe-Y2YI0gcwBkerWvt0nqqzxofrbBNHSakpOJ2vv1u46BubV1wdMdUJbqGXWSbcmIjN8nFep8bztbqNgBAvGwIJot0lAMwXz_GBflsurdN70lBXSElUqsAN8D8ZjEbaDP2Ists-MzhDbK7soet6wueq2fmI1DPhDMsobDlQhmHYmOeVBiwiMvx0Jo75Idj4EfJUDNARvplCik6mK67Js38GDlmmCw2CBOr74LWNu6O1JqsbyNHvsBhpqwwdNUgucB-bDZKwfYs6Xk_Vb-9J-nWFbwxl0WtAyftQdwLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینستاگرام، صفحهٔ «رواق دارالذکر» مزار نورانی رهبر شهید انقلاب را مسدود کرد
🔹
صفحه اینستاگرام «رواق دارالذکر» که به پوشش حال و هوای مزار نورانی رهبر شهید انقلاب و شهدای خانواده ایشان در رواق دارالذکر حرم مطهر رضوی می‌پرداخت، ساعتی پیش از سوی این پلتفرم، از دسترس خارج شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/683199" target="_blank">📅 23:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683198">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
پزشکیان: راهکار مؤثر، ایجاد ساختار مردمی است نه صرفاً ساختار دولتی
رییس‌جمهور:
🔹
در حوزه بهداشت باید آموزش‌ها را از مراکز درمانی و مدارس آغاز کنیم؛ آموزش به زنان و کودکان می‌تواند در این مسیر مؤثر باشد.
🔹
این آموزش‌ها نباید فقط گفتاری باشد، بلکه باید به شکل رفتاری و تیمی ارائه شود. باید به جای دعوا و تقابل، فرهنگ همکاری و هم‌افزایی را در جامعه تقویت کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/683198" target="_blank">📅 23:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683197">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
پزشکیان: وقتی دانشگاه بودم بحث‌ها بر سر اندیشه و راه نجات کشور بود، نه دعوای جناحی
پزشکیان:
🔹
وقتی در دانشگاه بودم، اصلاً بحث چپ و راست، مذهبی و غیرمذهبی مطرح نبود؛ بحث این بود که کدام اندیشه و ایدئولوژی می‌تواند کشور را نجات دهد.
🔹
چالش‌ها بیشتر در حوزه فکر و اندیشه بود، نه اختلافات سطحی و جناحی. شرم‌آور است که انسان برای رسیدن به جایگاه یا شغلی، دیگران را زیر پای خود له کند.
🔹
در مقابل، گروهی با علم، اعتقاد و تلاش خود، برای فراهم کردن آسایش و خدمت به دیگران تلاش می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/683197" target="_blank">📅 23:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683191">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NaYle84aFLteA2usjQViIWnJUtCFWmdP9yLve0W4Yufp7BqTVmAQmkJ0sdKuTUZxzbVvlOtiBHRd1MB1oe2f4Sl4aSAibEmQiAxLiU9PgeeVCFpuqtJAK4cI6GcG5i_q6YPlMPJOOI0xhbBsOOihyqkW40QVMSu4mQ_fQHW0G5ZWeHTXjJnpy7ALdWTC4lwGUoeuD7K1KnQZS1sM6JnEk34pRRpg-P1mYVXNAxS_i0zlDhx8en1CO1aBMtY5DAptdX5CKgQbz4Y7UueQAzuNzlsj1PdhSn3d5cRVQNVYd_P6Lvw91GGCCVl-9pwg1P7VgxyqIY9Y5DPT9z5CRnf42g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qh3xQ99GbxYYxTjKzNLgitFWmCpuAXq8cTrZm3SA4xeSof5X-ij9DaA6vQSXE6LgcAX_ZkkeYNMyfALjMWd9S5iiLdEQ26nsJOcYCglvfqF0GaTmAy9iVUozM2_R3vKGI4PUDu4rc48uyKfiIl2khx541ze5JMicARq7CEY90y-xSy2j5o5ikNEnY2AcuyuFd3qabuJcRbelrm41175tReIuBa6UzprzdH0Z8KgbKjYBUXluJPiTt1oRKVy2j6tmbnc7b-d8JjcbLzLxGuOsF7-NavnZHRmyWQxPnqHkeZhyCrXrXkhRdidkm7h1Cd6EUfTviRbMX0l8Zc-LwwI4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XXkpEzat18cLGLGX_Hb8RsqJqKB89v4PQyP7LOyPanj9zlZs3GCuSrTPLLX-XZQW3wgFCnIpjaaH-y_4UD5i3rlNTuwErjtR7ALGYiAXpGF10X1mSoqcd7lyZSxK0nC-_GWJku-7AbMh2eM1gVSq1aYgHBZRfqnJ-v7P_qim_VaoaEO4FMb2MhwPVwxGuTCLaDDNb8de3GnVDqZLOGiicG7zGepscUrcTnTgYqjjSLVY-GAnYgbpB-qDkjz0aAy-9UZ-_UszjebBmZ3_j--UgE9it98OjmrIGTt_KdE6wm8pfNCEGGJDxvMbLp8ntwM00ZyoAw3alaKGJBMkLrU7Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAkhmw8tcpfpgCqvHH6PrqNpfnGTAyOTD6Mi4c4wvNCaHTf3Vh6Uy3mpBC9lAUQfFk3KsafpLz8K0ozs8_-CHTETNqlsjliFqxZA6rNCEQ6sBhE7aJKR0asuHQhL6vu_Dm1NKbcP4S7sQf8_wUJGtdYlQBFArbG7Bb9h-aCWbFUXcMEHOTKfXsQTvTsjxSkHxAJYQ7o-8Q4_5idBuELmddZNqHinW2M4AVhkWx9nFP1IOOffw6i9nyEF9llju09nYC58tsmVVL4_t_KbBPm_AwQ87B3FWSx_e7b_RPWXrWPHI11iOsXIFEzFF104tUmsw-GctlgOWcMETrgkEA76fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T749nsDttiBYV15VIz1HCXfSuLrT60onVQbOLeLCpL1kPoUyy-PUkiuOkG6DPFF8gNGxuAp3-6A2lfWGojO5NTkvIGYoeTyCLqi7i5oKr010AgI52FmP4ERKc7HHtmLogfzOFj__1wNV31uj_IaLTD6oCMPKNJdHON9p6Ycwr4exqmpjM09tPPM0eJNAFtqY5uKfAWT2JOzfGBYgj1Na2T3X3-TT2r_yw6Hl5CQOGp4cfDp19T41s5RZXoLplujWK4HYBgDgbvFdeKOl0Yk7Al3VDJW46Pon6eAD9NB8JqYqbiF7L15fm7jrI731qd9TjMxw9pkYohVF_xVIZHCd_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQvPdMwTXttcM6AH5xYd2DeGLf8_0wpXYq3gx74E1ywV9ZX_MtKOBA4Vs7Rvi2oIK4iU9aOK5phA5cNJOsyoisGh5Yxuxt-lacflcOFd--deT1bHriWL2w0LIIwj4v3tySkvfNqDyj-pe8wd3oSPlYfy6K2QCdJlR1CqZr7QwfUan2iWcMItjoTLAjPX6yOSxHW0EcspQ6y-dmH0AquLz41cYsAKF51KpyDJzyz--3QgrGsuCzduUIljge4R1ivUqE6rSub0xVNOkcZhmXoWBlYAznx1ZayyeSxO6EWJGacDJ_s6BuVrBfdqBAexDNfp9f77GGn_1nt1EYZvZJZ2kQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند ترفند خانه‌داری که زندگی روزمره‌تان را راحت‌تر می‌کند
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/akhbarefori/683191" target="_blank">📅 23:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683190">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrZzWG_LhPH25DlUy9w1pXGeS7y2Nl4Gt3VPQdKl9HXBzgPtjXTBfErD4qg05-fdONM0bWKsCj1emCJLUhaPuujtFD2uOLNijM3K9oOkjwo6WgFBIFla2uI1UIT6ixjR8VUAqAXsG4MPKiWNDANC_7kzNsCiNa7EFcXujADJIwXR24nYgCKc_3zIp5k59_wUj5i-NxOLFCDzoZFfDUMux4YVLuH10-XmyP8XYFmu2XliXJokOdE0J1Fi7H23FP97Ed2g234mRDzEZ3yUtdScLwQllDkQsyQQgI3dwESTMl9Ld74MJaBCx3dHgWz55GeLMsB33b67tToQXpt6V2MJWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری متفاوت از پزشکیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/683190" target="_blank">📅 23:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683189">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر جهاد کشاورزی: دیگر قیمت‌های دستوری تعیین نخواهد شد
🔹
مقام ارشد ناتو: هرگونه راه حل درباره  بازگشایی تنگه هرمز به توافق با ایران نیاز دارد
🔹
اکونومیست: نتانیاهو برای بقای سیاسی، خطر انتفاضه تازه را می‌پذیرد
🔹
رویترز: کمبود ظرفیت پایانه‌های نفتی ونزوئلا باعث تشکیل صف طولانی نفتکش‌ها شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/683189" target="_blank">📅 23:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683188">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f36536d542.mp4?token=CIOFKi6VouQKnfrvFLanpHA1H2DGdtwnSQMnsjyKtP3hsKOrl5lD1uh-kwFDnHBXnr8o1VJxRgYDR3nlMXLzADXJ3jPvAPWxFNOqt7OxEWCvPn_yGNTELUEoterx0RSVk5sPawQsqDY8AfebWw9fUFL_-1PN48biTLGeQCzuV_vnfz4XIqS8mYoG6dkTm3YlB32EBHLANvMUhjDDA0_XeKMwnX5t44P0PDI1OawCZU-JkQGhkc1T5mOl8kggYMNDnXfwkuYoKq8CoW5tfWZfP8v51bM0TjoT6bWvNxh1W4upJoTEZSJnbWWoREM_nJJ6O5v8kmPo3PftjaAKonlYOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f36536d542.mp4?token=CIOFKi6VouQKnfrvFLanpHA1H2DGdtwnSQMnsjyKtP3hsKOrl5lD1uh-kwFDnHBXnr8o1VJxRgYDR3nlMXLzADXJ3jPvAPWxFNOqt7OxEWCvPn_yGNTELUEoterx0RSVk5sPawQsqDY8AfebWw9fUFL_-1PN48biTLGeQCzuV_vnfz4XIqS8mYoG6dkTm3YlB32EBHLANvMUhjDDA0_XeKMwnX5t44P0PDI1OawCZU-JkQGhkc1T5mOl8kggYMNDnXfwkuYoKq8CoW5tfWZfP8v51bM0TjoT6bWvNxh1W4upJoTEZSJnbWWoREM_nJJ6O5v8kmPo3PftjaAKonlYOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار طلایی‌نیک، سخنگوی وزارت دفاع: یکی از عللی که سال گذشته و امسال نمایشگاه نظامی برگزار نکردیم و رونمایی‌ها را متوقف کردیم، برای غافلگیری دشمن و برای صیانت از اطلاعات و اسرار صنایع دفاعی کشور است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/683188" target="_blank">📅 23:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683187">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRr0Do97Aow6mBrRn00ZxtQRLj8JyYiruR4VbeSsBVaJDhaRUiGPQpheuURmKMS5Ej4wwD0sCubSqp7f_vjJDvbS4YWWRINjSZzorhamxStoeVWRdhj33z-xJGeOn3k3raUDInPybIM3A1TWaxNccWMIiXA0oWGh34sniOxMNPqIkcnVDZTE6MnJDVox9weAazHnxYX2-YbbC2R57mBASTE5ifD4bvocGp4jM2iOcLLyqAGnWpT--71ZdLgTnO7ZUZsC_NJOUolyTreJTzQTxL3nJWcKF1zY5pqM2EER7hR7HGKCnJPLqxpbrMNS5Wu4UPKeB_lZDU3kj09iyX33Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه وسیع انصارالله برای تنگه باب‌المندب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/683187" target="_blank">📅 23:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683186">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70ea7675b3.mp4?token=cbcwh0rqAa1V0Sx41wMXgUQn9z0Z3THZflNrn0wHZ-j3TfeoLZy0A_63F0VisLMDsib2nrm1Lx-doPjJjTdXa_JbQQVVHLny0RvUS_nQvSoC8OasW1Len5hdWREUiBk3XZbZaLHi9McUnKLeRg9BViQGSdQSA-hMpqg0JcGpMGVlmeO2K9553ZJLWTE_jCh-XfoWBZAmaA7We6ahVClmMg5IfcyiCk9xCbyqlSrIUo_PSOUtNTAyMh3wsw8HseSlmY_NsNXUHahhMQVQwyAxwRwlF7yJXcGbhEp8HWEHsP5WNvturx-NGdeieWWCL-c_5omszMPXNcbxe0n6dS3wFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70ea7675b3.mp4?token=cbcwh0rqAa1V0Sx41wMXgUQn9z0Z3THZflNrn0wHZ-j3TfeoLZy0A_63F0VisLMDsib2nrm1Lx-doPjJjTdXa_JbQQVVHLny0RvUS_nQvSoC8OasW1Len5hdWREUiBk3XZbZaLHi9McUnKLeRg9BViQGSdQSA-hMpqg0JcGpMGVlmeO2K9553ZJLWTE_jCh-XfoWBZAmaA7We6ahVClmMg5IfcyiCk9xCbyqlSrIUo_PSOUtNTAyMh3wsw8HseSlmY_NsNXUHahhMQVQwyAxwRwlF7yJXcGbhEp8HWEHsP5WNvturx-NGdeieWWCL-c_5omszMPXNcbxe0n6dS3wFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهر ونیز چگونه ساخته شد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/683186" target="_blank">📅 23:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683185">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFM1X4KtUjz1wh2sYjMuYlcTH__oG0tattUgXjQ9eAQ05CnVFnzzo0VC-04quS9kRPGoop5cgRrwb7fDlhY8yuKoMxn0WJcIGINZUg81udIjoD-xhb1x5VNLZtvHniWDXdtD-Sz21OZjLaE7LVXoNcLYwSQwMxbfW510UaIGsZOXOwtDld7D4z6kr8A6I3UsWwvrn2afvWtzvv3plRzf4coAdbAPMysnHiAtV7SMcJceIG2i61_NV8_i4xmdrbgX2UUCDNdmCEXBMw2Iqcl6_FywyEOn2-vuDvdWvY2mSETIIjTkQa3nz0wp2ifoStKF_aj3duTPMnldnLetMUrzlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسکات بسنت وزیر خزانه‌داری آمریکا در حالی از اعمال «سخت‌ترین تحریم‌های تاریخ» علیه ایران خبر داده که تصاویر او در کنار همسر هم‌جنسش، جان فریمن که در این عکس پشت او قرار دارد، بار دیگر مورد توجه کاربران قرار گرفته است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/683185" target="_blank">📅 22:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683184">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
تهدید فدراسیون فوتبال توسط تاجرنیا با چاشنی کنایه به پرسپولیس: اگر تصمیم بگیرند جام قهرمانی را به استقلال ندهند، از طریق فیفا و AFC اقدام می‌کنیم ولی لابی سیاسی نمی‌کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/683184" target="_blank">📅 22:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683183">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UryGa-bXNJkGsbihavRz0ZLNUD10zDtScItn05hozEu7TK_WcJhZSL-sodm5CjdbgEik9m75cWCptYBDqexxq4nfX1l4uH-A52HEle2rjz873h9-VMrHslmZ3AR6qqK8jfo8KwV_typBbQ-aBOg6-6j1aSlfl1bXIcV_jGIwLqDkpQ35uasHxbsvxUr6D7jGVZlGbQaaAjVaiGtmqASJrVUWhBam60SqKAwBs6UXL8oe5l7eFU9-Cexhk3qDwY9Sc67U3v7RPe4EWm3W2ZfzAPMZvLzimtLiynBm1eWRU4jBmIvhlA5DvRk93nWRoLdjQoDm8--UJxdwkiEhAMOt9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فهرستی از با ارزش‌ترین شرکت‌های هوش‌ مصنوعی دنیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/683183" target="_blank">📅 22:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683182">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29cbf6bd8e.mp4?token=R8B_SMxsFg26fNZ3Z2yTNF_rEWpZ5mFWIS_eG6zgmJztYJXMjCbqMq7jNyW-UAd51VZyVVMMoEN1nJN7oYsy3_tP6Hvy79oNL3W-Xay96r8q7W0pApJUanFFKCbfSfSyIPyOHzELdy0F0j7ahJDAbjvN_-JoYaox8ee4PDuVUZloifiCUukcKik60iHP-ZtYVKSTvi4QH1qPwLACnwOY4Pzv7vR3Ldy_7K03QBWhcpiT_JwGAmowoIPbrESDD2p4b_Q7xa3m_9cfmSdjRBSi-deimm09pIq5Yl8JacJ2ACKa40Ja9EPuxR2i6JJ9m7p37QQe9cwHalDNj0qltfOPlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29cbf6bd8e.mp4?token=R8B_SMxsFg26fNZ3Z2yTNF_rEWpZ5mFWIS_eG6zgmJztYJXMjCbqMq7jNyW-UAd51VZyVVMMoEN1nJN7oYsy3_tP6Hvy79oNL3W-Xay96r8q7W0pApJUanFFKCbfSfSyIPyOHzELdy0F0j7ahJDAbjvN_-JoYaox8ee4PDuVUZloifiCUukcKik60iHP-ZtYVKSTvi4QH1qPwLACnwOY4Pzv7vR3Ldy_7K03QBWhcpiT_JwGAmowoIPbrESDD2p4b_Q7xa3m_9cfmSdjRBSi-deimm09pIq5Yl8JacJ2ACKa40Ja9EPuxR2i6JJ9m7p37QQe9cwHalDNj0qltfOPlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر سابق فرهنگ ترکیه: ایران برادر ماست
تامیک کمال زیبک:
🔹
ایران فقط از آب و خاک خود دفاع نمی‌کند، بلکه به باور او، در خط مقدم مبارزه برای آینده بشریت قرار گرفته است.
🔹
ایران دوست نیست، برادر ماست و شرط انسان بودن در این روزها، حمایت از ایران است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/683182" target="_blank">📅 22:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683181">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4748c9bb82.mp4?token=IOc85Ybl19m2hTXvO6UXJfuFJgDdRcRR8WIj_97678kXhp24Vvl39-rF631hRrisrbXK0WLtt43SZHcGC0gQmfoRKcxpjtlvzf-PTeAGNlh0kR1PBKpM9KfrUrONfL2fgvl9KPKGHsUNNYBFaAIH9hnsP1rCCT8g7QM0ch1mSS_Rpfzg9hO2CzbJzLA0rs4K-wnDEmQUxCzCw-BhlgsENT-tkjqJuVv0CPa9MxP3hIyZPzoplVoyqXb9ZMfPsyH25-9_0RDH_VORUvFwzKURyPt7WjrgxKStmt44-ZQovyoC47_cmdmu74fdnsbtFPqwZmQl3YyAJ5_CGbr1SbfOWyd0Jt0KRs-TyU0_4mCYhBoI9zYKGuWfUHeCL9Jl4aidIBzqSk5BlF45WfPIvGNeSzoE2Ep7cq6qy1BfP_DajS4MqwF3GDht3q83nuDvnEXnxzrc9WEPPvvKdoesL-ONG5KxwZCXMBh1UHo_FUHU0q9mjhSY31FuCW0avJqSARmyLFXtVL0bukW07IgekxXbcrIiP6puNlcW_jXQizLDmIjQshosKo2bjSRDsRzLDZiaH28Z6r9PKplLvFF7OvzPCXf1YcTcsCMqMzBiCeUVCqgmfiRvXcC9ynrbtYJObweVu9rcYHECDOWoBQBBu63dprWmcE-ABmXNgOibDDcA-ho" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4748c9bb82.mp4?token=IOc85Ybl19m2hTXvO6UXJfuFJgDdRcRR8WIj_97678kXhp24Vvl39-rF631hRrisrbXK0WLtt43SZHcGC0gQmfoRKcxpjtlvzf-PTeAGNlh0kR1PBKpM9KfrUrONfL2fgvl9KPKGHsUNNYBFaAIH9hnsP1rCCT8g7QM0ch1mSS_Rpfzg9hO2CzbJzLA0rs4K-wnDEmQUxCzCw-BhlgsENT-tkjqJuVv0CPa9MxP3hIyZPzoplVoyqXb9ZMfPsyH25-9_0RDH_VORUvFwzKURyPt7WjrgxKStmt44-ZQovyoC47_cmdmu74fdnsbtFPqwZmQl3YyAJ5_CGbr1SbfOWyd0Jt0KRs-TyU0_4mCYhBoI9zYKGuWfUHeCL9Jl4aidIBzqSk5BlF45WfPIvGNeSzoE2Ep7cq6qy1BfP_DajS4MqwF3GDht3q83nuDvnEXnxzrc9WEPPvvKdoesL-ONG5KxwZCXMBh1UHo_FUHU0q9mjhSY31FuCW0avJqSARmyLFXtVL0bukW07IgekxXbcrIiP6puNlcW_jXQizLDmIjQshosKo2bjSRDsRzLDZiaH28Z6r9PKplLvFF7OvzPCXf1YcTcsCMqMzBiCeUVCqgmfiRvXcC9ynrbtYJObweVu9rcYHECDOWoBQBBu63dprWmcE-ABmXNgOibDDcA-ho" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سهم وزارت دفاع در قدرت‌ ملی و قدرت‌ دفاعی کشور چقدر است؟
🔹
راهکارهایی که شهید نصیرزاده برای وزارت دفاع داشت، استمرار دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/683181" target="_blank">📅 22:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683180">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7984717235.mp4?token=Gs64vgOs7HZgOVSimbVdg4JR_OhTVvXkrDBfrD7LpbroaqGALS7zJGCHng2MjG321bnEL2Q34it2F8ySrhUa9CORvuqSvQH3xycdXtjqAk0sXfj7wSp2Lqr5gBr74pGIQL92IXAqQrL8wu3nZQMTF95D_jFXP_tvjUC4CRddt2Xo9uxJvxM4kMVYKSWvtT1q29NJjHhTR11APRDYFJ4Ya--qPwmjjhslYvqfx6E3aISEGp9xAppw7OVTOQ0SeARSwkH3YNKxernIMDAz5ff8n_UrpHYet2jmZBlG4XPy1dtDvukJwOPqh70Rfdulk4UaCqaip0sUkTh4Zs6hvzjYZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7984717235.mp4?token=Gs64vgOs7HZgOVSimbVdg4JR_OhTVvXkrDBfrD7LpbroaqGALS7zJGCHng2MjG321bnEL2Q34it2F8ySrhUa9CORvuqSvQH3xycdXtjqAk0sXfj7wSp2Lqr5gBr74pGIQL92IXAqQrL8wu3nZQMTF95D_jFXP_tvjUC4CRddt2Xo9uxJvxM4kMVYKSWvtT1q29NJjHhTR11APRDYFJ4Ya--qPwmjjhslYvqfx6E3aISEGp9xAppw7OVTOQ0SeARSwkH3YNKxernIMDAz5ff8n_UrpHYet2jmZBlG4XPy1dtDvukJwOPqh70Rfdulk4UaCqaip0sUkTh4Zs6hvzjYZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از اصابت پهپاد به تجمعات سعودی توسط انصارلله
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/683180" target="_blank">📅 22:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683179">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5FcTu9j8_6Gt6z3EbMzMqn_dY3hQqv7eCQNN83OkIRH0P9P4Lj4RfiHqvLb026S7sDUISTIXOC2W_ar7fsBweD_OibJquBFviL9YuMNKLnaiGDNjHvwsidex2I5IXwUl5AsX_khuYhPWhOO76krf508L5aIObR3mzPkANbhonOxV8QQGXS3BtpCLbXefiFT8j03HaXCHhlWay_QN9H_B1z268-UOwxpV-7MK8cLexYRyUR49UGDyT_YlUfvOe6oZFmNAoMYBEFiYDk-i1n5hm07o19P4rC1v_bXJJObLCrn5w3ewCbwn3jcp72JIjS6VyRaSzV4aUDAv1NLRb1wYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
‏
ایلان ماسک: رسیدن بدهی آمریکا به ۵۰ تریلیون دلار برای کشور بحران ایجاد خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/683179" target="_blank">📅 22:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683178">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/227375ee24.mp4?token=N7M5fkI3YW2ymY85ap2eCyhldKhmfkIkpwAX8DfKe1EkpEN-FkQ01_yTwHspxC5lwPXde3i6HXqRKHObzVjZjxaK7GNjFuNBeDNLETatkMA3KFqksssjBL2loJk8uE2BaxNXPC940hgyU3qt5ec8FyDuitOawCAAJY3XxULbWLLuKifuaLiZPZnFFloyDa-uV1cdYxZ-0Es1rPI0yMi_3XjnKwrfaWEZMJXiBU0RwvL6IpVB4OTT6cunUCOww9A5R_h6NE9XPqZmT27KbY6PFu9ym-EtsSMpmac62-8yxSFe3bAqKkuJIo860ghsvftgLBGNPUZzirgdXW3izTWGoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/227375ee24.mp4?token=N7M5fkI3YW2ymY85ap2eCyhldKhmfkIkpwAX8DfKe1EkpEN-FkQ01_yTwHspxC5lwPXde3i6HXqRKHObzVjZjxaK7GNjFuNBeDNLETatkMA3KFqksssjBL2loJk8uE2BaxNXPC940hgyU3qt5ec8FyDuitOawCAAJY3XxULbWLLuKifuaLiZPZnFFloyDa-uV1cdYxZ-0Es1rPI0yMi_3XjnKwrfaWEZMJXiBU0RwvL6IpVB4OTT6cunUCOww9A5R_h6NE9XPqZmT27KbY6PFu9ym-EtsSMpmac62-8yxSFe3bAqKkuJIo860ghsvftgLBGNPUZzirgdXW3izTWGoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت دفاع:
در یک سال گذشته، میزان تولید تسلیحات و تجهیزات دفاعی در کشور ۲ برابر شده است
🔹
در جریان دفاع مقدس ۴۰ روزه، برخی محصولات راهبردی و اقلام مورد نیاز جنگ، بیش از سه برابر افزایش تولید داشتند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/683178" target="_blank">📅 22:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683177">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/972614d705.mp4?token=TIBCBqFeW31xedMzmAiD_pdoYbGzRpJYRKpAQGw5twW8WN-EV8nDKNxom94JgJvPQek9EZYwbRVdTsxUR_hZICnkps6H86kdwtyIUSW2iU0VOlTBHlmwXSb6boBaPkYkNIig3AXDLp540OUfwRAwwVGODL265yHlur7OKr3xI5U4aNo1CU6HpU1QOKY7qpCl2oGwUFIjBDra2C59cwFfdwM8BspatRpJvYYhH0IaXsIqlnUSmAh3gqZYVsqoT-0edb8r6Ssq7LZLyDBawafMmtRAhO_JqrQ6wuwM5W3bjdS-ySUqclTnOH7FDpiIrjBoTL1vSvwCQor6AhEpzgLOmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/972614d705.mp4?token=TIBCBqFeW31xedMzmAiD_pdoYbGzRpJYRKpAQGw5twW8WN-EV8nDKNxom94JgJvPQek9EZYwbRVdTsxUR_hZICnkps6H86kdwtyIUSW2iU0VOlTBHlmwXSb6boBaPkYkNIig3AXDLp540OUfwRAwwVGODL265yHlur7OKr3xI5U4aNo1CU6HpU1QOKY7qpCl2oGwUFIjBDra2C59cwFfdwM8BspatRpJvYYhH0IaXsIqlnUSmAh3gqZYVsqoT-0edb8r6Ssq7LZLyDBawafMmtRAhO_JqrQ6wuwM5W3bjdS-ySUqclTnOH7FDpiIrjBoTL1vSvwCQor6AhEpzgLOmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تهدید فدراسیون فوتبال توسط تاجرنیا با چاشنی کنایه به پرسپولیس: اگر تصمیم بگیرند جام قهرمانی را به استقلال ندهند، از طریق فیفا و AFC اقدام می‌کنیم ولی لابی سیاسی نمی‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/683177" target="_blank">📅 22:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683176">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113caef9ab.mp4?token=mXrlYSdpYHPiq5IXZpXQceaiM-0LYCxGvxjzQ3WiQ5GbtoCmYVVgcP4U328nQR9rzDWt06HAQcdSAPSiZyK2ivNRU1Nc_Y0qa_1Kp5O4NM_sfNbpUzH4s-U9csR5MCcjdn9j3gAMFt_auBjXI3CotixpvS4Q7B_F9plDASItJ3U19Smldh8XkJsHTmnZwY_bl0MPqwB4EmQDk34sSMY9vRAu_NgkhTMSvWbIPIvTD233aDU1DwSTbMdH_sn4RWxwVC9Aqh6lHDjct9ueXuMte2SbY2cbIGiU-2v8lqFZ_hP-9c8M51cOFqxjXOU_BZ64Q_6LTDe5-jCa3De1KqNXRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113caef9ab.mp4?token=mXrlYSdpYHPiq5IXZpXQceaiM-0LYCxGvxjzQ3WiQ5GbtoCmYVVgcP4U328nQR9rzDWt06HAQcdSAPSiZyK2ivNRU1Nc_Y0qa_1Kp5O4NM_sfNbpUzH4s-U9csR5MCcjdn9j3gAMFt_auBjXI3CotixpvS4Q7B_F9plDASItJ3U19Smldh8XkJsHTmnZwY_bl0MPqwB4EmQDk34sSMY9vRAu_NgkhTMSvWbIPIvTD233aDU1DwSTbMdH_sn4RWxwVC9Aqh6lHDjct9ueXuMte2SbY2cbIGiU-2v8lqFZ_hP-9c8M51cOFqxjXOU_BZ64Q_6LTDe5-jCa3De1KqNXRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت دفاع: یکی از ویژگی‌های برجستهٔ صنعت دفاعی ما، سرعت و قابلیت تولید محصولات دفاعی است
🔹
به میزانی که در میدان رزم سلاح و مهمات استفاده می‌شود، با سرعت جایگزین می‌شود
🔹
تنها راه سلطه‌ستیزی و مقابله با قدرت‌های بیگانه که می‌خواهند استقلال، موجودیت و هویت ما را مورد آسیب قرار بدهند، فقط قوی شدن است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/683176" target="_blank">📅 22:33 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683175">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb6313bb63.mp4?token=qy5x2JnUZJL_fAF0gWjRQr6OWeMoZ1kMwpl1eOn53O3qfXE-MMfX5T50HPensxsWm8d621PPtK3azJnkbG9jKkdtUNdhvoLoVSQxiSnSJb_qxpePbX4n85xRELXOpuO1p5DtNT8D-_2kTndMNAMyQtJbxK5PlQ0lMTXbmU-khnspIcu0d54sop7xI-i0HcseDd-B5mU0qpmGri8rXBiidIr3jQh9InPPpPNGrRYnmImlyLIg409o5_QXZA-uivFUfnrLudK3oiJ4YJRUt-c2IKO9rA_x-p21iKlQgZaHcF7xTmWgBfPvxvNODYpw7bKS7ntHZQaVSJdTqiRG5x8WDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb6313bb63.mp4?token=qy5x2JnUZJL_fAF0gWjRQr6OWeMoZ1kMwpl1eOn53O3qfXE-MMfX5T50HPensxsWm8d621PPtK3azJnkbG9jKkdtUNdhvoLoVSQxiSnSJb_qxpePbX4n85xRELXOpuO1p5DtNT8D-_2kTndMNAMyQtJbxK5PlQ0lMTXbmU-khnspIcu0d54sop7xI-i0HcseDd-B5mU0qpmGri8rXBiidIr3jQh9InPPpPNGrRYnmImlyLIg409o5_QXZA-uivFUfnrLudK3oiJ4YJRUt-c2IKO9rA_x-p21iKlQgZaHcF7xTmWgBfPvxvNODYpw7bKS7ntHZQaVSJdTqiRG5x8WDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجمع جنجالی برای دفاع از مادری که به قتل سه فرزندش متهم است
🔹
تجمع گروهی از فعالان فمینیست در حمایت از زنی که به قتل سه فرزندش متهم شده، واکنش‌های گسترده‌ای به همراه داشته است. حامیان او بر ادعای تأثیر داروها تأکید دارند، در حالی که دادگاه درباره عمدی و آگاهانه بودن اقدامات او بررسی می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/683175" target="_blank">📅 22:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683174">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
میکروب‌های زمینی در ماه زنده می‌مانند!
🔹
یک مطالعه جدید نشان می‌دهد که میکروب‌های زمینی می‌توانند در سطح خشن ماه زنده بمانند، البته در حالت تعلیق این اتفاق برای آنها رخ می‌دهد.
🔹
تحقیقات قبلی نشان داده بود که سطح ماه برای زنده ماندن میکروب‌ها بسیار خشن است. به طور خاص، یک مطالعه در سال ۲۰۱۹ نشان داد که اشعه فرابنفش و گرمای خورشید بزرگترین موانع برای حیات میکروبی در سطح ماه هستند./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/683174" target="_blank">📅 22:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683173">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
نخست وزیر عراق: هیچ قصدی برای رویارویی نظامی با گروه‌های مسلح وجود ندارد
فالح الزیدی:
🔹
برخی گروه‌ها سلاح خود را تحویل داده، ارتباطات سازمانی خود را قطع کرده و به حشد الشعبی پیوسته‌اند؛ با گروه‌های دیگری نیز در حال گفت‌وگو هستیم.
🔹
اجازه نخواهیم داد این کشور به عرصه تسویه‌حساب‌ها تبدیل شود. دولت قصد رویارویی نظامی با گروه‌های مسلح را ندارد./جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/683173" target="_blank">📅 22:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683172">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGLqn9NQ36-cvRTgmpdZ39AV4hwT2n2m6nvJKUhbtN-3AafxAKwq3IIeq3dlTo_XHQ43XrQphWt3_4NSesmXxTDu8epMeJaCvlsfkT6lgxrqGvoupFVfWZ5c97LkevieppZz5uYMZ8pcaUGDlVhWGxikIZ2ATbl__YcfA53hhcaFwIzcxGv4Zbtorcl97ylQfCixkUORJH7micnTip13wI9mMsqIWzuqrf1NsMMLZQSIakMk6PCHt7rKn2Zg8KBdmQSsnJg8S51H9rQXUqonrpiQzQJ8gI_kKic3SaCzbPjn_xa3GGVzccosEnxSWbI1w7crbyW7_y2HHILZChhM9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چجوری بوی بد پا رو از بین ببریم
؟
🔹
ترکیبی از آب گرم + جوش شیرین درست کنید و پاهایتان را ۱۵ دقیقه در آن قرار دهید باکتری‌ها را نابود می‌کند.
🔹
قبل از پوشیدن کفش کمی جوش شیرین در آن بریزید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/683172" target="_blank">📅 22:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683171">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUNiWrll5kD-W8UkfTGb8sLkp39Y6BHaoMU2a9AN3S6b1jkty1Tv-dhtXInN3x47oKah8qaVNShbGs_RnRl0eQxXAyahfXvntL8bUNd9ZmxDNAWrJLxNS8vdM-YL_xZpATH1gdsOtDlOE18odJUpROz9rJigUnsskDSmF_GMttZ5hAdLFEfGOUEhI6zcIJ9NcaTWs1h320r9yQ86fO-K7vuD8NyCqgYY0CWH-djnoLoZ3fBn5gTI3dtiXG1BJs1YkAxuTS8rTUvuOHg96GCWddzW35csFIBQsms1vyo13Qb1lPywe2YGL6zcd3ib7qQuy1dXtxIK7SsoR6vmL_ULBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاردین: نگرانی مردم اروپا از وقوع جنگ و حملات سایبری، آنها را به نگهداری بیشتر پول نقد متمایل کرده است
🔹
برآوردها نشان می‌دهد هم‌اکنون ساکنان این اتحادیه یک تریلیون و ۶۰۰ میلیارد یورو پول نقد در خانه نگهداری می‌کنند؛ این رقم در مقایسه با ده سال پیش ۶۰۰ میلیارد یورو افزایش یافته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/683171" target="_blank">📅 22:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683170">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
نتانیاهو کودک‌کش: اجازه نمی‌دهیم اردوغانِ دیکتاتور سوریه را اشغال کند
🔹
نتانیاهو با متهم کردن اردوغان به دیکتاتوری، یهودستیزی، کشتار کردها، پناه دادن به حماس، اشغال نیمی از قبرس و زندانی کردن مخالفان، تأکید کرد که اجازه نمی‌دهد او دامنهٔ تجاوزاتش را به سوریه…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/683170" target="_blank">📅 22:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683169">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B43oz-Jvwq78uXGiZYbBgeK_H5D6H5YVBSHh4ufIySUZhKsAjf1qwYGeAz4aCMovvpYul5w7nuDWiOTBrIVFxgwbdgYQqYl6TzUQM8zrCGdVNEYh8sgmxB3xbkmsM4XcXo5hVGgrv2Pv-RL1MVRujk3Hn1wx4RJ-217qvkVmihIHl7j6P44g3lA6pye4-S6uFwveM-1SnP-_Cm5VTtRyjwzu7rN2WgyBw06o4sNZuYb7ALxJCh16WNomvOCZ0ibWrTUcddrX3oviclF-10SdGCDxkpFGfmrpM4c9QyLS-a5E7h6rf1TKI9tVChFkoh4hMQTmcNG31LIe1OEFaKP6WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
اگر دانشجو هستید یا در ۶ سال گذشته از دانشگاه فارغ‌التحصیل شده‌اید، از شما دعوت می‌کنیم در این نظرسنجی علمی درباره کنکور و قبولی دانشگاه شرکت کنید.
⏱️
زمان پاسخ‌گویی: حدود ۱۰ دقیقه
🔒
پاسخ‌ها کاملاً ناشناس و محرمانه است.
پاسخ‌های شما به شناخت بهتر تجربه‌ها و دیدگاه‌های افراد درباره آموزش عالی کشور کمک می‌کند.
برای مشارکت در نظرسنجی، لطفاً وی پی ان خود را روشن کنید.
🔗
لینک نظرسنجی:
https://harvard.az1.qualtrics.com/jfe/form/SV_6MsiAUIGfXgJZQy</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/683169" target="_blank">📅 22:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683163">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EBA68UWtDho0wptMKglYEGNamGNu1700QRIwa29AcpqT1HqpCmNf1A9X-BGxJZXx3m8_8YLKbno6K59cwM8D-EtqsF2gjEKKZnI-WrkA-RoyHnV3EFUcBn9khLJkfKx6at6QvtxMjsMyBkXTH6al7gJTuvxeSeWFc0l_84Y3qcf3p5r9JnI9T_lBhjWi0Hf8VdeLJwEelVvtOdge53z-PUMjCQrsBmA6VK7jhG384CvQ6CREb5G8sly6EOtH7yL0JyTCOtSxwgfUb2MbsckCn8lJH9tPw68D3DnH6gj9wQGw9n2lQums6kuzIROrJm7zhrRyjDf5L6yfSTDB-0ZMrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IgpaUiDvfpqECTN74aQhPynoB3kAesPmOq7WWn7jP3V54oy5v9Y2pWXsKkK-kcCxKwEtVP9EDooKpOwiDL0WirSihRiykJPuCl1K_le_J4XlvkPKU1AK_8-_Z7C27WWMxa_eWhaczHZdQ9sHP6N4N6ZclODSQLIYiMdK_57rR6ITcEAVwyQ_0MzbqnUE_uNiWYAku4NgoKX2uLhSPQvy76pNPYggNHkhp4AmdO_XmmpLDug3lM7bq9Jj3ZiU2AJnFrW2EosP8WizdYlyOjINM8Pj2Yhz9HNEVOaBON7Xu0MuYVYRsD_50Tb4MrZR1tBRlp_pnM6sXtgUHxu4T3EGeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a5da8055a.mp4?token=ZmzuQeXjndOa-AEWOt1SF83UrlgW477iI0VEEwSHPZ2jqo7AvB2QIJPXSFpKCyY2TwNv0rSg1QveU2O787Aq2vhVS0MtCuRITVqEErOK5FdGWI4PAM3HZ0yk4iXI_QYlnrYRTt8ACv-Q1_B9ZgfOyC992Qu_grOrXujbhekw01FWuxBK-1vVHoD5tx8weHksq-t6nb-Tvds9RUBX8kg0ma38r-I8DNXOdaY4P1e0f77Z_zbIM_yUnKUUWiQllSZfup5nz49Hz6cPshImRN7if9rVLLGVXoNMBOjJVOxp60djvCfDlgrL_Wb8y8o328otRNhBNApndiv8GAWnGXVvOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a5da8055a.mp4?token=ZmzuQeXjndOa-AEWOt1SF83UrlgW477iI0VEEwSHPZ2jqo7AvB2QIJPXSFpKCyY2TwNv0rSg1QveU2O787Aq2vhVS0MtCuRITVqEErOK5FdGWI4PAM3HZ0yk4iXI_QYlnrYRTt8ACv-Q1_B9ZgfOyC992Qu_grOrXujbhekw01FWuxBK-1vVHoD5tx8weHksq-t6nb-Tvds9RUBX8kg0ma38r-I8DNXOdaY4P1e0f77Z_zbIM_yUnKUUWiQllSZfup5nz49Hz6cPshImRN7if9rVLLGVXoNMBOjJVOxp60djvCfDlgrL_Wb8y8o328otRNhBNApndiv8GAWnGXVvOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
#پک_استوری
امامت امام زمان عجل‌الله
آقا مبارک است ردای امامتت
ای غایب از نظر به فدای امامتت
#امام_زمان
(عج)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/683163" target="_blank">📅 22:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683156">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda5519a1b.mp4?token=hsgiWuGKI4ZHcZ53c5Ub7ZdA0YIUniI9tklnLbCWXugd0EwrMykDjOPI-B1FZufB3vaPhx3WbHO-mj7hd8mS88vSPLZ9d7bNX11xwdfq4apDNv9FWKrxzvHdJctsPghHRlx0_s1jisXxQdAdPfdFQ1J3Zo7MN64z7PN2ElCFuYpRQZel_u2XsIbT75mf7oJaXT0Vng0Hs_Wz4_8lXnfReL1i-e3E6CtobBcSHoa9pIHU0pKdTjRwthvJeuxsihzqNSJmer9mzD9io6nhnfkYLUxZ1JFE_U9mt0d3lpBJAij61zxvULEXhK3KNKWd0fhuFmmijL1hV2Td96SdCKkKSx2hQik_mSdrDW23WzOdgXzfUBgFx2GzwhJEVVwrKBPc6nLYy51nTCj42t9971UwnEMFJa4Dg_FwnOdUwfBjtKOv5dYjY96haRO83CAv7c0-KmAOdR3Yu4z1xqqY81mSv-EZrSsN8346VPsdotyZjsXlIiwFyBxzAP504d3txQS8pPYgyrHsMfSEkBetm7gOzB05Tgg4I-bmSQHxB3SW3BFnOTQwkvmu8vWE821Q4nj_knbrR0IeQNK_-AUMqsf75zFGa_J4kEG0A6PImroD9Q78lgHvLyUepmv97ZKMUAFrC8XcbHrphw8hsb0NJGG4yr9CC78_gjjJoJt0CB19KqI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda5519a1b.mp4?token=hsgiWuGKI4ZHcZ53c5Ub7ZdA0YIUniI9tklnLbCWXugd0EwrMykDjOPI-B1FZufB3vaPhx3WbHO-mj7hd8mS88vSPLZ9d7bNX11xwdfq4apDNv9FWKrxzvHdJctsPghHRlx0_s1jisXxQdAdPfdFQ1J3Zo7MN64z7PN2ElCFuYpRQZel_u2XsIbT75mf7oJaXT0Vng0Hs_Wz4_8lXnfReL1i-e3E6CtobBcSHoa9pIHU0pKdTjRwthvJeuxsihzqNSJmer9mzD9io6nhnfkYLUxZ1JFE_U9mt0d3lpBJAij61zxvULEXhK3KNKWd0fhuFmmijL1hV2Td96SdCKkKSx2hQik_mSdrDW23WzOdgXzfUBgFx2GzwhJEVVwrKBPc6nLYy51nTCj42t9971UwnEMFJa4Dg_FwnOdUwfBjtKOv5dYjY96haRO83CAv7c0-KmAOdR3Yu4z1xqqY81mSv-EZrSsN8346VPsdotyZjsXlIiwFyBxzAP504d3txQS8pPYgyrHsMfSEkBetm7gOzB05Tgg4I-bmSQHxB3SW3BFnOTQwkvmu8vWE821Q4nj_knbrR0IeQNK_-AUMqsf75zFGa_J4kEG0A6PImroD9Q78lgHvLyUepmv97ZKMUAFrC8XcbHrphw8hsb0NJGG4yr9CC78_gjjJoJt0CB19KqI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی پایان سربازی هم تبدیل به یک «مُد» اینستاگرامی می‌شود؛ از یک اتفاق شخصی تا نمایشی برای لایک و دیده‌شدن!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/683156" target="_blank">📅 21:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683155">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45944f0cdf.mp4?token=HJMF7t4AMfbdIxdv4aQv3gh8LulSNPVHIIeRY8zyY6Y0SB4PLKr2iL0Gw80vR8DX5y3Tc2vuFNZNr6uJEGFkDcenkmO8sSsQ_VD37BWMlijPN_X-bxlus13i4pS1fFMCtqZzJw8ZqqMOJWQtPiFM3yX39NUuCdugDpNCAlaB7dBEJBLapbHkjvNdiX7MiKo8F5i4aCQfCJsal5BKTxMPTqngHtVniT-HVguhRT7uzpExeX5RaZDUxRT3AcD6IcFSB3iQYfkWl9wvn2eONK3hyqv125k3fIRdl7_IMZBwf7IuFQkp72lSApvKxsJeVLWTiHstVK21ih4vNsn3ak4Gfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45944f0cdf.mp4?token=HJMF7t4AMfbdIxdv4aQv3gh8LulSNPVHIIeRY8zyY6Y0SB4PLKr2iL0Gw80vR8DX5y3Tc2vuFNZNr6uJEGFkDcenkmO8sSsQ_VD37BWMlijPN_X-bxlus13i4pS1fFMCtqZzJw8ZqqMOJWQtPiFM3yX39NUuCdugDpNCAlaB7dBEJBLapbHkjvNdiX7MiKo8F5i4aCQfCJsal5BKTxMPTqngHtVniT-HVguhRT7uzpExeX5RaZDUxRT3AcD6IcFSB3iQYfkWl9wvn2eONK3hyqv125k3fIRdl7_IMZBwf7IuFQkp72lSApvKxsJeVLWTiHstVK21ih4vNsn3ak4Gfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایرانیان در تاریخ بارها ثابت کردند که خلیج فارس و جزایر آن، از جمله خارک، با هیچ سلاحی تسخیر شدنی نیست‌‌...
ادامه ویدئو
👇🏻
https://youtu.be/PkNQz2D9nTY?si=MZvjgT4CBM9FkUZQ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/683155" target="_blank">📅 21:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683154">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
حکم نهایی نظام وظیفه؛ بیرانوند از مهرماه سرباز است
سردار زاهدی، معاون نظام وظیفه عمومی:
🔹
علیرضا بیرانوند از مهرماه ۱۴۰۵ سرباز خواهد شد و دیگر امکان بازی برای تراکتور را نخواهد داشت./فرارو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/683154" target="_blank">📅 21:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683153">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-poll">
<h4>📊 به نیت سلامتی و فرج امام زمان (عج ) نابودی شر و کفر چند صلوات میفرستید ؟</h4>
<ul>
<li>✓ ۵ صلوات</li>
<li>✓ ۱۴ صلوات</li>
<li>✓ ۱۱۴ صلوات</li>
<li>✓ ۱۰۱۴ صلوات</li>
<li>✓ ۱۴ هزار صلوات</li>
</ul>
</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/683153" target="_blank">📅 21:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683152">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ادامه گزافه گویی معاون ترامپ علیه ایران
شبکه اسکای  نیوز:
🔹
جی‌دی‌ ونس، معاون رئیس جمهور دولت تروریسنی آمریکا مدعی شد که واشنگتن ابزارهای فشار لازم برای مقابله با ایران را دارد
🔹
او از ادامه حضور آمریکا در منطقه با بهانه‌ موضوع هسته‌ای ایران اشاره کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/683152" target="_blank">📅 21:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683151">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
هند خواستار حل‌وفصل تنش‌های خاورمیانه از طریق دیپلماسی شد.
🔹
سی‌بی‌اس: تحلیل‌های اقتصادی نشان می‌دهد ۲۵ درصد از نیروی کارگر آمریکا «عملا بیکار» هستند.
🔹
رئیس مجلس و هیئت پارلمانی همراه وارد تهران شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/683151" target="_blank">📅 21:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683150">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkgHx1fgekMR8xnn4FVui2aGCDpxhRg-hrxmZBZDOE8fRUlJu5H9wWFmXz6YkKMq-wEqGOB33yfC0jACx7NGtv05TDBY-5DDUtHtpD6FWzP7vxQyxn5Zhi50QfzioiJ7YkvPyGMPNxRC_IDgBRYF90plHDvNf0-eiIxbNIz43nWXeD2say6oDTaUQAa3L9S7nJQSvIH7LbxDj0_Vvb2LVkYasgQUraLvDyNooT053yml8N2QrDS6VwWS45XcO7Dt7I2UyKOiwQdHcRnmmvwxeri4a5S_IFrYccTrWQKao3qMjy5FeMbDHCg13ujda27BdJgikfYcDPmTElFfuxgHhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت جهانی انس طلا بیش از  ۲۰۰ دلار گران شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/683150" target="_blank">📅 21:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683149">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/198312ec77.mp4?token=hugbt3TOSmbofsiwNFBZsVw73dJaXs76zFGZQmwEod7I-Z67atcBlfOfL9yG64BGn1xOUbMeUGWFFdXsq0Lusb1OUAh4dxnmDh6a2j4KuWn-KADysx-LXFexB7c1hU21C3qgIBrbOIa03JUAOVB9p4RJRn2hMe8nyqELqC8GQ4CMGHgFm4b3nlk6yS5WVRf_KN4X9I1qydB643lqxTkfWm3irH7xpQCfbbuLZqG2JY496pjLa4Fdyj8Bf2GnnqMpJXDCvNKdx-qddV4XZy14dMn0BtGSZgDb_jfMHibG1xePqkSoRvsywwDIhc82ojOmiUETE-EouSiu7CQlxGQPSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/198312ec77.mp4?token=hugbt3TOSmbofsiwNFBZsVw73dJaXs76zFGZQmwEod7I-Z67atcBlfOfL9yG64BGn1xOUbMeUGWFFdXsq0Lusb1OUAh4dxnmDh6a2j4KuWn-KADysx-LXFexB7c1hU21C3qgIBrbOIa03JUAOVB9p4RJRn2hMe8nyqELqC8GQ4CMGHgFm4b3nlk6yS5WVRf_KN4X9I1qydB643lqxTkfWm3irH7xpQCfbbuLZqG2JY496pjLa4Fdyj8Bf2GnnqMpJXDCvNKdx-qddV4XZy14dMn0BtGSZgDb_jfMHibG1xePqkSoRvsywwDIhc82ojOmiUETE-EouSiu7CQlxGQPSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شقایق جای خشخاش را می‌گیرد
دبیر ستاد مبارزه با مواد مخدر:
🔹
کشفیات مواد مخدر خلوص کافی ندارد، واردات مورفین هم گران در می‌آید برای همین مجوز کشت شقایق برای تولید دارو صادر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/683149" target="_blank">📅 21:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683148">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ایران قصد دارد بزرگترین نیروگاه خورشیدی جهان را با ظرفیت ۵ گیگاوات در اصفهان احداث کند
🔹
در حال حاضر، رکورد بزرگترین نیروگاه خورشیدی جهان در اختیار نیروگاه خورشیدی می دونگ در چین است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/683148" target="_blank">📅 21:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683147">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bp7yBP28-kZMPAnIy6rf0y3x6ZiC6_CpMBUXgXqr8CsnMyOnva4kgzpykD-WhXz2d1RZpsWlp1f6dp7QvvdmI2pJjqrwN9_LQBH0UzO1ZqU5kG83-LTVRUuW5csWzzAWOpnjWaqa9IUgW-RFYIlqj1LLqCWsmPX0Q5HNrcPKMYZ5YEV5PiTjhp3jsBaYYXvkEYVB_j-zR0Pz7qfAf23_Rsm_r92tglthEteaRuZtzrkPp9gyj81BktN9AVpXLTJkjw62i1Z8ISAzqAnSUP1U5PM4hTqqk748ASZyW-xJBCI5ha6jPMRUvpw6nqxLW383PnMpMC7EMB8BT4z62mj78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از جنجال کریدور مرموز در جنوب تنگه تا شایعه اختلاف لحظه آخری تهران و مسقط در مذاکرات/ عمان؛ کلید جنگ یا صلح ایران و آمریکا
🔹
همانطور که عمان می تواند حل‌کننده مشکل و درگیری ایران و آمریکا باشد، به همان شکل، قادر است این اختلاف و درگیری را تبدیل به گرهی کور کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3239391</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/683147" target="_blank">📅 21:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683146">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAxXokfVnw5tUTnnnPX6QAngT61RWXFjdEFmR_tGc8jQG1liZTNMC6O0vHT-hnpTAEIel2B6VjTh6Hko_fIaItKuRZf26_jEzdfo2xU5e1QSxABazLOnRRSy5g1nNYSXyzUyElYTAOn4-mXdwunyzKqMd-qrYUN5Hb8YuwRHwUnXCqqIZHdsI1CUEVjFPIBY_FNtuK-0X44e1jPJj9wqRXe8mH1hg4PXPXWOv5xQ84KVOo-VBB7ZbtKvmo7L_IfVBhgYPiFWxfDJSfcipFop0sBztZS4f8B7bPOAptgN26GKu1QJyNpF5fDUIpDCGTgtpd66C31OCItRIwFxIP1XSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌼
بیعتی دوباره با صاحبِ زمان ( عج)
💚
به مناسبت سالروز آغاز امامت حضرت ولی‌عصر (عج)، در اجتماع بزرگ «مراسم تجدید بیعت با امام زمان (عج) و رهبر معظم انقلاب اسلامی»
▫️
با کلام: حجت‌الاسلام و المسلمین حیدری کاشانی و علی‌اکبر رائفی‌پور
▫️
با شعر خوانی : احمد بابایی
▫️
با حضور:  سرکار خانم الهام چرخنده
و حسین حقیقی
▫️
با اجرای : امیر مهدی باقری
📍
وعده ما: شنبه ۳۱ مردادماه، ساعت ۲۰
میدان شهدا، مشهد مقدس
🤍
بیایید در این شب عهد و انتظار، دست در دست هم، بیعتی دوباره با امام زمان (عج) کنیم...
@Heyate_gharar</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/683146" target="_blank">📅 21:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683145">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
خیابان‌های نیویورک پس از طوفان شدید به رودخانه تبدیل شدند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/683145" target="_blank">📅 21:08 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683144">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4e4525ee9.mp4?token=JXwqExefPzGM9mSZ4zRux416d5ZLwuOx7ikd_l-cG3rNrRo73COpgX2CtPSIwuzGEgZU-uzTFQpE9HlPsLF5gOs2HeFqhlUAx7UCTxS1tvVHckoNCh9Icws_0vHDghsq5G1bsGrYtl6liRpj0KNRpnpj0LKcUlG174y43NDKaUWpJfDnWblDE50qyIYREKtDO4gCSPfwrt8Ui6-K6y4-uZz12TSEVpyVLeGRkYDflV2ULt1zRLVLrjIL3NuRC0N8WtqbxWdM_QSuJus2MEx1B5sa8mHdgLm9QRUDJytzY2Eh7iKJfyqnT2h8m8cX5H6vTpJGDWR_sjtnNNTu80bl3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4e4525ee9.mp4?token=JXwqExefPzGM9mSZ4zRux416d5ZLwuOx7ikd_l-cG3rNrRo73COpgX2CtPSIwuzGEgZU-uzTFQpE9HlPsLF5gOs2HeFqhlUAx7UCTxS1tvVHckoNCh9Icws_0vHDghsq5G1bsGrYtl6liRpj0KNRpnpj0LKcUlG174y43NDKaUWpJfDnWblDE50qyIYREKtDO4gCSPfwrt8Ui6-K6y4-uZz12TSEVpyVLeGRkYDflV2ULt1zRLVLrjIL3NuRC0N8WtqbxWdM_QSuJus2MEx1B5sa8mHdgLm9QRUDJytzY2Eh7iKJfyqnT2h8m8cX5H6vTpJGDWR_sjtnNNTu80bl3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطوری با حقوق ۳۰ میلیون پس‌انداز کنیم؟
#جیب_من
#چرخ_زندگی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/683144" target="_blank">📅 20:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683143">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afd4c75b53.mp4?token=aq607iI53-xxdbnHnRolyHV6Pznwwv2UwNogwPgORyAlVSsvYDi8ZfJXTuzskw-50pcJl_SYy0o0ZUOagZBMItjLDf0_Cv9is9eULUVkdbGLfv1IBuINOj77tG6wVdcOWbcb7wDbMl-Wd0zsn7MBMpL9LdwqA-ni103LdYaVpT6ZEk7UYzMiiUl_6MmfttdYWh4zIxS-MI9tgVfYVmtElcZaG7GLASXh9HGz3L4Ov9BDEBK0hCkSSm63GbRV3Dflo8UZeIiaJcAyLkzszgPFTRKv_LgrGAhtfhkzkOfNFTSfNcktk28A5t1wuAKQBgIZ-6olX2VpBeeZHrYZQHgxUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afd4c75b53.mp4?token=aq607iI53-xxdbnHnRolyHV6Pznwwv2UwNogwPgORyAlVSsvYDi8ZfJXTuzskw-50pcJl_SYy0o0ZUOagZBMItjLDf0_Cv9is9eULUVkdbGLfv1IBuINOj77tG6wVdcOWbcb7wDbMl-Wd0zsn7MBMpL9LdwqA-ni103LdYaVpT6ZEk7UYzMiiUl_6MmfttdYWh4zIxS-MI9tgVfYVmtElcZaG7GLASXh9HGz3L4Ov9BDEBK0hCkSSm63GbRV3Dflo8UZeIiaJcAyLkzszgPFTRKv_LgrGAhtfhkzkOfNFTSfNcktk28A5t1wuAKQBgIZ-6olX2VpBeeZHrYZQHgxUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابلاغ پیام رهبر انقلاب به مردم عراق در سفر هیئت پارلمانی ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/683143" target="_blank">📅 20:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683142">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcf5d544c.mp4?token=ACA6OqMZxlLf5awfy7zPhUCSuZDxDa4fVkHQmvaMHvQj1Yj_moBK6Js9GqxKfTolVCsCvy7QF73liWGQMt-EMjrAb_kzArN6c3csPy-fGV-DS8k8-B6xcgLWsAhPJVgnQ-t5i1iZBQQNnThc7SMiv9Qds6RoWdSnjVuEZ-KNUaQJCvnjQbTbLFGch62DolNgZrVEVzp26fn4KooRbWmIsHa4RebPw8p4yxlgZ97mtpHZddagXCXVJPtRN1AqaRQoyLaWzYDMS0OL4I22v8bL83fyZe0CD1ouA8ihnpDMEPjTz3AYI9t7eFYqWPkl-0He-PKajZQbFDJdjhMYhDM3Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcf5d544c.mp4?token=ACA6OqMZxlLf5awfy7zPhUCSuZDxDa4fVkHQmvaMHvQj1Yj_moBK6Js9GqxKfTolVCsCvy7QF73liWGQMt-EMjrAb_kzArN6c3csPy-fGV-DS8k8-B6xcgLWsAhPJVgnQ-t5i1iZBQQNnThc7SMiv9Qds6RoWdSnjVuEZ-KNUaQJCvnjQbTbLFGch62DolNgZrVEVzp26fn4KooRbWmIsHa4RebPw8p4yxlgZ97mtpHZddagXCXVJPtRN1AqaRQoyLaWzYDMS0OL4I22v8bL83fyZe0CD1ouA8ihnpDMEPjTz3AYI9t7eFYqWPkl-0He-PKajZQbFDJdjhMYhDM3Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنباکسینگ ربات انسان نما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/683142" target="_blank">📅 20:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683141">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f649371350.mp4?token=Q1jkm2pUVAgAofr3vx7zGCddoTIxEm6Oag953RPIbdC52F9bHwBkIEZAOHhDj_f5sowmXvTGjVo5DMD3bxt8dgGsWpCASc1SEuR4nJFoyLCgI9Ci6uOOFimoe-f9uMk1VvQLGJR89qBYaxwcRfCFlo80Pf6V8ymzXeiShQtTjqtxaiORBeNA-KW90HBR3juwByID2GirCZCYU_U9EYiNmah5V__OL5GD4Ko8GKP20xvGGrquAsZws2HU36n0BbQbrIvDwv9dBfPO3UfupPb6WTkfbAYUAAfuYlzZvKRyLmCNOXsRzmRcdrZ_wiTmPyd3SG_DOkvchri1BzO_BRNymFLpl9-tp_gARPOm6v7iEizVnPEyT3_-NRD38IfjrF7WoSMpNN1eqrV4ypqghVqJrHAVcxrjORqwI0y90ThCs_P4Ay1S0FP18Fttz72k679_MctsqVtPnc6osc2l9aaP2TuklNW5vkRXUH9j0C6r23W1Vrksjckv3f_-IM2DElGcS4YZb1qW2ttCk2gXo6FEp6NxLiyoWYR2XOKPzqbTOmEIVSFCICcrjXtXoGNW--V0FMvCTOISow-Mql6tzxwnZWbUT-H7zTRIqHbaEww-qlzjEG7VJstrcDPL8baQuI-7qIaCKR3RZZvRT0VHBhWYgqM9wxf__eq8XTJgIz9MXeU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f649371350.mp4?token=Q1jkm2pUVAgAofr3vx7zGCddoTIxEm6Oag953RPIbdC52F9bHwBkIEZAOHhDj_f5sowmXvTGjVo5DMD3bxt8dgGsWpCASc1SEuR4nJFoyLCgI9Ci6uOOFimoe-f9uMk1VvQLGJR89qBYaxwcRfCFlo80Pf6V8ymzXeiShQtTjqtxaiORBeNA-KW90HBR3juwByID2GirCZCYU_U9EYiNmah5V__OL5GD4Ko8GKP20xvGGrquAsZws2HU36n0BbQbrIvDwv9dBfPO3UfupPb6WTkfbAYUAAfuYlzZvKRyLmCNOXsRzmRcdrZ_wiTmPyd3SG_DOkvchri1BzO_BRNymFLpl9-tp_gARPOm6v7iEizVnPEyT3_-NRD38IfjrF7WoSMpNN1eqrV4ypqghVqJrHAVcxrjORqwI0y90ThCs_P4Ay1S0FP18Fttz72k679_MctsqVtPnc6osc2l9aaP2TuklNW5vkRXUH9j0C6r23W1Vrksjckv3f_-IM2DElGcS4YZb1qW2ttCk2gXo6FEp6NxLiyoWYR2XOKPzqbTOmEIVSFCICcrjXtXoGNW--V0FMvCTOISow-Mql6tzxwnZWbUT-H7zTRIqHbaEww-qlzjEG7VJstrcDPL8baQuI-7qIaCKR3RZZvRT0VHBhWYgqM9wxf__eq8XTJgIz9MXeU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بانک ملی ایران: ۹۸ سال اعتماد، فراتر از اعداد و ارقام
🔹
بانک ملی ایران در پیامی خطاب به مشتریان خود، از رابطه‌ای سخن گفته که به گفته این بانک، طی ۹۸ سال گذشته بر پایه اعتماد و حفاظت از سرمایه مردم شکل گرفته است.
🔹
در این پیام آمده است که سرمایه سپرده‌ شده نزد بانک، صرفاً یک عدد نیست؛ بلکه حاصل سال‌ها تلاش، امید و زندگی مردم است و بانک ملی خود را امانتدار این سرمایه می‌داند.
🔹
بانک ملی ایران تأکید کرده است که این پیوند طی نزدیک به یک قرن، همچنان پابرجا مانده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/683141" target="_blank">📅 20:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683140">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VberFzRMDQSx-zOVu32wc46aDpdvTF3xAbOAtjw4tiGw_ZE2Yw4qpSOe65lf4UAeos-tZOgEzjnA423inos8VtHdmqI9Jt0t7hzZZCHTNLWc6OO8x2P8q-HxB8ZKzJrLma8Rl3TTcc_DYZYR22OhEvCm6ZrlzGylhik62nDsrvS0LPJYbghfk3mAERzQtTSmF5KwQqL2rlnPN9W0gpS2vE0IqeQ5Dh7YpfpgIG5ZiLA9a4o75Wjlrb1MNbjd8aQ7VltoyKHij8xrcHGJ1Uk2O28Xu7djlU9BRcVl8AMT-fADlyHxNs8PdQ2jrgIyfH_rXSFw02-Bb6FElloIot5abw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوراکی‌های ضد بوی بد دهان
🫢
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/683140" target="_blank">📅 20:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683139">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b9fc42fbc.mp4?token=cWECzKNIo8WAA3P7EzIihvGNaVS3q10uV5A73ZBkHoCcjfWNOv1mx_uxY9SKdDH9w8OTpUBInXUFwVygdMeE_5-NVQ8F0ujdjmR-AfjrOjQwpJtHlROwIwQEdFI2MOiMAdzZen7bDET0DTKOAkZFuJYj-NXIsiSnVA4kyfzyp2DknlitKX6z8ozOGzuT6_CmCijTdy2nzpj9_9KNjH360juI-QaevJW8GsczfiFy2IC5r52Vhed1joV85qZ1yCmxLUpgfbiVXb8NIo4VPJLnFHHEoqO6C4EFRCg3Z9xmjAuvFw6mRkaiTKo5r7cVdYCkiXIEpWdN9Snz5lm9P2awoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b9fc42fbc.mp4?token=cWECzKNIo8WAA3P7EzIihvGNaVS3q10uV5A73ZBkHoCcjfWNOv1mx_uxY9SKdDH9w8OTpUBInXUFwVygdMeE_5-NVQ8F0ujdjmR-AfjrOjQwpJtHlROwIwQEdFI2MOiMAdzZen7bDET0DTKOAkZFuJYj-NXIsiSnVA4kyfzyp2DknlitKX6z8ozOGzuT6_CmCijTdy2nzpj9_9KNjH360juI-QaevJW8GsczfiFy2IC5r52Vhed1joV85qZ1yCmxLUpgfbiVXb8NIo4VPJLnFHHEoqO6C4EFRCg3Z9xmjAuvFw6mRkaiTKo5r7cVdYCkiXIEpWdN9Snz5lm9P2awoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قصد فرار ترامپ جنایتکار به پنج طبقه زیر زمین به بهانه ساخت سالن رقص
ترامپ:
🔹
در این سالن رقص تا حد زیادی یک بخش نظامی هم محسوب می‌شود؛ با پهپادها، پناهگاه‌های بمب و همه چیز دیگری که در آنجا داریم.
🔹
این سازه تا پنج طبقه زیر زمین امتداد دارد. می‌دانید، تقریباً ۶۵ فوت، یعنی حدود ۲۰ متر، به عمق زمین می‌رود."
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/683139" target="_blank">📅 20:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683138">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/826d7da14f.mp4?token=hGDJ7RKHGjdq7RVBXNddnPb-0F-k0DayavDWruvQB75-7KwzKStouwOhL-Q-MCo8qhD-NuQG2hJI0xDizjgHE7SznK5DZSRT-DAMYhQD69sL3p2Hu7-z6snVydjpsYpTFF6mGDbSnXdlG8QC9pA86iykI8KjnZmcb3KjifZGBGW_BLQNDAxAjifZ8k28yYujAiZkyc731DU2Gaz6gtcDnpnUYbrtB6ib9VxXX6eb0QaakwCchWwNVY4NaXrgcS8i_7swH3__vO7N6LLmpG3jsJAiuua9xqrAFuASl6JrRe8fkq1oNZDniR7Ryx-fwAUyUeiAydhQlcX2nr9tj3kFbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/826d7da14f.mp4?token=hGDJ7RKHGjdq7RVBXNddnPb-0F-k0DayavDWruvQB75-7KwzKStouwOhL-Q-MCo8qhD-NuQG2hJI0xDizjgHE7SznK5DZSRT-DAMYhQD69sL3p2Hu7-z6snVydjpsYpTFF6mGDbSnXdlG8QC9pA86iykI8KjnZmcb3KjifZGBGW_BLQNDAxAjifZ8k28yYujAiZkyc731DU2Gaz6gtcDnpnUYbrtB6ib9VxXX6eb0QaakwCchWwNVY4NaXrgcS8i_7swH3__vO7N6LLmpG3jsJAiuua9xqrAFuASl6JrRe8fkq1oNZDniR7Ryx-fwAUyUeiAydhQlcX2nr9tj3kFbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زاینده‌رود زیبا؛ جایی که هیجان و آرامش کنار هم جریان دارند
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/683138" target="_blank">📅 20:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683137">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
آب سرد سازمان بین‌المللی دریانوردی بر پیکر ادعاهای ترامپ درباره تنگه هرمز
🔹
دبیرکل سازمان بین‌المللی دریانوردی، آرسنیو دومینگوئز در مصاحبه‌ای با شبکه خبری بلومبرگ ادعاهای دونالد ترامپ و مقام‌های دولت او درباره باز بودن تنگه هرمز را رد کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/683137" target="_blank">📅 20:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683136">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K42WGrWJfl-50KYay7ZVblYdjAv62ovzbZF47kRTS3YZy5affJByOq6L8aKdilzRm2TrR4Q324P7AzSomZ-CLYrWEvMJklSiHasDKFIsX7HDPgZFE24Mp95zZNx7Bhc8ycJ00v6jBaZA_QihBE5-cS_2u6I-BijDB7iQgDvui9lTQX_sYYfpAP5LXgKMlhJhY14GOT-JRvqkWVYbLFt-o5StIfUTF2ibg9LLDcZ06RZaPa9vSlJxboNNqE-6WFSx1B3wDIZjwGc_idovzB9pwALxkvox2nsKNq_fcspBwkzzMYjJ9iINM7U4ePy0g7AJ-rUupSjzMqVxd3YxO1uqLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا اعلام کرد پرتره ترامپ روی سکه جدید یک دلاری چاپ خواهد شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/683136" target="_blank">📅 20:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683135">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jcu_pVJRYPNDGe4AnE5Z8ZKBRH3T2MKXBLa1GG1389x74MW4IMO8KjpfWKbDd8-RuvZ2sbLRPzu9WBEsi_A4kJBRoIWsK0YnDCez55t-uf3p1WTZDknYvuU2ZWsoj3slmprAgrWghKNP-B9tX5-Zz0RwlfH-fzFB1QAy-wfY9JhIYNtYYz_4SckqnzNd5XQAgmWQv9DRhjZ-AWDQA-JOcCBqtDBPKAirxvr9cnDjzc5MaKpDUrh0o7eY47IwAM6MAHPMLM_6RITF_SVqEKG1BpVlAFqG8DIVcoQHA-jE13iZXw0n3disGRR_-Ns-csqMAL7gIMxDGQ3m7z8kRq_aIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: آمریکا با عذرخواهی از مردم ایران، منطقه را ترک خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/683135" target="_blank">📅 20:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683134">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EylqiMj-yS5E6wxCNZUe3Dj7wPKi4oZk4-q8yQfHjsWCtxLhqMqED4Fh8csdpyiUzcEYvY5U2KB2c0Ap8szDdkNC92G6z1T1QJhBYv64cAAfKYmRs6eHdKsFkOZ32TeVlD5gsqHgcyNhHOg7rLKclIMB134YwNQee09PZu7INkWcnYEZNAkguQ7pGaf4Xq1U-Gd1vIGQ-M-lOFAF5T4XNTUcJ58GBYc8N_PocOr0Lo28SZDE3LqLUAt-W275uzBxjFvPXxk9_7Hmi1wlxqIyU5ZTTx9BAVSk7cjLtNj6uDT95VpltSpLpvakxJe1SS8rYWU6AfLjqL11BxW_HdO18g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص‌های سنجش بیماری چاقی
🔹
چاقی از بیماری‌های مزمن و شایع است که علاوه بر تاثیرات فراوان بر زندگی روزمره افراد، باعث افزایش ریسک ابتلا به بیماری‌های قلبی-عروقی، دیابت، کلیوی، کبد چرب و آپنه انسدادی خواب می‌شود. تشخیص و بررسی علل بیماری‌ها، اولین مرحله رفع مشکلات مختلف هستند و بیماری چاقی نیز از این قاعده مستثنی نیست.
🔹
اکنون که با دردسترس قرارگرفتن درمان‌های نوین و موثر مدیریت کاهش وزن و بیماری‌های متابولیک مانند داروی تیرزپاتاید (Tirzepatide) داروسازی دکتر عبیدی با نام تجاری زیکورپا (
®
ZCorpa) و داروی سماگلوتاید (Semaglutide) کوبل دارو با نام تجاری ولوریتا(
®
Velorita) ، مسیر درمان چاقی در ایران هموار و آسان شده است.
برای مطالعه متن کامل این مطلب روی لینک زیر کلیک کنید:
https://abidipharma.com/health-items/obesity-assessment/?utm_source=telegram&utm_medium=post&utm_campaign=pr</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/683134" target="_blank">📅 20:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683133">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
تماس تلفنی وزیران خارجه ایران و عمان درباره اوضاع منطقه و هرمز
خبرگزاری رسمی عمان:
🔹
وزیر خارجه سلطان نشین عمان و همتای ایرانی وی در یک تماس تلفنی آخرین تحولات و شرایط ازسرگیری گفتگو و مذاکرات را بررسی کردند.
🔹
وزیران خارجه دو کشور، اوضاع تنگه هرمز را بررسی و بر ادامه بحث و بررسی‌ها برای رسیدن به تفاهم تاکید کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/683133" target="_blank">📅 20:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683132">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRzdhRhhfNIVYpAsExon_lJyOL7g_sew0z0RD5npoym1rfZJkzBddwzQPAa9i4s8Sr59g6Wr7Qt83vdo2cTirS3kguzhuJxXJu563DoHsAsCP19UYfRch2IGxFOEEp5FCGviBqm-MCEYDgfBLSFrB4YkJUhwSGC5MrznkrrHaP-3Q--fISHUwasI-90K1DJg_Gx4_ZOMMRg7mXNrUVSOP4RJuV_vkWkB_ZgWBgvE-AtO5O921WXaYBED_JmwwbzneiVINjfVZnIKlX5D95PlQTabwqA0XLfBycKTmGYOWCKnwedzDmxNkHL1zjot2_tGrdY043kPSw6OY3pPwruKqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیگه از شر لکه‌های کفش راحت شو
👌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/683132" target="_blank">📅 20:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683131">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpF6doZg2MHT8f3_lEMtehdPssJ6PoyQQg-vqpbMc8npVH5xxzbpNeCPe2V7opQ6lHYHG9gcYqlDxZb_ijWY5u5uBnbsS_d5D71Upwn5WNEtf0AqvKzIl1tbYwEu5hZkuOVFbh9LNrFF7vUwpFlDyPbLiTgspN-pxqz29Vg8kQLuHgAHNXE0Vd-rDqInURstM9tHw6_GQll3EOzwaEQ0qjq9E-ylD2gCw61-FfN7bqeBioeSxesKLbWZZi2jdPlypKeTIA3yD-AipeERnCw41sAx_LWyXSl_rJTfXj8pvijkLvLgVXWuuh04zwBfTtKf5YM4YNscL9j_a5BQEtPX3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا ترامپ واقعاً می‌تواند مانع تجارت کشورهای دیگر با ایران شود؟
الجزیره:
🔹
کارشناسان حقوق بین‌الملل معتقدند که هیچ کشوری نمی‌تواند بدون مجوز شورای امنیت سازمان ملل متحد، یک تحریم همه‌جانبه و کامل را علیه کشور دیگری اعمال و سایرین را به رعایت آن ملزم کند.
🔹
به علاوه تحریم‌های پیشین نتوانسته‌اند جریان تجارت ایران را به طور کامل متوقف کنند.
🔹
کشورهایی نظیر چین، ترکیه، پاکستان و عراق همچنان به مبادلات تجاری و انرژی خود با ایران ادامه می‌دهند و منافع ملی خود را به فشارهای واشنگتن ترجیح می‌دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/683131" target="_blank">📅 19:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683130">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f1a148fb2.mp4?token=BQS9Qd9bStbZ5JULO5dilvwkck7uOEzgV3SIP5JCwuAiyTGqxdHpKsoH3ylkdW8trT4DaIX36lz-JSoGIhE6o1kzBqgkaA-0PQIbJZ62xSyyiG6v1nQyXNA0U764jkLsaz__WWWxZ8B_ICuXl3qevew-xrIJ0GjuC9nV9yDxxsSz7MEax10VOD0Jjm3Mue84z2rlp4hD1qYD0jvUIe17rbOa0ZmG6F440XnU4FDXo_pwojrMpzNbvWuwt3c5UWyGYZi6Az7WDiNQJZDHs3Ki-Ltn70v-SgvQ-qKtiNh1AHAB6vsDfT4huY6NYcZfkf7jho8XwMyv4g3fxoGn_hQC3RkG_ZUutw4WdHUOK9YHT1MCn9Fzg0pN-mXgaEEau6yeucXcqC5mtlq9pr4kkZP_grn3CsSvCmn3OC39bAc_mGfeuQ2t01lVfgybBhhGDxB_aKsormj_8wM2K36oonjmZSfHm3Cx022w-0WaJKcPAJ5rvYgHG5b_hK_Rk72imug6Q5zhf8x4ZAu3qyXb-iHwZ6x6U9R03ATJJZt6fJHgWEl6MrNYmMw_Jhp_3Ieqx9lrHD4PS10AvG7tarUaDejmBnKhziTli6Km5-iIM7znEnTwSFbJc9R5Fhzw9SCD7GxSL8F1dDCjDFl2U06MeFUJZLMn2Mr6W90Q6m6xiUOS5m4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f1a148fb2.mp4?token=BQS9Qd9bStbZ5JULO5dilvwkck7uOEzgV3SIP5JCwuAiyTGqxdHpKsoH3ylkdW8trT4DaIX36lz-JSoGIhE6o1kzBqgkaA-0PQIbJZ62xSyyiG6v1nQyXNA0U764jkLsaz__WWWxZ8B_ICuXl3qevew-xrIJ0GjuC9nV9yDxxsSz7MEax10VOD0Jjm3Mue84z2rlp4hD1qYD0jvUIe17rbOa0ZmG6F440XnU4FDXo_pwojrMpzNbvWuwt3c5UWyGYZi6Az7WDiNQJZDHs3Ki-Ltn70v-SgvQ-qKtiNh1AHAB6vsDfT4huY6NYcZfkf7jho8XwMyv4g3fxoGn_hQC3RkG_ZUutw4WdHUOK9YHT1MCn9Fzg0pN-mXgaEEau6yeucXcqC5mtlq9pr4kkZP_grn3CsSvCmn3OC39bAc_mGfeuQ2t01lVfgybBhhGDxB_aKsormj_8wM2K36oonjmZSfHm3Cx022w-0WaJKcPAJ5rvYgHG5b_hK_Rk72imug6Q5zhf8x4ZAu3qyXb-iHwZ6x6U9R03ATJJZt6fJHgWEl6MrNYmMw_Jhp_3Ieqx9lrHD4PS10AvG7tarUaDejmBnKhziTli6Km5-iIM7znEnTwSFbJc9R5Fhzw9SCD7GxSL8F1dDCjDFl2U06MeFUJZLMn2Mr6W90Q6m6xiUOS5m4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ اگه توی رابطه‌ات با امام زمانت شکست بخوری، کل زندگی‌ات رو باختی!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/683130" target="_blank">📅 19:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683129">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab1e9a0c02.mp4?token=CUvaVl9tXo-fnYUEF7UYPHLMTPkEoYgQyJF90JEuCb9SAtmvPAAQnSvERUvyeL05btotRoY1mr8xbi3QpTWcf8IgSchsM16D27S7Syvp_3CV400cALAuJ0yKrwuIlwd9XTFUYSgM4sUe4GPBFfrunFvZhsYtUHbIyWKBmmh7BouXkNv4jwhedRjdgSD72jhDd5MEzyyQVFNzzkSgiMXH8tunxeLYEGHYHfttTrBS3H62RtikVyVrp71DQoH707dSeZjxRC1clDoSlh2Zs-pdTKIPoeHe9IxL7x7053vT8AZYrU30xBrDictkXrUJQPeK-SxdPEwBkAt8h-Ps1MTFRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab1e9a0c02.mp4?token=CUvaVl9tXo-fnYUEF7UYPHLMTPkEoYgQyJF90JEuCb9SAtmvPAAQnSvERUvyeL05btotRoY1mr8xbi3QpTWcf8IgSchsM16D27S7Syvp_3CV400cALAuJ0yKrwuIlwd9XTFUYSgM4sUe4GPBFfrunFvZhsYtUHbIyWKBmmh7BouXkNv4jwhedRjdgSD72jhDd5MEzyyQVFNzzkSgiMXH8tunxeLYEGHYHfttTrBS3H62RtikVyVrp71DQoH707dSeZjxRC1clDoSlh2Zs-pdTKIPoeHe9IxL7x7053vT8AZYrU30xBrDictkXrUJQPeK-SxdPEwBkAt8h-Ps1MTFRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت سد لتیان
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/683129" target="_blank">📅 19:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683128">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvgaeeiLY25YXrFEPuNKjmz6eiHSfqEOgRCgVJ7JVtJ6s9XHwtq9jv2ejFRrl3NaEndRdoAzFFL9FHNO0Ww7i65oI9yt-ZLKi_mf7ZRMKp5j3yxh3iNsDadRnhyx-Sc_a4jsPbzEqOhn_Fp8_kf2sRrROAwQBbqyYPStY0Jowf9pXn9R9013H1TzmYSfve7iTB4IlnSlYdhdbA4C27A-NNIQpXrqsngvOG44B6lM9LrzsNW8LmxQLoLQ01lOMhEbmej3WhItM4E6WgebqiIacDJqkPyCkLTmgEvBb3yStyCQ4nns_xge2L-sGkyrSNHvwCJesvzjcsNnyPDEtBNXxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسن‌ترین زن جهان ۱۱۷ ساله شد
🔹
اتل کاترهام، زن ۱۱۷ ساله بریتانیایی، بهعنوان مسن‌ترین فرد زنده جهان تولد خود را جشن گرفت. او متولد ۱۹۰۹ است و راز عمر طولانی خود را نگرش مثبت و میانه‌روی می‌داند.
🔹
رکورد مطلق طول عمر با ۱۲۲ سال در اختیار ژان کالمان فرانسوی است که در سال ۱۹۹۷ درگذشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/683128" target="_blank">📅 19:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683127">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qL51HCTBHiisEVn52W95syawoQCcX8D9DbO5F5TIzY2qBI5yhLTCUd1kErZOIfsv_cN8Ms_h6tF3qpD_5Gye3c0N1kZezbbq-VgpMsxo55Jtlua7iUCW4Bc0KimUfBQVTbFNg3IRfbn6HVHAk537HTKbCxFjCMwsCIxRTNfk1XJyv4CxU3uIu98YUyBJyPlWIkLh7ra2bzzs4Rv3no_1vbfJYk28NWFDGMt9DsSqCaYRUGsOpIAWkDDb05GSJ3abMH9M7QmpaB8g5m_-QVNu2rMWK1Wp7HRGpzZz_DrmGTxaJ4qBtgbARk8mCtqHs6F_hGfl8hix2b63PzB0TTeAXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/683127" target="_blank">📅 19:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683124">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bbc1c9f3b.mp4?token=EVA1mV0_Qhx0lIOGM043itdKMqMkPDuWHOwty5NSRvTp9uTD-Zc7LA_uZIJmCWrzvXeW2sg-z0_RC5_OwJ7pk1EK1jsbzF56pXgZBsddhbl1DYiR6KCHb7urlsUjoKn6SEqY9hnsNXiJdMaFbx_M3vR0ENqIZXJTRYyFM_by8WsrSti727mRXTloDmmQDaJVV3dfL-dlII8vFSZPMWTQtfbY1QOeaFFNB1R-o4d2nXwdOKX8wcxlISWYOwBN-ZoD-qxP8htcaR_S1k8Ka9xkr7ZHo6s4ZirDkLu5t4MNYiZSgbeE6onQZifHrULmmqmp4j4Gy5cORqMKNz_AbrQvQ2PaQ552kZ9GFsL4jOZmVuKkDaJK_pRIOr3DkFmcgD-6il-MU85VKSY9_8UxQCwMIKMsiOTgiPuLUL8FotwC0J3-BNBXT8q0oJ93SrIJwRwHpjyXg5KNxN3lJEKRxzJQgnKcxKUrk8O3I0v-FWjDjLCAaXrjXl_FW6x4DpvWBXM0yS07as-NWLN51DIDvLOVSY3g7eAos8okyrEm71bgWkuH_-wPO7D4ffOcWd5czE661m_RNS2dixS4pZFSnYznTX9Vr8-fag_5cQqs-05BIjN5n2vB5-7wRQGkiIjdSkD0n9c0MisTWbnn8Zi-rwUB7GVml3KQkQEYhNHAKB_zrIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bbc1c9f3b.mp4?token=EVA1mV0_Qhx0lIOGM043itdKMqMkPDuWHOwty5NSRvTp9uTD-Zc7LA_uZIJmCWrzvXeW2sg-z0_RC5_OwJ7pk1EK1jsbzF56pXgZBsddhbl1DYiR6KCHb7urlsUjoKn6SEqY9hnsNXiJdMaFbx_M3vR0ENqIZXJTRYyFM_by8WsrSti727mRXTloDmmQDaJVV3dfL-dlII8vFSZPMWTQtfbY1QOeaFFNB1R-o4d2nXwdOKX8wcxlISWYOwBN-ZoD-qxP8htcaR_S1k8Ka9xkr7ZHo6s4ZirDkLu5t4MNYiZSgbeE6onQZifHrULmmqmp4j4Gy5cORqMKNz_AbrQvQ2PaQ552kZ9GFsL4jOZmVuKkDaJK_pRIOr3DkFmcgD-6il-MU85VKSY9_8UxQCwMIKMsiOTgiPuLUL8FotwC0J3-BNBXT8q0oJ93SrIJwRwHpjyXg5KNxN3lJEKRxzJQgnKcxKUrk8O3I0v-FWjDjLCAaXrjXl_FW6x4DpvWBXM0yS07as-NWLN51DIDvLOVSY3g7eAos8okyrEm71bgWkuH_-wPO7D4ffOcWd5czE661m_RNS2dixS4pZFSnYznTX9Vr8-fag_5cQqs-05BIjN5n2vB5-7wRQGkiIjdSkD0n9c0MisTWbnn8Zi-rwUB7GVml3KQkQEYhNHAKB_zrIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از تصادف رانندگی سنگین در نیویورک
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/683124" target="_blank">📅 19:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683122">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
آکسیوس: بازار نفت دیگر مثل گذشته به اظهارات ترامپ درباره ایران واکنش نشان نمی‌دهد و معامله‌گران اکنون بیشتر از مواضع سیاسی، به واقعیت‌های میدانی در تنگه هرمز توجه دارند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/683122" target="_blank">📅 19:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683121">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDeu7S3vynwssCVieU3ledmOdYxbtN0ZCBXhoF6ObVExFml71OfAtoJgwOlFytNc0RFcXXToOBtMnTWm5iCWiGJYSNK1Fg9lcGcndFxQiOSEjf3fkT2qGpJF69_YI_fbaKMAhtX3zc1Varsv3yw4LQA0jft082rnaI8Z2VpRotB2A77dEXem4vXHHVy0TKMf3clh42EnRp08C6_z0kMqLoEa-b8VBHaX1gt4s07j0_Zau-EUPdxTwjjmPePmxVLctpjBGgd5LyyZO5VAA3nadMCmNYv27lcE6JI7ByNhcCtbN8LT4mD3WP5Cwn84H2Jn4j5l8CGxiwu3jEijOG5ojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینترسپت: برکناری‌ها در موساد نشانه شکست از ایران است
🔹
این رسانه آمریکایی با اشاره به برکناری روسای اداره اطلاعات و بخشِ ایرانِ موساد آن را اقدامی بی‌سابقه خواند: آخرین مورد از این نوع برکناری‌ها به دلیل بی‌کفایتی، حدود ۳۰ سال پیش و پس از شکست طرح ترور خالد مشعل رخ داد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/683121" target="_blank">📅 19:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683120">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0140942b56.mp4?token=JBCk8ueXMrk5z8m_MwdaSIjCBZw4eVQfOmV9Gg4o5zzKq7oTLnaje8efjBPsa86HbMmZcbGiJB9hs_cv9om_pK640t4GGu7KCSowu30_ADvW-AbEYPYUozbTCwWIVl62GsUx7dwBOJdGCLjM9yMM2MJ5JHnn6PScN1snGTxYJVqPn6bP2TXKyLL5HQHIoNio7m1aooOZaJs-m6WP0PG-NhIxo-flyw2aJLN3R_jikfOrRD57Kp3XQLQ0BinfPHPky_i73N8H9HW7fVt1GL1fIt3qfJ911niAvZvP5oJA34T97U8vPYslgx2SnrpwWI29Z4R-Ty79qiG58Z4aT73B7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0140942b56.mp4?token=JBCk8ueXMrk5z8m_MwdaSIjCBZw4eVQfOmV9Gg4o5zzKq7oTLnaje8efjBPsa86HbMmZcbGiJB9hs_cv9om_pK640t4GGu7KCSowu30_ADvW-AbEYPYUozbTCwWIVl62GsUx7dwBOJdGCLjM9yMM2MJ5JHnn6PScN1snGTxYJVqPn6bP2TXKyLL5HQHIoNio7m1aooOZaJs-m6WP0PG-NhIxo-flyw2aJLN3R_jikfOrRD57Kp3XQLQ0BinfPHPky_i73N8H9HW7fVt1GL1fIt3qfJ911niAvZvP5oJA34T97U8vPYslgx2SnrpwWI29Z4R-Ty79qiG58Z4aT73B7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جاری شدن سیل در جادهٔ روستای گیفان خراسان‌شمالی
#اخبار_خراسان_شمالی
در فضای مجازی
👇
@akhbarkhorasanshomali</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/683120" target="_blank">📅 19:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683118">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRL4TmyXrKpMzqLcIHgNbzDX72AiWiPN2QCcDtrvt4cHIlC6YYrqAQbdQYD_X9zylmnFsGRfzCRooJI72LnsA4ejTH2bOYnu193etgXEc23ssrZnx1ppoMGVlPGnJN03ubTtt-MwaFepAlEGLWPlxs93aq21UVzMbga3NMoWZwy8WwRjVGP0dKDnnjs7r0mHz1VLwVfgxR72CKpxmxOY0RN5h2THyBS6Fjnz6x8L6bHN8za-XdkbIay6wfrMwD88YO96B_gSHeOZAxRkDiOZyy5EouH9BjyzLLmJpGFWD2069RjKFekKed2zj9yZDIBAdz4pDbm_lEMQAxEnmLaOlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو کودک‌کش: اجازه نمی‌دهیم اردوغانِ دیکتاتور سوریه را اشغال کند
🔹
نتانیاهو با متهم کردن اردوغان به دیکتاتوری، یهودستیزی، کشتار کردها، پناه دادن به حماس، اشغال نیمی از قبرس و زندانی کردن مخالفان، تأکید کرد که اجازه نمی‌دهد او دامنهٔ تجاوزاتش را به سوریه گسترش دهد و اسرائیل چنین کاری را برنمی‌تابد.
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/683118" target="_blank">📅 19:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683117">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/466763a826.mp4?token=WlI8tisPOiEwy5k1xnKXvX_7x-UaflrzqRR0Ea5LHsSmzwSergH5A3LnToX-vrQnBzH9r6e7rq_NsbUxcnRgijYGUCctIITVb-QtErFuuDjWx_ej8iwts574AuS9F6pe57NjvFSfyCE0kyCn-A5FfEI80shrT4zHQ6oRDZ4qVtDoCpPXfycdook2xpayLG0-YgP0XW5RlumW_PCuo6mlymXPJyIB_E8dNHj3ZK0iiFPctOvY5YituXdD8fw5HXyTZ2yrvbae7_x2tEWZqppHvgYuyXMyMmLEURjyp5OfGde_xaXtjrVFZ6RcmanZMSgqh4aawVYPww9LmLVEL_ytuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/466763a826.mp4?token=WlI8tisPOiEwy5k1xnKXvX_7x-UaflrzqRR0Ea5LHsSmzwSergH5A3LnToX-vrQnBzH9r6e7rq_NsbUxcnRgijYGUCctIITVb-QtErFuuDjWx_ej8iwts574AuS9F6pe57NjvFSfyCE0kyCn-A5FfEI80shrT4zHQ6oRDZ4qVtDoCpPXfycdook2xpayLG0-YgP0XW5RlumW_PCuo6mlymXPJyIB_E8dNHj3ZK0iiFPctOvY5YituXdD8fw5HXyTZ2yrvbae7_x2tEWZqppHvgYuyXMyMmLEURjyp5OfGde_xaXtjrVFZ6RcmanZMSgqh4aawVYPww9LmLVEL_ytuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت‌های شما از دلایل تجرد | چرا ازدواج نمی‌کنیم؟
🔹
صداهایی از جنس حقیقت ؛ بازتاب پیام‌های صوتی شما پیرامون موانع اقتصادی، فرهنگی و اجتماعی تشکیل خانواده.
🔸
پیام های صوتی  خود را  به آیدی زیر ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/683117" target="_blank">📅 18:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683116">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/En8B6rwhXf8up_gsuVjomEE3DDLKAWPiO_61ZE1RtRLF04faMQh7hfsSvhJ0a5TIdIKlQOZSvn_SGgRuUDyxbUMbtruzT3qMI6NoApiw-uN_tKZY5PIETzFs2eVqTyjXNRSxnpMIeUjfduKG27igHPx8-FRRAm478b3ZqF4ujAs7sLmc_7XepCGxuTpiLsYtUG_iAM9HL7U0GJCQT2pBS8wa7Iy9AnpbHkKmQkAsTQtjpP9DkhYlmslNwFyFKhXklHgh6mLUhAQdHkd5nvR4PpdZjNmfAAWT3vpVy_ayd-TA-T1DEdCcserKQHix7d1ZT6sQ0zFbQl-dZXBCORFpLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش سید عباس عراقچی وزیر امور خارجه به ادعای کمرشکن‌ترین عملیات اقتصادی تاریخ ؛ این فیلم تکراری نیز محکوم به شکست است
🔹
۱۴سال پیش:
«فلج‌کننده‌ترین تحریم‌های تاریخ.» شکست خورد.
🔹
۸ سال پیش:
«فشار حداکثری.» شکست خورد.
🔹
۵ماه پیش: «تسلیم بی‌قیدوشرط.» شکست خورد.
🔹
امروز:
«کمرشکن‌ترین عملیات اقتصادی تاریخ.» این هم محکوم به شکست است.
🔹
این فیلم را قبلاً دیده‌ایم؛ همان داستان همیشگی، فقط با قلدرهای متفاوت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/683116" target="_blank">📅 18:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683115">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
فرمانده کل ارتش: صنعت دفاعی ایران با خودکفایی و تجهیزات پیشرفته، بازدارندگی را افزایش داد و دشمنان را به تغییر محاسبات و پذیرش تفاهم سیاسی وادار کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/683115" target="_blank">📅 18:49 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683114">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ce969d3d3.mp4?token=c2-ob2svoDN_NvMzoJAzdA7c3BchLYYIHC-srFJHkFO_9a7t16vq-sYqVWIx9m4bP88N5eZj5oyNzaIzaOBbIvitdxEfyovNpkOxPU9W6lzX0BygHA3t1LQmPeYl2-1gbWDppL7fNCN6RPo4EUJ4O7MSLXCuhhbDdi5MzU0PsPJZ7dgU7rHSripaF4Cal_xnq6SnkvWtejo9P9QzAV6f0jIRPZ7NLP80FgW9FshbLECD9eF2cH2J73HISjC-xDizycdH3qnycqvaVUHpqAGtFzDTNPHghds1Uz6FCrDRnnzXZR2HFHl2DAyNntAkuLpCIbMIi7Ce7B87e7dZ3aII3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ce969d3d3.mp4?token=c2-ob2svoDN_NvMzoJAzdA7c3BchLYYIHC-srFJHkFO_9a7t16vq-sYqVWIx9m4bP88N5eZj5oyNzaIzaOBbIvitdxEfyovNpkOxPU9W6lzX0BygHA3t1LQmPeYl2-1gbWDppL7fNCN6RPo4EUJ4O7MSLXCuhhbDdi5MzU0PsPJZ7dgU7rHSripaF4Cal_xnq6SnkvWtejo9P9QzAV6f0jIRPZ7NLP80FgW9FshbLECD9eF2cH2J73HISjC-xDizycdH3qnycqvaVUHpqAGtFzDTNPHghds1Uz6FCrDRnnzXZR2HFHl2DAyNntAkuLpCIbMIi7Ce7B87e7dZ3aII3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: تفاهم‌نامه مفصلی در حوزه امنیتی میان ایران و عراق امضا شد/  ایران هرگز در امور داخلی عراق دخالت نمی‌کند
رئیس مجلس شورای اسلامی:
♦️
عراق در آستانه خروج نهایی نیروهای خارجی و تثبیت حاکمیت مستقل خود است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/683114" target="_blank">📅 18:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683113">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKvTHhfq_hEZbSQXaypUOUGcIKjq7bhBnB_FaPIU0t3NxmS8Cv3Cd7SGyGxPPmgLBALTJZHPKYQAU4xmwHhLH-fnBnVF3Y5hyc2qgzCsdDHE1Gm_O5UO4HNtiu-dV7Mjfwj8I20qAblcna4JuE68l2GaGUJeHXozzU90NEoDv6G8ooqzzQ7DORv81DCmd3zYJ_s0TrvB37FsnNWcmaH9QYOmLlahGo8oyHaDoQAeTqPZaHnAl3LQqalXI9QpFR931qgSjwEQ8LJHywShJOtRMnRcgSFyuZ62sL75YR1IxHzFjroEgkFnMKMVmP6iDZig3InKV7woq0E1riFbfPSQUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده نیروی دریایی ارتش: به‌زودی در پهنه دریا درس تاریخی به دشمن می‌دهیم
دریادار ایرانی:
🔹
شرق تنگه هرمز و دریای عمان تحت کنترل کامل جمهوری اسلامی ایران است و تحرکات دشمنان فرامنطقه‌ای به‌صورت شبانه‌روزی رصد می‌شود.
🔹
نیروهای مسلح تحت فرماندهی کل قوا محکم ایستاده‌اند و به‌زودی درس بزرگ، تاریخی و فراموش‌نشدنی به دشمنان خواهند داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/683113" target="_blank">📅 18:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683112">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhndI4KNUig8X6QMbz2g_QJnv4MISNM4na92MFtKRomC_cRVF6W-jyjFgQA2OcohQtV0WkVX9VcpEQ7y1t9YmI65Sb5s2vakMt2QAOokxUs8yQN_-NTOgrQ5_qApOYbcWgjE2k08tK7ReGcGiTrhQBLDn9eVB4SMmFdqvdEbX8ysVUj9g0nZmnKFIPwvPRNxfB3spNe0Q6kn6T6Ve84M_rofpV6wUSDIxt3rKmlkjbiU7slw3XJz8d5BMfYL99Na8O1MOMkVVG3wa0_oAu3SFz725mipidHn0XujHcVl3EzlFOfYHNRn9rzYBCHyfz-qGgqAHk9hNWgg3TtyISNSEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار مبتلایان به اختلال نقص توجه (ADHD) در ایران و جهان
🔹
بررسی داده‌های سال‌های ۲۰۱۹ تا ۲۰۲۳ نشان می‌دهد شیوع ADHD در ایران از ۱.۸۵ به ۱.۸۸ مورد به ازای هر هزار نفر رسیده است.
🔹
در همین بازه زمانی، میانگین جهانی شیوع این اختلال از ۱.۸ به ۱.۰۹ مورد به ازای هر هزار نفر افزایش یافته است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/683112" target="_blank">📅 18:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683111">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed0ebad46.mp4?token=NmONXdOCFzO-40EBthbIiE5ydPWvihE_7wllDC03qTCQG3s8MfMlQH86qJtIbxfdnXQ_2NNHSEQMqKVXTavN0_v9AftkP7R7RFTcWYh9oK7WggOSnwihqEiI_2eq0cyKkApDYylzWcky-WGFzaQXCzitPMVe_LoyW3Ktpsts5QVJgdxeIIF3ePG0gUUcfV8MPY_KO09bADUjGahtK_hUW81mhJfv0-tCrEzT1_NMZiYEqYZICRZ3rGR24z5gUthD8eVqGQEZ8I9DYOle9qBCEwfB63XIkIxSXRoaoqM7fVF9u6p_lNrX2u3-cps0R3IkA4vkYTW_J7L4YYRHd6vMKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed0ebad46.mp4?token=NmONXdOCFzO-40EBthbIiE5ydPWvihE_7wllDC03qTCQG3s8MfMlQH86qJtIbxfdnXQ_2NNHSEQMqKVXTavN0_v9AftkP7R7RFTcWYh9oK7WggOSnwihqEiI_2eq0cyKkApDYylzWcky-WGFzaQXCzitPMVe_LoyW3Ktpsts5QVJgdxeIIF3ePG0gUUcfV8MPY_KO09bADUjGahtK_hUW81mhJfv0-tCrEzT1_NMZiYEqYZICRZ3rGR24z5gUthD8eVqGQEZ8I9DYOle9qBCEwfB63XIkIxSXRoaoqM7fVF9u6p_lNrX2u3-cps0R3IkA4vkYTW_J7L4YYRHd6vMKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حقشه!
🔹
جمله‌ای که ممکن است روزی علیه خودت شنیده شود؛ حرف تلخ عمو فیتیله‌ای درباره قضاوت آدم‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/683111" target="_blank">📅 18:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683110">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn9biPFFiz8taQHrTP8Cvr7eMEJxblxQwQzejJ1K1H9JQpjWDo5ochhibFFfgSoz_VLEenxlqddBDa-PVF2KJyfqi4EtivMUspvP30bPGIXN-upDHL9T1wtZaS-QAVO-oIJiZFl2kufu2U6vlr8SLm1y8fx5WJ80blMtwg8mdVlVEoCjDbo3chOz0fPGIJpg7jI3XAHaFxjHRiVfd_WGSr0OM4leKt39QiI5PtmlS2IuTra9imWFEbJ9rAvWI4mbBKanJLH22NMLMXI1Tu4s5ZFYG5WMIQxz_R9DFsT7YQbQ9culuFg-ZoQOMXyk3grNm0-qMwBE2UtsqQ3zO-G52g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قهوه‌ای؛ رایج‌ترین رنگ چشم در جهان
👀
🔹
حدود ۷۰ تا ۷۹ درصد مردم جهان چشم‌های قهوه‌ای دارند؛ در مقابل، چشم‌های سبز با حدود ۲ درصد از کمیاب‌ترین رنگ‌های طبیعی چشم محسوب می‌شوند.
🔹
آبی ۸ تا ۱۰٪، فندقی و کهربایی هرکدام حدود ۵٪ و خاکستری حدود ۳٪ از رنگ چشم‌ها را تشکیل می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/683110" target="_blank">📅 18:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683109">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
ادعای سازمان تروریستی سنتکام: ۶۶۰ میلیون بشکه نفت با حمایت ما از تنگه هرمز عبور کرد
سخنگوی سنتکام در گفت‌وگو با سی‌ان‌بی‌سی:
🔹
از اوایل ماه می تاکنون، نیروهای نظامی ایالات متحده به عبور بیش از ۶۶۰ میلیون بشکه نفت خام از تنگه هرمز کمک کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/683109" target="_blank">📅 18:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683106">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RZhnIx9P2h_Glg7kQw-LYqnqKXCcVMN8HECxjhW0XL3Gf99GGHXPRq6vujMFja19Rk3vk5fh0bPqEGhNuhqoy7OLhdMOGykjV1BzuTfJG6ttOyTfnHWYeXmJmFNeOF55IQ22e44WxOcBDRTRKHjRXhvjaO_My9OYHJaqpng5uP5WCfazm7AMHFQqRSyI9cenErN2JG2A87xJPeeuHdUOLNnxaBUjBu7uAivDCr9GQuIKOAk01zaexIXSYxDvv3EBDlpO4k-zm8gI6BDXWQhFWd705zNCHd_M66B2GEw4rb0PI4AcM1lSdbX7zC7ehjV8s1HBQxhD-liP8usF6tP0VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KeqylryXKJX36Gw6KeE_SsI_DFR8XtuJvY8JDt3iQPKZ6nfzgfnAsnmkU5eoitEfAFdwXaM7LA2LMt1kmJ6CbeU4qCWppWBPgA2tFrPVJ7S4M7pcvvDdcK03tUUZXHfxxvSWv_Z67q4jns9ki0ezD9BBg5_DobGlBhDGdT5OUQS762SYWT3qhGWIKNZM5wicRCoOLFrqLKz2iSvJN9fTFtxuTSSgcKOJlWCROyvSDqGHwZIEoVlM_ZAiva9fHG4itydN0nm3-Dd9Hr4JuQXp7Jq1hRdUxYlUpNCPnrcXTZ_7bCEecztCjTgY271GRrfk0j_lNDGpZTkaXlpRCSo68w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YmcUviaeky9X9TmC8JMUxocewnayyLOVof9Vl2JDr7DTJJhOpyv8c8vs3PEBdRXJonT5WgWJTSCe-luVlSu1DP-_f7zjfp6z6XasefRiCrXzSYktX_2YiZU01CPzxDBcya4y7cOVCyKkU2swRF6RntUsFLNci9N9My2BKlMPgaPER4cPV6WAAkgkWbKGWFkvDMHz1Kt7wLd8GNVKvs3G7KWtJSucIQ9iFU-J4mmiXWE1-vFbaLRzW4dmfD71kXDDYcjzQi4UPtdQBNVCFD9Ov7JV0sd2h5Y3ZhhRfuyxmBTTOjLMNrjFHMkNJAwvDp0GLjW0DeIuP6AS1Giw-iJeLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بارسلونا؛ شهری رنگارنگ و تماشایی
🇪🇸
🔹
بارسلونا در اسپانیا با معماری و خیابان‌های رنگارنگش، آن‌قدر زیباست که انگار همیشه یک فیلتر رنگی روی شهر قرار دارد؛ اما این جلوه در واقعیت هم همین‌قدر چشم‌نواز است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/683106" target="_blank">📅 18:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683105">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fbe2dacb5.mp4?token=rXHHKQcUqT9pdx_F86OOzuhnfLWYJkFyyJD6E1ib4CaX_hBj1IRNVChkEeXLhs1DUx8C1Jc4HT7GMF5QVaGplitd9fbWYTuPXDoJ9oxs7JQbE5froBpY9SXhFptCxwxkjzPkfmQ0RrzDj6SHY0mo-U9dGCHLwj-8Y7nXsHNfDN-dN9_htTTGrhZgnOQSKoKPe9OiJFItM9IDidhhczpTgvT_fW0StF05AhYe28C_3fklPBvCgrdmU_LJy38tftQuNTFY2CwL8_ef7OiMalRIh7JNwSQbHJ8hU25FNYQlBxsuFBsbQCpg6jceTy-GkRrP0eRXZLCjXfO2MImmTjdX1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fbe2dacb5.mp4?token=rXHHKQcUqT9pdx_F86OOzuhnfLWYJkFyyJD6E1ib4CaX_hBj1IRNVChkEeXLhs1DUx8C1Jc4HT7GMF5QVaGplitd9fbWYTuPXDoJ9oxs7JQbE5froBpY9SXhFptCxwxkjzPkfmQ0RrzDj6SHY0mo-U9dGCHLwj-8Y7nXsHNfDN-dN9_htTTGrhZgnOQSKoKPe9OiJFItM9IDidhhczpTgvT_fW0StF05AhYe28C_3fklPBvCgrdmU_LJy38tftQuNTFY2CwL8_ef7OiMalRIh7JNwSQbHJ8hU25FNYQlBxsuFBsbQCpg6jceTy-GkRrP0eRXZLCjXfO2MImmTjdX1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله هوایی اوکراین به پالایشگاه نفت روسیه
🔹
پهپادهای اوکراینی به یکی از بزرگترین پالایشگاه‌های نفت روسیه در پرم حمله کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/683105" target="_blank">📅 17:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683104">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/683104" target="_blank">📅 17:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683103">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
مصوبه مجلس: کلیه فعالیت‌ها و ارتباطات افراد با اشخاص خارجی باید در چارچوب قانون جدید صورت پذیرد  مصوبات تازه مجلس:
🔹
هرگونه فعالیت یا ارتباط اشخاص ایرانی یا خارجی که منجر به نقض وحدت ملی و موازین اسلامی شود، ممنوع است.
🔹
هر تبعه ایرانی که اقدام به اخذ هر…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/683103" target="_blank">📅 17:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683102">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffhlS8jAzeiNDVdlXOy6ZSmAwZpyAHSrvRvzCz9YI0wL1tu-7VUMX4NEehmUkxfS8UZ2ypR9E_kpcgJAFJNiHAklYOpogi_OPby38677FsqPIkzkXcRr1mY7maeMxOaSyc7ZRApK9Ul9t_V9djAxTbTWdMcAREGU-EnJCq488uUtEF-8mgMIwgeqZ6pqfBMv930woDX_jWfHlQ9ek02n80gZtxcuSvsl0muzInTW7QiHWiyfwvBywTPG9bBKRjXHPgRwWg8R3qXY4GI-nujboIbY__GpzVA0g9ituyfsI8n6knD40IkDZ2i5FoakZp8koVI8lwU-fOglbnFktt3ZyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
آخرین جزئیات پرونده ۷.۵همتی بانک کشاورزی
⚖️
احقاق حقوق بیت‌المال پس از ۸ سال
🔻
در پی صدور رأی قطعی دادگاه تجدیدنظر استان تهران در پرونده مطالبه خسارت از سعید جابری و محکومیت وی به پرداخت بیش از ۷۵ هزار میلیارد ریال، حقوق شرکت کارگزاری بانک کشاورزی پس از حدود هشت سال رسیدگی قضایی احقاق شد؛ رأیی که بانک کشاورزی آن را جلوه‌ای ارزشمند از استقلال، سلامت و اقتدار دستگاه قضایی در صیانت از حقوق عمومی و بیت‌المال دانست.
🔻
ماجرای این پرونده به سال ۱۳۹۴ بازمی‌گردد...
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/683102" target="_blank">📅 17:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683101">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06dc26b5e1.mp4?token=dkPbt7iBsBaFKcTlP1UHXQPISkmxT7rTq-D4Tx1swDk72yYEaJvfWhfeDWwi8fkqSLl6rs168awvvnEax8WTVaFZJPjMf2RotH7n0666otoYFHlAG2epihuO70fJspQZtwFI25VAcBoQAVdV3tS9-FEVVFR3ERaMj61QHgjUdjybMLvXre5ff4GEPTct3GwHSw4GyjPEDyWQqiF4qZ1i-lMbifkb9CLL9qV7mOIqPNeMvnEHBWU63kR3T_HWDPufKb9NDdrXFqY5fsEfxMen99QOu0MO8GUY23IItRq_dxMd-lbIGlee0V927eZN7RGFHcL5QZvDTTv5RTEZ3WWQ9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06dc26b5e1.mp4?token=dkPbt7iBsBaFKcTlP1UHXQPISkmxT7rTq-D4Tx1swDk72yYEaJvfWhfeDWwi8fkqSLl6rs168awvvnEax8WTVaFZJPjMf2RotH7n0666otoYFHlAG2epihuO70fJspQZtwFI25VAcBoQAVdV3tS9-FEVVFR3ERaMj61QHgjUdjybMLvXre5ff4GEPTct3GwHSw4GyjPEDyWQqiF4qZ1i-lMbifkb9CLL9qV7mOIqPNeMvnEHBWU63kR3T_HWDPufKb9NDdrXFqY5fsEfxMen99QOu0MO8GUY23IItRq_dxMd-lbIGlee0V927eZN7RGFHcL5QZvDTTv5RTEZ3WWQ9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار بیانات رهبر شهید انقلاب در جلسات روضهٔ‌ خصوصی شهادت امام حسن عسکری(ع) در سال‌های ۹۶، ۹۷ و ۱۴۰۲ برای اولین‌بار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/683101" target="_blank">📅 17:44 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683099">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec0b3d8249.mp4?token=YOO-Qwl31_fNRjlwyRdG_i7CBn6pDm9r7dth4QbXYdIuuBUShsADal_ZDWTWOQ0WdaCI19AYeQJU-wHMseyO8MwA3Y2vX74W6-uaGtx16ie4UZyT0J9u_z5ozRaOkcletuzQF3XPJuvIC3QFZnh0RarHRQ9uhgRGTFY-SOgZF16Mm580wL_44tGXqKlVfK1oCR5hjSWKRs97uDG-mrG9o8fkAEYaPRS5PZouomFHIA15YLOLpGeLTCMKz7hfikySIsVxHbhytHzFOrzPczfcAo957Z4eJskIeHyYUVpMqdr_nDVKQJi05nZFmnf2dcmJVRcyS2QuOy9bNbr7WgUZbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec0b3d8249.mp4?token=YOO-Qwl31_fNRjlwyRdG_i7CBn6pDm9r7dth4QbXYdIuuBUShsADal_ZDWTWOQ0WdaCI19AYeQJU-wHMseyO8MwA3Y2vX74W6-uaGtx16ie4UZyT0J9u_z5ozRaOkcletuzQF3XPJuvIC3QFZnh0RarHRQ9uhgRGTFY-SOgZF16Mm580wL_44tGXqKlVfK1oCR5hjSWKRs97uDG-mrG9o8fkAEYaPRS5PZouomFHIA15YLOLpGeLTCMKz7hfikySIsVxHbhytHzFOrzPczfcAo957Z4eJskIeHyYUVpMqdr_nDVKQJi05nZFmnf2dcmJVRcyS2QuOy9bNbr7WgUZbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
الفت‌نسب رییس اتحادیه کسب و کارهای مجازی: خیال مردم از پلتفرم‌های بزرگ طلا آسوده باشد، نهادهای بزرگ نظارتی این پلتفرم‌ها را کنترل می‌کنند/ برخلاف بازار آفلاین و سنتی تاکنون یک شکایت برای تحویل طلای تقلبی در پلتفرم‌های طلا نداشتیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/683099" target="_blank">📅 17:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683097">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی بریتانیا: میزان عبور و مرور از تنگه هرمز حدود ۹۰ درصد کمتر از سطوح پیش از درگیری است
🔹
مسیر عمانی در تنگه هرمز پرخطرترین گذرگاه است و از ابتدای سال جاری تا ۶ اوت، ۷۴ حادثه گزارش شده.
🔹
کشتی‌ها به دلیل حملات و نگرانی‌های امنیتی مستمر، بیش از پیش به مسیر شمالی در تنگه هرمز روی می‌آورند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/683097" target="_blank">📅 17:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683096">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرمانده نیروی دریایی ارتش: دشمن اجازه نزدیک شدن به خاک ایران را ندارد
🔹
فعالیت فرودگاه بن‌گوریون برای روز دوم بدلیل اعتصاب کارکنان مختل شد.
🔹
قیمت هر هزار مترمکعب گاز در بازار اروپا برای نخستین بار از آغاز جنگ تاکنون، از مرز ۸۰۰ دلار عبور کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/683096" target="_blank">📅 17:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683095">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee96d3b3c.mp4?token=fowNsyg2gORorEoKhXrVXTGw0yKR6f9TyRyhGiPW2ZC1XR_ybkWdA4L677PZkMhvxgfeRxQfY3OPusRAxJxRYVjo_-GuIFx8AZhjpsx43PHtWNYj3pxoQHIq8OzeFZQDfLFTRdH5O8VeaE5jn_i1LHZPkNN9GiffY9Bcvb-Qr87d0odcEc6_u4cCm3Yga_lBpjBtmb7262ZzaaNrhTXF6vMMRfLTJGVBtHDsAoMKkO6M1GBNHvIOndCuPQDPcLY7Z1mCqbwNGP8WLO5fTRBFqC_6enoX9Vm9w5Dz8bzasjmkH1TZrP_AdMqTX61Nk2qtyRcHl_AKIsdjjHwPnDXINg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee96d3b3c.mp4?token=fowNsyg2gORorEoKhXrVXTGw0yKR6f9TyRyhGiPW2ZC1XR_ybkWdA4L677PZkMhvxgfeRxQfY3OPusRAxJxRYVjo_-GuIFx8AZhjpsx43PHtWNYj3pxoQHIq8OzeFZQDfLFTRdH5O8VeaE5jn_i1LHZPkNN9GiffY9Bcvb-Qr87d0odcEc6_u4cCm3Yga_lBpjBtmb7262ZzaaNrhTXF6vMMRfLTJGVBtHDsAoMKkO6M1GBNHvIOndCuPQDPcLY7Z1mCqbwNGP8WLO5fTRBFqC_6enoX9Vm9w5Dz8bzasjmkH1TZrP_AdMqTX61Nk2qtyRcHl_AKIsdjjHwPnDXINg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای که گفته می‌شود مرتبط با آسیب‌های وارده به پالایشگاه نفت جازان عربستان سعودی پس از حمله پهپادی یمن در ۱۸ اوت است
🔹
یک مخزن بزرگ ذخیره نفت هدف قرار گرفته و دچار آتش‌سوزی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/683095" target="_blank">📅 17:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683094">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDd7ozM2DTBaRX2puQNoctWExhYoAmaI4qxuesof4lFC9d8_UW2Lpb8qkeO5VBIZ1rTZh1KRhRt-L-hzSh_7rzBori84PynSMcrXdJCtv2IGO5qwujFnAR6HufSi6lhlk6D3-Es901GHQP23GKDrqbyElUFcWRMwITPc3lU1mCtnlQMM8VnYMRvFw1cvYwNcNwR5E0Awu3A_79j1H_Cu45yy5jwW4F1bE_f_Qdq4UUBX4jeiqWIlHkDW5pq0kcqUgL2NEVYZmpgQ6P5526py33jrKJKz9WDUmVHQ0Z1ILEYbo1P_h2Ls0a7hi-TFjL-lnFdRwPb6k_ZHDlGzPgD4ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌼
بیعتی دوباره با صاحبِ زمان ( عج)
💚
به مناسبت سالروز آغاز امامت حضرت ولی‌عصر (عج)، در اجتماع بزرگ «مراسم تجدید بیعت با امام زمان (عج) و رهبر معظم انقلاب اسلامی»
▫️
با کلام
: حجت‌الاسلام و المسلمین حیدری کاشانی و علی‌اکبر رائفی‌پور
▫️
با شعر خوانی
: احمد بابایی
▫️
با حضور
:  سرکار خانم الهام چرخنده
و حسین حقیقی
▫️
با اجرای
: امیر مهدی باقری
📍
وعده ما: شنبه ۳۱ مردادماه، ساعت ۲۰
میدان شهدا، مشهد مقدس
🤍
بیایید در این شب عهد و انتظار، دست در دست هم، بیعتی دوباره با امام زمان (عج) کنیم...
@Heyate_gharar</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/683094" target="_blank">📅 17:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683093">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14bee6ddb.mp4?token=skfxXGyP5wBh-PNwCycsxKvjA6lZZs4zy26wuorodkgMBaoV_LjsVNuYuLPOtlmAGKY_drrSHFu_tuiNCjLg2VBRmEtVE8txkqAXtBVf5AVq7jdjd3MEXqEHO0t5PGbK4SzLuV3jJy8EK3WpnDMo7vdxuaB3Dhw7fDwPurMutzlJZWgq61nLqT9Qm6aZAPigZUcxpp5O18cWFcU5V0x2UgyD2E7u9w06E1DhmVuQSd_rPnZnkun5GJ4Ebkps4v5I-6OWW0MjidtnP_jZedb8TAaYvq23MdDL6Wp7AeCcRi010wBRdcEsidjT2TcU-zQwhaZ90sp_OmWXPgo4A7jWNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14bee6ddb.mp4?token=skfxXGyP5wBh-PNwCycsxKvjA6lZZs4zy26wuorodkgMBaoV_LjsVNuYuLPOtlmAGKY_drrSHFu_tuiNCjLg2VBRmEtVE8txkqAXtBVf5AVq7jdjd3MEXqEHO0t5PGbK4SzLuV3jJy8EK3WpnDMo7vdxuaB3Dhw7fDwPurMutzlJZWgq61nLqT9Qm6aZAPigZUcxpp5O18cWFcU5V0x2UgyD2E7u9w06E1DhmVuQSd_rPnZnkun5GJ4Ebkps4v5I-6OWW0MjidtnP_jZedb8TAaYvq23MdDL6Wp7AeCcRi010wBRdcEsidjT2TcU-zQwhaZ90sp_OmWXPgo4A7jWNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردبیر ساندی تایمز: ایران حتی راه فرار آبرومندانه هم به آمریکا نمی‌دهد و سطح مطالبات را بالاتر برده است
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/683093" target="_blank">📅 17:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683092">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Srgh3Q5HO444lZYvo7NJA5i0ax-m17yHN4vKomqxSAmHx2PeX74bJY8vCmYJCHPuE5YOIe6zZi_jZOmXsFOWpgx4GHm66FxIamcbyVPWdSXAN4P6DON4BGbSh6uLgzVOywJ-g29SnpQq1pAxtEsszEx1HzGe3nbqDHYXDOFJi0XrQx3ByXVyQc5FhFcItfSYx-Mtgo69oWAwE53sC5DHIdvwdsqmCFuWd7X4TWqgcAvAGo_UqopSecU-0JZAf3MbGvgmKQFAUpIQN5pbBcxRlALNMP3tzp7Zuk3nyLwBY9hQWnMUgLdY9ZA1y9kCgTSbtGgSA3lUQjbWDa-Tvlh75Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری بی‌نظیر از یوز ایرانی در خراسان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/683092" target="_blank">📅 17:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683088">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/169c3f70d5.mp4?token=STlXg9MRl8GY6F35kARJvYmVuiBv4LwZdL5nUcfZZqZ7xcWNuGD8E7Jq-ZV7ECIKP4riJAcV0PISM-Oa0u8fTFmPV-ylGG5W2XwVZpUPAiIZZQAUqN-jSRFWXaWsEltjVFeZ8D_nmYhkiueonnnpjZLP-CVQM8n8ocJXqIOjjQqL2QsCyg42PInBWUd_wqv1TIlUcOYzoyNTzqFRJrTFNRhPxywWaoXs27U2MJMXzKs9MAZPk2a3NqW2fUeUsApvS3DCi9WlhQnQyCidLcmxMaZbz59h8pj8QjoAYA8kVPANFCFJrLIKyRGLnEVLHVmogXa634ks5Jz1KJq3ZlpFYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/169c3f70d5.mp4?token=STlXg9MRl8GY6F35kARJvYmVuiBv4LwZdL5nUcfZZqZ7xcWNuGD8E7Jq-ZV7ECIKP4riJAcV0PISM-Oa0u8fTFmPV-ylGG5W2XwVZpUPAiIZZQAUqN-jSRFWXaWsEltjVFeZ8D_nmYhkiueonnnpjZLP-CVQM8n8ocJXqIOjjQqL2QsCyg42PInBWUd_wqv1TIlUcOYzoyNTzqFRJrTFNRhPxywWaoXs27U2MJMXzKs9MAZPk2a3NqW2fUeUsApvS3DCi9WlhQnQyCidLcmxMaZbz59h8pj8QjoAYA8kVPANFCFJrLIKyRGLnEVLHVmogXa634ks5Jz1KJq3ZlpFYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای خالی فروشی پلتفرم طلا چه بود؟
خالقی معاون پلیس فتا:
🔹
صحبت‌های من در مورد پلتفرم‌های طلا ناقص در رسانه‌ها منعکس شد. پلتفرمی که ۲۰۰ هزارکاربر داشت به مردم خالی فروشی نکرده بود و به میزان طلاهای فروخته شده نزد بانک کارگشایی طلای ذخیره شده داشت.
🔹
مشکل تعهد این پلتفرم به شبکه همکارانش در بازار سنتی بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/683088" target="_blank">📅 16:49 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683076">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AiYajdd_JNpPUJFnfkyBTXseKIqTbTRBDe65hrBAAsU-xzjSqq6402sTFt0vPXL5SXB35Pm5UjAPn37wFHMrsNQdvwD93ImqIb5eYx1XCwiQ406Ysujp2Hbl6ujv73BP3i4OVvCUIRPorOKTp5G4jO6JnnvyhUKIzQn2q99QaYlkq0BuEQJBD1D30l54aJ5Ouz6bTBF8ac5MZlFL3CKFxmtBI8E7PRrKQWavKhQqjV1syS9KyRO5R4IKRmeSeJ5p3CilHtIBbZ2g4sMSjBuP0xFOH7vqPvtxAR3is0hMqC8jyaYdtKnhdLjZbJCaNNu8rWfi0yPtICVxF9s2k_qqAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oC_DaWYIWEi6tj3xr_SREQAiTJAbpSVmJggeNHRHWtNOYW7MOLhE8X2yOcnzUIeEH2yb0SyrZ6DThlw4kL3-TG7uxf3LG5TRV_AG1qa2CajxKsVjtRG2hrITLcgTBP9tunpad4R38ez4LPTndxE3ZG8RIbZbvXUAdV9bYZJDC9d1HqIpw4yoDMwC0NxS9onlPy3I7zQquAXRYML_C5c3f8Q0qiiJ_u1RLLkC3BFH2La3Ino1LyEo6_yTTfdiWxfXsletCZfngBLwOSlz5AJYxnugVHxzPQ3FHDNvOMDgPTlBjWmt-rtlcHuUPdj_oR0GE1BrHTDm_3sY4owJK74IwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBRK5Ow0VxuAowFE5HmSNpGQcUQVX04hfadeh039pPwqCR1yqpZuQDXUKMPJMA7P8RdI2OE3_BdGTXAn__QTM_FRuSyDGvlZEH_CI092AXVlOiE89FZEISulGK3EKjYa3t2ENLVUFwlerS8O86tf2tccocFQuWAeYuD3zDyZFzlNUgjadUXuhrh9ehQBD48AlkeqzLbI88n03jWPemkmmw45u8J6TTdsUGXYVcfTx-C_WOdX9I8LgqYSrKtzUxYjbT_08pIOrpYn3l61lqteNXKHuwre0pcsB3fdGSSESV5Y189WVbxQ3qwJuqtQbjGT2H4W-sKcPs7Spain8XF7Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nixVxYqkIL_07cXllQ-Y6pfePwWQAWHWSoJscu3DzE7ZZCrMbVdzphXWuj496rW2lVfvmQmCjYxjZLYeZYtUzdJJqDf40uBcIvjOOsrStOpoGrkmYtwINmmrRpEIkrHyeRj-8QgrgHOraKOHscRPymg7-T-1ul14-YirGXyB5Db9ycsGUrERkEwcoclnZT1XheDWD1se12K_mJDM5Z7uo6E6uQbmOF2ek0QXzQx3CjRAUh2jJTPi0T0YdTVEw3_5_pJoEn3u6acgd8KbdI9khLcPrrBHh5XEHLzo_M95MP-8VWKqkVcDnz1GgwI-yVKmo6UPN7PCEFfToBwlPiMnHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gV1rI3sgQ2eldB1XagNFdYLuWT1pusZwUoD3hbZgJbfnqDWjjiaUkTcQolIkRN34Ig0NmblTVHlgb-Jz_EpZHH9MWciV0-MowMdG1OmEpL-ic9Lcsi1fy24C1Gz-IfynjrK7S9EX_4vlcBftH2DkyMakQ6KUzY0aSnVyG-xmuvjCp-bVImFuILZuostJesecjiMSOvkNUZLKNS99kaWLx-1db3l7kvUQKmoooDa1lbzJUsyLTwNuYJJUnLWSieVe4gX_zhB1_GAO1HCdb0iZvCTzM4hhKLp7HtUSYD7tPfYEMIrIUiRxn051W4c7QdJeBt-FY9AqI5auFGQiUK0JvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bm6giIlIkXeVH2251isyrLJAAq4VrHnQozDx-NtGeQOXTAk2ET7z1YqaahhPT2gk6RXJN2f4aiCN3ItZFS8lfpv4BoQglGv7HRm03Phdie5BHHgjWGxaJnvmiC-paMa67kWSQLbA4P1SzLHkjHkFrSUHwL7oz8EWy1sbu8eSsShWYsNVgqoWHhLSTW0gkjU4tNjV1JirvET26Fo6RhHboPCralKFCTCZI2S5V2Owf5OPad6Mtrv_HIo5X9cCjkabEg8nK3EamkJiqRC5wRNVMIGQV1iUbn5wd0iMo9MKViyepzY7uI7TpF6JQDhIFl8N3aL76_vg08NIBPouCGwxzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/svSCqQp72NrKIi7j6ss8Ha9LzauLR2xe7aMM6O73bh_TalTzYgkcut28lmzppVUgBfuBjXq0WbJd8xreXhCKwcosU6C-y7Iz__fBLUrtSCAe3Y5DKRMd0SQ34KTBNsQq9Mo0-MLCy1c9STkeNcOmpzOb2g57xOxxiqVUQH8qeHZzLSuRxV1mT9gjmMisYTOF5ny0ZfmbONK75Oy59rxPyl5WENyIzZ7pMr5xhs7Slr0i7DD2Ciz1FytFNcWPcGixkYKm8QLRuI8dGh5_2zVcH2rnoaK0sfHZwjA_Y2clXnhpLDY32fsFEwSSHhdInC7Fu5nAVzHQ6S5XKk_JrqbS3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBLy1NPjtKM62NTmS-E_N5X3QTOClts6Lnxs-fMIZJV8Y6wuvZJUnKhQh7sS-Sid_x7OgPYpRsI-1jXNNS9dTNLk9t8njZNso4ILARehIYbAOYKnPzvTLP48eV_FwSB_0SZ4X_c6tg-X-6NyYQHeMLkAJamjgwdhPkADeWLxCvLEF_SJBfH9ZsQRMkHRKafy-h5FsnBdvJMLrOgx_2tjUbHlmiM4fScHphpsXYpVVC5iwi26wTQGA8CPEcSacwaCBtZ6Po7mzONKNVxzXdM4qOVTEQF0ziH2-CHbYDIzAHDl8CmXBhDNTEWjP-0NzVyqShliN0tQtATEi6O7XhmLYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0dLQd2tWdO9k4LNdugG5s2ANc7C7ZJ1_EQsjA-Rb3SM_JNrFpkbpM1M1TgoijI_95nnQPU2Y9hwqYuNzf56AYWdTBiQXzrteqe1pPtK7Sr2YzPeKeGFUAW2Ibi9kY7lnEnwMv23s8MPXwySCZH1qSRJy9Eju-3zlWWdT2s_MGtkOSKEZyVmijrA0kwbznXhsCujLUznm8snwYApG8oE1luWaWa44-SoifY0dUrBsPTZjbiRvftSTO2pWuY0YxMSsGujbIEFC7XfmrHJLVq5ZPdlm15AUt_y0GbWB68WLMPhAUW9tWBcjZxdBxiF2Prk7CER-7Cp8r9Vys5mxrjVoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Po_ZyPkytzQvC8qjn26BhuXDE-CwSLfh_LmGZHMPIz5BUYlzI8ZtxVrDnjcQLt-lKGPlxwdc6-We8vZbbX412LJY3xXeIxxuoIxn1tgvhfmQahNVEk5qxFqMYLTRWy7febmVdmzzyW7qi7lXZYevf3D-NjqyDCqaJ9xPHdGdjZ3b0DdbcATVpocj1ruKm2fXpbLoQ_cgMday6G18xR6Q2jhvWF9aL51Vffn2tiEGPozY2XdJ3OQRB9jXZvGyZWZybR3awqEr5Wdi1jmRJPR9x4yEju2gUpWKS3Agm_CHTz3RYhtKfKsNVRDkLNP2C3uK4BvLoupxGuj6znLgVqIyog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نیروهای مسلح یمن: حمله پهپادی به مواضع نیروهای سعودی
🔹
نیروهای مسلح یمن تصاویری از هدف قرار دادن تجمعات و تجهیزات متعلق به نیروهای سعودی با پهپاد «رجوم» در مأرب و ساحل غربی منتشر کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/683076" target="_blank">📅 16:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683071">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/axA04BHLYexMTejd4dTGrJn4sPWnssnSWv4AVkxHpWInf1ckC8aDPNsitpPuezKEwiTzf76ys_TAo_LOlBRW4RyS1e2ZsGrB_BI-xhohrEv1mfpLCk5VuOJl4G2ExL3lS_tOnS0w6lHS5_VLVybK7_2HEcOumhp3wX2XLyFRQ7KLPEeZPptfj5YIT-ePiRqXyBbR6K4gUVbv9gZAvcQrNfhx5KbhSEfC4DE74t-nTyY1ER82QKgGC1_Bjz1Dlp02iDFcX-oXhPABSMuK2yuXbcJIzg5bsqQ4punKRZIqncHdmM7wDE7QNU3zbyebk6oR1odqk8siEcyoV3ZGfpcODQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GuuO1ftqxVIdHuEvio-R8aQlAV4yXiiMe6KFDzU4izIT-zs2zfvumIAScwfW54zk3fHqgWf_wH50VlyoBIovWKKmmjJsaz2Xbo8wc0YUGiUXCdq-TKQ6JO1TqzEJ48zgD3tQ2C4oJ558Ih-d5IGBV2UJz15ENAgK7J5Kv2yf2GXmems2W8UfbLOdftSQVIH-0Zb0VbLC43t_kg4YYivtmidVzafJFuBNTrWyy6sjpIlrVeGu6kAW49U2qkb8EoW9g7MPImdjpI-_UEQmKAKzDUOHr7-YAHtxsPfTvD1FaeX9CZHaKY0r8A4BaiCbIy3QOHOhX1osnsDeFspisdaTOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJ_xlJuDtmWfr2AavIBMFEEzRBilROU14V8aesozlLUZjJhxdIFJVwIOdtH3AkL-wMiBm9ms0rOVexnlpe_ZjrU1a8yjDEqId3CWNBkFVhSF6jmWtzwOOsXkXlfg7hDyoXlhUGfNB3cPR2zLfRPsgA72QY5HyzoEdYbY7Ti4pdVyGCW7vQ_09LiZjbqR6ed_OK9xKrAOVcLekmLP4PkY21ykof13sN9qzVZYbsOhVbD86OXTe1VVItEIJd45jx9J5CxM_vh75JHJCesTEO63aMHd-XtSoW3RIiAvcr63Py39ayLA10NGpkIXz6QV0s7C-VRaMoeCPRBestfqu1Xj1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BI4pAjkOb9SBNHmy1lsb_qAwx0s-WzN06JUUZTlHGQb_7TMBL7k8Yf3x-9vFgAFp3sMOFiTd9WpWW95mi3ve9N2rGdZ62rJB8NSbid6zP9Og1y9iE7UwyAtCmlLDzkW3Bn5MUNzWtQ8lzaDzoZP_dSUMujIsBlRTFGoHBpB3vr8F8G4pOubyu9VO3Sd47XOromoMANa3nTA3a_T5UxSkij3cbhkFsA6365B5vHJiWjSPXHJQGqSpdtndTliwJT183W1BilkC90Q1OSRNlvbRzaSFUXypDjCFCPeliFK2FU5YOgq7jTBRoSwWFiqMKFk4xwNCNIS0UNj0EZpZApYdXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
صندل عجیب شنل در فرش قرمز جنجال‌ساز شد
🔹
مارگارت کوالی در مراسم فیلم «The Dog Stars» در لندن، لباس مشکی ساده‌ای را با صندل‌های «Barefoot Sandals» از شنل ترکیب کرد؛ کفش‌هایی با طراحی متفاوت که ظاهر پا را شبیه حالت پابرهنه نشان می‌دهند.
🔹
انتخاب غیرمعمول کوالی توجه‌ها را به خود جلب کرد و بار دیگر بحث درباره مرز میان جسارت و انتخاب‌های عجیب در دنیای مد را داغ کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/683071" target="_blank">📅 16:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683070">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7e5c725d4.mp4?token=TD3vNKByoGNl92cgyUA09ES5b5eJzfFXAy10u-T_F92m7UzZW_KJZxrL6FOEwvQhChAP3jUl1ZmLlv8bwWyFMNShL3OxlZV_6AXI941exCfM7zn8GrIQfBdoHZNoXKFxccdfzRV4xky83a1tswJ9yihr6A45F1BkayQP75wfMip59QcR37wFIGz5sD_SIWEbmIuv1fG3Zh2lthmlxZREqtCKmNVkQaoUKQ1AWmkedUyT3AY-9zjZOZTE_8-etOF29hB-8_JhLPwTcm4nT1XmbZIzIVLVtOHQON6n-g1D3qPQN7RjowTnKmLenJV9Ft_1mfpdtXlZCe8TZtu8FKMIOiZAZSfcQ5sU369Nqnn9uI_ZyRY2X4eKc4fPu_Jvtc1xI88h98Wt1iZbBgdTuWWKqZ4dwxoRd1MfJE5F61JZUPzRUOQLC2i4O5LRX-50E-vA_1m9NUAh5qP76A5yDS4nJkBiyP26XeMtXf1edcBizAupyGd60J1BIc1ZH0YPd7-puomX_1SA68hw4t3aqu1upFJzE_0C-6BwDU8wx4LS-J3bpIXXTjePxtgmLu4p2aM4NTjb6JmPnAW_k9SfxZC0fU0foDmD3m5ZFqb_bDxcWg2wjqqd4e2eowQAdetruKTVsp4vZ0dcLKXemY3wTn5MNk6XRcPwkUJkaoNOFKGt4LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7e5c725d4.mp4?token=TD3vNKByoGNl92cgyUA09ES5b5eJzfFXAy10u-T_F92m7UzZW_KJZxrL6FOEwvQhChAP3jUl1ZmLlv8bwWyFMNShL3OxlZV_6AXI941exCfM7zn8GrIQfBdoHZNoXKFxccdfzRV4xky83a1tswJ9yihr6A45F1BkayQP75wfMip59QcR37wFIGz5sD_SIWEbmIuv1fG3Zh2lthmlxZREqtCKmNVkQaoUKQ1AWmkedUyT3AY-9zjZOZTE_8-etOF29hB-8_JhLPwTcm4nT1XmbZIzIVLVtOHQON6n-g1D3qPQN7RjowTnKmLenJV9Ft_1mfpdtXlZCe8TZtu8FKMIOiZAZSfcQ5sU369Nqnn9uI_ZyRY2X4eKc4fPu_Jvtc1xI88h98Wt1iZbBgdTuWWKqZ4dwxoRd1MfJE5F61JZUPzRUOQLC2i4O5LRX-50E-vA_1m9NUAh5qP76A5yDS4nJkBiyP26XeMtXf1edcBizAupyGd60J1BIc1ZH0YPd7-puomX_1SA68hw4t3aqu1upFJzE_0C-6BwDU8wx4LS-J3bpIXXTjePxtgmLu4p2aM4NTjb6JmPnAW_k9SfxZC0fU0foDmD3m5ZFqb_bDxcWg2wjqqd4e2eowQAdetruKTVsp4vZ0dcLKXemY3wTn5MNk6XRcPwkUJkaoNOFKGt4LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«موج‌سازی مجازی» یا عملیات فریب؟
🔹
در روزهای اخیر، برخی جریان‌های ضدانقلاب با فراخوان‌های به‌اصطلاح اجتماعی و خاکستری، تلاش کرده‌اند موج‌هایی را در فضای مجازی ایجاد کنند؛ فراخوان‌هایی که در میدان، مابه‌ازای قابل‌توجهی نداشته‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/683070" target="_blank">📅 16:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683066">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elyrk9VlE8HrSEbIDlUkMPw3pM3Y9FDzBNgBkCXzHe048i6W6m8wqTpYTrnXu2wX3VqnrkrYYL4LlUKxOc1WK5RF_MW5LVwkHCOkD0aEpw6_9wE_iPD3H8hZTQZSSE20ysDwGgUp8jDyZQNhmUwgdO2TM1o5cBmIQ3ypDbbaDyA6Epq4IcH_ayRz_i5TVmsx3uphhU9y1HDzzvzgXubgj_TQ2uXA-9j3OPtONTmNwR-ZvYkMPR4UTSdoPT_Ag2q_rafWYn1kS3GjLI6mBBrRkpG1l4LwGKqV22QI0azcCen27x0Py6DogbYA6uUDBPXuf3zp4B76-Yps9Q2eZZuhsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ممنوعیت واردات لوازم خانگی؛ ممنوعیت قانونی واردات، مسیر قاچاق کالا را هموار کرد
🔹
هاشمی نخل‌ابراهیمی، نماینده مردم هرمزگان: پیگیر رفع ممنوعیت واردات لوازم خانگی از مسیر ته‌لنجی و کولبری هستیم
🔹
سید عبدالکریم هاشمی نخل‌ابراهیمی، نماینده مردم هرمزگان و عضو هیئت‌رئیسه کمیسیون برنامه و بودجه مجلس، با انتقاد از تداوم ممنوعیت واردات چهار قلم لوازم خانگی، این سیاست را عامل افزایش قیمت‌ها، تقویت قاچاق، کاهش درآمدهای گمرکی و فشار بیشتر بر معیشت مردم دانست و گفت:
🔹
ممنوعیت قانونی واردات، مسیر قاچاق کالا را هموار کرد و سود آن به جیب قاچاقچیان رفت. تداوم ممنوعیت واردات نه‌تنها به هدف حمایت از تولید داخلی نرسیده، بلکه موجب افزایش قیمت‌ها، تقویت قاچاق و کاهش درآمدهای گمرکی دولت شده است.
🔹
اگر بخشی از واردات لوازم خانگی از مسیر قانونی مجاز شود، مبادلات رسمی مرزی می‌تواند جایگزین قاچاق شود و دولت نیز از محل تعرفه‌ها و حقوق گمرکی به درآمدهای پایدار دست پیدا کند.
🔹
پیگیر هستیم بخشی از نیاز جامعه از طریق ملوانی، ته‌لنجی، کولبری و مبادلات رسمی مرزی تأمین شود؛ اقدامی که هم به معیشت مردم و اشتغال مناطق جنوبی و مرزی کمک می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/683066" target="_blank">📅 15:49 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683063">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
استفاده از متانول در بنزین تولیدی ستاره خلیج فارس تایید شد؛ احتمال افزایش خوردگی در برخی قطعات خودروها
🔹
مدیرعامل شرکت نفت ستاره خلیج فارس استفاده از متانول در ترکیب بنزین این پالایشگاه را تایید کرد.
🔹
انجمن خودروسازان ایران پیش از این در نامه‌ای هشدار داده بود که استفاده از متانول در بنزین سیستم سوخت رسانی، باک، فیلتر و پمپ بنزین، لوله های فلزی، واشرها و قطعات پلاستیکی را دچار خوردگی شدید می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/683063" target="_blank">📅 15:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683062">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPM-nya2Bmw6ocNcRGMGW4JNvkLYw680OcN4_gpbNvMGSWl8O0t2is3K8uQYHIE40G0dGZEDv4WC7tbXi1KBTTJFjhVxfEYC29GYsQL-a_Wt3fFY8bXBJ7S1xL9iG3X5mgCDKbies3LR3cDtQOIp6wf6MMqzy1vuA6dxlG2mbewV_2ojpprq6boQnJsJCIP-dmvi5O1WEDqNlC65LuEOCWq4r-i06g4zxfKqqHuf3TrVjeQnPfgMH6cHlklPqXB_9kgSauUqWBy8HAT_HF8pSMja2ekmYU1jMfVblcRh26XpXrV8ucdgDJvsPkFX18R5DYc8OpS3PVcWJEHwx8UwHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت ملانیا پس از غیبت مرموز یکماهه | مقامات امنیتی: او ترسیده بود
🔹
ملانیا ترامپ، روز پنجشنبه پس از بیش از یک ماه دوری از صحنه‌های عمومی، با جمله‌ای شوخ‌طبعانه در باغ رز کاخ سفید ظاهر شد و به گمانه‌زنی‌ها درباره غیبتش واکنش نشان داد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3239331</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/683062" target="_blank">📅 15:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683061">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae1568e3bc.mp4?token=hIYw1GpJrrQh6pzMSGiDzp44P9lusRkH36m1vgoH3naETQJmh2gAgUwmQmGBjnlU435pfxnm6yDIQ7E4t2SIL2OLAGLWn66JWFeWG8srDmyzKarIo-zx7OCLj0qjRSFBSRyWNN9SXFsYtOREuXutI16bH_OdD0v9Et6gEaqI9peN8aCcnE-DdWU0zsTZMn7fs5pBmYQ7rUqlifJXLG4uLl18SXFzKdp2W57m1LiJaaB0iWIrsfh9OX1Q4EpLr7k5EjOI6Q9gRr5VU_vB0C_B-3pDMW4cXD37bIqDvVRm1gLAGZQajkZIA46XA9oKntWymR7Wb6447Zv4NxK1OeeVUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae1568e3bc.mp4?token=hIYw1GpJrrQh6pzMSGiDzp44P9lusRkH36m1vgoH3naETQJmh2gAgUwmQmGBjnlU435pfxnm6yDIQ7E4t2SIL2OLAGLWn66JWFeWG8srDmyzKarIo-zx7OCLj0qjRSFBSRyWNN9SXFsYtOREuXutI16bH_OdD0v9Et6gEaqI9peN8aCcnE-DdWU0zsTZMn7fs5pBmYQ7rUqlifJXLG4uLl18SXFzKdp2W57m1LiJaaB0iWIrsfh9OX1Q4EpLr7k5EjOI6Q9gRr5VU_vB0C_B-3pDMW4cXD37bIqDvVRm1gLAGZQajkZIA46XA9oKntWymR7Wb6447Zv4NxK1OeeVUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ناکامی گروهک مسلح در ورود به مرزهای جنوب شرق کشور
سخنگوی پلیس:
♦️
مرزبانان هنگ مرزی سراوان مسیر نفوذ یک گروهک مسلح را مسدود کردند؛ در درگیری، یکی از عناصر گروهک به هلاکت رسید و سلاح و تجهیزات ارتباطی کشف شد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/683061" target="_blank">📅 15:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683053">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swPJ-UsQ-exS5vDlWhspWrF_G_-X0YVjT-Q0dBs0N_dDPlx0CBcLr_XXRYSU349BwXWPMc-jObdZAwWo--NUGTtUOKNnCYvNviGHK_t9_Eum0ZDRYi63SaG1exZS7pcrYFqJI1_IrHkjLaKfjqyhTgQ6mXBe_jBDd2Y4c1AHnhuhthPHy6NBr3JZir3Ar2TgqU23UzEnusgEyr0aplzkBssMYeQRE_0jBe66o4IN-1-05Dejvo0akn5A13uQR86nBFdt3jDoqtbcFt_Rk_YfiDfM08uGSp0r6oQjLmck7phDh8BuqoH3rzUpbNA2aSdSwLvWlzyt0vmSQbG80RZLpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FcjGbOqoZNOIkLMULcLeF6k9S6BwMLnuHyamjTHoLzqKnihqayQl0u-ho0btBQXKXADnV9iQOE5x0XLgjHSwF2L4h5l94cTyoSAk5mS6lODnEaefuqaiMipL9Y8u7-Bxd6MpWiw-wgH_hHBcd5P1BJabOYeILnnCDcACHMWmWqsOGt59WQGUTY8kKuelUvgmBMVS2mryeJyiIE6FEqHMU55piFX9OtUfwYV_LPTtLKTRqW-7FNAsP4fVEXUz4-FpI0sg1aLYPm-of9meQikPEi0qO0ozhzvDDhiElyeAKswuBk_Tv1EOKGM1K0Zx-ZQYlGbeFnCZsrIz5dL6rcxkLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R79bOFI_3xbcVnWb9Ng4xZNkvi4U_EMogskvME-xnmybwX4GYr89bjnwYzW70ijnms8mcBzTfZiJfcIc1LJlP_JF_b6inqCHxQr03x3Ntda21vi_-4dZ-B3bUbHsTDllABwt4YY2K_rQ9dfO6_-n5bgNl6Lf3NFjJngf1TvIoKtYTJJGeaa_ACUERE_pkwSCUdCjzXn-4euLgOQgRj3_bZM-V7Ll85C67K1ara4tl8gbak6DNZAU5LwASTzRTlFxE93sTqgyRoZFZE5jsMyKXhKdxUxqZ2tViWTMnwhY2SO09YCe47Ur7JSdAwVj9zNf-10t-nEy2tnZ_Ms4rrVpJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7Z6Mp86ROT4UW80LF7lJRN6ChwwUweKodI3NuT3q2bYSCcE9wOWyQKk-N2vKZnL8pj_C5q9PNjsIYIl7kQa1eFjye7YRkwrlSe3rJYv8myf5il3mlGNEydf-BfvplMd0wWVjEk35w-eyrY8OWAKNYeJ3hfwEBnqKlP9rBFOE4jLvskNr4z03-pPaEnlebQSBKvCLncwpO_ME5P4T6ORL3DixNxDmth7TqnnVww0oTsXqrW4U5_5IPwoQaQ4n_aJHSEHSINF6OzZg_IS0PXKxZjApr8UEXEn6kI02N-2cVYIfTDJ-ErYo95sciGmA7Qdd8kLAzA50oFtGQWh709t8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qrr6sHqN2ORjlcLg6Uy91HH5kItBqfAmMXl7Cl09MQKtxx5H87Rvcq0oGZXWD7xutYlitEsOBDXedfs1vQfnGdWeHthOxWbb347ecL0oLrZxEK4RWkAaEiaPS44VLDRkfYtEPbF9CVBwzsa27udK59_1auumG98zywLCfMKxyDVr5D2qtcGCgBEdXfTAeE-AXIhRRuCVFkD9YvibYDYXidz0DiWAlUg6yQT910470wh7DnkJPpq5eyYLWowyCX-n7XEGbURRrx56uQ-bX6jyjT4GMiQX3kV2_h1H7txMJNz98wJbm0Bevu-oHiWIVYs4mbsZ_h1nIUJecy9JXLD6Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F1yFEZjryosuZTUwEm34rp1RmD4hLjI5ELGz4P6dxdc6QqYXCSUalsSojkD2e4Nqa_Aq6NMMKWULx1fNPV6EaJlsQ6OL-hqJWZJLtDikRoM1Ox3Dvh0IYHpp0PokjxdOyGLsJAHhOFVqnwkd9RjUEz_sQbWfuQRqlpp0kwihwWWuQmAc-6h76Pf59jguvR-t28rCIfLlHA5wb0cPNYH-bOVehmCnurC8mHDXBJoYYhDcykdmlr_sEBy9calUMPawBENLT1loYQ0r3PYqwK7NIfagLNLOonyz4U4vZ2Qx8l88e_vpyhNa2-FGoDk0JkCp1dnLyVVfYi6kuf3ro719xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAwByUXtduete0IvWnPyh285zdsJodayYZZKqf030Isd5hDzkhUidVdBX6NFG1LCPTNyyTDoC58Q_EktNkSYqTC9oiKMzsMs1tu4dwhM_cDjwUtuQL52w8Lj917G2k0g5jDLcLi5ECUrukk-TsNfs3MmYxiyzFyLPD8a3YTH09OrUel71etOsAsL21QBkLrGq4Q7QKHvcKkHw2AO2HWGxeMlhxObUEjIK06RWcJ0wnff7zFO7owBSdcHwv_DTXN2-Y_IQ0M4Uj2dmxh55y_6xHRN1oy4tzaUSlbUxZypSEPTZMAlRFgsilrQdDNHG4UiS-DdW31GGEN6ooiQakySLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۷ مدل بستنی خانگی چوبی خوش‌رنگ و خوشمزه
😍
🍦
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/683053" target="_blank">📅 15:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683050">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMkPhBO3Cv0nLrFsmndrqdyjhqUkxxGc33DkloiHlRwO0JK6fxJQzb9wIWyhXeQi1tx-Yi4vTZMAkSAeDsYPe4WCLCmDw6s_PUcqgP4o0zIcR7WTfFSn1ft24poCy5JNSCR46lDhj6mGIfPccnWhCGRu9po1m1DTBUuiKYdi-3_SzC9M7NHauzwgotGAWkaipF8JLdplms10W2DHlyB5Uj8YsbhSeoU0zYblG5vsIiUNgvytgg6SW0SUVo4li7GHpQMeeby8NcIh4Ey9O9pd53gP3yTV4FPNgpRMYhHVbq8JKwZipY9erLFUcQCtRutN4yDQmOKsLX_jM0fitzBpvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QL3BQz30qojh1Jb_W_FQVNKVQ_R_oF-z1DuglR_9LPyPI29tGtZVRmScE-2C4Kywz-lw9_kHlRvbFa9r0AnBROdbsMywSctAWdEfaamxpx_6HVEPj1wUNBOSRG15ai5ZTu3RS-vX1CEB5g6bOemXsjCmoT-FjJwT_gKGGrIMgsGSTNF90WUQCpOc-WY8zmkABkBofcRnLBFLhWEvmKca6anXPN33sP7K4cP0uSahcAj18sS_DG2V1aqA3wvU4u9txHlfEb3ui2jf9REmVXPuA_A1x0iBemhq-JNV5wIMFf7sGP48O_nL726STXc1TA8lr1tLaKn0PcPN4rCfSfeF0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dVbS5vKnpXn6XXVsapZID8_W8bNWYhZpg7BajvAJpNOxcYzt2sp5XHptrifVYw6xAqYvij_12LDElHBTypmY-sLfFX5fFAv1eeXrFLLJ-B2sPyk9TLzxoBYjSjb16nPmtWYbv-gdVTywLTJp9Z4bB6ey_dskEQ07lfIhHtaq2yX9D0ykAMKluZ2HHIB9ORPYt6rYOhknssIWqAU-L-aCX16nmfb-0MMjmtbtgFtHhN5Ic64-u63AI8CXtn2xhUzTLt7v-Dy7-so4DyV4_HuCC5vHFFiDQa31RdZVlawOr0vaYAUaBbU_AoEjvfHDsYPARpY9lvBQ-fAooQjD3UanNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
بستن شیر آب در زمان‌های غیرضروری، گامی ساده اما مؤثر در حفظ منابع ملی و مسئولیت‌پذیری همگانی است.
🔸
الوفوری را دنبال کنید
👇
#همه_باهم_برای_ایران
@Alo_fori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/683050" target="_blank">📅 15:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683047">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
نرخ غذای دانشجویی در دانشگاه علوم پزشکی ایران اعلام شد
🔹
طبق اعلام امور دانشجویی، قیمت وعده‌های غذایی افزایش یافت؛ صبحانه ۶۰ هزار ریال، ناهار ۱۳۰ هزار ریال و شام ۹۰ هزار ریال شد.
🔹
برای دانشجویان بین‌الملل نیز هزینه وعده‌ها به‌مراتب بیشتر تعیین شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/683047" target="_blank">📅 14:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683043">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fb760beea.mp4?token=QBe9i63-Ag2L9p8rmnQ5GNRKZxGM96pWHxbYFxdUvfFN2iRIblIeDhCQkjih0BX8CWDhmTccRTaVAuK6C1-FMpTg9Bi4V8ji0SjHkYq0249y27FZyTP3nUz_WRN8KP-VinUZs-__ztMPav0lUx_OY0g3edPZyu0BDte75Eje5_IKRwTId_PDKErt8UPW_ZmmmznKpg6KVcMEPrzfjc2Y_NN3kQ_UqzPIGN6AFKCR4a9sEJHOTWqNqvSpnVsr9Cd3YNM4IuQUBqT0zeLmoMwlTsYlLge5ECL96V4FZtZWsIfZhhnTlYXrLSic2dxg2YsXCSRSQJBJ7Ef5QR4briTOqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fb760beea.mp4?token=QBe9i63-Ag2L9p8rmnQ5GNRKZxGM96pWHxbYFxdUvfFN2iRIblIeDhCQkjih0BX8CWDhmTccRTaVAuK6C1-FMpTg9Bi4V8ji0SjHkYq0249y27FZyTP3nUz_WRN8KP-VinUZs-__ztMPav0lUx_OY0g3edPZyu0BDte75Eje5_IKRwTId_PDKErt8UPW_ZmmmznKpg6KVcMEPrzfjc2Y_NN3kQ_UqzPIGN6AFKCR4a9sEJHOTWqNqvSpnVsr9Cd3YNM4IuQUBqT0zeLmoMwlTsYlLge5ECL96V4FZtZWsIfZhhnTlYXrLSic2dxg2YsXCSRSQJBJ7Ef5QR4briTOqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شغل عجیب و ترسناک یک زن در فارس؛ کمک‌رسان چوپان‌ها در دل طبیعت
🔹
یکی از عجیب‌ترین، ترسناک‌ترین و هیجان انگیزترین مشاغل در ایران مربوط به این خانم است که در استان فارس زندگی می‌کند و به چوپان‌ها کمک می‌کند.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/683043" target="_blank">📅 14:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683042">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_q-eZ3nepb8_Jx2azDasQAmupz8oLO0prDyUYbqPeO8t5C31OxhpH6_bUC4QE6xkENCENHKiUPJ34w-eZqwyfSQ4Bhifl8Fz0zl24TinotfLLodIYoZ5uHzI_7ufaoN4Y0Klb7MRu_mlUHpu2XLDQ0Ux05eiSs-JLzeoHJ7FznX9j1fGN_mSNTnSpN2X0BmKORokKbvRif8lbQxEztFS9t88bbE5JoMqn3goh5y4nC9lZA9_91INhxEyYZTJu-ZFafnBLuXk_9Ty6l2yz_hl6UegmGvPzKZscFaCEyEGAfrVovRc6hh8TpATjiCsjM0m0HFkBJLHfaYx2Xa_RYsow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقدیر معاون اول رئیس‌جمهور از خدمات سازمان راهداری و حمل‌ونقل جاده‌ای در اربعین حسینی
🔹
معاون اول رئیس‌جمهور با انتشار پیامی، از تلاش‌های بی‌وقفه و مدیریت موفق سازمان راهداری و حمل‌ونقل جاده‌ای در ساماندهی مراسم اربعین حسینی سال جاری قدردانی کرد.
🔹
محمدرضا عارف از حماسه اربعین به عنوان عظیم‌ترین همایش وحدت‌آفرین امت اسلامی در پهنه گیتی یاد کرد و گفت: این راهپیمایی عظیم مقارن با رشادت‌های ملت ایران شد که در جنگ نابرابر ۴۰ روزه با الهام از حماسه عاشورا، حماسه دیگری را آفریدند.
🔹
وی یاد رهبر شهید انقلاب اسلامی که عمر بابرکت خویش را در مسیر عزت اسلام و مسلمین سپری کرده و همواره بر پاس‌داشت شعائر حسینی و عظمت‌بخشی به حماسه اربعین تاکید می‌ورزید را گرامی داشت.
🔹
عارف از تلاش‌های بی‌وقفه و رویکرد مسئولانه سازمان راهداری و حمل‌ونقل جاده‌ای در ساماندهی باشکوه‌تر مراسم اربعین حسینی سال جاری، مدیریت مدبرانه در مواجهه با چالش‌های اجرایی و ارائه راهکارهای اثربخش و ایفای نقش محوری و ماندگار در اعتلای سطح کیفی و کمی این رویداد عظیم قدردانی کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/683042" target="_blank">📅 14:16 · 30 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
