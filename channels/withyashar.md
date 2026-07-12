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
<img src="https://cdn4.telesco.pe/file/KvRRoHMgctw-ifpnNZYr_KLKb5rpm2pTmX66vDC0J0qK6iRlWdtDeLzwgBjF7fiNfyheALMoGH4YtyQXF0INRppfl3cAeXBiPIXTy-FeZuT4Akf4XCwi2YUJQF-pQtCzVxZNGVR9T_dWhwSSvP8CB786wbwM7mBBucSE5XA6MFBke3Ekr66wq03nsshsVhLnipybK9hnp8hncrGUxx7734BkrK2rUS8O9206PDLlkPdVmSiO6YkdPfgJAB556-yHtqmrDGbPJJ6tZMUPAH47ExE8hTTxCEYjqd9PllPaJibXTf4L_AoxyTBhuMgo0d52vZCspEL0wxbEeGucv1_0cg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 371K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 13:13:50</div>
<hr>

<div class="tg-post" id="msg-17564">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">همین الان پارچین پاکدشت ۴ بار صدا انفجار اومد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/withyashar/17564" target="_blank">📅 13:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17563">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4352950692.mp4?token=V1R2YR08oXmImkZSp9RBtP2JFHC2Ewr1GtSx75mRZqKIev6sO7mVqmL3vA3TU6XFPUHP6iCdIkhQMLHLsl_cisqhrlEoxvfm0pIqrYi8uDxIq6MIccTA4fP8vtv-ZiFp2zdiwLXDShuY1TWTowqzjfl5IITfj1IuJFsylRgr1tqd0WqAUmXO24lPI4x74sehL2k0HnNxloR_CI7iMOQPbfvNJI2Rc69-ucWyZRSTAr-HAYCssm2vtk_YCKZ9o_hyWhHYPNY4nyWVWZYvmD7jlhMPsrVTBc5If8ZUhdgOkxf_8ccJlSLrjZJ-VxFrgHEBHQ3vBcefryH46AGFcppEG6saAUe7LtT8gpi1d250IKAla3CY9ltzkI-841ZwG8SiQl5EXevNoFzmZLBKrwZTKKbBMbh93G-YySk5wiBoEvt6ggSr6iBKlR5pCHvEkU29WKKqpfA3GzDIILPwsQeIw0V51-Q8r2M3rpI96Dae04wrRc_lSxWo01T0qZUoN6Z7qzz2j1gL1RHjv5Lt-BPaUvOLl0k-4NZUDyG_XSb_ZEVRbZ9sSg9kox7y3wcA-x8pnybDojjVp6V20C5Rf04335NrOCtt1K7-kURL2oH6MAFcZjxenaVM7uVvtqGV-hNG0CAbAMus1zAdCqgFfRtwbvbb_4lahx9Zsb55_K9UYuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4352950692.mp4?token=V1R2YR08oXmImkZSp9RBtP2JFHC2Ewr1GtSx75mRZqKIev6sO7mVqmL3vA3TU6XFPUHP6iCdIkhQMLHLsl_cisqhrlEoxvfm0pIqrYi8uDxIq6MIccTA4fP8vtv-ZiFp2zdiwLXDShuY1TWTowqzjfl5IITfj1IuJFsylRgr1tqd0WqAUmXO24lPI4x74sehL2k0HnNxloR_CI7iMOQPbfvNJI2Rc69-ucWyZRSTAr-HAYCssm2vtk_YCKZ9o_hyWhHYPNY4nyWVWZYvmD7jlhMPsrVTBc5If8ZUhdgOkxf_8ccJlSLrjZJ-VxFrgHEBHQ3vBcefryH46AGFcppEG6saAUe7LtT8gpi1d250IKAla3CY9ltzkI-841ZwG8SiQl5EXevNoFzmZLBKrwZTKKbBMbh93G-YySk5wiBoEvt6ggSr6iBKlR5pCHvEkU29WKKqpfA3GzDIILPwsQeIw0V51-Q8r2M3rpI96Dae04wrRc_lSxWo01T0qZUoN6Z7qzz2j1gL1RHjv5Lt-BPaUvOLl0k-4NZUDyG_XSb_ZEVRbZ9sSg9kox7y3wcA-x8pnybDojjVp6V20C5Rf04335NrOCtt1K7-kURL2oH6MAFcZjxenaVM7uVvtqGV-hNG0CAbAMus1zAdCqgFfRtwbvbb_4lahx9Zsb55_K9UYuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
@withyashar</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/withyashar/17563" target="_blank">📅 13:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17562">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حمیدرضا دهقان، افسر پدافند دریایی ارتش ایران، در حملات آمریکا در منطقه جاسک در جنوب شرقی ایران کشته شد.
@withyashar</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/withyashar/17562" target="_blank">📅 12:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17561">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نتانیاهو در حال بررسی سفر به منظور شرکت در مراسم خاکسپاری لیندی گراهام است. احتمالاً ترامپ نیز در آنجا حضور خواهد داشت.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/withyashar/17561" target="_blank">📅 12:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17560">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">معاون امنیتی استاندار خوزستان: سه شهر در استان، بامداد امروز مورد حمله آمریکا قرار گرفتند و در حال ارزیابی خسارات هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/17560" target="_blank">📅 12:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17559">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خبرگزاری مهر :  شبکه ارتباطی تو کرمان بر اثر حمله آمریکا دچار اختلال شد
@withyashar</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/withyashar/17559" target="_blank">📅 12:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17558">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دیوان امیر قطر: پیکر حمد بن خلیفه آل ثانی پس از اقامه نماز در گورستان لوسیل به خاک سپرده می‌شود.
از امروز چهار روز عزای عمومی در سراسر قطر اعلام می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/17558" target="_blank">📅 12:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17557">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cgs0RShng0GKO54Y9Cg6rbW0OyodryFt8eGmsI0icu5uzT_2CYL1jjdabGQwFnIfnR4fInSbuJo9gLiHq5f0xbpMmF1IZFhAVMgxzWIC_wz00o2UoByw0AHpCvy-k277VD58C_izZZQ4zrS2JkABffmacTe4qQEJHvSgIeOl3yfbj9c-DVUiyUGd4-XENFj_b03C_GNrM_VFACZtlHCSqgXhztfOkLVgYhd1Ri_Da7em8g41zDu5eXLGNditqvU1U-b9kaYiaKHPqaEDTkg7cqIv39_OJYSP_cJq0jxW191dSnJuHZsZTRxZlfPm0cNj79iifAtTPnPCjJQJGyRPaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب
🫱🏼‍🫲🏽
@withyashar</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/17557" target="_blank">📅 12:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17556">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">هنوز تو شک ام
🤦🏻‍♂️</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/17556" target="_blank">📅 11:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17555">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سرویس جدید رو فعال کردم اگه بخوام یک استوری حالا ۲ روز میمونه
😂
🙌🏾</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/17555" target="_blank">📅 11:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17554">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شاهزاده رضا پهلوی : از درگذشت ناگهانی سناتور لیندزی گراهام عمیقا غمگینم. او دوست استوار مردم ایران و مدافع سرسخت آزادی بود.
در لحظاتی که نیاز به شفافیت اخلاقی بود، سناتور گراهام همیشه در سمت درست ایستاد. وقتی دوستان کمیاب بودند، او در کنار مردم ایران در مبارزه‌شان با استبداد قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/17554" target="_blank">📅 11:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17553">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">استانداری کهگیلویه و بویراحمد:
اصابت پرتابه پهپاد آمریکایی به اطراف شهر یاسوج در ساعات اولیه بامداد روز یکشنبه
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/17553" target="_blank">📅 11:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17552">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نتانیاهو: اسرائیل و آمریکا دوستی بزرگتر از گراهام نداشتند
نتانیاهو با ابراز اندوه عمیق، سناتور لیندزی گراهام را دوستی عزیز برای خود و اسرائیل خواند و گفت در آخرین دیدارشان به او گفته است: «ما دوستی بهتر از لیندزی نداریم.» او گراهام را کسی دانست که امنیت اسرائیل و آمریکا را جدایی‌ناپذیر می‌دانست و تأکید کرد اسرائیل یکی از بزرگترین دوستانش، آمریکا یک میهن‌پرست بزرگ، و خودش یک دوست عزیز را از دست داده است.
@withyashar</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/17552" target="_blank">📅 11:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17551">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGQGN95Ty8FDK1R4SWWNlH8OYVI680TSunfehytAlIglalrNFuny3x5GDKnWVVsWEWPvA13DYqHteEorRsEiori2OHTZbCAcTo64YbNyU7-t0Pg8ru9yNvwiMlJNEFBhXhMCx3e04r691_OhHtNJf7y25T2TOKw8glvb0NnrYKcdmtZLMs_i-qzeaCa0ji0gevdkwwRfgrsUnwmKy3oIAyFVOFuTMqqCG3Kw8eG2Fg51VhRW8R3YTonRWhPMs6h_bVGsohOQq3u1ZQJpsH6fMosvi3NI_BAkLsGoggNLvv2FkFubwvWuSElof1CiWn8oy5qmxGPb01iKSUcVpoAlyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : شکی‌ نیست مردم واقعی ایران و انقلاب شیر و خورشید یکی از بزرگترین حامی های خودشو از دست داد ، عمو لیندسی عزیز …، خوشهالم که به واسطه این انقلاب با این شخصیت بیشتر آشنا شدیم و همه با هم کامنت های زیبایی‌ رو براش‌گزاشتیم
💔
😞
او واقعا مردم ایران…</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17551" target="_blank">📅 11:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17550">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گزارش وال‌استریت‌جورنال :  لیندسی گراهام نقش اساسی در متقاعد کردن ترامپ در حمله به ایران داشته!  گراهام مکررا به ترامپ تماس میگرفته و پیگیری میکرده و حتی به کلاب‌های ترامپ در فوریدا سر میزده  گراهام چندین‌بار هم با مقامات اسرائیل دیدار داشت و حتی تا تل‌آویو…</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17550" target="_blank">📅 11:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17549">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اتاق جنگ با یاشار : شکی‌ نیست مردم واقعی ایران و انقلاب شیر و خورشید یکی از بزرگترین حامی های خودشو از دست داد ، عمو لیندسی عزیز …، خوشهالم که به واسطه این انقلاب با این شخصیت بیشتر آشنا شدیم و همه با هم کامنت های زیبایی‌ رو براش‌گزاشتیم
💔
😞
او واقعا مردم ایران رو دوست داشت و یک آمریکایی وطن پرست واقعی بود
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17549" target="_blank">📅 11:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17548">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtWzDX9IFU6k3lvdgO8lfusPw-HqLalVQV0V0FkmI1FmJ0_xWCpWZJpD-5pBhuLIOWGLBbI4ytEM326gOYt8eB9bcps32LM7JhiaqbJCZyo1h2jcaOYfWDqyTww3ngDjKv0EgX2hSv3XHpfXb11U9z3J2Hf31fqCIBSEqLSxJv3tzvIzZXuLAIslINjsSBW4LzX1yDZIVILWQQIiTbrsu54cqMBdbtKf6k4Pde0wab_5agRsyRQ_kvoE4c3FTDamVhB00P_OQMNoW08HQ6-gq5sGFp7JOoorU4RGmkAeFnK1K5QaEc_qAyNLW0FngFXu-WrQ3Y5BIH4f1JpOIX3GlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: سناتور لیندسی گراهام، یکی از بزرگترین افراد و سناتورهایی که تا به حال شناخته‌ام، درگذشت! او همیشه در حال کار بود و یک میهن‌پرست واقعی آمریکایی بود.
جای خالی لیندسی بسیار احساس خواهد شد!!! جزئیات و ترتیبات بعدی. خیلی غم‌انگیز است! رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17548" target="_blank">📅 10:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17547">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سناتور لیندسی گراهام در حالی ساعاتی قبل از دنیا رفت که دو روز قبل در اوکراین با زلنسکی، رئیس جمهور اوکراین دیدار کرده بود. او همچنین قرار بود تحریم‌های جدیدی را علیه روسیه به تصویب برساند!
دیروز هم از کارخانه تجهیزات جدید و پیشرفته بازدید کرده بود !
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17547" target="_blank">📅 10:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17546">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گروه تروریستی سپاه فیلم حملات امروز را منتشر کرد
در این حملات از موشک‌های بالستیک، سوخت جامد و مایع و نقطه‌زن قدر، عماد، خیبرشکن، فاتح ۱۱۰ و ذوالفقار استفاده شده است.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17546" target="_blank">📅 10:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17545">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">صداوسیما:لیندسی گراهام به درک واصل شد!!
@withyashar
🤬</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17545" target="_blank">📅 10:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17544">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دو انفجار در فرودگاه بین‌المللی بحرین رخ داد.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17544" target="_blank">📅 10:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17543">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دیوان امیری قطر: با قلب‌هایی سرشار از ایمان به قضا و قدر الهی، درگذشت والامقام، امیر پدر، شیخ حمد بن خلیفه آل ثانی را تسلیت می‌گوییم
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17543" target="_blank">📅 10:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17542">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حمله به عمان، رأس المسندم هدف قرار گرفت
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17542" target="_blank">📅 10:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17541">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qp24jMPaZyg-JmR-SpF6xYWXUbQhWz4Kw5cY67gjDebEafi-hNzpOv5fpmSBCMqTADQog8Cn9LGINPlKW8u__48Csy8V6XXSXia8CpRIstjvt6RZR42pKqRX9kxL5X4PWTm3b44_i24wVjuDOU1DdP9z8xxbMsiv3k9NgkD8FOy0cgSCLZNbUJnWnluCynRIb3wJlgTPL9RgH0ylEZTNT7YM42YaeVtROzoAowVjccQ8fjS263TS5Whpn6VWhz1urukNFj92rsg_GdhJVFw1WaaqedTmqkQrWIs6quhlw6nyPki24mRaFvLmYEoSIdFzeMxHp6UERQbZOAm5g0dK5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت لیندسی گراهام که دوباره وایرال شده ….
حداقل از یک عکس خوبِ من استفاده کردند.
مرا از روی دشمنانم قضاوت کنید
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17541" target="_blank">📅 10:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17540">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">در بحرین و کویت، مجدداً اعلام شد که آژیرهای خطر به صدا درآمده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17540" target="_blank">📅 10:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17539">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وزارت کشور قطر اعلام کرد که سه نفر، از جمله یک کودک، بر اثر برخورد بقایای رهگیری موشک‌ها و پهپادهای ایرانی ، مجروح شده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17539" target="_blank">📅 10:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17538">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">واکنش ایتمار بن‌گویر، وزیر امنیت داخلی اسرائیل، به درگذشت لینزی گراهام:
«امروز اسرائیل یکی از بزرگ‌ترین دوستان خود را از دست داد. سناتور لینزی گراهام در کنار اسرائیل ایستاد؛ نه به این دلیل که این کار آسان بود، بلکه چون باور داشت کار درستی است.
حمایت بی‌وقفه، شجاعت و مواضع روشن او باعث شده بود میلیون‌ها اسرائیلی برایش احترام قائل باشند. اسرائیل همیشه دوستی، حمایت پایدار و تعهد محکم او به امنیت این کشور را به یاد خواهد داشت.
صمیمانه به خانواده‌ی او و مردم آمریکا تسلیت می‌گویم. یادش گرامی باد.»
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17538" target="_blank">📅 10:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17537">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از مقام‌های آمریکایی گزارش داد اطلاعات اسرائیل نسبت به احتمال وجود طرحی از سوی ایران برای ترور دونالد ترامپ هشدار داده بود.
با این حال، این مقام‌ها تأکید کرده‌اند که تهدید ادعایی در ارزیابی آمریکا «کاملاً معتبر» تلقی نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17537" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17536">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تکرار تاریخ؟ سال 1979 نلسون راکفلر بعد از فتنه این سال در ایران، که شدیداً از شاه حمایت کرده بود، به شکل مشکوکی از دنیا میره. راکفلر دقیقا مثل گراهام هیچ بیماری‌ای نداشت و کاملا سالم و سرحال بود. و با مرگ ناگهانی (که سکته قلبی دلیل رسمی اعلام شده) از دنیا میره.
حالا گراهام هم بعد از حمایت های زیادش از شاهزاده، به دلیل مشابه فوت میشه
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17536" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17535">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">لیندزی گراهام، سناتور جمهوری‌خواه ایالت کارولینای جنوبی، در سن ۷۱ سالگی بر اثر یک بیماری کوتاه‌مدت و ناگهانی درگذشت. نیروهای اورژانس پس از دریافت گزارشی مبنی بر ایست قلبی، به منزل او در منطقه کَپیتول هیل اعزام شدند
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17535" target="_blank">📅 10:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17534">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارش های جدید از انفجار در بحرین
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17534" target="_blank">📅 10:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17533">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سپاه : ارتش آمریکا به تعدادی از پایگاه‌های ساحلی و برج‌های مخابراتی در سواحل جنوبی ما حمله کرد تا شکست خود در تنگه هرمز را جبران کند.
@withyashar</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/17533" target="_blank">📅 06:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17532">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سپاه : ما مرکز فرماندهی و محل نگهداری هواپیماهای بدون سرنشین MQ-9 را در پایگاه هوایی الامیر حسن در اردن با استفاده از موشک‌های بالستیک منهدم کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/17532" target="_blank">📅 06:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17531">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فوری،کان نیوز اسرائیل : واشنگتن تصمیم گرفته که محاصره دریایی و عملیات نظامی علیه ایران رو از سر بگیره.
@withyashar</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/17531" target="_blank">📅 04:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17530">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بندر ماهشهر ۲ انفجار خیلی بلند
@withyashar</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/17530" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17529">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDpIFmZSayjVl9oEPc_OIEfqLfRJw0KVAIK6qq2V_rqytO5KQh1Byfmv9ro1s7CZesJxyna9Hqj4iTgMjXZxQKWx5aF_WwEAWCgksxFcUyRHjSqAIZe_-71WvoCq7ZTXLzm8LI4Rv_QuW8b9L4RBC7ohgezu6J1Inep4hztaki4b7NrM_CS_zKGt1R8m8hHRpILswc-j2kbIlD26xnfCmIvfRqMfCmIVCxiyjlba679_YVUcLFWTY9tmdytr3e0Q3oio8XNw2Dq3PpnsNNjQickLvhKnQtHYnfK6LvodaQOQV2HQY9-025S3I8I0VH4iKqww7H_vCxR8qgEIWXHN3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار پایگاه نیرو دریایی کنارک
@withyashar</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/17529" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17528">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">صدا و سیما: ۱۰ انفجار در جاسک در یک ساعت اخیر و ۱۲ صدای انفجار در استان بوشهر شنیده شد
@withyashar</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/17528" target="_blank">📅 04:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17527">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مقام امریکایی: هم اکنون موج جدیدی از حملات علیه ایران آغاز شده است
@withyashar</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/17527" target="_blank">📅 03:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17526">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">در مجموع ۵ انفجار جدید بوشهر ولی از‌
نیروگاه دور بود
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/17526" target="_blank">📅 03:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17525">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">۳ انفجار جدید بوشهر و جاسک
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/17525" target="_blank">📅 03:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17524">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6654096451.mp4?token=Wi85aigks-VqOrAKADDzG0brk7NVyDTW7VgRqOmeegZrvk-O0tke4Gz7XcwURQai8AtPzE3-FL7zaRnDYnWck3dHhiLRA-j4XyuT9SFnFyGcKxRu7AeyxsZXedbwvXPMyL6z9d1FHzTkIdBFIf_8vC4grleYIIUxGpee8q15CQIUfXb4eZ61dKrJBh-GP7iMfBDKoGaaoS04skg5519d65_U6imELBfm-MWapLwYzlUJIgeQa3P8Pf10vwogVAmNDSHJKSPpBVbccu9goubV6rswxNf9GzOReHtQVf_bsoEv2jBiI2n-wRLy0QJhQCtN8I6d5Ma9cIgchLpVYgHz-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6654096451.mp4?token=Wi85aigks-VqOrAKADDzG0brk7NVyDTW7VgRqOmeegZrvk-O0tke4Gz7XcwURQai8AtPzE3-FL7zaRnDYnWck3dHhiLRA-j4XyuT9SFnFyGcKxRu7AeyxsZXedbwvXPMyL6z9d1FHzTkIdBFIf_8vC4grleYIIUxGpee8q15CQIUfXb4eZ61dKrJBh-GP7iMfBDKoGaaoS04skg5519d65_U6imELBfm-MWapLwYzlUJIgeQa3P8Pf10vwogVAmNDSHJKSPpBVbccu9goubV6rswxNf9GzOReHtQVf_bsoEv2jBiI2n-wRLy0QJhQCtN8I6d5Ma9cIgchLpVYgHz-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدافند تهران
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/17524" target="_blank">📅 03:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17523">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پدافند شرق تهران درگیر شد
@withyashar</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/17523" target="_blank">📅 03:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17521">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fjQ5BATf-smI_xdzU02wLjxde6jQijzxcu_goJOebtJeCvXwlW3i8onagLgHslJybB30WDe9mOS5uUQqbm0QbrSZnjvJ7pHWUbVvTxfsOOmmLc3wHpv26gwUnZCgldFfYOHIauUINvH0q3BnWhk56APU7RXzC0zxw5VMjN-YGcTBWAuaDDZr2zDDtMsI7ODTc34uGmeV1MHM1BHKs0aBriyKq5RLfxP-fIajMTJi_SYAwfUJy9FPYJw9ojUoxP27p-cPINrp1hG84IvC3EytQJUxANmnHV9hb8xCr95rwPSyNj6dKMvKkZQPNCcDFua93m-M_Cj04FM3Ee89xt6Rfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TEu_tw3CfRV4EQ5GZeDLjdPL3IRHgbYKvB2dtVzTKNptkSimFTVqDhgIPhDwaeDBZ7Ea41cDR6a2KnLJu0O9mPWZdYhcbl-horRsyL9n50wA171OFl9f6eimZQlxdDcHTusADJbB353QdmofXG36RV4WvLcybLfRHeeteaVUcbF-6jQ-oHyXpzt5myTNs1PWFGyrW8V4DWqF9w9Tdan3FJy7Ry8CUFOGlQs_nx_D3iThlVVEi3PyeoQwzR0wlbOfI_tgZNjag5w2Q3D93FG6w43PanRFnr6hm06vSg3EaQnni6CMjjZVawEieZGqfOR1ppn_bLuKE-1vGV8YXFT-DQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هم اکنون تهران !!!!!
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/17521" target="_blank">📅 03:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17520">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">صدا و سیما حملات به بندرعباس و سیریک رو
هم تایید کرد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/17520" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17519">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuH2IyzcX8qrwRiX_1yd_MNdNq_-hkc3ArO3oCsct-U8dlKmJXN_mREdHXzT8y8xp6HlAqT601sG28uaHij3P3YrR7SF0_-p9r4uhU95VPkO_imkRFfcMssDeiI-h5S0aIzp_Mdj6nAdG1jlzVF0TVHJlhTLCbQKayJt09yKruBzS2H82JGoyduPAWskJpnrvHZPvMFp8nKHIAj4uLrhjPnOZVa65h6TGOW65wudVBXBS3blN8zWCxqdOjNvLhAeMFG_N-4TT0PZIUhDUWctKsiw1HPkjPn6RUvScBhFmY3upPGQ8lFNczxlrAv67YbQbb9_YdNMVi8XXgiu_q1Uqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثه دریایی در ۹ مایلی شرق عمان
سازمان تجارت دریایی بریتانیا (UKMTO) از حادثه‌ دریایی در ۹ مایل ساحل شرق عمان خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/17519" target="_blank">📅 03:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17517">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FwaYCJAXDMn4ovfbO6NZ12pS-bmp9jUAzGGtFrTVWFlGc7T---lY5PR96qAJuIcqDkcQtsrAXLXShN5ZmfXOUmmkvJABUvXcXqXf-5oa9KuUR4tT8uQqH0Mt53CQAo-V7AoFxaItP1gtDnSEpDDARBnSdDI4DbaTJ6STnkWY_ZeWjHMbBFxEk82CBMrfsHvparmmbP8XcSzuurXqHghMF3S908EaqEyUhgNp19br5vBVBaT2-tdlofv6NVaiTE7pvBKLTuveoiLNe8QvyWQTtXksA6KzlJ4LyCWl0l_70hZvod9oce3tUR0gLShBsIegZPdwUJYBgUHoUqtMlueo3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P4Vgdh-ZBHi15Oa16sckqAgi1awVc7C8-iVetXOrv9J6i3zxooKP8UK3tOLWZV4JxdvIJ3qIIWYnpUgMdfu9dIZtKbvXA_Q98pRyq2tCmM8g5en78OVtGm3DDm_w5coZ1DbqrZxVwa5KdJ_Yyw2jTqUUA8YINGoZfy_-RHFgBG5Ykq4e1kVtOISEnblrphm2s0T1tYxgn-eq18oOVTdSYdjOH54acyG2hBxJHbfcKXzK45RzahtnROu_Bl6fpvsvn0EGkkSNpfzN5OI8uphg8wL5zaWiqYYimQcgJ4oWF9EF1O4TxgTqtQlokqt19cjijYp8qlAqH0x_s5AFt1qieA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کنارک الان
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17517" target="_blank">📅 03:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17516">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دو انفجار جاسک
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17516" target="_blank">📅 03:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17515">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انفجار کنارک
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17515" target="_blank">📅 03:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17514">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هم اکنون شلیک موشک از سیریک به سمت تنگه @withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17514" target="_blank">📅 03:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17513">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سنتکام: سومین دور حملات این هفته علیه ایران را آغاز کردیم  امروز ساعت ۷:۱۵ عصر به وقت شرق آمریکا، نیروهای فرماندهی مرکزی ایالات متحده پس از آنکه نیروهای سپاه پاسداران انقلاب اسلامی به‌طور آشکار به کشتی کانتینری «M/V GFS Galaxy» با پرچم قبرس در حال عبور از…</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17513" target="_blank">📅 03:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17512">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دو انفجار چابهار الاننننن
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/17512" target="_blank">📅 03:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17511">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انفجار یا شلیک ، سیریک
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17511" target="_blank">📅 03:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17510">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کانال 14 اسرائیل: حمله امشب به ایران بزرگ و گستردست...
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17510" target="_blank">📅 03:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17509">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">صدا و سیما : دو انفجار در شهرهای عسلویه و بندر دیر واقع در استان بوشهر در جنوب ايران رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/17509" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17508">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سنتکام: سومین دور حملات این هفته علیه ایران را آغاز کردیم
امروز ساعت ۷:۱۵ عصر به وقت شرق آمریکا، نیروهای فرماندهی مرکزی ایالات متحده پس از آنکه نیروهای سپاه پاسداران انقلاب اسلامی به‌طور آشکار به کشتی کانتینری «M/V GFS Galaxy» با پرچم قبرس در حال عبور از تنگه هرمز حمله کردند، سومین دور حملات این هفته علیه ایران را آغاز کردند.
یکی از اعضای غیرنظامی خدمه مفقود شده و کشتی به‌دلیل آتش‌سوزی در داخل و وارد آمدن خسارت قابل‌توجه به موتورخانه، قادر به ادامه سفر نیست.
پس از آنکه ایران به‌دلیل حملات پیشین به کشتی‌های تجاری پاسخگو شناخته شد، بار دیگر فرصتی به این کشور داده شد تا پایبندی خود به تفاهم‌نامه را نشان دهد، اما بار دیگر ناکام ماند.
در پاسخ، ایالات متحده با ادامه تضعیف توانایی ایران برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، هزینه سنگینی به این کشور تحمیل می‌کند. این حملات به دستور فرمانده کل قوا انجام می‌شوند.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/17508" target="_blank">📅 03:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17507">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHVHQzY7q2T9LKUQy1mxJlBZmCSOhg8Atvxu0IArIGmRLgP_4ZbQJBdu0LWOyPS-QEidcUeOGeOq4kqXbe_P492XHvmNEbbnCSnkp1sNWMrBPSPCB2kiiar41S0wBWLi1BofWdsXyJjXZeUfbPDQhRYsl0zX2RPlr_ajNJ2OJM7qyVyGFlKqqtGcg6vALVyi1sSr8RV9SnT53vfXisdmqblpR0wz-HtVJeFyywo_TA-3yifiF0DUD1flKAL-QX2M4ThTE0TjFRLAZAIJ_izprvPfsvoEMLScblgd67PtG7Ag0UBrlqF4EOBtweIZRIVC7S7VCnyRMOWeRVjWqLK8mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندر عباس الان
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17507" target="_blank">📅 03:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17506">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اکسیوس به نقل از مقام آمریکایی:
ارتش آمریکا در حال انجام حملاتی علیه اهداف ایرانی در تنگه هرمز است.
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17506" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17505">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e4298477e.mp4?token=IDWfp5AhKmN0c6d0E0DfsIAkGaaijzDry_sqp1Dmifp34H8iJXScxSYURBoT5yOjDex2HvuNuzgQxUnLGpGMOZXZMubo0CHZNDzZ1QfG_tk7QBqfOaX-VQJYwCqdmPyREjltqHVNn2d-Ou8n_fUcDsheuXvW1YXzC0PDuN22zuSaKpXLVmctiQW9gSLeNp8JbVSpaaBpvuopnwfs6Tq7UUA7T1bDfyy6a_0Pwrt9OCBAJXiwR9c5V7hhH7BiTXDKlBEygVhBqq2k7WFfbG9TTcfv8hCL7HWWJlYKLLNXRxh9u7OSM2S8Kg_e8zLjHpRMTHplgDW0s9oUZljS5TbafA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e4298477e.mp4?token=IDWfp5AhKmN0c6d0E0DfsIAkGaaijzDry_sqp1Dmifp34H8iJXScxSYURBoT5yOjDex2HvuNuzgQxUnLGpGMOZXZMubo0CHZNDzZ1QfG_tk7QBqfOaX-VQJYwCqdmPyREjltqHVNn2d-Ou8n_fUcDsheuXvW1YXzC0PDuN22zuSaKpXLVmctiQW9gSLeNp8JbVSpaaBpvuopnwfs6Tq7UUA7T1bDfyy6a_0Pwrt9OCBAJXiwR9c5V7hhH7BiTXDKlBEygVhBqq2k7WFfbG9TTcfv8hCL7HWWJlYKLLNXRxh9u7OSM2S8Kg_e8zLjHpRMTHplgDW0s9oUZljS5TbafA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سپاه بوشهر
رو
زدن
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17505" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17504">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">قشممممم
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/17504" target="_blank">📅 03:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17503">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آبجو ۱ - ردبول ۰</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17503" target="_blank">📅 03:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17502">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17502" target="_blank">📅 03:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17501">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دینی ۰ - کنکوری ۱
@withyashar
🤣</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17501" target="_blank">📅 03:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17500">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سی بی اس: حملات به تهران هم‌میرسد
@withyashar</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17500" target="_blank">📅 03:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17499">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بوشهر رو جوری زدن که ملت ریختن بیرون
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/17499" target="_blank">📅 03:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17498">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بندر عباس دوباره زدن
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17498" target="_blank">📅 03:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17497">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17497" target="_blank">📅 03:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17496">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یه کلانتری تو اهواز منهدم شد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17496" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17495">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">منابع عربی: موشک‌ های HIMARS متعلق به ایالات متحده، که در پایگاه هوایی عیسی بحرین مستقر هستند، از بحرین علیه ایران شلیک شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17495" target="_blank">📅 02:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17494">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">برای اولین بار بعد از جنگ رمضان صدای انفجار در آبادان به گوش رسید
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17494" target="_blank">📅 02:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17493">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8mKDNdTfUgIMluSpyUabjHR6Ojp23aPr2yAbvztS-SHW9J6y3e8czGe-YUeA3JKc0wXsjIIocCokdhw6N5r6RD0K6iCEjXisilhe9-UZU3nJnaYFCgubnSkfcz69T8ugifudGuNO5VfqLPTOZvRzOdKqGbwADyMnIKnQBVRYHZuZnZZ24MVi4BKQCXts_C5BKu9hPIki3o9ZKy1yeN5apljQBDZzEdlbQbLiE-9MarID5_iHoQSdf8kAtcxdwwL9V7X_nxSOXT2UzYjcT8tc39yo9LrFYMMGZmGasTN1ZJB87xBVOHaxAW9GO_xt3GBtWEjilxK-kXq9IDR1m6XAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بند دیر
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17493" target="_blank">📅 02:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17492">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بندرررر عباس
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17492" target="_blank">📅 02:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17491">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گزارش انفجار اهواز
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17491" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17490">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گزارش ها از حمله آمریکا به عسلویه ،  بندر دیر و بندر کنگان
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17490" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17489">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گزارش انفجار بوشهر
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17489" target="_blank">📅 02:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17488">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer"><a href="https://t.me/withyashar/17488" target="_blank">📅 02:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17487">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">العربیه :هم اکنون تماس وزارت خارجه پاکستان با دو طرف برای کاهش تنش در منطقه در حال انجام است
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17487" target="_blank">📅 02:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17486">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">منابع عبری : ترامپ چراغ سبز رو به نتانیاهو داده.
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/17486" target="_blank">📅 02:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17485">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">منابع عبری : مجتبی خامنه‌ای شخصا دستور بسته شدن تنگه هرمز و لغو مذاکرات را صادر کرده است
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17485" target="_blank">📅 02:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17484">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کاتز: ارتش اسرائیل توسط من و نخست‌وزیر نتانیاهو دستور دریافت کرده تا برای یک حمله مستقل به ایران آماده بشه.
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17484" target="_blank">📅 02:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17483">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">باراک راوید خبرنگار  آکسیوس:
حرکت امشب سپاه علنا به معنای رد کردن درخواست ترامپ برای اعلام باز کردن تنگه هرمز است
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17483" target="_blank">📅 02:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17481">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تابناک: گزارشات تایید نشده از حضور تکاوران ویژه دریایی سپاه  "S.N.S.F" به صورت تیم های غواص مین ریز  و قایق های تندرو در تنگه هرمز مخابره می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17481" target="_blank">📅 02:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17480">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کانال۱۴ عبری
: مذاکرات به بن‌بست خورد؛ ایران یه پیام جدید برای ترامپ فرستاد و گفت: از این لحظه تنگه هرمز رسماً بسته‌ست.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17480" target="_blank">📅 02:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17479">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انتشار این پست و معرفی من تنها کمک شماست
🙌🏾
🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17479" target="_blank">📅 02:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17478">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">احساس میکنم ترامپ داره فکر میکنه که یه توییت جانانه بده
🤒
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17478" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17477">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سپاه دوباره به یک کشتی‌دیگه حمله کرده
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17477" target="_blank">📅 02:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17476">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">راوید، خبرنگار اکسیوس :
یه مقام ارشد آمریکایی گفته سپاه یه موشک به سمت یه کشتی تجاری که داشت از تنگه هرمز رد می‌شد شلیک کرده و اون کشتی هم مورد هدف قرار گرفته.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17476" target="_blank">📅 02:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17475">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">احساس میکنم ترامپ داره فکر میکنه که یه توییت جانانه بده
🤒
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17475" target="_blank">📅 02:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17474">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هم اکنون در تنگه هرمز و دریای عمان سیگنال های رادیویی نظامی به صورت گسترده و غیر عادی در حال مخابره شدن است.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17474" target="_blank">📅 01:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17473">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انتشار این پست و معرفی من تنها کمک شماست
🙌🏾
🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17473" target="_blank">📅 01:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17472">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">انتشار این پست و معرفی من تنها کمک شماست
🙌🏾
🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17472" target="_blank">📅 01:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17471">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شبکه ۱۴ عبری :  ارتش آماده است،ترامپ ممکن است هر لحظه چراغ سبز حملات به ایران را نشان دهد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17471" target="_blank">📅 01:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17470">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دیدبان های اتاق جنگ میگن موشک ها رو هوا رهگیری شدن توسط امریکا و سپاه هم زورش‌ گرفته و گفته زدم کشتی رو !
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17470" target="_blank">📅 01:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17469">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">هر کسی هم که که میخواد یه کاری‌کنه زهرمارش میکنید ! بد مردمانی‌هستین</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17469" target="_blank">📅 01:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17468">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هم اکنون شلیک موشک از سیریک به سمت تنگه @withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17468" target="_blank">📅 01:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17467">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">هم اکنون شلیک موشک از سیریک به سمت تنگه @withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17467" target="_blank">📅 01:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17466">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وقتی‌نمیتوم دایرک رو باز کنم لیاقت ندارن بعضی ها همیشه به چوب همینا مسیوزیم !</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17466" target="_blank">📅 01:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17465">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer"><a href="https://t.me/withyashar/17465" target="_blank">📅 01:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17464">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">میرم فوتبال میبینم خبرم نمیدم</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17464" target="_blank">📅 01:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17463">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17463" target="_blank">📅 01:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17462">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17462" target="_blank">📅 01:28 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
