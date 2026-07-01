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
<img src="https://cdn5.telesco.pe/file/Nc-cII8i0XDz84v1XFyEo6I0MXz71hzZ91No93OOe6vtbiucK4t4Cnmjvc7yPVp6ph0b-u1hoKU2vDMGSzw-2Z9nbyNZp08M4Cyqpn2-WV3jB73Pl64FhbSqNn_AUvLi0wqAQFOdl9KhCeNXJD-F0SgPRdaWtpK32KDbWzSr2gw6_l6-sy0iVmcNmlTkpIoWw9SpE_Bo4L8P5Y8PGcGwV4qNmxiNG-sC12QvjqU498LZYEUjXI26vkU9JE8UpbvyxdCRng5dCh-X4G3Gihott-bMgqQWMdIxFut2UeYlEknT0LMPZLsioFs8AT0SoCW42nCcZkod2-I-NEd13LcPXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 671K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 07:45:33</div>
<hr>

<div class="tg-post" id="msg-97317">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIOidHrbVaBQ8K-MbHDybe6ICg2-iPoTV80w0uwAnWcM-l6jHfZfoOfBsajoc5Kcl2UbCyn_Od7cDH5PtgwyYW1V6cJbYYFoNgwujmmkqkIeasMKU6LMmEjPVKWT-pypFvViYPlXRYM3rgQ-yLFAyNlBAnJn6C1hUDShQspekSXZLvpHdoqimGkuQv2I7tsLiIxzC1ceOU5n-DkrHzkAiGYxukZO26xD0WLH7x_-kak2Thy9tkZzc94VzPXZKFwlLyqQN1aVSp1DyK8iVXNS3nyDk_dIxJO3cSU099h5IrNNaCOoI2OxFOGB96CvaUHS3ox2zIF0b0XI9fnhzcVpYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طولانی‌ترین پیروزی‌های متوالی در جام جهانی:  ۵ پیروزی — مکزیک
🇲🇽
۴ پیروزی — فرانسه
🇫🇷
۳ پیروزی — آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17 · <a href="https://t.me/Futball180TV/97317" target="_blank">📅 07:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97316">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AykQUUwEJFqpk3aSWIFpOJkFBQEhfUvBk1r8gDJLrfXmYsOP0ayGU_sKUWsF9oAKxm9FmnUPb6ukqoxlamGnb1twDwHzlUrr1oyZAiryrexDol3PtNx9T09nXclwnKtWYeQrXvflO489COIGUOwuvK6-6k3BTP1oV-yvmFT3v-scoQKIAy78K1BPWQugH6O58NOI4C1R-QYDwUFU99Qup4JExea9Ta1Mh72OfSitFziPJU5b1VIWpU31EUX4-OLP4VT4f83XX2RPIw3tBW0TCRcqxUm6EavXX9RmTI_zZ2PyUqm5zzvCunBOSn9WrAUz-I9mjhBZJYHYSL1arKMVKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طولانی‌ترین پیروزی‌های متوالی در جام جهانی:
۵ پیروزی — مکزیک
🇲🇽
۴ پیروزی — فرانسه
🇫🇷
۳ پیروزی — آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/Futball180TV/97316" target="_blank">📅 07:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97315">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9JRhewkYPT5kx8mY80hB4D_DGlBUdddaL6gh8IcL0WgCgvZ2RQ7J8D6woo3Rc97Ak_4VnAJI7na1W02cP5It38OjPll00vCkiclfFzogw1CTPc3FrLgQUSFWcdJEZraskiBfY1tZLa2Z6R4PVTKee5GpO-UJ-4TCw8irtXwLAC4AOz8vkKpjZKb5Tae94zbmtGILbRljS19_2qRjUa81u-t4Z64zQY3f85UVfjaNYn-ajY-nZH2qfQ8VeZZ1y8yqkFShZ-_x7ptR6eNtAh8FJMU7Qo6VCa9oc7IWLSyJu-UB4vZphxUb8NVLB2kFFuxCRyl9tfzZNLGa9UAH6UUPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
قانونی وینی(پرستیانی) بازهم قربانی گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/Futball180TV/97315" target="_blank">📅 07:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97314">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🏆
پایان‌بازی|میزبان همچنان مقتدرانه پیش میرود؛ نماینده آمریکای جنوبی با شکست از دور رقابت‌ها حرف شد
🇲🇽
مکزیک
😀
😏
اکوادور
🇪🇨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/Futball180TV/97314" target="_blank">📅 07:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97313">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Amw-yPIgYw3gvztblmQuGZOoAcPkFznQcVwBv4dgBT6aua0v8H1upYG_gdIAZE1FpMllqOEJXadwmrawYOF-FbwwnNLklwKEmUbg5tGxk8NvsFUYhKPmOJT5fSdfZxPxct2tLmxjWDVqCJl1Qj4kmTP8YTNl1mQPG_2jQkFIE-8tym8trfeK_VfUY6-33dFh3RRk99oNyl0ChuCw6ml_HgbEgrHN3KSyfC8CuiSkNukEZsivdvEaueAH4zav73SXpuIyYBM1N0tWT_ChcZ6zrUcqLOAK9I0G-xCwSiEPhFwNhovfoNiDrkdCzZ0gTY3wfCPqCAI-kGtrdN4sRs8ZlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|میزبان همچنان مقتدرانه پیش میرود؛ نماینده آمریکای جنوبی با شکست از دور رقابت‌ها حرف شد
🇲🇽
مکزیک
😀
😏
اکوادور
🇪🇨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/Futball180TV/97313" target="_blank">📅 07:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97312">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دقیقه 95</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/Futball180TV/97312" target="_blank">📅 07:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97311">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">هینکاپیه اخراج شد.</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/Futball180TV/97311" target="_blank">📅 07:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97310">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59fc7f9397.mp4?token=RIPtawLsZ44CdzC3oYULmdl4ZTNuoZhJ0kXR_WOC65peplTHu5w5B8uRt43El3K_aE0PA3I-bAjg-v78tm5_bqr7Vnd7rOMxNBLb-VpBfnTausiWQzqCfxO_UOAV-DySB8PAZzYVYa8511isovKPMZTWv6kBi4xbY6ZbWxQ3miFi9ngyesI1uGmgfymaCAn5XHFxuB5fWFmLFBDqMAs_1O-v93kRDI51LI7wn8t4l00_mxTsd9FyQ5UZaImOvrkewz_ToSuFjSIWlQfhmHX8ejdN8UOgB2uhng_9sgXfR0CRHAazz9G0OxMcwSRw1qFbZIGLP4ZbxjYR7DH25TBWgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59fc7f9397.mp4?token=RIPtawLsZ44CdzC3oYULmdl4ZTNuoZhJ0kXR_WOC65peplTHu5w5B8uRt43El3K_aE0PA3I-bAjg-v78tm5_bqr7Vnd7rOMxNBLb-VpBfnTausiWQzqCfxO_UOAV-DySB8PAZzYVYa8511isovKPMZTWv6kBi4xbY6ZbWxQ3miFi9ngyesI1uGmgfymaCAn5XHFxuB5fWFmLFBDqMAs_1O-v93kRDI51LI7wn8t4l00_mxTsd9FyQ5UZaImOvrkewz_ToSuFjSIWlQfhmHX8ejdN8UOgB2uhng_9sgXfR0CRHAazz9G0OxMcwSRw1qFbZIGLP4ZbxjYR7DH25TBWgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
مانوئل نویر در ۴۰ سالگی، پس از حذف آلمان از جام جهانی ۲۰۲۶، برای همیشه با پیراهن تیم ملی خداحافظی کرد. او که پیش‌تر بعد از یورو ۲۰۲۴ بازنشسته شده بود، برای آخرین بار به درخواست کادر فنی بازگشت و آخرین فصل از یکی از پرافتخارترین دوران‌های تاریخ دروازه‌بانی را رقم زد.
◀️
۱۲۸ بازی ملی، قهرمانی جهان در سال ۲۰۱۴ و سال‌ها الهام‌بخش میلیون‌ها هوادار؛ بعضی اسطوره‌ها از فوتبال می‌روند، اما هرگز از قلب هواداران پاک نمی‌شوند...
Farewell Legend
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/Futball180TV/97310" target="_blank">📅 06:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97309">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شروع نیمه دوم بازی</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/Futball180TV/97309" target="_blank">📅 06:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97308">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🏆
پایان نیمه اول | مکزیک 2-0 اکوادور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/Futball180TV/97308" target="_blank">📅 06:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97307">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مکزیک هم هوادارای خوبی داره هم تیمش زیبا فوتبال بازی میکنه.</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/Futball180TV/97307" target="_blank">📅 06:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97306">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آلمان چقدر لوزر بود که به این اکوادور باخت.</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/97306" target="_blank">📅 06:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97305">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58e871bcbc.mp4?token=HfSRjsso3AGwOapS3pRtDFU2eFaeDc2Xdgt8TUIapmWpY4aRKeu0nGrSHsC1FK4texew3iGHwOGC6gTTOpMDCiyi4buhN5iGJrtU8fr-eB2U9EWqzLif8mjDUbOAWenwBFRRb2SY1A8vR4se29nyHfrKKXoGOhAoMCLmSxpva6F1BDL8DPavSoxlhthpNLBY8LiazUZKnuQP0IfV7K562xNvG_bzngDgERgq_6BvUaSoA3O-Y6vObWeY-1M-N4276pZGmbqr6NNTCMCLLPsMn2nYd0cy8LOy0-W_PwIeOoV3bA6lkAv6HoX-OT51tqS3lhjNbVSaWCL23fML8JShmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58e871bcbc.mp4?token=HfSRjsso3AGwOapS3pRtDFU2eFaeDc2Xdgt8TUIapmWpY4aRKeu0nGrSHsC1FK4texew3iGHwOGC6gTTOpMDCiyi4buhN5iGJrtU8fr-eB2U9EWqzLif8mjDUbOAWenwBFRRb2SY1A8vR4se29nyHfrKKXoGOhAoMCLmSxpva6F1BDL8DPavSoxlhthpNLBY8LiazUZKnuQP0IfV7K562xNvG_bzngDgERgq_6BvUaSoA3O-Y6vObWeY-1M-N4276pZGmbqr6NNTCMCLLPsMn2nYd0cy8LOy0-W_PwIeOoV3bA6lkAv6HoX-OT51tqS3lhjNbVSaWCL23fML8JShmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم مکزیک توسط رائول خیمنز
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/Futball180TV/97305" target="_blank">📅 06:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97304">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رائول خیمنز
🔥</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/97304" target="_blank">📅 06:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97303">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مکزیک دومیییی</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/97303" target="_blank">📅 06:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97301">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ckdz9seO7iGTF0QvDceB1jqrCikDb0EwdIHek_0ZbgIidSpOBNINZVJmW3zXnDOULF7FsMQPzJLjVtYKXfEivnlk8RPrkRmArE3ZmThgPpB9_aXLp9xIlZppvaPVrltUi39-12QOfts6phdc0gTD2K-_uyNNbBvqsZkVxxFZTz-BUOrXBCk0gbhkdeX0eXuoq3PeNygtPcVmaBRIHI45qp8tICBuUiW1I-IDWN7Ur7bP1s4T5hc_eICsg1oxREgWaTW-RmtWMq_QEgR22GwBBE6uOyK8DTHCv3VzV65SL_RLZ7wrv4r945A-ewxS_3FOrVIfsMjrLT6d3x-htRl4EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KC24vaSTClJ3kQpKOHwMevL1nIpIOEb6T-Z50WFFN77HIUmTegrSiQi3lxVzCEgLLmh7raAs5cOKhUMVMuwUhU2qulHmj2ljALmKPPxWTc6Jtx7Pkw_n6uoSMQiC_n_IILQ8wK1re8HrA4aerNfuP7GMt4EixjrjyVEZIOmWOkv3KvBvFkEcmEeZBhWKd5Dam0Sikc-ljy1TPlsprDaAoizLtnUddGCETIVZDcIPmV557rWtri1U6YKnc-eJourKDNv9qnPhNp0Nk6rrcX9e_T0ekDKX4p05OtRaohtTkbZpZZ-edZ9kB9KWunSy8CKMQE4y9rXO2jxBpBAEOH8FTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گل اول مکزیک به اکوادور
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/97301" target="_blank">📅 06:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97300">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a754997a6a.mp4?token=p0KC6ACIW3tgSVqc-pecv1hxG87i6Bw-4Nm2gIFSfH6yDHL9vHAJhm_iEhA1brAfCqcpefKbfsMlRnnfRre2pg-syUk5Ek5fRHVmBDDfZqDlNTuHz886tMpIUZnez-x3IWK7gPZAr0F_eH3ssuOgTMl6T4YwFMZ6VkxRF3UAfhlaTPvFuQ2GPV5k0tqicRIuYe8hDtYszOlvlAnNf2wgqNn5LdeyFwzVz16b92YzBkZ__Wr_N8nKHdIl_7mwsABrgnTH9ttdfAzy_GM-H3kLjVQF4mta_nTILmbPbcB8XNnIdM1UH9Fnem9dPztmqZ83EQVM3XPlg-zuhhKOQY0Tug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a754997a6a.mp4?token=p0KC6ACIW3tgSVqc-pecv1hxG87i6Bw-4Nm2gIFSfH6yDHL9vHAJhm_iEhA1brAfCqcpefKbfsMlRnnfRre2pg-syUk5Ek5fRHVmBDDfZqDlNTuHz886tMpIUZnez-x3IWK7gPZAr0F_eH3ssuOgTMl6T4YwFMZ6VkxRF3UAfhlaTPvFuQ2GPV5k0tqicRIuYe8hDtYszOlvlAnNf2wgqNn5LdeyFwzVz16b92YzBkZ__Wr_N8nKHdIl_7mwsABrgnTH9ttdfAzy_GM-H3kLjVQF4mta_nTILmbPbcB8XNnIdM1UH9Fnem9dPztmqZ83EQVM3XPlg-zuhhKOQY0Tug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول مکزیک به اکوادور
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/Futball180TV/97300" target="_blank">📅 05:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97299">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqwjAwp1vASe-48WRNDbAVh4AVY8R3adRU6tZBSzu7STDpqisog4NDwoq8lGMjgSEtYWBl04Jcyz8ts6fovIUUGaN8nIiB1HmC51y08vAc713_YYzRoB5wLfjwIojFFE8Aa4pHrxDRqkz3b6NqwCfifPOsnulC9gzMIX48B8LMPhUdYG3XWn_G_B4upoq3GG9x03rlNakYQd70D9MQzD_e7GLchOWQrgHwNqyUEWTJGhr9t3pHnxmiICqW4aZscC0SHcf7sqnmAXV0-n8OdxMBF4n1FEF1RuOMHf7B3YcR4WL82iDDgwlsdp_e4ape25FFfdDEt2oV_IfMf2ZUJVQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خب خب یه شخص کاملا جدید اومده ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/Futball180TV/97299" target="_blank">📅 05:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97298">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بریم برا شروع بازی اکوادور - مکزیک</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/Futball180TV/97298" target="_blank">📅 05:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97297">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZZBNliYjMYNzFSIDGGwncVpWpZe089XBwzBxRYioDj6v_JthplTVmTQW9sul_rqoMIJ7Hw2ehfpIVmfb6UpUJV98CCLM6eh6cCizFnNUYHq5_bXUJ8ZF2j7Hk3e2R6J2hfmS6M8EMXPaUenCC_E-UgXiIqlY8VnytkENv_CXy_Av_zvMD9lJZ6G-OhffHuEYSnJv-yQS5sejrUDWpkHRcg6CfLAVu4Ct5RBp3_POUj_DX2asCh3U-vzd5FVl4r5hZtoU22hpr3Zdl3CtpW6Tj0K3lZqdhQtbrAzRQUOI3B-21auwtC3AMviYs4D4H80ahLJTnc__PtV8iwIINQqXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
⚽️
امروز قرارداد محمد صلاح با لیورپول به پایان رسید و او رسماً بازیکن آزاد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/Futball180TV/97297" target="_blank">📅 05:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97296">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01873d097.mp4?token=Arp7oHHcXW8cBRclDP_qiMoudPcAwxRNNzl2BTjSFbsmzizhKsJ-wT284Ewl-T89OWF8rA67E4aFiTkXtuckUm-4jm2N9jqh90IVEk7seFewSb8jZ9hYt4uYXUnKbLYdEKuoSnjaPLY6m5fY0Muv_wuD304ua90fes7FcPbERcCm997NEAyo8nVJeAl8RepDMiVauraP4xeWIncRD1p0KM8qbzKlAXFNpKjoFq1tkeFFMBliq9x6L_VPc0G0tJ9iB9eg49i28yKnnSoayTQVPDa5S0LrbFht8cwENQmvJCki-ReWfg7k80cJePprzzV18uIj0vmR82VMYlgMNMmrNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01873d097.mp4?token=Arp7oHHcXW8cBRclDP_qiMoudPcAwxRNNzl2BTjSFbsmzizhKsJ-wT284Ewl-T89OWF8rA67E4aFiTkXtuckUm-4jm2N9jqh90IVEk7seFewSb8jZ9hYt4uYXUnKbLYdEKuoSnjaPLY6m5fY0Muv_wuD304ua90fes7FcPbERcCm997NEAyo8nVJeAl8RepDMiVauraP4xeWIncRD1p0KM8qbzKlAXFNpKjoFq1tkeFFMBliq9x6L_VPc0G0tJ9iB9eg49i28yKnnSoayTQVPDa5S0LrbFht8cwENQmvJCki-ReWfg7k80cJePprzzV18uIj0vmR82VMYlgMNMmrNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
قلعه‌نویی: خوشحالم که بزرگان دنیا یعنی آقای مورینیو و تریلی هانری از تیمی که من ساختم تعریف کردن.
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/Futball180TV/97296" target="_blank">📅 05:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97295">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKIBiRud415DxlZ4xIuoRC1Ah-4EuthsQGMSul1zHvALWkzUgGZOX12P14nGt1XDi8Ou1hVevhtrSzHP7h8yqOOHxlFssLGMVeTit-uBY7XRmFnT-CKQ36AU0m3OM8lG4xJhVPHF52QVRTp8tO16Bb6sYcaYCJqCLy4pWlnzkwcL55-jkH4sxLfXUvRcZbslbCJyrF4u0SVkCEnc3_gPUJ7KmKNvpy4Ug2q2Ty_T6ZM59EH3EVV0705mavAKYx2NYNhRQdRqSCORaC9O7apbrSQW6Nx3oOtff3lQaWS51EcATlj5Ir8qZPnPtztTBn2E44NaLHAP80GEE7p4-awZJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه حاجی رعد و برقو
⚡️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/Futball180TV/97295" target="_blank">📅 04:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97294">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7f2XeBtF4dUktfm3AEXb1WX7dtSRESfLqvbwPsKGwKygSS4dWd4FyI-AwVJL-uAFByCql_SHKMsYqaENyKtohq1JDwkN5urTRcHBiFah_96ogY9Xvwjlq5N4a_TByrnL0WXDUuJlW9QV5r2YKYGipwpcupwz5zqwSd4PutJgC97SZnwfoLzxbVXJod8nYX9_wzwFwF6oRTHLpxg-mR1HV386Sa-yO92_tRmtlJuUCgVpUk0uBviZOwpeIv63YV_N01V8428TjgMfJx9xt9aejpn_lL653C70Fsg-twNRdYiqmU_EC3Xhb4zdCGuLdDTzo1NuCNnDwiLVow_Kqqgiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
| از زمان اولین حضور امباپه در جام جهانی، تعداد گل های امباپه در مراحل حذفی جام‌جهانی برابر یا بیشتر از مجموع گل‌های تیم‌های ملی انگلستان، پرتغال، اسپانیا، آلمان، هلند، بلژیک، اروگوئه، سوئیس و برزیل در جام‌جهانی است
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/Futball180TV/97294" target="_blank">📅 04:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97293">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a18350dd6f.mp4?token=eAjbLJliSY5XGiUwJq_jMbZWZ6JOceTW_pxvkkcerxvkfxBNMKM7Pz7is9y4k2Bo0uMoNZk9ayMtRIQob0n8BH1LbQYBwgX1Sf4LVUwVAV6he3YLtDwEbWsDLI4A755NRJDv46ZO-6CJ-PBc5r6-dj_KtQyjywrr8ifRbLBkm2jD-NLaUwCSTjwxZPZfoFSIkxi6OqQ6Pd4dush_Xi0aMWSJGs9q3ETcG-mC2Jskhot4yyScP3gk5wm8JCV36V4ZxHSFjalsf5kaCipDvGsL1wIK5fVjvtU8MRpryGxlS4iD2oFhkkY7X03hCUqnrtMjqN4qjnPIi7g8QcbvOTdS0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a18350dd6f.mp4?token=eAjbLJliSY5XGiUwJq_jMbZWZ6JOceTW_pxvkkcerxvkfxBNMKM7Pz7is9y4k2Bo0uMoNZk9ayMtRIQob0n8BH1LbQYBwgX1Sf4LVUwVAV6he3YLtDwEbWsDLI4A755NRJDv46ZO-6CJ-PBc5r6-dj_KtQyjywrr8ifRbLBkm2jD-NLaUwCSTjwxZPZfoFSIkxi6OqQ6Pd4dush_Xi0aMWSJGs9q3ETcG-mC2Jskhot4yyScP3gk5wm8JCV36V4ZxHSFjalsf5kaCipDvGsL1wIK5fVjvtU8MRpryGxlS4iD2oFhkkY7X03hCUqnrtMjqN4qjnPIi7g8QcbvOTdS0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کی دنبال دلیل درخشش امباپه تو بازی با سوئد میگشت؟
🙈
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/Futball180TV/97293" target="_blank">📅 04:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97292">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t05F-wNdgixyDTOFg-2K4z7vTS-IYk_xZlc856MHuxrU9n4jOGtoZE50wW2o3dWSuibGf-HsAoGLwZNxZZGz2_O3nOBpS2bw8o7XC2FEowTUdOn5JKLdSdaJO481PTMCM0a7VGoD_cGoCtYfkJ0D_K4IfJVYWwPX2TxCNpld5U9PdjMFEIDHsEmu-JP64PWPkNmmaDbvRA-RgZEYSve6RUkLEMve1RvVIxHKck8VCCIOL-_ywLwRxde5qYR4Sw0WE-obta3IYardcrpYqk5SaxLojyqQLOS-FlSClicV35z-GNEHy4mZBvvbN8BMQTivVBl6suH77Imny_4ep8q5dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
به دلیل شرایط جوی، بازی اکوادور و مکزیک نیم ساعت به تعویق افتاد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/Futball180TV/97292" target="_blank">📅 04:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97290">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BIw_0RyAuiE6VXDXSSNmz3wOGZRfL-PHV159cHFbmjQigSPNDcvu1Gf82f3zJtmVXQHRS_BPa71o2xeglWRE52qPLy7Aa4wF3fx11ANjTldjJ6q8IR1ivKmNKl4fyvPGqx4PrtLOFa8jfF2GbQe9AhQ8ya8w-7AdFtvdfppsrNU2qLCjWuzL697yuXvTX1V7TJYOlotD4Cu7v4Mrl3-_maaoQvzgE7tUwuD2vGimzIVYr6rRSa2DJoKIqNg9DzHpx5JO51WIVC04WH9sk9JCA0ivP1yIQIRKX3Ay6uKWBOq2rjxANBhy_u3NmU94YAcnfNRC5W5yZAERO6McdpeLkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e97yxHDR9NoKJFbw6CXRgDaTvd4CnINXG753FW1mCkaP1AOskXVoeMnEMcEVbI3hp--SB3co6RcxeAh-GTXJ1StZwIkFI3D9o2615xblSQxug6j-ypaDyecfHxzqkPSATD6jbSCQQndmgk6YVHImcwPdoY0aP69rfC-Bu1cf_jbjuA_OTCZJtgUKc0muOQCxjXsmkRwNZi-GJxNUNZY2zXS7OMACQpvdqE_vqlNkyHEt_LfY9qgZxnY5s2LQKvhhaonXNtMe-1JirKgmlAtj7qF1i5yUI5JANlGOZkXa6RFqYRh9lD6OqpyKLxG7fi8GkvSI7rPPJZWx-QF19aSyYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇨
🇲🇽
ترکیب مکزیک و اکوادور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/Futball180TV/97290" target="_blank">📅 03:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97288">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MU06yvs5EHnS1Xyu3G-0Si0EZ12EC-URdsrFcBX4HduwT6X4jegsj-PkWQHMhbB-Z6p5ZERoWNyRwNOe7t_qD57wbIQVpKswDOow6TwpjguRN5ZIyuugmZo28ShmVSnICNOBjyRGmbfDsTwEzOiOM6pTiXCEhZkYC5SmRV0ZRjFqIn6J4xkfVCP-7986CDz6ndFBK2h3utconDMHKGL2SkUR4tf89X_OcbNsWltzJVvmQd6zB1TnQ2iibbVC7XgtE1GRJJNljuMbM1J2l6odijZ-bCwatO2X0Evgas7u3N_fXu_1KK19RwLFNiwY1MjYIQHBsgccpRpCEpL1R4giAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/efJT0MR2cUHvGxnGsM_F823ytDAavRut0LCZGjPaL04Thtg1HNvVDWHu8iflPmtZFfBXl4iEhlDJv2-ZGLXi9MfjPmhd3wXcicJaswjGKVXmYGYZs8CnMzoXxSWLl1XqZR76KaMjqm_PpDw6OpT6OGpgJ8_JSA_NlzaKpKM-Fy2joPpaSsTSPpBzMLY9DIlNQsEWlhEv1Kx6KUzglWTIIKGwnzXKCIymRx8eROfuiwhDcZWprVY0s24nYzNT64GHSF9ogSiLoE06oaXf3a_Xy5GyXNxkf5ldq45P8i6UZIhJCUdEF6u4moja5r9qZJREmr2rS7v1-FQcjqpnKxpqSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
رایان شرکی که حسابی کلش از نیمکت نشینی کیری شده اینجوری دشان رو بعد بازی به تخمش گرفت و باهاش دست نداد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/97288" target="_blank">📅 03:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97287">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb_xJ4aDEKoQ0D_Qy6RZxnNRz7DKabb9URAGbCDNVVkD1F0XF09tjnnh6riiNwRiZBTOWlV1lagVlNRzDDWFBzIMj6frJmvaoIMdJVD7EGsY7GSReyoRwrAaUusv_eQV083DP1lf5SQiwbqYtI4LuVLaX3pQErBPEyR3Oo8WPDv8gf04dV6ehEhGbtHkGxW8TEoiZ3YHfP-LzIgfsjgZsvBL_jNuep44I0RJiZgb7pKCIl3UByYgCf2x5-czdxaBZ3AErQN2RRIwDaThY6IjpRikJZz18k4nedQSjLNsrSZzVPkFJ2RomQ_BNzr3ejk5YuDOncUBQOwXw1amLdWXPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیافه میثاقی قشنگ اینجوریه آخ‌جون بالاخره یه نفر غیر محسن بیاتی‌نیا و سیروس دین‌محمدی داره باهام حرف‌میزنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/97287" target="_blank">📅 02:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97286">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mltwaeUe4mSa0x-vLA7iafQH8HTTWiA6DNiGxiAN3CdXFXmYSrGCdbK0wWnrEprPzSkuN6-s993EPo9qXeEvU9EfOgX6L2XhV3x4vheGCipNmsnAqaGUza71yZex7cevVGwe3PN__Yjop4BO2lxOTG2XTLtu5x7XRftL6brb2-9cSVTKw17G4vHV9kOsB89UiBuWfyPMGwKh_ko99XZ4N6Ng7qjZAsf_NGVOc_Bu3MzDrfcUVIt95lAIvwSiDyZXH6_32ZSTuoFLdJ2mQA2GMxx63tV2Ph6CWO9ZfO89D6lr7km7y5nSS1mvfv1W1YVg_W-UZm5GkMeKZAjraL87dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلیان امباپه:
🔺
پاراگوئه؟ من در واقع دارم به رختکن و کولر فکر می‌کنم چون هوا گرم است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/97286" target="_blank">📅 02:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97285">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eK1-udsHd1DJd0HIOarv13pD6HCNbaSJv0qFi_V7z8nwcV_k9FDLNF9OXGe0IOGHNX8Mqis95eMvyNTigE5gSZUJ2ifp3qsmz1IsW4qLFSRFTQFxgZn2gjolnv5ALRRvDGXrE0qreT4GbyW5TOiOz70FzPFQ8p11WMXJ8tYj5JdNApxJq5bkZcCLknoZuGpbQ3vttwSFn3ASsh0q85pCzqouHx5qhQxashfjdIwAaqTJNrSfylnE3KIpJ0FOEvnRm2IcxRpwxDn1LeRfhkcD17lqg1EU-xqnu--XzfoK35LF_OfIl-r8Ofkpz-3BUwIVdR-l616FoTb8n26YE4VqXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
امباپه با ادامه این روند موقع خداحافظی تموم رکوردهای فوتبال جهان رو در اختیار خواهد داشت
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/97285" target="_blank">📅 02:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97284">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsumfVOK4CQcFTn335eYYu4Whe7AXXEQ7SSvCejy329aI7OGvjwf4YTvQ7jXYZg3stHsc6wzB7k4hWicuXc8o0zN1kBr-4k3nmKuDpQy7K2NNLX7cjJr7Z1DoMYq2HCVQoUfZ82QSGoTgQgrXsr_LbW9LCQ-n6mB_f0Bn23idz7FQ7U6HNubvjNonY-t03pqmT6p-Y_Vq1_WkM7QJPYpEl6psPy0wDHsSFBWZopvSvI-bnUPwtf5RqBMGaWLxNlU8k2uGdiYWktxZg9ceMrV57rko5e_NyIJ4S5kJAHsjoDva2ziwpmj-n83DjbRZKa3jjxh2lT1ONnQCHWwhkJQ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تیم‌های اسپانیایی با بیشترین گل در یک دوره جام جهانی :
🥇
بارسلونا در ۱۹۹۴: ۱۶ گل
🥈
رئال مادرید در ۲۰۲۶: ۱۳ گل
🥉
رئال مادرید در ۱۹۹۸: ۱۲ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/97284" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97283">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/97283" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97282">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ghu0lynbMP45v2A1ompJNAZ95h3HAvzz1w5YyuuImto4lV1wPOXfGkBrbjHokQjSQqc7vKVA682XY-mKA1RycLEah7HVp1bEhenw968AJmuJNpnkcMp4xykaAHjm76Cs3xRwuCrokLd-T4d5JRKN3HaSnl0eFGuHhIyrikPMCM72gWLZU0TeSjhc7XOx8DN5DY9YSOKh0tYHt5hfR8FTAx7k6QJ4v7qxQ6QBrWdhCO8Pbopm0orM52VEARygDs9ykW555t5u2V-Dn3TpMxhsMnToRrpmA5ZeOwn9fidEg6E7JZOzstKllZCMUkXNIjtBDtxKTdwxbTALhr87QUn7BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/97282" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97281">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snd1zK_iUdEzbYa_IDXPTNbAM0Q_bqO2n823hjgeLP9XaM1Y_GkKLBn_FZN4PnmRD-H5Uf7sXrjeA6JF8fI4_qhMsqlPu8FyA_dmUBjT7F0BFSx1XFQNLldaT6YGpFVeTXNWbFeQTbgPkWZPiq4vdykML6JPVTu6rmFPXloMvunq_Z686HLiE8r-qvd6wUTTDjXB_Xs9VNBt6bc9xy3IkPWgJdkz_oi3hMS0XkYSeLVvUaAFX7yJHfcJ9j6J4yx3f5uZsA_-hu9gjg-RzP0WdIzmo-na-gR1zT02UgoEpuU4mYA1ri-lWVchlaGYHReevYUJBzEMEAci6OuiS3Nbcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار حذفی جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/97281" target="_blank">📅 02:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97280">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xzsd2cNNGtHEnY7IUKa-QgOR1B7wGCpXjp8Wh4-XzXcK61Uh1JBtploqhDo_mRaGLo48DNBgHa-KiJyN5JUjXcyUwpuxVlj9Lt5OMTktXkDPB160MwXB41Nm3P4oMeCdqEkTw-C4ZK2APO9wE2jYoUKPvJFuzYRZywLaEq3-6jnPoTfrAwmF_uvao0OD0j6kfqItqwNriPzqkcpXzmUDKLaRYUyi6mi_56YMn7WIrVynxTclYArl-ephhoKNVAPk96mVpEb54RPbthSgt2o12ffP3Yp68_93aaMSvTb69ithosTvsMWYpjn2meeBiBpZeX9BqbjjO2ne7Qb-DTFkFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دروازبان سوئد با وجود 3 گلی که خورد نمره 8.6 رو گرفت
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/97280" target="_blank">📅 02:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97279">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FG1tzzUC1CWlEyd-gQvo4mFLMiNvPt_GCG_7AIqnzWI0DBbhLsneZ8i70x_t8xfOXWsAWfFJHtHQJ_e2x6gm16wCTRyTcS52J9MlTVhUiAtu1d7q4eFS0D6ghy68NPzUuLjBlwLz3xzT2A6fOH8Xy6pWrASsJNBUCyH4bRkCY9bsn22Qzd4TYOEoi31e8bywn6zIq0qtXgVyLboVkau3au89U0WXLLMVmRa63xBvak7txeJn7mZ3ezmPTo6lQn8G50t096Xs60W-vzDPcJtjIvgHWlURuy7bzrRbXhZdQnOGE6RXa0tZ7rZorhpfTBkQ7qoq3OcKAqujL6wiMzvYvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | خروس ها با درخشش امباپه به مرحله بعد صعود کردند
🇫🇷
فرانسه 3 -
🇸🇪
سوئد 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/97279" target="_blank">📅 02:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97278">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIUMBrdZZd22qh6I-fuUDKNKVihdFzvJXigxul1blikWXDcFsDz8WZj5daXMEZFe6pp0sSoy9wxAKlhJTQ6sCMOllRoyud1lYlAd5HhPi_8Zc_-U8kQbHs8_lSJhb7Av9wu_aLMUM9b_u2Is0TdWzLWm_wy4gLkgApwZoQHpdtanrATzqojJs3fbYjZABRagXxktdsHKNmSPJoUkO8hq8zSajlhxIMcsDHY5shskou9SVu20W-HnISNPWR1Pv9i5xIdCCmYPfGtH9RlM0FIMJv7o0GfEJBv7PnAfByuuQsC-fEQKLyjBqIUiw9gafsNGeggC73oeOo-qdU-8zlOqAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
برای اولین بار پس از جام جهانی 1958، تیم ملی فرانسه موفق شد در 4 بازی اول خود در جام جهانی 13 گل به ثمر برساند!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/97278" target="_blank">📅 02:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97277">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsoGJ57TT1pM5XcMO9jh74OD5fSk1Iz-i5qru9PIG-8C8ItY1yGuLYrccnOnTdV6pzQ8XzeyMSiVkqsCLZwALQ21S81bEhofjaYivG5qzdjwVcuW_q-iMhFd8195XcgWS6b9nfMZOWn3zbIv22QoxJIYMFkphdCaVN17_-c_uiPdyx6Vh3Phj3lN9DXxtaPEumedejRRgfJogqnZLa3WmK1a3TYBdvOJBFacJEAju_cyeHm4y9gJ7QYayc1naSI26FEUGNLtZFsHbU3pS9SGmmM9F1LzOoYFalXhR9OR4Wkx7bsk3Gu7kxyRkuCuqSgkoSo2r6ugLx14ls1o70Npfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | خروس ها با درخشش امباپه به مرحله بعد صعود کردند
🇫🇷
فرانسه 3 -
🇸🇪
سوئد 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/97277" target="_blank">📅 02:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97275">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PzXuvzz1gofGor3jTEo9s9BY4IKYfYbo1Ds-qPpSr4PSYDQPOJJ1eKkS_7jUflZDHct2T4520gEBtLVwMzGVT4cuWdxt1qbhZNIdef-FiAaRI2thk6REQEVhSWp8d8zUdch-27x9U3rEPg4dgAkvomi2fjzSnVdpDqfIag1ptI8tBfsxxKkyoi5BeNt1Gu9mkJVB4XIJv5B1mGsjWwLpBXxy2P6z9HecnEAJk2cIwAZpZpr2_sh06DXZd9QoxNCGdEvZv9xduFaEi9VjLeCTY_ihPH95zmy-dsKKVqsY5OpbTyzm5hErpO2Jremy-EdGBUP46Nsy0iu4g5UE_87eUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KZSrCII_2n4cohl1Ist7-dxLC8I596AUN7pgX0s8MsmyRxBt-HTyzUa-cNjWJRc5NeMrP66Y2JqZg7BeeMRA8uGtd-4Ho8iNzKzYi8mI4W9bl-QX_zMlkmw26wfcYAMVGaVnNrAwGQOIorGcyf638caJ2GP0PNCGFPVSuA07sItR4n7HmBSTtPEWJTs7pERknODkZZJKcYUwfQY93VR0GEb0eN17KSZq5GPlXINFuywgqmhxLxgTp9MlMk8I9DI1n8Oan9LoJWU-1bZXlaBJNZJva2kgX0OZWTkZU_T0w5R3ei5npB8CyvwqrRXCCAl6vFPS8yi5jEWjYZIkEUQTLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
🔻
لامین یامال :
🔹
راستش اگه مسی نبود بازی های آرژانتین رو نمی دیدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/97275" target="_blank">📅 02:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97274">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFjHAz-MmjZAsLxUgqae6WO5YP0JlXg9P-blMmy_MKpiCkqibpLtvKojKVR-svizg575WqqSRLmZmhyUEA2hQ_GlqzSr8X4l4xcU-MjEjpHwcbdFaSjAKyGWEIFcHoggilOYnlBv_eoM8Jeuj2IUvtXjN8sXMtfGS1az3G3OvkRRHcM-8Gt4cMml_Z1ELbrCKpbVKlh2M-vZ5tkd4LYTBbZis_gwGcsk65EqpwRJcp0kWUO026mYd0ulNi_cjMs6Umq8JnJFaD3UH4-_54L22Em1eVdBELCw8-a7FlTkvX8AUDI41TEJpoYcbstoobDANh9BTpVLj9QXIh6YrOtWIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعظیم دشان به امباپه وقتی تعویض شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/97274" target="_blank">📅 02:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97273">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHwig7Y7QCijsVnjuecN3nnWnuFgLBFzRk0H5O5s9XFOqqYI73ZcIflYVvHccUmlSqUWsg2Ux5nkLV0NrV3UuqV5_RQ3ML3A5O3qRJEBETX6PzYWjhkw_C3_LJhQH5wWn5-v63_LJuI_MPOlupHq1Og_XeZpOgZpuHue9LSgbRDi9W6dIdN4Jrfb1R6yVJWAiW8he3zDZ3U8Jz3ADtB8FsY-OgoOv3yrLrAz9rrfBkAo2v6_3hP71yh6OK8Y99fz5W1DE9htLlMrOw7CRbaycs5eK44vk_k38mpdej4rxfPXfGbh4BVbTW7wIHjTekbP9zIJmmliAa-s948NVGi8Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026 تا اینجا 5 میلیون تماشاگر داشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/97273" target="_blank">📅 02:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97272">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_m0uLICWVIcZwYC4MHtBijb6031ra3KyF-_2Mk0Itm9HwIq4rJHP-jzSTLfn8axkksHHdeuEOIbCKfFXPT1X_ruFrHkSKARKPHe0v-GZbgviKL2vGNqUrqW_AJ9LKV1-9SP5KrUuQAe4yAVVgcFLYIY3LHwpNmRTBddxK0C_8UVX8c725caT4EeRPoax2t-QkIbw6iee5FDzeU6UAVaiYDFCds4__AFtu-82tNkURc46wvPfGOkhWj1I0rZJ5UQQPZV6GGKy5C3lql7AgzCsAzB6oFIztfVUp77x_3vY0qNbERkB-xuBbswlTY69wbLjw_GbNeFh-5kFlejhrHOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/97272" target="_blank">📅 02:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97270">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nxQjZst1qy7tpiipbI3_oNZ3jc5BZZzOYeeonfyFOjIbkyX7e_YQIDS0xStk0fzlhqhDbTZ9_WHfGaOaFJKk9RbofEHJTECcj1bN6f0RPRxqprnSuR4yeAgp9K6YYGqk_m9DntRm9IiQrX13kupwY_jN6flu6SflMB-2rXRa0B7rRkxGkVbMAVVEPwgiJGZVtgpjJ9ihYDoaysR-T3q2JrG7KKMs6obMtKXqbaO2cXA7phsiaIFEXWlH7STg6MY3B13aC_kGVuL-yW9YoVSJrRxorNqOV0Tt3TzByEktOrF24nBAXu0XTKiFBI7PDGMlyyICrwliPKtawfFRXxewww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5IE3RLvXsgjyrRagKXjrUOFwUu7tIp-OETkmiXzlQ-ApCnv9qBhcOhqzitrr1k7c6f1rhvsDnwTa8nzD8ObReS47Kqw-GngwZtiaMMwW7Qh2CGC1HWzyEq75ufd497GDUu5N1IBj1ajpepu8AXlLxlPaocsleSL9oMfnmt0ykjglz92Y-Mi8ZZf4c6CRlocb46SJHjqP45Ze5Xx-8BuGD3uNnTubFSUYhx8UmekL3PiwcsFPPmv7WCC2ADbXWQGe54xzhTTeyCjMu8vyiua5uqzA5vLZeHm5bY5NvWTSxEjSGpqjCnkIneAALQmpdsl6CpmzpFk1Rc2VTPRW_utEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🌎
برترین گلزنان جام جهانی 2026
:
🔻
لیونل مسی : 6
🔻
کیلیان امباپه : 6
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/97270" target="_blank">📅 02:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97269">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ey4f8sOz6qKC-A4Fea-RBujgd-z4uH8M0GpA-jsyHmvmIgXbDpCsaL_KlermjaRn7xA4EEkGsbLBMd8r7egnSHzeeaeIsxXTaH7EJfRV_QgXJgAwCnQMOhmwDwO2wrpGjmeRc2gBnR2xJcz21xjpW2n31XCH7ubUZrBku44IG_53JYOxJ4ZvSh3PHSDJnT2H0YojL55nNhLe_2EZB99lXVSI_9nSp8h8aDvlJjcmlC8toVLpGqqOaRAnrPbK4p4J0kYFOjHR8_F6aQzQHW_RId2DrIqdtp3Nvq9r8oFXWWwuScViF9ILdZeqZIv5n-_ot0QrL28t9rClPoNnnbqPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرانسه به اولین تیم تاریخ جام جهانی تبدیل شد که در 5 بازی متوالی 3 گل یا بیشتر به ثمر رساند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/97269" target="_blank">📅 02:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97268">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59c55785b7.mp4?token=cWtxttB5MHA_YTxsq_3S-oEaKInl7ow6C6YREd4X10WGCE0nlWsri9PRwWvkPenm5t7E_xu_ZONTt6pYxGZcqJPsZRBk-84cUSlO9YnR8wcrnIOkt9rcuzRRrwp6zAAZEoiYXIeg2EHrHUdRr4vFZZdyWxY5XgMXTmhO-VDeHWiDG3AxIF8ZEYx0MVhKCnKfwACPAjvwyk8PU91jvUhER8iQEyRxm7JWVMFXMp37oiGBCwvJP2kfwJXKNbfI4GTxLVDPVs2yYAe83jG-SobfdlWnspdQognaC3yA9ul1ceGtEiDLg3qp4bpDgAxyKYt7Kpi7PzUbpF_7CQY6UuCFLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59c55785b7.mp4?token=cWtxttB5MHA_YTxsq_3S-oEaKInl7ow6C6YREd4X10WGCE0nlWsri9PRwWvkPenm5t7E_xu_ZONTt6pYxGZcqJPsZRBk-84cUSlO9YnR8wcrnIOkt9rcuzRRrwp6zAAZEoiYXIeg2EHrHUdRr4vFZZdyWxY5XgMXTmhO-VDeHWiDG3AxIF8ZEYx0MVhKCnKfwACPAjvwyk8PU91jvUhER8iQEyRxm7JWVMFXMp37oiGBCwvJP2kfwJXKNbfI4GTxLVDPVs2yYAe83jG-SobfdlWnspdQognaC3yA9ul1ceGtEiDLg3qp4bpDgAxyKYt7Kpi7PzUbpF_7CQY6UuCFLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم فرانسه به سوئد روی دبل امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/97268" target="_blank">📅 02:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97267">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دبل لاکییییی با پاس اولیسه</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/97267" target="_blank">📅 02:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97265">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گلللللللللللل سوم فرانسه</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/97265" target="_blank">📅 02:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97264">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">امشب اولیسه تو گلزنی طلسم شده</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/97264" target="_blank">📅 02:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97259">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhGCMfa5eMQqWiAl5-iFcBYuGPNosl9a1vfo6g5y4YdNGOq0PdmNpLN2fKIfyovX0VdmhwHFzp9Oa61HIPjZ5cHyS58FlK70Y_RH8e7P5T60B68sN5NbuJ42F62FXaAtWkz1j8fjLh1u7yKEPHr2mTIU4vDIatiPzwm5167JAvB-x8_FkjW65DuyWZd3oAKvsV52ajN2H77YLEYUyKSbup9bUXekLAmL_AIG7a-Syb2NXxSureq6U73bN2VC4aR8sXPLhNHJnv7k3o6HaGrghKuT_sV_QqB6HdEHh5zFh6ILtCJ8IJ0KA-r9pWEx0ZLhVciqfsglYJ2ojBVO5jXDvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c5ptr2YOViHjtELTlu24sy03outppwMy1MknOheUir62llceXsa_OAY3ZiSWgGX63taQCIDlJWtikVeAG7l65HCc82pmDu4esFFcheVqwP1b6DmdhMNzM8TZQjtEiBZAVxEzPiKlLcyUz3KabkYnxstxJEaNFtS1nd2u3zlyXZoBMOYf_8qhlWFAnix7E3BlydcixWVuufGoY-tx1iFE0yTglmJnz7P9rJAU0OlqFlzUf4qZou8PGz6E2bKm265PN_VWt7Us_ZrNlqik0Qe4gjR_ZXkSgmH5xeq2JmHB7tVPaYw27eEuyBBN8xz6gLiQRI_WzwPrYV3vVUVGCLpiWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/htmarO3nt98G8vjQibozQ2iJ1GF5AXOQ0FjqMmrH0WHKAizmmiddAc4Sjtyw7eE6rSYMBe9fYYZ-Uc3uRYx_ncp2nvinKn0UERJaXpl8lkoNaw5_6n9tuR2IFfzCK4B4z6mr6v_T2PTIrzSMQ6-6uqx9lL-J3VOhQWg6A2mllAigyNvOgMDWrmqKek0pZuOxLyMrsOf64UlUCXmj0tZ3QTa4GsQEcenOij0Dh6jeG_U5YWA3SDE06Ok9EqXNwcR4DvPy6UfsYvpyrbHmiZc1oATuyjnwI5HQx39w71Gklr8Kle76fdgogqDEVllZeoFu3ShVhXJnN5jr49aBqCXLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eXsCihwslrGhcapBywom6KXrfaWWiQFZKEeJSG2PnTEN5lAbGUJWvnv75XwBQS6aNJTDX8_q43m8ydpaL_vEz-wMW61rvgoKOxkIZQQMjv65NBBNFXnlz3r66rAoNS7CI-UDN3xdbcbs5IGIhTTScLqZEmtUUaJcwzkH-S-8uZD3Jq7gabe39u4MgIy7d_gB9L3HB185YRqUeYPOam441CxBV5n-5vE1kCgG_ZUUz5IxKLOd0CDYppU4FfMFDTONE8oLKjRs4-yjOMe1vJ5Zv0sOe2sb9s6ZQ_ZiT-tVCsYXSeNtGPuh7y5DapPYRAHuk3avQbNzzwobEUDY1fG-jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FmdXDni-QxTpKm6rtfUB_bzv53QetUbS-qb_fI3SA1X1xU6sOBOz4_E45PSDaod_4ctRkpVQi-fMIEw4HqBuCEWQ5Ad-wcdADsoNePbKbHFRDIOx7z_lgKiDipM1t0OZ8baO1i8Qlfyr6q2p8PFi1ANAK-YUHZTd08-DfwLY3yBjvW21TvxJ1d8-m5Tefh6vZMca4vky-qIj-_bN8IRhLCjltHEhLelMYikpw1QL8fJ2rnFVDM9YSsGjPYs6X_Ibl3pTONPmsPcyp9w25fVWf8K4z0GT7GI6thW-BDKJ-P4xpaUIcteajUnR-i_K0431DV0AOjbUBUwGU6BxHx7Azw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
بازیکنای سوئد و زیدیاشون هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/97259" target="_blank">📅 01:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97258">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAFoD_R0gqJChM3hm8MetNAhdrSPGCAvpisY6G5DuYmelVob9zCODWcp6GCwcpplRFKa7m-H0rXXiY_YlHhsNqEVcrEbcshCYyiK_t3bg_2i3tKq2yZlrKZ69zXqm9dJgk7mfk4uxLpnEJs2EaPAl7FVHIIm91mdsQwyDwbytYyx_jVEuKbPW8jIu-eihpiPuGYXWNmZfKayCEtGmjBNMZUHJ4a4xom1YKT5hYfDnwH5ZegQh0wXSSwZpd02q4qExE_SFpfVmqpE5AMQDd3lgWttQOYONNyQA5cXKLR44tYh9g6j9o_CFzjSUMUJi77Be4AauGPZK7gDx_N4bDTYLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/97258" target="_blank">📅 01:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97257">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گل دوم فرانسه به سوئد توسط بارکولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/97257" target="_blank">📅 01:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97256">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">چه تیمی توان مقابله با این خط حمله رو داره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/97256" target="_blank">📅 01:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97255">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmvAt5Dmho_BjM0dtgfAjN2PNl-pXtazgMUiIc0kGawFkSb6FjuVq3DBPrHZfvsnzy-SFAnF2FuYGL3cvzYcSdaALf-C_ZRlE_jzbRV2VI4SuACDlS5h8XK-lR2NOwVHZ3_3VjYcKmYAiE5biBmra1AXbb_g4NM0Zrkm6Pr5hG6J7uKqyXxlkGgTm2bR07ivzGqT3LNmpB7ASS3vRXe1upCqF5mdGTXYrXiMwzxlgYBJwG5ksaOo_i2TK7IVB-4thkoC018hPxX8rz6k-Fqn3hb0sKRAgfsntHa_Y8i3msvje4gb7eInCywbzajdQMnAFlcf5ERlskOi0vYZZez0tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه تیمی توان مقابله با این خط حمله رو داره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/97255" target="_blank">📅 01:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97254">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بارکولااااا</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/97254" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97253">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گلللللللللللل دوم فرانسه</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/97253" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97252">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آغاز نیمه‌دوم بازی فرانسه و سوئد</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/97252" target="_blank">📅 01:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97251">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anRmWLzSzIBv_9Baizq28MKo8g_0_Hk7F7Vix8WA5a3riYnDfL6Do00N3ztgWTqh4eLazE1-oYUuGj-Z7_Auzm5CythVLh2rmS3bwlZG4KlSfLXK3lfIRWMSFSQN0Rb5N93qnpqenOIGgsmKSFOTjVdU9xL1j86zZ1hca-WOt-OdAcJMBFrbpRcKg43yW8oo_Bf3rIip0DbjWzzBoHXz89Xmlz7ZcRYVRvM3tAR-03OT1-yuDxc4dCxicj_64RbbQfIpCWAnNE_uLVpthqr3qh0iIpHaGBZx30FYW4zAiM0uZnMrSl7O0j5qrFtYU808f1tYl9WyKlwCjDTpepX6gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
امباپه جوان‌ترین بازیکنی شد که بیش از ۱۷ گل در تاریخ جام جهانی به ثمر رسانده است:
کیلیان امباپه در سن ۲۷ سالگی به گل هفدهم خود رسید.
👑
افسانه لیونل‌مسی در سن ۳۸ سالگی به گل هفدهم خود رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/97251" target="_blank">📅 01:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97250">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
📊
🏆
دیکتاتور کیلیان امباپه برای اولین بار در دوران حرفه‌ای خود در جام جهانی در ۵ بازی متوالی مشارکت مستقیم داشته است:  ‏
⚽️
گل مقابل سوئد
🇸🇪
‏
🅰️
🅰️
پاس گل مقابل نروژ
🇳🇴
⚽️
⚽️
دو گل مقابل عراق
🇮🇶
⚽️
⚽️
دو گل مقابل سنگال
🇸🇳
⚽️
⚽️
⚽️
هت‌تریک مقابل آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/97250" target="_blank">📅 01:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97249">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cf8s0ab2YjrCGTnhIIrBrSwCXSwXi-vNDsybIPzuilfemDm5CN4M0c9r9rN_HxlEA1duXCZiVG4nmDu5dyEaCaLG31y5kS3OGheAzPHnxnpfLt7OAO4WyYikOGE1bq3Ph08wK9AyNVwKq679jZftiKP7JWO5AG1C36WW61wJms4nFdoC3wT1qkL3R8QWYTJfKI0g5djXYslBewqtMoX7EujR3kP219Bt7H4c0icAfq47S6GIvHTdu58K44cUd0lhqhK2_qCXdNbS9Wph8yxJ01C830wfhpMkf_eFVUSb9e6J6Rb_9OPstWQ_MkZc-5W7ggVJtI-gQUJLcDCt49ThMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
📊
اولیسه اولین بازیکنی می‌شود که در یک دوره جام جهانی برای فرانسه بیش از ۴ پاس گل می‌دهد، از زمان ریموند کوپا در سال ۱۹۵۸ (۸ پاس گل).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/97249" target="_blank">📅 01:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97248">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/is1yvMlvs3Fa5yWqtJyPQpOhBZjovLBrR9jc3u2RCCGSYmMVEr_7F8EYpIGOt9Ekoq_0ZRgT0N4j7IRA7nomw-3qPycBE-KvhAT9vUEPLojAbK_jdju__XOSR-ySa_57CfXwBusxM84ZRujU2UVUhDIXL9iz0U7V3o3DCxfN_DP4UXZlXdQ6m3osyhX6d0u9TCXMbgQsSWWJxfhmnEAWlAXq2Q06HAEt0tzWNXw_0PQS6txgZpyjUV3pW_V_8iBFiCBcbJM-b4f6N6elpz4dzYZQfkaex5EB2LfOzOy7xOQ54-r2PnftwQyDpHzBZ98pDY0qE39-aHP-SsJ_oBzysA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🚨
عملکرد دمبله و امباپه در جام‌جهانی ۲۰۲۶
🏆
🇫🇷
۷ مشارکت (۵ گل + ۲ پاس گل)
🏆
🇫🇷
۶ مشارکت (۴ گل + ۲ پاس گل)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/97248" target="_blank">📅 01:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97247">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
📊
🏆
دیکتاتور کیلیان امباپه برای اولین بار در دوران حرفه‌ای خود در جام جهانی در ۵ بازی متوالی مشارکت مستقیم داشته است:  ‏
⚽️
گل مقابل سوئد
🇸🇪
‏
🅰️
🅰️
پاس گل مقابل نروژ
🇳🇴
⚽️
⚽️
دو گل مقابل عراق
🇮🇶
⚽️
⚽️
دو گل مقابل سنگال
🇸🇳
⚽️
⚽️
⚽️
هت‌تریک مقابل آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/97247" target="_blank">📅 01:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97246">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZccKEKkB0p1Tt8tmTjkX7o9PaZf-BR1OClWl1CCkc8A2mX_8zpSZFlErGMUUj5xRR6WfQILd8tRCpPVKUoZctYJrrqyW7NJE8qMN5PWycQaL4trLKo92HjYVjumn66J9mL2fw3fZqBKVprrhDkguRLn6TPR3j1TFmKgniPr9ytttQQ9-Dg-n0LaDkwQrKMgyCGH-bAdybMKa9xsMnCGbahDJ5r5BTMvAO6wDF1D5EA-T_ZpGrsTi6khhd0RmHxJRvOI34r1tYu_WQ3cyy8FzUQ4mCW8Bzwcf35nbAzA-NXxTPhIceja6-G4QBZlg6RS39M9m65EXmvGrhRb3tZ2a6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
دیکتاتور کیلیان امباپه برای اولین بار در دوران حرفه‌ای خود در جام جهانی در ۵ بازی متوالی مشارکت مستقیم داشته است:
‏
⚽️
گل مقابل سوئد
🇸🇪
‏
🅰️
🅰️
پاس گل مقابل نروژ
🇳🇴
⚽️
⚽️
دو گل مقابل عراق
🇮🇶
⚽️
⚽️
دو گل مقابل سنگال
🇸🇳
⚽️
⚽️
⚽️
هت‌تریک مقابل آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/97246" target="_blank">📅 01:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97245">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSfywowbJTVoUR-VsrfwDWoT9Rz0LonOOnEk4uV2M4azH7v78a1Sjj_Wc8C7WpS0dYU9hhBEcFnMtMp386U__JhskPVoPqnnNLFThArYbQIgt1fMPYhJhB-3oxAxyyLZ0yYDufq3-VzRkY4CCfKv-29YJFPco_Hfc0eadjcwJCTANmaBqE8OWszjsBqBWv2zd0Ai4KXGf_VvdFitxE6uQktPOgijtJFcvjAo4PKGa5wNfCf2U38AgaOWatFhTI3EPNhLKMlqtokvrx5S2gqW9nr_Iusl6_ncfVY4AEwaRpS7-H5nKBLjgLxQi2hHKXxwMjnVa5MHmop_YdZ9g6Tv2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
🤯
امباپه با ۹ گل زده رکوردار بیشترین گل‌زده مراحل حذفی جام‌جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/97245" target="_blank">📅 01:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97243">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇫🇷
گل اول فرانسه به سوئد توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/97243" target="_blank">📅 01:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97242">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/49dea00f2b.mp4?token=kUX86R5oy0OmGyyFMd4S3nHj1xafxG5dq2GG5L_At3Ed9nBsiu5-56YeYROI-USkopt73mSMvygEqbiJttYZO-AqTrZPYJgvP2ehux6DB3J2o5qq7E43S8K3bHO1C8iwr1-QVFNJ0z-yN8XlQa-j29QGIBcdrvJKe-OGA-uo2Y-xNtw10Ox9tFXZOaRmGTfFGzWAsgdsEEb5CvOvxsakI4U_HPBDA0yptQc3J80Z53U8GCZV6u3CnM3JUBMtjJoxpeUZUmG6sawqw6HNRrqSoMmLaynww1Rl0vMlXZNQhu6E_Y1Tz2xYrFHvXmzjfkdsfew1-giAEppdxhgpXOakiYeZEqS6bCxvExQpLAnmT_t8N3ttRtzgMAuE9QyvvrB-o6I-eNRAymSs8O7ef6sW53agxtTpLgEP9voWpbQqAs4a2I2HU3yCp-mp8Tu_iBF4eoTPuDlqhyCSCl5T7mgCmUkqsWHVua2yyZfSzlFHqZMC9O6wvrOM_gR4oghp7bdHUwWmoZYR12LdVFG7-XQ6uIqOEvij51dIVTKN_6LFxgvsWDduUbwL8K5PalAX8lGvvXVHc1ApJMUEmIDdCxwm4IHkeFA1XFtQMKBzvOcLcMzTeLcrrx_LrV6RC8AaLz26MxWmvF7ZOfigfiuwk7yboGADQwtOdFNROSmEU6QOGto" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/49dea00f2b.mp4?token=kUX86R5oy0OmGyyFMd4S3nHj1xafxG5dq2GG5L_At3Ed9nBsiu5-56YeYROI-USkopt73mSMvygEqbiJttYZO-AqTrZPYJgvP2ehux6DB3J2o5qq7E43S8K3bHO1C8iwr1-QVFNJ0z-yN8XlQa-j29QGIBcdrvJKe-OGA-uo2Y-xNtw10Ox9tFXZOaRmGTfFGzWAsgdsEEb5CvOvxsakI4U_HPBDA0yptQc3J80Z53U8GCZV6u3CnM3JUBMtjJoxpeUZUmG6sawqw6HNRrqSoMmLaynww1Rl0vMlXZNQhu6E_Y1Tz2xYrFHvXmzjfkdsfew1-giAEppdxhgpXOakiYeZEqS6bCxvExQpLAnmT_t8N3ttRtzgMAuE9QyvvrB-o6I-eNRAymSs8O7ef6sW53agxtTpLgEP9voWpbQqAs4a2I2HU3yCp-mp8Tu_iBF4eoTPuDlqhyCSCl5T7mgCmUkqsWHVua2yyZfSzlFHqZMC9O6wvrOM_gR4oghp7bdHUwWmoZYR12LdVFG7-XQ6uIqOEvij51dIVTKN_6LFxgvsWDduUbwL8K5PalAX8lGvvXVHc1ApJMUEmIDdCxwm4IHkeFA1XFtQMKBzvOcLcMzTeLcrrx_LrV6RC8AaLz26MxWmvF7ZOfigfiuwk7yboGADQwtOdFNROSmEU6QOGto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
گل اول فرانسه به سوئد توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/97242" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97240">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دیکتاتور امباپه زد</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/97240" target="_blank">📅 01:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97239">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فرانسه اولی رو زددد</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/97239" target="_blank">📅 01:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97238">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/97238" target="_blank">📅 01:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97237">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91457d579.mp4?token=ZRyhpuLtht0AZM3iBkw_LqVat-ZC0lGDkI2ulj_0FcPpIQbE4A-PCzsu2rJ6mic7mBnCaoWuiBNZJYjLfzU8JdQBi0X3ZoudMQHgpD74MDlqw_4wFe3KCez8rxMBWqXMtS30Ltnw5toeaZrGM2fFPhjHunGmwdcvN4ltYtHjGtDECRUH4ri1Dbe2rSgRk7vTJAq1NURCKLSzlblzsHLlc7NVv9rxMwnxGP-iUvURQaEhQytKUmrCObXL6PXZB6YiPplGjpijwoRhl3Y5m0KxAS552439EH22w64Td7OZZkPL8W2oM0EIdwbHlzWMWTk6vDD-0hNn6INik0lCaR8Pcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91457d579.mp4?token=ZRyhpuLtht0AZM3iBkw_LqVat-ZC0lGDkI2ulj_0FcPpIQbE4A-PCzsu2rJ6mic7mBnCaoWuiBNZJYjLfzU8JdQBi0X3ZoudMQHgpD74MDlqw_4wFe3KCez8rxMBWqXMtS30Ltnw5toeaZrGM2fFPhjHunGmwdcvN4ltYtHjGtDECRUH4ri1Dbe2rSgRk7vTJAq1NURCKLSzlblzsHLlc7NVv9rxMwnxGP-iUvURQaEhQytKUmrCObXL6PXZB6YiPplGjpijwoRhl3Y5m0KxAS552439EH22w64Td7OZZkPL8W2oM0EIdwbHlzWMWTk6vDD-0hNn6INik0lCaR8Pcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل میشد قشنگ ترین گل جام شد.
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97237" target="_blank">📅 01:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97236">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-1rUyZ15lMxt-CulmTcoNknzWO4ojTWqghyOzmU7B5janfRU88OjWVGMlCOLLkvjLxwV5usE0DmMWVLcj5-m3kyo-W9lG-SPCZrAt_0Y47HhEH3vTGCkiMpamHcdQ6hLa2sbqGCcskJ1gjDypYHzRjhwg4Fvwg51PZxo0H4NGk4bVvR00JFpZ9xssCYoM3ETiXoYYxNne9meBpzpuBSDMCf3E1M1nWPYKEeECBP2T5MyU_qFRUMDot1hXnsdNykAaVJSyJbdrmd9cNArnxwDABv-jSFHUxwXmcf-FKzU9Wjizn7CLPfG0g34YWrP1CJBLiBdZC5DGoVglwObZLdhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگااام ریخته این اولیسه عجب چیزیه حیف گل نشد این برگردون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/97236" target="_blank">📅 01:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97235">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پشمام چجوری گل نشد</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/97235" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97234">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPWiJLKiqFviCp2YdhIk-myr-AFx_3nJPQuKq79D6lkHt5tZYIsgGj9ERaMpchb47LtrNgviRJb_pql-2G4RhQGoYyVfxXbt1EKUgs9djsWVEDKdsvgWrwAVN1OZ1cvK4RlkUS-4fyr5c3ml1FpjuEBBQ9zMvCRt_BzJ6tkYTjNU7bNnxNXVKwYkruJ5iYeQvVIgrL2zV9SFE8v663eadJvrqfZnxmwWC-LlPFFGhbxmFohWPo4u14yR8mmx7GY7PrzrzIhIV2KZyJ4dHUv995csECN366Ky9fp9JMyU-u_tFiConEDbxfJReINAOkZ-Ck45Ayrbx1sZalbieD6-mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مارسلو بیلسا سرمربی اروگوئه رسما استعفا داد!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/97234" target="_blank">📅 00:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97232">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ojKyVxW2AK8wOm11lFmcV1PMsg4Il1fNw19hrMjh7Ho4LF75QjkE8rK5wZUQ4sysWcaOViBhhGw408fobKJRp4qFm-ZBKd5ACJ7DEV0huAwOPDMUJoW5CUKbbNCXay5XLIddq8wuTRUNtcroKzjwLAHl82ZxBHF5NX7bU-zpZIV7gtRkVw1WugHI-sHS4qK9lulQeWfTMG_Z830M8Z7thXkOyU4EyfyVBo--SByuzO7Em1mlido3JK10JVhN3sdLc17Uywe9amDfnSp_Cfn_qZ_DRqiLh0G0yChwsB7dh54UGDDNRvQX8v_ZJQQZnGEXaZAD_hkLimEE27_Z3aQWCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AD7KZZALyJUBObMKViQ9UIXLuMMfm5hQmBejGGFLYjPtKWJGx1yoaFMJeggBD18GdRIdXrDy3m_5Yw7MqObY49J9gkVrFKBc-bzWRHEsIlyxJdl1awLRxLy00EpJ6TK_f-p5OdJfO6sEPrbKjVSdVdCm9vBLI59bOgAv_4i3eFEfAIE21Gnyb6jAGWN_AFAfd8KWtsI1KVZ0syq7a3vHmm0u_V87phdbUu9Cis2XlH62G2549jpb6ZKWiFNvold0dgNeIOAsLHvkNcSYpfDQX6ghgYYtgwgR3jyo-VUjAZARQUjI9Qvv5NBjBHv2dju9s_w7yBzoHODKeX70ixqr8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آفساید شد</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/97232" target="_blank">📅 00:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97230">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فرانسه اولی رو زددد</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/97230" target="_blank">📅 00:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97229">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فرانسه اولی رو زددد</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/97229" target="_blank">📅 00:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97228">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/97228" target="_blank">📅 00:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97227">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrT_uuxN32oua_KA9Rf0M6OEzj5N8_IwRNCnef0Blhvx7yH4ht3Z8tlblcwd6qVtTRpZF4NhS-uJXK4tmlzBvI449kxJH14S9cAz8PCiR1BknjUfG7WrlhPuCRZ7SNhJE_qBDOsQMUgaJLr-3EorJ9MVh3Z80vmxeJXvtJRHKw5IqTDydP4Ji-H11SDQOSSzgfpW4GM4yeyJZcvdB5YB0XImRzGG93IEkPa7fU59XX4fVysmpAvZPW7T1qRkHMAKjcWDmn8vfsIgCDMuNXTW0raSmsZ_B_nhXmkPVKJgSpR-UFmC-BjJgiMXOuapkxQAJ-8HTcvV9L2F0BVtcy9gmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
رسمی؛
رونالد کومان از سمت سرمربیگری تیم ملی هلند استعفا داد و از سمت خود کناره‌گیری کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/97227" target="_blank">📅 00:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97226">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇫🇷
🇸🇪
بریم سراغ بازی حساس فرانسه و سوئد</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97226" target="_blank">📅 00:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97225">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDMxjrtlhwhy2vYPtSuvgYrl0v7BnBb9-Bvo1fhO3GJOfPI6V0JxFruAmqmAak0zRcc1fY23Jjj2WbfaudvAPicG_OXqJRJcosWELhma9ScWkbVwgi9lfibidyJOECpDsmfuL0KaFd3MMyOC5vNh2rEEh3AWUw5Ey4ZNJeVpbmB7XBJGsNz6wLtmZ0Mpv_VsKHqcfBKlFY1pA_rth6E4dt1TOF80yO0A66YUj-Vv3B3kICHWCd8LvJimlsGbHkCZ8zsqHJEgXD9yE2JXQjNFaRMw5Q9I6bem45m23WRV2f8_yr4CjKvGPHTgeVfcXv4mHGciDwhvJWPlnxDQV-uCdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
با اعلام باشگاه فولاد و برخلاف صحبت‌های رسانه‌های فیک‌نیوز، قرارداد یوسف مزرعه با این تیم تمدید شد و خبری از حضور این بازیکن در استقلال نخواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97225" target="_blank">📅 00:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97224">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIP1Cz3v5GEltKlFfZSz14g_P07jAwe7swwHrXMfb_WHbzHDUOAW-iXtyVGdlr67YzhkCp6AdQic-bmYnLGZoB5SYYALkyVtZiluMveYiw1KnktoPKGLfbawONoTSjenSF0_EnbK-13y71Mc9OzPrLpaZg7yUyXUA18FE_9AV7usVcQi4IKgSv-oOwUaUm1a5pB200VtnHoYs70aZc2m2WMugn4vdOrxBl_T_RrmyLuqTwHI-dlba8_9iAUCXjdImsJak-Wp2a8Ad_AJHMjMiqBvbBAq2fy2RHfWzl_hZvCcWiWUvBqy3992T3KE4Ft6dj-OxshTXN0p74wRhbd8YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمار هر ماه 16 هزار دلار (2 میلیارد 700 میلیون تومان) به هلنا دخترش نفقه میده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/97224" target="_blank">📅 00:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97222">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGr0SOMqugm1eHyrvs9ehelp785wVmVLUWRlzcYpckfEQ6mbxey8BxAiJH4qjAF2SEtIakLsp31spzMzC68zj04trJ7WIMNTzBjbvVrZLb6P4TnVYFSokqAFoQppQWBgNqd4qJF4BrT1AnzCjpiL4o5v1oLCX9f17FdrV8GrnesOrLRQnIubvwKSmhyhaAECevhcL9oOSOnvVO4xm_qt2e_vYzWz84W3_mHEAw5ewQ0lljOWGywt3MzkLXnYlA5rAN07n0kgDtOh66MhFSaE-LcGznrTcRcSZf0sAZgBuM7M0dPSR8T4OckhZ0EKUcAHRcichfjQxvdqF7lrAABHOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d668_lO6G15aBgxEjWQSOYoOFFAx6T6Hxp-qTGZ8O09e2cC3N1XVLHjDjnpgav_iFRqJYQwXyZZbs6q1e2znlZB5bhw079WAXdE89Xl2rLF5UOM6zPMKZaLAfM9XjCJacbHB8qPcDpAlJX0nuj_etf_1fD8r-RgBb_lbpFQ5rKJuqcvZ5dHzQJduDpOZAeauNn7AEr49js8qxYkNEd7R2hhJPKQCagqe8nBobQTsgW2hmYgIhQ3MnTyi3LuK5A6OeBUMCI2RLqQX2cZdl7J8CJh6PkGLQPPhzBcmXIFMaj0a5kjLt_d-ocny9MtSagtsJxUfJw8FkMtGQfDXU_V6IQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
بدین شکل
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/97222" target="_blank">📅 00:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97221">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JapbjwxGaNbd4obN_oPd5l1eaG1dWU9D5kGI7J1pHo1TO4B4c_7JZU6Qqilzn39Sjt3ZATpX_AmUsIDE3AJ_T-tYWJjh-672AVNn3jvh-Vc1TZc-FIKFEcLzrnOWDqesLZr-1ayufn-tAmVjfyp4p8lYrz0DZggnZOhBIWNdsAqDn8S-pB7WD-SwgDJsE2Gj1B0dShaWNww8F_fRRFcXI9xCFUtq_N66byFFGpweSgJNQswIlXgOmaMU6WYCs9UDwKS7X1TkibiNReqf2D0h-rJDp2fB6sIvLhJRH-9e1a3cGeSycmiR0KbLMiHxgSi2Nf2uEMqiICguCWBYWJ_eGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
قلعه‌نویی: خوشحالم که بزرگان دنیا یعنی آقای مورینیو و تریلی هانری از تیمی که من ساختم تعریف کردن.
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97221" target="_blank">📅 23:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97219">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pTB5wXLS8871jvFnEpBKEWsJ0vUaAMAbTPOmAu7wHiyMsfdwXePjywgiTRwTQAoVtFtkWiIaOCm_23b1bpqoY-8ZGUAGahe_2DEj9A_whZF0PuCi8J3MEQ2ktrUbfzQ6bLp5dgACRqBSBws4jBilzgFfIt-bjtgSfTYWGwyUcxlrS-psg6psbM1k2Exgc68ktB-_GkTWe7pPJw6LZV8ub6d_xh6OTddkvXIcLRTgcxRNAUkIgsp6hFgG2S7iPhdh6sdj8edj6rbPvhmXwlJqVlOMUqy1d_SqdtF6XiPjnHRkHBH6Eie55C4xFHkJpNm8MWSgWvzmUDC-RXOJpnSxTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VCBtYUbyzN1z6UErDfLk7_yAv8mXBQ4FTyk7VsswLnOQmzrnFKuow9lATdQ0MKOnvIYSm8fp1s05C6vA1lDZPghgbHhp9JDyZcKwLR_4I1-h1qK4c5tlWjxS-q_gu-zVkgfBNbF0KEpS99W7K6rUCe-851Mmi-lRY3z-gzAVh4qwAHDFNeuig0yrwTIAYQgxXGhqBiSTiA3_nUvvspX5FHZvxEsnucr7SechKLNnM_kWxNfheoRKNovDlo0VP4qAkstMzekj8rw-xAVvjdsc9D0rlNOnDg3NVblDA_s2PGzQ3svovV7o_sR9mATbAUWiqUZTTd3wgCvIicko-Z_IYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
رسمی؛ از پیراهن اول بارسلونا برای فصل 26/27 رونمایی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97219" target="_blank">📅 23:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97218">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=q3nnVT2NBhoDeBTyoUiPm0Yh7ueWmRZgVjUEHRHpyC7CHjsHdZEpooxpEta2POZeycQIRgLeC4aEduxMkptUscjAqPK5IWu0dgXOORuvrSiBDFuN6efKc-rs5StnoGeG-3uCQHaYmxOs4A87902bHTqvGuFWmI1m_q_qF4aZzZf5pv6jooEsJmCKHooQwsFiXa5mO9drxz4VbCOdyD7UFmS5ocWAhRQ1r0_dx_7y5txODx98LBuoIbGL5vkpDiuAnWmBhpZvTQuRY7GK_ttiABIbjx7vWtAa4f2VIX6fgNJS9IlCqd6XPqA5Px7hIimr3-stBECA-Q-tRgbbIJhWsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=q3nnVT2NBhoDeBTyoUiPm0Yh7ueWmRZgVjUEHRHpyC7CHjsHdZEpooxpEta2POZeycQIRgLeC4aEduxMkptUscjAqPK5IWu0dgXOORuvrSiBDFuN6efKc-rs5StnoGeG-3uCQHaYmxOs4A87902bHTqvGuFWmI1m_q_qF4aZzZf5pv6jooEsJmCKHooQwsFiXa5mO9drxz4VbCOdyD7UFmS5ocWAhRQ1r0_dx_7y5txODx98LBuoIbGL5vkpDiuAnWmBhpZvTQuRY7GK_ttiABIbjx7vWtAa4f2VIX6fgNJS9IlCqd6XPqA5Px7hIimr3-stBECA-Q-tRgbbIJhWsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
قلعه‌نویی:
خوشحالم که بزرگان دنیا یعنی آقای مورینیو و
تریلی هانری
از تیمی که من ساختم تعریف کردن.
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97218" target="_blank">📅 23:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97217">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgEFkRx1sInTGfVWZVeSbWJZ0TMc1hd243a9itA1UsKp-CiVpBn5MWJJFN01uF_Th2mOuwpqnkO-7nDhi54FR8Vb-BBwFk3Ef9j_KNHZRJon7mgMdSoo3bE5sPebwc0hu-_O8RGClqJNEJrpCnKrrUGUlJjNoM_URokI68OS0wOCOLg8dhwYHKATHBYJSZ4JY9Woe67HTUuAEqY7AGcChX1BpxvD1PobzqeClcdqK0OanUpbbYXNyDxHEwRHpNYAwCem-UvZvEnqm4AjM5F8oQFA444FX77qwCWwRza5HwrQwgXABe_sxwLobWqVM99IKuXC6Tu2mnS46_10ny7oQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند در ۱۳ بازی متوالی برای تیم ملی نروژ گل زده است:
⚽
مقابل اسلوونی
⚽
⚽
⚽
مقابل قزاقستان
⚽
مقابل مولداوی
⚽
مقابل اسرائیل
⚽
مقابل ایتالیا
⚽
مقابل استونی
⚽
⚽
⚽
⚽
⚽
مقابل مولداوی
⚽
⚽
⚽
مقابل اسرائیل
⚽
⚽
مقابل استونی
⚽
⚽
مقابل ایتالیا
⚽
⚽
مقابل عراق
⚽
⚽
مقابل سنگال
⚽
مقابل ساحل عاج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97217" target="_blank">📅 23:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97215">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tN7A9bmLIQk2vgMX0DPJKPVtR6Yiqbx6YLoZG3pxKPCOpJQoaION9ZauC7g1AtEPP1Ba-Y1qr-iRnnBXW-ELMDscZJpHN7rLVUX2gtO-uw8CtHKwp118zLqEj2KFO7KDCpkjZ5YSH2Lk5qw3QePCa6m-CiCLurgJqxejtKYGExjCG8-JdqN50pb8gG3gLRS-822x1X_5KKUFGoVHXgE1QZSvdpWtAVF6tmu4mz07y1EkCwADi5rJ54Ll4zpgsYfLnRjRJMKW7vX8nwdZCnXip1vLoCZeTfuWDOQqbmwJteCydnJGSbKi7B2pVA7Aek-mBkMnsC6Bd07m4ckNTqyRDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dxn949V6qoiR8obhpgFW6VTMGJuyjl9-Ee_UN_oqynjkC28cFVu5gBz7peDyQY3NePC4X7AX3XYEunf-EAmmHKxD4wJGFAjHIg9XIrDlEfTdsmfuC8dBPupHhOvOVcdSSXTWDPRHEJi7J2DeoaSfGpCV_qUXae0Q1xVVE7emnLgDh0q20Bv4JWuQM3pALFeVDxxepSRyt82K0EUAumyc4zvYPfaOt4RvT-B93U3sPyf9CeaYIRzahdoplp73X3eUSoNnc22PG7HGSQ_FQHYCz96Fgl3LdBsYpE5G2T2auy58ib1kunivs2kUUS_5SIaoAhz8OJTO_EQCTOmav9I3Hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
🇸🇪
ترکیب فرانسه و سوئد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/97215" target="_blank">📅 23:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97214">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c96ecc5660.mp4?token=Ui6jtoJ4SxyOc8GnfP1mpsHTLtr1hZH3TOF6MZsNnE-zNOx9oZo0UNPdARgCkRavZgoT0nIiv7AT9thGGppsv9xwItOhApqUGrjQic6EmL2x2AfDW4rRzd5UNQU_n3VMG_Mc0-zP7jUZcTfgUMQiCvqF8QKaKJ6Dm8K4SH2l_i_mB9Y4eHKjENFkZVQoKJJudaX8FN8G8pc-AnoBvbSuo-POGsvn9Kclo8xdwETFB7QdA_DT8U__NpWD2_wK8aoBlRIRuNyc7sHYKPBxn3hsE7H5Bklxm7OtlXlDfRiiK6MpZ1Wmfhej2I1CLpH8dj5QrX02ysRCs7sb4NH7rKOkZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c96ecc5660.mp4?token=Ui6jtoJ4SxyOc8GnfP1mpsHTLtr1hZH3TOF6MZsNnE-zNOx9oZo0UNPdARgCkRavZgoT0nIiv7AT9thGGppsv9xwItOhApqUGrjQic6EmL2x2AfDW4rRzd5UNQU_n3VMG_Mc0-zP7jUZcTfgUMQiCvqF8QKaKJ6Dm8K4SH2l_i_mB9Y4eHKjENFkZVQoKJJudaX8FN8G8pc-AnoBvbSuo-POGsvn9Kclo8xdwETFB7QdA_DT8U__NpWD2_wK8aoBlRIRuNyc7sHYKPBxn3hsE7H5Bklxm7OtlXlDfRiiK6MpZ1Wmfhej2I1CLpH8dj5QrX02ysRCs7sb4NH7rKOkZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو بازی دیروز اندریک بسته آدامس انجلوتی رو پیدا کرد و به همه تیم آدامس داد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97214" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97213">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خوشحالی معروف نروژی های بعد از صعود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/97213" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97212">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0f902f8b.mp4?token=fN1NEWNi53gi4KB5zsH2-w8J-7nr0pBx-yOmFfzMEld8HpS0GRk7boL8jr3bN0UEgsB9gPmeoqbwXp7QhK0NH3oQVuTA4jnZZzP5rS4miFBEUUcg9Y-RaOcRt5Yu-xiv5yRXYvRSTdDgsfqksKfn6nC6MQsnlJe-FkPX1TTEASQT9IN2TSVC5or_W3hrf2AeMTRpnoR6TuS60YpYvENjyzGYN0xLQxIATPgO5Sw18bhyCSLR2yOvtz_2wsmcEDlV8729WrSG4MFIXtxqJFjbPo0BB_C-KeD2cLunxIYLvBvFkwgDna-eHGXzW5VVsDGbgwUGt3UvhM3UgzftYYBOn338KCCfb7yaM3xeYbi9QE7xxRqsZZ7OUriof0149QBRWEkWqkGOz4HWdczRnki1k2-4l_IiUOloBz_Q5vhVEq2XaznbOf4Oa4pOALg6dKfOYtZTrc7Rf62TO3bRf-fxXyEOrp8OQfpcRGxh0a8sznvJJGdfl9Yz9U1Qp9SlwwbyUn2eqhmj1PwsqYq5iEgkK-eM7FEPS-VoztEhfCmiAG3FTMxdDiDj14aC5tHsF7ZUWPr3UKv8v35m7phlgXfkHg1FHueTGj2imcTQlJq7s5lMqaf1oU4PtNpJ10QDeVgQJpverKzQ8C2l75Z4P6x-A9YgLi1aqYDwgw-yADu1MSc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0f902f8b.mp4?token=fN1NEWNi53gi4KB5zsH2-w8J-7nr0pBx-yOmFfzMEld8HpS0GRk7boL8jr3bN0UEgsB9gPmeoqbwXp7QhK0NH3oQVuTA4jnZZzP5rS4miFBEUUcg9Y-RaOcRt5Yu-xiv5yRXYvRSTdDgsfqksKfn6nC6MQsnlJe-FkPX1TTEASQT9IN2TSVC5or_W3hrf2AeMTRpnoR6TuS60YpYvENjyzGYN0xLQxIATPgO5Sw18bhyCSLR2yOvtz_2wsmcEDlV8729WrSG4MFIXtxqJFjbPo0BB_C-KeD2cLunxIYLvBvFkwgDna-eHGXzW5VVsDGbgwUGt3UvhM3UgzftYYBOn338KCCfb7yaM3xeYbi9QE7xxRqsZZ7OUriof0149QBRWEkWqkGOz4HWdczRnki1k2-4l_IiUOloBz_Q5vhVEq2XaznbOf4Oa4pOALg6dKfOYtZTrc7Rf62TO3bRf-fxXyEOrp8OQfpcRGxh0a8sznvJJGdfl9Yz9U1Qp9SlwwbyUn2eqhmj1PwsqYq5iEgkK-eM7FEPS-VoztEhfCmiAG3FTMxdDiDj14aC5tHsF7ZUWPr3UKv8v35m7phlgXfkHg1FHueTGj2imcTQlJq7s5lMqaf1oU4PtNpJ10QDeVgQJpverKzQ8C2l75Z4P6x-A9YgLi1aqYDwgw-yADu1MSc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میثاقی: به مردم توصیه می‌کنم در ایام جام جهانی روی مسابقات فوتبال شرط‌بندی نکنید چون پول خود را از دست می‌دهید / در فوتبال چیزی قابل پیش‌بینی نیست و نمونه آن برد اکوادور مقابل آلمان است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97212" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97211">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🔥
🇪🇸
زمان برگزاری ال‌کلاسیکوهای فصل ۲۰۲۶/۲۷ مشخص شد
💢
بازی رفت:
📅
۳ آبان ۱۴۰۵ (۲۵ اکتبر)
🏟️
در ورزشگاه نیوکمپ
📍
هفته دهم لالیگا
🔽
بازی برگشت:
📅
۱۹ اردیبهشت ۱۴۰۶ (۹ می)
🏟️
در ورزشگاه سانتیاگو برنابئو
📍
هفته سی‌وپنجم لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/97211" target="_blank">📅 22:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97210">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hhie2HTuS1dwLFpEs_cxPGYdCBhGlT72EH_7B4q67tvnc1DNspPh_yuV9C-r2YfT58HBZRcNZyebZ3f_zSnKODeQJFM1CJevLSoiJbLMg_HK-wvfv_5pMP_tNEsdNSHBgjmtsc5Dokk1gvnIDWwn1-T6VkPVEYKketWUSnOun1Z4vmtdnpoJmwo8VbWLu52FG28JVj71vvjwnNGrCwlR6i-8wiPUChquUg5gjbi8W_5cip1J3TAhXbQNNsZccnHQFHn6OC71vltfR76qYHSxrsOh0ZPhVCO89fJFK82Uj50zeEnkpZLq_OiNqUpDVL8SoHRsU2rD65ZyK3LWzNoGQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔥
🇪🇸
زمان برگزاری ال‌کلاسیکوهای فصل ۲۰۲۶/۲۷ مشخص شد
💢
بازی رفت:
📅
۳ آبان ۱۴۰۵ (۲۵ اکتبر)
🏟️
در ورزشگاه نیوکمپ
📍
هفته دهم لالیگا
🔽
بازی برگشت:
📅
۱۹ اردیبهشت ۱۴۰۶ (۹ می)
🏟️
در ورزشگاه سانتیاگو برنابئو
📍
هفته سی‌وپنجم لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97210" target="_blank">📅 22:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97209">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rheJGnX0YRmkSgbKq5RR7P9_DyaBo8K9D3d7n5HYgxnn8QHrnc0-5KmWCpcCM_t5ZqVv5gOgnI_TWi7zb-tlKxrNZSq8j_rvB77gT9bNrep8NbWyJJLk2t5XE5NljsHHDVBJPjrJmn2PTSlZTeAcqiIIQxX4iGfNMHHJqVjeV5TAO_bw4Xtm8gAe-sznbocwMmLfX3bip4-u0eq_c78mylFb85bdRX4jzTKH3hpnf5LSTVxocCYmjsEvL9VznVAAdQyPr1gU6jduuHjoaJQxm3GmNu9Z6bN1MSMGqHfPhEPF_J1F_6NRAIW0jkcqLGnncMkj3z2nXVH8d-elHBdEyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود نروژ به جمع ۱۶ تیم پس از جدالی سخت برابر ساحل عاج؛ هالند باز هم درخشید!
🇳🇴
نروژ
😀
-
❗
ساحل عاج
🇨🇮
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/97209" target="_blank">📅 22:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97208">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtcNVSqjxCmEvwtiN-_Ae7vNMDzDajsz5th5k0SGLx7N4GVXFXq-9kEiTFWMlaWkVAIAc-16F1dDyqeNpL-wfgzTjRwOFhOJquBoI3yGfh_biab6gDVkDjjKgV-yD0cVQJoZHVdk4jvyI5LWbInv3b1WpC7Gg95VLWjRNdGUw-0fLupQSxC3AxGF9kGN52Afn8NsbD2efVNuW0xwJdv0QTNwQPraUbkg-do4CRpq7bkc7Qm_7MU7ztRiGCRiUxaLVkpybwSxdgCOq3-lqfFteZMgI-eybwV0GVTEhA_qKOtfsl6N3JzWuBOOboFMgn1kNl46GzATLujfYOUvcvMEhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود نروژ به جمع ۱۶ تیم پس از جدالی سخت برابر ساحل عاج؛ هالند باز هم درخشید!
🇳🇴
نروژ
😀
-
❗
ساحل عاج
🇨🇮
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97208" target="_blank">📅 22:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97207">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ3Z7oI-Tf7dGUritCdWRNfeZcUyVWQ3eGAjZlalLBqCTja6pvkbZ_idzWxg_gFKJxkq4-HeRs7BMonf5w1DYOEanAGiwyZJ_Gt5Aq4CkhsMUNt7p6d_Ke4T0uWGfWU206G9Re4m3K3sdBzBNq1ZXgZKv2e0rk7smlZLXLAmQVEPmOLZw3mRRt_qnv6v19iGWm-y8QdqIMwJF0epxCP5FNZnEFAw2fdcmhKcw7-5_rQRf8bcVNy9Pa5vZCMjQOnLKtiyu0A4OxPXRs8TXl_pwv3wRQP_o4A6_Lrl837AmIQ3vKkPfUalQxZ7Mq0dNGlwGz4E5oZF5smb1hiAR0itQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فووووری
؛ برنامه هفته‌اول لالیگا اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97207" target="_blank">📅 22:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97206">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇳🇴
گل دوم نروژ به ساحل عاج هالند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/97206" target="_blank">📅 22:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97205">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">هالند بازم گلزنی میکنه</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97205" target="_blank">📅 22:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97204">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نروژ دومی رو زددددد</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97204" target="_blank">📅 22:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97203">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/97203" target="_blank">📅 22:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97202">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4771a77adf.mp4?token=rE9o9zIS67SAdbepAjpsW6PV3UWWP70S7Pw_uWB0tBtIFCyul2N5RVod0e8HsV1UDn9OZsP62tg3kw5lGzacgLkQHBVaijwV4Y6jnf-lJEygvIOsbHwq-lAIS567E-Liq1cJF7NbKTqdSIYfjOVCD0TP8jvMi7FgmG9NZnQnLdUKq5etGy5_qu0M9ejvVotetwRZph51z29P_d3zAv-Z-JDsPorFaO6U79sY8Ky0k4U9H6N6CGhw1t3PK749pltTtV_iODK6vFypAgxzyR3sf4t-HD_N82NMYiABY0sKp0IZhNN54uhhiL0WD5zquZt7rs1bjG0Sjtntf5SKd5fZa6jOmoACcFBNAcchCscVUDs7Rds0h8OmHczHhKNztVvxI432l47HPEbmvkGnlJXyVFexZ_IaYwdqrbUBJUyo_JctFWHOO68QJ0rGa7lKV7VUXdjyxYk24M8kMbY7gSJxS30kjJhhzm7m5fVlLluv2-WdPjyGl46lWEddDABTaYHjfbqq0iG4Oe8R7R1bbkiR5FwzlzdOxR3duY54-qmHGbId7RHnUZNqb_5eQd4NFoDnjGVJvl5HAPFMBA2WMJrJ1K-49Hou4nucTSizBQWhFMJnTlPmg1hkPOvH3nhhjZV9zV1fCDhh2TNWXFpzI7oJGp8sXItm9OKOOi1BtPTaqUk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4771a77adf.mp4?token=rE9o9zIS67SAdbepAjpsW6PV3UWWP70S7Pw_uWB0tBtIFCyul2N5RVod0e8HsV1UDn9OZsP62tg3kw5lGzacgLkQHBVaijwV4Y6jnf-lJEygvIOsbHwq-lAIS567E-Liq1cJF7NbKTqdSIYfjOVCD0TP8jvMi7FgmG9NZnQnLdUKq5etGy5_qu0M9ejvVotetwRZph51z29P_d3zAv-Z-JDsPorFaO6U79sY8Ky0k4U9H6N6CGhw1t3PK749pltTtV_iODK6vFypAgxzyR3sf4t-HD_N82NMYiABY0sKp0IZhNN54uhhiL0WD5zquZt7rs1bjG0Sjtntf5SKd5fZa6jOmoACcFBNAcchCscVUDs7Rds0h8OmHczHhKNztVvxI432l47HPEbmvkGnlJXyVFexZ_IaYwdqrbUBJUyo_JctFWHOO68QJ0rGa7lKV7VUXdjyxYk24M8kMbY7gSJxS30kjJhhzm7m5fVlLluv2-WdPjyGl46lWEddDABTaYHjfbqq0iG4Oe8R7R1bbkiR5FwzlzdOxR3duY54-qmHGbId7RHnUZNqb_5eQd4NFoDnjGVJvl5HAPFMBA2WMJrJ1K-49Hou4nucTSizBQWhFMJnTlPmg1hkPOvH3nhhjZV9zV1fCDhh2TNWXFpzI7oJGp8sXItm9OKOOi1BtPTaqUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇮
گل مساوی ساحل عاج توسط آماد دیالو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/97202" target="_blank">📅 22:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97200">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ساحل عاج زدددد آماد دیالو</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/97200" target="_blank">📅 22:04 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
