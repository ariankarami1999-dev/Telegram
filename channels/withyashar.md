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
<img src="https://cdn4.telesco.pe/file/OG_0QGB-q0_5h2KKxyGgdJHPW9qpbzqgQPFjMQt1V7slUm7EIR5YEksDuUeyStZY5mjhGECw_N0PoF2gPWvX60rKcPIsqck1wGSV7Qz7YTRToZZGS7OBwToqUM5F0skSdOC9rBFaUQZWV5uwBzK1GQgWIBtu7iT-7BeLMU_8tGLAoezvZP-r2SY7zlXLO0KSsMWO4Sgo0Ofcw_gptdU4zLFNyWCm_4gqD2Yill2KKgTNhmwvNZD2pEJ80LfK3iEwx6aSwiv_0DzvLIERLhtuq7ITRu772-yZ7vRsifhEPsE_REuVmh-z9iA0wtOOVGtuDGXmciJn5lbgZgz3Yyv9iQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 357K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 20:42:49</div>
<hr>

<div class="tg-post" id="msg-17150">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">الجزیره: سپاه پاسداران ایران یک مرکز فرماندهی آمریکا در غرب آسیا را امروز هدف قرار داد
@withyashar</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/withyashar/17150" target="_blank">📅 20:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17149">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فوری | شبکه خبری ABC به نقل از یک مسئول آمریکایی: ما از دیشب تا همین لحظه ، ده‌ها موشک و پهپاد ایرانی را رهگیری کرده‌ایم.
@withyashar</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/withyashar/17149" target="_blank">📅 20:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17148">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مدیرعامل راه‌آهن: با تلاش مهندسان شرکت راه‌آهن در کمتر از ۱۳ ساعت پس از حمله دشمن آمریکایی به خط راه‌آهن مشهد؛ یکی از خطوط بازسازی شد و به چرخه خدمات‌دهی بازگشت.
خط دوم نیز تا ساعاتی دیگر بازسازی خواهد شد.
هم‌اکنون تردد قطارها در خط بازسازی شده از سر گرفته شده است.
@withyashar</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/withyashar/17148" target="_blank">📅 20:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17147">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">منابع : پس از پایان رسمی مراسم تشییع (آیت الله) خامنه‌ای، احتمال دارد که سپاه پاسداران (IRGC) بار دیگر فعالیت‌های خود را تشدید کند.
مراسم تشییع امشب به پایان میرسد و خامنه ای در حرم امام رضا در مشهد به خاک سپرده میشود.
@withyashar</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/17147" target="_blank">📅 19:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17146">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0da60dd210.mp4?token=MFR5qcVn7G-jEBrTOphXyAtFqNw8vuA7QPWhkNejQ9NpX5y5eIc_uYmkWm8Dv0d7eNpfc1G0GvxCbcLLDuSeSGwXu1CLk5qnyfdmbmv4OKMYd6qLyjI6UxZIYLThz27Va9dpur1-0wCouYl4rxdMyEjvFQroUIFHVnPKmv9XwZqb-fUD5nwR23NgJU8wiZ3gToe3yUYlpOvwLsonld-3-rmejbSXd3HXLmtTLioULz-qcql15683zm-PkFnjBUaGZC4nPLN31lK44Is0mLkvmrmCKp_k4CNXDmzy_TjMKlfbL5XwyrfJwvzCL-Q2O3zrWP36BrkK7Bg5qZkoUxj_PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0da60dd210.mp4?token=MFR5qcVn7G-jEBrTOphXyAtFqNw8vuA7QPWhkNejQ9NpX5y5eIc_uYmkWm8Dv0d7eNpfc1G0GvxCbcLLDuSeSGwXu1CLk5qnyfdmbmv4OKMYd6qLyjI6UxZIYLThz27Va9dpur1-0wCouYl4rxdMyEjvFQroUIFHVnPKmv9XwZqb-fUD5nwR23NgJU8wiZ3gToe3yUYlpOvwLsonld-3-rmejbSXd3HXLmtTLioULz-qcql15683zm-PkFnjBUaGZC4nPLN31lK44Is0mLkvmrmCKp_k4CNXDmzy_TjMKlfbL5XwyrfJwvzCL-Q2O3zrWP36BrkK7Bg5qZkoUxj_PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمه از نزدیک آتش سوزی شدید زنجان
@withyashar</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/withyashar/17146" target="_blank">📅 19:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17145">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شورای همکاری خلیج فارس
: حملات ایران به کشتیرانی در تنگه هرمز، امنیت انرژی و تجارت جهانی را تهدید می‌کند
ما از شورای امنیت می‌خواهیم که موضع قاطعی برای تضمین آزادی دریانوردی در تنگه هرمز اتخاذ کند.ما ایران را مسئول این حملات می‌دانیم و از آن می‌خواهیم که فوراً و بدون قید و شرط تمام اقدامات خصمانه خود را متوقف کند.
@withyashar</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/17145" target="_blank">📅 19:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17144">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5fspNLHD_XkjPkdg587O4bwBOScf_1b5yiBT_s2WYWJPGXLFGLnWdJXkE2YbBot00_zFR_6zoK5tgU4Vh7wHoYkZ4bUE6d63jJjTwE_FD_YROz_Y6D_30qTzzVVCLYsPDsiomMkhBTevAE8Pz8pNz_TnDjdbrju1qTTfxqY9jG8sm2V1z9OqcJKTCrW35_9ezyCVqAgSpJQWkohP_YfFutFSKc5gOpPwLbtUVKMB2P7lwCJM6Jt5cyfja46EX6Oc3cwSPHtUECIK9cV_arFrBb8qxfM-jzSI7JgOSTL7kmgt3zBl8jYI9GdNbxnO9ZKPiJrPXQy7u3zwZJkRkK97g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنجان الان از زاویه های بیشتر ( دم بچه های زنجان گرم
😁
🫱🏼‍🫲🏽
)
@withyashar</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/17144" target="_blank">📅 19:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17142">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f0aX8ccFfv9u4bkfAe76Z4026IwqM34zfNRodxg6dMicb0RdtES3jn7JSFXqELBMFXi1NgrJMdpYOvCxJGyomYXedBR36aawU6PlrvhTA1dF-NRP3hLTSxqP6JDSdcMaoFoicaaqIiQiHbI__F5BddBmJ-IPJARJp4c6HxeJjYi6kjrFXMBdM_ct_37NZuwUSEnWo4qRDAi-U-86Cq1-gLqVwM_feNhq7ClsQNsn_kWKgfzHfrXnAwMXhWpz_dxnZaSoWACQkodLRzJQA9GnZU7775NP7gMyW7YQe50lYlzOjk_1Khx8k2MSRoWJPLWRAaoIqj_rMVDWGaxAYxcYOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ENV7WsOmvA0XW3wah6c2sdSLB34BauNh2vGiXDOjxRNSP9dk5VRHW3rQ_LfdQbDmO5tFrgzOnh-E7T8NkiVhOEFgA8C-tDj9m8vlicfKjfpOnEKIB_glsdvLPrRVRyCHHwRzqZCD38i4PnSLdy1NHlAmTTgwFit6ZRF6e9mgB6GXHBHt_EjGhUBPMihlZK3PRb5VHvD0K5zO1PWvMzqTZ5pNEFllVupH9h-sxApLPl3uIrlMpEY3oqwmceFs0cBnDLmwKuUlQZz66sJnMm4Zq25uH7hYoYonvMAThnf_3PmCtRdAPf64WHXuTkICKKTpQ1Za8P9HKkxpxE5vob0Z_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انفجار‌ در شهرک صنعتی زنجان (تایید شد)
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/17142" target="_blank">📅 19:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17141">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گزارش تایید نشده صدای انفجار‌ شهرک صنعتی زنجان
@withyashar</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/17141" target="_blank">📅 19:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17140">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نخست‌وزیر نتانیاهو خطاب به خلبانان جدید نیروی هوایی در مراسم تحویل نشان‌ها: "جنگ هنوز به پایان نرسیده است، چالش‌های جدیدی در حال ظهور هستند." وزیر امنیت اسرائیل، یوزی یعکوو، در این مراسم گفت: "ارتش دفاعی اسرائیل آماده است تا عملیات را از سر بگیرد و به صورت…</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/17140" target="_blank">📅 18:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17139">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نخست‌وزیر نتانیاهو خطاب به خلبانان جدید نیروی هوایی در مراسم تحویل نشان‌ها: "جنگ هنوز به پایان نرسیده است، چالش‌های جدیدی در حال ظهور هستند."
وزیر امنیت اسرائیل، یوزی یعکوو، در این مراسم گفت: "
ارتش دفاعی اسرائیل آماده است تا عملیات را از سر بگیرد و به صورت مستقیم به ایران حمله کند - حتی برای بار سوم.
"
@withyashar</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/17139" target="_blank">📅 18:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17138">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/976290cc1c.mp4?token=Su-qTxvlqH0fmkmqzk_pskadtYeKbFQVUwzWJsr2mR1NiZSjnqBoNhRr0zUWo3-ZAqGpnyBQF8iEUq9_OSaFYlM2BD3jS65UZUfoI4_ZvoCrKuAsREcbt0aVvOlyLHYHlqG2PW8VEg_2xTvFO3-UyY8Wc-pet6JMFImLdcbzg4sGq4DYvWqffUcrsfqd3JDXFtYnfTzjDiqiMPSGAF89C9POYO3QmeiYDGC3m8KmodZlXqZPzkHVUzOLqZC7U1Js4Bh2ndxyghObKHHvFp6otnc6tS3X83No1vW-UXQeeo_H8bx-nOH4dOURpQW0Bfx6ipDlO0molSfoqPeiKFlO0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976290cc1c.mp4?token=Su-qTxvlqH0fmkmqzk_pskadtYeKbFQVUwzWJsr2mR1NiZSjnqBoNhRr0zUWo3-ZAqGpnyBQF8iEUq9_OSaFYlM2BD3jS65UZUfoI4_ZvoCrKuAsREcbt0aVvOlyLHYHlqG2PW8VEg_2xTvFO3-UyY8Wc-pet6JMFImLdcbzg4sGq4DYvWqffUcrsfqd3JDXFtYnfTzjDiqiMPSGAF89C9POYO3QmeiYDGC3m8KmodZlXqZPzkHVUzOLqZC7U1Js4Bh2ndxyghObKHHvFp6otnc6tS3X83No1vW-UXQeeo_H8bx-nOH4dOURpQW0Bfx6ipDlO0molSfoqPeiKFlO0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقایسه زیبای قبل و بعد بیت رهبری برای درک بهتر شما
💥
@withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/17138" target="_blank">📅 18:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17137">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cac8f1356.mp4?token=febXmLZIQKhEu5myDJ_c9hjgSJ3uLei6Xc6AaNkvVbA3B_6pDhCsu3B5WMkXfSg5WQZkSPa2luXLFc2SCZKwTpdhCwzb44Bor6BbSNRWxTwXpOXTouW8BDxCfD3IIFQnVU3LmZi5flvANQn0LpgxAA0PkPW0etpKDbrLR3RoSkGMLumoAhKfRVGvGngfuwbDMAoTT_8ha13I-d_XuDD4IR1oFgTG-0ElirC9lond20--MXob869pHRsxPbRiA3YV759tZJgHmfWcLUerrHQ22pTG3xzpvM4Ct9wsgpdtR3aCBp-fjHR2JSlEY0pMlUDcYlKQDHm8aKjsinK595GJhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cac8f1356.mp4?token=febXmLZIQKhEu5myDJ_c9hjgSJ3uLei6Xc6AaNkvVbA3B_6pDhCsu3B5WMkXfSg5WQZkSPa2luXLFc2SCZKwTpdhCwzb44Bor6BbSNRWxTwXpOXTouW8BDxCfD3IIFQnVU3LmZi5flvANQn0LpgxAA0PkPW0etpKDbrLR3RoSkGMLumoAhKfRVGvGngfuwbDMAoTT_8ha13I-d_XuDD4IR1oFgTG-0ElirC9lond20--MXob869pHRsxPbRiA3YV759tZJgHmfWcLUerrHQ22pTG3xzpvM4Ct9wsgpdtR3aCBp-fjHR2JSlEY0pMlUDcYlKQDHm8aKjsinK595GJhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارسالی : حمله آمریکا به اسكله صيادي بنود در بوشهر خدا راشكر خسارت جاني نداشت ولي خسارت مالي حدود ١٢قايق صيادي دوستان اتيش گرفت
@withyashar</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/17137" target="_blank">📅 18:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17136">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آلن ایر، مذاکره کننده سابق آمریکا در برجام: فعلاً احتمالاً در چرخه بی‌پایان «حملات و سپس کاهش تنش» گرفتار شده‌ایم ! دلیل اصلی این وضعیت، اختلاف بر سر تعریف «باز بودن تنگه هرمز» است.
@withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/17136" target="_blank">📅 17:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17135">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ارتش اسرائیل (IDF) اعلام کرد که اخیراً دو تونل دیگر متعلق به حزب‌الله در شهر مجدال زون در جنوب لبنان تخریب شده است.
@withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/17135" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17134">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وزارت امور خارجه ایران: عراقچی، در گفت‌وگوهای تلفنی جداگانه‌ای با همتایان خود از عمان و ترکیه، درباره تحولات در تنگه هرمز گفتگو کرد.
@withyashar</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/17134" target="_blank">📅 17:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17133">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbiu-K4QacS09w44dA_CFb_gLgldzOkVuAJQgAUvzr_cOgi-1-iW6N8nbLSWsYP9pzjAI4TL9nYQTk2GLZJl7Jgw1pJKIiFmhqxJPleKDGHsnTgFWGUZHtTfW6OF2PBgmGcipGAchGN7d9tlSISDkHXEeXPE5Y7ELHiBxvN_XppRBwrChFg8rQAXKugjwFXItn6H42fgUMYGE6B6nYmpNMt5y7kmIbS3auT9O0F4IdX86Jo0ztw8BGc9yV-56-o9_aJnXwxMfA7wNAb4iOBj7ApRWY7IIGTBBIQfpzH5XnitECFfUF17Nh7rdPNQReSezkA9LUVqMxDCc0XnDPCURg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر نادری که صبح امروز توسط یک دیده‌بان در شهر اصفهان، مرکز ایران، گرفته شده، جت‌های جنگنده F-35A Lightning II نیروی هوایی ایالات متحده یا گارد ملی هوایی را نشان می‌دهد که بر فراز این شهر پرواز می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17133" target="_blank">📅 17:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17132">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">۳ پا : مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی الازرق اردن با ۱۰ فروند موشک بالستیک در هم کوبیده شد.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17132" target="_blank">📅 17:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17131">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نیویورک تایمز به نقل از فرماندهی مرکزی آمریکا (سنتکام): طی دو روز گذشته، بیش از ۱۷۰ هدف نظامی ایران را در جریان حملات هوایی مورد هدف قرار داده‌ایم
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17131" target="_blank">📅 16:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17130">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f75c9892.mp4?token=btsbk2D2UB38FKftMRUIWfEfIDHpbtx2PjC43jR0XpKz6KBRCQwAWJj9cGmk3UPo9V5MIQOGoN-8Vf3Tr1GhC8IRulH_c7e5u-DxUNQ8lhvZ0X4NqBUBo5SormTABMGkrymI5bwXt-dJyqUFVn6A5NuTq_w0Er5t4zB_llbRuDzuZnzIkWrYBXlWB6rYmN0Ga2VzlZZ569e4SBiJ2CpgbhlJvRGp5AE104me2kI09q5XMXUNeaxdCy_XgB9yGSebgUcS4SChVvMqmVPquAXtEEsa5Ii2wI-zapWTwWsMruLchUKNbryQXKBb5-ESWYPKybYl41SJA897J3A-RltFDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f75c9892.mp4?token=btsbk2D2UB38FKftMRUIWfEfIDHpbtx2PjC43jR0XpKz6KBRCQwAWJj9cGmk3UPo9V5MIQOGoN-8Vf3Tr1GhC8IRulH_c7e5u-DxUNQ8lhvZ0X4NqBUBo5SormTABMGkrymI5bwXt-dJyqUFVn6A5NuTq_w0Er5t4zB_llbRuDzuZnzIkWrYBXlWB6rYmN0Ga2VzlZZ569e4SBiJ2CpgbhlJvRGp5AE104me2kI09q5XMXUNeaxdCy_XgB9yGSebgUcS4SChVvMqmVPquAXtEEsa5Ii2wI-zapWTwWsMruLchUKNbryQXKBb5-ESWYPKybYl41SJA897J3A-RltFDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">l
نتانیاهو : حمله به ایران مانند برداشتن سرطان از بدن شماست.اگر سرطان را از بین نبرید، خواهید مرد.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17130" target="_blank">📅 16:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17129">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyMgk5ST3pTPpZbKdSEp_8sxmI4SeuPR0WRLi7EYHTWSI2GVUpafRBGkaZPS54a4DCC6LVtRyGlDRT9-4cT-i29HxVIO2bRX6eSsYcETOsjf8uolOgUA8dWahpzLxxZWiNhDWZeykBKupeDfv-zeXSeg8FObmEyGyjDqqQh-l8uQKkR-B1qMqYX94H_k3FdHXXgBlce_g2sL0TySKi-dO4J8vHC08atalud-DS7hyvJamo--0XdIYllCWHYTHaNfIXZYULYGmZ9_u7ixAtW3lDIkxdsA8s5E4HH7E6sUMnpvdhFkXqVd8S4pxrDvHD1GdUBSLuWHzg_8ejNYc7L5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان پهپاد شناسایی آمریکا در آسمان زاهدان سيستان و بلوچستان
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17129" target="_blank">📅 15:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17127">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54fd028548.mp4?token=QpfxbNR0tZgRD-o6YBkIQex9BPZMA08aklyeiMopDyIn0ANyeR93q8c4GsMrwZ_9TVcTr_XHyAhEMYi5BqEuS2i6tZuzFvQABB7FJZTevgoIL6euVUz-5dnBrFB_niVSC5a4QPDryounS5IAx4RfsjUIShG02pXRS6aLoVi5WXGH-3IF-WO6guDHet_Ym9aC-dwvAWdvIU4NANqog5xxA-BMmxG50vWWQFrvjO5hWQNClLsUdLlsFmN-u658ba_CQ_2-3mBQ7PwnEuf5R0S4tN739ccSy2jkVR9gBIMtuI1IiW2ubwaqeQerRdiEKTltUcWQmqGOAJqza1OhXW4AEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54fd028548.mp4?token=QpfxbNR0tZgRD-o6YBkIQex9BPZMA08aklyeiMopDyIn0ANyeR93q8c4GsMrwZ_9TVcTr_XHyAhEMYi5BqEuS2i6tZuzFvQABB7FJZTevgoIL6euVUz-5dnBrFB_niVSC5a4QPDryounS5IAx4RfsjUIShG02pXRS6aLoVi5WXGH-3IF-WO6guDHet_Ym9aC-dwvAWdvIU4NANqog5xxA-BMmxG50vWWQFrvjO5hWQNClLsUdLlsFmN-u658ba_CQ_2-3mBQ7PwnEuf5R0S4tN739ccSy2jkVR9gBIMtuI1IiW2ubwaqeQerRdiEKTltUcWQmqGOAJqza1OhXW4AEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برج اسکله گمرک تجاری بندر چابهار @withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17127" target="_blank">📅 15:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17126">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc71b6295f.mp4?token=JhpEsILITa_wMQhkarARw3bHr39KPtH4KvyAcuFLAQ5RbrW-Iaq1EBuMPipfLXnEgOT1FaBwFFidc6oemQXHq2xx6iSWSPm7UzZqpOXgMcZxbnLPNOspljAirAr0x3GprrxmKAEZNUynhOME5dLU4ORzWFNmWd4bi9hZInltpjJ8BtaobEkAwBgrK6uS-ERb2lIpG3rTn2RwsngEepmJu004uHiaQzinZqIDhvKDl5y0ckUDLKEGK6_lYfoJlL9RLkeG08uFOA2DLCxotbhrmKsxRRHTpAqgXVpL4oLwBnP39n0jXYh9gFtjecHrJqyqtvQ27YmOpcIRPnF9Lieztw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc71b6295f.mp4?token=JhpEsILITa_wMQhkarARw3bHr39KPtH4KvyAcuFLAQ5RbrW-Iaq1EBuMPipfLXnEgOT1FaBwFFidc6oemQXHq2xx6iSWSPm7UzZqpOXgMcZxbnLPNOspljAirAr0x3GprrxmKAEZNUynhOME5dLU4ORzWFNmWd4bi9hZInltpjJ8BtaobEkAwBgrK6uS-ERb2lIpG3rTn2RwsngEepmJu004uHiaQzinZqIDhvKDl5y0ckUDLKEGK6_lYfoJlL9RLkeG08uFOA2DLCxotbhrmKsxRRHTpAqgXVpL4oLwBnP39n0jXYh9gFtjecHrJqyqtvQ27YmOpcIRPnF9Lieztw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون ترکیدگی لوله گاز شهریار
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17126" target="_blank">📅 15:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17125">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">۲ موشک بالستیک از شبستر، استان آذربایجان شرقی شلیک شد به سمت اردن
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17125" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17124">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zv7bTkC5fK3RNONYaS6WUGGmXusBE291SIg0uNYn4HbxBgWsaiGHofA2bqwHAux_tfsZEOwNaAAWRt0XeRG1CCIrqIrkSv0Ddxp2AQyS-ny5vqJWqF03NNsZCjwX0AL8W0fnUJhwVRWCdpBozJZu6sbOyYd4CxFjdq1jMnaozXWW0JibkjEQQo1T5GXp7xmHgDtDt1VvPH9sOmtAZBcoT5QcRXhgmXHQ-LZlcl9KpeywFinpRiqY6eSF1LUNFWq_sXFng3mUs_ArzbgYUZ4r9g9V7FeMihjfH5pKCFupD0d_wOkNrhCMHz5T3EU9hr8Qlqrafx3bH0YqxNKm-UlbDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش از پرواز گسترده جنگنده های نیروی هوایی ارتش بر فراز مشهد از ترس حمله به مراسم @withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17124" target="_blank">📅 15:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17123">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVzdeyvDGnznBgn7Z0pzHV_e6khaKk8r2cgSALHLUfFu-KueNyIJHtGiKcwAlWdrUsyR4jYByWnvMRKdfVVC2VdTHKmB8bX0Rh50GkeJi6rkmZQqK0Ifu0VDcZT55rfD6qOKBUA0okbfVTtweZi6lGTKqEkU5eX9lRsfIxbaehonKxnzXvFSXr7USwca1EogxPs6I99sh5G6E1VxezSYQERDnJZsmDgeynVps7vaY4JFKGCb-bmYBuzMv5cDAsp7lYBAmQv9yz42N00Fal_jL8N6tqJaWCGUT4YKnkpwtWOSg9v12kV8ttcKcbhblcAHYJm0dHD5ZcGDhxOLcRRxhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو ترامپ داره بصورت زنده از تنگه هرمز گزارش تهیه میکنه برای صدا و سیما
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17123" target="_blank">📅 15:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17122">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سپاه ثارالله کرمان هدف حمله قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17122" target="_blank">📅 15:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17121">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">آژیر ها مجدد در اردن فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17121" target="_blank">📅 15:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17120">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کانال ۱۴ اسرائیل : علی خامنه‌ای حدود 600 میلیارد دلار(۱۰۹ کوادریلیون تومن) ثروت داشت !!!!
رهبر سابق ایران، علی خامنه‌ای، در حالی که تظاهر می‌کرد مثل فقرا زندگی میکنه، املاکی تو ترکیه، کوبا، مکزیک، ونزوئلا، سوریه، دبی، بریتانیا، روسیه، عراق، ارمنستان و صربستان داشت. همچنین مالک چندین هتل تو اسپانیا بود.
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17120" target="_blank">📅 15:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17119">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نیروی هوایی اسرائیل:وضعیت حالت آماده‌باش در سراسر اسرائیل اعلام شد.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17119" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17118">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حریم هوایی سوریه بسته شد
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17118" target="_blank">📅 15:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17117">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارشات از شنیده شدن صدای انفجار در کرمانشاه
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17117" target="_blank">📅 15:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17115">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UhbpDEc7Jbblxgie5C0mqJL9B6YENK-qDRW5_c1yJLg0HMuBZDVQiAaBtUbaaioQBlz3g0hycmebmMtj0YcGA-hvxpfyQBnHIdh_HXxxG8aEC6cvR_vkPzsGC2FzY8nQI8p7JVbqcKiQyDstQNzASRmJxy1GN8k-w1Fx-lkFIAIE8T_YgAMfekvTNogiQPlSILjXbs_KLpILE9JReX7cR2L0gb9tX30bTfzyZWGkbHP77NYM1YhhsgKRBd8-kN4LPJncP1req680XzD-RDmSJKkCy4I-iR78EgydkbdDPD-5pIRNiYTqr-fv1O_AqxYJRfwu94Nf-CuQ3jCnKkCFuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tQCrRICO-99ttUop-ETwpUishGenAl0yKRfJ2vizeCSYucBtaXbet3libpiWfmWK-8tLoYGMjujErGsIXycWFT6huOnCHwtA7GRySO8WGOH95oSA43g1-OqkEuHMAB1qecUoxEE5rRupf_fOZHVgp6xRmwGhiM_kslw827dkxEpQ770U5UXEwH6VccsdUmGM4aqPU8ucprl6FEv04giTM0HHWgbdUtSTRpAj7m-b_CIO5xv8ASnvxRc_QAdtUPRTcTQy60zVi-nGb6X2NHV2Q55SBugJBxatB70bBJRB8wvGnms-tjELxvuTBi31GabrowPdSVUyk0SJHdYTCJT2xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت قایق های سپاه در اسکله بنودِ شهرستان عسلویه
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17115" target="_blank">📅 15:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17114">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حمله آمریکا به شادگان در خوزستان
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17114" target="_blank">📅 14:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17113">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وای‌نت:  مجدد یه کشتی جنگی دیگر آمریکا تو خلیج فارس مورد حمله قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17113" target="_blank">📅 14:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17112">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گزارش از پرواز گسترده جنگنده های نیروی هوایی ارتش بر فراز مشهد از ترس حمله به مراسم
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17112" target="_blank">📅 14:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17111">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آژیرهای خطر در پایگاه نظامی آمریکایی التوحید در بغداد به صدا درآمدند
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17111" target="_blank">📅 14:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17110">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تانکر ترکرز: ایران به علت احتمال ازسرگیری محاصره دریایی، 10 میلیون بشکه نفت را در شب گذشته صادر کرده است
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17110" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17109">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پایگاه سلمان حاجی آباد هرمزگان دو موشک به سمت تنگه شلیک کرد @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17109" target="_blank">📅 14:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17108">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گزارش انفجار در شادگان خوزستان
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17108" target="_blank">📅 14:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17107">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پایگاه سلمان حاجی آباد هرمزگان دو موشک به سمت تنگه شلیک کرد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17107" target="_blank">📅 14:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17106">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خبرنگار وال استریت ژورنال: علیرغم صحبت‌های دونالد ترامپ مبنی بر پایان مذاکرات، این احتمال وجود دارد که به زودی به آنها بازگردیم.
پویایی اساسی، بیش از هر چیز دیگری، تمایل به عدم تشدید تنش است. و من گمان می‌کنم که این موضوع در واشنگتن شدیدتر از تهران احساس می‌شود، هرچند که در هر دو مورد صادق است.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17106" target="_blank">📅 14:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17105">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سامانه های پدافند هوایی اردن در حال فعالیت در آسمان پایگاه هوایی موفق سالطی. @withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17105" target="_blank">📅 14:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17104">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">منابع رسانه‌ای: آژیرهای خطر در پایگاه آمریکایی «حریر» در استان اربیل در شمال عراق به صدا درآمد
@withyashar</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/17104" target="_blank">📅 14:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17103">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bd8d735f9.mp4?token=eM8JlTZk-6UO71fndf7SHeT9mncXfdVaYln_eYc9MGaqUdUoXG9SkykeqJBs4LCNY5tyeYApcv94suiZbXN2nOLeMsXpF4GDU-kg6u4AhVMUF9-SPtSFK7Hvc6a2NRLg7dZX6OCDSVuUWoPeM6b7r3By9YlTx6sCCvwkhBfCtz3OUjhALRrJeDf4rtox49TJqnSskpiNeiba919e8BXXTtfebCP6QTaCKNC2AKJFUM0GVh_btEqvMCCoar1qU4tMK4cOR8sasZbH9RN8-MSbZ8rQu2gCnLj5TXT_YY06dVIrNVMlZB1wb8yf504V-yJHSXEUgiCIuCluVwAAfxu9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bd8d735f9.mp4?token=eM8JlTZk-6UO71fndf7SHeT9mncXfdVaYln_eYc9MGaqUdUoXG9SkykeqJBs4LCNY5tyeYApcv94suiZbXN2nOLeMsXpF4GDU-kg6u4AhVMUF9-SPtSFK7Hvc6a2NRLg7dZX6OCDSVuUWoPeM6b7r3By9YlTx6sCCvwkhBfCtz3OUjhALRrJeDf4rtox49TJqnSskpiNeiba919e8BXXTtfebCP6QTaCKNC2AKJFUM0GVh_btEqvMCCoar1qU4tMK4cOR8sasZbH9RN8-MSbZ8rQu2gCnLj5TXT_YY06dVIrNVMlZB1wb8yf504V-yJHSXEUgiCIuCluVwAAfxu9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سامانه های پدافند هوایی اردن در حال فعالیت در آسمان پایگاه هوایی موفق سالطی.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17103" target="_blank">📅 14:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17102">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سفارت آمریکا در اردن به دلیل «گزارش‌هایی مبنی بر وجود موشک، پهپاد یا راکت در حریم هوایی اردن»، دستور فوری برای پناه گرفتن صادر کرده است
@withyashar</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/17102" target="_blank">📅 14:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17101">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6_lRSemA11KqkwbxYUkXoWkGPoIaDSBp81O1ORs3_fO0c93pExSRGMoN0FNeMK7hjUrrv0c0p-iGV97_3D9T-xapIjqfGWsQxegAvhbPvxtUVwoy5agMj2KUSSzdC405QWYaDSW_1R5TUYvRDI2C74NCNLrntYn1KOFPmRrBnGRG-BeKdPZaQcWUV0jICBWGS5ZCPGshE8uSihRrPDF1XgsT4q6Zd_5XlCjFgE7Dn3x01tAybYHHlvm91y22EDidOWL3cC_l5N0GwMM7s_zMyrR-yKxKH77IZqEzCRK1QwZu0tCfMSPURKLyEWHtcix1QXXtovgcasTKwgMLIAkzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک موشک از حوالی تبریز
@withyashar</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/17101" target="_blank">📅 14:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17100">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دقایقی پیش موشک های کروز تاماهاوک در بوشهر دیده شد
@withyashar</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/17100" target="_blank">📅 14:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17099">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/17099" target="_blank">📅 14:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17098">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گزارش ها از نزدیک شدن جنگنده های اسرائیل به مرز عراق و سوریه خبر می‌دهند
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17098" target="_blank">📅 14:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17097">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7-a7q2psSTL1uqSNcDUPxvuE877_TpIAK6gPkh51h-vUMvBLNpIq8CiautI8c8s4z-uD2J9IA7qoeSf_7wgQlBO61yV9f9oNPaOA5glIk3A6xGRtozlZmyAQmj8J4zIqzz-q8GzaJXsVIWjVxz29H-YI2-CDAqbrnjtIkYSZaXrPypKJNePHNNdN5EF0QRdtEqos4SNVe3Um0NvrVfPNPNuS7mAVqWkkR67ZFltmecj9RjW6LH5gu2ZHK9CxH61Tg8HYYj-FInhFdBzT1wfXESrSmejbAglBG0cnSgZzccWIGVcqwzYmTgDIq9vAK-Ca4nZb6f722tUA4fJkejMSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس زیبای مقعیت و لحظه شلیک لانچر موشک در خمین
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17097" target="_blank">📅 14:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17096">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/17096" target="_blank">📅 14:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17095">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بعضی رسانه های داخلی خبر دادن مجدد کنار نیروگاه هسته‌ای بوشهر مورد حمله قرار گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/17095" target="_blank">📅 14:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17094">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تانکر ترکرز: ‏تهران، در انتظار ازسرگیری احتمالی قریب‌الوقوع محاصره دریایی نیروی دریایی آمریکا، در یک شب بیش از ۱۰ میلیون بشکه نفت خام و نفت کوره را بارگیری و ارسال کرد.
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/17094" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17093">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گزارش‌ها از صدای انفجار جدید در کرمان
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/17093" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17092">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گزارش صدای انفجار هایی در پایگاه  بندری علی السالم در کویت
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/17092" target="_blank">📅 14:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17091">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شلیک موشک‌های کروز به سمت کشتی‌های آمریکایی در نزدیکی بحرین.
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/17091" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17090">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آلارم حمله  صدای انفجار و درگیری پدافند در اردن
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/17090" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17089">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36ca620126.mp4?token=updgNqi3YXMRUMX571PsZgi1ZJeBpUZ0y8NRDpQL5Sabi4hk0aD-NHuKnrRMsqd8il4OjMbtqnF86HJ3ZhfATuTun7QVh2BLNRNwYCwuXfgS-n1_iV2nftlFaSfrxm2Zsu7V2XvkLJ_4hGIvmyh0bGEuc3lxMGiu25xNkvU_HhjFylIrwpDgrTVHdiOEoLbLqY3u59NurDzBajsxxTc7Rkdr7jR3gwBvwytX0fw3wMHHmRZhK2M7GEugTVcCRngund07P3411cxcuoGyde4JrQWLU7sDnyiJUxHbg2BOoI9_oaTVA2LHqzX5kMHgXrAVf8dAi6NXUa8i-cgNjeUTow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36ca620126.mp4?token=updgNqi3YXMRUMX571PsZgi1ZJeBpUZ0y8NRDpQL5Sabi4hk0aD-NHuKnrRMsqd8il4OjMbtqnF86HJ3ZhfATuTun7QVh2BLNRNwYCwuXfgS-n1_iV2nftlFaSfrxm2Zsu7V2XvkLJ_4hGIvmyh0bGEuc3lxMGiu25xNkvU_HhjFylIrwpDgrTVHdiOEoLbLqY3u59NurDzBajsxxTc7Rkdr7jR3gwBvwytX0fw3wMHHmRZhK2M7GEugTVcCRngund07P3411cxcuoGyde4JrQWLU7sDnyiJUxHbg2BOoI9_oaTVA2LHqzX5kMHgXrAVf8dAi6NXUa8i-cgNjeUTow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از زنجان هم موشک پرتاب شده
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/17089" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17088">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آلارم حمله  صدای انفجار و درگیری پدافند در اردن
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/17088" target="_blank">📅 14:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17087">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/di2uhuRHFWtuSA3JAOCFA9muf-RuF8Smpg-Te6p-pvQ9CoctHpFWVHd-t7Sq75PNH6D11jrFwwTnmSNmRAAOOGh-F4T-KnGHG_bsqRuoZCDhp8LSiQsA3y8n4Bm3YNoLFi4MM8vg_UudJbAjznoZUwsZjcZMo72-Na0jzX7PndbQzI5iVHmgOFC-liXzJ-ause6UeiEPPGpFFd2bCe36yoW0Fr26BbUCkzUMKOdBAp_ABCyymYBOCR6PHY-7dSy0dqW7hLYxS_1Knm-9InlFRBKiJhdkb_WKMJd90uzaErm0njINL04a-gaZM5qyqoFPrI0VWhQGkeH6MvEiIUPMUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه موج جدید حمله را شروع کرد :
۳تا موشک از بین خمین الیگودرز بلند شد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/17087" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17086">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/857d372470.mp4?token=M6Dug1B6sC4r0jIZhOMYoNAsZLtiS8-xZVxVzbBsk0vfRzB9T6_x-1YMURlzhcDX7xo_k-wMRiZIrCRmgMzdJVMH-uC2yV7Ap53Ak5xvL0KptjU1DgXQXzVvIeZnivMszbdoFMELlRzoCQECNIUAanahgpjnmVf4JdupdMcZMxr9BB7D5xZLX0ewzhM3jvmpbyjA_uVVn44MWCmViyyGrBFqs4xGR3dKt6uxp3QlfFD3XTKd6ezVvHYGO_EeKzrYuGmwU5O1LWfCZMfmtSu2zVd3YQOL9oddpzgh-u96kihp5upE6pgGCid1ZdB6ZhJHUzGqDsZWxm9783IqqoIvj1iKkvsGqGa7eL6bnBuLvTEp8p--8Gx1Pxd6o5Z6nAezkSR3q9x9Mczq0svlKnRqb3dV9wR1niBe3ia6Ph66rbBtISQhd9kpjcyTstt2-UuTm3Gjn4zyVUUiORX5AjFwRcJGRdWEe9g267X6hgT12elXKnYxpVMTeqNvv_N-2y2kQ9JaaBcowQN4ECOETOZfnWtbwnMJnkTdltJFf4AC9qyJZc5U9dn3Emd4gce-MTNmo5KTgy-8yzwuRTDBPU3XV5sIssdV8_F3JQuYgIIRaDQBlYlM2Vw-AKaQ8Fnf_xouz2g3lFTP_DLCJ7JO-DoCzkLswSzw7cCl6-SyjH8ygag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/857d372470.mp4?token=M6Dug1B6sC4r0jIZhOMYoNAsZLtiS8-xZVxVzbBsk0vfRzB9T6_x-1YMURlzhcDX7xo_k-wMRiZIrCRmgMzdJVMH-uC2yV7Ap53Ak5xvL0KptjU1DgXQXzVvIeZnivMszbdoFMELlRzoCQECNIUAanahgpjnmVf4JdupdMcZMxr9BB7D5xZLX0ewzhM3jvmpbyjA_uVVn44MWCmViyyGrBFqs4xGR3dKt6uxp3QlfFD3XTKd6ezVvHYGO_EeKzrYuGmwU5O1LWfCZMfmtSu2zVd3YQOL9oddpzgh-u96kihp5upE6pgGCid1ZdB6ZhJHUzGqDsZWxm9783IqqoIvj1iKkvsGqGa7eL6bnBuLvTEp8p--8Gx1Pxd6o5Z6nAezkSR3q9x9Mczq0svlKnRqb3dV9wR1niBe3ia6Ph66rbBtISQhd9kpjcyTstt2-UuTm3Gjn4zyVUUiORX5AjFwRcJGRdWEe9g267X6hgT12elXKnYxpVMTeqNvv_N-2y2kQ9JaaBcowQN4ECOETOZfnWtbwnMJnkTdltJFf4AC9qyJZc5U9dn3Emd4gce-MTNmo5KTgy-8yzwuRTDBPU3XV5sIssdV8_F3JQuYgIIRaDQBlYlM2Vw-AKaQ8Fnf_xouz2g3lFTP_DLCJ7JO-DoCzkLswSzw7cCl6-SyjH8ygag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که ترامپ از بمب افکن ‌B-2 تو ثروث سوشال پست کرده همراه با آهنگ بمباران ایران
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/17086" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17085">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c1e5bc22a.mp4?token=rd87Uf0HAUZ86nI_J5vIjuuD0SOOocoQcQnPzK_-217vjv4SCVATVPYMbc7SQ9RM8PK170L0zhpklQrVj18EYP1_E5UHfN2A1cKNOfjHQk85IPBitPnUq8jeiepb36kIMIqtrj4JXsxkRJdWGLmXm7uU3hEPOCiQ_Bj6CFwjXa574Lk8NiVHGeP6mgHE-lYXjzU2XyrlPcYg5U1OtN5NNnzVD0ynNG1rDxwTuUiQTkKbk9Nbccm87OzVlbpzORBwScDtT6XPxsL9hcm9kfgaE5n2pIlr_6MnHpWldugUaswoU2FeQvtZAzFp-fE1MFVAvZX0FZqDWBaififCwdDkZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c1e5bc22a.mp4?token=rd87Uf0HAUZ86nI_J5vIjuuD0SOOocoQcQnPzK_-217vjv4SCVATVPYMbc7SQ9RM8PK170L0zhpklQrVj18EYP1_E5UHfN2A1cKNOfjHQk85IPBitPnUq8jeiepb36kIMIqtrj4JXsxkRJdWGLmXm7uU3hEPOCiQ_Bj6CFwjXa574Lk8NiVHGeP6mgHE-lYXjzU2XyrlPcYg5U1OtN5NNnzVD0ynNG1rDxwTuUiQTkKbk9Nbccm87OzVlbpzORBwScDtT6XPxsL9hcm9kfgaE5n2pIlr_6MnHpWldugUaswoU2FeQvtZAzFp-fE1MFVAvZX0FZqDWBaififCwdDkZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار
کرمان هم‌اکنون
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/17085" target="_blank">📅 14:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17083">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pQ2Mcv9VDlXpGVJsK7th7fdgs1VYhwADoTzVbkAz6URiIb0lu15QYNoCRuYItLus89ACFSKK9eLAXVCd83UiL1u4Jbsi-11NNvFpVJcOIVp7o2XftoJ20X0hGHOFQQlGdlzbXsNgRKd1rv8HnHf0Jc0Oo9irkgLLzvH_Qq2_G8Pry-1IffP5qP1n55HNAO68nfD4HtwqTy7OTd-UdNKOOtfwwMRl-zlo2Lb4dWpn95mvuRgSjbQ4KoiZ7eoBmfgf6kdjqq3POoasL8ygeUHdenntt0nbLIy4NEnfqJl27XvEgtqos-ak_-oPnPliNzWa0B1UzEKUgPx3Gp7aGPbzRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VBzyccLBduL6cUnWkZWtUjIFYdZTaa3LnV4feE6Pr94HvDNaKiNSrzb7dwRHg0Ogq_danzBrmrW0Y_k6U6OxNhtikUuOShCcRYnPVmDPI3l9_gyXdJGh7tSA6gQzQ3w-7uwMMa1CfGwr30umzX8z0kmIpldb4sbXXjeUCx_C-qYYzkv1pOGccg_cf5YMCQsyetOkGFsa5vWqlLF-2KyBqKcs-Wd4JyikolF6exngcYoLBmyhA9T-peIzXnBhjLYhZ2xjCk-K4yHSrWUbMws-xiZG8u1wLndNUvw-v-IX2tbo6vYptj5R6UtTtZcTC65RDTpo_lq63gPGQvUtX_Hw0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر از‌ انفجار شیراز‌ الان
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/17083" target="_blank">📅 14:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17082">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">انفجارررر شیراز
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/17082" target="_blank">📅 14:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17081">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شنیده شدن صدای چند انفجار در چغادک بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/17081" target="_blank">📅 13:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17080">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">صدای انفجار‌ بندرعباس
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17080" target="_blank">📅 13:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17079">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">منابع نزدیک به کرملین: پوتین احتمالاً جنگ با اوکراین را تشدید خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17079" target="_blank">📅 13:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17078">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXEe6mPN_QXUy95uHtQHKpLVMr2tXcIM24MdYsjGnUWWRkTIdtCWP9aPIoTFEUFkxVA9zVgyBJGNnMTeYp2sDdLfbVpsjR4RD36uhAYLRpiZBTdLiyqMWoCyayvu0owYro8EQhZr9OlRvFb3O786Cv3uCgVuloZjFN-ND1Td79Bb3t9gySPO7lfRUJj8mrwefX0PPRBogdkLs4VjYITvQLazu22XgWojiy-l8LeEF2ufuWuPYUBvxueRNpX8p5VKRHYtWfOIbx93HVNjS3nUVIiVS1-9mb8_qoGhADKvwny9g27gfKGczi03wlRHu-mBV6BVWpNQNh3DtQzGgKNP2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آثار حملات هوایی شب گذشته آمریکا به پل ترانزیتی و مسیر ریلی آق قلا
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17078" target="_blank">📅 13:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17077">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وزیر امور خاورمیانه بریتانیا: حملات ایران به شرکای خلیج فارس ما، تشدید خطرناک تنش و نقض آشکار قوانین بین‌المللی است
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17077" target="_blank">📅 13:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17076">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کانال 12 اسرائیل به نقل از یک مقام اسرائیلی:
طرح‌های تهاجمی آماده‌ای علیه ایران در اختیار داریم
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17076" target="_blank">📅 13:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17075">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دلار و تتر ۱۸۱،۰۰۰ تومان
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17075" target="_blank">📅 13:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17074">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آکسیوس:ترامپ آتش‌بس با ایران را تمام‌شده می‌داند؛ نبرد بر سر هرمز آغاز شد/ مقام آمریکایی: آن‌قدر ضربه می‌زنیم تا باور کنند ما جدی هستیم
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17074" target="_blank">📅 13:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17073">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خبرگزاری CNN : صبر ترامپ در مورد سرعت مذاکرات،به ویژه آنچه که به نظر می‌رسد تاکتیک‌های وقت‌کشی ایران در مذاکرات هسته‌ای با واشنگتن است،رو به پایان است!
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17073" target="_blank">📅 13:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17072">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">همکنون تابوت خامنه ای‌ رو بردن تو دوردور مشهد تاب میدن
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17072" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17071">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رسانه های داخلی انفجار‌های الان در بوشهر رو تایید کردند
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17071" target="_blank">📅 13:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17070">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">۴ انفجار‌جدید بوشهر
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17070" target="_blank">📅 13:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17069">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نماینده دائم روسیه در سازمان ملل: رقیق‌سازی اورانیوم در خاک ایران یک گزینه عملیاتی است
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17069" target="_blank">📅 12:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17068">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خبرگزاری وابسته به سپاه :  آمریکا پل کریدوری ایران با چین و روسیه را زد  بامداد امروز آمریکا با موشک کروز، پل استراتژیک ریلی «آق‌تکه‌خان» در استان گلستان را هدف قرار داد. این مسیر که محل ترانزیت کالاهای روسیه و قطارهای چین بود، پیش‌تر نیز هدف حملات مشابه بوده…</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17068" target="_blank">📅 12:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17067">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDertBDhgQpN9-4jFaVPy3T72wwCrJDFtPrlZYLTfRAkHXiIh8wocXSloi-_RdFgVPotm94FB7mjrulsCF3lUUfhhK-WUPWCWSSlJ4FJt4UPxFT6ledH1egyRHx_zQdEZ5GLUIjoolxW1C9FCGRehtOLV0ePB5496uwbVGiguFdQMEaKOetnG_YQlSvqSiG7lm3FBsbqQr4sH_pc5GA19xG-7u3K6HLcVCKwaXX8DYESQAjEtufMV3H2rHH0TXzzsn6ki5VX00SAElz4CmzjmCrqTwHrXSoXexrKif-R1QYJSBz1G8GrDLhIhmJ1tcvoXAu35Ub-4ZvKe7SaH0EIYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع کویت : امروز پدافند هوایی ۳ موشک بالستیک
۱ موشک کروز و ۱۰ پهپاد مهاجم رو که وارد حریم هوایی کشور شده بود، با موفقیت رهگیری کردیم
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17067" target="_blank">📅 12:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17066">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مقام آمریکایی: یک سیلی به ایرانی ها می‌زنیم تا بفهمند ما شوخی نداریم‌‌ ، فضای بیشتری برای تشدید تنش با ایران وجود دارد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/17066" target="_blank">📅 12:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17065">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ورود محموله بزرگ ریلی چینی به تهران. ویدیو ضبط شده در هفت و پنج دقیقه صبح امروز گرمسار(دیشب توضیح داده بودم) @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17065" target="_blank">📅 12:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17064">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آکسیوس: حملات آمریکا ادامه خواهد داشت
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17064" target="_blank">📅 12:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17063">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGU4GhDRvY3HftkqVTk3gNAyoFsUTS__o4RNUj7uEO_NVcEs5cpwLh36Tnkm1CxwHd5v70XGVU_mxJWqId7rnmBbERnPNL9zDhGbCuRPhyL6jGXkDWGHRuU6wYnesqXEzjMp0ZWL8hGgtf9OKhNrr3pkKvOyCOk6KEQf1viJIcjfnyf_LAnjU08ZZai-I0QFN_3qe8B-LNysFMzH8DzjyWVZfVY6yaHr8TiSB_BAHVTFcdbx6kNdXRHrhg5lxKDKDuQMli2aKujMl2JvahivDyQZsMJcG7llJiW5zwX_iCAVU0pqfyPVTggkx2myhf39Rv4Y9KhsfKPvyNRgknVbaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه براتون سواله که چرا آمریکا انقد زومه رو سیریک:
سیریک یکی از نقاطی هست که بدلیل ارتفاع و موقعیت جغرافیاییش اشراف بسیار عالی به تمامی ورودی و خروجی تنگه هرمز داره. توی روزهای عادی و وقتی هوا تمیز هست شما راحت تا خصب(عمان) رو با چشم غیر مسلح میتونید رصد کنید.(تجربه شخصی خودم هم هست) بدلیل موقعیت نسبتا کوهپایه‌ای منطقه سیریک نیروی دریایی سپاه با کروزهای ضد کشتی بیشترین حمله‌ها به شناورها رو از این منطقه انجام میدادند و سریع متواری میشدن. تمامی تجهیزات ثابتِ راداری و موشکی توی جنگ 40 روزه منهدم شدند ولی این الدنگهای اوباش بصورت چریکی و پارتیزانی از سمت سیریک هنوز اقدام به پرتاب راکت ضد کشتی میکنند و البته خب سنتکام هم مرتبا با پهپاد و ماهواره تحت نظارت داره و مرتبا پیداشون میکنه و میزنتشون
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17063" target="_blank">📅 12:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17062">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گزارش انفجار مجدد بوشهر
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17062" target="_blank">📅 12:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17061">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">صدای ۳ انفجار بوشهر
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17061" target="_blank">📅 12:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17060">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آکسیوس: ترامپ آتش‌بس با ایران را تمام‌ شده می‌داند
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17060" target="_blank">📅 11:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17059">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067e87ce1e.mp4?token=LfXVZRm4d8SMTscXWp8hKsR6fmBDb3peVjl3fcs6_zD73yCn-uuk42GcfIXPlSI4957AIKA8Jzz8FmQ3YWGH5rws04-jWo4Ov_kEM7Hu7PiIUpvPOKoqxXLVBjApgGHG4aweh6dFewNBt5luxJeOaazhU8oyJNFwFcdN_XwNm91KYzIIWMs2qJ4HPRwceqAflIB27WgBI0FmFQhjeGnUS38fMgiXVVQ8zHt8uOlKENxI-yC--G7jn1bclPnLT1Q2jwyam7Fm0eY4aNqLj55_7C7WuzgYW80mIy2k7Ra8LGtwtVpcx6UYpnAxUt9U0gk8KngFnOKeLybv0ddL_aMxdo8vLW0hKc0jawccFOHEjOBNn-_g7rFMOh8UviTHMnVQGzt0XeXX8jWsDc7JEZn5t2fQGgjhWUslBTSBWtCrGTQeWUravp7D2_89lb8R1thrn1yj4WObfJAAA3pdNZest_4n7f3R9rVHKx8X9yrBVfvYSHVa0Gj5T7xFwbv-4vpykknlWlkJgKJIpWW393l5bFo_NBE4tYVHevqkiLu4WpQd-s9J9GLCjJA48Tma47pD7WDK_4HSZLV9pImKJPVWx7g_0c-wxWBgiWKaTPJLKgwMJHq_L4WeJ_ns2dgkx95250m-CZLoLuY0-peB9-0He3L6pmq1e33RzuMi21LDNQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067e87ce1e.mp4?token=LfXVZRm4d8SMTscXWp8hKsR6fmBDb3peVjl3fcs6_zD73yCn-uuk42GcfIXPlSI4957AIKA8Jzz8FmQ3YWGH5rws04-jWo4Ov_kEM7Hu7PiIUpvPOKoqxXLVBjApgGHG4aweh6dFewNBt5luxJeOaazhU8oyJNFwFcdN_XwNm91KYzIIWMs2qJ4HPRwceqAflIB27WgBI0FmFQhjeGnUS38fMgiXVVQ8zHt8uOlKENxI-yC--G7jn1bclPnLT1Q2jwyam7Fm0eY4aNqLj55_7C7WuzgYW80mIy2k7Ra8LGtwtVpcx6UYpnAxUt9U0gk8KngFnOKeLybv0ddL_aMxdo8vLW0hKc0jawccFOHEjOBNn-_g7rFMOh8UviTHMnVQGzt0XeXX8jWsDc7JEZn5t2fQGgjhWUslBTSBWtCrGTQeWUravp7D2_89lb8R1thrn1yj4WObfJAAA3pdNZest_4n7f3R9rVHKx8X9yrBVfvYSHVa0Gj5T7xFwbv-4vpykknlWlkJgKJIpWW393l5bFo_NBE4tYVHevqkiLu4WpQd-s9J9GLCjJA48Tma47pD7WDK_4HSZLV9pImKJPVWx7g_0c-wxWBgiWKaTPJLKgwMJHq_L4WeJ_ns2dgkx95250m-CZLoLuY0-peB9-0He3L6pmq1e33RzuMi21LDNQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمان بحرین : 4 حمله به مقر ناوگان پنجم ایالات متحده
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17059" target="_blank">📅 11:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17058">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سپاه : تنگه هرمز اکنون به طور دائم بسته شده است و ایالات متحده و متحدان آن دیگر هرگز از خلیج فارس نفت دریافت نخواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17058" target="_blank">📅 11:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17057">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">هم‌اکنون هواپیمای حامل تابوت خامنه‌ای و خانواده، فرودگاه نجف را به مقصد مشهد ترک کرد.  @withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17057" target="_blank">📅 11:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17056">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آلارم وزارت کشور بحرین:
از شهروندان درخواست می‌شود به نزدیکترین مکان امن مراجعه کنند.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17056" target="_blank">📅 11:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17055">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">هم اکنون وقوع سه انفجار مهیب و پیاپی در بحرین
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17055" target="_blank">📅 11:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17054">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">همین الان فعال شدن پدافند مهر آباد تهران
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17054" target="_blank">📅 11:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17053">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6621f9c274.mp4?token=ZKsaRrMRm_iwYJ3L_YOuG5yLZM9han557shUW28Qm1UAiQvRbxwcXN88XKp4fKS3yxoyitYMPwFYD9r_4z4-n80Duo6gtmkryLWEQ6RgOH27ALYWfT0GaKwMV4b5lLztx3wbcyw_fgCv3BD15X93Jst9N7z-XHIYsNk_zXEnqdbHgb6NfGCIDsNICKyu8D7uumXa0VydI9v-FtGZr1SVc4JLu9GQZv-tnaGf3JGQhQhyD0WcSsvMzyU0TcRID-UtkdEP0P2CTFsxfotwMBHEPh6UTMctdnqQTM1fVtIX4-TCEVUn7-9iV7bKiJCFzyf7_L4OgiBlcCTa55eQcbMtK6V5PEzWRzm0oMaSy8qSCi7UUO6lqrYPJlQzYm-NkuVI_2L749loCgvSoZ2pM2FTWcNKqg6aMsw_nkzvYWPOXNuAVvzNQrop8cDoggjMzNBR7hfJVpca1oDKbpx1S0IRDAIL_QsbMEVY1hGDhJcsW09uDDo38CNZuhxElrETPw2zbtzbbhxkumZ2RV4qn-cDXkFOSKpgzP_WoaxVswygCrIfcSROX2eeKjjeZdn2CwuEYqhcr0GcxPOXQASmkc_wti9R449GH0J_mA2cVivrYM1sL3noYKYUsBvVrVkf5j0WT1bBUFXNj2kqw2Z7lyE6bfQ65JGrBWnx9uiCyL2yfNM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6621f9c274.mp4?token=ZKsaRrMRm_iwYJ3L_YOuG5yLZM9han557shUW28Qm1UAiQvRbxwcXN88XKp4fKS3yxoyitYMPwFYD9r_4z4-n80Duo6gtmkryLWEQ6RgOH27ALYWfT0GaKwMV4b5lLztx3wbcyw_fgCv3BD15X93Jst9N7z-XHIYsNk_zXEnqdbHgb6NfGCIDsNICKyu8D7uumXa0VydI9v-FtGZr1SVc4JLu9GQZv-tnaGf3JGQhQhyD0WcSsvMzyU0TcRID-UtkdEP0P2CTFsxfotwMBHEPh6UTMctdnqQTM1fVtIX4-TCEVUn7-9iV7bKiJCFzyf7_L4OgiBlcCTa55eQcbMtK6V5PEzWRzm0oMaSy8qSCi7UUO6lqrYPJlQzYm-NkuVI_2L749loCgvSoZ2pM2FTWcNKqg6aMsw_nkzvYWPOXNuAVvzNQrop8cDoggjMzNBR7hfJVpca1oDKbpx1S0IRDAIL_QsbMEVY1hGDhJcsW09uDDo38CNZuhxElrETPw2zbtzbbhxkumZ2RV4qn-cDXkFOSKpgzP_WoaxVswygCrIfcSROX2eeKjjeZdn2CwuEYqhcr0GcxPOXQASmkc_wti9R449GH0J_mA2cVivrYM1sL3noYKYUsBvVrVkf5j0WT1bBUFXNj2kqw2Z7lyE6bfQ65JGrBWnx9uiCyL2yfNM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره‌ای جدید، خسارات قابل توجهی را در یک پایگاه نیروی دریایی سپاه در بندر عباس تأیید می‌کند. یک آشیانه آسیب‌دیده، خسارت به یک سازه در امتداد جاده و ضربات قابل مشاهده که بر دو اسکله تأثیر گذاشته‌اند، قابل مشاهده هستند.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17053" target="_blank">📅 11:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17052">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17052" target="_blank">📅 11:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17051">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ویدیو از محموله بزرگ ریلی که از چین اومده بود ! @withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17051" target="_blank">📅 11:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17050">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">درود وقت بخیر خسته نباشید چرا حملات فقط شبا هس؟ روز ها چرا خبری نیس؟</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17050" target="_blank">📅 11:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17049">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromnima</strong></div>
<div class="tg-text">درود وقت بخیر خسته نباشید
چرا حملات فقط شبا هس؟
روز ها چرا خبری نیس؟</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17049" target="_blank">📅 11:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17048">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">قالیباف: آمریکا هنوز یاد نگرفته است که زورگویی و بدعهدی دیگر بی‌هزینه نیست. شفاف بگویم: بزنید، می‌خورید.
دست و پای بیهوده نزنید که بیشتر فرو خواهید رفت: تنگه هرمز، فقط با ترتیبات ایرانی باز می‌شود نه با تهدیدات آمریکایی
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17048" target="_blank">📅 10:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17047">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وزیر دفاع اسرائیل: ما از هیچ نهادی اجازه ای برای ورود به لبنان درخواست نکرده‌ایم و نیازی هم به اجازه برای ماندن در آنجا نداریم. ما خواهیم تا زمانی که حزب الله در تمام لبنان غیرمسلح شود.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17047" target="_blank">📅 10:31 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
