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
<img src="https://cdn4.telesco.pe/file/rwRXE1YMoSXfC3MCErMvgNjK2GwHN0_EXer3tsTz3_mxciHhyoE8kfc-KZA3-h3z1P3H3FdaFH4DJJnU_8DAfDFKQ6ZZ8sqzm41S_URoeYDOKH_dlgqo1R0R3X3nBlGHaM3VMvYB94R59THqH9_dpVY8EGFjMM66JF9xpkbW2NNH_sKSAMrninP45rSflDU0UL4tbc4OsQGs88TfuPUJanoHK0Cy0x4TOe1vOoL-OlCWSjQzt0SgH_wjUuUpLXLpnXTKCG1ogteTACxxo-qn6Y3SWHuj5ei3o48Sr3sI2WXPBBvaHKBk1kZUP74gp8oj0M2vKZPCKoREWKqDfyC8aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 08:49:22</div>
<hr>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVI-IOdvEAZx6-9-CopNdi5IZCOxhXNsw9SnoT5dEYcsf9LtT8Qg0FWn8moSQL__-sE2n0qhox37_dHUgn1F_IfWlunkm3PG4FYSvEMuF7XxdUof_lNIYqxkCDGHcLmnmKgPWmcEbjmz5i3FTWHacDdbnwFFGhqTmVOzbxKuYy7fy5lAQsXGQ6UE6oWFMZjzxUI3RIqZSvY3y_1IKMvtq-eRuEUJ7cmtY-TdqbvA-u4fsj8-q4qFKl3nRLLQEYfQrKKeB4rh3vvcrntoXfSsAbcd3tSj68IvWLIM55HLMm2AjaAZ60w_qR0XT88G3iZJkU2W7rAyx97I1X6YvIQrSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر
و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)
که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار کند است.،
🔺
خلیفه بن حمد از اقدام پسرش برآشفت
و این اقدام را «غاصبانه» خواند.
در سال ۲۰۰۴ با یکدیگر مصالحه کردند.</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farahmand_alipour/6043" target="_blank">📅 08:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b23JA1V-CUObD6TwsH0RRZ5uUMT3GPFPlu8-Ear75DGj3Dify3JlWq8Pl8-QxvZXuUgcw0tQb-3Hjt8QDWru6E6a-YCBxcDtcSptuUZWy8I5yHtbAWx5m6cRcP2WXFd35rF3YAZ2jw1fIwR11r8q_iZ1FbVInjo3zu12LOhg6uQqFHka6XRpBEB2BNC86F7q-1MCzjuqTeBHf94Ui8gTdFXCzs9R4KUBPeV4fQU0FnYyv1JQheOE4zzsFokjQ3_-rWVB4UagcPau8qToGGQ1SOKEfDbnAm_kZ6huOR424klAvZAD5pN2yjmCbJu2AshOo03ovnPRIKhYmCehAAI32A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kmu9B_s9vTvyGj2zrTe2Se3chjW2pVp_c2Bn-1El-QP9_jMVDGuE8_juGijtDpMgRtXTEQnvMhxqeCIt2l-5hb5cq5AwyewDBxzvb1uqXXDBbmKBkSxT7-Pu4ApO654kjS1l8LwE2_d0RGI4Y47P35pSif4QVhBQlK7Tfy3ApU0b7jtfRRcD2X8nfBk8rmssW4K96l51gzutnV3p3QnINZEIsDH6eP0ZEpnMUEDm-h85JtuCMMxclxDhNWztnwbXFB_9vSJQc_QPt2iqGkwzsP2TkW-EESCrmodrHUzBt0WQqiUEs93kL8FOaJD-GwGEoiYlKhvvtkuKirTpS-JJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=cZLuP9V2_XSRxmGZpnEvA-VvgXEoV2kqzvFn8YMZDPooamEs8IE0tWvNUlf5TRW96ONOfwjbFXAjPiqgkSb4RwNgKb48Xktq-n94w4yS4ZwhstuseoEMZJD1xuksITDTJEPQKhbD2aYXwObvdaL4wmTmkVI_anshkcClHLC4J-AICkaD8xLQsL4XKvGZZc64yaVdSJliuPA9EvOrU10odOIGxuc1lhukEzz_viNkl1OQX_EXcUsFfZQZt-dI7G-iPPwBKn7n_8Zl1duy02WTCN3c4YIJbHDVi7ObAPsh4Uy5TvAUeSDJsVt8b8L030TiOPiNXktGXAGMd5ChWt2x1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=cZLuP9V2_XSRxmGZpnEvA-VvgXEoV2kqzvFn8YMZDPooamEs8IE0tWvNUlf5TRW96ONOfwjbFXAjPiqgkSb4RwNgKb48Xktq-n94w4yS4ZwhstuseoEMZJD1xuksITDTJEPQKhbD2aYXwObvdaL4wmTmkVI_anshkcClHLC4J-AICkaD8xLQsL4XKvGZZc64yaVdSJliuPA9EvOrU10odOIGxuc1lhukEzz_viNkl1OQX_EXcUsFfZQZt-dI7G-iPPwBKn7n_8Zl1duy02WTCN3c4YIJbHDVi7ObAPsh4Uy5TvAUeSDJsVt8b8L030TiOPiNXktGXAGMd5ChWt2x1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
سپاه: تنگه هرمز بسته شد / به سمت یک کشتی موشک شلیک کردیم.
در بیانه دقایق پیش سپاه آمده است که : «در اطلاعیه قبلی گفته بودیم تعیین مسیر غیرقانونی حرکت کشتی ها در تنگه هرمز، برخورد قاطع ما را به دنبال خواهد داشت.
ساعاتی قبل، این تذکرات نادیده گرفته شد و
چند کشتی تلاش کردند از مسیر غیرمصوب حرکت کنند
و به اخطارها و تذکرات ما در اصلاح مسیر و حرکت در مسیر مصوب بی اعتنایی کردند.
به ناچار یک فروند از کشتی‌ها مورد اصابت شلیک‌ِاخطار واقع و متوقف شد
.»
🔺
جمهوری اسلامی به زور میخواهد که کشتی‌ها از مسیر آبی ایران از تنگه هرمز عبور کنند و نه از مسیر آبی
عمان.
🔺
آمریکا از جمهوری اسلامی خواسته بود که شنبه - که دقایقی پیش تمام شد - ‌به روشنی و علنی اعلام کند که تنگه هرمز برای عبور و مرور باز است، ج‌ا اما دقایقی پیش آنر‌ا بست
.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6031" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuF20fyARGEKCUWi3BNM_a9jOooamRFNPR0rkC4bTEIwC1O5OLccf8jEJCveW_aaaL4rPV7IVqykbQBaDePx6O2w_selBi3s0LUzCY6iS_e0vYW4K_WktYSqd8NLtFs6e1xbec6GgaJdblmuW8QQ2xfT0rgUO_ptyJowHZqohokwT99DtdbKwCKV8zoOfrUWnHm3iF0UYdHDjyU5ZHhQCAhHi0128BlV7_0sc357IiUBjrCPegTkMvPrR20dVBXwYv9xP3koRWGJtR-YvcaUBvF4Hk-iFgnR8k6-zJMZFoBU9eUKsod0cC50dZYIFF-NjaZtRZ9vgjbSphd8I67RFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=r26ne6TvbHHd98cDEEenuw3JKy-pzc1C_M2JcywUfLFPklxKo_xEXfE34RlleeOEIKXnbq8LvyMv7llNRaLbs6dRhYHGKsTqby-tBUb7cHwatkPeCoaTEaY99WUG-BLjbCEptfn0MBjVmw2w4BMKXbh5dpRY-IwilZc4QHRdBYMQtsrVOV4dkR-F1nS_steNmxfW6o6CY4LnVDBNDAVBACSMLhQLNO7Bwl2pNw8OZkCoOSePk7nQltMYfwQBN1-fspAqsUMGzlcEhhNbtql_4t-byO825LcgF114DCnwXi10uFZZCzLT79xYxpw7T_wAy0xHVqVY70F-BO_dO8JwHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=r26ne6TvbHHd98cDEEenuw3JKy-pzc1C_M2JcywUfLFPklxKo_xEXfE34RlleeOEIKXnbq8LvyMv7llNRaLbs6dRhYHGKsTqby-tBUb7cHwatkPeCoaTEaY99WUG-BLjbCEptfn0MBjVmw2w4BMKXbh5dpRY-IwilZc4QHRdBYMQtsrVOV4dkR-F1nS_steNmxfW6o6CY4LnVDBNDAVBACSMLhQLNO7Bwl2pNw8OZkCoOSePk7nQltMYfwQBN1-fspAqsUMGzlcEhhNbtql_4t-byO825LcgF114DCnwXi10uFZZCzLT79xYxpw7T_wAy0xHVqVY70F-BO_dO8JwHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvig1ayycEUO61gbGKyWPQwWAgtEOIUfc7dj6Uvm8TZGIc-ut-VHA1cGNpDjTZ_GT4inGe5rvqItsMgPqX1UP67NnLkk5_eNMvIc1Tj2WmTL0M6UpW1EcThYla5kK8PAExzocn8pRk-yMknNceJY2yPjjrrW2NagUfO73k1AbIKW0Pk3HFQouvCChpGX6GplhTqiXkcXt62csvBIiRW0X99vVj9H6s4_vNsFAbUILs-CCckIuo8WZ8wCKWOhcC-is2uC283a9dJmWV47SlGkoUo_YdAj_kj987RnHWDMuXJosE0k26QNrBDvzWC9M5H3ZHyUDKn8R7ocAsJ2ynzK2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2wkjnFFYSVLJW15uFIllcIY9Hr80JsZJObJ_zS_d0dY5c3k_F7S6twNyo619DnxB4hfYYVqigNEh6FzUBXvgLdLJm4Wh0P9zhS6rIw9-AtZsOcVOWk_ZypNnHEhXtDJd_Sr8lwkAw1HNqPVIPBDb24w6axNW3__btmlZwBxU_gPvmqJWjDUq1GTNLNofdipbs7HRrC1iZT5Rt-RyoE5EJIgPMNNkTqjnT7H_wbxqAzrTykEqZMWQw5rjo8s5JgYjymhgPuYJ3qWIeqfj1AKFfADjNqeUOp8KA-7BTOx3eMCSo8TUbIsUQeMqIaGWj3yitW1xtQwLcNx4UCOgTB0JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر یک مجله ژاپنی
در آستانه جنگ عراق
که پیش‌یینی می‌کرد جنگ جهانی سوم راه بیفته و…..! رسانه‌های غربی هم پیش از جنگ، ارتش عراق رو باد کرده بودن و بهش میگفتن : چهارمین ارتش قدرتمند جهان!
رسانه‌ها عامدا اینگونه می‌نوشتند
تا خطر رژیم صدام‌ رو پررنگ‌تر هم کنند،
اما این باد کردن‌ها، در عراق هم باعث میشد
که فکر کنن بسیار بسیار قدرتمند هستند
و جهان به قدرت اونها اذعان کرده.
رسانه‌های غربی با «قاسم سلیمانی» هم همین کار رو کردن!
و بعد ترور شد.
تروری که ترامپ هر روز یادآور میشه
که اون دستور کار رو داده!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=f5w01YbXXyKZbKWgBH6SOD4YT7dOa6cOkHpXu8qyxQ2WFsg6V7FSFt37g2AZK_ZmBs8K8zPdhPULP8zV8VhO57OgTnvPxw2N-TzucUl_SPNfIk1yqWAY6p47rTDdHZcMS2jX94UDWyDRDB1bnj6d1x6RVsGRKNpVkfILmlDNZfSzcOhnyU-sZSnP9-ztarQHiGsfrW5D-G9fEAT0pzHbXIj75yiUZGADzNUKB62Y3c6IpjIusSFftzO6V01qluRnkqHBgxQGgtaKIVFRvrNYGH6TeEUbzNutvlA9WE4EvyrNlLBRwkazlQLWcZmRJuVjYc9DWFSUUhdCSEtKZzGlnUGLY_L7JnjCrtk3V9UPcuv9xtKC2b9OPbDUj1894euonPvBB6GRtZ0BKZ7VFU9rjlH0t5Mr3iPrjK5Qu86UlbEeF3n7nVoFOwQvwZ6q4YB5vre69idoHlBmzNE1uK-qZVbbD5JpUcxaDAtNPy8MB4O7gaACMuJfkDmTI-It3VoQLzcfytFPilkUON2bfmGjWLDB-L_98ctyOw6oVnU8m4b2vafxDC2GAJ2OMiPRxMr7czbjhPFmP0y3y-qMkbClQMmK_Z5g3I8_8JbvO9Cidl_lZO7IFXPYiWcAmBrgcSpBuQoQaoT-PkV7pJZijKm_uwJqpmzGK7ig5JO0Ukv6das" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=f5w01YbXXyKZbKWgBH6SOD4YT7dOa6cOkHpXu8qyxQ2WFsg6V7FSFt37g2AZK_ZmBs8K8zPdhPULP8zV8VhO57OgTnvPxw2N-TzucUl_SPNfIk1yqWAY6p47rTDdHZcMS2jX94UDWyDRDB1bnj6d1x6RVsGRKNpVkfILmlDNZfSzcOhnyU-sZSnP9-ztarQHiGsfrW5D-G9fEAT0pzHbXIj75yiUZGADzNUKB62Y3c6IpjIusSFftzO6V01qluRnkqHBgxQGgtaKIVFRvrNYGH6TeEUbzNutvlA9WE4EvyrNlLBRwkazlQLWcZmRJuVjYc9DWFSUUhdCSEtKZzGlnUGLY_L7JnjCrtk3V9UPcuv9xtKC2b9OPbDUj1894euonPvBB6GRtZ0BKZ7VFU9rjlH0t5Mr3iPrjK5Qu86UlbEeF3n7nVoFOwQvwZ6q4YB5vre69idoHlBmzNE1uK-qZVbbD5JpUcxaDAtNPy8MB4O7gaACMuJfkDmTI-It3VoQLzcfytFPilkUON2bfmGjWLDB-L_98ctyOw6oVnU8m4b2vafxDC2GAJ2OMiPRxMr7czbjhPFmP0y3y-qMkbClQMmK_Z5g3I8_8JbvO9Cidl_lZO7IFXPYiWcAmBrgcSpBuQoQaoT-PkV7pJZijKm_uwJqpmzGK7ig5JO0Ukv6das" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند غیر ایرانی در ایران صاحب خانه است.
ایران، منافع و ثروت‌هاش، برای همه است، برای تروریست‌های غزه و لبنان و یمن.
برای آخوندهای خارجی ساکن ایران.
سهم مردم ایران اما فقره و سرکوب و گلوله</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEbnon-3iv3-EW_HU6CJQfWBvTD2myEVQgE3BJjRzfBTs1Q2jpalJK6LdCzj1pZUtGVx_LPBACJ_hal66BrpTjbWbfA6Yjt4hOVmw6gD_pzxalcaBvRUNlwfInV9dpyaeiW3ZjNxJ1G7cQWsjx2_D_Ee9DhJPL19TRSdUxJ_IFHgv8PgHsEEvbXBTCwh-lziHAek45faUzLTBfH14gaMPpo7qSg2IVmPgxfg2fmxN20V2TZyZnaDhuP6jJfQb3Rye0oD5d2C6RSJXVAnjdFS7S7lUWqhC5M6Bn0x7Kb49L87kGkxgMYOcHz7e1WR_bv83mtSuqc9mVgNSYSdZnCk5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9pbetLdHoHFsEItEc9dm5A-8n4mbZOZeFBvtyaxnG4iBNop8-dFQ5rVEAbxearR0ipLiqhqgx-0mJiV1plv3qpknotsIgWTPWHqOrFo7Y06MwjfkQ8hmQchSAbuCJVPf6jg6sGswNTCKcnrgeApAZfjVgk0Fcyl_3TClFJvz9Z5488xonb8-a-XuwTwC0Oq9Nhw-cf_5RtOuTYUYYwfw1EN3OrckeASuAl_It9dZB2QwDGZoY-gAlxIZdkgzMsuOy5mejMOOykrdD-HkwusKSTE3DX8_J7lSXZZ_GWnX6b_XhVGUoGUtt89cmd5IAPGZ-W2DcYmxuX4z5X1I2b4HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/py5pVBAHjciZdQDxDeXlebKT_mn0hToihK0H8ZD-O-vPCxzgWarx6Wwpy284gXP_I5pInK_xlh2jMO0sR2aqbOEkeQNcjvoMrANxhTgZ25q7x5NVERH0a7bF7aivhuOMq3p4epzR0c5klumgmFuuJav2INbmZq57RzGV50zgnwAHyYYFIm0CoVWCg09v_HYeeF4oEwmj9fe-TLVE-2SV6AoQ4oDGTLUcMsAQw72EEMJPJQe5ZxHodwLvnOOmY9-ot1VtbEBS4NUKurcI7xVFd0BjnA1HpLQlUuQBCa1ezLq5lQJD-dv38ZnyMyO_cfy9wWVcSeWwqWTv-UB9OhweBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=LkcvmfrdzpxGkmgSZeK8_6hPNsH8i_pmYcMGfBVC1PLRxBf-dKrqjcXjomgvbijsofmZ2uhPeCaOjlU_Eq3dxXscDdNcQAu_2kSlHwr3ZzzZ2pnRHEC9b2hNu-orfPzBlI88XJJQoZE_ONxpes9qOa1tGGiDHi2KJjgdIr9foUbWKliFdpLZ856jnxGhqTc3pGjzVWmLfPTAZIT2XHQMHgUWw82HiXBAfjVPsrnkHk3kzalijpC8dwwBPC_wktr-ucCiClcv5E-LdUNzXw4q94AtKXJqeJCsyCQMqrXdDJa32QZn3r4Rl4KOxljEdIhl9hrmCR_Wn6f44Mt_8I27FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=LkcvmfrdzpxGkmgSZeK8_6hPNsH8i_pmYcMGfBVC1PLRxBf-dKrqjcXjomgvbijsofmZ2uhPeCaOjlU_Eq3dxXscDdNcQAu_2kSlHwr3ZzzZ2pnRHEC9b2hNu-orfPzBlI88XJJQoZE_ONxpes9qOa1tGGiDHi2KJjgdIr9foUbWKliFdpLZ856jnxGhqTc3pGjzVWmLfPTAZIT2XHQMHgUWw82HiXBAfjVPsrnkHk3kzalijpC8dwwBPC_wktr-ucCiClcv5E-LdUNzXw4q94AtKXJqeJCsyCQMqrXdDJa32QZn3r4Rl4KOxljEdIhl9hrmCR_Wn6f44Mt_8I27FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFBHiFZm8fAMSiTqrDXjhuuQLRrHCYW6o6i3gDS1k0IZRWi69pH275dYJ3vncd_qv0LaBLjeuImSWQF4jvOWcLQe_bjIy2ETCKNRCRm6IjzQN6ez-mWRx2eViQOmOkIsHhhRDmBvMb7OM2s3nYUh2jcR6kuCH7JLNzWv7LzEm2bCjc-Hh1IQSPv2vf1f0cnMpoqyCRUJFvcDgAOLeMmnjy3xSSDb4iZEopRc83z6Pm0_4Fd4N0JK7TvOgk4zHjvEnR4Cm8ZqDDYTnUsoLZ5cXuSJvAw12Zp3C_zTQd1nbIhyMPOzx_7LIU2o1Lnph5eoDgoXJZKw0-Dpfdv8lX24fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7R7eylBN0enMjg8hm88svdCf3cEvTZe1oPGwvNTTtuZ_Poo6kWwszZNxkP9YDOoQz8gl3nHRO8iqsKAjKxECVEihOSVEEl19bnMB4Or1sZgboVL2idfgCgTmftnZNtxDR07vFbQkt8ko_JW8wCybvDUROeNKNd_WfR9B3E3enI2VmZTkhxDFpK53KIiTHCrr-soAF3yepX0g3SoEEFFKXNZNABFqyw-NDmHiXUMhgzDCHNyoAYr1ybZjT846oN3TXHDDRPTNpjw1EOJFXYfBzkCjD-jFYgKZnGr6UBMWfag4de-nAyfDQeS5jUZaweFMcSa1QHNKziFtcuiJGIFww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJqeGgnUgFsLYEGoF0wjtOZjP2qe_2TP2VRrv97QhG6uTnpybpsTh3HXKgsPeGpT7TMYYMsg38-9U4z4BMNk_8LXPoTRe-rzqkp1cWcai0W2sdfpYvKAMfkTMdCFATiKyAJt5aXrHdmA9pFsjm5nKy4Q_vIzFB8GsHxaHi00LyGzkC3Geehz9yYc0sTLGLNopQz1WU9wEwZiJZXrg5lgw5dqXpQ3g1BYKq-kI9ULJql5MF-pV_zMbQ4z7LPYiCCOMKsdhJGuTHi6A4eOeEL6dS7kszNlZz3O0yckf6_rQjbODb-zn6U34E5CjjgKoauQ7Vf-UpnvUbBzuv4iIry7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rceJVYU589Wadm0oouxWGenhDL4TkuJ986crKiRjneKDE45ePDH0AJQk8KdH7uCvWf7D8hXgw8NFbvlOc0FAW1j_PV0IXLQpIHGxY4dAGqn_MgM74pDMuKoz8ROm65OVrW0WmsvTJp8NlcLecJVdSfZPjrECLKmFLmjtDf-X9DCSsLD5kETKozKxCMB_SBWT9wvwv_Gr62nLX0pN3NqQmGVHsS-V6bSqIT3GG2Z0853sPtUpoTPYUPCSFKjo7jQCImBF8EzdI8UkHRUpYTIJIYxD7srttvJyC-_c24fsq5dDwyeW6-NOHsF89_f2ukPoz1QKdeA9w3fjp7xcE2gGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6e3EMTxUL_Ng3Ifw8Cu7RuhfDQU53Fp0O5Jb5tC8Oj3aAvBhFgc8_mJTIUpX_D0Ixvu9JbsQY8GiH1mExO_NG97sx4q8XwYdxd4ZCMhKLXVw3Rmj2L9XtXgUdzyfd3nRMEDJpuS6wRmi-WrXGky-NyTVHXdaUSngrcMYLXpNSGDRirigA8VfydiDIYvEIQgJdc2Q_1DOLP6PLZJqjhNfn9jpNwTbKGlbLlCFj3y7aOuSoAm14aBTovp7r_Cylhl-qhGthgaTHoyu4QqlNoHKq2h2mqO0V9pbRHXkph35pBlifugI9O3_PsKaBDd_Ie5aJAmqmwqMLsJvN5ROquKdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_dOtKmmBlJ_DJhL3YbfZMhN7nDhI1TfV3cT-Z6Bhg-xPaeHF8f4AmznPY_E8BxMKkl1R54YgqBdQ0eyy4tnsCrUjGC61D3WgQ9GPJdzuru-MQGCaBabaJRoI5mIUqKYCUz9873Gr4x4TR-ysoBstYNvgaoFosbBn137sRwMX0xD95R6eDaucxxquY6NzISJ_VwZ8vUPM9iGlhU_VQNjTLQEuDa3QBQaSOnMJM9U_Oj1EJQbIxSP7NOQK8Z-uz3cuRyondzECnN8lS0yhTcmLTsBiIKr1vzQ-9rEfBulHn-nJBYYPxGGAE0bRBmuNB4zipI4aOo4cJyFmFkDuahzZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRoQd0u0qFE7ywy8u3OnVuLB4492frC6ne5KA0A8z5QN3PaI5SLIwBYOhOPpTKVJlOJSK1qj8lwBU39S6rEbMybs_r7NHG1EzIajE1oHP_HhuuETZeHrkNAsAU7-1vEOHUt7M8zOUYi4KIh0miU2B116_cQpVgz3KUGtzJcjRosBZGJsvraSTVBLHBneWDt99p4zs9vJnZdbN26a9LpZfpjQSBIpfeDqS0HyIarhkFKA5xkxW0onIi_6C_KibNjyRz7tOv95h-BEs54xej-vkoxdOuzPyLsiHR6dWqDI7dNkDvM4UVvPcWNKgIy8eLTZEBQ2cpvOhltei2ut-xktxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIzxZ5se4cjRmgX83VZDe36DBksnO3k-HL1ef9m9rhVDfS4MlP6zSTbdYM2gVhstIbMewH_3XoTnDEgjDgoWLmXK2TX6yj2SrzktDtfiSQdfgcW18UXIXMymcMwVOSnUPaYIh_Iuyo3P3WLZK8pJbPyhgQn-k58z8MmqwzaK7n1TVDFo6sdEhpjHC8XvggVrki9fGWZJnwLUnMRiy8VlzfOH2LIsAFv6CLdD71ebNYa4D3KXYmzA_4Y3bPUoIPtQcOyaiwbOsKYe4zQ76XvIZoZ-wlcRMLHorRfiWY3wbQoaN5-vxfFi3C8b58vZ9-qkQohKvQUswrPnNeeRudT-5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KDALIHpPqJ2gpGijXQ0eCw5625yt2B1V9Quez_F9eW9Jafoy79HIeS6Tl1GsLYNfdGSW5S3qUSZEXXD8s8BUlJb4qEs0EPOFC4_3e4WkcAAtcCBSn0Yj0dF6wKS84EUErJj_EB5RM70bVeZKIccIJs3UkGrIEgee2uPQGs6bwSTQoJg9xOFqSOqqMuLnsCMBrBFiRguL2nd82Rubabtbe1twKZBm2hl5T-nH_0OuxNrunPGMy1jQcmOUajQuAnuluvXlfMQ7Q6vqDIcM4JaScP29jWEszbkJkQ1CnbHj1EWCNdAc46vJvXRkE61l_ffnedx15TJGpCimXYMbL-PHKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IKkD8kI65tOxEf2UlDp5Q3hEAOqSjuP6CbB06JwPOuFK_seSSO4qAdbGWQihFuQx2jhK08aetWQwDDIXfyXX1h5GbBGaK5vX-xmDRPJlUMeZtY14TnXrjuNdChmRAGIkPlmu6TSE3GVniV6VKmbKUWuXpLlHDqmWWaX89LadkBpotho4v8sYjRjglZr6w032DZysRHQMoOQsqrUNDl2XSLUoS05udm5IaD6MOjUWHK_nAjbeYBnjWD9yRCWKqcE6VYrpe2Kin2vhxqzVdzm5JVnVLQaufPvq0xbFxjMHP4ups1Gs6wYNTiwxEjb0WtyReK_XkrNOfZfvz9wJCBzzVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=Fyz0LiUHgjruzM3R4HKKWuQi_yZl7fvX7dPRiQk9G6YFDrApUYwcHOgDNRF02wkoCte8rmh4BdELb4fOQppDs5ow8aOcFPWSoK8jKEDxYkve6Vy50xWbELoH94IsCIGTXEPafaooWjy8zU47LPDjiofRxwXZBproN--xn7pgWd8vgJVrbjSSGuCVXQwNmKk5HHxhoEPHqqY0ejABdzn8X7ibVTb-m_lAu9DSkfMXMYDl9JwsnRfR51kodVEJpfYT1npxniPdxpgnN3QX9qNAtqj7EXX3zGtosJjmuLXurAo2upUb62NTQQ65mPS7-YRApgCWqZKBjwiB4mphVqCCxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=Fyz0LiUHgjruzM3R4HKKWuQi_yZl7fvX7dPRiQk9G6YFDrApUYwcHOgDNRF02wkoCte8rmh4BdELb4fOQppDs5ow8aOcFPWSoK8jKEDxYkve6Vy50xWbELoH94IsCIGTXEPafaooWjy8zU47LPDjiofRxwXZBproN--xn7pgWd8vgJVrbjSSGuCVXQwNmKk5HHxhoEPHqqY0ejABdzn8X7ibVTb-m_lAu9DSkfMXMYDl9JwsnRfR51kodVEJpfYT1npxniPdxpgnN3QX9qNAtqj7EXX3zGtosJjmuLXurAo2upUb62NTQQ65mPS7-YRApgCWqZKBjwiB4mphVqCCxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در حرم امام‌رضا چه گذشت؟
از صبح رفته بودن حرم که تابوت خامنه‌ای رو ببین، ولی تابوت رو از در پشتی برده بودن، اینها هم شروع کرده بودن به اعتراض!
از ۹ شب تا ۱۲:۳۰!
اعتراضات که بالا گرفت،
به جایگاه حمله کردن و با خادم‌ها درگیر شدن.
بعد که آروم شدن بدون هیچ حرف اضافه‌‌ای، خادم‌ها رفتن و چراغ‌ها رو هم خاموش کردن و بهشون گفتن خوش‌اومدید، بفرمایید برید
😅
حکومت آخوندی، مدیریت آخوندی</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=FtRR2yuo6jKou41XkcrxZha772hiaTIbh5_8zkrZV5mYSWSTp3rOBx_MvZibo17LvmhUPj6aTRS9fHz-vOPOmQwsiCHJD31spGzgsbyk4n6hB_LmyTWQmYgsuNSl7XnrLDth1lO95Y29uSxm8FoFpoiX9gMOY83m-wAY490q11TrOd1XA0HKGQIJvWJe7scxGg8J0M9WnKONrc9Pr5EVyYtcOF50nWvbcBJJTiHDzygKUCVfkdji_hTCbY71eL3d_MrQn2mqXOS8mbA4uiQHT_hSdeTtgHTDgfHfXWORqHuhSYj0daF0DfVqGBLj_VGCsY3xAC1ikUqxmqDv0uPuEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=FtRR2yuo6jKou41XkcrxZha772hiaTIbh5_8zkrZV5mYSWSTp3rOBx_MvZibo17LvmhUPj6aTRS9fHz-vOPOmQwsiCHJD31spGzgsbyk4n6hB_LmyTWQmYgsuNSl7XnrLDth1lO95Y29uSxm8FoFpoiX9gMOY83m-wAY490q11TrOd1XA0HKGQIJvWJe7scxGg8J0M9WnKONrc9Pr5EVyYtcOF50nWvbcBJJTiHDzygKUCVfkdji_hTCbY71eL3d_MrQn2mqXOS8mbA4uiQHT_hSdeTtgHTDgfHfXWORqHuhSYj0daF0DfVqGBLj_VGCsY3xAC1ikUqxmqDv0uPuEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lk97cZdk0i0Ts8_aEEqYsPWkDr5flL-ETrQQRpcAdSfOD0Cj5jCAAI_iDp5J06cdCwDiEs5SDXlyAdRdBs_y67o_lKxlkhXM5pvV_KUZ9WnKecCgu7PKqZX3vELfX30M-1Zvp3AZ2O2yK_cb940DfA-rochaDyvBj7jAYXhxkiJkjjjjROzm5tmw65WmXztviAJ-VkEOdRZTAkUnLH9g72hg2FIQBuNOHkFiJhzwYKrpLUF8xAun0QyCa2O4B4pe8X0twedfHabVSXPqW5yaOhFduFkTqsCHdH6L-Zu8CTaPd_GA2_llCcy53aIUJXlY6MSS1tBePGuxg6Zu1yaIbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJcLFQacA_O_eMM_fiKsEOAopIEXJssmMfeE2b1HZNqA7mbQLH24aTz5zVYh2Mc8IFSTjYKLIwSaTRuAsLVQKWvTPdPwPSkRtBWFB9NRQLgSnwFzqz3WI393IsDlR1MBEk1OacY6GPGeIb0pt0So9lCeiQfi4M8CfU1CJpOrcAJEJjk2DVKpXXl7stwPm7JmT44hnZnD-APjARXO4OwTXD1nDbJToSuwxTcb0kWJaatAHjQQHrTNl5cT6V6QmAfL6Pzj3f1V7utNOYgQAgXguwYO81XYwjLnuhZMvWBU_YAt5nBiqjJW3catWgMIFnSY4LK_8KOyMfuWRda6zk6_5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-ng3jckc62nc9XzTTqu-OOcoicVEOuTV5kBHUtZVOJO6vVaJ-8XvIuTjOdUCSSp_gzwybbY8aA7qR5jc9Ec1qQayWLzRnoxr3nUwrnATg3YvO96KeHgGKdgv2X6DUBZ5oTcSMUp_9es8dgNlVCviWF3gRTGKr0IqT4yx20sMyWP3ArzVH1oKEE65BMHTo8kCSRKvCvsW137lgglQmZuh1kxojEAmSiehcWcMMXoC-lgrgy7cW7ZV9O_Hp-8_s2dJfZF_cGoCe3sjzwYoSU8UqGOKtoiOr-2jCk4ea2-CX6GYJpOm9waUgSHXBL0zctY05YAY_hYgWGPQgBTs_2e2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=EggTrDRvJ3VcBgef6OaBDyOK0j4x_Pq4LoS3j_pVPDeVvI1ezG3WYXFJwnM58w1wm1tp1KEs_eXfxo8piLZGLc5NsLsGa1-zSN6dfkvzbDXKLHBtT3FU38u9CTFQB7RomhXjG5qF11jB6ps9gd9te4QEMmHQSTdDGX-zKWD0gHuFMU2Ff3A_64jkdKpl1zxj2HGjX0_kwMLJ6QEal7tosMOsZqbvSgC44b_e2EpXyOYVgvqopB26Rz_pvVBaXUg-koi6z0r6zuovnoxG-aqeRcNfYu56Yd6d0BlEVYcHJv74xAy-k728rKOtUXYRbjzcTSkeVnvjwsVxti4cJHO7lR-LM2asaX7C2Fx1xN5voXnC20f8XtDCpV3WWfB641vUwMtuo_k6fgEseKhq6LBNS853Td-6y9iPq-2efOfS-HTkZCrwlZclaS2U8DrODC-aDvMFEh8Za8in9Ycz14K_8Q2TbWCyWKJKFqiF04iS5EtizMqwhzTQ2mmJpiX-PbG_lf87vU6Cr5KQynISilqrqzAvq0mihVmbxnVIomLhsG7dCurRje6LMsOWANvjwNz2HCmXLO7sPOur7ypVa-Tb4WoG2RFgqdh8z5WqYhlIbLdElAIUlGj4ZtKv2ZyJ1nzVXW52SygsJljV3OX2iD1gB-A1stpoZt5ogova30I2o1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=EggTrDRvJ3VcBgef6OaBDyOK0j4x_Pq4LoS3j_pVPDeVvI1ezG3WYXFJwnM58w1wm1tp1KEs_eXfxo8piLZGLc5NsLsGa1-zSN6dfkvzbDXKLHBtT3FU38u9CTFQB7RomhXjG5qF11jB6ps9gd9te4QEMmHQSTdDGX-zKWD0gHuFMU2Ff3A_64jkdKpl1zxj2HGjX0_kwMLJ6QEal7tosMOsZqbvSgC44b_e2EpXyOYVgvqopB26Rz_pvVBaXUg-koi6z0r6zuovnoxG-aqeRcNfYu56Yd6d0BlEVYcHJv74xAy-k728rKOtUXYRbjzcTSkeVnvjwsVxti4cJHO7lR-LM2asaX7C2Fx1xN5voXnC20f8XtDCpV3WWfB641vUwMtuo_k6fgEseKhq6LBNS853Td-6y9iPq-2efOfS-HTkZCrwlZclaS2U8DrODC-aDvMFEh8Za8in9Ycz14K_8Q2TbWCyWKJKFqiF04iS5EtizMqwhzTQ2mmJpiX-PbG_lf87vU6Cr5KQynISilqrqzAvq0mihVmbxnVIomLhsG7dCurRje6LMsOWANvjwNz2HCmXLO7sPOur7ypVa-Tb4WoG2RFgqdh8z5WqYhlIbLdElAIUlGj4ZtKv2ZyJ1nzVXW52SygsJljV3OX2iD1gB-A1stpoZt5ogova30I2o1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما
که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!
همونجایی هستن
که بهش گفته بودن
نفت آمریکا در ۲۰۲۱ تموم میشه امروزه
در ۲۰۲۶ آمریکا بزرگ‌ترین تولید کننده
نفت جهانه!!
سال ۱۳۸۷ گفت بر اساس محاسبات کارشناس‌ها تا چند سال دیگه  دلار و یورو نابود میشن، در عوض و در عمل این ریال بود که نابود شد!
کلا محاسبات و آمارهای شما همیشه خیلی دقیقه!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=jn_BgavgOHR3Lcb7m-JeYQZqQPLEANBA-8-YRdILiX_jNEG5rCZni-J1gfjPMOeqRDeHMnP0QzLjPpq3LrG-bu1BZHg_XJcvGasclhd515Cj8YRK956ADU-FEhCsutePRMOtzWk3JMwXUsd0bKmQku_K_sqrqQnHo3ucUfB2TbYQt9YdPRij7JyGNxuRViMLkymNpWZOYz7HlmeTf_j2nM6q4E_vEossnWhOMp6eJDuUmUBTncNnE4rEK93FusRFFlAk62Oze0JXElTBBJ_qZY2nSuBow6puQgNiKyiJuEe5KbBP4DvYkTt4C9vUO44ccXunIOx2_Q1nR9hsqkaakSVfSLwJN3dj4BZBqWQvH6qgpuk8s5xAwvYts40Dp978BOeqgQCyIrt7koMHfCrTv0bKmBOzWI6gmPmN8vC1ZEbQoAFwa56QKo1tFCi-PRrwc_0qo8l87ViDAF8uEWaAnQhNcfPASY6DYvgrGLR_8pYty7AVjMPLNrz7omZD1n5GCs2dnbrATWB8OjERbYnHLcQgXstGsz1LWxenJym-qVo6u8VX-ky1_UEhJC42CuCkCENMNbkyHDCvzsGu0Wj8Gm4im0U1lLU5gaECPeAJ7GffruuqMnNzSY3rTt4xodkrmGMJJz098Kt9HVzPGM5BLyMCNHb9eyIHV6NW-4LRO58" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=jn_BgavgOHR3Lcb7m-JeYQZqQPLEANBA-8-YRdILiX_jNEG5rCZni-J1gfjPMOeqRDeHMnP0QzLjPpq3LrG-bu1BZHg_XJcvGasclhd515Cj8YRK956ADU-FEhCsutePRMOtzWk3JMwXUsd0bKmQku_K_sqrqQnHo3ucUfB2TbYQt9YdPRij7JyGNxuRViMLkymNpWZOYz7HlmeTf_j2nM6q4E_vEossnWhOMp6eJDuUmUBTncNnE4rEK93FusRFFlAk62Oze0JXElTBBJ_qZY2nSuBow6puQgNiKyiJuEe5KbBP4DvYkTt4C9vUO44ccXunIOx2_Q1nR9hsqkaakSVfSLwJN3dj4BZBqWQvH6qgpuk8s5xAwvYts40Dp978BOeqgQCyIrt7koMHfCrTv0bKmBOzWI6gmPmN8vC1ZEbQoAFwa56QKo1tFCi-PRrwc_0qo8l87ViDAF8uEWaAnQhNcfPASY6DYvgrGLR_8pYty7AVjMPLNrz7omZD1n5GCs2dnbrATWB8OjERbYnHLcQgXstGsz1LWxenJym-qVo6u8VX-ky1_UEhJC42CuCkCENMNbkyHDCvzsGu0Wj8Gm4im0U1lLU5gaECPeAJ7GffruuqMnNzSY3rTt4xodkrmGMJJz098Kt9HVzPGM5BLyMCNHb9eyIHV6NW-4LRO58" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ej2ApWcDtjjIhgOfton93PCJ82K-zGzLJCYUZJpk2VdRg1odepuck1R-DXEkNw0lUg5Nr4Tzrw1cO8m8UcyP7iKy60b1Ybn8dYsTGXx5bOnDAUz8UYU3oUbKEPphkNP8o5uTOv3BezoWgB-agScllpphlHMQuLnn3ZGx016NrqV0CUIqO6UK0kl-rzhNH_RnGBw0gGHdylx9RNEK2iLp97rcbqqeiu6WcplK-VmllVhmkUBpAm6nmTCAjZ2fVroj5BJOPr9LkVGINFTIB6JQeCahm5uB8BdgouZ4RXrer3ypUOJn1QFb-xGVf-JrGVyYztUoe_BJgU0ZAkjIjIk05Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEBDSuP5jJvUIwOUeEwBi20lOWnhSzZfHyNaUSAoL4utOq55aG2KUtC0lWJnd9aCdGcWuIPdnpcmTfxATQo6NEmMKdMUHGDBsOTxmSh63PW8B73Iv-KvasxwgFB_ht6yYTO-WOkzPEkEjBjL1reFPKI0yECXJ9iQrIQnkK7j3boKU218lFp5l_1rXUlKM3aNbZcK6tE8auoQTZXpzd1ogfDjZ21wDRYxhlKvebNa2n8ccRG4TaDBrL4FPOxfeUG7ctzZa0kfmSgGojXVC9sGc4KseUDFaeke43vXMOYDbZf-LU-6ELxdDb7-EJLhjB_WxiJLY1g7M7OUY5i-wiKQxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام - فرماندهی مرکزی ایالات متحده:
‏
🚫
ادعا: رسانه‌های حکومتی ایران ادعا می‌کنند که عبور و مرور از تنگه هرمز فقط از طریق مسیرهای تعیین‌شده توسط  ایران مجاز است.
‏
✅
حقیقت: ایران تنگه هرمز را کنترل نمی‌کند. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از طریق این کریدور حیاتی تجارت بین‌المللی کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nakBYvNqcez1YDQVnDvXgVVMWFY8K_u7dzUyvQpEGdBrWSbnn6CB3hon6v930eUbD_2c0RDt5iUvY2CA5c6djWS_JKArchdtZIdbCs4y6AOZ43vCaiV1DKhMUM0XHwxxgBlcskBJJJAYvdatKMS2QzLDyl3ZjUjMTWXojJd1LAeQpx_UpFLEt_Zf_ZebI5PRu6e_-Odvid9DV-QTek_9M9id078tdsYXQwnddI2uCwaF85s_96RsVmPICTa1uVO77F-TzczBvn4cB3nCD_k8_xBiXAAT6XW2ASoBKujVSWGBR9YoLO1Yb5FZWBr5AqDU9veXHr4Mt7vqeE_I3ccqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=vlwCY92ThInoeMgpNLtJKHu55-SbDv71niykeLtFhKYxuIaoaz7mqVugF7ShUzkV0Jij_2hShyls8QNxGgMabiRMljxeL053HplWBLOWpqZaF2caaat3uq4dA7dnxwo8Xsuqb7dvicT_lUlqBIOOJFlntcl7X91TgbDHuahhEW-bPhyM8lA7IqTPsUNWq4lxbYYx6W4eQHM-iVwG4s9AW-cOL_g6EMdtJ0aIFXgQoV6ZK3JitPyANAR1-x5yvBJzRdEW0zvE75bOoIjVCofNO9ZOo6BdByXEe1Cs2cDshKgPOIbIydcWeRd9_xc1YEZ_tC3qmzug6qO20dgiLSKe0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=vlwCY92ThInoeMgpNLtJKHu55-SbDv71niykeLtFhKYxuIaoaz7mqVugF7ShUzkV0Jij_2hShyls8QNxGgMabiRMljxeL053HplWBLOWpqZaF2caaat3uq4dA7dnxwo8Xsuqb7dvicT_lUlqBIOOJFlntcl7X91TgbDHuahhEW-bPhyM8lA7IqTPsUNWq4lxbYYx6W4eQHM-iVwG4s9AW-cOL_g6EMdtJ0aIFXgQoV6ZK3JitPyANAR1-x5yvBJzRdEW0zvE75bOoIjVCofNO9ZOo6BdByXEe1Cs2cDshKgPOIbIydcWeRd9_xc1YEZ_tC3qmzug6qO20dgiLSKe0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpJYPe0U8p14x1FYEUHzxW-Yg1DMeRxHgQR7sbdWcZm7abIkxk8kmJ5GkH0j3vDR02-NkxxdBBkflbsiKZ8YqPQPV57aNnPp6c1eQpZlruDil854ZlqqRjR9AsoCySQFFAKc1QzmhNdvILt6w9WThCo1K_XswPkBcABUUL-_0HaF84MFsLDGtk4SkZ0nMXDn5WQsg30wgCNgfD0EgwlcRLHNTyl-Y1ozIoT7VKNdESsIjm9roTrVb8zQITSQ7vIbZqcfGTr7vy6OwfOMBBcjhwIfPulJirub17ENFSAv8alq6ciflgG4BTCgqnluZCDFzAwALKAfAXf7iUxa5w6oJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=NCqXznclyzT-YHpn6OU1d-WvBmNHGiof_lA2xmPYnZOorMQREvpnMCZypxpANxgj_URqQZLTERpL3ryTU5qrhCL8XA_K_E2Z5oJksdpaw_5ZPjJ_R-ArazQQrWvRnxdoQH5nm04q_xpaFybPiiU7q_EfNRYMxG5X6p4_toYEXkw5qwTv3Rf40xdcEoX4-qY-qO7LIcWOqcuQse5SIBdNd5RLEintH9Kyat9XNGg7y8HGhsZF8JViUN1R9kO2iNpWMUcgk_zzm7T7rNk3swxxCFSh8rRigA226MOpn_GtCuK3lLM3MAkAhzcZ29VZa-fUHw-C5Zh1jA9Ypx5F-EJcfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=NCqXznclyzT-YHpn6OU1d-WvBmNHGiof_lA2xmPYnZOorMQREvpnMCZypxpANxgj_URqQZLTERpL3ryTU5qrhCL8XA_K_E2Z5oJksdpaw_5ZPjJ_R-ArazQQrWvRnxdoQH5nm04q_xpaFybPiiU7q_EfNRYMxG5X6p4_toYEXkw5qwTv3Rf40xdcEoX4-qY-qO7LIcWOqcuQse5SIBdNd5RLEintH9Kyat9XNGg7y8HGhsZF8JViUN1R9kO2iNpWMUcgk_zzm7T7rNk3swxxCFSh8rRigA226MOpn_GtCuK3lLM3MAkAhzcZ29VZa-fUHw-C5Zh1jA9Ypx5F-EJcfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXT0vzl81qx3G9dqAO7KWp6491J3LqVJN_dMNuO5IiBqLN2mR-Ofx4k6S3y7t_Jesdpig4qPIdn8XVaM2NcKEEzTnF7iFlEVzNZd3u6dtiOnVjA2l0jFA57N5pkHjJiI0FNStn4QwyzOjPdSzWaE6q-jFIOOpOcDAKa4DEdeFVmfsHmrFTNxbtXKiZYc4NhLoTd5pGWtPVbCTzggHW1Pz0MFxjOR792aeyUdSx61zyE9ubkkDyHXzE5weBIDT8FqE2U0PuLIvXjcSLhs2phBmB2gvgNKq2vOOwKbpN6hDQdDIuTlfZvkIOqjQs3890fsIc4WBgh8Tnkg35RWyxOy5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXmz_fDfPmzgVu7BoJmorrG5roPM11QWU-Tk1tLMsJmLtOREAjWpB9KIqVBKtRNuIDcGkiwuDjqk8a-bZcyapdG7Oy7L6YOTaj-WaJ_akv0fYajK5KYqXmBKMWzVSgp5PsbGp1iLhxYL5HqMdoqqY7ZoCQ8vdUg_eJUatFlRMiPZoxjbCQ5r2bNZTQ4497LMKC1NZHWRT5Q4x8cEGWfC4lvkfdNysfzXo5hfDSwtcn5E2p4acnKiv-RV1cbLbPCl-1bfEJvazQtO5lLwpNxPv2fjMLCR5y7LqmdTSPyIGSV8TdGxgfZFcM0Y5tMXpiifu9VUYO50dCmpyFf9wG0i8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=v_YBrIYyJ6OdCByybjWbu-KCWbrJhRTJSCvzzej748YQXG8wPp3f_b65qHHD6eMu3g4owAqZEbNri_j4w_mnE1SYh1-QGNSzBqwetyfy3sfFfwAGgqLeqf6FcIk4HwQ82ax-CIE8KhLXgx2SGq00V8k9r2YpllRrr7s3G3BldamgYEUcrSPeNHv7sWrw81Zxd4vvEHxXHAVgvS6iXAbk-Ggl7gvkWO3xiDQeavv1hHJPNM54ck1bKhs55aeiWA-fGxp_VArcyzFMeq9yLRVZ9lQQ3MYt146OwAF6_Fhm8-tZn-rMbn_IV9hZwEpUn8u-R9WxSh4nLNCid5F2XluPvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=v_YBrIYyJ6OdCByybjWbu-KCWbrJhRTJSCvzzej748YQXG8wPp3f_b65qHHD6eMu3g4owAqZEbNri_j4w_mnE1SYh1-QGNSzBqwetyfy3sfFfwAGgqLeqf6FcIk4HwQ82ax-CIE8KhLXgx2SGq00V8k9r2YpllRrr7s3G3BldamgYEUcrSPeNHv7sWrw81Zxd4vvEHxXHAVgvS6iXAbk-Ggl7gvkWO3xiDQeavv1hHJPNM54ck1bKhs55aeiWA-fGxp_VArcyzFMeq9yLRVZ9lQQ3MYt146OwAF6_Fhm8-tZn-rMbn_IV9hZwEpUn8u-R9WxSh4nLNCid5F2XluPvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=Ll4HheKMzkyXxzc1OYcB2ZUocSMoxMh-DxuE3R9k604ipe-49aSicV5J0cUGegcHXIPpak6zBPiYmriLYUzZOMICGjxUvlOsgLFwLWALRj35sYvNmLPMkXVr9clHvKe8ZQ2OSGjiMKxk-p5Bs60QGVIFKvZMKdCa3wqaGTAPk8Ip91lzwnMqaIhPu5VetF53aZ699WXsNUPF8T4Vw4PxGtxNRp06JthJakomVHz6y0ayTMGU9JMZlh75jEq5K7e8M1CpzAIGO7EtRevlZmCP3SLfDa9w3EaxD7LRqQuPJ6uLYc57mYh1WCgYwPDyfcGrBFdD2viSE3FawOYrXO8P7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=Ll4HheKMzkyXxzc1OYcB2ZUocSMoxMh-DxuE3R9k604ipe-49aSicV5J0cUGegcHXIPpak6zBPiYmriLYUzZOMICGjxUvlOsgLFwLWALRj35sYvNmLPMkXVr9clHvKe8ZQ2OSGjiMKxk-p5Bs60QGVIFKvZMKdCa3wqaGTAPk8Ip91lzwnMqaIhPu5VetF53aZ699WXsNUPF8T4Vw4PxGtxNRp06JthJakomVHz6y0ayTMGU9JMZlh75jEq5K7e8M1CpzAIGO7EtRevlZmCP3SLfDa9w3EaxD7LRqQuPJ6uLYc57mYh1WCgYwPDyfcGrBFdD2viSE3FawOYrXO8P7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=etWA-EHI2bItExOKFy66hLxlU0uQQVHaClYRMvGUNXF9C6Fohrk56jlly6dzHtgdw72UjQj3PTUGvw-VLNNLEThmfYvgELtf-rWvFZun9sbCqMKC6yW2g8AbJJSvPfV4h05XjXOLi4XA1N0x_gDR6gXonzdCkA8wznYwsHc6ojRmiGBZ7x6W13xjEJwcUfs3-ligolmaKLbjQ-yCxBQXngguWHdp0-47qjXa9xr3mTO4skA_q_J4EZtWjzITLNrDFSgk3LIhv6UHXnwyiLtTttzdo0tH69_-LuCJcmcz5isOCvwPCZl3V-JMivkNluF5JUM_PbfoYZ7tpHDE9pmm5UECQrDKSJ1dNdVo7eDTP-J2KGaKXaWoDNhwZh6fvlM9BA3fjBJ727zyfudBDry3rcFz42phzneJ9TOMpYPTxX9m58UYHKfJGzMDbQSQPsIsGp7mDaq0THZAvyVlJi2F9RF4s9S3rIApQ336bRtFqvSqKPBnKoUhvWoUR_fc3v3P0XhDnKyiIOj-U8PBJiouwLF5CoIfW99YcBl_gvGZBvOeYAQiXXwW8QQszs-7x8Td6e-DxaPLX8SRPntKFEWElgNg19Y67VWWVZQ3tCwUKRanbD-1v6o4oyx5VcG3ibXurS9mDDMI7tenIYhi1iCVbpGWOsGrrENfWkG_xspGT1k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=etWA-EHI2bItExOKFy66hLxlU0uQQVHaClYRMvGUNXF9C6Fohrk56jlly6dzHtgdw72UjQj3PTUGvw-VLNNLEThmfYvgELtf-rWvFZun9sbCqMKC6yW2g8AbJJSvPfV4h05XjXOLi4XA1N0x_gDR6gXonzdCkA8wznYwsHc6ojRmiGBZ7x6W13xjEJwcUfs3-ligolmaKLbjQ-yCxBQXngguWHdp0-47qjXa9xr3mTO4skA_q_J4EZtWjzITLNrDFSgk3LIhv6UHXnwyiLtTttzdo0tH69_-LuCJcmcz5isOCvwPCZl3V-JMivkNluF5JUM_PbfoYZ7tpHDE9pmm5UECQrDKSJ1dNdVo7eDTP-J2KGaKXaWoDNhwZh6fvlM9BA3fjBJ727zyfudBDry3rcFz42phzneJ9TOMpYPTxX9m58UYHKfJGzMDbQSQPsIsGp7mDaq0THZAvyVlJi2F9RF4s9S3rIApQ336bRtFqvSqKPBnKoUhvWoUR_fc3v3P0XhDnKyiIOj-U8PBJiouwLF5CoIfW99YcBl_gvGZBvOeYAQiXXwW8QQszs-7x8Td6e-DxaPLX8SRPntKFEWElgNg19Y67VWWVZQ3tCwUKRanbD-1v6o4oyx5VcG3ibXurS9mDDMI7tenIYhi1iCVbpGWOsGrrENfWkG_xspGT1k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoYv7r8ktxJ7_K93pMruos4OYL38f-C7770pZHoVjU0BOVMmUZywialWcK8wk_XqKA44jWgUiJj6RRj3OguXBwHaU3FrBrYKAN-ytAJoNRleVaLEr0_HL5XT4efSiyK5Z4d7uBeyqkUCuefhUluldBxjE0icJQp-1E-xYSWHrP3lk3s5tzyS15uOXej9u492V7L8qdDK955Wb8C_aFleHE3a-0hO6nt6PQ1VAgrK1m-7YN3eflp-sMmcglHiIN1sGePshXAc_TNyjOrowGwZnsqmhR2T5nEroxLiKxE0PURQW35UI8P9XXsqyWIA6Tmyk_yoJ8WfkVaIm1UqlJJXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcjwtfYycX7aNpsDf_XQq8h6efQpA3SnCEgNCDzeKdi7tQ1fkMtMx0bJOeiu1mPz5itYOviPM7tTJer_uQGnigp-K9pPEba1FdB2Zp_aoIlNc7pIS5Q2sEWuXJwjYHB4sYGVgOIprBGMf0KA06vqrTcW1HgnbZY9DdXGXX0_NVVtz41SCQxz26YsndIZC8phjJy0Kmwjxe0qW0Fg1s9XUZ2RNdrABkWGnG322nVNOiQZufF-8MN3y9NcOTfcP5JxNDrunuw69qS82lFwKYH5jsedYUXeJCCfnNCFWSjau4bPjDPhkvl6Js-BZLSu4EZ7XuPypP2ISzzYSRdkaIPt6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcGM8Xz9-dH1G3x9paGO1LWiy2ImQlkxxllMXDoRVc6uV2G-oPlMCQLHtsv8kakVr3G_ww0oRmbVhdyDcDQfEZcps5alHUqfFg1lOzUxdIgnZcD7_7Bt0i4A0PGvI7_trA_WYwJIWCu0_LJv0V3d_M1uZzAfwwBVucTb_uYbfIusAFk_QjAUzGiES7bGPsV6aQEvaoW-_m7kBbWIIIUld77s36wVz9oynToq-014YhIjfTE70DU6qRzQYZPQduplsu77kp7_SjTA29irGGZ4ZsFWGxHCh5pVamxw3v1IezS039RR-XgnkPIOd7H3WJQiy4zHIk_G9F5SdHEhzFK6NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=XrDPMMje1PkXJ8hEvfxAEF_HxU0lmTFQk8A61lg5NyIsVRnEKcZuSzy1InTjRRfWRUoTUepeau6a4zaafxw-aJgYZ24dpC1e8n3HaYCbL_h8Fm4vGWfhgsBeXYyW_D6sBBBz5CaSCbHjoTXViM-3bHLgTaFtMgcYnRu_wEXntC57ptIqx__Q0MEJO3rBKdQYPPI4gtp8CpifbZiILOzP7opMDLo3Df-SZJpDZtUc6kIeeT7ivKceeUKejOHpjXL2P0GSxQjdrvH-UH2aku8XuUE8oGw6kscLWj2Gdwr6mSRGi75RO2GcxOMRMxsTPAQJFlkmgYXpmsDKUGxqViYHvDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=XrDPMMje1PkXJ8hEvfxAEF_HxU0lmTFQk8A61lg5NyIsVRnEKcZuSzy1InTjRRfWRUoTUepeau6a4zaafxw-aJgYZ24dpC1e8n3HaYCbL_h8Fm4vGWfhgsBeXYyW_D6sBBBz5CaSCbHjoTXViM-3bHLgTaFtMgcYnRu_wEXntC57ptIqx__Q0MEJO3rBKdQYPPI4gtp8CpifbZiILOzP7opMDLo3Df-SZJpDZtUc6kIeeT7ivKceeUKejOHpjXL2P0GSxQjdrvH-UH2aku8XuUE8oGw6kscLWj2Gdwr6mSRGi75RO2GcxOMRMxsTPAQJFlkmgYXpmsDKUGxqViYHvDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=QU9-0PInPmieiCfLWiUI21nyG635ENICePkWlsWwnl3iF2HVe0YkK_887EuhB4maH8AtxIN0b-7J7nHtnFcGCJkywrtGr_q2rkMzYKqsZcLygr7G4FKjqFRdFLNgjYIiRzXZLT3nszZl4wCcPrRb98SeIudO76rSUALl-1tA4QMvxihkzpNCFRxXtLRcnxN0DJVDWhV068h2mOH60NvCdWXrrYOmdnQp3wuqTiACRc6BtjbqLFBRt08zTtkcUlqhMlSsBg5fV6-HJzRnqE6XrGxW6hyLlQ8Bk4pbKDZ62kUsVgKUPvGWQ1d6AtECYpCTD1oqS1CvO6mb_RQbcwLw6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=QU9-0PInPmieiCfLWiUI21nyG635ENICePkWlsWwnl3iF2HVe0YkK_887EuhB4maH8AtxIN0b-7J7nHtnFcGCJkywrtGr_q2rkMzYKqsZcLygr7G4FKjqFRdFLNgjYIiRzXZLT3nszZl4wCcPrRb98SeIudO76rSUALl-1tA4QMvxihkzpNCFRxXtLRcnxN0DJVDWhV068h2mOH60NvCdWXrrYOmdnQp3wuqTiACRc6BtjbqLFBRt08zTtkcUlqhMlSsBg5fV6-HJzRnqE6XrGxW6hyLlQ8Bk4pbKDZ62kUsVgKUPvGWQ1d6AtECYpCTD1oqS1CvO6mb_RQbcwLw6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=CABCBpRT5eG0dVlCcHUWs7fQKKzhcrj9tCH4Cy7AcyElzSHW-r4VIuGELCG_wwX2Nh3aV0e897A9aHtN9L03eV9OQVOQJX0ZIbeduNX2haKWAxLvDUoLW5diF5On3dEzDLHVdI98BLtQ7Tm9yk-851NAz44SRFiMeg2hYVEpCq6FTn75yUa3R96j3ZSb_PuKSCvpB1QYQJHNrzMGoFHTN1PYucj0zehD8GPFd37Ue0gfWNTojTo2GsXahco_4at2bnXoKhcm9aNtq5PVbcQ51v3Ss0MbMQSSCf3TO_9thfr1xoZIgDqUcyek253KOOEYAqpk9WTLrR3Gu5L2zOUovw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=CABCBpRT5eG0dVlCcHUWs7fQKKzhcrj9tCH4Cy7AcyElzSHW-r4VIuGELCG_wwX2Nh3aV0e897A9aHtN9L03eV9OQVOQJX0ZIbeduNX2haKWAxLvDUoLW5diF5On3dEzDLHVdI98BLtQ7Tm9yk-851NAz44SRFiMeg2hYVEpCq6FTn75yUa3R96j3ZSb_PuKSCvpB1QYQJHNrzMGoFHTN1PYucj0zehD8GPFd37Ue0gfWNTojTo2GsXahco_4at2bnXoKhcm9aNtq5PVbcQ51v3Ss0MbMQSSCf3TO_9thfr1xoZIgDqUcyek253KOOEYAqpk9WTLrR3Gu5L2zOUovw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=vfJrHJbuNFRls_XifgQp4r2lu7WoaxZlxPGVss6iEGlumPSHa2DRlgpF2F01i8YmFlz65or32ZyL29WPh85VHRnArRZaxKiio7YaKeBpXU2Szfzo6ZQ5AXqBosUvstQaM8Pu49TpB8KsriwXssI4dAGo5_4FuOYSl7EDdbvzk78uuaFDaFKcidkNemGkvrAWbFZqWq5vp6qzQptetwg9wptt0u3rYWsAMtbhGzsX79LMBuOe6I0pMbdD4auprOY4MPUkkx1djVcwwLMOYogiTRHp9OVPXAMqmOiCe4UZlhae0V7HhQ_jsymvcq-LvanewZ7Flw4q0IvsnA28v7M6uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=vfJrHJbuNFRls_XifgQp4r2lu7WoaxZlxPGVss6iEGlumPSHa2DRlgpF2F01i8YmFlz65or32ZyL29WPh85VHRnArRZaxKiio7YaKeBpXU2Szfzo6ZQ5AXqBosUvstQaM8Pu49TpB8KsriwXssI4dAGo5_4FuOYSl7EDdbvzk78uuaFDaFKcidkNemGkvrAWbFZqWq5vp6qzQptetwg9wptt0u3rYWsAMtbhGzsX79LMBuOe6I0pMbdD4auprOY4MPUkkx1djVcwwLMOYogiTRHp9OVPXAMqmOiCe4UZlhae0V7HhQ_jsymvcq-LvanewZ7Flw4q0IvsnA28v7M6uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDoEZ_KJh1l7U5hlRQtkXoZ4tlM5lKwMLO41gWcK76GMc7GCQKO_2zDMZZjhiwzncQjJEhuKF7SJufXyERllgDC05sLJdfnGsC8ec2fm0lwiMmnhA_8zipjPR_3bXQiq5c1qxUzo0TQXlaBl6FNaSAf2R_CpOM2z99NXHpZvBgKKLgFyz4JbW3JYopDzGCRcfMtp6FjozHTaEiRSehaNiGAx9uhXGqaYTO5AJs0mYakRJgra4rmcMmSSdikySJkvHXZOS4yOSXFZjrMiTW5OsXlNa7O_bQQkdk67rsO_iWc5AnPtsoQtq93Vim-g7RZovtk6Evrvw0sVdTQMF7BS6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=IOdlIWBHr0BBwQyNEkzhk3lAdEfxR9dCpIpGP5pV_Uad87BS1FUjUjiQa9AjUQ6qxQoXJnebOB6pcIwKRhVtAyI2CXTorDQ239qc_mPRppj_zIQkMOUbnOJYkBWckstyL9pduXSpz0Kb74WZrgknyeMGJ4SBMuAP7HFIDnGvQgz29gmMXuQA6ej1Si-BUL_PGv0O3YH6Dk-GD0syW9bfR7X6BAFeNzi5AEByF9XYHIkeunEz7UMA613DHS-znBwKcx1_MKFld1gHJsl2BgtduIDBNasGFzuAwrlHT9isN6GECud_06XMYYXvl_aUpCZpA7wvrbTel_gLk_PZPEIPRi9KlmrX-qRfB3NChPOBbP7eJR2JmXfA-o6GXZAvdpeM0hHw1JKlRvtjpS9mj_GnIAJe0LHLJ-YJJAhjK8-p8bnUNEj_eCR0v3Tw8j8trlboQVMEuMbiOAVREfmm2Ma4HBNkgJdOXme4zFN_o3xutNUC5fpc9j7tDjc2OmUHCbdRi8ijISC-xMuQui2D2ekeD_2GC-_6Ctvg3q-_62tAF5yjdUvrXcImA_NHhm84eNhj1IDx3kUP18xobDDyPCLNXNd0NpKZg0DnuwYEBDR0_L87wDpYACmPRY8gxbj8XXqvyIc9I9XW3h_Mr9m8O75fpcjbM5ztsstE1HoK2IT-_x4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=IOdlIWBHr0BBwQyNEkzhk3lAdEfxR9dCpIpGP5pV_Uad87BS1FUjUjiQa9AjUQ6qxQoXJnebOB6pcIwKRhVtAyI2CXTorDQ239qc_mPRppj_zIQkMOUbnOJYkBWckstyL9pduXSpz0Kb74WZrgknyeMGJ4SBMuAP7HFIDnGvQgz29gmMXuQA6ej1Si-BUL_PGv0O3YH6Dk-GD0syW9bfR7X6BAFeNzi5AEByF9XYHIkeunEz7UMA613DHS-znBwKcx1_MKFld1gHJsl2BgtduIDBNasGFzuAwrlHT9isN6GECud_06XMYYXvl_aUpCZpA7wvrbTel_gLk_PZPEIPRi9KlmrX-qRfB3NChPOBbP7eJR2JmXfA-o6GXZAvdpeM0hHw1JKlRvtjpS9mj_GnIAJe0LHLJ-YJJAhjK8-p8bnUNEj_eCR0v3Tw8j8trlboQVMEuMbiOAVREfmm2Ma4HBNkgJdOXme4zFN_o3xutNUC5fpc9j7tDjc2OmUHCbdRi8ijISC-xMuQui2D2ekeD_2GC-_6Ctvg3q-_62tAF5yjdUvrXcImA_NHhm84eNhj1IDx3kUP18xobDDyPCLNXNd0NpKZg0DnuwYEBDR0_L87wDpYACmPRY8gxbj8XXqvyIc9I9XW3h_Mr9m8O75fpcjbM5ztsstE1HoK2IT-_x4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=I9I0lgJxJrbDzSYC8gaVuuM_pEg7Ii763q6NnNajFYD-6taRcMQd-wSbMAIk6Slo7M2wWLxeZ8oTsD5oIbekuenEKXCBgXDJJXLVOwL-3qZY8TeB05sZhtslcFSFfAGLy5oC6Nb6LvMGlwLPcKtqURXMP5pTF18TtyepIFAEtIb54Cq4EKDnNy7EUFDKhEor9Acz_r9Lr9b0jhpDPBGzeurXNTvTe8mHyvzMc5KMAvpf_qI_eRjnXnKfevQLw-WAZkyWk4Eq_mwxsGy3lz1ocvI4Tg9fcIo9DdDTnU91dv5_serCLPMpJF8npINp9nkCOMeNwTkxZnh5jVfB_HyXsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=I9I0lgJxJrbDzSYC8gaVuuM_pEg7Ii763q6NnNajFYD-6taRcMQd-wSbMAIk6Slo7M2wWLxeZ8oTsD5oIbekuenEKXCBgXDJJXLVOwL-3qZY8TeB05sZhtslcFSFfAGLy5oC6Nb6LvMGlwLPcKtqURXMP5pTF18TtyepIFAEtIb54Cq4EKDnNy7EUFDKhEor9Acz_r9Lr9b0jhpDPBGzeurXNTvTe8mHyvzMc5KMAvpf_qI_eRjnXnKfevQLw-WAZkyWk4Eq_mwxsGy3lz1ocvI4Tg9fcIo9DdDTnU91dv5_serCLPMpJF8npINp9nkCOMeNwTkxZnh5jVfB_HyXsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwG5a5k9OvkxAQYJC72LXR5-lKEPIldIEZbWwWqnGwxgUMBlAGd7GIUp6UD3TILMc0CxA8fEGdD7nkmyLNG5rB50QzkNn8IKMsRuOA6jPpBcCiU1-OdfLat64M8c8esFLEzVzgaZcXpjLywbUUwcTYr31APd83bzCQoTt2L8KcmXAaPTpHjbP2z0D2NwIz593MjAjvESWeJuxwtTxec3lQ8PhgKLYIFIWieSTGjvHp1gxg1dvX79r-96CyjOVOOA5pXhMDAgIkiO_2Lus7ogML-zaiGDXqn9D4cLlNuCxBhIPoJTD48auCOL92QS9-3gCfgUrSZgGF-4lk8xD89L2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=mDWH5cw_U1-bq3kIE57CwQuW8ZmlT_x5mCDnbu9bDIDoWhMWbManzI4KgM5Bu6WUAzVO4StkQjl8XDFXgqp9Ia9-o8SlPgWsexJAfbH6yu9vC91uEnGkCTa651bgxAOAmJ6ErdWT2T_mSsn001gesQ4mYkMoGg4YUe0IDN4T_I-PiS_U24juhUntos2TwcdVBees6KZAK_tZbu8ZJ88VORpHq_zogIenwbfGE_I5tWc4GXllj2Mq9rJdKwqN7HNKnntFGZGqvYZ391EQtGAtZuiYWiEs3fflbgwL7ZRXf53eDYznTzH-CEa92KkbzxpYrB456zdxAkEJ5YBsrOwFwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=mDWH5cw_U1-bq3kIE57CwQuW8ZmlT_x5mCDnbu9bDIDoWhMWbManzI4KgM5Bu6WUAzVO4StkQjl8XDFXgqp9Ia9-o8SlPgWsexJAfbH6yu9vC91uEnGkCTa651bgxAOAmJ6ErdWT2T_mSsn001gesQ4mYkMoGg4YUe0IDN4T_I-PiS_U24juhUntos2TwcdVBees6KZAK_tZbu8ZJ88VORpHq_zogIenwbfGE_I5tWc4GXllj2Mq9rJdKwqN7HNKnntFGZGqvYZ391EQtGAtZuiYWiEs3fflbgwL7ZRXf53eDYznTzH-CEa92KkbzxpYrB456zdxAkEJ5YBsrOwFwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=l52fhUN8JTWtFVvSBvOq9_LCSwxkj9392moyZek4-O4K1L9XrwhcmZArXxJVlFwcHT01SdOP_l7NwiR3LlmiAcpYxz1RjXdV0u-6CCvs-S81AA25zmi7Khf3Xeol9W4_tkT60UAMtDRAdquj2SPoF3jTZal8P6NWrrLTvxwSOuHTnCqjvoGmcRnk9A5pLcJFwDd2A8f0qgHmakDPUx2-7YHIlBTXU5oKX3YKJjtNyl62tOmqqsiuctBHB35CHVBQ8a-XeSSWqRrumUAY7mhDr5d4sY66lN-HKn6jprnSOnzmhVwlKEcvLDrYwycLR8CgbY1fNdnihHI03-gxDzGoZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=l52fhUN8JTWtFVvSBvOq9_LCSwxkj9392moyZek4-O4K1L9XrwhcmZArXxJVlFwcHT01SdOP_l7NwiR3LlmiAcpYxz1RjXdV0u-6CCvs-S81AA25zmi7Khf3Xeol9W4_tkT60UAMtDRAdquj2SPoF3jTZal8P6NWrrLTvxwSOuHTnCqjvoGmcRnk9A5pLcJFwDd2A8f0qgHmakDPUx2-7YHIlBTXU5oKX3YKJjtNyl62tOmqqsiuctBHB35CHVBQ8a-XeSSWqRrumUAY7mhDr5d4sY66lN-HKn6jprnSOnzmhVwlKEcvLDrYwycLR8CgbY1fNdnihHI03-gxDzGoZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOUSnIWYctG4vffSAI0Pp-IKPv2kxVv-zIAsHavXPjZijAc-O0RrSpJtZl1S4fCaeP7ex5ZMxdgmpSynOXU9qfoxwc8D6CgUBrMDihl76uKKnGxbfm4xunMmKXc7OmJmo_em6DN8XOiXjjWUJ0JNjFpdCTbg4OgwNxDt0GQEPwBbd1AqNB3B2JG3jEr5Np2-i26Z5tuA5_1fuFeeA-rhU9ScVcPmFHz8B9HXoxPjXKFi1fXK-le9zO3nuW6rT_3BZreKUSFifeS7t_CWJ4wPjR_Vj5A10Yd3zeidLfhHfGbiNMU3szKIEMX81s6MrbC2uWcsiB0vVY3IIv2f-4pziA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=Qbc7y80wHk0iHNuwyHjA9FsyJlyFwlhdWwRuCfKDLv8K3Z7AmtcEudrXM1Gl2BUcbVO7-8EK9tz9JuCtuSH7fFoQlk9A0OoLByupf-cESR7SBSgTw6Tjry7FoF5Dbiz7WCdXwWP5Xc_O9xhDfA9q67kd1ryPQrzQ2LsoEUsueLy_1gToZpiFTV-sfpTvYGSvRVv2Owga1LtbFyq3Ecmq0dgHN9rnYgU5IatHFMQuyJSriZrxeK2m3MlxNxoM48qFPF9YTi2tbT2Sacqh_K2HP-92tIJCvbjj-I3DTa4G2m9059VKrIP3jAL-J10QqFOitKLj5KuL4kpxjFpL5Ttzag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=Qbc7y80wHk0iHNuwyHjA9FsyJlyFwlhdWwRuCfKDLv8K3Z7AmtcEudrXM1Gl2BUcbVO7-8EK9tz9JuCtuSH7fFoQlk9A0OoLByupf-cESR7SBSgTw6Tjry7FoF5Dbiz7WCdXwWP5Xc_O9xhDfA9q67kd1ryPQrzQ2LsoEUsueLy_1gToZpiFTV-sfpTvYGSvRVv2Owga1LtbFyq3Ecmq0dgHN9rnYgU5IatHFMQuyJSriZrxeK2m3MlxNxoM48qFPF9YTi2tbT2Sacqh_K2HP-92tIJCvbjj-I3DTa4G2m9059VKrIP3jAL-J10QqFOitKLj5KuL4kpxjFpL5Ttzag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABRlu0wZ6YupOh4f_CrVsStcU5MPPhRk49y85751yFyzAMQjwSd0bJJaRTDaAX6azeBcJAzaQ-2cxd75ESKrBn1-3C1SxcHJ5dIvcmO2c7Iz8_5FHt3fAeU9LlHbYwRu-jjyBsH_RDt0iPEGD2NEvKVsS7oHQwxY-rOqTTVEKopzQRpJhuu-ePQWAsUWLXnc4Se5NU4y1Czd85EO8cc-5d1noqLaSoDGp_eJGoTIPSNvtA3p9hTfzjus4oalYsyz4ZPA5WCDbHa1RjE-zDI10KNSxEen2QwOtHwVHC3gYXzJBnxSemiCOYJKwI3J0OQSswuDwfFjtbbyDvN9gNnH2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=VTMIe9Raatbc8dxArGObrkR7CVH2XF-7y_8w-omL7Q16IJNDWlEV_xP-kXGvQYgNzoSlEMoqAIcbYgzOkCF0u0O5mRgtLWjlv1q86jEI4uZZfUJPUMd8JHIY6qdxxxb0LjyQ0xJxp2sR6sLFHdut_BhlBjG3jaI-3OlVCowszj2xT1ZFerWO3ifqE5IOkibweYMLVNLQ779yngVuNuXLe1bHky63N-pkvOf9Y6XAzPjfFKhg6Goh8_TyXUNHe_gRF18Ow0r__L3jUMqpiFpSTeqBuDQACqg-Adg7WelGt6zumklNvkWh8DnSXnt374NyHNrUvlFgmJOUp4x6MSE6vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=VTMIe9Raatbc8dxArGObrkR7CVH2XF-7y_8w-omL7Q16IJNDWlEV_xP-kXGvQYgNzoSlEMoqAIcbYgzOkCF0u0O5mRgtLWjlv1q86jEI4uZZfUJPUMd8JHIY6qdxxxb0LjyQ0xJxp2sR6sLFHdut_BhlBjG3jaI-3OlVCowszj2xT1ZFerWO3ifqE5IOkibweYMLVNLQ779yngVuNuXLe1bHky63N-pkvOf9Y6XAzPjfFKhg6Goh8_TyXUNHe_gRF18Ow0r__L3jUMqpiFpSTeqBuDQACqg-Adg7WelGt6zumklNvkWh8DnSXnt374NyHNrUvlFgmJOUp4x6MSE6vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lINQFSnRaPACS0xpHD3ctZjnZdtDXqQ2GBwajs92dKYtaop5R1XX9KxcPAhzOd4mm7_2CE3UA5r8t9LVXpoY5F2PNHtqibXYXQ0nZkVXKs8En0HrkLhI55PWLKejklMHIlapSY3c1ByX-5xgJmln5U_SK3rmdWqTJwnFCLYIenwqEpVzhz4nhpVjzHF4tTN8FanGoMdo3iWH_yrxLnSYludPp66HKZ9qc62E6Ky31GRTXIBvQPfXxitFwc4OaDYKOQI1_caBY0KOrpddiyletuamQdFlz9QrL_jTqMg8FxUL2bScxdISb7wlfp1WywqnNdu7gqFbDYqNPoV3tPJilQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=uzOPQGvNlhTBkLFg9wxZsFEcezN8NKpTiLH6BTZri_JQ6tOZEGfPKTxIGeuwxc_Xc1y2A4K9DEjks1A2XUxi35by5RTDEngYRIqetfeFaaTnbjOWXeRUYxukRLT3j6U5NyEH06yW9kqQ33H7Pfggz3gAiz-AtG6wc7IZzkNwkAEF1lQKXRGSmGUiUndpqP2SIkW_YjRgT2NNSaweErGWdl5CyPdNcRZWUi6UqZnfeS3SNHZ81jHJZiGa8rdWZGZltg-pqq_FchUJkxkG4pKikC5wEsSf_S-1L9BQ7Ay5k6jjvfmnuZ1W8OMczXBkEQmJJcQKNP0kjvpFN6A-AiJvvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=uzOPQGvNlhTBkLFg9wxZsFEcezN8NKpTiLH6BTZri_JQ6tOZEGfPKTxIGeuwxc_Xc1y2A4K9DEjks1A2XUxi35by5RTDEngYRIqetfeFaaTnbjOWXeRUYxukRLT3j6U5NyEH06yW9kqQ33H7Pfggz3gAiz-AtG6wc7IZzkNwkAEF1lQKXRGSmGUiUndpqP2SIkW_YjRgT2NNSaweErGWdl5CyPdNcRZWUi6UqZnfeS3SNHZ81jHJZiGa8rdWZGZltg-pqq_FchUJkxkG4pKikC5wEsSf_S-1L9BQ7Ay5k6jjvfmnuZ1W8OMczXBkEQmJJcQKNP0kjvpFN6A-AiJvvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگفتی سران فعلی ج‌ا آدم‌های باهوش
و منطقی هستن، چی شد امروز گفتی
که یه مشت بیمار روانی هستن؟
ترامپ : شناختمشون!
و لبخند رضایت مارکو روبیو
[معروف بود که روبیو ج‌ا رو می‌شناسه
و ونس اینها رو نمی‌شناسه،
ترامپ امور رو داده بود دست ونس،
که الان ظاهرا دوباره برگشته به مواضع روبیو]</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqjdqvqJlQpcW7QxPYBmkoYaGhLh2Augi7B7ZBFYhRNYvZECQaOs-1F7TQmvlUWXuK-xCas4Mq3kYjrzCE8ipzlIDpyUXIEZ_-9k_epjmIzEs8h5FxjiZ76Zc_Xg-YAphn46opJdTvtaemD09esB9dNT4Kq43Wb0NEIWJvscWud7L2rPqEhQEhA3pcul_VNHdMpb6qHroFVmfvlC2RZ7hgG2UajB1LuCtB9En-Fkw8Vpm1ZlyAZtvVo084Cbe7IMCd_OM_kObsApXBaCzpR3NQsmbEhk5N3XDieDv9D7dgGlXJnJIfGt2K71gNuGqEBRLom-E9zOoNdSN_P37t58vYXk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqjdqvqJlQpcW7QxPYBmkoYaGhLh2Augi7B7ZBFYhRNYvZECQaOs-1F7TQmvlUWXuK-xCas4Mq3kYjrzCE8ipzlIDpyUXIEZ_-9k_epjmIzEs8h5FxjiZ76Zc_Xg-YAphn46opJdTvtaemD09esB9dNT4Kq43Wb0NEIWJvscWud7L2rPqEhQEhA3pcul_VNHdMpb6qHroFVmfvlC2RZ7hgG2UajB1LuCtB9En-Fkw8Vpm1ZlyAZtvVo084Cbe7IMCd_OM_kObsApXBaCzpR3NQsmbEhk5N3XDieDv9D7dgGlXJnJIfGt2K71gNuGqEBRLom-E9zOoNdSN_P37t58vYXk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLzMRhyF0XIa6t05IpZ7wdy6UUiJM9-QOBIjTxWAF7JGAyy-oVKCbzKUJP9qKbZV3xoCeUsRcBIZSS8u3t1-LirKv2gi2wo6Scl2uq1X3vwOzPZ_YP0zoSdiYAgmjQcZx2FX7nY3xhzHvD9Rl1WPDucGczogr60IxbXYro6XB47VwOgBEBKNvnrJVL8-PVgr0HEaSM4n1tuyiRflFvRPs6_lBy0OWmPqh6Kzig3UM2DP-JdaVir4oYTTK6mEJT8Oeq3sroXOImWg55PvmuVWb3xppEFFkkUyhY7BgMDPyd00AZ9JhiN3Rx2v5oQ7i8FipSb3y_vUxT2O8u4PefrZCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=J7TqBcdyXgRJ85lLqZrdvGYwEhKc_TWzLkgNQIFd96z7hexuPvdG0l3prUiCCBf2ZubrochI4Lp3LC-6lCH28ca3raKJw9Vlx6apNQPt-Cev6MxKgWUb3cY1d3PSqGHSpidY--6uozaFzDT6Pew6-hXoLsS07GTDccO8AVSA2dNEf2_D4MypHDGkcP2RAknfEGPv4Jv1m7wKyg8Yj-hDdyywUj4jeoQ8ujOvNaf9fkut9Wa5eENbbki62riod8umPFZgDtzLaz95ggiskCjCkdro7zh7xR7JcXlhqT7v2dbzWcFm7XAOyY3Wf9FjVl7tShxkiGVactgFRBvkfj4gvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=J7TqBcdyXgRJ85lLqZrdvGYwEhKc_TWzLkgNQIFd96z7hexuPvdG0l3prUiCCBf2ZubrochI4Lp3LC-6lCH28ca3raKJw9Vlx6apNQPt-Cev6MxKgWUb3cY1d3PSqGHSpidY--6uozaFzDT6Pew6-hXoLsS07GTDccO8AVSA2dNEf2_D4MypHDGkcP2RAknfEGPv4Jv1m7wKyg8Yj-hDdyywUj4jeoQ8ujOvNaf9fkut9Wa5eENbbki62riod8umPFZgDtzLaz95ggiskCjCkdro7zh7xR7JcXlhqT7v2dbzWcFm7XAOyY3Wf9FjVl7tShxkiGVactgFRBvkfj4gvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=C6ozQbaSuuAe2oxbxfTxyAkuGm4_pHrdZV13QFa726qdVVpv-hjgojqZ0rCyNFDKK9a8tmLiwX9LKthTGLiQEwtlHs0dpPscZEGRkGtWARa-SzNuJcJmQCRFAU4TcNC9EaUeyetuK2jenWUYBFo3JbIxO-7KhV97hrwEyhYoKQDbYqT-a-qvNxHPoH02xQBh5ErDvUua1jCTBBMuWXWyfY2Az0s4DVK28wF9YUNuXDtsT_XnoM5m8rWtCtk0N1S4zKZxwFTmjRpD7CnjkP_IzlnwG8OASe1uIoOp2D7WFXDd3wVT9hSecBht8l430fxONEwEiuCVm3ZOqEMVgOTiPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=C6ozQbaSuuAe2oxbxfTxyAkuGm4_pHrdZV13QFa726qdVVpv-hjgojqZ0rCyNFDKK9a8tmLiwX9LKthTGLiQEwtlHs0dpPscZEGRkGtWARa-SzNuJcJmQCRFAU4TcNC9EaUeyetuK2jenWUYBFo3JbIxO-7KhV97hrwEyhYoKQDbYqT-a-qvNxHPoH02xQBh5ErDvUua1jCTBBMuWXWyfY2Az0s4DVK28wF9YUNuXDtsT_XnoM5m8rWtCtk0N1S4zKZxwFTmjRpD7CnjkP_IzlnwG8OASe1uIoOp2D7WFXDd3wVT9hSecBht8l430fxONEwEiuCVm3ZOqEMVgOTiPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaJH0mmeWjHSEI0C4bK_FzuwAVpNia5tKhvNQ2mraeSxFWpmAQ88P4XNyCumAWZVQcv4DdwdzZtK0aRfd-SaYJMbDU5W83FGqDPWLXdsBOHY3ovVS1P-qkrT8lhKVtCVV3UIzjJDMX4HJVQ3s9pQ-_TiLzLptLLpJGRQqjfHQI3mqns57M3SM9eigDJP4ELj_OCA5BHi8izCSJpitUO5GdHPy_Xy0iFJMb8qY3N3jkl-bF5FTYY_J61GhZNgpIYS3fR6YGylSi9IAfgV7gm0Os1l_HFw3Uejo84qXzytQUAGR0XNynchfMLRYJSu4JPFj2WwwGcQTRE_RSzQgEUcGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=I90Pj-SNM7qoQwGcs8pcwm3fwOGv24Ro-KdMrwTOBdprigHaG-7V0Wt6yB2rtXpaEAe5u_i6LcWhc51yCMVhuV7x6qzy4X87MMOb98M6T3Q2K-1N7mrgKuirx74ZcwJMY9kRc0jFVqiyvXzMbMhdhL82LQ_CEvo9U5WvbEn-PfDsRTt5hEQcs7el0TGgclJE9yqNL1W4FwWVbglZXOAYLk3-8a7keEvNlCFURbqxP_9s51mGYZ1rBYzL_BYYX7l7b4QUJxBnXivUGa9GbLiogUmUu2J0djEecfnE3buYaeeKTLqAmX38_nhSyYeY3edVlGMLgvrDj2fQ7iENU94RbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=I90Pj-SNM7qoQwGcs8pcwm3fwOGv24Ro-KdMrwTOBdprigHaG-7V0Wt6yB2rtXpaEAe5u_i6LcWhc51yCMVhuV7x6qzy4X87MMOb98M6T3Q2K-1N7mrgKuirx74ZcwJMY9kRc0jFVqiyvXzMbMhdhL82LQ_CEvo9U5WvbEn-PfDsRTt5hEQcs7el0TGgclJE9yqNL1W4FwWVbglZXOAYLk3-8a7keEvNlCFURbqxP_9s51mGYZ1rBYzL_BYYX7l7b4QUJxBnXivUGa9GbLiogUmUu2J0djEecfnE3buYaeeKTLqAmX38_nhSyYeY3edVlGMLgvrDj2fQ7iENU94RbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
