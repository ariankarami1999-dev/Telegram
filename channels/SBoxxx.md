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
<img src="https://cdn4.telesco.pe/file/W7lqK-nuAywqh4d4N0AJm6bqCbfGnu95WsMpqoQQiIuz7Pb_tEJ167xfExJAkpfwUocC0mp2BYtZA4CIY7ZfJVe46IpX-o8KhXuxpFwYTHnDOxlj-WyrDuBjL1YOrsGbmy_QeKWlqIXOhUf8swOQzMYtjxii2atVKdXHfx-Txb-xz4_6Fe5cG887CS0-0agXCpr3j0NI49eucJduew4-w1DM6c_iVdpfal5IEYFx1PSNzF8cIEShKv86yo9w-vV8VxolzXDUDa5JH3gDhcooWK8_nAWGiX-DjeAim0Coit9hd4ZH3M7fmzBb1V--Hd-r5N8yMnsQFz1cixPtTe56gQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.9K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 06:11:45</div>
<hr>

<div class="tg-post" id="msg-21217">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سفیر ایالات متحده در چین، گفت که رئیس‌جمهور ترامپ در مذاکرات خود در کاخ سفید، از رئیس‌جمهور چین، شی جین‌پینگ، خواسته است تا هرگونه کمک چین به ایران را متوقف کند.
او اظهار داشت که واشنگتن به وضوح اعلام کرده است که «هرگونه کمکی که چین به ایران ارائه می‌دهد، کاملاً غیرقابل قبول است».
او افزود: «ما از قبل حرکتی در این زمینه مشاهده کرده‌ایم. این همان تعهدی است که داده شده است. آن‌ها به ما اطمینان دادند که چنین کاری انجام نمی‌دهند.»</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SBoxxx/21217" target="_blank">📅 02:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21216">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فیلم کامل مستند BBC درباره نسل کشی ترکیه ضد کردها در عراق</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/21216" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21215">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ada5e22fc.mp4?token=i1DwLWc9WO_VL88g4gDb9PQw_XU4hmpfyeppgedqh1ofkBytjlxXg1V4IiC7VBZ6mpJgg_ngUC3JnV07HBBA2DX4AQsIYGGqHEHOPplcuZMjnOCxR4FsjNAr2M46Hf2xO-GGw4a4dIiq-d328XgT74cCw9gBgbz8RxlVvKFMOSFWB1T-Y6j4-LKN650z2-PqO1i7Vh6zfV7sj-4F0nqg_bzOSnpkHON0qnuEk6jt0uxVvVvVb8sNIUROD-Po2dyIC6rB2Q71AHoFx79JV_KLCn57DdWVZF33N5p--U7vnk0-5-eczquQpHTINvR0HVqj2Eyw6-5en9bI7QxKTGS1mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ada5e22fc.mp4?token=i1DwLWc9WO_VL88g4gDb9PQw_XU4hmpfyeppgedqh1ofkBytjlxXg1V4IiC7VBZ6mpJgg_ngUC3JnV07HBBA2DX4AQsIYGGqHEHOPplcuZMjnOCxR4FsjNAr2M46Hf2xO-GGw4a4dIiq-d328XgT74cCw9gBgbz8RxlVvKFMOSFWB1T-Y6j4-LKN650z2-PqO1i7Vh6zfV7sj-4F0nqg_bzOSnpkHON0qnuEk6jt0uxVvVvVb8sNIUROD-Po2dyIC6rB2Q71AHoFx79JV_KLCn57DdWVZF33N5p--U7vnk0-5-eczquQpHTINvR0HVqj2Eyw6-5en9bI7QxKTGS1mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثرات خانمانسوز جهش دلار روی مغز مردان سرزمینم!
گفته می شود ایشان قبلاً پرایس اکشن کار بوده که بعد از 36 بار کال کردن اکنون وارد مباحث تشکیل سبد و تخمگذاری در آن شده است و گرنه این حجم از آشنایی و تسلط بر مفاهیم بازاری نمیتواند از دهان یک اسکل معمولی بیرون بیاید!</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/21215" target="_blank">📅 23:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21214">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">علی عبدی برنامه آمریکا و اسرائیل برای جنگ بعدی علیه ایران را نفوذ آبی و خاکی و هلی برن از سمت خلیج فارس، غرب(عراق)، جمهوری باکو، آسیای مرکزی و جنوب شرق (پاکستان) دانست و تصریح کرد حملات هوایی، تلاش برای شکار شاه مهره و استفاده از بمب اتمی تاکتیکال نیز رخ خواهد…</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SBoxxx/21214" target="_blank">📅 23:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21213">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">— تًن ماهی — گوشگیر سیلیکونی — آب معدنی — چسب زدن شیشه ها</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/21213" target="_blank">📅 23:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21212">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">علی عبدی برنامه آمریکا و اسرائیل برای جنگ بعدی علیه ایران را نفوذ آبی و خاکی و هلی برن از سمت خلیج فارس، غرب(عراق)، جمهوری باکو، آسیای مرکزی و جنوب شرق (پاکستان) دانست و تصریح کرد حملات هوایی، تلاش برای شکار شاه مهره و استفاده از بمب اتمی تاکتیکال نیز رخ خواهد داد، ولی پیروزی از آن ملت ایران خواهد بود.</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/21212" target="_blank">📅 23:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21211">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">به پزشکیان رای دادیم که جنگ نشود، هر هفته 15 بار جنگ می شود!</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/21211" target="_blank">📅 23:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21210">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">به پزشکیان رای دادیم که جنگ نشود، هر هفته 15 بار جنگ می شود!</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SBoxxx/21210" target="_blank">📅 23:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21209">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خداوکیلی راست می گوید ؛ این بار دیگر غافلگیر نشویم!</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SBoxxx/21209" target="_blank">📅 23:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21208">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGOXEApH-eFRoq8WqrKsBEtfRgjX39CLw57sUfUQuxtqx6Jv9aEZwRGOxB9aS1CKOh7o_GUZGD-eJZik_agHoOd-_FsXpyWqmF5GiXBE98T35cEGNYRFveyAeQtwKwMrckKEHbqy2SBOmLH-h3zCcS7VGOD7KZF7Ki5FtSoH628CY4xaQpajME8zRzq114Z9gsC02pcakM0aZA-s6e_LZAhQTyHsG9jiV3ybBnOIAhOGXkbYRhHN4Kgzw26rJ0NaRKsyjH5kSWfrQLe2apF9Njm0-gCj3Pin71I2KMkhAHxdvR3zjjR6fYiOb0eDSYaHUSkixoz6t98TZwXSmcHCHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من شخصاً هیچ وقت به نزدیک بودن توافق ایران و آمریکا توجه نمی کنم ولی اعتقاد دارم نزدیکی ایران و آمریکا نزدیک است.</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SBoxxx/21208" target="_blank">📅 23:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21207">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">چرا می خند؟!</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SBoxxx/21207" target="_blank">📅 22:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21206">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nE04ZMY-MnSqqRuoPIDNtIAEfcUYt-gqbDhLzoDdWKkPIv5DHbd4tFxpHMNUW79AU2pKJTYWRMhuV-FbpnHFE7WNaqb4JHBW8CtPo4a1Z8G03TgVwEhaEDFJyHImz1jf8ymifTsL59BsvBWSw7ver91LV6oCIgP0Ae_4bUm8h_Lxv8acX59I-pE3p4l3wGhFDBhRsfGUPoxibFORbQngs51EMDBMHw3F6z14vUTUgQj5sYoJ4ra7CCxgjcN1Nt-U47NppACyFyd9XKuWA2r7BOIS7pQy0-1yM1ZNgcPl4k4Ssqf1xkjzMHfDiqJwXSo6t-Ix9osDX0vVppBGFQzaug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">First Time ?</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SBoxxx/21206" target="_blank">📅 22:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21205">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مرندی ذوالاکتاف:
هیچ پیشرفتی در مذاکرات غیرمستقیم با رژیم ترامپ حاصل نشده است. منطقه به سوی تشدید تنش پیش می‌رود، چرا که دیکتاتوری‌های حوزه خلیج فارس که در جنگ علیه ایران همدست بوده‌اند، به توطئه ترامپ و بسنت علیه ملت ایران می‌پیوندند.</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SBoxxx/21205" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21204">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrgmaO2sJwXtIBAUbNAcSN9u4ZIUfs7h3hzQXx6ONNApxG6f364axiUhjw4eC2Y0ZQIIjzI5c0l5a90YEe_GpsI5dtQ1qtQM6K9XRcTE2AOxMOUlTj7LJ5E9VE04UaKVLIVoLJPk9o-JFtTuZeXjTE-GZuvHmxAH6cdiGuZ3uhISjZBTTcTihvYY5PHHR0mhrfOutmjzLKMDxd6jaea7gkxWKj0onIbJwFX9gJdU6jGnd6Hl4_-0aFWyNkDh-QIYB0V2VSMPn-QIDqKYDhHgmbBsfCAHXPlhhBm-ioztL_MPJM3jtK0nJxs9YB21FwbnOjMymLriqR2VX8NqtA3roA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محدوده 4255 بسیار مهم است.</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SBoxxx/21204" target="_blank">📅 22:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21203">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUwkton5uYATM2yl70Zeui_ntMvk89GFoiy0Gt4twVADa6BakFGgkYkQMy9anT_r8l-0pXcuXZuclIemNLoWDIsmbSwH5CM6WV4SO9OnNuf9AGWXz23xxF5RSHyPhjKKt3bp5cMIrEMCIMq4aNqZNJuTXAZBH85V97JAg7HtAQ6gLAF5f4pUXTW_KlSVW99bg2qgsg6xEXgg8V2MD0Ks33y3QK3lOQtw5exg3nKTdnvqq9Jk66y1jnDn7l64j5Mw8Ewl1BnQsMQtxyMABuFbYWCUxvQpGqh1hQHoS5kfkJLUvzVeBGeNnMUonEHlWrbJpYEwwA9rhH0_AyXgBCcy2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقتا خواهرمیانه جای مبتدی ها نیست!
از ۶ ماه پیش بلایی نبوده که جمهوری اسلامی و نیروهای نیابتی اش سر این سعودی های فلک زده نیاورده باشند؛ بعد این هفته جشن باشکوهی به مناسب ۹۶-امین سالگرد تاسیس کشور سعودی در قلب تهران برگزار شده!
سبحان الله!</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/21203" target="_blank">📅 21:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21202">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">Ali SharifAzadeh – انتخابات اسرائیل</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/21202" target="_blank">📅 21:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21201">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ
:
در نوامبر در چین دوباره با شی ملاقات خواهیم کرد</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/21201" target="_blank">📅 20:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21200">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">First Time ?</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/21200" target="_blank">📅 20:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21199">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏ قائم‌پناه:
به عربستانی‌ها گفتم انشاءالله برد موشک‌های ما به آمریکا برسد تا دیگر به پایگاه‌ آمریکا در کشور شما حمله نکنیم بلکه به خود کاخ سفید موشک بزنیم.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/21199" target="_blank">📅 20:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21198">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سفیر آمریکا در چین:
پکن در پی هشدار ترامپ، بخشی از حمایت‌ها از تهران را متوقف کرده است</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/21198" target="_blank">📅 19:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21197">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">میانگین 200 پیپ</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/21197" target="_blank">📅 18:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21196">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">#FairValueCurve  نمایه FVC در حال نزدیک شدن به کف محدوده بیش—فروش است.  در این شرایط پرتناقض، بهترین استراتژی فروش در مقاومتهای نزدیک (4292 و 4308) با تارگت 4235 می باشد.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/21196" target="_blank">📅 16:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21195">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رئیس اسبق سیا:   امکان تصرف خارک برای آمریکا وجود ندارد</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/21195" target="_blank">📅 16:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21194">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کارشناس صداوسیما:   در صورت اشغال جزیره خارک توسط آمریکا، خاک بحرین را پس می‌گیربم</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/21194" target="_blank">📅 16:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21193">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
عربستان سعودی ارسال نفت به اروپا را لغو کرد!</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/21193" target="_blank">📅 16:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21192">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بی حجاب ها بیایند توی تجمعات شبانه بعد که تمام شد لطفا خودشان خودکشی کنند</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/21192" target="_blank">📅 16:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21191">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بی حجاب ها بیایند توی تجمعات شبانه بعد که تمام شد لطفا خودشان خودکشی کنند</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/21191" target="_blank">📅 14:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21190">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بی حجاب ها بیایند توی تجمعات شبانه بعد که تمام شد لطفا خودشان خودکشی کنند</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/21190" target="_blank">📅 14:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21189">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خاتمی، امام جمعه تهران:   کسانی که حجاب را رعایت نمی‌کنند نیز شهروند این ملت هستند و حضور آنها در تجمعات و همراهی با مردم کار خوبی است، اما دهن‌کجی به حجاب، خلاف وحدت است</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21189" target="_blank">📅 14:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21188">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مخبر، مشاور رهبر انقلاب:
پرواز در منطقه یا برای همه آزاد است یا برای هیچ‌کس
اگر ایران امکان پرواز و دریافت خدمات فرودگاهی نداشته باشد هیچ کشوری در منطقه هم این امکان را نخواهد داشت.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/21188" target="_blank">📅 14:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21187">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خاتمی، امام جمعه تهران:   کسانی که حجاب را رعایت نمی‌کنند نیز شهروند این ملت هستند و حضور آنها در تجمعات و همراهی با مردم کار خوبی است، اما دهن‌کجی به حجاب، خلاف وحدت است</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21187" target="_blank">📅 14:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21186">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خاتمی، امام جمعه تهران:
کسانی که حجاب را رعایت نمی‌کنند نیز شهروند این ملت هستند و حضور آنها در تجمعات و همراهی با مردم کار خوبی است، اما دهن‌کجی به حجاب، خلاف وحدت است</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/21186" target="_blank">📅 14:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21185">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hr5I5WeE8M7wHcpZjD0uqfuLv2Z027oi7N6gGmwXbhReGRQVjMIb7wnoflEH3pykEMMJBXfkOEaNVsFvN4zr8GYo23fcNtwimBeglYE9RzX-X4xz5zPCFV4MbvahGoMlBM1qtBomOAXr_BmaOItPnHLND8hXWa-DEzbszjTsQm5Tz9cHq5IaQPs7EV_r4nT7OtdlvfJIQsO6a-zNHLYCPV-hiVCjqETB6s-T0BiJfzwpKatyvfZYXyu5LZqCaJRfQUfinpaF28DrtXXyS-ELap4Bk_Hg7_4vumhKPOy47iMNWhM-vbeJ2OCKcjUwECFTff1Awu7ktYuAahJiVA5ghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در حال نزدیک شدن به کف محدوده بیش—فروش است.
در این شرایط پرتناقض، بهترین استراتژی فروش در مقاومتهای نزدیک (4292 و 4308) با تارگت 4235 می باشد.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21185" target="_blank">📅 11:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21184">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyNPRQ1MGfmZJKtihnyI7nSL0aDhHLUknVUbwQPhplyD15OZ6JHjswSB8KAoPh0UYlR3rd9dc5TgdHTi--Lw4rLIHe13s4B_MMYpW6F5nWG1W5_kTZJ7i_ao71DWPuwo6ZKJdWpTRncSKT83TU6TEP_YDRFrYDAuekt6l36VoKd-xBT1zqzgclE6576zdyGQWGCCaSq9wVPsfL4rpVEhPiV_gJ1a3GRSDIQhCkOgwn0sL4yOWc_VftZDvlSNCgVxzGHpEa8AZj4s9K7rDr_Ea4NI88EngssXudGXaGnJuZluUIS4ha5LDa-hWK_kD5kX5LcFxFv5Ud8EkPgWMLdqhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است و هر بالایی فرصت فروش است.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21184" target="_blank">📅 11:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21183">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پاکستان، ترکیه و عربستان سعودی در پی افزایش حملات حوثی‌ها به خاک عربستان، یک جلسه اضطراری رؤسای ستاد مشترک را بر اساس پیمان دفاعی مشترک مکه تشکیل می‌دهند.
این جلسه اولین گام در سطح فعال‌سازی تحت این پیمان است که مقرر می‌دارد هرگونه حمله به یکی از اعضا، حمله به هر سه کشور تلقی می‌شود.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21183" target="_blank">📅 10:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21182">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کلمبیا تمام روابط دیپلماتیک خودش با ایران را قطع کرد
دلایل اجازه ندادن به بازرس ها آژانس  بستن تنگه هرمز رعایت نکردن حقوق بشر و .... بود
یکی از دلایل جالبش رابطه ایران با گروه های مواد مخدر  بود</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/21182" target="_blank">📅 01:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21180">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نتانیاهو:
«آن‌ها اسرائیل را — اسرائیل کوچک — متهم به استعمار می‌کنند. و چه کسی ما را متهم می‌کند؟ در میان آن‌ها، گروهی در بریتانیا و فرانسه هستند.
به نام خدا، آن‌ها این اصطلاح را اختراع کردند — مستعمرات آن‌ها کل کره زمین را در آغوش گرفت.
استعمار؟ لطفاً دست بردارید».</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21180" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21179">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dad7c5c99.mp4?token=q3dpepLSXdCR-Qyx3voTDMJkSvCF8XzmlFnBbtMgCH-nmoWXhQcRJRSVPBW0U99FSvWg-cu_oYvLzqculIV-q4YS8jRhboIL_C1mh7H3ekP1Q0r6H976ZGWTkEw_xasfJvyg-IxbrKMtfqFBiBCmE1LXLxnm_8Q2aNAYo1yLaZsM3VhLsi9fJTAQCzzbV3c6O3yJf4G8cwGrdxNWTsRI6EhiEr86tq7rKq1Ql5R5Ft8VCGeY3kfzNRIU429JGj1lq0JMML5ZrdtEglJ5OdzoVIeWvSGXlSnv9Bl-ver0VE5uaarHm0gnsEbOKMkQVxshM-5b5NMv4YP-UFtxOnjjmwN1dwN-Dx8-7hQvytqrZsxyrURH4xP7-a8G45n3P0jENJ3Q8cN7X2DghcgzbndZngvp6CT6kp9Djn59oa6n1pBAvRxgeSOIniAUWSm-j5v8jnS96Esb6sYtJuZ_mN6QoGAa_aJX9cFL4M9g35kbl6OR-kB5YNypGeLU1v_Akp6OFvWcOZz8k7vZ2e4iMTp8ZcAhD1ch3Er6iY-WaY59_86ByF96fJJYKWqAjeQgmJ80X_M-mVrm3AjG6Sf7wah08Ud6jRLp5Zidi4uQwAph1nc_N1FjA5Grbdt0XciuZ_7oB_RPHKKfVUqInBBzNNrEg7tO8doWYvQfZnNt7bZh24g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dad7c5c99.mp4?token=q3dpepLSXdCR-Qyx3voTDMJkSvCF8XzmlFnBbtMgCH-nmoWXhQcRJRSVPBW0U99FSvWg-cu_oYvLzqculIV-q4YS8jRhboIL_C1mh7H3ekP1Q0r6H976ZGWTkEw_xasfJvyg-IxbrKMtfqFBiBCmE1LXLxnm_8Q2aNAYo1yLaZsM3VhLsi9fJTAQCzzbV3c6O3yJf4G8cwGrdxNWTsRI6EhiEr86tq7rKq1Ql5R5Ft8VCGeY3kfzNRIU429JGj1lq0JMML5ZrdtEglJ5OdzoVIeWvSGXlSnv9Bl-ver0VE5uaarHm0gnsEbOKMkQVxshM-5b5NMv4YP-UFtxOnjjmwN1dwN-Dx8-7hQvytqrZsxyrURH4xP7-a8G45n3P0jENJ3Q8cN7X2DghcgzbndZngvp6CT6kp9Djn59oa6n1pBAvRxgeSOIniAUWSm-j5v8jnS96Esb6sYtJuZ_mN6QoGAa_aJX9cFL4M9g35kbl6OR-kB5YNypGeLU1v_Akp6OFvWcOZz8k7vZ2e4iMTp8ZcAhD1ch3Er6iY-WaY59_86ByF96fJJYKWqAjeQgmJ80X_M-mVrm3AjG6Sf7wah08Ud6jRLp5Zidi4uQwAph1nc_N1FjA5Grbdt0XciuZ_7oB_RPHKKfVUqInBBzNNrEg7tO8doWYvQfZnNt7bZh24g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک موزیک ویدیوی Erotic از اتحاد عربستان و فاکستان ببینید شب جمعه ای دلتان باز شود!</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/21179" target="_blank">📅 21:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21178">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رویترز:   آمریکا و ایران درباره توافق مرحله‌ای برای پایان دادن به درگیری‌ها مذاکره می‌کنند</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/21178" target="_blank">📅 20:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21177">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رویترز:
آمریکا و ایران درباره توافق مرحله‌ای برای پایان دادن به درگیری‌ها مذاکره می‌کنند</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/21177" target="_blank">📅 20:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21176">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اسرائیل می‌گوید حملات جدید علیه ایران «مسئله‌ای زمان» است و تأسیسات هسته‌ای ممکن است مجدداً هدف قرار گیرند.</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/21176" target="_blank">📅 19:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21175">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">محدوده 4255 بسیار مهم است.</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/21175" target="_blank">📅 15:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21174">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fn7sLpzqJiJnCBSG_RIerKtAi_aN3f0EwZxgYR0p7FJ246VJ3ac8ubrzTAaty1RVTq4jTrQF68tXWUr-zZIcoFsB9vRv66TKsSbVhjq7dyP6uowvHhstV8g4W-MJ2wEqDu49RVdmXSX56xQ9aRucMN2bV0WCSvROvRaOhxwX9iUDJImqAtGT28ENsJnwnm96NSwplqAlw7bE7JtgSMiyN5gtv2oP9K1MX4tAACurPDqsjxVxaAnNuY8Wb2IpbARRoPohBLFIub0f9CrXJ_iLTO9UiA0ZgD99397mDd_f4MXISRHABzlxUu2NoRHyPmeul3ujEb8DX4kCLaKMLvDN0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشناس صداوسیما اشاره نکرد که اگر ما توان تصرف بحرین را که میزبان نیروهای آمریکایی است داریم، چطور توان حفظ خارک را که مال خودمان است در برابر نیمی از همان آمریکایی‌ها نداریم؟!</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/21174" target="_blank">📅 15:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21173">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کارشناس صداوسیما:   در صورت اشغال جزیره خارک توسط آمریکا، خاک بحرین را پس می‌گیربم</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/21173" target="_blank">📅 15:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21172">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کارشناس صداوسیما:
در صورت اشغال جزیره خارک توسط آمریکا، خاک بحرین را پس می‌گیربم</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/21172" target="_blank">📅 15:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21171">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مرندی ذوالاکتاف:  اگر کشورهای خلیج فارس جلوی پروازهای ایران را بگیرند، ایران فرودگاه‌هایشان را با موشک باران تعطیل می‌کند</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21171" target="_blank">📅 14:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21170">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یک پرواز از شرکت هواپیمایی وِارِش ایران، که قرار بود از تهران به دوشنبه، پایتخت تاجیکستان، پرواز کند، لغو شد و به فرودگاه بین‌المللی امام خمینی بازگشت.  علت لغو پرواز این بود که اجازه عبور از حریم هوایی جمهوری سلطنتی باکو به این پرواز داده نشد.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/21170" target="_blank">📅 14:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21169">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏
مصادره ۶ میلیون بشکه نفت ایران توسط آمریکا
تانکر ترکرز مدعی شد:
نزدیک به شش میلیون بشکه نفت خام ایران (به ارزش تقریبی ۶۰۰ میلیون دلار) که توقیف شده، بی‌سروصدا در حال عبور از اقیانوس اطلس به سمت ایالات متحده آمریکا است.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/21169" target="_blank">📅 14:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21168">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b70a5ce7e.mp4?token=RsN1j_MzXqtxdnUrLg4r2qyeDGzSqI2XBKN1B3EBLqpH_angFQjiJiodmmgbBhOfqoD23ZE1GcD08kyirVtdoNbEXQD59GHEF_DpFs7oIU9ojJLH8DkhqRi-ooBs9USO5mam0UmLQ8ctwEMcxLeUlloYYDmpVK98sz0J2KfC8fk3ph2xwlbNF60OWpRvNnpaS8qUzzdk-2i1zKihqRsW-Xxb4qkoPiF8N4EkvLftO_tKNYbArgxg9Z0SL-70DZ-O4RK_V52T5q_6ToIVhCcgeR8nVvVAI-z9Bf7XyzAxT-RSoVfhlyNyM1QlylAYEWApa3iMILuBAXfpsGcIleXTbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b70a5ce7e.mp4?token=RsN1j_MzXqtxdnUrLg4r2qyeDGzSqI2XBKN1B3EBLqpH_angFQjiJiodmmgbBhOfqoD23ZE1GcD08kyirVtdoNbEXQD59GHEF_DpFs7oIU9ojJLH8DkhqRi-ooBs9USO5mam0UmLQ8ctwEMcxLeUlloYYDmpVK98sz0J2KfC8fk3ph2xwlbNF60OWpRvNnpaS8qUzzdk-2i1zKihqRsW-Xxb4qkoPiF8N4EkvLftO_tKNYbArgxg9Z0SL-70DZ-O4RK_V52T5q_6ToIVhCcgeR8nVvVAI-z9Bf7XyzAxT-RSoVfhlyNyM1QlylAYEWApa3iMILuBAXfpsGcIleXTbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پرواز از شرکت هواپیمایی وِارِش ایران، که قرار بود از تهران به دوشنبه، پایتخت تاجیکستان، پرواز کند، لغو شد و به فرودگاه بین‌المللی امام خمینی بازگشت.
علت لغو پرواز این بود که اجازه عبور از حریم هوایی جمهوری سلطنتی باکو به این پرواز داده نشد.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/21168" target="_blank">📅 13:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21167">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پاکستان حملات هوایی متعددی را در افغانستان انجام داد که هدف از این حملات، مکان‌هایی بود که برای ذخیره‌سازی و پرتاب پهپادها استفاده می‌شد.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21167" target="_blank">📅 11:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21166">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoJJMVpo1rUdwGFPLG1VqXTQKT8SGMGfc-CI5rqTifQlvHvRLF12Up795oj-Bg2UHNF-LtLETqc_VTmV9T9cs176mbx5cKbd-7SkSyFciSxWrULVXhr6XQewDh5oql1a8fhVa7M8VlGXmrTLFtb9dbgDH_aXg71QSuTnxsCmt_jnJ1GJ-oMCQE95u3ZRnV-TVGEJsW8Qt1guO79SVfmCMQnCYJ21ECyBKWxNDA-5t2VY-ABfPxK99H3AJeqn_2dks3iTITJvTyupPugqfrl-N0H_LnSn09CD9MfXrhrAAP0awRo3YmsFNooINVICkMloOTvp359tRiQvgzxxwglg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC در حال نزدیک شدن به کف خود می باشد.  در این شرایط و با این تناقض، 2 راه داریم:  — صبر برای رسیدن طلا به 4335 برای فروش با تارگت 4230  — خرید در محدوده 4260 الی 4255 با تارگت 4300</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21166" target="_blank">📅 11:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21165">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/21165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سخنرانی پزشکیان در سازمان ملل اینقدر تند بود که حتی کانالهای ارزشی 6 سیلندر نیز از او ستایش می کنند!</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21165" target="_blank">📅 11:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21164">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">#FairValueCurve  نمایه FVC کماکان نشانگر پایین تر بودن قیمت نسبت به سطح ارزش منصفانه طلا است و لذا خرید توصیه می شود.  محدوده  مناسب خرید:  4302</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/21164" target="_blank">📅 10:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21163">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc_PtsgdlCfMdvSC1nP3uE3RsIiXfO_M5_6nMkAABxJbcltfEoBQSvShFg-wKI7ZJ4l5rLiFDd6NlrVdUlAwYFT1f29o8p-7hmplKtxWANc7zdr4N-tT9GboMVQQzD41mE_28F083EmOdi-lf6R21E1YCfMIwymaYGN6nK9_DfDojTZ1lloYv_p1is0NKmzJ_nwyYOxroT5917lwj9xrfhePryWxWpKKySMweUctdCW9gDYOZBFXZP78i26CDJDXvF_mduOZE97uj_KZ6Pq1VSGYP3XjMupibilS_sfIJ7XrmjMbbDf5BqXSAqLv9B1K9pSllFt4HrwFh8PIvjoFOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در حال نزدیک شدن به کف خود می باشد.
در این شرایط و با این تناقض، 2 راه داریم:
— صبر برای رسیدن طلا به 4335 برای فروش با تارگت 4230
— خرید در محدوده 4260 الی 4255 با تارگت 4300</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21163" target="_blank">📅 10:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21162">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_Y6-8ORMv0lG_VFutxUZkn9yYhfDOm-zbRxLr7oPctaiUfPSvKlMgpsPw28MsrbEsQeV706eGpD3exfTkrjgsYSwsNeeXtvRNhudi8Ju2RtISsJ4HPP_xdynrwNP8JTMASffwTslo_TgIvYO1uJPl2YiDkYv0bum8KTjTXxVKONsSyXkmt3_1Ehws82a0qsEJWTpuhTHuAN4bwUoY153DX1y83lx1fhbINFvJY5L1pEunvag3l3ZHtymm_lGkzzR-tQjO1RYgNQyQu8FWvd1JDRUvlj8HMqX0sq6ewHCnK17Vl3ix2matsEdFigs829MFDH8uM1Qq6c0r22SQoYWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بسیار بالایی قرار دارد.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21162" target="_blank">📅 10:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21161">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حملات هوایی پاکستان به ۳ استان افغانستان
نیروی هوایی پاکستان بامداد پنجشنبه حملاتی را به استان‌های «خوست» و «پکتیکا» و همچنین «قندهار» به عنوان دومین شهر بزرگ این کشور انجام داد.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21161" target="_blank">📅 09:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21160">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مرندی ذوالاکتاف:
اگر کشورهای خلیج فارس جلوی پروازهای ایران را بگیرند، ایران فرودگاه‌هایشان را با موشک باران تعطیل می‌کند</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/21160" target="_blank">📅 01:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21159">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شلیک موشک به سمت هرمز</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21159" target="_blank">📅 01:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21158">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H37g7jzx-6VTuKButrZuWwQNZYWjWkZVqT5VJR9KH5D6TRdVqOccchesPWcmVc4Uu_hqJRyYbWiNEiZye7cC9T4cS_okoo7kmSmQONHjs31Z6_UGPnCcM-J6rfMePU7YAoUVMn6eN9roGgcGW8PaHrYZJWt5-__79EoiWQzXA1Cd7KOMuaHiApcNW7cOfIYaxc2ukGvnRkUwd9qX5EDBH0_iTuzB1xE844kWIJ4_Ceos9NzEj5E1gk573KOOKYY7HZSRAIycTy3w6c0U0FOlAviVg8e74d0iVCSIbn90Mt0Hw4vVtylPWrtbhfn5q4EiKhUFFFBuildEM9L9ApmKyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تی وی جبلی هم عجب سیرکی است!
خود مردم ایران صداوسیما را نمیبینند بعد اینها برای اسراییلی ها به عبری زیرنویس میزنند!
باز عربی بود یک توجیهی داشت؛ دستکم بدبخت‌ها میفهمیدند کی قرار است توی سرشان موشک بزنیم!</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21158" target="_blank">📅 23:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21157">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بیانیه مشترک ترکیه و عراق اعلام می‌کند که ترکیه بر اساس یک زمان‌بندی توافق‌شده، به‌تدریج پایگاه نظامی بعشیقه-زیلکان خود را به عراق تحویل خواهد داد، در ازای آنکه عراق به‌طور کامل اقتدار دولتی را در سنجار برقرار کند و گروه‌های مسلح خارجی ممنوعه را از آنجا خارج سازد.
آن‌ها همچنین توافق کردند که تجارت، سرمایه‌گذاری و پروژه جاده توسعه را تسریع کنند.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21157" target="_blank">📅 23:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21156">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJsc5RZhkwpkT5YQmk5LTrY5i69dDiJJvaE0qHWnR0zEPX9s8qHrksgcAbbxCNw3ChGT0zyXMuxFa2WyVRqQ7iainaVVkMshiYCF5Nv_hbfRrPDAREHEnJZBglGvEtVJdrpggUDBx1Pj05175_DIEj0HvzMx9JqC8ifIkWm3m8DzWGF0yroUgDmtQbcRiRqmJntGGFf21oq1bwS3yI0w834DA3Ha2W2FLJ5QUTXKAVM4BkNh1jCHQRi-r1BAd_8hvDjmoA1ntfDdwFKXQVU3XJoylKg3lKctRovwFdJI0aMQPVJWyAx0wfS9WAF2JjE5Eg4fSUFy8BHyHD4o7LXELw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا چین به عنوان قدرت بزرگ عناصر کمیاب جهان غالب است و چرا این موضوع اهمیت دارد
چین ۸۵ درصد از تولید جهانی عناصر کمیاب تصفیه‌شده را در اختیار دارد و در سال ۲۰۲۵ بیش از ۵ برابر  ایالات متحده استخراج کرده است.
این ارقام تصویری از بازار جهانی عناصر کمیاب پیش از بازدید آتی شی جین‌پینگ از ایالات متحده ارائه می‌دهند.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21156" target="_blank">📅 23:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21155">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">درگیری مسلحانه‌ میان نیروهای امنیتی و افراد مسلح در محدوده جهادآباد سراوان</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/21155" target="_blank">📅 20:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21154">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">صندوق بین‌المللی پول: جنگ در خاورمیانه که از اواخر ماه فوریه آغاز شده، به طور قابل توجهی مسیر رشد جهانی را از طریق اختلالات در حوزه انرژی، کالاها و زنجیره تأمین، تغییر داده است.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21154" target="_blank">📅 20:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21153">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سخنرانی پزشکیان در سازمان ملل اینقدر تند بود که حتی کانالهای ارزشی 6 سیلندر نیز از او ستایش می کنند!</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21153" target="_blank">📅 19:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21152">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ایران معتقد است که دموکرات‌ها در انتخابات پیروز خواهند شد و ترامپ نخواهد توانست علیه آن اقدامی انجام دهد.»</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21152" target="_blank">📅 18:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21151">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پزشکیان:   بمب اتمی در اسرائیل است، اما بازرسان در ایران حضور دارند.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21151" target="_blank">📅 18:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21150">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پزشکیان:   با فشارهای نظامی تسلیم نمی‌شویم. به دیپلماسی معتقدیم. از جنگیدن نمی‌ترسیم.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21150" target="_blank">📅 18:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21149">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پزشکیان:   با فشارهای نظامی تسلیم نمی‌شویم. به دیپلماسی معتقدیم. از جنگیدن نمی‌ترسیم.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21149" target="_blank">📅 18:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21148">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پزشکیان:
با فشارهای نظامی تسلیم نمی‌شویم. به دیپلماسی معتقدیم. از جنگیدن نمی‌ترسیم.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21148" target="_blank">📅 18:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21147">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سخنرانی پزشکیان در سازمان ملل اینقدر تند بود که حتی کانالهای ارزشی 6 سیلندر نیز از او ستایش می کنند!</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21147" target="_blank">📅 18:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21146">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رویترز:
دولت امارات فعالیت شعب بانک ملی ایران در این کشور را از امروز ممنوع کرده است و بانک ملی ایران دیگر اجازه هیچ گونه فعالیتی در امارات را نخواهد داشت.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21146" target="_blank">📅 17:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21145">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">جنگ ایران.pdf</div>
  <div class="tg-doc-extra">300 KB</div>
</div>
<a href="https://t.me/SBoxxx/21145" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترجمه یادداشتی از Foreign Policy درباره علل ناکامی آمریکا در جنگ با ایران</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/21145" target="_blank">📅 17:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21144">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">محسن رضایی: تجاوزات دشمن نه تنها ایران را تضعیف نکرد بلکه آن را به قدرت چهارم جهان بدل ساخت</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21144" target="_blank">📅 17:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21143">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">با این منطق، فاطماگل قوی ترین زن تورکیه است</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/21143" target="_blank">📅 17:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21142">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">محسن رضایی: تجاوزات دشمن نه تنها ایران را تضعیف نکرد بلکه آن را به قدرت چهارم جهان بدل ساخت</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21142" target="_blank">📅 16:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21141">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">روز شکوهمند بازگشایی مدارس در ابرقدرت چهارم دنیا</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21141" target="_blank">📅 16:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21140">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiRlNcyFVUeHt7CqD8llDeKvbQOEu53NwfLJLxenSj5N_MppDM6BLw8Kf-cpZo_sm__cIiSmPIBEby6DQe1nOx2HMqNJMFkm425N4K3EIeEZhzn4Gdy4S2DYCrHVgRec2jqylc0SFD_ni8ddGDXBfYfJfx1jnUobVlDwlsxWJ40f8up8-vH-0h5dMk2H2_rtpW8WiNAxXHrv6S9VjQi1x0zBDF9HuTVkkOf0A7IwHBvVMZMwMAfgb6-UT2CRkDn0LZZ51slpsjraQ61k1sazk6hwAxcUjpBTjsamSU56ZlXvcq618gYbXX7uOg9hAJJF6xXjT83Guo2sZZrJPluyzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باربی های وطنی به مقر سازمان ملل متحد وارد شدند!</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21140" target="_blank">📅 16:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21139">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هدف قرار گرفتن یک کشتی در هرمز و کشته شدن ۲ نفر</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21139" target="_blank">📅 15:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21138">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">#FairValueCurve  نمایه FVC کماکان نشانگر پایین تر بودن قیمت نسبت به سطح ارزش منصفانه طلا است و لذا خرید توصیه می شود.  محدوده  مناسب خرید:  4302</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/21138" target="_blank">📅 15:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21137">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هدف قرار گرفتن یک کشتی در هرمز و کشته شدن ۲ نفر</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21137" target="_blank">📅 15:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21136">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">چکیده تصویری پادکست</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21136" target="_blank">📅 15:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21135">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">📌
خروج عربستان از mBridge؛ تقویت خاموش نظام دلاری  خروج عربستان از mBridge در کوتاه‌مدت اثر محسوسی بر دلار و بازارهای مالی ندارد، اما از نظر راهبردی یکی از مسیرهای بالقوه برای کاهش وابستگی به دلار را محدودتر می‌کند.  بااین‌حال، این تصمیم به معنای توقف دلارزدایی…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21135" target="_blank">📅 13:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21134">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flQmDwKI4znA0Lg6nrRcmQIP1Wq0ROAlqQziTgPL9TA_B5Rrz9rQ7IXmXKxqGhX_fHNHDnBVZ7D49ac64SrVbhGlFZDFqjcayLOKcP1iRV59Ld3zms5ajEPl19AXuXwbQ1rnCt0aUYpX8rAsiNgyAI_1F6K7vPNE-VpnyzninSmlJCiB26LN6Jev4a_fV8DQea5jLB84Z9c2A8TtsZJO5Ey87Pv27WQFshlyL6fWLHTp3H1qlO0_NOD1aMqgdJcC0ithQ8zCOn3jLvZsmR7JMSBSd07L_DCu0IhQIBxu3fF16u7ThUoPOkXkSjNM5XVx5c43Kvt-7LXt97aDFwO7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
خروج عربستان از mBridge؛ تقویت خاموش نظام دلاری
خروج عربستان از
mBridge
در کوتاه‌مدت اثر محسوسی بر دلار و بازارهای مالی ندارد، اما از نظر راهبردی یکی از مسیرهای بالقوه برای کاهش وابستگی به دلار را محدودتر می‌کند.
بااین‌حال، این تصمیم به معنای توقف دلارزدایی نیست؛ چین و سایر کشورها همچنان در حال توسعه زیرساخت‌های پرداخت جایگزین هستند و
mBridge
نیز ادامه دارد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/21134" target="_blank">📅 13:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21133">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gn4PPwYI_Gc5tN9aF3IYGcMrUYRjUDTUdkg6hGxNU-rB-BE87xSdrPGkkUD-JF_m-Ji3KbxIw8IyfCkGkGtePA4Aiuf5H1ildpPIJ-p5-xBpGall4Zmu9ydY0A0DpfRQgCfiWCV9muAgJyvkpvW8uKwahNleAP_VwZvA0Rhtrj3WeyBLB8u5T6fRNjaEktvVVSJngMRPNYZrrUkvJ-pLX_5KBG7GStC1fsqVuEi7-RqthArSj7_fX31xbP1WmND1RvnkDczvPulkiAGAFrKXZIbBan2-R20rW2Rg07Ltyh0-s_0X3fDiSLweqRwfNHnOP7uCr_4HXOx6SK9x4PPaBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC کماکان نشانگر پایین تر بودن قیمت نسبت به سطح ارزش منصفانه طلا است و لذا خرید توصیه می شود.
محدوده  مناسب خرید:
4302</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/21133" target="_blank">📅 12:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21132">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZ0dFG9iazLqeBrfq8Co6lxBAa-8kjPiDuARIqhFD9SYmTmzmyc1vyFmVfA64GmrwAlWXtqE4hLEv4SNG2GShAwkIq1LZEn1vg3coWso7lNLD247Y-KFqEyBQOes3YURtGVSH4DcjKWgEq5DGgKglauTyBOLQQ2OWML-RKYYS_ANGnQX-9oslShkQ2vGu-o1tJTACAXhoN800gvRcOyPxmCEttCYfclQhXJkHSwUR7mmnkoX82tyz40eg41e7Heonzpbv4CET7oc6spCEe4bEZ1CVnMibGZ1dUpqtQg8hoZUErkLbzcDXQZSmm9sVenWeuKHD2HpQSxpYs1VYEv1pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بالایی است.
اما طلا از صبح ریزش سنگین داشته و لذا دیگر وقت فروش نیست.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21132" target="_blank">📅 12:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21131">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8eae425e.mp4?token=S4jypmOQpZhu4IlUEtc3vbp8Z5L45YgH2gErSo2fIbwLlzqKuZPO8dCLIlKzybCUhSz0TgX_QNZJz1NlvKPz0lgrJ3qq6TAMGrAH8YVO3ZLoUSVD0AlM7sI-PmHkYNCF6jr7exiQaryOq7H-L7fKIU2A3Xl-TJfJUqXccSSKpnvD-GdObtoZyfu_7lowltk-YYMqnO9PwxJetwxXXVlRhEj39KG-kpIfwNRSv1efpkg3ZIYk7sYRWiDZEjfxcUwsek8pU2JvguE5tv3DCiNUiJ2Xtxf278OiAmJYIWXf1h4XOPGTHgWOSEFrQ_CgowE6kuxvFF5IFUbu9e6VDJKafA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8eae425e.mp4?token=S4jypmOQpZhu4IlUEtc3vbp8Z5L45YgH2gErSo2fIbwLlzqKuZPO8dCLIlKzybCUhSz0TgX_QNZJz1NlvKPz0lgrJ3qq6TAMGrAH8YVO3ZLoUSVD0AlM7sI-PmHkYNCF6jr7exiQaryOq7H-L7fKIU2A3Xl-TJfJUqXccSSKpnvD-GdObtoZyfu_7lowltk-YYMqnO9PwxJetwxXXVlRhEj39KG-kpIfwNRSv1efpkg3ZIYk7sYRWiDZEjfxcUwsek8pU2JvguE5tv3DCiNUiJ2Xtxf278OiAmJYIWXf1h4XOPGTHgWOSEFrQ_CgowE6kuxvFF5IFUbu9e6VDJKafA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز شکوهمند بازگشایی مدارس در ابرقدرت چهارم دنیا</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SBoxxx/21131" target="_blank">📅 12:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21130">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">زلنسکی
:
ما باید قوی باشیم و باید به پوتین نشان دهیم که او تنها در این سیاره نیست، حتی اگر این رؤیای اوست. و به همین دلیل او باید به مردم احترام بگذارد.
متأسفانه روس‌ها فقط زمانی به مردم احترام می‌گذارند که نشان دهید قوی هستید. آن‌ها به ضعف احترام نمی‌گذارند.
طبیعی است که گاهی اوقات مردم بخواهند ضعیف باشند، زندگی خود را بگذرانند، وقت خود را با عزیزانشان بگذرانند و به فرزندانشان عشق بورزند.
اما نه، باید با روس‌ها نشان دهید، باید نشان دهید که قدرتمند هستید.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/21130" target="_blank">📅 11:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21129">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آن دو دیگر (کوبا و میانسوسمار) هم که میبینید ستاره شوم کمونیسم بر بیرق چرکین خود دارند.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21129" target="_blank">📅 10:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21128">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">موسسه مطالعات جنگ:
به نظر می‌رسد حوثی‌ها با تهدید شرکای بین‌المللی عربستان سعودی می‌خواهند این کشور را منزوی کرده و مانع تشکیل ائتلاف علیه فعالیت‌های آن‌ها در دریای سرخ شوند.
حوثی‌ها در حمله به پایگاه هوایی شاه‌فهد در طائف عربستان در ۱۷ سپتامبر، یک جنگنده اروپایی «یوروفایتر تایفون» ایتالیایی را آسیب زدند. ایتالیا این جنگنده‌ها را برای پشتیبانی از عملیات‌های دفاعی در برابر حملات ایران به عربستان مستقر کرده بود. مشخص نیست که حوثی‌ها عمداً این هواپیما را هدف گرفته باشند یا خیر، اما حوثی‌ها پرسیدند که چرا آن هواپیما آنجا بوده است.
حوثی‌ها احتمالاً این مأموریت پدافند هوایی را تهدیدی بالقوه برای کارزار تهاجمی خود علیه عربستان می‌دانند؛ کارزاری که عمدتاً از حملات به تأسیسات نفتی عربستان تشکیل شده و در میانه پشتیبانی دفاعی کشورهای مختلف از عربستان ادامه دارد.
حمله حوثی‌ها که به هواپیماهای اروپایی آسیب زد — هواپیماهایی که برای پشتیبانی از تلاش‌های دفاعی عربستان در برابر حملات ایران به این کشور مستشر شده بودند — در واقع اهداف ایران برای شکستن ائتلاف مدافع کشورهای خلیج فارس در برابر ایران را نیز پیش می‌برد.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21128" target="_blank">📅 09:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21127">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdqDPsB8mn0Nx11erBM4OWhqjQVbkLHramsZHswNtsFpMsyJ86ZsRzeHWplQo627FFvEK9IlJPGcUgbRmcmtqbqh9XPk-1fuXHIsCn1K9ZHC2__ZodGd9OXvpwXEa2iQ77NDQxitUlWR75gkdsjO5GqIt7_iHD-vFkjmFS3hlHRV44HxJFKj2jeNlZmmDIQC9aeB2PtEKWAxZuYLMIx3oZ1ENhtDEq-nEksoxIOVa5tm5PhhREUeDbmLycXN7gxJCmDIw_L57gg7MhxOo69-YAFlh6sH25QsrpSOXZlLulk_ee_uW-IAKpGc9eTvvouuyhvXjlhJYmtS3PmGDK1I8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 28</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21127" target="_blank">📅 08:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21126">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نخست وزیر یونان، کیریاکوس میتسوتاکیس:
ما در ۳۰ سال گذشته هزینه‌های زیادی برای دفاع صرف کرده‌ایم، اما در زمینه صنعت دفاعی داخلی، دستاورد چندانی نداریم.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/21126" target="_blank">📅 08:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21125">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏
سخنگوی سپاه: نحوۀ پاسخ ما به حملۀ جدید آمریکا از اسرار نظامی است
اگر آمریکا به کوه کلنگ یا هر نقطه‌ای دیگر از ایران حمله کند با قدرت پاسخ خواهیم داد.
این‌که پاسخ ما چگونه است از اسرار نظامی است؛ ما اسرار نظامی خود را فاش نمی‌کنیم اما در میدان عمل نشان خواهیم داد.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21125" target="_blank">📅 08:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21124">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو، انتظار می‌رود این هفته سفری کوتاه به ایالات متحده داشته باشد تا در مجمع عمومی سازمان ملل متحد سخنرانی کند، در حالی که نگرانی‌هایی در خصوص اعتراضات احتمالی وجود دارد.
نتانیاهو قرار است به جای فرودگاه بین‌المللی جی‌اف‌کی، در یک فرودگاه نظامی در نیوجرسی یا فرودگاه بین‌المللی لیبرتی نیوارک فرود آید، که این تصمیم تا حدی به دلیل نگرانی از پیچیدگی‌های مرتبط با ممدانی، شهردار نیویورک، اتخاذ شده است.
هیچ ملاقاتی با رئیس‌جمهور ترامپ برنامه‌ریزی نشده است، هرچند گفتگوها با مارکو روبیو، وزیر امور خارجه، و سایر رهبران خارجی همچنان در حال بررسی است.
بر اساس اظهارات مقامات نزدیک به نتانیاهو، سخنرانی او قرار است بر ایران متمرکز باشد و ممکن است «غافلگیری‌هایی» در بر داشته باشد.
مقامات اسرائیلی همچنین برای احتمال اختلال در سخنرانی او در سازمان ملل، از جمله آزار و اذیت یا خروج هماهنگ هیئت‌های چندین کشور، آماده‌سازی‌هایی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21124" target="_blank">📅 01:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21123">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">صدای انفجار در نزدیکی جزیره قشم!</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/21123" target="_blank">📅 01:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21122">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">صدای انفجار در نزدیکی جزیره قشم!</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21122" target="_blank">📅 01:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21121">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گویا جلسه برگزار شده و به نتیجه نرسیده!  First Time?!</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21121" target="_blank">📅 01:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21120">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLuYYpEhd-i_7YClcMF5WTbFUJ5OMbiKgkttL6-RaFDNDiWbW1v8odruVwCotluagINMwsVLk3ueHe3p39nNHFl_QvM1V_iZSf2URg8fYF0ucVrbDDuwA3c5188lVg6lBlDDeiiztJEiqrYl_CjwuUt1wi60OnbB8ARTabUZ6snmMiOIayaSy7VT7h_JSPY7sz1hJJIo7jQV2DFiT4nXTLylrrWQFrYRXl3-6cSu_U1xOtDtYHonci_pfSGsGJ_sCMkEVktb4RTie-SHi6mY7xN8K3bsua9onhC1IaecveCx5is6gAjcmZuQ3v99Nnq83RKSWEmHug-LnyDEWw_p4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا اعراب به دنبال فراهم کردن شرایط دیدار حضوری پزشکیان با قاتل امام شهید هستند.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/21120" target="_blank">📅 00:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21119">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bY6HYQ7-2I0av3wnqgwY8VOfLHXogULrmFEiOJWwc83g4XswmzZoFd5G3uE58Htj1_Ih3c-JHLlUnoAu8D6Kt41pAYBpEEtvg2E3gHPJGSkONwzOFf-JKNIeGJdrB1Y2NpK-yj4gKVLQL8gwVQc8dusr-iXOdB0REYxpIEBUppd9HOhJT9yY9WaKGU0ZpbZCJ9ABN59yhFHHzh8z-wCDYsRB6UXcbwR-XXjP74r-gmvgSv22SK7h6pT9XK2uXkm3fsuTpNaMjOc1M6PvsqCW2qWpXXY5A0ou5N_t2mMGfexssYn7VeTq6l0FTwrSIxs3533IOB9GSElpEZG0GLqYDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RUNCFD — W #SUNRUN  مقداری از نقاط ورود پیشنهادی ما پایین تر آمده است اما هنوز بشدت روی این سهم مثبت هستم.  پیروزی دموکرات ها در کنگره و توجه دوباره به بحث انقلاب انرژی سبز می تواند این سهم را به بالا پرتاب کند.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/21119" target="_blank">📅 00:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21118">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8dL5ywsLQ-4-zqpUFjYUtyz0FemBzaOjeIQ9qTNGlRZ54H5bErBN9J_WnFes3Qsvc5ZgXZ_NkY1u8tzh4-6SpsN06VIqG6ivwl341_fFduijyd5ubYk4zwcg0vVWVYkDU78Lc91W4C19XgeTNcZHM-xMnliwf0GOIu9MkCfb39Dpqz5LcgdOXQw8Y7O8rWZVC_HGPOWVY6dgCcMus4OMrCpZ767AH5Qoabje8od5mbLzVk1BNy5Ef28kQ7SJbBD2rs0shx1g5vSHzCmWoTXG-VpWa-bjGf6vK-GVq2rQLXa5UJsDz-mLGSraOjAb2AUDM_ssLgTQJiNY83_0ZNOsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RUN_CFD — D #SUNRUN  از محدوده ورود دوباره حتی اندکی نیز پایینتر نیامد.  البته هر چه پایین تر بیاید خوب است، این سهم یک رشد دستکم 3 برابری دارد.  همراهان Secret Box در خارج کشور این سهم را دریابند و هم میهنان اسیر در درون مرزها نیز میتوانند روی بروکر WM Markets…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/21118" target="_blank">📅 00:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21117">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJf8zr4cRlBp-zIFMb2EZiXmhXVvdw-OTjNeCCfMAfnzmASvcoqHnNOVgrmVGo_dgYYDzoiq5rFaKwVV32lqOj2Bw_2o5Bf8SxP0EczbzF42kbObURi4rTN_vPw-uJfMHdw7nVtnYAH3Bs1jFp3kAMqN43W__MDCWFH-yw6NdYi5dEegKdB-TDkkgkOh_uU0rEsiR5seHsMLvSOFZT9FHoOoumr3mABpQOc4vD6xpW6Dyp8mlBddyiX4ncyUsrbQAl8HPa38E-zGjbwpxJgAJ9o7sXmfsKh1AHDvFmGnejlwtuFsvY9KsM_jv3KhuowL9oMIjF_eZLW-MxzLCFluGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL   دوستانی که درباره نفت دایرکت دادند؛  پوزیشن های خرید ما به هر دو TP پیشنهادی رسیده اند و فعلاً خرید نداریم روی نفت.   تحلیل جدیدی از نفت ارائه می شود.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21117" target="_blank">📅 00:17 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
