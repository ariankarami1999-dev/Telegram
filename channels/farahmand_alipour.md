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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 22:38:16</div>
<hr>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjbkYuqHCX8tvk8FH738oH6LbiW0LBtTtr51yVpVZLz_IUafjqyAmhutjet4C8pXhfMEKXQ3fzUZpI46h1Lr98uixjbp9vEAbYLBZMIzDnFPUTsQaRr36JlyTJ5JzG09hpJJvhwdDc0duJSFunKhvqLDArL3c9idpHajMBVIZ9heLshXp1hBxXpGnfn8eFzUA_jbM_KKJ2nIV2oe-E5ml3PL7uYj2p5QDVRAVb868m7gnyGMVDqEndNejC-fpQm-tnQ75DCKzizXsXmrjMywi_pIEJ8f4-vGDm2A_PRKP_kw9FuaqbjDC9FJXQqDsYYDNSselLkHNpUozWE01bf5Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOnvpxa3yMMXdMFzGbv7vNk5xdCTrkFF-pF-B691LL-njXx_zK48ITb0b7Wb4fpnecu_uxVscObgyoAiJf-gMEypbFAM9Noe1NPADZno3BHq9_wkY4OiJPXgSn_aOyXROQF--2wctSkrd7O8zoER_KhgMGBOlAodROTaCBJBW6TnZ5zRWX6Scv1fSaZchDASMkJZLjK--5YPTFJrTepEy6SYr8DlYOTmYNkMnGnhKGAod17RLdRFVFguvQyUEdJ2V8BdSb9QwNLSarYYITsO8EPyxhZlXS3ZwduwJHYLPUzR7zmyid4ARVcg5Mgf-FlsOKKPm2pLeTmIhtl5DWXB1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=FX0--yIVzTty_e0CyZEfIqykjL7Luki0bnLnOnZuOdDq_S7E-_JmndKaanId45ULsd8s_PdSpkFPN2-cwDHXvH2BvlO-_y7uJ0Ie1CU0gl4ko4vGZPjM06qchSfFvXngAZVIPCF_XD3CdgQIrhOyqrU2ebkqyZRRWJc0xnGzDKJPI9nBBcZUoh1hZZoI37sPbENDBxIl_sAA2WGr17MhOQYC-X-YaMsyAXXibupy9_4fDcHPDnRZMJqGE8Z9_DUiFfl9ufh5UvWNz3qY9PY9Z5ofaFeaTuZ95SY60sfq956mXkgpWV0h9jX17AZvHNiG5cSOimd60kxNAdohPu6dcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=FX0--yIVzTty_e0CyZEfIqykjL7Luki0bnLnOnZuOdDq_S7E-_JmndKaanId45ULsd8s_PdSpkFPN2-cwDHXvH2BvlO-_y7uJ0Ie1CU0gl4ko4vGZPjM06qchSfFvXngAZVIPCF_XD3CdgQIrhOyqrU2ebkqyZRRWJc0xnGzDKJPI9nBBcZUoh1hZZoI37sPbENDBxIl_sAA2WGr17MhOQYC-X-YaMsyAXXibupy9_4fDcHPDnRZMJqGE8Z9_DUiFfl9ufh5UvWNz3qY9PY9Z5ofaFeaTuZ95SY60sfq956mXkgpWV0h9jX17AZvHNiG5cSOimd60kxNAdohPu6dcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUIFPTt3kZkRq5RjumETcNKCTkK33JcQlyruONT3qksb7sHWHt-rf8SsRd81OSHIT1ZXjmrP_HWPWOjma9VwMSb13jlamV68KYwjtFRoVwXSI_yrPWYesdZ9-4w-vhE8aZZ4yf_G0Rg-2zzUbYEchqVUFE8AuJ0xwTK3d_YsEIu28CsoESl8RYBlxL21BuFJ_Th9JaBp2tedq4ApJGtCnLugWehFVGY9fjKZEQJxSz5rmMbzzNeNQXXspOuxTN2yttg879Y4OCjCihgQXlXywaRtNMYRz_xuVHvAfN3jgR9VFF-CKcapgTeDsVMBlcZajPO1jnKWdW5V-GLKbVUhJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=ESnN8mrtxHsd6gN_CB1HZ8Cg3D2ikeXJRfEAGBP9YYp7wZlfUsdMXse38-98nwAwoUfCIcz2CrPVzyfbUbCkAkRkJoilTIfzAfY2iSxjRimYq_D3lhYhPdeNZxMPqjcU3ZHMiRwcstQnMo1inKfB8ueJzPIVLr8ftmViEDhfzhYPenLbEkvSzM-o_AcYPLAKqFXaM1WMVJ_NBwpMiuwomOHaNu24FLtsqRWPqZw-WVDBugGOp5E1nEpEo0Il8Dq4IAA8h5ag93vuie5rjgM29-BkPIozDZI8TDOI6klJhJuRlYKfFnkrjK7Ll8DePgIf7veaKx-3IS2rJ14YRabcDYGbVVgMVYP6XljUsuzobgWcUp78VHP2c4AJAwF3XheGM-36mQtGJBfhd-yefF10NyZhbZ4OFG_WlxxBSZocoNMxOLp5J-W3JuSyNzv7jwefQ0sVyjkByrnvf0EvP-s2VMisdAKk0SrzGEBgyBJAPkpbMAaEHyHjl1oSOUuCK38IqhN3eJOzoqHZOAU6SmJwEAWoTlmzPgQf9XKFRCw0v_wp2H0dVByRCM_8-BNnr4QKuAqHbHE_dfsMW7qP1jbMYK4g-pbsfMYbVd1HjP90vDVcU5LdMaRn6tb3QUN4tP7hUhvrHKaRx-GDSLN5npm7UD3TU74vbVPQ58qShkE5uVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=ESnN8mrtxHsd6gN_CB1HZ8Cg3D2ikeXJRfEAGBP9YYp7wZlfUsdMXse38-98nwAwoUfCIcz2CrPVzyfbUbCkAkRkJoilTIfzAfY2iSxjRimYq_D3lhYhPdeNZxMPqjcU3ZHMiRwcstQnMo1inKfB8ueJzPIVLr8ftmViEDhfzhYPenLbEkvSzM-o_AcYPLAKqFXaM1WMVJ_NBwpMiuwomOHaNu24FLtsqRWPqZw-WVDBugGOp5E1nEpEo0Il8Dq4IAA8h5ag93vuie5rjgM29-BkPIozDZI8TDOI6klJhJuRlYKfFnkrjK7Ll8DePgIf7veaKx-3IS2rJ14YRabcDYGbVVgMVYP6XljUsuzobgWcUp78VHP2c4AJAwF3XheGM-36mQtGJBfhd-yefF10NyZhbZ4OFG_WlxxBSZocoNMxOLp5J-W3JuSyNzv7jwefQ0sVyjkByrnvf0EvP-s2VMisdAKk0SrzGEBgyBJAPkpbMAaEHyHjl1oSOUuCK38IqhN3eJOzoqHZOAU6SmJwEAWoTlmzPgQf9XKFRCw0v_wp2H0dVByRCM_8-BNnr4QKuAqHbHE_dfsMW7qP1jbMYK4g-pbsfMYbVd1HjP90vDVcU5LdMaRn6tb3QUN4tP7hUhvrHKaRx-GDSLN5npm7UD3TU74vbVPQ58qShkE5uVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=rF_PUfJyimf-q0CBMHTzXxIQSjJBwdPMdtnBgDDz1TOQUVZYfsole7NNTQe45kZ4hK-dXe0K4CibYDIOJ9Aj1vhRFKszDVBNflN_s4e0YT-Hf4VrHg1TeAXXilwA0C7AboFeHs8XzDHIdHpVgYW4ET0tS2p5fc9uwa9F01jJKix2T6bRQQ68ly57_6oBirK7_jbCWnf0_8DhIgx0B56m9DeoW08Ss1Fs0H1cgcnPGTdKpEYvv4xJ_-_9hB2Npqxo9PcyKqDj-0TMrIJrNUOZYmnUsfCFVtSuZoqBdrx4WSWZ8xSMY1gB2cfTe4VBgy_zePNA4mAvEGB2fDNnIXeASw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=rF_PUfJyimf-q0CBMHTzXxIQSjJBwdPMdtnBgDDz1TOQUVZYfsole7NNTQe45kZ4hK-dXe0K4CibYDIOJ9Aj1vhRFKszDVBNflN_s4e0YT-Hf4VrHg1TeAXXilwA0C7AboFeHs8XzDHIdHpVgYW4ET0tS2p5fc9uwa9F01jJKix2T6bRQQ68ly57_6oBirK7_jbCWnf0_8DhIgx0B56m9DeoW08Ss1Fs0H1cgcnPGTdKpEYvv4xJ_-_9hB2Npqxo9PcyKqDj-0TMrIJrNUOZYmnUsfCFVtSuZoqBdrx4WSWZ8xSMY1gB2cfTe4VBgy_zePNA4mAvEGB2fDNnIXeASw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4QHgHCil5rd4sclLYacHIEjcZTRA31fSEd6RN7LVA-9HKipES_Z9ogd1AelRI1HOFiEdu3z4yDw7tjf-NFA3byiJUJqCt2iJqSkBvYw4AFt8dMbu9oOg1DO_ppLYeFExI6FNWH6Mjox2NQtkD14KLYHL0t_Nc42L2B67n7YNfJrpZl_gBCatKVjzfX-EKN_xI53V6xdzB20DrYrfdgTtoTPshCYZ8UHa2JyF6y73vgTwsGxw8tHkX6qqW-g16Vd3X31gRrG0NDqN6Hfjc_9fGSIog9ccdDbgWKM9ytlEYhEaWhq22N3rso1aJ1qOMnhbpG9wL-3G3JmZHvJ8xa7yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDxH9xYAlPxXFikQvxbNpz4Gc3y_eZ21LMqXDBnKdheNLtVGmmsia-w_iWcitRAJKWO2-WzsdMfbXutzpMOZBgFv_-42bxYmKfkeHbl4n4kkrUkmwhIFHL2cgAr717lYXoXYU9oCecpMJV-2L_qjCG_9J5EPnpEA6Eufrjhcp2lFtCtd_kCK8z2oQVo352cVOeTAEr75dYiHv_k2bARzI41QsIfqbiAiFJ4EqgUKXejuViRhtw0OuVH1E9TvCygPCD7SPC_wtsyA60MTeRSdZxUuguW6qpcqIXQ0YwFV4zRmPT0JHoZWBzIicKcDkeCEeFXj0zj28tMPHHfjOwl03A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mkz72Q0hJEM5YYY1hBAW-dqXjWbEQWV4P51QSENt7MQYl9C4mf712FnkbQSglsH-Qdmn9RcmZoN8lD-dmMwWvgUowhy4JEfR27OCccVK9-zD1IuJYcZ45kr58uyTI6xBg-Fo6_PaqhFT6ZMBFHCeBD7QZOWcAvNDwq-6sDqvjSmqngB_QqwyTaUdBJMswRn0A66uJuYEjh2r8wFV6cKD1ankod9WAvtlCFnzncqcuYpkktunzxx-G-_e38Uy6NDAtlFLXtE1suP8Mc3iMe3mt77_u-YTPzfbTLJqHQdF9_XQ03Ptz4oN8Z6AwVnqFw_R5rS38TXVOMFzHBBBI3J5NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOVPCbEho_LCJfbislahVjkvbdL-hw2wOSvfEOWP3cg_hAsbEWBrQLmrHEPEv-_BNizT7CFHLsO_tHEIUADQLwcxgpBPilLldQddVsOE__g6mCfmcviAN80OvM_rf56I0kdv29vRt9N0VB-V6HgvczQ19bBi9b2Em7p7_hwJQwDGCIeLgAK7v7P0tBlA44I8L6b8fj5XrqrFfzgDY1naLdfTDtZ6JLHMIbpyQHn8P2fYt1w8ivmSOI8NjMClA8MeZTR3PhWeMH_VVE7nMPunYbqxSXm1a9FU-f5eZ46qyls0Ob2zefAFXseuJ9Ap7CEiC0-nnqNAjseB5dtZC36SQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuwj_JZqkXtDQ1OLHs1VTa42sbyvsck7Qn-cd-9LgAodYChZIliy570SmMyHDnVnXqSyfla3kPI8QCdybQjDCSEdGF1xyTGk2dDZhlTRqTqBSh68YYyAPZ50a6qR1-VAvSm7owrJe_MG7tH4Gl3n6SBbmYvXFLXHR8xMS4daFzS-qK8PEokNfe-RridAHh4SKltjkLqIUjUQioOnDwlhp3hdrZAV0JPQYzbeulgD34zwzGE6kx3H_SwlE5H302w2PL0EqlolJTDp15VbBZsWSOaXCXSi0wYcZI-9achDc6egLm5bR4YMYoOMBfSuwYy607hT_0xNrhqp9xDVgIce6njg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuwj_JZqkXtDQ1OLHs1VTa42sbyvsck7Qn-cd-9LgAodYChZIliy570SmMyHDnVnXqSyfla3kPI8QCdybQjDCSEdGF1xyTGk2dDZhlTRqTqBSh68YYyAPZ50a6qR1-VAvSm7owrJe_MG7tH4Gl3n6SBbmYvXFLXHR8xMS4daFzS-qK8PEokNfe-RridAHh4SKltjkLqIUjUQioOnDwlhp3hdrZAV0JPQYzbeulgD34zwzGE6kx3H_SwlE5H302w2PL0EqlolJTDp15VbBZsWSOaXCXSi0wYcZI-9achDc6egLm5bR4YMYoOMBfSuwYy607hT_0xNrhqp9xDVgIce6njg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=oOyXUNFC8EUa3NM_vxSJVoNxAjmDD0JWNVICc6CuLQkenEsMmQ76XCXloxvyisk7Ux_BFSyM6iHIBLMxWPb6zZBLJSdSHzIm7RIcEmW2HvjBzWX9nUofPn0iAk5KTbV4dR7KuNf6P_PYyHc6_sZkzp0Uq0xvFgqPieuPnULAza2EXAyL4A0r1V2DfjvCS2-12hklLsUlse4wUUh7W1CNHQX_DDTFsI99DJScS8yWalvq0gO53i87UiWCijOR6loRKDmt6lgu8Pudugqj-WJ9CMdD9ZavF8pBYcWTu84WX87ysFdS4_Zn7SqCiwbt4X7Hx8laOq569kJNCceftlHGsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=oOyXUNFC8EUa3NM_vxSJVoNxAjmDD0JWNVICc6CuLQkenEsMmQ76XCXloxvyisk7Ux_BFSyM6iHIBLMxWPb6zZBLJSdSHzIm7RIcEmW2HvjBzWX9nUofPn0iAk5KTbV4dR7KuNf6P_PYyHc6_sZkzp0Uq0xvFgqPieuPnULAza2EXAyL4A0r1V2DfjvCS2-12hklLsUlse4wUUh7W1CNHQX_DDTFsI99DJScS8yWalvq0gO53i87UiWCijOR6loRKDmt6lgu8Pudugqj-WJ9CMdD9ZavF8pBYcWTu84WX87ysFdS4_Zn7SqCiwbt4X7Hx8laOq569kJNCceftlHGsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=FJK4kbGenPXaEy5HrSLF2RWlcLRcSy67mXIFN8kAeIBODieOrA6qt6VKPXDH4mZZ-XMFCbs_eijVC94upbKPl3ShisAlqjcxMvuZyFFXoH7TCEFSdLpfpEPXorLGdYcwGwLR5fIvwwrfYVJBvGN9Ic27rxHqGn_t6wFC4sfmvXikjbVcpCRYEqqDuTCI5Kdb6EZQnF_TN4mAns2TTgKgAO8BCLxmMAA2JsUUVEWL76gEqRlX4QX_E727mkwcSrMZhwiA8ABN2D23QxtpDp-CXExVA9Gn961QMlXeILNABikA3twgoerCHWM-Bw3y-3yZWDyLm1s1FiM8nwp21-RQRo_KGbCqNhUOktzXnHdc7vDAUtQ_ZAvwLjCNanOaqX4L5e47qnNu58zb29eUeTkBBBFh-m4ePXNpzRF_Ll4I3vYM8Nzd8fkDjZunh5P9OgYhEAbDNyVxVcF_T77ghkAIOfApcjg23KxC94Blinu_L0gTvAazV4TuDOX2NvuDZqVaMJ_XVf2LCL5mCoMw621f46YiYcj_-_EFAowM7XYimPLpX75CkCmyWeRDNcLz-3205jyCC6GSecFICqTQIll64N2qJoigcHuVykqtdfTLWMHYkWhNkdHYftIMLAC_eLEHVPAuxX72qtcAj1WoiGSHNbaI9-hoJXjKDYljFPRouGo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=FJK4kbGenPXaEy5HrSLF2RWlcLRcSy67mXIFN8kAeIBODieOrA6qt6VKPXDH4mZZ-XMFCbs_eijVC94upbKPl3ShisAlqjcxMvuZyFFXoH7TCEFSdLpfpEPXorLGdYcwGwLR5fIvwwrfYVJBvGN9Ic27rxHqGn_t6wFC4sfmvXikjbVcpCRYEqqDuTCI5Kdb6EZQnF_TN4mAns2TTgKgAO8BCLxmMAA2JsUUVEWL76gEqRlX4QX_E727mkwcSrMZhwiA8ABN2D23QxtpDp-CXExVA9Gn961QMlXeILNABikA3twgoerCHWM-Bw3y-3yZWDyLm1s1FiM8nwp21-RQRo_KGbCqNhUOktzXnHdc7vDAUtQ_ZAvwLjCNanOaqX4L5e47qnNu58zb29eUeTkBBBFh-m4ePXNpzRF_Ll4I3vYM8Nzd8fkDjZunh5P9OgYhEAbDNyVxVcF_T77ghkAIOfApcjg23KxC94Blinu_L0gTvAazV4TuDOX2NvuDZqVaMJ_XVf2LCL5mCoMw621f46YiYcj_-_EFAowM7XYimPLpX75CkCmyWeRDNcLz-3205jyCC6GSecFICqTQIll64N2qJoigcHuVykqtdfTLWMHYkWhNkdHYftIMLAC_eLEHVPAuxX72qtcAj1WoiGSHNbaI9-hoJXjKDYljFPRouGo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=Abz3mketN8gljhP58oV1SEI3g8Y96l_QQskkQ7WbUBe1M0UkvlDBeXVz0yK6LYQpbmAAa1JbH585nYyP8wiJGKPlBQWbHUJ43iXjcDb6Mt-JtkNcVe2lIMOfq45soQPOy-HFn6xr3AxLGyST5c3viMjMbjktlnUVrAt0t0Y8384fD5MurosE6iz2PQeF6I9QWLOISpIbrI8wL95wWGUO7DxPhswM8FgixA3mkceMnaEcelqdgBQdurlwUP-RK-bI92-mWBQL1D2S-7bLhzFySvErodxR3VPEEuER0YuRlK7AzCVt5AKkZzG_LmnATrPabPAyVpkpAet-dz5PfHWMuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=Abz3mketN8gljhP58oV1SEI3g8Y96l_QQskkQ7WbUBe1M0UkvlDBeXVz0yK6LYQpbmAAa1JbH585nYyP8wiJGKPlBQWbHUJ43iXjcDb6Mt-JtkNcVe2lIMOfq45soQPOy-HFn6xr3AxLGyST5c3viMjMbjktlnUVrAt0t0Y8384fD5MurosE6iz2PQeF6I9QWLOISpIbrI8wL95wWGUO7DxPhswM8FgixA3mkceMnaEcelqdgBQdurlwUP-RK-bI92-mWBQL1D2S-7bLhzFySvErodxR3VPEEuER0YuRlK7AzCVt5AKkZzG_LmnATrPabPAyVpkpAet-dz5PfHWMuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5dMQLWShAP5Ioe2gbG20h9qsxQASkU_hFE2NgM9S-ugqOS-T-tCMnqVD5q_1eX-VeU6UQyuFqnj9BZLiO_a5UF0qRLSm74jWF16ht6nnJSedddtHdrk-uAnKGL47mB21JRbjw4hUvpSoSp3ViEQRDmH92nxyXB0bOY7Hs0w5RUKk7RTQ6gCvOkFbP9YXsfEa11h8soGUr0Lc816Re_6I3lCz3wGrMG7ASKsdD_rpffvHCyDaTkyhokM6oLnqskkI327IxW6XREvAb-yCBEKQszdwGD1uL_XobXPymNNograyRNKJPpA00R4Tk9KaqIkNuNWSSzk9W7GQJTLPNv9Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=rOtkOJag3N7mUDYkKrm1YUn5P-OFCyk6Po1EwjucieJSnXzsTk6HUSbTCn5fck850rr3ob8GF56MM8Axni3ZzOCIbr5j-CBVam_WTrEECt99JAidrqn6O-TPvigOLdPD1SymKHJHYPTjh4rryX7zGgtUNcIxunPUAGzlYhqel9-y977oeON0XkSZ-qx-OTvxBtYq6ov6AQTXt_UaU0Dt_TxpEHXANj8qGHVyCVbpKwKeXf8Trixe68sbPR5UMhiBYrec8PoCh2pPns8Wmf3hI2VjJevQTUWMUA_H62hHw-O6h2XoFpN7mBRnw2SXxOhE4XLzW8zdjv7Gmf8uSPclIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=rOtkOJag3N7mUDYkKrm1YUn5P-OFCyk6Po1EwjucieJSnXzsTk6HUSbTCn5fck850rr3ob8GF56MM8Axni3ZzOCIbr5j-CBVam_WTrEECt99JAidrqn6O-TPvigOLdPD1SymKHJHYPTjh4rryX7zGgtUNcIxunPUAGzlYhqel9-y977oeON0XkSZ-qx-OTvxBtYq6ov6AQTXt_UaU0Dt_TxpEHXANj8qGHVyCVbpKwKeXf8Trixe68sbPR5UMhiBYrec8PoCh2pPns8Wmf3hI2VjJevQTUWMUA_H62hHw-O6h2XoFpN7mBRnw2SXxOhE4XLzW8zdjv7Gmf8uSPclIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=XM0QFYu04-sx-Ak8ucuhyM6ROqDUCAZ2TSK1DBTtq9G33tSn1ijwieb1Ovc-64Mn7mOjAPTy7FSwchPUd8Wf13IgN-KLgLiUjcvagaX9OwXxPT9usVy-foQPsnUdwD-5WzsIzKuVaxGBLS2PLuD8oUNWjZizr-dxfeLGYagV5igd7-yOp0H1I7gVG0vrvIY18f4P3AFNlWqQdKCbZ_JjLxyny66UYYIItSf2AunYT3iC4zV8Ph0cgt70OMLh3LBy7aMNYrELaLs4h1v-WsXFBSLu_aEQ0JGri8kR3zFxxW88VAfSd7wSZY0iNyOFTFrJ68mvCbM7JGk3qDaiSidf_QuLByJfCSvTFznTE73rTEDcEKMInSPIuwTR_rS2zfoyN46KrVDUGwr0HHan1AnKHz2st9qM9zmpW9aYMMW1MbC9XhYhqI5Ghn64stGAiWg92s9WQKmn8HbvXkWHzwIsmlrZVy3y2cqBI95lZkngZ1ihmHDoxcE1imRECKG1OG7SERblVbJi6fl5bOBH7-AIGbfCs-mLPbbMDX-ubdXf01As7iChWj7Cvu68IYQH1TpRFaYOFVPXjyr4z-ZYCdPqiBDn96iriEnSbJSqpObNjGIlTDJVOSLmDax_3Nqk2xBk9moMy9V3B0Zo91EqCKQWL8BzaKuMApQHc6dk-QcIlTY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=XM0QFYu04-sx-Ak8ucuhyM6ROqDUCAZ2TSK1DBTtq9G33tSn1ijwieb1Ovc-64Mn7mOjAPTy7FSwchPUd8Wf13IgN-KLgLiUjcvagaX9OwXxPT9usVy-foQPsnUdwD-5WzsIzKuVaxGBLS2PLuD8oUNWjZizr-dxfeLGYagV5igd7-yOp0H1I7gVG0vrvIY18f4P3AFNlWqQdKCbZ_JjLxyny66UYYIItSf2AunYT3iC4zV8Ph0cgt70OMLh3LBy7aMNYrELaLs4h1v-WsXFBSLu_aEQ0JGri8kR3zFxxW88VAfSd7wSZY0iNyOFTFrJ68mvCbM7JGk3qDaiSidf_QuLByJfCSvTFznTE73rTEDcEKMInSPIuwTR_rS2zfoyN46KrVDUGwr0HHan1AnKHz2st9qM9zmpW9aYMMW1MbC9XhYhqI5Ghn64stGAiWg92s9WQKmn8HbvXkWHzwIsmlrZVy3y2cqBI95lZkngZ1ihmHDoxcE1imRECKG1OG7SERblVbJi6fl5bOBH7-AIGbfCs-mLPbbMDX-ubdXf01As7iChWj7Cvu68IYQH1TpRFaYOFVPXjyr4z-ZYCdPqiBDn96iriEnSbJSqpObNjGIlTDJVOSLmDax_3Nqk2xBk9moMy9V3B0Zo91EqCKQWL8BzaKuMApQHc6dk-QcIlTY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdQTbtdh7OmzTg3UKU8VTnISrAFYUMJL69m088jskHRG8lmZ_P6SlvBFwVPl3vOIZNbqz_ncG8QJPtgqvQOE7l8j-8pFfQdh9uAoNOQb2dRi7WAaB8vSo_iIodaTJ61ftWBa3HWBsk22aGTbeBZi5tAPO2jn4q9jn5rzgipWH2QNdS7_EO8D1sXckio6kgpacUWzswTIisbikPb2lB3n-Oja_dfmEjZIPXstZDkz1AIoLrOL9-FF64XlfqAxXXcyNktmtY9Xt9ryZ1IauukE8q_JY4TNL7NyBGZaZQGC7loEcvAM2Znu-mCoRES1orozrq0cTLF57c0fl2Xdvx0BHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=kzQ4sCafileCoJpEGvuE9YCiEjPgW3cjEmRhrSIbSWwSjITBglbp2MDoGDBTIRaFQ1bnztJW5epb_eeJVE3AJ6kv0XZbm4zUytFSxizgmIUxz8BUescFWE3NDaa5DcUyNn-Qo05ETWjthZIESiEkd3hOiT1pNeVf7jJ6br6y6iu9psaSFcsIg_8MzBzXSyxkXXP3kw0pkNh3qw8_O_lhB8smgecSw8TKJVgCiV8QQeqOU6WmkvPWUtTaHSe-C0-_sM0eWoKhwPw6OCv8aOAE3J7vosWRrivk6dDysshVfkDQgGTbnW6SZni3FJRLLLK6D9ta2C5DNfB_gug3FJ_olSeOD58O5NuDScYOAOF74MZFt8lQx9U4sMklz_nVGCj1Fhd-3m8D2CMeyjTt72NueFWzIUuVaBjsaDLgE6XVmUkdwy9Y5hdRGxeQxsR3KSbh-ro2T28nymtchFTlQ_F32eo_pbTOHr0M1Z36ggZWoaFh_hY5_bIFJthXrToIHLOAoYPsklqvjbxcYLxavezyikTCxBXNHIOJifU7uCNOQk6wanswr7Jq-XRY5y3pGEzyi8wty1XgUlN3r5jpifeo_qOrI9qaGezI7X4-IKzU5JvPMdD6q248Zd_dt3abNB5Q4kbQ4se5aC_3uZJ9qNqR5-fJuVpNac-0A7A1kr5Q1v4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=kzQ4sCafileCoJpEGvuE9YCiEjPgW3cjEmRhrSIbSWwSjITBglbp2MDoGDBTIRaFQ1bnztJW5epb_eeJVE3AJ6kv0XZbm4zUytFSxizgmIUxz8BUescFWE3NDaa5DcUyNn-Qo05ETWjthZIESiEkd3hOiT1pNeVf7jJ6br6y6iu9psaSFcsIg_8MzBzXSyxkXXP3kw0pkNh3qw8_O_lhB8smgecSw8TKJVgCiV8QQeqOU6WmkvPWUtTaHSe-C0-_sM0eWoKhwPw6OCv8aOAE3J7vosWRrivk6dDysshVfkDQgGTbnW6SZni3FJRLLLK6D9ta2C5DNfB_gug3FJ_olSeOD58O5NuDScYOAOF74MZFt8lQx9U4sMklz_nVGCj1Fhd-3m8D2CMeyjTt72NueFWzIUuVaBjsaDLgE6XVmUkdwy9Y5hdRGxeQxsR3KSbh-ro2T28nymtchFTlQ_F32eo_pbTOHr0M1Z36ggZWoaFh_hY5_bIFJthXrToIHLOAoYPsklqvjbxcYLxavezyikTCxBXNHIOJifU7uCNOQk6wanswr7Jq-XRY5y3pGEzyi8wty1XgUlN3r5jpifeo_qOrI9qaGezI7X4-IKzU5JvPMdD6q248Zd_dt3abNB5Q4kbQ4se5aC_3uZJ9qNqR5-fJuVpNac-0A7A1kr5Q1v4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=HDjc6V54kh97Kzstbj7EpP2uZZKBiB7K4jUSsk8lu9yWR-HtNi-JQj408IK_sM5f1aur6mD4HAPqtu5e6kkA9O95Myd5hQuiCxBWseLglLCzfdjHIlNu1Jk6y8_mNrhTi6sVktwR3lZo0QSVW9kjwsvaTg3wL5J_b54cgP6YeBJVC2_cppEhqYJy6JzODyyBpxJPKp90PQd2q-PXqxIMzTMMi5hjyMkG3zNuhKJubK6n-hioxrNXa8Hp_KSpNqLeW-Zgh0yY9_VqYaLn31LOjhvzNxD8IfLvR13ItWFB3wWKrIaHlEa8MVSzVbB747aqs4xl-e5_fHMv1IHEXKSlfjco4Ct_Iwq_aombHXtCd-XPZGHf2lxEQfml14aLrX1VllGsrhgMYjk4-lydspHy2OHdC2lnWQDsyL8ogwEQffTWBYbryHXoygSDt9v7IetDCqzlV8jpltty6nMjeyNbMI3NcGf25CCL-mG1EjWEMfW-BqpTH__ot8AhdAigOWMlJ3HrataoG1ygbYXJXFrm5770pVYSP4gdwjgXS0Ltrgk8XGxpKpAMywUNv6dmwnLh6FZZsKWFEi1kQYHxCeBehhZ7ikDh5bp7sC8dMUYvBa3OMrPAeH_KTyd9KnvFYWjLbPEVjVXEe_TxgTZydjMyQWtmTSXxNAg8sBzQ90jDVpU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=HDjc6V54kh97Kzstbj7EpP2uZZKBiB7K4jUSsk8lu9yWR-HtNi-JQj408IK_sM5f1aur6mD4HAPqtu5e6kkA9O95Myd5hQuiCxBWseLglLCzfdjHIlNu1Jk6y8_mNrhTi6sVktwR3lZo0QSVW9kjwsvaTg3wL5J_b54cgP6YeBJVC2_cppEhqYJy6JzODyyBpxJPKp90PQd2q-PXqxIMzTMMi5hjyMkG3zNuhKJubK6n-hioxrNXa8Hp_KSpNqLeW-Zgh0yY9_VqYaLn31LOjhvzNxD8IfLvR13ItWFB3wWKrIaHlEa8MVSzVbB747aqs4xl-e5_fHMv1IHEXKSlfjco4Ct_Iwq_aombHXtCd-XPZGHf2lxEQfml14aLrX1VllGsrhgMYjk4-lydspHy2OHdC2lnWQDsyL8ogwEQffTWBYbryHXoygSDt9v7IetDCqzlV8jpltty6nMjeyNbMI3NcGf25CCL-mG1EjWEMfW-BqpTH__ot8AhdAigOWMlJ3HrataoG1ygbYXJXFrm5770pVYSP4gdwjgXS0Ltrgk8XGxpKpAMywUNv6dmwnLh6FZZsKWFEi1kQYHxCeBehhZ7ikDh5bp7sC8dMUYvBa3OMrPAeH_KTyd9KnvFYWjLbPEVjVXEe_TxgTZydjMyQWtmTSXxNAg8sBzQ90jDVpU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=fhYtEA7T3rmynIjV2zsJW5raC4Xf2aVphsNvVhfpGusPA6I5K32GmIFd18hUL2gfFL6VFKUJ-e5Sq1tYZHnhkxytZXxvaltjfcJarUFxn5lrUL4iXAxaSxpbXzfz0KX5VrwbQh9g3AGtFZWmM_K56CJnf8LgWcxBWwksWLWwpuIm-_zOVPijlc_7RysXloO0ipNj7yHiAUTfu5XpvvLXW0m-d_MyAF4BHPSopeG6rMVawFQ5KNdt50yRiLz4c1OmZ7_tosiK4dAs4t26V3QGgM-sy6AL0UASTZd2GaTe8uPs1UhiVM4Quc5EyR9wwKStyhja3rMw7j2CFbFAJduNsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=fhYtEA7T3rmynIjV2zsJW5raC4Xf2aVphsNvVhfpGusPA6I5K32GmIFd18hUL2gfFL6VFKUJ-e5Sq1tYZHnhkxytZXxvaltjfcJarUFxn5lrUL4iXAxaSxpbXzfz0KX5VrwbQh9g3AGtFZWmM_K56CJnf8LgWcxBWwksWLWwpuIm-_zOVPijlc_7RysXloO0ipNj7yHiAUTfu5XpvvLXW0m-d_MyAF4BHPSopeG6rMVawFQ5KNdt50yRiLz4c1OmZ7_tosiK4dAs4t26V3QGgM-sy6AL0UASTZd2GaTe8uPs1UhiVM4Quc5EyR9wwKStyhja3rMw7j2CFbFAJduNsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=jcZTea8NGLIaXUR88lzrBKJ0OtEdm-l7i5jcJT6qbzkl6-Pk6WYkUuehGysWRn3hRtjfMPQMjKcN4-DCDFs8gOHNfiVY1OqfPsk4ldNKJe8mGIxQ94Sd4bZX0nIs-LwIKBW1cBkgOUoUD9W_BqHH4gIsL-UYz3Z10WxsPDW1p7Qjedkhp8mbnU-SpiA8cuv070xTnTelk7OFUam-oHNOZePUxj3HMk3and2J2o5bEorcOnCev8SY2ZmGd8qOs84z3KG1OWPv_GrzYjxdbo3W1IqaDjd7FbjDpm4omIknLRScN70CbADPHeBT22fxB7vKTRFwphhf4PBgJlJrHSLItQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=jcZTea8NGLIaXUR88lzrBKJ0OtEdm-l7i5jcJT6qbzkl6-Pk6WYkUuehGysWRn3hRtjfMPQMjKcN4-DCDFs8gOHNfiVY1OqfPsk4ldNKJe8mGIxQ94Sd4bZX0nIs-LwIKBW1cBkgOUoUD9W_BqHH4gIsL-UYz3Z10WxsPDW1p7Qjedkhp8mbnU-SpiA8cuv070xTnTelk7OFUam-oHNOZePUxj3HMk3and2J2o5bEorcOnCev8SY2ZmGd8qOs84z3KG1OWPv_GrzYjxdbo3W1IqaDjd7FbjDpm4omIknLRScN70CbADPHeBT22fxB7vKTRFwphhf4PBgJlJrHSLItQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=s2BTumiQeiu24dhqCqCABKH2B3STM3H75B_DtcSD2X0Hy1PyANqFQVwyglTuzidgj11MuQxzJrr4o4SiH27Ejpld-yYCHjrFVZykLtPIkOo7j3GQpAojDPhjgG1CH7RnyylLrJIcKZbybPeXP6Hf0ZWE4Tms8rJL4aHrcLCKRMr0LwvhCUU0yZ5BnVENb0azYjoQVYULwt19i7sw8vM7QClEusFTb8-9igIhw-ExoXyKINwiyx3xjr3rPlvQAJ1jQglUScCQytFjmFgq6CGhhjrXCKzf9v0wKozubCe4X8LznMvWhpWk0jXGgy198QJ0Mtjud7oVT9Es0VAwIo9oAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=s2BTumiQeiu24dhqCqCABKH2B3STM3H75B_DtcSD2X0Hy1PyANqFQVwyglTuzidgj11MuQxzJrr4o4SiH27Ejpld-yYCHjrFVZykLtPIkOo7j3GQpAojDPhjgG1CH7RnyylLrJIcKZbybPeXP6Hf0ZWE4Tms8rJL4aHrcLCKRMr0LwvhCUU0yZ5BnVENb0azYjoQVYULwt19i7sw8vM7QClEusFTb8-9igIhw-ExoXyKINwiyx3xjr3rPlvQAJ1jQglUScCQytFjmFgq6CGhhjrXCKzf9v0wKozubCe4X8LznMvWhpWk0jXGgy198QJ0Mtjud7oVT9Es0VAwIo9oAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=h2C4ccVUxy8fK37E_2mupxa3wFn-2itpIa4gEAHMMvRJ0BZWA4NvNjDzfH0cfBLrgZxJMM76FmRl0vAxewg6rGwuh8c5w-JuGvLua8QMAFFHYzvF24MR-OqPMsJ8PKQlJQCyLvZWk3BlY08djsiQGUSlWjIepaakHynE2KfiPgwnUOek8P3baAM-g1_oYvUlF6EUl3LU2HWuWDBYeh55H1mVq2DAIFgDDqOe7HtFCzDR1nk9whJ-qqaXsRpNYdocy32krO-TlwPONeDStvZSwblnSXwM0J7to08X5pRHpBHEQRvZUsPKd00P-oRNf_llnUvZOBQc-JggOxKCSJOTig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=h2C4ccVUxy8fK37E_2mupxa3wFn-2itpIa4gEAHMMvRJ0BZWA4NvNjDzfH0cfBLrgZxJMM76FmRl0vAxewg6rGwuh8c5w-JuGvLua8QMAFFHYzvF24MR-OqPMsJ8PKQlJQCyLvZWk3BlY08djsiQGUSlWjIepaakHynE2KfiPgwnUOek8P3baAM-g1_oYvUlF6EUl3LU2HWuWDBYeh55H1mVq2DAIFgDDqOe7HtFCzDR1nk9whJ-qqaXsRpNYdocy32krO-TlwPONeDStvZSwblnSXwM0J7to08X5pRHpBHEQRvZUsPKd00P-oRNf_llnUvZOBQc-JggOxKCSJOTig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=vk2l6lTrlrIt_Tb050klH72o49Pmeayfqwhsu6K9lJpO_sMaUvXRZ48XmLQop0ke-Dlw3CmnPBMIzPETAJH7ZyJcw5kdzC4pciYza1OHbC9y3lDgoKGiqu_ps_WxGKlvwfHQ8vDMWVEOwrbexaiAuQF2YZln2gs-_kiC97QmHWsqEZ3HwHSbONinvIdjqo3gP8AWM8htXczD64U8Kdz1JonP_932afNCw1BzFOdZNQjb9Yutq2mcpXQ3-Cn-bVYCbIryqOnuSW2xdSvy8K1MQXH0DD7kovHPavS4jXogMzPyLkDQbDMjBvU_hPCQuesUoNkSnN8a7h5v3NOAn4Ztfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=vk2l6lTrlrIt_Tb050klH72o49Pmeayfqwhsu6K9lJpO_sMaUvXRZ48XmLQop0ke-Dlw3CmnPBMIzPETAJH7ZyJcw5kdzC4pciYza1OHbC9y3lDgoKGiqu_ps_WxGKlvwfHQ8vDMWVEOwrbexaiAuQF2YZln2gs-_kiC97QmHWsqEZ3HwHSbONinvIdjqo3gP8AWM8htXczD64U8Kdz1JonP_932afNCw1BzFOdZNQjb9Yutq2mcpXQ3-Cn-bVYCbIryqOnuSW2xdSvy8K1MQXH0DD7kovHPavS4jXogMzPyLkDQbDMjBvU_hPCQuesUoNkSnN8a7h5v3NOAn4Ztfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=SUYAq55n-oEWektYvmSMMzrWn-Ftte24t8bH1N_cScYXIErlnWzJbJE1SbMmEdx3TnG-QApJ9mNW0VyrtJXdjRaWFrYTWPdjmE5VK_EX3WNgvfA9Wx8fps8cVUXP4jnD7vc3f3EHJ9nUVmxeaLpTLCPq_yB4rnjRavFa1lQHbqyWhfmmvvdAD5o7yrDzfZu_t1nMhMERRZs0TQeskVDuIg5EbJs876qrxUevEY6mYg9S6lNUfTGt8gUCL0A7Y-8aZsdfLZEIXSD-t-Y1bxTNN1D5VPT7oO9y5g6PUbtIswMl9O6-K2f3Tx0ZDOZtDy8NUgQFfAxUSR7wtAn9EJk5Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=SUYAq55n-oEWektYvmSMMzrWn-Ftte24t8bH1N_cScYXIErlnWzJbJE1SbMmEdx3TnG-QApJ9mNW0VyrtJXdjRaWFrYTWPdjmE5VK_EX3WNgvfA9Wx8fps8cVUXP4jnD7vc3f3EHJ9nUVmxeaLpTLCPq_yB4rnjRavFa1lQHbqyWhfmmvvdAD5o7yrDzfZu_t1nMhMERRZs0TQeskVDuIg5EbJs876qrxUevEY6mYg9S6lNUfTGt8gUCL0A7Y-8aZsdfLZEIXSD-t-Y1bxTNN1D5VPT7oO9y5g6PUbtIswMl9O6-K2f3Tx0ZDOZtDy8NUgQFfAxUSR7wtAn9EJk5Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=XYFsTV2uBjjRcc7XvmA5zydcMgM-3r5aMsWxKjWWruQfBD9-gjyAQuumXG7esPumwbRjwG26Jjyc9H9kQvCOxMdpm_hBatry2sd_PgmQ9y63aupBrxPeKuRpDi5BMeYjTmPyrG1ysP7_UEOwXGU1gLJrVHOTblsk-tEN4gPtiZPyTNrkRipc4VJVTIGT6903LRq-sYQwu7ehZz53n4hB7ojj7MFnlfo6oIHqC1FsaPzonMyWMZIHlOBKiVmTKK18T18i6ghgKhMFyQH9oWGJesoDy_SWMDMSYbV1PTn2yeEQTpmE7kwdtfOAgxv8BJpqRStRL2kv1RhNLugyeJgfCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=XYFsTV2uBjjRcc7XvmA5zydcMgM-3r5aMsWxKjWWruQfBD9-gjyAQuumXG7esPumwbRjwG26Jjyc9H9kQvCOxMdpm_hBatry2sd_PgmQ9y63aupBrxPeKuRpDi5BMeYjTmPyrG1ysP7_UEOwXGU1gLJrVHOTblsk-tEN4gPtiZPyTNrkRipc4VJVTIGT6903LRq-sYQwu7ehZz53n4hB7ojj7MFnlfo6oIHqC1FsaPzonMyWMZIHlOBKiVmTKK18T18i6ghgKhMFyQH9oWGJesoDy_SWMDMSYbV1PTn2yeEQTpmE7kwdtfOAgxv8BJpqRStRL2kv1RhNLugyeJgfCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ubxb8FedJv-828eu0eLkKSAAItJEngl_G7uZWCSU4TYy9jMqWRz-dp2J0KLP5FQgK3YI78jcNOuuFRU_ZBP-JvvdQvZtlCeVAwpY34Xnul7hbYmHOUkYAnQinA0rcqALFtw_WPBqlYw4CIt5CHuCulBw2OrEeoI0HQQ7AKthDlXmQEcqkTtXsBX8Dp5FCXGME2dwx32FKYIfmDoQegrjRWx50qeaPfrNQioBR7KcSwpq4L1HjRnKIyNVJO7OLUigt9t2vfap23AwYx0Hq_cq_lvBvCur3elsjBwt3IvKcH82j5uK_AcffCmmnyS5QbTfL8qMEwo0Zw3PCjJEmwZHbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=q38zCq2SgT6Ftf9OYT98WotIuJNKfN1EssMNnngD3zdUrGLKiSqtcFoxK3GWQAM8C78bK9I7j6MVKpwkNkJxstSZ1jV_MTsbhPPqM9Dn4VlhRP_ExZCmYgVUPbHfaI-g6X-9yzMImFbBeocvBK4Y_Vatij3a994in4e38k-k1XYjxOl1_-wTxMe7OTD1LoIKHoWhMQhRfho8ZwSVe-PX6jbfuvd6CHjMSqRTFdWvrvWdqU_jZVWo3AgQ_JNJKl9Fbrp4GY0mKygO0R8833gVA_7nV2NEnxfdv9_RWWATmRjckOcmpUmsMuz4NoFRb7mS90RrPnxvWf9xLJH7B7VpRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=q38zCq2SgT6Ftf9OYT98WotIuJNKfN1EssMNnngD3zdUrGLKiSqtcFoxK3GWQAM8C78bK9I7j6MVKpwkNkJxstSZ1jV_MTsbhPPqM9Dn4VlhRP_ExZCmYgVUPbHfaI-g6X-9yzMImFbBeocvBK4Y_Vatij3a994in4e38k-k1XYjxOl1_-wTxMe7OTD1LoIKHoWhMQhRfho8ZwSVe-PX6jbfuvd6CHjMSqRTFdWvrvWdqU_jZVWo3AgQ_JNJKl9Fbrp4GY0mKygO0R8833gVA_7nV2NEnxfdv9_RWWATmRjckOcmpUmsMuz4NoFRb7mS90RrPnxvWf9xLJH7B7VpRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=VksyOHhoNgKGUd5tl8UaVe2xZcsOG-ERd5Gmu39j3fQ4rFwfNdvdjewehkXkmQC1F6Ykd8F2NXhcP1Afpu8wwmJAaNJYx5Tt4bbEuqa3RGcPf-x9ClNgcecgj7uwvAlgK4dQsxdGZ70hngb34L4h760WbxHYE7C7X30XjM1nLrVIu3GFyUSdPsODyfingHa3uMlogawXjYqSze1-y8RA-2hexgPo76cZfOAev7_4ppkFlHsEaAm205lkdTZK80SwjwEhdmKnrvPUsKbNaWA4wKWPk7aoHvKbwqbMMcDAi8mbpa2t1qpAr-PnLkq7HFqncBZNmYg0qkSEt4aJAT4SLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=VksyOHhoNgKGUd5tl8UaVe2xZcsOG-ERd5Gmu39j3fQ4rFwfNdvdjewehkXkmQC1F6Ykd8F2NXhcP1Afpu8wwmJAaNJYx5Tt4bbEuqa3RGcPf-x9ClNgcecgj7uwvAlgK4dQsxdGZ70hngb34L4h760WbxHYE7C7X30XjM1nLrVIu3GFyUSdPsODyfingHa3uMlogawXjYqSze1-y8RA-2hexgPo76cZfOAev7_4ppkFlHsEaAm205lkdTZK80SwjwEhdmKnrvPUsKbNaWA4wKWPk7aoHvKbwqbMMcDAi8mbpa2t1qpAr-PnLkq7HFqncBZNmYg0qkSEt4aJAT4SLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=QfAo8QqHzn3XCZsPL17Y-ZcSF7Tm2tin9zfgCIHVFchPFbP_9tpJNxZ3mgDJIu5IkeRFzIJzhRZW7SQP_WqVVFDz2C9rzwnmkqvjVhIozBaxog5CxZyDYQwNEpwoZ7laJnYraLPLprZeKwZrPEUJdDKHa-6g2-1QWq_WRiIHiD-4K4DEFCd-Q-rqcIUon6dbeDNlng2YFVhzKDZwP_bHFjIUUeIThRa2QWLM0pLlrvT-5fDYEn2Oq358uGx3p28y7o3xz6gPeqrty32FHjpFdtGPCF-XoIaKzHJuqS34sikDDP8TCeM9f-HabZ-uaMCU_Z49ijbmyiaGQ69YwMbQig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=QfAo8QqHzn3XCZsPL17Y-ZcSF7Tm2tin9zfgCIHVFchPFbP_9tpJNxZ3mgDJIu5IkeRFzIJzhRZW7SQP_WqVVFDz2C9rzwnmkqvjVhIozBaxog5CxZyDYQwNEpwoZ7laJnYraLPLprZeKwZrPEUJdDKHa-6g2-1QWq_WRiIHiD-4K4DEFCd-Q-rqcIUon6dbeDNlng2YFVhzKDZwP_bHFjIUUeIThRa2QWLM0pLlrvT-5fDYEn2Oq358uGx3p28y7o3xz6gPeqrty32FHjpFdtGPCF-XoIaKzHJuqS34sikDDP8TCeM9f-HabZ-uaMCU_Z49ijbmyiaGQ69YwMbQig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=tPmc5IreAOQ_gVRykecBi4ZJRzL0kjMkpWOxXjxpWTyqEIijuIVe0psabEHkfNPIZrf4yDXcxmBckl_fa5jjHSBWv6mYVCT4roijijFvvOG5c3iPhyozOS-DZZCdWOEepTUL3GtXaxRgCvYIDiRLtl_lZkFN1yxaE21a0c2hQ95AJJfj0y2ux9J79knclhtpWPTURDbCXDXwgrzEVw7DVAnYFV3j0BRDBTGsndcx9S-LkEDgvtzUaiwR2m2_kCDHxXZYFYyy7o_k-91eAK-R5YVwKufPCMvklLzDpeCIbnYKrx5Ma3fUiR-gwuO8HA12PsASxft3JG2guP5CDp6Lwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=tPmc5IreAOQ_gVRykecBi4ZJRzL0kjMkpWOxXjxpWTyqEIijuIVe0psabEHkfNPIZrf4yDXcxmBckl_fa5jjHSBWv6mYVCT4roijijFvvOG5c3iPhyozOS-DZZCdWOEepTUL3GtXaxRgCvYIDiRLtl_lZkFN1yxaE21a0c2hQ95AJJfj0y2ux9J79knclhtpWPTURDbCXDXwgrzEVw7DVAnYFV3j0BRDBTGsndcx9S-LkEDgvtzUaiwR2m2_kCDHxXZYFYyy7o_k-91eAK-R5YVwKufPCMvklLzDpeCIbnYKrx5Ma3fUiR-gwuO8HA12PsASxft3JG2guP5CDp6Lwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcN38kUlS_z77erUSA26m3dwBSG4sOPyYAg77Xmxp3l1KzluutzJEVTwHjTX6gWx_zfW1WolRLBtF0qdJY7Qo0p08jH9wonB4uvTrxGUBSyUnoO20Oo8PNgt6W6PgZCXZbugPOH05wbWK3BolRCMRL8uAqD-OuVTWtG5s-awq-a5VnrMrdUSr7y0cbMmv5_r9me4LpWyhxy-AQ8TFQUoR8mfVajm3iJ3WrNtwgd3WjomtXWjqda_I3IyiXMytDBVhDR4hWa8urzOUZllZjX039njrEci-6HudH4z1oKAPckTXEQ3C2aK5woBrO-eqMEtlDlMkwIGApaKYPWTZLPRXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=cwd0dYF5vkWMo2xvwiFdYbV8jSIucU1LB3EJxBl5Eg1Eu20vm19XpENYshtpFhkE5ue5TPSaQllxPu-CRuhffK4N8K3VNbCbMeOwrNCTnfcyImnppqOnDKUE3B_GWaQWy9TNd0j1-QF2wOORHoPq0ertgQ3j143iC0gtqVi9XXTg7ZioG2yr4ixL9Ndj3zTn74BnRoz7Xudwa6Y5yF1XZBPiHrX0bvt5dvrNgLGqUe7tmz9vi-CpZ0D-G67_ZnkmkG2Z_k8f4Q-SyQTUo3ojQNKwhgn6JrRVymgskmKxnaP9dczFW9heauUP88kmGTWBO3uouaqUQTH3fAEGKpfZ1TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=cwd0dYF5vkWMo2xvwiFdYbV8jSIucU1LB3EJxBl5Eg1Eu20vm19XpENYshtpFhkE5ue5TPSaQllxPu-CRuhffK4N8K3VNbCbMeOwrNCTnfcyImnppqOnDKUE3B_GWaQWy9TNd0j1-QF2wOORHoPq0ertgQ3j143iC0gtqVi9XXTg7ZioG2yr4ixL9Ndj3zTn74BnRoz7Xudwa6Y5yF1XZBPiHrX0bvt5dvrNgLGqUe7tmz9vi-CpZ0D-G67_ZnkmkG2Z_k8f4Q-SyQTUo3ojQNKwhgn6JrRVymgskmKxnaP9dczFW9heauUP88kmGTWBO3uouaqUQTH3fAEGKpfZ1TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=SP-2oEWK0JNiEFpOZNOPgXUu7eIXN-YXpFDlTzlWCRmkIyD_zKZf-BXuvej1C2zmUAUF0vC4TVJzcsW0IiFzLLvlydNDvjbSurOSVZlgrX1y263wrxAonGlKbtoyRzohoV-B7hOVsT8tqR9aaFQZn4LyntcNquQvAnmp1KnhXLUHVsQEM0Aip_MNUhnQnHI6aJZZE4I36VFsUAKVjzE4p0-jEBPZFaBEjqPXLFpHf7A1H60CPgQcb-B0y2hmp7z6GCJ7T6eh7AdUHJ_Z-T8zADQm-g0so03iozIAfbM96iuLUsYvOWF0qyUAMugewWkmkRg2cItQUPl-HCPR26-5_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=SP-2oEWK0JNiEFpOZNOPgXUu7eIXN-YXpFDlTzlWCRmkIyD_zKZf-BXuvej1C2zmUAUF0vC4TVJzcsW0IiFzLLvlydNDvjbSurOSVZlgrX1y263wrxAonGlKbtoyRzohoV-B7hOVsT8tqR9aaFQZn4LyntcNquQvAnmp1KnhXLUHVsQEM0Aip_MNUhnQnHI6aJZZE4I36VFsUAKVjzE4p0-jEBPZFaBEjqPXLFpHf7A1H60CPgQcb-B0y2hmp7z6GCJ7T6eh7AdUHJ_Z-T8zADQm-g0so03iozIAfbM96iuLUsYvOWF0qyUAMugewWkmkRg2cItQUPl-HCPR26-5_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PTeea0lCFUdpDhUR04qUGm-Hd3o5tyMLfvyHMZ3yXd75kEoPp6Mu00Zoyx3PQ0MQJP4IK_rRvhjNDJVv2HRnTJ4trNhx9pslKRuJBk4DzFhCeA5QT4kRCRkidYbS-fjkouGoO821GjdKGk4GBfio3me9mEXXVcMdjlVgnZ_tZYHpqOMohQrXHKnwvIYGtu-9h-uEKtwFgb-jElyuHY9hP_FdXCYMPsRNVInBfKWEgqg0OcPWn3tnAlYxHLbCJKNsdF1QZC1i7RCDG6q5MMVEbxQWm4zInjDVXWZ-a2poE4NmGP-p-oxdFftLdjYkhFXR4SZTUM33Sph0PjenzElu3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-oFWSIaILW4NrPXAFPkFsS6LPO4Z2-IWCnYWk-GsI3Ka_NOBRx0cJLOqctTTS6jRMmYpgGH0yQwVYvPImVXGYnDBCCNA3Dz96rLvYstR_Pk6O4KzXVeUdITqLA67PXLKHfvb8MFAH7dA2RW0OKXHWFlm6KCW_M28J2g6xSRiX9q0voTP03Z7DmhRISkSkOZfMYyPq1kAoF-PWWJegviuC91qRg73zXsKP5H6HiE_PZUFzACziJWr29MFSMfNTMqh3_CPiAjW-ZpNxX9IsQluZIRx8UpitujzB6Vq7-41Lzqpz6jIk6sONRnB38iQUUSoeaKLXKkhvW9pmBrFzzWdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=UcRng6_6G1FxY8Px93HYVJzryhirB5lZBhF_JiyRcZRXn543PJBLWF1w33h4hRzp2Qyfv8rWIc40opg7VhpoYAceroqS2eMCpaGgOXkLOcMfLenMpkOoynwM_-cdGd2jw9qllh7zTdcLWXqoUGPHZJj5sQxCvrcNXUImEXMhQ5rbAcBdNdLSeRS3AWc8mugaMoKETwf0-unE8XDlyAG20fgk5qezRVY6Zn2I402CmR1tuLlY3icNcMYv_MVVOJkZA8UTESkY5WSf5uzd5PHR5knWR5r9592sRbw1ZauqcVGK6wR6BRZjHRM_shqF7EyaMfIdN3Ztx034gVLFemiZNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=UcRng6_6G1FxY8Px93HYVJzryhirB5lZBhF_JiyRcZRXn543PJBLWF1w33h4hRzp2Qyfv8rWIc40opg7VhpoYAceroqS2eMCpaGgOXkLOcMfLenMpkOoynwM_-cdGd2jw9qllh7zTdcLWXqoUGPHZJj5sQxCvrcNXUImEXMhQ5rbAcBdNdLSeRS3AWc8mugaMoKETwf0-unE8XDlyAG20fgk5qezRVY6Zn2I402CmR1tuLlY3icNcMYv_MVVOJkZA8UTESkY5WSf5uzd5PHR5knWR5r9592sRbw1ZauqcVGK6wR6BRZjHRM_shqF7EyaMfIdN3Ztx034gVLFemiZNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJQcckhgZsqPmFEzUqWxHqUd7UulKpkEpTEW00U7QiSVeC8IJ7wkKY4HyJJdo495hzQI8jECXlvh7G6WRQpGSCs6kHxaEZ76TZmsxBLzkOkrgZPdWVfdiWXylu3kWpBvQ2PY1yKzjlUqc1Bg_OoRg8a6-te00HAyPFpK42Vued0IEY_Ziwv9nBtVQKas-4QNjDUBadRkNY_CDZ9vfVrNdj8fMeidIAMKOPuli2Xv3wwK4dYFS_yu2h8fsuXGQQPso0arJWwGiWOfflDbTqQU9YnNxqZajjR9tb2uN5vxwOr3_eC1ltb8XRhf0xqUGKsedALIjbL3mf4OoYUgfwQXlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJ-U0mXV3JGqRoOrSNR3Ms6CktGFIfOhICPrJT-TJ6ErY4xyPSDsNZfXVxbhuhbEKg-xYkf405KkRc5hYHkurU-11D4CRxCxvobKKk6u3ICsiVBpgBuWKpbMnO-W05FnfQNi5eAuCkaluWQ-EjfWwTP08ZviMC0_axQMe5QgkoKdLhR0yusDw7mJMwFpA4193abJHYzNOGLvShZpHpwS99lL8JO80YLxg8DI8FVD3frAtgxu11WD2O6HqjqgZ6uRK-1GYJIiXivYOfFpaQoYGI4zl7pAl4zlVJThmBu3PYUbzhfij_RBoLg8iw2bqJ7UffvDAixCFNj9jeUL2HsciA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuKPmJTX0J-onrk39fudv38QEHayBSbZ0-iECs7LrdPzI0Zv1GJdYVjvxBUNvvfEpM82uKdcD1uDJIOnzQqWHVqgZHBLdUprIkNkVU6JzcSlSHTQTuhf8WATq4vzjUjQCph4VlXBiURNGLNMzUa40VB4AwC148eA3DEh4vMVHiw4JbCOEOcHydo7Hm2PZjG-G0BPlBPEcsNy-B8s1lf5nbBW5_UJaVpgwlwCPyz_ja-BN9nBM2ioNcyj_G8DLVz4kNIqorhWMtIYeRL_j_VzriSxrkT9yoUkl0GyvHKGbch9tYMY2WxU8DDEUI_xoTliwiUZnBiaKHJG2CHpl5Cd0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=YYnaLrUQTnWc_eddxvPED0n3IiAWFjFxPQ17QAskdMKB01v18XgI1aLmjA7nq0aSKfpMGtlD8rN48hirSrXyuY0BHM26aH5oaSgk8YqILVLahv3-UVxrsAI5z_7zDn4tBAGXzrZUY7g2U_wS9sxDfmgbmnRUb1pKwgGP4E5qED3Y0GtW6TrUjgtixZ_eeAY6RlPqjgUEdKfgOH1RR-K3vHq6NRJWAalJ6JOAeie3OvrAscClyriREa1LOmc2O25zR3LZAH14CB9eBwOjFewAx38aoFMbJJWf4LF-9nNAjqIRKZFAEVE2SMk3a-OsimhwSspuzIdcGG95EKx9VwL-kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=YYnaLrUQTnWc_eddxvPED0n3IiAWFjFxPQ17QAskdMKB01v18XgI1aLmjA7nq0aSKfpMGtlD8rN48hirSrXyuY0BHM26aH5oaSgk8YqILVLahv3-UVxrsAI5z_7zDn4tBAGXzrZUY7g2U_wS9sxDfmgbmnRUb1pKwgGP4E5qED3Y0GtW6TrUjgtixZ_eeAY6RlPqjgUEdKfgOH1RR-K3vHq6NRJWAalJ6JOAeie3OvrAscClyriREa1LOmc2O25zR3LZAH14CB9eBwOjFewAx38aoFMbJJWf4LF-9nNAjqIRKZFAEVE2SMk3a-OsimhwSspuzIdcGG95EKx9VwL-kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=PrNWo0-PZXEm86iE9BHV-ZWi8MaOYLpTppiVEpIo5nvjh-k5Xk7JZLfcQVWD4zNl4_oFglSQl0G4kwhGawP6X9bMEhbbH8Fk0Umbbe5lKdEWW3y-9v-7UKUt9uK55OCWGXBuYjxVnKynO4W8tQDbe9ODfiJTQCAMRZT35SaZ5mlMrDCemi2Gp6YHmOAzXYuwnZMPANNFIRQ_A5NQm9RTBRXSA6S8MIPRnvjYcnMkMWFD5UAKJEkypMriNSSi6nLkIup3Ti-vEKFkOCY7YZoKGrN9SKixVDyrk1t8YqCVKWZq7xhH4Yx3LAMdjGkeAs3LP6zfTrA4n2_esQUE9Iv1cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=PrNWo0-PZXEm86iE9BHV-ZWi8MaOYLpTppiVEpIo5nvjh-k5Xk7JZLfcQVWD4zNl4_oFglSQl0G4kwhGawP6X9bMEhbbH8Fk0Umbbe5lKdEWW3y-9v-7UKUt9uK55OCWGXBuYjxVnKynO4W8tQDbe9ODfiJTQCAMRZT35SaZ5mlMrDCemi2Gp6YHmOAzXYuwnZMPANNFIRQ_A5NQm9RTBRXSA6S8MIPRnvjYcnMkMWFD5UAKJEkypMriNSSi6nLkIup3Ti-vEKFkOCY7YZoKGrN9SKixVDyrk1t8YqCVKWZq7xhH4Yx3LAMdjGkeAs3LP6zfTrA4n2_esQUE9Iv1cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=LZ386ip5WhJeg4UZYJx0zsWaQucEp_G1bg5dJCuEP5rXjfdNUG9KMmG19lF4udSMC7EfDZ4OxMFn2xHV_RWb-lfAnxt5WYMDyJMHzIju3RAmyk4mwRXgnVFe9krhrFaKzD9lXDkB9nAlLrIT68Pgq1Pyd8EG8s2wYaDRB-yGcIGAY9p1u6lKL5mG6tNiMeUAsQMS-ZoYT18RYnGROeIVJZ4S8hIjkd0LI0doQkNRlfCHWgVMTQcJC86vqQhhKZpgEUVAVxV61hUmqU_FVXt0kAHDc7WwCoxu3FYLDNPu9MgrXewXG5lZVR-afIAx_KNc1zdsGHoZOF5OdiLf0615IWjMDPrVRshnYX3ICW2EX8znRYaT4o11w0XJZWey2cCbFjSxu606nsX-n6gsu7RzaEVVT1q-nNTF0S6SbEwMDCL08lEIgL8H0SbkivKpXMWPwntIv_s6GEeXyDao3K_qh1_RH82uou12P5V9I4qzyCKcej6JFO7sQnWUhPpXwAZbL2fPikzXE9IHggcjafgGzrOcXNdO_iUYmSpDn3uXZzjZ-2Z8Jmau1TBeFkFhIwEj0MqXEMz_V-21zQl4ghq10P31tRnJFsNLn4mBk96hJ51w64ANwQukvbSSs90QeyZRj6otQZ9312uTwxAazpqbQhv-hK5gXU56sXhmtogGZ8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=LZ386ip5WhJeg4UZYJx0zsWaQucEp_G1bg5dJCuEP5rXjfdNUG9KMmG19lF4udSMC7EfDZ4OxMFn2xHV_RWb-lfAnxt5WYMDyJMHzIju3RAmyk4mwRXgnVFe9krhrFaKzD9lXDkB9nAlLrIT68Pgq1Pyd8EG8s2wYaDRB-yGcIGAY9p1u6lKL5mG6tNiMeUAsQMS-ZoYT18RYnGROeIVJZ4S8hIjkd0LI0doQkNRlfCHWgVMTQcJC86vqQhhKZpgEUVAVxV61hUmqU_FVXt0kAHDc7WwCoxu3FYLDNPu9MgrXewXG5lZVR-afIAx_KNc1zdsGHoZOF5OdiLf0615IWjMDPrVRshnYX3ICW2EX8znRYaT4o11w0XJZWey2cCbFjSxu606nsX-n6gsu7RzaEVVT1q-nNTF0S6SbEwMDCL08lEIgL8H0SbkivKpXMWPwntIv_s6GEeXyDao3K_qh1_RH82uou12P5V9I4qzyCKcej6JFO7sQnWUhPpXwAZbL2fPikzXE9IHggcjafgGzrOcXNdO_iUYmSpDn3uXZzjZ-2Z8Jmau1TBeFkFhIwEj0MqXEMz_V-21zQl4ghq10P31tRnJFsNLn4mBk96hJ51w64ANwQukvbSSs90QeyZRj6otQZ9312uTwxAazpqbQhv-hK5gXU56sXhmtogGZ8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=ghnOJbvduC73XUjDKPfdoaU9jPK0Uhrghg-_ub5KRNQwYWgehCAEzKRLQXtBeNaDA8tsicPV5Vd-qwMDM0DwwWEMF0ZMlb89ENbwbE_6yxGdymbLqdfcD6vy_lim7qSsJq4Mwon3dtJ39N7H97gOQbOX0nr9PH8aHAt8k1JoLKW76jfI7QzzirF23-CnFUdm1AcIwyFS77WZnKjRFstZIVf61o25ZShUSxBPZJb5LQyn8z44D9fqM4RYV6xx9vxZBAj1FdWjrVdp78nuwmOZu8UlODDLtN0XYMaPONg1fxJsJiH0XFIDM1n2jpDRQ6P-bzWxOKtaD7uG59c_ZxgHyleK5itsy-YCptzeVNVffIuhdanfkRZmj9g61hSYJmVOXdu4-2LJ9NpgSoQ-sPzPMYGgm-CS7ZKed7KYXluepunN4EerNQ30vB8H1V7rjltn8L9yct1t0xV1HrxtisGfV4mwW0gCJ8Wpn0KbnZVSJaT86FBtmP_BLTrVpsiCPIY6RBvRKZc1z36iiSGiLoYTGVKEUQAG9SOl9_GzcTgl4aKDb0-m4fepyKKzZHgqNyaE6iMZPB7QTdhsssdgkvJIrCRm3NkVbSkMu8UDu9AvcK2uvdvYSaO8XJEkb01Dy8QMVnuB3CMcdKfCcHHojaaRRJb-itH51q0VkOWw1qcjyE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=ghnOJbvduC73XUjDKPfdoaU9jPK0Uhrghg-_ub5KRNQwYWgehCAEzKRLQXtBeNaDA8tsicPV5Vd-qwMDM0DwwWEMF0ZMlb89ENbwbE_6yxGdymbLqdfcD6vy_lim7qSsJq4Mwon3dtJ39N7H97gOQbOX0nr9PH8aHAt8k1JoLKW76jfI7QzzirF23-CnFUdm1AcIwyFS77WZnKjRFstZIVf61o25ZShUSxBPZJb5LQyn8z44D9fqM4RYV6xx9vxZBAj1FdWjrVdp78nuwmOZu8UlODDLtN0XYMaPONg1fxJsJiH0XFIDM1n2jpDRQ6P-bzWxOKtaD7uG59c_ZxgHyleK5itsy-YCptzeVNVffIuhdanfkRZmj9g61hSYJmVOXdu4-2LJ9NpgSoQ-sPzPMYGgm-CS7ZKed7KYXluepunN4EerNQ30vB8H1V7rjltn8L9yct1t0xV1HrxtisGfV4mwW0gCJ8Wpn0KbnZVSJaT86FBtmP_BLTrVpsiCPIY6RBvRKZc1z36iiSGiLoYTGVKEUQAG9SOl9_GzcTgl4aKDb0-m4fepyKKzZHgqNyaE6iMZPB7QTdhsssdgkvJIrCRm3NkVbSkMu8UDu9AvcK2uvdvYSaO8XJEkb01Dy8QMVnuB3CMcdKfCcHHojaaRRJb-itH51q0VkOWw1qcjyE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=tSwxBbmGClS9RYBOxCBoXG9fhx3VlJqZuJaFw1zclZm3INzcxZYzeZg9kJYPZCJkQXYV-412bDQx7joTdn4g5cGBrC8so4LZXEvrK1bogcVgQni8u6nVuHI25kY3-2SUP34d9cFSnu05w-4usFf0lTaPGYrhS3v1GZXoPyTmpwWEx8rNzzSgdNeXw6QF7nZgcmh9QGW0aoaZWvto41_bTIbIiUNjD5mas9-jtqpClz8jESoEx6o0ITQNeuu6Q7LHClqbmSckDGZhATJ4NEcKkrIft5Jd6vWYKpnceQ2KgmeuCAHaWwEN2IeAV3qo6Hq2isiofPZTZBg4M_lOecks1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=tSwxBbmGClS9RYBOxCBoXG9fhx3VlJqZuJaFw1zclZm3INzcxZYzeZg9kJYPZCJkQXYV-412bDQx7joTdn4g5cGBrC8so4LZXEvrK1bogcVgQni8u6nVuHI25kY3-2SUP34d9cFSnu05w-4usFf0lTaPGYrhS3v1GZXoPyTmpwWEx8rNzzSgdNeXw6QF7nZgcmh9QGW0aoaZWvto41_bTIbIiUNjD5mas9-jtqpClz8jESoEx6o0ITQNeuu6Q7LHClqbmSckDGZhATJ4NEcKkrIft5Jd6vWYKpnceQ2KgmeuCAHaWwEN2IeAV3qo6Hq2isiofPZTZBg4M_lOecks1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1GgdCJ_8j_-guTn1y2snHol9fXj6XlxkGv4NhJQo59X5saplu5WdKt7uchYMcmbtTfP-WwBuT7Fxh-WbddvtXoxOJHNkJJo3YIaFlMPXYq877rK12pCX3-9q9s4jJ2cuYRfYbpfZsZ7_l_eHwYdRjPAUe2LAzx39r_3Qr0yEeGGq0Los6xQFP8NQNlDdjzC1Fhv3af7ogMxh92GwG0dERlAJNoAGcUZaILz1r-25zFD_cvK-uxnyi7vEZFk5QOfdu1uneMSEBN3k-S08A6g4dWGi_vlUEquD8_GsWbSDCARJ0vf2BwyrCXu7KnGRSgoxOnWiDwON0ZbQWlqYNJPtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=nqmjjqy8J2jpZ1cgJv-OMe4ivDF6O5RJ2xoEw7AhBhYvjVSkudjrGr1UG1vNPeRms56zjST2bM-a_g5GSoVI-En-N43qUIuBFMK25PKYP1eDluQnyMerF_JiHpgSERnRLkW06iHo0mBtxRbjKbnTS6938RmSjXBF91BVfnaNY24gHcI_6YFvLmBA-2udj9g5svXG3N-2p5NL4LxsO37QoKYg7K0oUasMePurNcupnREB76HqGdcIxM1xEM7C6SHGFzFWLNhh3oxd4cHv5Rz8qzSCASu4FLB2bLHg8YPzStSiO9OoHNrT84NYA30c1WN8wwpZ5j0Sw7-txiAZnoVRcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=nqmjjqy8J2jpZ1cgJv-OMe4ivDF6O5RJ2xoEw7AhBhYvjVSkudjrGr1UG1vNPeRms56zjST2bM-a_g5GSoVI-En-N43qUIuBFMK25PKYP1eDluQnyMerF_JiHpgSERnRLkW06iHo0mBtxRbjKbnTS6938RmSjXBF91BVfnaNY24gHcI_6YFvLmBA-2udj9g5svXG3N-2p5NL4LxsO37QoKYg7K0oUasMePurNcupnREB76HqGdcIxM1xEM7C6SHGFzFWLNhh3oxd4cHv5Rz8qzSCASu4FLB2bLHg8YPzStSiO9OoHNrT84NYA30c1WN8wwpZ5j0Sw7-txiAZnoVRcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=ZCNgcYBKwZc-umQJVBFFZ9olN2imy3MlPIbLnHO-WXB7N53RMfqpPE4iQoF_mRoEKflI1A6cc5waGCr1gY5dL_wnHfRa41BkSje7GuUtImHT8V76fwiS_LKm6e-yuW_7ubDEj8JIFpPgyBpMDhqxOngQf2J7nwTdx8oGTmcP5hzlbbLCAV-G64C0ZKzlOEWPNmheEjR5wtIVNzPNbfS0ENwSS0i779hNhnLAX3jr3Vcn_FIsIQVoPG9pi0FysU3b385IxTrlNAPmabPUG3QP8um4KNkwvWuqTWuAn6FcToLD0mgqRruAh4qNQFvcWnFEetrJnSW_3rD0_nF96BB1LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=ZCNgcYBKwZc-umQJVBFFZ9olN2imy3MlPIbLnHO-WXB7N53RMfqpPE4iQoF_mRoEKflI1A6cc5waGCr1gY5dL_wnHfRa41BkSje7GuUtImHT8V76fwiS_LKm6e-yuW_7ubDEj8JIFpPgyBpMDhqxOngQf2J7nwTdx8oGTmcP5hzlbbLCAV-G64C0ZKzlOEWPNmheEjR5wtIVNzPNbfS0ENwSS0i779hNhnLAX3jr3Vcn_FIsIQVoPG9pi0FysU3b385IxTrlNAPmabPUG3QP8um4KNkwvWuqTWuAn6FcToLD0mgqRruAh4qNQFvcWnFEetrJnSW_3rD0_nF96BB1LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plI2kh3dODBvARScc_oHBxfrhW7YwrJx07EB1SloNZuSqg8gJ3bMAI-6YFWhGMxHCM7AIWcjv96Se0ncrfyCDQukxcGAHNhzS0Gb_xR9SnfntV0_M2_nZAH3vxVr1EFETdSrHYxSq3nvErZq5BxLdd-A5LwQo1uWCHoXlSNgjzC5xXO5pdJnpb_bJYfO2dlKID-BeiMK9bBJ1A8haYBMzrunzYl-GGuG4oshGgpc7w1tI7zElj6ikLbWUrIgFTxo0HkfiKnSVmtwy4AE_DHRgL9Sqrk0M_-UINhTNHYK0HnO9qnMOiX-LX5udV9zWg0kXvMsoMD25Lw3Zt-iS9mrZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0nQzvx7t9x3uzC3SaCRznaeaSTlDGKAZdqGk0M_F68lORK1JYWmatYNPz8OcBDIF2jLVpAJHp4Ci087dvyK0Y_yZnMyCIWykyUO8yvtBQIClTS0Yad61IJQFs-ke88SrAm9887RsBjlnnNZMosrhgGYpkkBBBUlBUbIJZUOo_pknBF7kT2v4WVNjCvTVmkZr_i9t91CnANwSGMM79Xn-8psIiyymrfNOHk2cSwQnapkuNXh7YosZLGGaJ9ffeTemUYP8I1Q8KGOOjjLS4zCuj-jJLCAceS21y_upLUfnz8o9AlBhQZt-GrHPtS-Ut1agUbpshgSukVGdRx6n2Qzdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSncEHHwPu5qgCKPQENTTaDDO2Nj81AmtnK8w3huex1BzDffT9TfbT8BlemsONXAVFtGR9RM85jQ2XB1RNMM09i_V7uAiVoszr24gXqDUVVO05iXNXRO8qswgyYao6v_J_oGFqrxE8VPLAAClWXlscoKxOkfDsv7dJedn8KIhr9akHfNRl_9PiW2RFk_PQd4jVFlq2bHlmsq7gxJVcdTHF5Y2xYxkorV3hA1ryEJ1GTFkvu7JO90EDgiQKTlySqIm3NnO8a981syV73fnfsDfIvHnvhTEVKBjhKMEDuFe8whEDJN22PkLr7-wCDUDfLrJuaeoyERlNb5UQS9BmakoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvHGqK5YGxwIy7l6vhSu8P-h9uxdJEqIp3OTPoXfcPPKQiTaVEDLVwDM0ulNr2o2ytlw1zXGMVQ52OT8CB1v-KFRb4nw_vU4odA9Rt4io80j9Bkutis_WRtxiBUh3Y7zJQtPvfh_hXIkJK9j0vTtI9LNzXDJO4Dy12USi--fTkprVEkXR_N8Cgz325gatfV73yGPN4JEPP8nHU8iipvFL7p--xgYjCLi6WUKQrLi-usl6bUD6odpYPtbUnlWk8I8nW95h2kxCEdn3xdFPakI3TznSL4HDgXxJiQp03vLQPz4kktmG7G4pXsTykFG7jOHs4wwm93QV0VRxE2qMFISNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byNr8OD1bomCKk904or32gj5zeViQoIusC53c2F6fHz6D_ZXZad3N0fMCxRPrhXgamorlsQ1PI2UteouV31oyzJEUUvVAJoio9cBT-NL9J5Ponc14BPAhWylogbLieaZU49iFcMfRtpBKp48_Cin5ptU9hIrj6P57hPvduhC7_FXSNIMsbPvykcBNji8vFXJsv6O87_xyVh8DKCkYMglmnBX2QIsqlqcgLMRpNwl2luBnueEpeesZHFe-yqd6vFjOrmhzi_NstvuFyOMWQC-pksA4aKrNnpDWfFU7KkPxuJobOru8-kHEvo5OyHONCIxeNttIg0s-YyzVIU3EHyAzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o501p9Z9r28EC4M9P0__HOhHE9MPquBIT8BnyFWgug4-wJWSdwtojf8n0sopircUZxLxvA2d-m2swuitWWzuLXNG_9Bjq5KdUZ1sWSLsFSQ0pY1NGAqY0KX4G8sMbW1F8nftsRUL71ii5wKX5GSIREZLLkOp6v5Ju_Immzvt61hiipgAK0HDGEVP9-jTjL17Z5OZrotX1ldSM3iwlxP38OZpnpdj7mJdFuvbhXLM6NSWmyCbzfVkai5BjrDh9yQBRds5GAJYMOemhzLsPzpEtI-NthJmakbcRXWEXYCJSTThYHItYucatUiAbWwaAssbUU_m3zS0DvWfA6Pbq1b08g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pN4KcWi2t11rYrlnDHQtms_pYh9yYxis-sVNBf7cwnA6gmoo-qJ87yZ2Id9oexFkMdTBY57-aVBPIg6fTZTJs0t6HjHs3iIF-nAmsjL__qwlr1XZwt9-CXvoegO-mftyEyikUG1_1qo7BJhKLggS2Iy-cEraU6xr2rdv76PYItB9rZbSRFAzihoQ2HSqYtgJ3NkSKUsSCksfeFESI12dye7gCBU-X70iSSG5M-HkhEQzCFhzmpwoQMo6ByrWcJqVEzt5Psd4Mk7B-6ru9e3G-pgOtZ1OVJE3mV0au5g-YkA9W2KO6s256iTdu2LUh5YsshjBQwI0_oh7QbcrM0PShw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7PmInZNi-luWd1NKrsX0C4UQcxrlAvtm3sTDBlQyZ9YCL-GHT6CJuFOsMd-8vAgSSGNRvpOCaf_jciMNmTeC4wjfTtin3OzxLJY-rUnIvmJjsLlWvJmEop4vieKrdlPVMq-Q4VTAB4-2Y7fbhshD0Yj3dSQvFBo-BCvDVGIzQMQQauJ6Bn6To0epwPXdf-WgDaTiOGdf0yayZjKC1cU_FgvfxTSFPFI9icy0qc8HHf59bP6RKlWfFsCf84ZtPEluWVwmuyLK-ld0iYTY2aQt9dgjDisqylXq5OdjdnI9ra0Mj8BqHC4g9iB01yvjkA8WV_A0gXe4Uy-eZP9gkzfpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tqdiAthdRGyA3If-sfvhW7K8Omeq-e413XiCctA5PMYZ7fjkK23RBKRPNDKz6oWLracm89SJAhgWKYAxkb_DalcIwzPC7xAty9otMF_484GPBDeFWDIAtMuPpx8vbVMXWY3zkCxIGZgMD8Obi6ujD8DyZeJMT5-vnbi5s0NhrSUjlIE9tf8AuMihayWOXbZ6idCLkMDzxjcsIz91BJ7Gt895j5blnEPCk4lQksrk_tDUKNQgUNm10E9CXuXJtKTxZiJdRfrHSiTrmuqFzdg8utp1nNycOFyEZ3f1Z3ooDDE7nLmHsN0IwQ29oZm-KSzJsmCoaI0_o3UbptkeLbW7UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dRoti6onbZvv4y1KJPo_aqfsjpjBdAoWboPqP3Xp6zJgw-VfSakPdeRYZSPJp9UunrpePNRZE5xp6zsWmVBf2suhkanxS7PdcksMONmSOjRHBOaSX5vWZgKC3-6adsF5YRRKCVAIPyO9iomB_CMbhZNdDL5K2q7H6jlXhsAgo7xyoxWEc2iuHXTvPd28TyWslZH1SusG8SfhkwYKsOXzOSq4vEQPpRtQHwD89qJEdi8vm0Wy5oZ2fy6e0-eVX1i-i8OtyMTr-DiHh9oBChUWxDGCTIweBm_wZ18d9sJHTmm5zEW_Rpdiu3QMcSbutLwBCcfRf0psToYjaph_RQEaCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=VdFQUXIWKNZt1AWdQEfjjelrLi8p7sdFQ7BAvJXGNznSupX-Y7i4BEZfVyjgZZKS7W08tY4jd5I481N9trX6c9TH7qlCK_64BdKAWFtTYktUp1Eihs_xAicfNIwCBWQnlaOE0b4QXLlMipuSyX0t6whfZ16PwDQQ7djT3Hlzl4GJDnRzSFxBJ8sbhdwCMkSjCvwe4IHaPRLZQgHKLBiBQVKHlGEkLmmsyhPUs1WiSJ0RA1EaG9jqhuv5VrBBS07Kdjyy8RrrmKpVmZe06bcEedvr8qsFS_6kiH6YqSQsIaLg4v_9yn-nZ8cbNAx9fUlHTWwRiMmi7CgvFldDIht1sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=VdFQUXIWKNZt1AWdQEfjjelrLi8p7sdFQ7BAvJXGNznSupX-Y7i4BEZfVyjgZZKS7W08tY4jd5I481N9trX6c9TH7qlCK_64BdKAWFtTYktUp1Eihs_xAicfNIwCBWQnlaOE0b4QXLlMipuSyX0t6whfZ16PwDQQ7djT3Hlzl4GJDnRzSFxBJ8sbhdwCMkSjCvwe4IHaPRLZQgHKLBiBQVKHlGEkLmmsyhPUs1WiSJ0RA1EaG9jqhuv5VrBBS07Kdjyy8RrrmKpVmZe06bcEedvr8qsFS_6kiH6YqSQsIaLg4v_9yn-nZ8cbNAx9fUlHTWwRiMmi7CgvFldDIht1sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDYNWeROU5lcKmlemaNaGUiLACRoBripsU8MCBFhCDq6h1ZsKOq2FGUGOxZlLjH4Ek5sXCux50ZR4i0xhVq5q0vl41t2xRN5iFsd4l9v_Obeg4s086b2L_AvZ1prCq4y2qUpZJ5p6-EI75fraQ9ZTaMq9SPGHwkbybQzjvUqVTaVDVIz96PmOlD1l_NlwAZcsDzUEUqyF8XTUwD6V3whKQ9PRQl_VS4MZRXI3uVW8eJG8qZxOtqiuGM-BqaYJl7A9qrUUk0bmAXqxHe1Uu3HTId0pltGQ-r5pb2T1-ss11Cm5S04XoooS_ecy5lNBejrFtg-t5S73iP7sT2Ezx8kdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJ9dbGNlUVq8AAJ2rgs6SSifCulfzwZ2HBSSH4KD5xYCg7SMzTRqqy5kW6yjAZsdyqITqlfVg4v8UrZP4_2dUsbVoPSaTgDHA-36r3nM2reju4sbi-SuGTIgvEeh9AanYXEh8s0KTg_xKkVGmjteGyAOHzgIeTF2yQJI18RoLwptFj49gLBQKdEaWHooHyU-thZJfX7TH-wruVz8R_Sdk-t9WU1VW_BHeMb2ny40Ubbfm9cig8PeRSbzzPDd2HOtzqZmrIIwyaTgaW_GnjAQgIjjZlXwE7hWXcgcIEzhlTlUL1JKvreTtxhjV5OAfPh2iHAvYbnTuAiOE2RWTDD3cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=dmVYtnhzoeBY_nVm9J0WPX5lpbC8GHrPoxTeyBzokcDI_XCXrH-iBsk6tX9VxkPeeugC_BiYDuFU_B5dKpLCxvfYUK7K7aziFZbyn9yeDvRP1eqz5Iym8UT-ZxEXn5nGBhZrT091rSY6W681_13Jb3VPD_aSFEwI4Y0fNBmQAf3wksQd244AU204gF_VxeUnpRuOnbVUZ3qL7NgFSDqaiIi-oIyJzLCymiM5dVvCN43oO-tC2DerYcOySgAUYJbwGv8XFZt7gg5C7Mj7Eor0Z1NvGLpPyarnLWVYJTm0ri0nQK3IlzxbnrIPzYAA60qkrQPiYCqfFE9ip0H4e2OGpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=dmVYtnhzoeBY_nVm9J0WPX5lpbC8GHrPoxTeyBzokcDI_XCXrH-iBsk6tX9VxkPeeugC_BiYDuFU_B5dKpLCxvfYUK7K7aziFZbyn9yeDvRP1eqz5Iym8UT-ZxEXn5nGBhZrT091rSY6W681_13Jb3VPD_aSFEwI4Y0fNBmQAf3wksQd244AU204gF_VxeUnpRuOnbVUZ3qL7NgFSDqaiIi-oIyJzLCymiM5dVvCN43oO-tC2DerYcOySgAUYJbwGv8XFZt7gg5C7Mj7Eor0Z1NvGLpPyarnLWVYJTm0ri0nQK3IlzxbnrIPzYAA60qkrQPiYCqfFE9ip0H4e2OGpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=XLLoPI9vsGHAVDN0thyARq64myjah80ibE-vsErGmxo-6omH_pKN93qMRVJSg5FdQ7I3Ztc3HM9CgQw9ebKg2bjTGjOBGvAFCCSydCNsmNzDOZJtVzJKDKZup9MPBrGk8FE0QGuU-hTfgwh7vRwhg3ijOngvXqyv0pvOxfmv6rbiNaEL4R-rsFdxAIUc2HQdYPn1FThVLjd3pWK8rmfumtJRCV2tA1sW0JWz5XybvRNSzHh89H1Yc1yR7OdPUmYqKXUv-PAWpjnzxAJBLMoMUSRKRL2db4tPKPbsI6XAeW5sWh93fjbBFSBK7jmP4-8PFRLSQkL1FHx0gEQqHiR8HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=XLLoPI9vsGHAVDN0thyARq64myjah80ibE-vsErGmxo-6omH_pKN93qMRVJSg5FdQ7I3Ztc3HM9CgQw9ebKg2bjTGjOBGvAFCCSydCNsmNzDOZJtVzJKDKZup9MPBrGk8FE0QGuU-hTfgwh7vRwhg3ijOngvXqyv0pvOxfmv6rbiNaEL4R-rsFdxAIUc2HQdYPn1FThVLjd3pWK8rmfumtJRCV2tA1sW0JWz5XybvRNSzHh89H1Yc1yR7OdPUmYqKXUv-PAWpjnzxAJBLMoMUSRKRL2db4tPKPbsI6XAeW5sWh93fjbBFSBK7jmP4-8PFRLSQkL1FHx0gEQqHiR8HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceAFvY4bKYNOqXY2HcHHqwaJMu7IEEhg3m7VNEvZSTlkCOTSMcs5GZYRVERqrGanusr8WGO07QpAnkHGi5mkG6i1IDiRdBcBxtidmvwRdjSVwA3gIGrlB2hmKbJx-aerVMUDVRkQ1bAg-RKzHptrHE_4I6Rdj7SJgvGli4NY-NsvOk6DVbe2WVlummytJyoz2eYpo0MTSzA7ykrLKIvWmi_fgDsTjhmjzxkC3iqYV3D3Nj5oDFXvlLppK6iJKsnQK8Zaa15U6Kq45KbUl5Ih-B745u_dq_GRoWPRXQd-DMPGsL1SMHpCm-dr52j56k9AlWvoVsbN5r0RbNLj2i0bAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJLDdwV7UAELK6s5yrXN1wx3kgAj9LOYwaMMa59XdW6uYJBb1Y8a83uAtVYgyzDd_I21i-fH2v0i-SkfH_lhcNaBWOokp2cD-Mgv1A4jOkbvOuM5ZXJ-6KubSS5I56LnP8KojZ0dODGtOuXtMjm8xwXBr_KUzDTeFAgNHEHDn63yQuKb2gpvmegstrAqrsMeKHPDCsvZjil4gcrePRDoHmjwwM_UIGvjSVRfuc15zOkC_ZoilGd0S2wH8p7d5msP-MU_m7SXuQPkUuyGB1Y7LTlgfP0R8n8nmy-FzaSGbn_GpO1Yz_AsdKkKDwakBA0aBnHjGzEaDoyNGabixw1mxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GehyRnXdqqZ9egL3HLZI0Q6VkwmZwuwoY8VQK0Tdk86s1CphthVbJX0AETfNziA-TjXVLR_9HvDMTIVa2qF3fjL3KLhQBImiBPnlPyOH8Qpb-y14rUwHznrfSla5fiGO_WkDJVZExIzpK8j2EJZXxdfx8TMDjjb03bQnzrqG6RBpmyG2m1J8nmdvZpH5s1RHTd558dhLUU0nSqje49_wtR19jo2xVs63tH_R93nLnLFy_gk4NYicqSP-2GmxpXRZ0UN8NsxX13gEOaOZcix7QosBAxtDxsYs_4ncC2dzbVSmFEvYRgZUd0CYWI7Vcuq3sZYy9Rd9yGOVz7hgmjOjLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
