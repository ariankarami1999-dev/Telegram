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
<img src="https://cdn4.telesco.pe/file/OG_0QGB-q0_5h2KKxyGgdJHPW9qpbzqgQPFjMQt1V7slUm7EIR5YEksDuUeyStZY5mjhGECw_N0PoF2gPWvX60rKcPIsqck1wGSV7Qz7YTRToZZGS7OBwToqUM5F0skSdOC9rBFaUQZWV5uwBzK1GQgWIBtu7iT-7BeLMU_8tGLAoezvZP-r2SY7zlXLO0KSsMWO4Sgo0Ofcw_gptdU4zLFNyWCm_4gqD2Yill2KKgTNhmwvNZD2pEJ80LfK3iEwx6aSwiv_0DzvLIERLhtuq7ITRu772-yZ7vRsifhEPsE_REuVmh-z9iA0wtOOVGtuDGXmciJn5lbgZgz3Yyv9iQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 356K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 18:03:59</div>
<hr>

<div class="tg-post" id="msg-17137">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cac8f1356.mp4?token=febXmLZIQKhEu5myDJ_c9hjgSJ3uLei6Xc6AaNkvVbA3B_6pDhCsu3B5WMkXfSg5WQZkSPa2luXLFc2SCZKwTpdhCwzb44Bor6BbSNRWxTwXpOXTouW8BDxCfD3IIFQnVU3LmZi5flvANQn0LpgxAA0PkPW0etpKDbrLR3RoSkGMLumoAhKfRVGvGngfuwbDMAoTT_8ha13I-d_XuDD4IR1oFgTG-0ElirC9lond20--MXob869pHRsxPbRiA3YV759tZJgHmfWcLUerrHQ22pTG3xzpvM4Ct9wsgpdtR3aCBp-fjHR2JSlEY0pMlUDcYlKQDHm8aKjsinK595GJhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cac8f1356.mp4?token=febXmLZIQKhEu5myDJ_c9hjgSJ3uLei6Xc6AaNkvVbA3B_6pDhCsu3B5WMkXfSg5WQZkSPa2luXLFc2SCZKwTpdhCwzb44Bor6BbSNRWxTwXpOXTouW8BDxCfD3IIFQnVU3LmZi5flvANQn0LpgxAA0PkPW0etpKDbrLR3RoSkGMLumoAhKfRVGvGngfuwbDMAoTT_8ha13I-d_XuDD4IR1oFgTG-0ElirC9lond20--MXob869pHRsxPbRiA3YV759tZJgHmfWcLUerrHQ22pTG3xzpvM4Ct9wsgpdtR3aCBp-fjHR2JSlEY0pMlUDcYlKQDHm8aKjsinK595GJhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارسالی : حمله آمریکا به اسكله صيادي بنود در بوشهر خدا راشكر خسارت جاني نداشت ولي خسارت مالي حدود ١٢قايق صيادي دوستان اتيش گرفت
@withyashar</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/withyashar/17137" target="_blank">📅 18:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17136">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آلن ایر، مذاکره کننده سابق آمریکا در برجام: فعلاً احتمالاً در چرخه بی‌پایان «حملات و سپس کاهش تنش» گرفتار شده‌ایم ! دلیل اصلی این وضعیت، اختلاف بر سر تعریف «باز بودن تنگه هرمز» است.
@withyashar</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/withyashar/17136" target="_blank">📅 17:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17135">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ارتش اسرائیل (IDF) اعلام کرد که اخیراً دو تونل دیگر متعلق به حزب‌الله در شهر مجدال زون در جنوب لبنان تخریب شده است.
@withyashar</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/withyashar/17135" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17134">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وزارت امور خارجه ایران: عراقچی، در گفت‌وگوهای تلفنی جداگانه‌ای با همتایان خود از عمان و ترکیه، درباره تحولات در تنگه هرمز گفتگو کرد.
@withyashar</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/withyashar/17134" target="_blank">📅 17:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17133">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbiu-K4QacS09w44dA_CFb_gLgldzOkVuAJQgAUvzr_cOgi-1-iW6N8nbLSWsYP9pzjAI4TL9nYQTk2GLZJl7Jgw1pJKIiFmhqxJPleKDGHsnTgFWGUZHtTfW6OF2PBgmGcipGAchGN7d9tlSISDkHXEeXPE5Y7ELHiBxvN_XppRBwrChFg8rQAXKugjwFXItn6H42fgUMYGE6B6nYmpNMt5y7kmIbS3auT9O0F4IdX86Jo0ztw8BGc9yV-56-o9_aJnXwxMfA7wNAb4iOBj7ApRWY7IIGTBBIQfpzH5XnitECFfUF17Nh7rdPNQReSezkA9LUVqMxDCc0XnDPCURg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر نادری که صبح امروز توسط یک دیده‌بان در شهر اصفهان، مرکز ایران، گرفته شده، جت‌های جنگنده F-35A Lightning II نیروی هوایی ایالات متحده یا گارد ملی هوایی را نشان می‌دهد که بر فراز این شهر پرواز می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/withyashar/17133" target="_blank">📅 17:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17132">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">۳ پا : مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی الازرق اردن با ۱۰ فروند موشک بالستیک در هم کوبیده شد.
@withyashar</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/withyashar/17132" target="_blank">📅 17:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17131">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نیویورک تایمز به نقل از فرماندهی مرکزی آمریکا (سنتکام): طی دو روز گذشته، بیش از ۱۷۰ هدف نظامی ایران را در جریان حملات هوایی مورد هدف قرار داده‌ایم
@withyashar</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/withyashar/17131" target="_blank">📅 16:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17130">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f75c9892.mp4?token=btsbk2D2UB38FKftMRUIWfEfIDHpbtx2PjC43jR0XpKz6KBRCQwAWJj9cGmk3UPo9V5MIQOGoN-8Vf3Tr1GhC8IRulH_c7e5u-DxUNQ8lhvZ0X4NqBUBo5SormTABMGkrymI5bwXt-dJyqUFVn6A5NuTq_w0Er5t4zB_llbRuDzuZnzIkWrYBXlWB6rYmN0Ga2VzlZZ569e4SBiJ2CpgbhlJvRGp5AE104me2kI09q5XMXUNeaxdCy_XgB9yGSebgUcS4SChVvMqmVPquAXtEEsa5Ii2wI-zapWTwWsMruLchUKNbryQXKBb5-ESWYPKybYl41SJA897J3A-RltFDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f75c9892.mp4?token=btsbk2D2UB38FKftMRUIWfEfIDHpbtx2PjC43jR0XpKz6KBRCQwAWJj9cGmk3UPo9V5MIQOGoN-8Vf3Tr1GhC8IRulH_c7e5u-DxUNQ8lhvZ0X4NqBUBo5SormTABMGkrymI5bwXt-dJyqUFVn6A5NuTq_w0Er5t4zB_llbRuDzuZnzIkWrYBXlWB6rYmN0Ga2VzlZZ569e4SBiJ2CpgbhlJvRGp5AE104me2kI09q5XMXUNeaxdCy_XgB9yGSebgUcS4SChVvMqmVPquAXtEEsa5Ii2wI-zapWTwWsMruLchUKNbryQXKBb5-ESWYPKybYl41SJA897J3A-RltFDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">l
نتانیاهو : حمله به ایران مانند برداشتن سرطان از بدن شماست.اگر سرطان را از بین نبرید، خواهید مرد.
@withyashar</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/17130" target="_blank">📅 16:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17129">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyMgk5ST3pTPpZbKdSEp_8sxmI4SeuPR0WRLi7EYHTWSI2GVUpafRBGkaZPS54a4DCC6LVtRyGlDRT9-4cT-i29HxVIO2bRX6eSsYcETOsjf8uolOgUA8dWahpzLxxZWiNhDWZeykBKupeDfv-zeXSeg8FObmEyGyjDqqQh-l8uQKkR-B1qMqYX94H_k3FdHXXgBlce_g2sL0TySKi-dO4J8vHC08atalud-DS7hyvJamo--0XdIYllCWHYTHaNfIXZYULYGmZ9_u7ixAtW3lDIkxdsA8s5E4HH7E6sUMnpvdhFkXqVd8S4pxrDvHD1GdUBSLuWHzg_8ejNYc7L5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان پهپاد شناسایی آمریکا در آسمان زاهدان سيستان و بلوچستان
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/17129" target="_blank">📅 15:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17127">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54fd028548.mp4?token=QpfxbNR0tZgRD-o6YBkIQex9BPZMA08aklyeiMopDyIn0ANyeR93q8c4GsMrwZ_9TVcTr_XHyAhEMYi5BqEuS2i6tZuzFvQABB7FJZTevgoIL6euVUz-5dnBrFB_niVSC5a4QPDryounS5IAx4RfsjUIShG02pXRS6aLoVi5WXGH-3IF-WO6guDHet_Ym9aC-dwvAWdvIU4NANqog5xxA-BMmxG50vWWQFrvjO5hWQNClLsUdLlsFmN-u658ba_CQ_2-3mBQ7PwnEuf5R0S4tN739ccSy2jkVR9gBIMtuI1IiW2ubwaqeQerRdiEKTltUcWQmqGOAJqza1OhXW4AEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54fd028548.mp4?token=QpfxbNR0tZgRD-o6YBkIQex9BPZMA08aklyeiMopDyIn0ANyeR93q8c4GsMrwZ_9TVcTr_XHyAhEMYi5BqEuS2i6tZuzFvQABB7FJZTevgoIL6euVUz-5dnBrFB_niVSC5a4QPDryounS5IAx4RfsjUIShG02pXRS6aLoVi5WXGH-3IF-WO6guDHet_Ym9aC-dwvAWdvIU4NANqog5xxA-BMmxG50vWWQFrvjO5hWQNClLsUdLlsFmN-u658ba_CQ_2-3mBQ7PwnEuf5R0S4tN739ccSy2jkVR9gBIMtuI1IiW2ubwaqeQerRdiEKTltUcWQmqGOAJqza1OhXW4AEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برج اسکله گمرک تجاری بندر چابهار @withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/17127" target="_blank">📅 15:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17126">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc71b6295f.mp4?token=JhpEsILITa_wMQhkarARw3bHr39KPtH4KvyAcuFLAQ5RbrW-Iaq1EBuMPipfLXnEgOT1FaBwFFidc6oemQXHq2xx6iSWSPm7UzZqpOXgMcZxbnLPNOspljAirAr0x3GprrxmKAEZNUynhOME5dLU4ORzWFNmWd4bi9hZInltpjJ8BtaobEkAwBgrK6uS-ERb2lIpG3rTn2RwsngEepmJu004uHiaQzinZqIDhvKDl5y0ckUDLKEGK6_lYfoJlL9RLkeG08uFOA2DLCxotbhrmKsxRRHTpAqgXVpL4oLwBnP39n0jXYh9gFtjecHrJqyqtvQ27YmOpcIRPnF9Lieztw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc71b6295f.mp4?token=JhpEsILITa_wMQhkarARw3bHr39KPtH4KvyAcuFLAQ5RbrW-Iaq1EBuMPipfLXnEgOT1FaBwFFidc6oemQXHq2xx6iSWSPm7UzZqpOXgMcZxbnLPNOspljAirAr0x3GprrxmKAEZNUynhOME5dLU4ORzWFNmWd4bi9hZInltpjJ8BtaobEkAwBgrK6uS-ERb2lIpG3rTn2RwsngEepmJu004uHiaQzinZqIDhvKDl5y0ckUDLKEGK6_lYfoJlL9RLkeG08uFOA2DLCxotbhrmKsxRRHTpAqgXVpL4oLwBnP39n0jXYh9gFtjecHrJqyqtvQ27YmOpcIRPnF9Lieztw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون ترکیدگی لوله گاز شهریار
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17126" target="_blank">📅 15:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17125">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">۲ موشک بالستیک از شبستر، استان آذربایجان شرقی شلیک شد به سمت اردن
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/17125" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17124">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zv7bTkC5fK3RNONYaS6WUGGmXusBE291SIg0uNYn4HbxBgWsaiGHofA2bqwHAux_tfsZEOwNaAAWRt0XeRG1CCIrqIrkSv0Ddxp2AQyS-ny5vqJWqF03NNsZCjwX0AL8W0fnUJhwVRWCdpBozJZu6sbOyYd4CxFjdq1jMnaozXWW0JibkjEQQo1T5GXp7xmHgDtDt1VvPH9sOmtAZBcoT5QcRXhgmXHQ-LZlcl9KpeywFinpRiqY6eSF1LUNFWq_sXFng3mUs_ArzbgYUZ4r9g9V7FeMihjfH5pKCFupD0d_wOkNrhCMHz5T3EU9hr8Qlqrafx3bH0YqxNKm-UlbDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش از پرواز گسترده جنگنده های نیروی هوایی ارتش بر فراز مشهد از ترس حمله به مراسم @withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17124" target="_blank">📅 15:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17123">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVzdeyvDGnznBgn7Z0pzHV_e6khaKk8r2cgSALHLUfFu-KueNyIJHtGiKcwAlWdrUsyR4jYByWnvMRKdfVVC2VdTHKmB8bX0Rh50GkeJi6rkmZQqK0Ifu0VDcZT55rfD6qOKBUA0okbfVTtweZi6lGTKqEkU5eX9lRsfIxbaehonKxnzXvFSXr7USwca1EogxPs6I99sh5G6E1VxezSYQERDnJZsmDgeynVps7vaY4JFKGCb-bmYBuzMv5cDAsp7lYBAmQv9yz42N00Fal_jL8N6tqJaWCGUT4YKnkpwtWOSg9v12kV8ttcKcbhblcAHYJm0dHD5ZcGDhxOLcRRxhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو ترامپ داره بصورت زنده از تنگه هرمز گزارش تهیه میکنه برای صدا و سیما
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/17123" target="_blank">📅 15:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17122">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سپاه ثارالله کرمان هدف حمله قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/17122" target="_blank">📅 15:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17121">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">آژیر ها مجدد در اردن فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/17121" target="_blank">📅 15:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17120">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کانال ۱۴ اسرائیل : علی خامنه‌ای حدود 600 میلیارد دلار(۱۰۹ کوادریلیون تومن) ثروت داشت !!!!
رهبر سابق ایران، علی خامنه‌ای، در حالی که تظاهر می‌کرد مثل فقرا زندگی میکنه، املاکی تو ترکیه، کوبا، مکزیک، ونزوئلا، سوریه، دبی، بریتانیا، روسیه، عراق، ارمنستان و صربستان داشت. همچنین مالک چندین هتل تو اسپانیا بود.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17120" target="_blank">📅 15:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17119">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نیروی هوایی اسرائیل:وضعیت حالت آماده‌باش در سراسر اسرائیل اعلام شد.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17119" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17118">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حریم هوایی سوریه بسته شد
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17118" target="_blank">📅 15:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17117">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گزارشات از شنیده شدن صدای انفجار در کرمانشاه
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17117" target="_blank">📅 15:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17115">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UhbpDEc7Jbblxgie5C0mqJL9B6YENK-qDRW5_c1yJLg0HMuBZDVQiAaBtUbaaioQBlz3g0hycmebmMtj0YcGA-hvxpfyQBnHIdh_HXxxG8aEC6cvR_vkPzsGC2FzY8nQI8p7JVbqcKiQyDstQNzASRmJxy1GN8k-w1Fx-lkFIAIE8T_YgAMfekvTNogiQPlSILjXbs_KLpILE9JReX7cR2L0gb9tX30bTfzyZWGkbHP77NYM1YhhsgKRBd8-kN4LPJncP1req680XzD-RDmSJKkCy4I-iR78EgydkbdDPD-5pIRNiYTqr-fv1O_AqxYJRfwu94Nf-CuQ3jCnKkCFuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tQCrRICO-99ttUop-ETwpUishGenAl0yKRfJ2vizeCSYucBtaXbet3libpiWfmWK-8tLoYGMjujErGsIXycWFT6huOnCHwtA7GRySO8WGOH95oSA43g1-OqkEuHMAB1qecUoxEE5rRupf_fOZHVgp6xRmwGhiM_kslw827dkxEpQ770U5UXEwH6VccsdUmGM4aqPU8ucprl6FEv04giTM0HHWgbdUtSTRpAj7m-b_CIO5xv8ASnvxRc_QAdtUPRTcTQy60zVi-nGb6X2NHV2Q55SBugJBxatB70bBJRB8wvGnms-tjELxvuTBi31GabrowPdSVUyk0SJHdYTCJT2xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت قایق های سپاه در اسکله بنودِ شهرستان عسلویه
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17115" target="_blank">📅 15:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17114">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حمله آمریکا به شادگان در خوزستان
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/17114" target="_blank">📅 14:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17113">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وای‌نت:  مجدد یه کشتی جنگی دیگر آمریکا تو خلیج فارس مورد حمله قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/17113" target="_blank">📅 14:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17112">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گزارش از پرواز گسترده جنگنده های نیروی هوایی ارتش بر فراز مشهد از ترس حمله به مراسم
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17112" target="_blank">📅 14:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17111">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">آژیرهای خطر در پایگاه نظامی آمریکایی التوحید در بغداد به صدا درآمدند
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/17111" target="_blank">📅 14:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17110">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تانکر ترکرز: ایران به علت احتمال ازسرگیری محاصره دریایی، 10 میلیون بشکه نفت را در شب گذشته صادر کرده است
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/17110" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17109">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پایگاه سلمان حاجی آباد هرمزگان دو موشک به سمت تنگه شلیک کرد @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/17109" target="_blank">📅 14:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17108">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گزارش انفجار در شادگان خوزستان
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/17108" target="_blank">📅 14:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17107">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پایگاه سلمان حاجی آباد هرمزگان دو موشک به سمت تنگه شلیک کرد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/17107" target="_blank">📅 14:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17106">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خبرنگار وال استریت ژورنال: علیرغم صحبت‌های دونالد ترامپ مبنی بر پایان مذاکرات، این احتمال وجود دارد که به زودی به آنها بازگردیم.
پویایی اساسی، بیش از هر چیز دیگری، تمایل به عدم تشدید تنش است. و من گمان می‌کنم که این موضوع در واشنگتن شدیدتر از تهران احساس می‌شود، هرچند که در هر دو مورد صادق است.
@withyashar</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/17106" target="_blank">📅 14:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17105">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سامانه های پدافند هوایی اردن در حال فعالیت در آسمان پایگاه هوایی موفق سالطی. @withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/17105" target="_blank">📅 14:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17104">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">منابع رسانه‌ای: آژیرهای خطر در پایگاه آمریکایی «حریر» در استان اربیل در شمال عراق به صدا درآمد
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/17104" target="_blank">📅 14:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17103">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bd8d735f9.mp4?token=eM8JlTZk-6UO71fndf7SHeT9mncXfdVaYln_eYc9MGaqUdUoXG9SkykeqJBs4LCNY5tyeYApcv94suiZbXN2nOLeMsXpF4GDU-kg6u4AhVMUF9-SPtSFK7Hvc6a2NRLg7dZX6OCDSVuUWoPeM6b7r3By9YlTx6sCCvwkhBfCtz3OUjhALRrJeDf4rtox49TJqnSskpiNeiba919e8BXXTtfebCP6QTaCKNC2AKJFUM0GVh_btEqvMCCoar1qU4tMK4cOR8sasZbH9RN8-MSbZ8rQu2gCnLj5TXT_YY06dVIrNVMlZB1wb8yf504V-yJHSXEUgiCIuCluVwAAfxu9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bd8d735f9.mp4?token=eM8JlTZk-6UO71fndf7SHeT9mncXfdVaYln_eYc9MGaqUdUoXG9SkykeqJBs4LCNY5tyeYApcv94suiZbXN2nOLeMsXpF4GDU-kg6u4AhVMUF9-SPtSFK7Hvc6a2NRLg7dZX6OCDSVuUWoPeM6b7r3By9YlTx6sCCvwkhBfCtz3OUjhALRrJeDf4rtox49TJqnSskpiNeiba919e8BXXTtfebCP6QTaCKNC2AKJFUM0GVh_btEqvMCCoar1qU4tMK4cOR8sasZbH9RN8-MSbZ8rQu2gCnLj5TXT_YY06dVIrNVMlZB1wb8yf504V-yJHSXEUgiCIuCluVwAAfxu9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سامانه های پدافند هوایی اردن در حال فعالیت در آسمان پایگاه هوایی موفق سالطی.
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/17103" target="_blank">📅 14:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17102">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سفارت آمریکا در اردن به دلیل «گزارش‌هایی مبنی بر وجود موشک، پهپاد یا راکت در حریم هوایی اردن»، دستور فوری برای پناه گرفتن صادر کرده است
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/17102" target="_blank">📅 14:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17101">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6_lRSemA11KqkwbxYUkXoWkGPoIaDSBp81O1ORs3_fO0c93pExSRGMoN0FNeMK7hjUrrv0c0p-iGV97_3D9T-xapIjqfGWsQxegAvhbPvxtUVwoy5agMj2KUSSzdC405QWYaDSW_1R5TUYvRDI2C74NCNLrntYn1KOFPmRrBnGRG-BeKdPZaQcWUV0jICBWGS5ZCPGshE8uSihRrPDF1XgsT4q6Zd_5XlCjFgE7Dn3x01tAybYHHlvm91y22EDidOWL3cC_l5N0GwMM7s_zMyrR-yKxKH77IZqEzCRK1QwZu0tCfMSPURKLyEWHtcix1QXXtovgcasTKwgMLIAkzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک موشک از حوالی تبریز
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/17101" target="_blank">📅 14:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17100">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دقایقی پیش موشک های کروز تاماهاوک در بوشهر دیده شد
@withyashar</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/17100" target="_blank">📅 14:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17099">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/17099" target="_blank">📅 14:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17098">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گزارش ها از نزدیک شدن جنگنده های اسرائیل به مرز عراق و سوریه خبر می‌دهند
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/17098" target="_blank">📅 14:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17097">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7-a7q2psSTL1uqSNcDUPxvuE877_TpIAK6gPkh51h-vUMvBLNpIq8CiautI8c8s4z-uD2J9IA7qoeSf_7wgQlBO61yV9f9oNPaOA5glIk3A6xGRtozlZmyAQmj8J4zIqzz-q8GzaJXsVIWjVxz29H-YI2-CDAqbrnjtIkYSZaXrPypKJNePHNNdN5EF0QRdtEqos4SNVe3Um0NvrVfPNPNuS7mAVqWkkR67ZFltmecj9RjW6LH5gu2ZHK9CxH61Tg8HYYj-FInhFdBzT1wfXESrSmejbAglBG0cnSgZzccWIGVcqwzYmTgDIq9vAK-Ca4nZb6f722tUA4fJkejMSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس زیبای مقعیت و لحظه شلیک لانچر موشک در خمین
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/17097" target="_blank">📅 14:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17096">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/17096" target="_blank">📅 14:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17095">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بعضی رسانه های داخلی خبر دادن مجدد کنار نیروگاه هسته‌ای بوشهر مورد حمله قرار گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/17095" target="_blank">📅 14:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17094">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تانکر ترکرز: ‏تهران، در انتظار ازسرگیری احتمالی قریب‌الوقوع محاصره دریایی نیروی دریایی آمریکا، در یک شب بیش از ۱۰ میلیون بشکه نفت خام و نفت کوره را بارگیری و ارسال کرد.
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/17094" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17093">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گزارش‌ها از صدای انفجار جدید در کرمان
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/17093" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17092">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گزارش صدای انفجار هایی در پایگاه  بندری علی السالم در کویت
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/17092" target="_blank">📅 14:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17091">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شلیک موشک‌های کروز به سمت کشتی‌های آمریکایی در نزدیکی بحرین.
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/17091" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17090">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آلارم حمله  صدای انفجار و درگیری پدافند در اردن
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/17090" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17089">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36ca620126.mp4?token=FO_7fk6bHAtJpi06YRBfeZE92Nt4ZtJ36KsAeyAm42FNno2LqRLPyNDTeSKI8wrcquf2ghMD40pLWujqL2FY6tbWw4JO8f5s2YEF82CnkTBym2cbHSefBZLSeAJ_5fRSlvB5hvsyGV5DM7pcs-ZYojnwW6ELtlvFqcni49mgJUg2B9TmQJHLeUnZIild46a83kCTJk2bO-cMtSvWSDoo-vG3HBLH0Jn7fW6pDCFwEK6nb1oqwyYkfVPVR7mQpnuyPYzfZY3ITCLVAanqVW-d0CX9dz09tnoB7jKIa5wwYs5rJob4BaDjJ_sJlbZvPGh-g6A1kGaGA50Uas_5TpDs3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36ca620126.mp4?token=FO_7fk6bHAtJpi06YRBfeZE92Nt4ZtJ36KsAeyAm42FNno2LqRLPyNDTeSKI8wrcquf2ghMD40pLWujqL2FY6tbWw4JO8f5s2YEF82CnkTBym2cbHSefBZLSeAJ_5fRSlvB5hvsyGV5DM7pcs-ZYojnwW6ELtlvFqcni49mgJUg2B9TmQJHLeUnZIild46a83kCTJk2bO-cMtSvWSDoo-vG3HBLH0Jn7fW6pDCFwEK6nb1oqwyYkfVPVR7mQpnuyPYzfZY3ITCLVAanqVW-d0CX9dz09tnoB7jKIa5wwYs5rJob4BaDjJ_sJlbZvPGh-g6A1kGaGA50Uas_5TpDs3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از زنجان هم موشک پرتاب شده
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/17089" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17088">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آلارم حمله  صدای انفجار و درگیری پدافند در اردن
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/17088" target="_blank">📅 14:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17087">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/di2uhuRHFWtuSA3JAOCFA9muf-RuF8Smpg-Te6p-pvQ9CoctHpFWVHd-t7Sq75PNH6D11jrFwwTnmSNmRAAOOGh-F4T-KnGHG_bsqRuoZCDhp8LSiQsA3y8n4Bm3YNoLFi4MM8vg_UudJbAjznoZUwsZjcZMo72-Na0jzX7PndbQzI5iVHmgOFC-liXzJ-ause6UeiEPPGpFFd2bCe36yoW0Fr26BbUCkzUMKOdBAp_ABCyymYBOCR6PHY-7dSy0dqW7hLYxS_1Knm-9InlFRBKiJhdkb_WKMJd90uzaErm0njINL04a-gaZM5qyqoFPrI0VWhQGkeH6MvEiIUPMUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه موج جدید حمله را شروع کرد :
۳تا موشک از بین خمین الیگودرز بلند شد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/17087" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17086">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/857d372470.mp4?token=M6Dug1B6sC4r0jIZhOMYoNAsZLtiS8-xZVxVzbBsk0vfRzB9T6_x-1YMURlzhcDX7xo_k-wMRiZIrCRmgMzdJVMH-uC2yV7Ap53Ak5xvL0KptjU1DgXQXzVvIeZnivMszbdoFMELlRzoCQECNIUAanahgpjnmVf4JdupdMcZMxr9BB7D5xZLX0ewzhM3jvmpbyjA_uVVn44MWCmViyyGrBFqs4xGR3dKt6uxp3QlfFD3XTKd6ezVvHYGO_EeKzrYuGmwU5O1LWfCZMfmtSu2zVd3YQOL9oddpzgh-u96kihp5upE6pgGCid1ZdB6ZhJHUzGqDsZWxm9783IqqoIvj1iKkvsGqGa7eL6bnBuLvTEp8p--8Gx1Pxd6o5Z6nAezkSR3q9x9Mczq0svlKnRqb3dV9wR1niBe3ia6Ph66rbBtISQhd9kpjcyTstt2-UuTm3Gjn4zyVUUiORX5AjFwRcJGRdWEe9g267X6hgT12elXKnYxpVMTeqNvv_N-2y2kQ9JaaBcowQN4ECOETOZfnWtbwnMJnkTdltJFf4AC9qyJZc5U9dn3Emd4gce-MTNmo5KTgy-8yzwuRTDBPU3XV5sIssdV8_F3JQuYgIIRaDQBlYlM2Vw-AKaQ8Fnf_xouz2g3lFTP_DLCJ7JO-DoCzkLswSzw7cCl6-SyjH8ygag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/857d372470.mp4?token=M6Dug1B6sC4r0jIZhOMYoNAsZLtiS8-xZVxVzbBsk0vfRzB9T6_x-1YMURlzhcDX7xo_k-wMRiZIrCRmgMzdJVMH-uC2yV7Ap53Ak5xvL0KptjU1DgXQXzVvIeZnivMszbdoFMELlRzoCQECNIUAanahgpjnmVf4JdupdMcZMxr9BB7D5xZLX0ewzhM3jvmpbyjA_uVVn44MWCmViyyGrBFqs4xGR3dKt6uxp3QlfFD3XTKd6ezVvHYGO_EeKzrYuGmwU5O1LWfCZMfmtSu2zVd3YQOL9oddpzgh-u96kihp5upE6pgGCid1ZdB6ZhJHUzGqDsZWxm9783IqqoIvj1iKkvsGqGa7eL6bnBuLvTEp8p--8Gx1Pxd6o5Z6nAezkSR3q9x9Mczq0svlKnRqb3dV9wR1niBe3ia6Ph66rbBtISQhd9kpjcyTstt2-UuTm3Gjn4zyVUUiORX5AjFwRcJGRdWEe9g267X6hgT12elXKnYxpVMTeqNvv_N-2y2kQ9JaaBcowQN4ECOETOZfnWtbwnMJnkTdltJFf4AC9qyJZc5U9dn3Emd4gce-MTNmo5KTgy-8yzwuRTDBPU3XV5sIssdV8_F3JQuYgIIRaDQBlYlM2Vw-AKaQ8Fnf_xouz2g3lFTP_DLCJ7JO-DoCzkLswSzw7cCl6-SyjH8ygag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که ترامپ از بمب افکن ‌B-2 تو ثروث سوشال پست کرده همراه با آهنگ بمباران ایران
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/17086" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17085">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c1e5bc22a.mp4?token=hdq_Vin9Es8sFWuBJNtbSglCiiPPvt3mikZRDhaBup29gZiF6V9sROTFrnk-ahPQmy_5vpu6fF6RY8sridceniCkyuWm_w6rJM5j5x0EoAlC5Cc-oyYBtl23H5evO7YH0OXFJX7qCUFBs1YSCbvrksfx51MNAYNOIHsydkHn6u_nSQeun8NV7uWYnjkQ0odbIXTDnIa-i3TEw8yjOqmFjdKPWTQukDt5BD1AQFx8-7f-x8b-YlrBzIkUhszN3I1eDFAJ564LZauRmBSlB2CFFYZ_wusK80hWVMb8hb5LjJ8wWgoD_K0IxMNR2mvF1hX0BT2nKp1uRV_vqgQeNbzUMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c1e5bc22a.mp4?token=hdq_Vin9Es8sFWuBJNtbSglCiiPPvt3mikZRDhaBup29gZiF6V9sROTFrnk-ahPQmy_5vpu6fF6RY8sridceniCkyuWm_w6rJM5j5x0EoAlC5Cc-oyYBtl23H5evO7YH0OXFJX7qCUFBs1YSCbvrksfx51MNAYNOIHsydkHn6u_nSQeun8NV7uWYnjkQ0odbIXTDnIa-i3TEw8yjOqmFjdKPWTQukDt5BD1AQFx8-7f-x8b-YlrBzIkUhszN3I1eDFAJ564LZauRmBSlB2CFFYZ_wusK80hWVMb8hb5LjJ8wWgoD_K0IxMNR2mvF1hX0BT2nKp1uRV_vqgQeNbzUMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار
کرمان هم‌اکنون
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/17085" target="_blank">📅 14:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17083">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pQ2Mcv9VDlXpGVJsK7th7fdgs1VYhwADoTzVbkAz6URiIb0lu15QYNoCRuYItLus89ACFSKK9eLAXVCd83UiL1u4Jbsi-11NNvFpVJcOIVp7o2XftoJ20X0hGHOFQQlGdlzbXsNgRKd1rv8HnHf0Jc0Oo9irkgLLzvH_Qq2_G8Pry-1IffP5qP1n55HNAO68nfD4HtwqTy7OTd-UdNKOOtfwwMRl-zlo2Lb4dWpn95mvuRgSjbQ4KoiZ7eoBmfgf6kdjqq3POoasL8ygeUHdenntt0nbLIy4NEnfqJl27XvEgtqos-ak_-oPnPliNzWa0B1UzEKUgPx3Gp7aGPbzRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VBzyccLBduL6cUnWkZWtUjIFYdZTaa3LnV4feE6Pr94HvDNaKiNSrzb7dwRHg0Ogq_danzBrmrW0Y_k6U6OxNhtikUuOShCcRYnPVmDPI3l9_gyXdJGh7tSA6gQzQ3w-7uwMMa1CfGwr30umzX8z0kmIpldb4sbXXjeUCx_C-qYYzkv1pOGccg_cf5YMCQsyetOkGFsa5vWqlLF-2KyBqKcs-Wd4JyikolF6exngcYoLBmyhA9T-peIzXnBhjLYhZ2xjCk-K4yHSrWUbMws-xiZG8u1wLndNUvw-v-IX2tbo6vYptj5R6UtTtZcTC65RDTpo_lq63gPGQvUtX_Hw0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر از‌ انفجار شیراز‌ الان
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/17083" target="_blank">📅 14:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17082">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انفجارررر شیراز
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/17082" target="_blank">📅 14:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17081">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">شنیده شدن صدای چند انفجار در چغادک بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/17081" target="_blank">📅 13:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17080">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">صدای انفجار‌ بندرعباس
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/17080" target="_blank">📅 13:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17079">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">منابع نزدیک به کرملین: پوتین احتمالاً جنگ با اوکراین را تشدید خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/17079" target="_blank">📅 13:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17078">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXEe6mPN_QXUy95uHtQHKpLVMr2tXcIM24MdYsjGnUWWRkTIdtCWP9aPIoTFEUFkxVA9zVgyBJGNnMTeYp2sDdLfbVpsjR4RD36uhAYLRpiZBTdLiyqMWoCyayvu0owYro8EQhZr9OlRvFb3O786Cv3uCgVuloZjFN-ND1Td79Bb3t9gySPO7lfRUJj8mrwefX0PPRBogdkLs4VjYITvQLazu22XgWojiy-l8LeEF2ufuWuPYUBvxueRNpX8p5VKRHYtWfOIbx93HVNjS3nUVIiVS1-9mb8_qoGhADKvwny9g27gfKGczi03wlRHu-mBV6BVWpNQNh3DtQzGgKNP2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آثار حملات هوایی شب گذشته آمریکا به پل ترانزیتی و مسیر ریلی آق قلا
@withyashar</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/17078" target="_blank">📅 13:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17077">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وزیر امور خاورمیانه بریتانیا: حملات ایران به شرکای خلیج فارس ما، تشدید خطرناک تنش و نقض آشکار قوانین بین‌المللی است
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/17077" target="_blank">📅 13:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17076">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کانال 12 اسرائیل به نقل از یک مقام اسرائیلی:
طرح‌های تهاجمی آماده‌ای علیه ایران در اختیار داریم
@withyashar</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/17076" target="_blank">📅 13:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17075">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دلار و تتر ۱۸۱،۰۰۰ تومان
@withyashar</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/17075" target="_blank">📅 13:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17074">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آکسیوس:ترامپ آتش‌بس با ایران را تمام‌شده می‌داند؛ نبرد بر سر هرمز آغاز شد/ مقام آمریکایی: آن‌قدر ضربه می‌زنیم تا باور کنند ما جدی هستیم
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17074" target="_blank">📅 13:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17073">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خبرگزاری CNN : صبر ترامپ در مورد سرعت مذاکرات،به ویژه آنچه که به نظر می‌رسد تاکتیک‌های وقت‌کشی ایران در مذاکرات هسته‌ای با واشنگتن است،رو به پایان است!
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17073" target="_blank">📅 13:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17072">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">همکنون تابوت خامنه ای‌ رو بردن تو دوردور مشهد تاب میدن
@withyashar</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/17072" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17071">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رسانه های داخلی انفجار‌های الان در بوشهر رو تایید کردند
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/17071" target="_blank">📅 13:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17070">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">۴ انفجار‌جدید بوشهر
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/17070" target="_blank">📅 13:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17069">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نماینده دائم روسیه در سازمان ملل: رقیق‌سازی اورانیوم در خاک ایران یک گزینه عملیاتی است
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/17069" target="_blank">📅 12:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17068">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خبرگزاری وابسته به سپاه :  آمریکا پل کریدوری ایران با چین و روسیه را زد  بامداد امروز آمریکا با موشک کروز، پل استراتژیک ریلی «آق‌تکه‌خان» در استان گلستان را هدف قرار داد. این مسیر که محل ترانزیت کالاهای روسیه و قطارهای چین بود، پیش‌تر نیز هدف حملات مشابه بوده…</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/17068" target="_blank">📅 12:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17067">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYCzkPG-mooXDTMSPS0HDCOjv-b-VE2-IajWe_sisd8C3CJhUd87Xu1NTt12f8_y3ff0ZYBBBC1fcCpg54NwzGtgBT-kBeXBlp91A1jsLUKJRtLwfq_utySMBK_6rgX5YmRpO28LkhNj3tRdmpk55zpfx9gK4mFj99MOosxKxynvTkmCzgXiu8y94ARvzDhrYWEyVHY6WjkIlyTpjjP1xe52L3u14vLjN83jAInRjyixiQEEncMYrFp5me9iI4pLjfYMYFvl7OLDgtCMGo3SbYb993i6MuHi03d24OzgxgwjuLGk1THrBp81Chx3ma7AsyOnoJskmaA9JDJWvMf6PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع کویت : امروز پدافند هوایی ۳ موشک بالستیک
۱ موشک کروز و ۱۰ پهپاد مهاجم رو که وارد حریم هوایی کشور شده بود، با موفقیت رهگیری کردیم
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/17067" target="_blank">📅 12:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17066">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مقام آمریکایی: یک سیلی به ایرانی ها می‌زنیم تا بفهمند ما شوخی نداریم‌‌ ، فضای بیشتری برای تشدید تنش با ایران وجود دارد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/17066" target="_blank">📅 12:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17065">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ورود محموله بزرگ ریلی چینی به تهران. ویدیو ضبط شده در هفت و پنج دقیقه صبح امروز گرمسار(دیشب توضیح داده بودم) @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/17065" target="_blank">📅 12:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17064">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آکسیوس: حملات آمریکا ادامه خواهد داشت
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/17064" target="_blank">📅 12:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17063">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmfIjkrev265rhUb9FbeHOpgGXI1h6QwtL109td-pOGV83y7Tz7J9RbPtwxIvfpxsav0Jnn6g-T0P2TBxromFrDzMC1eXwYA_FT5LLLoSI010OfzqTStqJQg734SBNgqJ6ALj6NIROkW4eTZfwP-u9Zbzg8JMSq2rObczUB39stb_GDo4-lzF4aaAG2gYNEv4IEpKNfFoYnlNQXNho_J1YIol98IrEqatx_lMVRTu57EfAbn5wesbwG1HgXSUOQU48qqA5bYj65AQJ03Aun4_JwtVRZ1zTXNu4iGtq3liOipxxjs-oMbPz9elvKCbnO11u2dU1Yw4ertgVdszWK2AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه براتون سواله که چرا آمریکا انقد زومه رو سیریک:
سیریک یکی از نقاطی هست که بدلیل ارتفاع و موقعیت جغرافیاییش اشراف بسیار عالی به تمامی ورودی و خروجی تنگه هرمز داره. توی روزهای عادی و وقتی هوا تمیز هست شما راحت تا خصب(عمان) رو با چشم غیر مسلح میتونید رصد کنید.(تجربه شخصی خودم هم هست) بدلیل موقعیت نسبتا کوهپایه‌ای منطقه سیریک نیروی دریایی سپاه با کروزهای ضد کشتی بیشترین حمله‌ها به شناورها رو از این منطقه انجام میدادند و سریع متواری میشدن. تمامی تجهیزات ثابتِ راداری و موشکی توی جنگ 40 روزه منهدم شدند ولی این الدنگهای اوباش بصورت چریکی و پارتیزانی از سمت سیریک هنوز اقدام به پرتاب راکت ضد کشتی میکنند و البته خب سنتکام هم مرتبا با پهپاد و ماهواره تحت نظارت داره و مرتبا پیداشون میکنه و میزنتشون
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17063" target="_blank">📅 12:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17062">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گزارش انفجار مجدد بوشهر
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/17062" target="_blank">📅 12:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17061">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">صدای ۳ انفجار بوشهر
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17061" target="_blank">📅 12:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17060">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آکسیوس: ترامپ آتش‌بس با ایران را تمام‌ شده می‌داند
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17060" target="_blank">📅 11:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17059">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067e87ce1e.mp4?token=fH4i3yI2yymHvZ2W1mIHWiD7IzcY-FhrQH9FfHPaKd7k-59kRdpB5RS7aRbrXeM09XjkbySJz27DVfXQZYyx1MzSxkPY5-R-Z6QVLs2VYHI7jlglnP48HrvLGK9ofU9pOlfuv40rqKd4Foya30w4PerXPyG6nxKWavJSu5aQ9q6S1xc5IJ3I2V7E3MKDaCGiVseU2VJAnyX-WumtYY9VGRTFWiT0t7SK5s9mdu4FFC2ErSwTkb1gj8u3qmY8AQxRhBAuvwcKP3OUXF73NgVMHOcjinCzk1WQnpBNozwQ2FCbHGisDxRk8Jw609VJfLnT3XQgL2UokkzWmjwCdQtVPHMGhLief2ginuzCFEzFktcmst2CN70uEH3r7sc4gnQY_JFyNu_NONA1NEmBn3FVlYd2GWxhEA12-EbvVmA6JhWVkCZ6uLFknv7QAMakvPsOM-z11PG8VY3mpFIU-iflyWUFpASjpf3iD5dwKixQAp3EEvrILhhFtr4uHayqaqg9oi4xJ9ZqxN2e8IJIl4f4mM9psVueTn4qYcKQIOjDO10ZDtAvAWyCQxJi6UmLJMndvlHb7rR-DfOt4ranOSbI_2gGENvo6FPAC7yNvm48YYPRqYQRN0dIvc1-S4LysfwDvxBgmY_WLsM7LbWnRGuQq6yFsemzL9Q3BSymN4j1VNI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067e87ce1e.mp4?token=fH4i3yI2yymHvZ2W1mIHWiD7IzcY-FhrQH9FfHPaKd7k-59kRdpB5RS7aRbrXeM09XjkbySJz27DVfXQZYyx1MzSxkPY5-R-Z6QVLs2VYHI7jlglnP48HrvLGK9ofU9pOlfuv40rqKd4Foya30w4PerXPyG6nxKWavJSu5aQ9q6S1xc5IJ3I2V7E3MKDaCGiVseU2VJAnyX-WumtYY9VGRTFWiT0t7SK5s9mdu4FFC2ErSwTkb1gj8u3qmY8AQxRhBAuvwcKP3OUXF73NgVMHOcjinCzk1WQnpBNozwQ2FCbHGisDxRk8Jw609VJfLnT3XQgL2UokkzWmjwCdQtVPHMGhLief2ginuzCFEzFktcmst2CN70uEH3r7sc4gnQY_JFyNu_NONA1NEmBn3FVlYd2GWxhEA12-EbvVmA6JhWVkCZ6uLFknv7QAMakvPsOM-z11PG8VY3mpFIU-iflyWUFpASjpf3iD5dwKixQAp3EEvrILhhFtr4uHayqaqg9oi4xJ9ZqxN2e8IJIl4f4mM9psVueTn4qYcKQIOjDO10ZDtAvAWyCQxJi6UmLJMndvlHb7rR-DfOt4ranOSbI_2gGENvo6FPAC7yNvm48YYPRqYQRN0dIvc1-S4LysfwDvxBgmY_WLsM7LbWnRGuQq6yFsemzL9Q3BSymN4j1VNI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمان بحرین : 4 حمله به مقر ناوگان پنجم ایالات متحده
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17059" target="_blank">📅 11:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17058">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سپاه : تنگه هرمز اکنون به طور دائم بسته شده است و ایالات متحده و متحدان آن دیگر هرگز از خلیج فارس نفت دریافت نخواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17058" target="_blank">📅 11:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17057">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هم‌اکنون هواپیمای حامل تابوت خامنه‌ای و خانواده، فرودگاه نجف را به مقصد مشهد ترک کرد.  @withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17057" target="_blank">📅 11:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17056">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آلارم وزارت کشور بحرین:
از شهروندان درخواست می‌شود به نزدیکترین مکان امن مراجعه کنند.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17056" target="_blank">📅 11:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17055">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هم اکنون وقوع سه انفجار مهیب و پیاپی در بحرین
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17055" target="_blank">📅 11:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17054">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">همین الان فعال شدن پدافند مهر آباد تهران
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17054" target="_blank">📅 11:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17053">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6621f9c274.mp4?token=JU3DmDQtOs4KCZp1T2QXo5RFod5RqwUnwK2Z_T2dbnwHmt25i8OxbMLZ3eW1apRKcC_4MP69bWhPdDZqZgfXoiLzzdCCapirI-Q-m21u25fBPgv2FkDMdv01L6YENulmuZXulMSkb0dEDdkR-cL8q0PyKjd-rzmGgjzyJJadYaofmXQ1MenK_y00JI0YTpg7KlZsssHoPc7-FerKH9kK__2jKAxVtIXvlg7_IJNRpDeTq9QCy3BGLuOr6jkse6FbBpc2VnuPzLZMDzCJ6q5JCR3PtEvj1EABHopaXyDr4SUJMa7gGtTaKuOGXj28jMLLFzIC-tDycjgDJegHWccBTgYMME0vgFrqvCG5YHlaAyxhco5Gev-9ejpxZyFxp9LFDybA-n3Nrc00271g53C04Qupl3O8r7jpqjpAEIlFe0kiLTRMSDnvjnjOmABO1J7ymOOnJ2rdEBH9or9PiI1FF0XyDDSiJp21S4l3RUwbtpcHTdYizu2wRIULmVLfet6p7LmGTmKSoQPGKW-MsO6vEF_PlMcMwPDQ9iG5tx1KhJ06HQL8VFUYd0LqMEnKX7VHhiaxiC6ShsTrNTrSwBZk1nHtdS2xahEOvoUjgeq0Tal7X_D30W9h3FnfHaVEi__PUSa9eXIr1oOEoVLQOLeCgPg-Nt2rUpINXt_8pbf8-wY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6621f9c274.mp4?token=JU3DmDQtOs4KCZp1T2QXo5RFod5RqwUnwK2Z_T2dbnwHmt25i8OxbMLZ3eW1apRKcC_4MP69bWhPdDZqZgfXoiLzzdCCapirI-Q-m21u25fBPgv2FkDMdv01L6YENulmuZXulMSkb0dEDdkR-cL8q0PyKjd-rzmGgjzyJJadYaofmXQ1MenK_y00JI0YTpg7KlZsssHoPc7-FerKH9kK__2jKAxVtIXvlg7_IJNRpDeTq9QCy3BGLuOr6jkse6FbBpc2VnuPzLZMDzCJ6q5JCR3PtEvj1EABHopaXyDr4SUJMa7gGtTaKuOGXj28jMLLFzIC-tDycjgDJegHWccBTgYMME0vgFrqvCG5YHlaAyxhco5Gev-9ejpxZyFxp9LFDybA-n3Nrc00271g53C04Qupl3O8r7jpqjpAEIlFe0kiLTRMSDnvjnjOmABO1J7ymOOnJ2rdEBH9or9PiI1FF0XyDDSiJp21S4l3RUwbtpcHTdYizu2wRIULmVLfet6p7LmGTmKSoQPGKW-MsO6vEF_PlMcMwPDQ9iG5tx1KhJ06HQL8VFUYd0LqMEnKX7VHhiaxiC6ShsTrNTrSwBZk1nHtdS2xahEOvoUjgeq0Tal7X_D30W9h3FnfHaVEi__PUSa9eXIr1oOEoVLQOLeCgPg-Nt2rUpINXt_8pbf8-wY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره‌ای جدید، خسارات قابل توجهی را در یک پایگاه نیروی دریایی سپاه در بندر عباس تأیید می‌کند. یک آشیانه آسیب‌دیده، خسارت به یک سازه در امتداد جاده و ضربات قابل مشاهده که بر دو اسکله تأثیر گذاشته‌اند، قابل مشاهده هستند.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17053" target="_blank">📅 11:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17052">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17052" target="_blank">📅 11:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17051">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ویدیو از محموله بزرگ ریلی که از چین اومده بود ! @withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17051" target="_blank">📅 11:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17050">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">درود وقت بخیر خسته نباشید چرا حملات فقط شبا هس؟ روز ها چرا خبری نیس؟</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17050" target="_blank">📅 11:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17049">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromnima</strong></div>
<div class="tg-text">درود وقت بخیر خسته نباشید
چرا حملات فقط شبا هس؟
روز ها چرا خبری نیس؟</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17049" target="_blank">📅 11:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17048">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">قالیباف: آمریکا هنوز یاد نگرفته است که زورگویی و بدعهدی دیگر بی‌هزینه نیست. شفاف بگویم: بزنید، می‌خورید.
دست و پای بیهوده نزنید که بیشتر فرو خواهید رفت: تنگه هرمز، فقط با ترتیبات ایرانی باز می‌شود نه با تهدیدات آمریکایی
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17048" target="_blank">📅 10:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17047">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وزیر دفاع اسرائیل: ما از هیچ نهادی اجازه ای برای ورود به لبنان درخواست نکرده‌ایم و نیازی هم به اجازه برای ماندن در آنجا نداریم. ما خواهیم تا زمانی که حزب الله در تمام لبنان غیرمسلح شود.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17047" target="_blank">📅 10:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17046">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یک مقام ارشد آمریکایی: نیروی نظامی ایالات متحده امشب به دو پل راه آهن استراتژیک در شمال ایران با استفاده از موشک‌های کروز حمله کرد، این اولین حمله آمریکا به زیرساخت‌های ایران از زمان آتش‌بس بوده است. @withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17046" target="_blank">📅 10:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17045">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc7c1dd8a.mp4?token=dfXOHP7W4MDM78IfFjMelIpGLkF1LtL-uZhe1YIgJu9RLTgPwEa6Z6-O1HRnIPeIDJGZHo_jLrFhFdAR9TjCRubcoX4cJAluBjQnmLxO4mZqJrnNtT06zLTUXKRX_wDCOAbOs36TWM42xl9lVm1P_tzW7J9C4LrN4arrqCd4w54eTSiik3QBsZwEEBP274RuYxGMKRNpXj4VQArNRFrF4PuUg6DQSUnQUvcpYDQgpMGUQHUal2Ib04bpt2u85MRwgc-3KsASCrD6XWQdYk2FfF3f0qdv38QgHeAMcrKm-_llzPdvQGSgEQNmYDrVKQ2PVJhcam-M9FwR5bbwSNfQjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc7c1dd8a.mp4?token=dfXOHP7W4MDM78IfFjMelIpGLkF1LtL-uZhe1YIgJu9RLTgPwEa6Z6-O1HRnIPeIDJGZHo_jLrFhFdAR9TjCRubcoX4cJAluBjQnmLxO4mZqJrnNtT06zLTUXKRX_wDCOAbOs36TWM42xl9lVm1P_tzW7J9C4LrN4arrqCd4w54eTSiik3QBsZwEEBP274RuYxGMKRNpXj4VQArNRFrF4PuUg6DQSUnQUvcpYDQgpMGUQHUal2Ib04bpt2u85MRwgc-3KsASCrD6XWQdYk2FfF3f0qdv38QgHeAMcrKm-_llzPdvQGSgEQNmYDrVKQ2PVJhcam-M9FwR5bbwSNfQjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارسالی : سلام. من با قطار دیشب داشتم میومدم مشهد از تهران. ساعت ۳:۳۰ صبح که قطار توی نیشابور واسه نماز وایساد، دیگه حرکت نکرد تا ساعت ۷ که گفتن پیاده بشین و با اتوبوس باید برید مشهد. مثل اینکه ریل رو توی یه قسمتی بین نیشابور تا مشهد زدن. الانم سوار اتوبوسیم و هنوز نرسیدیم مشهد
😔
😔
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17045" target="_blank">📅 10:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17044">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTKAIUkmKFEKSj-HW8N3atCnd-uaUt0IppoBvGrsW_TObE5dZTQp606cmANPBvKhhQTR_YoyMqmssT8i2kW7dfattbIwf_NZ8Xn9Np2GQXnQ8yC0pWi6bgBTlDanVDWRYiqaY28iWtXqJozNTpAs2v8GORI0tB8mLsPe9bUDoNR0urixjZHm3MEytlyycwLVfDa_HWh7F4uR5HtL_mRLDArXo2a8OD6yn4MCupXcUxaFMx1Se7IFy0gXYaOBAUqW_gEr-CT_GKQ6EW5e-JRb7KcUE-PkK4yN1E3Pm1a_jgVTF2j-Zin2Er4BUkw_xYRATHEGxpZst4F1MpjAWWHvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان : آتش‌بس رسما تمام شده است/ احتمال انجام حملات بیشتر و فراتر از آنچه اعلام شده است وجود دارد
همچنین به نقل از یک مقام آمریکایی مدعی شد: وضعیت مربوط به ایران همچنان بسیار متغیر است و ممکن است حملات بیشتری فراتر از آنچه اعلام شده است، انجام شود. ارتش آمریکا در حال حاضر در وضعیت «انتظار و مشاهده» قرار دارد و اهداف حملات امروز، موشک‌هایی بوده‌اند که می‌توانند علیه دارایی‌های آمریکا مانند ناوهای هواپیمابر مورد استفاده قرار گیرند.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17044" target="_blank">📅 10:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17043">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">یک مقام ارشد آمریکایی: نیروی نظامی ایالات متحده امشب به دو پل راه آهن استراتژیک در شمال ایران با استفاده از موشک‌های کروز حمله کرد،
این اولین حمله آمریکا به زیرساخت‌های ایران از زمان آتش‌بس بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17043" target="_blank">📅 10:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17042">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">باراک راوید ، آکسیوس : کاخ سفید در حال آماده شدن برای چیزی است که می‌تواند به دور جدیدی از نبرد با ایران در اطراف تنگه هرمز تبدیل شود که چندین روز و شاید حتی چندین هفته طول بکشد. مقامات ارشد آمریکایی به من گفتند که مدت زمان این کمپین جدید و شدت آن کاملاً به گام‌های بعدی تهران بستگی دارد.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17042" target="_blank">📅 09:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17041">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b09f2f3a4f.mp4?token=h8jUdYHmSK18UZF-p0-ERV3mr_HHrkFqZFsUWWC4HvQWiR7oO2fmdTS_l59Yw8sIWpyy618XsGnRbaoHme995sI-e19jJmqFAMZaaus3uuhY07qcWOEfkrrZHOhTfAlmMq2h_gWAHif0OZ4HP9JBiNqIc-v8_hLsYIU3qHuNp39T07nXnHLYVg1QcQ9bZWPyzn9zuSI81CddKrCCkMWkLVDmPf-YW_DC6YzVnEyKfvWUw99s7H7YnMAMNaTBUhIfEPPnGfLfjDV3uglwd4rJ4bJOVC2FutpMz5z0C-leXcOKkdSlOjBj-shg-KHZ0EumXAfL_2RMv1_RxZWyynVHGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b09f2f3a4f.mp4?token=h8jUdYHmSK18UZF-p0-ERV3mr_HHrkFqZFsUWWC4HvQWiR7oO2fmdTS_l59Yw8sIWpyy618XsGnRbaoHme995sI-e19jJmqFAMZaaus3uuhY07qcWOEfkrrZHOhTfAlmMq2h_gWAHif0OZ4HP9JBiNqIc-v8_hLsYIU3qHuNp39T07nXnHLYVg1QcQ9bZWPyzn9zuSI81CddKrCCkMWkLVDmPf-YW_DC6YzVnEyKfvWUw99s7H7YnMAMNaTBUhIfEPPnGfLfjDV3uglwd4rJ4bJOVC2FutpMz5z0C-leXcOKkdSlOjBj-shg-KHZ0EumXAfL_2RMv1_RxZWyynVHGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون هواپیمای حامل تابوت
خامنه‌ای و خانواده، فرودگاه نجف را به مقصد مشهد ترک کرد.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17041" target="_blank">📅 09:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17040">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ادامه حملات پهپادی ارتش به پایگاه ها و مراکز راهبردی آمریکا در منطقه
روابط عمومی ارتش:
در پی تجاوز ارتش آمریکا به مناطقی از کشور و یگان های ارتش و در پاسخ به آن ،  ساعتی قبل و در ادامه حملات ارتش جمهوری اسلامی ایران به پایگاه های آمریکا در منطقه، سامانه پاتریوت در کویت، آنتن ماهواره ای(سایت اخطار اولیه) در قطر و مخازن سوخت ارتش تروریستی آمریکا در بحرین، هدف حجم انبوه انواع پهپادهای انهدامی ارتش قرار گرفت.
نیروهای مسلح جمهوری اسلامی، تحت تدابیر فرماندهی معظم کل قوا(مدظله العالی) با اقتدار و تحت هیچ شرایط اجازه تحقق اهداف و آرزوهای رییس جمهور نابخرد ایالات متحده را نخواهند داد و تا پیروزی نهایی از آرمان های والای انقلاب اسلامی دفاع خواهند کرد.
‎
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17040" target="_blank">📅 09:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17039">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">در پی حمله ارتش آمریکا به مناطقی از جنوب کشور از جمله چابهار، مقامان منطقه آزاد تجاری چابهار تصمیم به انتقال خودروهای وارداتی از انبارها گرقتند.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17039" target="_blank">📅 09:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17038">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سنتکام مدعی پایان حملات به ایران شد فرماندهی مرکزی ارتش آمریکا بامداد امروز با انتشار ویدئویی از هدف قرار دادن مواضعی در خاک ایران، مدعی پایان دور جدید حملات به ایران شد. در این بیانیه در توجیه این تعرض این‌گونه ادعا شده است «نیروهای فرماندهی مرکزی ایالات…</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17038" target="_blank">📅 09:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17037">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a63174b6.mp4?token=dp4n0Fmux3iySsqk5gksLKH4Rk-tVMVVaD6v17a_0M90HAeO-CW54EWrRJc6G1z48duYWsBPwwmOmqzF2LdOknobKzYu0kHixEtnyUz4niAPE_HjZaepN-qMYBkPSrQ7HU3nxiYVodL9Tydkn3ORHzhjp3A2VspAc-fV_lQZdGMjjalxt-X0UoBWVdO2YQ4ehfkL92LlktEnpJje2hRGHLQ7aTW6e4BzGUMHem2IuAlPHHNiFiKT8YglHPaCEo2Jadg-hm-vJpqouAcx-uyajwfVdZIoguSx8IvQ57suW4P2cPPRY629yZe3Ys1Wzl6a9Joa7BFG8KwQyc1kSpoLEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a63174b6.mp4?token=dp4n0Fmux3iySsqk5gksLKH4Rk-tVMVVaD6v17a_0M90HAeO-CW54EWrRJc6G1z48duYWsBPwwmOmqzF2LdOknobKzYu0kHixEtnyUz4niAPE_HjZaepN-qMYBkPSrQ7HU3nxiYVodL9Tydkn3ORHzhjp3A2VspAc-fV_lQZdGMjjalxt-X0UoBWVdO2YQ4ehfkL92LlktEnpJje2hRGHLQ7aTW6e4BzGUMHem2IuAlPHHNiFiKT8YglHPaCEo2Jadg-hm-vJpqouAcx-uyajwfVdZIoguSx8IvQ57suW4P2cPPRY629yZe3Ys1Wzl6a9Joa7BFG8KwQyc1kSpoLEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام مدعی پایان حملات به ایران شد
فرماندهی مرکزی ارتش آمریکا بامداد امروز با انتشار ویدئویی از هدف قرار دادن مواضعی در خاک ایران، مدعی پایان دور جدید حملات به ایران شد.
در این بیانیه در توجیه این تعرض این‌گونه ادعا شده است «نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در تاریخ ۸ ژوئیه دور جدیدی از حملات را علیه ایران تکمیل کردند تا توانایی ایران برای حمله به کشتیرانی تجاری و دریانوردان غیرنظامی بی‌گناه در تنگه هرمز را هرچه بیشتر تضعیف کنند.»
سنتکام در خصوص اهدافی که مورد تعرض قرار داده، ادامه داد «نیروهای آمریکایی به حدود ۹۰ هدف نظامی ایران، از جمله سامانه‌های پدافند هوایی، دارایی‌های دیده‌بانی ساحلی، سایت‌های ذخیره‌سازی موشک و پهپاد، توانمندی‌های دریایی و زیرساخت‌های لجستیک نظامی در امتداد خط ساحلی ایران حمله کردند.»
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/17037" target="_blank">📅 09:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17036">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تردد قطارهای مسیر تهران-مشهد متوقف شد
راه آهن جمهوری اسلامی ایران اعلام کرد: به دنبال حمله  بامداد امروز به یکی از ‌نقاط مسیر ریلی تهران-مشهد، حرکت قطارهای مسافری در این مسیر با وقفه مواجه شده است.
تیم‌های فنی و عملیاتی راه‌آهن بلافاصله به محل اعزام شده و عملیات بازسازی محل آسیب‌دیده در دست اقدام است و تلاش می شود در کمترین زمان ممکن این مسیر ترمیم شود.
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17036" target="_blank">📅 09:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17035">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گزارش انفجار در بحرین
@withyashar</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17035" target="_blank">📅 04:14 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
