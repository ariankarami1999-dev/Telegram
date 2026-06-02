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
<img src="https://cdn4.telesco.pe/file/gu3ReaQ210xuXWBZ65JMG5L_UroZ2TFDjTLLnKhhmpiPvIhQz-KbFtg36yWhT6mkFSxKdrLsQysiXaINAukkcVmuhMdkuTIGWMg4DXwYAuhrT8lgaE2EW1i4aPcvCz069Cz9w8Er5h95hzvrpKHazTEM_Nq9dr3LsPT2sGDdlu2yEh7iHzZnw-fzY7Mc6PGJ7kVAAqsFcZjQB0fr3h9j74Fg0zycHqcC_Rbc8dRjOTjmP2l7ZZolDMiS5D8EO1Sjo6ut57EDT1MTN2_inl0vCiBGwEGLul-VwqoHtNuaFSoVUWnRUhGnTIHxEQAFw09rmGywmnLweQXLUI3MpC37jQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 948K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 21:30:46</div>
<hr>

<div class="tg-post" id="msg-124540">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKABQhKse8zJpCoure1yU8uOapwVo8wXvY_5tU1xZbvMoi1xTuqC6C4XIoZGCgkkygsyj10g90WIIoZ5GIayBWtUXkxgLLccCAhFrMizBGOTnG50ceAWJnWtJWkt8rToCUdu8_JQrxj6_9YwBITkY29ez41uc08qK9AYsi5YJl0pClYJuHmXVpihU-xr8F4ySS_y_ZbcKBrVat-watnqOXM5frf7a-dsvpYRg1vpfxsXcmmU5RyzyRNFj1OcUpXXejyTdskVXIPQh8yx8ZiLxxt2_zxACcg1GWDdz68IB6jc_XY6hfMgh_aVtQl0aeJBJZwyMA6Y2xyfKCKSP3n6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار وال استریت ژورنال: چیزی که ایرانی‌ها گفتند این بود که دیگر پیشنهاد رد و بدل نمی‌کنند. کاملاً مشخص بود که میانجیگری ادامه دارد. بنابراین اینجا تناقض مستقیمی وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/alonews/124540" target="_blank">📅 21:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124539">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
شبکه کان به نقل از یک مقام اسرائیلی:
تل‌آویو به دلیل فشار آمریکا انتظار حمله به بیروت را ندارد، با این حال تأکید کرد که ارتش اسرائیل از "منطقه امنیتی" که اسرائیل در داخل مرزهای لبنان در آن نفوذ کرده، خارج نمی‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/alonews/124539" target="_blank">📅 21:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124538">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
المیادین به نقل از منابع آگاه: هیئت لبنانی جلسه را با تأکید بر لزوم دستیابی به آتش‌بس جامع آغاز کرد.
🔴
مذاکرات شامل پرونده‌های مختلف و مفاهیم مرجع مرتبط با سازوکار آتش‌بس و تثبیت آن می‌شود.
🔴
تخمین ما این است که مذاکرات امروز به نتیجه قطعی منجر نخواهد شد و احتمالاً مذاکرات فردا ادامه می‌یابد.
🔴
در طول جلسه، ایده‌ها و راهکارهای عملی از سوی طرف لبنانی و «اسرائیلی» و همچنین پیشنهادهایی از میانجی آمریکایی درباره آتش‌بس مطرح شد.
🔴
یک جدیت آشکار و یک تلاش واقعی آمریکایی برای دستیابی به تثبیت کامل و پایدار آتش‌بس وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/alonews/124538" target="_blank">📅 21:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124537">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
بی‌بی‌سی‌ : ترامپ به پایان جنگ ایران نیاز دارد، اما تهران عقب‌نشینی نمی‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/124537" target="_blank">📅 21:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124536">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی:
ترامپ احساس می‌کند نتانیاهو کنترل خود را از دست داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/124536" target="_blank">📅 21:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124535">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
رئیس جمهور اوکراین ولادیمیر زلنسکی:
ما از طریق اطلاعات می‌دانیم که یک حمله عظیم روسی ممکن است در زودترین وقت امشب رخ دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/124535" target="_blank">📅 20:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124534">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
فرماندهی مرکزی آمریکا: ناو هواپیمابر آبراهام لینکلن به حمایت از محاصره دریایی اعمال‌شده علیه ایران ادامه می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/124534" target="_blank">📅 20:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124533">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f23fb8dd41.mp4?token=mII68-f-D9rJ7eY0OFf4EDBTWlCQgEN5QFbBTG7fXOpG33p3DWnUd-EOgx7G5KFulf3tTjQBF2PnM6Jdkp_e0rIIbEyowoCbXbPoiSG6cHF5W5Ce9kHwWSUWo8GZ5UoHeksVB0lCKqXR0_3vR201xt-VvszHvosVmkP0yaoms78IKQwILZ2jZCALkv9lfnJOXc6aAePyjiKX5YRvZtvxcafNMAizyouNDYskeqokBH5hH7efQP2StHBJ24L4X4wqsyvF8Ift5vJljAT_EhoofdWTM-5pNe6LoZ_HC0vw4dMdMN3uPvmq2DBKFf8vj22nRCocoWZvnPV3dVCQsoY13A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f23fb8dd41.mp4?token=mII68-f-D9rJ7eY0OFf4EDBTWlCQgEN5QFbBTG7fXOpG33p3DWnUd-EOgx7G5KFulf3tTjQBF2PnM6Jdkp_e0rIIbEyowoCbXbPoiSG6cHF5W5Ce9kHwWSUWo8GZ5UoHeksVB0lCKqXR0_3vR201xt-VvszHvosVmkP0yaoms78IKQwILZ2jZCALkv9lfnJOXc6aAePyjiKX5YRvZtvxcafNMAizyouNDYskeqokBH5hH7efQP2StHBJ24L4X4wqsyvF8Ift5vJljAT_EhoofdWTM-5pNe6LoZ_HC0vw4dMdMN3uPvmq2DBKFf8vj22nRCocoWZvnPV3dVCQsoY13A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ماریا کورینا ماچادو رهبر اوپوزیسیون ونزوئلا می گوید به زودی به ونزوئلا بازخواهد گشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/124533" target="_blank">📅 20:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124532">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada3d308cc.mp4?token=tjlMfBWA_lTRW8vsp96Vk5C849QNnhZlmF-YuL3GpoC1_538ARlaRaDDpeDBvqLeyMJFIZOR2rb_6wfOVCOu5FXz-TvdcIeBJASa5ZAuHyGK36OJdOhkdxEvf7Ub5RC4u_dwR_ib8Ugxz2LB-1wXjkiRNWpDTcG9owkk86ofOh9k2Owm3Rxk0yjEs5nP65prfTgI26-tR3VHMRK1qRO194ATPhcxvEfqU-S2pXq17C06ttCDqBIgHoxFkYhLfawWtZqiW951xWf3SgBThwBqVoJfL0McugMRIqwIWz6-gGif2RvYjDy3RwXbCcFLJTv2W-yNUizaUEbsNppGTXMNnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada3d308cc.mp4?token=tjlMfBWA_lTRW8vsp96Vk5C849QNnhZlmF-YuL3GpoC1_538ARlaRaDDpeDBvqLeyMJFIZOR2rb_6wfOVCOu5FXz-TvdcIeBJASa5ZAuHyGK36OJdOhkdxEvf7Ub5RC4u_dwR_ib8Ugxz2LB-1wXjkiRNWpDTcG9owkk86ofOh9k2Owm3Rxk0yjEs5nP65prfTgI26-tR3VHMRK1qRO194ATPhcxvEfqU-S2pXq17C06ttCDqBIgHoxFkYhLfawWtZqiW951xWf3SgBThwBqVoJfL0McugMRIqwIWz6-gGif2RvYjDy3RwXbCcFLJTv2W-yNUizaUEbsNppGTXMNnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: حزب‌الله نه تنها دشمن اسرائیل و دشمن آمریکا است؛ حزب‌الله دشمن لبنان و مردم لبنان است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/124532" target="_blank">📅 20:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124531">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
فرستاده اسرائیل در سازمان ملل، درباره پهپادهای حزب‌الله: این پهپادها کمتر از ۲ کیلوگرم وزن دارند. می‌توانید آنها را به صورت آنلاین تهیه کنید. بسیار آسان است. می‌توانند آن را از میان یک پنجره به داخل یک خودرو هدایت کنند.
🔴
پرواز آن پایین است. شناسایی آن بسیار دشوار است. و تا وقتی صدای آن را بالای سرتان بشنوید، دیگر دیر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/124531" target="_blank">📅 20:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124530">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ادعای شبکه ۱۲ اسرائیل : دستور تخلیه ضاحیه جنوبی بخشی از هماهنگی نتانیاهو و ترامپ برای فشار به ایران تو مذاکرات بوده و نه برای حمله مستقیم به ضاحیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/124530" target="_blank">📅 20:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124529">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ترامپ: گزارش‌های جعلی مبنی بر اینکه جمهوری اسلامی ایران و ایالات متحده آمریکا چند روز پیش از صحبت کردن دست کشیده‌اند، نادرست و اشتباه است.
🔴
گفتگوهای ما به طور مداوم ادامه داشته است، از جمله چهار روز پیش، سه روز پیش، دو روز پیش، یک روز پیش و امروز.
🔴
اینکه این گفتگوها به کجا منتهی می‌شود، هیچ‌کس نمی‌داند، اما همانطور که به ایران گفتم، «زمان آن رسیده است که به هر نحوی یک توافق انجام دهید. شما ۴۷ سال است که این کار را انجام می‌دهید و دیگر نمی‌توان اجازه داد که ادامه یابد!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/124529" target="_blank">📅 20:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124528">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
نخست‌وزیر مجارستان، پتر ماگار:
مجارستان سرباز یا سلاحی به اوکراین ارسال نخواهد کرد.
🔴
نه حتی تحت دولت جدید مجارستان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/124528" target="_blank">📅 20:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124527">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad80e601a.mp4?token=eiV9xJjtNU5sre47R4yhiK3xap3VtwWEvPeBCZF8DuK2uYlsQjSxieyJHkMS1mnokEzI1fxwZzCOfJsF_VTdwPYU-CLPp6x9YfEF0xVR0k9mphCqfN4XS1OysTzD6TSslg7bX6nbJFe9Kan_gaza0HeolSKynQiBWOWMOJHcPUxhujw2gKg-1AAXZec3hxqWhmR7ly9_K6MNcrq88OtGYMoGWpBfLcuxNNE9fpgPKOjK_wCxssYhUwlQWoQYw1IaJH_BCqZgnUtkP773tbP9_ZUG4T44OjixTAPMVsM1q8BBOZn0KYATn99Z33t2mIyrjf1JXat5zITq8iEnQNHAOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad80e601a.mp4?token=eiV9xJjtNU5sre47R4yhiK3xap3VtwWEvPeBCZF8DuK2uYlsQjSxieyJHkMS1mnokEzI1fxwZzCOfJsF_VTdwPYU-CLPp6x9YfEF0xVR0k9mphCqfN4XS1OysTzD6TSslg7bX6nbJFe9Kan_gaza0HeolSKynQiBWOWMOJHcPUxhujw2gKg-1AAXZec3hxqWhmR7ly9_K6MNcrq88OtGYMoGWpBfLcuxNNE9fpgPKOjK_wCxssYhUwlQWoQYw1IaJH_BCqZgnUtkP773tbP9_ZUG4T44OjixTAPMVsM1q8BBOZn0KYATn99Z33t2mIyrjf1JXat5zITq8iEnQNHAOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از لحظه برخورد موشک به کیف در شب گذشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/124527" target="_blank">📅 20:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124526">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
روبیو: اگر ایران سلاح‌های هسته‌ای به دست آورد، مانند کره شمالی اما بدتر خواهد بود.
🔴
آن‌ها کشور اسرائیل را نابود خواهند کرد و شما قادر به انجام کاری در این مورد نخواهید بود زیرا آن‌ها یک سلاح هسته‌ای دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/124526" target="_blank">📅 20:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124525">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
روبیو: در مورد هند و پاکستان، ما آن جنگ را به پایان رساندیم؛ ما در کمک به میانجی‌گری آن نقش داشتیم.
🔴
مارکو روبیو می‌گوید سودان به یک درگیری نیابتی تبدیل شده است زیرا «امارات و سعودی‌ها در دو طرف مخالف آن قرار دارند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/124525" target="_blank">📅 20:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124524">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5843d7de41.mp4?token=qaVVTli7kKbYxzdMGGIEE9NFHE7G2rx-uAvZwtBq2xQ3wrvHB2WsXJwlj_a6vP1EzBNBkkACmrb5abWjgb35DM2F4HN0vC4o0ZkNpuv_mFHtr0lyhefeWzJyhJHusL9DYFhSgD7Hrx_hssf_kvRtM6Xq26E-Y6AMhk01eNtyYLHLWZexbgyCFsW8rbjtomaBdqkK84Jkc5jsmbpmjAmyosLRQJcYT9dYZB7iTCNfxSuZPM63p2AD6fiCKLlOINJ0O10QRzs0vJ7heWenzAZiJujT2vL8JvAy7RQZeZUDuuKCR5nhruAYgv5QIk8RPuOdy7ekhCeGXEVluCfE8w5-sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5843d7de41.mp4?token=qaVVTli7kKbYxzdMGGIEE9NFHE7G2rx-uAvZwtBq2xQ3wrvHB2WsXJwlj_a6vP1EzBNBkkACmrb5abWjgb35DM2F4HN0vC4o0ZkNpuv_mFHtr0lyhefeWzJyhJHusL9DYFhSgD7Hrx_hssf_kvRtM6Xq26E-Y6AMhk01eNtyYLHLWZexbgyCFsW8rbjtomaBdqkK84Jkc5jsmbpmjAmyosLRQJcYT9dYZB7iTCNfxSuZPM63p2AD6fiCKLlOINJ0O10QRzs0vJ7heWenzAZiJujT2vL8JvAy7RQZeZUDuuKCR5nhruAYgv5QIk8RPuOdy7ekhCeGXEVluCfE8w5-sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو
:
برخی از متحدان ما در منطقه بسیار به صورت تهاجمی همکاری کرده‌اند، مانند امارات متحده عربی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/124524" target="_blank">📅 20:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124523">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
روبیو: اگر مردم ایران اختیار داشتند، فردا توافق می‌کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/124523" target="_blank">📅 19:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124522">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
کرملین: در صورت عقب‌نشینی اوکراین، جنگ امشب پایان می‌یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/124522" target="_blank">📅 19:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124521">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
حزب‌الله: در صورت بمباران ضاحیه، تل‌آویو را هدف قرار خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/124521" target="_blank">📅 19:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124520">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
روبیو: جنگ در ایران به پایان رسیده است.  ایران به صدها میلیارد دلار برای بازسازی نگاه می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/124520" target="_blank">📅 19:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124519">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
مارکو روبیو: ما از تهران برای هیچ چیز التماس نمی‌کنیم.
🔴
اونا ممکن است التماس کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/124519" target="_blank">📅 19:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124518">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9z02i9B9Lu9SZU6jHz6fnp6hcQDjbU4ZNdokrt5QDTDTeEkX2cXS-Jc0lBrctSR7ApHdLhYc6TbhUTPBtr9IQny0cQLOrbIGr5XZXzKZOF0qbYjqPsd7nmHKpoNZZjvvxonpPZM9I0JRrA6KBmVZzmUWiV3C7QQJ04R2Ax6VR9LkEV9YF2j0oweOxpMNRhlCN8FWfGWih3evdJJtUBr40tgHS04PJ02R2gMiHa8kZyn7dGAyWJDqU4ZFjzFvvzaoyJlGPfeBKOK_YV0FTedfd8I2erYVgeolulDcWBvEhTf-duBraq8D2i1cVi6IB1sE-Cu1F5il6_AEHJqzAu5yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سقوط بیت کوین به زیر ۶۷۰۰۰ دلار
🔴
۷۰۰ میلیون دلار از بازار ارزهای دیجیتال در ۲ ساعت گذشته نقد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/124518" target="_blank">📅 19:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124517">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
روبیو درباره ارمنستان: روس‌ها از درگیری ما در ارمنستان کمتر از خوشحالی هستند.
🔴
به نظر من شواهدی وجود دارد که نشان می‌دهد آن‌ها دوست دارند رئیس‌جمهور فعلی به دلیل این رابطه رو به رشد با ایالات متحده، انتخابات خود را ببازد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/124517" target="_blank">📅 19:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124516">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
روبیو : در نهایت ما هنوز با چالش‌های دیگه‌ای درباره ایران روبه‌رو هستیم
🔴
جدا از برنامه هسته‌ای؛ مثل این‌که پولشون رو صرف حمایت از حزب‌الله، حماس و گروه های دیگر در نقاط مختلف دنیا می‌کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/124516" target="_blank">📅 19:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124515">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
روبیو : چین این موضوع (فروش سلاح به تایوان) رو همیشه به‌عنوان یک فشار در مذاکرات مطرح می‌کنه؛
🔴
ولی این موضوع تصمیم‌گیری ما رو متوقف نکرده، در نهایت، زمان و نحوه انجامش با رئیس‌جمهوره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124515" target="_blank">📅 19:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124514">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">یه افسانه ژاپنی هست که میگه:
"اگر به اتوبوس نرسیدی، شاید از یک تصادف جا موندی
اگر پذیرفته نشدی، شاید از جایی اشتباه نجات پیدا کردی
اگر کسی ترکت کرد، شاید داره جا رو برای کسی که قراره وارد زندگیت بشه باز میکنه."
گاهی جهان پشت چیزی که اول شبیه بدشانسیه داره ازت محافظت میکنه
به مسیرهای غیر منتظره اعتماد کن.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/124514" target="_blank">📅 19:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124513">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 8T!
🚀
😍
فقط گیگی 8 تومن
😍
✅
باخرید 90 گیگ 100 گیگ تحویل بگیرید
😍
✅
❌
فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!  @Netaazaadbot @NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/124513" target="_blank">📅 19:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124512">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ECzMvjOedYT15wfaW0jjS0LihQ2bsR7LG-uS4FWNTkAgNlHLUrSDJh_lVsAwdbLRgc7klo2WjvBFzkPZ34ex6TAtiZv2c9jOme-PGamXeGyEs2zCzVeKsMR-vknrJfvqCPt9NTCA88bqW1SM381xQ_V1fcj-ec-phStJY3vxxUAxAC1sPEjTgcIv-c6-9Ja6mp9KyFPEUT-k-9dKSIBXYq9uCyRTHa_NvDWRitGBuoqnsaQVjQelPj_oSYL8WrDazHmwTax1_mWxhLApxiqrowHPivGynLrsptBhXmyfQBLwioyoS4U4Iejud9jpGn2ZpBdYj_riZvr6KodJq4mHHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 8T!
🚀
😍
فقط گیگی 8 تومن
😍
✅
باخرید
90 گیگ
100 گیگ تحویل بگیرید
😍
✅
❌
فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!
@Netaazaadbot
@NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا حتی در ساعات شلوغ
@Netaazaadbot
@NetAazaadBot
📩
برای خرید و دریافت سرویس استارت رو بزن
✅</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/alonews/124512" target="_blank">📅 19:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124511">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gl-yenguRFhKYH5Z2AGMtAHcydqfmOKuF_-Ifd9yXuWT2KXB-CqObOg_FY-nXlVu2PR2imaz7B9kOqY279TcxueNEbbIj_N2ViVIiMWzzz-1B0cL7DGNvJplZHWGmNIF3zUMyVwEJ9DmHfcv8xcjtjduorn4s7sSr_bkK0X_x0uvGVHhM4Tf4f-p2yi92RQVoS1c9oOpkpPjOOJQWWsYXj6KJT86IAUhAaHZl6fiQx1zoXPw5o4jlRKSTuVzT-bduLsKhLGJNQYWTkV2oY5XvimHtKh-JtG2gz9N9O_iF6qGKZTiA8rGEkFtC8UdHFnwAzwZF5dIPlDzZubow1_YLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت متروی کی‌یف پایتخت اوکراین در بحبوحه حملات سنگین روسیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/124511" target="_blank">📅 19:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124510">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
بر اساس گزارش بلومبرگ، امارات متحده عربی در حال بررسی طرحی برای ساخت یک خط لوله اضافی انتقال محصولات پالایش‌شده است. این خط لوله با هدف دور زدن تنگه هرمز و انتقال مستقیم سوخت به سواحل شرقی این کشور در نظر گرفته شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/124510" target="_blank">📅 19:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124509">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
جبهه داخلی اسرائیل: محدودیت‌ها در شهرک‌های مرزی با لبنان کاهش می‌یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124509" target="_blank">📅 18:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124508">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7c945a1dc.mp4?token=oGCL56XL9loiBbcTu9OUxTSUFIHW1PEs8ZvEC2JeGJlcsf5LRhwymXPNebgmeX3jZUgPON62XXJzooSQctv55rvSpEYiLC1R-GAmvTegMLqBJPoRjGlTJlOp1ybYi6xMV_I2cMSRzE1E2VZMeQDzuUMaIDPt2SNdqllty-v8GGOPnRoWJ0lz6YI3XTloJlDBUiocUiF8ZvpeE-1ZuOnVAFliP315OMiZJHnL06hnEYXNGxoTrwusIwPfPZd5NXlGyyl2-La1aTObJnpn7LPf3dkS1EVy0SF3Tfqq1W8RuNJT7b5IVRXzsLc60ckZeVgIknv7DN1pb4I3Qcq4d-IDeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7c945a1dc.mp4?token=oGCL56XL9loiBbcTu9OUxTSUFIHW1PEs8ZvEC2JeGJlcsf5LRhwymXPNebgmeX3jZUgPON62XXJzooSQctv55rvSpEYiLC1R-GAmvTegMLqBJPoRjGlTJlOp1ybYi6xMV_I2cMSRzE1E2VZMeQDzuUMaIDPt2SNdqllty-v8GGOPnRoWJ0lz6YI3XTloJlDBUiocUiF8ZvpeE-1ZuOnVAFliP315OMiZJHnL06hnEYXNGxoTrwusIwPfPZd5NXlGyyl2-La1aTObJnpn7LPf3dkS1EVy0SF3Tfqq1W8RuNJT7b5IVRXzsLc60ckZeVgIknv7DN1pb4I3Qcq4d-IDeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو: ناتو یک جلسه سرگرم‌کننده خواهد بود...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/124508" target="_blank">📅 18:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124507">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
روبیو: هیچ تغییری در سیاست ایالات متحده نسبت به تایوان ایجاد نشده است.
🔴
به نظر من، به وضوح، طرف چینی دوست دارد تغییری را ببیند، اما در این زمینه هیچ تغییری ایجاد نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/124507" target="_blank">📅 18:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124506">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63fdfdb0cf.mp4?token=ct1uO4LR-0hP0HmSAyfRg7W80r9tWindm3rYFTpKIChrW2GA1mmDJlIEj-_SLeq5xgsFc-t4zZBJrLzOh13NiatB4ONWevNOAO3jLsNfBDKK3H_nlSng2nTmh0BIE2nD7l9AQ5CXLXpZXk8rVLkY4wBigs4YVShEQAdc4J8tRpFvvIc8NOihakEs_Tt72n03ZioAUFIGG1aWfqGIU0e2Y3OCullj1RY8lcCEo5WtCD2I4UbBvzuAaaZMlX_PhdbCNYVqdyMuysGtG-obSZCEKdVsMlEdoAsFfeOaFGd5AeTWLPCvkOupnkVR8tv-HggzErLfqv3aHGvMshTOhKzYpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63fdfdb0cf.mp4?token=ct1uO4LR-0hP0HmSAyfRg7W80r9tWindm3rYFTpKIChrW2GA1mmDJlIEj-_SLeq5xgsFc-t4zZBJrLzOh13NiatB4ONWevNOAO3jLsNfBDKK3H_nlSng2nTmh0BIE2nD7l9AQ5CXLXpZXk8rVLkY4wBigs4YVShEQAdc4J8tRpFvvIc8NOihakEs_Tt72n03ZioAUFIGG1aWfqGIU0e2Y3OCullj1RY8lcCEo5WtCD2I4UbBvzuAaaZMlX_PhdbCNYVqdyMuysGtG-obSZCEKdVsMlEdoAsFfeOaFGd5AeTWLPCvkOupnkVR8tv-HggzErLfqv3aHGvMshTOhKzYpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه مارکو روبیو می‌گوید نشانه‌هایی وجود دارد که نشان می‌دهد رهبر جمهوری اسلامی ایران، مجتبی خامنه‌ای، زنده است و «در سطحی» در تصمیم‌گیری‌ها مشارکت دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/124506" target="_blank">📅 18:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124504">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
مارکو روبیو در مورد ایران: اگر مذاکرات به نتیجه نرسد، به وضوح همچنان مشکلی در مورد جاه‌طلبی‌های هسته‌ای آن‌ها وجود خواهد داشت.
🔴
اما چیزی که دیگر به عنوان سپر متعارفی برای پنهان شدن پشت آن است، ندارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124504" target="_blank">📅 18:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124503">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
روبیو، وزیر امور خارجه آمریکا در مورد ایران: اگر ایران می‌خواهد بتواند دوباره نفت خود را از طریق تنگه عبور دهد، باید تنگه‌ها را باز کند.
🔴
اگر از انجام این کار خودداری کنند، گزینه‌های دیگری نیز در اختیار ما قرار دارد، اما ترجیح می‌دهیم برای باز شدن این تنگه مذاکره کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124503" target="_blank">📅 18:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124502">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
روبیو : شاید چند روز آینده خبری از توافق بشه
🔴
مشکل اینه که جواب‌هاشون دیر می‌رسه و همین باعث شده بیرون هم گزارش‌هایی بیاد که شاید چند روز دیگه یه توافقی بشه.
🔴
چون داخل سیستم خودشون هم طول می‌کشه پاسخ بدن، بعضی وقت‌ها حتی ۵ یا ۶ روز طول می‌کشه تا جواب‌ها و تصمیم‌هاشون رد و بدل بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124502" target="_blank">📅 18:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124501">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری/روبیو: اگر ایران با توقف هدف قرار دادن کشتی‌ها موافقت کند، به محاصره پایان خواهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/124501" target="_blank">📅 18:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124500">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00588eedce.mp4?token=vqhQfprLqmJu4MY9PTKIsmhClZOMpZ4Dn7WwN-SS96cjVJoggW8-TX_SB5ex3gkpj3MhLsdTVuLOo6g8ZSPjniKCiWJKmQgqzQz5v_i4oliPkbnAqiZ4DiShunRug1s_A27dkk-fY4JOes9Q8voVocq8EJk025MtCAEKqUv-opljlReAlyxlRIdtgOpqL1bIUTusMoJPCFGCcRov6pznaE87dvfLyH3-x8lc15pmlVAri6f85mktyM_aVyDTCxAMKohpY-5IGdAFw10bHF6SvHPiRmOnVzwTGCjG6dll6XXGA7z0Yfu9gi53Hcz8Q1hf8Y0EbsnU1iS9nwg1smioig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00588eedce.mp4?token=vqhQfprLqmJu4MY9PTKIsmhClZOMpZ4Dn7WwN-SS96cjVJoggW8-TX_SB5ex3gkpj3MhLsdTVuLOo6g8ZSPjniKCiWJKmQgqzQz5v_i4oliPkbnAqiZ4DiShunRug1s_A27dkk-fY4JOes9Q8voVocq8EJk025MtCAEKqUv-opljlReAlyxlRIdtgOpqL1bIUTusMoJPCFGCcRov6pznaE87dvfLyH3-x8lc15pmlVAri6f85mktyM_aVyDTCxAMKohpY-5IGdAFw10bHF6SvHPiRmOnVzwTGCjG6dll6XXGA7z0Yfu9gi53Hcz8Q1hf8Y0EbsnU1iS9nwg1smioig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه، می‌گوید که ایالات متحده پیشنهاد لغو تحریم‌ها به ایران در ازای بازگشایی تنگه هرمز نداده است و اضافه می‌کند که لغو تحریم‌ها تنها در مذاکرات هسته‌ای مطرح خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/124500" target="_blank">📅 18:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124499">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
روبیو، درباره رهبر ایران : رهبر قبلی دیگه تو صحنه نیست و عملاً کنار رفته، و پسرش جای او رو گرفته
🔴
اما نکته اینجاست که حدود یک ماهه هیچ خبری ازش نیست
🔴
طبق گزارش‌های منتشرشده، اون در همون حمله به‌شدت آسیب دیده
🔴
شما خودتون مطمئنید هنوز زنده‌ست؟ چون واقعیت اینه که ما هیچ حضور علنی یا صحبت عمومی ازش ندیدیم
🔴
بنابراین تا جایی که اطلاعات عمومی نشون میده، وضعیتش کاملاً مبهمه و عملاً خبری از حضورش نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/124499" target="_blank">📅 18:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124498">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
روبیو: شرط اول در مذاکرات با ایران، باز کردن تنگهٔ هرمز است
🔴
لازم است ایران به وضوح اعلام کند که تنگهٔ هرمز از این پس باز است.
🔴
روبیو: اگر ایران با توقف هدف قرار دادن کشتی‌ها موافقت کند، به محاصره پایان خواهیم داد
🔴
هیچ کشوری از ادامهٔ بسته بودن تنگهٔ هرمز حمایت نمی‌کند، از جمله چین و روسیه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/124498" target="_blank">📅 18:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124497">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
روبیو: عملیات خشم حماسی، برخی از شما آن را دوست نداشتند، برخی از شما آن را دوست داشتند، در دستیابی به اهداف نظامی خود بسیار موفق بود، که به طور چشمگیری پایه صنعتی دفاعی ایران را کاهش داد.
🔴
آن‌ها هنوز پهپادهای زیادی دارند، زیرا ساخت این‌ها آسان است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/124497" target="_blank">📅 18:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124496">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزیر امور خارجه مارکو روبیو در مورد پهپادها: این یک چالش جهانی است که هر روز در سراسر جهان رخ می‌دهد.
🔴
کارتل‌های مکزیکی از پهپادهای بدون سرنشین علیه یکدیگر استفاده می‌کنند و ما باید تصور کنیم که در مقطعی ممکن است از آن‌ها علیه منافع ما استفاده کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/124496" target="_blank">📅 18:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124495">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
روبیو: اصلاً چیزی به اسم نیروی دریایی ایران وجود نداره
🔴
رفته ته اقیانوس. چند سال دیگه هم تبدیل میشه به محل ماهیگیری خوب، چون مثل صخره مرجانی میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124495" target="_blank">📅 18:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124494">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
روبیو:
هیچ کشوری در جهان، به جز ایران و شاید عمان که کمی با آن هم‌سویی داشت از کاری که ایران در تنگه‌ انجام می‌دهد حمایت نمی‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124494" target="_blank">📅 18:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124493">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/458aecaa09.mp4?token=mBmMZr7SgKovivJfttv8BLH0Whe3TtBbBNHj8Q5SH4MC1KaPyLx9BL2JMS3DckoGSixWoWCTzXTprN1S8EjrYnvSTjZNd9l4FGREgtmBqZ2lbqtJ1VCjTLq5t8YEcRjmMDVy7zCnmeDuNxBiOUJyvAefmYkjZBd3SlEJKiq7GJEEr3IyxZXW7u-fOP38j1nI5vNFBrQEwwT6J9xmYtnqrNkwLy_ffB0FXWVDJx81iOsngGiMxfpWyfQBQPs3yf1Go8MbWlNoo7T-kQrzlhbyBH1jL71Bz41iiKv2LjT7x0dbh5_ETS1wSRrk7JRFzUpSdxz4WA22ozJlCu8l4mVu7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/458aecaa09.mp4?token=mBmMZr7SgKovivJfttv8BLH0Whe3TtBbBNHj8Q5SH4MC1KaPyLx9BL2JMS3DckoGSixWoWCTzXTprN1S8EjrYnvSTjZNd9l4FGREgtmBqZ2lbqtJ1VCjTLq5t8YEcRjmMDVy7zCnmeDuNxBiOUJyvAefmYkjZBd3SlEJKiq7GJEEr3IyxZXW7u-fOP38j1nI5vNFBrQEwwT6J9xmYtnqrNkwLy_ffB0FXWVDJx81iOsngGiMxfpWyfQBQPs3yf1Go8MbWlNoo7T-kQrzlhbyBH1jL71Bz41iiKv2LjT7x0dbh5_ETS1wSRrk7JRFzUpSdxz4WA22ozJlCu8l4mVu7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو: ایران به کشتی‌های تجاری شلیک کرده و بخش‌هایی از تنگه هرمز را مین‌گذاری کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124493" target="_blank">📅 18:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124492">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e969f05d.mp4?token=LDRdiavuzSwSGGkUnG9xQnKeQ4_m_sBxXOJLGzNqP2MddGFwVZzLOTsI6_goPFi4pFlCvdlWJmJR6dlRtdTdCfd1zNk2k2W2OvEs2PxgybFMAJtLMvYoGvGM44l1T8tzjX1scQ8aOSaZPUhrL5xJdjbKSHbGSVrxDm0CVHoyzShJkKkU_FW15YhtMIzDnI5BZAo6jKWyRsoU2X4LACYWHKCIk3rcdOdHbo1DIYdw1NRkZOhSDvfUdFzTI1pfySEKmC31pYMrnlmxPAm_dcgtMLfQDH-CRDyU_V8cUXaraCFXZysr9ugoX7nIxCHgxu3gE9W4ftFzTY_dpDcpfaN6HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e969f05d.mp4?token=LDRdiavuzSwSGGkUnG9xQnKeQ4_m_sBxXOJLGzNqP2MddGFwVZzLOTsI6_goPFi4pFlCvdlWJmJR6dlRtdTdCfd1zNk2k2W2OvEs2PxgybFMAJtLMvYoGvGM44l1T8tzjX1scQ8aOSaZPUhrL5xJdjbKSHbGSVrxDm0CVHoyzShJkKkU_FW15YhtMIzDnI5BZAo6jKWyRsoU2X4LACYWHKCIk3rcdOdHbo1DIYdw1NRkZOhSDvfUdFzTI1pfySEKmC31pYMrnlmxPAm_dcgtMLfQDH-CRDyU_V8cUXaraCFXZysr9ugoX7nIxCHgxu3gE9W4ftFzTY_dpDcpfaN6HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه در مورد ایران:
ما نمی‌توانیم جهانی داشته باشیم که در آن فقط کشتی‌های ایرانی از تنگه‌ها عبور کنند.
اگر آن‌ها قصد دارند تنگه‌ها را برای همه ببندند، ما نیز تنگه‌ها را برای آن‌ها می‌بندیم.
هزینه برای ایران هر روز و درآمد از دست رفته به دلیل این اقدام، در حد صدها میلیون دلار است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/alonews/124492" target="_blank">📅 18:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124491">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
نتانیاهو: علی خامنه‌ای بزرگترین تهدید تاریخ قوم یهود بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124491" target="_blank">📅 18:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124490">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn3azCrMKY07uxudj_5eIVitoJ4BZzH8F_rC2pWwNZCQVu75GdGpAvRrIYDt83izZd_K1y5mTlo8qXmal6nSIAxNsxQfgM3orNbW_TxNnXcQ7KmMz4kss_Jx2v9ba8MuOSdXxnqV5Ec_QHaRopPZT3xhx51ma9GOncrO7Uu5ASFTk0dUlkpLAgRTJnfMIP4fnONMxcmh6yUl90TCuFQG-DH9C6ixMx8jWNTKsuc2HmrLPweeVNJdRZLF-g4iVGTWX884XrqHodumBITe13YinlBYVGBZlYC5nydP1DyrOR7L1UuAkNi5Vo8S-LuM2vkojgGmjRtkLGOusWNBUN-Y3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیوید بارنیا، رئیس مستعفی موساد، می گوید تغییر رژیم در ایران "هم هدفی واقع بینانه و هم قابل دستیابی است."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/124490" target="_blank">📅 18:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124489">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
وزیر خارجه ترکیه: آنکارا در مذاکرات ایران و آمریکا میانجیگری می‌کند و هر دو طرف برای تداوم آتش‌بس و بازگشایی تنگه هرمز صادق هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/124489" target="_blank">📅 17:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124488">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zyz54YoIOauSpVmsRXqJeihsUdvnKiTs33BN-hpMZF8LVt7BTtvCge0AvcWHUCuIDko54iQK75dR-4owZklVaJjJydmZyINxFfGUKTj0XBJXkzIh1xjhnpgOCqUWWD8CJLUgoJW_q7j9oMQ-v3ztCGq_JYpt7HKCfl1hhPaYZ-4raJOWkNlLwqIRKYcwyKwrt_OrxQlulgngbnabCpewH12UKmK6ULSqyAhJPX_P3KVEDWJt7W4ZdMyu55vr_LYR1G3uuPcy_CNBHUsiqgRUb2sC7H9nhasF-nliZvnFCIc5Jm3gduHg1mJvtk16rm44L81ZbIzXoe35O-hSSxiZvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: کانادا ایالت ۵۱‌ اُم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/124488" target="_blank">📅 17:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124487">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
نتانیاهو : موساد همیشه تو خط مقدم مقابله با «تجاوزگری ایران» هست؛ - این هم ادامه همون سیاستیه که سال‌ها دارن اجرا می‌کنن
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/alonews/124487" target="_blank">📅 17:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124486">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf4413f80f.mp4?token=hPOuwrC8O7JspmpzDimIay7G312A6urbhlNtyj43KM6AqiXUHINaulNOuH3oojHeytDw8tEOzOP2Ga4Tz9vHPT_dV47_u1GaUeba9TA5IvHHjD9f13aho6OczR93RkRgcRIvMbQtMUSaMcFsKMh5gpwyZppqbBW7SpYEGPSlyCjA1kr0e0qZ_va0HAolJ1tLIKb901pu2RyGNlVHmsdvlGqecmBcLNho6JUK3TILV57kyIjgf-UJmU0rTOZ5LoM6-rwe5COdn9k-vyu74Rn0L6GXigZhKgGauDSThMYU-9E1vfqxRgGYlEAPeoJRuQVOkFoQIg5DFO_7CbAPt4nSKijaRkTUb69YH-VkXeKqcBYIZQjtkskoj1y0dM2fOx5_o-tbMctqaBHDNUPG4yhgQSQ_Ed6pgGhStsCBT7PbaDp2NKf2UNSxY3sQZd7cM4wENRf4SrZC199-DfGZazvgn8t0jE19oNrUqD49aPxEpWekKnKfSsHIe61rAv0BgnuzvuF66NvTyO_Fp8YPPLZ8TDR2kkHB2V6LJZSpLttvghtttF0kd2xl4JtXd6u8Lhw8839J3utopwnidH7yQSTDwU3v27Uml1-JqK88GVsuJqeZTcFL4OjMs8wEcBdHXCdJs1FbK1xpFf-_OEl5mmGkuY80tpSiR-fs8P_BoX_meaU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf4413f80f.mp4?token=hPOuwrC8O7JspmpzDimIay7G312A6urbhlNtyj43KM6AqiXUHINaulNOuH3oojHeytDw8tEOzOP2Ga4Tz9vHPT_dV47_u1GaUeba9TA5IvHHjD9f13aho6OczR93RkRgcRIvMbQtMUSaMcFsKMh5gpwyZppqbBW7SpYEGPSlyCjA1kr0e0qZ_va0HAolJ1tLIKb901pu2RyGNlVHmsdvlGqecmBcLNho6JUK3TILV57kyIjgf-UJmU0rTOZ5LoM6-rwe5COdn9k-vyu74Rn0L6GXigZhKgGauDSThMYU-9E1vfqxRgGYlEAPeoJRuQVOkFoQIg5DFO_7CbAPt4nSKijaRkTUb69YH-VkXeKqcBYIZQjtkskoj1y0dM2fOx5_o-tbMctqaBHDNUPG4yhgQSQ_Ed6pgGhStsCBT7PbaDp2NKf2UNSxY3sQZd7cM4wENRf4SrZC199-DfGZazvgn8t0jE19oNrUqD49aPxEpWekKnKfSsHIe61rAv0BgnuzvuF66NvTyO_Fp8YPPLZ8TDR2kkHB2V6LJZSpLttvghtttF0kd2xl4JtXd6u8Lhw8839J3utopwnidH7yQSTDwU3v27Uml1-JqK88GVsuJqeZTcFL4OjMs8wEcBdHXCdJs1FbK1xpFf-_OEl5mmGkuY80tpSiR-fs8P_BoX_meaU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : موساد همیشه تو خط مقدم مقابله با «تجاوزگری ایران» هست؛
- این هم ادامه همون سیاستیه که سال‌ها دارن اجرا می‌کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124486" target="_blank">📅 17:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124482">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QwHdraP1DSV2npqjIMaxdTDxXIm5OM3vBAuSzq6QqvlKq0EhjhLLJVdoWqJdUfjIDzSefl-mki9ENCtvOWA3N2-39BHI-fhnQ2ah9DtmlFKLv3-1TqCtrrCAz4izp4v3G6VC_a0e8WuL1goJyEl6hD6K9BMOKk3D1ADQt2KrROV0WNS_NAgrHSZw0I2iwlcA2F25n8QgJU8yvoRmMD1uZ8mecadS4gqjgs5dRV80aCRezVAZvTSFaR3YouosQ_iIADlxUo0f7eSEMS-TSlK56HH3MYcZ2zYNEv2BFEGkv2rH5jTSHyjQ6lBOokONae0K1QGw1kyJp0QFtKIDSQV7HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KeVJKxPaQJ4PodNkPtJZipoCBpS30UYygPEe26tk8u7rTpwrAMFfDVxZ2pBuc3iQ6rKThXpUyGYU8eQYKIizKb8YdfQLENSITn-sKLZKxCW8A-baB0a3aygw3FS8lgbJttkAGeK-DHlsx_ru8h9rWxlNqOpzLHmLnvjYL7j4JYfp7ZFFhxeYb2oevPygFwizj8gB4CpN1QtpatUye4aI8762LbRYajV3rliyKQ8mEhtn2JHjJ49ghmvYUpx-E7vrwFAyutYfKpF7n4_32OZmA_vNWE4cVyz6QX2I4OxfPkd5AZ7lSNeMpNNO5aXwHoZDYJSsPD27cmDurQxhUZlKkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Plo6lEizusPHpQqCD2TctuHSFTyx-mFQ9fAZG4aZT1Uk_H_dIL0pldmxMip6-sL3-vvUriL5oTA98MpBMPhY-V-sHmKT_f2y-gLgOA09sa4BQxwRIGVupnJgh9fBuA9bdTDbtGrFNNe_WZx6S71b2HaM-9_K_N_E5M5p17XmzePZbB1VJvhjWIuLJt02gqLzI6gluoAd7GwSMLP_SCmkOEnP_aIkQefLbB1lLbSFPWfRVWgg5njjFuUq8S5mBY3WK8B-BAWH1kdvG0xpcOpkYTZNxmewGEJzvqJV7vmX0AM6p2_Tr6b-RcYcrWy4zOb_6fTsCiMxVRiEPm5uUuY7cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/owRR_bE66tMMXmyP6UcimVGrJTK4ixiEb2YchkuiZ13TbA18j35eyHBSbUV-T0nO6gNgl4OTuh0AzWsiX0F1D4zyRRL3SXPMI6uw7NeT47RI5NvJYejNhn50tCBaoEY-aaGU4WvfDW9rUHj_7zmlILaOVjY77W3_c4rObi_vrrXCVMsQ9emRrUQ_wPh6CpeXI-SEJFM38M3g4jITlTYbQVbxHu23CGReLCpq2CsGG1HJpBuImbehFcEMeEgCyhVL9AQ8KWIowusXF4oSTc5wUKfwQiWIQsutKMzGD49WyI0Ke92rKWFxkyMorgcHEkz3jnbypHd4igo-T9D1cQdGHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هم اکنون حملات بی امان اسرائیل به لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/alonews/124482" target="_blank">📅 17:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124481">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2ksQISPlafofvKMv8x1CZzGOAe7_8IsGcLtZ_7S8c16o0X4BLXAFC_2qDVoIoUMXHThHChqo4AeKQCj3dpIHlIfo0hCjnsuORZugozDRwdVGBkFPLeiuo4CVQkUvdEDHFHPIz5TbnDQz8M5LPj5ew5geh9RkJOIrsGHhHHqIbTPjX20pocVi1gzrrqacfpSiBIEu5IW-dv-i0TQC5HuIUf1VLGKhGW4fFjYZd6lF6KRFpUnJwcCC6y-UnX0DSxfLHCEdIhdiZmY0NWPWNhQ8Ic6e95TJ4SEPiBeAdv9KIYmCp-egqRM6EBh5jTEa8mzwB4Ed3rPdERg7NmC80js1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون شهردار تهران:
برای تشییع جنازه علی خامنه‌ای سه روز مراسم بدرقه برنامه ریزی شده
تشییع تو تهران، قم و مشهد قطعیه و تو تهران حداقل ۲۴ ساعت طول میکشه.
در حال تدارک برای جمعیتی بیش از 15 الی 20 میلیون نفر تو پایتخت هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/124481" target="_blank">📅 17:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124480">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
شبکه اجتماعی لینکدین پس از بازگشایی تدریجی اینترنت بین‌الملل، بدون نیاز به فیلترشکن در دسترس کاربران ایرانی قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124480" target="_blank">📅 17:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124479">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMZ5Oc8Z2rFZRdZ8_fQQujsCjSZCimNPdPRps6ouE47p0ZOa3JLPbRZWPkQBUOL0LWAuhihSktTNo_Ha5vk8yF3RTh9JAXrdujlywI0mV34R4vedTesN8yRFgAq3WN8_cSPJ8aJaB4RTgYwKEEFNW1IpfUkv_qEjpnljkr_WCzYYT_w4BhKRpD_2uv6eusa-0585nn6TVI0gX1WsiMJWDLkgeThBltCUP8U5c4TXbqZTTPz9E0wZk-NExOVeUMLnR-HyvlQaO5LiE-92F8_sG39_jrV1nHRd_nYBcfVFJqJ7XpMKkYwdpd0at2LI2EHzVy0RqIQ9H0uvj71YlNz0rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بانک مرکزی: سقف کارت به کارت رو از ۱۰ میلیون به ۱۵ میلیون افزایش دادیم مردم حال کنن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/124479" target="_blank">📅 16:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124478">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
خبرگزاری معتبر فارس: یک منبع آگاه می‌گوید که تبادل پیام بین ایران و آمریکا برای آنچه دست‌یابی به یادداشت تفاهم اولیه بین تهران و واشنگتن خوانده می‌شود، دست‌کم چند روز است که متوقف شده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124478" target="_blank">📅 16:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124477">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYI2IlFEIPoeLgtbgMF_sOnLwzPrOUVBNWKWCzmIOESG72ge3VMtzdCnbCINm9LTaNICZyoQtgRzq3JgclCF5rNlAOE5Y4ql944rNSfAPLo1x4f35PWP5QTV_4zP8z8STJ--Q8sHrkF4LGFRsZ5e98FVR_Wdhroj99i2wvV0huPSpJ1c-NoUAmSYvExPP5bUGJxj6sQM_OcU9Wu7cTSPXyc3GtiuHdebY6Iz3Js-Emhq-sAyd8ZLgQdppNRwCTicneYBw1_D0gQIXsp5OI5MxeogN3GdA0AHyZZYLjTz7t6p8Zhqwi-ml1G_lZUMi2bNtuIztqe78cC6Zdflftu2Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خسروپناه؛ دبیرشورای عالی انقلاب فرهنگی:
من در زمان شاه به خاطر اینکه فیلما مبتذل بودن به سینما نرفتم؛ بعد از انقلاب هم نرفتم.
گاهی وقتا بهم میگن فلان فیلمو دیدی؟! میگم من سینما نمیرم. فیلمو بیارید اینجا ببینم. به جوونا هم توصیه میکنم سینما نرن.
در زمان شاه هر خانوم بی حجاب و پا لختی میومد مغازه پدرم من از بالا پشت بوم با تیروکمان میزدمش. پدرم هم میگفت چون حجاب ندارن کار خوبی میکنی و شرعا ضامن هستی.
جوون که بودم یه شب خواب حضرت علی رو دیدم که اومد گفت برو طلبه شو. منم رفتم طلبه شدم.
خسروپناه کسیه که تاثیر معدل نهایی بر کنکور رو تصویب کرده و دانش آموزا ازش ناراحتن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/124477" target="_blank">📅 16:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124476">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVkGMhPBRT2mPkuVo-wDUz1S9jfqAkIONpO038y7W_nK7lRlGIDuKnyqvOWQCyfY5SgrS9r7-GcLad4cOF0CIc4C23SNFEQZTKYP2XT5erMMZ8FM3FR95abhWXDJER27AA2kRWREYldXRKkPPtJvGUuUENcR2vcZPb1zJPPWcwV-m6BruAhvkULON7LM9X9mGfBJLws7GJVQkUcgoLaNfYOIMZMM1qkjKvMkkcyPLT57CKhzenHVgtw-WcUvSTBU3SKI-kFI-c9CFxytOBJLkxu9YlIelndQosIzBhA6F8b_HHU7jImL203fhyUFgSWqvM-rKvLT-meh2Lp_JiMpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یاشار سلطانی: ‏سیاست‌گذاری و حکمرانی در صنعت خودرو، از راهزنی عبور کرده و به حرامزادگی⁩ رسیده است
🔴
البته با پوزش از حرامزاده‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124476" target="_blank">📅 16:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124475">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cncr3RJAs2v3NACsiD9kvHXnNgmeP9whp6E_7c_VIHQa6FSbZTOaa_z_H0iHJBdpcwP814j_Qu-fo8O2JJvUfqRSL8vQizA71B7Xgr-2Noa-dMqxlTYnmDAFvw-nI4Q13Eh4RLiwwLYzSWSAqoHpq3EIcPLY3VQhvWRmpW_jPBU8u6dWyiWTSrEz6AVgZt03hISY8S3dT8F5BJbM6bA9-KPsCmsDG0kTX7pLAIZMNhMnnv7oQOUs23gO2d_iAnUiTw2l6ByIBv5Z4YTOCfbPywRWlSEK6sIU1ssySdM3YDxFyf4nRkvIJRqNCKlZAdJId9s3TkigaCL9Wrz51onhgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید اکانت ایکس سفارت ایران در ارمنستان: طولانی‌ترین دوره ریاست جمهوری ایالات متحده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/124475" target="_blank">📅 16:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124474">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">واکنش آموزش و پرورش و وزارت علوم به تجمع اعتراضی دانش آموزان  [@AloTweet]</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124474" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124471">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/on1dcpF6vfjUWpRYCFX98FeqXNl7waJLTOPyNOnMdxYsdLxkeyuYS4OttixzlJ8EBk03G0q51eIsUaV7Wr96tnqmS2SkmnYlMjPwY-2EJFPwdb-9yVDx_8oTeBKFxdnQhm3MG-1ARJakwiv9gojkawTfNby3sGrI1KGuo1HGZ5gyA5A4aIQzShA03a8V0iFIDSBNc-28PKE1TMjn1g2bLmAmkS5P1xTgDEKxIF_g2I_9bPvyyC3xMqaknsDnYl_K6NaNFcoNmOE5txoI0JXpNMQuLESpMz6IpnsYsiWnGXdPl0X8ubjwDQEAlCxJHfrXOqgRHgOOCXLK7UUZu_mFWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tN5GZLK4qt39HEGFtYrOJAAYRqIGuRGrB-XIsklZNYNGex1AyI-2hu507rDCvg1TLFUWNKPP66Kciuav0DI-swG2XMgI3fFU0IX9AF5M-nH0A815VJmZMcOub_PFAjtsX1_nMHuQYK5BB1YRPBglt2Sde0lRQlWvd_MZ-_z3X76Lc-9VfqFeidvKTHwdpCQjwd8nuoFZnBvR1HTZADBlqHV5DJZ-JaXyRaqkjDgYopHA0CurKFS7UiKHxSJWl0ivYNKM-yi5CSgR1uNbK40aiq587kt9Wn4PFIwshar24OCQ3_9PuHXyrk97nnJRCaf_bnxGX7vvVIZLMdxDiaIVYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hm4EEgnVjPdI7rEVyDVR05PfgnpgRPmWpP9lUfpATKHRVJ12DoldabXoeZaGx6e31aODLCV22WOUCiDuVOSS7r1vUlbQMXKiEMUnCu9TT-LcrvoW1ipDPy98ublC2XX42-DPNs929zRjYNQlWIXehN_6IZ9RhoQvlNj4IQchnSt2sX9AZbP80-5gXZw3PLIcf0gY5m5eG1ejJoYpHBuXCSCd5BKxXT1nfJYt6rdPsmzN9RI3iqHcZldIefG9rkPZMoOar0oUw---dI6FU97mB82JA635lPr0OGFiphvsKRtGjQXL0WHreOyNtvHBjxvGrL5KajChSrZvfpk9dCWvjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حملات هوایی به میدون، نبطیه، القلیله و الحنیه در جنوب لبنان انجام داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/124471" target="_blank">📅 16:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124470">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 8T!
🚀
😍
فقط گیگی 8 تومن
😍
✅
باخرید 90 گیگ 100 گیگ تحویل بگیرید
😍
✅
❌
فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!  @Netaazaadbot @NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/alonews/124470" target="_blank">📅 16:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124469">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/acBmjWxkp-rcScInzhdr5wwGa3oraDchs3yT4YoGARhyfVR1LhSX6bdi4TzbjdqTJqt999EreCV72sRCyWSabf_JmttJGwTkqTQPO84cJVK1y_oaSh_q3XaQD2rnSBqdwN2QgEKTtLZ_kcA8WmDE8HC83iL9QBhmcPAPji-1vkPmnTz1KqnPBeHafeiz0eNyy79TEyKcEctGyH0B2UQOvgk9WJI1NCCkdHBcfigU62Y-Uu1cjgwiq0gEEo_W-eliw91_vz1OUexIwLr-cYnpCtOhJxpymi57OO0VwQaEhkTg6LKhHCP9MsKoUGRoD8J2LGOe7Qo22B_JCIQd_LAMZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 8T!
🚀
😍
فقط گیگی 8 تومن
😍
✅
باخرید
90 گیگ
100 گیگ تحویل بگیرید
😍
✅
❌
فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!
@Netaazaadbot
@NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا حتی در ساعات شلوغ
@Netaazaadbot
@NetAazaadBot
📩
برای خرید و دریافت سرویس استارت رو بزن
✅</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/124469" target="_blank">📅 16:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124468">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
بریتیش ایرویز، همه پروازهاش به اسرائیل رو تا ۲۴ اکتبر لغو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124468" target="_blank">📅 16:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124467">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned «
👈
جهت رزرو تبلیغات فوتبالی ویژه جام جهانی و vpn در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews https://t.me/ads_alonews
»</div>
<div class="tg-footer"><a href="https://t.me/alonews/124467" target="_blank">📅 16:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124466">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1e247e908.mp4?token=rapD9W92XA1zkXeMxg7qZeEmpiJ2ITln1sB8N4YOVrpXotVX8qfSyMoAbuywy_w2jIWRcGutw2pXbA5Jzia0JXj4VAa8_zj1af0_aasS2uFYzhU7GdNu5nZp4pvjyjYm1SRGdlw9dmDkEQKC5LCpJNHRFOJrKEoatfwbVngE9J0QJPzgnCXg5dAF4-C_9iKB40RRuzJxXOycH1xLn9qsD8DM8vtH-vpo0RLnmUDv5PPPmmtxQ9Ki6T6WHiZBCsCK8X0VkUQQ_DtDNslnx_-cwVfqgc3kh6jj8gBFvv1XgTE2f2JMSvUsiZwHpB7UALeiFRShsTi4diHv0sFlA2R6IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1e247e908.mp4?token=rapD9W92XA1zkXeMxg7qZeEmpiJ2ITln1sB8N4YOVrpXotVX8qfSyMoAbuywy_w2jIWRcGutw2pXbA5Jzia0JXj4VAa8_zj1af0_aasS2uFYzhU7GdNu5nZp4pvjyjYm1SRGdlw9dmDkEQKC5LCpJNHRFOJrKEoatfwbVngE9J0QJPzgnCXg5dAF4-C_9iKB40RRuzJxXOycH1xLn9qsD8DM8vtH-vpo0RLnmUDv5PPPmmtxQ9Ki6T6WHiZBCsCK8X0VkUQQ_DtDNslnx_-cwVfqgc3kh6jj8gBFvv1XgTE2f2JMSvUsiZwHpB7UALeiFRShsTi4diHv0sFlA2R6IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جان بولتون درباره ترامپ: وقتی کسی سه بار می‌گوید «اهمیت نمی‌دهم»، شاید به این معنی باشد که واقعاً اهمیت می‌دهد.
🔴
اگر ترامپ نگران نبود، با نتانیاهو تماس نمی‌گرفت تا برای آتش‌بس در لبنان تلاش کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124466" target="_blank">📅 16:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124465">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70931bb43b.mp4?token=uDZS8M2NcMdLoDkAq2PD1RJ_vrJZgwgabE46QEr6sG8fofugYGG-F5pDHK5zxAzwwgH9A5nH3BnnIrvWnd1z0CvNUg7JjlyNI8APvogbeNS1litEfGw91d-LF5OcCAnhfKe2EVf4BbaYapkI9VK3_J6BCzFcI01Yb6ijEWcFCL-NCRniLEE-gK9w9Pj8k9yKGfD2FLlpKlx_NiUdOourv0eG8RpPAbsAwUXNCRW7oARQujyhuzsIsBENsYTaLzquMz83hIci3znSDtkGPzJj-mcoMYv4Ht8tUPBPFLRf88sJ2BTjx2cU6qVG6XfkSXAADJC5lTKJtV7q1-q7LlNdYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70931bb43b.mp4?token=uDZS8M2NcMdLoDkAq2PD1RJ_vrJZgwgabE46QEr6sG8fofugYGG-F5pDHK5zxAzwwgH9A5nH3BnnIrvWnd1z0CvNUg7JjlyNI8APvogbeNS1litEfGw91d-LF5OcCAnhfKe2EVf4BbaYapkI9VK3_J6BCzFcI01Yb6ijEWcFCL-NCRniLEE-gK9w9Pj8k9yKGfD2FLlpKlx_NiUdOourv0eG8RpPAbsAwUXNCRW7oARQujyhuzsIsBENsYTaLzquMz83hIci3znSDtkGPzJj-mcoMYv4Ht8tUPBPFLRf88sJ2BTjx2cU6qVG6XfkSXAADJC5lTKJtV7q1-q7LlNdYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جان بولتون درباره ترامپ و جنگ ایران:فکر می‌کنم او به شدت به دنبال یک توافق است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124465" target="_blank">📅 16:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124464">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0a709187.mp4?token=BZxM8-5kC-8C2nLcLsiQPxkcUiXt13XCcVvzYbiY8_9u4uY_lpEfGaeYtpqSefAeXCk1yhU2XrqPorInPokR8FcOjT5ZyaxMJU1wi_rgL7X3oV6r6dzAuK-uZ7PD0SkruaxKTyVaq-7WxZR9H6yOl-3GRYFjcK16iloQQr30Nl8Y4SwZkSv-9IuNaVAbgWHd3fAK6zdzLIm5PaAZLzu2MOIZy3Iq0gD5FYChIZCAp4m1NI8njtpkv6sr7mBnd9MM8LBLSUc3Z3m6UY0VpHlt9WSfNPmI8jwUD7uPIHtATyl2dyo1GyK3bZ5qeU3I2YDPmazLMJzXND6l4VXjovtAww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0a709187.mp4?token=BZxM8-5kC-8C2nLcLsiQPxkcUiXt13XCcVvzYbiY8_9u4uY_lpEfGaeYtpqSefAeXCk1yhU2XrqPorInPokR8FcOjT5ZyaxMJU1wi_rgL7X3oV6r6dzAuK-uZ7PD0SkruaxKTyVaq-7WxZR9H6yOl-3GRYFjcK16iloQQr30Nl8Y4SwZkSv-9IuNaVAbgWHd3fAK6zdzLIm5PaAZLzu2MOIZy3Iq0gD5FYChIZCAp4m1NI8njtpkv6sr7mBnd9MM8LBLSUc3Z3m6UY0VpHlt9WSfNPmI8jwUD7uPIHtATyl2dyo1GyK3bZ5qeU3I2YDPmazLMJzXND6l4VXjovtAww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جان بولتون: ایران معتقد است که می‌تواند از ترامپ بیشتر دوام بیاورد - اینکه صبر بیشتری نسبت به او دارد زیرا او به شدت به دنبال کاهش قیمت نفت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124464" target="_blank">📅 16:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124463">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
حماس: آماده واگذاری اداره غزه به کمیته ملی هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124463" target="_blank">📅 16:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124462">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
بحرین به دلیل شرایط امنیتی،
سفر شهروندان خود به عراق و ایران را ممنوع اعلام کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/124462" target="_blank">📅 16:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124461">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
جهت رزرو تبلیغات فوتبالی ویژه جام جهانی و vpn در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124461" target="_blank">📅 15:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124460">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رئیس سابق موساد در مراسم خداحافظی:اردوغان ترامپ را متقاعد کرد که عملیات نظامی به رهبری کردها را که قرار بود اولین گام در یک طرح گسترده تر علیه رژیم ایران باشد، لغو کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/124460" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124459">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
وزیر خارجه ترکیه: اسرائیل معتقد نیست که صلح بین آمریکا و ایران می‌تواند به نفعش باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124459" target="_blank">📅 15:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124458">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLNl0ubRSW8UlTzmZhrJBQvF9CFlHCZt8cNHScEvnU7M57Y3MUY-hTOm-b8l5tizX2mpOr4PxYSRg5DfClk5-V1CcsQPUPe8P9hlgjUpzhNpGGCSfqf4irx6eUrsi67cmEdZkEuTDV3FQTGi_VGlhmZOT7mt8LqHtGwLFgYeExzq-FDPEXSc1AHgw1A3is4uRbf3372gSUyi1WewgAOgw4DoqPBBRie632QrJkFX4u_4ApJ9vB777nLrzXycg5oXWb_dF2X3AvB5S6H3BbogXKqhrkIr2nusSJO3Nz9XGZQpOSbOqLX1B3SaUg-isYYdzNMua8-hz_Jf0kWcvLDQGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روند ۶۰ ساله قیمت نفت و اثر شوک‌ها بر آن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/124458" target="_blank">📅 15:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124457">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSESZEqOmYryFjj0NZtXTjJhLaiBPO5STK3gcE1wd_JmXjyr2mcnqJZ_8P7StlZDqUZWSZ3gAOPOjFS5-R1iRoaJnGP1JbTufUlTNj8U0nTABMkG8Vc6-t_Us1oIxbdjIS7phToxTMTTnBSMGjn0qwk3PER46DvuP5fyjiDSg2W5xLWTH003cIF3X582JRTjNADvT4OTzA-uS_iHdnfPFw9PPla4caNoNdwmHGZgw-TCnMDKEmBUppm3L_PqZkzx40v1dTibmnFXN2I6xe-fYRMBc3knCT9obiLEieI0LiRrLBll31h4Z-Wi7sqcxpuiDr365pxbConEtEwkUcT7Lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/124457" target="_blank">📅 15:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124456">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc44189c36.mp4?token=DPPNzon7Kbj1_CQJWH86-INTs9UUz-v4S3hI1fYJP6qPQsC91rhb6KOkCeq9Kd_RgxcQ2_FzeMlVZVKnjY7kVO0x8QmATpiW7Xa7ILsqvgnkGxnPKu01AEjZuVYMFIVO65Xg2-gmMiTXDNFWL1V2pE5erjNYOAml6enLn4PMZ1fHPeRIHHZAF5H4GnRfYs1It3NMrIl4cWbmUIWtkFmcerd3v0C_h7xcG8q6UoVmpCggwsgxP4XhAgajKYf7eHi-iRQWou-fWiaGi0HpDBWJrZvivV8G69ZMviEyoqQ--XF4K2R2a92lRPFa25KygWu00yKbdtpqK3xJd-dSin2l-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc44189c36.mp4?token=DPPNzon7Kbj1_CQJWH86-INTs9UUz-v4S3hI1fYJP6qPQsC91rhb6KOkCeq9Kd_RgxcQ2_FzeMlVZVKnjY7kVO0x8QmATpiW7Xa7ILsqvgnkGxnPKu01AEjZuVYMFIVO65Xg2-gmMiTXDNFWL1V2pE5erjNYOAml6enLn4PMZ1fHPeRIHHZAF5H4GnRfYs1It3NMrIl4cWbmUIWtkFmcerd3v0C_h7xcG8q6UoVmpCggwsgxP4XhAgajKYf7eHi-iRQWou-fWiaGi0HpDBWJrZvivV8G69ZMviEyoqQ--XF4K2R2a92lRPFa25KygWu00yKbdtpqK3xJd-dSin2l-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای حزب‌الله از فاصله کمتر ۱۰۰ متر، با آرپیچی تانک‌های اسرائیل رو میزنن!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124456" target="_blank">📅 15:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124455">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
نماینده روسیه در سازمان های بین المللی در وین:انتقال اورانیوم غنی‌شده ایران به خارج از کشور لزوما ضروری نیست. برای این کار، رضایت تهران نیاز است.
🔴
از لحاظ تئوری، در صورت توافق دو طرف، گزینه رقیق‌سازی اورانیوم غنی‌شده در خاک ایران نیز وجود دارد. بنابراین، گمانه‌زنی‌ها در این زمینه زودهنگام است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124455" target="_blank">📅 15:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124453">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/027e5850b9.mp4?token=nrIKzC0Zn2OtJdauOHGbzSmNhnsb2PZfkJ9iH80Xm6yJ8dKnjTLJhk-wPpVRVTkgjtaQSbZJHB7iUFjJlbMFLbnAsKTr97-XpPaRemLFe5r0J4A-3Q93VRnwprnUmthvyyOBQyVLFi-fI2yHlk96YNeDFKUTUZ7tiGR3GzUds8Uirmvc3ZwxfJkYqjbmRenR_rkoB6F9rYeXkO-qSWdVc0jnFvWwAdf150XrrwvkwZNkoawCNinag-PGvkGmtAiSyefO4Bo9E-ZPm5EgU7XyzBdTK9Yq9-nnWdVun0ylm7WP9eRptLWKXSrxgx9G6vtWJo60uR8LrA_apyxyB1FpfllB7k-IXOYrXBwipfeE4uMGviQnowWxw8oKuNjj3Je_aLILqDfjfNpu4c-PVW4MDNL9HDLGwqhsAxJ7G3qaroKbkEtDwaAeontsc_HDV5ynDuO3mt63B-56VQZ8FfgrVbh8wTcGzIV5BszIDdGwr-Y5dpCjpMEHzyE82yGk149hT_DatpEhnPuSDa5dUeGlTxhGYDgGUoEjHEOn5t6RtKo_q09WHB5y6vwMSIC4rZo1ZsOv2CqEEReEqb43V0UEyi4IQIrGP8Vm8S8F4WQGimc7hbnRptaWoJT5XP04YJrTD2hUU8wcvgsgN6BETbFlJD6LkX1dZU7ZCZ6wqmjGOfk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/027e5850b9.mp4?token=nrIKzC0Zn2OtJdauOHGbzSmNhnsb2PZfkJ9iH80Xm6yJ8dKnjTLJhk-wPpVRVTkgjtaQSbZJHB7iUFjJlbMFLbnAsKTr97-XpPaRemLFe5r0J4A-3Q93VRnwprnUmthvyyOBQyVLFi-fI2yHlk96YNeDFKUTUZ7tiGR3GzUds8Uirmvc3ZwxfJkYqjbmRenR_rkoB6F9rYeXkO-qSWdVc0jnFvWwAdf150XrrwvkwZNkoawCNinag-PGvkGmtAiSyefO4Bo9E-ZPm5EgU7XyzBdTK9Yq9-nnWdVun0ylm7WP9eRptLWKXSrxgx9G6vtWJo60uR8LrA_apyxyB1FpfllB7k-IXOYrXBwipfeE4uMGviQnowWxw8oKuNjj3Je_aLILqDfjfNpu4c-PVW4MDNL9HDLGwqhsAxJ7G3qaroKbkEtDwaAeontsc_HDV5ynDuO3mt63B-56VQZ8FfgrVbh8wTcGzIV5BszIDdGwr-Y5dpCjpMEHzyE82yGk149hT_DatpEhnPuSDa5dUeGlTxhGYDgGUoEjHEOn5t6RtKo_q09WHB5y6vwMSIC4rZo1ZsOv2CqEEReEqb43V0UEyi4IQIrGP8Vm8S8F4WQGimc7hbnRptaWoJT5XP04YJrTD2hUU8wcvgsgN6BETbFlJD6LkX1dZU7ZCZ6wqmjGOfk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل امروز سفارت خود را در فیجی افتتاح کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124453" target="_blank">📅 15:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124452">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
فوری / یک افسر ارشد ایرانی به CBS گفت که جنگ تازه با آمریکا به نظر «اجتناب‌ناپذیر» می‌آید چون اسرائیل و حزب‌الله به درگیری ادامه می‌دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124452" target="_blank">📅 15:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124451">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
فیلیپ خوری، معاون اجرایی شرکت ادنوک (شرکت نفت ابوظبی)، می‌گوید:
«اگر تقاضا افزایش یابد و بحران عرضه ناشی از جنگ با ایران ادامه پیدا کند، ماه آگوست می‌تواند نقطه عطفی برای جهش شدید قیمت نفت باشد؛ و حتی پس از بازگشایی تنگه هرمز، ممکن است تا یک سال طول بکشد تا زنجیره‌های تأمین انرژی بازیابی شوند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/124451" target="_blank">📅 15:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124450">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
منبعی در هیئت لبنانی به LBCI:
ما احساس می‌کنیم که مذاکرات این هفته مثبت خواهد بود و امیدواریم که مارکو روبیو، وزیر امور خارجه آمریکا، در جلسه مذاکره امروز حضور یابد، اگرچه این هنوز تأیید نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124450" target="_blank">📅 15:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124446">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sr9rO0AW5kVzi1-uUdZcaRUNR5i3kCGmqhxXMxIv5TepW3qpy66qX8uResy5p3NuOeiQudRGx2uMlGtME5wQ-1A68TB978h-dGaRfWxsCIU2IFgDts2heY02w7wHSWvxBRAgEtRX8i9-7prKKpNIv9QMYyUPZakusf2AwijL7VvUhR_bYKZuhUmPolOYq4fQeiUTFAfeltTTNhpY2WyLwY4e2mNhUYmPELrMC-jQ4cb3n4vdYj2cWsvRBIbp2DYG613saMrTWKEVsCIi19WthV2LyYjC1cldgEKHHUzIqirRnwN6lx7PkftGfYxJkmxiA3cuD-0ic6FEzD_M7J6lzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GriT5DIfgeDw8-kzmeNhQjlpJBWjjcBI-xeM31axl5jqxlwSkyBGqNCuDF6TaxvREGGOjm6xJHRynUF_qlWwIbwsU_Wyl35DAn_GPkWyFEUVXuOPS1BE4PO-rg7q5qI0NM0oNinbiykLUzkilWX_xSWemn7sEq-GFs48AFOjChlooVX7IoaFjwatC8bot5TuZJ5ox71irUawbkSPCEiZXj5QXw5cg4knQ28-LmDiDLnGwf0sXp1N6uR8yuhiqNwR68fWeb71D-dHX8dzfAUFs49475zCd2-Bgo0TBAJRajfRJP2-4ZnKuxBI8QFzlQ8fhOfl-jNCDk5aWvmiRFrBew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S0uRqqMQ-7KdcHKsIcewtL_7Xycc2CwwBHOboQE98ywzI8dglyeR2bi093ekNJE6jr6Z6TSTpxXOtWp4auvY7O43B6H06gG_nW2f0PUJu1uQ5dv76nQ4y2RveLkLfz3WipsZMNoWv4S2fEAn7Do5-jX7ZRgYITn_pf_IOUsnwBPTwtoRducTmJ1T0W93iFWKl0LOEvEy1BimdeHIwMYiS1Bm6XO9bHlCC22lWNLicTwsfTkd0JjdUOw-FBsbUO6W7b-SxgHaE3vJVM1D_LpCok08o-7c0ngXG2MRUZ5UqkimUAdXOUhB4OlJszpVCqMHBZskU0RKtH0ZvPrFfIvLtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/slI0wupgmlMNUEUXJ6oVspd96x9E1y3_wdhLGB9R-knOBioarMdKVWqvOe41EAQ4WIj6IJqkp7hUuR85RtLZ-pur5XxCf8THcThFnUJU7IN6JQ0UwOxQDpXa31uBz9fTZamMMV3dqMaqj_lznzGhwzhw47NnsKaQESomYj3iZx6-XvPpeQYmVdl7nyQjPy5wuLm1QPT0Ahsb6oeWr_poNKpux71WX0hTUMn_zyt-_Xdsejq3zTtkiwccnah2SH3tLTebGvuT6tB-IY1MetzoaFJF1WjbIb-xafJrHrKZubkJKrNXydEksFbcnjhhP-wSQaQ4Y-1xSVUYIAYtKbLgzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی به حملات هوایی خود در سراسر جنوب لبنان ادامه می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124446" target="_blank">📅 15:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124444">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dc2SEXXPboIl3F6E0wQ7ZW35SFXjev64_EUdPsK9yAP6eDI_Gt9t7xo5DlqgYeAI4oQ8ef0qQ7-u4WzBPFNeIO0s_7IAhVTMs0R_8fNDHS-tpqh7QQZ0W9duiV00q_yK97LiadM0G9Us33ah__ois5cQ3t3wFOP6lgzS9MOmnJg8HqH3z3jfl1fmZneysmJ_PaCT7cAlUwjVDnMgZ7ul_VkcLfGeArLJsXYKittEpKTNyFrgxK9fC98DWvDeL5X2FiOfO4OrEFD1ZwCLfCn-I3bz6LADSmKZbcZHz3qU_adypeFIsXI66OdWTLQxwyKo_HXR5kvbnxx9Jff922w0VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l74pS7rOiG2i9bWDRn-ZxnYILIMOXMEOyeNg7v4KX4X1j_8PcCDfno1h8cwT9UFsAC34uO--oOshpvwxbqicDbDrlQ4NYYm_IkabLLZWCfTbuqvdgU3iL38W0JT-QM-BtCWeusV1oLzp1Ujwjb_NvibSlMSUuakPr-NEjBfMaI9JWPPD2n6fqc2rZ1jNyXLZ1PX3MT6tbv8y7ybRHtMqarCZQt9KG7DBbBAYBiQpP6FexfE95IryB82uwEW0_1fehL32rFAMw0TSoP793Nh4SEuYL0vsNOACriHw1vJFFOT6dN6eNBuRgK2vjQGRrNq72zQb_UPrwWQuHam9FWrjPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💔
جاویدنام مازیار نوروزی اصفهانی 36 ساله، 18 دی با شلیک تیر جنگی به سر در گرگان کشته شد. پسر عزیز و شجاع ما دغدغه  مالی نداشت برای آزادی وطنش رفت.
🔴
حتی اجازه گرفتن مراسم و عزاداری به خانواده داده نشد.
🤔
عرزشی حرام زاده از عدل علی بگو
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124444" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124443">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVjoCDPu5SX9IeNYKBYACVVfD098RsIBoYZ_HrAUH73xlGvPVNSqhPR1DseHYHjLRoellv3mjiteYlKzNnKDV4ONyFUj7Jfhfv1Jk-Ay3EHP4xqTSb0YEbPVZyXMMLWzVaJnzuqB1JPM2CA1DRGLwgH-wOnVkhrUtiFoSf3JZnaliubjycovb67IJS6j11WBaKF9d2G0K2gXqXvr04sYdoxJfZW2SSTBIltyRMdzgDEL8OVv9SZuc9ExpvNGoWFWrB4qGNfMGA7CGQrServsvyFRIBqKKJ6N0jvAySGjV13sx9VxppwDzmAe5c3OLiTZzHwvzHuKr0gJvaMDxDsPmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازار داغ اجاره پراید برای کار در تاکسی آنلاین ؛ روزی ۸۰۰ هزار تومان...!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124443" target="_blank">📅 15:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124442">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1414d98730.mp4?token=vh6Rgy-vaCrGixRtZZtwvsnqba3adSM-vuV8bZBSyeCi2ByE0f_NbInu47KWmLuPe-vowLUM-kd_PNZccGMlL9nApuxEb37orFsSKICbe3_XLwqWAAjGeezzE_zE4vW5WY2eUz9dIi4nxQgLrfZN8XfIuMQZ-tB1IxxeX9-QpbnPWKu7_ezhlcy0vRWWsJURrJFC-QXEYlUGflotjDrMQfhS_iSZQK-_ozbAqfo0f4HVCN8f80xPongF6_-O6Xt4tyRe4PKLkLU6jMn9qOSpgnmAxrWNHepzvLwjW57-cRfrgu3Uw--RAnta9xUnPFTAjI4KincM8GdYK81LEKf4fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1414d98730.mp4?token=vh6Rgy-vaCrGixRtZZtwvsnqba3adSM-vuV8bZBSyeCi2ByE0f_NbInu47KWmLuPe-vowLUM-kd_PNZccGMlL9nApuxEb37orFsSKICbe3_XLwqWAAjGeezzE_zE4vW5WY2eUz9dIi4nxQgLrfZN8XfIuMQZ-tB1IxxeX9-QpbnPWKu7_ezhlcy0vRWWsJURrJFC-QXEYlUGflotjDrMQfhS_iSZQK-_ozbAqfo0f4HVCN8f80xPongF6_-O6Xt4tyRe4PKLkLU6jMn9qOSpgnmAxrWNHepzvLwjW57-cRfrgu3Uw--RAnta9xUnPFTAjI4KincM8GdYK81LEKf4fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از
حمله هوایی و انهدام سامانه موشکی در جنگ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124442" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124441">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
فرمانده قرارگاه مشترک پدافند هوایی:
شبکه پدافند هوایی یکی از سنگین‌ترین خسارات تجهیزاتی را به دشمنان در تاریخ نبردهای هوایی وارد ساخت
🔴
پاسخ متفاوت ایران با استفاده از تاکتیک‌های پراکندگی، فریب الکترونیکی و اصابت دقیق، اثرگذاری حملات هوایی را به شدت کاهش داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124441" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124440">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
رویترز: امروز در پی انتظار بازارهای مالی برای پیشرفت در مذاکرات ایران و آمریکا پس از آتش‌بس در لبنان، قیمت نفت کاهش یافت، طلا در محدوده باریکی حرکت کرد و دلار تثبیت شد
🔴
عدم قطعیت‌های ژئوپلیتیکی گسترده‌، معامله‌گران را در حالت تنش نگه داشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/124440" target="_blank">📅 15:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124439">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
کارت‌به‌کارت بین‌بانکی از ۱۰ میلیون تومان به ۱۵ میلیون تومان افزایش یافت
🔴
بانک مرکزی:  سقف خرید با کارت بانکی به ۴۰۰ میلیون تومان رسید.
🔴
در حوزه انتقال وجه غیرحضوری نیز سقف حساب‌های غیرتجاری به ۳۰۰ میلیون تومان و حساب‌های تجاری به یک میلیارد تومان افزایش یافته است.
🔴
انتقال از طریق «پایا» و «ساتنا» همچنان تا سقف ۲۰۰ میلیون تومان انجام می‌شود.
🔴
سقف برداشت نقدی از خودپرداز‌ها نیز ۵۰۰ هزار تومان تعیین شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124439" target="_blank">📅 15:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124438">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
لینکدین رفع فیلتر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124438" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124437">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
صدر اعظم آلمان مرز: ما ۴۵۰ میلیون مصرف‌کننده در اتحادیه اروپا هستیم.
🔴
اتحادیه اروپا ۱۰۰ میلیون مصرف‌کننده بیشتر از ایالات متحده آمریکا دارد. نباید خودمان را کوچکتر از آنچه هستیم نشان دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124437" target="_blank">📅 14:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124436">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
صدر اعظم آلمان مرز: ما می‌خواهیم آلمان را دوباره به مکانی مقرون‌به‌صرفه برای انجام کسب‌وکار تبدیل کنیم.
🔴
ما در آلمان با مشکل رقابت قیمتی مواجه هستیم.
🔴
حتی اگر همه دوست نداشته باشند این را بشنوند، آلمان بیش از حد گران شده است.
🔴
در بسیاری از حوزه‌ها، دیگر رقابتی نیستیم چون نمی‌توانیم از نظر قیمت با مناطق جهان که با ما رقابت می‌کنند، همگام شویم.
🔴
دلیلی برای بدبینی یا ناامیدی نسبت به آینده کشورمان وجود ندارد.
🔴
بهترین سال‌های آلمان پشت سر ما نیست؛ سال‌های بسیار خوبی در پیش رو داریم—در آلمان شرقی، در آلمان غربی، در کل آلمان و در اروپا.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/124436" target="_blank">📅 14:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124435">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9da7adeabd.mp4?token=Ev_HKG32RpY2MgrRXxhAJMhH3nIbhn9WleI7R-5hgYza4R_zwMp8uzIwNPHK8H3JK69TW1-gUsIV4nvEXLmTmEe2qqdCOvPFjASOyFiSaO3yFBwmdETjZgTSJVCvvDwncxRrJipsWPK-PDX1jJnMepO8-tFmdKdD86Ik9sd_7E7lEoWpNCD4w8mnbxpfVBp9If6ENIGIXxUuT17ruTeJr_scsBG5uwr4AD7Z5PoJNqO_Ky6ZGBIZi2ALHDg66TpYnCz5kgUYr0-nQQgMmflGBNCGAdMKpqkRA4tuNiglnMRMr97ESnj4MzEREla8oOO5tuZvx_HS6vqIRDniZzAFqpw5CFAlzRmIZVTyWlk1D9x_MShPzCy0f5x3h7AzC2cRUfZ0zsfhScVEkUI5HlcJo_RMbOkZZdDusdrqmk8gvNB91nbfEPQDMkRYsyXfKahiNjLRIj4SI0fGT0JC6SK69j6J5e8UYdGxptF3z_ozkL6FgvdSjxfsztjRVr3Ff71_SbSW5ZyrvXaGvEyrxVetRGCC-0tobLHg9L2eUeyW9YHAClbzIm-pWJHf1xC1uyMU3wptd6GTIfPE5EXPhD0pt0JohwIRrcWp1xRJB8HBYYGEy4YG2A_gtFEW4TNeiG0GWK-nZqg6gTOqNp6wODTQpq04O9sQyjhpVcSOQfb9R3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9da7adeabd.mp4?token=Ev_HKG32RpY2MgrRXxhAJMhH3nIbhn9WleI7R-5hgYza4R_zwMp8uzIwNPHK8H3JK69TW1-gUsIV4nvEXLmTmEe2qqdCOvPFjASOyFiSaO3yFBwmdETjZgTSJVCvvDwncxRrJipsWPK-PDX1jJnMepO8-tFmdKdD86Ik9sd_7E7lEoWpNCD4w8mnbxpfVBp9If6ENIGIXxUuT17ruTeJr_scsBG5uwr4AD7Z5PoJNqO_Ky6ZGBIZi2ALHDg66TpYnCz5kgUYr0-nQQgMmflGBNCGAdMKpqkRA4tuNiglnMRMr97ESnj4MzEREla8oOO5tuZvx_HS6vqIRDniZzAFqpw5CFAlzRmIZVTyWlk1D9x_MShPzCy0f5x3h7AzC2cRUfZ0zsfhScVEkUI5HlcJo_RMbOkZZdDusdrqmk8gvNB91nbfEPQDMkRYsyXfKahiNjLRIj4SI0fGT0JC6SK69j6J5e8UYdGxptF3z_ozkL6FgvdSjxfsztjRVr3Ff71_SbSW5ZyrvXaGvEyrxVetRGCC-0tobLHg9L2eUeyW9YHAClbzIm-pWJHf1xC1uyMU3wptd6GTIfPE5EXPhD0pt0JohwIRrcWp1xRJB8HBYYGEy4YG2A_gtFEW4TNeiG0GWK-nZqg6gTOqNp6wODTQpq04O9sQyjhpVcSOQfb9R3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل ، کاتز :  تو لبنان هیچ آتش‌بسی در کار نیست و ارتش اسرائیل همچنان داره علیه حزب‌الله عملیاتش رو ادامه می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/124435" target="_blank">📅 14:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124434">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
کرملین: اگر زلنسکی دستور عقب‌نشینی نیروهای اوکراینی از مناطق روسیه را بدهد، جنگ «تا پایان روز» به پایان می‌رسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/124434" target="_blank">📅 14:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124433">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
نبیه بری رئیس پارلمان لبنان:  هیچ‌کس جز ترامپ نمی‌تواند یک آتش‌بس واقعی ایجاد کند ؛ این تنها راه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/124433" target="_blank">📅 14:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124432">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_fCd2Yx8yfBbF9m_Kap6K3fjd14IVuB5HYh6TkvxKywaQCIUATNEoOoeDMLwjTZoL52i1iNyFpNx-lyj2MOFpeHGeN8fpg5auLFPdFQh1cbgBQM4nYgN_7BZDbN7p3jHJGmisMuOxCIvZMwk4rnqZkoilSoVfn-sZfSWGCUvVxUJxB0ArsK3DDC3GOQWiDacLHHUcNvAlStGDqPSwR4MTYdqJmLJPUw1aNmLN3glGHx00DBy4UjJoladE73SrIk0msYgJ7eAf3wd6DZkKzE9RXB9eYPnDDNuUWMrnplkx1Sxg9OlM9and9kvb82WXKJjz3D4kIhQvAHbKCVJDEPtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کنایه معاون عراقچی به انصراف نتانیاهو از حمله به بیروت با تماس ترامپ / اگر تصمیم حمله با یک تماس تغییر می‌کند، چرا ماه‌ها نقض آتش‌بس ادامه یافت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124432" target="_blank">📅 14:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124431">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6YGTxNxZxuYTLHjz91YLlH9_zA7YWplvSwDU-wiYu3VKxIV5Dw4AeH7QzDRLDtcKj9ag-Qrqx9_AlkQtj8CPu1NxYsoo971-VsJPQCcmHxYp9rdoq1jZ7DxHKXZ5AYTC8f5SDnBWIN1V0TZqavYRWYPpl4t8DNUeovMyokbjaEwqRtvsiGfiD01Oein7kT6FBMlgMczJ2htPcp-wMhvd_rMZXrdsXLeGyK0zTlv0A3G5SpgOGpt51uZQ7M4rPnjKfMEki37zWHTfk7MJA0O-LBLqDvRiDJaT7pIpYw-fcAZNj8j-3QD1fAB04LEv3XQsj8u74txHT3iGuUGOSJJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جزئیات طرح رایگان شدن دائم تردد با مترو و بی آر تی در تهران؛ رای گیری به جلسه بعد شورا موکول شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124431" target="_blank">📅 14:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124430">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
واشنگتن پست: طرح بازسازی غزه با بن‌بست روبه‌رو شده است
🔴
واشنگتن پست گزارش داد برنامه بازسازی گسترده غزه که تحت عنوان «هیئت صلح» دولت ترامپ مطرح شده بود، به دلیل کمبود منابع مالی، نبود حمایت سیاسی کافی و ابهام درباره آینده اداره غزه با بن‌بست مواجه شده است.
🔴
بر اساس این گزارش، مذاکرات درباره خلع سلاح حماس همچنان بدون نتیجه مانده و ادامه عملیات نظامی اسرائیل نیز روند بازسازی را پیچیده‌تر کرده است.
🔴
واشنگتن پست می‌نویسد با وجود وعده‌ها و اعلام پروژه‌های متعدد در ماه‌های گذشته، هنوز هیچ طرح بازسازی بزرگی به مرحله اجرا نرسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/124430" target="_blank">📅 14:09 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
