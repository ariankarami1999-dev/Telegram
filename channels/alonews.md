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
<img src="https://cdn4.telesco.pe/file/ETp76c6biJqfO4-WKWsg4UcrPlENKBpSujwTBGKHzVoQrvcAYFqozNcLeLmJbkKEnmR60IOEEASsiuCnAc8ZDjCUz8XBbNoY88rNAQi5IQ3HqW_s0sB7BGlMN30ibF5whCieic5sQ8aDmcVeZAi1tmxqb3Jee3199BPGVmFQqpq4YUq8oPU-g7M92ki-cONUWbnE1eZfqIbnXoioNeRH0bVbIlBxglp9RfYoEkx6zVuLD3hWkEIWRw2WLf9FNGhO0kWv0q0arbS6kPyQdOlyrv8RppdGLfCPQLUAvrU7FkHXWzddfodyZl0sR7vHVBHiDilCLabArTzdLU708NqU0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 942K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 22:27:32</div>
<hr>

<div class="tg-post" id="msg-134809">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سخنگوی نیروهای مسلح: امنیت کامل تنگهٔ هرمز هنگامی برقرار می‌شود که آمریکایی‌ها نباشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/alonews/134809" target="_blank">📅 22:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134808">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
صداوسیما: شنیده‌شدن صدای ۳ انفجار در غرب بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/134808" target="_blank">📅 22:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134807">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
وزیر خارجه اردن: هیچ پایگاه آمریکایی در اردن وجود ندارد!
🔴
وزیر امور خارجه اردن مدعی شد: روایت ایران مبنی بر وجود پایگاه‌های نظامی آمریکا در اردن نادرست است.
🔴
هیچ پایگاه آمریکایی در اردن وجود ندارد، فقط سربازان آمریکایی به عنوان بخشی از همکاری نظامی بین ما و واشنگتن حضور دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/134807" target="_blank">📅 22:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134806">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e3f23f983.mp4?token=rkdQLyHJ3cO6OE1zIl-wjR3OFUltZai5TJBnRhRc5E38hgp9grigq0D6Ok130JMl0VxFPK8maLRl2odR5RKfMeNSA-Pffecmz8W15O-psXwwP23KHOKidxaLO-pvwXXlWTBcZ3hEdOc2-1hzIoGAeQpfH9I4GsUZE71DjSoAUGx3JgVL71qqB-uKzHdM6WcYVw3v8Mju6LXbXinXsQKRH-j8FXXID6BdZEy2qUh6-RpJDys99cSp5yEd46DK1ROGPnzBq2HlwrqbQxG0326nOtnGNmncsbW5PlMC1FHetdOvzelHdPX9VtJGsfKqLpKhzrioFJUtFqdwQbfMr3rsYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e3f23f983.mp4?token=rkdQLyHJ3cO6OE1zIl-wjR3OFUltZai5TJBnRhRc5E38hgp9grigq0D6Ok130JMl0VxFPK8maLRl2odR5RKfMeNSA-Pffecmz8W15O-psXwwP23KHOKidxaLO-pvwXXlWTBcZ3hEdOc2-1hzIoGAeQpfH9I4GsUZE71DjSoAUGx3JgVL71qqB-uKzHdM6WcYVw3v8Mju6LXbXinXsQKRH-j8FXXID6BdZEy2qUh6-RpJDys99cSp5yEd46DK1ROGPnzBq2HlwrqbQxG0326nOtnGNmncsbW5PlMC1FHetdOvzelHdPX9VtJGsfKqLpKhzrioFJUtFqdwQbfMr3rsYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فیلد مارشال محسن رضایی: مسیری که در ذهن آقامجتبی هست، بهتر از مسیری بود که شورای‌عالی امنیت‌ملی رفت.
🔴
مجری: چه مسیری بود؟
🐸
محسن رضایی: نمی‌دونم
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/134806" target="_blank">📅 22:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134805">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
گزارش انفجار در چابهار و کنارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/134805" target="_blank">📅 22:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134804">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpR1RN2CKX1QyK8GAzazDpF4JT692xO06Xd4y4BMdwOks25MstwCUn2QFaClTqbE6errP-Im6iNzjOd4xF6UEFbrrQS6ZtzTKXRDtPYWBqHPjh-2af1-EmJRJ6EllZ6a6H2rknA_q-bFu18Tw5ddPC1EXnFJ1rumR6e7onElqugA0Poz6PpWgRp_wr5B3gOgM2nhbWh71-Z97td2V5VeKy-l0AHup5Onk4Z72hByK5uZ2q02dpgm54cUvB32DM_sYPdVO4dmU6203Tqi3DdKfyKnCMAydUniraOF_oFEn6y4_0C96m4tNI4v3SJiOeJGlhZfO7BFRyBv9zFfT2HxLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: موج جدیدی از حملات علیه ایران آغاز شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/134804" target="_blank">📅 22:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134803">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
اکنون کل ارتش و سپاه در نیمه جنوبی ایران تحت بمباران هوایی آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/134803" target="_blank">📅 22:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134802">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
قشم صدای ۲ انفجار به گوش رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/134802" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134801">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
انفجار های متعدد در بندر عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/134801" target="_blank">📅 21:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134800">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
کارولین لیویت، سخنگوی کاخ سفید:
در حال حاضر دونالد ترامپ و جی‌دی ونس در مورد ایران دقیقاً بر سر یک صفحه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/134800" target="_blank">📅 21:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134799">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
انفجار های متعدد در بندر عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/134799" target="_blank">📅 21:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134798">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/134798" target="_blank">📅 21:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134797">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سخنگوی کاخ سفید، در مورد اظهارات جی‌دی ونس، معاون رئیس‌جمهور، درباره اسرائیل: ترامپ قطعاً موافق است که بله، کشورهای خارجی قطعاً سعی می‌کنند افکار عمومی آمریکایی را متقاعد کنند.
🔴
در این مورد هیچ شک و شبهه‌ای وجود ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/134797" target="_blank">📅 21:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134796">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
سخنگوی کاخ سفید:  ما مردم مهربانی هستیم و بهترین کشور جهان را داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/134796" target="_blank">📅 21:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134795">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a427bd448f.mp4?token=LhKeuherjIsNPyo2R0lJlN8xUmm3d3aJpaO8AKrc0KsgcxDHabsU_xfuXvZt1L3eHWUyZseTvwYyAbMKrxjyqtDLbso9N4iiu1pCruOqqY80H2rpVuufu5OyRA9s59XI-Aqah_874M7buPfuNRYmxpTyM9twg6K-u2Xsc_qYtAC0IJO-yqneMpwcKxcR6dGoBCBj2dG9oWCUo5Vf0x_Y96f4CTSXRCwOOxT51FEpOFDS3UVLGfwUO5FGxRTvCVl-XVvTX-Mpp_DNXDYZKj9M7r9f3WbTkgmOVPe7ScQw-f2l0_BXzC3TMyiZBFAAxB7xQKJnIUgbiDE4efZ4QU9YRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a427bd448f.mp4?token=LhKeuherjIsNPyo2R0lJlN8xUmm3d3aJpaO8AKrc0KsgcxDHabsU_xfuXvZt1L3eHWUyZseTvwYyAbMKrxjyqtDLbso9N4iiu1pCruOqqY80H2rpVuufu5OyRA9s59XI-Aqah_874M7buPfuNRYmxpTyM9twg6K-u2Xsc_qYtAC0IJO-yqneMpwcKxcR6dGoBCBj2dG9oWCUo5Vf0x_Y96f4CTSXRCwOOxT51FEpOFDS3UVLGfwUO5FGxRTvCVl-XVvTX-Mpp_DNXDYZKj9M7r9f3WbTkgmOVPe7ScQw-f2l0_BXzC3TMyiZBFAAxB7xQKJnIUgbiDE4efZ4QU9YRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی کاخ سفید
:
این پربیننده‌ترین و موفق‌ترین جام جهانی در تاریخ آمریکا بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/134795" target="_blank">📅 21:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134794">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سخنگوی کاخ سفید: هدف اینه که قیمت‌ها ثابت بمونه و ایران هیچ‌وقت به سلاح هسته‌ای نرسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/134794" target="_blank">📅 21:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134793">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85ded96abd.mp4?token=DUP3aLpEjCzu5LVU79a--vIfhd-Fvr_nEDLt5KPcH4Zju4rJL_WxMHZA_Cojhvt6GXPdcQZIAizstnvmuMs6mqejodss7ZT7iZChyBDi5iFdylahohO5lO-BS0teJToqwT7cf2yxRxnxDV7mQTjURp1k6wYn6OYgVVaDvmWvNyY_AW0v12PJC3km0LkKqWuoFRkcW38B3LXzzUylqpkSr3GlXC2b3bUamATW8DN6c1MiDly-8JNC0D39CwGGKj183R0pRZ3DFnTr8qkQ1cpeCxnE1-_g3ONpZtqAwP0UxJ1Ro9WbmxQ_6d5C3cC8iB1lWy6uhjsEhd21axBqajiPJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85ded96abd.mp4?token=DUP3aLpEjCzu5LVU79a--vIfhd-Fvr_nEDLt5KPcH4Zju4rJL_WxMHZA_Cojhvt6GXPdcQZIAizstnvmuMs6mqejodss7ZT7iZChyBDi5iFdylahohO5lO-BS0teJToqwT7cf2yxRxnxDV7mQTjURp1k6wYn6OYgVVaDvmWvNyY_AW0v12PJC3km0LkKqWuoFRkcW38B3LXzzUylqpkSr3GlXC2b3bUamATW8DN6c1MiDly-8JNC0D39CwGGKj183R0pRZ3DFnTr8qkQ1cpeCxnE1-_g3ONpZtqAwP0UxJ1Ro9WbmxQ_6d5C3cC8iB1lWy6uhjsEhd21axBqajiPJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاخ سفید درباره ایران:این تنگه برای کشتی‌هایی که به بنادر ایران رفت و آمد ندارند، باز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/134793" target="_blank">📅 21:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134792">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=IMfgET8XsKAHQ5OqvhDyTksdC3qtWS_FRRUUQbp0wpZS0L4KoMDL6cp31pLaWryRKqjufckl9j0sPvX8YQb17JO3Sas8TqCgct8FTlxqW8wawy4-utCmLwU1qu9FwBKd3-EzS5eZJDrnveNmzbYmKt8byA8mJooQrfCW_QcvF0cLNRtSY_0Jc7ktQ4Vg39eG3nQtF813whxNtcOErTaWBs3FfJRIVBopD5Bn82cdUr2Ebjvk7yFjMPJo6VZ7GFG6ij5Jx8ATHFcQU64T4SEft_Cm6MVmo494Njwk28z9d458T1ajQHG0Qd3Qlny5BW5Lh_AG8tUmCJIeyrRUOlQtKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=IMfgET8XsKAHQ5OqvhDyTksdC3qtWS_FRRUUQbp0wpZS0L4KoMDL6cp31pLaWryRKqjufckl9j0sPvX8YQb17JO3Sas8TqCgct8FTlxqW8wawy4-utCmLwU1qu9FwBKd3-EzS5eZJDrnveNmzbYmKt8byA8mJooQrfCW_QcvF0cLNRtSY_0Jc7ktQ4Vg39eG3nQtF813whxNtcOErTaWBs3FfJRIVBopD5Bn82cdUr2Ebjvk7yFjMPJo6VZ7GFG6ij5Jx8ATHFcQU64T4SEft_Cm6MVmo494Njwk28z9d458T1ajQHG0Qd3Qlny5BW5Lh_AG8tUmCJIeyrRUOlQtKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی کاخ سفید: ایران همچنان با ما در حال مذاکره است!
🔴
کارولین لیویت:
«ایران همچنان به شدت با ایالات متحده آمریکا در حال گفتکو است و ابراز می‌کند که خواهان توافق با ماست، زیرا آنها از سوی نیروی نظامی ایالات متحده ضربات ویرانگری را متحمل می‌شوند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/134792" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134791">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
سخنگوی کاخ سفید:  دلیل حملات اخیر به ایران، نقض تفاهم‌نامه از سوی ایران است؛ آنها تعهد امضا کرده بودند که به کشتی‌های تجاری عبوری از تنگه هرمز شلیک نکنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/134791" target="_blank">📅 21:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134790">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وزارت دفاع ترکیه : کار روی سامانه S-400 ادامه داره؛ هر تغییر مهمی اعلام می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/134790" target="_blank">📅 21:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134789">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
کاخ سفید: ترامپ روز یکشنبه آینده در فینال جام جهانی فوتبال شرکت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/134789" target="_blank">📅 21:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134788">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
کانال ۱۵ عبری: ایالات متحده در حال آماده‌سازی برای گسترش حملات خود علیه ایران از نظر دامنه و تعداد است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/134788" target="_blank">📅 21:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134787">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سخنگوی کاخ سفید، لیویتِ : ترامپ فردا به نیویورک میره
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/134787" target="_blank">📅 20:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134786">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9a850642.mp4?token=S2iP0nd3Dm2BXTF_SfrTf839GRQjwUGoHVEGWU4shuGRteQ-j08ThJUZeYs7jRYkShinDXSSoMKe9hJ-0xzygGOYMqcbyXcNl5o5DlQDW2oxP40pUtV0Sv9PXhMVQ-CqWplFOaQx5jLgVhTGRFFpen02jLt7zbO6ZyzFTHIwOiRsoBiPWwbHmvZ-xiZ2hLY90iMkpMVLrcA1uTtcMxwMjvJSJ4WB1fooWqqQxh7JvBDBqzLPYUePQFH6jYQf6p0a6KGqBXmdSEXks5eZrMrVQikWGlupVhnDJ7_Syo8zuDYVRQtkEOeCCs5T68adumZqsKFud75E3WRy7za1OJb0VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9a850642.mp4?token=S2iP0nd3Dm2BXTF_SfrTf839GRQjwUGoHVEGWU4shuGRteQ-j08ThJUZeYs7jRYkShinDXSSoMKe9hJ-0xzygGOYMqcbyXcNl5o5DlQDW2oxP40pUtV0Sv9PXhMVQ-CqWplFOaQx5jLgVhTGRFFpen02jLt7zbO6ZyzFTHIwOiRsoBiPWwbHmvZ-xiZ2hLY90iMkpMVLrcA1uTtcMxwMjvJSJ4WB1fooWqqQxh7JvBDBqzLPYUePQFH6jYQf6p0a6KGqBXmdSEXks5eZrMrVQikWGlupVhnDJ7_Syo8zuDYVRQtkEOeCCs5T68adumZqsKFud75E3WRy7za1OJb0VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوریه اعلام کرد محموله‌ای شامل موشک‌های دوربرد، موشک‌های ضدزره و پهپاد رو که برای حزب‌الله لبنان ارسال میشد، در مرز عراق توقیف کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/134786" target="_blank">📅 20:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134785">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
پرواز بیش از ۱۰ هواپیما سوخت رسان امریکا در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/134785" target="_blank">📅 20:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134784">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سفارت آمریکا به شهروندانش در عراق هشدار داد که در پی حملات پهپادی ایران به اربیل، در بالاترین سطح آمادگی باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/134784" target="_blank">📅 20:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134783">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی: تفاهم نامه  برای ما تنفس بیشتری داشت؛ میلیاردها دلار نفت فروختیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/134783" target="_blank">📅 20:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134782">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
تسنیم: دود سیاه اطراف شهر بهبهان خوزستان مربوط به سوزاندن لاستیک است و هیچ مورد نِظامی و امنیتی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/134782" target="_blank">📅 20:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134781">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
قطر: ما گزارش‌های رسانه‌ای اسرائیلی را که ادعا می‌کنند ما با مشارکت در یک عملیات نظامی علیه ایران موافقت کرده‌ایم، رد می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/134781" target="_blank">📅 20:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134780">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
کرملین: هیچ درخواستی از تهران برای برگزاری مکالمه تلفنی پوتین و پزشکیان دریافت نکرده‌ایم
🔴
به تماس‌های خود با ایران ادامه می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/134780" target="_blank">📅 20:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134779">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a807ff4625.mp4?token=FtkZin6DSIun60DgrgxrIayRcR3UQ_LOw74a8GtByirC_GY4XvLMFNMDNAx_IPekzH4Mn2M42hggeQRgqkdz49U6F5I-gRf_u4jelX2OQgrKa8EPtYmBaKCWbr1ExxCgsJuCN5sO0Zf19SRy8pBU_atkxHjn_CI1BblT8qpKyyFZO6gxmWVwL2ChZyJZHdK8JSGPTB3U-JYa7Ym2vmF0983u55PBrrUqateXUdfA7yfTqav8JBn0C8PUxj97ZMCyr3Kx3h7ki6_kUZpMu7af5-SLim0MzmR5Vdpalhm5n28bV2UkWPUlASddRqwbu-bEa083rSE5MqfjtlKAOOz3FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a807ff4625.mp4?token=FtkZin6DSIun60DgrgxrIayRcR3UQ_LOw74a8GtByirC_GY4XvLMFNMDNAx_IPekzH4Mn2M42hggeQRgqkdz49U6F5I-gRf_u4jelX2OQgrKa8EPtYmBaKCWbr1ExxCgsJuCN5sO0Zf19SRy8pBU_atkxHjn_CI1BblT8qpKyyFZO6gxmWVwL2ChZyJZHdK8JSGPTB3U-JYa7Ym2vmF0983u55PBrrUqateXUdfA7yfTqav8JBn0C8PUxj97ZMCyr3Kx3h7ki6_kUZpMu7af5-SLim0MzmR5Vdpalhm5n28bV2UkWPUlASddRqwbu-bEa083rSE5MqfjtlKAOOz3FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلش ریپورت: تصاویر ماهواره‌ای نشان می‌دهد که یک پرتابگر سامانه موشک پاتریوت آمریکایی در حمله پهپاد شاهد-۱۳۶ ایران به فرودگاه اربیل عراق منهدم شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/134779" target="_blank">📅 20:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134778">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3aA9rrFC9CPQJO3Rn1NT2mVLSJbt-_fC-XB54SpuC5CfcKp9yaxzYzFljfxFoMsola2DE8Bp9GZBNdTmRQUcJdqDB4KMS8DQfVAqpUr1ZRqidd2IbRpa9RChApB_58SgkMMA2ato-okxAKlHGV73hTUyGpk-i41vOJkPV14a7BfVWk4r9RtiMapLoNW4vKzdU2JFyR5JIypDD4ayZIG6QvMdgkLtp-hO1hkqdy_BsYivmMuCNQnbyMC6-DLcwgNIFzoya0s0Uyr3hJRpq9Qus-8OicTjrprqzmoyx6jyoH0Xm6jc9ikU1hQHy-2TG4PJXAyZOBEyF5GpCYb1Y8Eeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در اقدامی جدید برای شکستن محاصره عربستان، شرکت هواپیمایی ماهان ایران از ۱۸ جولای پروازهای مستقیم بین تهران و صنعا را آغاز می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/134778" target="_blank">📅 20:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134777">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
رویترز به نقل از مقامات پاکستانی:  ناامیدی وجود دارد، اما ما میانجیگری بین تهران و واشنگتن را رها نخواهیم کرد.
🔴
تشدید اخیر تنش‌ها، سفر هیئت ایرانی به اسلام‌آباد را به تعویق انداخته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/134777" target="_blank">📅 20:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134776">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSOfWpFZnShnQKd5mKAPyivd5rSPM5uOeVfu_sFfsW903OkLVGQUf7lys7rTUfeL4hUs4yle9C_RwIejQ4nLkl4vkBuJ2N7lM7rUOW56YUiWzk-_TQqflrXxswOksVL_34JK8XnM1GyD6bnzZCqVrokH75mURoxfzJoWDu6y_W9c_OfxkAm1U7pNOxlwaQXWrbGPTq2AHfJ02i4RcGYiCFIbuydk1np-2xZ3SRkjR-9NQ5X7Byfdh76k5XqhG5kR3vYhXK902YZyNhusXASFsqCVNwmL0DwjuqHZe4jwCjCHmoDIVPjHYhGxfOSmcKTJ9znycSekMZ0_2-KsiRYVhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر  بعد از حمله سپاه به دبی که آسمان‌خراش‌های دبی را شفاف نشان می‌دهند.
🔴
هیچ آسیبی و برخوردی وارد نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/134776" target="_blank">📅 20:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134775">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
عضو کابینه اسرائیل الی کوهن: حفظ تفاهم با لبنان به صراحت بیان می‌کند که ما در سال‌های آینده در لبنان باقی خواهیم ماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/134775" target="_blank">📅 20:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134774">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzXwNSMQf8GC2JsAmaQxVDJQo0mpQb5pKEEIKqctNR8_7Hh3danVXugHc2k48xdEK1jrhTgQ8EvtgHpR7W4iKASrbHahPgm8descdZMEeMUnnlb_sEWdX8IFb5qqHp1PNYCavY619ca_n7P2IbIY_1kLtCUNjfyDlakXcHX32UCJvq_35Hi5ynXzJQxycrivyYSoLU7jB5ia_AFH-dw-wvG4EQJQiQnHKzNlZ0w2EJExsDYxqXcDWKczYryvvmOJqbowBJNU7mpO9B6Ge63bAu0bMYK-IocAPyduMprneeCmDgvgyGZaJ68JS5JevlEG1Dj9MuQUTBJmO5-kMi7GHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقام وزارت دفاع امارات به فایتاکس : هیچ انفجاری تو دبی رخُ نداده
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/134774" target="_blank">📅 20:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134773">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
رسانه عراقی نایا (نزدیک به حشدالشعبی): صدای انفجار در منطقه فاو، در نزدیکی مرز عراق و کویت شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/134773" target="_blank">📅 20:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134772">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری/رویترز: انفجار هایی در دبی و ابوظبی شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/134772" target="_blank">📅 20:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134771">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
روزنامه آمریکایی نیویورک تایمز نوشت: درحالی که ترامپ در تبلیغات انتخاباتی خود متعهد شد به جنگ های ابدی آمریکا پایان می‌دهد، اکنون خود را درگیر جنگ طولانی با ایران می‌بیند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/134771" target="_blank">📅 19:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134770">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saZrvoSR532OeiePrwNMMDv4uIi6WvY7KvNAr7s1Q6yYTMBI0hURsI9GzmBvhN3xZx4eSPIx-doNfQX4_WEAnv0d82eH_qAHfz5RRPnImPuQEusQ2X5uplImj2jsyO6uQa5wIiBAJcO2BD5gdbPyLJP1P_O5DWnmAdv3U0LPvTwqFVFUqq-e-lryCwO9Qme4os-WSh-0IN0K5BCUTgioBkVzMOHBwStX6xzwOYFqidLaJN6oUggZH610Upn13MUmAsRW3pYo2uIPIWQH7VUtmOHOS4beWa8YU1MPhb6xe-1k-XAZXe_UiCAg19SEwXSHTwShcMN3nrUh_Kk9K4S_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایالات متحده در حال آماده‌سازی یک برنامه انتقال برای ونزوئلا است که بازسازی پس از زلزله‌های ۲۴ ژوئن را با آماده‌سازی برای انتخابات دموکراتیک ترکیب می‌کند، گزارش‌های ABC می‌گویند.
🔴
پیشنهاد تایید نشده شامل حدود ۳۰۰۰ پرسنل آمریکایی و تقریباً ۳ میلیارد دلار در تأمین مالی اولیه است.
🔴
این برنامه بر بازسازی زیرساخت‌ها و هماهنگی کمک‌ها به جای اشغال نظامی تمرکز خواهد کرد. مهندسان آمریکایی و متخصصان غیرنظامی به بازسازی جاده‌ها، بنادر، سیستم‌های انرژی، تأمین آب و خدمات عمومی کمک خواهند کرد.
🔴
واشنگتن در حال بررسی یک اداره نظارتی موقت برای مدیریت بازسازی و جلوگیری از کنترل نهادهای چاویستا بر کل انتقال است. این برنامه شامل الحاق ونزوئلا نخواهد بود، اما به ایالات متحده نقش مرکزی در نظارت بر بازیابی کشور می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/134770" target="_blank">📅 19:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134769">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
گزارش انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/134769" target="_blank">📅 19:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134768">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
گزارش انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/134768" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134767">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
حزب الله هرگونه فعالیت در سوریه را قویا تکذیب کرد و اشاره کرد این شایعات برای اهداف پشت پرده آمریکا پخش می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134767" target="_blank">📅 19:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134766">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
اسکات
بسنت
: اگر کار درست را انجام دهید، اگر می‌خواهید سخت کار کنید، اگر می‌خواهید تصمیمات خوبی بگیرید، آنگاه هنوز رویای آمریکایی وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/134766" target="_blank">📅 19:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134765">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
فرمانده نیروی هوافضای سپاه: درگیری با ایالات متحده در مراحل بحرانی خود قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134765" target="_blank">📅 19:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134764">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
صداوسیما: عصر امروز یک پرتابه دشمن به روستای مسن قشم اصابت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/134764" target="_blank">📅 19:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134763">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8014c826a.mp4?token=ddM_EYuDFLkcDXAflL13vmAPPQesGG6FKBendORiiuIM4DJXJR9yZi8cwcqIlsv28jVMwHeByLebMdVYo-Isl_Ao0IRhyAL1Gcy0IJ6Stn-cSAb7zXQFP_JzolMzsJHw__ixbjqkm6_R5B33kW5zFo4DCKzXixmq_RQVdSZ58EbBFJiukSs3NY-Z54szw49ZiGTIEtFFinvY3aZYhz0TqBdX5yBrDMifOVQrtOjUpy1M5TDIdNZh1E9yfUAlvLRxXuWWjPprM-HVBMaBUgF4DFw6vJq_2cwtXHMqonB8Y45ffwyQilv837KLm7p8a3GuDM7J5uY4O4Fwyv13mK3qmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8014c826a.mp4?token=ddM_EYuDFLkcDXAflL13vmAPPQesGG6FKBendORiiuIM4DJXJR9yZi8cwcqIlsv28jVMwHeByLebMdVYo-Isl_Ao0IRhyAL1Gcy0IJ6Stn-cSAb7zXQFP_JzolMzsJHw__ixbjqkm6_R5B33kW5zFo4DCKzXixmq_RQVdSZ58EbBFJiukSs3NY-Z54szw49ZiGTIEtFFinvY3aZYhz0TqBdX5yBrDMifOVQrtOjUpy1M5TDIdNZh1E9yfUAlvLRxXuWWjPprM-HVBMaBUgF4DFw6vJq_2cwtXHMqonB8Y45ffwyQilv837KLm7p8a3GuDM7J5uY4O4Fwyv13mK3qmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تیزر فینال جام‌جهانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/134763" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134762">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEGoVC8-Ax8j8AoWRgzUAqg-ntj2tWiuademHa0X56VOG7fnvLXU9PrSqWT6Qa5HcZ3od14VRUH-WfxddunYDp4ACCr2puQ-_2hUDIrbXdE-Ra95YeKFQ4EehaaSmQEdIuwAAdSVhTd5s8V6HhIfuITxt6FGBrutW0f_aB01pjR3b4gbmXDb6nOO4ZxA_C9CEkfwQCFXnGdjxVTRbfNj1Asef-uc8JZk_Nq2dynwuEPolYd12xKX_dr7sscPvbMLJHHP04cfpZIV8LzXP-BJccKIUxz2Mut0GABca6SkX2eJz5sWqHpjDbQyf4xIE0bFT_gWjq9ywEU9LlnUuxfsGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور سوریه احمد الشرع، حسین الصلما، رئیس اطلاعات را با یک متحد مورد اعتماد جایگزین کرد تا درگیری‌های داخلی قدرت را کاهش دهد و هماهنگی بین نهادهای امنیتی سوریه را بهبود بخشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134762" target="_blank">📅 19:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134761">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJew05Kw1FpehCyL8xp93flbqiWMZl8Gm0tqeQ8GNTXFkpjPVp11Pr0y8r9bc-12lbvLP6gg9DGqWizbfthBRG0PZ7UXgHsz742Jf1cHMrhg3zzoseoj_hHldgGpM2vTNQSW4S5m50MRG1nwXLLJkpn7l8mY0eiUC44PLf7e8ZBt_L0IEaBH7fel2200-JPOi_Yo3YonrM49Bccpy2LlGijOLHj1ka2_zpYBF68iuCkBgZMLBvFP_BxnIWFyh1bYHOqPkHzPaFgXESXjbwabY6A2Exrj9mYs69owx7LlOCtm7bqOUeX4bJ-sxbb-RfNbnJa9tGdXj3tYwDI_9uTBDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خارجه: آمریکا با نقض تفاهم‌نامه اسلام‌آباد، آتش جنگ را دوباره شعله‌ور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/134761" target="_blank">📅 18:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134760">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
معاریو: ارتش اسرائیل ساخت پایگاه های نظامی دائمی در منطقی امنیتی لبنان را آغاز کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134760" target="_blank">📅 18:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134759">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzYaLeRAfBsioetWrxSsTIX4RNDb9SxfPrYjjfEU8lAoaKFBXfbvfoGlauuPW4FeBHR_5TVTKoImnaNH62MFX4unYBM_yatstBnpsyGQd0WnRIfAsIXskVJoBLN8afiJKkOJ1KShEKgkSqPV1aJcXTNzK2K9BzsNbWj-N474rAZ0kIFZYHFASzd3YCSQCECuEI6P2bz6SKjmPnHQ688iVGbTwyke2CyzS6p7bvQ_Vi8u7PjfFI8pD0FsXKex6w6tdErZCoLmdGztUrjW0L0vA4wczeyZmlHh-2aRpcrCSTwO_091AU06aogqBsDCTjrK-qPYXgYWVcllRW9cCNq3yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکا مبالغ مالی تا سقف ۱۵ میلیون دلار برای ارائه اطلاعاتی که ساختار مالی جنبش انصارالله یمن را هدف قرار دهد، تعیین کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134759" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134758">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری / گزارش ها از چند انفجار در جزیره قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134758" target="_blank">📅 18:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134757">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
وزیر دفاع سابق اوکراین، فدوروف: وقتی اولین شاهد با استارلینک از بالای کی‌یف پرواز کرد، فهمیدیم که اگر استارلینک را برای روس‌ها قطع نکنیم، شاهد‌های هدایت‌شونده توسط اپراتور که نمی‌توان آن‌ها را مختل کرد، مسیر پروازی خود را تغییر داده و تمام پدافند هوایی ما را نابود خواهند کرد؛ پاتریوت‌ها، اف-۱۶ها و همه چیز.
🔴
شانس موفقیت در این کار ۱ درصد بود. اما ایلان گفت: «بیایید فقط از طریق ویدیو صحبت کنیم.»
🔴
این اولین تماس ویدیویی ما بود. او گفت: «باشه، انجامش می‌دهم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/134757" target="_blank">📅 18:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134756">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری / گزارش ها از چند انفجار در جزیره قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/134756" target="_blank">📅 18:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134755">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11f469213.mp4?token=X8wBwwP5UwEVzqW0zobeEO1cS62_fq-T7wSi5Hu2abkDMQ4crjuQDTDde-01xLw0IVhW7PAhHBb6zKgNGLZ1Dsj4hOxyBdXymCTjHtI4kFjLcU2Bwww36Ez2SbhVUKAwldh94LZ_XflTiC0YpcB-LIKj2tw9tqx14klDyCbZt3kTDD_HAbvhBfYDXia1RwGuHP8wRlbDcoTthrnZubl65aqKw16JgX8UNn7j9uiutu47n_W_2bG6dzBKRuSlMLKmTVf4DHD9m9KLk01aSsnBbmzYn5xV7I3-0WLHzurO9NNVAEo-Sf6vK36e3fg9-wSgpkptlwdZQdxyCQUFJm1AYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11f469213.mp4?token=X8wBwwP5UwEVzqW0zobeEO1cS62_fq-T7wSi5Hu2abkDMQ4crjuQDTDde-01xLw0IVhW7PAhHBb6zKgNGLZ1Dsj4hOxyBdXymCTjHtI4kFjLcU2Bwww36Ez2SbhVUKAwldh94LZ_XflTiC0YpcB-LIKj2tw9tqx14klDyCbZt3kTDD_HAbvhBfYDXia1RwGuHP8wRlbDcoTthrnZubl65aqKw16JgX8UNn7j9uiutu47n_W_2bG6dzBKRuSlMLKmTVf4DHD9m9KLk01aSsnBbmzYn5xV7I3-0WLHzurO9NNVAEo-Sf6vK36e3fg9-wSgpkptlwdZQdxyCQUFJm1AYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خارجه ترکیه، هاکان فیدان:
اگر نمی‌توان جنگ را به طور کامل متوقف کرد، حداقل در چند منطقه حیاتی — امنیت دریای سیاه و امنیت انرژی — می‌توان آتش‌بس اعلام کرد. نیازی به حمله به اهداف نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/134755" target="_blank">📅 18:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134754">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
پکن: آمریکا باید فوراً تهدید به توسل به زور علیه کوبا را متوقف کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/134754" target="_blank">📅 18:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134753">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
وال استریت ژورنال: نیروهای آمریکایی در پیامی رادیویی برای کشتی‌ها اعلام کردند «مسیر جنوبی تنگه باز است»؛ یک ملوان از طریق بی‌سیم گفت «گمشو»
🔴
افسران نیروی دریایی آمریکا هشدار می‌دهند که پهپادها و موشک‌های ضد کشتی ایران می‌توانند تنگه را به یک «جعبه کشتار» برای نیروهای آمریکایی تبدیل کنند
🔴
تهران به اندازه کافی از زرادخانه موشکی و پهپادی برخوردار است تا عبور کشتی‌های غیر نظامی را مختل کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/134753" target="_blank">📅 18:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134752">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری / رویترز: نیروهای پاکستانی در عربستان در حال آماده‌سازی برای اعزام برای جنگ با حوثی‌ها هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/134752" target="_blank">📅 18:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134751">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01eccbfb3c.mp4?token=fLLmzB771qpEThGFNbTQVG3sqrXcsex0J1UD_iO0m41X9kzzAN2CVHd_WwkV_X9hGLOKBjAfK4nh-SZSsfah3x_LYEyLjClPtoSu0FhHHwCOTs1wDFmpmhJcoFvUCnbmCGghEWFJsKVmd4V6A4onbmHMXAsjLwv3Pr7MnaBOXpowu0dufiAVhm3qN7TSYi0VZcNTZ8mIPB1vAycjsOT89Gl6U6ZNxnZ64N31KY7M9LpjJ-5NIH_fwFl7sbmpoLyda7ijDVTAaJCtR-3L-qkx6CUM-LCPr5lRt8tqZR1A1LfPwaxjiUHh6XFhN9XsDYR0qKCELwD_qeJGFyKg4M0qow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01eccbfb3c.mp4?token=fLLmzB771qpEThGFNbTQVG3sqrXcsex0J1UD_iO0m41X9kzzAN2CVHd_WwkV_X9hGLOKBjAfK4nh-SZSsfah3x_LYEyLjClPtoSu0FhHHwCOTs1wDFmpmhJcoFvUCnbmCGghEWFJsKVmd4V6A4onbmHMXAsjLwv3Pr7MnaBOXpowu0dufiAVhm3qN7TSYi0VZcNTZ8mIPB1vAycjsOT89Gl6U6ZNxnZ64N31KY7M9LpjJ-5NIH_fwFl7sbmpoLyda7ijDVTAaJCtR-3L-qkx6CUM-LCPr5lRt8tqZR1A1LfPwaxjiUHh6XFhN9XsDYR0qKCELwD_qeJGFyKg4M0qow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امید محدث؛ کارشناس مسایل سیاسی : مذاکره بخشی از جنگ و ادامه آن است
🔴
دیپلمات فردی عافیت طلب و محافظه کار نیست؛ بلکه سرباز جنگ است؛
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/134751" target="_blank">📅 18:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134750">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوری / رویترز: نیروهای پاکستانی در عربستان در حال آماده‌سازی برای اعزام برای جنگ با حوثی‌ها هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/134750" target="_blank">📅 17:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134748">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/916cff4f6a.mp4?token=ORJNuLfLO70pVNLVE8dx9otMOjHG5bOXCl9WgQ7bkXzRnDhynCPpYczbpe8BDOOKBFSUJCYfM6HostjCqrD8UDeylsm3e_-2aXPRkJ2TA0UG5VcLldQlSRttbf0x3SZg8Ie4yWjzE3DoMVd7MOJ0hbT8V7deP8-hHiAGTL6AQFyH1ItlcFAD5h5t9OQOR35frD2nAAMhLpfkLTpoXgi1ig4g_gCgOqu3hJknKQcNwLDJ0am1fv5DXc4oa4Re9NKM1MJ838yMJlth7sGc1iBNE6RCE5zxiZhkSu_D_VWQgkBCOmjMu-bwjsv49CoOWBzug0vfJISr_3xMK_fyqxiwQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/916cff4f6a.mp4?token=ORJNuLfLO70pVNLVE8dx9otMOjHG5bOXCl9WgQ7bkXzRnDhynCPpYczbpe8BDOOKBFSUJCYfM6HostjCqrD8UDeylsm3e_-2aXPRkJ2TA0UG5VcLldQlSRttbf0x3SZg8Ie4yWjzE3DoMVd7MOJ0hbT8V7deP8-hHiAGTL6AQFyH1ItlcFAD5h5t9OQOR35frD2nAAMhLpfkLTpoXgi1ig4g_gCgOqu3hJknKQcNwLDJ0am1fv5DXc4oa4Re9NKM1MJ838yMJlth7sGc1iBNE6RCE5zxiZhkSu_D_VWQgkBCOmjMu-bwjsv49CoOWBzug0vfJISr_3xMK_fyqxiwQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراضات شدید در کیف پایتخت اوکراین
🔴
معترضین خواهان استعفای وزیر جنگ اوکراین هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/134748" target="_blank">📅 17:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134747">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef7072e45c.mp4?token=K-oKyn7jBXA2Qe3l-L-03L6itap7qh8WDnUtgA1_zoHZZ-zWRxM05Gp_E9wesdkARzenHkYUFAZhsfHi-yPxg2isTo-yndHtpeaYAilRaVVP_Ahv-wO5svVJvGIs3ayrhNUL3lSIspfwd1P8Xii88sSMXcTl-rAgKiEnKLs9IHWyL7b7gyw3-XdYv4qEK4PcEBWEbTTknyFuTNFWKqUWJXGRxFQpaTjiM97Ste1EdFr9nF39M6g10engaP3dXRoIbvfSNw6UHH983uyTPioHOwgWBmTEJh-80A3STC_8C7CEQPvWUlWFdzzwERmhHyaabRVhKrmghIIcD8-6y_jliQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef7072e45c.mp4?token=K-oKyn7jBXA2Qe3l-L-03L6itap7qh8WDnUtgA1_zoHZZ-zWRxM05Gp_E9wesdkARzenHkYUFAZhsfHi-yPxg2isTo-yndHtpeaYAilRaVVP_Ahv-wO5svVJvGIs3ayrhNUL3lSIspfwd1P8Xii88sSMXcTl-rAgKiEnKLs9IHWyL7b7gyw3-XdYv4qEK4PcEBWEbTTknyFuTNFWKqUWJXGRxFQpaTjiM97Ste1EdFr9nF39M6g10engaP3dXRoIbvfSNw6UHH983uyTPioHOwgWBmTEJh-80A3STC_8C7CEQPvWUlWFdzzwERmhHyaabRVhKrmghIIcD8-6y_jliQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ستار هدایت خواه، نماینده مجلس هستن که توی تجمات شبانه کلاه خودشو در آورده گفته هر کی پول و طلا داره بزاره توی این تا یه نفر رو اجیر کنم بره ترامپ رو بکشه...
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/134747" target="_blank">📅 17:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134746">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyQfwH_82SwTTXhjqceWkzH8V2TxUNUF2FDLC00ajO5r77ykJtsx7AbC2Oulukk1oMBlRC8LX-Mg6-kak-vDG7kiWvI4cocWmP3SbbFfcm0r3YkBQzamc5jOM7qW9WmUW9WZ2fZmQfOun_4vv7rFfqa5hlcN8F5xAef6d5f0NmjJ6fuzK9MMcyfBTStoVWLqRcnmQDh8pqyi7UDrRIBUJ6tPOkt6lVb1UaMvCaMYhv-c4kwB9D7hrYJr3wR72YYbNBEIt13MHClgqNdrwR5NVZGMYVOoA_5EeeP-XgeS0JsdXE5OnVGtcaGo9QvsRWdYZmjnZ9SUfynNNE6fN_kzoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: من جانباز هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134746" target="_blank">📅 17:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134745">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
رهبر انصارالله یمن: عربستان باید مجازات شود
🔴
نقش عربستان در همکاری با آمریکا، اسرائیل و بریتانیا برای ضربه زدن به هرگونه موضع واحد و یکپارچه امت، اکنون کاملاً آشکار و شناخته‌شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134745" target="_blank">📅 17:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134744">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e83aff651.mp4?token=n0-TqG4sHHbRYjvyNCkai6mateBy0qTnBYdSDAEP33GEfjHjKLfHETb5AteIHgffDckydI50wDp4ylGxscW_gHjPByiFsObnnAW2ixuR4nwqTlkbVTt98HRKxodV0j_GHOAah2aLsYuy10ZGvPLUYhCMHeGDPXMPwnqrLdZegXr3PmoFpXgr6PXZ_H-KjK9p8SfWiVaIoETjRzD3GNBTwLaC88X4vNuVagYby8DnhqiSrTE76uiB99ry2AoXlDmEbczj1kc2-efstJT2P3VK8DCsU3BOQR-bu6bj2XYKyxxDl5gqAQ9Z_oGJGhTpUQdqXsljjbqcDK0fCM69Veyzqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e83aff651.mp4?token=n0-TqG4sHHbRYjvyNCkai6mateBy0qTnBYdSDAEP33GEfjHjKLfHETb5AteIHgffDckydI50wDp4ylGxscW_gHjPByiFsObnnAW2ixuR4nwqTlkbVTt98HRKxodV0j_GHOAah2aLsYuy10ZGvPLUYhCMHeGDPXMPwnqrLdZegXr3PmoFpXgr6PXZ_H-KjK9p8SfWiVaIoETjRzD3GNBTwLaC88X4vNuVagYby8DnhqiSrTE76uiB99ry2AoXlDmEbczj1kc2-efstJT2P3VK8DCsU3BOQR-bu6bj2XYKyxxDl5gqAQ9Z_oGJGhTpUQdqXsljjbqcDK0fCM69Veyzqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مصاحبه با فاکس نیوز:
اگر ایران به بازدارندگی اتمی برسد ، مجبوریم آنها را با احترام آقا (سِر) خطاب کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/134744" target="_blank">📅 17:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134743">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbc5724b26.mp4?token=h0RGucemy-sZaPBsfakgco4Mf4nOsJLBFm-gnua-YTTv3FLIaOz6CBlbCS5qAsOaeZ8CX106Mu4Mb8kwilKC17h35KafXWmuzdG2wzKHfbLFwGx9jmQn-27MIR7p6968uCHXWdgVUn0Kw6EmM13EwVRgJgGpGOd7ZiFCML8XWzeqXS-53925KA3GndIs8h8SwCFqXu-B3yxdPwjh_tHkNvG_ZsvvYe-knbokko3mpUBR9YITFGXwXLLJXj8pzJTDoa6cY851BWCvfoRpwQcINbCiz19CfOnzi8s87hrGRvV8Dc40cjppybdZmeJTuYUrW-E_NSFWQjd7DQ2Uab2PXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbc5724b26.mp4?token=h0RGucemy-sZaPBsfakgco4Mf4nOsJLBFm-gnua-YTTv3FLIaOz6CBlbCS5qAsOaeZ8CX106Mu4Mb8kwilKC17h35KafXWmuzdG2wzKHfbLFwGx9jmQn-27MIR7p6968uCHXWdgVUn0Kw6EmM13EwVRgJgGpGOd7ZiFCML8XWzeqXS-53925KA3GndIs8h8SwCFqXu-B3yxdPwjh_tHkNvG_ZsvvYe-knbokko3mpUBR9YITFGXwXLLJXj8pzJTDoa6cY851BWCvfoRpwQcINbCiz19CfOnzi8s87hrGRvV8Dc40cjppybdZmeJTuYUrW-E_NSFWQjd7DQ2Uab2PXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لاشه پهپاد MQ۹ ‌آمریکایی در دهلران‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/134743" target="_blank">📅 17:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134742">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6cc16d12e.mp4?token=Pi1jA6D6jB68K11HxKIepicDD-SszP4u6H3Nh4mNKEfD9jV4TuDXUANQw2cFAQXzQi4ZeeuSidMiPg1KpStwPMABf-lp9xqwg0NqII5a0Leij3lLGKeeqJgBSvaklijm-poM18GMlojXOkWFi6j5sm7nEwszlTdS4658BJDUP90B6-O3C69XGPSwcW5ocv-UrpN4XbM3U1b705Y8qM7vXFPjpwVzIxQaU1lQmGqrHzvLKoTUMCVoFyW18iG1taXDx7KDlna3H-pDn0eK3sF10cLv5SA_Z9X6a1DQ8SOjPsfA2J_AGxg7AELTmj1PhkJP4GU_PSZRtxVUM_6aMzZ13A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6cc16d12e.mp4?token=Pi1jA6D6jB68K11HxKIepicDD-SszP4u6H3Nh4mNKEfD9jV4TuDXUANQw2cFAQXzQi4ZeeuSidMiPg1KpStwPMABf-lp9xqwg0NqII5a0Leij3lLGKeeqJgBSvaklijm-poM18GMlojXOkWFi6j5sm7nEwszlTdS4658BJDUP90B6-O3C69XGPSwcW5ocv-UrpN4XbM3U1b705Y8qM7vXFPjpwVzIxQaU1lQmGqrHzvLKoTUMCVoFyW18iG1taXDx7KDlna3H-pDn0eK3sF10cLv5SA_Z9X6a1DQ8SOjPsfA2J_AGxg7AELTmj1PhkJP4GU_PSZRtxVUM_6aMzZ13A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در میدان مرکزی میوه و تره‌بار کرج و اعتراض کسبه به مدیران
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/134742" target="_blank">📅 17:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134741">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه:
در ایالات متحده، سهم حملات و توطئه‌های تروریستی چپ‌گرا به سطوحی رسیده است که در دهه‌های گذشته مشاهده نشده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/134741" target="_blank">📅 17:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134740">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
مشاهده دود در منطقه ۲۲ تهران مربوط به آتش‌ زدن ضایعات بوده
🔴
سخنگوی سازمان آتش‌نشانی تهران:
منشأ دود مشاهده شده در منطقه ۲۲ مربوط به آتش زدن ضایعات در یکی از کارخانجات تولیدی اطراف تهران بوده است.
🔴
این حادثه هیچ ارتباطی با شرکت مینو نداشته است.
🔴
مشکل خاصی در محل وجود نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134740" target="_blank">📅 17:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134739">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f71UlWkx8KZyHr1Xvh-JGVooytLF8k3cJPBTR9M-PV-MmCfm7WtHgapmuoJBYZr8VIlmbqnPt5ftH0OlbdjfMV86p7uUMqAqfMYGhlPEy5-gWZ-F7VDS7M11lEozfZ0Dd0xBOZKjmqMRg71biwYTOKFMUq9g5W8fPryJxVXy0aBaEiWe_Y4kY_GOiJ4tsdvAdPMqPQQRXk53cg1quWdRESonoMCUxTGYS2pvMMt2G4Dpbdv4GR7u7WW7bjk1K68q-tRTec-5hoxH12kgK05QIaii02VSZFnZOgQ2CmPynJTmUXLAPlqHWc0hLYURoEZ1OrghzEiL2ZncOBy98rnVBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که ایران به هتل کراون پلازا در شهر دوقم عمان حمله کرده است
🔴
این هتل محل اقامت نیروهای آمریکایی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/134739" target="_blank">📅 16:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134738">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqcJL_iRmyeOauAXAoZFh1M-ipnpGyP0ycWCLy8BzMSqv-xKBeG9psPXJQ51HDxhRKOWx444UlFRw_lK5FZ-PfU_3aXP0LsN8GYRnwO5IA8vwix-sKCHO5mhZLjdBlf1AIbRyyfbFNgNO6FpEFgBVQAoPOPdbpLmtkEbTrqda5WaQx2S9g0ADmkC3V931ObyKdvdNonDca7nk0LqDuqhNvLaf0K1dQgD81tKns4iliAwnzIvzzTAk6EKT8xEJzUYHWx6lEzNdX1dbq5g8za0qfQPxBrVbixW7BDO36cN_lRJGSqFx4S_li9ZDkAGkO8sd5FdzkQO4Va8nqvDoTM2Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: تصمیم مهمی در تهران اتخاذ شده است؛ اگر حکومت جولانی بنا به درخواست ترامپ و فشار آمریکا دست به اقدام علیه حزب‌الله بزند، با حملات موشکی و پهپادی مستقیم ایران مواجه خواهد شد. این هشدار به جولانی داده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134738" target="_blank">📅 16:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134737">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQCrU2OiDZZ2UPbR6-h0xsRsS_Ze0Zh8Mkre3FUa_1ng4F2m-eF09LG5-BTFuootmwHpV5OmvfKEyskSEz9uHC7XbNbILfWf78vZSeqqB6iATf-dvVNB3g3sH_HuD5QDT0DQO2Mm6v2WUjrOGYGX5ImRgNKHub8HCz5ZPeYNl6Vw3pSyRTLT0IT4Vv1xg5RjRFP2bpjpnGv8T9Ivr-G0XmX-QcyMZlUTzJ_471q_RmbuW8V7tVev44wFWEr6R0XEp6N0frSYCEv3E5d2kJ7edgiSJ5B6P5YqFqKM_dLYwIox-yZCMPs6jnwPIun9vJVMCa_EzDjJ3M9scbfSvouxXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خسارت حمله دیشب آمریکا به فرودگاه سمنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134737" target="_blank">📅 16:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134736">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLnrMa3xSUocDwHh4qsWuE-rxOqHqLKCgjWSiC7N7tap3EdyW5LE9jUYdDTUsY6bkPrWIrwYPyZs7JlAu3dzHmEWIXwUB-mDxTbhjhbhPFl5FFuF0m_bLqzmKnbBPGvBwxu3JeKD7L_uE3O57f_bO_wX_QfKDlcPdMFL-TPQofavYkxPllRJXmQCnivKZjm50ReBfF2_OPoPS0bir2rsYRkCnPwySvv8ozq5e57aO6jTr0x0bKwzYA5PWX_YLR3jTeMPz8fX7BnvY9ID6SocDTZnEr5fZkZiUfmOJHcjr-XpaKxR7jSv8dNK6JyI6hI_5YAWN8atgRmVuBU_ScHtKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز
:
مذاکره‌کننده ارشد ایران گفت راه دیپلماسی همچنان باز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134736" target="_blank">📅 16:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134735">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Go_SM8i-NHB8KEMKJP9Unid7SAttZOg8Qpp4_lGYUBN8xiGSk04Y5N56PJhNGMYm-srW_m6UODtvCmsyotepObRHeqKYrxSbzCdiCNxpgSvexahUccUr72rH_XNnejZrKunLzGm7-1FlP2aC2bksDuIet2L6kmQldcj84C_qTKqO2UlDGqSbMJb59d4v29ypjsOzN3xkrYWX92tGAY373Q5_kPS-mpKxSSF4Wue235g-2kIBhVmAhAqm2IGlDOMGU8fU3UDXoqP-MU4d0PmSrEXHi3_huwbTsEOq8EzoQUuMlHJBAFyewxeWT45czfuuQcT327BM5iYVQrN5NBNn4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین وضعیت قیمت نفت
🔴
با از سرگیری درگیری نظامی ایران و آمریکا، قیمت نفت هم به وضعیت صعودی خود بازگشت. شنیده شدن اخباری مبنی بر احتمال بسته شدن تنگه باب‌المندب از سوی حوثی‌های یمن نیز بر نوسانات این بازار تاثیر می‌گذارد.
🔴
در حال حاضر نفت تکزاس ۸۰.۴۱، نفت برنت (معیار قیمت جهانی) ۸۵.۶۹ و نفت امارات ۷۸.۹۹ دلار در هر بشکه قیمت خورده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134735" target="_blank">📅 16:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134734">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
هند خواستار پایان حضور دریانوردان خود در تنگه هرمز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/134734" target="_blank">📅 16:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134733">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
فوری / گزارش ها از چند انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134733" target="_blank">📅 16:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134732">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
رویترز: شرکت‌های حمل و نقل دیگر به اسکورت‌های نظامی ایالات متحده در تنگه هرمز اعتماد ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/134732" target="_blank">📅 16:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134731">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7129ac30e.mp4?token=S7WqGY22jEneMyQT8weWmmOJCiUVX4MuvQPHm-ssi6_IlW6oA8hhlLcBgRslxhzHgUc-oMhQPmyCSKBB1OIP-Z55itqgzK0ZqCS8TpWPhOE2zJ7GqewrEWTkQy4hUfUxZ1NE5Y31qXkvwLHvbzRUoKfWfdc7YcHRUdDQmwL6OyJz_mWh3Vy6JJEDUiY8yPvovcnNa_lI-7vXjtQGjwiwXIrSL2TSabNGKeig_xoxXxgzP35PyUlXF3_DwB9ej7s9GEfdXxkUGffr6QezraDCrciaKcj1MGYVUKfl0hXYHTrKW0PD7ByMNXhtOrl2mTIueasQq11Hhr4igmbdJijvfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7129ac30e.mp4?token=S7WqGY22jEneMyQT8weWmmOJCiUVX4MuvQPHm-ssi6_IlW6oA8hhlLcBgRslxhzHgUc-oMhQPmyCSKBB1OIP-Z55itqgzK0ZqCS8TpWPhOE2zJ7GqewrEWTkQy4hUfUxZ1NE5Y31qXkvwLHvbzRUoKfWfdc7YcHRUdDQmwL6OyJz_mWh3Vy6JJEDUiY8yPvovcnNa_lI-7vXjtQGjwiwXIrSL2TSabNGKeig_xoxXxgzP35PyUlXF3_DwB9ej7s9GEfdXxkUGffr6QezraDCrciaKcj1MGYVUKfl0hXYHTrKW0PD7ByMNXhtOrl2mTIueasQq11Hhr4igmbdJijvfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویس کرمی، مدیرعامل شرکت ملی پخش فرآورده‌های نفتی ایران: نصف ظرفیت پالایشگاه لاوان در حمله دشمن آمریکایی - اسرائیلی از دست رفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/134731" target="_blank">📅 16:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134730">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XevUinXqOqAgf9X9EWZLzxovFaGqP5VpgJ7yfvtQNRawrT1dOw-Fs65oD27j2_s7qRGxMY5qL1JYAHxAsC5wxxhLlwj2xEGlyQUWW08daEcksNKQjCyfh5CBu00Wtyf-JuHW2rzdrl6WdvdSZ2TU-kWHJ0Qni05UxCmE-mWQwm9JuYScg362tgFyx44lK1AqtxMngBuYRlGUkSsjYA2CAWhQRiGWxRGgzXBZwC1DjrKGK6YCzPCsq7Ep0i7xCRdcHjUX-jIk2chpFRq9MWqeLqyVHQboXnvhcvSUJ-aPWS_A1udQImgxVBNfLf6HGqVtXCiA9eREmkm3LxRTHDB-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت جدید محصولات سایپا اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/134730" target="_blank">📅 16:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134729">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سخنگوی ارتش: آسیب به توان موشکی و پهپادی ما در حدی نبوده که عملیات‌های ارتش رو مختل کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134729" target="_blank">📅 16:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134728">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوری / آژیر خطر در داخل سفارت آمریکا در بغداد شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/134728" target="_blank">📅 16:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134727">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وال‌استریت ژورنال: ترامپ شامگاه سه‌شنبه نشستی برگزار کرد تا درباره احتمال اشغال جزیره خارگ یا بمباران کوه کلنگ گفت‌وگو کند.
🔴
ترامپ در مورد اعزام نیروهای زمینی تردید دارد؛ او بارها از بزرگ‌ترین تهدیدهای خود عقب‌نشینی کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134727" target="_blank">📅 15:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134726">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
کانال 12 عبری: دیشب، ایالات متحده و ایران با یکدیگر تبادل آتش کردند. آمریکا به هدف قرار دادن اهداف در منطقه ساحلی ادامه داد، اما برای اولین بار، اهدافی را در مناطق پایتخت یعنی تهران مورد حمله قرار داد. ایران نیز موشک‌هایی را به سمت کویت، بحرین و اردن شلیک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/134726" target="_blank">📅 15:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134725">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pU9Ep24LptpD9Zo_viSb8kL_3kwo-E3cmPqcdmhXyUzI2S0Y96eWFoUQu9JyWjXcnvTBnBWm8TL0ouw-U_D4HlHs_AWu-rekvnUvGxq6EnaZ5qaArwmshdfkJlDGUfTg8ZidRR2r77J28xAzIqrJHZ9B7vw7D8B9AQ-wMY_SlF6UgZqx4TcZWyGINSnbmtqghOWW8vl5ynsm4kMhZgWk77tTITpC980mEXh1itilwdBy3ruPj4XsjCHlBIOgdak7OIKsvybLXwNFV7Fc-FAIHRCnoFQ1wvFqycJE7kRMZ_H80n_ScNNPXTWolW929keZle2ohzhC0HJ7JLyptpbwbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گریگوری برو: عرضه فراوان نفت در ایام منتهی شروع درگیری اخیر باعث شده قیمت نفت فعلا بالا نرود
🔴
قیمت فعلی نفت با وجود حملات زیر ۸۵ دلار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/134725" target="_blank">📅 15:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134724">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
منابع عبری خبر از گفتگوی تلفنی بین وزیر دفاع آمریکا و وزیر امنیت اسرائیل در مورد جنگ با ایران میدهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134724" target="_blank">📅 15:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134723">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
رویترز به نقل از منابع: حوثی‌ها اعلام کرده‌اند که در صورت هدف قرار گرفتن شبکه برق ایران، تنگه باب‌المندب را مسدود خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134723" target="_blank">📅 15:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134722">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
کپلر: ۱۳ کشتی روز گذشته از تنگه هرمز عبور کردند و تنها یک مورد از مسیر عمانی استفاده کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134722" target="_blank">📅 15:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134721">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXiGY6lX06P1NCMc70zPzShetQArMKNWRXZEodTlfF7uglVcB3HXS0ZpBTmpZJV4bFSqVQ_qDFKNPNaTjdOaJR_4ZEQLsRlnX3UHgh32Vn6d5bTteoz6t55FCBDLT5lSbwhTgWMURnKB97ecqMIFe6djbzobBPGT4wwvioxbzVmOIT1jsYgSv5yGTMN-plG32BrJShd7LDXOcYEDpDhGIhvxtSvOpgVIJd5_sGUwP00zvt6J-fbaF6MFRR2EhbbuzkYMYnsyg4fexl9ZmHPlF2DBM7U5PnOVpoM6N3iEg6y68yrCpFYOuaVr2qfWSg4GrHt_y-DS-m2HGTxjumqSSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نگاهی به آرایش ناوگان آمریکا در محاصره دریایی ایران؛ هر چهار ناو لینکلن، بوش، باکسر و تریپولی در منطقه حضور دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/134721" target="_blank">📅 15:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134720">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: در حالی که اسرائیل در حملات آمریکا به ایران شرکت نمی‌کند و به آتش‌بس در لبنان پایبند است، نوار غزه همچنان مهم‌ترین منطقه برای عملیات‌های ارتش اسرائیل است.
🔴
در غزه، ارتش اسرائیل دامنه عملیات خود را گسترش داده و در ماه‌های اخیر، حملات خود را با شدت بیشتری انجام می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134720" target="_blank">📅 15:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134719">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ثابتی و رسایی رو باید بست به سرجنگی موشک و زد به پایگاه ناوگان پنجم تو بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134719" target="_blank">📅 15:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134717">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D33xtteg-KzNSN6MJqyW6EGGuR57uuzu9AmY8-j7pMQp3DbSOOHZuATZMIVl0UWxM9SrPnvCId_3PGLL9wei1-KYaa8tFjwcug8PfktAnphfM-vA883drHeYkwdP-QB7qhal-DlegFMSrsxk5RRsWYmc_TFSILnCma0S9Wkl73-Z8lYzxHUbGUnguHjUOkwEL8vRhdc8xIYWchDg7PxDhEESaBzaaKD33oQaMXERNk3WKd8hCa80qnEzQHPxi1AaHk2sx0X3bH8z9ibVoney34NMuU5GdlmbVBcM1KloDPRwAgEPpogFfjDoSZhwueKPx9ar11cxhw2opYVLE48hbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی منتقدان خودش رو ولگرد خوند و نوشت ۱۸ماه جبهه رفتم و الانم دوست دارم برم جنوب
🔴
بنده ادمین الونیوز جلوی 950هزار نفر اعلام میکنم، آقای رسایی ....... هستی اگه نری جنوب و زیر بمبارون ۱هفته زندگی نکنی
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/134717" target="_blank">📅 15:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134716">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5JPUmlkN4v0DPbtWxeHUDWVgf4jMny8nf4cCOIEmfTZAY375Q39jkegkPAnSD16KGZkLSMikTvq6hPGZSPKW9HU9EatIDB-OmB7LbC9TehElyxBz_nvMu8v99Kqboi9oPCtJUA5GpXYy5To9ZwpLdU1tXNupcK8MW1PAGxVXs8x-rC8P0AYRo2aOk3lMy7i3B2FSDABFSEC77vXBhVuWMyKHrXnzNP3oshWUNhW5-o_z-SyJa6JepHy3Arjtqw3UX3bo2tCRnMc1qHi60HEuyl5Vej8oe5tQvekqd372KXC33U3-0SSwLwkD9CZWgqQNTQkzOrk_njj8SDZ4oMcNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی اکبر ولایتی: تنگه هرمز متعلق به ایران است و هیچ قدرتی در دنیا نمی‌تواند تنگه هرمز را از مالکیت ایران خارج کند
#بوتاکس
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134716" target="_blank">📅 15:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134715">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f854ed7d0c.mp4?token=BCZ9U-x6lp-Ur7UPfcLmGy9gRItoQWLKTk8_ksjKnztQ6L4invjtoTrff7VYt_r221rVXcxhS1EHbhxPzGYMbdqHcLx3wHkN-IHaW2MNXSDT4s3yxeaOew0FhtyxCd0yVbNKRuX27jRjFa31JaekU9ZLaVArWerbF6S18mkTT_eW2Sj1HMnh2jjEzB_Bi9OwRfdIGoxEfNTPhC5RDN4GwR2mHdXYxlt0FagV_AULyGyd3R6mZ7bYAYjt79rSiNAYAvdimLMv4OZGOfbuIjArF46gZ-Rtte8wQI2jLFS0WJLWcSSw3INa1L9CP_WoHRQgg6GChnDXW3I3Sv3aZ06qdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f854ed7d0c.mp4?token=BCZ9U-x6lp-Ur7UPfcLmGy9gRItoQWLKTk8_ksjKnztQ6L4invjtoTrff7VYt_r221rVXcxhS1EHbhxPzGYMbdqHcLx3wHkN-IHaW2MNXSDT4s3yxeaOew0FhtyxCd0yVbNKRuX27jRjFa31JaekU9ZLaVArWerbF6S18mkTT_eW2Sj1HMnh2jjEzB_Bi9OwRfdIGoxEfNTPhC5RDN4GwR2mHdXYxlt0FagV_AULyGyd3R6mZ7bYAYjt79rSiNAYAvdimLMv4OZGOfbuIjArF46gZ-Rtte8wQI2jLFS0WJLWcSSw3INa1L9CP_WoHRQgg6GChnDXW3I3Sv3aZ06qdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد انتحاری اماراتی در آسمان جنوب
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134715" target="_blank">📅 15:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134713">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGKn4IJLr3v0re7f1r9NQW_hp5EiFppO-pgi8lpbOyfPIUfgGreyVufogEd1zpp8a0eO8irQ4LcRZSf6QHjGzvaDMZw2li5AnMcIPpso6kbcsQJ7vOEia-8DipIPXJVxOPYkfxb7HmbheXcFntG6eeJdZY6cPVZhRiDIXO9X7HVoqC-0Q2ofPqFxLvpCYdM6zYSm3e2cHmEYZKl5QUHdWIeI2run4Qg6hf9UKAh2v-AMneWcoloRfye-tf0Tlxe91sI50fgibmH4WfPqs5rV90VXdoMjkQG6BGgboDdyf5bi9QiBFQWVxxW4s2AH8q5_9iDZ-tgL31JYC7cULIWTqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/679fc2d852.mp4?token=ij8XSQ1FuBGyesCCs8klFieCZbpwb_ixNqKvM1Gr5PL87_Ap59krFgWEfUta96cfQJh6svnUGft-cojUug3s8yYmnzZK5B5KIq_4J3W2bwX-5yG2Q0q8fXAfswuFvRI7XEXI5alTHtbHqxI6dEISiYwDDDM2uwrrtnxvnjgzLIUrZWy-VbKWNXCj9Wx42PYh0lTOLwORarq24Oc4jbMWd7IdQGoiYhPboxKeB6avnD20Qojz0ZmfYxm8ZMPTDV_FL9r956hcpy8sDeZ5R26scNO-Tj0AyK9BFlmxOyw7tugthZJZXsWnJBXowLDfEV8-DXLOsfa7z2twDDcCFV7bNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/679fc2d852.mp4?token=ij8XSQ1FuBGyesCCs8klFieCZbpwb_ixNqKvM1Gr5PL87_Ap59krFgWEfUta96cfQJh6svnUGft-cojUug3s8yYmnzZK5B5KIq_4J3W2bwX-5yG2Q0q8fXAfswuFvRI7XEXI5alTHtbHqxI6dEISiYwDDDM2uwrrtnxvnjgzLIUrZWy-VbKWNXCj9Wx42PYh0lTOLwORarq24Oc4jbMWd7IdQGoiYhPboxKeB6avnD20Qojz0ZmfYxm8ZMPTDV_FL9r956hcpy8sDeZ5R26scNO-Tj0AyK9BFlmxOyw7tugthZJZXsWnJBXowLDfEV8-DXLOsfa7z2twDDcCFV7bNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم‌اکنون حملات جدید به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/134713" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134712">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
جلیلی: مردم میگن حاضریم تمام کشور رو فدا کنیم اما انتقام بگیریم  #قرومدنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134712" target="_blank">📅 15:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134710">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RUAsnAl_yCuOE45x5N6xjtJI1Mdbyhv0439bF7QynWvT7Py_eJfctZaz5rDVtOYffQ13KkDdZs_hJy_DMPq1h6UhpkP7Jw9nUXXTRlJPRy0O-kNxI3soZuV7ATf_dtq9jvCf94CWJKIKTHDw7DMiyY7apsKTgUcZq8eiI0245DTMQR-UIjHcZWReUb8KoSK-_JujpFyTtmd87bEyiB-WqKIvNnFG_clBuyeKYhZIpVAwYxNfMTZXte_kkFVquGYaPtLfUnvMS64e2ELMBVwA2JEWI7QarWzimNwriD1VzPjej6PE0ASsefqHQ0h6qJ8CFn1XVF0-geafQU8_bDSM3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UC2_fLWuCfMDeA1wIaTusI2avxiL0tngK-mpOgJHUDUM9FP0v4kWDvkOG2WItTIQ-jIM4Ejap86P0_HMQ_dKg8mVlT_VIvdkaX260t7DIxU0V3YB6vz_fn0DFJ6kIUu91szDe5dHTJ-xpHiCj4b0TnVllLwhW7awhMavKT1NsMDDg9FmyaE6HK6oqvMgyUsVlO0ig7V-w2fhrkpRZ6BRYAwxeGy9QhLQZuqURyRMEfINmnOpYPqH28rlLm6fl2wwumgmNdpadjuzM3IhglSZ4eG7bwacHnyzgrrKH8f-ASqZ9djziToc1EU3fh9i5Oag6srz23Y3_8Y6QbvuJurxKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
آتش‌سوزی در نزدیکی کارخانه مینو در منطقه ۲۲ تهران!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134710" target="_blank">📅 14:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134709">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ژیلا صادقی،مجری صدا و سیما: همه جای دنیا مشکل اقتصادی و قطعی برق هست،مردم بعضی کشورا تا روزی 6 ساعت برق ندارن، مردم ما ناشکرن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/134709" target="_blank">📅 14:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134708">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
بیت‌کوین امروز در محدوده ۶۴ هزار و ۲۸۵ دلار معامله شد و اتریوم نیز با رشد ۰.۶۸ درصدی به یک هزار و ۸۹۰ دلار رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134708" target="_blank">📅 14:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134707">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6lEj_o2wci6nRV_pcD3VFNYJSebFQu8xucg04B6CBBmKnZ6folqXcXn7HJotdNlmavtOF8iHconcsUjtIJA5XZ7jH96urhz43iQqkygk1VfP_k5njWBDP-92k9YK9LqIfgfGmFpj47bCiYHwhfslcIbKb29KSnVXasAD6xNAymF_7THwCEgevmELBwoxBgvWl_YCuI6HVvYWSZWO9v11vufIQ6gvdv2ViZLGGg2cpUwV3tvE-2EA0XflspyIGLkWVRA7YAXpf9JNvbo0ldOviBih6kNoUnp3gGJbrC-jGVKfsJ19inyOxBOTet0PgxsqNeLttknRrXNifGfCYiLNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلیلی: مردم میگن حاضریم تمام کشور رو فدا کنیم اما انتقام بگیریم
#قرومدنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/134707" target="_blank">📅 14:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134706">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
صدای انفجار در آسمان کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/134706" target="_blank">📅 14:39 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
