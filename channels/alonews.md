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
<img src="https://cdn4.telesco.pe/file/jgbFB-Eiw6AhjbiKjitEwtcqtuInrvqg76cb5mGF7hxvuKYkXhcEkMplmptFXPCmkw63_I_DPxu6fLdrX8w3iIx63J9mrxTBu-ZS5TkzGeZqr1gDyEHNUMiBBAceV_9ITI5KZh_TfGV-jJQDkbazdm1MljtdykuzqzFNqpeWtTIzGuQni5GpVm7viA-XMboTMbqz_wNXTKwP1kyphCyV6cxzvq1u0zySVeImvi5eJSl-TKJNaRVIH62oWMJMoqsxvTZAMcFrIWjmXY90-tIvB9KigdXZF-QogN5s-WzFbHw623-EfNt-FU40x4mwAJSQCDNfOmfscyOXASRN1JVkrg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 924K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 10:05:14</div>
<hr>

<div class="tg-post" id="msg-123214">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
اتحادیه اروپا: همه به دلیل بسته شدن تنگه هرمز هزینه سنگینی می‌پردازند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/alonews/123214" target="_blank">📅 10:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123213">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
افزایش دما در کل کشور
🔴
هواشناسی اعلام کرد: امروز و فردا دما در تمام نقاط کشور افزایش پیدا خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/alonews/123213" target="_blank">📅 09:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123212">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IP-0j1bCmgHwfoE972yASS6mYCzQ9LxVopuvfgJnKnrHQ6lybKJOrPSJjXYnlEhWPuQ3QAq1QL_2RkC__9t7yJ8KnkWcWNa-XmZo44Ap7BKBoYiBpsTCkwJPLyjXTQQMfze8MsPUQtgY54OsQl8ct4GU9ucf-YQ5BgX7OT9-W7vLSKlxbtu2JNN7v68t2fuI_ypse07EYpVFWOfrP1w9SdBkRpr3Zz3Y5mIRHWccqO1-IOj-5T6xEr27LIXrS5z_fgvn26LBzycVQxxDOxdNHvelj71onCuhBKvFFhh0SyZb_K11Y2lfEeSET--ayeAQe9-z8JKnNGlSL68dtRVOcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی دقایقی پیش حملات هوایی در شهر نبطیه، جنوب لبنان انجام دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/alonews/123212" target="_blank">📅 09:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123211">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
رویترز: قطعی اینترنت ایران، طولانی‌ترین قطعی اینترنت در تاریخ معاصر جهان بود و زندگی میلیون‌ها نفر را تحت تأثیر قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/123211" target="_blank">📅 09:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123210">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل گزارش می‌دهد که فردا دور جدیدی از مذاکرات بین سفیران اسرائیل و لبنان در آمریکا آغاز خواهد شد و این بار در ساختمان پنتاگون خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/123210" target="_blank">📅 09:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123209">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad5a7a9116.mp4?token=IYMX1CVmNbiPRglUpQzd0eiqffwyUvym80MANXwl_WrbD-YdsjjsbqJI32R9jw9teMfsMHFHvsWdqg3_IoC13YHwJd9P3XyBvyuRelC2sFhVpCS0WpECuEwMqCpv3aweZqN-lAeQQCsBDMRIbtcWnpPrbKH4ziEfmB8KX69eLSAQ5xpSIo5vUasjavcCM1LUL_F84cHqKE85KRG_EU4YxvldqAToQbgXmrOGcioCygz2dHrEaJGiVAqlDX9EiCdLHAtmXyBBOIm0KpecBNihgl0lCcOLXIVXsOK-a7gnkQWFxrH9MBp_9--eLef6uPr_AP8zfnfXLuQ2BPLqjT5rCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad5a7a9116.mp4?token=IYMX1CVmNbiPRglUpQzd0eiqffwyUvym80MANXwl_WrbD-YdsjjsbqJI32R9jw9teMfsMHFHvsWdqg3_IoC13YHwJd9P3XyBvyuRelC2sFhVpCS0WpECuEwMqCpv3aweZqN-lAeQQCsBDMRIbtcWnpPrbKH4ziEfmB8KX69eLSAQ5xpSIo5vUasjavcCM1LUL_F84cHqKE85KRG_EU4YxvldqAToQbgXmrOGcioCygz2dHrEaJGiVAqlDX9EiCdLHAtmXyBBOIm0KpecBNihgl0lCcOLXIVXsOK-a7gnkQWFxrH9MBp_9--eLef6uPr_AP8zfnfXLuQ2BPLqjT5rCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم‌اکنون - وضعیت تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/123209" target="_blank">📅 09:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123208">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فوری / پولیتیکو: تجهیزات لازم برای حمله نظامی به کوبا تکمیل شده و تنها چیز باقی‌مانده دستور ترامپ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/123208" target="_blank">📅 09:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123207">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
رویترز از عبور سه تانکر نفت از تنگه هرمز بعد از خاموش کردن ردیاب خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/123207" target="_blank">📅 09:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123206">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل گزارش داد که ۱۵ فروند پهپاد انتحاری از لبنان در ۲۴ ساعت گذشته به شمال اسرائیل نفوذ کرده و تأکید کرد که ۵ فروند از آنها در نزدیکی مواضع نظامی اسرائیل منفجر شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123206" target="_blank">📅 09:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123205">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c882b2806.mp4?token=PHh2s6DUVimBeZ-GPd4TJ7L511Udf7wYxdVnL8PiwvSGKBYzmz8TJuuWx9l0xxmpgm0W8f8PmTrI3S5NFueoQqnckKwSozvQpxmvg4cbSr3YSUVSrnHfZPMVzDOQRJaEkVfISn8M-mtkO9T4NFj8rQH0UiMRSlWet-YmqAA5TGrIz1bdSP6ocWkfs7LoLm9IiHKuUEUZ1-z7Cc-J_drGp7FfpCycPYbqDOldgHlTk4Bd0U88xqpdSrhVD3Njw9Bd4Jf6wcOfEc3xQVk-fxdDgNYrOPyZBZi9PjQ_h2d2ui9LYLibBXdNelhn8vw8hUTftII5UU4fZbI68q6QQA-gfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c882b2806.mp4?token=PHh2s6DUVimBeZ-GPd4TJ7L511Udf7wYxdVnL8PiwvSGKBYzmz8TJuuWx9l0xxmpgm0W8f8PmTrI3S5NFueoQqnckKwSozvQpxmvg4cbSr3YSUVSrnHfZPMVzDOQRJaEkVfISn8M-mtkO9T4NFj8rQH0UiMRSlWet-YmqAA5TGrIz1bdSP6ocWkfs7LoLm9IiHKuUEUZ1-z7Cc-J_drGp7FfpCycPYbqDOldgHlTk4Bd0U88xqpdSrhVD3Njw9Bd4Jf6wcOfEc3xQVk-fxdDgNYrOPyZBZi9PjQ_h2d2ui9LYLibBXdNelhn8vw8hUTftII5UU4fZbI68q6QQA-gfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جیل بایدن گفت که نگران بود جو بایدن در حین مناظره پربحث ۲۰۲۴ خود علیه ترامپ «در حال سکته کردن» باشد.
🔴
در مصاحبه‌ای با سی‌بی‌اس نیوز، او گفت که «هرگز جو را پیش از این یا پس از آن به این شکل ندیده است» و از عملکرد او «ترسیده بود».
‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123205" target="_blank">📅 09:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123204">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
اورسولا فون درلاین رئیس کمیسیون اروپا ضمن تاکید بر حمایت کامل اتحادیه اروپا از اوکراین، از کمک نظامی ۲۸ میلیارد و ۳۰۰ میلیون یورویی این اتحادیه به کی‌یف خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/123204" target="_blank">📅 08:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123203">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رسانه‌های لبنانی از تداوم حملات اسرائیل به لبنان و حمله به شهرک «الغسانیه» در جنوب این کشور خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123203" target="_blank">📅 08:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123202">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
دولت ترامپ به دادستان‌های فدرال در وزارت دادگستری دستور داده است که از پیگیری هرگونه تحقیقات کیفری علیه رئیس‌جمهور موقت ونزوئلا، دلسی رودریگز، خودداری کنند، طبق گزارش AP.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/123202" target="_blank">📅 08:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123201">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4334f4dc71.mp4?token=tU706ihGRvAbA5gaXVOLsJi2wNQni_nJV6FHdY8WF5eqMCG5v3dflyocvxDNUDADYjwEUzxXcMHHSfeThHDnnj-VX3iuCrwiNbdSbPZkR3FBq1dHuEj7EG2kYGpz0aILgoOWqOkTS1-Orv1fM3wwf-8oSF_2ciIwAXKJp9emGzdcW0ExBO7K0vSO8Q7PkGVKwucFi20a0lWEJN38UeZKxB9mf_9blgwqs-9Gd2xaxNP7sGbaxxeAFl2SxVSM2oNXxLaVklyLXPi4CyqiHNy31Ln7Y-eRERanKn6fx6pwyWIt7QJzKgErvCivPZ5ooQjSmlx-E9Lg_8KxRRZf0obRIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4334f4dc71.mp4?token=tU706ihGRvAbA5gaXVOLsJi2wNQni_nJV6FHdY8WF5eqMCG5v3dflyocvxDNUDADYjwEUzxXcMHHSfeThHDnnj-VX3iuCrwiNbdSbPZkR3FBq1dHuEj7EG2kYGpz0aILgoOWqOkTS1-Orv1fM3wwf-8oSF_2ciIwAXKJp9emGzdcW0ExBO7K0vSO8Q7PkGVKwucFi20a0lWEJN38UeZKxB9mf_9blgwqs-9Gd2xaxNP7sGbaxxeAFl2SxVSM2oNXxLaVklyLXPi4CyqiHNy31Ln7Y-eRERanKn6fx6pwyWIt7QJzKgErvCivPZ5ooQjSmlx-E9Lg_8KxRRZf0obRIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای فرماندهی جنوبی آمریکا در قالب عملیات «Southern Spear» روز چهارشنبه به یک قایق مشکوک به قاچاق مواد مخدر در شرق اقیانوس آرام حمله کردند.
🔴
این قایق در مسیرهای شناخته‌شده قاچاق مواد مخدر در حال حرکت بوده است.
🔴
در این حمله دو مرد کشته شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/123201" target="_blank">📅 08:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123200">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
یک منبع آگاه نظامی: تردد در تنگه هرمز بدون مجوز ممنوع است و نیروهای نظامی با شلیک اخطار، ۴ فروند شناور بدون هماهنگی را وادار به بازگشت کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123200" target="_blank">📅 08:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123199">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d6c40b930.mp4?token=iYBCmMduYuSWT4ryGTX-muKX7R1qhLU95zZN0LYbIC74WT00n4nUzze5uUhZS_1DNAhJtP6SYGHv0_zPPON_3u_enpZRE4oDCn4H30MEufS6Kvx2p9wnRkTd6IFb69elhyUShkINDYMsnh2PtgTd5bT5g3eDtXC_gMc2E5KsFiFKJPWLfoRWO6uJ4VQFODCMpSPNmyGtpNXao8lniXAqiWaN0U-LLeyRhC4tUPkVLBeZRXtjGjz-uhAzEA39YLr7z97dSw36BBZOZwtqyOx2_5C-L4S2lfC4ngJuyhmbJaBYLkpWvG4wK3OafJ5qxvD28oXkWzHxNN8U9r9KZUsqVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d6c40b930.mp4?token=iYBCmMduYuSWT4ryGTX-muKX7R1qhLU95zZN0LYbIC74WT00n4nUzze5uUhZS_1DNAhJtP6SYGHv0_zPPON_3u_enpZRE4oDCn4H30MEufS6Kvx2p9wnRkTd6IFb69elhyUShkINDYMsnh2PtgTd5bT5g3eDtXC_gMc2E5KsFiFKJPWLfoRWO6uJ4VQFODCMpSPNmyGtpNXao8lniXAqiWaN0U-LLeyRhC4tUPkVLBeZRXtjGjz-uhAzEA39YLr7z97dSw36BBZOZwtqyOx2_5C-L4S2lfC4ngJuyhmbJaBYLkpWvG4wK3OafJ5qxvD28oXkWzHxNN8U9r9KZUsqVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار صداوسیما :  با وجود شنیده شدن صدا، نشانه‌ای از انفجار تو بندر عباس دیده نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/123199" target="_blank">📅 08:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123198">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وال استریت ژورنال: ایران همچنان نفت خود را می‌فروشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/123198" target="_blank">📅 08:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123197">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
قیمت نفت برنت پس از حمله موشکی سپاه به پایگاه آمریکایی در منطقه، از مرز ۹۸ دلار عبور کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/123197" target="_blank">📅 08:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123196">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b018624a4.mp4?token=JKh0JhGoa8ceFU0KBBJHCpXMLPWpKPab67mFOkB9a5ippCNcJQMLxGQoAIa140wMIDsLh1qH1E4hJ_tXy-iUlvYGtx-ANMDMSkZ8muqNQioDaPsD5pknS2AM5cdIquby2tYW3afbX1BMUsDg2vXNPiAdGG07nnOsrOjt_hx2z9Bih3RkJDNWiq0FMn4diMif8iZOXIoVbV2bT94A0w67prcaYZt0F5xAvsXohkv2yjrrvmOxDM-9_OMMRr3hte1YzfIyYRZDCHFNNoPqSYz4EA3LXbXMYHPZTGSZsZH3xIH6n9YOd6dLqK0uDkVIAnGsyhbtuxnftadFnErty7riFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b018624a4.mp4?token=JKh0JhGoa8ceFU0KBBJHCpXMLPWpKPab67mFOkB9a5ippCNcJQMLxGQoAIa140wMIDsLh1qH1E4hJ_tXy-iUlvYGtx-ANMDMSkZ8muqNQioDaPsD5pknS2AM5cdIquby2tYW3afbX1BMUsDg2vXNPiAdGG07nnOsrOjt_hx2z9Bih3RkJDNWiq0FMn4diMif8iZOXIoVbV2bT94A0w67prcaYZt0F5xAvsXohkv2yjrrvmOxDM-9_OMMRr3hte1YzfIyYRZDCHFNNoPqSYz4EA3LXbXMYHPZTGSZsZH3xIH6n9YOd6dLqK0uDkVIAnGsyhbtuxnftadFnErty7riFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه انهدام یک فروند موشک کروز در آسمان کشور توسط سامانه های پدافندی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/alonews/123196" target="_blank">📅 08:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123195">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a29329702.mp4?token=gJGf1nRd3mobkoyKxsBNYUCYmbn2PQasBtM7mpZE8JJf82SE1TDpJCcWp11t1eJcEeeklzGiaeI7_NzrlprCwLYfN_90_LsgveKfvzOqVTWJlhSRU92U4mjkia9kGFIvgCXmFUWo1kNGrmtqN4qSZgfGEC2BYsLlop3WbmrVOG2NtYHxFwtL3TBKabqAmUCm64If5AJB8xxjV6NWcnqaxdsMIbNMF-_Nbmp6TsIk9WHUZtvbwEdyOLa6T5UhvaFXZGsqTSpE2ef-BFOHYSCrMF8PglpUMJ7AJmbH6xsgNjZ-o0FHIAwmcQbeBpfyo8ei-nOZPCwPCIPEAeqVLfY6ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a29329702.mp4?token=gJGf1nRd3mobkoyKxsBNYUCYmbn2PQasBtM7mpZE8JJf82SE1TDpJCcWp11t1eJcEeeklzGiaeI7_NzrlprCwLYfN_90_LsgveKfvzOqVTWJlhSRU92U4mjkia9kGFIvgCXmFUWo1kNGrmtqN4qSZgfGEC2BYsLlop3WbmrVOG2NtYHxFwtL3TBKabqAmUCm64If5AJB8xxjV6NWcnqaxdsMIbNMF-_Nbmp6TsIk9WHUZtvbwEdyOLa6T5UhvaFXZGsqTSpE2ef-BFOHYSCrMF8PglpUMJ7AJmbH6xsgNjZ-o0FHIAwmcQbeBpfyo8ei-nOZPCwPCIPEAeqVLfY6ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کویت از رهگیری حملات موشکی و پهپادی خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/alonews/123195" target="_blank">📅 08:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123194">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
آمریکا «نهاد مدیریت آبراه خلیج فارس» را تحریم کرد
🔴
وزارت خزانه‌داری آمریکا اعلام کرد سازمان تازه تأسیس ایرانی «نهاد مدیریت آبراه خلیج فارس»  را به فهرست تحریم‌های خود اضافه کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123194" target="_blank">📅 07:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123193">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdnZTXM_Qv2110fQAwCw5Ws8wi9Fg0msAKyB3adXhwDT2-eMeMDBGUS646nRqxbuvjikdvKUhtWzf93fJzKN4vHd4tJeYz2f2tDRph8xj-qICGntNJ5KIakeEU_LI2Ku6YHXifCbaAagqHYkiEy_GQzT1_3XwLkxgKx_TVUTS4NixYTfaNqGxgvhanDxkjRoRB7uE0ci2L7vdC9djl-215R1m817b7s2Of02SjK0xYX6G6voAYWbrOlzgQuCyZJj-60VBrpJI6Sz6BFjNDc01gTQqgK4ygWu89dt1WECovj7gpRiweq0R5DPP0yMPsoJCg4WIGBY1ZBi2UepDUAHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا مبدا حمله کویت بوده.
🔴
سر همین قضیه قیمت نفت هم داره میره بالا.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/123193" target="_blank">📅 07:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123192">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سپاه یک پایگاه هوایی آمریکایی را هدف قرار داد
روابط عمومی سپاه طی اطلاعیه‌ای اعلام کرد:
🔴
به دنبال تعرض سحرگاه امروز ارتش متجاوز آمریکا به نقطه‌ای در حاشیه فرودگاه بندر عباس با پرتابه‌های هوایی، پایگاه هوایی آمریکایی به عنوان مبدا تجاوز، در ساعت ۴/۵۰ دقیقه هدف قرار گرفت.
🔴
بسم الله القاسم الجبارین.
🔴
فمن اعتدی علیکم فاعتدوا علیه بمثل ما اعتدی علیکم.
🔴
به دنبال تعرض سحرگاه امروز ارتش متجاوز آمریکا به نقطه ای در حاشیه فرودگاه بندر عباس با پرتابه‌های هوایی، پایگاه هوایی آمریکایی مبدا تجاوز، در ساعت ۴/۵۰ دقیقه هدف قرار گرفت.
🔴
این پاسخ یک اخطار جدی است تا دشمن بداند، تجاوز بدون پاسخ نخواهد ماند و در صورت تکرار، پاسخ ما قاطع تر خواهد بود.
🔴
مسئولیت عواقب آن با متجاوز است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/alonews/123192" target="_blank">📅 06:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123191">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCtCvjsDR-d_Fxn3wMfsRgO2ZeavaNB0l3VazIZWNtr2yw3807c0j1HJGGWVVGo0cBZkOC6l9zRS_Nlb9V5sw-LHa42AONWXYvDxnhgyKSDkJHIsIpA0m2vb50f2pdF9Te5TQRGxYiQhHNJn8ogFDaMYQHfdoBDHljZTqxHs_HSgYiEADcBfBVrroCHnELn-Mdv3wkIO3EJZ2_duMpRLKBexj6H-0_WR0h4cGHIoYAQl8SdbZLrTUsKQjWVNkLb0SiAcuRdlY9vi_mnmxFBxyizQBkr6aOanadG9WjZl2_TbJNIIf0vOryW4t6b8T10cMDs2egIFBWoXRgE6b2_KEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
👈
فاکس نیوز: آمریکا یه ایستگاه کنترل زمینی ایران رو تو بندرعباس زده؛ همون جایی که قرار بوده یه پهپاد تهاجمی ازش بلند شه.
🔴
به گفتهٔ مقام‌های آمریکایی، چهار تا پهپاد انتحاری دیگه هم که تو تنگه هرمز تهدید محسوب می‌شدن، زده شدن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/alonews/123191" target="_blank">📅 06:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123190">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
خبرگزاری CBS: "یک سایت نظامی در خاک ایران هدف حمله قرار گرفت."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/alonews/123190" target="_blank">📅 06:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123189">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
یک مقام آمریکایی به سی‌بی‌اس گفت ایالات متحده حملات جدیدی را علیه یک سایت نظامی ایران انجام داده ولی آتش‌بس همچنان برقرار است.
🔴
یک مقام آمریکایی در گفت‌وگو با رویترز از حملات جدید آمریکا به یک سایت نظامی در ایران خبر داد و گفت ارتش آمریکا همچنین چندین پهپاد ایرانی را رهگیری و سرنگون کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/alonews/123189" target="_blank">📅 06:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123188">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
یک منبع آگاه نظامی به خبرگزاری تسنیم گفت: ساعاتی پیش یک نفتکش آمریکایی با خاموش کردن سیستم راداری خود قصد عبور از تنگه هرمز را داشت که با اقدام سریع و قاطع نیروی دریایی سپاه و شلیک به سمت آن، مجبور به توقف و بازگشت شد.
🔴
در مقابل، ارتش آمریکا به زمین سوخته‌ای در اطراف بندرعباس شلیک کرده‌اند که صدای انفجارها مربوط به این ماجرا بوده است؛ این شلیک هیچ خسارت جانی یا مالی به همراه نداشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/alonews/123188" target="_blank">📅 06:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123187">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGMPMNwnAbiegp8QxPWxPOH4SfYsEv8yLAStVFHJXBOvSSnxD5BAzOufmgYACJfeaI2GkjysZtmdF-x6H3DnBjxaA2dLvgL8Vaq2YvOMABGQppHjOm8D05uaQM3HN5uP-O9YK0BjHWCacT6AITlT5B-OS3xzuS4haYQ474L6-1yWkx67E1fOaAlrdUGqUenHQW-k6sIHh8ll4l639uTsMBiSm8y6dfEGAIPAm4dICKqLCwjxz2rqPHkQrbErogOAPtmDQZXeQYDInmG5CN5T_cEz1p-icbj4du4UMT9W0AgwbS7yDBArFC9-Nr4VDU2ems18hArC2F_u14tEIWNg7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین سرعت با بهترین قیمت با God Vpn
🔵
تخفیف ویژه برای امشب فقط
✅
✅
10 گیگ فقط 150,000 تومن
😍
بقیه قیمت ها در ربات
👍
✅
😍
❌
قیمت در حالت عادی گیگی
10 گیگ 250,000
❌
✅
تضمین بدون قطعی
🌐
اتصال با تمامی دستگاه
🔻
🏪
پشتیبانی ۲۴ ساعته
✔️
دور زدن نت ملی
🔘
بالاترین سرعت با تمام اپراتورها
⭐
با کیفیت عالی و ضمانت بازگشت وجه
🌐
🌐
🌐
🌐
🌐
🌐
⭐️
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
ربات تلگرام جهت خرید لحظه ای:
@GodVpnV2_Bot
ربات 1
@V2rayPc1bot
ربات 2
ایدی کانال:
t.me/God_of_Vpn
پشتیبانی و خرید عمده:
@Pc_V2ray
@Mmkhh00</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/123187" target="_blank">📅 01:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123186">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92515bedfb.mp4?token=v4oX4RE6_5c2juyoNUpDw_jLcx1szuC68FzT_StaoBnU8S6mPEydtKNeZbq__GkwIyEZ2vIhEss0Q62mnphTcp_ajJ0JkQEe3XOuCTMwRkimVdcCnA_NGUN5lDw71a8AuWM7Je_kyFJ6QG35-9d4TkwrO0YuqHEv1MOy1tXzslqokjeHQ3iWvHrYWXg-g0RTlwdbN1S9OVyFrIv7-pCRSMPfKnk74pKJxk2CuX2GKsrIsQSa4Wjj1GJYazVUPptsHRbi2yOsBRMF4gIvb0CH2PC8yI7OTdC64HAxRhaNjvoA37zIsyOeu-EcY1zS2ABlFp3WgaG6f4uonirmLk2IXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92515bedfb.mp4?token=v4oX4RE6_5c2juyoNUpDw_jLcx1szuC68FzT_StaoBnU8S6mPEydtKNeZbq__GkwIyEZ2vIhEss0Q62mnphTcp_ajJ0JkQEe3XOuCTMwRkimVdcCnA_NGUN5lDw71a8AuWM7Je_kyFJ6QG35-9d4TkwrO0YuqHEv1MOy1tXzslqokjeHQ3iWvHrYWXg-g0RTlwdbN1S9OVyFrIv7-pCRSMPfKnk74pKJxk2CuX2GKsrIsQSa4Wjj1GJYazVUPptsHRbi2yOsBRMF4gIvb0CH2PC8yI7OTdC64HAxRhaNjvoA37zIsyOeu-EcY1zS2ABlFp3WgaG6f4uonirmLk2IXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون
حمله به اسرائیل بندر صور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/123186" target="_blank">📅 01:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123185">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
خسارت حدودی قطع اینترنت در ۸۸روز
605,440,000,000,000تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/123185" target="_blank">📅 01:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123184">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cc6I79RerBImSfigzE7vIJLaOrpX0lWcC358RrXTDFYbaEuO8jxpYRPlk1N1TT5gYbzkgbtYZkH0ga04ZdYqqgI7ezsd_5wb840Iv6QdfQrAMQTlcS5ObDcXBsjPaOk8P4sI_1v-I0yynNKCHtz-fI5HhbAhMKZh-qgbOYyoZx1cycNA89mcLpGmoudhZgR-S9hFyeHRfE4IwKYddQ-c4WaoR3XKVwFZDshB_eFYOiNriHoqPmRydXlgUqFjK6l_3W_Jh6CJE6Jmn7MKQ6rXIlJssVBwRlBFIgSHUT-GJ2iSb0SH46Lj1yFiYPZU72CO-Q5JxqtPeSuUCd_dGqnlOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که تازه آنلاین شدن در جریان باشید اون موقع که شما نبودید، دنیا جهانبخت و مهدی رسولی باهم رل زدن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/123184" target="_blank">📅 01:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123183">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idzdwaZVNN_s4-G20Jzg26vh1pOezJXXbbu7mSMYQz9Hl6mGF1QD277koOkTtdKSaeAzdPPMRtv6ZDMP_L3nDqXutos0Z15j6M3bI3fLWw1XTqGB0xf0ph6FbJjwDI9SqJgZ3LUElfe2jcvKSqo5ZWWGgtaN0H9k4eS5HYts7sqQPBUG9le_FP4MjGpiPQ-H28YKbCs6Ze_cpRCZfzJxJlUyUG4uYxksUCfVDuMvGM-iT2PHWKifJOeYlOzYUg98DDPJPmUzjLWXCOc05nQijsENllosn504Bc5qlEEv0k29TRhBcn_8Ay95cwjSrZXFN3cMINkpJaA58FY_sS0TiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روتِم یانای ۲۰ ساله از تیپ گیواتی امروز در حمله پهپادی حزب‌الله به یک پایگاه نظامی نزدیک شومرا، شمال اسرائیل کشته شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/123183" target="_blank">📅 00:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123182">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f9eb9dc12.mp4?token=n3e9_0q89rhPhkXNb_cr6KrckGVdoMq8ZUwSgP9sMblpeKq5Q4pHTNhMRcd01GYulysJwfO_gn5LxWGW9xWVwB7X7Tx9HOEKqxJsPfBRTu7re8-XZwrlK2_GJMiJSJ_CU-0dCCgvKTHV2koW4oMS8Jdfk-ObtQkQiAZsv7Ea98Yws3DuSUKnaStsMjGDYERex8ovTnWryk7Tc6FZEI_HnaGXDW1A2kJ0fHHZBG1PJ0LqiulQarvgPDU54byoesyQ7v-3XsYEFUm1Cb3SgeaGSOfmjgBXjz8byhVkLxO-DBYqWk4ziEeCTSAEgX9CxpPSSsxrexnvLRlVM6TnJxxucg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f9eb9dc12.mp4?token=n3e9_0q89rhPhkXNb_cr6KrckGVdoMq8ZUwSgP9sMblpeKq5Q4pHTNhMRcd01GYulysJwfO_gn5LxWGW9xWVwB7X7Tx9HOEKqxJsPfBRTu7re8-XZwrlK2_GJMiJSJ_CU-0dCCgvKTHV2koW4oMS8Jdfk-ObtQkQiAZsv7Ea98Yws3DuSUKnaStsMjGDYERex8ovTnWryk7Tc6FZEI_HnaGXDW1A2kJ0fHHZBG1PJ0LqiulQarvgPDU54byoesyQ7v-3XsYEFUm1Cb3SgeaGSOfmjgBXjz8byhVkLxO-DBYqWk4ziEeCTSAEgX9CxpPSSsxrexnvLRlVM6TnJxxucg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه شکست دادن نفر اول شطرنج جهان توسط علیرضا فیروزجا
🔴
علیرضا نخبه ایرانی مدتی قبل به دلیل مسائل سیاسی از ایران خارج و به فرانسه پناهنده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/123182" target="_blank">📅 00:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123181">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c71d1a18e.mp4?token=HlCOW02zvh_-U-0zapyobfCeufEbT4yxdJwK6XtnDcY8E6Z-e7n3DXWmrc3Q7aSqeQfu4OjdT_yT-wY2vnQl-kWtYKZV_1tBpn7BF92FT0URQzJkt4XE4JkPK03i--bMaCYpsRdOPgO4HKij8ywRZAJ0rSXD5slFWAf3ViuKQ_3sMMnSCwoxbcaDSL9dFCpxzHUjB7ML0z9tm-UKBhbdaef2HwV69q3mPmmDxzWhzHLIa0B92NITzjiATmOGwVh9yX4WlfGb_IdmTRDc48m_8BmsaJqtHDheAoQLMEQ7Al0SYk0iTR6b1d1091Vt9OMQefvWuIwLueAHSu-Nh56YPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c71d1a18e.mp4?token=HlCOW02zvh_-U-0zapyobfCeufEbT4yxdJwK6XtnDcY8E6Z-e7n3DXWmrc3Q7aSqeQfu4OjdT_yT-wY2vnQl-kWtYKZV_1tBpn7BF92FT0URQzJkt4XE4JkPK03i--bMaCYpsRdOPgO4HKij8ywRZAJ0rSXD5slFWAf3ViuKQ_3sMMnSCwoxbcaDSL9dFCpxzHUjB7ML0z9tm-UKBhbdaef2HwV69q3mPmmDxzWhzHLIa0B92NITzjiATmOGwVh9yX4WlfGb_IdmTRDc48m_8BmsaJqtHDheAoQLMEQ7Al0SYk0iTR6b1d1091Vt9OMQefvWuIwLueAHSu-Nh56YPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دی تا خرداد.......
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/123181" target="_blank">📅 00:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123180">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRZ0cSxFnw_SoIVd0Vw3YbO3Ku0nVWPWL5Q6eIkulD0aC6PN3VhrQvbcfg3BDVHzFo6f3uJRIBY6oaUIumEU2e70Ig01zCHrzfkskK_WavpiuOnFLrj94yVLe0MR7gjxwZwHN6jk9-xXG2CyfKLkHEs8p5W2DuSp6haTdVPTRP62wXXO6StRfVt4obWr-rwP0wSCjwZLRK0ZAgJW3zqYXwFC9fvrgHFLENudjRB_ECzzkCYLSqHlyeCDF3jmB-Ph1OyTkyR8nYJ3DR1Po8e6bazricYF02G7cfa63NGWFao0DvNQfml629T4BZAd9-ykd14zunoPoqh01crv_MbceQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علیرضا فیروزجا (ایرانی) با پرچم فرانسه، نفر اول شطرنج جهانو شکست داد
#نخبه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/123180" target="_blank">📅 00:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123179">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
چین: تلاش می‌کنیم تنش بین ایران و آمریکا را کاهش دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/123179" target="_blank">📅 00:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123178">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c649a74dc4.mp4?token=V07DCYWoXOa34UdApsPQxZXLI7kFuUnuost-w-BgWrqydBZNpVF1PUefLhVdzWMf9Oji4VkokT9Ybu9glv7bFcJwDdgcQN7QD6pUbeBO7IPPklIGfwyxgUr5uXQsa7HHTI6Rvi1lQs0w65IAQ4QfyQnr5tA8iPOLOoUfQIJNxyHgrKn23gakEPWoyjho-uoSlhVJyHnRT1TnzLpwnQi8voieqp6uHnqKjx1DNrNpzyi6BgUQtNyXPZFtq58h5Cn0UsSxMjAVBlH6nAJwDOye9FTRUjTncwuxNlpUZFR4PdM3n2-jDyUQhMlTPuZ5wi6e5al6wUaIdHwhPZqaJUrHyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c649a74dc4.mp4?token=V07DCYWoXOa34UdApsPQxZXLI7kFuUnuost-w-BgWrqydBZNpVF1PUefLhVdzWMf9Oji4VkokT9Ybu9glv7bFcJwDdgcQN7QD6pUbeBO7IPPklIGfwyxgUr5uXQsa7HHTI6Rvi1lQs0w65IAQ4QfyQnr5tA8iPOLOoUfQIJNxyHgrKn23gakEPWoyjho-uoSlhVJyHnRT1TnzLpwnQi8voieqp6uHnqKjx1DNrNpzyi6BgUQtNyXPZFtq58h5Cn0UsSxMjAVBlH6nAJwDOye9FTRUjTncwuxNlpUZFR4PdM3n2-jDyUQhMlTPuZ5wi6e5al6wUaIdHwhPZqaJUrHyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه FPV حزب الله افتاد دنبال سرباز اسرائیلی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/123178" target="_blank">📅 00:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123177">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
عضو تیم رسانه‌ای هیئت مذاکراتی ایران:
سفر قالیباف به قطر درباره آزادسازی ۱۲ میلیارد دلار از اموال بلوکه‌شده، موفقیت‌آمیز بود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/123177" target="_blank">📅 23:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123176">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
چین: تلاش می‌کنیم تنش بین ایران و آمریکا را کاهش دهیم
🔴
به گزارش سی‌جی‌تی‌ان، وانگ یی، وزیر خارجه چین روز چهارشنبه به خبرنگاران گفت که پکن نقش فعالی در کاهش تنش بین ایران و آمریکا ایفا می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/123176" target="_blank">📅 23:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123175">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
گویا گوگل پلی تو اکثر مناطق وصل شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/123175" target="_blank">📅 23:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123174">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rrp6A4vnVlAdbjc1sGIbEg4XJCxIWNoyHRwTFrACreR0fis3LO04cdxrI2j71FkC_guRSNboiLOvx9Ympd2oNRcm77GolCPUGigrUPr0MTmBV759GmcdDYZon_D2hkLK6x8exLAYtPCTvj_yoOIDA2XMZ-IeerQE-M3GfslBR9EUYC3XJ-cFwO-aHDaVYykmB1_Q3-0f_AYZ52zDldrd4xYfwBN8J5kYUrU1YZifdZO2hwJ4F6_z8z0fq2BqN5W1djjUeb1aQm7ZapVnOSpiVEXETdSUwG1sX8NGhvnbmQGMAtAMw2ZIhqTT4XQrsSj5qda4mWZomFfxhQbSsM8cvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جایگزینی تسلیحات راهبردی مصرف شده در جنگ با ایران برای آمریکا، ۳ تا ۵ سال زمان می‌خواهد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/123174" target="_blank">📅 23:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123173">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
حمله امشب اسرائیل به غزه
🔴
احتمالا ترور
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/123173" target="_blank">📅 23:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123172">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: اصلا چرا باید به آمریکا تعهد عدم ساخت سلاح هسته‌ای بدهیم؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/123172" target="_blank">📅 23:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123171">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuYQFrLab-lr0s96qVEwSWm5rdmdeFf0teDoa__IG9NO_fv5UEt4OHPcowHbj6nXp27ZDjojQerOcEe4JDdpSyTHzqqCHm0TkDd61Jy5juqFtsBnCE86KyaT3rWPu0fDsRWjzD2k9zYZ2HTpadLUQNJFsIkXed0qmYQRlnm6ccBEJw_i7Gyou09EsQ8mR3K7cuKlpgs2WLOLNBHvERZygLEtftPJ-hNcX7n-220gVNKn5S-IOGsTcvxDvUCATYBPVvz8-d3ZBa7IBK77Z0Qhuz9aLIzF3uUDcMZlPAHA1xxJPte_KS2MnOhS7NDwvBbI2YmiflmFeGo3bFLq8pUd2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله امشب اسرائیل به غزه
🔴
احتمالا ترور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/123171" target="_blank">📅 23:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123170">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔥
حجم‌های بالا با قیمت‌های باورنکردنی
🔥
⚡
سرعت بالا
🌐
پایداری عالی
🚀
کیفیتی که حسش میکنی  همین الان جوین شو که جا نمونی
😍
@NetAazaadVPN  @NetAazaadVPN</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/123170" target="_blank">📅 23:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123169">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iDR9EkrUKKnrKSf_Z-q7PebyREsciJuPlp3xjMDesGeUEZYuvonMBfjZQWkMPhSfmVBgwY-Uw_REc_-pZzPs7YgH3aceiP_cctNmk3twyJkQ-ahbkqyH1VLoR1TAHKhTfC9-MOGUVLqgOK9STPu6trxNSgkyZgfQidkKklBPUZGcis9hYB6nWz_KMWlpTv6zlaf0yJwyc2EqfBBkw33NGzfSZn6t0qu2Pc4VyVGKanw3ImViNFR_tNkZQOflI6q1VlDJkkYgm_pGf9uMFX-n0A1TCZHK4Bpuu_9AfsKheOl2XD9MfhlkCxp6H_aeN29kNbm7Ip-zDqwzNNiT3OzEKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
حجم‌های بالا با قیمت‌های باورنکردنی
🔥
⚡
سرعت بالا
🌐
پایداری عالی
🚀
کیفیتی که حسش میکنی
همین الان جوین شو که جا نمونی
😍
@NetAazaadVPN
@NetAazaadVPN</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/123169" target="_blank">📅 23:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123168">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmAy379_kxZJo_pUnF0nTSGDz-nzu2_H95SePD03a6NmUleEBhCbpzbpGdbM_oIOhRFZezCNukIQVpUtXOdpCJPwfx--nokjh1atLg1n6Xf23sfGs0_SzlzO80MugBIA0F44eyjrV_LaZMy7vj0GqklRza3jLkv7hnEZ_79DFcOGgHEEHCiiKZ2VDLE86iPkw9q2_YbOIWk55Xk8y9PiG6D4hb1r7vKWcQCpkgO_aqA0ZdadNIKi7C-FbseyEgqZToEHTjqExXbKh8CDD0uptJQJKUFZZOHDMYb5nDMxiyQeMilXi_hSiT2A0WVHD6eUMluJx_Jelo0f05_ntTXd5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
کشوری فرد، دبیر سازمان لیگ: پرسپولیس به چی اعتراض داره؟ اونا حتی تو جام حذفی هم نیستن. 22 بازی نتیجه نگرفتن، بعد می‌خوان تو 8 بازی همه تیم‌ها رو ببرن؟ چطور وقتی خودشون میرفتن آسیا، مشکلی نبود؟
@AloSport</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123168" target="_blank">📅 23:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123167">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
بقایی: موضع ایران در رابطه با قفقاز جنوبی هیچ تغییری نکرده است
🔴
سخنگوی وزارت خارجه: جمهوری اسلامی ایران نسبت به نیات بدخواهانه امریکا که سابقه شرارت و تجاوزگری در مناطق مختلف دنیا دارد، سوء ظن شدید دارد و مخالفت خود را با حضور ناامن‌ساز آن در قفقاز جنوبی صراحتا اعلام کرده‌ است.
🔴
موضع جمهوری اسلامی ایران درباره امنیت در قفقاز جنوبی روشن است و هیچ شبهه‌ای در این خصوص وجود ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/123167" target="_blank">📅 23:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123166">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
امانی، سفیر پیشین ایران در لبنان: حزب‌الله برای حمله به اسرائیل در ایام جنگ ایران فرصت را مناسب دید، قضیه راهبردی است و اینطور نیست که حزب‌الله بخواهد در این جنگ طرف ایران را بگیرد و موضوع تبدیل به موضوع کلانی شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/123166" target="_blank">📅 23:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123165">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd6cb21c5.mp4?token=Lw2_iM77oGDJZgleuskJvaqtzv74uNgV3aWJEmBrTnVBvnOVd7P9EuzzXhTkW5dV6CtdZIZmFWHStmDqHUzYYF_r8KJhDMa2_aYFIjjAsNg87-TQ4hBW6ArJ3R_reNwRYADbYmqIsJsH8Uu5NZcNx5LMb6OqHl49bj2eAoKSeqQ3sAzaE68NQQfm7Rc97jByb_R1eygqk6Txay1BTQPxGKHjXI3380WYs1D0uYkvBpTjkSu3R1CIKV-3XjDErrHQeKOwQxJYKnoSDjMp8X4DeCd1-OKqred2aw5XJgUPLOwKYXbe8_XB_GIrcDJ8kwbdi7IfHl6a5-7sZT44SNXfug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd6cb21c5.mp4?token=Lw2_iM77oGDJZgleuskJvaqtzv74uNgV3aWJEmBrTnVBvnOVd7P9EuzzXhTkW5dV6CtdZIZmFWHStmDqHUzYYF_r8KJhDMa2_aYFIjjAsNg87-TQ4hBW6ArJ3R_reNwRYADbYmqIsJsH8Uu5NZcNx5LMb6OqHl49bj2eAoKSeqQ3sAzaE68NQQfm7Rc97jByb_R1eygqk6Txay1BTQPxGKHjXI3380WYs1D0uYkvBpTjkSu3R1CIKV-3XjDErrHQeKOwQxJYKnoSDjMp8X4DeCd1-OKqred2aw5XJgUPLOwKYXbe8_XB_GIrcDJ8kwbdi7IfHl6a5-7sZT44SNXfug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
من خود به چشم خویشتن دیدم، که جانم میرود…
💔
جاویدنام محسن جبارزاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/123165" target="_blank">📅 22:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123164">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
بر اساس گزارش «گلدمن ساکس»، تقویت ارزش دلار در نخستین ماه از درگیری میان آمریکا و ایران، موجب شد تا نهادهای رسمی خارجی اقدام به فروش اوراق قرضه خزانه‌داری [آمریکا] کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/123164" target="_blank">📅 22:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123163">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزیر خارجه آمریکا: طی روزهای آتی میزان پیشرفت در گفت‌وگوها با ایران را ارزیابی می‌کنیم؛ توافقی وجود دارد که می‌توان به آن دست یافت و مقداری پیشرفت و تمایل مشاهده شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/123163" target="_blank">📅 22:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123162">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBqhJjK2WnZTBT6oTmgSA7Q-8O21EgDkG8-pPZs4h2K3QFJbnDmM8p1vb96QFjdqatM1RdrWrZUVr2uLtcgHnd30_FGCFdse-neMfsfYjcDrJwK5MKSm_2DDNhZes8lY3IOAH4eNF1MNl-RaI2MbE21IE1gBovfW2JEyTb3EUqtUW39aHFMYwisOOfYst6a4XlnUPKR3yWB3s5xvOiF-i2yVVIZx8aHbDV67wB0E1FA44ki3KlU2wFNquzbzWqvkvQ3ADpMc7inBAXVZ9BKAe75t61spEucOuBdbfsi9kx7wg9_dHj7r3aBkS4u3uMjj84IFzY4kvz6gJyWYmIDuaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکر ترکرز: نزدیک به ۶۰ میلیون بشکه نفت خام ایران در نتیجه محاصره دریایی نیروی دریایی آمریکا متوقف و گرفتار شده است. این میزان تقریباً ۶ میلیارد دلار درآمد نفتی است که در حال حاضر به تهران نمی‌رسد.
🔴
با وجود این‌که هنوز نفتکش‌های خالی زیادی برای بارگیری نفت در دسترس هستند، اما به دلیل کاهش تولید نفت، میزان بارگیری نفتکش‌ها نیز کاهش یافته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/123162" target="_blank">📅 22:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123161">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
الجزیره: پهپادهای تهاجمی حزب‌الله یک سرباز اسرائیلی را کشته و دو نفر دیگر را زخمی کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/alonews/123161" target="_blank">📅 22:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123160">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgV2G-sCZtKzS32qtW_0Cy-mIfVIEHJOCZ50arPvaLfgBTxagxT1GwqrtVfnR5paaP785nbdkdHhrIFeut9Jt7SP-MQ9rc5MFYjhZK1x6tZsGP08z0InyLQLUBdgm9kSL9G48eHU0JxTubyKewHEIoLuVrbzyGuMN3wQgn2YnaOWxA6YH0UL0atxsUaz_AT_F1q7m2LZWE8ZM5vbXFMP89c-XrKqbzx7go7C1TXY49AYJOHsym65ZtHwoIz_FbqTnRNDeA39U_iKqRnNStvt51WA_1dUBH62JzfkZIToQ7MNNO1lLb0wY4CAhTPuOu_RVFc6xcQJeXZRPFbmmxooPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینم از وضعیت اینترنت وصل شده
پر از اختلال...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/123160" target="_blank">📅 22:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123159">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
هلند مدعی ارسال مین‌روب به تنگه هرمز شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/123159" target="_blank">📅 22:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123158">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
روزنامه‌نگار چینی: آمریکا و ایران به پیش‌نویس توافق دست یافته‌اند، اما واشنگتن نمی‌تواند تصویر «پیروزی ایران» بپذیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/123158" target="_blank">📅 22:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123157">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
نرخ ثبت ازدواج در دفاتر اسناد رسمی با ۴۵ درصد افزایش به ۲ میلیون و ۹۰۰ هزار تومان رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/123157" target="_blank">📅 22:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123156">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGRd7Rv2pbNQ_2KzW6LHTihFbITzR1mCZDwYIaxX9_RhHjX6h6Srhn1XkPRd6Bvbd7n7rLUWZtW6vfQRl7sEoJfmPHaV8extciDHsLHL4Jzj4cQOEi7gYPZ-5rXxDFfWAilD0oxTXXNbp5N_36ki3itwx-l0ZXxy2WAnm7qY5QvulNnU3TmqtOlTd4Z3JNvTfvMtSjOBo56a2nzKCY2gxefjDaJSX78huVciFTLzl8OWX_DP_yoJ7kyFiPlD4UwYimIVvcoldawKSoJEILWcKsLLtT6Klt6SHS1GquLa8g8KNjBBDm8OGCgkTmLAgNS5Hyzxf-d_VfTC3HAXhV32Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسوشیتدپرس
: تحلیل جدیدی می‌گوید ایالات متحده ممکن است به ۳ تا ۵ سال زمان نیاز داشته باشد تا انبارهای مهمات موشکی کلیدی که به شدت در جنگ با ایران مصرف شده‌اند را بازسازی کند و این موضوع نگرانی‌هایی را درباره آمادگی برای یک درگیری احتمالی با چین برانگیخته است.
گزارش می‌گوید تأمین موشک‌های کروز تامهاوک، موشک‌های رهگیر پاتریوت و سیستم‌های ثاد به شدت کاهش یافته است. حتی با افزایش هزینه‌های دفاعی تحت ریاست جمهوری ترامپ، بازسازی موجودی‌ها سال‌ها طول خواهد کشید زیرا ظرفیت تولید محدود است.
تخمین‌های زمان بازسازی:
موشک‌های تامهاوک: تا سال ۲۰۳۰
موشک‌های رهگیر ثاد: تا اواخر سال ۲۰۲۹
موشک‌های پاتریوت: تا اواسط سال ۲۰۲۹
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/123156" target="_blank">📅 22:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123155">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یه مشت جاکش هم نشستن اونور دنیا چپ و راست میگن مردم قیام کنید حتی اگه شهید بشید! خب جاکش تو خودت میموندی همینجا قیام‌ میکردی نه اینکه گوز گوز کنی  [@AloTweet]</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/123155" target="_blank">📅 22:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123154">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
فرار گوسفند قربانی روی پشت‌بام ساختمان در الجزایر!
🔴
در شب عید قربان، یک گوسفند قربانی در الجزایر از دست صاحبش فرار کرد و روی سقف یک ساختمان دیده شد؛ صحنه‌ای عجیب که ویدئوی آن در فضای مجازی پربازدید شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/123154" target="_blank">📅 22:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123153">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGva6NzZz5Vu3qZbor-dgILuGV25ji3Ls89FMrVpTFy5gFqfBKFujN-EKkYxVio2HiD020yYvLwHsSBVJyErzMqp45ks38304obW13YbcJuoH82UQKBvnvp3Tz4P8-ngVf4w1Q_MYhbX_2M7ChEyudJIO_0v0bWqr8cPAO9eguuR5732p85PvDiRwNpsoCHiEx8sUg5woPkOEntog_qoTE5bqX534lX5cJyhK2s6FZ8wym6jAlHdDOiqnNUrChqnX9BgyMeaiPscFfUcJZVacnGqiZUOujha3i9FgkNPA5I8DBdgn1EyU7bl8zXVSuNFo-uIVnI-Wa4MBOie1mBF2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/alonews/123153" target="_blank">📅 22:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123152">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
اسرائیل هیوم: ترامپ پیش‌نویس یادداشت تفاهم با ایران را به نتانیاهو و رهبران منطقه تحویل داد تا نظرات خود را اعلام کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/alonews/123152" target="_blank">📅 22:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123151">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJkmYH7PxbqNPQ8WafnWh0jL1cPhgvbXO7lPwGlPOy209tfcUTUYysARaJPostjukQPxqbhgEXp97dyCsZo9I1V7XEr9AmS2fU4Gl2ItEMxJdhtRiXG11Hqi6NJ8228VGxgP_qmNnhigYVnVYVb8QuVplfDgnevY7_WIsr0tZyuL6E_-eBXAlbH3tnHybJZmr352yTyYJdsbvl6efOnCJt5TDY-UEaxrrAHrERIjwYe_pNtgRgI-ApNDXIqrxsRt4iEa6-ALXG0ro6ALqG3l__1jYX9mza4JbcQl6KvtI3zv-z1iU2dsz8_E2tQnFP9qEoTFov4JLHI73mvAuUPRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ملت کارزار رفع ممنوعیت کشت خشخاش رو راه انداختن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/alonews/123151" target="_blank">📅 21:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123148">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c78b1410fd.mp4?token=aGY3wsaul5vTT336uH0FzzFNPXz2qDzwdA84QOWe1_KYoyGNPwj2kFiuG5-g4he0m3KpPaCoAjS_rIQ_hp8PXKS8cCJqis-GYpTrxAr_8j0NiD4JoSBjYtPNbO3uDzddryJNAO6kJXxjy4DbAteJUd8ElKd-ZDlOSVgVDfNVOwDUAz3yIs9kjfitKR3dnvh51TQ3KmcfVL3yrFz1jgMGy9ZXjcjQQP6EzHpGV_DzBbRW-V46-8iLOus8jgzATIQT-QJXnpQTsk1nP61LiC-gWSF-pSy1mpBOIOKrOVwGoaehRp7lDlUhtZKhT82lamlgDtzP6sXTXrHUPZ8qlQKNfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c78b1410fd.mp4?token=aGY3wsaul5vTT336uH0FzzFNPXz2qDzwdA84QOWe1_KYoyGNPwj2kFiuG5-g4he0m3KpPaCoAjS_rIQ_hp8PXKS8cCJqis-GYpTrxAr_8j0NiD4JoSBjYtPNbO3uDzddryJNAO6kJXxjy4DbAteJUd8ElKd-ZDlOSVgVDfNVOwDUAz3yIs9kjfitKR3dnvh51TQ3KmcfVL3yrFz1jgMGy9ZXjcjQQP6EzHpGV_DzBbRW-V46-8iLOus8jgzATIQT-QJXnpQTsk1nP61LiC-gWSF-pSy1mpBOIOKrOVwGoaehRp7lDlUhtZKhT82lamlgDtzP6sXTXrHUPZ8qlQKNfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله‌های سنگین ارتش اسرائیل به صور جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/alonews/123148" target="_blank">📅 21:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123147">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AszSncYCA3E1SstWkg4lFZh4r8JHcfXyFmyV198CLEeJEvyTrqHOfzmbnuSiC-5oTXASZpWhQ2yJ0oE9qYsrg3V2FAoPQNBNUZxsEXju9mcu6DLkcA7pvfoDYEteP5v844D48fQwhkaCmg4o0XXfOFvj5RJE-JFTSD1RuZMk-EEQR5RKHjfGrAerLfNRxpbYT3iro_WjWjLBbfvvM1JAIWKVHs6ko0Xxqa9eq5_zNUwpbVSl2ZRdCbtjJg0eGUllfW0ulsCNhNcEdB94FLznIZPDDyRjnqFDIX3e3lbTrXqfLMSEllco9MzY2jNVp_7MQ1GmbgNdzemzgOTyq21KfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک گاومیش بنگلادشی که به خاطر دسته موی بلوندش، «دونالد ترامپ» لقب گرفته بود، پس از آنکه ویدئویش در فضای مجازی منتشر شد و مشهور گردید، از قربانی شدن در عید قربان نجات یافت.
🔴
وزن این گاومیش ۷۰۰ کیلوگرم بود و قبلاً فروخته شده بود، اما دولت به دلیل نگرانیهای امنیتی و ازدحام جمعیت برای دیدن آن، وارد عمل شد.
🔴
مقامات پول خریدار را پس دادند و حیوان را به باغ‌ وحش داکا منتقل کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/alonews/123147" target="_blank">📅 21:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123142">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AeW9BOHopE6BDD5ihths90YZqRoumcMjOSkyjYP9EjUKAlEMKrtVqe4E7CDdUq4buj_NY1BRojwBrBCnZSVl7p2EUE2yvBkQIZ_cuwlFk3LEoZjEX-Ysb4H15KKamTePwfZ6d2pMsEX1FigL0ohR76yWvu6Q5bzi9IQBg9VgDxl4Bimcq_z3JRM4KmwHtWjMs3TR2Kyz0yGA_oCQ4Lelq8E7F9YFkVdtzB56itwRmxQZpPD8tAE3RisA8vmkIa2UWx7y83Jxu-xrIIuqObxFSNTuPjeJNA35EUVB7VQWmqAap5m-is-tsTM2WqGl0j2hCe1aXX5edfdkkpaM-RFv6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SWgXxi107mdY-P_XNqOvahBaAgjmQyfufSuvVkCNmN3BgD9AteQdYAedNGuKDVneUx4PYwJROVvDAfTxKjdAjnRGrBrvr-fkDjBjKUE7VLLht7HntJYOIgdV_16ypMBr5IxMO4KGQZ-koA-Ag5by5SoyXgf65J6sSsbQWBBof9LyI9BM2ld9D7Je7yQutqw0W75391n0pWdIk3np0q2nPfWaSXsed78mlROO1r_Bvz_c7xJKJTEB9wLuI4_Xxx_MljDttrxLS4LAANPVApCzx27Iv3TUnzLDPHiOXvrFXaLyOwAUHW5CKT7fybLmbpTUoC5L61zK5Tj9lIzYSNX1cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbcyVcEMXlUo1lX85UadzEw6x9QN85jXwshu8STj2hGnFEhxuLIIzePq-7yEnc08_o_bmpS4a4-zr7jkWa6ZUn3BxxiJ6B5kPlKAM1Ab8berk0VDkAEtZcUlDNK-fx--IOt1QlOHeuygi89dEWSP1yl9GQ7A40QTTKpWctDL8T6ANHg9taQvtmaWvAKM3q9UE2zKUMPtbEuEI2eVG1Fl4Mvwm-XTa2HwZka2Xx2hNZ_TVfbeNIHGbs981jkSLk_328wO7m1TnTeUdQp5KEDQqOh4aUsifaqpSjvgAKB_25CZ4SDNYCB8rkK2EBaUn-dY1S9XNMTRSyxA3dwFSLiShw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AzLArf0v0ey6w0Hikja1Uk42eHCkrohG5vpOfME2VTz5s1p-aV4ulL7-W4X5H6LqG4smRPssIrXfp52kzjihaIEOb_Begj7QwbIk0EXLqcaqZOHCyZy1hWP_GccjzZzoFj_IJmaxSsd0Z9971OFERYxTSj8C1d1gqgOnQvfF8HagCFNO6h-dyveBUIRwpKPKDWG5qX3BO0O-7GVADiStwxq-ChGYiEpFGsG_5rS4YKb18D9V_RyH440ZeMJtfDKUv6mQHSGyowr4H6Cm2p33tD8BF_DX1kbfwJYA7p7HKSTECvVvnerVuwke7Y3IECgbZ2-ckDUBst7xvz_7ixqdtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e5e9e4dc3.mp4?token=PtNmyNAOo7lY3eEfvkzo-uwvdKMv8AjxUWrTc8c7VpZDaykqga0kY7aH3_URyrBXXn7YlAmo8zENFE95oa0uN_BWq1-DPptFJ43v983-uS5mFWHMc0Mo_a8AINVtDj0pUyGCLMqnmdfrKOXvdszrGShEcOnqy7VGAK5ikfSb1hlj4oTiGJsZHAivL1psvWVEimGBvIbLyYSQKSnjFHHv2ajBnu-GTAZotkcqyXyYaBa6yeIY6BshrI8gCKt_0_7YJyUMorUZflRAPII1-nJWhFKnf1WAkO4naZnA5JEIb_2Dsr0IY6Iow0IKOvctVkcl6aHeYSfMdnCzunt79zxn2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e5e9e4dc3.mp4?token=PtNmyNAOo7lY3eEfvkzo-uwvdKMv8AjxUWrTc8c7VpZDaykqga0kY7aH3_URyrBXXn7YlAmo8zENFE95oa0uN_BWq1-DPptFJ43v983-uS5mFWHMc0Mo_a8AINVtDj0pUyGCLMqnmdfrKOXvdszrGShEcOnqy7VGAK5ikfSb1hlj4oTiGJsZHAivL1psvWVEimGBvIbLyYSQKSnjFHHv2ajBnu-GTAZotkcqyXyYaBa6yeIY6BshrI8gCKt_0_7YJyUMorUZflRAPII1-nJWhFKnf1WAkO4naZnA5JEIb_2Dsr0IY6Iow0IKOvctVkcl6aHeYSfMdnCzunt79zxn2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حملات امروز به لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/alonews/123142" target="_blank">📅 21:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123141">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
تعداد تلفات لبنان از زمان شروع جنگ آمریکا و اسرائیل با اسران به ۳۵۰۰ نفر رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/alonews/123141" target="_blank">📅 21:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123140">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a49d8fc6a.mp4?token=iqVuxvKvfhAg76AzpsDeoefYLYOCKgBZDjN7DQ04rxMiTJ3tEwSSXuJVkQsSf4m4h3Td43M1UDcsUP1hedWGNTHxShT0uK9KaUFuXt-t8nJwSoJDMFCfIoMArpFRtuLYoiq8N7PORvasq9Zsy5IkuNQLpVwJCU5o03CUEaBgoow_HSRYrK8mN50gByQTwODbd5hmHmEXqu1uBt8_sxu6IbCzCz_23-Og-U5ZJl3XfiU2rrPZcpmvYI-hNDcK24cwc5deC1jGeEF36FGA11iTc6_4lRGw-Tus4blBl2DdNx3IaJt2vrY-m083tFcajKYTAqwZoGiFAhBuvNk4dV0JjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a49d8fc6a.mp4?token=iqVuxvKvfhAg76AzpsDeoefYLYOCKgBZDjN7DQ04rxMiTJ3tEwSSXuJVkQsSf4m4h3Td43M1UDcsUP1hedWGNTHxShT0uK9KaUFuXt-t8nJwSoJDMFCfIoMArpFRtuLYoiq8N7PORvasq9Zsy5IkuNQLpVwJCU5o03CUEaBgoow_HSRYrK8mN50gByQTwODbd5hmHmEXqu1uBt8_sxu6IbCzCz_23-Og-U5ZJl3XfiU2rrPZcpmvYI-hNDcK24cwc5deC1jGeEF36FGA11iTc6_4lRGw-Tus4blBl2DdNx3IaJt2vrY-m083tFcajKYTAqwZoGiFAhBuvNk4dV0JjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جمهوری اسلامی در 18 و 19 دی مردم رو به گلوله بست و مدعی بود که این جمعیت معترض تروریست هستن.
🤔
دروغ از پایه های قانون اساسی این حکومته
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/alonews/123140" target="_blank">📅 21:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123137">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c78b1410fd.mp4?token=QQj7LjFk9aZm6uxxllhjWGhyVFgyFl6M5ZWQpcmUcPtKy-XwDnwEjbwFF87lTlTpKFYMqcoPqN5sSkrgZXQcbwaQXx66ZR39dZ6jeywEGzOwxrlv03w2QxMNWZC75pGdljrS7HfpXqwRlMOZF7Uq1g3an5AB4-RFZdhpEqc592i26IFLTwKn1oHPNGpvEidjOVy6DpHzh37IC3D2AdoDW252KoahMYZjPVRODQrVE-Z1Bt6GOLRPLeookXDIJTG8jBkp8p1pIvxMUOFqEA_b3BvVlb6nUMd7vjHDuc74B9wqUjXZv9GUBcfB48iQDXyuvN2hJ27QK_BSeWBVKyW0pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c78b1410fd.mp4?token=QQj7LjFk9aZm6uxxllhjWGhyVFgyFl6M5ZWQpcmUcPtKy-XwDnwEjbwFF87lTlTpKFYMqcoPqN5sSkrgZXQcbwaQXx66ZR39dZ6jeywEGzOwxrlv03w2QxMNWZC75pGdljrS7HfpXqwRlMOZF7Uq1g3an5AB4-RFZdhpEqc592i26IFLTwKn1oHPNGpvEidjOVy6DpHzh37IC3D2AdoDW252KoahMYZjPVRODQrVE-Z1Bt6GOLRPLeookXDIJTG8jBkp8p1pIvxMUOFqEA_b3BvVlb6nUMd7vjHDuc74B9wqUjXZv9GUBcfB48iQDXyuvN2hJ27QK_BSeWBVKyW0pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله‌های سنگین ارتش اسرائیل به صور جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/alonews/123137" target="_blank">📅 21:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123136">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibkGd6Xtqx5VbbWKal_mJInoqfyBGRp-v77T0i30EyE0-OhTVEFs1zO87widCqy51pJCt9bgTeHgGzDq0Wm5o-ejlK2NBXC5wIYBy-nujB_CHrLhStW2vgrNp_jUGkMuf__w1pKX1So01zydh5syiw042TXBpV-AA_zb4K57CpmGuqZyiy9GvrNbA9C3SuyN25jbBwW61UvQNbGP0uP5tKqegKysjFTYW-PpLQJZ7dsmuGmKabzg4ep0KX9mqqs1pymWe8OnoclKEatT6CWRfnSoHbTNVtmp89Lg431VuPmK6fOSljCeuZNMkXeRisHPQkEwR_YTGfPacyA2cIYXmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله به پزشکیان در تجمع خیابونی‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/123136" target="_blank">📅 21:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123135">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سفیر ایران در کره جنوبی: ما به هیچ وجه به یک کشتی کره‌ای در تنگه هرمز حمله نکرده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/alonews/123135" target="_blank">📅 21:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123134">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
نروژ تحت توافق امنیتی جدیدی که در پاریس توسط نخست‌وزیر یوناس گار استوره و رئیس‌جمهور امانوئل ماکرون امضا شد، به چتر هسته‌ای فرانسه خواهد پیوست.
🔴
استوره گفت این اقدام در پاسخ به وخامت وضعیت امنیتی در اروپا، از جمله تجمع نظامی روسیه، بازتجهیز هسته‌ای و جنگ جاری در اوکراین انجام می‌شود.
🔴
نروژ تأکید کرد که در زمان صلح هیچ سلاح هسته‌ای در قلمرو نروژ مستقر نخواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/123134" target="_blank">📅 21:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123133">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDOoEcWEjTZVWYkzt8VfL0-sl3rIA-xbOrMUDnnJxTOgb1yJ9W-Zr3_kAMwoN1Z1ps_1cf_KesA9L4Ycn3xG0CLsDYfTX8mp8-iJVonL5yGM3Eo-QamBb0DQZ6Ipaf2P7Mtxj65nHjDOIClI5owX5PLFzs1v109f7ipAETU9R8pVv_2vvze40WvMzyZ9BV7bCmSmwanesoz1ValX1tcVDbBDsb05EoEXyCMJk9QYmJoion1pU9Cgs8hbmaJVXWUsNaCBwr1oYhqx6U4kexJ-tac1WIxaKlnWSJqWBhSQEGmdX13TCcJ4fcAE5hoUcaMU0Yu36hQVYn2Wdho0JCq-ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر امروز ماهواره کوپرنیک از وضعیت دریاچه ارومیه و مقایسه با زمان مشابه سال قبل که نشون میده به نسبت پارسال وضع دریاچه خیلی بهتر شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/123133" target="_blank">📅 21:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123132">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bG4GMriDK-z18wjKtVzaQLEdpC64DXIJ95BEFqSKZRRUPCviScAMuMH-Inkm19sf30vJGw0txIzYjDDaj9SMWdlW_yfQb4PWzTpoo4P_Py42ZL0vckQ4Y3eA7_VBDTyMO2eoEC1tqVC3i_EKDagIO9liFkFFN1YdKqVK3qQ8MvG2laYnEsRBZHQY3wZC7f5a_loI8tZjd6oLs3nkMqHP9Wp6CpdUC9umJxESHD_mY2cO6Q3uoYhWe-jSOQhhVkY1PIIpBJrUfIFfCKAi8EbYy7pa0PzyvRTMpVPkdpzzVa7Hy52DSKnuLVTiyHnBDX-_uUz1E852TY4IxLkVQNhBfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سال ۱۹۳۶ که درهای دانشگاه تهران به روی دختران باز شد، رضا شاه قدمی برداشت که حتی از مدعیان غربی هم جلوتر بود!
🔴
جالبه بدونید اون زمان، دانشگاه کمبریج هنوز به زن‌ها مدرک رسمی نمی‌داد (تا ۱۹۴۸) و هاروارد هم سال‌ها بعد (۱۹۷۷) پذیرش کامل زنان رو قبول کرد.
🤴
رضا شاه روحت شاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/alonews/123132" target="_blank">📅 21:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123131">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
بلومبرگ: رئیس‌جمهور ترکیه، رجب طیب اردوغان، در حال تلاش است تا هم‌زمان با برگزاری مسابقه فوتبال جام جهانی میان تیم‌های ترکیه و آمریکا در لس‌آنجلس ماه آینده، دیداری با دونالد ترامپ ترتیب دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/alonews/123131" target="_blank">📅 21:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123130">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
صدا و سیما شرط جدید ایران برای توافق با آمریکا را اعلام کرد: پرداخت غرامت ۳۰۰ میلیارد دلاری از آمریکا به ایران!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/alonews/123130" target="_blank">📅 21:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123129">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ecae41bf8.mp4?token=jNVu2fEGYkrcORGbZHe1pawUjAe68XCvWUc8mmSoxyxbg94f8l1VfWAe1ovUy8ZsomrFaw9oyj9WZObIHKN-KT7DUc1AudviBc2-26iP-2iX9QjjL5QI69vVHPZx99t1lZjcx15JkfzQs9uyAeVCPvhMerXf2R9KodWZddQz8oUKKyrTbhoZYrXiEg4NbEmGM51l6dvWuvR76tiYMUtzXjer_P2sNg4y9Ys3z0PjfzT0YhxP4QshXc5n87gDcbzfPGqoyFLWIJD4sfbr6bZZaUca3IxpyrivuJTMkJeKybZowZUBHV5fAvtqpegy2CgxCjrJ45dpUfd4xBEIWvbTQYnn21aP3dToujaVlU5RATiSPT4WO-rheLrtBwzuHuc49yXbBeBFUbz8uOWtD5lTiL7tsvSqx7EROyu9qJA0VZMJBmtt71DHccttqlnx8SBnk3ypKQ6LE0uX9yT43z5nKsa8uUBTHZ5j6Cuf1odzjMaB69ne8XnUmcUXXFLZvkHirYyLNuWqqIAoZVygA0VSq9o_bKVDes-SeGV82dBY_Ihiz0anyP4y5GxLWv-oefiCBq1kWiusjDAvVohpiyo8htbDCPqJTB1aoOR_j-XpmUDoXvV6CUOfgI57OqP5P0KWRn8CL0jLbbSC90eG36H7uhh_w3BboNs6SI6HcsnlcKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ecae41bf8.mp4?token=jNVu2fEGYkrcORGbZHe1pawUjAe68XCvWUc8mmSoxyxbg94f8l1VfWAe1ovUy8ZsomrFaw9oyj9WZObIHKN-KT7DUc1AudviBc2-26iP-2iX9QjjL5QI69vVHPZx99t1lZjcx15JkfzQs9uyAeVCPvhMerXf2R9KodWZddQz8oUKKyrTbhoZYrXiEg4NbEmGM51l6dvWuvR76tiYMUtzXjer_P2sNg4y9Ys3z0PjfzT0YhxP4QshXc5n87gDcbzfPGqoyFLWIJD4sfbr6bZZaUca3IxpyrivuJTMkJeKybZowZUBHV5fAvtqpegy2CgxCjrJ45dpUfd4xBEIWvbTQYnn21aP3dToujaVlU5RATiSPT4WO-rheLrtBwzuHuc49yXbBeBFUbz8uOWtD5lTiL7tsvSqx7EROyu9qJA0VZMJBmtt71DHccttqlnx8SBnk3ypKQ6LE0uX9yT43z5nKsa8uUBTHZ5j6Cuf1odzjMaB69ne8XnUmcUXXFLZvkHirYyLNuWqqIAoZVygA0VSq9o_bKVDes-SeGV82dBY_Ihiz0anyP4y5GxLWv-oefiCBq1kWiusjDAvVohpiyo8htbDCPqJTB1aoOR_j-XpmUDoXvV6CUOfgI57OqP5P0KWRn8CL0jLbbSC90eG36H7uhh_w3BboNs6SI6HcsnlcKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره فوتبال: من آن را ساکر می‌نامم.
🔴
می‌دانید، انجامش ساده‌تر است، چون ما فوتبال داریم و آنها دو فوتبال دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/123129" target="_blank">📅 21:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123128">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ: ما میتوانیم همین الان یک توافق خوب داشته باشیم، اما شاید نه یک توافق عالی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123128" target="_blank">📅 21:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123127">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JuYvdSCCle2e6-oTaN3yrvMCk5q-Ot8FMi91iMyv7qAGfdBN-Bpm4idhkP1rwC3tSxfDzer5ctgB1X7P0riIZab5l1txhFQoclHwZ1PTaNgTZXAC8khmzx7iuW1S0yzVJou9tHpQOfwZxAbmJK7eYjU-VqaqwKvec6bYJbambUrT3FljC5Smxq6TvETX-35LLDV84VxlhSPp3Rjb3DnquSbRd0SLRRtHQQLYEkRsTz9ogfqJ_wOI59hUuJRZmBeu8k_VpcHrs6KRUVIOf311yfIIJLQSU2j0BA8YwGX5L_FiJH-Pi6X7SEzQab3-aZsUKdJqcDUeaU8IV6RIZmq-Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از کانفیگ فروشا بعد از وصل شدن اینترنت سکته کرد و مُرد!!!
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/alonews/123127" target="_blank">📅 21:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123126">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e3f045f53.mp4?token=IccAodZuOZWV75vnVpxrUUU4GgAIHcMDpOciI8ZYA7i6hVXAQ111vpA0p4E6PbdnkvsfCi0G4rrUINHU-Ih43Bi09gYjf3Rxfu_KqhsCKE3_TFzvxjO-U0O9xHDyxcz6jgYW9ebWUkTq2-xggBaTp2MfBvbc3J-CfUpApiHGImqi7nccPtMtEHQbV6_4iArhHj-Vn_7Fdz42fGxW3w_3n8g4HzlY25r-A1Qosi4igmQcJukUlnRGzJd0R02kGEB_s7U3Ucv5l2QHpwqKCUiCyGRM8fpvKc-OGqnsoqBWUOVEzp1IcDFpv4Fvp4fxtTQjl-QqiSwxgcq0uCqNrQHunA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e3f045f53.mp4?token=IccAodZuOZWV75vnVpxrUUU4GgAIHcMDpOciI8ZYA7i6hVXAQ111vpA0p4E6PbdnkvsfCi0G4rrUINHU-Ih43Bi09gYjf3Rxfu_KqhsCKE3_TFzvxjO-U0O9xHDyxcz6jgYW9ebWUkTq2-xggBaTp2MfBvbc3J-CfUpApiHGImqi7nccPtMtEHQbV6_4iArhHj-Vn_7Fdz42fGxW3w_3n8g4HzlY25r-A1Qosi4igmQcJukUlnRGzJd0R02kGEB_s7U3Ucv5l2QHpwqKCUiCyGRM8fpvKc-OGqnsoqBWUOVEzp1IcDFpv4Fvp4fxtTQjl-QqiSwxgcq0uCqNrQHunA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فلکه گاز شهر رشت، 18 دی ماه
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/alonews/123126" target="_blank">📅 21:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123125">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyJBzQtKo1URd1FKFA73owxXXMG4-grPzw5_D0PxpAdhkktwWA-zund_oeWc6dFOE3Pwa7in6fAY-o4bu4tBPMW_hpfp6IJWoveP1ZcJU31LHX_pSYe7u9SSzhBXoRGZ2O-VVTdcWkNQlZM6Fh7cDqcUKNZRAknktS6pM5pjtazi0pLNJ93wlPq4UJYDTElyiyPbtID-q6HfxMoth-SbgrXQ56FlCKcWmu2xbAmRgNpEEDbXL8SteYzemBcrhnlJ_hOAZNIprxEalbW9hZTHgXGl_1y3PWbLlMecjTIvibJ8RbjDO2zxU0tK9q1N6r1-0NpiEj3b_u6zX5vtoiBJIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ریزش سنگین بازار سهام آمریکا بعد از اظهارات ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/alonews/123125" target="_blank">📅 21:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123124">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
یسرائیل هیوم: ترامپ پیش‌نویس یادداشت تفاهم با ایران را به نتانیاهو و رهبران منطقه تحویل داد تا نظرات خود را اعلام کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/123124" target="_blank">📅 21:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123123">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ترامپ: اوباما کشور اشتباهی را انتخاب کرد. او باید کشور دیگری را انتخاب می‌کرد. به شما نمی‌گویم که آن چه بود. او وقتی ایران را انتخاب کرد، کشور اشتباهی را انتخاب کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/123123" target="_blank">📅 20:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123122">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ترامپ درباره ایران: آنها شروع به دادن چیزهایی می کنند که باید به ما بدهند. اگر این کار را انجام دهند، عالی است.
🔴
اگر این کار را نکنند، هگست آنها را تمام خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/123122" target="_blank">📅 20:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123121">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a286aadd.mp4?token=VM7Dz_sVauEbsZGFe16RsT9rxoNczNvkJI_HSSxHv41xnUhBS852NpOUzdu37s2FhFI3sG702U_U2CjmYtG51xBiRELjX_tx9xnKjgYU2aog1-10XE6qHR0z9jkE4kkJ_p5FExxvqJ_uR35SFiRtHGM1ASan2i7tOHhGH1X-HVHswZcnxlyKXdCsTLTSFS9qz67NrVsZKC72F72eVAdDCCwU8TJMMXZPCS6VgPL21Sprp8FcniqbF3YsYE633WmLbY5d9XOIc7zZ39tonyUdCT_gnDh4D3kK8UCnC_q36PQ2gHQ5HnSDM3Dnlwfnv7erEcZmGiBRTiCw2zHbCvPVDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a286aadd.mp4?token=VM7Dz_sVauEbsZGFe16RsT9rxoNczNvkJI_HSSxHv41xnUhBS852NpOUzdu37s2FhFI3sG702U_U2CjmYtG51xBiRELjX_tx9xnKjgYU2aog1-10XE6qHR0z9jkE4kkJ_p5FExxvqJ_uR35SFiRtHGM1ASan2i7tOHhGH1X-HVHswZcnxlyKXdCsTLTSFS9qz67NrVsZKC72F72eVAdDCCwU8TJMMXZPCS6VgPL21Sprp8FcniqbF3YsYE633WmLbY5d9XOIc7zZ39tonyUdCT_gnDh4D3kK8UCnC_q36PQ2gHQ5HnSDM3Dnlwfnv7erEcZmGiBRTiCw2zHbCvPVDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: این تغییر رژیم است. یک رژیم از بین رفته، رژیم دیگری از بین رفته، و ما با بخش‌هایی از رژیم سوم سروکار داریم.
🔴
پ.ن : تنها چیزی که تغییر کرد مارک سیگار من بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123121" target="_blank">📅 20:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123120">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری / ترامپ: می‌خواهم عربستان سعودی، امارات، قطر و دیگران به توافقنامه‌های ابراهیم بپیوندند
🔴
آنها «به ما بدهکارند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/123120" target="_blank">📅 20:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123119">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: آنها ممکن است موشک داشته باشند، اما در حال حاضر نمی‌توانند موشک‌های بیشتری بسازند. نمی‌توانند پهپادهای بیشتری بسازند. نمی‌توانند کشتی‌های بیشتری بسازند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/alonews/123119" target="_blank">📅 20:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123118">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ترامپ: به درخواست نخست وزیر و فرمانده ارتش پاکستان، به ایران فرصت کوتاهی خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/123118" target="_blank">📅 20:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123117">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a107aa436.mp4?token=WKPk5QqfZFxMcY7onc6ktq1ObLH5A7XGQn8aYd8hyiMx8Z2uXnWWexgvnavhdSfR2HfzHkDRfZGsxPUP-kexZzBlKD-PP4DEMXZzgJPxw3KFz94GRuoqNQ3oJAPdc-yW6nvRm6tTiVXS48mLLjf1UFM54y5C86tPm9gTEf_nDOe59cm1K3pVIlrAgjy1o656-z8Z9tfMgFAjvRVxVmPCjGM3itczuv9ceQtt416ZPTLkwssy771GOY8jLQDpyz8UETjSGOb6Ykvn4jVvBpMjL6b3yIaQy5wPJi52nVaKRFH97EZkXA9Nm9xqC2PAdau2RzkanX4-ge6NM_Hx4i24KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a107aa436.mp4?token=WKPk5QqfZFxMcY7onc6ktq1ObLH5A7XGQn8aYd8hyiMx8Z2uXnWWexgvnavhdSfR2HfzHkDRfZGsxPUP-kexZzBlKD-PP4DEMXZzgJPxw3KFz94GRuoqNQ3oJAPdc-yW6nvRm6tTiVXS48mLLjf1UFM54y5C86tPm9gTEf_nDOe59cm1K3pVIlrAgjy1o656-z8Z9tfMgFAjvRVxVmPCjGM3itczuv9ceQtt416ZPTLkwssy771GOY8jLQDpyz8UETjSGOb6Ykvn4jVvBpMjL6b3yIaQy5wPJi52nVaKRFH97EZkXA9Nm9xqC2PAdau2RzkanX4-ge6NM_Hx4i24KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما چند ماهه داریم این کار رو انجام می‌دیم
🔴
جنگ ویتنام ۱۹ سال طول کشید،بین دو جنگ، ما ۱۳ نفر رو از دست دادیم
🔴
این خیلی چیز وحشتناکیه، ولی اگر به تلفات جنگ ویتنام و جنگ‌های دیگه نگاه کنید، اون‌ها صدها هزار نفر از دست دادن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/123117" target="_blank">📅 20:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123116">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری / ترامپ: ما در مورد کاهش تحریم‌ها علیه ایران صحبت نمی‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/alonews/123116" target="_blank">📅 20:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123115">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ: اگر ایران آنچه را که می‌خواهیم به ما ندهد، وزیر دفاع کار را تمام خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/alonews/123115" target="_blank">📅 20:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123114">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ترامپ: با این‌که روسیه یا چین اورانیوم ایرانی را بگیرند راحت نخواهم بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/123114" target="_blank">📅 20:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123113">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ترامپ: تا زمانی که ایرانی‌ها رفتارشان را اصلاح نکنند، هیچ پولی را به آنها برنمی‌گردانیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/alonews/123113" target="_blank">📅 20:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123112">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ترامپ درباره منفجر کردن عمان صحبت می‌کند : تنگه‌ها برای همه باز خواهند بود و تحت کنترل هیچ‌کس نخواهند بود. ما مراقب آن‌ها خواهیم بود.
🔴
عمان مثل همه رفتار خواهد کرد، وگرنه مجبوریم آن‌ها را منفجر کنیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/alonews/123112" target="_blank">📅 20:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123111">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa3da0b6f4.mp4?token=LU7l5LW1-yVXsoElmOe8lEpnWjtPCoTP3dYdf63_1AK1iK9kFB6jp_wxWmyAbqv2qnjUEc7D5cMpOaqb6dAFt3HhC3dHMu0VB28L-IVbPIGix_iNx0SbLyXHB2zq2SSk_ntADpJfP8zFULtFYftQ2fej8MyNxqf8ELFTgv7W8yaAof0bOo5xSjCMbVB7sx8ezBXaWks85QYrSPA4wGxRuXi5XKGZfE-svT5Ijhoy37LFszh_BbrcghjoC0m-V5WViTi6FhTN0WTOK9gbWL_JzKa3hnLd4n0DJJBM3pC7QqNNALblBQ2_ye03eUgTSLglci8h7HT6BTJWMtYM8VCB4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa3da0b6f4.mp4?token=LU7l5LW1-yVXsoElmOe8lEpnWjtPCoTP3dYdf63_1AK1iK9kFB6jp_wxWmyAbqv2qnjUEc7D5cMpOaqb6dAFt3HhC3dHMu0VB28L-IVbPIGix_iNx0SbLyXHB2zq2SSk_ntADpJfP8zFULtFYftQ2fej8MyNxqf8ELFTgv7W8yaAof0bOo5xSjCMbVB7sx8ezBXaWks85QYrSPA4wGxRuXi5XKGZfE-svT5Ijhoy37LFszh_BbrcghjoC0m-V5WViTi6FhTN0WTOK9gbWL_JzKa3hnLd4n0DJJBM3pC7QqNNALblBQ2_ye03eUgTSLglci8h7HT6BTJWMtYM8VCB4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : تنگه هرمز برای همه باز خواهد بود. این آبراه بین‌المللیه و هیچ‌کس نباید کنترلش کنه
🔴
ما نظارت می‌کنیم، اما هیچ کشوری حق کنترل کاملش رو نداره، این هم بخشی از مذاکرات ماست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/alonews/123111" target="_blank">📅 20:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123110">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
پیت هگست، وزیر جنگ آمریکا:
ما توانایی موشکی، دریایی و نظامی ایران را نابود کردیم.
🔴
ایران ۴۷ سال علیه ما جنگ به راه انداخت.
🔴
یکی از افتخارات ترامپ ترور قاسم سلیمانی است.
🔴
اگر در میز مذاکره به نتیجه نرسیم بر می‌گردیم و کار را تمام خواهیم کرد.
هم اکنون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/alonews/123110" target="_blank">📅 20:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123109">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔥
حجم‌های بالا با قیمت‌های باورنکردنی
🔥
⚡
سرعت بالا
🌐
پایداری عالی
🚀
کیفیتی که حسش میکنی  همین الان جوین شو که جا نمونی
😍
@NetAazaadVPN  @NetAazaadVPN</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/123109" target="_blank">📅 20:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123108">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P-kRq6_zMxNqExmNvKVoMERtQWFmwIHzu3QPLsB4Mmsunt5euVqhxbfifi1jfDkzqJtoJlcFmNOGOTjqyxq_6tFPEZXB9FlvQr3rTN8ris2h5PXcfEMNwyArO16HwpzlJq_5fyed3UDHYhKok_QWi3YEzTMfsdbIFA3vroYyssfCV65V94hpR-F2Rcu4_8esg4mBE3Xm_bNC8t8E5eVrz096CFunrKlXoSKY-tNS_E4j963P4BgrV1DzjfJ4jJlyMaPQA8emG9-fGFZXrUh_vUNJyOlUuTTw97w7qVUpUlS61QX9hGegfQgYfmDCQMFQ7MucXMPiOjz5sDy8AnMCrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
حجم‌های بالا با قیمت‌های باورنکردنی
🔥
⚡
سرعت بالا
🌐
پایداری عالی
🚀
کیفیتی که حسش میکنی
همین الان جوین شو که جا نمونی
😍
@NetAazaadVPN
@NetAazaadVPN</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/123108" target="_blank">📅 20:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123107">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) کل منطقه جنوب رودخانه زهرانی در لبنان را به عنوان «منطقه جنگی» اعلام کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/123107" target="_blank">📅 20:24 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
