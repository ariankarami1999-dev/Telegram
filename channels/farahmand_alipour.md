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
<img src="https://cdn4.telesco.pe/file/bpEiaJBqZUMb9k_GwUxW30hxMdTYUpYZstdaxatDW5NJj0cLoVElwwY91W36SWLTiWH_b-t0OrANjJZcQcBeedh5Ah_J2UiiGAPmPu-pY01aw-f5rk52b1pl-VY5yaOhY1zb9ZPa5Mgdar66ZUQgWnsE_NkbtJMknNmVSw6KLXs844Aua_hDbtj6YXs8hrO-gcBAEyFE94FsX0NP1o2qF-bU9_dS_9G6aSjHvv4hBGVEDFIRZJTbREDTynZeiPc-BklLyvT_yOyiJNG-fZ4Y7n-2zoWm9_rhl5eLfGFgCDdu1y7IoWZuXyMVGqgAGGRo-o7Z-AqYY_GbbomeWAJzKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 01:53:59</div>
<hr>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTqVQFinp70oz5TRHA5W7JpxzXlz74iqygmxNnv2ReML2BVuUsNEzpAHBhy83RPDf8ze2YQ95cTAjOlvVya1cfyZWZtW1Igbk6_tOEZKu8vQ5RqQp_Ndb4qN5Pa22z7SaXgzwck0eaZH_t5Cx7RludIRZTQtvm8zEp_g0vagqP3WVN-dfnqp6OsAhQA-729j2m4oagCiKkzMfGJyG9cDAL1xTznWPdMgGdTbXuGf4opboTSQ0FNVBFwboIh8iJTIp2xKW3zqpVKr5BmhdoOG9dXk5Rd0KD6BgWQ4C21Plmr2BdV2Cn4oiie9UBlY6U3KIF2QRCsv8g-N1VMaxDvV_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjbkYuqHCX8tvk8FH738oH6LbiW0LBtTtr51yVpVZLz_IUafjqyAmhutjet4C8pXhfMEKXQ3fzUZpI46h1Lr98uixjbp9vEAbYLBZMIzDnFPUTsQaRr36JlyTJ5JzG09hpJJvhwdDc0duJSFunKhvqLDArL3c9idpHajMBVIZ9heLshXp1hBxXpGnfn8eFzUA_jbM_KKJ2nIV2oe-E5ml3PL7uYj2p5QDVRAVb868m7gnyGMVDqEndNejC-fpQm-tnQ75DCKzizXsXmrjMywi_pIEJ8f4-vGDm2A_PRKP_kw9FuaqbjDC9FJXQqDsYYDNSselLkHNpUozWE01bf5Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=AG5EkUkCCI8xclPl9ny12A_28p9l0185u4ab_blvCGIZiDujcfhWmFqJwQw3ieiWgs4wBX7tTahaE4-KtNHXHP_x55tuofubLxQ7YSyzzCzvQsViKI06laFm49mH6iX_gX4UxxBaNpl_nEFm5En-SbhgNGuju2_PpxYYGMWnI0I9jDAKstEDn9ZlWg386jFN1O1QSK8AkT3gwV1v7NzGQCOZBKprX_yDrHRhTlraEmiqsfEkAM9MBgaYrzHZeZ5hIY2pjAgV_XmV0EjN-BUzHGlprJdQFSbhW-mYmHL3INgGceFYz8hRXVZ7tIuGZzgvO6hlFTWnE4AIQ5qv4jesJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=AG5EkUkCCI8xclPl9ny12A_28p9l0185u4ab_blvCGIZiDujcfhWmFqJwQw3ieiWgs4wBX7tTahaE4-KtNHXHP_x55tuofubLxQ7YSyzzCzvQsViKI06laFm49mH6iX_gX4UxxBaNpl_nEFm5En-SbhgNGuju2_PpxYYGMWnI0I9jDAKstEDn9ZlWg386jFN1O1QSK8AkT3gwV1v7NzGQCOZBKprX_yDrHRhTlraEmiqsfEkAM9MBgaYrzHZeZ5hIY2pjAgV_XmV0EjN-BUzHGlprJdQFSbhW-mYmHL3INgGceFYz8hRXVZ7tIuGZzgvO6hlFTWnE4AIQ5qv4jesJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=EVRLWKK1gxH4nmYi8WrYJtmetFEicLolDhhfT6yy2WnjKjFxnN72Huerk2L_yz793iWaaJpiH6iFrfMLd2P1iQWvo6st2s8EJJaYB4qtqpuyfZF0XaTS2XtZbs4dH12fPSA4kAFUguNw51E2adC6q2JGQUmm2cB3xcTzBGR7amN6IgWgAVsMTYeW0OWEW1AmaA41_0qDk9vobV4k2naQnI-X-u4E66lV_s7iTDkP-ump14tER0MVQ1mGmiHLJQtnJmyWiTr_zgp1VDa0DSsw9_PyKlllcQFWfRM0zY0D2px69kaGtUne0L3HlVHKc62Xr6Mpot1WdizWpCmgsh1cuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=EVRLWKK1gxH4nmYi8WrYJtmetFEicLolDhhfT6yy2WnjKjFxnN72Huerk2L_yz793iWaaJpiH6iFrfMLd2P1iQWvo6st2s8EJJaYB4qtqpuyfZF0XaTS2XtZbs4dH12fPSA4kAFUguNw51E2adC6q2JGQUmm2cB3xcTzBGR7amN6IgWgAVsMTYeW0OWEW1AmaA41_0qDk9vobV4k2naQnI-X-u4E66lV_s7iTDkP-ump14tER0MVQ1mGmiHLJQtnJmyWiTr_zgp1VDa0DSsw9_PyKlllcQFWfRM0zY0D2px69kaGtUne0L3HlVHKc62Xr6Mpot1WdizWpCmgsh1cuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=uquHqQzbEwhtkOxOt_uVeo-8FRNcxGLr9CmO9j2R79RY1fQhq5v8ENXuwhmMxfTqPCirNM8L3_B-MS4n_tZKdSHR3eLpk--4o1XLOmjJJfIU-p0jrSyvuySN2rO6Weigo6d8MqU_nKUKY2MBPrO5u4y6bAv_gsnJw3HswJmNnB1UFZ8fW_Kz7qc0QgMDsgXbU6cIRZGR1gfO6r6_WUPU1xPVpEx-Z8MfX1eImtHe3UezgbhRelLV-5JxIpKYIG0yypnZWZpCNefgSziqPWwdNcsOZmpSTEk8R3s_iiw59BOpWrfHM52f1V3QyubYGjQAKgqfSIGfKs_ZkCuD_R0k9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=uquHqQzbEwhtkOxOt_uVeo-8FRNcxGLr9CmO9j2R79RY1fQhq5v8ENXuwhmMxfTqPCirNM8L3_B-MS4n_tZKdSHR3eLpk--4o1XLOmjJJfIU-p0jrSyvuySN2rO6Weigo6d8MqU_nKUKY2MBPrO5u4y6bAv_gsnJw3HswJmNnB1UFZ8fW_Kz7qc0QgMDsgXbU6cIRZGR1gfO6r6_WUPU1xPVpEx-Z8MfX1eImtHe3UezgbhRelLV-5JxIpKYIG0yypnZWZpCNefgSziqPWwdNcsOZmpSTEk8R3s_iiw59BOpWrfHM52f1V3QyubYGjQAKgqfSIGfKs_ZkCuD_R0k9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOnvpxa3yMMXdMFzGbv7vNk5xdCTrkFF-pF-B691LL-njXx_zK48ITb0b7Wb4fpnecu_uxVscObgyoAiJf-gMEypbFAM9Noe1NPADZno3BHq9_wkY4OiJPXgSn_aOyXROQF--2wctSkrd7O8zoER_KhgMGBOlAodROTaCBJBW6TnZ5zRWX6Scv1fSaZchDASMkJZLjK--5YPTFJrTepEy6SYr8DlYOTmYNkMnGnhKGAod17RLdRFVFguvQyUEdJ2V8BdSb9QwNLSarYYITsO8EPyxhZlXS3ZwduwJHYLPUzR7zmyid4ARVcg5Mgf-FlsOKKPm2pLeTmIhtl5DWXB1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8ENc9FHMupRDworajGVK6jscJpi0uhlxQv95RXHr570s_3DSYqHRildrxUN4Q2VRdPHLGHkQ22RQ2TqbWEpqvZSvcw7qvIXTqD4yPK6tq6r9LaDZS2_pPpHi3dRD6do0wIALoZoM9cT_POnwzwP3Kq_4OdKheJ56FEYBWi3WcK8j8A4YbPn8FBeslffZE41mwgnrwzVjuCPjdepbwBwEJ2ZyXr5o1bnlt47ZTZK5qJ0TXpD5uQcciElkVYxSThYMZpas8h7Lc5dq_epY4VVB99NGxUpcJI2BcrlIlXD7frXWdcMJumDLEaq1kaAh69RcXOSJh2dnnE5Dx4eSlsRqQUE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8ENc9FHMupRDworajGVK6jscJpi0uhlxQv95RXHr570s_3DSYqHRildrxUN4Q2VRdPHLGHkQ22RQ2TqbWEpqvZSvcw7qvIXTqD4yPK6tq6r9LaDZS2_pPpHi3dRD6do0wIALoZoM9cT_POnwzwP3Kq_4OdKheJ56FEYBWi3WcK8j8A4YbPn8FBeslffZE41mwgnrwzVjuCPjdepbwBwEJ2ZyXr5o1bnlt47ZTZK5qJ0TXpD5uQcciElkVYxSThYMZpas8h7Lc5dq_epY4VVB99NGxUpcJI2BcrlIlXD7frXWdcMJumDLEaq1kaAh69RcXOSJh2dnnE5Dx4eSlsRqQUE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=FX0--yIVzTty_e0CyZEfIqykjL7Luki0bnLnOnZuOdDq_S7E-_JmndKaanId45ULsd8s_PdSpkFPN2-cwDHXvH2BvlO-_y7uJ0Ie1CU0gl4ko4vGZPjM06qchSfFvXngAZVIPCF_XD3CdgQIrhOyqrU2ebkqyZRRWJc0xnGzDKJPI9nBBcZUoh1hZZoI37sPbENDBxIl_sAA2WGr17MhOQYC-X-YaMsyAXXibupy9_4fDcHPDnRZMJqGE8Z9_DUiFfl9ufh5UvWNz3qY9PY9Z5ofaFeaTuZ95SY60sfq956mXkgpWV0h9jX17AZvHNiG5cSOimd60kxNAdohPu6dcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=FX0--yIVzTty_e0CyZEfIqykjL7Luki0bnLnOnZuOdDq_S7E-_JmndKaanId45ULsd8s_PdSpkFPN2-cwDHXvH2BvlO-_y7uJ0Ie1CU0gl4ko4vGZPjM06qchSfFvXngAZVIPCF_XD3CdgQIrhOyqrU2ebkqyZRRWJc0xnGzDKJPI9nBBcZUoh1hZZoI37sPbENDBxIl_sAA2WGr17MhOQYC-X-YaMsyAXXibupy9_4fDcHPDnRZMJqGE8Z9_DUiFfl9ufh5UvWNz3qY9PY9Z5ofaFeaTuZ95SY60sfq956mXkgpWV0h9jX17AZvHNiG5cSOimd60kxNAdohPu6dcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUIFPTt3kZkRq5RjumETcNKCTkK33JcQlyruONT3qksb7sHWHt-rf8SsRd81OSHIT1ZXjmrP_HWPWOjma9VwMSb13jlamV68KYwjtFRoVwXSI_yrPWYesdZ9-4w-vhE8aZZ4yf_G0Rg-2zzUbYEchqVUFE8AuJ0xwTK3d_YsEIu28CsoESl8RYBlxL21BuFJ_Th9JaBp2tedq4ApJGtCnLugWehFVGY9fjKZEQJxSz5rmMbzzNeNQXXspOuxTN2yttg879Y4OCjCihgQXlXywaRtNMYRz_xuVHvAfN3jgR9VFF-CKcapgTeDsVMBlcZajPO1jnKWdW5V-GLKbVUhJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=ESnN8mrtxHsd6gN_CB1HZ8Cg3D2ikeXJRfEAGBP9YYp7wZlfUsdMXse38-98nwAwoUfCIcz2CrPVzyfbUbCkAkRkJoilTIfzAfY2iSxjRimYq_D3lhYhPdeNZxMPqjcU3ZHMiRwcstQnMo1inKfB8ueJzPIVLr8ftmViEDhfzhYPenLbEkvSzM-o_AcYPLAKqFXaM1WMVJ_NBwpMiuwomOHaNu24FLtsqRWPqZw-WVDBugGOp5E1nEpEo0Il8Dq4IAA8h5ag93vuie5rjgM29-BkPIozDZI8TDOI6klJhJuRlYKfFnkrjK7Ll8DePgIf7veaKx-3IS2rJ14YRabcDYGbVVgMVYP6XljUsuzobgWcUp78VHP2c4AJAwF3XheGM-36mQtGJBfhd-yefF10NyZhbZ4OFG_WlxxBSZocoNMxOLp5J-W3JuSyNzv7jwefQ0sVyjkByrnvf0EvP-s2VMisdAKk0SrzGEBgyBJAPkpbMAaEHyHjl1oSOUuCK38IqhN3eJOzoqHZOAU6SmJwEAWoTlmzPgQf9XKFRCw0v_wp2H0dVByRCM_8-BNnr4QKuAqHbHE_dfsMW7qP1jbMYK4g-pbsfMYbVd1HjP90vDVcU5LdMaRn6tb3QUN4tP7hUhvrHKaRx-GDSLN5npm7UD3TU74vbVPQ58qShkE5uVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=ESnN8mrtxHsd6gN_CB1HZ8Cg3D2ikeXJRfEAGBP9YYp7wZlfUsdMXse38-98nwAwoUfCIcz2CrPVzyfbUbCkAkRkJoilTIfzAfY2iSxjRimYq_D3lhYhPdeNZxMPqjcU3ZHMiRwcstQnMo1inKfB8ueJzPIVLr8ftmViEDhfzhYPenLbEkvSzM-o_AcYPLAKqFXaM1WMVJ_NBwpMiuwomOHaNu24FLtsqRWPqZw-WVDBugGOp5E1nEpEo0Il8Dq4IAA8h5ag93vuie5rjgM29-BkPIozDZI8TDOI6klJhJuRlYKfFnkrjK7Ll8DePgIf7veaKx-3IS2rJ14YRabcDYGbVVgMVYP6XljUsuzobgWcUp78VHP2c4AJAwF3XheGM-36mQtGJBfhd-yefF10NyZhbZ4OFG_WlxxBSZocoNMxOLp5J-W3JuSyNzv7jwefQ0sVyjkByrnvf0EvP-s2VMisdAKk0SrzGEBgyBJAPkpbMAaEHyHjl1oSOUuCK38IqhN3eJOzoqHZOAU6SmJwEAWoTlmzPgQf9XKFRCw0v_wp2H0dVByRCM_8-BNnr4QKuAqHbHE_dfsMW7qP1jbMYK4g-pbsfMYbVd1HjP90vDVcU5LdMaRn6tb3QUN4tP7hUhvrHKaRx-GDSLN5npm7UD3TU74vbVPQ58qShkE5uVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qU1e212cd_QEG-t8f2VCwgrFuAVeXGmecHuAyhgGtYa_7RinljYpMNqf2UtHx44GEYofxI8L004yhiLhzEZE9FqkKuyURauv4Xni7m6k3jfEnbFCTuRcWwch0Nreastdaa_9BDqIi0bcN_wJAnUXM2u6uUmBHg_UwHwSrkoe1VVW2qQxhFR3yCtu-F_hQH1P5WTQKNy4ceGOOsZumD6GcnCfPR27xEKDGTV832SWgS84GaWsGNhFNcvF7kw1L6TU9YVxAPzGrF4JV2OlzYV3TRjjAx5WnVo65whnkMi8XzfgJ3bGyWDgP4Zw4aOLSMd7t2ZfPt7g2aVsy5BomE_52A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=rF_PUfJyimf-q0CBMHTzXxIQSjJBwdPMdtnBgDDz1TOQUVZYfsole7NNTQe45kZ4hK-dXe0K4CibYDIOJ9Aj1vhRFKszDVBNflN_s4e0YT-Hf4VrHg1TeAXXilwA0C7AboFeHs8XzDHIdHpVgYW4ET0tS2p5fc9uwa9F01jJKix2T6bRQQ68ly57_6oBirK7_jbCWnf0_8DhIgx0B56m9DeoW08Ss1Fs0H1cgcnPGTdKpEYvv4xJ_-_9hB2Npqxo9PcyKqDj-0TMrIJrNUOZYmnUsfCFVtSuZoqBdrx4WSWZ8xSMY1gB2cfTe4VBgy_zePNA4mAvEGB2fDNnIXeASw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=rF_PUfJyimf-q0CBMHTzXxIQSjJBwdPMdtnBgDDz1TOQUVZYfsole7NNTQe45kZ4hK-dXe0K4CibYDIOJ9Aj1vhRFKszDVBNflN_s4e0YT-Hf4VrHg1TeAXXilwA0C7AboFeHs8XzDHIdHpVgYW4ET0tS2p5fc9uwa9F01jJKix2T6bRQQ68ly57_6oBirK7_jbCWnf0_8DhIgx0B56m9DeoW08Ss1Fs0H1cgcnPGTdKpEYvv4xJ_-_9hB2Npqxo9PcyKqDj-0TMrIJrNUOZYmnUsfCFVtSuZoqBdrx4WSWZ8xSMY1gB2cfTe4VBgy_zePNA4mAvEGB2fDNnIXeASw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4QHgHCil5rd4sclLYacHIEjcZTRA31fSEd6RN7LVA-9HKipES_Z9ogd1AelRI1HOFiEdu3z4yDw7tjf-NFA3byiJUJqCt2iJqSkBvYw4AFt8dMbu9oOg1DO_ppLYeFExI6FNWH6Mjox2NQtkD14KLYHL0t_Nc42L2B67n7YNfJrpZl_gBCatKVjzfX-EKN_xI53V6xdzB20DrYrfdgTtoTPshCYZ8UHa2JyF6y73vgTwsGxw8tHkX6qqW-g16Vd3X31gRrG0NDqN6Hfjc_9fGSIog9ccdDbgWKM9ytlEYhEaWhq22N3rso1aJ1qOMnhbpG9wL-3G3JmZHvJ8xa7yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDxH9xYAlPxXFikQvxbNpz4Gc3y_eZ21LMqXDBnKdheNLtVGmmsia-w_iWcitRAJKWO2-WzsdMfbXutzpMOZBgFv_-42bxYmKfkeHbl4n4kkrUkmwhIFHL2cgAr717lYXoXYU9oCecpMJV-2L_qjCG_9J5EPnpEA6Eufrjhcp2lFtCtd_kCK8z2oQVo352cVOeTAEr75dYiHv_k2bARzI41QsIfqbiAiFJ4EqgUKXejuViRhtw0OuVH1E9TvCygPCD7SPC_wtsyA60MTeRSdZxUuguW6qpcqIXQ0YwFV4zRmPT0JHoZWBzIicKcDkeCEeFXj0zj28tMPHHfjOwl03A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mkz72Q0hJEM5YYY1hBAW-dqXjWbEQWV4P51QSENt7MQYl9C4mf712FnkbQSglsH-Qdmn9RcmZoN8lD-dmMwWvgUowhy4JEfR27OCccVK9-zD1IuJYcZ45kr58uyTI6xBg-Fo6_PaqhFT6ZMBFHCeBD7QZOWcAvNDwq-6sDqvjSmqngB_QqwyTaUdBJMswRn0A66uJuYEjh2r8wFV6cKD1ankod9WAvtlCFnzncqcuYpkktunzxx-G-_e38Uy6NDAtlFLXtE1suP8Mc3iMe3mt77_u-YTPzfbTLJqHQdF9_XQ03Ptz4oN8Z6AwVnqFw_R5rS38TXVOMFzHBBBI3J5NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=sDUImp91Gp-AIDM2mGjlcYxEUCchgeMa4ElS4kd6c7Tb-fTQ2oIKihWZpXVf9FRkokIiEAIvpoXuR7AROouyRw72RZU1BFSkv0s1kLaYRwF-7XWYflCiKbAgK1vK-GwCOXtGUY-KH1H2hnwFVwxzsbnvwDvhlLHJ98qXAf-C9yyXb5Wso04NpU5mULuJYa_zuXDQFSBr6UnpxEuAgNKzvAqNB-bC_AJzA_GL7MY-toiR84DvLtt0kjhofYCf4qff-Vq2RbdxgPsovuOuE1iQbSUGffZe9BMIAaPz5KZ-rmT4mJ1cAmqSv2rG-nhHU4sf8X59eiYNHknQOdUQNvKlsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=sDUImp91Gp-AIDM2mGjlcYxEUCchgeMa4ElS4kd6c7Tb-fTQ2oIKihWZpXVf9FRkokIiEAIvpoXuR7AROouyRw72RZU1BFSkv0s1kLaYRwF-7XWYflCiKbAgK1vK-GwCOXtGUY-KH1H2hnwFVwxzsbnvwDvhlLHJ98qXAf-C9yyXb5Wso04NpU5mULuJYa_zuXDQFSBr6UnpxEuAgNKzvAqNB-bC_AJzA_GL7MY-toiR84DvLtt0kjhofYCf4qff-Vq2RbdxgPsovuOuE1iQbSUGffZe9BMIAaPz5KZ-rmT4mJ1cAmqSv2rG-nhHU4sf8X59eiYNHknQOdUQNvKlsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gym8gu95PGs1yl0OqYBRThK48UaKLZnoKxw3wi1bUt13P7LbJKozWQA2hB5zDwD9XowxQILA2D62jHGQ3rgMlrhLA8k25hu1HXsdoxUa_ZUnCyDKmz8f0Y3w-3fXb-pwBYn6tJysBNPH89hzp8SdrzrPOHYQxuSmRNM7I3BgnmHpVr0ofxKIT8IBo2j3HUmPmRyOl5VssbbwU2J9bGq5T3xe0RwZiP1pZS619eEOdmwIguQLjmGqX9A-MjR5_QC_7ujrVgf9PNwYhXlTnOzrtuvvXTOBjYVtxHkYlAJMjeleHmIN7Yd81UZgm08pB_sjtWzHWafBbhTPYbrpMtZkEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFARBFLYwJRF_x3NgikfVjj2jYK_odIxWJgo4bMph-ERg4TnageNOVamf6NSNrxCNUF7bErHPLUFUJLj-ktlzCIjGLcAqaan8zlXSlKe5dzULV3qMZr8e57_d25UGmGzGx-0-KhFee-UEFRNVyYywaI7OTO6OX4w08vANrfPAPQnqkvLF0CO_adpsXWMAoCtg8FjwSXQMqFCjYi-wFiU2mooFqxZ4RS48vuNk3IwbJ5YMAK5WvxnHcAOOCia18hcpdPHNA9uqROfccFweocUmM_rEZCQ0Xm2Z_QSWSMhXVSBj_XQh-2bdtnzva7uWy0Km5lAkbJp5SbDaN8bbJWLsvsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFARBFLYwJRF_x3NgikfVjj2jYK_odIxWJgo4bMph-ERg4TnageNOVamf6NSNrxCNUF7bErHPLUFUJLj-ktlzCIjGLcAqaan8zlXSlKe5dzULV3qMZr8e57_d25UGmGzGx-0-KhFee-UEFRNVyYywaI7OTO6OX4w08vANrfPAPQnqkvLF0CO_adpsXWMAoCtg8FjwSXQMqFCjYi-wFiU2mooFqxZ4RS48vuNk3IwbJ5YMAK5WvxnHcAOOCia18hcpdPHNA9uqROfccFweocUmM_rEZCQ0Xm2Z_QSWSMhXVSBj_XQh-2bdtnzva7uWy0Km5lAkbJp5SbDaN8bbJWLsvsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=I5lGfhoAzDmBVM6uBUENtmZqN-z3Lnm1Gxlyfi05-KuOq0qLeroEUqBDaTY7uBur3S34zS-WKuqpUJ_YAwBvEYjcBkvhEpZvqJkxScQKr7ue-OCANC02VEE_0vjRzWLEKJ_iNA8gw6xyGItK3AF2BqlrHiNd80d7--zJwYG8g30oLjiXroAQ90pqzU_bwFor7ejJOSYyQqmdM7AkKqxrTDD5wUknU8T15k02gh7pp95_7GdaYgocwa3LYdcLeOLOznqN4QfcxyvmqVxA8dGj6WF8QR48JXFS9KBXDl-E9m-pLrzbO8cJW48fi6_eq1v07Y21X2CIwG39cJ_htLaVPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=I5lGfhoAzDmBVM6uBUENtmZqN-z3Lnm1Gxlyfi05-KuOq0qLeroEUqBDaTY7uBur3S34zS-WKuqpUJ_YAwBvEYjcBkvhEpZvqJkxScQKr7ue-OCANC02VEE_0vjRzWLEKJ_iNA8gw6xyGItK3AF2BqlrHiNd80d7--zJwYG8g30oLjiXroAQ90pqzU_bwFor7ejJOSYyQqmdM7AkKqxrTDD5wUknU8T15k02gh7pp95_7GdaYgocwa3LYdcLeOLOznqN4QfcxyvmqVxA8dGj6WF8QR48JXFS9KBXDl-E9m-pLrzbO8cJW48fi6_eq1v07Y21X2CIwG39cJ_htLaVPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=sOGELgRmdJcXYBwA7T6CT45xp0ecdhFQ2KKFsXpvk7mZawpeqIkA3tpQlJZIHFtON0v-uVQ8w5xjoy8legu7slt_-3HTSYIe81oCdzESnFee8L24y9qxQD-6RggapvwjKM_nvdLz2AlaaW0Ad7QOJP5F_mQiW9hi5XtZSNIUo-XjogYTKRP7KuKOnc8YQ_4z9midghleDiNAWZRtxDRxJZ1DkMU9ZDr2VvxG-1UmZ9bKT4qYdeT-Fw6QOrWbVQGN3syb-rdVuvpWgeRzv4DcUVjex1u-0uZFs_fSkCAfzXWnQcW_PzZuEmF9mC_hJW4Lkn71joDdG7PTCNYvtPqLF2QlZu8NU-DhNsd4OMysYgOwMtOVX2Iupfc8jVqRR0HgC6gV1dKAMzf2MfGrhQA2qd3HZEEdvCCdUyBEgGg9Pzxiywcz4s-5f6P3yBgP6IysWHX5HRijKrYMDWUCl1KPiaf--s2wo1XoQ6vUe_YIqS_HbTWWZoOJH1JAyd06zKbPvQjTm1Se9FYk1Tqh-yYLhE2L_430pq34RJyywqBn7FJUciidyp4itTpChxxqIw7ux38ezhsJFf2GoE1AP8vcQ1lcoupxu_8aBAN42yGOvC-4BFzRJLU9A2SPkJilwNtEKsrHkSeSj22F_DxGnolj750YpzRGYytOp_kGwUndViw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=sOGELgRmdJcXYBwA7T6CT45xp0ecdhFQ2KKFsXpvk7mZawpeqIkA3tpQlJZIHFtON0v-uVQ8w5xjoy8legu7slt_-3HTSYIe81oCdzESnFee8L24y9qxQD-6RggapvwjKM_nvdLz2AlaaW0Ad7QOJP5F_mQiW9hi5XtZSNIUo-XjogYTKRP7KuKOnc8YQ_4z9midghleDiNAWZRtxDRxJZ1DkMU9ZDr2VvxG-1UmZ9bKT4qYdeT-Fw6QOrWbVQGN3syb-rdVuvpWgeRzv4DcUVjex1u-0uZFs_fSkCAfzXWnQcW_PzZuEmF9mC_hJW4Lkn71joDdG7PTCNYvtPqLF2QlZu8NU-DhNsd4OMysYgOwMtOVX2Iupfc8jVqRR0HgC6gV1dKAMzf2MfGrhQA2qd3HZEEdvCCdUyBEgGg9Pzxiywcz4s-5f6P3yBgP6IysWHX5HRijKrYMDWUCl1KPiaf--s2wo1XoQ6vUe_YIqS_HbTWWZoOJH1JAyd06zKbPvQjTm1Se9FYk1Tqh-yYLhE2L_430pq34RJyywqBn7FJUciidyp4itTpChxxqIw7ux38ezhsJFf2GoE1AP8vcQ1lcoupxu_8aBAN42yGOvC-4BFzRJLU9A2SPkJilwNtEKsrHkSeSj22F_DxGnolj750YpzRGYytOp_kGwUndViw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=dUE4RDYL5hx1oj1cengtXC9IIm5iQhL8HlMsD_Uzh7hSab4KKfWTk8jkM3ePWEMTP7IM2HxioK6BuNbiqxR0OZlOfr_nNToMCiwIcPR1crlFHeglzz1RuM-sGbW8IKm5psyKDYXVLd8NGSpwv5-ltw1imIGtbSikMnzlCdT7u9JVyprBKZG4K6rxdh62OjxHtTbR3wNJMrtJZceaAW0u83rS5R-ei38FQ-sGpMMiKsi5aEOb9Bg7zzpiltuJ5GHHHvN6BaOmLm3nQhr-tQ8XpE1D5MFR3_iARACAqIxitdUavfHZFcpz4VIMygMfsL8TKR78etERwf20TmC6g-SWHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=dUE4RDYL5hx1oj1cengtXC9IIm5iQhL8HlMsD_Uzh7hSab4KKfWTk8jkM3ePWEMTP7IM2HxioK6BuNbiqxR0OZlOfr_nNToMCiwIcPR1crlFHeglzz1RuM-sGbW8IKm5psyKDYXVLd8NGSpwv5-ltw1imIGtbSikMnzlCdT7u9JVyprBKZG4K6rxdh62OjxHtTbR3wNJMrtJZceaAW0u83rS5R-ei38FQ-sGpMMiKsi5aEOb9Bg7zzpiltuJ5GHHHvN6BaOmLm3nQhr-tQ8XpE1D5MFR3_iARACAqIxitdUavfHZFcpz4VIMygMfsL8TKR78etERwf20TmC6g-SWHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQ-cHzLE1BAmJhVW539WUlGraHL4Q5Ne8NHVc1vybKZKjlQ83T3yHmUc5FQ6Wcv0qSc2HtO2r29y9aBtIRaG6pqK9SveRQRRk10Fg7iYAReYSnDpRizHkMCzpTmAwRdkpdYKWQ46VE4-U1oCmkaSXSuk7n5TfTfQHA7fOZAI4x4B_DXE2cFjj5GU1zUjPzX7O8Je-J3XfxoVVKpWAEFgTgwE70UYXgQIQjnDcmfSO7Wb35kEHLT35_9_c-PIvuNIIKbgRdA1IVHNh2T6hGjSnG7Qt6NhgBtr88w9KpJZN4aAqJduqYCQ_Yxf__CBV_qCkHzbN2G_Dwtr3bLkKTOulQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=pOAogeE9Wd-vUJWPfFU2T2cF0_tbDIUIbT3UFSBxIRHqGBAH-admnHbJAolRHDjnnEbH-ewNE2UW6Zgt3OUEwV6AG3BpzOGgycfNaEATt76LKG7iFYIfFBmy57ULG5K3D-Fea5Px4GelYpRAuL0fJjpQlnNl92J9kAVlIsnuP6HWYX8Sb79KZJ9P_AXBJQZRioS98G-xhIarK50Fgs3jqUiRkS8dQ3Ay66oIzjHJnvcsfmnBrsk1QEFBkWV0GnqpRE1JZ1hUilQx5G2mT1-BrTcAHv2tPQwNblEJ-dpEq_rSPa7gs7tdx4wgsa75nXdYrQk0FYNl5zehkdIJo-r6Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=pOAogeE9Wd-vUJWPfFU2T2cF0_tbDIUIbT3UFSBxIRHqGBAH-admnHbJAolRHDjnnEbH-ewNE2UW6Zgt3OUEwV6AG3BpzOGgycfNaEATt76LKG7iFYIfFBmy57ULG5K3D-Fea5Px4GelYpRAuL0fJjpQlnNl92J9kAVlIsnuP6HWYX8Sb79KZJ9P_AXBJQZRioS98G-xhIarK50Fgs3jqUiRkS8dQ3Ay66oIzjHJnvcsfmnBrsk1QEFBkWV0GnqpRE1JZ1hUilQx5G2mT1-BrTcAHv2tPQwNblEJ-dpEq_rSPa7gs7tdx4wgsa75nXdYrQk0FYNl5zehkdIJo-r6Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=dYkpUpRz1gsumc6tQmsiSeTDXvdQJgHhxS_eb1Cfxu4DQ38tp-747PAmA3i4daFNAVpItjYsRB6dVFZt-avMRdasmL2C7rca8qeIiGrQUSVNHlHAp1oMOzyYZgeUzOx1GXyozGcZWNk7sQ2oLxvrTl6bf1wKPewPZnLG1rdfvO6zFyywyLX3dKzPj5khpuN23yf7lUc8A-lu34wYyP3DvV2PuzPjNGX05fUl8QMNLa-s6bc9qv3yNThmqeA2F9z5DyVHNnc-vcYc2H5WhtSdaatPiI-aV1oez2pRQ1Cg5TyfuPluZ1dyVZSUYTqbvm9EQa9CGE2_Q2NThG9ZOnQt3DLYCmM2lINT-lEu5Jh2s4k1VjFk_bB9_EXAyZJUawoL51kPFhzue3e5Q1rmCKKO1r89ZPVAQgPyHkxoHLNnlrIIGLOPElOKceaxNuElRUjbbA6QymDDSXj8vz6ARyeO0veDw_6D_WtQQcUVpj8Xjqh8DiNxAZuUFVuHebvuF8ugK_cKhVOkUyYT0U6BsCCI0awpvdDewSKsyNl7wB3gSFGoYEoSJ_VdOZgEjbbVlm1_h48kKQMhzJBHOC5N71B-ak4UGIiR1V-OopPBmGoZ_-nUJ_23iPlrqS1NlWGfebsH1zoaflREYGK3hRxznSgRdYD40_KEt5lV171Xl5OmZeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=dYkpUpRz1gsumc6tQmsiSeTDXvdQJgHhxS_eb1Cfxu4DQ38tp-747PAmA3i4daFNAVpItjYsRB6dVFZt-avMRdasmL2C7rca8qeIiGrQUSVNHlHAp1oMOzyYZgeUzOx1GXyozGcZWNk7sQ2oLxvrTl6bf1wKPewPZnLG1rdfvO6zFyywyLX3dKzPj5khpuN23yf7lUc8A-lu34wYyP3DvV2PuzPjNGX05fUl8QMNLa-s6bc9qv3yNThmqeA2F9z5DyVHNnc-vcYc2H5WhtSdaatPiI-aV1oez2pRQ1Cg5TyfuPluZ1dyVZSUYTqbvm9EQa9CGE2_Q2NThG9ZOnQt3DLYCmM2lINT-lEu5Jh2s4k1VjFk_bB9_EXAyZJUawoL51kPFhzue3e5Q1rmCKKO1r89ZPVAQgPyHkxoHLNnlrIIGLOPElOKceaxNuElRUjbbA6QymDDSXj8vz6ARyeO0veDw_6D_WtQQcUVpj8Xjqh8DiNxAZuUFVuHebvuF8ugK_cKhVOkUyYT0U6BsCCI0awpvdDewSKsyNl7wB3gSFGoYEoSJ_VdOZgEjbbVlm1_h48kKQMhzJBHOC5N71B-ak4UGIiR1V-OopPBmGoZ_-nUJ_23iPlrqS1NlWGfebsH1zoaflREYGK3hRxznSgRdYD40_KEt5lV171Xl5OmZeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAid1YGerpVC0TBx50LM4tV5FLYEXut6LpZ0l8P6lNnNWoOHlxaKYf8rnZbY77rqi8NtW3Gwb7mURsNjKo_W9IE4rELsR-oHr9PrDuK1M6kmNdCkaaRS1HRmIqlc_oVwdmoatOi63p69Pe9ZGJzhdooOxA9Bw-PMnGXaiiAj-FhhZ3qxudK_w7ZVzIjNIS2Nmm4kqUSFnQv8gS8i4ZwiwaPbwBn7wVhN0LSX8JRSr3fwy3WguQceHDwutGTuADM-eOkzSA5OIYfTrR78av2-ljQWNgd-JLO0cBYAVXFDsMYmJUGos7X8wUMiTBablHNj-SVhqo77p6MVcSEf7iKPMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=j_6V856SWcm16mCL1BdFLxF__spkQIRwJy_os_wXdg4R59DbokAfPOc9-XFflk3nKsjxJbeBudVYW-2uuRVRkXCdlTPnRk1SlourdTLNjwiTDjFCLvC9jYyNX9sRg2PgOk9FabT8gPdmWbbBq6GRaURwCzP0AKUodr1ibn9P8eQHJDYPTzvhG4RSAGBfZD_eWFfQXivPF5RlTckpm-4Sm8xFZzEkU7K-JU1WQgIZK-sbaM-ju4sMQ_1Hdk3FGaBdcjLaFhBeQOcIpHn2wNywbLv272zg4n_Ions8b7lj1VdQTuClmJdleuGu6_rNe6I9z9ifZsDQQjhTou5tL9KCkpM0YsqAGzTHmCTLXx1S6_IYjrdHued3Ftt6kAycYJb4sxfDwjy7-nb7-zGmRrw4JF45KAuvhGo89FfyDFQ69vjUbYjcAUkZmGr3D-pRoexyyu_vhSQBT1V-JHLGV9s9F065lcFEpX7YI92bqMBiYof3Wm5wDmOpM5Bd1A9UpgrBm0O445uH2OgaWuAH1g9MbbPAaY44yIgwp3tTuSP3lhCQK44EmCFWsfV8tBS2sMufEmvbkgeKxLDaCAEwKfIiKZfFxdQIdeqsrrAT5hhGaXwfc12uJabndTKZM6qzrJPa2RVbQiCT2kW-FofFxIrrZqOernN9IcBAEILKdTt3sKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=j_6V856SWcm16mCL1BdFLxF__spkQIRwJy_os_wXdg4R59DbokAfPOc9-XFflk3nKsjxJbeBudVYW-2uuRVRkXCdlTPnRk1SlourdTLNjwiTDjFCLvC9jYyNX9sRg2PgOk9FabT8gPdmWbbBq6GRaURwCzP0AKUodr1ibn9P8eQHJDYPTzvhG4RSAGBfZD_eWFfQXivPF5RlTckpm-4Sm8xFZzEkU7K-JU1WQgIZK-sbaM-ju4sMQ_1Hdk3FGaBdcjLaFhBeQOcIpHn2wNywbLv272zg4n_Ions8b7lj1VdQTuClmJdleuGu6_rNe6I9z9ifZsDQQjhTou5tL9KCkpM0YsqAGzTHmCTLXx1S6_IYjrdHued3Ftt6kAycYJb4sxfDwjy7-nb7-zGmRrw4JF45KAuvhGo89FfyDFQ69vjUbYjcAUkZmGr3D-pRoexyyu_vhSQBT1V-JHLGV9s9F065lcFEpX7YI92bqMBiYof3Wm5wDmOpM5Bd1A9UpgrBm0O445uH2OgaWuAH1g9MbbPAaY44yIgwp3tTuSP3lhCQK44EmCFWsfV8tBS2sMufEmvbkgeKxLDaCAEwKfIiKZfFxdQIdeqsrrAT5hhGaXwfc12uJabndTKZM6qzrJPa2RVbQiCT2kW-FofFxIrrZqOernN9IcBAEILKdTt3sKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=ja_oGIKGGBGWw02PLV45QBGOIl1hm08wBCy-_m97sTYxM10f-rvdUi7AxuOlid4EzbmRBtcpJBXWuUXnt_uKILQN6pYuwMYhqIjG-dtmdwRM9x8Lza2z46HNBVMpzRJwtXrU0TIx3vRdOfZo-12PHHvYhfZNrWnpEijM59EokAf1ExBZ479gX9j1Jc1tRvgI9kG6g15vRdYTkL8yZu9JNAdKnWH6K-icvnjEJ8A6rpT0xGiPSck86UtYJgd-SnpW184RPJRkiq6zYUgOxJDehJCggEXw57sbiodru8NzfY4waD3gChFqEBirzioqcWQ0nRX_16BKpPEChSxDohPyc0UKbnuxqQwNOBg1ue-INQLbls51Buus-UfrO-ZXWDpN1Wfu2QR-KNvC4TWcVjAjbncv-xGdxRLNWgl8o3t0x_sC_8t107wZM4hxHNMdh1B9FtSlvI9uG6EoWPyX72A1sCEi4REgE9spDSYQwLcQdcWa6h6DvR0-BHRCmhnP0HPwvxMFRTzGo0xRNdFLynv7dcNYn7ssdmXMlVE9ZZ9msTGamVc15NwIUy0iwOu0rhnp2XB6j6tLvmYrPlXnrv-vNC1BW0KqBhlnrMyc8ntbSw8Z0tffpXToE0bHQGiiQZKrMQLb92735rWJnLGxfZwVsLPwRHyvd4DmR69kNsx5jWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=ja_oGIKGGBGWw02PLV45QBGOIl1hm08wBCy-_m97sTYxM10f-rvdUi7AxuOlid4EzbmRBtcpJBXWuUXnt_uKILQN6pYuwMYhqIjG-dtmdwRM9x8Lza2z46HNBVMpzRJwtXrU0TIx3vRdOfZo-12PHHvYhfZNrWnpEijM59EokAf1ExBZ479gX9j1Jc1tRvgI9kG6g15vRdYTkL8yZu9JNAdKnWH6K-icvnjEJ8A6rpT0xGiPSck86UtYJgd-SnpW184RPJRkiq6zYUgOxJDehJCggEXw57sbiodru8NzfY4waD3gChFqEBirzioqcWQ0nRX_16BKpPEChSxDohPyc0UKbnuxqQwNOBg1ue-INQLbls51Buus-UfrO-ZXWDpN1Wfu2QR-KNvC4TWcVjAjbncv-xGdxRLNWgl8o3t0x_sC_8t107wZM4hxHNMdh1B9FtSlvI9uG6EoWPyX72A1sCEi4REgE9spDSYQwLcQdcWa6h6DvR0-BHRCmhnP0HPwvxMFRTzGo0xRNdFLynv7dcNYn7ssdmXMlVE9ZZ9msTGamVc15NwIUy0iwOu0rhnp2XB6j6tLvmYrPlXnrv-vNC1BW0KqBhlnrMyc8ntbSw8Z0tffpXToE0bHQGiiQZKrMQLb92735rWJnLGxfZwVsLPwRHyvd4DmR69kNsx5jWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=btDYeA301ZTvxVFxRWB4IT8NTJ7-VlwPu_NruIDV5uLoeQPhgvsEIZT5KPAgi7BZVT2E3-ZFraxRuGTXs9DCmVKy4PQjG6SpGfCqyccCknCBd9sbi06oFgPDkPO5Vf0O02TMzHv5Rk3urd3IH9EoQ8lpxaeCf-Wjp0wJLdL7obo-eqq4DcAoIyv09YgBgZXySR3kt8y2zOCBC8imSK6ibFo87GKZpg1kV9bl1rQiohYJr2RupC3gV6FLFyQJvbwIVLErM4R1dfLHsloDKFUNj9hyDEhjs-XHRckPg42kCi1PNLLCGZe4Po_dBR0KBl87TzDdGElRtKTN5fcPEy7Nog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=btDYeA301ZTvxVFxRWB4IT8NTJ7-VlwPu_NruIDV5uLoeQPhgvsEIZT5KPAgi7BZVT2E3-ZFraxRuGTXs9DCmVKy4PQjG6SpGfCqyccCknCBd9sbi06oFgPDkPO5Vf0O02TMzHv5Rk3urd3IH9EoQ8lpxaeCf-Wjp0wJLdL7obo-eqq4DcAoIyv09YgBgZXySR3kt8y2zOCBC8imSK6ibFo87GKZpg1kV9bl1rQiohYJr2RupC3gV6FLFyQJvbwIVLErM4R1dfLHsloDKFUNj9hyDEhjs-XHRckPg42kCi1PNLLCGZe4Po_dBR0KBl87TzDdGElRtKTN5fcPEy7Nog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=GWjzms9bJunS9nsUTdUOtxcCo7zAd9ga4VTBpNaHl5E9IEQABLL-VE7st_iIdaiH6hkzrLh9DoDBqsgOcIKWw8qTqFEwfOgUfj5wlmRxq0JsnRLyj0kSKivoEh7HfeSGVYuAfVxrVYV4QTKqe84HjkfZEuvri8N4mY0Z_StcnQgSklLAgBVaEzPXEXRoOxvR5tuiM_MbEof8LlJh8tVapkswYk3QwTC6qMqwINNQforKzuHAhlvi9XEM6UcnBQeOGOUzqPRx7Rhkc00WwZO99sAccG65Jh0_HEd01oXl7YzcGzHgTppokXlJ4Dctk-nSoPqDcRfmUWFSakyZebtjxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=GWjzms9bJunS9nsUTdUOtxcCo7zAd9ga4VTBpNaHl5E9IEQABLL-VE7st_iIdaiH6hkzrLh9DoDBqsgOcIKWw8qTqFEwfOgUfj5wlmRxq0JsnRLyj0kSKivoEh7HfeSGVYuAfVxrVYV4QTKqe84HjkfZEuvri8N4mY0Z_StcnQgSklLAgBVaEzPXEXRoOxvR5tuiM_MbEof8LlJh8tVapkswYk3QwTC6qMqwINNQforKzuHAhlvi9XEM6UcnBQeOGOUzqPRx7Rhkc00WwZO99sAccG65Jh0_HEd01oXl7YzcGzHgTppokXlJ4Dctk-nSoPqDcRfmUWFSakyZebtjxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=A_mvZAerucQP4zumQ8-HhyYZpZyQRbTuf4qjRcIrn8is3it2aqGJ3j1GL2k1eptgYOMcgNUm4yb_JQRrA9l1wZhxb_KEBjlQqagEcKtU8PK0NfKWQU-gdL8oR9gqKu8nXRkpONDEqc3lv70Mzl6ZMjXjwUFcG0ePlqdt0dwnJfu0EE7Z0tN8wixQGXi7ctplceW12hsliCd8jgU3chdh5rduOoQ4kB47TZyoc75oL3r_mC0bn2MoambJkJW6ourVGtlNXR9jtLoxmL_cGm-CX3kaRaA8hRk_y4XFCEqvzT_ver1unKLCz6PuAa3vIgATSEWWXrHOdjHHs-9r_6mDrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=A_mvZAerucQP4zumQ8-HhyYZpZyQRbTuf4qjRcIrn8is3it2aqGJ3j1GL2k1eptgYOMcgNUm4yb_JQRrA9l1wZhxb_KEBjlQqagEcKtU8PK0NfKWQU-gdL8oR9gqKu8nXRkpONDEqc3lv70Mzl6ZMjXjwUFcG0ePlqdt0dwnJfu0EE7Z0tN8wixQGXi7ctplceW12hsliCd8jgU3chdh5rduOoQ4kB47TZyoc75oL3r_mC0bn2MoambJkJW6ourVGtlNXR9jtLoxmL_cGm-CX3kaRaA8hRk_y4XFCEqvzT_ver1unKLCz6PuAa3vIgATSEWWXrHOdjHHs-9r_6mDrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=tKF8pZC7KuNFFXjnICOTDRpMYAHIO2cRxymtuZp4ewW_6eORbVhUOYtpiQe2cluo3gA7rsGF1chm-3LHjs8UtVYEuz_-6zhgX5ZCLZAjHHhFZfLqcxVdcVXrO7wrWqI84pVPNWrRiOsb4Xa_wtukGelwmIiCsHiBVlB29ltKYq2gkXMWco1rCnLXQYlrCLAa3cKi9UYK9JyHOZXWOghYLKaqGGVy2U27NABnfgrtTYsFPV1dCe_eFOD42h41KXjLlQHUUabnl7js8wVBGZqrHlStSc0p4Ue3nqXlXhXUHVtcqXy1o_VgZyzM2GJsgZ36_z82xUZzPokszMgrHZOp_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=tKF8pZC7KuNFFXjnICOTDRpMYAHIO2cRxymtuZp4ewW_6eORbVhUOYtpiQe2cluo3gA7rsGF1chm-3LHjs8UtVYEuz_-6zhgX5ZCLZAjHHhFZfLqcxVdcVXrO7wrWqI84pVPNWrRiOsb4Xa_wtukGelwmIiCsHiBVlB29ltKYq2gkXMWco1rCnLXQYlrCLAa3cKi9UYK9JyHOZXWOghYLKaqGGVy2U27NABnfgrtTYsFPV1dCe_eFOD42h41KXjLlQHUUabnl7js8wVBGZqrHlStSc0p4Ue3nqXlXhXUHVtcqXy1o_VgZyzM2GJsgZ36_z82xUZzPokszMgrHZOp_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=X_M3w01WRGM-N2kdnx1_PDQ_F8PmCOqxFEMl-wuqG0nZ2MV5hRlLqxgMIxYSeZl0M7VXfXeHGWYoCZkAgfJgdcjm5MozHOhKa4jdFalrE6Yg_oKKA4Gy4oy9pWaveoh2RziSLQRt7dPKkg15oeyCTzJJtYIqGVMjV-7s-r6TMmPxt74ONDZz9H-fLakU-2iU_oUTz-XUEC4DHIg59I1L_4yluHgNumrGqrqr6Ai_MKa-fTe6-vwkEMqmmIkKH6ORrtrIeMf1jmoKLXp_pgwB3j52qT8DZiJBHwCkbEgFhZvAx9nqhb0RuCU1YQlGuMdfa9vbpJffRNh_FLNy8rAo9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=X_M3w01WRGM-N2kdnx1_PDQ_F8PmCOqxFEMl-wuqG0nZ2MV5hRlLqxgMIxYSeZl0M7VXfXeHGWYoCZkAgfJgdcjm5MozHOhKa4jdFalrE6Yg_oKKA4Gy4oy9pWaveoh2RziSLQRt7dPKkg15oeyCTzJJtYIqGVMjV-7s-r6TMmPxt74ONDZz9H-fLakU-2iU_oUTz-XUEC4DHIg59I1L_4yluHgNumrGqrqr6Ai_MKa-fTe6-vwkEMqmmIkKH6ORrtrIeMf1jmoKLXp_pgwB3j52qT8DZiJBHwCkbEgFhZvAx9nqhb0RuCU1YQlGuMdfa9vbpJffRNh_FLNy8rAo9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=EQzVZi1IrNq3Ys_tmOCGRwaRgA7CDgPYYi67uIKxx99fTlqCEOVCam0Ihnv6K2ZDzPFBp6e9tZ5FyNYRXMGlrUhBLYu4KNQY_FUHlAHIaemwrkSMIEQaE312SwN4tgxy4oj6m71bD5WkhLdZymx4qUqRziSr6Ss94zIoFG_tsEtUbS6ESCOemlImiVG_eIGrRqlj1a5rcf18Q-Rj2_cAHTBvUXif4tXXSqC0llR2YXYmObzgGzEHoV34XyZp62M5pRwRv2IxPMXoeebSMMBuvplTNMAuS26xo5lXtoRhTuc52cNGIWfFKNjD_A1LYWEbDLz-pJjUDQ5lJDIbMUmO-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=EQzVZi1IrNq3Ys_tmOCGRwaRgA7CDgPYYi67uIKxx99fTlqCEOVCam0Ihnv6K2ZDzPFBp6e9tZ5FyNYRXMGlrUhBLYu4KNQY_FUHlAHIaemwrkSMIEQaE312SwN4tgxy4oj6m71bD5WkhLdZymx4qUqRziSr6Ss94zIoFG_tsEtUbS6ESCOemlImiVG_eIGrRqlj1a5rcf18Q-Rj2_cAHTBvUXif4tXXSqC0llR2YXYmObzgGzEHoV34XyZp62M5pRwRv2IxPMXoeebSMMBuvplTNMAuS26xo5lXtoRhTuc52cNGIWfFKNjD_A1LYWEbDLz-pJjUDQ5lJDIbMUmO-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Dlo4qh7Tpmq4WfNxQZgZ8uQb1t0JPNZ0GXayGtLiLwzEI_9nO49VQlUerxFXOE7i4k6-AFCeLbXLI595sTXYzV9kPQl8r_QfYs56Kw2kJP1Jokt4BO8yDEaPR2Z8G7tQYzQ6yGcNOujAkPsUIkS--Uc8olEDuLPIRHbP7_Zh-nptqsi3DNpPcFKWqYZy2NV5ZB_tPt7-41aFNnIs1Io9bxHX7e8q1k2EAQifOMeIvZCeTxQqY-T7WpFZPQdeEDmxHAG91F1w3xotyHtek_v3yIfXH0X4-ibMiNfBUmWGyrTT6XB_7RPrdxZPpb5S7pnlkSl7-9ceBMCcP8PhgHTgCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Dlo4qh7Tpmq4WfNxQZgZ8uQb1t0JPNZ0GXayGtLiLwzEI_9nO49VQlUerxFXOE7i4k6-AFCeLbXLI595sTXYzV9kPQl8r_QfYs56Kw2kJP1Jokt4BO8yDEaPR2Z8G7tQYzQ6yGcNOujAkPsUIkS--Uc8olEDuLPIRHbP7_Zh-nptqsi3DNpPcFKWqYZy2NV5ZB_tPt7-41aFNnIs1Io9bxHX7e8q1k2EAQifOMeIvZCeTxQqY-T7WpFZPQdeEDmxHAG91F1w3xotyHtek_v3yIfXH0X4-ibMiNfBUmWGyrTT6XB_7RPrdxZPpb5S7pnlkSl7-9ceBMCcP8PhgHTgCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tk9axT8T8rOrQ2w2Ju1GIIvNCA2mcbP6jNDXIy7FMAyz3dwq4geCn29fMyUfAvEy0MZ7ODhZnQYu4f393fIWEWLPk2xjgeHUI4W3NiDyycWUgHp_4a52GoHaDRN_fwMb7k5HE67JdVLUXMe2Qxace13Up8fu15nrtxqToZj9BkACTK3oZsQFR-YDmePlV251msXGqOCjsL63qmB5jLyjTygEUkvRt1lPGtxkdPvqvByYboH9TQBJKQFrwEnvGB7zdBLdw8G-J142Ip3-JyKlkLD1Dg8gK_Us5WICUtSJiWQ3ByzWk6iGERPen65B2TkUkNUQAUqv3uAcJ5Gf5jGJuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=K4eDYrvCmqPZayt7TAGVhy3uq6T8TaCwqpJ2_si5xS_-8iCju2OTMTS-7CZExkkF3NbpKd-ksbAkglWUe9zQDTg-uXu17BbIefyRyhYtXB5dXNORS8sFZucO2Rn2ZfQBpUKuI0_AxCzCINdxdRfxjqxQje5S51T-PMiBWy5IEhBnP-F5x83mGpsVBpqm-wNUtRf6rjVlX7OTVTQhpJ43WV1BGsErbD34XUUw2zmCiSKSAkHNBGFZpjftJdeLvOjlNz_J8vjoj-qVHWXcDrlNTkJ3sUQO-5Tn8lNIWLCWhqdZqoEvcb1hJSM9dxTCmPHRxS-Dqhd8Mu6zKpiOsJTKxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=K4eDYrvCmqPZayt7TAGVhy3uq6T8TaCwqpJ2_si5xS_-8iCju2OTMTS-7CZExkkF3NbpKd-ksbAkglWUe9zQDTg-uXu17BbIefyRyhYtXB5dXNORS8sFZucO2Rn2ZfQBpUKuI0_AxCzCINdxdRfxjqxQje5S51T-PMiBWy5IEhBnP-F5x83mGpsVBpqm-wNUtRf6rjVlX7OTVTQhpJ43WV1BGsErbD34XUUw2zmCiSKSAkHNBGFZpjftJdeLvOjlNz_J8vjoj-qVHWXcDrlNTkJ3sUQO-5Tn8lNIWLCWhqdZqoEvcb1hJSM9dxTCmPHRxS-Dqhd8Mu6zKpiOsJTKxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=Bi_ibeRwfITAmpFhF9YkeF0a7HRlIFN_z1NfgVOZWQurIXSlGdoXJI9GTX0dQknG5by0oIKPDRu5o-sXjqtRxz-guTJEOzbapl-tdcyD4me7dFDGKM9cqSJmermiW1r9_ALZ7x9cgVDLTRx3M7dCQ-CTSARJD0k4Wo4zNkwa-O0UoTSYsS5pvACLUCfjhJbwdtKuadLcEYeShn7tmgSJHhS7S-1jbI9Ynm9PrX4mnQ46IxFbiaeJzVVLEi6hAesKEgQVrWZMXIUCSA-yXRRBy2IZWu7rVNTrUK0QvBO-o90PlRexy_QbhcVCyfwodmAqjZrV5dHhFI8LiKDGIGj3Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=Bi_ibeRwfITAmpFhF9YkeF0a7HRlIFN_z1NfgVOZWQurIXSlGdoXJI9GTX0dQknG5by0oIKPDRu5o-sXjqtRxz-guTJEOzbapl-tdcyD4me7dFDGKM9cqSJmermiW1r9_ALZ7x9cgVDLTRx3M7dCQ-CTSARJD0k4Wo4zNkwa-O0UoTSYsS5pvACLUCfjhJbwdtKuadLcEYeShn7tmgSJHhS7S-1jbI9Ynm9PrX4mnQ46IxFbiaeJzVVLEi6hAesKEgQVrWZMXIUCSA-yXRRBy2IZWu7rVNTrUK0QvBO-o90PlRexy_QbhcVCyfwodmAqjZrV5dHhFI8LiKDGIGj3Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=mCQz2Vt2iRvjgRS4JEW7osO0ue-Tw-a_nJVsWpOWYpMmxfJJW5KzQXIe_O0h9-4SDhbL5Ebf6nH_Avckg6GQ7L9xZMYjWRU2b4274rHfjIndoDb0P0-inwJ5luK4-njJqTwtCYWmcqv0EKHSqmccXzFTdg3wdMKkZW3HjCd-D3i06CRogevbm4s1tTfY5EE8ONjU_GT1fvJu42yjnLlORl4xExhxBDf6uuvs3dLrI2TaJ-3tt-8JdshibsIHVW1Je2FV1pLOSQvY9_LxfUQJpPmuxbs4cUBeyLaNa32zewQTMJluMDxiMQ9z4vsoctqsmg9XATiQKqcH0p_ft2Auhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=mCQz2Vt2iRvjgRS4JEW7osO0ue-Tw-a_nJVsWpOWYpMmxfJJW5KzQXIe_O0h9-4SDhbL5Ebf6nH_Avckg6GQ7L9xZMYjWRU2b4274rHfjIndoDb0P0-inwJ5luK4-njJqTwtCYWmcqv0EKHSqmccXzFTdg3wdMKkZW3HjCd-D3i06CRogevbm4s1tTfY5EE8ONjU_GT1fvJu42yjnLlORl4xExhxBDf6uuvs3dLrI2TaJ-3tt-8JdshibsIHVW1Je2FV1pLOSQvY9_LxfUQJpPmuxbs4cUBeyLaNa32zewQTMJluMDxiMQ9z4vsoctqsmg9XATiQKqcH0p_ft2Auhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=VVdlojF-qlynKYZMxRvkk0mLYB0YLWl8FJP02rsFMKUpm_HJ7bTDErqZBNkQRpMPo0_jWj-I_hos39s2jbDzk-n30euGipr-1MaXCmMn4aYP8gAsBBnmhgoe-hVBvoDfQfFTlZy7JmmcbrXxoZUg0A-zyyimSecweXSOjFSI7XyKN3qp_PQx42O2BQmlmTtpDhkTDXwyG5NpGgEDTYzjUVigSCysnTapYvr8oQfGEQRw-lTwm4UYUzSV10Zwb4wBZurZW5tq5yuHoAqTuNpcuJ3r7b8Y4Uf0tPF0alD6mlLX0YzcjaNyMnKmR3a1Bk2s4rzigmBp02AQlg7rAe01OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=VVdlojF-qlynKYZMxRvkk0mLYB0YLWl8FJP02rsFMKUpm_HJ7bTDErqZBNkQRpMPo0_jWj-I_hos39s2jbDzk-n30euGipr-1MaXCmMn4aYP8gAsBBnmhgoe-hVBvoDfQfFTlZy7JmmcbrXxoZUg0A-zyyimSecweXSOjFSI7XyKN3qp_PQx42O2BQmlmTtpDhkTDXwyG5NpGgEDTYzjUVigSCysnTapYvr8oQfGEQRw-lTwm4UYUzSV10Zwb4wBZurZW5tq5yuHoAqTuNpcuJ3r7b8Y4Uf0tPF0alD6mlLX0YzcjaNyMnKmR3a1Bk2s4rzigmBp02AQlg7rAe01OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwO1J9Za4gAGJw7sb2UPqkl40z4CqMTQT1-mOAMnFzvrjDRdYizmxShdxZkM7zF4coCyKF_XKKjXJjjkNBfgNovNbORNrUk__bbx58n1ixOfhalmbhv93-sHnnzRL6FqqKbndNs3fmb-S3tphAEuVT-VljiZDhRvLJWGYVy4Mb8Xk_Bjfp3TOp8vX-IgFL6KlaLfDAgpGxHWby2lNmTj9ffyqILPZT9c4fjCn9pRFOncq5FtwhzKhsvhfOLGFsDaobfgew5l9ei4PSaYoVQJNtlrR9-wwuNNNFO-yP921yCXFlgwqSR8r9itixE2ADMzI0aKCzuSoaF1C9CqOb4IPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=qqFVRgDSw6xvEED7lA4tdTz_J7nxMHrK3sZQ9-rFBhWGt21brFyg1NoBRc2cHnNFrCDyLfeAXXLvNoIdREDFbCPoxiPC8Kc9ROFGvHFc817VYIqBlM2pzr-3l7FxfnjcXFehq3liPZUIs79hzxabdrfy1QMrMVbOn4Vm-I7RrbJok8l4vIcaMKYW7iFPU9WyfxCdiBFEDHfIhFq-6fRJv4mvr5rNoZh1NY3gs2TJSbQgRExufQ9EqMCXshpJsyD31WXhP51bjk6CoGMkCPLqaLED3Vmz1kH6oSUqIcKz_EKdvSe2ZnAj3HMMMeaCdDfnWqw6-JKY25EVW1NuF8A_H4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=qqFVRgDSw6xvEED7lA4tdTz_J7nxMHrK3sZQ9-rFBhWGt21brFyg1NoBRc2cHnNFrCDyLfeAXXLvNoIdREDFbCPoxiPC8Kc9ROFGvHFc817VYIqBlM2pzr-3l7FxfnjcXFehq3liPZUIs79hzxabdrfy1QMrMVbOn4Vm-I7RrbJok8l4vIcaMKYW7iFPU9WyfxCdiBFEDHfIhFq-6fRJv4mvr5rNoZh1NY3gs2TJSbQgRExufQ9EqMCXshpJsyD31WXhP51bjk6CoGMkCPLqaLED3Vmz1kH6oSUqIcKz_EKdvSe2ZnAj3HMMMeaCdDfnWqw6-JKY25EVW1NuF8A_H4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=DnahnhTAv2svzUwfeqy7I8RFjdBnzOG_dn3CPrXJBBREHUoq06Isezft_Kqu4_C-I4L7vffve2WOXF5hGOcaea8PmM0v5F_js30ZYP3ZP3vQmb2V8YprDU3QB8CyKG8Eup-aVVxpyRWCWAPCjiuik_nE_JlZEQ1OWFMg7J2FYYPRBVBtwSrhpwQgivcYS1EK7ayNsAQqe3ImgKDNYUxpKeyIb9yFdo42X5JRcYvEZrePV9nqZodbof9EVDTJW9wi1MGJL8Fu-4iSPJcD9iITg8FDpWr2ZIZN-e5Mzaz4KqMi8XQguBRti9JBX3UyDilRhiKvuWPo0p3luIZU17mkmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=DnahnhTAv2svzUwfeqy7I8RFjdBnzOG_dn3CPrXJBBREHUoq06Isezft_Kqu4_C-I4L7vffve2WOXF5hGOcaea8PmM0v5F_js30ZYP3ZP3vQmb2V8YprDU3QB8CyKG8Eup-aVVxpyRWCWAPCjiuik_nE_JlZEQ1OWFMg7J2FYYPRBVBtwSrhpwQgivcYS1EK7ayNsAQqe3ImgKDNYUxpKeyIb9yFdo42X5JRcYvEZrePV9nqZodbof9EVDTJW9wi1MGJL8Fu-4iSPJcD9iITg8FDpWr2ZIZN-e5Mzaz4KqMi8XQguBRti9JBX3UyDilRhiKvuWPo0p3luIZU17mkmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uOl0YP-JBgoH5HBmlsbbB21XphCXinDhx-rmq98n_LCGcw72aehcAHWesI5Ej4JjCGVS_U5wPC-Nti07IsPxKiiJEdHv45FrMlcxEgp6trwkHBQy61kw3chTvOm_bOX7cPjBPYbBaP28hywc5BTNxnc8l96UjXftIP9-ROUxQqy13DJTm5C_6RF_wxJGc0FCf5yef40O7VYGR_srTOQTuo-nYbb3YH6Gvm7Aj_wDY6f1hhQA-R8a3WJqsTy6E9gwKZB7oyKECyAYmKL2QvTO6L-g4YEnlZfDJp4Q-Y-kM0DF7jZSh7Hb0hiH_qXrJsAZTU9cIo9DzqP2tp0rB2DdSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kwmu2UkS2-pPf4eD04cjcnR371Xt_fSkCp39PtxjOhhJuCXMEnPofFcKpiDNEtBiGmXFxSUEwjdkGkQ8EmtQgj_KRUrwzZrq8LYjgV_9xm-JLAIvKnDULO9Ex3odnJKUt9sKoSB2Y1bP5sz7ePUgWsy13RZSt9SDNY87h0uNhTT9FgerlmU3fOc_oqaA3Y4nQao6OaGJtePLOPpQoEaSSKxg_2d62wEnU8jamHSa0HDu9G1NNHHH3vf1SfZG89zWTfoq7hhQI4v43g48qdTRKEayhQnc7xOQWSeow-y03TkKlKd2daAakebX-6I_uHIFcZzlJm6utZVK6n8xntszKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=M_crDEw0Np3n_BXCkRit6PaTO-q7kKXAqMKXJwMuWbUS2a6Jm8AvpqW37fNdcFkMWtzk6JwWyWepzzrFYoUfGWroCf-N5vJZjSXEt2JPUNANzmeNxGBdZkuIn_rJbR35KfJlTGgTmQg3YgSHyDlISTOL-wt4qNAx-NBUEKxpKl_4CflmXLpjk8IVXUPjo4wpurBIDDVMnzRMMIW7Tb9I7_ZAKYPXnpdBBH8RDYSWBlR4H0iACfQejk2kxY9vidsiEO5gtOHQybqEpa5gCHNgqYEdcGeC8ZVhp5Qx1rlEj7PeZ7nS3kPAgbt_RkD9yPDUIC6UGv3qsilceu8IX26Bng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=M_crDEw0Np3n_BXCkRit6PaTO-q7kKXAqMKXJwMuWbUS2a6Jm8AvpqW37fNdcFkMWtzk6JwWyWepzzrFYoUfGWroCf-N5vJZjSXEt2JPUNANzmeNxGBdZkuIn_rJbR35KfJlTGgTmQg3YgSHyDlISTOL-wt4qNAx-NBUEKxpKl_4CflmXLpjk8IVXUPjo4wpurBIDDVMnzRMMIW7Tb9I7_ZAKYPXnpdBBH8RDYSWBlR4H0iACfQejk2kxY9vidsiEO5gtOHQybqEpa5gCHNgqYEdcGeC8ZVhp5Qx1rlEj7PeZ7nS3kPAgbt_RkD9yPDUIC6UGv3qsilceu8IX26Bng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuFzJDa2plDwyVJMZuDb1GLoJcDv5ehAycxyWiI4HP0sEE4ZjUAKMh6EmTUMdZISKWnYosTdz4GXz6hABuQrxO183ItQOxxWAz5ukffrbhShjoF4EtTwqhVh_RV4zp2G4-Raj_yYe4x1d72nid8o9Q0euNQzXKdCAuiLvgbRgKJCnLGxXurKmfKuT2YUUAD3W1IueffpbSAiEhpS8vG_G21KCgAzmi_Cm0gKa41hUzea-G7M1-NIkd5HNe_czApCQAN-hpNV3P58dLNaL5SA936b25_MsY6PeSTt5vQsYhYpCTUUI8-Hai-4-h-Lyzdj9TOIU5mL_5l7mLKPSmjRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l98exSoT3_1s8g3aYxTlTlJ-WdlU-ljHGRmh-_dObRDE1dIBWq4uSQRReB-E996esOX_K5XI4JE_nMkYNj6pWcGYAkja54_qJrlJNIZyGM8_gVpm7UCtGsn_t-QOCsoNcv1VkPRB08axQqtCPg8WISv6dphYPEIjie1FHpkJvEhc90DlqM2C_qyauQhJoUQ2Evi-8FertogMzncMg9e1IHx2v93JF0D0axkVRvoCsIgPrB6igBt-CAS_mQUxw5CVXjBLNp03u_c5H8FX8v7nI8l4_cwg3ZAhEfiJE1JhcdHuiDr2ID14Ltq5wMxxl1zANe65iam4UcKzKF6evPk86Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzDIfgUn417gNh1zbuY5mtkSw-0Wpgi6U9CcMRpE1TthEaSY6YJJl4zE8sNQIsp56PC_XfLhPPhQ6ak1kqn5w2cop-ucK2rYl6M2W71RvD46QrHIcbff9oS9b5kkuJzP7SmlcD_qf6X8t4JbLFvK840-T-db4Ktdtb6t6L-gQldf44XnGZg836O3x_dT6HtyoLgc0EJRJVRoEMClT-iA1Ur_arX1RjMbBVTjJe-Mad5R31LtjVO7P3r1GuPco8cHrWjSTgSbwjNT8eXzS9W7nMs5hf-FaXr8xO06zkAShbJgzB28ns4LErt1s0Azn2zBXHZlEks8woMthLd1qQgZ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=CnDeZKx-G0rgcPfdDycYrWf9aC96dvMhacKdtqGzzuOAHWZ6ngAHlQZIxtHYbCKAlYyvyONbzO3_vzvlGJNOu2aiW4doPA4s53W5KiuSR5ODaKRF9y8J_d4dbjGPqdD5Hg0UTUDmyndU4lxv2lmYXhvpYOo37gNWTsZRhg9IbiYW6-o_miBmIU_Ar02wZNTJIeshPZdPSi6hajJZSzv6qCWgULWn8jHku9QklX1JXtiJxx8HfsDTohY0qB88TRr1CFJt3q81mgRcGzxF56G_dFGxklGr-FVE5Aab9KSpcenLtYCzgwS__hY5UWr3fJOkYc2zhFOwhJEiSh3WrY5ljg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=CnDeZKx-G0rgcPfdDycYrWf9aC96dvMhacKdtqGzzuOAHWZ6ngAHlQZIxtHYbCKAlYyvyONbzO3_vzvlGJNOu2aiW4doPA4s53W5KiuSR5ODaKRF9y8J_d4dbjGPqdD5Hg0UTUDmyndU4lxv2lmYXhvpYOo37gNWTsZRhg9IbiYW6-o_miBmIU_Ar02wZNTJIeshPZdPSi6hajJZSzv6qCWgULWn8jHku9QklX1JXtiJxx8HfsDTohY0qB88TRr1CFJt3q81mgRcGzxF56G_dFGxklGr-FVE5Aab9KSpcenLtYCzgwS__hY5UWr3fJOkYc2zhFOwhJEiSh3WrY5ljg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=AYvn9xyXhG1Iz-sDoIFUcqbDQNTwTl9sDwuFy5EhbFTowSQuY3sh5gWYZsnq6-ln9q6p_WJpWTz896Yrl3y184YyqEqv1gxX-ShbCPffdOVLGloP-snZk6XcclEWW05E9Nm6rVLn4fze67YBs0EoQ-vbYoolPEPCsZAy4bv-NHsT7x2p9VjJt36luVlBTbjZzyfSMZELgeCLTYbu4xEoBeVQpp5wddA2ULBQsQeSTeDlRKcW3bgL6uVkLBxCAI_t7Ij0AAlwWzvvjY6PpLSTZsQilbgemdcxZt7eyEaNjwBYNXBCvOwyoY4uDfitVYuyVfXn3Wa_q4Sa-pSrE_R2Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=AYvn9xyXhG1Iz-sDoIFUcqbDQNTwTl9sDwuFy5EhbFTowSQuY3sh5gWYZsnq6-ln9q6p_WJpWTz896Yrl3y184YyqEqv1gxX-ShbCPffdOVLGloP-snZk6XcclEWW05E9Nm6rVLn4fze67YBs0EoQ-vbYoolPEPCsZAy4bv-NHsT7x2p9VjJt36luVlBTbjZzyfSMZELgeCLTYbu4xEoBeVQpp5wddA2ULBQsQeSTeDlRKcW3bgL6uVkLBxCAI_t7Ij0AAlwWzvvjY6PpLSTZsQilbgemdcxZt7eyEaNjwBYNXBCvOwyoY4uDfitVYuyVfXn3Wa_q4Sa-pSrE_R2Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=NjN-KkJwPd4gD5WOBFC11sxfjPnFwF5ggZc5OdyaJcwuESaklFR-rQ969VuI7b7d9JuYcoXItCjvGxQJ3tWrakg-q80CZQGzNBOsYusb0_KkiZMjJpwwDWWswbGB_izZsAfOMcPVIqcvBXS3ksPZJT6S3JKFLx9G8y7j9Q4oxiYX5XJDtgduHrFIcSiYp0B6ZD33X8S12bZguQ5Yt5NBet_FKyD2nEf7sbfQymCiG95lVuSjDn4tmacsJkUin6W0E0l-JpqoWzWc87O_eXeYQiQUi9J_px4DrcqAk4CsaL3kp7p3xsqeHCJ_0BG3r5O2uPphtyrOpuQywYf9fiEUtXK6y13e0YRWXkKHbaDOES05BZPQwlxM0gbSRFtIaqYzwzslbIgpEDDcdKU_-aD4UGss3owQkW5Q0vqfRAXlVkGHVUxFeL05VrzpC2StNXfFZ90VUIJXUkwQe6af3S6lfwn-OsG3gx5n_7njeLWWK41fnKIxB1lHbcXievwJUoRWIsbgUPOdF67S0q8eWwoavR8Ylc-aOZilM-mLcHM2HNWVEqOhVR7zmFE7vW5QRSSwu8Qyr9sjFviynYYIsPechn5szrUUmcV8A-42xkg6hodUybZdyw9JllB1wfMbiVedAhWV1ouQ4buB71bEQzHK7ek5itn5gP_CKCmj9Ul9iAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=NjN-KkJwPd4gD5WOBFC11sxfjPnFwF5ggZc5OdyaJcwuESaklFR-rQ969VuI7b7d9JuYcoXItCjvGxQJ3tWrakg-q80CZQGzNBOsYusb0_KkiZMjJpwwDWWswbGB_izZsAfOMcPVIqcvBXS3ksPZJT6S3JKFLx9G8y7j9Q4oxiYX5XJDtgduHrFIcSiYp0B6ZD33X8S12bZguQ5Yt5NBet_FKyD2nEf7sbfQymCiG95lVuSjDn4tmacsJkUin6W0E0l-JpqoWzWc87O_eXeYQiQUi9J_px4DrcqAk4CsaL3kp7p3xsqeHCJ_0BG3r5O2uPphtyrOpuQywYf9fiEUtXK6y13e0YRWXkKHbaDOES05BZPQwlxM0gbSRFtIaqYzwzslbIgpEDDcdKU_-aD4UGss3owQkW5Q0vqfRAXlVkGHVUxFeL05VrzpC2StNXfFZ90VUIJXUkwQe6af3S6lfwn-OsG3gx5n_7njeLWWK41fnKIxB1lHbcXievwJUoRWIsbgUPOdF67S0q8eWwoavR8Ylc-aOZilM-mLcHM2HNWVEqOhVR7zmFE7vW5QRSSwu8Qyr9sjFviynYYIsPechn5szrUUmcV8A-42xkg6hodUybZdyw9JllB1wfMbiVedAhWV1ouQ4buB71bEQzHK7ek5itn5gP_CKCmj9Ul9iAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=ZPL_ApO9p7DXtWB-bf-LSMOra_aArE_tfDx_jFEdJnkP8YzhcADZdW-Nb2Zdx9gwLGtP-3A9UzRzN5L1mopk8QzFQPlR6YvVg85SUgnAieRW0OE8-aF62pmmqRkJ3Kn4uyzFiAlfIoj7_T7rDBlOP10rVQfwa_YHURYTqip82VIt0ycvgnWQohZEoH-zxMoCXo8IIf3k8ALDtDKbvIN6fdCvt1yhFfJZdyYxoE2pOfbs9_d7XySJ-3AGknTGMuze-3CQfOiZkQOsfjX0VxDFxWDPF7yck6FXKHzZfls3dDoXnyamtbzDa-SRx3UbKG0UslAv3VZFOeIZMjWoAvL-0AXZbXPTQ6oefWGDvXPPlr9a54vB6MNxTdGBtfgL61g5nU5LtqTUTAzHKhw6W_x_HJVi60L2PqAE3tQGdZlkkmgFyWELNf1QIJhmHhsa9nIfq_28Np6rR6NARtTaXdN4LHYp5wI36TYx5kNrU9KsX_PA5PSd17t5vpA7pRwcIS_evdrRq1nbzq6pbqmd0pV7Hw-7pbNyGetcLNY2T95eVoo8e9z1p7AnoFvr1ynbiYYkdHtORrxk4PGHhLcDaKoh-yvLYa-Enaay77_r7lsTsXwNbmlzO8h9RZw53YX2zGGhrj2pj4CVChPyFH2diCkS4sfQA7XsEFkBMC2RlKnqKhk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=ZPL_ApO9p7DXtWB-bf-LSMOra_aArE_tfDx_jFEdJnkP8YzhcADZdW-Nb2Zdx9gwLGtP-3A9UzRzN5L1mopk8QzFQPlR6YvVg85SUgnAieRW0OE8-aF62pmmqRkJ3Kn4uyzFiAlfIoj7_T7rDBlOP10rVQfwa_YHURYTqip82VIt0ycvgnWQohZEoH-zxMoCXo8IIf3k8ALDtDKbvIN6fdCvt1yhFfJZdyYxoE2pOfbs9_d7XySJ-3AGknTGMuze-3CQfOiZkQOsfjX0VxDFxWDPF7yck6FXKHzZfls3dDoXnyamtbzDa-SRx3UbKG0UslAv3VZFOeIZMjWoAvL-0AXZbXPTQ6oefWGDvXPPlr9a54vB6MNxTdGBtfgL61g5nU5LtqTUTAzHKhw6W_x_HJVi60L2PqAE3tQGdZlkkmgFyWELNf1QIJhmHhsa9nIfq_28Np6rR6NARtTaXdN4LHYp5wI36TYx5kNrU9KsX_PA5PSd17t5vpA7pRwcIS_evdrRq1nbzq6pbqmd0pV7Hw-7pbNyGetcLNY2T95eVoo8e9z1p7AnoFvr1ynbiYYkdHtORrxk4PGHhLcDaKoh-yvLYa-Enaay77_r7lsTsXwNbmlzO8h9RZw53YX2zGGhrj2pj4CVChPyFH2diCkS4sfQA7XsEFkBMC2RlKnqKhk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=ZSaZlquHYfCBHgDaUIbtImA5HW7_T-o60YL7TeunF7lRrlWG-7mt99LXOxkecSpxxhMLdq-opGuRNryJjfE6yf42FgH-hXUr7k1pqBp5bjRcXU51R-f4MQj6VMWvuwoYQzv_33rkYWHJdsVB9gAa2SB-X6L6hL2E_JQ5GBvT83qkKQW1bVqrc8YX6n0L_PlHC5K9O_XuyJUrlYiE6dS65149WIlyXvC6CYaJAmCgB6GTOACZOwRSSj1gkz5f_KeLV4luGSDp8Zge9zEQ_H4NmSW3OTkLBZmzi8CaSLGwBtFUaq_6Fct8cp1sdDoI_kRWzqbSSJpnwNd57NbAYowr6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=ZSaZlquHYfCBHgDaUIbtImA5HW7_T-o60YL7TeunF7lRrlWG-7mt99LXOxkecSpxxhMLdq-opGuRNryJjfE6yf42FgH-hXUr7k1pqBp5bjRcXU51R-f4MQj6VMWvuwoYQzv_33rkYWHJdsVB9gAa2SB-X6L6hL2E_JQ5GBvT83qkKQW1bVqrc8YX6n0L_PlHC5K9O_XuyJUrlYiE6dS65149WIlyXvC6CYaJAmCgB6GTOACZOwRSSj1gkz5f_KeLV4luGSDp8Zge9zEQ_H4NmSW3OTkLBZmzi8CaSLGwBtFUaq_6Fct8cp1sdDoI_kRWzqbSSJpnwNd57NbAYowr6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_rG7DfpSr1gEO6GdcxJqGK5-3jKeJu5SHAhnxzF5p4FD6NcHYjDvWNeNcn7_XvyG-HEr6tqYAgQ6STFd-IFaurMRdfU7fvKp8qr8YrtULaN60-QErb7MQ4D_geQKuZi5Rvbp2-7r_1wfJuWCvPqE0Sp9S4O7TSKYwRhzE4uVdJRWjKGnK3vCnquk1Yk4jRzDsEsYsmx3treo3J4zz7qA10srqsxiPyryCvcHXFoy1puQYNPodT254JUEyeAkuACUIlZNtgWFKwqfEBWJ9FbTUrUpWSi90zL6ysY1j43qdgJKgGDBe_yMnK-0eA1Dd4JMPUNMkMXDb_ZymGAyDk4iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=FjSzizuUKHhwIXZuvkQ3_NTUdHJgJJKfu13JDUZ5QdKllpYsJvXQROtWLOXyUjhHp8hy6E52ByCM1680o-WaHVw2PXX1Y8tYn5erz6s7YXe1Txhn-wTqCbl2ZlgBgYVq5ps3O6cTrnsK4EBZMcH99LO2x5GoY9vzcdWu3fGd-JlvvFEI7MuwMjJhET-rTuldbsiABI3XnDsdJE8naDXVZSpfYWLvembbeREf4zupzkzSeRl0FnBxbbnInycoIOEDna6LEJVoVJ5zMWnaRxjO2fZX_PciZWo42VxcRvnZxOY53Ct18qQSmeBGO2UGh30T43hkqSyztd7yTmse5FD1Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=FjSzizuUKHhwIXZuvkQ3_NTUdHJgJJKfu13JDUZ5QdKllpYsJvXQROtWLOXyUjhHp8hy6E52ByCM1680o-WaHVw2PXX1Y8tYn5erz6s7YXe1Txhn-wTqCbl2ZlgBgYVq5ps3O6cTrnsK4EBZMcH99LO2x5GoY9vzcdWu3fGd-JlvvFEI7MuwMjJhET-rTuldbsiABI3XnDsdJE8naDXVZSpfYWLvembbeREf4zupzkzSeRl0FnBxbbnInycoIOEDna6LEJVoVJ5zMWnaRxjO2fZX_PciZWo42VxcRvnZxOY53Ct18qQSmeBGO2UGh30T43hkqSyztd7yTmse5FD1Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=Hq221zkeMKDyJXj3Xeb5R07SLZTL3PtukDqm9xS2QUzt17srKQKQYEhhol2kh9wRX5CcFlCjltgwM0cl9lfUqw68iPk2sAoFUfhGrJFTsFUElkK84g_kTzmtgFVFjJ81ySYLgj25wOaJi285c63ftxT9co4C_GKv2T49L3guX7mg-WgTz3De3a8vgD-kB7D0zYPNV9Qc9_n_bOyFg2oxYFIwyp9dmmFYLyC_LYXjfA8zxRhlKkaKrUEo3QXqzNfsHIYxh-QzQ-_3titSfKyGnQ4N5iLfb5EOspZu5XG3ZpP_AKeSAWAGN4XM1f5VgkRL4UvJhsgG19pfUBeI1uQyLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=Hq221zkeMKDyJXj3Xeb5R07SLZTL3PtukDqm9xS2QUzt17srKQKQYEhhol2kh9wRX5CcFlCjltgwM0cl9lfUqw68iPk2sAoFUfhGrJFTsFUElkK84g_kTzmtgFVFjJ81ySYLgj25wOaJi285c63ftxT9co4C_GKv2T49L3guX7mg-WgTz3De3a8vgD-kB7D0zYPNV9Qc9_n_bOyFg2oxYFIwyp9dmmFYLyC_LYXjfA8zxRhlKkaKrUEo3QXqzNfsHIYxh-QzQ-_3titSfKyGnQ4N5iLfb5EOspZu5XG3ZpP_AKeSAWAGN4XM1f5VgkRL4UvJhsgG19pfUBeI1uQyLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAftx2-HTXn1WkvPLtcUn9pZ0yGA3rBGFB3Nh9sI4wrZ8s6auoe3_5y9YMMqhMQyLhKTMiBvBTVT-9JFBkdlxsHNDwugZsIyHnHMR7WHCfXn5Zx4sX1hHabiR0jdkJgYyzH214fF7afsEXZH-dHa0pAxND1qRpgr1AioxVzNVuB2GhHLIrs-lmBtFnlD1U4sIaF5oLTfncLBZez8Ukpodii9LJTk-hShEaKrP-S2Qbfet6JrPbtaIXk8-MF1oKdZ6r5cjMHX-dNYhk53OUwG-cMyyfqz4YYW6FRwdDkhiJMY6mFywhesPg10n4t6rdv3uvrPYATKFAccyv6N6k5f5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nk1rrAbdlUsOD95zCMwihNy0OfCp5fympkjp7eCImtxG1OqtpilCmrNRN9I1I8fRf1fvefU1vmyaO32E0cCUexp0HQrvo_yXeKc-IZxGfzB336D7bhNdUAgKaY7akSJsJYPCehQbU2ixFrWwqMkZGnRAoiIrVpTNADZBSt24Oto4QteO3tyKVSXBEqhxH_DKiO6aIiDGvtx5qumyqASQl_FEo0dQfyW0bzm-4jAKNgYO6Z549XocrdTYjGpcF-VqVOSf6PKnckdYuWlsE8ESWyle2yFRy99XFQzc46DsBytNRSfQiwAlWJ-dFRYlLGaikNvwivDspS8Rt8COJ_BR0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8atfsuuPIZq603F5W3-twI2Joxhax68l2Hi_bT9ssLBjEVlc3pS-bS6UCl1CQjrbBU0Dx-FKVbSTm3mUvWsGN2E_-DCTxsezu1yT0I2eXSkaIfFNDkXJ2LIlQOIYK5cPZpbIxCq_Z4EncZEqZ-8F4DfgZpVWCJI8w3p3LcCli0y2_9BQ60_8zw0uH9m4RLcHeSBimk_n2TO1mxBeKfk6mG6yzVkz7FHOrIBop2-PiI1UowluiCeSNViCFr3Tx4MUOr4x6z2TxG6Alr7IPBMDuucuE9zHUYpz9Q1tvDBmIYDgfBHhEDq0qIhujv0KcJJLa67VQ3ImxqCdkcUpyrmpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap3f2ROpZaEPKcH57ePV1mlhAYEWi16uZh3tfXKTGZzoZslBj8TxHofJXZ8zrqib5x0XBiUKJxocUuHWzgs5oVSFjVnLjX4HdsxLzfkrXgaZViKu_RYb0nu0SpgaHuZejyhK6R4D3HJse31oiBYXLCtC1zaukgpXe4cnDi3ToaZByGmu1N6pgbZgdqF9D3KFBA2rJoO8_PY3KG-35pcF-pCh5KPVh8NjdnuVRj5M7XLJIs_abnB_zuEQgPT3mecglgyTj_ohCfLulJBZzDKoMktP23WYNVyHh-5rSD66FZuH4Q8ncJ0tZN_LQmxRspcGN2woNMXoDYk0Ks-JxmCC1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLjrsatY9vwP5vE4nceg43xX6-obb_w4aIBVmdAnJH2gDyFnx_oYPhiN3mGT4UCnIO5ST-95xoaBehIRAY80653OXw7EhxfJUhrsgSDJDZGQuFkGdk9RzRTpThNrrAZXlbRv7iTWjYY2Zx72vNZCkmhk3GpHc7JVkmNr1KZlikHRrRVwB-TFKC1mZ2WiVggz-CnSAZyP7Lk9KG_suTu0bKCgnwjy3Uokhpl3UhChwy75fxHomHJq6O2mZoO9aX7ESSNOwfKl4Cd4REIbTDK2tgNFqq4l7fEq-hGRAigSqV-lpRY4GPySpVnftpKXPRSzwZLOM1vJuigLdmvt_aoSdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHH_eZFzFnyc75MWldvPVDOkxJqtqYE8kuiI-rwgvlzlrXPf_FnXT8Fm8Bd5uWjbf2DmirLpOVjy9Mqhw4ct9FfuCMYmg_G_E7mxfRkHbnWXF68POzDEv9H3Z0CmqELeRgD04T5OcE3TNWY3s6WqrbwryV7EUjOmGdyRGNGhqThULzB87DZ-IitwTZrEBSej1xJY-28Ymr8LF5j9m-JW2JYRmjjo2nn3xSScVbKfDZ3G1OAarTGPVV19AJ7ZYvckkc1iGQ-4ru22STzudUtbJ8S_rGW0gld3HiDexzn39fe2pnZ1eIzTd3CnmcioE0OpEvFa5SPMeFjjlTLDaVmw8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_SBMhAgkDfRv65gJXCIbbnzK0rEnEWKzyLYhrwJchVBMr-_-JSCibNFR8m2ljdNXuwSyJz1U1izTKXwrvY8hwX5U8MnnzuoWuEueY18S1lCP4dwFsuFYnHQwyMW38TDI2geLSszJd15AmwMpahe8SXVIlqg2YE4iYYksCtnvw8Ed5d3nf6lspq1xr81EwERxa8ax6oEZ2TUfNbmnOL2_5BnCwQAzEd7P-0r9byG7zp2Wb0wQvYuMVs0Uz3YwwnAoiSSaLbkVyt0J8asZ-lQk1koIJlajD3jH6o4BZHvq4rkKMnqTF0NE2_lCT5ni9EgaC0jPLT6txieKYLOsTsLjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ijmajyYiB0tpXa8ByBiK8QXg1LO05LlXXCGbWYCnE_EnVw2XGPI2u3_VFLrQvIM-jtnVJHinDkcUkLCuOZnvV1atcT7RPH-F0YUGKrkd2SZH9H4SHIfEY6D9DhNo1x23_JmukyOs2D4ewre6gKE4yR2ubkwhX-AsjNXgSosTdjBybMbfSlWR4aCM830vdVBhIEAy3lpVGRDpWlZgn2XAP-3k6fXloKTJ37KBe2SDvvJD_aFwYrYqDaaQ5NJV_DG_3pdCByHfrhB92UEcPvchVqe4dhKLcC-qJVVMA84CPt-c3L_QwOAxbmBegRk6KzdZOX-86_dQtNvvGQECXN50VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFzlEdNr0brqfaNu7kVUM6khyo8pm9kRM0M59K0WNxjgs-ud9mrfURQQ4o7w0ZVHpZdLL9TBNj_P8puisReyUJ4U9eAQRSKoBFKynI5JqUfKT_zqYiAUUhll_bcp83do8nNEq5Ix7X1pLHUgarLDLkFtmA2_PZIb3Wacstq2s5Pg1TUEHwQxSaiofQgWVR0sOSo47KEHDbArLgIET_M64Gzb7GLzPbRcotv3iO52DKm7oN5xxBzHa93l2ELe0rYBD4uuDCYLTnlLg0DVClPxhGCI1-VfIDxs_18ZeKnwP_0O1DH6rXY3JxxntLwXe38MgF9N9t0jiw66cdCK7qiyTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4EGNhFX7AR-zT6LWD0ujvZ8DGIz55lu1L3-NLCjV0jwDam_rjkL5JOAf7ehqQ_ujhju5DwYquKIKd5H_-KNFNtC6ABmGxifC53ow5DXvQ7lrBboysr1U4NrAkIXcE3LAu8VwF_CZ9U8y8o9OEAHRz3MQiRwAzHm-ZRSqJRyl-WPdixI-mjVvJLFXjKlJ57f8lEZ_glvCghQ3N9Xo0YGyDbp4o4Q_OmZbc1dIxW-06kcycpOddGZHWaOkqvbFFSzRSguXZBnJZZIvVciZ_na68GVvHdhCo43OS_OEzN8wqlgs66NRPB3QzLR7S-Gyej0WmnFf953WnuvPMN0f1KxAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=DKKSyZHo3YK04K84idsSqZ4P_BF2BvvgIS8_Sq9swsVFt-n0ZIT02DVkCz_AQ0ZN_9zk48zYajlyZWgr0GmvpNE5TGP9TDB3Vz0khSiccJB6gZAfRltRRsZuxmFaDm8RmDwL9rjXOG5K_SGgGPpTnXTF8C3AOebCz-XO11cF1aZlsmYtZEAAI9yxkeMcDq9sd9MU-7c0E67E583jtL-YW00BSBZGIs7lNitl_0BNQR5qq51MGSO8_JzhF7DXn-Zb2bC508G0jZl2ZDwOa-DJsMcVX9zmpbK3gvpI3tVTmfF09ZWGAej8ZIp409hHd-wOf851eJ6zHdvGOWUd6cZRdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=DKKSyZHo3YK04K84idsSqZ4P_BF2BvvgIS8_Sq9swsVFt-n0ZIT02DVkCz_AQ0ZN_9zk48zYajlyZWgr0GmvpNE5TGP9TDB3Vz0khSiccJB6gZAfRltRRsZuxmFaDm8RmDwL9rjXOG5K_SGgGPpTnXTF8C3AOebCz-XO11cF1aZlsmYtZEAAI9yxkeMcDq9sd9MU-7c0E67E583jtL-YW00BSBZGIs7lNitl_0BNQR5qq51MGSO8_JzhF7DXn-Zb2bC508G0jZl2ZDwOa-DJsMcVX9zmpbK3gvpI3tVTmfF09ZWGAej8ZIp409hHd-wOf851eJ6zHdvGOWUd6cZRdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogKfEybUdNEsgZ6Q_ocE6o04QUcLwMjVAwHexI-VWenVNfVZfpOTz9F2cQtD4TyiBt74pMKmR39dIhjoMfZS_3gyLPRbIXUNOgaYNp1wwyV7u6k6gCWokBo6uZ9LxnDtAcmwxzQMlYoLhHSrX5-8_22GSGXLiCzcf0NH0RPNIQVbXdsFB1tN_ACCtZXFXaqCa3hr5hv6Mj2lCzdub3PkmAAHaMJZ1g-Aug-CWt2nV0OL-ac3en2oytwEh1ITzb2hCZoWv1ZQpPU6nkMYEMZPKE6NRnMbFxrGenUOaji5Mnn6xxXPCQLKJieivX2-IpIya22Ch_Trb9TCyROgfxq3Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhPJgLAhniBEqBBYSbiQ7vvdArVdjj6NLvNJ3S_JMpuix6cKLSqZKW3XTzBsw0z-UMvrF2Lk-HYEpVHF_6ILovfrdUe58NN-CrcWN8clFnZmH3RK16M4gb3vL7NkuCjeBZfhSBcu7nnm37DeewcnzuDfWYiWOoPDV52pWwy5op3Lql62tmDy5zBiUc3cvpoltsM_Y3Cy0Ynum1jjBFvh6LAJQ2NSplYxcNj0-qZLUMB_Fd0fJMz5NlS-2Vf8JNf1IMVnH2-68sFJLCyLFLDGjzOiSZCB6_oKxmE5il7z2bEaTwp_YAFF39MUN7pW3B92V85dvB9WqzCOQ4uvhwrDQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=OUmYFTtbTNSO_0DdgGvJl5E2Jlc_mnLVBIwIimPhUV1TClXRDH64vLiOr9dZTjxEOMIUp_yeTqk_sxuOe0g7xuEk1IO4-UCbuISGG-taBfKHzHsD4TBp-odGB1WUeGf-j1hKFzVFYjsmHh1mQRdlWVsDI_kt5nu3EPTnKc4oUeXfj5zZI0BBnqBwsmvJFBkbppVsHdjlblXR59cT1n2Oh47b95rhpH3OaZkzewHbjl_bgqpLQda_DdE7JHBOFGqcrXNngGm2WYod5UJiiVAOgT3F_9R41Upwu8wC2FHXNHEuu9TaNDiymnG6ambwA4e4upunRr6C-wY8ZP7mLH5MVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=OUmYFTtbTNSO_0DdgGvJl5E2Jlc_mnLVBIwIimPhUV1TClXRDH64vLiOr9dZTjxEOMIUp_yeTqk_sxuOe0g7xuEk1IO4-UCbuISGG-taBfKHzHsD4TBp-odGB1WUeGf-j1hKFzVFYjsmHh1mQRdlWVsDI_kt5nu3EPTnKc4oUeXfj5zZI0BBnqBwsmvJFBkbppVsHdjlblXR59cT1n2Oh47b95rhpH3OaZkzewHbjl_bgqpLQda_DdE7JHBOFGqcrXNngGm2WYod5UJiiVAOgT3F_9R41Upwu8wC2FHXNHEuu9TaNDiymnG6ambwA4e4upunRr6C-wY8ZP7mLH5MVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=KN3QVMdlDtt3lnzYxwFGSCWQ7ird61584HewHmShdH1UaNCA_CdUH1pd8RuYRaLRXdQ3I6HeuH57QlxMxbEmdkJzuV8m2RtZjTKIOqojLqnIItbOoY0hfoe2LJscMEfhf2SMR0mNGiGbjxUEU2ICKuHeoGKWIzB-y2FdpRKo7lzW6ZhrNEcdXGexhUP2KTs3LAfS41FzN7gZWz3yZz4wpcuOzZVT4tZIIn20R2EwVbjw3v4rXDw5SAVhud0V_oKQo0jZ5KVGw2PHjLBfTEvz0StQ7V81Vrk3NMEbuK7ROzTujkdTXefUvz6sweTBUv_ZJ5msP-1vkCA7qBVvRLaRzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=KN3QVMdlDtt3lnzYxwFGSCWQ7ird61584HewHmShdH1UaNCA_CdUH1pd8RuYRaLRXdQ3I6HeuH57QlxMxbEmdkJzuV8m2RtZjTKIOqojLqnIItbOoY0hfoe2LJscMEfhf2SMR0mNGiGbjxUEU2ICKuHeoGKWIzB-y2FdpRKo7lzW6ZhrNEcdXGexhUP2KTs3LAfS41FzN7gZWz3yZz4wpcuOzZVT4tZIIn20R2EwVbjw3v4rXDw5SAVhud0V_oKQo0jZ5KVGw2PHjLBfTEvz0StQ7V81Vrk3NMEbuK7ROzTujkdTXefUvz6sweTBUv_ZJ5msP-1vkCA7qBVvRLaRzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNM3m8SPDpj05KCRar6JzTYwMaGn9T4Wycgfkzd8o0ubOsCTFJF5MJG5KWrZDPzQezygaYKJoJs6_iPwQnyOUXP2_kiZ41P7zBqbfX7O_ZqzoG9HysBRHPRNV4XrBWc-m3dicConmTDZ_KaT59qphBvlmPzDimxZxkliKfFJOcexjX2IjihnrQVbEzIXpPYKcTnuj4TXsQo_ZqMm8qTtftwS3XimepIDflTUxlnD4W6hs_3VOWlL2h-LgfuXi5UUljYXOUTQG2OiC5c3FQypdsGK_WI4RbpzEG2QllSMDdJPTZd5amxEe9QU3IifNZi3vx4QjOlnQm_dbp2ODhm-mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJLDdwV7UAELK6s5yrXN1wx3kgAj9LOYwaMMa59XdW6uYJBb1Y8a83uAtVYgyzDd_I21i-fH2v0i-SkfH_lhcNaBWOokp2cD-Mgv1A4jOkbvOuM5ZXJ-6KubSS5I56LnP8KojZ0dODGtOuXtMjm8xwXBr_KUzDTeFAgNHEHDn63yQuKb2gpvmegstrAqrsMeKHPDCsvZjil4gcrePRDoHmjwwM_UIGvjSVRfuc15zOkC_ZoilGd0S2wH8p7d5msP-MU_m7SXuQPkUuyGB1Y7LTlgfP0R8n8nmy-FzaSGbn_GpO1Yz_AsdKkKDwakBA0aBnHjGzEaDoyNGabixw1mxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
