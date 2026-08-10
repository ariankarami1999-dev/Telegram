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
<img src="https://cdn4.telesco.pe/file/KeFNhqeTxV4U7KRpuCe5uyTrpfgEjEM5hakugEWK2nadMCT2YLemJ3hf9eN2wc9T0G-xCiihO9YvH1cJGhtf_6M8u7rJv3X-ROTMBGJAwVsbGA4wvyv2-hrdi8Vhn9V4uaTbxYze6QwxhWxjobqqmn5hdNl4ZusHCB_QNJNVCjKdUAKj8O0PlnbW17Jiopof-N7Q8ihu0CTbyQZrrBRHPx_mc-x1HYt-0tSCpnWUVlHJnscEynbsYa02qzbf9WxBbSMV3yZFyZzIUrGdG3_P_1av0OxS5-94NjCdr6Rd4dXZ0yfveZC9BAxDqtPfhaiiAyZQqmIAKYRFYQ3FQXwkfw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 971K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 13:24:39</div>
<hr>

<div class="tg-post" id="msg-140922">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEXFp7EI5F_uRdzkYY_oJWymowywvitMWtSRiCAiVm1n0gAhcfjVzJIHABS4kykODaqq90Nfk-iAs4sB9nzgLgMlkYthCgZC49W20T3OQO5aZM2FfE698Uz-Yg6j3AFhiDJ9Nvx9dkWCu499M8n4Db65JP78yae3TYWuvZotA6EADKAIhYdXOrL7i1vYoUpZLUX0nLT1IKp8fj5JMVD3TPjCwRPhEGLO-FYnaxxugSiAGu8zkAK2Ft-RmDFnRnr1ByXOZjkbLTk1xSy3JIdTpgM-zF6RE763mwpoYXpYem8MzsxUJh6-7fsU5pkqkjg8lbMDN5kUVbclj4WHGw9BlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رشد ۹۴ هزار واحدی شاخص بورس
🔴
شاخص کل بورس با رشد ۹۴ هزار واحدی در پایان معاملات امروز به ۵ میلیون و ۶۵۴ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/alonews/140922" target="_blank">📅 13:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140921">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
نایب رئیس مجلس: بازگشایی تنگه هرمز هیچ راه‌حل نظامی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/alonews/140921" target="_blank">📅 13:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140920">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل:  کاتز، ویدئویی منتشر کرده که توش اسرائیل چند کشور رو بمبارون می‌کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/alonews/140920" target="_blank">📅 13:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140919">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_AWk9KPBvg8kwAhrCyGclvnnvN9qBI7DFd387pa6B01O1fRMsbHJu6BgCr0SSJ14yzubcFVqaplKofofzWA-gQqB7X8G66Wiwk2sxFWkl6MLm5buS8KTak9hL7Vwov1GhLphhGE-M7DEAxlcm25GeLXw5LBKAt0FwFSF5d1GGXZHjZgSWltym9uQNSY1j1g6UtQaKUwKoWDScZDv-3E35H76NKWB_RDAD4WOUvxrO1XgFOQbV0V5XUF2qHkkcRC9-SDltFYckQ5zeJHTU4uBA1PstuqZxLsOyyC1AJY5Hsy7DVG2ESNL3L_T6dg79H27MDl_4bvno1C0RiYJVLiNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امور داخلی عراق: تمامی سلاح ها باید به دولت تحویل داده شود و از این به بعد هر کسی بدون مجوز دولت، پهپاد به پرواز دربیاورد، به عنوان تروریست با او برخورد می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/alonews/140919" target="_blank">📅 13:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140918">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
۶۳ نماینده مجلس به توسعه اختیارات رئیس‌جمهور در فضای مجازی اعتراض کردند
🔴
طبق این اعتراض رئیس جمهور نمی‌تواند هروقت که خواست به قطعی اینترنت پایان دهد و یا برنامه ایی را رفع فیلتر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/140918" target="_blank">📅 13:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140917">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
مایک والتز، سفیر آمریکا در سازمان ملل: ایران بیشتر از اینکه هز وزیر جنگ آمریکا بترسد، از وزیر خزانه داری آمریکا می ترسد، چون او کسی هست که آنها را تحریم می کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/140917" target="_blank">📅 12:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140916">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3eecf6773.mp4?token=de0kRoNIwwjNhTWwpXboz7XIba3MeDbXkfdtiCixEnqOW5ViKvwZO3ulIAG0fWqBnhJyLZt3Wu1NO_U4vQieEbyt8zQxtVZ7fp9Cck0aBBMcauaOLcIG_qAb44LsaZ_0f1xAnrRIai56RFxHnpIT5Vdl9dSCDERX_kc-S7Db7Bpb1w4r492Ia0lC1deW8q01b1UC9Xwe9scHcc0VqCD5kfroICvhacQm9QboIkrhOccBvAAa6wXV6kwbbGYvuAVRo8fTwflLGxk5Xd8GKpZHCU-i3OCcGX3j5pgxXweu7RbV1ht0UzCzGDZy2qKuoph49ECi6TRBV7iFo_RZ16Sj_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3eecf6773.mp4?token=de0kRoNIwwjNhTWwpXboz7XIba3MeDbXkfdtiCixEnqOW5ViKvwZO3ulIAG0fWqBnhJyLZt3Wu1NO_U4vQieEbyt8zQxtVZ7fp9Cck0aBBMcauaOLcIG_qAb44LsaZ_0f1xAnrRIai56RFxHnpIT5Vdl9dSCDERX_kc-S7Db7Bpb1w4r492Ia0lC1deW8q01b1UC9Xwe9scHcc0VqCD5kfroICvhacQm9QboIkrhOccBvAAa6wXV6kwbbGYvuAVRo8fTwflLGxk5Xd8GKpZHCU-i3OCcGX3j5pgxXweu7RbV1ht0UzCzGDZy2qKuoph49ECi6TRBV7iFo_RZ16Sj_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مدیر عامل شرکت توزیع برق: به ازای کشف هر ماینر ۳ میلیون تومان جایزه دریافت کنید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/140916" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140915">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd3d7d8977.mp4?token=Y5rg4gUOxJGxo3Yps8c7P1cjTwQpWUHOb2pFb4pmMara45B3TllA0Z1XolINtGAUCzzlmuDoEaLJiVPshsTpgohSdVa8jxBFefqQLFHvvlk2jJsHdSN_G6k5fZdqE__gehcwX7jGdk1mCZm0kCDvGsJurCzdhn0Y2SUy6aVXYGztW3Zqv2v_AydDQF4dTaSL6WP1FFl1e7heFR9RGTmJKy_Qvi5dHsln2ZP2ErtdtfAG6EIivh6S1_f7d2aHchSfsOD7U2zQdBLuO6Bte_dR5TJYL1hDaTncI2yKfT_JbhXC_nl4eZyUrahWYZ6xKB6w4stZ2ymBWmKVLJ_F0rF27A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd3d7d8977.mp4?token=Y5rg4gUOxJGxo3Yps8c7P1cjTwQpWUHOb2pFb4pmMara45B3TllA0Z1XolINtGAUCzzlmuDoEaLJiVPshsTpgohSdVa8jxBFefqQLFHvvlk2jJsHdSN_G6k5fZdqE__gehcwX7jGdk1mCZm0kCDvGsJurCzdhn0Y2SUy6aVXYGztW3Zqv2v_AydDQF4dTaSL6WP1FFl1e7heFR9RGTmJKy_Qvi5dHsln2ZP2ErtdtfAG6EIivh6S1_f7d2aHchSfsOD7U2zQdBLuO6Bte_dR5TJYL1hDaTncI2yKfT_JbhXC_nl4eZyUrahWYZ6xKB6w4stZ2ymBWmKVLJ_F0rF27A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برگزاری مراسم اربعین در لندن
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/140915" target="_blank">📅 12:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140914">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a8c9073a.mp4?token=PavfA8qzgajI7iA6T2ZhHgBXvCj0TIsdhqOINYiT162JtS74v4MwVyY3H0KDuzf6LNVs_B7tHJvdvljYoBPDmx92G5weZovAlV0ESM9wL-RCE-NNjvaLDY2cTbjinwTmXjUgrwO9xOxf1ETcfQk7rOevSy0oBAtYY_mdnMbn2jPXIkRuypfzFJxDSjodRHLH5WpYSzNeWdepTV91CcDaHDGl7qdWEIajOlCcbjgmzpx1IyLex3V7xGGc7_hwg8Got7gDge1l37E1APuKsSVj6YoKEn--E6lK3ydteDahUsym7QZf5cwvszUw3VHkCTKCDyocKuBQNOYeTFQvSJE7Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a8c9073a.mp4?token=PavfA8qzgajI7iA6T2ZhHgBXvCj0TIsdhqOINYiT162JtS74v4MwVyY3H0KDuzf6LNVs_B7tHJvdvljYoBPDmx92G5weZovAlV0ESM9wL-RCE-NNjvaLDY2cTbjinwTmXjUgrwO9xOxf1ETcfQk7rOevSy0oBAtYY_mdnMbn2jPXIkRuypfzFJxDSjodRHLH5WpYSzNeWdepTV91CcDaHDGl7qdWEIajOlCcbjgmzpx1IyLex3V7xGGc7_hwg8Got7gDge1l37E1APuKsSVj6YoKEn--E6lK3ydteDahUsym7QZf5cwvszUw3VHkCTKCDyocKuBQNOYeTFQvSJE7Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجید شاکری، مشاور قالیباف: ترامپ با ما توافق نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/140914" target="_blank">📅 12:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140913">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
رئیس سازمان هواشناسی: احتمال وقوع پیوستن پیش بینی ها تا این لحظه ۷۰ درصد است.
🔴
بارش و ترسالی احتمالی سال آینده نمی تواند خشکسالی چند سال گذشته و کمبود منابع آبی را جبران کند.
🔴
مردم خبرها را از مراجع رسمی اطلاع رسانی پیگیری کنند، خیلی از پیش بینی های منتشر شده در فضای مجازی قابل اعتماد نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/140913" target="_blank">📅 12:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140912">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
بقائی: ادعای نتانیاهو درباره ماهیت برنامه هسته‌ای ایران دروغ‌پردازی است/ ادعای بمب هسته‌ای ایران دروغی ۳۰ ساله است
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/140912" target="_blank">📅 12:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140911">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6c2ee8a2.mp4?token=tt2aC4x4DqytTLMmBCPcaVYO1eR7huIWnT-5WU2TUPKHJV8boNXMU6kEdRrq4jogp_aXICKpFOa4GNfiOiX75nADAeeEzg1YHBgOPn9hY2L152hgec_HPdFTsrWUbJMp_d-ijAwu3B7sK4QNJHACmmrVZf1y5Rq9B40NYQmSZQe4CTnHoTiu1pGOFmqs0f9wfexEZuzGWE8GATm6fV9KJCLsj1eCh5Bljt4OHXhpXGh6viYbYufgk9xonLTpP1eTT4Ofwe8lNACN_pqlyB4DG43UV-RN_j8ShZDiXlud7GkBGgg8kLldctSoil59tnkrOERgFKSSl2cXKZeGi-grpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6c2ee8a2.mp4?token=tt2aC4x4DqytTLMmBCPcaVYO1eR7huIWnT-5WU2TUPKHJV8boNXMU6kEdRrq4jogp_aXICKpFOa4GNfiOiX75nADAeeEzg1YHBgOPn9hY2L152hgec_HPdFTsrWUbJMp_d-ijAwu3B7sK4QNJHACmmrVZf1y5Rq9B40NYQmSZQe4CTnHoTiu1pGOFmqs0f9wfexEZuzGWE8GATm6fV9KJCLsj1eCh5Bljt4OHXhpXGh6viYbYufgk9xonLTpP1eTT4Ofwe8lNACN_pqlyB4DG43UV-RN_j8ShZDiXlud7GkBGgg8kLldctSoil59tnkrOERgFKSSl2cXKZeGi-grpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تراکم کشتی‌ها در تنگه هرمز کاهش یافته است، به طوری که تنها ۶ کشتی در ۹ آگوست از این تنگه عبور کردند، و بیشتر آن‌ها از مسیر مشخص‌شده توسط ایران استفاده کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/140911" target="_blank">📅 12:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140910">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: رفع وضعیت تنگه هرمز مستلزم جبران همه نقض‌های یادداشت تفاهم است که آمریکا در حال انجام آن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/140910" target="_blank">📅 12:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140909">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-Pm9N2kEw_AEC8NZ7Ap3aXfexAqBJzhjqWT0rexccaRO4Dq4DB3ze5YZC1rntWnl-jQ66nBStriZZ0Af2eRUlmkAk-Bd0g4engikAwa4bdwP2oT9lx35VZ390y11JmHc-ZXGWIU__Sm0FgBeYx0UgxlVruwHQ_vHiG1SxkwhnGnrZUHUvnr7SmUxynWTN3Nzvt83T4gcdST_rjOAQ9b-Wlb5a2hvuH7Cl_CNH4eIXkiw5knpNMuofB2VisP4_VRfdL6aWqyKH5oLdE-xRu0Fvdaek4HeU2EanCie0a6b37ngww9SR25qMtHJRixhlXdKmwOoKz6Mz7Gqr2q0M8sVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: ۱۳ میلیارد دلار خسارت، صورت‌حساب سنگین حملات ایران برای آمریکا
🔴
از آغاز عملیات «خشم حماسی»، ایران بیش از ۲۰۰۰ حمله هوایی، موشکی و پهپادی به پایگاه‌های آمریکا انجام داده و به ۲۰ سایت در ۸ کشور آسیب زده است. خسارت وارده به تجهیزات و تأسیسات آمریکا ۱۳ میلیارد دلار و ۴۲ هواپیما منهدم یا آسیب دیده است.
🔴
با این حال، آمریکا آمادگی کافی برای دفاع از پایگاه‌های خود را ندارد. گزینه پیش روی کنگره و پنتاگون روشن است: یا حالا برای حفاظت هزینه کنند، یا در آینده با مشکل جدی‌تری روبرو شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/140909" target="_blank">📅 12:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140908">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXlkQ4JvGi0v7jcWr_tK0qUlwoHRbAxJJo9kRIZx8pVEGLAw7mj9siz5wPSGpZQU6JjNDxjtASmooW00wF77iKT9ylB0XlmFeDhuf7coL1PnmC7kzeRqJRGT6Rt0Xazrsys1OangnCQo5ZSewYBqXYlKz_x9y1QWKkWCp8P2aNVi4JW1toQJwCuLGEZ484NerZNMm6duQHJXdAm4PWuOnuw8BsNmj5yMBS5vaH1InT-uys4KFRmNRZAbiT3TYceUFJf46rzr5zA-kggpnOlbpAKPbvgwKpPBWLceqJ8rLa51CzhBOjGvOqiFMMEu5oN9Fl0UAdXcG1Kxl-xPG6tGqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور محمود احمدی‌نژاد در جلسه دیروز مجمع تشخیص مصلحت نظام
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/140908" target="_blank">📅 12:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140907">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: به هیچ گزارشی، چه مثبت و چه منفی، در مورد میزان توانمندی نظامی آمریکا اعتبار نمی‌دهیم
🔴
موضوع مهم برای ایران حفظ آمادگی خود در بالاترین سطح است
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/140907" target="_blank">📅 12:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140906">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سی‌ان‌ان: شروط ایران برای بازگشایی تنگه هرمز قیمت نفت را افزایش داد؛ برنت به ۸۴.۵۸ و نفت آمریکا به ۷۹.۲۸ دلار رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/140906" target="_blank">📅 12:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140905">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
یک مقام ارشد اسرائیلی گفت به کانال ۱۲: هیچ شانسی وجود نداره که ما اجازه بدیم قطر و ترکیه به عملکرد ما تو غزه نظارت داشته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/140905" target="_blank">📅 12:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140904">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=rHkaDW1Q9rHbXeEA2aVdCx_TEdGeFxJA0l2KyhYkA7g4vmH0HKziEyAoTBwZUCB1IlyxuAWB9K5Y3PyC4gfm6CzmQhM-vZdeRcEvMhHLRFp94hYOE8yYJ90yIjE_Nmgxcbxq05SV2trKPOSnMcOAcuMI4ZT4ziV5CC1jOzi4F_FECylObeG9zuiuX3Yc_5blNMa0cKfk5XlSGg_xA7SGSrem0dQP8bUEZhg_xyX6gaEUZzqnnBiU3-YMqRUg4gLEaFy0--jnqJl5HpxcS5no5zh3uwOf0x71h1ALQgj8qv0c6ZzBLRyWt7VBJUkmSv5CG-oLB-R4PwDpr16CZ4i4VmbUfMmBVLJ0Bnxlu4SmaSZmfV56qvxAJa-4SWO0edJ4GdvuJJCpE4lSeTNoOIrhDAn1sKGGvtLM_JDDSCgfGmFLCuztoHhRB397FettmRp8rlUU1ZfmqPssbfSnlopGaDTH5gNkdec_lj5rC61-CpK-wNnEsWA9NbOgwG-pshPi3KRGiizWK0sBhxHwURFdEMWzZoxXeP3a5Bss0d_SnXAmAWEKfKFnB9iMIQ-b1D7BCFT3XHPdyM9f2CmzZu2nsULA9Q08RvWSPEKcN08dMckkI6JzPo3UDpQFarKK7-Fez0-jkGHRSMd8B_aPz4VIR2ulsWYmkHqZKszkYXwh6cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=rHkaDW1Q9rHbXeEA2aVdCx_TEdGeFxJA0l2KyhYkA7g4vmH0HKziEyAoTBwZUCB1IlyxuAWB9K5Y3PyC4gfm6CzmQhM-vZdeRcEvMhHLRFp94hYOE8yYJ90yIjE_Nmgxcbxq05SV2trKPOSnMcOAcuMI4ZT4ziV5CC1jOzi4F_FECylObeG9zuiuX3Yc_5blNMa0cKfk5XlSGg_xA7SGSrem0dQP8bUEZhg_xyX6gaEUZzqnnBiU3-YMqRUg4gLEaFy0--jnqJl5HpxcS5no5zh3uwOf0x71h1ALQgj8qv0c6ZzBLRyWt7VBJUkmSv5CG-oLB-R4PwDpr16CZ4i4VmbUfMmBVLJ0Bnxlu4SmaSZmfV56qvxAJa-4SWO0edJ4GdvuJJCpE4lSeTNoOIrhDAn1sKGGvtLM_JDDSCgfGmFLCuztoHhRB397FettmRp8rlUU1ZfmqPssbfSnlopGaDTH5gNkdec_lj5rC61-CpK-wNnEsWA9NbOgwG-pshPi3KRGiizWK0sBhxHwURFdEMWzZoxXeP3a5Bss0d_SnXAmAWEKfKFnB9iMIQ-b1D7BCFT3XHPdyM9f2CmzZu2nsULA9Q08RvWSPEKcN08dMckkI6JzPo3UDpQFarKK7-Fez0-jkGHRSMd8B_aPz4VIR2ulsWYmkHqZKszkYXwh6cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: تنگه هرمز از زمان حضرت آدم تا 9 اسفند 1404 باز بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/140904" target="_blank">📅 11:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140903">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7feda1ed7d.mp4?token=GYNDuCtq0C9OY9LcDCHDFoGELk_iqM5x_kFu9TR8yO5vr2nBaJ-zBOTYgKI0m1-c9cZyO8kUOgBb4Tok7X2PEyczNEu6iCECsbrXETDo1118PfoOJKauYt9qmo4hiyehpeQsczHExUFzq_VBFp-79vhcQn0EoU0Wbe8fkNvu1j4rwOOHnGnSmsiC1tLFgXOT3xgnzZSqY8x1xlKJyl__0eclZti9iyRbdXehFA_D_KJ4OoWUZxHkYcUYQHNOtNplIhWcr5_kEJqu1GYHM2VsCoiJzhx-sCOfCpm-Gshx1Ar-GeFpzADSAlNX8egfdJ-LDDxNeLiS4oDE15w06ZTwcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7feda1ed7d.mp4?token=GYNDuCtq0C9OY9LcDCHDFoGELk_iqM5x_kFu9TR8yO5vr2nBaJ-zBOTYgKI0m1-c9cZyO8kUOgBb4Tok7X2PEyczNEu6iCECsbrXETDo1118PfoOJKauYt9qmo4hiyehpeQsczHExUFzq_VBFp-79vhcQn0EoU0Wbe8fkNvu1j4rwOOHnGnSmsiC1tLFgXOT3xgnzZSqY8x1xlKJyl__0eclZti9iyRbdXehFA_D_KJ4OoWUZxHkYcUYQHNOtNplIhWcr5_kEJqu1GYHM2VsCoiJzhx-sCOfCpm-Gshx1Ar-GeFpzADSAlNX8egfdJ-LDDxNeLiS4oDE15w06ZTwcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقائی در پاسخ به ترامپ که گفته بود «داریم با ایران چراغ خاموش پیش می‌رویم و مثل بازی شطرنج است»: چه چراغ خاموش و چه چراغ روشن؛ ایرانیان نشان داده‌اند که شطرنج‌بازانی حرفه‌ای هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/140903" target="_blank">📅 11:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140902">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: دعوت‌نامه‌ای برای سفر آقایان عراقچی و قالیباف برای سفر به پاکستان واصل شده و هر وقت که زمینه مناسب باشد این سفر انجام خواهد شد.
🔴
اوکراین باید اقداماتش علیه ایران را جبران کند در غیر این صورت ما جبران خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/140902" target="_blank">📅 11:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140901">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/32938bccc0.mp4?token=A-y6OtzKdMfr_aD6JRbon0RkEjVdZ1EtdgqjjrCT_RQTVdqj0RAqFICNA6IKQgYFJK2QJz4FiziTMcrYS5juNA6KMMXFXfJ1aLCMsF_cHRxEDmdcBcUcq_ytI2j8CAi8zkMS1tWZs7Ud7yz9VSWA4OKBAQsof3fELsR7fmum2wkNoDT4o0zAxaqN4pM8PIkXXhpclS8tXb2W_4V3zd-PrEFnPV1ed30BSkdFMenhukCsUUl-accSZKCfR_MAnX3I24jf-i-LZv7Y6rhCdL7STEheyvGy_wFaOzTa5uuD0qN8HqnxvFkeqyaHUiLzcnofhCWBPrlbQQWmBfpR7jaF-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/32938bccc0.mp4?token=A-y6OtzKdMfr_aD6JRbon0RkEjVdZ1EtdgqjjrCT_RQTVdqj0RAqFICNA6IKQgYFJK2QJz4FiziTMcrYS5juNA6KMMXFXfJ1aLCMsF_cHRxEDmdcBcUcq_ytI2j8CAi8zkMS1tWZs7Ud7yz9VSWA4OKBAQsof3fELsR7fmum2wkNoDT4o0zAxaqN4pM8PIkXXhpclS8tXb2W_4V3zd-PrEFnPV1ed30BSkdFMenhukCsUUl-accSZKCfR_MAnX3I24jf-i-LZv7Y6rhCdL7STEheyvGy_wFaOzTa5uuD0qN8HqnxvFkeqyaHUiLzcnofhCWBPrlbQQWmBfpR7jaF-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: دلیلی وجود ندارد که نگران باشیم پیمان سه‌جانبه پاکستان، ترکیه و عربستان علیه ایران باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/140901" target="_blank">📅 11:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140900">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8c0fb174.mp4?token=wAG80PF1v-DVZTnXIfksMBYuTj9_y6aZOMOzD-XXI0BkHYLvAjCrJTM4DW22JJOEyKfrU2NrsWgJwrDG7hZXLBnHmSZ2KyfmM9ZUBKkL_Qz_OqeUAGPLJfpxyXfA5-26TcKpcvctjdtMhc_WEq_WIRaQFn3ud-UU51PnVKdoSnu7_kkRQEkuwFBFgXZTzvDuHeqNh5APFIePW6foWKsnaap6Lo-ciHnYoHVsi3R_MBPFruNNJ_ZUTb-uHKRJx9qgue7X0-rkpDXIO7juFe703zVWhCbXuhF9LuNFHf1BbGt9jC8bOxdU75EGFyVeViBkssaAaNN1pk0OjRj2BnDbpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8c0fb174.mp4?token=wAG80PF1v-DVZTnXIfksMBYuTj9_y6aZOMOzD-XXI0BkHYLvAjCrJTM4DW22JJOEyKfrU2NrsWgJwrDG7hZXLBnHmSZ2KyfmM9ZUBKkL_Qz_OqeUAGPLJfpxyXfA5-26TcKpcvctjdtMhc_WEq_WIRaQFn3ud-UU51PnVKdoSnu7_kkRQEkuwFBFgXZTzvDuHeqNh5APFIePW6foWKsnaap6Lo-ciHnYoHVsi3R_MBPFruNNJ_ZUTb-uHKRJx9qgue7X0-rkpDXIO7juFe703zVWhCbXuhF9LuNFHf1BbGt9jC8bOxdU75EGFyVeViBkssaAaNN1pk0OjRj2BnDbpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تهدید یک تروریست به سبک ریگی:
حالا که مداح ما رو شهید کردید؛ از این به بعد هرجا ما شما رو دیدیم میزنیم مبارکمون؛ هرجا شما ما رو دیدید بزنید مبارکتون. ما مثل شما ترسو نیستیم. منه مجتبی اژدری دارم علنا تهدیدتون میکنم هیچ غلطی هم نمیتونید بکنید. این دفعه بیایید خیابون به جان امام شهیدم؛ به جان امامم سید مجتبی یه جوری میزنیمتون که پزشکی قانومی جنازتونو با کاردک هم جمع نکنید. جنازتونم دیگه خاک نمیکنیم؛ میدیم سگا بخورن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/140900" target="_blank">📅 11:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140899">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
آکسیوس: کاخ سفید از رد طرح ترامپ برای غزه توسط نتانیاهو ناراحت نشد و آن را بازی انتخاباتی می‌داند.
🔴
یک مقام آمریکایی گفت: «ما نیازهای سیاسی نتانیاهو را درک می‌کنیم. مشکلی با آن نداریم تا زمانی که به آنچه می‌خواهیم عمل کند»، به‌ویژه در مورد مهار حملات. اسرائیل حملات را متوقف کرده و در حال عقب‌نشینی از خط زرد است، در حالی که آمریکا و میانجی‌ها حماس را برای خلع سلاح تحت فشار گذاشته‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/140899" target="_blank">📅 11:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140898">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تصمیم قطعی درباره سفر رئیس‌جمهور به نیویورک برای شرکت در مجمع عمومی سازمان ملل اتخاذ نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/140898" target="_blank">📅 11:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140897">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
بقائی: بازگشایی تنگه هرمز به لغو محاصره دریایی آمریکا مشروط شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/140897" target="_blank">📅 11:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140896">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
بقائی: بازگشایی تنگه هرمز به لغو محاصره دریایی آمریکا مشروط شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/140896" target="_blank">📅 11:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140895">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c174bcc983.mp4?token=S0BzPbzKwTeQCurl2gOMdAVzpte2vHSB_6gC3_MhQ0uVplyJrUYZD70EjhuTtCTOuWA1MbrP--WDHlwSuNj_tE6bBtLAXahNH5pcfa6PsFZL3l0a3nbjmbwxWih7zKRESCz_J0nP5qmIPjdn3gLsyki0ejMEI8dn6ZCdzM5RIn9kYzvWBgnJ1YxlVzYD20M2O05t0hlgTSR_-a7R47K_z4LzfpiTinTT0wrQ_A1eWIzsh2eRFZ3ZNz08LVHtPAh9GmU24ngFMnwWNR9jOgZ7jUKnjzlSglYVUeDwBVBG5oCrAnb5vH2QQpduSmyQmTTMGPyUHizAuzapDcg-m1t6QjysgvpegLcJzow1yKyWCEULRioBIc2CUXdtsk4oO22e0_Ou1tRBI9OxjXlw5ju2N9R9r7nyPvd6ivjR0MLDmfAwep20dYVL9v2R7QD89ydYlDgx6Co2PPiTccO7xXnbIkRl4uUuKgz1ioK-0Caind-0ETT6bByOCY0YfHIa5IdexoZ5hHD91jW8DmWe8LP-q8lh8nppEeUr4nQ6_eCYkvzqZztli_9cGkr2WQG1SfC5_DuYzsQNcl9VB0rVnr8dMYDxP0aQqIFKmnqpCIU-ExnUxSvzUymmdycE-9lGydcV2s0_l8qNI3hed_KG9dEVXataTFUGnLuZlqjdA6scHFM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c174bcc983.mp4?token=S0BzPbzKwTeQCurl2gOMdAVzpte2vHSB_6gC3_MhQ0uVplyJrUYZD70EjhuTtCTOuWA1MbrP--WDHlwSuNj_tE6bBtLAXahNH5pcfa6PsFZL3l0a3nbjmbwxWih7zKRESCz_J0nP5qmIPjdn3gLsyki0ejMEI8dn6ZCdzM5RIn9kYzvWBgnJ1YxlVzYD20M2O05t0hlgTSR_-a7R47K_z4LzfpiTinTT0wrQ_A1eWIzsh2eRFZ3ZNz08LVHtPAh9GmU24ngFMnwWNR9jOgZ7jUKnjzlSglYVUeDwBVBG5oCrAnb5vH2QQpduSmyQmTTMGPyUHizAuzapDcg-m1t6QjysgvpegLcJzow1yKyWCEULRioBIc2CUXdtsk4oO22e0_Ou1tRBI9OxjXlw5ju2N9R9r7nyPvd6ivjR0MLDmfAwep20dYVL9v2R7QD89ydYlDgx6Co2PPiTccO7xXnbIkRl4uUuKgz1ioK-0Caind-0ETT6bByOCY0YfHIa5IdexoZ5hHD91jW8DmWe8LP-q8lh8nppEeUr4nQ6_eCYkvzqZztli_9cGkr2WQG1SfC5_DuYzsQNcl9VB0rVnr8dMYDxP0aQqIFKmnqpCIU-ExnUxSvzUymmdycE-9lGydcV2s0_l8qNI3hed_KG9dEVXataTFUGnLuZlqjdA6scHFM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقائی: تصمیم‌گیری نهایی درباره سند دریای خزر به مجلس واگذار شد/الحاق به اسناد بین‌المللی صرفاً بر اساس منافع ملی صورت می‌گیرد
🔴
سخنگوی وزارت امور خارجه:تصمیم‌گیری درباره تصویب و الحاق به اسناد بین‌المللی منحصراً بر اساس منافع و مصالح ملی انجام می‌شود و ارتباط‌دادن آن به تحولات بیرونی توجیهی ندارد.
🔴
سند بین‌المللی دریای خزر (شامل ۵ کشور ساحلی) که در سال ۱۳۹۷ امضا شد، پس از چند سال بررسی همه‌جانبه در نهادهای ذی‌صلاح، جهت بررسی و تصمیم‌گیری به مجلس شورای اسلامی ارسال شده است.
🔴
لازم‌الاجرا شدن این سند مستلزم تصویب و الحاق هر ۵ کشور ساحلی است؛ از این رو تمایل ۴ کشور دیگر برای تسریع در روند اجرایی آن طبیعی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/140895" target="_blank">📅 11:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140894">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b558b46621.mp4?token=oqfRqvVcEzsdYbvyQoL8JgaBVVJPY34G86O63yZ8CHMCxQH7cGQ7lcBO27ZoYwTLiydJZcgjWUfiOEpIzWQb_Oq8zkwLAGgsdKDdqb3jIdK9qk2wd7QGQs8rb33MJgX1AZQyjMlFLjZV9z-PDEICpa_RXecHEjosmlDLSpXkZwJDchci1q2Pyu2VpPPiCw1u3Shon1CyH3avq_slGkK1TiKxzn2vTJqUBBM51WrDqKMaCAT-GpaAQA1fyHLpuvXOJs8j7plToUsjg0y0l-F9r2l3PzGhvrdQmGYvevqzDpbBOQCa-Rl9RdpcR6ODstrRETTCMA0xRUsWxeIQoCR6TT8UZ9SedW_9NFUqstR4PxoCLYsovxKLhTWd1KBLSnXx38KqQ8yasMOn-0AhilyEh1Jlsp014XSb8rKi3gojUTM9LdPSvRByA57aKN5Lth6GJRZjWhQlc1pZbMX7wWiMTBEbuK3btFvOT1QWiL8oRy3z5BO09QcDTRUOLIOF8TbvF8jZIK4X1_lS8GjKlB6W5Wl9arRcuPPs79CFjnhDRf_OqzR8hh1t7G9i9hMj39llzEcxr_8qtAOQgtY6-2SzxbYl_VZbYVk7sceDILLex8NDeYwWHEhR-JFG3C7Oq2tzBDuVvY3g7W7vZZt4DeaYSS0Nc92gGq5TWGRN36e_iAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b558b46621.mp4?token=oqfRqvVcEzsdYbvyQoL8JgaBVVJPY34G86O63yZ8CHMCxQH7cGQ7lcBO27ZoYwTLiydJZcgjWUfiOEpIzWQb_Oq8zkwLAGgsdKDdqb3jIdK9qk2wd7QGQs8rb33MJgX1AZQyjMlFLjZV9z-PDEICpa_RXecHEjosmlDLSpXkZwJDchci1q2Pyu2VpPPiCw1u3Shon1CyH3avq_slGkK1TiKxzn2vTJqUBBM51WrDqKMaCAT-GpaAQA1fyHLpuvXOJs8j7plToUsjg0y0l-F9r2l3PzGhvrdQmGYvevqzDpbBOQCa-Rl9RdpcR6ODstrRETTCMA0xRUsWxeIQoCR6TT8UZ9SedW_9NFUqstR4PxoCLYsovxKLhTWd1KBLSnXx38KqQ8yasMOn-0AhilyEh1Jlsp014XSb8rKi3gojUTM9LdPSvRByA57aKN5Lth6GJRZjWhQlc1pZbMX7wWiMTBEbuK3btFvOT1QWiL8oRy3z5BO09QcDTRUOLIOF8TbvF8jZIK4X1_lS8GjKlB6W5Wl9arRcuPPs79CFjnhDRf_OqzR8hh1t7G9i9hMj39llzEcxr_8qtAOQgtY6-2SzxbYl_VZbYVk7sceDILLex8NDeYwWHEhR-JFG3C7Oq2tzBDuVvY3g7W7vZZt4DeaYSS0Nc92gGq5TWGRN36e_iAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش سخنگوی وزارت خارجه به پیمان دفاعی مکه
‏
🔴
تفاهم‌نامه سه جانبه امنیتی میان پاکستان ترکیه و عربستان سعودی نشانه تغییر در ادراک کشورهای منطقه است؛ کشورهای منطقه با توجه به تحولات دو سه سال اخیر دریافتند که «امنیت» کالایی قابل خریداری از دلالان دروغین نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/140894" target="_blank">📅 11:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140892">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbac70904.mp4?token=iyYH6OwfknX_w4geA-xWTetuc6zM8NvTDqFtaTg6udFax1rpwCBAU-eXDMMRWmh0a9akU3kAesQ-dUghfvpbxROiGgOBsbhWIbGO7xMNL0HFupyj81HNz74f1uQVZYqNpFMJD6mbtD_0cBNJlpKO8zIOFS89L36MxMRMTbS0OKtx6IRAhePkBUfUSlVE4jx84G86pfYwiOoReiCnU55lp_Kty-598qCpSLtYpj3XTDPztZUBWq3UHThfB8ZGh9WhpHmmo3tmMi16H42Q2JzhxCTxkltEIOsP7qK6V81IB7ihTe6qBR5VdLErEvMg64FlXxYzGeSuN6FyUJVIDVrIbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbac70904.mp4?token=iyYH6OwfknX_w4geA-xWTetuc6zM8NvTDqFtaTg6udFax1rpwCBAU-eXDMMRWmh0a9akU3kAesQ-dUghfvpbxROiGgOBsbhWIbGO7xMNL0HFupyj81HNz74f1uQVZYqNpFMJD6mbtD_0cBNJlpKO8zIOFS89L36MxMRMTbS0OKtx6IRAhePkBUfUSlVE4jx84G86pfYwiOoReiCnU55lp_Kty-598qCpSLtYpj3XTDPztZUBWq3UHThfB8ZGh9WhpHmmo3tmMi16H42Q2JzhxCTxkltEIOsP7qK6V81IB7ihTe6qBR5VdLErEvMg64FlXxYzGeSuN6FyUJVIDVrIbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای اوکراین، یه پالایشگاه مهم تو تاتارستان روسیه رو زدند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/140892" target="_blank">📅 10:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140891">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZkXuf294WW4ISwDTAQX2_kSs5M-qdGwjosMM4f7rtfFK5EUUJzUZkkW_Rann3AWCC4lmyFEkMbLSgzvh3dz2PdDCCkYinmnA1sqSYyEOKGrO-NLlBHH0sl0RiMrVXgVlWXQpg6xSs_RGrdTBVYN0j6qASCjKBD3Ra5xPJaILXZimE5oiZGuhB8ZGbupqc8HkfiviMlqnBi1hvNFoUMw8xaJJUXFSfiv-YvuyMqlLRQMjqQaa1OxZf_3d_BSxvoxm7LGUiu6RH2MtCkP_u24Qym5q0TWF0Av34CN5ROoN-cVfKDURZ4BWV60a8ZmOiz52pZIJ0wuEp9oG377D10jzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای جدید هشدار زودهنگام آمریکایی E-3B از آلمان به پرواز درآمده و در حال حرکت به‌سوی پایگاه هوایی شاهزاده سلطان در عربستان سعودی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/140891" target="_blank">📅 10:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140890">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
باراک راوید، خبرنگارآکسیوس: کاخ سفید مخالفت نتانیاهو با طرح صلح غزه را بخشی از فضای انتخاباتی می‌داند و نگران آن نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/140890" target="_blank">📅 10:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140889">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
الجزیره مطرح کرده در صورت ادامه مخالفت نتانیاهو با طرح صلح غزه، ترامپ ممکن است به هواداران خود پیام دهد که «دیگر نیازی به حمایت از اسرائیل نیست».
🔴
به نوشته این شبکه، نفوذ گسترده ترامپ بر پایگاه سیاسی «ماگا» و جمهوری‌خواهان کنگره می‌تواند چنین چرخشی را به اهرم فشار قدرتمندی علیه نتانیاهو تبدیل کند.
🔴
اختلاف بر سر غزه، در این صورت می‌تواند از تنش میان دو دولت فراتر برود و به رابطه سنتی جمهوری‌خواهان آمریکا با اسرائیل سرایت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/140889" target="_blank">📅 10:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140887">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YoCKuH2VqdZrxaLD9n9dHfBhGdDxw-_y43O02e6zKALnVmFf2XJ9pPdlKDP7RRWN8COkfQFwizi3mb14S1j5PSxc4qCzIrBwXWuDyvMXXurPQtQp36mufyxxb6q-HGW44Ux4THzRXDiK4ccpr4DBoGvc-s_qz2Nm2_ZjiMkVqbrEznRnYvJSxu4x_shIKS62pV4rR76JZwAVelsGpeVraQ8dZIlkEvUZUhiYxJLpjV7NibFNI9vDI75So2V10tMpvl6Q9LeONRcpqdzDeaNC22IKR8PH5q22bJjGYbfrBGUMGpcktfC_Q7FOVIfjzjUGqgGmM5EzOtRSPvnzAEtp4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ouYLVt4VJ0YiP9nrKMmk0vaTo9OlPJlgQPgzKSEMzhKDACmRk3UyHVDNVWwmWw1d0CIf4eJIRMTq0Gf2qgXzvU1Tk655KMTB-LYinvf3mxArz3j2e7LtpwOamLGUAXcn4_J_dKcc3-mk4A1A1Yyh6eWZeiuyGSme2rt2jdY0dn-VBtIYBnIgH9PxD3KskwqF6vPw-eWNzOZ1v0YEeFI83q-g2juhMzgkWmAGcwMvb4Mo7uJP4t8oF1XVFi9-mH6k7eHHoA4FnX2MLZuV4sd92iB5lq8w8Kt40cML0IsY2hwAaTtzn_6NHRpP8CjgKdQNZzM-Czs6njYi7P4dcuxRMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
معامله‌گران در پلتفرم Polymarket احتمال پایان محاصره دریایی ایران را تا ۳۰ سپتامبر ۲۰۲۶، ۶۶ درصد و تا ۳۰ دسامبر، ۸۳ درصد برآورد کرده‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/140887" target="_blank">📅 10:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140886">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سپاه اصفهان از احتمال شنیده شدن صدای انفجار کنترل‌شده مهمات در حوالی این شهر خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/140886" target="_blank">📅 10:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140885">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
پزشکیان: عراقچی اگه شبا خوابش نیاد، تا ساعت دو سه نصف شب تلفن میزنه و جواب تلفن میده، چون روز و شب ما و اونا (آمریکا) برعکسه، عراقچی بعضی اوقات نصف شبا هم کار می کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/140885" target="_blank">📅 10:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140884">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639af17896.mp4?token=qGJJ8WkhBaBqUTNvH4MiRFHMqnl1IwM5Hd5HpQXV6IYDqzQ5E4Pw_W2ntOTEAV5mJBNBqB3pUDuVvm1jiCzmZwSrMkIFJIFzqrsJgZ6UBAGB7b9WRGu3AB1AUa83sd29FlCUZ-fENy0Yi8uQRB6LtHL-sxS5ekwdI6M4IqSUA0dovYr1zwWi-C4m4GTXkvWSgq7Jpk-rZqQBfR23X23VFufVFmVPefw5ItSQjlCo-66CkKFChCVQA0luFlE8jD2tppUr-M9x_pp1uMn39Bzur3KnT3IP_t68TP2TC0gZv0JOJcSamKrj-q5TKL9auELWUTymnipIqm37WAQay9cwuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639af17896.mp4?token=qGJJ8WkhBaBqUTNvH4MiRFHMqnl1IwM5Hd5HpQXV6IYDqzQ5E4Pw_W2ntOTEAV5mJBNBqB3pUDuVvm1jiCzmZwSrMkIFJIFzqrsJgZ6UBAGB7b9WRGu3AB1AUa83sd29FlCUZ-fENy0Yi8uQRB6LtHL-sxS5ekwdI6M4IqSUA0dovYr1zwWi-C4m4GTXkvWSgq7Jpk-rZqQBfR23X23VFufVFmVPefw5ItSQjlCo-66CkKFChCVQA0luFlE8jD2tppUr-M9x_pp1uMn39Bzur3KnT3IP_t68TP2TC0gZv0JOJcSamKrj-q5TKL9auELWUTymnipIqm37WAQay9cwuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای، خسارات وارده به یک پایگاه نظامی آمریکایی در حسکه، سوریه، را در پی حملات ایران در جریان جنگ نشان می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/140884" target="_blank">📅 10:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140883">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzUu_c2IjrM5Yp8UcpppmtLhup1SBLv8kZEktKCcw6E_48CQ8sLovJXc3A-tB4hcWmVZJ_uxy8i7eFbhxmc9Yup4rRT6g9skAlN-RUAhlEhpjBaiX_CXrYb4B6KIjyogZLsJwTUyUEXAmFhdch5gCm470f5_2ESiohdqia_11Fq9ThtCWFBs5V3z--2_5ILn9ts22IVsPJYUjYu58XHxnMsyukodzJRFckTlrn5AHXv3G1SQifbk2SlJ9WYcWd7ImOhjxe7W6vaaBiMqKi5pke6FxgdMcJFb-Tt5sbPaaT4G3YMPXIo4YS0twxLvbIhXTMY8BmEKh4WSo6F5SxvASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در مجدل زون، جنوب لبنان، به دنبال فعالیت‌های تخریبی اسرائیل، انفجاری مشاهده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/140883" target="_blank">📅 09:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140880">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f202621736.mp4?token=PBHkrYfbk90Bmv4ILMQAjYgcDuG-0PvgcAqNOqrwUL_ua1tJ4W2T-bm05QQBqpYCcv6lgNYsAm3JQaeU5OTOkzkOj7d21JEDr_iMbwLnSFFNLxFgs3DKjSzTmp_uUPOKvkL9ncvIWoTz4SsAJzbhhpxIhHumsEK6TSVqj1rhOp5VHVSne3Lz4JmibJSkuZdVxcBQ_PDJ2nbR-URg7tO8ht0FjE0PJmbuo1ncJunG0cYq85EooVyPmSZPr3R6YOWsv4aa8bzoJayG_V55qGYNOVFFGsL4eBFInvLR03mBMvzLs-wqyVoMwBj1if6N8X8yHJvUIWHZY5kTcl0kn_pyww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f202621736.mp4?token=PBHkrYfbk90Bmv4ILMQAjYgcDuG-0PvgcAqNOqrwUL_ua1tJ4W2T-bm05QQBqpYCcv6lgNYsAm3JQaeU5OTOkzkOj7d21JEDr_iMbwLnSFFNLxFgs3DKjSzTmp_uUPOKvkL9ncvIWoTz4SsAJzbhhpxIhHumsEK6TSVqj1rhOp5VHVSne3Lz4JmibJSkuZdVxcBQ_PDJ2nbR-URg7tO8ht0FjE0PJmbuo1ncJunG0cYq85EooVyPmSZPr3R6YOWsv4aa8bzoJayG_V55qGYNOVFFGsL4eBFInvLR03mBMvzLs-wqyVoMwBj1if6N8X8yHJvUIWHZY5kTcl0kn_pyww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از ساعت ۳ بعدازظهر به وقت کلمبیا، درگیری‌های شدیدی میان نیروهای ارتش و گروه‌های منشعب از فارک در مناطق روستایی ال تامبو، در نزدیکی مرز با کاخیبیو در استان کائوکا ادامه داشته است.
🔴
گزارش‌ها حاکی از آن است که غیرنظامیان نیز در میان درگیری‌ها گرفتار شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/140880" target="_blank">📅 09:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140879">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
وزارت دفاع روسیه: پدافند هوایی ۴۵۶ پهپاد اوکراینی را در طول شب سرنگون کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/140879" target="_blank">📅 09:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140878">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
الجزیره: در بحبوحه تلاش‌های ظاهری دولت نتانیاهو برای تثبیت قدرت خود در انتخابات ۲۷ اکتبر، نگرانی‌ها درباره آینده دموکراسی در اسرائیل افزایش یافته
🔴
نظرسنجی مؤسسه دموکراسی اسرائیل نشان داد که تقریباً سه‌ چهارم یهودیان اسرائیلی، درباره سلامت و تمامیت انتخابات ۲۰۲۶ ابراز نگرانی کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/140878" target="_blank">📅 09:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140877">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e68930a72.mp4?token=F_Ts9EvPlBNecXdbQRL6b5WvrSLLb4TY-Mh4VBKGslRBAdmAWOxjXahz-VCX8ekEYtBEhu1cGRE2vSTYDNvPme6xbLZtSniJhZwWawalPsPwtUF8BSuxKs6Y6q58HuBJV9XuVIoGJwwks32MqdNvy2xkoQbAYr8jV5fewujCIUJlng5cC_AvuJwNBF-0x2a9v6TMT1pyFIlzsTfxUxsttKIba_SEm6_eawraF1ofuDQm5zF3zHgG1NJxaFY4jb3nACDhbpdFtguO66WGJ5Gw591WamjpDzBhnyDfQAsgqxkpEhjbO2c-GSO1SGm875lcRhmIl57Yw0XRd1vsvyzbfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e68930a72.mp4?token=F_Ts9EvPlBNecXdbQRL6b5WvrSLLb4TY-Mh4VBKGslRBAdmAWOxjXahz-VCX8ekEYtBEhu1cGRE2vSTYDNvPme6xbLZtSniJhZwWawalPsPwtUF8BSuxKs6Y6q58HuBJV9XuVIoGJwwks32MqdNvy2xkoQbAYr8jV5fewujCIUJlng5cC_AvuJwNBF-0x2a9v6TMT1pyFIlzsTfxUxsttKIba_SEm6_eawraF1ofuDQm5zF3zHgG1NJxaFY4jb3nACDhbpdFtguO66WGJ5Gw591WamjpDzBhnyDfQAsgqxkpEhjbO2c-GSO1SGm875lcRhmIl57Yw0XRd1vsvyzbfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مردی روستایی در چین این بازوی مکانیکی غول‌پیکر را فقط با ضایعات فولادی و کار دستی ساخته؛ بدون هیچ پرینتر سه‌بعدی یا تجهیزات پیشرفته!
✅
@AloNsws</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/140877" target="_blank">📅 09:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140876">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd1d57d3f5.mp4?token=V-EWam6n0RJNWSNmewQvlaapVgLeEIFlEzoRlXDtXfarlzron01aUhts4gUKOXEyf28PP3E9Nwp1CGeRUgwHz0kbtqlissmrTlo3HWLWgRqZSA9PUjE8XQvXlt9j5E8IFHj5p5cP1btGLmlZZBVj2j5plfKxgxygNcQHwdXkIRX7OZsrEjgTekpJBkJxY9a1wx168iltVMQeGMKDAbY1N4wzXYpav0Hf52--AQE-Qz6dxTIeRceCQIksCRJR3Setr3tNqdNp2bR9emrO5nDPkLulZGPyaV4IOTlIXpGeHDYdIuQgD5svhdu7eTROH7pGF1iqOuhMUNQJA1JHlXJ0LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd1d57d3f5.mp4?token=V-EWam6n0RJNWSNmewQvlaapVgLeEIFlEzoRlXDtXfarlzron01aUhts4gUKOXEyf28PP3E9Nwp1CGeRUgwHz0kbtqlissmrTlo3HWLWgRqZSA9PUjE8XQvXlt9j5E8IFHj5p5cP1btGLmlZZBVj2j5plfKxgxygNcQHwdXkIRX7OZsrEjgTekpJBkJxY9a1wx168iltVMQeGMKDAbY1N4wzXYpav0Hf52--AQE-Qz6dxTIeRceCQIksCRJR3Setr3tNqdNp2bR9emrO5nDPkLulZGPyaV4IOTlIXpGeHDYdIuQgD5svhdu7eTROH7pGF1iqOuhMUNQJA1JHlXJ0LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گلوله‌باران توپخانه‌ای اسرائیل در جنوب لبنان همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/140876" target="_blank">📅 09:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140875">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dffbdce4c3.mp4?token=tLYJZTvOU78ALY0Jvtb96l596IwG5RtZVOP8q7prH0bOu-ZDMpHKUiryXS7NraxnL7eaQQMb3PkTlwXo3ImY-W8nVTkAWPruvQfeuI4htrRS_nSNXUSIYKCpa_W3U6FxokjEamp01U8WFz0Vu4VZWyY21gX0ICjEkdX7CW0wik5J7Lo08Ergxvu-t0d1cJTf9lzqzA2wZJw1Ca0MAUecVfCVg88UcEW8gcEdg8sXc9CHLRTbIY8NxMAymep-N62ufJL090HejdrM6DXRmo_9c6xq9NAHjGwJmrzSSdKNJucShHugwrxp0yodTuz2KM_kMeCcIRy2mZv83KTbeR795w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dffbdce4c3.mp4?token=tLYJZTvOU78ALY0Jvtb96l596IwG5RtZVOP8q7prH0bOu-ZDMpHKUiryXS7NraxnL7eaQQMb3PkTlwXo3ImY-W8nVTkAWPruvQfeuI4htrRS_nSNXUSIYKCpa_W3U6FxokjEamp01U8WFz0Vu4VZWyY21gX0ICjEkdX7CW0wik5J7Lo08Ergxvu-t0d1cJTf9lzqzA2wZJw1Ca0MAUecVfCVg88UcEW8gcEdg8sXc9CHLRTbIY8NxMAymep-N62ufJL090HejdrM6DXRmo_9c6xq9NAHjGwJmrzSSdKNJucShHugwrxp0yodTuz2KM_kMeCcIRy2mZv83KTbeR795w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برخی منابع عربی با انتشار این ویدئو از هدف قرارگرفتن یک کشتی متخلف در نزدیکی سواحل عمان خبر می‌دهند
🔴
شبکه راشاتودی گزارش داد، شعله‌های
آتش از فواصلی دور بر فراز آب‌های عمان قابل مشاهده است اما علت آن هنوز مشخص نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/140875" target="_blank">📅 09:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140874">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجارهای کنترل‌شده در خارج از محدوده شهری دزفول
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/140874" target="_blank">📅 09:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140873">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
رویترز: قیمت نفت در شرایطی که همچنان درباره بازگشایی تنگه هرمز ابهام وجود دارد، افزایش یافت
🔴
نفت برنت ۹۱ سنت بالا رفت و به ۸۴ دلار و ۴۶ سنت در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/140873" target="_blank">📅 09:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140872">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سنتکام: در چارچوب محاصره ایران، مسیر ۵۵ کشتی تجاری را تغییر دادیم
🔴
فرماندهی مرکزی ارتش آمریکا مدعی تغییر مسیر بیش از ۵۰ کشتی تجاری در آب‌های خلیج فارس در چارچوب اقدام این کشور برای محاصره دریایی ایران شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/140872" target="_blank">📅 09:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140871">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKktVCz2ijxx8gnWOF4ZJhsL0FV9iMZl7UQhnWkwCbhCWEbvHE22hQWmTrCE8rBOSUN2v9h-4H96pz4hYafZmRNNmE8vYa0It1vAN9dHrafIxPa1pF3kA7oYNeLSiOPDndZ7GlFPaz41qPaOmirF7sFBBbsFB_JBOjcX57tH0f4snHwvwiMK_XCNHUNUSAefQ-OF4wOLHyhlkHfY0xkGg500b0BS9UOug0_qGvcrCyKIuxt4D-eRdHyKkqVedoC5NkVqLYNi6XiLTcDQDSmOszjj-rU52AJnvPQyviQI-nmZUNxS6Nx4NAtxB1iwfVBxO6rsAbUf-m3YKr4qhsAY5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت تتر
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/140871" target="_blank">📅 09:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140870">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e48ea88a19.mp4?token=aTFDw2omLOfgLUO65w4mqdsX6aaFJ3Hmj7vok5TvxUQxmxi7SC5pv0BIG8PqY0LcfUDLgo2lqaa6pTcksk5NZAS1b4CMVthtQmgv8qpFJulqwNek_01W7y7Up2A6baWjhkPWU0dTCODqOuulRbw1xVKP_d567oq6bHiWFdhd5IfJIHoQQyyN4yq7C1REYNQTU1AYMPhlV1TUvjIxIznJuGY60bqv8SKCYguNkvB6625EDGaIyQWs43x2NP2fO9kXEjRQD2ZVJbmSzm6EyiulhRwVhTxx17aYz-fBUkYtfh1IWIEutEK1oFfUc6ri6WdgOyvgY0saU48Xjx0foB2SqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e48ea88a19.mp4?token=aTFDw2omLOfgLUO65w4mqdsX6aaFJ3Hmj7vok5TvxUQxmxi7SC5pv0BIG8PqY0LcfUDLgo2lqaa6pTcksk5NZAS1b4CMVthtQmgv8qpFJulqwNek_01W7y7Up2A6baWjhkPWU0dTCODqOuulRbw1xVKP_d567oq6bHiWFdhd5IfJIHoQQyyN4yq7C1REYNQTU1AYMPhlV1TUvjIxIznJuGY60bqv8SKCYguNkvB6625EDGaIyQWs43x2NP2fO9kXEjRQD2ZVJbmSzm6EyiulhRwVhTxx17aYz-fBUkYtfh1IWIEutEK1oFfUc6ri6WdgOyvgY0saU48Xjx0foB2SqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برخورد نزدیک دو هواپیما در فرودگاه سیدنی
🔴
یک فروند هواپیمای شرکت جت‌استار در فرودگاه سیدنی استرالیا برای جلوگیری از برخورد با یک هواپیمای قطری که توسط یدک‌کش در حال جابه‌جایی بود، مجبور شد ناگهان ترمز کند. دو هواپیما در فاصله‌ای بسیار نزدیک از یکدیگر متوقف شدند.
🔴
در این حادثه یک عضو خدمه جت‌استار بر اثر توقف شدید هواپیما زخمی شد، اما هیچ‌یک از مسافران آسیب ندیدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/140870" target="_blank">📅 08:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140869">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
الجزیره: ذخایر موشکی و سامانه‌های دفاع ضد موشکی ایالات متحده به شدت کاهش یافته
🔴
این کاهش به نگرانی جدی برای ارتش ایالات متحده تبدیل شده، زیرا نیاز به حفظ توان کافی برای مقابله با چالش‌هایی فراتر از خاورمیانه دارد
🔴
وضعیت ذخایر نظامی ممکن است بر گزینه‌های واشنگتن در برابر تشدید تنش جدید و [احتمالی] با ایران تأثیر بگذارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/140869" target="_blank">📅 08:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140868">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgYiFx7Tojsu95-OmB1kzQxy4_a30Hr0BR8WrT3iGmuBoXYyi6y8VoO1PsWYIMiOtWqsr-dKmjkIzZkARnaSsNrJrUvrpIoltNWmVJwTCNA15GH8KsHrlHYFjmlQ2Isf0EYEjfRi3zzUP1u0PdrOeTGop6Md2SvXcf9ykXaD4pyLHvlPwwugNcwmEaBVGUQH2QKm-XsN87C5Xee6NJySbuXtGTs18tP-mFUTqwE3SMaPqWBi8jzTPoNsr7jP0hQo9X1WdIMtdiZ94n16mTRGd0N3KfLShfS5AZ5xwpTFhYO0T4TzOOd8Lb5cbxnYvUZsH9KoLJ_aoVo9rTexsQmgnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در پی حملات نیروهای مسلح یمن؛ عربستان همچنان پروازهای فرودگاه‌های جیزان، نجران و ابها را تا اطلاع ثانوی به تعویق انداخت و این فرودگاه‌ها بسته خواهند ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/140868" target="_blank">📅 08:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140867">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
رسانه‌های اسراییلی به نقل از منابع سیاسی:  بروز اختلافات میان آمریکا و اسرائیل بر سر سند ۱۵ ماده‌ای درباره نوار غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/140867" target="_blank">📅 08:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140866">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
اسرائیل هیوم به نقل از منابع نزدیک به نتانیاهو: ما وارد طرح ۱۵ ماده‌ای نخواهیم شد و اسرائیل عملیات در غزه را متوقف نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/140866" target="_blank">📅 08:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140865">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سخنگوی وزارت کشور: از فروردین ۱۴۰۴ تا اکنون، حدود ۲ میلیون اتباع غیرمجاز از کشور خارج شده‌اند.
🔴
اتباع مجازی که در کشور حضور دارند قدمشان بر چشم، اما باید بخشی از هزینه‌های زندگی خود را تأمین کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/140865" target="_blank">📅 08:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140864">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
بهای نفت برنت دوباره صعودی شد و به ۸۴ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/140864" target="_blank">📅 08:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140863">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9012d16498.mp4?token=LL8-PJ1rprKIYHs_Z4QDK-ihjSnuQUO9sXA2yxRzgrUwj0ghOCvYeFO5Dy-FZsuvRUBPBqkbNuZjMICdB_FtHY_jKV8-RjR4YRD2LcHZRzxBog3-1vyyw6N8KSjOixJsXJIDDWKfiF8ncbgJpn2GIMt5gGM5hab2FGvx4J1VTBj4LrzBnTAbPRnF6ofQnEuXEFyi0rukqEFHhnpyk0MvxIQSV8Xwb3g9MaLwZGjQj3pGYZKYWTHX-riNzHS56Wn9Jlao2quV7cwQeJxY7BB3W3CoLxPWTUI1ArqFnD3w_3Ct0Fbez9YXwWAjh0-cpv2AQshvLY_SGb2pddwXnOZ-aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9012d16498.mp4?token=LL8-PJ1rprKIYHs_Z4QDK-ihjSnuQUO9sXA2yxRzgrUwj0ghOCvYeFO5Dy-FZsuvRUBPBqkbNuZjMICdB_FtHY_jKV8-RjR4YRD2LcHZRzxBog3-1vyyw6N8KSjOixJsXJIDDWKfiF8ncbgJpn2GIMt5gGM5hab2FGvx4J1VTBj4LrzBnTAbPRnF6ofQnEuXEFyi0rukqEFHhnpyk0MvxIQSV8Xwb3g9MaLwZGjQj3pGYZKYWTHX-riNzHS56Wn9Jlao2quV7cwQeJxY7BB3W3CoLxPWTUI1ArqFnD3w_3Ct0Fbez9YXwWAjh0-cpv2AQshvLY_SGb2pddwXnOZ-aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
جشن امشب مردم ترکیه بخاطر توافق مکه:
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/140863" target="_blank">📅 07:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140862">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feeb36b6ca.mp4?token=A3TIqQNGcozlWcSz5OAEmdyrvLaHGvivkd19klKdTxz2atuw-SstebpPsYnKKDjAanWAMzWxTFF_CfgI_ajhLLXtb-7vbVO3myp5JhZcLinxuvdKbjeGaQY4PEotZjOH5k8hYg7HuJB2D3g2WRGJYUGpAkSrIK1rXNhl95t3bs7fV681uVAr3dTHernbMQf4Z_au128ETQz8i06uFOXEfBaZwrSMLkdEkYusDrJvMJ_3sej3KgTFxtf77VEABml30D2kyUedd_7tJDRQSZwiKmOb1S5RV0xHLe66Kn9vs-69ULdXRC_30YZoPk5hLdN1LvrPVudYTSz0zK23S3JDIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feeb36b6ca.mp4?token=A3TIqQNGcozlWcSz5OAEmdyrvLaHGvivkd19klKdTxz2atuw-SstebpPsYnKKDjAanWAMzWxTFF_CfgI_ajhLLXtb-7vbVO3myp5JhZcLinxuvdKbjeGaQY4PEotZjOH5k8hYg7HuJB2D3g2WRGJYUGpAkSrIK1rXNhl95t3bs7fV681uVAr3dTHernbMQf4Z_au128ETQz8i06uFOXEfBaZwrSMLkdEkYusDrJvMJ_3sej3KgTFxtf77VEABml30D2kyUedd_7tJDRQSZwiKmOb1S5RV0xHLe66Kn9vs-69ULdXRC_30YZoPk5hLdN1LvrPVudYTSz0zK23S3JDIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طالبان کاملا جدی برده داری جنسی زنان رو قانونی اعلام کرد، از این به بعد مرد ها میتونن مثل کالا زن هارو بخرن و مثل برده جنسی ازشون استفاده کنن
این در حالیه که حضور زنان در مدارس و تحصیل همچنان ممنوعه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/140862" target="_blank">📅 07:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140861">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">💢
💢
🔥
🔥
💢
قیمت طلا و دلار فردا سه شنبه ریزشیه
👇
سایت رسمی اتحادیه طلا و جواهرات goldonliveeeee@   لحظه ای قیمت میزنه  منبع دقیق قیمت لحظه ای طلا و تتر
😀
☝️</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/140861" target="_blank">📅 01:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140860">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">💢
💢
🔥
🔥
💢
قیمت طلا و دلار فردا سه شنبه ریزشیه
👇
سایت رسمی اتحادیه طلا و جواهرات
goldonliveeeee@
لحظه ای قیمت میزنه
منبع دقیق قیمت لحظه ای طلا و تتر
😀
☝️</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/140860" target="_blank">📅 01:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140859">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwjqNstYTeXd_CFqERGQ2MUQRyQtzZZkLsLLWh0ie-C4C84JVEpa92qLxVvARnN_Ya8SCOyuQF-IucrXo_B5-lAqOfylol9KQYGcOSAdM5LJXyQZvT9ws9hSlsw6-bPS78x6q45UvEPhADrHvcVDlRipEI-CUoL_PGHh5S8K74Q-vulS4qzpSEgWqsh09lqu01zwJ78_Y06xqwKHgrNyGLJPK9fbjuIkCNKMXvsj60GBaZ7MFJFcn_vdrP-XGEu5mWyYBVgPMsUJFezbTETB2La5aWpX87xMpyIsVQX8DWjENzAMROwJ5xQgjDmWx5dtsHrjvOEdQuL7PprrMSJG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که نیروهای آمریکایی مسیر ۵۵ فروند کشتی تجاری را تغییر داده‌اند، ۲ فروند را غیرفعال کرده‌اند و به ۲ فروند دیگر صعود کرده‌اند تا از رعایت مقررات مربوط به تحریم بنادر ایران اطمینان حاصل کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/140859" target="_blank">📅 01:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140858">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌
🔴
فوری/ بلومبرگ:
توافق درباره تنگه هرمز اکنون دور از دسترس است؛ ایران با مذاکرات مستقیم با آمریکا مخالفت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/140858" target="_blank">📅 01:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140857">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
کیهان: اردوغان و شهباز شریف مثل روباه مکار و گربه نره بن سلمان را سرکیسه کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/140857" target="_blank">📅 01:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140856">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cd2301599.mp4?token=IDVRJ71VJ8w5vCuNvuZXhfHcLpcgdwROwSyu0irFGzZwZTGqTH9jtR4TUQOGnIrCPQd05ywQxx_YaCt3loT5V4WqraB99xbmKaTICXfwNnpe-gnWVKvq8qIlc7TW3uICF7DCOZL9EVfNKW2hesKWUEJlEKFfUJzkykDPV2bY-vKoTqLZMWkgjPblx_7zzpP8j3U0XtdESpdnqUy1yGfxC4lqOBILdox6hpQ9a2dcAFGZ_7EUQ5mtbxGCkUW-wnnAo9Pp7nj_29ZiXfTZxpYUiRWszqpTqRr9DyTR1j9AXy4hRV7PiXq828elDj4Y65YcI5ceCO75ogUYAZONmbnvCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cd2301599.mp4?token=IDVRJ71VJ8w5vCuNvuZXhfHcLpcgdwROwSyu0irFGzZwZTGqTH9jtR4TUQOGnIrCPQd05ywQxx_YaCt3loT5V4WqraB99xbmKaTICXfwNnpe-gnWVKvq8qIlc7TW3uICF7DCOZL9EVfNKW2hesKWUEJlEKFfUJzkykDPV2bY-vKoTqLZMWkgjPblx_7zzpP8j3U0XtdESpdnqUy1yGfxC4lqOBILdox6hpQ9a2dcAFGZ_7EUQ5mtbxGCkUW-wnnAo9Pp7nj_29ZiXfTZxpYUiRWszqpTqRr9DyTR1j9AXy4hRV7PiXq828elDj4Y65YcI5ceCO75ogUYAZONmbnvCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه پهپاد رو تو جنوب کشور زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/alonews/140856" target="_blank">📅 01:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140855">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efvjJmrr5e9W8xv3cKuak8De7ykH_zaatduV00rQhlPGfMv65FyKzR-YZCe8QhdA20lVmahAL2r2A6TBOu0aG5LbnCwdkBv3RHGwv08CxA8M2X15ouD2O8xpN27goeFsKH9slloDJbRNpPC_hqMUwcTwMgbOufnQUrmZhb2HNuWIJxYRVQC5nmO7V371t0raif7eboK3kFH4MJKx4fk0VjxwWuF-RqNqAitVBAzqYB8gY_l-KSMFajPSC00-NzzNg4fs8HhEcvPjCWCDX9bNM90S419xT4KB_ybkomvuwdTfxG_3dxVkFN9hZfsLdlPkfTiTA8TvNyO_qyFCSgDCfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میثاقی: علی دایی در حد فوتبال اسطوره هست و الا تو سیاست و روش زندگی کاراش خیلی چیپ بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/140855" target="_blank">📅 01:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140854">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EU_BhTmmXvi3Ox-KSgGilveyrpwGrnm3R722BT5q_uFmomap5Z1rKWzYrda7ysp6zQIYCQqR58HRXahiuHmoUPB9cayU2vIX8htzO-YCXiZEBxR56xxWaNmmflDDu7sTTNidpnxREQsUIgQIvYjYb-NpuqBe7x3aF3R1UBvfCbHqW-AmwLRaIX_RgkL4bUnOFDMLl5LTy1kUwYONx3Ghrl_fUHYij_TR5HUjdMbW3JzTEtBmyKVmsVeNxCO7uD_ReJqDntUk51zHWCevEInOeK_G04zXXgftmEYk5xJw3aGFBlhulCexBe-XQwb-REKUbtVXiKSTqvR2O5V8tVI4QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه نفتکش تو نزدیکی عمان هدف حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/140854" target="_blank">📅 00:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140853">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">💢
این وسط فیلم مسیح علینژاد و دوس پسر سیاه پوستش منتشر شده که.........
💢
مشاهده ویدیو</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/140853" target="_blank">📅 00:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140852">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGt83eBx34yDhn8gxiOhzYMeNEPE4su1q9ukxtnuhRWzeWYZIojk9MpKBN3GvTNkd90KgJXe_2mFTWSLObP-txxwqStHfzwKYmtv9Y5pfrW7Ly-XxzpYcl92tz_Go3_mbUweWE4soeJxxt1R3AcgkLtfDhegUwT4RVq1Egrus0TgeCi0o3DR1QTO24X9TcQx0cfonraFBkF2maG2FV0Wo_8iQLJ_RqVZT1onBjYBO8HCnaRAB3fxzLgMZ5F3u51rHrVZ7QkMHac4EJeqP8j_EQsJ2YfoCc3-vBC2HvC08uYQG2TicItRp0ym1KI4GB8DjbQThjJD0ogtcjr9fRTUQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
ترامپ: 51 سال رفتار نامناسب ایران!
🔴
جالب اینکه چندسال آخر شاه رو هم رفتار نامناسب میدونه!!! و فرضیه اینکه غربی‌ها تو رژیم‌ چنج دخیل بودن رو قوی میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/140852" target="_blank">📅 00:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140851">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeaa90a135.mp4?token=aXDVbbqnhSyUq8nQIr7IuXut6axh1tqsDsIEBnogv01GmT3IVlgUle_0_M04zyxUNGfGAnWQMZY2S7VfRueCRUF5BLTzDUSc-82Tx0zeG-KFUFj8-o4YRQFDGiRM0MaWI-0-ZeB8qkMvq8TzfL5zkPj7ivNhvMaHfDINeX0HSuPrA7LgmRVscp_RdVBcmiyGzXwwyiR_UQsrBTbgHMhZf4XpGRWqaPRyqH4MGSyWUChDw3InpHpJ_UOteQx2ap-Omp6XJcxgl8ufEQo27Cws7ZASeKYrcq9uLquaW0_Oue3BSHGtuXTyU94qSOVY2XHPbbC_uPwMaeDhn-VtzOwcmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeaa90a135.mp4?token=aXDVbbqnhSyUq8nQIr7IuXut6axh1tqsDsIEBnogv01GmT3IVlgUle_0_M04zyxUNGfGAnWQMZY2S7VfRueCRUF5BLTzDUSc-82Tx0zeG-KFUFj8-o4YRQFDGiRM0MaWI-0-ZeB8qkMvq8TzfL5zkPj7ivNhvMaHfDINeX0HSuPrA7LgmRVscp_RdVBcmiyGzXwwyiR_UQsrBTbgHMhZf4XpGRWqaPRyqH4MGSyWUChDw3InpHpJ_UOteQx2ap-Omp6XJcxgl8ufEQo27Cws7ZASeKYrcq9uLquaW0_Oue3BSHGtuXTyU94qSOVY2XHPbbC_uPwMaeDhn-VtzOwcmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این زن چادری اومده اینطوری انتقام خون «رجب زاده» رو میگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/140851" target="_blank">📅 00:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140850">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pCHPVC4xnHlpv4AYQjQMTundqKjo7rqA038YV8yw6KwkEhpGezxIiXJh-d1Ug49_H7FxgfyuZJshnr5-WfgrUVBVEoDfjSvdOSEX1Yyg3u_n9BLhS1srFCVN42Z0BY-DmPFNXG79kPChRLkXmfDn7xvpHd47jEwrngUt6qY9TH--4taLmP-KfOsesBBCMonoy3kyDSe_60l5cnMxMbaTmoCSWtIu5JGi71S3rjNZ79NHNnedrrBJxbAJtjjf668PHgvWp9N4w8wVRAasuIG6YCNeMW4HLOqEfJ5mDz3wulUCGW-ymDrHDmf0cgtOuzuWpOZCF0nf_VP6QqoTELSlHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون شرح
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/140850" target="_blank">📅 00:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140846">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iHB2HrL_Yte4v5MfiH8M7Mc7NUiRjPs6w3j-m2IButlYoF9V-ptn4NuBIsTR-Q2_39oNjzqu53VYFYajiA_5soS4koqrCmBnYUGWYgXJXg9RB5__70cIrhRGK3xGLsSg91bNvcQu3qsEjPkTholautTy2276Ft3iMXydseRjoUYBS-KFG3qpVoFM1ejujKJDgpjIgz_W9QcnxVPx0qHPKRKu0JVYzqq66JTtubGsNK9ZTYEW6r0WxZpjA2l2yqjJugUAPiAAo3dFbiZYbJO9ZFqnpbh_FoOxAyzNN32nANUpwmF-Z-JGloCqt2EOyFEkymuOg4AUaQEZknJtHRbIDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_mG3SGiZnDwvJFnyAqlXwKtI052oh7ywMxp0yulsh-9-riWn1VbI__IjHzsYngN4gLmf0Oa8v1ZHbYQ_C4BIUpV0CcvR8g14dOeK_V61zyI3VXJt1DiOiTy85A0xJcqx2OOk162yGhVOI-GiGvJ7biwEiYi9H4WDK2_1EX4p_ADtSTNU4m9yp5KNIBNKqXoX-Bex9KuAdP4pDbXmB6GkZUKlN3_bIecJI7no5ZLsAgNRDg5xkEjuG2i6rtvNNheFQhHggtXasoIjXfeg9TwBK4eOjBSCiYmiFhW1E16TNGuHS2A9B1vYoguv7axHKi5akKK66Pi0S4Zwqj66Uf1tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d-Wza_coCWAUIpjHtQEeaFn_EIqIpoDma7sgLFFfNBPJ8NbrczPdbnAODMbd_mTafIZEsolEVY3GvTMdwSRMsSlDczTaz342qkz55wivcB3_ShUdOJRJLKO8exVlO1YISsEwnEfBYVQf_EnPvqYK2jcnqpLE_JrkIwNr6jwrU9p_TimWtHMMT6b4SuYTnLAN2v-pkAoRKTW_gnW8BQZgClwpq-YFxlReeF_-VvvxqwtcIofUoRZt_TAAg65Muyw2_jixxSTkFa8ERLcFvFNsnNAmqbQ5CieVi-JOLeksH2PJkx7GMMjy1ZIc93Rp2u2E4ch8kKF7L2PRLpWSFpemTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یگان‌های پدافند هوایی ارمنستان با استفاده از پدافند هوایی مجید ساخت ایران که اخیراً خریداری شده و سامانه موشکی هندی رزمایش آموزشی برگزار کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/140846" target="_blank">📅 00:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140845">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏
👈
اعتراض شدید کارشناس هواشناسی: هواشناسی جای ترسوندن مردم برای بیشتر دیده‌شدن نیست
‏
🔴
ماجرای ال‌نینو را جدی نگیرید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/140845" target="_blank">📅 00:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140844">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f191ecf5.mp4?token=dPFt4VxL1YEVdbNT_EpxtAQWEIJHPQy9U_sZp3uDDqcQ1GlfIrOgmjH1NgB2GqZiHbDeJq8im5DEU34lrhloXEL42wCXGVSLQ0L8dRcvGca_pFr1VCNMa_2KSOT3RRxQlDsC-rmJE3BAqjUbZHoswEeryC_H9B-zccG-Lt3bRbVWN832ymTqR4i5rPSr2bx6_kdZpBYwjnQ48w8zS3QYb8-GZPgSUHPMz8EZUak9-SAjkLpaaGKkpbGqWN5zh_Afr-oT2ZzBhbyv_VPFupJUBLBipS4UJlARJPjD6pKWN0ayUlPn1OYaMGakdDQffukbDqbSGhhkqlA1cjZsWQ0zEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f191ecf5.mp4?token=dPFt4VxL1YEVdbNT_EpxtAQWEIJHPQy9U_sZp3uDDqcQ1GlfIrOgmjH1NgB2GqZiHbDeJq8im5DEU34lrhloXEL42wCXGVSLQ0L8dRcvGca_pFr1VCNMa_2KSOT3RRxQlDsC-rmJE3BAqjUbZHoswEeryC_H9B-zccG-Lt3bRbVWN832ymTqR4i5rPSr2bx6_kdZpBYwjnQ48w8zS3QYb8-GZPgSUHPMz8EZUak9-SAjkLpaaGKkpbGqWN5zh_Afr-oT2ZzBhbyv_VPFupJUBLBipS4UJlARJPjD6pKWN0ayUlPn1OYaMGakdDQffukbDqbSGhhkqlA1cjZsWQ0zEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش سوزی گسترده در ایالت بریتیش کلمبیا در غرب کانادا
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/140844" target="_blank">📅 23:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140843">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TlcbuJQw1xqc29u_vSqZpRc8ZvPn9vgUwConYExEzb7nsnNtctX8z1xu4xmEMI-xp6MqDQD_7dWc7JEDtRVsxhpi4T2_gshznNE67MRswWRwJOZxEXEl5aPfhVcUHFbeC61s0O3jAJGSQUsNqszhSSh1tuI-pREoUtEqThHfSLJfbEdLVwl0Hn8rTWuSFZaAXV5F2THE1527zQKTvHCGtJTx-PxkmjMAhxHbK0Cbh3LEkRz5LAE9jx8XXKtP5ts3CjYy2HbisCFRIzSHOt0Bq5e44nYkyDD2QInx-RvpNWA9jGdOjGE0ItLWpREIQAHBeLzkN-PPmBZqf9IZnwpaeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان 730 تیر موشک PAC-3MSE به همراه برخی ملزومات ( فاقد رادار کنترل آتش، پنل فرماندهی یا پرتابگرهای اضافه) به قیمت 9 میلیارد دلار خریده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/140843" target="_blank">📅 23:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140842">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4403cc9061.mp4?token=boh8-i1Kso-Howy0YxA7qaYfttpSBC-_vzZYQ1ypFWdKGVSY03X2zIRVq7yjRVyowpcSWGZO26VnuPFi8d-Yvz15zf2A8rjh_HQNUPXugRWLKv6mFWOl1Ex0tsmSSjqHIpACmBerigw9M6wXahd7kE-96HHbiu2vM6oI17FRyypwlw8CHXhCRhQsMZejLJBf76qb23p5C8QSgTiBBh4aMIZUs7O5V_s8zn_3hOEo8O7AJpqVnT7xBDwDQ-cwiQC-i7MsBzAj7pizstQwn4XbL5ahyZUxK6QRnnynaVDfPo-4aCEpj8IAPUpI8Ppc9UrarE8pD_s0xJpcSRh2DClDgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4403cc9061.mp4?token=boh8-i1Kso-Howy0YxA7qaYfttpSBC-_vzZYQ1ypFWdKGVSY03X2zIRVq7yjRVyowpcSWGZO26VnuPFi8d-Yvz15zf2A8rjh_HQNUPXugRWLKv6mFWOl1Ex0tsmSSjqHIpACmBerigw9M6wXahd7kE-96HHbiu2vM6oI17FRyypwlw8CHXhCRhQsMZejLJBf76qb23p5C8QSgTiBBh4aMIZUs7O5V_s8zn_3hOEo8O7AJpqVnT7xBDwDQ-cwiQC-i7MsBzAj7pizstQwn4XbL5ahyZUxK6QRnnynaVDfPo-4aCEpj8IAPUpI8Ppc9UrarE8pD_s0xJpcSRh2DClDgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: [مذاکره کنندگان] در حال گفت‌وگو هستند تا انشاالله مسیر را پیش ببریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/140842" target="_blank">📅 23:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140841">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
زاکانی، شهردار تهران: با اصل مذاکره مخالف نیستم، اما مذاکره باید با شرط و شروط باشد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/140841" target="_blank">📅 23:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140840">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔥
🔥
⭕️
قیمت طلا و دلار فردا سه شنبه ریزشیه
👇
سایت رسمی اتحادیه طلا و جواهرات
goldonliveeeee@
لحظه ای قیمت میزنه
منبع دقیق قیمت لحظه ای طلا و تتر
🚨
☝️</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/140840" target="_blank">📅 23:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140839">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIkjy8qXQIPoQgroxKNH32uS4X7NJSnq51uFSp0GYwcXfi8geTfPXarTgjNG2E7PezYrt1iuowf-ZxlPWQZIXODd7swXulpdBEiC4gbuZOr5ie-H9NIEYU0Qx_xxdJpyV2Au77BpGs6CpwUaCHfDL-7lXowbLHwuIiVlOssFXXdIu2bFK-HvxweG8hWWddZuIEmO_KG3fsPszay265q06LbhVREcHKOJXhFIoHzD4_n-4nXhCaCjvOgEf5vdq1L9NmuX-zwB1Lgro-rGHdw1LrwWWAqR_e6OZsQL3b2opceRRNRXO5C3ptkq7lsy5k66CyfRzvOlc54aA4gdnbQSBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: افرادی که در چند سال اخیر _خصوصا پس از ماجرای ۷ اکتبر_ مهمان جلسات خصوصیِ «فیلد مارشال محسن رضایی» بوده‌اند، شهادت می دهند که تمام اتفاقات بُهت‌آور این روزها را «محسن رضایی» به‌ دقت پیش‌بینی کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/140839" target="_blank">📅 23:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140838">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1xMpgDLSQ7KKQPcu9Li4VKzyegkefNMLPvOik4vxTU3H6XuIt6B2vNY7tWznLENGgCJHDjKk_dVa4Q60WCKLl21OZbrYhagpNWnP-kk2XmVgl5Bkjg2Pt8ygW55wmemvcr-Fb98Xo0YWDLWcEdqSSnarOHyBFMeBTvgbO4TCi0e9e98BbZ7VhNWiQNSMfGfY_WriNeTaMumgTq2TvcOWsDuIhys1Gg6qK15zUDlDOpr2pMM9UfdwOJpGWCM35-wsyisAQDdCQSJJgqtu2QLzx6LrCz9B7LmUrhgTSYr_X2l7aPeQZx4g1mB-XQLVi6Yzfeq_JW4SXEgqyvNOsicpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
این شخص پادشاه تایلنده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/140838" target="_blank">📅 23:24 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140834">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oX405NlPcohPWo4msbrhdnIWyuq8cI2G81TFvxUnbBPIQ1vquZXeb1yWrIYHV1Js_Vhvews-X0kAzmu2LEStSuQtwF-XWKG8F_RA-Z136bc9df0h6B5K1Qwl3h3gb317zMItOXCMYMTr3ZsLa0g4HcnZP92TIRx1xsz-Ar2_HmYMRgU5MkQLSM9vyKodpIDFFtx4jV9sjhHUU26ONXpikLxTomsJ8EvwgS02ImyfExn5bjOJ14UaniWMuXNJ1HpqAXNO9g2hsO4CXa2qayvpi2wVGc_6_x--0sBUvBj7qE7e-6RkDc3hvYzuBTnxYcP0Eke-f6_YQouCEBJg8i6YAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGyCBPuf2Rpoz7xoXlka0NoIBOw5t7mFZQTnuUwuCqVfpcehAoRa0WgqWFpo0EeQMr5pqPpePqujdCjO-HwePezvdyWRQ723fENBDUbmoIX7qIUrqNRiAdd_6NqvpBnOhRbtqmMzWHPXlNhKbvhTS2EvIRr2OfTHANG8O8SyGfKCnZic6xU7ayUMVCACHvetjMiEwyG8Wx12j82myHy_ZKBKcaIgWG4QMJ7tkVpDtBGUQbHGvfsxrV8v1_qz5ug1RvmqQXu-U24qCfJTNDexuf7m46Ix25fnaFvoWdGZ1WQ1SS0jP7rqelUBACMOS8p7MSaKWJkDEQvJ3DBXQ06BhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uU4_ryuwSpSCy9By0wsE83rT9QOVjmI7LeDxgv-OiYFYSBPanorSsTioUnpcu5-TW0LnUX66-LURhzZCym20A2GtDvZd-MUA4OaV9w7tD_fjoCsF2xpctiysh9cS5IRi0xAJdWKRSBCWp4KILxQ0Ad6pih9e7Kay2UhwQsZ8wbIeOaXjjiroB4tRhnR2w3ZkRGwAd-c1PLSE6wiEGTouZcJIeR8GYeuigaMwKhvhPikOnuHqoT6MkzPix0yR7niH0Dp8Ee1QStEC9GqjPsP1zzLwfT0NotDO6Bonk2pKLmnpRvHeLX8xzO1ULNSuQapOFJgrwCcAyMjPXhRaQxMktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k50hkYpV66HSQnSpclQMZ1AoWbArAg5WzqjduKpIdw3NY5GC7RmbLaBuPwaXjep9ZtJBmIoWnBYz0TzyqOUEP82JIcNvSWV6Js2YRLYjnTEGd9FH8xyuwurKrYyGYGESZ5N2t2CBOl5Ez7-whRWJxJj06axz_xQljCVdP9E5aoC4YJGPwmlGdRzl3WFK5e8J0xuTT_iWI2B4SsfHnNXFUfX_F6-Z3DNtBiLsGoDtLAImW1B6Wxf1xpLeW_KNJrt_dh5CeFsLExspsSBOyyIiJj7GaG6e6-H6gK1PSRQWOsD1RITEr5Wn2N1IMmYU3h1dCsE8Ya4SQszH4B-uL4cd7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
شمار زیادی موشک و پهپاد به سمت تجمع‌های نیروهای دشمن سعودی و انبارهای سلاح‌های آن‌ها در المخا شلیک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/140834" target="_blank">📅 23:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140833">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWq-YiDFFyQoC91YjPdatPsjM2k4uGT3fqxNBKwPBX82eEUj2CBhHgkR--sCMooZgLeCMk06yywozyYl8GpH3qFeK1YO7uc6uo6VjTitu6s9-a-QADRTLDIsHzUAkvEx2csp5sULxiRzlLZsOOU2A2K2nZzeMsadG8ZQkUCmxU4uBYF6IxcpV8iNMAoowjokN0Pq9ukhjzfRsC44wVF_IRWTfG9UiTBvRJYxTcwUaxDqwzOYswK95y_lDx2NDnL9hv2fDhxWG78nWRy4RMCT3WVoPlqUcLHYiRvT8YEBEpVKM0g10v5PcU1jJ8RbRD5BdtXJvfmtFV9h-6_KWtcJTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تیتر یک سازندگی: مردم می‌خواهند زندگی کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/140833" target="_blank">📅 23:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140832">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12032b204c.mp4?token=nzju7Oh_0MShld7wTx8CBAfqiyILASq7jNDFMXbBJEwykTY-bY_lNcpitMjTc03SfkVK4af6ktfLQcqXOlYWj5JVFsI5n5Qv55TvIrAbaOQ_xz_nKV4ocKvd-2HT6009MgjEe-C3e_h38N0gdi5aiExwuYDJjjQm7k4o3_OC39FaOzS5kyAeaqO2WPjtO59t4S_psLHuKhbgl1JwkoA34k9j6cEwU7v6lovBZZbwpY-RG6PBNsUv_3napwKUDNs_aLhiaaO7IuOAbiX0f3zZ8qGxpINvDBj6yUBIH__dvu6GpfflvpolRRHYqFJ8ykg15rBRP7k97lExJPmhgmiwGIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12032b204c.mp4?token=nzju7Oh_0MShld7wTx8CBAfqiyILASq7jNDFMXbBJEwykTY-bY_lNcpitMjTc03SfkVK4af6ktfLQcqXOlYWj5JVFsI5n5Qv55TvIrAbaOQ_xz_nKV4ocKvd-2HT6009MgjEe-C3e_h38N0gdi5aiExwuYDJjjQm7k4o3_OC39FaOzS5kyAeaqO2WPjtO59t4S_psLHuKhbgl1JwkoA34k9j6cEwU7v6lovBZZbwpY-RG6PBNsUv_3napwKUDNs_aLhiaaO7IuOAbiX0f3zZ8qGxpINvDBj6yUBIH__dvu6GpfflvpolRRHYqFJ8ykg15rBRP7k97lExJPmhgmiwGIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بخش اطلاع‌رسانی جنگی یمن، تصاویری از شلیک تعدادی از موشک‌های بالستیک و پهپادها منتشر کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/140832" target="_blank">📅 23:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140831">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: اسرائیل به فرمانده سنتکام اطلاع داده است که در صورت توسعه برنامه‌های هسته‌ای و موشک‌های بالستیک ایران، به ایران حمله خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/140831" target="_blank">📅 23:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140830">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
میتشل باراک، دستیار سابق نتانیاهو:
مخالفت علنی نخست‌وزیر اسرائیل با طرح غزه به انتخابات اکتبر مرتبط است
🔴
او این مخالفت را در جلسه کابینه و در میان «دولت بسیار راست‌گرای خود» اعلام کرد؛ موضوعی که نشان می‌دهد این اقدام بیشتر با هدف جلب پایگاه سیاسی داخلی او صورت گرفته تا مخالفت با واشنگتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/140830" target="_blank">📅 23:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140829">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wr2qp8adDDXsvv9pEK3t4k3gSho8HiRs02Ppek1b_GjX0lGOeeyliqgIKil7Zz4zsdo6RCOj_xvchkQ9SOfDzCMPJ3r2ngEvCwDJImNjwTUiIvaqfRxZTJMv7-sMDpq6W-iUWJBZdd9oWH4kp3a8pu5dLqSJNf5Go4BDRcNuErzBJlVOr-vJ7zufFVcZRp6XS5wYrVLSbjk-RtigqNw9BEb_GHAfrMhmPmv2zpFs9s_vUScwL7N_uyQOM1c5kQQLLZj3-4-N_4bA3uB8TN8sGFuh8IIzRFiYdFvKTMCf8cV05zE-p1hGo0CxNymxTuzg3DZGGTaWOqkx0Nwm1qXQEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری فارس برخلاف نتانیاهو و رسانه های اسرائیلی که گفته بودند احمد وحیدی گفته در حال توسعه سلاح هسته‌ای هستیم، هرگونه تایید توسعه سلاح هسته‌ای توسط احمد وحیدی را تکذیب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/140829" target="_blank">📅 22:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140828">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0662ccaa16.mp4?token=snfQqXfrT8v9ZRCWBL9JGEv9VZR8Tu9E2kiW3gqGHV8c_zhY14EH8MVq6mwhOnp9fsY-IAYynPR3D25cw_BY-Vp0peLlVILgjdN0qjrhv5_JoFMCkbh9gQc9a12at_n-D7x7LZB7fagTAlgJ-MaIDyXxbA5ZeoY_sIqRIQ6EYBGYSZlwDA_9Q9oBIHssG_KGlKhDJvQRSMKJ-PPayTcHGQOxIKY8zZzZKWc7nXlqVPNn02WzjabGTVay1pJgJ3ZxlFWkUmXavl7Gbahj9Y_F69uhasl2Tbkf6Q-MIUnRtStkxQyhAGw6ELWqqU-XGQAj5qk4_ggz_GMoAOtk1DyFFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0662ccaa16.mp4?token=snfQqXfrT8v9ZRCWBL9JGEv9VZR8Tu9E2kiW3gqGHV8c_zhY14EH8MVq6mwhOnp9fsY-IAYynPR3D25cw_BY-Vp0peLlVILgjdN0qjrhv5_JoFMCkbh9gQc9a12at_n-D7x7LZB7fagTAlgJ-MaIDyXxbA5ZeoY_sIqRIQ6EYBGYSZlwDA_9Q9oBIHssG_KGlKhDJvQRSMKJ-PPayTcHGQOxIKY8zZzZKWc7nXlqVPNn02WzjabGTVay1pJgJ3ZxlFWkUmXavl7Gbahj9Y_F69uhasl2Tbkf6Q-MIUnRtStkxQyhAGw6ELWqqU-XGQAj5qk4_ggz_GMoAOtk1DyFFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جشن امشب مردم پاکستان در اسلام آباد بخاطر توافق مکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/140828" target="_blank">📅 22:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140825">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dNOr7NJqtWcej-8jhvvO5iYOC6drgk2dzeMxwPvAumCh_owC1pSM5o_NSmDHfKrft3AIIKFlKZyLGI9JsDycNR3JtRjMhirb1oB15L4PyVMvuIGiEnyxFsijn8NsCTEq3qO_rVAeokCLZXB4hbGyLZWdQfo1atWtJ3SPZjh0j3y8EIXCh_A1g5ZOVutFFFjLh5S1qdAcJ_Lf9T4-bIfIiFvKJoamyTIzzEm6vNn77yghuAdvP1CNPCGR8M34w46Yq8a1tzrQkbm0UTDVddV3BHL3dB_CRSzYrQqVpELAra9rn1AyVOosRSCqYTrGf1VZzPMePiDqpYN7xT0ScDHYCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vka4oR7TzGE_uyB7OMO4AAny02rmKvW1Fr4U_4cH_Wu6lUsyqrQuRuKv5uomxvuoWGK2Tkv4iUv3GRZv6LJWBOrM4K5bAUYbAJDviEEGy5JbTlrVoh7euOEvW2NJ9ojuxf8oNM5hmcqxwlET-UOTzOi_jmQYrFuQvcPg8rPtc4C-NCBGsX2jfFraST9K2DUIFRIGMNbTSZFUvi8KthkSbOWJwI0uJIg-dwgoQOHjbs8Zn4yTFE9TeqB9oIjJjlfn5pXOv74IzxR0XPhTA4N-1GG01T45zEd13aPe7QfnHDFKhVrh_XhzzVAe-b1afJ_GdFvs2j1vPFrKFLcoxcNHBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D2qMr3MiSuC6wEheMCXQSyDzA5JEmGjgbmgsD-D2x5aHt7FRfEoUqKJnJxAX7TKTOYG3oXFoY84gjVpc0PS61sTMR5GYmR41mLOcpsA5dmOlslMDKJSlKkb-m1h-P0P14r3-Gw9gcGBVU5YHMEokS0WMCfSbLSpQfa4cCwNI0V59snYTq2i9Th6qzvSq6hlABhtAjxuWu8TLlqwNqQJYAFS0o48h3ZUncZAce7tT3eUulHW55kZ3wHeXVo5U3RkVxN2lE11qoiTgoYJ7MOWoN9mdgcrS8gi7irCtxpdEfwb3xjQrisMfwF8vQLKeU7hJo0zsWMto7hhBzOYnz-nGgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
انتشار تصویر تلخ لیونل مسی در مراسم سوگواری و درگذشت پدرش
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/140825" target="_blank">📅 22:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140824">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
اوکراین دیروز یه تانک روسی رو منهدم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/140824" target="_blank">📅 22:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140823">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHEGQg5yyoJvYFvtKlgSba4SQRVa-ZUgYCU18X2zxavF1vFoKQS9Xw5ZzehM9knoldqSwCiN0yHNLVmLLbi_XVjybJmvpK1-h4KCnDSp1rMoubZaHcvDNBlCpzUzRxsp2-Lj7xtyEFmeDi8elPEyjHUr1UuoMfCvCiksU6gWT6E96mfLeeiVkc_NS_Hjxe-TP1a4E6vGacdb7WvGCn4J0cpA37LMDJwtWZpdyxr-f_FWA9nDbH_ScC7RCrO2Bcam2N3NO9lgM-xknBw7JUu2StyPu808CtH6ULx_AUOhVjhTR8OAahfK1yPCbcfxsQTbEtalinI2yZcQwwlhXthWzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه مراسم تعزیه، امروز تو ساختمون وزارت خارجه با حضور عراقچی انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/140823" target="_blank">📅 22:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140822">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a610735f5e.mp4?token=Y_mwSXHJs1BHUighBsgP1EEWKyRmu6jmnZaWdFCx3l2gr9eAozkzT1LjQ3f9hmM2Y1onLLxQcAjBgaig9F1QKKK7WUZr9ImLbp5MQWFH-lzN4pzE0vUB7cJxJVF7klY2qT0xZmaQqLTcPjU-DEoux1zn347lJvutjjX1ZmQAYvR6xrQMMT4uOu-3GNDogQrYkuOA_LDYXAbFESxqh9_uuGRT09p5R2kOxPCHXbJsv983WOzL1twKOyb80fAH9Aft_octXoFi5DUVyHZUAtyooNdijSfEbl3_LAYGlP8ean2yXDSuAkAFqGCCX2n8jUJHe-70w9jIxgE1scyaV5QejA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a610735f5e.mp4?token=Y_mwSXHJs1BHUighBsgP1EEWKyRmu6jmnZaWdFCx3l2gr9eAozkzT1LjQ3f9hmM2Y1onLLxQcAjBgaig9F1QKKK7WUZr9ImLbp5MQWFH-lzN4pzE0vUB7cJxJVF7klY2qT0xZmaQqLTcPjU-DEoux1zn347lJvutjjX1ZmQAYvR6xrQMMT4uOu-3GNDogQrYkuOA_LDYXAbFESxqh9_uuGRT09p5R2kOxPCHXbJsv983WOzL1twKOyb80fAH9Aft_octXoFi5DUVyHZUAtyooNdijSfEbl3_LAYGlP8ean2yXDSuAkAFqGCCX2n8jUJHe-70w9jIxgE1scyaV5QejA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌ها امروز به پرواز درآمده‌اند زیرا چندین هواپیمای عمومی وارد فضای هوایی محدود موقت نزدیک باشگاه گلف ترامپ در نیوجرسی شدند.
🔴
تمام هواپیماها به‌طور ایمن به بیرون هدایت شدند
🔴
این رهگیری‌ها زمانی که محدودیت‌های پروازی موقت در اطراف رئیس‌جمهور فعال هستند، روتین است
🔴
هیچ نشانه‌ای از نیت خصمانه وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/140822" target="_blank">📅 22:24 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140821">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79470446aa.mp4?token=jX2E2FGtf4sAdjlzEaxsLUD6V2CFuHWn8l3yLqBBzzfGIpsKjQpCu7_cuU3btY4LuOhs5Cm7cqZBH7z7g8yKSCCYCML5drvkyjLaJPJjDpqxeP-o-TnO_pGlQh_v6kprbSbCsq3ee3R1YUbPZbQg9NA1Ypqy_SwtOj0UbiLZmiRgmn65FRgp8bkbJWfdLeQGRqO1TfnQ_rVriQmkx2vWB4Lm_zhJSEWFgolL9kjjI7kqrAZbc03U-B-u_6zg_R71dYeZb-lrpOhfJgstKwJ-BYbQlzIbGq8nabvX5Tauf5Hhz9rwp_rq_QdISKUwU8rz3dwCUNMJ_uu4A2hfGat157FdBBOs7MV1OGZPt0c8sxZlE7XtsK2IIrR4IR6FdME9v7oXWDM9U5RI17iRG_roe2tByPIVUvzmwCycl1yQmk6rm1mM17mOL2qLsihvMROa2Q9t7BRTAS1dQzMgJeHePnDJ3VAXrtgqnF0zRHkouTS16PiyWUgLcE2DBQEJkoIUjARiloNyi6ylVJPYaAx-Sw2r031IWR_GdhjanjlKYqgjhjSRJYHNOJgbQfWZJZAZupTpNkkXkngkNHbFEbK-eQVpZMFuWwVtbUEzjwaPgLvN2Fi5vqPXVuL5nAB5McNh4ZleQ1RMsO3BW_UdoNC6TzE8Bw1OZqdaRIzOImV7Y6c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79470446aa.mp4?token=jX2E2FGtf4sAdjlzEaxsLUD6V2CFuHWn8l3yLqBBzzfGIpsKjQpCu7_cuU3btY4LuOhs5Cm7cqZBH7z7g8yKSCCYCML5drvkyjLaJPJjDpqxeP-o-TnO_pGlQh_v6kprbSbCsq3ee3R1YUbPZbQg9NA1Ypqy_SwtOj0UbiLZmiRgmn65FRgp8bkbJWfdLeQGRqO1TfnQ_rVriQmkx2vWB4Lm_zhJSEWFgolL9kjjI7kqrAZbc03U-B-u_6zg_R71dYeZb-lrpOhfJgstKwJ-BYbQlzIbGq8nabvX5Tauf5Hhz9rwp_rq_QdISKUwU8rz3dwCUNMJ_uu4A2hfGat157FdBBOs7MV1OGZPt0c8sxZlE7XtsK2IIrR4IR6FdME9v7oXWDM9U5RI17iRG_roe2tByPIVUvzmwCycl1yQmk6rm1mM17mOL2qLsihvMROa2Q9t7BRTAS1dQzMgJeHePnDJ3VAXrtgqnF0zRHkouTS16PiyWUgLcE2DBQEJkoIUjARiloNyi6ylVJPYaAx-Sw2r031IWR_GdhjanjlKYqgjhjSRJYHNOJgbQfWZJZAZupTpNkkXkngkNHbFEbK-eQVpZMFuWwVtbUEzjwaPgLvN2Fi5vqPXVuL5nAB5McNh4ZleQ1RMsO3BW_UdoNC6TzE8Bw1OZqdaRIzOImV7Y6c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله‌بیشرمانه و فحاشی مجری عن صداوسیما به سلطان علی دایی
@AloSport</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/140821" target="_blank">📅 22:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140820">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: ایالات متحده می‌خواهد اسرائیل به نبرد در سه جبهه فعال پایان دهد. این پیامی است که ژنرال برد کوپر، فرمانده ستاد مرکزی ایالات متحده، که آخر هفته از اسرائیل بازدید کرد، منتقل کرد. در مورد ایران، ارتش اسرائیل به آمریکایی‌ها اطلاع می‌دهد که اگر…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/140820" target="_blank">📅 22:13 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140819">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کنار تریدت بیا داخل ربات جایزه هم برنده شو‌
!
🏅
🔍
فکر می‌کنی نسبت به بقیه
زودتر می‌فهمی
بازار کجا میره؟
💥
پس وارد میدان واقعی شو
؛ جایی که فقط دقت پیش‌بینی حسابه، نه حرف و حدیث.
🔝
در ربات Preward قیمت نمادهای مهم
رو پیش‌بینی می‌کنی؛
💸
BTC
🌟
Gold
🛢
Crude Oil
🇪🇺
Eurusd
5️⃣
S&p
💵
هرچی دقیق‌تر باشی
، بالاتر می‌ری در جدول رده‌بندی و
جایزه دلاری می‌گیری
.
🛡
نه سرمایه‌ای درگیره
، نه معامله واقعی با ریسک حساب...
⚡️
فقط قدرت تحلیل تو تعیین می‌کنه چند نفر از بقیه جلوترن.
🏆
رقابت
هفتگی
برای کسایی که سریع می‌درخشن
🏆
رقابت
ماهانه
برای کسایی که با صبر و استراتژی جلو می‌رن.
💯
اگر مطمئنی تحلیلت خوبه و نتیجه میده
همین الان شروع کن و اسمت رو بین بهترین‌ها ثبت کن.
🪽
@Preward_trade_Bot
📱
@Preward_trade
#ربات
#جایزه_دلاری
#فارکس
#کریپتو
#ترید
#پیش_بینی</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/140819" target="_blank">📅 22:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140818">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
کوین هاست، رئیس شورای اقتصادی ملی کاخ سفید، به نیوزمکس گفته قیمت بنزین در آمریکا همچنان «بالاتر از چیزی است که می‌خواهیم»
🔴
او تأکید کرده تا زمانی که بحران خلیج فارس حل نشود، نمی‌توان انتظار کاهش چشمگیر قیمت سوخت را داشت
🔴
فشار بحران منطقه حالا مستقیماً به پمپ‌ بنزین‌های آمریکا رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/140818" target="_blank">📅 22:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140817">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری / گزارش‌ها از وقوع «حادثه امنیتی» در نزدیکی باشگاه گلف ترامپ در نیوجرسی
🔴
فرماندهی دفاع هوافضای آمریکای شمالی اعلام کرد جنگنده‌های این واحد، دو فروند هواپیما را که به حریم هوایی ممنوعه در نزدیکی باشگاه گلف دونالد ترامپ در بیدمینستر ایالت نیوجرسی وارد شده بودند، رهگیری کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/140817" target="_blank">📅 22:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140816">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: ایالات متحده می‌خواهد اسرائیل به نبرد در سه جبهه فعال پایان دهد. این پیامی است که ژنرال برد کوپر، فرمانده ستاد مرکزی ایالات متحده، که آخر هفته از اسرائیل بازدید کرد، منتقل کرد. در مورد ایران، ارتش اسرائیل به آمریکایی‌ها اطلاع می‌دهد که اگر اطلاعات نشان دهد که جمهوری اسلامی به تلاش بی‌وقفه خود برای دستیابی به سلاح‌های هسته‌ای و ارتقاء سیستم موشک‌های بالستیک خود ادامه می‌دهد، اسرائیل گزینه مداخله در ایران را برای خود محفوظ می‌دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140816" target="_blank">📅 22:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140815">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqImNXBjaONpoGz95iUKAvVRyV-5AD_Me_DMg0VYzQB5MdMA3hrgaBNmDuwvGDZmIAqQRI-x0XeXkxTBno3AUA0sPEW30gKK5tVpEXPk9R-fx_fWjQWhl1FqFirzJufn8k287Nrug1ScA4Ax-fI9GG8m3UMBacp-T6egLkh8YTOvSb5GvSjrBXtIr_titdyjzdGg2ZzOecIPXOYkPFggw0-TrFTA5qG22DVcTeitF-BJ4xp53wyhvEHgTfzXd2H191Bfz8IbBuS6O8G1APveGLhshbC1YaIE7PdV3RDhli8eSnEmul4JWVdNaRzmNGbrCz8bM6gk5GiSGYqx-PmnQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
رییس کمیسیون امنیت ملی مجلس خبر داد/قانون کنترل تنگه هرمز در کمیسیون مجلس تصویب شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/140815" target="_blank">📅 22:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140814">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnSoDjBvleUXFr5vTfceKH_jx1RsfKzlsrMyutljfo3fHDPQ9LFJiGKP2BO7PFrR4peBvwQy_BFRdnE8ro6Ed-ktr2U6rTS-3sG6St-OQvBYFgartBQlDYyNx2DrJPfyeeC-kX2HcoxxtmtJy8kKrsqAcCXGdHQujzmTi1B9vKQpeh2ipMAvzRpNxWFaYeX2g1cg73LHPzmO756J6UEr5bTutnWt0fI5VHgO4EE2cS4K62wNkYNB-9IEWIeIo9sNtT7Razz4FQAjrMlTAUVGC4waygFpgckwLfjL6NTqC7SO_oyrqkgzAqr5L1aCKneCxY4ro2Jii0PENIRxIgYNEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید: هیچ رویایی زیادی بزرگ نیست، هیچ چالشی زیادی بزرگ نیست. هیچ چیز وجود نداره که برای آینده‌مان بخوایم و فراتر از دسترسی ما باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/140814" target="_blank">📅 22:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140813">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
حمله مرگبار به یک پایگاه ارتش در مالی؛ ۱۰ نظامی کشته شدند
🔴
بر اثر حمله‌ به یک پایگاه ارتش مالی در شهر «سان» در مرکز این کشور، ۱۰ نظامی کشته شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/140813" target="_blank">📅 21:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140812">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMIQWaHiM6WfpqYo-Tsn7-PY5WHl6e6yW-h2T4Pxx-ZSE34-ROFBi-IGswaRUF7U9RyRWzMipN6HdXMVYcW7LOY2vIp0yDhC9rEvOVAjJfdUq55atJ1LTKkRbOeH0DuwyBNzF7LeOJB-1eonFZxdUsgsZq6IfuOhqDvnXRwa5vOlP_aRKqTMHNGH_Qfbx-gGaOqfejArdnkcQxIaWF_EQ1oqOK1tSPpetV82NR5GLtfajyjpVglzO4x27823NQPdLvRxZAjpO7KcD-x2lUbpvHFdOGQXdg5GrkycddvRIa0DpiTNyicAYlhDmujpMmdjsK2YKM1WOu5bQOpSOSSO5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شانس برنده شدن انتخابات ریاست جمهوری آمریکا ۲۰۲۸، از نگاه کاربران کالشی:احتمال جی دی ونس بیش تر از همه هست
🔴
بعد از اون مارکو روبیو که به کم ترین
احتمال در چهار ماه اخیر رسیده
و در رتبه سوم گوین نیوسام، فرماندار دموکرات کالیفرنیا قرار داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/140812" target="_blank">📅 21:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140811">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMpCTZKSvs77XLhdvuIWR_GRlBWti8d5z4oKDQDVUdBRCPRtxQhNs5CnKZOU9AB-D3OYabhA4sDY3DntZ0ru7No4WlPbCH0wDkp-3wZfI5MbhsLuj-WgZuCU87qG9Hk2Ruvi1z2QHIwubqbvL_MRHmL_5h0gdsh9ZJmM9Q0YY18RuybjnPldMtkXQ25C65UX2LX7PX7HhktFxLjnz9FTbBYAldi4-gJm6LnaxOMRMnUxHKB_L1RSPpWIeCfttd52FEnlVATnFKh6PHIk3jzJh7Jj8ByV29EzJ5hyKeUd791zQOcnOYvTWVREFXBKznqEsPHekfEtE6tNYIlvc1i2kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با حکم پزشکیان، محسن رضایی به عنوان دبیر شورای عالی امنیت ملی منصوب شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/140811" target="_blank">📅 21:33 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
