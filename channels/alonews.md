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
<img src="https://cdn4.telesco.pe/file/sDsm_-keZKlNr-QSejrR9gTOXDRKiVP4oS_kEgmYxkv5yQ6DrIJxYLxyJw5RNNGVp2N113yJD_U1tQGuoI6phqBSQ8Q--AFGo-FpGzLKHpvrFVvF6eKjCwc5bfcXBOJu7wQ-9y-Jo1Bz1gLBw9NeHbfRe0ahU72475GOkFHgbVNEdN2PeW92HmCpRh3YGI0IgNb3h5IzXiHznyQ7uLQXe-I9pl1EIUmDLFGOI3LEsIhmuLqdix0xQWT2fA3xCXSs0wnQFuMhKfFTwyWXaM6bMuheuDumHYldqGp4sW0UACHKDpT-5LgTEVf0Uuo7DgwAERmSZXsKz0ZJvQNviV7txw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 951K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 20:17:40</div>
<hr>

<div class="tg-post" id="msg-120645">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
وزارت دفاع امارات: ما با ۳ فروند پهپاد که از مرزهای غربی وارد شده بودند، برخورد کرده و با دو فروند از آنها با موفقیت مقابله نمودیم.
🔴
یکی از پهپادها به یک ژنراتور برق در خارج از محیط داخلی نیروگاه هستهای براکه در منطقه الظفره اصابت کرد.
🔴
تحقیقات برای تعیین…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/alonews/120645" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120644">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
وال‌ استریت ژورنال: جنگ خاورمیانه موجب بازگشت جهان به استفاده از زغال‌سنگ شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/alonews/120644" target="_blank">📅 20:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120643">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SL4nW-g1ao-sG3m_HFC4C28JCqTePSAlnfaGBimUIi9bW511CJvdLKxbhY_je2yVnF39FUWlda-ZJfm1D0zpsUGegMyM5NqLxaYbzt_Y1fwK8JTACCFrln0jIhVqv3eHhKBHIBD6JCd5zNCHGRTCCsis6i4OEvzHCqDMFiYXLKJmTi-mQP0W1N4w1hDquuKCyTj6BDEz24q2bOFmERJH569LKpzoipekc3RvhThcUiYlmrPuUarzXOo4xq1cV-IhUl_nVPXbLBOhe69faUpaLJJ0hk4H3jV-ZW8afUBRAm4pK9zheC4qQzRzeCZpC_NMXswxWmOCpf8RvM2P9JeKYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نمونه اولیه جنگنده دو نفره سوخو Su-57D روسیه برای اولین بار در آزمایش‌های زمینی مشاهده شده است.
🔴
اگر تأیید شود، این جنگنده دومین جنگنده دو نفره نسل پنجم جهان پس از Chengdu J-20S ساخته شده توسط چین خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/alonews/120643" target="_blank">📅 19:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120642">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزارت دفاع امارات: ما با ۳ فروند پهپاد که از مرزهای غربی وارد شده بودند، برخورد کرده و با دو فروند از آنها با موفقیت مقابله نمودیم.
🔴
یکی از پهپادها به یک ژنراتور برق در خارج از محیط داخلی نیروگاه هستهای براکه در منطقه الظفره اصابت کرد.
🔴
تحقیقات برای تعیین منبع این حملات در جریان است و پس از پایان تحقیقات، تحولات جدید اطلاع‌رسانی خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/alonews/120642" target="_blank">📅 19:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120641">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ec930db1c.mp4?token=bwYtki9729J3WpNRdUaykHMHDUhp56rmAi3xBakLG3EUos2ShhIlpgAlqjGnd_7S9H14i57ba9i_OvTIbXAeHcBkgziNqzG2CRJFxbT_1Sz7gUGriOPEK-vFKmX4RBrYDIhTW6G9GOtv5unCH1Zlxtf9ioPSzNYcW-z1guO_4C3eSvGgKhQEvqOVrfFNLTNPSatevObD6grh70lx7mTx_1tECGK-EaCMa2OA1rrmwKRHVqIvYzsixmP5TvHAoykIjussLaq2zPvFcIqLTsncjApMXa6XFgWIJxOms0Qz_1lyy9zvdhk6oTm1B2Bs9tKy9j07SRZ0mieHB8q8GkfRuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ec930db1c.mp4?token=bwYtki9729J3WpNRdUaykHMHDUhp56rmAi3xBakLG3EUos2ShhIlpgAlqjGnd_7S9H14i57ba9i_OvTIbXAeHcBkgziNqzG2CRJFxbT_1Sz7gUGriOPEK-vFKmX4RBrYDIhTW6G9GOtv5unCH1Zlxtf9ioPSzNYcW-z1guO_4C3eSvGgKhQEvqOVrfFNLTNPSatevObD6grh70lx7mTx_1tECGK-EaCMa2OA1rrmwKRHVqIvYzsixmP5TvHAoykIjussLaq2zPvFcIqLTsncjApMXa6XFgWIJxOms0Qz_1lyy9zvdhk6oTm1B2Bs9tKy9j07SRZ0mieHB8q8GkfRuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله تو جنوب لبنان با پهپاد FPV به نیروهای اسرائیلی حمله کرد و زدشون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/alonews/120641" target="_blank">📅 19:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120640">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام اسرائیلی: ترامپ و نتانیاهو در تماس تلفنی پرونده ایران را بررسی کردند‌‌
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/alonews/120640" target="_blank">📅 19:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120639">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/437d8e22c8.mp4?token=oQ8FgBwJqPYk2HmlfBA2_Ag4-VQw-pavljOyKdnTH2S5yWYOFpygrV5cuNTVN86DcWRPZW20C4v3lJAKjDjd1Yd2Q0vhqOBIX0Owg6zeSUYy_SCLUv0HWKZrt1v6qNzLWuT-Ivy1YcLHAZ3AX3hufYhz4QOA5rbb4nopJon95zCKjFW2rmTWD985k9ohvxMhucY_V-nX-WUw63ZGgCfwMsD6If0a4TbNg1fZwBBsbfeVrwUEuB03BehjPwak5MmIF96D7Vy7Ew5TvNO0UQcnZ3RAd5DiBsxYmfMURC5fb52ylCwPsJg2bzga0C7XMkPYmAcZwLJhuKZWdP_HIOcDYQVxFHWU0xHjL7xyfZ6eEAlY1N3XQIQ2_D0WEtCb7s6wKOJn1h52tsUvUfh_B-M3bZq-QA_8zhvLG6pseB11FPYSSHdJcgFw0S2uV-FYQxLqVoCk3xiDRrt0uXRVw9wLa8CpkvdNKzZUqk1WYcQB4Qslg3xwSFwT8acTY1HjvynP1ZoHIhTFCLKitlL-tFwnx7wqrDE_zJkvv5wv2mtZGBHZCjqqr-nBaylFxxtyMbWRL8eELszcbCG2is4nTHYByAAZEACMvdl23sc5XhBmKWa-ORpLSRRoY4OF-oWT56v77AgGdr4jmO8-T5CyL7JjqzSBOa_ePd_Yqi8tzpY8l4c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/437d8e22c8.mp4?token=oQ8FgBwJqPYk2HmlfBA2_Ag4-VQw-pavljOyKdnTH2S5yWYOFpygrV5cuNTVN86DcWRPZW20C4v3lJAKjDjd1Yd2Q0vhqOBIX0Owg6zeSUYy_SCLUv0HWKZrt1v6qNzLWuT-Ivy1YcLHAZ3AX3hufYhz4QOA5rbb4nopJon95zCKjFW2rmTWD985k9ohvxMhucY_V-nX-WUw63ZGgCfwMsD6If0a4TbNg1fZwBBsbfeVrwUEuB03BehjPwak5MmIF96D7Vy7Ew5TvNO0UQcnZ3RAd5DiBsxYmfMURC5fb52ylCwPsJg2bzga0C7XMkPYmAcZwLJhuKZWdP_HIOcDYQVxFHWU0xHjL7xyfZ6eEAlY1N3XQIQ2_D0WEtCb7s6wKOJn1h52tsUvUfh_B-M3bZq-QA_8zhvLG6pseB11FPYSSHdJcgFw0S2uV-FYQxLqVoCk3xiDRrt0uXRVw9wLa8CpkvdNKzZUqk1WYcQB4Qslg3xwSFwT8acTY1HjvynP1ZoHIhTFCLKitlL-tFwnx7wqrDE_zJkvv5wv2mtZGBHZCjqqr-nBaylFxxtyMbWRL8eELszcbCG2is4nTHYByAAZEACMvdl23sc5XhBmKWa-ORpLSRRoY4OF-oWT56v77AgGdr4jmO8-T5CyL7JjqzSBOa_ePd_Yqi8tzpY8l4c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در ایستگاه پر کردن محصولات نفتی «سونیچنوگورسک» در روستای دوریکینو، منطقه مسکو روسیه، پس از حمله پهپادی اوکراینی در طول شب ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/alonews/120639" target="_blank">📅 19:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120637">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aHoexqdPSFAb-R58xyhgS_sRdO4noyuGbb6Sd7KU3yEhurLTXHr_8NJjCFvF6UV_01xVu0GY4UyFY0B5-5HhEWndDeJhQ-bDh1HipRwkbQdnpfkCJqNzlwdhH_OUQQUngudYla_o_FPE2rXOl0xlflulUoEcAGg4Rqnx7oS3IiCzm71VTd_HTynlPCLsJqb1Vx0KY4ZcEM4VY_V5TCsGfEPg2x8DJ_ssLqHxdlM0P3tFuuzMkJSLRnw31fWRM4ASmTBJTt2UElz_l7EzSVEGgXhF-wqLu_u7Z_RBsDz7DbXo1DBHe7ppJMOXInSVaZuAM907EvVy1V-wvMmNuWj7EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ThMO2enalqI-KldVc3XoBPyfQmIkef49ruZfWQLy1ZINZ1FaCyGdDQM_DDmRK9FlNt5h1PIryplfDKfgJD0YmgDJXuZtOsrQb6VU83DZkTMlCJsC_b-coDHjXHEvc_i_Ubu5unwHvan5TcPjBFOZoQOjMC2RkV1mU8Axz4ZzFWNpSl_w_7GOIafoBKUYM51kMaQUwCZAw6TbwzPPV340N8WPXKj-1pbx1sUx6sz83oCLgvF_pJspOFGHE6ku6_tcFNC7fNJ72nZ3B0WwMq0RFnJtvAbHVNrIuvWI-ePi50Y9s50OoAkT0xtgpugchAb8pwc8yXRzmd6ADhexPT3EfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
آنالیز تصاویر ماهواره ای نشان می دهد ناو هواپیمابر آبراهام لینکلن در فاصله ۲۴۵ کیلومتری از ساحل ایران مستقر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/120637" target="_blank">📅 19:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120636">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
شهباز شریف: امیدواریم دور دیگری از مذاکرات ایران و آمریکا را میزبانی کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/alonews/120636" target="_blank">📅 19:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120635">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
کانال ۱۲ عبری: تخمین اسرائیلی‌ها این است که آمریکا در طول این هفته به جنگ علیه ایران بازخواهد گشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/alonews/120635" target="_blank">📅 19:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120634">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
گفت‌وگوی تلفنی وزرای امور خارجه ایران و قطر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/120634" target="_blank">📅 19:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120633">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahOADv8dfcMG3tPj_RuwXTST5EbCca4gknYzV1_Hd7d_jTcmb-rMVKnB830Nb4tZK0kX_cKLRDRc9rcBTcdGSE8HGeCgdxZiW1tg3WOR5x6XXXo0CXdlEJH6VaHiCCUp6xsfrBYbA4tcEcBri4JBI_A3UTXR_0ag-4HwGoSHuYx6MtTtaxu7TKjG6AtL4H4_4yXFcfRn2k7hSVgrWCDwWISfBm7r0YI9v443KblAqrP56tCpNB92TFsC3z8jp3wkAhSZIXahezfX8l6sihd0gLiWTMUKc4_dYp7jIfM0CCAzXjEmVOtQUAoFdBtcpifihEIAO8TcMN0fhcDOkDZQvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام اسرائیلی: ترامپ و نتانیاهو در تماس تلفنی پرونده ایران را بررسی کردند‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/alonews/120633" target="_blank">📅 19:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120632">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
الجزیره: هشدار ارتش اسرائیل برای تخلیه روستاهای سحمر در بقاع غربی و رومینه، قصیبه، کفرهونه و بنافول در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/alonews/120632" target="_blank">📅 19:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120631">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFlPtI1_PDRnmh3h_4rCIwM7mpBG8HODuK8DjS4yYyUfEPxokmdQOfXL7skjwf3syisRXLW1RPDC62hkNDN3j7E9Sk6fn4AzTUPYh_OYkFizHlVYU7NP8YJUwafUkj94lUYfsTnYhLeRthoN9UCtL_qkXA-EiKsDvdyVmbboDoXr6zjSHJusQeMlVJma60pPno4Ee29qJacILdIWD9MQ7mbwJ7zmQm9arwFsg_FOjMoaxFndzQYlp1kC9XKgUvTQT0vjikHao4oqWhG_nDI29ZDYTyv1K4BwEUdSdE3Hyw85P1O4Gr_V__Gq3MYTBvK_uL0RXMmgD713hQgiGUCnAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
به درخواست شما تمدید شد
🚨
🚨
قیمت استثنایی گیگی
9️⃣
8️⃣
1️⃣
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
💤
این تخفیف فقط تا ۱۲ شب فعاله
💤
⭐️
@Napsternetiran_bot
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🔶
@Napsternetvirani</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/alonews/120631" target="_blank">📅 19:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120630">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3494a163d.mp4?token=ATnqcDe9sKeaGxFlNiaFgVL2OUgwcqqvgbGr8xVNPerZ2G5VDZUB-2NXcfgnQiQlg55uCbVAyloio1Jm1cBy_6CFLHpeWBDWY512qSBraAVsKc263Znzqe4E3zr5uveWRbZCWrtlzPBJ1Gh27-AhEYGfpT62dOiI1c3az6RwYdJvqDd4-eWW5sbgx-sjIvXvrWXx_65kc6oNUT6DXlPmZzGepSe3apHzAm2VZAHbY_C_oyZ50KEjOINyDJpspm_JVBLTKA-QOQc36q3UB1jakaGSXMvCLqa-6rq7J9aADzLnHRLHGwl5AZYOVsTeJJfN2timy1XdITd_9VeNrVcVAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3494a163d.mp4?token=ATnqcDe9sKeaGxFlNiaFgVL2OUgwcqqvgbGr8xVNPerZ2G5VDZUB-2NXcfgnQiQlg55uCbVAyloio1Jm1cBy_6CFLHpeWBDWY512qSBraAVsKc263Znzqe4E3zr5uveWRbZCWrtlzPBJ1Gh27-AhEYGfpT62dOiI1c3az6RwYdJvqDd4-eWW5sbgx-sjIvXvrWXx_65kc6oNUT6DXlPmZzGepSe3apHzAm2VZAHbY_C_oyZ50KEjOINyDJpspm_JVBLTKA-QOQc36q3UB1jakaGSXMvCLqa-6rq7J9aADzLnHRLHGwl5AZYOVsTeJJfN2timy1XdITd_9VeNrVcVAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریستن ولکر: آیا ارزش از دست دادن انتخابات میان دوره ای را دارد اگر نتیجه یک ایران غیر هسته ای باشد ؟
🔴
ارزش از دست دادن شغلم رو داره اگر مجبور بودم کارم را رها کنم تا مطمئن شوم ایران هرگز سلاح هسته ای نخواهد داشت ، این کار را می کردم.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/alonews/120630" target="_blank">📅 18:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120629">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزیر کشور پاکستان: پاکستانی‌ها شبانه‌روز برای موفقیت دولت و ملت ایران دعا می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/alonews/120629" target="_blank">📅 18:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120628">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=IkNfFI_j0Yf3Pyjw-Jk5n_d22u70Z5NNDUDnUEA7NxhzFnBBN3TaZpQE4zojv0cPGIJ_QJhudT_fACKwCdBhg8ZMEMRKq6fQ8XwNkX0iBbTvcyUWc-MPE_-hpTVx6Zx8aqX1KcH9AGHav9poIS3OLDHcoVp5KdyYeLwSXCf04hjo10lugDsqziH2XqX0GhSQv8ql7EB32JAxNv74yqshXpEIXPfhuVCcAf7ZfAJ8ttCWcjUPFQyzhJsp6cq3S6emReG1Kn9QJM_FvIgbmcklMNBJnDgv7X1TEmhWCTdOhKZVRB714_VyRO-t9a4_aRFkA4R4InpbGwckdfdskbSN8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=IkNfFI_j0Yf3Pyjw-Jk5n_d22u70Z5NNDUDnUEA7NxhzFnBBN3TaZpQE4zojv0cPGIJ_QJhudT_fACKwCdBhg8ZMEMRKq6fQ8XwNkX0iBbTvcyUWc-MPE_-hpTVx6Zx8aqX1KcH9AGHav9poIS3OLDHcoVp5KdyYeLwSXCf04hjo10lugDsqziH2XqX0GhSQv8ql7EB32JAxNv74yqshXpEIXPfhuVCcAf7ZfAJ8ttCWcjUPFQyzhJsp6cq3S6emReG1Kn9QJM_FvIgbmcklMNBJnDgv7X1TEmhWCTdOhKZVRB714_VyRO-t9a4_aRFkA4R4InpbGwckdfdskbSN8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور گراهام درباره ایران:
هر قیمتی که لازم باشد بپردازیم، خواهیم پرداخت.
چرچیل چه گفت؟ «هر قیمتی که لازم باشد برای شکست هیتلر بپردازیم، خواهیم پرداخت.»
همین موضوع درباره ایران هم صدق می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/120628" target="_blank">📅 18:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120627">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3706aba91d.mp4?token=p4JAdS5-584oUQpIgtKxpXL1hARelHVoR0SV9TYqF_hf44hMkItuKVSvKvDYltx6UQr-clgRuM5xS0Z3C9tSHGcDTmjqhZklQz64t5U5Vaaeu2imJdI1X5tv8Z9NWlGA6nYHBTnNiGAgGj0MKL-qzfjTQZ-qnkDMx127tpjYsDcslEWouY6UVn_2lfXz0lm1OTqghhl8vbkRPDgNXm36BujJIuajtM-PlAZejcNw01d8sQjeMFE1GSD_UEbiRaT9owt38mIA85WJXzNVtdXCwlU2AtOOIlTjUyl3dGUsT8Z-lFGcG47W3DoXUJf6L8IInXp1RGHCaktoVW9Zf1UrVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3706aba91d.mp4?token=p4JAdS5-584oUQpIgtKxpXL1hARelHVoR0SV9TYqF_hf44hMkItuKVSvKvDYltx6UQr-clgRuM5xS0Z3C9tSHGcDTmjqhZklQz64t5U5Vaaeu2imJdI1X5tv8Z9NWlGA6nYHBTnNiGAgGj0MKL-qzfjTQZ-qnkDMx127tpjYsDcslEWouY6UVn_2lfXz0lm1OTqghhl8vbkRPDgNXm36BujJIuajtM-PlAZejcNw01d8sQjeMFE1GSD_UEbiRaT9owt38mIA85WJXzNVtdXCwlU2AtOOIlTjUyl3dGUsT8Z-lFGcG47W3DoXUJf6L8IInXp1RGHCaktoVW9Zf1UrVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور گراهام درباره ایران:
بر اساس تحلیل من، هیچ چیزی نشان نمی‌دهد که افرادی که اکنون در قدرت هستند با قبل متفاوت باشند — آنها هنوز هم می‌خواهند جهان را ترور کنند، اسرائیل را نابود کنند و به ما حمله کنند.
پس شما باید آنها را بیشتر تضعیف کنید. کاری که رئیس‌جمهور ترامپ انجام داده از نظر نظامی شگفت‌انگیز بوده است. زیرساخت‌های انرژی نقطه ضعف آنهاست. وقتی به مبارزه برمی‌گردیم، انرژی را در صدر فهرست قرار می‌دهم.
من خواستار آسیب رساندن به این رژیم هستم. بیشتر به آنها آسیب بزنید، شاید آنها معامله‌ای انجام دهند. اما در حال حاضر فکر می‌کنم آنها سعی دارند این وضعیت را تحمل کنند و بازی می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/120627" target="_blank">📅 18:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120626">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJRGNjBuyMiowlaWXkMZc02t2HYdi-GBNCiTIxZUYx7bKVgnMOu5vIh0ezFdcjk0zKIRDw9fbuQevNGS7PXEj3EUR667ewDLyhDkAEbAEH78HMUHe55vjHZsw21nW8LCp707F8dYtmjQRv_ksO6vbUJKonPVbbAdKxNFNcV7EKFoU5dc3BAxRo4FYTZbIhxSFdWTSCy40IOqQhz54KALCN8CBPjlU0xbXGhdvp9uXrqPiSNeoL6RenOaPmjM_ZagJ7bxGnl20thY0pjIeWq2X6RBj8azDDdrEFcGnY1xKRjTiooxCII8KiEyNu0m0LjdDFW6hWmTvgztJmGTcWOM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگارای کاخ سفید رو صدا زدن که برن تو محوطه جنوبی کاخ سفید واسه یه "رویداد نامعلوم"
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/120626" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120625">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AK63fd7XaSXu_xDkxPyShalIJUVpJLHZnDBPzXG_W-1gz7bXLOs3K4B3oMw8bOlw0mne-_Ei_ablS83oHElAKXzYa-MOETRpvaZ1z8M2IE26-87lBH55_OQNiojJuDHULjzElLi8OL6Ff_w6oZFeMJxLRWjQ6NQ8oKDswGl1OtKGFbNVu1p4eQlWRR0g5A5R-7RPus-ZWHzBh845JY7zHoz6lcq1yEm7Nsu2F2xqLnpCHyudB6QVoQ632XpxEgKPp6enAaIEXg-zqw_CErkIsEexa4Xa5RV-WOTKCS237RKCfdRL4419fFHoHvndhf4dKUt09tiaGn1ANhGAFXDIHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بنرهایی که سپاه تو ساحل تنگه هرمز نصب کرده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/120625" target="_blank">📅 18:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120624">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82a4f48946.mp4?token=gxXbeTR8ovspbWSt-wJoPmYWjeomP6fbZZeshIuKYDiF3485P5PIbByw3kHIvI6Q-ppwlJLU8aMoJagXwCx1mXP2-bORAfiowzwafDkc6B9EA7l--mrs6v1G2MAdT3uyBDrqIbauD6SUTG6ZPGcM5QHf73q37r0R66PV-6XeYbfh_SgxqhZ6fb7twWhGOlbYwoh7kvd56jOuNOISTGcwYztCYhnE7zjpmicIrY8A-bXJsppzgxCO8SeCbkVnLBxZu8HeNgUihDPxo-MbY-mN-8tm7Sd1YmMlhN8l1OTxQInpN3PqGKxLEbCdh7hqyF0u13ZRGQ3Z0f196ZM4LblKeg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82a4f48946.mp4?token=gxXbeTR8ovspbWSt-wJoPmYWjeomP6fbZZeshIuKYDiF3485P5PIbByw3kHIvI6Q-ppwlJLU8aMoJagXwCx1mXP2-bORAfiowzwafDkc6B9EA7l--mrs6v1G2MAdT3uyBDrqIbauD6SUTG6ZPGcM5QHf73q37r0R66PV-6XeYbfh_SgxqhZ6fb7twWhGOlbYwoh7kvd56jOuNOISTGcwYztCYhnE7zjpmicIrY8A-bXJsppzgxCO8SeCbkVnLBxZu8HeNgUihDPxo-MbY-mN-8tm7Sd1YmMlhN8l1OTxQInpN3PqGKxLEbCdh7hqyF0u13ZRGQ3Z0f196ZM4LblKeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جلسه دادگاه ساعدی نیا، مدیر کافه زنجیره ای معروف ساعدی نیا به دلیل حمایت از اعتراضات دی برگزار شد.
ساعدی نیا: من بلاتکلیف بودم تا اینکه استوری گذاشتم و مغازه رو تعطیل کردم، بعدش از ترس استوری رو پاک کردم و موبایلمو خاموش کردم، من هیچکسو به حضور در اعتراضات ترغیب نکردم.
منظور من از فروپاشی، فروپاشی اقتصادی بود و نه خیزش علیه نظام. من هیچکدوم از کارکنانم رو برای حضور در اعتراضات مجبور نکردم، از کاری که کردم پشیمونم و از دادگاه می‌خوام فرصت جبران بهم بده.
قاضی: شما با فراخوانی که دادی کلی جوون رو به اعتراضات کشوندین و ضربه زیادی به این نظام زدی، چطوری میخوای جبران کنی؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/120624" target="_blank">📅 18:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120623">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
رئیس مجلس نمایندگان آمریکا:
عملیات «خشم حماسی» به پایان رسیده است و آمریکا در صدد اجرای پروژه‌ای برای بازگشایی مجدد تنگه هرمز است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/120623" target="_blank">📅 18:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120622">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtD6d4_UnUI5yFODN6g5KNAAVLM8DF9SHCYeSTWTzUPZBilTu5MmpAgftsKY6AKVL7sDH8nSSMW-50lc_HwLa9NghtmGckqO2aPxAkU4KFvSjs-yn-YCyQ8udxC3OIG0a-6-NjgxPLVddYT7CukXF--pDwN5Uhvwns-PMHn98y1cCqmxhXPYr4nj6uxeoAottsJ6sAbJXLkGCVcUycJW41eJSD-A4jByTCQbcoXIQqpMDA5vr3pbKdqYQK1EFoMDue7gjaKGjmnxaPFZdADEvC549-VpTqhtwa_qS-vUqAjN8CujTSamgLyU0NeowpxduJ_puJ73Yhr561M96S7F2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇮🇷
شانس قهرمانی ایران در جام‌جهانی چقدر است؟
سایت گل با انتشار پوستری درصد شانس قهرمانی کشورهای حاضر در جام‌جهانی را مشخص کرد.
@AloSport</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/120622" target="_blank">📅 18:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120621">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGAWlkBfcu51HFtvrUfm4DrSmACrNNENhgOI5Fj5zR26kaQc37QUUSypL75A6lYyl0LCvKH6r71A5q8gzh-LyVZEcb7sy2lm9jBQalgeZXHxB_D6R6DRnxZZpH5LVcOEO-V0VbtvLsMQYX-oFlhc0kkzQru9XGdonzzsm1ulKrQDcmNJ8axYvWXFNIj4RhlMDC-e3cvaoR6mw_SGXothU0iRrmUKMnoiS6aEPrqA4-de9uFcFzdVaInqXwsMDpstVOdSwZ1_OSDshT0Ssw7-9r5GMZq72TLEU7omyUmjBqWgbH6z9BO5x3GdBS7uls6mB9sTNWZ16H_VrAWwmCaAdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فووووووووووووووووووری</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/120621" target="_blank">📅 17:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120620">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فووووووووووووووووووری</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/120620" target="_blank">📅 17:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120619">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOzygS4903m-S4JWx1MdbcEWIeu8s9FUSH7hys1enNbCqS_jWLwiB7INt9RB0e6pNrbb1dCYWGdsqVTrOTSyincY43ufHS1ljocFDOEoZM5ZTUscwGil79llks_ex70h8-jPuKL7Mdm7S-ZsPLXVkbErV4oQteHZMgOJ48EP2qBF_kzwNn0puJJIVXx8z0LevpG86-ki9DggaqHGti8S3woPffFh1s_56ohQV6YoG6z6R_Id3vYA3hG-opkE3XfAnYFqySuw1luFR3Auc8i0TqvsI3Xxl-DwOc6FPKaJt5M1b_HfLKGjF3O-tMVldiBcQyxJEbqFrqHphI-D9PnjVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: تا امروز ۸۱کشتی تجاری را برگرداندیم و ۴کشتی را توقیف کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/120619" target="_blank">📅 17:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120618">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvD4cXjPAOaOlEXaIb5T72u3kuy6AVI1msfBisCmU3rICcCKcy3U8vLCvPZzNW1CHC7fZht11gaDEk5Zf4gDlsO300J5Z1GJlpfyXpoaz6wGZrcF-qPgDapnafskkWota80-xWN7z8Gzl7bz38jA280-am8dPfJnts0htssgzJ0ZuwUuY6gENCLgEmZMu_yclK-JOTQCzDKazwnxzY0MIKaG-YTFyC1VgPfC0W-HTlEj64SAhzBt6kx__lTU2dwOu_O7dtHAobyZC2ih1oC0dz14Nv1jMYKrWEx3fl0r_Dj3ok21qmOo5oah_xwfaTAI6zFctwZz2PaLNBkC0QlvQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای ویژه C-40 Clipper نیروی دریایی ایالات متحده که از یونان حرکت کرده بود
🔴
دقایقی پیش در پایگاه هوایی شاهزاده سلطان در عربستان سعودی فرود آمده است
🔴
هواپیما حامل چندین ژنرال ارشد ارتش آمریکا می‌باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/120618" target="_blank">📅 17:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120617">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/840e1333c8.mp4?token=TN06UYMqlmELM66kK6ZSCQ31n6FzFgdPbTeEd3e5MoxVH7ielC505Rryn6O9UmaTecnPJS7RM93cU4MYbj1g10o4C6G_ek2s00GXCz0XBFXv7vJMlRR2juD1FOc-iTvMrZncxgJqlrGb-Jog4P2F8VZBpArSzH-Rn2dcLiNyCfzJTnL31bnuOqSh9sR61M88PDKqrc_DDIi5aO5WBTCtOyo8s2Fdlt4WU2KyuDLLzPrnZkhLJSH7ORqzK0V_JyxNPEIAHFhjfeCoO_21IxRfr47wiVh8phG5Xbf4FEvL2q_TH3zN5_FE7q43kB8R86gyKcqITMbtzMAuSnJM3VhfjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/840e1333c8.mp4?token=TN06UYMqlmELM66kK6ZSCQ31n6FzFgdPbTeEd3e5MoxVH7ielC505Rryn6O9UmaTecnPJS7RM93cU4MYbj1g10o4C6G_ek2s00GXCz0XBFXv7vJMlRR2juD1FOc-iTvMrZncxgJqlrGb-Jog4P2F8VZBpArSzH-Rn2dcLiNyCfzJTnL31bnuOqSh9sR61M88PDKqrc_DDIi5aO5WBTCtOyo8s2Fdlt4WU2KyuDLLzPrnZkhLJSH7ORqzK0V_JyxNPEIAHFhjfeCoO_21IxRfr47wiVh8phG5Xbf4FEvL2q_TH3zN5_FE7q43kB8R86gyKcqITMbtzMAuSnJM3VhfjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات هوایی گسترده اسرائیل به شوکین در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/120617" target="_blank">📅 17:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120616">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
وزارت دفاع امارات: یکی از پهپادها به یک ژنراتور در خارج از محدوده داخلی نیروگاه هسته ای باراکه در الدفرا برخورد کرد‌‌
🔴
تحقیقات برای اطلاع از منبع حملات در حال انجام است و پس از پایان تحقیقات اطلاع رسانی خواهد شد‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/120616" target="_blank">📅 17:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120615">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
صدای انفجار در امارات
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/120615" target="_blank">📅 17:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120614">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
صدای انفجار در امارات
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/120614" target="_blank">📅 17:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120613">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bba9ba238.mp4?token=M5V2WgC2EAqN-vS6q5lRX7k4UyrJjjcNDrgbYWBRZ10jbcac2I3r1L8UvJ8lddk-BcOcg5qwbrZI_3yh_e7ybEJ1w7_81WqdI-rrcnnxrnjOKKL0UVUyXe5K_mp7wW955rfSe-rR_pXh5TrrNE_qm2Dou5Glz-bb7BN9NXlUc7gjLbCLm0fPZArO0NEmJ5cCoraIKg--0Hsl9J_QOtVHi-vCzRog68M6odAhd7SIsbtGeVLzrE__q5mQax0kQcWWO6VPbaNHLpMrtvGtl9LuJQVBm4k8HaxSKNZ3VP9oksIZ-P1HOIAoftJ4a4_IlTtN27vl5tb57lDEx_I4VIkz2hmz0AeHBObHQ2exxqxZZCPJLeLR0kYcb5YK1z3KIXjnW9W21OIwGXrC7dvqmUBbMscRSnUTkStj8Q_MdZlbWY-dEQIhvA3pznXIpMdVGEg1qBvgiysmGFPQ126P_1qZhKKonqarO8H1lym95BQ3qgnbXRwyB8XPFtb7VV7lePMZyeDgiO8WPieiUx0K7oysUflKBb8Z2Ogj16QPaOUqkAXg-6TKBFyX-DXiSbAq13mr9u2v9IwwyVyo9886HY6F2eNR4JMNXZBiovo5YRPHsvCjBKlzo5EnRQCe77AZYSTmtM4imS-W3CK4TE20gPmhSJjhBBw_ZhvsnRjiw7rXgyc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bba9ba238.mp4?token=M5V2WgC2EAqN-vS6q5lRX7k4UyrJjjcNDrgbYWBRZ10jbcac2I3r1L8UvJ8lddk-BcOcg5qwbrZI_3yh_e7ybEJ1w7_81WqdI-rrcnnxrnjOKKL0UVUyXe5K_mp7wW955rfSe-rR_pXh5TrrNE_qm2Dou5Glz-bb7BN9NXlUc7gjLbCLm0fPZArO0NEmJ5cCoraIKg--0Hsl9J_QOtVHi-vCzRog68M6odAhd7SIsbtGeVLzrE__q5mQax0kQcWWO6VPbaNHLpMrtvGtl9LuJQVBm4k8HaxSKNZ3VP9oksIZ-P1HOIAoftJ4a4_IlTtN27vl5tb57lDEx_I4VIkz2hmz0AeHBObHQ2exxqxZZCPJLeLR0kYcb5YK1z3KIXjnW9W21OIwGXrC7dvqmUBbMscRSnUTkStj8Q_MdZlbWY-dEQIhvA3pznXIpMdVGEg1qBvgiysmGFPQ126P_1qZhKKonqarO8H1lym95BQ3qgnbXRwyB8XPFtb7VV7lePMZyeDgiO8WPieiUx0K7oysUflKBb8Z2Ogj16QPaOUqkAXg-6TKBFyX-DXiSbAq13mr9u2v9IwwyVyo9886HY6F2eNR4JMNXZBiovo5YRPHsvCjBKlzo5EnRQCe77AZYSTmtM4imS-W3CK4TE20gPmhSJjhBBw_ZhvsnRjiw7rXgyc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : تو این جنگ معلوم شد ایران اصلاً براش مهم نیست چیو بزنه
- نه اماکن مقدس اسلام براش مهمه، نه مسیحیت، نه حتی مکان‌های مقدس یهودیا. به اینجا موشک شلیک کرد و هم اماکن مقدس رو به خطر انداخت
- هم مردمو، برای همین الان داریم بودجه ویژه می‌ذاریم برای محافظت و تقویت دیوار ندبه و زیرساخت‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/120613" target="_blank">📅 17:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120612">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f6049b0ad.mp4?token=gZOwSzQTF6CZ8YFTB0_GrMjc94u1tat-iKTI1Z6nf0YOY4sbpnVtfHukwXH_XNceycWYbdhi7yBl7OKgdopxOzZ4VqQagQRqBa8j9dGMoA0-CkAm95aAcGbOp3sDVOTejxvvTZj09t1G8rrW0mmnnIqHjsXncnfqpuJxOKrGm_3UX0TEncjm-QgkrVF_mweZNp9qJ-A3orKo_hz6wEvhIjMIis_6tCpl75WoUe-RUBv2uABCWpPjCL17OcTyNKpegLs8E97xmY4D5lIgwul9PYugHX5Tc-VKktfeikO21y6taCoeyAWfOgqEZP8cU-BKq3PfLTTfPsmep6RP-wVmApIsqcH7EMdWEG-RMzQZz4bhOBqdBp8MWbDwKzLIw3szARzljozA_gfbAVw620IuLzC_w9a6TUbzitQVePYOw4Ynl4yoZhZEugZZhDdJIC0nBFs7Vy8s1_sabTuJfW4SY9fxTQM1Nf-pqQ531kNW2_hdhSYJsjas3-1cSjsEVY6noqLQ85tfiBcrRWo8wJ0jWNVAziP3yILHq-K6o5Hv_R6JziKhfaQQe9a7Hu-RJFeu_LbR-EGB37BBL3HHGpTBRO2poP35NYtQDkbmKszvx_IBjYyDt2Wk4XrScSvEgfkN9w0G1AK0rKWYKnCmnrWlVNecJ-vmyEec2I-26qCE3Lc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f6049b0ad.mp4?token=gZOwSzQTF6CZ8YFTB0_GrMjc94u1tat-iKTI1Z6nf0YOY4sbpnVtfHukwXH_XNceycWYbdhi7yBl7OKgdopxOzZ4VqQagQRqBa8j9dGMoA0-CkAm95aAcGbOp3sDVOTejxvvTZj09t1G8rrW0mmnnIqHjsXncnfqpuJxOKrGm_3UX0TEncjm-QgkrVF_mweZNp9qJ-A3orKo_hz6wEvhIjMIis_6tCpl75WoUe-RUBv2uABCWpPjCL17OcTyNKpegLs8E97xmY4D5lIgwul9PYugHX5Tc-VKktfeikO21y6taCoeyAWfOgqEZP8cU-BKq3PfLTTfPsmep6RP-wVmApIsqcH7EMdWEG-RMzQZz4bhOBqdBp8MWbDwKzLIw3szARzljozA_gfbAVw620IuLzC_w9a6TUbzitQVePYOw4Ynl4yoZhZEugZZhDdJIC0nBFs7Vy8s1_sabTuJfW4SY9fxTQM1Nf-pqQ531kNW2_hdhSYJsjas3-1cSjsEVY6noqLQ85tfiBcrRWo8wJ0jWNVAziP3yILHq-K6o5Hv_R6JziKhfaQQe9a7Hu-RJFeu_LbR-EGB37BBL3HHGpTBRO2poP35NYtQDkbmKszvx_IBjYyDt2Wk4XrScSvEgfkN9w0G1AK0rKWYKnCmnrWlVNecJ-vmyEec2I-26qCE3Lc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : قدرت اسرائیل الان توی میدان جنگ داره معلوم میشه
-  هم به خاطر نسل جنگجوهای ما، هم مردمی که جلوی همه این چالش‌ها محکم ایستادن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/120612" target="_blank">📅 17:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120611">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkGOCgCtvc9c68nNOwqvgZ4cX2v5nyHeB87Tc3vxmX7RFO4XFNWBWpw5pgsGLN3KcXzHX692u2usEtWEgqpdSgz0HeJtXFyEjhABhphIK1IvAJGEKnBxL0pZyYk7_bE7VAMRITedHufUkV4OEWNJJJX1v34LKiCYoqfDoC3VRtOtMaK8bOL8fVmfhH1V34Ti5vRTMMe7lQQ9PDb_VmESSdHU23fFi2taOZQhWXZlXYSlta_HpfWOXCeV5rDVJl4a1Ro_fUgraFnfb_k88o3fC0IVebeSqaNPdMUq94qex9X3L2CcWOVxSLzqrf7HRFm2bX0uacuNID4n5zuprfE9dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حاجی‌بابایی، نایب‌رییس مجلس:
اگه تاسیسات نفت ما رو بزنن، نفت دوست و دشمن در منطقه رو میزنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/120611" target="_blank">📅 17:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120609">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RdOHLH4nOutjL49BAjKuO3fmZyulcysAjV_GuJSSafsJZSeOf4rV417HdL9iz32ixR6eySg3XZVypmNrP-pB903btL542gcMtN6Q2upM8vXzof8L_4XaLiSoUZoqsj8fZEdRvvQjaa9OjM-WiRC0BXY7cBGh18Pb9aluSegj6llsQI_2CJj8K3wmLaDH0a2Tj6GL7dQONozeVPhY3QwHpxGyPk8BaIG5uTfqsule1bbQUpPL3nnYhFFkNyE35SEadFbQ5CqANY2yMgfjw5O35Lyv2IfMd3foqsH0JKHBBmY2EjIRE4FgPh035xKrc0zEtvXlDD6Kl4PsYiblv7nd4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SLvfsUlNO4CUry8UeBtgryHIZbj6tS1mExqO1BeoU756ge8irhdL2HQf2KpMGjUKH61hDVbyQmOn0a98mzh069vInu1FjMQyGT3pb0V-6Rc4aqDNBhmz8ORD3Hl3kr0YvsG5t4JYwZd8UmsLPp3LT36Bm-VNf_E3eXoBt550UBTSax9zvogvOajpKZ8MHnNp--mCvBI00Z1CSNZq99qwWS_XCqnkvO8726HH774JQe-OaEWiWxsv5wVgb3qqMOrh12wxQMkKQSJecuzRIYKnNA9sIAmZ_MJMstMiJiZ3bE50xDgZyfkb5bM9sDZXSXLpTjdVpR0CvuaYExTiSM-dPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این روزا تو ایران دوست اجاره ای از همه چیز پر طرفدار تر شده، شما میتونین یه نفرو به صورت ساعتی یا روزانه اجاره کنین و باهاش تولد، کافه، سینما، خرید و... برین.
خیلیا پارتی میگیرن و برای اینکه جلو اکسشون پز بدن، یه پسر خیلی خوشگل اجاره میکنن و همراه خودشون میبرن.
قیمت اجاره با توجه به ظاهر و... از ساعتی 300 هزار شروع و تا 1 میلیون ادامه داره.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/120609" target="_blank">📅 17:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120608">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeeTPpzE9CXEdbyNDakU9g42i4owP0VHUJt97vf8efSm-_YmJNz8IR3jEu4eLHNkw0rgtwE-xT0vmxSgEwDRNadkDdxvFOhhNTnsx83NbdhN3pgq7ZzCZADHGGioKirbrSamXVQoNQD7gfcWyEpi1LERqYIhqCjaNjq4UGVFI2XSooD23q079eeLKCAppSD-PBLesXNHV3KpN8_XCsbeVMQz_9nE490MHHaDxpFl3GoiZk-7mGaARihVwZnvx_dcqiHD2HyBs-tvF-665LlXxT6aN4tidcfTLTno2j8PkXG1AeK747Mgz8XQFRKnS5k-J3ZbVRsvsnDTEp9fsFzBGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس با استناد به اطلاعات طبقه‌بندی‌شده: کوبا ۳۰۰ پهپاد، عمدتا از روسیه و ایران خریداری کرده و در حال بررسی استفاده از آنها علیه تأسیسات نظامی آمریکا در این جزیره یا مناطق اطراف آن است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/120608" target="_blank">📅 17:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120604">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kcsvCfswUpENClQzY4bM8_-men5dOAUOT6JkhxRmr37qZOeVDo-UOdWn5MEkBit6mFnKrmwvLTDX-5lA-ASovuy3mD3C-irXiu5uAcUUSumv2pbLhvuOq32nzoja3SL5SqyQeeGGK3Dk1msSl2P3gVPvmRmNc_w4UyTiMPYg0OwXpRsb54VqPuSbCmz7TdKM9u6grs3Cs2ZtC-zPIn3oQPT-E_a39EFn8Y-m96rCjY6Nc0IFgGptLtoXsourGeCisP0qYVFKXSAcQZrjhloaJWgLrw4IJPBOxz_R76Ov5O0K0OzfQ8-cK61c7cEY058_YK9X8lMxVw0gIjg6_sfJ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vd1xojK9lvavid6p_HL9T2apOmAKD6tx64JJzc4fHbw24oLw-BaJ9n3xrhptuC7Js83Qkabpco245eykoGGsX1UG6pKBUkPeFy70p_M7RKQDJnyiXw1ZE157UL0RC8NgPxkrdv2pkoW505crsw7lYChyJZAKki56sF6H4qFYg5EYQbbpQt1dMKLvfhi6gZaH5l5I5gPCEI_BwR3e052a2QuJgHOEam16kfRjZoTfHyXPu2dPQb5TJw9qlFlXGac2_7NtG97gq_DcdFTyY0HHIjNAgQvynPxRm6CuAi8qDPv53tWhrkM5K54flrBmpV91m6TFRIZcbtyhm9-JrUxzRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7x15uksSLAwyGCS3zLkENET3sK4nJfRgv2IlFsbrJAiorOCoiJYU36VMWBa1zIm-sPHN2Yxc_NQdL-ImVP6YC466c1vDuO4dzrDl2L8LyzPvYfQg0CRmkwfK6bX3RDcrzOWfwBkvt-7CYAwmbeLlhIJat50cFRdvCvNL_D_-Mh8_-EIsGpOUwiLknGkxRPLy_sBTYebZQj5-9BrhY6VwTDd2FRHPE8kVFR44fKTjOYLmWgmr0NT3n9I16ppEa3lfr_q8_2YEhrazV9Ig-RToocOhYnSuZvnG45OekSCFbpq1sbaykvHQ2TMy26j3yqoMCdqMEI4u74RHLz-XTLDGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4a5c89c4f.mp4?token=F7EoFCUXDVysqgNxzQ24SwY3hincfdVuLQJ4AjDyd8EAn5J8dOelPVB8EuEgsnZy4PFj8-xmHG4o1pnUhabLb_BBClAyh_8ocFopFS6TaE2u6ddAjEPED83-yPurxYbZOft12iRp9uFHhxbWSQSuUcWzhUQOVS8tIbWJxOBrwXODoLmNlYmenrOPVzOE0Ed2c6R-1xBQCgnSosxNTmiamxCpA8tmkowIVyYgpS5kdKMrAxrK2Du9AiYb6gO07j9BOpajY1qK2pEolTdo7fc-31kdwfKxCW12aatuihOaWQXbz8P_dxUVoCWpHUQOL-se3EXHX8d4Vq1kVhztwyLzmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4a5c89c4f.mp4?token=F7EoFCUXDVysqgNxzQ24SwY3hincfdVuLQJ4AjDyd8EAn5J8dOelPVB8EuEgsnZy4PFj8-xmHG4o1pnUhabLb_BBClAyh_8ocFopFS6TaE2u6ddAjEPED83-yPurxYbZOft12iRp9uFHhxbWSQSuUcWzhUQOVS8tIbWJxOBrwXODoLmNlYmenrOPVzOE0Ed2c6R-1xBQCgnSosxNTmiamxCpA8tmkowIVyYgpS5kdKMrAxrK2Du9AiYb6gO07j9BOpajY1qK2pEolTdo7fc-31kdwfKxCW12aatuihOaWQXbz8P_dxUVoCWpHUQOL-se3EXHX8d4Vq1kVhztwyLzmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حملات هوایی به ماروب، دیبین، البیصریه و صدیقین در جنوب لبنان انجام دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/120604" target="_blank">📅 17:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120603">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/883878a9d7.mp4?token=G133-M0271lR_1lsBlsLcRpziXvsgw3SrssI7GAfjW9rtJX483S1jdbPE6XW4UAdjt4nRnq3-M3oLfq6jzFFPql1CYxh2wsvKSAhg8u4t18ZCNtuJ4AwTMnUV5uWuek0L4Qv9FHisCFlKzZn41iizBW5wgpN8wB_Pe0G0SNGPXTaA2VneepHU-TM48lzhO0nNWZT41EWwiDVRXxde3h22oRh0Qc8fwaJ5_kUOoXd3tvn-97q3P-wqUqSAR0jqjFOYcVWx3GFPfHkZtywYplQwbvpPUKOV8lNjkEv0zjUgee9qTdZe_rUqRJ1WeEtPBSpQpGref8QBaqA0pGOO_jEqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/883878a9d7.mp4?token=G133-M0271lR_1lsBlsLcRpziXvsgw3SrssI7GAfjW9rtJX483S1jdbPE6XW4UAdjt4nRnq3-M3oLfq6jzFFPql1CYxh2wsvKSAhg8u4t18ZCNtuJ4AwTMnUV5uWuek0L4Qv9FHisCFlKzZn41iizBW5wgpN8wB_Pe0G0SNGPXTaA2VneepHU-TM48lzhO0nNWZT41EWwiDVRXxde3h22oRh0Qc8fwaJ5_kUOoXd3tvn-97q3P-wqUqSAR0jqjFOYcVWx3GFPfHkZtywYplQwbvpPUKOV8lNjkEv0zjUgee9qTdZe_rUqRJ1WeEtPBSpQpGref8QBaqA0pGOO_jEqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
یکی از معماران بستن تنگه هرمز همین اکبر کوسه از جناح اصلاح طلبان بود.
🤔
سگ زرد برادر شغاله، همگی دزد، تروریست و قاتل بودید و هستید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/120603" target="_blank">📅 17:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120602">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83c933a239.mp4?token=eVdQNYhvilEajpHeCU1hV3kl6GgfCbS6d-1oyJzLOp7E9TrbfHzto0jpmz9gTs7tf4w3MlR0Mwva8PGRHFmo49v27psVF8Bp7yDIAACpKun0CU5EPbm1YcqcU-B1qLq6770dk6mbX751YZRzpbgAcEn7vzX7nev-4HBPGWAjHpot51aRllSN-FjLfvZymIorQVTVts-U2VSIC05X0BpEg8wPCHALcTgzMT3I5_3y67UwGDOR5aKmXrNaRvPtRwRp72U5o2bD5z8xlq3KOzz-dd3S6tI2IIJD9TQr0ietDZHFarKkJnzfR75KyFJItKigSHSW_7gQyGGSQKFTd9Sv0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83c933a239.mp4?token=eVdQNYhvilEajpHeCU1hV3kl6GgfCbS6d-1oyJzLOp7E9TrbfHzto0jpmz9gTs7tf4w3MlR0Mwva8PGRHFmo49v27psVF8Bp7yDIAACpKun0CU5EPbm1YcqcU-B1qLq6770dk6mbX751YZRzpbgAcEn7vzX7nev-4HBPGWAjHpot51aRllSN-FjLfvZymIorQVTVts-U2VSIC05X0BpEg8wPCHALcTgzMT3I5_3y67UwGDOR5aKmXrNaRvPtRwRp72U5o2bD5z8xlq3KOzz-dd3S6tI2IIJD9TQr0ietDZHFarKkJnzfR75KyFJItKigSHSW_7gQyGGSQKFTd9Sv0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنوب لبنان پس از حمله اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/120602" target="_blank">📅 17:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120601">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vU6vpKDsV9NeVDkVW4hykmWVOvUxD7CDSZ8VAbdyUPn9hQp6x63BuZmCfQhKE_zhunivdrECzOZX9tmXnbG1SVNxlTMQLreCU14dXwQc6lqdkJxn3x5aRDOUowWyXC_xs7V5a8KxJAv5qB_Ul1OUFCbKxhlswJ4zvH1UUgBBBwhQSav16FYtGPSTxXjkta8wGpok8Rfi-guqvuX5KgxaWTNOTaoEsBvvGW6a54MZPyggCOzSb9gYSeGaBlCRVzt2Pdf6KDSFK-suDS_AnxXITuE0U-7lwnC7-IFYx6zrU0H8Vu972LVus_Z90kMDJRZ_6ocGk1ZaDiw7I0F0yBEwEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات پهپادی اوکراینی فرودگاه بین‌المللی شرمتیوو در منطقه مسکو روسیه را هدف قرار داد.
🔴
شرمتیوو شلوغ‌ترین فرودگاه روسیه است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/alonews/120601" target="_blank">📅 16:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120600">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWOJzlKudKOU2-yOXY_1efQXL2sEurAabjpTeh_jpI-nELmROSUSqFynjiAVs-takqLwhEqXJsFYiWH6lvn0--acomoLFjolRdrBjdFJecbDE5GJUFuM1guCpVOdWHNZM4JuOMzUnlJZo5dcbP5m1xB08lK2nDOyXrCz1G4Ps9Mm11rniyH8CQmS4_zzRLhLb9eJMyCHhJAm1cD6v2JFmb_ZjADYNCkl5r5vIoC_Hi6_yWq7k63jiw0JizFnpc86wm75Qp6irbX8U_c9KKK65OeF2TIBLCxirVQPLC9jVQSZuM1GgpKdg-dVOz8Bm5BPI9VTULONBLsqjOcgTLuaDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بعد از ۷۹ روز قطع اینترنت بین‌ الملل، پزشکیان با «سیم‌کارت سفید» وارد پلتفرمی شد که خودشون فیلترش کردن و گفت وزارت ارتباطات برای اینترنت باکیفیت تلاش کرده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/120600" target="_blank">📅 16:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120599">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/270f3391c3.mp4?token=UxTH1689o8FajRRTqQ-skx9tqXoCH9cyDa7tSk8N2ExhnsA0KHypJpqmqzpYtvwsh9Peb6qcKEo229eIhQACGvBswmEflKi_mAhYAJQ_WygSS4HEII-uxIZ1MZKtCHZ4qZd-V8ubAkzDQWef-HphJqZQ7w6KYFUtKKW_IhbH1Az3WKG8bgE_8CdToO6ZFrMkCxHgxKGFeTSHzfcN30oOyLffm9Hw-ydu0WaKNUXnNp-s4SkBmXcoPAg1G4eJHB5jF3Cr1yk9iK4qsxpp5jl_itjWIM_rLPP01B2-_do2avBqOBgpUTuxozlnaiEsHNxzX-uSRcIWIUYblQwGr_w3HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/270f3391c3.mp4?token=UxTH1689o8FajRRTqQ-skx9tqXoCH9cyDa7tSk8N2ExhnsA0KHypJpqmqzpYtvwsh9Peb6qcKEo229eIhQACGvBswmEflKi_mAhYAJQ_WygSS4HEII-uxIZ1MZKtCHZ4qZd-V8ubAkzDQWef-HphJqZQ7w6KYFUtKKW_IhbH1Az3WKG8bgE_8CdToO6ZFrMkCxHgxKGFeTSHzfcN30oOyLffm9Hw-ydu0WaKNUXnNp-s4SkBmXcoPAg1G4eJHB5jF3Cr1yk9iK4qsxpp5jl_itjWIM_rLPP01B2-_do2avBqOBgpUTuxozlnaiEsHNxzX-uSRcIWIUYblQwGr_w3HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سواحل دریاچه ارومیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/120599" target="_blank">📅 16:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120598">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc82c8bf8b.mp4?token=MparcYfNXapFsEebSIbeo84t6YnuCGsi9kNPMClAPUxugEB20_zW_WCx48os6bWrYk5P5rihE2EAA6YoU_gzqOxg6Q6_nkXZa0BAPmAdW1cKlhavGEXwLVD_da66KVlA5-GpD8_9VOU2Us_kLwyrb6L7o0v__3H0ZHxfTB3K_GyP4WdGdrNjBWfJ1kpGg478yZ8sxbO-ovjVAylvsNVdT00bNhjgg3agxswEowcSeKCzlsj0UZ6jeI0rqJs1px3fewXddmQMKyYDtMpz_uDP5pOkAzTBPYBY8y-FnRUgDzybd4GUbVl0jrbBgG6i1R4RCuvPrsYn8BjOvUHofEoYjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc82c8bf8b.mp4?token=MparcYfNXapFsEebSIbeo84t6YnuCGsi9kNPMClAPUxugEB20_zW_WCx48os6bWrYk5P5rihE2EAA6YoU_gzqOxg6Q6_nkXZa0BAPmAdW1cKlhavGEXwLVD_da66KVlA5-GpD8_9VOU2Us_kLwyrb6L7o0v__3H0ZHxfTB3K_GyP4WdGdrNjBWfJ1kpGg478yZ8sxbO-ovjVAylvsNVdT00bNhjgg3agxswEowcSeKCzlsj0UZ6jeI0rqJs1px3fewXddmQMKyYDtMpz_uDP5pOkAzTBPYBY8y-FnRUgDzybd4GUbVl0jrbBgG6i1R4RCuvPrsYn8BjOvUHofEoYjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
که‌ «خانم کم حجاب» هم دخترمونه! تف به ته اون حلق روضه خونت کنن عرزشی بی غیرت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/120598" target="_blank">📅 16:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120597">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
آکسیوس با استناد به اطلاعات طبقه‌بندی‌شده: کوبا ۳۰۰ پهپاد، عمدتا از روسیه و ایران خریداری کرده و در حال بررسی استفاده از آنها علیه تأسیسات نظامی آمریکا در این جزیره یا مناطق اطراف آن است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/120597" target="_blank">📅 16:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120596">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
گفتگوی تلفنی وزرای خارجه ایران و کره جنوبی
🔴
چو هیون وزیر امور خارجه وزیر امور خارجه جمهوری کره طی یک تماس تلفنی با  عراقچی در خصوص آخرین تحولات منطقه ای گفتگو کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/120596" target="_blank">📅 16:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120595">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزیر کشور پاکستان یک دیدار خصوصی با پزشکیان داشته که بیش از ۹۰ دقیقه طول کشیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/120595" target="_blank">📅 16:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120594">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e19970416a.mp4?token=R0z5KQEysu1juw8RQiuNIrda5VmVqyRbzfHIqzuP4vXBlk4kSV6lRfQjX2pBnE1Ao52OpjePxV8IMEl90DZOGtKKe3IFbjrOPMzHP50zCO7hBakjlLBU3iaWNRUdN7qVk3w8eISWUnIAnx1U8qzJdw9COy8P2k1z4QM-NQ4n-HG3IBp0O7NhkfNmjqcQ06ly7IsBNBTitgyyu0AIoEOnXfIMEnjtOlSV0Rr7YhvTmLPvhP1fJR21SkwgTiDRITxReNuf3TLoA4FvEN4GjdBP6LH1xR__YFlMupshWcf7ynFCFmgQMXhjjEMrI2d0FoVS_eYazzuphAMB7lBwSdJy_QOeH-IgypbdAj438CEIGb8UpdSpjEBaBJ04Xfipqo3kG1NsHLTf9YUjoS25CnKEmeJ1swYN0e-58k2QCG5lHSbuWof09-_-U0uWzasADW4wIS0-rmdB3Q4iAxIuMVKJPaziMuAlQ-zGNRY4ZZWaspXNqxEAGriadksZ2EuzLVd4v1dxJa-MI9YVzn7jhHW5_DQfutSCDqSWUw_2jDf8DHVNCeYjaV1usKko3Eq-iEK2LV-FvduEGAaucfkAoPyz8r348rqj1KWCwirgFo4jS4uTcR2V_O7pQjFwUWUZlJDgay2lNxURXL2CTujrKFgVGgoH7mpALIl011t62tWDu4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e19970416a.mp4?token=R0z5KQEysu1juw8RQiuNIrda5VmVqyRbzfHIqzuP4vXBlk4kSV6lRfQjX2pBnE1Ao52OpjePxV8IMEl90DZOGtKKe3IFbjrOPMzHP50zCO7hBakjlLBU3iaWNRUdN7qVk3w8eISWUnIAnx1U8qzJdw9COy8P2k1z4QM-NQ4n-HG3IBp0O7NhkfNmjqcQ06ly7IsBNBTitgyyu0AIoEOnXfIMEnjtOlSV0Rr7YhvTmLPvhP1fJR21SkwgTiDRITxReNuf3TLoA4FvEN4GjdBP6LH1xR__YFlMupshWcf7ynFCFmgQMXhjjEMrI2d0FoVS_eYazzuphAMB7lBwSdJy_QOeH-IgypbdAj438CEIGb8UpdSpjEBaBJ04Xfipqo3kG1NsHLTf9YUjoS25CnKEmeJ1swYN0e-58k2QCG5lHSbuWof09-_-U0uWzasADW4wIS0-rmdB3Q4iAxIuMVKJPaziMuAlQ-zGNRY4ZZWaspXNqxEAGriadksZ2EuzLVd4v1dxJa-MI9YVzn7jhHW5_DQfutSCDqSWUw_2jDf8DHVNCeYjaV1usKko3Eq-iEK2LV-FvduEGAaucfkAoPyz8r348rqj1KWCwirgFo4jS4uTcR2V_O7pQjFwUWUZlJDgay2lNxURXL2CTujrKFgVGgoH7mpALIl011t62tWDu4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاکس نیوز : ارزیابی غالب داخل ایران اینه که ترامپ ممکنه دوباره بره سمت اقدام نظامی
🔴
تهران عمداً داره سیاست «فریب و وقت‌کشی» رو جلو می‌بره تا با خریدن زمان برگشتن به جنگ رو برای آمریکا سخت‌تر کنه
🔴
دو مقام اطلاعاتی منطقه‌ای اینو بهم گفتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/120594" target="_blank">📅 16:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120593">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی اتمی: وضعیت نیروگاه اتمی براکه عادی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/120593" target="_blank">📅 16:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120592">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزیر کشور پاکستان یک دیدار خصوصی با پزشکیان داشته که بیش از ۹۰ دقیقه طول کشیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/120592" target="_blank">📅 16:16 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120591">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ادعای اکسیوس: آمریکا تهدید پهپادهای تهاجمی از کوبا را شناسایی کرد
🔴
کوبا بیش از ۳۰۰ پهپاد خریداری کرده و برنامه‌هایی را برای حمله به پایگاه آمریکایی در خلیج گوانتانامو و کشتی‌های جنگی آغاز کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/120591" target="_blank">📅 16:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120590">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fff2934367.mp4?token=oJ0U0ASDprvuXjLS8CbKXS4Z9No0IxIX86BoUAQN1HDZFoPKTWDluxcbVK-Ayn_gHOYNRQudhof1MmOlmy8CE97gRaJtkVJrP3eacu8X7Mm0vkImzB9nvvpcLv49ppaDoFrk0vICq1ju5IuOWMd0wsH97Er4SuzW7UuwU47Q_zsIJDZtGyrEvkBQLgkTA5FH8GqXGBlc_Dm_kBaR7MPbubblD4OF6je-EPqezJMD6ZFB_JAUMACrYs7zpv4OoNIau5g-pg2p_uCEAkNFLvn8dKpuvkV8-qtoRzGp3Oe-Jiqs0xgaezFUIbp_qpVgZjT6BwybLb7k_abN8SSlA3Z-Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fff2934367.mp4?token=oJ0U0ASDprvuXjLS8CbKXS4Z9No0IxIX86BoUAQN1HDZFoPKTWDluxcbVK-Ayn_gHOYNRQudhof1MmOlmy8CE97gRaJtkVJrP3eacu8X7Mm0vkImzB9nvvpcLv49ppaDoFrk0vICq1ju5IuOWMd0wsH97Er4SuzW7UuwU47Q_zsIJDZtGyrEvkBQLgkTA5FH8GqXGBlc_Dm_kBaR7MPbubblD4OF6je-EPqezJMD6ZFB_JAUMACrYs7zpv4OoNIau5g-pg2p_uCEAkNFLvn8dKpuvkV8-qtoRzGp3Oe-Jiqs0xgaezFUIbp_qpVgZjT6BwybLb7k_abN8SSlA3Z-Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نارندرا مودی، نخست‌وزیر هند، به گوتنبرگ سوئد رسیده است، جایی که قرار است با اولف کریسترسون، نخست‌وزیر سوئد، و اورسولا فون در لاین در رویداد World of Volvo دیدار کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/120590" target="_blank">📅 16:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120589">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
نیروهای دفاعی اسرائیل هشدارهای تخلیه برای ساکنان ارزی (صیدا)، مروانیه، بابلیه و بیساریه در جنوب لبنان صادر کرده‌اند، پیش از حملات احتمالی اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/120589" target="_blank">📅 15:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120588">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
بلومبرگ: امروز یکشنبه هیچ گونه ترددی در تنگه هرمز ثبت نشده است
🔴
تعداد کشتی‌های عبوری از تنگه هرمز روز شنبه به ۱۰ فروند افزایش یافته بود، در حالی که در روز قبل از آن ۵ فروند بود
🔴
تردد بارگیری تجاری از طریق تنگه هرمز تا حد زیادی متوقف شده و حرکت محدودی تنها برای کشتی‌هایی انجام می‌شود که بیشتر آنها با محموله‌ها یا شرکت‌های مرتبط با ایران در ارتباط هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/120588" target="_blank">📅 15:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120587">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
نتانیاهو: شش سال پیش در یک جلسه کابینه امنیتی در مورد خطر پهپادها هشدار دادم.
🔴
دستور دادم تا راهکاری برای مشکل پهپادها و هر تهدید آتی پیدا شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/120587" target="_blank">📅 15:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120586">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
یک سرباز ارتش دفاعی اسرائیل به شدت زخمی شد و یک افسر به طور متوسط پس از انفجار یک دستگاه انفجاری در جنوب لبنان در طول شب، به علاوه یک افسر و یک سرباز دیگر در همان حادثه به طور خفیف زخمی شدند. طبق بیانیه رسمی ارتش دفاعی اسرائیل، همه آنها برای درمان پزشکی تخلیه شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/120586" target="_blank">📅 15:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120585">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ادعای نیویورک‌تایمز: اسرائیل حداقل دو پایگاه مخفی در صحرای عراق را به‌طور متناوب و برای بیش از یک سال اداره می‌کرده است
🔴
آمریکا به عراق دستور داده بود که توی دو تا عملیات توی ایران، سیستم‌های راداری خودش رو خاموش کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/120585" target="_blank">📅 15:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120584">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
کانادا اولین مورد ابتلا به ویروس هانتا را تأیید کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/120584" target="_blank">📅 15:21 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120583">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
رسانه‌های عبری: نتانیاهو امروز با توجه به تحولات و تنش‌های منطقه با ترامپ صحبت خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/120583" target="_blank">📅 15:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120582">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
اسرائیل بیشتر از یه سال دوتا پایگاه نظامی مخفی تو بیابون‌های عراق داشته برای عملیات‌هاش علیه ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/120582" target="_blank">📅 15:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120581">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-jEsoORQVuf4nE4UoEf1cNjJ1fTh1ggQVfSU6PAC9sR1PNM7390T5ZwYplTogW4_I5FoHd32xhM-41WTdescJ9fEgrSDUBVDJluZrSwmnSiPeOrExLuspI-6L5_iVJGYVR2Wa9LnToIwch-fLVceUyX7dNdenIHt8EvLhe7kTxY-ZNRVQ4m5o7N2iv0yXhroFLSi8D7gPgqJLBHI1LEZcYOgOIIuxJW_gGggA4Vnav2-PlfeA8Kj4solTdMjQv04gNVbiBLlwxQSEMHycOBsABRYiWpW50h3A7bJbrpdptOFCQePOxT7LKw2pLj9xbhz88Ux0pZ1B1w-rSocCTOlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی گیگی
9️⃣
8️⃣
1️⃣
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
💤
این تخفیف فقط تا ۱۲ شب فعاله
💤
⭐️
@Napsternetiran_bot
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🔶
@Napsternetvirani</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/120581" target="_blank">📅 15:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120580">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ادعای نیویورک‌تایمز: اسرائیل حداقل دو پایگاه مخفی در صحرای عراق را به‌طور متناوب و برای بیش از یک سال اداره می‌کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/120580" target="_blank">📅 15:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120579">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
نتانیاهو: ۶۰ درصد غزه در کنترل ماست، برای هر سناریویی با ایران آماده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/120579" target="_blank">📅 14:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120578">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
دبیر ستاد ملی جمعیت: اگر با همین شرایط پیش برویم، در ۷۵ سال آینده جمعیت ما به ۳۱ میلیون نفر میرسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/120578" target="_blank">📅 14:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120577">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
هاآرتص: دادگاه کیفری بین‌المللی حکم‌های بازداشت مخفیانه‌ای برای پنج مقام اسرائیلی، از جمله سه سیاستمدار و دو افسر نظامی صادر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/120577" target="_blank">📅 14:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120576">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
عارف معاون پزشکیان: ما تا حد امکان قیمت کالاها را مهار می‌کنیم و بقیه آن به مسائل بین‌المللی بازمی‌گردد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/120576" target="_blank">📅 14:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120575">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
روزنامه Dawn پاکستان به نقل از منابع دیپلماتیک در اسلام‌آباد: سفر اعلام‌نشده وزیر کشور پاکستان به تهران در چارچوب دیپلماسی مستمر اسلام‌آباد برای احیای روند متوقف‌شده صلح میان آمریکا و ایران انجام می‌شود.
🔴
این سفر برنامه‌ریزی‌نشده با هدف جلوگیری از فروپاشی کامل مذاکرات صورت گرفته؛ به‌ویژه پس از آنکه شتاب حاصل از دورهای پیشین گفت‌وگوها در پایتخت پاکستان به‌شدت کاهش یافته است.
🔴
انتظار می‌رود وزیر کشور پاکستان، در جریان این سفر با مقام‌های ارشد ایرانی دیدار و گفت‌وگو کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/120575" target="_blank">📅 14:16 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120574">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rL8M1IC5szziD8T9MuzwcjbSVZsG2bsoNLqIYvSQ3GNypRK-LrgDINmLbUyU4T9oQ052PJJzRKm4owXSyFvIMUus0nTdRh4mmGceqqRMpHNiyVwaeH8UrBEf-gpB96uoN-XWJSUM1iUI3KDtmHtFmAJ4DMikGCbnMSTE6MHW90tgIDvqeUWoyKKvO9s_E-y2ditv5OroFl2O2bKoWRD52kU8OiH5Aqr67vKz-VvS_GQJeLp9GNF9N2OM8R9HkLDccLRP6EWHbaTMOYBYtoxLGUMivwXx3rjzPKW6iLU6qUW6qoxQ1lZRoZ-5D-hM3djQb6NInyOJmIih3nf3LNsUeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور در شبکه اجتماعی ایکس نوشت: ‏در روزهای جنگ، فرزندان ما در ارتباطات و فناوری اطلاعات، شبانه‌روز ایستادند تا ارتباطات و خدمات حیاتی کشور پایدار بماند. دسترسی باکیفیت و پایدار مردم به خدمات دیجیتال، بخشی از آرامش، پیشرفت و حق زندگی شایسته مردم عزیز ایران است.
🔴
روز جهانی ارتباطات را تبریک می‌گویم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/alonews/120574" target="_blank">📅 14:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120573">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
اقتصاد اسرائیل در سه ماهه اول سال ۲۰۲۶ به دلیل جنگ با ایران ۳.۳٪ کوچک شد، طبق گزارش کانال ۱۲ اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/120573" target="_blank">📅 13:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120572">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
گزارش سی ان ان از کابل هایی که زیر تنگه هرمز خوابیده!
🔴
مدیر تحقیقات شرکت تحقیقاتی TeleGeography، گفت که دو مورد از این کابل‌ها، فالکون و گلف بریج اینترنشنال (GBI)، از آب‌های سرزمینی ایران عبور می‌کنند. این شرکت اعلام کرده:کابل‌هایی که از تنگه هرمز عبور می‌کنند، تا سال 2025 کمتر از 1 درصد از پهنای باند بین‌المللی جهانی را تشکیل می‌دهند."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/120572" target="_blank">📅 13:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120571">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
دفتر رسانه ای ابوظبی : یه پهپاد نیروگاه هسته ای برکه تو منطقه الظفره رو هدف قرار داد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/120571" target="_blank">📅 13:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120570">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
امارات اعلام کرد: آتش‌سوزی ناشی از حمله پهپادی به یک ژنراتور برق در نزدیکی تاسیسات هسته‌ای براکه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/120570" target="_blank">📅 13:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120569">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax7Cm-EIQet44QweJASmnEmXnqhB2707FLBZnwov1dPBuDflaFuOZkkd2P1JmSnXqIAcd4FCjxX4wxrItbEl_4K5SChLTNcScLBz_fhAhWriQ9lh-cqVfTnXh8QbJa730OMHDc_i-2CFJjRRLyJVW0PnsYtBcneN-NU7hJjAT_QFBDm1-D5JKPWSBEk1EnA7VvU4twtcuvXg4hdIf2Ci4jC-dosQaUWbqANM1j6SN337lcA1hE3r_lHL6--P18DO1DlyXZG35-bDt9H5C6Oa-tC53Ydl8qQQlF02-bIsgVdfvqOJD8FzqeHEXE42dcDYQkmjMqEaiv_B0AsQ5LtEbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جلیلی سوم!
🔴
پس از سعید جلیلی در سیاست خارجی و تحریم و قطعنامه؛ پس از وحید جلیلی در صداوسیما و سقوط مخاطب و مرجعیت؛ یک جلیلی دیگر هم چند سالی است بر زندگی شهروندان سایه انداخته.
🔴
رسول جلیلی، عضو شورای عالی فضای مجازی و مدافع فیلترینگ؛ کسی که اینستاگرام و تلگرام را اف-۳۵ و اف-۱۵ می‌بیند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/120569" target="_blank">📅 13:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120568">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
دفتر رسانه ای ابوظبی : یه پهپاد نیروگاه هسته ای برکه تو منطقه الظفره رو هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/120568" target="_blank">📅 13:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120567">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
پزشکیان: نباید با آمار غیرواقعی جامعه را ناامید یا شرایط را عادی جلوه داد؛ اگر اینگونه القا شود که دولت عامدانه در مسیر افزایش قیمت‌ها حرکت می‌کند، ناجوانمردانه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/120567" target="_blank">📅 13:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120566">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
برخی منابع خبری از انفجارهای مهیب در پایتخت امارات خبر دادند ولی علت انفجارها مشخص نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/120566" target="_blank">📅 13:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120565">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQIsISRzSxoR1ABUSByeb1D0gzJl_YxeJ8qb0vvQv_SZi8-DN7yiPFCthh5bfQS8CLStpjUJAPUxlZxoCPVs118xxw3TRbl6QkkrG8rOLTtB_FMRKqGMoF5f6TWVYtnx7_SZxYRbqakxqmxPegzzS5NZrU-7JDDPUmBbiSc6rYDOfwYXFsRilnvYvC8lLzhDlmNHR3evi16J3FVEhGwzO8zOjGjBBxGTuze7bc8o9p0kcNllEnjbkzp4ila3d9qfexFfJqAXtk3uMLryYsSuzu02lzcAxyNaOKeOKijwTIzaK6MkaozCxrV7Kq1stUODU-tx0ibQvtu-Kx0ktR-tSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نروژ مرفه ترین کشور جهان تو سال ۲۰۲۶ شد نروژ این جایگاه رو بخاطر درآمد عالی،وضعیت خوب مردم،آموزش،ثبات اقتصادی و اعتماد عمومی بدست آورد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/alonews/120565" target="_blank">📅 13:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120564">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
حدود ۳۰ هزار نفر در فورتزهایم آلمان پس از کشف یک بمب ۱.۸ تنی منفجر نشده مربوط به جنگ جهانی دوم توسط کارگران در حین کار ساختمانی، تخلیه شده‌اند.
🔴
مقامات یک منطقه ممنوعه ۱.۵ کیلومتری ایجاد کردند زیرا تیم‌های خنثی‌سازی بمب آماده خنثی‌سازی بمبی بودند که طبق گزارش‌ها حاوی حدود ۱.۳۵ تن مواد منفجره است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/120564" target="_blank">📅 13:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120563">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
نتانیاهو قراره ساعت ۶ عصر به وقت محلی یه جلسه امنیتی محدود برگزار کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/120563" target="_blank">📅 13:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120562">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNDsFWNQwEN4Ix8E5-AEiDswBtzEJ67rXFPHrNyCiipP1rrAttb5eJUdx_s8tw1sZlZbVbidr_3Rv-PQCvRC34wXNAdAuuwgTb6kYhGv1zYvq39gQJcmtDXz8YqtCNCR8RzWXS3u1nd5Mj2uIBCdu6NuHAt4ILoCVX2OlvI6zdv9Am8S7cNwjmN2U_cNZJyY8QsXHqMqxoOjUs9VDmCylpGn8AIPCW9gqyjM94xDPro6WGg-5nWWsIlkmen_MVjMONokvBRms_h0ygXTbtDfDdb6YvsabKEvYwf1bIuBB6mvmWFkWabKad2vjzlq4lE__Q6sCgHuWFGWpP8bUeFsfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این حاج خانوم که تو خرابه های غزه داره قدم میزنه اينترنت پر سرعت داره ولی من ایرانی نه
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/120562" target="_blank">📅 13:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120561">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزارت کره جنوبی : کره جنوبی و ایران به گفت‌وگوها برای تضمین امنیت تنگه هرمز ادامه میدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/120561" target="_blank">📅 13:16 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120560">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c08a1dc7e.mp4?token=SDZTRntUKfBGg6ipXSkN_LVnSgpU8oiLbHcNuSdjPBCHd-gysSkuIX1spFgonvkJ1U0gfQDDGeYbkL_CFhRgMKccRKEPLOekKEGnu1OWsSxUBGC55oqTPk0CRc9RfkED1PuA4HaaKP2EcS7_kIk4T5B1YKalXxALenyfnQUAPVt8GIsOO7ikL_wEqfTdP-DNq9BQUUXXdcz4hYQTVUWfBFSYpOGnTUzqgWYexcHzinaqkCQzMomYBUnnU1cZzeKtXJd3IpLgtARpqaNGJGJHe-gqgQ0xGlLyh3AIx09ui3vE_m1QaE1nQzl9T7KwIr7R8w4r_bzix4dtPwDT9k86bTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c08a1dc7e.mp4?token=SDZTRntUKfBGg6ipXSkN_LVnSgpU8oiLbHcNuSdjPBCHd-gysSkuIX1spFgonvkJ1U0gfQDDGeYbkL_CFhRgMKccRKEPLOekKEGnu1OWsSxUBGC55oqTPk0CRc9RfkED1PuA4HaaKP2EcS7_kIk4T5B1YKalXxALenyfnQUAPVt8GIsOO7ikL_wEqfTdP-DNq9BQUUXXdcz4hYQTVUWfBFSYpOGnTUzqgWYexcHzinaqkCQzMomYBUnnU1cZzeKtXJd3IpLgtARpqaNGJGJHe-gqgQ0xGlLyh3AIx09ui3vE_m1QaE1nQzl9T7KwIr7R8w4r_bzix4dtPwDT9k86bTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حاجی بابایی، نائب رئیس مجلس: اگر قرار باشد به نفت ما آسیبی برسد، کاری می‌کنیم که آمریکا و دنیا تا مدت قابل توجهی، از این منطقه نفتی گیرشان نیاید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/120560" target="_blank">📅 13:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120559">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9627342f.mp4?token=XlavYMrpNzk-h1skdbOFaaftLcls3E2SzYdfdNhZHvA53Otxya6a0lF1RNLNFwqOlX7eadOrj_jQA1Ar2bdBLWNr7JTfhRIHzjAhKX5aWZKki2FhfpNmMDqNztZy_WZBoKzst5Mmo9O7vTutx2VS_gplwiusQy1JN3-b_q2GiqFJlHhN5VYhPTFdGb7VOdhvNlYtPznyhRE-X2em9BNTlfM6TEcQIQMj_Xl2-oLaq3fXtoJ3bwdEJd2OY91OHYcSIkqTgxeGbVC097Ac-W1pVYB5P8lAHl_J50El20OZ00OODic_bNrJbubjpAW3ied5Qi-o8apF40SwtTgBnjmmIoPqEspAmFwQS5ysUAz1LJXpN5oWwC0gQRuQxxBbEALbI4v6Asw1-WkfNJzD1u-P3lv5TNlO1PKSmQTZo0r26iSUhEjik7wC24tcAJvMyEGr7WWIhD3yFbXxCVBq31o-I89Q-sIMqLkt4NjuOTpMqC252jAH4sjeVe20IloIlhx1QV8w6B-3Jyv_BiueddSGc9IcLXNr-Yo5VufT45R7PbYq8IqaKWoAsdns-3_iRWfzMBccNvhOdtvV-hWszeP25yeCtlMZu7cHwUp76g8xS3vpgtP_mlqxEBLGkhBPsg2dMAFvQ1JufBQvuvRQEHQvEUg1PStPdYyyveY3y_tQr6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9627342f.mp4?token=XlavYMrpNzk-h1skdbOFaaftLcls3E2SzYdfdNhZHvA53Otxya6a0lF1RNLNFwqOlX7eadOrj_jQA1Ar2bdBLWNr7JTfhRIHzjAhKX5aWZKki2FhfpNmMDqNztZy_WZBoKzst5Mmo9O7vTutx2VS_gplwiusQy1JN3-b_q2GiqFJlHhN5VYhPTFdGb7VOdhvNlYtPznyhRE-X2em9BNTlfM6TEcQIQMj_Xl2-oLaq3fXtoJ3bwdEJd2OY91OHYcSIkqTgxeGbVC097Ac-W1pVYB5P8lAHl_J50El20OZ00OODic_bNrJbubjpAW3ied5Qi-o8apF40SwtTgBnjmmIoPqEspAmFwQS5ysUAz1LJXpN5oWwC0gQRuQxxBbEALbI4v6Asw1-WkfNJzD1u-P3lv5TNlO1PKSmQTZo0r26iSUhEjik7wC24tcAJvMyEGr7WWIhD3yFbXxCVBq31o-I89Q-sIMqLkt4NjuOTpMqC252jAH4sjeVe20IloIlhx1QV8w6B-3Jyv_BiueddSGc9IcLXNr-Yo5VufT45R7PbYq8IqaKWoAsdns-3_iRWfzMBccNvhOdtvV-hWszeP25yeCtlMZu7cHwUp76g8xS3vpgtP_mlqxEBLGkhBPsg2dMAFvQ1JufBQvuvRQEHQvEUg1PStPdYyyveY3y_tQr6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پارسا تاجیک، مهندس شرکت «ایکس ای‌آی»،  درباره روند تغییر پرچم جمهوری اسلامی به شیروخورشید در شبکه اجتماعی ایکس، توییتر سابق، توضیح داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/120559" target="_blank">📅 13:07 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120558">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وزارت نیرو: تغییر ساعت رسمی بیش از هزار مگاوات صرفه‌جویی در مصرف برق به همراه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/120558" target="_blank">📅 12:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120557">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83970d0297.mp4?token=uQ_PmfpGp1cRWURkMeKh1MD8w1A8JUTetzbo9nXcnLasTPvhBr4EjzjFTodDewNhhLDIenjMjgl5OiU41jGiFQk6d7dUS9_2nKiF4UNRwwniW8VXOZE6XBYAfbXfeTVVcx2QyNHX1UXY2uAyF6BVTRUVQRpMLHN-96Y-Ko0u5htaZ0o61HL2XQIuEMUTYp_4sjoDchdirbkXYv_QKpetm_ozFC-9rVD4MjXbtCq64x4H3z2csBJytEsunLMeoQwEf_tE_mywC7nlqr-xK4QG2J5xGhcarb9IfmP1f4k4fpQmU-QTMzGBokqN97jRcPTMamwsYco8FoUtWw_OGVlxdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83970d0297.mp4?token=uQ_PmfpGp1cRWURkMeKh1MD8w1A8JUTetzbo9nXcnLasTPvhBr4EjzjFTodDewNhhLDIenjMjgl5OiU41jGiFQk6d7dUS9_2nKiF4UNRwwniW8VXOZE6XBYAfbXfeTVVcx2QyNHX1UXY2uAyF6BVTRUVQRpMLHN-96Y-Ko0u5htaZ0o61HL2XQIuEMUTYp_4sjoDchdirbkXYv_QKpetm_ozFC-9rVD4MjXbtCq64x4H3z2csBJytEsunLMeoQwEf_tE_mywC7nlqr-xK4QG2J5xGhcarb9IfmP1f4k4fpQmU-QTMzGBokqN97jRcPTMamwsYco8FoUtWw_OGVlxdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله‌های شدید ارتش اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/120557" target="_blank">📅 12:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120556">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سوپر اپلیکیشن بله مجدداً از دقایقی پیش با اختلال روبرو شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/120556" target="_blank">📅 12:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120555">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVcA0G1eaW4FpGUDo6H-9g3j242fX6l9FTqhFW4HdefAMjNLSHFJ2MuovKXFSLPzRoLTGHAi5esIhLBqKhP4YomznlNmv86B_irXXQVY5JVLEaZrlz0JeNLgZfYdCOsxUZXorAdVSsCiAJ9H-H4ceSz8iYj0sHYI7zEpwb9i3C6OyyHRSrMca4Z7nyv0GHqYyH410K6NDSXTjMmScgv2QH8PrtUBHE_LGfeShV9qGWDH5dOWAvg_hDFK9wzzRToNs_MnEviWXO6XhAGkEgHf00syEWE5wvUyLhzPBrgzGhbJdEI9P9fBX_qlKV9GUJEDD0Qc_L3JUXAqtj1mbIA1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلهکی: یکی از کشورهای منطقه هشدار شروع جنگ را برای دورماندن از تیررسِ ایران، به تهران منتقل کرده است
!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/120555" target="_blank">📅 12:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120554">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
جزئیاتی از درخواست‌های آمریکا از ایران در مذاکرات
🔴
براساس شنیده‌های فارس از پاسخ آمریکا به پیشنهادهای ایران، ۵ شرط اصلی واشنگتن به این شرح اعلام شده است:
🔴
عدم پرداخت هرگونه غرامت و خسارت از سوی آمریکا
🔴
خروج و تحویل ۴۰۰ کیلوگرم اورانیوم از ایران به آمریکا
🔴
فعال ماندن تنها یک مجموعه از تأسیسات هسته‌ای ایران
🔴
عدم پرداخت حتی ۲۵ درصد از دارایی‌های بلوکه‌شدهٔ ایران
🔴
منوط‌شدن توقف جنگ در همه ساحتها به انجام مذاکره
🔴
این گزارش تأکید می‌کند که حتی در صورت تحقق این شرایط از سوی ایران، تهدید حمله آمریکا و اسرائیل همچنان پابرجا خواهد بود.
🔴
کارشناسان معتقدند طرح پیشنهادی آمریکا به جای حل مشکل، در پی دستیابی به اهدافی است که این کشور نتوانسته در طول جنگ آن را محقق کند.
🔴
در مقابل، ایران انجام هرگونه مذاکره را منوط به تحقق ۵ پیش‌شرط اعتمادساز دانسته است که عبارتند از:
🔴
پایان جنگ در همهٔ جبهه‌ها به‌ویژه لبنان
🔴
رفع تحریم‌ها
🔴
آزادسازی پول‌های بلوکه‌شده ایران
🔴
جبران خسارات ناشی از جنگ
🔴
پذیرش حق حاکمیت ایران بر تنگه هرمز
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/alonews/120554" target="_blank">📅 12:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120553">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Os8iicC7q6quuQltaHglvJgEP3k2hdbxoYalbp2U9l85CNnTYCuQ_CE2KKXTJA6PmSgIeiPwBA7GYwB_yBde0_UPPT8uGCsiwk-ZSdQ1o124nenCsNxUO8s_cDXvF2mjWDtHbaRsrqL9YrZUpvCjaJ1VGEjGallAS3-JYwKek2iv-CixeGvHhXAJ2Nunc-ZP0G_X-GfMaMlSguhjC2FocPQ-GjUaX9KidY6M0vrxOAgAuDmNpZL5xWJjtoE9mbYqM3f0vzmpbKnOrSKwig6V9f7_WC3oyGGeigFv3YWHyxd98iIuKpC5-aWqN0hGvcddZOZwlX-O2e4HwHqhiMn5gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست ترامپ تو ثروث سوشال : یه شب بزرگ تو سیاست؛ از همه متشکرم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/alonews/120553" target="_blank">📅 12:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120552">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBuSTV5cncXaycxC6mwncTkD1JkARasnZHLTEjaKKfix5G6NB8gVYUGVYHCzB30X1BNx9ytLDDTkUYJ8B6DOBaxufnT3VZMxevnpC61ys-RWTSaf92yfDZo0CFwfwC4xBPyiKLl8zJz2hqJnZVYfhjm3fICo3Ozt6G51keIbWUItn-_iXZaY-fUBuADXNe_6Sc2wTkmcCYigk1Lo6tBVSesHl0SENbGWyZk7xeweAC9DqmzVyvOa9fSUJzchkNQ8ZnYLBIYi92OZG3YLTmTkexnchhHIo8JEGdrUxhEcrY3SE__Pu-Wl1fmZy6FcCQ3kZqwNMUVldnNdoVKgvtkaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا تو اصفهان برای خانم‌های بی حجاب ابلاغیه دادگاه ارسال میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/120552" target="_blank">📅 12:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120551">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
وزارت کشور عربستان: برافراشتن پرچم‌های سیاسی یا مذهبی و سر دادن هرگونه شعار در مکه، مدینه و اماکن مقدسه از جمله مسجدالحرام، مسجدالنبی، صحن‌های آنها و مسیرهای منتهی به آن ممنوع است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/120551" target="_blank">📅 12:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120550">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pJCoV_hplISPIgFQj9NzNmXy6p3uY2uU-zlAvQxmJY8SlFVdamFL2JsFyP69-dctzohc_0u0aD7r1QT5nU6oeq4TqzdfWTXvyxrQCJ-4-abYTqjmyuNnnluo0YjUYsR5EYNGk9wqHTJYrifq6rBqyBJGRuYMFhp-BSoDegXJs_fasWP1cZIOcd297YKcng5gmnTqoMT-tflaLAfLgbkcjhRJp2ZdywDR8CzL-2VlycC-t__A6y6avUoCop5x06V09WWbfyn2KLzrcUG6eUJCY4Zk3aO2c-SCD5JDUhyi7dRFquEQd2m7sAib3PieCqBFKps2cfhU6eHlEUIdIPbVMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
💥
اینترنت آزاد و رایگان
🌐
🚫
تنها جایی که کانفیگ
رایگان
میزاره
⬇️
⬇️
@NetAazaadBot
@NetAazaadBot
⚠️
هر ساعت 100گیگ شارژ میشه، رباتو داشته باشید تا مطلع بشید</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/120550" target="_blank">📅 12:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120549">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YldQrQWrZ8JIf9A2EzkJ5XfA1WlSLYU-TQYSYoDYVveK9cyBLsybTCefeaQrpFHpoaqWkUo_UUA_F5ZeHdAC8Iqk86p2Y_MGd-ugPJsfiH0U7Dwfe1KqhYzrjRK3yV9Hy92gsxl9AD1FBWMGHqZ287vxEhF1lMEJzmsEtE41XoD3CTR7ROIKy5e9Yeh2P9mtwrvPdG87Py4HEbQbW2iNERLoiaVLuggtdgbzKaFLvbVK__h2EpL2xNJS8g32lCJ5vWTanRTZMWNRXSRcDEqlNF3wYr8X06KHmbJfsJM_z6yuIUQTJGIsGSDXG5hwcoDte1Rh1fFrLlVmILp6BztSFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میزان: دادگاه «صادق ساعدنیا» برگزار شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/120549" target="_blank">📅 12:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120546">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MGzgjkcY0M3m2IAGLC9ZdiD1A-bkRXqFgwQG3LxFfvk-2yIuf1ko9rZzinxy1jjxU-UZpS1muJTncI3n79618Jd02KIAJ-idEw8NjK9qjnS9AIK67GAVaVFiXPUPI7s4Tgju_adwoL4vNK35RSGbPqtTsyASmt_EUl7Mj7GfBFlZSpUJdxWUKsHtkvZ9e1NCg3OsyEL3sJrvEGZ2TYAB1k3rOSjsmKTNa7YmPVd25xJFiQ76RHNlAD8yzYT7ImQSP0jcpeMiUTMp-BjC1XLuvq2SiYtDvufsXL_C9JFsOJSYqFVq-f1VSwkj_F7hcAPCfNRHbBiqQgOJMf1U_IYIuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5UWQqL9LdoTY06bDMP0LcWJqTNy1BUIbKjV3mIHCeWFr6iEDSYl30C9o5xNVwnENsqHqNnWBFDf6q8kpKXY2BjkAewh_kqRRc-rSzsEo5cdITIvdAiItRNbY_JKxL2S7wV4weXxgcUyzvEXasDAIUZp2NoXb_Q3IV2uO5EtPxAc6hM3acS2B6c3CwOBg8QdzZnmU8t7yVJSg6jRGUp7sITm2Lp_Ymp-21CspOSTAesDlpeSf3gnavTZCrlA8cRxVy8w_VZGw3XD9oGmTrCMIEiRtzrKvcUKmahTnL8572ttQQFgsQaKBJaRGucDrDto6EFdo3RZOf4N7BhKDfBu3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3gPsxpeTX_ZGEHclvIq0Rb_kFT5pkLrgqQ60ErfGGoeQFjZy5GkzH6eM72YnnlJuvsMlLRSV_618SZ8LQlPEo4fZjTesRLdQyeC0YhdP-IPV7x5prWgPtUntGh0XfWNgz5sikVnyfdOM4YcNKwU7PcKXQdqHU60EVCWf8hudPZ2ELOGci6PxSyd2bFEXE6f4Bu0W9UtXQPQmkdpMPuKSxDx4HbamAsxzFV_knznhbYTrOyjk6-sUriw16jaodhqF5F3owM3Dbj_CJBYIqKVMFSKXjLYbLR-0EbbZPaLTGI9YOLLA7yIErGuMlQQNc9QMffIXUB5SXQPszwRcXE15g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصویری از نصب مسلسل ۱۲.۷ میلیمتری گاتلینگ چهار اول نصب شده در دماغه برخی نسخه های بالگرد میل۲۴ با یک سامانه دید حرارتی در روسیه برای مقابله با پهپادها ..این سیستم بیش از ۲۰۰۰ گلوله بر دقیقه آتش می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/120546" target="_blank">📅 11:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120545">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCQL5hcvtI20egbxYuNiALfrM4MV08fAiadQ2ptMGM8oJg-FwN8v5umSNzJ12tmL_YSM61krS9j9WZT9kGUfKtCWgk2G-FXYV3vWzxedU9AUjBQ0ieRkuLnyXK-vDRpUjkK1uWSkA1aymU2u2whjBCmanPx9m_ERLViLhm-rAc4MTuCZ0vS-HewWnUrJhw7Df3ax9K_vHl1BPEam5idfJzhM8ONuE8fjWsUS7X1GLU-hA4y3gqmM5kCl9JlTDd4d8L6flggBkCxVDZK8XEdNNiFA02Uu-_66vA9cpNWmhYuL7C6StWaWpVxSv6muA5XN-jDHvzqinroG6RPiBfv4DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از چند ساعت گذشته بیش از دوازده فروند هواپیمای ترابری راهبردی C-17A گلوبمستر III نیروی هوایی آمریکا در حال ترک خاورمیانه و حرکت به سمت اروپا هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/120545" target="_blank">📅 11:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120544">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
فارس: محمدباقر قالیباف، نمایندۀ ویژۀ ایران در امور چین شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/alonews/120544" target="_blank">📅 11:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120543">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
معاون شرکت مخابرات ایران: دسترسی به اینترنت باید برای همه مردم فراهم باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/120543" target="_blank">📅 11:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120542">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAfJWAFnfPhDHpPMd9eFU76oXElfaOBxV6jTJBQ8GzibK8nIlRZyUsvgAkTxdiHi7VcsQPPR-IAKMlJIsKKFtM7Bb6AmDSc4wGZh3y30L2c8hjDS8ybrliZhxJGumKCUXecbcwC62yuWJOmQnF6lmmCVPSQ4Om9p9FnKWi2GIlgAhJQX3yi9HD_7skJdtCwbHXm6-sC2yXBYokQl5RF0CV8ACKf9WFynLwheUGjiRqFDc2tI7qxqYi6yy4qCqqdtRUnVN0I9T1NwHsWv8FnhjvKcRjYOsHI5owMYViHlrmTOSU06fTrZKstRj0xWPg827oJqAiFZH5P2RpcWMw3ksA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری لو رفته از گلشیفته و مکرون
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/120542" target="_blank">📅 11:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120541">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fy0UlrjiWbsY5tJzWiQ8UdnxsIPi3JQWFD9Pj3CCMdtdG2Y0WdSHt7GAlegYPl8_PUYSg_pQm68GlCzje86Anr2Hoq-WIRtw1LcWLIXcu5U52W-NFcor-3dnsI2pQSlx2Vo72Bl4P5Jzet6h-1BjbeNMQqWvA_jVwJqvEVdkGHzfIaKNwUwlLTxw7cCYRXp0X2xE12cNd1ShnO4Hgi5YcloI6ulA8IZxG9qwq3pAVz-ev-mF0DBgk0cVWouLvDJfnKaAQxxS0t8qpouTq0epW9n8LhP89KRcKY3sd4GefadCIirNmHD2hWyuJVa0HU2w_72frWY6uoPvZYDAXwyuZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفر ترامپ به پکن نمادی از کاهش قدرت آمریکا بود، به طوری که چین تنها رئیس‌جمهور را سرگرم کرد بدون اینکه هیچ امتیاز واقعی ارائه دهد، طبق گزارش آتلانتیک.
🔴
فرانکلین فور می‌نویسد که با وجود پروتکل‌ها و مراسم پرزرق و برق، دیدار شی و ترامپ هیچ دستاورد سیاسی یا اقتصادی قابل توجهی برای واشنگتن نداشت.
🔴
مقاله بیان می‌کند: «وقتی آمریکا دستش را دراز می‌کند، دیگر هیچ‌کس برای گرفتن آن عجله نمی‌کند، و وقتی تهدید می‌کند، دیگر هیچ‌کس ترسی احساس نمی‌کند.»
🔴
شی نه تنها از ارائه طرح مشخصی برای پایان جنگ ایران خودداری کرد، بلکه از امضای توافقنامه بزرگ تجاری یا ارائه تضمین‌هایی درباره دسترسی آمریکا به مواد معدنی کمیاب نیز امتناع ورزید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/120541" target="_blank">📅 11:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120540">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
قطر و عربستان وضعیت منطقه و آتش‌بس را بررسی کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/120540" target="_blank">📅 11:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120539">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfU8JGszgvOgGADbtYdDJru0_pWttQRZnZN8yDdzSY3sAihlNWECH4f6eFiSWwccJbq6XtFzN2b5yF7HOs3j2rsjNu3STA-euosn1sCsm_WdqcvMKs5EwwTan-uS8WtbTYLFRGJmz5htHJI15hAprruEb8s9xm9BXcM3V3vr8GZvlWHZoX6iZtjDhJu1MgUqMtIyOuO9vGJZKWMveCEsgnUAslcvYR1xRdnnohYBDC-2Vyccft8ArKiXv9I9LS3HsP7d7PtdOgmHMFeif2elHyaOHRlRF_i1Az29N6B0gllwpIOuwFmJhjWszrn6NSulhIWlyelzl2g2T06RP2fBJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌ان‌ان: ایران به کابل‌های اینترنتی تنگه هرمز چشم دوخته است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/120539" target="_blank">📅 10:58 · 27 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
