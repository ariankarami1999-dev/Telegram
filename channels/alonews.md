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
<img src="https://cdn4.telesco.pe/file/fGpM3Wtb8_UP4XsjmRS75dQQ48LrT8duiDKIfJ6iDAuETtFfK3h3QaJFHWfVnkhrQTukCCFqS7LoiVPlg7maYb1SsWj-bv0WbC7Is8qx6jPmWGFegXpBtgAGXECi-0cpqBhHNxlW6QZLmgcti1SWRR0KBdrAJo216T4y4zYFuj6Sao1pnGNsrjUoiLn1Ujf1PTbdwgyqBPh0w-q-xzZMrpcAOsVCtKKKGFnCS0RoKXBLOZp4klKLpjG1FHj45XcZvX755183CDoFpJ6U9CzaqeW5tfNnEPbnZhJbS0kb_VaesrQiSH1E4h4oth1W5BL9pANlsOWzGUnzbOhkFtn3pg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 977K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 11:59:02</div>
<hr>

<div class="tg-post" id="msg-140532">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
وزارت دفاع روسیه از حمله پهپادی به یک کشتی «حامل تسلیحات» ارتش اوکراین در شرق اودسا، بزرگ‌ترین شهر ساحلی دریای سیاه خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/alonews/140532" target="_blank">📅 11:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140531">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
جهانگیر، سخنگوی قوه قضاییه: رأی مصادره تمام اموال منقول و غیرمنقول ساعدی‌نیا جهت فرجام‌خواهی به دیوان عالی کشور ارسال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/140531" target="_blank">📅 11:43 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140530">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yroy7z7WUjJ8-R2j7mxAIGeHKA6fTDfJ-IvTS1G8Sb5pOrLaROmoTK9sooccRN9u8vMEAZQmBNIwqZCJOQGOx8aBXdxpdkLI--aSWDq4_28nzKkt7btQbk2DeB7FghuMG_wb-XZuhvtFYEiQp4PVmVoIr7MM5s6UDzvwP6h3KAP5XqzYuZtnDxdZSMt8E2znEzi_WbSxsfxd3Vg6k1Z8RYQ_BQLUs1SSx-Rm5XDZIOmgO4JOZSh-3FCjTtAlLEWOPxalXPX9Rn8WyOPg50NljEInYzDKkjU-6jjpw9mt0xscC-Ako14eg6-lY6YH_4zTgjyGLTkmnSeO7e70VyovHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیمرو در رستوران‌ها یه 2میلیون رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/140530" target="_blank">📅 11:39 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140529">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
کپلر: صادرات نفت عربستان پس از اعلام محاصره یمن از بیش از ۴ میلیون بشکه در روز به کمتر از یک میلیون بشکه کاهش یافته و بارگیری نفت در ینبع نیز به صفر رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/140529" target="_blank">📅 11:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140528">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efb71292a2.mp4?token=F-i-3KSvYGjTqElMHegQRCabQAVRKATK-l9jJ6_ri3H2e7LuGoPd-A2N7xAttKvkqwj-BkiUFBEO3f9cb3Gshsf3r1w0FE0uIJaP39IGPfW7xJvTiOvkOMLimabWjUIs8W-r9e7iyKT1I2v5yO6xDC34_cSk3ruFp3t2bOG0JlhV3IYWlkhXlTFSbKp3_E0lDaiz93uo2beKzibDlovxYXEo09GzwSTl1aKohKSGHvpIQk7KIxLCqy-6JezQdRbDl2n9iNo7QBUsQI6J40Y_gQ9f_LaCBkjDPNxa1IgkG6ckXXhCogeqj_dGsPC0Y52GZSWlwj4zfTLna6BynSrm9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efb71292a2.mp4?token=F-i-3KSvYGjTqElMHegQRCabQAVRKATK-l9jJ6_ri3H2e7LuGoPd-A2N7xAttKvkqwj-BkiUFBEO3f9cb3Gshsf3r1w0FE0uIJaP39IGPfW7xJvTiOvkOMLimabWjUIs8W-r9e7iyKT1I2v5yO6xDC34_cSk3ruFp3t2bOG0JlhV3IYWlkhXlTFSbKp3_E0lDaiz93uo2beKzibDlovxYXEo09GzwSTl1aKohKSGHvpIQk7KIxLCqy-6JezQdRbDl2n9iNo7QBUsQI6J40Y_gQ9f_LaCBkjDPNxa1IgkG6ckXXhCogeqj_dGsPC0Y52GZSWlwj4zfTLna6BynSrm9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون وزارت بهداشت: حمله به لامرد با بمب های فسفری بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/140528" target="_blank">📅 11:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140527">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf6e59b058.mp4?token=tlVf6u2AOOzrrB9UWylTvU-1LRbuvhK4U7Z8N9ad4Kr15-nhr98gm59Qhv4znKR0me2VijIF5jjY5fsPtj0vFTQxiuMwWqzw76QAZe1PWCuTthkddUuvitSCYd2JknXo4IUDIheqV9Z_Bzhfc876G5L5-xDI6rG7HVDGTAuOum6LKmfhCnJDN1qOrkcPPCcAsCJuBrEBXvGF_QGoIWQOZyBWcvf6TrQcNU4xUCEHVfpQ1gXNK_ZmLnJ2KEgyf0FYNaFfH4XhjOm7QeTKmhg0PWwSJXheanKYU5Rp19wpTd5fCAwj1vmHB9FCHqwi60_WJeCNZe6KLn91gkTn9bIhvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf6e59b058.mp4?token=tlVf6u2AOOzrrB9UWylTvU-1LRbuvhK4U7Z8N9ad4Kr15-nhr98gm59Qhv4znKR0me2VijIF5jjY5fsPtj0vFTQxiuMwWqzw76QAZe1PWCuTthkddUuvitSCYd2JknXo4IUDIheqV9Z_Bzhfc876G5L5-xDI6rG7HVDGTAuOum6LKmfhCnJDN1qOrkcPPCcAsCJuBrEBXvGF_QGoIWQOZyBWcvf6TrQcNU4xUCEHVfpQ1gXNK_ZmLnJ2KEgyf0FYNaFfH4XhjOm7QeTKmhg0PWwSJXheanKYU5Rp19wpTd5fCAwj1vmHB9FCHqwi60_WJeCNZe6KLn91gkTn9bIhvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهمات سرگردان
RAM-2X
اوکراین، پدافند هوایی متحرک روسیه رو هدف گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/140527" target="_blank">📅 11:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140526">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c02b892b.mp4?token=RL_Qfo4xqb7dXCI-wT43_N6-7utxr8AUUYiFAsLTKRY-Z8RcqrQh7MVnVG5D3v72Kk02-aXCYUwdhdaLCESvvwI8M7UNrDGZJS10EuHZm8GDtP10yyASMla97PWBPGD2or88jNvKFjrgSkAbno9J4gX_Lxk3wSYBPBkGPGiO5SpRBsELX-X5Juqw-4PBcjCBSxINssBQpmInf0kSzUcWIRaXhm0oF6_yK2unsCLHrjKjlAv6AyfmCdNnukMORGBJ2UkdCuGx6gHPpzyb1xfackaT6waHAdXPkxykfg30uIfQ8CKM3aJLv1P9yU0_xBsF42iE6m31x4xT5pVc2p4Mmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c02b892b.mp4?token=RL_Qfo4xqb7dXCI-wT43_N6-7utxr8AUUYiFAsLTKRY-Z8RcqrQh7MVnVG5D3v72Kk02-aXCYUwdhdaLCESvvwI8M7UNrDGZJS10EuHZm8GDtP10yyASMla97PWBPGD2or88jNvKFjrgSkAbno9J4gX_Lxk3wSYBPBkGPGiO5SpRBsELX-X5Juqw-4PBcjCBSxINssBQpmInf0kSzUcWIRaXhm0oF6_yK2unsCLHrjKjlAv6AyfmCdNnukMORGBJ2UkdCuGx6gHPpzyb1xfackaT6waHAdXPkxykfg30uIfQ8CKM3aJLv1P9yU0_xBsF42iE6m31x4xT5pVc2p4Mmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک ارزشی: این چه وضع حجابه آقای پزشکیان؟ من هروقت بیرون میرم تحریک میشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/140526" target="_blank">📅 11:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140525">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
واکنش بانک مرکزی به ادعای ترامپ درباره تورم ایران: تورم قبل از جنگ ۴۶ درصد و در حال حاضر ۶۱ درصد است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/140525" target="_blank">📅 11:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140524">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
رویترز: اصابت یک پهپاد به مخزن پالایشگاه شهر الزاویه در لیبی باعث نشت شد و این نشت اکنون تحت کنترل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/140524" target="_blank">📅 11:09 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140523">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
الجزیره: بعید است که عمان گفت‌وگوهای خود با ایران را بدون هماهنگی با آمریکا انجام داده باشد
🔴
واشنگتن‌ از مفاد توافق احتمالی بر سر تنگه هرمز، آگاهی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/140523" target="_blank">📅 11:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140522">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
وزیر دفاع پاکستان: در ارتباط با اسرائیل، همه دولت‌های مسلمان باید متحد شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/140522" target="_blank">📅 10:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140520">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رویترز: قیمت نفت روز جمعه به شدت افزایش یافت، زیرا معامله‌گران همچنان در حال واکنش به ابهامات پیرامون تنگه هرمز و مذاکرات ایران و عمان بودند
🔴
نفت در پایان معاملات در این روز، ۸۳.۵۵ دلار شد، یعنی حدود ۵.۷ درصد صعود کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/140520" target="_blank">📅 10:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140519">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_nDiZnwFar4iVWcooDEMGC0XtDTet3SaTEjUKBOvX2F8VaGBl4bRCizUdt1IgfQ2e56XVw3CuyfsWbAQMGdyyZN_60KqL7gX78-eYr67aA7CktSjU-aj_lxSw82FEvkeX_5rs27vRmysOMN0PpXqzf5gQUDgpL_baqvCRtv7cPySBGgC79RSyDfEqKQAytrmDrmV1vy8AcGrdlocHwtB5NxeKTlPEBgFm2CCU6eRjfNSYhOGlYUAjZAeBD0XYM8ZxOhAUlvGKPdtuaUH13HosDVEPgZeBfGyNnBquy4YdpRerTMVcWELa-L0gyBMInGtydUunW0RREq2sZ6kvO0eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات ارتش اسرائیل به اطراف تپه علی الطاهر در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/140519" target="_blank">📅 10:41 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140518">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e96kk0BMI4jfwJv4e_nVJUiHJZQvTjdDJzdgdw0DPlqrdz9bXy9BwBJuYQlErbyuDXcOh-7oPK5dahEFoU3oc2RbrvvtSEElnh9-boo0a9yKpbFW_vvg8etCRwEplag9mc8coyrkJfnF4j4FUd60HxOrXZAJp49B64JtXsD7jZ6G_ZDxNHvP0wS6Mv4FR8HW6IOeRBRmbLh1ZXmg3OxxWxnh8FjeMeLLOqihhPioVStZub2r2FpcuU7MUVmJwSwmkajjQqq_MfbDw4VNrp61_PrzY4xz0D4X2XS9HpvDyG2PbJX8HtMdOB5vU2S90iUsqqpS64nUJ7k5Npxkkjn9sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: بایدن حتی یه هندیکپ ۱۰۰ هم نیست.
🔴
(یعنی حتی نمیتواند توپ را بزند)
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/140518" target="_blank">📅 10:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140517">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ساختمان‌های مرتفع و برج‌های شهر ریاض به مناسبت امضای «توافق‌ مکه» با پرچم‌های سعودی، ترکیه و پاکستان تزیین شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/140517" target="_blank">📅 10:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140516">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
بخشی از بگومگوی ناصر هادیان و فواد ایزدی درباره رای گیری در شعام درباره تفاهمنامه
🔴
اظهارات عجیب فواد ایزدی: آمریکایی‌ها تهدیدات سردار حاجی زاده را باور نکردند؛ ایران بعد از جنگ ۱۲ روزه به آن تهدیدها عمل نکرد!
🔴
ترامپ ما را مسخره می‌کرد
🔴
اعضای شورای عالی امنیت ملی روی مقاله ظریف اجماع کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/140516" target="_blank">📅 10:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140515">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزارت دفاع روسیه: ۸۳ پهپاد اوکراینی صبح امروز بر فراز چندین منطقه از جمله مسکو سرنگون شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/140515" target="_blank">📅 10:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140514">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
الجزیره: تردد کشتی‌ها در تنگه هرمز طی این هفته باز هم کاهش یافت
🔴
بر اساس داده‌های تردد دریایی، روز پنجشنبه تنها ۸ کشتی تجاری از تنگه هرمز و ۲۶ کشتی از باب‌المندب عبور کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/140514" target="_blank">📅 10:16 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140513">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
عطریانفر: به‌کارگیری به موقع دیپلماسی، تهدید‌ها را به فرصت بدل می‌سازد
🔴
بی‌تردید قدرنشناسی، فحاشی و سنگ‌اندازی نسبت به مسئولان، موجب دلسردی می‌شود
🔴
رقابت‌های سیاسی باید به گونه‌ای مدیریت شود که تصویری از ناتوانی در تصمیم‌گیری ترسیم نشود، زیرا این موضوع دشمن را به اتخاذ سیاست‌های سخت‌گیرانه‌تر تشویق می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/140513" target="_blank">📅 10:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140512">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eL4s5hIJm_0hLGB6t6nuQc5rzQYgjZYSNzw1ywixNwlrd0bhmfzQn0GE3gy9_ZBf_XREW-87GeeoBMgTS_8joMLPBxMBBVKbsQ2e96_YH3cYi3CXr68U1Xd5kLEydsmDyqaF4OcOQGqor20lTbQtWWe9OCpIZpUd3VvUmGA9dkvhN_LwjoBARTNG_btF_LQiWUtgMvSelqRpPz0c3o-3ycY9xZ2swYN9-M7jvMHJH7KVD1ZqEeA--I-1oCp_EElP2nQA43E6GmepGQvAo8UnS_k_D3rOXJs6z4N1dnUMwucsTDECMgGApctyrbsJzWc25zYntIhDN3KHkg3NcSFq1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت دفاع آمریکا، دسترسی امنیتی "فرانک کندال"، وزیر سابق نیروی هوایی، را لغو کرد و او را به افشای اطلاعات محرمانه درباره نقص‌های امنیتی هواپیمای "ایرفورس وان" که  قطر به ترامپ هدیه داده بود، متهم کرد.
🔴
کندال این اتهام را رد می‌کند و می‌گوید که به او اطلاع داده نشده است که چه اطلاعاتی را به طور مدنظر افشا کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/140512" target="_blank">📅 09:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140511">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0ofgQz8ETCd8rIcnPHtwkqj-GHxaCJlV6ICRxK43lNKntF1vF6KBuajdI7hkzv-9Wvwfax9fVz42MJxwEvEu8TAVih4CYwhYR9bNWU9zAweX6LUo3r0pzkAqAN7gofO-yafc3wfJSr-k-hfDLr5Mw4go6OS4SEPH4HnaW-AsE5A0uSc12DWhMUiqIwzL48Z1xbaaiIESPoK8rwwabDsyyeW5EKuB7tDeCdoszpWOCyghBFVWi2_UN9U4_NCXHU3suzrO8A8dZfG5p8sM7Yyms1NVeJoRWbDN0S4XrzAn1LuE2j9c0_mcJ9BMUV3cRZU98qM7-JcEbttnCeE9WwWkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زلزله ۵.۶ ریشتری آلاسکا را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/140511" target="_blank">📅 09:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140510">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ای‌بی‌سی به نقل از مقام‌های آمریکایی گزارش داد توافق موقت ایران و عمان برای بازگشایی تنگه هرمز قرار است ۶۰ روز اجرا شود؛ دوره‌ای که هم‌زمان مذاکرات برای ترتیبات بلندمدت هرمز و پرونده هسته‌ای ادامه خواهد یافت.
🔴
به گفته این منابع، جزئیات هنوز نهایی نشده است. آمریکا خواهان آزادی کامل کشتیرانی است و با هر سازوکاری که به ایران اجازه دریافت عوارض یا صدور مجوز عبور برای کشتی‌ها بدهد، مخالفت می‌کند.
🔴
پس اختلاف فقط بر سر بازگشایی هرمز نیست؛ دعوا بر سر قواعد عبور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/140510" target="_blank">📅 09:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140509">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/78924983a9.mp4?token=Py73qai4NejphXncxDpH82YyjUfDXiiTttJC9-tfOnmqvHYirlss8yimazeepD7Qncisg4JU9uZreZFRhhdQQ1MFrWI_U2CFP9gHFWHq5mj7hJmd6DvUBOsi2zm6AKNDaE5WjB80PuDoPrsAJqBsWGFRLMDTIZsAsXq91__dbJdG5VunHncbi0t4z_APCZ0atGBRI2gBRIb9HIdIvTNCx0P-zSf09Wiz4XYB0ijRqYlBTIECO1cmgrWsXEflJ1J8ZkZNvwHv2Jw9I807psUttyfIANJ6qAPdUryDusT7YmyDfAfdcpkf-Wp2WDd6Z910Dx1_C5AmfAPV4aKLmz4lKg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/78924983a9.mp4?token=Py73qai4NejphXncxDpH82YyjUfDXiiTttJC9-tfOnmqvHYirlss8yimazeepD7Qncisg4JU9uZreZFRhhdQQ1MFrWI_U2CFP9gHFWHq5mj7hJmd6DvUBOsi2zm6AKNDaE5WjB80PuDoPrsAJqBsWGFRLMDTIZsAsXq91__dbJdG5VunHncbi0t4z_APCZ0atGBRI2gBRIb9HIdIvTNCx0P-zSf09Wiz4XYB0ijRqYlBTIECO1cmgrWsXEflJ1J8ZkZNvwHv2Jw9I807psUttyfIANJ6qAPdUryDusT7YmyDfAfdcpkf-Wp2WDd6Z910Dx1_C5AmfAPV4aKLmz4lKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
ترامپ: لاولی ایسلامیک ریپابلیک آف ایران
!.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/140509" target="_blank">📅 09:09 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140508">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
اکسیوس: گفت‌وگوی ترامپ و بن سلمان در مورد ایران و تنگه هرمز
🔴
اکسیوس از گفتگوی ترامپ و بن سلمان در مورد ایران و تنگه هرمز خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/140508" target="_blank">📅 09:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140507">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
رسانه‌های عبری:  مهاجرت ثروتمندان اسرائیل طی سال‌های ۲۰۱۹ تا ۲۰۲۴ دو برابر شده و سالانه ۷۰۰ میلیون شِکِل از درآمدهای خزانه اسرائیل می‌کاهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/140507" target="_blank">📅 09:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140506">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سی‌ان‌ان: ژنرال کین درباره پیامدهای بمباران گسترده ایران به ترامپ هشدار می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/140506" target="_blank">📅 08:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140505">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kwq2Hj7mDzAlDr1wZXmZ_lsB0eql0wjnU6mPF5GCOCZgyfH-6yG7QNjNwyOPd4rsGwfmuLJDAk1jBc-ErM5Zn2xRMTl_kbjVvWZVhomdQp2KF6qNsBG_2IINPAex-nnR7Z5JPa6b3mUY3D_R9FPIeQ7W4TF6eHKZXhsUod7hFrZO74krd4rE13AYAYYhbuxSLdNR7aGQFGkU58i--FtrfPgXw36NNou6YBhdvcFsdu0P2Ug5i8cPsS_5AfSE-UH3O6phtpcHyeSqSh9znoaWZEy-oASvc3MNVHo6ZYoEueyP9rme-sQLj5I29oqJskx-jOIk51DmNZ-zM3gAD5Nn1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک کشتی تخصصی در زمینه مبارزه با آلودگی ناشی از نفت و اطفای حریق، در حال فعالیت در منطقه‌ای است که یک تانکر نفت در تنگه هرمز مورد هدف قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/alonews/140505" target="_blank">📅 08:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140504">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAXnGtWxR1b8_8cIl0yie-4zn8GLM5q4tgK1vlXeo6SgZ7Mbz_nruIGX4iV8RXSWkkkUVa5KpmqhmMKuQAvxhie8VlpnzcamhA6-E4PCApNBAL22Co7ibhat1i8oUDr9L_4L7t18_l1dDADKasYqw_T2QH4oJ0gKK-lzxV4JeA3YkQTGtdE-9lm9GiQCBjhMgOIR8HVbw1782grBYBcs9RorOmAg0d0OoNtJgKZMmf4E1TYO0vE3jV27slkL1G3qhYJpbvmD-24KfWe1Gobnx3093zCfpJxPmCj1ryOjDYQ0xicuMwT3Vww3mPXFHbu9o7TnG51vTJ2Ad4jGUnG7tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش‌های منابع عربی حاکی از حمله به جده، عربستان سعودی است و به همین علت هواپیماهای غیرنظامی از فرود در فرودگاه جده خودداری می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/140504" target="_blank">📅 08:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140503">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
حمله حسین شریعتمداری به پیمان سه‌گانه پاکستان، عربستان، ترکیه / سران این سه کشور در قتل‌عام غزه دست داشتند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/140503" target="_blank">📅 08:43 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140502">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c194ac9d25.mp4?token=kSUtLKcltGjxHhNM_tzbpTDg7WvyVnK3c5nvEBWEQg-P1kEOhi8y9tWdEr7Cuz6gnTAFL3xbnP9QbJmP46peQJoq2osw2dVaALdO_MuS50AZp2hY5_5DrXXHi6VOTfpJhhaaBb9GqdVbSxjwdIj7nc1z97XpNveJxCNprJ8_l1MyUqsi85AQ1OSdH5iBnsCsYhPfZm6PugGfhyfur2gJmThHjRx4RFWyPOZCP4T1m2OU-HxJGdFGddjhQtU7V_Ur2cUJ_IXjo1dxG6emG5MkWYKGHBTceY6fLv9pV9eIpA6UQp1geET_2XQzGBPyN8141K3WIoMiDtFPiA3gi0CCAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c194ac9d25.mp4?token=kSUtLKcltGjxHhNM_tzbpTDg7WvyVnK3c5nvEBWEQg-P1kEOhi8y9tWdEr7Cuz6gnTAFL3xbnP9QbJmP46peQJoq2osw2dVaALdO_MuS50AZp2hY5_5DrXXHi6VOTfpJhhaaBb9GqdVbSxjwdIj7nc1z97XpNveJxCNprJ8_l1MyUqsi85AQ1OSdH5iBnsCsYhPfZm6PugGfhyfur2gJmThHjRx4RFWyPOZCP4T1m2OU-HxJGdFGddjhQtU7V_Ur2cUJ_IXjo1dxG6emG5MkWYKGHBTceY6fLv9pV9eIpA6UQp1geET_2XQzGBPyN8141K3WIoMiDtFPiA3gi0CCAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
تصاویر ماهواره‌ای نشون می‌دن که یه کشتی توی تنگه هرمز داره در آتیش می‌سوزه و این موضوع تایید شده.
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/140502" target="_blank">📅 08:39 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140501">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g69BC5B0LT3ooOy0kQwJ_4c1VsIJ99Og77rclGLyqlKX3Af-H1sJNbdJx3tzbEi2CdlO5HHBtYd_aXUh0ijq-3ZSoW5ojSDpgIjTaM6iQkgFYxDeHzXB55pRO3qXhpVQVC0kKUJwS1WnJSBtQ4TDKG3TLGHmfK5qVgcbXHNYtXDQynPnzEUuTpsZy_-oh5Hk79oNN6Ym2wtKwbkcoUSYoqjBUadtNVctl5gtwRZbTPoDIoQ8LGWBooQK31_3RgIWX0uaiwlqUIK_68f_qY_B_JwcyRcsEamX5PpLLUOIR0BVggpl5rBPVB63a3xA9kUzm9RRJmUbZCE0neR62BRJpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی ان ان: ژنرال دن کین، رئیس ستاد مشترک ارتش، به طور خصوصی به مقامات ارشد دولت ترامپ روشن کرده است که ایالات متحده باید «راه فرار» از جنگ با ایران پیدا کند، زیرا معتقد است گزینه‌های نظامی موجود برای تشدید درگیری ممکن است نتیجه عکس داشته باشد.
در حالی که کین به ترامپ اطمینان داده است که ارتش ایالات متحده «قطعاً می‌تواند آن‌ها را نابود کند» اگر دستور داده شود، او همچنین بر محدودیت‌های نیروی نظامی، نگرانی‌ها درباره کاهش ذخایر مهمات ایالات متحده و خطرات یک درگیری طولانی‌مدت تأکید کرده است.
در نتیجه، مقامات به طور فزاینده‌ای درباره یافتن «راه فراری» بحث کرده‌اند که به دولت اجازه دهد تنش‌ها را کاهش دهد و در عین حال ادعای پیشرفت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/140501" target="_blank">📅 01:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140500">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
در یکی از بزرگ ترین قراداد های نظامی تاریخ خاورمیانه، ایالات متحده مجوز فروش 5250 موشک رهگیر از نوع پاتریوت و تاد به بحرین، کویت، قطر و امارات متحده عربی را صادر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/140500" target="_blank">📅 00:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140499">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8192485a22.mp4?token=WIi_u00m9IxjSwyey2NKAXCdmwJncrL8I-stTyLNHWdYiCHMO8tok3E1bk1NbXZ4iaErLGaUWIXRsK0SdOMr-lsUVCB77gmKmTJXOTOuR6NiS9oZlDTmwy3Tde2c0lsLBp2pdYUkM5Glq1oukn3k95axM0dxpEwOzbnm2dmXdysGbO-0bNN9VLFhf_7IKio5nAtSqDvvEYAnr9PqiDymPIXsfN-LnqS9D_DlMwesZw2FFMGiEuaA8DKEHIeB6phyhKcB4mAc4J-o6MycnQbo0wYPg7mYS6IYffnfCHM_CNlZ8ppbSWA8NDELXMoc4LdzEwUWWwhgQ4EqexvxBCaSzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8192485a22.mp4?token=WIi_u00m9IxjSwyey2NKAXCdmwJncrL8I-stTyLNHWdYiCHMO8tok3E1bk1NbXZ4iaErLGaUWIXRsK0SdOMr-lsUVCB77gmKmTJXOTOuR6NiS9oZlDTmwy3Tde2c0lsLBp2pdYUkM5Glq1oukn3k95axM0dxpEwOzbnm2dmXdysGbO-0bNN9VLFhf_7IKio5nAtSqDvvEYAnr9PqiDymPIXsfN-LnqS9D_DlMwesZw2FFMGiEuaA8DKEHIeB6phyhKcB4mAc4J-o6MycnQbo0wYPg7mYS6IYffnfCHM_CNlZ8ppbSWA8NDELXMoc4LdzEwUWWwhgQ4EqexvxBCaSzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ خطاب به خبرنگار‌ها:
ما یه جنگ بزرگ رو درپیش داریم و بنظرم بهانه‌ی خوبیه واسه اینکه اینجارو زودتر ترک کنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/alonews/140499" target="_blank">📅 00:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140498">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd08a7bff2.mp4?token=KMAAD6JDsySYr9lzsxrQlr1xvwLkgfZqFC1V1ElUHDCdMRzEYuYK5-7MkQndxLeYjvJ5h1rTKWoK4VfQiivlvju6gHc58jXoI_ET1WSJJrSTQrOiZi49W3hpOezoL0qRfKRO1RTdIytxGIlJl7_jQam8dSYIWQr3mA2uHNSsMC1oaS0ASccEyqzyj4zUaiZ8ily8tK-BIaagPbF7ez6dt-_PxOQcJRVc070GbYrE39goFFqU9V68U13toa4uUcR3zO62U3668RcnpKuooVAnUOplhCAmgACOaIMm6fqTULc14HiaVOyix9W7qLEFK-3Xi130wMizIs9DmvWmEfUwBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd08a7bff2.mp4?token=KMAAD6JDsySYr9lzsxrQlr1xvwLkgfZqFC1V1ElUHDCdMRzEYuYK5-7MkQndxLeYjvJ5h1rTKWoK4VfQiivlvju6gHc58jXoI_ET1WSJJrSTQrOiZi49W3hpOezoL0qRfKRO1RTdIytxGIlJl7_jQam8dSYIWQr3mA2uHNSsMC1oaS0ASccEyqzyj4zUaiZ8ily8tK-BIaagPbF7ez6dt-_PxOQcJRVc070GbYrE39goFFqU9V68U13toa4uUcR3zO62U3668RcnpKuooVAnUOplhCAmgACOaIMm6fqTULc14HiaVOyix9W7qLEFK-3Xi130wMizIs9DmvWmEfUwBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت دونالد ترامپ با هواپیمای نیروی هوایی یک از پایگاه مشترک اندروز به مقصد فرودگاه شهری موریستاون در نیوجرسی حرکت کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/140498" target="_blank">📅 00:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140497">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b422b0ac1f.mp4?token=t6hcNDN8gJzG7vgHH5S1kPmrFY2fVV2MEClmB_Y-DX4kKJh8saSc-4ew2Mtyy8N8NgAno3u2HThNPdT-V0wa1OhicRXLBtHdzxAkrEDPLDvpzFNNewiZpseh-fzZGCFJGAJrCa-6aHP6U_TmDsmFMRyzfeyK2D72UrGQqNdz6aga6rqqAQqN7n-g7A9jjrtw3siQ4o29D2gkBESQGWgXKgdKbBEh78jgmwysGnv3hJytzgkABRlf4yWtMIeufN0ufWlRYYq63JqU4jfD9odWLYC3aBDELmPRYmIzeFeOjeVQPo53ktho6SkAFbu1xox6O0loHAscz3HFornzAL9prg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b422b0ac1f.mp4?token=t6hcNDN8gJzG7vgHH5S1kPmrFY2fVV2MEClmB_Y-DX4kKJh8saSc-4ew2Mtyy8N8NgAno3u2HThNPdT-V0wa1OhicRXLBtHdzxAkrEDPLDvpzFNNewiZpseh-fzZGCFJGAJrCa-6aHP6U_TmDsmFMRyzfeyK2D72UrGQqNdz6aga6rqqAQqN7n-g7A9jjrtw3siQ4o29D2gkBESQGWgXKgdKbBEh78jgmwysGnv3hJytzgkABRlf4yWtMIeufN0ufWlRYYq63JqU4jfD9odWLYC3aBDELmPRYmIzeFeOjeVQPo53ktho6SkAFbu1xox6O0loHAscz3HFornzAL9prg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند: اوضاع مردم خوبه و تفریح و همه چی سرجاشه و همه راضین
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/140497" target="_blank">📅 00:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140496">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEyTt4ib_beIvHPquV763HvxCvs31-k6fDa1y_vPo0kTlLIVj8x_PjEjkBYfzbUXHjo7IgpDOgF7vRhKQ0b3r2wHRR-GqBBlecaxxFTuyT619l1AEXedsbXPTlD8AgyAUGarpI-GS3-KCm1ObWCmyq50axtX1yRAGdedlEEBfb9BRBXljy7e7og0y3StgoURD7wZCWtzjBVpfW_OLAZ2IlTi8PZingukcGWoet-9PJS3YxWd054Jqrd9ucxawiKvRjKiRn5kNKZA7BhKRpqlkeVL6bTN-TL8DbAxZqmsDNmUqqOCtC2t6C6VG_CQvmEg3R-MreI74Q9kdP140aVFDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام:
یک ملوان آمریکایی در مرکز اطلاعات رزمی ناوشکن یواس‌اس میسون (DDG 87) در حال گشت‌زنی در آب‌های منطقه‌ای است تا از محاصره بنادر و مناطق ساحلی ایران توسط ایالات متحده حمایت کند.
تا امروز، نیروهای سنتکام 51 کشتی تجاری را تغییر مسیر داده، 2 کشتی را از کار انداخته و 2 کشتی دیگر را توقیف کرده‌اند تا از رعایت مقررات اطمینان حاصل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/140496" target="_blank">📅 00:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140495">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAXplt8s8dTemStZ7USvdxkUwJsfIg6pSXI0_f-s-oPIFtRcMWJlgHD0bx0De6jMZMrHOeeOZxMJvzTqSndptEyJZS_JyBn2SdyD1VcuB7Q1TWDFLaxUWp1ge0ndhY-BZuLNmI3YzY6kBM9UDbz9RabZ7Wzwli2YWGBol_Df9N7qjt_mc24BErQwLWuO2GoJUiCvN1U787GBBJdCuWr7qLBtF1GXJua37xg275E12FsPDVcemVTPcyFclHfmf5FBRZzL5ce7WX9i0HBjv6M71P7k2pzdy4dpLexTIUUM36LVrxflkQoPPmOQKYoayLri774sBu0w1XWTElpWgYEdoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/alonews/140495" target="_blank">📅 00:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140494">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/140494" target="_blank">📅 00:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140493">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVVIkEFcSmriHDOpdfCCc31Y0bW9M37Cgkbn2X_-_fIrA3zLRm2Hx_yaO9bkDsEocXfqnNv_QZ7JkLc6_YnDIu7HM5K2VdOuyvIAc074G1B1B0wgYornCLYB1L9IeEES2zSX1feiAX3Z3JWQdr0WZhnbp8Qwq3SHgmkEqareUHt9xMqohLeYs-lEH887H5i2BofUSOJzqwzQQEbla0YJNWOAH9bbkZkDXji2n-UL3dbH4ofVuCVAGNIb5BQZaU9NaJc_IV41FxLYi_dgN_sz6V4-rff37mwTL1tLbnaBYBi5VTyKILpJPoO6khBiGUxiMzxXYvS8HIsTl9_sB86YlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش تعداد سوخت‌رسان‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/alonews/140493" target="_blank">📅 23:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140492">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXCZEN8NNBPAUVoglpI90drsmydygkLwmX_TAxShnsABdIysKpGbuN5d-nvzmGfuQCMns7n1HMOBBCkXcFPFlqqNHz13kK_3fGk_j8Ynrs-8aGSVf526CQMfdIwsko1NV-lCwZ8FoMs2G1uaAaCHyLgfFMSFFl2zY5zWZJj1SPHf82QxB6i_lMN76KAfdAN8FzPjcfdQQlmWDjteiNwdES6aJQWVqbZ0iZmz57FEOh7e2FkJtV0DT65Sxc1oEJ04iznaPKnPOIFVhc5FsmmyZAKPAYyxkZx31YL9VCgMEFPVfFU7anSK1PGC4BweALVU8saKjhQc-MWxKZnOTk0J2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همزمان با برخاستن هواپیمای هشدار دهنده و کنترل زودهنگام هوابرد E-3G بین کویت و بحرین، چندین هواپیمای سوخت‌گیری از پایگاه‌های ایالات متحده برخاستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/140492" target="_blank">📅 23:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140491">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
سازمان ملل: منتظر نتایج مذاکرات درباره تنگه هرمز هستیم
🔴
معاون سخنگوی سازمان ملل متحد اعلام کرد که این نهاد بین المللی در انتظار نتایج مذاکرات میان ایران و عمان درباره تنگه هرمز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/140491" target="_blank">📅 23:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140490">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHHeZWEAeBTpDkfusPrrb6qCDG7ZzLXEvJvS8plX_PAxPJ3sr1UgEQZXu3dRHulGFW5BaMgkdui2soo-OkGxOpdhRAXTdOI5VbJwvYXkM9UR3xx_iJVEkoHw3WCACdE3q6LC6aNVoXst-oMtcJnepEHOuh577BkZaf02HtEcgnoRFn1L3wjzaUQ8CGKeqj3knLawtTMezHX6v1myux9BHboL_8sKUptGKfPw3SqHXV9AEV0WdW4vOPDyiXqBWr6cB4CbjeiJVnRaE0bajGy2TaUgTPIpEFaImQHsNequHJqERBBvIIhXNbEP6YQGbfZaCg_mxXEGD_OIJXUlJHs4BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت هوایی قابل توجه آمریکا بر فراز تنگه هرمز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/140490" target="_blank">📅 23:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140489">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا: تحریم‌هایی علیه پلتفرم‌های خرید و فروش رمزارزها که از سپاه پاسداران پشتیبانی مالی می‌کنند، اعمال شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/140489" target="_blank">📅 23:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140488">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOLKSxAk-va0W6-oprfYHiZphHnz9_xC_F4zSw9vKfPtDm9Kpf6K_RM_YkdTC9kzHM8JzMcK1tpvvO2dBvOZ0jLdZzN_8bwYEsZQ4YSR1z0Ao0CvKrbHPo0eXfyKuzl94SSj68evSZRhqZIk43FBuV_WTKc9O7WMI6U8-t3HD5OxyL_OvshwjSZgZzIQsNMODcIr4tpkmAEsSYJ3SFYp4rRN3W_MsX-SdNsHoskQGiU2H-bU1qo-LTHP1TLcsevtvpo9jLKKFATGF-wLtpRSbnM4Uhov6Di3m_ptdmZJKciOdh8FBcf6M7T_yfJTBGUxp_pKUm1FGrTev0i9kuFO9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دقایقی قبل مختار توسط صهیونیست‌ها کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/140488" target="_blank">📅 23:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140487">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
آبان تتر هم به لیست صرافی های تحریم شده امریکا اضافه شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/140487" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140486">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
دستگاه اطلاعاتی آمریکا درباره ماجرای فرودگاه لایپزیش در آلمان
سی‌ان‌ان: دستگاه اطلاعاتی آمریکا مدعی شد که پهپاد حامل مواد منفجره که چهارشنبه شب در فرودگاه لایپزیش در آلمان کشف شد، متعلق به سرویس‌های اطلاعاتی روسیه بوده است.
🔴
بنابر این ادعا، این پهپاد حامل مواد منفجره بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/140486" target="_blank">📅 23:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140485">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/78924983a9.mp4?token=sLXRBiUeXmwvHHNLVWnVg-VkywXNKdoOOE8zXQBfSTtgMR89eRLLOo4EPskXXiJSroMuS5C2ez3QgnHJmbT2YI4tNOvvCowk_Hz4ufXznSQKUFzQ-nT9D7kR2NmGDCdpAq6r95esK17KCMZGgdhmCyufHGjORofnraIK_bT3j45L3lyAXbb62DBp3cnzrDCVhwk9Y_uRnDukz6qHQrlk7Jg5HR-etGma7Bb7_TALkr6bOw5A7RHru6rLWFA6rcHLqH5d56jOhMW5AhlIIofbFKSUKHLZ736KtS_cpv5BXLPU22S-wm7lhkGMOYHjyCuQt4E7KPZWwECMhS67jhft9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/78924983a9.mp4?token=sLXRBiUeXmwvHHNLVWnVg-VkywXNKdoOOE8zXQBfSTtgMR89eRLLOo4EPskXXiJSroMuS5C2ez3QgnHJmbT2YI4tNOvvCowk_Hz4ufXznSQKUFzQ-nT9D7kR2NmGDCdpAq6r95esK17KCMZGgdhmCyufHGjORofnraIK_bT3j45L3lyAXbb62DBp3cnzrDCVhwk9Y_uRnDukz6qHQrlk7Jg5HR-etGma7Bb7_TALkr6bOw5A7RHru6rLWFA6rcHLqH5d56jOhMW5AhlIIofbFKSUKHLZ736KtS_cpv5BXLPU22S-wm7lhkGMOYHjyCuQt4E7KPZWwECMhS67jhft9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: لاولی ایسلامیک ریپابلیک آف ایران
🔴
جمهوری اسلامی ایران دوست داشتنی
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/140485" target="_blank">📅 23:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140484">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/889f666c39.mp4?token=o7fuNb7ZU9jsW9wX8DWCUT4e4xE1nXtvMFNZkg9Wzs3O80H48jnnBdZkC_z1427oMUDYN1NfpeG5DLrwr-7c05j6aXi9GlVwaqs9L_Mvcx3lLNhQjRM8ohKkEy64DBROeDokRRrH2SDUmYeBsRpiDPK1rS3bBGx6aLfCMouo-e49LtPfoPTh5MD9nGLbtmfx0JBY5-juCXDnw77nBNwWZSjC66rMYWHGJ2AkkPi8KJxpa-ZhUOKcSa7aIUHV0eaaSq7h0X40lM40wDeYehetBGOwj6z-Vj8EkHLZvZV20-nW_7hf2D6IFPpGGwEOP_MH_CQERxTNT0IFHKaRLFx63A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/889f666c39.mp4?token=o7fuNb7ZU9jsW9wX8DWCUT4e4xE1nXtvMFNZkg9Wzs3O80H48jnnBdZkC_z1427oMUDYN1NfpeG5DLrwr-7c05j6aXi9GlVwaqs9L_Mvcx3lLNhQjRM8ohKkEy64DBROeDokRRrH2SDUmYeBsRpiDPK1rS3bBGx6aLfCMouo-e49LtPfoPTh5MD9nGLbtmfx0JBY5-juCXDnw77nBNwWZSjC66rMYWHGJ2AkkPi8KJxpa-ZhUOKcSa7aIUHV0eaaSq7h0X40lM40wDeYehetBGOwj6z-Vj8EkHLZvZV20-nW_7hf2D6IFPpGGwEOP_MH_CQERxTNT0IFHKaRLFx63A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
برگزاری نماز جماعت وسط خیابونای لندن
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/140484" target="_blank">📅 23:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140483">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
خرازی: باید ابتدا اروپا رو فتح کنیم بعد از راه دریا به آمریکا بریم و اونجا رو اسلامی کنیم
🔴
همزمان میتوتیم به شرق آسیا هم لشکرکشی کنیم
🔴
یک لشکر هم میتونیم به استرالیا روانه کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/140483" target="_blank">📅 23:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140482">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1qaZneA-HFhFicbOONDyeq8EIdckkvjwGNywaISv9dSOuYSIHDGS0AqoNc0fhj-ppFOO5S1MdKOeNcIZaaNhJ6FWy8UtOsHYWQXHQ8HeXRC6N-AfGmUdd1whW72fLJrsEB4yxTNQ4FaIRSHfphf0yrBd2lxWzjmF-4axYAEe-itrzpiZ09udHUEzOyqO1uAuottYxtdyJ9Br9vCwXzA6Nm4r1CTzGbRXlHo97eTCAdRBxo2zT0WvHETqUrgNXvLIG1b3eixz7-yaq2_aylfFhLzCaR2aSHvBEy7jcvH6TV0Q3LR7qbLmSkaHULnEejY2KATBIWWpPpOVe2gSrh1KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خرازی: باید ابتدا اروپا رو فتح کنیم بعد از راه دریا به آمریکا بریم و اونجا رو اسلامی کنیم
🔴
همزمان میتوتیم به شرق آسیا هم لشکرکشی کنیم
🔴
یک لشکر هم میتونیم به استرالیا روانه کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/140482" target="_blank">📅 23:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140481">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ولودیمیر زلنسکی رئیس‌جمهور اوکراین در صربستان با وویچ، رئیس‌جمهور صربستان، دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/140481" target="_blank">📅 23:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140480">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca22d0550c.mp4?token=duFwZupb_AZsiagLGRIz1oJXSNhKJSM6BHfex0QGw6mIRsmdVwXE1yvd2ED1vJNpdXNF22SgLjIJDbZbITdP9ZtZzQiy7Gwuakz4_-lCTpAnjx40kaTILuINXpfko4mNHA1GeGEHFQU5RnLgtj6IDdgYsX0RS6ivXWc-SkEVSDHJre_h87SaC_li8KaGUlmKdNxb8bfStaZWOTXPzopkzpwTGZHiwIrKwlKH0zxovfk0_SMHrvApIXhuZkKtme33V3wo0ITQIxh2mOxcgMbHPkNOCFk9_m-LEs52plWlo7M-sIgOrf6ECG62LiKohjKHtSfDkIfBnoeJrVLLs250iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca22d0550c.mp4?token=duFwZupb_AZsiagLGRIz1oJXSNhKJSM6BHfex0QGw6mIRsmdVwXE1yvd2ED1vJNpdXNF22SgLjIJDbZbITdP9ZtZzQiy7Gwuakz4_-lCTpAnjx40kaTILuINXpfko4mNHA1GeGEHFQU5RnLgtj6IDdgYsX0RS6ivXWc-SkEVSDHJre_h87SaC_li8KaGUlmKdNxb8bfStaZWOTXPzopkzpwTGZHiwIrKwlKH0zxovfk0_SMHrvApIXhuZkKtme33V3wo0ITQIxh2mOxcgMbHPkNOCFk9_m-LEs52plWlo7M-sIgOrf6ECG62LiKohjKHtSfDkIfBnoeJrVLLs250iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
ما این‌قدر آدم داریم که من کل روز اینجا می‌مانم. اگر می‌توانید سریع بروید، ممنون می‌شوم چون ما یک جنگ برای پیگیری داریم، باشه؟ این بهانه من برای کمی زودتر از اینجا خارج شدن است.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/140480" target="_blank">📅 23:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140479">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6987dc0f6.mp4?token=ESWuNF1SpTRgDBa2qpvl7w4NreKIaXYR4njJE6GxYLqzMIpWR8pW7hMbvx3o21b6akHQfdiZk4-1rXzgTazLkwqY2rUh_pFdMR-oNBnk33X1QmVpqF-A_8GYdz1Z_XXzqgDL468WI4trCe6PgrD5cnwTAXKm_L9k0smQywzUGpllyz8ZtKk0jz2sJYfJmkPTO4-Xx0HX-i4il8czrApH8VcOZ1c5ANhu1H1FWnaD1jABWwxR4Lmow1PYE8GMxT9Ey68EyunKtJagBo0i3zp4kMBQQHadgwgSRG_B2oZvOUuGqerugJiZ3uYrisvP5ecjfWWilLxSvnHpddOpFlb2jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6987dc0f6.mp4?token=ESWuNF1SpTRgDBa2qpvl7w4NreKIaXYR4njJE6GxYLqzMIpWR8pW7hMbvx3o21b6akHQfdiZk4-1rXzgTazLkwqY2rUh_pFdMR-oNBnk33X1QmVpqF-A_8GYdz1Z_XXzqgDL468WI4trCe6PgrD5cnwTAXKm_L9k0smQywzUGpllyz8ZtKk0jz2sJYfJmkPTO4-Xx0HX-i4il8czrApH8VcOZ1c5ANhu1H1FWnaD1jABWwxR4Lmow1PYE8GMxT9Ey68EyunKtJagBo0i3zp4kMBQQHadgwgSRG_B2oZvOUuGqerugJiZ3uYrisvP5ecjfWWilLxSvnHpddOpFlb2jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
ما مشکلی با اینتل داشتیم. آن‌ها ۱۰ درصد از شرکت را به ما دادند. از زمانی که شرکت را در اختیار داشتیم، سهام آن چندین و چند برابر رشد کرده است. ما ۸۲ میلیارد دلار سود کردیم. آیا من بابت این موفقیت اعتباری دریافت می‌کنم؟ خیر.
🔴
به هر حال، این برای کشور است، نه برای من.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/140479" target="_blank">📅 23:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140478">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ: می خواهید باور کنید یا نکنید، اما من یک طرفدار محیط زیست هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/140478" target="_blank">📅 23:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140477">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b30c2de122.mp4?token=tASkx6JdCfx2D2YnfWgX-g6Ysc4gjNk4UNFT3Uz5UXT_-c4L1gHS2tEbbKqedgtgaWFYKzLO_eIzGbkAfbu4yYmiFlOmWtdn0MnrlM-GxauITu2YpP3tTuTyBZdTJs9fFQFzxI_1C9eOuI4ICrwyw8pMBVFVgS44ue2Lm7-m4g1yFc_bcApVJhcEAuM3--NnUS7PbkqxyRbIM3ZPs10Sr3fFsHhizA_KNTn1NU7FdJXlyw1H6mCEdwrtrwCJqphckCdrr7f6txUVIfGxHxDRT4OzKEOnMaanGrKCA7qpCAcudLvCRb37MscJYC7GmHSzQIILvtwjV-3QKVVKqJffsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b30c2de122.mp4?token=tASkx6JdCfx2D2YnfWgX-g6Ysc4gjNk4UNFT3Uz5UXT_-c4L1gHS2tEbbKqedgtgaWFYKzLO_eIzGbkAfbu4yYmiFlOmWtdn0MnrlM-GxauITu2YpP3tTuTyBZdTJs9fFQFzxI_1C9eOuI4ICrwyw8pMBVFVgS44ue2Lm7-m4g1yFc_bcApVJhcEAuM3--NnUS7PbkqxyRbIM3ZPs10Sr3fFsHhizA_KNTn1NU7FdJXlyw1H6mCEdwrtrwCJqphckCdrr7f6txUVIfGxHxDRT4OzKEOnMaanGrKCA7qpCAcudLvCRb37MscJYC7GmHSzQIILvtwjV-3QKVVKqJffsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در ایتا از مجتبی خامنه‌ای رونمایی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/140477" target="_blank">📅 22:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140476">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
پزشکیان : من نه تنها از شهادت نمی‌ترسم، بلکه اون برای من یک پیروزی بزرگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/140476" target="_blank">📅 22:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140475">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
آمریکا در اقدامی مبتنی بر اتمام ذخایر و ظرفیت تولید موشک های رهگیر، مجوز فروش سریع حدود ۵۰۰۰ هزار رهگیر پدافندی را به کشور های عربی صادر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/140475" target="_blank">📅 22:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140474">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
پزشکیان: از قالیباف خواهش کردیم که رئیس تیم مذاکره‌کننده شود/ آقای عراقچی علیرغم توهین‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌ها، شبانه‌روز کار می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/140474" target="_blank">📅 22:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140473">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
مقام آمریکایی به رویترز: به محض اعلام توافقی برای ازسرگیری بدون مانع کشتیرانی تجاری، محاصره بنادر ایران را لغو خواهیم کرد
🔴
مذاکرات بین عمان و ایران درباره تنگه هرمز پیشرفت داشته است و انتظار توافق زودی را داریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/140473" target="_blank">📅 22:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140472">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
پزشکیان: برای اینکه بتوانیم بمانیم، باید بدانیم چه می‌کنیم؛ چه زمانی می‌خواهیم بجنگیم، چه زمانی صلح کنیم و چه زمانی هر طرف کار خودش را انجام دهد؛ نه جنگ باشد و نه صلح.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/140472" target="_blank">📅 22:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140471">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
پزشکیان: ما یک بدن و یک قدرت واحد هستیم و تکه‌تکه نیستیم. کسانی که می‌خواهند بخش‌های مختلف را از یکدیگر جدا کنند، به‌دنبال ایجاد تفرقه و شکاف در جامعه‌اند.
🔴
بر همه کسانی که در این کشور زندگی می‌کنند، یک مجموعه مقررات، قوانین و یک رهبری حاکم است؛ نه اینکه هر گروهی برای خودش خانی تشکیل دهد. بااین‌حال، گاهی عده‌ای نمی‌خواهند این واقعیت را بپذیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/140471" target="_blank">📅 22:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140470">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfxH0LxbEWrUaJCHbSbwFSAlxt3Ic2V2TwTV1ho1l_Zto7AeUy2Jqri0Wvc9bzKANOQIYVKqTWQR_kJ3cCme6aViCF45xTtWv9V-uOp8F56iFGNPWLq5ozGxq2dhAA2tO6TIWlXqxTBpM8Y1zAMjiTl2nmlxqYsXl6vyk174a63oBmjEZAOeACjUK29LLEXFOIq6aMF4lm3hXXAnexICMSqh6EVnIDb_fIKh6wdRP8s2iTrFsfUr_L_2MOygWTQoC-h1GNBfNQQhflLtsdfU1LEAkMkgWcL8FFDtkbr4y7_grD3Z-1B_tOrNvnGZ4mSBakqj6rc_X934LMYSTOURog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: ایران آغازگر جنگ نبود و همراهی مردم، محاسبات دشمن برای فروپاشی کشور را برهم زد.
🔴
امروز ایران با قدرت و انسجام بیشتری مسیر خود را ادامه می‌دهد. دشمن روی فروپاشی ایران حساب کرده بود، اما ناکام ماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/140470" target="_blank">📅 22:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140469">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
پزشکیان: این اروپایی‌ها بودند که موضوع اسنپ‌بک را پیش بردند و این مسئله در ابتدا به ترامپ ارتباطی نداشت.
🔴
ما با آن‌ها به توافق رسیدیم، اما ظاهراً باید از طرف دیگری اجازه می‌گرفتند و در نهایت نپذیرفتند.
🔴
این نشان می‌دهد حتی اروپایی‌ها نیز برای تصمیم‌گیری اختیار کامل ندارند؛ چون اگر اختیار داشتند، ما با آقای مکرون تفاهم کرده بودیم و میان توقعات آن‌ها و خواسته‌های ما هماهنگی به وجود آمده بود
🔴
مشکل اینجاست که آمریکا از خاک کشورهای منطقه به ما حمله کرده و پایگاه‌ها و مراکز ما را هدف قرار داده است.
🔴
سؤال این است مدرسه میناب را از کجا زدند؟ از همان کشورهای مسلمان و دوست ما.  چرا آنها باید اجازه بدهند بیایند و ما را بزنند؟ ما نمی‌خواهیم آن کشورها را هدف قرار دهیم؛ جایی را می‌زنیم که از همان‌جا به ما حمله می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/140469" target="_blank">📅 22:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140468">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
پزشکیان : با امر و نهی نمیشه جامعه رو به درستی اداره کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/140468" target="_blank">📅 22:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140467">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca37ce2571.mp4?token=lNtSn6OQV9pXArXeyVYOFfFdauV89rE4eha-CrTKiwc9We1bYdT3f_K4ND1NYI3kUlNDqbKC616ofRdK7OVPpKvDY9_GXTevUGcXearpzheXj5hwtDod3k-X3LaUymWfd3m3ey_Mnm4AXq0IsRZC6Oh7Ea-cvsAWbkNQ3oWFRUvQ9TMzsLdzFbtj_BgYNPLyLkTcWUAlDnOvsewD_LkL9h6ihF6uDPGx4gqL6Y0uKvgnvRolwFksGNraq7ZZBqgFIJzZf6nU1mFHK0fBA7uiQviRvediH8HafpZElZ7VmgQGax6Vab1UYVQE71ymPjKa1W7nmOWo2pMtZjTBYfIrzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca37ce2571.mp4?token=lNtSn6OQV9pXArXeyVYOFfFdauV89rE4eha-CrTKiwc9We1bYdT3f_K4ND1NYI3kUlNDqbKC616ofRdK7OVPpKvDY9_GXTevUGcXearpzheXj5hwtDod3k-X3LaUymWfd3m3ey_Mnm4AXq0IsRZC6Oh7Ea-cvsAWbkNQ3oWFRUvQ9TMzsLdzFbtj_BgYNPLyLkTcWUAlDnOvsewD_LkL9h6ihF6uDPGx4gqL6Y0uKvgnvRolwFksGNraq7ZZBqgFIJzZf6nU1mFHK0fBA7uiQviRvediH8HafpZElZ7VmgQGax6Vab1UYVQE71ymPjKa1W7nmOWo2pMtZjTBYfIrzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جیغ جیغ کردن یه زن چادری فضول توی ایستگاه مترو بخاطر پوشش اختیاری خانم ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/140467" target="_blank">📅 22:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140466">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
پزشکیان: ما با کشورهای مسلمان برادریم؛ برای چه باید با آن‌ها بجنگیم؟ من واقعاً نمی‌فهمم. نه‌تنها با کشورهای مسلمان درگیر می‌شویم، بلکه در داخل کشور خودمان نیز با یکدیگر می‌جنگیم و همدیگر را قبول نداریم.
🔴
خب، تو از من بهتری؛ پاداشت را خدا می‌دهد. چرا بر من منت می‌گذاری؟ چرا برای من قیافه می‌گیری و به من امر و نهی می‌کنی؟ چه کسی گفته است که تو باید به من امر و نهی کنی؟ تو خوبی، الحمدلله؛ به من هم خوبی کن، اما بدون منت، همان‌گونه که قرآن می‌فرماید؛ برای خدا، نه اینکه بیایی به دیگران امر و نهی کنی که باید این کار را انجام دهید یا آن کار را نکنید. این رفتار موجب فرار مردم از دین و باور می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/140466" target="_blank">📅 22:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140465">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
نبویان، نماینده مجلس در مورد توافق مکه: همانطور که پایگاه های آمریکا نتوانستند عربستان را نجات دهد، سعودی ها باید بدانند آویزان شدن به نوکران آمریکا هم شما را نجات نخواهد داد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/140465" target="_blank">📅 22:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140464">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
پزشکیان: چون نگاه‌های ما بسته شده و تصور کرده‌ایم کسی که ما او را مذهبی می‌دانیم، خودی است و دیگری غیرمذهبی و غیرخودی، نتوانسته‌ایم همه را جذب کنیم
🔴
در رابطه با همسایگان، بسیاری از مشکلاتمان را حل کرده‌ایم و روابط بسیار بهتر شده است.
🔴
اکنون، با جنگی که شکل گرفته، اسرائیل و آمریکا تلاش می‌کنند کشورهای خلیج فارس را علیه ما متحد کنند و ما نیز در تلاش هستیم اجازه ندهیم این اتفاق رخ دهد.
🔴
البته در داخل کشور نیز چالش‌هایی داریم؛ چون همچنان نگاه‌های متفاوتی وجود دارد و طبیعتاً آمریکا و اسرائیل از این وضعیت سوءاستفاده می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/140464" target="_blank">📅 22:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140463">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
روزنامه عبری یدیعوت آحرونوت: فرمانده منطقه شمال به حزب الله دستور داد پرتاب یک پهپاد انفجاری به سمت نیروهای اسرائیلی را در 24 ساعت گذشته پنهان کند و جزئیات بیشتری از فعالیت این نیروها منتشر نکند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/140463" target="_blank">📅 22:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140462">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
رمضان‌زاده، سخنگوی دولت اصلاحات: باید جمهوری اسلامی خودش را به پیمان‌نامه دفاعی «مکه» الحاق کند تا اولین پیمان‌نامه بدون حضور اسرائیل امضا شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/140462" target="_blank">📅 22:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140461">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2yyHxPRVYuRJcLd5LeKM7cmRI_obWiInGmTRPmwiTWpqHCgCXIIc1iG_tKCUuOe9SheShsK7enQcHTPZi67-VJPhOA0ifIFvRa_P810wx1gBFcguwwvczDO3Ng9i45WWgS4y251I1hxknPXTEQ9DMKG_rGkVh70h3Fw0SaEA6_EncyNhwFaT14a2A_CtORlTGsQE-jiHKIM7-t0u1SVnbJNXfh-vJLZF82crqBHJw8x9x4JuNzewVacz5Cp3QltiziN5mgCRfeGZ-je4KZjKlcChc1ROenobbTBqQiOoF7Buas97ugE8_LsdD38RoARMgkidvjVB_4nvY_sEgH64Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تتر وارد کانال ۱۸۶ هزار تومان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/140461" target="_blank">📅 21:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140460">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBlRbu5xeKo7wdflnA66IDx-3uFAUPxupcgTdWaPvkKJnf55VCe8aaT4oOtw9EkDV7QyWOXasbNymHCODlkZQsf8flmBZ16smnHcRbJKGBT2cOC9Q6uXbmj-9GONobGY4-92eojeEtllx1xFKF8p5ziBe7HoOnIWT7-L_t3Zir2BCJmKxTZZ7AbT2n11mu42MFzobWThi523ityaYs0OWL7X38AkawHPAhkKt-xoWC3nMnp-mqx463Jd2k2QenObpGDXvyLJ2Fo4s4N0IaRb5goXQk0TPe4kyyRRofQvDhBkgmpIcqVPK2QDu3aQH5Glfjk3rexL6edbl0ylPnscgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی
:
نیروهای مسلح قدرتمند ایران آمادگی، توانایی و قدرت خود را در برابر گران‌ترین ارتش جهان به رخ کشیدند.
🔴
وقتی مسلمانان متحد شوند، می‌توانیم با هر چالش و تهدیدی از سوی بیگانگان کینه‌توز، رویدَررو مقابله کنیم.
🔴
زمان آن فرا رسیده که تنها به خودمان متکی باشیم و برادری واقعی را در آغوش بگیریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/140460" target="_blank">📅 21:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140459">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
عربستان سعودی در طول ۳۸ روز اول درگیری، حدود ۸۶ درصد از ۲۸۰۰ موشک رهگیر PAC-3 خود را مصرف کرد و در ماه آوریل، تنها ۴۰۰ موشک باقی مانده بود.
🔴
ایالات متحده آمریکا نیز بین فوریه و جولای، حدود ۶۵ درصد از موشک‌های رهگیر پاتریوت خود را مصرف کرد و تعداد آن‌ها به کمتر از ۸۵۰ رسید، در حالی که قبل از جنگ با ایران، ۲۳۳۰ موشک رهگیر در اختیار داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/140459" target="_blank">📅 21:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140458">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
المنار: بمباران توپخانه اسرائیل شهر المنصوری در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/140458" target="_blank">📅 21:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140457">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
سازندگی : رئیس‌جمهور با استعفای "محمدباقر ذوالقدر" از دبیری شورای ‌عالی امنیت ملی موافقت نکرده است و به او گفته که کماکان به مأموریت محول‌شده با قوت و قدرت ادامه دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/140457" target="_blank">📅 21:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140456">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEjz0j8vkcOvpEK8IM9fulzaTKwVuDNW1mCImWpa4YFg_ua9bvrexdIbPKKjoJU-aUGlPG5dFsDvfBEMneFj7InVE_ryAFmjShhOuto07v0LWbEdU_MDlb64SfwI-QAAzmhX8Yxovz9rtMsRmuKFjWfxDdxl_aCHaPiAkVkscyOQlA3lBmGwBravXRcnrfeG2sMXgPR9sDuUVxKwlmNhJkzDiCFpC00SxdMbdKBoiBjRsJ5wt2h80fQFgwzA9kHNYM0L7mtiNPNj6Lz-JTlz-lQXIFQFjyvgJc_FTncgJfWgB5T1hH9WYbLiyTjr_I89Fed_3lONSW8qVFLAmWwOLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: مذاکره‌کنندگان ایرانی منتظر تایید نهایی شعام در مورد توافق با عمان و آمریکا هستند.
‏
🔴
«انتظار داریم این تایید به زودی انجام شود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/140456" target="_blank">📅 21:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140455">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
رسانه‌های عراق اعلام کردند که رئیس سازمان اطلاعات عربستان با علی فالح الزیدی نخست وزیر عراق دیدار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/140455" target="_blank">📅 21:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140454">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سنای آمريكا لايحه تحريم‌های گسترده انرژی روسيه را با ۸۶ رای  برابر ۱۱ رای تصويب كرد و آن را به مجلس نمايندگان فرستاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/140454" target="_blank">📅 21:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140453">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBJSKBT2kjvrcamFhKE6fWY7o2W5_D91I-NT2V_uqAvhgIHP9anBp9iyaBEkGwAksLa1wSZ3jKSU5qiq83vEfnRgmNKN5WYSz6fv5K1dZXAaik7VL8WdQhrCvynENv_t4zDck8dNxY8dIO-B9-H_qPkGxWJk_5YAWbhP509Zf5dUyuxrRE2ny5EE4S-w9Apv0rG_JwID0oGzMj2fQZTDo__Yc6fiTI3582MAfF33X0JGNawO0OxyPueaN-d4Xz3BOVkNOS0O4hGc5gd3LqWlwEyBh9stPoHgU_gGpSCCF-wYJRaS44BiMPU-XTEWNxJOqhNhGpNiD9bUTOc8_GEqIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: پرونده «مرکز نظامی» واشنگتن را به دیوان عالی آمریکا می‌بریم
🔴
دونالد ترامپ اعلام کرد دو قاضی دادگاه تجدیدنظر فدرال که در دوره‌های باراک اوباما و جو بایدن منصوب شده‌اند، علیه ایجاد آنچه او «مرکز نظامی ضروری برای امنیت ملی واشنگتن و آمریکا» خواند، رأی داده‌اند.
ترامپ این حکم را «ناعادلانه» توصیف کرد و گفت دولتش فوراً به دیوان عالی ایالات متحده اعتراض خواهد کرد تا این تصمیم به‌طور کامل لغو شود. توصیف این مرکز به‌عنوان ضرورتی برای امنیت ملی و همچنین «ناعادلانه» بودن رأی دادگاه، موضع شخصی ترامپ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/140453" target="_blank">📅 21:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140452">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
یان برمر، تحلیلگر امریکایی: «توافق‌نامه دفاع مشترک مکه» مسیری کاملاً متفاوت با پروژه توافق‌های ابراهیم در خاورمیانه را نشان می‌دهد
🔴
یان برمر، تحلیلگر امریکایی نوشت: عربستان سعودی، ترکیه و پاکستان با تشکیل یک پیمان دفاعی، که عملاً می‌توان آن را هسته مرکزی یک ائتلاف اسلامی دانست، در حال پاسخ به جنگ آمریکا و ایران و این برداشت هستند که دیگر نمی‌توان برای تأمین امنیت منطقه به ایالات متحده تکیه کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/140452" target="_blank">📅 20:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140451">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
بقائی در واکنش به سخنان ترامپ: پیش از آنکه کسی بتواند ادعای «غنائم جنگی» کند، ابتدا باید در جنگ پیروز شده باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/140451" target="_blank">📅 20:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140450">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
جنبش انصارالله اعلام کرد که یک حمله موشکی بالستیک و با استفاده از پهپادها علیه اردوگاه «صحن‌الجین» متعلق به نیروهای مسلح یمن وابسته به شورای انتقالی جنوب (PLC)، در شمال شرقی شهر مأرب، در یمن، انجام داده است.
🔴
این حمله به طور خاص به نیروهای یمنی و " مزدوران" (احتمالاً نیروهای سعودی) و همچنین انبارهای، خودروها و تجهیزات نظامی هدف قرار داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/140450" target="_blank">📅 20:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140449">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27c2dba3c0.mp4?token=sWi5Tmwus1fXE96mwF-KvUvj94NwvHHJjD1fa9XD9bIMYlxL1VXxTY-22h_k89_nYo1JINlSWKXOem727OxWRzgoOgtuzOybNZhMaO6HueJgkqrAXaTAAY8yGRuNZ39tnjbE4XlRZCOboaNos9TAoVdC8mVn-J6j3Fa6-IpIxZoln3kO9y-9lhs2eVukyQL5vde6jEy4xCh8Hz8D_LLzqG57HPI4FMuvBwYgF2I5--QrEL8l7OTElzCa1pf4Bq4dK55_CS-q40_UKj19ke_Ea3iN4z7z5lyOmBN7V4vJJq2ZbBaAPRARstR0old1xSeIrDQw9elbK-t5ljYygdw7hodmSMvCKfVVlb3J4gwXAU2dpOcy_IFyq0DT-7VCW_RFJaeOHyyzi4eKEbGninCfjHobjpjraaUnqx7HtcSwwY0afk5H3luuwmqtHQk83TesRG914ONS0MVRViPjg5MQz3stbQmNTexDMrzTYALFwsQurh8AVDFxB0_E76xEgBqIoC0NfpOOlhPbgJl8D296hPdh5Y7TZLjSVy40ypoy7-PXiYZvQlla8dgiNNvV8MGPMvnHyTBBEwvoMV9lIcFTWLBAdvchJ4v3dRTd-AKGfygW8x2TdtrU6HYPRjZGz5Hdc5_410e-5t2y4z5yxVa86vs2yOJQ_XvwUNMBq7W7NTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27c2dba3c0.mp4?token=sWi5Tmwus1fXE96mwF-KvUvj94NwvHHJjD1fa9XD9bIMYlxL1VXxTY-22h_k89_nYo1JINlSWKXOem727OxWRzgoOgtuzOybNZhMaO6HueJgkqrAXaTAAY8yGRuNZ39tnjbE4XlRZCOboaNos9TAoVdC8mVn-J6j3Fa6-IpIxZoln3kO9y-9lhs2eVukyQL5vde6jEy4xCh8Hz8D_LLzqG57HPI4FMuvBwYgF2I5--QrEL8l7OTElzCa1pf4Bq4dK55_CS-q40_UKj19ke_Ea3iN4z7z5lyOmBN7V4vJJq2ZbBaAPRARstR0old1xSeIrDQw9elbK-t5ljYygdw7hodmSMvCKfVVlb3J4gwXAU2dpOcy_IFyq0DT-7VCW_RFJaeOHyyzi4eKEbGninCfjHobjpjraaUnqx7HtcSwwY0afk5H3luuwmqtHQk83TesRG914ONS0MVRViPjg5MQz3stbQmNTexDMrzTYALFwsQurh8AVDFxB0_E76xEgBqIoC0NfpOOlhPbgJl8D296hPdh5Y7TZLjSVy40ypoy7-PXiYZvQlla8dgiNNvV8MGPMvnHyTBBEwvoMV9lIcFTWLBAdvchJ4v3dRTd-AKGfygW8x2TdtrU6HYPRjZGz5Hdc5_410e-5t2y4z5yxVa86vs2yOJQ_XvwUNMBq7W7NTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: آمریکا سالانه ۴۰ میلیارد دلار به سوئیس می‌دهد؛ بدون ما با مشکلات جدی روبه‌رو می‌شوند
🔴
دونالد ترامپ مدعی شد آمریکا عملاً به برخی از ثروتمندترین کشورهای جهان یارانه می‌دهد و سوئیس را یکی از این کشورها دانست. او گفت ایالات متحده سالانه حدود ۴۰ میلیارد دلار در اختیار سوئیس قرار می‌دهد و بدون این مبلغ، این کشور دیگر جایگاه فعلی خود را نخواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/140449" target="_blank">📅 20:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140448">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ترامپ: خیلی‌ها می‌گویند من یکی از بزرگ‌ترین رؤسای‌جمهور تاریخ هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/140448" target="_blank">📅 20:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140447">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
تصاویر جدیدی از توقف کشتی‌ها در شمال تنگۀ هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/140447" target="_blank">📅 20:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140446">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f48f2a3f4.mp4?token=H_rxKHCXdmwN6-GvNT7FYqVIHVJN6L2PK4FKtcBkCqnfQLq19fvkPl3TxDRR8M-7GAVq4kNeU39Y7fq45uzNyc6jYNvaL0h5nQyc7wYyK5ouoWN3xsUdLs1ZZ6fxmskmWpH-bDV07RrM_Gz5Vdx4m-D8JyhOwgn8SEKMGUFqT1zXwYo3eOLGfR7w3aejLRamI0oBmsYaNdHdKfLvS0cBOvH7PpL3jH2Hx1T0e4U28QRJkAD4_MphykatOKHIyGOh00OOgtUAG6CYhXHThKRmm4NAHbt-ZXwyTUZFTcrKzfl08MQk57g3MtZFRmGxyXW0dZMy41DBVa9mQOJCL71Mqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f48f2a3f4.mp4?token=H_rxKHCXdmwN6-GvNT7FYqVIHVJN6L2PK4FKtcBkCqnfQLq19fvkPl3TxDRR8M-7GAVq4kNeU39Y7fq45uzNyc6jYNvaL0h5nQyc7wYyK5ouoWN3xsUdLs1ZZ6fxmskmWpH-bDV07RrM_Gz5Vdx4m-D8JyhOwgn8SEKMGUFqT1zXwYo3eOLGfR7w3aejLRamI0oBmsYaNdHdKfLvS0cBOvH7PpL3jH2Hx1T0e4U28QRJkAD4_MphykatOKHIyGOh00OOgtUAG6CYhXHThKRmm4NAHbt-ZXwyTUZFTcrKzfl08MQk57g3MtZFRmGxyXW0dZMy41DBVa9mQOJCL71Mqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی برای اولین‌بار از زمان شروع جنگ، وارد صربستان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/140446" target="_blank">📅 20:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140445">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وزارت ورزش و جوانان : ۱۸ میلیون زن و مرد ایرانی بدون حتی یک بار ازدواج وارد ۴۰ سالگی شدن.
🔴
بخاطر شرایط اقتصادی و کسب تجربه از زندگی مشترک دیگران و هم چنین لذت بردن از تنهایی،بسیاری از جوونای ایرانی ترجیح میدن هرگز ازدواج نکنن و تا آخر عمر تنها بمونن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/140445" target="_blank">📅 20:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140444">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d279dcf86.mp4?token=rzJRy2i-K1MgQZ09LXNLzAznZol9ihXqHZVIN7GinoFAAWwOBNjO0n5AQzjFOjTmyT_vrkQyf58AFYIES_Qq3DJlBbS53DfAH2WRUQ8gYrRO1JnGJdWxTX5fxz7ML24MuFUsvgVmnTKCxixYre--QXgUyQ-P1xAdSe1MeUquMiOxkVwKKwPYa8I3eJt_w6Eny4xFhVP32xRQMUPaSS6Vt9Hl6WRKrl7s23srhw0b74VBECSKe6nO4WNU6xmhzrV6qALU_kyF5Q01wuKfWbVOh4J34rS9AVwHmjUV4WGuzPfsTX5fzwDg10m3B72t7o44KHIgfNK3T7y1vNWgK28jUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d279dcf86.mp4?token=rzJRy2i-K1MgQZ09LXNLzAznZol9ihXqHZVIN7GinoFAAWwOBNjO0n5AQzjFOjTmyT_vrkQyf58AFYIES_Qq3DJlBbS53DfAH2WRUQ8gYrRO1JnGJdWxTX5fxz7ML24MuFUsvgVmnTKCxixYre--QXgUyQ-P1xAdSe1MeUquMiOxkVwKKwPYa8I3eJt_w6Eny4xFhVP32xRQMUPaSS6Vt9Hl6WRKrl7s23srhw0b74VBECSKe6nO4WNU6xmhzrV6qALU_kyF5Q01wuKfWbVOh4J34rS9AVwHmjUV4WGuzPfsTX5fzwDg10m3B72t7o44KHIgfNK3T7y1vNWgK28jUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان:
من اگر بخواهم استعفا بدهم رسما اعلام می‌کنم!
🔴
آنهایی که به تفاهم‌نامه می‌گویند شکست، حرف اسرائیل را می‌زنند
🔴
برای جهالت انسان همین قدر کافی است که نداند قدرتش چقدر است.
🔴
یا رهبری را نشاختند یا منطق و عقل سرشان نمی شود. ما به آمریکا چه دادیم؟! کلی دستاورد داشتیم.
🔴
آنچه به اسم تفاهم نامه نوشتیم با قدرت از آن دفاع می کنیم، آنهایی که می خواهند آن را شکست لقب بدهند من می گویم که بی انصاف هستند و این چیزی است که اسرائیل می خواهد و دانسته یا ندانسته دارند پیام منتقل می کنند.
🔴
کنار گود ایستادند و  می‌گویند این جوری است و فردا هم اگر مشکلی پیش بیاید باز هم می گویند چرا این جوری شد.
🔴
از اقتصاد نظر می دهند، از سیاست نظر می دهند، جامعه شناسی نظر می دهند. من نمی دانم این علم را از کجا آورده اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/140444" target="_blank">📅 20:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140443">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
غریب آبادی: امنیت خلیج فارس باید به دست کشورهای منطقه تأمین شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140443" target="_blank">📅 20:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140442">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: تنگه هرمز دیگر هرگز به وضع سابق خود باز نخواهد گشت
🔴
تنگه هرمز دیگر هرگز به وضع سابق خود باز نخواهد گشت، زیرا ایرانی‌ها از آن به عنوان یک گلوگاه استفاده کرده‌اند، یا تلاش کرده‌اند از آن به همین منظور استفاده کنند.
🔴
آنچه در دو سال آینده شاهد خواهیم بود، این است که تنگه هرمز از اهمیت خود کم خواهد شد.
🔴
این تنگه به یک آبراه معمولی تبدیل خواهد شد، و من معتقدم که بیش از ۵۰ یا ۷۰ درصد از انرژی که در حال حاضر از طریق این تنگه منتقل می‌شود، از طریق خطوط لوله زیرزمینی منتقل خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/140442" target="_blank">📅 20:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140441">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WZX-DWKVVdumy-5MkS9wqtYlMFtVCJg4rAF8IF5GP4pLCNipkE1H3LhtjH8nDqDx3wvnHofWSu3jmqO--YKV1Ks3jVd0a2QvMUKOpd1gHL435T22vc9gQ0H2y_xqesUWy8jOwvr9JSvCiSlp8zlqbX3dl5hg-wm31TW4MS0FgHFj8R-Zrbt6y5FwOGm1LMu855E53pHNFaGDVG8b7zHLPzPifFXDWxE9PTuuBBkFpb5BcBz3xeo0hAeITH_Cagl9cowm_1Xw3NoTWUysiTmmigNzPYKjQHXPLiPkGNxNOt56z3hSCbmxg3gsVmkxOEsd_ogwWF9fnsnu5HFzdeHBCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنبش مقاومت اسلامی عراق اعلام کرد که عملیات برنامه‌ریزی‌شده علیه پایگاه‌های عربستان سعودی و آمریکا در غرب آسیا را به تعویق می‌اندازد، این اقدام در پاسخ به فراخوان قبلی مطرح‌شده توسط هادی العامری و سایر رهبران سیاسی عراقی صورت گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/140441" target="_blank">📅 19:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140440">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزارت خارجه آمریکا در بیانیه‌ای اعلام کرد اقدامات جدیدی برای قطع مبادلات مالی با ایران انجام داده است.
🔴
‏در بیانیۀ وزارت خارجه آمریکا آمده: اقدامات ما شبکه‌ای از شرکت‌های مبادله مالی و شرکت‌های صوری که به ایران برای نقل و انتقال میلیون‌ها دلار پول کمک کرده‌اند را هدف قرار می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/140440" target="_blank">📅 19:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140439">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8367154b7.mp4?token=ilnuMiAadNaSc0oCGPrD2ZJg8W3RYfeKwD8kkfRMwjrBZ19b8MyabVpYRgyhunXdxP8u3LQSRBTrZkVSzCDBpCF96qWZykV-Hj2iip4o-Q_ze3eU7m794WAs2AWSoNrx_UtdHZsv_lD8A2VBMWdchbjxUCc6kXL2tTcvtfERF3F3gAa1vpyK4vFtG8MrOL72JbKTRku4EPQkqZpY_6lpICgXTIcg9TqeU0hs_cQYDva61CDNF8LthU_8TQv8Ppjwys7KWj1_CddzLIXbljK02_a9bQfoWwhAhPQVkqpoZJfM1A8eF-jAhuOb_N03moH-SjB06kCUNACB2VKL5DEWiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8367154b7.mp4?token=ilnuMiAadNaSc0oCGPrD2ZJg8W3RYfeKwD8kkfRMwjrBZ19b8MyabVpYRgyhunXdxP8u3LQSRBTrZkVSzCDBpCF96qWZykV-Hj2iip4o-Q_ze3eU7m794WAs2AWSoNrx_UtdHZsv_lD8A2VBMWdchbjxUCc6kXL2tTcvtfERF3F3gAa1vpyK4vFtG8MrOL72JbKTRku4EPQkqZpY_6lpICgXTIcg9TqeU0hs_cQYDva61CDNF8LthU_8TQv8Ppjwys7KWj1_CddzLIXbljK02_a9bQfoWwhAhPQVkqpoZJfM1A8eF-jAhuOb_N03moH-SjB06kCUNACB2VKL5DEWiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عطریانفر: پوست قالیباف به اندازه‌ای کلفت است که خیلی نگران اهانت تندروها به او بابت مذاکره و توافق نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/140439" target="_blank">📅 19:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140438">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
کانال ۱۴عبری: شواهدی از وخامت حال مجتبی خامنه‌ای وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/140438" target="_blank">📅 19:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140437">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
عبدالرضا داوری: ایران به توافق مکه وارد نمی شود، چون قدرت ایران ناشی از استقلال آن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/140437" target="_blank">📅 19:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140436">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
المیادین به نقل از یک منبع در وزارت خارجه پاکستان: به احتمال زیاد، عباس عراقچی، وزیر امور خارجه ایران، روز دوشنبه به پاکستان سفر خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/140436" target="_blank">📅 19:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140435">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
به گزارش هیل، دونالد ترامپ گفت رأی‌دهندگان حزب جمهوری‌خواه در آستانه انتخابات میان‌دوره‌ای از عملکرد جمهوری‌خواهان حاضر در کنگره ناراضی و خشمگین هستند.
🔴
ترامپ مدعی شد این نارضایتی متوجه او نیست، بلکه متوجه نمایندگان جمهوری‌خواه در کنگره است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140435" target="_blank">📅 19:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140434">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
خبرنگار ارشد کاخ سفید: سنای ایالات متحده رسماً بررسی تحریم‌های سنگین علیه روسیه و ایران را آغاز کرده است.
رأی‌گیری نهایی ممکن است امروز برگزار شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/140434" target="_blank">📅 19:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140433">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
پایگاه اینترنتی نیروی دریایی ترکیه: یک کشتی باری با پرچم ترکیه در سواحل بندر نووروسیسک روسیه هدف حمله پهپادی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/140433" target="_blank">📅 19:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140432">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
معاون وزیر امور خارجه : اگر به شرایط صلح برگردیم، احتمالاً جلسات امنیتی بین کشورهای منطقه برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140432" target="_blank">📅 19:18 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
