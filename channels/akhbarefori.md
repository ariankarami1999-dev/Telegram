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
<img src="https://cdn4.telesco.pe/file/laAKNE_p4yaKYZSjCUOmJ3eHF5zWKTmnHslrGdPDpQPly5ytgmbGh-R3V_l5asTXjesJgvV6b7MxJkPcCTvbnHx3BqZlInrJWTQdRbop1DzY0GYT_fzWTpgfYPRROQBaVs9FiVEcf0xlV7G-9xOX3SvZ-fP4prt-MrKmho5pZ2xBv2rP3y7vGMccBLSn_e4nmJf7mBcPbGg3fNdxE_jyedu4Xqc6ooKIYPmkN9KQSBmZX9scyf0lKMnQuEJhMRmC9X0baoi499Z2zfqI4jKmlX72Q9Y-sjgVLcmo_xL_FdaTu-3_WPE6RFKqAo1EBvRkNDpAnXpY73oQlMhvHeGIFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.08M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 13:09:42</div>
<hr>

<div class="tg-post" id="msg-655222">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8vYLHJ13oXu2AgNiCKIDxKytjJHCZGz1v6ZxYF7zUnDKHAN9bfGjV-VUtgenrk0zsH6IRScvFBdtt_ZJ87QlgdIpnteLYUfoY3AUbzITQG-THfRfnybywueuz64fuCqv7SQQdy5OTf-tNK1T0HYho7VCw6ycdCNlwUPMGmGksgLYD1jfXRjW0KxU7BwcUg1oADssyGQDneVpl5_ke8V8u4V1IhkFuMu0lWMO9bPucD0N4-BTWF7n3nrgRA2ez1s5YAL8iXJ96cLQoWkpZYCdVkkoVdjvxRSuEtiWGeyLw-ECz8LyBDKFwANmYoR8u4zDxlRa7KvqtUUDq-qnMNhnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف به پزشکیان: ابهام در حساب کالابرگ مغایر قانون است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/akhbarefori/655222" target="_blank">📅 13:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655221">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ee313a03d.mp4?token=cyJLFEFHNeCuK4mhlmYL-sfthYebX9WxTM1DN5pEbEY0689YSbU8bTOOzAnIN9ppXJdK8s2Kak6N4_eQWkY4qXT8jrFqn6rYI7pkq5IK_eq6Fo6sFoRI3y4X6NYeoYQ4a1iSXP2hqPbF_gaFwyqbfNx0uXOrShy473hCg7wnqZJxi1yczN5I-dCTI4sVcQa7WsmZjq-YZdOs-KS2X4hHfdiOvuwwYQgLN8nTdaPMGplcrYUyazDT5pLssycHG_WFEtl0ZGdKV3wIZJHzyNmP5Mo2uhbJBrBFLqapzPAVCB32RCoEJp0W2ivkdeFPSFDP1okI7kDJnY-WIysiEvtJiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ee313a03d.mp4?token=cyJLFEFHNeCuK4mhlmYL-sfthYebX9WxTM1DN5pEbEY0689YSbU8bTOOzAnIN9ppXJdK8s2Kak6N4_eQWkY4qXT8jrFqn6rYI7pkq5IK_eq6Fo6sFoRI3y4X6NYeoYQ4a1iSXP2hqPbF_gaFwyqbfNx0uXOrShy473hCg7wnqZJxi1yczN5I-dCTI4sVcQa7WsmZjq-YZdOs-KS2X4hHfdiOvuwwYQgLN8nTdaPMGplcrYUyazDT5pLssycHG_WFEtl0ZGdKV3wIZJHzyNmP5Mo2uhbJBrBFLqapzPAVCB32RCoEJp0W2ivkdeFPSFDP1okI7kDJnY-WIysiEvtJiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"قرار در بی قراری"؛ از کیت آرامش تا دسترسی به بهداشت پریود در شهر
🔹
۲۸ می، روز جهانی بهداشت پریود بود؛ روزی برای یادآوری اهمیت آگاهی،دسترسی و بهبود کیفیت تجربه پریود برای تمامی زنان.
🔹
مای لیدی همزمان با روز جهانی بهداشت پریود، کمپین «قرار در بی قراری» را با تمرکز بر این تجربه در روزهای پراسترس و ناپایدار اجرا کرده است. بخش اصلی این کمپین، «کیت آرامش در اضطرار» است؛ مجموعه ای از محتوای آموزشی، کتاب، موسیقی و خدمات مرتبط با سلامت و آرامش بدن و روان، مانند حرکات ورزشی و مشاوره با روانشناسان که با همکاری پلتفرم هایی مثل فیدیبو، خنیاگر و دکترتو در اختیار مخاطبان قرار گرفته است.
مشاهده کیت آرامش در اضطرار
🔹
در کنار این کیت، مای لیدی باکس های دسترسی به نوار بهداشتی را نیز در چند کافه قرار داده؛ اقدامی در ادامه مسیر این برند برای بهبود دسترس پذیری محصولات بهداشت پریود.
🔹
مـای لـیدی پـیش از ایـن نـیز بـا نـصب بـیش از ۵۰ ونـدیـنگ مـاشـین(دسـتگاه ارائـه پـد بهـداشـتی رایـگان)در مـراکـز عـمومـی، بـیش از ۳۴۳ بــاکــس در ۱۲۱ محــل کــار، تــوزیــع رایــگان مــحصولات بهــداشــتی در مــدارس شــبانــه روزی مــناطــق کــم بــرخــوردار و اهــدای محصولات به کانون هموفیلی، تلاش کرده دسترسی به بهداشت پریود را ساده تر کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/akhbarefori/655221" target="_blank">📅 13:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655220">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
نحوه برگزاری امتحانات پایان ترم دانشجویان تعیین تکلیف شد
قائم مقام وزیر علوم:
🔹
امتحانات پایان ترم دانشجویان دوره های کارشناسی ارشد و دکتری دانشگاه های کشور بجز چند دانشگاه فوق در نیمسال جاری به صورت کاملا حضوری برگزار می شود.
🔹
دانشجویان کارشناسی برای سال جاری آموزش باقی مانده خود را به صورت مجازی ادامه خواهند داد و آموزش حضوری نخواهند داشت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/akhbarefori/655220" target="_blank">📅 12:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655219">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
تیراندازی در دانشگاه علوم‌پزشکی قزوین با یک کشته!
دانشگاه علوم پزشکی قزوین:
🔹
در پی بروز حادثه در دانشکده دندانپزشکی،  بررسی‌های اولیه حاکی از آن است که انگیزه این واقعه، مسائل شخصی و خانوادگی بوده.
🔹
در حال حاضر دستگاه‌های ذی‌ربط در حال بررسی ابعاد دقیق موضوع هستند و اطلاعات تکمیلی و دقیق متعاقباً از طریق درگاه‌های اطلاع‌رسانی رسمی دانشگاه به اطلاع عموم خواهد رسید.
🔹
گفتنی است در ساعات اخیر اخباری درباره وقوع حادثه تیراندازی در دانشکده دندانپزشکی دانشگاه علوم پزشکی قزوین و قتل یک نفر در فضای مجازی منتشر شده است.
#اخبار_قزوین
در فضای مجازی
👇
@akhbarghazvin</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/akhbarefori/655219" target="_blank">📅 12:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655218">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iks7NV5ujTrIGzWm1KNXztoSzyO73qFMqzN2-bmB29wzx5GxuDzjRBaHeJ-Eufb302X4D8oWM2KpSdhY_pt0ef9hfts3-7O0YKSrGZmpShHGq_oDDKitDEDlejwuu4OUq6sz05n4K2eZ9FOS7Y5lnmJfS9zHS7Wia1352HVQrWsnxHlTjdJavHx5c8J7RhhDC87yr1qPPdxch5Llna-uo9-ca1jqGreWyfh4Evmtp2qFExyQ-AGTuXGsMTccuR3YnywfdOV6U2kdcKSHvxFfAP14wdy8zVBXEFxQiO5lycFQUEZaNpadkVZg1X7VzF2iNler4qBS76xcHmCs5y09fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاهکارها و منتخبی از آثار برجسته ادبی کشورهای مختلف
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/akhbarefori/655218" target="_blank">📅 12:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655217">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f695ea1873.mp4?token=s1s5socvA_xeaG7CPgVsZX-LLdvkQsxVXLquBRZ1NMp4kuSs545Ji8buFx2RnADLqNIctgH14o2eZo1dvhvTjE2-K-XGGTmW8CUbMiV1n-1Wb6Q6G5Zb85Fckahh2PZTu-E6aEvQ09vzPiUZ3zXwOYQ-74Ui9jpUDjDpHD5YpePNrjLrLsPeUzTsJ16DqMDfg7vupz_4erTw1iOZcenZNuH17Zv6QGgREIyZ_eRZwOcyFxcLiI0y9tttSMN1ZMlSaaQ2tDmePE8Yp73iU8mQxTFNnQ_DP0vJ_1WVGvmAiP5tjmJI2p8XC3_2CInf3UY5xprnAih0zGUBwf4bNPFgnDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f695ea1873.mp4?token=s1s5socvA_xeaG7CPgVsZX-LLdvkQsxVXLquBRZ1NMp4kuSs545Ji8buFx2RnADLqNIctgH14o2eZo1dvhvTjE2-K-XGGTmW8CUbMiV1n-1Wb6Q6G5Zb85Fckahh2PZTu-E6aEvQ09vzPiUZ3zXwOYQ-74Ui9jpUDjDpHD5YpePNrjLrLsPeUzTsJ16DqMDfg7vupz_4erTw1iOZcenZNuH17Zv6QGgREIyZ_eRZwOcyFxcLiI0y9tttSMN1ZMlSaaQ2tDmePE8Yp73iU8mQxTFNnQ_DP0vJ_1WVGvmAiP5tjmJI2p8XC3_2CInf3UY5xprnAih0zGUBwf4bNPFgnDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس قوه‌قضائیه: گرانی‌ها باید برطرف شود
اژه‌ای:
🔹
اختلاف نظرها در کشور نباید به تنازع  تبدیل شود؛ در زمین دشمن بازی نکنیم.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/akhbarefori/655217" target="_blank">📅 12:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655216">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChpBCfun9I1FrxtBROUn2dVzgJAQ8Z18tVUsV5Fhm94ajl0MPTaiqCYgGLIrUBPPTn6WMeb90L7FHLxsYmnOW-oFIoAz1ts9e4RzHL3PXwTfqwmsTmToffKzeobGcpEymqvJbV1bJzvbjHpzxVsFDOCLKQ9Jqp4GWA_23m6rmIuhTwv1qfQ54qjemg_2p-jEYA9U4ING6f-QeCBxCeh_PeWjViVdM8sziyfyGJtw36gqD0npMUO9RBlKvkmRP2KjWj_cpL0z8wmjUKKdnDhbBwJGpApd-u9zJr4d_J6A4rtp6Fh7j2Ou8KAPeVv38MkiefUQfu-ANp_kqUu8GPCM_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمامی استادیوم‌های جام جهانی ۲۰۲۶
#جام_جهانی_۲۰۲۶
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/akhbarefori/655216" target="_blank">📅 12:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655210">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/771bcfe756.mp4?token=JRsGCaO_C05UdzunF8z8KYHuy8yjrZMXThVTsyur78UBR3u5B8TuHYg7gzUIDt6uFx7QnPgMM9-e69IClWbEnukzR1HyAPkwaAxDf1v0avKnfc0o628F7Ms9DVPyunjwuZiifc7NAAyT7X-MkQoj-LeDOcCP9XD9UNsdRZHtS8umFel6xc4g5VXwpPW8VqmlOpnXgbimLiy2Gc6AlL4vaIhsMJNA8p6pZS-AgWSqiqeyBXby9khylJRibrE4wzX1mAOOGkNnX9sQD2IH-uGEKipgYlLQ7os_loZOZHnG96f7oxcRrca9cLhxUAwRMpsQeGzOt36mMCZGkLEpWy7vsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/771bcfe756.mp4?token=JRsGCaO_C05UdzunF8z8KYHuy8yjrZMXThVTsyur78UBR3u5B8TuHYg7gzUIDt6uFx7QnPgMM9-e69IClWbEnukzR1HyAPkwaAxDf1v0avKnfc0o628F7Ms9DVPyunjwuZiifc7NAAyT7X-MkQoj-LeDOcCP9XD9UNsdRZHtS8umFel6xc4g5VXwpPW8VqmlOpnXgbimLiy2Gc6AlL4vaIhsMJNA8p6pZS-AgWSqiqeyBXby9khylJRibrE4wzX1mAOOGkNnX9sQD2IH-uGEKipgYlLQ7os_loZOZHnG96f7oxcRrca9cLhxUAwRMpsQeGzOt36mMCZGkLEpWy7vsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آثار حملات ایران به پایگاه الظفره امارات
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/akhbarefori/655210" target="_blank">📅 12:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655209">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEl8eZ5LP9qLHibxwU_gWDS3ThO6T8QROXDjJVKhheOpIgjswoHDk24NbJHaMuKAauI_kYAmpiVh09jGKJkbOClI1aemV-LB66tXc2Hi1BfZo8-yWiRT4rhARLjOMJN2qIsqZn_IZJB0gP0XXpGEtkWi_5Wlmsaxcab3_bTxzd4pdnUYzeSsHizQdajrfvXiXIZfQX4pSBmJuDImegs5dhYCD4TAAL8eDAo3AKCJgyB65bc4eAw8TvJQJtXexngjiTOadjWTX-Kzi_Xskj5Q7rWsmdailS5dD5eMeoi8TYVdpzUOvq01ovhxJK_s3vsEroABeesDxqDDNUuDDkrDDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاردین: ترس ترامپ از ضعیف دیده شدن، سد توافق با ایران است
گاردین:
🔹
«هنر معامله» ترامپ در برابر ایران شکست خورده و او در مذاکرات نتوانسته از خرابکاری در روند گفت‌وگوها دست بردارد.
🔹
ترامپ از نشان دادن هرگونه نشانه ضعف بیزار است و همین مسئله او را از رسیدن به توافقی که ممکن است او را ضعیف نشان دهد، بازمی‌دارد.
🔹
ترامپ همچنین به شدت نسبت به این انتقاد حساس است که هر توافق احتمالی او برای آمریکا بدتر از برجام باشد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/akhbarefori/655209" target="_blank">📅 12:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655208">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BF2JJ3IB043s0tt2k6IumCY7d_P6CctrFndG4g4sICy5_GkSm9i2bh8RE2Wi4ihRiVbyg2h5cPyiWEI57qkUK35-gwyhXCdMCdQZO13W_zzuLOqgwkIXrpf0YOZSBu251DvP1oQNR21oWGo1qdtKK5Q-tbMcxkEiFL2jsVgKQdxrqvubmuDjVtLotmJ8I4bzs_SCC2SzrYa6EzDadHiLjuR39yRqGHZ9ajq_gsX3rQDO-Cdor8Bi3RD7-edrWYSBNjb9F8yNpS_p-nm0Yyt38kNEY8zzPDGsrnAn_XKpmyDlYyw47_SLfpQQ_DpIgq1SalZWFPwsx1nnSygkAFeBHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاوضه لوازم خانگی با خودرو در بازار!
🔹
با افزایش قیمت‌ها در بازار خودرو و لوازم خانگی، شیوه جدیدی از معامله در بازار شکل گرفته و برخی افراد لوازم خانگی را با خودرو معاوضه می‌کنند.
🔹
در یکی از آگهی‌ها نیز کولر گازی و فرش برای معاوضه با خودرو عرضه شده و کف قیمت کولر گازی حدود ۶۰ تا ۱۰۰ میلیون تومان اعلام شده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/akhbarefori/655208" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655207">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
انصاری: پیام مقام معظم رهبری در ۱۴ خرداد قرائت می‌شود
دبیر ستاد مرکزی بزرگداشت امام خمینی (س):
🔹
مراسم رسمی ۱۴ خرداد از ساعت ۹ صبح با تلاوت قرآن و مداحی مداحان اهل‌بیت آغاز خواهد شد و در ادامه، پیام مهم مقام معظم رهبری قرائت می‌شود.
🔹
امسال امکان حضور گسترده زائران همانند سال‌های گذشته فراهم نیست.
🔹
یادگار امام در مراسم امسال سخنرانی نمی‌کند.
🔹
نماز جمعه ۱۵ خرداد در مرقد امام برگزار می‌شود.
🔹
امسال مهمانان خارجی در مراسم حضور نخواهند داشت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/akhbarefori/655207" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655206">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i09xlkYa8rwlI4ZYBWad_z_KGWFk-vauLUpisNj41VkrV96qj9O9LRxRvxwNvtBHabllX_6Fx6hYDETVEWP1_UBL2bkkOTDiNWMasMIG4fYWeIK4kIk4uz_S1MYjWueqY0HpdukxXyLpQfAUnapb14wqMXaY7Fo4MuqtK6jd1mm1kgp-VMuTmRrDTGay-HiRTUVwPUw5BwR3xHkkqKHlhPS69_woFQ8OGXimc0HafCOchTq7clkVXTbc9oTXrgeNZKNi7yqfbzYhwy6UwKZ8YqxJ5XqA_U3NDSEipH_kuSL8EGqhU1N9CP2zSSAUfzRyx6Ma8otCpJ3oSEOF1nu2kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: باید هزینهٔ جنایات رژیم صهیونیستی در لبنان را پرداخت کنید، همه چیز سر جای خودش قرار خواهد گرفت
🔹
اعمال محاصره دریایی و تشدید جنایات جنگی در لبنان توسط رژیم نسل کش صهیونیستی، شواهد روشن عدم پایبندی آمریکا به آتش بس است.
🔹
هر انتخابی، هزینه‌ای دارد و صورتحساب آن هم از راه میرسد؛ همه چیز سر جای خودش قرار خواهد گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/akhbarefori/655206" target="_blank">📅 12:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655205">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XS_gkrbQqOJgxNXNVVl-8NGDKX3nEvHCiqsr57c8zMLexFbXa8-Bj_JlL_tEyLr-DRvnW0wP64WWTZs21531mEyPS3154E2etJjR-NH_ITPoVGvDNPyidWkqSKkSglR6u4StFSYCc0OZTNARh5LixqeLKKzM1AsUE3bSW2gPAb4xiwXUwq6lvw6SbAZPrkrInACWhyAP1gw7ZB4JMQ0eJXwyLQJyvBGlmP8_aLczyDY6AAvLkU4AQSCCtVENJLzfpojlRom4fxMvJ3M_HF6PrkxHRJQLib6bwe_R-27qWGH0mY0BiOc8yKd7mNiNMEhAleXzIJ_l0P40la1N-hqDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت درهای بسته چه گذشت؟ | طعنه‌های تند ترامپ به ونس فاش شد | مذاکره‌کننده اصلی با ایران کنار گذاشته می‌شود؟
🔹
بر اساس گزارشی که به نقل از منابع داخلی کاخ سفید و تحقیقات روزنامه‌نگاران منتشر شده، تنش‌هایی پشت پرده میان دونالد ترامپ و معاونش جی‌دی ونس وجود دارد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3219292</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/akhbarefori/655205" target="_blank">📅 12:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655204">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edc35d9fc.mp4?token=TylDtJbNOGWOzQKc9mp6cjp36a0E5GgPNiiuxze-9ycA3w34IiG32IIT1okpzKCONcaTrCjIviQXwtWBD_hJaSY4c6RS_kK3IWbN3h0VYBS7n7DNdSXI_5TfLAWjDgmHiKKAfYJBAWdReDR7oYBWXw3n7kk9vsyHSLiqM5zzv3j9PA87pBBc3q4Q4GT3id2InYfbGSD9PupsgCK31akwxutaR_9V3JPmTV0_q-GulZPKxuM9tVFf47ukSWwDygc41ZncwhrYt9UVHff7eJi-9E7iAZFB_fqX0KsaGwIcn_3sGT_gNQlq0xpjqXC4Dii38EBcPoIreAkim2QcPi_QaDINxO6RqW8p1oG_RENZY9-Pkmdhozn5ViXHt_wA19Egy10Y5-aeU97S0ceHax8eIr7uqBouKqjKUKGblfkizcIWzeXq0bSyvhPWZPB-AbK9UDlWMGLjhTrbOwqAtuRMENSVSS_sizRx_hR-Vlip-RZ1ACxJix3xcv0C-uV6r_eA-sK8JRwpEzwnN-LaukodJVaszejnu_Vc16bmzGbCTf59e7RFEqdltfJMneVgRG-A7sQk0P0IoSpTSA_XBUIQeoNAIbocKHDYPrK-EiBkXXYYJZvHJGw8FPXDM7Hnifa7M778jtvA1I_VnhKVXYVmf1mVNfcaKVv8SlVaFKNCjbI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edc35d9fc.mp4?token=TylDtJbNOGWOzQKc9mp6cjp36a0E5GgPNiiuxze-9ycA3w34IiG32IIT1okpzKCONcaTrCjIviQXwtWBD_hJaSY4c6RS_kK3IWbN3h0VYBS7n7DNdSXI_5TfLAWjDgmHiKKAfYJBAWdReDR7oYBWXw3n7kk9vsyHSLiqM5zzv3j9PA87pBBc3q4Q4GT3id2InYfbGSD9PupsgCK31akwxutaR_9V3JPmTV0_q-GulZPKxuM9tVFf47ukSWwDygc41ZncwhrYt9UVHff7eJi-9E7iAZFB_fqX0KsaGwIcn_3sGT_gNQlq0xpjqXC4Dii38EBcPoIreAkim2QcPi_QaDINxO6RqW8p1oG_RENZY9-Pkmdhozn5ViXHt_wA19Egy10Y5-aeU97S0ceHax8eIr7uqBouKqjKUKGblfkizcIWzeXq0bSyvhPWZPB-AbK9UDlWMGLjhTrbOwqAtuRMENSVSS_sizRx_hR-Vlip-RZ1ACxJix3xcv0C-uV6r_eA-sK8JRwpEzwnN-LaukodJVaszejnu_Vc16bmzGbCTf59e7RFEqdltfJMneVgRG-A7sQk0P0IoSpTSA_XBUIQeoNAIbocKHDYPrK-EiBkXXYYJZvHJGw8FPXDM7Hnifa7M778jtvA1I_VnhKVXYVmf1mVNfcaKVv8SlVaFKNCjbI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر یکی از عملیات های گشت و کنترل تنگه هرمز توسط شناورهای تندور نیروی دریایی سپاه طی روزهای گذشته
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/akhbarefori/655204" target="_blank">📅 12:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655203">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbNq3YUOmVuriUhKOTrSkNkDa2pMM0AmE6z9QEdHCYORLB_ergCu3nfyVDCK_KiXIVeSIOpwjbVDp51I1rXJGGua3-SgjwdTvH6wLzQ-I1WMh0-b_ySW2HpGQSMmeDQQ0UFzz7ifX0_7uw-gN9_KK3IZ6wheNInGnO_r9XPH0Qi5OKW-Fz6wDaJL87wwq2kn2hrfnEKzEVZKE9oCDGdBh6puVg2w5bXDyTTo8A1BrQtl0BADZXW4unXAJDy-LFZfnI0sRJi5QEMvIngfMURXIln5sZ-vBuXo5W2u4p7tCF3uoe25ykS6ODqwFl_8k3Eaj2rLCJWiqpqw5hQTU4IThA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار رسمی حج ۲۰۲۶ منتشر شد!
🔸
تعداد کل زائران حج ۲۰۲۶ به ۱ میلیون و ۷۰۷ هزار و ۳۰۱ نفر رسید که حدود ۹۱٪ کل زائران از خارج عربستان و از ۱۶۵ ملیت مختلف بودند.
🔸
زائران ایرانی با حدود ۳۰ هزار نفر، نزدیک به ۱.۸٪ از کل زائران حج امسال را تشکیل دادند.
@amarfact</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/akhbarefori/655203" target="_blank">📅 12:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655197">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ag7Gi15nNf18QWgRTir5kNZZqRGRW5Ai83vjx-OOtq_BTxMKorkrozxgTf13076fjXGqsPk_-jFaQts-Zf6QRyGgVx9K5P9Hr8pNhcoud2lzEaOJFw1Tt6gbsIGhMSN44UnofXS7qvoEgmfxerTXmwljOZRWNFZH6oOmoi34yjJMUK7zmO9vMPEgWB-l_ogkiDeHFqV1iR5Ft8UFf8szLi5izBsBKYtfQQxAGlja1J-9ZP-9JbTBibBfRR0wbIMK2KXZFM1NVb4CJKFZbvV6IqcnJ9jnpn3Cj9hCbyFYRvPGUwmuX2e-5T1i_a8RVmyQN_zIU-Fo4ouexl86yy81YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/czxwOg1kHx5peGHIqHn4-7QtRROt7z-WlWYwQOgtVJWxIUrfO7fN9OK7_Gr0X56CU457l50aIBsFVNCtat2mUGLMrkehG31uDmUWvPq8VReaLo2RCgNNA41V3kPYM2CcObCQwgzaX5O9BcLHPtnbvklB8WM-YfcuBMwJDztA-LQOAvVPOzk26-_lY3cmsTv6Su6ot5Xzu2N73YCwMsTuavNFXeADxPWXBrOhzEiyzoSdxesNVKjiktm_ZB32PsnZj17O2zHJ1myTENaaE6j5lraMDYKRK_XaaSiQGylAB6KtDhMaF5zUM06wMn50R2j_IbUv-dKziYcBtNzps-PPYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUiRw2DwrDyIzsUU1LPSllGOTgcs5l2HNpm8Ht6hVMMs9_FQvAmo_-naImTrj0UFgOX2Ga7sRw_LteRoyEc6WrcJfHcrdDn_I83XonosXwwtjB7LmKfHrIOjrmiSPdyKXXn87lJ-m5lxKsf5mW1ax44JkydNnyRrEXvy3BmTGdLRs1t-0ig8IgZ5pavijO3fNPQsZPSqtcm-4y37zhvkJ60CSx_bBFjugNTf9AALxYPLpIEMPBpJHUhw2A-krpWRbgjrzWFKgfuUAduXg7_7XvKsM1LBozH7JESq8my4mDZbGcBXm6urMzrMaS6BXXXbIeQShJEq3rg2votG5EyWkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlB4VyGS5rn_kTuMCHmpDZkKwCvgVsvQM-l9I-xYbMtuHEdIy6VmUOXBEwCgvBReA6N0lPplt747xqP6lAcxEiPTKnhheBPHyahKpKNa21b5VhkFmhwbD-w6ax8NDEH3tnnArTxYQCGLsavbdqBPlTQK8GnYdt0u4_jnDhA-QdTjkmU0lMAopha8Zq-aAV879WFwly5mbXw9QvhdCjY4ik2BOYyvgk-cTNHOzPwq-wN4G2bNDN8kGlCEpjAOrcWfFF9QFk6G3rJbvlm0SHJvIojSMj5IGxGVjPFM6Vuo1o_f12qfERfX4ElD2T67UG_lgBQoBAA77pY3_IL9eaXVzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ITtYZE-YgF-QzoOunBqOvfpzXSOhznqW6Jeiyn-7hptiaVsQgWTd4pICVBhkMIatdTi1qQ6g0LES9cSIWy0WTu7MX-zW_uBz1l_5SAjFU9_qKrrsbZfy_Me6gGMkv-ni_lRShSxbn_MwJgtGodi4MBsZqkrulFiLegtMwOGyN29hVDCMpyZRhmyb0AweHqLAxKVf42sBEnsZylT4XFHRVcJoUyvUzAeZLDppPnGVoXBZmnqPaBYRiGw5Iruez33iEPYdCGGg2UD_VxdwR9Z5YGPAgiCMeVGc8mh5OvlFR4qFZtN7ZVW9en4u53mqc-fpORQJkL8xkJ9PHiBmo5_ahQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k35-ljf5bn2Ka4OgoigUD2ikXFJc69XWksqTsaLg6hE4juq4_vPzWy_KSoyOtzoBGq7DFX70KpGXCuMLx-5VGO2At7lFMjheWH_LVgLSRat_0g0aqvEx_wpZwz0hx6TblpcCRTfXHNAObQqN87nMat2F4tpgjTwigdnVlq9FcDCoTDBM9TYNa0KWa242YAvm-E6wMslPQYfIQpWGlP4iD2M-G_Qi3uzmU8FtDbFwjX-DyfHHi_tuLt_lbLZCcNipvdSa_FRtA8YYHDOhOo0makiyZQiZcoB_2woLol4kaaCWkkZn7il1JIThInGcix4-kV2u2WJ1yFu0c-6CShj7mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نصف سد طالقان خالی است!
🔹
سد طالقان با ظرفیت ۴۲۰ میلیون مترمکعبی بزرگ ترین سد تأمین آب شرب تهران است و هم اکنون نیمی از ظرفیت آن خالی است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/akhbarefori/655197" target="_blank">📅 12:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655196">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a05b04c632.mp4?token=VT5YT1iiFzqdJtvnE_ox93mV1P1x1KeuwFOBuRsB_Su_BlZctwp5n_2Ex4gSH-w4XfvncW1RruAdfa9AvYlwRDaUmBE8O28BYc9qw6apMRn2mQplCfQiJ4a7uiXhVg7TDNM50KnZEXYXnpu7UylyCCUS4mWYvpVzUatTyEIHH4kpAkRFI68zwoZR8U6Vp-vuqncF6fvJjjmagOE_5K8ifHXS8ArJbcbaVXEBDeM_cXTPAt1QNjHUuc9tpKlIsLRxcS9Z3dRaEeCh2hMQSgj7IgDExOhIrA68t_GAR4mVgQa8zyhzk2eLR5xBW0gILSvX5hajFCwFfZIUgnshmK44wZuov_hdD5PRqeGgkHZ3Hzm-mfwDBbcwX6M9G8cOABtG6v6WldcmAwNu1pu-9_MaqnM4HuiXZLaIldyMJVEt92omBXW2xn4I6-klPg35NSG2dmte06j0Ujvr4es9ltOz27BtBix8SD7a4qeNOsbZemX7fQ6hXxYdcfA4xlPa4deRTq6KJgtH6zHbnspXyi484hCVDDFyufmWdfzfEL5rCzonOYhqvCbZZyq6Ew2g5xcufqqVn3_56Tkb3KmjVqSsZFVRb7uBDZflsELyqfWAzfXRP6evYV6gOi4uGHSQCxjgaFZT1vituZf_8rri-3pk9op_fjSdSJKOGNj3hZAKdbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a05b04c632.mp4?token=VT5YT1iiFzqdJtvnE_ox93mV1P1x1KeuwFOBuRsB_Su_BlZctwp5n_2Ex4gSH-w4XfvncW1RruAdfa9AvYlwRDaUmBE8O28BYc9qw6apMRn2mQplCfQiJ4a7uiXhVg7TDNM50KnZEXYXnpu7UylyCCUS4mWYvpVzUatTyEIHH4kpAkRFI68zwoZR8U6Vp-vuqncF6fvJjjmagOE_5K8ifHXS8ArJbcbaVXEBDeM_cXTPAt1QNjHUuc9tpKlIsLRxcS9Z3dRaEeCh2hMQSgj7IgDExOhIrA68t_GAR4mVgQa8zyhzk2eLR5xBW0gILSvX5hajFCwFfZIUgnshmK44wZuov_hdD5PRqeGgkHZ3Hzm-mfwDBbcwX6M9G8cOABtG6v6WldcmAwNu1pu-9_MaqnM4HuiXZLaIldyMJVEt92omBXW2xn4I6-klPg35NSG2dmte06j0Ujvr4es9ltOz27BtBix8SD7a4qeNOsbZemX7fQ6hXxYdcfA4xlPa4deRTq6KJgtH6zHbnspXyi484hCVDDFyufmWdfzfEL5rCzonOYhqvCbZZyq6Ew2g5xcufqqVn3_56Tkb3KmjVqSsZFVRb7uBDZflsELyqfWAzfXRP6evYV6gOi4uGHSQCxjgaFZT1vituZf_8rri-3pk9op_fjSdSJKOGNj3hZAKdbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایسلند اولین قربانی قانون جدید داوری فیفا شد
🔹
طبق قانون جدید داوری فیفا که قرار است از جام جهانی ۲۰۲۶ اجرا شود، اگر خروج بازیکن تعویضی بیش از ۱۰ ثانیه طول بکشد، بازیکن جانشین تا اولین توقف بعدی بازی (حداقل یک دقیقه) اجازه ورود ندارد.
🔹
این قانون در دیدار دوستانه ژاپن ـ ایسلند برای نخستین بار اجرا شد و به گل پیروزی ژاپن انجامید.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/655196" target="_blank">📅 12:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655195">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
صف وام ازدواج و فرزندآوری از یک میلیون‌ نفر عبور کرد
محبی نجم‌آبادی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
متاسفانه در سال گذشته وام فرزندآوری و ازدواج بیش از یک میلیون‌ نفر محقق نشد. در سال ۱۴۰۴ بودجه ۲۷۰ هزار میلیاردی داشتیم و در سال ۱۴۰۵ این بودجه به ۴۷۰ همت ارتقا پیدا کرد. اولویت پرداخت با وام ازدواج می‌باشد.
🔹
قانون تامین مالی روش‌های جدید از ضمانت مانند خودرو، طلا، ملک و همه چیزهایی که نقد می‌شوند را در نظر گرفته و امیدواریم این سامانه هر چه زودتر راه بیوفتد.
🔹
براساس گزارشات، در شش‌ ماهه اول سال جدید قول داده شده تا آن یک میلیون نفر وام‌شان پرداخت شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/655195" target="_blank">📅 12:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655194">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1N1LjXCaAwMigp25Jn3EMSa7an_qGfqht1UOLevUfUHpPyZUCOU5VLMztTEmZTHMUdrJGs_IQIGpJpAm5yakX5TPhu_rmCUM2TdVDCedrwt6_EHnOgPnmvqdT3W8Z9m4fX203ftSmmJOtZWTCcp38BbyGnagYdJMEKFG-sWl9sznXnfhiRVvNIHDKLTWCCoKtKi1CFRPs0uzYWdEdxeXRwE89Z1Am5A2v5dK6oinz-umHq6LL7F1xluXkhmVoZp2m_PdUxHMeaIoNTr14eDYM2etINUO-O31TK-ok28eWI95D9SWibDEuB2f58VMMoE6m8cey7inTNihCTLB7spgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای سریع برای شناخت بات‌ها و اکانت‌های جعلی #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/akhbarefori/655194" target="_blank">📅 12:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655193">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4G7_2VpXn2bWhljZi3WiqyFjg0nSa8Qhvtvj2Aw_feFlGE5OUpb8hHdTmMIjZchYeaMoqkk5idzG210cD_OwJLCRBsjkch1tTDu7aiojS8iDQxRV_j1zruKloSeq-N5u033OZRAO5jiEUf4pDm2-2NSIA3Q7f0wyyuHzGQZNbc0Ihy9TvIBZsdK0EzhsUlfA93rfC7u2JJMLRdiLdnkOWFcrIrUId3fkWIOu94XuhPMgG3reC06jAg0qSmC_GGSsGVKS7nWcHWgWieOGdkq9DSqW8esr95Ao9e8Hu7dYgIBseOT-_Nrfy9f1NZ0lp-1UuZp77n9H11_gai-ezuyZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فروش طلا به قیمت عمده و استثنایی و اقتصادی
💰
🎁
🎁
ویژه همراهان و سروران گرامی کانال
🎁
🎁
🌸
اهدای سکه طلا به مناسبت اعیاد قربان تا غدیر
🌸
🏆
ولیعصرسبزایران در قلب بازار تهران
🔸
طلا بخر، بدون مالیات، بدون هزینه اضافی
💥
تا یک درصد تخفیف هرخرید به مناسبت عید سعید قربان
💳
فقط ۳ تا ۷ درصد اجرت و سود
💰
خرید طلا طبق نرخ تابلو با تسویه آنی
🔸
فروش آبشده با نیم درصد سود
📍
بازار بزرگ تهران دورسبزه میدان ضلع غربی پلاک ۸۵۶
⏳
ساعت کاری: ۸ صبح تا ۸ شب (یکسره)
👤
📞
مشاوره و تماس:
📲
0938 436 9323 | 0910 480 1538
☎️
021 55 1500 50 | 021 55 1500 60
🆔
آیدی ما:
@valieasar
🏆
بیش از نیم قرن سابقه و ۵ شعبه فعال در تهران</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/akhbarefori/655193" target="_blank">📅 12:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655192">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کانال ۱۴ رژیم صهیونیستی: امروز رأی‌گیری برای انحلال کنست انجام خواهد شد</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/akhbarefori/655192" target="_blank">📅 12:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655191">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f1aef0067.mp4?token=kJBWiZ7te0Pcuip1FrXeAFhd3OnZKSLDtlP_EDz8MGYICxTN45u2TFBL3bOZyAK2E-2GlcLrZoea2BtgsfmuXRDPgFTYMCZZqIDTC96kkT6QgsDdqyXXmXNnJzgimjtERKZn8eGwImEuwpIVR7ITTIuk2n2fvPwG5nREwm_qCmCtx5o5OrWG_RY4mdz-jSzB21wo2xjgFchxYycxLMElCUZL6AuDrPCQuR-WtZjnRVfSq8QJ_Wj5wQZaiEQaXYMhJp_i5GjAqBATUb3bEkvYyyLDc5n_L2B4RLFxV--o3yBfwg1MjZaJozizxNzv6eomFadKbOOg_HlO6N01TGzBLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f1aef0067.mp4?token=kJBWiZ7te0Pcuip1FrXeAFhd3OnZKSLDtlP_EDz8MGYICxTN45u2TFBL3bOZyAK2E-2GlcLrZoea2BtgsfmuXRDPgFTYMCZZqIDTC96kkT6QgsDdqyXXmXNnJzgimjtERKZn8eGwImEuwpIVR7ITTIuk2n2fvPwG5nREwm_qCmCtx5o5OrWG_RY4mdz-jSzB21wo2xjgFchxYycxLMElCUZL6AuDrPCQuR-WtZjnRVfSq8QJ_Wj5wQZaiEQaXYMhJp_i5GjAqBATUb3bEkvYyyLDc5n_L2B4RLFxV--o3yBfwg1MjZaJozizxNzv6eomFadKbOOg_HlO6N01TGzBLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان ملخ در مشهد
🔹
تصاویری از هجوم ملخ‌ها به مشهد مقدس که در فضای مجازی وایرال شده.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/655191" target="_blank">📅 11:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655190">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: قطعنامه شورای امنیت برای ما تضمین نیست
🔹
در تفاهم اولیه یک بند دربارهٔ صدور قطعنامهٔ شورای امنیت در صورت توافق وجود دارد اما معنایش این نیست که ما قطعنامهٔ شورای امنیت را تضمین می‌بینیم.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/655190" target="_blank">📅 11:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655189">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6732ddafe.mp4?token=VztK70elQZffJQrcBeGCNxkUOFDNQZegC41gbkG1a2-x1BtjLBY7QLWU8BCknn5QcFgATRZkBVCbhb6ksze9TKkAAXpF9IaSKTZb2k7GX2TkmkOq_UUt6lPXF4JTfJsCeOWg5KzAYPm4IK4fAHJe1p1wujWi3J1VrPpNnfjg3T8mpjdN1SMd37Q7afBNJKNwU6q1p84ZgRSLAftog_EtOnmC6LDz-2UdlHU3Ia2YSucd3i9XaVmMOTAV81xC-bXDB8P5vkR26RLcdC2NlDkyAB45KchftnVtrnHFFZ5bzI2x58kltD1jmgysu312kQa0gFfrjYTshjPv5t4l9Bid1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6732ddafe.mp4?token=VztK70elQZffJQrcBeGCNxkUOFDNQZegC41gbkG1a2-x1BtjLBY7QLWU8BCknn5QcFgATRZkBVCbhb6ksze9TKkAAXpF9IaSKTZb2k7GX2TkmkOq_UUt6lPXF4JTfJsCeOWg5KzAYPm4IK4fAHJe1p1wujWi3J1VrPpNnfjg3T8mpjdN1SMd37Q7afBNJKNwU6q1p84ZgRSLAftog_EtOnmC6LDz-2UdlHU3Ia2YSucd3i9XaVmMOTAV81xC-bXDB8P5vkR26RLcdC2NlDkyAB45KchftnVtrnHFFZ5bzI2x58kltD1jmgysu312kQa0gFfrjYTshjPv5t4l9Bid1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: حاضر نیستیم راجع به موضاعاتی که به دفاع از کیان ایران است صحبت کنیم   سخنگوی وزارت امورخارجه:
🔹
مدت‌هاست که گفته ایم حتی در سطح رسانه هم حاضر نیستیم راجع به موضوعاتی که به دفاع از کیان ایران مربوط می شود صحبت کنیم.
🔹
تکرار این گزاره که ایران نباید…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/655189" target="_blank">📅 11:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655188">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
بقایی: آنچه را که ایران در توافق برجام دریافت کرد، اموال مسدودشده و حق مردم ایران بود
🔹
حالا هم به‌دنبال احقاق حقوق مردم ایران هستیم.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/655188" target="_blank">📅 11:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655187">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc5de7670.mp4?token=KvfC0vj5HHvFvUbF6c7iRajMhxENW5fYpvbEmcvuQBJwA-kQ1XfK2zd4dD2x-buURyfx621h_9dTtj8g4vJsiyzYlRY5oANpPaA5IRCdMOG8aldgefKqI3oi8IBHvCOxl99PALPQMqViEVEAzT0j_tckAqDMeE5--dgjmk2XfFccWhZf_pH1DWkKVCCfpvShwedT9McqXulWZFmNHCP9I55kgSJJDE6y86AMfwbUGLazdvwPO0feiy7_uItSjVFxoDSQMZerAyZFFF2J8i5C7DHkG9v4c0Nl6Wdeo-3Zt2AqGx9Yi2TnePBtKBt16Mk0W3Mjls06S5w1Vj29aY4xag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc5de7670.mp4?token=KvfC0vj5HHvFvUbF6c7iRajMhxENW5fYpvbEmcvuQBJwA-kQ1XfK2zd4dD2x-buURyfx621h_9dTtj8g4vJsiyzYlRY5oANpPaA5IRCdMOG8aldgefKqI3oi8IBHvCOxl99PALPQMqViEVEAzT0j_tckAqDMeE5--dgjmk2XfFccWhZf_pH1DWkKVCCfpvShwedT9McqXulWZFmNHCP9I55kgSJJDE6y86AMfwbUGLazdvwPO0feiy7_uItSjVFxoDSQMZerAyZFFF2J8i5C7DHkG9v4c0Nl6Wdeo-3Zt2AqGx9Yi2TnePBtKBt16Mk0W3Mjls06S5w1Vj29aY4xag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: آنچه را که ایران در توافق برجام دریافت کرد، اموال مسدودشده و حق مردم ایران بود
🔹
حالا هم به‌دنبال احقاق حقوق مردم ایران هستیم.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/655187" target="_blank">📅 11:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655186">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afeea0bfd9.mp4?token=T2DzJpPt73-cFBX7KW9iXMNLOKyx7XghL98p_L-_NuBtK5w3DHBuxEbP4g9pdnPFdnCR2EvSOKwm_SLvRt-5G0VzY2Ef4N9p9lKZR2Q85XTuY9BJJ8NdWWKIr4Qw2Egn8JSPNBaksjidiZLDCqOULd1uk_g48o1blOVPN-rSCf8etaxn_iwYdBg24Is-n_M9LR57FHF7Y6g30IT92WGwXlTT0D8_DpwmqWxjEzyr00I1QJj0ZJQ_UPUjWS5TlYrk4hAczNeBv-VuLGA9ksnyM7IcPkJOq1EJRZ-5BlJ8It51deCtTR8XwSfuRbVbHnw2tqlCZPs5h28bPN7JPyPM0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afeea0bfd9.mp4?token=T2DzJpPt73-cFBX7KW9iXMNLOKyx7XghL98p_L-_NuBtK5w3DHBuxEbP4g9pdnPFdnCR2EvSOKwm_SLvRt-5G0VzY2Ef4N9p9lKZR2Q85XTuY9BJJ8NdWWKIr4Qw2Egn8JSPNBaksjidiZLDCqOULd1uk_g48o1blOVPN-rSCf8etaxn_iwYdBg24Is-n_M9LR57FHF7Y6g30IT92WGwXlTT0D8_DpwmqWxjEzyr00I1QJj0ZJQ_UPUjWS5TlYrk4hAczNeBv-VuLGA9ksnyM7IcPkJOq1EJRZ-5BlJ8It51deCtTR8XwSfuRbVbHnw2tqlCZPs5h28bPN7JPyPM0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل فده والورده به منچستر‌‌سیتی به عنوان بهترین گل فصل ۲۶-۲۰۲۵ لیگ قهرمانان انتخاب شد
#ورزشی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/655186" target="_blank">📅 11:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655185">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هشدار امنیتی پس از وصل شدن اینترنت؛ این نکات را جدی بگیرید!
🔹
اینترنت تا حدودی وصل شده؛ قبل از هر کاری این ویدئو را ببینید!
🔹
چند تنظیم مهم وجود دارد که اگر همین حالا بررسی نکنید، ممکن است اطلاعات شخصی‌تان در خطر قرار بگیرد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/655185" target="_blank">📅 11:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655183">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای رسانه‌های صهیونسیت: ایران اف-۱۵ آمریکا را با دوش‌پرتاب چینی زد!
ادعای جروزالم پست:
🔹
موشک دوش‌پرتاب ساخت چین، جنگنده اف-۱۵ را در طول جنگ ایران سرنگون کرد. فناوری نظامی چین به ایران اجازه داد تا در طول جنگ، جنگنده آمریکایی را سرنگون کند.
🔹
سیستم‌های مرتبط با پکن از پدافند هوایی و قابلیت‌های هدف‌گیری ایران پشتیبانی می‌کردند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/655183" target="_blank">📅 11:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655182">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghYQPaoJICKbLx5EgRW6DLTPds92rBkp_MyKXBGIn0P6jepU12klcpgz0v1EidkFnNR5_GgAZaubhHYhJPBUFbANcmBE9bFo2iI4F_VUXS5P5-nIxhsV-owqqFO08GPPcy-SfkOl5Z4pFTPyceqGLL5bgnjt61QjHwB2tfEClBSQV1muYkfpbUBDGtSPLrJa2l8eTAp5I21aDNuBffaEbzti6gygSg8T3e7sRH4Qk19WEkwwrRgg5nLjuQtEDW01_lZlscLDPDcxnLzBfYd5XA7Md8Gw6f9UaauDN7wkxyx8M-u6Q0Fs7x8G-WDzdidfNI3u8JkL2IKepSWWxygo0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشخصات ملک
برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir/
نوشهر
📍
چلک
۳۵۰ متر زمین
۳۵۰ متر بنا
استخر روی روفگاردن
شمالی-جنوبی
چشک انداز جنگل و دریا
سند تکبرگ و مجوز ساخت
شهرک ویلایی تکمیل
🔻
برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/655182" target="_blank">📅 11:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655181">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a1a43cb2.mp4?token=Bc_oKEywfWodFWmi6NSJta5DHje8tsWM9_w8VQL1wFHOuGk-R2bXjGYWB5WM1rdEM3At2yCoPQvAFiq9EZs7ZAUFrdupNy9CBsN2oxhcNFI9k2oBP7jNgqxPb79Mk4ZPXk1SVAQwX7qvOFJimgDKjnxySc1IfSQpriGWqIfAaWwRR9v5X-dpzhCb44ohXgCXJ46u5zT1uQu16g67qdVnIBbHutOcu0Pdo2g8j7MIIUPXPZcomsexEOpncOILrkuvzMfbrS2QKYQG7yfTg_yL17JJ-N1rd-Mv5FWDnub0ApDdKHv8mJq-LGkonRL2vGI1CUryv_lFcQdUGT_yIxP8MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a1a43cb2.mp4?token=Bc_oKEywfWodFWmi6NSJta5DHje8tsWM9_w8VQL1wFHOuGk-R2bXjGYWB5WM1rdEM3At2yCoPQvAFiq9EZs7ZAUFrdupNy9CBsN2oxhcNFI9k2oBP7jNgqxPb79Mk4ZPXk1SVAQwX7qvOFJimgDKjnxySc1IfSQpriGWqIfAaWwRR9v5X-dpzhCb44ohXgCXJ46u5zT1uQu16g67qdVnIBbHutOcu0Pdo2g8j7MIIUPXPZcomsexEOpncOILrkuvzMfbrS2QKYQG7yfTg_yL17JJ-N1rd-Mv5FWDnub0ApDdKHv8mJq-LGkonRL2vGI1CUryv_lFcQdUGT_yIxP8MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: درباره جزئیات موضوع هسته‌ای هنوز مذاکره‌ای انجام نگرفته  سخنگوی وزارت‌خارجه:
🔹
درباره جزئیات موضوع هسته‌ای، هیچ مذاکره‌ای در این مرحله صورت نگرفته است.
🔹
کویت هنوز امکان دسترسی کنسولی سفارت به ۴ شهروند دستگیرشدهٔ ایرانی را ایجاد نکرده است.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/655181" target="_blank">📅 11:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655180">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c3c5347bc.mp4?token=QwAIu_XXXGEq-TQFjmI94M4Gvjt7yzsIldhJYHa8j246E-PjsaK-YbJH48cfZxb8y1s0Qcsd79uIvKiMFAIeBW7Hn33DtWhyIB1kZYJOPJCJbxmWOB9VfQYsWPR4WJvJzwMHO3Cn6tH8eDg87JJddCkL8vU2S4k04M6DxxFYCYl3OU7FZa9Fuq3elsYEREF73EKmIyHq8_BD2dBZo9tKj0C3V5sn7acJ7tSSmxglNDetzS2daXFtqHEOJcLP9CFPaK_TrMCky3fMdV2s3IwVOYgFsmwHvE7pbt4ZiaacCz1eolFwlHKtFtDkT-rrtW1J_DEk3cWfXmcbitEbEaz4gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c3c5347bc.mp4?token=QwAIu_XXXGEq-TQFjmI94M4Gvjt7yzsIldhJYHa8j246E-PjsaK-YbJH48cfZxb8y1s0Qcsd79uIvKiMFAIeBW7Hn33DtWhyIB1kZYJOPJCJbxmWOB9VfQYsWPR4WJvJzwMHO3Cn6tH8eDg87JJddCkL8vU2S4k04M6DxxFYCYl3OU7FZa9Fuq3elsYEREF73EKmIyHq8_BD2dBZo9tKj0C3V5sn7acJ7tSSmxglNDetzS2daXFtqHEOJcLP9CFPaK_TrMCky3fMdV2s3IwVOYgFsmwHvE7pbt4ZiaacCz1eolFwlHKtFtDkT-rrtW1J_DEk3cWfXmcbitEbEaz4gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: درباره جزئیات موضوع هسته‌ای هنوز مذاکره‌ای انجام نگرفته
سخنگوی وزارت‌خارجه:
🔹
درباره جزئیات موضوع هسته‌ای، هیچ مذاکره‌ای در این مرحله صورت نگرفته است.
🔹
کویت هنوز امکان دسترسی کنسولی سفارت به ۴ شهروند دستگیرشدهٔ ایرانی را ایجاد نکرده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/655180" target="_blank">📅 11:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655178">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94723af1c9.mp4?token=VMmhYA0smEzZnIOP52JwyF1IT7P_gHv5aOe3aNqjci6mHLwCj27phwbMWGY-ELwoJTRKtzp3bhal7UDrmhFcnh1JSFompoqep1YmxQJFDGif9jF4QU9VSd-t4AamMYeDFBOLLDAk54sfDDydK4qakFTA9Mhs1FJdXMZ7-3jDZHwQas9_vKVsZ0pE44xOAsHfTeFoLdOCsCl40fOFicJ5bQBD_BRWibBs2IXKCYIFthGDITrFU2Z41hJ9tsUosu2d_4Z_qU_mI6eH_xOZke2pzjvsxtTErHRxUeMpwIC9_PdJYjx_QdA4OfaThXDnOOArKcp1eotfbUupSgUdGvnJPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94723af1c9.mp4?token=VMmhYA0smEzZnIOP52JwyF1IT7P_gHv5aOe3aNqjci6mHLwCj27phwbMWGY-ELwoJTRKtzp3bhal7UDrmhFcnh1JSFompoqep1YmxQJFDGif9jF4QU9VSd-t4AamMYeDFBOLLDAk54sfDDydK4qakFTA9Mhs1FJdXMZ7-3jDZHwQas9_vKVsZ0pE44xOAsHfTeFoLdOCsCl40fOFicJ5bQBD_BRWibBs2IXKCYIFthGDITrFU2Z41hJ9tsUosu2d_4Z_qU_mI6eH_xOZke2pzjvsxtTErHRxUeMpwIC9_PdJYjx_QdA4OfaThXDnOOArKcp1eotfbUupSgUdGvnJPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: اقدام تجاوزکارانه آمریکا علیه ایران نقض آتش‌بس است  سخنگوی وزارت امور خارجه:
🔹
نیروهای مسلح جمهوری اسلامی ایران در واکنش به اقدام تجاوزکارانه آمریکا که نقض آتش‌بس تلقی می‌شد اهدافی را در مبدا اقدام تجاوزکارانه آمریکا مورد هدف قرار دادند.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/655178" target="_blank">📅 10:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655177">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
بقایی: آتش بس در لبنان بخش لاینفک هرگونه توافق و خاتمه جنگ است
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/655177" target="_blank">📅 10:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655176">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c002955880.mp4?token=MkFPFZslSl8z6i1xLcU4H2Zy5vaQ9TY27UiXjpEyKBQRt3DEeoqUWIrQD8TjXGocuF_6aXcS1WqyGzbYkA7s5QQETzJtv6ZmJlkuXW--Ms-Xks3g7Qj4w1x6rxb6fEgoGHuuU7rQ6f8BQKE6cAMj5CR6MJLTvEHYzbh9ruOgcRlqLifTLXU6Q9nguUtchzNboNecGHHHhfsMyG9QVZt19yC3RZ-U4uS88qTi-LLCpSrS4r--8BwhPwCqpBokMJOTUevhyckLi8NjCdkZf1RIxSjI87WuUANu2LgL4K4_QTa3rZDf5ncmaRcFRJ-hFyzLW1c_rtkLjbyJuBOylH-uVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c002955880.mp4?token=MkFPFZslSl8z6i1xLcU4H2Zy5vaQ9TY27UiXjpEyKBQRt3DEeoqUWIrQD8TjXGocuF_6aXcS1WqyGzbYkA7s5QQETzJtv6ZmJlkuXW--Ms-Xks3g7Qj4w1x6rxb6fEgoGHuuU7rQ6f8BQKE6cAMj5CR6MJLTvEHYzbh9ruOgcRlqLifTLXU6Q9nguUtchzNboNecGHHHhfsMyG9QVZt19yC3RZ-U4uS88qTi-LLCpSrS4r--8BwhPwCqpBokMJOTUevhyckLi8NjCdkZf1RIxSjI87WuUANu2LgL4K4_QTa3rZDf5ncmaRcFRJ-hFyzLW1c_rtkLjbyJuBOylH-uVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: آتش بس در لبنان بخش لاینفک هرگونه توافق و خاتمه جنگ است
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/655176" target="_blank">📅 10:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655175">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b9c9e7f7.mp4?token=ZEfjRUoLMc0-xuk34Qr67W5MFrrEQ_IgVq6LbHC3xELaQdl7Ki63ahK1K57DzT2Ij-Yf1yXbTVo-Mi3Ba9MwNcEwoCKRP5Qj5JdpjcWxN1AZtdwaqRst_D5bDekcQjPVc-R6lokaeAEcrMwMnDeN6LNECC8wRjfNww5ozMoiM-Yo-h8kc1GL_b4hnm_kVY9TLqMnyRXZtEa4_Yw5ntfIeTGi6ZmCRpoCACqYMKsjhYDUDZqrsGARnfFpqnQSjfBj3DEHF6RzUC2-wS8_dLlMhNGsgs8DDEsXdjqDcuuXQUFSgd2KXlQi9Sz_WZCtPBCd-dFAD9bQx78eEUeIRLCPlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b9c9e7f7.mp4?token=ZEfjRUoLMc0-xuk34Qr67W5MFrrEQ_IgVq6LbHC3xELaQdl7Ki63ahK1K57DzT2Ij-Yf1yXbTVo-Mi3Ba9MwNcEwoCKRP5Qj5JdpjcWxN1AZtdwaqRst_D5bDekcQjPVc-R6lokaeAEcrMwMnDeN6LNECC8wRjfNww5ozMoiM-Yo-h8kc1GL_b4hnm_kVY9TLqMnyRXZtEa4_Yw5ntfIeTGi6ZmCRpoCACqYMKsjhYDUDZqrsGARnfFpqnQSjfBj3DEHF6RzUC2-wS8_dLlMhNGsgs8DDEsXdjqDcuuXQUFSgd2KXlQi9Sz_WZCtPBCd-dFAD9bQx78eEUeIRLCPlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرانسه از توقیف نفتکش روسی در اقیانوس اطلس خبر داد</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/655175" target="_blank">📅 10:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655174">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
نتانیاهو: دستور حمله به ضاحیه بیروت را دادم
🔹
بنیامین نتانیاهو، نخست‌وزیر جنایتکار رژیم صهیونیستی مدعی شد که به ارتش دستور حمله به ضاحیه جنوبی بیروت را داده است.
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/655174" target="_blank">📅 10:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655173">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
سخنگوی دولت: فعلا خبری از افزایش مبلغ کالابرگ نیست  مهاجرانی:
🔹
افزایش مبلغ کالابرگ از مطلوبات دولت است اما باید مطلوبات را با مقدورات هماهنگ کرد.
🔹
وقتی جریان عرضه و تقاضا دچار مشکل میشود بازار واکنش نشان میدهد.
🔹
نمیگوییم ورود محدود میشود اما دزدی دریایی…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/655173" target="_blank">📅 10:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655172">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daGtVWHL1KKGo3tyVzEtVimHfykQPQLu9kN3jFsXc7w1v0XezWHM57HOrl5exXIuX6BWkDXemjpOgzWcQAZK9r5hRlmuoPS9WMnPxqSAwLJHA0jLHYiXPXX6nCrdOEBzpSC4sA8-y6i7VFn7FPbP5XBNZZR4567uROTrkoH9zbwX4La6X-sx8jVLh_H5pHYNsEeK-Fh3Zt5v_hahDZiWc-60jaZGl_FZXKyN9J1Rl4PlQmfZnVxD0IRDMFU5J-lQl26vBNlbWvcO_42QHONZy1s6q8Ps9hSW-smOVz5u75bwNl31zrM_HgpQXZH_59HIwREh9igGaWdixVKdYcCNVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بی‌بی‌سی: تصاویر ماهواره‌ای نشان می‌دهد حملات ایران از آغاز جنگ به ۲۰ سایت نظامی آمریکا آسیب زده
بی‌بی‌سی:
🔹
با وجود ادعای کاخ سفید درباره تضعیف کامل توان ایران، تحلیلگران می‌گویند خسارت‌های تأسیسات آمریکا نشان می‌دهد حملات متقابل تهران دقیق‌تر و گسترده‌تر از اعلام مقام‌های آمریکایی بوده است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/655172" target="_blank">📅 10:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655171">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11406001ab.mp4?token=BuSApYR5O0yQRidpdaudlcJxLM02BNunvLRLGkEjD6MzjHpeHoT0leksL2w9C2Ghkoxp0uzhYG6WHzYaYf4LJ9eZkgStJPKa_2p3QGGdpnfDIgyH3mr6p47ocAw7Wwz2KvIY_uCji_9gZVJgTD1owHFqNhzP4NQFDT33uN8w22HSByfOutqViqjwjdgJaGTDYtoCEA-ltfmRIII9YByY6nH6eiA3PRd1XqRZ295R0PV_sd_xtGKTb7kj8Y733EAfcQrRc8teJsv3g5qWfm8yrUL2CVMc4-0l9uJgezSVfX_bg5BsDjNR-KiXANIHBcpQ1lA8ORcmRGLqrFN2x1sFhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11406001ab.mp4?token=BuSApYR5O0yQRidpdaudlcJxLM02BNunvLRLGkEjD6MzjHpeHoT0leksL2w9C2Ghkoxp0uzhYG6WHzYaYf4LJ9eZkgStJPKa_2p3QGGdpnfDIgyH3mr6p47ocAw7Wwz2KvIY_uCji_9gZVJgTD1owHFqNhzP4NQFDT33uN8w22HSByfOutqViqjwjdgJaGTDYtoCEA-ltfmRIII9YByY6nH6eiA3PRd1XqRZ295R0PV_sd_xtGKTb7kj8Y733EAfcQrRc8teJsv3g5qWfm8yrUL2CVMc4-0l9uJgezSVfX_bg5BsDjNR-KiXANIHBcpQ1lA8ORcmRGLqrFN2x1sFhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ده سال تراپی خلاصه در یک‌دقیقه
#سلامت_روان
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/655171" target="_blank">📅 10:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655169">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
اعترافات مردی که طلاهای ۲ زن را دزدید و با گلوله آنها را کشت / به خاطر سرکوفت‌های همسرم سارق شدم
متهم مسعود در دادگاه:
🔹
مشکلات مالی زیادی داشتم. روز حادثه به همدستم گفتم زن کنار خیابان را سوار کند. چند دقیقه بعد اسلحه را کشیدم و او را کشتم. جسد را زیر پل رها کردم و طلاهایش را بریدم.
🔹
چند هفته بعد همدستم را تهدید کردم که اگر نیاید لو می‌دهم. او به شرط نکشتن قبول کرد اما دوباره نفر دوم را کشتم. از ترس شناسایی مرتکب قتل شدم، هرچند نمی‌خواستم بکشم.
🔹
قاضی پرسید چرا سارق شدی؟ گفت: ۱۶ سال کارمند بودم، بعد راننده تاکسی اینترنتی شدم. مشکلات اقتصادی و سرکوفت‌های همسرم به خاطر بی‌پولی مرا به فکر سرقت انداخت. اولیای‌دم خواستار قصاص و پس دادن طلاها شدند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/655169" target="_blank">📅 10:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655168">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHqKCnHK2UEHYF6nifmSdEG-ZqIxdSkJfOt3AK3_YSPk-UMR5typEZr3z9mrzakJZq56MrmhPaCJAs_8sj4_Q4LsVq3B6TaEkECyzsOE8BO3QmS_i2YMfVvJgKF4LVfKKpm0_VUitmLi8LlcBm1X6Ora8xdnVJSU3K4b9_KLQGVEw4CnCrwIM_1As5vIGB8Z226L56u6Yp8FpIRKSuSjCO1aBE0VBK1PP1N38FMqM15P4iB-iCKWCwKWT2DgY1m4eKwtsZ5m3AZvDTh7wOi7e-FcNu_9kvhMbQClOM-FtuYwbJtdCCLdMVn0RNxq2WAGTlrFwcmwlpybEZVi0LsF8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش کمال شرف کاریکاتوریست یمنی به توافق لبنان و اسرائیل
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/655168" target="_blank">📅 10:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655167">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
موافقت هیأت‌ رئیسه مجلس با برگزاری رسمی جلسات صحن
سخنگوی هیأت رئیسه مجلس:
🔹
هیأت رئیسه مجلس، تصمیم مثبت و موافق خود را برای برگزاری جلسات به‌صورت رسمی و فعال‌سازی چرخۀ قانون‌گذاری اتخاذ کرده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/655167" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655166">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
واکنش بقائی به بیانیه اتحادیه اروپایی در رابطه با اقدام دفاعی ایران علیه متجاوزان آمریکایی
اسماعیل بقائی سخنگوی وزارت امور خارجه:
🔹
بیانیه اتحادیه اروپا که ایران را بابت دفاع مشروع در برابر حملات غیرقانونی آمریکا محکوم می‌کند، نمونه آشکار نفاق و استاندارد دوگانه و بیانیه‌ای ریاکارانه و غیرمسئولانه است.
🔹
اقدام ایران در هدف قرار دادن مبادی و امکانات مورد استفاده برای تجاوز، قانونی و در چارچوب حق دفاع مشروع است و دولت‌ها تعهد دارند مانع استفاده متجاوزان از قلمرو و امکاناتشان برای تعرض به کشور دیگر شوند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/655166" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655162">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWaF3yOCiLY-bHqMPvhE0B4hUtMnSB2PAIBL12nbf7bDGUG1Nzh09oIZMKxS1sJUNyhYqqVBnf11cmDhfAaxNELLtSXMgQc3DiazJeAWCP6nAH-LY34yPrcpEYTc3L4jxB5fzxYS9pXLbZstvbwdyXZaXhd4B-MbdxNVfKFzCd7myxeQd61zcgwMzudp_16RqtT3tWUG-919nZcUMbXhLgw_eHobfS7qpuuPQrd3ZWJYRzjKHfV9jlFiEk_YfPSYv5X81hsTNuGyWmSf-YvnDmu6AyWaULvyTzbLqNHZXWv-nDIilddl3S7iIDRmCXS2Q0UzgQpFfcuA1qZRV3tTAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bv_DYMmyK6_B4JbjSLbyorC6JSXtds5QVL9COPkwIQUW_m4JGNxOZrOeFXrUMF5dD56KagVXEsdSFcIWEqtjj6LhUKS3M_Y6u7cT-S6hcuCSd4HB8LGLJ5RK2PJDGXxz4S1uGXFxq07N06jY6F46aObGEru3veoqxUrG7suU2bOJ4kj_aq3wUELUztMaRLq9muoV4gnUL60l5DNLzn0yZVumSjL3MCHcXNXd-btzAgnJ1BDqCnTyns610qx-H-0P4G7wS0tupYwENzjVCe5GHirXOubYcgp1hvNbY4-UOZjAtKkaA-YAQ87bovxPEz85JKVZJe6hkSC8W0HYpnOm0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IUcvalON9KXq74WRA7OFiaQiX66rhaYjqMehPno9BMrg38pWs0FP_Si-QVTOIef_kTYAUgpUeR9OkrDGOgIrjhYPMvzsu7UbmzTDf0eUB4GrUjdBdbGVGa_jx83Y_mMsMwdR5IWoYmntSzlbE4PleqYxxMvXQwckU71NIHPhhMHasFSL9gQJksSZkofEtJA_tbc0FMrJVMDUpRsnQT0KsMGUZb6ThqyI5fzvLa4fENiatv8LkEFNM2uT9Q09B6jgzP5qGi9VPOY1p3hAuppC5fohO2Q0u3iDk5pa73__VcGbVm4CkFgiK72uhyVzbkX5wU5FW9QAKYFYqqGEmMkzkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KnJNRRN2StCIhB8-J6JfRW7RODgjlg4P1EwHpBz4h5UkAlfadGfTzuVFKphGW3ErFTbpMnMIdizL_9OmtEjq_MLOLTFRY5wxtB5nHKUIaKZTiK32VeytZiUm_Jfd686lAQ1UNu9TzP_JelGFN5JoOM5Oc1u5diOxdz4UCZgXdu-Y-Vb1lNLJnt3025p81DPSYT2OgW5U9Q5Fv0XpNx3ppndd7T47-G5ftTkatrgFu9n1WAJAqi09fwKaTbWDs0CveIGh8MYfyDCra_Iy8ItxGB8esNnIIBlsacNGST2pO9pnpulUVgp9FJZjbTMj_ApnccmK8iwD5Du9dNm_haDClQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بارش برف ارتفاعات ترکیه را سفیدپوش کرد
🔹
بارش برف خرداد ماهی ارتفاعات و مناطق کوهستانی در کشور ترکیه را سفید پوش کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/655162" target="_blank">📅 10:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655161">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عضو کمیسیون انرژی مجلس شورای اسلامی: افزایش قیمت بنزین در مجلس مطرح نشده
🔹
کانال ۱۴ رژیم صهیونیستی: امروز رأی‌گیری برای انحلال کنست انجام خواهد شد
🔹
فرانسه از توقیف نفتکش روسی در اقیانوس اطلس خبر داد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/655161" target="_blank">📅 09:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655160">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
جام حذفی رقابت‌های فوتبال ایران برگزار نخواهد شد
🔹
جام حذفی رقابت‌های فوتبال ایران هم برگزار نخواهد شد. رقابت‌های جام حذفی تا مرحله یک هشتم نهایی برگزار شد و تیم‌های فولاد، گل‌گهر، شمس‌آذر، سایپا، ملوان، پیکان، خیبر خرم‌آباد و استقلال راهی دور بعد شده بودند.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/655160" target="_blank">📅 09:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655159">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8EfUxSU4BZUfePzzxMUYPbd0gXvoy9Wzb9DwyVlBI9hKWg_Ra1CPsNRVDUKL6L6-6sqtK9uLxPv4aqjhbl9DlOat68YV5_YY3ONHy1-Vgo0mCn8mtxHjSbncMbweQih8PlrI_UR80hU_HJru8Jpv5tplNPoARm4iEa8uRbt74hJ9utNYqpHN1RC0Wc-9khN5U5b4joiL6JR4MOErYt_ToB6TNuuo1aV1dnl2rO1PjhpkOdEbwOG4YYTB9gwJ9CXIWL1nli26naUYI-xilnnB0Y5z4Oba_xGtyHF-NDoHgb_ty184Gu2ryiM66VQ2RZxXJD4_a3OLy78-yYnT5W-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طاق بستان، کرمانشاه
🇮🇷
#ایران_زیبا
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/655159" target="_blank">📅 09:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655158">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3JNPq--HfNYRnMudMx6zQouK2CMjyv4vO4pHkjUxVCNmqYl6VuRAnBqzPpumPP8Lds1Siewi1Z4_TxCh22KoZoSCkTtvnaBnJC_ZKxG5l6Upo8QyDf-oyLJJqILdKGlsIWMT_juvyX6HNdQM6P2wyHz537CE17sGoHOBGkcupD0rY19_xD5vc4aDwwj-_kjm9pRJkrOt7n8H4E-bEmT5hiiigcQwuuSYnWRZ2SStH9b0MkwHC-KAYnWAeCscIfF8t1AyolloKNfvKnnaw6MAuYfXoHprv6pRg_3-kgXTHZ3GSlb7BsVu8fpyVbGnCjdfZLRh2EV8zjETTmInqoKKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
چرا رقبایتان همیشه جلوترند؟
چون از قدرت خبرفوری استفاده می‌کنند.
✅
تبلیغات در پربازدیدترین کانال‌های خبری
✅
پوشش همزمان سراسر کشور و استان‌ها
جای شما خالی نباشد.
همین حالا پیام دهید
👇
👇
👇
@newsadmin</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/655158" target="_blank">📅 09:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655157">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFrqEy8XxpVQWXx4XCP9YlzCm8g_1EHo1EWTP_aXFnCMH9hK0HetgBrPqv4zK1KLGGhSjDtyqXEr6U_Or8vjNQ-_0Lhv20r_JdhWLa8P5EX9c517odhuEnLk5YH99I1a2qt-lsgkIFff1WrDZjk4pw5P666VbEXVwF2JZKLMrNQhf2phEiXNhdh1wr7YKcrv6YxJUj1RLgwcwgDXTs0AVRngYnQBTZRffvhVHhuFLNcucWniokzeyd6dg_9YdctsaoobV_d3Xj0rx0TkuRLyWcOZ6kbccw7ucydDcykrjAQOavhso4dxN0rs7o9TkmOhuiAT5plREmvstJwIcNDRyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص بورس تهران وارد کانال ۴.۳ میلیون واحد شد
🔹
نهمین روز سبز پوشی بازار سهام با افزایش ۷۸ هزار واحدی شاخص کل بورس تهران آغاز شد و به تراز ۴ میلیون و ۳۱۴ هزار واحد دست یافت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/655157" target="_blank">📅 09:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655156">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0mXcHFHt99xYvyJk27bCP7s12mM1FeYVA40NxHOMkRXx8QAP56o2u_1XWz4VcQ03GZXtYF-dbPwNaRKhlNWJUFFBMRmHEQ4mr2AJnyWy7v66jIHcj41Nx2iyEObJhmWyjTDtUG9wgu3Y_P3yakzQJH2mKpOLsttr49-xwnBG_Tianie47NT6Eimha_2pAGo_6Pc7iXyToRCDqNAiSSLlpwIy9TOtGaLuP8ebszxuuXH4S-hJ76DKHiTdboQ2jqQZ3A8g3ns-wiMre8u67IEIntYC163nWHVE48sVl3psBO2XJDrBsDr5MYiR3rbei-RcmemeSUyz1SbTYvevw7wgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای
نیویورک‌تایمز: ۷۰ کشتی با کمک آمریکا از تنگه هرمز عبور کردند
یک مقام رسمی به نیویورک تایمز:
🔹
فرماندهی مرکزی ایالات متحده در سه هفته گذشته به عبور حدود ۷۰ کشتی تجاری از این تنگه کمک کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/655156" target="_blank">📅 09:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655155">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
مبدا تجاوز به دکل مخابراتی جزیره سیریک هدف قرار گرفت  روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
به دنبال تجاوز ساعتی پیش ارتش متجاوز امریکا به یک دکل مخابراتی در جزیره سیریک واقع در استان هرمزگان، رزمندگان نیروی هوافضای سپاه پایگاه هوایی مبدأ تجاوز را مورد…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/655155" target="_blank">📅 09:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655154">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptvMMbS-Yx8H9Y2tTmRL2P_VXpcWh8tNdgHozo2wzhPZSN2wXo6VitNuJH089iuAJ4o3bPpSkjhO1uNcFyrTjoDAPANNbI3NycwlaZ-6w54XV8DsSiOiUGZLVC7SLb5Xnn4L73Ww9XwAwitf4qVNvgNR2KvdCdKkelraq_NAvWidYZj-1qYVnMn8N82siVYS1JbJhRTXq22byV_7BfRGySmq0ITxnwJJFW87Aiagf7rOLCvIUQhBwDf9EDsmX1meC2VYmJvmjqsmtuJGURaKMlYcs5u2pxfMsfZsZs4DmE1b4ZG1KzA_n868bM_9W2IjxdmJvSCvo2gjyjdYFnySpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای سگ زرد: ایران خواهان توافق است
ترامپ مدعی شد:
🔹
ایران واقعاً می‌خواهد به یک توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
🔹
اما آیا دموکرات‌ها و جمهوری‌خواهانِ به‌ظاهر میهن‌پرست نمی‌فهمند که وقتی افراد سیاسیِ فرصت‌طلب، به شکلی بی‌سابقه و
بارها و بارها به‌طور منفی اظهار نظر می‌کنند و می‌گویند که باید سریع‌تر عمل کنم، یا آهسته‌تر عمل کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست وظیفه‌ام و مذاکره کردن برای من بسیار دشوارتر می‌شود؟
🔹
فقط آرام بنشینید و آسوده باشید؛ در نهایت همه‌چیز به‌خوبی پیش خواهد رفت، همیشه همین‌طور می‌شود!
#Devil
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/655154" target="_blank">📅 09:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655153">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
رئیس بنیاد ملی گندم‌کاران: ۵۰ درصد پول گندم‌کاران این هفته پرداخت می‌شود
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/655153" target="_blank">📅 08:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655152">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyE2i_Ac3x7_WqI--bsfThRfr8i-jXVj1YuKrFrUYTxqOAFiNqn1VksQLeoE-LLIYxc8l8siKSDnsZk9LmIlqbsb_8X57WGxGkHW023StLQDdidAC_om_AOdkW2XMQ2euG6guGOvSCL_8Y8YPep1g0w-qfS7zuN66IBr3wQQ9jAAGIcp-VMhdlACZoKc3LQUzl6MZXvvXV9dirPiS0B48wGHyglT_rCXr2_LqAHwCnt0-AIIUIh7T-tdoYtIOJS5tvP_4yuJzf1m_c0SbcB21XUDr8yqdPhg73MRHobyLSqVwYL6J0038NPwoBymZ_imijkuE3XVWNHeKjY9uIx4FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون بهداشت وزیر بهداشت: هنوز هیچ مورد مثبتی از هانتاویروس در کشور گزارش نشده است
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/655152" target="_blank">📅 08:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655151">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
معاون بهداشت وزیر بهداشت: هنوز هیچ مورد مثبتی از هانتاویروس در کشور گزارش نشده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/655151" target="_blank">📅 08:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655150">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKUgCoyrssp5HfrmPpN6h-fFA7Z0vvCZF2xGJuS_iwzwLECDcT-0grnz3e5YrP9P_y8BT03xRRgqEJy0h4xFosAeH36zKd4euyNbiag6XagtpcysG9AEVWanSeTGxh5M187ecErEvDz1LwwFV3UGg6A0IsTAzLXynMqQxdaydfyJmAhlADIJhXsrxhr4xSdR92pkmR3My79DQe2cdulXzjjAgsgReB05cMVOvlX29Dk3H7A6067bjFOXNF3MVMFRcCl5Mr2rm7BrKCtSN_BwnFXBc_jDoqNU0ZpCT2NdxwD9dpW-9_qb82G3XYt4ZcDfXR_yEhgkiGlHMSq31edtjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک‌تایمز: ترامپ در ایران، اوکراین و غزه به بن‌بست رسیده است
روزنامه نیویورک‌تایمز:
🔹
ترامپ که همواره از خود به عنوان «سیاستمداری توانمند در دستیابی به پیروزی‌های سریع و قاطع» یاد می‌کرد، اکنون در سه پرونده مهم ایران، اوکراین و غزه با واقعیت‌های پیچیده میدانی و سیاسی روبه‌رو شده و به مرحله‌ای از بن‌بست رسیده است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/655150" target="_blank">📅 08:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655149">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ترامپ ادعای تکراری خود را باز هم تکرار کرد
🔹
دونالد ترامپ، رئیس دولت تروریستی ایالات متحده در ادعایی تکراری باز هم مدعی شد که ایران به شدت خواهان توافق است و این توافق برای آمریکا و طرف‌های مقابل ما خوب خواهد بود.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/655149" target="_blank">📅 08:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655148">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWida8fvoWtNuecgvvIup-WZxKHD2UtvD2jxn1BHQ79i8fnFOLB1_p7mpiIgMBL8gxC_oc4VOD691qXwi1h-JeEHaGinDSZn1NEfHJYVfQnTGaf7JPG-hkYvoc0mmBTBP0KaZ6xMPGXmweITnSrmNzRGNgTLFAZ8wgnZ6KNuv_0Wg2ZNltntxzWcmArRKMrU_3SnL3jM1kZ8xN3he4PZbnXnkvRGL1VDtZfBZqWGJPuB3gy0PeeDK62HYjev_hqWeeU_LYp8JDi-xOnl5fZZAd2HO2qGpVlvED4J-GT_GrFBC2EP4SEk6Af14YqewJ1nfL6Qmdhcuo49NbiFsLJwiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازدهی بازارهای ایران در یک سال گذشته؛ طلا اول شد، پژو ۲۰۷ دوم، دلار همچنان در صدر گزینه‌های امن، بورس بازهم عقب افتاد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/655148" target="_blank">📅 08:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655147">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47d9a802d1.mp4?token=icNR5U8SdqYjLbQK5AgAv8LVi383Z0ryvr-4_3m06rmV0C_MVNoVOVA3SzBJ_jQHHGw8x9zgCizjvNnJvpd4P3g_HyZ-CPP9AgKrVhbfklzd0A1gY_jNL-Je1r0mwZQdBCLGZNKiIqo5V-Yoy9PvHbHajimm_j4FerKXvTz399jcNQc6efbWTcsWkwA3gSjnINfmDlPh9AfywLeKT_scxF1FzX2vC3qUAmOwQUuEeCaGV6GNtPAjLuBuxQJ6u9cCXThetjbAEWmCUGIhVp1YCwetW3kxcZS4hVOcTKWbS27OoYfWOlgiQuhPCVjPb2T7CHeYEkDsTQpdgCOhpJItxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47d9a802d1.mp4?token=icNR5U8SdqYjLbQK5AgAv8LVi383Z0ryvr-4_3m06rmV0C_MVNoVOVA3SzBJ_jQHHGw8x9zgCizjvNnJvpd4P3g_HyZ-CPP9AgKrVhbfklzd0A1gY_jNL-Je1r0mwZQdBCLGZNKiIqo5V-Yoy9PvHbHajimm_j4FerKXvTz399jcNQc6efbWTcsWkwA3gSjnINfmDlPh9AfywLeKT_scxF1FzX2vC3qUAmOwQUuEeCaGV6GNtPAjLuBuxQJ6u9cCXThetjbAEWmCUGIhVp1YCwetW3kxcZS4hVOcTKWbS27OoYfWOlgiQuhPCVjPb2T7CHeYEkDsTQpdgCOhpJItxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از پاسخ موشکی ایران به سمت پایگاه آمریکا در کویت
🔹
پس از انتشار این بیانیه، تصاویری تحت عنوان پاسخ ایران به تجاوز آمریکایی‌ها، در فضای مجازی تحت عنوان پاسخ ایران، منتشر شده است.
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/655147" target="_blank">📅 08:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655146">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eP_ez3w7h0mF9HQqb08NMnBRWpefg7HxccYuDvo2p_PQE9VBvJKI_E3VFMY0CYqdRCSpx0DTqrFcpPZIztROE4ZizL1ebomPpeu9sG81X6RCd79Js7T2opXMd31qmFq__Id61htlVMx2lNm9Nt0UTM_o2hdOPkkS0XGXc_iL-Nk4Uj_nOQiAToQO7hLLh6K2D0oCc1GmG-jPGL8gcpKMX5Jvqh3u8IkLV_mq6WSJiSor2K0WQwgdOwD5B4K6ESg2c7ybCEqjmohVqB9yrFnECR1bvwcNFraDskND7_O92fjlmc6tZUE-JATYzx1hR0_YCe6u361ofvzri0g3AkT1ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام معنادار بقائی به مناسبت سالروز میلاد امام هادی(ع)
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/655146" target="_blank">📅 08:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655144">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/369862f740.mp4?token=jcE-xYbXDUD_DSbwHoK7AOWUfnpGKAjUv8d0UD39CgLjW2fUvSPPUrHer6ZFn84ybMp9C_tZHFMhH8IYCH16t29rfc5qcuFKuZdE_CSU8xNKlzGHFesPcA1g-Y2VQv6naMLTXROgmk3wWccQPGT-1QEtpDKls2gHd1mpzDZx_wJcmWa0q_dXtbqRs2HMe042mq74LkUUmdwjvyzyNJeD52OzCRDMEMvec3sbhuBZAH0Qy9qNx0xoA0ufC1es9HfyhPIAvjrLVInBQC22M10Nwti-8zmHWFSAJRcxPTV8KDITLZ-ykkkEY4U7Rc1u8jgk59H_uaJJlt6Zk6BG5V5pGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/369862f740.mp4?token=jcE-xYbXDUD_DSbwHoK7AOWUfnpGKAjUv8d0UD39CgLjW2fUvSPPUrHer6ZFn84ybMp9C_tZHFMhH8IYCH16t29rfc5qcuFKuZdE_CSU8xNKlzGHFesPcA1g-Y2VQv6naMLTXROgmk3wWccQPGT-1QEtpDKls2gHd1mpzDZx_wJcmWa0q_dXtbqRs2HMe042mq74LkUUmdwjvyzyNJeD52OzCRDMEMvec3sbhuBZAH0Qy9qNx0xoA0ufC1es9HfyhPIAvjrLVInBQC22M10Nwti-8zmHWFSAJRcxPTV8KDITLZ-ykkkEY4U7Rc1u8jgk59H_uaJJlt6Zk6BG5V5pGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مبدا تجاوز به دکل مخابراتی جزیره سیریک هدف قرار گرفت  روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
به دنبال تجاوز ساعتی پیش ارتش متجاوز امریکا به یک دکل مخابراتی در جزیره سیریک واقع در استان هرمزگان، رزمندگان نیروی هوافضای سپاه پایگاه هوایی مبدأ تجاوز را مورد…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/655144" target="_blank">📅 08:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655143">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
آکسیوس به نقل از مقام‌های اسرائیلی: اسرائیل از دولت ترامپ خواست مجوز اجرای حملات گسترده در بیروت را صادر کند
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/655143" target="_blank">📅 08:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655141">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dThWcBXBMZGJQFTg_KSCRmaxm5cYN6ho_twRN6kGSumzYT3prYCg0gk5UcRC_wGc2HnrWHNRDBvl9X6Tls1PP_GuH8BP0oI2Upl0cqJs6Q5FRPxt332UJN898fmvo49I3wOl9PIIGSjn8htuPIJySMc4G8bEjE0hg9Np7_iSC6f1qRTU2V9NXvHPon9oBISZFphqlRduwOJm6HFd1vqCLS_aaObVK6mq1pmKaVXvDTxCm6N5dJSmNC3shqWNo5yh2K4hrLIBP5FQlwfr9042nKm-jNEfmAFur36_hEFUv0FjNM-wKFqVvKzmRZbEI2njCWiq6SV8P6vAIp4a78dTHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/muaEdpBrEOLff-W25z7KBBpZQTqf7IpiwlqxQZ9gGKWPW9AxkzuPFjsc_H6gvfP_n_nh5fOj2hPC71884B1N8Fyd17T1dKvSdTlPUw97Mi_-mnZKmKf-TxLc-kh-Gvz727LuRv5JWTa4FB-9d8w1nN7vn68QIXpVeZ7zI9FyZ7xa3Waxtgya2sm5QNVSB61I3OtjcB6IGDZoz2CA_66pdUJgZJgAMVsA5k6E9EZWtzq0htvFjG-hZJpw4J58eyEmsMNW4jtNEyE-wHTne_bLhWunLP095LfcyPwHVMl97x2FuiCiV3G2rTvZN2L486JBfV0PfcQtVxAsYekYujL6sw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حکم
اعدام ۲ لیدر کودتای دی ۱۴۰۴ در تهران اجرا شد
خبرگزاری قوه قضائیه:
🔹
مهرداد محمدی‌نیا و اشکان مالکی، از عوامل اصلی آتش‌زدن مسجد جعفری در محله کوی نصر تهران که اقدام به تخریب و آتش‌زدن عمدی مسجد، تخریب اموال عمومی، درگیری با مأموران انتظامی و حافظان امنیت، انسداد خیابان‌ها و ممانعت از عبور و مرور مردم کرده بودند، پس از شناسایی و دستگیری، رسیدگی قضایی و تأیید حکم در دیوان عالی کشور، اعدام شدند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/655141" target="_blank">📅 08:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655140">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deefa7d677.mp4?token=jm72bIHxFk8kX0BHtK1VVAKSa1RXmIN-qCkLBoZXA6-ROcUMmy8_UfrIlT_9EL2T_QGBGPPyWb9cUU4jH7BTpEkRZvo_LecSDmTPWd7_HELrNmZhv3MQfc_TdRYmJqMWorKQ3DXreNO7t8Brhx-7Jz8xAHJDwwnMMgOD2IZel4feH6655WsYHtjP2GdLO6boKuBWJWxdJF0xHKXVRrlUx6t6baFps5Uex6GpY50xDWQuZvoe7ohSkw-7woi1rVvUeUiNx9QG3lwjdz164msQ5jEkzB__SELazSDaoP2eW-X5vcNNTqZRc9D8zDTdg9gEy570kOhyhr5-t6kQ5y2jLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deefa7d677.mp4?token=jm72bIHxFk8kX0BHtK1VVAKSa1RXmIN-qCkLBoZXA6-ROcUMmy8_UfrIlT_9EL2T_QGBGPPyWb9cUU4jH7BTpEkRZvo_LecSDmTPWd7_HELrNmZhv3MQfc_TdRYmJqMWorKQ3DXreNO7t8Brhx-7Jz8xAHJDwwnMMgOD2IZel4feH6655WsYHtjP2GdLO6boKuBWJWxdJF0xHKXVRrlUx6t6baFps5Uex6GpY50xDWQuZvoe7ohSkw-7woi1rVvUeUiNx9QG3lwjdz164msQ5jEkzB__SELazSDaoP2eW-X5vcNNTqZRc9D8zDTdg9gEy570kOhyhr5-t6kQ5y2jLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۹ حرکت یوگا برای کاهش درد، تن و گرفتگی کمر #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/655140" target="_blank">📅 08:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655139">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTuloqB5BJ9LBbSa4UIWC5ayL97P_r8oX6TrYOoJWgh_GqdOLqdBhhqCPdGe3E8iUjezNzcw12L66L-lzme0_-Mam6CekwyaG2Y5_qY5E9ppOsWcHM-3UAwYWh9_Q3dSY3fFxTVGUfUB4hBNNPRHsxRoHwxwlWHsg48Hp-TEX0Gz0lTlaUE4V6oLUF6QeaVPwdUXavuBQaMxO1Ndvhok9GWNFysKMI4u2wOeIxrNjBPDSwUpv7GFsIyJH3S91_xDFKXnyXTHUIVWMeHminqSMyJOLiOzHV3NlnNiekNfOQ8IlMBnufDXYTvUHCTCVokB8vDyAvRxb1KjoCqxzpUEzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تالاب سولدوز نقده در آذربایجان غربی پس از ۱۵ سال سرریز شد
رئیس اداره حفاظت محیط زیست نقده:
🔹
آب مازاد این تالاب به سمت دریاچه ارومیه هدایت می‌شود.
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/655139" target="_blank">📅 07:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655138">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B34uTmXG8b81ibX7DUPoPdBF92cs3yI4bNKmj8HSNFx9OZCrUmA0y0kcmpqjn0DsamE6dXcr5-ECcCzArrFXjgoUT7BETtFhonXdnrd_YT984iKtIFbDxnfQoMp7GwU6_UuYxaRAvX-LQPCv--sSe2jpTWXPFWkfwmb2B3yKZSq48Jh3L6yaumGEtVVl1tdMLzqsdzLXjD9PdRLv1oluwV6YgZE-ddQFDtCylI5YsZ3RZpaIbBrwIU67blH8Wd4TtWS9RpOuRVI9NsaY8abyZV4fi3J9sSAptObGGCUXduaakZj9P2Mt5mUHQp21reIXIWJItsYDXzFjWGrDduYegg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات قتل ایلیای ۹ ساله در رشت
🔹
ایلیا زادحسین ساعت هشت و نیم شب ۱۶ مرداد در حالیکه مقابل خانه‌شان واقع در شهرک حمیدیان رشت مشغول بازی بود، به طرز مرموزی ناپدید شد.
🔹
تلفن همراه ایلیا دقایقی بعد از گم شدنش سه کوچه بالاتر توسط یک رهگذر پیدا شد.
🔹
در تحقیقات…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/655138" target="_blank">📅 07:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655137">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9MUNgS6VTgF5Uy1wrx2u2ctS7pVTbYXGaCtSFSz8zMpIcNXPYTuRa77VuxHvNUvn3itJKydpXJscVoG3GgJR0t4u1GmJB6U2xxqnhmIoNXm6xS7HSzowpoM5zWaG4bwiEZHsotz0us2wejyPdvaKauqPujvQXuSERDB2IPAc2280YjCO_6uMzo_tlG2ltrYFXdhYFoyYCAFk1eEq__X9tZfl9NyHGeyVzJLbBxqxjoHRy3-f3zVF4h2CgQioNB7SjYxBHSPXFk1fVFguPucALObAY7P8FiAddl9gQa8sYcl7Xi7NBlBU_0uKefMyLN-Q75ItqLKl92EiFhqACbJtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای سگ‌زرد: سی‌ان‌ان حقیقت توافق با ایران را تحریف می‌کند
ادعای ترامپ:
🔹
شبکه فیک نیوز CNN امروز گزارش داد توافق هسته‌ای من با ایران راجع به "هسته‌ای" صحبت نمی‌کند، در حالی که واضح نوشته شده ایران سلاح هسته‌ای نخواهد داشت.
🔹
بخش اعظم توافق درباره همین موضوع است. CNN و دیگر رسانه‌های فیک نیوز، یک فاجعه کم‌بیننده هستند. حتی با مالک جدید هم، بعید است روزبه‌بودی پیدا کنند!!!»
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/655137" target="_blank">📅 07:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655136">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
مبدا تجاوز به دکل مخابراتی جزیره سیریک هدف قرار گرفت  روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
به دنبال تجاوز ساعتی پیش ارتش متجاوز امریکا به یک دکل مخابراتی در جزیره سیریک واقع در استان هرمزگان، رزمندگان نیروی هوافضای سپاه پایگاه هوایی مبدأ تجاوز را مورد…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/655136" target="_blank">📅 07:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655135">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
آموزشگاه‌های آزاد حضوری شدند
رئیس سازمان مدارس و مراکز غیردولتی:
🔹
مراکز غیردولتی اجازه دارند کلاس‌های خود را به صورت حضوری برگزار کنند.
🔹
مدارسی که مجوز رسمی فعالیت آموزشگاهی دارند، و همچنین آموزشگاه‌هایی که فضای مدارس دولتی را اجاره کرده‌اند مشمول حضوری شدن هستند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/655135" target="_blank">📅 07:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655134">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
گفت‌وگوی روبیو با عون و نتانیاهو
یک مقام آمریکایی به الجزیره:
🔹
مارکو روبیو وزیر خارجه آمریکا با رئیس‌جمهور لبنان و نخست‌وزیر اسرائیل در مورد تلاش‌های دیپلماتیک میان بیروت و تل‌آویو گفتگو کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/655134" target="_blank">📅 07:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655133">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVHKrSLoswDcvw83Mw2lO3iTE5VIKRn1MD6nqap73AEAkrub4bv76-c_zQupoWKOXhK6uAJBTbBvhT61WhzYmENpqsjkDSbvNLvkx9HMnlGfnGUPpktzaWyDrT0mz-zUi4g7c6vqIL9gmutt-hBPOsy915q1eNUEmJnE4cHkvM0m0GLneppkhj6zRB5i-K5lAmJwkrZA0Q9uJRkGy2eSrR489PL1Y8qODEF0cePXuFivqz3InpcKqaz5WgucgKWBiTjnETGhVfC7WCKLJknlkAWaK-Th3oXWa76TgZI4uWqdpMHnAfHrC546kx15bJ1XhKId45kXzmupau7EPyyw-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صفحه اینستاگرام کاخ‌سفید در دوره اوباما هک شد
🔹
به‌گزارش راشا تودی، در جریان این حمله سایبری، علاوه بر انتشار تصاویری از حاج‌قاسم سلیمانی، پیامی با مضمون «کاخ‌سفید تحت کنترل شیعیان است» در این صفحه منتشر شده است.
🔹
هنوز مقام‌های آمریکایی درباره جزئیات این هک و عاملان احتمالی این حمله سایبری اظهار نظر رسمی نکرده‌اند.
🔹
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/655133" target="_blank">📅 07:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655132">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idCQuKIiwVUTMG_x86TgAmYuKi25ZEMkggn7XhKzn6kdxErGjfme9pE_zWPoobpodXzVP0iWufUbbIKTMe8Etl580Ux5BOlA0NcQQovCamIXzuDkEGVSvFhlpZ-hBKqGeSLsPMtDIz1KNL69SEQLvJpQ8rLtuGQ78oXI1_kFKxlV-lMyzfzPqmtSx2UI4iepU4kkFFJhloPQs_h5O84jA2CyqRDxE4DTKNJQNuPf0JXw1uF5y13zgHPX1SSrPXAMkEDDsVL9f6USMPJKjoV_zSM0ovcCQOmubpHz_Lsa64sSAscN3qBl75xwlATlSE9hpUrgav9oQ_9G-OdEa8uN1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۱۱ خرداد ماه
۱۵ ذی‌الحجه ‌‌۱۴۴۷
۱ ژوئن ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/655132" target="_blank">📅 07:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655131">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
مبدا تجاوز به دکل مخابراتی جزیره سیریک هدف قرار گرفت
روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
به دنبال تجاوز ساعتی پیش ارتش متجاوز امریکا به یک دکل مخابراتی در جزیره سیریک واقع در استان هرمزگان، رزمندگان نیروی هوافضای سپاه پایگاه هوایی مبدأ تجاوز را مورد هدف قرار دادند و اهداف پیش بینی شده منهدم گردید.
🔹
نیروی هوافضای سپاه اخطار داد در صورت تکرار تجاوز، پاسخ کاملاً متفاوت خواهد بود و مسئولیت آن به عهده رژیم متجاوز و کودک کش امریکا است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/655131" target="_blank">📅 06:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655130">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
برخی منابع از شنیده شدن صدای انفجارهایی در منطقه الجهراء در کویت خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/655130" target="_blank">📅 06:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655129">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ارتش کویت از فعال شدن سامانه پدافندی این کشور خبر داد
🔹
ارتش کویت رسما اعلام کرد: پدافند هوایی این کشور در حال مقابله با حملات «موشکی و پهپادی متخاصم» است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/655129" target="_blank">📅 06:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655128">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
صدای آژیر در کویت فعال شد
🔹
برخی منابع خبری منطقه از فعال شدن صدای آژير هشدار در کویت خبر می‌دهند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/655128" target="_blank">📅 06:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655127">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b32ef18ff5.mp4?token=lRqC5cEXgSg7OtHDulJNmV8gSRGUkZvGOG2S5mOmKWrB5KSqju8V5rPLSOJQ9puvUigXWklc2n3t3tawSxSnS6xIg0z0gal71ahPqltzu3kz5dCx5QQoRbwmcSto4F7yMD16QLq-Kg5LRKBfFlv5Vua-crz7vm8R4rt7WLD0G_O20yGDUly418w6OswFR-5kB9us9CYO_BHdFJ5MWHRnu6BXQAEEY9DI0FJjveUyvsgxr2ylx6XbCkvVANSk4vexyRDxjoftfvi6Ed-Pq3k3ukTohFTkBaJvtz801nv059_1uLo9gxPxyqoNBJmEyRElaT-nc0IYe1mKAGO1d2Fo6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b32ef18ff5.mp4?token=lRqC5cEXgSg7OtHDulJNmV8gSRGUkZvGOG2S5mOmKWrB5KSqju8V5rPLSOJQ9puvUigXWklc2n3t3tawSxSnS6xIg0z0gal71ahPqltzu3kz5dCx5QQoRbwmcSto4F7yMD16QLq-Kg5LRKBfFlv5Vua-crz7vm8R4rt7WLD0G_O20yGDUly418w6OswFR-5kB9us9CYO_BHdFJ5MWHRnu6BXQAEEY9DI0FJjveUyvsgxr2ylx6XbCkvVANSk4vexyRDxjoftfvi6Ed-Pq3k3ukTohFTkBaJvtz801nv059_1uLo9gxPxyqoNBJmEyRElaT-nc0IYe1mKAGO1d2Fo6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#آراپیس
( آرسکا )
💊
کپسول مفاصل آرسکا
🔸️
غضروف ساز
🔸️
ضد درد زانو
🔸️
آرتروز گردن
🔸️
ضد دیسک کمر
🔸️
درد سیاتیک و ورم مفاصل
🔸️
کمک به درمان بیماری های مفاصل
🔸️
تنگی کانال نخاع
برای اطلاعات بیشتر عضو شید
👇
👇
‌
https://t.me/+U65oequC0vhwZpKY
‌
ثبت سفارش ارسال عدد ۱ به شماره تلفن
09146342317</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/655127" target="_blank">📅 00:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655126">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvrZ0uBk-QMle3bXnrm7rskz8Zl1TloIsZGAekY8XckvEZu_-997cNcwwf68o1J8keMWd6Qqe_N8ax_owA_YARTZYFytGYjKXD-3OExqR7IgWGb373p9kSYgzbS2fgPf54sr4h_RKLtiYsaQ7epDMNMAUEb6C-0Oku4TigWDpZCF_-TxIzEXGnZQS_hKtJbYJumHx-LXI_EFBZ_-YudDMACTO8hujl31OrgxhI6-vvvE756Nx08NLTPV4Frbg9IpDsARo81jcwf8UyCGmhBTOESMgQ0MVspfnGYQsoCCkbkXqUnOmEWCDNK4gcHWjvogCf2XGPpBgotrBPjyImPuHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/655126" target="_blank">📅 23:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655125">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار شدید در اربیل عراق
🔹
منابع خبری از شنیده شدن صدای چند انفجار در حومه استان اربیل در اقلیم کردستان عراق خبر دادند.
🔹
المیادین: مقر گروهک تجزیه طلب «کومله» در اربیل هدف حمله قرار گرفت
.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/655125" target="_blank">📅 23:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655124">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLuFNjdi47EC7X6eaM8z4q_4-YqWyRHANLVJyMwVnjiSnsDFQSSddFAYb4lSzhe2DnY6mgLsEtsQDCACV0NMfXnn2q7ikvbEPRsztbOfnvGqS9mX0Mg5FC89dYVewRoEIYrXUAcVZ9irZi2Ew4w7Exugg6rbFDXsiTZ6qWOZqvx3zq-b3MeIK9f8E4Pe1UPjv2F6-OpCnF6QzOZRIMy8OvdI9BdHWQO8pnQOFt_lA9E4OLGZ7fi8r23fsI4rA-yxRNvKEWnfACTfvfcuTBMNlJhSR1m1lj7sGqy8YuTR54cM1mf-FxSXvLAu8iwQyDcsUHHsn7F0eSiC77ZdXW696g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
با یک بار ورزش در هفته هم می‌توانید لاغر شوید
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/655124" target="_blank">📅 23:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655123">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/889980ef31.mp4?token=i_E89N3wQ2mL3BWqbnDfDMTwwpYRm_jQNSKvnYtDj9MWdBHTJctJAg6tv1NtABYBxZs9-gAy1pjA-Q4FIePJC7ogekY7r0wDICyalHzwDuYB7tP-FbCgYAwzPwMEAIfjSKRBYM-8MwI0etLwBrf3OF02-pzCi8sWjpY2tMEPm9au4OfYK6ZuhG80616wP0D9BC39infqpLJI6JNat45GFFlwCxZVhzwq1XZkQlJdEKnoQzWyHF4sdCurKByMnkW209s0BYG9TDb82jra148KH36l7_Fx_TSthagp-ZnlaAPl29prYACFRlmsq4a7Ui5h4_tC09Iquml6ufx3pZa56g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/889980ef31.mp4?token=i_E89N3wQ2mL3BWqbnDfDMTwwpYRm_jQNSKvnYtDj9MWdBHTJctJAg6tv1NtABYBxZs9-gAy1pjA-Q4FIePJC7ogekY7r0wDICyalHzwDuYB7tP-FbCgYAwzPwMEAIfjSKRBYM-8MwI0etLwBrf3OF02-pzCi8sWjpY2tMEPm9au4OfYK6ZuhG80616wP0D9BC39infqpLJI6JNat45GFFlwCxZVhzwq1XZkQlJdEKnoQzWyHF4sdCurKByMnkW209s0BYG9TDb82jra148KH36l7_Fx_TSthagp-ZnlaAPl29prYACFRlmsq4a7Ui5h4_tC09Iquml6ufx3pZa56g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با رشد سرویس‌های اعتباری در ایران و افزایش تمایل کاربران به خرید قسطی، انتخاب پلتفرم مناسب اهمیت بیشتری پیدا کرده است.
توی این ویدیو، پلتفرم‌های فعال این حوزه را بررسی کردیم تا ببینیم هر سرویس اعتبار را با چه شرایطی ارائه می‌کند و کاربر در نهایت چه مبلغی پرداخت می‌کند.
هدف این ویدئو، کمک به انتخابی آگاهانه‌تر، شفاف‌تر و کم‌هزینه‌تر در خرید اعتباری است.</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/655123" target="_blank">📅 23:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655122">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Va1FZbJYTorSTad2pRgzBTXMhGdAO58PNi3Tnx7vz0LpwnwhshgjKSV49wtZ6Mgem-_FcitgLyvOiQosncZSKNKR-xSfti0Op7-uj7CXFkHouCObc8a7s4L0zvcLFJshrJSj1cYn0SUItHSTmfbffR7MKYYBYWXzjtsLj4GZji0qaLwz-jIecsZyJIP8JjsYllPrZJn15We0euZ6XVRhfrSFg78v4_zisPv94ksn8jkcAT_xD0wJ3sLB1LL9N3KJrrTED4Ci8ngNBaSg-gF1AffEUgoPhcooOLNjDcn0QSliBxXt63wecNN7k-68sNJeMqK8trV3mQIw-NbGjlyCVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رژیم صهیونیستی قلعه بوفور را تصرف کرد | قلعه‌ای بر فراز جنگ | اهمیت استراتژیک بوفور چیست؟
🔹
امروز نیروهای نظامی رژیم صهیونیستی کنترل قلعه بوفور در جنوب لبنان را به دست گرفتند که این اقدام نشان‌دهنده عمیق‌ترین پیشروی آنها در خاک لبنان در بیش از ۲۶ سال گذشته است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3219361</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/655122" target="_blank">📅 23:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655121">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pzlz7qKhKdHbFkVBBuIkwJooUPQjxgACjjBc-9LRAcPrJY3JNoEGuHbG3-cvkXvYg4_PaT7L7CT7MMv9H0-TZLRYqZpGMCGBoYGL9ctyd_vUFy0xmdnIE3K-Qwg5MwHWCqLglhArx10q8atjVRUeBbpXeiz5zGKRY6MkI2seIk7WoAVAhyUQi9nBASXOrXnQxLCZxS0Qa9p_zh6eYlDGZ9FLQiS95Ust7-kRjU0Jw0MxBtgXQ6-790Pk0baf_IiJiU_7LrKu1UUwZ7tCOMLB8SDB0QdQSdhM0kxzQ8NNYfheTeKskX9wi1Yxw6-vfZHEJKBqYZlP3KeBF1LRIrhCCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخست‌وزیر دانمارک: جواب ترامپ را واضح دادیم!
مته فردریکسن:
🔹
رئیس‌جمهور آمریکا درباره تمایل خود در مورد گرینلند بسیار صریح بود.
🔹
تمامیت ارضی ما باید محترم شمرده شود.
🔹
معتقدم که اروپا باید کاملا مسلح شود و کاملا بتواند از خود دفاع کند.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/655121" target="_blank">📅 23:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655120">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromایران روشن</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90222c673.mp4?token=hRZh2jW2LiZc8l9g5Xq9npCCktkmRqjJ-As4V2Pd3n1mP6JuWrZGriHKx0XyzEDJR_AI3e1r_wMqqdfAxN5YxFjOOonux8zsr2DtCSvZ97_uPAFvS9QY9cYQ2t8Tko8zqxBddOM1CtIHnlyk0ekb5PjHSt27ryBJn9B-ezCNiB2vH5JaDo-PjsygkitvtlR99ANqQjqZqI0iNr0q6tK3yTcWPF3kg-Z9xiOqOlAWly8cjMLAejOl9H4WjhejLSLWG9Cb8urVYAHcGuh62r6BjkbDjb7mRVJiV2q2IDenR2EtBiMdX4w_VlDSfZMN6fo9EnJmFA7kcTZP1VQ-0ttwHEJuYB-SwemQn_32JlkgFJCqx9MAK6EVIYPFM9TmBFid3h4a_1ID8fUgWDu-ofism5Yw0Li4tBm2D4PWml49pIoyWYSlUiUHBjXS0Vs8GElJ5nYHRMH3L1e24D1t1oaAj4szQi7BOjd92RjbEp0OkeS5UunP_2rIjVai7tekff5gfC4zC0AmFV8g4R4vK5ozz_grdn75ES6Bl0mQLBh47QEBt_C8uJUI82BgadAlSiC9BHb3viUI4lWWhR9S7SKxNgBKHJu_HRoZGpB6tPeVwYBHzTeFQdwwEvjEh5ArC7n4lIyogcc-5jQJsvKjXSM06-SydMYMCamBWUcvMXFc6do" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90222c673.mp4?token=hRZh2jW2LiZc8l9g5Xq9npCCktkmRqjJ-As4V2Pd3n1mP6JuWrZGriHKx0XyzEDJR_AI3e1r_wMqqdfAxN5YxFjOOonux8zsr2DtCSvZ97_uPAFvS9QY9cYQ2t8Tko8zqxBddOM1CtIHnlyk0ekb5PjHSt27ryBJn9B-ezCNiB2vH5JaDo-PjsygkitvtlR99ANqQjqZqI0iNr0q6tK3yTcWPF3kg-Z9xiOqOlAWly8cjMLAejOl9H4WjhejLSLWG9Cb8urVYAHcGuh62r6BjkbDjb7mRVJiV2q2IDenR2EtBiMdX4w_VlDSfZMN6fo9EnJmFA7kcTZP1VQ-0ttwHEJuYB-SwemQn_32JlkgFJCqx9MAK6EVIYPFM9TmBFid3h4a_1ID8fUgWDu-ofism5Yw0Li4tBm2D4PWml49pIoyWYSlUiUHBjXS0Vs8GElJ5nYHRMH3L1e24D1t1oaAj4szQi7BOjd92RjbEp0OkeS5UunP_2rIjVai7tekff5gfC4zC0AmFV8g4R4vK5ozz_grdn75ES6Bl0mQLBh47QEBt_C8uJUI82BgadAlSiC9BHb3viUI4lWWhR9S7SKxNgBKHJu_HRoZGpB6tPeVwYBHzTeFQdwwEvjEh5ArC7n4lIyogcc-5jQJsvKjXSM06-SydMYMCamBWUcvMXFc6do" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جیک جیک مَستونِت بود ...
فِکرِ تابِستونِت بود ؟
+ شُمام
#پیک
شد ..
#قطعش_کن
. . .
مِثلِ ریز‌عَلی ، مثل امیر ، مثل آقا ذوالفَقاری
🕶
#ایران_روشن
💡
جوین شید خوش میگذره :
@IRANroshan_Media</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/655120" target="_blank">📅 23:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655119">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔹
خبرهای داغ امروز و امشب را از دست ندهید
🔹
🔹
پزشکیان استعفا داد؟
👇
khabarfoori.com/fa/tiny/news-3219368
🔹
پشت درهای بسته چه گذشت؟ | طعنه‌های تند ترامپ به ونس فاش شد | مذاکره‌کننده اصلی با ایران کنار گذاشته می‌شود؟
👇
khabarfoori.com/fa/tiny/news-3219292
🔹
رسوایی بزرگ/ خواننده مشهور به 4 نفر تجاوز کرده است؟
👇
khabarfoori.com/fa/tiny/news-3219320
🔹
حاشیه سازی نماینده تندرو با آیه ای از قرآن و تیتر «چه کسانی شایسته جایگاه رهبری‌اند»
👇
khabarfoori.com/fa/tiny/news-3219141
🔹
گزارشی از جدیدترین اخبار گفتگوهای ایران و آمریکا و احتمال جنگ در منطقه
👇
khabarfoori.com/fa/tiny/news-3219088
🔹
ویدئو‌های جذاب را در آپارات ما ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/655119" target="_blank">📅 23:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655118">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بانک مرکزی: رقم وام ازدواج مشابه سال ۱۴۰۴ است
.
🔹
هاآرتص: هدف اصلی اسرائیل اخراج ساکنان نوار غزه است.
🔹
قطر خواستار فشار جامعه جهانی به اسراییل برای پایان دادن به حملات علیه لبنان شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/655118" target="_blank">📅 23:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655117">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPCwt-SySIG9_t7mz9H8Nar9VVAEX717tQuDEu1r8cGaiTmxcu3aL-U1_V14vVeJKH1DUsu1pCJmaI_CGhshpc4MRc3OROEAk0yqs4VH8upBjp46azwwxOnIO9JPyVMEjzkVvEPNDzyvqeP7L7XV4G3EmDyL8D0Y2vaZ8gQnsEUlt-CdLg_Pxyu6OnQJqdX51IkwfOezOGDXnF37WsaIrjZMeBve_Lv1meOngXpCKDYvjxQRI8eyq9Znhue7u5qm48-6XT_iIZmrruKBafhCXO0ebBV0XrVmAT6JAPiVrrS-PhWnpitxH1HWeseyKhKGxZ2d2qpuVSDyyChaN9ILBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تفاوت تصاویر رادیوگرافی و ام آر آی و سی تی اسکن به روایت تصویرهایشان
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/655117" target="_blank">📅 23:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655116">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0ben2Wez0v3ylN-sGuLqtQLv2V380rxvvFOGB1kF2cnPK_wh4LarAm_ilZNkAgCWwo4W7fas-Sk3qBfuR_fAOHM1vB9EnGwLwh_eFpEYRtrUP5CAphh1hPWTk346TjaOzsfLU-cmuax1rrV42oO2pfe6xiCShtyuH9a4KLYnwBKyAFL6OWMBQnw4enmR8H_dOqK4HOm6mXWePbMXwO8Ez31sP-SyBWSgkP54sRC0gGray7rKU9TzIz2mTV5uQuFMeQaV1yS34Posc0wlcVbizSC7a9dLke27ETEWsyoOB52XiWQOulosZC3pT2ObxkXPK4MtoMS_iks0y7jzIO4eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با مردم حرف بزنید
🔹
اظهارات امروز مسعود پزشکیان درباره غیر عادی بودن شرایط کشور، تداوم فشارهای خارجی و ضرورت آگاهی جامعه از هزینه ها و الزامات مقاومت حاوی این پیام روشن است که کشور در مقطعی حساس و پیچیده قرار دارد. رئیس جمهور تأکید کرده است که عبور از این شرایط نیازمند همدلی هماهنگی و مشارکت همه بخش های جامعه است؛ اما تحقق این مشارکت بدون گفت وگوی صریح و شفاف با افکار عمومی ممکن نخواهد بود. مردمی که قرار است بار بخشی از این دشواری ها را بر دوش بکشند، حق دارند از واقعیت ها چالش ها و چشم انداز پیش رو آگاه شوند. اکنون زمان آن رسیده است که پزشکیان مستقیماً با مردم سخن بگوید
🔹
هفتصدوشصت‌وسومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/655116" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655115">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paWVB6om1rfMBRyWCBQAVPDKZs_4E06Ln2RGL9-5mk8Bvmil1aTOJVjg-mdpnua_twDDAJeOK7q9fV6ig2zz9tsRTx7kBUm1WfC-ZcjoPeduNJzF0YQafjm7EblSdTzzniSs4IUyAverdRqIYzmSV3Qf3tAdTaBzLmHrs6i5-0ZXIuLyrzLHsasGQc_5SUZfOFK_ljGPzzS6rOt3YZ52RGmKwItJMBDlRK2QdwEnWTOJWiNZrhnn8lpVQxMJFhiUafmyRaGOq4aLY4W65KgRzJZyuRCbOIknHQ8kqh2vW6vs19RLkh7cOnotAwhEOxY_lokOO14sWx_T4J7m0oIQQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر معنادار در یکی از تجمعات شبانه
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/655115" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655114">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
امحای کنترل‌شده مهمات باقیمانده از جنگ در کنارک؛ صدای انفجار فردا شنیده می‌شود
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/655114" target="_blank">📅 22:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655113">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0PsJ9_8LGhzvqHHCHHaW2Ik2UWTVaaZza5l6OAqMJaxtIw_C52j6zJKG402gvGAkLSwayw2wNTqEMvnplXgbkh0wfjxkToc7v9EMNYMER404ueaaWiVoHtqX6ZufT1vyJhPDdUHaRurlYydwtGicGgP0AqJKBV5NDV6ys3uBnceIID4OQCklsZ0iwvghY-pc95y4PcalrEGuiwLNSmJP3mIGzuri4iVhQH8Lh_yIN8bahXyKABpRZZaVBwpM1xrt1x3dYcdSrDFp_6Qbij38LctfGkum-ojFNsQu_Bme7PXYXZq-_WgRMIorjalHYGt-MSEM6Ny43ZraKNeiBa3mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
عید سعید غدیر مبارک
به عشق امیرالمؤمنین علی (ع)، هدیه‌ای ارزشمند برای عزیزانتان انتخاب کنید.
🤍
بارگاه امیرالمؤمنین (ع)، یادگاری ماندگار از عشق و ارادت به مولای متقیان؛ هدیه‌ای شایسته برای عید ولایت.
جهت ثبت سفارش با یوز زیر در ارتباط باشید
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
📍
ویژه عید غدیر
@ghararshop
@ghararshop</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/655113" target="_blank">📅 22:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655110">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rDHHAyyBLNd3fPNyMagCPpaJatd3UsaI2mfPsptEalyucewxbzV8HNiQCDaYPjVzwX5dHgwAqZr_dNwql94Lq2RxTlUtHG6TdyfF0fUCBUelXljnIQQtg9RPiKI8zj-RtBgAbPD0_j6EGBJLAd8W2gevO6c2Q7NWMlTbNuP7xKLeQwrOFxfOxC-8EeJPVMb-1IaLPECa1AYaZNhlOt7khvoMjMriopzR85FHT3eYbYfAbrf9dZD-1sbK1ZslG9l8UYQQ7fIMzUbam25SnLklqr7XEWgeXB8Y83lyph02dcL0kpgPQD3TNuitd2l8Tizt35TvWvjCwSMSS0gtFc7l3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OrYYl2ZF61lYGamLr5nHsK8zePpzNl6tMfFYTLx8so-IJ6hNMeKFY8zyG4wiFjQYjiGqNMNbW-8mArO8sGK5wByNSB28cnMAzIxoKn3Ya66VM4z-GgWTKx04TG8qWA3M6Z2UT0Aj2TeZaOB3mCnD-o_qeu5dtQ779r5alo8un2qRsFO_v-bTCAH_OAh2knF2u5Gi7XPderX7qjKwZdKpuuP1X_1kze_UpULoSD1iUFkUOuLkV78Gn6e3nW_yba9OhsiHkY3QlG8ij6jKnEhg3sildMSXrF5A4uq9SEUqKA4Zhl67xWJLEAUno3F2ngenPyrVCHY-gl-zXWN6tz8mEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ioBr9-vodL8ad7WruMQuJVuaYQY_Ak8mLaESlLMn8xZxpH7xbGBsJhL5Tr5aMT7hgQA6jR2y_Sp8TGykrxfZwxXBtEqF5YOas00zISCG46U8gWvGZmMa0x4yp8yShM1zVOpeXI9l3tKYcVbFhXvbqDq4MsxTMWYtahBS0Uz0zokCbf_PgoFE7AzvgfLXHIqjbGZDh841xuI76MeCJBNL4iYZmt188zl0qyi96YgjFNjDxly7t8iJCz0-FfaHSBqDvJPt_uPlUuZbbP27EAFKcaYHB5n_D-X1GzU4g9uy6baspTGhAZK8HgIADYiDY3BwwVRGjHE8vLxQUszfDWB_Ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر هوایی خیره کننده از ساحل معروف برزیل
🔹
منطقه پرایا دا بالیا در شهرداری سائو سباستیائو برزیل، با نوار ساحلی ۵/۲ کیلومتری، به دلیل میزبانی از بخش وسیعی از جنگل‌های آتلانتیک، اهمیت اکولوژیک بالایی دارد. این منطقه الگویی از تعامل میان توسعه شهری و طبیعت بکر را در نوار ساحلی سائوپائولو به نمایش می‌گذارد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/655110" target="_blank">📅 22:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655109">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
تاج: با صحبت‌هایی که با مسئولان فیفا انجام دادیم، صدور ویزای آمریکا برای ملی پوشان ایران مشکلی ندارد
🔹
فدراسیون فوتبال دارد تلاش می‌کند که سپاهان از آسیا کنار نرود، اگر سپاهان نتواند پنجره‌اش را باز کند طبق روال جدول لیگ نماینده ایران به آسیا معرفی می شود.
🔹
بازیکنان تیم ملی به دنبال این نیستند که در جام جهانی صعود کنند و حواله پاداش بگیرند بلکه با صعودشان به دنبال شادی مردم هستند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/655109" target="_blank">📅 22:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655108">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c108240e5.mp4?token=WDfD5bNNIx7jJZE-6sQSbyObkRyqaltjULf2BWFhl0fSUN-RxGQiu8kSAHKBM9ijueMEpYGQ8Nm8o98YxXFNaKMn0Fjg6prqeKt-Ho5UuvNQ09VrdRhuAmYRKTR0jFtaG3e-g1PhW0t4s7cx2GBoNelBicy0sonIBIQS2jxzDBa1maqWMFeMH4ylqYil08EeaIlGR69oWzhvlG8NwDv4ckcKa5vn_YU3CV-3c9bFFLlqO_KyVrFgY05hHiBWRs1jY2zD15ZzmfSjoPcx4NyB0Em8NQDxnYAmjs3BBFyu4YHI6bRntC7f8xwth-8yHMfU6wt2X6ENmW5jmPAwlKiEUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c108240e5.mp4?token=WDfD5bNNIx7jJZE-6sQSbyObkRyqaltjULf2BWFhl0fSUN-RxGQiu8kSAHKBM9ijueMEpYGQ8Nm8o98YxXFNaKMn0Fjg6prqeKt-Ho5UuvNQ09VrdRhuAmYRKTR0jFtaG3e-g1PhW0t4s7cx2GBoNelBicy0sonIBIQS2jxzDBa1maqWMFeMH4ylqYil08EeaIlGR69oWzhvlG8NwDv4ckcKa5vn_YU3CV-3c9bFFLlqO_KyVrFgY05hHiBWRs1jY2zD15ZzmfSjoPcx4NyB0Em8NQDxnYAmjs3BBFyu4YHI6bRntC7f8xwth-8yHMfU6wt2X6ENmW5jmPAwlKiEUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسرائیل پیوندی با انسانیت ندارد
مورخ یهودی آلمانی:
🔹
سیاست اسرائیل به‌طور کامل پیوند خود را با اصول اخلاقی و انسانی از دست داده. هیچ انسان شریفی نمی‌تواند چنین وضعیتی را تحمل کند. آن‌ها دچار جنون و شیفتگی مفرط به ایده «اسرائیل بزرگ» شده‌اند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/655108" target="_blank">📅 22:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655107">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4XkK2NwiA8HQNeDUozHMYG3BAamW0L4GjWAtnsy5Rxlv1fUxO96IUA66XEMERZKM8IflRy58e7LjiyeH6rR4t6Tu4ktEV-q_QbOL4yuLfLvGvpFp4KQ5zb-XGgXlcz7mIYfiIA8ixgRMOBKDeASm5tS0keRbXNI48f_r9EPfzlX3Jo_bah7mFAi1FJRmTAJUFNB-YyQ7CsGVu43T_614pLMIQFmz1lQEXWvoqAfQVKphFUmoNNaDTDqD9rjv5nXkQfauTlY-vWM5AB9rHnk7LSBWoqT5GA2oJge9XyBSZuidCdeShSseQ1Jq4TOuHmkDAQ8XeNl_rqvTwqzum9SEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خطرناک‌ترین سلاح آمریکا را بشناسید
🔹
بخشی از عملیات و پروژه مهم ارتش آمریکا که در سال های اخیر روی آن سرمایه گذاری فراوانی کرده، عملیاتی است که می توان آن «عملیات تلقین (کاشت)» یا «Inception Operation» نامید.
در خبرفوری بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3219318</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/655107" target="_blank">📅 22:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655106">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ماجرای کشتی خارجی منهدم شده در نزدیکی آب‌های سیریک چیست؟
🔹
در پی درگیری‌های روزهای اخیر و هدف قرار گرفتن یک کشتی خارجی حامل محموله مس در نزدیکی آب‌های بندر سیریک و کوه مبارک، گزارش‌های محلی از تجمع شماری از صیادان و قایق‌داران در اطراف این شناور خبر می‌دهد.
🔹
همزمان، بررسی ها نشان می‌دهد با توجه به ادامه تحرکات نظامی و شرایط ناپایدار منطقه، احتمال هدف قرار گرفتن مجدد یا انهدام کامل این کشتی وجود دارد.
🔹
بر همین اساس، از شهروندان، صیادان و دارندگان شناورها درخواست می‌شود از نزدیک شدن به کشتی و هرگونه اقدام برای انتقال یا برداشت اموال آن خودداری کنند.
🔹
همچنین به مالکان شناورها توصیه می‌شود از در اختیار قرار دادن شناورهای خود به افراد سودجو پرهیز کنند. مسئولان تأکید کرده‌اند در صورت بروز هرگونه حادثه ناشی از بی‌توجهی به این هشدارها، مسئولیت آن بر عهده افراد متخلف خواهد بود./ مهر
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/655106" target="_blank">📅 22:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655105">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
بهترین‌های ورزش سال گذشته کشور معرفی شدند
🔹
فدراسیون کشتی - بهترین فدراسیون ورزشی
🔹
تیم ملی فوتسال - بهترین تیم سال
🔹
پژمان درستکار سرمربی تیم ملی کشتی آزاد ایران - سرمربی سال ورزش
🔹
مهدی طارمی - زننده گل سال
🔹
مبینا نعمت‌زاده - قهرمان فردا ایران
🔹
هاجر صفرزاده - بانوی پارالمپیک ایران
🔹
علی‌اکبر غریب‌شاهی - آقای پارالمپیک ایران
🔹
زهرا کیانی - بانوی ورزش ایران
🔹
امیرحسین زارع - آقای ورزش ایران
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/655105" target="_blank">📅 22:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655104">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb367f0e92.mp4?token=MmwZ4D3_9npQZxbq_OVrBwdZ_VX0og6-0G5dNkYXciC2RnpOa-mYnC8CKYHxRpxg6PV8WCsor15lVBVnYOdcT4ssg8eMyDmal-6NyOFvWSnxBQK41SShWWAulSWYXnwKt3C8vEkgasnKQ57YTy_L0M0vQyobIv-RSeMcLmzHyPZleGxV4lK_IhCJWJOCjOwQb69EMB1TtIlrqzlRkPdUJy9Of1O59H9GrAJA2EZPsF7R9ah4WQ12sqlOY3IrDKddzWHSTNYxF5WTh5BRnfMUtf_2lz_eXKAOP2WlwdADr8V2V4vWqBMBwRzdeek9O53D9WQ6o5Q9vfD7hq3MPng4aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb367f0e92.mp4?token=MmwZ4D3_9npQZxbq_OVrBwdZ_VX0og6-0G5dNkYXciC2RnpOa-mYnC8CKYHxRpxg6PV8WCsor15lVBVnYOdcT4ssg8eMyDmal-6NyOFvWSnxBQK41SShWWAulSWYXnwKt3C8vEkgasnKQ57YTy_L0M0vQyobIv-RSeMcLmzHyPZleGxV4lK_IhCJWJOCjOwQb69EMB1TtIlrqzlRkPdUJy9Of1O59H9GrAJA2EZPsF7R9ah4WQ12sqlOY3IrDKddzWHSTNYxF5WTh5BRnfMUtf_2lz_eXKAOP2WlwdADr8V2V4vWqBMBwRzdeek9O53D9WQ6o5Q9vfD7hq3MPng4aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طبیعت بهاری کهمره سرخی
🌳
#ایران_زیبا
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/655104" target="_blank">📅 22:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655103">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
کمک فوری/حال این 2 کودک بیمار، خوب نیست
🔹
کودکی ست بیمار و معلول،از ناحیه دست فلج است یکبار جراحی شده و نیاز مجدد به جراحی دارد کودک دیگر نیز دیابت دارد و هر ماه باید دارو و انسولین استفاده کند وضعیت مالی خوبی ندارند و به کمک احتیاج دارد.
🔹
مورد سوم دو مادر هستند یکی از آنها به دلیل سرطان پوست تحت درمان دارویی قرار دارد .مادر دیگر نیز برای جراحی پری آنال به 10 میلیون تومان برای جراحی نیاز دارد
🔹
مورد آخرنیز پدری ست بیمار ،مدتی پیش با قرض جراحی دیسک کمر انجام داده است
❇️
توجه... خیرین عزیز پرداخت انلاین خیریه بامشکل مواجه شده است.. لطفا هدایا وکمک های خود راازطریق کارت به کارت یاشباخیریه واریز کنید
✔
پرداخت انلاین خیریه نسیم وصال:
http://www.nasimevesal.ir/payment-new
شماره کارت بانک ملت : ۶۱۰۴۳۳۷۸۱۱۴۱۶۲۳۷
شماره حساب بانک ملت: ۵۸۹۸۷۷۱۴۶۵
شماره کارت بانک ملی: 6037997599156198
شماره حساب بانک ملی: 0219934010000
شماره شبا: IR310120020000005898771465</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/655103" target="_blank">📅 22:09 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
