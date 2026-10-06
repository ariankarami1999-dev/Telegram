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
<img src="https://cdn4.telesco.pe/file/Kf6X10OmpU7k1z3AVH3pgA-EZOwDlkelak9C82BUzd5M0V0_QWNdF6B841ZM8Exp56nSN5GUO5EN1jknCiXOkWwRYbz6gjWzokedGtaVLHA6PArgEVx5RsvZqQKPJt2VfB1uxhbz6owrGcMU7nkuiRP8TVham-H_M8kBJpSXvJmoqlMX-vxbzM-E-eGy01iWYN-yhiaSsUU7W-3U4fE22LqDd_s0Qub_tZFYXYRWoac7LlXhEPyC33XEnmn7NaW9rCvN6NDw99jCKMO69U1XiHpRH58_XYqiiaU255FS2DPI7bti6KtsMg2yDvEoMi3KVQ8qWbfXwDnkEoRCCAxM4g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.87M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 17:18:01</div>
<hr>

<div class="tg-post" id="msg-466646">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PglajCuZ_gP6qQDU9Z69Amu4lFodAj-P-qJVJR77EyXfaXQBH_SROJ_t9fZP-09t6VKIqoTs_p1mP3e36LOu18bN_ffbmsRAT1J8i82Xkyb2Br51YvGQNPAFkaN67ZXkqfqpxdp3aONMTZU6v2cYe0IZdIGXkalcBQE0cPoa7KQoem95R7parotejKlJS-K8KNVvdvvtMNNURae16_4o9QzWfoxtFlpUPfwAhTGlyiWEFZU_SKLfyQ7asOoXK0-Whd8odeiO4EovBxySTdHAwW0oO_UNJVfzcZ6nag75GMaEV9EaNPJAfGiN8F7CkrNEW7IQTGC2uDFglN3C7ctwug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶۵۰۰ صندلی پزشکی در آستانۀ حذف
🔹
همزمان با انتخاب رشته داوطلبان کنکور، پیشنهاد کاهش ۶۵۰۰ نفری ظرفیت پذیرش پزشکی در سال ۱۴۰۶ امروز در صحن شورای عالی انقلاب فرهنگی بررسی می‌شود.
🔹
حاجی‌دلیگانی، نایب‌رئیس کمیسیون اصل ۹۰ مجلس می‌گوید: «کاهش ظرفیت پزشکی و دندان‌پزشکی با اهداف برنامه هفتم توسعه و نیاز کشور در حوزه سلامت مغایرت دارد و نباید نیازهای واقعی مردم تحت تأثیر تصمیمات کوتاه‌مدت قرار گیرد.
🔹
تغییرات مکرر مصوبات، اعتماد عمومی را خدشه‌دار می‌کند. تصمیم‌گیری درباره آینده صدها هزار داوطلب کنکور باید براساس مطالعات کارشناسی و نیازسنجی دقیق باشد.
🔹
اگر شورای‌عالی انقلاب فرهنگی با کاهش ظرفیت پزشکی و دندان‌پزشکی همراه شود، مجلس در صورت لزوم برای این حوزه قانون‌گذاری مستقل و بلندمدت خواهد کرد.
🔹
ظرفیت پذیرش باید بر اساس نیاز کشور، جمعیت، پراکندگی پزشکان و وضعیت مناطق محروم تعیین شود و تحت تأثیر منافع صنفی یا لابی‌های خاص قرار نگیرد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/farsna/466646" target="_blank">📅 17:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466645">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba9921587.mp4?token=Gxt0FfDIMpf2Xrl49ns13T1v-1tKTVDMVFxqrFGvtZGriQJdyEFEtgqrqEU350wyrzhx5E-SE5Xsc13ikcsUYxlZAhvHvQTCkP-H92xesZu3cn5JiQiz5tsKEmgbboP-4CSxPKLa46seUPdS-QzvHSAxGe2eGj3YDEoqSi3LGkwL17gnTUngzO5IbxLGbeh6G042WByIWcuIkosXXbRR8IImRu9RnkujkXKfLRuFkMo2pe0xpOHjb56bH40K2DiEdkXhyucyRMy3G9LP3XOOCa91P35qdmciHbyeQqnaMnJbY8mb_nN35lC6n_YgdZwCnriQ_GGxdTZIUi6NQIeHRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba9921587.mp4?token=Gxt0FfDIMpf2Xrl49ns13T1v-1tKTVDMVFxqrFGvtZGriQJdyEFEtgqrqEU350wyrzhx5E-SE5Xsc13ikcsUYxlZAhvHvQTCkP-H92xesZu3cn5JiQiz5tsKEmgbboP-4CSxPKLa46seUPdS-QzvHSAxGe2eGj3YDEoqSi3LGkwL17gnTUngzO5IbxLGbeh6G042WByIWcuIkosXXbRR8IImRu9RnkujkXKfLRuFkMo2pe0xpOHjb56bH40K2DiEdkXhyucyRMy3G9LP3XOOCa91P35qdmciHbyeQqnaMnJbY8mb_nN35lC6n_YgdZwCnriQ_GGxdTZIUi6NQIeHRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس بسیج اساتید از نقشه دشمن برای التهاب‌آفرینی در دانشگاه‌‌ها
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/farsna/466645" target="_blank">📅 16:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466644">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ماجرای «طاعون» در روسیه چیست؛ آیا باید نگران باشیم؟
🔹
در روزهای اخیر، گزارش‌هایی درباره مرگ یک کارمند آزمایشگاه در منطقه ایرکوتسک روسیه و احتمال ابتلا به طاعون منتشر شده و نگرانی‌هایی درباره احتمال شیوع این بیماری ایجاد کرده است.
🔹
با اینکه اطلاعات قطعی اندک است، گزارش‌های متناقض فراوان‌اند؛ از نام کارمند آزمایشگاه و سن او گرفته تا اینکه آیا اصلاً جان باخته و اگر چنین بوده، علت مرگش چه بوده است.
🔹
با این حال، مقام‌های روسیه اعلام کرده‌اند یکی از کارکنان مؤسسه مبارزه با طاعون در منطقه ایرکوتسک به «ذات‌الریه با منشأ نامشخص» مبتلا شده است.
🔹
باکتری عامل طاعون معمولاً در جمعیت جوندگان وحشی زندگی می‌کند. انتقال اصلی این بیماری به انسان از طریق گزیدگی است.
🔹
باتوجه به اینکه این خبر در کشور ما باعث نگرانی شده، مرکز مدیریت بیماری‌های واگیر وزارت بهداشت ایران نیز اعلام کرده که هیچ اطلاعیه یا گزارش رسمی از سوی سازمان جهانی بهداشت دربارۀ شیوع طاعون در روسیه دریافت نکرده و فعلاً نمی‌تواند صحت خبر یا میزان خطر احتمالی آن را تأیید کند.
🔹
در روسیه نیز «سازمان نظارت بر رفاه انسانی روسیه» اعلام کرده وضعیت بهداشتی و اپیدمیولوژیک منطقه پایدار است و مردم باید به اطلاعیه‌های رسمی توجه کنند، نه شایعات.
🔹
نادی اونیشچنکو، یک متخصص بیماری‌های واگیردار روس نیز احتمال ابتلای فرد جان‌باخته به طاعون را بعید دانسته و گفته است طاعون یک عفونت باکتریایی است که با آنتی‌بیوتیک قابل درمان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/farsna/466644" target="_blank">📅 16:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466637">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F2Xb-fkTFQ4ZR1DIIaMbr4OQgbJ1O3m6ovJxmz_fTEIAtMpjg0A16MzJyUVyQ7_3ew9uf5BphkWlmCaHMZcHFMHvWYZWTx7oCOhCIoYgWQYapuOwZFaaQXJYq3nAQdopnFatZiGeFb16FfWcA1Xe80DzjK-8ZWgtuKreooC_roiJPXzNdZ2kaUolWQGQR_htdBzByVwfY7Ouw-PnaqZHz0bT5yXo87qux_AIVOEaov6rq0bJr-A9Xp7O7GIwUAylg9TNptEhS-i3moCEjnX7JsaP-MmZ4a_bA3W7zu3Z33yBJV4BKkFmKGioe4Wl9wWoHP-ilvalL-ZOQC1xzEzPkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aLVDSVZQ3pUS59W1C5FPyl7eQRoY4pzsVJgGnKT0MwlmuHzPffAqwUqFpcv4qRbUwbvlFiQNgivCyE15ZbTNQZIHS8byf3Paoz8DmWR9CaxMPekAaMU4MAbESQEHBR4EnaVQ8mvNWRFHK5pooHHTpY3ICftqgKZV90eTqd1Yq3bLGLKKnjlsuvkbCmgX4tKE0wgAWCmX41-H_MkwKGhMj7-cJXT0E5oiOcd4xS4L8w2XA0UAXcnhxazfiGoDfKuE3cMeTEqFh8OP3nhmFFHZsdUrpxIeCNLt_UV9sw0SMFPq48ALhdeC35il2LYOVAFR046FxQUftlISXV8Qp-NkPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Na1UHo6AwEWqa8THCDgSqnxJY18iVex5csi9wB0aEu6c-rgo02nSkTRZOsKpnPKrPIKnC-TmozD1UvyImnor8Q2tPz-ROqWZP1akYE3XLEZX158WF8-ppW885bLTWYDVkDr-M3kuLS6FSbkzsjHVqQz-xt9JVdsk-rJ3lPQkvKifsRw2a7b1SHDbeJuLlhkS8jYGFq8wrNdK5VHd-suIOG3lL0SIsGlKtvSnzz1a4Qncdr8YTOWkk0939ZRLbbKtNdUkBP4qShjQVdZ6CHH1ovmCxnemGsfkz4tjERZiTYwJX3MwRd2a9aUyjUcrWHX4ttTFivQYIge180xYyS_Eow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0zJaUFIkUKO_B-s1YZ9THvPxHRAU5SrZf_E7JNKr7l1zyVD5XBiyTi4b3oNZdj02ZFQf-wfHtzW7M7uXPzSOoRf-QYMElBtKWmGkYINvgNRRlrmJ0l4NxykMbN-8sh_65iGTYJK3cijE_hhrNKwt5vUDrzhfnBJInHvLsg5nhO9xMlxRzxBM6NwqFmWfLSWn-I_gdwKBtfBEwXt9cJVz2HsmY5PsS1X_aMKyiUjN8On1A8IdmgDZccVS3VEEyqC8bJEFOFgQCve-52_UVsfPvUuoJdIFc0hdbZChpJ2LEoxjSJNQjKAibYCv37Qcu7lERNI1Zxb9X8-i-XcQXsevQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_kQTGM_7cWO8Dse37s6Xltv5I7seIrOPsSFKhOsxFvCqM9PVQYLq35X31n3JfnXAoKccPiZfh5aYzVI5xzZs0CMSdUK_b_PA_Eda6ViGqiXrGUCxEkHTB8JGgZWduyIe3C3BVSKSfErdcMTMJMX3EFivTBNWZEL4KB95NG0NbdUrInqusrhSBrOGaNQwZsEVQaipAyIDSavn95V7UKAWTLNYeVTwCBNEW30IFPYHuJr4bQDZ-NCP85IxQjhCOAOp9mN_-apxdvLMZ-gbzLz_gD3Xd0V0GrjYEuOVar4O8QDccCR3Ykj1jrr9LjmicobNVoQ8WFxu4LQ0WIz9wGp7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PQ0a4EUYUQgRXSvs2errTbsQDDCyfpC3apmA0Dyry5r2Yw2zQjXg2ybVDxp26MfhM0yuNKCMaBHkTl-ZR6FIfU_iKXjs1gGwaTd4aY1zVXH_cK7FVfJkQyjRqslvug6zP_4fKbc7n5fyDXb_ss0VO0fEVFFJ8FrSXeY6uIaGfVsbUZ2agchDRfV0vxwgk2sRlGXrydabUwO_dB7uIasVWjdQHkzUNADTwEn39ZJj66IxiTfPPcRj8UwqnghsSeWUBXTVTLm7COwqMnrJxcgtTegxoqLjGyYukMtSWjeG9lQ2UJ09TMNxG9HN-vTR76-vegVkoIsO3WCqAy25UDKx6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aWXqQOR5Lau3kse1IMKxEBgYBaI9cIZIX7goIcHkx1s_wOLA9W0OlABf78MjlN3OKNQXpiJun-Nt338mdilAcWcPLnxpWHtc2ZH8BluhHpASMhTfeh152RI2xtN6SOqafZgP17l0vKD4EXKUe7IGk4rLAxAp3XdrSjpizb79fJr75MQ-9i9JmUg98qT05aWbz2Bvji13W0khqgNSVU4Z3iYnjDHIGCK173KD7w5BtPq4XJQf-0kX2d3VhBZZcP2TXdLliJDkEjuEO9RiF0FgetE5GSx7FUKEPI4e18hwnugv5lHAgBSCltSKV-nLzC9GmJ9qVFIU__rWhXSa5B9cXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رزمایش جان‌فدایان ایران در خراسان‌شمالی
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/farsna/466637" target="_blank">📅 16:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466636">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YY-V2i3ukNKvmkWzpiGjx6yANVlhunYRGaOI85yVtq-cYWOZMIzDO8VUwZIaLEaaqSX2DJ2RtH5kPf8XOYUTNuWn7kfKpV6CsyhaCeYHfN9RWUlxmZGUn76vFy8c4pBbj8UcsCprKYJCrkWhDwj0R-B65eJAHNXMuhEhzzlocHd_qPXx2Q8-bHBNy5RMVo6l8JA3saNLxs1CBjOv6pXSyr3Y3sMbzVdTLzRcwVMnwaIcRZUbquDkEOJpmosWKOmMLzdU163RCJ_RUEYsCs209wpeJ-FzPA7lTf3m4A8sh7AjVVtlqs5n7okHC25SHjlr5qC13nrlAm0ZwtF4Z998zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت سعودی به جای دریا دل به بیابان می‌زند
🔹
ناامن شدن مسیرهای دریایی و حملات به زیرساخت‌های نفتی، آرامکو را به بررسی انتقال زمینی نفت عربستان به عمان و صادرات آن از ساحل دریای عرب سوق داده است.
🔹
عربستان درحال حاضر برای صادرات نفت خود به ۲ مسیر اصلی یعنی تنگهٔ هرمز و دریای سرخ وابسته است.
🔹
هر ۲ مسیر در سال‌های اخیر با افزایش تنش‌های امنیتی روبه‌رو شده‌اند و حملات نیروهای یمنی نیز هزینه و ریسک عبور نفتکش‌ها را برای عربستان افزایش داده است.
🔹
به‌همین دلیل، ریاض به دنبال گزینه‌هایی است که نفت را پیش از رسیدن به مسیرهای دریایی پرریسک، از طریق خاک عربستان به نقطه‌ای امن‌تر منتقل کند.
🔹
عربستان می‌خواهد بخشی از نفت خود را از شرق کشور به‌صورت زمینی به یک خروجی جدید در ساحل دریای عرب برساند و از آنجا راهی بازارهای آسیایی کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/farsna/466636" target="_blank">📅 16:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466635">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyq5rkWoqunuIsFfGdolQMOGYjKVZThSj539FNAEN13ocrRMQPCQOqo7qSo7bSon55UCQg8OqYs7btQVZyWwuiSZXACnISPOITJMdOTEOeuM0bKdylYjJUx-nebDLhKu5BGQkYI_NAaTUKELjNH8sh-N4LO6aW-sLpMiVfvU6bpuPfddYXm5LYHP5SWRWWF4wIUkSI3lw8SKx00x1dkr1ht0GIaUO15-BfsqwCq3YH4qsOIUN7Bm-mw756E9X_AHpjSBROQlVkV8SpLD-WjBuZUgjD78Z40tHzmLiKuhJ3Z08SRtYEMDkce3b9z-3t7KqH1u71xUQd6fJVhpgCs-kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نفت استعفا کرد
🔹
معاون اطلاع‌رسانی دفتر رئیس‌جمهور: با پذیرش استعفای محسن پاک‌نژاد، طی حکمی از سوی رئیس‌جمهور، حمید بورد به‌عنوان سرپرست وزارت نفت منصوب شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/farsna/466635" target="_blank">📅 16:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466634">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FukuGBICLZges6jHYs_TN8PSxo6T09lbmiEBjiXxPXkdUyCs6xvql7UMzhy2d-i-74dA40CPoPIrX57cw53wTMrp104k3S--HfFjg2FlZNdmymwV9grGk1YMOd2CUwH3mA-rvzZG04MvnjnUkL5b1-qH77oBdpXYVAm30flGWIJk5zKKK5e_nLEIwQ-tDn-m-Qvtsr5GFOfN8HNEettwwI6AjROV_3T_Bh5w2iOsmygIahP_htoWG-SV3ThTkkb1x7ghZRNxol8RZe3UE1qCCpeGCM-5Y8hPOljyl6wS_k9-ME7fsXtyt2EzCZSIzO6wHw7yx5VQmFksaz2aDVJxjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای‌عالی امنیت ملی خطاب به آمریکا: ایران عقب‌نشینی نخواهد کرد
🔹
پیش‌بینی‌های توهم‌آمیز بسنت از همان ابتدا هیچ اعتباری نداشت. تبلیغات اخیر او نیز به همان اندازه عمر کوتاهی خواهد داشت.
🔹
شما در جنگ نظامی شکست خوردید. در جنگ اقتصادی نیز شکست خواهید خورد. تنگهٔ هرمز با تهدید یا فشار باز نخواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/farsna/466634" target="_blank">📅 16:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466633">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c79e7f6ebb.mp4?token=B640PDSejec0y6JedwL0HMpgRzZEszzRLbgznXNrBAh7rRJUv1y1vIezRPMRteNLq30yktXaib7arSQtyO07GlK9LIXI43Uck3A3XBm72acICQBN6O0HiF69QIgPmC7SG_K0S-1k5_iJR1YJnl7JsGwDZZ7vXmn8bjM4xfywch5sSmxg6keLa6Q0yoGkrDbHrwrgs3otV_IGSNHDXANAeN3W6AI0HOFHgMBDqSpQr3VRRW4kYNKn6SqJeXTj0hDHP-k9hG7XQaxsNibuflIcRPnXz0khHrWo8FuwWDovNIFHOYrlEDikVTaJg6YfxozeT86hXjy8IAxYR59PlqH0jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c79e7f6ebb.mp4?token=B640PDSejec0y6JedwL0HMpgRzZEszzRLbgznXNrBAh7rRJUv1y1vIezRPMRteNLq30yktXaib7arSQtyO07GlK9LIXI43Uck3A3XBm72acICQBN6O0HiF69QIgPmC7SG_K0S-1k5_iJR1YJnl7JsGwDZZ7vXmn8bjM4xfywch5sSmxg6keLa6Q0yoGkrDbHrwrgs3otV_IGSNHDXANAeN3W6AI0HOFHgMBDqSpQr3VRRW4kYNKn6SqJeXTj0hDHP-k9hG7XQaxsNibuflIcRPnXz0khHrWo8FuwWDovNIFHOYrlEDikVTaJg6YfxozeT86hXjy8IAxYR59PlqH0jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ مرگبار به کشتی ترکیه‌‌‌ و اعتراض هند
🔹
روز گذشته مقامات رومانی خبر داده بودند که در نتیجه حملۀ احتمالا پهپادی به کشتی رویاد ممدوف در دریای سیاه و در نزدیکی سواحل رومانی، ۲ ملوان کشته و تعدادی دیگر زخمی شدند.
🔹
حالا امروز وزارت خارجه هند با انتشار یک بیانیه این حمله را محکوم کرد و خواستار آزادی دریانوردی شد.
🔸
به گفتۀ وزارت خارجه هند مجروحان توسط مقامات رومانیایی نجات یافته و تحت مراقبت‌های پزشکی قرار دارند؛ ۳ تبعۀ هندی که از خدمه کشتی بودند، در سلامت کامل به سر می‌برند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farsna/466633" target="_blank">📅 16:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466632">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/401d1ab6bf.mp4?token=LyEQekNFSuydShI3BzzKzZhKVHOW5TYWNB_-l5i1QVcx9ZslcWOy8xSOSuhOcoUhbn7LFKtfb4M4kWtA8VGBTf8XJYZFJ8UK5D0qkqyE0jDjIzUw_xFph_vBFEW77jt0qFVqPy-oueKWLJuJrESn3jJpoBwlz_eLzFiZIKUx9B6lFbzYIBpchqSYLDb1il2XH3m8_DDr9VUwTocZZpBoyh15IqHtzOxCCnDcT_dwMq6Ffkg8W9-od9FDoK66GMUa7HWrr7LN4oRrahphyOK6oJvLgu5oep_LLyPFJVWhzLba7igicRR2fwKEnamCFkc_SURdeaG6E50DZ3hwn0zJ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/401d1ab6bf.mp4?token=LyEQekNFSuydShI3BzzKzZhKVHOW5TYWNB_-l5i1QVcx9ZslcWOy8xSOSuhOcoUhbn7LFKtfb4M4kWtA8VGBTf8XJYZFJ8UK5D0qkqyE0jDjIzUw_xFph_vBFEW77jt0qFVqPy-oueKWLJuJrESn3jJpoBwlz_eLzFiZIKUx9B6lFbzYIBpchqSYLDb1il2XH3m8_DDr9VUwTocZZpBoyh15IqHtzOxCCnDcT_dwMq6Ffkg8W9-od9FDoK66GMUa7HWrr7LN4oRrahphyOK6oJvLgu5oep_LLyPFJVWhzLba7igicRR2fwKEnamCFkc_SURdeaG6E50DZ3hwn0zJ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مزدوران سعودی در راس‌العاره توسط موشک‌های یمن
صید شدند
@Farsna</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/farsna/466632" target="_blank">📅 16:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466631">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WETyyo3Kuc1NKIQpfPJp5VTkP_eSSCZ4zetvYuJrv_VccKhoSK5O_9UVSYPZoyYXKFC8xCZ6FfeR5WW5Bz7lHlb8wyMl_M7AKGcSh3tNgTP2r_vsuZGyfjWGcEfNlYnvxiOY1mB9yfct7Fc7Ebs6B3kRpF_MjLbDVMHC1tYZF6tve8oF8u94tpy9WhA0me1Are-TjYAf0SU74ksY6zF411RPy6kTAEtGESoybGfNC34AIqMrUwa0apMwxY6lWayRrudbBUfIcxNZ4JLkxKD8_-oUSldRLUxZPQd2olzSsNKJYCzALaJBcIwuFUGLP8NfkcsIP0yQc4LmmJ0fDOdw8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از تز تا تولید؛ نقشه‌راهی برای توسعه فناوری افزودنی‌ها در صنعت روانکار
✅
روزنامه دنیای اقتصاد /اکبر میرزاپور/ سرپرست شرکت نفت ایرانول
🔸
صنعت روانکار یکی از حلقه‌های مهم زنجیره صنعت نفت و از نهاده‌های پشتیبان حمل‌ونقل و طیف گسترده‌ای از صنایع کشور است. در این میان، افزودنی‌ها (Additive) اگرچه از نظر حجمی تنها بخشی از محصول نهایی را تشکیل می‌دهند، اما نقشی تعیین‌کننده در کیفیت، عملکرد و امکان تولید بسیاری از روانکارها دارند.
نقشه‌راهی برای توسعه فناوری افزودنی‌ها در صنعت روانکار
اینک بخشی از افزودنی‌های مورد نیاز این صنعت از طریق واردات تامین می‌شود؛ وارداتی که علاوه بر ارزبری، با مسائلی نظیر تامین و انتقال ارز، محدودیت‌های تجاری، حمل‌ونقل بین‌المللی، طولانی‌شدن فرآیند تامین و محدودیت دسترسی به برخی تولیدکنندگان و فناوری‌ها مواجه است.
🔹
[لینک متن کامل یادداشت در وب سایت](
https://www.tappico.com/NewsDetails/d925c49b-d925-4e5b-9056-08df237183e6
)
@tappico1381</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/farsna/466631" target="_blank">📅 16:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466630">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAJqaRXiFOuDaUVH1rDG3qU_s8UJwHA_jOesjhOszAX2yJI_wPyToLIsp0kEvwn0GKP0sN-4abPLwkBf8mfqmsXr0yoR-oBR1G9JtYOU2HaZlkTRnEWT8JnLXs8a3tj5-BggheYjy357lPH7WbtVIEtEBLih3uU_gimQClyLMYiV_0xBRlQqfXUbA3puzUhFB8QKp1yVhGM1O40PkusLzmOUVLDJX4WMQNnszY24l6wzqG0jk1bq7s9AXmTGuPRNpDJO7Hfkj2EokxrfHggbYwD6zQnE5GD3r1apYS6iCiayGKWUl85Rkz-AmbuayUvZui8UFjlw_MvQMBU2hgnHbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
طی شش ماهه نخست سال ۱۴۰۵ صورت گرفت؛
رشد ۶۳ درصدی پرداخت تسهیلات بانک کشاورزی / تزریق بیش از ۱۴۶ همت به بخش‌های مولد
🔻
بانک کشاورزی در نیمه نخست سال ۱۴۰۵ با پرداخت بالغ بر یک میلیون و ۴۶۰ هزار و ۹۵۴ میلیارد ریال تسهیلات به متقاضیان واجد شرایط به ویژه فعالان بخش کشاورزی و صنایع وابسته، رشد ۶۳ درصدی را نسبت به مقطع مشابه سال گذشته به ثبت رساند.
🔻
شعب این بانک از آغاز سال ۱۴۰۵ تا پایان شهریورماه، در مجموع ۳۱۷ هزار و ۱۰۳ فقره تسهیلات به متقاضیان پرداخت کرده‌اند؛ رقمی که در مقایسه با عملکرد شش ماهه نخست سال ۱۴۰۴ ، از نظر ارزش کل پرداخت‌ها ۵۶۴ هزار و ۹۰۱ میلیارد ریال و از نظر تعداد تسهیلات پرداختی، ۵۴ هزار و ۲۶۵ فقره افزایش یافته است.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/farsna/466630" target="_blank">📅 16:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466629">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/farsna/466629" target="_blank">📅 16:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466628">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7afb904f50.mp4?token=djhdipiVFdAVdi5-TeYQQaTlmXy4xBtIh_eikf0awmrIcltRAzKfCNn7EPHNSo5bbAIyyee2bDA6X5IqZad4Iv0lC4hHSYKL9O8IEsLWbgrIxDcANV00kMYuSzxq7YKtpvevZeDXwqTn1pgkWXcELq_0ekdVHkMmJQUXg5pKhM90y15SIq16GsTOWMh9bL6xpzRQX5-1cGyUwWS_z8NTETRMyUw-vrQ_RQWfKFX_9JbTaHIJNNuoGEQtey6FhaOt8vfQYG8ow5tCYMe5bDEEOCN8S51gekWEZ0mC9nx5H3Iv3vxd0lbDA8dfTU0zbhdv27Du6MIpn8XMs80IaP0vKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7afb904f50.mp4?token=djhdipiVFdAVdi5-TeYQQaTlmXy4xBtIh_eikf0awmrIcltRAzKfCNn7EPHNSo5bbAIyyee2bDA6X5IqZad4Iv0lC4hHSYKL9O8IEsLWbgrIxDcANV00kMYuSzxq7YKtpvevZeDXwqTn1pgkWXcELq_0ekdVHkMmJQUXg5pKhM90y15SIq16GsTOWMh9bL6xpzRQX5-1cGyUwWS_z8NTETRMyUw-vrQ_RQWfKFX_9JbTaHIJNNuoGEQtey6FhaOt8vfQYG8ow5tCYMe5bDEEOCN8S51gekWEZ0mC9nx5H3Iv3vxd0lbDA8dfTU0zbhdv27Du6MIpn8XMs80IaP0vKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدارس فرانسه به دلایل امنیتی تعطیل شد  به دنبال اعتراضات دانش‌آموزان دبیرستانی در فرانسه شمار زیادی از مدارس این کشور که در کانون بحران قرار دارند تعطیل شدند.  @FarsNewsInt-Link</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/farsna/466628" target="_blank">📅 16:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466627">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dg0DN2Pc4IfZlkSOCnbDgB4NAOuAlxjX4P0R4RNBPDcPNJVwuMk_7mv8l2hcpkAecJv5EI_bFT_BMQYZFSLPWC0246T_PR3e_QdsZtmRKgZ15jjJEC_caogxmbwBH47094r102rPevfUws-8ymk8kefa1uMpMxbXZKSBHAPaN6gDmh2tu9rfhcnUHSY36wb9OP4242goSq89VI_Iz6mnQA8mOv0tgI8nyIQqYs6ffovZ7O__6ISrru4-RKeiXQnbXYg9SU1THD3WhWqQFQp8UaWtKCGesnN4ahXE_mD7uW-yO1lnPkEMQEDjRyOjE8N2ini2jl6RT-gcF-pEDc_AGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت واقعی نفت به ۱۴۰ دلار رسید
🔹
کمپ، تحلیلگر ارشد بازارهای نفتی می‌گوید که قیمت نقدی نفت خام فورتیز (Forties) بیش‌از ۱۴۰ دلار در هر بشکه یعنی بالاترین رقم از زمان آغاز جنگ علیه ایران است.
🔸
این نفت که در دریای شمال معامله می‌شود یکی از بزرگ‌ترین اجزای سبد نفتی برنت است.
🔹
قیمت ۱۴۰ دلاری نفت درحالی‌ است که ترامپ و وزرایش می‌گویند که عبور زیاد نفت از تنگهٔ هرمز و خط لوله‌های جایگزین، صادرات نفت خلیج‌فارس را به وضعیت عادی برگردانده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/farsna/466627" target="_blank">📅 16:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466626">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_vFSSFxeoHrJ6aSV5HYiQviFn8pSsamZT71sLgHK_4W_nA9oEn1QrivfcU178OeqtkR-gLgm40TUf2Gi84PDsSZoOGEpfv2mAp2hcMSgo_HQQNowZrR9i_5Ib7oJ_9BIFjrr4tUqVSd460VfZThs_7LzuKgC_nVRQqQGo5ZtdC2_Hjk9DtmDgz3G3HRE7OFQLzCbf3WbS2dxpOOfa_COkfr_mA3tcFudoAH8QlyXkMZAGsVqt06mjiW9O_coNiSGT-hXMhdUem2IGjs0ObOSYuyjY2Emez6zoA336EBsnPZtaCxEhm6zwjMgR7yxYc7wPhIjIQ6UEHVUquoDkA1SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۳.۶ ریشتر در عمق ۸ کیلومتری زمین، امیریهٔ سمنان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/farsna/466626" target="_blank">📅 16:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466625">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHmKSYJ3_eOOZ9C0QK3e35zdgi5PTPs9D3twh_av09EoLRgFILxOv2tryWm7yJIvEYeTbQ_sS2xDEuyRVnyTCUFTJFgLzXwR4V_vtD48LWBJDfTXicf72luzAqnwvw--znHAimiSmGErTAoYxQ9STj8hyvY4fNag5IuJ_gB2mAyOgx6rbhJmYkL-5Yf26OwTCfCpPBceyKB_W7YiRUgkNGwTUhLEZ9uygrFLxqZWNUBYfppYagOVWc9GjCWkDj6sMnp1-E_q8LLtsXJywNUMPTcfBrn_PueFGYEFbZZHUSMoV9H9atUkSmTlWzbKf-lSxHScvt7OzwYrxsnmwIN7_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان تجارت دریایی انگلیس: یک نفتکش در تنگهٔ هرمز هدف حملهٔ یک پرتابهٔ ناشناس قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/466625" target="_blank">📅 15:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466618">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ro55vBwG__Xqh1IXylfttxwsd7sW0TTjYOnGp9NdyQgxBOfcaYoMTtpYAbpg2WN-QkthmP8RYHfz6H-Q35tilLd8hI2F307Mob6BxZOlz_E9cB8EcX65Q1GtoBU0-XrPMQJUhZu1qt2-W4LblKqJpwuP8boNPOMd54pE6i89Cr9dxALY4lj5K8h0qe3063dXBi2UTU8MSBFn-Epw6FnBxn4HwzqvGs1uea_i8JJVW1LhZ9iGqvNB12Dgf1WqFBE5_9m67bwkSq9U-MJTbBMubFk2yBUCSePKxBHCSGrtc1KZ5HIdHc7ZARuPIsk1bkDdNV02Jm8tFHTZuWW1dhc5og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOxrdFIcfchXxcPX883Py5Ec3DRTZWINmiTWn0N9Cr-D4QUvyFgkS7GcVeOdKb_30EXGfc3FQzAw67lfgqKzb3Hk1ysAYz-I3vwsVP5b6vTR9pd5hbdowpTql8t3MIvxd58FMMbUe86AK0pc--kMf891oH5O-VCv-X8uq_dxzFRD3mm18JY0pRE4ePxL8kfFJgzlBurpodG2sK8vCqUhzqk4HOfugzfCd0vVkjUN9gY3k5s5Vbzqsbc3Sy9UJnXUwXYXK27KYascfVU-03tNPKropwQZsvqiat7fs-jW320Kpf8zfMyduPsKOY6YgoGEX7rjsVM5Oy7gweUvTfuFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bGUCOLzezE8HxhxGnTWJqstysFxNpG3v9pj6qnGST-YjeNr2rCyLA_VRYuLjoQMGFAQYWWaMOFKNEGjT1v4IacWgdXoQuUvylsgkNZyC7JZ0Pd7ITVyevAkrTu9iP-6izCgpWqj0gO352ZX57t9127VBUSyxc5QdB6e6xGsCOcr3IeBjgurltE9nnWuji_LzbL1ALF-ogJRUluRUepbxsQzYzZQoVWtjZlzF2lw6itpItiNwqHVYmFdgUNDYNGs4zumC0ClqV3Zt3Oxe_Ek4c8qRG4vRrzTSAd3hnKcOv8vq87xBqPkKIHpBQwr_Sl9oNRvWeWckumcLtofH28bmzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bGUCOLzezE8HxhxGnTWJqstysFxNpG3v9pj6qnGST-YjeNr2rCyLA_VRYuLjoQMGFAQYWWaMOFKNEGjT1v4IacWgdXoQuUvylsgkNZyC7JZ0Pd7ITVyevAkrTu9iP-6izCgpWqj0gO352ZX57t9127VBUSyxc5QdB6e6xGsCOcr3IeBjgurltE9nnWuji_LzbL1ALF-ogJRUluRUepbxsQzYzZQoVWtjZlzF2lw6itpItiNwqHVYmFdgUNDYNGs4zumC0ClqV3Zt3Oxe_Ek4c8qRG4vRrzTSAd3hnKcOv8vq87xBqPkKIHpBQwr_Sl9oNRvWeWckumcLtofH28bmzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HV6-WG9U_xq0YRWbcclzFG0qD4rqoMHxoBgyx_Um3sdp6Me-b_lNvJ_UYCcM-PqWin-YZR9UATrGBvXDt0XByZJRXsPI0BYMMCidwGiDRMWGXzA_vTUGK2TDrdp-6CA301lCnYo8qhbmblosvhnGqhd26AUNHokPan-jYAT77MOkCVnSwCzYa4Luqlroj7eoUfVJEs4yWJwOodqLkyggyN9qzalY3lpA5R2uPDwE5QhqoOiqj2Fxi9J7pBGHIfheOeMPsGvE6Q31NRpJT487hQFrMH4-XvLsvS4WJBnlc-qDxOKI1GR1p4RrZK3uFlJ55CH-jhesayO-JPrTYqJoxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EizZhGyqTCWyDgYJiOiLQ0RWhGZDlcBs872c7cfu8aYG3_ibxllqzTO7HAmhPlNhBikKQoRUDH7tnT4bMGQ8ln-9WN6GtF14WoTSI1TtjeStA4_DM_TIGND3b9O_NYljEuKW4WAE6eH5vC511DtmF0O7VxT9cnbUcCkSJIp24aFPhURSSRjyZSAcG7YuhvW_3ktjht3K8HDPazsGobnDILXvrlDjYmD5szdjytDuLbyMcDbUO8nIPMeL1TgLgt1dWxawvlvroWWh4dvVDaWaFR_1WViHw_39mCIZgdHeGKIH8Ni0RcdvMJiF5M1wwpZvssCemDCXdYY7W4PbHnJmEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRkLt8-iIh2rSN07pdsjMDlZ0cBWXroXnRtyeNBjZnYUNI1IQmvzI3o4UZKVV_CBnpIMGSsHvDhK_SeONqklsrf4IIBj8-KtBZnIyBzZKTGIqNVofIdmRTlcWQbr4sHqfEcEOfiLcKkjJjSZbHElVApY9Jtrmi-N1dygzk62VLybsfu8qRjfdqi8jP-U7WMdF-A7LcFMlvzdruBllKirTn7Uvs5xefc_Wuu9RU_jCXKZGcxv3-mN1OmbfbzYymur2rU5oWmaxLDSoHeW_6c2I9W2iH3AGcohYGcLj8QlePGZpHhzzisbhtzRdPz929XsV6QEYcGP5zcL-jYxZCyawA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جنگ رمضان روی جلد کتاب‌های درسی آمد
🔹
امسال طرح‌هایی مرتبط با جنگ رمضان و رهبر شهید انقلاب به جلد کتاب‌های درسی اضافه شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/466618" target="_blank">📅 15:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466616">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مقام ارشد انصارالله: تعز عملاً آزاد شده است
🔹
عضو دفتر سیاسی انصارالله، با تأیید محاصره کامل تعز پس از آزادسازی مناطق اطراف، این شهر را عملاً آزادشده خواند و تاکید کرد که این پیروزی با مشارکت نیروهای بومی استان و حمایت مردمی به دست آمده است.
🔹
حزام الاسد در…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/466616" target="_blank">📅 15:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466615">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b7acecaf4.mp4?token=J2jE3ccUmwmNclvhMb591I5HU7LDdn708uQg9nHD2Cmo_Knjua5y7TpwEvh9aJWKAvqaz4DiocooJ6TjyEh12GJVBNJgtI4AjJRJFHtIL6hqswFZDZrWuS8jy3hRoF9x9AAr6OslS0olsnkQXe4Lq4a-34SX97mIGvDqIbMxydPwsF5xWom6O2_klCIW67lhd2JLg3jk_NVsPUDirhXEWwk-3okAQb4gRyjLzmRczmt5IBFvOukyFOzHxSkzejMWboS724zfnfnQnf1YQadi6zEhVwjwZU27d3a9BQtVpf1pDpqcxBXNyQURpAECiFTVyEvTEghRmGQSpqKX3z_TmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b7acecaf4.mp4?token=J2jE3ccUmwmNclvhMb591I5HU7LDdn708uQg9nHD2Cmo_Knjua5y7TpwEvh9aJWKAvqaz4DiocooJ6TjyEh12GJVBNJgtI4AjJRJFHtIL6hqswFZDZrWuS8jy3hRoF9x9AAr6OslS0olsnkQXe4Lq4a-34SX97mIGvDqIbMxydPwsF5xWom6O2_klCIW67lhd2JLg3jk_NVsPUDirhXEWwk-3okAQb4gRyjLzmRczmt5IBFvOukyFOzHxSkzejMWboS724zfnfnQnf1YQadi6zEhVwjwZU27d3a9BQtVpf1pDpqcxBXNyQURpAECiFTVyEvTEghRmGQSpqKX3z_TmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقتصاد فضایی کشور
روی ریل پیشرفت است
🔹
رئیس سازمان فضایی ایران: تبدیل داده‌های ماهواره‌ای به محصولاتی مانند تصاویر پردازش‌شده و نقشه‌های تخصصی، می‌تواند ارزش‌افزودهٔ چندبرابری ایجاد کند.
@Farsna</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/466615" target="_blank">📅 15:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466614">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cveo2Yq3mmI3QbWtCFwdnRCFUPoHRfj5NU0GwGgeNDhplwFDhF3GKgw6AUMCh_FpYE5uuhltKYLP5rS2VOulH1i8O85y7xcPPJyrm_MfzJT0IhPudU1pHAXZi1rNgAhaso6mxLjN1irhyNaURFY7FZ7KrXLKX1707W9zpllxEgfEf0uQngoP32Y6-32cwaP5kHYnQw04LapdBxo7XTL35-uDMfoBwvGlKA71DiihUTYE-khFfqx-kpi9EC8VktmvMeVLkYXwz_6E8t5B38Q2qA5yTRE9UMbn4haSAWx5u6TKkpfwKD5GBtI4VqFucC8K21l4aEJM5-gYRLjDIcReDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساپینتو: تاجرنیا به من گفت فتاحی می‌تواند کاری کند که داوران با استقلال مهربان‌تر باشند
⚽️
سرمربی سابق استقلال در گفت‌وگو با فارس: تابه‌حال مدیری به شهرت‌طلبی علی تاجرنیا ندیده‌ام.
⚽️
از روز اول تاجرنیا به رابطه من و مدیرعامل وقت آقای نظری جویباری حسادت می‌کرد…</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/farsna/466614" target="_blank">📅 15:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466613">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‌ سخنگوی وزارت دفاع: همکاری دفاعی ایران با روسیه و چین ادامه دارد
🔹
همکاری‌های دفاعی ایران با روسیه و چین متوقف یا کاهش نیافته و در برخی زمینه‌ها نیز تقویت شده و ادامه دارد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/466613" target="_blank">📅 15:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466612">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc17e016e.mp4?token=duPmXTw7IN6eA-qJVYftT1ftzqXe11h8k6xcPpW7B-pwS5wHzttbpGo-SlSHVoRcehINuCniJ1mpZfaNfXjq0YT1CVS1tZid9sw5i8F0GoHCu6t45bfk56bVTnJ2jnllxUHzVk9tXi7rtWjXN-JqPm5kQzDjVQwsFmRgLb_HCJABhe-wiiThxj0XFdrO5dbTs_ErsDCh9XNQUnaHD7dYc-MmuKgNYY2CEG-rFV5ysQ7Ep2rsxJNpdYoQ28HQRy3sgwg-3i1mYQK8vAw9JQcn_N8Ay3RJX3KTWby8znTPXKH_NdpWNewLsfVx0-5mAJn4MX9XUHQaC_CILsv89CpL6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc17e016e.mp4?token=duPmXTw7IN6eA-qJVYftT1ftzqXe11h8k6xcPpW7B-pwS5wHzttbpGo-SlSHVoRcehINuCniJ1mpZfaNfXjq0YT1CVS1tZid9sw5i8F0GoHCu6t45bfk56bVTnJ2jnllxUHzVk9tXi7rtWjXN-JqPm5kQzDjVQwsFmRgLb_HCJABhe-wiiThxj0XFdrO5dbTs_ErsDCh9XNQUnaHD7dYc-MmuKgNYY2CEG-rFV5ysQ7Ep2rsxJNpdYoQ28HQRy3sgwg-3i1mYQK8vAw9JQcn_N8Ay3RJX3KTWby8znTPXKH_NdpWNewLsfVx0-5mAJn4MX9XUHQaC_CILsv89CpL6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی:‌ امروز در بخش‌هایی از شمال‌غرب، سواحل جنوبی دریای خزر، دامنه‌های جنوبی البرز و دامنه‌های جنوبی زاگرس شاهد بارش هستیم.
🔹
این بارندگی‌ها منجر به هشدار سطح نارنجی و سبب آب‌گر‌فتگی و بالاآمدن سطح رودخانه‌ها و مسیل‌ها در آذربایجان غربی و شرقی، اردبیل و کردستان شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/466612" target="_blank">📅 15:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466611">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaJtcEG-59xFVWzfsTJZmXv1G-ic74NcX2M8LWBbjiRhvOh80PVIiBmJmfkMPwG6d24FG4CzD5Tl6w9Fpo0sLN4aLLVJV2sEABzF8hTlWdRrVmVXD5PwluWjubXyc-EjzJwXTm_Cb0vTGlRUhwNW9OtB5goOghKYY_Uqw2aDpleRWtbkKBskYKJhmk6FZdlo_Qc3ir0QFTaOKux-V9-vjDu4cIIQUg_3brqyKOFVF-woBf7VkMe-rMS6lJ5_wBDUVEE7JNZV__bCVbqYUTWHBJEAD1AAghRbKGuHXNWPlljYFP1iCeUSux2YIeIxIF2pkUvTpqvYjx9OfSb37NPlDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عیادت رئیس دفتر رهبر انقلاب در قم از آیت‌الله نوری همدانی
🔹
آیت‌الله محمود محمدی عراقی رئیس دفتر مقام معظم رهبری در قم با حضور در یکی از بیمارستان‌های این شهر، از آیت‌الله العظمی نوری همدانی از مراجع عظام تقلید عیادت کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/466611" target="_blank">📅 15:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466610">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/364de1749a.mp4?token=fbicKpZJWBiWscz7MechRp-2d_hfBkRQWqAd1KLqc1oABhuNzxm3OUny7G4BxoTHci0C3VfIYI4PGUShk8itdsTmsd7VPtMl2AkDxA8HtgIv-Wn3qMd0GhoG1_Qvnqo1MkGDVwIAehYq8RmPBAt-rYH8YTOd2f-MNOmANIfui4Y0d3DyPs-WMxEUnpieLjgTcwleID-BOhEiuaHyhsSiIv0JQGiC8fuhgHmkgXHUrNrugexHZMRXKkrMm5aTUFABDe7D2r_SHkIVuJZbIh9sdl_lY3x6MPQUf4LwUTjhYa9iFT7vGJFO5hjyXIw5IdTWHXqMG1QHaje8UZ907aEeew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/364de1749a.mp4?token=fbicKpZJWBiWscz7MechRp-2d_hfBkRQWqAd1KLqc1oABhuNzxm3OUny7G4BxoTHci0C3VfIYI4PGUShk8itdsTmsd7VPtMl2AkDxA8HtgIv-Wn3qMd0GhoG1_Qvnqo1MkGDVwIAehYq8RmPBAt-rYH8YTOd2f-MNOmANIfui4Y0d3DyPs-WMxEUnpieLjgTcwleID-BOhEiuaHyhsSiIv0JQGiC8fuhgHmkgXHUrNrugexHZMRXKkrMm5aTUFABDe7D2r_SHkIVuJZbIh9sdl_lY3x6MPQUf4LwUTjhYa9iFT7vGJFO5hjyXIw5IdTWHXqMG1QHaje8UZ907aEeew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی جغرافیا معنی آشوب و اعتراض را در برخی رسانه‌ها تغییر می‌دهد
@Farsna</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/466610" target="_blank">📅 14:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466609">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1a5676575.mp4?token=dXcubmuYx0GsRThXYC2guzLYPDh8guM8F6XE3CGsMlp0n8Lfas6AJzFUCk2sRMnAjvZXt3l10X_nMjzP0mo9KiK61nZPsjs_QfpLGxDMlBU5KzAErLaGC5JCXMOF15i7iv-erYNXYZ1lcRei4YA4_kIlXaa5_45-MPZ8H2BHnaLLJhqs_7Idru1xs-K4200PI3WpY8WCbrFd8IpN4R3arSTyI9mQsUWPgNsjfOHHDxX-u2TpA0IKnWcEIagqi_5CQPWzrVDDU2mDDwhM_K118STg5vkm-VIveRO-cQ2_xTHJ_PxnNgibYFOWrGvJKR-zijqOplJAfhytfFFzwiUilQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1a5676575.mp4?token=dXcubmuYx0GsRThXYC2guzLYPDh8guM8F6XE3CGsMlp0n8Lfas6AJzFUCk2sRMnAjvZXt3l10X_nMjzP0mo9KiK61nZPsjs_QfpLGxDMlBU5KzAErLaGC5JCXMOF15i7iv-erYNXYZ1lcRei4YA4_kIlXaa5_45-MPZ8H2BHnaLLJhqs_7Idru1xs-K4200PI3WpY8WCbrFd8IpN4R3arSTyI9mQsUWPgNsjfOHHDxX-u2TpA0IKnWcEIagqi_5CQPWzrVDDU2mDDwhM_K118STg5vkm-VIveRO-cQ2_xTHJ_PxnNgibYFOWrGvJKR-zijqOplJAfhytfFFzwiUilQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ذخایر سوخت
نیروگاهی به ۹۰ درصد رسیده است
@Farsna</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/466609" target="_blank">📅 14:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466608">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ظرفیت تولید تسلیحات دفاعی ۲.۵ برابر شد
🔹
سخنگوی وزارت دفاع: ظرفیت تولید تسلیحات و تجهیزات دفاعی کشور نسبت به پیش از جنگ رمضان ۲.۵ برابر شده و در برخی تسلیحات، میزان تولید بیش از ۳ برابر افزایش داشته‌ایم.
🔹
برنامه‌های تحقیق، توسعه و تولید تسلیحات متناسب با…</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/farsna/466608" target="_blank">📅 14:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466607">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572d31cc4d.mp4?token=BzHo_SyiTDfzF74y_Znch0_lYXfPhidhsmpIqtG5vh6K_8ZdHUNLKwx6l64Fvcsc3UaqCv3hRneig8E4GzGwc7SrIxrDNa8ce2dYVUtX2qQQwq8p-Zb_TaahD4RmL9uv90PEQcYDENmzwVUxQCQwWJvi37SGEBmpQuL6Ks2mlTDIhG6wT4hSvpXRthduOT5aAI73xAmC3joKUEa5CArb2pA1WoXCxsbcC7P_odwBoPUOxq8de3jaKs3jIRLn6oJv3E-XjkpudX_MwDwARGmAQRy-gxYgb63zka-GtLDfzWVTeGNjuatzQDES_0joiaKBZzvI1ICr7MLvj4i5JKsxaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572d31cc4d.mp4?token=BzHo_SyiTDfzF74y_Znch0_lYXfPhidhsmpIqtG5vh6K_8ZdHUNLKwx6l64Fvcsc3UaqCv3hRneig8E4GzGwc7SrIxrDNa8ce2dYVUtX2qQQwq8p-Zb_TaahD4RmL9uv90PEQcYDENmzwVUxQCQwWJvi37SGEBmpQuL6Ks2mlTDIhG6wT4hSvpXRthduOT5aAI73xAmC3joKUEa5CArb2pA1WoXCxsbcC7P_odwBoPUOxq8de3jaKs3jIRLn6oJv3E-XjkpudX_MwDwARGmAQRy-gxYgb63zka-GtLDfzWVTeGNjuatzQDES_0joiaKBZzvI1ICr7MLvj4i5JKsxaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بحران قیمت سوخت دغدغهٔ اصلی کاخ سفید در آستانهٔ انتخاب شده است
@Farsna</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/466607" target="_blank">📅 14:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466606">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ظرفیت تولید تسلیحات دفاعی ۲.۵ برابر شد
🔹
سخنگوی وزارت دفاع: ظرفیت تولید تسلیحات و تجهیزات دفاعی کشور نسبت به پیش از جنگ رمضان ۲.۵ برابر شده و در برخی تسلیحات، میزان تولید بیش از ۳ برابر افزایش داشته‌ایم.
🔹
برنامه‌های تحقیق، توسعه و تولید تسلیحات متناسب با شرایط جنگ و اولویت‌های نیروهای مسلح به‌روزرسانی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/466606" target="_blank">📅 14:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466605">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meUNCe0AL15b8vLE-JD6Ud48OHxkncmTzk1AW4Vsa4PhOHVOUldMo-6P4jiI_JUyRd8Na-3iJ3tRN0-rRrvylSybNG9Iz0KZSkjk5lwDAMcuLLgM3TQ76a2jGg792ancnALN98PaHXoEInGA6lxiErVNvPIb9uJz-KUPLNaF48kaVx792gRU3_PxFqRCc_T5rXk5JUxqIJicM_9oRQQf3igrga9aV2TsEQRpNNiA52SXeyQIuNIZp5GwQ7E6R0G1rZrb1AAyo9mI_79DNu6AH8szOG5tYcQjLRGoyAPHYlFqswU8tz3Gm0HpAlSFigozAAtcg2i7b-tvJ0SkH-hfBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره های کاردانی و کارشناسی ناپیوسته دانشکده خبرگزاری فارس تا ۱۵ مهرماه تمدید شد.
🏷
براساس اعلام سازمان سنجش آموزش کشور، مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره کاردانی و کارشناسی ناپیوسته دانشگاه جامع علمی کاربردی
از امروز تا۱۵ مهرماه تمدید شد.
📚
رشته‌های تحصیلی:
🎙
خبرنگاری
📸
عکاسی خبری
🎞
سینما‑تدوین فیلم
🤝
روابط‌عمومی
🎤
گویندگی و دوبله
ارسال  عدد ۱۴ را به شماره ۵۰۰۰۱۰۱۴
🌐
لینک سایت ثبت‌نام
🔗
futurix.ir/go/rxDxXO
☄️
☄️
این فرصت رو از دست ندهید
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/466605" target="_blank">📅 14:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466604">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6520f38466.mp4?token=AL6nGQiC1cRBd8UDRwgDdX4m1LKHb_sG6EjpqJFpe8AGc7tlCG5YoDalteV6YoBzStP_OYlx1-7Iu-hJlgwRv8I8q__3ga45qJuZo6tEFBHvT-2GZQIcFs79xHGW3hsOias_kabvzNZHhJxMFCzElWoQHBhwpkJA1fKP1D4kSmy1ynJMrISjqOPcLPK85Td894McjOj8Bwq70EpIYsSJdfHuw43KvoJVTCUmJvZqc8Ge8SoUNXR7jrsTOw-l1KhpnljKypL75agD2ppTAJ-VLY1oDyxrBKYSbazs3DbW6FRM0uyTeGseGYcf5X5wu_uMM_h3etKZ0_pkBlXVNIKUnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6520f38466.mp4?token=AL6nGQiC1cRBd8UDRwgDdX4m1LKHb_sG6EjpqJFpe8AGc7tlCG5YoDalteV6YoBzStP_OYlx1-7Iu-hJlgwRv8I8q__3ga45qJuZo6tEFBHvT-2GZQIcFs79xHGW3hsOias_kabvzNZHhJxMFCzElWoQHBhwpkJA1fKP1D4kSmy1ynJMrISjqOPcLPK85Td894McjOj8Bwq70EpIYsSJdfHuw43KvoJVTCUmJvZqc8Ge8SoUNXR7jrsTOw-l1KhpnljKypL75agD2ppTAJ-VLY1oDyxrBKYSbazs3DbW6FRM0uyTeGseGYcf5X5wu_uMM_h3etKZ0_pkBlXVNIKUnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از فضاسازی‌های رسانه‌ای تا واقعیت‌های میدانی میان یمن و عربستان
🔹
خبرنگار شبکهٔ العربی: نیروهای انصارالله توانستند مسیر اصلی عدن به تعز را به‌طور کامل قطع کنند؛ همچنین بیشتر مراکز نظامی، امنیتی و سیاسی در مناطق شمالی عدن از حضور نیروهای مخالف انصارالله تخلیه شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/466604" target="_blank">📅 14:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466603">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4bdd7169e.mp4?token=nC5UmsFcqMvPeaY6ECzOcKhxQE6GtIWsFiZDOvikKWlAHzFldcIEiNbTNEL71wQCvt4us-y6mGlHjQT0Edex3ko-L68l9eC9O4WAjXcFV_wEnulmVT51tZVE5Iaf59FGDsnnu26eZ1plihIF8LFC1OfXPghpw5olhD92tKz6w59238--pTMEnX0W-WNnRt-a6OIX3gB5pkF0N3gMeqpUReGRrXSleyXAwei_m4GYvt-xOiBqslrrA0hd54E_kXuLDw_MpKc4l6q43hC4y4P-Gzme3637e4ub3nVj8AOzvT2-cntD5kAYiyxUhKl24fxbiFgjgVOmPyq57FN6x5z09YcEbuL4NDN2f_ckwFU7C9qz7e5GeycDCMlQlZjWSrpS7ACDdbTPl1_uLtvg9DmonEW6ctfOEU_F-nfsW_jWBy13QsYQKVC-YMlnkrpuOg9T6ydG79lw1fxFL3xQOweqAtcnrlms15VW_l5ihdLFoleQDawKxq2d3KUUtlK_7buaaf2zFSiuwjGtmqxaAiAd7xRDTpsz6aSoFdnh-o66YJd1va2zzZPJ7fSnUrP7r0hmhdVb9DRcHroD5pZaGeCl0dyqlLKdtaJ_LEafkQkjoLrSy7nOIpfhQ9KGHaQrfAoHTrDLF9OTIqOy3su-PWUhfEc1MAVev0fmM6q9fqyu87U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4bdd7169e.mp4?token=nC5UmsFcqMvPeaY6ECzOcKhxQE6GtIWsFiZDOvikKWlAHzFldcIEiNbTNEL71wQCvt4us-y6mGlHjQT0Edex3ko-L68l9eC9O4WAjXcFV_wEnulmVT51tZVE5Iaf59FGDsnnu26eZ1plihIF8LFC1OfXPghpw5olhD92tKz6w59238--pTMEnX0W-WNnRt-a6OIX3gB5pkF0N3gMeqpUReGRrXSleyXAwei_m4GYvt-xOiBqslrrA0hd54E_kXuLDw_MpKc4l6q43hC4y4P-Gzme3637e4ub3nVj8AOzvT2-cntD5kAYiyxUhKl24fxbiFgjgVOmPyq57FN6x5z09YcEbuL4NDN2f_ckwFU7C9qz7e5GeycDCMlQlZjWSrpS7ACDdbTPl1_uLtvg9DmonEW6ctfOEU_F-nfsW_jWBy13QsYQKVC-YMlnkrpuOg9T6ydG79lw1fxFL3xQOweqAtcnrlms15VW_l5ihdLFoleQDawKxq2d3KUUtlK_7buaaf2zFSiuwjGtmqxaAiAd7xRDTpsz6aSoFdnh-o66YJd1va2zzZPJ7fSnUrP7r0hmhdVb9DRcHroD5pZaGeCl0dyqlLKdtaJ_LEafkQkjoLrSy7nOIpfhQ9KGHaQrfAoHTrDLF9OTIqOy3su-PWUhfEc1MAVev0fmM6q9fqyu87U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در شب ۲۱۹ کاروان پاراالمپیک را برای بازی‌های آسیایی بدرقه کردند
@Farsna</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/466603" target="_blank">📅 14:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466602">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12adc89d93.mp4?token=Uamoi2BdQDQi9u8VVbAQqBCI8EZW4yKA0X5oJbdd-gGRnTMJQoHRtdkgsD8arDBMFuyDe8LOMXD3_ppwKtpxPWPRF-dTFDPMu5qS6VJs9CNyTJEHu6FRNEK83l5lGkZ8Lt6jmjN_8QqrPLAfEu3G_6yPLRSIjF7fZZGBRQjBCVGoWaA6A19Ne_ttmVsII3LnJAqodK6wmAbNkmhsDEKVfbIxdpJmuXCY8zbOTYHPanJjC-BpjuWqXt4fqBHHVr0-H0Daq4HBc6rJGmRdkUyrdnxMGQd_xPrLBBXXchXJJYh-fa_XVY_W1FVEzQcGGjlFnuUhKOGAdL40FFxyskqA5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12adc89d93.mp4?token=Uamoi2BdQDQi9u8VVbAQqBCI8EZW4yKA0X5oJbdd-gGRnTMJQoHRtdkgsD8arDBMFuyDe8LOMXD3_ppwKtpxPWPRF-dTFDPMu5qS6VJs9CNyTJEHu6FRNEK83l5lGkZ8Lt6jmjN_8QqrPLAfEu3G_6yPLRSIjF7fZZGBRQjBCVGoWaA6A19Ne_ttmVsII3LnJAqodK6wmAbNkmhsDEKVfbIxdpJmuXCY8zbOTYHPanJjC-BpjuWqXt4fqBHHVr0-H0Daq4HBc6rJGmRdkUyrdnxMGQd_xPrLBBXXchXJJYh-fa_XVY_W1FVEzQcGGjlFnuUhKOGAdL40FFxyskqA5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت دفاع: ریشه‌کنی نظامی تروریست‌های آمریکایی و شرورهای صهیونیست از منطقه تکمیل خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/466602" target="_blank">📅 13:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466601">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDJ2JR3HyVYaHTKvuWxR8qzQ676Ls025RH81m2tJ56ZhahxG_x_kMGGM7lCJTIz7ktm2S7v2Aq9kvU5ULta9kjInvbNsDcDUpe7S8uR-0ieYlSksNV1W0P6fUyYlYnYsZV5OC_exeX0fuAdfdwKDM3r8hVp2anTM5mUny-DxoSwkyFjZAg2fCoXGyZNIMwPKQ3xOZOg_6NkC5WpBRRH9Xku9cHNblsXrxcAZQ6HkWaBOhWxVaDEY0TPFiM2uGG--Djg5n4hv4-pD4EgTu_R5p0t1ql-NmlMoEmzEDLPUSWPdoMySOiphwMCxTISXH8iEhibT3UvF66FY_HXJJGm7Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برندهٔ نوبل فیزیک اعلام شد
🔹
جایزهٔ نوبل فیزیک ۲۰۲۶ به فرانسیس هالزن برای مشارکت در رصدخانه آیس‌کیوب و کشف نوترینوهای پرانرژی کیهانی اعطا شد.
🔹
این دستاورد راه را برای نوع تازه‌ای از اخترشناسی بر پایهٔ مطالعه نوترینوهای کیهانی باز کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/466601" target="_blank">📅 13:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466600">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X01-U_LFNdbs1uYba8WW9xg_xyAwg7Dw3b0oDLUQrzsP7IA-9tfbNvZuwVm5d_QaL1ECePpbcjFzYPmN1n11e9koRPGt2Xsp6MpmX7BSX6l0fzkQChaCh8crv4OJg8jRb1h7jPVKGrLaosTQ4FtmyE3F7m8ilipHXh5NbHylcQtXFDFU_Qi82m_T2OSwfZ8Fa_65-I-fo-CRXrFpJOnJVFA_V_8svPpBx2a-ImWP7oKI54b8Pk4nGRfAyB22upvpuV9Q4TWXsz1ADESG44aWn6hv2D6lUz_k_gCK05NERLPDoC1QrTzQ4qGuNokapfN4Gl9r1qxctQLuiy5xLeXvQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گام بزرگ بومی‌سازی: تولید لایسنس PVC2 اروند به ۶۰ درصد رسید/صرفه‌جویی ۴۰ میلیون یورویی و خروج از وابستگی خارجی با همت نخبگان صنعت و دانشگاه
🔹
با اعلام مدیرعامل شرکت مهندسی نوآوری و ساخت فن‌آوری‌های نوین خلیج‌فارس، تدوین دانش فنی PDP پتروشیمی اروند به پیشرفت چشمگیر ۶۰ درصدی رسید و به‌زودی نهایی می‌شود.
🔹
این پروژه ملی که توسط نخبگان صنعت و دانشگاه در حال پیگیری است، یکی از مهم‌ترین دستاوردهای خودکفایی در صنعت پتروشیمی کشور به‌شمار می‌رود.
🔹
این موفقیت بزرگ نه‌تنها کشور را از وابستگی به خرید لایسنس‌های خارجی رها کرده و صرفه‌جویی قابل‌توجه ۴۰ میلیون یورویی به همراه داشته، بلکه زمینه صادرات دانش فنی با برند معتبر گروه صنایع پتروشیمی خلیج فارس را نیز فراهم می‌کند.
🔹
بومی‌سازی و تولید لایسنس PVC برای نخستین‌بار در ایران در آستانه نهایی شدن است؛ دستاوردی که ایران را از واردات این فناوری بی‌نیاز می‌کند و گامی مؤثر در مسیر استقلال صنعتی و توسعه پایدار به شمار می‌آید.</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/466600" target="_blank">📅 13:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466599">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sx0GuNSvYSjsyzVoAFfPuEBtKzvrsP8c-D1mL4jtajybfVYX3PNjoC2LLuqqiWR1tMMBMzinMzUdZXb78QMV_AhHTWxVZckkjnjyGNG-oHoYqRJHmEj6l1IpB25wqdNG5pAEr7Za4OXtmotx2HUhXDwLPBgcb-dgi-iiWncht7tiyABM1MbQgF4AHs9cWlMhAR33zPssn85-WsCF3g9s5x5USw2YJdnyPGvkHsXpM5IX9lUx-WNRgn81h2kJTJhI9n5Toai1FM2INEg29SzMNyn2i0UHXX5HB4Csgcxs1qf8kGeFdBTLNrDHrrNlaOzILmVTzTjK3wmRDqiiIrYY2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
دکتر للـه‌گانی: بانک رفاه کارگران با ابزارهای نوین تأمین مالی، حامی شرکت‌های دانش‌بنیان است
🔹️
با هدف حمایت از استارت‌آپ‌ها و شرکت‌های دانش‌بنیان، تفاهم‌نامه همکاری بانک رفاه کارگران و شرکت نهادین‌آرمان از شرکت‌های فناور فعال در حوزه نفت‌، گاز، پالایش و پتروشیمی امضاء شد.
🔹️
این تفاهم‌نامه طی مراسمی که روز دوشنبه 13 مهر ماه در محل این بانک برگزار شد به امضای دکتر اسماعیل للـه‌گانی مدیرعامل بانک رفاه و مهندس همتی علمداری رئیس هیئت مدیره این شرکت رسید.
🔹️
مدیرعامل بانک رفاه کارگران طی سخنانی در این مراسم هدف از امضای این تفاهم‌نامه را حمایت از شرکت‌های نوآور اعلام کرد و گفت: این بانک در سال‌های اخیر به روش‌‌های مختلف از این شرکت‌ها حمایت کرده و در راستای ایفای مسئولیت‌های اجتماعی همراه و همیار این شرکت‌ها در پیشبرد برنامه‌های اجرایی بوده است.
🔹️
وی افزود: در مسیر توسعه کشور، پشتیبانی از این شرکت‌ها از اهمیت فراوانی برخوردار است و منجر به بومی‌سازی دانش فنی در صنایع مختلف و قطع وابستگی به واردات می‌شود.
🔗
متن کامل خبر...
#خواهیم_ساخت
#بانک_رفاه_کارگران
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/466599" target="_blank">📅 13:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466598">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/466598" target="_blank">📅 13:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466597">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzt3YDOnH-IJdpWSXmlVahJUfQ0o3JF3BuFrZi4HfhGXjpEeJY4PIA7viYIg5DXovo-u_KZBqERR5_vsWwtR9rB5B-6eJsV8wIKt9eH_eF8rDItfvD_ZVNXjH-hRGyh7dbfQxnuTMfxodPnCqKUbtjyJWdmxf4H0YwJH2JqzaXQETivd4Gjtrt12kZEIEuAdX433axpCpErZyNkWZcji_rYdnIi7qAhLNYaYaPyGkuoRQ3eLrHebn-ff4BsaYsAhiq-s1Li3E4vdgcLwsyNKm-TsLRXH8fDp7x7fq3g7-JMhPwbYDMHmhLSkiTTpCkzgCzcSrQSNbAP7kBDjWCFcHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصابت موشک‌های یمنی به ریاض
🔹
منابع محلی از شنیده‌شدن صدای چند انفجار در پایتخت عربستان سعودی خبر دادند.
🔹
رسانه عراقی «نایا» گزارش داد موشک‌های شلیک‌شده توسط نیروهای مسلح یمن، ریاض را هدف قرار داده‌اند.
🔹
به‌گفته این رسانه، انفجارها در محله «المصفاه» در جنوب…</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/466597" target="_blank">📅 13:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466596">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YX-Ih-o3LuUPHgw__r4ETXd045GZvrnO6CTZRNBRo_RoPtBpqyi2m2H-JtZUIOmfSJoFYqn5Xf49U7oX8Xbllf0ZvbdWzwNdpez_rkSW9Kgfhs7ZbXcWGaxXG_kQoEV3eHVe1Ow9Ul-nOButUHyaqIRFBoBVkHT7dTOXxc0ITavzbvTDAs3ai7oygGdLWfCzL90RgwQLAT9Er8KmlJQeR3BJlG0lsWQ5TPdB-l-qXixbc6ufbAeo0uGK6lkHfS2iZTgvftN7q54tkz3KFyDtbqucgPoYDho34MUhDGpIZ5FBPrnT1H_1FXY-Tr10MnHpeAHGsYQXtLuOv0KwTgTvRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن فرودگاه أبها را با موشک بالستیک هدف قرار داد
🔹
نیروهای مسلح یمن طی بیانیه‌ای اعلام کرد که فرودگاه بین‌المللی ابها را با یک موشک بالستیک هدف قرار داده‌ و اصابت این موشک دقیق و مستقیم بوده و به توقف حرکت پروازها در فرودگاه بین‌المللی ابها انجامیده است.
🔹
نیروهای مسلح یمن در ادامه با صدور هشداری به همه شرکت‌های هواپیمایی جهان، از آن‌ها خواست که از ادامه پروازهای خود در آسمان عربستان خودداری کنند.
🔹
در این بیانیه بار دیگر هشدار داده شده که آسمان عربستان به میدان عملیات نظامی نیروهای یمنی تبدیل شده و آسمان مناطق مقدس مکه مکرمه و مدینه منوره از این هشدار مستثنی است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/466596" target="_blank">📅 13:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466595">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انهدام باقیماندهٔ تیم‌های تروریستی در سیستان‌وبلوچستان
🔹
روابط عمومی قرارگاه قدس نیروی زمینی سپاه: تیم تروریستی تکفیری که در ترور علمای اهل سنت استان، شهید مولوی یوسف گرگیچ و شهید مولوی محمد انور ریگی و نیز ترور ۲ نفر از نیروهای خدوم فراجا در قطار خنجک زاهدان در ۱۹ شهریور دست داشتند، به‌طور کامل منهدم شد.
🔹
در ادامهٔ شناسایی سایر عناصر و پشتیبانان تیم منهدم‌شدهٔ در منزل‌آب زاهدان، ۲ نفر دیگر از اعضا این تیم دیروز به‌هلاکت رسیدند.
🔹
در مجموع ۸ نفر از این تیم تروریستی به‌هلاکت رسیده و ۴ نفر دیگر نیز دستگیر شدند.
@Farsna</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/466595" target="_blank">📅 13:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466594">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8108fd17d0.mp4?token=U6BYXhH4uHsFWmHwhivWxA65dfLUmDtoZzU8ObYozH30OhDzf28xVu6QbF7JIEP9dwYm4aYfwBaeMnEk9Fp5WVN9FfFagx11aK14jML-gaOJ_q3loZF1J3qMC11qlwMJ8bQp-rTILEn2Cmkrsw3oQnwcEW7M0gBINoqpZ4CqQPsPasm9SM_EXcrX7pCGdmCND6QDFFcLQRX6KaHOGPt71omzVUB65YJoP-bb1yjeMutb9vEBFTPm7T5Qm0gMNYZoqFEqL3xpEgDh_J4B2KvWOKB5m_i2Wl4w-Jmpdtp6ejl7rdQf6MfGiaqozu-F06Cg-2T5ChPCNtqH23E2_bDkdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8108fd17d0.mp4?token=U6BYXhH4uHsFWmHwhivWxA65dfLUmDtoZzU8ObYozH30OhDzf28xVu6QbF7JIEP9dwYm4aYfwBaeMnEk9Fp5WVN9FfFagx11aK14jML-gaOJ_q3loZF1J3qMC11qlwMJ8bQp-rTILEn2Cmkrsw3oQnwcEW7M0gBINoqpZ4CqQPsPasm9SM_EXcrX7pCGdmCND6QDFFcLQRX6KaHOGPt71omzVUB65YJoP-bb1yjeMutb9vEBFTPm7T5Qm0gMNYZoqFEqL3xpEgDh_J4B2KvWOKB5m_i2Wl4w-Jmpdtp6ejl7rdQf6MfGiaqozu-F06Cg-2T5ChPCNtqH23E2_bDkdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجهٔ قطر در دیدار با پزشکیان: امیر قطر شما را مثل برادر می‌داند. موضوع خلبان‌های ایرانی را هم با صداقت پیگیری خواهیم کرد
🔹
محمد عبدالرحمن آل‌ثانی در دیدار با رئیس‌جمهور ایران با بیان اینکه «دکتر پزشکیان نزد امیر قطر از جایگاهی ویژه برخوردار است» گفت:…</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/466594" target="_blank">📅 13:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466593">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce928690f0.mp4?token=HfyWtaIE_MqxsrmkGytm8DGsaY7yF7qxkH9-Tw6xjmeJeVeR3ziHqu1Q_VSdZ6DCCxUQYYet3iZ1IzFIRslJ06TrFpy7DY5kqs3Kg5t4bidDbPqYQowuD76foVC9TJZTlzbAf2lpf9LaYJ4Dfbqm4eblVDv1khHPMyXmGoCtgr6dqI98Kdq0EvTcu1Cu9P6Ia790wQqcTpZUACofKY_SLlfGiEdBFhPAsuM4wh7VR8fPiyUqXofDr0RLj_UHAjzN3JPSUB-e5ulmWeqqXr6HIy0AHa7YIpGAJjkMU0e3GWgE_vGu45HAbOFAuq2OdTB3ujNI1aLneCLCKmb72AGqIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce928690f0.mp4?token=HfyWtaIE_MqxsrmkGytm8DGsaY7yF7qxkH9-Tw6xjmeJeVeR3ziHqu1Q_VSdZ6DCCxUQYYet3iZ1IzFIRslJ06TrFpy7DY5kqs3Kg5t4bidDbPqYQowuD76foVC9TJZTlzbAf2lpf9LaYJ4Dfbqm4eblVDv1khHPMyXmGoCtgr6dqI98Kdq0EvTcu1Cu9P6Ia790wQqcTpZUACofKY_SLlfGiEdBFhPAsuM4wh7VR8fPiyUqXofDr0RLj_UHAjzN3JPSUB-e5ulmWeqqXr6HIy0AHa7YIpGAJjkMU0e3GWgE_vGu45HAbOFAuq2OdTB3ujNI1aLneCLCKmb72AGqIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ رشیدی: جلسۀ رای اعتماد به وزیر پیشنهادیِ دفاع یکشنبه یا سه‌شنبه ۲۶ و ۲۸ مهر برگزار می‌شود
🔹
عضو هیئت‌رئیسۀ مجلس: درخصوص برگزاری در صحن مجلس تصمیم نهایی گرفته نشده.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/466593" target="_blank">📅 13:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466592">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43a8657d55.mp4?token=rxBy-V0WspQGYsy00zFlGYdFmfMmU8c1Z4aIfbRYbkXsBCwm5DhVEYNV5nls64wwPO3okAwlaKoU8B-6HbFEyhS-z3XtlYLveGMqWWkW7wjQJRpkRrfmShsV2Hl_6q8ohkKZwM8qa3S61Vb7r505OdzJCQXtzZOxIq6HNuvXa6AaybT7CMlS1inVqhkNWILnSHy6FD_g-ow_cuxhgWQUggwW-QjhajhMqTmjtluXFnXj3dZIJmSQmlM-UbiWtVgEYbS7UFAyZG7P_oOK2WJLQVTJE_SwX1zqgc0_H5QR7r5EFvSDu9ZQGltqUhJfqHVTCB9-PemOzSbAyl_V9YTQIop08yxssyFZ6tFqnbz9Q8gmxS_zkR8XIEiJUKAy674ZvCU0gusAbZ1fOICisSHbsHV4r0sa_ihd4ApsADZBU196b6P_ml69HGCWybrFR9BZ7EhwEygI8JgNMMBf_l0ZKpIsjpfdIsAzky8SJ-augvkTfH9jhLyWt7ONeBg848p44BmbANJivu1pa7vqjKDKdCaZjoqOl0dn_a2wBKQZLPuqXL5sg58fBT4x1qKbGj88kuNnYo22MxfTRbGdbnC4IlJmCFyza48vBfPW9dTF00I0TCk3v74h8kLIh7ohsnF7kQLae_dhRkJ7a4XxSerXPlESq3JK_QRQlYm7WRX6UGY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43a8657d55.mp4?token=rxBy-V0WspQGYsy00zFlGYdFmfMmU8c1Z4aIfbRYbkXsBCwm5DhVEYNV5nls64wwPO3okAwlaKoU8B-6HbFEyhS-z3XtlYLveGMqWWkW7wjQJRpkRrfmShsV2Hl_6q8ohkKZwM8qa3S61Vb7r505OdzJCQXtzZOxIq6HNuvXa6AaybT7CMlS1inVqhkNWILnSHy6FD_g-ow_cuxhgWQUggwW-QjhajhMqTmjtluXFnXj3dZIJmSQmlM-UbiWtVgEYbS7UFAyZG7P_oOK2WJLQVTJE_SwX1zqgc0_H5QR7r5EFvSDu9ZQGltqUhJfqHVTCB9-PemOzSbAyl_V9YTQIop08yxssyFZ6tFqnbz9Q8gmxS_zkR8XIEiJUKAy674ZvCU0gusAbZ1fOICisSHbsHV4r0sa_ihd4ApsADZBU196b6P_ml69HGCWybrFR9BZ7EhwEygI8JgNMMBf_l0ZKpIsjpfdIsAzky8SJ-augvkTfH9jhLyWt7ONeBg848p44BmbANJivu1pa7vqjKDKdCaZjoqOl0dn_a2wBKQZLPuqXL5sg58fBT4x1qKbGj88kuNnYo22MxfTRbGdbnC4IlJmCFyza48vBfPW9dTF00I0TCk3v74h8kLIh7ohsnF7kQLae_dhRkJ7a4XxSerXPlESq3JK_QRQlYm7WRX6UGY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت اطلاعات: ۳ هستۀ عملیاتی گروهک تروریستی-تکفیری در جنوب‌شرق منهدم شدند
🔹
اداره‌کل اطلاعات سیستان‌وبلوچستان: این سه هسته در شهرستان‌های ایرانشهر، سرباز، سراوان و زاهدان و با همکاری اداره‌کل اطلاعات استان هرمزگان، در شهرستان قشم، شناسایی و قبل‌از هرگونه…</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/466592" target="_blank">📅 13:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466591">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwOuCJkW9LKC9DtXUKCW0SaDGwaOwEmcxV0YOfxPSJNg5i0M7GUSUn0tkIxCjwREMfkzm6VuH14gxFHBwGaN1AyO4gMafXIKQJtZXDsCmih3T3zE8M0KCglk5UcvYiCxys_Kv1yUcUmXXC1Dk5G-_SYjePztbzbT46gtLPReoAaGqn4DpeSRBsFcpQHZ7eNHu8ryySZZe8X8VmmrSA1zc01Agg1AiHP-yEtGC1YwYGn7q3OzRIFZ8LwszIlOYGtTRfyXWUU_r7aWokfpDNBAlSv-fIN55ycdINZsilwFd1ailAEQ2IiSoC60v1Ui3-wsskKakHGfElVNmy8b8zC0Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس به یک‌قدمی ۸ میلیون رسید
🔹
شاخص کل بورس در پایان معاملات امروز با رشد ۱۸۷ هزار واحدی به ۷ میلیون و ۹۷۷ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/466591" target="_blank">📅 13:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466584">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RVPw5zogEpMFn-d4kbJOMtmZR3hi5umQxiyFzMBDAffhFITMv6ewbpG-rAtV4KKMXRT9oBw7MR6E4a4fzkoluCHfkP8yF1A_W2ct5uwogBbXf2twgZc58Hg8vWnewhBkgPWzPNr_cOwpvA62AdGwFmf1_ZfJlFye0NjUWPTbU4a-hUltKyUewBYW_zqP-XDUgyOMHcC8W_rVXWNrbzMFcl5UXokMaJDl5628bvLe88txJJwNNQ1V-0F5WOrO6LkEADWXZyd28X9lSQ__6_JXEeMYdsPKYq6-QdZYKdSrQiWEZaKZefDKTIEbNNOebsDc0rozM-7uATFN4apjsT8QNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fr6EIIOxsIMl5-tvMjhgwZac7G_D0HuUxk_egzsHhBScKqt9NE-2-ABX8vLA9RoyoSngEkKhT_WJgnhXviaYotTLeEtDNRH07WMyVb-pjEStjZ1tcF68_36CSRtOrdkeCsYbV6-jTy2EiPLHCPLDv-leSFxAVjlvA2IV3XZeQsRtZpdRtp8y1ok12MKrOJF9S3ZerYQc3XaJ8dVrn_Ip6vT1vG9TOfiBB9IGGr-fbh-QxodykMT3Pcavve1sfiMPcO0c0QHSD8Cgxod0MwO7jrnmy1DHIETzAOG6MHjgLoHTQNGD4FfoOi_KQ9HPkbfod2xCDnlf66CDVxXD7rqDWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pczmelpNVuoh2q1sWxp7N_meuP9Bz6yz4cILWBaWEpnqpDdO61YV1VjW7x5kqfR5WRdeiyS1PQ9XCouy_Xz9PnwN46W-WCdQ71OhnFxMrXXTYk0stYBtFyC2E_LwG05G9pySrbTaXqMz9W5LPUZ7r0f9iaDukgDZbu9zLPvCnif2KxjVO75jzs9slB3la1_l4dRUJcVEij54TCYum6bCOqP1BKmV9UMxq4IZpIjN2D2sCgsiF83oCZEwCvUwM25pFQtf5cZtJ0UHUC_d5JL-uqNJnP-YL9Wl9dVKTsmuGllH1nW472pvmB6hOPgV-UZ6KZOpI_ognGNuwdwoJ0dzNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CnBVjin8lWGdqkaWQLl2Tsfn-bKOkKCfFYFNByWP-Pk6UBm-kXiSZh4boEkNUkwvFiKyOG-vC14TfWsdR4A19iyRY7eh5ojt1MTKeyv5AX-kvjx4v8e1eVn0rQcmImyofbRAAWEs4iS7BdrofeIXwa8XpgObXonGk7v8nDizptHQ65X4CDpBgZyCrL1MnEBfVgAAna3JvEdvCprhJYTkgcggd92Q03i8aBgTMBb3o20VTfR_LUyLR6yMvrgXr910KF0_B3cRc_ik85_mgAvyYQfYq-arXvfEL7Twd-zDrGJ6HJNUeT3GGQwSVhjRgTzkJvmEKKUMM3JNku06BJheLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oIuJtHkqSh7Hv9fN6sOYwoCjvD9yrdLpOP2Th3-uxK1V3UNlRyVlzjQyvPy5k1N1DvWJ8yhppjDKWStQN-Dydqk2duwA9cLjJ-RwLWGJwtTewSh32HOwEj0cOXabVxabeqhf5NsyYmW5lFEh7JcrFIEnUZoGPGXcOsPcsEJWEeV_xIFEjuOwdwL8TXue8mG-La_E-2v29ocFiXi-wB2EaEkftK_08NhVim53fR153-AmSiS3HTIgRJQQFoQrL9uCklee8TjS_D2Rmt3C6-wAQifOTafal5dt7ijHHO7CRsYJwxMLEK4-fkilg5LTAoLLIpP7Ng1Z89pWeCos6HG0Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7kFesjaOMbXfNDj6bo5MP2nzDbUut_uJCYhD0ShrO0dRTTZ-0eraeuXhvBy0uY5c5QwkQGZaARJICnFenV--CyYsnRCIQVRJLXTjLw123VJ3V0gFeIOjASQG9EJjZ-Bce1ngG7kJAik4ZKZE2NilGJNyjUNmSh7K7R5R2COnBVX8Zsc5qvfsg-WnWWQgKrejjRYjHW9Fdgr9K-vEGFSz8Br_Yx1hPrM5jTbQbPvU-zBjlu8pnlMMBQhaEuqkWmWv-UsFidJBcQK5IDWSIb3JDsYrl2DIRRRrSLOs-UiMmlM4EYpYOnfUd0ic-3nK6Ys7ORKVnolrHAqc7J1N-8Yqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsI3x2Cxvuyd93Fh5-1qVJtohWx7m8uj0DFz2BwliuD8UpRfo4TJK4A40CiLjSO1qcBhgIRAPwwtZHyIbfWW4N-DSuQ3xA7ftkBvteMQpMFXJgHokH7wYKYYD29Aq0zo2A06dTvdI9_Rpn3_2QXVcXv4jLgaQ5bZphrMiK-hfSzrrRtNGYFtGCk629esVXBIY4VBUG_pKHOiIuH6MLmtNTUXTkK95srA7Hf9XMbjvFSbbIgys4GThHe1a-vkBpWHvckEun0JaN0IBEfJ9lkeeVGoYSkgJXjFqDj_QCSf3Eyg-Yq47hk75L69ate6nXEK6lAqGOEA1U2P2f8hhaZtZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن عاطفه‌ها در مجتمع نابینایان شهید محبی
عکس:
زینب حمزه لویی
@farsimages</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/466584" target="_blank">📅 12:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466583">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fc97edf18.mp4?token=U9MGbBuhhwbZ-kAPYZBn8aeydYUKGC9cDJDV7Tn8RnpJgOx9-g6MIYBBTlaGjmJMSV9XFuxUmFgLCgC_iZIE1DSqsCq87bYezNCGc5s77CxuIVlwcVIAxAwLLfQh9EGICn21Gc10bCyrLIOW2ZSEh5WWBUAzftvRkZguoKj3iEmvQYAsmTjj9-snEWX_LPj4EI1GN0SaS9aHYa3B0HRnRIeCOgqmy9fw4mM-6wmKRGDW9TY9JRtyyMOJ8k6IB-Yhjp7ewiXVP9_m9EQdmld6YkipjfHNafwJ-PxPuO5JjQ3NFEjzCEDWbTsyHyqG08A5gx8KNm_ii6uVdMiWbVziFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fc97edf18.mp4?token=U9MGbBuhhwbZ-kAPYZBn8aeydYUKGC9cDJDV7Tn8RnpJgOx9-g6MIYBBTlaGjmJMSV9XFuxUmFgLCgC_iZIE1DSqsCq87bYezNCGc5s77CxuIVlwcVIAxAwLLfQh9EGICn21Gc10bCyrLIOW2ZSEh5WWBUAzftvRkZguoKj3iEmvQYAsmTjj9-snEWX_LPj4EI1GN0SaS9aHYa3B0HRnRIeCOgqmy9fw4mM-6wmKRGDW9TY9JRtyyMOJ8k6IB-Yhjp7ewiXVP9_m9EQdmld6YkipjfHNafwJ-PxPuO5JjQ3NFEjzCEDWbTsyHyqG08A5gx8KNm_ii6uVdMiWbVziFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جانشین فرمانده فراجا: ورود افراد هنجارشکن به اماکن انتظامی ممنوع است
🔹
در داخل اماکن نظامی باید حجاب و هنجارها رعایت شده و ورود هنجارشکن در داخل اماکن پلیس ممنوع است.
🔹
چادر گذاشتن هم ممنوع است، خودشان باید لباس درست بپوشند، آقایان با شلوار پاره و لباس مارک‌دار حق ورود ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/466583" target="_blank">📅 12:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466582">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/466582" target="_blank">📅 12:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466581">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">رئیس نظام پزشکی: سالانه ۵۰ هزار نفر براثر آلودگی هوا می‌میرند
🔹
آلودگی هوا با بیشترین اثر بر دستگاه تنفسی بیش‌از ۵۰ هزار مرگ سالانه در کشور ما رقم می‌زند و روزانه بیش‌از حدود ۱۰ هزار میلیارد تومان آسیب اقتصادی به کشور وارد می‌کند.
🔹
در کنار مرگ‌ومیر و مصدومیت‌های…</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/466581" target="_blank">📅 12:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466579">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نامۀ معرفی وزیر پیشنهادی دفاع اعلام وصول شد
🔹
نیکزاد: نامۀ رئیس‌جمهور برای معرفی مهرداد اخلاقی به‌عنوان وزیر پیشنهادی دفاع اعلام وصول شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/466579" target="_blank">📅 12:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466578">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a8ae2eac0.mp4?token=UYixl7DZW-Xv9z_Yaz6dyfRhwJUyh_e6hVMDCdyHVVhbTX9d8MGMqiybrynJIWFiIgSPEn4lHf45lPMLKzaJvEvf_BLRJ-vA8Z7-JSVKQgkF-CsU89xftVTFBeCH2VqN0DxdTdOUICm1FLDYJdOTma8sppW7Ls_22Y_2MqKmNhQNpBtO81xLSfrg8gVMf9ZZa21gOGyYd05s6-RL1nxd-RkOAc1dLtut9hX-YRsEhVaOetOp9HoKNyc1OfpGfBPiBJd6T-tJG2ipZOdLuh0BGjaDJt8vmNuqiHfB99mLXlsj63diVPQIz4czdZK0iGLtYvmGwmvm30LsI2t8jKDWXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a8ae2eac0.mp4?token=UYixl7DZW-Xv9z_Yaz6dyfRhwJUyh_e6hVMDCdyHVVhbTX9d8MGMqiybrynJIWFiIgSPEn4lHf45lPMLKzaJvEvf_BLRJ-vA8Z7-JSVKQgkF-CsU89xftVTFBeCH2VqN0DxdTdOUICm1FLDYJdOTma8sppW7Ls_22Y_2MqKmNhQNpBtO81xLSfrg8gVMf9ZZa21gOGyYd05s6-RL1nxd-RkOAc1dLtut9hX-YRsEhVaOetOp9HoKNyc1OfpGfBPiBJd6T-tJG2ipZOdLuh0BGjaDJt8vmNuqiHfB99mLXlsj63diVPQIz4czdZK0iGLtYvmGwmvm30LsI2t8jKDWXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۰ بار قصاص و حکم ۱۰ سال حبس برای کلثوم اکبری
🔹
سخنگوی قوه‌قضائیه: کلثوم اکبری متهم به چند فقره قتل عمد و شروع به یک قتل عمد است.
🔹
در خصوص قتل عمد، برای ده فقره، حکم قصاص نفس به‌صورت مستقل در حق اولیای دم صادر شده است.
🔹
در مورد قتل محمدعلی حدادی، همۀ ورثه…</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/466578" target="_blank">📅 11:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466577">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b746fe3f45.mp4?token=uLZVWqo9gAEGBHSs2ZpmBOD_ki5hyeUxXR3XG9eFJLaDJzvTTT3ibT2svVGI0u5IUNZeMu4CsPFvbEHm6L65WN13fVS58FYZDWaYh1WRuknr3xQQJk_5TWy4ZZGsmuhp-_1zH-Eygs85wj66tPZMcpuncDb4jWBiMiemlBntpO0Y6weALN82TbQuRXnpO3Jex0tF-EFCLONFSmSAhuSaAvzlQMdwrF-0mAnYTxyLF01RjOOlN8EGV4uD_GnAzEdS9NQJ9XgJwYE5rTMOdfIu06HoEWDLEc1m-rWLq7kxZaLZtDijWm2LDuw68oRQUK6MbvjMSZftSyK0U4d6ogBJPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b746fe3f45.mp4?token=uLZVWqo9gAEGBHSs2ZpmBOD_ki5hyeUxXR3XG9eFJLaDJzvTTT3ibT2svVGI0u5IUNZeMu4CsPFvbEHm6L65WN13fVS58FYZDWaYh1WRuknr3xQQJk_5TWy4ZZGsmuhp-_1zH-Eygs85wj66tPZMcpuncDb4jWBiMiemlBntpO0Y6weALN82TbQuRXnpO3Jex0tF-EFCLONFSmSAhuSaAvzlQMdwrF-0mAnYTxyLF01RjOOlN8EGV4uD_GnAzEdS9NQJ9XgJwYE5rTMOdfIu06HoEWDLEc1m-rWLq7kxZaLZtDijWm2LDuw68oRQUK6MbvjMSZftSyK0U4d6ogBJPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای طرح هدیۀ ماهانه ۳.۵ تا ۴ میلیون به نوزادان متولد ۱۴۰۵ تهرانی چیست؟
🔹
شهردار تهران: اعتبار خرید، خدمات فرهنگی و سلامت و بهداشت به نوزادان متولد ۱۴۰۵ تهرانی تحت عنوان طرح «چشم‌روشنی» اختصاص داده ‌شده ‌است.
🔹
اعتبار پایۀ این طرح ماهانه ۳ میلیون و ۵۰۰ هزار تومان است که در حساب شهرزاد مادران شارژ می‌شود.
🔹
از این اعتبار، ۲ میلیون و ۵۰۰ هزار برای خرید کالاها و اقلام ضروری، ۵۰۰ هزار برای خدمات فرهنگی و ۵۰۰ هزار برای خدمات سلامت و درمان اختصاص دارد.
🔹
برای مادران متعلق به ۳ دهک پایین درآمدی، ۵۰۰ هزار اعتبار اضافه در نظر گرفته شده و مجموع اعتبار ماهانه آنان به ۴ میلیون تومان می‌رسد.
@Farsna</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/466577" target="_blank">📅 11:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466576">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dfdeb3870.mp4?token=iDRhFCrRoWzoW1oDJMW8o-toXfc_JCHDI6TvGe_6R7pjIs5m25TwH-KE6F23rfIHGQDvrGfLeIk2X5VjNdM5pOYWtAzCL-uFt7Q-kqWOIzDRbp_WU7htQUOVo-eBQ1EsF_uEz2F6KPKpKNAhDtpM90413npa-HF3l5SdQ6_Ck_k3Hf5aBnhsxCQkXItzRAPzZB2qL8rVIscXeDEwNSfdCgXxvVFJ6We78kxRzLUYCC0zjZLkWVCV-BYEEnSbNTuKyWIvTfOW2754XHJL049TDMXtcxF5Fm_GBJ5WebKK9blc3aTb8QiGomvY95um_dp99YZh2rACiBDCXEQ82F55sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dfdeb3870.mp4?token=iDRhFCrRoWzoW1oDJMW8o-toXfc_JCHDI6TvGe_6R7pjIs5m25TwH-KE6F23rfIHGQDvrGfLeIk2X5VjNdM5pOYWtAzCL-uFt7Q-kqWOIzDRbp_WU7htQUOVo-eBQ1EsF_uEz2F6KPKpKNAhDtpM90413npa-HF3l5SdQ6_Ck_k3Hf5aBnhsxCQkXItzRAPzZB2qL8rVIscXeDEwNSfdCgXxvVFJ6We78kxRzLUYCC0zjZLkWVCV-BYEEnSbNTuKyWIvTfOW2754XHJL049TDMXtcxF5Fm_GBJ5WebKK9blc3aTb8QiGomvY95um_dp99YZh2rACiBDCXEQ82F55sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استخدام سرباز فراری ممنوع است
🔹
رئیس سازمان نظام‌وظیفه: با کسانی که سرباز فراری را استخدام کنند برخورد می‌شود؛ حتی اگر بخش خصوصی باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/466576" target="_blank">📅 11:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466575">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وزارت اطلاعات: ۳ هستۀ عملیاتی گروهک تروریستی-تکفیری در جنوب‌شرق منهدم شدند
🔹
اداره‌کل اطلاعات سیستان‌وبلوچستان: این سه هسته در شهرستان‌های ایرانشهر، سرباز، سراوان و زاهدان و با همکاری اداره‌کل اطلاعات استان هرمزگان، در شهرستان قشم، شناسایی و قبل‌از هرگونه اقدام خرابکارانه و تروریستی منهدم شدند.
🔹
۲ نفر از این تروریست‌ها در درگیری با نیروهای حافظ امنیت به هلاکت رسیده و ۱۰ نفر دیگر از اعضای تیم‌های تروریستی وارداتی دستگیر شدند.
🔹
این تروریست‌ها دوره‌های آموزش‌های نظامی، بمب‌گذاری و ترور را در خارج از کشور گذرانده و با قصد تخریب و ایجاد ناامنی وارد ایران شده و در خانه‌های تیمی مستقر بودند اما با کمک گزارش‌های مردمی و همکاری فرماندهی انتظامی و سپاه سیستان‌وبلوچستان به دام افتادند.
🔹
از تروریست‌های دستگیرشده مقادیر قابل توجهی سلاح و مهمات جنگی کشف و ضبط شده است. ‌
🔹
همچنین در ادامه سلسله اقدامات مستمر و هدفمند اطلاعاتی در ضربه به باندهای شرارت، سربازان گمنام امام زمان(عج) موفق شدند دو باند سازمان یافته‌ی شرارت و مخل نظم و امنیت عمومی را متلاشی و ۵ شرور مسلح را به همراه مقادیری سلاح و تجهیزات مربوطه دستگیر کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/466575" target="_blank">📅 11:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466574">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6efc31add.mp4?token=Hcufhg73tkdd8P8eFFBMtjNdtYy4CCAxr6xAlpz10WTQMRalnHgmUdnqBcKHKoj4TaTLXTvn2e_FVMK8wIgQX4yx4EB6n-UcHhkNFnAW0t_C30u5d-fjWP4tgJQvvja4E5U6RZDyWFb4Tfk8Uf6UX8tyDJ5-G_Yl_QpjAVTlOR9RcTlgwoDu3wheZsWFnYof66gFaMAFYUxKtkutGxIkVjJ4UodnPJopwsqvLhVq2dal4GH9xdW_g3csEItBLhwa61jYte2VYIrSQe4PKZcoEhHezxrzlG907er5mLWhExdzLqhEnHzOhTapa9ALPstxZT_hktSp_Pq-Fbh8WdV4HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6efc31add.mp4?token=Hcufhg73tkdd8P8eFFBMtjNdtYy4CCAxr6xAlpz10WTQMRalnHgmUdnqBcKHKoj4TaTLXTvn2e_FVMK8wIgQX4yx4EB6n-UcHhkNFnAW0t_C30u5d-fjWP4tgJQvvja4E5U6RZDyWFb4Tfk8Uf6UX8tyDJ5-G_Yl_QpjAVTlOR9RcTlgwoDu3wheZsWFnYof66gFaMAFYUxKtkutGxIkVjJ4UodnPJopwsqvLhVq2dal4GH9xdW_g3csEItBLhwa61jYte2VYIrSQe4PKZcoEhHezxrzlG907er5mLWhExdzLqhEnHzOhTapa9ALPstxZT_hktSp_Pq-Fbh8WdV4HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: محمدباقر خرازی در بازداشت است و پرونده‌اش هنوز به مرحلهٔ صدور کیفرخواست و حکم نرسیده است.  @Farsna</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/466574" target="_blank">📅 11:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466573">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7227f9c501.mp4?token=vo5fukUuC1urNeC2DN-tJHYq4aNnuOs7hKRxGDBT9s52I3m61CUHxuSJ9HqS6lG_Eo6szsjGShwzxG4MW0LonxFFUtZItnSTFqn4xV-70F-ZQ-Bwy4C7JfK48KeEh5HETaFcP3Q2FAuODQDIzkDjWhhschwRcLC6zzaKNAVcUgG2CUezlp7mUWIic6kewIMCQmHLFdVFrUmA3xqacuwZ37LUDbiqX2ts43vBR_7fQIKHMetzL5nS7-QC0zH4GzEb00iij-la57tXXLIcmFl0dHIdvyg6LlmsLH2744FUunl5d5FWP2wrdzNU_Vs-wVUbhttF2qOZmKypBi2E6j26Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7227f9c501.mp4?token=vo5fukUuC1urNeC2DN-tJHYq4aNnuOs7hKRxGDBT9s52I3m61CUHxuSJ9HqS6lG_Eo6szsjGShwzxG4MW0LonxFFUtZItnSTFqn4xV-70F-ZQ-Bwy4C7JfK48KeEh5HETaFcP3Q2FAuODQDIzkDjWhhschwRcLC6zzaKNAVcUgG2CUezlp7mUWIic6kewIMCQmHLFdVFrUmA3xqacuwZ37LUDbiqX2ts43vBR_7fQIKHMetzL5nS7-QC0zH4GzEb00iij-la57tXXLIcmFl0dHIdvyg6LlmsLH2744FUunl5d5FWP2wrdzNU_Vs-wVUbhttF2qOZmKypBi2E6j26Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ صدور کیفرخواست برای ۲۳ پروندۀ تراستی با ارزش ۲.۵ میلیارد یورو
🔹
رئیس‌ دادگستری استان تهران: از مجموع ۶۶ فقره پروندۀ ارزی و تراستی که در دست رسیدگی قرار دارد، ۲۳ پرونده  پس از صدور کیفرخواست جهت رسیدگی به دادگاه ارسال شده‌اند که جلسات دادگاه این پرونده‌ها…</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/466573" target="_blank">📅 11:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466572">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تیم نیروهای ویژۀ نیروی زمینی سپاه برای شرکت در رزمایش ضدتروریستی شانگهای وارد بلاروس شد
🔹
روابط‌عمومی نیروی زمینی سپاه: تیم نیروی زمینی سپاه پاسداران، به نمایندگی از نیروهای مسلح کشورمان، برای شرکت در رزمایش مشترک ضدتروریستی کشورهای عضو سازمان همکاری شانگهای، واردکشور بلاروس شد.
🔹
در شرایطی که دشمنان و کشورهای غربی و اروپایی در تلاش برای کاهش ارتباط ایران با کشورهای منطقه هستند، حضور در این رزمایش در ادامۀ تعاملات راهبردی کشورمان با اعضای سازمان همکاری شانگهای انجام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/466572" target="_blank">📅 11:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466571">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2ki1MbISbxdb5LwfDK2ydBeJyBbHJeu8QRv7UsBbjqvyfo3oUPS-yjSCk5vuk0zRmdWuArOT3f6P4WZVhLzNNGD2GskdBcrCwVH07eOxcIQDXQh5G8cC_-rqmMKzQpCyEssAaw7AbIjC8exyj_frmr9QbRezI8VAtqHgpJcHNowK4Y7qPDrrLR-TatNPcWRdg__qL7uIxsIUytkzCHuQWxGjrkb6ue1q3OF5uPOP0Lp0Ibd62Vmnvj0D8qUAk255UjGaUw8ZBO27XfuRwL-KWu6HEXMPooTxRQTaLT-M9Jkn40ZICl51FIwlO_c7xLklh-tW6flmsQNC4L5syenTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان نظام پزشکی: آمریکا پس‌از شکست در عرصۀ میدان نظامی، امکانات پزشکی را به ابزار جنایت جنگی علیه مردم ایران تبدیل کرده
🔹
دولت کودک‌کش آمریکا برخلاف همۀ قوانین بین‌المللی و پس‌از شکست فاحش در عرصۀ میدان نظامی، همۀ امکانات پزشکی و نجات بیماران و حتی…</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/466571" target="_blank">📅 11:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466570">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ew_tAhUgCQ1Wrthzmlnk3RHEK62lWMv_Xja1I1gv4q1wngStbjwyDmunWk6-w-0J35jQ0LRTMIdHE38_OsM0C6S5NN0xxh2VIwEOnc9HaeH4iXxrSKrLVyTdV6DwRY7woS8F9YiMpzDPPhC8NIasjmiaQ6LdUJSuQp1Y3T_2kkOUGeqOwOgx_Or8vYTNC0drjF1k2jhBR1HobKx_Vt3Bj2TWA41crN72Nzp5vxzSL4SaBy7_jfm2LJ18iCNOmUvBBhcE6RK64eoRonPRC3N1vIYqoS0MnFlV6A4XmKPyacMMZ7uqotD7e_bTLrvEMx2hjzQ0WYYGecJxNZHN-sYPkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان نظام پزشکی: آمریکا پس‌از شکست در عرصۀ میدان نظامی، امکانات پزشکی را به ابزار جنایت جنگی علیه مردم ایران تبدیل کرده
🔹
دولت کودک‌کش آمریکا برخلاف همۀ قوانین بین‌المللی و پس‌از شکست فاحش در عرصۀ میدان نظامی، همۀ امکانات پزشکی و نجات بیماران و حتی داروهای بیماران خاص و دیالیزی، ازجمله در اقدام ضدبشری حمله به کشتی توسکا، را به ابزار جنایت جنگی علیه مردم و ملت ما تبدیل کرده است.
🔹
پزشکان دنیا و نهادهای بین‌المللی نباید اجازه دهند جان انسان‌های بی‌گناه به ابزار جنگی دولت‌ها و رژیم‌های شکست‌خورده در میدان جنگ تبدیل شود.
🔹
صد البته که کشور ما و ملت ما و دانشمندان پرآوازۀ این دیار کهن، حتماً این رژیم‌های ضدبشری و نهادهای منفعل بین‌المللی را روزی پاسخ‌گوی این خاموشی و مدهوشی و سکوت بیشرمانۀ خود خواهند کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/466570" target="_blank">📅 10:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466569">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8874806088.mp4?token=ulsOYti6i7C7IA8BMjPmWxfN-AfdfcwMSIVnahXHt7bGGRETUFLa4ApMmhA6XpgyjFTINbyBcB03QjaVhdwMPi94HwTkd_0C3fOYy5aN0BXuPLrLzkOxAxM17pblJ3EutM4njdcA6WeZS_muDO_tHhOmR7dGqb1xBe4cjDVxOsJcFTTy8VBJHx37uroWfoZfenHUr7SLU3pGVocrzJYntobowIoYNMpZl8tD5jHTN1dBdXZzSrtHuTlo4IWeFaAEq_BpPhlbXg-5taUkG2iIF5oqrgv94u1TGgc-nhJzZ9PW3K3Xj-YX50BCALtDHMbCsFH6LIiRJQ4DQzZ0ud4Gww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8874806088.mp4?token=ulsOYti6i7C7IA8BMjPmWxfN-AfdfcwMSIVnahXHt7bGGRETUFLa4ApMmhA6XpgyjFTINbyBcB03QjaVhdwMPi94HwTkd_0C3fOYy5aN0BXuPLrLzkOxAxM17pblJ3EutM4njdcA6WeZS_muDO_tHhOmR7dGqb1xBe4cjDVxOsJcFTTy8VBJHx37uroWfoZfenHUr7SLU3pGVocrzJYntobowIoYNMpZl8tD5jHTN1dBdXZzSrtHuTlo4IWeFaAEq_BpPhlbXg-5taUkG2iIF5oqrgv94u1TGgc-nhJzZ9PW3K3Xj-YX50BCALtDHMbCsFH6LIiRJQ4DQzZ0ud4Gww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دانش‌آموزان جانباز مینابی ترس و دلهرهٔ هنگام وقوع این جنایت آمریکایی را روایت می‌کنند  @Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/466569" target="_blank">📅 10:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466568">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1940e45f30.mp4?token=q5Vjy0P-epRYYHO2xSoET1GLqucj0qE49KHuP--XT6MPQ5wBJjEQbvgMfGATGlUdhSJjfL6x06l1x-pfAxmAAE0z0FDxDYWwd6jJbFpExv9bHhuJDKlFgy2C0bwzN7lSVtOfxW0ipa418kuC9o964zHc7a8c4FOdxDc2omQ7WJVuQr1SGaUaCtdUXeni6zpQuf0JbGEtO0U949DmGKktlPuXR_QAewEAuBh9WPF-uG1_8iTw8KuLl1o2omgtu1C3BtQSJlQg8EtUCtxXQsgiStfCTJfxz8ThQeN-omXG_Q_IToix_dMldQ0v_OzTfJeBizxJX6_3YF80iebdUO4WWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1940e45f30.mp4?token=q5Vjy0P-epRYYHO2xSoET1GLqucj0qE49KHuP--XT6MPQ5wBJjEQbvgMfGATGlUdhSJjfL6x06l1x-pfAxmAAE0z0FDxDYWwd6jJbFpExv9bHhuJDKlFgy2C0bwzN7lSVtOfxW0ipa418kuC9o964zHc7a8c4FOdxDc2omQ7WJVuQr1SGaUaCtdUXeni6zpQuf0JbGEtO0U949DmGKktlPuXR_QAewEAuBh9WPF-uG1_8iTw8KuLl1o2omgtu1C3BtQSJlQg8EtUCtxXQsgiStfCTJfxz8ThQeN-omXG_Q_IToix_dMldQ0v_OzTfJeBizxJX6_3YF80iebdUO4WWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیزر قسمت جدید مستند «پشت جبهه»
‌
🔹
در این قسمت از سری مستندهای
#پشت_جبهه
سراغ نیروهای آبی‌پوش اورژانس رفتیم.
‌
🔹
قسمت «گروه آبی‌پوش‌های جنگ» را امروز در
خبرگزاری فارس
ببینید.
@Farsna</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/466568" target="_blank">📅 10:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466567">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bb8b3276b.mp4?token=I7ERTzmPPf7_0UAFRCzBuTDKZJ-zaox9th55d1YZkHHgHAF4WGir9aifKexe7k4DBbaPRNcufewBzf_Cm1H41NSA09WAFfwcgIQFW-VCVtjXjuRHekY1OHiRf97Sl3_USj2r084ZDX4rwkRFWupZPbGZgAFlrfarVHBjdtSTcxS2A3vUwVYL-8F4rzN8OXB1iHUlTAT__-f8HnZM9rTYd_IpjzjMRKrPdsOYu0ZLFEHemFB5ss_jul4BanDiz6NuUOuusqk5Nx33vRYSmJYTv4ogfOqStEGfrVmynJTsaI31MyxG649novJPHfXwz30rEjEwzROdp9xSivMJ9Jdl3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bb8b3276b.mp4?token=I7ERTzmPPf7_0UAFRCzBuTDKZJ-zaox9th55d1YZkHHgHAF4WGir9aifKexe7k4DBbaPRNcufewBzf_Cm1H41NSA09WAFfwcgIQFW-VCVtjXjuRHekY1OHiRf97Sl3_USj2r084ZDX4rwkRFWupZPbGZgAFlrfarVHBjdtSTcxS2A3vUwVYL-8F4rzN8OXB1iHUlTAT__-f8HnZM9rTYd_IpjzjMRKrPdsOYu0ZLFEHemFB5ss_jul4BanDiz6NuUOuusqk5Nx33vRYSmJYTv4ogfOqStEGfrVmynJTsaI31MyxG649novJPHfXwz30rEjEwzROdp9xSivMJ9Jdl3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ارتش از امسال دانشجو را از طریق کنکور سراسری جذب می‌کند
🔹
معاون نیرو انسانی ارتش: امسال دانشگاه‌های افسری ارتش پس‌از سال‌ها اقدام به جذب دانشجو از طریق کنکور سراسری کرده است.
🔹
بازگشت به کنکور سراسری برای جذب دانشجویان در دانشگاه‌های افسری ارتش بعد از ۲۰ سال این پیام راهبردی را می‌تواند برای جوانان عزیز و خانواده‌های آن‌ها داشته باشد که ارتش می‌خواهد دامنۀ دسترسی علمی کشور را افزایش دهد.
🔹
دنبال این هستیم که دوباره دانشگاه‌های افسری را با منظومۀ آموزش عالی کشور پیوند دهیم.
🔹
جنگ‌های اخیر به ما یاد داد که جنگ فقط به محیط‌های نظامی محدود نیست. مرز بین محیط‌های نظامی و غیرنظامی کاملاً ازبین‌رفته و این پیکرۀ واحد را در دفاع باید نهادینه‌سازی کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/466567" target="_blank">📅 10:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466566">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cc8j5UUbuzsZrMC0nVKH2G03ELCC137yMd2HWDf_km3FfiE-JpjXl64QrztHJUvmL3PKyxRQcwVlAMwdG4qked7Aiy0e0grFFP95_DA7bmfZ13IfxRzN0ZKt4scU_lwWiFsqDTyOB2n92Ia-qRSa64YPpk0vLsk4FGkqb_ZUqR9nHPuLMi3uwaeuowLRNC1BAfozRd67IMhEr8arAW_737rdfCpEE9j3o0FaYIH8DoqRD6Q09GCzSmktdKMV67JSDBTUOHTh7oS0o_dXzLv-3Oj7vqsOt9zQy-a_foJISebk7I9VOZhBZ_SI7xEMJiqSzv8yckWnzVsrCo-fSSZvqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وام یک میلیارد دلاری روسیه به ایران آمادۀ واریز شد
🔹
فرایند پرداخت وام یک میلیارد دلاری روسیه به ایران نهایی شده و منتظر اعلام شماره حساب از سوی ایران برای انتقال وجه است.
🔸
خرداد امسال بود که وام یک میلیارد دلاری خبری شد و گفته شد این وام قسط اول وام ۲۰ میلیارد دلاری است که در دیدار شهید لاریجانی و پوتین تفاهم شد و روسیه در میانۀ جنگ آمادۀ پرداخت آن به ایران بود.
🔹
با وجود این همچنان دربارۀ سرفصل هزینه‌کرد این منابع تصمیم‌گیری نشده و همین اختلاف دربارۀ نحوۀ هزینه‌کرد و تعیین محل مصرف وام باعث شده دولت تاکنون برای اعلام شماره حساب اقدام نکند.
🔹
سازمان برنامه‌وبودجه به‌دنبال استفاده از این منابع برای واردات خودرو و دریافت عوارض ورودی است درحالی‌که وزارت نفت خواستار استفاده از آن برای خرید تجهیزات نفتی و وزارت کشاورزی به دنبال اختصاص این منابع به واردات کالاهای اساسی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/466566" target="_blank">📅 10:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466565">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Se4kgt1LsCENGKEQ5MXZHUfxSSlABuyLIfnef1Tl4xS4eew-a2Z6eg3YzVu83aRoLe-XmVDpVdH4LJQb52B7AeRUe2MZJ1ZLHMlBv6hU-GOmcxbOlG3vUiEa0t4RYGdVXOAUNmQAsafA__Eldj9kJVe-4sa8RoLLVvY3Buf7HIg4MsJ8K5yOTwuRYwTs-ImSGgbF_HQTtDp9wkyNZKZvWhJbIE0fKNJ6eAaXHL64lIZOF98qM2Oj-mjSqsr7MlZKYCmE3KJKVxMsDvByQzqXBn9cfKVWHY-iQb45-BHTIq19Ft3HlE037JFe5_3Gfg002nHA8McXQ_NHAuc29r9Egw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاضران در رژۀ منسوب به منافقین در کرج به دادگاه رفتند
🔹
در پنجاه‌وششمین جلسۀ دادگاه رسیدگی به اتهامات ۱۰۴ نفر از اعضا و سرکردگان منافقین برخی از افرادی که در نمایش دورغین منافقین در کرج حضور داشتند، برای طرح شکایت از این گروهک در دادگاه حاضر شدند.
🔸
ماجرای این نمایش به شهریورماه امسال برمی‌گردد؛ زمانی‌که انتشار تصاویری از یک رژۀ موتوری و خودرویی در کرج خبرساز شد و ۱۵ نفر در ارتباط با این پرونده بازداشت شدند.
🔹
این افراد گفته بودند برای تهیۀ فیلم جشن تولد و در ازای دریافت دستمزد در این برنامه شرکت کرده و از ارتباط سفارش‌دهنده با منافقین اطلاعی نداشته‌اند.
🔹
همچنین اعلام شده بود که فیلم اصلی پس از ضبط، با ادیت و الحاق تصاویر و پرچم‌های مرتبط با منافقین تغییر کرده و نسخه‌ای متفاوت از مراسم منتشر شده؛ موضوعی که اکنون در جریان رسیدگی به پروندۀ منافقین در دادگاه قرار گرفته.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/466565" target="_blank">📅 10:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466564">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f416b2a7bc.mp4?token=ZsIhMqkk-D69g6Lakx5mdl-4X0p5ujwSLsoWy7Sow21X6bZ5ttoDgmuwAjKREX0ziJeBnNBLlAZQ6vIifnBUXeT-DiWizVCHxqorVh32V7kXTkfK7hthNRnEoCxjvZXhkzlf1F_ZxSN4--5jpa4jktLvwPwBoy_cfy7WDxd6duXtDFHSng75hl5RP57SFX8suCnvhji5Esp493Zc7Yg3qFpsgqGd8C6nwDZ5Pe-mf5rz_SAGEDhpYy0MpxB1GSJjcDUIV1jx5TvGaWgCy3J79X1u7mjBILW7yrpBkieFeJ4Tt4AlagQ1WxXu1AKpy7J3tcHZD7iQ6mqYfZ7_oVeTLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f416b2a7bc.mp4?token=ZsIhMqkk-D69g6Lakx5mdl-4X0p5ujwSLsoWy7Sow21X6bZ5ttoDgmuwAjKREX0ziJeBnNBLlAZQ6vIifnBUXeT-DiWizVCHxqorVh32V7kXTkfK7hthNRnEoCxjvZXhkzlf1F_ZxSN4--5jpa4jktLvwPwBoy_cfy7WDxd6duXtDFHSng75hl5RP57SFX8suCnvhji5Esp493Zc7Yg3qFpsgqGd8C6nwDZ5Pe-mf5rz_SAGEDhpYy0MpxB1GSJjcDUIV1jx5TvGaWgCy3J79X1u7mjBILW7yrpBkieFeJ4Tt4AlagQ1WxXu1AKpy7J3tcHZD7iQ6mqYfZ7_oVeTLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی در تأسیسات آرامکو در جده در پی حملۀ نیروهای مسلح یمن
@Farsna</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/466564" target="_blank">📅 10:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466563">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‌ سرلشکر حاتمی: صنعت دفاعی کشور به معنای واقعی کلمه حامی و پشتیبان عرصۀ نبرد است
🔹
فرمانده‌کل ارتش در دیدار با وزیر پیشنهادی دفاع: در جریان جنگ تحمیلی ۱۲ روزه و جنگ رمضان باوجود تلاش دشمنان برای متوقف ساختن زنجیرۀ تولید تجهیزات و تسلیحات نظامی، مدیران و کارکنان…</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/466563" target="_blank">📅 10:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466562">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فرمانده‌کل ارتش: مهندس مهرداد اخلاقی چهره‌ای شناخته‌شده، مجاهد، مجرب و انقلابی در عرصۀ صنعت دفاعی است
🔹
سرلشکر حاتمی در دیدار با وزیر پیشنهادی دفاع: ارتش جمهوری اسلامی ایران، تلاش دارد هرچه بیشتر از ظرفیت‌های بالنده، پویا و مستعد صنعت دفاعی کشور برای قدرت‌افزایی…</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/466562" target="_blank">📅 09:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466561">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INnsItJsCPDcBt5qB26wsHuwd0bBdSrjzdMhHbUDHydNqgIdgjNaC950Z03WxQ_tDOCR-TyjFqDvsH1kx-F4CS7E3A49ZSwbiEsyvry87ICMTinkPDbta0cLjuu-Wy4fs05ZDEwgDakWKMnhqsgZ2o4t4T4Yry7d39lsF9bp7C720S6mWcpGSKPPuvzdj3sSueYYO3gISUjeSXitYppwCnfI1qCjeqVp5L12-Fv7HiV3NfaUsyIohZiOgdJjaBgU3txcgUi1ZuA06a7PA6lfOBVFieLzMFcVb0rhQ4o5kT49wySZJiFUZtTOrvxnyO_-DCfstNDLrEJ9aKtx8gXMIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامۀ معرفی وزیر پیشنهادی دفاع اعلام وصول شد
🔹
نیکزاد: نامۀ رئیس‌جمهور برای معرفی مهرداد اخلاقی به‌عنوان وزیر پیشنهادی دفاع اعلام وصول شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/466561" target="_blank">📅 09:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466560">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzfu-DI56v43dvfQ-NOcWYHxLZ2COD0HUvAZBbI5NLd2dgQDXMrnhcJPXz70FdNlrf-k68UJKR0vEL8g06SFNipDEcTZMIFWw_tz3Mk2u1GWiG9XreG4gDPiZpxHAZwFfEDktODPhB6G4iJgQKcgbYdKGVk7oAoUWcJ3x2cyeLuDH3Q6eFCOu5qXOz9jLpIURh5a2ek5yvsgrL-8M1v4Ae0h8Laf8f18P6TTLWljeBLZzJejJohZu6auQCiFdoKbzDBqozCNcz-b8JrOEbzoYds3UbwUrWy62tW9m6S3DkgoTOdp9iRDt_ecRRrrULjcqXhclsqRg54YwIQSaxBJUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
یک منبع در مجلس: مهرداد اخلاقی برای تصدی وزارت دفاع به مجلس معرفی شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/466560" target="_blank">📅 09:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466559">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B97DqTYHpEqxEyQWs4zd0lZWLeC89JEIa4pwWGY179V8Pyhb32sSuhGso3selIWUXaPNJNBQALqYcrrIFIStQptg4Aag4I4rGYTGLBSPeSK0Ti9a42NN9q0JwtLBSjGoVhTignwXX7S0zOZowJtEcgYjFRKl5jjTXgfsbwVMdZh41yuHSAekApDFiUR6l3HC6x62_Yp9rUFFe87459WE-Up_DkWBrQDlmjk9I3wtZVJIbjHpFS1Uy6qOIr-RrIvwqWxHIBSyBkMo1mTzPHMpEk0INUPX5L0IJUMvAALKsjdPcbuO_5L32i-pTA_gxWh08s8KALrQWO7Ucpc0afuAzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجارت مافیای لاغری باچربی شکم ایرانی‌ها
🔹
تب آمپول‌های لاغری، بازار بزرگی برای کاهش وزن ساخته است؛ بازاری که منتقدان از شکل‌گیری منافع تجاری و مافیای لاغری در سایه تبلیغات گسترده و سکوت درباره عوارض آن سخن می‌گویند.
🔹
چاقی فقط به اضافه‌وزن و تغییر ظاهر محدود نمی‌شود؛ می‌تواند خواب، فعالیت اجتماعی، باروری و حتی سلامت قلب و متابولیسم را تحت تأثیر قرار دهد.
🔹
به‌همین دلیل، درمان آن هم صرفاً به رژیم و ورزش محدود نیست و روش‌هایی مثل داروها و آمپول‌های لاغری و جراحی چاقی مورد توجه قرار گرفته‌اند.
🔹
حامد قلی‌زاده، متخصص جراحی چاقی و بیماری‌های متابولیک، معتقد است انتخاب روش درمان باید متناسب با شرایط هر فرد و بر اساس نظر پزشک انجام شود.
🔹
به گفتهٔ او، مصرف خودسرانهٔ داروهای لاغری می‌تواند خطرناک باشد و این داروها نیز مانند جراحی، بدون عارضه نیستند.
🔹
از سوی دیگر، جراحی چاقی هم تضمین نمی‌کند که وزن فرد هیچ‌گاه بازنگردد و موفقیت درمان به انتخاب درست بیمار و رعایت اصول پس از درمان وابسته است.
🖼
اما کدام روش برای کاهش وزن مؤثرتر و ایمن‌تر است؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/466559" target="_blank">📅 08:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466558">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc1315d689.mp4?token=rTNQrwACmB43vpx35fF0bdsxgg9ekIvzl98nfv9ZRw7Ete9aYfSLkSSNB5GJ3_WsPzukAEBPt5pvMrZdk5p6rSx0oYqltQO6kJP_S9tXSAUrZY-UDe_mhzkgFJ6-04TP5DacVUpPg8J_kjV7DduRuvuE872O9HnCqLs3GAYFZe_Wln-2Ztf0CiQp3ifNyYk9MVFTe5l5DxqfdHhXzlNL9AwF7WIViH4ZXKS-v6rzYJ42xLebuFydSmtzQVpbbJ-kzS0k4kZEHXqtVmoVJ_814VEmpw3Z_UUOOHHzV2AM2JLv0zL6995uA0rimy-5ZJ5QYm2EUT0jEyZ9S8ueQubdhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc1315d689.mp4?token=rTNQrwACmB43vpx35fF0bdsxgg9ekIvzl98nfv9ZRw7Ete9aYfSLkSSNB5GJ3_WsPzukAEBPt5pvMrZdk5p6rSx0oYqltQO6kJP_S9tXSAUrZY-UDe_mhzkgFJ6-04TP5DacVUpPg8J_kjV7DduRuvuE872O9HnCqLs3GAYFZe_Wln-2Ztf0CiQp3ifNyYk9MVFTe5l5DxqfdHhXzlNL9AwF7WIViH4ZXKS-v6rzYJ42xLebuFydSmtzQVpbbJ-kzS0k4kZEHXqtVmoVJ_814VEmpw3Z_UUOOHHzV2AM2JLv0zL6995uA0rimy-5ZJ5QYm2EUT0jEyZ9S8ueQubdhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: سامانۀ بارش‌زایی صبح امروز از غرب وارد کشور شد
.
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/466558" target="_blank">📅 08:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466557">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار لرستان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/253b2d9da1.mp4?token=LN8vsiWGqyhwkl9S-hIhxa9g2mlsyMHoiZ9JX-QkiELr3l_aNBfTSgd4wFxytYl9tra1OlsLutjWlUUVyLSaXbx1oBx979Sz6YvlsIyZhtpLddtSFBE9RLQ0c9uBHqlBf8SIy5u0A4WgSsESxL3bj7nbs6jKamENyjERH4FBeD13vxTZ7nH23rPejLnMDgwO0j9G8ZjeS3A5fbW6J8rhoHu0zvkf7XaozhjXFyZW_KRteLy1WImrEvE7tGbTBr_2kug1aFqQhROsXZgBQAlFq8efdJ52rgIIm1ZN_H3cRik35_e4pkq2gjv7LXHoBIRoGEzobF5QkVVyYUiMcmXAkFPsPS7aiWCnvpCkQhOA1KIRAX9dyVP800PnhxdTBf73grbM6mFlx0K6fEEgEF1riHGkqcwhbMeFOI8g6KIVvxbVnHzshXW6btIhFxu4GRnIYHw9t953D5vwTWhKniwi33RdonRQybFAN3-o-3GunvobzDo80YJ9KonqXP2Pp8dzHGCbKtHj9LyGX-zsUDEVOyCf15ZVzn461iQW3wKnzhxpYKei_yhcA4U0rIkuPHTxU8L41B3EdwVXT6QQF73MfvddOyHqzPQ3Y5kdeG8Oe16XsQxuzrSMl6DCXQUohvDv-oBm4D0k16okcSyBnWnU9NE4WFQFQJkQ0ZJOpq67SE0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/253b2d9da1.mp4?token=LN8vsiWGqyhwkl9S-hIhxa9g2mlsyMHoiZ9JX-QkiELr3l_aNBfTSgd4wFxytYl9tra1OlsLutjWlUUVyLSaXbx1oBx979Sz6YvlsIyZhtpLddtSFBE9RLQ0c9uBHqlBf8SIy5u0A4WgSsESxL3bj7nbs6jKamENyjERH4FBeD13vxTZ7nH23rPejLnMDgwO0j9G8ZjeS3A5fbW6J8rhoHu0zvkf7XaozhjXFyZW_KRteLy1WImrEvE7tGbTBr_2kug1aFqQhROsXZgBQAlFq8efdJ52rgIIm1ZN_H3cRik35_e4pkq2gjv7LXHoBIRoGEzobF5QkVVyYUiMcmXAkFPsPS7aiWCnvpCkQhOA1KIRAX9dyVP800PnhxdTBf73grbM6mFlx0K6fEEgEF1riHGkqcwhbMeFOI8g6KIVvxbVnHzshXW6btIhFxu4GRnIYHw9t953D5vwTWhKniwi33RdonRQybFAN3-o-3GunvobzDo80YJ9KonqXP2Pp8dzHGCbKtHj9LyGX-zsUDEVOyCf15ZVzn461iQW3wKnzhxpYKei_yhcA4U0rIkuPHTxU8L41B3EdwVXT6QQF73MfvddOyHqzPQ3Y5kdeG8Oe16XsQxuzrSMl6DCXQUohvDv-oBm4D0k16okcSyBnWnU9NE4WFQFQJkQ0ZJOpq67SE0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی از پاییز طلایی دریاچه جهانی «گهر»
@LorestanFars
-
Link</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/466557" target="_blank">📅 08:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466556">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLtCcAPh9z0TR1p8auHcQildd5IfhN9j8GgiM1p2a7ikdTBGjseCJ6fzicNhnIsHXb9c8CHDkp_mdvjkt-R-03HBoTjLBjLQ3mf6B-Hcs-jW8SLFPFaWmVEu-c9gerRlJh4gaYGC45yer0LNyG0lonBsrZUGsVHz6ydvnzCt2F9QlyzTbGl5-g8gJ23QbjZFHzeGtlFpsDVYW-SnWSsKX-NXYtk2MnplmPjSVR090nxtxcgnIYojQI7LBEpjspZ4AatWCAWYjZbQw0sSQmJmvMv_dW4HnHf15gIr8HeSWz0tllCHTco3bWUx0aVYm1T15umYVOeNP6ylj6iwH1rUGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش: ذخیرهٔ بزرگی از تجهیزات جدید در اختیار ارتش است
🔹
امیر سرتیپ اکرمی‌نیا: تجهیزات جدید پدافندی و آفندی از جمله موشک و پهپاد، در طول جنگ تحمیلی رمضان به‌صورت روزانه تولید می‌شد و امروز نیز تولید آن‌ها ادامه دارد.
🔹
اکنون ذخیرهٔ بزرگی از این تجهیزات…</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/466556" target="_blank">📅 08:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466555">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4783e8a603.mp4?token=myiGDiuL3J56ZIKoCuUg3PqLHxL3_mlOZsjIqX0BJJZXOJ_S0eyX_jmosBzmhAETIr2ROFJblDrvweO1EDvGqIyHSw6E2sW66Up3TX7dV25aOZZAaKP0jyMMXTmEuh2CRk8s_QnFsSuq_f-C96OGP5dKS5cis1tpJorD3yy4tjqhQ3IKzbBJs9wdMCXDermpJUDOqbKqcfXF628Fbmnaphc6LObF3RBBZ4lTt-ydWZG1PReVSx0jWgsKKevYJyvqncIEXt6rwfNHVQVggAafMXDU7gx6fMzSYbWHPNKV9ub4nISDvJtM-FOCOJ7y3yPMEjCCJ6ai-SHwFnb7i_R6Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4783e8a603.mp4?token=myiGDiuL3J56ZIKoCuUg3PqLHxL3_mlOZsjIqX0BJJZXOJ_S0eyX_jmosBzmhAETIr2ROFJblDrvweO1EDvGqIyHSw6E2sW66Up3TX7dV25aOZZAaKP0jyMMXTmEuh2CRk8s_QnFsSuq_f-C96OGP5dKS5cis1tpJorD3yy4tjqhQ3IKzbBJs9wdMCXDermpJUDOqbKqcfXF628Fbmnaphc6LObF3RBBZ4lTt-ydWZG1PReVSx0jWgsKKevYJyvqncIEXt6rwfNHVQVggAafMXDU7gx6fMzSYbWHPNKV9ub4nISDvJtM-FOCOJ7y3yPMEjCCJ6ai-SHwFnb7i_R6Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش: ذخیرهٔ بزرگی از تجهیزات جدید در اختیار ارتش است
🔹
امیر سرتیپ اکرمی‌نیا: تجهیزات جدید پدافندی و آفندی از جمله موشک و پهپاد، در طول جنگ تحمیلی رمضان به‌صورت روزانه تولید می‌شد و امروز نیز تولید آن‌ها ادامه دارد.
🔹
اکنون ذخیرهٔ بزرگی از این تجهیزات در اختیار نیروهای ارتش جمهوری اسلامی ایران قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/466555" target="_blank">📅 08:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466554">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">هوای «قابل‌قبول» تهران
🔹
شاخص امروز کیفیت هوای پایتخت روی عدد ۷۶، و در وضعیت قابل‌قبول قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/466554" target="_blank">📅 07:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466553">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb98f0b2d.mp4?token=rO3LT9zjblnZgfJ3Kp6Jdu3iHcvjxfUpl0NyIR3HQHCN604t23N1uxOC3h64i7iJTw2l3BDSuO-iho3_70AMajCNq7IVqSdfWpTHS9mZwmVa2XZTc2sd7zTGjAqgZnYHQn_QLDqX5hSCIobBceUiiyreQaZrHdNpqe6izCiCBtvgTWrV1u7Z9KUh-gpJKEFtQggNcYQ6ecwtnBhr8tKI8N65DN0EmgXsv31JBD5zXXS1psIh40lhugvvi3tkTUWcHnVvPX9cl47XwMjAO4d17yKeh3hi5qGZ0KBmd-PcsYwsiHDKt4Q2J4sf54L03UphfxUJwadK15HOMlsy-fRoZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb98f0b2d.mp4?token=rO3LT9zjblnZgfJ3Kp6Jdu3iHcvjxfUpl0NyIR3HQHCN604t23N1uxOC3h64i7iJTw2l3BDSuO-iho3_70AMajCNq7IVqSdfWpTHS9mZwmVa2XZTc2sd7zTGjAqgZnYHQn_QLDqX5hSCIobBceUiiyreQaZrHdNpqe6izCiCBtvgTWrV1u7Z9KUh-gpJKEFtQggNcYQ6ecwtnBhr8tKI8N65DN0EmgXsv31JBD5zXXS1psIh40lhugvvi3tkTUWcHnVvPX9cl47XwMjAO4d17yKeh3hi5qGZ0KBmd-PcsYwsiHDKt4Q2J4sf54L03UphfxUJwadK15HOMlsy-fRoZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ پهپادی اوکراین به قلب تأمین سوخت مسکو
🔹
پهپادهای تهاجمی اوکراین مرکز بزرگ ذخیره‌سازی و توزیع سوخت جت، دیزل و بنزین که پایتخت روسیه را تغذیه می‌کند هدف قرار دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/466553" target="_blank">📅 07:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466544">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSK3KzezsFXtu7Aon6ii3GpulAU82dL3Nab0uJbT5GKEvo_2WtN770xJDG4k1PqC4uLyPyjz6Dv0r3B9QW9b9ncUUbOOfq6lLBMjig5ex7SctKbZsb645r2nOPZv2w7rh1A_qwxqCUamULLTd8doWWQstW1gWIdmg2H0W8kivia7LjIes2u_OnZt7QXF2f-L9pQWGO1JWyigeIkplquSRv5A1JwU5GtvVGWnJqfuN3AXdHz7rMYHY4jF-T_WvCkC7lMFKuK5q4gfcpOKTTUh0jNlyqSCMIzWkOEOQq74MLXcqk3bYVQiWmFHIOFpucS9F-4xiI-_tsR7R8J92PdzYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SUd9FHLqkKrP9A270fyhW9TmKV55zRl0eR3N4uwRXYRkEHXgXHRkTLJovxIENsBUBsaixBfwLL9-qEAmCu9cepm_MGHy8OBQqndTdUkqHCgXaZAuovOFdUD3dxaxoiWZGj7fLknGDbkORrdiKkcu2iItKH9w9ESLPgyJnZs8O_pT7o7qgwtj1VxjXlQLPQopcc1L2663LE4rTlQiM7tU2UnIM8K7pexLzlYnDM-6YNbxaw7JEF1lL0zXhc7Wra5GNULlQOq0c6hvnrkxRFfG8raSOG4zDOjsko8XnDivtj30qMI30oMDCWIGGSXKUm0_vkItYdw0syd6Tg7RNV2mvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFacnF5OELGy31W1YXp1RuTwgkzvUEHBZAZ01jvg6bxWWpCLPs_2YK_eob_flJb4UM0T1Q0aQpZpcNHTO7fcQJ4zuq_DSWSc1t_2Jeoq-P7jY4GUF0Vn0awNR15R7H0RtepgD7syjaMWVwe-dXthJEhWTb8VvTNzdqMJZvJi28BAlWmo1iRBeIg1Jx6dDlHUWM--8xEJXp4vGgDHrBNPDcppXTxtszGJxWDfoHf4FztQ3KZoLbU6TyzNLAVC7vb-T0bycMrT5WHMZ2_0S-Ac9rUhFv4av-Y-TiehFhuzLm63noHHTRKawiAF-oN8YlUqWCCQPCzbHRL-GtASYW28qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QR7glJJfK-BIAWH9LURlkAeYQriTbblNIXZLxiJZSSkj9s2VzD1nGJ2vzchnyNSF72AjwTuEpQHFoHV8gTkz-cqRnUUiLVEnFqNDOlVt833WPzGzIv1A2dZWJsilafCBFG0HuN7rUu2ruIaJ4-7T21s6_LmH-nzuCp2dbVFFNzOUTuYwRSZEk9XOrUO9Es28Hcx2HTSw-vSb3fAGPFXXnwqRUBv7lxBnm8c8BYn_fzXy3FWL5sprSa1Crcp7fqhfrm-7iwhy7N_V3KkLA3ebmNQWCz-mr-aZM9G6cefd8DnDZIp2ciVw9UCYuLVPErh_AWGxuPXN6cQ0S1UHYSwEUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FatiwzdaM2xybPq8je5RdqV-k9zrmFIYOaF8Le_FtxUfHkgo3qR_yXKisGl-JEd3AZlTHAHufDNwI0Lv84YF6QM8ptpURMCoqPSBQDJ8el-y60l2iuKKnAbV5hT9zmO-tL8bfCZLrRMKJxg8BnrnnM6wgRdN09Kz0VZjAM2jTKXrbsZjZMHtGMUhwMJ_eaMH8p1Xc-P-FKaVKcKuWbrgxw9AfeMUrFfb5txjoCpBFnGBeV6m5SzdOyszhKdb4lI69AlK-ffxhHm6ly4F7JnVEWXiJnosLE0ADP39aLEcJfFmeVIuoJyrxy8XQAIx6TW0spUaE0Oz7DOJ8MmIQzkg2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JplfalJ0m6bGxhOGvgkvce1pwCpEs16OeUmjhv8gVhjsBSm9qWkaPhLpaRqKxBhu8qXxOR3200ZB9RMRrDWhF1bTGQfUqyIS1jRr158nUfPpxg5W7bodnA_FsQuSgFhDaf0weL4CI9WOtqvC69dVsuLW7AtWmgHpvAO3zD9AL3YrfNVX8hh8-9D-VGhDsW8StjQxf6El0LfSoBk6Ea4jx2SQrM4by5xgIO7kiX0C53zuCmA0wrgESWq94pNOo8EtpcRNGRbP6f_MCkhEpehTVLnP39B1gKjk6MJtu-N6mxeIaS8YICMMxMxnlPsnFTiMSmXMjVheoHCRA-5uEnDEQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BqGnxVje8BKrRbNo9k2Uz_54IFDe7MkH1jjGYBpgjLWPUQMBsNHGppNBfpSbep-EsWIbRzMUPQ0qTFBpYIBa3kqp35wFvZmjSaVCLrKKgmiXKE1A_CuvDRBxVBVGxxxg5zKiF5wVVrUAni7yqvohEzlT9dO3L4KH8UTbARYsiw-kgaimSIQ2q0c_91iL93cC-WtXZKBW97yTmMt0L8I6wZlE7up6vqYa9duDl_Z6KM9Zs8FDSl85Xi0Hvg3zFeX2iiLjkekZ3myQlOo7pOimZlIHclUF4mhLBq7r190XeQ7ssNxx-YZaVkQq249yZiRmWdZ2ZpTGGtxf0w1uQsaJ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QdHd2kFPIr0u8G8yz4xp2gpvYocTqmLxjTd2YhCqzXybRmMmxaiQdXgdeoRoN-FGLM4fNaRiYBwyzGXzSvUeUMImiBPBDRck-NdCqoPPwkeBVVz7Df-z6OKpwoYGIksOYXTM_FiCeipajpZWRpp1VJKWUcPPkykgyiORMwsa2ybGonvhGf0aLBt3rnTw057pC6V4g2txqAHPRMIOa9nTTNs0x80DYM8U3ODQNTshBxxUDBK5cZ5XtVmttrcd05xm4xxcKp6TnqDL0L67LeUSE9hcEZBmhAqXivhaRYxrmes8he1HYfTuJjhDHx466_drEEROKDHU4yXbL8TZJXzrlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ou3x_GrUkSs0vpLzrUgOEFFecgQq8Yld7Ne85nl4V0XBrcgMuqUXL1quDkFnNFFOUl3R89_tLifEc0apHO2f3fOv5VF-wL2MS7MoqfSC6HlWVin_vgmqRmbpzH3IAavKwT96ysmAaO9PffVnJLsfloFrQNxM3f-Sv5UAC90rKrifOl4YxEhcFxOvvZN-tW4SjYtziMynGAleA1wgzm1Ziy-MT4swHZfldrYAtPbdDUhJwDghbfe0ZTJkz1jVRdaArXec7dNlEI7q9fZpmFN3smtdfYD0yanB8aDheQL73g_iVyv2C4YUC0LDVzNPOuCbEP0NX8ouUxEbxzPy1DMmeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
باغ‌های خراسا‌ن‌شمالی پُر از بوی سیب شد
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/466544" target="_blank">📅 07:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466543">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">حملات هوایی عربستان سعودی به شمال یمن
🔹
منابع خبری گزارش دادند که شمال شهر «صعده» چند مرتبه هدف حملات هوایی تجاوزکارانهٔ سعودی‌ها قرار گرفته است.
🔹
همچنین توپخانهٔ رژیم سعودی روستای أم الضهی در شهرستان حرض را نیز گلوله‌باران کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/466543" target="_blank">📅 07:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466542">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‌چرا چک تضمین‌شده جایگزین چک رمزدار می‌شود؟
🔸
قابلیت استعلام، قبل از دریافت چک
🔹
اتصال بۀ سامانۀ صیاد و امنیت بالاتر دربرابر سواستفاده‌های مجرمانه
🔸
امکان نقدشوندگی در سراسر کشور، و بدون نیاز به مراجعه به شعبۀ همان استان
⚠️
از امروز صدور چک رمزدار ممنوع است،…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/466542" target="_blank">📅 07:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466541">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
مدارس و دانشگاه‌های مناطقی از کرمان تعطیل شد؛ آغاز فعالیت ادارات با یک‌ساعت تأخیر
🔹
به‌دلیل افزایش آلایندگی هوا، فعالیت مدارس، مراکز آموزشی و دانشگاه‌ها در بخش مرکزی شهر کرمان و بخش‌های چترود، ماهان، شهداد و راین امروز تعطیل است.
🔹
فعالیت ادارات، مؤسسات…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/466541" target="_blank">📅 06:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466540">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4626e38b60.mp4?token=YueSwhOFGLlK2nduwIFNnkas7zD_XH3NrVj3sWcKBcoA_32xTXUotIT-3tZTdqbqHJ13xGUm-CzUdPux8myrdHXbwri1BMXcnGdk6jUxsfC5Q0wnRpzld7xLaj4SyYRBXP-NwFUqtTf4_ygMQ7iNf7ul7lTq_UoXW5Fq1E4-Gm2FXepgNDlLwOgO95NeGGsLvp3gAnEqGKTWLGjGz_JMvwRAocvUxiVPmga87gCA-blavLVT1568R1-Bu0s0a0BH4h9hpEGt6Vr-_mZvvcJAgOIu40cU53SQum8V5SPFp_TDX9w8cIZ9SFdN5dPKd7TcDpX5d2_deWjHTOdAUdBGhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4626e38b60.mp4?token=YueSwhOFGLlK2nduwIFNnkas7zD_XH3NrVj3sWcKBcoA_32xTXUotIT-3tZTdqbqHJ13xGUm-CzUdPux8myrdHXbwri1BMXcnGdk6jUxsfC5Q0wnRpzld7xLaj4SyYRBXP-NwFUqtTf4_ygMQ7iNf7ul7lTq_UoXW5Fq1E4-Gm2FXepgNDlLwOgO95NeGGsLvp3gAnEqGKTWLGjGz_JMvwRAocvUxiVPmga87gCA-blavLVT1568R1-Bu0s0a0BH4h9hpEGt6Vr-_mZvvcJAgOIu40cU53SQum8V5SPFp_TDX9w8cIZ9SFdN5dPKd7TcDpX5d2_deWjHTOdAUdBGhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از آتش‌سوزی در فرودگاه بین‌المللی «ریاض» بعد از هدف قرار گرفتن توسط موشک بالستیک یمن
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/466540" target="_blank">📅 06:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466539">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgI40gAq40WPNOH6sz5znL2MQNiH5uU564QygyXDPl-1NLM4NAcYM7fza0hw576ixr7WVwINsY0bGG-7daawcsNxz7fQUfKSMqK_vc8ZfOt5i3P9R_cICRmCurMwik0HG71xlRPrO-Rs6eqgn4AsVZ5WhEy4iIIg1oZlASxzRjzBVp2uXMr6C9wMKAPkLwxITcMDCY7lvMaGpQHd0U7hUz25SlvSMT-uai46C_364bHpzeIzlSjGgIUlVTje75ddveGTHWX6vOJTlpKdposyb17-rEXY_7CKfQ9E_bKruA-TcycCQWRZL8wsDXBrCBQeOjW1NnVKNm34BjKU_3KqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌قیمت کالاهای اساسی «تورم صفر» اعلام شد  برنج:
🔸
برنج پاکستانی سوپر باسماتی: هر کیلو ۳۳۵ هزارتومان
🔹
برنج پاکستانی۳۸۶: هر کیلو ۲۲۰ هزارتومان
🔸
برنج هندی ۱۷۱۸: هر کیلو ۲۸۰ هزارتومان  گوشت:
🔹
گوشت منجمد گوساله یا گوسفند: هر کیلو ۱ میلیون و ۵۴۵ هزارتومان    روغن:…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/466539" target="_blank">📅 06:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466538">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/466538" target="_blank">📅 05:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466537">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJBsiRPq0ES-q-7OixPmvKnWl7CmKEWcusAnW1FZDBsxYx62co2sClpd3ANW3J8vvBbrnwIX6f5kyxzCrubUI3Guk375YgKyUfffYMMmyc80_lIqzxLxrIzbP-nCc7Hrabh0blGICcBP66FRt4NO-6RN6LFUfUNSRBpBCnvltsmE4OGysjZCducPxfydWVtDgWp9JMx-f5r63OS2pyHRj_f_Sn42y-9jrJg5eBomH7PuDUZk8Nb9t77JIIu6k2B9mLpd2igqR_RA7MODx_YxU0HuRcF7klyA8v4hhRuffnVKWu0WkQPIQlvaqVX6sjVTgYBI1FtoouQyBYjowcimQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمک نظامی ترکیه به اوکراین
🔹
وبگاه میدل‌ایست‌آی به نقل از منابع مطلع گزارش داد که شرکت ترکیه‌ای «آسلسان» چندین فروند سامانهٔ پدافند هوایی کوتاه‌برد «کورکوت» به اوکراین ارسال کرده است.
🔹
این سامانه شامل سه خودروی جنگی و یک خودروی مرکزی فرماندهی است و شرکت سازنده آن ادعا می‌کند این سیستم در برابر پهپادهای انتحاری مؤثر است.
🔹
این منابع که نامشان فاش نشد می‌گویند ترکیه در سال جاری چند فروند از این سامانه‌ها را به اوکراین تحویل داده اما تعداد دقیق آن‌ها را مشخص نکرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/466537" target="_blank">📅 05:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466536">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_rWCTu5gVXvoWgymUceKEavzM7I-L98wKAKUuzX2CNaHDWck6E2WuSSI_w9XCkBAKzE53PUcHbNt08QQSBTsBgu87EzOAr-wbay0vTbpQDny8ej1zqd-6jCg7nEsiUw18wLjYJOqdZSBPQ5CDbSGALpSSlY9xlL0C_Cse92GrNV09XS_uRP8JGJ9OQQJhs7PTW0NoZJLQiaZ5CpMzVFjCGy2m6e_cLT44lGeGT5ncoMRh6UHgOrgl3O4iNnY1txpCoA8PcuLOOLAdO7A_XLbgmeEqRIJ5OvvMPf7cqWgTT8cbBQQIVSKuIZ6c9EXWUGITV3SkMehb8G_VT1EFAvsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: عملیات زمینی برای سعودی‌ها خودکشی است
🔹
سرتیپ «عابد الثور» مشاور وزارت دفاع یمن هشدار داد هرگونه عملیات زمینی برای عربستان سعودی، خودکشی خواهد بود.
🔹
وی با بیان اینکه کنترل تعز به معنای سقوط آخرین برگ برندهٔ مزدوران است، گفت: حالا عملیات خارج از خاک یمن به سمت عربستان سعودی به واقعیت تبدیل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/466536" target="_blank">📅 04:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466535">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a7a8bf03a.mp4?token=iP4BH4rPIT5n6awv3YUp1_dAem8X3GFBOsW2EVUUsOiRRM5Lo-fjdkzu49-eqWDQqXCy8LXDknBgCMHpV_SgMiod7v27HlqKNhfZyq_Xdxdo5DtRgzTuDenRoplj-KPbq5mJnBsn8ZZWrNxasTkNxRBntwMWE828JElkg6pIvgSj3zYb_n68xsTLZHK9Z0yolGHZMXPMPHbU5OlVf5NUzNlsZhTopURMzCvi0TVA0mCQqNCWnia3IDamAjaDKZSw8IBtq0WM5_JiCFpCPloVssQ0114e7RD3DS0kgXw3lQb5wAGPJb43blZ1jvw7jXMLBpZoQ3XYrLUXQPLWZrsBw3bdRCwavgEXgveIv7n3ixtwg5czfARLIaxNwu-8CfFAGaEXm1zV7WmvK_TTdzku0rVuNocUKuMtCBGwVgfCYnwM2Iw9d2R9l-ZrHsf7OvcE3TOo4qvu1rNyUzQEb_X1pALNsImpWEU-TwwlQpNvUmh54gIpZwwGtVNLU4IcnYfDCKg_80Bz1puj5twA9Ggatw22rZZJker1Pm_MJoV11mB_MajXZ8KSGpGE1mJATOOjMebdREoKeHfl9qVLGbtxhvlTSnWbfBZ9yFQyJaYzglOV0_9iBuDJIF-J3A0VVBELwRhe_AcutmpbQJkhS1iR6CCGHGtCIDs8ltwg9t24L3Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a7a8bf03a.mp4?token=iP4BH4rPIT5n6awv3YUp1_dAem8X3GFBOsW2EVUUsOiRRM5Lo-fjdkzu49-eqWDQqXCy8LXDknBgCMHpV_SgMiod7v27HlqKNhfZyq_Xdxdo5DtRgzTuDenRoplj-KPbq5mJnBsn8ZZWrNxasTkNxRBntwMWE828JElkg6pIvgSj3zYb_n68xsTLZHK9Z0yolGHZMXPMPHbU5OlVf5NUzNlsZhTopURMzCvi0TVA0mCQqNCWnia3IDamAjaDKZSw8IBtq0WM5_JiCFpCPloVssQ0114e7RD3DS0kgXw3lQb5wAGPJb43blZ1jvw7jXMLBpZoQ3XYrLUXQPLWZrsBw3bdRCwavgEXgveIv7n3ixtwg5czfARLIaxNwu-8CfFAGaEXm1zV7WmvK_TTdzku0rVuNocUKuMtCBGwVgfCYnwM2Iw9d2R9l-ZrHsf7OvcE3TOo4qvu1rNyUzQEb_X1pALNsImpWEU-TwwlQpNvUmh54gIpZwwGtVNLU4IcnYfDCKg_80Bz1puj5twA9Ggatw22rZZJker1Pm_MJoV11mB_MajXZ8KSGpGE1mJATOOjMebdREoKeHfl9qVLGbtxhvlTSnWbfBZ9yFQyJaYzglOV0_9iBuDJIF-J3A0VVBELwRhe_AcutmpbQJkhS1iR6CCGHGtCIDs8ltwg9t24L3Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودت را با دشمنت بسنج
🎙
حجت‌الاسلام نوروزی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/466535" target="_blank">📅 03:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466534">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIl-JaM6ab76hemy8kHrAF_gBGxY7xpap22nSYGPETztLDG_M-h4eZ2N2hEwfUOBVhB6MEoKghTkB_khsaEHxgNO70CnOsPRuzy_-W51oUWMtXjAuIzr8eT-bu5kKwQB2Eaj3j3SpM7_DuWtfoWCVyzL820uMUu3Dt18fkh35_aoIY7qUURhNH7cOVx2Rm0w1f2btyP8ZGcyWJsDEF-XFbVas-sdWg1YCPzLGSCjzql5FR6rw2wUMTriiGHqKMS2d4oLFhc5iqK5zkk5C0wkeXm8QMH59RgPczeI_dZu7rw1GLqKn0vhbertItRYl2UeVqt-uTOtPHOB10eVZ0lKwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از ضربات یمن، پاکستان و ترکیه به دلداری ریاض شتافتند
🔹
در پی ضربات تلافی‌جویانهٔ نیروهای مسلح یمن در واکنش به تجاوزات عربستان طی حدود یک‌ماه گذشته و ناکامی سعودی‌ها در جلوگیری از پیشروی‌های یمن، پاکستان و ترکیه که تاکنون با وجود امضای «پیمان مکه» نظاره‌گر تحولات و ناتوانی عربستان در برابر این حملات بوده‌اند، اکنون از آمادگی برای ارسال نیرو و تجهیزات به‌ منظور دفاع از ریاض خبر می‌دهند.
🔹
کشورهای پاکستان، ترکیه و عربستان سعودی در بیانیهٔ مشترک تحت عنوان پیمان مکه مدعی شدند که امنیت هر کدام از این کشور بخشی جدایی‌ناپذیر از امنیت جمعی سه کشور است.
🔹
در این بیانیهٔ مشترک آمده که اجرای تعهدات دفاع مشترک و تأمین نیروها و توانمندی‌های نظامی و استقرار سریع آن‌ها در عربستان سعودی باید فورا آغاز شود.
🔗
شرح کامل خبر را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/466534" target="_blank">📅 02:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466533">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">🎥
حالا نوبت دعوای خطیر و کریمی شد؛
جروبحث دو عضو هیئت‌رئیسهٔ فدراسیون بر سر تمدید قرارداد قلعه‌نویی
@Sportfars</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/466533" target="_blank">📅 02:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466532">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0eQ64vVqCApJLTuQ58mwZ_IJPzVDXO8OurJEDeGflyAkOhVN39L5FvBRvPZCreuX6eOZjHDVU9iUePnWEvS0yUu3NoBaqedoI396ADBA4G0a9wwRWM_A8qbPyA9zv6pckKmx_PnPeStYbkGA7zKaH1mjD5JRvb_wq8FOejaFeF2pCZ8nuVKBIgsYqDdSb2t_YiYHR4lahTUKCodxgvoUNpwZ6Z3xPT9sPA3hb-w47i2m2Omiz6LRwRwyWAdfkM6vjhsBYtYM7eyGl3Zv0WsKN1vuC7FZ36Y_uD96FzZ0L7U2LG-smAW3UvWyRRzb-2fTGcacC3JaELx2eUk5TmMuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌ها از سقوط بالگرد آمریکایی در دریای سرخ
🔹
یک فروند بالگرد «سی‌هاوک MH-60R» متعلق به نیروی دریایی آمریکا در نزدیکی آسمان بندر «ینبع» پیام اضطراری (۷۷۰۰) ارسال کرد.
🔹
اطلاعات راداری، ارتفاع نمایش داده شده برای این بالگرد آمریکایی را صفر متر از سطح دریا نشان می‌دهد که احتمال سقوط آن را بیش از پیش می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/466532" target="_blank">📅 01:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466531">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cf32291e6.mp4?token=HiDl9cBw-zzp-Egli6nbd3c5LWdV68RHze2tPdy6jIsPOzIH0KmMMng4kREawA8Y30I7ddeemCFr7NqqEZMLQSTvnRxG6DFz7RXv_48tzub3zRRav6ZDGgkmjK7XfxwFM_TIZUhInuQqTatDscs3YcebpuyAAf30RRcuUNddzMyGo36dax5wvdszKFwY1xw8hmYk0-fA2v9ewfCi-2ANW6M0vwiBNhhSVC1DR1hk2h5b1GMVUO4tlEKOsxC1YQmvx76eQPYyBWVAEKd-dTt9shMQdFAUATGNZ5SbjLpPMUPD_GHjOo8_29NRYJTmJ4vI9xbwgagm-jq4pCRBi7IYUkc44vCXx4SK1aDICG7Z2gr8nj9zw2E4QMH3MbHbYrhfNoVu4cYx9eXGeo_VCwf_4VvlOsNqf-HGobZLQhhNtCCB0ubcKWbvdbrHJVmWC2iTtv9ifer2SZmlp400Emo93c3zphF2GDFTgnT1GxTj9R6VGy8X-l3l3bvstXsTBvPrwvjgt8sYxFJqCVv3CaAxdAqFsWA_WvVCB811qDe01jV8LG_qyH6ADMVPXbpuPMGkjN8KDGu_QdH-zGjC0BJqzJGaS1uVLl6-9S1rD4I6HE6bv-1iML-3P9p21Qs6gxBDAB57zOhE288MuvkEHiccgozbaaIhVnK38D4GRMEIuAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cf32291e6.mp4?token=HiDl9cBw-zzp-Egli6nbd3c5LWdV68RHze2tPdy6jIsPOzIH0KmMMng4kREawA8Y30I7ddeemCFr7NqqEZMLQSTvnRxG6DFz7RXv_48tzub3zRRav6ZDGgkmjK7XfxwFM_TIZUhInuQqTatDscs3YcebpuyAAf30RRcuUNddzMyGo36dax5wvdszKFwY1xw8hmYk0-fA2v9ewfCi-2ANW6M0vwiBNhhSVC1DR1hk2h5b1GMVUO4tlEKOsxC1YQmvx76eQPYyBWVAEKd-dTt9shMQdFAUATGNZ5SbjLpPMUPD_GHjOo8_29NRYJTmJ4vI9xbwgagm-jq4pCRBi7IYUkc44vCXx4SK1aDICG7Z2gr8nj9zw2E4QMH3MbHbYrhfNoVu4cYx9eXGeo_VCwf_4VvlOsNqf-HGobZLQhhNtCCB0ubcKWbvdbrHJVmWC2iTtv9ifer2SZmlp400Emo93c3zphF2GDFTgnT1GxTj9R6VGy8X-l3l3bvstXsTBvPrwvjgt8sYxFJqCVv3CaAxdAqFsWA_WvVCB811qDe01jV8LG_qyH6ADMVPXbpuPMGkjN8KDGu_QdH-zGjC0BJqzJGaS1uVLl6-9S1rD4I6HE6bv-1iML-3P9p21Qs6gxBDAB57zOhE288MuvkEHiccgozbaaIhVnK38D4GRMEIuAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بگومگوی خطیر و واعظ‌آشتیانی روی آنتن زنده
🔸
شما رو به‌عنوان ایجنت می‌شناسن!
🔹
ایجنت خودتی
@Sportfars</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/466531" target="_blank">📅 01:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466530">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">۷ نفتکش در ۵ روز در هرمز به آتش کشیده شدند
🔸
درحالی‌که تقریبا هر روز ترامپ می‌گوید که تنگه هرمز باز است و آن را کنترل می‌کنیم، گزارش‌ها نشان می‌دهد که نیروی دریایی سپاه هر روز تقریبا بیش از یک نفتکش را هدف گرفته است.
🔹
اکانت رهیابی‌های دریایی منچ‌اوسینت بر…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/466530" target="_blank">📅 01:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466520">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fsleZcUR0V9ddqv4Z_6jFUnZ-9B_Xqf6fvwz8OYh8aLBl9HBtUZ-E0sGE0iKrcuOK3d0B5d05dI7UG-gn3dOBbGj2G_xLlRqd5-SKuKo88W07TQBYbLRHvpBHM5d-9DVL_wyY_FewJAZJTdwxpr8eeUPlRzLtcZ5rUc05eOPBkEzdZCWIgpbcnUry51MxtOn1h08NgbbYzwAv7MNGj73F9uT1XB9atuSHscIIPR4ia9P4R4Pny_or8hauNpFIotOUoSFbWS5rxt12bUx6nMnCWndkwqZsI7ntTrl_Rk4fMMkS7zcQLjvYkWEpI2Sm-vMQO4f2t1WlO8eHPaWyhl7yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGzh5UXLA_HvJlnG0XkzYaaf4dmxNGpdqCCXpoX1Y0T7gxM6Zw5MTUrRVmnyttEQKPvqaG4XRCBHE4-CWnNfZzrZHO2B0jMOowROlS-Sjwayp_u4P8WMH8-UQYdFl4YyUZ9K4wrSfwbLrEPAzXev63O9FVxjBEH38s_sR4uU_ysBrB9rsQC9OKliKue0_NrXzodnoatG6ZoKZdzSnBeWMDgyCvm3slH9ZFqKtxhHO3scFSC2yw8AOby-O0WQQ6r2HT1w1Alc3A5UgYpc15i4Zk4ODlWr2QozPSUMTRLGyosU02k0e9L1Ql92xQd9bonp4VHk7rOaBaZr0zczEAi2Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m7pJfLyMpBOW2kYtPOFjDWnlQsiN1FMUmlAPNgNxKNIPTvrMr3vWzZOX6N_z_VjZXjP9N-DI9Bpy-v-2uyjYsY1b778BVXd2qp62Uzza1xJIzZRP-qzQxtuflpJ8-1MrvugQDpDV-w-D4NJCPv_fTp0QXbl9qaCALZ4uqha0kXUw9NZB5_-YymP00Ebfj72knOwhIGvTgFbVmcDcsTlm1pBOZ8VqbQwoOPdRJ1iYVRO08dNC9N0-wPjRuaOGR5oTSDnFPqJMQF6_nIpeVlsJwkEIhjRmBlK0x4hmTLQiJRS_xvdgV9zRNb5uZ5eqNxDhhRDeopVbu1_3Y2tM2l-neQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UefHPHd8ITxuFMGnnA7H5cUircYt1Yqos0nqJQNZvJshxci1eGv_HI3i7D7IjesBvgGcfJi0KbAHwZAwDqYN2xnibYQNZwIMXU9w0PU-c9fjaCTRti3doz_JaNBp90HsFjHn_sWu9TOytupGW17p7i5BmZweWN2zmYZ9VS43bEJXM_pYnKuMOnOXV3IIgYP72Wcot-fVCgBeBd1U4mVxXP53yj34JtYt4ADiq9KkjYuJyY3M7fDSvyOQKfEdxb7Bbv3f-G7OLutDoCJTR_rmB3Zxw_PDtWwYBbH9dMUdH38sTEVzgTeXTkS6FyVM4RMC6qlFeaZKs1Dc0JMSZr2kNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QQiE4Per4y-ySbu3bBScyAJ-LLDi0gsMsI4YUi5ay2HRYvuB9fhZgnF2m7yRRxyQ7_hgDY7Ht98ls31Cf3OOhEwLCrmwQlnefHE5PAerQ8v2BuFWf9BaYJqiX2CAepsiK7qWu8dsD8pxZ03I3UvIGSxqCy732RChAkG7nBeQL_OUi_wiCZRbg493BKbTtRGI6150COdcQsg2xpUC3_5btWL5gS7vohTYObt6M41cgRA-_8mA2wAo4kFLjx22PKG4Q9NxpDxQRG_hXAT1fS-tJOO_3253bpAZGrAyDnXT7XdYgN9uAMK8KqSELRaxNWlxXkvaiChPUmGHGtPDFUrnyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/puNXfUD85AzzJg-5VRZMmEIxVy-3qR0I7w4xxU-rq3e_uqwM5gkCBE3RCDs5G2vEk43EumRMwRpwdIlNjHIyXjjXK7XmNYY38ECvy3CpC5x24XNBq_bQL0mjc4a5hXPMlJyUveMrXakqT_i-zRonBNz7uBax43LVS5YiYdG3b-YFhWFFweLOq6nYH4NNPtzYLOuDzfbFVjfNJ6_-7PsfPYLDfvHETJLGdv1m7DOHa8de5hfFJkEHyYz81HxZoYGQBdoqNm_QklAdyTks5SjFJQlIBqpZ8tFM03q9wPUR9vDeLx-skAFCnJPXzdNyKTmXz4ap45UkKN72Gbh6xcYc2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nyXYha4mbBp0UZyWcq9w8E239xTF7RJAliNjs9nHEu80dkXlI5saStmtgwP9NvkVPhGLlawz1pU7pJkOWp2shjJMXfMwcvIF7OXA9gDTpifCyQamjFD9YvUdf_L7HLvwqyegLkFDwMLti2r5-rXNbXYttgnvlNyHoADYoYFAjAjj43bDVYgJWxbjA3kbPjjhYTiaeMqxYIzFrRGtKnX-YmF6w9m5S4Q8kuS6wfA_V-XJCYyUwtG1gK4UVG9PVG-Wc7Jg212NH5g9IcFODP0kbYPQT4NWCRpNuaQKqJd3fYRDj0YkySoWzuiKbMNhmx-zxkWYOfjXpKgpVbtsepHjMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CGeGoHWlFI5FL-ZLJrXO50t8-bcKrN9NkGp-tdwtnrcv7JQizUp0m_feaNfDKjPpF-N4mDFyoBNN2CgAHcvrIEIRmCscSDxuhDbrOs0ld9Z7xeuZRMAA3LfU_Jth3297pwCbjCIEbmXYHcdXlsIL2fv_gUJE_h6QcCilNEZQDalJkrEjh46g-fsrkcImXBNtI5zPv3q9wiqYH2gCLXTiPK2kHy3k6SvX5spfQWKykcWnGsO4eb21aV1SiAG-8xWQCZwt5CkEwCwX-1O0tO6gRdnneB_zYDFVnTEKDKarFSKoxOnivwcat5z7f8VaU4DEXLm1DGiZz6t8ih-jjb2b7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v8lOr_jereEm_6qWzXIyQI8yw4m10E3gu49qi24FArNNAS7B4VLwMxx6BAkE-v2yZkp3U3zgQ8d1hR_YTuQmt0_wbnAl1mS931xHeZJOe86fmiY9O4vyBILzl4KijBW0LBgT0yn8fxvP8CDV1DHMupmfNuDvSSkPOpXaodS0LSlElP8JRM36WQxjjVrhDyF3HVhXIa6sFtAj7Ln2oDrr_u-o1OfptGb6Dl8d1U1jlWHU7ElNid7ym-_hl8dwwI4f23ePvtfjNv941MWoL1I1k8CgzFNVFkof2_5mcaPGb0dvys_ZBL_JsRAbzAnC6r7SmId-Kxlr834xZnT0aQQQcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BPuCge0o3LP2BLEejIWXEiG0udg24wzFIT6geAWuCMBBy9ARpGpggMuCMtLfbkvbu9NUiHc_vy4w9uW6p6TXZi__aQSURm0PdYqHZKwMlHVoco5qBxj4DyhnLYLDg2T8-LFqHZiKe9rAQ8wqXo_PtYQ4934OfiAhlm5AmBqnJRSAOkVA_yT1UG7AwLery7Y5BKlSucsnjf4wwyEEkURFq9ixlyh0ea7pYx7PdfOGTESKwH10CkHsbJdNg19tBzSRliZW6bgfr32mpD8gd08XTIXKLoiKiZa4EkD2UVJM8loL5XEPns14sCG2Oc6etPBMSUrgSmFd1Q-4rHXLQ7MuZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بدرقهٔ قهرمانان؛ به مقصد ناگویا در میدان انقلاب
🔹
مراسم بدرقهٔ کاروان ایران اعزامی به پنجمین دورهٔ بازی‌های پاراآسیایی ۲۰۲۶ آیچی–ناگویا در میدان انقلاب تهران برگزار شد.
🔸
کاروان ایران با نام
«جان‌فدای ایران قوی»
متشکل از ۱۶۶ ورزشکار، شامل ۶۲ ورزشکار زن و ۱۰۴ ورزشکار مرد، در ۱۵ رشتهٔ ورزشی راهی ژاپن می‌شود تا از ۲۶ مهر تا ۲ آبان در پنجمین دورهٔ بازی‌های پاراآسیایی به رقابت بپردازد.
عکس:
صادق نیک‌گستر
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/466520" target="_blank">📅 01:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466519">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSVk62kmWYDvHVSrOv_-g-4ywQZUUG3IBTyVufFczzuF_o2li61DbY9c5abMrueDYEdWrq6bEYHMk7AEqRTRubzjW0D7U1IWx-gC6QgE1ZEEBxtuOWgNtVhJveDNgJKiv1GzLo5Sd-h0VNvrQN9BSSV2A0uZ2z5CSh1zXqNHgPgNh7r6BCyaQ-0x95hr1A6pIDr0XqMJ0FZ5AGJfn1u54NRa-BJU0dtAgE68MEhILamJGypaf2nG45yO43EQ6rZW1ird9OSK6QXb54narq_Mp_mDKq_Xcpt6XpgYyCzNcV0tewb5xexrjXoPGwDLb8443BA-oo4YI3_--WfMoVcD8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر کمیسیون امنیت ملی مجلس: تنگهٔ هرمز باید بسته بماند
🔹
بهنام سعیدی: بازار جهانی اکنون هزینهٔ اختلال در یکی از مهم‌ترین مسیرهای انتقال انرژی را پرداخت می‌کند. کشورهایی که تصور می‌کردند می‌توانند بدون توجه به نقش ایران برای امنیت منطقه و انرژی تصمیم‌گیری کنند، امروز با واقعیت متفاوتی مواجه شده‌اند.
🔹
جمهوری اسلامی ایران امروز از یک ظرفیت راهبردی برخوردار است که نمی‌توان آن را در معادلات امنیت انرژی نادیده گرفت.
🔹
پیام روشن است؛ نمی‌توان امنیت منطقه را نادیده گرفت و همزمان انتظار داشت مسیرهای انرژی بدون هزینه و بدون توجه به منافع ایران در اختیار دیگران باشد.
🔹
تنگهٔ هرمز امروز به یکی از مهم‌ترین متغیرهای بازار جهانی نفت تبدیل شده و ادامهٔ این شرایط می‌تواند آثار آن را از بازار انرژی به تورم، تولید و رشد اقتصادی کشورها منتقل کند.
🔹
ایران به‌دنبال ایجاد ناامنی برای بازار انرژی نیست، اما اجازه نخواهد داد، امنیت و منافع ایران نادیده گرفته شود. مسیر کاهش فشار بر بازار جهانی از پذیرش واقعیت‌های منطقه و احترام به مواضع ایران می‌گذرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/466519" target="_blank">📅 00:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466518">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">تمساح</div>
  <div class="tg-doc-extra">قسمت ۱</div>
</div>
<a href="https://t.me/farsna/466518" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
#روایت_شب
|
تماشای معمولی با پایان غیرمعمولی
🔸
یک کارمند، همراه همسرش برای تماشای یک تمساح به بازارچه رفت اما در جریان بازدید، تمساح او را یک‌جا بلعید!
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/466518" target="_blank">📅 00:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466517">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxkETbM9YqNHtBpKcJ31r4zkxof-VNVW3k_eizMM2LY71-Cdw_s6dvJzf_vqRVmZjuScKv8wg1_qTjHiGls5Uaahd4gxcl06o_g3Rf_qKGMAK6uj7S1nvd6ck21yCK7DJx4WsFh41h402xS_aIUpNVP2uHSRaB_gMf3IyxdhSV6fJz1FX-mirrxhZwFdbvO5YxYS_Ati-LwnWE49dKjoFOe1Iohkhmn_MAmaLCR8ClbI4ITaWmo0MYEG0WtY6CV6qkgZhccUCTHzS9V9bkaxoBrWZl-LCLo04oTi_pSrY3v5R_zeVrp3QTQEYPQWckmIZGLsWLm-VZ-zozkIsyIswA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
برخی منابع می‌گویند فرودگاه ریاض هدف حملات موشکی نیروهای مسلح یمن قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/466517" target="_blank">📅 00:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466515">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSJsAguLqK0i4-kmWMsljDFUb0fydnCIfEIjOC15NtlXEb_HpnsDpw1vQGPJD5vJZkJY_YhHbSMM9kkImmtsckgh-eL20mDqazNE0vR_E5Kc9AWnaoXX4FpZEVz_vAUFYKcReweOgh-2s36f1yzZ3-wHxifarLcIzbn-DwM2WwHQvN705dr8sAeTlKGjvTrDmRRJNmfJqax5groIO2tqW2O8WWvc0Rt-K4_R5Fy5PjsTunlgWuIBKSRrDituX_PO9SqYbodyNhve16G3n965OKMvxSxc0YoyH6YS91tYN6EhVf9PdfcfmWF9Tkqef48jf7ly8EgGla6ospw-v7eQ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دهانی که بی‌موقع باز شد
🔹
در برکه‌ای باصفا، دو مرغابی با یک لاک‌پشت همسایه بودند و میانشان رفاقت و الفتی عمیق شکل گرفته بود. روزگار گذشت و بر اثر خشک‌سالی، آب برکه رو به خشکی رفت.
🔹
مرغابی‌ها که دیدند دیگر امکان ماندن نیست، نزد لاک‌پشت آمدند تا خداحافظی کنند و به آبگیری دیگر کوچ کنند.
🔹
لاک‌پشت با اندوه و اشک نالید و گفت: «بی‌آبی برای من که حیوانی کم‌تحرکم بسیار خطرناک‌تر از شماست و زیستنم بی‌هیچ آبی ناممکن است. رسم جوانمردی نیست که مرا در این بی‌آبی رها کنید؛ فکری به حالم کنید و مرا نیز همراه خود ببرید.»
🔹
مرغابی‌ها گفتند: «دوری از تو برای ما نیز سخت است، اما تو عیبی داری که پند دوستان را سبک می‌شماری و دهانت را به موقع نمی‌بندی!
🔹
اگر می‌‌خواهی تو را هم ببریم، یک شرط دارد: چوبی می‌آوریم، ما دو سر چوب را به منقار می‌گیریم و تو وسط چوب را با دهان محکم بگیر تا به پرواز درآییم. در آسمان، مردم هر چه گفتند و هر فریادی که زدند، مبادا دهان باز کنی!»
🔹
لاک‌پشت قول داد و گفت: «فرمان‌بردارم و تا مقصد لب از لب باز نخواهم کرد.»
🔹
مرغابی‌ها چوب را آوردند، لاک‌پشت میانه‌اش را محکم به دندان گرفت و به هوا پریدند. هنگامی که از بالای روستایی می‌گذشتند، مردم چشمشان به این صحنهٔ شگفت‌انگیز افتاد. غوغایی در میان مردم برخاست و فریاد زدند: «نگاه کنید! مرغابی‌ها چطور لاک‌پشت را با چوب به هوا برده‌اند!»
🔹
لاک‌پشت با شنیدن همهمه نتوانست طاقت بیاورد و خشمگین شد. به خیال اینکه چیزی به آنان بگوید، دهان باز کرد و گفت: «تا چشم شما کور شود!»
🔹
اما همین که لب گشود، چوب از دهانش رها شد، از اوج آسمان بر زمین افتاد.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/466515" target="_blank">📅 00:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466514">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhtmBi8NegCiqI-TDlRj7MEePacHeuYZCVVgtG0QGz1V8zssAkzBQRfFxDSWs9ANkQr4PKpQ90U0jbGnYB3CUTcje6wxv4KP13gpAmsB1IfW7lXT0t5RIYfa7DBBBVCkbTqcrec5fmMsiwMOQXJFdhlbBvG2ULzDqHNs8GLIkD-dw6AzTbZeM6S9Jk9aT9O0WxGNiJ10CnjDMkCCW8rbNveJNpEZlW9ry2R6MIuC-ExOKPciNgT9xb36tV_wLgvHrek_Rfr7TLDofq5lSm0--lRwuZDFooPZCNa0vH7AVtxe90og8JFurIFtOaZwIbU7flgS937DO3JX_AI4y9eQVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/466514" target="_blank">📅 00:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466513">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFFifYhRZF471__bk9XQl3RZK2Hztmz7gNAbnNmwW00qTwrPR99waljqw4aHJKT6QTFbB8GnyUVGFbO5aYQfBo5KDSe7gezn_Ql5rhmMxnMKpvcUPTzAxvKm9RRSue8-WcVYIvnhnSof6shenRiXsfALZLsGrQBk2wuKkuyGZG0wBi35SVr_5m4gUIDFOl-0LWSo51BADQH2QbYs_5R4uQlf8vuAww02VsAsUqNz-dq7dtJhuVT6u7su_GtNLJjK6jePOEjBooR_s75U9MrABpsSAmpJR-kQD7s-iBqQgd71cAEeCKlp24L01lfWAl30rgxeYzJci1ITETYP5sPTiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای مسلح یمن: در ۳ عملیات ۵ هدف در عربستان را مورد اصابت قرار دادیم
🔹
فرودگاه ملک‌خالد ریاض
🔹
شرکت آرامکو در رابغ
🔹
پایگاه‌ خمیس‌مشیط
🔹
اردوگاه نظامی در عسیر
🔹
مواضعی در نجران و جیزان
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/466513" target="_blank">📅 23:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466512">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">جزئیات واردات خودرو برای نخبگان خارج از کشور
🔹
قائم‌مقام بنیاد ملی نخبگان: نخبگان خارج از کشور در صورت بازگشت به ایران، مجاز به واردات یک دستگاه خودرو با سود بازرگانی صفر هستند.
🔹
همچنین این نخبگان از حمایت صندوق نوآوری برای تشکیل شرکت‌های دانش‌بنیان و مزایای قانون جهش تولید مسکن برای خرید یا ساخت مسکن برخوردار می‌شوند و در این زمینه در اولویت قرار می‌گیرند.
🔹
نخبگان می‌توانند تجهیزات علمی، تحقیقاتی، آزمایشگاهی و حرفه‌ای مورد نیاز خود را یک‌بار و به‌صورت غیرتجاری وارد کنند و از حقوق ورودی معاف شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/466512" target="_blank">📅 23:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466510">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/llCut0WV4Sh5dQ3NUs8se3oYZtZbZXIl8alartwA2Z7KoDrVhJDZuxtlBjwuilJhrRzHetKwfiy22Z-DfKvJm5GImiOu1BmbRBTIPB9JIVbPpg19b_ftVJ6tNR4s0ahdZXRakTXwygGJoTfjHsp2NcmXVi1huXf0ZHZXnckAt-t4CPtMeD9LRjmtMJczwnOpedJhqomKODnbu1Q5XHkGFzMRDFKXp79ZyxhhqBnQw_l7DV0_WB2kyAFXjD4ESJRQwhbmDgBulxp8m5XSBjZ-wgSSqcXxJ6IHhVkfLaZ6TY55REVMlZJYbt5WGTCLYeP7AvvW4dBdp2rDgtCmhrO1Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XFOafkyoPAVcQ2Yr8RowszzsVARsma0C8miKj9Jof_K3H4EXHTI9w6IMlgtTDxnGGeGasU88aNJpnsrev_D_5yjl-CD-KEctCUcStvph1r_jtArHGWOFlumu-Fv8GmiUh8oSya5j-FjlITZRZE7meDchg_UoPZYx3nJH6bJOv9oBFPsn2Hs9MmWy932WngBqV7BTELAdNg-PkHm4D7kKQwoodyzu1VY0savbWCLlIhoxSHYX9bxslv7p5OJLK0DftRy9sItzdr4hHwhcq5sjmrbfHVOD9WGFTnWTcikqk3YWILvjqwoX6Hs3Y-wbXR5ABXXWULEIwe3OGsPieIn9pQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از رهبر شهید و رهبر انقلاب در رویداد «جمعه نصر»
🗓
۱۳ مهرماه ۱۴۰۳ @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/466510" target="_blank">📅 23:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466509">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ff1838966.mp4?token=Wvbkr6iIIj_-RlYM2mm1ER9EuxCdq0ExAfTvO8XcF_HjmCnsxcoYJJRsfS5rRyfFVJMGV5AtvJR8iIrNgSFfF3HYzGR-0o6eJXodrlVr5-r3ERqcfunGZ7u0440Pa6gQsyj9XD1_zT-USJ7g3YO5TDzOTgOLI1du_xKLVDKdq86g0P9mEWxXJx-FpGk5D-7KQtnjg82xE0Ogr0w1kYR1JG7OnGlbQkzRWyFU5muKjTX4fe4iBnDwWIm459p5QpuOAA-nlCZIGSRZ1t-9EQyZSt9cDZ2C-EiStj9dOrj4U9lBTnjQlkqt7CT2PBp3DyRWhCgzoeJktpala_03MUtUXwwmq8Ub1dhGylUqJig3H_L4OqIcUoh2dUDpYL4GRJx1S0y8Kxr15cLzbQcEJ10f6egHhMzIZMJZUY0b4cX8RDb_q_vFvKVUwuzXXW53lJspPz4Pv-wGvTSH63DQYsmVRDesdEIU4LMoXkG00KWi9yoduK6YCyXnJFv972-0TQNXhObFESD8zfHTAUfrOr67x5PDQGnbuETvFjcsoBsNYoUh-pjQ0B-FiD7rvqyUv4HTlpLfdYfraLcBW-RWrB4SI-xGHUVpBlkRSJ3cGdQb003ElQYZ0HArpVD1NZkMpjIM12XHhoEXKEb1L0K5IErwPnG6FNQ0JLQwLUWXNWVexPs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ff1838966.mp4?token=Wvbkr6iIIj_-RlYM2mm1ER9EuxCdq0ExAfTvO8XcF_HjmCnsxcoYJJRsfS5rRyfFVJMGV5AtvJR8iIrNgSFfF3HYzGR-0o6eJXodrlVr5-r3ERqcfunGZ7u0440Pa6gQsyj9XD1_zT-USJ7g3YO5TDzOTgOLI1du_xKLVDKdq86g0P9mEWxXJx-FpGk5D-7KQtnjg82xE0Ogr0w1kYR1JG7OnGlbQkzRWyFU5muKjTX4fe4iBnDwWIm459p5QpuOAA-nlCZIGSRZ1t-9EQyZSt9cDZ2C-EiStj9dOrj4U9lBTnjQlkqt7CT2PBp3DyRWhCgzoeJktpala_03MUtUXwwmq8Ub1dhGylUqJig3H_L4OqIcUoh2dUDpYL4GRJx1S0y8Kxr15cLzbQcEJ10f6egHhMzIZMJZUY0b4cX8RDb_q_vFvKVUwuzXXW53lJspPz4Pv-wGvTSH63DQYsmVRDesdEIU4LMoXkG00KWi9yoduK6YCyXnJFv972-0TQNXhObFESD8zfHTAUfrOr67x5PDQGnbuETvFjcsoBsNYoUh-pjQ0B-FiD7rvqyUv4HTlpLfdYfraLcBW-RWrB4SI-xGHUVpBlkRSJ3cGdQb003ElQYZ0HArpVD1NZkMpjIM12XHhoEXKEb1L0K5IErwPnG6FNQ0JLQwLUWXNWVexPs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران حریفِ میدان‌داری سنندجی‌ها نشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/466509" target="_blank">📅 23:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466508">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4N9yYxw9O597VD498-rf1YZeSUtzmOYvk4LUDtM7tEFLYrCGGHdvtKdDbj8uLPU3zwsi6ZtuED9DaZ9X7LWvpd2hpu8VfMEMClGMufr0InUuiDgqVg-mnnWrd3xNy0jnaw0jSQxtWoB57O97ZLb1UT7mp0KrewT3rkCayUhqwo7eHgMji1kYs7c9s8kiBMP1yuckDNQaoCl3UYv0TUwfcx6DlvU3FzpcuiYmDZKgoLT-YkuavEoFvU_1OXaO9xY-dJruSzEdohbIbnx1iu3zl4dscV87O19FY77m3eX_XhTTCRlCtTu7b13-06X1WvvybVQyqWCpTaxgzBg-FhawA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رئیس آموزش‌وپرورش رباط‌کریم بازداشت شد
🔹
رئیس‌ ادارهٔ آموزش‌وپرورش رباط‌کریم تهران به‌اتهام فساد مالی در آموزش‌وپرورش این شهرستان روانهٔ زندان شد.
🔸
پیش‌از این ۸ نفر از متهمان مرتبط با پرونده‌های تخلفات مالی در آموزش‌وپرورش و برخی مدارس رباط‌کریم دستگیر…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/466508" target="_blank">📅 23:26 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
