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
<img src="https://cdn4.telesco.pe/file/ZzDp9W0ZDLtejLlQiyPBG8RhXlGzCcQ_fletEC4kPUO2-L9y4xL4bBFV22D2AO5OkVAlWfvdEFzCZI7Y3bHmtK3IvxEeM3Ox0rm_nobh7D9u9fVkjI3p81JqE9rH-UhZgNlL-S2VrrJkiVHRCwg9bVWvdyF9F6XawkjLT4F5eCacKOv-tEDRljrqwKiUZhpC4zZd4Zzd3eQ3ec3OU9jySMZ8p2o2Q8ZamazJ0fCiBzeUoVPmBT-XAUTXAPvhXJwxLhJ4piXOxaZdeSsgeGqFcqN4X65NsrFZzg5oS31Z1ImtiLTSNO-szc2MCFJsLSuBGGDEZSbKqVO-jKhZesQmCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.52M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 01:29:10</div>
<hr>

<div class="tg-post" id="msg-659939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppuWhJ95zGljCmVGR6N0M3xEWGHl6n-c62HuPyqqJv6lU2tsEB2fuKa3hZpf0tQ-nHAtH15XsYjU7nCdtB9A60XzEdZYV4FGhGIaIJzvRUN1hyLvQPTHdx5JLCnnX7DfBMNmGVWJqRngsIMCHnKM2wK7iFpLVkVyD32lqYIdVQvuNxH-uab-58CxDIQyc-qMgE5HQCDe9uf0QBOxpXzuuwV14niv84xGgCNft-zhIfk2Ji8Z2NYw54ozVoGl6c29_7SDKM17Je8wQvhA0CKXEmIwoOCaJ6Ft6RCTtDiQieHZsquXHvny_TF41qMtRhvt0NuO7hqey_nJZIq8fH6e4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
برند شما لنگر است یا یک قایق سرگردان ؟
💭
برای تحلیل برند شما فقط کافیه یک پیام بدین :
👇
https://t.me/+Xot5PGy2C04wMzA0</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/659939" target="_blank">📅 00:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvM2j18oJU5JoIMZ8cuKJOjLZ2McoNpNqJyHXNd3o-GXEE671K6OMFg3OGR2nbQSsm6X3a2vNq0EN1b3j-CRhMihOcJE2pGIuHyx48oat7BWt1u4jcr65yfMHVFlicU0EnF7ISqta5H6mnDPXly1wxX7h6Jd5Qm2R8vMYK8qlJaJ_vNOoo0y6zmR1DVqY_9dKTtCviv5FjHYM0tEFMhyvndqcpkPUoG4T3xO60i3yr39BcNmY6mNDJQdtPYLsx0MYtXZIl3cn4TgReWFcSM_LX_uACFshTjkV3FVz04N0SqzVfOzc53Kitz3JrDOvkRMeFXSPuWrwnb_ErPKDn6ayw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بریتانیا: استفاده از شبکه‌های اجتماعی برای افراد زیر ۱۶ سال ممنوع شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/659938" target="_blank">📅 00:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659937">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ux_F5ABJVv7SeDxNBG44PWxrCrIxNfNncCZW5lFpVEx5Ey1imI7h4_TJQiXIt6dGf_jrM-twtR376PjUeiU6Q5BPUDi-cNdMUo-pRXcJCoTyfkGBbHMTc5IOoPpQE0cDBbIWJjE3NxYTrYHeuA-q4dzg_cI3vlGUE3mO9OzjCw13fif87byLCeSsfTfQIsRbGu4xgB2t6KsL7ZLzRJkzHZa6TQPJXz-CFxWwqNHQa2ADyB-pSluFKUYRtv85xaB_FYkF57xmgcaCbGfe_jQlIrxxTTkjx051FxxQIL604LHerfsqnPamGS0hCj-XFCNDf0Go_7ROGWUDQmGZCazUhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار کانادایی: فقط برای اینکه شفاف باشید ، ترامپ میلیاردها دلار صرف ایران کرد ، هیچ چیزی به دست نیاوردسپس تسلیم شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/659937" target="_blank">📅 00:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ادعای اسرائیل هیوم: آمریکا به طور محرمانه یک توافق مالی بین قطر و ایران را تصویب کرد
🔹
در این توافق به دوحه اجازه می‌داد وجوهی را به تهران منتقل کند در ازای تضمین آزادی دریانوردی در تنگه هرمز و جلوگیری از حملات به شناورهای قطری، به گزارش اسرائیل هیوم.
🔹
این توافق که تقریباً یک ماه پیش مجوز آن صادر شد، با هدف تثبیت بازارهای جهانی انرژی و کاهش قیمت نفت بود، ضمن اینکه زمینه را برای یادداشت تفاهم گسترده‌تر بین آمریکا و ایران نیز فراهم می‌کرد.
🔹
این توافق به ایران دسترسی به وجوهی را می‌داد که در قطر نگهداری می‌شد، از جمله پرداخت‌هایی که به عنوان عوارض عبوری برای تانکرها ارائه می‌شد و یک خط اعتباری تا سقف یک میلیارد دلار برای خرید کالا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659936" target="_blank">📅 00:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDPblND8x_p5KKJzhGoK3rGf153vb0GGRswweXPLZyazsbXhwzNLAKDk61TxNN0evz7pF0aMn9_J_lI_OxfcMHJ5l5n6x76ZvyrhL7-TVcmzTVU_UQndlE6V5w80PnZ7T3Tsy1wftUVFOrNCPiR3xgth9Bjfbmk_XIZEryy6dcFo1D4VPECuKVF8ULDZjansmKSd1dP12_Af-WlDD3P_Zr1VwUddAxbjY1A-pe-W5cL55ocs3jc6b9lZKoUS4gllO0is0ApsH-DcI3BlUatBLUFnqyWSc4CPTWGyZJSfCuniCdDYDKfrJwDraqPYTS8Ou8r3Ym_-MLAUt6C98feyHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه روز سه شنبه بازی‌های فوتبال جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/659935" target="_blank">📅 00:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659934">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
لوکاشنکو: اگر خواهان عدالت هستیم، باید تمام سلاح‌های هسته‌ای جهان را از بین ببریم
رئیس‌جمهور بلاروس:
🔹
ایرانی‌ها می‌توانند بپرسند که چرا ما نمی‌توانیم سلاح هسته‌ای داشته باشیم؟ به خصوص وقتی هند و پاکستان در همسایگی ما قدرت‌های هسته‌ای هستند.
🔹
چرا ایران نمی‌تواند سلاح هسته‌ای داشته باشد؟ اگر سلاح‌های هسته‌ای یک عامل بازدارنده هستند، تضمینی که هیچکس هرگز به شما حمله نخواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/659934" target="_blank">📅 00:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659933">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KabK5CnvNygzQgob9mMVYSNYHARRE5WpcC0gAl-_i3cycyh-skDez0YACoqgOKnDiZmlEF9W9CjF2gvGaahbIXiMIwy0U_PLsmBvli2Db9onMtjuyNwhXmgBZCA8aSSdUNdA8Z6b50VLUMhuSu4QQWB796tm3Xiv93a8VBYRjtZq8rWEV6ph9iKSqoQgmGlD8PzcBi9hwcN8_CCD0vMLu7O_v8HDGpzEb48d8wXCcqLnhonP38NhKi9s0B6A7w3igDqvgFuGpFFpsxcChVtJoRxc2KNlKS1lyKIShzBRaHQ2eyNPBnPUo9b45NczEu9RpB0h5EKjZrn6LTlck69_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بی بی سی: توافق ایران کابوسی برای نتانیاهوست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/659933" target="_blank">📅 00:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659932">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ادعای شلیک ۳ موشک از خاک لبنان به سمت نظامیان صهیونیستی
🔹
شبکه الجزیره مدعی شلیک ۳ موشک به سمت نظامیان صهیونیست در اطراف ارتفاعات «علی الطاهر» در منطقه النبطیه شد.
🔹
ارتش رژيم صهیونیستی مدعی شد که تعدادی از موشک‌هایی را که حزب‌الله به سمت مواضع نظامیان این رژيم در منطقه مرزی شلیک کرد، رهگیری کرده است. هنوز حزب الله بیانیه‌ای درباره این حمله صادر نکرده است .
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/659932" target="_blank">📅 00:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659931">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOPe94D8scLDsgiFldRBXBamqtxI3ifKkqkiHJSDAub8ZFIbeqLeSctyaztyeCPeLhFwQZlc9b9LmegL58NiKqdOjnHTgBPM_UTJSlZQKsl7Dw4Ni8ZYnpRVJpXWjAz6K0Du0UwEh_H8mmTDnC-j3YtnsDwLnV9BAKr9QqNxwRcReu76TdBBTl-Fc9XKOXLBXMkkzwHnp5UxLeM0ffSZ7Z2PPW7LMpgsEt1BqlqphX5vz7YAEZADCifPdrbJGfOVhtOCZMH7dBA6T5ZXNL5WKd4Kmb8w1YGX00V3h2FvXrn9Cy5qvAZ_ilJ05A-rCDGXtEutdBs1KgkomVfkkCQ_zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقاومت عراق: سازش نخواهیم کرد
🔹
«ابوآلاء الولائی» دبیرکل گردان‌های سیدالشهداء عراق با انتشار پیامی، پیروزی جمهوری اسلامی ایران در جنگ آمریکا را تبریک گفت و تأکید کرد که مقاومت اسلامی عراق هم در این پیروزی نقش داشته است.
🔹
وی خطاب به رهبر شهید انقلاب و شهید سید حسن نصرالله گفت: سازش نخواهیم کرد، بر سر عهد و پیمان باقی خواهیم ماند و به همین مسیر ادامه خواهیم داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/659931" target="_blank">📅 00:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659930">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">#خبرفوری
♦️
اجرای رفع محاصره دریایی آمریکا آغاز شده است
🔹
سه نفتکش و دو کشتی حامل کالاهای اساسی برای ایران از محاصره دریایی عبور کرده‌اند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/659930" target="_blank">📅 00:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659929">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mK2F1Hi58fEIhiC8CVkwZQTLnFLQPMQzynlummU4Jy-NI-qmUsopYTzUddrv9Rqj17rSKTkuqmoCzXR3SsEeNpLzyq05Cuuy-lwq1wDtrRurRnpZ-F9pCoysjyluu_qx13p2tqQJO7uQA_MHSTpw8PNy-LsOeOKAOKDjrZCwyMxB1o548jKjc1lUAyyDE7jpt25Kt21s5PSaOLmf3G3N8tSLWfUv1oyWkY2GQArrMk1KxgnfAkDAeSbsXO9ofjUYT2fr6j8bzWFxap4pHUi5lXbRpgbFQ_r4apdoYFh8C5T0nybhKtzCWlKyW4e7EXbZ8X9XHP8GtMUwZvff0m1EJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/akhbarefori/659929" target="_blank">📅 00:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659928">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/040ca7825d.mp4?token=Fy7rLDdW_7azyftLaLb4PiKbGs6TvDnalGEJ5ldEBq0uetVBHfzzGgHZkYrYNJ9-f3Bgjj4n4WEFMYA9mwnJATW_hTdxm80PTPB2jm9vxvPr6RmvA3if3mwQ39pCEav94GYELkJ5lUlrwOTEnfRr2co2wssrsiECjLJLmhnl-uTS5kSsXMCaLmzrlOpqwG3Ghlyu48Jbu4byskdeqxWSK3WhnJcnzYapf2TpeZ7c_Kf6J3ZRZI02HtE37BYst1wiruIWEVOvY4LdxRAtz5ZMDkhLS4EqhrqB8dgn2UsXhKUk9o2gk2mExYqafp7_5zrT-knH6thoWKdjvEaxjwUcoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/040ca7825d.mp4?token=Fy7rLDdW_7azyftLaLb4PiKbGs6TvDnalGEJ5ldEBq0uetVBHfzzGgHZkYrYNJ9-f3Bgjj4n4WEFMYA9mwnJATW_hTdxm80PTPB2jm9vxvPr6RmvA3if3mwQ39pCEav94GYELkJ5lUlrwOTEnfRr2co2wssrsiECjLJLmhnl-uTS5kSsXMCaLmzrlOpqwG3Ghlyu48Jbu4byskdeqxWSK3WhnJcnzYapf2TpeZ7c_Kf6J3ZRZI02HtE37BYst1wiruIWEVOvY4LdxRAtz5ZMDkhLS4EqhrqB8dgn2UsXhKUk9o2gk2mExYqafp7_5zrT-knH6thoWKdjvEaxjwUcoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداقوت سردار قاآنی به محمدباقر قالیباف و افراد همراه وی در هیئت مذاکره/ طوری با اقتدار برخورد کردند که ترامپ به لرزه افتاد
🔹
چه آن برادر پای لانچر، چه برادران در محور مقاومت، چه برادران در هیئت مذاکره، از جنس مقاومت هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/659928" target="_blank">📅 23:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659927">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
سردار قاآنی: هیئت مذاکره‌کننده ایران به محض تجاوز رژیم صهیونی به لبنان با اقتدار با دشمن و واسطه‌ها برخورد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/659927" target="_blank">📅 23:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659926">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
سردار قاآنی: باب‌المندب یکی از برگ‌های برنده جبهه مقاومت است و اگر لازم باشد برگ‌های دیگری هم رو می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/659926" target="_blank">📅 23:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659925">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCgrCPPX65Nd-g7u-tcouYvbk8NLqbnkgM-HqHPzPrOKQo51V2U-fiq-PlSVL-52yEGU3xn95nnqVevNCD4M2gMWtuB_ojsL50_KZzI33rVvlqUfAkJJ8w8WWksfpBcpGHwmEpL2q6QJPVJSzTgfAXYSGqSL1MfYAMXh0cde099UJ5wXw9MR9Rb94UkyT4mBbvLxOW6FT5IM8boEqQn_eG-g61ax9WSyHZg6VtyhvTZPkeeIvCB5cU5vCCT1XE14SOFC2ya8SFtydzR9EJ6pFmBxADxiIerA8SSu_53vFC21_5d-88ZdnLBHI9qRQb1Qt5eW7jhUBvIEJUT05JeIOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جک سالیوان، سناتور آمریکا و مشاور سابق امنیت ملی امریکا: اگر من جای اپوزیسیون ایرانی بودم جایی غیر از آمریکا را برای زندگی انتخاب می کردم. آمریکای ترامپ آمریکای گذشته نیست. و همه چیز در آن می تواند کارت معامله باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/659925" target="_blank">📅 23:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659924">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e31d2e069.mp4?token=eSM_kimp6Bhgf2XvVUnVWfmtdcI9mexk1BkOOR5i3QzekAvBkYcJISZ64tTcx85Y5WiWqtzKZnRXL6XQBKukXMJ1CFwpZJFm9uWrtJQ0DOKnpelMjWThfew87git8xEIY-0dN-PUj8PrRczYQPy6sdOBMRj3CIjFeUSMmnELdiXSRu18Ij4Q2Ds4ayTqCLGbCabt07wBxFtG85d6B8RJ3GrIDndhapaKSfpqxH-181Xdwt3Cwa2p6nzpKG0idCOuoJwJ8R4QjHVoH1KQkyXwHjkXuPSyN0i0EqgZ49kbacItl7EAlauhEvh7n5gIPtWNSo40GxGfhyQydfQR32MqmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e31d2e069.mp4?token=eSM_kimp6Bhgf2XvVUnVWfmtdcI9mexk1BkOOR5i3QzekAvBkYcJISZ64tTcx85Y5WiWqtzKZnRXL6XQBKukXMJ1CFwpZJFm9uWrtJQ0DOKnpelMjWThfew87git8xEIY-0dN-PUj8PrRczYQPy6sdOBMRj3CIjFeUSMmnELdiXSRu18Ij4Q2Ds4ayTqCLGbCabt07wBxFtG85d6B8RJ3GrIDndhapaKSfpqxH-181Xdwt3Cwa2p6nzpKG0idCOuoJwJ8R4QjHVoH1KQkyXwHjkXuPSyN0i0EqgZ49kbacItl7EAlauhEvh7n5gIPtWNSo40GxGfhyQydfQR32MqmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بنظرت اینا چرا نرفتن جام جهانی؟!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/659924" target="_blank">📅 23:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659923">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
زاکانی: پوتین گفته بود که نیروهای نظامی روسیه به من گفته بودند که ایران نهایتاً یک هفته می‌تواند تنگهٔ هرمز را بسته نگه‌دارد
🔹
روس‌ها به ایران گفته‌اند باور نمی‌کردیم شما اینقدر قابلیت داشته باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/659923" target="_blank">📅 23:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659922">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
سردار قاآنی: باب‌المندب یکی از برگ‌های برنده جبهه مقاومت است و اگر لازم باشد برگ‌های دیگری هم رو می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/659922" target="_blank">📅 23:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659921">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
امکان ورود خودروهای سال ۲۰۱۶ به بعد و کمتر از ۲هزار و ۵۰۰ سی‌سی از مرز سرخس
احمدی، مدیر روابط عمومی منطقه آزاد سرخس:
🔹
امکان سرمایه‌گذاری در این منطقه برای عموم مردم بصورت خرید سهام وجود دارد و یکی از این مزیت‌ها استفاده از پلاک منطقه آزاد است به این ترتیب منطقه آزاد سرخس از کد ۸۵ برای خودروهای شخصی، ۸۶ برای تاکسی‌ها و ۸۷ برای خودروهای دولتی استفاده می‌کند‌.
🔹
مالک پلاک می‌تواند از خودرو در منطقه مشخص شده استفاده کند و برای خروج از آن می‌تواند از شرایط مرخصی یک ماهه استفاده کند‌.
🔹
شرایط خودروهای منطقه آزاد بدین شکل است: خودروها ساخت سال ۲۰۱۶ به بعد باشد، خودرو ساخت آمریکا نباشد و حجم موتور آن بیشتر از ۲هزار ۵۰۰ سی‌سی نباشد و سازوکارهای استفاده از این خودروها تا یک ماه دیگر بصورت عملیاتی درخواهد آمد./ جریان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/659921" target="_blank">📅 23:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a346e05a73.mp4?token=egOVgiG-HAOtcEFFRfxeT9pCuUk5yN3q8ZFP5TR8v_RSTVmuTNyqboxVV4GBifp-TjG89Jfe6iBW_-xzs724rdDKXyos_bR5rFAakIL5W3T712U9b7cVlCsKg5lNyp5pwjxeHO8WM0V4NbdANFbBkZH0PDTiFTNYk0Zc3QKSefQHhGrQFp8oVA6GmwAoNX_2GeDf1ln7iZa6ThBvHUS8cm-s-leIp9_P32gW_axi1vpwvVwGkaFSHgzPdGRaBLdtMly643ORh50wCJ7dmOZ1VKdZjwWcJ2tfeKzu32FDlhmfFphUgbA3cLpdR-EX4lAt5cXJxxH8qphwmyI1ieKMVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a346e05a73.mp4?token=egOVgiG-HAOtcEFFRfxeT9pCuUk5yN3q8ZFP5TR8v_RSTVmuTNyqboxVV4GBifp-TjG89Jfe6iBW_-xzs724rdDKXyos_bR5rFAakIL5W3T712U9b7cVlCsKg5lNyp5pwjxeHO8WM0V4NbdANFbBkZH0PDTiFTNYk0Zc3QKSefQHhGrQFp8oVA6GmwAoNX_2GeDf1ln7iZa6ThBvHUS8cm-s-leIp9_P32gW_axi1vpwvVwGkaFSHgzPdGRaBLdtMly643ORh50wCJ7dmOZ1VKdZjwWcJ2tfeKzu32FDlhmfFphUgbA3cLpdR-EX4lAt5cXJxxH8qphwmyI1ieKMVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف جنجالی عضو سابق تیم مذاکره‌کننده آمریکا؛ ایران پیروز این جنگ شد و آمریکا در دستیابی به اهدافش شکست فاحش خورد!
آلن آیر، عضو پیشین تیم مذاکره‌کننده آمریکا در توافق هسته‌ای:
🔹
ایران از بسیاری جهات این جنگ را از نظر راهبردی پیروز شده است. ایالات متحده در دستیابی به هر کدام از اهداف راهبردی خود به طرز فاحشی شکست خورد چه از نظر برنامه هسته‌ای یا توقف پهپادها موشک‌ها یا حمایت از گروه‌های نیابتی.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/659920" target="_blank">📅 23:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659919">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1deb3b2bdc.mp4?token=MMpEt817FuVOhWUQQRBMfFsOawPiOw2xwre4F7Id0Q7t5AbNqAjBzH7gkHKMLH3NdK1B0Paj9gpyoFaCbfDI-BD2V_KVgdA_O0RAmUVjn-MBnZMth8P_ownbRlJhU9u6VGMZ7wQzymKdzA16DqDFAPz9uJRWnc_7ZuOPxEEcBcnKs3Kr23KatUaKwT5Feg9DpQ-r9_vj3jopMiyPSq5Yq1ut1UIWWZz71c0yU98Ye7WtOMbHbTO0nLV8WHA-M7I5RCCvQYaI8FM9r-KZHiV7fJVRV7AV0DT-CeFr0Me78p_687njmbTi6XbTtM8GGlx4Mv45iP_D7iA8Clx5DZFDPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1deb3b2bdc.mp4?token=MMpEt817FuVOhWUQQRBMfFsOawPiOw2xwre4F7Id0Q7t5AbNqAjBzH7gkHKMLH3NdK1B0Paj9gpyoFaCbfDI-BD2V_KVgdA_O0RAmUVjn-MBnZMth8P_ownbRlJhU9u6VGMZ7wQzymKdzA16DqDFAPz9uJRWnc_7ZuOPxEEcBcnKs3Kr23KatUaKwT5Feg9DpQ-r9_vj3jopMiyPSq5Yq1ut1UIWWZz71c0yU98Ye7WtOMbHbTO0nLV8WHA-M7I5RCCvQYaI8FM9r-KZHiV7fJVRV7AV0DT-CeFr0Me78p_687njmbTi6XbTtM8GGlx4Mv45iP_D7iA8Clx5DZFDPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دمام زنی با شکوه گراشی‌های استان فارس در اولین شب حسینیه معلی شبکه سه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/659919" target="_blank">📅 23:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659918">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سوار شوید به کشتی نجات حسین</div>
  <div class="tg-doc-extra">جواد مقدم قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/659918" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🥀
توی گوشه عالمین میخونه سقا
ارکبوا فلک الحسین ایها الغرقی
سوار شوید به کشتی نجات حسین
دچار شوید به باده فرات حسین
🎙
#جواد_مقدم
#محرم
مرجع رسمی مداحی و نماهنگ انقلابی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/659918" target="_blank">📅 23:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659917">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
شبکه ۱۲ رژیم صهیونیستی: قضات دادگاه نتانیاهو درخواست نخست‌وزیر برای کوتاه کردن جلسه فردا را رد کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/659917" target="_blank">📅 23:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659916">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pgyj8b4ieeMVemyBoqPwrHhxSJ5jwpQeVmJH5T9qzZQS3cxcov7QRvJT7geBSUwdFHvUC1r6mSxtxWzat3NOU9iG6_Vh1k7fo0ykVLSns2ZG4DxQZgeQa2HJJB7KPC6KYTfUx5BAQqfD-FL0oMnV9quISo4e_69YpssrJ-H2vMbt9IOs6Ui-HnyyaKbK-Ttrlj6jivbVS1gPYLTYtRqULDm0XeuX5NT7qioXeJb2ZTANA_pF54EbtJsZ1rEUFDTzkYVjXaplYq8011uNd03X1a-PdcC74RrhXRsDR1Zom-vmZUZWLSjx1EQaenA0FNRhu5ogrCs0Vo484yomkxarJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هیچ شبی نیست که ما نخوابیم و به شما فکر نکنیم
There's no night that we don't sleep and think about you!
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/659916" target="_blank">📅 23:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659915">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
سردار قاآنی: مقاومت فراگیر است؛ از درون خانه‌های مردم ایران تا دورترین نقاط منطقه درگیری موج می‌زد
‌
🔹
دو جنگ تحمیلی و کودتای تحمیلی، دوره سختی را بر کشور و منطقه تحمیل کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/659915" target="_blank">📅 23:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659914">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
ادعای الجزیره: اسرائیل برای نابودی توافق آمریکا و ایران اقدام خواهد کرد
‌
🔹
شبکه الجزیره با انتشار یک گزارش تحلیلی اعلام کرد که اسراییل هر کاری برای برهم زدن توافق میان آمریکا و ایران انجام خواهد داد.
🔹
در این گزارش آمده است که اگر اسرائیل در تخریب توافق موفق نشود، ممکن است از دونالد ترامپ رئیس جمهور آمریکا بخواهد که در جبهه‌های دیگر، مانند عدم خروج از لبنان یا آغاز جنگ داخلی در این کشور شکست خود را جبران کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/659914" target="_blank">📅 23:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659913">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37d47c8494.mp4?token=cwkbuXC1XrdQTkrruvuvuWtKw2WybggFstx2Bw2hWDLNkXWA6ZgrEyH8Bg2ljHkCOJzpCkGUt25vbv-_kxHuaFv333TFD5ML6JNieKOg2sj31UzrcAHRE1pn-ap6mpE8Twf0cFrOoiIye9HK-FSYjRhPE7m-D5LFglYESuU8lY-NnrtxJBxs8kffRkmIk5EOPJvozNiKreb9qGYrgrAd1foEMspaiJ-H_f8CE-RZG5uaH5dON_MWMxWKUDKapOwtnXR5vf57c44n7Xg_1ip_4k_Bm83zFRv6MxxhFLrVi85QO4-KiKFJojQGNbnYqm_OtJ7k-sUi8Eg5Jdr32tlffA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37d47c8494.mp4?token=cwkbuXC1XrdQTkrruvuvuWtKw2WybggFstx2Bw2hWDLNkXWA6ZgrEyH8Bg2ljHkCOJzpCkGUt25vbv-_kxHuaFv333TFD5ML6JNieKOg2sj31UzrcAHRE1pn-ap6mpE8Twf0cFrOoiIye9HK-FSYjRhPE7m-D5LFglYESuU8lY-NnrtxJBxs8kffRkmIk5EOPJvozNiKreb9qGYrgrAd1foEMspaiJ-H_f8CE-RZG5uaH5dON_MWMxWKUDKapOwtnXR5vf57c44n7Xg_1ip_4k_Bm83zFRv6MxxhFLrVi85QO4-KiKFJojQGNbnYqm_OtJ7k-sUi8Eg5Jdr32tlffA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاید اگر امروز ماکان نصیری بود، میان هزاران هوادار ایستاده بود و برای ایران فریاد می‌زد
🔹
حالا فقط خیال است که او را روی سکوها نشانده؛ خیالی که گاهی از واقعیت هم واقعی‌تر به نظر می‌رسد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/659913" target="_blank">📅 23:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659912">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd8760fcbe.mp4?token=HpITYNWFY8iczUdS88McjdqJEcfLjT8q2IA0bksdCj9EPjGi0wL84TR5EbBnTgGdz2Dny5TXrzVs-O0NbGsXu8m-RDDAIWlvQAMpGB8cfI03NLomNFdwGt51SGxv3uYJysndj45KK36aTxu3IEgtdDnQXjdEXlRJuL6ueCdU3dz7851-VRl_RurTszW24lybr6ndphiDtJvzZSvuxBDIGotOLbL-FjmQaTXysjMAeDjylcIkQ9FbJUVo61cz4fAtcOsXhhnJ4QotNRVIQjeV_3NtYrajpFiuNi6NYV5vJk7wVxACg0sywu9gV54_Mewiz36B8BiRxOjT6K2MhOF74g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd8760fcbe.mp4?token=HpITYNWFY8iczUdS88McjdqJEcfLjT8q2IA0bksdCj9EPjGi0wL84TR5EbBnTgGdz2Dny5TXrzVs-O0NbGsXu8m-RDDAIWlvQAMpGB8cfI03NLomNFdwGt51SGxv3uYJysndj45KK36aTxu3IEgtdDnQXjdEXlRJuL6ueCdU3dz7851-VRl_RurTszW24lybr6ndphiDtJvzZSvuxBDIGotOLbL-FjmQaTXysjMAeDjylcIkQ9FbJUVo61cz4fAtcOsXhhnJ4QotNRVIQjeV_3NtYrajpFiuNi6NYV5vJk7wVxACg0sywu9gV54_Mewiz36B8BiRxOjT6K2MhOF74g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط بمب‌افکن استراتژیک B-۵۲ آمریکا در کالیفرنیا
🔹
پایگاه نیروی هوایی «ادواردز» در ایالت کالیفرنیا از وقوع یک سانحه هوایی برای یکی از بمب‌افکن‌های استراتژیک این پایگاه خبر داد.
🔹
این بمب‌افکن از نوع «بوئینگ بی-۵۲ استراتوفورترس» (B-۵۲ Stratofortress) بوده…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/659912" target="_blank">📅 23:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659911">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
زاکانی: پوتین گفته بود که نیروهای نظامی روسیه به من گفته بودند که ایران نهایتاً یک هفته می‌تواند تنگهٔ هرمز را بسته نگه‌دارد
🔹
روس‌ها به ایران گفته‌اند باور نمی‌کردیم شما اینقدر قابلیت داشته باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/659911" target="_blank">📅 23:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659910">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kW0hxS6Un0zSeHdtz-als13-Y080Yc7BDJdcURS72kPiNYFDze6OZOO9KA_3CJAlUP8lmplSuB8_WCd4m081UidTPUvOAe44HupYiAPppXq2Q76RFo2c7o0WV0aCqosLCG8pDZ5S58A-DJzoeeQJrKitJ-tHzyG9K7N3VhGB-xfdNS0Sx7xfxlZLwUcHwxLpZdCbBjMcuP9wFwwJv1QvfbtlE5zxC1YxrAjZxGqxlEVFgWFaW_MKrl9JimMXZl23jONf3d5ZFXt_rOsv5Ty17IwukqQoPYDLoJ85_sXevK6uoD-5FKRDfQqJkMxf8LjYWAyG3ML6Qgt7gsZ6838tDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار برای نخستین‌بار؛ تصویری از شهید سپهبد باقری در دیدار با فرمانده کل قوا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/659910" target="_blank">📅 22:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659909">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d326d270d2.mp4?token=N72o6_pF3JRKMrFNPeg1BsW3klP2D71ZvobpVsuBfOMY02FzJkKgIaOmf1T6hgomeO3Nga1b95NYJ-4STz65i-UNbiiQCKrsNNSn3LYOvPbY3Uqv_4yKQinK0cjTnYJTzu-J8TReOKFNKQdhYLqtnaK5aWxu7eyeGEslsIz4fYNSl3mhgfsXz8OY4k8S_JUQebBNHvI32Cu0MYyOHZ8TPDESc474tJrGO0k3ptIFaQA2B-6Ue2-M1mjyINWickkGhgqByqYrXM0dyZa9lTervs3lcjPFGNoPcon3KtyIu9NZyhEbQmE7COe1pB9T-qWeDLLRa8iForPpZvjxRK6jmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d326d270d2.mp4?token=N72o6_pF3JRKMrFNPeg1BsW3klP2D71ZvobpVsuBfOMY02FzJkKgIaOmf1T6hgomeO3Nga1b95NYJ-4STz65i-UNbiiQCKrsNNSn3LYOvPbY3Uqv_4yKQinK0cjTnYJTzu-J8TReOKFNKQdhYLqtnaK5aWxu7eyeGEslsIz4fYNSl3mhgfsXz8OY4k8S_JUQebBNHvI32Cu0MYyOHZ8TPDESc474tJrGO0k3ptIFaQA2B-6Ue2-M1mjyINWickkGhgqByqYrXM0dyZa9lTervs3lcjPFGNoPcon3KtyIu9NZyhEbQmE7COe1pB9T-qWeDLLRa8iForPpZvjxRK6jmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مذاکرات بعدی ایران و آمریکا چه زمانی برگزار می‌شود؟
‌
عراقچی:
🔹
قرار است روز جمعه در کشور سوئیس که محل دقیق آن مشخص خواهد شد، یک دیداری بین هیئت‌های دوطرف انجام شود، که در آن روسای هیئت‌های دو طرف ابتدا این یادداشت تفاهم را امضا کنند و پس از آن اولین دور مذاکرات بعدی را داشته باشیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/659909" target="_blank">📅 22:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659908">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7143f0be3.mp4?token=avvsTsOqBou4VnwnpHOroG_rKXm6reDqz-EOLFtQIU0nKIW9v98pd1TvU4W72Og7wDup4HvCu9Q-Do2uK6_P3yKinVoLKM-X7BUZh3OiA3xOSPzkX8cmYlT3TSavIUayHvzxK90XHAuzueO4zkvbFKlQyDO5F4NORyiA4I-KbqL2wlD7cyfswcoB2BHq7gxx_gnBlz_6M7EL-UzUmZZrfSGt0_ZP2XRK5A-sp82vI4n09X1BhqfqKtQUySp0qu8dl65s4CNUWo3u3cK1TArOx8ncJ22i2_W5ZwxX4hTMF6lPBYdubObFMTl65uIHt4wSMelDj3E-XZLhGyZs3H5lIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7143f0be3.mp4?token=avvsTsOqBou4VnwnpHOroG_rKXm6reDqz-EOLFtQIU0nKIW9v98pd1TvU4W72Og7wDup4HvCu9Q-Do2uK6_P3yKinVoLKM-X7BUZh3OiA3xOSPzkX8cmYlT3TSavIUayHvzxK90XHAuzueO4zkvbFKlQyDO5F4NORyiA4I-KbqL2wlD7cyfswcoB2BHq7gxx_gnBlz_6M7EL-UzUmZZrfSGt0_ZP2XRK5A-sp82vI4n09X1BhqfqKtQUySp0qu8dl65s4CNUWo3u3cK1TArOx8ncJ22i2_W5ZwxX4hTMF6lPBYdubObFMTl65uIHt4wSMelDj3E-XZLhGyZs3H5lIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط بمب‌افکن استراتژیک B-۵۲ آمریکا در کالیفرنیا
🔹
پایگاه نیروی هوایی «ادواردز» در ایالت کالیفرنیا از وقوع یک سانحه هوایی برای یکی از بمب‌افکن‌های استراتژیک این پایگاه خبر داد.
🔹
این بمب‌افکن از نوع «بوئینگ بی-۵۲ استراتوفورترس» (B-۵۲ Stratofortress) بوده که دقایقی پس از برخاستن از باند فرودگاه، دچار سانحه شده و سقوط کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/659908" target="_blank">📅 22:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659907">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6580fb232d.mp4?token=rvf_PAfQiDSsNLu9vXtlzyyR7cHJMgtkXMA9bzGuwa9rk-rXa_NSuBv8LmXdgLMszjlDpENH5b1IDpzE_py_JB9Z0Pfli-MAWtsBJOxHLmJ3Yvriy30H2-wgBECwkoC6FAnZmiRhfhk4tvDQ_tWVmhQPb8DkEgcUgZuKtodNdlY-IcMKrj8qsmVminPbsCgdrRcr1_5v3QR1cNeU8QZYzbqXcP9lTnxd_zPMLGZA7v-VbR1eGA_UZ6YOihTYdjF9Wn3LZlCy9_mujCvKweqDQhbiBq-zlTYbDlxXOGewa2yalVzIdGVMU0ZEG49TRcJtMirYCx1NXYHR98QtqGoptg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6580fb232d.mp4?token=rvf_PAfQiDSsNLu9vXtlzyyR7cHJMgtkXMA9bzGuwa9rk-rXa_NSuBv8LmXdgLMszjlDpENH5b1IDpzE_py_JB9Z0Pfli-MAWtsBJOxHLmJ3Yvriy30H2-wgBECwkoC6FAnZmiRhfhk4tvDQ_tWVmhQPb8DkEgcUgZuKtodNdlY-IcMKrj8qsmVminPbsCgdrRcr1_5v3QR1cNeU8QZYzbqXcP9lTnxd_zPMLGZA7v-VbR1eGA_UZ6YOihTYdjF9Wn3LZlCy9_mujCvKweqDQhbiBq-zlTYbDlxXOGewa2yalVzIdGVMU0ZEG49TRcJtMirYCx1NXYHR98QtqGoptg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل برای مصر
🔹
مصر ۱ بلژیک صفر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/659907" target="_blank">📅 22:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659906">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
سخنگوی کمیسیون امور داخلی مجلس و شوراها: انتخابات شوراها به دو ماه بعد از اعلام رسمی پایان جنگ موکول شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/659906" target="_blank">📅 22:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659903">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زمینه</div>
  <div class="tg-doc-extra">حمید دادوندی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/659903" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پک هیئت قرار  ویژه شب اول محرم
🖤
#محرم
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/659903" target="_blank">📅 22:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659901">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
طلا ۱۶ میلیونی هم خریدار ندارد
یوسف تقی‌زادگان، رئیس اتحادیه طلا و جواهر مشهد:
🔹
انس جهانی در حال حاضر ۴ هزار و ۳۰۰ دلار و قیمت طلا ۱۶ میلیون و ۶۰۰ هزار تومان و قیمت دلار ۱۶۲ هزار تومان قیمت‌گذاری می‌شود.
🔹
با امضای توافق‌نامه اخیر، قیمت طلا  که در روزهای اخیر ۱۷ میلیون تومان بود، روند نزولی به خود گرفته و به ۱۶ میلیون و ۶۰۰ هزار تومان رسیده است.
🔹
در حال حاضر بازار طلا در رکود به سر می‌برد؛ مردم ایران هنگام کاهش قیمت، تمایلی به خرید ندارند، اما به‌محض شروع روند افزایشی، تقاضا در بازار بالا می‌رود.
🔹
در حال حاضر پیش‌بینی می‌شود که قیمت‌ها به‌صورت موقت کاهش یابد، اما انتظار می‌رود که پس از این دوره، روند طلا دوباره صعودی شود./ اخبارمشهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/659901" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659900">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
منبع آگاه: ادعای الجزیره در خصوص عدم شمول لبنان در تفاهم‌نامه کذب است
🔹
پیگیری خبرنگار سیاسی از منابع نزدیک به تیم مذاکره‌کننده از اعمال برخی تغییرات در متن یادداشت تفاهم طی ساعات پایانی گفت‌وگوها خبر دادند.
🔹
براساس اطلاعات دریافتی، یکی از مهم‌ترین اصلاحات انجام‌شده در متن نهایی، اضافه‌شدن عبارتی با مضمون «احترام به تمامیت ارضی و حاکمیت لبنان» است که شامگاه گذشته و در جریان آخرین مراحل جمع‌بندی متن مورد توافق قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/659900" target="_blank">📅 22:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659899">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
حملات توپخانه‌ای رژیم صهیونیستی به جنوب لبنان
🔹
ارتش رژیم صهیونیستی در جدیدترین تجاوز خود به مناطق جنوبی لبنان، ارتفاعات «علی‌الطاهر» در حومه شهر نبطیه را هدف حملات توپخانه‌ای قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/659899" target="_blank">📅 22:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659898">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
انفجارهای کنترل‌شده امشب در بندر جاسک؛ شهروندان نگران نباشند
‌
🔹
طبق کسب اطلاع خبرنگار مهر، امشب از ساعت ۲۱:۰۰ تا ۲۴:۰۰، عملیات کنترل‌شده و برنامه‌ریزی‌شده‌ای در محدوده شهر بندر جاسک انجام می‌شود که طی آن صدای انفجارهایی به گوش خواهد رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/659898" target="_blank">📅 22:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659897">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFwtM-oQon6SA8w1qYRVEw9UlNGTEGLdI33AmkUjpEKAZoapRsOoxXwX8hDVEwbfHiql9KnJwLM8UPp4RKjRFFcV7TxeUUHjgBaaFo0k38t9qYPMQuCsiEz9KZNqM7FfssQxvIcUcNyLRb-rPn28Q9iuzzoPYePjZKZL_wqqEReqEFx-HqhgiAdFnenpyZDT_NTwDqBWFmwieK3uWYgRnDbFl4dNVk2W_yDnVHGd_ybwS936fRUPuzvASB7bml6kPuT4u-Ug8DeR1gxCP_oA2_OGt7Fmsi0k5a5yDHkVyElW2NmGKGJBBsqyWhQ31ML-eyadKYl4g-6a1psdOGC1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرهیز از آرزوهای طولانی
🔹
امام می‌فرماید: آرزو اگر از حد بگذرد انسان را به بدعملی می‌کشاند. امیدِ معتدل محرک تلاش و پیشرفت است، اما آرزوهای طولانی انسان را از آخرت غافل می‌کند، او را به استفاده از هر وسیله حتی نادرست وادار می‌سازد. چنانچه در دعای کمیل نیز…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/659897" target="_blank">📅 22:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659896">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKGt67Azk76ooRzuOskuAkyJaCRJzcjXMQ3EzhWcyz6VT-k2TrmUyPvPg-enioqvqE0tbArPqVn-kPxGnsvLXkv-t2VT1Gn57P-Sa7g3uJEqqQqBkpOAPB-umOKJBO5hbwVMk_AUWE1r0P6Y2IP0nbCziREt4AIl2YJIj-cWtriyXoojMo3NBuDq6B6M_X5abUdPxqHpOnJopENaWMNSKkubPGyDJnYG_gPBclr2Oz9D4nxA5mxsDacV2AWk7N9Z0VWxSPO9i9a1KKeS3MkL96xWVnqWIhj1gzISd37DvZwO_oQB6Ra3tydgfpD1Z7z4-gKjS0pJQ6NL7EvaK_0StA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ناپدید شدن مرموز جاسوس اسرائیلی | گریز در سایه بمباران اسرائیل | خالد العیدی کیست و چگونه گُریخت؟
🔹
در حالی که جنگنده‌های اسرائیلی حومه جنوبی بیروت را زیر آتش گرفته بودند و ساکنان منطقه با وحشت در حال فرار بودند، مردی از دل این هرج‌ومرج فرصتی برای گریز پیدا کرد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3223272</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/659896" target="_blank">📅 22:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659895">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e59a6bef4.mp4?token=IzCfeOPrDJCdRyL68IvPYbfEqNhz7K90DjS-h9zOFZ1tN9gA95z5ng58C_r35PjtdzjacAusKCMwi4GDR5ZOOrbl-Dkdwoh760fiYKI8bi35xXdzxIkLD1u-FFlfjiT-bfBQ4OutDPO_KHoJVHNRxKgM0r2oQNJ8wBXQS3DyrVpJqoC5tWApAiK5WSf5GVmOT_rxyBrX17nc4_iMD3ufmfNRCE1ZF0D9uO0K7Le_Xi1jMsrmWQlGVXq_SanfUgqdo9N5hDWtuKJuS8t7MX3iE5dDSAAYlUKRNgrHYkLBTGO4GOGAwQZBc5y8-iLn9yWqpAl6lYSgZrG8tDaQaluit4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e59a6bef4.mp4?token=IzCfeOPrDJCdRyL68IvPYbfEqNhz7K90DjS-h9zOFZ1tN9gA95z5ng58C_r35PjtdzjacAusKCMwi4GDR5ZOOrbl-Dkdwoh760fiYKI8bi35xXdzxIkLD1u-FFlfjiT-bfBQ4OutDPO_KHoJVHNRxKgM0r2oQNJ8wBXQS3DyrVpJqoC5tWApAiK5WSf5GVmOT_rxyBrX17nc4_iMD3ufmfNRCE1ZF0D9uO0K7Le_Xi1jMsrmWQlGVXq_SanfUgqdo9N5hDWtuKJuS8t7MX3iE5dDSAAYlUKRNgrHYkLBTGO4GOGAwQZBc5y8-iLn9yWqpAl6lYSgZrG8tDaQaluit4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازیکن دوازدهم
🔹
بعضی صندلی‌ها هیچوقت خالی نیستند؛به یاد ماکان نصیری شهید جاوید الاثر جنگ رمضان و تمام پسر بچه‌هایی که قرار بود جام جهانی را ببینند اما حالا از جایی دورتر،تماشاگر رویاهایشان هستند
#اخبارفوری_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/659895" target="_blank">📅 22:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659894">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
بنیامین نتانیاهو: «مواردی پیش می‌آید که من و ترامپ دیدگاه‌های مشترکی نداریم. آدم باید با خرد و تدبیر از منافع امنیتی اسرائیل دفاع کند #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/659894" target="_blank">📅 22:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659893">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
تهدید تازه نتانیاهو؛ «هر زمان لازم باشد اقدام می‌کنیم
🔹
ما تا زمانی که لازم باشد در «مناطق امنیتی» مختلفی که تصرف کرده‌ایم باقی خواهیم ماند تا از کشور محافظت کنیم. #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/659893" target="_blank">📅 22:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659892">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8702b068a.mp4?token=IlUgN_7Zf4b7H1N6xV02p8ts118CNK1d1n2CSoLvJ4r2q_4iSH_d5_TqED2ZoE96res7AQ4iVeuClWLw_K0cXpKYQ2djoPM-d6PeiEupQLAhacA9XWAKbvc06sKKkdoqM_FD9RZwT3IHiVxRyHwV5oWEbwN4vr6W5HJwKWxRv5KWce1K74z0CpIYMZY-BRI3mDtl-nG9tZdwtkb3K1NS1zaN9Hwv1GgeIFud4Buy9xR8PFYKMX8YtR0dxd4gfKA6vzjhujQJGeIOc9Gl7mMAC_C1ltMVDqm5JBod49AFRLX7ZZClbTzSt5ms_ohyeKGdaYjNE8i52ZyxeT4VXhdVfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8702b068a.mp4?token=IlUgN_7Zf4b7H1N6xV02p8ts118CNK1d1n2CSoLvJ4r2q_4iSH_d5_TqED2ZoE96res7AQ4iVeuClWLw_K0cXpKYQ2djoPM-d6PeiEupQLAhacA9XWAKbvc06sKKkdoqM_FD9RZwT3IHiVxRyHwV5oWEbwN4vr6W5HJwKWxRv5KWce1K74z0CpIYMZY-BRI3mDtl-nG9tZdwtkb3K1NS1zaN9Hwv1GgeIFud4Buy9xR8PFYKMX8YtR0dxd4gfKA6vzjhujQJGeIOc9Gl7mMAC_C1ltMVDqm5JBod49AFRLX7ZZClbTzSt5ms_ohyeKGdaYjNE8i52ZyxeT4VXhdVfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مذاکرات بعدی ایران و آمریکا چه زمانی برگزار می‌شود؟
عراقچی:
🔹
قرار است روز جمعه در کشور سوئیس که محل دقیق آن مشخص خواهد شد، یک دیداری بین هیئت‌های دوطرف انجام شود، که در آن روسای هیئت‌های دو طرف ابتدا این یادداشت تفاهم را امضا کنند و پس از آن اولین دور مذاکرات بعدی را داشته باشیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/659892" target="_blank">📅 22:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659891">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5234ca4dd.mp4?token=BUHIRufP4i5g-V1hjB0cZDuwR7ToG2Rfs8wO6Fmj4e54bZRp7NFt3terBvld72y4sMMICYgvhtBQbWEpppIqTqQjITGjFUmAcya1hKcsfKAqeBYUFoKEtZkCfJllWpUUGopavaxV5WbijvwW0NtK8FjWF9KH00fWX-8ZdvKkwg8MXqMm1F7HP90HDjZFrrs6S8yiTqsdwEJeBKEHpOEc1kjMbEQYZLVIj5eOuMW3vDnSXlx9Nm6cTFQEiQ4SlUqHfEVph0L3jMdt8DrFZbyQX_XCtPFcNdLMbAevIfjQ7lQEL7_FanRbhX668yh2GvDvtkRRvQ-PX4Y0OxQYzBWa1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5234ca4dd.mp4?token=BUHIRufP4i5g-V1hjB0cZDuwR7ToG2Rfs8wO6Fmj4e54bZRp7NFt3terBvld72y4sMMICYgvhtBQbWEpppIqTqQjITGjFUmAcya1hKcsfKAqeBYUFoKEtZkCfJllWpUUGopavaxV5WbijvwW0NtK8FjWF9KH00fWX-8ZdvKkwg8MXqMm1F7HP90HDjZFrrs6S8yiTqsdwEJeBKEHpOEc1kjMbEQYZLVIj5eOuMW3vDnSXlx9Nm6cTFQEiQ4SlUqHfEVph0L3jMdt8DrFZbyQX_XCtPFcNdLMbAevIfjQ7lQEL7_FanRbhX668yh2GvDvtkRRvQ-PX4Y0OxQYzBWa1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار فاکس نیوز در اسرائیل: همچنان نیروهای آمریکایی در منطقه باقی خواهند ماند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/659891" target="_blank">📅 21:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659885">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ec236e29.mp4?token=UVDL9ykymGYozK2cGtIXzlaI6nbs0Nh83lEKF3T04vHlwHJMXCnfJxW-TrpdyixvSR5F5kU7-4cRsT-CCuZicPSbrEQQdrfg-Mw_5AxDfPoTkDKGGC1or2JW0UsXovKyR5kxPuYPt_7zyC7BYDE3Xanva-e1zX6WCggcuT6Cofs3xATIzrwcIxmivcz8k0_32DcC01nbCOjG-D9wVnZDL4yPNLwYa6jCb4uhdudMOJljYfYXhX8KfU0a7DswZVT6PDjh6MujYWCH7T1XLBBrCiRGXPsyGeKOV8Z84hm-zsuMvHyh00JZGLhsZiT1FqLHkLQIQ2xyhw03V83YIoLpyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ec236e29.mp4?token=UVDL9ykymGYozK2cGtIXzlaI6nbs0Nh83lEKF3T04vHlwHJMXCnfJxW-TrpdyixvSR5F5kU7-4cRsT-CCuZicPSbrEQQdrfg-Mw_5AxDfPoTkDKGGC1or2JW0UsXovKyR5kxPuYPt_7zyC7BYDE3Xanva-e1zX6WCggcuT6Cofs3xATIzrwcIxmivcz8k0_32DcC01nbCOjG-D9wVnZDL4yPNLwYa6jCb4uhdudMOJljYfYXhX8KfU0a7DswZVT6PDjh6MujYWCH7T1XLBBrCiRGXPsyGeKOV8Z84hm-zsuMvHyh00JZGLhsZiT1FqLHkLQIQ2xyhw03V83YIoLpyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
ویژه شب اول محرم
🥀
شهر را سیاه پوش کنید ؛
صدای محرم در کوچه پس کوچه های شهر می اید…
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/659885" target="_blank">📅 21:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659884">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/351804f828.mp4?token=X-e59mHckg6dMdOZyK6aw0MeL_94FzHcroIjroNY0N_saAsceGEWTJ_3v9OcCQK4qElGd-6NLY2yVyu2IbyL341NSaRc_YqkaA8OHvzl974dn80SLvVGipj6uURGGCYZcWg8FkxD6LXeCVgYuv4dmsTL70dPgLnQ2zklWjQXoLQhoPumIJuTcjEwOX-oj6F3UEsuP1oNYqPfpLHn2ehN0gxNFw4PGgpMuEHUwmXK2bzQrpIwYGXv2jdYkn6oXPGkZCnvSlumCRhl3pUr0wlySoMopHDKAF1Hkbrj4OfNIUAzwj2Kyg6INk184TDCsBFzFTg-zrjso40Z2BTBQgMJFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/351804f828.mp4?token=X-e59mHckg6dMdOZyK6aw0MeL_94FzHcroIjroNY0N_saAsceGEWTJ_3v9OcCQK4qElGd-6NLY2yVyu2IbyL341NSaRc_YqkaA8OHvzl974dn80SLvVGipj6uURGGCYZcWg8FkxD6LXeCVgYuv4dmsTL70dPgLnQ2zklWjQXoLQhoPumIJuTcjEwOX-oj6F3UEsuP1oNYqPfpLHn2ehN0gxNFw4PGgpMuEHUwmXK2bzQrpIwYGXv2jdYkn6oXPGkZCnvSlumCRhl3pUr0wlySoMopHDKAF1Hkbrj4OfNIUAzwj2Kyg6INk184TDCsBFzFTg-zrjso40Z2BTBQgMJFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تهدید تازه نتانیاهو؛ «هر زمان لازم باشد اقدام می‌کنیم
🔹
ما تا زمانی که لازم باشد در «مناطق امنیتی» مختلفی که تصرف کرده‌ایم باقی خواهیم ماند تا از کشور محافظت کنیم.
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/659884" target="_blank">📅 21:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659883">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a83d00b039.mp4?token=q5LtDZ38SlaB_OjWQJMKE4Q87elRw9zGP56gwpfyEO_B-Zs1L0oYj_2IS1d1eyqvoNjJjIgaoyPRerGL3s7pAzZMNCeYdTuzHeCZ6UVvIIVub5QONrP_TAIL3Ch7bvKiG-2Gls3mQreBJ0Tys4KKmAXcpOEr3kU-xp84IBrAZKu4HdUsWfeM2_Jm2ZJBLMDMOgu16uEfTpnNInUnCXMLp2gWvAI7i-B9d9lb2cyXeyjJG94z5hSIhzoGu4i3gnHR7Dr_dBv6Z3gvRwwNx7xGSiyEFDLXTSSO0f973zM16hqGAa1fXqM_l7FHoDm6Eg_Cm4pRU_9XY0MtV44tKBCcPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a83d00b039.mp4?token=q5LtDZ38SlaB_OjWQJMKE4Q87elRw9zGP56gwpfyEO_B-Zs1L0oYj_2IS1d1eyqvoNjJjIgaoyPRerGL3s7pAzZMNCeYdTuzHeCZ6UVvIIVub5QONrP_TAIL3Ch7bvKiG-2Gls3mQreBJ0Tys4KKmAXcpOEr3kU-xp84IBrAZKu4HdUsWfeM2_Jm2ZJBLMDMOgu16uEfTpnNInUnCXMLp2gWvAI7i-B9d9lb2cyXeyjJG94z5hSIhzoGu4i3gnHR7Dr_dBv6Z3gvRwwNx7xGSiyEFDLXTSSO0f973zM16hqGAa1fXqM_l7FHoDm6Eg_Cm4pRU_9XY0MtV44tKBCcPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو باز هم نقش آتش‌بیار معرکه را بازی می‌کند
نتانیاهو کودک‌کش مدعی شد:
🔹
«ماموریت زندگی من مبارزه با برنامه هسته‌ای ایران است.» او همچنین تأکید کرد که «با توافق یا بدون توافق، ایران به سلاح هسته‌ای دست نخواهد یافت.»
🔹
همچنین او ادعا کرد به اقتصاد ایران خسارات عظیمی وارد کرده‌ایم؛ برخی آن را یک تریلیون دلار برآورد می‌کنند.
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/659883" target="_blank">📅 21:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659882">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
پربازدیدترین ویدیوی این روزهای یوتیوب که میلیون ها بار بازدید گرفته در مورد اقتدار ایران
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/659882" target="_blank">📅 21:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659881">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🏆
مروری سریع بر داغ‌ترین حواشی این روزهای جام جهانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/659881" target="_blank">📅 21:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659880">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
سی‌ان‌ان: یک مقام ارشد دولت آمریکا گفت که عمان در جریان مذاکرات با ایران دوپهلو و غیرصادق بوده و عملاً از نقش سنتی خود در میانجی‌گری کنار گذاشته شده است
🔹
ما از کاری که عمانی‌ها انجام دادند بسیار ناراضی بودیم، احساس می‌کردیم که آن‌ها بسیار دوگانه‌ رفتار بودند و تقریباً مثل کارمندان ایرانی‌ها عمل می‌کردند، بنابراین ما آن‌ها را تا حدی از این روند کنار گذاشتیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/659880" target="_blank">📅 21:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659879">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FL8JKl6pZFoRdXlsjJ65vFHKCsaLeWITbNxd6XQg6CVrmUe0JlJxhb5_DbnY2N7oZBmig-QYwK03q5U3tJDSigJhzgfOnihKQWIEWZK329lQU8Lx-TD9v2JbUMHnBd-L9Jr9umVQejdzX6bgMb9ONV7Z311-W-RmkZvwMNRQ7bkRjTBX7YWJCJdnNm5mJw30XUJun8vrl0-0GkvDI7-2v7lkt7SCLBaTr7Z4EPgOetM4a95EoLkQJaY22ZbErhLqo5h4DAj3alsWEdLrb4b-O28_CWUwVaW5W0ZhGMTc4gUfdWJs1tBiOcID9bMML2wouR6rb2JCCdy1IUmiH8fSog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: هدایت‌های رهبر عالیقدر بیشترین نقش را در گنجاندن بندهای صیانت از منافع ملی ایران داشته که قدردان ایشان هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/659879" target="_blank">📅 21:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659878">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPZW0mClo1AxFIhI7Q35URWbyE_R734wzvefSMXi0iH1GcziCpVZcOdaJ8prTRgVZNxhSrBwo7V_MXKjtRtIGc0ch5QxeUIkkQDyLLo0YPYtpe5ToX7I9ULQPOPIIe4W4VuHiCUfMG9nesWJdkGeEmQiLOLqcjsVN8vWXSmXCyXV1AYd9aOcAFfecO5I80Z4HzB7608yDXsKzTiLG4cBaQKmvNvxxeIyqgxPO51tbrx3AuECyrrnA_xKakN-VCyoP6uJFSnG5oMY968EAW6TM6A9dbqRxjTsyY-5nyO-xqbUQNvKe7_aciV2VKA_dqlGbWrHNEc4mlp6UXtlZ52rDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسن‌ترین تیم‌های جام جهانی کدام کشورها هستند؟
🔹
پاناما تنها تیمی است که میانگین سنی بازیکنانش به ۳۰ سال رسیده است.
🔹
ایران نیز در میان باتجربه‌ترین تیم‌های جام جهانی ۲۰۲۶ در رده دوم مسن‌ترین‌ها قرار گرفته است.
🔹
حضور کشورهایی مانند کلمبیا، قطر و برزیل در این فهرست نشان می‌دهد بسیاری از مدعیان، همچنان به ستاره‌های باتجربه خود اعتماد کرده‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/659878" target="_blank">📅 21:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659877">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
اردوغان: توافق ایران و آمریکا راه را برای صلح در جهان باز می‌کند
🔹
رئیس‌جمهور ترکیه با استقبال از توافق میان ایالات متحده و ایران، آن را گشاینده راه صلح در منطقه و جهان دانست و از تلاش‌های پاکستان، قطر و عربستان برای تحقق این توافق قدردانی کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/659877" target="_blank">📅 21:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659875">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
شبکه ۱۳ رژیم صهیونیستی به نقل از برخی منابع: گفت‌وگویی پرتنش میان نتانیاهو و جی‌دی ونس درباره لبنان
‌
🔹
ونس خواستار عقب‌نشینی تدریجی از لبنان شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/659875" target="_blank">📅 21:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659874">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
عضو ناوگان صمود: در زمان بازداشت مورد تجاوز جنسی قرار گرفتم  جولیت لامونت، مستندساز استرالیایی و عضو ناوگان صمود:
🔹
در جریان توقیف و بازداشت توسط ارتش اسرائیل در ماه مه، وقتی دستبند و پابند داشته، داخل یک کانتینر تاریک توسط یک سرباز اسرائیلی مورد تجاوز…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/659874" target="_blank">📅 20:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659873">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0fcd76c0.mp4?token=HFPXDKz7EbQ_RQjy_-asXe0byXTwdutUYLlm9udly4J_8w7lm8C1n-RIuGrummu4T00q-wlRZMdRV2KXPHRBswe103aItMxy1Um1h6uf9-LK06PC8KgpoMKbGRDCU8u5FNVf611WVBoS-N8swz-IEKbPG2sqJ4gCxnxNHG8LXADG3A7gW6ABIsd4J5Ay4mfPYS6srlzniH4H2MIJOsFidjUVeNcsgGjez2-t8okCmnnj5mFiCk1Ed4Of9famlmrecCWjlQWELLlFQC1DO2qeuEHaDI6iDLfae-IUHSS58D3fnwuCQ-Ra0DKhkSQXMa4qx06vlQ7gCETQQxZUvxYwEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0fcd76c0.mp4?token=HFPXDKz7EbQ_RQjy_-asXe0byXTwdutUYLlm9udly4J_8w7lm8C1n-RIuGrummu4T00q-wlRZMdRV2KXPHRBswe103aItMxy1Um1h6uf9-LK06PC8KgpoMKbGRDCU8u5FNVf611WVBoS-N8swz-IEKbPG2sqJ4gCxnxNHG8LXADG3A7gW6ABIsd4J5Ay4mfPYS6srlzniH4H2MIJOsFidjUVeNcsgGjez2-t8okCmnnj5mFiCk1Ed4Of9famlmrecCWjlQWELLlFQC1DO2qeuEHaDI6iDLfae-IUHSS58D3fnwuCQ-Ra0DKhkSQXMa4qx06vlQ7gCETQQxZUvxYwEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: سعی می‌کنیم از تفاهم ایجاد شده راهگشایی اقتصادی ایجاد کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/659873" target="_blank">📅 20:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659872">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
آیت‌الله سیستانی، چهارشنبه را اول محرم اعلام کرد
🔹
دفتر آیت‌الله سیستانی، مرجع عالیقدر شیعیان با صدور اطلاعیه‌ای اعلام کرد روز سه‌شنبه، مکمل ماه ذی‌ الحجه بوده و  بدین ترتیب، روز چهارشنبه، نخستین روز از ماه محرم‌الحرام سال ۱۴۴۸ هجری قمری خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/659872" target="_blank">📅 20:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659871">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ادعای
مقامات آمریکایی: آماده کاهش تحریم‌ها علیه ایران هستیم
شبکه cnn به نقل از مقامات ارشد دولت آمریکا:
🔹
آماده انجام گام‌هایی برای آغاز کاهش تحریم‌ها علیه ایران هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/659871" target="_blank">📅 20:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659870">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
افزایش کالابرگ دهک‌های پایین تا دو هفته آتی
‌
وزیر امور اقتصادی و دارایی:
🔹
افزایش مبلغ کالابرگ دهک های پایین تحت پوشش کالابرگ در دستور کار قرار دارد و وزارت اقتصاد در حال آماده‌سازی پیشنهاد خود برای ارائه به دولت است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/659870" target="_blank">📅 20:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659869">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
نجات از دو موجود وحشتناک با توسل به حضرت رقیه و ....
🔹
00:04:30 فشار مالی مرا از خدا دور کرد
🔹
00:07:50 لحظه نشستن روی کاناپه لحظه ورود به برزخ شد
🔹
00:15:20 رؤیت نوع عذاب غیبت‌کنندگان
🔹
00:21:00 اعمال خوبی که انجام دادنش فایده و ثمره‌ای نداشت
🔹
00:31:40  عذاب وحشتناکی که از جهت بداخلاقی با خانواده ام متحمل شدم
🔹
00:44:20 توسل به حضرت رقیه(س)
🔹
01:06:35 به جا ماندن کبودی سیلی برزخی بر کالبد دنیایی
🔹
قسمت چهاردهم (دخترم)، فصل چهارم
🔹
#تجربه‌گر
: علیرضا غلامی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/659869" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659868">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
صدراعظم آلمان: توافق ایران و آمریکا باید شامل لبنان نیز شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/659868" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659867">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حقایقی از تیم ملی ایران که شاید تا به امروز نمی‌دانستید!
🔹
تیم ملی در آستانه اولین دیدار خود در جام جهانی است
🔹
در این ویدیو نکات بسیار جذابی را از تیم ملی خواهید دید که شاید تا به حالا نشنیده باشید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/659867" target="_blank">📅 20:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659866">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba82007ab0.mp4?token=oo45OzgVlTTZZ1g7Ovg6hNxonQyx_3VED48CO1TN8NGj9n-ooNRUch2M3ptIVo1hpk3sS-1vQegw1klflNGsBl6QQm3eQ-0_bChwW15iyEpuM-X_jziHpZK0SVsgaznlKWcl_ggT6E16q8Dmwd2kA-JRtxJv25-fSUJF2GZHGuwDaN0dtO3L8ZwjKDVr5ZA0MMsNZ8f7QBaosK_jWDdbcXTWIxbeKThSRdQwzU0T8OFmnc6JtiLHx18VemMkAThwgmlZ6m_0SlhZzOkzwqxfXixhxEG5iF04G1UGvGCWzkdc-PQ87stPEFYJb-zJWH2nIsCjezSGET6onnekWKnfsqj9TtM2mI3JQVp9iBvjiVp8Cu6yzIASO_UJGuP9ayKXeeDltJ5TxgbSWUZuWGLa--YZ7VUCxdcXaednEzRRuMlINp5OeO4pJsPMimD0rXbocsRmIlRA65iAgQv9Ixlw10doRmAGzcSekZTz3xblYxiPzwr4PROJy_tmuJDi3Qsf9XdCgSoE-mEjWlWzjKXyav7duko5VSJ_U5cfgzSQtShZACPeh1but8XkYXsTwdktCcjz8FwnPeZIrDHnzokPKyf7tSBzjCiMttV96TwNaq1hXyTYafWl_halhEAS8rEicVd8KaK-XsWIAVH11hP5fpizWxysq4OASrcVM0flrBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba82007ab0.mp4?token=oo45OzgVlTTZZ1g7Ovg6hNxonQyx_3VED48CO1TN8NGj9n-ooNRUch2M3ptIVo1hpk3sS-1vQegw1klflNGsBl6QQm3eQ-0_bChwW15iyEpuM-X_jziHpZK0SVsgaznlKWcl_ggT6E16q8Dmwd2kA-JRtxJv25-fSUJF2GZHGuwDaN0dtO3L8ZwjKDVr5ZA0MMsNZ8f7QBaosK_jWDdbcXTWIxbeKThSRdQwzU0T8OFmnc6JtiLHx18VemMkAThwgmlZ6m_0SlhZzOkzwqxfXixhxEG5iF04G1UGvGCWzkdc-PQ87stPEFYJb-zJWH2nIsCjezSGET6onnekWKnfsqj9TtM2mI3JQVp9iBvjiVp8Cu6yzIASO_UJGuP9ayKXeeDltJ5TxgbSWUZuWGLa--YZ7VUCxdcXaednEzRRuMlINp5OeO4pJsPMimD0rXbocsRmIlRA65iAgQv9Ixlw10doRmAGzcSekZTz3xblYxiPzwr4PROJy_tmuJDi3Qsf9XdCgSoE-mEjWlWzjKXyav7duko5VSJ_U5cfgzSQtShZACPeh1but8XkYXsTwdktCcjz8FwnPeZIrDHnzokPKyf7tSBzjCiMttV96TwNaq1hXyTYafWl_halhEAS8rEicVd8KaK-XsWIAVH11hP5fpizWxysq4OASrcVM0flrBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لغو تحریم‌ها بستگی به رفتار ایران دارد و فوری نخواهد بود
🔹
خبرنگار:  آقای رئیس جمهور، آیا این توافق شامل لغو زودهنگام تحریم‌ها برای ایران می‌شود؟ این لغو زودهنگام از چه زمانی اجرایی خواهد شد؟
🔹
ترامپ:  نه، اجرایی نمی‌شود. این واقعاً مرتبط با رفتار (ایران)…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/659866" target="_blank">📅 20:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659865">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4cb986925.mp4?token=EPgD66i1hdUTGt1fH1fdaO4KbWTnUgCIsIgr9vUoKLou4dMsqCGBouJbcio--LUpMiSVVuEDYzDCzTKC3FrlAVd94ljR19uJ1CoU16bKsvtidZUx7DnFhTyvoFE9qR9wIx0EDPc9Tj2i8L4tcl22vmzozmBWP-F32YVPbDGSTfUaV-Q-6paF6ANSgoXsnPwChN1A04v8uFVai9C5OWQY9cSsPwbTQL-QBz2Mbl_QF5ZRfQRE8kVGFH_aZwT0A5vSAtIdNzdkm7_Z88_oE5djRoUeBuiCIenoe0lxapzYie2-aQHaiTo2FtPwRG0L2ubXe5bYEf0SqtbhPe3u-etM5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4cb986925.mp4?token=EPgD66i1hdUTGt1fH1fdaO4KbWTnUgCIsIgr9vUoKLou4dMsqCGBouJbcio--LUpMiSVVuEDYzDCzTKC3FrlAVd94ljR19uJ1CoU16bKsvtidZUx7DnFhTyvoFE9qR9wIx0EDPc9Tj2i8L4tcl22vmzozmBWP-F32YVPbDGSTfUaV-Q-6paF6ANSgoXsnPwChN1A04v8uFVai9C5OWQY9cSsPwbTQL-QBz2Mbl_QF5ZRfQRE8kVGFH_aZwT0A5vSAtIdNzdkm7_Z88_oE5djRoUeBuiCIenoe0lxapzYie2-aQHaiTo2FtPwRG0L2ubXe5bYEf0SqtbhPe3u-etM5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایرانی‌ها نظارت قوی بر تأسیسات هسته‌ای را پذیرفتند  ترامپ در دیدار با مکرون:
🔹
آنها کاملاً با این موضوع موافقت کردند و با قدرت‌های نظارتی قوی، سلاح هسته‌ای نخواهند داشت، که دلیلش هم همین بود، چون اگر سلاح هسته‌ای داشتند، احتمالاً از آن استفاده می‌کردند.
🔹
و…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/659865" target="_blank">📅 20:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659864">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed953f1774.mp4?token=Hi4hdiq20J5KVvfi-9zMOnIiV67WqKc78kTT3o4QXb5jPXHHrQzXwX9LmLYEMRa5ufFzgoda67DSjx-hDhLenBxITvibJPIoQ1sM1jW7STVSxpyw2-nEaPn20jFnS874avjB09oSt0EM-RJDlYhodwCRfveoNMiHztoUnTP6ImuDBycTeZtzfHFAd29dBmzA528uak5W9mBfWZmRnF4eKzqTK2kqutPr_vTYBP535GxfxwbLM6uXlihkEz7jSMr35uBhmQ3nkQXHhIxapQgMWORLkdOXr5nhTNSQbgu8mkeGkjAKMyIBYhM2fC7ByyslrDIaq-nOCuNMNO-9jjXBow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed953f1774.mp4?token=Hi4hdiq20J5KVvfi-9zMOnIiV67WqKc78kTT3o4QXb5jPXHHrQzXwX9LmLYEMRa5ufFzgoda67DSjx-hDhLenBxITvibJPIoQ1sM1jW7STVSxpyw2-nEaPn20jFnS874avjB09oSt0EM-RJDlYhodwCRfveoNMiHztoUnTP6ImuDBycTeZtzfHFAd29dBmzA528uak5W9mBfWZmRnF4eKzqTK2kqutPr_vTYBP535GxfxwbLM6uXlihkEz7jSMr35uBhmQ3nkQXHhIxapQgMWORLkdOXr5nhTNSQbgu8mkeGkjAKMyIBYhM2fC7ByyslrDIaq-nOCuNMNO-9jjXBow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: تنگه هرمز تا حدی باز شده است   ترامپ در دیدار با مکرون:
🔹
تمام توافق امضا شده است، تنگه هرمز از قبل تا حدی باز شده است.
🔹
آنها در حال جستجوی کمی برای یافتن چند مین هستند. کشتی‌ها اکنون شروع به حرکت کرده‌اند. روز جمعه، تنگه کاملاً باز خواهد شد.…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/659864" target="_blank">📅 20:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659863">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HD4DUXja9MPDxWSVUuQhcq5ZDhl-yhHWA1ruStERppKcdvK_j7swlSy5t6N6Rjq7ez--RGNJob4p1MJvGfI1vAvPlL3jpz_7TnslnBP3CKco0qoY0ngFfXVV94f25TcLcXRDNGl6mCA2HqsA7esddVdPpgp3Ci1PPKjl5An7xsXkiMDL75Y-zQ9CyK3miUPb8cT8lXV9gIbXNKJMCLRLhgphzaMcSwBieiU8kllAKdbuOVdav6LYjgtluzdgwqzmvNcm-f7VfRza-6a-54rXxOWRWnD1g6k6YxBU_Z69qcIO-TQTi-d-TfvdhfPleKrmiXzga6hWu8DcCyMKAq7T_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود بازار آنلاین طلا به مقیاس تازه؛ پرمخاطب‌ترین اپلیکیشن خرید و فروش طلا ۲۵ میلیونی شد
📊
بازار آنلاین طلا در ایران طی سال‌های اخیر با رشد قابل‌توجهی همراه بوده و حالا
میلی به‌عنوان یکی از بازیگران این حوزه اعلام کرده که در کمتر از سه سال به ۲۵ میلیون
کاربر رسیده است.
🔸
براساس داده‌های اعلام‌شده از سوی میلی هر کاربر از زمان راه‌اندازی این اپلیکیشن تاکنون
به‌طور میانگین چهار نفر از دوستان یا آشنایان خود را به استفاده از خدمات میلی دعوت کرده است
؛ آماری که می‌تواند نشانه‌ای از افزایش اقبال کاربران به خریدوفروش و پس‌انداز آنلاین طلا باشد.
🔹
میلی در تلاش است تا طلا را وارد زندگی روزمره کاربران کند. برای همین در کنار امکان خریدوفروش و پس‌انداز طلا سرویس‌هایی مانند «خرید قسطی طلا» و «دریافت وام خرید کالا به اعتبار طلا» را نیز به سبد خدمات خود اضافه کرده است. به همین علت تاکنون کاربران زیادی تجربه استفاده از خدمات میلی را با یکدیگر به اشتراک گذاشته‌اند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/659863" target="_blank">📅 20:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659861">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HmXzJyGfFBTRdGL7TA5JGb4AN9JqAYHRc8Uy62WmGCWYxmlEQAaaHYb3Txlba1tfy3_Fx4CxjqXg1NFd6Fu1cAu5JbW4mSHIsjfjplnGRsPGN4xfMY74oz-P-yfHOFvmzYMYfQzA7C18daq1v--208Kh7nXXmeVErKZjEawfVeBfeJT0UVaLOk1QEhws6cYr8TjyVQUcnwyZR2l2-5Lqkblu-jR3bZWtcxAJDkpqCDzJIfLGUrVMwX-rJ-LWwXt0L2Y0weJIui1ec3CAJWV60dnxakgU8L3hR34r6hjEShJcltXEqFqZPHrSPPLmexlQuWM0CytCgxVKTGlU7z4Nfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qH1473XOKiPhwaMlgpVE4M3yGkHUXJXYjUPBx3DUI6XPzd_XzEua8WS9C09IUIIDfmE-q4MHNJXz1tlnCxcDc_fbKQ6aaTSvrkfvnB9Hnn4oVcRkiu8NPF5DUsxGEEQqiWgww2vLdY-nLbZhkg5RzpCZGFhynuB0M17zuK_Cd-5_L3AG5boe9e3P8Dl2BQoPbqt2kwHOjKJlpZ0Q2dRqaeHjcFW7jfrBV6lZukDpyFfZzzmv2Z96KAwK4ZJ5hm53IY9LMAX6qm8sYTx19f4RsCEGfArZdEI-iZOmcRSit57sDkSi54RinvIb0qzkhWy_JRGEoLtK59nLi8sKA8aUsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📚
نام کتاب: حسین از زبان حسین (ع)
🖋
نویسنده: محمد محمدیان
🔹
این کتاب روایتی متفاوت و اثرگذار از زندگی امام حسین(ع) است که حوادث را از زبان خود آن حضرت بازمی‌گوید و از ولادت  تا شهادت را با نثری روان و مستند پیش می‌برد.
🔹
برای کسانی که به دنبال آشنایی عمیق‌تر…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/659861" target="_blank">📅 20:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659860">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0c3dfd0d6.mp4?token=fo8ZvvdhHOHzZCGAzPAPuA1uhbcGSnXD4NyUiyn-AiuPJh6eu64Lx6JxfxGqI7hlJBGNVOr0R_VzQre3tPL1gWGGTPSBWKTa2cwhu8n_jBQLD3O78urWAM-jlbLFv9U6VcpJwbJXBq96lOdiHXYA7JRcc6H9cjWMNj2dmtycp3-xzZL8v9zpQS0IYskU1wIt1FGZIjvlTP6b6TK3TGZ8eYSeSOadNjYx15nKKkqURWr1OmH-S69Zc_oe-HrOnF66raL9km8ty6h6SXsPVkgqXUKP1m7qs8cI3uhzxGy60mszqGpzXgZcto7JrqIUY-guAEIeW8fI5MBnq9XpQstFWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0c3dfd0d6.mp4?token=fo8ZvvdhHOHzZCGAzPAPuA1uhbcGSnXD4NyUiyn-AiuPJh6eu64Lx6JxfxGqI7hlJBGNVOr0R_VzQre3tPL1gWGGTPSBWKTa2cwhu8n_jBQLD3O78urWAM-jlbLFv9U6VcpJwbJXBq96lOdiHXYA7JRcc6H9cjWMNj2dmtycp3-xzZL8v9zpQS0IYskU1wIt1FGZIjvlTP6b6TK3TGZ8eYSeSOadNjYx15nKKkqURWr1OmH-S69Zc_oe-HrOnF66raL9km8ty6h6SXsPVkgqXUKP1m7qs8cI3uhzxGy60mszqGpzXgZcto7JrqIUY-guAEIeW8fI5MBnq9XpQstFWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: شاید بتوانیم در مورد اوکراین کاری انجام دهیم. فکر می‌کنم هم پوتین و هم زلنسکی برای آن آمادگی دارند
🔹
حالا که ایران تمام شده، قرار است روی آن تمرکز کنیم #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/659860" target="_blank">📅 20:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659859">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
متن تفاهم‌نامه با ایران به زودی منتشر می‌شود
🔹
خبرنگار:  متن تفاهم‌نامه چه زمانی منتشر خواهد شد؟
🔹
ترامپ:  فکر می‌کنم خیلی زود. منظورم این است که می‌خواهم منتشر شود. این یک سند قدرتمند است. مثل سند اوباما نیست که فقط یک سند وحشتناک بود #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/659859" target="_blank">📅 19:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659858">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
عضو کمیسیون بهداشت مجلس: افزایش حقوق و متناسب‌سازی، نشانه ایفای تعهدات قانوی تأمین اجتماعی است
🔹
احمد آریایی‌نژاد، عضو کمیسیون بهداشت و نماینده مردم ملایر، با اشاره به افزایش حقوق بازنشستگان و اجرای متناسب‌سازی گفت: این اقدامات نشان‌دهنده ایفای تعهدات سازمان تأمین اجتماعی در قبال بازنشستگان است؛ موضوعی که در شرایط جنگ و بحران اقتصادی اهمیت دوچندانی پیدا می‌کند.
🔹
وی با تأکید بر اینکه متناسب‌سازی گامی در جهت عدالت و حفظ قدرت معیشتی بازنشستگان است، افزود: دولت و مجلس باید برای تأمین منابع پایدار و استمرار این مسیر، حمایت‌های لازم را از تأمین اجتماعی به عمل آورند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659858" target="_blank">📅 19:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659857">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdbba1879c.mp4?token=GzViGW0t00wsnzHtC2k7HC0kgxgPxCyJu3aMRyAzbz--t8v8Ghc14T1h17_i2shV2TN1KNSNoO2vc63DDkjGvVks4JyaeUP3geR6cY17GnHOdqf63xLbZx3NqNhro3vB3LPACzSNL7q2TpG_i7rKo_wlMnn6B2q9IwYgPxJQUXcDUapu2s099ORGu5ghLs8OdnkpT_WVbpA-EfBBfArZlO57S8LMG-Tb3IyJnF_ICK3IJsIs3moK1tR0BzjD5hAh9cn_BzINPYGyp7G1kxqfw8jEqah1nrYPxZDaKG04CoI2Wpq9GMiIeEOkaj2QIeo1rEKdsnOH_kL-uy_yqhC_XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdbba1879c.mp4?token=GzViGW0t00wsnzHtC2k7HC0kgxgPxCyJu3aMRyAzbz--t8v8Ghc14T1h17_i2shV2TN1KNSNoO2vc63DDkjGvVks4JyaeUP3geR6cY17GnHOdqf63xLbZx3NqNhro3vB3LPACzSNL7q2TpG_i7rKo_wlMnn6B2q9IwYgPxJQUXcDUapu2s099ORGu5ghLs8OdnkpT_WVbpA-EfBBfArZlO57S8LMG-Tb3IyJnF_ICK3IJsIs3moK1tR0BzjD5hAh9cn_BzINPYGyp7G1kxqfw8jEqah1nrYPxZDaKG04CoI2Wpq9GMiIeEOkaj2QIeo1rEKdsnOH_kL-uy_yqhC_XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اولین هیجان و اولین قدم یوزهای ایرانی در جام جهانی پیش‌بینی جام تایم از بازی نخست تیم ملی در برابر نیوزلند
🔹
قسمت دوم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/659857" target="_blank">📅 19:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659856">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df1985986c.mp4?token=DAffNYQsow9ra9g8kTcLoJmKAWB60F_HG7G4p5xkC6pPbkyF22PxcO6TRrQpfYxmV9tZ0cdR78aW90njdizgvmyJMGLhx-YowKjGbN2WoYBe_ROTpDf_kPRopqQ7e7NJcpzqadxguxvJaqC7k1HLSNT8S28ZeIshYmOGk7Q4allZWsggkduZgs5Fjcb4KE_kPSGForyCOsI_En7FRjC1FR1W-NkTjCjtpkJDtP1A338AA9R9eV1ZyFrs4NDRIu_YdBWMO3mMzhHHBrtdAY6CQqYZrNKsPt_4hpLW2KgVXuo-HHDWhITdScg8-yW8LbkII9mHfZaAkX23yXiYwMZNDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df1985986c.mp4?token=DAffNYQsow9ra9g8kTcLoJmKAWB60F_HG7G4p5xkC6pPbkyF22PxcO6TRrQpfYxmV9tZ0cdR78aW90njdizgvmyJMGLhx-YowKjGbN2WoYBe_ROTpDf_kPRopqQ7e7NJcpzqadxguxvJaqC7k1HLSNT8S28ZeIshYmOGk7Q4allZWsggkduZgs5Fjcb4KE_kPSGForyCOsI_En7FRjC1FR1W-NkTjCjtpkJDtP1A338AA9R9eV1ZyFrs4NDRIu_YdBWMO3mMzhHHBrtdAY6CQqYZrNKsPt_4hpLW2KgVXuo-HHDWhITdScg8-yW8LbkII9mHfZaAkX23yXiYwMZNDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متن تفاهم‌نامه با ایران به زودی منتشر می‌شود
🔹
خبرنگار:
متن تفاهم‌نامه چه زمانی منتشر خواهد شد؟
🔹
ترامپ:
فکر می‌کنم خیلی زود. منظورم این است که می‌خواهم منتشر شود. این یک سند قدرتمند است. مثل سند اوباما نیست که فقط یک سند وحشتناک بود
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/659856" target="_blank">📅 19:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659855">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e99fa9a3b.mp4?token=a1pKquKEQoac7Q8x6-X16-2eE2c5p_x1HW-QKvkuIyW3cP3GFGUnsRPjpwBux-qcVafU8MaET6w_RYW63emw13jAAcOtTXbyxJBVc8j2ARrc_BPFGBnCS4DgQeBLnIQwiuKEH_KCxQ5AnxpcrUfRUIH5P91FQzb-_q49m9lF2xTFFRzymDCRv8RxRXwaANrCj9p5Gdidrs8nGBAtbhKGhtgMcp5lcqOLPbD3EnW2P_ynWF3_2FpCHEm8IxkFoCnMhp1FyJRZ23Iu67HLjuUngutgEvJ9S1ELjmNkK7WHaO4x2fEU3Lflyqq95WkSNqf6MqIianR6LEqYR5jSV5DOvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e99fa9a3b.mp4?token=a1pKquKEQoac7Q8x6-X16-2eE2c5p_x1HW-QKvkuIyW3cP3GFGUnsRPjpwBux-qcVafU8MaET6w_RYW63emw13jAAcOtTXbyxJBVc8j2ARrc_BPFGBnCS4DgQeBLnIQwiuKEH_KCxQ5AnxpcrUfRUIH5P91FQzb-_q49m9lF2xTFFRzymDCRv8RxRXwaANrCj9p5Gdidrs8nGBAtbhKGhtgMcp5lcqOLPbD3EnW2P_ynWF3_2FpCHEm8IxkFoCnMhp1FyJRZ23Iu67HLjuUngutgEvJ9S1ELjmNkK7WHaO4x2fEU3Lflyqq95WkSNqf6MqIianR6LEqYR5jSV5DOvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای ایران
🔹
در آستانه اولین بازی تیم ملی فوتبال ایران، مخاطبان خبرفوری با ارسال پیام‌های صوتی، به ملی‌پوشان انرژی و انگیزه دادند.
🔹
این ویدیو، بخشی از پیام‌های صوتی مردم برای ملی‌پوشان است؛ صداهایی از جنس امید، عشق و حمایت.
🔸
شما هم با صدای گرمتان انرژی بخش ملی‌پوشان باشید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/659855" target="_blank">📅 19:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659854">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پیراهن شهرم رنگ مشکی داره</div>
  <div class="tg-doc-extra">مداحی آنلاین</div>
</div>
<a href="https://t.me/akhbarefori/659854" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎼
پیراهن شهرم
رنگ مشکی داره
آماده‌ی کاره
هر کی عشقی داره
🎙
حسین_طاهری
#زمینه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/659854" target="_blank">📅 19:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659853">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bebc4fb1c.mp4?token=EZLgzO4izghBfyZfnqlcWRDdTblAdxJfSBJ9vUCH7if9NajyaF3w80BVarYxL5rm3pY69nhJn-jPXIRkkXiVfyDW5muzXTMBxHwY-Kk5Qj1pPNa1HVBCJJSt2Jjcoq4u6puyaT7fBBrDir47buMDK4Y_1xJ6USVeyM-YQSiz6BhMdURikPj8RAE4rqihODG4_z2GIKymjY2mka4VJF10ir47xRzSYlRHlKt-B2TrDMA7-ILUgKb5pdu_q-NlpdenF9csZfO4Ubrg6HTYoGuJWTqQj0tehdDFNFl2asWi4sJp1W0nr5j4On_zv0jQtmSg21YVNhELpWeztLUSVMeVoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bebc4fb1c.mp4?token=EZLgzO4izghBfyZfnqlcWRDdTblAdxJfSBJ9vUCH7if9NajyaF3w80BVarYxL5rm3pY69nhJn-jPXIRkkXiVfyDW5muzXTMBxHwY-Kk5Qj1pPNa1HVBCJJSt2Jjcoq4u6puyaT7fBBrDir47buMDK4Y_1xJ6USVeyM-YQSiz6BhMdURikPj8RAE4rqihODG4_z2GIKymjY2mka4VJF10ir47xRzSYlRHlKt-B2TrDMA7-ILUgKb5pdu_q-NlpdenF9csZfO4Ubrg6HTYoGuJWTqQj0tehdDFNFl2asWi4sJp1W0nr5j4On_zv0jQtmSg21YVNhELpWeztLUSVMeVoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باز بوی غم ز کوی محرم رسیده است
دل‌ها به یاد غربتِ مظلوم تپیده است
آغاز ماه ماتمِ سلطان کربلا
بر عاشقانِ حضرتِ ثارالله تسلیت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659853" target="_blank">📅 19:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659852">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ترامپ درباره ایران: اتفاقات بسیار خوبی در خاورمیانه رخ خواهد داد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/659852" target="_blank">📅 19:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659851">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piwoKu97DzUuWvmBDX_XUvjTjYSnOzvVx_zD13plhZ4IomrkcUVJejuPW-yQyT9OzUnfG3y5DGBlFA3DFGo4n6Lh9WPXS0re6tqn8D-p38VAWeKks7d34ShzCuh_xgRRiDrC-ixUjQJ_XlreFwQpqADKYN7Bqj58QuwqPmg0l0blz8kaoPFDwOdTQ44sy7nOBoiwjJ3KNE0yG1GIjGitpmagywVS43mzugNv0fvN3YpKApkK7RFtcObmCBl-3Qm3yzcRURLXr700tEan4POS3aIBWu208AjaiBNQhSftaSnUkPlDSx2VRZqrLUDX1iTSH_88nTNNGFm8RPmDQlvRNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحویلِ سال به وقتِ مُحَرّم است؛
حَوّل قلُوبَنا بِبُکاءِ عَلَی الحُسَین ...
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/659851" target="_blank">📅 19:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659850">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
نخست وزیر پاکستان: تفاهم آمریکا و ایران پیروزی برای صلح و دیپلماسی است
شهباز شریف:
🔹
توافق آمریکا و ایران پیروزی برای صلح و دیپلماسی است؛ ما روز جمعه میزبان مراسم امضای این توافق در ژنو خواهیم بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/659850" target="_blank">📅 19:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659849">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
دیروز تولد قاتل ۱۶۸ کودک معصوم بود
🔹
فرشته هایی که پیکرشان هم پیدا نشد صحبت هایی با قاتلشان دارند...
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/659849" target="_blank">📅 19:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659848">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
پیش فروش بلیت‌ قطارهای مسافری تیرماه از روز چهارشنبه
🔹
پیش فروش بلیت‌ قطارهای مسافری برای بازه زمانی ۱ تا ۳۱ تیر (مسیرهای رفت تا تاریخ ۳۱ تیر و مسیرهای برگشت تا تاریخ یکم مرداد ۱۴۰۵) از روز چهارشنبه ۲۷ خرداد آغاز می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/659848" target="_blank">📅 19:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659847">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNi6fwGjcygBA96owYOG2Znxzu36atWOFNRTmPWK0vnoV7UfwD3Xjq9kJSQPK8W-cR5LtBzxTqrBZIuVxgAwXiTvOfV0DuajuxhFW1YyVFTKg-6ATxYEcfykc9iqHsdJCNs0pipre212746mlssuq9IcMUSPt04l6X3jvhcbI5uWGmfMnFifxJ6jTPoGIW3SXSnkmfRCVKb7UGOOxLNzSOIiDUsQVJqaMqkKFeaY6p45MjW3T6YpF8e1tTjKaGp9DorjZVhxTSMNzajiJsgxVYoNkqPlCUaOtmmCv2E2cGa8g63ehOo9VsLNRbzy_5mhItMV1lpi-MvyT1mtBx-2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: با مقاومت تاریخی ملت و رشادت نیروهای مسلح، ایران گامی بلند به سوی پیروزی نهایی برداشت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/659847" target="_blank">📅 19:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659846">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3953919e97.mp4?token=b2NnEZ7O3VL9-UfFpVaVZ8zFSjWpTukq5XrucuG-tQVj_i9xTM8xwFVx1kHsDYNg89XLw--ZBHIZ2bXXf77PpyKPUc7pFntwjq87Oh-scwB4WRUbhGTYa7xEDLwtxVNDP4Y37Yx20AA7r_Q9b_rmjisRolAvmDD31dh7RLYDvKF07AQ9y5H_-Y4gC5dDxN15DkSQHYJMJpaz5uUcOwWsLV3xksRqsUEzrOCKfAqddl4UEub0GP8N1T3IDcMQW-r4sop564ZL7s_nvw77vA70AVUyFxzpf5-yNebkUyzyas8gpwiWEMYe5Mw5G5eGIDoiVWQl_Vg5u36ydy0Z0Zhb7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3953919e97.mp4?token=b2NnEZ7O3VL9-UfFpVaVZ8zFSjWpTukq5XrucuG-tQVj_i9xTM8xwFVx1kHsDYNg89XLw--ZBHIZ2bXXf77PpyKPUc7pFntwjq87Oh-scwB4WRUbhGTYa7xEDLwtxVNDP4Y37Yx20AA7r_Q9b_rmjisRolAvmDD31dh7RLYDvKF07AQ9y5H_-Y4gC5dDxN15DkSQHYJMJpaz5uUcOwWsLV3xksRqsUEzrOCKfAqddl4UEub0GP8N1T3IDcMQW-r4sop564ZL7s_nvw77vA70AVUyFxzpf5-yNebkUyzyas8gpwiWEMYe5Mw5G5eGIDoiVWQl_Vg5u36ydy0Z0Zhb7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس: ما آمادگی کامل داریم تا کشورهای عضو شورای همکاری خلیج فارس، سرمایه‌گذاری‌های گسترده‌ای در فرآیند بازسازی ایران به عمل آورند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/659846" target="_blank">📅 19:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659845">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ed1fbc1e1.mp4?token=syPp_P1ECPTXdnFrUySqzv0lBoZFoX_hk11UE_S4gFCnPhWQCIhUMVYCkyCNCWhN_EwItNpsxlorjmcj8Hs-omnq_nKIYR8jIaLie3ETRFhadQTxSbOAzlzRYPH5fV2ztCIYNdaGZbDUlP4KNyw-ZatJDYsBzu-HCq7bYQ6hunL7R2mi2k3mKrajPctbinCe6_voMbzZ0LtiAEkZiZxrTdvl54ZzHPBEXPVe5F3JUVMif0EvtEO0FHMO4xEVV0ivR_DTuGFY344XSopiXa2Qomw20ApoqDw-FJRvVaQWxrlNp3--cN0a95Mho4Oblfmb5KhfnddRtKK4ZdriJv_f5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ed1fbc1e1.mp4?token=syPp_P1ECPTXdnFrUySqzv0lBoZFoX_hk11UE_S4gFCnPhWQCIhUMVYCkyCNCWhN_EwItNpsxlorjmcj8Hs-omnq_nKIYR8jIaLie3ETRFhadQTxSbOAzlzRYPH5fV2ztCIYNdaGZbDUlP4KNyw-ZatJDYsBzu-HCq7bYQ6hunL7R2mi2k3mKrajPctbinCe6_voMbzZ0LtiAEkZiZxrTdvl54ZzHPBEXPVe5F3JUVMif0EvtEO0FHMO4xEVV0ivR_DTuGFY344XSopiXa2Qomw20ApoqDw-FJRvVaQWxrlNp3--cN0a95Mho4Oblfmb5KhfnddRtKK4ZdriJv_f5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارزش تجهیزات هر لابراتوار سیار به‌طور میانگین به ۱۰ میلیارد تومان می‌رسد
سجاد محمد علی نژاد معاون مالی و اقتصادی شهردار تهران در مراسم رونمایی از لابراتوار سیار خلاقیت و ساخت:
🔹
در اتوبوس‌های رونمایی‌شده نیز مجموع تجهیزات نصب‌شده به ده‌ها میلیارد تومان می‌رسد و با اضافه شدن آزمایشگاه‌های تخصصی‌تر، هزینه تجهیز این واحدهای سیار افزایش خواهد یافت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/659845" target="_blank">📅 19:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659844">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
سخنرانی امشب نتانیاهو درباره تفاهم ایران و آمریکا
رسانه‌های عبری:
🔹
نخست‌وزیر رژیم صهیونیستی قرار است امشب در خصوص تحولات اخیر و تفاهم‌نامه حاصل‌شده میان ایران و ایالات متحده آمریکا سخنرانی کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/659844" target="_blank">📅 19:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659843">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
من عزاداری تو رو دوست دارم...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/659843" target="_blank">📅 19:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659842">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
رئیس کمیسیون اروپا: تحریم های ایران کاهش نخواهد یافت
اورسولا فون در لاین، رئیس کمیسیون اروپا در موضع گیری خصمانه اعلام کرد:
🔹
اتحادیه اروپا بدون تغییرات مشخص در سیاست‌های ایران، تحریم‌های خود را کاهش نخواهد داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/659842" target="_blank">📅 19:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659841">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e56e60def.mp4?token=je6pQv9vlRcSBAVEpoZM7bW2IaxRM5nENg3pTbo24iSPfLcbLMP-6lif6wB7RNGKPLtoLHqRu6JMAY_FciZBkVJQZ9udQDCyL3ZE0-DF61f-XicfbF-9geIRxDvi_Eh-dh2mc4Ijalrh7S5nq4npqtcMgfsg3KJJUzyxUyc-ei82jwhVV6HWgfiydir58avB_t0VZn4RT_vma9hkuM9z2R9ft0U1061ApNncxVA6Ae4yMKeoRGE2RMnTxdmVxDhnn-T4XNXN_tGsDUo3-8cP97r8oBh7QCSXvnnkvuiuhtLfrwScpsoyLfFvRowNL-Mt2GTypbfWO2JXRqKvqpsTUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e56e60def.mp4?token=je6pQv9vlRcSBAVEpoZM7bW2IaxRM5nENg3pTbo24iSPfLcbLMP-6lif6wB7RNGKPLtoLHqRu6JMAY_FciZBkVJQZ9udQDCyL3ZE0-DF61f-XicfbF-9geIRxDvi_Eh-dh2mc4Ijalrh7S5nq4npqtcMgfsg3KJJUzyxUyc-ei82jwhVV6HWgfiydir58avB_t0VZn4RT_vma9hkuM9z2R9ft0U1061ApNncxVA6Ae4yMKeoRGE2RMnTxdmVxDhnn-T4XNXN_tGsDUo3-8cP97r8oBh7QCSXvnnkvuiuhtLfrwScpsoyLfFvRowNL-Mt2GTypbfWO2JXRqKvqpsTUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپاد انتحاری اسرائیل به زندان «اصداء» در
غزه
🔹
پهپادهای انتحاری رژیم صهیونیستی در تازه‌ترین اقدام نظامی خود، یکی از ساختمان‌های واقع در زندان «اصداء» در شمال شهر خان یونس را هدف قرار دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/659841" target="_blank">📅 19:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659840">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
عراقچی: احتمال امضای تفاهم‌نامه ایران و آمریکا روز جمعه در سوئیس
وزیر امور خارجه:
🔹
احتمالاً روز جمعه در سوئیس دیداری میان رؤسای هیئت‌های مذاکره‌کننده ایران و آمریکا برگزار و تفاهم‌نامه‌ای امضا شود و سپس نخستین دور مذاکرات بعدی انجام گیرد؛ این تفاهم می‌تواند گشایش‌های اقتصادی ایجاد کند، اما اقتصاد کشور نباید به چنین توافقاتی متکی شود.
🔹
عراقچی با اشاره به سابقه بدعهدی‌ها و عدم اجرای توافقات، تأکید کرد روند مذاکرات و اجرای توافق بر اساس بی‌اعتمادی و تجربیات گذشته برنامه‌ریزی می‌شود؛ ایران از مسیر توافق برای ایجاد گشایش اقتصادی استفاده می‌کند، بدون آنکه به آن دل ببندد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/659840" target="_blank">📅 18:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659839">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuRu7ZKuU7l7X_ISI69zJ0jXD1vdD1Lkt0dCGYpRkW6_L_zvnA7wYLtwC-jdptXNW7yRoUV5yTGWFYtnfbR03xiOI9KxAuRzIpxKUokL02VJYirljMYZZaeyKzQpMWSIofukPclxLVLOflM9fxxdkX9y_P4x2vxKpGsInKODSTywR_-qR_vgoj1xyAmbuXn0FqF1_L31XBpisLS_HFoar82d5S2kliVtG-kbytWEhpefvlWWJ9SyvTY9D1mBn_OPF9T0rH0Ga27Qj49UJu5xJAFfa6iKbiGYZSRysGrUl7Nu3_MIyDXOPEM1Utxq7CJxcD--nbE7t4eBW-3a1ET4cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/659839" target="_blank">📅 18:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659838">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76223f1b49.mp4?token=qC7IEnUV_ikgewB3PjZXotyvmc5rVOi2aZ-_ivfv4acsVhhkjYjFSVYVsH5ji_RtoF_-rNWDmsCv3gP89xZ19MJfnvziGE2ffRehfeK_kXHdPPzMmo7ABmd7RXKQIk4paRt8i3MvDGyx89pY-cVidlHPvWxgjwIQpYtEA5le5NG2YaMSDCXiiEddnE5a-3oX9uAqdgkkBc5-9JluxM_iseOHknN3TEBXTvEk8DLJy1Thx0K3VsEkW_RNneVStu73ZSBjtgEMT-RDGro2yM5YIVI_CjxOi3PxO_mVGkRsB-nUXoqS5r9NyEYQ4A23Cy-UmFdrU5FW0O0oCZC90wdA6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76223f1b49.mp4?token=qC7IEnUV_ikgewB3PjZXotyvmc5rVOi2aZ-_ivfv4acsVhhkjYjFSVYVsH5ji_RtoF_-rNWDmsCv3gP89xZ19MJfnvziGE2ffRehfeK_kXHdPPzMmo7ABmd7RXKQIk4paRt8i3MvDGyx89pY-cVidlHPvWxgjwIQpYtEA5le5NG2YaMSDCXiiEddnE5a-3oX9uAqdgkkBc5-9JluxM_iseOHknN3TEBXTvEk8DLJy1Thx0K3VsEkW_RNneVStu73ZSBjtgEMT-RDGro2yM5YIVI_CjxOi3PxO_mVGkRsB-nUXoqS5r9NyEYQ4A23Cy-UmFdrU5FW0O0oCZC90wdA6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود ترامپ به فرودگاه اویان
🔹
دونالد ترامپ، رئیس جمهور آمریکا وارد فرودگاه اویان محل برگزاری نشست جی۷ شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/659838" target="_blank">📅 18:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659837">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
گستاخی رژیم صهیونیستی؛ عملیات‌ها متوقف نشده و تنها کاهش یافته است
ادعای شبکه ۱۲ رژیم صهیونیستی:
🔹
دامنه عملیات‌های ارتش متجاوز صهیونیستی در جنوب لبنان به‌طور قابل‌توجهی کاهش یافته است.
🔹
این تغییر رویکرد نظامی در حالی صورت می‌گیرد که فرماندهان صهیونیستی در انتظار ابلاغ دستورات جدید از سوی سطوح عالی سیاسی این رژیم هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/659837" target="_blank">📅 18:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659836">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47c8ee5a78.mp4?token=OEZclFyhfyjYQQ_57a7I5pv3ftJ3S7H3UBkubQ0vU2IxrbosN52ZkBa7bCRiNqFPTgMZfJ-wEta-KNH05fs6AIXUs_cihw_g-yuRsFiBSNFwcEgp37CN1ReyZ5j2GAjkAF4EEb2gVzuDb2Ahm34DEFwUnDLS1A9oOqORyHIEzxs4h7AkHG8Q7O4HoSeDKFC-zum9G5PiHYNbRNg8S2NvTRXTYzQdhb0T4JnXjGZW4dFr6N_IIFg0iwSXWqnPImIIzMzMp9nz8RtdFm7-NXsgfxrOmWffOiXxphdyC4EOflbchEhbzv1-RNbN8PLWRbWi7KrzylWMUmfWwBB_udK0xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47c8ee5a78.mp4?token=OEZclFyhfyjYQQ_57a7I5pv3ftJ3S7H3UBkubQ0vU2IxrbosN52ZkBa7bCRiNqFPTgMZfJ-wEta-KNH05fs6AIXUs_cihw_g-yuRsFiBSNFwcEgp37CN1ReyZ5j2GAjkAF4EEb2gVzuDb2Ahm34DEFwUnDLS1A9oOqORyHIEzxs4h7AkHG8Q7O4HoSeDKFC-zum9G5PiHYNbRNg8S2NvTRXTYzQdhb0T4JnXjGZW4dFr6N_IIFg0iwSXWqnPImIIzMzMp9nz8RtdFm7-NXsgfxrOmWffOiXxphdyC4EOflbchEhbzv1-RNbN8PLWRbWi7KrzylWMUmfWwBB_udK0xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هدف ما این است که دانش‌آموزان در کنار آموزش تئوری، ‌ایده‌های خود را هم به صورت عملی پیاده کنند
سجاد محمد علی نژاد معاون مالی و اقتصادی شهردار تهران در مراسم رونمایی از لابراتوار سیار خلاقیت و ساخت:
🔹
هدف از راه‌اندازی لابراتوارهای سیار خلاقیت و ساخت، فراهم کردن فرصتی برای دانش‌آموزان است تا فراتر از آموزش‌های تئوریک، ایده‌های خود را به مرحله اجرا برسانند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/659836" target="_blank">📅 18:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659835">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwO_aEXmzfrtmg5fv5j9mmq30384JmDxhoBWJfao3BfTtHAG2VCN5opzJ1SjBwbNa6wmKfp70Y3UmLPljqLRutXs1iS_RkiqmJpQbKLIqjR4bY6_P2q9REbKTVA1dxc--2BaBWnZ2AGafpVAHpm8y1jzSIG4zpvhDwxMJQ9ozxgJaquoAaGVhRjql_SyWvYusbl-uTGbCh2hNl_1LNuh3MWXpReJFamtkvV90ZkhvF1WdzgohOCS0jsxhFoGerKo-SN5kqnrRc837SfQH4OWm1W8KVODnLpO5tiVR1OLGh9ZjQTyvFAfPXlpvNbUq6fm9bGBWzC2T58VXn5la9Uatg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین سرانه مصرف آب در جهان مربوط به کدام کشورهاست؟
🔹
ترکمنستان و مونته‌نگرو با اختلاف، بیشترین سرانه مصرف آب جهان را دارند.
🔹
حضور چند کشور آسیایی در این فهرست، الگوی مصرف آب در منطقه را برجسته می‌کند.
🔹
ایران با مصرف سرانه بیش از ۳۶ هزار فوت مکعب، در جمع کشورهای پرمصرف قرار گرفته است.
@amarfact</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/659835" target="_blank">📅 18:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659834">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2540562b52.mp4?token=cmCx3qYVOFmWpAJkGrWtukubo3GksHgC_3f25ERNmxtAwhwoevibscjWyuc_aqSOUjX3n63Eo9xknmpKtSvd85ztuJyEPS9r0Le8hGCek4DyfxaJrz61Sq3XBRjGRbxFHc_yUB7aNiinXtbskzZMnuqxYoeYvLqy-XUyfWYNip7YTOpFGenePl2Pz7Umh9LOU4fBHN5ccJn5zfBVnXMwQ7xIY48RYYkqS2IoyH_OPr1QdI2FUddsuUAI56SHHa11OD7dVQJWua8oFTf_hFX7FAPO7jxtaQ4ov9wywU1Z2nVfGb1LMSb2pUbcPPxi09M5Tgv3Q9GZMBOio00DJ7OF0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2540562b52.mp4?token=cmCx3qYVOFmWpAJkGrWtukubo3GksHgC_3f25ERNmxtAwhwoevibscjWyuc_aqSOUjX3n63Eo9xknmpKtSvd85ztuJyEPS9r0Le8hGCek4DyfxaJrz61Sq3XBRjGRbxFHc_yUB7aNiinXtbskzZMnuqxYoeYvLqy-XUyfWYNip7YTOpFGenePl2Pz7Umh9LOU4fBHN5ccJn5zfBVnXMwQ7xIY48RYYkqS2IoyH_OPr1QdI2FUddsuUAI56SHHa11OD7dVQJWua8oFTf_hFX7FAPO7jxtaQ4ov9wywU1Z2nVfGb1LMSb2pUbcPPxi09M5Tgv3Q9GZMBOio00DJ7OF0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط بمب افکن توپولوف ۲۲ روسیه
🔹
روزنامه سان از سقوط یک فروند بمب‌افکن دوربرد فرا صوت توپولوف ۲۲ ام ۳ روسیه در مزرعه‌ای در ایرکوتسک خبر داد.
🔹
علت این حادثه هنوز اعلام نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/659834" target="_blank">📅 18:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659833">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7b04b313e.mp4?token=ndD9PZlfdDuZ1hEgCqAICfukw0KVl_7yTTaQ1J9L4ll4rx0rm_O-dwA1mIHFo1PdDN07siEipYo6oMyeT7nedRBabjwSCXkXk0HCUun2iitEnqdqDNGzQBq3wO2Ax-TBMFxmvx5CpFcYxlisEXRJCcmYtWTrj3vV8lej6ZHE_tlzO0_r0p-6DfEndRbtUuuaMICCjZMfk3au6WY2g9jHHVJMSIzC_IR-5aZVCPMveGfKDrzpoZSluZlenoVa95JFXVwYtdu97_TVCHli0WR4HB-PLoyOewJ49HyMJ8jWNph93fdoGXMwmbgq05Y8HRbR-NIyZeXNjFQGL3y0h3kC6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7b04b313e.mp4?token=ndD9PZlfdDuZ1hEgCqAICfukw0KVl_7yTTaQ1J9L4ll4rx0rm_O-dwA1mIHFo1PdDN07siEipYo6oMyeT7nedRBabjwSCXkXk0HCUun2iitEnqdqDNGzQBq3wO2Ax-TBMFxmvx5CpFcYxlisEXRJCcmYtWTrj3vV8lej6ZHE_tlzO0_r0p-6DfEndRbtUuuaMICCjZMfk3au6WY2g9jHHVJMSIzC_IR-5aZVCPMveGfKDrzpoZSluZlenoVa95JFXVwYtdu97_TVCHli0WR4HB-PLoyOewJ49HyMJ8jWNph93fdoGXMwmbgq05Y8HRbR-NIyZeXNjFQGL3y0h3kC6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در خیمه حسینیم، خونخواه و جانفداییم...
‌
🔹
نصب کتیبه ایوان طلای صحن آزادی
به مناسبت فرارسیدن ماه محرم
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/659833" target="_blank">📅 18:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659832">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDar18uuT2YD0SYe3ofuj3wJLdPyZP2wovngs8N2uQDpDUGtwSTUgBjtljw8u65bj2CdMtatWc577LoRVnIFAzZ_i_pNyb-4W_2vVx73-ZM0Tq_noy199q4IwpzAH_f1mONyfcT_CcDtnD5UZWbmHzx84cbmTJVfucbuoiTTbIOW3uuIfmFC5IFPcQhAsZjnGO0U8_s7N5iFqb6powE6-5MB9uO5pE6gPwq11JGwuNnZJi5lLHbYo3xPi5WgShgf3x8orGfeYLRFOEpa2IJr1aKlcvou9ZCWYJas3FpOXzSx9E2WWEQ_Ql8FCmXzLTFUtmtuq6HhAJRIi4VhtIeCzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری کمتر دیده‌شده از رهبر انقلاب اسلامی حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای
🔹
عکاس: علیرضا فراهانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/659832" target="_blank">📅 18:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659831">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
پزشکیان: تیم مذاکره‌کننده به هیچ‌وجه از سیاست‌های تعیین‌شده از سوی رهبری عدول نخواهد کرد
رئیس‌جمهور:
🔹
پیروزی دیپلماتیک اخیر، سند افتخار ملت ایران در برابر زورگویان جهان است.
🔹
سرمایه اجتماعی و همراهی مردم بزرگ‌ترین پشتوانه امنیت و پیشرفت کشور است.
🔹
هرچه انسجام داخلی بیشتر باشد، قدرت دفاع از حقوق ملت در مذاکرات افزایش می‌یابد.
🔹
آینده ایران در گرو هم‌افزایی همه ارکان حاکمیت و بهره‌گیری از ظرفیت‌های مردمی است و هیچ قدرتی نمی‌تواند در برابر ملتی متحد و همدل ایستادگی کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/659831" target="_blank">📅 18:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659830">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
گزارش‌ها از وقوع حادثه دریایی در سواحل یمن
🔹
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع یک حادثه امنیتی در آب‌های نزدیک به یمن و هدف قرار گرفتن یک نفتکش خبر داد.
🔹
بر اساس گزارش مرکز عملیات تجارت دریایی بریتانیا، یک قایق کوچک با چهار سرنشین مسلح به این نفتکش نزدیک شده‌اند.
🔹
سرنشینان این قایق در جریان این حادثه، با استفاده از پرتابگر آرپی‌جی به سمت کشتی شلیک کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/659830" target="_blank">📅 18:29 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
