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
<img src="https://cdn4.telesco.pe/file/M6Ie8xSixTc1Aw5onol_Ny4Z6LVAEz6I9lsFxDZW1crsh6AIbX2GeYg89_7fUnrEH4d4IxftbhAVwj8w6QxW8TMVhwiIzyMbsEr06YSKMGkEfqBOe3OzO_xzBlHHFxxbzh67hZB_BzsdAvYRGnxV9AAqa0shOW40QcSmz0Mp1fPK6iRyX09ctWIXIx0W_wkFlV_YIeIFZ9QysLDwBIhSxAmMI5yRE2HzeE6Ir7swtADjiFbvywEfk1twvbybh8ukKTyQm0X8cB6fW-KCOeE6Ap6dgeu1RMfbVj8hUF-gY7w_RgV0_jokmfsm5LhEkFtFCRkR1547hEOU4NV1HqsWFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 925K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 01:19:51</div>
<hr>

<div class="tg-post" id="msg-132358">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
مقام آمریکایی به PBS: «ایران به‌وضوح نشان داده که به هشدارها توجهی نمی‌کند. ما در حال افزایش شدت واکنش و فشار خود هستیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/132358" target="_blank">📅 01:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132357">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از مقامات آمریکایی
:
کشتی‌های جنگی ما در حالت آماده‌باش هستند تا در صورت تصمیم رئیس ترامپ ترامپ، بنادر ایران را دوباره محاصره کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/132357" target="_blank">📅 01:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132356">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=t_KVOi9rjaukuA3sp7KXn9tQes1zeyoU1NMHyfWhH0sN8Hlnrm5LJW7c7x17PHRF5K8lkml2WV0dGygf7DFTy8wTQQhAxMX8D32r4wqziJ3hn4hQ-HSdHc-1y0NDxL3g-DTNIuGo39G3mUeS3dqGYjbAFdmkLr_oMBuqO4fzN-jIUQCsKakrteWb_zltVrEspjnOYd9xbUa5vK82lO6ASbQYXQqaiJB2Z1130SSzXtJZpFS_9-MoRi6Ev18rpB8h6UMAWF5dxWFImS3A27IRJHGBu3xBRCaNQ0vRNmEhtxqCfSGcYMgyUT56v2LcNkk9bDXlHiQL_QudEZN502RS6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=t_KVOi9rjaukuA3sp7KXn9tQes1zeyoU1NMHyfWhH0sN8Hlnrm5LJW7c7x17PHRF5K8lkml2WV0dGygf7DFTy8wTQQhAxMX8D32r4wqziJ3hn4hQ-HSdHc-1y0NDxL3g-DTNIuGo39G3mUeS3dqGYjbAFdmkLr_oMBuqO4fzN-jIUQCsKakrteWb_zltVrEspjnOYd9xbUa5vK82lO6ASbQYXQqaiJB2Z1130SSzXtJZpFS_9-MoRi6Ev18rpB8h6UMAWF5dxWFImS3A27IRJHGBu3xBRCaNQ0vRNmEhtxqCfSGcYMgyUT56v2LcNkk9bDXlHiQL_QudEZN502RS6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ما که نقض نمیکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/132356" target="_blank">📅 01:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132355">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlCO67nuQFhuYmNa6hjYTbOlahWFXnymf__gCasXC467xEMI4tHqAL5e2EXDVO8uxqresPW3sWfSm3nM5fBZGZLItzIXBIN2sWWP1y6Lr7vHOEAckUW1RlP1vUF5BoJ8kwr-EQX5tparTga8JOuLFQ8ujoMYolZe497opBvqJxhvibKxZ80qnnL7nzT4pLOzLvZCgjZ8_Qfli4pMkTZDtJGn-tgLeMbfotf2E2tjSz1vJJUDx8z5mgXMpxF_KInDSA_LeB0COCD6bo2CmW7iiEESTo1pGxveQ80B45msYIXZgZ4NO3yvKvvUtUlzylxJaxlYprDwPvqyXMf2c-RfhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پنج هواپیمای ترابری سنگین نظامی آمریکا شامل چهار فروند C-17 و یک فروند C-5 از پایگاه‌های آمریکا در اردن، بحرین و امارات به پرواز دراومدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/132355" target="_blank">📅 01:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132354">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6xj0IjJUrRv4ppV296q8e7a7qgY_9O2Vw5ZOiriKzLAp1S73wC3U3nWqblupBVqgmq6EEg5DR6cMCSEUIq8o6XmfKO8UrJ8SfcQpdIcpHsjLZznQ1ukehkacwphqEvovjaT76KQ1yEizjtR2gpaukCGE-qChXKs4OKvDClYzeWtx25VoccGZlpgxIPuNslfeADVUR-stuPH_gfch8n-JToq1tC1NX45tCa8-QhJaRwWFwckdhnIqhH75wdoy6ZT8vtchakfzKgzkmOjCb_LJp0RTFXrK8NaOtZuvSiFhxsgSADiBzZosHMjpChC1Gs0_BKB1DcS3VsvgCnnlWAfwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار مهیب در
اسکله‌ی سپاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/132354" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132353">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDeeBa3c9vIDZl9gnFeYXWN85LSNJitRMrauhHolm9jv3k1K9GhN24LfFttUtiPIFvKS-qw7IL8zWjmSMa6W6mremiWSyte00ThoefKythIa5n503Z_YtRCrFYXwjhZqnrrpIW80TuXfOKKvCKGk485oLRURFOTgacskefRG8Py6LMcnNI8bpEnqxz9U05t_AxK5MRO_MGEZdcbrbC6UfO6pCLUrIj4409xiEq0zxsz-A3y_xZQrJLRveWIkrYDHT2Q9QNt4Maa4aFyjxb6w_IvLA23iNpAd05svhR0yQKGu3yddjLxR4e3WsQokfcZYuhNW0RNGeW8n5dLBsV5CpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش اون دکل مخابراتی توی جنوب که آمریکا هر چند وقت یه بار میاد میزنه میره :
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/132353" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132352">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
بندرعباس 11 انفجار رادار های دریایی اسکله رجایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/132352" target="_blank">📅 01:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132351">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
گزارشات تایید نشده از حمله به نفتکش‌ها و تانکرهای سوخت ایرانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/132351" target="_blank">📅 00:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132350">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
حملات همچنان ادامه داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/132350" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132349">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سنتکام: آتش بس همچنان پابرجاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/132349" target="_blank">📅 00:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132348">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eR_6dIkrX1uhXukK2EGKANnWEXQukyTANRHxHfIuPsLuRXG2hG6cBcoDptoSLgGd1oK_1RewtWY7xcsq7ijGRTOyglvKmfqfsxMghZfSmtbD8RShLgG6M911NA9JZqGHFBlW6Kiz_d1dlfHT_iw5XhXn07IHo9chPjfJvukMqOKomFikWWNLCPcoGHKo_H2sLQJS91kGzmoIu0K8Cw1Sq-Ruvwk9qAtC2H_sq9lsLypsPjn4ur6jTzgwmUKlLnN5O3LhtfCgcmFsr8KFGcgR0jtht0Z07_U2rVtwmxN-DSxFUvOx7EGG5utu9ZcIUvdRwnPUn_NdJfBq8j91Et9a2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام):
نیروهای فرماندهی مرکزی ایالات متحده حملات قدرتمندی را علیه ایران آغاز کرده‌اند تا هزینه سنگینی برای هدف‌گیری و حمله به کشتی‌های تجاری که توسط غیرنظامیان بی‌گناه در یک آبراه بین‌المللی اداره می‌شوند، تحمیل کنند.
این حملات آمریکا در پاسخ به حملات ایران به سه کشتی تجاری است که از تنگه هرمز عبور می‌کردند. تجاوز آشکار ایران غیرموجه، خطرناک و نقض آشکار آتش‌بس بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/132348" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132347">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فوووووووری/سنتکام: در پاسخ هم حملات ایران به کشتی‌های تجاری و نقض آتش بس، مناطقی در جنوب ایران را بمباران کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/alonews/132347" target="_blank">📅 00:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132346">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوری/با حملات آمریکا و احتمال لغو توافق، حمید رسایی دقایقی قبل ارضا شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/132346" target="_blank">📅 00:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132345">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوووووووری/ترامپ از ترکیه و بیخ گوش ایران، دستور حملات به ایران را صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/132345" target="_blank">📅 00:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132344">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فوری/حملات اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/132344" target="_blank">📅 00:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132343">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فوری/انفجارهای پیاپی در حوالی بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/132343" target="_blank">📅 00:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132342">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری/با حملات آمریکا و احتمال لغو توافق، حمید رسایی دقایقی قبل ارضا شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/132342" target="_blank">📅 00:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132341">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
فوری/انفجار در بندرعباس و قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/132341" target="_blank">📅 00:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132340">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوری/حملات آمریکا به ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/132340" target="_blank">📅 00:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132339">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgBYhSb4X-FKWHKJjfJX4wZEqYBf8QXinYKPBFy32upLns4Q9Tb00ss7koEn0MxC8JmlkZI4d3opzSRrLnAAZqghSo7E5JSDteTO5kA2FHQU0L-wBtCDkLBTRcQ-opuIH3FeFoqzU0TDpBqV5BhoGJ2pa4H3NkUVcdDdtZZI4lofoxTNlt6H-SN0QAGsL8vvS7xIT3Sk7n8QZmuuk1F2U4D7RpsGgDmz23uOkhD8f2ZYD72qmv1q5asYYSiu8XB8h5PRi6huzyzeaqF3ga0K_ivzIqdEwAT2ie6bRtfm6s0eJAwsmOWcHxFQzwtaMnmFMRKmK0iHO2hl6hbNPsAQ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محل اسکان ترامپ تو آنکارا هتل جی دبليو ماريوت تو طبقه 23 هست
🔴
اگه انتقام میخواهید بگیرید بفرمایید اینم‌ مختصات دقیقش، یا انتقام بگیرید یا حضرت عباسی شعار معار ندید بزارید ملت زندگیشون کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/132339" target="_blank">📅 00:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132338">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kP1NVQCjP6FM0ZpbyIihk9hruno7uaNe0r3OeKMVFhxN7ECR4PRYd6JBXGiwscH8qVNxXfyW9XqxphtYOBI7HQpp6bOT9g7ZrGo9fOgEBYBSjJnBeJT9LMYi0mE0FiTlTMyIUM2kRHBNl7OKVXjwFJg5mPWOozW6Ca1NeYouP5JkU3gXZr3epwdvQozJHukoYKvxfFnv2TC2yreDivjuhe7Zbw5nWmiDUDb4qpJ2dRZPl1ypZLvvLoVV_lhzjysP1Ev3RJWd8hvyitsxhYA5N6SK44-hwLsPmS3hlEcMMZWtHg5D849kZMHOTTFM7KXsJyt4t0Jyhw-xRmUJnayNwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری هادی چوپان
"
یار سفرت بی‌خطر
"
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/132338" target="_blank">📅 00:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132337">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBg01GZIvLdR-LhAWKEjI5_dOS0oD72acJGHugs0ChpV9ZG4DZIELJkZNmyk0wyOiB5GNvfL0hJewqNyvQlHOmRkLpJUDhm_SNDjEHhR7svtLYyhxxGN1mHOyEBaPiR2QBR5-St951N20T9a2auptW1LxUn53x4tdKAM4NYbmlj6pFHLb56OUe5skuH7rW61Iv6izg-16fyqEFrL9GHlWaPORV8rRrevB9ZdNklNx1VxDcOVW--HiLAgmfR9FlTEwhesBkZFCCls9iIuJoxHKibYzsRfdX6Gxlwl1mBkK3vdN98IE6nBT0_vE1o15K9IQIfnHxILuOABpgJhuSsZVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شب و روزگار خوش
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/132337" target="_blank">📅 00:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132336">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">💢
فوووووووری/پرواز جنگنده‌های آمریکایی در مرز ایران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/132336" target="_blank">📅 00:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132335">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری / سوخت‌رسان‌ آمریکایی درحال پرواز در نزدیکی مرز های جنوبی ایران است
🔴
پ.ن : ترامپ الان ترکیه‌ست
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/132335" target="_blank">📅 23:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132333">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوری / آکسیوس: آمریکا امشب در جواب نقض تفاهم نامه توسط ایران و حمله به کشتی های باری، حملاتی گسترده انجام خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/132333" target="_blank">📅 23:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132332">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
فرصت ۱۰ روزه آمریکا به مشتریان نفتی ایران
🔴
در مجوز جدید وزارت خزانه‌داری آمریکا به طرف‌ها اجازه داده ظرف حداکثر ۱۰ روز به تمامی‌معاملاتی که قبلا فروش تحویل و فروش نفت خام، محصولات پتروشیمی‌و فراورده‌های نفتی با منشا ایرانی را مجاز می‌کرد پایان دهند.
🔴
در مجوز جدید همچنین تأکید شده است که ایالات متحده آمریکا از امروز (۷ ژوئیه ۲۰۲۶) هیچ‌گونه معامله جدید از جمله خرید یا بارگیری نفت خام، محصولات پتروشیمی‌ یا فرآورده‌های نفتی با منشا ایرانی را مجاز نمی‌شمارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/132332" target="_blank">📅 23:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132331">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
فیلد مارشال رضایی: آمریکا به دنبال عبور دادن ناوهای خودش از تنگه هرمز است
🔴
آمریکا در عمل زیر تفاهم می‌زند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/132331" target="_blank">📅 23:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132330">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d9920461.mp4?token=bV_jSIp9m-djJxswgdzxHLYgsj2A2qaBj2PYBG1CFQVwIEST5tyz8LduD63djxCiANe44aJBIB3gZFsxInWkLlJntG70GyN0s5cwtH652UxPiBk3uCxDdpp9KeWpyCIiaFYvw13swdC8atvWiOQYhKVilbu8Gw7yQ6koOTbmf2tjzZZzOH4QPph5re3w1mjAaK1pRKLFJbelTEVhc0TQyXUYB_0mqtEbJmM4p4DdU3wFc1fr8C3kXCPy__Z8UD63aVfJpYQHctzf3Nk_fbUGtyo9Rgkdb7_qvvsueKE_qIMEgkQB1iFgCPY0XcTGw-_0FECbToRAjgq6Tt-lRR6c8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d9920461.mp4?token=bV_jSIp9m-djJxswgdzxHLYgsj2A2qaBj2PYBG1CFQVwIEST5tyz8LduD63djxCiANe44aJBIB3gZFsxInWkLlJntG70GyN0s5cwtH652UxPiBk3uCxDdpp9KeWpyCIiaFYvw13swdC8atvWiOQYhKVilbu8Gw7yQ6koOTbmf2tjzZZzOH4QPph5re3w1mjAaK1pRKLFJbelTEVhc0TQyXUYB_0mqtEbJmM4p4DdU3wFc1fr8C3kXCPy__Z8UD63aVfJpYQHctzf3Nk_fbUGtyo9Rgkdb7_qvvsueKE_qIMEgkQB1iFgCPY0XcTGw-_0FECbToRAjgq6Tt-lRR6c8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلد مارشال رضایی: آمریکا به دنبال عبور دادن ناوهای خودش از تنگه هرمز است
🔴
آمریکا در عمل زیر تفاهم می‌زند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/132330" target="_blank">📅 23:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132329">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbbDwjEZozu0WP_20M29k5sXm6-AU0A7OMo8mg0w0-bF4R2onSu3bv-CRW8sn0E-r39KvCQ98dR41igr4Zu-VPVyiggwnpsASxMkEpwmvdQWz5wCkZqTh2XUqU6KgxhkoGc-TvfUDNJntvmIKcD-I56VaR9lAfjwFJeTZSsgZijuaPFOa70XuzTHNZ69T-fOJ7Q0OYomOwSCaqs8Um3UDf6opAg1TPAtucUuXxRA8tZxQ5zKEe6vCj1rCwZc9IINJpjIPl6oz1CqwxzlgL4-Ev1_QUlSV0jlTpWbNg2svJRAzXKsI7jlQ6umCKrdUF-GK1jE3bacfVeEhCynmsCtAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان قصد دارد قیمت نفت سبک عرب را برای ماه آینده ۱۱ دلار در هر بشکه کاهش می‌دهد و به ۱.۵۰ دلار پایین‌تر از شاخص منطقه‌ای برساند که کمترین میزان از ۲۰۲۰ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/132329" target="_blank">📅 23:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132328">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mb2nyJTF8-io_BzuHup2N_lW5DRpUNg05PjMDbJMfJw7wmbQdtZ4AQ2DgUs5qwp2pD2Ukt2VKo76RB9cuWbJOnHwwN5ehS0cyrEILBNJYKuPTuEd9Ol8iDyplMw0uaUwKTMb6Z6U4yoyNjiritcHjf2QeeDSQC5AL-K87KAgD8mfD2_MpFa4v_YEG_h_z_lyRqzr9wIy97fcLkswxSc3x_iesPDr-zH5bq4SB9t-amIz7XBVpDSiteWb2ORO2bJCSa0RduwTpNQVarmtTdRfLKlUrBmA3Z_Eiha6XqNRgwWFjF4j5bDCTp0hhh93M9dUvNST5iWMA0TK6ahaVJzb6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراق قصد دارد از طریق خطوط لوله نفت خلیج فارس را دور بزند و ترکیه بازیگر اصلی این جریان خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/132328" target="_blank">📅 23:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132327">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
کل عراق فردا چهارشنبه تعطیل رسمی اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/132327" target="_blank">📅 23:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132326">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
قیمت نفت از ۷۶ دلار گذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/132326" target="_blank">📅 23:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132325">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
مقام آمریکایی به آکسیوس: تفاهم نامه به عملکرد دو طرف بستگی دارد. رفتار ایران در تنگه هرمز درست نبود و این دلیل تصمیم گرفته شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/132325" target="_blank">📅 23:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132324">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ایتامار بن‌گویر، وزیر امنیت ملی اسرائیل: یک هفته قبل از هفتم اکتبر، من گفتم: «بیایید عملیات‌های ترور هدفمند را در غزه انجام دهیم.»
🔴
به من گفتند که من دیوانه هستم و اینکه درک نمی‌کنم چه اتفاقی در حال رخ دادن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/132324" target="_blank">📅 23:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132323">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/152e43cb9e.mp4?token=qegK9pAYfAbdCvMK7lIH4eVLP2gF_9HPqnmMGE7fcIlgcedz_n0OJBvEQrutLIJLK_c1F8z9QA1fDhd-nF5Ash_SqkqmLrUNCNfbKG5czEIKNke0adFwkrsP6BbpQ2wBM-pmopJUXUqZSw-e0yo2YcliRLRqREtO3TFSBa9i6YX3gjoWrC1Bo_DgBdy7YGjzah5jsl9KUPnYNAU5ztejtiyD3YhrbUyetFgC0wNe0g3AVMLPgCfN6vRzUo_DP8mWoUaMCbBhTlDyxt7RoSIXr8yaOFB4s3cg3224rBdKdl74ZlxYZZBbCIBBd9_m_8tFiVU1ZMe04VTc02wGelDFk0TZG6HMD3nvjMj-hDYSQSXddZ3_lH8VJX-RPPK0aTZaNHBvXfFWjUaQ6vEMmbFmQGtHee1Lf5fNUeUFvzrFpsqcSrP2Lv4XjcrW_xhi1EwpLrrIH0csrwWEJk67Q3KfWpx3zv96iirhdiNuhuMOIUXEWgJrrr6S2z_FL93Wl2mNXmLODOh6PkNCPDgvhrMytl1eGkZ2dCXdRRjJsdGbKHYG2f4BTM-fLS7xEVhaSN2s98EI44JOSeCLIqpr3BNzbeOeTyfuC6MxgLRDBuJZxW_8F45Rkfrms8EwejcIHZo4kukPV5qCQxsCqicNRdzcvuVKmkfFIFSULrUHBwkr5AY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/152e43cb9e.mp4?token=qegK9pAYfAbdCvMK7lIH4eVLP2gF_9HPqnmMGE7fcIlgcedz_n0OJBvEQrutLIJLK_c1F8z9QA1fDhd-nF5Ash_SqkqmLrUNCNfbKG5czEIKNke0adFwkrsP6BbpQ2wBM-pmopJUXUqZSw-e0yo2YcliRLRqREtO3TFSBa9i6YX3gjoWrC1Bo_DgBdy7YGjzah5jsl9KUPnYNAU5ztejtiyD3YhrbUyetFgC0wNe0g3AVMLPgCfN6vRzUo_DP8mWoUaMCbBhTlDyxt7RoSIXr8yaOFB4s3cg3224rBdKdl74ZlxYZZBbCIBBd9_m_8tFiVU1ZMe04VTc02wGelDFk0TZG6HMD3nvjMj-hDYSQSXddZ3_lH8VJX-RPPK0aTZaNHBvXfFWjUaQ6vEMmbFmQGtHee1Lf5fNUeUFvzrFpsqcSrP2Lv4XjcrW_xhi1EwpLrrIH0csrwWEJk67Q3KfWpx3zv96iirhdiNuhuMOIUXEWgJrrr6S2z_FL93Wl2mNXmLODOh6PkNCPDgvhrMytl1eGkZ2dCXdRRjJsdGbKHYG2f4BTM-fLS7xEVhaSN2s98EI44JOSeCLIqpr3BNzbeOeTyfuC6MxgLRDBuJZxW_8F45Rkfrms8EwejcIHZo4kukPV5qCQxsCqicNRdzcvuVKmkfFIFSULrUHBwkr5AY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از حمله وحشیانه آدم‌خوارهای عصر حجری و بی شناسنامه به عباس عراقچی
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/132323" target="_blank">📅 22:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132322">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
یک مقام آمریکایی به رویترز: مذاکره‌کنندگان همچنان با حسن نیت تلاش می‌کنند تا به یک توافق نهایی با ایران دست یابند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/132322" target="_blank">📅 22:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132321">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcuv8E8hvRvbmpEptkjtRS4kYBrx6KgvDQsFKvd_o15XvjZhIOq7tVYE7qUvw9o3xG8OS71ihDfa6UF0XWXMNTNq0zY8fqvapSYU_PXWnSDnRCcKpDPQmrgeHsMX85c0FlFqSOrdia45UbHVWNvh_Rf26jXXT2Y9mLS5Chy98-4Icb_SJC3aOxOESDhKPvAJma3g7OCHjTgy90Q4-LZACJeaL2IwLt-l8WCLLywqvEfK9S2jVIBRZD_H6yzMyQy3KXdUE9MGUyMP6GW2R2QvKYp89j0E2XIuzTrovfu-RgzICCqrP9zQgT9MSMj1XOpP8bhhMaKd1AWcRJT7GHW6Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت‌ نفت پس از لغو مجوز آمریکا برای فروش نفت ایران، افزایش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/132321" target="_blank">📅 22:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132320">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrQzG3DlD0l_geyKsxNqBT9nlRxPdCYbcjZxm-Hs0RATXIR4fFVw5mOHE9O4YyvGx4qW-z9269QlUsMEai97MeahAiDR-wcelThZbGXjAdshOChuM92ILsNsh8WQNcZz7Dg3bRpMkZMnTuaRoAFrpFZEYGPaRbItDbCZLkq5NE694o6eqtjCaWCSj0K1cBHJVrK9tYumCZclQmjUd05ZlEJX4HD8_I_5phgL-ENPgDi1Yg-NvisrtHiq0uZjafr5UTDL9Ye7qpz8wvYub17zaALQlkFIYLRT6HEPx-wck5N_NIp1lydcTsvd7SvkonhxXH_i7Vfl6L5lJXdC8dVTJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت خام ۵٪ افزایش پیدا کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/132320" target="_blank">📅 22:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132319">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
قیمت جهانی نفت در پی لغو تعلیق مجوزهای مرتبط با فروش نفت ایران از سوی آمریکا، روند صعودی به خود گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/132319" target="_blank">📅 22:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132318">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
قطر معاون سفیر ایران را احضار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/132318" target="_blank">📅 22:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132317">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری/مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند
🔴
یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
🔴
به گزارش خبرگزاری رویترز، این مقام آمریکایی هشدار…</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/132317" target="_blank">📅 22:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132316">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6798819134.mp4?token=IfFSLLq5cw6JOEfEsTYS0IeBrRyVUVhfcCaWcRh00Yzgv2oySyndSFqHxf_NgNy-aQw_km9BCZcpK2nBInDoACEIGOkslm7lfBnHVAkilfEnfJCUiu7yYf-hyY2FV3Yd89GvedDhAx9KJbmhTCBimLvUyuqiC9Hf-hYm-v3128XN6QodpioadvTj_WKmonL8WCEitEog2Op7R9ZCgOM5Oh6bDGkFNCpGcL1SXshYCsOzmFTouh3Gwy_XDUmRLnvjSoqQXZWrqxKiufQdQ-tk8WX3J0hNH8jqpPFY1PL86lBOUKcqIAAFo7udZP44OgEeyz4x8McDUlONWlN1O3FgXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6798819134.mp4?token=IfFSLLq5cw6JOEfEsTYS0IeBrRyVUVhfcCaWcRh00Yzgv2oySyndSFqHxf_NgNy-aQw_km9BCZcpK2nBInDoACEIGOkslm7lfBnHVAkilfEnfJCUiu7yYf-hyY2FV3Yd89GvedDhAx9KJbmhTCBimLvUyuqiC9Hf-hYm-v3128XN6QodpioadvTj_WKmonL8WCEitEog2Op7R9ZCgOM5Oh6bDGkFNCpGcL1SXshYCsOzmFTouh3Gwy_XDUmRLnvjSoqQXZWrqxKiufQdQ-tk8WX3J0hNH8jqpPFY1PL86lBOUKcqIAAFo7udZP44OgEeyz4x8McDUlONWlN1O3FgXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: چند کشور و سازمان به شبکه‌های اجتماعی نفوذ کرده‌اند.
🔴
آنها از این فضا سوءاستفاده کرده‌اند، به این صورت که از ربات‌ها و سایر ابزارها استفاده می‌کنند، به ویژه با هدف تأثیرگذاری بر جوانان آمریکایی، نه تنها برای ایجاد نفرت از اسرائیل، بلکه برای ایجاد نفرت از خود آمریکا.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/132316" target="_blank">📅 22:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132315">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BapISnxOq_dUK7mBzkfbthAFQHi_zDanTPTCIK1kxQiZ_PafSOmDgxQPg915lAWrrWDCaDFyL-hiefckJSzV6qvSb0yGw06qzTDnBm2y-KfDsjOfokKQB8ASstm5fHr_kAEpOxohXfhH_E6gBHXX2dO3tRFfvuDtRRaxwOly4prUaqNcvFJmUonGkO-bkSIQM_QbXpmw-hy2rI2adQIyIEglQXvoEs2vHD78L-iPc_qFMLGkGGD4xKyRvu0cLtyQqLq7bWB8Ik98TUm5AcssuPdD41GfI7o109ICMDt7GxfqZ3catDVt6_qwPdEBmJ9VY-HMSYGbsNf2qk3DXpVyZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز به نقل از مقام ارشد آمریکایی : کاری که ایران تو تنگه هرمز انجام داده
🔴
از نظر واشنگتن اصلاً قابل قبول نیست و بی‌پاسخ نمی‌مونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/132315" target="_blank">📅 22:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132314">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDb5NWIzNuEOPrqQOVs8WYsazkF2bawkqZFPHmkYeGde2AGejr2tMk8AiNipjaT-axaEsbvToXXeyV_ZA4gKH42jC2zBnyPRSvsWEKEeNf86quLYbmjoTHPXceKv2xqi4GYsPtm-kf5U2O-zqqua1gEzdrXRLj4Nlv7kCBo_TDofp8n3rlIpbjdU2pNFuWzOK9Ri5nt10lYCbuAZmmXQukxWokoDekKywV2D_oF1SL2TYaVbwSE0qeAAWY8yoK2zuvORGxLKwZLI1nMVgXKB0Je1z5rgE4t49fbSsDTZD8qQ7KRFj21oYGxZOh6O79YZcm4-0Gev56EXukh-zNWw1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
😐
😐
😐
😐
😐
😐
😐
😐
بعد از برد دراماتیک آرژانتین گروهی از طرفداران زن این تیم در استادیوم لخت شدن
😐
⚠️
⚠️
مشاهده بدون سانسور فیلم</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/132314" target="_blank">📅 22:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132313">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc7XkjF0g-9ZaTIp8VMxR5_3zssylj82JJFB1TtmrzgeGw0DVHCWrsVp2CoNu4pENpV3BvPed7GGAEpyXvhlfKN_GXBzP7oVzWfK0VU7-_f9IGt7U5qaLx9OzWwPYR8MnDHd-uXHblBK5Mpps3ZIFDhzXq0W3lzsAbTOjaCShCoWn50ktZWjTzzZ2Gmekypq6-Ri5nW6jzhYLu7gVR2NkM_q1Ic-I8K0eZ9kJ6ccfiGmdGTEMcQrZt-qenVJG5Am55j0ZJNr7pMSmqWxiiF-3RrgdiGLZy3ZSUTFV1PNqgzRWysBgO5vzn6bg9C9N7G1Pb81eK6oIEmqeyTeAt2xfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنگ ایران و تورم پس آن چشم انداز نرخ بهره در جهان و بخصوص اقتصادهای پیشرفته را تغییر داد و حالا انتظار کندتر شدن روند کاهش نرخ بهره در جهان و افزایش آن در اقتصادهای توسعه یافته می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/132313" target="_blank">📅 22:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132312">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری/مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند
🔴
یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
🔴
به گزارش خبرگزاری رویترز، این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد».
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/132312" target="_blank">📅 22:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132311">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
وزارت امور خارجه عربستان سعودی: هدف قرار دادن نفتکش سعودی توسط ایران هنگام عبور از تنگه هرمز را محکوم می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/132311" target="_blank">📅 22:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132310">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctip-2eH5IMX7vMhI30VJiW-TKeXYXUaw7eEkhXuUdaQxEktbKaUzAIhOKojhBgUFOmM6e7E0MYaW6fGNgMQJgu1MYy0hUIxLi2MZ8G8i3rxJivm5MYB4GUwXFUOs6II62xj_wrVf7KLIc3G4oy2HK8nuNQd26vz3au2om3K5geyo0CnvAPmWUsDNjj7Yeo9CPFth2XlG5LAqq7on_TMyUIS-LndpObkS0bpMqk57HCP2TO44rlkVxbGUyJ07zV2G1raImPVKJh5L7BP_aDywzqd88nJUPmGFE7M22sjc9BiLBeYfo8HTaZtky76pZqM3ypM7iAkMex63QKBMFqf9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نشست سران ناتو در آنکارا
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/132310" target="_blank">📅 22:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132309">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری/طبق گزارش ها یک نفتکش بزرگ دیگر متعلق به امارات نیز مورد اصابت موشک در تنگه هرمز قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/132309" target="_blank">📅 22:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132308">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/132308" target="_blank">📅 22:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132307">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTrlZPzlwpMBQuYe8klw7sVNwvYcIWwAIA5-mGL6ck6wHrYWuuEWUoRnEsodRV1CfuMPJEOpUIo4mCQBe4D9jmDQ6j5p4RfcPuwQ4Fn7ziArdcCS4J1qcl4spcl3962-9gtu_RzqlJZGNqJqTb80c0Ieu931RJXq2iMv56C1fHiG613eRCdKzpl27qrsJ620GyFiKOeUYK6yIsWV-QSLTm9mnLewKhumvxfEH9XT7mwV_Rp0IWvyA_uHHeqGWrBw8CLtKRPcbVGItT8I8u7tzKy4v4e4p0tgJvV9qfh-mcLZDyoPNgGyRPqx7LWtcCHsx5s2dG1O3-ePsEATikez-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚘
✨
رضائی موتورز
✨
🚘
خرید و فروش خودرو | ترخیص سریع و مطمئن
🔹
خودرو: ملی | گذر موقت | مناطق آزاد
🛳
ژنراتور: ارسال و ترخیص
🌍
صادرات و واردات قطعات و تجهیزات
⛴
ترخیص کالا از ایران و امارات
📌
بهترین قیمت، سریع‌ترین خدمات
📲
موجودی و قیمت روز وارد کانال شوید
👇
👇
https://t.me/rezaei_motors
https://t.me/rezaei_motors
https://t.me/rezaei_motors</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/132307" target="_blank">📅 22:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132306">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqnF1wjCE5gW7NvZNXEqekhQwrJnOAEsBKFPF6J8Y3tVoPTcVBTol71w2Qa1LNgo_BY1ZjUETLB5Yu7imUmyf0eMHJJWbxrtoSu87R63U_4JeDBUE90T62zOZnDu1kgYpYjM8rl_7qklIBBPgHjfdhY7T1zJdvE6JqloTZtxTWAJSNPkPYNxx_KU-neOJzxCOgLPUsvSkgz2RjWMVGlpCPwn0mgh_wnh3wBt13veGFixz_o5amcDaAJdc9tsR1U7X3KIXbpJ6591dUq32c0lTqZ8lLulw5M3TnLu7lmbJjoa1fRL0r03nE9Qm7k3_3CGDNvCXbG2L9LnMeHQQAHyUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاهکار امشب ایتا
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/132306" target="_blank">📅 21:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132305">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
اردوغان، از رئیس‌جمهور آمریکا، ترامپ، در ضیافت شام اجلاس ناتو در آنکارا استقبال کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/132305" target="_blank">📅 21:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132304">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0EgYrClKhm5vKY9Z-fi_K7f_H1EKTposzTj1TZsPjK1tiYCD2QAtMJnm94Aw2GhzomPbEgcZ-4GWKw39VYWEomKCnUYq865KhVrSqFsgJfshbMafBAe5MvcBhpq-mUzBtw8bXlMq_9bdE7j-10B2UJBMKTv7NImJXt-LbNqo6WL7Byg-xr3kMmXJM1pLapYT4bjIFtdAKNUvecnXC7MpxGsoEBHYMgIfr_hi1RrKYt6o1CXyO6YqEr2Fcfsro-QDly7U6gM5IMjQdF55zMZU85Zji2-subDWCAvuAMbK1uPtY642CSsqDLRJ6Vzo46MnoVqANCNdBvKTllscgDQ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از استقبال نخست وزیر عراق از رییس جمهور پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/132304" target="_blank">📅 21:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132302">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
حدود نیم ساعت پیش، نیروهای دفاعی اسرائیل (IDF) حملاتی توپخانه‌ای را علیه منطقه نباتیه الفوقا در لبنان انجام دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/132302" target="_blank">📅 21:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132301">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وزارت امور خارجه امارات متحده عربی: ما تجاوز ایران به نفتکش قطری هنگام عبور از تنگه هرمز را به شدت محکوم می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/132301" target="_blank">📅 21:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132300">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ارتش اسرائیل: هنوز زمان مشخصی برای عقب‌نشینی نیروهای اسرائیلی از شمال و جنوب «خط زرد» در جنوب لبنان مشخص نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/132300" target="_blank">📅 21:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132299">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d43e59d0fe.mp4?token=k7skYehaJ32IZhpmIRwGzynbLi9yruecfTaYM4UaFY8ca_XBGlAakM9OG-HIXcLOzshu64ZQeZAi11uyXSFWOjRAvlaYJFldMy-oATysTvrsrueE0L74tfKRf_jpsN13wqve97ifj5pkq3sbjFnRY313A8d-vI3lMdfWeDyVJ3CgNU1r3Wp9_OLZTrXyGxqvgYcieXTpLdA3amO7EzfhYb_xW_1e4k7nS6f7y4aLHcuLuoj83LbY8tW1XSdVvSEzyKM5veT40ywH-X2fDFqWvwJAr8oAqBRXlhhJmaIjm7I8T-PeO-6WlKrSj4PYSJPU2BMAb1vsTvMAxBoDaby3YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d43e59d0fe.mp4?token=k7skYehaJ32IZhpmIRwGzynbLi9yruecfTaYM4UaFY8ca_XBGlAakM9OG-HIXcLOzshu64ZQeZAi11uyXSFWOjRAvlaYJFldMy-oATysTvrsrueE0L74tfKRf_jpsN13wqve97ifj5pkq3sbjFnRY313A8d-vI3lMdfWeDyVJ3CgNU1r3Wp9_OLZTrXyGxqvgYcieXTpLdA3amO7EzfhYb_xW_1e4k7nS6f7y4aLHcuLuoj83LbY8tW1XSdVvSEzyKM5veT40ywH-X2fDFqWvwJAr8oAqBRXlhhJmaIjm7I8T-PeO-6WlKrSj4PYSJPU2BMAb1vsTvMAxBoDaby3YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور فرانسه، ماکرون، تلاش کرد دست همسر نخست‌وزیر ترکیه، امینه اردوغان را ببوسد اما شکست خورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/132299" target="_blank">📅 21:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132298">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GT-dCbvimSIibTilShmLcU7_mRn9hFIh9dI5PxKL4fVzhCN_OUEH2Z_Zldj2bGSyZhPQseuBc3JPz_YTzoi6HztjPKEgup0N96rCSUgLdqqkrMo_c2oPRokowDzr474duGbJgzwcv7iPkoyTJ-REi7G_pzVIXe-FvJ3xegTgCDBkyzfKo28FhChX7xe-Z15GuPb3A1VJfnbYwVgfxVrHn9WCViEO6ECfCnIAi8Q9AbCVvQTjbmxfbZcZyF21UF5Lg2dCpHkVQP5cPjZ7nd71D81Jw2u5wQ4Oz_GDLUR2YOlJV_KVlH6eYgNB6iFxQfHqnSnWBCWfbz0CPBXJZfHcVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی :حالا که ترامپ به ترکیه آمده، اورا با موشک هدف قرار دهیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/132298" target="_blank">📅 20:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132297">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
نتانیاهو : اردوغان فقط مشکلش با اسرائیل نیست
🔴
حتی یونان (که عضو ناتوه) رو هم تهدید کرده به نابودی
🔴
نتانیاهو درباره ایران: توافقی بشه چه نشه  من هیچ‌وقت اجازه نمی‌دم ایران به سلاح هسته‌ای برسه، این دقیقاً همون موضع ترامپه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/132297" target="_blank">📅 20:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132296">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
پزشکیان به نجف رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/132296" target="_blank">📅 20:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132295">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3e488565d.mp4?token=SqL1pNJQN_DFFvLeIzp6Mb7i_Ao4BfwqhC5ma5IfL7TcEQeS-gQNLLqALV6jxhZYGrgi6XUXbOhs4TJowXtbCAsfU9ukuZNyL7ZDQxQG32sNO23YkHC6uC-uzHOw8j6NDjCZPf6RducdkyxT7fmpCzLgXl0HyQDSJfSgly8fl-mqtDIpsVhpPqW2L76-x4MVCHRUfOem5JPzCsXo12aMSOoceoSdRnPMhT-gnmduWZHitg0ZyDgzQes_-x26GaYsztMziSW87SQ4GtbLVcdfmRYxNLCsyFa8d97Yj4pRg7VSxp5xg3OwsWz5DZZj29reFdWqYHQUp3GyEnAs72PzuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3e488565d.mp4?token=SqL1pNJQN_DFFvLeIzp6Mb7i_Ao4BfwqhC5ma5IfL7TcEQeS-gQNLLqALV6jxhZYGrgi6XUXbOhs4TJowXtbCAsfU9ukuZNyL7ZDQxQG32sNO23YkHC6uC-uzHOw8j6NDjCZPf6RducdkyxT7fmpCzLgXl0HyQDSJfSgly8fl-mqtDIpsVhpPqW2L76-x4MVCHRUfOem5JPzCsXo12aMSOoceoSdRnPMhT-gnmduWZHitg0ZyDgzQes_-x26GaYsztMziSW87SQ4GtbLVcdfmRYxNLCsyFa8d97Yj4pRg7VSxp5xg3OwsWz5DZZj29reFdWqYHQUp3GyEnAs72PzuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جکسون هینکل، فعال رسانه‌ای آمریکایی رو بردن تو میدون انقلاب شعار مرگ‌ بر آمریکا میده !
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/132295" target="_blank">📅 20:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132294">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
نتانیاهو در گفتگو با سی‌ان‌ان:  هنوز خیلی زود است که درباره آینده ایران صحبت کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/132294" target="_blank">📅 20:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132293">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rtvE2hJZG6BV7ERM4Ar4eV46nNb1QLQHkQtCv0xKJ7J9Sv6hAgPhzv2siIFj_tQbf2afr_e4-5petNJA6s_vPZzHSTJ7jV3rCQUuIZeSYHKKqnoPiHxcdtI31gUaA2ypY5HnJg-pJcTI4qt-j2WsKOqvdq-B1QdYo6CalT2Yqk-y9WRNf9i3h45FkYoUWXkeEXzkTzVymTczKP26cTrnbtXJiIlvOFb6qJen2spRTVrOY5YTvMTnVHp-QhgybBXHrRG5dmsCZMQ_bvyFr-qwC1cd2OasgD-qbwA5BNtKIsMNo8N_tYYoPOc-jFJEtY2W-a-uuxiDXIp5SsA3zdAUBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز اطلاعات دریایی مشترک، سطح تهدید در منطقه دریایی خاورمیانه را از "قابل توجه" (احتمال قوی وقوع حمله) به "شدید" (احتمال بسیار زیاد وقوع حمله) ارتقا داد، این اقدام پس از سه حمله به نفتکش‌ها در تنگه هرمز انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/132293" target="_blank">📅 20:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132292">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxrP2gCe7Q7br9xF3a33iZ26O7Ejh2ix34v51koUGe8C_V8ri3eKlUEU5xbpp251wYIBPY5uN82EX1Xv8jixZxARQhclyEDF2vQYZBU-sD84RDPmtgmkpONpk0hBGD7DFF8pu--PHccJWdZ8idavC42SV_ER5F0vcdqJCsbwPVgYafuxIuIf-n_qqPZ76md8_GO5qOjiJAdVNRlPyFYOfxmsvdaVhUwXr80CffvkVOeHuVF0pgCvEmQGH0JXKgTkej9I95Zy_mtT9dGxbkwx3WkjrLk211Z3a-yiIVkOzlvmmvKffSVpJZb7JBDkkKT5nCiXGIHzrsKGDBufj2J__w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پر شدگی سد کرج با ۱۶۱ میلیون مترمکعب ذخیره آب به بیش از ۹۰ درصد رسید، ۱۱۹ درصد بیشتر از پارسال این موقع
🔴
تصویر ماهواره کوپرنیک، ۱۵ تیر امسال و پارسال
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/132292" target="_blank">📅 20:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132291">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
نتانیاهو در گفتگو با سی‌ان‌ان:  هنوز خیلی زود است که درباره آینده ایران صحبت کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/132291" target="_blank">📅 20:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132290">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
کرملین:  روسیه میتواند هزینه‌های ادامه‌ی عملیات در اوکراین را متحمل شود.
🔴
گفت‌وگوی کنونی بین آمریکا و روسیه نسبتاً خوب است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/132290" target="_blank">📅 20:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132289">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
فارس به نقل از یک مقام آگاه: عبور و مرور در تنگه هرمز، مطابق ترتیبات ایرانی انجام می‌شود. هرگونه اقدام تنش‌زا از سوی آمریکا، با پاسخ فوری و قاطع ایران مواجه خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/132289" target="_blank">📅 20:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132288">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
فرمانده کل نیروهای مسلح ترکیه، ژنرال سلچوک بایراکتار اوغلو، ژنرال دن کین، رئیس ستاد مشترک ارتش ایالات متحده را در حین نشست ناتو با یک مراسم نظامی به گرمی استقبال کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/132288" target="_blank">📅 19:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132287">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
الجزیره: قیمت نفت با تجدید تنش در تنگه هرمز افزایش یافت
🔴
قیمت معاملات آتی نفت برنت امروز با ۱.۴ درصد افزایش به ۷۳ دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/132287" target="_blank">📅 19:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132286">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
طبق گزارش شبکه الحدث با استناد به یک مقام آمریکایی: نیروهای آمریکایی چند پهپاد سپاه پاسداران انقلاب اسلامی که به سمت کشتی‌های تجاری در تنگه هرمز پرتاب شده بودند را رهگیری کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/132286" target="_blank">📅 19:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132285">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0050bbda7a.mp4?token=OOPbeVOZ9jx4smMEWQnFofeQyA8QrrW4W--ZHnpxmnUwMEr-QpAROzBVR7ZPzWwklKa-MMBZaRuLl8DLGtJhCaLzSozd28-mp45wLe3_VTmo5DqLM26FwkK0AELA79oaV70XDyvPXKB45ORPryq0uAtCeTqcgIFNGFvCxFgI5xLFrloLYbqN42skZkQ9I0uR_uSphHSuUUKW4l2YQQYhuVVMC5d-K_0zCiU5mSmp5QPyWrkGBGsUiUthcZ7jN8bpnOIiBG5IWKfWZFuBCZarjDaqCC8bOjqPkb0qWqSnAk0CRkCCTp_Cok9xDSMfQXZHDz2xl9_rbzbnrNQgUN0Tzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0050bbda7a.mp4?token=OOPbeVOZ9jx4smMEWQnFofeQyA8QrrW4W--ZHnpxmnUwMEr-QpAROzBVR7ZPzWwklKa-MMBZaRuLl8DLGtJhCaLzSozd28-mp45wLe3_VTmo5DqLM26FwkK0AELA79oaV70XDyvPXKB45ORPryq0uAtCeTqcgIFNGFvCxFgI5xLFrloLYbqN42skZkQ9I0uR_uSphHSuUUKW4l2YQQYhuVVMC5d-K_0zCiU5mSmp5QPyWrkGBGsUiUthcZ7jN8bpnOIiBG5IWKfWZFuBCZarjDaqCC8bOjqPkb0qWqSnAk0CRkCCTp_Cok9xDSMfQXZHDz2xl9_rbzbnrNQgUN0Tzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که ایالات متحده، از حدود 60 تا 72 فروند هواپیمای تانکر سوخت‌رسانی هوایی که در فرودگاه بن گوریون اسرائیل مستقر کرده بود، 32 فروند را خارج کرده است و تا اوایل ژوئیه سال 2026، حدود 32 فروند از این هواپیماها باقی مانده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/132285" target="_blank">📅 19:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132283">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
مقام ارشد آمریکایی به سی بی اس:
ایران با شلیک موشک ها به سمت تنگه هرمز، یادداشت تفاهم نامه با آمریکا را نقض کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/132283" target="_blank">📅 19:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132282">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
پزشکیان به نجف رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/132282" target="_blank">📅 19:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132281">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0qM_akOdResmCCC0h7lVreuZhx8aeARo4Nn83aTRvfaozR31RVg_BzxmZ8RXTGTtiD2dtiHYU-1eBPIq5J9i0TyUi6gBewjBK6oPVxL5bcH2FyK0ftN7ikKhJtAxNlsCv1RZjH8Kw4w564-EihYQraua1eLjxEqmpRAetskcSsVOvdSrLI15oUCSUN5hI6qEqwdqnCVpJQ_RGT7RkC-jKOC-dlc2IstyCOKxs_klkNFqTXOXdpqxZbNpCimf0fCtacYn_Eplqa_Tbn3Imn3im5da5kzECMU6LqoNyi3BQ4qRz1ZLHTKinKljSRT5jbZ1pUnjvN6dsHb66H2M9h3Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیروز یکی با دوشِ حموم خونشون داشت آب می‌ریخت رو عزادارها که خنک بشن اما آب میریخت رو ماشین جلو در
#مغز
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/132281" target="_blank">📅 19:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132280">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa9b62c5fd.mp4?token=k71f5AkJc7ymVeGyYeOIqVE17CaVaxmhgiuuW68K3mpfTmwqB8xtouQxjLEBTEL9e2o4JLSqXC8Cnf4eZ_P7-FR2VtwrqUoMMC9sbGfoJmbOmOf5Tn3IMqsYzr-sQWnKDW7PM-W1egXttQqel9F0fvlhvkH-S5E6Vo9tgF4FtzSpQhNxlBG1Wxm_bs5BV9QlO0OCE8p77VC9tSyol1DXx1xExHZPLtjbxRyBJOgdboHBbre_D2wY2KBlPu0whIHvjS-v7Cl04-VGOEIaL-ulY01uCetIY9uvD3vsUMkAV89WVjwqjgVWSlPHMtxdBcwiKj5LdGwmOXoOiREdmbv1jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa9b62c5fd.mp4?token=k71f5AkJc7ymVeGyYeOIqVE17CaVaxmhgiuuW68K3mpfTmwqB8xtouQxjLEBTEL9e2o4JLSqXC8Cnf4eZ_P7-FR2VtwrqUoMMC9sbGfoJmbOmOf5Tn3IMqsYzr-sQWnKDW7PM-W1egXttQqel9F0fvlhvkH-S5E6Vo9tgF4FtzSpQhNxlBG1Wxm_bs5BV9QlO0OCE8p77VC9tSyol1DXx1xExHZPLtjbxRyBJOgdboHBbre_D2wY2KBlPu0whIHvjS-v7Cl04-VGOEIaL-ulY01uCetIY9uvD3vsUMkAV89WVjwqjgVWSlPHMtxdBcwiKj5LdGwmOXoOiREdmbv1jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
تندروها نامه تهدید به قتل رودر خونه معاون پزشکیان فرستادن و همزمان ویدیو دادن و تهدیدها رو ادامه دادن! کسی هم کاریشون نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/132280" target="_blank">📅 19:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132279">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ان‌بی‌سی نیوز به نقل از یک مقام آمریکایی: ایران دیشب با دو موشک که مسافت کوتاهی را با سرعت بالا طی کردند، به دو کشتی حمله کرد.
🔴
ارتش ما امروز چندین پهپاد شلیک شده توسط ایران را سرنگون کرد. حملات ایران در ۱۲ ساعت گذشته تهاجمی و نقض مستقیم یادداشت تفاهم است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/132279" target="_blank">📅 19:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132278">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZQg9MB-yLPhSjAwXp6rkWZiDAr1ruk3YSYNdQxM0YFWreMm4gqJE0YiReNbZU1plXuoezLBYdIME5d-zBsalSosuNV3LMDkXCrlbwZphSjA_wNmHQdzQ_VnrhaU44n-lEJTsVs1afC2Ik5WG-m8obPWPP0apSYuvS0brk5w7PJFPO117C1geRDu1QoXwFzBYa5Qn459xTBVd0zJamouIjsfeysYGjIPuz1N1ha3_22CnqpnV9qH4zTBBULxnwR1JykGg2L-Xr6oh-O6wRVeqqbymqBH5gO2cg6-xRy4H7nMe2x9L7TUe_F3iRf70Bggag1FiVKTNb_0VTTNl3Qk7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش قیمت نفت در ساعات اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/132278" target="_blank">📅 19:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132277">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
دبیرکل ناتو: بدون اروپا، آمریکا نمی‌توانست به ایران حمله کند
🔴
رومانی بزرگترین فرودگاه‌های تجاری خود را بست تا به هواپیما‌های آمریکایی اجازه برخاست و فرود دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/132277" target="_blank">📅 18:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132276">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سازمان دریایی بریتانیا:
سه نفتکش در تنگه هرمز طی ۲۴ ساعت مورد اصابت قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/132276" target="_blank">📅 18:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132275">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
هم اکنون تعدادی از سوخت‌رسان های آمریکایی درحال پرواز در نزدیکی تنگه هرمز هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/132275" target="_blank">📅 18:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132274">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdvuKWZaEqrxcYjfVHJAiGEqov_3QqT4cyXHwNM2kCPN-jDhpqg_R6uz99aVibAiT9nPZtABs-C6wMC8J7FShQPjlj01g_xcxsQ_ucuUh9EkG67mUZpC_SLzQyPSAXFEaN6oysLchpFjmYOxg1LJVk8ux2575IpwD0kylxWY8aOzMkRdIbgNyHPUPKIx3NyMRmyw8bGgtfvuk9w9J-9UvhziIbBdaqwX35j58cenKb4NKt3d9jWk3p34DWafrUneLp-wbmuRdpjoNnHXDNz9laF3Sgi1aLsh_hJ80zNfSWYQDprCusOu1hDzhGnWCHrHDFyE0LBYeYfb-tVBS-hFxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گفته شده است که دولت مصر تمام برنامه های سالگرد محمدرضا پهلوی را لغو کرده و وزارت امور خارجه این کشور، ورود رضا پهلوی را به قاهره ممنوع اعلام کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/132274" target="_blank">📅 18:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132273">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
بقایی: حمله به بیت رهبری یک جنایت جنگی آشکار بود
🔴
اروپایی‌ها نباید در برابر جنایات آمریکا و اسرائیل در ایران سکوت می‌کردند؛ این یعنی شریک جرم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/132273" target="_blank">📅 18:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132269">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c1W5_3NPRW5AfJdxBPNGbDQU_VHWCbHDIMQw1LXzDec6aY7OBONz0qJaFom2OivqtMuV1ikhkmWD9jUe6j2NcD2WRfoctGwMKIhUKN1GIGxEk4x4GMg3LK4p1gaqZCbnNHNM2PfuTodl_vViyisWk1kds-B7BJBSsCBya9rVKyabZ4vXwTYhJjSsVTSouZClmlq5vjk5taMj7Gi8kimUMMIhEebwkUlaI537xchc52jkZRzTHNLRKT5dCG5Du9NSQ2P8j6GOIN3GDRbtlG5sMfq1IzRFkj7oV3JjcBh5Aq8E4z5QoXUJDAxXMSmOXL9TmrYHywfoKLBtXaQgJHs0Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l8UZrkC9ksrRoj-epQO_unna8DWlUflKN4qRvAP0sgD6bMaLqEgSTQWq4VAxvjxE-en9L2maGLQz0mxQBlPYOQF92s126lzTj9GxhF5qFWqF9bZmZaFJD61BIPK2HD-y0pL1ELPxsoIcVe6TSJFW3nbUpARnZrIVC9QewjLwbg_Pr_pmCRVum8Jdwql4SWT8js_ZJUXNwX1fxG7w9Jv4lvP4dZ_xgNGi9YZq6Wm4PbNIJdRWkEHzhLmn6kQRXDxpY6ZmszW0kRENNfFDlJ_Y50iYoALhP2-qe1RFjLztOvLCLKYwRqNeRy6XpOG6CDuUHIj4hlucNJeC_WIjA8ZBcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iQR5sKlI3knHzCevVg89_YYKe_mawPGV2iAIZDhYAB8VELOIsOJSYmC_Dm0lNq_LWLSl0CN-TU8I7nJCaKuvkCQhzBX_IJxmLK9P7ux55KdmZjLWaXmTUuKFZS72wqA19Px3FHUaPp4Wn2J61D2j51iZv_WG-hRUoPlyFjGlAOAQz7cjTCSReIf2WbMDdE4ZST9jP0S4zUDYzcMcJhkTporn65AzGLtYk54urESPM838hPXr_4aXFkhkFMOp1gLiGD0zikSh8fUCn9Ih_KwLfPcSHYYk506A-tZ4jw2_wV2_9-IXGtLtysvRJrGQnT-kUf2qFYSkc9kYJ3HjWwxFIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gkbKbO4RGtAa_L7y0zuC7AnwTqhBRxhO-nY8S0wJkwysahobK7S1B0V2bxEy8DzeRnOHtpqhd9jc8kbHZtlRrnEKXsYM0kyyiBxERef_A2n9fn5f7LTJw3k3I8cHCqgE4Wzy-WtkbeHBwic8giEiFe3x1PrWaV0_r0pJR5w1JNXKSvh9YXZnjWYN13980I5fK3U7Be-1lR3-XyZvDMSvBAoT1J95IW9Ctm7UezzrD-fRCc7lj_2x8b9wBV0oT1zTIfQd3ZzOKrsOG-cBX50F4HvcAbF_mV2-ULEbylhd1LFWwGQwr6OSM6H1O9hCdmF6_yTOTT2BRR6CwbQUpgsc5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک دختر بخاطر تاریخ امتحانات خودکشی کرد
میگه اگه خونوادم رتبه خوب نمی آوردم، بزور منو شوهر میدادن، منم بخاطر این شرایط نتونستم درس بخونم که رتبه خوب بیارم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/132269" target="_blank">📅 17:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132268">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
خبرنگار حوادث:
امروز یکی از عجیب ترین پرونده های طلاق رقم خورد، یک آقای متاهل چند وقت پیش تو تهران با یه دختری میریزه رو هم و به همسرش خیانت میکنه.
🔴
زنش جریانو میفهمه و ازش طلاق میگیره و مرده با دختره ازدواج میکنه حالا بعد از گذشت چند وقت از ازدواجشون زن جدید مرده بهش مشکوک میشه و مچ مرده رو در حالی که تو خونه زن سابقش بود میگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/132268" target="_blank">📅 17:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132266">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3538709b7c.mp4?token=LR47L_WKx78OW0ArhlgAVhlpNo7sourDBKLnPQCmmXfXTbIskJLvuHWSORX0YZo2lXHDhhaojD3XlqFB3sMFGxZbAz248zphpW0lsLixfUZ-8GdH7k37yJVYgZToW67hTYeystlxNcsS65F310Z1xzMk8_LFRaPkw9yHj2sUxGnmTIhQV0BU3ZHqhrpiFTu5JFofLT7C3NaWLb5eF04KcQSBPjqlwHPxHE-z-4G4c93pIWjOG4UUZOqataDp_SDW0HArX-yu0OXa2CpZyBkBwkd3TVB5lya0jdo-hw9i4rqzWZ1cq-Wq3XwmE7unQKq-63wPOcgKYEjdQURTddCENIy9yL11eXwZPYw2HdiUeo3lfLnPzUSmakTFbAN2KKrtvfuOePsQXfpBiBpl4X59F34i_hEMc7TSG4aQH4YwePLxx1BAO3HQ5JKdVBAtTaXsBxjAsc2hppQilGOtSOmvmdIncDl1ISVIkqqL1LN6gxsnmUPGYia_lFmh8CGvc6vGIzR56-bK78XKwkr-l3nD3U0a5vtlhsoLymtHepjjHR_j44Al0FDJoFYRnpnTCBQRFOSGRaxvzKVUdswiiXRciRMthcfrlFaLcwDrzdfXvLGrk0Ph-J--rC_JZPwjwzWpl-vkJsozOqjxOgBsCVFxlDEC_kUv2S8oL5yo_wd-u5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3538709b7c.mp4?token=LR47L_WKx78OW0ArhlgAVhlpNo7sourDBKLnPQCmmXfXTbIskJLvuHWSORX0YZo2lXHDhhaojD3XlqFB3sMFGxZbAz248zphpW0lsLixfUZ-8GdH7k37yJVYgZToW67hTYeystlxNcsS65F310Z1xzMk8_LFRaPkw9yHj2sUxGnmTIhQV0BU3ZHqhrpiFTu5JFofLT7C3NaWLb5eF04KcQSBPjqlwHPxHE-z-4G4c93pIWjOG4UUZOqataDp_SDW0HArX-yu0OXa2CpZyBkBwkd3TVB5lya0jdo-hw9i4rqzWZ1cq-Wq3XwmE7unQKq-63wPOcgKYEjdQURTddCENIy9yL11eXwZPYw2HdiUeo3lfLnPzUSmakTFbAN2KKrtvfuOePsQXfpBiBpl4X59F34i_hEMc7TSG4aQH4YwePLxx1BAO3HQ5JKdVBAtTaXsBxjAsc2hppQilGOtSOmvmdIncDl1ISVIkqqL1LN6gxsnmUPGYia_lFmh8CGvc6vGIzR56-bK78XKwkr-l3nD3U0a5vtlhsoLymtHepjjHR_j44Al0FDJoFYRnpnTCBQRFOSGRaxvzKVUdswiiXRciRMthcfrlFaLcwDrzdfXvLGrk0Ph-J--rC_JZPwjwzWpl-vkJsozOqjxOgBsCVFxlDEC_kUv2S8oL5yo_wd-u5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره جنگ اوکراین: من صحنه‌های جنگ را دیده‌ام. آن‌ها عکس‌ها را برای من می‌فرستند. در واقع، دوست دارم بگویم: «لطفاً آن‌ها را برای من نفرستید.»
🔴
پیټ هیگ‌ست عکس‌ها را برای من می‌فرستد. من به او می‌گویم: «پیټ، می‌دانی؟ این کار به وجهه من کمک نمی‌کند.»
🔴
من هرگز چیزی شبیه به این ندیده‌ام. این یک فاجعه است و باید متوقف شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/132266" target="_blank">📅 17:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132265">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1YhKnVjoV2ET6VNS5kaTTHatjGJOdNWILf5AfftqJlJ9RpEAjoOUTEgIJzM3Lp_3IV0jFRXdTbqvWQ2vM8vRlVr_toNKInaRNZLZEssP5XCSUOuBCRASZhJW4W4pZpzIGLvny_0KZi1Zb3SOnorRTSKHmSeHRxMlGKhs8gIPDVef_OGV1zXDW4NKp6ubaJEQSJFRDIn2vS-1mic6EXRWr_rkOCuLjOwbZ3zASXSY4K9qbabzQQqUPSeahlVNthV2BmCsESea1lnK1jwJNbfRPKQRMp0J1FmxR9JFVtJyVKAH5-RioMIc__Gfw20QluM80_7bVicckgBQwUNrWlVjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز عملیات دریایی تجارت بریتانیا (UKMTO) گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفت‌کش در حال عبور از تنگه هرمز دریافت کرده است.
🔴
این نفت‌کش مورد اصابت یک پرتابه ناشناس قرار گرفته و به نظر می‌رسد آسیب‌های ساختاری به آن وارد شده باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/132265" target="_blank">📅 17:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132264">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
به گزارش امواج‌مدیا، ایران با برخورداری از منابع طبیعی گسترده، نیروی جوان تحصیل‌کرده و موقعیت راهبردی میان آسیا و اروپا، ظرفیت تبدیل‌شدن به یکی از ۱۵ اقتصاد بزرگ جهان را دارد
🔴
مشروط به آنکه سرمایه‌گذاری‌های هوشمندانه و هدفمند در مسیر توسعه انجام شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/132264" target="_blank">📅 17:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132263">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ترامپ درباره اروپا: ما می‌توانیم تمام سربازان خود را از اروپا خارج کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/132263" target="_blank">📅 17:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132262">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فوری / گزارش شلیک موشک به سمت تنگه هرمز
🔴
ناو های جنگی آمریکایی در حال اسکورت چندین نفتکش در تنگه هرمز می‌باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/132262" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132261">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
بر اساس گزارش رویترز، عربستان سعودی در حال بررسی امکان افزایش ظرفیت خط لوله انتقال نفت خام خود به دریای سرخ تا سقف 2 میلیون بشکه در روز است. این اقدام به منظور افزایش صادرات نفت و دور زدن تنگه هرمز انجام خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/132261" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132260">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
جولانی: اسرائیل باید از مناطق جنوبی سوریه عقب نشینی کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/132260" target="_blank">📅 17:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132259">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
دبیرکل ناتو: بدون اروپا، آمریکا نمی‌توانست به ایران حمله کند
🔴
رومانی بزرگترین فرودگاه‌های تجاری خود را بست تا به هواپیما‌های آمریکایی اجازه برخاست و فرود دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/132259" target="_blank">📅 16:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132258">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca40d53017.mp4?token=ZSVW0X17wD4NLtyipxiNPB8LQXpMPecONE-s5OChMqVKT7T40BEUsR7oVCuMTtG6KayQCYApvq5gdh7qLKXExVepbQC8DX_sU-FqdWOuvf-Uk5HAV-2ntdci5201lTdjLAgRupdc5ITXPGR5qTOMWF2KfToEtoth3Y-U2oyUUTTiOUvvJ4f6C8rwKsGxyFbNpkbc5dP51cVdKuPpUFXxArhbivuuTLWXXdqSQwYsejsc9lqxb7eTFvVECS7lSJK7oboK2dyqyngrM9EPyg71d6h2VInmAs0eOjdJarqqm-sTKvotM6ZZoMmF3QMHT05-PmI_GygAZmGXNSqZyP3qDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca40d53017.mp4?token=ZSVW0X17wD4NLtyipxiNPB8LQXpMPecONE-s5OChMqVKT7T40BEUsR7oVCuMTtG6KayQCYApvq5gdh7qLKXExVepbQC8DX_sU-FqdWOuvf-Uk5HAV-2ntdci5201lTdjLAgRupdc5ITXPGR5qTOMWF2KfToEtoth3Y-U2oyUUTTiOUvvJ4f6C8rwKsGxyFbNpkbc5dP51cVdKuPpUFXxArhbivuuTLWXXdqSQwYsejsc9lqxb7eTFvVECS7lSJK7oboK2dyqyngrM9EPyg71d6h2VInmAs0eOjdJarqqm-sTKvotM6ZZoMmF3QMHT05-PmI_GygAZmGXNSqZyP3qDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کیر استارمر: به نظر می‌رسد نخست‌وزیر بریتانیا دیگر در آنجا حضور ندارد، شاید به دلیل ایران.
🔴
آنچه او انجام داد، بسیار ناخوشایند بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/132258" target="_blank">📅 16:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132257">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ترامپ، درباره روسیه و اوکراین: هم پوتین و هم زلنسکی می‌خواهند به توافقی برسند. متاسفانه، این اتفاق خیلی دیر افتاده است.
🔴
به نظر من، اتفاقی خواهد افتاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/132257" target="_blank">📅 16:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132256">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb42c6a06.mp4?token=DY6TBQtLTDL1YgSWmy487Q6SxVBZQRgB_gZq4MgIQjTeUvIWAHAqwddOYUKiEH0oo5hxmnbWH8fBvAkurNtSdD6KZmffVa5aF44pD7t19h9PEb8VeksnFCgVzmJ3Qv-GqSpnbPffOlsWEkJi7RRqDFSALFQinE1vK_4scewA1mzePZDS8I84QxNB2nZpR-Yb3vJlLcmFOahD69e2hvWZr4AdrjaX7ZqvMXTpE0RxIIGnP6wFOzoG2ObYJmHWsfjvseuxcB_Ek6neTZy7NJx7amcn_4zuEd2Akxxa1a3a9DJAZpU7DT8t8_vaIhsnDlC5J_Wdo8z1JHjs1B7mWqk_5L74_LP9FKqgGQlcSHJaK1DoDJyefW8rkPyMtP5OuD5VOZ4o5xx0Zp1xkkqcUCtJ-iXJrGztErhNtRjHEIYGPiHRPNSIz6nIXiQDl03inRgHywa0UYgUxBe87XKSAdp-IaVRAsGTHP08t8E68dSyM1O11HN8PHZFuDHZx4iMqOLCk9JM-WmpXXou9iGeh4ZZLrNaCdnCARsEkj0pMuKp6j_iVGZsro7VKlacQfSyNW6omtch0uRmU3LAHUSCnahgW9C8TUrRuxWE7o-5xd5p2ReqQFmp2_QLsxfBqgl-Kqqpw945P7nE1Xm4xex1ZU0g9ScxTfLwg9JiaO0VHDe4hcI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb42c6a06.mp4?token=DY6TBQtLTDL1YgSWmy487Q6SxVBZQRgB_gZq4MgIQjTeUvIWAHAqwddOYUKiEH0oo5hxmnbWH8fBvAkurNtSdD6KZmffVa5aF44pD7t19h9PEb8VeksnFCgVzmJ3Qv-GqSpnbPffOlsWEkJi7RRqDFSALFQinE1vK_4scewA1mzePZDS8I84QxNB2nZpR-Yb3vJlLcmFOahD69e2hvWZr4AdrjaX7ZqvMXTpE0RxIIGnP6wFOzoG2ObYJmHWsfjvseuxcB_Ek6neTZy7NJx7amcn_4zuEd2Akxxa1a3a9DJAZpU7DT8t8_vaIhsnDlC5J_Wdo8z1JHjs1B7mWqk_5L74_LP9FKqgGQlcSHJaK1DoDJyefW8rkPyMtP5OuD5VOZ4o5xx0Zp1xkkqcUCtJ-iXJrGztErhNtRjHEIYGPiHRPNSIz6nIXiQDl03inRgHywa0UYgUxBe87XKSAdp-IaVRAsGTHP08t8E68dSyM1O11HN8PHZFuDHZx4iMqOLCk9JM-WmpXXou9iGeh4ZZLrNaCdnCARsEkj0pMuKp6j_iVGZsro7VKlacQfSyNW6omtch0uRmU3LAHUSCnahgW9C8TUrRuxWE7o-5xd5p2ReqQFmp2_QLsxfBqgl-Kqqpw945P7nE1Xm4xex1ZU0g9ScxTfLwg9JiaO0VHDe4hcI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: می‌توانید توضیح دهید که منظورتان از پست دیروز در شبکه اجتماعی "تروث سوشال" در مورد نخست‌وزیر ملونی و "دستور منع" چه بود؟
🔴
ترامپ: خب، نمی‌دانم. فکر می‌کنم او شخص خوبی است، در واقع. اوضاع کمی بد شد، زیرا او حاضر نشد به ما در مورد تنگه هرمز کمک کند، یا می‌توان گفت که او حاضر نشد درگیر مسائل مربوط به ایران شود.
🔴
بنابراین، این موضوع کمی رابطه من را با او تیره کرد. اما من از او خوشم می‌آید. فکر می‌کنم او شخص خوبی است، در واقع. اما فکر می‌کنم او اشتباهی مرتکب شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/132256" target="_blank">📅 16:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132255">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMOsD6yDgMMf19jEOF8oqXtdD7yToK9uZQ9ImTQddAlLWl893aoDWFElGjzn4HFrAAo29CXu5LIMn_VWIbwZw6ErLIGOzZLnTS0MNiRTbYGdaC3ZajQyip6qH9QrUpDpPG7qdr0BtaEBEtzCk3_8URhQSf8DAOKIS5dYxIT7jkWB2pw52iZim6GH9Rwm33nTBI64LlFRfkPDMW22ykM-wfqguPlh4x6eNSKcc-unH_qBIr6J2635usWyJ3S5oMAcPayyYl4etIK4LmsPZDP59Sy3KeAujRYKD-vYx9hB9lggZff1PXlHDm-0uhWuOh_uVAa-HTE_Dgi573UdRnsZgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید: ایران شب گذشته به دو کشتی تجاری که درحال عبور از تنگه هرمز بودند، شلیک کرده است
🔴
این حمله تلفات جانی نداشته است ولی کشتی‌ها خسارت قابل توجهی دیدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/132255" target="_blank">📅 16:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132254">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ:  گرینلند باید تحت کنترل آمریکا باشد، نه دانمارک، و ما ممکن است تمام نیروهای خود را از اروپا خارج کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/132254" target="_blank">📅 16:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132253">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ترامپ : ما نمیخوایم دوستانمون رو تحریم کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/132253" target="_blank">📅 16:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132252">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ:  ما به تنگه هرمز نیازی نداریم چون مقدار بسیار زیادی نفت داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/132252" target="_blank">📅 16:39 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
