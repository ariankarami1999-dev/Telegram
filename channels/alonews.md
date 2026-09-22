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
<img src="https://cdn4.telesco.pe/file/vISDtCftnA20Twf5uc23E5YWsvus-NX9Fl1XBt3IuaK-lCAyQgU9itzXAsoZqITAjpCq3hsOexpKSyiQdKV6MTsenEBVnx8t-UMMh3Wr3oE_umV3hyotWM-ImHVDLGsIl7GPpLhrTTgQ6y-Eg3KZ7HQgKnwKruupHC6tyx8Rz03_sh5PHzyofSh2ZpCJazCXOp7Z_OdE40_n0DmoPnQhPCoF8B34YhHA-VsuseOBcn_V2I0P330I1C4lZcQ36KxgmlYmoHeAlQ3jGttBK_SwWoXoTHWtiQrvX2KB8d6lFts4QdUZzQeIM3QAluiRdDKu1laWRP4WPY_uuvaQLdSIvg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 991K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 18:34:28</div>
<hr>

<div class="tg-post" id="msg-148781">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏
👈
ترامپ:
زنمم تو سالنه، کوشی خانم؟ کجایی؟ اون فوق العادست عالیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/148781" target="_blank">📅 18:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148780">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=HisO0OhqTQ-gAlASIslOVoeqJnno_P5yDNNSoVfhVGbEbCMVYJ9JBuWImP4WAI7p1P0fFFkQX_keNWkIyYn7Um9JX7kONEJCorqe3ptqwt0SYhm_sdh7zKEn1K05JNW_c5-0TlskG9cYF3NMxghaQbidkr3BYsXjMZI6NSSV7FqkwGU5F4KlNgMTvyuT0G5YLmPMD3qYaX-iTqyo7eVi2rrIpJVyl8n7st1Xz6294LNtZxE1_Vjim-G6-1RO9YCg8-dy2OjEvPGTBRZsaKujJOrhvxVNK5rC5HITIDxX_GYMhK8JOpGypt7f-Hn1vnNzhbgx3cVzoWdS6UrA2Qy8_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=HisO0OhqTQ-gAlASIslOVoeqJnno_P5yDNNSoVfhVGbEbCMVYJ9JBuWImP4WAI7p1P0fFFkQX_keNWkIyYn7Um9JX7kONEJCorqe3ptqwt0SYhm_sdh7zKEn1K05JNW_c5-0TlskG9cYF3NMxghaQbidkr3BYsXjMZI6NSSV7FqkwGU5F4KlNgMTvyuT0G5YLmPMD3qYaX-iTqyo7eVi2rrIpJVyl8n7st1Xz6294LNtZxE1_Vjim-G6-1RO9YCg8-dy2OjEvPGTBRZsaKujJOrhvxVNK5rC5HITIDxX_GYMhK8JOpGypt7f-Hn1vnNzhbgx3cVzoWdS6UrA2Qy8_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: آمریکا و ایران قطعاً به نتیجه خواهند رسید؛ به هر طریقی که باشد
🔴
دونالد ترامپ درباره ایران گفت: «آمریکا و ایران قطعاً این مسئله را حل خواهند کرد؛ به هر طریقی که باشد، این کار انجام خواهد شد.»
🔴
او افزود: «این اتفاق سریع رخ خواهد داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/alonews/148780" target="_blank">📅 18:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148779">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee7ed8073.mp4?token=h9vL7o4BDJ3_b0l5DkaxhGIdxB3hffL1yZSyecQ6rPjgYbEwY82M_8sAMatKZWgx216dbS_nMNNNlULTMDYCF8mZ66Xgky-HHFuoXAodGmVxJEhhX5BHUG70med-8-THne5QCjc7KUIo7CoLKzo3M7jyYEgkGc88flBpCjjsR_oAvwzUKPadheFNVS-7NQcJTrhe6LhNyIFvIS18S2WCtWoK7NqeyNkvtXHgmqR_JZgkzciKEt482w2K0cvDGsERIIkYcOSH1xLtdqS4JQx_6P3B5BZb7kBcP24bFe6vTIFfxMnyrAL1oIL2eYsOl-4ApzUuKAUVMymnfcwq7gDmKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee7ed8073.mp4?token=h9vL7o4BDJ3_b0l5DkaxhGIdxB3hffL1yZSyecQ6rPjgYbEwY82M_8sAMatKZWgx216dbS_nMNNNlULTMDYCF8mZ66Xgky-HHFuoXAodGmVxJEhhX5BHUG70med-8-THne5QCjc7KUIo7CoLKzo3M7jyYEgkGc88flBpCjjsR_oAvwzUKPadheFNVS-7NQcJTrhe6LhNyIFvIS18S2WCtWoK7NqeyNkvtXHgmqR_JZgkzciKEt482w2K0cvDGsERIIkYcOSH1xLtdqS4JQx_6P3B5BZb7kBcP24bFe6vTIFfxMnyrAL1oIL2eYsOl-4ApzUuKAUVMymnfcwq7gDmKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: جنگ اوکراین زودتر از آنچه مردم تصور می‌کنند پایان خواهد یافت
🔴
دونالد ترامپ درباره جنگ اوکراین گفت: «ما همکاری بسیار نزدیکی با رهبران روسیه و اوکراین داریم و این مسئله را حل خواهیم کرد.»
🔴
او افزود: «فکر می‌کنم این اتفاق سریع‌تر از آنچه مردم تصور می‌کنند رخ خواهد داد؛ آن‌ها دیگر از این جنگ خسته شده‌اند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/148779" target="_blank">📅 18:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148778">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ترامپ: بزدلان و خائنان دوست دارند بگویند ایالات متحده با کمبود مهمات مواجه است، اما چنین چیزی درست نیست.
🔴
ما بیش از آن مقدار مهماتی داریم که حتی بتوانیم تصور کنیم ممکن است از آن استفاده کنیم و در حال تولید مهمات با سطوحی هستیم که هرگز پیش از این تجربه نکرده‌ایم. ما ذخایر خود را سریع‌تر از هر زمان دیگری افزایش می‌دهیم؛ مهمات و تجهیزات درجه‌یک.
🔴
علاوه بر این، در آینده‌ای بسیار نزدیک، کارخانه‌های عظیم تولید مهمات افتتاح خواهند شد. در حال حاضر ۱۸ کارخانه توسط بزرگ‌ترین شرکت‌های صنایع دفاعی جهان در حال ساخت است؛ ۱۸ کارخانه در دست احداث است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/148778" target="_blank">📅 18:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148777">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ترامپ: جمهوری اسلامی تروریست است
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/148777" target="_blank">📅 18:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148776">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=aZblgDWILJyHybee_eGaCMiW0F0UsplJJr6zx38OUIT0PRWwslD6b-u6GRGUJd-z3GLRiPdGy-Dqcy-XGjZ_t_Y-oqd-FIE2XLuGVeok_CHoYFxKppXlPoRJMI1G7A1pI8X0Usy0NcHzlASXs5ngNUVtO47czG80bhX5zfCRfrYHj2_mQrtY4mNBQYjm_Id7dfJZ90LgZeK9i3Zmb4SwmktEWF-OYkUCKpdWMXPoaVImZWIE6qNBllg8kyXW7EhJ0dLyLNKpMI2WO9a8g6naadN8iVeOysCfM3stAg9MycNn0cpSdjdlJb0lxzOHfwzi-DoMlA7GdOIEoFBjNjOXfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=aZblgDWILJyHybee_eGaCMiW0F0UsplJJr6zx38OUIT0PRWwslD6b-u6GRGUJd-z3GLRiPdGy-Dqcy-XGjZ_t_Y-oqd-FIE2XLuGVeok_CHoYFxKppXlPoRJMI1G7A1pI8X0Usy0NcHzlASXs5ngNUVtO47czG80bhX5zfCRfrYHj2_mQrtY4mNBQYjm_Id7dfJZ90LgZeK9i3Zmb4SwmktEWF-OYkUCKpdWMXPoaVImZWIE6qNBllg8kyXW7EhJ0dLyLNKpMI2WO9a8g6naadN8iVeOysCfM3stAg9MycNn0cpSdjdlJb0lxzOHfwzi-DoMlA7GdOIEoFBjNjOXfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: انتخابات هیچ تأثیری بر تصمیم من درباره ایران ندارد
🔴
دونالد ترامپ درباره ایران گفت: «برای انتخابات، در ارتباط با ایران، مطلقاً هیچ اهمیتی قائل نشده‌ام و نخواهم شد؛ حتی به ذهنم هم خطور نمی‌کند.»
🔴
او افزود: «تنها چیزی که برای من اهمیت دارد این است که ایران هرگز سلاح هسته‌ای نخواهد داشت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/148776" target="_blank">📅 18:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148775">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ترامپ: رهبر ایران(اسبق) کشتار زن و بچه یهودیان در ۷اکتبر را تبریک گفته بود او تروریست بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/148775" target="_blank">📅 18:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148774">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ: من از تمام کشور های جهان میخواهم که به جنگ اقتصادی تمام عیار آمریکا علیه ایران بپیوندند تا زمانی که ایران برنامه هسته ای خود و حمایت از شبه نظامیان را کنار بگذارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/148774" target="_blank">📅 18:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148773">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63e99476e.mp4?token=q8-R3vQVaPdWihNSFVEAUqj8W7L-otVgG2Y331i9I0jI2pz-tf_vu_FvsbTy4yW98cxqIs4yary6Egc3itHvFEteZkJrQXTsdJEPTaAc5WHOAvM_Ou6CB6J0GAvi8NZZ_JNnxlAevLoqfvMRkreIDN50-nmwhPYxaorGELAGJihek3-BIEQYccwXDvtwfWyF75Y8GDn7jFhJRVdtNVsp-df0BCrt2gwy1zpv37NLrrJ5w-UeH--ZccCDeTZFoo4tRnSp9tPpGL-N4yRGLM__GDz5SR0muzPF-8nxvD5FYfTTo7CWUNPnF7-PYlIEYf5A-HLqGkdRSIWlXzddMbM6sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63e99476e.mp4?token=q8-R3vQVaPdWihNSFVEAUqj8W7L-otVgG2Y331i9I0jI2pz-tf_vu_FvsbTy4yW98cxqIs4yary6Egc3itHvFEteZkJrQXTsdJEPTaAc5WHOAvM_Ou6CB6J0GAvi8NZZ_JNnxlAevLoqfvMRkreIDN50-nmwhPYxaorGELAGJihek3-BIEQYccwXDvtwfWyF75Y8GDn7jFhJRVdtNVsp-df0BCrt2gwy1zpv37NLrrJ5w-UeH--ZccCDeTZFoo4tRnSp9tPpGL-N4yRGLM__GDz5SR0muzPF-8nxvD5FYfTTo7CWUNPnF7-PYlIEYf5A-HLqGkdRSIWlXzddMbM6sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ایران ۷۲هزار شهروند معترض بی گناه خود را به قتل رسانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/148773" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148772">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏
🔴
فوری/ترامپ در سازمان ملل:
با تصمیمی بزرگ در مورد ایران روبه‌رو هستم؛ توافق یا نابودی کامل
🔴
آیا به توافقی دست یابیم که به این کشور اجازه دهد به ملتی بسیار بزرگ‌تر تبدیل شود، یا اینکه آن را به‌طور کامل نابود کنم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/148772" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148770">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ: جمهوری اسلامی معترضان را میکُشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/148770" target="_blank">📅 18:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148769">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ترامپ: به مدت ۵۱ سال، حکومت افراطی ایران با خونریزی و کشتار گسترده حکومت کرده و در سراسر خاورمیانه و فراتر از آن، مرگ، ویرانی و هرج‌ومرج به راه انداخته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/148769" target="_blank">📅 18:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148768">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e271237b80.mp4?token=JCDmrQAVOSBQOaN1YzPbPPVgkOmBkI10jhWwmX0ChGEyYlQgagcH5k9OL-G-0gRBsrVU95vkrnpSnUgHIfpU_5TNSMyEUYl8JuXd38lDMPHvEQlhw23953ufdWUfpemSXzQxWrAC7AfKAz5XHEh7A7anGZT0Hu6XmLj_1sl95Zm5HaKWTgsuXgqKwDxZlA3MD2XWndg_F796MurIKrz07h_DmPeBltUYaMS1uONHcUeFHRzg1MROQM5887EaBd0BDxTIL-GnKQHH_Ci-0IbkTPI6Ui79NAyN73Zvo3YtSSABYJ1cC4W_cz2DizI2TmPApL-UJVhggEyjZiVf1VRtYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e271237b80.mp4?token=JCDmrQAVOSBQOaN1YzPbPPVgkOmBkI10jhWwmX0ChGEyYlQgagcH5k9OL-G-0gRBsrVU95vkrnpSnUgHIfpU_5TNSMyEUYl8JuXd38lDMPHvEQlhw23953ufdWUfpemSXzQxWrAC7AfKAz5XHEh7A7anGZT0Hu6XmLj_1sl95Zm5HaKWTgsuXgqKwDxZlA3MD2XWndg_F796MurIKrz07h_DmPeBltUYaMS1uONHcUeFHRzg1MROQM5887EaBd0BDxTIL-GnKQHH_Ci-0IbkTPI6Ui79NAyN73Zvo3YtSSABYJ1cC4W_cz2DizI2TmPApL-UJVhggEyjZiVf1VRtYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ایران موشکی با قابلیت هدف قرار دادن اروپا ساخته بود
🔴
دونالد ترامپ درباره ایران گفت: «آن‌ها موشکی ساخته بودند که قادر بود اروپا را هدف قرار دهد و به آن بسیار افتخار می‌کردند؛ امیدوارم اروپایی‌ها این موضوع را درک کنند.»
🔴
«هدف ایران این بود که در پشت سپر موشک‌های بالستیک متعارف، ساخت بمب هسته‌ای خود را تکمیل کند.»
🔴
ترامپ افزود: «اگر آن‌ها موفق می‌شدند، این حکومت می‌توانست بدون محدودیت به گسترش ترور و مرگ ادامه دهد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/148768" target="_blank">📅 18:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148767">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=X43mfrde7DNStszNIgAc44x17FuVfucgeYTgaoAmrMaXKab78zLm3Z8AH14Gkj_VyX21FchcuC7OwH-G8ZHxJJMYbZM2NYx6b2lodJtirnwCqt7hIsxR9UZv9Kvp9DpAG4EIrj43Bavem6qo1URRuIW_XehiEJFjIbOhpvXmXxaxSRrNDYmFSJmSl0-sOtkSBdY-6seJkUhUyrDlcUT7whEAhImF5RGoEP6uzWJhmdAhE6LM2f8zI2cFqDVcDJfYkIM_BUbwtk4joV5nLK3iFEjiWbT5qf02Fg1XV4PM8R08WHWc_74wwljD67ATIFUyrqcw6L3QM5UM2mlDRVaZIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=X43mfrde7DNStszNIgAc44x17FuVfucgeYTgaoAmrMaXKab78zLm3Z8AH14Gkj_VyX21FchcuC7OwH-G8ZHxJJMYbZM2NYx6b2lodJtirnwCqt7hIsxR9UZv9Kvp9DpAG4EIrj43Bavem6qo1URRuIW_XehiEJFjIbOhpvXmXxaxSRrNDYmFSJmSl0-sOtkSBdY-6seJkUhUyrDlcUT7whEAhImF5RGoEP6uzWJhmdAhE6LM2f8zI2cFqDVcDJfYkIM_BUbwtk4joV5nLK3iFEjiWbT5qf02Fg1XV4PM8R08WHWc_74wwljD67ATIFUyrqcw6L3QM5UM2mlDRVaZIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: به ایران در ازای پایان برنامه هسته‌ای و حمایت از تروریسم، همکاری کامل اقتصادی پیشنهاد دادم؛ اما نپذیرفتند
🔴
دونالد ترامپ درباره ایران گفت: «پس از آغاز به کارم در سال گذشته، مذاکرات با ایران را آغاز کردم و در ازای پایان دادن به برنامه هسته‌ای و حمایت از تروریسم، همکاری کامل اقتصادی را به آن‌ها پیشنهاد دادم.»
🔴
او افزود: «اما آن‌ها این پیشنهاد را رد کردند؛ این یک اشتباه بزرگ بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/148767" target="_blank">📅 18:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148766">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ترامپ: ایران دیگر قلدر خاورمیانه نیست؛ هرگز اجازه دستیابی به سلاح هسته‌ای را نخواهم داد
🔴
دونالد ترامپ درباره ایران گفت: «آن‌ها قلدر خاورمیانه بودند، اما دیگر قلدر نیستند.»
🔴
او افزود: «از نخستین روزی که وارد عرصه سیاست شدم، موضع من تغییر نکرده است؛ هرگز…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/148766" target="_blank">📅 18:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148765">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29ba0a501a.mp4?token=TMn7_fDkysYTjP4b-4DNdO_L9x1zqRYVPdr57X8DSfb2TpOQwdKnTDCbkXhMFoZfYyDCX3DIY-6PKGunIBACD2qxnEd-r1yEYvnXdayYJUMy0U_CGJOJt_XqewZqA-vZySF9J--uxo8i-XRkCE7CPsmXlbGpUCLb7jDHNjoF4ECDKDAltTDnsMC8GTZY5jnkhEXB561-PTstdIUEWpd2ug0XUpDsA4cS_p5nQNhBxTjjvowZmI2r0et_6PmeoLsn-6o1XsbRgUWoZ5disXLZ6JHykXAmJ6JEZHrgb1CQ5n__0fle4WGHFGslMe-0DWKHORlfKN2pGs8r_8EeMST2lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29ba0a501a.mp4?token=TMn7_fDkysYTjP4b-4DNdO_L9x1zqRYVPdr57X8DSfb2TpOQwdKnTDCbkXhMFoZfYyDCX3DIY-6PKGunIBACD2qxnEd-r1yEYvnXdayYJUMy0U_CGJOJt_XqewZqA-vZySF9J--uxo8i-XRkCE7CPsmXlbGpUCLb7jDHNjoF4ECDKDAltTDnsMC8GTZY5jnkhEXB561-PTstdIUEWpd2ug0XUpDsA4cS_p5nQNhBxTjjvowZmI2r0et_6PmeoLsn-6o1XsbRgUWoZ5disXLZ6JHykXAmJ6JEZHrgb1CQ5n__0fle4WGHFGslMe-0DWKHORlfKN2pGs8r_8EeMST2lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ایران دیگر قلدر خاورمیانه نیست؛ هرگز اجازه دستیابی به سلاح هسته‌ای را نخواهم داد
🔴
دونالد ترامپ درباره ایران گفت: «آن‌ها قلدر خاورمیانه بودند، اما دیگر قلدر نیستند.»
🔴
او افزود: «از نخستین روزی که وارد عرصه سیاست شدم، موضع من تغییر نکرده است؛ هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست پیدا کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/148765" target="_blank">📅 18:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148764">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
پیام مجتبی به دانش آموزان: تقوا داسته باشید تا قله‌ها رو فتح کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/148764" target="_blank">📅 18:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148763">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBrG8VzrXWMdyycLn8VLo-FlAIXOelPC1chs4-W8COPSMA-2yA0thgCMp3cNfVJoV5c4BUPDlOsRjlWrIKrQw8_ZuzOtXVoItUzp7qPmcVFL9IhKpbj3L89P1LooCbkZrvUhWw_ma4pkjvXrBaK3csAutOPsVdwi5LosOf8R2GBuKtHB093KjG5YKsvq7xvZhXZ7x77KAha90diMNjhVYxMipp8cgdfI-9MhYX44uByTK3SssqY5kbmyWW8dKNAl4KxKOCcl1HpQzBOovFgHa1jDuMvYgFHgdNpMb1kqAx7vNcT6qJPJC3oZQbj1PX-h-wJk-P4HXHp70KqkhPu_dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تلگراف :
ترامپ در حال بررسی گزینه‌های مختلف درباره ایرانه؛ از مذاکره و  تشدید حملات و افزایش فشار اقتصادی گرفته تا حتی «منفجر کردن کل ملت ایران»!
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/148763" target="_blank">📅 17:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148762">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوری/هم اکنون پس از شرکت‌های ترکیه و عراق، شرکت های هواپیمایی امارات و قطر نیز پرواز های خود به ایران را متوقف کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/148762" target="_blank">📅 17:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148760">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AjZi8bbkbOMH9PKQecwognsBlY8_h_KHDjrwY6LzGyl_umXx6MatT88-DY4u0DqVvMjpiin3tJIIBs2hQGPzKhaWiFe-OO_stfyfJLUEFKdzRRDMh0tPEo_56Y4UJRrAftamn9dt1TWWVGWytBrNGg70dKXQy-LpApDPPGnlpPVX8owr7NUkbP6Pf1CoOQdNVeEp1vBdHBpoywSw_eXCDMBuzyTgTrCl1U5wLE9-_I4Q6LMxwAVVkM0yGPE3vdGz2n4H9_w5RSvcupG78KjQDEdMjIurJhF3VcDjytocPIuGu5-HTfe25hFzLHoQCBuudHwgNBwghFdAw5EPs4YPyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jJkPPJOp4fkAEXlqyPHsOV9yDSkjQZNaCo_dBXn1HZtae_Hh8mA_LCpkdDFGIRfXAoX6LqWLd2FMqECN1p7UWb4wxOGEFb9TCYA-JNW-MhG949kryUTBUaSCoeUsEwV5j4WhE4dHYm0T-rl0idD2Ri51fTlNimZBoKwoLhv1N-EGpJmY2-ax6v07lDBcA3apfMAOUVOvREuQi79NsuEPPf6l604Bs42oT6D3xJb54CX_IiO1g0wJBKyGwnJSly6VeguflU_cKAQ0H35UVEfY6wGhc9wZp52Uw2f05CKdwLGtCRYd8a7UW4dktVEHei2YF4Dm1jJNC9P-f8IffXNv4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
عرازشه:
پزشکیان باید ترامپ رو به قتل برسونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/148760" target="_blank">📅 17:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148759">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
طبق گفته اکسیوس، ترامپ قرار است در سخنرانی خود در مجمع عمومی سازمان ملل این ها را بگوید
:
در آمریکا، به‌تازگی بیست‌وپنجمین سالگرد هولناک‌ترین حمله تروریستی تاریخ را پشت سر گذاشتیم؛ حملات ۱۱ سپتامبر که در آن حدود ۳ هزار نفر، تنها چند کیلومتر دورتر از اینجا، کشته شدند.
دو هفته دیگر، سومین سالگرد حمله ۷ اکتبر در اسرائیل را گرامی خواهیم داشت؛ حمله‌ای که در آن تروریست‌های مورد حمایت مالی ایران، ۱۲۰۰ غیرنظامی بی‌گناه، از جمله ده‌ها آمریکایی، را شکنجه کردند، به اجسادشان آسیب رساندند و کشتند.
رهبر جمهوری اسلامی ایران این کشتار را جشن گرفت و آن را «خدمتی به بشریت» خواند.
همین حکومت امسال بیش از ۷۲ هزار نفر از شهروندان خودش را به قتل رسانده است.
فقط تصور کنید اگر چنین حکومت نفرت‌انگیزی می‌توانست در حالی که زیر چتر هسته‌ای قرار دارد، حملات تروریستی گسترده‌ای انجام دهد، چه وضعیتی به وجود می‌آمد.
این همان واقعیتی بود که ما مجبور شدیم با آن روبه‌رو شویم؛ واقعیتی که بسیاری ترجیح می‌دادند نادیده بگیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/148759" target="_blank">📅 17:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148758">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7aa5b4a7d.mp4?token=J7sBKNvFDc5lpv3DM_sC8tmI0BRIsxoTeEKZMEHdpeIEvDIRhVxnbeCbtY4HiHdFWF2TNInZXoRotYGPDkjjdPlLVbQUyqIHZDYu_-ndl5hiUjyTaFQQo4i4JfUoJjLeY0HSvzO7T6lK5tsaIcAvkQK-U2XqftkOUN7noegRM8POhTp-8iicaLAWDWSfv2kIKD7o7w2W7SfkjVy2ficHvdIRuTl8Uo1hR2dc76r8cBE4xSkJ2SwU2x2NXrr9x9WDut3bCAUzmTun7qFuZj88WJpe0l25JwlsAufmGsgrMUjn0J9VvgVGzXbRzXZjzxuFKhY-jE_GtT4iaq_YjalQ5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7aa5b4a7d.mp4?token=J7sBKNvFDc5lpv3DM_sC8tmI0BRIsxoTeEKZMEHdpeIEvDIRhVxnbeCbtY4HiHdFWF2TNInZXoRotYGPDkjjdPlLVbQUyqIHZDYu_-ndl5hiUjyTaFQQo4i4JfUoJjLeY0HSvzO7T6lK5tsaIcAvkQK-U2XqftkOUN7noegRM8POhTp-8iicaLAWDWSfv2kIKD7o7w2W7SfkjVy2ficHvdIRuTl8Uo1hR2dc76r8cBE4xSkJ2SwU2x2NXrr9x9WDut3bCAUzmTun7qFuZj88WJpe0l25JwlsAufmGsgrMUjn0J9VvgVGzXbRzXZjzxuFKhY-jE_GtT4iaq_YjalQ5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ هنگام ورود به مجمع عمومی سازمان ملل خطاب به سی‌ان‌ان:
🔴
تعجب می‌کنم که سی‌ان‌ان اینجاست و اخبار مربوط به مرا پوشش می‌دهد. شما نباید اینجا باشید.
🔴
شما گفته بودید که قرار نیست اخبار مرا پوشش دهید. نباید مرا پوشش دهید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/148758" target="_blank">📅 17:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148757">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCuZnlQr4093-Zfzs5SC_hi-8RWxdL9ccW36856Cc32S98QhzZuPmbMuoFOb2enfja8Um3BiX4mc7ZQzBG_gGe-VMAbQGBd03y_UqyvgnONsN9oUipHI11qdozuzKo7Xzn-rzQpdLbGWbciUkPX1MZ8ymbOKwyP-kboy7Ttb3wGaEZfhcaHlUB7IEozUUXCGAygWPVTwmycnjjCbYQ92D5AA8WZGd9LSJZCMVe1yKliI-B0FFBF4mHT2UPiFraUQqiHKf184Dq1hURnHCOOIS_koaWCmKfS3FG55k1yeqwFz-2TTzeWwPmIJpV-x_6HmcuFWOzhqGXk9l0eKbRRqxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ امروز یه شبکه اینترنتی به نام "TRUMP TV" راه انداخت و قراره 24 ساعته سخنرانی‌ها و برنامه‌هاش رو پخش کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/148757" target="_blank">📅 17:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148756">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
کمیته امنیت ملی مجلس: آمریکا جرعت نزدیک شدن به تنگه هرمز رو نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/148756" target="_blank">📅 17:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148755">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm5EUY0T1zPniiS96gl15_CC2-TQXHDR_Tqy7fgDnVjr9KqHondciFTRUqB-qmBv0ZLNLysrKx4ThOzvJAmHA6qQGFqv_O6HtHAvh9sn3EwagahTt8UQjSeigjOS-1t-MOz73D6ajZC792uMPIX7KTmaG-RYVnLt5aQSLSsAtRF9rAqvhwhMEL7KEhxXDMssVe9o8MzQFcaljOoXfktnOBJwSoc23ucgQ2_heDLn4MAXU4tnec4LuOc6ideMj-Jt-NXL8vPx0a1fxfUeQBklwVdhMgIEGwf1PAojsCYWgdaiuK1QstwHsxSRv_1ZtEfEL-aiyIw_-tW9LMU3P-CW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامینگ سون
🤣
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/148755" target="_blank">📅 17:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148754">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
آنتونیو گوترش، دبیرکل سازمان ملل متحد: «ما نمی‌توانیم اجازه دهیم راه‌حل دو کشوری در برابر چشمانمان از بین برود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/148754" target="_blank">📅 16:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148753">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca659922b.mp4?token=HMRqCLuPknTFeYYtuY7k5EvpCIVuABiBGzfK6e1F1j4ie7JYVPlmALqVvuCvGP8OqPuNH0RjDxFpKxyi5Y2FGKdqiJc32MhgJtjXW_BKqBEW6OrPAa62qLvNKNFlZkdS0Ek24DfwaRy8VJB8uv9xv0osc-H3GXUOCKcD5mX5i8Gu5Q8hL5Q7mHYYd_QejNDZ1UK9YRNzb2kBsCi-oUckonilRU119t81o9ZFZq1OF6fIH1CYHDNy167fqNBfdwU5TiGN69uw-N_e2122qzTkpF43Z7cgwYocN7zBn9AvL3TZ7Ti8pdjfqd-iQWBqHrNBrA28FaLqdqKsmDgOtVQgQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca659922b.mp4?token=HMRqCLuPknTFeYYtuY7k5EvpCIVuABiBGzfK6e1F1j4ie7JYVPlmALqVvuCvGP8OqPuNH0RjDxFpKxyi5Y2FGKdqiJc32MhgJtjXW_BKqBEW6OrPAa62qLvNKNFlZkdS0Ek24DfwaRy8VJB8uv9xv0osc-H3GXUOCKcD5mX5i8Gu5Q8hL5Q7mHYYd_QejNDZ1UK9YRNzb2kBsCi-oUckonilRU119t81o9ZFZq1OF6fIH1CYHDNy167fqNBfdwU5TiGN69uw-N_e2122qzTkpF43Z7cgwYocN7zBn9AvL3TZ7Ti8pdjfqd-iQWBqHrNBrA28FaLqdqKsmDgOtVQgQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی با وزیر خارجهٔ ایتالیا دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/148753" target="_blank">📅 16:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148752">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
وزیر بهداشت: کرونا نیاز به واکسن ندارد و شرایط تحت کنترل است
🔴
مردم توصیه‌های بهداشتی را رعایت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/148752" target="_blank">📅 16:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148751">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f8382345.mp4?token=BicRXR9tPfEEUCQNqGxnIsZccu483Uw1QsQOo2sDJp3CBWXHH466k_k0wXMqXID3Wh_g1wW9mKbULm7onTNQNNhtBkLLLWzswSisMZdtQ9FI0PYQ2SAymyhK_np-TrfIu3A1flxEmVQsrBop73XT6BJVEDws1UrjYOHp0RrWhe7CgNiWhDU1FCp5E6emAiut5D-3E1s9wghkDMAmQEsV1Ojl_qiqRZxrBL3U5qqqELZ6H3bMmVzdbO-qrMKhSDzmzxjdpwp0Lc1HNSVlDG-eDN6LgzN_FesrEoacjMJ8lkHSUlHXCM1iaS20mRWUgHfaFntsIzMXSf15CN5IDcCRIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f8382345.mp4?token=BicRXR9tPfEEUCQNqGxnIsZccu483Uw1QsQOo2sDJp3CBWXHH466k_k0wXMqXID3Wh_g1wW9mKbULm7onTNQNNhtBkLLLWzswSisMZdtQ9FI0PYQ2SAymyhK_np-TrfIu3A1flxEmVQsrBop73XT6BJVEDws1UrjYOHp0RrWhe7CgNiWhDU1FCp5E6emAiut5D-3E1s9wghkDMAmQEsV1Ojl_qiqRZxrBL3U5qqqELZ6H3bMmVzdbO-qrMKhSDzmzxjdpwp0Lc1HNSVlDG-eDN6LgzN_FesrEoacjMJ8lkHSUlHXCM1iaS20mRWUgHfaFntsIzMXSf15CN5IDcCRIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ورود فیصل بن فرحان بن عبدالله، وزیر امور خارجه عربستان به نشست مجمع عمومی سازمان ملل متحد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/148751" target="_blank">📅 16:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148750">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a14e65bfd.mp4?token=Uk_dN4IP3z5TCPUIHeSHnL_PKMMf7hXWQG22tDTWd_mbnVlw1hRVlWdl_SJQuuO45Y4gLWNnQn9NPOVJAK4RYkQGexpeQgmS8tvCso1cqB1ZsAOHzBcJjfk5xInJMtraQuP4DXJTRqxCrGQY2RJuC1487xh5UQtu4zwhsT_ndksWxxUMoTkMR1x6uxbZ0ZzzlOKExIaaQHSfaJlJwTpCzXuRj6e4ylVZ929TmDimv5cHdN4iFFEoJ4k2xKKXz04Gj3VT2LTy_rAOdKuzEnSgq0Nq8CZHKQIPwqtzb_xd27tB9kstPV-fPZyGIm8Pj960MbzLUep0rqzVlipSLr5seA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a14e65bfd.mp4?token=Uk_dN4IP3z5TCPUIHeSHnL_PKMMf7hXWQG22tDTWd_mbnVlw1hRVlWdl_SJQuuO45Y4gLWNnQn9NPOVJAK4RYkQGexpeQgmS8tvCso1cqB1ZsAOHzBcJjfk5xInJMtraQuP4DXJTRqxCrGQY2RJuC1487xh5UQtu4zwhsT_ndksWxxUMoTkMR1x6uxbZ0ZzzlOKExIaaQHSfaJlJwTpCzXuRj6e4ylVZ929TmDimv5cHdN4iFFEoJ4k2xKKXz04Gj3VT2LTy_rAOdKuzEnSgq0Nq8CZHKQIPwqtzb_xd27tB9kstPV-fPZyGIm8Pj960MbzLUep0rqzVlipSLr5seA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مرادویسی، تحلیلگر اینترنشنال :
اینکه ترامپ، پزشکیان و عراقچی رو تو خاک آمریکا دستیگر کنه و مثل مادورو بندازه زندان، احتمالش خیلی کمه اما صفر هم نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/148750" target="_blank">📅 16:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148749">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🤫
اگه توام دنبال کد تخفیف
🆓
📌
دیجی کالا و اسنپ و ..... هستی بیا
👇
🛍
https://t.me/off_khooneh
🛍
https://t.me/off_khooneh</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/148749" target="_blank">📅 16:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148748">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
سی‌ان‌ان: دونالد ترامپ به مشاوران خود گفته است که اگر "شرایط مناسب باشد"، مایل است با مقامات ایرانی که در مجمع عمومی سازمان ملل متحد در نیویورک حضور دارند، دیدار کند. یک مقام آمریکایی این مطلب را اعلام کرد.
🔴
هیچ جلسه‌ای هنوز برنامه‌ریزی نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/148748" target="_blank">📅 16:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148746">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
رایزنی تلفنی پوتین و بن‌سلمان در خصوص موضوع یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/148746" target="_blank">📅 16:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148745">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
منابع دولتی عراق به خبرگزاری العربیه:
تا کنون تصمیمی برای ممنوعیت فرود هواپیماهای ایرانی در فرودگاه‌های عراق اتخاذ نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/148745" target="_blank">📅 16:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148744">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سخنگو سپاه: به فناوری موشک خیلی دوربرد رسیدیم، منتظر دستوریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/148744" target="_blank">📅 16:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148743">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a8258249.mp4?token=aNtaSdBi0p9Tpj_ZXbcHtetao7GQs3JhV_MMjb7tCPZdG81cDKiBR-J0e4KPuOSH-k16Liv34ZgHvQOyRzxwntZ6ViqAZIQ8yIaydai-HM221PtTnFnJLuk7-0rkvAwQviviVqEy4R5BsfJSP0XbCkrKjigBxGrGgetXixEVQ3ltP0pgScQOR-Z-AJ78xszXLnH6Q0WlssnWt0-JP58DzCUkK8ljqCcOFdEbOTKq49BBReSZthMIWWra2WkGrt60V021HlBJ9yIoU1CI2ZySDkYu0vCgJsGvCnrE2HwhruwpYa_FlkVeA0Pz76Rn3IMLmJUpfkP03mmmh-zPUg3qhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a8258249.mp4?token=aNtaSdBi0p9Tpj_ZXbcHtetao7GQs3JhV_MMjb7tCPZdG81cDKiBR-J0e4KPuOSH-k16Liv34ZgHvQOyRzxwntZ6ViqAZIQ8yIaydai-HM221PtTnFnJLuk7-0rkvAwQviviVqEy4R5BsfJSP0XbCkrKjigBxGrGgetXixEVQ3ltP0pgScQOR-Z-AJ78xszXLnH6Q0WlssnWt0-JP58DzCUkK8ljqCcOFdEbOTKq49BBReSZthMIWWra2WkGrt60V021HlBJ9yIoU1CI2ZySDkYu0vCgJsGvCnrE2HwhruwpYa_FlkVeA0Pz76Rn3IMLmJUpfkP03mmmh-zPUg3qhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی در حاشیهٔ نشست مجمع عمومی سازمان ملل با وزیر خارجهٔ سوئیس دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/148743" target="_blank">📅 16:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148742">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ارزش بازار ارز دیجیتال، از ۳ تریلیون دلار عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/148742" target="_blank">📅 16:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148741">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7frxh0sA91_JDeljGCmQi5Csku7u24bJ-NHGFEIkBH76g9XIUUaybT-7p8S7VGk01-TKg4r-tXJ3YJyWGX0co0ZiByfcCUnt1OcWY1G2LZ1lXuX6Fr_DDOvbAEnfm4SlTOtb2P0lmHzIOrFxe6nr4rQbZgVAPL25YMW3dJpYKqhR0O_U7eaWXOr667GJhBvFP_y3CEnNSrNDoS7pOB37ZznrrlE5IdN7fGaOLdcppKzdAyX0X0LAC_feFgIAd8YHbn2ULALw4miDMRVMzv9HELxrcBBzuuvgRbcI17BgvNod8cobaiUWKGgGT5gZ8nHZ_-nxl3QBWcjdZBIYHwBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استقبال وزیر کشور الجزایر از پزشکیان، در توقفی کوتاه در فرودگاه الجزیره، در مسیر سفر به نیویورک
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/148741" target="_blank">📅 16:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148740">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3MYVAQGVf-Mx3XqGv-0dxKLxK3Hza1UmHtkk8Yizqcizos7wiTcfKDTfo9sOSEolGVEp5l-xbguRiuPB9sQil9mQpC2sVtlFXlgiYN5se3GVtg_xzDkCwkgCLmMAeJDMSinTkieVu1CiD9mW64LgAh0uQIBwG5LU942EbAd66hpRFQBldZEyJcrXxmIzrdULPZHwfM069TJExAMb51mLEgK6IwBE669fL-Mbl1i55SZW2zX8YFExikbvVudWGp8fIVsLNocEG2VxKIu7HLrk_xNSvNM0mnTc78EWIhQJSBKtUS0umIdCVNkm0p1V61BoCI2HNPARZ6NLulNhnGbuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای A330 MRTT متعلق به نیروی هوایی عربستان سعودی از پایگاه هوایی ملک عبدالله در شهر جده برخاست و به سمت جنوب و کشور یمن در حرکت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/148740" target="_blank">📅 15:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148739">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
دولت اسرائیل قرار است طرح فراخوان و بسیج حداکثر ۲۰۰ هزار نیروی ذخیره برای یک دوره دیگر از خدمت در ارتش اسرائیل (IDF) را تصویب کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/148739" target="_blank">📅 15:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148738">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idD7SzBzEIjHHJcwUJMjoQHlOWgaxS_rYZlR__IJII28TiQ7UDYli_F8YrmpBLsZXuea7Kc8_tiDrqKG3BvFMnezh4x1ONN4bISbCV4OLZXl2K9hdpFRi30f-5nKgBXxdsTtoLifZn25EnNfn_ZYocdlh027u256NprYL6ZywbvnigQKnNsMBTkP3uXfp2VI6fdhaYtKLdfI7mCuDd-2vpTSn2mg3wjet9aum_6VTsNZ8h2LQR7J9Cgn0Z3fvM8X0POCl7O6SaqBoCyC2flCxr9No7vcln1cK2drqBuvs7X9ZGLitLU64lbdDeN62Gwn4JbLbCM9hmEyu-Ic-rD7lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نامه‌ای از وزارت خارجه آمریکا به تاریخ ۱۸ سپتامبر نشان می‌دهد که سرویس امنیت دیپلماتیک آمریکا (DSS) در جریان سفر عباس عراقچی، وزیر امور خارجه ایران به آمریکا برای شرکت در هشتاد و یکمین مجمع عمومی سازمان ملل، برای او تیم حفاظتی اختصاص خواهد داد.
🔴
در این نامه آمده است که یک «ارزیابی کامل» از تهدیدهای احتمالی علیه عراقچی در خاک آمریکا انجام شده و ترتیبات حفاظتی نیز با نمایندگی ایران هماهنگ خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/148738" target="_blank">📅 15:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148737">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
بلومبرگ: کشورهای عربی حوزه خلیج فارس در دیدار روز سه‌شنبه از ترامپ خواهند خواست از تشدید تنش بیشتر با ایران خودداری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/148737" target="_blank">📅 15:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148736">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d59f3d89.mp4?token=T2zKUoDyZQmvhnJ2mxNktlT9Rx1SOHeTYAf21hT8pLI66Isyelma9r49QGfEAgcR1ymoV49-Dz1KIdhN_AJqCX93aqgJxnt9dILVWg_RSY92tnva-125JlQcViRPHoAeu9GPW7qZsII5OPivxgyOspdev60OmbfuZyMqOflmEWzeiNJwMrZpL4pNsWx47ZGPsqkKy_z7H1x1_GhqmVEacmKM9JA4X9AV6-ceuONAwbYUxrVSmUdLgeyOB21QQPP1ukClyAL-6aXdiscbIxcwQc5VGYJPPB4VhcZO9AFttROglE-N40Vq_JVhPIbzhxZy_HdLSS8gQHw47NsDJekoyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d59f3d89.mp4?token=T2zKUoDyZQmvhnJ2mxNktlT9Rx1SOHeTYAf21hT8pLI66Isyelma9r49QGfEAgcR1ymoV49-Dz1KIdhN_AJqCX93aqgJxnt9dILVWg_RSY92tnva-125JlQcViRPHoAeu9GPW7qZsII5OPivxgyOspdev60OmbfuZyMqOflmEWzeiNJwMrZpL4pNsWx47ZGPsqkKy_z7H1x1_GhqmVEacmKM9JA4X9AV6-ceuONAwbYUxrVSmUdLgeyOB21QQPP1ukClyAL-6aXdiscbIxcwQc5VGYJPPB4VhcZO9AFttROglE-N40Vq_JVhPIbzhxZy_HdLSS8gQHw47NsDJekoyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه آمریکا، درباره ناتو: «اگر در شرایط اضطراری نتوانیم از پایگاه خود استفاده کنیم، صادقانه بگویم، پس اساساً داشتن این ائتلاف چه فایده‌ای دارد؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/148736" target="_blank">📅 15:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148735">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/759912fdab.mp4?token=VZcJ901JeNpLbYjn0P0aabgB7t91RDwLRXbFwHII8O2Frq1peMgMZIZ5lmij3H55tyJqU322aiT8pHW7q3QFpXK3-8mjLqKnIakFm0nzJna1cttxafloBRldebJXAaRTr7onjnJu8xssEkibyQPLoo4YilA2zUslErVoX_w_j1V8nasks1w3acJf35A5TtAdhFOHitgmYDkKPbgaAM41qcJQyCEf669EjmGaWi2823eAVS0BJnDahGvVDy1z7Ud44YNX__CimWV1_CpGLLcjCvTVGOkUAecmvuSVRvJfkA9E2Kuy_W0wxqZyD7MYR2VZEI9kusck40XQ56UqXbJJmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/759912fdab.mp4?token=VZcJ901JeNpLbYjn0P0aabgB7t91RDwLRXbFwHII8O2Frq1peMgMZIZ5lmij3H55tyJqU322aiT8pHW7q3QFpXK3-8mjLqKnIakFm0nzJna1cttxafloBRldebJXAaRTr7onjnJu8xssEkibyQPLoo4YilA2zUslErVoX_w_j1V8nasks1w3acJf35A5TtAdhFOHitgmYDkKPbgaAM41qcJQyCEf669EjmGaWi2823eAVS0BJnDahGvVDy1z7Ud44YNX__CimWV1_CpGLLcjCvTVGOkUAecmvuSVRvJfkA9E2Kuy_W0wxqZyD7MYR2VZEI9kusck40XQ56UqXbJJmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه آمریکا، درباره گرینلند:
«
چندین رئیس‌جمهور آمریکا
اهمیت جغرافیایی گرینلند را درک کرده بودند. اما
ترامپ نخستین رئیس‌جمهوری است که واقعاً برای آن اقدامی انجام داده است.
»
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/148735" target="_blank">📅 15:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148734">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8d10b7d9.mp4?token=L1jpD8UmQGRfPOXlYZQEYJWWWMsaGi6SfoHBSxm0VppzIrnlBDNAcy36JtUIW30oYrYN5euP-To5f_L8GKjDT021UnHW7pA3UkrHF0Ax8SR3-Bo-bl2pCtUXY756W4oHPoiFz-Z0HkOzXT5sBi_ZJXKNXlFkPOJRadKosgRLdR-aFLnbvtrnkMgf31oUhSnrdlTOUHR9ZEkVRroqAljhGCo-6cC70D-CkVT24e_QOvuQZtM0t_tA5vxpYBWqBU1qV9hypES0UNp0z_CVmtTgwULyYRy_UTkxrJf37J357kq08G2smmIuVgmm8VbhNBJldRbP6KT0G-0UXGXum5ITAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8d10b7d9.mp4?token=L1jpD8UmQGRfPOXlYZQEYJWWWMsaGi6SfoHBSxm0VppzIrnlBDNAcy36JtUIW30oYrYN5euP-To5f_L8GKjDT021UnHW7pA3UkrHF0Ax8SR3-Bo-bl2pCtUXY756W4oHPoiFz-Z0HkOzXT5sBi_ZJXKNXlFkPOJRadKosgRLdR-aFLnbvtrnkMgf31oUhSnrdlTOUHR9ZEkVRroqAljhGCo-6cC70D-CkVT24e_QOvuQZtM0t_tA5vxpYBWqBU1qV9hypES0UNp0z_CVmtTgwULyYRy_UTkxrJf37J357kq08G2smmIuVgmm8VbhNBJldRbP6KT0G-0UXGXum5ITAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه آمریکا، اکنون می‌گوید
کتائب حزب‌الله عراق
مسئول حملات پهپادی اوایل ماه جاری به خط لوله شرق-غرب عربستان سعودی بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/148734" target="_blank">📅 15:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148733">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2c33e10f9.mp4?token=YlG_YCf50vaIGqrzTfkklaDIB47NojQU1ZtKToQr4RcY1oQPKxpu8ikmV5jhXMdBDSiQmZFiWJABTf2Xn9GyXHpyq0O9FewTynmhX--kLd1iPVDEsTBcxglHaB0rKROvNaalcg3Y1Sa_rSLbJ1nDLkdmXSllOP3rAiyf919iiy6b_R5J9QUJAFtvvOCu_-LT49Iwgi2n9I1gYNmXPUE5-CHuRA3pj7qqiCtvrnFF6_Aq3touy7Hwr6JwdDLSfsowf2ngiz7o8DR8HQ3FkswRvzMbCRyLnEbwNoiw2sIyCC8hLwDhhXn1BIRPWcq9nJ_vihaWZY6_RVM7zh8iwCxVEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2c33e10f9.mp4?token=YlG_YCf50vaIGqrzTfkklaDIB47NojQU1ZtKToQr4RcY1oQPKxpu8ikmV5jhXMdBDSiQmZFiWJABTf2Xn9GyXHpyq0O9FewTynmhX--kLd1iPVDEsTBcxglHaB0rKROvNaalcg3Y1Sa_rSLbJ1nDLkdmXSllOP3rAiyf919iiy6b_R5J9QUJAFtvvOCu_-LT49Iwgi2n9I1gYNmXPUE5-CHuRA3pj7qqiCtvrnFF6_Aq3touy7Hwr6JwdDLSfsowf2ngiz7o8DR8HQ3FkswRvzMbCRyLnEbwNoiw2sIyCC8hLwDhhXn1BIRPWcq9nJ_vihaWZY6_RVM7zh8iwCxVEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره اوکراین
:
فکر می‌کنیم آتش‌بس در حوزه زیرساخت‌های انرژی ایده بسیار خوبی است؛ به‌طوری که زیرساخت‌های اوکراین هدف قرار نگیرند و در مقابل، تأسیسات و منابع انرژی روسیه نیز مورد حمله قرار نگیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/148733" target="_blank">📅 15:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148732">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78825914c9.mp4?token=uYvEkbOYBrp5vfd5apS9j6TAcSuphHi_j4I9gMYxgKPdIersazxFtxYgxrTr-CB9ES-G3ey-_23RL0G8qpstCy4aQ-FK2NsJDV8OaNjL0_jUnrqNUoPVfpE5La7sx3jxlkS0YQm50axENGjjRkSmeVBkNoRVcp1sNMYKsPshCiIy4KfQWZvyJR5M7eGkoJ3qN-rmZyAAE8bVnmgxYM7TwQGdNy2eZlx3JAOSy82gDeK42OrkuAZL-GRjWeiWesSmAfJ57bBKHs3awJFBHC02Ekd5gmvp2LxClV9qRp-Vtubbkpt_zgsHoVc7tuLiBBXomXwKwJmbRQn0FB5OA8bTcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78825914c9.mp4?token=uYvEkbOYBrp5vfd5apS9j6TAcSuphHi_j4I9gMYxgKPdIersazxFtxYgxrTr-CB9ES-G3ey-_23RL0G8qpstCy4aQ-FK2NsJDV8OaNjL0_jUnrqNUoPVfpE5La7sx3jxlkS0YQm50axENGjjRkSmeVBkNoRVcp1sNMYKsPshCiIy4KfQWZvyJR5M7eGkoJ3qN-rmZyAAE8bVnmgxYM7TwQGdNy2eZlx3JAOSy82gDeK42OrkuAZL-GRjWeiWesSmAfJ57bBKHs3awJFBHC02Ekd5gmvp2LxClV9qRp-Vtubbkpt_zgsHoVc7tuLiBBXomXwKwJmbRQn0FB5OA8bTcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره اوکراین
:
در چند ماه گذشته، در چند مورد کشتی‌های مرتبط با آمریکا هدف حملات اوکراین قرار گرفته‌اند؛ احتمالاً این حملات عمدی نبوده، اما به هر حال این کشتی‌ها هدف قرار گرفته‌اند.
🔴
نمی‌توانیم اجازه دهیم چنین اتفاقی ادامه پیدا کند و این مسئله باید حل شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/148732" target="_blank">📅 15:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148731">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fd254ba0c.mp4?token=XToTl5sFeegqt_YnSRUeC4vG3TBTd1Bh7CxuEFP_CwgqW4VbEI10Xr6SWJjfT6YA_R7IZ-RxTDX9RlwrxwAOYZVgdi_AUQn6P0V4aqy2om5_KUt9kqWZtzqzBnGdZZ1IpgkSWQPC7f0wEgIWJ82Nic3SON8jMAuL0SKm55bhvY-4JfNC0KFHJZwNbE7BvtgVEIjY9UPxq0iampreSQUeWVMbtaDkUTLsRxip1OUZOUpaBzPbjIeNHjm8_pI2J-FwZIs0dxrwddExCHyQtZKG4PQmJew8kznoGFirefptieHMF1bbZODE43HAYbRmH7j6Vaka3O6uzn7d8VhnpOWfWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fd254ba0c.mp4?token=XToTl5sFeegqt_YnSRUeC4vG3TBTd1Bh7CxuEFP_CwgqW4VbEI10Xr6SWJjfT6YA_R7IZ-RxTDX9RlwrxwAOYZVgdi_AUQn6P0V4aqy2om5_KUt9kqWZtzqzBnGdZZ1IpgkSWQPC7f0wEgIWJ82Nic3SON8jMAuL0SKm55bhvY-4JfNC0KFHJZwNbE7BvtgVEIjY9UPxq0iampreSQUeWVMbtaDkUTLsRxip1OUZOUpaBzPbjIeNHjm8_pI2J-FwZIs0dxrwddExCHyQtZKG4PQmJew8kznoGFirefptieHMF1bbZODE43HAYbRmH7j6Vaka3O6uzn7d8VhnpOWfWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره ایران
:
دولت بایدن به‌شدت به‌دنبال توافق با ایران بود و چهار سال تلاش کرد با امتیاز دادن به ایران به توافق برسد، اما در نهایت نتوانست به هیچ توافقی دست پیدا کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/148731" target="_blank">📅 15:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148730">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e1ebf6542.mp4?token=fgBykVyqsYvJ-IT6mSnopWSazlLemT52yPhc5g3YP4z3J13cziCHapDBy6PRLdF6ngrtndKD6Ewcni6x5ucwEAnqLEjGyX52BrgAMlWX3u1QXlS-dZpHvl8cBSm7r8ZueHd5efKiUdx3NwjE7zcViYUS44Vk0IIrmvcklzUhi19PZLdqVjWfXIQJd3SXocdF8_tD6FJC6Zv_FNcOrKWEVXLLfsex5veD15ZUCl1GDd11HeowOrkbdhhjX0tD2vuC5ukuxz2_HQuQc0uVy0W8e8zHRWZp0YC0R4DNCBvapKjTAT_mmLl4oRabJWwKRM4z6e89cvOzYtOu2VMc8p-YVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e1ebf6542.mp4?token=fgBykVyqsYvJ-IT6mSnopWSazlLemT52yPhc5g3YP4z3J13cziCHapDBy6PRLdF6ngrtndKD6Ewcni6x5ucwEAnqLEjGyX52BrgAMlWX3u1QXlS-dZpHvl8cBSm7r8ZueHd5efKiUdx3NwjE7zcViYUS44Vk0IIrmvcklzUhi19PZLdqVjWfXIQJd3SXocdF8_tD6FJC6Zv_FNcOrKWEVXLLfsex5veD15ZUCl1GDd11HeowOrkbdhhjX0tD2vuC5ukuxz2_HQuQc0uVy0W8e8zHRWZp0YC0R4DNCBvapKjTAT_mmLl4oRabJWwKRM4z6e89cvOzYtOu2VMc8p-YVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه آمریکا، درباره ایران: «در حال حاضر حدود ۶۰ تا ۷۰ درصد از جریان نفتی که پیش از این از تنگه هرمز عبور می‌کرد، دوباره در حال عبور است و این میزان رو به افزایش است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/148730" target="_blank">📅 15:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148729">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bb79220ba.mp4?token=D-QbHzYQw3T91g1wXB741Z9FmHcTVD2MRMlFxLqKeGyYRdKOmKjZv3k1yXykCcKga3SGND9ru_JIIBfe4uBM6lf2xE9efQO4hb1j-ivdk6N-lhzSrYWJRt9ghxhQt7NpKEIiAtNsW0Cwyo6Asg1hOWfn5-1OyjL0f4RYHyTCDe-UzFbfbpnqfiGg3WfnUKNnNFbhUMPMX8GkwaJjSiU1Hv9ZUnAWRR054h3aJO6mavkBBV-WGtaiGfRcfLdSS6gk--rzJe7I0846rjTyF5SwWUVirgWkr2o7pTZMHSReGnOcV3XxPdHJcPMvJOl0tG5WqSPWW_JjyaZ3gl4sKZHVww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bb79220ba.mp4?token=D-QbHzYQw3T91g1wXB741Z9FmHcTVD2MRMlFxLqKeGyYRdKOmKjZv3k1yXykCcKga3SGND9ru_JIIBfe4uBM6lf2xE9efQO4hb1j-ivdk6N-lhzSrYWJRt9ghxhQt7NpKEIiAtNsW0Cwyo6Asg1hOWfn5-1OyjL0f4RYHyTCDe-UzFbfbpnqfiGg3WfnUKNnNFbhUMPMX8GkwaJjSiU1Hv9ZUnAWRR054h3aJO6mavkBBV-WGtaiGfRcfLdSS6gk--rzJe7I0846rjTyF5SwWUVirgWkr2o7pTZMHSReGnOcV3XxPdHJcPMvJOl0tG5WqSPWW_JjyaZ3gl4sKZHVww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه آمریکا، درباره ایران: «تصور کنید کره شمالی در خاورمیانه وجود داشته باشد. این وضعیت برای جهان فاجعه‌بار خواهد بود.
🔴
در آن صورت، دیگر برای گازوئیل ۶ دلار یا هر قیمتی که امروز دارد پرداخت نمی‌کردید؛ بلکه باید سه برابر این مبلغ را می‌پرداختید.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/148729" target="_blank">📅 15:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148728">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70ab0515ff.mp4?token=qqh25qiID7IyHJPWMRCJVMw0bfEgZcqE44QwOQJowZGd6fjNpPQTVEtbwqACrSbO7iKmyweO-AetXPZXuRQupJJGSPGlrdYBf8B_x7VLSXF7KM06eAkvrCDfvIxAePoC0l82XYmkemQDVhgFtGxr8Py3Gt7hK_mJb_lbCTwHVKmOCZJaUB1ZPEfERxCGtarANWtz3F0iNuClnybSOO2AA4NR0e1I7dspQxNI_Km0WQV99nfa27p1I2szDhpHdYJA50Zx9x-zzUQdPz1LvQBBxogNh4WvB6pAUZssnGuWqRxqtNexAqyRtxC7nm11-9fVPtmMLNINfxm-dVP_rCFWSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70ab0515ff.mp4?token=qqh25qiID7IyHJPWMRCJVMw0bfEgZcqE44QwOQJowZGd6fjNpPQTVEtbwqACrSbO7iKmyweO-AetXPZXuRQupJJGSPGlrdYBf8B_x7VLSXF7KM06eAkvrCDfvIxAePoC0l82XYmkemQDVhgFtGxr8Py3Gt7hK_mJb_lbCTwHVKmOCZJaUB1ZPEfERxCGtarANWtz3F0iNuClnybSOO2AA4NR0e1I7dspQxNI_Km0WQV99nfa27p1I2szDhpHdYJA50Zx9x-zzUQdPz1LvQBBxogNh4WvB6pAUZssnGuWqRxqtNexAqyRtxC7nm11-9fVPtmMLNINfxm-dVP_rCFWSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه آمریکا، درباره ایران: «مسئله اصلی اینجاست که ایران توسط روحانیونی اداره می‌شود که دیدگاهی بسیار افراطی نسبت به دین خود دارند و نگاهی آخرالزمانی به آن دارند.
🔴
این افراد هرگز نباید به سلاح هسته‌ای دست پیدا کنند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/148728" target="_blank">📅 15:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148727">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
شبکه سی‌ان‌ان: هرمز بحرانی بزرگ‌تر از کرونا است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/148727" target="_blank">📅 15:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148726">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
فارس: منابع داخلی گزارش‌های مربوط به توافق‌های مربوط به بازگشایی تنگه هرمز را رد کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/148726" target="_blank">📅 14:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148725">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrVIVlsRXsfqHj_35NPaPndFB5-Uqsh5MwbxzMGCdouhKCFCXja_X-nxplH5qm63-6n_vPd2vIHpNknVA5HSyPf1V3IV5a2-l438fMeKgojfoMB9hWESK6LRNVl6205khjaGo0QXQdnbEwppETC5US6v6w9YvDAdsbM3Z9Utl4-ETDniC5OG2-JxYa1VX1S2VqvJQ4aKWpBAP7_9GnQ9DJG82X7Fs6auArO4KORbnxArT8m1ulKiLo3UXC5FBfVrclv7Wf_umf7EUwQCjxfp5hdlr-UEpAvfauinfaohB1Hm_Gpif790C44JzABzmAYnH0pAoFRlMUIKFDteH7fUSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : ترسوها و خائنان دوست دارند بگویند که ایالات متحده کمبود مهمات دارد. این درست نیست.
🔴
ما مهمات بیشتری داریم تا اینکه بتوانیم حتی تصور کنیم که از آن‌ها استفاده کنیم، و در حال حاضر آن‌ها را در سطوحی تولید می‌کنیم که قبلاً هرگز شاهد آن نبوده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/148725" target="_blank">📅 14:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148724">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوری / روبیو: برای دیدار با هیئت ایرانی در سازمان ملل آمادگی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/148724" target="_blank">📅 14:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148723">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فوری / روبیو: برای دیدار با هیئت ایرانی در سازمان ملل آمادگی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/148723" target="_blank">📅 14:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148722">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سی‌ان‌ان: گزارش‌ها حاکی از آن است که قطعات حساس جنگنده F-35 که از استرالیا به آمریکا ارسال شده بودند، پس از آنکه پرواز حامل این تجهیزات به هنگ‌کنگ تغییر مسیر داد، مفقود شده‌اند.
🔴
گفته می‌شود این قطعات شامل کانوپی (سایبان کابین) یک فروند F-35 نیز بوده که حاوی فناوری‌هایی با دسترسی محدود به آمریکا و متحدانش است.
🔴
جزئیات مربوط به تغییر مسیر پرواز و ناپدید شدن قطعات همچنان مشخص نیست و این حادثه نگرانی‌هایی را درباره امنیت فناوری‌های حساس F-35 ایجاد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/148722" target="_blank">📅 14:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148721">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
رسانه‌های جنگی یمن:منتظر تصاویر تکمیلی از عملیات نظامی "به نام خدا، ما قدرتمندتر و انتقام‌جوتر هستیم" در ساعت چهار بعد از ظهر باشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/148721" target="_blank">📅 14:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148720">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
کرملین: «ولادیمیر پوتین همواره گفته است که روسیه از صلحی پایدار حمایت می‌کند، نه آتش‌بسی که در عمل هیچ نتیجه‌ای به همراه نداشته باشد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/148720" target="_blank">📅 14:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148719">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سخنگوی سپاه: اگر آمریکا به کوه کلنگ یا هر مکانی حمله کند، مقابل آن می‌ایستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148719" target="_blank">📅 14:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148718">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری / شرکت‌های هواپیمایی اسرائیل به دستور شاباک (Shin Bet)، تمامی پروازهای خود به دبی را لغو کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148718" target="_blank">📅 14:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148717">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
شنیده شدن صدای چند انفجار در تعز و صعده یمن در پی حملات عربستان سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/148717" target="_blank">📅 14:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148716">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
مجله «مانثلی چوسان» کره جنوبی: دو عضو هیئت کره شمالی در بازی‌های آسیایی آیچی-ناگویا در ژاپن، برای دریافت پناهندگی اقدام کرده‌اند.
🔴
این دو نفر بخشی از هیئت ۱۸۰ نفره کره شمالی در این بازی‌ها بوده‌اند و طبق گزارش‌ها، ترجیح می‌دهند به جای کره جنوبی، در ژاپن درخواست پناهندگی کنند.
🔴
هویت و سمت آنها اعلام نشده و هنوز مشخص نیست که در نهایت از کره شمالی جدا خواهند شد یا خیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148716" target="_blank">📅 14:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148715">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وزیر نفت عراق: بخش عمده‌ای از نفت‌کش‌هایی که از تنگه هرمز عبور می‌کنند، عراقی هستند
🔴
ما موفق شدیم در یک رکورد کم‌سابقه، حجم صادرات نفت خود را به ۴ میلیون بشکه در طول یک روز برسانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148715" target="_blank">📅 13:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148714">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
قیمت نفت برنت امروز هم دچار کاهش شده و به دلار ۹۷ رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148714" target="_blank">📅 13:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148713">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/028a71ad71.mp4?token=v5im5Xhp2T3smq5B0XQ6QQh3t21k-e-slBQs-rmJ6jnIj-DcHExEI0YuRoyoChMEwhRxkUEBCByweemAPgTxG2Gpz_3ws3Nm57Nxu4ZcsMUdgbQ_TarVMhuYrNLLhfasv1OecriJmzwwnQBV1F7YKocS_w85dQpyQEssEVmulRxKFVtpIZu2jPYRuCitNF9E8TzG1OEVZ34y8EpQ4GNbhrV2RGyr1CSaDb5zUEdieFovdxBGD8LJgdT22m0Ru7bPvj1RbsyLS_GlZFuHdUibradOdlKaEtHDUitMYNgds7dItBLC24P-Nz1Ss9wl1N6W2OAC5H6m12eP0oXRIQZNFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/028a71ad71.mp4?token=v5im5Xhp2T3smq5B0XQ6QQh3t21k-e-slBQs-rmJ6jnIj-DcHExEI0YuRoyoChMEwhRxkUEBCByweemAPgTxG2Gpz_3ws3Nm57Nxu4ZcsMUdgbQ_TarVMhuYrNLLhfasv1OecriJmzwwnQBV1F7YKocS_w85dQpyQEssEVmulRxKFVtpIZu2jPYRuCitNF9E8TzG1OEVZ34y8EpQ4GNbhrV2RGyr1CSaDb5zUEdieFovdxBGD8LJgdT22m0Ru7bPvj1RbsyLS_GlZFuHdUibradOdlKaEtHDUitMYNgds7dItBLC24P-Nz1Ss9wl1N6W2OAC5H6m12eP0oXRIQZNFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پروازهای مکرر و گسترده هواپیماهای جنگی سعودی بر فراز شهر طائف
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148713" target="_blank">📅 13:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148712">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری / عربستان سعودی فعالیت خط لوله نفت شرق-غرب را از سر گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148712" target="_blank">📅 13:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148711">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8adae7aeaa.mp4?token=LJdvT-868C9BcLcQV7aBCD68KS18O2egs2PWyV6dtQeiOgXrf4nGTWP1BNrsKAe3HrkkaLsa5ntPjGY-43tYQJDxV64whzCj8d1Tb4Yb_8TlDH0_tbsR10jxDaeXXCI20aWw-X5uUKvjAPMPWWsO6gOP3FxuYaLHXX2Pb4swlmTgwOmlaGjmxc-QbovnP3Zjx1DaQ5Ec4TkWJRXSHHzCfcOJxFaUPP5ci2K9Lqh148MSBIQOq2A88hFShyoKitDtM-WP_b56vvazkEo8T_-F4mdyPEvCp82ybLgbANRW6CFslWyBwpqlw5uByga1-IKnC4T1UEpY_YGQfToyY-FH7zN1gg1GL5h2B_Ig6-gJiRduQcW8sQzZkwY19WXYVG3amAkIv92z9nrcyEU4Pxb6f2AUNgPht8PWQrOmBnDtyMplKx3V1gmjhTOqsDfjgVB-jCzrv8HmoeVTCP0fphGaJoAwaY2QDVSx7KL8Pt_hpHzcvqz1ibczUF-ZRN09_79oAUxD8rlVlcmIMFlCCdhPMvRdN5t7M4i6E7yoDqykQNOjSXwz4CikZ9jdIXtYsdO4XYGDtfImR8yK8X0F3btxqyz0Eki0FEGru5vvRazRSTRqd8HMz8U_0uRUNQ-ggHujjuSAwXKPUlAMIxEdMEeH_AB-ILy0F6tTlciks3_157U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8adae7aeaa.mp4?token=LJdvT-868C9BcLcQV7aBCD68KS18O2egs2PWyV6dtQeiOgXrf4nGTWP1BNrsKAe3HrkkaLsa5ntPjGY-43tYQJDxV64whzCj8d1Tb4Yb_8TlDH0_tbsR10jxDaeXXCI20aWw-X5uUKvjAPMPWWsO6gOP3FxuYaLHXX2Pb4swlmTgwOmlaGjmxc-QbovnP3Zjx1DaQ5Ec4TkWJRXSHHzCfcOJxFaUPP5ci2K9Lqh148MSBIQOq2A88hFShyoKitDtM-WP_b56vvazkEo8T_-F4mdyPEvCp82ybLgbANRW6CFslWyBwpqlw5uByga1-IKnC4T1UEpY_YGQfToyY-FH7zN1gg1GL5h2B_Ig6-gJiRduQcW8sQzZkwY19WXYVG3amAkIv92z9nrcyEU4Pxb6f2AUNgPht8PWQrOmBnDtyMplKx3V1gmjhTOqsDfjgVB-jCzrv8HmoeVTCP0fphGaJoAwaY2QDVSx7KL8Pt_hpHzcvqz1ibczUF-ZRN09_79oAUxD8rlVlcmIMFlCCdhPMvRdN5t7M4i6E7yoDqykQNOjSXwz4CikZ9jdIXtYsdO4XYGDtfImR8yK8X0F3btxqyz0Eki0FEGru5vvRazRSTRqd8HMz8U_0uRUNQ-ggHujjuSAwXKPUlAMIxEdMEeH_AB-ILy0F6tTlciks3_157U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوشحالی جانفداها از گرانی‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148711" target="_blank">📅 13:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148710">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ایران‌ایر: هیچ ابلاغیه رسمی برای توقف پروازهای استانبول، باکو و نجف دریافت نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148710" target="_blank">📅 13:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148709">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
رویترز به نقل از مقام ایرانی: هیئت ایرانی حاضر در نیویورک، اختیارات کامل برای از سرگیری روابط دیپلماتیک با ایالات متحده را دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/148709" target="_blank">📅 13:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148708">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری / عربستان سعودی فعالیت خط لوله نفت شرق-غرب را از سر گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/148708" target="_blank">📅 13:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148707">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
روانبخش، نماینده مجلس: ما در جنگ با آمریکا هستیم، ممکنه پزشکیان رو تو نیویورک دستگیر کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148707" target="_blank">📅 13:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148706">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
الجزیره:ایران آماده هست که تنگه هرمز رو در عرض ۷ روز باز کنه اگه فشار نظامی آمریکا و متحدانش کم بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148706" target="_blank">📅 13:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148705">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
الجزیره:ایران آماده هست که تنگه هرمز رو در عرض ۷ روز باز کنه اگه فشار نظامی آمریکا و متحدانش کم بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148705" target="_blank">📅 13:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148704">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رویترز: چین میخواد در ازای توقف فروش سلاح آمریکا به تایوان برای فشار بر ایران کمک کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148704" target="_blank">📅 13:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148703">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
خبرگزاری ژاپنی کیودو به نقل از یک مقام ایرانی: ایران اعلام کرد در صورت اقدام آمریکا برای کاهش فشار نظامی، تنگه هرمز را ظرف ۷ روز باز می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148703" target="_blank">📅 13:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148702">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148702" target="_blank">📅 13:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148701">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">در روستایی کوچک، کدخدایی زندگی می‌کرد که بیشتر مردم از رفتار و تصمیم‌هایش ناراضی بودند. او مردی لجباز بود و اگر از کسی کینه‌ای به دل می‌گرفت، حتی به قیمت ضرر مردم هم کوتاه نمی‌آمد.
روزی یکی از اهالی پیشنهاد کرد برای نجات زمین‌های روستا، مسیر آب را تغییر دهند. کدخدا فقط به خاطر اختلاف قدیمی با او، پیشنهادش را رد کرد.
چند ماه بعد، خشکسالی آمد. زمین‌ها خشک شدند، دام‌ها از بین رفتند و خانواده‌های زیادی مجبور شدند روستا را ترک کنند.
مردم می‌گفتند: «خشکسالی بلای روستا بود، اما کینه‌ی کدخدا آن را به فاجعه تبدیل کرد.»
کدخدا سال‌ها بعد فهمید که گاهی یک آدم، وقتی قدرتش را با کینه و لجاجت همراه کند، می‌تواند تاوان اشتباهاتش را به جای خودش، از مردم بگیرد.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148701" target="_blank">📅 13:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148700">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
منابع ایتایی: تا ته تو ماتحت دو کشور کمونیست کافر چین و روسیه فرو رفتیم و دمشون گرم و عالیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148700" target="_blank">📅 13:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148699">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
مجری صداسیما: مردم میگن میدونیم گرونیا بخاطر جنگ و محاصره هست و مقاومت میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148699" target="_blank">📅 12:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148698">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
وال‌استریت ژورنال: عربستان سعودی طی ماه‌ها تلاش کرده بود با تغییر مسیر محموله‌های نفتی، از عبور از تنگه هرمز اجتناب کند؛ اما اکنون ناچار شده است مجدداً محموله‌های نفتی خود را از همین مسیر عبور دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148698" target="_blank">📅 12:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148697">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
رویترز: چین میخواد در ازای توقف فروش سلاح آمریکا به تایوان برای فشار بر ایران کمک کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148697" target="_blank">📅 12:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148696">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
خبر لغو پروازهای ترکیش ایرلاین به ایران تکذیب شد؛ ترکیش ایرلاین ۸ ماه است به ایران پرواز ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148696" target="_blank">📅 12:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148695">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: آمریکا به‌دنبال ایجاد صندوق ۱۰ میلیارد دلاری برای زیرساخت‌های انرژی منطقه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148695" target="_blank">📅 12:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148694">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
زهران ممدانی: ترامپ تنها کسی است که می‌تواند نیویورک را درست کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148694" target="_blank">📅 12:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148693">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12cc58cbb1.mp4?token=iDYE3BI6cL35cV9Z7TP5HNLakRzKV-3qrDRuMVCE_RFnZlJXnxy2FDMYSJCZF4pdbin4ZsjI8xVQl5rijepvN9vVFx7SgmUb-h2R1W2kSBbINtJtwAMVTjtK9OPIUK42vakxjGI3sAGY08m_EQIkN-I_21_b_EfRjg22M1djBhj5A8rv6r8xpyfgajOgFcRM0VsEM-LyIuyKwD9gq8X5-86kUTSFcs2DXAgAp9x1y5rcGmFUxW9jHyS34ovFQSQS_lqXdIb5CDoPE5JfjGwq6a_MPpkm5o5wGxYZ8oNVy659dRPN0PxK5VHustEpKZ5nGt7a-fhCiBWABiVuomZmVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12cc58cbb1.mp4?token=iDYE3BI6cL35cV9Z7TP5HNLakRzKV-3qrDRuMVCE_RFnZlJXnxy2FDMYSJCZF4pdbin4ZsjI8xVQl5rijepvN9vVFx7SgmUb-h2R1W2kSBbINtJtwAMVTjtK9OPIUK42vakxjGI3sAGY08m_EQIkN-I_21_b_EfRjg22M1djBhj5A8rv6r8xpyfgajOgFcRM0VsEM-LyIuyKwD9gq8X5-86kUTSFcs2DXAgAp9x1y5rcGmFUxW9jHyS34ovFQSQS_lqXdIb5CDoPE5JfjGwq6a_MPpkm5o5wGxYZ8oNVy659dRPN0PxK5VHustEpKZ5nGt7a-fhCiBWABiVuomZmVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز صبح تو محمدشهر کرج شوهر سابق یه زنه میاد تو مغازه زنه که کافه داشته با کلت به زنه و خودش شلیک میکنه زنه مُرده خودشم
فوت کرده.
✅
@AloNews
|</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/148693" target="_blank">📅 12:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148692">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ec0706b8.mp4?token=AWw-5Ahq6piVhtOkydW0AJCbKLL1nAvt-0467AwVZNPa3FxH28zmJX_YhF_KDWbz-7gY62zhnk1uTeDCAHyK_5aaGr7UtRn9HR4rkj3xSh0NmkLEM0ZX0UAx6nsyP6drI9gySotncmk4DoJoK1JBao3nyZh64eO_EHaMzi4h1wYjLzQ4v89GiQ8BDWMOfmNy0qH9PFuLAdiN-sA8AAIXXK4kx4P6IKXsZ_IJR8q1ougRs65AMehVtPjzjNBL2hkjYq56Oed70wXOuVMMbwEIADKHwsu8XObueurqk2mPwZqsbqN4B40HWV3-xBPIxdlW3gZL_KdObypW5HEMDh-xNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ec0706b8.mp4?token=AWw-5Ahq6piVhtOkydW0AJCbKLL1nAvt-0467AwVZNPa3FxH28zmJX_YhF_KDWbz-7gY62zhnk1uTeDCAHyK_5aaGr7UtRn9HR4rkj3xSh0NmkLEM0ZX0UAx6nsyP6drI9gySotncmk4DoJoK1JBao3nyZh64eO_EHaMzi4h1wYjLzQ4v89GiQ8BDWMOfmNy0qH9PFuLAdiN-sA8AAIXXK4kx4P6IKXsZ_IJR8q1ougRs65AMehVtPjzjNBL2hkjYq56Oed70wXOuVMMbwEIADKHwsu8XObueurqk2mPwZqsbqN4B40HWV3-xBPIxdlW3gZL_KdObypW5HEMDh-xNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو جدید کاوه آهنگر زمان در راه پاسارگاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148692" target="_blank">📅 12:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148691">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
اردوغان خواستار لغو حق وتو در شورای امنیت سازمان ملل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/148691" target="_blank">📅 12:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148690">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
نخست‌وزیر قطر: خاورمیانه به یک «چارچوب امنیتی منطقه‌ای جدید» نیاز دارد که ایران را هم شامل شود
🔴
جنگ ایران باید برای منطقه به منزله یک «زنگ بیدار باش» باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148690" target="_blank">📅 12:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148689">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaXl0t7wXtjei7DVwSJdqddeGc8lriwY8o3GIKQCgrLFd6F_4Zu5hd2dTFV4OsR6Xj6qQo1B8rNCXO21QGi4DsnBfhJ2maQrlRJVLv9iWjGT2nwgxWjVgkv99UwQist7X-3EifbuLUDXqQK2AmATpqKupkS-6F6h1bHpePUl_E_qHDXHP1TRJTOKw20gPkLLZkRJYG7UpgvV7JygWMZJ11R16muQ8gm1TJ_KyzxeOm_IjkaAVa34SFBIP67FyMHe_nPzLCemNCdgHHFsTJSfcV6AJBhKpxMNGfZqY6ftuC3w4_L5O2DTvfE2Xe181hnDytRc1hbBBW1XRZwoCsmerQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صادق زیبا کلام: مشکل ما با تندروهای خودمان است که ۳۶سال همه قدرت را بدست آورده بودند و حالا سرسوزنی حاضر به ازدست دادن آن نیستند ولو به قیمت به خاک سیاه نشستن نود میلیون ایرانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148689" target="_blank">📅 11:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148688">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وزیر نیرو: صنعت برق از نقاط قوت ماست، قطعیا و مشکلات بخاطر جنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148688" target="_blank">📅 11:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148687">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c75ab8b39a.mp4?token=c-rK0keD0KtlKaxACr7hTXUBPhuxFNO0QiKOrfpIMzAYCF8E0Ud3TxmLR7PYboXHLRwyf8u_LgGdyCi0IgQijOCLC64BUuUe291oAeCjw7lBm_N1JrWh8mKu1HITcIFMN0GL0AkyvWYePZXz5l_ssvO2yofuFdSaGWYw0_st8LZ3hAbBJ2xx3GLkcaUxob7y3AUPQHfQbLLlXQQ8-QpEjNYJeAOoU7VuiVQdlxRhWQ3bfuO10R6eJnNrqux_-2W-gY0PfaaX2w_vcfpYe_wGVF37OU55ul1h-xlQgl-R1xczVgs4HOzEUM-V9hF2p6V1m8lQ5UfPz2uJJPcDxiFVhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c75ab8b39a.mp4?token=c-rK0keD0KtlKaxACr7hTXUBPhuxFNO0QiKOrfpIMzAYCF8E0Ud3TxmLR7PYboXHLRwyf8u_LgGdyCi0IgQijOCLC64BUuUe291oAeCjw7lBm_N1JrWh8mKu1HITcIFMN0GL0AkyvWYePZXz5l_ssvO2yofuFdSaGWYw0_st8LZ3hAbBJ2xx3GLkcaUxob7y3AUPQHfQbLLlXQQ8-QpEjNYJeAOoU7VuiVQdlxRhWQ3bfuO10R6eJnNrqux_-2W-gY0PfaaX2w_vcfpYe_wGVF37OU55ul1h-xlQgl-R1xczVgs4HOzEUM-V9hF2p6V1m8lQ5UfPz2uJJPcDxiFVhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرقت موبایل یک پاکبان در مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148687" target="_blank">📅 11:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148685">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8e76cebe8.mp4?token=GDVlJEYJqzMW_PLQjrC-JZnSY3cQjE2TWPZDvk_n8WJt-63lLM08TeH98tWQRwaaLvMU4T20ODcMo-Rszz8phm7xmv6nvag0QOybTbyEnaEtMsTEEcgO2QuYZyrnL5hlBk2-Qm9LJtaHX0sgYWnHcKQRxi_qKEYjonqUgi4gXY-3JMcgCzQ8mrDj5x2eCZO2LjyN7FvcfOrwE-YWxkIrZNzIvEqIZsT5lr3ncknjBw53cQZwDczVgpl_sg7N9w8xDXmX8TX6aDOWdJyFNNR-9G3xAGyVrozZenvJELC7ArkxPtQ9BLAYIf5_agZwMmEME2p_yIURJd4Tbm3y6ij1VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8e76cebe8.mp4?token=GDVlJEYJqzMW_PLQjrC-JZnSY3cQjE2TWPZDvk_n8WJt-63lLM08TeH98tWQRwaaLvMU4T20ODcMo-Rszz8phm7xmv6nvag0QOybTbyEnaEtMsTEEcgO2QuYZyrnL5hlBk2-Qm9LJtaHX0sgYWnHcKQRxi_qKEYjonqUgi4gXY-3JMcgCzQ8mrDj5x2eCZO2LjyN7FvcfOrwE-YWxkIrZNzIvEqIZsT5lr3ncknjBw53cQZwDczVgpl_sg7N9w8xDXmX8TX6aDOWdJyFNNR-9G3xAGyVrozZenvJELC7ArkxPtQ9BLAYIf5_agZwMmEME2p_yIURJd4Tbm3y6ij1VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی پالایشگاه نفتی بزرگ روسیه در حمله پهپادی اوکراین
🔴
رسانه‌های اوکراینی در پی حمله پهپادی اوکراین به روسیه، تصاویر و فیلم‌هایی از پالایشگاه نفتی بزرگ در شهر «سامارا» واقع در جنوب شرقی روسیه منتشر کردند که در آتش می‌سوزد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/148685" target="_blank">📅 11:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148684">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
هم اکنون ، پرواز جنگنده‌ها در آسمان بغداد و چند استان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/148684" target="_blank">📅 11:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148683">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkYpKhy9wm76jHvTpXhkEqYUIXIks0ySkB5NW6JJZKEkiOo1_2wLiTH5QVRhv2i3zeKbqVjF0IAIyTBnwtD2QkFy5I2iyMZDLwcmH-NmyfRtgg-1TujxdMIu_NFdJ3WiCNGIxRfUK8ZbTTQlTMDTfxtCqo4o2e70fkDfs6e4dcRdn0flx-RMJIhluAULt69x2rsrlKTAMaUpUmlIjFLfTVgs75B6Jm2igoQMmyXMlS9nWqovnCuOYCuTK7aoEg8IDmbm1K2f-1yiIeKxPA6JX42um-YjocA86me_ujRePvJ34YSt3_2m2-5KSFVizQyYSjzMAt0CUlKD08kx5dmCRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزرای امور خارجه ترکیه، عربستان سعودی، مصر و پاکستان در نیویورک با یکدیگر دیدار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148683" target="_blank">📅 11:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148682">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
چین: با تحریم‌های آمریکا علیه شرکت‌های هواپیمایی ایران مخالفت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148682" target="_blank">📅 11:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148681">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
عربستان از فعال‌شدن هشدار حملات هوایی در منطقهٔ نجران خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148681" target="_blank">📅 10:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148680">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
عربستان از فعال‌شدن هشدار حملات هوایی در منطقهٔ نجران خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148680" target="_blank">📅 10:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148679">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
عربستان از فعال‌شدن هشدار حملات هوایی در منطقهٔ نجران خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148679" target="_blank">📅 10:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148678">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
پزشکیان: دشمن در تلاش است تا تمام راه‌های هوایی‌ و زمینی را بر ایران ببندد تا ما را مجبور به تسلیم کند ولی نمی‌داند ما تسلیم زورگویی دشمنان نمی‌شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/148678" target="_blank">📅 10:42 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
