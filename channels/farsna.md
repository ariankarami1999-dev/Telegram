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
<img src="https://cdn4.telesco.pe/file/odtcdlrOfbkelo_Vj87Q4oy_rman3GbbIdsQfEU1oSJPRjPR4lZDCqJE-nT00AyG5R1m27JjYntj7KD4hzUFxOHYUY-e4ndGfWS1smBdevnyEth941pom78-X17nLHCC_QILDblKxkQ1fD-ivgwVH3hS6h17F01-tBrZfGlo0TPQGmHOf3SBTPUmmalzoT9NGUyrxRy0rrmpLxy0GuAj3YTzbAElF9hpRLZyhfLUcojdqoHCS29ABCxg_i8yL_IE-mivZoqgXE4QW3shrVX0qbSgMq21uTtgKIrBY3jKGh_gJcWxgrZe_As4VcuI_5OCJYHkS-0_K2LcF3qjGkuDng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 03:31:43</div>
<hr>

<div class="tg-post" id="msg-443335">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXwbWrkfbv2ikGtKxE0arVoPafPD4A9vDkYjabnIvfqi68RVvckvbQ5xYpLq1oA7fm_-6c1ReRjwq7klUkkWIxL3IbfNUVIljvdj1VLDjWbzl8ICvIbXh2kOfJQpYVpKhEOs2Zoi4sXsbJurIWTSFGtYsKnp5twvObu4xylYc2exZitcJ7qaDgb4Dcc9-ICD4lkSFG8Ud9KBopkWMDu2rYuVRfJpou-vynOG4SA-DxDFZ0TRuqP_3xNiGhAzdGRTEAUA7VM6K7OObYPKcroDQZb71wMoA93WOVRcQ1g4Zn-Ileg38Fyil1Y8172qe7PsOrC83u4GdUOzavX47Whv2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدافع پرسپولیس در لیست خروج
🔹
حسین ابرقویی که فصل گذشته از خیبر خرم‌آباد به پرسپولیس پیوست، در نخستین سال حضورش در جمع سرخ‌پوشان نتوانست عملکردی در حد انتظار کادر فنی ارائه دهد.
🔹
بر همین اساس، به‌احتمال زیاد این مدافع فصل آینده جایی در ترکیب پرسپولیس نخواهد داشت و باید فوتبالش را در تیم دیگری دنبال کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/farsna/443335" target="_blank">📅 03:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443334">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5599fb0ca.mp4?token=X_HCeKTZ1LJnUWOvIza9iwl_wZcSl5pxo5-ebZejX8z6LZw_Q1Nx8l8IDQs2HP6NdZI106iLyX0Nmu0lReqVw96Gnnqf-H0zhQcLLmHeBw6v4Auosn4qidj6wiqaFQc4cCkIdmGqcilDEOryEHXSvHpn9Y7t_vfRfr7QwbpFteXdUefGus7Q0kaegcZg0gNZC-ALP7OEjWGPzCBy2TjayLxdoBL7OIVTwL3t10aafXrq1S6mlbOgtmQrf45kfdJ0nFRsSaur1QVwAnf925ExHaIDhpB8sHLFj-gtTRUt1TJZnpMpSEhG3kHeTYT4MMuBKhLGz74R0HtKZm8rZxRiDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5599fb0ca.mp4?token=X_HCeKTZ1LJnUWOvIza9iwl_wZcSl5pxo5-ebZejX8z6LZw_Q1Nx8l8IDQs2HP6NdZI106iLyX0Nmu0lReqVw96Gnnqf-H0zhQcLLmHeBw6v4Auosn4qidj6wiqaFQc4cCkIdmGqcilDEOryEHXSvHpn9Y7t_vfRfr7QwbpFteXdUefGus7Q0kaegcZg0gNZC-ALP7OEjWGPzCBy2TjayLxdoBL7OIVTwL3t10aafXrq1S6mlbOgtmQrf45kfdJ0nFRsSaur1QVwAnf925ExHaIDhpB8sHLFj-gtTRUt1TJZnpMpSEhG3kHeTYT4MMuBKhLGz74R0HtKZm8rZxRiDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله مجتهدی: به‌دنبال روضه بگردید
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/farsna/443334" target="_blank">📅 02:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443333">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
رژیم صهیونیستی شهرک «کفررمان» در جنوب لبنان را هدف حملۀ توپخانه‌ای قرار داد. @Farsna</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/farsna/443333" target="_blank">📅 02:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443332">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
رژیم صهیونیستی شهرک «کفررمان» در جنوب لبنان را هدف حملۀ توپخانه‌ای قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/farsna/443332" target="_blank">📅 02:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443331">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7rI5jpJEoLc_1OvB7SdP_InoEBFkDSgFaGARFN4SqLdWKKkbAQafqpuYlVKiqJOhc50-U5U5KZoTiSIgX4_28K3s82IsYx5jGtF_znZxOrt9mqhzl9IZrfgM1pCDwOXXqZvbL9pnYpHoXEnSF97j0RQWXl_M7_aN2Jt5U-_imxVeRw-ub_nEhqdrfSc79vJ71vYBIhOzE_v5bS0BUygKxxG6sF460bcU20MxkjbkaDpu9qiUsR_QpCQgg9x194h2ZsAdLRKHkVofVy-e6baW1JOKGAXp5d6zITm0DGXEU2wLKsoAEWxT3BeJUyIWHZpz83wy-XsTjeseh878V46Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقاومت مسلحانۀ ماینردار بزرگ دربرابر پلیس
🔹
سفیدمو، مجری نظارت بر استخراج رمزدارایی توانیر: در جریان شناسایی و جمع‌آوری یک مزرعۀ ماینر در یکی از شهرک‌های صنعتی کشور، عوامل حاضر اقدام به درگیری فیزیکی و تیراندازی به سمت مأموران کردند.
🔹
در این عملیات، نزدیک به ۶۰۰ دستگاه ماینر غیرمجاز کشف و توقیف شد؛ اما پس از بررسی بار مصرفی شهرک صنعتی مشخص شد این کشفیات تنها نیمی از واقعیت موجود بوده و بخش قابل توجهی از دستگاه‌ها پیش از شناسایی خاموش، و همچنان از دسترس بازرسی‌ها دور مانده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/443331" target="_blank">📅 02:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443330">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab12f1bdf.mp4?token=bSDmhZWVli-2yyKv3h9c7ROCiPJDk5iCaPVyU9sVqp5gIKDOp08VngsIziXcvg9yXtvlQ8DdJm4Mh2wbJfjuRhW6GMeva9eFd92WdhsPrkmrPL-2f36DiFO0Pm9yiJEYvUp33Ex4z11ftOJfSXnv6bjhhFgrLZ8P3-v2EhkBrrEWWh6cqDSTpEI0ylxMJv9XHb-fOsn06QwYgixr-b9lza-pIfjKe9fbMz5vwpFQlhFaL5xLa0njSQP0aXJKcJZzYni6dPScOKLeaCO5ocs0T52qg_OyngfIM2kdUsi8sIbsrc84ryBmgBFZ2r8mfN8j9oakxdTe_YBQ4IrYaAbYSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab12f1bdf.mp4?token=bSDmhZWVli-2yyKv3h9c7ROCiPJDk5iCaPVyU9sVqp5gIKDOp08VngsIziXcvg9yXtvlQ8DdJm4Mh2wbJfjuRhW6GMeva9eFd92WdhsPrkmrPL-2f36DiFO0Pm9yiJEYvUp33Ex4z11ftOJfSXnv6bjhhFgrLZ8P3-v2EhkBrrEWWh6cqDSTpEI0ylxMJv9XHb-fOsn06QwYgixr-b9lza-pIfjKe9fbMz5vwpFQlhFaL5xLa0njSQP0aXJKcJZzYni6dPScOKLeaCO5ocs0T52qg_OyngfIM2kdUsi8sIbsrc84ryBmgBFZ2r8mfN8j9oakxdTe_YBQ4IrYaAbYSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شروع طوفانی مراکش؛ گل اول در دقیقۀ ۲
⚽️
مراکش ۱ - ۰ اسکاتلند
@Farsna</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/443330" target="_blank">📅 01:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443329">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca518b96fd.mp4?token=CE6MPA0BGhhsmc1sazSd_Ayxc9LAo-G4gh0oH3I8oxk26bff-xZLeXtPP3n7-3vBOQPkbVRPshRqOLu8EVTtkGQLw42W3eHQVeXqltxXUIUs_exZ_DyyLAmqMx9a8mJZMmPZIBr5zCEGFO9X6bgM9U9GGzdUeIvC1MkHeXqFx4iM5DKbxURFpeqb4UceGZ8kIQI7lfWrvfgfg2hdHGmSrlLZw5DfKKAoJLwDbz3FK9lEn68N334eiekD718NIuL_wEQLp_lYM6jgi3NCwZTmSkNNyYXJIEI86zlWxKoNq5jRJMPG6kqq1gYxXnpG6z-lAWV27fIn_swvxvCe1-tO_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca518b96fd.mp4?token=CE6MPA0BGhhsmc1sazSd_Ayxc9LAo-G4gh0oH3I8oxk26bff-xZLeXtPP3n7-3vBOQPkbVRPshRqOLu8EVTtkGQLw42W3eHQVeXqltxXUIUs_exZ_DyyLAmqMx9a8mJZMmPZIBr5zCEGFO9X6bgM9U9GGzdUeIvC1MkHeXqFx4iM5DKbxURFpeqb4UceGZ8kIQI7lfWrvfgfg2hdHGmSrlLZw5DfKKAoJLwDbz3FK9lEn68N334eiekD718NIuL_wEQLp_lYM6jgi3NCwZTmSkNNyYXJIEI86zlWxKoNq5jRJMPG6kqq1gYxXnpG6z-lAWV27fIn_swvxvCe1-tO_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«علی‌الاصول» مسیر حسین و شمر جداست
که شمر بندۀ شیطان، حسین عبد خداست
🔸
مداحی مهدی رسولی در شب پنجم محرم
@Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/443329" target="_blank">📅 01:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443328">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPWr2WQgQh0J4_aCbkuRASSsfRG3Lg_czhElI47U2KySYppMefrobbWwk3Cf7O7xFomwiEHzcUV4aAXvE_zwkFn5_lJR5KSNDCMu4OZ8iJQUOwoyV6dIDVolp6CacM91z9DaiwD69MkW_BbeePSIaRVB8gLxyJPrndn3wJaYUC8qjD2B-dQD1d9JthO0uCmTSK3DMd9OeDcIPLqef1XqlEUCBso8LEsjQACQJqNZTKshrSNUSOBOoXVyH5B6uVkrYCL6e32stEMXEAuObrY1q8tkbhWMYmFZ1MeIfzGL-f7HzG4b60ALLTpLJEnW_FrY-H4Comd9IZ5k-yXYFgegXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدشانسی مهاجم استقلال برای بازی برزیل
🔹
داکنز نازون، مهاجم استقلال برترین گلزن ملی هائیتی، همچنان در شرایط نامشخصی برای حضور در دیدار کشورش برابر برزیل دارد و احتمال غیبت او در این مسابقه بسیار بالاست.
🔹
نازون از زمان دیدار مقابل اسکاتلند در هیچ‌یک از چهار جلسۀ تمرینی گروهی هائیتی شرکت نکرده و وضعیت او تغییری نسبت به روزهای گذشته نداشته است. بنابراین کادر فنی این تیم امید چندانی به حضور او در مصاف با برزیل در جام‌جهانی ندارد.
🔹
غیبت احتمالی نازون می‌تواند ضربۀ بزرگی به هائیتی وارد کند؛ بازیکنی که نه‌تنها مهاجم اصلی تیم به‌شمار می‌رود، بلکه یکی از مهره‌های تأثیرگذار و رهبران این تیم نیز محسوب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/443328" target="_blank">📅 01:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443322">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rqwYXG_wliGvgQcyrYrY7NsacHYppb528hNOWwnmhzSeMsZAcpKn4R-5l7oZRkop2ECUjIdVK9C5B9UChm9TGc1rqeS7PH-hGBvGK_rDm4d6bkipzaIk59FX9nu7TOzgepY2x3V3HsDrNkbH_t9mvGJi6HAa63tLvoPYKLdDsiJZnBgu2s55SJj7z4j13YF5Ar9YTMvKfhILUuenIKHeIqamNfLCcvjJb4_VlAy2nzr1xGUEE5iR79BRTl9eeAGoRGp203tldpFVAKrO36vV8mHvjgoEqIzxkeKQ1X22zAE9lzg-fD6HUufb0AHWG3rAltshMNsO-5WH025thk8odQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U8w_DZnpd3MiJWnVRPJiF4ifRfk7Qdzi-Vwkq4V8wfBkQdCFdAFu-WFVG2czIZmcx-f0t4zpL9nUAREpVvt-iKP48C597JSMIoF0eU1ouqb0ATdF-IXtkLzIIuAS5YzH16UqqOm2wAYB6WHnYzHq_bJu7eO0xtgll-umwWJE45sdxTxDHjI-p2grYVScedn5TW8vrHBTDUVsj4Ks3dbkzEoMmRdzIP5hsIST1p8aFeXfOfh3mRKMtXDWrk2tkkUaR6xDdmmszj4mnzmyNmUt2DpmZ7qc68r1PRJ49Q5g4c4RnFZLVHCjLHtefbeOKOF4BKNCKngi63tzPw6w0i9FxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BlUQzk7jh9_nL_g4Q0LaLVtmUzCGyKA4htIz9ZXhlwKDVpnXadpMkM5pGwhhXXhSxurgWw_aUlxrhOE7jzxCFBRyEKgBHj6sSEH-0MLJt56QGW-4f7dvugSEb-6djrd71wdzW3wOXFqztHbbUaVpwHufOEf5_iMXNtPYWsxkFiEVD8onuwIoKjijNPPPh3wPkktXgSJz5mT4Ylq0e27iBiL-uAx4GU_Igvgw_bo47oE47jGl6hKO--D06kQew4grw2AJLcDfmEtcwyD9Z_c7NssOAXCIIDdc-OfPx18g5I3bixxt9HEqf_uY4YHUcZAki-3YwcH9tGsqOKa_CRJthg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7246T4eHpkrkQJEKs9tr_QwBRp5vdfgj_HRiMw-wfi-8CwOKUy7TnmvG_jXq37rG_0vUeBl_HsRE_X_ZHfxPSQeYowIOh-teRoP-xOy13-txKGtf_HeeUAsxnqHCLKSFEIbw2QBp_33mgyYYkNDHEWaFa4q6ZlKD6FBf82Kioy8woS29BV8_oG04HkBeM_BhFKAM931pu9Bg20C3RyCSJisIqciLxQSb-a9x7m0jlQV_WpKkmmIGzvlADxbsq_8UFDRyf0JQ9dIRMiqcYDLrKKOPJ81EVUas0LcmpYJQHFgGN2XtkoQrNOAb52y4MgdVyeMrxKKXVulGvi5XWRv2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zbloe16hbGC0Ag_GRCXXDX40fcdPlMxlF2p4_LAZ3mp5ufSk0s9nKTG17Zx6GR8ai2SS56pltlKlVwm95p5IhWSuZY64SJN_nvEiYQ8txj7Q8_zJksqx-GMeHvZtwLBJwZuVu0Awc9GFjeYkUaNBdFIjTSm_6qaqZqN4fw1YMW1tRzNXaLgrXaGCx3GOIzg3-dKKn4Twq_DySD8KTGamKX5jrLcFrQmCBMjXbs8QcIzKVjX8L0oIWZIFsbT4d-mcF8ct80E-NNlpVFeGwBIjw52H3UQ1_LuKGA-m30eI0ptcB7AEQUN3hm8mTvOJ_volcgtrFazmJGwir6_p-3Brbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmQ4LvXLrMYxNHpJ-JlXYzZD4z-5cTosIwaLuEJIa9Yi-ue1nj0w-FuMng3qZc5fSM5Vg77uvD4HicB01XociN7TIJrhRaRxf69T1l3IlA3vz8RoeIHI9h81QtE0Q16-OOZxs2DhF7IJDv_je4cPTZfpzea2vgbXfLVvF5uKtS6nkrgzfqWa6imJApqFcfaVhLEQaDC0opdDg-hCVjP3JCgcSLc6kLxfNqiArJZomcv7_tPW7PUJvrNn7Lw1Ly_ftVHFjE5RO96ZB3Xw-Tw-xCjAi1FvHcP_QsEUaOU5S24DKnf-mt0qMQhtLvHyDj6hP71kwJV5UwyNVH3-zQH3ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۳۰ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farsna/443322" target="_blank">📅 01:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443312">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OwgB6ZfyBhg7W58xlYQdCiwGt_pT5nsiuVz6-4Ibe97ABFXtzjuc8HVYiLeubxPuPUygTsVrkzP4fTOIufhZkkfBFjN_Z5nfln9piL-1ugn9uUcFs8yadbL3Dl-G4hl4OXWuuVjQ4_9Gq18WcVkqPsr9GPcxtgA41OphHAMPkI_Tk_sLiie9rjQHfrbYMcRxOOIuAY6VQVJPpRVYdBzbpBUKbEf07BkOL8NzU5BKnZ6XyqvxplVbyBupEVStPfaQ9__1xcJsmYAqnIHX7_5dCqRpMRa2CyWZJTkcADC8w8i-DLiHAQvHI4gyoF723qZLb9eNWwU4LKiGTI4m84j0sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qIXJvMWX_U4I1AHpANipyJ4nG9HhFzrK35OxAcq5cL6pyC3vXskgsOwcDOAF28ry3ouSglWH8W1l4JSWWPZSfgJ2EQQqxZzfX3ewlhpB7cg_lbeS51FT4MDwsQ3fM7u7GTIuWa3tslhijrnhHnS-FQBA8uSv_-qLKnJ3PdTrT6nBHK0ZDZEINj6U4MTywvANtyBuTHnve9Pi4jX9OQIu7GV2xyFvYV9Brcjez15bQPUyvuQ3hgJxNGsN7N3TrqkcLjR6yXd-pqDGG7LgClsUMaet71VOQ0J-6rp0_KbTqU0m3ifABUTL6z-g7HdCMx0S72l8FxDe7KVPk6-n0Yu2RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ra6QSjXU5T5h9bjzj7qwrqzSAGlkSmSZFD2gmZbUUBfzO3V6vmFgchDVIIDtFGWKwFKo-fQlQ6ZbWMe7i3GqrrBnEqaXmDhN4C4v4yudct54yG4PgSsLhIoSB2y37ReasUdVd0inULQMdojiKZkAaTC2xjNKCBjsxSNteQuuQ3_6vzxGjPkn7xwP83cGHIkbcf7FTPqiDkeYkoiX32oZoS3eIiph9pH14oW7huuf9MYmhMMJh4OpNe-QcqKIyNIqw2fpf6iTGe5AyRvxKJQP72gBRcfse5piNPBLy4Q6Uy-KnreEMmoi8wokG4ROpMulYZ58LfS6kX3agvarQErEQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WotG6vA_R5wDzSH2eqSh7tEyPesNT1rhtCfXXB1P5pZxJVAznrPw5wKvWYOr8liHCAxtypvPLaY03WQxUzn6KccE22UQ6kbitBp545vnXaxE6-rMvqCIfjaohR-4bfLFa57bhRWYfznj3K_SfzmPuAfLtUS8oE5YsyHr1r81Eu-iX16CvTwNHu-AC3iwvxSpnfNhOT22Y_zezsW4v3u9Ea1kuqhO_1vMbYFrKdZM_NEoX1tmLk0RBV4HDNrwG7rctOZ85RFpXw8uaIyban18bMUSHCf9BdD9Zl1AnJkdtgaRVShm2t_gm0w0UZBDITvcY6NrG0b6YRZNTSB-TvqXng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cjiTDimk2oSF19hzb16kbDhFxcurm_1mzpficQRNlCPqYTdJXtp_dsz0rj-leYLAPpe8pTWn_JG1FjTHi1jq9GymzcvM6Bff1nKzaIySQ_aXKBmVPdUr_TQpDgmTgXP-XrvZ7d8lZ4GSUxGa7gf4G1uD2vvjwsgFhWpk_J2gR1EKAVsVHV6H7cRgyZFpWIHKm6oLiZ459bRmvPXp2mLtudfsH1IFbsGgVlsvXuBLMLt52e9FDUyJRQTMsOWXob9OiHvSLkjjR575qZ3vxtCmb3oSIiI02mYxUDe9GK0Ejy_k0yfwfVfOyIgwzDUdGmf2_YEiRPXhers2k6Hwzmar1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I6nWKj_7YIU8C-aU9t4idX4nGZHTfbbfoDyrzSMSbDBtjPaM99VvSHBnUw0lDa1L3_JY_YJGwnBtqcWtTtAcGD6Om_f7iOqPzsWQg7s33Ltd69swUANrxKs9bVvyfTPFF1-OrbcNTtsTTSFi1VhBVb3JV73smtauu-ILUx9DLFIRJyG24xybRBbkzxa_kNdn4aLbfh1tvoMUf5Ch0J4fClCYmUfxX9z3xD6EjlecCHX4Jxeeq8YOnNZ7meboQFIIP-yBtdKUfeTOYlGWINpmr07iRU6RXcKUsYwZr7fB-tycS4bY3SIoJX334_0sWkHVIOKiEl8xqWAz1qIBMsiTWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/REDiDoRI-QmmHrYlxTnOQSen0c3yAVpPwc0KQzlaV_PmzXz1TG0DBoKeZ1IO6uoBkWDH8nJ93M5N8IQE2--SQw6K6GCvRJEinIhigi6yp43Wtjjbo4jHn7xsm6gtsvbL6kbcnq1VkFYgXgga6QirX_YM2RifUlNQER06PLIo3iYG4sZkVhj6yNs9TdkckXVOPXAf4yxrN-nyPtNaSVizZmXX6qF54KfvzImMWvRoniOlcSb9V6xP9aZ_6KByy63y8HQvlyN0CgQlx-71HtFRghUslHfh5RFZJd7GfrVr6GhEJs5ApMWaKDF4fHoj39C4v0Tpbe_y6frOPvsGzWTyvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TKcOM9ltkZqfzU0aCigFkUfa1lzZsNJWW3VnoWF-TFNAeTAl9zoDLoMnczSFbV8kkaTfD3hWuAIS109h0tf3Ugi-hbUS_mMw53oB9dSoNaUhBNr9mXiQjffZlezHcJj9hgLBXObneCKBoaLFQi2W1I7Ug1HJ7UMGKBKJKdO0Ok8qwT4Ewqp--KTftge7waWjtT4mFF0Cojbwakb9GGdjyxw11IoPeh4oyJzsVIx28qspKDMZ5uo_hElen9VpiRkM6DGmcGIHazK56E1bTPvadqqq01pwUvCeWAJsLyUwB4rdGPqyjiKkGzDVnbY3kC9D4CJAN9kODcitYC8hIl67Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BDQ3NphGGu6uZfodrKEpWFyCVLCPEE23PT6d7OFTHLsaW49aVKyvLh9StHF-rcUHWxHIMWXfotI68bFU0x5DDhP3aDFmg_FVL20YQKDYUFgjtv53Ls3hvuzB4Z1AjCcpOYKe6QAjE3v1BR3N4UGazXWaQALaNTbaTeY9xdsefMaI3oSaKTYl66wgW1e2F52k3SbmLd8cra46O72DBOYbVQe1ew-hMVT5fZJ1snYo-vUjbFEdH2mCk6njqqINgzxV7gNOE0S5BXPHt-efIWPLPda7PzwW3sGJqpFrWecUOXvWU-zZuyTWwou9VsFr30zZxgQQ_FEje6fGbr-PkOO9Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s82PlS0Cd3w-rr5Gc5nYeCPRGFeyfV3x77RghL6gNZYcn64cLhTmckSij0Glaax-x3VlSgur9iFjrAANiq-N8mrDy61QDtUOyx_JC07gj1kHK3aqk0lqRH2Wu0I3cFsVyHKPUthXujtrP8tANcfP4A9G5QzD7M5AnetbGC0Yf_YPCYFJ-QGZP9zhSA_bmh0F_J3NKSDFLqW86n4757OWOskjpwKjWn2suXmlaOHnmfVOBPAu3sa2iHFgsd6rj0wqTGZPLhgkECcm1ZCqwi-Xmpt3JehgLKew1SeSKQBNr3f6jcXj25knBF2qGJeveqMTOSRpf0CUlrfVLOWG_d-wNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/443312" target="_blank">📅 00:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443311">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdee81c2b3.mp4?token=tEOx-cgAM7N4NAETs4KM_aWKCWFvMdoAgi4WcbhQxh1nhtgWo_-PUVHt-Bjr1Su0Ike1kEso1KQrVyvSM5G6pyzZkfD8Q0ZqmZ9nmA79sjbJO0RhRbiW17HYPCkMT2Y3uHkIanVVvYo8hxHNGjHQrBMJEv71my25I4NWi-uZOhZIABiUXP-ygEdhGD0jRfgV-unFHtMrRkNzNcBZI-wZUDFPqtavEXWzucj2j2BMXU_t-Z7qI5ADxRphcudf_3jhq7-WKKa1fqe3LDEkQfK_DVEsL9GxODLhBIYyIImQ2UyhWPB6WZKyh5ix2a_jo5m3fqkG1SaErXHA7g-07repgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdee81c2b3.mp4?token=tEOx-cgAM7N4NAETs4KM_aWKCWFvMdoAgi4WcbhQxh1nhtgWo_-PUVHt-Bjr1Su0Ike1kEso1KQrVyvSM5G6pyzZkfD8Q0ZqmZ9nmA79sjbJO0RhRbiW17HYPCkMT2Y3uHkIanVVvYo8hxHNGjHQrBMJEv71my25I4NWi-uZOhZIABiUXP-ygEdhGD0jRfgV-unFHtMrRkNzNcBZI-wZUDFPqtavEXWzucj2j2BMXU_t-Z7qI5ADxRphcudf_3jhq7-WKKa1fqe3LDEkQfK_DVEsL9GxODLhBIYyIImQ2UyhWPB6WZKyh5ix2a_jo5m3fqkG1SaErXHA7g-07repgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
توپخانۀ اسرائیل با بمباران شدید جنوب لبنان، آسمان در بحبوحۀ «آتش‌بس» روشن کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/443311" target="_blank">📅 00:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443310">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
رسانه‌های عبری از هلاکت سرهنگ دوم «دور بن سمحون»، فرمانده گردان ۵۲، در حادثه امنیتی که روز گذشته در جنوب لبنان رخ داد، خبر دادند.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/443310" target="_blank">📅 00:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443309">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWvCJ_Ac9i3nJ48EtdbRvsdDHxVx5FMp-4k19xBCxDRchchuZu6jYBLCHFqc6vJimygPoZFSTLhSNj5eKJ6odVhulS5rqs7WDRocPtGMuDGonQuUb9BJg7afWFG67CmgVudqC4_Bdm0D45gGTID_i05RMRupzW1RKYuyr0r9uQwf1RWTcH7QO2O3rcZ9VZtf7RDWJP1BtjPIcoCGjpzoeqW-L_ieJIsFUTB9R01BPW5M_AxHodzCL4WGlvLqj_3Ct3vszydX6bjWMbXV5zu3vJ2779cwbj-RTfVvjkaZHlm1Jz_grVP_S_GtC0csG2MbT21_oAXE8NpD6xZCLCscbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فعلاً گل‌به‌خودی آقای گل است!
🔸
جدول گل‌زنان جام‌جهانی ۲۰۲۶
@Sportfars</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/443309" target="_blank">📅 00:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443308">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۵</div>
</div>
<a href="https://t.me/farsna/443308" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۴ – کتاب آه</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/443308" target="_blank">📅 00:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443307">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmDpUlMInzCtfotMJsexwH6FBrTbwY_1GmVmW1ODHWmhyANMghYO94UDTr3BQwU2O6GyRsWInOMiXdMVJilWxEb36wSHmC5br8gY4gLjc81zMiZDmX7P-q2zEOQBhadNxWjZ8alk7asiwdpY52DuJVpe2D7LtNJi2QwSV4qGCFFCKcZb71FnZ-kkjg_G5dWXz73x8M3RItwQjJnLLN9X4UwRXMvMpJU5-WtxTWp0RFwvZMRx5Xu8A4FwWJ3ry3j1nPmDH9tVTOF5CmkIVerLCVXpCMnjQOlKKJLsFPEuiSn0xOtEunjO8rnwAsT-XtUseazuKHwNvgnJqCKrtgjdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقائی: اظهارات وزیر خارجۀ فرانسه دربارۀ مردم ایران، اوج نفاق و ریاکاری است
🔹
سخنگوی وزارت خارجه در واکنش به اظهارات وزیر خارجۀ فرانسه نوشت: آقای وزیر، ظاهرا ریاکاری و نفاق تا به امروز از ویژگی‌های بارز فرهنگ سیاسی فرانسه باقی‌مانده است.
🔹
همان رذیلتی که مولیر در نمایشنامۀ «تارتوف یا ریاکار» در سال ۱۶۶۴ به‌درستی درباره‌اش گفت: «ریاکاری به مد روز تبدیل شده است.»
🔹
شما در زمانی که شهرهای ایران با قساوت بمباران می‌شدند و ایرانیان بی‌گناه در میناب، تهران، لامرد، اصفهان و جاهای دیگر به طرز وحشیانه‌ای قتل عام می‌شدند، سکوت کردید و در واقع با متجاوزان همدستی نمودید؛ و امروز در راستای مصالح سیاسی رژیمتان، به ناگاه وجدانتان به‌صورت گزینشی بیدار شده و شما با وقاحت در مورد حقوق بشر ایرانیان موعظه می‌کنید! عجب نفاق و ریاکاری!
🔸
وزیر خارجۀ فرانسه روز گذشته در اظهاراتی عنوان کرد کشورش تا زمانی که مذاکرات هسته‌ای ایران به انتظارات خود نرسد و به موضوع موشک‌های بالستیک و نیروهای نیابتی ایران نپردازد، با لغو تحریم‌های شورای امنیت سازمان ملل علیه ایران مخالفت خواهد کرد. این دیپلمات ارشد فرانسوی همچنین در اظهاراتی به مداخله در امور داخلی ایران پرداخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/443307" target="_blank">📅 00:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443306">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEzoG3fhihryBvQFy7azo-Z-L4OK9IODclBvs3Pb0J5jI4MFonXSHkndiSI_gi1UeN-QrmRufJCTc81Qvu1LV_madiwjpUVTP4ASo3y4-VCqYuYBK9fy2rPNMAYQADYM717YRN3grUJuI-txd2cIkOEq3eM5JPhyqxXCScRBV2KApjjiwZuoLb-2eYKmesZ8CpeHSk7b6NsC-Mtx0VGt3yNcx6oHaY_tLWelWggL5ZkGHDI4Aggnq9Ie_eIz02PSYdJUkJAB6tp6v9K-RCSC5ffp9cf87MExGMKQdBG4VeXIaQag51tFja32m9hh0ULAEhOEdNZykLYEtThArGpp-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان فضایی: مهم‌ترین پروژه‌هایی که در آیندهٔ نزدیک برنامهٔ پرتابش را داریم، ماهوارهٔ «پارس ۲» است.</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/443306" target="_blank">📅 00:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443305">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2674fd9d79.mp4?token=kR1_DA3vprpMlWk_aZc90WZARNhTA83dGqhuQSj-c-XJqYqO03PWXYGEb0G795P7xsIOtQhLjXWaBL4WjTwETzrgqkfZrFhbIDq8Ecrp_2K9y-rMZOswA5jF9GWKOno2Ly8S2CgaKMC7YKwKjcdErhtDhUYG-ZYWICvSR_DqXrE_8xizcgpbLbJdfKeQpi45j9i_7TYs99ty1EsZG6oUiHI0SqiuJSWGYgZu1Kx92R81a-vrqLVv7ae6pZPddbRVcLeT4O9pmirKr-4I5pHPYg2fB_f-n7MQc-Wbf139-mp9gek4uz6aN02Bh8ki4oBISYTrjHL2HyVrzsYPxCGCXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2674fd9d79.mp4?token=kR1_DA3vprpMlWk_aZc90WZARNhTA83dGqhuQSj-c-XJqYqO03PWXYGEb0G795P7xsIOtQhLjXWaBL4WjTwETzrgqkfZrFhbIDq8Ecrp_2K9y-rMZOswA5jF9GWKOno2Ly8S2CgaKMC7YKwKjcdErhtDhUYG-ZYWICvSR_DqXrE_8xizcgpbLbJdfKeQpi45j9i_7TYs99ty1EsZG6oUiHI0SqiuJSWGYgZu1Kx92R81a-vrqLVv7ae6pZPddbRVcLeT4O9pmirKr-4I5pHPYg2fB_f-n7MQc-Wbf139-mp9gek4uz6aN02Bh8ki4oBISYTrjHL2HyVrzsYPxCGCXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ما رابطهٔ بسیار خوبی با اسرائیل داریم؛ نتانیاهو یک جنگجو است
🔹
اسرائیلی‌ها باید از نتانیاهو قدردانی کنند، چون او واقعاً کارش را انجام داد. ما واقعاً در کنار اسرائیل به سختی مبارزه کردیم. @Farsna</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/443305" target="_blank">📅 00:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443304">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d2fd01ab5.mp4?token=SkFo-5KCchTXq6dt8r5D7-0jidoJbWll2pclvByadoeHDpV8WLnvE5NZUEuWvS0tJz6xad4u5JeoX2Utyh9AUAuDaf2KZCdBmy3wpB8HxPZMQ9_MnPvfPACTKOPIYyV3tGhyjjJFH7U1CCyz1Tn1O06mQautenFpzi_ZVrrKtHehqa3c8nhDPOPT708M706OWl0D0AoJ-REVPryKX6y9_a5afw4PINiMnZdqpwlCtX059BdHUe2hrWql7tWjnN441LLjNqlg1IqLuflL1kVe8txlTJjz9oP1O9HKq4YftoCs0YhIJ7OHMveEXnZWOistAyadgV40iUa7ZQO2piltnQvkFdTRCIC5d1JQgCSiJZarjkgljhlzToUW_psHp8QirOc0a_ltdgjHfcBUMZr0z1s0ph27Vsvg219KN0ZpmlH44pHJDPrbSBtXfPxXYjJfk75H-KBAaSjbZG1TUtWquDoRNXqiTzWegbW7iF99jSzdvWfDT455Yg8mUkuAFtLNSSWSJsjpvXtzimzGu7JAXkYKYhP5dposQhHSVVbVJalMltc_MhT19w0JKCL9OEhbdasrh16RCetEWezMiIEiJbIjK4mTDyTRprldu59Mg1mwb45TA9pamg0MNUXN6lTBT944LYeUb4DOIOxMNyuJYQAh74syNry1ul3hZHDKKwc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d2fd01ab5.mp4?token=SkFo-5KCchTXq6dt8r5D7-0jidoJbWll2pclvByadoeHDpV8WLnvE5NZUEuWvS0tJz6xad4u5JeoX2Utyh9AUAuDaf2KZCdBmy3wpB8HxPZMQ9_MnPvfPACTKOPIYyV3tGhyjjJFH7U1CCyz1Tn1O06mQautenFpzi_ZVrrKtHehqa3c8nhDPOPT708M706OWl0D0AoJ-REVPryKX6y9_a5afw4PINiMnZdqpwlCtX059BdHUe2hrWql7tWjnN441LLjNqlg1IqLuflL1kVe8txlTJjz9oP1O9HKq4YftoCs0YhIJ7OHMveEXnZWOistAyadgV40iUa7ZQO2piltnQvkFdTRCIC5d1JQgCSiJZarjkgljhlzToUW_psHp8QirOc0a_ltdgjHfcBUMZr0z1s0ph27Vsvg219KN0ZpmlH44pHJDPrbSBtXfPxXYjJfk75H-KBAaSjbZG1TUtWquDoRNXqiTzWegbW7iF99jSzdvWfDT455Yg8mUkuAFtLNSSWSJsjpvXtzimzGu7JAXkYKYhP5dposQhHSVVbVJalMltc_MhT19w0JKCL9OEhbdasrh16RCetEWezMiIEiJbIjK4mTDyTRprldu59Mg1mwb45TA9pamg0MNUXN6lTBT944LYeUb4DOIOxMNyuJYQAh74syNry1ul3hZHDKKwc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مردم اراک: فداییان رهبریم، از شروط نمی‌گذریم
@Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/443304" target="_blank">📅 00:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443303">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33b806bb2.mp4?token=t3Un_a57vDSdFMKRkeiuqjAUCwhON7dBl7K4hM-4gl7i6ij2c4-RqfWeOzDJm4ABE9-QNI97KFvFHEE6xUNA8UUgau3t6hnqdL_hVeTvtNBG1UK9RD_4sgkKErsKMjFziQ_EqmHOHLFeutqw1JcjRIjyPaVzR28E_bW9LMDktsTS1G2H2E98Px1R8_vmQx2d6PEf6FYyVqEh6sBCRzF4mRPeuqVYVYyOL4AX62vaI6D2VV_dlCgAzWkHa9txSkqhOrEEceiFjxpg9O3fZ4G4Tg6gRgTc0niUL4k8BZHPSsBfQKTcFE9cq9cHrNMG2IVmyJQsIy0GmnlJLFlx8v5LVoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33b806bb2.mp4?token=t3Un_a57vDSdFMKRkeiuqjAUCwhON7dBl7K4hM-4gl7i6ij2c4-RqfWeOzDJm4ABE9-QNI97KFvFHEE6xUNA8UUgau3t6hnqdL_hVeTvtNBG1UK9RD_4sgkKErsKMjFziQ_EqmHOHLFeutqw1JcjRIjyPaVzR28E_bW9LMDktsTS1G2H2E98Px1R8_vmQx2d6PEf6FYyVqEh6sBCRzF4mRPeuqVYVYyOL4AX62vaI6D2VV_dlCgAzWkHa9txSkqhOrEEceiFjxpg9O3fZ4G4Tg6gRgTc0niUL4k8BZHPSsBfQKTcFE9cq9cHrNMG2IVmyJQsIy0GmnlJLFlx8v5LVoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد زنجانی‌ها: حزب‌الله دلاور کنارتیم تا آخر
@Farsna</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/443303" target="_blank">📅 23:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443302">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e891b77b63.mp4?token=bAnzMD_q12SkQXk3qFoR-DgvBxlqOKHrUONslhkicYv5J45UlMdoLvWEvygSv4gly4hgUCUHv6ukSghVe6LqqFqlV5VzylsbGkVra74HN81XYXoL1xC3RvbAwlGEOBpy4Wv9QTM_twHecn514GCBY5RPEhOspDQRZkP4ZLR55yJ0vR4ZLqw4D2M6SySWipVqe48ICtK8ORPf0fHA_z9aIonTZEBFDUua9qTNEzB1CqHykawIsmGqE2T9JZrEWbAm2G28Rpqdg0VZwq3apzfibceFKxtGAXGUQKV0u6alg9_1KroPBvipiVLoxkM8QoPqwk_yggybHYTe8usAOIamig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e891b77b63.mp4?token=bAnzMD_q12SkQXk3qFoR-DgvBxlqOKHrUONslhkicYv5J45UlMdoLvWEvygSv4gly4hgUCUHv6ukSghVe6LqqFqlV5VzylsbGkVra74HN81XYXoL1xC3RvbAwlGEOBpy4Wv9QTM_twHecn514GCBY5RPEhOspDQRZkP4ZLR55yJ0vR4ZLqw4D2M6SySWipVqe48ICtK8ORPf0fHA_z9aIonTZEBFDUua9qTNEzB1CqHykawIsmGqE2T9JZrEWbAm2G28Rpqdg0VZwq3apzfibceFKxtGAXGUQKV0u6alg9_1KroPBvipiVLoxkM8QoPqwk_yggybHYTe8usAOIamig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ما رابطهٔ بسیار خوبی با اسرائیل داریم؛ نتانیاهو یک جنگجو است
🔹
اسرائیلی‌ها باید از نتانیاهو قدردانی کنند، چون او واقعاً کارش را انجام داد. ما واقعاً در کنار اسرائیل به سختی مبارزه کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/443302" target="_blank">📅 23:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443301">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d6e2275b7.mp4?token=og6jppPg9AMWFKOo35lkJNSa83IhVQcNeLSqNfEjZX6-Yg6_QVWAoo3CCucvRL8uFUDJCEfknNsvBK_9Y80cbo3jItxp52T2H8bBr7oGXl1rvxS87FxXLhXQ-Wx3u32Od7pr14YOrZzmYTrrjDuDdQwDoYDNpTXJ8YZ4ySkL9mys06BU7OlpBhyQD0Gh6CvcLH4TffqgwsFs0yZLsq58zzRocgPVMORenMHTTC5ECcnu77AzdE-fb9GlH6lDn4jjW98vfI59rjRToycXLdRra2eR50-wmr4KNGHQkoxQy-QjHYMN0S6SQk5Tj3IYHnnCzBTlVk-h5RUBkd-Qh99VH5mLpl8HADqdTCo5C8wGCWpK01GrTcn17GrYqansQQTV86asRq4pezbSFSzaAmF6vA7XQ6xI_NeesC1HmK3fOXwuDg6F-SQz2c8nBRoaaw5WwSNcpJ1dngsASAwIlz_ORoE2tsKPMp511fWk2kqFyXvA2vORjj8Ck_lCtZm0vIQAbCCyaJQHo9Cb61pjZWWCubVK-hMTlHmlHk7-aPe_s3OZCUpHGLY_g4dajWejKI-NHwH8U0SWRQfvVXcJ8kcZQE6a3fT4-cTfyxcsteVlaq6a-9jQDcEC_e4bVMHovg_AbjfVQPMbkXhSluY38iOf37ahGmB6UCkUArDcN2QNSbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d6e2275b7.mp4?token=og6jppPg9AMWFKOo35lkJNSa83IhVQcNeLSqNfEjZX6-Yg6_QVWAoo3CCucvRL8uFUDJCEfknNsvBK_9Y80cbo3jItxp52T2H8bBr7oGXl1rvxS87FxXLhXQ-Wx3u32Od7pr14YOrZzmYTrrjDuDdQwDoYDNpTXJ8YZ4ySkL9mys06BU7OlpBhyQD0Gh6CvcLH4TffqgwsFs0yZLsq58zzRocgPVMORenMHTTC5ECcnu77AzdE-fb9GlH6lDn4jjW98vfI59rjRToycXLdRra2eR50-wmr4KNGHQkoxQy-QjHYMN0S6SQk5Tj3IYHnnCzBTlVk-h5RUBkd-Qh99VH5mLpl8HADqdTCo5C8wGCWpK01GrTcn17GrYqansQQTV86asRq4pezbSFSzaAmF6vA7XQ6xI_NeesC1HmK3fOXwuDg6F-SQz2c8nBRoaaw5WwSNcpJ1dngsASAwIlz_ORoE2tsKPMp511fWk2kqFyXvA2vORjj8Ck_lCtZm0vIQAbCCyaJQHo9Cb61pjZWWCubVK-hMTlHmlHk7-aPe_s3OZCUpHGLY_g4dajWejKI-NHwH8U0SWRQfvVXcJ8kcZQE6a3fT4-cTfyxcsteVlaq6a-9jQDcEC_e4bVMHovg_AbjfVQPMbkXhSluY38iOf37ahGmB6UCkUArDcN2QNSbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: اگر با ایران سرسختانه‌تر رفتار می‌کردیم تنگه هرمز باز نمی‌شد
🔹
می‌گویند چرا سختگیرتر عمل نمی‌کنی؟ اجازه بدهید توضیح بدهم؛ تنها راهی که می‌توانستم سختگیرتر باشم این بود که دو یا سه هفته دیگر وارد عمل می‌شدم و به بمباران شدید آن‌ها ادامه می‌دادم، درست…</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/443301" target="_blank">📅 23:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443300">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81dafdbf72.mp4?token=e9xcMv9qMNWU29L_pNAVzoXsyQbFYv02_VVuboq2g19ftQaVn-KoV-_GW1t9HsiOExviPOr8WcpQq-KJlnQ8fNIeKnOcA9j4O5zWHAI6gCKBlysgrOjdBxfYX5-Cwr-s3gjNegBBoa0hhJICLsGLQWLmGJTN7qMnd2Nnb7CQubCzzsyPpVJofa4qVdHAppfJbr-cvgA1feMxo_d1qAPuBWCvZ8hfRvzQda9KWZyJ90rhP3IrNPQbUQ4qk4FOza2_bkhgeppPsm8GQVz1tHUVRedAJpIu50i-snzn5hV0h2zFTObDdW2aDJDdhvcT3Ol81MSJsgkhwv3sKPJKNgEp_IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81dafdbf72.mp4?token=e9xcMv9qMNWU29L_pNAVzoXsyQbFYv02_VVuboq2g19ftQaVn-KoV-_GW1t9HsiOExviPOr8WcpQq-KJlnQ8fNIeKnOcA9j4O5zWHAI6gCKBlysgrOjdBxfYX5-Cwr-s3gjNegBBoa0hhJICLsGLQWLmGJTN7qMnd2Nnb7CQubCzzsyPpVJofa4qVdHAppfJbr-cvgA1feMxo_d1qAPuBWCvZ8hfRvzQda9KWZyJ90rhP3IrNPQbUQ4qk4FOza2_bkhgeppPsm8GQVz1tHUVRedAJpIu50i-snzn5hV0h2zFTObDdW2aDJDdhvcT3Ol81MSJsgkhwv3sKPJKNgEp_IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۱۱۱ قیام لشگر حسینی مدافعان ایران در الوند
@Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/443300" target="_blank">📅 23:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443299">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a2583bd5c.mp4?token=Rq2cx1CNAft9QdwqBLEE0_E-Fu80DlwDN25azFrwhodB9leaLaR0cSjpG8ycM7Ckf-0vVF3h9FA_6EmjKyOCz1z0t5N9B8mno2Drtd7bFNusZDberItcCxIVMlYx6SDjmzHHtJv-P0556KquyzMz8IdFeFQ5wK-Ofr0fGJnCjFjerGZ0Mo4VIITGkbOuJ4WZIg5dzE6vf2l-S9kor1xZG-V7q42xHwImwuYzX1RhMCPuLv8pIVrMUE3onwAgDSEliYr7K-1gy7wH4SGDAVvGFdXzCwWXF8t6GVlGBphrp0N31Yvmn2naKzu5v1sie26Pbd2d8pLqiaDTUHb6-134mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a2583bd5c.mp4?token=Rq2cx1CNAft9QdwqBLEE0_E-Fu80DlwDN25azFrwhodB9leaLaR0cSjpG8ycM7Ckf-0vVF3h9FA_6EmjKyOCz1z0t5N9B8mno2Drtd7bFNusZDberItcCxIVMlYx6SDjmzHHtJv-P0556KquyzMz8IdFeFQ5wK-Ofr0fGJnCjFjerGZ0Mo4VIITGkbOuJ4WZIg5dzE6vf2l-S9kor1xZG-V7q42xHwImwuYzX1RhMCPuLv8pIVrMUE3onwAgDSEliYr7K-1gy7wH4SGDAVvGFdXzCwWXF8t6GVlGBphrp0N31Yvmn2naKzu5v1sie26Pbd2d8pLqiaDTUHb6-134mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام تجمع امشب مردم شهرکرد لبیک به رهبر معظم انقلاب بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/443299" target="_blank">📅 23:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443298">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-WqirGETrWB67xynh0F0AOnKfB97eseJjitQzhc2bPM_VEvoPSdNGOC3cQwOI6IJst2RQ6qf7_5eIYXz-diNSDltBccY-OPjQ4UGCpDecHvNCZAm1mz-enioQvIClWydL03d_-ICHKRamt27XaBASjSC3Cfu-HBS5pTdf2D3LJ5vUGuHXszOryD945wrDl-7ZRTyfgxqLAIR3RdCdGbcyytvSzEe_lu7q0E7leJUps4zCkS5g4TFvVF5IuR5_ghmWLk59ab8098AMvXNRxmckiIQWS3TqneLa2eek1qzylw6XSxzY8XpZuJsljWTcemZ77s2f__saFm6YYSs6toog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله گروهی از نظامیان اسرائیلی را هدف قرار داد
🔹
به گفته منابع لبنانی، رزمندگان حزب‌الله یک بمب را در مسیر تعدادی از نظامیان اسرائیلی که در حال عبور از منطقه علی الطاهر بودند، منفجر کردند.
🔹
در این حمله چند خودروی نظامی آتش گرفت و تعدادی از نظامیان اشغالگر نیز زخمی شدند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/443298" target="_blank">📅 23:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443297">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df838b83ae.mp4?token=lofmiVBHFsT1xSYurlbb9KxxVIZIvSSzVoO5ztoNI5hrYsDMWELe5fksF58Lojbh9NuS8OK3ZTTHfc0Rb63cDndh6_NwGnrX-YR4bQbZq8V4-JTGf5shEx3kqLg-3B9eiq9Rnbs6nnmY0vBIQFMTfy9SU8QStkPMyiZCTpuCV1S12eRVU8shLCMEYCg5ACBNbIos6qmVmSyJR5q7tpRkLfQPuuSVo-SzVebocsnGyjIFqZC5IX7407F5TJkzDySiGY5Rq8j-3Ws6hexExbeWpYkn7owJsA6wYE98kQA2Mc9CYU4ryXibQC3SWEk9U5rg-latKXwGs54BBEFy3FJ9Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df838b83ae.mp4?token=lofmiVBHFsT1xSYurlbb9KxxVIZIvSSzVoO5ztoNI5hrYsDMWELe5fksF58Lojbh9NuS8OK3ZTTHfc0Rb63cDndh6_NwGnrX-YR4bQbZq8V4-JTGf5shEx3kqLg-3B9eiq9Rnbs6nnmY0vBIQFMTfy9SU8QStkPMyiZCTpuCV1S12eRVU8shLCMEYCg5ACBNbIos6qmVmSyJR5q7tpRkLfQPuuSVo-SzVebocsnGyjIFqZC5IX7407F5TJkzDySiGY5Rq8j-3Ws6hexExbeWpYkn7owJsA6wYE98kQA2Mc9CYU4ryXibQC3SWEk9U5rg-latKXwGs54BBEFy3FJ9Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری مردم بجنورد در تجمع شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/443297" target="_blank">📅 23:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443296">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8cea19557.mp4?token=UhIch277zyOvxSgTzCJaCxqx-JQ09WZB-KBpFxCHTw-5X8bPgplMGwhkV1MONAiIPFEWEfPiAdG-ujw5GIn3UMTM2QBiLbXTrE8hBXg1DDA6QMraehzywa0_rZkjU3-wHD-3nnetkiY7AU0Cy86xSqnURltRW6ZRQTpjgwZUoeA66ddsr4y668NAm8YE2BfJM0G_8SA2X9NpTmMYTSkfVjywNNB7xOFb_5FgXrYoQ1DozWnt7W64lMpoDqnPZIlCxnAI4xHBDl52ZoL2c3XQdpm17bSTnlDD1QiPhjtK2Mzqpymb75qSvAxA5UgQWmtWr4GWks157o1A2UUhEYnpLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8cea19557.mp4?token=UhIch277zyOvxSgTzCJaCxqx-JQ09WZB-KBpFxCHTw-5X8bPgplMGwhkV1MONAiIPFEWEfPiAdG-ujw5GIn3UMTM2QBiLbXTrE8hBXg1DDA6QMraehzywa0_rZkjU3-wHD-3nnetkiY7AU0Cy86xSqnURltRW6ZRQTpjgwZUoeA66ddsr4y668NAm8YE2BfJM0G_8SA2X9NpTmMYTSkfVjywNNB7xOFb_5FgXrYoQ1DozWnt7W64lMpoDqnPZIlCxnAI4xHBDl52ZoL2c3XQdpm17bSTnlDD1QiPhjtK2Mzqpymb75qSvAxA5UgQWmtWr4GWks157o1A2UUhEYnpLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ماکرون زمان زیادی رئیس‌جمهور فرانسه نخواهد بود
🔹
امانوئل ماکرون، رئیس‌جمهور فرانسه که البته دیگر زمان زیادی در این سمت نخواهد بود، در میزبانی اجلاس جی۷ عملکرد فوق‌العاده‌ای داشت.
🔹
او حدود یک هفته قبل از مراسم از من دعوت کرد و گفت: «می‌شود لطفا لطفی…</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/443296" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443295">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86872fd21b.mp4?token=FiEuLVoXDCE42i4fjmffkklmxkW0-cSo3Twlid0q5gTwewQJGQalnnc8u4kOWgDxZAsFfZRQsRk9DXY8umCvPCRc5G1Sik9RlAtCvEW8A56Yj-9om2rIVEUnWPmDB2jl4RGgJFTZ5JkcfaqaZtjJXj4nEFMu9t8ygIl-37wNgILy_QWaN_fUlVFE1HS6XEUREeyPjEtOMtMqx7X_t_lJy9cUvr79hche7RWARwhvDgESqGPKzIWTutGtsHSF8MsSV0cp7IGrH1w0KxcwRnubLMAAMmnlcap-qwUIU4C9MYuIwWDik0ToI28fCroJ-JhE95pdrhdKsOxJimliKz8f0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86872fd21b.mp4?token=FiEuLVoXDCE42i4fjmffkklmxkW0-cSo3Twlid0q5gTwewQJGQalnnc8u4kOWgDxZAsFfZRQsRk9DXY8umCvPCRc5G1Sik9RlAtCvEW8A56Yj-9om2rIVEUnWPmDB2jl4RGgJFTZ5JkcfaqaZtjJXj4nEFMu9t8ygIl-37wNgILy_QWaN_fUlVFE1HS6XEUREeyPjEtOMtMqx7X_t_lJy9cUvr79hche7RWARwhvDgESqGPKzIWTutGtsHSF8MsSV0cp7IGrH1w0KxcwRnubLMAAMmnlcap-qwUIU4C9MYuIwWDik0ToI28fCroJ-JhE95pdrhdKsOxJimliKz8f0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین مرگ بر آمریکا در تجمع مردم نیشابور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/443295" target="_blank">📅 23:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443294">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfDfXfd0BizKcbbw43Vj_GIKOyyIVsSqN1P8PDSrzXChis8iYxp2KvAQt26JAWQLtUh-lTIQ7D0ENpkKi8eTfb24hcX7hc2kGElTPv2mIxH-kZoFZguxDgNkCVFXsf6SW0TxgTFhWLvg6QVfbeCcXPLJt6MxK2SAieFvHOp23Mlz51uV9GORJzgNky9hQKwWE3P42AcmqxepS8KJEImwm0_p3a-b-GVMAx8slb2kv90L8yYUqJ_w4DTmBAQHA9KKRy6F8Jw9ThzKvyh_kGsPei3o2ZZ14BHQBYlDfBLz0JkvKF7KFv4imyjcpaP41smVnMAVNZP2bAQfUafBwNGT5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی: حکمرانی بر تنگۀ هرمز و اقتدار منطقه‌ای ایران نباید تضعیف شود
🔹
متنی که برای توافق تهیه می‌شود باید از نظر فنی و حقوقی کاملاً دقیق و متناسب با خواسته‌های ما باشد؛ در مورد رفع تحریم‌ها، باید کلمات به دقت تنظیم شوند. در مورد رفع محاصره نیز باید به طور مشخص بیان شود.
🔹
مثلاً ما در این ۱۴ بند خواسته‌ایم که نیروهای آمریکا ۳۰ روز پس از توافق نهایی از پیرامون ایران خارج شوند. اما ممکن است آن‌ها بگویند که «پیرامون شما» شامل ۱۲ مایل ساحلی آب‌های شماست که این برای ما قابل قبول نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/443294" target="_blank">📅 23:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443293">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de95f3d4c.mp4?token=E8lxso9plZtil2HvVe84QNS8PD2xieynyzTYPv-oyt-GWjG3zEev6n-l9QCIiRK6ynLvMNhc_lK4zkxHCaERATM3o61EryA57SkDHUDssEfDg6hsUxQ9ucJnAeSU1Z8UKi2D_zVEwIF_NgkIsleY08z0aWXGQBx85D9fKA8SubEmsCI815ck_Sx6ClwVwRszmtvfneobQ5UBSHkawJvVMqK0r8j-03mUBtJmtVM4v9UCYm5LEeI2e5nMNx62V3H88KU2u2eIg5ISZxPfnsM9rFD2r0dIve3BQRE6tdPLU7lBgtvnA9IpDviQ0DTWZs37tbVCyfNW_vx9LQhBRuPWWYgUdRd6DrAE5drnlSnZ_74-ND4Z9gMxArtfqphH5tyyymA02SoCxjsQ9D_nkQXLsFrMFQoxu10q_0HkSFKk_CayToLCCZ6TPOA2Hycq9qNZJNyPtziAWOj4M4VRgpgFfFoHuRI53z0_R-mfJ8o_PYVfMN9eiHBiII74lUNhVkFwaoO0oKws_XAvC64pjgdYCE937c4fyfSo8-Q5yINfVsqWBD7Eb37ocTSJ39SJdORzQ_LTj4NI1o0Gr_JM-zCNbDyL-m2Tad9z2-El-q0mZO6fWYuTqkFaa3l-dRdNLxGtE5XK5IgKDZ6S-RUgQpXlqJeNAPmHDUASfnwcgy7k_kE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de95f3d4c.mp4?token=E8lxso9plZtil2HvVe84QNS8PD2xieynyzTYPv-oyt-GWjG3zEev6n-l9QCIiRK6ynLvMNhc_lK4zkxHCaERATM3o61EryA57SkDHUDssEfDg6hsUxQ9ucJnAeSU1Z8UKi2D_zVEwIF_NgkIsleY08z0aWXGQBx85D9fKA8SubEmsCI815ck_Sx6ClwVwRszmtvfneobQ5UBSHkawJvVMqK0r8j-03mUBtJmtVM4v9UCYm5LEeI2e5nMNx62V3H88KU2u2eIg5ISZxPfnsM9rFD2r0dIve3BQRE6tdPLU7lBgtvnA9IpDviQ0DTWZs37tbVCyfNW_vx9LQhBRuPWWYgUdRd6DrAE5drnlSnZ_74-ND4Z9gMxArtfqphH5tyyymA02SoCxjsQ9D_nkQXLsFrMFQoxu10q_0HkSFKk_CayToLCCZ6TPOA2Hycq9qNZJNyPtziAWOj4M4VRgpgFfFoHuRI53z0_R-mfJ8o_PYVfMN9eiHBiII74lUNhVkFwaoO0oKws_XAvC64pjgdYCE937c4fyfSo8-Q5yINfVsqWBD7Eb37ocTSJ39SJdORzQ_LTj4NI1o0Gr_JM-zCNbDyL-m2Tad9z2-El-q0mZO6fWYuTqkFaa3l-dRdNLxGtE5XK5IgKDZ6S-RUgQpXlqJeNAPmHDUASfnwcgy7k_kE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری شیرخوارگان بروجردی در حماسۀ خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/443293" target="_blank">📅 22:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443292">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f337e5e65.mp4?token=D7lfpFjwqbTHh0g3gf_EM0siAffLJy8U6xDfpj_4autA0kblmDG8qLAmwgA5N4Uq0YzsZuXVvqiV8_pJ8thuF7FxJSqn9gQZC0Z6sSaMF1jfgLDZUsXetr4lwPLQAenQZDr2uZwYF5hq9DIZgY8vVxGYDcOMngOmrkz30Qz_xOxRl_1hCUKCLpdr-usEISeL5CINWxksLGTBkmJVDkXFwfpBpF_iFAo6Cc_LA2BHEUXEqw-FUHmdrRJk1pLFd49E-UbgexdiYks5VlpCeI2yWOjkp_eThKkgvPLdIPwT9ADx0PCXgxHjrm-aSF0hm00xCkF5pEEidBFByLe5NT4aTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f337e5e65.mp4?token=D7lfpFjwqbTHh0g3gf_EM0siAffLJy8U6xDfpj_4autA0kblmDG8qLAmwgA5N4Uq0YzsZuXVvqiV8_pJ8thuF7FxJSqn9gQZC0Z6sSaMF1jfgLDZUsXetr4lwPLQAenQZDr2uZwYF5hq9DIZgY8vVxGYDcOMngOmrkz30Qz_xOxRl_1hCUKCLpdr-usEISeL5CINWxksLGTBkmJVDkXFwfpBpF_iFAo6Cc_LA2BHEUXEqw-FUHmdrRJk1pLFd49E-UbgexdiYks5VlpCeI2yWOjkp_eThKkgvPLdIPwT9ADx0PCXgxHjrm-aSF0hm00xCkF5pEEidBFByLe5NT4aTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: من بزرگ‌ترین پل ایران را به این دلیل که آن‌ها دیر به یک جلسه رسیدند، از بین بردم
🔹
آن پل، در واقع حکم پل جرج واشنگتنِ آن‌ها را داشت. من آن را ظرف ۳ دقیقه با خاک یکسان کردم. @Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/443292" target="_blank">📅 22:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443291">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8222fb9f5a.mp4?token=svSUSGHP1U8Xyj2g_lcxQHlkyC-eb6jXuadxKRv9-MgS3ArRBOLjpJpTC_Ff9LUmCINzqB7IrUot6t-UzJpl0-1q2sfJZq6mGLfuPgEhFAu72jzz2VoaO4kAzpIjMVOV9Sjm90N7G06j5etFleRrJMNwuMTa3xZeLjltrueHwOJVimyIALabPqMZJELLB9dIhrzVR5Xhccv02zckAU16Dyi1UGFaUQlogJkkzzzjwOLR8ScLb84CRub4oYLMIbYF-wMz9cBx-1mNP0xtRDyKSziXTBsTKXw4fVN7stBS5KGtahTW5BAQctDbT3i9iCuCp6GQbhm_kLP4Y3rJcBrwhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8222fb9f5a.mp4?token=svSUSGHP1U8Xyj2g_lcxQHlkyC-eb6jXuadxKRv9-MgS3ArRBOLjpJpTC_Ff9LUmCINzqB7IrUot6t-UzJpl0-1q2sfJZq6mGLfuPgEhFAu72jzz2VoaO4kAzpIjMVOV9Sjm90N7G06j5etFleRrJMNwuMTa3xZeLjltrueHwOJVimyIALabPqMZJELLB9dIhrzVR5Xhccv02zckAU16Dyi1UGFaUQlogJkkzzzjwOLR8ScLb84CRub4oYLMIbYF-wMz9cBx-1mNP0xtRDyKSziXTBsTKXw4fVN7stBS5KGtahTW5BAQctDbT3i9iCuCp6GQbhm_kLP4Y3rJcBrwhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: بدون تغییر رفتار ایرانی‌ها هیچ‌ سرمایه‌گذاری‌ای در ایران انجام نخواهد شد
🔹
بزرگ‌ترین سوءتفاهم این است که تصور می‌شود سرمایه‌گذاری در ایران بدون هیچ‌گونه تغییری در رفتار [ایران] انجام خواهد شد.
🔹
این ایده که اماراتی‌ها یک میلیارد دلار برای ساخت نیروگاه در ایران سرمایه‌گذاری کنند، بدون اینکه ایرانی‌ها رفتار خود را تغییر داده باشند، کاملاً مضحک است.
🔹
آن‌ها چنین کاری نخواهند کرد و ما نیز اجازه این کار را نخواهیم داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/443291" target="_blank">📅 22:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443290">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c612bc2d1.mp4?token=AG4JKL8C9j3TqzNRMaQdHQA9JBHHb_OdbSd45OVbwwjO3OjcXaKCe8pao_Py3lx0Vb9Eg9Hrvw9gTscbsmocN3I3oKRgSqmAINKrij2nvJKBFqmiu1i_GCE0lzS-2xt1E6n6zfsPp6fPDRGgmFtPepCNvMoTKZsDmyyXkPualltdflb-QFTYC8TAWS2ojby6gPKtutBGnYdn6tIKyAhFu2gWMt6aQduMosGwJkBabtdFV-jbQJxDgsK2MnbohRYC-BVcosK0Fv6nAaWHH0rLG1qySfNs79NDY2KU_2gpfoU7JSKclFaZgL4WXxbIHnK0uGfjX8DfyWGAfcLks0yxGpCVMF8Roagxe6BrDVlL6hek6IKJTOEp_BUGZsUJUX0rgjxuJX-BhuFi7jnW0sB2dWdJ9rOBmfK2BTMf3KP9AKYYLX-LyGSS4iKxiL7H1wOEneu-rAeBNqFX8Vn7sD_l6xeQkJvhVB1rEY-Ou_NiFuc6M6Hx69-M1ZV5zEVFwUXPIlrVBunQ0_r8uGM6OOt9mo3-BRmauHNDqhJ7u4UsxZTuVfXk9_qfcJV4lARv9cPYlh-kDuS8NIyMVHYEVhUFvXZGJqd21cLxSY48Fsv1Q78JVKPcPFvJ70A0o9wN7pI99rY7s4MeCspiADrBEEXNd884LMRB3i4E5UkXBeMP4Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c612bc2d1.mp4?token=AG4JKL8C9j3TqzNRMaQdHQA9JBHHb_OdbSd45OVbwwjO3OjcXaKCe8pao_Py3lx0Vb9Eg9Hrvw9gTscbsmocN3I3oKRgSqmAINKrij2nvJKBFqmiu1i_GCE0lzS-2xt1E6n6zfsPp6fPDRGgmFtPepCNvMoTKZsDmyyXkPualltdflb-QFTYC8TAWS2ojby6gPKtutBGnYdn6tIKyAhFu2gWMt6aQduMosGwJkBabtdFV-jbQJxDgsK2MnbohRYC-BVcosK0Fv6nAaWHH0rLG1qySfNs79NDY2KU_2gpfoU7JSKclFaZgL4WXxbIHnK0uGfjX8DfyWGAfcLks0yxGpCVMF8Roagxe6BrDVlL6hek6IKJTOEp_BUGZsUJUX0rgjxuJX-BhuFi7jnW0sB2dWdJ9rOBmfK2BTMf3KP9AKYYLX-LyGSS4iKxiL7H1wOEneu-rAeBNqFX8Vn7sD_l6xeQkJvhVB1rEY-Ou_NiFuc6M6Hx69-M1ZV5zEVFwUXPIlrVBunQ0_r8uGM6OOt9mo3-BRmauHNDqhJ7u4UsxZTuVfXk9_qfcJV4lARv9cPYlh-kDuS8NIyMVHYEVhUFvXZGJqd21cLxSY48Fsv1Q78JVKPcPFvJ70A0o9wN7pI99rY7s4MeCspiADrBEEXNd884LMRB3i4E5UkXBeMP4Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بجنگ پهلوان بجنگ
نماهنگ جدید مهدی رسولی در آستانه دیدار تیم ملی فوتبال ایران با بلژیک
@Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/443290" target="_blank">📅 22:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443289">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e3f93872f.mp4?token=BrbQmg_yw0w-3u_ZZsYplMxHJX-9V1pYbTfmOJLlOoj9X9R9Got_9Hv7iiDF3r50qU2TAxlKqVMA_QZgysYBWkyCTFKgGzYC99e61xdCDP9_df5qWZXVU53NEvFF6-R939_h_ZCL3ei8cmhIn2nXKaq4l6KiTtZjZWPR27cxah7vRI8Tkzwzkhz1embUMBkh_DWtbT9_7qMeYzdq-6SUHOKDE9zDrtIvW1dXop7spA_-9dH0_auW4xT5zyLqtLRGD7owZv586DJHblZdqUPAEEUz8OrYdZ6TpNJ_nsjOsvNQXeMnkPrt189cSoZqxysxz97PNshjq1faqIxXrPUWgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e3f93872f.mp4?token=BrbQmg_yw0w-3u_ZZsYplMxHJX-9V1pYbTfmOJLlOoj9X9R9Got_9Hv7iiDF3r50qU2TAxlKqVMA_QZgysYBWkyCTFKgGzYC99e61xdCDP9_df5qWZXVU53NEvFF6-R939_h_ZCL3ei8cmhIn2nXKaq4l6KiTtZjZWPR27cxah7vRI8Tkzwzkhz1embUMBkh_DWtbT9_7qMeYzdq-6SUHOKDE9zDrtIvW1dXop7spA_-9dH0_auW4xT5zyLqtLRGD7owZv586DJHblZdqUPAEEUz8OrYdZ6TpNJ_nsjOsvNQXeMnkPrt189cSoZqxysxz97PNshjq1faqIxXrPUWgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداران گرگان امشب در خیابان نماز استغاثه خواندند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/443289" target="_blank">📅 22:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443288">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b64596567.mp4?token=XtiTlVkgTE-iIskFON0Hw4G4r-ZyK49kvwTHplO1NQaNtqXmukkqQDAGNzmGRJUkNGoQv3DyQOqzO5ZTGRaTus_A6_vyO6Y6I7RD-F40wo3WS8rmbCpOqSjKCCQtfo50y8dmGMdDZkKJv6BQ94Ie5qlawHjtH0-sSlN0uITwvnDBBVtj10zCdqqKTTK2ozRnv4Q5zlwCrNyhRu8lmXqgJQY8h_ftpnrTpppz7z9BGdAJamll7Z9x2sAERglGa5-d7PCJgwupRBUIFCVi8Qgu3Hgu_fIurEJycaE0JEJvHKpTjS0vM8MTs2qgksFdbsni_-MCRPu5sSjMio2ZEbVcFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b64596567.mp4?token=XtiTlVkgTE-iIskFON0Hw4G4r-ZyK49kvwTHplO1NQaNtqXmukkqQDAGNzmGRJUkNGoQv3DyQOqzO5ZTGRaTus_A6_vyO6Y6I7RD-F40wo3WS8rmbCpOqSjKCCQtfo50y8dmGMdDZkKJv6BQ94Ie5qlawHjtH0-sSlN0uITwvnDBBVtj10zCdqqKTTK2ozRnv4Q5zlwCrNyhRu8lmXqgJQY8h_ftpnrTpppz7z9BGdAJamll7Z9x2sAERglGa5-d7PCJgwupRBUIFCVi8Qgu3Hgu_fIurEJycaE0JEJvHKpTjS0vM8MTs2qgksFdbsni_-MCRPu5sSjMio2ZEbVcFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ایرانی‌ها مردم بسیار باهوشی هستند
🔹
من باید آن‌ها را متوقف می‌کردم، زیرا اگر به سلاح هسته‌ای دست پیدا می‌کردند، از آن علیه اسرائیل استفاده می‌کردند.
🔹
من به توافق باراک حسین اوباما، یعنی برجام، پایان دادم؛ توافقی که مسیری برای دستیابی ایران به سلاح…</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/443288" target="_blank">📅 22:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443287">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf812ba81f.mp4?token=nT7CV0oPeI4S-3R7uxhOp_G0Kd4oroEs4HZmA2kBVUtfH3_drvksA-mfHuwS3mGBJIs6xCJ3y3zdVtwiGdOv3SLc0oRm-elETnXbBopsiFcz683rftCN8rhomV5eVkKgzN-z1hZMMEmVGUCc3w9G_DPDM8PWGB8mM0eos_-OrBkYDg_8MFZ1Z6X5HTvt4Epu0QFDPb7ZpzL_xCUJQ7crVwc0ANYW8yUx77Ko27YCwiOaZR2-2wbyvc4Xbvn1qAJ0ZMOPyFgjs2vf7eJwkLHyfteMz9CXr9h0JTkZX3QVtwUVOvGQsTlsGB1lNrsQ07CZ9UTD8bKffPAzwPlvD_K7Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf812ba81f.mp4?token=nT7CV0oPeI4S-3R7uxhOp_G0Kd4oroEs4HZmA2kBVUtfH3_drvksA-mfHuwS3mGBJIs6xCJ3y3zdVtwiGdOv3SLc0oRm-elETnXbBopsiFcz683rftCN8rhomV5eVkKgzN-z1hZMMEmVGUCc3w9G_DPDM8PWGB8mM0eos_-OrBkYDg_8MFZ1Z6X5HTvt4Epu0QFDPb7ZpzL_xCUJQ7crVwc0ANYW8yUx77Ko27YCwiOaZR2-2wbyvc4Xbvn1qAJ0ZMOPyFgjs2vf7eJwkLHyfteMz9CXr9h0JTkZX3QVtwUVOvGQsTlsGB1lNrsQ07CZ9UTD8bKffPAzwPlvD_K7Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میثاقی: باتوجه به اخبار به‌نظر می‌رسد ۵ تیر برای سهمیه آسیایی یک بازی بین پرسپولیس با چادرملو برگزار شود و برنده باید با گل‌گهر بازی کند
🔹
گل‌گهر و چادرملو هنوز تمرینات خود را شروع نکرده‌اند.
🔹
پرسپولیسی‌ها چیزی را می‌دانستند که بقیه از آن اطلاع نداشتند…</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/443287" target="_blank">📅 22:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443286">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3c41e3b9a.mp4?token=e_UTvQxjclVgnqmopjQqXWJ-s3afOaLCGDBbBl4KXZt058rbJSOcf0VN3huwWDXm17YEpw17S7wiEyR2uuhzOrWUCTDGxHPmfYgYNmnYESoj9datJjZdx4SgxsW4qc3JVX-ITWGVVG-Or8byBxF_f_KAQaVboqQcCkZu9sAOTjsABFWqHO2UM7Z7eQSJx6D5UQuAg9gJJQ2Yer9y6xFeXxHttf_DHSt1YvUeWGKyFrnnDqaCns62Sams-DIb_xx_U52uBjkELASCxYXWSeok4gZZzC1F9H9CnkXUiKPgQqqZsEe9M7bzQKvCEFnXCF41_XtzH4xZU7CLyO6CYA14mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3c41e3b9a.mp4?token=e_UTvQxjclVgnqmopjQqXWJ-s3afOaLCGDBbBl4KXZt058rbJSOcf0VN3huwWDXm17YEpw17S7wiEyR2uuhzOrWUCTDGxHPmfYgYNmnYESoj9datJjZdx4SgxsW4qc3JVX-ITWGVVG-Or8byBxF_f_KAQaVboqQcCkZu9sAOTjsABFWqHO2UM7Z7eQSJx6D5UQuAg9gJJQ2Yer9y6xFeXxHttf_DHSt1YvUeWGKyFrnnDqaCns62Sams-DIb_xx_U52uBjkELASCxYXWSeok4gZZzC1F9H9CnkXUiKPgQqqZsEe9M7bzQKvCEFnXCF41_XtzH4xZU7CLyO6CYA14mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میثاقی: به‌زودی جلسه مهم کمیته استیناف برای یک سهمیه آسیایی برگزار می‌شود
🔹
پرسپولیسی‌ها خیلی محکم درحال تمرین هستند و به‌نظر چیزی را می‌دانند که بقیه از آن اطلاع ندارند. @Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/443286" target="_blank">📅 22:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443285">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa27036b6c.mp4?token=SekhbbJ1DUUZHNoaabYFDE0BiwJNk9eGEnGgpRSxjnFN4g2KongDtqLizWNgITsDBf7AEc8o01KydvsqhV0KomtU5-PMkIkjnzVaYhTOVZg0Bi7oEhQm71_9VrVYzKQhBaNfM2Lota6o3ELlptTxF2eGF5u-MUNmO-pSk_Z8uVGLhS2UTl1fOVNoQz07Qjdc4nkEogMAlAZg4mx3zvBMgQNFJC8BooMSXB8Y4k2-6Zy4xeMCkQGBYSzLVhYIHqaYTGzrLodx_UcdebgOerlYWSAItDlpDkHXT8QICHVh0YJhwvHHnBMriuQsCUB5ggqzVFskxqRYuR8VY9-FNOBc9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa27036b6c.mp4?token=SekhbbJ1DUUZHNoaabYFDE0BiwJNk9eGEnGgpRSxjnFN4g2KongDtqLizWNgITsDBf7AEc8o01KydvsqhV0KomtU5-PMkIkjnzVaYhTOVZg0Bi7oEhQm71_9VrVYzKQhBaNfM2Lota6o3ELlptTxF2eGF5u-MUNmO-pSk_Z8uVGLhS2UTl1fOVNoQz07Qjdc4nkEogMAlAZg4mx3zvBMgQNFJC8BooMSXB8Y4k2-6Zy4xeMCkQGBYSzLVhYIHqaYTGzrLodx_UcdebgOerlYWSAItDlpDkHXT8QICHVh0YJhwvHHnBMriuQsCUB5ggqzVFskxqRYuR8VY9-FNOBc9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میثاقی: به‌زودی جلسه مهم کمیته استیناف برای یک سهمیه آسیایی برگزار می‌شود
🔹
پرسپولیسی‌ها خیلی محکم درحال تمرین هستند و به‌نظر چیزی را می‌دانند که بقیه از آن اطلاع ندارند.
@Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/443285" target="_blank">📅 22:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443284">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cbc790f95.mp4?token=c1uue161fhTpWgcadC9KSSj1_EfacljbOc76Rng5BZnsJ5wvwHS6LcJQ_SAi-kiRZpbSxovC0w-mnvSAVgPPkeeCMujd4e1Kkb6vHQhJCaQYDvcxo1XlYj5_HvtoiELjeB8TY_4qC3AQdrtA7qd2z8LRqdRxzzbkY6q7ddYxmsnmPvKq5dmcVbVQrOcCji3vLSzUXTEzFTQOXPTmquN4SoGdxbQPTg8KkIWIUXdTwmUC09H3hENksnueCPSoC9Kg14Txftt3P2HxIM-OpoAZBWp2O7P_xz2pjEO63fFWPwZrUNVpQQldJZJYDu-7z3ahin1kfVYo3Sk-dL3U504TsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cbc790f95.mp4?token=c1uue161fhTpWgcadC9KSSj1_EfacljbOc76Rng5BZnsJ5wvwHS6LcJQ_SAi-kiRZpbSxovC0w-mnvSAVgPPkeeCMujd4e1Kkb6vHQhJCaQYDvcxo1XlYj5_HvtoiELjeB8TY_4qC3AQdrtA7qd2z8LRqdRxzzbkY6q7ddYxmsnmPvKq5dmcVbVQrOcCji3vLSzUXTEzFTQOXPTmquN4SoGdxbQPTg8KkIWIUXdTwmUC09H3hENksnueCPSoC9Kg14Txftt3P2HxIM-OpoAZBWp2O7P_xz2pjEO63fFWPwZrUNVpQQldJZJYDu-7z3ahin1kfVYo3Sk-dL3U504TsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: من از رئیس‌جمهور چین خواهش کردم و گفتم واقعاً ممنون می‌شوم خودتان را درگیر ماجرای ایران نکنید
🔹
او می‌توانست وارد این موضوع شود. او می‌توانست یک نفت‌کش بزرگ را به همراه دوازده ناوشکن به منطقه بفرستد تا ببیند آیا می‌تواند با درگیری، راه خود را از میان…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/443284" target="_blank">📅 22:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443283">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار و تیراندازی در شهر مهران
🔹
فرمانداری مهران: به دلیل تمرینات رزمی یکی از یگان‌های نظامی در حاشیه شهر، فردا از ساعت ۶ صبح تا پیش از ظهر احتمال شنیده‌شدن صدای انفجار و یا تیراندازی وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/443283" target="_blank">📅 22:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443282">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d53ccdde.mp4?token=fXJpoxKEtSQk0tApyVv71N3zZMFoCgbwtJSLO12WPhqetKYvAepmfldD8QTbgAJbuA4rrUfs3JU9ZysPVbuGCi1O3wMQxl5MgS9dDR-HP6y8seFYTQFUxXjONv1NThJbSJSjOEe_-cvT4-sfNG4e1aldc8xpS5MSKIx338t2DLrR4JE37tSwvl60N2BD07mxmXwc1gHj8OOrZrG1a3hfFSMfpcToKinmjIIPrH60mDRBcLB0duub0j9ahVI253xykikF9lpqkGnVuMIfHKTv82Sz-G9JnYX2fy1crVbNOVr0zcW26W3JCyz3h8wfz3akIHpXQXt-7NSBFoneiAfAtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d53ccdde.mp4?token=fXJpoxKEtSQk0tApyVv71N3zZMFoCgbwtJSLO12WPhqetKYvAepmfldD8QTbgAJbuA4rrUfs3JU9ZysPVbuGCi1O3wMQxl5MgS9dDR-HP6y8seFYTQFUxXjONv1NThJbSJSjOEe_-cvT4-sfNG4e1aldc8xpS5MSKIx338t2DLrR4JE37tSwvl60N2BD07mxmXwc1gHj8OOrZrG1a3hfFSMfpcToKinmjIIPrH60mDRBcLB0duub0j9ahVI253xykikF9lpqkGnVuMIfHKTv82Sz-G9JnYX2fy1crVbNOVr0zcW26W3JCyz3h8wfz3akIHpXQXt-7NSBFoneiAfAtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: وقتی جنگ شروع شد، فکر می‌کنم بزرگ‌ترین غافلگیری برای من این بود که تقریباً بلافاصله، موشک‌های ایران به‌سمت قطر، عربستان، امارات، کویت و بحرین دیگر شلیک شدند
🔹
آن ۵ کشور مستقیماً به‌سمت من آمدند و با من همراه شدند. آن‌ها فوق‌العاده بودند. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/443282" target="_blank">📅 22:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443281">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3679be7cc8.mp4?token=vwQRqKJvpUX0o5a_WQi3dhEWi9t2D7ktGfzwk9i4CwsiepQlXFCVHM3cWQgi6lOf7DzOz0_3Q68NqwzsMbLEvbuHdEyqrJMmd9-WpYvSyqOez2RMLbXf3WLR5YgBGBKmdRCCr5IZgCu6evfIeB7G5FWUjR3_-aayfRz2rlyXPmlfnffxpWq2DcL38iQl83BgKGmLBy5Cj7gBDNeEFZ0ICr92TTX6ZoL339nyjsZB3WmxWtbvMP5J4pryP1wCcP38_8Y0sOiMqD34HywlzpOwWDhRs5u0mPJs5mlvKHA5hgbsl_OadWFrarXPt_Hs-Y0-RGNJuwyzTv_RuA-50fvhrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3679be7cc8.mp4?token=vwQRqKJvpUX0o5a_WQi3dhEWi9t2D7ktGfzwk9i4CwsiepQlXFCVHM3cWQgi6lOf7DzOz0_3Q68NqwzsMbLEvbuHdEyqrJMmd9-WpYvSyqOez2RMLbXf3WLR5YgBGBKmdRCCr5IZgCu6evfIeB7G5FWUjR3_-aayfRz2rlyXPmlfnffxpWq2DcL38iQl83BgKGmLBy5Cj7gBDNeEFZ0ICr92TTX6ZoL339nyjsZB3WmxWtbvMP5J4pryP1wCcP38_8Y0sOiMqD34HywlzpOwWDhRs5u0mPJs5mlvKHA5hgbsl_OadWFrarXPt_Hs-Y0-RGNJuwyzTv_RuA-50fvhrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: اگر من نبودم اسرائیل نابود و تارومار شده بود
🔹
نتانیاهو همکاری خوبی با من دارد، اما خودش به شما خواهد گفت که تسلیحات اصلی در دست ماست، تمام توافق در اختیار ماست و بمب‌افکن‌های بی-۲ و دیگر تجهیزات متعلق به ما هستند.
🔸
مجری: آیا می‌توانید مانع حملهٔ…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/443281" target="_blank">📅 21:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443280">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0df62eb34e.mp4?token=jVlc_zXKkB0TPvMSNTONfUHOZskSvlawGpbUPTKnv6XStQ1WIrzX2-SC0tVThr2q88X-dQuUBuN79G5HNd_N0hpxxh6ttgJ1Uik6GCYcE17NtUyjkWMAZipbg3_iCFQQmUoyGQ22GkbM0IbyRn26UcwWeh9jN7scvst7EbDdzJDFMa9esPhUc6QGGCdSJFJhCgliVEvQBjBLab7DI04fahjGlAaBc2C6FcUQK9Qu3ADFOH7qyn2kSl24_I4tkA8DCnl8zujanzae6f_0_zrhFGuIhm8sHX6xj-GXWoN9wigwI9QW0Ah5hiKkSELB8S6TyB5hk-NIMk6OYmpEt7nOsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0df62eb34e.mp4?token=jVlc_zXKkB0TPvMSNTONfUHOZskSvlawGpbUPTKnv6XStQ1WIrzX2-SC0tVThr2q88X-dQuUBuN79G5HNd_N0hpxxh6ttgJ1Uik6GCYcE17NtUyjkWMAZipbg3_iCFQQmUoyGQ22GkbM0IbyRn26UcwWeh9jN7scvst7EbDdzJDFMa9esPhUc6QGGCdSJFJhCgliVEvQBjBLab7DI04fahjGlAaBc2C6FcUQK9Qu3ADFOH7qyn2kSl24_I4tkA8DCnl8zujanzae6f_0_zrhFGuIhm8sHX6xj-GXWoN9wigwI9QW0Ah5hiKkSELB8S6TyB5hk-NIMk6OYmpEt7nOsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تماس تلفنی ترامپ و مقام صهیونیست درباره لبنان
🔹
رئیس‌جمهور آمریکا، در گفت‌وگو با شبکه ان‌بی‌سی از تماس تلفنی با مقام‌های اسرائیلی درباره تحولات لبنان خبر داد و مدعی شد که از تل‌آویو خواسته است توافق آتش‌بس با حزب‌الله را بپذیرد.
🔹
رژیم صهیونیستی امروز نیز…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/443280" target="_blank">📅 21:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443279">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f7f57be1d.mp4?token=YokmVCFkLdIE7swSUp6XunpkGJHmhFgKGE45UwD2nJ7KeQw4fq_rFD5NYdusGvKjBuTbhmH14WDdVpuYmowrFk9E0fd9UbImXU7Fwq3TMp1svQOT4AACIpFDm41IrAbBPtqfll1d-g55WWsshT9ul1AJwl1GUVGyr48FGT_VLsTZ1aFtauydaBavxn3_3ywGaAHdTTJmUbvsyxTr0Uu6L_7QClInVh2F66BQRowzCPFJwFN5eDWXGtVmTzG-aRFWPMTrl2M6tlKt7nhTALTyw6Jp1QDQZYSvHCnSCZSZ2IVds83HxawA3AxjLpskdSpc0K4-R8meHXnaIopkrNXnpIPm-rP7P7TfmEgUKM3sLMAeNSpBuWQ3D-2hpOdYQ8onri4ZpBN0T5pwM5s7jsCvbRnaMqz0FsfBDvWSKoZpqYJvEY6ZLSU6TabcobEepC6L6RUtpL3CHz4oZ40kBsvAM93XoN9nRQRAPUTdMCh6PA3PrRk44RPBB3NxbEZLHxC599EHUoxP3n9h30rcSgVDMIeZmJ3bbtQ4hHI-dYkK7Xhg31z2mrbe3JFFinnF1c0xgzldNEiTIQjqn7ELheqgM5Q-I8jXeJY2Pb_54thSm3Bwr1AeDD-r5X4IG78T4PbXToAbF_Qc1XYFnR7QaHtQ7CN1_Kbld_QiJb2KfHplgek" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f7f57be1d.mp4?token=YokmVCFkLdIE7swSUp6XunpkGJHmhFgKGE45UwD2nJ7KeQw4fq_rFD5NYdusGvKjBuTbhmH14WDdVpuYmowrFk9E0fd9UbImXU7Fwq3TMp1svQOT4AACIpFDm41IrAbBPtqfll1d-g55WWsshT9ul1AJwl1GUVGyr48FGT_VLsTZ1aFtauydaBavxn3_3ywGaAHdTTJmUbvsyxTr0Uu6L_7QClInVh2F66BQRowzCPFJwFN5eDWXGtVmTzG-aRFWPMTrl2M6tlKt7nhTALTyw6Jp1QDQZYSvHCnSCZSZ2IVds83HxawA3AxjLpskdSpc0K4-R8meHXnaIopkrNXnpIPm-rP7P7TfmEgUKM3sLMAeNSpBuWQ3D-2hpOdYQ8onri4ZpBN0T5pwM5s7jsCvbRnaMqz0FsfBDvWSKoZpqYJvEY6ZLSU6TabcobEepC6L6RUtpL3CHz4oZ40kBsvAM93XoN9nRQRAPUTdMCh6PA3PrRk44RPBB3NxbEZLHxC599EHUoxP3n9h30rcSgVDMIeZmJ3bbtQ4hHI-dYkK7Xhg31z2mrbe3JFFinnF1c0xgzldNEiTIQjqn7ELheqgM5Q-I8jXeJY2Pb_54thSm3Bwr1AeDD-r5X4IG78T4PbXToAbF_Qc1XYFnR7QaHtQ7CN1_Kbld_QiJb2KfHplgek" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور مردم در میادین همچنان ادامه دارد
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443279" target="_blank">📅 21:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443278">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WI2L3QqAxIQNTXzofu77PxPuN7arn-P_qelkZC8tUGs2nSFWlqIFQFm2RfVNKhPc2uEOmx4dwiYOpVNU1bBr3gr3o_1CpGdCyRKHrIJWHxYGiE-gTgg5MUwveghirJddyO11m1fncxKhhnQneHs9FvPVF69-TEzzjDiyLWzyl48SOIICu-hAzvASvcjFM4-erT1wHLpgu8_4wsbVS7zCWvLka3E7N35CYoJsQWQ81qnBeLvEvBHBrKlalDFgvuKynCekEeD_7f8_d6IjNgVUp1uTnbUCJJjMMAF7ZBkzywGgWAIr_rQQrM2ynHVtWuStTsTxwafdhZXwKvDxyZp1FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار قاآنی: غزه هم طوفان دارد، اگر به خواست سیاستمدارانتان حرکت کنید گرفتار طوفان می‌شوید
🔹
وقتی گفتیم حزب‌الله مرصاد دارد توجه نکردید گرفتار شدید؛ یکصد نفر تلفات را چه کسی جواب می‌دهد؟
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/443278" target="_blank">📅 21:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443277">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80924e16e5.mp4?token=R8OuaqKVIYxqeO8PAbtMIeTnbZB7sQzzqqO2SmvfYFKDyBUaTG0-CHWTOdZVp0C5A1VRpx5ha2EEiBUpC_nEvvWQjhF6KvEin7W1Y99yLLqTtKW8Kta8D4ZVR5S-_GGszk_rXRXbqOxfNzkRWwelzndposa7TKzmDqh9R9W19rLvVnLseQxb28vUUNeCKtCSk_enlbe66wBk0D3Qrb4-P4_57VVGu5K3tO7xYiDT_m7Fk8mEk2bzIzFFIWc2xLIOlmQYh7UhqnabuLXIQNRiq9zQ93fxRgu-8oIUE2j396QdQNnFhKMj39560U8U2hwUAQHBirAR2S7I1nVoDBriZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80924e16e5.mp4?token=R8OuaqKVIYxqeO8PAbtMIeTnbZB7sQzzqqO2SmvfYFKDyBUaTG0-CHWTOdZVp0C5A1VRpx5ha2EEiBUpC_nEvvWQjhF6KvEin7W1Y99yLLqTtKW8Kta8D4ZVR5S-_GGszk_rXRXbqOxfNzkRWwelzndposa7TKzmDqh9R9W19rLvVnLseQxb28vUUNeCKtCSk_enlbe66wBk0D3Qrb4-P4_57VVGu5K3tO7xYiDT_m7Fk8mEk2bzIzFFIWc2xLIOlmQYh7UhqnabuLXIQNRiq9zQ93fxRgu-8oIUE2j396QdQNnFhKMj39560U8U2hwUAQHBirAR2S7I1nVoDBriZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انهدام یک تانک مرکاوا توسط پهپاد حزب‌الله
در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/443277" target="_blank">📅 21:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443276">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584dd0151a.mp4?token=Q-fdk5A9XMvwu8E0Xmna8nrqUiIyjL-ZUHRgXjdC3xTkX1n02rqOzdjwbIJZDHyQYiY-KtNqaYB4oBG1WMi14Am_J6PGdnZNFJGHBvZIWFvJDmpuL8F5HiWh9GbNlBlg2-1NafcXGdZKBuL7zaVOKcg2dDCIHOt_6CWOiKLRBFZQadLcMW0gb5n-0PVPY2EvMKrfbHtJbGALNIbnbwA_17beTAA2X1pruex3bBtGjQO5BDb6oHnvRtWlhLUfAjFtl8-BVDyXhrug6K1NPtjAnQpxw2CLMLSa33Pbiicswq-bncvGe3rcJk9uR2zITvZ2Ri2uOuNpTEZuFvcuAZXRHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584dd0151a.mp4?token=Q-fdk5A9XMvwu8E0Xmna8nrqUiIyjL-ZUHRgXjdC3xTkX1n02rqOzdjwbIJZDHyQYiY-KtNqaYB4oBG1WMi14Am_J6PGdnZNFJGHBvZIWFvJDmpuL8F5HiWh9GbNlBlg2-1NafcXGdZKBuL7zaVOKcg2dDCIHOt_6CWOiKLRBFZQadLcMW0gb5n-0PVPY2EvMKrfbHtJbGALNIbnbwA_17beTAA2X1pruex3bBtGjQO5BDb6oHnvRtWlhLUfAjFtl8-BVDyXhrug6K1NPtjAnQpxw2CLMLSa33Pbiicswq-bncvGe3rcJk9uR2zITvZ2Ri2uOuNpTEZuFvcuAZXRHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این صدای تپش قلب کیه؟
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/443276" target="_blank">📅 21:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443275">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANn8ynGfQmSTnQyBx8H_F6xkpso4VAq1OxudbV67kA257oJepZs8pY0tB3YXCGzBa6Yop1H1VxFrfVIHBnT6lIGSQTTE3DylWSx06Ex5-FxovXZTenYY6s2uIvrAB0BZDNfkhsOlQtiYFYZKw4zM1jbvFW18TtGoGw0WFhyecLLT1Ich-f0FT61UVa8SC0LTvqCdvKivMDvlL46rYgFevwnufC68WbOoLYRWFmxGHvMMdZJPuUzQYTEYx8RMs6Ph22tZAY6bXqL6rSxEgbV_Nt2TNux5gZyaVaTDiTdcp3sOYKZRbGlz78sqwDw6Rcvd1pDe4fXi6YJNVUn9JmwWVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ نتانیاهو همچنان از حمله به لبنان سخن می‌گوید
🔹
نخست‌وزیر رژیم صهیونیستی در شبکه ایکس می‌گوید طبق دستورات او ارتش اسرائیل ۱۵۰ هدف در لبنان را بمباران کرده است.
🔸
این پیام در حالی منتشر شده که رسانه‌ها ساعتی پیش مدعی شدند که رژیم صهیونیستی آتش‌بس در لبنان…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/443275" target="_blank">📅 21:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443274">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4063415f27.mp4?token=ij4JNWY9dDifGEn18kdJAYJBa4VVShShE4R4yB7QM4tgOZD-t3pZ3XB062XVxttSxqllPzgNKvBSivIpDPQz7c5ZHwuNHfglRUHDrCZsyEdkh_pze1nFZBPiDb-YKyQL7dtFn_k82xhlXOdveT1MJM-PsooxjGvcd45kv2x1I0FQuype9XRw8ZnWS4YRPKH5tgkUYr2Zqw_itHPhJdIzvvcyCHH8AHbwVg-a4_KfNknIwk0MknBHYYE9M3_RjIHFEeGE-dyy7K6MbaCLEwxgTg7-QrQ4VK2l9aBCSlk65qzIV9bU8lDlbByKhUC019y1HmQSgw_p9bgmVqW4VmSALYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4063415f27.mp4?token=ij4JNWY9dDifGEn18kdJAYJBa4VVShShE4R4yB7QM4tgOZD-t3pZ3XB062XVxttSxqllPzgNKvBSivIpDPQz7c5ZHwuNHfglRUHDrCZsyEdkh_pze1nFZBPiDb-YKyQL7dtFn_k82xhlXOdveT1MJM-PsooxjGvcd45kv2x1I0FQuype9XRw8ZnWS4YRPKH5tgkUYr2Zqw_itHPhJdIzvvcyCHH8AHbwVg-a4_KfNknIwk0MknBHYYE9M3_RjIHFEeGE-dyy7K6MbaCLEwxgTg7-QrQ4VK2l9aBCSlk65qzIV9bU8lDlbByKhUC019y1HmQSgw_p9bgmVqW4VmSALYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نظم بی‌نظیر و شورانگیز عزاداری یزدی‌ها در حسینیه معلی شبکه سه
@Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/443274" target="_blank">📅 21:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443269">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی</div>
  <div class="tg-doc-extra">حجت‌الاسلام کاشانی</div>
</div>
<a href="https://t.me/farsna/443269" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
#حسینیه_فارس
| شب پنجم محرم
سایر مداحی‌های امشب را
اینجا
گوش کنید.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/443269" target="_blank">📅 21:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443268">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/443268" target="_blank">📅 21:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443267">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/869e161982.mp4?token=aC7g0BKkDMOQX2NmiKqpI7iXoOs1T8o86miy2IzyX2_WNoVO4wTxuVSTEqefPvVhFE1W3Tutm2RFsADEM5ntCaNyVzvkHRYFewYwnHo4jt1d14tUR1o1oArZIGFLiQKWQQr9TR697PAWBaC2Zl6-SShm4XI-h6pXkAqwEGzVxt3cL46GpHDvO-DS0akjL1UkBu3Q0lvT1l3L5t_AjnuCliQbOlGb9HKej-1My39_jxMvL1js1nTJgv1U7_0ql_RXCUrL9KqfVjCcN_OEx7Tm7a7O8IMNPYqWyJLz9ZRNz2OlhYIgfdjXolaUXuqa3UoQ22VxLlHB8nTz4f8lm7K7Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/869e161982.mp4?token=aC7g0BKkDMOQX2NmiKqpI7iXoOs1T8o86miy2IzyX2_WNoVO4wTxuVSTEqefPvVhFE1W3Tutm2RFsADEM5ntCaNyVzvkHRYFewYwnHo4jt1d14tUR1o1oArZIGFLiQKWQQr9TR697PAWBaC2Zl6-SShm4XI-h6pXkAqwEGzVxt3cL46GpHDvO-DS0akjL1UkBu3Q0lvT1l3L5t_AjnuCliQbOlGb9HKej-1My39_jxMvL1js1nTJgv1U7_0ql_RXCUrL9KqfVjCcN_OEx7Tm7a7O8IMNPYqWyJLz9ZRNz2OlhYIgfdjXolaUXuqa3UoQ22VxLlHB8nTz4f8lm7K7Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سازمان راهداری: مالکان ناوگان حمل‌ونقل کالا و مسافر می‌توانند تا سقف ۲۰۰ میلیون تومان وام خرید لاستیک بگیرند
🔹
همچنین ناوگان فعال در حمل‌ونقل کالاهای اساسی روغن موتور رایگان می‌گیرند.
@Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/443267" target="_blank">📅 20:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443262">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cMtxkxLgO88lza_voZNNLGjgEIMGv-ysbtJeZOQTrDoz15Z3a1zhHuUeqzE7Rgd88HG8CdWjAAWMY58Ftv_ZEf2Ie34q7cwo4Tsaw0XY884WsYnMtMIfRlVI1XUr5VcFxS9-ImooNSO6-1hjVq7Y0ByhuIgSa7bX3AqsPihcqvDrihx96K_UGndpJobqnWPe9N7eK-kC8xHbXv0RMBRjKqGddzsp4EyBK702QqLgp0rRZPP_t667LaXp26ef6NzexkqZUxQRLmP8Q80LqlzK49ff4wjc4pXlbQi4YV1ak9Oa3LFrCn2sU_xUdGM2R2JIWOITjXnAWMLdZ-If8PPp1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MCadlgMGjevU3MrGCMsqjy5bmJZ1bygAjni9nurq9pGNvObHUxA6QVPcW6tuKHdXioCwqvsGkWAB0AVHbF34qbqOcjlT96Q23yBWnVrnegjUBVM-gDJvbolc7MgmyywlIDSa9p9QOg1DJOuJdJQL689YD9BzrXQQs6rInxpnYqLf9NaZJQXxyU4qMjY31XFfCBQJakzIH20c1shfEH2qzjpLYlubZ4frMmpcHb4Di3ti_5s050UeGXrkcRtDsS1a3IqrxqL67toSoYX1qvNf-cnfEOq0kK6OwvbNJ3CsBQ-lzkeqi2mQkRwcmq1h_8tn1o7Wh9hC0cujG3QHSCHfNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fMO8QD7KNhjREVxvdk6jcwObKi4O7bm32MXL7h7xmK_QUFah0d_x_v-QI6SsTMdHEL4cmHJAhGhMatTzxbdOi292VdoYeTJNaQM4YHOXPJCDvtKXrwGXgDFGwRgc8i62j07tD6EuA5Tt8vuEz8VDjOEhXf-KURfACsfiJJKsd_XjX5exU7IBLneK8EQV5TvbG4alErNyXdROX-zVKVQw3vYX4YwP-62fiovzT3ZnegkKSM3eVzWsUiw56rRmPjdrAoJgwloyuBdsA0jiFN3TsWk3n85MNHqwhYcyGujUv1Yyisy_w8pw-MAVE69G14tyB_2VrEbduW4fP2AB0d8KKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kdPEDg3WQDSqahkvfRWESXQD8w2prKk0FHyoHE2ZJzjrLufC8-m4AcztF4Us8j0eHH22h9jMzlBIMsHlsB376zixojuSQBAmVOtA0Pc_hI7JA5Mq2iQjvevWhwZg1rpwFxRntUZSBeVy2QD6kzLg2JwLxSh2RcMuVzM_8SfkrXGkvKw2PXwrAnTZ9FuDCrOIAzIWIg1Cs41ww4z5Yxsri7JFHdhn2Bfc6KccMcNA-_9zmIndepRMf8H7tfuAamZ6x3zI_cW93bT66ZBe-iQYYnRapb-t_1lzRU63JSRHMDAqgZcpmv2wGaSMrNG8xwZ0kxTvbJC6URp4RappzYWyaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hegVOmGpDVuLe_4O95iOmB0uDoxIHk-fXQIVhMa7q_wTDMKhKxij2SNoFFMvR-pBQNBru4K1NHM7GHt6J37p4jU4Oe8wvv9uV0vmbUDIEHIUvBtE52hhBOR685tdEKnErqAUYLOYvUz8fTJLCaLW0xG2tzcZ6F2VO3NaybqIQIGENKusl-CAJympYqsF4DQE1yzsAO7pDHLOyzm9EYkKMFC6VWWJ6WY5Ixegd5QuiFp-F0QVmMBPqo51FUj8y70B3I4xnKbP_BguF8pREkD-5oKR-N-_I-WQUEt_jOSkA7WX2O-mb-h4rD8lGfS-WBYWRaAIc_EZSRVwshEzKaVLqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری روز چهارم محرم زنجانی‌ها در خیابان‌
عکس:
عرفان تقی‌بیگلو
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443262" target="_blank">📅 20:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443261">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b72671eb73.mp4?token=abt9ShneZFL309sh03D29Nk6pILl9FVxp4QFfkIl4e0_YX1M3IEtyDf8RfkjHN6VElh_uKbFsvH_S5P1Tuirnb4s9Fa0ZlqEsIgV_j50ESD0tqRashVO_ugVCLo07TEMRV86Srp7FaYrfuOEWxUVTCYcGmQoUKOjCQd2rUypxROsMS3qUmsc5h8tab732zRGVU2pfy1JZsZVLI5GbH2CPYHwiz0VNOJQkkjjK4z1jgQ8VGhGvZlmomVgMatqv10t12A5SYbvbdR94kjg0av46qTuag5eNkr6SrNfNGEBipB8bfyVnmeqdfXNKeGF_11vuZU4qGR9aZaU2AlDQvz13Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b72671eb73.mp4?token=abt9ShneZFL309sh03D29Nk6pILl9FVxp4QFfkIl4e0_YX1M3IEtyDf8RfkjHN6VElh_uKbFsvH_S5P1Tuirnb4s9Fa0ZlqEsIgV_j50ESD0tqRashVO_ugVCLo07TEMRV86Srp7FaYrfuOEWxUVTCYcGmQoUKOjCQd2rUypxROsMS3qUmsc5h8tab732zRGVU2pfy1JZsZVLI5GbH2CPYHwiz0VNOJQkkjjK4z1jgQ8VGhGvZlmomVgMatqv10t12A5SYbvbdR94kjg0av46qTuag5eNkr6SrNfNGEBipB8bfyVnmeqdfXNKeGF_11vuZU4qGR9aZaU2AlDQvz13Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی در جنگل‌های ایالت واشنگتن
🔹
رسانه‌های آمریکایی از آتش‌سوزی گسترده در جنگل‌های شهرستان اسپوکن ایالت واشنگتن آمریکا خبر می‌دهند.
🔹
مقامات اعلام کردند که این آتش‌سوزی تلفات جانی داشته و چندین خانه نیز دچار حریق و تخریب شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/443261" target="_blank">📅 20:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443260">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ee2bb640.mp4?token=fAoPvSi6dcBB7X65mpFz-fjE_XTZSzYFlYD6gel9ABRR5oWHGcizVJGEnYHziwTvzGR0-s5sWeTOqEzB-rV7c5G0abQDLe2uIOWaGFQx-lGuVuN73sC2N6WC7_GkL-8lbrgVMCfuGe_-yV2Mg89-eRC5LXkT-XZ0xHSJ2Y1F2SLtQM91MIpL4PxE0P7fr4Lo0jB6c5BAyDVos3246nuosseqJsXo3e1-SPowqNjW7_Fbsqi1JKdroQzESXNc5f14xb-FdOmbARHHBgYh57T6-tYPWAosH1pr3jjAl8YfLUSO9AozAvSdwtmZIk_RMr2sFAYdvhCuVXycDuYS-419EkwW4TWexg2eB-f4WI8ZfB9vHjA3QVsq_4CSOhxuAfgWmVShXYg56b-SFue92H1-C8Ud10TffOLdoKqAFEbNCcHuC-gxtV2hiLnt8cetR9CnkdPODK7BKPUdhYEWo1eoWDjb5BlIEmdCZOBzURv-8qIK39Xag6nNpLTh0OQ_3jC0slZcoQzjc7hhmNxXZgl5g1n1IFnuUF57ZXxgdyocjCYHCyjJDgTxdtlaFzhITgBSTRbfG3qC_2zZ7wFpiWAMAXgARWj5qAS9-d_-Bj3nXHulQPuyn5k0hYbjHJMExdlO0Nia2b-mkYbr-5DE4wBYXNOYPmCIMNPMXbODcfLxGtI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ee2bb640.mp4?token=fAoPvSi6dcBB7X65mpFz-fjE_XTZSzYFlYD6gel9ABRR5oWHGcizVJGEnYHziwTvzGR0-s5sWeTOqEzB-rV7c5G0abQDLe2uIOWaGFQx-lGuVuN73sC2N6WC7_GkL-8lbrgVMCfuGe_-yV2Mg89-eRC5LXkT-XZ0xHSJ2Y1F2SLtQM91MIpL4PxE0P7fr4Lo0jB6c5BAyDVos3246nuosseqJsXo3e1-SPowqNjW7_Fbsqi1JKdroQzESXNc5f14xb-FdOmbARHHBgYh57T6-tYPWAosH1pr3jjAl8YfLUSO9AozAvSdwtmZIk_RMr2sFAYdvhCuVXycDuYS-419EkwW4TWexg2eB-f4WI8ZfB9vHjA3QVsq_4CSOhxuAfgWmVShXYg56b-SFue92H1-C8Ud10TffOLdoKqAFEbNCcHuC-gxtV2hiLnt8cetR9CnkdPODK7BKPUdhYEWo1eoWDjb5BlIEmdCZOBzURv-8qIK39Xag6nNpLTh0OQ_3jC0slZcoQzjc7hhmNxXZgl5g1n1IFnuUF57ZXxgdyocjCYHCyjJDgTxdtlaFzhITgBSTRbfG3qC_2zZ7wFpiWAMAXgARWj5qAS9-d_-Bj3nXHulQPuyn5k0hYbjHJMExdlO0Nia2b-mkYbr-5DE4wBYXNOYPmCIMNPMXbODcfLxGtI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجدید عهد شیرخوارگان با کوچک‌ترین سرباز کربلا در جمکران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/443260" target="_blank">📅 20:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443259">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pq1SJjUL0Ki22b5iszese2xt-fJx2OVegN-Z5wwf2Lpd3sWbZFlxT-CGcgdeGxuJCCZ51ynmMw4SIYCSx0Mxur6T7OhvzQRsSfb0qsra0WSdubnWdKXREyd9mYMMsDex2UGi6e7pdAjWCiwIYXmP5--yENdLmB3ZoY84TnTSEu9gG-2FWaAQfvMtlnbd_jAL3q7Pq8Tp4q4Xvjc23NiB6XIkgTkRQSdyVWK1_o6nGgA54sTo3iU9XVOKjHGKm3QzlUxf6ycfRderrzfRvZ3DuQnyKlNcpa4sYC72yppFhP0OhwK_1vqQiRN-s-N3svVvKaYqfxDiXBnI9cUNJCS47A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجۀ روسیه: مسکو احساس می‌کند که احتمال دارد آمریکا رویکرد خود را در قبال حل‌وفصل مناقشهٔ اوکراین تغییر دهد.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/443259" target="_blank">📅 20:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443258">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gi6U4qXqGwZQIcVIbB1kZ9qZQSe-AvBj7iO6VOyki-OTeFtv5vHKjvAOAxTNvxlTZgptVko0vNiyjSlLANS0oxAl9Kf4EUznmE-XJ7AWezke6eFc_07ILuuAreYnngqWvHhpQAQPKQBim7GqsQwHS2v7ARPJfQb2QOk18D6ncgRD9fTp7Gl-mPkn5m1aUTrZv5lUZjFdf2PuTo4dF85GTS1ts-cspAusDHXeMf_od8kHyvwCbupEakeLAiGfeyH1V98HA3Y2q7w5qyZX_BpLB3STfvOM9JIHzXBCP6VRPl7Eb6alYdUMwuoJLulJctKIE8ZFkXh9EXNW6Kc9oL7SVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی بلاروس را تهدید به حمله کرد
🔹
رئیس‌جمهور اوکراین: «در امتداد مرزهای اوکراین و بلاروس تجهیزاتی مستقر شده که آتش حملات روسیه را علیه اوکراین هدایت و تنظیم می‌کند.
🔹
من یک هفته به بلاروس زمان می‌دهم تا این تجهیزات را جمع‌آوری کند؛ درغیراین صورت، خودمان این کار را انجام خواهیم داد.»
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/443258" target="_blank">📅 19:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443257">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🎥
ماجرای شهادت حضرت عبدالله بن حسن به روایت رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/443257" target="_blank">📅 19:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443256">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: ما تصمیمی کربلایی گرفته‌ایم که هیچ سقف و محدودیتی نمی‌شناسد و این تصمیم کربلایی همچنان با قدرت پابرجاست. @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/443256" target="_blank">📅 19:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443255">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: تجاوز و تعدی اسرائیل کاملاً آشکار است؛ پس چرا نباید با آن جنگید؟
🔹
یک چتر حمایتی بین‌المللی و عربی از سوی برخی کشورها وجود دارد که با عناوین و شیوه‌های گوناگون، تمام‌قد به سود اسرائیل و علیه مقاومت فشار می‌آورد.
🔹
آمریکا رهبری این ارکستر…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/443255" target="_blank">📅 19:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443254">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: مرگی که دشمن از آن به عنوان یک سلاح برای تهدید ما استفاده می‌کند، [در برابر ما] کارایی یک سلاح را ندارد
🔹
حتی اگر از ما به خاطر وجود تهدید به مرگ کسی باقی نماند، بازهم ما تکلیف خود را انجام می‌دهیم و در نتیجه از مرگ باکی نداریم.
🔹
دشمن…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/443254" target="_blank">📅 19:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443253">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: طرح و نقشه‌ای که امروز علیه ما درحال اجراست، هدفش نابودی کامل مقاومت و مردم همراه آن، و ریشه‌کن کردنِ حضور آن در لبنان است.
🔹
ما درحال عبور از خطرناک‌ترین مرحله در لبنان، خطرناک‌ترین طرح توطئه و هولناک‌ترین چیزی هستیم که آینده میهنمان…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/443253" target="_blank">📅 19:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443252">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: هرگاه دشمن با سلاح با ما روبه‌رو شود، ما نیز با سلاح با او روبه‌رو می‌شویم
🔹
تحمل خسارت‌های سنگین، بسیار آسان‌تر و کمتر از تسلیم شدن و شکست خوردن است.
🔹
ما مردمی هستیم که از مرگ هراسی نداریم و در مواجهه با هرکسی که ما را به مرگ تهدید کند،…</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/443252" target="_blank">📅 19:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443251">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb35598b8f.mp4?token=kkOFJUn7I5tdzAyXVHowxiEV7iFSEb1GKP7Pvdy6Dfsihr2h5KZ9uvQMCwwoQqWrk09vB9N1QDsQBVhylXl2xLZpLlXrEJ3edvma22vqO_W-Tfmdoe51JSBDe_kImJcBFZiRuAyYNXgcIQXSJcPpMXISqoMEZ7Ii5UXgGWdMhwhZeJT600MEGCxz09CECOI-DjK1q7DBMdGXJUf2Qwkq271aU7cfacCVFPQh9FwnVRQIrJrm9ETLTw6ba9pNfVe90AB54WM_bsBlkBSV1sA3EZL2oE3wES3qdvkmGRZgaNCqpJ0Jp5l6Sy58W9aMhhJ8KOYNQL4v8_k6DVJMxxZCMjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb35598b8f.mp4?token=kkOFJUn7I5tdzAyXVHowxiEV7iFSEb1GKP7Pvdy6Dfsihr2h5KZ9uvQMCwwoQqWrk09vB9N1QDsQBVhylXl2xLZpLlXrEJ3edvma22vqO_W-Tfmdoe51JSBDe_kImJcBFZiRuAyYNXgcIQXSJcPpMXISqoMEZ7Ii5UXgGWdMhwhZeJT600MEGCxz09CECOI-DjK1q7DBMdGXJUf2Qwkq271aU7cfacCVFPQh9FwnVRQIrJrm9ETLTw6ba9pNfVe90AB54WM_bsBlkBSV1sA3EZL2oE3wES3qdvkmGRZgaNCqpJ0Jp5l6Sy58W9aMhhJ8KOYNQL4v8_k6DVJMxxZCMjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اسیدپاشی روی صورت بازیکن کنگو
🔹
جیمی‌جامپ هر روز به نادانسته‌هایی از جام جهانی فوتبال می‌پردازد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/443251" target="_blank">📅 19:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443250">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: هرگاه دشمن با سلاح با ما روبه‌رو شود، ما نیز با سلاح با او روبه‌رو می‌شویم
🔹
تحمل خسارت‌های سنگین، بسیار آسان‌تر و کمتر از تسلیم شدن و شکست خوردن است.
🔹
ما مردمی هستیم که از مرگ هراسی نداریم و در مواجهه با هرکسی که ما را به مرگ تهدید کند، همواره پیروزیم.
🔹
هر گامی که در آن با اشغالگری مخالفت و مبارزه کنیم، برای ما یک پیروزی محسوب می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/443250" target="_blank">📅 19:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443249">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌ نتانیاهو همچنان از حمله به لبنان سخن می‌گوید
🔹
نخست‌وزیر رژیم صهیونیستی در شبکه ایکس می‌گوید طبق دستورات او ارتش اسرائیل ۱۵۰ هدف در لبنان را بمباران کرده است.
🔸
این پیام در حالی منتشر شده که رسانه‌ها ساعتی پیش مدعی شدند که رژیم صهیونیستی آتش‌بس در لبنان…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/443249" target="_blank">📅 19:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443248">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f499c8d6.mp4?token=gQaz6jjvy1LksdZ-cNZxK_VTy38fnffWYQMxECVvQ9yYJdV7voJ5e_j4jWAIdOlaFqGh7Ys-12bMsDCpZH7oM7yXY2zlm-E4vLbvFLVj4znZK0SQPgjfxZ-fiAPRRRDmv1b3csHGH156HkqybDVMjhLispWQNMWie79eIkSTAihp8NPF6FppkW1N0HsxMzhPyUAUx1fmWprRayD2YtPOp3tHBhsGvH3uZd3Eh3SIQtcE5tfPRNGQPa0lvQ9I-OXtZkY7tkwq6CEq929qjsXaAujMeuNouvbSkn5TLm-jpqyssBWaypYN0h6FJd81pdQU045ixGXNydOAIMJMTg4EibF6yFfl0tBIC4YPvHRvvJQ3HK6n7WAJPsYL_jwjOPnZJuoqoOoyW3poro7OgkBkXt0uP1wY7gGj0hk2T_r8-0QREPSXLLWUb1FYdP7xAsTSRQnGd-rdAVpeYYoEkdoC0AEjKqVFICsQBe4BASgAGsl5ypjnhf_9goCnm-xU1jxiMY3DbU8egyNXS0TmSvDKNcPbcPvJ4naO04dQHaXpTmLWLLxS5u-1TzFfpnSHL0guDnTVU7AApNVpPxRn35n7dtnjrXuf6ywuAVhNWR5oszv0Aya19i5TkVbEKcmbr9VtLvFf0KulUldr66Do4Up76ef_3JlIwKO68aLni7hun08" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f499c8d6.mp4?token=gQaz6jjvy1LksdZ-cNZxK_VTy38fnffWYQMxECVvQ9yYJdV7voJ5e_j4jWAIdOlaFqGh7Ys-12bMsDCpZH7oM7yXY2zlm-E4vLbvFLVj4znZK0SQPgjfxZ-fiAPRRRDmv1b3csHGH156HkqybDVMjhLispWQNMWie79eIkSTAihp8NPF6FppkW1N0HsxMzhPyUAUx1fmWprRayD2YtPOp3tHBhsGvH3uZd3Eh3SIQtcE5tfPRNGQPa0lvQ9I-OXtZkY7tkwq6CEq929qjsXaAujMeuNouvbSkn5TLm-jpqyssBWaypYN0h6FJd81pdQU045ixGXNydOAIMJMTg4EibF6yFfl0tBIC4YPvHRvvJQ3HK6n7WAJPsYL_jwjOPnZJuoqoOoyW3poro7OgkBkXt0uP1wY7gGj0hk2T_r8-0QREPSXLLWUb1FYdP7xAsTSRQnGd-rdAVpeYYoEkdoC0AEjKqVFICsQBe4BASgAGsl5ypjnhf_9goCnm-xU1jxiMY3DbU8egyNXS0TmSvDKNcPbcPvJ4naO04dQHaXpTmLWLLxS5u-1TzFfpnSHL0guDnTVU7AApNVpPxRn35n7dtnjrXuf6ywuAVhNWR5oszv0Aya19i5TkVbEKcmbr9VtLvFf0KulUldr66Do4Up76ef_3JlIwKO68aLni7hun08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوزادانی که نذر یاری قیام حسین شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/443248" target="_blank">📅 19:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443247">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-text">صدای شکایت ایران در جام جهانی پیچید
🔹
فدراسیون ایران امروز با انتشار بیانیه‌ای از درخواست ورود به آمریکا ۲ روز قبل از بازی با بلژیک خبر داد که از سوی میزبان مورد موافقت واقع نشده و این عدم قبول درخواست باعث ایجاد مشکل در روند آماده‌سازی تیم شده و به‌خاطر این برخورد ناعادلانه به فیفا شکایت کرده است.
🔹
سایت فرانس ۲۴ نوشته ایران از محدودیت‌های سفر به آمریکا که باعث ایجاد مشکلاتی در آماده‌سازی شده به فیفا علیه میزبانی جام جهانی شکایت کرده است.
🔹
بی‌بی‌سی می‌نویسد که ایران از محدودیت‌هایی که دولت آمریکا در جام جهانی تحمیل کرده به فیفا شکایت کرد.
🔹
گاردین نوشته ایران بار دیگر میزبانی آمریکا در جام جهانی را به دلیل محدودیت‌های سفر برای بازی به چالش کشید.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/443247" target="_blank">📅 18:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443246">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euKBgozT3pp8Nqvwm-YLm_o4BCrwid90qep9eNS-9jbhlU2tnG6kvy2MLx1scPOa5jTtzFgO9WHyXS1Jl7N0wqFgJUANc8fwDt-lX6QHdmX65geRGDaFrubTLmBVVPcYQYxW5wjpY6llhrTd3rCo8-JBbz1Qp09FCpN61oGtYnSVWgdInRvr4k8MQL3Nvz26JvGdxRSuB5vssEFjmbAzs71fVOnC21vTYKocvis5PGCeb6kRLWFtBOR_71imRBtPs1lWYU78p3w22IKn-9HrNTP4z65UcdEPgC2CxmxByQwhY0QBcedU7ZKu0udpOp53oSR28--HIrzuGdNVUpI4NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترس بحران ذخایر نفت بر تن ترامپ
🔹
ذخایر نفت خام بزرگ‌ترین مرکز ذخیره‌سازی تجاری نفت آمریکا و جایی که قیمت نفت این کشور تعیین می‌شود، یعنی کوشینگِ اوکلاهما به ۲۰ میلیون بشکه رسیده که پایین‌ترین میزان در ۱۱ سال گذشته است.
🔹
بیشتر از یک ماه هست که مدیران شرکت‌های بزرگ نفتی آمریکا هشدار می‌دهد که اواخر خرداد تا اوایل تیر، ذخایر نفتی آمریکا به مرحله تنش عملیاتی می‌رسد یعنی دیگر توانایی جبران کمبود نفت را ندارند؛ ترامپ هم چهارشنبه گفت که اگر توافق نمی‌کردیم دیگر نمی‌توانستیم ذخایرمان را پر کنیم.
🔹
در این ۵ روزی که از اعلام تفاهم گذشته، ۱۸ میلیون نفت ایران به بازار وارد شده و دیروز ۶ میلیون نفت عربستان هم از تنگه هرمز خارج شده است.
🔹
حالا سفیر پیشین آمریکا در عربستان چاس فریمن می‌گوید، عقب‌نشینی ترامپ به خاطر به تمام شدن نفت ذخیره‌سازی‌شده‌ است که افزایش شدید قیمت نفت و بنزین در جایگاه‌های سوخت را به دنبال دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/443246" target="_blank">📅 18:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443245">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d3551b736.mp4?token=o4A3ibMSyRX00rP0f2ZvDIdHc00YXQzy2i1qTsp3gVXYxEOrZz0s_9yQ2X_eQY1Qnmd3cNY6vWUW9YJ44MSq-mW-NvllPiAAIH3-rLpzo1CY0iEqe7oI35VZmmGQuwSO4NXzkkeYhRHdweWHDZj06nBu6bg9hvgo0GA9rnW2sgg2vfk4oaYyH5-6-M-BDd3pwHtKSDciMCP0YKuJG-J6hAWBhgadDhh7oh_4oWbFyba1tWu6SLJ130nVxoVNEAhjMMarFhMwULjXrdegAWATyrbYxc6HWGcwGgZdRDfOK-NWecXdjvdZk81aPPZZ35pk_OPyDJWdv6IOA8KWUVZtdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d3551b736.mp4?token=o4A3ibMSyRX00rP0f2ZvDIdHc00YXQzy2i1qTsp3gVXYxEOrZz0s_9yQ2X_eQY1Qnmd3cNY6vWUW9YJ44MSq-mW-NvllPiAAIH3-rLpzo1CY0iEqe7oI35VZmmGQuwSO4NXzkkeYhRHdweWHDZj06nBu6bg9hvgo0GA9rnW2sgg2vfk4oaYyH5-6-M-BDd3pwHtKSDciMCP0YKuJG-J6hAWBhgadDhh7oh_4oWbFyba1tWu6SLJ130nVxoVNEAhjMMarFhMwULjXrdegAWATyrbYxc6HWGcwGgZdRDfOK-NWecXdjvdZk81aPPZZ35pk_OPyDJWdv6IOA8KWUVZtdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت عکسی که به اصرار ماکان گرفته شد
🔸
ماکان نصیری دانش‌آموز کلاس اولی مدرسهٔ میناب است که در حملهٔ آمریکا جاویدالاثر شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443245" target="_blank">📅 18:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443244">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
ادعای یدیعوت آحارانوت به نقل از یک مقام اسرائیلی: ما با آتش‌بس موافقت کردیم و اگر حزب‌الله حمله نکند، ما هم حمله نخواهیم کرد.
🔹
این در حالی است که حملات رژیم صهیونیستی به جنوب لبنان همچنان ادامه دارد.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/443244" target="_blank">📅 18:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443243">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ارتش: در صورت هرگونه بدعهدی دشمن با نثار جان از منافع ملت محافظت می‌کنیم
🔹
بیانیه ارتش جمهوری اسلامی ایران در خصوص تفاهم‌نامه ایران و آمریکا: در ایام پیروزی خون بر شمشیر  و اهتزاز پرچم عزت حسینی، بار دیگر ثمره مقاومت و صلابت ملت مبعوث شده ایران اسلامی در برابر یزیدیان زمان و جبهه‌ استکبار جهانی در جنگ تحمیلی اخیر متجلی شد.
🔹
ایستادگی جانانه‌ مردم ایران و ایثار و فداکاری نیروهای مسلح و دلسوزی دولت مردمی با تدابیر حکیمانه قائد شهید امت و هدایت رهبر عزیز و فرمانده معظم کل قوا در میدان جنگ تحمیلی سوم،  دشمن را ناگزیر به احترام به ملت بزرگ ایران ساخت تا مسیر آتش‌بس و تفاهم را در پیش گیرد.
🔹
فرزندان سرافراز ایران و فدائیان ملت در ارتش مقتدر جمهوری اسلامی و سپاه سرافراز پاسداران انقلاب اسلامی، دوشادوش یکدیگر و با هوشیاری تمام و چشمانی بیدار، دست بر ماشه و گوش‌ به فرمان فرماندهی معظم کل قوا، هر روز بر توان رزم خود خواهند افزود و آماده‌اند تا در صورت هرگونه بدعهدی دشمن، از امنیت، عزت و منافع ملت شریف ایران با نثار جان خود حراست و صیانت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/443243" target="_blank">📅 18:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443240">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۶۹.pdf</div>
  <div class="tg-doc-extra">3.2 MB</div>
</div>
<a href="https://t.me/farsna/443240" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-67.pdf</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/443240" target="_blank">📅 18:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443239">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXiT_Kf1gEkmnEjjfUmU_OPNUHGOfC0tWQm5oHpbBvhNa2OgC8zcEEgMBzx0OXWwPg1PF8B-1V2kZJGVNK7BCJE4fTmNsn48bPY0MGgRDW8UEtw2-ghdrsuf93NrkEDl5XyMyfp_oWDzcCWF7ls8xvuC-LZpgnC5annbnstwNIaEx4nvReBcuqb2kCUp2wpBOo2LRtWZN_ahct3OpGyb9V7aY3qfHRU6z3k0u5wJN54m2SUnnE3zcx8IuVs-0mJ-WKRpji3eKG5q9ENqTLHQ1W29u7EYd0HViyEfNbLY-qYsvyhPQs5oxHtMZ6_ju4RHsaCVdTzQ6tbRvBoG7hDg2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران پس از ۲۹ سال در جام جهانی بوکس‌ مدال گرفت
🔹
مهدی حبیبی‌نژاد با شکست نمایندۀ انگلیس در جام جهانی چین مدال برنز خود را قطعی کرد.
🔸
آخرین بار کورش مولایی‌ و ابراهیم موسوی ۲۹ سال پیش در جام جهانی چین موفق به کسب مدال برنز شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/443239" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443238">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">مقام حزب‌الله: هرگونه تحرک اسرائیل خارج از چارچوب آتش‌بس با پاسخ مواجه خواهد شد
🔹
یک مقام ارشد در حزب‌الله در گفت‌وگو با شبکه الجزیره تأکید کرد که هرگونه اقدام یا تحرک رژیم اسرائیل خارج از چارچوب آتش‌بس فراگیر، با واکنش و مقابله مواجه خواهد شد.
🔹
وی همچنین با اشاره به ادامه تنش‌ها در مرزهای لبنان گفت که اسرائیل همچنان به نقض توافق آتش‌بس ادامه می‌دهد و همان رویکردی را در پیش گرفته است که در توافق‌های پیشین نیز دنبال می‌کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/443238" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443237">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: بازرسی از تاسیساتی مانند بوشهر که تاکنون انجام می‌شد، ادامه می‌یابد. @Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/443237" target="_blank">📅 17:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443236">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: در طول دوره ۶۰ روزه مذاکرات، وضعیت فعلی برنامه هسته‌ای ایران حفظ خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/443236" target="_blank">📅 17:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443235">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه:‌ طبق بند ۸ سند تفاهم، مذاکره درباره موضوع هسته‌ای در بازه زمانی ۶۰ روزه انجام می‌شود و البته این امر مستلزم تحقق پیش‌زمینه‌های شروع مذاکرات وفق بند ۱۳ خواهد بود. @Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/443235" target="_blank">📅 17:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443234">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه:‌ برنامه‌ای برای بازرسی آژانس از تاسیسات هسته‌ای ایران نداریم
🔹
اخبار منتشره در برخی رسانه‌ها مبنی بر دعوت جمهوری اسلامی ایران از آژانس بین‌المللی انرژی اتمی برای بازرسی از تاسیسات هسته‌ای ایران کذب است. @Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/443234" target="_blank">📅 17:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443233">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه:‌
برنامه‌ای برای بازرسی آژانس از تاسیسات هسته‌ای ایران نداریم
🔹
اخبار منتشره در برخی رسانه‌ها مبنی بر دعوت جمهوری اسلامی ایران از آژانس بین‌المللی انرژی اتمی برای بازرسی از تاسیسات هسته‌ای ایران کذب است.
@Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/443233" target="_blank">📅 17:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443232">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه:‌ برخی گزارش‌های رسانه‌ای مبنی بر بسته‌شدن تنگه هرمز صحت ندارد
🔹
نیروهای مسلح جمهوری اسلامی ایران وفق يادداشت تفاهم خاتمه جنگ مورخ ۲۸ خرداد ۱۴۰۵ تدابیر لازم را برای اطمینان از تردد ایمن کشتی‌های تجاری از تنگه هرمز اتخاذ نموده‌اند و کشتیرانی در این مسیر درحال انجام است.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443232" target="_blank">📅 17:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443230">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: طبق متن یادداشت تفاهم، آغاز مذاکرات توافق نهایی منوط به شروع اجرای مفاد بندهای ۱، ۴، ۵، ۱۰ و ۱۱ یادداشت تفاهم و تداوم اجرای آن‌هاست. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443230" target="_blank">📅 17:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443229">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: رایزنی‌های لازم از طریق میانجی‌گرها درحال انجام است و در صورت فراهم‌شدن شرایط لازم برای شروع مذاکرات، اطلاع‌رسانی خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/443229" target="_blank">📅 17:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443228">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: نشست امروز جمعه در سوئیس، به روز دیگری موکول شد‌. @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/443228" target="_blank">📅 17:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443227">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">لغو مذاکرات نفت را گران کرد
🔹
درپی اعلام هیئت‌ مذاکره‌کنندهٔ ایران و وزارت خارجهٔ سوئیس مبنی‌بر لغو مذاکرات امروز ایران و آمریکا در ژنو، نفت برنت به ۸۰ دلار در هر بشکه افزایش یافت. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/443227" target="_blank">📅 17:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443220">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YRN8GA9uiNuqlz0oIRa_Z1t5Z-FSEWk1KROEtzga1V-gHwTo-_ti1trv3uOPimuj-yga48NCmuj7RT1HMG9qhtYdkTqLk0euF3Gd_VFBWecWKDVV_B_0zQHf4AE-fjlu3jMycqA5Km3bm6xgzW1JcHMG9YDRU65C7jGhd6YdDPNpZmaBQw8Pl-HmmG3Zib19jk13J6Ngpg_qGxqfqP0DTjgoIqFkFPBmjlaoCDjdlMDIvXUT3MqNgXDqzEARaWc8M13gXCDbkjhm_Tqr5EJBsl1jet6crswnc4xQKJmk5gKhynZpuhqc1W7QNpfnIp_mNSvutoe_Dg9KtCr9MgyRBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m_m9T1PsCBz_PhwgM38xboGUemFlk0gkNGn4oISCrhjZuVMS-nmRd1cBy5ULzLkXCbEr-2TTLGO6UHq4gEDnxJRSYhdMXiEpqV3r6HCe1hyXc7XhsX5_rXnxXSq2QO8GIZgXS_KpGlsFEH0uLnOeKEkAmIW2wrXViGwyuoTdi81ixWpUHxUbjhd9uav7_aST48wVmqqCj96HCYJ8Gml9A-NNpECGjc-8lLguhkbUqMl8heeKE1whvh7qCh6fFTxacJRf9vfvqQsLK4iynfXJwbFbG7LBC7Ih8WUAarewU9rpfhKnQcgxB7mcH_0BmbgJpQ6JwHEhbCaEsxLRcMCa-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SrJZHJeMSM4CmWDqca7IoAcHWsQ-tjVL-37zBi6GbMwHaGdxAE2BzOfTfr7P94_S-q0Dc8eC7g6fkKomgFWw1zn_VvhA01cfi69SVDTVjnJ2NIdM4VBSX7gBa9fxH_UQP5hy9kAC5dbuSzLUvOgBISaAExq7heyBeSz6_0W0L_lL6beEFjZgaZi4QYfnYNdHzOrUjfM8bZwyf0TxTiUZhMTV74cPgwfmbIVCOnrmahWFRH2g2OT4nh4u2r8r-d9P-Qy1z6nrgxc3WV7YI0CKpz2eY6VjVvKfowgiY_jndbiSjrFyXqcl2SxAKkIxypAn3cKM2Kf0-yd_xrIufPKfRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A4XE7AHLz2q4l6wZ8HES5x9Z_Jm3LQ8L3WihWmbNVYoylo8UHGnbpIhdXSf4k70VFYHebgOu6TIWyTASmjiXISJyoV2KOdZzGSQ3lIXnv1RaCjW2WjHYycdhSjrAm0VZ_X3xDdWsuHd0YUDFrsrM3zuOqm5p3uvfUJfT2OJDEb6orlkrkz0jZ2oMoGSCeAO9R7ZVLbXjorQjqAY6SW9-SLOHCIc5fXS-DPpy_4OsBlVcribmCRoqVVqe6OyAvpRhIp6Jqpsvc_CrQ2kqsm66Vkf8sINVPGjbvq_w2zh9fNIqcCeU-_0ns4wHQzRp8sVk5wEXxMkbWJ4NWkYV3-5_Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q3Ts7zkFYCCzHOFK_RSVQY-GrbrgqTyfZcuEnn9t8uoNb4S85VGQfmc9Wp3j9S0_4XfG1vvdgUjTxEdz8e9IPrt-UfiHSlfbH0qps6u6Ku6loTM-4a2Exfis8oqW4oYtHbyk_5IrK6NXaiObiiatoHv2hCRwSRRtKnIvKXBpZIqeaEuRpicND0ZOD6x7uBCsloGL6YAjjSlqhwORj8W89682_UZYdI3KQbhklXgTVB-jXHVKNF7qR7tBPms_9UN9O7phxr1a2_qhC-B1smVHuWtYNPG3w6F1hKSItImBDbijOma3sgIvzVJmDhfOVcLPT3vdXAAksQeJFnJ3mmeQ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dV_qR5IEYUjuc_UhItn1irKdTQp7ZLXpSpIiFhKf1mI-cKSRI3mbt61xQZYXGir4tg_s9d8cR8CC5i3Z4I3ULy4-K47uOITWsoRqPorEnhSI3jabm_bWPUN2Trp0egDirEL3HYSk1xbLLzxx5rFwMrAwbgvDyzhUe6SEnYkVb0qp8DGuI0ESufsV4qAArwhqjT17VM6E3Gowhy5-6aWp0Qtf3g0edPyRloTuWuDsgZMnkIs2LRuUyeJXtUitvBX6Gsfd-gSu9CouC4G672ax7XxIA6YvOBhXJ54POU4DzLEvM2WyeqNAFj13XnP37DHBrDa7KgIVDu24vSYynTmilA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RLBPcuya57gv4v9xwsBf1U-EP0tIPzh8WZfUfSI07gRt8ZJ5RHLnkHD8l-UKqh3JrnamHN5pe6YK1IykempkGHsBK620m77DW98KRS7UglpmQUJo3DCNKjqGM7ht9irfJ301M_iN8FWJIANuqnfrkB3DXg6gfpYDka5xzk9apQyeFUAu0IhGlhYWnBfkh_BuWHYJ98hx2QX17BPpA5wIO8uog71Sy8wuDxRSG0SvhalD-ury849kEmOaUejIG9v8TvOMyHXCIeJdlf1EEv41mFblfkVUq6UVJGuVSDhqvDeifzZUszcfawzT8HG30i0M7J-KsG0xvGfGmnROu5HCng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم شیرخوارگان حسینی در حرم حضرت عبدالعظیم(ع)
عکس :
احمد بلباسی
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/443220" target="_blank">📅 17:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443219">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔴
ادعای یدیعوت آحارانوت به نقل از یک مقام اسرائیلی: ما با آتش‌بس موافقت کردیم و اگر حزب‌الله حمله نکند، ما هم حمله نخواهیم کرد.
🔹
این در حالی است که حملات رژیم صهیونیستی به جنوب لبنان همچنان ادامه دارد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/443219" target="_blank">📅 17:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443218">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcS3tm_QjTyBcC815QFF75MkCnM8c2mg444cWT50AjN5twDpxRSmLLW9X2O-yqwIR7BuDqn86tOYJI2CW1xwtM3JSLGB2rK5JotCdlwVx77DCUvMaGDGq-hd3kb5mGoNv8dnAY8Pcpp9BuCcakqVJYRQBkxwIKXgy-H_hIb-FYKRviesl8kdLdTMFIbpKWTaVph9my5xdkKVgj1UOBs56M7xgxTNsJZq_-hDww0oZhVvoiYDWv3y0vfi_XF08Srr45k59wIhihG5603mJEFuEMbC03cQsi0ll9kkD2oHb8UvM2_tbgjlDpN-Q1bL2fn9loCkbtBRd7QlnvHAmIVFNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با توجه به تشدید حملات رژیم صهیونیستی به لبنان، ویژه‌برنامه «عزیز ایران» امروز ساعت۱۷:۳۰ با بررسی آخرین تحولات سیاسی و میدانی لبنان روی آنتن شبکه افق می‌رود.
@Farsna</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/443218" target="_blank">📅 17:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443217">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkFP3RJhyCFho9fGnksmpkMiJ5rFWrb6h00t3eSDk7bd8Z8uoaZWKCRHUxG5UPIAHBqQEcf_5rP00dvt7tuvEHgB_ufMhcBWCObf1os-pFLWuxV46Phop3eEHWBGOlhCxoRGOjGZn78_OxT-SyLtxnr1JBmKYWq6-uY8HI8fjFSMIi8spV-31XUkJkEdfBUO3LAgLijA3K4WOmEGXPvHLeytWVxozuocdQ7OwxdP1s_e25F3MHIJ9wIK4bxx5KhT2T9OcigN4Azo7eL6DXzrNOd3l3rq5ZnLngRh_sBCKofvn8LpRa72RjdYNFqO8z7ja3j6iveqMBruD4rwpW0ncQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/443217" target="_blank">📅 17:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443216">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/443216" target="_blank">📅 17:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443215">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اختلال در موبایل‌بانک و اینترنت‌بانک ۴ بانک ادامه دارد
🔹
شرکت ملی خدمات انفورماتیک دیشب از رفع اختلال خدمات مبتنی‌بر کارت ۴ بانک ملی، تجارت، صادرات و توسعه صادرات خبر داده بود.
🔹
بررسی‌های خبرنگار فارس و گزارش کاربران نشان می‌دهد در حال حاضر همچنان اختلال…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443215" target="_blank">📅 17:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443214">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
تصاویر منتشر شده از حمله هوایی رژیم صهیونیستی به شهر النبطیه که به گزارش برخی رسانه‌ها تنها پنج دقیقه بعد از اعلام آتش‌بس ادعایی صورت گرفته است.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/443214" target="_blank">📅 17:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443213">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhGiMRftoId8-l5IZeYidTwoMA73L8M15UObhMC-SReNNnn-dzeym2YGlJ1m9Nxr0yAtTSgpAcl7pwEG1zUOwIXBOMD0H2oR_PhwIU_cOmRcePcHaM8qR7kNHQxHfRibxZj36bP2v-_nSNykh7oxH1vlDHrSobXh2o8CWks05ahNglPH-NusVKv6Kwmk2FG9pZ0zolt_ZfI1sTgG6SahgIeJzcZ9qN-QJBIDPCbNnWNYvXMqfKgM5xyf1-yIMOgNlRoucFS9wQWe94dY55Nog8gkIFm9KxNXoEIIAXXubIB4pdZNflLRJcuFeokimee8X3kkLn0QFvYdvYYDmue5KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویر منتشر شده از حمله هوایی رژیم صهیونیستی به شهر النبطیه که به گزارش برخی رسانه‌ها تنها پنج دقیقه بعد از اعلام آتش‌بس ادعایی صورت گرفته است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/443213" target="_blank">📅 17:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443212">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‌
🔴
کانال ۱۲ رژیم صهیونیستی به نقل از یک مقام ارشد اسرائیلی: آتش‌بس به ما اجازه می‌دهد تا به تخریب زیرساخت‌ها و اقدام علیه تهدیدها ادامه دهیم. @Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/443212" target="_blank">📅 17:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443211">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‌
🔴
خبرنگار المیادین در جنوب لبنان از حملهٔ هوایی رژیم صهیونیستی به شهر النبطیه در جنوب لبنان همزمان با آغاز آتش‌بس ادعایی خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/443211" target="_blank">📅 16:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443210">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‌ مقام ارشد رژیم صهیونی: آنش‌بس میان اسرائیل و حزب‌الله برقرار است
🔹
یک مقام ارشد رژیم صهیونیستی در گفت‌وگو با شبکه ۱۳ تلویزیون این رژیم: درحال‌حاضر آتش‌بس میان اسرائیل و حزب‌الله برقرار است و تا زمانی که حزب‌الله حمله‌ای انجام ندهد، تل‌آویو نیز این وضعیت…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/443210" target="_blank">📅 16:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443209">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
رویترز به نقل از یک مقام ارشد آمریکایی: اسرائیل و حزب‌الله بر سر آتش‌بسی توافق کرده‌اند که قرار است از ساعت ۴ امروز به وقت محلی آغاز شود.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/443209" target="_blank">📅 16:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443208">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
رویترز به نقل از یک مقام ارشد آمریکایی: اسرائیل و حزب‌الله بر سر آتش‌بسی توافق کرده‌اند که قرار است از ساعت ۴ امروز به وقت محلی آغاز شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/443208" target="_blank">📅 16:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443207">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgPbK07UF1U5ebm1wPwT1n3T0oPYxUbMhHCFEh1ILSht2k_PiJevspGOS3-EPNfMUb__rBjBpppdAmHbiuowjsM4Rs_CpP_5guJgjcK2DicH2jVJHAN2pav-lyxeXujsk1122xpORptRLQj7Q9AmHm7-WHMmbboc5LKvtcFO0HiNC3XgumAb_aNEWGL0h0HlxUyF3Bqm_YzTaoGGztgxJeC3J7kiAZDIco_qsaziDy0vNHqIdWreuf7-pDGK5vEDkgwrZEv_exCBztnhr2jm59c_hR6ki7I9g_Y8hY31n0eWodLSuk7lifoaHZcQr5nBuFaWZDrJNWESRsaP2-JUzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه: تدابیر لازم را برای صیانت از منافع خود و متحدان اتخاذ می‌کنیم
🔹
درحالی‌که حملات رژیم صهیونیستی به جنوب لبنان ادامه دارد، سخنگوی وزارت خارجه امروز عملیات‌های تجاوزکارانه و تروریستی رژیم صهیونیستی علیه مناطق مختلف لبنان را که منجر به شهید و مجروح شدن ده‌ها لبنانی و تخریب منازل مردم و زیرساخت‌های این کشور شده است، به شدت محکوم کرد.
🔹
وی همچنین نسبت به تبعات جدی و فوری تداوم جنگ‌افروزی رژیم اشغالگر و نسل‌کش صهیونیستی بر صلح و امنیت منطقه هشدار داد.
🔹
سخنگوی وزارت امور خارجه، مسئولیت مستقیم آمریکا در این وضعیت را مفروض خواند و با اشاره به بند ۱ یادداشت تفاهم خاتمه جنگ مورخ ۲۸ خرداد ۱۴۰۵ که صراحتا توقف جنگ در لبنان را جزء لاینفک توافق خاتمه جنگ در همه جبهه‌ها دانسته است، تأکید کرد جمهوری اسلامی ایران کلیه تدابیر لازم را برای صیانت از منافع، امنیت و حقوق خود و متحدانش اتخاذ می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/443207" target="_blank">📅 16:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443200">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWU8yRviJKQ8nqsh9q5ThOyWZs4qbAi4dW-vdtQSd_aiCAIwW6D8rJqKtpK2Q217874Sxwy5gL5yZrGjDMzxA7ry7_ofrnWvmNv11Tnc5e6rQM0wQp0o1BWlYXqHIcPbUyEtBSl1gjCwBTw8M62VxyQM6OdkdXpf6pD-jkn8TjETDDQz1xJAgi47bNdpJCZju2vjvgdA8FoCJ8A1iFa8oB_759ro0PwIWX9gmMQSQpy582TU1r-mZ-0tNBlgr5yoRHO7uJRxYtWzrU8YD5Yy8i2zzBhx7dxc2VDnvuhLKHsboRCOVcAZkCasgkJYPUfp28tNAs5E1qbvMqbdvDNLyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2nd2T8-2SJyttVaan6x320GE0f3dUxXerp1ry6BnVfBvHAty8O7_iB3KO6Y2TPMvI9ZWkbmSccE4qsEyinVncDzHpx4VFaXU2Au-T1I_9Nu_l2gP9YcvmINrp_9fCLDtzPBNxFCmplszuhJ-H5i4I_pZVwWeI86aPnexy78K1RWkDK99YdI30vtvmVr0STdt0Aq7Gn5PabUNmvb7zvY_bLiVQSFebeF4N2-Fi4WOCzXhvRlwq1Xg341xOobQvwAcsHkwT24WgJTcDJSovgAcaSBRrlziTntn-MyCSOaj7_eKEX7Q3hoOmlp4FAXNorNw95jZVvrSCivu_J21OJ1Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EnbbDyMrdRZm6nCeqDioo4VB53fJfYruYZFZvho3shXM4UhLW_wMMxCQHKui5Pdc-2adTWL6Qf_l2rP8iONecl1oRVE6rLtVVy5o-7mSi22yxMhWNdAvupWpaaOmot4SDaAcpGFd-OvldQv_fkD2NORq_zM9DpEkHLtU7Jwc4s8DsV9bGbN-Tl5hbpTLxmTZbhkck0VT9tPTlRajTaKkDTJWIl2mTQxJW0fQgGSRT36EJzaCRuvYG2wjDIaKqbrtsv5dAAc2eITmp1k35j5Eqf5O0JoK7OEKE_oUsO0FrQY5wMbucE43hQSl0m-z0mXsEUq3f0rXFgCBHgLyMW8sYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LkbWbzpuAIX5fDcWqbDQIHimQwU4CB6mgCnc439bsyXQL7RKNgRx3n5WaC5po2dcckI62xiu4DYg0PjRK-vSYsHhqqhop_X8gwUSV6P4JX5dlUdXJm4NckJxijhZFJSLxl2GLL0EGsU_H2AdHZJTwXACiaJUnmRenWwXMJMI682qjuSdbt-RXsnllOgVeB_JFDA0eW-1Mfnx_yPXTY2mq2CyLTZmZDUWqBK6XPbAg2fm8dwYpNt9THFBTZoVgx55cZAAQ1KS8JmrDEFhN1qKgP-50yoSYKsjTjr8snv0PmB3UpFSAs17vKzCAmtSkRBp7MgjHOWF54eT12cB_4S_pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fR0kCbhQDfFxcRdnfBrH22l-f9Tracu_OQvEE0YsY-Ln8ox6_rya1l5hFDmsH_7a0gmm_vo_BVJzNJuRkKFMua0R4FWOK_T1oKT7l4VkCv5ddRbztg8FZvve0fdhx7NhVck8iZK4I9cGU3yTb0MOcKvuaf8svfjoLIn3oFxSOzBrAEpxIuUnAvFl1QuVdUdchoHwUb7n5Mn-VT7ZdaBX62yg6EPp3w1bXxmOeZYDkrpTc8GuTbdmiIXt0k7VpNACT_XPIfw5UYYHxvMarOm1gDw_GWsnVuhL5PTJokcxj59ItqOAppTbJWK1SYF_Op3DPGTjMroKkCWv8HmmqpprGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ps3iBk1qpxqscXLFE-0SXghsH4tKlnctvnEcDLYv2_cRbtAr0bPpWG_elmcCFy6ohHswFBOrVncCVnvBOU1NudEjC4zdHgEwFSygmNTLkGHTnyX-W4q6dIVIaukrJqB4ohQ-YtMrJ3HEMUyx4l1kYWpohZ8P1v0lzL9ZACkpeA7ZvEfS9vnsYYEpngNVmfliqaJeeS3yGDqbMkKWAvLeJ8UV4IY7dOJjnAWeiB6NlhO60x80WGebQcpAf4ItL3K4IBnybfzCqT7u_6qnqNznEm2dOWTAZP4Xl4T46z2A2O9g-Tw1T-vNj2PzXyO5Pkjm7d1Fiuk39mrrZfD4CCFb7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RilIxKydxYyvDC0w9CG03pUS5pE5EyIWLRwBIaw5yUjv8mJ7Taz7rTD22PBfRA1-r1rplKyWvP6N_ZorfZTG8sNkwwJqcgqFEKPa-V3xgKjfo6FzNvSGXbN5tZwfa7tZyzma-ZAL5heQWKK7bxXS3fZyLcdEzBMFYTglIVLgApjuBJWpS3pWZRZH5n7KU5InmJKdgzZ54CpFvDDUGLTyYzSIrBzXkM8PpTScSudVTnGTM7xJWFxGYZcEypu4csS8DJcjpe64rNtpeBp1zxEMjw_YmvCom_t9LLq5Ew3OBznTus8LhtgCtgYZrQzXXdafpyDqR3bNhcvHSDcg-nugZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نوای لبیک یا حسین(ع) از گهواره‌ها برخاست
🔹
اجتماع بزرگ شیرخوارگان حسینی با حضور گستردهٔ مادران و نوزادان شیرخوار در مصلی امام خمینی(ره) کرج برگزار شد.
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/443200" target="_blank">📅 16:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443199">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUZpeojCOzadH3-PKXZNYdxtrGvDmLyFS-y0-BQCGoAsaCtssOrnsG8U9Mb19wI2l_eH8ehS0cKZyBoq4FwHO7mObghelCDiAEjEIKbi19RPbhaph6HBkIXiJarjS_Ruj_yov2WZ13Kekq-VJWjYy7_Ib1xoEdnMtW4b1Yeg5-j7Lia9x9udfg8sckeS1NGcSZYykHhXOvomzY2GCAqaldu422JEQlD4X1J0GbHvSZyb6XH4DbeHZtuTgyKKpwWNiGSmF437EORKA-2sNtX4VDUVmHkza1q9vmbbPXqmvIm4ZoZsH1e1PqjCIfhmxa24WB3XMFT1OQZMlN0n30Z2Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ عراقچی به رجزخوانی وزیر امنیت داخلی اسرائیل
🔹
وزیر امور خارجه امروز در واکنش به رجزخوانی وزیر امنیت داخلی اسرائیل که گفته بود «در برابر هر قطره اشک یک مادر اسرائیلی، باید ۱۰۰۰ مادر لبنانی بگریند و کل لبنان باید در آتش بسوزد»: این‌ها رجزخوانی یا اظهارنظر یک دیوانه و نسل‌کشِ بی‌نام و نشان نیست، بلکه گفته‌های علنی وزیر امنیت داخلی رژیم اسرائیل است.
🔹
فرقه مرگِ نسل‌کش که مقر آن در تل‌آویو قرار دارد، تهدیدی برای همه بشریت است. این جریان همه انسان‌ها را تهدید می‌کند و تنها هدفی که دارد، جنگ دائمی و بی‌پایان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/443199" target="_blank">📅 16:10 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
