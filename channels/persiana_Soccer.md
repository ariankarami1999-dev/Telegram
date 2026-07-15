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
<img src="https://cdn4.telesco.pe/file/dxqpSRbA1xS9BN8Q3JEwY6Nu9W1COBz_7JWtds_bJfEuHltUyOkbrHLi6ruPanWHZ8_i-UAFJi3KXWPpjhdJIHe2WS3FCtIj3nni1a5owFUQ-SLyfCd5HMPJOOor08fN-RDCXd6shx35kLi4XE2iCkQOstc1r0fU5AlWqkDylXlsPqI5UycDO6Nwjl4EFRw6nt2xAT1R8hV12bL2zcH7A_Gd87ujpXeqNUjojUd7uZsUOF5nWnVTmrACUtPfFEKRhpt_Pj1Jyc2pXyJaf1B37WeyZXDB6RUsuibDvNBT_ZFuB81CpoQSxZxRS5cUC-UaQkqWlMGhMXeQt9YmgjxSAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 459K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 12:35:10</div>
<hr>

<div class="tg-post" id="msg-25748">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtWOdb-g1lc07xnC2M2hSLsZdBb2P5_9Gbg0qAdWpYKr2rksaYYCGl7H5tBDjASi2SDNLt2-8gNXbZKvX_6sw52DE7oMwn1-xJ3lP9hd0jSoET4KC8HCA_IE5-UwLy5ri9dQGplXH-iL8fYTYzyPy8EeTqtEBOWoGoCXJmsge3io-3Jw7T1PjaFbP0zpg7ahtZS7U6Uq4eXSfJPX2MEQGrL1SducwqRbcOEE7Iac7-o-95d_wQhdpbzz1JRDiUkHu0pPO7hWaCPpv7jbC0xoMatInuqKosMjrre3RN6OJIkgtRULgZt2nX0Cl21KNbAgj7SesakTwCpPx1iT08XkVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران استقلال: آسانی برای ماندن مبلغ جدیدی میخواست که مابااین‌موضوع مخالفت کردیم و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/persiana_Soccer/25748" target="_blank">📅 12:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25747">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB3qC-glbsoN8z-7G8g5SYBZ5DDYk8pO28AmSyIxZDI9i0rRmtoMdHIhWO0B-I8bn27jlKMo2frw6U41ZW6b8XL0Jz7v6GG-ACQIL0vNiq_l3slKzJA9EVo3x-US-YUzJByhzBsM3i-SKTAhWicuqnr-xsPY_3__PcpTtkcVWlauFH48FsicbYAtyz06iSNrGqm0yXt8tBx0C1O8rdiGOfFeEujyS-2jeOLmNsDvAyz6NbFLm7CPAA7SCEeV_yKuj5hOXCVMXGet2CmsCfpZ854RoGSu_3jKknArk2wRikwHo8ldPQ1ptheiYgBj92_-0zFEBNrzYttD7NYZWRsSYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/25747" target="_blank">📅 11:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25746">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWnRT52FHCZKEA9s5TT-JY46PKw3-fXgxyOT0Ag82-_Ovhq-mo466VMzp-E3OwYcEcUogzETOfLH0T44MoobTVeJPyrHWLcnrygd4uQD6hVQ456NG2iio_gW1RVef496T7JpCjUksztdeVlhQbejSvykOyjqKGH6qPODODqXzaQHuAFkZuLS6cglU24nvoX63HqZeG2iRGVwyEcv2tnk9v6k6VtpVtjGrak4a4_2EINsqHcBfMBO0gre4ES9QtdXlkCDxqSgWXV0xxKhvp4EV3ff3itTesiMp1wLfnajxOmS6aN4YfNkF6sffxAFTh-0IWvF7vLjRDM3egLMt07QFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دیدار جذاب و تماشایی شب گذشته دوتیم فرانسه
🆚
اسپانیا در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/25746" target="_blank">📅 11:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25745">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0ReULuo-p7yL1I9Rh-kcePaX4qgkwrbH_gOmKouwJnjaOL59f5vBoK5QPJBWyiRsa14MxxYjfqtvaSHGhpWNsF9ZqHAeb60t_qKPtU6x-Zde3eAZ_JqEj70v1yQTyI6EQ7aYjNY5EWZBEQwXtvN9AWfH3UFZy4s4p_fb1MVS-X2gksaRb_IsyKYYK5ZqXplIUOHxx47L2goCayhb8801LZOssbP2CjqjtAeweAurcos2xCq9EY_aiRrQy_NdCoLFvYbnD2yTozaNtgXJ-vhiKzOT84P7brV5ExntjslXjzelddfNwtgRbyqSISn7MVvjRqq0czVEAeUIqk7DHhftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیشب‌مدیربرنامه‌های آسانی به ما گفت که‌باشگاه استقلال ریالی به آسانی نداده و به او گفته که‌میتونه بره قراردادش روفسخ کنه ولی اگه بعنوان اولین‌رسانه این‌خبر رومیزدیم قطعا هجمه‌های زیادی به‌ما وارد میشد پس صبر کردیم همه بزنند بعد ما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/25745" target="_blank">📅 11:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25744">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyaNw6Y6nqRFN_Oajqw3NT5UdYXVNtRFrVkacvfg90C7zCjijwK8nLgEUjbCDVOpIwiup30mPtQwCwYWLOo33FTeOl3bvLS9zG4mVQUy2CuAR4ukXSZywFaLmFFGgKubxNBGxIqUqS_lMi08zjidR2y3kodQENVd2JqvenQx0LHjRVeDPpEmDQutMI1dMWojDGoUIhOjW9xw4oq1SLU8c4OP7krbn5nBW8YOBsNDfrM_CGyo7WWJwZoFvqt7qzGC7hiP0dGJTyE1vyhNqHFHucce0asKfERHxUxKzguku6GgOmcA-kcAMbh8zbNWLqkxtzk1r9gwhtelCb9KaXFFIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ پیشنهادباشگاه‌سپاهان به امید عالیشاه دو ساله به ارزش95میلیاردتومان است که به احتمال زیاد به آن پاسخ مثبت خواهد داد و بزودی با حضور در باشگاه سپاهان قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/25744" target="_blank">📅 11:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25743">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=FAzRtR36fE-MXtMTQaxpKvdt0ZIeXK_SoouHeNYPzdOvKtabN0Ps7geE0XEGLg3YwkiHlPemCrxsg0UDJ8PXkSjLTv8G2sdk-PRgZ2l_73xw6z7nRnrjskLjIDcfM1ms56161Cz7bclV3zJ17rg9_L5hjHkPfxRot3wq6hrEr_NeVMGc5sV3f3YXPOLqyBJq3JAvAtB6SR-RkSxFF4HnxtlIowW0ueJ2DFSC2jeZrnIf2kxCOVyjN7CLS6HWKWtoPq5HVwhru-omnilY7UwinVu94OrZiTmtl9pRQhyq5jV9O_UtFWtDaV7JCIF4RkAuC71F5FdxLNqQAWJjuXZ2pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=FAzRtR36fE-MXtMTQaxpKvdt0ZIeXK_SoouHeNYPzdOvKtabN0Ps7geE0XEGLg3YwkiHlPemCrxsg0UDJ8PXkSjLTv8G2sdk-PRgZ2l_73xw6z7nRnrjskLjIDcfM1ms56161Cz7bclV3zJ17rg9_L5hjHkPfxRot3wq6hrEr_NeVMGc5sV3f3YXPOLqyBJq3JAvAtB6SR-RkSxFF4HnxtlIowW0ueJ2DFSC2jeZrnIf2kxCOVyjN7CLS6HWKWtoPq5HVwhru-omnilY7UwinVu94OrZiTmtl9pRQhyq5jV9O_UtFWtDaV7JCIF4RkAuC71F5FdxLNqQAWJjuXZ2pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/25743" target="_blank">📅 10:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25742">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/25742" target="_blank">📅 10:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25741">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuF6wy77hm5XO5qkBs8D0PgnericKY7Rfe6ulxDp2ulIxRFz6O5z5Vjg8pU8t8x42szhOV1DImlbraccZOcV52-JAm14Fxc0C1wEH1-5CjwXn2v7sqTk0SrNf2ueNJXt_FeZUbH9qvB3ZLAenn80pxhX_a34sxI7dQyAAosIDz5DtHS7Mob1WSYFhNTfEY6nLF8bEjBvZ3AmT_mW7pSMGQKN0VloYzv--Vv_3ItguEJTrom2AGqub0d-kGfDeCYaFSnYQEXnBTpM-SYPdh4NWfkcl0NO5eyCipGSb9e2Y7T9oOQW0Pp3CUvsN64ad2rxjdhxhX_o_AlQNhxbY-RjNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/25741" target="_blank">📅 10:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25739">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJkRoIheXulO6d-j8NogDmAioConPDtxgojKSJGNNK1Psa3gHCr7aMUZM1M3Mploxs0TSvPA2PiuTjdQH2u_m7aeYDgH14Gs0gjR5lLG2DVwxNjiUGJACoCsM2V27GDhMAJTI4MuutrEw_Byx3IUnZ7GSbm_DJDh6u7Oe4U7RrAuBAyjnyHJ9YVPgRSiOWzJfzDuRgcWHTkZgwmm0nJNmH9WJhnRBgmu8oD3CZOwF9Ull_FGnZfwbEDGJBQ4K6CdiCH3HoDN8fjEeOCAEAwrTb0Cm9otdFdQVCoXOY-g9tTTzOv18jO1csovts3RLz-2TAl1enlSbpKZq_0IdWZmNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم؛ سال 2016 دقیقا در چنین روزی؛ باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/25739" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25738">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=iyV13s67lvwqfTssR5DDw5ekyrJMQARUbB91y1OziNc_O-K8DkpQF1c8AJ9DXlVOwr8slZbR4a_zmvx8p2ujBEl55TiiCAUL4VK2ye94hC8uBtN5pJb1T5DYThfaW9sndh0uozWBb65WW_9vi5DlUAotElfSIESeTMPk2THWz6b1_UgP2i9gTf-_mHGY9GFi445YlePpRyMs-zI5XOIOOdr83lrMMtFC5wk4bc5WFqKuyQbHG0aOkUVIlRr3ZA1CHBM_Xn-wMQxV9WluUrEIsEHwRVsbqk_-ZJcSoVayOnPf9PR11jCfw7LnjVWGoc54n4HhoZYHnojLzetHLR0H4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=iyV13s67lvwqfTssR5DDw5ekyrJMQARUbB91y1OziNc_O-K8DkpQF1c8AJ9DXlVOwr8slZbR4a_zmvx8p2ujBEl55TiiCAUL4VK2ye94hC8uBtN5pJb1T5DYThfaW9sndh0uozWBb65WW_9vi5DlUAotElfSIESeTMPk2THWz6b1_UgP2i9gTf-_mHGY9GFi445YlePpRyMs-zI5XOIOOdr83lrMMtFC5wk4bc5WFqKuyQbHG0aOkUVIlRr3ZA1CHBM_Xn-wMQxV9WluUrEIsEHwRVsbqk_-ZJcSoVayOnPf9PR11jCfw7LnjVWGoc54n4HhoZYHnojLzetHLR0H4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو لو رفته‌از اعصبانیت‌شدیددیکتاتور کیلیان امباپه در رختکن فرانسه بعد از دیدار برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/25738" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25737">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PI1tdyKYEXqznEynSe2ACHsdTOEqD3rmzxl2JC7woqUWcIPPNNfL1iY4BR67dOB_DVAbv564Z2HnGw8mD5cRiM557B0Ee69j3ee17kZGB8ttaFYJ5z1BQ2H02_hKfMTkiaVrTmvYgpNwnJ3xmfYJpCwLdSm-Npi9V0uj0jYEkwLsX-82TvO8-T9QzWCJ7-M5mx01St68hAQm5KtWH0n0TEFeTfX3N2wtrjTJVx_jKuTb0HGKHBTrI3NzHKKZnD3CQiQXs7iKDCwXaCpJv3yuXA8tQ3l9TO2QT7Z29hR8BSqYQREUmEn6ZNQcmuIXrgOqsy5melbQdY5BDfj-AqY_-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک‌کنم‌اگه‌هرشب‌با ۱۰۰ هزار تومن میومدین چنل بت ماشبی بالای ۲ میلیون‌سودکرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/25737" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25736">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=VO8HMxzJWBsCctLvx5tqSGwwqXTsp-a1uILpCuFolVoHjoB5cRQ0gqgpN0nrB-BI2VMPxbPHxSGjQRcJdpOBoWQcTem05o6keRkPJ_Wa96v-YAAmhh4clqw_8Q_p3ZInQ6AjQCXgU701VlJn8lfpuzJO1T-Ih5X5GPqdUyEz4Onwf4ipZKjqgSdZX6-vFw0kv3CPoM_j9jNIG2ymtIeP0wEeEytYvVj1jGnxQEcazgn55l_V5I8A5xRFUrlkerPODst0FFvrKeNPLxKTSEbO4TNQsAOpIlX37S5WLZB_dIZAkOgApG9oWVVSuubxM9OWduFHQxMc_hJYDlngFYD7JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=VO8HMxzJWBsCctLvx5tqSGwwqXTsp-a1uILpCuFolVoHjoB5cRQ0gqgpN0nrB-BI2VMPxbPHxSGjQRcJdpOBoWQcTem05o6keRkPJ_Wa96v-YAAmhh4clqw_8Q_p3ZInQ6AjQCXgU701VlJn8lfpuzJO1T-Ih5X5GPqdUyEz4Onwf4ipZKjqgSdZX6-vFw0kv3CPoM_j9jNIG2ymtIeP0wEeEytYvVj1jGnxQEcazgn55l_V5I8A5xRFUrlkerPODst0FFvrKeNPLxKTSEbO4TNQsAOpIlX37S5WLZB_dIZAkOgApG9oWVVSuubxM9OWduFHQxMc_hJYDlngFYD7JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/25736" target="_blank">📅 09:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25735">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvOBbOZfBTWbmpeJhPODZfEtupRRRFqUeT3J6WG7kKC9sNB8pSJ6vyIT976TGTpaYw69mACJxL8IrZdNxw4JwW3RBAs0zQ6hg_6ITtrL5qg8UXrmj3ziIOoJvQaQo-Azv6KockadoinxLjd18DBArA0F0H0GUutadzfZgk9XMWbq4bY37HOy-K4ZcL42ondJHJ9skgBs2ByhwkAYhqhwW7GXwvUQGTRTlyJxuhtL-QUpw0RE-ArNVahDoKRedLbJdKqxFr2dMgvlWbB9xx0kpXfGfdHlmiECo434lzNvOSroT5doCMVnFYPHwhNEQM2pB7aZI0cUZ0Uc3FyLFYakvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/25735" target="_blank">📅 09:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25734">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5a_Fz6mUt0mH2M6SH7cr0e7KP0czjdwgiebObXnVysctzWgTRMXGtrjNG0GI7ySx3li53T_BP80qAfuL-TWv8NwxNpRuV681liXNUcTs4CdKDuqiBt9mStEEro2cAMGOTDyTSdhiRK8YR-2Jlm8NuZwQa8yvjUBHJYFhBycSmqqGi6eXe2zlPsa21wtMmexMdlRa5VH7AuscLZXszUTaejLz9qiraXI_KHXaIEvzOE6IcoVFa5-q1eWKoGmSmETuPG-k4qaUpOHxt8wMkDgztKvcdBATpjesajUJ90BlvS06VlMqJHteZHbu_dp7TSzySsUfc_Jh_iUMK83LR6ZFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گویا فوق‌ستاره‌انگلیسی‌ها شارژشده؛ دوس دختر جود بلینگهام: فردا یک‌ورژن‌جدید و فوق العاده ازبلینگهام مقابل آرژانتین خواهید دید. مطمئن هستم جود میتونه انگلیس رو به فینال جام جهانی ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/25734" target="_blank">📅 09:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25733">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=Q47ubYABGQhgijM8wJuVrCXLKG3_TUb7pdtpsiCMfvanBEevqKqOZ8RGPt73gdb4KCtvVrzHoIHOiTU5fUvJ6YBUygkDa0O4e1IkaJ1XO-bmOw-l_dCQqW2uKjEgxE_KvCn8K-kO2syQMGBna7oCdVDCekwUv7TJHXZFuy8McLxoKf9hqjJc_zH2NEFCTzCGvjV266F68ob0IaUtJbO943QJ9fws_frPI-nZQgdDkqa2rX-6EowvhryAuX0OZyRR9G4mVXZp8G_QBVZ2WC3jVeOeI-PrXSCYBBvNdEnCmeZMaL8II6I7l9LiV3Tk1Be1ku8_aoBM-riyfx4Ekb-we0aMItUYgQAgBj_E1Oyz_pbGTDndFem2hxWWKGziLIIa1RJtGWI3lhrc6A4hRj3bwtJXBQ34czDC18V7QCrvKKVnoI5zEX0UFe1lLFQzEISYOQJbSqJGvq_5INIV05hGrmBz_WkjUhmEsGnnYPo_-r39aqX19YNAQ7_PivME4Q1yokauEcmOAwt-HPKl9xkVLC_HhmFCt6SJ9CEuDcQ17Ftz369kn3fr6D6TYXvAwWmQumPecyrlRRdVPc7vDS4MeyF1JvCFEbu1-0owKv9HpUN_5yNazYtDjXsgmphd5zd9qMb9zP06n-RQxlYcbcVyAE5G6FYnG7lO8zsn-l2E6ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=Q47ubYABGQhgijM8wJuVrCXLKG3_TUb7pdtpsiCMfvanBEevqKqOZ8RGPt73gdb4KCtvVrzHoIHOiTU5fUvJ6YBUygkDa0O4e1IkaJ1XO-bmOw-l_dCQqW2uKjEgxE_KvCn8K-kO2syQMGBna7oCdVDCekwUv7TJHXZFuy8McLxoKf9hqjJc_zH2NEFCTzCGvjV266F68ob0IaUtJbO943QJ9fws_frPI-nZQgdDkqa2rX-6EowvhryAuX0OZyRR9G4mVXZp8G_QBVZ2WC3jVeOeI-PrXSCYBBvNdEnCmeZMaL8II6I7l9LiV3Tk1Be1ku8_aoBM-riyfx4Ekb-we0aMItUYgQAgBj_E1Oyz_pbGTDndFem2hxWWKGziLIIa1RJtGWI3lhrc6A4hRj3bwtJXBQ34czDC18V7QCrvKKVnoI5zEX0UFe1lLFQzEISYOQJbSqJGvq_5INIV05hGrmBz_WkjUhmEsGnnYPo_-r39aqX19YNAQ7_PivME4Q1yokauEcmOAwt-HPKl9xkVLC_HhmFCt6SJ9CEuDcQ17Ftz369kn3fr6D6TYXvAwWmQumPecyrlRRdVPc7vDS4MeyF1JvCFEbu1-0owKv9HpUN_5yNazYtDjXsgmphd5zd9qMb9zP06n-RQxlYcbcVyAE5G6FYnG7lO8zsn-l2E6ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/25733" target="_blank">📅 09:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25731">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b512fOGI-5V7KbPwI72KeBdgI-u-VWldwKSUuXmHcjqbL_MXPNLg-P7wB_LJgDjn44qpYSo_R7lSWan6hvqQc4GnbqBsexfmo9w4zxZ7XLdmT1ZOXL-HzktSq_HOulvdcZ8keIEntM97lxQxugTjRYLRgWmMT37rp7FEpLrvntArAs4hgyOilAvltbe71Om5Jr-VfeVb6YrjMsY9KCSxq5dEz4gO3RJDiNfShr2BUo1uJr9OIZ1TvEhleaH0f16tbwodpWLYOJwSfI79gezKIyAiPNXgt2_gHaEcQ9Tk8HQuQEog0KGDwz6IEWO6fU9hgc8Au1OAzTeDBkSAP6m_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/25731" target="_blank">📅 02:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25730">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oem9qpJOtXsdSezFGb1gw2DJXjfo-xTc4HGH_Ot7rODoD3hDquVFPUT38cR3uqQi0MGa3Et7sgyh4e9kIG1VZQMVpM3NCIR9J5Cgj1etlj5_AJXYY9ZEwmcDW1dbs508ih0SGrdQQQYbqC3OeNwpJfT_Q6zvVnOWxW6U2c0ywUFkFDpmUyYUGQR8wTr7WmzDDOdnXLc36DkbFjdO0QvoudZRUxDHWhx3e1HjOQ3t8mV904Jmisx8iGsG9gfVDnCl_rkjklt_neTCpVsqI7x3czgrtrl7wJwz6aSrxkeovmH6W6iWAorZ8UZpXcav3zwBD9laj1DqMVJObi2TiGUlJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درسته که کیلیان امباپه امشب تو زمین نتونست گل بزنه؛ دقایقی دیگه گل رو توی تخت خواب میزنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/25730" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25729">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpxoPMK5xe93eWcMpICWYARTqa73n8hxxVpaL5QRu96qAjDP4LEQ5thHCcxKhFjmTBwngrrAyH9nEl2ATQKa7PYMe8NWGnkKqn77D0IgcqQDMS3vElkMrQjrdUsPhwA1tS18bXek5urmolJ_3QNaJBeuk59C-C0fhSvFV_1KqoJez7__4O6Vu6oosv5q5sdDsVpbxT2EPv3_LsOLZT-f4KPBldV40aJn70FBTHvECAcNVqs5Hc5Vkub-Sg5ShaU-qBEc5a5iBw0o7SoqUSa0N8GcfSWrz3zfG_Q82JR5XSgeQWMyjA5mVEbFayNQA0GdzxQ-ZGfhApXfRYFRWviZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام ستاره‌انگلیسی‌هاگل‌هایش در جام جهانی رو به دوست دخترش که قبل هر بازی به او روحیه میدهد و او رو شاداب میکنه تقدیم میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25729" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25728">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJQ34acsS189yaWTHx1mOYY5gJbhu5nxxHGQ1NDsFAeqzLCgK99lNjcZgz0jeIep-xdg8cxT-XWrvt4CTOCwHlZqHL0SWDwLaWEedMpoBb_krfX9Z-_QGG2E5QqjVihbxg3GKt9Se844HUknXYjfBekDwdkRjRw2HxhsNIyIVTHotR59NQgwneP2gE6DhNxl5dUN19nugel_gF4afNhuV2f3VloYt-lxqIeXTkcksGeunV4j_SFkNscHuBTO0HDl8U7p53_ktmxyD8f6XDnNTywFnbKeCyVBa6su-ff-V3xl4lTvjKbLQHSjc9pYCkaYqmcxYcCfCtmxcPOPWVYVhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/25728" target="_blank">📅 01:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25727">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=sCEL6Ghu7jZam2EicwhkFdH4rdQpxTGk-YPS0RUMUr94pmuh8zo2LLhbLm7SUnfsV2MhI30UGo_cmebZqM7wOju897gnoOS6FFFCQSYcGfJkkFKdxqAFLqTDW-vt8DLI3sJGDBnpVk5nz6OmyzILl_3ICySUVTEb8d-UDPrA4Iy2yBB4bojSyTh86g6mV--5-oK8n2YmSgwr3dF-FbQ1KQkYdigk7FN7ZQEEpLZB6ebPnhLLbWPFUJEPsgx2e1RAwhJwD8PtqT_OWVA2YFNWaJHJwuBJZnRGTtrQSWbZQAXN3cbmwPDCV6HaziJZXo5gDJDQDJjEM1g-3FJLUZv6WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=sCEL6Ghu7jZam2EicwhkFdH4rdQpxTGk-YPS0RUMUr94pmuh8zo2LLhbLm7SUnfsV2MhI30UGo_cmebZqM7wOju897gnoOS6FFFCQSYcGfJkkFKdxqAFLqTDW-vt8DLI3sJGDBnpVk5nz6OmyzILl_3ICySUVTEb8d-UDPrA4Iy2yBB4bojSyTh86g6mV--5-oK8n2YmSgwr3dF-FbQ1KQkYdigk7FN7ZQEEpLZB6ebPnhLLbWPFUJEPsgx2e1RAwhJwD8PtqT_OWVA2YFNWaJHJwuBJZnRGTtrQSWbZQAXN3cbmwPDCV6HaziJZXo5gDJDQDJjEM1g-3FJLUZv6WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25727" target="_blank">📅 01:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25726">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGMHT60lXFwxiJ6BYiC1U7KnpCUBUHQ3uUocKZwRAqo63O9LcQt7C28suwii0CiXl0d_hVCzWOV7Gm3uQue0yW8g-LAh8OYvNjN3xMErt38HpCB_uvuefiNOIiO_xLiKIcgJ-NO0ZzzThe9Skk6e9dcp-tWM9L-ucJ_cDFNwqk359lTgG4EyKrs9c4BZ-53IgE0LMBvGQaP40nIM8rNr9fvai1emU95vHA69TEK1ApqMP2Is1h39BkytJhaFWjYYoGwAfWD9-E3-OW2DzReS9HJgv5oprSJI9PJlc9g30nSFJr2RrwByZKukR51KCMQ7JnyV_AFILKawd023uZ13hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇫🇷
استر اکسپوزیتو دوست دختر اسپانیایی کیلیان امباپه امشب تو تخت: آخه من چکاره‌ام؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25726" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25725">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8mBkTBzs-Cgph1A_WzXP4LuBYWeaPnq1S9wNDz-CgU0vPf61iK_sVAFxp2RYWOoq_R75ft-9C-I_5i7wHmIzqR53AL0lPkBOeR4nfgLrP5-id-h9hxWfMxxGYjynjegs-ODaGSzjTBqzbgoIo5RLrEqsTPjSCtvKGvsBNG3KknxNVkdMaVm1samDfAWJwEV2hLZmyR_h3er9zOn9gMwugbFCyKUpDk_CEAjwDcho-zReZaBVxyRCmdD9-iwcuXhuvv6c15b_U_IMgejRGPnSsadExUAg0Jda1VUeBnUVP7rU25t9NCQ4YZpvITo8slWLTmN0fnNyb5SvEf2zREzDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25725" target="_blank">📅 01:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25723">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IlEekSHKfllcM7yk4G1FZ8wN4BFLc7nFVTfOZZhsMu9khEMXp6infbqSbISxpISqYgHfMI_lGxLi_9Bi6xAY6fcG4tXYTeKc3blr5aickVrXUvZ95ZW1gZWaUVxMCObpkxvJq1fVrUCAiwfIXrro580WuEwQbTmr16zm3acoT7K2NbOaEJej21ebWGcElnKYbGEXulam_KMhge7u1CNJPVWI79EQ0eLSpx12d_B3vo20StLScfgu9BX6n54zyQeM_ntz8ftkdPXg6JneFNIWtL1OitJ3PGSVjnd6q0QX9FV3hDBvtRKEluj8-azN6QpsSk9p1u1mXukDlovj_Y2zVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dH-oJtKIele4S4cI4AmUOh9ocUZ_ZO0orx2rYKJ33cmli87SBbT3-QaBqlXJNiyvKQNncCUp-2qqLsZNeVT3Dcl3vun-qH7jldQ0SIVXUAwhgGSZWLTHs0tIeh4lBqND35AL9xu0_jaa2tj59rKg4azG_4Zq4oxthp6cwVBtgGormAY4B5s8sAhe8C5SYbYd4n83-Viks4OiL88u17pyX634SSmpwBIp7jLdsZC7iqliTeXY3GZ1OmDnwoZ9OCIdRM8Y9LO-CDJMsw9qfdZ2CMuQYiRFNhtVonASPeIoAqyUJB5umKe5SRDryyIMrew3a7xZ8Twk517EcmNqzmjvNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25723" target="_blank">📅 01:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25722">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R61qpiPap0R-u2vpbNVVcAZY3pmuak5_4-Pdph3F6LgbKexJgigLMGT5qkwchXF2UEsf9S2x5yegCuthhFXid-ngJUaWDmPvhVBTRAJwbe74ieW5FnA9iGzHbvzdwv4qdS44gFQoRJMnZYRCFWGVJNDxXGp383hYgTi55N834vk0qTpmXRo5TCYieAuuyslVJU0HYbmmUBxmYIdCzEpExa-kNO3Ho_lc8NzccIo86surYJXAOIdqZuPNul_C6XojkoeQILr8JPJSGjiiJe8RUA3eu954nLCtifP7kw32MlbxDgva_kcOuBysyAw02eam9iRWOpTH4sKBgaBlAv_-tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛
جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25722" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25721">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pt3LIVuUh3ZsjB1Dw6_8ldm3JhYeeXhgrbh_ps2UZNZc8P9Ixlpj1JB8HkKM2Sz05iLStMHecFsFTniy9YUOiboB3bM_-zz4oTUW3Sf5H7HzmEySQ0GerAE2Hb8pMNu5YzztPEw9rD1hHnRxIBaNHdHt3h9Nu6wDXeirsHcyuZav8EuB1uPodOH81kIEb3oLWEeD4jKmFExyyc2oTWPAYwdrAKcom7zVHLXPjDjXI5lwBCj3QxQrE571ggTin9nNtZvg8gmWWI4GFMpqi98hwbqrSAhUupyyVFjeDogh_LA1YKVRe9GdJMs0fghwYcx3klJPLhqU3jfNB2BPDwavEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدار‌ دیروز؛
راهیابی اسپانیا به فینال جام‌جهانی با نمایشی منظم مقابل شاگردان دشان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/25721" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25720">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcyB35bvZu9XHV1vhMX_fAiy4K4h-NWllhkx9Qx5Nd-fS2vcqAph8rtcNgjrmDHxf1nb9aUVfHxvhKmSMiPQSqG4i7lw4KY066B7rYtosQQSd23n_2zpmWCIdt6jHMRoiAckqfjcbwSOYVulmYZzyNyx6vFWaWCdTgU_kjUiuRykD4A3pHBFD2ZM6Xw262veA3sRiDOubULrK5mqBMjewq9HX_d7xAt2iK6BXgOInTKQ8AYGctlwsUqputT2SZOCvFUqU4SVfQqsheF58yFs7XNP5rCAjDiLXwqqqvYiVdfvB8CkUHlwnboA1sOg_C76SuMdIedPGP6x02_FNlmjUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ زین الدین زیدان برای قرار داد 4 ساله بافدراسیون‌فوتبال‌فرانسه به توافق کامل رسید و در پایان جام جهانی 2026 جانشین دشان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25720" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25718">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RiKVeqflHnqx6S_JyknpwZnblAolpZ_IMm4LWD5nC9ZB6U1ViZzpfPtoCuARES2whKSG7xkvHupoWJJ7nngqOWtes86q4iaHqpSK3n48OvjWmnHiz8N-u1ZzrnFtXi14lUsafrTfrqCN7K3SJ-rXJD2p8_eTbkVQXTkQNXAYmRpGkb-vyaPUQvimyIn94m4Wp8sQgsfr43Cgf6Xpe3wdO089pxZUUATqgB40Gvah7O2MOy4n-DQrLp6uv4g2zU1raLMTFTHrA0f0D7_iLHEhjmkCc3BjJjyB8m7PSzZlHvceBqktxKJ6SDHkDaUUkOTpXqS4rCCJr285NtkON5KuFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OG0ySUQPDFlXak4x5S0Yore-8E57wvc5oz4Y2nzEXjsc0dUHmlG5L87KdgOicIDckR4otl4fL1G9LEXB0V4JuBoru3hywGV_9h7ytUlWxS_rXYJLU0PQuGYRcIW7veiAfBWZDOWuT3x9i8fn0XUK6fUsZ9gKZ92EpiZyR67x46yGMCLK93Tk_WZ0z2aG4mA352l3WcwmzgfbokItmDJ8U71eRsItqGC1NTojWlmb75IyvFSD1PAX32ejIXDSAqRcX-KFBroR-i75KHJ1e-dTSLLJBQd8oNSTBkV20EE9CIC4k6vSOcazr-jFYke83Hgar-6v5ICl2JsF8r5Vxuur3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/25718" target="_blank">📅 00:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25717">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8cdOqqxHgPT4CqNs01bxwU2J7mfRk842DFPuSUTUS8F95-InmHCmV_D9IFEgyK8Upfnj7yMdgjlcu3NY7iE5su3xZ-GNYhhZKIhoV3LyaCTUQPgvBSXIENpAnWLPrBUXvO0Tnih9MxOkUvRvIcfK7slCfnCOuu_RgoZ-Ms4rFdVwHOnUxD3TiJQ28emZ4dxMvwzRzxTE1aXNIRzs5is4z49a95Uvhh0xxINzh0C8_kdP0M-RyeTjXJ0YMQr4RHKBJUjWBTLL_aEGkva6AbhcLR9x4m678_Hxa2jvOCZEqbW8tXTO3EqabyfpiHIohcq7Ihi23gSdCuRnRUba-vx5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25717" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25716">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDQTBZbd_BrxGpQkzRm8JLY6Boy67c6UK0DFRn3OYcMwzsneouqGD2JDXfWwc58RFm0l422hR4KWQB5eycrZQh1-sCuExvt5pOI6vSLbetmiUV-pR1v1RWrrvdWSePZTyzx7vVYf52Odh_oihiu9wN6atWMiBvoiHfXLXArn1l-vGxtkRHeoZSuWEJe9WvED8lqXQLKyp4vGi8MkaUGopYEqySMyec8OiD_KPAk4afk_O-oSYvCFFvTghiwjnGfhzEuBTFeHdFsPLk9Oqkh0AeT1YPh2zFq-jPQvspmsSQED7nn-sAw4qmVfGTLSV555pwSqyiF7WtPmJLrgu0qvLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25716" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25715">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7CdIG7FtWFB-sgKlXwG_deBgO7XBCaZvUFjKwWOooxYWtcLm1wPWhjHH9RkyaOgBDpBYDuxcfC8LUN1eoklXyCZa3hNOzJykNrJnUOp9cZWaeDzTDB65AW-9G7hYElCQARgGS3g3KmUGMabsTNkY5TPIqggrXrC5SrDvEH1C507hWTGPJr5sEXWF9Oa77Y25UQ7APEwDp53bgTxhQAtiP937hqlKE2gks9ZtYWPmuvW6f9tdRAQicXygwPslXcU14KPGnuS_z0OZrZLPL6vM1uhoFGlpbSzEMoLRGYn_6V2-xuTieEVoy9TwQYfNPt34SBBVQ0mTgIvoXto-9ZJnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25715" target="_blank">📅 00:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25714">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3rb7R7hhDXLy9Y8Ybfo1oVKZLRgTEMoVSMRHAawWld6FEyIB0EUIzMGXSeO22434eyRGE8XumkBh0sw8w0jsE14L2huNklupyLAMdwkVYChRvRCue4fna_nst9JyhPuCjgsoc78G2aNLo2ESWUXaKBh_XdAFGuEGc3piwgzi_q65f2DYSgAl72f3eLuTFmvGgYAKwu4m001VRJpA4vpIjfm81nu1MEnBz001mjCk99ej84OtBYPvVviXnSxuE6xWGLyEhtCHX-UDb_A2w_toVhZZU_2mb93sK6t_wi0efPkzqJv4KeFaJHSl4DM8gYN3hFZfLSqEL9AhHxsqOm2bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
وریا غفوری کاپیتان‌سابق‌استقلال درگفتگو با عادل اعلام‌ کرد دیگر نمیخواد بعنوان دستیار فعالیت کنه و به همین خاطر پیشنهاد کادر فنی آبی‌ها رو رد کرده. وریا میخواهد سرمربی تیم لیگ برتری شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25714" target="_blank">📅 23:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25713">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vct-i5wFP8bD2Z_lRkGsP0EwnTss3ur7snb6IWMc-Oq2Tk3MpHE-71MjZJrA9thVyN-NbmCAoTVcfDtdSSZ2Agfjnio9YDeFPLlbuZGeuevO-1ff9K7wcOzDA4TLqBJxNQLpTf1kR_a_PWzXykazeb2p0HkXxr8iCCEstRuBmhbrUzuRMwCRqp-qW_1QudNbHRMM_gQm_hVAWKj3qGDgmaW9hS2aA4IMnN_Oxe0TSgHYnoVd643VyiII0N3URuyYgZr9b_YDtuiDXQLq39hPxf_WC1YPj2eR-NSrs1g_8kUxm0KNpUvwtNwn6IZlwiQjKhS51R8IrMxTiPsQUXp0aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25713" target="_blank">📅 23:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25712">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TI4_h7lSGAvgX2ctnn6sbtbWrkaSydQR1lt-dmdHMXiOb6gzfEquYSvSykT6btRqTHmGWcBfyl08LPLYcS5BfTaFZ3ELRqBTcXiIwtTjG5TB6rjFcvWLJljtAs2iQ7lRokYlTsPJiworUB8LR-L2c8LR7xl1ok6tXs-qsROVTLWuWSEG89RfFFOjU0QVjnXT4M_9LofuAkmDNWdCW_TDPNDn1-wUmK-mY34sXUhSJ7PygWpKQY7KoxIPT7DUH3dXv3vsd4YRFcuwPSzW5tzPaCNlbwvaG8_GhaE5SDKr5wz-iXrZt8M0k77aDuTUSK6m9aAi-jbBRR4K2yX4-Ut0Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25712" target="_blank">📅 23:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25711">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SURVbIs-qSSe-4CBisPr8IOj18RUTpdvxFg42Q8aBIBm0lGnOgVVeJ0R8GFJFzemgTJ74yPUsKCbbES5HJh7xZfWszAhTucxnrR_x0w8uW-n5C5FqM_JTLd_B0rOvR0DN8E0FnPK6C6uPgkut2WIMdP9hLKfek8m2s5DlLuEpTthh64aHb3RK_7uIR6HJIyu-m7Pe4HM1TAkYObZkEvMOJ7SHwNosGMoNYHMVgOQLz4VLehcxV3xViT6pwJII-gpDxm6QgTZ89NJkcFJhM6-WaZfJV2EjwAZ14-FbNZzUyNleHhoepDyyYDO3C_giYG-vdG80jflUsCSILeG8FPe8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛
فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25711" target="_blank">📅 23:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25710">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=oPAvqlZBcj1GjAw6ldLW-XcQpegXeigXOLi-aqRrzC4hpYCSwzW4BdcjUOvysuz7UBp8_BxDqynkO-fMXnd8-Z8ap_UO_mQpeCVwqvVWePoBscu6kePFp3nHvyatO-guX0y_kxlpUsSCVZz7LQVOgl1KiYY7bgOfurG4JWRmyJ0Q7Fs8CiK_oQgOUvQMEk6X5E40ro65NWoZVBvyDuxKiM3jW5ygYwOphQr44GI7gwZzyTW39DEcezPGhObfy2VapXI5QPe2l967t1rturz6Gv8iV01cuPVbHZEp-nQAlTmSIobB4nSoT7Oou5fVhZxzUoR72292U2sidtjGzcPWwAhyv9H0f-VRc6aUm0RHEvEk9AlJdwbTBJzgQMZjO_kqaVqwVFn5EdNcQzX2doRCjzYqUcc13TM7RJnxF1gMTSALgPeuoRqPkbXs3-_0wAfGbMPseoM1iun-qDge0mLRKVfAXUZ58Utqs7woHfn8qDl9_YDWHGIGT_ncmq3hGlu-zCmn10yu4eW7gLpVUH7ySYpphi-On9mQGtNlDzv5hQQqcBpyeCe-vUmqlkXbwXDd_kk-qot8kaNo0lOVOUQm6Ewx-uCeT4CDQYuq-ZZPS6XLK01iUb3WDUEirFs3xwxYKycaJopP8jJkZaWZoiDqIUSCYc5j18XDn5-sopvYC1I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=oPAvqlZBcj1GjAw6ldLW-XcQpegXeigXOLi-aqRrzC4hpYCSwzW4BdcjUOvysuz7UBp8_BxDqynkO-fMXnd8-Z8ap_UO_mQpeCVwqvVWePoBscu6kePFp3nHvyatO-guX0y_kxlpUsSCVZz7LQVOgl1KiYY7bgOfurG4JWRmyJ0Q7Fs8CiK_oQgOUvQMEk6X5E40ro65NWoZVBvyDuxKiM3jW5ygYwOphQr44GI7gwZzyTW39DEcezPGhObfy2VapXI5QPe2l967t1rturz6Gv8iV01cuPVbHZEp-nQAlTmSIobB4nSoT7Oou5fVhZxzUoR72292U2sidtjGzcPWwAhyv9H0f-VRc6aUm0RHEvEk9AlJdwbTBJzgQMZjO_kqaVqwVFn5EdNcQzX2doRCjzYqUcc13TM7RJnxF1gMTSALgPeuoRqPkbXs3-_0wAfGbMPseoM1iun-qDge0mLRKVfAXUZ58Utqs7woHfn8qDl9_YDWHGIGT_ncmq3hGlu-zCmn10yu4eW7gLpVUH7ySYpphi-On9mQGtNlDzv5hQQqcBpyeCe-vUmqlkXbwXDd_kk-qot8kaNo0lOVOUQm6Ewx-uCeT4CDQYuq-ZZPS6XLK01iUb3WDUEirFs3xwxYKycaJopP8jJkZaWZoiDqIUSCYc5j18XDn5-sopvYC1I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌جذاب‌وشنیدنی‌فیروزکریمی‌کارشناس‌بازی اسپانیا
🆚
فرانسه از تسلطش روی زبان انگلیسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25710" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25709">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=X8aliGJimeS6UL86bfJTZjMhV8xWLq4fSUlI42d_4xAuBkfCr--jNrPAU-S0_gWNOh7bymj_epFt4g8T3x5sVDrLoWIk9QLF-gwpsMBg0ypB9hmgiid6fSku-WRFTriKLmB-fioSsmgTmtjgPUIDUOr-M8E-3DAIvYWQT6w0aa0TYjrLq7CknQ5kzicOxlzM5LSKIvnMeooSFDoH4dPF7xJFQ6WIeUF4M_tT2Jg7KgQKyI4fJeCqLXobk6OTJusFXMsXg0HUK7L521zQy9ouxp8vWIYeY-1xCH3U_sniAZBfhN0jZrwIVWEr4_lnaTKYHCl-I8-CyC8vFW87MQdM8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=X8aliGJimeS6UL86bfJTZjMhV8xWLq4fSUlI42d_4xAuBkfCr--jNrPAU-S0_gWNOh7bymj_epFt4g8T3x5sVDrLoWIk9QLF-gwpsMBg0ypB9hmgiid6fSku-WRFTriKLmB-fioSsmgTmtjgPUIDUOr-M8E-3DAIvYWQT6w0aa0TYjrLq7CknQ5kzicOxlzM5LSKIvnMeooSFDoH4dPF7xJFQ6WIeUF4M_tT2Jg7KgQKyI4fJeCqLXobk6OTJusFXMsXg0HUK7L521zQy9ouxp8vWIYeY-1xCH3U_sniAZBfhN0jZrwIVWEr4_lnaTKYHCl-I8-CyC8vFW87MQdM8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس اینیستا اسطوره اسپانیا خطاب به عادل فردوسی‌پور: باعث‌افتخارمه‌که باشما حرف میزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25709" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25708">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOBkqGPFYBYuhvzD2qM_dvdJRawKuxshgollvsi1RuMETdVqeDMvQGZm6kE-wm9kWdOcET3mD4ljwbHjRhN3LCSWv8SOrTodxzwjfzVSr7lqKlMPSm7sXOKEVdV5FNCTEwuTww6h-6d6t_l0gpWP0M5BvZ6-FPbu3PMfem_KZy8w21u2p232heyNH6S8uLvkpWXZpgvvZDIw3X2rjt7Moxs2OEU4Y-tLgg2xqD8OTZozDR-U9iP7GdqWApEzuiAzkG6uUqpiPubdrJqRsDqb3saAM3T_KTZRUT7l1M8lHclIri7rZxyeek_sLuW47i_ZT5G2RBLvcCbjNumAs7NuRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25708" target="_blank">📅 22:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25707">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUfrEGCsBtu8VwWjUFuoz3h3ygv9TqFViDxVqDJgBurlsvC3d7lLo9HWmdabzvlLlKI-bYjxs2Xbai0wPFr8fQPnGUBGamQB_7LcQePV8oImS9kKyrwEkweY9HujSgYVYoAQaZ5tjeCMA1nlA3li7QdyCAInZxYvEFiVAq48A7lyerW7o8Mz6klBMhWLdQw-ZmjZVko3lZhXTX6lNxKlRh4OYu7RQOQZ1RojIA3KO6AZxCq9yUO2rPAN4UVQotxU33CFT4boXGLlzbgmTrfHGTnctZXoXNqVh0bFqpJY8lC1VIJ8txLIXTVuZ6Ye7KkKhgd-sKeNlA7uMMsvHaVSIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25707" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25705">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fg8Gst_BdCKSTuJEH26yWhWhj3VEQgLQdZc8_s7gfwXH5YKKa3Q80yiy5MRLQJrLo8RQr_jtabPiNIB_-uO-q68QBGO1oJgiHoOz8CS1H549rw9869coWy4kAFJ1HGcJQD9PzIvcRgyj35crfo5FVBvCfmToaHviiY8QkgMJVSJsD3SqOojLf-3vD0Uv1qtAIwqaIzpc3tuBgR-riFjdjfo_hpyKgWwYOlMawA4gx4AyQMJdq3FDTiGeRSZXV8m9mW6fk0wR51BZErJpzNyJkwFnBYWsi0ipYPAI7CV7YV2AEKRyasXtXUbFh3Ktnv0bGQjb241bCOviAkn0iiAyTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h6h_7xTasqZVTz4HoUf5W0rAjDsP_HMw3jmHYbdZ5eh00JvYp-GPyBNTVNe3IaSfUptKj-dPgqnPkLZnmLtip14CDsHVdpyMNsqr9xyM2qKWQbjM-acQDFaCYfI759IQzX9TRxVHbQZG8EG_6F_8q_7vBwd-_j_iDGPcgHzgMWWXG2Z30Pau9PJ0a9XT1y27FQBIwbhl5oImbq_wlJFYjKFMHiiE21HzTDLfu-_m0tR4xem5cvGwwGTUAvVlSyIjsztlv6fMZpm8QAfXrXHyiwl0RwQMp60UwI-08ox2nz-vkm7v2OTF_L9ABBi5ffbvE3gc2h2kbQ3YYoc7frKflQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
خبرنگار معروف‌ شبکه ایتالیایی DAZN که معتقده تیم‌ انگلیس قهرمان جام‌ جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25705" target="_blank">📅 22:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25704">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V00ZeuZ605uFEC2Tc_LoULFXNeZkHclLrXjQjYb1VltfpGmhql77Mb9-5fn9s2Qvr5Qxp5Z7VfnNsHP3VvXCBf3VxACNCXb5MMzfylcQh-IqZLZgXKP_Ui_2rGJ10wwSD4Dj9FGjWZMvEwTXYneWHxoKtxxiXL48-6dSsIzYOFdkryt6OfEPtrkHVZlCwZDwvSEkMLYmZpu9spby6BGm8aNFNbzbzDdbOZ5ObSC_Dqv24eR1qASY2c0wAp8XXuABKti9zqmwOo3P3oQo9Ari4d4LUQTLxv9gnhJUr_QLvIx3ZnzMZHlOXfAYmr1lyhcTyB3Uh4u1xwWW1D6gY0MbdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهاب‌زندی‌‌مدیرعامل‌‌تیم‌نساجی: برای خرید یک بازیکن‌دیگر از روسیه باباشگاهش‌به‌توافق رسیدیم که روی 1.8 میلیون‌دلار این‌بازیکن تهاجمی روبخریم اما خودِ بازیکن حاضر به امضای قرارداد نشد. پدر کسری طاهری به نماینده از خودِ او امضازد و به تیم‌ما اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25704" target="_blank">📅 21:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25703">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lm2XopEJvD94zTVNKfYlQV0MVOTam7aINfcpgEzlIqXHI0X1QItvXMGVFGtF8tVCbo5LDBfnQxPWwMbHh_Xd4BeaHbkzxZaG3jR45Yk1LM8ytYsbN3GkZseh_4Xc5YA8CPseSvfymVtDPBPkhOoWjPQGR6lBLCc9NgXaKC2y_wjU77nJUL1jZhN2xoEL_cayiqzljjzIe5WvjRg2hruZZebCEoKWt_GCX0EfRGEUQiE3udH9DU72mUMb0LBiIjbIi1mMiBvV9L4BH2L90iI15y_Zkn3axzxtqn00HJjLyk__5rar1Wg3jjjSFM8cVhibl7Vn8XXQFHBYrcjtixDlbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
طبق‌نتایج‌یک‌نظرسنجی‌درکشور پرتغال، اکثر مردان حذف‌شدن رونالدو ازجام‌جهانی را سخت‌تر از جدایی‌خودشان‌ازپارتنر و کاپلشون توصیف کرده‌اند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25703" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25702">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMjfaNg25UuctPYtqRB_ndQvLIavRK9p_FdHJbOub5GfMFAYb66fNJL_b9hTxPu1g90zSNh8ovEP4YbKBASVTnoyCsBAD4vk94fcGOgTol4yEKbeO8qx-8rzkxAQDFgXaEWxHp-Taw2VizT_q8WLd5_9w6LphPGWZrLcUs7IZzOOAS3sH_8ojj5_HvGasLxBKdn48BhpXPAzF1KUcRkvgJZEn7SEukYs0tw_GOPY1gxIHj_Y59a9KuxfG6Mm0KkRfKcssM9inc-e1lDC9WbCI8U1FAu5iXvrCP_AvkzLjpNFQ74uWQOE2CqkQUQplvyJiYDeCmO9TKEvUyoiEo_Cwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
۵۰۰ دلار جایزه نقدی + ۱ گیگ اینترنت رایگان!
🎁
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
🔥
نیمه‌نهایی جام جهانی ۲۰۲۶
فقط کافیه نتیجه بازی رو
قبل از شروع مسابقه
درست پیش‌بینی کنی.
🏆
۵۰۰ دلار بین تمام پیش‌بینی‌های صحیح بصورت FreeBet تقسیم میشه.
🎁
علاوه بر اون، همه برنده‌ها
۱ گیگ اینترنت یک‌ماهه رایگان
دریافت می‌کنن.
⏳
فرصت ثبت پیش‌بینی محدوده؛ بعد از شروع بازی دیگه امکان شرکت وجود نداره.
👇
همین حالا وارد شو:
https://t.me/betegram_bot?start=p7_r4EF37DCE</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/25702" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25701">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlB8lWX4Y5EsHTT4exeNOOo8fr4BORFZXX3NYFlBq6-34xvkajdryIOOvg75EZ5ZT3wjVxPhV6gYhiCSlFvZDr4ys4L44E8kEv2edrxZj92MWzszUR36UiwLAFHPhIkzW6zVOjY_NI_kWMxYCjnVafRhddpX6BSQbpvCx8r55R-9GqiW3rkzWg-pxrJoy5O4nClPhnvDO8UZvWFWjwmJO5MunbrOO8dWqAHz6zHgMoyBq6RfDbprXQIllnI8YUdch8lswFZEvFHdHNtc74-h0MoojXGJez1FGBWE026tuFLKNO1vepyPiXb1iAQJZAKqT-oJgl3OA9S57HZCAwgu2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25701" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25700">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKQZXayWGWTBP9u7n-JekPN-lVm3pIvvU__8xSMhFOXXZqzEndC87aNaStSRL0k40DkzDqJJPCsRyizksk60Fs8S9MtThOTYeXYKjF--tD9YgFZfCink9hYZtA6A6MqVw8WpowwWLdO8B0VIAcQDPNvSNI-osWis3GWwOLg3sJ8BFAycuSuDgpIHL8kXNMSoyOXC2YrZsHD-E3vfe21vOzzbKyWPhZPWMp_ODkSwhz25M5vX7xm1Ocrp2upryQ9sNlzsre1nWpySTezLWSMjdcExBp7xpZkpLOgGANF7lvxP0loIW3CZRn2VXbEFHJUnXCx21apMLKAga_pfVS4Y6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
طبق شنیده‌های رسانه پرشیانا؛ هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25700" target="_blank">📅 21:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25699">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N96e4V6kvlNdXZejMJ0IFbWKDc-q7f1TZWsbnbc2rxu8Y8HM-quB3nU25EFEA0ehgPMZBx7ga7Upk6S3iK3aRNVM8z045STHw-Gojv9WCjJ7GXV0MLmAsiwUeX8KfQF5sHtgFaSqTEilZOkVB_kv8zXTgQUFwZYRZYyRd3TrFJWp5Ha5MbXdzFhjSjd74N55r7MgjQ0gcMRt3pL6HcNuWpt2ZU2L7y7x1yl0H2aSJ76OF6msrPCNbCvQ-YrcnQgnx8bMEKlryxV_leJiw6E9LltoOmLUaqbmg0XaZ0uOHPjGhzpWvb--w-4bttk6kmkNSPmYmaTmEXtLp5OB8zX6Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25699" target="_blank">📅 21:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25698">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=nw3ziMs1YSHkq6bFKeQ1-PlLXk03nwxvBt5OuUu1yxPEYMEy7tRbEJNPb0UMgmNUGNgBFnhuiWd4fVu7aLuTrJup99YuME7oyIUiT464_mHXzuujH6TGVN690iy0W_5v8IuFsk3w00K4BlO3JHbq5ra2SK4XFZKGMwxVC7LVc1o1Pq7zAiIJZ5-_4B7q75yJRw1MiKXvlfk8aTqlwj0oSrz0jMw7K8Aa7nS23dlUhAWNmRyWmo-v_zNRJSY8bGA8Tg1gy-ou-2WvcvGe5atZOzPpz8iB0bnyHJZfpsIzT5PgaCXqR9CqtNDYTUL31h-b-jlcRO__fzWxaXhfjbe87A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=nw3ziMs1YSHkq6bFKeQ1-PlLXk03nwxvBt5OuUu1yxPEYMEy7tRbEJNPb0UMgmNUGNgBFnhuiWd4fVu7aLuTrJup99YuME7oyIUiT464_mHXzuujH6TGVN690iy0W_5v8IuFsk3w00K4BlO3JHbq5ra2SK4XFZKGMwxVC7LVc1o1Pq7zAiIJZ5-_4B7q75yJRw1MiKXvlfk8aTqlwj0oSrz0jMw7K8Aa7nS23dlUhAWNmRyWmo-v_zNRJSY8bGA8Tg1gy-ou-2WvcvGe5atZOzPpz8iB0bnyHJZfpsIzT5PgaCXqR9CqtNDYTUL31h-b-jlcRO__fzWxaXhfjbe87A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛ یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25698" target="_blank">📅 21:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25697">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-1rmeTkdHaDgGjwyhdz6A0_T5vUQF6WQ2q4upaOPQbylBWGSRWKu0TgLnkItgwraNWq7Exed3ehlJyNv6mjR60SsA9sZ8GEAXGGx2T7Qk7qQJScNiSR7WNSE8ExsFrRjqWsRNjkABG5SfnqNukSBECeTfjyW_nknMASZhsMAOxpr9UhvkBjr83rA4q89mYBaIX57bifrZ7JPZGeTsUH9BWk10UVS1EgLxhe-8ORuOpyiY-xaFb3d7rGUmy3NyOr-N3y_pyfhM8KblgBju3kO6czF2m_YIGsSTZ7mx3bEEM-1o6sW6Ly82P5V47fBlsEtI5JHqjN6BPZ5qBtNRWP_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛پوریا لطیفی‌فر ستاره‌جوان گل گهر امروز از سیدمهدی‌رحمتی‌بابت موافقتش باجدایی از این‌تیم‌ و پیوستن به پرسپولیس تشکر کرده‌. همانطور که‌درروزهای اخیر نیزخبردادیم تمام توافقات بین سه طرف انجام شده و به احتمال زیاد این انتقال بزودی انجام خواهد شد و لطیفی‌فر…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25697" target="_blank">📅 20:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25695">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nURTF8jfyx79c-eSNoflPqDCGab6ZpyRI2xVNEhkNEaEIGbbrO-seAiaDytHiMMk96W4taXiVGy2t3l2YWXyiiT8sjDuNzawakeF3J7JfAgGKtn22wliK5XNiuqe7P3XvdVgC8CgUrHIa98b_oClm345D2T5zi3orwZdDvFuTcJ3LEE4JMKyZEWGC_2qsk2xu5lMpGKLpCvndlbeKz8vTCh_psfXp3pRQ9OBkoA6Y4yqKQyVCLeAIMyt7U4LMdM_Th0XeqBcUob4hPa2IcDtiPhj6t_Qyo1szd-UOFuqBpC5U4u4psZy8v5FgEnLMYTtKA_jg49ujriZXWOr5h7x-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iCHG-RHg42rQlzmkOXw5gFgKw4MmY6b38621WiFzA61O2A5tyjs28opNXNwsoudN1zQyCbwyZcBBdTaWKedBc5dJ2eVQh2AAgtBtzeBZq13N_fCWqqtO1BZe-WGMNtmreSy198o-BzjqikE0jwtCZZMk9suJ9VbWxTjK8NYSSLNBYXnFREgRIL5YLds3nzAvKecO_MlE38kLONJ8Vg0tDGlQl5pRqs1dGBspi61LuvQ69F9LEGT91g5eV97j6AYshrSbBbYUoqUWtunig0BwOb108m6_2yqX-n7Okjm-Zqz_7Uk-u5mIdVzRkMB1S048OgOBj4cg8OgsXbKSnU08KQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛
شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25695" target="_blank">📅 20:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25694">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrNnAUObaNlujDpx6ZqHJBvnFW3Wsk8KTt_tCAjrYD2SW6EphO5-qk1hrnz_RVAPgWwNy3qICRgoGp6a3lSDIaKdNzPb1emb9ptYFNzlz7td3V-JupSIr8dkjedfQMHAGrhMpMX7iTiLi_i6NVpxWlPaiu3PEef58kBErZnlo280OCNATfeAlL05JysywkjcWiliCxclk_gcnizg5mUpjbJCCrGrX7ItcJcPJvkXLuuy7Hd4C2UuonpLKJnUJ1GTTanX5Drf0Nff-tZU1Bw2TWo28MM85mTs1XKYxRbqCanI6qgCD6DI-mA6FBiQsjlOYtYoDj3pM4fu1S3ixU_JrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
کمیته‌داوران‌فیفا پس فردا عملکرد نامزدهای قضاوت فینال‌جام‌جهانی رو برسی میکنه و به گزینه نهایی دست‌پیدامیکنند. علی آقای فغانی در این جام جهانی سه‌بازی‌قضاوت کرد که به بهترین شکل ممکن هرسه بازی رو در آورد. یه کوچولو شانس باهاش یار باشه قطعا فینالم بهش میرسه.…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25694" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25693">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuvO6iInJuG4s3jqT4d8AqMQX7e0dEo8_MLdpHhJ9RyrDqKas9_L9Yt0StgPOMEc9Lg4T7-BqyYdgOHjETSF7616ND_qVnNslMdJ4deRUTGgKY5cKoENBpOfRm4glYIe0b1tNYn63UewDmgSMjwgCgkrHdCztDB5DDgP6vRCJXQGIHFOGL34hYaxavKUNi9-6VeGrHCQL-fsd8ORDvx8WI23D4qyIESlfHB0mbP3VgeDFN40NImug9fCJuAd3ZieQDWzVIxV1AclJzLrqFZ57g5Z_jrGO5wQlalLI0fazfyUH1nbCDuUFe6x-ku8x-cuu1UKHO9v5e8HiG0v_3in3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25693" target="_blank">📅 20:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25692">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQuTwuP9LrFpz4sNCGjmcG_xx1Hz1birNXtzFKkwilkCrmIGtiBRU2WoJGGkdn2sPmhmlv3KUrXwGSP3WfHR4vJy4zYChHfFKx9nAprPjjFqTuylQz1tPSpfec2S36Zu7gnaKhv-B3pfbmm9TUwxGi7RNeb4LGhF21HIWGrdT1FHbsDSh0W3vQLKI6uJcIN0CC2SkAYa-argIwOkU5JljMypJOQ-EZfjcZZGJdlQkpRvClaAnknI70m-x9dd1Fq6GbTDx7y9_6fqgNX9GlypMa7f_Hlyum9bYF1BwPvirBwaA1a0hoteGoxzo44MbWeJQqXgwOuynTJvaYwQpKL4ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
یاسر آسانی ستاره استقلال ساعتی قبل با ارسال نامه ای به مدیریت آبی‌ها خبر از فسخ قرار دادش با این‌تیم بدلیل عدم پرداخت مطالباتش داد.
❌
مدیربرنامه‌آسانی: باشگاه هیچ‌علاقه‌ای به ادامه همکاری دو طرفه نداشت و از قصد مطالبات آسانی رو پرداخت نکرده تا او قراردادس…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25692" target="_blank">📅 20:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25691">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtTfE_kibDc0ocGJveANZP0L38LSS8N7pBt1sJateWUlw0jVboz0MlH0CVZy0W6ot0A4YYCXp9uqpmyXUrK50HhRLK8DuckfxudM42PH09YDP2IB0zAZcsyziHnQ2o_zPcQPVlWZPT5GTGAfyFTurMxFvzI3O6CRJjJ0r0SDR9Uw9eHNc3VUYuAdeSHWvQAymt_KY1ayqwPcyc4mIJU6kndRFl9xLtlKNFfBEkXB4HVVUzK4VHWq89ftuxBXWLJTWkt3snWtlRhLxk-G8I0ku4yhBiFRGyxTiBnulCaUHgYWDF_MrKIv94EWPRq02TqhYoCBw7fNA2PdJzEns_oDJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئیس‌هیات‌مدیره‌باشگاه استقلال: یاسر آسانی و منیر الحدادی با باشگاه استقلال قرارداد دارند و به ما قول دادند هفته اینده به ایران برگردند. امیدواریم به قراردادشون پایبند باشند و آن‌ها رو داشته باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25691" target="_blank">📅 20:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25690">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25690" target="_blank">📅 19:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25689">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZNoe3cpSPo4DI9yNvC5lDSm4KFSGNPn4G8x_XhGBQzzG7RWxhOYwcSkB9uPiyHjDLttdhzgeJ_e7sH_pXeFY9qBzA0MEQARR1ojVN6qTnfmo7kx1RC2pj40ApK99S9e50fM3xeisj49kzFhJwXzjQyADqQRqJkrGxDMVQj5sKNRdhVJ8_PidxSpJiy2DG1WzR0dReLdU_kaZWqd4RU0KwCxjxcxTsVgiPWfC-f-7VaeVpXyypEcz_w7ymoyER1ygWIr468IbW15TLsECosr4CrM_-7glHKNE9NudD0Kvl746w1VrnLZTxj-tlKvOnfMbI7L5hSGCduP8JmETTKIgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25689" target="_blank">📅 19:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25687">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZ_dQo-OE13vb_MHq65z7RchvJum8LVM_n_IjQCujmURzUiTQLXTnmNpwYORDOPUtkcJDhIzcLHlN4cYPS1oCDAOSh0rrH_m0BTvFWOKsJjQHwImGG_zui8NBYcHL8CSdRCgQmWGIxOnf_qhK8xUOlgVBui2z3OswdDYBep6VDSB0N4CmoxW66B_c1nt7mNyNqE47NBkPIUD4LZW7pdUN3H4NxNwXES4XgjqSgBf3hQtM_CpOAMUEKbEK3Y2--W2Ff2FHwVdHZha9cUtdUMfFB-jENtnuDCrhtJGDmL7Xf3bF6_WEQTfNYeOF4JArn6cpB6xwEF5Atsuo_kXbzY3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AdhZ-2p7sLmJikUJY-Ps06qDZRbNKXC7dPrx-OKtQ5dweaRd8xNt2E5JOd7PXRG94QtG2uTjN4wELepSaXV4qxwjnvt0v5bG-lt_UM1TyHwC_EypSn0e6efjyaKZegCFW88HIvn-vzGfeVTGx0SdGXARMlsk0ptRm_jdU4_UqJ85D3MtEOQDeGCpafw_ET6jtzBe7PyY89Gm0PPHr0E2-9zeAKsv9jtktn5vug66J_903ICCwXesRHpByYK06Lk2-hbgTrQlXuyUnEIUOBapFLkbvC3n8DxHKWESlUVukpf06nVh-vyq0BvFbRwZ7nkTHO8HTThawZAj08c0HcdhVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25687" target="_blank">📅 19:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25686">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcqFbYHB6kx9511HX-cc4ypDrlMJjRcSNaonmF2iD_btTQK_k1oCVzcVDO39k7SHW1umLPuqh7bcpxcjkFM3cLaFHETXYo1UWRvN6qpvlMW9Z06AUfdACvcQ8Ef-9CDlIMYr7Yfae06EH7HDFu3bPuWrTQR5R16XtuBqV6AISjebXoyxcpZpvQX0sFOYPUo0ooXiwQupqAAG-g_v-wToRVTKu7l6hXKbuldYA-cS9FqwQRP4bzQE1REVy5Puvlz0KrOy_qa6AIrD272oSXKcnRtiPCKQIp_-MFRBHwKzqVc3GB3i4RT8DdxiooGDX2X9IVaLqFAf6BvPo0X0qz6wbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25686" target="_blank">📅 19:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25685">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHAo_cu-6FSPts6D4Sy5882aE_rwGSE2cnCs-HeICaznmcviTvBb3ngD0-hMdT4Y9UYCgE81AS247F7p4unTG9EQ9K4XG51FgUzHn_lMFDR8trRAe0Z4qtoiQxvpHxGA1JWl1hcbO4WCSYBpCyxFO9YVFIm6u3wl2qh4EGsQzA5unr-usNcgMC0frNK3xZJKz5RmKWsOr2focS4pQARxq68y3KqNJS1iPM8zKuZQx0qjFt68MIy4f0E_SwC3rNFFQVGZ4BhX3sQOVgfgqaZcrl-i2GnoLnfoMD9ui1xnCzTuEFGKIhfXqZ4j58xIrjbDAm66Q2KGxgo-VLPq_QJPqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا؛باشگاه‌استقلال علاوه‌ بر پین؛ با یک‌مربی اسپانیایی که بالاترین مدرک مربیگری اروپا رو داره در حال انجام مذاکرات نهایی است و به احتمال بسیار زیاد با او قرارداد امضا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/25685" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25683">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XTNmnFVoBtJp5VThSekvtWvywhaINdD3cZBPVb8DMhRHh_hWTyZEglrl0_6IOWzmJxsnQqcFNKlSCU4caPRqk3UyULcFMRK900DStFrPW3A-FnfZMsJRiwJvMHqmSp9PXjSPr-pOb_JSF0dfDLF6VcpCjuxZIriYLeWrWAG2c2OuAz85jzT-Gtp3jo_iPa_1NwPrU_ggKqelVkrczVB9LRbKJ7oVhMZFkA18Iw9MJ3H6gV4DwZm_VjF2ACtbDpEle8-Cmil2Fwozg9KGBDL-DAdlBbAr8JXpDbAt9leuOahXZPrI3cuFpI4Fxf07UWDxHxdjEoHTlxWiiWuz9a2yjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VC98FwuGmywFXsyNbvHUiyuxI_tIdoysttX9r3mlQY0_yg0E3m3XLqEk1DqIPn9927OgjWOdEhjpQJK6H7XuMqKHkrMYqELEB_-WZ_mGCIdieegME_r2YJoB9eR05ViwTFwFEh1Bh7UqsR9qIw8xZlGVpoEncp2u_lU956s8gHRdfkUAW0JlH3DCUkG30Gnk5ZAjh5V6YUvBYRpzhtFyCmH9GI__WC-1uQBctdGl4g7Hl1DV94wNTrW06z6fkeEXc2euwlU29tL00jhJIRpTN20gxE6A_xbXpjIP-r-QNLcj3oY5oCmty8CMXVKHabhJzvUVEjXjzW1HFLFjVOOLFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/25683" target="_blank">📅 18:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25682">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🏆
40 سال پیش، بازی انگلیس و آرژانتین یک چهارم نهایی جام جهانی 1986 گل دست خدا و گل قرن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25682" target="_blank">📅 18:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25681">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7oda46_9ITDy3iWPqTiT8J1BTei3qZS05Uc0wjew0DetIubZxa-BiArx_qerpvWI4bHoYA_Q25OrxVhn5Uf1FvonkzV61V13-K-ILgv5Y1QsTrCTAhVPWOjSZJI9JnQga_m9SHIldzPh651fcnYgfiVRbszV1CRqHtxvVLsYM5vcsEQuMhJC3uy-aSq_v15CqFZ-1U8DSVPxGhB0admXr4mO7WZMTSVHehh7C2l2gqTe4GxzlgPETYpPokRzbgm8W6jgXsWH43OBUCoCOtKZ-qwku8pmz_NNdZFTHJr2EWP_l-LxDAyDH7iivE63rwj_bxCixFGsK2y6CgnpTNCbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در انتظار دو دیدار در نیمه نهایی جام جهانی
🕐
فرانسه
🆚
اسپانیا؛سه‌شنبه 23 تیرماه؛ 22:30
🕐
انگلیس
🆚
آرژانتین؛ چهارشنبه 24 تیر؛ 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25681" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25680">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyRmtsJBzTFIMzULOnT_Yri9yP-HOhccMaeOv0x3i1YwIdAhXosCkm6xs-BShFcW_yuMSBn17NPO1R2d6ixFruDxPGMsHO4MvidBFavud6_CwNZHswPN-zqp0nqdeVKm1zzF3Z2YilSFueYTmIlP90dd6R0XObW4x21yGP-oIhjmLuaSpo87x6piFy5dmf5HafgFYNuBZSJOx2NvCn3jCVTo7-LJXM7D0WCRobs0FW_ilVZJ06wXOy2zdgAVRasSrAKweUH8Dmk3b7HKVKDFq_5dtZT_5IEOMSdCE30FzEqx40psd1_aOMgIrNYZWKwVJTCi-JqT__CQRwtR1ehTCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مسعود محبی مدافع جوان این تیم رو 350 هزار دلار اعلام کرده است. یه چیزی حدود 65 میلیارد تومان. دو باشگاه استقلال و پرسپولیس به دنبال جذب این بازیکن جوان هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/25680" target="_blank">📅 18:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25679">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3xf4NSbw6NYu8X95eT5y4jCwjOp0cX4HEZwHthBqjBHhL_0geNq9HQWL9uQAsmp4du-dNBQjH9H8vLLobu45xVUrCfV2fX92aY0eWWuVCYQpqgqK3Kt6IKGGSMiNlaHXJIA-0N17TtwpzKlIzfdh3Ts-ZFXZZwEO2LVfAdBUYKAviydfXSbwhYQ0jkSAtIBMtgNnNJt5jIoYzPiVf6ImF0s8e1EMBV_zltoujaxyFNYNidnmUoRcoVjyuCtsFT-JU4a1VIT1pXWpjMn_IceRqMwYgNPoGgR-juLDo-24VBJGY9H08rh_dVrV7dv2zRDiISP8K20UpB9KIaQz0u7cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری #تکمیلی؛ آغاز مذاکرات سرخپوشان با ستاره سابق برایتون!
🔴
بعداز صحبت‌های شب‌گذشته علیرضا جهانبخش در فوتبال برتر؛ صبح امروز پیمان حدادی مدیرعامل باشگاه پرسپولیس با کاپیتان 33 ساله تیم ملی ایران و مدیربرنامه‌هاش تماس‌گرفته و پیشنهاد مالی…</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/persiana_Soccer/25679" target="_blank">📅 17:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25678">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S92iljw3OPX3qHtd1736zS64OfxIePfaGjivMMEsrvLzEF-K5BTn_P9JrLQJMo61yzwj72v_eH6FU58gxg0kQBgJok4Y8szQnS_nffnudk0ePu_rPmOdbwhU84MmA7wQnnyhUO17bqq3baZ-CmtSKJuDi4vXUJ8u8KZgGEyqukfKPbZhPm7jQPKb9ZEJsxOEPyWXG6ZWb8mE7PYOWoiAi7iJpNjAgzzfUAZSr_lmn6CfxIMSvr1QZRERxkaaTtYV6kisMDi94BD3F735lVhG-xjbSovEGPPz_pP1GFhtplbdPOgtWarEZVxtMrG1xURizfwm5TtmPRjJy4-GVB00vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
علیرضاجهانبخش کاپیتان 32 ساله تیم ملی: تا یکی دو هفته آینده از باشگاه جدیدم رونمایی میکنیم‌. اگه‌ایران‌بیام بین استقلال و پرسپولیس یکی روانتخاب میکنم که از همین حالا انتخابم رو از بین این‌دو تیم کردم اما همچنان دوس دارم اروپا باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/persiana_Soccer/25678" target="_blank">📅 17:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25677">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBJ01GobAtDMESkyffvGWorofdzWTTpu1p-6dwd3WBly3eiB4fMM07pQCE1uDYKAaS5PmHgPPVdIFvFvwoKZd1fmloa-g6XKYmkWQA6UQ0eYAZoM0bJd-pqBhs_SMtQ0BxFK-rvSaeHEONvsyyLzJwbY7N8q4PflUberwP2j2M4VY-BOkolV4FiXwz7yw1hpDKitbQclIRrl9fZsAFWYMnGzA-5iCRQecQAgw0ceJSH0lJasBZCkspETYQlYBsyNMyX3EFXUgc85CEM_dI7udKFHOlyhNM3SB0qGOXnIJILPUZ2lXjlDevt22S0_BwAtid46Cba4AEmZnRDglAY8eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسی، نیمار، رونالدو و هالند اگه دختر بودن:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/persiana_Soccer/25677" target="_blank">📅 17:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25676">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiNEyb4O2T9qrh6et4BZNMzpvL8w6aDubIbA61_AKbB8ZDHx7QDm_AJT4WYJ1nitTb8rRYYPZ0ux2qpYF_vk4a0NrISZXpGDXlMGw0Oz5qOvII3xXx_DQsz4G4xzux-jn-VJBRHYE7dgGaqVHsCVqemS2NT4Gb0U1L9bngXyDBzqOmTKSqRSzDwnIozdOGDjKkjwo5YBBKwfVEoMRxGU8bljdResmS65vgD7xr-nHfWemL4BUVRfi8XyJUocGJprJehgLsf9lPiBvsT0um4Nn_kuVvRPLONDpnUL8dxqWjOtR5YanNkSx2C9QEbEZPahn_pgWzIuwJQGRj_6itwCeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... علی کریمی هافبک سابق استقلال با عقد قراردادی 1.5+1 ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/25676" target="_blank">📅 17:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25675">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfo-J-WjHBfRgWVijGYmiiYvucP7OD-N374FilcxEZ38zXUCdWQxyssD8eveTG281yXzx8mfYhJltBKVztFvDktK-Ewn-Cdqjk7Ce1HLEy_aesgBvrYaQqpoRKs5T4xATpFU6hL8uwX8_fNL_4e6FZ_AhEEWCm8jgYcWR6pRNQds4HRjbddHm1uIQLnVLQlbg0otET1YRKB-vMID2shSoqweMv8nQNCbxPoeT_QVoKOXFX3KgXdrNtq1zrsOqkx8dTI9Pmqlm7Rxw5SOWO372W7-YN81O_tu9J6cliortnLm5KfbA05TmAjLDJrnWojPYlmNZ0F6AuMZJeH8Nwbz0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25675" target="_blank">📅 17:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25674">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1FyGWRelRRWJd34wgw4lstaTCOBujPEyMezuem5a7ip0LPcKWE4EtBhTjuhM5_QU2w6-K50QLbn0DlsLWhXwqRN3SV8O_lFHyQZr9ye5BaqJjMGRqroaNLAce88tPHLnBSzLup6e5ximH8Q6n-p6_MVktq4U15QrB-sZ_gnmUm2dBKhxnAI90PTUtb5Ky7AO1nqsMRot72Jrs_eAvZNiCQ-Nv2zOE0Cmuta6censpTaMQiLuo_M-Wyrvvo7ugGJ6b2V5hjNgqdKchlSmOTdF_E2X1C59BpN9UBsHGfUuVu2dkUNhfrNsaZeD3pYTtjK7zGQ6jqD9VLL3cXJI7ysBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آندرس اینیستا اسطوره فوتبال اسپانیا و باشگاه بارسلونا مهمان امشب برنامه عادل فردوسی‌پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25674" target="_blank">📅 17:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25673">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=aShWDTAn-ZAbrz311bw3Gqs_Lztc9zg7aDCfn6G6gY2ly2-3TN1OKx0TP_bEysAkELF6WKANkxpWAsczQD4AxiqBF2unSHtoECGOnPxJDWHMqbFCEBcZLTfFUlIkcgTAT5zefSZlqpMOfpGaDFh8BFHiQfDwa6VyW9D4N9Iu-wFJC4UKcFeLgK7nXL-IXxCWHeOrbb2d8zQsuo2HZpodSE8bQcbKR47quqSeBIRSh74w4y5nuiW-M-fLuJDQpzh83U3PeYlPKNEJIdS7E5Uetk8o9YcQyfBsV0bNFn1ukR6Kuz6nPDW-FTTSFFSlZbiLglnVZLwD4KC3RuGqbP_xgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=aShWDTAn-ZAbrz311bw3Gqs_Lztc9zg7aDCfn6G6gY2ly2-3TN1OKx0TP_bEysAkELF6WKANkxpWAsczQD4AxiqBF2unSHtoECGOnPxJDWHMqbFCEBcZLTfFUlIkcgTAT5zefSZlqpMOfpGaDFh8BFHiQfDwa6VyW9D4N9Iu-wFJC4UKcFeLgK7nXL-IXxCWHeOrbb2d8zQsuo2HZpodSE8bQcbKR47quqSeBIRSh74w4y5nuiW-M-fLuJDQpzh83U3PeYlPKNEJIdS7E5Uetk8o9YcQyfBsV0bNFn1ukR6Kuz6nPDW-FTTSFFSlZbiLglnVZLwD4KC3RuGqbP_xgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25673" target="_blank">📅 14:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25672">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vISz2LJDkPaJsI646zZxxwcaePfzfBWqI2Jk2stjWkoWFBSImmtiL9fxKgwTOSaCsrI9xQQQh553RZxiXG_dWWf4Mc3U2Q2iGp6pgCXXwz6fFt6mbLBU5sUvM4AH0QC63YlKhNFN9Qn8UfbQKMHygGBw0KQNn67_h6T0qJAXgJDCfi6eBFlNNOGu7CUCGO0HIt4lL5bZb7eTy_-eM-ZK-bhu48CVks37GXD-5nagsQeWUTl-rS-EHYd7jbBoXOvnq7bshqZCvXxZAWnzRugDJdHyexeIUR2LfyE4-C3OypYg3yn5sB5rkORPDAkuj05YNo9IRdFU8b-0xk8E1CeR8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛فرناندو پولو خبرنگارمعتبر اسپانیایی: بارسایی‌ها یه‌فرصت 72ساعته به اتلتیکو برای خرید خولیان آلوارز به ارزش 100 میلیون یورو داده است و سران اتلتیکو رو تحت فشار قرارداده تا زودتر این انتقال انجام شود. آلوارز به اتلتیکو اعلام کرده تحت هیچ شرایطی فصل آینده…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25672" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25671">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=WnthRxp8pLPc5Wsl544WsVS47le1Po_gXFr01kidz4SwunnAyv54M68aiE5UHnjMj66MDzBh0Z6CVAsSP_dQYFEqybzuhyb78PBln6-BUlveIVqjtPrH3gFYzWk5anADij0aGH5ypQlTFJmr81yZO0_3f9O6bQrNQOCWvdhaZRrNRh5-2rTvj7SW4IBIyvSBCYVSDSDCHnXTC5K9pIAZ9XmwdAEfT5Z19wvuhOHRAniktcwVoqIGlIQ6BCMAeJ55YOztarCMsVyyAE-1huBn99F_6j2ZFl7BrKjpSro--e_VhlN33RubTjhR7g5nIzvIxnAbr1lOUdNvYBZCZOOGxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=WnthRxp8pLPc5Wsl544WsVS47le1Po_gXFr01kidz4SwunnAyv54M68aiE5UHnjMj66MDzBh0Z6CVAsSP_dQYFEqybzuhyb78PBln6-BUlveIVqjtPrH3gFYzWk5anADij0aGH5ypQlTFJmr81yZO0_3f9O6bQrNQOCWvdhaZRrNRh5-2rTvj7SW4IBIyvSBCYVSDSDCHnXTC5K9pIAZ9XmwdAEfT5Z19wvuhOHRAniktcwVoqIGlIQ6BCMAeJ55YOztarCMsVyyAE-1huBn99F_6j2ZFl7BrKjpSro--e_VhlN33RubTjhR7g5nIzvIxnAbr1lOUdNvYBZCZOOGxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
کریم باقری اسطوره‌باشگاه پرسپولیس:
تو عیدها و مناسبت‌ها هرکسی بهم پیام بده جوابش رو میدم. اصلا برام‌فرقی نمیکنه طرف روبشناسم یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25671" target="_blank">📅 14:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25670">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=Cfmo7enOO6TYUQ2Ku0RSjzgoNJSQw-30ign-EKt1IVHpAmrFLS3I244GowUdHsMgIduXJBN9BchF2dEJ8-3y3h6_jPrLuymvSXYazpu_Q9eRh3KGsYcsEiRgZhkV_yXUhnqMo5qXOr6M_iMx842w-LjT9HV9FZHunshhJikb3AMqfX8TLrXAOTVrQkpKGVvi8ZOi9pEZlTUuEzUSPa89Du9ja_ocdnrgr8vGzzLA8WmvqUn36EDeXsRq1GrSS075SLuEfzwzl7-7MYTOqKUM-Zg_01LV4Mk5xb3Av6nOOT8_PAZyLgWUBvY4Sk1FpZjlGsmu-akgayqf9NDmoTItt5x4Ujw5i40ColVHu0zIvU2v-EGaq27fVVJJ3kiRPZJ5dcvZGZ8IGCzQGxhdskzbl-i_bOvXdPVsjVatrktUnpNhGC8vgP-NRkr4kZT6xxVWn1dXfRpsc27VWd96Dt60r2hVjecCFI40Divm5c5DS-xUh4UZtYHNCEsFLdm4pyO8j9I_-wbvVivNLl9VfuXoMeRZIeL9L3T-TQUkfj17QHQfHDEox1AgYG_HBBUpO0IEf9cEV14D1owcAj-FCCb7kvOLevo3iNl-csReinfvms-a6dm4lFwOVL5NIx6QCpmjfj98FcJ2eZ223Lchz2Kdcte9brPxuhFA1e4nSkteLn0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=Cfmo7enOO6TYUQ2Ku0RSjzgoNJSQw-30ign-EKt1IVHpAmrFLS3I244GowUdHsMgIduXJBN9BchF2dEJ8-3y3h6_jPrLuymvSXYazpu_Q9eRh3KGsYcsEiRgZhkV_yXUhnqMo5qXOr6M_iMx842w-LjT9HV9FZHunshhJikb3AMqfX8TLrXAOTVrQkpKGVvi8ZOi9pEZlTUuEzUSPa89Du9ja_ocdnrgr8vGzzLA8WmvqUn36EDeXsRq1GrSS075SLuEfzwzl7-7MYTOqKUM-Zg_01LV4Mk5xb3Av6nOOT8_PAZyLgWUBvY4Sk1FpZjlGsmu-akgayqf9NDmoTItt5x4Ujw5i40ColVHu0zIvU2v-EGaq27fVVJJ3kiRPZJ5dcvZGZ8IGCzQGxhdskzbl-i_bOvXdPVsjVatrktUnpNhGC8vgP-NRkr4kZT6xxVWn1dXfRpsc27VWd96Dt60r2hVjecCFI40Divm5c5DS-xUh4UZtYHNCEsFLdm4pyO8j9I_-wbvVivNLl9VfuXoMeRZIeL9L3T-TQUkfj17QHQfHDEox1AgYG_HBBUpO0IEf9cEV14D1owcAj-FCCb7kvOLevo3iNl-csReinfvms-a6dm4lFwOVL5NIx6QCpmjfj98FcJ2eZ223Lchz2Kdcte9brPxuhFA1e4nSkteLn0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
رونمایی‌جالب‌از شباهت مربیگری پپ گواردیولا و فیروزخان‌کریمی دربرنامه‌جام‌جهانی شبکه جم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/25670" target="_blank">📅 14:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25669">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxRqdRZ2vthb088VJ-q_ykahH5PaO8179wVV7v4V3H3S6Bp9wzGp2bmog355tMXz_l3BSh2p_-WuyZpYp3jLrReZ2r0xz1iJqgfLooQMPfw2xb67gz08jUuiPHNJ7Ap56V03U4oOj7dnX0Y-uWQkZk0RXYXcZXFof-FMIh--ao21ot8G61VLAyICUoqLJmRq0te5OgGDc-FUaCCI1ECOkRFo3sKAP2nUqPEW--yEL2WIH7a5XSZOOSYtu7zXv0pNmWP1tF4CIZZb2USKA4pTTiHtNif4PpVprOo5lI3HS9JRQAMPi2Wpp5IhfUkCiToAPejCMuWuWAmWdiJOpkX_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
کرک و پرتون بریزه
؛ رئیس فدراسیون فوتبال سنگال گفته که: من‌اعتراف‌میکنم که بعد از حدود 10 سال متوجه‌شدیم‌پزشکی‌که همراه تیم ملی بود، اصلاً پزشک‌ورزشی نبود؛ بلکه متخصص زنان و زایمان بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25669" target="_blank">📅 13:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25668">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd10299011.mp4?token=QxhDiKL7TN1NkkcXguNPplsktgGQo1DexeRBPiSC6O5olFAvAmrWCIxjfrZeLkb-8XoE68Xg-9DbOMAF9Kgz9JUvIGM9-Q_ySGHccVfUQQgnhT9jlfLlPllfFWLcTYBaLrqYXxd5pstNguumzc1idIfmmIfTm0-kiWrflpbjXRy_0nbJZ8qadi1RPmjqy6zCy_xCQKrpRnzWK_-4kNUqAKOkrCccfo0UKqulHLQ9vnWP5HZknvOrE0YaZjHF2DbsXysNUfWz_jM5Wkz48AQOqXQj2OV74qWiBh-TNwWuxJw2tn8ETTamSMa3ppwJDpwTeWhh3PxSWWgpP3STRS1oWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd10299011.mp4?token=QxhDiKL7TN1NkkcXguNPplsktgGQo1DexeRBPiSC6O5olFAvAmrWCIxjfrZeLkb-8XoE68Xg-9DbOMAF9Kgz9JUvIGM9-Q_ySGHccVfUQQgnhT9jlfLlPllfFWLcTYBaLrqYXxd5pstNguumzc1idIfmmIfTm0-kiWrflpbjXRy_0nbJZ8qadi1RPmjqy6zCy_xCQKrpRnzWK_-4kNUqAKOkrCccfo0UKqulHLQ9vnWP5HZknvOrE0YaZjHF2DbsXysNUfWz_jM5Wkz48AQOqXQj2OV74qWiBh-TNwWuxJw2tn8ETTamSMa3ppwJDpwTeWhh3PxSWWgpP3STRS1oWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
متاسفانه مادر عمو پورنگ صبح امروز درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25668" target="_blank">📅 13:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25667">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3e0f878ea.mp4?token=dkpD6i3haAZHPkVBRnZluQCJzULOs3zh1iOU3ANBfwoH2de-jrN1TzGthN6pYQqO6OnSRJJnnm7qlvc2h1t_rNAue_dkxrBKZ4GsEK04RI2Tda6d2pAr6TY1WmkeCs6XvNswlLDWGt8tbbK8Yv3O5jkN6Cd3arfMp99S_q1S5a0Wnxivf1Bt_oVGhGxHDPIWDxorNrteLBISRNkAmGBuJlHd6sJeUxWOhUKcrznkr7jsdzZxYQ1PoG3iAb6xpm-t5Lxx5N0vuU4z44uxCejr4Vq1qUBDTl6Qw9yeEoKWqYPKsJYtLfEGKq1QkLpHwey0BX5MzjiOmJMbd6c8p7CEXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3e0f878ea.mp4?token=dkpD6i3haAZHPkVBRnZluQCJzULOs3zh1iOU3ANBfwoH2de-jrN1TzGthN6pYQqO6OnSRJJnnm7qlvc2h1t_rNAue_dkxrBKZ4GsEK04RI2Tda6d2pAr6TY1WmkeCs6XvNswlLDWGt8tbbK8Yv3O5jkN6Cd3arfMp99S_q1S5a0Wnxivf1Bt_oVGhGxHDPIWDxorNrteLBISRNkAmGBuJlHd6sJeUxWOhUKcrznkr7jsdzZxYQ1PoG3iAb6xpm-t5Lxx5N0vuU4z44uxCejr4Vq1qUBDTl6Qw9yeEoKWqYPKsJYtLfEGKq1QkLpHwey0BX5MzjiOmJMbd6c8p7CEXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔹
فدراسیون فوتبال و سازمان لیگ بزودی خبر به تعویق افتادن لیگ برتر تا اوایل مهر ماه رو منتشر خواهند کرد؛ با این‌ شرایط موندن بازیکنان و مربیان خارجی در ایران سخت و سخت تر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25667" target="_blank">📅 13:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25665">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFmG_ZCkC3EBcc7YO5qHophZ2sIErNb51yalhGfz1sZhc5Np0bx_NOG7GWQEa2HBk0VrD-1jg-hR0nk1obXE9GkuVB7e2btqu4rffXnAQtwNWqepIZSRBudo9m1KAXjwSVn4wW0auKgBdvykioiNSXKfPP5ECpFPYrsvjuCI6lGVWd1phuxAt2haNKVHING9Se3Tkq4YJLMnfGWtG-0jtaFDN0cFv58qcN_yGyoyMoGwQnSrOSv4Iw8iUK3DwAXYKT9rya6V8_62TGvNrAng6d4izsS5_ZrT2f027c3iXgeFiaCtgVIjvARwJr5_oMYjg8OjJRTgYSyGsBVp3fu3uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700f8025d4.mp4?token=B9Lmj8Bnz7kKZx2Op2DjVx3I411JBt9zHBruFgiYMKzVe6lzW7GTxR7BrI33ERWSBkjBG4j9qjhxxGcg_9oTHXyfiuqkgNLG4Hc5Qb4lbuNC-aDna6UCEQg6XW1Lt7s4Kkf7Hslci1U5O_8Gdds5dyfuk1NniIOdIxoxAv6jtuniC0ukQh2cS6FbjG1uUU5N-d-g9FBnRf-4-rqfZTZxkTWgEczttmQhaJ0GWQQlVzDGXiVJQeKHBC9N6n4QgPnLLOYb01Nuf-71fOCs4GbEVqPwXPoPTBhQl7tBxpgKFpmY9AZ9znPUK_qBzpn3vDFk7PdYlOE053-pSyVINJ-iGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700f8025d4.mp4?token=B9Lmj8Bnz7kKZx2Op2DjVx3I411JBt9zHBruFgiYMKzVe6lzW7GTxR7BrI33ERWSBkjBG4j9qjhxxGcg_9oTHXyfiuqkgNLG4Hc5Qb4lbuNC-aDna6UCEQg6XW1Lt7s4Kkf7Hslci1U5O_8Gdds5dyfuk1NniIOdIxoxAv6jtuniC0ukQh2cS6FbjG1uUU5N-d-g9FBnRf-4-rqfZTZxkTWgEczttmQhaJ0GWQQlVzDGXiVJQeKHBC9N6n4QgPnLLOYb01Nuf-71fOCs4GbEVqPwXPoPTBhQl7tBxpgKFpmY9AZ9znPUK_qBzpn3vDFk7PdYlOE053-pSyVINJ-iGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بیژن مرتضوی خواننده‌وآهنگسازایرانی با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت. عمو بیژن بابت این یازده دقیقه مبلغ ۱۷۰ هزار دلار نقد میگیره از فیفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25665" target="_blank">📅 12:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25664">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u99riyA2ckReTbeDwMdwxS0qiWG7g1OzBfS9xAo7VR-aESEnA9ItAhcGV5L4Loj4mo4cxZZ-FnkaFd4TSlumMOkrdaVyw-u_o7E8f4Nhx0_1THx1OPU6UspOHN-ZBNCYhBmSmvCpDLhxfvINSBmS5KzLrSeJHzKuK6ahReHji7ERfZuNu4HJZrEN2NmbJLTLtwI5b1l1rSI4LSbxrvo8QumRejY2LS3chZtMI56OySIS47q06bGvhWyU9i2J8ue8cwyoMi9cMgDprjBbAd-V1oW1fRxbNvP2nnQs_o0016PLNLQGykCebvLoJUM6EWYlEjKz112INFsRfxep-YbtQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه…</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/25664" target="_blank">📅 12:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25663">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07accb99f.mp4?token=UXCvqUYgjkBi6gzP1Beda1p00LOmU3svCRlXPfPTL2J38IRo1vx-1psfziYLDUJTjlpPsBuyt4Dlk3BnJ50S2wkVLiWO6Fk56EJQAm2XcS4Sa6VBpPhm4_f7a247_d2pQGSoel1m04n4b9PpabdajZhbpHnfzy9wOoKZNfmudcCPxXVGSfEyGpMXGiNUSnRkeDfyWX0rDoXFYM1zxiw7sy8MQeGYu8aGVlf6dnbQh3nVIlh_FkoRjO2vX-PvLL0O16oJHFnYcqVTl4AE6mfwe-QS88UGWdy3_aQuDJOLzO0MwXGOqCVZCHiW02wFGlhDeSNYSKLx4t3wdPtJt1C1mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07accb99f.mp4?token=UXCvqUYgjkBi6gzP1Beda1p00LOmU3svCRlXPfPTL2J38IRo1vx-1psfziYLDUJTjlpPsBuyt4Dlk3BnJ50S2wkVLiWO6Fk56EJQAm2XcS4Sa6VBpPhm4_f7a247_d2pQGSoel1m04n4b9PpabdajZhbpHnfzy9wOoKZNfmudcCPxXVGSfEyGpMXGiNUSnRkeDfyWX0rDoXFYM1zxiw7sy8MQeGYu8aGVlf6dnbQh3nVIlh_FkoRjO2vX-PvLL0O16oJHFnYcqVTl4AE6mfwe-QS88UGWdy3_aQuDJOLzO0MwXGOqCVZCHiW02wFGlhDeSNYSKLx4t3wdPtJt1C1mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
متاسفانه مادر عمو پورنگ صبح امروز درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25663" target="_blank">📅 12:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25662">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMpoZIo5aanvDOupf1Y5DUxVABooJPE6A7RpRoWSF9H5-smbeqGSawg4AQ4RrRCYJqJxod4Ly6paSlDEBs0PWmTofQyYcaT39zkbtGibT1zPkcwVv3G1gJ1kZdpatEwpvBeNFQqZRmYlgTvKJQRaNz37JMZpakR6Aezw_hQy5sqOL1b4wU3BhL4d22Ek1MG7YOyTmDcJvJ78qjiVRYL7M_ZhhrW-XnrD8TzhM9i7WbSVR_pmOwH8drNE3NXPjDORzdXNaZ3PIExHioomry5XyBZ-LWBWX6LU6jcq6Beq1UwOh6_no4sYRShGeRFYUpoqbWo3D1LibA8EW8Tl6NfMHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25662" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25661">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-T7_GKNKpt1gFJjBBCcTM55xX8iCmaQnkfgPM1pr8SxT-KYVsP6af2SZq0bPvAZ_aC8M1IpGICSxpYLIEJN0S2dZK6hS4e958wV5ZFMtVK6p3j31AygJ3ij_9tYRonpekgFN87VIOwDIejrFvoAjjy0ENLAobSo-xjuYVy89_mwRzaycKPCVSVImQsc9KXcJmJRb4ByTXBsU8vX_4WMuCrtNoY8LaYYu0VcTQGUziBE9hZ1oEUrqNrEO9V85PhtGjS5cKe6VKuq3aVKVXALTS0vzJcn3XNjjm3MZSnmlbZrIqhDJh7XIaClh6Wpwb_hdNz5y7y_udTUIqo4NnRmbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اولین تصویر از حضور یاغی جدید فوتبال ایران درتیم‌جدید؛ سیدابوالفضل جلالی بعد از پنج فصل با لباس آبی امروز با لباس قرمز پرسپولیس دیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25661" target="_blank">📅 12:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25659">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hO_gg_g5Gl9O0zRAC_WFwPMQuaoa23T5KMXOephITo0OIegHu6nwi65Bb_xOUnkOhRVHaPIrsAdKXb4z6OokTPgQoDMSoNjuaiP704oyYAsU63TgJZ01vwLyoeg26GAeBcsl4PaR2Gv5O7gmwgkRsASIAcJ_svxEnSA52DGm6xL17-bMamtlfXFJqvcdTJZa4RWJwpMCYbQ3jw2YBn55w_0hczob589dWqxBFhgV2K9UuD8T_SgZh5N2pUqeqzDMIG7-TM9Qjm3ZCNINasI-2UCyZ_bSknNzihOcwKF3-EFwAaR-StCzIAT1Yo6hjLuAgO114jtG7fY4aWM1XRI83Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری
؛ افشاگری‌برگ‌ریزون عادل فردوسی از امیرقلعه‌نویی:
ماجرا از این‌قراره که چند روز قبل از دیدار بانیوزیلند؛ امیر قلعه نویی به مهدی تاج زنگ میزنه و میگه‌من تو فشارمالی‌قرارگرفتم و همین الان 140 میلیاردتومان‌میخوام‌اگه‌جورکردی خب دمتگرم اگه نکردی من انصراف میدم و روی نیمکت تیم ملی دربازی هفته اول جام جهانی مقابل نیوزیلند نمشینم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25659" target="_blank">📅 11:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25658">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6C6ufuzxKrLFFo8xrvzcTAnVfX-YWedXbAY-FcjRxw_sUSN-Ga2xHKsYInp99vC3ar3l52U-BnPiivSZpGTW0PFqkZtvq9JHkUDJxDstNV-5rcCqAXKGA_2HwKrhQGCal-Gucksq1NC6HUPT7cEGyxW0H2iaLlbiC7Fm37P4JyP2iy28sNao5dLJaLAnK1MYaWk1_9ViDuGp_fKsdNdicVDFRhMib6U_OSj9JmvCyscKY0yPg0XN-qqwzZFiiKC8Y8KUjB2DF_DT737j03xN34NYN9ucyhQjUTGjOBD9CazxMiUSiS1ZwBe4XU6KTIM0nqboH1ADQzh7HyRCs_pSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
5 داور نامزد اصلی قضاوت مسابقه فینال رقابت های جام جهانی؛ علیرضا فغانی در رتبه سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25658" target="_blank">📅 11:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25657">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bb7a3c33.mp4?token=c7tOEZNDJd1bBtqQwNel4PseqGrPb6YzF-SfH-5yxTjrJetadSotfoiB16HPUwpVDu_CYCtVFT-eu4NAK8Gjte7at8k3e_B2xXz0uq669-Kc5t6h6Uze3UOOPhCTMXM09R3u6cw0J_RgKy1A-fqTi8n2tPxUbPtaKyiZa4D8YKZhrAIo71EnCAJ2yaFzso5NmtIZx7S-qwMGbH8WKvMEgxYKooTKwvJkolVRQeQ65mn6XNfd4OpvsaLewWWX7hzfsau-QmP9BjMOVopztAdgmDBx4cx4ADh5rtmTYSr4BPRd2bEGnMBZZ1-NXrpCi_v0tyjc-xNPCHIM0u9aHhRGyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bb7a3c33.mp4?token=c7tOEZNDJd1bBtqQwNel4PseqGrPb6YzF-SfH-5yxTjrJetadSotfoiB16HPUwpVDu_CYCtVFT-eu4NAK8Gjte7at8k3e_B2xXz0uq669-Kc5t6h6Uze3UOOPhCTMXM09R3u6cw0J_RgKy1A-fqTi8n2tPxUbPtaKyiZa4D8YKZhrAIo71EnCAJ2yaFzso5NmtIZx7S-qwMGbH8WKvMEgxYKooTKwvJkolVRQeQ65mn6XNfd4OpvsaLewWWX7hzfsau-QmP9BjMOVopztAdgmDBx4cx4ADh5rtmTYSr4BPRd2bEGnMBZZ1-NXrpCi_v0tyjc-xNPCHIM0u9aHhRGyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25657" target="_blank">📅 11:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25656">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f067d59f.mp4?token=B6nglUD6HRQyiGWwZb4GZcKweBXr4bb2zioNr7NNUlMEvKKcLUXAOak0Xt0s80-e87FLROx_0R2ZQ8cFxLU3IqEsyapKM51l5jLwmF3RXuxNevT6Wf1tzijUV9rATDfSt1xPL_Tl5CfZWEhvo6iSB8nlseI3p1cThfQBgdlv-e86D2ub3caMSFjKAiuB3Nt_wse4i6GSsY07ynHCkSFMHqqITXr4u-wdxHcsZ8rEjtTjGpbhRW3c7oVBfUiONsDfE5hV9SfYuNhIwaQ8h6pJDMtuMtnUPmfH3kB-JBKwyYabn0RC_arAzqnlsnuTDLgn--PQS10xk0VZFnrUE7wmpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f067d59f.mp4?token=B6nglUD6HRQyiGWwZb4GZcKweBXr4bb2zioNr7NNUlMEvKKcLUXAOak0Xt0s80-e87FLROx_0R2ZQ8cFxLU3IqEsyapKM51l5jLwmF3RXuxNevT6Wf1tzijUV9rATDfSt1xPL_Tl5CfZWEhvo6iSB8nlseI3p1cThfQBgdlv-e86D2ub3caMSFjKAiuB3Nt_wse4i6GSsY07ynHCkSFMHqqITXr4u-wdxHcsZ8rEjtTjGpbhRW3c7oVBfUiONsDfE5hV9SfYuNhIwaQ8h6pJDMtuMtnUPmfH3kB-JBKwyYabn0RC_arAzqnlsnuTDLgn--PQS10xk0VZFnrUE7wmpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کسری طاهری مهاجم جدید نساجی:
من اونشب تو شوک دعوای آقاخداداد باجواد خیابانی بودم که به یک‌باره‌رسانه‌ها خبر دادند که پیوستنم به پرسپولیس منتفی شده. بله از الان به بعد بازیکن نساجی هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25656" target="_blank">📅 10:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25655">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyaLlI4fXJDh9hkv4OjzG95Tei6KkaoM93P_DVxm-K7WWYXUU7ilo2h0do4CKM8cA8jq2F6kmrcBAwHzstisB3TVMC9kT5Y6L25t2C0w48kBVwLKVHE42sWzSIN26kTHKz8uWCDAOWhMqmcRexM-M_g757Fj5AVUlawIDenF6-0P1aHAf7qxAixSlchf3yBT_Zuf7dKP2cO_Mow0ygaYUiubxCTRfQISHwTFfaXwBUfnfbHZJGMUW5QaF8M7E8ZCmPSStXVuY8BUfZF5yJCSViJFQrG-wE2d2IJvr9_LczUodXY_x7Z19kUjHSU897QhBaJm9D57SX1irvvpcOlILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ باصلاحدید کادرفنی استقلال؛ آرمین سهرابیان دیگر مدافع میانی استقلال در لیست مازاد آبی‌ ها قرار گرفته و بزودی از جمع شاگردان سهراب بختیاری زاده جدا خواهد شد. پیش تر عارف غلامی نیز در لیست خروج استقلالی‌ها قرار گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25655" target="_blank">📅 10:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25654">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5705053c4.mp4?token=Vzg4huzjvH3LahxaKuyQtfFm15eh4pXw6Vj3wBf20NFJrHUeK7hrMzPWgSWOlpcI2DgPU8v0u0ynCicURBAMRf16IXkPZdOaBk3Z_GEDGL8kPvhZwovOpUUa3CaZ_yUyd4iQ78uPXQ79JWRdJ4uWch3TdeF125VhHWy2sNL9mAqj5B66RiHor4IsDmd-uxm_rJaXgsIjfGOHQ6YKbBK-0HmKfaLL3jF82KyKU4u2fpXmky4NqSmMM4GyZLRJAaQ031Wr68DFlHxlXGTZl5-w2fuZrOhFeLMwFgDphk6Iz_C11E4lhQqh7qY-W1eKcd32rxe7-bssEDouWrOMMUoV3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5705053c4.mp4?token=Vzg4huzjvH3LahxaKuyQtfFm15eh4pXw6Vj3wBf20NFJrHUeK7hrMzPWgSWOlpcI2DgPU8v0u0ynCicURBAMRf16IXkPZdOaBk3Z_GEDGL8kPvhZwovOpUUa3CaZ_yUyd4iQ78uPXQ79JWRdJ4uWch3TdeF125VhHWy2sNL9mAqj5B66RiHor4IsDmd-uxm_rJaXgsIjfGOHQ6YKbBK-0HmKfaLL3jF82KyKU4u2fpXmky4NqSmMM4GyZLRJAaQ031Wr68DFlHxlXGTZl5-w2fuZrOhFeLMwFgDphk6Iz_C11E4lhQqh7qY-W1eKcd32rxe7-bssEDouWrOMMUoV3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ایسان اسلامی درخصوص درگیری شدید دوشب‌پیش جوادخیابانی
🆚
خداداد عزیزی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25654" target="_blank">📅 10:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25653">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33fe4e361.mp4?token=PLrRBGmpHLawu6_haeL4dZIZl9g1iTySKfbQy2JhbVYe_29kI-LvEMiBbOtkSidxUxDKFgBQ8qOW94Ts4taSkmTAgBkPH2Zw0kaf8DT14DviqC9oGnO2xixaxAmMX--IQ6VIALBHRMaEZgfikbgwhY3Y47WFUv-ZEHSSRe1KJ5WvI_1TBHf4qEeR5-mqZrBgmLHvdV9ijERUeajzNfQDwxCiEksA9H96i9ie1WqQ3ZMeZWkiy7liPARJI77oFO5KEzQi-oBAhg2bA6oIxJP8EZnZkznlGWIwJ8dHTwPg-ZHccHfLOXVrgxDH9S9aybP36E5Yd2PwAJacbiZlxoOq-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33fe4e361.mp4?token=PLrRBGmpHLawu6_haeL4dZIZl9g1iTySKfbQy2JhbVYe_29kI-LvEMiBbOtkSidxUxDKFgBQ8qOW94Ts4taSkmTAgBkPH2Zw0kaf8DT14DviqC9oGnO2xixaxAmMX--IQ6VIALBHRMaEZgfikbgwhY3Y47WFUv-ZEHSSRe1KJ5WvI_1TBHf4qEeR5-mqZrBgmLHvdV9ijERUeajzNfQDwxCiEksA9H96i9ie1WqQ3ZMeZWkiy7liPARJI77oFO5KEzQi-oBAhg2bA6oIxJP8EZnZkznlGWIwJ8dHTwPg-ZHccHfLOXVrgxDH9S9aybP36E5Yd2PwAJacbiZlxoOq-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند: توقع‌داشتم‌عادل حتی به دروغ از من حمایت کنه و بگه‌مورینیو از من تعریف کرده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25653" target="_blank">📅 09:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25652">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c3b52fc8.mp4?token=V8jNafQ3Qi8thICSGseeWaXuTFfX0UWxnhhqbnDWWh6rVvL-mnVH1iyFxu9ral_WbOzpvN3DfWCnzuWt8JIGofRiQMRab-2SsUUUBX-fTfWxRye7FlDGD1fs6Is4BwhMHHTGorXHQnLhYNfqcfj9mcMXxrHpHs7dAofZm_2eR0Ds5ZJBPE3wJCLTVM4w71QHkSFqAnMbEParTddmFon8M72SeYasd3GUm1Z-xdg6XwIHtb_AwEmkAm6oBKfRkzyH2NqNqbkT7r8W5iQrTmV_P7zjOZHRFiWQwhc8t-Lqoiuxy4P4IplHhMzf7239_rcaDeFHnHJ4GMz4kPbhqqmA7CHjxecY9fM-5BUF4nfv0xS2mkEoeaExrVnhLPzshHxQqqPlzEywFCgpDS5GU0hM2khavpfAfLMR1voNfn8FKFn3QGwtAmbV7-8mc3-MREP1BR0Xi6a1ZZFQ8Rw6Lk_ViVjelk3iWpHwwBa_9xb_wzYNSgHS2p-KlQd7LOatLFeZRAdRdIzpBBqmKAGcG9e3bIE5E3WFx6XFg7rtITQZUVlbjSxNWpAv5wIWBhG-w3VOncGtcMdVHDCHJEEwLtkyRp2xtGH-qkTABncOvZi7Qq4C1jhjjgcMt8as4KavtCseZu3Am2IEbVT61mxVl_MfmB6s3ZpT32I3hVlOTYw-pDI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c3b52fc8.mp4?token=V8jNafQ3Qi8thICSGseeWaXuTFfX0UWxnhhqbnDWWh6rVvL-mnVH1iyFxu9ral_WbOzpvN3DfWCnzuWt8JIGofRiQMRab-2SsUUUBX-fTfWxRye7FlDGD1fs6Is4BwhMHHTGorXHQnLhYNfqcfj9mcMXxrHpHs7dAofZm_2eR0Ds5ZJBPE3wJCLTVM4w71QHkSFqAnMbEParTddmFon8M72SeYasd3GUm1Z-xdg6XwIHtb_AwEmkAm6oBKfRkzyH2NqNqbkT7r8W5iQrTmV_P7zjOZHRFiWQwhc8t-Lqoiuxy4P4IplHhMzf7239_rcaDeFHnHJ4GMz4kPbhqqmA7CHjxecY9fM-5BUF4nfv0xS2mkEoeaExrVnhLPzshHxQqqPlzEywFCgpDS5GU0hM2khavpfAfLMR1voNfn8FKFn3QGwtAmbV7-8mc3-MREP1BR0Xi6a1ZZFQ8Rw6Lk_ViVjelk3iWpHwwBa_9xb_wzYNSgHS2p-KlQd7LOatLFeZRAdRdIzpBBqmKAGcG9e3bIE5E3WFx6XFg7rtITQZUVlbjSxNWpAv5wIWBhG-w3VOncGtcMdVHDCHJEEwLtkyRp2xtGH-qkTABncOvZi7Qq4C1jhjjgcMt8as4KavtCseZu3Am2IEbVT61mxVl_MfmB6s3ZpT32I3hVlOTYw-pDI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
به‌ بهانه بازی امشب فرانسه
🆚
اسپانیا در نیمه نهایی یادی‌کنیم‌از بازی دوتیم درجام جهانی 2006؛ فرانسه‌ای که به زحمت از گروهش بالا اومده بود به اسپانیای آماده خورد که هرسه بازی‌گروهی رو برده بود و اغلب فکر میکردن فرانسه رو هم میبره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25652" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25651">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOX7u81B4EElbSm6ZPquXZjqoAGKUOYK10WIRhp0znjli0mYWgSt9Za_ElAAus7acyk2sNZcGG93iGLLQ_pOiqi7xWXrobPGlLx0nFEtpzVd9NeKV22R_EAzydjkCv8Uuvp_kXN2Lkb5g4ClsvLR6c6urEIwnVmkyc-OLUVOYZqStWovGZc9MLVpAEzaXRQ0KwtducesnWnIsQgXlI6P6IlTRVV8Yb9b4mnVo2YVAf6MAlzCMgLThuesvNQKvmDif8_8hseBBiPK5mnSYOu7ivGcnGC4k-gTXf3b3ycjtX_3Bs_58F0gx7iL1Gj2b8vB5yZhpR2Uaa9kSVsyqduUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
#تکمیلی؛ با توجه به اینکه قضاوت دیدارهای نیمه‌نهایی به علیرضافغانی نرسید؛ شانس ایشان برای قضاوت بازی فینال جام جهانی بسیار بیشتر شده.
🔴
فکرکنم‌دیگه هممون دوست‌داریم که آقای فغانی فینال رو سوت بزنه. انشالله که نخوره تو ذوقمون و فغانی بعنوان داور فینال جام…</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25651" target="_blank">📅 09:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25648">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/298c4f2fe3.mp4?token=hZJl6U1MYaCcqgAGsNU4Fcn9YrrtrcGkS7GUbEdbWepMwKZKEbPiM6VNxBnst-AHaE7gNdBAJeF5SjuVkrqLJKocznSd-dw3UPU24z-tVo6NI-m9E9MvzaMzJXC04WEmwpaYTYxVQSKdHLoSg-eY47_pDjUKCKm_-qlfKz5hf6Z0zhAr2hCUaxrue21Edc1P-po1F_ej6rQirxCjYkYbBQVPYnqI4ehWAHySXu1wcc2PiEcKX6SRlgBZMEwMpf3Yf62ErQxhULYBzH-b3xVuh-Ctv9yIP0HzCw_WDkwy3Yaz0kdiyf2bpn10lhBqVREY2iF9Kpvx2qDOSubzJvvO9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/298c4f2fe3.mp4?token=hZJl6U1MYaCcqgAGsNU4Fcn9YrrtrcGkS7GUbEdbWepMwKZKEbPiM6VNxBnst-AHaE7gNdBAJeF5SjuVkrqLJKocznSd-dw3UPU24z-tVo6NI-m9E9MvzaMzJXC04WEmwpaYTYxVQSKdHLoSg-eY47_pDjUKCKm_-qlfKz5hf6Z0zhAr2hCUaxrue21Edc1P-po1F_ej6rQirxCjYkYbBQVPYnqI4ehWAHySXu1wcc2PiEcKX6SRlgBZMEwMpf3Yf62ErQxhULYBzH-b3xVuh-Ctv9yIP0HzCw_WDkwy3Yaz0kdiyf2bpn10lhBqVREY2iF9Kpvx2qDOSubzJvvO9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
افتادن شال یکی از مهمون‌های امشب ویژه برنامه عادل فردوسی پور؛
تعجب عادل عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/25648" target="_blank">📅 01:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25647">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euxc2J3kAh87uUKM411oAJw03yS5IELJCp52MSw1ikFkuiMh0PGen_D12DYq9U-W9f_zmGNyPkHr_nNO6BhfCjYjGFF4J70UwF-p8UMFGpSWnFR6x4dVOFgyubXoBEQGNOoo40fL57nl9PfoMyvBB-XAYyUGnZOUnXIP8xQ7SalqTlOsu3b6h_SaI8yQ623_SZ9M_Zq09nFsNEI317XdTqIyipYRqFHEtQKs2XQ3rb7VNoxZkmQaMEak2_cJL4ihxOvxDoJonnRdM57iA_HESn5JH4F9ReqwnXgtMBvl-5SzHkI2J4_ros3_XiUcDkdg8CmWUVporwOFtbv8CQ4LTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
علیرضاجهانبخش کاپیتان 32 ساله تیم ملی:
تا یکی دو هفته آینده از باشگاه جدیدم رونمایی میکنیم‌. اگه‌ایران‌بیام بین استقلال و پرسپولیس یکی روانتخاب میکنم که از همین حالا انتخابم رو از بین این‌دو تیم کردم اما همچنان دوس دارم اروپا باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/25647" target="_blank">📅 01:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25646">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYr8aoYoBEenURQoT8J69xxzNVDJQ967ynEWsEc8KQRsVmSww6b97zQNFcVWY42IqvEvR9Msccbk-7Ep9v-_oFqXV3HwASJEk18wK_V0OogfNDtTqbgjSfZgsTVO99xE5nD5dFtgeH0K5ofe4MKs7qW5Fc7Sk7P41UaCWIyV6X2tTADflLD1r7iaPDO6sJafwkqmGK-ufUaGSslVNzVMcDxd1jN6DlQnIPazM3w-fX6XMO48csU3szqS2dUAvTzENCmG8ragwbVqstThQVfYMGUcusRsPmk_21RzDuzdvXxcx5DtVHLRYx-uwxISQ5AiA2jJ1vyoSxxTZlGwAtAbLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛
نبرد فوق‌العاده حساس دو تیم فرانسه و اسپانیا در نیمه‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/25646" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25645">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3e63bfe28.mp4?token=rD7QDsmQ8zvOU1jE3pag1NLKn6ib3qDs0KJkJjNVLc28YtsFfBeaTSse2i8Wn1N0rw2Sw90YESo3NLREOz7UueVNKX-Bqc3_81H07nXTzSruvcPDVok5Zmorp9rcsUa2MpwILUIU1_dL3rW5q4Uz9JO0i9pu4wOXaC_c3huvUqqmGE7xaAGAiDaBW9cgTGTG5psYUU1w8l1Eu_F9SQQ47Cjo8r7le1VLyg5UDsyaVaefIyQZ7F1Eq0UT2IESXYFmpBzxV6U7lZkIllahOayI8LQUU6ol6gK4dan6puGivMp1dvubu0JfG5xj-Zd1PDWXhA926uK3JBQJtH_lTESttA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3e63bfe28.mp4?token=rD7QDsmQ8zvOU1jE3pag1NLKn6ib3qDs0KJkJjNVLc28YtsFfBeaTSse2i8Wn1N0rw2Sw90YESo3NLREOz7UueVNKX-Bqc3_81H07nXTzSruvcPDVok5Zmorp9rcsUa2MpwILUIU1_dL3rW5q4Uz9JO0i9pu4wOXaC_c3huvUqqmGE7xaAGAiDaBW9cgTGTG5psYUU1w8l1Eu_F9SQQ47Cjo8r7le1VLyg5UDsyaVaefIyQZ7F1Eq0UT2IESXYFmpBzxV6U7lZkIllahOayI8LQUU6ol6gK4dan6puGivMp1dvubu0JfG5xj-Zd1PDWXhA926uK3JBQJtH_lTESttA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/25645" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25643">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAuKGeBramWJgtuIGv94si87At0ykXLwnYUItJMsbh0zbBWpDJIUOLC3_qohvQDPNcZnQsd1OIoh5LvonsKw7ACPCfOzPIuNV-ATn6zc83pSg9L97Sx_l9YtoKalk7LpooaZjTyLXc38sO-7ZTXLGe25C_sGE0F5PUS_i2qdHyyo7ueY5NUx-8SvdggIs_mfA79d9pY2SF5sYGw6PPDTJarXlHe3dlMeHKPuOvpDJ7-MPSjDPGuSIGHAzZIpp1lFA6U0ZNJB_wKZmzz73JezGOT7Apj86q_Ar08na6OKqN7cfRYxtQEHOm6wEMHx21-r05c4CFbvRArUfQyXLIMzgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
با اعلام باشگاه فنرباغچه؛ اسماعیل کارتال با عقد قرار دادی دو ساله رسما سرمربی این باشگاه شد. ارزش قرار داد دوساله کارتال پنج میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25643" target="_blank">📅 00:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25642">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98ca4a5638.mp4?token=aZ9yFSqi6XNT9Ny16uagtfK5Bfai8gMUCvkHRAJSv7_5YNtJ7bc3_qHwmFaRgP4w_bFsAk0-Rxd23MHeLfvAXTYvKyKNE5_unrCuXiYjOZ-aIm3TzFXcJlBVKFN4ixYD1ov2hcFmY1Og58YRwfvtxjRLs1V50twepFlR_3nRvRXmLppNGKyxosgRpSzuv2-K9uUzlFhsCOm7ApYYOV4EojFs6OJtufMHyA_bkVn1RjsXUZSvHlZ8CjHXmNImc3WiJ-KpUTtxKFVZNGhXSe-yIcVcUZuLxIk_0rfNzBjoZN5bOsUr4YnpsG08yTuXf6vFZK1yaM-RFOnpnVHmhid1Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98ca4a5638.mp4?token=aZ9yFSqi6XNT9Ny16uagtfK5Bfai8gMUCvkHRAJSv7_5YNtJ7bc3_qHwmFaRgP4w_bFsAk0-Rxd23MHeLfvAXTYvKyKNE5_unrCuXiYjOZ-aIm3TzFXcJlBVKFN4ixYD1ov2hcFmY1Og58YRwfvtxjRLs1V50twepFlR_3nRvRXmLppNGKyxosgRpSzuv2-K9uUzlFhsCOm7ApYYOV4EojFs6OJtufMHyA_bkVn1RjsXUZSvHlZ8CjHXmNImc3WiJ-KpUTtxKFVZNGhXSe-yIcVcUZuLxIk_0rfNzBjoZN5bOsUr4YnpsG08yTuXf6vFZK1yaM-RFOnpnVHmhid1Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای شدید و مجدد خیابانی و خداداد عزیزی که مجبور شدن پخش زنده برنامه رو قطع کنند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25642" target="_blank">📅 00:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25641">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3d13a462.mp4?token=U58OIWVH8ILRIDhERrAJe1b8wPaOcj9v6VXBrA_PvHTXeUBnlJXvdU2r-BUt7YuH8d-cBM5BRXk1_dSXOj24dXvcmcDnrB5kQCKPl38o5ULFZE3NrwnPqyhgVmNmoI7IoGyMXI73SpSH29mRFapUggbNuRErKu6fxRBG0dsZefWwICrbhZmIfQ_PnhBBFV_IergjS3ZHQ0VE6SWofcNsQZHk2nhBk_2LB-2hXz-6lEzLJSl1OqCwpR52-MVKDRNqUfF3QYINrJSfMuvh6eUfqyQp6b97jT0drEbBl9eQRBcEjPLkqDxBEe7sLMj8xLGO9bAxCIV0lI6msd_7bPiCFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3d13a462.mp4?token=U58OIWVH8ILRIDhERrAJe1b8wPaOcj9v6VXBrA_PvHTXeUBnlJXvdU2r-BUt7YuH8d-cBM5BRXk1_dSXOj24dXvcmcDnrB5kQCKPl38o5ULFZE3NrwnPqyhgVmNmoI7IoGyMXI73SpSH29mRFapUggbNuRErKu6fxRBG0dsZefWwICrbhZmIfQ_PnhBBFV_IergjS3ZHQ0VE6SWofcNsQZHk2nhBk_2LB-2hXz-6lEzLJSl1OqCwpR52-MVKDRNqUfF3QYINrJSfMuvh6eUfqyQp6b97jT0drEbBl9eQRBcEjPLkqDxBEe7sLMj8xLGO9bAxCIV0lI6msd_7bPiCFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
فیروز کریمی درباره‌انتخاب دومادش بعنوان سرمربی تیم پرسپولیس: انتخاب خیلی خوبی بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25641" target="_blank">📅 00:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25640">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npmdJVUGKNWm2ygu21kBKRkfVmxCnyRQwnDohj_p5a5fsygoRRLNSEhtq2YSmkt-po9rtWpYly9lXOUJ2eWj7j8ydEK1lLzGPrruL-_vPdMTveTDkhcQsJQn34ubd1kp6PMXPCWBZBEcc6iQuZ3gdoSh7Z4sbXiRVlb4tAmr_0kr5E4QEGic06aJ4nNfapFmvBZI-hjAQEeRseoPhiSDnq-99BsxmnfhQpXO1uO9z3sCh3z3OEMWUQwX-htrSZ5swtpyw0ST3KL80KlsRpSaPPrb18UEJXKFT2eejxpmLEDg4ji87AhbGQKfQgFOX2U-A_rrAvgqZD8KRG3-54geHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
رامین‌رضاییان ستاره‌استقلال درسفر خود به فرانسه‌کیفی‌از برندمشهورHermes به همراه داشت که مدل‌آن Birkin 40 است و قیمتی حدود 21000 دلار دارد؛ معادل 3 میلیارد و 800 میلیون تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25640" target="_blank">📅 00:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25639">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNr-KxqyTVQIEufYLPfoMie5wSfZ0QqzUrL8jW_5OAS7HVP8gWjwoYA8-Kdnw0Sbeo_n-D9vNuhjlfac1CnDwDNT8wpX6-blMqkmawq5IdrmMfyvMQdiAZ99_0Gh4_04uacEcin9r_Cv24h1TBGvoRt9BKi25IeUipvf2ZJ7w-5WZJV_joGJVlIZc4WGP3Ol1V69K2n93uQFHtfIQ5sQMlMpBL5h3fC90FPKcQBtxus8PAt0MCgF5RmMiUaAVDmYXmfTJRCWWFm1QFfoHWg0id5pDCfOaPwRrnItBXs6-LYMRB-w3OYwkBhTKLMIuRgeyZ2m2dPJ9D9yY6UBK-srjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس باارسال ایمیلی به‌باشگاه‌‌الاهلی‌خواستارجذب رضا غندی پور مهاجم 20 ساله این تیم شد. اماراتی‌ها پیش‌تر مبلغ رضایت نامه غندی پور رو 2 میلیون دلار اعلام کرده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25639" target="_blank">📅 00:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25638">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5yI2-Ywignqk0cGh-hp0GVtRErGhRZ_ZRoeKoc6OncNTGaeRnHkBNKS9XE7Ox1wytjHVqI_YU2Q2h4TwXo2iyX3CsdUMEOs_wq5yUsLJuooCUUMmNJyo3Qtw3r53wNajv2rH4BvqzU-jOJunHT7X39Hyb2Vi-bJNvSeNX-mFV6ffVyJZDbY9v7AimIHnchQQjsScwK3wYl85A_cMBZ9_VC77w0sEAk-MSM4PUeA_KASsEIpXyldXJ4WpYq-HIv_kz8BsvRGDoTte69EUXcx1sjLCQB7ZnAmSn71jTbmed4mJmkpVFNXONyl61pF8d33wEElCHHtNH_EKoAyj4c3RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
این صحبت‌های مدیرعامل تیم نساجی نشان میدهد درصورتی که باشگاه استقلال در جذب جواد حسین نژاد عزمش روجذب‌کنه با مبلغ زیر 3 میلیون دلارم میشه این بازیکن رو خرید. فقط مذاکرات باید حرفه‌‌ای‌باشه و بی‌تعلل مثل آقای زندی‌. گفتنی است باشگاه استقلال برای جذب حسین…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25638" target="_blank">📅 23:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25637">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8ae1ae07d.mp4?token=JUpuIcE-djc-KWA3q-4N9XR1dWh294oVth0lKBA9WbsqZ-G6pbPPl0hKDh08qK2_nTVxZhdp9LVeQrwVgfQMo8jXog9Ucl9rX8MfCA2mrzH9QahBqmYbkZ3fb0jThFymrzu6wHI5eFsvRlBnhBMwkQf8aE7AgCqZfrgdcqsZOuUYtnJ10yItWDWnRSZxjbV6mMi07tl56mrzqo6Ggve2QyJTwtBNWnLFH532oCP-3sBM0PV75TISMcRFnZCj-3NGPm_vFF1Gw6tQrFVO7DfWDm_swgRHmYZ0tVVjxIVieI2nc3N9wOYiV3_em5LO4MyNp6O1wi6QW0xoim_JGpwLnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8ae1ae07d.mp4?token=JUpuIcE-djc-KWA3q-4N9XR1dWh294oVth0lKBA9WbsqZ-G6pbPPl0hKDh08qK2_nTVxZhdp9LVeQrwVgfQMo8jXog9Ucl9rX8MfCA2mrzH9QahBqmYbkZ3fb0jThFymrzu6wHI5eFsvRlBnhBMwkQf8aE7AgCqZfrgdcqsZOuUYtnJ10yItWDWnRSZxjbV6mMi07tl56mrzqo6Ggve2QyJTwtBNWnLFH532oCP-3sBM0PV75TISMcRFnZCj-3NGPm_vFF1Gw6tQrFVO7DfWDm_swgRHmYZ0tVVjxIVieI2nc3N9wOYiV3_em5LO4MyNp6O1wi6QW0xoim_JGpwLnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند:
توقع‌داشتم‌عادل حتی به دروغ از من حمایت کنه و بگه‌مورینیو از من تعریف کرده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25637" target="_blank">📅 23:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25636">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4483a354d.mp4?token=olD1dFB7QrBvbqigHA4B9U2jYgLkcvExyzfmeU3358UQOmqI8uZIchoNrBYqLzbF3s_lWYktJsCLX19XlCNVSldWedd4t_7oiLGsdcWMaW-69JCOv0H1RTszeBEvhAbc9aeCf2oDqVWKIjo2v1nbA9GGfLkrs9mqL_FmAjmGL_scma1dYh--FeM0eMbYZ8zmhZwch3t9ah8w5Br7fKeRff4Dw3t1BwYU69DwnMY5OKOCmikg3UsfVR9yjziAtvyRHwFv6lA9l4TcaITaaWr4u8Lvv5_55_aheSSlIaIpbM7R7ujbULh4VfyhEbc6IzBYBytT-PsWruN3De2_uGtrUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4483a354d.mp4?token=olD1dFB7QrBvbqigHA4B9U2jYgLkcvExyzfmeU3358UQOmqI8uZIchoNrBYqLzbF3s_lWYktJsCLX19XlCNVSldWedd4t_7oiLGsdcWMaW-69JCOv0H1RTszeBEvhAbc9aeCf2oDqVWKIjo2v1nbA9GGfLkrs9mqL_FmAjmGL_scma1dYh--FeM0eMbYZ8zmhZwch3t9ah8w5Br7fKeRff4Dw3t1BwYU69DwnMY5OKOCmikg3UsfVR9yjziAtvyRHwFv6lA9l4TcaITaaWr4u8Lvv5_55_aheSSlIaIpbM7R7ujbULh4VfyhEbc6IzBYBytT-PsWruN3De2_uGtrUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وسط برنامه زنده شبکه ورزش برق رفت!
رسول مجیدی مجری‌برنامه: بازماانتقادکردیم نذاشتن ای‌بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25636" target="_blank">📅 23:24 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
