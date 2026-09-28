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
<img src="https://cdn4.telesco.pe/file/LxLGU3_Qfon5Z0btmDbTYLDm1CaXXLiNwU4BCrQ3EWPJgBbf2_M0RKSINAoKabXP_m1bYkXdaK9d7f9XGLAXYSeIPYcXfTL7QyF9JZcqDw_wuU8D5sCCfd2grUBgrRsGM9KzdBIaPOZc34FpSfThquZRx9ePRaqA6oY-Omi7F0f45pPNDVpZNmwoTjWz6SJfoSflxG6inVZnuiLBoGSpr88YSh7FuEHKa64e2SJajcLgn1fGI4GpLk6TXeKOruxt-QcZAdkgxLweI5u8bnBMrYRHLzMjn9bPIR9LRLppxz_EYDC2KU3VVrqceWJGYPzjeMd3c_JufbuVnOfOnfTaQg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 02:17:12</div>
<hr>

<div class="tg-post" id="msg-149963">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
عراقچی:
امروز (دوشنبه) یکی از واسطه های قطری دیدار مجددی با ما داشت، بحث هایی را انجام دادیم . روی ایده هایی صحبت کرد و اینکه چگونه می شود برای تحقق شروط ایران راهگشایی کرد و چگونه این شروط را محقق کرد.
🔴
ایده هایی داشتند و بحثی را داشتیم که باز با طرف آمریکایی هم مطرح خواهند کرد و بعد پاسخ نهایی طرف آمریکایی پس از آن به ما منتقل می شود که امیدوارم تا فردا (سه شنبه) این کار انجام شود.
🔴
من چند ساعت دیگر به سمت تهران پرواز می کنم و پاسخ را قطری ها هر موقع که داشته باشند، می دانند که چگونه به دست ما برسانند.
🔴
این ارتباطات و پیام هایی که میانجیگران قطری و پاکستانی رد و بدل می کردند، همیشه بوده، الان با توجه به طرحی که ایران ارائه داد، شکل جدی تری به خودش گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/alonews/149963" target="_blank">📅 02:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149962">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03738737a2.mp4?token=k6o9ME9M_cpWPrwUSs84Z7fX1YuqfhWMuojgYC-In9xpgST2ZpY4tFI20blhk4QDmHtzyQFadSUDw0_XvK5sT2pWGwtai31gyNLaBcI6A3rBO-2iRAVaMKHoqEg-xSRT4ijMABg8fEBiJWYrlSAuMr8XB7rzV2FEjgeShS0ETCSpMWRJ1uB61Bo-lIs8gRwy5NpVI2kMwNKakwdfo03dKEEN2DhXwEIInSqaDGdEm73410Ub0GksOs_bRJ0I1KT9MFS9GHg-58u0N1GpwWcKq48PoUecFxXi82vYgHhI_VNLYN0k1VF-ZUi1GMAPWyzPJCnhcZGifSeWRFrchKoLRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03738737a2.mp4?token=k6o9ME9M_cpWPrwUSs84Z7fX1YuqfhWMuojgYC-In9xpgST2ZpY4tFI20blhk4QDmHtzyQFadSUDw0_XvK5sT2pWGwtai31gyNLaBcI6A3rBO-2iRAVaMKHoqEg-xSRT4ijMABg8fEBiJWYrlSAuMr8XB7rzV2FEjgeShS0ETCSpMWRJ1uB61Bo-lIs8gRwy5NpVI2kMwNKakwdfo03dKEEN2DhXwEIInSqaDGdEm73410Ub0GksOs_bRJ0I1KT9MFS9GHg-58u0N1GpwWcKq48PoUecFxXi82vYgHhI_VNLYN0k1VF-ZUi1GMAPWyzPJCnhcZGifSeWRFrchKoLRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بن سبطی از چهره‌های اسرائیلی: مجتبی خامنه‌ای زنده‌ست ولی کسی دستوراتش رو جدی نمیگیره. به گفته او اسرائیل منتظر درگیری بین رهبران ایران یا قیام مردمه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/alonews/149962" target="_blank">📅 01:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149961">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBsJYja_sY7Cnt-Lc962hRWgIydRcpyM93vqs-36BBzuN3MltFxZ4HZfEomlB_Klve7KidDEt2ZEBR5NOlAy_fS2ntXYdK6KvQrEzDdBuZirbXXDVR-R0zXuIQwbs-XhzVjlACAhGUIV7HBLcz83T_Uk5bcmsHID5elQPJFrx4clJ6gPMTb30SjrFPOy7-bFCsMv-Gd4jI7iHsDBP3z2VdkvJ1G6CAkOuPI7hzeRKVVNKI6za4WPzE798M2cSujmm8Fd6tHCYMztiT5d4pzspNkGJBcwtiioUERFU6EVBjwpUIYkAfYuo2CiQUul-dZ2bQLVkPatuCbUuzpADNxhdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
آکسیوس به‌تازگی گزارشی منتشر کرده که در آن آمده است "ترامپ" به ایران پیشنهاد رفع تحریم‌ها و آزادسازی دارایی‌های مسدودشده را داده است. این خبر نادرست است. من هیچ پیشنهادی به آنها ندادم!
🔴
گزارش آکسیوس، مانند بسیاری از گزارش‌های دیگر، یک داستان ساختگی است که صرفاً با هدف ارضای "سندروم جنون ترامپ" آنها منتشر شده است. آنها باید فوراً این گزارش جعلی را بردارند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/149961" target="_blank">📅 01:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149960">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
شلیک موشک کروز از هرمزگان
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/alonews/149960" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149959">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">در روستایی دورافتاده، کدخدایی بود که سال‌ها با حاکم شهر دشمنی شخصی داشت.
هر بار نام حاکم می‌آمد، کدخدا می‌گفت: «روزی او را سر جایش می‌نشانم.»
اما به مردم روستا می‌گفت: «روستای ما از همه دنیا قوی‌تر است و هیچ‌کس حریف ما نمی‌شود.»
کینه کدخدا روزبه‌روز بیشتر شد و سرانجام تصمیم گرفت با حاکم درگیر شود.
حاکم هم در پاسخ، راه‌های روستا را بست و نیروهایش را به آنجا فرستاد.
کدخدا که نمی‌خواست شکست خود را بپذیرد، مردم را وارد جنگی کرد که توان پیروزی در آن را نداشتند.
خانه‌ها و زمین‌ها یکی‌یکی از بین رفتند و روستایی که زمانی آباد بود، ویران شد.
مردم مات و حیران به خرابه‌های خانه‌هایشان نگاه می‌کردند.
کدخدا اما هنوز می‌گفت: «ما قوی‌ترین روستای دنیا هستیم!»
پیرمردی از میان جمعیت گفت: «اگر قوی بودیم، چرا خانه‌هایمان را از دست دادیم؟»
آن روز مردم فهمیدند گاهی کسی برای پنهان کردن یک کینه شخصی، غرور جمعی را سپر می‌کند.
و روستا بیش از آنکه از قدرت حاکم شکست خورده باشد، قربانی لجاجت کدخدای خود شده بود.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/149959" target="_blank">📅 00:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149958">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GvzIFGNhOOBhRl2xzrOpod3IURQaYyEZUaZ_R6oANLQYYrII1Wb1W1-P7fblSGhdiKLIlEGPbUoSzUnppFC2fBvuwE4nxxd0AKiGvxHEYtf0ewzAkAJvpsk7R5DlLANsur1wpOHkk3J1cplCE89LLbPCPsC0VUzPP2rggKxE9mIydlUhT_N7XfFA1Dm6kEdJHk4IYLdobd4vdKVDQQeWXiQ0xRbJ9rY-ID1wnLbZzaerCqzEEdE6J2M-ySkJ0k9BE62C2XK7Fn6H1znayoaaohPYBdoqZj7_cuqc2QWVCpB2Vy6GovvV8VI984bxWggptQxaloYCqfieU666e4cABA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید:
«ظرف دو هفته چیزی از اقتصاد ایران باقی نخواهد ماند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/alonews/149958" target="_blank">📅 00:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149957">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نکته اصلی اینجاست که دلار داخل و نفت خیلی این حرفارو تا اینجا جدی نگرفتن  هروقت دیدید اینا شروع به تغییر محسوس کردن بدونید ممکنه جدی باشه  نفت ۱۰۵ دلار  تتر ۲۴۴  @shahab_gold_trading</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/alonews/149957" target="_blank">📅 00:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149956">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
مهدی محمدی؛ مشاور قالیباف:
روحانی و اصلاح طلبا برای آمریکا پیغام فرستادن که اگه یه لایه دیگه از رهبران و فرماندهان رو ترور کنی؛ احتمالا زمینه تغییرات در ایران به وجود بیاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/149956" target="_blank">📅 00:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149955">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d63f3c9c5.mp4?token=QRIQXX5SQRyhU35FrqKQgKFsfEnj5YLNkPg7vopOOL9rTR_0BDOcVXBpfHCnDH_BRtHYJT5sJVNeNwN5FvVQtsxaapHKM04HOcLFA4waHRccTcljRGcF1w_yJQSTRxB884Jlu4531EsIfie8NlWZZsD5obqfzyFi0zf6iS2MBO7bHRhOOhZ7B60q6cbD_fCHAiHWw5ZLwFpuDgzFc8Hc3onJfHHvw55p7lX_ffTlpEIjxv7FW88_37jhCxeVrJTpydVFpLfgXLkuKIK5E61igxqUsHjV6PPV3CdpLKkgyCzkTF56yHhTlrSLN7cNiTsGKEB6Q1iUl1TiuKhj_A_NUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d63f3c9c5.mp4?token=QRIQXX5SQRyhU35FrqKQgKFsfEnj5YLNkPg7vopOOL9rTR_0BDOcVXBpfHCnDH_BRtHYJT5sJVNeNwN5FvVQtsxaapHKM04HOcLFA4waHRccTcljRGcF1w_yJQSTRxB884Jlu4531EsIfie8NlWZZsD5obqfzyFi0zf6iS2MBO7bHRhOOhZ7B60q6cbD_fCHAiHWw5ZLwFpuDgzFc8Hc3onJfHHvw55p7lX_ffTlpEIjxv7FW88_37jhCxeVrJTpydVFpLfgXLkuKIK5E61igxqUsHjV6PPV3CdpLKkgyCzkTF56yHhTlrSLN7cNiTsGKEB6Q1iUl1TiuKhj_A_NUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار خطاب به ترامپ:
آیا تیم شما امروز با ایران صحبت کرده است؟
🔴
ترامپ:
بله.
🔴
خبرنگار:
با میانجی‌ها؟
🔴
ترامپ:
بله.
🔴
خبرنگار:
چیز دیگری هست که بتوانید با ما در میان بگذارید؟
🔴
ترامپ:
ما پیروز خواهیم شد‌.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/149955" target="_blank">📅 00:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149954">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yl4gyeYCvhyZPylAGebKGMiM3JbgPJ93ZBfclnhv7oFwrIRqgeZGv1KZR2SqkMMS88W0DQZiC1CkweWnYDxJpyNZdPNbNS-O-M-kW0AzrXQ1E3M0XRJD7YCHuYOXa8DKQ9mK4jF2OUaQ0QV9F_a0W7uJBeRHAHW3rfiD6qxCDBtn6zUpKMLzv1WcWrm1q07HgPFqpk2zE2RJwF4uFXxSdQZWFSRI8Ey3hSny4uVVBU9iduSdtaOuhyNa9EMyJ6Z_wwjzfPQ0Pc1bVuCDWU6AZ3-_k9VquRVlcmljsEyg8zoBZhXhXJWq6wAuy4sGfqFE5efl0C5DrWEcWqUkIv9IRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پاوربانک بخر، ایرپاد هدیه بگیر!
🔋
پاوربانک ۲۳,۰۰۰ میلی‌آمپر Xiaomi M10
🔥
فقط 2.199 م تومان
✅
پرداخت حضوری در درب منزل
✅
ارسال به سراسر کشور (شهر و روستا)
✅
گارانتی تعویض و برگشت
لینک خرید اینجاست
👇
https://yeklinks.ir/powerjzl?utm_source=Telegram&utm_medium=lead&utm_campaign&utm_term=63575912425450218</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/149954" target="_blank">📅 00:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149953">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b6cf54c5.mp4?token=j9EiBMcjoxfYiprjn07PmN8_4Xjhkh4WP2plY_YqNWV0MPnHZs-Q1Rl4cqI4BGnHwWD--Qo4GTOtIi7djDA9UBP3vU016iwCV5tWUIB5_ek5vXcZYWHGCmeSBYRAfItgzkKfwVGrj6rrb00Lm5xHZ84kzFvPKeabYZEY_BnlBYvngQRk1eatQyso4l53-p47wU_AEKWwToe4IdolcsHgERl4k5JL3suM9CnygIgQjNYPVFt1fyPNTJ1rwloNMKm0F5lD0iV2jaN0_aF08KC7PAuEHkiGZHD2LOe3yQZVDwsskmJnQ66ZrMyBDg-IEsPSzj5KUkG6FFWKSelP3-sxew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b6cf54c5.mp4?token=j9EiBMcjoxfYiprjn07PmN8_4Xjhkh4WP2plY_YqNWV0MPnHZs-Q1Rl4cqI4BGnHwWD--Qo4GTOtIi7djDA9UBP3vU016iwCV5tWUIB5_ek5vXcZYWHGCmeSBYRAfItgzkKfwVGrj6rrb00Lm5xHZ84kzFvPKeabYZEY_BnlBYvngQRk1eatQyso4l53-p47wU_AEKWwToe4IdolcsHgERl4k5JL3suM9CnygIgQjNYPVFt1fyPNTJ1rwloNMKm0F5lD0iV2jaN0_aF08KC7PAuEHkiGZHD2LOe3yQZVDwsskmJnQ66ZrMyBDg-IEsPSzj5KUkG6FFWKSelP3-sxew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دولت امارات در مجمع عمومی سازمان ملل: امارات خواستار پیگیری اشغال جزایر سه‌گانه تنب بزرگ، تنب کوچک و ابوموسی توسط ایران است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/149953" target="_blank">📅 00:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149952">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
بیرانوند: همه گیر دادن به سربازی رفتن من، خب اگه با سربازی رفتن من دلار میشه ۱۰ هزار تومن، همین فردا میرم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/149952" target="_blank">📅 23:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149951">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
نایب‌رئیس مجلس ، نیکزاد: مجلس طرح سه فوریتی خروج از NPT را بررسی می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/149951" target="_blank">📅 23:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149950">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCJglbzb_qoB386w9uPjC9Gyt9YVCoIjKCn_N4bRIMgMj-dWTWkQpQ3exQlzzevESLwcEbOR_scGWOuLZ16beHbC8vrUod-q5o8qgU88ocVAW8aa9GD0eq0dHYmI_W5-kzAj8BUGG9kQ6oIQUY9AD6_vfBKEOiWQVVY-GzW6oxSpKa0d8TBNH2E0KtxNvJqiNIrqC_slBdLRCaZq5l7uWkjRUqMj2WV1MD0T5DA1bFqWaqAmZ4nrNyxyVYLHoWMJZR8K8EthHDnjTKJzpT6XZjmvkt9VKKkQD-sQyzqU5-PdSf6PebNtW3Acuo87xY0akk242REtLnX-W233GGTscQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز همزمان ۵ سوخت‌رسان آمریکایی در نزدیکی تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/149950" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149949">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
نورالدین الدغیر،  خبرنگار الجزیره: اطلاعات حاکی از آن است که پیشنهاد جدید ایران شامل هیچ تعهد هسته‌ای نیست و موضوع هسته‌ای نیز تنها پس از اجرای مرحله نخست مطرح خواهد شد.
🔴
اختلاف کنونی بیش از آنکه بر سر اصل مذاکره باشد، بر سر این موضوع است که کدام طرف باید ابتدا از اهرم‌های فشار خود صرف‌نظر کند
🔴
میانجی‌ها در حال بررسی فرمولی هستند که امکان اجرای تعهدات را بدون آنکه یکی از طرف‌ها به‌صورت یک‌جانبه از اهرم‌های فشار خود دست بکشد، فراهم کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/149949" target="_blank">📅 23:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149948">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فوری / گروه «کتائب حزب‌الله» عراق اعلام کرد که اگر محاصره هوایی پروازهای ایران تا اول اکتبر لغو نشود، گذرگاه‌های مرزی هر کشوری را که در این محاصره مشارکت داشته باشد مسدود خواهد کرد و تمامی «هواپیماهای متخاصم» را در حریم هوایی عراق هدف قرار داده و سرنگون خواهد ساخت.
🔴
این بیانیه همچنین «علی الزیدی»، نخست‌وزیر عراق، را تهدید کرده و تصریح می‌کند که اگر دولت در راستای منافع مردم عمل نکند، با توسل به هر ابزاری سرنگون خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/149948" target="_blank">📅 23:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149947">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوووری /  دو انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/149947" target="_blank">📅 23:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149946">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
اسرائیل هیوم» گزارش کرده که سفر دیروز نتانیاهو به امارات ۶ ساعت طول کشیده و در این سفر، رئیس موساد و رئیس شورای امنیت داخلی اسرائیل او را همراهی کرده‌اند.
🔴
شبکه ۱۴ اسرائیل نیز گزارش داده نمایندگانی از چند کشور عربی، از جمله عربستان سعودی در دیدار اخیر نخست‌وزیر اسرائیل و رئیس امارات در ابوظبی حضور داشتند.
🔴
المانیتور نیز مدعی شده در سفر محرمانه نتانیاهو به امارات، موضوع ایران «بر دستور کار دیدار» با شیخ محمد غلبه داشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/149946" target="_blank">📅 23:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149945">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
سیاری معاون ارتش: کل مردم ما به عنوان سرباز آماده دفاع از کشورن
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/149945" target="_blank">📅 23:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149944">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ثابتی: حق حمید نیست زندان بره
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/149944" target="_blank">📅 23:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149943">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNKC24E6NUaBT08EciDewplPmdwarMaiLt-9RY4wzYLI8UWAsO6TIbXKnJSy5P8rY_DULCoeNi0q7qa0fdl3VFy_4SwpGfyGfL9za3KA0fbXxpRjRsyARdIiAvs5mWaZuvBLdVns8TlET063Q1EDn98oUEks1iOaU1vtCCizjCYE9yWQF-wDMYH3j2cK1Z27YtCvlTqxqTT1cK-yrYZQ93OuTzcjMEnLCcw_jqipFD-ScvhmRx8d-HanikdAIFBKdXqEWgCv9OAKMz2G99wCcOKCfu8mT52tsZsV-yk06RSNpGp_Fz4sSJjMWMK3-MGq8NruCRvTnrepHGPkPmG0dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: برخی منابع عبری-عربی مدعی موافقت ایران با توقف غنی‌سازی شدند؛ ایران پیش از جنگ ۴۰ روزه هم با توقف غنی‌سازی موافقت کرده بود
🔴
آمریکا پیش از توقفِ غنی سازی به دنبال ۴۰۰ کیلو اورانیوم ۶۰٪ است، پس از آن تعلیقِ بلندمدت غنی‌سازی حتی در حوزه تحقیقاتیِ موثر را می‌خواهد و بعد از آنهم بعید است که تحریمی بردارد، پولی آزاد کند و جنگ را مجددا پس از انتخابات، از سَر نگیرد!
🔴
آمریکایی‌ها دیگر «تنگه هرمز» را امتیازِ ویژه‌ای که به تنهایی واجدِ شرایطِ مذاکره‌کردن باشد، نمی‌بینند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/149943" target="_blank">📅 23:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149942">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18688252a5.mp4?token=jXgaEjvXG5jOjmlGVkSxSdq6dbuibSRLMKSi7EaNxfnNZvUC4lmhaUAxE3t5Lizopw7skhNGsFRj2Th3bBt2zx6UhNbC_G8sVdbZ95KDVRZPV2mZhfQELbGTn2O_5ZGyiRKnX7JT1E9Lt670vj0_vRzIWj1gXwuk3vt9h2qpPAbwGv8R9IzFSjL3J-wmbx5kiSl6WOKFGRL34pnVTTy8ZjzY0czPA2le-7Ai7eKm2E2JNuuzZDTpczUFqphxsR5OZQr23rsOC07sMCqiZFkovuSNA40YgBcI8pzxe0eVpE0ZBMhi1iUA9XdZjp_6gGK3rfWNdNXgnhL5hJ_Gb4MSHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18688252a5.mp4?token=jXgaEjvXG5jOjmlGVkSxSdq6dbuibSRLMKSi7EaNxfnNZvUC4lmhaUAxE3t5Lizopw7skhNGsFRj2Th3bBt2zx6UhNbC_G8sVdbZ95KDVRZPV2mZhfQELbGTn2O_5ZGyiRKnX7JT1E9Lt670vj0_vRzIWj1gXwuk3vt9h2qpPAbwGv8R9IzFSjL3J-wmbx5kiSl6WOKFGRL34pnVTTy8ZjzY0czPA2le-7Ai7eKm2E2JNuuzZDTpczUFqphxsR5OZQr23rsOC07sMCqiZFkovuSNA40YgBcI8pzxe0eVpE0ZBMhi1iUA9XdZjp_6gGK3rfWNdNXgnhL5hJ_Gb4MSHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز مردم ریخته بودن جلوی در میلی گلد که ودشکست شده و پول ملت رو خورده
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/149942" target="_blank">📅 22:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149941">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خب مثل اینکه ترامپ هم تأیید کرده که تیمش از طریق واسطه‌ها با ایران حرف زده   @shahab_gold_trading</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/149941" target="_blank">📅 22:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149940">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ترامپ: ۹۵ درصد تجارت کانادا با آمریکاست
🔴
ترامپ: ۹۵ درصد تجارتی که آنها انجام می‌دهند، با ایالات متحده و با ماست. سهم تجارت ما با آنها در مقایسه با این رقم، بخش بسیار کوچکی است و اصلاً رقم بزرگی نیست.
🔴
ما به آنها تجهیزات نظامی می‌دهیم. به آنها یخ‌شکن هم می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/149940" target="_blank">📅 22:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149939">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ترامپ درباره ایران: اگر می‌خواهید هرج‌ومرج را ببینید، بگذارید شهری را با سلاح هسته‌ای نابود کنند. من فقط درباره اسرائیل و بخش‌های وسیعی از خاورمیانه صحبت نمی‌کنم. بگذارید با سلاح هسته‌ای به ما حمله کنند؛ خطاب به همه آن آدم‌های احمقی که فکر می‌کنند این مسئله اشکالی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/149939" target="_blank">📅 22:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149938">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ترامپ درباره ایران: من وارد جنگ شدم تا جلوی چیزی را بگیرم که می‌توانست یکی از بدترین اتفاقاتی باشد که تا به حال برای جهان، و برای ما، رخ داده است.
🔴
در حال حاضر، اسرائیل نابود می‌شد
🔴
اسرائیل وجود نخواهد داشت، منطقه خاورمیانه نیز از بین می‌رفت، و سپس موشک‌ها و بمب‌ها به سمت ما و اروپا شلیک می‌شدند.
🔴
و من این [جنگ] را متوقف کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/149938" target="_blank">📅 22:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149937">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ترامپ: تحت ریاست جمهوری بایدن، شما برای بنزین بسیار بیشتر از آنچه که اکنون پرداخت می‌کنید، هزینه می‌کردید
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/149937" target="_blank">📅 22:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149936">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bda947fd66.mp4?token=pUZTd8MpxrPi7k0NHWhdUet_ZZ-4iTvKRI3jFu8tZWm41xLWLL0ERV-1ZHxHMd74elZRZt1EWQkXiq2euReRIwYG-gPpXwKRH6wigE8z3N_7L6s_wx5bO2al8pxVDPv75asnWhdYPbG0aXKtmEvswVFmftX7TGcTwxgcrJzZMdJ_clnN5h-IgTyeprZygYX8ktr8ZCsn8AZ8ULRPVkaKNSxSh0vUZAsY6Wx4Xj_QbxACEcvw5QbfcVUNJCMOfXKi_CNr6AIlPQxefk1rV-9FONInzPjufvGTp4YYHc6BAQ6Vu7tummgm52Rpw1bgkaFTiHZy2DD27a-64j1Q1DwcTSfFa26Zr5-atbof8VrTiGLIdQDEGbpUC74JN8EBxgBidtX5ullLPN4_Omq0EoF_iV2_o65kst6b00gwFIPskYVvh0PjTtaesAuFs-C5fNKwQeY10_zFjwWCDKej6HHmXymcDZPgkadirhbWFLp2eIb0j8AteJhnhjPEkUM4pt_joAcrNC0LLaHMvfUczz4deTUS0i6tvboPv8O9wVsCmlopcH35c7OXzZ0kRFw-iK3PmXNGW5kzOJqVprj2tk_7jfqjLkQmKHEwFEo6q0DuR2DQeKV_9_ia2W6b5PQaKE1pyeYQqsflQAdQExjDZGktwIH9_YbHQk_vSfxX-tzKlNM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bda947fd66.mp4?token=pUZTd8MpxrPi7k0NHWhdUet_ZZ-4iTvKRI3jFu8tZWm41xLWLL0ERV-1ZHxHMd74elZRZt1EWQkXiq2euReRIwYG-gPpXwKRH6wigE8z3N_7L6s_wx5bO2al8pxVDPv75asnWhdYPbG0aXKtmEvswVFmftX7TGcTwxgcrJzZMdJ_clnN5h-IgTyeprZygYX8ktr8ZCsn8AZ8ULRPVkaKNSxSh0vUZAsY6Wx4Xj_QbxACEcvw5QbfcVUNJCMOfXKi_CNr6AIlPQxefk1rV-9FONInzPjufvGTp4YYHc6BAQ6Vu7tummgm52Rpw1bgkaFTiHZy2DD27a-64j1Q1DwcTSfFa26Zr5-atbof8VrTiGLIdQDEGbpUC74JN8EBxgBidtX5ullLPN4_Omq0EoF_iV2_o65kst6b00gwFIPskYVvh0PjTtaesAuFs-C5fNKwQeY10_zFjwWCDKej6HHmXymcDZPgkadirhbWFLp2eIb0j8AteJhnhjPEkUM4pt_joAcrNC0LLaHMvfUczz4deTUS0i6tvboPv8O9wVsCmlopcH35c7OXzZ0kRFw-iK3PmXNGW5kzOJqVprj2tk_7jfqjLkQmKHEwFEo6q0DuR2DQeKV_9_ia2W6b5PQaKE1pyeYQqsflQAdQExjDZGktwIH9_YbHQk_vSfxX-tzKlNM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: درباره فروش تجهیزات نظامی آمریکا به چین با شی صحبت نکردیم
🔴
خبرنگار: سفیر آمریکا در چین، آقای پردو، گفته شما به شی پیشنهاد دادید که آمریکا تجهیزات نظامی به چین بفروشد. این درست است؟
🔴
ترامپ: من اصلاً چنین چیزی نشنیده‌ام. احتمالاً آنها دوست دارند این تجهیزات را بخرند، چون ما تجهیزات بهتری تولید می‌کنیم، اما ما درباره چنین موضوعی صحبت نکردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/149936" target="_blank">📅 22:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149935">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، درباره ایران: به محض اینکه آن جنگ به پایان برسد، تورم به طور کامل از بین خواهد رفت. کاملاً.
🔴
هیچ‌کس درباره این موضوع صحبت نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/149935" target="_blank">📅 22:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149934">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad829cf81.mp4?token=PZTabsf8CJO45Jxv5IZFn-Knc1IxfM9AdGBrUF1x0XuHl2S1ICgHV97sPTj6cWxDeDoZxpolkW5RLlbqqhGm9-xdgwkvabHnfo2MfWwVfp5zC9BrWwWJX-VvPMPimFT8_H7xSyZZexrulq9J3OUpudiEXiiwjo_MC3xXiUkyjlcg82DcuodZFER9hgVHsZHGKdNO7cz_D0M5oNKVVhVkAupIH-1eGnvYXkDfes-YjIB-_iZrczJNFQXebOd-Jt9pU8JiTwkEKvDaj1gBNDRTnfb2dkwauqzXLXAaSso-RnIhJR2ZfXVG2DzbFuuTkWh25tunT45O0HcySdN_jO6zUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad829cf81.mp4?token=PZTabsf8CJO45Jxv5IZFn-Knc1IxfM9AdGBrUF1x0XuHl2S1ICgHV97sPTj6cWxDeDoZxpolkW5RLlbqqhGm9-xdgwkvabHnfo2MfWwVfp5zC9BrWwWJX-VvPMPimFT8_H7xSyZZexrulq9J3OUpudiEXiiwjo_MC3xXiUkyjlcg82DcuodZFER9hgVHsZHGKdNO7cz_D0M5oNKVVhVkAupIH-1eGnvYXkDfes-YjIB-_iZrczJNFQXebOd-Jt9pU8JiTwkEKvDaj1gBNDRTnfb2dkwauqzXLXAaSso-RnIhJR2ZfXVG2DzbFuuTkWh25tunT45O0HcySdN_jO6zUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کانادا:
به نظر من، در طول سه یا چهار هفته آینده، کانادا با ما تماس خواهد گرفت و خواهد گفت: "ما تمام تعرفه‌ها را لغو خواهیم کرد."
🔴
ما در همه چیز پیروز خواهیم شد. حتی دریاچه انتاریو اکنون "دریاچه آمریکا" نامیده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/149934" target="_blank">📅 22:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149933">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3cbb91c.mp4?token=C3aJcaWwiB8TQKi1zWdG9zRjcmOeNYy4kTYYVD47W7AD6nIi8vmxynoempZnMaN8-ZkfoU0bVr87mdBJaY4dHVQx2nxjmzHDmKISM9W6EXjM64Hb7l-Qt3eb8Vk6QoOF0aXZT18nkWqOHJ3aKIcJP2gqmSR2kpNLGPDPHaXFCen4HAfKMTph5AXWHNaQBEWtb5QVe36WIiaTtVy4VEqxREV2HLsFhzSaLSHlsLvt0ynb8i3zOkaLuIWBtdcHVjTZD3BpWoWrRPGt0g9VbZrpwzv5acjzjp6JUHsu5LNGfNLjm7HYDe-PFbsg8IOlz5Z5unCwM-U5CtL99tEBC7K7Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3cbb91c.mp4?token=C3aJcaWwiB8TQKi1zWdG9zRjcmOeNYy4kTYYVD47W7AD6nIi8vmxynoempZnMaN8-ZkfoU0bVr87mdBJaY4dHVQx2nxjmzHDmKISM9W6EXjM64Hb7l-Qt3eb8Vk6QoOF0aXZT18nkWqOHJ3aKIcJP2gqmSR2kpNLGPDPHaXFCen4HAfKMTph5AXWHNaQBEWtb5QVe36WIiaTtVy4VEqxREV2HLsFhzSaLSHlsLvt0ynb8i3zOkaLuIWBtdcHVjTZD3BpWoWrRPGt0g9VbZrpwzv5acjzjp6JUHsu5LNGfNLjm7HYDe-PFbsg8IOlz5Z5unCwM-U5CtL99tEBC7K7Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
اگر می‌خواهید آشوب و فاجعه ببینید، اجازه دهید آن‌ها یک شهر را با سلاح هسته‌ای نابود کنند.
🔴
من فقط درباره اسرائیل و بخش‌های بزرگی از خاورمیانه صحبت نمی‌کنم
🔴
اجازه دهید آن‌ها ما را با سلاح هسته‌ای مورد حمله قرار دهند، برای همه آن افراد احمق که فکر می‌کنند این کار درست است.
🔴
آن‌ها دیوانه هستند. هیچ شکی در این مورد وجود ندارد. آن‌ها آدم‌های بسیار دیوانه‌ای هستند. من همیشه به آن‌ها می‌گویم. من می‌گویم: "شما دیوانه هستید، مرد."
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/149933" target="_blank">📅 22:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149932">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2335881783.mp4?token=BKQQqQC9CK2hprO0FBaaJUGEEa3QS1t_zeg2SGVHTygPc3qoc2ZcliG0q2llg7SgZx9TpidQ-RChaU7-09lcBTxHA7LHNcwd3odfdPZfDNn4JNlDIvTLQH3bXtUrqo1cxcgUV-e-RNLAo2XG-tnZvPAL-RLsABlYj4TV7xWbDvbjGHYZbPd4TRnIcf7dKaTN2P_0jkR6BvapFYk_6Odb4UJHtJG7C9m-avN78_6dhOBvjzAmbBriLRCyWNFD_bsXY6obICK1KjhP5kr56F6q-bJ2Hf-LuLZ6CKCUDujGStjYpKW-Q5E7FIRXdDaSo_nr_sVYx9-Um7Qv7M_JshfxAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2335881783.mp4?token=BKQQqQC9CK2hprO0FBaaJUGEEa3QS1t_zeg2SGVHTygPc3qoc2ZcliG0q2llg7SgZx9TpidQ-RChaU7-09lcBTxHA7LHNcwd3odfdPZfDNn4JNlDIvTLQH3bXtUrqo1cxcgUV-e-RNLAo2XG-tnZvPAL-RLsABlYj4TV7xWbDvbjGHYZbPd4TRnIcf7dKaTN2P_0jkR6BvapFYk_6Odb4UJHtJG7C9m-avN78_6dhOBvjzAmbBriLRCyWNFD_bsXY6obICK1KjhP5kr56F6q-bJ2Hf-LuLZ6CKCUDujGStjYpKW-Q5E7FIRXdDaSo_nr_sVYx9-Um7Qv7M_JshfxAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره دیدار با شی جینپینگ:
به نظر من، اگر بخواهیم این دیدار را از 0 تا 10 امتیازدهی کنیم، من به آن 12 از 10 می‌دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/149932" target="_blank">📅 22:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149931">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
خبرنگار: آیا رویداد مربوط به پایگاه نیروی هوایی سلطنتی بریتانیا در فیرفورد  ارتباطی با ایران دارد؟
🔴
ترامپ: «ممکن است داشته باشد، اما باید بگویم که از اینکه آنها این موضوع را علنی کردند، تعجب کردم. من این کار را نمی‌کردم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/149931" target="_blank">📅 22:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149930">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ درباره ایران: «ما خیلی زود در آن جنگ پیروز خواهیم شد. آن جنگ تمام خواهد شد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/149930" target="_blank">📅 22:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149929">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171bfa07ec.mp4?token=K5lKBxKzIlVr_FZEPMHQvKEtdWTZNX84R2iWhkLAY9kIBLHlLnwgNK90mqnRUvkNSJ_IU5_jC7aOjIgmX9Z6qh7KJllUxns87IL8ejhXfXhLTqq64Nza5gbdFXVqulUB7XPMM1hIby4bIKY1cvMDFMTvyU3j0_00pBd0Q3iA8qmvRhH4JYk4kVi_ETsPZrYDr5QAQDXe1G78BE-7S_d5JACHJSAZCiqNVvxt3GVGoSF_FzqX_YyKS0KrSwt0ZRb9C7gzdHyrAL3SJp2eM7XCeNJ97t3mRj4eT05I6m-HHzcm0A4UrDfrZvyDDfAgpcxqn4SHSvSuuS1W6b-vLaDlcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171bfa07ec.mp4?token=K5lKBxKzIlVr_FZEPMHQvKEtdWTZNX84R2iWhkLAY9kIBLHlLnwgNK90mqnRUvkNSJ_IU5_jC7aOjIgmX9Z6qh7KJllUxns87IL8ejhXfXhLTqq64Nza5gbdFXVqulUB7XPMM1hIby4bIKY1cvMDFMTvyU3j0_00pBd0Q3iA8qmvRhH4JYk4kVi_ETsPZrYDr5QAQDXe1G78BE-7S_d5JACHJSAZCiqNVvxt3GVGoSF_FzqX_YyKS0KrSwt0ZRb9C7gzdHyrAL3SJp2eM7XCeNJ97t3mRj4eT05I6m-HHzcm0A4UrDfrZvyDDfAgpcxqn4SHSvSuuS1W6b-vLaDlcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: حال شما در ونزوئلا چگونه است؟
🔴
وزیر ورایت: ما هر روز پیشرفت داریم.
🔴
ترامپ: هیچ‌وقت چنین اتفاقی نیفتاده بود. این یک اتفاق فوق‌العاده است که در حال رخ دادن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149929" target="_blank">📅 22:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149928">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فووووووووووری/نیوزنیشن: یک توافق ابتدایی میان ایران و آمریکا حاصل شده  @shahab_gold_trading</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/149928" target="_blank">📅 22:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149927">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c729dfe11a.mp4?token=g7dg9GmAeO0-yfIPenPcrM2M0BySqvEyFXAQNAXf2KUkMdcgul0oL8eC362xgRDk5AgMlhdVW4tGuxlgeDpdf9gSqN3-nG6VUAJvXoE6ZuvO9FOoukHUYE7G3hOVBPgde5IdSn-vEbXV6Y33qH-wDFBsGvwsB42ZtTY30Lqmq1b5lFKdHK58Xxtm-f6Aeww-rWkpnEL5vYnlRurYPceWs6z9ETTdx1tJslMnn93HdX2dh3262G_ZKENFvI55D7BkUJbJko7NwVdlwDHeUZRW4E3rkKVLOdJyHnko4wZ0oMYChBLspN158L5QZcDfMHKv9BqJCj3EyRjTSQTJZK44fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c729dfe11a.mp4?token=g7dg9GmAeO0-yfIPenPcrM2M0BySqvEyFXAQNAXf2KUkMdcgul0oL8eC362xgRDk5AgMlhdVW4tGuxlgeDpdf9gSqN3-nG6VUAJvXoE6ZuvO9FOoukHUYE7G3hOVBPgde5IdSn-vEbXV6Y33qH-wDFBsGvwsB42ZtTY30Lqmq1b5lFKdHK58Xxtm-f6Aeww-rWkpnEL5vYnlRurYPceWs6z9ETTdx1tJslMnn93HdX2dh3262G_ZKENFvI55D7BkUJbJko7NwVdlwDHeUZRW4E3rkKVLOdJyHnko4wZ0oMYChBLspN158L5QZcDfMHKv9BqJCj3EyRjTSQTJZK44fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : اگر جمهوری‌خواهان اکثریت را در مجلس نمایندگان و سنا به دست آورند، به هر فرد بزرگسال پنج هزار دلار کمک خواهیم کرد. و ما می‌توانیم این کار را انجام دهیم.
🔴
دموکرات‌ها نمی‌توانند این کار را انجام دهند، زیرا دموکرات‌ها هیچ درآمدی ندارند و آن‌ها ما را به سمت رکود اقتصادی پیش خواهند برد. آن‌ها هیچ پولی نخواهند داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/149927" target="_blank">📅 22:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149926">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbaf1d565a.mp4?token=cNdEaNdIYNba_U9OthdoPZsFnAP2kFGa8JZ3ADgTcI12GCKQaXgmmS1kmGVlDouJYi85ViKfGC2tDg1iA_edwraDgYlubvcdllAVOvftkVg7kBPCVXZHblzWMyeIZdnkjLv5ofetHaU2Yrmqj7XBW-ut_C79zoTZnuJNXR8-cggba7kxNS5c3dSgfCvnet6z1bYbXpJZxf0-_nfp-2dp5dUp6_pGnf1w1kqXrAkSB9h1hflS11S68Qn8yrwQyjvS8eeaQCYT1VTM6v_mzoDKWXJRkD8ep6X9HFFpWesMblvUiSjBwInQ92goNI6cXq9tPsVWMGx5lhsU-gyeFdjriw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbaf1d565a.mp4?token=cNdEaNdIYNba_U9OthdoPZsFnAP2kFGa8JZ3ADgTcI12GCKQaXgmmS1kmGVlDouJYi85ViKfGC2tDg1iA_edwraDgYlubvcdllAVOvftkVg7kBPCVXZHblzWMyeIZdnkjLv5ofetHaU2Yrmqj7XBW-ut_C79zoTZnuJNXR8-cggba7kxNS5c3dSgfCvnet6z1bYbXpJZxf0-_nfp-2dp5dUp6_pGnf1w1kqXrAkSB9h1hflS11S68Qn8yrwQyjvS8eeaQCYT1VTM6v_mzoDKWXJRkD8ep6X9HFFpWesMblvUiSjBwInQ92goNI6cXq9tPsVWMGx5lhsU-gyeFdjriw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: امروز، با خوشحالی اعلام می‌کنیم که شرکت "مسابی متالیکس" بزرگترین کارخانه فولادسازی در تاریخ آمریکا را در ایالت بزرگ آیووا خواهد ساخت.
🔴
این کارخانه، بزرگترین کارخانه در جهان است، اما به طور قطع، بزرگترین کارخانه در آمریکا محسوب می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/149926" target="_blank">📅 22:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149925">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d586ff7959.mp4?token=emGrM8MN1nSuU5ie9oj2dB2v4b1dNkfIPxByGJ-ti1MlhrUjCncEfemvoYk5tXY-VJfmLsgO39r7OHShgZGiq4dUhHqYzp20Vj1tCe0vE-TGalCAZGnJ7cOZoS08vR0E0jrTRHJsNZtVoqsAhJ9xLzZVtWHbmbF6nY0uI0vsPOVobodEZmro3l-BIDguggc5sqXGy8p5D2tQryzFpGRB4tq6CpwJuT3IMshDLAJSeRIL9VrT_1USNCYCbekcxnCQAOMa8Zv_hGtqFfj4916CmK9R23FG9hdzctq89U1Pmb8lM2b0qegIN6vGxZcbANyo9xqjl3fS798BMsNAeF2nDpxbfPS_RZ5rMpSFNIw5EpoSL6q1BSmHAcgyq7ae1aA_nsLTZSxgjrnvnXYoIc6EPtaO-7mcSrexTul-VGVMrydu1ThIX8g_342jDosMfwBQSuzV2XrRCeYyVzItpzJguqF5YupLKHw7xgKMbqtHhL0YU9zvutVUMCcVyvN1jNG_KX6b5gDs8162WYThp8B6X-vvzuZWy-3NN0EtpiASCNv4ChPMuZHxVAlNudSrFS4y_kzFfDY5zQya6PMi6vhEq85JAPIdhFuZE6b_ObF6TcPsSt5Ty_8IJo19BmlwgXez6GCZcdro1gIxbaFcP0p25oGHOhfFwXzt9bfSYMRGomE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d586ff7959.mp4?token=emGrM8MN1nSuU5ie9oj2dB2v4b1dNkfIPxByGJ-ti1MlhrUjCncEfemvoYk5tXY-VJfmLsgO39r7OHShgZGiq4dUhHqYzp20Vj1tCe0vE-TGalCAZGnJ7cOZoS08vR0E0jrTRHJsNZtVoqsAhJ9xLzZVtWHbmbF6nY0uI0vsPOVobodEZmro3l-BIDguggc5sqXGy8p5D2tQryzFpGRB4tq6CpwJuT3IMshDLAJSeRIL9VrT_1USNCYCbekcxnCQAOMa8Zv_hGtqFfj4916CmK9R23FG9hdzctq89U1Pmb8lM2b0qegIN6vGxZcbANyo9xqjl3fS798BMsNAeF2nDpxbfPS_RZ5rMpSFNIw5EpoSL6q1BSmHAcgyq7ae1aA_nsLTZSxgjrnvnXYoIc6EPtaO-7mcSrexTul-VGVMrydu1ThIX8g_342jDosMfwBQSuzV2XrRCeYyVzItpzJguqF5YupLKHw7xgKMbqtHhL0YU9zvutVUMCcVyvN1jNG_KX6b5gDs8162WYThp8B6X-vvzuZWy-3NN0EtpiASCNv4ChPMuZHxVAlNudSrFS4y_kzFfDY5zQya6PMi6vhEq85JAPIdhFuZE6b_ObF6TcPsSt5Ty_8IJo19BmlwgXez6GCZcdro1gIxbaFcP0p25oGHOhfFwXzt9bfSYMRGomE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وِس استریتینگ.، وزیر دفاع بریتانیا، درباره جمهوري اسلامي ایران:
🔴
فکر می‌کنم حمایت از اقدامات دفاعی انجام شده توسط ایالات متحده درست بود.
🔴
بی‌شک درست است که بگوییم جنگ در ایران جنگی نبود که ما آن را انتخاب کرده باشیم. اما از سوی دیگر، هیچ شک و تردیدی هم وجود ندارد که ایران یک نیروی شرور است که بریتانیا، منافع ما و متحدان ما را تهدید می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/149925" target="_blank">📅 22:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149924">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/149924" target="_blank">📅 21:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149923">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚀
کانفیگ v2ray نامحدود | چند کاربره
🦋
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
📍
نامحدود _ PLUS
⚡
:
🇩🇪
🇫🇷
🇮🇹
🇸🇪
🇦🇹
🇦🇿
🇵🇱
🇹🇷
🇺🇦
🇦🇱
🇦🇩
🇫🇮
🇳🇱
🇺🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇲
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
برای اولین بار در ایران
👑
کانفیگ ها بدون تبلیغات هستن
🚫
تمامی لوکیشن ها قابل استفاده در جمنای
✅
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/149923" target="_blank">📅 21:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149922">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
خبرگزاری عراق: ازسرگیری پروازهای شرکت هواپیمایی عراق به ایران از طریق فرودگاه نجف، با تلاش‌های مستقیم نخست‌وزیر انجام شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/149922" target="_blank">📅 21:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149921">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
امارات متحده عربی سفر نخست وزیر اسرائیل به این کشور را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/149921" target="_blank">📅 21:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149920">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsL5erk3FQh9CRmVKyZHYl6k2Pe8gWflmlNXtwxaQHchu_JFsgjo4bDT7YreOAGyM7TzkISSOeb8gK3ENtzBHUkBG9xTtqS-AxInS1J8TXlpGCR8WQFrMiAcBKxCRHZq8yfG6VDR9N6HzSO9OGQXwif5KTySVPYfL09PIFoxUbBGQQIpakjG9duLapLS5dNzxvVdoiXblxrYwgjMA75I3923JKuwD5ri9F3o3HrONLIsDQ3g8pn8yjAsB3rerpGfyROXvYetxZVioZQu7t9REx4H0h4NXEr1H2nKy4z4D9mIRlFyBx0YnfDZP6nASHQsMeMXi9MAEJRA1pA6lcTHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار آکسیوس :به گمانم ایالات متحده می‌خواهد شاهد آن باشد که ایران بازرسان آژانس بین‌المللی انرژی اتمی را دوباره دعوت کند؛ کاری که در جریان مذاکرات سوئیس متعهد به انجام آن شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/149920" target="_blank">📅 21:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149919">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DK8UAHSriz2gksvi1c1xeHglLPV0iS4TUu5ciYM17IP5NfOGtLbkEAR0Y0qKoTaLwxp58MnxaWJUBo4QzH8RL2fCn2e8OFGOUn1pI_eIdMfyXxeASr5-QC3xeS_Ei2Mv0_YuLgDJptFhN_0ltBDhotCXmXDyey8qKy_o3vNIAZzWiLpO8by33Ssv60EceqRUq-6DmyFNFHuhZ_2uNuVyayVAEsU86Q7DrRxTrmYxo6PgGLG1RZuK6P2-KqmrAjYy_yK-KXrr-TwdaRVM6RmubTfCn7iyBsjU86ARM85ps-VjthcLxjXP4AKSvLzfJKpIH7KrUypnvVl5ul7VUjAJCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جایگاه هند و چین در تولید کالاها
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149919" target="_blank">📅 21:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149918">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXZ3QFcgMqwSQBviVCpJBkVGQUd3vMbuDQq6YcJODCRP8TblKm6qu7Af_dugwCMZw0kJw-GUHaOXxhB0cNZwSEnFlPe2IJFMa7SSO7FMFqFX8QZ84jJVdx_OMWTLwVBJl7Miq9LDQAlZ5HfxZHgUf0MAoRGcNNm3ov8A70cI38cgIzEbRS8RL299CoUFP4xjYRtcc1eh9__xIKRlymbCjOn4vRZzU3qSQel3N-q2FLCkSo0cInmyuIRq02RrXhP8gxfrJUdqv550mOTIiW0Jq8kWtidIRegi67F_kDIeXdLp5r9KYyTYeCJN4NHZdc_jf56e8WJYnYiGwU2-Agl4KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سقوط آزاد درآمد دولت قطر از نفت و گاز
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/149918" target="_blank">📅 21:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149917">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSHL0zXjrClIiX_epUBptjAxvOqQneRyby__8ssnMmB2tAC_oEcr63lX9EDJGt6f5mcRIsZVkpTdZXAnXBAL5C37I1huo6gNv_oZz7-nhTEMPpuVdBp9kylVB11wVLbJMYH_ktk-lPx4ftHrVNBe-YyaHkrzUT92Tu-p6bYweDJsF3zsM94g9nSi-rG0uqv4D6IZV6UDA1rgK6llEBWiV8s1YMqY9bWnZd2prSGkqn-Gmcz5lJs9PfVUOHzWNxK6m4Wq9bQUWEpN09lfJ5XVlH1Tm6qR39IlLIv8Jm6tgIbKGBJEAoqyOL0wUImqco4q5v7G3WWm4OsjJakjjr7Mng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکات بسنت: عملیات "منزوی اقتصادی" باعث شده است که ارزش ریال به پایین‌ترین حد خود در تاریخ برسد.
🔴
ما به تضعیف توانایی حکومت ایران در تأمین مالی تروریسم و توسعه سلاح هسته‌ای ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/149917" target="_blank">📅 21:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149916">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیلی: نهادهای امنیتی اسرائیل در حال آماده‌سازی برای احتمال از سرگیری درگیری‌ها با ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/149916" target="_blank">📅 21:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149915">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF): لحظاتی پیش، یک موشک رهگیر به سمت یک هدف هوایی مشکوک که در منطقه‌ای که سربازان IDF در جنوب لبنان در حال عملیات هستند شناسایی شده بود، شلیک شد.
🔴
جزئیات در حال بررسی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/149915" target="_blank">📅 21:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149914">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
نایا : شرکت هواپیمایی عراق، پروازهای خود به فرودگاه‌های ایران را از طریق فرودگاه بین‌المللی نجف از سر گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/149914" target="_blank">📅 21:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149913">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: نتانیاهو در سفر به امارات نه فقط با مقامات این کشور بلکه با نمایندگانی از سایر کشورهای عربی دیدار کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/149913" target="_blank">📅 21:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149912">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری / فعالیت‌های پدافند هوایی در منطقه کریات شمونا، در شمال اسرائیل و در امتداد مرز اسرائیل و لبنان، مشاهده شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/149912" target="_blank">📅 21:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149911">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
مطابق گزارش خبرنگار شبکه الحدث در پاکستان، به گفته منابع، ایران با توقف فعالیت‌های غنی‌سازی موافقت کرده است، در ازای آن، تحریم‌های ایالات متحده علیه ایران کاهش خواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/149911" target="_blank">📅 20:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149910">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
یک مقام آمریکایی در گفتگو با سی‌ان‌ان:
مذاکرات مثبت و سازنده‌ای را از طریق میانجی‌ها با ایران دنبال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/149910" target="_blank">📅 20:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149909">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
عضو هیئت رئیسه مجلس: ما قدرت چهارم جهان نیستیم، قدرت اول جهانیم و تنگه هرمز هم ناموسمونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/149909" target="_blank">📅 20:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149908">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
حوثی‌ها (انصارالله) اعلام کردند که عربستان سعودی در ۲۴ ساعت گذشته، ۳۸ حمله هوایی و موشکی انجام داده است. این حملات با استفاده از هواپیماهای F-15 و تایفون از پایگاه‌های هوایی خمیس مشیت و طائف، و همچنین موشک‌هایی که از مناطق نجران و جیزان شلیک شده‌اند، صورت گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/149908" target="_blank">📅 20:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149907">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4HsMC4zqk5VAjuzuOUEiKYuwesENWZnBgVNSclD9USAxjMJ-K-IEumsqN4WH7H9x7OJBDLxZ87DIlDLAI3vpvNoAvPx_VmCvDOSIQqoodEHh3cmB-2hW4mrJkflbKOtJOzRJVgTAsycRa8ce5zQ9LKq-hilzCDUkTh8SKTAwkk_Dop9yR1eE1FuPZobeAiuAEi14tXqwFcRqUG9krvUR3iQ0PN-OLrCr9EMTAOKgg4YSIpz4Leb_XgZ3i2vaDH9wdbSjS-uNjgz97i-nOlb-kzxSE6Wti_HQlEiXv9mzbBpzNDgf0TtgrzZkXpL_LTAj6VIaHM9IP6KnB4k65IG7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۴درصد کاهش فوری قیمت نفت در کمتر از  ۳۰ دقیقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/149907" target="_blank">📅 20:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149906">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXDiI45UcXWhcqGf-gaSCmBpZqK1rPcxSIhznS9as72DsTvYMzp419DOEUvSRS_U0V5ztRoAuoV-4NJLBx-MJ9rv0dQWvMTQ7EKnrxsheRlsAu0HjzTpeVZxWVXKDsapPh21jXEV-Gj8RiW_rpNynrxWAtbBwKsOa1ar37W_unW9-cRgmR8Y3kDGO2ux2VzDYSxK-G1auQrGUnkfDCGHDfrzptcjI8aju6-Zl0rSntkLpDSaGAuj7ZfZoJbtuQ0zWg2cWrneZ7JtlmQXlfB7AeUgcYH5R4UTE5KW3eRtz09FUSCn0D5kvNIkb3RBDHy3W9ias8L7MvwHqR6gN7h2wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابراهیم رضایی عضو کمیسیون امنیت ملی مجلس: مستعمره‌های آمریکا در منطقه که این روزها برای شعله‌ورتر شدن جنگ فشار می‌آورند، مراقب باشند که در جنگ بعدی کاخ‌هایشان هم هدف مشروع است.
🔴
‌خبر داریم که برای جنگ مجدد فشار می‌آورند و هزینه‌هایش را متقبل شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/149906" target="_blank">📅 20:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149905">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
یک فروند هواپیما بوئینگ متعلق به شرکت هوایی کاسپین، به دلیل بدهی سه میلیون یورویی در فرودگاه استانبول توقیف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/149905" target="_blank">📅 20:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149904">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوری / مقام آمریکایی به باراک راوید: ترامپ آماده کاهش تحریم‌ها و آزادسازی منابع مسدودشده ایران است
🔴
یک مقام آمریکایی به باراک راوید گفت: «دونالد ترامپ آماده است در ازای پیشرفت ملموس در موضوع هسته‌ای، تحریم‌های ایران را کاهش دهد و منابع مالی مسدودشده این کشور را آزاد کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/149904" target="_blank">📅 20:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149901">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
مقام آمریکایی به آکسیوس:
بدون پرداختن به مسئله هسته‌ای ایران هیچگونه توافقی در کار نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/149901" target="_blank">📅 19:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149900">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
العربیه به نقل از منابع آگاه: امروز مذاکرات غیرمستقیم میان آمریکا و ایران با میانجی‌گری قطر و پاکستان برگزار می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/149900" target="_blank">📅 19:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149899">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
فوری / برخی منابع عربی مدعی شلیک موشک‌ از خاک ایران شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/149899" target="_blank">📅 19:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149898">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFGDyKFKHZPaV9Yg5sBonOI-MDiszWYLM4-Ohz505SqBcAa9Wj0dUTq8ddCkjFduXAG0SI3MFMmmtr-5gmtU2L2NpeNqft88pnvhIIbIkBn7nz3FMalQmT5wk49ISMxE6DLFnQyDMNVtMU25qfSq8VIN3q9CQniyMe8RmvBCYmDArD0t5XVuxojH3yv1VxHyiiDOpUnzwBI8UQyTfQrAbJF5MlLDFFENB05pAfihSRgvOgkXOOtRG_G_YhAz8VNyoHEMOYyhYo48MdbYuqZgdeMAdDoxad0sKuZ1bsssAwYSwXXlANAzMQBw6YYSj1ftA3kPoZSt17cUdKKW3TZswA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت جدید خاویر بلاس، ستون نویس مشهور بلومبرگ: صادرات نفت خام از عربستان سعودی، عراق، کویت، امارات متحده عربی، بحرین و قطر (از طریق تمام مسیرها) با هزینه‌های هنگفت و با کمک نیروی دریایی ایالات متحده، به حدود ۸۰ درصد سطح پیش از جنگ رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/149898" target="_blank">📅 19:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149897">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">میانجی‌ها امروز یا فردا مذاکرات جداگانه‌ای با آمریکا و ایران تو نیویورک برگزار می‌کنن ولی بعید میدونم اتفاق خاصی بیافته  @shahab_gold_trading</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/149897" target="_blank">📅 19:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149896">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
رویترز: در چارچوب دیدار شی و ترامپ، چین و آمریکا بر سر کاهش تعرفه ۶۰ میلیارد دلاری کالا توافق کردند
🔴
چین و آمریکا توافق کرده‌اند تعرفه‌های اعمال‌شده بر کالاهای وارداتی به ارزش ۶۰ میلیارد دلار از یکدیگر را کاهش دهند؛ اقدامی که طیف گسترده‌ای از محصولات کشاورزی آمریکا و کالاهای مصرفی و خانگی چین را دربرمی‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/149896" target="_blank">📅 19:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149895">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
رسانه‌های سعودی: امروز مذاکرات غیرمستقیم آمریکا و ایران با میانجی‌گری قطر و پاکستان برگزار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/149895" target="_blank">📅 19:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149894">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IThnmCfew2bpEshRSMLhnjzHxQYAoBBFCAhjK5tqeqPptHcmXa7Myz4Erg1eDxM_gcphTJJSF9FxJs8L_iSXzc5wlLY1JTRXAuWhKw5wRoRf2nU_vNrVsoNPCywnUHTD5RvrzindlqKbHNtadcgBGAunow3IqDAaj25ynPS4fWGfysDIqpo6DG6ZNrv83XTlT8Ck7KwyccsruTekXCTSdrYFz-gfwDQcVjqE5EAXwtJVkaizjmPI_aDlwpdSS4v3ay4juyBXUzb1JJAbt2gZd4Vm46yp4qNsdvrfAfXiLM4wkN0LlIEF6atIsLetrwFlcmGJHr5i4LAJVyavb8VNJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز امنیت دولت لهستان در منطقه لوبلین، در شرق این کشور، هشدار حمله هوایی صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/149894" target="_blank">📅 19:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149893">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
هم اکنون دیدار عراقچی با میانجی‌های‌‌ قطری
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/149893" target="_blank">📅 19:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149892">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ایران رسماً از محدودیت پروازها به ایکائو شکایت کرد
🔴
رئیس سازمان هواپیمایی کشوری: ایران با هماهنگی وزارت امور خارجه، اعتراض رسمی خود به محدودیت‌های اعمال‌شده علیه صنعت هوانوردی کشور را به سازمان بین‌المللی هوانوردی کشوری (ایکائو) ارسال کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/149892" target="_blank">📅 19:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149891">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fl675tpzapdALl09SpKMjn7jKhJGXix9NNONeA4gq-HmXeUjMUqlT1SU25LWMu9myCFiBwRlVVtCgK8Adikm9MLKNRSOrhMGRWWySOpscFs1Cc27TpyJcoV6gmepk4ecvZzi48Dqx4swsxjBrB0JA_HONrG_4zs1WWDEeNm9MXCIljTwdkg8ECGBPou7oPxJw5GS0WScyh2jpOoXmVQbUu5ucF7vRjr24EbJ5QFJlHMZ2B2vFePYRtLkWiOne4rr4nIFLzZfppIelb1upUbk3crOUPgKnWoLknUf9b_NIMtdrR7eJVuRPgwunqEnnCn39p-5ZorOAm0_n6gtC1CXSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر هوایی از غزه قبل و بعد از ۷ اکتبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/149891" target="_blank">📅 18:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149888">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z2Z2LFRn7wCkrNaMsdIjL19o1UbGHAQBDAYzJh16d0-eg687iuiShzXAJSuITw7OplLGwlhID66_Uf2Lv3ZhIDI9idaq2fhU3J0n1OFu0UqNtW-QmRpzeZUqvBiOl2NrXzNdwceSBLuZtqerDWAv4LgWI-OjCHy9r6q-AGJCYO27nj1pbzItROlUFBJmW3tpxwdMjE5qsW5DEignByN82mH2vPORoCPJE9UAKc5dz1ez5EV55xeG1ZBTFi5YGiT5j8S3e9_fpGnhLV8cuVRf75KgLjGgo5ByykHKavjv6k_lrTSSn9Xbjv45QgcmGOIQIMI6XSLO9onZokVFnHOwoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P1Z7FlFoHINfUvVf_ZcTk_fwhlt9uR5MuvxFcLqz8gmlDCfN7weY5FZvMSyayNz7xBV-3Wstg_1SfdjstUuLmg5aAzIeiqLDOJwNkPusuo5OUC4I3p5a1md5ZnYaSBl3TVUc5VEP6UqIUWpqv1xd2x_QpxqK-o6nLJIxcz9kXC4dhhR7BSug8EzIDBzOUNvh9tyR5xEbsdRklz3XX1ZKj-GOGg89VsjnbbCFZIwFgFOnSqL_SHo-FD7pUErjZVVNWpVIJh1yryuUc5DE0alUCHYOLWFjpd4QTa1b4FEOyku5IJc3Qdz6bCl1wZBZDUGh69e8T-TpMz7Aeu5l8NVNqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8eZX-LVUQaXli7gPQFGFWNsrz2DR9f9-130ChdOoMaPoFnVQgozfD7nD1ZIzoeE92we-mWFztvFR0Zpoh4vISTEv8KuUuIEq_mIqBsbmbTuaPpdzEQA73dGIjTwtB2LzJNpdBFTUH1UWbG1hA5251Lu0vo-3xADaAmMB5hqtUGD_0o3mE1jrFTDYE7ASQ9OkGFZFp_SE9EGSxvb7AJOKjoJNy-Srj6U6M-G-v2xaGpsJM4ytGbRYTlJ4fOn91EqFtwcDPMyv2bvqsyucQZ21V8QO-OEZZsTdQfIE4OnI7NktEiBgpSfHf_dB7Gf_UBQUplz8JQ38VK1VTyd9FHlOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات هوایی اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/149888" target="_blank">📅 18:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149887">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvnmW2-MSkA8MNHnYfIwuD6nPqxjV1QtXEgYB4Gk9J8S2qf9O45pM2_LMYpRk35YXWs2mEgxkjmlvF0kW_TuFtIIZVCrkkOsrtM2A5NmOvJC1G6BTo3Oype4nmeyLtcfOkMR8r8mTc2saZg8sRnWT7En4joLANybiM16sEjQ4uNN7RD-7DUPxcwWQ_67AByG2Q__nWpCuzPVfzMNTCzP8nA94q7Wt7Q2fkHkhfMB5-C_5p-onRbV-q-MOMg0I5oqm1NdxftusHI-9Q8wE4hqebri--PEZQPLe-W9igt33tod4tyoVnTuea3TxZc41-yNculb3mbyK3cwKaZnYLAtPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نواف سلام، نخست‌وزیر لبنان، در واشنگتن با مارکو روبیو، وزیر خارجه آمریکا دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/149887" target="_blank">📅 18:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149883">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hoM3Hi3ARFS1PSPmD-ihtUzmbk0_-fLED2y-gwedoBKavCdZ-Mi9mrBpPOYTOVt1lZvZ0hh3zR45kuK3Jv4QoIN1G7z5JpVSz-pEDL4kZ30y4Cf0W56OQ1x6kahVukbQZgLE5er0Ja6LsXEjEayniF1_7q9RjrIBFQkSfb0OrS_uLFEOFqHeeqUK0RD5u4YaFcmnuNTTEFTVoTZRRdZElXylZTqAiVzbhnGp6uXUQZny2JVUs6QfI69Clg-MJQm6h1djxyEGAKPwvnh7H7K-5uUKoP0jo_Jt0OACyOkNzhfqrQCrqXex-pyc-fEhkybU1kGbWDggP_E0NHJIPbyY3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W_HqvR-mLbimLEMHefdIRWMdjZ0H22sD1UtgwsyPUtZSqpFOVcnvO2k8q0qpVaY4qsplRfhBnKnx5TaE0yai6OykOuFglWDwR-AMJacIto4jrdMekSOYxXQ84xKpWuKe9e6zI2LMkYFhGQxnnt8AEiAXTOylwgYYYAugU2SKTCA-5pZd6dqe3yMajT88vqMBSm3Wyw8Kjz2M5BUK2YhN_Lag2EdkZyb-1nZ9o33828XsXL9XSHWTSF0w1FQeErRMOI32Flz8OmUwpPEMxAPrUCNzf6vLyOWVBfWBfO4s7mu8w-f2exQ3tguSi-40MEDlUag0vOqGVr7gJuZNq8Y6nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rdx521EaT8wbMnVqWGVLzlkdcVPcxxskiOuivGums605BZcPhJDFZSDHCU3zioxR-5Vw435mqedUJwky1BH3otWATaN6B_mHqMTQzQJWLmDzPrgE8_8cdSDyWR0nNoA23zmimXee0-t4SJqLk1FfYVKRsnnrIjlMw740-h4tKQcJdZt3UlBq5inteyJEJK3ODJdkFglyYGHtaeUGrKZl8nhmdYU2LBve6aGL9H-JkKGyCWfaBdcWEMQkwroi9vUOmAzty32lmQcJJKoSSQ8c2PTkW0wjfMC79vCTIZZEmI0rdv3WywSL-ztM28Or9Pj-QSRfYQy-YRU4XibpHD0yQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T9eRFX6iquoq3feCaAeXA777mvwvTecSFvWwWEd0SahwAnGtLktxQVOEJBiMmZJui3Bf7CwcFueVHIttcsCCiugDSoOb9RLznAM61y-aT0iRiXuEpY0zqYcMiZX_34ddXYwRhnSRQZUexmN_wp9Q1FzDALIO7nNO2pRXjHuJC798HnL6QXWzo5783NonyesYaGByThTpltLOH8qSEMmkSgvdT2MNSvRaQagigDitJbQvanCYjPdUGr3lt5jVxeAJvCwGgcCuWfVIIa5_RSC39xU9LQn3XzRzLOt7jrpsOOduc3NMvE_jwZDz7ua63wol-wUNXzNmP26MAu7nvLOQZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بلومبرگ: خط لوله شرق به غرب عربستان سعودی در حال حاضر روزانه حدود ۳.۵ میلیون بشکه نفت انتقال می‌دهد که حدود ۲ میلیون بشکه آن در داخل کشور مصرف می‌شود و حدود ۱.۵ میلیون بشکه برای صادرات باقی می‌ماند
🔴
این وضعیت باعث کاهش بارگیری نفتکش‌های سعودی شده و امروز تنها ۳ نفتکش بارگیری شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/149883" target="_blank">📅 18:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149882">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">به نظر میرسه قطر داره به ایران فشار میاره تا امتیازات هسته‌ای رو هم داخل پیشنهاد به آمریکا جا بده تا بلکه ترامپ راضی بشه و توافق صورت بگیره  بازارها خیلی متشنج شده  بیینیم میتونن کنترلش کنن   @shahab_gold_trading</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/149882" target="_blank">📅 18:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149881">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce0f9e6ce.mp4?token=Yp6xnI1EuGj7N_EVxJldn8PWGHGdB_rQ3pJKR3kJXRnRV5iR4Jl-w7JMWxuYyZKd7xd3qewIkJQSnaBl3dMVj758NCCbY-wGaipOA3ZlCyVcgCjk17SUBpfyhKhspqiUbo-9yxtVzUTr9T9Bjq1Ydu_rsVCvQum8mEYULfyVBCqWSAiTMiabkp9C-YDowjXXIz8QjrYklFmiUDjG4r5-763Ku6wERP4qDNhVwCmiTlpXC0dCkE7BU4kLoA9Bi-ZZPdinzzMM414ltOzEvixku_L3CjUNt9KKZyTmnzZ0_NVYP3dA2XYHltJwdD5EARUbJPu2gBV4BU09Gi6HuTvsL6yWd2S1Dl3xxQ5CsKbdtcTykgpm1H-8SEjHvN4CW6bBW9LiO-0W8yxrcEC_KIy3KXvPQMUdl9xmbCyau6EPHkcsuYKnqk2dQgk5tKD9bZUqnKdjL_vQf053o8ubDFNwrin5TOZvRuy3rz9g2UJ1e_b9qy5MLLsH-FnHqkoL6lwuP7hxycqyY1-NeXUTdvGAXtvwHh4jKh9hV_0q5-s9UF-Jms0LoOzc4qwLGrnQCm3LJefH3QyyKHlV4W3loJS83sY1y2BtYjscsFNnKF3SCfJN3vuScKl4ASZz6WJRypCMHR5RhQcPZg3351xdXHdTKniE4bZ2qIzPFXtUfs-83Uo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce0f9e6ce.mp4?token=Yp6xnI1EuGj7N_EVxJldn8PWGHGdB_rQ3pJKR3kJXRnRV5iR4Jl-w7JMWxuYyZKd7xd3qewIkJQSnaBl3dMVj758NCCbY-wGaipOA3ZlCyVcgCjk17SUBpfyhKhspqiUbo-9yxtVzUTr9T9Bjq1Ydu_rsVCvQum8mEYULfyVBCqWSAiTMiabkp9C-YDowjXXIz8QjrYklFmiUDjG4r5-763Ku6wERP4qDNhVwCmiTlpXC0dCkE7BU4kLoA9Bi-ZZPdinzzMM414ltOzEvixku_L3CjUNt9KKZyTmnzZ0_NVYP3dA2XYHltJwdD5EARUbJPu2gBV4BU09Gi6HuTvsL6yWd2S1Dl3xxQ5CsKbdtcTykgpm1H-8SEjHvN4CW6bBW9LiO-0W8yxrcEC_KIy3KXvPQMUdl9xmbCyau6EPHkcsuYKnqk2dQgk5tKD9bZUqnKdjL_vQf053o8ubDFNwrin5TOZvRuy3rz9g2UJ1e_b9qy5MLLsH-FnHqkoL6lwuP7hxycqyY1-NeXUTdvGAXtvwHh4jKh9hV_0q5-s9UF-Jms0LoOzc4qwLGrnQCm3LJefH3QyyKHlV4W3loJS83sY1y2BtYjscsFNnKF3SCfJN3vuScKl4ASZz6WJRypCMHR5RhQcPZg3351xdXHdTKniE4bZ2qIzPFXtUfs-83Uo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چندین فروند F-22 raptor در راه پایگاه های بریتانیا هستند که احتمالا برای انجام فعالیت در خاورمیانه مستقر میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/149881" target="_blank">📅 18:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149880">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
دیوید پردو، سفیر آمریکا در چین: ترامپ در جریان دیدار با شی جین‌پینگ از او درباره خرید تسلیحات آمریکایی پرسیده است.
🔴
با این حال، واشنگتن هرگونه پیشنهاد یا برنامه رسمی برای فروش تسلیحات به چین را رد کرده است.
🔴
همزمان، یک بسته تسلیحاتی ۱۴ میلیارد دلاری برای تایوان همچنان در حالت تعلیق قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/149880" target="_blank">📅 18:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149879">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03bde46572.mp4?token=dZBCHLGOFhM7X-tUkkEX8ifyir303GfrHChgwQ_7CmELG0zNafx_HvGbtoek3FG8NlLhJkYq834pf4E3yw7LKxJDUmOsrzlazFH-SmmD4Rnsx2ujPB5uagt0sXE0VI2t61tFcLLBqYfjSOZWUu772nB6ZyQadoH5CmG4-U-ghijv9Hl2TAt6bUgOwJqF37BNYHqVWDzvzMcJMx2lTs36W3UcqelCLW4O7DskcUivf1KyVk5P-tJW2OzaFtLwJcL6Iw1zlhYtEfyQIAnDkOqBYE4Oa8ZveCdSN4LGsn_BT3YC8e2DzofHJ42B1qsk0KtKDjs3Cee9qk-PvnZnlnBsCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03bde46572.mp4?token=dZBCHLGOFhM7X-tUkkEX8ifyir303GfrHChgwQ_7CmELG0zNafx_HvGbtoek3FG8NlLhJkYq834pf4E3yw7LKxJDUmOsrzlazFH-SmmD4Rnsx2ujPB5uagt0sXE0VI2t61tFcLLBqYfjSOZWUu772nB6ZyQadoH5CmG4-U-ghijv9Hl2TAt6bUgOwJqF37BNYHqVWDzvzMcJMx2lTs36W3UcqelCLW4O7DskcUivf1KyVk5P-tJW2OzaFtLwJcL6Iw1zlhYtEfyQIAnDkOqBYE4Oa8ZveCdSN4LGsn_BT3YC8e2DzofHJ42B1qsk0KtKDjs3Cee9qk-PvnZnlnBsCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کالاس، رئیس سیاست خارجی اتحادیه اروپا: اقدامات خرابکارانه، آتش‌سوزی‌ها و نقض حریم هوایی که روسیه مرتکب می‌شود، همچنان ادامه دارد.
🔴
از سوی اتحادیه اروپا، تحریم‌ها علیه مجرمان و اخراج دیپلمات‌های روسی، اثرگذار است. اما ما باید بررسی کنیم که چه کارهای دیگری می‌توانیم انجام دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/149879" target="_blank">📅 17:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149878">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
رویترز به نقل از منبع آگاه: میانجی‌ها امروز یا فردا در نیویورک، مذاکرات جداگانه‌ای با آمریکا و ایران برگزار خواهند کرد.
🔴
عباس عراقچی و میانجی‌ها در نیویورک می‌مانند تا مذاکرات را احیا کنند
🔴
مذاکرات در نیویورک بر نسخه‌ای اصلاح‌شده از آخرین پیشنهاد ایران متمرکز خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/149878" target="_blank">📅 17:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149877">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s96_4QNrVRTeVbctaiIxPEaUwHWEIIgoI4OmWaUtZbFPFYL-zRBvBPpMVC8A68nkyzWDweHRgYOUDDuQqVKgt80PTTCqZgsvfp8qTGzrZF8SGVKKB3wijAyb9BpgV-T79Kvmq1FctH0y8_1qF25Wh0k8U_q48XgvpZEtOMpC08ZKvPYOQBb3ZsVjmvjCevdCgwNOk0pebaVdvQN-Xo39kjMc7A8IsjDcLdrg9xnWl3sKkj1z-u3eW3Npx0XCoCE1fuC2U1F100pne7MrePVxNXdupYxRAjDKdNG10mKfwr3in3DgK-2hgSRDN2dSy2BQSBKcuJZQR6oYp8k7dPsvjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی: امارات نباید زمانی که اوضاع از هم می‌پاشد، شکایتی داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/149877" target="_blank">📅 17:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149876">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
رویترز:  میانجی‌ها امروز یا فردا در نیویورک، مذاکرات جداگانه‌ای با آمریکا و ایران برگزار خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/149876" target="_blank">📅 17:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149875">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijNrpecv65Be_cGPBMUauVw-tojjy3tznz9IlmUZ3YK2oCrrO-OvNHun6Uz_By-GDrhFBRRYR1zkArbSlqHJDS70rTF3wS8c8Wm3FoYQHWb9mrqe5vxvO_tJLx5fXkyvTJZe8pVO0lCZg0H5w3FakRI2n3oMl7w18xtEUFClhwj0ULkioy5UJqoUCv9Pfcz31Q1CVWSB18OFnCxbHiCi3ikyrFqiLKTXMgUJXIqG82IsXh3t6EEuxDTKzC3DIXYUSIYOpMSYVhzMplIYzzfoiGgHqMYR98cr9-IpD7iGJTliy0elQ4wE4LY7ZLwQqskKzOHN-L3RtXAqj7KSwZW1iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ریال ایران به پایین‌ترین سطح تاریخی خود رسید
🔴
ریال ایران به رکورد جدیدی در برابر دلار رسید؛ قیمت دلار در بازار آزاد از ۲۴۰ هزار تومان عبور کرده و حدود ۲۴۳ تا ۲۴۴ هزار تومان معامله می‌شود.
🔴
ارزش ریال طی یک سال بیش از نصف شده و قیمت دلار از حدود ۱۱۱ هزار تومان در یک سال قبل به سطح فعلی رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/149875" target="_blank">📅 17:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149874">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9798ee16b7.mp4?token=Z_SIeJf9r2W3ypvCFdazeSZw9805Y2icd3GjZJ2cVRJCvY9JSd0iFUHstcaoj07j_iuNeH8K0VPfaSL_gfb6rQ21Nn8SeLngySLl44faWfzFbTX6AiNUsTfgLEsLCY7u5u8RRGLx1nMz1gBkYYpr83kWCMLza3gw48xi2rIqXdnVtzGc2rkji7zjOEGE8rwL2GkatoZikXof9PC6wHQVgiVmfRPBJMo9BufjPOlHLFCUKJCrwDjBWqdSjibLOtNiLVDKAkckE9Wj_5W26FFP8CaK28m-RfSufkFlTYLRQTYPOm0nbyHPbvZymCjiu_YM9h6DX6iSS57Z3xWOr2ylmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9798ee16b7.mp4?token=Z_SIeJf9r2W3ypvCFdazeSZw9805Y2icd3GjZJ2cVRJCvY9JSd0iFUHstcaoj07j_iuNeH8K0VPfaSL_gfb6rQ21Nn8SeLngySLl44faWfzFbTX6AiNUsTfgLEsLCY7u5u8RRGLx1nMz1gBkYYpr83kWCMLza3gw48xi2rIqXdnVtzGc2rkji7zjOEGE8rwL2GkatoZikXof9PC6wHQVgiVmfRPBJMo9BufjPOlHLFCUKJCrwDjBWqdSjibLOtNiLVDKAkckE9Wj_5W26FFP8CaK28m-RfSufkFlTYLRQTYPOm0nbyHPbvZymCjiu_YM9h6DX6iSS57Z3xWOr2ylmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد اوکراینی در تعقیب یک سوخو-۳۰ در کریمه چند ثانیه دیر رسید
🔴
یک پهپاد اوکراینی تلاش کرد یک جنگنده سوخو-۳۰اس‌ام را هنگام برخاستن از فرودگاهی در کریمه هدف قرار دهد، اما تنها چند ثانیه دیر رسید.
🔴
خلبانان جنگنده خوش‌شانس بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/149874" target="_blank">📅 17:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149873">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfLQY7JEX5GVHgnLmfsn8blldiEoEjsz7PuXdeVHrWQhZ9wbD9g20RtaLEkce8ZCTiTcorq6z4eSCTO02qC_6Tas8UT213SeYoulTqg0tfCNWRq9TNsjRpzP93PmR1URL3SqcNBgI51RmUhR7Yz7m5b6RlZtFsd4jCO74KDVJ4POieMEZ0MPYSrG84iNzwnC_znMvfXWUNBNWMFfZ2LaOmXUpHGDAMhYO9VHG4ZkCjbE4K2wTHj8qtHJtI3lU4M7b4sDNBnEcMhEqoVP_gfb0iM7kOiqm2BR9GMExwRiA1r2uHpft6WX9bnwi_f9jVeKvFc9ZEjngm5YWzb6MpoMDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اروپا درباره واکنش در سطح ناتو به جنگ ترکیبی روسیه بحث می‌کند
🔴
اتحادیه اروپا در حال بررسی یک پیشنهاد امنیتی اضطراری است که واکنش کشورهای عضو به خرابکاری‌ها، حملات سایبری و ورود پهپادها به حریم هوایی را هماهنگ کند.
🔴
این بحث در حالی انجام می‌شود که کشورهای اروپایی در حال بررسی این موضوع هستند که آیا اقدامات فعلی برای بازدارندگی روسیه کافی است یا نه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/149873" target="_blank">📅 17:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149872">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
مجید شاکری، مشاور قالیباف: هر کس بگوید ایران تفاهم‌نامه اسلام آباد را به هم زد بی شرف است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/149872" target="_blank">📅 17:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149871">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
دلار 244هزار تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/149871" target="_blank">📅 17:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149870">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ثابتی: حق حمید نیست زندان بره
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/149870" target="_blank">📅 16:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149869">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGqN-TzbyYzszOakZ07wZVUd14d96-5i3B1VtTntLDTWrGTe3zIbnW_-ByRDKdn5fhFHo46mm9fyWoI3wKJVOqyhbAZJF_Js2SeOXPg2DTIP3zTOpr4tlZuMM-k1v-zwMG1hyoAh4AWqBuzznun9aRDWdO1pGeJOGZKzDYmAFfth9-cPUkWtGreWiaNq0o0v5tnMJzT9eaShWIyp0xxfVy_imTuhRoAgky_8DPm1YHeHtijSqsWt1PPdihEnnqE4TydY5jZEWsUodyyZfIcvoMz2XTKMsgfdz7AH_5PyI7m0Du-SLRQ_Tyc66pqkWmRB-OhGFcW5sCS02E9y2cbrcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: حق حمید نیست زندان بره
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/149869" target="_blank">📅 16:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149868">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuG1ewAREr8DFzMsNy54iuTUdLEir02Mm1KW2JoTnlVFG0eV9ZkcvaS8_X0Nz4EGimSutjZpACDuq5v3CUIYN-9JXwyGulVaLbuODGOeZhqu-saRIkCw7F6nh70VbOROLzk9dVhIRtTmIfhh8rlhBlpp51I9TZ_BvdBCxJRj1waFYqWFtYe2lUjja8W9NBXBtCcz87c9crnoez3061ngOiOydApwc5vvylj_SBm_perAmm7qeRo0EVWQeWhc4vb0JmHoL3iL577z9XNhPycF_W5D20gTv0BZIVLhNDDyT9_VT1lesvy6WKFcFTkciOaE8VJCAmZUlWA1-UQ0uw792g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بهمن بابازاده، خبرنگار حوزه موسیقی: حالا که بیژن حضورش تو ایران رو تکذیب کرد، منم مستندات رفت و آمد ۲ ماه اخیرش رو ساعت ۹ امشب منتشر میکنم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/149868" target="_blank">📅 16:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149867">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏
👈
یاسر حجاج، سفیر عراق در ایران: فرودگاه نجف از ۲۴ ساعت آینده‌ برای پروازهای ایرانی باز خواهد شد.
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/149867" target="_blank">📅 16:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149866">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwPMui_7WKOG6hSpjZ8vfqFFERuNdCEMLWxigOIDOu--8Dlx-reW7tuKTTmquXOnM0AAhKA1hfvFiLfP9Iu8egGIE8EX5me6Tpeo5SZUJUiMTpO8L0eEARHBJyYj-kRsip4SBakulTh9A9WZBIZTpRlyXCsjSlLSLGICPywGtyT1aHY_k4RDuUsObMkf-DZMSo7ZbcMcaArYHhexio0RBuSXGimkv7MZFL2Np0AZ1dkizeKB_xb7m1P32zCY22t4NGLgc4PQoDB3YUKtuum4OajKrbr8UfQsjy_IoEHvpU_lWWPPLg4ORFWaXqvT7soil7dYsCIADA5gF29qxJk6Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار دوربینی(حسن زاده):
اولین نفری که موقع بمباران بیت رهبری در موقعیت حاضر شد من بودم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/149866" target="_blank">📅 16:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149865">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اگه نمیدونید طلا و دلار بخرید یا بفروشید حتما اینجارو داشته باشید تا ضرر نکنید
👇
https://t.me/shahab_gold_trading
https://t.me/shahab_gold_trading</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/149865" target="_blank">📅 16:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149864">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
دقایقی پیش 6 فروند جنگنده f35 آمریکایی به همراه 4 هواپیمای سوخت رسان از خاک آمریکا به سمت خاورمیانه به پرواز درآمدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/149864" target="_blank">📅 16:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149863">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
شعارهایی که دانشجوها دادن:
گرانی، تورم، بلای جان مردم
بیگاری، بیکاری، حجاب زن اجباری
دانشگاه پولکی، نمی‌خوایم نمی‌خوایم
با رتبه‌های عالی، تو خوابگاه پوشالی
🔴
در نهایت بسیج سعی کرد تو اعتراض بچه‌ها دخالت کنه و ادعا کردن میخوان گفتگو کنن، اما یه شخصی که در صف بسیجی‌ها بود، دانشجو هارو تهدید کرد که تو گونی میکنتشون. اونام در جواب گفتن:
🔴
گفتگوی تو گونی، نمی‌خوایم نمی‌خوایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/149863" target="_blank">📅 16:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149860">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3de8da7ba2.mp4?token=dPiLMNeTmWgp4xX69vRg5Crc4KIBHKgIJwgZReHPg9eElxKfgUPhQzlXIotbKAJeCpKZsKOm82O8XiEkYMG23aYRVWTA9jtR8ETxIH4vR-31Sf13PPuxkG85Qh6r57R5dyWM3-r1mE3GkSiuRw_Fel_3G2VII2-S5N6wg81ewNCpWzL3x-cq3AQ9DcgMYMpZ0dR7NE52QfS-1Z64z2TIY6bwrv1GrfG3yewI9nShCh8Mcq4cB6TiqHGS1S_PDUqgMRTlcFiDxZRrHBZRS0ojIWE5QweUYxHa2Ce8c9Utr7v30GdOCZS_LsfTZGzANm8JESZF2h5sw61LrTXU8cPg-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3de8da7ba2.mp4?token=dPiLMNeTmWgp4xX69vRg5Crc4KIBHKgIJwgZReHPg9eElxKfgUPhQzlXIotbKAJeCpKZsKOm82O8XiEkYMG23aYRVWTA9jtR8ETxIH4vR-31Sf13PPuxkG85Qh6r57R5dyWM3-r1mE3GkSiuRw_Fel_3G2VII2-S5N6wg81ewNCpWzL3x-cq3AQ9DcgMYMpZ0dR7NE52QfS-1Z64z2TIY6bwrv1GrfG3yewI9nShCh8Mcq4cB6TiqHGS1S_PDUqgMRTlcFiDxZRrHBZRS0ojIWE5QweUYxHa2Ce8c9Utr7v30GdOCZS_LsfTZGzANm8JESZF2h5sw61LrTXU8cPg-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراض دانشجویان امروز در دانشگاه علامه طباطبایی در واکنش به گرانی، حجاب  و سایر مطالبات برگزار شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/149860" target="_blank">📅 15:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149859">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UEKDl-GWPihIOLHVA8c4K9CmwkxqLTEfOfQFF9KNhFfj7DR_60LhCs54g5VgnDUx6Erw1s224C6dQ-q_aLlFR8UBpnijuOJnfnu2yRyd7boCDvuoSmyIpDVNMfQifpcUccP3H1Q91fgvZ87ZTtGAIaz8xRyz3LZW2WWoBLnikpBsJK60B_K4zXoj_WH7HquhKmEzwcVTWHWm682x8FjIvZINlUAHV-dsyb65BFip1-xTcPpnUUXidsXiDM05huWsQgvGGwNrFF99XpD_KbP646-iegOw8u1Z7xRBOhfEO3kiA9q6A3WZ1yPHc-b9oD1fS1b4gqp84WF9ju9bk3NPsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام در پاسخ به دریادار سیاری:
ایران نیروی دریایی ندارد، زیرا نیروهای آمریکایی آن را غرق کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/149859" target="_blank">📅 15:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149858">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
رویترز:
میانجی‌ها امروز یا فردا در نیویورک، مذاکرات جداگانه‌ای با آمریکا و ایران برگزار خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/149858" target="_blank">📅 15:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149857">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRboOJQi5U1ySlOAWxxrOc4S9h7SsSMuQSMr2ILbZPk_exsOYZBM5C2yaiVyFwWchU420HsShZmP7SrVZNQ4wM41WC-I8HYwMXuJ-eUp-Jtml_B5pZ06KROHEtMHt4dY-r6VJ8sOMpwaUTJ5fnvlbIn2hkYqwqxLTKex5fm5s1mHEiei2YsOXDbAhAQgdks-wURMDPSZjvnD-oQUTlShmdlT7zH1h7p4DsY3CPgOVt7gHM0hqVyz1UBimxCYc1NFxZigj7ViYrStu7S5YBxB-CEK92u2CNjsC3IYmVAc1Jc6BPmUjuJEPtooHPpDxb2dYCupXslsjLFrcrfpKc8vAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناو هواپیمابر تئودور روزولت در خاورمیانه مستقر شد
🔴
ناو هواپیمابر «تئودور روزولت» نیروی دریایی آمریکا روز یکشنبه از سن‌دیگو عازم غرب آسیا شد؛ مأموریتی که ممکن است به دلیل کمبود ناوهای جنگی، طولانی‌تر از مدت معمول باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/149857" target="_blank">📅 15:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149856">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dfa657f59.mp4?token=ryddDQJ2ySyIzxG79_Km1PkfEq2P7IUQvKPl4qhtugjo50XxFddxrxUvtJ8jGS1bi4DV9vJ3kOXk42U-scLByz0fTpqbomn0jLqaAhD0CRRJchdrfmtQai9U3yNXnNFLdPoB_1t7krDZMcChCMtCb3IRfk6fW0_DuszdjnuOde_dPlWsTPTOOiP2wP_EZSNFSPvlB3as0LLv7Pbh_Zj46zEvyDdOhrE5N_yFpEdLCgp8OZsb6rcQOgHk1nwypUXujYxIrDGuSYI8Og2sVM4exqtzgHoj3wH8MglJAtGG2Rk4p0TxNrnadJxivVtg-ufjocUSmhZfIPW4kAG-7X7ccA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dfa657f59.mp4?token=ryddDQJ2ySyIzxG79_Km1PkfEq2P7IUQvKPl4qhtugjo50XxFddxrxUvtJ8jGS1bi4DV9vJ3kOXk42U-scLByz0fTpqbomn0jLqaAhD0CRRJchdrfmtQai9U3yNXnNFLdPoB_1t7krDZMcChCMtCb3IRfk6fW0_DuszdjnuOde_dPlWsTPTOOiP2wP_EZSNFSPvlB3as0LLv7Pbh_Zj46zEvyDdOhrE5N_yFpEdLCgp8OZsb6rcQOgHk1nwypUXujYxIrDGuSYI8Og2sVM4exqtzgHoj3wH8MglJAtGG2Rk4p0TxNrnadJxivVtg-ufjocUSmhZfIPW4kAG-7X7ccA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو وایرال شده از حسین طاهری یمنی‌ها که اخیرا خیلی معروف شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/149856" target="_blank">📅 15:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149855">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">میلی گلد ورشکسته شد
‼️
بار ها توی پیام ها اشاره کردم که به ابشده فروش های انلاین اعتماد نکنید  حتما اگر ابشده میخوایید بخرید فیزیکی باشه و همونجا تحویل بگیرید  یا طلای مستعمل با درصد پایین بخرید برای سرمایه گذاری  به هیچ کدوم از پلتفرم های فروش طلای انلاین…</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/149855" target="_blank">📅 15:21 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
