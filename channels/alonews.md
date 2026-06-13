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
<img src="https://cdn4.telesco.pe/file/f_qNT3E3MIMIrLfMkDfQau8nTg45wvoAADe5ExpfLPCAs0QKHSu82xi_FemrUJIg35TR07mwYNB7DFgOlplcNB_UP0xOK2TBUqb0EukKp7mXIX_cxU_O71eFwY095VJXJb3vccU0hQkifq-x_yBRio3cn3sb_vG6aVsne93nBTVsmP3u50_PTDw-IGvbY-EruJvgoVt89b6_fxvMO2trSNGR8EHd-ImynaqxoxlTBdRntjn3LRFV0ZRUgmtz4GLBq03u1w7Yg7OcbPvDaHVHZTqJXouPFe740HsZsttZ0CrFs0ZcAwV2NYpyFTQFyrXSyxaZPJqQI3rnmoGaPn0m2Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 981K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 11:49:06</div>
<hr>

<div class="tg-post" id="msg-127573">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yw02O7T0DKK_4Pa4oKt4oOd3F9sZa10SStd7AujpWI2Dk43jhegl6yxXmKasIPSnfdKS2p0TX47jYpdCfRKtUsZZaLn0AR3Hpz2064Rv_UvYbcWtbGwfIviFVggloMOqGdBBb0mcdwkh6UvV-v63EoCQyK7ohc5qus7msbpZVMIXZnmkRqFE5Rrxd8F8fP6eOA8xDhstxcf87Ofqt1g2mQBIOM2K5sj2ZXqTzpbc-L9KlGFcsyFq5oaWLs5gSZE_DnUoM2fAyzz31uFeEj8o3tA2rmUwIfvtpjUiB2yTVIC1D-OBrtuGEKCz3XbFBPOTgKcT2fGCZH0TvjXtMpZa2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه سی‌ان‌ان به نقل از پنج منبع آگاه از سازمان اطلاعات آمریکا: ایران در هفته‌های اخیر تلاش‌های خود را برای پلمپ انبار اورانیوم با غنای بالا، به طور چشمگیری افزایش داده و عمداً دهانه تونل‌ها و ورودی‌ها را با انفجار مسدود کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19 · <a href="https://t.me/alonews/127573" target="_blank">📅 11:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127572">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
آخرین قیمت دلار ۱۷۲ هزار تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/127572" target="_blank">📅 11:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127571">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه داری آمریکا اعلام کرد که با توجه به روند پیشرفت مذاکرات، انتظار می‌رود توافق صلح با ایران «احتمالا تا پایان همین هفته (میلادی) یا اوایل هفته آینده نهایی شود.»
🔴
وی درباره پیامدهای جنگ علیه ایران افزود: «ما درک می‌کنیم که در ماه‌های اخیر شرایط سختی سپری شد و افزایش بهای انرژی بخش زیادی از رشد دستمزدها را بلعید، اما ما در حال عبور از این وضعیت بحرانی هستیم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/alonews/127571" target="_blank">📅 11:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127570">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از منابع: ارتش آمریکا برای اجرای مأموریت زمینی به منظور تصرف اورانیوم ایران در اصفهان، تجهیزات را سریعاً آماده کرد
🔴
اما ترامپ پس از آنکه به او هشدار داده شد که این اقدام به احتمال زیاد منجر به واکنش خشونت‌آمیز ایران خواهد شد که باعث طولانی شدن جنگ و افزایش بی‌ثباتی اقتصاد جهانی می‌گردد، این گام را به‌طور موقت متوقف کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/alonews/127570" target="_blank">📅 11:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127569">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b6b203f35.mp4?token=Zt8TDRy0joehaxxqX-N0EI1_oL1A_jVtkQDzpArcRXc-Ib5gclqylVMjJiWRm4fhaQvxTGQh6n07sSLDtiF6bd4uaBdeundGLF4s8J23_5HXlDHpuf0MCgekd3AoYaOTULUTj8U5_dS4RuJObxXjugB1ubTTf7iCCsFIGcGSM9bH32YGzrQ2gZuZGWob2rCZBS21-7-z5cpjdcwXG64QCT5og0wlxTP2wVXxTu4tAGpgHUviq1zXwwzRaKIKLe6bbBNnhI6UK7HZBjiCkCIbg-gr0MokPjeDAdQkDChIUtd9_Z_w4cGRz6vNeObKWwRePpkj_q8So14INmsNq07suA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b6b203f35.mp4?token=Zt8TDRy0joehaxxqX-N0EI1_oL1A_jVtkQDzpArcRXc-Ib5gclqylVMjJiWRm4fhaQvxTGQh6n07sSLDtiF6bd4uaBdeundGLF4s8J23_5HXlDHpuf0MCgekd3AoYaOTULUTj8U5_dS4RuJObxXjugB1ubTTf7iCCsFIGcGSM9bH32YGzrQ2gZuZGWob2rCZBS21-7-z5cpjdcwXG64QCT5og0wlxTP2wVXxTu4tAGpgHUviq1zXwwzRaKIKLe6bbBNnhI6UK7HZBjiCkCIbg-gr0MokPjeDAdQkDChIUtd9_Z_w4cGRz6vNeObKWwRePpkj_q8So14INmsNq07suA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عباس عراقچی: مسئولیت مذاکرات توسط نظام به قالیباف سپرده شده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/alonews/127569" target="_blank">📅 11:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127568">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
هشدار سیلاب و تگرگ در ۹ استان؛ گرمای غیرمتعارف در شرق کشور
🔴
امروز (شنبه ۲۳ خرداد) شمال غرب کشور به‌ویژه استان اردبیل با بارش‌های سنگین و خطر سیلاب مواجه است.
🔴
همچنین در نیمه شرقی آذربایجان شرقی، ارتفاعات البرز، مازندران، سمنان، گلستان و بخش‌هایی از خراسان شمالی و رضوی رگبار، رعدوبرق و تگرگ پیش‌بینی می‌شود. فردا از شدت بارش‌ها کاسته می‌شود.
🔴
وزش باد و گردوخاک در تهران، قم، خوزستان و یزد ادامه دارد و گرمای غیرمتعارف در نیمه شرقی کشور ماندگار است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/127568" target="_blank">📅 11:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127567">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
تحلیل روزنامه ( خراسان) نزدیک به قالیباف: تفاهم ایران و امریکا قرار نیست اختلافات را حل کند؛ فقط یک فرصت است که طرفین خود را برای جنگی دیگر آماده کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/127567" target="_blank">📅 11:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127566">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7YfEeOY4O6ZLQJPLDzr5_vIXmIZImgrZ7H5_x_XdF_A0Cic2CwJ6qK9K3vILC87S3hFcS2UfxxD_G7pThY9Td5PxVCgR41FkSL6z-cQraHI1wmEn0pkcDFEHplShQxphHxDiRhr2S4mgSaa1tYGqT9Facgsko4X1d3ujus2uPF65izpLoRBMLyKbgcN4zwjunFlqisNeE2rqh0IYdkMXLBaFbW35gdrmwibSWMmm5ckwjlsSNGw1wb32fElSmhu_G3T0vbCyeBLFRDkAWk3bp_yXC5kybSjwHqLCvmgzYmmsj9kdHg9P8nXmR45Aea2S_zxFgjuBKV18sSv5IOZDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۸۷.۳۳ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/127566" target="_blank">📅 11:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127565">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
خبرنگار الجزیره: حمله پهپادی اسرائیل به شهر آرامتا در شهرستان جزین در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/127565" target="_blank">📅 11:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127564">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
یک مقام ارشد آمریکایی به نیویورک تایمز گفت: «میانجی‌گران و مقامات نظامی ایرانی تأیید کردند که رهبر ایران از توافق راضی است».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/127564" target="_blank">📅 11:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127563">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49ecd56daa.mp4?token=su8-UIe9xclz9rh56FyJQeS8WhRdemQA9oAUZiOZf1zhme0bXUYLqo0_eHkhdR95sBdM_sTRe-8oaDVmgmxXiMKWFi1kLVQCx0tA_6i-1K0B1rCRxFEF8Xh1QCRIKCeqgQoxipzIpL7fWaAISdzHPu_UtmWD2mMaYxauIA43yjadhLx8JyfC-2o-o26822UI6sxSzUXm5_uSjMelLsIO0fV-_T9eU-aCDZgR9U2diWMssqHjeje4LWWoaHxJDctG-q-xIUI2_bUdQaoy_d_5Ny1j8GgkmjKnPKYtNgD7CtsKJlx2BnFM1XQh1o3mnqa3Onqq2uE4y3345kplsrO8GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49ecd56daa.mp4?token=su8-UIe9xclz9rh56FyJQeS8WhRdemQA9oAUZiOZf1zhme0bXUYLqo0_eHkhdR95sBdM_sTRe-8oaDVmgmxXiMKWFi1kLVQCx0tA_6i-1K0B1rCRxFEF8Xh1QCRIKCeqgQoxipzIpL7fWaAISdzHPu_UtmWD2mMaYxauIA43yjadhLx8JyfC-2o-o26822UI6sxSzUXm5_uSjMelLsIO0fV-_T9eU-aCDZgR9U2diWMssqHjeje4LWWoaHxJDctG-q-xIUI2_bUdQaoy_d_5Ny1j8GgkmjKnPKYtNgD7CtsKJlx2BnFM1XQh1o3mnqa3Onqq2uE4y3345kplsrO8GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/127563" target="_blank">📅 11:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127562">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/453f586f69.mp4?token=qCIKp9hPgVHzyucCnGWqbo8fc65opjjdIcpVWczWC-1hOhNak-0dKqBrwDf1CApbKDO1FYuanrqp7XngxzYcXBTpQ3ErmHHkr1WszUJw42e3ALtV11fg0Z-1zTuH4x1VxXTU2UVV3UDVsGX4DKnOM5R3V5JrcK94nXQpotcXTGZTx4b-95rdW0qQvpBLID7PayO7jwxmqEiGP5YrSbj4cVDB4_6mkEqJoI6R_RdbWxcHQG-M7T9NGa9uxyU8DwlqrsJps-kE-EhB5RI-OlVwUHdbiH4D_-5N6hsOLFhgyth6fjCXr0dBhHhzkm7gvsMpcscE3t_Za5lIqP5NUPEiWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/453f586f69.mp4?token=qCIKp9hPgVHzyucCnGWqbo8fc65opjjdIcpVWczWC-1hOhNak-0dKqBrwDf1CApbKDO1FYuanrqp7XngxzYcXBTpQ3ErmHHkr1WszUJw42e3ALtV11fg0Z-1zTuH4x1VxXTU2UVV3UDVsGX4DKnOM5R3V5JrcK94nXQpotcXTGZTx4b-95rdW0qQvpBLID7PayO7jwxmqEiGP5YrSbj4cVDB4_6mkEqJoI6R_RdbWxcHQG-M7T9NGa9uxyU8DwlqrsJps-kE-EhB5RI-OlVwUHdbiH4D_-5N6hsOLFhgyth6fjCXr0dBhHhzkm7gvsMpcscE3t_Za5lIqP5NUPEiWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو هند، یه هواپیمای روسی نظامی آن-۳۲ سقوط کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/127562" target="_blank">📅 11:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127561">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpQ_sIcH8bZsxDZb6KHC4pj-kXminM9ry1bBvGV44AVVWxmXfRMClN1RvnpwhVCd2U__eTS7HhUBcYmjB3D8WRUXnyB79hoB4dim9vSubnwaVloQDIg_8m9iP4JIzSSPGnReeEsxRmohiKZ4ceSZwiGmp1MEn3-vBYFKRFrMeuf0oeb3SHGZwigkk1d4oIGXNbzuzX30gYhvDG9IW3Hyvu0MmDPP8zzgFIkEEj5GE1guGI9AK3jHXvQmP_wgCeOuFYRh-r71qlE67KCymCWfogv3C0loLq4SSv_19FN8NAve19CHq0UHrgGKlxfwBXURtt-u63iVcglGSiuc-joZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: مذاکره منجر به جنگ نمیشه بلکه مقاومت منجر به جنگ میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/127561" target="_blank">📅 11:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127560">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
روزنامه وال‌استریت ژورنال به نقل از منابع آگاه گزارش داد که سفر یک هیئت دیپلماتیک قطری به تهران، به چند روز حملات متقابل میان ایالات متحده و ایران پس از سقوط یک بالگرد آپاچی آمریکایی پایان داد و رئیس‌جمهور آمریکا، دونالد ترامپ، را متقاعد کرد که حملات شدیدی را که علیه ایران در نظر گرفته بود، لغو کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/127560" target="_blank">📅 11:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127559">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyAsqVRP1JbTXvEgUcHPxnyoJheaqTi_oPQL9Alsi_XGT1dLy0NmF_jCl7NIKeTHr1ViHdHjt9hpJ_IPfLmgLgW0scK8yuQqVbm1PRbwtPl68XBQ25YJ9yEWqE--P4rBy-VN4xUeaomU0mY6KhfmfSuuPryn8ZQpvWcGXLAss_-_OIFG6s0FH82w2Yp3WKA_wvjibSbaP3bq5p-MKpcKU86bF7ntJ8hckSZQHImfoY-TA_u7PfwIlUzgLcuzBp3cHT9C1dgks6NrW7AmT2tCdqrXKJVTfTJFfXbMMH8HkI0tovK-Ly_bgttAcC_Szg7h97GJsiMj9gUNi5Ebw_vsZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سرمایه ایلان ماسک حالا از مجموع ثروت ۴ فرد ثروتمند پس از خودش بیشتر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/127559" target="_blank">📅 10:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127558">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
لیبرمن، وزیر جنگ اسبق اسرائیل:
توافق، پیروزی ایران و فاجعه‌ای برای اسرائیل است
🔴
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، مسئولیت کامل این وضعیت را بر عهده دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/127558" target="_blank">📅 10:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127557">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سی‌ان‌ان: ایران بخش‌هایی از ذخیره اورانیوم بسیار غنی‌شده خود را با ریزش تونل‌ها و مین‌های انفجاری در اطراف ورودی‌ها مسدود کرده است. این اقدامات در پی نگرانی‌ها از احتمال عملیات آمریکا برای تصرف این مواد، دسترسی به اورانیوم را به‌طور قابل‌توجهی دشوارتر و خطرناک‌تر کرده و تلاش‌ها برای حذف یا نابودی ذخیره تحت هر توافق آینده را پیچیده می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/127557" target="_blank">📅 10:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127556">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I28SQLUTpbskCrsgVFdsO6Un4Ac_0DF07gOYD-r9V16-yT8K8tHYcodCVSSv7lRoz9sS7BJ_GdRH4jltky61ZVDUgbJQhuasOl5qpyNeqgUKg11Nh6dap6UV2LKiedDdM9ZF7qmsOAqTrMZp2k69CL_mbXwkgooeSMnHzZFJiSjAbyjcSmBu-0ciNMJm1fYtEEl2SqKKJgqVDT3s0KGrUvomK3bor5ZjimzUiv9V5TOvuaRb_EOccEnKBg7WI0MreLWGhtA3BXOx5V1hjhAZCC6G8v1fov3tT6xLRLGgEkxlnc28Cc11Tra4M2Iun0UZqMcAJoZufi5cWmonWCskww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید خبرنگار آکسیوس: نتانیاهو امیدوار بود که جنگ منجر به تغییر رژیم در ایران شود، اما رقبایش اکنون او را متهم می‌کنند که با پذیرفتن شرایط آمریکا، اسرائیل را به «دولت دست‌نشانده» تبدیل کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/127556" target="_blank">📅 10:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127555">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رویترز: ونس توافق‌نامه صلح با ایران را امضا خواهد کرد
🔴
خبرگزاری رویترز به نقل از مقامات آگاه ادعا کرد که معاون رئیس جمهور آمریکا توافقنامه صلح با ایران را امضا خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/127555" target="_blank">📅 10:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127554">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhWoRzU7ZcKjrn7qjEi8QWDc_PKkCVpSyBq7M9NF80lrG_ETBz3SDoA8EcAt5U1S5_OQ1lGUbsclOqtNsSvTqRGSnVziuq-wmaL8tQQrseKPS4xvPcx1-lX1pM6Dii4h399tDZwIJMfxge-ENgambq0NZ07EmCDGqUik7VOOp_w82ZyRYTIhv5JddoYLM40vEfQAwxxAsTLWbnTSZLDIf3ExMVshPmcP8L1dnxZSSdAKPd-aRhhSWAUJ5TKNZyLwjBhP-dlvh4yfHFYektSWCD7hpE1X4zTIEB1OHneMaWdrivLf2bTB6C9ReI9F2ZHsjkOZYdRzNO8KZjB3eqQKFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بورس باز نشده ۹۸ هزار واحد رشد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/127554" target="_blank">📅 10:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127553">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
آحارونوت: احتمالا توافق تهران-واشنگتن شامل آتش‌بس در لبنان هم باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/127553" target="_blank">📅 10:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127552">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل، هشدار فوری تخلیه برای ساکنان ۲۰ روستا در جنوب لبنان صادر کرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/127552" target="_blank">📅 10:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127551">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجار در دزفول
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/127551" target="_blank">📅 09:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127550">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
طبق گزارش شبکه المنار، وابسته به حزب الله، نیروی زمینی ارتش اسرائیل در پوشش گلوله باران گسترده توپخانه، حمله خود به سمت جنوب شهر نبطیه، پایتخت حزب‌الله در جنوب لبنان را آغاز کرده است.
🔴
خودرو های زرهی اسرائیلی به به صورت گسترده در حال هجوم به سمت جنوب شهر نبطیه مشاهده شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/127550" target="_blank">📅 09:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127549">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joaMm_Xb0OQUoHXStL6PWGsKIQArCxIXUg68l0PlGm6DdHY2rq_aD-LP5YhoKZQS35D44lBfF-INNcb24reVTw-TlvPSmbKwtLZmJO-P0RK8ZZACNHFFoUnMyN8du6ufL0qXTFX_RnwK9e97ecFifJTJqVh1-iNKrlPxBfUTa3MRVzOEdus7lxaXpKAU_kFqE5vHnGZWXWaYEiLkzynz6srIpIw8d3zuu8j_-bX1Y3KsNx_5fRP_3zkrUtED0J-krzo1hxrPPtqHvgKTnwMGcuZYvC6SIe-_4I25FPOqMYAaTVsSLniPP38gb1YUS6XkF6Y_tWs3wTQvYc_yiOL9Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشف ۴۱۸ کیلوگرم تریاک در یزد مأموران پلیس مبارزه با مواد مخدر استان یزد موفق به کشف ۴۱۸ کیلوگرم مواد مخدر از نوع تریاک در شهرستان یزد شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/127549" target="_blank">📅 09:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127548">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
کانال ۱۲ عبری از رصد ۳ راکت شلیک شده از لبنان به سمت شهرک‌های صهیونیست‌نشین «المطله» و « مسگاوعام» در شمال اسرائیل خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/127548" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127547">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
دانشگاه شریف از امروز به روی ۴۵۰۰ دانشجوی مقاطع تحصیلات تکمیلی باز شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/127547" target="_blank">📅 09:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127546">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
نیویورک‌تایمز: ایالات متحده به شرکت آنتروپیک دستور داده است که دسترسی تمامی اتباع خارجی به مدل‌های پیشرفته هوش مصنوعی خود، «Mythos 5» و «Fable 5»، را مسدود کند و دلیل این تصمیم را نگرانی‌های مربوط به امنیت ملی اعلام کرده است.
🔴
آنتروپیک اعلام کرد که ناچار شده فوراً دسترسی را غیرفعال کند؛ اقدامی که حتی کارکنان خارجی این شرکت را نیز تحت تأثیر قرار داده است. این شرکت همچنین این وضعیت را «یک سوءتفاهم» توصیف کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/127546" target="_blank">📅 09:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127545">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فوری/ ترامپ میگوید ایالات متحده امریکا رهبر گروه «ترن د آراگوا» را به قتل رسانده است.
🔴
متنی که ترامپ منتشر کرده:به دستور من، فرماندهی جنوبی ایالات متحده یک عملیات ضربتی سریع و کشنده انجام داد تا «نیِنیو گوئررو»، رهبر بدنام گروه ترن د آراگوا، که یکی از خونخوارترین سازمانهای تروریستی روی کره زمین است، با موفقیت ترور شود.
🔴
پیش از بازگشت من به دفتر، جو بایدن مرز جنوبی ما را به روی میلیونها جنایتکار غیرقانونی گشود و به این ارتش بیگانه اجازه داد تا با مصونیت کامل، شهروندان آمریکایی را تجاوز، مثله و به قتل برسانند.
🔴
در طول مبارزات انتخاباتیام، قول دادم که این هیولاها را از کشورمان بیرون کنم و برای خانوادههای کسانی که به قتل رساندهاند، از جمله «جوسلین نونگارای» ۱۲ ساله عزیز، «لیکن ریلی» ۲۲ ساله و بیشمار روحهای پاک دیگر، عدالت برقرار کنم.
🔴
با این اقدام، ارتش ایالات متحده برای آنها، خانوادههایشان و عزیزانشان تلافی کرد. در اوایل دوره ریاستجمهوریام، به قولم عمل کردم و ترن د آراگوا را به عنوان یک سازمان تروریستی خارجی تعیین کردم، هزاران جنایتکار شرور را اخراج کردم و علیه کارتلهایی که مدتهاست با شهروندان ما میجنگند، در حالی که رهبران ضعیف آمریکا را درمانده و دفاعی رها کرده بودند، اعلام جنگ کردم. این اقدام با هماهنگی نزدیک با دوستانمان در ونزوئلا انجام شد که با آنها بسیار خوب کار میکنیم.
🔴
در نتیجه، تروریستهای ترن د آراگوا دیگر در ونزوئلا یا هر جای دیگر پناهگاه امنی ندارند و تحت رهبری من، این قاتلان بیرحم و اربابان مواد مخدر را در هر زمان و هر مکان پیدا خواهیم کرد و به اعماق جهنمی که به آن تعلق دارند، خواهیم فرستاد. خدا آمریکا را حفظ کند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/127545" target="_blank">📅 09:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127544">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
گزارش‌ها: یک فروند A-10 آمریکایی به پایگاه بازنگشته است
🔴
منابع رصدی گزارش داده‌اند یک فروند هواپیمای تهاجمی A-10C Thunderbolt II با شماره ثبت 78-0614 پس از عملیات اخیر به همراه اسکادران خود به پایگاه بازنگشته است.
🔴
بر اساس گمانه‌زنی‌های مطرح‌شده، احتمال دارد این همان هواپیمایی باشد که در جریان عملیات نجات افسر سامانه‌های تسلیحاتی یک فروند F-15E Strike Eagle هدف قرار گرفته و توسط ایران سرنگون شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/127544" target="_blank">📅 09:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127543">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
یدیعوت آحارانوت به نقل از منابع اسرائیلی: اگر ایران در صورت هدف قرار گرفتن ضاحیه جنوبی بیروت به ما حمله کند، ما تلافی خواهیم کرد و اتحاد جبهه‌ها را نخواهیم پذیرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/127543" target="_blank">📅 09:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127542">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
کیهان: اگر تنگه هرمز را باز کنید دشمن دوباره حمله می‌کند!/ هیچ آدم عاقلی نقطه قوت خود را پای میز مذاکره نمی‌برد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/127542" target="_blank">📅 09:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127541">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jV3LHvz-zwNDwVDOy1truon7o5m2veaJE8kL7z8NM3k95q362Omf0x4ejo-g_WpEGQdBmIJHk9M7gZ7ejWIX5X_MK-gzOVi24mSp4_DGEUcJDu5EkYdTjwc0YSGRDPN3uxVvOamJpEpSDc-9Qs1DlaY6TUm9GgWFReY66khLRHe95hdQl866AXxChPUDV7JhgYNt7kSDUqUCfyvq_bb4giLQgbr-A07rpHW4dyzTvlF5az-rv8Bh-eEYYMfKMsw8PhWh8LwBSLygQucn7btke56boaMbNnxbidEWwc1pBrmvcKSk602WLZfnWzFPcvMbv3Tg8ynqb3s_Djhl3Qlwig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کارآگاهان پلیس آگاهی شهرستان آستارا، با اقدامات فنی و اطلاعاتی نامحسوس محل احتکار و دپوی غیرقانونی کالا‌های اساسی و موادبهداشتی را شناسائی و افزون بر ۱۵۳ میلیارد ریال ارزاق عمومی در آن کشف کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/127541" target="_blank">📅 09:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127540">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سی‌ان‌ان: ایران در بحبوحه نگرانی‌ها از عملیات زمینی ایالات متحده، بخش‌هایی از ذخایر اورانیوم با غنای بالای خود را با تخریب تونل‌ها و کار گذاشتن مین‌های انفجاری در اطراف ورودی‌ها مسدود کرده است.
🔴
این اقدامات دسترسی به اورانیوم را به طور قابل توجهی دشوارتر و خطرناک‌تر کرده و می‌تواند تلاش‌ها برای حذف یا از بین بردن این ذخایر را تحت هرگونه توافق آینده، پیچیده کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/127540" target="_blank">📅 09:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127539">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزیر خارجه فرانسه: ایران و آمریکا از فرصت موجود برای دستیابی به توافق استفاده کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/127539" target="_blank">📅 08:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127538">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
رویترز: نیروهای آمریکایی چندین پهپاد تهاجمی یک طرفه ایرانی را که به سمت تنگه هرمز در حرکت بودند، سرنگون کرده اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/127538" target="_blank">📅 08:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127537">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrYeqYuSXfDl6A87YSTDTrPfvjtLUdkjXApPXUXOgHIKNIsBpN0MBg_6p5JGotEkdml8unw6lqn4EO5LIG-5fJRWAZ8Kg4S1sWfWxTUTqri5BMpMqgogkEAmNqd_TeszUtPU5jfKhv-JHjs2TYIR7v945IIO8hzUpoqbOzObpCirFMczxubP-rCB5grSrU50f8f-QnWXP1pS1sr0Q6wdHG7xvjcUC9SN48P1N25tR_pPod7ivHUEyHukpu7XO8JU9jrHfrUssNkJyreU87WjGmYQjN0jxCAwhVH9QG4SXs5xTinnMx5hxG_gWoKc04tEh2TEpa1vBUZjKmAex6XCeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رافائل گروسی برای دبیرکلی سازمان ملل اعلام آمادگی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/127537" target="_blank">📅 08:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127536">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
سی‌بی‌اس: کاهش ۳ درصدی قیمت نفت در پی خوش‌بینی‌ها نسبت به توافق تهران و واشنگتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/127536" target="_blank">📅 08:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127535">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: رفع تحریم در ازای اقدامات ایران در خصوص برنامه هسته‌ای صورت خواهد گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/127535" target="_blank">📅 08:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127534">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpbsMBcvGfja91a23Tsn6SapfKlJAT12yUn5PU1ujmZRim3CKULI46ywPG1Q6VvA7qkpY_gCvzrPyRTqSh7v5vFgTQ6_zLf73kYgkvz_BHHuBBSM6PIGZtdChENoNqwpLWYME-3xPScxtMq19pLpOVn3vfJM69QXCYY2v31c54OPJMCmU2FPL1go8MJcbzzyHCbTAO9DLwK3nrvSLtROD422YCO1PdXpgS5zwm-mUZFPtKyzsO6eqHSyQn6TchdJIyKaZM3EoIj8bCYUTW-g3Ow7aSEZnhte6-qIn6FNNdvuhYyghU7N_4f9g_lzNTigAULfCLZaynLj2gq_idTPbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبر شوکه‌کننده رسانه فرانسوی؛
کشف جسد در نزدیکی محل تمرین تیم ملی
🔴
به گزارش خبرگزاری فرانسوی RMC، دفتر دادستانی تیخوانا در تماس با خبرگزاری فرانسه توضیح داد که یک گشت نظارتی، در صندوق عقب یک خوردو، جسدی در حال تجزیه را کشف کرده است.
🔴
این کشف وحشتناک در پارکینگ سوپرمارکتی که مستقیماً روبروی ورزشگاه کالینته، جایی که تیم ایران از زمان ورودش در روز یکشنبه روزانه در آن تمرین می‌کند و با ماشین یک دقیقه از هتل فاصله دارد، رخ داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/127534" target="_blank">📅 08:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127533">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWhgFVQ7CKtffOauvGM2KUvqPCEKuHrfMIXGhcmAomRgVdFxPQXwJK-KM8ugU4omijp412wluu7byF27GqzradGJSxT1-GP3vl8HUFvNpUF4_S-F4nKSA3uAewzLSkbt00P_RdQIpl228WPiccIrsW-1ggnJ8lvilMGZ_ua3JGhAeI7_484vHFq-G1ElsfyvU9wsHlPPovPb2-BS_O_z8XHHCJNt51Y8Ha-2_EYSDzwf6iWIS_neIZq6n7WxCogm3viQFFXJzyMKZUS7qffghIyXP8eVk7SVEVwixl9lqfLm7ZuZCrr6dxokTgYS35IgzgBYiARHDdVgyuOtC80BMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واشنگتن پست: بانک جهانی اعلام کرد: جنگ ایران رشد اقتصادی جهان را به ضعیف‌ترین سطح خود از زمان همه‌گیری کرونا خواهد رساند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/127533" target="_blank">📅 08:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127532">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
الحدث به نقل از یک منبع بلندپایه: امضای «اعلامیه اسلام‌آباد» به‌صورت غیرحضوری (از راه دور) انجام خواهد شد و دیدارهای ژنو نیز به‌طور موقت به تعویق افتاده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/alonews/127532" target="_blank">📅 08:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127531">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
اکسیوس:
برخی در واشنگتن معتقدند حتی اگر توافق اجرایی شود،
نتانیاهو ممکن است بازهم بتواند نقش یک اخلالگر را ایفا کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/127531" target="_blank">📅 03:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127527">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtaRIsLy0-bjvoH-6dHpT4Dujth_zgluhgtAzNi3GjIHeuk1abXkRgjyB0kaqx309hCkYU4Qz1l8GvgakoMkEpFE7hYFNONSEdS1uoQ5h8vR0rrTlw0HZYGy-JhM-oyBCgmwT04RMg5J2twZZYZiWSJuq7SJQMFzlKnRy9TzB74hhhNBpjyLM6hx1JxjrC-XoICQIf_X9gTySgLbCMyOEuTbAGGA5RNlJIswudBTJoNpt5mwPEMoKE0tzaEx7sObV2ugd6Z2cRgSpIJWJSti_EiGYgbdDfK8ndLiQpF9W5618_dokuGTOywCdNysOs64MCTA5JEJUnkwEYJ2AwRmtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/انفجار در تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/127527" target="_blank">📅 03:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127526">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
فیلد مارشال محسن‌رضایی: آمریکا با آزادسازی ۲۴ میلیارد دلار از دارایی‌هامون موافقت کرده؛ اما ترامپ نمیخواد اونو علنی کنه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/127526" target="_blank">📅 02:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127525">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c23cc9050.mp4?token=hErGu0ZNpp4L4fdhuFNl7nw7UpmDFc02dr1d1CkPQWMrRD12g09sMYf3YVRDL7GYn1FHHgG3vHaTQpFSQLYJVWhieNmHSxOtWNKNowwJX3OgWvFcinSkkfFzGabMA66G-bi4ubG5YCCvRJGLl5dKu04jOa1GUTzwss4fFSOgSJLRqi_Tp0-42kvMKxwzqwywDxnEn9MqL57JZWLFaVcRf8halNZL_ozaAhkuTLjTF11jyDdZXJq-oprRbhLNcL930lr_1EifzXaDxEbCZRvz4i9KNq18o__lx4Z574NtlMVtwsVjoTm1i5E7C9akx6RE1eP8aGZcDPHx-JfvYC_nsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c23cc9050.mp4?token=hErGu0ZNpp4L4fdhuFNl7nw7UpmDFc02dr1d1CkPQWMrRD12g09sMYf3YVRDL7GYn1FHHgG3vHaTQpFSQLYJVWhieNmHSxOtWNKNowwJX3OgWvFcinSkkfFzGabMA66G-bi4ubG5YCCvRJGLl5dKu04jOa1GUTzwss4fFSOgSJLRqi_Tp0-42kvMKxwzqwywDxnEn9MqL57JZWLFaVcRf8halNZL_ozaAhkuTLjTF11jyDdZXJq-oprRbhLNcL930lr_1EifzXaDxEbCZRvz4i9KNq18o__lx4Z574NtlMVtwsVjoTm1i5E7C9akx6RE1eP8aGZcDPHx-JfvYC_nsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توهین‌ناموسی محمدحسین میثاقی نسبت به منتقدان تیم قلعه‌نویی
@AloSport</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/127525" target="_blank">📅 01:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127524">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
آکسیوس: به نظر میرسد نتانیاهو در جریان تماس تلفنی با ترامپ متوجه شده که نمیتواند مانع از انعقاد توافق با ایران شود‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/127524" target="_blank">📅 01:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127523">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef6825a80c.mp4?token=OJ3ZoeU2UpfOk2NlKNxINVJXE3jBuF-2a6jCxfmY5bdR3CUMaicqn0CQOiwKeZRzGDPLqA2aHrKE2Xu8UtMGb3tv3D8dBIht6l2wVBnEwEy_SiMj058DyaqRC-B5urq5kfmcT4VhVZE2GEN_MeSu1pfyjuwke7gvuWxrdX12JDYhkV8a_V98MBbm1HS9cN1ji_b75zIxvBWjB14-kXYqhZstJNaDMA8arKxuxhvYI6QT2wxtj2KbKP5WdLzojAuNPxcxJCuy0cXLJFgsjVEJrcyXaFXWiW9OPsyBcLrT2KnKB-J4PqHycDeWlOHjM_0UKT8QbyT3bJ7GsZhZoT9mgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef6825a80c.mp4?token=OJ3ZoeU2UpfOk2NlKNxINVJXE3jBuF-2a6jCxfmY5bdR3CUMaicqn0CQOiwKeZRzGDPLqA2aHrKE2Xu8UtMGb3tv3D8dBIht6l2wVBnEwEy_SiMj058DyaqRC-B5urq5kfmcT4VhVZE2GEN_MeSu1pfyjuwke7gvuWxrdX12JDYhkV8a_V98MBbm1HS9cN1ji_b75zIxvBWjB14-kXYqhZstJNaDMA8arKxuxhvYI6QT2wxtj2KbKP5WdLzojAuNPxcxJCuy0cXLJFgsjVEJrcyXaFXWiW9OPsyBcLrT2KnKB-J4PqHycDeWlOHjM_0UKT8QbyT3bJ7GsZhZoT9mgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیوه جدید لب گرفتن و بوسیدن همدیگه توی فیلمای ایرانی:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/127523" target="_blank">📅 01:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127522">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
امارات گزارش‌های مبنی بر انتقال میلیاردها دلار به ایران از جمله پرداخت ۳ میلیارد دلاری ادعایی را رد کرده و اعلام کرده است که هیچ دارایی مسدود شده ایران آزاد، انتقال یا پردازش نشده است و این اتهامات را نادرست و غیرقابل اثبات می‌داند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/127522" target="_blank">📅 01:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127521">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
استانداری هرمزگان: صدای انفجاری که دقایقی پیش تو بندر سیریک شنیده شد، بخاطر شلیک هشدار به کشتی‌های متخلف تو تنگه هرمز بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/127521" target="_blank">📅 01:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127520">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ukI6SC4Ml5Lkbg-S4cc1yavTywLP4wM5WDenPePhovLIFPyD7NuicRi55le10WVlE8K7tHfxxyWS0Ol_zTWEjIPTazhlkRAoV3Q2l6OeXg7Ygss0t_En0L3O5xLdQrsuxlfesI-A579xIRUl352FOZG4p0I2UqF_eWpXve8eYafIDg99vse-q8TQbNt4IX0Z6nYO-ww4H3QdKpd1kLxNS5VDzf_q05iWs0mmcIwyAZ9_wPOYqzOW8jS0mW1Zsm01bq-dvgW6bWoVrIRNZVhNwyMBXmfmk6q3nHIeAeSGhnUH1dXlcLqxOrSP9YntMv0zQcxtJrzX_u_FaEM9QjpvNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله شدید تندروها به قالیباف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/alonews/127520" target="_blank">📅 00:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127519">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
اعتراف عروس و معشوقه به قتل شوهر؛ راز گم شدن کیارش پس از دو سال فاش شد
🔴
دو سال پس از گزارش پدر کیارش مبنی بر ناپدید شدن پسرش، فیلمی از قرار مخفیانه عروس خانواده (ملینا) با مردی غریبه، راز این پرونده را فاش کرد.
🔴
پلیس هر دو را بازداشت و آنها بلافاصله به قتل کیارش با همدستی یکدیگر اعتراف کردند.
🔴
ملینا گفت که با همدستی بهروز (مرد مورد نظر)، شوهرش را به قتل رسانده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/127519" target="_blank">📅 00:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127517">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d5B2OFw3qLtF003xfRZwv9ebg4FrX2GheJN2jX1TWaP8qVHOzeJ-OppDtzF8wSKTWbDV4QqmuI5n-kOpWXsxGcb3XbCypxWiZdg2I1aTHoVqcYlvroqiVNIEixJZ5AmRupv-mZibCYifzBPBvvOo6sf0LyGFdlv193kaSLi4woIxk9mv2zOMxzZqp7DnJCkyjz1vJqBbr2iTxxy4bMyqyv6FV3TSoToe8Uty9oOgmbksc32mB9eVBUdTOinUa3K_Ur4ll_QZbDx4MIa1S_5Twrwit1tnXZyuo5KqOV4u-o4CCpimofjKNItYEqXCzqRpvTUZlR29gtpvnKl14ictHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nug7m73iXYVD8esuA1FJrDxN0GIjlEndAP0KpkPgjNjkpu1Fh8SyC0t7fwtJZLVsGEetGoBaws8S4h9Yk7ASLCcca2bSDsvxbQRWmylVXWKffBZf_E2135Fp0kXPHXUO6kdlAfJRzt3nSI40K25_duxEGdNnthfW3LK2SyAY4jVq0mmea79haCnGODWgnW29kHdlv_EWKXBM1-eFxgTiNNuoOKjhSSUa61yc_JQJEDm8jozK7IFJpJ63Tx2PIh1Gp1nuZIMgpgDwukU6uSiKvESbotHDWd-cCpj1FJTelsTPkYhOjrxiblcdpjsdm9g2gsnCuS_nfmwu5mkoWq-xuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصویری جدید از ابوطالب حسینی که خود را شبیه یکی از وحید جلیلی، قائم مقام صدا و سیما در آورده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/127517" target="_blank">📅 00:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127516">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJziwxIayMcyVR8Zsbt76kuzAgaa0-c5wySMs9_prCfMsEtyqQYmGsJU1RqmfsqAlqOYjiyP4i98d5y-S1TxswMBTH82ijdBPmIsy9k4tH1JjNklQQEym1-HlcjOFpCtY90Lagsxj_QglK_OHAehOvH7NMLjns6yv7Wui8cP8CMC4D6JZLhJF_sm8Y3UUMpVqjBMKgxKSzHA9sWl_b50aJmB2dsdrkAyF2qGMRyBaYiYhhwAwp7nM7yC7PifUdWStWtFnCYV4mvmo8dGwcnAiDBwRkwGm5XWnnayUlLQd9kWWs9gHohO1NS3Qa7_69POVK2LKAmv_HCxHbXMEgTFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش فعالیت نیروی هوایی آمریکا (USAF) بر فراز خلیج فارس و عربستان سعودی
۵ فروند هواپیمای سوخت‌رسان نیروی هوایی آمریکا اکنون بر فراز خلیج فارس و عربستان سعودی در حال پرواز هستند
۱ فروند هواپیمای هشدار زودهنگام و کنترل E-3B Sentry (آواکس) نیروی هوایی آمریکا در حال پرواز بر فراز شرق عربستان سعودی است
۱ فروند هواپیمای شناسایی و شنود سیگنالی RC-135W Rivet Joint نیروی هوایی آمریکا در حال فعالیت بر فراز خلیج فارس است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/127516" target="_blank">📅 00:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127515">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/127515" target="_blank">📅 00:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127514">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrluUNtRcJyAuFEFwU9CUsrGvkEogTL_xozeSCXC6n10SA9zqGmeh-1lC41_TTBZV1Es2kypN2iOtkO_Uc4EAPlZoiw2xHALq-UgDSsNpimCgu6rGv0g_i6yIBon386aR9WzJ_5pVLTu-2Q2862P8xhVYPpujY7FJ4VKCA_w2jRNgifQOruV05WigOovyOjffx_PBle3laNHudXB97i7cOfoNbL5ors5G3wIRHjkFPQugdpGmHXXFNQSV51UHiXqW2zMYJohAwY-ONcCw137haDBNiEA7nNwY87UBgI8d4HvCiU2tA6zrFUpYKO1OwB95jWreAXI0oJTA12q5PUUeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای جنگ الکترونیک RC-135W و یک سوخت رسان آمریکایی در نزدیکی ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/127514" target="_blank">📅 00:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127513">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d4473eba.mp4?token=shKt4ShZwln8Gi47468wJlBpJji6T7vZotuomD0zMT_RrRwRMjLua1GdoK2jWp026mNdLuv8PawSeezjagRfKFnZ8JW72dksLdN-a8oNHaXUj47M8J4xkFEby2m2Jg6uETIPe9YX-aCup1ozgS7zEGTkhUZSKM7dktjRpm7avMfmEVHeX98rPpa_78a5cYg5lr0ewjA6PHhEZ-6m3RzZt3r2cG9OvpQbdEYlJmkThK2--rvvAA8q-lPDkVGqapGvfOjfrh3CvoMM3V4siukjPHzax8NS05LyYcSc3g5UFqGyYsKH9wx6Rrm3eC91xZPPGF_fUC76nLpAwYTe408DEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d4473eba.mp4?token=shKt4ShZwln8Gi47468wJlBpJji6T7vZotuomD0zMT_RrRwRMjLua1GdoK2jWp026mNdLuv8PawSeezjagRfKFnZ8JW72dksLdN-a8oNHaXUj47M8J4xkFEby2m2Jg6uETIPe9YX-aCup1ozgS7zEGTkhUZSKM7dktjRpm7avMfmEVHeX98rPpa_78a5cYg5lr0ewjA6PHhEZ-6m3RzZt3r2cG9OvpQbdEYlJmkThK2--rvvAA8q-lPDkVGqapGvfOjfrh3CvoMM3V4siukjPHzax8NS05LyYcSc3g5UFqGyYsKH9wx6Rrm3eC91xZPPGF_fUC76nLpAwYTe408DEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراد ویسی: جمهوری اسلامی رهبرشو کشتن، ۵۲ مقامشو ترور کردن، بعد کشوندنش سر میز و گفتن حالت بتمرگ و امضا کن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/127513" target="_blank">📅 00:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127512">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
صدای انفجار در قشم و سیریک
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/127512" target="_blank">📅 00:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127511">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
صدای انفجار در قشم و سیریک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/127511" target="_blank">📅 00:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127510">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
فاینشنال تایمز: اورانیوم غنی شده ایران، نابود خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/127510" target="_blank">📅 00:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127509">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
عراقچی: یادداشت تفاهم کمتر از ۲ صفحه است و کلمه‌به‌کلمه آن بارها بالاپایین شده و وزارت خارجه با نهایت دقت تمام موارد خواسته شده را لحاظ کرده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/127509" target="_blank">📅 00:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127508">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6363935340.mp4?token=UXJHDj0Nw6odq6wzd_jMDgXkaqGJPMrKFIHEojvWRy1IJd2ZZV82vgR-KFrTCo7g6isLbvrmxKJtBNgcjyP5b2mG6LVLRQ_2slVAkS6fb4P1mNAMpq0dkNML9IiVSmku6TopE3ibKfU-fexkkqRDs9QTRMGCccyyFsQwFKnXFaoEr7Bj5a7bzd9724UKt50iN7eZs0g-UKYuMSfvJ16OFgj6JZ4eE_jRyaarMreo-YMJvjdDAJFrOgu6O1fjm_PAHoLrFtltMq-TfPQDMsJOQFGgMFTgoZnUAtBqQdU7t-ATzvapceQuW_A2esAyQsl-m3qLi0Bnup8ozX3Vwosb2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6363935340.mp4?token=UXJHDj0Nw6odq6wzd_jMDgXkaqGJPMrKFIHEojvWRy1IJd2ZZV82vgR-KFrTCo7g6isLbvrmxKJtBNgcjyP5b2mG6LVLRQ_2slVAkS6fb4P1mNAMpq0dkNML9IiVSmku6TopE3ibKfU-fexkkqRDs9QTRMGCccyyFsQwFKnXFaoEr7Bj5a7bzd9724UKt50iN7eZs0g-UKYuMSfvJ16OFgj6JZ4eE_jRyaarMreo-YMJvjdDAJFrOgu6O1fjm_PAHoLrFtltMq-TfPQDMsJOQFGgMFTgoZnUAtBqQdU7t-ATzvapceQuW_A2esAyQsl-m3qLi0Bnup8ozX3Vwosb2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگن این ویدیو باعث شده ترامپ توافق رو قبول کنه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/127508" target="_blank">📅 00:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127507">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
گفت و گوی امیر قطر با ترامپ درباره پیشرفت مذاکرات بین آمریکا و ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/127507" target="_blank">📅 00:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127506">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvArhLeJAYBZ3l5j2QD9KicjFWv_DI8czY82xa91dmWxGtCu1vXTwkYHe73eAD6nULcZcfE3pv1s2qdDYN2vb85TNWATYObG8O0gWA1VoHr_v8BgJQeS-l9HM5O5e268jF-GAY6XSPeHqqy73vJ7gNqmIxhQh103K0o_wvD3nG5oDT2i7hi-LiVCLD4lQ9jpVOGNJgxBrvcchBnd7KZ-wXjrWVzym76ieRzVs8uo33BpToQgXsckMDJXHG1IxHbrsvPRr3bvbqBy6lX0srypCrwTCviNZjtogf9nKzTxU7YFG-213mfA-fMYGptXKVJftD3nTENyddPyiPyF_3WiBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: توافقی که با پخت و پز بانیان توافق ننگین برجام باشد حتما خسارت محض است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/127506" target="_blank">📅 23:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127505">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
رئیس‌جمهور کوبا: قوانین اقتصادی را عوض می‌کنیم تا سرمایه جذب کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/127505" target="_blank">📅 23:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127504">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d6d94579.mp4?token=FqUVJIE7d_fTd_-Gib32Gl06RWfG9urs6ZFB6Intrb0AYigGpdx2QJkvJJd1IGOqg7IKH_dJt49oSNtVOHxp3_Fo-agHVWeEuwlX0wckV2CLtSOpVcnGAHolpbmziCPZEkL3J0RH6x0nykYD7Y5C4TTvnrmb4802s25lFXoVu-em9OJmbxfjhrKPgoZ30HNN3o4twDvsmchLvLk8dTn6cuHAB3Vljhmln8qdA8SxXX-LO5xV70kbvOJRuDEynL_sjeowuDb5LgNa15kTL_eFsdfuErfVykMRyFCvDweM-obQGTjVWSFe-oc6gXO4bR2t7cxRbOy1oB1rmtB1WE-baA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d6d94579.mp4?token=FqUVJIE7d_fTd_-Gib32Gl06RWfG9urs6ZFB6Intrb0AYigGpdx2QJkvJJd1IGOqg7IKH_dJt49oSNtVOHxp3_Fo-agHVWeEuwlX0wckV2CLtSOpVcnGAHolpbmziCPZEkL3J0RH6x0nykYD7Y5C4TTvnrmb4802s25lFXoVu-em9OJmbxfjhrKPgoZ30HNN3o4twDvsmchLvLk8dTn6cuHAB3Vljhmln8qdA8SxXX-LO5xV70kbvOJRuDEynL_sjeowuDb5LgNa15kTL_eFsdfuErfVykMRyFCvDweM-obQGTjVWSFe-oc6gXO4bR2t7cxRbOy1oB1rmtB1WE-baA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
داگ بورگوم، وزیر کشور ایالات متحده:
کالیفرنیا به نفتی که از تنگه هرمز می‌آمد وابسته بود.
🔴
آنها قیمت بالای بنزین خواهند داشت. می‌توانید از گاوین نیوزوم و مجلس قانون‌گذاری ایالتشان برای سیاست‌هایی که وضع کرده‌اند تشکر کنید. این موضوع هیچ ربطی به تنگه هرمز ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/127504" target="_blank">📅 23:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127503">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
تتر بعد از اظهارات عراقچی درباره احتمال امضای یادداشت تفاهم، به ۱۷۳ هزار تومان رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/127503" target="_blank">📅 23:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127502">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
عراقچی : شمشیر ما همیشه بر فراز تنگه هرمز خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/127502" target="_blank">📅 23:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127501">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فوری / عراقچی اعلام کرد: احتمال امضای تفاهم در چند روز آینده وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/127501" target="_blank">📅 23:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127500">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
عراقچی: فکر می‌کنم نتیجهٔ تفاهم برای منافع ملی ایران خوب باشد و دستاوردهای میدانی را تثبیت کند.
‌
🔴
علت جنگ این بود که ما در مذاکرات از منافع‌ ملی‌مان کوتاه نیامدیم و مقاومت کردیم
🔴
دشمن آنچه که در جنگ به‌دست نیاورده را در مذاکره به‌دست نخواهد آورد.
‌
🔴
یکی از مقامات آمریکایی به‌تازگی گفته که ما تازه فهمیدیم که ایرانی‌ها با بقیه فرق دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/127500" target="_blank">📅 23:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127499">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
عراقچی: تفاهم در صورت نهایی‌شدن به‌صورت دیجیتالی و از راه دور امضا خواهد شد و سپس اعلام می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/127499" target="_blank">📅 23:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127498">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
عراقچی: اگر آخرین مرحله مذاکرات انجام شود تفاهم از راه دور به امضای دو طرف می‌رسد و اعلام خواهد شد
🔴
ممکن است در چند روز آینده اتفاق بیفتد.
🔴
رسانه‌ها فضا را مشوش نکنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/127498" target="_blank">📅 23:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127497">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
عراقچی: یادداشت تفاهم کمتر از ۲ صفحه است و کلمه‌به‌کلمه آن بارها بالاپایین شده و وزارت خارجه با نهایت دقت تمام موارد خواسته شده را لحاظ کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/127497" target="_blank">📅 23:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127496">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
عراقچی: شورای عالی امنیت ملی اشراف کامل بر مذاکرات دارد، بارها موضوع در جلسات مورد بررسی قرار گرفته است
🔴
کمیته‌ای شامل تعدادی از اعضای شورای عالی امنیت ملی بر مذاکرات نظارت می‌کنند و هر جا لازم باشد به شورای عالی امنیت ملی گزارش می‌دهند
🔴
موافقین و مخالفینی در میان اعضای شورای عالی امنیت ملی نسبت به متن هست اما نهایتاً به صورت جمعی تصمیم‌گیری خواهد شد و پس از تصمیم‌گیری ابلاغ می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/127496" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127495">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
عراقچی: ممکن است 60 روز مذاکره تمدید شود و ماه ها ادامه داشته باشد. ممکن است تمدید نشود و دیگر مذاکرات را ادامه ندهیم. باید ببینیم بعد از 60 روز با  چه فضایی مواجه هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/127495" target="_blank">📅 23:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127494">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKjU8s3YeFY2H1JvPjEBa8Mk12UcyViKXWj_xW5NsPZTrR6it18G50kqRFz_SaNC05RqwOocYi0TPYUFvBKh_CuPGivAz4yUOOIymZgbULofQXmEhpiLVA-p5pan1voWSYWbQwdiQ5fxSvAK0Zl8MCRh9VMPM-B-aEWYlf0IqkPPDvkht60eYanPbv0s3pc-Yp86eKWHnYFq9Vv3ymcZokMWPY96ObuKhwabVDp8YHjRgTqaamGzaERsdWLzCL-ikgL1nNx2xB20c80b5M14JQqydAzK1PSYbKOTEdUSbxEeUpFzrlZY50_NtiLTTQ8-cigXKSjcwwgYFgDj-yMu0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/127494" target="_blank">📅 23:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127493">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
‌عراقچی:  از نظر ما تنها شیوهٔ بررسی مواد غنی‌شده، رقیق‌سازی آن در داخل ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/127493" target="_blank">📅 23:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127492">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
عراقچی: محاصره دریایی آمریکا اولین چیزی است که در این توافق به آن اشاره و تاکید شده است که باید رفع شود
🔴
دارایی‌های مسدود شده طبق یادداشت تفاهم اگر امضا شود، آزاد خواهد شد
🔴
هیچ‌یک از دارایی‌های ما نمی‌تواند مجددا مسدود بماند
🔴
برای جبران خسارت ایران طرح بازسازی در نظر گرفته شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127492" target="_blank">📅 23:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127491">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
عراقچی: به‌زودی ایران و عمان بیانیه مشترکی در مورد اداره تنگه هرمز منتشر خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/127491" target="_blank">📅 23:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127490">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
عراقچی: طبق قوانین بین‌الملل گرفتن عوارض از تنگهٔ هرمز امکان‌پذیر نیست اما هزینهٔ خدمات دریافت خواهد شد و این در مذاکرات تثبیت خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/127490" target="_blank">📅 23:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127489">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
عراقچی: در مورد آزادسازی پول های بلوکه شده ایران بعد از امضای یادداشت تفاهم صحبت خواهم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/127489" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127488">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
عراقچی: هزینه خدمات برای تنگه هرمز گرفته می‌شود و دیگر این خدمات رایگان نخواهد بود
🔴
این امر مهم تثبیت شده است که هزینه باید پرداخت شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/127488" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127487">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
عراقچی: اگر طرف مقابل ظرف ۶۰ روز به تعهدات خود ذیل یادداشت تفاهم عمل نکند، مذاکرات در مورد مسائل باقی مانده ادامه نخواهد یافت.
🔴
احتمالا بزودی برنامه مشترکی با عمان درباره مدیریت تنگه هرمز اعلام خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/127487" target="_blank">📅 23:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127486">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
عراقچی: اسرائیل باید از لبنان عقب‌نشینی کند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/127486" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127485">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سید عباس عراقچی: اسرائیل دشمن این توافقه و درتلاشه خرابش کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/127485" target="_blank">📅 23:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127484">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
عراقچی: مقامات غربی میگویند باورمان نمیشد ایران سرسختانه مقاومت کند
🔴
این مقاومت در وهله اول مرهون جانفشانی نیروهای مسلح است و همه ما مدیون نیروهای مسلح و شهدا هستیم.
🔴
عامل دوم مقاومت ایران، حضور مردم مبعوث در میدان بود.
🔴
رسانه‌های ایران و صداوسیما نقش مهمی ایفا کردند.
🔴
از همه اینها کوچکتر، دیپلماسی بود که سعی کردیم صدای ایرانیان باشیم و دفاع کنیم از مردم ایران و یار نیروهای مسلح باشیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127484" target="_blank">📅 23:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127483">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
عراقچی: نتیجهٔ تفاهم یک یادداشت ۱۴ ماده‌ای است و وقتی نهایی شد تک‌تک آن را به مردم می‌گوییم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/127483" target="_blank">📅 22:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127482">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjiDqbkIThZ66ojTWNneFsGvZBFQ7zVIVgg_VEvWiPmxwzZdvmIZREnskJzBtyoAkGBxN7lodu-9GTvj06Wr4UfYY98Yuc3SLvawuBB8govGZ20R5yNyXzJX9FOrOTfl5AEXMFF-rzTWCY83dPSC4EHhd_nT5_XSq0xmP-svf_yi-3_p9R_AhTWgHX03awTJ7IKt4Bs1gSjioY-zcb-bMTS3sQuDebPceunBXU-7SDgv3rP7RAAoymgOQnJt4tHhxoaCNOFHRsilDwgJBEZEE34rJDAF6sqaPeGQCrYPQdCWdAqdRuQ2Fyb4lDn5UryiXByodR5MnN33L3J7n8hw5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: تعهداتی که داده شده باید حفظ شود. نه اگر و نه اما و نه بهانه‌ای. برای معامله نزدیک پیش رو، راه دیگری وجود ندارد.
🔴
هر چه بکاری، همان را درو می‌کنی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/127482" target="_blank">📅 22:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127481">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
عراقچی: دشمن تصور می‌کرد که بعد از جنگ ۱۲ روزه، در جنگ ۴۰ روزه می‌تواند ایران را تسلیم کند اما با مقاومت جانانهٔ مردم و نیروهای مسلح ایران مواجه شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/127481" target="_blank">📅 22:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127480">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
گفتگوی تلویزیونی عراقچی در صدا سیما آغاز شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/127480" target="_blank">📅 22:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127479">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFXlg0Yp8R2-booSphdlKRJIODecwYHErAi3n12NnoMGm3kxWvCcQUDfUK-1FVWR2rbfwrTudjESpBMZ1pNdbJ2oa5m0gdnUt33DU4O4b1INX2uermmFV_7gQct-uSz0QuN5cj0WLbCu-3pdczhAhH88Mhic4cA0XSw5ANAzhCTjgTKlzVhNK1P_15Vg1AyEmVBnl01pkeZwEz_dAU3cTT72RUO9LkuYo5F_K6Sf7hxu3ocD23gSE_Hf6zSBI_mWj9NwaVQ_nocazixyBaJ-fvmCbRF72DtIxUvYT_s4jcoqS8Yc-K4gSW-cDTUlkuBiqkg_dLBdqG_VAcR6fur8-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر هواپیمای Boeing 737-7JZ BBJ A6-RJF در آسمان تهران که حامل ۳ میلیارد دلار بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/127479" target="_blank">📅 22:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127478">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
تسنیم/ حزب‌الله: لبنان نیز شامل آتش بس میان ایران و آمریکا است
🔴
«حسین الحاج حسن» نماینده فراکسیون حزب‌الله:بر اساس آنچه از سوی مقامات ایرانی به روشنی به ما ابلاغ شده، لبنان نیز شامل آتش بس است.
🔴
بر اساس آنچه مقامات ایرانی به ما ابلاغ کرده اند، اسرائیل از خاک لبنان بر اساس این توافق عقب نشینی خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/127478" target="_blank">📅 22:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127477">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ارتش آمریکا: اعمال محاصره دریایی علیه بنادر ایران با قاطعیت ادامه خواهد یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/127477" target="_blank">📅 22:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127476">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vX_aHdGWJyJamUsw0_1SJBd6n-MYZ825cKtgtMTo9AuOuHePg1bR9vptnZrHnuDfzyCEr_9o4UmDMo3mrfehyi4c1Ncpnz79avjRnhZMS6YDYCjABGo1J5D8oHTh11Ml-MoBRZpIcxD0JP1btxPRSWhSHVxxqxU6n-t3-8V2f7L2QIjAe3PoPtyCFB0lmEZWM4-VXEBzVKNSmHb3VE-5XjFOo2ziAjsil3G0LNU6bZGUK_Zux4ntu9xNu_ahRdTei_CTbR6yIzs08zxzOTzVIJouf96ePHYJ6Jk4qWGC0pkSfBtexsII_ChljZwm3oZUKAMmx_JMVz0lO7v4Xxi12g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی بزرگراه صیاد تهران یه مرده حین رانندگی
دید عه زنش داره بهش خیانت میکنه
با ماشین از روش رد شد و به راهش ادامه داد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/127476" target="_blank">📅 22:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127475">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
توافق بشه یا نشه چه فرقی به حال مردم میکنه؟ هیچی
🤔
مردم فقط یه چیز میخوان و اونم خودشون بدست میارن. ظلم پایدار نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/127475" target="_blank">📅 22:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127474">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
عراقچی، وزیر امور خارجه در برنامه گفتگوی ویژه خبری امشب ۲۲ خرداد ۱۴۰۵ در شبکه خبر حضور خواهد یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/127474" target="_blank">📅 22:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127473">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
خبرگزاری فرانسه: سوئیس پیشنهاد میزبانی مذاکرات ایران و آمریکا را داده است
🔴
وزارت خارجه سوئیس پیشنهاد کرده است میزبان توافق احتمالی میان ایران وآمریکا باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/127473" target="_blank">📅 22:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127472">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988e3b12cd.mp4?token=Lly7_7IhCexlDwD9PqxJffcsFdx81c0q-YIzISJ6hd9C8a_p3tcck0MRE8gvEAs52q2LZeg-hK1ZE4d9p_J1nhtVAwuBrMx67TmEOjh1e1ga2URGEq1XfevQDo6gGYiCE0qMTcMY1kH9n-coBdWVbX2ak5ZkLv8UKZ6UBpUKoCIpA-_WEOHKgFcsXdG9JJsXxByS3qpx0Cf2ZvaeHzi2as9fqXCvako5fuYGzA4PCzTxQxES0vKvsfBMgKcRGHnGqpy_5IEIBS8UW02jx8_F16CpUB07C95VNfSfWIDnsenh_ECWx9tvztaIIn3fP5znLs-F5gmB2lEktlWDJ7ZyYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988e3b12cd.mp4?token=Lly7_7IhCexlDwD9PqxJffcsFdx81c0q-YIzISJ6hd9C8a_p3tcck0MRE8gvEAs52q2LZeg-hK1ZE4d9p_J1nhtVAwuBrMx67TmEOjh1e1ga2URGEq1XfevQDo6gGYiCE0qMTcMY1kH9n-coBdWVbX2ak5ZkLv8UKZ6UBpUKoCIpA-_WEOHKgFcsXdG9JJsXxByS3qpx0Cf2ZvaeHzi2as9fqXCvako5fuYGzA4PCzTxQxES0vKvsfBMgKcRGHnGqpy_5IEIBS8UW02jx8_F16CpUB07C95VNfSfWIDnsenh_ECWx9tvztaIIn3fP5znLs-F5gmB2lEktlWDJ7ZyYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از سایت راداری رادار هشدار زود هنگام AR-327 در کوه دخان بحرین که انهدام رادار را توسط سپاه نشان میدهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/127472" target="_blank">📅 22:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127471">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
رویترز از قول دو منبع دیگر، مقدار پولی که قرار است از سوی امارات آزاد شود را ۲۰ میلیارد دلار دانست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/127471" target="_blank">📅 22:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127470">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری / رویترز : قراره امارات چند میلیارد دلار از پول‌های ایران رو آزاد کنه
🔴
یه بخشی از اون، به مبلغ ۳ میلیارد دلار قبلاً پرداخت شده
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/127470" target="_blank">📅 22:01 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
