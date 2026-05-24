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
<img src="https://cdn4.telesco.pe/file/bdiIB1ufgds_E3tQk2lgIldjwrghyjnbu8VHMsHfO90aRfeGHMD78K1QwVAQdHyE15gIgA06awTCG08tFtHFacIggDVfS_ywEF7P_2gnhLHn2wEauSHUSxG-xGOsiXSQFJaRFliJOQLv4eyETUiPIPP-MbE3KHDsGBo6s8MpRroxOHMPO5RYSr1ZLj_aonFHwdRY6SNR02MGD8tmiSbdvgKrZsNU45rwFXAlL8-P0jEJWibaATh5U1FffdIvzVGbWHHmdYHKfvpQUOQCgiAGBjRxSHjWkEMRyokzky0bBf1sYlGj4pSHw4e-PyZ65qt4eO7QO4J-4dmzspcv5s379A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 938K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 22:34:12</div>
<hr>

<div class="tg-post" id="msg-122414">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
رسانه‌های داخلی: آمریکا مانع آزادسازی پول‌های مسدود شدست، احتمال لغو کلی توافق وجود داره!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/alonews/122414" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122413">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0235b6f6f6.mp4?token=EpEMgMvIhHX4N775FmaRL_8wsQqsTANEU8JkKPgh7R6I8ZLwa3E0rY0-b8JMF5nxoyW26bO0Dx7196p97tk3oiZbDfujQa3CRe1jRaAFfzZZVN5B2fg_tHOZwoJJyFEgUvq3C7ZAgW2z9Yv50_pJhxR_CcLi8DjCIoGyPZ1-76Cb_F5do8MOFvvLzz-rnPNudwtZ5mrZJascXoaG42QCdXOhnERd04XCjEogHmD1CAVGJzkecczfUm0Ac_sU4wftSZyKCxaPx5TST2wYTiigqZjG1OxZG94pD4rOJQu8h1Zhn1V9ltL0uAzpdncCGgzmXyxE_WElLOaHHYdoJW_0UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0235b6f6f6.mp4?token=EpEMgMvIhHX4N775FmaRL_8wsQqsTANEU8JkKPgh7R6I8ZLwa3E0rY0-b8JMF5nxoyW26bO0Dx7196p97tk3oiZbDfujQa3CRe1jRaAFfzZZVN5B2fg_tHOZwoJJyFEgUvq3C7ZAgW2z9Yv50_pJhxR_CcLi8DjCIoGyPZ1-76Cb_F5do8MOFvvLzz-rnPNudwtZ5mrZJascXoaG42QCdXOhnERd04XCjEogHmD1CAVGJzkecczfUm0Ac_sU4wftSZyKCxaPx5TST2wYTiigqZjG1OxZG94pD4rOJQu8h1Zhn1V9ltL0uAzpdncCGgzmXyxE_WElLOaHHYdoJW_0UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون هماهنگ کننده‌ی فرمانده‌ی ارتش : نمیدونم توافق چی هست، سر چی هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/alonews/122413" target="_blank">📅 22:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122412">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
منبع آمریکایی به الحدث درباره لبنان: توافق آمریکا و ایران شامل همان بندهای ۱۵ مه مربوط به آتش‌بس است.
🔴
پیش‌نویس توافق آمریکا و ایران شامل تعهد به پایان دادن به خصومت‌ها در لبنان است.
🔴
اسرائیل به واشنگتن اعلام کرده که هر توافقی با تهران باید آزادی عمل آن را در لبنان تضمین کند.
🔴
پیش‌نویس توافق بین واشنگتن و تهران شامل خلع سلاح «حزب‌الله» در لبنان نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/alonews/122412" target="_blank">📅 22:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122411">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ادعای منبع آمریکایی به الحدث: مخالفت‌های درونی در حزب جمهوری‌خواه با برخی بندهای توافق با ایران، اعلام رسمی آمریکا را به تأخیر انداخته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/alonews/122411" target="_blank">📅 22:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122410">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
وزیر امور خارجه ایالات متحده مارکو روبیو گفت که توافق احتمالی با ایران حمایت منطقه‌ای دریافت کرده است، اما هشدار داد که یک توافق هسته‌ای نمی‌تواند «در ۷۲ ساعت روی پشت یک دستمال کاغذی» به دست آید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/alonews/122410" target="_blank">📅 22:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122409">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از مقامات آمریکایی: محاصره دریایی بنادر ایران امروز با سرعت بیشتری ادامه یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/alonews/122409" target="_blank">📅 21:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122408">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ترامپ: اگر با ایران معامله‌ای انجام دهم، معامله‌ای خوب و درست خواهد بود، نه مانند معامله‌ای که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و مسیری واضح و باز به سمت سلاح هسته‌ای داد. معامله ما دقیقاً برعکس است، اما هنوز کسی آن را ندیده یا نمی‌داند چیست. حتی هنوز به طور کامل مذاکره هم نشده است.
🔴
پس به بازنده‌هایی که از چیزی که هیچ نمی‌دانند انتقاد می‌کنند، گوش ندهید. برخلاف کسانی که قبل از من بودند و باید این مشکل را سال‌ها پیش حل می‌کردند، من معامله‌های بد انجام نمی‌دهم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/alonews/122408" target="_blank">📅 21:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122407">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
نیویورک تایمز: یک مقام آمریکایی می‌گوید ایالات متحده و ایران در اصول برای بازگشایی تنگه هرمز توافق کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/alonews/122407" target="_blank">📅 21:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122406">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f1c8f1a7b.mp4?token=av9QjLaizKB5XfojyOsqMvUnCGVFcqRUPbMHxdKlIvCK4sO71NM9tbUCmnpGQ5pfhGWEryaoeYLJC7KJtU21Mr2MegnGr33Or3LP1akO30mx-eYfYXkpUPDFRj4nc1oZP6roCAtE4G2FuTmfvtTN50UKPLqIsmaF8XvJOLa1Lvm9vSCrxUqkS8_xDW-QAcukvpu2ylcuBgI9HEB9OT_YEanxAjsceLsOMDGXosjgruYnKu0Y37zUmEtV44inxWUrpRXX-Wxp8UVnw6xzL6TfI3OZKR0E0Bg6mGPVYeYj9jcPM8s2GI8ilgdChgoQC_kFA9PJV60ua_06QDcDFxotbSWxLSdQ0oGgcWEKcAjMzkaxezX2BMvyWnwmKyM_-McVLqLZ22fNqkqufoDDLZD1WF0QsVqerZYv6A-2kL-HX8GfdVhJ3VXDP6Rm0psNWQ7KZ0vFAEUl_mq1opk8NwkW4fsY0nolQJ52_SD5W8NZam1fuBxZkqrHAHlTi3dLsccEdGLlNCzjxQPkO6YR1stSs8n_zw7e-dVoHNkTgZydgVKsDWtnaoqqaPh367Sd8lzEyk2yeitktOc3CXjqCjLxmMry9FOCEqXRxo7TXUyx2_igSKsM_LCj6ymvdyYVv3_PGOnY2JXZlemtJHfRL7qSTxIVx2z6YLgamDwESRKK1mM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f1c8f1a7b.mp4?token=av9QjLaizKB5XfojyOsqMvUnCGVFcqRUPbMHxdKlIvCK4sO71NM9tbUCmnpGQ5pfhGWEryaoeYLJC7KJtU21Mr2MegnGr33Or3LP1akO30mx-eYfYXkpUPDFRj4nc1oZP6roCAtE4G2FuTmfvtTN50UKPLqIsmaF8XvJOLa1Lvm9vSCrxUqkS8_xDW-QAcukvpu2ylcuBgI9HEB9OT_YEanxAjsceLsOMDGXosjgruYnKu0Y37zUmEtV44inxWUrpRXX-Wxp8UVnw6xzL6TfI3OZKR0E0Bg6mGPVYeYj9jcPM8s2GI8ilgdChgoQC_kFA9PJV60ua_06QDcDFxotbSWxLSdQ0oGgcWEKcAjMzkaxezX2BMvyWnwmKyM_-McVLqLZ22fNqkqufoDDLZD1WF0QsVqerZYv6A-2kL-HX8GfdVhJ3VXDP6Rm0psNWQ7KZ0vFAEUl_mq1opk8NwkW4fsY0nolQJ52_SD5W8NZam1fuBxZkqrHAHlTi3dLsccEdGLlNCzjxQPkO6YR1stSs8n_zw7e-dVoHNkTgZydgVKsDWtnaoqqaPh367Sd8lzEyk2yeitktOc3CXjqCjLxmMry9FOCEqXRxo7TXUyx2_igSKsM_LCj6ymvdyYVv3_PGOnY2JXZlemtJHfRL7qSTxIVx2z6YLgamDwESRKK1mM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:هند می‌تواند ۱۰۰٪ به من و کشورمان اعتماد کند.
🔴
اگر به کمک نیاز دارند، می‌دانند به کجا تماس بگیرند — همین‌جا تماس می‌گیرند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/alonews/122406" target="_blank">📅 21:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122405">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
العربی الجديد: تلفات انفجار انتحاری در قطار در ایالت بلوچستان بیش از ۶۰ کشته و بیش از ۱۰۰ زخمی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/122405" target="_blank">📅 21:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122404">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBC2WOg6Wh7qpHrhkpMPtowIHPUNrSCOwIfgmCH3aDzRcSEUB1t82VrRxEe-axyuXtN4bHLms3ZKuKLTj8fD1WD0x3PaLXB7NN8gPgXqMWYuV9ICiW__aSWBocizcVkfTnmFIhCw3e-BlPgU0FulTRgKDmmZ_JaZ3MonQeZSfmBbSrw2i0xHxv2Es99-G7BtNwN3XNRNl0u4dpg2q62LiHabRVTKP6nbUR_XVm2AC5JF51dr1405GHeaJbswDAHt9FveW6rgBOdB1Xt3PPOYgsjMNA0QjSp7h36oTiCjhGCamC7EH-O43L8rkWapAcCFiyBife86bs6DBUUZ7KV81Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه وزارت خارجه ایران: در موضوع آزادسازی دارایی‌ها که مورد اختلاف است در حال حاضر راه‌حلی برای آن وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/122404" target="_blank">📅 21:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122403">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ادعای یک مقام ارشد آمریکایی به آکسیوس: «ما در نقطه بسیار خوبی هستیم اما راه‌هایی وجود دارد که توافق می‌تواند تضعیف شود.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/122403" target="_blank">📅 21:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122402">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
اولیانوف: برچیدن برنامه هسته‌ای ایران خلاف ان‌پی‌تی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/122402" target="_blank">📅 21:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122401">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
یه مقام ارشد دیگه هم به Axios گفته :
شرایط خوبه ولی هنوز راه‌هایی هست ممکنه توافق خراب بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/122401" target="_blank">📅 21:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122400">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
عارف: حتی‌الامکان خاموشی نخواهیم داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/122400" target="_blank">📅 21:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122398">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiRQlFYbdEvdDEdVJKk8CM8VHLKmxPvKVi1DTF3EemyE5nPicaQLPrLTD6Rxkve34IlC7gybrurWWK456uqKbNkkMU3CEBRpNIOfqzx7vxHRlWVczlCzGfS5RckgeKW4qxGkM6DodyIn1hv-iiDFjfUliP7X0WY67jeTf0hDwNaarl7j4HNJL9xWgHufQ9i3Wimyf8aMxuQ4TvVWCMFETjHGAr-hYMkl2TeJX8LK-mKKTqH2rFdRJJwKloHpXbiW1u8ic621PZkkkRf3Dm_GhcaRYgyGqPu57nZAq139JqdxTiQIstKJp0038-N5OEuwdNVVY2ZaI4drhvBD0wCCqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
اشتراک v2ray
🗯
گیگی
120,000
تومان
🔗
لینک ساب برا چک کردن مصرف و حجمتون
🔥
سرعت و کیفیت بالا
✅
پشتیبانی دائم
📱
جهت خرید :
@v2safeBot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/122398" target="_blank">📅 21:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122397">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ادعای واشنگتن‌تایمز: آمریکا و ایران پیش‌نویس توافق صلح را ظرف ۲۴ ساعت آینده اعلام می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/122397" target="_blank">📅 20:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122396">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hhc63T9wPyTES98iKGtaXLkhvQu1w6GPjHFwSKJ3I5sTLNXpDRfYdC28ppAQjl_zgxeEBo8JfGIFFu6o07KoJPSFfbgPLPw5t9ijEC5wOf6iuKu90SHpeNhLpW-UjZU-R6R9Xh_jQtFUlHbwC3PfjQ43KN5Is3I7aJCwETbWDwI6s3cU-G4uXKT9ZUUH6tqH5seH1Trui-cKa9MJq_Jw6sBvkOdZhOq6GRRMqffEbwD_8Vl1wtuc3VbKIA49Ln6zLlvWAD8HmgAH6cM79JKKf35-eHyzw7iNOMw0eoN0kzhmmezu6mwR8GcJmyiPBwev6iFYLXPWbS_ybHE50ZRJzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۰۳.۵۴ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/122396" target="_blank">📅 20:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122395">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل هم اختلافات بین ایران و آمریکا رو تایید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/122395" target="_blank">📅 20:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122394">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
فاکس نیوز نقاط اختلاف در توافق ایران و آمریکا را اعلام کرد:
🔴
1. اسرائیل خواستار تضمین «آزادی عمل نظامی» علیه تهدیدها در لبنان است و ایران این را رد می‌کند.
🔴
2. تهران خواستار آزادسازی فوری دارایی‌های خود است و واشنگتن امتناع می‌کند و اصرار دارد که این موضوع به فرمول نهایی توافق مرتبط شود.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/122394" target="_blank">📅 20:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122393">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
پسر ترامپ: پدرم بهم قول داده نزاره ایران به سلاح هسته‌ای برسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/122393" target="_blank">📅 20:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122392">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHAm5M24S9wgKqu4yrczy9ILq5ezrmLZX8-3hyRBD0b4VPzYT_pMxHGWbzh-b9hMYxiWAh9_J74IZAq2r-aAFxpSYsFY8shxU_3C8dbYRVFzsDb-AjKc1A4NmFb-LeSAeag-JyF6V6gWUmNdQ73sC0Clwk3lB6Tgont1AiZJEqa0AM0VDnAEoZt-nTL2ZlpjA9NfFrDnFSt-1yDP_-ae7y4gvXfwHPlF3pgwbC3ys2u_bQZMnAOI5ZUk_JW3SOdAk3v0S2P5x9Q-wyOzTFclh1tt5x0rIBm4RemumkEuZVmN9_8LxKMKiU9rfLLGk-vqdTnMFuNEctHhMZnI8xjwnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جوزالم پست: ایران در اصل با یک توافق آتش‌بس با ایالات متحده موافقت کرده است که بر اساس آن، اورانیوم بسیار غنی‌شده خود را از بین خواهد برد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/122392" target="_blank">📅 20:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122391">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
خبرنگار الجزیره: حملات هوایی اسرائیل شهرهای شرقیه، کوثریات الروز و زوتر الشرقیه در جنوب لبنان را هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/122391" target="_blank">📅 20:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122390">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
تسنیم: علیرغم برخی گفتگوهای امروز، کارشکنی‌ های آمریکا در برخی بندهای تفاهم از جمله موضوع آزادسازی اموال بلوکه شده ایران همچنان ادامه دارد و تا این لحظه این موضوعات حل نشده است.
🔴
بر این اساس، در حال حاضر همچنان امکان منتفی شدن تفاهم وجود دارد و ایران تاکید کرده است که از خطوط قرمز خود برای احقاق حقوق مردم کوتاه نخواهد آمد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/122390" target="_blank">📅 20:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122389">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوری / علی هاشم خبرنگار الجزیره: کمتر از ۲۴ ساعت پس از ظهور خوش‌بینی در مورد امکان توافق‌نامه ایران و آمریکا، حال‌وهوای منفی دوباره سر برآورده است.
🔴
منبعی آگاه ایرانی به من می‌گوید که نشانه‌هایی از عقب‌نشینی آمریکا در دو مسئله مرکزی وجود دارد: مکانیسم برای از یخ‌زدگی خارج کردن دارایی‌های ایرانی و دامنه آتش‌بس در لبنان.
🔴
بر اساس گفته‌های این منبع، توافق‌نامه شامل چارچوبی برای آتش‌بس در لبنان است، اما گزارش شده است که اسرائیل با این چیدمان راحت نیست و واشنگتن را تحت فشار قرار می‌دهد تا بندی را اضافه کند که به آن اجازه دهد تحت توجیه پاسخ به «هرگونه تهدید»، عملیات نظامی در لبنان انجام دهد.
🔴
ایران این فرمول‌بندی را رد کرده و بر یک آتش‌بس پایدار و ماندگار اصرار دارد.
🔴
تهران به تمام میانجی‌گران، از جمله پاکستان، اطلاع داده است که تا زمانی که تمام بندها به طور کامل توافق و تضمین نشوند، توافق‌نامه را امضا نخواهد کرد.
🔴
گزارش شده است که پاکستان پیشنهاد داده است با بخش‌های توافق‌شده پیش بروند و نقاط اختلاف را به تعویق بیندازند، اما ایران این رویکرد را رد کرده و اصرار دارد که بندهای مورد اختلاف بنیادین و غیرقابل مذاکره هستند.
🔴
تصویر کلی نشان می‌دهد که تهران فزاینده‌تر واشنگتن را در حال عقب‌نشینی از تفاهم‌های قبلی که از طریق میانجی‌گران حاصل شده بود، می‌بیند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/122389" target="_blank">📅 20:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122388">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
رئیس ستاد کل ارتش اسرائیل:
ما آماده‌ایم که فوراً به نبرد با ایران بازگردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/122388" target="_blank">📅 20:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122387">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
طبق گزارش فاکس نیوز، ترامپ می‌خواهد توافق پیشنهادی توسط مذاکره‌کنندگان او، از جمله استیو ویتکوف و جرد کوشنر، اجرا شود؛ اگر این شرایط برآورده نشوند، هیچ توافقی صورت نخواهد گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/122387" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122385">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
تسنیم: کارشکنی آمریکا در برخی بندهای تفاهم تا این لحظه ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/122385" target="_blank">📅 19:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122381">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tHjJU87iSQ8jbN5TDQM1C3YX1I0CEB7Z30boDV0d6THlOXn9eSPeEBLy-UaVOSAen8f51St9dSllHx5x0jm9Knoo3_KGwST3M-DCONXZv6GhfFmj1Wy7-xq2LrPra1Ewljw8l5GUdS-0mAZL5DqjJXhWkMvQxOey8vDIz7mtflv1GKEVDk8oVQ0-GFHPRqPn9hOulK3ImQi1-0CXtgoqcxgh_SflavqWkIoffT6MSpPeIirF7mTpGQ5dD-O2rcE2Smf6CF_q01UzHRestGvnYk5brz9MRdev0dmvDT4xTZMMMGFtuth_sGTpq1s2FBF1Vo0dw7ODroB5TfwRnL72Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGpgu79X6brJR8E1zlIBRZimp-sibkO1fBZrvPukNN3XbiqFXqKu4xPO9LjNXM1UTFq03h0HDbty2B6XtDPDRD3h79I-tEK4OEJDwJiaca0aT7WT_3NAIfgixqoAgPFQubq9Mvplf68HNiKV5Fzu8Zf22tG_II1nz6uMJJ4tJNDzAGEje3LqQGIBYOB-EokJ2Cv6e2gfv-Fl_UG9H2syraPuVRjNn3AroOcyqBJX3ZXGg_odjN8Er8PnN-LignxA5KQ_FO7Oi0I0l-IbVtvY6lDKdtuYjzo6M_KCoNdsUb6GS1aYCB9KZb_ine5aUPrl9smeYTWSXxBc_Dq7m6Tp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uy3IRo5ny16N-p3xGurLZysDppMOHUaNHSSs2t82oWVSTJsW2AGllD_jpFHIhR4NNW00UpH3lXlgsYUE-Wulk_acIDDb7eTq02h3JU1tqan08SRry2zZoMYuLEcmMQg5w9e0ZO2XDq_ydMcdod7RhkvydMlE1vjoB8Q1SfOS2vGPVX6VZ9h1Q35NAgHQTqbff8OaJuFvLxbbR-LLe5K0P1lZV9UPRh024qXRll3Gtz2fGkZ-W7qcWTWh8DwSxc6vIrkjmhTslPCv5BMKeHE1k2jOs2pLt9f3JxD378Dt78_OgQCwK8_UP7yMg-xRabDllHCp2SRnPc6LRU8dgFUbBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b49bac95.mp4?token=rZWeTafMnOTV7AL3SfliEZ1bmedy0trarRwoEbEUV2fIE2KhuJeELFan53SyFFNDv3-s40racCfEiPagEakSgLTM1CjQy0XxVx1R1m4viSJY-qyvefKlBlf7DiG-W4EXtQnqSEvkXqvhoNyCnYVo5MXs78a2K1FP2yS85-p3bp-3tmdLCJCyiCWAhumtgWMqcuAG-olHFmvsHRx3Zceeoydnr5PACaZx6gzO-kncCy0bSD_cw41tVGGoFOA2fyJ2_3iSGyrSZ0vc_zQOAsWMoqaEfoJK2gkivEp7rbhTzxwgfzn1qRyUdzdhGyqhYBMemrlseZgzdXAjDpIaVdUmtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b49bac95.mp4?token=rZWeTafMnOTV7AL3SfliEZ1bmedy0trarRwoEbEUV2fIE2KhuJeELFan53SyFFNDv3-s40racCfEiPagEakSgLTM1CjQy0XxVx1R1m4viSJY-qyvefKlBlf7DiG-W4EXtQnqSEvkXqvhoNyCnYVo5MXs78a2K1FP2yS85-p3bp-3tmdLCJCyiCWAhumtgWMqcuAG-olHFmvsHRx3Zceeoydnr5PACaZx6gzO-kncCy0bSD_cw41tVGGoFOA2fyJ2_3iSGyrSZ0vc_zQOAsWMoqaEfoJK2gkivEp7rbhTzxwgfzn1qRyUdzdhGyqhYBMemrlseZgzdXAjDpIaVdUmtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی به زراریه، سومور (دره البقاع)، كفرسیر و سر الغربیّه در لبنان حمله کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/122381" target="_blank">📅 19:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122380">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
دبیرکل حزب‌الله: خلع سلاح را نمی پذیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/122380" target="_blank">📅 19:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122379">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
سی‌بی‌اس نیوز: موضوعاتی نظیر ذخایر موشکی ایران و غنی‌سازی اورانیوم در مذاکرات آتی مورد بررسی قرار خواهد گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/122379" target="_blank">📅 19:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122378">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
یک مقام آمریکایی به اکسیوس گفت: برخی از جزئیات توافق با ایران هنوز نهایی نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/122378" target="_blank">📅 19:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122377">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از یک مقام آمریکایی: مسائلی مانند ذخایر موشکی ایران و غنی سازی اورانیوم در مذاکرات بعدی مورد بحث قرار خواهد گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/122377" target="_blank">📅 19:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122376">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
منابع به المیادین: ابتکار چین، تنگه هرمز را از نقطه تنش و اختلاف به نقطه‌ای برای توافق و حل‌وفصل به سود همه طرف‌ها تبدیل می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122376" target="_blank">📅 19:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122375">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
یک منبع اسرائیلی به سی‌بی‌اس گفته که به واشنگتن اعلام کرده‌اند حتی در صورت توافق با ایران، آزادی عملشان در جبهه‌هایی مثل لبنان باید حفظ شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/122375" target="_blank">📅 19:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122373">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AXwZ-ztoNig0CQX7iGtlABxvMYP15XsAFmPz9lTkCWH8DE5AW_RwP5JOCkj09TKPcmV9Z5qTnzeQEMzWH92Haa4i3pE9OxwkqW2BEW34tfudILlQIyMBqt96-zBAo09mzBumoiaiuLsQIP-hbNGhKS5l6aICP-Zvd4fyudeN9TFlsO4LkawDyOzSQB2Ab30qcDZYoMTQPWDPS1q-Od_sc96P-hJhRzyTRfdTRra1Wdw9598o8RD3jM-lpYTnKTayJSnL_cIEDmD_pecGfRlPZVjxN5ijP_8yqSQa1CcUOkE7fuYmlOgstIL4US3eVwmkI1cHVpgZFFcukpOSmF0pYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JvR8QY0Kja4N5wyM2iuY5xRXurzoT2Oo5GOhWNgW2h3SBP5zEAjkgsNpxf4O2cH2s9IvdJyNRioJRAnVke93tYelrJl1Y8Y8e8U29B2Jsw5fCX8ghcnBEMwg1emc9qI1iyxbR5fLXfI-srFYei0OQEmy0VyzgZ4V-aO_2pE5FPIH084QZ3BMJIKMUV5uBw7ZOBLnYo8A3n56DeyW2xtRjTtOv9JK2B11deXK-adDdWLfnlEKyCxTQIrM7N7B2N-2xpNcl6m9I50Z2ADOeZDNiZYYV6MBqxReaAcSTJWliinEwR5DUYIjhlo_6bcxM6Qz9F4OPGqtqJ_WVBzm-6V4xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اسرائیل دقایقی قبل حملات سنگینی در جنوب لبنان انجام داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/122373" target="_blank">📅 19:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122370">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUELXwrRDgx4KGBMfPEPDWkVoZUN2hjso5k62AwnMzsXMijAVoitTyGd6NMWdx0OI6lovWj5kUT6xMy0H_emKscldkik0r58Zhthsz1WVJGxz79Z990RyUcn6KnlFdQU0dmXbIN-b4ynMeBzQXeqmkSqWxnJvQ0FQyD9_vr6LlnmdUkLEQaw9v5VoBdPeapGctJ5d0zpx8gVq2H37JxXFoF9oOBnhf9cwlbf9DK00nfMdjIA8zHIwZzY1vQVhATJe5TC2ygsDfNzKlqnZtqJue2Yo2ew_FnrpPW7FTJbY6etqEd2hoSOs_PLpQiHpFN_l9MncioSfvjON83SgXRJCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSbjfy4kWqfAkLk-R78hYV_eMqShu0Wzez3iph_X8GsvqkHCu64GYm-LquBhJTVlVtoSgKMKwEcOl3fuHTTAk8bZRt3ytTXv9W1lUAE0n-_YwKt-x16hv0OJsC_9KNqMqIGthy8e-pYEJmYJ-GhJw2XTH9RMJUPdxR5_JgaADyLQNb0b0yLF8zGEIQwFjw07tSTEetfkOBliwXfrhY04472_4Pd9WiGa1Ga40W9J1ALpHf63ZU1ZwL9EiXkhPDCx527N9F8dptDvCkB_ZUe4XCKDpLjJOeY91txYUI_WflEGih-gch5LAq21lubWz41V_UnHz23TzYU9WxMzmEZgqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vUQSTO1TGw04YCeUJvA_sJR9RapeGEME-e9YqhW2XkNegTVCarySQ_DGwUzxJfQiUAYWjzR9Vicyba5OStBc6N3VFgCtGNT4ih41o7vI4CCtvPXONm-CL8uC5OK8-jOWQh_tnVurmWV-wBydfd6at8BwaC70E3KIdb5n89lT0tEVWMaTVRZ9nTLdQBqC2kBznuiDF_ZpszXEDLtcqWhC-CRcQ6aHrc-kyUFgjAu4dD3EdAErFJSdf_pwtHMDLmBoW4cePAUCHtzi2cKyyx8jTLsz3W1GUq0EiygFXZ-9GZjhWwTsHa-NGj_uiATvX63e0h8ewOhJrcZnwV1KXuYnww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
معاون بین‌الملل وزارت خارجه: نشست مبسوطی میان هیئت‌های عمانی و ایرانی برای بررسی مجموعه‌ای از اصول حاکم بر عبور شناورها در تنگه هرمز با رعایت امنیت و حاکمیت ملی دولت‌های ساحلی این‌ تنگه و در پرتو قواعد قابل اعمال حقوق بین‌الملل برگزار شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/122370" target="_blank">📅 19:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122369">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuwWxfpqQ8svxLISH-ra-m_1IJfwV2cuy3DaM03ZhOXiMEsDTyFAQAe36wuetdngwoswczYfeKp6NYShzT3IjAJ-WCXPF3aisRpGnEWlj1Tcrtac74HZVuX10ZqgdskvfBjenR64OqgiBd9k4lmX4Hl6VqzYadXK52BWMJ-VLyomD_Qy2Wu-U1fSrXXEPJ5io8i2nt9laOb-5bgiqkdBCSpiH8QCpxHRVXQI2MAsIZR5RuL1Iiq2_ymUuIiil6EGg85u9vMeVzoIfymR-YccJ6SxCPSc90ROvGNNKX1P5whsqoHWzsttHoPeSS4ED95flmbOpRuUL2WpxbD0BAJJYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: توافق ایالات متحده و ایران برای بازگشایی تنگه هرمز امیدوار کننده است، اما کشتیران‌ها همچنان محتاط هستند و بازسازی تأسیسات تولیدی و ذخایر زمان‌بر خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/122369" target="_blank">📅 19:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122368">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gz_VuoYm9cpuItyp2VuuA61AI4Usas6agg7oY-3m1iDHNNr1krnP-l50iKfqWvl4fFL2yT7kbruk_s5XJxRcUbwPppHAYst__mdDvHbtT9ZhgjSJ3eNHU7epDkaAIxhruu3xg6zJRGUGxDQf0epUhoHDAp90gpM85fKjtfAXEjXXBow8PMwlARcZyRNSnoflXpphA03IW-xEFr7LLT1gxBvuL-ouQWadKiP2u2NfaCkUDhutNn-IaQ17EW3VJPmYztl_x76JMuUb8R5YKwxfiz9F7xBNiTEOjb20Pwa7nhVKkrwd8pBuUMGzINt8-jbGqvQT5vGigs0F4ge6RsmaMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو: توافق نهایی با ایران به معنای برچیدن تأسیسات غنی‌سازی هسته‌ای و حذف مواد هسته‌ای غنی‌شده است.
🔴
توییت جدید نتانیاهو: من و رئیس جمهور ترامپ توافق کردیم که هرگونه توافق نهایی با ایران باید خطر هسته‌ای را از بین ببرد.
🔴
این به معنای برچیدن سایت‌های غنی‌سازی هسته‌ای ایران و خارج کردن مواد هسته‌ای غنی‌شده از خاک آن است.
🔴
رئیس جمهور ترامپ همچنین بر حق اسرائیل برای دفاع از خود در برابر تهدیدات در هر جبهه‌ای، از جمله لبنان، تأکید کرد.
🔴
مشارکت بین ما و دو کشورمان در میدان نبرد ثابت شده و هرگز قوی‌تر از این نبوده است.
🔴
سیاست من، مانند سیاست رئیس جمهور ترامپ، بدون تغییر باقی می‌ماند: ایران سلاح هسته‌ای نخواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/122368" target="_blank">📅 19:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122367">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuTdYZM2uqCJWNxCMXy5vVSOL-KJezJVHtLyiYVZ6YA3ufxN2nDoOvBCWFeuuEy11ySk_jn4IYGrmluA2x7o36eqMx5-7mrgqU25tpI5S3VaBklOaVbFLb73cGXI-6XAmGkmuPFDNGC4_zDEloo0RLxy2pedIqWM-sGjHmBt6ohm8x_4oyo_GtdtOy672VlHfUL5zM_weTZSc-n9vuqYvxObNNhBSGhle-8J9chvyPPC5w5QtWHva2lKs0kQkgn2UEpmqUffQyPjnjpRXdHMhpSp0YBPnHgWSpDIgCn80O0yyC5EI5mVLcxxVaj6ViWZX9HDEi62IXxfik7LwtpR3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ سخنان پزشکیان علیه سلاح‌های هسته‌ای را بازنشر کرد
🔴
پزشکیان درخصوص سلاح هسته ای گفته بود:  ما آماده‌ایم به جهان اطمینان دهیم که به دنبال سلاح هسته‌ای نیستیم. ما به دنبال بی‌ثباتی در منطقه نیستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/122367" target="_blank">📅 18:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122366">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_mnA7MvK1P4vUboiXvVwj_-N7RJ7jAP-6wvHaB19TE68wn9oJOzjEQ5qiZfxl0Kuf2qmRQn7scA8CNaQVHnXsFFdXhAUWy4IwmcIuRHghDUAKeaJ97Slr7Vx9iaE6r-cAnPkwKfkRuoiWI9kwTSAnFcYliyG0YDR14me0HQQIzEAx-HyCIv1lsmAAPQqOqRuE1en7HL5Ax4i69uq0c4vAroA9xIp6eI9RhucG4JNjmjgfQs914xUhd5z23xBmSzBAXqd-cnboB4DczgvluZH8V4REAbNWrs391WX0zeZY_ESTuEVUaNYHR3Z5FquBR_E4eZsh9h2Y2TGvv3ol448w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاکس نیوز: یک مقام ارشد در دولت ترامپ گفته است که توافق با ایران امروز امضا نخواهد شد، اما پیشرفت در مورد یک توافق را نشان داد.
«اگر ایرانیان در مورد مسئله غنی‌سازی تسهیلات قابل توجهی ایجاد کنند، ما نیز تسهیلات قابل توجهی در مورد تسکین تحریم‌ها ایجاد خواهیم کرد،» مقام مذکور گفت.
در مورد مسئله هسته‌ای، برنامه فعلی این است که با کل ذخیره مواد غنی‌سازی شده سر و کار داشته باشیم.
«اگر شما یک توافق نهایی دارید که در آن ایرانیان در حال غنی‌سازی هستند، پس شما یک توافق نهایی ندارید،» مقام مذکور افزود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/122366" target="_blank">📅 18:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122365">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c95c218f7b.mp4?token=frq050Cvxr7lFWHyqNPT5DCoRfcwJtO1sidabS7Pu1PLSbA0sCUSPjZIQB1NyvuF28EhGQRU4AMSqfy8xtxfwgNaCTulBkzN5sxSMuLOfBW_BoOvm6H1lj7ZE_51m1evsXCKCbTey0PB7WHVI88gVe0f6hI36bWSjNST_FHJyFBhZ8VpVHOzCSgzioJMtdarm1WiB9z6QGocQBFI3IFwUvtAq0mDR_9cvbPl4vCnJRj5Ve9xg3FePAFx4bCz_KvhsmesI87dD0RtJt8Kk3oNqtuMi-NElZgpyvzA6qLiyX6Cw_4m3uMb54mGhIQ8F41ExzX2NDLTzn5R5gOdgmzuCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c95c218f7b.mp4?token=frq050Cvxr7lFWHyqNPT5DCoRfcwJtO1sidabS7Pu1PLSbA0sCUSPjZIQB1NyvuF28EhGQRU4AMSqfy8xtxfwgNaCTulBkzN5sxSMuLOfBW_BoOvm6H1lj7ZE_51m1evsXCKCbTey0PB7WHVI88gVe0f6hI36bWSjNST_FHJyFBhZ8VpVHOzCSgzioJMtdarm1WiB9z6QGocQBFI3IFwUvtAq0mDR_9cvbPl4vCnJRj5Ve9xg3FePAFx4bCz_KvhsmesI87dD0RtJt8Kk3oNqtuMi-NElZgpyvzA6qLiyX6Cw_4m3uMb54mGhIQ8F41ExzX2NDLTzn5R5gOdgmzuCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل داره حملات خیلی سنگین تو جنوب لبنان انجام میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/122365" target="_blank">📅 18:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122364">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
یدیعوت آحارونوت به نقل از
یک مقام امنیتی ارشد اسرائیل:
🔴
اگر توافقی که در حال حاضر به شکل فعلی خود با ایران نهایی می‌شود امضا گردد،
برای اسرائیل فاجعه خواهد بود
.
🔴
وقتی آمریکا از ادامه جنگ دست بکشد، آخرین ابزارهای فشار مهمی که در مذاکرات بعدی بر ایران دارد را از دست می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/122364" target="_blank">📅 18:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122363">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rH4knzM314f4rvYNOvqAb4Kcc1bdYY6cA2OF1hV2g7wGydCOfN-36O3ewoJQu10vbLaDtVl-hsvfyWRfnJhfuh9FTSXwbbPtgcKehA7_2uya0C5f5jLxOhcyFbLKc0TCORbcL2BYlquxz7nDnEgUT8bm4bM59elReMQ2PXnyjrogfbW9bz8dqS9ypLHc8MYfy3goj2frKTQgyhwQWTL1XC8vfHQukrPZOlhZ7uVBzMOTYfKONxN2n0ft-A5mkg_T4xIhRYYtW_s2-jT5PhxJuatSvcw1Nk6rNB8SnSMs3YAzEgHMdUz1Xuy5ISd9k6w1VY1muiKpiWrtxAhyB1AWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
/
ترامپ در مورد ایران:
یکی از بدترین توافق‌هایی که کشور ما تاکنون انجام داده، توافق هسته‌ای ایران بود که توسط باراک حسین اوباما و تازه‌کارهای درجه یک دولت اوباما مطرح و امضا شد. این توافق مسیر مستقیمی به سوی توسعه سلاح هسته‌ای توسط ایران بود.
اما معامله‌ای که در حال حاضر توسط دولت ترامپ با ایران در حال مذاکره است، دقیقاً برعکس آن است! مذاکرات به صورت منظم و سازنده پیش می‌رود و من به نمایندگانم اطلاع داده‌ام که در این زمان عجله نکنند چون زمان به نفع ماست.
محاصره تا زمانی که توافقی حاصل، تأیید و امضا شود، به طور کامل ادامه خواهد داشت. هر دو طرف باید وقت بگذارند و کار را درست انجام دهند. هیچ اشتباهی مجاز نیست!
روابط ما با ایران در حال تبدیل شدن به رابطه‌ای بسیار حرفه‌ای‌تر و سازنده‌تر است. با این حال، آنها باید درک کنند که نمی‌توانند سلاح یا بمب هسته‌ای توسعه دهند یا تهیه کنند.
تا کنون از همه کشورهای خاورمیانه برای حمایت و همکاری‌شان تشکر می‌کنم، که با پیوستن آنها به کشورهای توافقات تاریخی ابراهیم، این همکاری‌ها بیشتر تقویت خواهد شد و چه بسا جمهوری اسلامی ایران نیز بخواهد به این جمع بپیوندد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/alonews/122363" target="_blank">📅 18:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122362">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ: توافق هسته‌ای با ایران در دوران اوباما (برجام) یکی از بدترین توافق‌ها بود و مسیر مستقیمی به تهران برای دستیابی به سلاح هسته‌ای داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/122362" target="_blank">📅 18:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122361">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgVJSBhurEksmSpTZ1ZWf8uJulRnDbMm4Ul51VVEOUhJs-orLdA7NPxALgmloVn3uU75zmHKjvM5gyDBXoFg49KA_8hCJQD5Ea1pfLAtFujGezdyVmr0rAX0nZHU3TgucHbrecF2-jre7A3Z55ioPddrR58pa0j0SWhW8mP-tK7Agevj1__87E57RBY2dm0AqbN_q10dI7TFFAjF-8sgxLyhcv5duFRu-L6jHFC75V9X5vW9g4TIMWfuU9P5kuh3RtA1v91tGNsD-NW9-CcPhjsq7u8PBjdLtG286OdrX3wjg7eNzN1nos2Sj1ZPvR2zWW26ZT0QdAHj2sgT06dqbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای جروزالم‌پست به نقل از پالو آلتو نتورکز: حمله یک گروه سایبری مرتبط با ایران به آمریکا، اسرائیل و امارات
🔴
واحد ۴۲ شرکت امنیت سایبری پالو آلتو نتورکز اعلام کرد یک گروه جاسوسی سایبری مرتبط با ایران، در جریان یک کمپین چند ماهه نهادهایی را در ایالات متحده، اسرائیل و امارات متحده عربی هدف قرار داده است.
🔴
طبق این گزارش، این حملات سایبری همزمان با تشدید تنش‌های منطقه‌ای اخیر صورت گرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/122361" target="_blank">📅 17:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122360">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bad4c4066.mp4?token=MYDdYaN8o0ziEE6EmBrHRjIJDCy_V6CzcK1X6OFHU71EMDtGacD4LjXw3eaQZz3no0LWWLCSQooqFCt45p8b_OjA7f14YiKVCDD3FDiX87N5Barv_228mEOOL_q41l8IFGWVLqO6k4N2C602viQ9ED_wU9lWOQd5FLMwJFQCdBubATZ3s8PwKkToqFxXl4_yYsVlUWTtI9HN2FdwBKhhaNkGjthqJGK0JLwQknN6Coor9doHM2oI389Ok-D383KlKOGoPX9fb-TMyIU7aHGNhKXRTw7AQKrYpn3wMkwpKd-1zRltisJo2abDATX_1He4oEM8KZi0EaXzM1jXrJKCEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bad4c4066.mp4?token=MYDdYaN8o0ziEE6EmBrHRjIJDCy_V6CzcK1X6OFHU71EMDtGacD4LjXw3eaQZz3no0LWWLCSQooqFCt45p8b_OjA7f14YiKVCDD3FDiX87N5Barv_228mEOOL_q41l8IFGWVLqO6k4N2C602viQ9ED_wU9lWOQd5FLMwJFQCdBubATZ3s8PwKkToqFxXl4_yYsVlUWTtI9HN2FdwBKhhaNkGjthqJGK0JLwQknN6Coor9doHM2oI389Ok-D383KlKOGoPX9fb-TMyIU7aHGNhKXRTw7AQKrYpn3wMkwpKd-1zRltisJo2abDATX_1He4oEM8KZi0EaXzM1jXrJKCEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت آخرالزمانی کیف پس از حملات سنگین موشکی روسیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/122360" target="_blank">📅 17:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122359">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdebcc5cf5.mp4?token=Jz4YShWZ8iqrVN8MMP4h-U3uNR4ZKZCjPVpSlI5XSZalpuRYmV3wnHAnYAGdcbz1PJ6c94sWa9uL4g3t7RXHLKhOkIWIxSyZLajnV-XVB3agXic1L6UmMysQaSsDUoRIbWeBQ2wOzEcxS52PxKoNFYyoCz1gwCbgsdrmC47vLEJt-8NKtoCTLkvJs8DAthFNVgicj4If6h3nDH1W4vxfjfKirsuAZOY7OxAD8yfe25CPeFx9Lr-vKd8_AR6zNr03NGLZrbvHJR8x4bqJ-jkusyUXTO78XNVQYPdpd3syXoH3NfXidbVEIWVySjVg9UjqZNF2vBcTVGjjtMK7tDrVng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdebcc5cf5.mp4?token=Jz4YShWZ8iqrVN8MMP4h-U3uNR4ZKZCjPVpSlI5XSZalpuRYmV3wnHAnYAGdcbz1PJ6c94sWa9uL4g3t7RXHLKhOkIWIxSyZLajnV-XVB3agXic1L6UmMysQaSsDUoRIbWeBQ2wOzEcxS52PxKoNFYyoCz1gwCbgsdrmC47vLEJt-8NKtoCTLkvJs8DAthFNVgicj4If6h3nDH1W4vxfjfKirsuAZOY7OxAD8yfe25CPeFx9Lr-vKd8_AR6zNr03NGLZrbvHJR8x4bqJ-jkusyUXTO78XNVQYPdpd3syXoH3NfXidbVEIWVySjVg9UjqZNF2vBcTVGjjtMK7tDrVng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواپیماهای سوخت‌رسان هوایی KC-135R و KC-46A نیروی هوایی ایالات متحده از پایگاه هوایی الظفره در امارات متحده عربی اوایل هفته گذشته پس از استقرار از اوایل آوریل تخلیه شدند
🔴
ممکن است به اسرائیل یا عربستان سعودی منتقل شده باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/122359" target="_blank">📅 17:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122358">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
اتحادیه اروپا: به دلیل بسته شدن تنگه هرمز، تحریم‌های ایران را گسترش می‌دهیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/122358" target="_blank">📅 17:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122357">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
فاکس‌نیوز به نقل از منابع منطقه‌ای، دو بند مهم از توافق احتمالی آمریکا و ایران را منتشر کرد: نیروهای آمریکایی به مدت ۳۰ روز در مجاورت ایران خواهند ماند.
🔴
به عنوان بخشی از این توافق، ایران معافیت از تحریم‌های نفتی دریافت خواهد کرد. همچنین میلیاردها دلار از دارایی‌ها و پول‌های مسدود شده ایران آزاد خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/122357" target="_blank">📅 17:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122356">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfHcaqDyr0CDGe04Q_UnHSKSuKBhSYfmyWCM7FjvReuCZcoXrXj85EliKaJtNkdhiQpDOlC1zVI9HJocXrQ5bP1sIN8OBb5NsLRxI0INGE4vPJ3ZqF_HnPpDYz1_NGqzYO0d3jq7Jv-DsyN3cfU8IceVMyONRolH9sD3B5svslh8RV39iIbFSwetWVkdRDD2l2nDCilTJHsUD_BlpY_aJ6gkMgDbGLPIKBPz3-KvbukpdqVy79dLmSMtzUGTiaIAH6dm0AHNlX5qGGaGaRAPRrobyKrHXSJY13O7zMYoJ--Rwqf9ElP2V7lUH6a7-dFfvV8zTC4iVKBxM0PRDM4auQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ
:
دموکرات‌ها نمی‌خواهند اجازه ماهیگیری بدهند. با ما در دادگاه می‌جنگند. برای محیط زیست بد است. شگفت‌انگیزه! پرزیدنت دونالد جی ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/122356" target="_blank">📅 17:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122355">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
فیلد مارشال رضایی: اگر دشمن به تنگۀ هرمز حمله کند، ما محاصرۀ دریایی را می‌شکنیم و ممکن است از NPT خارج شویم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/122355" target="_blank">📅 17:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122354">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
یک تحقیق از Financial Times نشان داد که سپاه پاسداران ایران از شبکه تأمین مستقر در امارات متحده عربی برای به دست آوردن تجهیزات پیشرفته ارتباطات ماهواره‌ای چینی مرتبط با برنامه‌های پهپادی ایران استفاده کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/122354" target="_blank">📅 17:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122353">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7dU2fdQH6uXHZo0rcdBzWryD3i3p61b5_I8fmyPShFwIgN6uUD161H8JOP6J3VnrSeCK4sJ3j_2pCHNj7M8cWIAGHSVR-sTqTvnmVa0wc_QjH_fHrBSxpjAFEQ9K1zhaggt-axxbZ3IrLwTjrALINr-ak9lhDoRMs_LDsn__mxD3JRafUUjbu8X0kincknvCJpw8w0K7kQW2j8en3mrmsbQy1FGcdKug91o1DYloKwZseICDD6LRcGXPy4GPu9IOmLvSRKBHxZhyLNmvcxmEMAYtDXr09ZHwEIn_v_VI-x1XoeA2UFkNOC1qQrk62ImrByBSAtR5e9nuIg-XkSZXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اتحادیه اروپا: به دلیل بسته شدن تنگه هرمز، تحریم‌های ایران را گسترش می‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/122353" target="_blank">📅 17:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122352">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XX8N0qjV_45wuJRyCBxTvildL3Z7TWlI7WgLWUAFIdlzr3J779YYf_jcgBW2w8ViEuZefHVIUWVQXn50NaleoaZHGKqqxJ9WmKvJ2yohnTz-ZrmashLxwepJlUsJGAVXw85vYuJX902QBtoRPFSbezWYjz5jKpG-n4FJTS7akgNQTTEjN6114-lZpGLMA7QOD-HdKUYHzSqWsqBUAz6VXTm4IX8sT8o6ae0sBKAezmJrbbxiqks88PmKdCHTxqsojcJPp2kXh6VVhIVb7O2_abEx0r1dzmerIFXJHzP8Pw76GBwP5aiWHpnR4K_g6VA4CCWP5hjjt358e-Q7DYiu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید نتانیاهو با عکس ترامپ : ایران هرگز به سلاح هسته‌ای نخواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/122352" target="_blank">📅 17:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122351">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6hT2INphM-7xM4Wlm7vi-hiQb1A1neOuW5ksa4VC4ZAuPHigxahbvv0Gz4iP0XWkq59Hj9By3Mr6AgZxIxW-PIklfQQilZGectRcIUEblqn5kGpFicDN2jjRwNbQZoh5P1SrZga73h2iQ0udiFYY6kpKFXl6CoNIQCfp9ey2PuuHqA8WiOMWnVrjkVZqCECYpu_kzyrvWovrg_mpD7hukbakuXGtwfkMp9wvKyuD-Q2l9dehg3QfNBJGSdFouqScSzOQ2mab57qqGtcs8B1CcJq81EQV1XemY99BONv9VQNccKneHFR1jB9waUZIbnu0rpvDTvTnJEAMTH4T9Z46Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک منبع نظامی اسرائیلی به نقل از یک شبکه تلویزیونی اسرائیل: اگر مجبور شویم برای مقابله با حزب‌الله از خط زرد عبور کنیم، این اتفاق خواهد افتاد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/122351" target="_blank">📅 17:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122350">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGa7oqy_y58bEotJcnY9WZGr3jqmsykPFdMnnC--0v4G77l7EIkXPrJVoIK01qJanM5cy7nezXpewIyUD99o-JKzL7dLr6MwiCgLX-2xrhm3AaAoVAjjXBUVDaUOvbS-MivtzDrJhFx5iuZYW0YhgKBcn1X4EXg8m66tpXCKohqIIlBn_ORZnZfe-MghE0ktD04LyvsEOWMFLPET4oHjzgFdPOizIK5V0PHAFprvZ5E3VV1u2xMsCPQtQVRdg_AVqG5kWvgeh3ygjUG9ne7fKtxN8K6y2P-jdA5vzV7zxVfBFSEVApYPasN0UX1aqh3fM94_TLXFS_xBgCTo6o1kYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مقام اسرائیلی: ترامپ به نتانیاهو اطمینان داد که هرگونه توافقی با ایران شامل مسئله هسته ای نیز خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/122350" target="_blank">📅 17:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122349">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار در جاسک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/122349" target="_blank">📅 17:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122348">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ به ABC: کل توافق فقط به من بستگی داره. فقط خبرهای خوب میاد. من هیچ معامله بدی نمیبندم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/122348" target="_blank">📅 17:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122347">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BInnIzxTF9RmFrl1NuaZIekKrB_JJgI2EiiFlImaqGO1TO7lnzVi58bLag9xkrG6flrLj1R2GRuGr3vIHMMxeYYRbyQxu3aVKFDocdjEhKnZiPelFC4FF2Wwo23SbRye-s0SIBHoNB3LvnQ_QeWdJSjqcY63Xld4qo73bk3mR7X0hG5AgWfHvdGz47oyrqjGXpv2gPELPg21k2cpMszY-FnCTnG_mmccctrP1Xch5hZcJCvkySNkCPwx_cYDjVOIvUMK0nTR_bb3XcuZT9qqakiqryP2khEdd0AS4o-GgR8CkzRxcNefvgCiuh3aIdfx9Lt2vwmMgmVxPur3676tkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس دفتر المیادین در اسلام آباد: گزارش‌ها حاکی از آن است که قرار است فردا وزیر امور خارجه و فرمانده ارتش پاکستان اعلامیه‌ای صادر کنند..
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/alonews/122347" target="_blank">📅 16:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122346">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
خبرگزاری معتبر فارس: مقامات آمریکایی به صورت خصوصی به تهران توصیه کردند که به خشم‌های پرزیدنت ترامپ و پست‌های شبکه تروث‌سوشال توجه نکنند، زیرا این موارد عمدتاً برای مخاطب داخلی آمریکایی طراحی شده‌اند و بازتاب‌دهنده موضع واشنگتن در مذاکرات جاری نیستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/122346" target="_blank">📅 16:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122345">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epAJD0c_dNivuRV4WCUrXIIqhIfw9W3SijF3nAOIIrlnhbZ7e8KDNOvMhL0bMNRa3yKJIcuYDrnTqAxbxBv3XrMsekLf32mYvgXqWXlZ7FzfWnWzb33sCB2E_Ot1RBBe2J1KzwP88Nchn6bKVD2IKTm9XfNIBhO9mPtwNgt-mXLlKDychDhQUvXNgJeSRtyRdoMusDrP_rTHQhUJMveHDkknsK8FjjZNixmlK8KOYKru-EhUKfD9dHwQ03qfug45aIot76fJI53nEYcAOGswOuapOjRUp0sJ-meBgZHa3XXn1Nh433gHpw2N6gD3-jxxC73Cxiokf3P_H-nVbwd_OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سه حمله هوایی اسرائیلی، شهر یومر الشافیق هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/122345" target="_blank">📅 16:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122344">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل (IDF): نخست‌وزیر امشب ساعت 18:00 جلسه‌ای برگزار میکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/122344" target="_blank">📅 16:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122343">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
«کاخ سفید امیدوار است که اختلافات نهایی در ساعات آینده حل شود و توافقی روز یکشنبه اعلام شود.
🔴
ممکن است این توافق حتی ۶۰ روز کامل هم دوام نیاورد اگر آمریکا معتقد باشد ایران در مذاکرات هسته‌ای جدی نیست» - آکسیوس، به نقل از یک مقام آمریکایی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122343" target="_blank">📅 16:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122342">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlUE1qo_YZ4POLpOC6dgedAbCZRzXL2Vbs-zbWM7YUhKOWuSTv_M5qjZGUZkcL_k-cuwfriPt3jdVVD_xPGNOTA02PVJYDqeIzab5snwklEEeB4pVZ_8ukLGV3xTkfN0c02z9Mht1DWg1v0dBlRBJptTTZHTMapnDNfEnQoprWQEl7MeVVJ9jJubgspcKDOFfCfSkXIe-GSlr3H27ZEhwWLVyTl4fQNaKKWdSKB1vYuMXFgPKO0yVoeMEbQwBy6ErMjMo2TOVU_kUXVtsOvPw2Zb3yomnIX2p32C3VstNfSce8G3CAfd2oJLd1_Y5_1683tNyiVvD04VLrgj1FwPYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / مدیر دفتر شبکه المیادین در اسلام آباد: پاکستان ممکن است فردا چهار بند توافق را اعلام کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/122342" target="_blank">📅 16:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122341">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
گزارش اولیه: در چند منطقه در شمال اسرائیل، آژیرها‌ در مورد نفوذ پهپاد به صدا درآمد. جزئیات در حال بررسی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/122341" target="_blank">📅 16:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122340">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
شبکه ۱۲ عبری به نقل از منابع: اسرائیل کاملاً از پیشرفت مذاکرات آمریکا و ایران غافلگیر شده درحالیکه همه نهادهای امنیتی بازگشت جنگ را پیش‌بینی می‌کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/122340" target="_blank">📅 16:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122339">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجارهای کنترل شده در شهر بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/122339" target="_blank">📅 16:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122338">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
نیرو دریایی سپاه پاسداران در بیانیه‌ای اعلام کرد طی 24 ساعت گذشته 33 کشتی تجاری با کسب اجازه این سازمان از تنگه هرمز عبور کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/122338" target="_blank">📅 16:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122337">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: اطلاعات حاکی از آن است که یادداشت تفاهم شامل توقف جنگ در لبنان می‌شود، اما اسرائیل از این توافق رضایت ندارد و واشنگتن را تحت فشار قرار داده تا بندی به متن یادداشت تفاهم اضافه شود که به اسرائیل اجازه دهد تحت عنوان «اقدام نظامی در صورت وجود هرگونه تهدید» در لبنان عملیات انجام دهد.
🔴
ایران با این موضوع مخالفت کرده و خواهان توقفی پایدار و دائمی برای جنگ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/122337" target="_blank">📅 16:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122335">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAw5QYrSvg9iuz7n4ythMKZDs-DbKgxoKgJWxk_sDjcOLSJ19cr80ALHqwHVFPPm-Bjul-9sU2aBEk9x8rC65eLdXOGNmZfEf4h1KIFUQfcs_cKQOJw6kuNGzS_FXGvqKwPz1i1_ccVrA_XSFpztmBUja_NWc0IAG6CnHuONtTDr3j8f65UqxeG7rK2Mk3Nq9RQt82SAi-A-0kqj2RrmiXXRR9X5T0sM_msmqFzThncYqsxMg-ztD3p0LoaQHMngButfnpPjjLHqYkA0KgWu-IMxeYFmoMMHs5Pb54lxTTepr8uaL6mWmHdVqa1iAjLjtUz5QfaYF_qVxREm7gL5IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8f7ec9925.mp4?token=k7Sf8Ml7QzSDE8iQNpqNexi-_b7ZRWnxTuGiC_sy4u-WryS0w2PZQMJhyVJstTPN3Y05fzZj7DMxA8Btgn9YtRssX6CrX85Hv1HkKNbEwr5KdD-eifMWeCO233MCeUENwNXifR1HW7HJDhgAY2xVonB_lPVovRzYVDqHrqqrZ_oxGGALztvSivhcivjIZDW2lqFlul2p3Vtpfx6IkdcAbeHOfy2v3ePYUX4D7SZfYQcykRhfqnc54nDzVVsKNGHq8M4GvqZP_auOpexp33pyF6wjlpr3lZkKFkybLiEER7BTAIik3ch9cVVW988QL6q45UKS9u7B8qYn7nSxWnkUEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8f7ec9925.mp4?token=k7Sf8Ml7QzSDE8iQNpqNexi-_b7ZRWnxTuGiC_sy4u-WryS0w2PZQMJhyVJstTPN3Y05fzZj7DMxA8Btgn9YtRssX6CrX85Hv1HkKNbEwr5KdD-eifMWeCO233MCeUENwNXifR1HW7HJDhgAY2xVonB_lPVovRzYVDqHrqqrZ_oxGGALztvSivhcivjIZDW2lqFlul2p3Vtpfx6IkdcAbeHOfy2v3ePYUX4D7SZfYQcykRhfqnc54nDzVVsKNGHq8M4GvqZP_auOpexp33pyF6wjlpr3lZkKFkybLiEER7BTAIik3ch9cVVW988QL6q45UKS9u7B8qYn7nSxWnkUEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده های ارتش اسرائیل(IDF) طی یک ساعت گذشته چندین حمله هوایی به نبطیه در جنوب لبنان انجام دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/122335" target="_blank">📅 16:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122334">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30316b65ed.mp4?token=Z-cHUsEpjmI3srcy0b8s-GG8FEl86i3RWT5HoTZ4pwieNySqtUXGB5Ok1nnySvS2YWRbRS6f5umm90O90KiFc_7u3DQ0jOlQwfUUmWYckGwivdXi_tPIT6N-wUT1hBnhNS4s9kvomF1k1vlH5OuGhiHZDZK71u3FqGioM-bKQYr_0CWtaGI3llQzuRuTCtpS0lWY2ICZmxGtbXMF0UZaBwZbJ7XPvY522s3aczh8c6v0ucW560gNSHviXh8FbWX-w4vZ-sGA0VpMU9I6dfHHXdrA_cWhngdNJCoIw6LJbLJbisrlDYSNwu0HDwsjDggYassTZE0RkroVeN2khuAI1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30316b65ed.mp4?token=Z-cHUsEpjmI3srcy0b8s-GG8FEl86i3RWT5HoTZ4pwieNySqtUXGB5Ok1nnySvS2YWRbRS6f5umm90O90KiFc_7u3DQ0jOlQwfUUmWYckGwivdXi_tPIT6N-wUT1hBnhNS4s9kvomF1k1vlH5OuGhiHZDZK71u3FqGioM-bKQYr_0CWtaGI3llQzuRuTCtpS0lWY2ICZmxGtbXMF0UZaBwZbJ7XPvY522s3aczh8c6v0ucW560gNSHviXh8FbWX-w4vZ-sGA0VpMU9I6dfHHXdrA_cWhngdNJCoIw6LJbLJbisrlDYSNwu0HDwsjDggYassTZE0RkroVeN2khuAI1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویرانی کامل در عرب‌صالح، جنوب لبنان، به دلیل حملات ارتش اسرائیل (IDF) که کمی پیش انجام شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/122334" target="_blank">📅 16:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122333">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea7eb6513.mp4?token=nXF4GAoaCOAVwSh55BVtTpzQmTWez54pyUymNlvCB1P0PpRafajxuCEqzG-HZHMrXBJSkmlk_WhKnUMYywDCAaWmaAIZPwMT3LDsz_6Ou8T-cnNtC66QY3aHjRIBgwKByAgyJbyhvZIedT3ENPK-UkiBbc1cijK5S9BwJC1nHoZBt0Fwyy_5bMjcbgxBAUVWCGeG_F-iP6tdbQYBwoTuxRENasNwpfhM1b5s_Qy2dNTDMbfRcArBYuJIQKbhePvdjm1cEKWPNshwdSkyWZ9igeqJXaYQx2bDmnzpEqd-L0ru1340rEw_hvU1kdLGOoNLBjOQS-xp8itOPEpmgFDvng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea7eb6513.mp4?token=nXF4GAoaCOAVwSh55BVtTpzQmTWez54pyUymNlvCB1P0PpRafajxuCEqzG-HZHMrXBJSkmlk_WhKnUMYywDCAaWmaAIZPwMT3LDsz_6Ou8T-cnNtC66QY3aHjRIBgwKByAgyJbyhvZIedT3ENPK-UkiBbc1cijK5S9BwJC1nHoZBt0Fwyy_5bMjcbgxBAUVWCGeG_F-iP6tdbQYBwoTuxRENasNwpfhM1b5s_Qy2dNTDMbfRcArBYuJIQKbhePvdjm1cEKWPNshwdSkyWZ9igeqJXaYQx2bDmnzpEqd-L0ru1340rEw_hvU1kdLGOoNLBjOQS-xp8itOPEpmgFDvng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات سهمگین ارتش اسرائیل (IDF) را در تپه‌های علی طاهر در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/122333" target="_blank">📅 16:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122332">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
پاکستان تفاهم ایران و آمریکا را بدون نیاز به حضور طرفین اعلام رسمی می‌کند
🔴
به گفته این منابع، توافق اولیه و احتمالی میان واشینگتن و تهران تحت عنوان رسمی «اعلامیه اسلام‌آباد» نام‌گذاری خواهد شد.
🔴
این منابع تصریح کردند که توافق اولیه در واقع یک «یادداشت تفاهم» است و پس از امضای آن، روند گفت‌وگوها و مذاکرات بر سر پرونده‌ها و مسائل نهایی آغاز خواهد شد.
🔴
همچنین مقرر شده است کشور پاکستان وظیفه اعلام رسمی این یادداشت تفاهم را بر عهده بگیرد و برای این اقدام، نیازی به حضور فیزیکی طرف‌های مذاکره‌کننده در مراسم اعلام نخواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/122332" target="_blank">📅 16:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122331">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رشیدی کوچی: اینترنت این هفته به حالت قبل بر می‌گردد، یا ۴۸ ساعت آینده یا تا پایان هفته!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/122331" target="_blank">📅 16:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122330">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
اوریت استروک، عضو کابینه امنیتی و سیاسی اسرائیل، به رادیو ارتش اسرائیل: توافق احتمالی با ایران به معنای عقب‌نشینی ترامپ از اهدافی است که خودش تعیین کرده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/122330" target="_blank">📅 16:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122329">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Evzjqr5DiLKVeMCGjrrK_J9-g18F5hYp5s3ZaXh_fjWT5D_cDtT9zqTVuuRqDwlGy02sI5y0dU6DnEaxkWcC8lZVGiLMJ6THTv_2W_AllZgqtLN6WsAzNagD-eSlE2Odnw7a6q6onhiPC714qni2EY252Yxie3vH1EagOG3ZHHq9vAnlteMiVd3qRUh4To2zuJrKjHKCRR6htSVRWUYhxoE27o09GxZ6EXaLqFYfWmbYMR8OLguWlJ024jQQIROBVGezH5WX3GUuMNMkouO0DnvOhBY5xbZObyih1qQlkXTas3G_Gwhq0bmCCrMjmnlSP-lNmyzSaYANuO7-OmrOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social: این گروه بد (بیمار!) است. بسیار مخرب برای ملت بزرگ ما.
🔴
از طریق تسلیحاتی کردن باعث خسارات عظیمی شده‌اند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/122329" target="_blank">📅 16:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122328">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIYC1uqrwW-78g6jJzth0wb_xUj5pMuHLTQ-8hG2NmmBuz_vjzsCS1ysYnuSx9_FPPjouo9gr56Y4V75zwjxUBWTID8QI5SMDorbar-MB5EUnyPH6nXh84H6Y_2lUuylkGKwTQov3wFR123BmqVT_N5ACXGT9K-km7vtvF8QiyAy91IzKhAI7vRmuKmPbQxXlGMVr72EtU0ZWp71RJ7_gvkj-Wj56LOAsStltk1z4tPfucGjHO_W8g8u-zngwDVm8Iva5HRX5vE7PyKW_H7KT6Gtmj0wiWAhJI3b7OlTxGtH2CW8L-AoIcXc_SfbeP0gCj1nl6FgpsdLv_-H6iV7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جمهوری اسلامی از مجتبی کیان اعتراف اجباری گرفت و در کمتر از ۵۰ روز اعدامش کرد.
🤔
خیلی ها حتی اسم این مرد رو نشنیدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/122328" target="_blank">📅 16:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122327">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
زنگ خطر شیوع تب کریمه کنگو در عراق/ 4 فوتی و 43 مبتلا از ابتدای سال
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/122327" target="_blank">📅 16:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122326">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmFeDJ9onn56oUCRwwUsHSZOHjI_x6iLwZsQSochdkvUa01okLxoC51vXojG0ij6c5bOuCZODWEZ1h8l_Bkq-Q_514tndhXxAp3W-t-5U1jJhzxPx2YfDzsti9g02Yeo9Mn72p1dR72dX3c4NAxzAkfEJ8TwFWN1D1zO7opYeP7f5ATREZzX7-xTklrPOczuXvOszu0cUiAzAIJdA_QlSZv6HBe3HYOQOOjaj26gXHQPSyuDB0RFbXJsSKV-GkVeED3_DUTIdmZAWeXfVQJ7-wjLwPg7Y8WhZNzV4QPiPvqOE19zPxGX0Ty3KNhKuOV6Wap7tozHWvSpzY_yXueYdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویری از لاشه پهپاد جاسوسی اسرائیل در هرمزگان‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/122326" target="_blank">📅 16:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122323">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BCKcSP36p7skClPITqh3TlRnteDjZNQKMDcTY3YFqlLekZ3adoZ6T9VtpAMx-IyUK2yDFHzY8XTY6__gW9bfjRW1ACBBmsaREqkagH0GZVYRTNmVpeA210EZwF8vGvjcg_P_S6SnHgOH7ACJ2AlmeHPGeu1IVJwwLHieVkkmuLZ49fbRUmqysTEhOtsg1bHz2C026TIdAg-X97LBiRQhXRcLr3xYeS8EdHDwN5LB3IKQvIMA5BtpKi4_eY1-_YftN1i9C5EpmnK_wuxDkKO2NInfp_-9dNoLfRMsAFoZtpA38lqlIRoxmzI_O0lmlyCDzEuWGnWhkYxdB7O0x8Zr9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VB6okloaCb2WbX0QhOlH7NtgwWzZnU451A0kzcA66o0GrwgveXfnlANQDy1nknykxT2mLRRiEClU4js0Y6WAbZnKU0LZ4OA1llglh4ShB8x4tse357d77rQPw0Iv7MCMru16DmKIEdKfTOLLpIGb5ILJTmm2K1zYoFCmeBLbQCZlafN5dUfXOsTM75Hv2Xx0ckeF6u3zgtF2x3taBQtU-59uBeec8i8jeLmVisTeRl7O6qsfvhg9Q2em5aubHznK81QQO95NXxamFuJnKRl8VNCw_AJbCiUyIHVF5_XbmwauPp52ZUR-_8CeMoSaapNYkNk_M1Ri5H0ik5W-UVCcWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EVoKZs8600xEXtovsylLIG61yNRLVsrd2WwqkSXlzDAqE8LocXSlDuZ5-ZO1RbSJK5gKbr1Ijx3-_lfETMYkm1eCdJsJRzADFj-zZWJYOz5ZALMW3YOUpy6uetpA4gtZyqcWqHpeg_0rzq_Z2r7VqlOPbmT-sY4X5zDCc6WNzi9ejyqEfFbi3a9nWq9UVs2xo3HAdSKYAv9TEN-f8uYstLTVe1aGKy_vRNubSUoCsi_YT7Qvv62Iru_Z_Yv8SbDl0tuQQSEjGq5oerTaZn3MAnS4LktCrsI7s591gpbZmsTRM8oX1Wmw8YHX_i7q0_CmSq4n5AujqBbsF-V6RU4Kdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ درباره چین در Truth Social پست می‌گذارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/122323" target="_blank">📅 16:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122322">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCP11teqmpCFlUZk3yJOM58c64VP3Q0ax-vfrzKPtpxFsO5_sW3cxEQtCkU272caKjwKwzKYjK7ALQsTms0saormmoXKAA1ljWwKKyg5jNsw3PjLZb60X1Ty3SCe8qEt1nIGdgIbuKoqqFYXUW5m73SccKEvOZLcrm0xqLitzf2RA1wdRUVGkzEIo_Qqe2nzJRYbKFLmAc0O3PME0LG-TPWEcLJzUEYHSRhljUgC5iWoW2HNOY89viNkHmgLDBycWLYg5O_a0PpbHdQthSgB1l4n0DEpoYGvR716JCV7ae6liohm1HzZN_i6ygBgaYjR43oCZ7pchhXiOxCFk95nMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری و رسمی؛ با اعلام afc استقلال و تراکتور به عنوان نمایندگان ایران در لیگ نخبگان امسال مشخص شدند.
🔴
تورنومنت 6 جانبه برگزار نمیشه
🟡
سپاهان به لیگ دو آسیا رفت
🔴
پرسپولیس سهمیه نگرفت
@AloSport</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/122322" target="_blank">📅 16:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122321">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
رویترز: ایران با تحویل اورانیوم غنی‌شده با غنای بالا موافقت نکرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/122321" target="_blank">📅 16:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122320">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYlv4m5lP2KibqkLz6YMi88y0JFgIPZffRpTlwVzha4HzJTwHuFAnWA5VhExPibCNMbFv2Mjj1UcOihnKra2x3ith5G_dDc4ZlwZDdFZHj8XpXCsKrPL37xhLtdRckJ7ULZ62LHx8_JwQVRjTxJPo6MGC_GT2E8exe-Uexrr8Vw-zP5hre6O6Uv06D_x-5drI7le8FKYtXm7XdoLFw_Tnpqo8GmtZA8JfXGXKa61m7hWKsnOkTQ9pR8kcFZ_SAWEvk85W1kqHDZLe1XSbjktGgaJl3_tPwTPGkqpT1ataVIrGNEdxruG9_kGeF6tfawDfldYg0Wm0aE0NtzVi0lhvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/122320" target="_blank">📅 15:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122319">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csFvfbW5zYIrbDKD66srvZ069Xpuna9Y2KeQ4Igcwt84hqTbqDYat7mOWR8oALe93Dx5V8kXLdFRjWDw9WV980od_Y_pRpK45zOWa2A-nY6XtiHzOYC3Ozg8X83RzTqRM8LboLAZjY9OR_rsuxopann3Sdp9EHSbrjS_iSTW7pd6IkFOicZ-Ibgmlhe0p6Qb1am1jtcK7995XuzVN1Y1yhNmQ732diL_jv8F46FSsAfKg9cfBR3543Wh-bE1iHDHGtTLuZtED43jc0OPGF3NXTUtXqpdu6lWOw3srU0xQ5JUVTiVn-vNqvqyo0Vva0JjLPbEVNY14VXO3i5se4-7iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ درباره نیروی دریایی ایران : خداحافظ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/122319" target="_blank">📅 15:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122318">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
رند پاول از سناتور های برجسته جمهوری خواه: جنگ همیشه با مذاکره به پایان می‌رسد
🔴
منتقدان مذاکرات صلح ترامپ باید به ترامپ فضایی برای پیدا کردن راه حل (اول آمریکا) بدهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/122318" target="_blank">📅 15:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122317">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ارتش اسرائیل(IDF): کمی پیش، پهپادی انفجاری که توسط حزب‌الله به سمت سربازان IDF پرتاب شده بود، در خاک اسرائیل و در مجاورت مرز اسرائیل-لبنان منفجر شد. هیچ آسیبی گزارش نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/122317" target="_blank">📅 15:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122316">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وزیر نیرو: برق مشترکانی که با دولت برای مصرف بهینه همکاری نکنند، قطع خواهد شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/122316" target="_blank">📅 15:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122315">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lP1Cvh1xBumsErwcO3oQcsulxPywALzeIufQoOb_gtuEmcaAuXDqWrpjxxnVSru5iGPAqSB9FkAPTlLkEvsYVwJWslBDgQ40E7wTUJxB0ErNBBdR_bAlPfsTmy4F-q75ZCGiGxhUeuxN30JnOXXdAoq8NJh_QIdLS-Fy48IEYjQ2QbUBI7WlnY-mbsSsrXbG2IysCGN56V3rs20FOQscNTaU_smz7O1mpgBti5uGe_eneNT1g6lN4ZBHjXunCNODPyetraI1plLw4UpRbQqC31m-Jh-sSvk3HkqhYeY4Uh1-mDkRHxB8_MVE15Qv1hsiX_NoiCo9NfD7A76Pe6R3mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کلش ریپورت به نقل از سی‌ان‌ان: شروط توافق احتمالی ایران و آمریکا
🔴
یک توافق احتمالی بین ایران و آمریکا مستلزم آن است که ایران از سلاح‌های هسته‌ای دست بکشد، غنی‌سازی جدید را متوقف کند و مذاکراتی را برای کنار گذاشتن ذخایر اورانیوم با غنای بالای خود آغاز کند. جزئیات مربوط به حذف این ذخایر و مدت زمان توقف غنی‌سازی، بعداً مورد مذاکره قرار خواهد گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/122315" target="_blank">📅 15:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122314">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ارتش اسرائیل خواستار تخلیه 10 شهرک در جنوب لبنان شد و گفت بزودی هدف قرار میگیرن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/122314" target="_blank">📅 15:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122313">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
سیتنا، پایگاه تخصصی اخبار اینترنت: احتمالا تا هفته آینده اینترنت بین الملل متصل خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/122313" target="_blank">📅 15:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122311">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jh3ENMHv6T_6Q_8l48x7JZnVtzCTuoiVkQaRKRYMCRHJyIjfCu6yfs8bx1ESf3VVFFpIgS2HycbVQD_lGxObl4as1pVZqdDMORLa_vW2KmzSUHILlItiRxnXwf-Lrbk-kOxmQo0Q5HrDP7f-0VGfAzUWg9Hlp2oVlT1EeicGcrhJN5e3Bm9yhNEwcFwqsX6mXZLpKiy-eSnW-SHRq3nu5ihGe455NuYltVb-hUE-SJvIStIIqNHKtllQKVWMh4-liL_s266xDOqc_qTTiOtgx98Jp02YQmMMTqcL_dCHAhMPx7Cb-KPMdjfGW0DqTLpNOnpy_dwNbH_-BDfp5e0HfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4j_xIcIm_kwXic-kLtJvlGwLO9eoEd1LoFP8KzOrRLRBr2h_iyJJU-wwTS0vXjyfl1Sm2UQsJ3O1ja73zoA9FOZrJpgTkYIbapZ4p-QjJpq1DWnSrb5e1CThi0KKwlNFr9Y07EwGbyZ3A489TRqgZU2lT2pNP5-80OplE33RzqHcjF-NvyudiSirXCMVqyWvnWuzhJFKZQB3QKx2yZI3L8SETrchlISJRMfKyeRfA0jqXtAM0gg44pMqf0GoS0K_Iu9SOauZlwtcoOmPuuF6ixcOHoyG1vShKx7GQdXlH1EnNcGqLZ54yAJ6nFQGwB1Vn3tNE1cvwVQTJY6bYIIFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصویری جدید از حمله سنگین ارتش اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/122311" target="_blank">📅 15:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122310">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beeb38d0d4.mp4?token=fwLl9OKitKh3jv6c9hmVzNlUHYEhbzMvQK2h4nEylkYkhhTH09M5veiojwFR87-bdLZKn2ZEHH2kzTwIc7tlPCLCFGABzxlWZxjMUoyBy4j_RK7bal9AivY9n-5ui33AxZSlmB3TcrGmqVooy7H59VchsOQPvGMjzK9qNiQyY10u2ri8MYa24D_Atyj1g8dp_BxuGk6jWnwtEabCa_8btMEPfPgpNts73pNOl7xbenEzpbjzD_OVcuaDaHkVcUkhBg7ULQEuy9LNmOfAkD2kW97miEc7AvVZmMqpsxNMLezpUHA-Ljg9kbB8cD_BIznlMaR80pck5nU-3JHVEWTSUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beeb38d0d4.mp4?token=fwLl9OKitKh3jv6c9hmVzNlUHYEhbzMvQK2h4nEylkYkhhTH09M5veiojwFR87-bdLZKn2ZEHH2kzTwIc7tlPCLCFGABzxlWZxjMUoyBy4j_RK7bal9AivY9n-5ui33AxZSlmB3TcrGmqVooy7H59VchsOQPvGMjzK9qNiQyY10u2ri8MYa24D_Atyj1g8dp_BxuGk6jWnwtEabCa_8btMEPfPgpNts73pNOl7xbenEzpbjzD_OVcuaDaHkVcUkhBg7ULQEuy9LNmOfAkD2kW97miEc7AvVZmMqpsxNMLezpUHA-Ljg9kbB8cD_BIznlMaR80pck5nU-3JHVEWTSUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم خارج از پارلمان لبنان در بیروت چکمه‌های نظامی سربازان ارتش لبنان را نشان می‌دهد که در نبردهای سال 2015 علیه شبه‌نظامیان اسلام‌گرا کشته شده‌اند که در اعتراض به طرح پیشنهادی قانون عفو ​​عمومی به نمایش درآمده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/122310" target="_blank">📅 15:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122309">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وزارت امور خارجه قطر: نخست وزیر بر اهمیت حمایت از تلاش‌های میانجیگری مداوم برای دستیابی به توافق صلح پایدار تأکید کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/122309" target="_blank">📅 15:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122308">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
روزنامه بریتانیایی فایننشال تایمز ادعا کرد که سپاه ایران از یک شرکت ثبت شده در امارات برای خرید تجهیزات ماهواره‌ای نظامی از چین استفاده کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/122308" target="_blank">📅 15:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122307">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTWFHrDXPkQLe_o_nEmnJ0KaHEqU5KyEs8nZ9VtO7dZOl89qyvN2NzdWRxgiZp5h3JbL899RD29t-nMWPRrEkLo52sSGPuD8MYcid5sBYcosohCMpidRCZgAE8u1stdQB2a67ySwPzRCtaviCKU_BE_UW758_AKnRNkpCN1sAQg72DJSyy4nKEqpwSJldZrY8FNd_fWvSKKkmWO8eORvm0n3kIvL-bQ3nOzjpj3aDVt2Yv3dstN3x9nJbQt9mn7ZI9g0veI2IcV4_v1biQfJM86aYbcP-Db2RoemGZSfCmTlChV26c7aQHr5F4wIV6r9eqwupplCsKqaJoatDWCzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توافق احتمالی بین ایالات متحده و ایران شامل تعهدات ایران برای دنبال نکردن سلاح هسته‌ای و ورود به مذاکرات درباره تحویل ذخیره اورانیوم غنی‌شده بسیار خود و تعلیق هرگونه فعالیت جدید غنی‌سازی اورانیوم است، گزارش می‌دهد CNN.
🔴
جزئیات مربوط به حذف ذخیره اورانیوم و مدت زمان تعلیق غنی‌سازی در مذاکرات بعدی مورد بحث قرار خواهد گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/122307" target="_blank">📅 14:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122306">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqsXy0jfMh5frkfl9rdQY5z90GZWDSvZtpF7znmNAu9AFiUbETjWostTukastWux0fKE_SMXfAVGItCCOEBskpaiFcYvKU-yOuiJ9tV4phPRRRMKklPcTKmM0d1nbF-lFuWasjEIRR0wKeTW1yOMp5j7DCRUnvBtcyj_jUiP5Mwdu98UFHsImV-gqBx9RbuboUoLV3FRaA4lPjG-vrlqwThPeQdaGhkvnHOOwtFxEBE4M1VuUuaTKhz9mGpFPWuuRAdXosFOjMMAN2N_ro90BI--NJyNarB9bu5uqhUbGOToHbCdoS360YQQbqiRf2fwYj9yI2CUzOHhJvioKMs6UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش صدا و سیمای ایران، تقریباً ۲۴۰ کشتی در انتظار دریافت مجوز از ایران برای عبور از تنگه هرمز هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/122306" target="_blank">📅 14:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122305">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80dbf33e59.mp4?token=rpdWnI4oWfKqragCZVCApYYCv9v9WtTCwKcwh-_PlWhbFK4zOsP2FkEbxgfQwpXfABLe93Ffh57x3sZt3AfDHV6mB3fF3EjLBXanfv5UosnNAN0sb3m8JgjV64bi5Z7BDcuMUnumJfwApmTVo4wRbYq2OeSrV3ejKOrBnOVvlLDkCEW44fgTQz64aXUDj5cGSjxPJOuxkT6sZ2oZjDZJmY4JcJ6E_ebQzGW__GgNup4WJsJwsW8KJ-LJLxsrbu39ivAynZVnankgyWvGB8lAEAwbSPa0u0yUfl_GkvOMp4c-64tbeH-YUPG7UgBrDx8_pdleerx2RPcOSFKYgBTBAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80dbf33e59.mp4?token=rpdWnI4oWfKqragCZVCApYYCv9v9WtTCwKcwh-_PlWhbFK4zOsP2FkEbxgfQwpXfABLe93Ffh57x3sZt3AfDHV6mB3fF3EjLBXanfv5UosnNAN0sb3m8JgjV64bi5Z7BDcuMUnumJfwApmTVo4wRbYq2OeSrV3ejKOrBnOVvlLDkCEW44fgTQz64aXUDj5cGSjxPJOuxkT6sZ2oZjDZJmY4JcJ6E_ebQzGW__GgNup4WJsJwsW8KJ-LJLxsrbu39ivAynZVnankgyWvGB8lAEAwbSPa0u0yUfl_GkvOMp4c-64tbeH-YUPG7UgBrDx8_pdleerx2RPcOSFKYgBTBAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: قطعاً ما و تیم مذاکره‌کننده هرگز کرامت و غرور کشور را به خطر نخواهیم انداخت.
🔴
ما آماده‌ایم به جهان اطمینان دهیم که به دنبال سلاح هسته‌ای نیستیم
🔴
ما به دنبال بی‌ثباتی در منطقه نیستیم؛ آشفته‌کننده در منطقه اسرائیل است که طرح اسرائیل بزرگ را دنبال می‌کند و به طرق مختلف توطئه می‌کند تا جنگ، بی‌ثباتی و اختلاف را در منطقه زنده نگه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/122305" target="_blank">📅 14:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122304">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcRi_GVjv4TcnQQ1UuZKjzhaNC-agRYtbNZRUwrQKFtg9sorKTvzULWCMUXMBtSEv3UwnluZea7IEd4NyGK0XzOenUKMuslnTVX06RCO76p5hZBPaesVwDF98SvdEmEk8TzlxhhrWklOzLP66fGHVBi4YFUIERiamc2_FvlZlUD3PI2v6VufPU0NxJlxLWCS2tSvUtfOc6HWGSDUfafwdhyJyZgkjY0vLU9RoYKLxyxZ8Sx_9oRegpGoOFBaOssOxAMA0nOiQ0Pv8lzC5PNArfrLu_NExfDGnkWFcJJaJAaPyrQbpyjTnVUdWvHo1ZN6H4ykOVmCUkcM4CL__Bc6Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نشریه اکونومیست گزارش داده که شرکت موشک‌سازی اسپیس‌ایکس بعد از فتح فضا، حالا پروژه بزرگ‌تری رو شروع کرده. طبق این آمار، اسپیس‌ایکس بزرگ‌ترین عرضه اولیه (IPO) تاریخ رو کلید زده تا ایلان ماسک، ثروتمندترین مرد جهان، بتونه روی یک بازار حتی بزرگ‌تر از فضا مسلط بشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/122304" target="_blank">📅 14:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122303">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
فاکس نیوز: توافق مورد انتظار تصریح می‌کند که نیروهای آمریکایی به مدت ۳۰ روز در نزدیکی ایران باقی خواهند ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/122303" target="_blank">📅 14:43 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
