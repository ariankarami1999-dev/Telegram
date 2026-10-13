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
<img src="https://cdn4.telesco.pe/file/symKfrijcFxG8zN2dWOabAN-U7IFwZ-4dEsPi2Dr3P3ujuMrLTILq7Ol3Tf1TnGCOfs1izT-iU258h9vkp_UWGWbDiZCsuWHoeo2FlmaYRy5Y5toL8V-68tFLKLrblbrqqfy6wghxAMcs1UcFWGdIOVI1IscUBMtg1vv4S9iTwzKcRUONiLYIOhKlOqz07kNSJd9SPBWhjSib7Ipuxa1AuzD9FZIRhij_ccUwkuow2h-jSU8YVFsudC38guFkyd0ASE2suunN8oKoDQaQRl6YmLHsFc6BrePwhfwvaplZHNAVxcKIJxkNiwOMjwTPD54kmdDym-CKCl8WU43pfZ6Jg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.46M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 02:50:38</div>
<hr>

<div class="tg-post" id="msg-698273">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfURSsCal9Uwb-VSUJpz1ELLba7nCJrYlakIwsZh-PRwH058f_oXsBSF7DU4kdIxBQNrkvGI7VNlWx-DxkPJ9Fx7-Nj-567XYctms9kz7hvUKrx-ntIcXObGLzx4-ebS24SOFMP1gu2HDKST3J1tb6IqgKvTNLtlniple61edayEw58uRRAviz6UtTmTLSF8QjmxBxr2atv88o10LrQBRVdOhVr80dYG_5rpZ5PaP84ay0J6qkB5FpPj790dcV3izd3KsvY42jxROnsRsQ0F-WIDPFcXfwN6VjbNGJ5AxGTRb9EcZ5M5npRgG05aKQt_XiDdfpkPd6lc133a7sh4kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین بلاکچین عمومی ایران،خدمتی نوآورانه و کاربردی برای صرافی‌های دیجیتال و بانکهای ایرانی و راهی برای فریزر نشدن دارایی‌های دیجیتال!
ادامه مطلب؛
🌐
https://www.zoomit.ir/pr/467710-novachain-cross-border-value-transfer-infrastructure/
nowachain.com</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/698273" target="_blank">📅 00:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698272">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbYGF4-hEODAHC0Vm777SMuBFGP9k71r6zMS5RU641O6XWHdsSDzDkLL9DkMFzlBZpb8wxAjuv9ylF_2u3NMknrbLX3I3xUtnlNLKAePYOfj7ka7UkLhc-yVY9oN1SkoEvDJLIxOG3lZKTLf27A7x2db2bd_7xz64B4ONcXUB5VvoNQtUIjEQ_hxXF2Zlcz9-Djn2v90Dgn7Vs7hG_G3n4XCuH4tccQ2iSFCn1EE0uLi8u8A2FZcBSRID9gSuyn7X5ilGU2UyaqMBMKjtYCPSeRWIvuoLCBhXFR41aPVa-Zy80QkLL3v_w-apW0B9dzbM94qu8LJevrkhAyjCCsLEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرفروش‌ترین کفش جردن در حراج به علت انبارگردانی
💯
رفقایی که توی کمپین حراج آخر فصل خریدن، 1.1 میلیون تومن سود کردن
❗️
پرداخت درب منزل شما
✅
موجودی محدوده، قبل از تموم شدن سایزت سفارشتو ثبت کن.
👇🏻
مشاهده و ثبت سفارش
👇🏻
مشکی
🖤
👇
https://memarket24.ir/product/fast/46467/180124/
سفید
🤍
👇
https://memarket24.ir/product/fast/46468/180124/</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/698272" target="_blank">📅 00:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698270">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a16c38eef.mp4?token=qCrCwZf1vgLGbh_j1T_tNX2FkvEEaDFkRFgxEcxPNaPuNcqwGXGyAqtcxIvg2DxeCLpEnHyg63yWPtpY2gk1awdfRgOUyFZesXUwGc83-SC8n_uR-xTgROn0uXzzls3FJvQI3mLKfmI78OEhL99qfGMl_5kxCn3r2LPdsDUIMB9_YZut3b00YC-vLTv5OlYEGUNxYmZ6lOhW7bzSxJU1LmpFvQD-x3S3rXbNHFIFXm_joyuTcydDei75boIN2Jl0UC8M7iOVGLO0CN5BX8dB0G6vO07GTxQ8eSyRsTQc2xAeUqb6a3XgMUokzzCsVHSTESIfztKUySfBuuwfTjtzxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a16c38eef.mp4?token=qCrCwZf1vgLGbh_j1T_tNX2FkvEEaDFkRFgxEcxPNaPuNcqwGXGyAqtcxIvg2DxeCLpEnHyg63yWPtpY2gk1awdfRgOUyFZesXUwGc83-SC8n_uR-xTgROn0uXzzls3FJvQI3mLKfmI78OEhL99qfGMl_5kxCn3r2LPdsDUIMB9_YZut3b00YC-vLTv5OlYEGUNxYmZ6lOhW7bzSxJU1LmpFvQD-x3S3rXbNHFIFXm_joyuTcydDei75boIN2Jl0UC8M7iOVGLO0CN5BX8dB0G6vO07GTxQ8eSyRsTQc2xAeUqb6a3XgMUokzzCsVHSTESIfztKUySfBuuwfTjtzxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجیب‌ترین چیزهایی که از ایران صادر می‌شود، چیست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/698270" target="_blank">📅 00:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698269">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ارتش سعودی از حمله پهپادی نیروهای مسلح یمن به ریاض خبر داد
🔹
همزمان منابع غیر رسمی از شلیک موشک‌های بالستیک یمنی به سمت اهدافی در عربستان خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/698269" target="_blank">📅 00:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698268">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ادعای کانال ۱۲ اسرائیل به نقل از یک مقام اسرائیلی: نتانیاهو هفته گذشته با ترامپ صحبت کرد و پیشنهاد عملیات گسترده علیه ایران قبل از انتخابات را داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/698268" target="_blank">📅 00:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698266">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5fl2izKeGY2uY664xbTioZlNyeqvrevax0LOsF0FoPh8H6_VaGHm7UDjC7Tn0UXaha5ZyaAZJ87seGm1Y-rojR2MyyXV-hW3qp3coJ2iFtF-0ddIYYB4CLhE5NCbj9avlRXfFuble9Q0VeBfc79zuWTEfw-30QrkWt2dM-tSYnJG1ic92x-Lx7vASgC8TXCD-KF5S1iMe5ebnRHiG4Q3BoYZajQTbIknJwbRt383iUWXjq7GWAY1jh4XXyIBpl8_BfR-qkYQO93UlnfEqeIFtvkCTdYpdGK9TnC3ZHl25bl9Q8ChTTy-ZS-lwn_gjPsmDm4ECT9SDpbYr8-aLFTBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/akhbarefori/698266" target="_blank">📅 00:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698265">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuSTxt0JsGYrtLYPc50g5yDAuzDcyZh6CyEC7J57nzXNkBdM7XTG-ADPPMzAaPCYg7_yVuX9D9fPZUx4UgTx22RAPSRvXTMrMvXwrH3CiuqFBPLGwzTLNLL5JSNPRtlKKROgXBIyb5hiLTUF9wXbd7UO8oNrIXHYMjvois7JyMAuJfh6RPKGva1X4ND-o-TmXk1L8zkEZAgE9oIMJZLrsu5dXZQJXeIZ1MhcthVJ5rLcFJOlqjRch2oQveHExBd5Q63qJ7Im7x-aRGyUmVM-QcIFFhBoU83d3h_Z1Stq0JbtNx1_9WA-UFADTKeHjeYwC7KqW39VQ_9lpi8w8tQTuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/698265" target="_blank">📅 23:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698264">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
کودکی از غزه که دل‌ها را به یاد علمدار کربلا انداخت...
🔹
گزارش اختصاصی شبکه سه از وضعیت نابسامان کمبود آب و غذا در غزه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/698264" target="_blank">📅 23:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698263">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3b948062.mp4?token=BgisIfO5ObTIikdXLQ0cGOV-kzlvQ42ungQnijgALdNNcc3mtdNwkyz6mtlxmL2WyH7IX2bfMRhsanRWM9X4IQuy3aeiOimm-aSecsOOqUjoiA0FHAu6FgAAWW15qyTv2w5M691pNCSF2ACZF_Adgd0H8snsTH1RbfQMU9OlJCf3BWJtFuigwTIma5MtKzX0VSVwey2lN15mVn5PS_Ts0U-UD-rC4YECnppKMR7etZc8sleqL-dJnqeD5wWeJO3AMT_jwQOgqvmYPEkN2_8PthK75Y5j2SoZ10-waihjloHvp60zOROP6_1n_LE_jxA7IKvF_QP3LL6azTfVgmRMCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3b948062.mp4?token=BgisIfO5ObTIikdXLQ0cGOV-kzlvQ42ungQnijgALdNNcc3mtdNwkyz6mtlxmL2WyH7IX2bfMRhsanRWM9X4IQuy3aeiOimm-aSecsOOqUjoiA0FHAu6FgAAWW15qyTv2w5M691pNCSF2ACZF_Adgd0H8snsTH1RbfQMU9OlJCf3BWJtFuigwTIma5MtKzX0VSVwey2lN15mVn5PS_Ts0U-UD-rC4YECnppKMR7etZc8sleqL-dJnqeD5wWeJO3AMT_jwQOgqvmYPEkN2_8PthK75Y5j2SoZ10-waihjloHvp60zOROP6_1n_LE_jxA7IKvF_QP3LL6azTfVgmRMCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای یکی از سردترین شهرهای جهان در نوریلسک شمالیگ؛ روسیه
🔹
این شهر در شمال سیبری در روسیه و بالای مدار قطب شمال است که به عنوان یکی از سردترین شهرهای جهان شناخته می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/698263" target="_blank">📅 23:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698262">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zoi2mONLWz6zpVO-khcAhaJXwV3SyfA3vpTujGybMjLwW80Ux9f1h_Em4KyW_g0SybuPkeuInihdP_8Mx5F2DYxnqkSDzuCu2E8RneLywJAdNRmH_PveQEOQZDzX-cI6XPDmfw2MqtGxcK6d__9jd2-_2vvxdfdJo1m0IFRqIscPCyFbEeLmXK_0IcBuYlzVCAt83EoYCShEqHD0iG-gZlDhuQAg_q_DNjdBZBEBkIhvsvIFMWCu63fqZK2BuHiOYByHrxVp5mwlS0AIRdinVLE_8_G15AQvIb0cym4fNCRBMeaBxP6Cfk5BDx3kKBtuNln7inMeZX9iTvTXNvm53w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری زیبا از جاده چابهار
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/698262" target="_blank">📅 23:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698261">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
در لابلای خبرها، داغ‌ترین‌ها را ا دست ندهید
🔹
🔹
فوری؛ نتانیاهو می خواهد در این زمان به ایران حمله کند
👇
khabarfoori.com/fa/tiny/news-3252237
🔹
حمله یمن به آرامکو/ ریاض هم هدف قرار گرفت
👇
khabarfoori.com/fa/tiny/news-3252235
🔹
پاسخ ناقص واشنگتن به شروط تهران | چرا توافق موقت هم دشوار شده است؟
👇
khabarfoori.com/fa/tiny/news-3252073
🔹
دختر ایرانی ملکه زیبایی خاورمیانه شد | حدیث ستاری یک دندانپزشک بود
👇
khabarfoori.com/fa/tiny/news-3252130
🔹
خاتمی عصا به دست شد
👇
khabarfoori.com/fa/tiny/news-3252013
🔹
خبرهای جذاب را در خبرفوری کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/698261" target="_blank">📅 23:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698260">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJ25dnoeOcAyMeYGTLDU8ygCa4VB2-uOErl3nK4BsP7fCS-dlaVB5QzcTlJBvNuogt2uO18W2BLCzTDVPcbR92h2PCjK8L138giKI9SEOBqzSpS4CCd9N92QLdE3vay0dVlKs5yWtmebFRXNHtNBAaUwwJnRWisKzEmgLOtgHlMNllm_3XXaTN271degXP6we0rDBPbuf9sZfo0fRxQbrhY6OglXt2_1KOWzmN0NqNZ49sPV2lAzrrDN_Y1Se7WaqQQ5pt45FJi9KHHKtgKRi7_QQWMZX0_f-ZPsUHw4VnQIcWaoopUp6HGCcJQxxiBMFL8eWTF1ADsNR0oHTfYsGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
تمثال قمر بنی‌هاشم، حضرت ابوالفضل العباس (ع)
اثری فاخر و حماسی، با الهام از رشادت، وفاداری و علمداری حضرت ابوالفضل العباس (ع).
ترکیب اسب سپید، پرچم سبز و طراحی پرجزئیات این اثر، آن را به انتخابی خاص برای دکور مذهبی و هدیه‌ای ارزشمند و ماندگار تبدیل کرده است.
✨
مشخصات محصول:
▫️
ابعاد:
۳۱ × ۲۵ × ۱۴ سانتی‌متر
▫️
وزن:
۱۳۰۰ گرم
▫️
متریال:
پلی‌استر
▫️
طرح:
تمثال قمر بنی‌هاشم حضرت ابوالفضل العباس (ع)
▫️
کاربرد:
تندیس دکوراتیو فاخر، هدیه مذهبی خاص و یادگاری ماندگار
💰
قیمت: ۱۵ میلیون و ۹۷۰ هزار تومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/698260" target="_blank">📅 23:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698259">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c7c193b7.mp4?token=epq__jFFViO4srHUHSW5RqBD6YZ6oX9FMZbSZREOhmIP_Py5MFBPJowrox8SLGm1fTeZEqVKAJSU0ev6gtsT9IemtlR_7Se9roJN2XZBUe_fsWmuv2Mv_iVMHU42h1L9qyLPlMnidV6wrfqd4d30L8naV6IqIygSHJqLTmWm8v8BxiaUCam2UK1psVjKyAUmHN9UtGV2kWcmiUAgiJuonczJb-HXAcNgr1tl1jZxq3r1ZLXfS5xUq-bHASWjIYk72mrZcu6PT5BOq_j23FvB2L_6ZS9wFUwIb-1s1nlcvZScGy-bUZETZ-p9PsbnX0HSUw1OLMc-NM65NVgNCAbShQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c7c193b7.mp4?token=epq__jFFViO4srHUHSW5RqBD6YZ6oX9FMZbSZREOhmIP_Py5MFBPJowrox8SLGm1fTeZEqVKAJSU0ev6gtsT9IemtlR_7Se9roJN2XZBUe_fsWmuv2Mv_iVMHU42h1L9qyLPlMnidV6wrfqd4d30L8naV6IqIygSHJqLTmWm8v8BxiaUCam2UK1psVjKyAUmHN9UtGV2kWcmiUAgiJuonczJb-HXAcNgr1tl1jZxq3r1ZLXfS5xUq-bHASWjIYk72mrZcu6PT5BOq_j23FvB2L_6ZS9wFUwIb-1s1nlcvZScGy-bUZETZ-p9PsbnX0HSUw1OLMc-NM65NVgNCAbShQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر این ۴ ویژگی رو در خودتون پرورش بدین؛ موفق میشین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/698259" target="_blank">📅 23:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698258">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
قیمت گاز در اروپا به بالاترین حد ۴ سال اخیر رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/698258" target="_blank">📅 23:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698252">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDeWja0DbmYE29h4m7dUOX31aj7yBSHLAEjTSZNtBiRXXc2QcyTeNBsnnkYIgqRsi-tPrDN46RCnwr3GB1rATPvZZt4z0RakMOVNNN3GtVEVNTRqub7WzcWznJI1_9aRFACoCX8lqyN5AvmO7JTA7bBkqUgNsY8VCH8RJMcbFifP7ZZ64fuJyXJFybqSRbo4mG4wHTzREk4WkEH2edhJOkmB6upPPASTt_Ft1uUgTFdp5pMOI4jKut7irtt_Ag35WRjrX0qlkGZeVZojJPE9epu2QHGvNqDvjGKTd3rui1jSr_5AwEgcklML0J0JaZEmp2jGZyfkV6bzrtDcbxs6zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله زمینی به کشورهای همسایه | برگ تازه ایران در برابر حمله احتمالی آمریکا؟ | پیام محرمانه تهران به کشورهای منطقه
🔹
گزارش تازه وال‌استریت ژورنال از تقویت استحکامات هسته‌ای و مرزی ایران، بازسازی توان موشکی و پهپادی و آماده‌سازی برای احتمال ازسرگیری جنگ حکایت دارد.
ادعای وال استریت ژورنال چقدر شدنی است؟ بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3252180</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/698252" target="_blank">📅 23:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698251">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رویترز به نقل از منابع محلی: صدای انفجار شدیدی در نزدیکی تأسیسات و مقر اصلی غول نفتی «آرامکو» در شرق عربستان شنیده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/698251" target="_blank">📅 23:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698241">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lTKumu1BLRECPFK9PgVYh4gipcPd6SZyaAUXeJ0ZuVYE9WKxGaD2NyfDjbvJLNsd0mB2FjlsM1W0bUyPwU_XHhhAVL65RiB8azKwNEJtF8sZ2jiGeUOc7bhceCE2qv2oheTYtmq4HaYYBDKCp6XefWZtMw24AbgAzl9fWLaLRug4Bo_z-ZoLLeoy_WWaBdZxpsNQxkZgyMvyvOKFpqww8Mrp-WEY_7sQsukbfajTncG8EG6INX72GNScWHYL14uikqkaIVmt0g3a-tm_42cCbY3D6bNiAQ8qy_u8EDOv00mKUpZasCyK0jWJ6CwSrwW-Tbrt-DBX99JdgXgINrLEHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/faK_skCi4eVNCqGgNlRAWnPOf32koUVTnUO-v9oiivqmI0-P1YDOwbM2fGnCM9X4H4CXZBx33rJkmGFHuixHhB6i3QFNMUqegss0ljrAGpMF1qxAowwIExxyZQhOzlJq7TKHQolV9vnWAzFCmbyBPMLEo8la0EjhwmyFyNLXRDTsqQmvxUr7dpaVzpEzs_e7ZAHxFWA9-Y5IikXkwleFhzvY8ILENWrGF6CYc21vw5awfC-PE5j58eAVtr6uBg-q35fuz2jx1IPdfzLwb2AkWLuEQl8-Fks0uy3pqlbOynwIMTfuRPXQBXBMZk9RdiTkZBr-l-K-C-st9L2xJBHDGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eqW8LFXCn_4PL75pT8PiaAsRFtyexwb_qOmM6m7rrZab1KQnlCzqjiDN4pTwUAuIRcvFOAiAzW6Gu9tkV8N4X4G5T9GOVyE2Jt3E_s2gKVNBiMHwOZKaCn0-Q1Ui96e0VTgplrvvNlyfmoe2rNkNXp29jWcjac6lPABnv16TnPQGlQK6V72iLUbuYL9NT0k73dOlBrQesgX_qAtfcyQQK5zRCmatBqYpCjwrgRjNt21WQCIZ88-yQKDFj8OGfdHK9PUX-5-zNS3qpu-L6uJlw18tFsUpAk1PVbeYYX6-rQmTyYbtPhCi3_mQitjTGy9QL6dK--uQx97Pl0K38AdS4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W7bFKR4-iu6pZN6ug487ePmAvVXD8PS50HLaGHnaBJ8CkpSUkhCcia4xEj0uGxYTpAcBrwwvWmi-LlqxUvKDtWLltwWVV0Uca7x5HVUDQBTf4F4aoJ55TnzD2bvEzZWkDuV_qTlQXhE21CTf1EiL9ZFqwG0EZxShRuRKegV2f9Y8IiG8cnU86mNbRljmLT7JmiSEjlSemZLAgwyAZuIF8qrT1RfrvrhWc87g8276yChoWGkqUMCq3Bk9BYxJkdKWEUOJfdoJzKY3MZ2kb9w9p0SYkQKU3nYXZ-NhMCAgZIKrMxTAqIog9epZi1RBUf7VTg87JiPwNl8u5v8mY05lmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gYFHsZciOJJND_hU6IIHJb_eCgMH9WqxARIL7YI_3MQqGonMlWMTfb0G9A6f9z29_eqjw55_WAhsHc3USwJAD7AXH700eS5qsB8arUWXz0AVwGJplTAYOfCRCRfOlH9qIM3JuNnLOO_51NMv9RoaIq8ZAcgGVv1rXKdyMOCh4SgF2mbQRPP6g0gNPN2HRxW5NonGyPjtvhTxyzBlLG4Yle89XlNwjl-0Zi7JXpHiDv4nPfuh59bZs6Rt2e7hxOQ0mr451cEuWJ0QD7OnEAe0dXqS_lxXB8gdJ7XenTTWCSZyvuLdtR5VYqzUHEmM8yb70Uzy_flqy9lrigRcEaeZHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F43CCmMFIXw2OzM4NFR8YGjTDLZVSLc3itJ2MjYcGD9U_nsG1dUdz8rnCEsmRnQ8SrtWlPNEAfLxRzaF73fwJx4PvJgxAO6vt0DP_ywch9rmQ1EnnKmn7hFduC64xYAW-u-Zv5vVUMWOPuDsz2DdalOQ6oWlcc9A2awapdwrwmhEBOSA_ZS0yqxUSU9jH8d_iqLbZRO2lFfz6dOhknL9EfW20Pg3UWZ9oPsEkDiFs5OASkR9q4VSRpC1vjW17Ekz6EWh5IpaV7njA_0AUIWNCm8X-b3k6AR21OMdHL6k6Wi3fHAotc8DZKz4oPZeXzVSmrHhP_HTHx52xdFKiFF8AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iploKfqj_B8RACrz57DgMcMq9dom71EXtPLl9jMII3TKbB73vQ_pvFKHHhg6Fgb0hlpE_jsmI6k2Q76RyWiXd_JGkyyrT5Et37A31ZW8r71rfisF7MQb-Ern3KC__M6U0nNzYgbgDLqutrtJdHh0DG_mjqHwxosLiC8wvpAV8AUrU2M7aCSu7ojA69W_gN91BAFUHZo2Lg-ygqtQBi6ZEeLm9NYPuiChqYmJwk7dqlt_gDRF10EzgeH1eHnOib5boFY0loPDWCFJ2VvtOBDfEyhbaxMGFYp8f24tOceE4Q3DORWGq88L1xN1Uketg2kaZqZrhB0KohcaTiGzACe_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FZJmg3pCwVufOcic_b0RyTtLPe8yRtXZrXQs-TSbjVc533BHWTO6BNXZJyAErIrXAJBdq_kq4rwmjpm-PffQa0e6ehOdWWGrInJspPkgvXGMxkEAQPhMOMelC6qAOPGjfeL3A3HGNJZXVeujWUQUuOH9oaUhKQyTLKwhdV8XhPExy2f8OucrHaTI0izoRuaSYDUHwPNUWLKmq1EBfPnZfghHFtsiUqwdmr_snyxWbbDM341_0g3NT9N_R9zYvn5NLEGrKtJeCX5Awy0nHgu9YO7WvY7xTQB0D75QPR2XGpDXXGHHoWrqmlWb7ZOq5ciLpGB65LUQGGpqYrr-vs1rPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FoujXCegmTqRr0svGTszvsNGVu4etzWm4XfzVUjFFOwq_dzpjB7N_LJs624xD16EVZUpKbkeyjhuaiC9_6mu-KSaJgS865GEzGTd72w4C0u_JrkyuJdr-DY47ik7AvKDB_CQqVOvJewF1D3At762l-VyyqGGBw-AeK5VOtHLtANkmkyCI63Ug0m9hpK1y73xxqz5c-1Y9v7pUO0qGMPXg4q5cSYv1Jl53AklijUrMi3dlI7PAFwP4vW06m9JuL1848g5kTr6ZB6-ckFA8rMvLMIOce0p3o4L_U1-5lHFDDPOsFu8M4eSmqDGiG1VwaJIhwQR4QWMgkmOPgPSYZmqlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7HM4j9OJJ0MapvRhlgdqfvf0P1RRKlrMfH0M5eMUIqIsvSZQTHA8ARBjzR2EdOm54gmUsRFfUIPnHl5X5QpZA_FhhwOeugAYZc4UsNPdk2Z9GLPVWE_zzkKkjBgjCUrQyZEOnPLIEX_SbVDdAaXc4PXRs5k4GUZckQTT08VLIAfHLQMs6NL-4JOcFA5tA69mwyhz2mujYA5M2L7xrs342Vj_c8YDjmoHS8rbUnqIal-DFuhWEj9Amy667HC2N3san9P6q5z4zPdWoNtlKk4jcBLzE8RwFgAiBN7hp1Wy8loeiy_yCk2tzvRDFafAEgrQZ9rtNEpQghG7gze_xQkBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
صف وام
🔹
طولانی شدن فرآیند  در واریز وام‌های ازدواج و فرزند آوری ، به چالشی بزرگ برای شهروندان تبدیل شده است.
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
#صف_وام
@Alo_fori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/698241" target="_blank">📅 23:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698240">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
نتانیاهو جنایکار: نگران انتخابات هستم؛ ایران به دنبال شکست من در انتخابات است
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/698240" target="_blank">📅 23:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698239">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b60a55b261.mp4?token=QVDWYJkPRLniKgUZfidoSU1_bVtkYjbqIQFyFesIoVbzEo1CFcwjfMNurIFQIpdENr7F6B8XwEa0P65C41BrcWlk_NNCXoM6PfNqMOylgxvLoypQfsipSO9-wp3OYPSEegfa_BzLnb9O3qvd70G4z5w7-PDg-AfbX9BegrKKSgJ1nEpFP1lYlLDzy43sa5WLlSuuhi_M265ET5Ncw_C9XDODArVzQx4AX8MbiWPWdIBkLg3xmTGZRKBbEOTFfQBBGH4Q6MnyR0gCPqp7c8k7KqcuK7gjYBvubnPvQ6tf6MXlct2QOlC3nYlNTm6xocm9Fww5fHC4ynaSlnQRuwk87kWpgyXygboGIMsJt7zj4zW7AKHAe2ehtlM_pH-hOMdJm1aH4Ut-k90kjZx91rWlKFFwGO2Lev4B20fKjzAg1z6jJcGjS17J01E68ucdP1MoSvLTVIcTgiYcvac1chjzpvnFze-lbC8qG2RSKSRJKbD2_AR-hCVkrJXpW8Vwxzsu_-3Rrjs_JqAQBBFKq_h_RPcfnzSFmYYfB-ZeHEVK9cusj2n4FjHd4VhvU09iJm4ORktk8zgk24raS-L6Tqn4wcMNxLnluXQMfDN8FEL6HUJFcCIVrM_H2Sg7F6vsOGAsZAqWvEJzOnWjeh49DyTIaF5FDXJzRJLckFYuhZkUFpk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b60a55b261.mp4?token=QVDWYJkPRLniKgUZfidoSU1_bVtkYjbqIQFyFesIoVbzEo1CFcwjfMNurIFQIpdENr7F6B8XwEa0P65C41BrcWlk_NNCXoM6PfNqMOylgxvLoypQfsipSO9-wp3OYPSEegfa_BzLnb9O3qvd70G4z5w7-PDg-AfbX9BegrKKSgJ1nEpFP1lYlLDzy43sa5WLlSuuhi_M265ET5Ncw_C9XDODArVzQx4AX8MbiWPWdIBkLg3xmTGZRKBbEOTFfQBBGH4Q6MnyR0gCPqp7c8k7KqcuK7gjYBvubnPvQ6tf6MXlct2QOlC3nYlNTm6xocm9Fww5fHC4ynaSlnQRuwk87kWpgyXygboGIMsJt7zj4zW7AKHAe2ehtlM_pH-hOMdJm1aH4Ut-k90kjZx91rWlKFFwGO2Lev4B20fKjzAg1z6jJcGjS17J01E68ucdP1MoSvLTVIcTgiYcvac1chjzpvnFze-lbC8qG2RSKSRJKbD2_AR-hCVkrJXpW8Vwxzsu_-3Rrjs_JqAQBBFKq_h_RPcfnzSFmYYfB-ZeHEVK9cusj2n4FjHd4VhvU09iJm4ORktk8zgk24raS-L6Tqn4wcMNxLnluXQMfDN8FEL6HUJFcCIVrM_H2Sg7F6vsOGAsZAqWvEJzOnWjeh49DyTIaF5FDXJzRJLckFYuhZkUFpk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابزارهای کاربردی و جالب گروه‌های امدادی برای نجات جان انسان‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/698239" target="_blank">📅 23:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698233">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QjhnvlZNho4h3YgKrdoND-DHCYuKKTaKif6OKR9pLnPepiu-vjGrZ1MMZfpZ_7hG1Sk4KhAoXZhMVpRtcbDcx4Y4qLO9P_JO840XpkO9NyKl2WfvR_6zpRtDKh2Ew9syYFuS0j5sMWnARSqP1sFhTO2wcMAn2dkKmrBIBNMOWO48EJR9Grabjd8zWx_povSpzfmu7t0h1Imgl-ERlS80dhFwxMqJhoxwtTJBDgWBhSnVEbyjz0rOLcEVF9r2WrKoJslQlHdIf21kuwUpikWXA5Q9MG35XICV46-J0n91RsP3nsgZspkmKW78C1ei0P1yJM4NO10A_AUIVZzaHBbWMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4Z5sK-3U1VbNkwt73r64Wq27o6J37zAfRyj4tENiafqHFUPt4HjgSzT1xPVG_IKI4Wx4uX5xmDa68KcDCCgRXUEYfUNDacRbxliDjKu88sGVkoRbf0ZZhty5G-KgMHTt87LhFKK1yGMJNDb71LIzXi1iIDcDO3yoziGDDpXz4D6mxg7vLl6FnvrIHrAJNBf-ukSWOTelkvwqSVicsYxtTLzu5357nWrA9YljhfV9G8qNmvXo4JBShQ7-y0_et44puvLZ4C6BomKJqOWEhDcgYemw3hmhVqZRSoRlDMW2f1yf1kmQQCTYLKHhPzcx_G6aMsft6GM2D75kD3UOz_vIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qhf8o7so5yIN9hpyE5hOva-94JDREoOhAt7sPUoiBPmgQj-bQies6ELg-7sHA4wuF_AgGctV9py33IqDKCPbfMdktPTQ6Eq-6jAeIVUX2IYghvwov7xa3HzavnOvJbwZu_TlRc7AhR01-SRJUacuhzoDpxRcBc3dx1J8GF4MIO_u3E4KG9vKIwjkQIiYGqwaIT8f1DY_nqiarjub-QNf3ymYHae4ZwtCqanGUl1i29lNA3DhlNjdVnZzCGKy4rJbMMd-IWFiJjLukhf86pSUd1z4B4DciWw1whzuhZwI_Qx7F_SlNf2VdZ2gQR2HBZkS59P_AW4OrkoCvGD9vo1yUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kt_pJDk7MdjoFYX12KSIcOEEnEawGg5DcTt0JNQbe0jdMfR5h4j_rORqb6YycWh2WPt9-nIo6GFHtOQ4yV0l_kiIGIaC-l-d-ovlwZuzfLHzff-YRYmylliGTLtZYwnKiFsrhzNHNWA3FIEb39UebdSATD-hW6ewtt4pKzYgC_26fiFFfFGQI45pFeFW2iOMZt4oUL5GZSJI5roqGDcDQ6IL7nqORhZ-c9Q9rRzJHHZ_DtyfhuBPs2svzU-GPmdCtzOhx1M7oUzxKDeSa4sp1KFNunXMDaU1xKjTJwr7AtiUA1az6OKZqr65FrCNF3SOpQ8bZh5eTT3vWGZIeS2h-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eBIAjNgv-gbnnFRhYBSNevmhe64q9huSnUaBo-hPyBeShiYDQfLAS0mnUjhuNDFzAa03dXqdbJJCkvlanN2bGXb4w5M7bclVPcKs5IaznYpy_Uu2U0M8sV3WVelDK0M6Xky_bDSgVe__j-XeojIoQFXIILCyT_j6ndV52crQFMfxtzP7Sm0JXqwTJDnAsGJ9KCKSNcRRDRwJzP8rDHLNyqJQbRz4cK5Rel9Tm0Sdxdjf-FDrHu-gbosdAvcHuEMmq6bW8kSgXFcLR2fRMfHw0yNoBHC_zNDlal8vxJhkCsawA9Ek-86rg4yYRM08bHJsokghSfAnl1QkRb-iIt0ZUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/csBoM2cHdyjKwkaPhv9NAyHw9Zp8Erd9DR58E1YPjHudSbHS3PGGph4Z1dh0hocykrab8cCKhDGr2QBk4RmTPjrRiwPTBXTuIh6W70dCCSYSw_cKIKyJJHM1n0JsZqjYvUlas48jeryaGVTvSEb0MxrF4JH1qxT3xVG6Ysebij02IQJx1EVikpj0Wtyr-queris4R0kkHmo0C6oE-Ogpyni-b2aG7F7aoBrk7zi2J3bscP6CrUeUQ3FrY293VV1unqRBGGXRewGiOJvwgY762MyzB-WSMhCurnCaBxVWy_YPZhMYfRBBJuKunUvsylX7zj4J-Dh8J7eN8fPTzXULaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با پول تیبا ۲ و سمند سورن، چه خودروهای لوکس خارجی می‌توان خرید؟
🔹
با پول یک تیبا یا سمند در ایران، می‌توان پشت فرمان کدام خودروهای لوکس خارجی نشست؟ مقایسه‌ای عجیب از قیمت خودرو در دو بازار!
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/698233" target="_blank">📅 23:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698232">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان 14- میدان چهاردهم، تجرید</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/698232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح کتاب صد میدان خواجه عبدالله انصاری
🔹
میدان چهاردهم، تجرید
🔹
تجرید به معنای برهنه شدن از نفس و وابستگی‌ها و بندهاست
🔹
تجرید در سه چیز است: تن، دل، سر
🔹
زندگی را معناگرایانه ببینید و از شکست و پیروزی‌های زندگی درس بگیرید و رشد کنید
🔹
این دنیا کلاس درس است و بایستی تسلیم‌وار درس شکست و اتفاقات ناگوار و پیروزی‌های زندگی را بگیریم
🔹
چشم امیدتان را به غیر از خدا و هیچکس نباشد
🔹
هرگاه در هر موقعیتی گفتید که من بهترینم همان جا سقف رشد شما خواهد بود
🔹
به آن چیزی که ندارید دل نبندید و هر چیزی را که داری راقدر بدانید و شکر کامل کنید و در ترک کردن دارایی‌هایتان نترسید که رشد شما در همین جاست همچون تفکر، اموال و...
🔹
در مسیر الهی اگر به جایگاهی رسیدید که فکر کردید حق هستید در تعصب خودتان هستید و هیچ انتقادی را قبول نخواهید کرد و این نقطه سکون شماست
🔹
در کمک کردن به دیگران و در مسیرهای معنوی، رد پای خودتان را پاک کنید و از ریا دوری کنید(حذف منیت در درون)
🔹
سیر سلوک از حق به حق است یعنی وجودمان روح الهیست و به سوی روح قدم بر میداریم
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/698232" target="_blank">📅 23:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698228">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d02f6abdd7.mp4?token=BHAxAMKDIqBsEyuB3CEDggrowJyxYYFEoj3K9fQtzqTlLsQ_WzLW5nT-Hgk_KSM0HEGgyyPdkNd7REOjKuT8Fum0C3e22VJZJg45AQz-f-nhKMDb2-p0JniJU-eXfzQCn3gXAq85lGaW-TAhpKyJBu09jvwndD5EsAlWsGDW5Pb25ACIHEnHUnKnazE2Fdy1j9uxosODfOetafSY2jIN2y4C_9Lsn9lKAerxb0FuXpn-cERScvMtRkVTp5KCleppYuAOtytzCwElQGT4WUHmMf0Ckq9MG3O6fcIr9fk2VX1N2z-msfwVqfawVYdY_8N08mvd-y4mUO4ZT1F1yhZAuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d02f6abdd7.mp4?token=BHAxAMKDIqBsEyuB3CEDggrowJyxYYFEoj3K9fQtzqTlLsQ_WzLW5nT-Hgk_KSM0HEGgyyPdkNd7REOjKuT8Fum0C3e22VJZJg45AQz-f-nhKMDb2-p0JniJU-eXfzQCn3gXAq85lGaW-TAhpKyJBu09jvwndD5EsAlWsGDW5Pb25ACIHEnHUnKnazE2Fdy1j9uxosODfOetafSY2jIN2y4C_9Lsn9lKAerxb0FuXpn-cERScvMtRkVTp5KCleppYuAOtytzCwElQGT4WUHmMf0Ckq9MG3O6fcIr9fk2VX1N2z-msfwVqfawVYdY_8N08mvd-y4mUO4ZT1F1yhZAuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حمله موشکی بالستیک یمن به ریاض که بیش از یک ساعت است که ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/698228" target="_blank">📅 23:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698218">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9902025f50.mp4?token=GyXkQ2XTVE7-R-JYizCsh4J_5gz2kMmtY9hAXus6IvgFO19aQmaBq5NmHVaoM0f4nE7tDa8geijBNTw00KFY_86tnh018wmZ-zBl3xFgnLR2O8JjT3p04orMtrEC5kIUhm2G5BwYPlxwxxNKR9h5K-LichXXKctiGIQhGUWH6ESVp4Ao3PxPQkxor623XswikQwIgPGeUW4pISjCFpfoCUMdNEEUixI4UtPcEU7rZP8KAzbOOcr6NMQVDMcv4_9IrYRXwG2IeRfYWChYKMxFmzMFHbyLuXMyy1YesRTkxgtCiGbM1ciMo14uTpwhUcCxtiWcIxIiZj6jBH6FPnrJOjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9902025f50.mp4?token=GyXkQ2XTVE7-R-JYizCsh4J_5gz2kMmtY9hAXus6IvgFO19aQmaBq5NmHVaoM0f4nE7tDa8geijBNTw00KFY_86tnh018wmZ-zBl3xFgnLR2O8JjT3p04orMtrEC5kIUhm2G5BwYPlxwxxNKR9h5K-LichXXKctiGIQhGUWH6ESVp4Ao3PxPQkxor623XswikQwIgPGeUW4pISjCFpfoCUMdNEEUixI4UtPcEU7rZP8KAzbOOcr6NMQVDMcv4_9IrYRXwG2IeRfYWChYKMxFmzMFHbyLuXMyy1YesRTkxgtCiGbM1ciMo14uTpwhUcCxtiWcIxIiZj6jBH6FPnrJOjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینجا فرانسه هست؛ ۱۰ تصویر از پاریس که رسانه‌ها نشان نمی‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/698218" target="_blank">📅 23:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698217">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
منابع خبری از حمله موشکی نیروهای مسلح یمن به ریاض گزارش می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/698217" target="_blank">📅 23:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698216">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUcy7qZsXY6cr4958IWi4MFMymhqTx9fHdT5Zg_Zs2h59sihaM3a6T3ikQr664sC4XUTcwGwJn8kMlYUDZLtzr5sPkTp2JDbauymWhEFU8iqHUftb2xs0U8ZFnxuwhIcge6Pwgb30VJjXc5RNn8qux9sqPYGJGVl2EiA1yUaQftc6QVYpD6ytUbAg0Ohrn6dlg2JA7wZk2pyq7BduBMfCHYrFWlxDjWWFxBO539-1Ef2P5S7fhOku1uCQ5CgMVUxoylTVdBmHPGgBc1FS7yb5UxW6nWn8KByrk2L8yENrBEW3BG_GMtVuMQDKdH9gWpgF5MLcVrBRUCnRv9dQLlV4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییر قیمت، بدون هزینه چاپ!
هنوز برای کمپین‌ها و تغییر منو، بنر و استند چاپ می‌کنید؟
با استندهای دیجیتال و کیوسک‌های لمسی فرانکس، ویترین و فضای فروشگاهتان را متحول کنید:
▪️
حذف ۱۰۰٪ هزینه‌های مکرر چاپ
▪️
مدیریت و تغییر محتوای تمام شعب از راه دور
▪️
ثبت سفارش و نوبت‌دهی خودکار بدون درگیر شدن پرسنل
▪️
بدنه تمام‌فلزی صنعتی با گارانتی ۱۲ ماهه تعویض قطعات
📞
مشاوره تخصصی و استعلام قیمت:
۰۲۱-۹۱۰۳۰۹۹۴
🌐
faranex.com</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/698216" target="_blank">📅 23:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698215">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvHTVc6aeKqljK6Gn6NfsR8kugJXsW6mKoewqn7Q-19YlN622ZqFJFaV9QNnqeltipup5DmsKDy8Z_KB75abmv6v2S1vqGYLfLUxJmlq5a6sqVQUBt8XGZrnpyafj-UN-J8RFW3Oz95cRf8ZA6Quhqy9feEJKTQOcce7GAv0bEBwG7gJTFHMc5Q8Ol6p-krYyiDHMTmowCQmCcXBYzYR68efBDtrdGsdKvKq23da9IJXEJAI5gFP7vksocqAu31Rpy5cW49CIHRu6u1J7TpMYCWvuNA17VRPhvru8iQHdyCMIW7Sj8ptQOmtnWvat140FDBa3a2JNQzss2Urgz3fFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بنادر راهبردی اسرائیل و ۵ کشور منطقه در بانک اهداف احتمالی ایران  رسانه جریان به نقل از منابع آگاه:
🔹
بر اساس اسناد و نقشه‌های منتشرشده از سناریوی پاسخ متقابل که توسط رسانه امنیتی جریان منتشر شده، فهرستی از مهم‌ترین بنادر راهبردی منطقه به‌عنوان اهداف احتمالی…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/698215" target="_blank">📅 22:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698214">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ادعای کانال
۱۲ اسرائیل به نقل از یک مقام اسرائیلی:
نتانیاهو هفته گذشته با ترامپ صحبت کرد و پیشنهاد عملیات گسترده علیه ایران قبل از انتخابات را داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/698214" target="_blank">📅 22:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698213">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpZSQgb39kWFR74DqoPPPNp4WX88o4uqTmQGvslnxdHGAitUr8HafPGM-UD889az9wBtUJeUzIWa60ac7JkxSD-TNDcIPWLWr32kmIPeJfc4qEOPEWVaNm8_1SpsE8pHxJkcZ5myarxddE1OBiX22wGgrTQh8VyNU9cz4eEdtSkb2toOCcKqUVz3k862GUSOvJu8rZDkcV8Y5ECeRhmjkPVVyneQvyH-UN_hFEYtabmuJ44D5os1XvewAFyofeGDthWzNe8b_P23ml4gWUvopskIyFIR6m9JeDKfOvy1aeiAqouTQcQkotq4zBYMPJKqQpMcY8dxh3ZlXQ4wtPMjBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هفت خان کالابرگ
🔹
۹ ماه پس از اجرای طرح کالابرگ و جنگ و جدل‌ها برای افزایش اعتبار این طرح، سخنگوی دولت اعلام  کرد که در مرحله نخست تنها برای سه گروه از افراد کمیته امداد، بهزیستی و خانوارهای سه‌نفره فاقد خودرو و مسکن با درآمد کمتر از ۲۰ میلیون تومان اعمال شده است. این افزایش در حالی اعمال می‌شود که رشد قیمت کالاهای اساسی، اثرگذاری اعتبار اضافه‌شده را با ابهام مواجه کرده و شروط تعیین‌شده نیز دامنه مشمولان را محدود کرده است. همچنین سازمان برنامه و بودجه با تصمیم دولت، متولی اصلی طرح کالابرگ الکترونیک شد.
🔹
هشتصدوهشتادوپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/698213" target="_blank">📅 22:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698212">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gm3lZQ5H7c-p77xYRCBtLbqlCtVXPLDEPvx9UIkvg2R91ulvdXLbFs3GmTCQrC6rIiytslR9XJEHDuxqUt83EMShCqENGU9SkezqoMP7qhdWf3SzArffbsIOFCZQ1wmFQGtL_uPMgmtM3QDT6QtKqY-vYjrPwWUdAL7WIY0NUu-Prtn5Bm5eEnnpviqsN8UAWTAutNul1ap70KWV1EaW5OUPhP5uPY5WL2cJzBG6pwfcBc0jfbS0Eakp6WzdKnVYEAfvv43EtL7xEQLQ7FoPjU8phacsTS3jaRfreYitUHeS8mZCnwihJHibDQsGZ3pNAKZIODKpC9hLvvsIjAKwbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی انگلیس: یک نفتکش و یک کشتی کانتینری در تنگۀ هرمز هدف اصابت پرتابه‌ای ناشناس قرار گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/698212" target="_blank">📅 22:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698211">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
وزارت راه و شهرسازی در موضوع الحاق زمین به شهرها، ترک فعل کرده است
پژمانفر، رئیس کمیسیون اصل نود مجلس:
🔹
امروز وزارت راه و شهرسازی در ارتباط با کاهش هزینه مسکن مردم کوتاهی می‌کند و این موضوعی است که قابل دفاع نیست و ظلم به مردم است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/698211" target="_blank">📅 22:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698210">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59a2aff38f.mp4?token=gfvmaRD36EdBSezyYo4DdXkkwj2T-RrWbWTk_TbHubU9gOhAlQYscnPitSLGimiafnrKlKeNtYf-PEUnUt-8q_WllcPiWz3vuCRH9xKSPFV0dL2QJ9dhumwjI2Q8sJvORE4WKZibWD6IOcUB8hvnk3gnLxBnLGdSPh10UspxlbCByaAO7Ypw4a_I_IO1r7EmER6OXMrdf77aukX0zFbe9gSCqNLG5e3Z0SFOrAoHxnCqYZ6DYWDtvxXxLNkzITspE6DRGY2rtlhfsblu8lX0VTAT-vp9l30BIq3lVyuOmmH5-Cvrd1BR67O_QYxzvCECbiXJjnn8ve3-HjaaQp-9hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59a2aff38f.mp4?token=gfvmaRD36EdBSezyYo4DdXkkwj2T-RrWbWTk_TbHubU9gOhAlQYscnPitSLGimiafnrKlKeNtYf-PEUnUt-8q_WllcPiWz3vuCRH9xKSPFV0dL2QJ9dhumwjI2Q8sJvORE4WKZibWD6IOcUB8hvnk3gnLxBnLGdSPh10UspxlbCByaAO7Ypw4a_I_IO1r7EmER6OXMrdf77aukX0zFbe9gSCqNLG5e3Z0SFOrAoHxnCqYZ6DYWDtvxXxLNkzITspE6DRGY2rtlhfsblu8lX0VTAT-vp9l30BIq3lVyuOmmH5-Cvrd1BR67O_QYxzvCECbiXJjnn8ve3-HjaaQp-9hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پژمانفر؛ رئیس کمیسیون اصل نود مجلس: خانه‌دار شدن دهک یک تا ۳، ۷۰ سال طول می‌‌کشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/698210" target="_blank">📅 22:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698209">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd70803b81.mp4?token=nQa7yMWpo9I19qiGkxGXii81GYHkGg2pNitopp6DscLrfv8fL5J_5GBMIE0ppy6QRwTJP2_LyZ1u2mUYLTPKFQBfaTmmXWM3Gla8RdTSOmxLjwDeJyiO4sVYyt6oeBQZU1udLcDIPQCVlWmVEBmECLDkGbzIf-hUgX0e2TthIef0RQckL8XUFIIIDKTzVW1O-x1pP2-U50o0B7YqheP3VpVJTbliuKfyeiYTjxKX-FQq4qcyhgm8SrV_03H_es4ueuMkQ0-vsbuADd34IUL_vO57YyYZURffC2BoHWqnnvxBbpdqh-SrwgQqtwyl5OEkhnC1IrMGDBkYeJhDq-PvHCcs7536_7jq5Ur2OZ_UyeiKTHLg3JNp8WpLutyE3_bL5LuKO3lt7SrBiEvBM2RmLsCEQwDB9zhGhhJrZSOcCYLQVJG5izikwB_bhEDs6nkUyG08BDK2ovC6zWkl4ED6hDkDVOroInO5DlMgXip5HaP9qvrCS204crqbB1NF6gbGX6G5PSBwn5VBFJSX7Kco0Qw2-exzAQyCz6M9WjxWG8Bekcg9RztRGy6somqOy73ECGj5VUZ7IXO8lVYotsJmZzdgIb_kc1jKN61-VSrmxoh4Xdb5z3O3mkca67KoQo9e6VkHw4gkYxsCxCKhMEJ0N-ruxomPwOF7yG0mtVOQRqU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd70803b81.mp4?token=nQa7yMWpo9I19qiGkxGXii81GYHkGg2pNitopp6DscLrfv8fL5J_5GBMIE0ppy6QRwTJP2_LyZ1u2mUYLTPKFQBfaTmmXWM3Gla8RdTSOmxLjwDeJyiO4sVYyt6oeBQZU1udLcDIPQCVlWmVEBmECLDkGbzIf-hUgX0e2TthIef0RQckL8XUFIIIDKTzVW1O-x1pP2-U50o0B7YqheP3VpVJTbliuKfyeiYTjxKX-FQq4qcyhgm8SrV_03H_es4ueuMkQ0-vsbuADd34IUL_vO57YyYZURffC2BoHWqnnvxBbpdqh-SrwgQqtwyl5OEkhnC1IrMGDBkYeJhDq-PvHCcs7536_7jq5Ur2OZ_UyeiKTHLg3JNp8WpLutyE3_bL5LuKO3lt7SrBiEvBM2RmLsCEQwDB9zhGhhJrZSOcCYLQVJG5izikwB_bhEDs6nkUyG08BDK2ovC6zWkl4ED6hDkDVOroInO5DlMgXip5HaP9qvrCS204crqbB1NF6gbGX6G5PSBwn5VBFJSX7Kco0Qw2-exzAQyCz6M9WjxWG8Bekcg9RztRGy6somqOy73ECGj5VUZ7IXO8lVYotsJmZzdgIb_kc1jKN61-VSrmxoh4Xdb5z3O3mkca67KoQo9e6VkHw4gkYxsCxCKhMEJ0N-ruxomPwOF7yG0mtVOQRqU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کوچک‌ترین استخوان بدن انسان با گذشته‌ای شگفت‌انگیز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/698209" target="_blank">📅 22:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698208">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
منابع خبری از حمله موشکی نیروهای مسلح یمن به ریاض گزارش می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/698208" target="_blank">📅 22:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698207">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G5xOyW4Z6nLHBpcvgsQBX04xjiYEhp6VjB39pghPTOVcExmalW0osFMKMpemgJeS10KZSTbsnRGvG_CRPMQz3P4-VEuB6m2Ns5upeHtFlYJMbDcyeJFUfpjod5U6biYfbeNHkW0aYs08pC7wPHkPdp7aOSwdaKTJe8u4ptjwUWsNVVAh5MOkhbKp-CW6OG90X8Tob-cWGp9ppm1oWYzoevkP9yj1B5z3I2g1YYJTVW4HKgtkYS-zMctA4WGKvByVsP9A_e8hf2z2X6_QMhNzllfAh68yeQy5Xym4Qe_SAs2Dmk1oIN7POFSvon_vf2QVpJqZhwWpU7ANoSUIkJhIqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حسینیون آذربایجان: الهام علیف دیکتاتور و سگ صهیونیسم است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/698207" target="_blank">📅 22:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698205">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6377634077.mp4?token=deuWWOVeSKFzqcArVd9FjG2XxT5qv9X_NvABe66_YtLV9Z6yIG_HMhbI1ihy3wmcy8q8CN2bxiSA0VNcuv8_ucof6MQ7CL2k68lRcfJTx6ATi30eUFJdubwayX2ma0nHXXD6hiargqElp_Na9jKB6_pIZsPEIagYAhnpTvNnq9F5kFMvXgFX4_tvsXkpUhHRALZ0RVl9CQMPvF6jWGsYpUDj2leFe19e2Z0Mj1RENpCcsCV71f6A5XUYRe79snE26GDPzSgkYtvceczMOzYFHR7wTzrO-6HA_-OpKqdmrF3ehKC5hK_uDTmh1zfmWLCXldRNHNJWMqEiv6hQ-IHhZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6377634077.mp4?token=deuWWOVeSKFzqcArVd9FjG2XxT5qv9X_NvABe66_YtLV9Z6yIG_HMhbI1ihy3wmcy8q8CN2bxiSA0VNcuv8_ucof6MQ7CL2k68lRcfJTx6ATi30eUFJdubwayX2ma0nHXXD6hiargqElp_Na9jKB6_pIZsPEIagYAhnpTvNnq9F5kFMvXgFX4_tvsXkpUhHRALZ0RVl9CQMPvF6jWGsYpUDj2leFe19e2Z0Mj1RENpCcsCV71f6A5XUYRe79snE26GDPzSgkYtvceczMOzYFHR7wTzrO-6HA_-OpKqdmrF3ehKC5hK_uDTmh1zfmWLCXldRNHNJWMqEiv6hQ-IHhZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی ترامپ و پوتین برای زلنسکی تصمیم می‌گیرند!
🔹
ویدیوهای کنایه‌آمیز هوش مصنوعی از بازی قدرت‌ها با سرنوشت اوکراین در فضای مجازی وایرال شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/698205" target="_blank">📅 22:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698204">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
حملات موشکی انصارالله یمن به تأسیسات آرامکو در منطقه شرقی عربستان
🔹
سازمان دفاع مدنی عربستان با تأیید ضمنی حملات یمن، از فعال شدن آژیرهای خطر در شرق این کشور خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/698204" target="_blank">📅 22:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698203">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‼️
حملات موشکی انصارالله یمن به تأسیسات آرامکو در منطقه شرقی عربستان
🔹
سازمان دفاع مدنی عربستان با تأیید ضمنی حملات یمن، از فعال شدن آژیرهای خطر در شرق این کشور خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/698203" target="_blank">📅 22:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698201">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alF__fHk_l_edajdosFKim3GhFBW2TphjQmSi9pAe_J6cHhYdzUUkVTvasyzNCq-H3ZGCuyMcdaKOFHD-RJBMYIpdRiP9pmNqsRQL_MigYorNOYbJMifsoAlEzxcKxsimfaj9Ub7RNYPAJTfIcJts0sew5DbaSGbh6MGb5hoBMtnC21EJQTOu-sFEZwB55z-d6C7HcqrAj-cW0QGx9aNxepIYzNUaTHmbgCcvFF_nVxqgTCzCn233gvqJiJnPMODNFFPRdcJ8G4nwmsUyBH8znGXd4ABMtF7nkgWUK3JLxBV6E1MCyTLIfQdAe0WHbpS_ZKogdEXLnD5s4Uqz5TsLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ: حوثی‌ها به درخواست ایران به عربستان حمله کردند
رئیس‌جمهور آمریکا:
🔹
حوثی‌ها رفتار بسیار بدی دارند. فکر می‌کردم یک سال پیش، وقتی آن‌ها را به‌شدت بمباران کردیم و به درخواست خودشان حملات را متوقف کردیم، درسشان را گرفته‌اند.
🔹
آنها مدت طولانی سکوت کرده بودند، اما حالا دوباره ظاهر شده‌اند؛ احتمالا به دستور ایران. آنها به‌شکلی بسیار شرورانه به عربستان سعودی حمله می‌کنند و عمداً تلاش دارند قیمت نفت را بالا ببرند؛ احتمالا پیش از انتخابات آمریکا. این رفتار خوبی نیست.
🔹
باید کسی برای آن‌ها توضیح دهد که من در انتخابات شرکت نمی‌کنم؛ چون پیش‌تر با اختلافی بسیار زیاد پیروز شده‌ام. اما پس از انتخابات به سراغشان خواهم آمد و هرگز فراموش نخواهم کرد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/698201" target="_blank">📅 22:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698200">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfzVzEFuZOKoL3psnNbkdB04pdl7gfj72Qu71JopIx9fHwOjRhKLcIj1Xxmy-Kj2bSbGxdqoXV07G6-ukmCoIZBdCuNcjZL3GbX3GBxvsHepYzV5_tms_ZjOAzAHbphZDKVKGfVMDpMngxLGErSEZni8xgto1xTAe-dNGeiEwYG8_qld7S8pqSwK7hSrSfpoAs9pHbu3r6MDXQ82boPjmQT2tBYmIoZ9Gyc88izJraTN7AjkxFi09awkVLrwDkwSaH1lS1sKE2BGzU0-J1acHZ8DHKeX50x1REC1DDzZBzbZz3SHCfUCMB4x6VgMTijH4RzePJCyKUYzIzVU1McDDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش مقاومت عراق از پرواز هواگردهای ناشناس در حریم هوایی این کشور
🔹
رسانه جنگی مقاومت عراق در گزارش روزانه خود از تداوم تجاوزات و نقض آشکار حریم هوایی این کشور توسط پرنده‌های نظامی متخاصم خبر داد.
🔹
هواگردهای دشمن با استفاده از پایگاه‌های نظامی خود در اردن و اراضی اشغالی، حریم هوایی عراق را نقض کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/698200" target="_blank">📅 22:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698199">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff51b864e1.mp4?token=bk0n7KGfsrMHK2zU76lSs00FeU1YBT1mODR2jzAzxKO-A7Ojdxcth7oJHC5E8OTKHU3rHupVIR5jKlUSVCzqD0OeavVo4l6f-fK2e0cdVNvtMe_tHRmZ7QXDmhs-fGPgxgnGLjdrf3fp4GhbmOTYXQ7h2_b79_LIT2dc8Z4172JR6y_sG7ye1XPFnRnE7S1vNsD2FeeVNhg9NEa4Rc7u8oRvDZGUIm1zwwMA-eJxivzd0aTLIauIVztq0AnmEkwftEjg16RNBwg13fFisLDeRZitqn9MWKEndo9oAveLFdzM0ZLextWkgow0gK5tNHNECKfkMdIbRoaS-pJmnav8TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff51b864e1.mp4?token=bk0n7KGfsrMHK2zU76lSs00FeU1YBT1mODR2jzAzxKO-A7Ojdxcth7oJHC5E8OTKHU3rHupVIR5jKlUSVCzqD0OeavVo4l6f-fK2e0cdVNvtMe_tHRmZ7QXDmhs-fGPgxgnGLjdrf3fp4GhbmOTYXQ7h2_b79_LIT2dc8Z4172JR6y_sG7ye1XPFnRnE7S1vNsD2FeeVNhg9NEa4Rc7u8oRvDZGUIm1zwwMA-eJxivzd0aTLIauIVztq0AnmEkwftEjg16RNBwg13fFisLDeRZitqn9MWKEndo9oAveLFdzM0ZLextWkgow0gK5tNHNECKfkMdIbRoaS-pJmnav8TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات موشکی انصارالله یمن به تأسیسات آرامکو در منطقه شرقی عربستان
🔹
سازمان دفاع مدنی عربستان با تأیید ضمنی حملات یمن، از فعال شدن آژیرهای خطر در شرق این کشور خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/698199" target="_blank">📅 21:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698198">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee41d205c6.mp4?token=HuTtOyBQsoSxijwn7ugbsJhv3JAIRRsavXs-Fs2ESJG_JLn-8-8zI8MCdvaqt5Fdv8-3WQWqBtF3pcxMCDzAIjbw6xAfq1vLi8ib8rRdZsYgsozDHNWlKwWCOcDc1FzlnMB6-RqWF-6FM9320e2v2bncc43ozkEADNMlkg1GVQGRfxqK0jvoTjX8qQfzFt3uFWGSEbKx-afo64UHYgTNcTEjBiNo41MADl4UrwtS9bDBgRUn0phxqqspzPfoHU90k2dNieVrdEZVokO-aS9iaBWuLNEHxKynxvOoGg2ZfDcd1h5Hy8QhucYvZbFuKp-ujIQwBti7ZBJQ_KRl9Ou-Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee41d205c6.mp4?token=HuTtOyBQsoSxijwn7ugbsJhv3JAIRRsavXs-Fs2ESJG_JLn-8-8zI8MCdvaqt5Fdv8-3WQWqBtF3pcxMCDzAIjbw6xAfq1vLi8ib8rRdZsYgsozDHNWlKwWCOcDc1FzlnMB6-RqWF-6FM9320e2v2bncc43ozkEADNMlkg1GVQGRfxqK0jvoTjX8qQfzFt3uFWGSEbKx-afo64UHYgTNcTEjBiNo41MADl4UrwtS9bDBgRUn0phxqqspzPfoHU90k2dNieVrdEZVokO-aS9iaBWuLNEHxKynxvOoGg2ZfDcd1h5Hy8QhucYvZbFuKp-ujIQwBti7ZBJQ_KRl9Ou-Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهترین روش برای جلوگیری از حشره گذاشتن برنج
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/698198" target="_blank">📅 21:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698197">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
چرا سازمان هواپیمایی کشوری مسئولیت زمینگیر شدن هواپیماها را نمی‌پذیرد؟
دکتر کامبیز بابایی، مدیرعامل پیشین هواپیمایی آسمان:
🔹
درحالی که متولی صلاحیت و ایمنی پروازها، دفتر صلاحیت پرواز است و مدیرکل آن بر ایمن‌بودن هواپیماهای MD تاکید داشته است، چرا نظر سازمان هواپیمایی کشوری با آن مرجع مغایر است؟
🔹
چرا همزمان با اعلام اینکه برای پرواز MDها منتظر نظر شورای‌عالی امنیت ملی هستید، به نهادهای بالادستی نامه زده‌اید که مسئولیت این تصمیم را نمی‌پذیرید؟!
🔹
چرا ایرلاین‌ها را مجبور به خرید قطعات آمریکایی کردید، نه محصول ایمن داخلی؟
🔹
چه دست‌هایی پشت پرده زمینگیر شدن ناوگان عملیاتی پرواز کشور همزمان با تحریم‌های آمریکا است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/698197" target="_blank">📅 21:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698196">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92c7c633a.mp4?token=NjeAukmj0k-BpfvF4oRAMHdjIJPPMFe6_SsJXHjjmGc7qUgbV12gyo0uBAkeaRiwSCzmYv0j7MLHCc0OjBHH8B07YQVeHFqxr9jvnB6Cb6fFOpF_4TCulYQEE2HSG7uJn0WCXdvE6BcZSqFOj0avDKKgoZ8bZnTa_a-mDsDcjDpxJcigAZIhp8aG5uXHLZmrUWfhJUSsgbMXI1t6_lFwbXmUCj_8Lncmbk7sf8NNpAY2uMUCFxVFxFDl_78tFW2DXAzfHvvxI__pIfqextAwYxa-QrreyQ-vxz6m80LBW4tic0ios26tBgtPiAtUSmgljZTDnILN8SE5TXeAdJvzOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92c7c633a.mp4?token=NjeAukmj0k-BpfvF4oRAMHdjIJPPMFe6_SsJXHjjmGc7qUgbV12gyo0uBAkeaRiwSCzmYv0j7MLHCc0OjBHH8B07YQVeHFqxr9jvnB6Cb6fFOpF_4TCulYQEE2HSG7uJn0WCXdvE6BcZSqFOj0avDKKgoZ8bZnTa_a-mDsDcjDpxJcigAZIhp8aG5uXHLZmrUWfhJUSsgbMXI1t6_lFwbXmUCj_8Lncmbk7sf8NNpAY2uMUCFxVFxFDl_78tFW2DXAzfHvvxI__pIfqextAwYxa-QrreyQ-vxz6m80LBW4tic0ios26tBgtPiAtUSmgljZTDnILN8SE5TXeAdJvzOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیت‌الله مروی: دو بار با رهبر انقلاب دیدار کردیم/ حالشان بسیار خوب بود
تولیت آستان قدس رضوی:
🔹
هم پیش از تدفین و هم پس از دفن رهبر شهید، رهبر انقلاب در مشهد حضور داشتند. دو بار توفیق دیدار با ایشان و اقامه نماز با ایشان را داشتیم. الحمدالله حال ایشان بسیار خوب بود و هیچ جای نگرانی وجود ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/698196" target="_blank">📅 21:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698195">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuAzSj-jji6QDE-3iwKTz1kp78am-Uuxdn3ob_68aw-4ey2eY6c-xsdYxbXq8r21QFd1lOa_l3IYW1Y26KQhO3LPbtBHFJTu5TPCXN3Xlh1u7-r0HAAhbYDXh0e5bRo1lYoBB8GzCkNnRK_A_gzexCGwLdQ6kWu0jpE--R3bzuaFlEjodRJYfPrlD1nPy55WhLubBo4IzBeOeBF70BflVAcWt1HhTRM_A6OJoEzb0VeH7JhD85MOdcOolaoyv_gLfQp8jj6htD_WkfyJ_TtI8mysYg-d1uKVUec0oUBXEIGmFfFqtMfP7iNArAhkdPGLDL5azIhze0xt5sIsxnI9zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احتمال حمله آمریکا به مراکز هسته‌ای ایران در جنگ جدید / پاسخ ایران به حمله آمریکا به کوه کلنگ چه خواهد بود؟
🔹
اکسیوس در گزارشی به نقل از مقامات آمریکایی اعلام کرد که پنتاگون به فرماندهی مرکزی ایالات متحده دستور داده مقدمات ازسرگیری عملیات جنگی در ایران را به پایان برساند. بر اساس این گزارش، اگر عملیات‌های رزمی عمده از سر گرفته شوند، انتظار می‌رود شامل حملات به اهداف انرژی، زیرساخت‌ها یا سایت‌های هسته‌ای ایران باشند.
گزارش تحلیلی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3252213</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/698195" target="_blank">📅 21:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698194">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
حملات موشکی انصارالله یمن به تأسیسات آرامکو در منطقه شرقی عربستان
🔹
سازمان دفاع مدنی عربستان با تأیید ضمنی حملات یمن، از فعال شدن آژیرهای خطر در شرق این کشور خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/698194" target="_blank">📅 21:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698193">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nl7j05Srh9nmj3eQXJJWKCkIWvFpF14huvY6MBs1COBPVeCb4uOVv86u4z7VgZOX9b6WE83NYkX6_E3GjQ2-YPPFWSE37sZ8IGWgKnq6R6kx4u5ghBVrW3XLwFPRJEIGQGXWPFc8JsAULAevtg87c1z8XkHZv9Lv6H8ANU54gJhEwvnOtaDd0ge-iC6xETO3prpY8c6pU9a6HyvRg8o8hl4nkXkFs0pTIoADE1nsUIBu5CfaqhWAhIM2-v3UVNfTAjFI6jq6OoxhWjs2h2D0OAVLrMuN9yBlOJ8enRt6CNsQSAvi0GUcNAZkS0YO4mE9jPpwKBoYjWw510jxcyq8kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توقف پروازها در فرودگاه بین‌المللی ملک فهد در الدمام‌ عربستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/698193" target="_blank">📅 21:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698192">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6KdBG1SSMDtqZjPCxngG2cSxxQ_k7M6-OWzgiVIbolxCpHhkf8VFqLMFla8lku9-pB3L2yZoMO1XXYJf4TqzdfHEUvVd8QscU3MzjvZS1T8dmeVr4UHuGOWJX5cCaX_xPwAYYa0nxoxtEmFqMluAnobe7kuux-sGRTzXDD0jHv5J3Xfn4KQdnYFZ2stV-RyqTULnHdvAwuR3iUZR88MbZEIlrWg6hChZ6QqTq4l1wsJKzTiznG0zZfUhJ63Qi-JfphG4HN_GdVKCnPgDvBfvVfNqHJYYVZ5rDedAxfDH7krtHalTr-cG7rNu0-Ii_rcyvp1hdKFkFSPJUpBRa2jkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۱ خوراکی مفید برای سلامت میکروبی روده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/698192" target="_blank">📅 21:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698191">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک اقتصادنوین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jO5PQZkOy2WJVP-Yd17vpM-i8UgF4nHNyqUbW4cz8Dgycurp1LYaqTqJEdRWPqhwnOF3b3vWsDUmCmtz9554UnHnStO8PpT-3rcRtxyRXkdvDJQKii904b4TxXp7aa1huB0QCeVb4-n07v0o4PxXvLTAMy70djXVUuZ6Xg9KJguyZDAcBhHjyRRkIlccPElAhNTD3vUxQP05Bkge3ISS4vmXAkOkx-Jvo6LhzJOXQ_cVlAADE3PJr0IFs8Z4nLhcEBgwxwe4D8lJY-IZYXN-liIdkPsjpezRAKFzbxPRse90b9PClV3MBpb3S9j42wioH3MOsgFtW55YVhoRvnRi9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
افتخارآفرینی‌های پیاپی «ونوین» در بازار سهام
🔹
بانک اقتصادنوین در بازار سرمایه دستاوردهای چشمگیری را طی نیمه نخست امسال از آن خود کرده است.
🔻
اطلاعات بیشتر:
🔗
https://enbank.ir/s/mfabbXL
☎️
02162740
🌐
www.enbank.ir</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/698191" target="_blank">📅 21:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698190">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe6fa0a8a.mp4?token=M2yEstqu84CQLWX-C2dxZ4kMs0MTN6UVgJl8xGXdvcscu5QTvrb-ujdrLYBOwQF_xgHMxjRKLzIx2kEja41IWm7zFDb-zVKmN0IQk5ppZ6ft7mI4b4-T1-reCIW5FIQuopDH7us42epi89RsWT-AGDKxsFNIpAnNpdGR7BeQg0f08C1oeEcK85_pSuMqbmSvWCsfeHoqosD3rVrUdPUaysYArYkweOCwdP1AixfHWKoUHrosALj_9xvlQEUmoz3CliulyNzJxJpsbYavY01f0KX56XgSuj4eW1rBQ6jm2CcBNSXktjHR1BaA_7FROOsOE127oYbQ6nO-TMWlRqgyRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe6fa0a8a.mp4?token=M2yEstqu84CQLWX-C2dxZ4kMs0MTN6UVgJl8xGXdvcscu5QTvrb-ujdrLYBOwQF_xgHMxjRKLzIx2kEja41IWm7zFDb-zVKmN0IQk5ppZ6ft7mI4b4-T1-reCIW5FIQuopDH7us42epi89RsWT-AGDKxsFNIpAnNpdGR7BeQg0f08C1oeEcK85_pSuMqbmSvWCsfeHoqosD3rVrUdPUaysYArYkweOCwdP1AixfHWKoUHrosALj_9xvlQEUmoz3CliulyNzJxJpsbYavY01f0KX56XgSuj4eW1rBQ6jm2CcBNSXktjHR1BaA_7FROOsOE127oYbQ6nO-TMWlRqgyRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ تست سریع برای تشخیص گوشت خالص کوبیده
🍢
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/698190" target="_blank">📅 21:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698188">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
فرمانده نیروی دریایی سپاه: ما فقط یکی دو نمونه از تنبیه کشتی‌های متجاوز را نشان دادیم
🔹
آمریکایی‌ها و همکارانشان در منطقه یک سکوت رسانه‌ای ایجاد کرده‌اند که مردم دنیا نفهمند کشتی‌های متخلف تنبیه می‌شود؛ برای همین ما ۲ نمونه از تبیه کشتی‌های متخلف را منتشر کردیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/698188" target="_blank">📅 21:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698187">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4410ea68.mp4?token=jDbYMuv5tH8OzQ-KgAjzSmzfBvmQ7CzpR-x6Yz1TklA0nkgUm611cg1Dmejpr2ZRiT9iGoV4iM53mViEkv4QVxSAFa2hpgwkDeFobFCJfTBa3JG72JzBNk-bwYCEsMSEC74o3iRUB9eTWUCZOFhGqJPHvEawzVZ4fvzZ51gdiAM7hGRsBcHzcY3k2N-Ma1o0feaX4bQyu5kgAhRZvHO5fydKQ3YUVfxQg16VLhvvoasV-fG-qqDh3DDlafj9QB075TleWF0T-E9Yxf_5rhBVNPnQNgFt3a-LVB-y4slL3K5SZR4z_bHYvoBy6lyCIjXFyNhRzGq5zfORwJgyvASJzFg5uqhaXLpj4QkWp3pjsMgwylrxpU96RH3oU1F9M-83IA6It1RG_VHQhkxILPl0sL-U2b7cU75iguekuF8_8mu-uGKxZdrRflRxi1wA3g1TUr0XkrFdC36hE9CjO1hgPLfO4N1-I_wQT6XnYf_O2HeIXt4oH0PnJLQDnl9yH0f1ZY3AlWQQNJPwbnHhBQYInMedzKoi8vkm0jZuZDDW5PG6iXgUmtdcdk0aDFIK03KwDMEnMXTKO28Tw0tVBEkKcYi6xkHo3YDbZT4Qm3nhk6v3CVgPCCGok6RpGMJVcApzcFp1ZEIeIiH8eg1BloO3AQCfn0QgXW3vPpBJYTS8KwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4410ea68.mp4?token=jDbYMuv5tH8OzQ-KgAjzSmzfBvmQ7CzpR-x6Yz1TklA0nkgUm611cg1Dmejpr2ZRiT9iGoV4iM53mViEkv4QVxSAFa2hpgwkDeFobFCJfTBa3JG72JzBNk-bwYCEsMSEC74o3iRUB9eTWUCZOFhGqJPHvEawzVZ4fvzZ51gdiAM7hGRsBcHzcY3k2N-Ma1o0feaX4bQyu5kgAhRZvHO5fydKQ3YUVfxQg16VLhvvoasV-fG-qqDh3DDlafj9QB075TleWF0T-E9Yxf_5rhBVNPnQNgFt3a-LVB-y4slL3K5SZR4z_bHYvoBy6lyCIjXFyNhRzGq5zfORwJgyvASJzFg5uqhaXLpj4QkWp3pjsMgwylrxpU96RH3oU1F9M-83IA6It1RG_VHQhkxILPl0sL-U2b7cU75iguekuF8_8mu-uGKxZdrRflRxi1wA3g1TUr0XkrFdC36hE9CjO1hgPLfO4N1-I_wQT6XnYf_O2HeIXt4oH0PnJLQDnl9yH0f1ZY3AlWQQNJPwbnHhBQYInMedzKoi8vkm0jZuZDDW5PG6iXgUmtdcdk0aDFIK03KwDMEnMXTKO28Tw0tVBEkKcYi6xkHo3YDbZT4Qm3nhk6v3CVgPCCGok6RpGMJVcApzcFp1ZEIeIiH8eg1BloO3AQCfn0QgXW3vPpBJYTS8KwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش مشاور عالی سپاه به ادعای ترامپ مبنی بر کنترل تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/698187" target="_blank">📅 21:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698186">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/482cb77a54.mp4?token=SAQ6X2CdUFr5RX6X9TbhjquBTByFeu3O40ftOraFF-jyOsxMWMyGO97YZt6-AyexBI1I9JVLUZdmZGlxq950yTTMwx9hb9W2aWN3Cxo9PuzBdZMqAGoY73tCEj-FmgCxqHn9RE4J0BgtC_TCnsrrUmEyQ_FH15MYpQUCiS-bcmh1K_AAUXt_5oJenXwGibM41i8Qk8u8pDPFIPpMlHar7O6cHztiwt9HD0frDiTalCEfsk-a3eqk-U8yM0MWUDbzyj9bInoIx3A4JjJn1d8g7hoCg1G9PrPNXjdQYvYN_e9yuv_qTp0ng-SrY2yhPkM9_epmh1dLfKjr3FY3uxPNHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/482cb77a54.mp4?token=SAQ6X2CdUFr5RX6X9TbhjquBTByFeu3O40ftOraFF-jyOsxMWMyGO97YZt6-AyexBI1I9JVLUZdmZGlxq950yTTMwx9hb9W2aWN3Cxo9PuzBdZMqAGoY73tCEj-FmgCxqHn9RE4J0BgtC_TCnsrrUmEyQ_FH15MYpQUCiS-bcmh1K_AAUXt_5oJenXwGibM41i8Qk8u8pDPFIPpMlHar7O6cHztiwt9HD0frDiTalCEfsk-a3eqk-U8yM0MWUDbzyj9bInoIx3A4JjJn1d8g7hoCg1G9PrPNXjdQYvYN_e9yuv_qTp0ng-SrY2yhPkM9_epmh1dLfKjr3FY3uxPNHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا به خاطر سیگار، تارهای صوتی و حنجره از بین می‌روند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/698186" target="_blank">📅 21:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698184">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
دریادار عظمایی، فرمانده نیروی دریایی سپاه: آمریکایی‌ها اگر فکر می‌کنند تنگۀ هرمز باز است نزدیک‌تر بیایند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/698184" target="_blank">📅 21:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698183">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f65bad778.mp4?token=oqkyHIpCOKVFQRWsDO1rk47Dm7uc6yg9ciNtJXihdbN9imv4pEfFrK3frm5EkBW05nymW0HvUGunIeJWiuu2Gsuk4DoBVSUUZ7ec-Tek3WLXPP_IcalsZl5enSISLxZi-UPi9qCRCAe4qBS7EZbRGM2dqt4KARezqqm_lSahlkzwy5pCrMrPWLhLkxONIXQXIhObIsNzW7aJfvCF7QX_swdyrNjIefMRHqeXjx6WIdQzhVbwfGRc3uTSWKx0TZM49lXpvTdZD7q4ucJaxLGCI9tCq0lY3fn7w9e5D2Zh0C3KfjompTibzkog3FkFzgTHCpuI2NtuqDqkDgIyhMSsXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f65bad778.mp4?token=oqkyHIpCOKVFQRWsDO1rk47Dm7uc6yg9ciNtJXihdbN9imv4pEfFrK3frm5EkBW05nymW0HvUGunIeJWiuu2Gsuk4DoBVSUUZ7ec-Tek3WLXPP_IcalsZl5enSISLxZi-UPi9qCRCAe4qBS7EZbRGM2dqt4KARezqqm_lSahlkzwy5pCrMrPWLhLkxONIXQXIhObIsNzW7aJfvCF7QX_swdyrNjIefMRHqeXjx6WIdQzhVbwfGRc3uTSWKx0TZM49lXpvTdZD7q4ucJaxLGCI9tCq0lY3fn7w9e5D2Zh0C3KfjompTibzkog3FkFzgTHCpuI2NtuqDqkDgIyhMSsXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی: آمریکایی‌ها اگر تصمیم به حملۀ زمینی بگیرند آن‌قدر تلفات خواهند داد که خودشان تسلیم شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/698183" target="_blank">📅 21:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698182">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآیت الله حسینی طهرانی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcbn89uxtIwCPTM-e5KjemBHhG7r5PENltY0h_UDwBHG9QhIjnSy-bboPW0Kk2fYRIDMWQ95YddZnAoDt302QY0MzjGzVYlvCuRWTyXplVAnpdHnYPJAqXsPlPUK4r8UBHc5KeMfo-H0UuVeX0lUk8RbDPOnuSKEvkleCupX-GskQBegh0SA3OHhfYSzT6kXN3U-2ciWUFJsigYXd4L7HxAQ7Eq7R9MD1LdbC45tJKcvx9vs4obqX2mChNOoNzEvoOSkztwbgFJZx_i5SnQpjZMmGuKFizwwrSCjdVcqr5VFnG3JAH3o7cjRHgB8iTExsi7yodLvYWC9_CbVTTWA1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحیم
🔸
حقیر به اخوان و اخوات گرامی سابقا هم مکرّر عرض کرده بودم که:
حضور در تجمّعات شبانه در این شرائط، موجب رضایت مولایمان حضرت صاحب الزمان علیه‌السلام، و نصرت نائب بزرگوار ایشان: آیت‌الـله خامنه‌ای حفظه‌اللـه، و وسیلهٔ عزّت اسلام و دفع طمع کفّار و مستکبران از میهن اسلامی است.
🔻
و تا زمانی‌که فتنه‌ها و شیطنت‌های دشمنان باقی است و رهبر معظّم نظرشان بر حضور در تجمّعات است، شایسته است که همه در حدّ توان و وجود شرائط حضور داشته باشند. و البته مخدّرات در عین حضور، کمال عفت و حیاء را نیز مراعات نمایند.
🔸
نفس حضور در این تجمّعات به قصد تقویت حکومت اسلام مصداق جهاد فی سبیل الله و سلوک الی اللـه است. خداوند همه ما در تحصیل رضایت امام عصر عجّل‌اللـه‌فرجه‌الشریف موفّق بدارد.
و السلام علیکم و رحمة الله و برکاته
✍️
العبد الآثم السیّد محمّدصادق الحسینی الطهرانی غفراللـه‌له
🗓
۲۶ ربیع‌الثانی ۱۴۴۸ هجریهٔ قمریه علی هاجرها الاف الثناء
🔗
hoseini_tehrani</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/698182" target="_blank">📅 21:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698181">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87b5f17af4.mp4?token=qjuUS6JfFyXwdTIchVcHOBQKuiAqrwKc_-3KNeWzn8bb17A9_dEEu7NKVbWzZMfVBRKAUWW7Temb7aLuQ9GlOsxB78AgtK_gMIxrCel8OIpVyOXcKzVp1PmaFnNZ2Kv7ngIzBxD4SIemRRKvEI1GRPWRfOpqkpIeTTdOxq_7bByGd4cHcav06UWa8vo_7Pp8rBTbPvJC8Glmn70baMG_BfWYxjobw4rVDsOINQNnbXB2mN1e0mrc0p8WsfZeV-Xmtj_Z3iIj8pKdb8sCKooYLNlAsosnnD0RFMt7k00lIuMHqavG_t0WfgfL605CRTJZN5AFsuJ8TkO13xbniBUrSAT1NA6ebtnRgan_CB1A02PNsUauzQ14nJzd1B1Mj3AZhMqRcl7pChVVDAKctC3ScimCS5P5lGLhK4asBNZkiQkUy03q9vQ_GqtZAX-t0gsJ1tDrC-imkIVTpoLW9yRcBT4hgAi3PrEDUgOPKKStuEKpugPPJM-kfil9-PxUaEYbiHlKP-nvglFFp122oTjpAyAcIcp9mqBq7IskslQm8cDiHeIgHovWGU3c9bkAb3T6oACMagRMDQc2SHYIfEjyZjFDop2JEYa0KxkuXq4tpPfgsyhCc09EgwIMRH8RMyx0cKpqqczv2nQhHfOnPBa3iH6MBREKz7KPHbNaTFuaalQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87b5f17af4.mp4?token=qjuUS6JfFyXwdTIchVcHOBQKuiAqrwKc_-3KNeWzn8bb17A9_dEEu7NKVbWzZMfVBRKAUWW7Temb7aLuQ9GlOsxB78AgtK_gMIxrCel8OIpVyOXcKzVp1PmaFnNZ2Kv7ngIzBxD4SIemRRKvEI1GRPWRfOpqkpIeTTdOxq_7bByGd4cHcav06UWa8vo_7Pp8rBTbPvJC8Glmn70baMG_BfWYxjobw4rVDsOINQNnbXB2mN1e0mrc0p8WsfZeV-Xmtj_Z3iIj8pKdb8sCKooYLNlAsosnnD0RFMt7k00lIuMHqavG_t0WfgfL605CRTJZN5AFsuJ8TkO13xbniBUrSAT1NA6ebtnRgan_CB1A02PNsUauzQ14nJzd1B1Mj3AZhMqRcl7pChVVDAKctC3ScimCS5P5lGLhK4asBNZkiQkUy03q9vQ_GqtZAX-t0gsJ1tDrC-imkIVTpoLW9yRcBT4hgAi3PrEDUgOPKKStuEKpugPPJM-kfil9-PxUaEYbiHlKP-nvglFFp122oTjpAyAcIcp9mqBq7IskslQm8cDiHeIgHovWGU3c9bkAb3T6oACMagRMDQc2SHYIfEjyZjFDop2JEYa0KxkuXq4tpPfgsyhCc09EgwIMRH8RMyx0cKpqqczv2nQhHfOnPBa3iH6MBREKz7KPHbNaTFuaalQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشف ۳۰ تن گوشت فاسد در کارخانه تولید همبرگر در شاهرود
#اخبار_سمنان
در فضای مجازی
👇
@Akhbar_Semnan</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/698181" target="_blank">📅 21:07 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698176">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D3ydcCr1O7DMiYTcwy2zkqi5bHWqFNme0DRRXIRg_QnzUV-xOqZ_Anc94pcfLrPglKoSG0-0zoRSrmlnwe18CkWH1OFyHdpw9FSJKrSXKv0C_XCVCpo6Q5Nnn0e_jxtoUfMbiaRtWS51MloEmealHEeniQRyJwAWYa-XvaJsBEYXh0DKW8bwzG00qd93AS3cje2SHkQDuagA6Q4Rs-Krfw-J-nsBGgNWoKPUAww_rLxnFAm2Oq3E3TGtWYihMWKwxhRHejBz1P7tFcvUgbJNADo7QDacJwyAwIlcn_mI-znd8OPXSv4fH3tQsG3Fb7BRGeRgJ_cR6QdQHpgSNlUU2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2frgEgqAyD_ALTyJuMAhrvPdPN2cwPArSPuOda6LxKdz1kTKJks9ZHL3WFgASvi8bEJRWHzcWCt2-ld_xCtrN-jhjRX2KY-DJpthDIFiuORxrThuP6Cg20D03wUUFVgBcQ3yGf5241h1DoqsPo5j4WAhGdiuuU3Wqay_7_HcC9CosxoflcgZfgQm8X97KnVxZFnOYej_HBmPiEQ_aY5aXGxMOZaZImUkO4nTrmMUSSGUrwewVhq6WFidHmf9GmpbyIN49F5cseHUNy2dFjDOguCfc84HlKTCNyY1sZjYOwdZv0KmP7IefBuUmck2mGmR36_CdcQI2S9CEXa0Hh2tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_4Nf71ljivqIlO52buHX5EbmJThZRWeF2DWkK-PXcGJarT3mBBG3YnZGnBw9ri-nTJBgi3F-MDPhCVgHIvZaSkCq1q-r5dw7qjoBvnQg66swgwgy7zZBSctK_h9WzL2ZQv6JH01l2bW9ONTYwQAVtneqeg_JEhTN4BteuUfG0Ig5AGsGu7kTu_q9wFTS_s9qOpwyMaY5PoCY24i9wQtaO_H1tPW1byFh2u7TOEGkiGqNzlJJrn-40W49jacJDVwJRXjrUIoXYztkffw7qxXPimj-dwYTJZBM6BpbpwdxSlGsJak-prgl2EUvmr4Bev9JN3HDpNKCfA9Fu4mKfsbTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hwoch3WO0Kq1OJkXId-LBvnZ8WMAULa4azR5GLZKNICR8_DnebZ3WlAbOT3Gf0APPrtxUn5mnQq7_-FlyI9LtZWvea1THg88Z-aL50by_kI8ZA8GQWfABaFearTDrqieGbLrSCFxxyZ_cvCmGa4aNr-UJ_vUx3nPFYUeUYSQIBjA5Upi_KkSKqN92AWWEUrrKTkrJ5dCDA3QX7XXy4Ds5-B5pQf5aBQMFyG3wY4wEyxXICxzoNFlBL4oCw09SBAiIzre0CBq9xICdUt-6AIWUnLCOzei5rp8RYG-u-75MDP88vSfrp1wP8h9BHGZR0dipzRZ_zAu4so_L9m2fa7xxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z0e5-LfHWLvec_Q9_51PBhZyzott4sPuxF3HwD8eE5rQ1cFpiPPPhL3bhqZy0h_a78db4uAOBQEEhgSNVZE4BlcTwRuEBLQSs6b6JPoc_OODsZha0KHcGcvlsaWvXc5foy9xbqRT1pmi50fub60w3QSgYsBTGcPep5akJ0aM7wyQlT706KyLzexnDonlNyXWIuv1Y54ypojEpDBK9-a3CtkEyaPxtKWJvohLiILt_4AgHhtzDqTX6MIGHNNJU9CzrS1pwDlAqM7P-6SS-uxs0ZtXVj8Iceu8QNbjbN38YVB-4PNFthKIlDa9NHS8qU2i8bRxOpFWvfs754jy9Ie_aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵۰ اپلیکیشن کاربردی که اگه روی گوشی‌ نداشته باشی، ضرر کردی!
#هوش_فوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/698176" target="_blank">📅 21:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698175">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ظهوریان: امکان نظارت بر کالابرگ برای این که دقیقاً صرف چه کالاهایی می‌شود، کاهش یافته است
میثم ظهوریان، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
مبلغ فعلی کالابرگ به دلیل تورم هزینه نیازهای اساسی خانوار را پوشش نمی‌دهد، با این حال میزان دقیق پوشش آن به دلیل تفاوت نیاز خانواده‌ها مشخص نیست.
🔹
با اضافه شدن فروشگاه‌های معمولی و گسترش اقلام قابل خرید، امکان نظارت بر اینکه کالابرگ دقیقاً صرف چه کالاهایی می‌شود، کاهش یافته است.
🔹
دولت می‌توانست کالابرگ را به سبد مشخصی از کالاهای اساسی متصل کند تا علاوه بر تأمین نیاز مردم، تقاضا برای تولید محصولات منتخب نیز افزایش یابد، اما این سیاست به‌طور کامل اجرا نشد.
🔹
دولت وعده داده بود اعتبار کالابرگ را متناسب با نرخ تورم و قیمت کالاهای اساسی به‌روز کند، اما عملی نشدن این وعده می‌تواند اعتماد مردم به طرح‌های اصلاحی آینده را کاهش دهد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/698175" target="_blank">📅 21:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698174">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
دریادار عظمایی، فرمانده نیروی دریایی سپاه: آمریکایی‌ها اگر فکر می‌کنند تنگۀ هرمز باز است نزدیک‌تر بیایند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/698174" target="_blank">📅 20:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698173">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11324dfbde.mp4?token=DTh6L4KSgUzrS8BawUCcSeqd4tLl1XG-ubQbadKGeIL6s8o_SKLx1SKR3s3xILz6nODryuB36xmKjdZlYHttc6_CjAbDbT-KOO8qqUz3lPdXKmxIv5bgdKCyfexJrH9QOsNsb1zksN7qMG1LC5DcV2R7ErhYlIrAlBNlvA2wCUkURK0ctNMixEXyKH_i-Wa3zwtpxWM1hD7l8HWlFpvjbRvmpA_LgqHajMDLDjFpMuOxwzj27Rv6glnrz97WXBUtOFQRmPYeZ3C8o-Bt5qlT0TsbRzkx5JdUr3KNbw_mFqKZalGuVz8zv6Aty9EZUGnLz4tc9ORmHkPNlUnszidj_kypGhaYbVDEUM8tE-PeLHp1BESwoxDHYLdQyHalyw3dquS8-5ycU3kaaOFoGr6nO5hq_FPw5cq0i9EGwIx0z4hpLKXB0TcmSc30KzXL--Yb361I-QDVfGOxCq_xOkILDYnoIveiyMP_0VH0EFDZ7PmrH5OgFXy-owd5kw_u7pDPyTcytfxgx_BJ80sDEuQVJmdiNCdXbp4rY3GoMJO3G6KdW8SS6ysGc1AKpvbgZ008H4ZPryfUDK1fF4hJcKen-pvXURRFU1sK_fsUDBiIZS5W0053Yth_OmX4Wd0u_OQ7zF10XPHBPMlnYUuv0PDXwlZaGyT8n8W1UYSh7S_6LLk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11324dfbde.mp4?token=DTh6L4KSgUzrS8BawUCcSeqd4tLl1XG-ubQbadKGeIL6s8o_SKLx1SKR3s3xILz6nODryuB36xmKjdZlYHttc6_CjAbDbT-KOO8qqUz3lPdXKmxIv5bgdKCyfexJrH9QOsNsb1zksN7qMG1LC5DcV2R7ErhYlIrAlBNlvA2wCUkURK0ctNMixEXyKH_i-Wa3zwtpxWM1hD7l8HWlFpvjbRvmpA_LgqHajMDLDjFpMuOxwzj27Rv6glnrz97WXBUtOFQRmPYeZ3C8o-Bt5qlT0TsbRzkx5JdUr3KNbw_mFqKZalGuVz8zv6Aty9EZUGnLz4tc9ORmHkPNlUnszidj_kypGhaYbVDEUM8tE-PeLHp1BESwoxDHYLdQyHalyw3dquS8-5ycU3kaaOFoGr6nO5hq_FPw5cq0i9EGwIx0z4hpLKXB0TcmSc30KzXL--Yb361I-QDVfGOxCq_xOkILDYnoIveiyMP_0VH0EFDZ7PmrH5OgFXy-owd5kw_u7pDPyTcytfxgx_BJ80sDEuQVJmdiNCdXbp4rY3GoMJO3G6KdW8SS6ysGc1AKpvbgZ008H4ZPryfUDK1fF4hJcKen-pvXURRFU1sK_fsUDBiIZS5W0053Yth_OmX4Wd0u_OQ7zF10XPHBPMlnYUuv0PDXwlZaGyT8n8W1UYSh7S_6LLk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
می‌دونین موضوع قدیمی‌ترین بیلبورد جهان که ۲۵ قرن پیش داریوش بزرگ بر سنگ نوشت، چیست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/698173" target="_blank">📅 20:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698172">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff0afaa5d.mp4?token=ERhU92RmgYwKMiBF4n_w6Kp4SiNKtxgRxSV9wjDJ0a-vI6vqYe1w80-ADlnzpC7-yGDQ_WFv8KXykj7d8uaBSrNG47IM6roPAhyr4YbOe6KyB4IwT-fP1GJK9Zy-WBUzeqGYaq4ZavM4LW0waD4oYLVNPIyyAy_TH7ii1QyHv9tZj1Utg2w6-W_qAv41sDHuyGzJIk9W9wvp8ttLZlm2IbfllrHSIn95azI07Knw3r4EVpZgue76hJHrLUWEpTvCii3kYsuH-cq78YLHkU0ufMAsNt-ZZM_rn_0Ma3zqPOAaQpFuBsGyJlcBKtjzRJuvMiXhLLYaDy1JTozmyjIp2ino1Se96g9HIdFcP0AEYgfUwdcA5JSyIkzi0Su0j9cWwjXq_wtwOkY_q67rlczmZefjkJLLdlFU_cdRLuV9qMDTF7tVkIeShV4_AEcLv0DY85DFmrH8eePMewyV6CYIdya3pNZzC62gIFe90toC25reZbcHv4oxtP0T1e6Z5iGOILB2OwQhHPt7e000yIuEWV6eKhbjoshwX2uoUhzcxuBxmM0om59OGJ_ARPJbqGuSA4258UmcD47lTWnXNMFyWqvrr45vyzEkEJipCmRB0EG-RabNP4gq5lBDDvAv_byXC_ptNgasETNNlazABrOFvQ7o-xRNqpq_Zfngq9Mr4E0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff0afaa5d.mp4?token=ERhU92RmgYwKMiBF4n_w6Kp4SiNKtxgRxSV9wjDJ0a-vI6vqYe1w80-ADlnzpC7-yGDQ_WFv8KXykj7d8uaBSrNG47IM6roPAhyr4YbOe6KyB4IwT-fP1GJK9Zy-WBUzeqGYaq4ZavM4LW0waD4oYLVNPIyyAy_TH7ii1QyHv9tZj1Utg2w6-W_qAv41sDHuyGzJIk9W9wvp8ttLZlm2IbfllrHSIn95azI07Knw3r4EVpZgue76hJHrLUWEpTvCii3kYsuH-cq78YLHkU0ufMAsNt-ZZM_rn_0Ma3zqPOAaQpFuBsGyJlcBKtjzRJuvMiXhLLYaDy1JTozmyjIp2ino1Se96g9HIdFcP0AEYgfUwdcA5JSyIkzi0Su0j9cWwjXq_wtwOkY_q67rlczmZefjkJLLdlFU_cdRLuV9qMDTF7tVkIeShV4_AEcLv0DY85DFmrH8eePMewyV6CYIdya3pNZzC62gIFe90toC25reZbcHv4oxtP0T1e6Z5iGOILB2OwQhHPt7e000yIuEWV6eKhbjoshwX2uoUhzcxuBxmM0om59OGJ_ARPJbqGuSA4258UmcD47lTWnXNMFyWqvrr45vyzEkEJipCmRB0EG-RabNP4gq5lBDDvAv_byXC_ptNgasETNNlazABrOFvQ7o-xRNqpq_Zfngq9Mr4E0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حیوان خانگی وقتی دغدغه‌ات نان شب و آینده مالیته، شاید بیشتر از عشق، هزینه و انرژی ازت بگیره
برای ثبت نام همایش بزرگ استاد مطلبی در مشهد از کد تخفیف BMT72 در لینک زیر استفاده کنید
👇
https://evand.com</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/698172" target="_blank">📅 20:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698171">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
سردار کارگر: راه‌های جدید برای ارتباط اقتصادی با کشورهای منطقه پیدا شده است
سردار بهمن کارگر در
#گفتگو
با خبرفوری:
🔹
تنگه هرمز کماکان بسته است و نیروهای مسلح جمهوری اسلامی ایران بر این منطقه احاطه کامل دارند. گرچه دشمن ادعاهایی دارد، اما نیروهای مسلح با به‌کارگیری تاکتیک‌های جدید، احاطه بیشتری بر مجموعه تنگه هرمز دارند.
🔹
در صورت پایبندی دشمنان، به‌ویژه آمریکا، به شروط و تعهدات خود، تصمیمات بعدی در داخل نظام گرفته خواهد شد. جمهوری اسلامی ایران تاکنون تاب‌آوری بالایی از خود نشان داده است.
🔹
جمهوری اسلامی توفیقاتی در زمینه پیدا کردن مسیرهای جدید برای تأمین کالاهای اساسی و توسعه ارتباطات اقتصادی داشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/698171" target="_blank">📅 20:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698169">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5VG07ujR3l6-obc5LPrXdiO0-upWMx2_zQ9yymvMkAkSR9fhpIPoEcAVtA2yqoIHADCYASaEy4yHWLweX9ie_1ngz9gC36HSKkg5Zbfeq1qigG3aoLL1zj0Q3ckowpX5_iTC8rcszEniMIgzyRj8fWlyyYrRB2kCItIEHZa6mhg0QnrHyfWYI6CqDS6jaIpV92PYy_oXu2T6b29fvIFr5ro1cQFPcaH6HTsYAYe9FYqJG4lLUgIvcLrrJkqAXQVbDV-ffBC3sOl-yrzlGyar2PXGi8chodSvPFi9pxgbjgMbvgdMio_ERCTrk8dEaieZb5QvxSkES9qRpjXfpTaSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ سالگرد تأسیس نیروی دریایی آمریکا را تبریک گفت و محاصره ایران در تنگه هرمز را دستاورد تاریخی خواند!
🔹
از دیگر افتخارات نیروی دریایی آمریکا می‌توان به بستن تنگه‌ای که باز بود و بعد، دست‌به‌دامن دیگران شدن برای باز کردنش اشاره کرد!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/698169" target="_blank">📅 20:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698167">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
نیروهای مسلح یمن به ۴۰ کیلومتری جاده ساحلی در خلیج عدن رسیدند
/ صداوسیما
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/698167" target="_blank">📅 20:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698166">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dS8AWCimRh98YXfoBZR6Ss8AAE19z6dWYE7roMDRDTxL9dFjNe_5XxvsbGyG7oMduCJjqI-Xrma-hDJXTAshO1cVYr2W8OFwnU9Dw6cAjjTck0lT5aJElChIwhuES2qiuBd_eXsy6jRZ9bVXpxbtV5FEeKC3orVArjGWw9nAZAJOtfddDQ9Xa28xeVAP3yi9F2Lwl6rHOLElTO3FkplFwjdtZ_u0gX8j8miMdjI3R3oJV-lDTvjrMw7kx9IgQYuWOxo8u2yABSUQaL9GrWv2Lg8ykLwSiZtQ-RuDS5uOkEwU7H4-njAP_oFKy1Fx364tIYjQmQQ_oKIo69zdIWr4tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیرعامل شرکت آب و نیرو در کنفرانس بین‌المللی مدیریت پروژه: مدیریت تاب‌آور؛ پارادایم نوین پیشبرد پروژه‌های زیرساختی در زمان جنگ و تحریم و محاصره
🔹
مهندس داود کامگار، مدیرعامل شرکت توسعه منابع آب و نیروی ایران در این کنفرانس، با آسیب‌شناسی دقیق وضعیت فعلی پروژه‌های زیرساختی، استراتژی «مدیریت تاب‌آور» را به عنوان تنها راه برون‌رفت از بن‌بست‌های اجرایی شرایط موجود معرفی کرد. تغییری که در آن موفقیت، در خلق ارزش از منابع محدود و کاهش «زمان افق طراحی پروژه‌ها» معنا می‌یابد.
🔹
وی افزود: در شرایطی که زنجیره تأمین با چالش‌های اساسی روبروست، اصرار بر اتمام کامل یک ابرطرح می‌تواند منجر به حبس سرمایه‌های عظیم و افزایش طرح‌های نیمه‌تمام شود. لذا راهکار رست، «خُرد کردن» پروژه‌ها به بخش‌های مستقل، مرحله‌ای و زودبازده است، تا مردم بتوانند از منافع آن زودتر منتفع شوند.
🔹
مهندس کامگار گفت: استفاده از مهندسی ارزش و مدیریت ریسک از همان ابتدای پروژه، کلید جلوگیری از اتلاف منابعی است که در شرایط بحرانی، به‌سادگی قابل جایگزینی نیستند. لازم است منابع و لجستیک طرحها با هم دیده شده و از انباشت دارایی‌ها جلوگیری شود.
🔹
وی افزود: تصمیم‌گیری جسورانه در شرایط پر ریسک کنونی اجتناب‌ناپذیر است و باید از مدیران پروژه در این مسیر خطیر حمایت شود.
🔹
مدیرعامل شرکت آب و نیرو، انگیزش، تأمین نیازها و حفظ روحیه سرمایه‌های انسانی را، بخشی لاینفک از استراتژی مدیریت تاب‌آور طرحها دانست.
🔹
مدیرعامل شرکت آب و نیرو در بخش پایانی سخنان خود تاکید کرد: معیار موفقیت در پروژه‌های زیرساختی باید از «زمان و هزینه صرف» به «میزان ارزش و منفعت ملی ایجاد شده» تغییر کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/698166" target="_blank">📅 20:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698165">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50226ddbc1.mp4?token=meO6CpTZJrkUN86onj0D6CQ84go8-dn5qyjaDver_QVeI9qW7d-iFOQnvoM7znyo58XwwgcCyexeozKlVz7092WdnUvd6Qf4s3qt81d0gtSfKjItQsg3mMAWBLCbsyNatYrq1ge6RvUAYSZ1yFnFZ1vmCinfsTrOC-3T2V2TK1tcGHk2G3akp-J0FQDmEmHx-0_C3jDF66M3LLOVC4YLOxQp-ulwKfkfn9wbBPWj8M6v4sAxzKyybiVjqaNr7Ozkml1Fi0MYIxdsiKqsaRfbm66GtlOUsLGW4iq3IcmGlnM23ozYTyCYI7dnv3Gklh4G60r5CD-zMkOD1KCIZ-WosG6GCRsr255kyDd8pAL_fQKyJ8scvp1Ym4vkL_9OE9U5iNa7oato18WkoOQdfJ7w55igiefZXepVEGp9LovenlnhAT90T97eA-yQvjeKqE1nrT4Iira3CIv64sLb0euwleomPsIrhTfd15Wt2BmbY_IIzXmlhHZO1jaX7VMVjMHep1ppGwdTQWEDHBF8hj2cw8vyTFGjS8yn1GRcRNuky7VDCbpTTfB3SRxmUt3_cMbRq_X6gW90SBApsH9bL551cUbyZDID4T-TXtjZIn-0qetjDj4XGpd7GXKDqwANxooq0ljYS_n0OZGN1CFxAUB8HgQIl_k9HB6Y5tO0joLm_lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50226ddbc1.mp4?token=meO6CpTZJrkUN86onj0D6CQ84go8-dn5qyjaDver_QVeI9qW7d-iFOQnvoM7znyo58XwwgcCyexeozKlVz7092WdnUvd6Qf4s3qt81d0gtSfKjItQsg3mMAWBLCbsyNatYrq1ge6RvUAYSZ1yFnFZ1vmCinfsTrOC-3T2V2TK1tcGHk2G3akp-J0FQDmEmHx-0_C3jDF66M3LLOVC4YLOxQp-ulwKfkfn9wbBPWj8M6v4sAxzKyybiVjqaNr7Ozkml1Fi0MYIxdsiKqsaRfbm66GtlOUsLGW4iq3IcmGlnM23ozYTyCYI7dnv3Gklh4G60r5CD-zMkOD1KCIZ-WosG6GCRsr255kyDd8pAL_fQKyJ8scvp1Ym4vkL_9OE9U5iNa7oato18WkoOQdfJ7w55igiefZXepVEGp9LovenlnhAT90T97eA-yQvjeKqE1nrT4Iira3CIv64sLb0euwleomPsIrhTfd15Wt2BmbY_IIzXmlhHZO1jaX7VMVjMHep1ppGwdTQWEDHBF8hj2cw8vyTFGjS8yn1GRcRNuky7VDCbpTTfB3SRxmUt3_cMbRq_X6gW90SBApsH9bL551cUbyZDID4T-TXtjZIn-0qetjDj4XGpd7GXKDqwANxooq0ljYS_n0OZGN1CFxAUB8HgQIl_k9HB6Y5tO0joLm_lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اجرای جالب پسران دانشجو در خوابگاه که در چند ساعت میلیونی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/698165" target="_blank">📅 20:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698164">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
سارق مسلحی که به خبرنگار هم دروغ گفت
🔹
باند چهارنفره سارقان مسلح که با استفاده از سلاح جنگی اقدام به سرقت ۲۰۰ گرم طلا و ۳۰ ساعت لوکس کرده بودند، پس از دستگیری، در گفتگو با دوربین خبرفوری فرافکنی‌های عجیب داشتند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/698164" target="_blank">📅 20:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698162">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4RsgORs_GruAi6WnSbjj1Okci_Ou9s8BiNwpkn-6MX-y6k-bRxFksseaWX79tZh6I7GI-nqr-Je61i4zrJ85G7HizCnXqnRx5p6VAUCdP_aHjIaWvgFfekY3avotHow0zvK4CkkwWjefX3N9EuvvL4TKpbPyB6sJIvy0hd3heVQXfojsHBGLYE7elelfYAa9S4nf1VTOa8UNKrYPlGwpHLhJT4C2MfolXjCd8h7H7di-Co_rPLunMboHNch8qs0NsZQEl4UUmS7ppq9iioiRfGcOrc8SY8SyYuaep7Q7v9dWT64Fen8ZHxeJ2hw-W23ceY1QL4zJ07klBpZ70EjJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ما منتظریم
🔹
سخنگوی سپاه با انتشار تصویری در فضای مجازی نوشت: ما منتظریم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/698162" target="_blank">📅 20:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698161">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixLSFdhXg2Y-lRygn3A9TkYjRKGxGKqJ8e4l1hWu5E2MK8_Iua78uZ23G7eYBqwvCyqpb5M7A1CTiude5XrdgQNLt4gnD51aKfCBeLvse045z0OX_Nv3wUP6xS0ryY44vuLjNNh7rg2CuMleAZsxq9NK0lBKoLee69HO-A4IjaTm-5ZiGw_8Lj4uYkuEWTZIy1L5WgmXKHXy8RZSG0Nuktd3PvtIQoqVe7Gnq4bRiJaP7Vk5BILrtJzZeb8fdCsayFY2ay4kPoYYZKfug_L4Rurt9QOZy1j3pSmyqu1VQmnWcRNJgDGVuNAtKHKEvlrmYfdzQqG9yfwLCEEkJrYjWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬅️
در بازدید سرپرست وزارت نفت و مدیرعامل بانک شهر از پارس جنوبی صورت گرفت
🟢
پشتیبانی ۸۰۰ میلیون یورویی بانک شهر از بازسازی تأسیسات آسیب‌دیده پارس جنوبی در جنگ تحمیلی رمضان
🟡
حمید بورد، سرپرست وزارت نفت به همراه مدیرعامل بانک شهر و جمعی از مدیران ارشد این وزارتخانه، از روند بازسازی پالایشگاه پنجم مجتمع گاز پارس جنوبی در فازهای ۹ و ۱۰ بازدید کردند؛ بازدیدی که با هدف بررسی آخرین وضعیت عملیات بازسازی، ارزیابی اقدامات انجام‌شده برای احیای تأسیسات آسیب‌دیده در جنگ تحمیلی رمضان و شناسایی راهکارهای تسریع در بازگشت ظرفیت‌های ازدست‌رفته به چرخه تولید انجام شد.
✅
به گزارش روابط عمومی بانک شهر، حمید بورد سرپرست وزارت نفت، در جریان این بازدید با اشاره به شرایط ناشی از جنایات جنگی دشمن آمریکایی ـ صهیونیستی و آسیب‌های واردشده به تأسیسات صنعت نفت و گاز کشور، از حمایت‌های بانک شهر  به  صنایع نفت، گاز و پتروشیمی قدردانی کرد و این حمایت‌ها را در مسیر بازسازی زیرساخت‌های آسیب‌دیده و تقویت ظرفیت‌های تولیدی کشور حائز اهمیت دانست.
🔵
بورد همچنین با تأکید بر ضرورت تقویت همکاری میان نظام بانکی و صنعت نفت، حمایت مالی بانک‌ها از طرح‌های راهبردی این صنعت را عاملی مؤثر در تسریع روند بازسازی تأسیسات آسیب‌دیده، بازگشت ظرفیت‌های تولیدی و استمرار فعالیت‌های صنعت گاز کشور عنوان کرد.
🔴
دکتر سیدمحمدمهدی احمدی، مدیرعامل بانک شهر، نیز در جریان این بازدید، ضمن بررسی روند بازسازی پالایشگاه پنجم پارس جنوبی، با مدیران ارشد وزارت نفت و صنعت گاز درباره ظرفیت‌های همکاری و نقش تأمین مالی در تسریع عملیات بازسازی گفت‌وگو کرد.
🟡
دکتر احمدی با اشاره به جایگاه راهبردی صنعت نفت، گاز و پتروشیمی در اقتصاد کشور، حمایت از صنایع پیشران و تأمین نیازهای مالی آنها را از محورهای مهم فعالیت بانک شهر دانست و اظهار کرد: بانک شهر با توسعه خدمات پولی، مالی و اعتباری، در کنار صنایع نفت، گاز و پتروشیمی برای حمایت از تولید و تقویت زیرساخت‌های اقتصادی کشور ایستاده است.
⚪️
مدیرعامل بانک شهر با تأکید بر اهمیت تأمین مالی پروژه‌های بزرگ صنعتی افزود: استفاده از ظرفیت‌های نظام بانکی و طراحی راهکارهای متناسب با نیاز صنایع، نقش مؤثری در تسریع اجرای طرح‌های زیرساختی، تأمین تجهیزات و بازگرداندن واحدهای آسیب‌دیده به چرخه تولید دارد.
◀️
تأمین مالی بیش از ۸۰۰ میلیون یورویی بازسازی پارس جنوبی
🔻
بانک شهر با مشارکت در تأمین مالی بیش از ۸۰۰ میلیون یورویی پروژه بازسازی پالایشگاه پنجم پارس جنوبی، در حمایت از احیای تأسیسات آسیب‌دیده صنعت گاز و تقویت پایداری تأمین انرژی کشور نقش‌آفرینی می‌کند.
🗣
این پروژه که فازهای ۹ و ۱۰ پارس جنوبی را دربرمی‌گیرد، با کارفرمایی شرکت نفت و گاز پارس و مشارکت شرکت‌های مهندسی و ساختمان صنایع نفت (اویک) و پایندان، در قالب قرارداد مهندسی، تأمین کالا، ساخت و تأمین مالی (EPCF) اجرا می‌شود.
🔹
در جریان جنگ تحمیلی آمریکایی ـ صهیونیستی، شماری از پالایشگاه‌های گازی منطقه پارس جنوبی هدف حملات دشمن قرار گرفتند که این حملات به آسیب‌دیدن تأسیسات و کاهش بخشی از ظرفیت فرآورش و تولید گاز کشور منجر شد. از این رو، ارزیابی روند بازسازی، شناسایی موانع اجرایی و اتخاذ تدابیر لازم برای تسریع در احیای ظرفیت‌های آسیب‌دیده، با هدف تقویت پایداری شبکه گاز و تأمین انرژی مورد نیاز کشور در آستانه فصل سرد سال، اهمیت ویژه‌ای دارد.
🔴
بانک شهر طی سال‌های اخیر با توسعه همکاری‌های خود با شرکت‌های بزرگ فعال در حوزه نفت، گاز و پتروشیمی، خدمات تخصصی بانکی و مالی از جمله تأمین مالی، گشایش اعتبارات اسنادی و صدور ضمانت‌نامه‌های بانکی را به این صنایع ارائه کرده است. حمایت از صنایع آسیب‌دیده در جنگ تحمیلی، به‌ویژه در بخش پتروشیمی، نیز در چارچوب رویکرد این بانک برای پشتیبانی از تولید و حفظ ظرفیت‌های راهبردی اقتصاد کشور دنبال می‌شود.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/698161" target="_blank">📅 20:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698159">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ead0dacf7.mp4?token=Yx0iAnYVHZrciHVbZg3qeeY_kqaSf9YWLfoe3ZITaQgmlKqp7ubZUW_kpKwMW4FyiONdbJiIcIKXT5fWuijQyoWUBvJR2-LOxrVPArI-Q5h2-3X9fWa1hrX6aJQh8aaasj9KvH3HgV3VFKxOE0Jx7StKKsLs2DhzmO9ErhQj3IGy7nruBUtg28yizq8ygVjsDajJVOaQo_zeueRRWRaTj9pZAdi_vSfN3tRGG6jC8l-GUeD2K8cG-euyD8We_P4o3OBt3LycfOWrw13dWbhJyV6KlvZ2ICDG3Tt9wWcQQhJUA15xX-RFE4AR_762UNM5K_PgJmoH3I2-K3fQo0UlyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ead0dacf7.mp4?token=Yx0iAnYVHZrciHVbZg3qeeY_kqaSf9YWLfoe3ZITaQgmlKqp7ubZUW_kpKwMW4FyiONdbJiIcIKXT5fWuijQyoWUBvJR2-LOxrVPArI-Q5h2-3X9fWa1hrX6aJQh8aaasj9KvH3HgV3VFKxOE0Jx7StKKsLs2DhzmO9ErhQj3IGy7nruBUtg28yizq8ygVjsDajJVOaQo_zeueRRWRaTj9pZAdi_vSfN3tRGG6jC8l-GUeD2K8cG-euyD8We_P4o3OBt3LycfOWrw13dWbhJyV6KlvZ2ICDG3Tt9wWcQQhJUA15xX-RFE4AR_762UNM5K_PgJmoH3I2-K3fQo0UlyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی: سفرای برخی کشورهای خلیج‌فارس از ما برای حمله به پایگاه‌های آمریکا در منطقه تشکر می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/698159" target="_blank">📅 20:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698157">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e7ed94014.mp4?token=g2MWDJsW8kQUB1opcIEwrZxTtgkbS-TdzFAPih0iGztY5LM5nXl3pcs2unEYPI8FI5P1Fzs0RCpKEiW6JrgsUyh74ZOlHmTkdnIgQmsi9NBVzgzR6dcdRgZw4usOimuNFt2s6-7F0StkPyVE1nGTYbSl2mlV61Ccc130HcRR_jB-qWxkbQzvf80svA53s2ePsEwS68IaP7iIfR8LR0ct-u6TlstRpNzLOJKALoR-b2v2YSBED3_pdOieSV_MlfRQRosl4g07u1cgcUl2vj_783OU0SO0se7i3yMa4G-Yom8o9nJElqLllms48JOMqvWsYDkXkan6Yjzcu8pj7xdKH3GPq9McAGyOPWZmyZkizWk7zqcwwj9cj-Wf6w7bjlFbt_gPJL_9qm3AIk44o1Fxvzi6lmPbJJerxtlaFc1wD7KBo7S8lCJTSb3wbYys-P66qsEuZ39hdZPyo18zCmxJ0xyojIWRAdoi3u2riI-m1VoLbHLFzh_98iEOF4iqKL3EP-NxAZv1lXNj7Rta-_4dAyehsW-Iye9JJpvkK2pdDkE8fPEoDAxxDqI0AYhgUb5NNC_kfE4eUlsTyoAyug2VtnQvSRrHbWFiQP2Hbl648FLtY6TaqclBy2J1fEY9aOoDFNGcX2yY_yurbcFZ81dJXnA_HIDn3rYJyKB-Hutihx4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e7ed94014.mp4?token=g2MWDJsW8kQUB1opcIEwrZxTtgkbS-TdzFAPih0iGztY5LM5nXl3pcs2unEYPI8FI5P1Fzs0RCpKEiW6JrgsUyh74ZOlHmTkdnIgQmsi9NBVzgzR6dcdRgZw4usOimuNFt2s6-7F0StkPyVE1nGTYbSl2mlV61Ccc130HcRR_jB-qWxkbQzvf80svA53s2ePsEwS68IaP7iIfR8LR0ct-u6TlstRpNzLOJKALoR-b2v2YSBED3_pdOieSV_MlfRQRosl4g07u1cgcUl2vj_783OU0SO0se7i3yMa4G-Yom8o9nJElqLllms48JOMqvWsYDkXkan6Yjzcu8pj7xdKH3GPq9McAGyOPWZmyZkizWk7zqcwwj9cj-Wf6w7bjlFbt_gPJL_9qm3AIk44o1Fxvzi6lmPbJJerxtlaFc1wD7KBo7S8lCJTSb3wbYys-P66qsEuZ39hdZPyo18zCmxJ0xyojIWRAdoi3u2riI-m1VoLbHLFzh_98iEOF4iqKL3EP-NxAZv1lXNj7Rta-_4dAyehsW-Iye9JJpvkK2pdDkE8fPEoDAxxDqI0AYhgUb5NNC_kfE4eUlsTyoAyug2VtnQvSRrHbWFiQP2Hbl648FLtY6TaqclBy2J1fEY9aOoDFNGcX2yY_yurbcFZ81dJXnA_HIDn3rYJyKB-Hutihx4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی: هلال‌احمر اردن به ما خبر داد که ۲۰۰ آمریکایی در حملۀ ما به اردن کشته شده‌‌اند
🔹
هتل‌های محل اقامت سربازان آمریکایی در کویت و بحرین را که هدف قرار دادیم از سر شب تا صبح آمبولانس به آنجا تردد می‌کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/698157" target="_blank">📅 20:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698156">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991a002efd.mp4?token=WsxXFoOu092MhAYtsTe2HixSp17_DTOckjpZWf4K8-13wMWWVYKzH5RI9LzoXMbC8ci8WXLUd1SkyeuoXEHIjzthxoaucvVa2Sam-vmUkJk9rnL0WqL0wojtC3bC6fMfLF4oTGtelYtu40VDFNq5aqj6crBkf4ogaexmn3UBZyV6ChnBtMI2MLyQfLwBGNCGwEp-uiGd9K-G-qKGOlhpvmvAW2gqWyzZlT-0UHBJaWBGpQMkgswZYx0Z-AmkAJBZ7YnUBMHFago70yVwq2FAxqGKCCpOu3p6wGaUPfJYkfKUtvg8gs3CcXeu5KtrTAnXK__he-EijiuAVEQOhUYmJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991a002efd.mp4?token=WsxXFoOu092MhAYtsTe2HixSp17_DTOckjpZWf4K8-13wMWWVYKzH5RI9LzoXMbC8ci8WXLUd1SkyeuoXEHIjzthxoaucvVa2Sam-vmUkJk9rnL0WqL0wojtC3bC6fMfLF4oTGtelYtu40VDFNq5aqj6crBkf4ogaexmn3UBZyV6ChnBtMI2MLyQfLwBGNCGwEp-uiGd9K-G-qKGOlhpvmvAW2gqWyzZlT-0UHBJaWBGpQMkgswZYx0Z-AmkAJBZ7YnUBMHFago70yVwq2FAxqGKCCpOu3p6wGaUPfJYkfKUtvg8gs3CcXeu5KtrTAnXK__he-EijiuAVEQOhUYmJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه هنوز مجردی، این ویدیو رو ببین!
🔹
قانون تسهیل ازدواج جوانان، از مسکن و اشتغال تا معیشت رو هدف گرفته بود؛ اما بعد از دو دهه، هنوز روی کاغذه!
🔹
جزئیات را در این ویدیو ببینید.
#قانون_متروک
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/698156" target="_blank">📅 20:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698155">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">25-2 Ane Manaee (1404-02-14)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/698155" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه بیست‌وپنجم؛ بخش دوم
🔹
انسانِ بی‌خدا خطرناک‌تر از درندگان! جنایات امروز رژیم صهیونیستی امتداد شرارت تاریخی فراعنه. [00:00]
🔹
شباهت وضعیت امروز با دوران حضرت نوح، انکار مردم نه از ضعف دلیل، که از نفرت نسبت به حق است. [05:10 ]
🔹
مظلومیت‌ها و فداکاری‌های اهل‌بیت برای هدایت بشر از ورطه جهالت به قله قرب الوهیت.  [11:38]
🔹
عظمت حضرت زهرا سلام‌الله‌علیها به‌ مثابه جداکننده نور از ظلمت و شافی مؤمنان از میان آتش. [20:35]
🔹
وسعت دعای اولیای الهی؛ وقتی یک نگاه، یک علاقهٔ درونی، یک نور اندک در دل، رشته‌ای می‌شود برای دستگیری [23:43]
🔹
فعال شدن رشته‌های پنهان دل در بزنگاه‌های سرنوشت‌ساز؛ از محبت حرّ به فاطمه زهرا سلام‌الله‌علیها تا کینه پنهان زبیر نسبت به امیرالمؤمنین علیه‌السلام! [29:05]
🔹
وقتی حب و بغض برای خدا نباشد، اعمال دینی پوششی می‌شوند برای شهوات و خودخواهی‌های پنهان. [34:29]
🔹
مقام خلیل الله یعنی رسیدن به نقطه‌ای که هیچ‌کس جز «خدا» در دل نباشد.  [38:08]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/698155" target="_blank">📅 20:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698154">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWSoEdQCCQhSvSDMvn6GDwfQczhWeKNh71ncd2vKacxryrO831_f3ZtIV9yROz_HgdO5kPlpYCVYxeI2pyn37WMPAWDLWWqH0rp7HKW0HU6kh1EH1eWvtLvFXTlwffEw4J4n_oq4XKD89gF6_PLcTvUb7YwBamKIsrXiQYBT9p_DBOoZEv3iDAm1FqQtCE9w17piasGarbj6XpbsAB4fI8CpBpuvQJuy2g3CNpUAF4nkM5bGGWwm3Eh1z2QRlKQHHWkZUtuTN8w6_JjAifMFAe-bbfCaOAuc-0Myx6ui0qdQ82Rf9CuYnPFLpruU8Hw-IQjD6bXUK06ty8xAAVLMyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بنادر راهبردی اسرائیل و ۵ کشور منطقه در بانک اهداف احتمالی ایران
رسانه جریان به نقل از منابع آگاه:
🔹
بر اساس اسناد و نقشه‌های منتشرشده از سناریوی پاسخ متقابل که توسط رسانه امنیتی جریان منتشر شده، فهرستی از مهم‌ترین بنادر راهبردی منطقه به‌عنوان اهداف احتمالی و اولویت‌دار واکنش موشکی معرفی شده است.
🔹
بر این اساس، در صورت هرگونه آسیب به زیرساخت‌های ایران، گلوگاه‌های اصلی تجارت دریایی، انتقال انرژی، جابه‌جایی کالا و پشتیبانی لجستیکی که ستون فقرات اقتصاد و زنجیره تأمین کشورهای منطقه را تشکیل می‌دهند، در بانک اهداف قرار خواهند گرفت.
🔹
این فهرست، بنادر راهبردی رژیم صهیونیستی و کشورهای عربستان سعودی، امارات متحده عربی، قطر، کویت و بحرین را در بر می‌گیرد. از جمله این مراکز می‌توان به بنادر ایلات، حیفا، اشدود و اشکلون در سرزمین‌های اشغالی، جده، ملک عبدالعزیز، ملک فهد و دمام در عربستان، جبل‌علی، خلیفه، فجیره و خورفکان در امارات، دوحه، حمد و رأس لفان در قطر، میناء الاحمدی و الشعیبه در کویت و بندر بحرین و خلیفه بن سلمان در بحرین اشاره کرد.
#ساعت_صفر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/698154" target="_blank">📅 20:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698153">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEv-C0NR-v8p5o0VIkaC2dZIEPFIptYu_1Wbp1aO--OJ2Fa38scF6ffQZGo-DuLZJM3c_ppXtganfdtTXNEJs0ogpFjPBpJw1j6EMbwN3FerpmnSH6pfPR0iew6e1AmCCZEGcv-XaVpfaymtVB2NB4CH2VatObqYFeTieHoQ7idhLpc3U8HFxVZxww5id09O3VXOUgiyI762E8_Y7ZjCeBM4j8DEqJs5sUJ24vGIyz1pDpKnXjmH-tEWAVrR9bZe7-IwYQPj6OLIzOVz-iWqBgrmXBzYu2tdmhvbufA0bRIcN15DFmhXLhAtiDNwKiCWTgu4u-Jzdk0Y82Nlo8076w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشاور سرمایه‌گذاری ترنج و بانک سامان، اولین صندوق درآمد‌ثابت ارزی بخش خصوصی را تاسیس می‌کنند
🔹
صندوق درآمد‌ثابت ارزی، امکان کسب بازدهی ارزی را فراهم می‌کند و ریسک تورم ارز مرجع را کاهش می‌دهد. مدیریت سرمایه‌گذاری صندوق با مشاور سرمایه‌گذاری ترنج و عملیات ارزی و ضامن نقدشوندگی آن بانک سامان است.
🔹
تجربه مشاور سرمایه‌گذاری ترنج با ۱۱ صندوق سرمایه‌گذاری  و ۱۲۵ همت منابع تحت مدیریت، در کنار بانک سامان به‌عنوان یکی از ۳ بانک برتر خدمات ارزی در کشور، پشتوانه شکل‌گیری این صندوق است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/698153" target="_blank">📅 20:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698152">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
گردش ۵۴ هزار میلیارد تومانی پول در معاملات خورد بورس!
🔹
میانگین هفتگی ارزش معاملات خرد در هفته سوم مهر ۱۴۰۵ به ۵۴٬۱۶۴ میلیارد تومان رسید.
🔹
این رقم در مقیاس دلاری، مرز ۲۰۵ میلیون دلار را ثبت کرد.
🔹
در بازار امروز هم مجموعا مبلغ ۵۴۰۷ میلیارد تومان ورود حقیقی ثبت شد.
🔹
امروز ۷۹ درصد خریدها توسط حقیقی ها و ۲۱ درصد توسط حقوقی ها انجام شد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/698152" target="_blank">📅 19:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698151">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5cDo8j6Pbmm1IwssvYlf4SlFU2LLZxoprEosQWz1onULHo9KTbu6SHxGQ4oWOOQazyzZYIMEbYviOMmGQT_OMyWly7XFlXdpaqQIt4QPDJLIAhGTC18KNwrXd17PH5a8gXyrH4U8awaeKjt6R_cNW_c6e9-AxVS-GwXZ0iqA1KT7DMPCpFW0BDa8aXjJFjLROehOS7o73EXjVcIgpvUarDBA0xF3BKWjDyYVk3GSReY1x-eQCOmEuELo9GENAuWO1vEu3cJyjPupfh5-DeXAFt88mBoQ4xBUBObEdWFb2SAowRkkpLZeAztlE6g0hmiwoQyPl59m_8Nx3tvCaVy_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان درگیری مسلحانه در کورین زاهدان با هلاکت ۵ تروریست
🔹
در این درگیری یک نیروی حافظ امنیت به شهادت رسید. #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/698151" target="_blank">📅 19:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698150">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4vV4_4VWv8DbdfSZ68_zcivpoFQdMRio7276qiYpktNHJAOwlfcoGcujB0JqkhYk2OSnUwfDt1QknybfZ5Y40rs8P4nlECoxBWfPPVvk7zHA00pAya0-luXYKD8IjyrZ_DmtvqOsrqtmQnsdieXCciB3iIrl0fSnOWV7_4BiKdCDgYnrHJ_mEsbRKFAP7ZOAOZiNv7H0D3REFtW4MkVtP5ZCSV8tCmG1EtG5xmMSXfioicSj6NHXTNIXmAqzzUsaqaJvm0wSZ6_XWFzOyZXDiRBWvZEkg1UFeinSaVf0T84uPILxta3pVFqDuYyM8h10YhhrL4jyGZr9YC0w0uALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شکاف کالابرگ و هزینه معیشت | با کالابرگ جدید چه مقدار مواد غذایی می‌توان خرید؟
🔹
افزایش ۵۰۰ هزار تومانی اعتبار کالابرگ، اگرچه می‌تواند بخشی از فشار معیشتی خانوارهای مشمول را کاهش دهد، اما مقایسه این اعتبار با هزینه واقعی تهیه کالاهای اساسی نشان می‌دهد که فاصله میان حمایت دولتی و مخارج غذایی خانوارها همچنان قابل توجه است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3252082</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/698150" target="_blank">📅 19:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698149">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c8a0dfe6.mp4?token=uoptXi_Ds3iTPeqWe_WZTjdLO04HF9YCN-wjrP1qhsE0gzCyrfNmvvo8cZtgSJZc6ruimbj1OYiT0MyrB05iOODdwtvrM9YPopTGVg1Zw4LfkK5Uu0-AZN9rVLX87RtRXgMS-OTfla70mehhzpj1-yBvdkyUchK8TjRJkTHbc9OW8jleFRbsr-ZKm1ij5nH5vKejZgzJzpH1N_mhHN7y8KajG1HTDlcsl-KXYYh3GVFWoMq_-Z9WYjytTiQc2baT1tV57N41QN9tgZQB_OKBQG2Z3KfOcemzSZ2R4eznBJKyhUHp0J-XAzsb4J1SqhntQP6OPAMuSxeW6OX0CF10VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c8a0dfe6.mp4?token=uoptXi_Ds3iTPeqWe_WZTjdLO04HF9YCN-wjrP1qhsE0gzCyrfNmvvo8cZtgSJZc6ruimbj1OYiT0MyrB05iOODdwtvrM9YPopTGVg1Zw4LfkK5Uu0-AZN9rVLX87RtRXgMS-OTfla70mehhzpj1-yBvdkyUchK8TjRJkTHbc9OW8jleFRbsr-ZKm1ij5nH5vKejZgzJzpH1N_mhHN7y8KajG1HTDlcsl-KXYYh3GVFWoMq_-Z9WYjytTiQc2baT1tV57N41QN9tgZQB_OKBQG2Z3KfOcemzSZ2R4eznBJKyhUHp0J-XAzsb4J1SqhntQP6OPAMuSxeW6OX0CF10VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت یوگا برای افزایش تمرکز و کاهش پرش افکار؛ قبل از مطالعه ۲۰ بار انجامش دهید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/698149" target="_blank">📅 19:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698147">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی: برخی با طرح استیضاح عراقچی، به‌دنبال مطرح‌ کردن خود هستند
علی احمدی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
استیضاح عراقچی به کمیسیون امنیت ملی ارجاع نشده و وزیر امور خارجه در جلسه کمیسیون توضیح داد که مذاکرات نیویورک با آمریکا خودسرانه نبوده و پیش از آن با دستگاه‌های ذی‌ربط هماهنگ شده بود، با این حال برخی افراد این موضوع را بیش از اندازه بزرگ کردند.
🔹
با توجه به توضیحات ارائه‌شده از سوی عراقچی و شرایط حساس فعلی کشور، بعید می‌دانم طرح استیضاح به مرحله اجرا برسد یا امضاهای لازم را جمع کند.
🔹
به نظر می‌رسد برخی افراد با طرح چنین موضوعاتی در فضای رسانه‌ای و تبلیغاتی، بیشتر به‌دنبال مطرح‌کردن خودشان هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/698147" target="_blank">📅 19:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698144">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15e26fba09.mp4?token=RgV3rQVP8HufZkhwQZ15kaQLdmZU0I12ynNiRunUZot0uI3PqZAk4fURj1trB9AulXtctJeYFUA8a4kNmANOIBci8rlbjkM-FOj-nYRJAukP1AYJyswh-fzEK_arszivbD96CE9Mb2-pbX4dTeMC7o8X6ImJw2bzhxKuHqxcHt1t-yvcMzfN3AD9EV68Pu8c4v74UsTW0_Jv1ewN5tjUZYPcTkUmcxuInfapVeBZnNFmHd-OfskIXIk5oaMYWTcWhxUx_HJ-fWtvREK3Y_SxocUlDUoi3KH0VdFJPXDdwnK3CfrZRNFII2WAsbg2p3n6UKzxQgso88ZkVVaRAoOj_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15e26fba09.mp4?token=RgV3rQVP8HufZkhwQZ15kaQLdmZU0I12ynNiRunUZot0uI3PqZAk4fURj1trB9AulXtctJeYFUA8a4kNmANOIBci8rlbjkM-FOj-nYRJAukP1AYJyswh-fzEK_arszivbD96CE9Mb2-pbX4dTeMC7o8X6ImJw2bzhxKuHqxcHt1t-yvcMzfN3AD9EV68Pu8c4v74UsTW0_Jv1ewN5tjUZYPcTkUmcxuInfapVeBZnNFmHd-OfskIXIk5oaMYWTcWhxUx_HJ-fWtvREK3Y_SxocUlDUoi3KH0VdFJPXDdwnK3CfrZRNFII2WAsbg2p3n6UKzxQgso88ZkVVaRAoOj_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای هر عضو بدن، چه نوشیدنی‌ای مفید است؟
🥤
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/698144" target="_blank">📅 19:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698143">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ادعای الجزیره به نقل از یک مقام آمریکایی: پاسخ به حمله به یکی از کشتی‌هایمان را با ضربه به کشتی‌های ایرانی خواهیم داد
🔹
حملات ایران به کشتیرانی در تنگه هرمز را از نزدیک زیر نظر داریم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/698143" target="_blank">📅 19:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698142">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ادعاهای تکراری ترامپ: بسیار به‌زودی درباره ایران تصمیمی خواهیم گرفت
🔹
ایران یک کشور شکست‌خورده است؛ ما کنترل تنگه هرمز را در دست داریم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/698142" target="_blank">📅 19:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698141">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocJ2aeK57AijJt9eQlr01KJYjdwqJzLrQgZxUi_CCOW-vEX8_hKkqbyd9DBmJS97VLQHOUhgLthsqyU3D31p1q4ED8rAjD4IoH6dRXR89b4ZfaVWpLQ-dQGsWAClkL3V99rzWN3x2YTkj0NujpxxwpGV5_yeJc6RzNNx-BjeMdtSVd5zpz2okpL-mLLICc5-CisaaCBCeZbDwjiDjZmpY-wBiG7Kc8zwHLVTtbbzWpKwENBludZfuuBfH1ThHIqVFhALyUXy6dNegk64au7Q_zYCm1fXdR9NRKp-otNnc8GyWJvJIe70nIpoQBkG1VmiJ2nsd9HDha8lSKBkS4aocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفیر آمریکا در آستانه برکناری؛ اتهام رفتارهای نامناسب و تخلف!
🔹
ترامپ و روبیو در پی گزارش‌هایی درباره رفتارهای نامناسب، تهدید یک مقام یونانی و تلاش برای استفاده از نفوذ دولتی جهت پرداخت بدهی ۱۰۰ هزار دلاری سفیر آمریکا در یونان، در حال بررسی برکناری او هستند.…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/698141" target="_blank">📅 19:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698139">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
چه کسانی مشمول افزایش اعتبار کالابرگ می‌شوند؟
معاون وزیر کار:
🔹
افراد نیازمندِ خارج از پوشش کمیته امداد و بهزیستی، در صورت تأیید نیازمندی از سوی این نهادها، مشمول طرح می‌شوند.
🔹
افراد در صف حمایت، دریافت‌کنندگان کمک‌های موردی و خانوارهای فاقد خودرو و ملک با درآمد کمتر از سقف تعیین‌شده نیز در این گروه قرار دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/698139" target="_blank">📅 19:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698138">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vB570cO2qCyY20xWyPTejvTgj2eH1dmaVy50QX86mBaJjS6xg_ZZmQYOhzq1JoUBE8TInUGHoZq85GIo8b3s8LmYSoYgMV9YFLLysio0BxYTR76MGRbJRAkdIA1mc_ygK86d04wm6Y1TfR3-ClsJ8OLVEXVLftYDdfomzK02HCOIB2bXNUOWkFSWaPddYszJ1MLpgozhV0QtSl9YD_LNoOh0gb1QThs8YDVQWOwH3FtGrs_wl11Ng0ph4uIWbgDAvM_aGoAcgyHpMqSYlmX04A2B1kJk-bEvzAQug4TQjW_XgLGNttafgkNMqsORgbRNEPbtd-2V50cfpM6B60wQXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغوشی که جان یک نوزاد را نجات داد!
🔹
در سال ۱۹۹۵، وقتی پزشکان از نجات بریل، نوزاد نارس، ناامید شده بودند، پرستاری خواهر دوقلویش کایری را در همان انکوباتور کنار او گذاشت.
🔹
پس از چند دقیقه وضعیت بریل بهبود یافت و کایری دستش را دور خواهرش حلقه کرد؛ این اتفاق بعدها به‌عنوان روایتی الهام‌بخش از روش نگهداری مشترک دوقلوها نقل شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/698138" target="_blank">📅 18:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698137">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
هگزت قربانی ترامپ می‌شود!
دومینیک میشائیل تریپی، تحلیلگر سیاسی:
🔹
ترامپ قصد دارد پس از انتخابات میان‌دوره‌ای، وزیر جنگ را برکنار کند و مسئولیت جنگ نامحبوب با ایران را به او نسبت دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/698137" target="_blank">📅 18:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698135">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f3530e82a.mp4?token=fCDXzemOxg4a_yLvBHP4T--ziTHV82UJvWAPb47qYqjhZOiMHN8KBuw12lXomeCF7oNvWf7poVAVOJvyJUwmfAldvUFPv_TP8ettXf6i0IVDBSwEdU9Ahg2geOTvGqebA-bkMOCaFdHy8QyrKLeVUOJm8CyEWnT9aohMdtdDg5nhd0FWcwbEpyRIT3x65S-3C7fCfrBBwZi0AoVV_MSQzPDTZcEK-JesOXJJxRztEz6FTgctwPrjO96HaRUEhPeUg9weEiesUyOiPzw5eZf7fGuDILtArKpmhsp5aYDyQO0HOQAPeILAjM7HwVYOaTvaGWy-9JOyu0xHdwEr5ovUWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f3530e82a.mp4?token=fCDXzemOxg4a_yLvBHP4T--ziTHV82UJvWAPb47qYqjhZOiMHN8KBuw12lXomeCF7oNvWf7poVAVOJvyJUwmfAldvUFPv_TP8ettXf6i0IVDBSwEdU9Ahg2geOTvGqebA-bkMOCaFdHy8QyrKLeVUOJm8CyEWnT9aohMdtdDg5nhd0FWcwbEpyRIT3x65S-3C7fCfrBBwZi0AoVV_MSQzPDTZcEK-JesOXJJxRztEz6FTgctwPrjO96HaRUEhPeUg9weEiesUyOiPzw5eZf7fGuDILtArKpmhsp5aYDyQO0HOQAPeILAjM7HwVYOaTvaGWy-9JOyu0xHdwEr5ovUWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
می‌دونستی آمریکایی‌ها به دلار نمی‌گن دلار؛ پس چی می‌گن؟ #زبان_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/698135" target="_blank">📅 18:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698134">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون بودجه: محاسبات، تورمی بالاتر از ۴۰ درصد را نشان می‌دهد
بیت‌اله عبداللهی، عضو کمیسیون برنامه و بودجه در
#گفتگو
با خبرفوری:
🔹
افزایش اعتبار کالابرگ می‌تواند بخشی از فشار اقتصادی خانوارها را کاهش دهد، اما در شرایط تورمی، افزایش مبلغ آن لزوما به بهبود  قدرت خرید مردم منجر نمی‌شود.
🔹
برای اثربخشی بیشتر حمایت‌های معیشتی، دولت باید در کنار افزایش اعتبار کالابرگ، کنترل تورم و سامان‌دهی وضعیت تولید و اقتصاد را نیز در دستور کار قرار دهد.
🔹
تورم ۴۰ درصد اعلام شده، اما باتوجه به محاسبات، بالای ۴۰ درصد است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/698134" target="_blank">📅 18:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698133">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f241bb3668.mp4?token=W7YH-BNJ8ZRbkmuBdZ21S1T8NjOUqsWgGvnMbo-_vZkyDn9VBxiYPcZlz0OLsO2_iQ17rL_GS5W02ldD6ASkoOpYCnHmweJ3GcqTwZG6xQmb6LyLCxXNn3fLvBll09YUYbiz1ZGJSrsGhUMmrQnHGJAzVPLKIKQidq6XAG0k-uW77JE_OflLMgkqy--FIvTtOFVVzKr9ryNcY3c9pHGd9fVfG0vF_N2pUy3h2wRrdfZVOaSVIgT62S2rMKJ2elsNEraPzntGN_PC_aZJYkJjUIzBZfUnWQkkYV6Eq9nm23FSOG7P5AuK8cY6oHQPxSvYETw2LRRyeU2E2ik3k_8_AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f241bb3668.mp4?token=W7YH-BNJ8ZRbkmuBdZ21S1T8NjOUqsWgGvnMbo-_vZkyDn9VBxiYPcZlz0OLsO2_iQ17rL_GS5W02ldD6ASkoOpYCnHmweJ3GcqTwZG6xQmb6LyLCxXNn3fLvBll09YUYbiz1ZGJSrsGhUMmrQnHGJAzVPLKIKQidq6XAG0k-uW77JE_OflLMgkqy--FIvTtOFVVzKr9ryNcY3c9pHGd9fVfG0vF_N2pUy3h2wRrdfZVOaSVIgT62S2rMKJ2elsNEraPzntGN_PC_aZJYkJjUIzBZfUnWQkkYV6Eq9nm23FSOG7P5AuK8cY6oHQPxSvYETw2LRRyeU2E2ik3k_8_AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کمبود سوخت در جزیره بالی اندونزی؛ صف‌های طولانی مقابل جایگاه‌های سوخت‌گیری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/698133" target="_blank">📅 18:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698132">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
معاملات شبانه تتر متوقف شد
🔹
صرافی های رمز ارز معاملات تتر را از ساعت ۲۱ هر شب تا ۹ صبح روز بعد متوقف کردند./ تسنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/698132" target="_blank">📅 18:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698131">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d60bae218.mp4?token=XNbh61KloVJKDpGZD6ixWmyKeqs1NyY6bJIO7sjSiQf7yIwXrb92-VCLqr4Pt790QILC3f6HO2KQdAlcNUxwBu9waQUR4Qv695NQYiE-Bok-4u7zH2ktbn-KKe54CWMhafA78v6frO2VzWEzaVsFKPaVoFts735qf4Qs7WbSwzORkeHOJ9Tq-S67iddPRSIzX55YujTuFT57Vz_-g9HfK4k3JW59bpbpoVw87eVReCATNCSWH6zZh0ilbuVvmqDSMejbZrWQszM1QY3FBwvYo-jlXuei81xgyFBZD37A4BpiMXKGtmAV7hmX8AZBSUldmaHsgrJPsPvmvN8cWiDONA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d60bae218.mp4?token=XNbh61KloVJKDpGZD6ixWmyKeqs1NyY6bJIO7sjSiQf7yIwXrb92-VCLqr4Pt790QILC3f6HO2KQdAlcNUxwBu9waQUR4Qv695NQYiE-Bok-4u7zH2ktbn-KKe54CWMhafA78v6frO2VzWEzaVsFKPaVoFts735qf4Qs7WbSwzORkeHOJ9Tq-S67iddPRSIzX55YujTuFT57Vz_-g9HfK4k3JW59bpbpoVw87eVReCATNCSWH6zZh0ilbuVvmqDSMejbZrWQszM1QY3FBwvYo-jlXuei81xgyFBZD37A4BpiMXKGtmAV7hmX8AZBSUldmaHsgrJPsPvmvN8cWiDONA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۴ کد مخفی موبایل رو که هر کسی باید بدونه
📱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/698131" target="_blank">📅 18:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698130">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd2e3d250.mp4?token=Uxlmbvw-TEnGh4KVIi1S0TTkVVRFluY11w9L1C9wB3mMSUHk7Lgw2ToAOyufnp4StkE5EoVB_Ry9nPtyaKh9BpX7ZT4p3yXRDd2bbgk-n5mYec123s0w10x2swXcLZWSY5MnUX9wsdxoewDXRZKcnhy6WZFkij4GGNL-N6OhlaR78EmFzR6yiGHHR6YKwrByWoChE1oj2LbeEAty3J5RZB3YEOWXH9AGCR_G6rCmlohofcFQRWoQDdf8Q26vr89YjGclbSNGLM2uAF35XJi9gYVteMGoBlaiVGbzD-_CSDiWL4Fgr84GfY2Wc7s90wgbgP37x3alGPSbT3QxOQ-iUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd2e3d250.mp4?token=Uxlmbvw-TEnGh4KVIi1S0TTkVVRFluY11w9L1C9wB3mMSUHk7Lgw2ToAOyufnp4StkE5EoVB_Ry9nPtyaKh9BpX7ZT4p3yXRDd2bbgk-n5mYec123s0w10x2swXcLZWSY5MnUX9wsdxoewDXRZKcnhy6WZFkij4GGNL-N6OhlaR78EmFzR6yiGHHR6YKwrByWoChE1oj2LbeEAty3J5RZB3YEOWXH9AGCR_G6rCmlohofcFQRWoQDdf8Q26vr89YjGclbSNGLM2uAF35XJi9gYVteMGoBlaiVGbzD-_CSDiWL4Fgr84GfY2Wc7s90wgbgP37x3alGPSbT3QxOQ-iUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترسناک‌ترین جاده ایران
🔹
اینجا یکی از ترسناک‌ترین جاده‌های ایران است؛ جاده‌ای که وسط کویر لوت کشیده شده!
😳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/698130" target="_blank">📅 18:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698129">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اسقاط خودروهای فرسوده نزدیک ۳ برابر شد
محمدصادق حاتمی، مدیر ستاد نوسازی و اسقاط ناوگان در
#گفتگو
با خبرفوری:
🔹
در مردادماه حدود ۱۱ هزار و در شهریورماه ۲۸ هزار دستگاه خودرو اسقاط شد، به‌طوری‌ که آمار شهریورماه با وجود کاهش بیش از ۳۶ درصدی تولید خودرو رکورد ۲۰ ماه گذشته را ثبت کرد.
🔹
در صورت تداوم روند فعلی، امکان اسقاط بیش از ۲۵۰ هزار دستگاه در سال جاری وجود دارد، با تولید و عرضه سالانه حداقل یک میلیون و ۷۰۰ هزار دستگاه خودرو و موتورسیکلت، می‌توان به تحقق هدف اسقاط ۵۰۰ هزار دستگاه در سال آینده امیدوار بود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/698129" target="_blank">📅 18:07 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698128">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
براساس اعلام منابع عربی فردی مسلح به فرودگاه رامون اسرائیل یورش برد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/698128" target="_blank">📅 18:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698127">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62841d418b.mp4?token=VnNW3H-hQMRm995roulSbc-orN7VMf_4aZ-jnX8WxZBdlIx1bfdhAO_XlHxuCxNatxqT4xsDyqoRbmL5LDkf2lcUoThyAE1s7tF5m8-A0Hi48Ni9hjjh1tykJaJy_He7f-1VTOI6vMvE-r5oz28ow8ftVF-l_VddS8AOMStkOHaNliaXuFmTpb7MVFwLtc8DO4DD7_OgqwXecXDjGS11EdKC1Cg0pZMvf5UNwCSJsBQ9fV4ym-hRYA-ALf7l38UP0Kpl4_OWafG2DZgg4rCgz5TA8osD8zTKCWDzTgMt9RO8et-rPqNbRC3lMbIR_vxLtr82QMNcABh2ZzPSMBaBkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62841d418b.mp4?token=VnNW3H-hQMRm995roulSbc-orN7VMf_4aZ-jnX8WxZBdlIx1bfdhAO_XlHxuCxNatxqT4xsDyqoRbmL5LDkf2lcUoThyAE1s7tF5m8-A0Hi48Ni9hjjh1tykJaJy_He7f-1VTOI6vMvE-r5oz28ow8ftVF-l_VddS8AOMStkOHaNliaXuFmTpb7MVFwLtc8DO4DD7_OgqwXecXDjGS11EdKC1Cg0pZMvf5UNwCSJsBQ9fV4ym-hRYA-ALf7l38UP0Kpl4_OWafG2DZgg4rCgz5TA8osD8zTKCWDzTgMt9RO8et-rPqNbRC3lMbIR_vxLtr82QMNcABh2ZzPSMBaBkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه کنجکاوید بدونید مدادرنگی در کارخونه چطوری تولید میشه
✏️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/698127" target="_blank">📅 18:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698126">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYBf-EAFx-hF_DDPyYRZNQMKaWSBEAFqa_-4OpgbWyGK-diYWrYwPFz9PVYPXlmm_Fw9SiOm-llNwDobekcC1HEe2qw9w-mToLbxAJsrOHNz5v8UWY463Ti8WyWJnQDeFuczRLJTt26EU3eX3esE3xLsxzOc2Oc5jb4GCJXbj0guoADdQEv1zeo1zeWlmIxSOFbFXG3gXauqH2APbmieVW3jUjp82IVWk1hCfZ1OqRplfgG9fvGsWW99IYshtxhv-SpiLiVgF92x7tcJkiXG3m6ZZ64-iM8Dmasizpfi9EQduWT-XdksNseyY4Hy0OUDfuZzLD3-K1ope2U5akrOxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔷
ساده‌ترین راه اتصال فروشگاهت به اسنپ!
📱
با خرید کارتخوان هوشمند اسنپ در ۴ قسط، فروشت رو بیشتر کن!
🧮
سوپرپوز اسنپ‌بارکد یه کارتخوان اندروید همه‌کاره‌ست که تمام قابلیت‌های یه صندوق فروشگاهی رو هم داره؛ به‌علاوه این موارد:
🔹
پرداخت اعتباری با اسنپ‌پی و تارا
🔹
اتصال به اسنپ‌باکس برای ارسال سفارش
🔹
باشگاه مشتریان و ذخیره شماره و آدرس مشتری
🔻
دریافت مشاوره رایگان و خرید در ۴ قسط:
https://forms.gle/77f3J2oCbVsDkdqi7</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/698126" target="_blank">📅 18:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698125">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c128d83f9a.mp4?token=BLN2KC_OHyBBmhSx4hWumXEa39yeztrLcdPAXpuVMCYvkXXeuAOlQeLZAr6eqdoand7a8i18DAvSoci-LzOBQcvKLTuQ23_Nbx1ZLKKMrum6L65syitY4rFxhZBuAFyA1laRNUBDWg9VNthsQG9B-y09CkN2ckTEFW7baFvZzSUjwL3u_qP3FtKixWP2uGuJ_3xnHNvmckhZaAf-ls0rxZUvM2SGmqr7EwZKPsV2xpadXuHAaY72PAywhyMIIJ5JZDhP990hczj6CUCzzNE0MyLamsSaCfD0c5_-YKfUHsENHcVRxPg5L6SG4eV_aIfgMc6ItfKZAqVfhUZQSWnpNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c128d83f9a.mp4?token=BLN2KC_OHyBBmhSx4hWumXEa39yeztrLcdPAXpuVMCYvkXXeuAOlQeLZAr6eqdoand7a8i18DAvSoci-LzOBQcvKLTuQ23_Nbx1ZLKKMrum6L65syitY4rFxhZBuAFyA1laRNUBDWg9VNthsQG9B-y09CkN2ckTEFW7baFvZzSUjwL3u_qP3FtKixWP2uGuJ_3xnHNvmckhZaAf-ls0rxZUvM2SGmqr7EwZKPsV2xpadXuHAaY72PAywhyMIIJ5JZDhP990hczj6CUCzzNE0MyLamsSaCfD0c5_-YKfUHsENHcVRxPg5L6SG4eV_aIfgMc6ItfKZAqVfhUZQSWnpNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درمان ریزش مو در کوتاهترین زمان
کشف شرکت دانش بنیان ایرانی در آنتن زنده شبکه ســـه ســیــمــا!!
😳
😳
ویدیو داخل لینک را حتما مشاهده کنید تا با تاثیرات عجیب این روش درمانی آشنا شوید
👨‍⚕
👨🏻
✨
🩺
بـیـش از ۳۰هـــزار خـانم و آقـا از این روش معجزه‌_آسا نتیجـه گرفتن
😍
روی لینک زیر کلیک کنید
😃
👇
https://www.20landing.com/214/2623
https://www.20landing.com/214/2623</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/698125" target="_blank">📅 18:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698124">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iin1VzJL2OW51EoJPpTGzvn8yK5lBM6LNMEkuHTcpSmtdGyo98MGrJBtMh69TvFaIMm_5LAJzhnAbo9ube976CtgznM-Mr8NZOFTJN6cTr-URnvjCbaBphqqAbFwo4_eHOmT6LRndov8YyMfvwS0Nxi4ni7EH7cXbzbcf63BIsJEFmHkuXLV_U6przZCqaj_fNgJvGJ9Pi-fFjvNi687WsAVYxuFtWoWW6s6IM-_5K7kWORsJFPyekW5nnGwiAtvcU_uXyUGXEqSZreithdsPwa0iTXW6udV77evuPDyafwteDPlegxXzorpnv7EXbk5WupHlWJwNBmeveHgTqdurQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت ایران بیش از ۲۴ دلار گران شد
🔹
جدیدترین آمار دبیرخانه سازمان کشورهای صادرکننده نفت خام نشان می‌دهد که نفت سنگین ایران در سپتامبر (شهریور ماه) ۱۰۵.۸۴ دلار به ازای هر بشکه فروخته شده است.
🔹
این رقم نسبت به ماه پیش از آن یعنی آگوست ۲۴.۵۹ دلار گران‌تر شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/698124" target="_blank">📅 17:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698123">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
یحیی سریع: شرکت نفتِ منطقه صباحۀ صنعا از فرآورده‌های نفتی خالی است و هدف‌قرار‌دادن آن هیچ ارزش نظامی نداشت، ولی ما به زودی پاسخ این تجاوز را خواهیم داد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/698123" target="_blank">📅 17:44 · 21 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
