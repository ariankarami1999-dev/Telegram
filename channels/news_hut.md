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
<img src="https://cdn4.telesco.pe/file/bXca-b8SWx0tTpih1-aWrk_ISuEviuD6adU5B5HPnDPgTUo4dYNkWkX11Ad6rPLAfkUU_12Zs6B6-lRcfvS__Q67sMkXfUw2WAa43yvkzwjKTgHjEOHqoqwAjrukIdM1Il8WHLxkeLWuNHSmsW5ecFXlnQnHtacB5lkhp8CTg0-lWCcKxld0PmpWOOwSZ8Gp0A6fWYrObFqvT7gKpcMgMaWWifcYZeF3M37_mpDtiSdJ3GajspuMv5GUIAHBoNjKs5A9xvRz1axTG4FEaqwqNJsBkWYlNd2FGdmAlVu8l53L0yZKxjjSuQqzSTzTkihcI-2n77rETxU8f6flWfuxsQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 158K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 16:52:31</div>
<hr>

<div class="tg-post" id="msg-68636">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⏸
🏆
👍
ویدیوی کامل مراسم اختتامیه جام‌جهانی ۲۰۲۶.
@News_Hut</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/news_hut/68636" target="_blank">📅 16:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68635">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
حوثی‌های یمن با صدور بیانیه‌ای، از اعمال محاصره دریایی علیه عربستان سعودی خبر دادند.
حوثی ها با صدور بیانیه‌ای رسمی، محاصره کامل دریایی علیه عربستان سعودی را بر اساس معادله «محاصره در برابر محاصره» اعلام کردند و تأکید کردند که این تصمیم از لحظه انتشار بیانیه لازمالاجرا خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/news_hut/68635" target="_blank">📅 15:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68634">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoNHQbd-xLkDa3vrRCSATGXr57hikAM_F55jDRa3qyeCxqsrNjO1Y9ah3dlmpL-1JT7_C_UJn4adC_ZiWS6-V2f6zNAIGuQB1aSmHkxdRx-rZNexbWBHV2z7gKWfkNt4LDyKz-k4qTMkU01PclnUM5vuqKREFvxg2OjWQ15BCmyEHiUIhncGFXz4L2asV3zf4_jCHvIggP4b2o86e3-WO2-fjH8S4KDhQVfHD3bRA3Cxqb6qYBUw57XT_lDuBSdfvwc7KLcDzi_HmAlXO_antnnNDSp_IKhXKPoLPi2H6G34TwaReAq9GudakRs6PKWM3FF4m0LvqtffdyKxoM7viw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز:
میانجی‌ها به ایران و آمریکا پیشنهادِ یه آتش‌بس 10 روزه واسه احیای توافقی که امضا شده بود، دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/news_hut/68634" target="_blank">📅 15:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68633">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acwW63iWBpdFN8eiB8yZQF4RVzZw9EQd8-xLTFRNuxAj9LSy6i_zsH8ZE9_peBTAhncP4ur6wMkLINEHDGynW-YegHueYN_hvVPeQD2pUnymnnlVOMzUpgOveXbXrIXeLlH_YYipsRTN47z0_oGa7dLypK3zZwUNTe0o3V8H6zkTn17b9eS4O0rUDR5ib-ztkwihViZwNa1psgAzX7Tnhs6xg1y5aNQtPucgkGJUMGh74ubPFUo1IXRTMJJHfGlwIj71UmNHgOC-WqLAePGhDed-JcmbMBswdRNxFmI0GraQLkXVsSArkfjlznRPmQhcH3gdzJCQgD_sMiIS1nB-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قالیباف:
آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و ادعا می‌کنند دنبال توقف جنگند. روی هوش ما اندازهٔ آی کیوی مختصر خودشان حساب کرده‌اند.
ما در شناخت این آمریکایی‌بازی‌ها به مرحلهٔ استاد تمامی رسیده‌ایم و بر این اساس آماده شده‌ایم. اقدامات باید مؤید ادعاها باشد نه ناقض آن‌ها.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/68633" target="_blank">📅 15:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68632">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=HM8GCqix2kQgdOuXvbZQ0584I687b_D2K3Ru0wGWnOdjdLxqjO5B5cVheFQzCHrzLBc4uX9GEvGUv33-0W03B5DFKdq9bCgA1FuhrRzi7F7NGInKm6Uk02G36p34s5qPdx95QBTCJYkZkgKR_tJMeeGzyxFPBaqa_eUvwexc--ANvQpyvcxr6ESfg9jj22peY436k2bOpZ-RAOhzQ8bH62Tzeg-nmgLXHQg0PVNFSjG74PdFww9RW1I9easnGgF7RnOxnlvKp00TSuzFFLwAwVjsy1-EETuBicCJYR7fAu3sEImnlYij-jFMqkK5K587Gf_TK8K6MDEmiwlCWp18SYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=HM8GCqix2kQgdOuXvbZQ0584I687b_D2K3Ru0wGWnOdjdLxqjO5B5cVheFQzCHrzLBc4uX9GEvGUv33-0W03B5DFKdq9bCgA1FuhrRzi7F7NGInKm6Uk02G36p34s5qPdx95QBTCJYkZkgKR_tJMeeGzyxFPBaqa_eUvwexc--ANvQpyvcxr6ESfg9jj22peY436k2bOpZ-RAOhzQ8bH62Tzeg-nmgLXHQg0PVNFSjG74PdFww9RW1I9easnGgF7RnOxnlvKp00TSuzFFLwAwVjsy1-EETuBicCJYR7fAu3sEImnlYij-jFMqkK5K587Gf_TK8K6MDEmiwlCWp18SYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل:قلعه نویی موقع جنگ رفته بود بیرون از کشور تو امارات و ویلای خودش تو آلانیا ترکیه بعد اومده به ما میگه شما تو غار بودید.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/68632" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68631">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/68631" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68630">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfcKiEJzsmAHRXSER5-zweYnhjzh4Ipvrb1pFXHsWMFYreLpah_Oht4vdVQrjQnFyhS7zLvYZy_eE0YNcwNVpKP82KjxwbMQpuYsScQV6bj4K7G5Pk4JkpomwMrNRvSsfmlVh1_9O-JU6IwtMsa63h5-8fYbBvbOSVe7ceTlqLhnhFST9HOu8LuCJX-6sbpaHJWfAgqcRKePX_aaw6OFuS4oLIsn5JFrLqxLX9_yzByyG6lJm9AAxFCB2EtJElvCPnyqFULSsrluwFru-wiGrYF19wylBBPXWUM02vdWAq5ZxcvxZvRISKJGwEngRm8tUX1tL5dzx2jgJ6sRF99gwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/68630" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68629">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBv1k09jaXvFsQEkmNUC2JNkDNzUI9eT9Khrt2JE_7uZE19M4S2W4UDDVRng53XEyjoTBMvxHsPWF8Ujg2mJCxarkD22Z7kpwNxKXnQrXqEiakD2RV9bDGeW7014dX10bTtGmTdQTSTZtLQg1WxVuSdvP5LAJgYwX5AtmrqF7f1E60JJzmq84RpZsaa9cReha30i2OeGvHVKSY-BBkpdN-2hBsCRgkxEA8M9fwKfe6mqF0R5EZfpYai9dYAT7p9DyrouCTN8DYg3Wp8EdPMyDvxoC_UYP3tgst5Mihba_AMQFGsMNGfdGhOgcRdeq93KRn5IedHUh3_NLr0asgYQwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عبدالله شهبازی :
شطرنج پیچیده این جنگ داره به آخرای خودش میرسه.
به نظر میاد جمهوری اسلامی توی این بازی مثل یه بازیکن مبتدی عمل کرد و ترامپ هم در حد مگنوس کارلسن ظاهر شد.
ترامپ طوری بازی کرد که انگار حسابی گیر افتاده و به توافق نیاز داره. امتیازهای بزرگی داد و با طعنه و کنایه، رسانه‌ها و فضای مجازی رو هم با خودش همراه کرد.
این نقش رو اون‌قدر حرفه‌ای بازی کرد که جمهوری اسلامی باورش کرد، فرصت‌های طلایی رو از دست داد و دنبال امتیازهای بیشتری رفت. در نهایت هم نتونست یه «استراتژی خروج» انتخاب کنه و مسیرش رو متناسب با شرایط تغییر بده.
حالا نشونه‌هایی از اجرای یه طرح غیرمنتظره دیده می‌شه؛ طرحی که اگه عملی بشه، ارتباط مناطق جنوبی از هرمزگان تا بوشهر و شاید خوزستان با مرکز کشور قطع می‌شه و عملاً حاکمیت جمهوری اسلامی بر جنوب ایران از بین میره. به نظر نمی‌رسه اجرای این طرح نیاز به ورود گسترده نیروی زمینی آمریکا داشته باشه.
⏺
اگه این سناریو موفق بشه، می‌تونه شروع فروپاشی حاکمیت جمهوری اسلامی در سراسر ایران، طی چند ماه آینده باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/68629" target="_blank">📅 14:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68628">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/357e3ebc2d.mp4?token=fgFvFkSOaEcZ2PFDqnuuVpKHA3COgFuYsn_9afzlhe1YK7ifNopx3oPhq3Al07O85D_L0RgoFuppZAF_l0r_AVtoSdYyOqijwNiKPvzJeVw_beG6zbX3YHU9_jYDxnwdJ639IJPSBgBSSRVxCoVpWO2c6e8tdtsWtE9KZLbIiXcR7wWo1DcGXBMWdo1xubi891cCYThaRnBtldrVeCBVKV2DQ0da3DhUQsuRqWBu9eH4qqpTkmdixaKOgCIoS-X6qCEkpM56-0RL7eWofi8XRquaT7lVCLkpw8MNRAkfcCRDhuT5oXfm21otXHZ4DeesNr29oXedBPXTXQWZlg7GaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/357e3ebc2d.mp4?token=fgFvFkSOaEcZ2PFDqnuuVpKHA3COgFuYsn_9afzlhe1YK7ifNopx3oPhq3Al07O85D_L0RgoFuppZAF_l0r_AVtoSdYyOqijwNiKPvzJeVw_beG6zbX3YHU9_jYDxnwdJ639IJPSBgBSSRVxCoVpWO2c6e8tdtsWtE9KZLbIiXcR7wWo1DcGXBMWdo1xubi891cCYThaRnBtldrVeCBVKV2DQ0da3DhUQsuRqWBu9eH4qqpTkmdixaKOgCIoS-X6qCEkpM56-0RL7eWofi8XRquaT7lVCLkpw8MNRAkfcCRDhuT5oXfm21otXHZ4DeesNr29oXedBPXTXQWZlg7GaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
«اگه اون دسته از آدم‌هایی که واقعاً می‌خوان برای ایران یه کار مثبتی انجام بدن، قدرت رو به دست بگیرن یا مسئولیت مذاکرات رو بر عهده بگیرن، اتفاق خیلی مثبتی خواهد بود.اما امشب هنوز تو اون نقطه نیستیم.
به نظرم دنیا داره به جایی می‌رسه که مشخص شده حداقل یه عده توی ایران می‌خوان تنگه هرمز رو در اختیار بگیرن و ازش به‌عنوان اهرم فشار علیه دنیا استفاده کنن.
دنیا باید تصمیم بگیره که آیا می‌خواد اجازه بده یه آبراه بین‌المللی دست کشوری مثل ایران باشه یا نه. این کار کاملاً غیرقانونیه و اصلاً قابل قبول نیست.
آمریکا هر کاری لازم باشه برای حفاظت از کشتیرانی جهانی انجام میده، اما وقتشه کشورهای دیگه هم سهم خودشون رو ادا کنن؛ چه با تجهیزات نظامی، چه با حمایت مالی، تا این بار فقط روی دوش آمریکا نباشه.
حافظت از کل دنیا برای همیشه، وظیفه آمریکا نیست.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/68628" target="_blank">📅 13:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68627">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb49be0645.mp4?token=fksMqsEzF41YNTDu78fgjx8PSlWeZiVyWk7WHYY51t8Gpvj5lF3jIWHmKeQBxv20Elc6V7TNFSczCs8FkLqCV3zPp2wwA3ozkyRoAI-6bQ7E1BsRn3b-LaRhkb_VgxC5-Lqx34wbNt_p7Y2LlKq3z6EbyjLzd48UQTnZ7gfstS9EoWZJDk6bMxX3Fs46cB5GkZkFyCH-eHyEEVptRJdZxngRb-W1PiPHylogHxxCEPecJRDdj4UbnVFqrEe8pUcZ1x03Un_YA_LAynq8vHGpZgmJMidEfrns3sDGBXN0Gy_Asxf3ZruGwhgmO0PG3oo3_-41wd3xeM2__YhESXj7oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb49be0645.mp4?token=fksMqsEzF41YNTDu78fgjx8PSlWeZiVyWk7WHYY51t8Gpvj5lF3jIWHmKeQBxv20Elc6V7TNFSczCs8FkLqCV3zPp2wwA3ozkyRoAI-6bQ7E1BsRn3b-LaRhkb_VgxC5-Lqx34wbNt_p7Y2LlKq3z6EbyjLzd48UQTnZ7gfstS9EoWZJDk6bMxX3Fs46cB5GkZkFyCH-eHyEEVptRJdZxngRb-W1PiPHylogHxxCEPecJRDdj4UbnVFqrEe8pUcZ1x03Un_YA_LAynq8vHGpZgmJMidEfrns3sDGBXN0Gy_Asxf3ZruGwhgmO0PG3oo3_-41wd3xeM2__YhESXj7oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
ایران کشوری ثروتمند است. یکی از دلایل وضعیت نابسامان ایران این است که این رژیم هر پولی که به دست می‌آورد — چه از طریق لغو تحریم‌ها و چه از راه فروش نفت — صرف سرمایه‌گذاری در حزب‌الله می‌کند؛ آن‌ها در حماس سرمایه‌گذاری می‌کنند...
آن‌ها باید میلیاردها دلار را صرف سازندگی کشورشان کنند، اما در عوض، این پول را برای حمایت از تروریسم به کار می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/68627" target="_blank">📅 13:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68626">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/425aec1f1e.mp4?token=cd-67mLRbYmdC4nQdCPq9YhHNtjgah8Y7xk-TcUSTQEn3yESPFLOwCZv78aIvz8Cc-pxOdVEDyIQ5eYg9wfFmBL1JQQs-mL4C4AY08zJ79vUo9FYlPqbQWSs0lt4ePCdQ2HxLvzfLGC71aZyBFkiYU368eZb1hOoqv0tZ5HzP9fZ-S8PXavY7f4DbA8rNoeoLHf5vEBcQJbA3C4T6UtmMxWEo5vtdQgimhx4W9EVDopBLbjqCVU_7dPwAHPs_jgnSczjaNXSaOyGapwuwJEnmOPrU_UXg52lV9FyX204doVo6avRC7LxkfUjLuC69pe2zGprVt4joH7DhPxP8Kl67w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/425aec1f1e.mp4?token=cd-67mLRbYmdC4nQdCPq9YhHNtjgah8Y7xk-TcUSTQEn3yESPFLOwCZv78aIvz8Cc-pxOdVEDyIQ5eYg9wfFmBL1JQQs-mL4C4AY08zJ79vUo9FYlPqbQWSs0lt4ePCdQ2HxLvzfLGC71aZyBFkiYU368eZb1hOoqv0tZ5HzP9fZ-S8PXavY7f4DbA8rNoeoLHf5vEBcQJbA3C4T6UtmMxWEo5vtdQgimhx4W9EVDopBLbjqCVU_7dPwAHPs_jgnSczjaNXSaOyGapwuwJEnmOPrU_UXg52lV9FyX204doVo6avRC7LxkfUjLuC69pe2zGprVt4joH7DhPxP8Kl67w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری:
آیا احتمال تجزیه ایران وجود داره؟
⏺
مطهرنیا:
امکانش هست ولی احتمالش کمه.
همیشه این امکان واسه کشوری مثل ایران وجود داره ولی تجزیه ایران نه به نفع امریکاست نه اسرائیل.
اونا خودشونم خوب میدونن تجزیه ایران بیشتر به نفع روسیه و چینه.
پس امکانش خیلی کمه بخوان بفکر تجزیه ایران باشن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/68626" target="_blank">📅 12:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68625">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rr9vzrQR-g5iR6_u3iim3Ve9Vr5LzV09-fl8neG05_uKsbhtk--cYDvy4qgBQSBKg9Q0mnP21Tr18GEK3k5tEYGnrIwhwzU23Vh05niWLDmjx0V84St5n10WJ94zbUeTMin3mtpMOP1KVao9VRH-UHX68gM6uCXhZlbZPYp8K-yNJPk7yby-zZspeGALrn_n7UMIHmBw5MDv7mfcNq0QzGhos-JvyorXObBjQ7ZDgK4qsXpTKnWgAlmoDLmINre4FFA-oJmLW3lkvY4s_6A9wo-yaMdkb_9uyROcAy5XkahjixzOKaz6arHMb9do-T2i4KbfZPKj9fKOEiHeQz-jCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مسعود قهرمانی تیم اسپانیا در جام جهانی رو به دولت و ملت اسپانیا تبریک گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/68625" target="_blank">📅 12:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68624">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5ad1a2f2a.mp4?token=bJyerNeJsP27ZSYsOjiF8qK4aml3lyYawl8C63l_ke6EzN9zoTayy205a8RqMEUI0esY8EpvNAzur9HhN1FswDfdnUdYpv_2BITci6vHKS_1H6stzn_ZyVNQze2Ix-xTMJvi1Ykzxh_jHy0_923oGbNnYlg5ZQiTjM5XziDqdhp7lVm56Ntxpp_0BLJrcV6yuA7KIuOWXpqhJhlg1Tn7VSd3nwmnpH1cOsZ-A_I1VgJz2Je8sTSLE7g33XqyCmvtwgtltuLqmftBBMkO194FGHvT9bjH3vYpY9o_F3T9Tdcj6foBmVEvWZ9CiQsHAQBmTipbwGKGHdrU_hczvJMR0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5ad1a2f2a.mp4?token=bJyerNeJsP27ZSYsOjiF8qK4aml3lyYawl8C63l_ke6EzN9zoTayy205a8RqMEUI0esY8EpvNAzur9HhN1FswDfdnUdYpv_2BITci6vHKS_1H6stzn_ZyVNQze2Ix-xTMJvi1Ykzxh_jHy0_923oGbNnYlg5ZQiTjM5XziDqdhp7lVm56Ntxpp_0BLJrcV6yuA7KIuOWXpqhJhlg1Tn7VSd3nwmnpH1cOsZ-A_I1VgJz2Je8sTSLE7g33XqyCmvtwgtltuLqmftBBMkO194FGHvT9bjH3vYpY9o_F3T9Tdcj6foBmVEvWZ9CiQsHAQBmTipbwGKGHdrU_hczvJMR0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنت‌کام ویدیو ای از حملات آمریکا به ایران منتشر کرد.
تصاویری از برخاستن یک جنگنده F/A-18F سوپر هورنت نیروی دریایی ایالات متحده — مجهز به بمب‌های گلایدکننده AGM-154 JSOW — از ناو هواپیمابر کلاس نیمیتز، و همچنین شلیک موشک‌های کروز BGM-109 تاماهاوک از ناوشکن‌های موشک‌انداز کلاس آرلی برک، در این مجموعه گنجانده شده است.
اهداف ثبت‌شده شامل یک سامانه پرتابگر متحرک (TEL) و یک پرتابگر پهپاد است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68624" target="_blank">📅 11:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68623">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60340234e2.mp4?token=PKP4ucWphgWdYy5FwCpfUTsAXkyatjQIj08y54xSYuv8Y073Z6hJsMMIP9jbRnZ_zJJSYxAjUiQPu7CvK0DkAFm32ap19rEJED8zjiMfwcg2r6UOEjRLhfgFFi2xlI-skBMZm8-Uzh49Z2ozLojDeV3LZ8cNGaFINj8BWuPgoPfsaE_7VTRanxSgVWv5Ubc_VaBnPO505xeVWdcSAiIZMYHIjqti-X4fiy79g1Lmwt6yCrV7yT-HagqOSZq0WqS6l8g4WI8sTX43vn9vb1g2B8a9KpbgaG7MRNN17oAwGMTFeALczcW0hNWjLzWWenh7uVQVnlsn1tivhijxdXAL0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60340234e2.mp4?token=PKP4ucWphgWdYy5FwCpfUTsAXkyatjQIj08y54xSYuv8Y073Z6hJsMMIP9jbRnZ_zJJSYxAjUiQPu7CvK0DkAFm32ap19rEJED8zjiMfwcg2r6UOEjRLhfgFFi2xlI-skBMZm8-Uzh49Z2ozLojDeV3LZ8cNGaFINj8BWuPgoPfsaE_7VTRanxSgVWv5Ubc_VaBnPO505xeVWdcSAiIZMYHIjqti-X4fiy79g1Lmwt6yCrV7yT-HagqOSZq0WqS6l8g4WI8sTX43vn9vb1g2B8a9KpbgaG7MRNN17oAwGMTFeALczcW0hNWjLzWWenh7uVQVnlsn1tivhijxdXAL0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در مورد ایران:
این کار بسیار بزرگتری است که ما انجام می‌دهیم. ما کار کوچکی برای جلوگیری از داشتن یک قابلیت خاص توسط آنها انجام می‌دادیم.
حالا ما فقط به آن پایان می‌دهیم. بنابراین واقعاً همان کار نیست. کاری که ما اکنون انجام می‌دهیم این است که هرگونه شانسی را که آنها بتوانند موشک هسته‌ای داشته باشند، از بین می‌بریم.
اگر به آن نگاه کنید، پس از یک هفته و نیم یا دو هفته [از شروع جنگ]، ما آنها را از [توسعه احتمالی] آن متوقف کردیم. اما من نمی‌خواهم از کلمه احتمالاً استفاده کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68623" target="_blank">📅 11:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68622">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVi4uW7x6J6g69-LaYnhYQa12tUpi6VdUwpQSAm7RIdXzMmQTANKOs_M8C2HMq5WQudL3A6q9_J3PPSyP0HMTc3fTdNRYNZW9YRbQagNR5wRDnLWpelKJ6btkYMKAKvdl3AhCNasXghonyZZwED-zJQtG6Dk6-XDJSIU9RyKa-hJM8hmzHQZKteQSFW3Hp0QRdG3DRD4Q24kW0uma886p49bXbxEJaY-EI2NC7nLDP7N7D6n8icGkpBAyVNlPSruWCt6JHZn8W71zMCWjRTnHBJY9PKwUL5YTt5Vm6Si1s2iDCrXFP7WhIe5nyh9wWNLt9V7N2Xiejpk6G_rPliiLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📢
نیویورک تایمز:با نزدیک‌تر شدن دو طرف به یک جنگ گسترده‌تر، یک نیروی نظامی دیگر آمریکایی جان باخت.
پنتاگون روز یکشنبه اعلام کرد که سومین عضو ارتش آمریکا در جریان یک آخرهفته از حملات متقابل کشته شده است؛ در حالی که جنگ با ایران شدت گرفته و ایالات متحده شروع به اعزام هواپیماهای جنگی بیشتری به منطقه کرده است.
این سرباز در شمال عراق هنگام عملیات برای از بین بردن یک پهپاد تهاجمی ایرانی که سرنگون شده بود، کشته شد. این حادثه در میان زنجیره‌ای از حملات فزاینده رخ داد که تقریباً آتش‌بس حاصل‌شده در ماه گذشته را از بین برده است.
هیچ نشانه‌ای از دیپلماسی یا مذاکره میان دو طرف دیده نمی‌شد و مقام‌های آمریکایی که به شرط ناشناس ماندن صحبت کردند، گفتند که ایالات متحده در حال اعزام هواپیماهای جنگی بیشتر به خاورمیانه است؛ اقدامی که برنامه‌ریزی آن حتی پیش از کشته‌شدن‌های اخیر آغاز شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68622" target="_blank">📅 10:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68621">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ba03b9d75.mp4?token=Tmo_xIc11f1E9JsG4eRog9yFkxFu1bL774aZ8u8N0bHPWhpRIjj7Yat019xR0xKlateKRYUKYDFqiCefc5QXxJQxZKLCZmwbQrxEU12ZFmJ4xConqFmUut1YXEQ57oUh4Knks_I8Ggun-czqBSPZy-7mY6wsHhH3M_wBe6SK1FMSLOaoofFFyy8-_k2DVyaSSoiGlWkqBCchMtALWKk-avdGLY-B10v0s4hnU1F7di-FGbSVXhACqas0ZEv0F9X7EyR3asxyiv3MbW24Rm4jlFVpTeSxCRnzNlBJP_tltHhXFIsv_jUR6PXTu0_lLJGxEngv1O3wtMI6pP6e45KtwikGdoj5DjbkUK_CZ5HgmRi8LJl9MXbejYENyqtiD5MxWSO8dmbQZXsbxRZxHxdu9MBArxlFqgQK--NPkk2Lg3Qv_bl4Sw6sGJ5Gx4zaCO4xb_Cz-Jh-qQ1uoQugNZYl-vw93JJujAbyCt_F32kuMH1u_yBCH9B9q4ncWlfAfGcT-eUFn7uYxcatItNtKM_dVlYdptrqyc7yhLqQkOmkkJ9JG6IStOUYqEd3l07rp1pjMVxp3MRs0fANmWUNfJhKgQSvMNVKBDk1wn-zc4I0UYFaNVQx5QM3caXHHq7XHMtq9ClBTkSseD9VuMTerLY7dnLB2OXTMfLfJD81ZzTdZ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ba03b9d75.mp4?token=Tmo_xIc11f1E9JsG4eRog9yFkxFu1bL774aZ8u8N0bHPWhpRIjj7Yat019xR0xKlateKRYUKYDFqiCefc5QXxJQxZKLCZmwbQrxEU12ZFmJ4xConqFmUut1YXEQ57oUh4Knks_I8Ggun-czqBSPZy-7mY6wsHhH3M_wBe6SK1FMSLOaoofFFyy8-_k2DVyaSSoiGlWkqBCchMtALWKk-avdGLY-B10v0s4hnU1F7di-FGbSVXhACqas0ZEv0F9X7EyR3asxyiv3MbW24Rm4jlFVpTeSxCRnzNlBJP_tltHhXFIsv_jUR6PXTu0_lLJGxEngv1O3wtMI6pP6e45KtwikGdoj5DjbkUK_CZ5HgmRi8LJl9MXbejYENyqtiD5MxWSO8dmbQZXsbxRZxHxdu9MBArxlFqgQK--NPkk2Lg3Qv_bl4Sw6sGJ5Gx4zaCO4xb_Cz-Jh-qQ1uoQugNZYl-vw93JJujAbyCt_F32kuMH1u_yBCH9B9q4ncWlfAfGcT-eUFn7uYxcatItNtKM_dVlYdptrqyc7yhLqQkOmkkJ9JG6IStOUYqEd3l07rp1pjMVxp3MRs0fANmWUNfJhKgQSvMNVKBDk1wn-zc4I0UYFaNVQx5QM3caXHHq7XHMtq9ClBTkSseD9VuMTerLY7dnLB2OXTMfLfJD81ZzTdZ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
«سرباز روح‌الله رضوی» مجری یکی از برنامه‌های شبکه خبر، اهل کشمیر هندوستانه
🇮🇳
و پدرش به خاطر علاقه‌ای که به روح‌الله خمینی داشته، اسمش رو گذاشته روح‌الله؛
⏺
حالا این ویدیو از این مجری حسابی وایرال شده:
🎙
روح‌الله رضوی:
با سنگ، تیرکمون، کوکتل مولوتوف و هرچی که میتونستیم، رفتیم واسه تعطیل کردن سفارت انگلیس...
🎙
دهباشی، مستند ساز:
به این حرکتتون میگن هرج و مرج طلبی، یه رفتاری انجام میدی که هزینش رو یه ملت باید بپردازه.
تو به عنوان یه مسلمون که به حق‌الناس اعتقاد داری، بنظرت میتونی کاری بکنی که هزینش رو میلیون‌ها نفر دیگه بدن؟
🎙
روح‌الله رضوی :
اسمش رو هرچی میخواید بذارید. وقتی همه‌ی مردم بخوان یه کار بد انجام بدن، شما سکوت میکنی؟ من اینجور مواقع نمی‌کشم کنار...
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68621" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68620">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⏸
ویدیو کامل مصاحبه جواد موگویی با عباس عراقچی درباره حوادث یک‌سال اخیر از مذاکرات تا اعتراضات دی‌ماه و جنگ:
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68620" target="_blank">📅 09:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68619">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DU2mQgwPPpyeadnPaC7b8QjEsJbE4SGsgk0pZCAmweuXdJvWlpoQZ431_lHBc7ei8xTtVnHPtaNo7xF6OvPtkCHPyGGdSG5hm9SebhwDYphxyHp-lV1iKwr97AfBIW7v32EL8gGfPMFBb18JPUb7sD0uqeGX7SKCjHAYqFsxWSWCOa7h-VFWstCDzzlswvLKhm6PSyn5p9t_n3rWbpbvmHd3GEZfaC5N5LVeMd4RHb8OPJUD59uUFNpPjSgiBwElPRTfclFj60RbXKSf8DDarVo8uXH7YyqMLqHaAntbFYswAwHhsX0e5ZZn-s8enOeyccNsDFx1lY3ObPAeRRCSwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68619" target="_blank">📅 03:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68618">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGZloMVydgeS1So-w3InX_MysJTwgdgj5ihXKaxRsL-muESgz-cffLjSkX_l4uID85gYwl7FGAe-Y485YbKrRySb9BoR-h2w4QoLOQsZj72PIUXuvSGRetyZphq44OMaDH12d5fDLvkFbhCEXvfVJC-quevNA4g65viNrY4klUl48Dtq_qQ_4LkQEfL082KskGlEPU4tGYCsxMljY0LwthvkPzp-ynQM1RAVQGFiI7infu7k2ATXgxui0SdLccqXjugaBcLGf8XNlDhPchhv120CYIJzgqCZHsO0wvlII-keBeWEiiFA0isffYJdwXe0eeyhJ1kvHfFYkIjwqGlThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی در نزدیکی سواحل عمان مورد اصابت قرار گرفت و دچار آتش‌سوزی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68618" target="_blank">📅 03:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68617">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68617" target="_blank">📅 03:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68616">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
انفجار در خورموج استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68616" target="_blank">📅 03:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68615">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00f692dfa.mp4?token=pN9RC_LEhR2zs56f_N7pSobUUX93lz2MP-Hock2VJwhjdd-AIaWP8cRXeS8OFNBWv7qXADhgJOoBkY9BbYAwIV4cGYwYBkviuQdh_TmeawJGanyauFipA4nwGLKKpc8OO425SPH5ty9IMwsr4HQLC0nOtB1-2_90vcMb1fB5AloaXLzYBpyfWST7ALuRaD1J9-eDWfqcuhhjYFwiTJMVlawqT8fOIVQEhfd5kjT1MuEJFGypkkWvmKwL92oXN5pxvOo5jf_bkmzzXNGOFMfuNwGOvTb2y3s8sVfrn7uDcoyaM1lXxFJS-yJrzbkHmhxzulkD8Ffglj46tTjLjBOOTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00f692dfa.mp4?token=pN9RC_LEhR2zs56f_N7pSobUUX93lz2MP-Hock2VJwhjdd-AIaWP8cRXeS8OFNBWv7qXADhgJOoBkY9BbYAwIV4cGYwYBkviuQdh_TmeawJGanyauFipA4nwGLKKpc8OO425SPH5ty9IMwsr4HQLC0nOtB1-2_90vcMb1fB5AloaXLzYBpyfWST7ALuRaD1J9-eDWfqcuhhjYFwiTJMVlawqT8fOIVQEhfd5kjT1MuEJFGypkkWvmKwL92oXN5pxvOo5jf_bkmzzXNGOFMfuNwGOvTb2y3s8sVfrn7uDcoyaM1lXxFJS-yJrzbkHmhxzulkD8Ffglj46tTjLjBOOTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پایگاه امام علی در چابهار مورد حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68615" target="_blank">📅 03:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68614">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fX-CcfE16KibuEIeaL-j0lKp5i7UZox0XC_va3fphMd4HlqN_d24Y1OPFXyVGxGLWfCanPvhmunhr0tOepp9OO8yFfkI-Z0vloAj93uuWpYqKgvy952FUl_JABbbaD3rDZYS5DSTAjk5101SG8SLmQduk2x6THW7a-0wXTN8YQD4m1_oa4SRvi0CfnU8-_6QqqvdN3yn4rr34ncZNbcWJ9nPt9TLff6nb96bf2KKAR3RTPUinQORgGlvhEqC5AN4X47kHAjbcERAq_GXfs9n1Ong3NGtRMUHbiQt68PrjfHfRerckNYdbGKaVVtKgvxSiKUhEmYpOCjSKshWWMkM8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ماهشهر
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68614" target="_blank">📅 03:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68613">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
منابع حکومتی:
انفجارهای شدیدی در شهر رأس الخیمه، امارات متحده عربی، رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68613" target="_blank">📅 03:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68611">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521034efe8.mp4?token=cVohRYuneJgkDS8JcJQvrU3Gky8b6eN6cQEb3o8OeYH_OKaH_SZL8WnP7KFPLD2sbjbPqCHm3qmUscf4lvdHWVl2KY21VLelNPu-xfctWfTK6Bw1FTqGSmG0YGCTbwRCEcJoNRjnmu42Deqhtk-Oi0SkxGPVO6qGJyYJOaC6EsUxHRGT9zJdBZsUmsUoN_vMYEmXNiUGRc8MX7NjJ3HN3OsqHTElDJ7_cDt8ahZeQpQqnnz6bjNRtUacdAdiLB0Hy-N5gE5Oze5mZFkJWLqyMb1wHGGHy2Xr1yh2-ASNsAna2cNcTvzxyWN_4WYhUuH6SuMHFrrBkmozdUcS4JDr3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521034efe8.mp4?token=cVohRYuneJgkDS8JcJQvrU3Gky8b6eN6cQEb3o8OeYH_OKaH_SZL8WnP7KFPLD2sbjbPqCHm3qmUscf4lvdHWVl2KY21VLelNPu-xfctWfTK6Bw1FTqGSmG0YGCTbwRCEcJoNRjnmu42Deqhtk-Oi0SkxGPVO6qGJyYJOaC6EsUxHRGT9zJdBZsUmsUoN_vMYEmXNiUGRc8MX7NjJ3HN3OsqHTElDJ7_cDt8ahZeQpQqnnz6bjNRtUacdAdiLB0Hy-N5gE5Oze5mZFkJWLqyMb1wHGGHy2Xr1yh2-ASNsAna2cNcTvzxyWN_4WYhUuH6SuMHFrrBkmozdUcS4JDr3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت سربندر ، ماهشهر استان خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68611" target="_blank">📅 03:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68610">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f087874ede.mp4?token=MeH2UzZzJ_w3kEtZdYNH-VZQF7UJep6xyX2sbCXq3esk5eq7wAvElSvPMoQrbD1uW4LxvNIoGyP1rP1vqvrNMQr1ie_XMJXT_s2Fpgwwy7ptzRR34nwHiSKHmgzZl-Y7XbNWXIjdHByS_WvTsuAk1Sob3vyeXUibnRXm_PgPLaZ6AtWhkrUMaTDyVlpyA_I5OWMHSQD7YlL-dPbWhknHYHXWBkh3H_LsEOX8YjHu80k19d2Ir5toZoA-gt5q1Yj-b8Rr31sGiWU3zpIm3h-LNay0kQq5HB05FOzQFQfSDd8S4hiVkLryoV5xuc-Cff6qdcgDNkZd88PKF7rerHf8QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f087874ede.mp4?token=MeH2UzZzJ_w3kEtZdYNH-VZQF7UJep6xyX2sbCXq3esk5eq7wAvElSvPMoQrbD1uW4LxvNIoGyP1rP1vqvrNMQr1ie_XMJXT_s2Fpgwwy7ptzRR34nwHiSKHmgzZl-Y7XbNWXIjdHByS_WvTsuAk1Sob3vyeXUibnRXm_PgPLaZ6AtWhkrUMaTDyVlpyA_I5OWMHSQD7YlL-dPbWhknHYHXWBkh3H_LsEOX8YjHu80k19d2Ir5toZoA-gt5q1Yj-b8Rr31sGiWU3zpIm3h-LNay0kQq5HB05FOzQFQfSDd8S4hiVkLryoV5xuc-Cff6qdcgDNkZd88PKF7rerHf8QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
منتسب به تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68610" target="_blank">📅 03:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68609">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
تسنیم:
دقایقی قبل صدای انفجار در شهرهای تبریز، چابهار، کنارک، بندر ماهشهر، بندر امام خمینی (ره) شنیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68609" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68608">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در بندرامام و ماهشهر
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68608" target="_blank">📅 03:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68607">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68607" target="_blank">📅 03:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68606">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6436592f1.mp4?token=EGPg9G4zCM-Yu7jFDD-rKnKw3SJZrYnGUfttgolBLaKdkbMmvbKGDBqbWXFuFomScQURuRfzRBq_TEV0rJWmdPFbhuzUz81dxSZeXFBhh5yCkAEKLu00ymwBzd3pqiEtskgjVFbYuS8BAp_pAaNFSRzE8k0B6-vs8dITnlqkwI55d-nUoyzcHRJF86EWXW_A5k--AkjW5WygRmpyZoH3vf9GU_FMbpM-2YfWBvNq3KJB8U7Uhehntl2znbe3fPoFIakOZ86vCcSfuIbbEQympFkGCF4kmybAlp7EQ1ORY6Iv2d39c3Z5-DXmuQA3qER2ZNjw4W-KxdzVhsu9k1COCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6436592f1.mp4?token=EGPg9G4zCM-Yu7jFDD-rKnKw3SJZrYnGUfttgolBLaKdkbMmvbKGDBqbWXFuFomScQURuRfzRBq_TEV0rJWmdPFbhuzUz81dxSZeXFBhh5yCkAEKLu00ymwBzd3pqiEtskgjVFbYuS8BAp_pAaNFSRzE8k0B6-vs8dITnlqkwI55d-nUoyzcHRJF86EWXW_A5k--AkjW5WygRmpyZoH3vf9GU_FMbpM-2YfWBvNq3KJB8U7Uhehntl2znbe3fPoFIakOZ86vCcSfuIbbEQympFkGCF4kmybAlp7EQ1ORY6Iv2d39c3Z5-DXmuQA3qER2ZNjw4W-KxdzVhsu9k1COCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله موشکی آمریکا از مبدا کویت
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68606" target="_blank">📅 03:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68605">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
خبرگزاری مهر:
یه پهباد رو زدیم سرنگون کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/68605" target="_blank">📅 03:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68604">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
شنیده شدن صدای چند انفجار در بندر ماهشهر و بندرامام
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/68604" target="_blank">📅 03:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68603">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2e2ba6741.mp4?token=EGdGg_Q6Ko70IgEUsvPRvA45WOYXKgefDDM590UjHjyad8fYcTjD65Ixv2qF2Uhpg36a1IO64mnhJRUs-CdOe2AQCdafezmPZysxF5zH9fN7gXRTg4SXpJKeHceiyW_HpigiDL1ou5zvq4tVPGI0H5as7ETua1k9128rO7fR94jhNUHH6u3wdUD6aZaXk155fpOdqyxca6SPIaBCuUiGXaFL6D_V6SALBQlZJlFxasRsQs2LIREqRDm9BWlkD0tTskQT6lILcEnesbp_WXzhfBxOeibcq-n1vxnZk12060KyfjyOe6Xkpcf2MCf-LeNFvE7Zp4Ssf2djrYWQ3p-5YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2e2ba6741.mp4?token=EGdGg_Q6Ko70IgEUsvPRvA45WOYXKgefDDM590UjHjyad8fYcTjD65Ixv2qF2Uhpg36a1IO64mnhJRUs-CdOe2AQCdafezmPZysxF5zH9fN7gXRTg4SXpJKeHceiyW_HpigiDL1ou5zvq4tVPGI0H5as7ETua1k9128rO7fR94jhNUHH6u3wdUD6aZaXk155fpOdqyxca6SPIaBCuUiGXaFL6D_V6SALBQlZJlFxasRsQs2LIREqRDm9BWlkD0tTskQT6lILcEnesbp_WXzhfBxOeibcq-n1vxnZk12060KyfjyOe6Xkpcf2MCf-LeNFvE7Zp4Ssf2djrYWQ3p-5YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات آمریکا از کویت به ایران
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68603" target="_blank">📅 02:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68602">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcqL3yCcGx08rmC9osjUZimMS6KrnoLRWjcegQVksFr0ap2X1YTzICLGYyZvofygiVwTJaQUAF2S0Fef6XEGab6MSjLdmhmAq9wVayf8PomLXW6-RwRCvsVFXxjZ_ILH_oACuPMmOI88lpTysAK1G7z2PB_rWkohjxJW-9SqQHn7OE0YN_Pvt0HgTRMndgCIrQMOIN0wqi1xO0pV4Vo5zF_pyfdjVXeR5EfH-ynVQAY5jnQ_fDCqku4aze2iFYyFm7NfKvuODYJKAjAQwYmqueSuaocKcFtNd4wO-wEqMWZIuA0aaVTk788st9L_GPa1saYe60YcytQ9enik90qGdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنتکام:
امروز ساعت ۱۹:۰۰ به وقت شرقی، برای نهمین شب پیاپی، موج جدیدی از حملات علیه ایران را آغاز کرد. این حملات با هدف تضعیف مستمر توانمندی‌های نظامی ایران که برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامیِ در حال عبور از تنگه هرمز به کار گرفته می‌شوند، ادامه خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68602" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68601">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68601" target="_blank">📅 02:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68600">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز شدن دور جدیدی از حملات آمریکا به ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68600" target="_blank">📅 02:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68599">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
خرم‌آباد چندین انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68599" target="_blank">📅 02:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68598">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
انفجار در بندرامام
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68598" target="_blank">📅 02:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68597">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c5e9c78c.mp4?token=sWjeJLtX8cTCFKb4877iV3l82B3SRFwP0maAp0ZwzWOREXG9SUa4OmpzXj3l5BvRNLP_Cy-fbUoPys9zGyAGSlZYipPiFrRKk7zZfE_OjzFzFhVTOjHP83ALZTD1K46NDMWMDtQyT4r_3fKMcz_aqwqqelS0jSo_l2d6i0Yg_WznqZamEDTFntNw4SPnA6Ar3vqaxuqgR31I9UIHKso6QkgPc917fFsjX8X6snyhJ8dJ8V80tuP3g6iJZdEXFxcegvLnuoj_Bs_H5vhwM6ClpeigSoiHXn-J-q8KqxQP0tFJoRr_-3OXyMWyHwIBfbwlyLeaQcltpZSqATLouNwk4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c5e9c78c.mp4?token=sWjeJLtX8cTCFKb4877iV3l82B3SRFwP0maAp0ZwzWOREXG9SUa4OmpzXj3l5BvRNLP_Cy-fbUoPys9zGyAGSlZYipPiFrRKk7zZfE_OjzFzFhVTOjHP83ALZTD1K46NDMWMDtQyT4r_3fKMcz_aqwqqelS0jSo_l2d6i0Yg_WznqZamEDTFntNw4SPnA6Ar3vqaxuqgR31I9UIHKso6QkgPc917fFsjX8X6snyhJ8dJ8V80tuP3g6iJZdEXFxcegvLnuoj_Bs_H5vhwM6ClpeigSoiHXn-J-q8KqxQP0tFJoRr_-3OXyMWyHwIBfbwlyLeaQcltpZSqATLouNwk4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
چهار انفجار در سایت موشکی تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68597" target="_blank">📅 02:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68596">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
صدای چندین انفجار در تبریز شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68596" target="_blank">📅 02:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68595">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-S2ERIJH6Eb7epiAdmUNhJ6pEp4wxId05mhEXt4h9ea0BtzCGaDUxUmnZ0BTIR3YWfPwyI-0n6xf6TFlDDKaqRWN3XvZoHM0BzUW3RuxqnPuGaXexfYvM6EnYZYFRE61kMXHxxLNkxsWPHJFV3Y-kPae4P-JzGtxcxkMSILabt57mJtkhgh2ua3Au4GzjPALNgzUayZOXSQmY_xaJtu_ueCaqxjYY2C098vxU1HOGgxI9_ivAZuQo2_TRhckfsWGjAVyupvKUuh30oxxHcNAEtCXJm2uU_9vXhyV3k_cUu2hu2DEN-GERnkAnMb4QrFP_wrwjuqp2gwoC0fUbuCvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ بعد بازی:
از دو تیم ممنونم، بازی زیبایی رو به نمایش گذاشتن و تبریک میگم به تیم اسپانیا.
همچنین ایران سلاح هسته‌ای نخواهد داشت
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68595" target="_blank">📅 02:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68594">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10cd1a4acc.mp4?token=rkq-AdB-A4NdIcneWfHtp5yXMdd6UhaIWFN79-I5KFjWS5nhfVxcCxT1J7NjN-Jr74TfiKLyG3CynbULb4Jt-YkNlrrzHwvyrOKW9shluidvcb2PQMiL6Iajmkjw4ge8T0h1nB_Mvcm87LnHhwPhZJb_hslF0rCW_WsZj4DNHH-W0OXkvk7oXx0EB8WFsE1zJstJJQ3Bylbfv-4ux9dfoPcA_HpERI6XUKuk0LSycRBWUkpQjutM0GwqAWbMpIx1bUxt9dncjKTJL1EioJqZ3CTnN-mvnCXWZlAExrEUoT2MSfibmfqZpX2a9Gr8ICxPXy9b2kL70trm185UjRWXSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10cd1a4acc.mp4?token=rkq-AdB-A4NdIcneWfHtp5yXMdd6UhaIWFN79-I5KFjWS5nhfVxcCxT1J7NjN-Jr74TfiKLyG3CynbULb4Jt-YkNlrrzHwvyrOKW9shluidvcb2PQMiL6Iajmkjw4ge8T0h1nB_Mvcm87LnHhwPhZJb_hslF0rCW_WsZj4DNHH-W0OXkvk7oXx0EB8WFsE1zJstJJQ3Bylbfv-4ux9dfoPcA_HpERI6XUKuk0LSycRBWUkpQjutM0GwqAWbMpIx1bUxt9dncjKTJL1EioJqZ3CTnN-mvnCXWZlAExrEUoT2MSfibmfqZpX2a9Gr8ICxPXy9b2kL70trm185UjRWXSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🏆
لحظه اهدا جام قهرمانی به تیم ملی اسپانیا توسط دونالد ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68594" target="_blank">📅 02:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68593">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5ecf5e7ca.mp4?token=HvdksuEXYfWpXELBVeQcnCX1PFzFyVb_ottnf_aA_6gwOjDVAgAI7LevXyLN739TsTC1HzmuqXvhJY-ttS7znI6xR6nMm-qpD7-D6TpnDAr_8zGUwd0IWzDdEJNyJsJTqWZI7LQzbuGKykAnSmDPqN9S3XLJaiPkO9HeGWAiazjNIvjm4Sqt47tE-RLCSJGYF3xyBapMJ2gdZkto49S9hTfGeT9DndydAmuRsmZLbKLhX5qyVOS2SzJD7BiGizkvnPuEWNT8KtjjBdMpiTL8WkON7fD9HqCbOqWnjpTs5MBKBf0njBp9SjY5Kz2xvzjSkMr81dj24pvL7Ol5_EF49w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5ecf5e7ca.mp4?token=HvdksuEXYfWpXELBVeQcnCX1PFzFyVb_ottnf_aA_6gwOjDVAgAI7LevXyLN739TsTC1HzmuqXvhJY-ttS7znI6xR6nMm-qpD7-D6TpnDAr_8zGUwd0IWzDdEJNyJsJTqWZI7LQzbuGKykAnSmDPqN9S3XLJaiPkO9HeGWAiazjNIvjm4Sqt47tE-RLCSJGYF3xyBapMJ2gdZkto49S9hTfGeT9DndydAmuRsmZLbKLhX5qyVOS2SzJD7BiGizkvnPuEWNT8KtjjBdMpiTL8WkON7fD9HqCbOqWnjpTs5MBKBf0njBp9SjY5Kz2xvzjSkMr81dj24pvL7Ol5_EF49w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
لحظاتی از اهدای مدال نقره به تیم ملی آرژانتین توسط دونالد ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68593" target="_blank">📅 02:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68592">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067eca16ef.mp4?token=M8oo20d8-Wbj2lVOuDtW-CEJzDAfVx5qkWyXDpe-zz_pTBMKbJg-Pje_VeQISh722QblUvDMGiRX7mShtbQGDAArUyVxmSrPcDAoNM36Vt4ZLoZnF4V1QKI3VgbVyHHWNKr1omMjPiPzkP4np7nuKZAxZS3A9jometHw9HHgxI7rBa4Bn80IJokp0uV6scagfXD8ypTpCjhla5NjI4GNscMx4WH7_T-Sf1NCF08Mvcciq6olMHxKbk60wrYvITKBpxHhfwNpODjczEseYaRbOCh4OeCnQ4DnKDDMF1Xu4Gh1PhQesWUQSDX6Gmjmsmsh97_bpM--B4cLd_jmKUpR6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067eca16ef.mp4?token=M8oo20d8-Wbj2lVOuDtW-CEJzDAfVx5qkWyXDpe-zz_pTBMKbJg-Pje_VeQISh722QblUvDMGiRX7mShtbQGDAArUyVxmSrPcDAoNM36Vt4ZLoZnF4V1QKI3VgbVyHHWNKr1omMjPiPzkP4np7nuKZAxZS3A9jometHw9HHgxI7rBa4Bn80IJokp0uV6scagfXD8ypTpCjhla5NjI4GNscMx4WH7_T-Sf1NCF08Mvcciq6olMHxKbk60wrYvITKBpxHhfwNpODjczEseYaRbOCh4OeCnQ4DnKDDMF1Xu4Gh1PhQesWUQSDX6Gmjmsmsh97_bpM--B4cLd_jmKUpR6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دونالد ترامپ به منظور اهدای جام قهرمانی به تیم ملی اسپانیا وارد زمین مسابقه شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68592" target="_blank">📅 02:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68591">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGcZ6Uc_p0OoJPwlYLkW04gta169qHkZGzKykpadfZ0AoivcdnKZOe3sJaQxDURm1-PxDA_j4gpW5hiMfmacR0uePRRHGYl1wYYr4k5WOqTLnY07m6MSQ87BkS3WCOsYtYyKdUXITRpxfhlX6ZMEoCzS05DA9bUi3ORdL1qZlOZLvGEUNfKCUu2480N_RqArcsCdq0TlFHQH-20U99ZkDOkOTQu8WFzPcS_nP3ywdMwmZn7jAHTx0eBZwOYI2IPJUAeark6_QOXfGF0-2q61msq3Zdi2wQvG_YT8opDD0NYKGmKIGSC55SP9dUx8uJfQ_zcic5qqbA8_7sJDZMVuPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
عرزشیا به زودی:
ژنرال فرنان تورِس، از جمهوری اسلامی اسپانیا، گلزن در مقابل آرژانتین
😟
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68591" target="_blank">📅 02:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68590">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEBQLjlKzHHN-_wcESVyBy1toY8G78ZBkaniRgQNW-wL4B1n3-wvIX4xQyDps6MrZZ5MWdHg5vppZrRb41Dkmk1HpFOOiQUmsB24STla-5qGRZ5ljrfCQYSdxwr8wqYbVAVuJXOYY5V5FpatsNgJMAKk-mdKjMZoQbRRwLQRUYA-I80y5qXrBFeuLYoiqZ7kO10LW_qG7ta5YuTxMv_Gj8xrSRlK6XEZ7dLAV-gBc8Q7PLQHC24SGEvBptzafaraYwXTQHik-xtQ1ZuQRAWwnpLiBgVku2trfl1aJJhzK1jRb1fU5oA-oa_cu4vE-6vvSV7rcuvQTFw8SQsKqLZurg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ اومد تو زمین
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68590" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68589">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">امشب سنتکام نمی‌زنه یعنی؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68589" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68588">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJhQydVgPjco6ZPQjgUPh6mszk7wni8oBX0QxIY216I6v0iOYKbt3h3jQs-BZXlzNqBTVD5c1ZYeKVResMGFbYGyX5GC0I5Yd5a157ZW4O5bS_f4fZTszb2_h-eOB3rKCo_Yaps6d9cpkZaK1SyjQzvnUb_w3hvn4HvSp0wz_YLVM-5-nzXMB1D-FDgiHIdcTNC7xw5m1jvSjJIZrwiFZdAs7hT1lcRJ5M-zzxXIRzchp9PDldUsLAA5QLrhuguEP33y4_ZuKHNP1buzkpiym7_B0BR-7m0ZpHBrCmiBVMThMWzS64ak9xdVI4yBhN8IUyt4F_I0OdJ-FJ5NKZ-iBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آقا تموم شد به راننده بگید حرکت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68588" target="_blank">📅 01:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68587">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6vF1U5Xwbv7CX1ovk80H9JhRzMLx5yW5dWOXnB0VJg1sn7BShnLp5jCdhozE0MzLJ4GOCtg-pU008W9pBSaU2vJcS2AZNEu2Ir8wbgjTPkK9k7aTGxRWuzvoH3lna-5AnRg6TLQ7TKpBgTfuovIKzqenBiykQqK-LaiI2HsvTNskfbIaJvuxfifJ5mm_-PSL-76AxB8BwCEePtoj-ine8YVDAPq6TPrK2lx76G7PuoJO1yyIqOsC0ymJg3E3vzEdxW1VaS_OnflzAYoBMkb6fD5omt4jP7cmwPQjPp3OfMOOfbx0ivaHb6--bhpEzG-lfepilIQL5HWurDkR6tXTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026 هم با همه خنده‌ها و گریه‌ها تموم شد؛
قهرمان: اسپانیا
🇪🇸
نایب قهرمان: آرژانتین
🇦🇷
مقام سومی: انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آقای گل: امباپه
🇫🇷
آقای پاس‌گل: اولیسه
🇫🇷
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68587" target="_blank">📅 01:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68586">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEYkn0vLuINnbj9b4x0UdQVMgspKLpo2dnTVQJQMjVrpjPLRYo1rXNKOT0pvuYAKO8vanlDrq6GLpw0ixHYtA2clZbbWWBmpZfRHwx9NgQ_fWW51EFZaVbHDn9i5TjjSAKYkrrBSs--KLmcclfToMJ243yXPnq6EcM60iVc12ORzSYZnEZnmRULt-tL7Jx0nLM_ZyB3aotZ07zLJVO0Sl5pnD5QQ6DjuIwwRy2EL0NU8qXjLftBsZreOQ7R40eg-7k5wNFyGCaX5rWgBgZ2cwp2vfOVcPMo8pOYxbFY9J7SuJMycl9Er1VsE5dtfTyadb5b7XT-WDVgGFBPUNr8YXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💢
🏆
تماااام؛اسپانیا قهرمان جام‌جهانی 2026شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68586" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68585">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اسپانیا خیلی بهتر بازی کرد انصافاً
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68585" target="_blank">📅 01:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68584">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇪🇸
گل اول اسپانیا به آرژانتین توسط تورس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68584" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68583">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
گل اول اسپانیا به آرژانتین
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68583" target="_blank">📅 01:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68582">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCHTFOGVtPuf7yUN33s0b2UQQwm-YcHPv9D5y3qpY0gCS1uYkpVqXztSSni5wffhXWenjm7Nj2nV8j40e-lRvH-1_g7W_u6LbidEPfQRaxqgENTBJM8L-DfU03QnPFJ8C4G0tuXyxZHB-VVXYIFKwsQTQlN1NUuG--RS9eDQE6GbYROABZa49KYa84PBKI387-DyG3A5vdVPu8bb-ibog_rCghc34HBqdBRmLmVyxQ1T71kaE6glaxN4m0_-T5J3lGy9FcWLMnrL4O6ARQSjT3vd5fPK5kxdnOmTy2AEk0FeTkOTBhvClGQSo6fJvPGhinyU8RCXFQGYKxplN--A0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پرچم شیروخورشید در ورزشگاه
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68582" target="_blank">📅 01:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68581">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بازی که رفت ۱۲۰ دقیقه، نیروهای سنتکام هم دارن فینال رو می‌بینن، حملات امشب، نیم ساعت تاخیر داره
😁
#hjAly‌</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68581" target="_blank">📅 00:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68580">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
آرژانتین ده نفره شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68580" target="_blank">📅 00:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68579">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
آژیر خطر در بحرین به صدا در آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68579" target="_blank">📅 00:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68577">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a67fe75354.mov?token=eejnZ6MykPj56zYcdZTXiJP-82Ya9qpqRxQpLT1uyEtghbrzzOC39kNYIYyjVjNDC7csulCcPqstJcDShHrNZwfzItd8eiKGeAG5CkPsNhpKB9enR1zb8h08E2bRrVM-tMcG6jLi4HaMxUImD8gUw-9l1nqJ8B8UcGzwmDFj_X1ECyjtm6U2CNUUAtB9TOvWnEC6Jw3SOdX2Z6qLRv8AgtRl5V13iG30JMMj4TLHjXiNmNoQMnVHEztNvQL2rLn2WNDn1LLYZQZCojWTDr661crfdfh-x_ax72C-2S_mFxJe1-1NR5eecFelN-RVJrQ2yPLYxeGK8z4S4NBFkQBYng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a67fe75354.mov?token=eejnZ6MykPj56zYcdZTXiJP-82Ya9qpqRxQpLT1uyEtghbrzzOC39kNYIYyjVjNDC7csulCcPqstJcDShHrNZwfzItd8eiKGeAG5CkPsNhpKB9enR1zb8h08E2bRrVM-tMcG6jLi4HaMxUImD8gUw-9l1nqJ8B8UcGzwmDFj_X1ECyjtm6U2CNUUAtB9TOvWnEC6Jw3SOdX2Z6qLRv8AgtRl5V13iG30JMMj4TLHjXiNmNoQMnVHEztNvQL2rLn2WNDn1LLYZQZCojWTDr661crfdfh-x_ax72C-2S_mFxJe1-1NR5eecFelN-RVJrQ2yPLYxeGK8z4S4NBFkQBYng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گویا از قم موشک‌ پرتاب کردن
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68577" target="_blank">📅 00:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68576">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4FmjxBqlsoivPt4t3dETQZu_HjAFMdH5M4lIeo4cuRjb4zUOSsbUtSLoGCKlJm3fA_C3MUTLzCMZAqCnwu7ryMmMa6w0CgdauBEMMfF1R90kmexbF_82IX6GkorFvtcHBJLNM2BpJO70_msIgv5RIOBXR9h7GmCA9Gia1QRXi0PIHqUo6HWGxVY_d-wa4wrsUHY4ChT_YvebIYmBAWH9i7El8fuAX-DoJsFs7-kB7NhfnJgnZ2u3rgOBUNHLWznF2IpHr75HQazsNol6G5NC1a_4ljE-_IC3hYtBPwWNPo4YBYFSJInD8Rb_HbI-fOxZE-vKKoXeBsHK24AurVgzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو بیژن تو فینال
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68576" target="_blank">📅 00:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68574">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🏆
اجرای کامل شکیرا در بین‌ دو‌ نیمه
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68574" target="_blank">📅 00:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68573">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🏆
🔞
🇱🇧
حضور میاخلیفه، پورن استار اهل کشور لبنان در آمریکا برای تماشای فینال  @HutNewsPlus</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68573" target="_blank">📅 00:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68572">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در ساوه  @News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68572" target="_blank">📅 00:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68571">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در ساوه
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68571" target="_blank">📅 00:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68570">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416fb2b432.mp4?token=nKZXKT2guFDUTdkXew-rACfbW8agyVIDniQZl7QZLE-sjqaw6-nsSWy8aemyco9pCj-BX7VQkofzB1OBYnOqZ09Idw3ARc3y48p9bWNQhLR6IxzPCXucsdGPDPAxTQ3S8l7umaK6YATTLM8RPjspBEgV3D2RePD5JeSZfXrnikaVSDFWSCRtUIsUW5QrwbgKor2fF2Bt45tuGgHre5BP0tWjzD2wtx7VsaCsOanhR4LWsEyc6ims-u9lr_587ntze-yUXZlxTeeATumi6EN3ROVbHuN2T19patb8ATTolZZ0FvDhE9QiXkl6N9ztoNQ7otMex-BoKvBcZ_x2msqYnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416fb2b432.mp4?token=nKZXKT2guFDUTdkXew-rACfbW8agyVIDniQZl7QZLE-sjqaw6-nsSWy8aemyco9pCj-BX7VQkofzB1OBYnOqZ09Idw3ARc3y48p9bWNQhLR6IxzPCXucsdGPDPAxTQ3S8l7umaK6YATTLM8RPjspBEgV3D2RePD5JeSZfXrnikaVSDFWSCRtUIsUW5QrwbgKor2fF2Bt45tuGgHre5BP0tWjzD2wtx7VsaCsOanhR4LWsEyc6ims-u9lr_587ntze-yUXZlxTeeATumi6EN3ROVbHuN2T19patb8ATTolZZ0FvDhE9QiXkl6N9ztoNQ7otMex-BoKvBcZ_x2msqYnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
اجرای عمو بیژن
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68570" target="_blank">📅 23:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68569">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVky4BVL4TTPTHWkzhTAC8OT9AWhG02jMi9yHHv-mdxCRhKnBKUJjXQqYURaSfrPOsTyRXcKSYfScXUZGjfsW9O2zrWo0nwCqNO3duVD7LEtYRh9UoAbCOtNZelzH3nutGvmpg8p4MCMzvpqGmvp9ADhEtvy0rsUOcTo2RTF-GTkaBBU5knQF2V-EUQhxVfplMNKzn0DbJc10RFO5VF2mPQqU7CAP2A4S_saoXgolt2zL-Dyx5qzO6doeyCH-k3e9Xrk822PO9MDfm1LsHo9NTNnt_9jEkiR_VS5Si0YXhDlZG3HqzTbCj2ms2K3FR3YKjYG55LCZxUocxssd7CU0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه آرژانتینا دارن کامل لخت می‌شن
🔥
👀
🔥
🔗
مشاهده ویدیوی لو رفته از دختر آرژانتینی
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68569" target="_blank">📅 23:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68567">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vivd7yKuZyyVi2HXrtrYbp1unJQ7KxAWuy-7NbQUsJbCnDa-XrMbW3ZWyTBy1XaKPor9xOMmAo3QYXvhUN2mQJ64B9s_K2LlAqqzky3J0vpXOLztGAFJuxr8uo_jHyr5nANRVhYsR1b469rOLYSOjL_rZAaE9BecJGTLsmDCBXIECkR9R9jkCTqtsBWJ4cggNL37BQMCt2BzFfjdbQAc7H9G2oLTwvB2cpy_mFtY4CImgrNLW3boRGX-YVj6Ti7u0H2fk_wd4tBkLRlHYYGjqTQFb4I6dGZZQQ62sBI5y0RfD5YgugS1ijirz-SqR6O-caoHDiFumXsbSb-GnnxGaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:یک نظامی آمریکایی در شمال عراق در تاریخ ۱۸ ژوئیه و حین عملیات انهدام کنترل‌شدۀ مهمات عمل‌نکرده‌ی به‌جامانده از یک پهپاد تهاجمی یک‌طرفه (انتحاری) ایرانی، جان خود را از دست داد.
روز گذشته، فرماندهی مرکزی ایالات متحده (سنتکام) خبر جان‌باختن دو نظامی آمریکایی و مفقود شدن یک نظامی دیگر در اردن را، در پی حمله ایران در تاریخ ۱۷ ژوئیه، اعلام کرد.
پس از یک عملیات جستجوی دقیق، نیروهای نظامی آمریکا امروز بقایای جسدی را که هویت آن هنوز مشخص نشده است، در محل حادثه پیدا کردند.
فرآیند بررسی برای شناسایی و تأیید هویت این بقایا در جریان است.
در رویدادی جداگانه، یک نظامی آمریکایی در شمال عراق در تاریخ ۱۸ ژوئیه و حین عملیات انهدام کنترل‌شدۀ مهمات عمل‌نکرده‌ی به‌جامانده از یک پهپاد تهاجمی یک‌طرفه (انتحاری) ایرانی، جان خود را از دست داد.
نظامی دیگری نیز در این حادثه مجروح شد و همچنان برای درمان جراحتی سطحی تحت مراقبت‌های پزشکی قرار دارد.
سنتکام به احترام خانواده‌های این افراد و تا زمان تکمیل مراحل اطلاع‌رسانی به آن‌ها، از انتشار جزئیات بیشتر، از جمله هویت نظامیان مفقود و جان‌باخته، خودداری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68567" target="_blank">📅 23:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68566">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mesHTnfnGIrLDyqiNjRzRqVzg0TrKdXPj-jqi_X3I2k7rwwIIxtPDKf48dseJEDGsv2KENA2OKBhPBMaVRalJNdwd2Oi-95-Jocw8LgFHg1xk-LT7N_wrbRWMeNNZLWV6dU4LAsiGc3wcYaTqFz2UoYLgVlJRviOVcCycEpdKM0t_i7lewQJhlnprt6LhKTkr3sAqzMGsDChF0inxZw2dti4MOd9sGIsZX4j9OpRGfv-pp3c7g14MttBJBchmD8vvfBM64nl5mCk7Jda7b-zl-4qkXG1MTd-uuxuoj_cq144HSy2anmWlywDSEBr8lIlBW8MoM5aPM7c6W_mKW0YKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا کاری به کریس‌فن‌ها ندارم ولی هرچی چپول، عرزشی و فلسطینی‌فن توی دنیا هست امشب طرفدار اسپانیاست، به امید باخت این تیم کثیف و سراسر چرک #hjAly‌</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68566" target="_blank">📅 23:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68565">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3cfd8ff5.mp4?token=o19Y8sVMUqBFdeSFpUUCu3ZgfrSXifZnKrda5W1vSS1XYpLo_3tBao1SLudvYv2YawXzwzF2pWPIYprH2Oipaxt7apkCMEFp7h0kazg6PGtFlmcVoPBOENkCpwOh2BgcsAqVc7ZTwHI0wAcLoA_77aCYxPTRz2pFlcLHQodK4HD0wIxWkt0y7oY6Uo1X6g6zt0A7qmTyTV-kpWigcFKs6NPj_6CbO4jRJpio5qKjqm9CemCFKtUyu_jobW0TrBpfWjcosRArdrpRCKJoaYwznaA5vSDa_rFiLCoCVHevJFIa7CRoThFrJivaSASX1xXoA2ySDYAtN9WeQwIkO8DbQ1D8Rsov69tazbmFmZRx-1H1rkw9ilXK45FtNTI_CeAjD_tBRqKU1_6nfB563ECWDWMCn1YhhAkGO5XE-dB-mTY4X4J28RenmVI1mKG1E75WQSuFHDiyjk2RrcYi05EGYXFmWxoM0NHxnPRe_GQWSX_TsRJsykKgJfwQ52h9AB3I8NcVZ3Cxpyx0wuh2D8xG_cUZ7JLtNsfYbSCeA9p2vxA2NYX_MOCt7sJmIHqephQbzZjx8_cDI9MTDhcOFKkpt0pFhhZUfy6o0-AloHeTKOyvyrCklJh6UKiEkIq-BLacR6OgzNM1vxqeLjxAuve37sA09zQRP9wjPle-3kMsp1k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3cfd8ff5.mp4?token=o19Y8sVMUqBFdeSFpUUCu3ZgfrSXifZnKrda5W1vSS1XYpLo_3tBao1SLudvYv2YawXzwzF2pWPIYprH2Oipaxt7apkCMEFp7h0kazg6PGtFlmcVoPBOENkCpwOh2BgcsAqVc7ZTwHI0wAcLoA_77aCYxPTRz2pFlcLHQodK4HD0wIxWkt0y7oY6Uo1X6g6zt0A7qmTyTV-kpWigcFKs6NPj_6CbO4jRJpio5qKjqm9CemCFKtUyu_jobW0TrBpfWjcosRArdrpRCKJoaYwznaA5vSDa_rFiLCoCVHevJFIa7CRoThFrJivaSASX1xXoA2ySDYAtN9WeQwIkO8DbQ1D8Rsov69tazbmFmZRx-1H1rkw9ilXK45FtNTI_CeAjD_tBRqKU1_6nfB563ECWDWMCn1YhhAkGO5XE-dB-mTY4X4J28RenmVI1mKG1E75WQSuFHDiyjk2RrcYi05EGYXFmWxoM0NHxnPRe_GQWSX_TsRJsykKgJfwQ52h9AB3I8NcVZ3Cxpyx0wuh2D8xG_cUZ7JLtNsfYbSCeA9p2vxA2NYX_MOCt7sJmIHqephQbzZjx8_cDI9MTDhcOFKkpt0pFhhZUfy6o0-AloHeTKOyvyrCklJh6UKiEkIq-BLacR6OgzNM1vxqeLjxAuve37sA09zQRP9wjPle-3kMsp1k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇺🇸
پرزیدنت ترامپ و بانوی اول ایوانکا ترامپ در کنار اینفانتینو در بخش وی آی پی استادیوم
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68565" target="_blank">📅 23:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68564">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UixOmYXuZkE_pjQ7zvQy4wHESAQK-2W6Lmn3c9mWd-ttkM8JibGuMn7S9jTEF4i0eZClM3oISQfDOIUoCTLuKNDLbqtMSMHx5r2vB9D6Fkj1HXDLahwSbRGkNBxM_umXnbQR7RWtI5AipN_2jiVgSXGp3r3gl3UVU_1y1lO7xtY0CwmB_ET-UIKOhyK70NSpuI5mIQ0M6kTaCkV6Um7O2kcPdCp6iEKrvrEmijYUGh-ZeCGIdLkRWhm7dMHPyTOTQEHxe2UArwAu0bR6GtnMzamzK0mr-u9HCOTvCDpXKGOQcqDIe7Ou4a2gMveklIAccWxbjVZ4qmBDW9ak3p347g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
گزارشگر صداوسیما : هیچ تصویری از ترامپ کودک‌کش و جنایتکار نشون نمی‌دیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68564" target="_blank">📅 23:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68563">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حالا کاری به کریس‌فن‌ها ندارم ولی هرچی چپول، عرزشی و فلسطینی‌فن توی دنیا هست امشب طرفدار اسپانیاست، به امید باخت این تیم کثیف و سراسر چرک
#hjAly‌</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68563" target="_blank">📅 22:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68562">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiQ852xfIE5ifhLaDWS6iNNBetXTQs54JdFKqwyZUoKk2INIiqUFCgcnfgvJwi4VBlf37ugqCQAZnQbyUBCkKwcnBNwLGbtmgt9Z9ZatEANsV9yhvqHV_FxvPWjHJYQsZoxCxSUHLpskO_hWL3L89f0MAuI4YSh8aMSIca7U9S05Mym-4MfFs_h6blSPWSyZBj1kcczMo8am9H94qUfUVf4FcMaq4XbFthjh9tfESM5kUDmW7TNYcmZ32Mp5rWHIhjhTK_4mhnAcnnl2bglPsqCLOCRHlZ4GcKNd9FKeDSphM2ZIVDoQ2c0WlxTi_8q94LKW6LU2-kRDE8bOojkF1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
هم‌اکنون ترامپ پشت شیشه ضدگلوله
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68562" target="_blank">📅 22:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68561">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGp3lP7IakpPuQ4kVFjJFm_Sn3kU4W3gtUqhcJ6SqwO7_JwDHpUI_2OJkFuCmHzljjBf_Gi3GichvQmyXY48D7F_WUe0BpWmttBjXXLJh8ss1ikqgke6ft2KW7R8Mt8ASf5mkabYB416WDmUswJTktibKEf3ZtZabbGASRr1KJtThuVJfu7ZXP6uiO-ukbMcM0Cs4kWgn7MCmMtbDnC2qQfiOst6sYDlaQsYjOpXJjmu147Gx7KY5AVIUkLhvscJtAacMj9jRNjvwMOtb7TDfUS_63HpysYdIU8X1xLUcjQzckTxNRXAftfzLfyxRgNfP3hqr-SJE9gaWdUmdtiF3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فینال جام جهانی هم شروع شد
سپی
یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… همرو
بدون سانسور و رایگان
میزاره
گفتم اینجا هم معرفی کنم شاید به دردتون بخوره.
هرکی خواست بازی رو با پوشش کامل‌تر دنبال کنه یه سر به چسفیل
بزنه
👇
لینک پخش بازی:
https://chosefil.com/fa/programs/318
ایدی کانال تلگرامش:
@officialchosefil</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68561" target="_blank">📅 22:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68560">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c88de66012.mp4?token=bu2I00HDfs65-RBGFcSRH3o3qc3-99a4Thc4Jc-v2iu3M6TzBDtm0VjI2UuSEpACFpuIBI38_LczkdCIPSL06l7vm1MLJpLGK52RiuCD-qv6u_A7RwlmyjDhEi7NLC-kgl8zIhdcrauYWzpECq3cu32d5FB5yBPsMxEM8uT0jO8nX5U53Tr59FQxAdrsX28UQp_rmp09nPn2K_AVvX37nlwvbrFW9GrqcU5Hso4sfomJLmSOFB9qF2LdigOQy_lS_AtIWas4w3pQ43NwZhI658CBzw-jknrZyeppQ1trGnPqp0zkJ6illImvvmN1duQVK2nHGje0cAc5PZ2xnIkr1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c88de66012.mp4?token=bu2I00HDfs65-RBGFcSRH3o3qc3-99a4Thc4Jc-v2iu3M6TzBDtm0VjI2UuSEpACFpuIBI38_LczkdCIPSL06l7vm1MLJpLGK52RiuCD-qv6u_A7RwlmyjDhEi7NLC-kgl8zIhdcrauYWzpECq3cu32d5FB5yBPsMxEM8uT0jO8nX5U53Tr59FQxAdrsX28UQp_rmp09nPn2K_AVvX37nlwvbrFW9GrqcU5Hso4sfomJLmSOFB9qF2LdigOQy_lS_AtIWas4w3pQ43NwZhI658CBzw-jknrZyeppQ1trGnPqp0zkJ6illImvvmN1duQVK2nHGje0cAc5PZ2xnIkr1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری حکومتی:مشهد در18و19دی پنج ساعت سقوط کرده بود.
عراقچی: اصلا انتظار اعتراضات ۱۸ و ۱۹ دی رو نداشتیم، جمعیت خیلی بیشتر از چیزی بود که فکر میکردیم
.
مجری: ترامپ درست می‌گفت، من رفتم آمارش رو درآوردم، مشهد در عرض چند ساعت سقوط کرده بود!
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68560" target="_blank">📅 22:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68559">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c26a9bf5f.mp4?token=SRskQQIKLc77Urq3Lt3YD-9ruqItr07f52Rc3Y2L97rVx-GqpF5PXgL3d1YzQSzckxiiAMNDKBSxL9PZl8FxVqCkxzWxog7Z8dd1YyYCDEhkocYQ4TDLyuGopExaTVuLmhSU5i7sjXK_v8l5W1Tr4Sb5W1L4a28RS6IsSXJ62hiBIX_iQBYzqtEZgQGWJNu8WvLo2mqCuE9wjIipw-LAErVBM-WQlbqh-WuNJorho3-02k21ytmmiLKv2UbYPsfFgygpcKKeJnKIRqZiYkgOxWxZT8VlJn-uv5X2V_CCj2IXvlS9cIniqmLlh-IUa7tZF0yldfVopRiN0Eo6d5M8wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c26a9bf5f.mp4?token=SRskQQIKLc77Urq3Lt3YD-9ruqItr07f52Rc3Y2L97rVx-GqpF5PXgL3d1YzQSzckxiiAMNDKBSxL9PZl8FxVqCkxzWxog7Z8dd1YyYCDEhkocYQ4TDLyuGopExaTVuLmhSU5i7sjXK_v8l5W1Tr4Sb5W1L4a28RS6IsSXJ62hiBIX_iQBYzqtEZgQGWJNu8WvLo2mqCuE9wjIipw-LAErVBM-WQlbqh-WuNJorho3-02k21ytmmiLKv2UbYPsfFgygpcKKeJnKIRqZiYkgOxWxZT8VlJn-uv5X2V_CCj2IXvlS9cIniqmLlh-IUa7tZF0yldfVopRiN0Eo6d5M8wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پخش تلویزیونی اسرائیل؛مقامات امنیتی اسرائیل و ایالات متحده:
ایالات متحده در حال آماده‌سازی برای تشدید حملات خود به ایران است.
این هفته، خاورمیانه شاهد تعداد بی‌سابقه‌ای از هواپیماهای تانکر سوخت‌رسان خواهد بود، که این تعداد حتی در مقایسه با آمار ثبت‌شده در جنگ اخیر، غیرمعمول است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68559" target="_blank">📅 21:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68558">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
کانال ۱۳ اسرائیل :
دونالد ترامپ، رئیس‌جمهور ایالات متحده، پیامی به کشورهای حاشیه خلیج فارس ارسال کرده است که در آن تأکید شده است: اگر این هفته آتش‌بس برقرار نشود، این کشورها باید خود را برای تشدید تنش‌ها آماده کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68558" target="_blank">📅 21:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68557">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
استانداری خوزستان:
دقایقی پیش یکی از مناطق خارج از محدوده  شهر و حاشیه‌ شهرستان آبادان توسط دشمن آمریکایی مورد حمله موشکی قرار گرفت. این حمله تلفات جانی در پی نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68557" target="_blank">📅 21:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68556">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مسی و نتانیاهو
🇮🇱
یا یامال و فلسطین
🇵🇸
؟!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68556" target="_blank">📅 21:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68554">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W9gLrVoz86C-uaTS-uaxZBjK5QrarRNNKZTPTf7Fyy-Pspqu9vlT-M29XYpHTuvw6od1uOXsuj3Yj35nTcJx9Q38SmLd9H5kOjuXoPr9lw0-yoWuR_xyEVZepkimY5a1JORieViMnS7yD0VI9FCWzXhqGemkw2VZzU2UAlbHClVSnwwHVIbfDfnMLXxlx7WVnk9T0UeFb6Va7-uRruoUVZdmefJE4n4_ApF5Uf0rC52Dwtzfuklvzg09PtG9Suu9P95wPJOOSp8tZdM_YrVg0-TX2IQns9iHqz9kFQNNymiGdtBqu4j5pN2T9o33xKjgRJC4A_sITxXVx91uCLKrIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBQJ3ezz175PRSPHS3VLTzd-Xu852mKbMuWW6WFJerej0eeUuCdxbQO0NKFoZXQMRDfw_f4tjzRo3d2sRuUjuxmQlNC_qorNCkKtsLdPZFF1vbsrN6YmE_1ny41TxDQQwxjtxVFK4KSbaAv0-7fxeozPJ1nLMaoNJmF82DBGESdfSIB0DRWa7ZxX3lhYnE7RczxdID2DhNp_Tiapurx96Usmfz0YxyQfvIgoYyA46OOtOEGX_pmmVZANKJqPW_yUrnZbqgsl4YEBDma3qzj-IeurPS9uLO_HoYGnPjJRq1dvus1IMdGZZVEqCrEJLdJ2UbLXIEcm3XRBg1VAZ1n4vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💢
🏆
فینال جام جهانی 2026؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68554" target="_blank">📅 20:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68553">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
یک پیشنهاد جدید آتش‌بس ده روزه از سوی قطر ارائه شده:
• ایالات متحده حملات را متوقف خواهد کرد.
• ایران دو مسیر دریایی در تنگه هرمز را به مدت 10 روز باز خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68553" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68552">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e08df79c06.mp4?token=tid_C5qBtk7Ltl83AhZ6mvh6bjK_sbfyFPjluDhYzfiOg7M7uwfI3gEmn-kY1USXFEMCZdR7gdTpHFzi0EbK80C5Ya6Wpklbqcg72uHJAVKJ7zPDJuVZrjcX33KWPIW_SVNRi0FieVKipvNxSmopEPbZn4kW7vGZ4Ev9TifXSNQHbcfjvmmiz2tAFi7S6R1SZ87k6ont_2hFZ0HE41Zoxy7L7OsIGe-fJaBEoFlGoT3LeYUXMsSNzXOpG-cKPI3wK-7lEXruFltd3R7gZlsUKrGoZ-0ZjPz5WNbf89Fd-5Oga62syfNim7vYpeXmT9QNAOQtSrn_Moy_hTtG9e3qSA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e08df79c06.mp4?token=tid_C5qBtk7Ltl83AhZ6mvh6bjK_sbfyFPjluDhYzfiOg7M7uwfI3gEmn-kY1USXFEMCZdR7gdTpHFzi0EbK80C5Ya6Wpklbqcg72uHJAVKJ7zPDJuVZrjcX33KWPIW_SVNRi0FieVKipvNxSmopEPbZn4kW7vGZ4Ev9TifXSNQHbcfjvmmiz2tAFi7S6R1SZ87k6ont_2hFZ0HE41Zoxy7L7OsIGe-fJaBEoFlGoT3LeYUXMsSNzXOpG-cKPI3wK-7lEXruFltd3R7gZlsUKrGoZ-0ZjPz5WNbf89Fd-5Oga62syfNim7vYpeXmT9QNAOQtSrn_Moy_hTtG9e3qSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
رئیس هلال احمر:
در تشییع میلیونی نه تنها یک فوتی هم نداشتیم بلکه شاهد چندین تولد نوزاد نیز بودیم
👅
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68552" target="_blank">📅 20:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68551">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7091c7c4c.mp4?token=lQz6U_l9Q29ni6wYNEkDhdYnN_VV-xtYag-cyhwxD_SRJH9OlOlCEXz5IO0728g0N2S7_sMmRviidl96DJcUAsKPJuscmGgiF2y5j7e-OOKuuIw_A2KPI-vcIzBR0jYqukLfRdR6Es9SPCmDsNvWNNPBJjvGRjPAzRMgLwGDO0oPd_pYgVPJn47DNfj63E6NWPcjqxDilE04m-qfILBx4ptjFGqfWjzFVduslbA3qsOniMoT54JRnm8hgym2R1qGcIWess_5MZPROBQoRvobbDDWG-ouScY-ob4k1jcpk92C9AKDckVLvdwTvl_kTH8kzKHedQDbpwFoT5KJnIjdYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7091c7c4c.mp4?token=lQz6U_l9Q29ni6wYNEkDhdYnN_VV-xtYag-cyhwxD_SRJH9OlOlCEXz5IO0728g0N2S7_sMmRviidl96DJcUAsKPJuscmGgiF2y5j7e-OOKuuIw_A2KPI-vcIzBR0jYqukLfRdR6Es9SPCmDsNvWNNPBJjvGRjPAzRMgLwGDO0oPd_pYgVPJn47DNfj63E6NWPcjqxDilE04m-qfILBx4ptjFGqfWjzFVduslbA3qsOniMoT54JRnm8hgym2R1qGcIWess_5MZPROBQoRvobbDDWG-ouScY-ob4k1jcpk92C9AKDckVLvdwTvl_kTH8kzKHedQDbpwFoT5KJnIjdYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو :
آرژانتین امشب قهرمان جام‌جهانی میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68551" target="_blank">📅 19:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68550">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpO4hCdkJ1V6PlF4JFNE8Qmz-l8F2gtnDKX9A7wugScY8bDzZcNb4-o05o5yIcOwYQMKmmhYGPDt-7qK58lgpt7ENWLOcT5iLIe_p8zJM8wVFyEnVsIwMfIhnh5FH_Uu8g9FWvJpPMzFDuHL5jxDzefRUecezLS8neVYwiMh3eVJ17a0RFkwTgMzlrjUlTWBOkYIRYepum58OBIrP-p8Vek2z7L2q4NuQIxrEVUxQ_XB9I5hP6fKqbAQBubMPzCCl9jurdQAzijzj3Nmns5GcPhORO7EWvbFje_2XzIBjCr_SzOXGUAf8Mt4k0FUz5Yr8xB3KBx377H8cqtdGtR1XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه امشب نیروگاهی در ایران هدف قرار بگیره، مقصر اون فرماندهای زن‌جنده‌ی سپاهن که امروز برق کویت رو زدن. #hjAly‌</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68550" target="_blank">📅 19:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68549">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
رسانه های عبری:
برآورد‌های امنیتی اسرائیل حاکی است که رهبری ایران دستور حمله به اسرائیل را صادر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68549" target="_blank">📅 19:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68548">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
هدف قرار‌گرفتن یک نیروگاه برق در کویت  @News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68548" target="_blank">📅 19:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68547">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNPvkBISOdp2nauqNnPyEdY8L7doh8mQOdG3oRD2AOcVCC6Alj7kZZVV_wwivttUTkdP8TcCUgTeLZ_XAG6XJMy6qBamoPDyGommy4ZMHdc98200eohR7eBMXLLqZphefGV-a3aR1G1G0_ZNfEHVv5lEUSxOqw_CiqZJwryd4v9Gu0WHJDa3ml5XqK0WkUMNjzHTNsejic4gAqbL62XmlFEqaVwaDHRhpVbb8jKg2fiab5AVsxGbJdqKtB_qGQL2M0eKbXgFifvMHO1zJSJxbfFAuJvFMik5WUvIF_YWTyx0lbbU2mYoRwZOs0KAEXAF2fWq-2mGqBj5I_9jXD7R1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فینال جام‌جهانی ۲۰۲۶ فوتبال
🇦🇷
آرژانتین
🆚
اسپانیا
🇪🇸
امشب ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68547" target="_blank">📅 19:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68546">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/798b52eeca.mp4?token=jWAcWAsbdT487zHG9GV62SDu7TdlSjKvO_W4KP_8wE3u_ffag_2b7yi1XsEYtj6a6EymrrmAm5KSo2dp4gWPm2XplbaEku0nWewgQvx7KfSFQvCFssLy-xGMib_ir5OBytJ5x8Nd6xfdYYdRI5zlQ6qGyMJGpM9w8FPaOSNENdcYz37LISnoonM34KIvBag1dc47TBUkOQwIipSgaF0cxGdz9tdYOBY5FonUANr8CpyLPgt5iII7LHQfubeTeH0cKExse0MOB3L7yX29V0pVokKo4tCOt6AlDqqgayHmOxiMB5alGi0fpWhHLEizl1i_RS0-ILM_BLH15oT_0J8yLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/798b52eeca.mp4?token=jWAcWAsbdT487zHG9GV62SDu7TdlSjKvO_W4KP_8wE3u_ffag_2b7yi1XsEYtj6a6EymrrmAm5KSo2dp4gWPm2XplbaEku0nWewgQvx7KfSFQvCFssLy-xGMib_ir5OBytJ5x8Nd6xfdYYdRI5zlQ6qGyMJGpM9w8FPaOSNENdcYz37LISnoonM34KIvBag1dc47TBUkOQwIipSgaF0cxGdz9tdYOBY5FonUANr8CpyLPgt5iII7LHQfubeTeH0cKExse0MOB3L7yX29V0pVokKo4tCOt6AlDqqgayHmOxiMB5alGi0fpWhHLEizl1i_RS0-ILM_BLH15oT_0J8yLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هدف قرار‌گرفتن یک نیروگاه برق در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68546" target="_blank">📅 18:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68545">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر دفاع اسرائیل:
«ما اعلام کرده‌ایم که اگر ایران جرات کند به اسرائیل حمله موشکی کند، ما با یک حمله قدرتمند، بدون هیچ قید و شرطی، پاسخ خواهیم داد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68545" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68544">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
جمعه و دوشنبه‌ها، شانس بردتان را دو برابر کنید
100% بانس میکس ورزشی تا سقف 30 میلیون ریال
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68544" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68543">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_vfWU5iSSvsBIsG4nd6D5QKkR_iNAatNhAWXe9ms54y0bnQQgcxvIo5hCDF0B3o2WuPsonPlB9CEh_NQbcABmBNyJy_35QVKVlKpRIBlevoI-xSWgdtazaN0Wpdaf_K3lsDKjfXUwmrPBjQR6EV0UUF7grZ0VxdRmD_HYHR3LPwzHYNo_k5IDxG5EIX3ekvgzGoxieWyUDtjZFGchVDSPI90MCgM0H0HFsxDuGgOXaL8d_0GZm4SIxaY9irwLHWNK4XAmMla4l9CTjG-cCS7Ng5CLpYB-riJ_xv_fBruwDEFc2DauOmxzjWBbdPwdizdEI2pQ4vsz-eEM3u1M65NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال جام‌ جهانی 2026
⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
⏰
شروع بازی ساعت 22:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68543" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68542">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6b1462.mp4?token=INrwZAcNhY5yjNMC8km7Y1-Q_VHE8k9lQKBCdwOLnNSJ_dkIkWXiHCvikxtp2z9YyZY0k6Ft3CmCesOOvbOjgw2HCNjlnZcTyFIP6y5lY8b7zPlXevL3d0mkG1nuoHqgKbqsngjVsHfSxosYE3qk7pRJ_zKvgeObPJrean4T_nzLr4HrZatL9aDfuIyYKnt8PbmsJMbc9jzj0Pqe41-lRPDS39WTRXW3DU5FNKKQF-uWlIJG_TX8x3TJDqLxPpDscsMtBE2HXrnGqHJRJWIc910ae34RkTR3UKnm6RMzjLqYDLUm5ASonn6ajwciddFlZeu_QpGrskIuRqu5NwrWCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6b1462.mp4?token=INrwZAcNhY5yjNMC8km7Y1-Q_VHE8k9lQKBCdwOLnNSJ_dkIkWXiHCvikxtp2z9YyZY0k6Ft3CmCesOOvbOjgw2HCNjlnZcTyFIP6y5lY8b7zPlXevL3d0mkG1nuoHqgKbqsngjVsHfSxosYE3qk7pRJ_zKvgeObPJrean4T_nzLr4HrZatL9aDfuIyYKnt8PbmsJMbc9jzj0Pqe41-lRPDS39WTRXW3DU5FNKKQF-uWlIJG_TX8x3TJDqLxPpDscsMtBE2HXrnGqHJRJWIc910ae34RkTR3UKnm6RMzjLqYDLUm5ASonn6ajwciddFlZeu_QpGrskIuRqu5NwrWCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در دزفول
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68542" target="_blank">📅 18:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68541">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c53fd88605.mp4?token=kNaQOuIMMHU_p0Cp0UqCEZBu-klWav7brbDUMxFxb7WwP0aHzSj291ECMqI3IjM2JpbgVJ_HhKsgkppsZuM35Z-Wb9znCiacA7T8foxKx0jqG1RL7Qct24GnkDMlmnFB8Cg9iWHyudrhdVwxByFFah8LfSBEfYFOW71U1E97l22Bxp2p5faOGgAgHCpkfOCbvXnaANkazXM0gyeGJ7RWQLu0Lbot1fQgG1KNb3bC8Fva3DSQi2Uq_oRu7J_de7PWqpJ1zwQXv37ZYz6H4qwn4dCWYdrRq83KWUD8bH-9Z4bqePCm6MW7GiPUZmZXGJaL9oe7V0Deg5HYWeMLS_5xNTlm5T2_hQSPzCwK5vmOrVP14eYhAZCartKKudWtK5dhmcJfj0aPFbxAnb23id6df8K9QCeAr70Q8rxzcYVPXjuUp5RwsrjILXI-9bN-7soZtUqAsOrvsaslGnyQkTuBW31-uFJQsjHnl2OXC8lzym9GYji6hPee9BSjaUgFDJtO6Q3N9VHbbRPFzvQXL0CtSM64jmGIyOLLsq6lJrPIF56qTbtDk1-57cmTvTkIao17k_Ej4XnGcindhOBN3dlV0VFjBspQP7AJVTiZ47QKSW8mJPfPQKTz_GYf9vJ4s-Cqk-T-xHIVGubqh2ABKxuoABHEVikZml-VgNe1V80ObD4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c53fd88605.mp4?token=kNaQOuIMMHU_p0Cp0UqCEZBu-klWav7brbDUMxFxb7WwP0aHzSj291ECMqI3IjM2JpbgVJ_HhKsgkppsZuM35Z-Wb9znCiacA7T8foxKx0jqG1RL7Qct24GnkDMlmnFB8Cg9iWHyudrhdVwxByFFah8LfSBEfYFOW71U1E97l22Bxp2p5faOGgAgHCpkfOCbvXnaANkazXM0gyeGJ7RWQLu0Lbot1fQgG1KNb3bC8Fva3DSQi2Uq_oRu7J_de7PWqpJ1zwQXv37ZYz6H4qwn4dCWYdrRq83KWUD8bH-9Z4bqePCm6MW7GiPUZmZXGJaL9oe7V0Deg5HYWeMLS_5xNTlm5T2_hQSPzCwK5vmOrVP14eYhAZCartKKudWtK5dhmcJfj0aPFbxAnb23id6df8K9QCeAr70Q8rxzcYVPXjuUp5RwsrjILXI-9bN-7soZtUqAsOrvsaslGnyQkTuBW31-uFJQsjHnl2OXC8lzym9GYji6hPee9BSjaUgFDJtO6Q3N9VHbbRPFzvQXL0CtSM64jmGIyOLLsq6lJrPIF56qTbtDk1-57cmTvTkIao17k_Ej4XnGcindhOBN3dlV0VFjBspQP7AJVTiZ47QKSW8mJPfPQKTz_GYf9vJ4s-Cqk-T-xHIVGubqh2ABKxuoABHEVikZml-VgNe1V80ObD4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
صحبت‌های وایرال شده سرباز آمریکایی خطاب به مردم ایران :
اگه حمله زمینی شد بهتره فاصله بگیرید از نیروهای آمریکایی
نه اینکه بیان شمارو اذیت کنن، چون ارتش آمریکا خیلی مواظبه از سپاه که بعضیاشون لباس نظامی نمیپوشن
سپاه میخواد با اینکار به نظر برسه که مردم ایران علیه ارتش آمریکا هستن
سپاه اصلا توانایی نداره علیه ارتش آمریکا بجنگه
پس اینا می‌خوان پناه بشن بین مردم و حمله کنن چون اصلا نمیتونن رودر رو پیروز بشن
خداوند ارتش ایالات متحده و مردم ایران را حفظ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68541" target="_blank">📅 18:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68540">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6029372426.mp4?token=FkU2zLemxZD9gMLFTcmgWW9gejrfzIDKfZ5xlr2U8YkT9s0_AZMOlvWgQVtB74EXcgeOGrMSr8Zj8KlWPR-OZYsIq0jE1JSTQXfxl6pPd5YSb1gMWigOUeeEJPn4AIqPRgJ8xBN-hA6fFbuciBEGPEJJMzyjGvrD8OhB8l3j_blGihvQ_kw_CiX3GbKxhhMTBoE20GqQAjswWU4eQqCXlaqiO3h9tleO46YiZG-JK7R94aJ0PQA19JrIIfpLMQnnzMTdVcetHtr0OEjHKlkA6nnIPPCQT5EA6PLsolvYjfqfV7EsBKohkKg81SBhfj0BjfPh7Z-VGvgPRtB8bL2QiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6029372426.mp4?token=FkU2zLemxZD9gMLFTcmgWW9gejrfzIDKfZ5xlr2U8YkT9s0_AZMOlvWgQVtB74EXcgeOGrMSr8Zj8KlWPR-OZYsIq0jE1JSTQXfxl6pPd5YSb1gMWigOUeeEJPn4AIqPRgJ8xBN-hA6fFbuciBEGPEJJMzyjGvrD8OhB8l3j_blGihvQ_kw_CiX3GbKxhhMTBoE20GqQAjswWU4eQqCXlaqiO3h9tleO46YiZG-JK7R94aJ0PQA19JrIIfpLMQnnzMTdVcetHtr0OEjHKlkA6nnIPPCQT5EA6PLsolvYjfqfV7EsBKohkKg81SBhfj0BjfPh7Z-VGvgPRtB8bL2QiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این مجری که اخیرا زیاد در صداوسیما حضور داره گویا اهل کشمیر هندوستان هست.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68540" target="_blank">📅 17:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68539">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJ6Ea3yVLyHSF4_a1DCsFLpWFHz-x_Ycd-xSgHbwxxcdt-gRh65YJqHgVwy88iw1Xay3DhsPXOLhKO6O-nqT7uNFhI1qHnJ5FLd_Rv2Ky6Aw0F8eBfFTCIreg2Kf_XZgPPclHV9KpuA-mpP2hnqjD-qXaucnwkiSo55KxCp6AGE7rF1m0yG1OVcn_5XcMiskHZHXb8WgZn2wYzAJGB6ETYacX1eW8OQNXuJ_AZuPofMkpEstacfSnkadP6LWxZZBeVTlsnlmPRl6CHz2VP5ThJFZ6GGUZIBbivdwO8Ec3qCFVHwOXJgSIRcwbQNQAbfcFmEwS5VTYXibNrX9mg5g_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان انرژی اتمی جمهوری اسلامی:جت های آمریکا صبح امروز با شلیک چند موشک به سایت نیروگاه هسته ای درحال ساخت دارخوین در خوزستان حمله کردند.
ما حمله آمریکا به تاسیسات هسته‌ای دارخوین در خوزستان را که هنوز در حال ساخت است، محکوم می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68539" target="_blank">📅 17:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68538">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4472fedbde.mp4?token=STR23VoGGmkApkUq2u38hLda6pDJYZ98lrasN5cSuJddtqgaO8zvKvaf5gaSDZLL6gm8MSGvIXiGsXHWxGItTZRu9Z2CG3Ryp5cM7fsPvOqMrjj7tS_F0nRu4MkdxZhQAZJDjMF3mxAB9A-1hdIxs6YOiKspqTS7RXHEosCqjD_ic8vTV738x_HQpGxBVr2x6Iz5NI6vWv64NmjhKWo48ImGJqWWEg_psosRr5LuhAp_K-7yptLh0zzXPlTxsLFyBNpU-lZiqEGYF5xzMzO8K7mtTaoCNih7w-gM-dz5CA_TK2bzWE9wBkhrxM9DTdxZgCaBji6PmsluundMEgCHcyI7nztdKa6kIr0WNRKg_72B447L2Ah88uBJVJIN3B_yq7IhEHxJUBLluHZDk2dor3Heei8sRSVWL3oObRsVGuMrj2C2GilHYeZGxAITnEzqEWOBm1eboF-QmKqhDANUT5aIXHWKskyvtDiOxG_4lVzpfGK3Fh9kvvNxWC75I83dlyNDPlW6r7c0o45foo-T1cLE62-YY9lKVv_OxNUAL7sUWhTgsHK0hswOGPqxA4_v9FnPkaaN-TwL1t6VCpzW4VKKMRnnOc2twDeEewnEnXH9JMzMKJtMF5dQ_z5TMkIg_L3JTsoxjf62JiUmrsvvWD01fvcIBMlmXXaLj72egwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4472fedbde.mp4?token=STR23VoGGmkApkUq2u38hLda6pDJYZ98lrasN5cSuJddtqgaO8zvKvaf5gaSDZLL6gm8MSGvIXiGsXHWxGItTZRu9Z2CG3Ryp5cM7fsPvOqMrjj7tS_F0nRu4MkdxZhQAZJDjMF3mxAB9A-1hdIxs6YOiKspqTS7RXHEosCqjD_ic8vTV738x_HQpGxBVr2x6Iz5NI6vWv64NmjhKWo48ImGJqWWEg_psosRr5LuhAp_K-7yptLh0zzXPlTxsLFyBNpU-lZiqEGYF5xzMzO8K7mtTaoCNih7w-gM-dz5CA_TK2bzWE9wBkhrxM9DTdxZgCaBji6PmsluundMEgCHcyI7nztdKa6kIr0WNRKg_72B447L2Ah88uBJVJIN3B_yq7IhEHxJUBLluHZDk2dor3Heei8sRSVWL3oObRsVGuMrj2C2GilHYeZGxAITnEzqEWOBm1eboF-QmKqhDANUT5aIXHWKskyvtDiOxG_4lVzpfGK3Fh9kvvNxWC75I83dlyNDPlW6r7c0o45foo-T1cLE62-YY9lKVv_OxNUAL7sUWhTgsHK0hswOGPqxA4_v9FnPkaaN-TwL1t6VCpzW4VKKMRnnOc2twDeEewnEnXH9JMzMKJtMF5dQ_z5TMkIg_L3JTsoxjf62JiUmrsvvWD01fvcIBMlmXXaLj72egwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش امیر رولکس به حواشی ساعتش در جام‌جهانی:
به جا اینکه بگم فوتبال با ما سر ناسازگاری داره از کلمه خدا«داره مارو میکنه» استفاده کردم.
چهل چهلو پنج ساله ساعتمو دست راستم میبندم.
اگه یه سرمربی ساعت می بنده و لباس خوب می پوشه که اشکالی نداره.
اگر من زنجیر طلا مینداختم  و یقه پیراهنم رو باز میزاشتم آدم خوبی بودم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68538" target="_blank">📅 16:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68537">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5ipYBIiz4IJogqAAp4n-vJDaXRqYiyJ73NQPeJNxJJQFAPyyouxqgEGH87ZKpaXl7V7-2t3UD8E3PE2AQ5rasBHEWe8FI2iOoc3NfrUfQH0jtVq1P8xXNhSxU1Ncpa0miLGeME1Nrfzxu2aQQo8VsLEVmZWORy9ZIYfjOwthTcrnYrcQNyZO9sU5K0K8979jR7JzeX1LUiWYVqxYn-SNMHVd4k9wo2R0nPlDxOxogtU16Q-GK2LN9Sp2xlF-x4sZWDxU59erLzv-v8wjXTJRX7VXDcQMx8pT-Vw8HVgEJ0Tx4w-ZsRq1DoylwqUQC8cRXauBEm6WNunxOtYH_Zz_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پرزیدنت ترامپ:
جمهوری‌خواهان باید ایران را به لایحه تحریم‌های روسیه اضافه کنند. این همان کاری بود که لیندزی می‌خواست انجام دهد و قرار بود محقق شود. مهم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68537" target="_blank">📅 16:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68536">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UV_iup0nnH2BZXUEsiGbn5Wf9O_lPX2I9zNLmfwYgGw1p_Jwfg6w6hGMJ-_tOJFUr-NCFq7i-gdEd2xRDk8q-9C2GI_Lqqtfi7_OnG10lRwc7Pm8d0p_V5V7e0sX-FjRMSyMi4-7B37ifD1NrjiGAfR0yFqNsy6bma2wLcUTaaD-PzSZ-5jTpDK1GEowf43LF1LVWEuFv8weWnC3xU_XovOILsaATSax4hw5qx1YUUo1F3P_kE6uHSiihNLO0zLpW4Hhg69LNsmcGOIbgFAH8LBGZ_l3fx4AD5b-9bquMNz1biKQlFOz4I9N4NF8J0TR-wNpT2Vs52NPcEI1ZwjZ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">14 زندانی تو زندان دستگرد اصفهان برای اجرای حکم اعدام به سلول انفرادی منتقل شدن؛ این 12 نفر از متهمای پرونده میدان علیخانی هستن. +پرونده میدان علیخانی مربوط به  اعتراضات 18 دی 1404 تو اصفهانه؛ اون روز بین معترضا و نیروهای حکومتی درگیری شد و جمهوری اسلامی مدعی…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68536" target="_blank">📅 15:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68535">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇷
عراقچی:
بمباران بیت از طریق حفره امنیتی صورت گرفته و این حفره امنیتی همچنان وجود دارد
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68535" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68533">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3548648f57.mp4?token=Ry5xBaGLu0qZG4X895sSopUiQN5wAC22sdSX8JHCM0f0DCGIy_sTwIP-T8A3U1R-roYu_Qdgcewm8CX3So2q1W5eLGAmjtYh3ATsoUVH4MfGKZmAdsOvjivJ1FFRBfcNulskzuowTQaQX-fYvP-_nHPpBt-LFF57qyMGC_rHZeMR_4vrfj0oNQEgn8Jj3G8Kucs3IhDcZRIDNCYpdne1LYZfZpWNeEdbVOfhFRPmhC-dl5qoGi5adO6z2L-09TbfUmZ9SWw656JnOMxiZYm9PN6p5BByl9n4wpca7qvN_cvGO8s0tSUkcyqI0zmNBmyHsT6KK-HLzt2qV1k7Sfax6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3548648f57.mp4?token=Ry5xBaGLu0qZG4X895sSopUiQN5wAC22sdSX8JHCM0f0DCGIy_sTwIP-T8A3U1R-roYu_Qdgcewm8CX3So2q1W5eLGAmjtYh3ATsoUVH4MfGKZmAdsOvjivJ1FFRBfcNulskzuowTQaQX-fYvP-_nHPpBt-LFF57qyMGC_rHZeMR_4vrfj0oNQEgn8Jj3G8Kucs3IhDcZRIDNCYpdne1LYZfZpWNeEdbVOfhFRPmhC-dl5qoGi5adO6z2L-09TbfUmZ9SWw656JnOMxiZYm9PN6p5BByl9n4wpca7qvN_cvGO8s0tSUkcyqI0zmNBmyHsT6KK-HLzt2qV1k7Sfax6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
وضعیت ایستگاه مترو در کیف بعد از حملات سنگین روسیه به پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68533" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68532">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
جمعه و دوشنبه‌ها، شانس بردتان را دو برابر کنید
100% بانس میکس ورزشی تا سقف 30 میلیون ریال
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68532" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68531">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbgh7pGWHo5xizSRKWF_xEvpTpcetglUi4t6sFRCwPV1ALknYlfr6b2-ENgwyLAlPTVyfS9jBFmYVNOccdJQv4ySGx-IuH5AWQMAu_h8cs4agdGQXV0yIxhBVhUASWBP5zL_XTuaryBMWNFcnFq9pB2sCELfy2YWSGx-TCBz4YO1qIrk4-ACOWs6xBxvYB-00CIA8PadYu-3TlF2iFguHvOgWh-7pRsCkqDyQDU143HwIbl-wQtA6Z8Abk5MwuZ2f_cdzN0UbPfwLfKcerU7jXdsH8TJD7Qt8mxOYOVJ1mT_xNos51gQiyZ8tBew7Ohp-LrkKYmHXka-N3lfXLu4dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال جام‌ جهانی 2026
⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
⏰
شروع بازی ساعت 22:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68531" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
