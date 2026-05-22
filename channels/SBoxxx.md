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
<img src="https://cdn4.telesco.pe/file/NAah_HD4QggWT8Uh3kl1niWirSCMOmzytnzy81adIYsz2DAj1TS-VbuD7KoRPzdSuC9T33wSss-vEghvtbClIPxsmx6OmGD0RPnII8fKzSHLQD93NoxnJOwM5g6_MoPDtDdIid6XGgD4i5CgDqNloMvZoMPsGg0ScJQ9IWwHnDb64tYiDTgmwowdNEI9SkUy9gPLK_WdMQ6-I_LrGLL5AFL_q9MxwjD5EisLx8MCj_IuVc8nZX-grUIXZOhscw9uPU1Wlg8M4VMkeE9tnePIbyLGpFV4zuhNV9zhmqf0N1Yp5GxHkBeuflGjbWpO7DYVi8Muq66FRAQKnNrgdexBkQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.87K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 22:54:31</div>
<hr>

<div class="tg-post" id="msg-16529">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ffd0c130.mp4?token=J2KsfgLIrkn7Og-J3uMx8Ebuj5kEPAvxxieMkP9RUsjZtMTlTQwQCvaN6QWH-w-BUCkKaRyD0JY0V_byjYglxaZ7zHmMX_gVtA7jFunaIP0pUdHZE7S3mRppMOLz1IcV5hg9P18zg-yMAII_HdFVbmMheh3whRh29eF2ghaG_GXm6vJTRlfIJCYvMmkGtAeHpqIHdbvLQvt-J0-7Zvy1gAiZWmcjsGKBaQYX9OCsr0fZ6MshMet5-Bvy0mI60o40BwPTYDWkns7rUkPfAkBOTzCPCD0JKadhHetgMBPNBRNki-HEidGhUZfx5Sx2xS9hP42S0QdRlaW_swzro-8jog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ffd0c130.mp4?token=J2KsfgLIrkn7Og-J3uMx8Ebuj5kEPAvxxieMkP9RUsjZtMTlTQwQCvaN6QWH-w-BUCkKaRyD0JY0V_byjYglxaZ7zHmMX_gVtA7jFunaIP0pUdHZE7S3mRppMOLz1IcV5hg9P18zg-yMAII_HdFVbmMheh3whRh29eF2ghaG_GXm6vJTRlfIJCYvMmkGtAeHpqIHdbvLQvt-J0-7Zvy1gAiZWmcjsGKBaQYX9OCsr0fZ6MshMet5-Bvy0mI60o40BwPTYDWkns7rUkPfAkBOTzCPCD0JKadhHetgMBPNBRNki-HEidGhUZfx5Sx2xS9hP42S0QdRlaW_swzro-8jog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
آزمایش و رونمایی گسترده چین از نسل جدیدی ربات‌های انسان‌نمای پیشرفته با قابلیت‌های نظامی و امنیتی
این ربات‌ها در نمایش‌های عمومی شامل حرکات رزمی، تعادل پیشرفته، پرش، و تعامل مستقل با محیط هستند و توسط چند شرکت رباتیک چینی به‌عنوان نمونه‌های «آماده کاربردهای میدانی» معرفی شدند
فیلم ارسال شده مربوط به رونمایی حرفه ای یکی از ربات های انسان نمای بومی در آنتن زنده صدا و سیما است:</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/SBoxxx/16529" target="_blank">📅 16:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16528">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🍆
طبق ادعای برخی منابع ، عاصم منیر ، بلندپایه ترین فرمانده ارتش پاکستان به زودی راهی تهران می‌شود
🔻
رسانه ها این امر را نشانه ای از پیشرفت قابل توجه مذاکرات می دانند</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/SBoxxx/16528" target="_blank">📅 16:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16527">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
الجزیره به نقل از منبع پاکستانی
:
بالا رفتن سقف خواسته های جمهوری اسلامی ایران و دولت ترامپ در بحث تنگه هرمز و اورانیوم های غنی شده ، منجر به بن بست در مذاکرات شده است . ما همچنان به حصول توافقی واقعی خوشبین هستیم</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/16527" target="_blank">📅 12:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16526">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKeApkqQFALKRqWzRcab1RZntCMFszMJg_30jQeKcvfRxUuAC3AkRS4HFjkykpW4SXJe9RGlFHI5DSD5hGgevo7ibMPAVoq2psIpdakMLf7chI9Oj5mmIEIbUi5ek018KSUeNgorUGNR1GWUG-e8W8kcDNxTkHHtH9ctNiu6ahWqYMt9Q7JXQdkToxqXmJzIlw_hJMwj4u5ox0RgsQY1ml19Sp5eTW5DHlLA5dt4Ks7W_MxntBhbnjYT5ZPTHODQNhkTc6quBd0SmRDQP4B86JF6nl6bhpjnLIn4McXZoO3sM4T4r87Dtx0sEA2ANX8VdiH00U2sRQa--uqtik4imQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#TUR — D  عیناً طبق مسیر می تواند با تکمیل این سروشانه که همسو با پایان یک رالی 5-موجی است یک افت سنگین اصلاحی داشته باشد و سپس رشد اصلی طبق مسیر پست ریپلای شده محقق بشود.</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/16526" target="_blank">📅 10:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16525">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiI5h_vhFwZYpf6XL9lF0SUgrgtqySyOYL0kkexHnzsUyrhry6pUMNOQzf8JTlRdQYISR7uJfKoKgFPmqHX9keJJilwz6GuOgJdqR1sYy8gA95fvRHsqNlj4CoBw8EDtLp_ulyJ0EFxZ0otLfOUHqQhKrcsHU9f6uKN5OO7QhVm_1FxffOXME4hUL4CXPZw4Num-TJjn3XxtGqE0G7lbBii8nH93VIRP8yrSDYUKFGVUasSH1OL6IJpmKh4U2_MmFj2ZFc9ApcV9qW9U_DiVTBcOiIu3tNHBYqmLor218icubvNNNX7xU1DajFoYnvTWAGjzC3AI9ZybV68Rr9HOxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#TUR #Turkey
🖊
با داده هایی که اخیراً منتشر شد (موافقت ترکیه با پیوستن سوئد به ناتو و انعقاد قرارداد خرید تسلیحات 23 میلیارد دلاری بین ترکیه و آمریکا) به نظر می رسد سناریویی که اینجا گفته بودیم (نزدیکی دوباره ترکیه به غرب) در حال تحقق باشد.  این نموداری که…</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/16525" target="_blank">📅 10:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16524">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQ_rt85aIXfFUlDNWCUU9a4LB2TMKdEm7RGq_s6_I-cUhOgPJKdtpyqVu4EDhBPNhc-I5Nz30CQyPQIvWz3cw2QITFRlGz8uQVyxPtR3u4uhGKzf-9EdU1SUkAVs-2J4AY2ZlP58bNiCWmMgAHneBhKouqvmEMVZEhGl6EpJUDC0jX-FBt4rE20Sd87iiMZ0p61gYXAUuR60whWJGzM-DI2CBOJryJrNMkmNb5BrU7dUhJtObaUQwJKAPCE4KSRWgBYF4Fwfv7KbaqmBpJPSCE_NKjMoGLl9chVbOkXq5CRRhwe-kwVNXtjepHs6dPYln7AUEiz636glJEnC8LkS8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط آزاد شاخص بورس استانبول در پی صدور حکم دادگاهی درباره ابطال نتایج رقابتهای درون حزبی حزب اپوزیسیون جمهوریواه خلق</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/16524" target="_blank">📅 10:46 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16523">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دولت ترامپ فروش ۱۴ میلیارد دلاری سلاح به تایوان را متوقف کرد  بر اساس اظهارات هونگ کائو، سرپرست وزارت نیروی دریایی آمریکا، دولت ترامپ فروش ۱۴ میلیارد دلار سلاح به تایوان را موقتا متوقف کرده تا ذخایر تسلیحاتی آمریکا برای جنگ با ایران حفظ شود.</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/16523" target="_blank">📅 10:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16522">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">به نظر معامله بزرگی در راه است.</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/16522" target="_blank">📅 10:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16521">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انفجار در ابوظبی!</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/16521" target="_blank">📅 10:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16520">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وقتی صحبت از عقب ماندگی ذهنی میکنیم منظور ما این است!  رفته با دیوار سفارت آمریکا در ترکیه عکس سلفی گرفته!</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/16520" target="_blank">📅 10:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16519">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEw7VfGsQM5p6yLokooP6IMOzo_CfEhpQvQaOzlQwBU0CXvVt5IQ86Nm7nW0cwf-ZOr4AxAYux2hdOyNh3CTkcneNdGtGQTZGXqw-RTJFDm2WRyGaN_VCi3I2tI-g6-xfnqs5E08ug1JYbpVt0beCGiO9s5lhNZZa9Q3XYbNQ802Q4DPb2EAOLt397w4gaOpYWH-4g2bmxs52Dqxs-Dxt3Bt9UCLcbYn0V5KoVUeZ5-I-v34c8cu3G6J6w6sTfwDxb2djos9k3RmcavnYN1zXhu_T5L2BgpUHjVJekY9pRSRKOEUkwSf4POjb5rOewq1XN8M_5f3tPnBo03RjeeQqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۸۰ درصد هم عقب ماندنی ذهنی داشتیم که ۱ درصد آن را جبران کردیم ولی خب هنوز خیلی کار داریم و نباید بهانه بیاوریم.</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/16519" target="_blank">📅 09:30 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16518">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCldi8mP_R9Qndtw1unwyVTeqh0bPuDn4if3_VPZtLyHyuaBDEt2Jbcv0QF_vNnbZ86xWBDSvZJFIwZliq8lMr83gM6I4pvwMGebWocWWOqnZd4KZW62DiQTByg3gaYPfBNKYUnIjGzH9O9JxzQeQ8BKkv7H4ERGYV4wsFSCTzCMDL_uqjSC9uZG2QL1p4AU9XOqZd7hkE5XNnXP_muGTJYDg8feomxBlGmhf0OCd4aRlRTNuvkGLdaCv7wH-LXO1ZsVrlw2eDbJRmcAdjKPkTNs5KXFEjQuhVsP5b7N5VFiE_Iq7ZzuIASPy4szcjieJK_6ID_kdmH6m7pRYvJCpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت سهام چین</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/16518" target="_blank">📅 09:17 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16517">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رئیس کمیته نظامی ناتو:
پهپادها نوعی مسئله انقلابی در میدان نبرد هستند. آن‌ها تنها سلاح نیستند، اما احتمالاً برجسته‌ترین سلاح خواهند بود و بر کل فضای نبرد تأثیر می‌گذارند.
احتمالاً در درگیری‌های آینده، آن‌ها اولین چیزی خواهند بود که در جنگ درگیر می‌شوند. آنچه اساساً آموخته‌ایم این است که آن‌ها به‌طور چشمگیری زمان چرخه کشتار را کاهش می‌دهند.
این موضوع به دقیقه‌ها — یا حتی ثانیه‌ها — برای شناسایی، ردیابی، تحلیل، کشف (شناسایی)، شلیک، ارزیابی خسارت و تغذیه اطلاعات به عملیات بعدی تبدیل می‌شود.</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SBoxxx/16517" target="_blank">📅 07:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16516">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNsOxBt1diBlWxBjG3u92Zsc8XHP1pTEhnJNtsVSCUUcuPqwR90bRH1qL8V6iEjovgAsx1Rdj6Qh8SNZwXgPv2cuRDEVrEfD7Vm9HtVoRHeuK6djTtikRYZZAvzyuGPls7yqnnIiaDXJHXcsC7nAe2BT1YpEpsZHb3vKV6qLT1udD9GjQfJlkdTdlkNfVIToBgyKsHbIVD7Eq7VL4TdQXC_bxxIkEWMbk9hZUkFjo_dc8N8nLc-yet2sz-iSpsuh0TtwRYs1Zc2ficfLvWSPvCDiCxnz_rXTV3CadB5qByco4iScUXkjBLYpWoYdC9iT0IWhjoM7ZSHusb5p3BKTGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/16516" target="_blank">📅 01:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16515">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">این جنگنده ایرانی هم امروز در تهران مشاهده شده که ولی خب.</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/16515" target="_blank">📅 01:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16514">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شماها چرا شب جمعه اینقدر میخند؟!</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/16514" target="_blank">📅 00:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16513">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این همه زحمت میکشیم بهای نفت را بالا ببریم تا هزینه جنگ برای دشمن زیاد بشود آن وقت این دوم خردادی های چهل پدر میزنند زیر کاسه کوزه مان.</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SBoxxx/16513" target="_blank">📅 00:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16511">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">العربیه:   «توافق میان آمریکا و ایران با میانجیگری پاکستان قطعی شده و این توافق ظرف چند ساعت آینده توسط ترامپ علام خواهد شد.  این پیش‌نویس شامل آتش‌بس جامع و فوری در تمام جبهه‌ها،تعهد متقابل به عدم هدف قرار دادن زیرساخت‌ها،تضمین آزادی ناوبری در خلیج فارس و…</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/16511" target="_blank">📅 00:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16510">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ادعای العربیه:
عاصم منیر امشب به تهران نمی‌رود</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SBoxxx/16510" target="_blank">📅 00:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16509">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">العربیه:   «توافق میان آمریکا و ایران با میانجیگری پاکستان قطعی شده و این توافق ظرف چند ساعت آینده توسط ترامپ علام خواهد شد.  این پیش‌نویس شامل آتش‌بس جامع و فوری در تمام جبهه‌ها،تعهد متقابل به عدم هدف قرار دادن زیرساخت‌ها،تضمین آزادی ناوبری در خلیج فارس و…</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16509" target="_blank">📅 21:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16508">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">العربیه:
«توافق میان آمریکا و ایران با میانجیگری پاکستان قطعی شده و این توافق ظرف چند ساعت آینده توسط ترامپ علام خواهد شد.
این پیش‌نویس شامل آتش‌بس جامع و فوری در تمام جبهه‌ها،تعهد متقابل به عدم هدف قرار دادن زیرساخت‌ها،تضمین آزادی ناوبری در خلیج فارس و تنگه هرمز و مکانیزم نظارتی مشترک است.تحریم‌ها به تدریج در ازای پایبندی ایران برداشته خواهند شد و مذاکرات درباره مسائل باقی‌مانده ظرف هفت روز آغاز می‌شود!»</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16508" target="_blank">📅 21:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16507">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فیلد مارشال منیر پاکستان امروز به جای فردا به تهران سفر می‌کند. با این حال، به گزارش‌ها، منیر به ایران سفر نخواهد کرد مگر اینکه نشانه‌هایی از پیشرفت واقعی در پیشنهاد فعلی که ایران در حال بررسی آن است، وجود داشته باشد.
گزارش‌هایی منتشر شده که احتمال توافق قابل قبول میان آمریکا و ایران را کاهش می‌دهد. به گزارش i24 News به نقل از منابع آگاه، آمریکا به اسرائیل اطمینان داده که هر توافقی با ایران شامل خروج کامل اورانیوم غنی‌شده از ایران خواهد بود. با این حال، امروز گزارش‌های رویترز به نقل از مقامات ارشد ایرانی حاکی از آن است که رهبر معظم ایران، آیت‌الله مجتبی خامنه‌ای، به تصمیم‌گیرندگان ارشد ایران دستور داده که با توافقی که اجازه خروج اورانیوم نزدیک به درجه تسلیحاتی ایران از کشور را بدهد، موافقت نکنند.
این در حالی است که فیلد مارشال عاصم منیر، تصمیم‌گیرنده اصلی پاکستان، قرار است فردا به ایران سفر کند و دونالد ترامپ، رئیس‌جمهور آمریکا، می‌گوید زمان برای توافق با ایران رو به پایان است</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/16507" target="_blank">📅 19:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16506">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GipT79PhuZpEegoTMFjLhTairw6Hn8gEsVTjIuq7ArwXL4R46JYnzzzWJlTULVE_ivy5RsQ7t9eEawixRyuDBDJD6K4sJx-zXN6obxQTc75nHDkGXV6MACov8JXM2RPhQ3rlqlKq15AGcBJPHEh5O5Ak4F7GN3xBjZod9yvIgMdtM26TiUrjBtpj91htBui3_J3u2i6-Q_k1yv9mp7dKeuwM8Nlv1l784wuaI-BXLPBo-4jkyVBDbt2RANDG68_bXA3HU3LYijHSbXhYIWWmQHeZkBkgjxJj8tMFvkizqXRyAH-t2QpC5uXpZ56K1yptnfC5SXmhHt8laxlE5ZPEiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاتا الکترونیکس و شرکت هلندی ASML در ماه مه ۲۰۲۶ یک تفاهم‌نامه راهبردی امضا کردند که هدف آن پشتیبانی از راه‌اندازی و توسعه نخستین کارخانه تجاری تولید تراشه‌های نیمه‌هادی هند در شهر دولرا ایالت گجرات است.
این پروژه که ارزش آن حدود ۱۱ میلیارد دلار برآورد می‌شود، یکی از مهم‌ترین گام‌های هند برای ورود جدی به عرصه تولید نیمه‌هادی‌ها به شمار می‌رود. بر اساس این توافق، ASML تجهیزات پیشرفته لیتوگرافی، راهکارهای فنی، آموزش نیروی انسانی و پشتیبانی عملیاتی لازم را در اختیار تاتا قرار خواهد داد.
فناوری لیتوگرافی یکی از حیاتی‌ترین مراحل ساخت تراشه است و ASML در این حوزه جایگاهی تقریباً انحصاری در سطح جهان دارد. انتظار می‌رود کارخانه جدید تراشه‌هایی برای صنایع خودروسازی، ارتباطات، هوش مصنوعی، تلفن همراه و کاربردهای صنعتی تولید کند.
با این حال، این تفاهم‌نامه به معنای انتقال فناوری‌های فوق‌محرمانه و پیشرفته‌ترین دانش فنی ASML، از جمله فناوری ساخت تراشه‌های نسل بسیار پیشرفته، نیست و هند نیز در کوتاه‌مدت به رقیبی برای غول‌های تولید تراشه جهان مانند TSMC و سامسونگ تبدیل نخواهد شد.
تمرکز فعلی این پروژه بیشتر بر تولید تراشه‌های مبتنی بر فناوری‌های بالغ و میان‌رده است. با وجود این، همکاری تاتا و ASML از منظر صنعتی و ژئوپلیتیکی اهمیت فراوانی دارد و نشان می‌دهد هند در حال گذار از یک مرکز طراحی و نرم‌افزار به کشوری با توانمندی واقعی در تولید نیمه‌هادی‌ها است؛ هرچند موفقیت نهایی پروژه به توانایی آن در دستیابی به تولید انبوه، بازدهی اقتصادی و سودآوری پایدار بستگی خواهد داشت.
گفتنی است شرکت بزرگ تاتا توسط پارسیان هند بنیانگذاری شده و مدیریت می شود.</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SBoxxx/16506" target="_blank">📅 18:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16505">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اورشلیم پست:   ایران پیش از جنگ اخیر ماهانه ۲۰۰ تا ۳۰۰ موشک بالستیک اضافی تولید می‌کرد و تنها در ۸ ماه حدود نیمی از موشک‌ها و نیمی از پرتابگرهای موشکی از دست رفته خود را جایگزین کرده بود.»</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/16505" target="_blank">📅 15:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16504">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSQVfrnhFzhyIJMTAPLYQndiiYpdtSR6PAO2vVCrtruRkXutChwidZ6oGhpiw0E0ajbtiloprE6tbSF-dbUHLIyiKKHh34yUPoBUn_WXc4AtNhJTT_zMFc0-p061-34QTiMr2yuTAA-zUIQxZ-2wAmHD2lYM0rjTPdgRbWWfwRb-ZwbYwSW5rZioe56qTq0m-TkYKeh0OrvPH2DfmYLuu4IpidRXkLzgyGF9jpgDw7FEqOFbXhDSChQeXc1Cm5KT15Hy44xz3C3c9E7zJkjUBHd4gDPEjCULn74orbDKXgB1FJQB_ws_NJx4yXuaL6HhLLqq4BK83D_1urQ4mjO-iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/16504" target="_blank">📅 15:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16503">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رویترز:
رهبر ایران دستور داده است که اورانیوم با درجه نزدیک به تولید سلاح باید در ایران باقی بماند</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/16503" target="_blank">📅 15:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16502">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3p3fzVwSLKcyVVjI8l0V_XI6nC3LtiJR0FF_r3_0kyQYeB9_lq6-4nyw08uF6TTsMf-pE2kSxbMUSIQmXkXCR_NqEEhcQSXVA0waHoH8gByTFrHuJeoTIqBauzEhVK9S-10UL41kXgZlcHSaV7ZpUZjnbIelQ8zndUkcKEqBLzXgCupRWh_iM48v94aLkPHcqFRTt6EsQh5j49tkDpDs97iuNLNQf70n73sMqSNA3gIycuop2PxofOBgVlU0UfXJXoMWzUfli5Ud0GqITWdLHGQjLra93gkuaaiEo4T4kJbwcwcPWG0Qf3JhGrGxAhiTMRZkovtxHFvPQ3QCHgBfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔷
هوش مصنوعی "بله" همچنان بعنوان جایگزین چت GPT و میرا ، در راستای رفع نیاز کاربران فعالیت می‌کند</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/16502" target="_blank">📅 13:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16501">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4193yRGNzYW9JSJFtYY8fbXiFG76n2D66dRyjFjxVxyVK1jGaSPF2bMMbc5UZCmV6PI99S5UzYdKgkJsKxiVge372Hrz3hPpevgra6hBXVMsGVt5MQ_cyQfntTVc3X28Z9CHPJ40IqlIN6sYMWb1ZHgrhghqwhMsneNik_XR7EFZ6eJG-PlnnyJfHU0jVQs83ItsZsvaqo5PMf8I1ji-c-n_erT0Ifd5yyUZtslODlIKDsz6nZGfWsJZQxINqr_6RuUiK_Kys9qPL5Gx-PlSsW0eOVM3kywKEzgJJnskfPhbpX3n4h7boIq4oA9qcYDIK4yry9qJwVv6U9RLFBzTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ایحاد شکاف طبقاتی دیجیتال در ایران طی ۳ ماه گذشته
🟢
در این مدت سهم کاربران اندروید از ترافیک اینترنت ۲۵٪ افت و کاربران آیفون ۱۸۰٪ رشد داشته است
🔴
آمار فوق نشان دهنده خروج میلیون‌ها کاربر حاضر در طبقات میانی مالی جامعه از فضای آنلاین هستش ، به این معنا که کاربران آیفون بطور معمول از طبقات توانمند جامعه از نظر مالی بوده و امکان خرید کانفیگ با هزینه های هنگفت فعلی را دارند و روشن می مانند اما کاربران اندروید که درصد بیشتری از طبقات میانی مالی جامعه را تشکیل می دهند،  امکان تهییه ابزار دسترسی به اینترنت آزاد را نداشته و خاموش شده اند</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/16501" target="_blank">📅 12:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16500">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🛜
روزنامه الاخبار :  اسرائیل درحال برنامه ریزی برای ترورهای گسترده علیه حزب الله لبنان و جمهوری اسلامی ایران است</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/16500" target="_blank">📅 11:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16499">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خیلی شرط منطقی است، پیشنهاد می شود حتما در شرایط توافق گنجانده بشود</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/16499" target="_blank">📅 11:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16498">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🛜
روزنامه الاخبار
:
اسرائیل درحال برنامه ریزی برای ترورهای گسترده علیه حزب الله لبنان و جمهوری اسلامی ایران است</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SBoxxx/16498" target="_blank">📅 11:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16497">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خیلی شرط منطقی است، پیشنهاد می شود حتما در شرایط توافق گنجانده بشود</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/16497" target="_blank">📅 10:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16496">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🌊
شریعتمداری؛سردبیر روزنامه کیهان:  تا زمانی که ترامپ را ترور نکنیم ، تنگه هرمز باید به روی شناورهای آمریکایی بسته بماند</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16496" target="_blank">📅 10:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16495">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🌊
شریعتمداری؛سردبیر روزنامه کیهان
:
تا زمانی که ترامپ را ترور نکنیم ، تنگه هرمز باید به روی شناورهای آمریکایی بسته بماند</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/16495" target="_blank">📅 10:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16494">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">شرکت SpaceX، کمپانی xAI را تملیک کرد و به این ترتیب ارزش کل برآوردی آن در آستانه عرضه اولیه اش به 1200 میلیارد دلار رسید.</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/16494" target="_blank">📅 09:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16493">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">روایت ترامپ از مقابله ناوهای آمریکایی با پهپادهای ایرانی با بهره گیری از سلاح لیزری!</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/16493" target="_blank">📅 09:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16492">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ریزپهپادهای حزب‌الله   فیلم‌هایی از جنوب لبنان تایید کرده‌اند که حزب‌الله بارها اهداف ارتش اسرائیل، به ویژه تانک‌ها را هدف قرار داده است، در حالی که اسرائیل به عمق بیشتری در سرزمین‌های جنوب رود لیتانی فشار می‌آورد   گزارش‌ها تایید می‌کنند که یک حمله پهپادی…</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/16492" target="_blank">📅 09:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16491">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lb0c8Cr1fJ3A83Fjq1yepvlsLR47Kwh8Gm4W26jMylss_w_4YoNSbAKobyLd8Bw1_AwhhlCvo6uX9D-uzy9H-O8MlKTXKf5S0kNDNQUnJfBxN51U80ZKOTqBv8gVUIULBW0GvDcN8ebBHVI91cri8CqP_thqlHJ5l3u0FlWsF851LphTKUENvhM5OA2mpYV4iDqXqdOvCS4ES4FW1jLAakQwFg8dvx6Nnw20tD1dic7WamYHpxAA8KZVvKjgBvTORIiTYLuusChB-cgJbLUyO0Yl7hClI4xxjjKXMjPMLxRx3eNbO6MhDDsBgnWCWm-O_eAxiIe0h_uijVfZYlsruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طرح جدید سپاه، کل منطقه بین این 2 خط تیره حوزه دریایی تحت کنترل ایران تعریف شده که ملاحظه می کنید بندر کلیدی فجیره نیز درون این حریم قرار گرفته است.  در واقع آمده اند تا خود فجیره این حریم را تعریف کرده اند تا امارات نتواند از این بندر صادرات جایگزین انجام…</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/16491" target="_blank">📅 07:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16490">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiEfEJJ7XyGFrjYnJ8Llz5K37SWe8Z-ajiUKWgkKzxQeaap4vbUjtdSu_ZCV22UwtOaeNxuYwhFj1KDjgwHnUATyQYgLIYKxEaaA3GFtJqFJLiCZ3EA4qo7Ruz7v3yWm7ISE0DMwX7wYoL74npjtH6FxZoDc7RescsLZH6B044znB9AORRflstNbt5LY78NdTWuzGzP9LXO7e6GiArOF7PXhfFfeCbRMkV9DTajS23vfFsJu-yoHzuY92BR6K-PpCDZ-Z0qv84Q_iHJfdOtE-G7_IAokriopgf1pjguraF9SjAevMnjeNSW2WfLlYIHdF_Zxx7ARsy1zUq1LjHR3mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متن کامل گزارش کنگره آمریکا درباره هواگردهای سرنگون شده ارتش این کشور در جنگ با ایران:  بررسی کلی  در ۲۸ فوریه ۲۰۲۶، ایالات متحده آمریکا با هماهنگی اسرائیل، عملیات‌های نظامی علیه ایران را تحت عنوان عملیات خشم حماسی (OEF) آغاز کرد. این درگیری شامل نبردهای هوایی،…</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/16490" target="_blank">📅 07:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16489">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgVCcVC8qdX_YGg2KBh93LgF1yHBRjRLjNae5n4Xj3O4RERm6kaGI3CTz7gVcSZd64lJeDyiLqumWbgCxSgqZaaEwsqCdUuFjoj3n-_6c1apZ26jj-3-sumePOUR3BgJ2LeyWoZqgLwS0nLv8oRLE97Zb6ix6MVsYorGvAL2Br6KW9qRuGuRwaU4d_ft2ZF0wUmZLwSbckOZoT0GBZtzMP3ng9LuIpu1WWISigNOF8jIECYIDaozdrHk-ADcUSPPImavavHfbSfjhSQbumiQXBiJITDOMl58Q_m1Ko4BQ_4QtKOBK7RMpMHV8BaJjw5-QnMDcT3GNlivYiGiXUGoAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران، احتمالاً با کمک روسیه، الگوهای پروازی جنگنده های آمریکا را نقشه‌برداری کرده و خود را در موقعیت بهتری برای استقرار سیستم‌های دفاع هوایی خود قرار داده است.
یک مقام آمریکایی اظهار داشت که نابودی یک جنگنده اف-۱۵ در طول جنگ نشانه‌ای از این بود که الگوهای پروازی آمریکا برای ایران قابل پیش‌بینی‌تر شده‌اند و با طولانی‌تر شدن جنگ، ایران به موفقیت در نابودی هواپیماهای جنگی آمریکا نزدیک‌تر می‌شد.
ممکن است روسیه به ایران کمک کرده باشد تا الگوهای پروازی آمریکا را نقشه‌برداری کند تا تجهیزات نظامی و سیستم‌های دفاع هوایی را با دقت بیشتری مستقر کند.</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SBoxxx/16489" target="_blank">📅 05:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16488">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کانال ۱۴ اسراییل:
نیروهای آمریکایی یک نفتکش ایرانی را در خلیج عمان توقیف کردند .</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SBoxxx/16488" target="_blank">📅 05:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16487">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
کانال ۱۴ اسرائیل
:
باید به یاد داشته باشیم که ترامپ یک تاجر است و اظهارات امروز او با هدف تثبیت قیمت نفت بوده</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/16487" target="_blank">📅 23:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16486">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">توماس ماسی جمهوری‌خواه ضد اسرائیل در انتخابات مقدماتی در برابر نامزد حمایت‌شده توسط ترامپ شکست خورد
توماس ماسی، نماینده جمهوری‌خواه کنتاکی که از سال ۲۰۱۳ در مجلس نمایندگان آمریکا فعالیت می‌کرد، پس از باخت در انتخابات مقدماتی حزب خود به اد گالرین، کنگره را ترک خواهد کرد. ماسی تنها جمهوری‌خواه بود که در پی حمله حماس به اسرائیل در اکتبر ۲۰۲۳، از حمایت از این کشور خودداری کرد و گاهی در رای‌گیری‌های ضد اسرائیل، همراه با دموکرات‌های رادیکال رای می‌داد.
در شب انتخابات، ماسی با کنایه‌ای تیز گفت:
«دیرتر خارج شدم، چون باید حریفم را پیدا می‌کردم تا باخت را اعتراف کنم. و مدتی طول کشید تا اد گالرین را در تل‌آویو پیدا کنم.»
گالرین، که مورد حمایت دونالد ترامپ و کمیته‌های حامی اسرائیل بود، با کسب
۵۵ درصد آراء
پیروز شد.
ائتلاف یهودیان جمهوری‌خواه، که مدت‌ها با ماسی مخالف بود، این پیروزی را به عنوان پیامی واضح از جمهوری‌خواهان کنتاکی دانست:
«در حزب جمهوری‌خواه جایی برای کسانی که پشت به برنامه MAGA می‌کنند، وجود ندارد.»
آنها گالرین را یک میهن‌دوست واقعی توصیف کردند و رفتار ماسی را در طول کمپین انتخاباتی، از جمله تبلیغات ضد سامی‌گری او، محکوم کردند. در یکی از این تبلیغات، که به شدّت مورد انتقاد قرار گرفت، ماسی مدعی شده بود که پیروزی گالرین «دیوانگی بیدار ترنس» را به کنتاکی خواهد آورد و این کار را به درخواست پول سینگر، میلیاردر یهودی حامی جمهوری‌خواهان، انجام می‌دهد. در این تبلیغ، یک ستاره داود رنگین‌کمانی کنار عکس سینگر قرار داده شده بود.
با خروج ماسی، حزب جمهوری‌خواه گامی دیگر در جهت حمایت از اسرائیل برداشت. این انتخابات مقدماتی نشان داد که در حزب جمهوری‌خواه، مواضع ضد اسرائیل دیگر جایگاهی ندارد.</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/16486" target="_blank">📅 23:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16485">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خبرنگار آکصیوص:
ترامپ به نتانیاهو گفت که میانجی‌گران در حال کار بر روی یک نامه نیت هستند که هم ایالات متحده و هم ایران آن را برای پایان دادن رسمی به جنگ امضا خواهند کرد و دوره ۳۰ روزه مذاکرات در مورد مسائل مانند برنامه هسته‌ای ایران و بازگشایی تنگه هرمز را آغاز کنند، یک منبع آمریکایی گفت</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/16485" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16484">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گزارش موسسه مطالعات جنگ از کمک های نظامی و اطلاعاتی روسیه و چین به ایران  روسیه از تلاش‌های ایران برای بازسازی توانمندی‌های نظامی خود در دوره آتش‌بس حمایت می‌کند. نیویورک تایمز به نقل از مقامات آمریکایی گزارش داد که روسیه قطعات پهپاد را از طریق دریای خزر به…</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16484" target="_blank">📅 22:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16483">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ در مورد تعلیق تحریم‌های نفتی برای ایران:
هیچ کاری انجام نمی‌دهم، مگر اینکه توافق‌نامه‌ای امضا شود.</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16483" target="_blank">📅 22:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16482">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ:   نتانیاهو هر کاری من بخواهم انجام می‌دهد</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/16482" target="_blank">📅 20:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16481">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇸
🇮🇱
ترامپ می‌گوید پس از پایان ریاست جمهوری‌اش به اسرائیل خواهد رفت تا برای نخست‌وزیری کاندیدا شود.</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/16481" target="_blank">📅 20:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16480">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ: درگیری‌های بیشتری در راه است مگر اینکه ایران عاقلانه عمل کند.</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/16480" target="_blank">📅 20:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16479">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">#US10Y — H4  فعلاً موفق شده با این سیرک امروزش مقداری نرخ بازده و نفت را همزمان سرکوب کند.   خواهیم دید چه خواهدشد.</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/16479" target="_blank">📅 19:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16478">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O54IuUVEwEDSHRnvw-uDBd6LAB6pg-FiB2XQMwQYncFW1eEyuAwNxCuQjSL0UAfwO3-tJCMnJ0DMHOKd7NfLTNTPxKEMHSmYKyoimT6PhUr3FYAfkYUxG-vmJVdxxy6FsUyqadL7TbLiLGLCnlY901LtQKSmBCdpk1Vv5sd19hmb0bCp9PcTzzQ0sfsJUM9kRrIGKqjFvYGTdxFRfuKQUQWNTExL6p683nlwe8OrOiJ7eN0blj60BeeYYqAtdXxQj30Qx4JtYMvFitUucSIGxwSf0qQGEaro47ARCYb-H2nk1dgEwENbSwhOmLZZ7mVqhvh64OwfG4zDM3cF-xgcgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#URA — D  #سهام_خارجی  این یک فرصت ویژه ایرانیان خارج کشور است. صندوق ETF اورانیوم می تواند در قالب موج 5 خود دستکم 70 درصد رشد داشته باشد که در چارت می بینید.  نظر به مسخره بازی ما در تنگه هرمز، احتمال هجوم سرمایه ها به انرژی های جایگزین بالاست و انرژی هسته…</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/16478" target="_blank">📅 19:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16477">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGMo72XClOGr2JuleU5p0Hmw7ygvjd0WsfGau81YPZn5AiZuUrM7j82xqb1JR2GR205Diz807i7flE9o-lxyhyO84I2eBD-jUeN4tj_gVVyRQK-W4cw9cgaoYmlC94gOM_q3nkyiKfZx3sdCLfatYjNh_A8octhNx0khS663-YU5l8Vz3I_xpedgRsygPIH3KxsAUhN6q86DAKiHb9ewT8wO9b19wTUYTKQ58B5I2f0iV_EDnWrWSFnZtldmM-vCHZJTM8wLpE29jeSHSEubdsPLn_QYnxVd58CTd6MuTOlQWwu3-VBNSnOL8JtEnxOT6zKmmA0n-9SEAx8d1Zg1PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ بازده اوراق قرضه 10-ساله خزانه داری آمریکا سقف مثلث را شکسته و عازم سطوح بالاتر است که فشار سنگینی روی دولت فدرال برای تامین مالی اش وارد می کند.  ترامپ اگر تنگه را باز نکند، بازی اش با نفت میتواند از کنترلش خارج بشود.</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/16477" target="_blank">📅 18:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16476">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❗
⚠️
ترامپ: آمریکا در «مراحل نهایی» مذاکرات با ایران است</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/16476" target="_blank">📅 18:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16475">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
🇮🇱
ترامپ می‌گوید پس از پایان ریاست جمهوری‌اش به اسرائیل خواهد رفت تا برای نخست‌وزیری کاندیدا شود.</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SBoxxx/16475" target="_blank">📅 18:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16474">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔻
ریاست مجلس
:
دشمن از تجاوز مجدد به ما ، پشیمان خواهد شد</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/16474" target="_blank">📅 18:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16473">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⛔️
اخطار قوه قضائیه بابت برخورد با کشت خشخاش</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/16473" target="_blank">📅 12:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16472">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">به خدا قسم این مردک روانی است</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/16472" target="_blank">📅 08:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16471">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtOprlGi2A3oQDjhF2jUkEWgYhpeSyPQ3WkDbZuEI0wOZtlathMRmcG65lhvKz_oDt84o8beqjvKVahDbzB4WDkXewBB1CDs_pxp260bAERYzj8TmeAy0s8gVVBEuiSYAjNf4ylXniwmPm5aod9oxmraErPTkLr-xZAPWASvCQv3CDPK7rvtfjWUUp8vtKyS3-lTnBuM1QS5J45TIJOM2NOIePUibQkr0UsvjWZJxcRprV_VaD_pMygOXvOmboJIYfz3KM8I5qE6T8BrZl4itswxgpZ4MlevVVzDeE5Kj4vgjZPMbrkVMtN9KxGgx-sc5E9WGZ7zJVA9Tb5s2vxjhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگرانی هند از ادامه تسلیح پاکستان توسط چین  پویایی در حال تحول قدرت هوایی بین هند و پاکستان وارد مرحله‌ای بحرانی می‌شود که عمدتاً ناشی از ادغام فناوری پیشرفته موشکی چین توسط پاکستان است.   نگرانی ویژه کنونی هند ، استفاده گسترده از موشک هوا به هوای برد فراتر…</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/16471" target="_blank">📅 07:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16470">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">متن کامل گزارش کنگره آمریکا درباره هواگردهای سرنگون شده ارتش این کشور در جنگ با ایران:  بررسی کلی  در ۲۸ فوریه ۲۰۲۶، ایالات متحده آمریکا با هماهنگی اسرائیل، عملیات‌های نظامی علیه ایران را تحت عنوان عملیات خشم حماسی (OEF) آغاز کرد. این درگیری شامل نبردهای هوایی،…</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16470" target="_blank">📅 01:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16469">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">متن کامل گزارش کنگره آمریکا درباره هواگردهای سرنگون شده ارتش این کشور در جنگ با ایران:
بررسی کلی
در ۲۸ فوریه ۲۰۲۶، ایالات متحده آمریکا با هماهنگی اسرائیل، عملیات‌های نظامی علیه ایران را تحت عنوان عملیات خشم حماسی (OEF) آغاز کرد. این درگیری شامل نبردهای هوایی، دریایی و موشکی در سراسر خاورمیانه بوده است. سرعت فعالیت‌های رزمی در جریان آتش‌بس در آوریل کاهش یافت. در عرض چند هفته، برخی حملات از سر گرفته شدند و شرایط همچنان متغیر است.
وزارت دفاع (DOD، که «از یک نام ثانویه وزارت جنگ» استفاده می‌کند، طبق دستور اجرایی ۱۴۳۴۷ مورخ ۵ سپتامبر ۲۰۲۵) ارزیابی جامعی از تلفات رزمی در عملیات خشم حماسی منتشر نکرده است. در جریان جلسه استماع ۱۲ مه ۲۰۲۶، حسابرس موقت پنتاگون جولز دبلیو. هورست سوم شهادت داد که برآورد هزینه‌های وزارت دفاع برای عملیات نظامی در ایران به ۲۹ میلیارد دلار افزایش یافته است. او گفت: «بخش زیادی از این افزایش ناشی از برآورد دقیق‌تر هزینه‌های تعمیر یا جایگزینی تجهیزات است.»
در اینجا ۴۲ فروند هواپیمای بال ثابت یا بال گرد، از جمله هواپیماهای بدون سرنشین (پهپادها)، که طبق گزارش‌های خبری و بیانیه‌های وزارت دفاع و فرماندهی مرکزی آمریکا (CENTCOM) در عملیات خشم حماسی از دست رفته یا آسیب دیده‌اند، فهرست شده است. تعداد هواپیماهای آسیب دیده یا نابود شده ممکن است به دلیل عوامل متعدد، از جمله طبقه‌بندی، فعالیت رزمی جاری و نسبت‌دهی، قابل بازنگری باشد.
گزارش‌های تلفات و آسیب‌های هواپیماهای عملیات خشم حماسی
چهار فروند جنگنده F-15E استرایک ایگل
در ۲ مارس ۲۰۲۶، فرماندهی مرکزی گزارش داد که سه فروند F-15E بر اثر آتش دوستانه بر فراز کویت سرنگون و نابود شدند؛ هر 6 خدمه هوایی به سلامت بیرون پریدند و نجات یافتند.
در ۵ آوریل ۲۰۲۶، فرماندهی مرکزی گزارش داد که یک فروند F-15E در جریان عملیات رزمی بر فراز ایران سرنگون و نابود شد؛ هر دو خدمه هوایی در عملیات‌های جداگانه جستجو و نجات به سلامت بازیابی شدند.
یک فروند جنگنده F-35A لایتنینگ II
در ۱۹ مارس ۲۰۲۶، یک مقاله خبری گزارش داد که آتش زمینی ایران یک فروند F-35A را در جریان عملیات رزمی بر فراز ایران آسیب زد.
یک فروند هواپیمای تهاجمی زمینی A-10 تاندر بولت II
در کنفرانس خبری ۶ آوریل ۲۰۲۶، ژنرال دن کین، رئیس ستاد مشترک نیروهای هوایی، اعلام کرد که در ۳ آوریل، آتش دشمن به یک فروند A-10 اصابت کرد که پس از آن سقوط کرد و در عملیات جستجو و نجات نابود شد؛ خلبان بیرون پرید و به سلامت نجات یافت.
هفت فروند هواپیمای سوخت‌رسان هوایی KC-135 استراتوتانکر
در ۱۲ مارس ۲۰۲۶، فرماندهی مرکزی گزارش داد که دو فروند KC-135 در حادثه‌ای بر فراز فضای هوایی دوستانه درگیر شدند؛ یک هواپیما در عراق سقوط کرد که منجر به کشته شدن هر شش خدمه هوایی شد. فروند دوم KC-135 در منطقه‌ای نامعلوم که نیروهای آمریکایی مستقر هستند، به صورت اضطراری فرود آمد.
در ۱۴ مارس ۲۰۲۶، یک مقاله خبری گزارش داد که پنج فروند KC-135 در پایگاه هوایی پرنس سلطان در عربستان سعودی در جریان حمله موشکی و پهپادی ایران آسیب دیدند.
یک فروند هواپیمای هشدار و کنترل هوابرد E-3 سنتری (AWACS)
در ۲۸ مارس ۲۰۲۶، یک مقاله خبری گزارش داد که یک فروند E-3 در پایگاه هوایی پرنس سلطان در عربستان سعودی در جریان حمله موشکی و پهپادی ایران مورد اصابت قرار گرفت و آسیب دید. در ۷ مه ۲۰۲۶، یک مقاله خبری گزارش داد که E-3 در یک مسیر تاکسی بدون حفاظت پارک شده بود.
دو فروند هواپیمای عملیات ویژه MC-130J کماندو II
در ۵ آوریل ۲۰۲۶، یک مقاله خبری گزارش داد که دو فروند MC-130J که از عملیات جستجو و نجات برای یک F-15E سرنگون شده حمایت می‌کردند، پس از اینکه قادر به ترک محل نبودند، عمداً در ایران روی زمین نابود شدند؛ همه خدمه هوایی به سلامت تخلیه شدند.
یک فروند بالگرد جستجو و نجات رزمی HH-60W جولی گرین II
در ۶ آوریل ۲۰۲۶، ژنرال کین در یک کنفرانس خبری گفت که در ۵ آوریل، یک فروند HH-60W در جریان حمایت از عملیات جستجو و نجات برای یک F-15E سرنگون شده در ایران، از آتش سلاح‌های سبک آسیب دید.
بیست و چهار فروند هواپیمای بدون سرنشین MQ-9 ریپر با ارتفاع متوسط و مداومت طولانی
در ۹ آوریل ۲۰۲۶، یک مقاله خبری گزارش داد که ارتش آمریکا از آغاز عملیات نظامی علیه ایران، ۲۴ فروند MQ-9 ریپر را از دست داده است.
یک فروند هواپیمای بدون سرنشین MQ-4C تریتون با ارتفاع بالا و مداومت طولانی
در ۱۴ آوریل ۲۰۲۶، یک مقاله خبری با استناد به یک سند نیروی دریایی آمریکا گزارش داد که یک فروند MQ-4C در یک حادثه سقوط کرده است.</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SBoxxx/16469" target="_blank">📅 01:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16468">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcumnP0_n4D5z4OtsRxJ5VJAWQBmzVlGxXTgziK8jkKFUG769Wl50AtEU40iy5ukfm2heeDncKFaNHrSnaw4Dvtl4HgFjnM1OZPtrNbtMs-aPNNFwsd_nxXtvR_stxY0F7ALbmcPux3UIDZ3Q-vNVHYESRk5CBq7v9ihvh-132vghdiKtPvzN4MYRxlRNkrHMK-ciM8LEjnrjMrdC-fiu_z0NtapqlF7Y8FfQrovvx--_sSWQ2TCFfFkDjROO7YAY9ns8K_mW4NKr9yjOPr-syQBaS3HJTp7uZdeg1mL776XnhyIQsfLDWpnYutq3A0cbUPvEFyiGO4eY2z9OvdmQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم با توجه به اینکه این بار نه نفت افت کرد و نه نرخ های بازده خزانه داری و عملاً توییت مثلاً صلح طلبانه ترامپ بی اثر بود، هر لحظه احتمال تهاجم نظامی آمریکا و اسرائیل می رود.</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/16468" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16467">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خداوکیلی مملکت عجیبی داریم!
انفجار روی می‌دهد دلیلش نامشخص !
گردوغبار همه جا را می‌گیرد دلیلش نامشخص!
وزیرخارجه مملکت به نیویورک می‌رود نماینده مجلس خبر ندارد!
سبحان الله !</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/16467" target="_blank">📅 00:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16466">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خبرگزاری مهر ایران: صدای انفجار در جزیره قشم شنیده شد، علت نامشخص است.</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16466" target="_blank">📅 00:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16465">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس:
امیدوارم خبر سفر عراقچی به نیویورک برای مذاکره در خصوص تنگه هرمز دروغ باشد
چرا ما در خصوص موضوع تنگه هرمز باید در خاک دشمن مذاکره کنیم؟</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/16465" target="_blank">📅 23:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16464">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ در حال ساخت یک پناهگاه زیر سالن باله است
او می‌گوید بیمارستان، تأسیسات تحقیقاتی و اتاق‌های جلسه برای ارتش، در حال ساخت زیر سالن باله کاخ سفید هستند.</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/16464" target="_blank">📅 22:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16463">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نیروی دریایی آمریکا یک نفتکش متعلق به شرکت ملی نفت ایران با بیش از یک میلیون بشکه نفت خام  را در اقیانوس هند توقیف کرد.</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/16463" target="_blank">📅 22:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16462">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نیروی دریایی آمریکا یک نفتکش متعلق به شرکت ملی نفت ایران با بیش از یک میلیون بشکه نفت خام  را در اقیانوس هند توقیف کرد.</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16462" target="_blank">📅 22:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16461">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔺
پزشکیان: بیایید اروپایی باشیم
🔹
رئیس‌جمهور: بیایید در مصرف انرژی مثل اروپایی‌ها باشیم. ما الان ۳ برابر اروپا گاز و برق مصرف می‌کنیم.
🔹
اگر بد مصرف کنیم، در تابستان و زمستان مشکل خواهیم داشت و این بدمصرفی به گرانی و بیکاری تبدیل می‌شود.</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/16461" target="_blank">📅 22:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16460">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔺
پزشکیان: بیایید اروپایی باشیم
🔹
رئیس‌جمهور: بیایید در مصرف انرژی مثل اروپایی‌ها باشیم. ما الان ۳ برابر اروپا گاز و برق مصرف می‌کنیم.
🔹
اگر بد مصرف کنیم، در تابستان و زمستان مشکل خواهیم داشت و این بدمصرفی به گرانی و بیکاری تبدیل می‌شود.</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SBoxxx/16460" target="_blank">📅 22:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16459">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ونس به جای ترامپ!   ای کاش ترامپ صفر تا صدِ پروندهٔ مربوط به مذاکره با ایران را به جی.دی ونس معاون خود می‌سپرد و خودش بخصوص از اظهارنظر در این زمینه خودداری می‌کرد! ونس حداقل گویا و آرام و قابل فهم سخن می‌گوید، اما ترامپ با زبان تحریک‌آمیز و شلخته‌اش فقط شرایط…</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/16459" target="_blank">📅 21:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16458">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">معاون رئیس‌جمهور جِی‌دی ونس درباره ایران: من فکر می‌کنم اینجا فرصتی داریم تا رابطه‌ای که بین ایران و ایالات متحده طی ۴۷ سال گذشته وجود داشته را بازتنظیم کنیم.  رئیس‌جمهور از ما خواسته این کار را انجام دهیم و ما هم به تلاش ادامه خواهیم داد، اما این کار دوطرفه…</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16458" target="_blank">📅 21:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16457">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇺🇸
ترامپ می‌گوید جدول زمانی برای ایران ۲-۳ روز است، شاید تا اوایل هفته آینده.</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/16457" target="_blank">📅 21:54 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16456">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">معاون رئیس‌جمهور جِی‌دی ونس درباره ایران: من فکر می‌کنم اینجا فرصتی داریم تا رابطه‌ای که بین ایران و ایالات متحده طی ۴۷ سال گذشته وجود داشته را بازتنظیم کنیم.  رئیس‌جمهور از ما خواسته این کار را انجام دهیم و ما هم به تلاش ادامه خواهیم داد، اما این کار دوطرفه…</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/16456" target="_blank">📅 21:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16455">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">معاون رئیس‌جمهور جِی‌دی ونس درباره ایران:
من فکر می‌کنم اینجا فرصتی داریم تا رابطه‌ای که بین ایران و ایالات متحده طی ۴۷ سال گذشته وجود داشته را بازتنظیم کنیم.
رئیس‌جمهور از ما خواسته این کار را انجام دهیم و ما هم به تلاش ادامه خواهیم داد، اما این کار دوطرفه است. ما توافقی نخواهیم داشت که به ایرانی‌ها اجازه دهد سلاح هسته‌ای داشته باشند.
پس، همانطور که رئیس‌جمهور همین الان به من گفت، ما آماده و مسلح هستیم. ما نمی‌خواهیم به آن مسیر برویم، اما رئیس‌جمهور آماده و قادر است اگر لازم باشد به آن مسیر برود.</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/16455" target="_blank">📅 21:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16454">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SBoxxx/16454" target="_blank">📅 20:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16453">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمو | مطالعات تخصصی آسیای مرکزی</strong></div>
<div class="tg-text">🔘
اقدام نمادین دولت تاجیکستان در انتقال خاک مزار «قهرمانان تاجیک»
⬅️
با پیگیری
دولت تاجیکستان
بخشی خاک از مزار «قهرمانان تاجیک» که عموما چهره های نخبه و بنیانگذاران تاجیکستان مدرن در دوره شوروی بودند در اقدامی نمادین به این کشور منتقل شد. از جمله این افراد شیرین شاه شاه تیمور، نصرت‌الله مخصوم و نثار محمد از بنیانگذاران تاجیکستان بودند.
🔹
صبح روز ۱۹ مه، امامعلی رحمان، رئیس جمهور تاجیکستان، با ادای احترام به یاد و خاطره آنها، جعبه‌های حاوی خاک مزار این چهره‌های برجسته تاریخ معاصر تاجیکستان را دریافت کرد.
🔹
نماز میت این چهره‌ها در مسجد جامع مرکزی دوشنبه به نام امام اعظم برگزار شد که در آن رستم امامعلی، شهردار دوشنبه، شرکت کرد. پس از آن، خاک نمادین در گورستان لوچوب به خاک سپرده شد.
🔹
شیرین شاه تیمور، نصرت‌الله مخسوم و نثار محمد در سال ۱۹۳۷ در جریان سرکوب‌های استالینیستی به اتهامات سیاسی در مسکو اعدام شدند. آنها در گورهای دسته جمعی در نزدیکی مسکو دفن شدند. پس از مرگ استالین، در دهه‌های ۱۹۵۰ و ۱۹۶۰ پرونده‌های این چهره‌ها بررسی و از آنها اعاده حیثیت کامل شد.
آمو | مطالعات تخصصی آسیای مرکزی
@C5_Amu</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SBoxxx/16453" target="_blank">📅 20:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16452">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">به نظرم با توجه به اینکه این بار نه نفت افت کرد و نه نرخ های بازده خزانه داری و عملاً توییت مثلاً صلح طلبانه ترامپ بی اثر بود، هر لحظه احتمال تهاجم نظامی آمریکا و اسرائیل می رود.</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/16452" target="_blank">📅 20:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16451">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔻
غریب آبادی ؛ معاون حقوقی وزارت امور خارجه دولت :  برای ما تسلیم شدن معنایی ندارد ، یا پیروز میشویم یا شهید</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SBoxxx/16451" target="_blank">📅 20:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16450">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqj12shx53Mjqr6KC5CPj0KcN7cjtZfb4aCuX1AUJj2SAidBNjLt18Pw1iH45WZNPEdGGvRB-i9VTB1Mxa6SkaM0FTVAS0lhBREh7IBiabpPt9L8mjADyK0F_XkA2aGEUANBoiT2yTHHEWygd4BKSCPwwloH4ZFTC6mUvQdUR0WEzIiZFvAuV1HGutuIR625fldL5nfrlhAPbsX9_novdC2sLluTUP1K-H8WoZd-roxrWhy6Ze8tulubcshrwtL90Lhr2PoRhFIwB_rTaAXPSOPcUNSyIZ6NpV_-AIr81FFeXDlSHbNOxxUa4P2IsgcaLHleEMhki_FMzuD4dG4x5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
غریب آبادی ؛ معاون حقوقی وزارت امور خارجه دولت
:
برای ما تسلیم شدن معنایی ندارد ، یا پیروز میشویم یا شهید</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/16450" target="_blank">📅 19:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16449">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBfFQzZsmpSHl-AvNWymF1e385aNZfT968NIJ3QhibLJL26oJSq5PkT6U1aWdJMKCYJkqphOXx57htxRXOItp6cX24OMwuszWm5iK5B7TfofMYjvD2kBPvmetM5o6ipzNXNFCGtvdFjRgI0EmqgqEPf0Buu2SGsueD5eLyIMbZIt69IbzIssY0KaCvPLWW-e90ROX8rFN1Wgqn1-RskyNXUKO1isLfJRkEtdTorEsPUdMbEpItfHq_f7sWvle-lREK4WHHyCT1iwt-ftdM8XEH9q5QFALAl5PDdlhzFmSVTI66UTEx6EA3PvaiHwYfKymJ8-0_NLjUNoAjtRBHTf5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه اسراییل بزرگ روی بازوی برخی نیروهای نظامی این کشور  با این تیمی که ترامپ چیده بعید نیست به این سمت حرکت کنند. بیخود نیست وزیر دفاع ترکیه هم نگران شده است.  برخی اطرافیان ترامپ رسما باور ایدئولوژیک به اسراییل بزرگ دارند.</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SBoxxx/16449" target="_blank">📅 15:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16448">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اینقدر که ما نگران خطای محاسباتی آنها هستیم خودشان نیستند.</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SBoxxx/16448" target="_blank">📅 15:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16447">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اینقدر که ما نگران خطای محاسباتی آنها هستیم خودشان نیستند.</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SBoxxx/16447" target="_blank">📅 15:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16446">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پدرسگ های کافر هر 5 ماه یک بار دچار خطای محاسباتی می شوند حرامزاده ها</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SBoxxx/16446" target="_blank">📅 15:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16445">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فوری | فرمانده نیروی زمینی ارتش ایران: دشمنان نباید در محاسبات خود در مورد توانایی‌های نیروهای ما اشتباه کنند.</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/16445" target="_blank">📅 15:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16444">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⭕️
معاون امنیتی خوزستان
:
امروز  براثر تست پدافند و برخورد پرتابه های آن به یک منزل مسکونی ، متاسفانه ۴ نفر از شهروندان عزیزمان مجروح شدند</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/16444" target="_blank">📅 15:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16443">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">هاکان فیدان:   اورانیوم غنی شده ایران باید خارج شود یا به صورت سه‌ونیم درصدی تغییر داده شود</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/16443" target="_blank">📅 14:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16441">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">هاکان فیدان:
اورانیوم غنی شده ایران باید خارج شود یا به صورت سه‌ونیم درصدی تغییر داده شود</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/16441" target="_blank">📅 14:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16440">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خبرگزاری تسنیم:   فعال شدن توپهای ضدهوایی در جزیره قشم به دلیل پرواز پهپادهای کوچک در حریم هوایی این جزیره بوده است.</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/16440" target="_blank">📅 14:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16439">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">در بازگشایی باشکوه بورص، این نمادها کماکان بسته خواهندماند:  #مبین • #نوری • #پارس • #آریا • #جم • #جم‌پیلن • #شپدیس • #زاگرس • #بفجر • #مارون • #شکبیر • #شگویا • #اروند • #بوعلی • #شفن • #شغدیر • #شجم • #شفارا • #شیراز • #شاوان • #فخوز • #فاهواز • #فولاد…</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16439" target="_blank">📅 14:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16438">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMjva1-WgIflH4X3V3K0uwscT7h8RiGK-Dx-qO1-dYYDrzCxeQavjysQsgsE8uz2bkUiKeDqKslxGGJYfVBM2XblWBkwDqWBlOFDaT8LCiedPqWBrPUYtWOn-t_63kz5E-WW_WpFuDZ8xv4Ot3_gpz55NW9NO6_qi8bSBm5AoqExYrImDAZNFraRwoWYlUX4BcoGi2EXn43Sd-KhRrd6IRhNIJTdOLfc5XdYYzwLj6oysNuzN6HK4qkLJtrxzsBUL49ikGBgh3Gc9nMp4ehb3K1bC8-OjzC3xnTdcpvoOdRwfQfK5jdrEVDkMtErJURhI2lRy5KlgNLE7I6yp_bdaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشورهای دارای بیشترین نرخ زادورود!
هند زیبا در صدر!</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/16438" target="_blank">📅 10:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16437">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">چرا میخند؟!</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SBoxxx/16437" target="_blank">📅 10:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16436">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکاخ رسانه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe204bf88.mp4?token=eCoPETFs1z7rcr8PH3ghI-aRejl7FP0wS2lxPnWWGczYzKqWlZYfDwP9XjPM8e7lQ-eVfnLpD6t5O4miQ_R-mtypEZ15ATYu-J4LDZU_VzvMMgjzzbn46GcCg3ISNNp6vhcOhqXkLV_nJV-pjaQ3qdzTdGnnY2fEw6t7T9TgrDSaBypTmSAnVjXXPeanuqJPeu7xoWLh95qbTb0Q2RJvtZ-Jks5BZ_DpVSwC45gsSeIImas1wSko96R_zW21og-DLcYhTd7Q_aLB71lvKFy_0lW8-IWunoICoyAclOcYxLgQnvuiEWJ0ODVu2ZVby22QdkALNp1XH08G3mCIZN1_nAAMMJSkmMSnpJcKmf9eOijTKAWE162UNL383xU3Bhc_wDWz1RSg8GY-RlaaZStwN4upPKSYeHjFKg37fNJbr95n3My3S-PfA6Fk8RxRDpgiU2mNCccxuUbJ4Eh2C1auzff6hgSr5ElVB0QuZMHzLg6Xn4gWUP4L6dmxTwohegmAkpesHW0_ZWhu6rq5f-5DNkS_w22D_rdwD1FZZu83U-6wbfWU7pB7BvoNqSzR9I6gpl8GrfGV7PnYBwJr5aQi-k7o-QWpt3bKeOzd5U-yruyhAD8pgHXbr2LskqEDhy7ZUGkzADXcaWjH6-GJ_So1sBHFT_ooiDKTwj3DjX2--ko" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe204bf88.mp4?token=eCoPETFs1z7rcr8PH3ghI-aRejl7FP0wS2lxPnWWGczYzKqWlZYfDwP9XjPM8e7lQ-eVfnLpD6t5O4miQ_R-mtypEZ15ATYu-J4LDZU_VzvMMgjzzbn46GcCg3ISNNp6vhcOhqXkLV_nJV-pjaQ3qdzTdGnnY2fEw6t7T9TgrDSaBypTmSAnVjXXPeanuqJPeu7xoWLh95qbTb0Q2RJvtZ-Jks5BZ_DpVSwC45gsSeIImas1wSko96R_zW21og-DLcYhTd7Q_aLB71lvKFy_0lW8-IWunoICoyAclOcYxLgQnvuiEWJ0ODVu2ZVby22QdkALNp1XH08G3mCIZN1_nAAMMJSkmMSnpJcKmf9eOijTKAWE162UNL383xU3Bhc_wDWz1RSg8GY-RlaaZStwN4upPKSYeHjFKg37fNJbr95n3My3S-PfA6Fk8RxRDpgiU2mNCccxuUbJ4Eh2C1auzff6hgSr5ElVB0QuZMHzLg6Xn4gWUP4L6dmxTwohegmAkpesHW0_ZWhu6rq5f-5DNkS_w22D_rdwD1FZZu83U-6wbfWU7pB7BvoNqSzR9I6gpl8GrfGV7PnYBwJr5aQi-k7o-QWpt3bKeOzd5U-yruyhAD8pgHXbr2LskqEDhy7ZUGkzADXcaWjH6-GJ_So1sBHFT_ooiDKTwj3DjX2--ko" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داماد شهید رئیسی: شهید رئیسی اثبات کارآمدی نظام ولایی را رسالت خود می‌دانست
صادق توسلی، داماد شهید رئیسی:
🔹
جوهر اصلی شخصیت شهید آیت‌الله رئیسی را می‌توان در دو واژه «تعبد» و «ولایت‌مداری» خلاصه کرد.
🔹
آنچه در سلوک ایشان به وضوح لمس می‌شد، احساس رسالت عمیق برای اثبات کارآمدی و موفقیت «الگوی نظام ولایی» در هر جایگاه و مسئولیتی بود.
🔹
تمام اهتمام و مجاهدت ایشان بر این اصل استوار بود که مردم برکاتِ ملموس این نسخه یگانه و نجات‌بخش را در زندگی خود احساس کنند.
🔹
رابطه عمیق، عاطفی و سرشار از محبت میان ایشان و امام شهید، صرفاً یک دلبستگی فردی یا عاطفه شخصی نبود؛ بلکه ریشه در یک پیوند تشکیلاتی و ولایی داشت.
🔹
این ارتباط ساختاری با ولی‌فقیه به عنوان عمود خیمه نظام، با این هدف تعریف شده بود که خروجی کارآمدیِ حاکمیت دینی را در عرصه اجرایی به ثمر بنشاند و حقانیت این الگو را در عمل پایدار سازد.
@kakhresaneh</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16436" target="_blank">📅 10:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16435">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">معاون وزیر امور خارجه ایران:   رفع تحریم‌ها، آزادسازی منابع مسدود شده و پایان دادن به محاصره در پیشنهاد اخیر ایران به آمریکا گنجانده شده است   پایان جنگ در همه جبهه‌ها، از جمله لبنان، و خروج نیروها از مناطق نزدیک به ایران نیز در این پیشنهاد گنجانده شده است</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SBoxxx/16435" target="_blank">📅 09:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16434">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">معاون وزیر امور خارجه ایران:
رفع تحریم‌ها، آزادسازی منابع مسدود شده و پایان دادن به محاصره در پیشنهاد اخیر ایران به آمریکا گنجانده شده است
پایان جنگ در همه جبهه‌ها، از جمله لبنان، و خروج نیروها از مناطق نزدیک به ایران نیز در این پیشنهاد گنجانده شده است</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/16434" target="_blank">📅 09:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16433">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vM5xKnZ58u8PrAvAJqDkZnUBpPT5B8sEBcOnUi7xKt_qNFWUyg0IeZ4JJR-W-tUlHss1XZKe0imvQSPcYs3sYZoO6P7gYbx0gOvwZPjgzqRunN2F5q70r5zLOkBoizm7rpDncVThIWasVEspUDZJKKZph0p_UXRKGA3WByTYQZXZYS6olCX6g-7YXywz4-N-xaLqRO6pEj-ul9P0LHBfTuxMa5p_wUUQ7Ky3yZlfA3K95phPjpycTurQPWRQ4j7a_dKcZtXWmc_1s-gPK0baj3Phdihid5Dv1_bAw45WZO-0WL-V2xenT2R3_-y3tK9zIvE7XlUtZFMZk5qX5I7KuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ نیابتی آمریکا با بلوک چین در شاخ آفریقا هم نمود پیدا کرده و دیشب نتانیاهو اعلام کرد که اسراییل، استقلال سومالیلند را از سومالی به رسمیت میشناسد.  جالب است بدانید که سومالیلند از ۱۹۹۱ دارای دولت و ساختارهای حکومتی خودش است و اتفاقا از دید قوام نهادهای مدنی…</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/16433" target="_blank">📅 05:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16432">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خبرنگار:
«آیا گزارش‌هایی را شنیده‌اید که می‌گوید ایران دیگر درباره تعهدات هسته‌ای صحبت نمی‌کند؟»
ترامپ:
«چه سوال احمقانه‌ای. من چیزی نمی‌شنوم، ما در حال حاضر در حال مذاکره هستیم، تو چه آدم احمقی هستی. من در این مورد با تو صحبت نخواهم کرد.»</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/16432" target="_blank">📅 05:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16431">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khGjg9XW2gBOTlRh1IQe1QFPJGWVwWyHGVa1H6pfWkTI9-uA7mRppRjBh7ECnoLfi81YzU8IVDeKOH07c2vPZOsUG36kOV68kUbmizYTeRvm1-JIIh6AAgY6xG7Ii2rhaevTU9wieUTzgZlpCOjEoGFukgU17TU4LdBiWy08XzG9AUW0rEetxMvOSPRDFONdCgC8ZBM8XwJJC-RPfsrgxXV96Y5qWgmNN-ml9G9oyKfA-VJJ3mzDa1B0QihOm2QaIv6Nqsjxzdc-eqw4clu2fVhjcLqEQypQdSS98ffnr0TP-Oyd6B5iLcRJxQOlzjvCwLSEjxEQnTAH-UGCxrBn6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب گویا شماری از مجریان صداوسیما فاز امام جمعه بودن برداشته و با سلاح در برنامه شان حاضر شدند!  سبحان الله !</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SBoxxx/16431" target="_blank">📅 00:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16430">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تقریباً ۹۰٪ از کشورها اکنون شاهد روند افزایش بازده‌ها هستند و نرخ جهانی ۱۰ ساله به بالاترین حد پس از سال ۲۰۰۸ رسیده است.</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/16430" target="_blank">📅 23:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16429">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">زیرنویس شبکه خبر!</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SBoxxx/16429" target="_blank">📅 23:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16428">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFDdQjnyXQDDQEwhrX0gEDiLggueNHkfwPCHOUe9QSmvNyCjuMSKMvI_XnLAOGhQKlqKmBgAbTICJA0sUXFkQAEATdE_w9_A2Nwx6Lp2z96h5i7wWyGe6n9Gjax9lTm2yNxdTtcj-9KQecIxg_Fff-0wDfGisRBiQfuPlDEZyQ7kwLRqgmcLY3u2YdxnMknYnXZoMwLGeLxaghNn9TKs4CxW-kkt9JWn1UpFsP4KTECHRHFllXfba-gdnle78GTXCm5gkpW3Pd5YDaM9-iZkWQNHG5iydw0nBHidU7CKAsDnNDwQMf0cu7hDopo7PvVnjnhN2uiPGopgkbjjJeT6Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس شبکه خبر!</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SBoxxx/16428" target="_blank">📅 23:24 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
