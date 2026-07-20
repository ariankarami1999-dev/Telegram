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
<img src="https://cdn4.telesco.pe/file/VodC7mPs4FrQXNI7816SdJh8oz1GJxa1vr6Qo63Hy4sSZ0Drh5plf5xmY9lEj6aY4UCtQLNcQzbxB99TAXB2qf2Wa1ra4Ka5NdmZi5S6dAwKE6OjMOiWkJgtyi7UHglsutJ2uc3YQZRLQbM4yD6hI63HLxwO1Afrrm5VVrhxh0LqRU9O7NY4_v03619P7ozwcAzfz01Az9MuhN_dZ5Q3BLgOEgxCoPYwdBY9XP4zztZDBLTL5dLe7NaGjg4H6t5sZSKnkQ6BsSYVUgOSv0hUZoPwVKE_6JlW7nICtdbQh-Eg6NocZEycvj09DYEJl0MYoHN-p_qHIro2Rf1FQ1hAnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 519K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 11:37:42</div>
<hr>

<div class="tg-post" id="msg-26130">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFN-Uf3bdPoHILSJBUa2Yr8EO15msXCmj4Yju0cOSZv43NIfknYOy04cfsKt75s88RumZVOTVGSEPW58hnK6eycvxeQG3DEoFBs4zo41e3e2nw57HeYXWW0HCfb59-Er5A2uWbxT6c6dZvUMUT8BPT1PD4Udnfc-kYLmYF2dC-9wAJZx2gi4NV7WPyVA2thfoq0GSUrm9sjnY4LdGoqYBLAisFH2hw8DnJ7FCP75NfQzCs0Y5VYdtmMeiizhWx8AveLRxDKZ-gSYaMxJJ-95IvkVBrYGfX7tJbenBQh3oxKfelusvB98NPR2QoPd_YZmEuqxIGNipirFfBf6P-aJYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/persiana_Soccer/26130" target="_blank">📅 11:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26129">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyHFyxZcKWYlsa9iGMUDNG6cZ5kn_-dvv_rV33sZpJC0DcmhI_EAu6RhIq-ls7WZIt8XXqrK9CyQkOiKTI_DPIpF9ZPZMV-vbw2sSGLSzh0fmXPHCSxgpVCnvdh7Gn-yvJd0EasNrlkMcTm0ltn-j8oqu132_6RlnoRNYGNvOMVQGYkZ1KXAtwYFOaVUZ63tKEyvN4s6evTrp2Si87KTZ_ZXG4Y0562Bne7rtkvoSS5ZUHkyoVJZHs3h3GTb0IENm1SEEjOEgJBPSKkBejbnr6Tuad6ogBREbBX6x4mjVacJSevnFfIKcmx2H7GBIqBqaaksQc5Xr06AWbq1R_FpRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#فوری؛ باشگاه پاری‌ سن ژرمن بزودی قرار دادی چهار ساله به فران تورس اسپانیایی تا تابستان 2030امضاخواهد‌کرد. تورس به مدیران‌بارسا اعلام کرده که‌دیگر‌علاقه‌ای به موندن دراین باشگاه ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/persiana_Soccer/26129" target="_blank">📅 11:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26128">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202f77d369.mp4?token=EzVPGDyzWBj599KTeFBF9zrqZeX6oDBsgLCWVd4soqMjpqCOXuds7KMqzJo0Jryay_AUxW7-pcjQy-qYXDF1dVJUmf7-WhcrrnPZC5wAXqeYVjqz99Xu_q00_sTDklVEA79sF7PBmYXruzEUm5tdLpxDax-u62N5s66UWJTaf50xYSiLOyFg7WF4gSvdgelQH0qWcAzYya5a-iQg5ot6DiP2YC1MYt-dWqDJSwi5ov6BVtfud6AHYBgYDGgBHLueNV3IJtXqGV5fq11-maZNjTJvzX8cVGrurdd1yCexj5d7t-ZGwW_UIzwF-F_6Rukvtw9x42K1lYKuwGOS764Si7fKE7DenOr7fzfUGXagk-onfzC1XxjofrkUPY5K9B49bXxR2HLTY1i2qz0KWX5ZqY5r4Wz3MGDkv0Aq_1ZuV8OpWz4XOu9-AzBIDi8VTAnu0zTPsml6MGcxj_l2xqwgAfuUGIqMAJOcxgkQ44Xxkv71DuZt2EvERQRhinE7-c-JMGJW6GzJr1R_FLoEcUNjiTb9pWY5Ewv9VE9mUkJqLLw-kf7mKfwclVXcx23RCdWW2jsIXHlzn0OHgafTYVtySc79hyujB4HfqE649axb8GhRbW1irU859L2cKxyfer2nqKCKYUe_9_4xOT1TStQpB0jvXZ39dMUWz-M66aOmvtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202f77d369.mp4?token=EzVPGDyzWBj599KTeFBF9zrqZeX6oDBsgLCWVd4soqMjpqCOXuds7KMqzJo0Jryay_AUxW7-pcjQy-qYXDF1dVJUmf7-WhcrrnPZC5wAXqeYVjqz99Xu_q00_sTDklVEA79sF7PBmYXruzEUm5tdLpxDax-u62N5s66UWJTaf50xYSiLOyFg7WF4gSvdgelQH0qWcAzYya5a-iQg5ot6DiP2YC1MYt-dWqDJSwi5ov6BVtfud6AHYBgYDGgBHLueNV3IJtXqGV5fq11-maZNjTJvzX8cVGrurdd1yCexj5d7t-ZGwW_UIzwF-F_6Rukvtw9x42K1lYKuwGOS764Si7fKE7DenOr7fzfUGXagk-onfzC1XxjofrkUPY5K9B49bXxR2HLTY1i2qz0KWX5ZqY5r4Wz3MGDkv0Aq_1ZuV8OpWz4XOu9-AzBIDi8VTAnu0zTPsml6MGcxj_l2xqwgAfuUGIqMAJOcxgkQ44Xxkv71DuZt2EvERQRhinE7-c-JMGJW6GzJr1R_FLoEcUNjiTb9pWY5Ewv9VE9mUkJqLLw-kf7mKfwclVXcx23RCdWW2jsIXHlzn0OHgafTYVtySc79hyujB4HfqE649axb8GhRbW1irU859L2cKxyfer2nqKCKYUe_9_4xOT1TStQpB0jvXZ39dMUWz-M66aOmvtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/26128" target="_blank">📅 11:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26127">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcihDwsCoyDfqG3i8XhpAoytQlrCZSZvWX7lHI0tEMKQOvsA2fBYJ_aHU7NjASKSafbW_mkAH_-vgHne7zpYrT7TeqoqN_YUeAB3TYLVXo1dhSKPfjXZ9QmYw_gaSw8GMEhw-POyveROiD7l_BkaxrXXbAA0pSs-1RWVmB0TFFBzm2ZXRWcrHa1VfVgGRjeePadNGS3UwY8k2mHB9qx3WhVpBKZF4Vj4zo4nuV2YMGBW9jCo4Q1NyDBPIJNuSDlNsovRBPIrSIUIRAfwH8Oj_MNUeFSw3Z7BzB5hiQ5ddzPV5sDpC_lDXbRQ-1zih7aHOp_2NUGj6FmH1pyFDXWkvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
طبق اخبار دریافتی پرشیانا
؛ رضا شکاری وینگر فصل گذشته پرسپولیس دو پیشنهاد از لیگ ستارگان قطر و سوپرلیگ‌بلژیک‌دریافت کرده و به احتمال زیاد درصورت‌توافق‌راهی یکی از این دو لیگ خواهد شد.
‼️
پیش‌تر در روزهای‌اخیررسانه‌ها مدعی شده بودند که شکاری قصد داره به باشگاه استقلال بپیونده اما پیگیری‌ها نشان داد هیچ مذاکره‌ای انجام نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/26127" target="_blank">📅 10:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26126">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=POsPw7obDXZSZdJA3mKo7IajoBmjrwvgCy0do82dFlOLxNwq7KtcX_KaWOj1ynuf6D-mlhm9VA1IystaLD__OX4o-ZhDL2udvPnt0gulvmc7TXjwPfrMyBXEeZc8hquqKLJ3m7dEVyamlKGzxH3yWcXv0akRTaA8RKpa3dvfHNd3cRN2Z2zjWhWvUrZLs5k6WRlh6og17F9W5xjH7K6ZBDN3KaI8CfMSzpczW2UhUex5qBgDQ1xw7-3JdadlYi0d6Lw092L9fnVxABhqZ41Z1JvE4Cxytd_FA4XpiihcT2iGypKwrTeS_-qu-RTId9OnlUi91_A18vG6xKwrAoXL6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=POsPw7obDXZSZdJA3mKo7IajoBmjrwvgCy0do82dFlOLxNwq7KtcX_KaWOj1ynuf6D-mlhm9VA1IystaLD__OX4o-ZhDL2udvPnt0gulvmc7TXjwPfrMyBXEeZc8hquqKLJ3m7dEVyamlKGzxH3yWcXv0akRTaA8RKpa3dvfHNd3cRN2Z2zjWhWvUrZLs5k6WRlh6og17F9W5xjH7K6ZBDN3KaI8CfMSzpczW2UhUex5qBgDQ1xw7-3JdadlYi0d6Lw092L9fnVxABhqZ41Z1JvE4Cxytd_FA4XpiihcT2iGypKwrTeS_-qu-RTId9OnlUi91_A18vG6xKwrAoXL6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🩵
آپدیت جدید تلگرام دیشب اومد؛
چند تا قابلیت جدید بااستفاده‌از هوش‌مصنوعی اومده. چندتا عکس رو میتونید مثل اینستگرام پست کنید تو یک پست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/26126" target="_blank">📅 10:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26125">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=k-oTW9uTi9w1VZ5CT3jdgWWs0zXRqriBZN2zwYoLCliZKPMD0q5HMcVZ1f1FQbW7twVvzdmRIP5F5bZ8n03ESs8agFI_hI2cNIhcrpORttuM2J9zKqYR5490X7oMlq0tLUmF7MpScjDuAhVFv1n4H8d5GYO5Y9eKSuc6nFgNzfVdk0fqbiavZL9A2OAardorjMRr48odUvzXU4oJ6VnxSRe3qg2IZAjCKH1JHpXBqQk45cDMgOfR-xPqPO2GrHsCDObxpbPACJxBB-X4Xbkex2x9MvDQGbfYK4b5Pr23I6V4-xQs9v8KUk7IcfdUy2mfAjMQOAfXRdrAAnex5ATlvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=k-oTW9uTi9w1VZ5CT3jdgWWs0zXRqriBZN2zwYoLCliZKPMD0q5HMcVZ1f1FQbW7twVvzdmRIP5F5bZ8n03ESs8agFI_hI2cNIhcrpORttuM2J9zKqYR5490X7oMlq0tLUmF7MpScjDuAhVFv1n4H8d5GYO5Y9eKSuc6nFgNzfVdk0fqbiavZL9A2OAardorjMRr48odUvzXU4oJ6VnxSRe3qg2IZAjCKH1JHpXBqQk45cDMgOfR-xPqPO2GrHsCDObxpbPACJxBB-X4Xbkex2x9MvDQGbfYK4b5Pr23I6V4-xQs9v8KUk7IcfdUy2mfAjMQOAfXRdrAAnex5ATlvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/26125" target="_blank">📅 10:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26124">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=FoS3q79XJZqJ9UecqStz5SvEMoyYLwmDBcfKnE3tm2tyMsJM16qXdxSel_lr3Iosyu9hOyBNbSrQcTk9qZ_eW_m2JHMLn8YqsVR_C_JTyoHble2pu-HYYUMdT0RAaqTURQCjZ7humZfWQD7nRegBhYJl_jbOUfjmdLfSIuaAstUryQTFfUoMwT8lT8qQ2Bov34Wx4HGTMyqDkc9ZeYZ-Yo5d4ZJBg1ujLUQiH6EP3VywJSrqWQUEXH_gxyBZSl12ovdmTz_0Ms0CQgYfpsx_WDktGVp5e8cvza7sSg9mvIUdn0s_u_GPhiLFZDrECxlqNrNQree0FsjjU_P2Hb9fOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=FoS3q79XJZqJ9UecqStz5SvEMoyYLwmDBcfKnE3tm2tyMsJM16qXdxSel_lr3Iosyu9hOyBNbSrQcTk9qZ_eW_m2JHMLn8YqsVR_C_JTyoHble2pu-HYYUMdT0RAaqTURQCjZ7humZfWQD7nRegBhYJl_jbOUfjmdLfSIuaAstUryQTFfUoMwT8lT8qQ2Bov34Wx4HGTMyqDkc9ZeYZ-Yo5d4ZJBg1ujLUQiH6EP3VywJSrqWQUEXH_gxyBZSl12ovdmTz_0Ms0CQgYfpsx_WDktGVp5e8cvza7sSg9mvIUdn0s_u_GPhiLFZDrECxlqNrNQree0FsjjU_P2Hb9fOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد ترامپ‌موقعی‌که‌کاپ‌رومیخواستن ببرن بالا ازپیش بازیکن‌هانمیرفت‌ بره‌ کنار؛ رئیسفیفا اینفانتینو دست ترامپ رو گرفت جدا شه از بازیکن‌ها، جدا نشد وایستاد تاکاپ ببرن بالا؛ فِش فِشه ها اتیش بازی بالای استادیوم چرا آبی بود. قرمزنبود! ازقبل بازی چرا آبی تدارک دیدن!؟ فکر میکردن تیم ملی آرژانتین میبره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/26124" target="_blank">📅 10:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26122">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmSVF-_FTtoTJ6fRG7HYeX20Vlsw0wCdgsGW0SM-IeXJgHRlAB4B2__AICkWb7G-Fe9mLnEPBb54UzBrXwLYLDOuxbsV_wwua_cqUPCmMt2tPtmoSDKdtk2fBm-7Bm_pEwgrjalkDOtErT_X64HE1LCeLVNrW-0Y5YuBOd4uKZnj0yJ5PuAgA97BoD-UFmaHPw2CffMLgCG_Ioy8v4gu46cBW7UR3i1zmN3CIEDCFeShaSFYrJVS0pQm_LZba34THtXwiH7eczvYPq9kGmXXdGuLtNf2hHh7Kj1jHNA0TtzIVB_KA4HotwWN568aoP6l7f_0W3Jfp7aELrAPqEEl_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDgzcDrhislvPaPBGvetnfulgEzLyONP2R2t99y8kV7gTZBJMrZ0v8uH4wYOIn4_zaAcJWZCKtp13D_wJPhQXJ8d5mbc3xuUb5SoSMOQ4TdbyscNe2gRmUAY0LGCKPsdoVsaN0excMFwEmB8P59WL8TQ8lMo9ZW7xkYvmkgJN2FA_cwA8eQoAliZPRaBHRses2X12OydiBHDeJacNtSfhSbJ1JrXEh2chAxZazrIWJFLzRaAGhQLxKrDCZ_hHyYEri60ng6F5B0YGzhlfJ3FzYujVXXiLs9tUtpNJb8EcJG2ki-rrUt4RPObHZcf9FmidMLTDg_723nSQ8nify9lrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/26122" target="_blank">📅 10:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26121">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=pdI6_3-5GLs_oPRhYg0lk0fbbeOzXAWaW6gJzqhipZbVgfYw8vakHt3q9FiJb_6szG6UlPjeIkuRdZ93OXXn3hATXByA-7P8WO__rbf2A8kaiA-LGWLhyJqI4VkppWxZ7FQK5jQRwT4Q08v39j2XIQgz6n2mKum1MgIjvgAI5gCCWLeBBf2Mwfg0fuV9KAeaAoTVQ4yEY5W5r3G_trgqK7Eq1PS6rg0mLIV4HxyuF2CUl_YWxk7tpPBXbiCfaK9x6SI52dyxYRMw7LTvH1TMp6Nf5nvxuIh5Cd-tKQHXiLlymdvU5fMZuXmuDKezKgdqCN512OlTI7nOGAC2q5p1fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=pdI6_3-5GLs_oPRhYg0lk0fbbeOzXAWaW6gJzqhipZbVgfYw8vakHt3q9FiJb_6szG6UlPjeIkuRdZ93OXXn3hATXByA-7P8WO__rbf2A8kaiA-LGWLhyJqI4VkppWxZ7FQK5jQRwT4Q08v39j2XIQgz6n2mKum1MgIjvgAI5gCCWLeBBf2Mwfg0fuV9KAeaAoTVQ4yEY5W5r3G_trgqK7Eq1PS6rg0mLIV4HxyuF2CUl_YWxk7tpPBXbiCfaK9x6SI52dyxYRMw7LTvH1TMp6Nf5nvxuIh5Cd-tKQHXiLlymdvU5fMZuXmuDKezKgdqCN512OlTI7nOGAC2q5p1fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حماسه‌جدید خیابانی دربرنامه زنده؛ خداحافظی اوس جواد با مسی و میراث مارادونا با شعر مدونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/26121" target="_blank">📅 10:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26120">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=U0gT-FYfVP-g7HvgE6h0x71uBanInd8pxhRc0USPSGM01U7-cbGPf_sWykPJEHHVExhvXuUuKWyuOoclzF_BrXCwwFgx_GXNREFw54KdFIOtSBLSUuzHDvemZFJJSwVdHwvAv9o87DHz68aeYmFQfFxAhvJJ-oTNh7Zp-NGb6LCnfpr1BDRLDLMy34NF-q7k1Zq0lSbSeUw-N7Q94jT32zBPEPguAVf1_Xk2L4uTV0Qrxkgpy5nySFEf8U41DYu_5SnvgnIPp_tLmaQnn7fWvBbbM7i32XU0Edf9grz0aBKVvBV_aCOKSLywQkwXanEV4GnOF5WqM9UUfdFO2QhPWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=U0gT-FYfVP-g7HvgE6h0x71uBanInd8pxhRc0USPSGM01U7-cbGPf_sWykPJEHHVExhvXuUuKWyuOoclzF_BrXCwwFgx_GXNREFw54KdFIOtSBLSUuzHDvemZFJJSwVdHwvAv9o87DHz68aeYmFQfFxAhvJJ-oTNh7Zp-NGb6LCnfpr1BDRLDLMy34NF-q7k1Zq0lSbSeUw-N7Q94jT32zBPEPguAVf1_Xk2L4uTV0Qrxkgpy5nySFEf8U41DYu_5SnvgnIPp_tLmaQnn7fWvBbbM7i32XU0Edf9grz0aBKVvBV_aCOKSLywQkwXanEV4GnOF5WqM9UUfdFO2QhPWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
#تکمیلی؛ اینجا دیگه عادل آن‌فایر میشه و خطاب به قلعه نویی میگه من تو جنگ‌های این یک سال اخیر ازتهران‌تکون‌نخوردم ولی‌تویی‌که خودت هرسری فرار میکردی تو ویلات‌نیا ازاین‌حرفای‌عجیب‌وغریب بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/26120" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26119">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=MA8WmKcC1iba_rYFI2ZHwTiiSHspXibMSpJJnn0-m3woBx4pMyvW0jzYZRz-G2-su0F6s8gd3HfWUEH1IzWMWTVg44U0f5I9TrETsurBsvU70UzYHlCY5QTnKmm922svqD4qmaGO_fLvodtKAZSZpD6NIh8vttrqAJ5xn56lqk_83cYHyDx0B4N0vtiY83jiNulGVzKpXdH4sFrRN2H8Nrku-gz3xXYJw6PoVtkftqTXo0bjVJrZgV3ce4AuUoOwfyDyLylHut8NJQ-WDBWlzwH2Sev505NGo2JxPZKeSavAzKzT6KXLaK0GDxWKfjFhWegFj9kT4TppconbECCoFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=MA8WmKcC1iba_rYFI2ZHwTiiSHspXibMSpJJnn0-m3woBx4pMyvW0jzYZRz-G2-su0F6s8gd3HfWUEH1IzWMWTVg44U0f5I9TrETsurBsvU70UzYHlCY5QTnKmm922svqD4qmaGO_fLvodtKAZSZpD6NIh8vttrqAJ5xn56lqk_83cYHyDx0B4N0vtiY83jiNulGVzKpXdH4sFrRN2H8Nrku-gz3xXYJw6PoVtkftqTXo0bjVJrZgV3ce4AuUoOwfyDyLylHut8NJQ-WDBWlzwH2Sev505NGo2JxPZKeSavAzKzT6KXLaK0GDxWKfjFhWegFj9kT4TppconbECCoFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/26119" target="_blank">📅 03:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26118">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=BtEM1AvtgX8wwaRje-tFdXEEg2OlhxgkEYweG7en48h8gUYbHLtydvEoD_cfxzp4G3zkg1fhjzdbDgZAzEMlWpF1bnko59IKKAZCv0ZXtsppV7-8mZJqcWd-Oz8x8Ycqd78XJX6RNv2ITuch0PXHy6Ns41hMXrYcCbbglqMqNgQwx5Txlwfj8UlOYeYEAVI_7sldUriOXgkA0ZB1iGC-AbEjj5N3sEvQUeEPUR-msZcKJSRynWMhlOMr5nHZck1Zl1faWullMr5wPExCIQ3L_mZRml5-b4fN_eXVxuj-prLvaYlOWClJXbEnKlL9AWP9KWUyQbANOIewMWS5eNQGjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=BtEM1AvtgX8wwaRje-tFdXEEg2OlhxgkEYweG7en48h8gUYbHLtydvEoD_cfxzp4G3zkg1fhjzdbDgZAzEMlWpF1bnko59IKKAZCv0ZXtsppV7-8mZJqcWd-Oz8x8Ycqd78XJX6RNv2ITuch0PXHy6Ns41hMXrYcCbbglqMqNgQwx5Txlwfj8UlOYeYEAVI_7sldUriOXgkA0ZB1iGC-AbEjj5N3sEvQUeEPUR-msZcKJSRynWMhlOMr5nHZck1Zl1faWullMr5wPExCIQ3L_mZRml5-b4fN_eXVxuj-prLvaYlOWClJXbEnKlL9AWP9KWUyQbANOIewMWS5eNQGjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/26118" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26117">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=iUgniqkKsoqAs9DZ0JUgHCPTdDeDr3uJhiBaFd1BlIOKsXKLh9UoTl5xZMD-APD6Qzr-H5Y4YSNcPN_1zEuOjO7XCiGXLimPqlbukMPrkWCnO2x66eYgA1nTZFTKaci_lMPGoNyrQd-3hlmtNQxYUtqozFP7jjhK-nyPFVXno4OqSoImILJHMixg3jJ32KRlZUtOv_FCBP335AU95CdtQsB4zHOay-oRaxOTMMn8vEbezv6WfpU3-jui66LJAoBcAUZNm3Mt3b5VBH_T7O5CSymmrZDJd7H74vwWkG_W1qe44njkY6CSQ288LbXexd2s1Gv5ZrqYzhzBP9sSXzIKLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=iUgniqkKsoqAs9DZ0JUgHCPTdDeDr3uJhiBaFd1BlIOKsXKLh9UoTl5xZMD-APD6Qzr-H5Y4YSNcPN_1zEuOjO7XCiGXLimPqlbukMPrkWCnO2x66eYgA1nTZFTKaci_lMPGoNyrQd-3hlmtNQxYUtqozFP7jjhK-nyPFVXno4OqSoImILJHMixg3jJ32KRlZUtOv_FCBP335AU95CdtQsB4zHOay-oRaxOTMMn8vEbezv6WfpU3-jui66LJAoBcAUZNm3Mt3b5VBH_T7O5CSymmrZDJd7H74vwWkG_W1qe44njkY6CSQ288LbXexd2s1Gv5ZrqYzhzBP9sSXzIKLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/26117" target="_blank">📅 02:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26116">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=Ye2-H6nvxnxTC0D5ralhSTYowkO3X9NVtfxL7qSTC3UGSfzAOcxahylEguuYiM4cLNkX-SF9aBpxMatJg8PforC4dVUJueZ0uIY0s3Vglocxk0MERyjdF_tCSMQDJki9Q_NhE8i4MD8Wy3a9GFlQ5b1lBNjuHdbyskJH9sglbi85fBTzjeHhtOsL4X93WedPRGpm13USUIEXaPwra_i_Yhe5bE_md31_GohMFx2S2GXocyJm-NalQmWKvUmQQSb3-Fr3OPbPFoSAV8TAzYutij1F0ZFZuMZ06Fk_tmLjwkKKnDWxmUjdzJ0txFCGzI22nQlp5oDtelvQHdkkr-UKFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=Ye2-H6nvxnxTC0D5ralhSTYowkO3X9NVtfxL7qSTC3UGSfzAOcxahylEguuYiM4cLNkX-SF9aBpxMatJg8PforC4dVUJueZ0uIY0s3Vglocxk0MERyjdF_tCSMQDJki9Q_NhE8i4MD8Wy3a9GFlQ5b1lBNjuHdbyskJH9sglbi85fBTzjeHhtOsL4X93WedPRGpm13USUIEXaPwra_i_Yhe5bE_md31_GohMFx2S2GXocyJm-NalQmWKvUmQQSb3-Fr3OPbPFoSAV8TAzYutij1F0ZFZuMZ06Fk_tmLjwkKKnDWxmUjdzJ0txFCGzI22nQlp5oDtelvQHdkkr-UKFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:
اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/26116" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26114">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qI9LFeqmAO-K0sPt0_EArkNZffobjr2m4qg3gfYkTCwjC09lqgPVhpuYuXiELwFIOUKE-vlQ1DqilzGB3shvTkSMy2vkSHbGCCyycCSoHTqpoLn5tRQkrvkHrcEC1pGWHc_s7wS164CQicC0bAr8nZv72PNm7NSvAEJ27hrp0wOCoMs1LiTCYBqUleSZbzbE5wnbEfRpXUKmtaPgzveVZTBvitC2AobRH3WFOfWnsFJhoih3o_N97IV35jgydIp4B2EXbQUfIf79itcpKKGZ66wbGI_UbIacCzDCcdDhWygctVh8B2mOMfq09cVBIHcBQjZjCsAb-zgrplX1wu_sRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/26114" target="_blank">📅 02:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26113">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4tRFLishIuQCSb36yaFcM5i-aQgWKs1ChbZVlv5n8f17x3W9vxfo3J6631WiG_b8UXTDtRb57fye2A_qPJ9OqmFUgOYn95Oaapr2VZ-e37jUid1Zfiu97iFrQeQp9B9wd0nIG1n81R4H6fDnOHT5HHKbJpAqAaLhHe6VMwfjfg7hGCOBmXBl4u8D0eEkDKb6zOG9PWBHO6rtTGSOZPAgId5I4Eg9WL9m0bz0pI5iCIU5bXHn9TAlvpXU_WByhCwtA1eHUf2uQWZWwK8KUYsFls21ZNDlwfF9LgNRMN0hFJ1wM9HkkWz5nkyAMFU9LgRY1RXq-kXJ51xOTTgZFes3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/26113" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26112">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWH3_iVTgsbfizoB6iYvplR1P1X6guFSGqIpyxm2jnctb1ZbkeHTWhxJ0bVY7DeJKsSEWkirJSigSb1XX-tHVT4sn02DU3pUOftW0ngM5Iixa1UiMv_zl0g30IyciZUoLNvKi70h-m0-7Nsxr_scyAjyjEtCjkLySUvUBVUjFgtLFlJErCYbgzdpd-sCy7KOc3_ipYmqDNgZrIFOurAAzxDYqvJjE3uHv_gTqN1ecYmH5IxzzqzE-ZwFa_tNRHmgV4-SqqzrOueCp2PI3RtWiCsOkJVKiQwQiQqCf5nRvU1KutHx3FAMZenvgpo5dLm5USGSCLQ9k9uHUYRPKHCLhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/26112" target="_blank">📅 02:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26111">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUBnvGjDUZy0SRLj4tTdG3iCXN7EkFGsoL31S-uuZFrNmd8GkZG1NKkfl0lq3gFUsaYH40WeZJQ1t-KKmrSvqQAxo3BJJgRAP5yTKwwX5BWPBHjFYtBMwZmhm-Ha3guTGge1a_1WIKNqkTZLBbGTvUXnsUnvr9bJc0Xkr93bdx4GSYQD82aaM6MFhizaTtdBQUHHGox0VrVUAb6a19v3OME-XhoSI0w2AnLgz2kIqSuvyTat6_0Uzc7ea2In9K3rE3nS3Uqwd41Wmj0eBr3FMw_P2F3QiAWtuEy63j40YKTmj6bNXPxAwWrlHr9ipEq-ltQJEqtTg8XDWinY0J2d9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با عدم گلزنی لیونل مسی در فینال؛ کیلیان امباپه با 10 گل‌زده آقای گل‌ جام‌جهانی 2026 شد. همچنین امباپه با 22 گل‌زده‌لقب‌بهترین گلزن‌تاریخ رقابت های جام جهانی رو دوره بعدی مسابقات از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/26111" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26110">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c41lE0S-130wzwnO0G_R8j0vPBrcmBh4wzQScf8K0ypfJ_KU-AeKbxlcgF9xn-SdlOvh4icDMZEkoy-NEB5NgR4lUdBJjSgzubtqWRncRoQpuoI_KcTGjQZOGmt5iSxqCvOnaCNzMRNVc9TUGM_-bEGj33C-ina5KgvbbzjaKR1alFzrzhxYybEh4aii0jTzfFifyb09mMeDq079K5tdO0FMFo0BRJFnCHZwdDs3Iv9DIk2_SwOtzvQHN-nmCTA4tzx141KVVI3V2ZuBx6ALORytYTUQTXeluc6zEQ7Cl-yWgtvxFNxOvQEXx8LGNgQa-WJR9p-8lRZ30lvDYnc-mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
پایان جام‌جهانی 2026 باقهرمانی اسپانیایی‌ها و گل نجات‌بخش فران تورس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/26110" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26109">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Im6AqAbk57LE4YnyOsrA0rhUSKS6Q68yW8OQOCGC8Sa6hNu61Rm7GLeVq3-6fflcBYpABQ9ifTeSPwUmunEUGLj5Y1QOE01mZkGjUy24R4eAT0kNTwmymoT6x6quv1U0eM_futSdjWqW6n12-ysoZMBHj4412SWH5DtuQjit1ocFSUbuQY-2m5WPnijfZvV-1I5CdlLcOww79eFUM9fb3DG8xozfqykmrJm5Ox5mD8QPBJ7bLqwSQyfwW4dpdLsK2DWFp1jtnoX3ZcWjoo7bLN__dEWZDMrMY5ZF8GMdSRY6QWFVVFXwmzlRWyF5otMd1ufhJ3niAL8WQqibA08HqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرژانتین وقتی فینال رو به‌اسپانیایی‌ها باخت که دریک رپر کانادایی روبرد آرژانتین شرط بسته بود. او در این جام جهانی روی هم 10 میلیون دلار باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/26109" target="_blank">📅 01:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26108">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_ZEe2x3-X1xiNBsEfUd7UkxOKqBTVlNDjog5uvLGki2vlGfPp9ZhzPWY-wAcBG-NTevFpCRUMVi3o72K9JoE2WEj4tp4CpE6zlufV7P26FEzMQURMeqYimmjWmv3zF2k8H8nSieqGtFNYSSXy9IMs8c07cqLTCdar0CL9qWNlj9su7VWIw6Oywj0AzPXl6maNKqM7igqvnawSTsQ9Q6po_JRvnwRS6Qw_xHKWC-gMvypeRKFJ1x9mf1dgb30VVOXXugwPxzhX32cmUImg18ZLHSH7PYs1HFJQ9PPN440sOuMUN57s1X8oKRWGGMBSat7L5kQaMYtqXjTP_06lqPLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید بلینگهام هم اومد:) فینال هم یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/26108" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26106">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrhJ5-y2OvPAdtWM8s16q3qPm2_291WqGmebs82no7WaHBXyPNt9qIgXVuvQq9p0XzeEfIYVChIE94Wmzl9t7qaqX3fq8iAQf2GiyVtg8g7ZdhbAAKo1J89p28CowDh7l-4ziNeJLhlZmmoAT-u8I8HU2Ber4-Pev4QnsB6Ar88MvTlIkVSczUepoKI44b1xaIiKV3JGB_aCbqejIAVf0dQCyCGH5KAILqY-x1Vs4W_cHkhTrPYTImQxZ_tSnZRz2a0y63RzKCbALtBaq5VHTpkBtG9dlR6XCSRCFosshIhIZBBu6h-qRr67_-5UTe9oig6kxtamwLzqtmAJ5MSQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/26106" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26105">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrBnz7Pbv3eKw0u7chpHY8yPzmsKvVMbwS2ecA4kFTki2JnNAdddSs_vvpC1Yf6JNmRbFDDpwDJLOF2o_VIXdJh_sXG5uly3iOjFb1OYN9d7KHA3XoPmPl58K930N_-UNHHwU-sJBmQkFFFU8zCQ-SReyusaxC18sqQQC4h5-6gqVvmPaYpueygmlTeBxsvMfPSSVFbvp78PPGTbSQFvesrsxfBSCsFcn89pjjNgZlyrTJNecLUapgaaeIWnwGrfdAFdTxm4CbYEt8H0Vl6oknNuAv_UVKZsweZ7WmHV_udUmaOYBS3zRv0te4NH5OHiiOUSVhZuKlBwyqpng95nWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26105" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26104">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuHMt4U9y2RKoxbC05HfRrf0_bIBgtL4mEybkSnW7x2jZR5k6NqlUhN9FyH1_qI2K_O_9Dpeey5SDG7Vn4PpdJUdH0Qku41RZFZ47V5nUNRl3Zqk96bzWRXGYU77mSO2rN1ZC9yK2fmpo-hbPaltrepgRy4_2PyDcr-B1Me6xkb59zA6qAkBlJZzk5JINwsAdzRJ1Gg49bc1n2gL2JG4NXH_O5GGFjjqi6OPOsLl0H-RNNW2YBw9xzgCBfleBzftmF4-kiHCpqzyPJ2uVeid7x49wAtom9tlOihEB4Ca7JMiuERahNNPN9LbeXV9YjQ4pwA_QcagPGnYsr7jTl3XFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بعداز 12 سیو بالاخره‌مارتینز تسلیم‌شد؛ گل اول اسپانیا به آرژانتین توسط فران تورس در دقیقه 108
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/26104" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26103">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=c1g49SJsgipNbHKZUJAfIh2AxZVbwhiAZPrppyuZ9qjtJQrWHPIULc6xPoDMooPJJAMPOeHEabL6m-ceEV8H1mDqHdrWzGS0g84RwawHjLJzuuHHF_78ertufH_UAHLxBjsVy97-UpqUPHaDfMGyKX9Q5CjiuCDwvWFgb92r6Pa2wrmMKLWT6RZTDPzB3IpwWAqZRPOBpI20wbsdHzsXjHaXNJ9bLuouMr5tVTJOFXeAHYnLScePNgHKHARpA3e_-j-9tWsxXTt1GgB0YXnXdIPjPRYWMIZSZi9a2JtvjjjoAoOW-HvR5gPLG6GIr2D322-DYl0wnuOfbufPlmovQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=c1g49SJsgipNbHKZUJAfIh2AxZVbwhiAZPrppyuZ9qjtJQrWHPIULc6xPoDMooPJJAMPOeHEabL6m-ceEV8H1mDqHdrWzGS0g84RwawHjLJzuuHHF_78ertufH_UAHLxBjsVy97-UpqUPHaDfMGyKX9Q5CjiuCDwvWFgb92r6Pa2wrmMKLWT6RZTDPzB3IpwWAqZRPOBpI20wbsdHzsXjHaXNJ9bLuouMr5tVTJOFXeAHYnLScePNgHKHARpA3e_-j-9tWsxXTt1GgB0YXnXdIPjPRYWMIZSZi9a2JtvjjjoAoOW-HvR5gPLG6GIr2D322-DYl0wnuOfbufPlmovQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/26103" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26102">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlrHjr9DTZ8KlkRuk6JU3-Njfua6UQvDJHZ8a0zP4cbNZkomR6_0F3lkvoz2YGLYuYySoiPyCzhwXtYnpPIXBZkTLhErovFGGMmvkgo_usEnyV3btTrxzFcE6VUxk0N9-7t_YVReqUwXmgeyMBdKdySRvI8SO5l2a36g2IrJ-g5a8ypN78M23kCyVcD2bh1mvgy3rG2y3q3Cy4Z2VyorUOYEoa6mRQGMZArlHi2IxCFeNg6vZj-IW6e8zDkEQbALPCwp-z7G7k-Z_ClL7_IRk31cH-K_RXaLma3nvvwqbR8pk9-TxL_zRVItDU0OxvUrROld1whN-p-CP-fqwcfNZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
ارزانترین بلیط برای فینال جام جهانی ۴۴۵۱ دلار و گرانترین آن ۱۸۸,۸۰۳ دلار قیمت خورده است. به‌عبارتی ارزانترین : ۸۴۱ میلیون تومان و گرانترین: ۳۵ میلیارد تومان و ۶۸۳ میلیون تومان ناقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/26102" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26100">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DxegBBMuFxmnc4yaHLJgbFi2Az4EuLpZlQLgt3U7yCWtNZpde6sQOMozeVl02VlYuvSSdqDOZne9xwjeEeZaajBj58sMsMJfrBE2fI8LE9i1J22s1KaiTY9sK1z49Eu64ZTyBoT5pIzTwrpnR_8RXRwFGPX8YqPjWRFZf_AeH2FybeJ_LD92ERzG4PgEHbNk0FUxbJ5dZ8LSfMnOjB_AGWF6Vuw1eXDp4cL7_arfvP9d0Y2FChG-O3Is8wU_OPfitXZy3-DayMRM316htlpbPMkWtNdcgETuKBCW2ue8tSvqXYg1dwqVi4NkDlYjT_iE5ya_pEkvoyHGKKBDSS_oQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qaqd0ggb5bnqYE6HEVE5oWfsAtF-C7oD49gTvHt_lmxvDTSmdid39VNH1eUef4JRNqbVZzyAyrPDXDZ-t6oMrP3D3NfKqqN_zMJN7XCl-UhVNGGfyo6m_8vSZKBfDldAcihlxo1YYaAmkdVjw2swrT6og6gcDBIOSgSpGeYKahoD11BoUmPPUt7co3DBqJNxQ570JYLqiSGIFLyW0i3WJhaxGSjMiWOeNwAzgq6PBOs98uGBHLnnAPZH-jPVwGNtPpy-3wJtk0vE7SPkqenw4XtTgAwR0Ximwl4P3o8n4rKQkZZ1-riIs948Sj7PvlHeBZjm-Npnugic2xTQIFdLmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
ملکهٔ آیندهٔ کشور اسپانیا به‌تازگی به‌ طور رسمی سه‌سال‌آموزش‌نظامی خود را به پایان رسانده است؛ ازش پرسیدن هنوزهم به گاوی فکر میکنی؟ خندیده گفته دیگه نمیخوام راجب این موضوع حرف بزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/26100" target="_blank">📅 00:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26098">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fqp78ikRzeorITIwnCNmkSzAy2tv1mI7lV-FkfTpBwTlN7PEutStUv-eDWF9r_U5DYIWLvYFE8KxH8igtvSQnsvnFhcZjZyFIfvnGkz5Y1jfiXb0920jxsyeio8h_vrUKgVXjeYXlgfvC0pXoVk4MMcIlaAjiXl9LaKrhkpbji6z8qxrTsa1Xr7rmEBW241c7OwFgwhyRM2leIBJT8N4n2DzEQ0i2MOgRWkQMzqhSJ7eupDdNFxBb_J0FH4CyVE-b4_8KDd8T0rjL6681rpbzXsFFc1TPD241fsfzsdQlWsuozakXX1_PAZQwtijY9etYY95ShwulPsix7XBvLNrog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0hKJ33PYq6JW0iHjPCb9qy-Y0BRjF-6Pv9hinZYhX2Gw9G08iqqHBYGNJRsdhvSHsT7yShfxW8aO8GDyQAVc0Ts36ZYqL5pzICeucB1Jllg5CG4-bEebW-tTPes20GF98htj2jgk7biVknz2C3QjrQBfwuTRv-72UYUiG2Oj7NDmhFhGWMiGVSvDZ1tZk9uTH35Y6J8M_ue382e89JmTD9AxIjYH_4s2xBWhUdeSwsBXVias_W59Z0pYJwLv0fEXdyuNIgF00bpCJOPCwf9FqEdaaTNQSxRQWrdZ59Oq3eMRwy6JMSI5Ff1vjxe7Twf1r3VnaSevjmxaUMIfVCxcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ویدیو کامل اجرای بین دو نیم فینال جام جهانی با حضور شکیرا و بیژن مرتضوی؛ عالی بود ببینید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/26098" target="_blank">📅 00:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26097">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🏆
لحظاتی کوتاه و جذاب از اجرای امشب شکیرا خواننده کلمبیایی درمراسم بین‌دونیمه بازی فینال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/26097" target="_blank">📅 23:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26096">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=Yz1ctfjtYNexzaBNGxog0-zCdEzGocLnbi08JNqzztA_PSlYyjPdEPyHYMfuUUOYEZ6IfuAI35BvF3gOZSHisoVhyn-XK1lbGNrY9CyimSIQFZ-Fi9Jgib0ux_4c-HBLIJarU7eGEuYrk6O7tp0nAImoxGPln1Ij_9gsTIDX68at1XNyTG281SfGfn4F5YHHRevB2XYF8WUTO-dVm5h9qwPF8Or2KZ7ityDEF-JgKEyXYC1ZXsRuxztWttfShrN_PkE_uIa6KwX3IHYFyc0OCTN9OGjkjCk3uWhTunGEqygqQ0CNFCBrjET2uSOPWh4PU8iBt2r9zLeuZKyv-RHKeLiq9ObEGO6uOu0Yy7GOS4S6_IuqaWyyV8YyUt1LwWPD1PE9nCP2wF40RqasBqCCtrLF-qSsR_y3qASHfFg0TRVJ4EMlRMgHbbp2xdOTb-Y6eKO_xqGD3m60smLPiM4ljDSfkwJDaCJFiD7sb0T3HP6c61l80cSFejf0K7zRKu2-EfI3nxlAvxmRHOKJv5fT76I_jx5tq17TkukADvjF3prshSp7b_7hI4_WDqconnUaNE4e2oBzLomYcumjdL5HsKy_CZaOmb5GtowtARx4oo5rEP9pd9DCHu98BB7V2CKxzqdakVkrlVz1fSaODYOxEB5RgT9T0Ni8mh8c-PA9GO0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=Yz1ctfjtYNexzaBNGxog0-zCdEzGocLnbi08JNqzztA_PSlYyjPdEPyHYMfuUUOYEZ6IfuAI35BvF3gOZSHisoVhyn-XK1lbGNrY9CyimSIQFZ-Fi9Jgib0ux_4c-HBLIJarU7eGEuYrk6O7tp0nAImoxGPln1Ij_9gsTIDX68at1XNyTG281SfGfn4F5YHHRevB2XYF8WUTO-dVm5h9qwPF8Or2KZ7ityDEF-JgKEyXYC1ZXsRuxztWttfShrN_PkE_uIa6KwX3IHYFyc0OCTN9OGjkjCk3uWhTunGEqygqQ0CNFCBrjET2uSOPWh4PU8iBt2r9zLeuZKyv-RHKeLiq9ObEGO6uOu0Yy7GOS4S6_IuqaWyyV8YyUt1LwWPD1PE9nCP2wF40RqasBqCCtrLF-qSsR_y3qASHfFg0TRVJ4EMlRMgHbbp2xdOTb-Y6eKO_xqGD3m60smLPiM4ljDSfkwJDaCJFiD7sb0T3HP6c61l80cSFejf0K7zRKu2-EfI3nxlAvxmRHOKJv5fT76I_jx5tq17TkukADvjF3prshSp7b_7hI4_WDqconnUaNE4e2oBzLomYcumjdL5HsKy_CZaOmb5GtowtARx4oo5rEP9pd9DCHu98BB7V2CKxzqdakVkrlVz1fSaODYOxEB5RgT9T0Ni8mh8c-PA9GO0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
این هم ویدیو زیبا اجرای بیژن مرتضوی افتخار ایرانی ها در بین دو نیمه فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/26096" target="_blank">📅 23:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26095">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=TLAbjhs7f9R3CKy_4sAtquvrqH4KxBPo2g4zJqZ0KnFz-NoIjEH6LwwjVzO8loCpbzkjAsjBvnG81UcUIibM1oG7qv9E7dND5ir7r4-Vx2qKRMZkyR_OjftjOAqhJvJK4P9pXutkU42uVPi6i4bHTxgx7WJSfPc3yaoXMd5Ives-rBa7BS2TnuMZfNngNpQSGRXO6B6AzlB89C9xzQ2E7ff3XegVyzvibJ7zk0AiY8s07n1MdgMgvuip-X5auFGdNDLI7LrI0634Q-N7HHmHo6jrWBURWK6HVNWGDQf3NJpQk1J12PAJnhKkTLYOtxfbEmC9FmETzoU7S9gXt-LfuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=TLAbjhs7f9R3CKy_4sAtquvrqH4KxBPo2g4zJqZ0KnFz-NoIjEH6LwwjVzO8loCpbzkjAsjBvnG81UcUIibM1oG7qv9E7dND5ir7r4-Vx2qKRMZkyR_OjftjOAqhJvJK4P9pXutkU42uVPi6i4bHTxgx7WJSfPc3yaoXMd5Ives-rBa7BS2TnuMZfNngNpQSGRXO6B6AzlB89C9xzQ2E7ff3XegVyzvibJ7zk0AiY8s07n1MdgMgvuip-X5auFGdNDLI7LrI0634Q-N7HHmHo6jrWBURWK6HVNWGDQf3NJpQk1J12PAJnhKkTLYOtxfbEmC9FmETzoU7S9gXt-LfuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اجرای شکیرا همین الان شروع شد؛ بزنید شبکه پرشیانا اسپورت نگاه کنید. ویدیو کامل مراسم براتون میزاریم که ببینید. نمیزاریم چیزی از دستتون بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/26095" target="_blank">📅 23:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26094">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwz038Tj-Rbn-aJYkzYvfuhY1rkps1K9EW_uDTecphzHafEWap3iEthHNgSsG2WfNm93CNGgvh9P6EdcMRzB2FQh84bzQBGtQz0S9AnIgFDKiKy7-chwA-HsdLb7g3A8AGq2ycb_TSRXEWdmpdpo2GTGVfo6uqXyJ7yUSipTsr2VQFypCpW4Q0lCSV8Cgwx5DiTiRErknG252_VIVx_wGbpVG382ygbryHnSLcrH6i3f0eleN9y8beiaoZMN4Xx661YUDAZIYgPasl1_Mq8I5fFmymMuV2x424b1LaGeu0o0BGLFnivx8bcW6ycXP1KuRLsa8BL8dlEOfI-AmRVPQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/26094" target="_blank">📅 23:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26093">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=ozcduTiBMS4Cxf9SEy6V1GtVcrNgGjwndbr6uSc2apOTaUnNSd2PxVRQKTuXgJbhWsyb7T4cV5Q7Qfine7dwutwNJ4Xn8pIPnw86XShb-b6q04lYl2KFVz8G4e4ewoQgtetlCvFT9jaGRdn-H7cYmOkhttZd72hIdsX8NvN_rjMb-dapcHZTVSIl5YGYooFIhL8SQLR3Wa52DkSWAAn2HcOFzkNxpjrYeAt3ub2TfdwRvfynhD_bXiZUS0bu3Zm26EnMbla_UVK-eImZVY7Bz8QIsD-3WY7STW_G8Gaxu3qeuzu-wuN4TmrHrHybNTBVZFDZRX19aD9SbkD7eCxCbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=ozcduTiBMS4Cxf9SEy6V1GtVcrNgGjwndbr6uSc2apOTaUnNSd2PxVRQKTuXgJbhWsyb7T4cV5Q7Qfine7dwutwNJ4Xn8pIPnw86XShb-b6q04lYl2KFVz8G4e4ewoQgtetlCvFT9jaGRdn-H7cYmOkhttZd72hIdsX8NvN_rjMb-dapcHZTVSIl5YGYooFIhL8SQLR3Wa52DkSWAAn2HcOFzkNxpjrYeAt3ub2TfdwRvfynhD_bXiZUS0bu3Zm26EnMbla_UVK-eImZVY7Bz8QIsD-3WY7STW_G8Gaxu3qeuzu-wuN4TmrHrHybNTBVZFDZRX19aD9SbkD7eCxCbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛
عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/26093" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26092">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDDE6CiP9JTujxKJivbsLM7Zg8PA005yKapFfSloRGnBn7OW5r4qywsUas4tEtJE-18aCbSU2z5U6YBvyczP36XjN9NW8XSgFWBxxQmlbmnJGyJzxwcRih3SbKe_WU3B0dekbQqaQp5CS42rE15vWD7MCjQ-zm4Rap1cbUvJkYXF2JlccQqQ6t86MymqPaI7ooHSgVQfNAWlhLl40bX9n1JnJCCbf-tuEVv0De-b2vN3fB61qciyRsh_t-6AOlx0wOFkB3t_oGLPOGmaE97Fwd9LiESoVtWI4nEfMAu85b2AGX5awAawj8iyyk7qvM_pu82FB2NzavnTlc6ub-QTYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تقابل لئو مسی
🆚
لامین یامال بعد از 19 سال؛ لیونل مسی: چقدر بزرگ شدی بچه جون! انگار همین پارسال بود که داشتم تو حموم باسن‌تو میشستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/26092" target="_blank">📅 23:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26091">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVKZHTsvPcJbVSAOUZduvsX8-aqHqsC_zVggOQzcTofnJR5qoUeuZRYGL7UioeSsfQZkDTOAihXV3gTFzs8YicZxNliC9eIXoXk9crhKO0XRjRj0f09uP_myltklu41G3bQ0tzl-4s-L6qM4TCUayKWQEEVJNQJBX9W7z-BOHhZnQKFiNhM4K5M69YJoUC5oNVtB0CG1P6Rl8Q_j28MbU143YbvvcPyU4B0lw3U6n2Z1BpIyvLR5zpKFdSJdhGCLJzN-Qt6D0o8t63qY5pZwtN9OMYnNm9hNQ4XKPBFm5_mesbTzNOm8XLlp9VZdwV0yz1O-Efe69JOAKgvL0VN9eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌فهمیدم CR7 چرا انقدر بچه‌داره؛ جورجینا: من آرژانتینی هستم و تو کل زندگیم طرفدار تیم ملی کشورم بودم و امیدوارم‌امشب آرژانتین قهرمان بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/26091" target="_blank">📅 23:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26090">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🏆
روایت‌جالب فیروز کریمی در ویژه برنامه امشب جام‌جهانی‌از غش کردن معروفش کنار زمین مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/26090" target="_blank">📅 22:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26089">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=puGFCwoxgcptT7vSd-HQffCyBqZYfjbczoyntti9WfufV41xhIzjfp6Q8QhKkcXNIbsHixDWdUCE0uRlERDf77GyzLsPVlbmADCA_Vkod6AFMxLEc-q4O3Crcg53K9Kwm2KK-klgntfnrxcRTPHiRfHJDb8mvaYfRsgBCZf7EyEtR27CAK8_j4GSszyz6s58QE_4lc3A-22w2c4jl-iH99VruXCq1MToEqpNa4DiAVrOq1eSigtkCcKZ9769c5JNCF3oI1fNBlukBsArsCInuBvQZzFMNwl4Zh54TJDZHStPbENAwUnY4LXzZsTjYK8mo5oSNM2dhU3NOyoQomaklw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=puGFCwoxgcptT7vSd-HQffCyBqZYfjbczoyntti9WfufV41xhIzjfp6Q8QhKkcXNIbsHixDWdUCE0uRlERDf77GyzLsPVlbmADCA_Vkod6AFMxLEc-q4O3Crcg53K9Kwm2KK-klgntfnrxcRTPHiRfHJDb8mvaYfRsgBCZf7EyEtR27CAK8_j4GSszyz6s58QE_4lc3A-22w2c4jl-iH99VruXCq1MToEqpNa4DiAVrOq1eSigtkCcKZ9769c5JNCF3oI1fNBlukBsArsCInuBvQZzFMNwl4Zh54TJDZHStPbENAwUnY4LXzZsTjYK8mo5oSNM2dhU3NOyoQomaklw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/26089" target="_blank">📅 22:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26088">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVCuPFe0zPQgy8VRFbnrNX2lMrdIMQQ9OlcHE5yegvoCigNhED482OT3g6S62KtQZBQlnNJtAk3GXhs-GRrigmAsX76ovd1hSkCTg8OZ1o3Oq0GqpgjY_lh22Echict0NyF6QvBD77Sa8PJ6qRiKxRW3Aci2Q0cJ-4Z0lKmPl98snGlGBHkFvJ_GXieZaeSp9qCkvR0lNMQ3j1Thk_JUA2kl90eL_u53nEOzBlcTxlHCSBon9V0DzurNHK6iV1X_0mVV8dLNPzRzozrxWcTWuotTaDZV6dU4CxYVwhtrbr2FOI_lGWev19FLimAvEYqmh3Kcms9V6kqL9Ni0q5vUCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل رزاپور درصورت جدایی میلاد محمدی.</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/26088" target="_blank">📅 22:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26086">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68101d4663.mp4?token=TF1TUtCqoJMsPsvoONmayMNmfzF4A3OPHP03I8xuUqrW4eDXvktXWiOVtim-RWlQfS49i4LKqtrU3Z6bWakIw879Hs43RRRw3tZJB8-T8I_IspGRMoGkmkdhLM9WMAM3emKjYL3YjhmJ5kigdFLP-sw8W7EdK7E7jRT7ZMlpg81xg2k29fYB8Nt-RQ28zgJOc0snCIFo4Ng5XQ9bPTI-T2_cZ-AOmf3MmpJEt03ng6OYdLi6cxP_MfXohwQL_rPZxwGq-4DxD5L2TbHZgu3Ava2ZmzK0lA51003Igql8qtkKLYGao5dqiKB_IXov0yeSxq3Qn-zpLYeD7EG0eu86XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68101d4663.mp4?token=TF1TUtCqoJMsPsvoONmayMNmfzF4A3OPHP03I8xuUqrW4eDXvktXWiOVtim-RWlQfS49i4LKqtrU3Z6bWakIw879Hs43RRRw3tZJB8-T8I_IspGRMoGkmkdhLM9WMAM3emKjYL3YjhmJ5kigdFLP-sw8W7EdK7E7jRT7ZMlpg81xg2k29fYB8Nt-RQ28zgJOc0snCIFo4Ng5XQ9bPTI-T2_cZ-AOmf3MmpJEt03ng6OYdLi6cxP_MfXohwQL_rPZxwGq-4DxD5L2TbHZgu3Ava2ZmzK0lA51003Igql8qtkKLYGao5dqiKB_IXov0yeSxq3Qn-zpLYeD7EG0eu86XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل‌فردوسی‌پور: سعی کردم تیم ملی رو خیلی منصفانه نقد کنم امااین‌حرف‌که هر کی نقد کنه وطن فروشه نمیره تو کتم هر کاری میخواین بکنید. وقتی اینترنت بین الملل نیست من چجوری میتونم برنامه بسازم. عادل از اوردن اسم قلعه نویی خوداری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26086" target="_blank">📅 21:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26085">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df505731d.mp4?token=CI9U2oEaqtq8li_98ecEuQcVxOiToTbSZzYH7b4z0W_BQuMdGBv2lfSeDNNMQQ_L5SeilWDeQpaVSAZRpBReh9AUd2XrGc-GLXuo-kqAZOrGi4wxtazkfWDm5J661pdiwLY75xICuiTDIP9Rr5JXca9_V575mkRwPujZUrPsrpVQX-ENRMYPH3oDiBE0o5hyvLmM-FK3BwjXJQRqt01N2cg5v6x6tCrgKjRiUI3d8VR9lkNyIiEqXy1yHhyKVeVoV8Z_edjiJzxdFDj7bFZsjN7eM93AoecRnfBgprOipGdz4hHEJIH6cAX0F_b9Sb9Rk1hVbHo49C4DcuYvvND29Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df505731d.mp4?token=CI9U2oEaqtq8li_98ecEuQcVxOiToTbSZzYH7b4z0W_BQuMdGBv2lfSeDNNMQQ_L5SeilWDeQpaVSAZRpBReh9AUd2XrGc-GLXuo-kqAZOrGi4wxtazkfWDm5J661pdiwLY75xICuiTDIP9Rr5JXca9_V575mkRwPujZUrPsrpVQX-ENRMYPH3oDiBE0o5hyvLmM-FK3BwjXJQRqt01N2cg5v6x6tCrgKjRiUI3d8VR9lkNyIiEqXy1yHhyKVeVoV8Z_edjiJzxdFDj7bFZsjN7eM93AoecRnfBgprOipGdz4hHEJIH6cAX0F_b9Sb9Rk1hVbHo49C4DcuYvvND29Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی تو این دو ویدیو به بد ترین شکل ممکن‌جواب‌صحبت‌های‌قلعه‌نویی رو داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26085" target="_blank">📅 21:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26084">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDGoEOhUoJSpSME0D2rdedMVqW87dMz7QwoFdsNUMY2U56RXVwkJMnXupD4dD1FvNx7RSGhqAVUzegooSl6r9FBW7p6H3UDR5cxbfsAndEelwvJPmSZxsD29NRqJvCh_QDOz2QhwMfR3LfN1kvnM8uc6iQ4b0N-vrzPZdzkPLXdoy9mvkFDLtxnDcjcFar3kwmynMTGTmQETBhOyTr8USH_MOunqwNTDSZsihooMkSTlGBNQClj7tFR2tG13zYE-h8UiLIUODi2Jw32ctYAbVh_KMLrD5B6PgDsCGGBStXm_NgHi6lkS5N1JczqSD4Aa1KsHP1LQMJNc31W5SAslYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26084" target="_blank">📅 21:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26083">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=aYhi3Jr4-Ih6txcTRNPnMyv5koIprarESbuZ1ARiFaJjCLWwIw5zf8kjnFK_b37zZ2VgXASWt1UbXGaY2LetXdTZeboI6xM2za1IkmLSAm1cNA_LuYJtnvgYP9r0bhUHtGjkvhQJLHGPXXKjjHIOVFcWyVvuTl3x_4vcGluM6Tm80f1lIAN_LZM4k7gxBG__tWhQEP0F3Ebis0LSW0lvmctIFnSnWvV5RpFCt4p1hzOZC1LtrwJ8Hp919y06mbWw2M3jSPk-wi-H7LaQP8s8_410Aco4tyOwn3tWL7TxHgI4-WQ-KvprYeNr_7n-AF2Ps7n6sVadMpNgaJ-pRCtM6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=aYhi3Jr4-Ih6txcTRNPnMyv5koIprarESbuZ1ARiFaJjCLWwIw5zf8kjnFK_b37zZ2VgXASWt1UbXGaY2LetXdTZeboI6xM2za1IkmLSAm1cNA_LuYJtnvgYP9r0bhUHtGjkvhQJLHGPXXKjjHIOVFcWyVvuTl3x_4vcGluM6Tm80f1lIAN_LZM4k7gxBG__tWhQEP0F3Ebis0LSW0lvmctIFnSnWvV5RpFCt4p1hzOZC1LtrwJ8Hp919y06mbWw2M3jSPk-wi-H7LaQP8s8_410Aco4tyOwn3tWL7TxHgI4-WQ-KvprYeNr_7n-AF2Ps7n6sVadMpNgaJ-pRCtM6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26083" target="_blank">📅 21:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26081">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
کنایه‌قلعه‌نویی‌به‌علی‌دایی: ساعت‌بستن و کت و شلوار پوشیدن نشانه شخصیت منه. اگر لباس یقه باز بپوشم و زنجیر طلا بیندازم میشوم مربی خوب؟!
‼️
همچنین قلعه نویی از مسئولان جمهوری اسلامی خواسته که مانع پخش برنامه عادل شود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26081" target="_blank">📅 20:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26079">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a_90qIQinPp6Vg07PN9-wkIGarUbq-UFT3eZeCzfU5S1Bt0D0QHB7QmE7Jp9OGNaeQfqWbDWhocH-FAQGH-Bm7mtaD02ccOpk85ESew8NjcYdovm908GID-AGot9UP-_OHtpFB8crO-kWTIjgAKrg0Pb2jxicEniTPiw9T536fVFdRrBJQqFcAvoaUJ2j1YdU9JcEt6hQ_D0A3aYqkVNRkpBRX7mIXVWGdbzSaX7tlXJTxsFyZXsmVcchU2uw4BDWgfKsA8B8_dAdMo1tRUB8AOOEYDGdf4imfBw7n_MjnlLiCM-ME2uaB9H1pAKlpn6-t5DopEDzKlfrnWd0mm8tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cnAzAcYqJqAh7rRTYAQ9_rmRo-zUxyAjLtZLlhhcOA63kuqTFAl3_kgYovx5jzIZMusG1l_11VkLVp0wRTGd0jnIWVmfYofKBB48R2z20_W7_AEz4iCY9Alf1c4xyUKR72x0Xa0XHolYpcSxl_1ZUzhYQTC6ILrbTudwHQHhenlw36tVdbR5ORzBG7zIhawctAZPpIt8YBN5waxpmwj6QlAyb_RqPBzXLKrUdikgZEcRBRgXXJVc7v-yVRBDQuDnu5lYbgNphGRzs7LToD-FqEwdqyNbcpWrRn4jpZ3YRqd2diok57PsGFYYKUJE5-Nd9KGNHtasyCen9IcrRQ0Zsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026
؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26079" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26078">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRmyarA08SOCK9ADG7LE1KmmJV2htidzKs7GPd8fm3sOrpe7ArTWCcT_ymaDfD28dZfsc6zh18GElhOAyxGBwLmBSKen96TKluPlN5Y6OlSk9XxJ3X2D3KAJ4ri_NXoSReermYAIKKlJZxPUJTx-V4bhVuH2aqhbAdChcstT_t9l_Vg5dpWr55amLBJndjRxvR6IBuiZHIw2SF5HxtRz3AIjrd9y1b8kfc_Q5S_tWhlL_RTacXL-o06lxdWaW7e35lWrHmKxGJRYGBCELdacgPMYbYIV1RH3sk7E4r4C1FZ4gT4KVj1tKUO_VMqN9vpWpYizF_b5PGJ0MyyVdnMlig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26078" target="_blank">📅 20:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26077">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMCRlutjmNMaMVI-fp4Mso9Si8sIKa0ITtQDNG5hdGRsleFhxCMcyLe304_Y-t_nTd_v_ByvZTD3eiudP1Um3OgTDc2M2b4uW4r5i3473SM3rSgUP0ehgIRo9FVd1rEtrvNwU-zwqyc2whiIEl7RP6MQYK_8u67OAASKPkcLR5dlpF3l-Dv70V4043s4RxWrjz5APk_Tq3wfh-l_DyS00Vcu6EuOWlQ3n06td3DC4dBpmXsrJu3-ZI7iuvX0kbI58ezds7nMTXCnNdGMZtWmVjYf83G1WoE8amS4BGWu4Epr14XNFV2Qy8mlqfBg6-3aIZn3TgnVCzhJFe-LxviTYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/26077" target="_blank">📅 20:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26076">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSE3tXD5PfpVfXPHViZZ1hb5cSOVHPfkN6yi4H2P8s-Mp_yU8x2KtmGE_GVPil6COoAV3BZRxGBqu7R4Qn6I2SmkYpXIZuYCB8zp6NIFCn5Xj5b0ON0bpdnlmziY69pSkwNkfHo8wBQyZ-Hkibg_007EvFIINuHRLPpT0sO4V0UrTj6qsdl6NiPrqvLnp_pMRqATC1ZAFmkBnMb4I82pI6aQpRgqterWBTwJ2sHiRfAn5zo_BzRygU0cFD7Rgdf7ZLU82-XsF0ovODxRaz6p3hCtxhPk2ooG_QpywptcjJ_f5sLg70P-9PypYMKdgMwxK2CzR1tyj7C31lKTOE0j4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
خداداد عزیزی سرپرست باشگاه تراکتور: تراکتور بزوی پنج خرید بسیار بزرگ خواهد داشت. 3 تا از این 5 بازیکن لژیونر هستند و سابق بازی در دوتیم‌ پرسپولیس و استقلال روکارنامه خود دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26076" target="_blank">📅 20:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26075">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jX5u_ks5dcZakGaTQ3f96pFgZbJ5cl_kXiSLqQUrnUTzJmA6s9txufG3EuO75PwvSP-79DKVZEJZcM2EHt8KpeIJCLaoPGOp2Lo0IJRy9Z6MK3gjGo0gpKOo_lwbu_QBjSVKqGRjPNHtTQD_CheHqD2j3QQ92jMdPEkM-12JNrRHMVUvoPbLX_DEenCF5f6MIyl8AyVRDiiJTTVG_47OVv9fEF-6-ZArhPbUxxDMIq57HVEQS5cFZX7emanpZbU92c6D1bEaYlz20lr2zRAp-NvFCOkkWsbASRjh72LMifB7X-4NlhWl-NLcGZXepX7uxKMRywWCzY4Noip8CKbmmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26075" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26074">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJd5cCOq9ZjEjPBzy6U1p9AGEZaJHoeJV0-IGMs94982wb5ejySkLQ9v3YAvGEnt4TdhTrfnh1W0OIUmc2U3_5BJp4jjbmr6cwWWO05Vk-I3tZvC6qugOv6xH4_Gc5qf5z4Nz5SqEKn65tN9VVGr2yXUuw-HxrecJIIlez5pdBwrz3-qGoRQ3b9GlqdiK5glwRi0nKsjGYLKNjfNqhe4f-sUkqKJvf0r6x52H9486p9X0UbzlkaBBhKGTyRAJwcJSESNW6uhauD6inYN8So-sm4bWC-qSPPkt9Ql7nyO-2eU6HmQFLppSUDQ8W4wccTJv0javuJdfbu1Q1SZzhle5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
علی دایی بهترین میانگین گل ملی در مقایسه با کریس‌رونالدو و لیونل‌مسی دو اسطوره فوتبال دنیا؛ بعضی رکوردها شکسته میشوند، اما بعضی از نام‌ها برای همیشه در تاریخ بشر به نیکی می‌مانند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26074" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26073">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgaPfOcA9HOy5mjVwdGbK54DkBTJV1aYl8DVEBlVF3MzC9u3RNA-CGsGqk7RQBoI-c14Wjsi0NlHLCAXmb0p6l01L6kC05L_mUV9RlXI1NGjot_JRUSeTHYTgekVNH-l4q-5niXupXo3844FKpSjFwxNenpHDC1Tr-1fbwOlz4VIgFTezjVvT0-w9KtJ2uW9GFJaqOf0Bsr213ZELeA_62bdNwh2eWOBZNFCrOBzyS3qEvuJ8HUpQM5vnZU9LWzcWewyrGhpKRTVT40GoQf9LCz2pp92ez_y0fEsVhYe6dMSqhzgGOIrWZws9O2-vAd-CB0_d1ah5tKJOszjSr6Aow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
آرژانتین
🆚
🇪🇸
اسپانیا
📅
یکشنبه ۲۸ تیر ۱۴۰۵
🕥
ساعت ۲۲:۳۰
🎁
۷۰۰ دلار جایزه
به صورت
FreeBet
بین برندگان واجد شرایط تقسیم می‌شود.
📶
علاوه بر آن،
۱ گیگ اینترنت یک‌ماهه
نیز به برندگان واجد شرایط تعلق می‌گیرد.
✨
همین حالا پیش‌بینی خودت را ثبت کن و شانس خودت را برای کسب جایزه امتحان کن
https://t.me/betegram_bot?start=p10_r4EF37DCE</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/26073" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26072">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7FgfDSHJPN2cZppvt8T1iRH95lto5rgm02q849N3J5A9x2LfQLEglHnh8mDkV7ZqFY8cC9UHkw_KwAPc2GJPO1SrYeXaUOJhZtON9gPpGsKgiN-ppIzb9ogGkJUmNsAjkEEpnrYcK8aXc8IjpbvykBepZT4ORr2-dAXvCDjnKJUA2SLymBxqmh-rmEgndpnrkzSBImBgj1hW9YiAKPRsrYmxN0GUBl4HaM7_Q5CEeyVVKyihUkO62ZOAZVuEs3_5_8XZ27SCT-Yy6LEnFndx1yVYdFzebNlufRCCbYxwQFf34j4so6_u8AlZOer3Q4Bij6vXeEfP7J6rdCC8skBTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:
عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26072" target="_blank">📅 19:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26071">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCiShKAuVHvPnloWd7Qbc8XTLgt5qONMWoX_az4N44VTXOe4N5Y4el3OUf5kcSmE_w9BEMQ0-t8tcsDjj-7kVUiFU0mJ-aH_F29xnqYUlw4cjIcpFS3TqNqCJKjGMdnMM-X8Nk7-Z7t7HO37FOXt9k4dl4wAVGOQV96CS-fMhMq5LQBSTUP96hsSix7eu-iN8abErO4Zy1mhHzDkLcLt_qdgbkwfZuoX8p9PvNbXUk8jXyrkj4Q8ek6l_cIy6rt2naXlWPBE26LO8l9kCvIAW5U5mLh4HeT76IjaD3XSI9FaBotKv_nDIRgoESl4Q7vkzVH5RR6Zxa71U3S4VNws4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26071" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26069">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=SgxWXqTrNaZYdzpUJnTDLdc8p4DmYuaGSrnzs7lSCZLvZlS3ZHZxlIvXE3i4X8vLFd2o0T93gDGJQvJNVRd6CJcb6azmOG5Uk22KwbJpB3q_JQdppJaPcGw_V1A8sE_sk5_h7vfZmJupCBy6nCxkv8v6ls_HjFqauTBjlzSY-EPWw6QZCNJ5s-b6RB2vmVYf09GqOc9dO22qa4wa1fu6INMHTcfpGoF2y2JcX4FBOyMFXAADSxrMNCciR3iIjmL5YbsSnW2NYBPe3_hbL6JFf_xjrtstUkASS9vW7x33jRPVdI72H1QxbN0F8-TSy9h3gP05ZlfExsTEGItllM491g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=SgxWXqTrNaZYdzpUJnTDLdc8p4DmYuaGSrnzs7lSCZLvZlS3ZHZxlIvXE3i4X8vLFd2o0T93gDGJQvJNVRd6CJcb6azmOG5Uk22KwbJpB3q_JQdppJaPcGw_V1A8sE_sk5_h7vfZmJupCBy6nCxkv8v6ls_HjFqauTBjlzSY-EPWw6QZCNJ5s-b6RB2vmVYf09GqOc9dO22qa4wa1fu6INMHTcfpGoF2y2JcX4FBOyMFXAADSxrMNCciR3iIjmL5YbsSnW2NYBPe3_hbL6JFf_xjrtstUkASS9vW7x33jRPVdI72H1QxbN0F8-TSy9h3gP05ZlfExsTEGItllM491g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26069" target="_blank">📅 18:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26068">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goqQZ9tT9fkDFW91Ny0WGH9PaPaZxUBIPAZJnJqQaseMBBMBeuRChswCzJa9yvVPVnA2Bafwf5bNkEJGz9p0fGW1vvGTPp9MGyN8t_gvfKrsOYjl9TLb556-W5H9AgxVkrkwkNMSUV7YdESOx1qIybX0d1liyL5b639erSb9FdTq-oDY1TcCi7ej3QJXPV7LvZKT8M6T7onNwkxzuXORz-ewIEXZTF1XPaR8O1C6KWVIy7p9hizcYuVMdhyhsYfVePiX_-XbciozAc7XxvN-KMEW3Ofhl6FpRB7lWXaV5lpZYWY3Qu0m6ft-jpySSFyL7pDNSlaQ1wS08u2oMk7vgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در دو جام جهانی گذشته؛ تیمی که در مرحله حذفی با نتیجه ۲ - ۱ انگلیسی‌ها رو شکست داده در نهایت درفینال‌باخته. این اتفاق برای کرواسی ۲۰۱۸ و فرانسه (۲۰۲۲) افتاد. در این جام جهانی، آرژانتین در نیمه‌نهایی انگلیس رو با نتیجه ۲-۱ شکست داد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26068" target="_blank">📅 18:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26067">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJNvFs_a1hFwCjzFohgf-SFeVcAgEnEASleLn6oXjPUQbHCE56TgG1D9PqDH2K2CIZk389Vb8ur8wS85Al6w_phFlgljaTW66-drvlgtw852OR3GDMBWRu8u17QplWCz5nVL8pf9FSgcMe0-VC-Gh_SylgxbEK93ZUOd8tQeTTqj3luAMldGFmhvnN80PNM9sFR5wSlIuQd7nx3Yov7i1NWiE03qTfUF_424IdlrrDiflpRsY6eENSL3NBYHTQA6n7avO2a-9p8_a5xaxy8u-zF7mwaCs9U2e8ktjmtVZMFpSnjCeSPd0tLVqrtdu4wj-iNQE_q9CIG16PBWY7GtBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26067" target="_blank">📅 18:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26066">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UL9boxpaPpAn5nz_VoDeoQwcs3ylw2W3_TeGYUlqENygX7bXXOz_-iBIyFmuQg9zrmj6X_UU6vvlzSwsGG-zN2lFtZuO0wym3GHJiqLSTxaPv91jjILQ9CYEJHGq-1fe3sGxlw2Q0CADTMkdFPpaQhPSwf6Tz1tA8uKpk1_ZcmOu6r2lwqGFxchimJdFeq07BRsyG2foEp2PV5PeYUAvph_3t9kJfxDC-wZ4bvHbzRGXqIl-kchamQ2xlP0gpnCOn0Rs9Guv33aK1HK4Z-Mi9Pryu33AXdraM10ow7xPWq7Iv-NBKuk4gsDuHCcoOYGYQtsL8ggl1I4VjtPl-qR_JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
طبق‌شنیده‌های‌پرشیانا؛ مهدی‌تارتار سرمربی تیم پرسپولیس از وضعیت فنی سیدابوالفضل جلالی مدافع‌چپ‌جدیدسرخ‌ها راضی نیست و به او گفته اگه عملکرد فنی‌اش بهتر نشود مجبور به فسخ قراردادش خواهند شد. تارتار نیم نگاهی به جذب مدافع چپ نیز داره. جلالی سه‌فصل قبل آقای…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26066" target="_blank">📅 18:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26065">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=PAELia9-HBzB0pDGkqGW_omkZNI26I9OkCB__PWw401055zA47WkrFcmsvk_GfUQiN0YQ3fQD2WHD1kkRcqWc9QELH7vk12SovlYfH76AXp3OWMWnWswy0toYwcmO7_CMFfMEmdlbSzRhJU39Mnh7LGj_9xeSQdJUbSzt4we9IO6irT0N7H1qapng9XAttf5Ey2H_FGHJH6hHl9JomTHphesV0AfKsabB0bUWgWhBLH-qMPZKH0gyvLbt4u-Vdlg2W4dFLHm-V5PND7lkjOEI_zuuiAUMatfkzgFNGvdCutBNTdpX-x_dhPONe8LX22vfxn3Z5JojOQFFJnLLvoO0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=PAELia9-HBzB0pDGkqGW_omkZNI26I9OkCB__PWw401055zA47WkrFcmsvk_GfUQiN0YQ3fQD2WHD1kkRcqWc9QELH7vk12SovlYfH76AXp3OWMWnWswy0toYwcmO7_CMFfMEmdlbSzRhJU39Mnh7LGj_9xeSQdJUbSzt4we9IO6irT0N7H1qapng9XAttf5Ey2H_FGHJH6hHl9JomTHphesV0AfKsabB0bUWgWhBLH-qMPZKH0gyvLbt4u-Vdlg2W4dFLHm-V5PND7lkjOEI_zuuiAUMatfkzgFNGvdCutBNTdpX-x_dhPONe8LX22vfxn3Z5JojOQFFJnLLvoO0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26065" target="_blank">📅 17:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26064">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_C-O_aJyQG5doWev3UD3iYOM4Naz9WySbEU-Zo0FdsYlJ2dT-GR7Df2JFJP5nuJdBMffSgBDtORYWFKYQmNeUgFqHuhWx0K76aueOtw1sOcP670_X85UQLdDSnRPnTMEz6As25OUmEkwZSSqor4CtxnmufbFAqJep1P_n-uPau4niiRgoK1FdNun1nctVUD9EDOWSwYj0AziHGJfPLuP7h6IUGVT9g_WMTyfQ6MyD0VR_T7_UZeMDuOBdylvbVC3KLVnuC1l0mlEfwwdgnHjpvi8U60lye-3iCVTY4TM83op1kUtQGqslDIZSb3_8yYp0b0watUH917Riq9yeZ4Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26064" target="_blank">📅 17:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26063">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=GUg-JFqnDOc3-7QZlD8SCyvj9DbqPH3RWeho6udKRw5l8axwfI9x9mRcnEf75lC9BNQARLPKeXF1W2TcevUUqMRNiF7VERmPi2bmN_BZDcl6d21ksceAo2BPF3s4B-8lbo_rtqP5sjZi0-f5Bc5vvaiKPyQ035IpQgCcLJYF9_1nzhnBor8T-jJ5qi2KNaN1KoEe0IIjH1RlhMBvVK_xnwGQ6aK0m1ITxOLawP-m6iOfnmxwwBT5UBaOaN0MUio89qJTK-vqi6Alm_TlG5cgS3zgCnqC6s551SDzfA8AWPpoH-q6XeKZIbXe9mykGu8JuR2sherCHiKwknzwEkV_ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=GUg-JFqnDOc3-7QZlD8SCyvj9DbqPH3RWeho6udKRw5l8axwfI9x9mRcnEf75lC9BNQARLPKeXF1W2TcevUUqMRNiF7VERmPi2bmN_BZDcl6d21ksceAo2BPF3s4B-8lbo_rtqP5sjZi0-f5Bc5vvaiKPyQ035IpQgCcLJYF9_1nzhnBor8T-jJ5qi2KNaN1KoEe0IIjH1RlhMBvVK_xnwGQ6aK0m1ITxOLawP-m6iOfnmxwwBT5UBaOaN0MUio89qJTK-vqi6Alm_TlG5cgS3zgCnqC6s551SDzfA8AWPpoH-q6XeKZIbXe9mykGu8JuR2sherCHiKwknzwEkV_ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه دنیای فوتبال را رقم زده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26063" target="_blank">📅 16:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26062">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PERiSNlBZROLsGieSKPcV5y3QzE8w0-D6K_A0WVGN7OUqGUuMhBD5f6H4sKwkKsYRu_SBnV4Qbx6_NtmvAJ1CNFN1D3SuB9TWkjE5srkPFzij1bakKS1jHMDfsJ9Cmpql9ZfGkYYyhjStZ9td4KGpSX7q2w9Um3fB9781UqJIzsxk9zxMbD5h0sTzMZ2K8MrCJFbW-6L5dN3yexVg0gzO0aPkdrmAypeaDQ6aBU06AjewIVd_lj2LLn0UbsTDHVT7A-UOu9CJkM4-Snu3qZe0Ij-Ut6soHA_jy9SJ8xNgaIoGDWQ1mFWy_51-JygT6k-5xTt83sX-YXpNArTItfiBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026
؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26062" target="_blank">📅 16:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26061">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ho3tOqTtU3PjHgI2NDO2Y5wtKUI5BG3QFUDhABOkXQXdIl1ksZVHpRRWQ18bWVENGyQawjD7Y7GW_wC2eWztOalm-2SjmcyiLWFHiJxva0NbRZAAnxdtrXbUS2IwgyCAFkX9ckDLczD30RLr9h9_lnXyDMEA-1U6GGK77-2NC4r5z1huFdpMHLUU4lvfeZlLcCk4d6GDGINTFUtuAd1qOBN4GpTu9VdygfRNVIhQfXCUcDJ2WbBqkUzxr6EeSpdBRDkdxvgO3IucIFdn3K7Xao7oDx0GpHoU-F83NBrTB_oX40ljAEpj5A2QjQrn4kDPh4ku8s_5MHuGnsuL8BMTKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق‌ اخبار دریافتی رسانه پرشیانا؛
به درخواست مهدی‌تارتار؛ مدیریت باشگاه پرسپولیس با 3 مربی‌ایتالیایی،اسپانیایی و ترکیه ای در حال انجام مذاکرات نهایی است تا یکی رو به عنوان دستیار اول تارتار در فصل جدید رقابت‌ها حضور داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26061" target="_blank">📅 16:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26060">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvAulQSRNe-9dCgl_QpTkwFY_3hBTdjqBcpJMNOtzQN4_q6_7XDd3--jY68e-24eYhN-NV0eBsCISdWI--UsEaVobjnzyoabpFhyVxm9D0xtQtyQbwWYgLXd65P7QbGf4trQTpBlPZZLZbe0l7m-_L6dGOJkAI-0LqqpqRJgqG8R5tYLfjFL2L3MFWxcycz4GklFvRleu2VW_0XNylVwPJbC6ldkjBIPzK_UNWdsK3Y9i97UOuSYTQJTA6mXeVPjfavgKF0MQSQpYLuebykU49pl4l7nFUgmTGoKUR1mVcebqyuvQ3CmxwadmfC137Cx7HGOMESQUEivYeJBIot4VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26060" target="_blank">📅 16:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26059">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=ibQpFXtdMl0dPO9GvMl3GYt2zMxZd6MSedh2gUM9rRcwLCiN6qByJhb6IdyAVNiaIu-tXimi4zb1Om4nZp56kQCHUHlFK3dRwlPi7sptOZGxWM8-ASyrhqLAgksXq8dDbvXV-piWLDWLDXHhwhqOSsw9GzFhYuSFKxahidiFndG2tDyC6XUy6kAhO_1YhOL7oV0kPaXl8HvTKaIKPuaERWtoYii7Kk0YIu4HNGQ_rCCS9ziagO_rgG990w2b2xMqaxZu52J-K6PkQGIKeOZ23MTlKwbra1ShykPls6YWBobdgHwFAn500hCnIrw6F1EeGqP5qreCbie22OXfZFP0Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=ibQpFXtdMl0dPO9GvMl3GYt2zMxZd6MSedh2gUM9rRcwLCiN6qByJhb6IdyAVNiaIu-tXimi4zb1Om4nZp56kQCHUHlFK3dRwlPi7sptOZGxWM8-ASyrhqLAgksXq8dDbvXV-piWLDWLDXHhwhqOSsw9GzFhYuSFKxahidiFndG2tDyC6XUy6kAhO_1YhOL7oV0kPaXl8HvTKaIKPuaERWtoYii7Kk0YIu4HNGQ_rCCS9ziagO_rgG990w2b2xMqaxZu52J-K6PkQGIKeOZ23MTlKwbra1ShykPls6YWBobdgHwFAn500hCnIrw6F1EeGqP5qreCbie22OXfZFP0Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26059" target="_blank">📅 15:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26058">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giO-Jv_Mq2Dxhy74SlwGo7hQNj7CcyysOfn5ELsR7SLVeaxIHyw4E9fkLDInyjNZpCCgeTcTMn2W12oM7exdoKFrsUguMK6VQzWOIqBZjLhrOC9tLWxfdhnBFFLinHpO4eR8YYF-8Ypw1N9NZNV7WSowgpxqo8FSnJyOychvkBZ8vH6Vni9Es-f_4tPpbnxLREGr-FxofulOkjiTbuyxICgdW0U9gxf3AXKI1ju5SYQInxjTzJ821qRFGzlCT6hF3NvD_--DrFFyVN-vqgssggQgKjRuFPZX3wfktxVQPuavxZO1457USq8Hug0ANXClHjpzgbtXjccVSLYDfMSMkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26058" target="_blank">📅 15:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26057">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1vqTNlQDGYa8ayev5dosqRXvG80eBeE_cfy__FKECyaisFDe0i4oykbcRsZ1y-78BBVE3qmigvtBueFupfl4ibuvW5qlhBGMHsRMm3VjO1MMEKRRwdGbgyCwBTrFffEumIfSrRzbR7SQOVh_T1Tuxl44rQbYYrpUBunU3ExsietfhWRuqdFrF0reADULLw8yVAndEUm4FdN-LFL21V282tYNOXQgO8KA0pw8FY3ts1_-AaG-nVGWFAZnFIqcPvhrUQclf1LEbPRF9yYs7WXdSzDzcDOtVwb6x6SxO_-JN2s2Yqsn-R3E69YXJmydBb8xdotVAYdELQl4mb6FHVwWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26057" target="_blank">📅 15:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26056">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=jE2oeqHJS0ry5y_zFzsO_cH8QwLwuiE-9lxGwkPo2Irof1GeAh5twhKsPmGs3i4Uzlsk9mtEd6tqxQ49aldJEJoQXvjV6n0rowHPxKD-H0sxdMEewnOHW2hWsrvxugF9loROrx-KibI-xf-73ISkMYBXs00hZXQHswofOrgnetLYJZkb8Ugz6-9liX1JprpcHcMd78jQ_XkuCBX07ahqydDwt0QlsWZMq0r4he4LngQmoYrQjmiiWwgBV0cOYAJbH5qHR6cxMZIvIiIfR5f2Edzfla5gJoCgbSiCUBclcNCYAMM9DzUhPlq3N3acDXVD-J3k7EQ4kwuJxTp_SBZUsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=jE2oeqHJS0ry5y_zFzsO_cH8QwLwuiE-9lxGwkPo2Irof1GeAh5twhKsPmGs3i4Uzlsk9mtEd6tqxQ49aldJEJoQXvjV6n0rowHPxKD-H0sxdMEewnOHW2hWsrvxugF9loROrx-KibI-xf-73ISkMYBXs00hZXQHswofOrgnetLYJZkb8Ugz6-9liX1JprpcHcMd78jQ_XkuCBX07ahqydDwt0QlsWZMq0r4he4LngQmoYrQjmiiWwgBV0cOYAJbH5qHR6cxMZIvIiIfR5f2Edzfla5gJoCgbSiCUBclcNCYAMM9DzUhPlq3N3acDXVD-J3k7EQ4kwuJxTp_SBZUsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
از تاثیرات جام جهانی فوتبال بر والیبالیست ها در لیگ‌ملت‌ها؛ دریافت‌جالب بازیکن‌تیم‌ملی آرژانیتن با پا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26056" target="_blank">📅 14:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26055">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=VphVpbFfYjHJ3ij6dJZGye6XnyvKEmd8vnCdLkBQGHBfMP47d8wFNctxNDHzxyxYmQR2YTRlWKfWbsm-PR0dvKVVFl1V4Na5wnnQBKizVrhQU9shzb4GAahhNvCUFN3QTwRrSgTxnaI9h1P-Oe8sSN1YBILTf3gz_wT7NN3NQsSGTH9qboj6edImcW5qDguaXbaT3MoWexExPM76vDXt4XHVqiumlQ9rIY1bwVCqv1fObcOUvDaVTUQ7_387BxSZkLq_9BjWVsUlci0ID01Pk09OwKIWscvTXjJEz2dH8kOX4Wc73Bl6k1Q2hUH7KqRBkkz4CR518Y0dxqcNWLBanQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=VphVpbFfYjHJ3ij6dJZGye6XnyvKEmd8vnCdLkBQGHBfMP47d8wFNctxNDHzxyxYmQR2YTRlWKfWbsm-PR0dvKVVFl1V4Na5wnnQBKizVrhQU9shzb4GAahhNvCUFN3QTwRrSgTxnaI9h1P-Oe8sSN1YBILTf3gz_wT7NN3NQsSGTH9qboj6edImcW5qDguaXbaT3MoWexExPM76vDXt4XHVqiumlQ9rIY1bwVCqv1fObcOUvDaVTUQ7_387BxSZkLq_9BjWVsUlci0ID01Pk09OwKIWscvTXjJEz2dH8kOX4Wc73Bl6k1Q2hUH7KqRBkkz4CR518Y0dxqcNWLBanQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پله همیشه می‌گفت زیباترین گل زندگیش رو در ۲ اوت ۱۹۵۹ مقابل تیم‌یوونتوس زده! اما از اون مسابقه هیچ گونه فیلمی وجود نداشت. حالا گوگل با همکاری خانواده پله و با استفاده از Google DeepMind، فیلم این گل رو ساخته. این ویدئو، فیلم واقعی اون گل‌نیست؛ بلکه‌بازسازی‌مبتنی برAI و اسناد تاریخیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26055" target="_blank">📅 14:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26054">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAn7r6C2fSf9o3Ffgo2k-YvduAlaNzvqdtjnEfhUjwKvAE5TauysOVnL_o4Wj4p2iaKaL9NzAJBUg-mmoOvZDKKtkW9cg66jVhjoGxb4hIX3rkxNWsqaIJ9sSAWy0yZCmeDfyONA6ZZfXIVreEnqlbm7zaKnIfFJ-Lvx6ieLLrqlqqSzu8urTSEOIA8vXF7ILM0tNT1IY64RQBunQFoWi3z-LsRiHzf8eyhobnzs57WxjWhOdU1v3nwS0oZdtbkAckBngVN_eyTlMO2oS6-CQEdkyj2np99na-I1h3MT5P0OrFR43uccDvcHM53lcn83oFBIY1m9oBq_6varcIXXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26054" target="_blank">📅 14:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26053">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIjTBUxBPMD77ZCLPI4rAvkAbi44e4BshL0Isx6Kb6Vq_OXuRNroksOARk3GGBt9qRcynap6d1IcErbGh0pd2pit1scAswVeGniPcD-Wr3-zgzWPSvfPcZ6hfV-6GJB6eii0AYLqcYvD5-_B-tCpedIJUDEKYhMgs7txM-PT5nVUFR39atOatVwKFrTdP_tT4_8Aky67He2nhpdkONbaSOntF-ki6V_CMPEsbMxDOWoICcUFGCUlotB-sOOZnFOzbz6HvKdas0jj0D8I8IRu0mNsTh8Swe-29lkh1vri1BPj43nsy7wBPn7fle63zarIdjcAgeE3Hr3pNZRhcqw6vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26053" target="_blank">📅 14:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26052">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nd0BFJu9Mp6J-ZPEr76Eq0d82VrWNs-5bWSQjx-yHBKwf7eX-gDGvGvHo0GcOpXP8H_ahOkTkecS2AuDd6xfYP4MmRYLc1XYjqhlHFjVDeURPNhfGMT9b8rKnTvW0QshrFHPdbdX5g49NQdkLMHQJ3Xe7-K8pZVcGNMNGLJKUcnaHJHUlX2qsFgJdUuVm51hT_86Uz8BNSV1p_KWvfgrfI40MXET3Wm2AUgd6W7LmQPsWm7rS0EWvF_pa9FMG7Y8VVhWcDCHkrhqXx7jiEk5GNbqvUoyPu5OX7xCQ_dZioE_m3iJ_SzB5qmvstMX1p7xmQ-YYi5elXc_5VXM9XM5xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26052" target="_blank">📅 14:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26051">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6dv_DW0ZawXgI46KWK5gPvZBeHKsmU8qvnXtBKR15oeB9gbt7s5xZ7hi3wDkOD1hbD_mEv-bUydHHoKH2G7rkF32nC0VyxaMl5VX99A3qVQ7-sr0bzxQhjWV3D03MiCQVkyQ6zJYZm12atS5AatKktNeNfmbfKKW8VCpyEh_M-uznRGZTg4vbptuIF_rCVqwI_q35MF_yH4eCjZiVKaprMyR_v_8ybwPvbykFB-tS-TuEiTTzEOglKhzaPoFTDJkGFlRjhPxh48Jff-oS8EcRas3NFnUbhLXu1sO7FADbUOPXkqKRESbBhfDMiRHr1yGThnlbEBvzOAj9-oOyVOdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26051" target="_blank">📅 12:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26050">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0106SoOFprM-L1xN37AhG5kMpYiB4s4BD8sEZkWSK1-YFjFZsbnjNPrU0LtZwOvEhSuPo1dqgKt_RlJxGcTcmQLJcBvFeRDvgYAGpvIbBuHrJSr08qi-1wQ-7DtVhS6DN4YPRmwSv_01A0DDVcYSovNUrOTGP2PXFpu7n_g1nIWECZ1krI-xuwZrJqOtLtSKff_2dzqmLr0yT88qciBrRSSwdOIiZsVpW9ogF4m3fCaZFRGDgS2yH4u0NlgSxpE4ulRDVEgebZ21TRK8x_CMbVrkHVWd2WpqcgtkXfU--zC2Hg_FviT8h2lDhOqFhyQj64tQAVPD_pTW6lWnzDWaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26050" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26049">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5oBjAIpsiwZ5DcLN4FORvcRNCQnP-3opg8gl7_qnsU-nk0uENm6lxDBrCQzmzhvTnbc7acfPJLPndXVCbalItstCU4rxJZ8vqp2fdl089KfzZc2niJjsB6VLx2V6QIjvQkjNG8jX8fgNZo7sqTBfK0OeOS-cB5JDjWAwOu9pxdjkRjoHANlfYy2lAOpRycolO3OgkYmBUjTUQAN-8aIX-HeQ9rQB0flNzc_vBoo031inUGYmDNHc24kxb5Q-OpxNmFVOSKZR1xxuXGDBhBD1RlRjYpkukmhEGEA7xEhQ5lrR9seMtTOTJWMe_40pZgwa2_9xtG83rrDHwV5jOGyWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کلارنس سیدورف اسطوره‌باشگاه‌آث‌میلان و رئال مادرید درکنار همسر ایرانی خود؛ سیدورف فصل قبل بعنوان مشاورمدیرعامل آبی‌ها 250 هزار دلار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26049" target="_blank">📅 11:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26048">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RALQUSWI8yxUYxv43jdILfRGp7PMPtSGxEwszGB1KNic3jCncrJpDjeXpDCJX53Of2A7SS3_dbTOPwmVg_-AtjheDQInoJktEPe9MHBOl2_c7z3Zrb8EHYy4YOk_5VFIdFlK-Ykcpf5uc_iWF2Bddui5lAOML_dcw4Sao7uCnU3ovlvNlOCkz5plzi1h9cdowQS-GlwONmTE9MVklyBXrTeMkMDcJUG6a40qiPqjdpJxc4fO2DkGR7ouGusYAVYFY8ki02CYi7-js9GePppwh3qZCnMPFffKH6hts9POBV38x5RLsZs51Y794ASS8NBzpeAXGY5O5gBaEXF8EhMi_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26048" target="_blank">📅 11:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26047">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbEV2zeDKPAws6r524Rprx3ZadkKCLrT4js34UHl6hT0oVnyGqem4-mzEERhx2qMwx72Y62kEkmhm4A1Ei-VQxOkaEnK6KoQbaUOtvQMQmJ--SHWqprcuJZhF27DodwZNX56K3NmHKV0hMG9hseYqeCkTEUxYspdOhSdFGGaJ3M9KOW2nqc2nudu2T8kZq-TqAOWZScqU2_0TQVZaDrU4IKA3XagfUtfA_OWfm_BGD_SMSZ83KvEaHQligWJBvI1yIsT_VHKN4DKbZnfxJ0i2KeR478bcP8_3oy0XO4awVgL1fjVfY25FyxSIUMa0x9Ku-EhggxmyR9iofb7a5QOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26047" target="_blank">📅 11:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26046">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYKpZgEr4UGWVwpsQTc64O1VSexCMajb5dCc-YVAxafjfDCHiASfKVOhOvROMof4GFVQ-t3I3UuGuhlTydJgxivOj5w5ZIIjZ0JYUa5wXPuB036-OoKYzabPk078tg71tsFPj3o3CHjmiuRGdhpo09RIsGnI-3YOGzEPs1tuxB9htfvaGX09IO6T8oFJEdAzHDaG18Og96RJf41dHVCtt-ztcvhLBj2z_oJ8SSenV8eyWjK6bEZB59HB89Bi_0z95KF5SObnJndkblH_BlR1cdS5J3HazCZbdxmNw6D1CyMxXb--JUlVBMG-tah-mWJK7UQ3bpwu4sVOpdtEJIXMOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26046" target="_blank">📅 10:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26045">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pojir-bDPJdFuTrTm7TpDdaiOYiaRQTxooBAxdA_6pMcn4CvsTLEYfCaY2Y-E_Lkmq0gVuGrzyam74Pc4-oR5zFBVAZgdt55GsGtIOsfY6kL3Z4II_dO1xBqx92un-r8tE44H0ja6aeWLoMHKIZFClPUc7ptxDaZ7l1N_qrwXg9CJjb_p1GeWzmB0a8o2rBGtinrnbXo_MO7i2Mj1WEgiju2QVeXP5vHjaKajwpcs7pbvr9kTHhezFXSurjHWrvQDG9R5uhi16dqtCxdzg47X9oX4OBoBtCj6lYuEO5n80ZmeDa9cwgM9fMxl-Dq5LZFJPlFbMiRqeNNra_82mxBPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26045" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26044">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">📹
ویدیوجدیدوبرگ‌ریزون‌میلادکرمی بلاگر معروف و محبوب ایلامی و ببینید. رفته رو پل B1 کرج!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26044" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26042">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05254735f5.mp4?token=GLZBKbtgknJO-dKB5z6sTY9THe3ZLuqVfrVpG4cvUSCPdD0mRa3h4a12aF_HGddLLJUamkUfzjBZTNgUn40SsShmVMXjtQkeXQVzEhjKQdzIb-BqzZuxJezLkrOPkRmk4iQSRliAbygrN482xJPFvWcrZ9dBcVVhI7TcveGUvOnX8ucjmS9BUfoKg1V_964FzRIbbSLPRy3RvDOK-PqXnMzWZsVELABE9rZbkVBiLFHdSirO-G9JtcwIohHTRX1jphUo_cRO068iOY3Km6mvyyiHOMIx9Yq9jFQRcYENanu3EnufTAUGb8AFYGjt0iOmqpYhFLLnfKveYYgt3-dYjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05254735f5.mp4?token=GLZBKbtgknJO-dKB5z6sTY9THe3ZLuqVfrVpG4cvUSCPdD0mRa3h4a12aF_HGddLLJUamkUfzjBZTNgUn40SsShmVMXjtQkeXQVzEhjKQdzIb-BqzZuxJezLkrOPkRmk4iQSRliAbygrN482xJPFvWcrZ9dBcVVhI7TcveGUvOnX8ucjmS9BUfoKg1V_964FzRIbbSLPRy3RvDOK-PqXnMzWZsVELABE9rZbkVBiLFHdSirO-G9JtcwIohHTRX1jphUo_cRO068iOY3Km6mvyyiHOMIx9Yq9jFQRcYENanu3EnufTAUGb8AFYGjt0iOmqpYhFLLnfKveYYgt3-dYjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26042" target="_blank">📅 09:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26041">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=k7zKxiRHlnx_yai7K78oX52iocty5x0zLF4YbdAzscxiy2i8QZsQx7BopTUVhCD2vO0lKQwQqJZPBnnYhdAh8PGNEoO_WOkSNNeN4IT2G522ww56ExxVUSieQlUOP36BRC3N9328FiCsEbsSXr6_M3Io0gMKzrkJTORfJ2uHvXC5rWBgyMVyvMGIBNuv-u_tKBahTqky2bPIa8chKyFUUwnXwjitTmtq6ldioPF4WpKLy_WmwWMA3vpjHZcZIH69y2QoCEFryi63225MmBG_hcpSNdU3GnQB7Qy8GppC5ckzfmvLRqAtNQivDSV6-D73Y87ml6uKPKw0CdmrJ9l8Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=k7zKxiRHlnx_yai7K78oX52iocty5x0zLF4YbdAzscxiy2i8QZsQx7BopTUVhCD2vO0lKQwQqJZPBnnYhdAh8PGNEoO_WOkSNNeN4IT2G522ww56ExxVUSieQlUOP36BRC3N9328FiCsEbsSXr6_M3Io0gMKzrkJTORfJ2uHvXC5rWBgyMVyvMGIBNuv-u_tKBahTqky2bPIa8chKyFUUwnXwjitTmtq6ldioPF4WpKLy_WmwWMA3vpjHZcZIH69y2QoCEFryi63225MmBG_hcpSNdU3GnQB7Qy8GppC5ckzfmvLRqAtNQivDSV6-D73Y87ml6uKPKw0CdmrJ9l8Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین و پی‌درپی عادل فردوسی پور به امیر قلعه‌نویی سرمربی ایران در برنامه شب گذشته
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26041" target="_blank">📅 09:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26040">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده و مهیج شب گذشته دو تیم انگلیس - فرانسه در رده‌بندی جام جهانی 2026
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26040" target="_blank">📅 08:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26038">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YTp5XcyYfhY_BWxxYQT6JasLPwjjyLcu805g_RUggf3qSgwoG1ipHaYCG5Jh4k2IlVkixDOiEJAoB1tYpHQ3p7FNLg94p-gjsLWVBgp45Q6j1EVyfYtXLdqIZfTD03MzkjSAijvt_Boo9am8ZEB4GUMeZWWT-XlJ-CWwtqT4O5le3J57bHkUxPSNMgx6scfNiFBWbuwQXHlEG1-NgkR8hjh-PgnETg_UUNM_ncu_a90SfqSJgUEVBA1KAksmAlSV0TcI10QCwsrNL_fM4jeOVYZQmJ6_aXUoGIbR4qb6coUd5NONMVqS2xFhcd5jhVmhme0oTH7Bnt9Y9X7UN_xnJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RgcZca-_PxzoKu-HlBVWAK5rUqpgkGUiaxVn69rtBzdKPcEmDW2ZhgmP840RTir7DjbKP1UllAN-AP7ffQpfposctYlzH_ilfZr9cUdPLJdFtbQjehC7A0Y6aqR8-WRZSxVuNEa9YMEmvmSo2SeL1-aI2-O9HCT6vRxMGmHu92_oC73i6F3cM9qqnGgSMQU1e_uHgzJfjWNjp9eCNigk6k-XrdA8k6tWp7P2BrOVhuy_kIRRhy_fZ851vtV23696ymJE-A2rT5rOWFQPkjJKK_XYKedQB76xjb_H34imOM_kSH9K-eGTKfr-Z_xT80WhXem-K01ljFUJfGaBvn2jKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
تیم‌ملی‌انگلیس شب گذشته در دیدار فوق العاده تماشایی بانتیجه6بر4 از سد تیم ملی فرانسه گذشت و رتبه سوم رقابت‌های جام رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26038" target="_blank">📅 08:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26037">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExZnHOacWtdv9DaLfbz4hWiyzdzjoVXyETRri37pHbRbwflvX5UjmDa5RBfi3GegfTkEALa0KP4y2o0iidfUc-kt1pEeDwXSUggNxF9dgBqS9EiJu84zYj9cDIQo-XjmHwuefElwTh9NG34uH3L30zAucNpplgserwCHrOG9RGo2zRpZcqN0b4nfm0DTMf5s6zarZeESrKGW8bEriJapm-AFdZ67RTBAnrc9ghrz6-uFTsedwZVzmc7jDXGoxT4NaMm6r1x7ApUCn-6Qqn6WSugfJPeD_pA6YfwePJsKPnbuUlA-5NP_T-jtSnvwzzSKq0Zq2BHpxqvdEnXTKX1lQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مسابقه‌رده‌بندی‌ جام‌جهانی 2026؛ شماتیک ترکیب دوتیم انگلیس
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26037" target="_blank">📅 07:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26036">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=rPrxKiWelnfmtROo4QvHdDIZFJw8jtixt7yudqDWOw-7Yo-UnFI5mOkwwqtPwpIQo4fiRYHjoteXSJ4YL4caBkyP7Ja9eiGXCcd55qlBbgOOkNhjWxBA6EZRaU25wP4LovZ_2E0n7Cw3IFet-q9ep9ThSHWuNkRchA_0qBmkp8sbbztgu8ldKEhFEbzshFyt7N4y5V0JQSxWDZVt0jVOZ8nO4U8daYRrc5TgMEAwNe3GsPKt7tqx4Y2jEdNKHEwFRdXSB3qQ0b8zqS8lfhF84Q87yJAipKbznhwQwaQf0qQvRZxNzzsXHAhTCPBijDJpvT4mPfNgGA4dSCKbJXf19wRXNh68tqD9e35t9fkokME3w1UwwZl98G6utQmS4qWlfJhsHv9c1e7lre34cNpXLu5pPdqjRenUqtKCD2JVzUUMTFpBLjRRYpgdK6DVT0pSUADzrJlH3JpwJhWEj_H3VDh_IQYk_71I1J6U0hXVDpG4oM34LtmzSnV_1m57bJd-stZTVDvvwgRzNVWmQtgkWu35kywPvff-AplDtLLo-FY8pojltlVfmknDSvVrfS7rd7QmOR8jSRkyweJEg6BJtwJXDiREzgATJFoJqUU-srmoEePnrQc6jTzVm5PmeazaKNCa3QiwGYPuXlCya-DnJ50S1IOIoHVlZLZk9TNH6Ts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=rPrxKiWelnfmtROo4QvHdDIZFJw8jtixt7yudqDWOw-7Yo-UnFI5mOkwwqtPwpIQo4fiRYHjoteXSJ4YL4caBkyP7Ja9eiGXCcd55qlBbgOOkNhjWxBA6EZRaU25wP4LovZ_2E0n7Cw3IFet-q9ep9ThSHWuNkRchA_0qBmkp8sbbztgu8ldKEhFEbzshFyt7N4y5V0JQSxWDZVt0jVOZ8nO4U8daYRrc5TgMEAwNe3GsPKt7tqx4Y2jEdNKHEwFRdXSB3qQ0b8zqS8lfhF84Q87yJAipKbznhwQwaQf0qQvRZxNzzsXHAhTCPBijDJpvT4mPfNgGA4dSCKbJXf19wRXNh68tqD9e35t9fkokME3w1UwwZl98G6utQmS4qWlfJhsHv9c1e7lre34cNpXLu5pPdqjRenUqtKCD2JVzUUMTFpBLjRRYpgdK6DVT0pSUADzrJlH3JpwJhWEj_H3VDh_IQYk_71I1J6U0hXVDpG4oM34LtmzSnV_1m57bJd-stZTVDvvwgRzNVWmQtgkWu35kywPvff-AplDtLLo-FY8pojltlVfmknDSvVrfS7rd7QmOR8jSRkyweJEg6BJtwJXDiREzgATJFoJqUU-srmoEePnrQc6jTzVm5PmeazaKNCa3QiwGYPuXlCya-DnJ50S1IOIoHVlZLZk9TNH6Ts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت عجیب‌وغریب میلاد کردمی بلاگر ایلامی از افتادنش از روی صخره بخاطر یک تبلیغ کلینیک.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26036" target="_blank">📅 01:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26034">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=u73YczM1B3RNNHC_s561QBm0lU8FOQxoJ9PonfKTRjw1YvdD_5zsqFf0vC7Y4iRgOlYDZdEFv-UT6UzQpmAw1Cv8bJY0QQFCeP-CcprrUbu15bpFlB-WeYOr58EgXc3a05WojIV5iIkXHr4X4jyCzRNYoB5UihUdvuEW5oj_oOlsru612CrRhfNDVZPPUMY7G3ajiGmk8TzYCgC97mMR_1YHefKoYdVR7Q8XYJ6kUAQ65Ori0DJiB1vZeZ3_T5oBpMK4j-Czr77ToDUIJN5ZCsmPQviguDIJQRoprFZ9inqrqjisjvQoAkaoRdsVQ51SUePKG3PgwqSpw--17U2AMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=u73YczM1B3RNNHC_s561QBm0lU8FOQxoJ9PonfKTRjw1YvdD_5zsqFf0vC7Y4iRgOlYDZdEFv-UT6UzQpmAw1Cv8bJY0QQFCeP-CcprrUbu15bpFlB-WeYOr58EgXc3a05WojIV5iIkXHr4X4jyCzRNYoB5UihUdvuEW5oj_oOlsru612CrRhfNDVZPPUMY7G3ajiGmk8TzYCgC97mMR_1YHefKoYdVR7Q8XYJ6kUAQ65Ori0DJiB1vZeZ3_T5oBpMK4j-Czr77ToDUIJN5ZCsmPQviguDIJQRoprFZ9inqrqjisjvQoAkaoRdsVQ51SUePKG3PgwqSpw--17U2AMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🎙
علاقه‌ شدید‌ جواد کاظمیان به مونیکا بلوچی ایتالیایی در گفتگو با ابوطالب: خیلی دوسش دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26034" target="_blank">📅 01:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26033">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=F1j6KTZCMHEglwOvsstuDZpLmJIKNS0cnVno09D3fQXmKWZFvVAZ0hukP5qqpPV2Hi5Sp81zhiUZweI-dwNmz62iMdCfvQzFLTScUAIgA6q8e1wIqgGYI8aC2cHwlfIoOjKBR53hrIk9Qmck19zaRT90BPnEIriok8XydeVncwOxAinKFr7Ztn7nhm9IwKZJKUSGZNC5TFYR8VAdWxolknXfGSVWQ0ycgWHk1goo5B6ZMwjzTYeogUWkaA3_OM9OzoKver6slrGBvRi5AaBeVNlsA-HrfJZl3GgIZ7P-oZmw5rnTXHWYM5fsjbnO7VlUyN-YXVfXVgjRoR4vOpXXzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=F1j6KTZCMHEglwOvsstuDZpLmJIKNS0cnVno09D3fQXmKWZFvVAZ0hukP5qqpPV2Hi5Sp81zhiUZweI-dwNmz62iMdCfvQzFLTScUAIgA6q8e1wIqgGYI8aC2cHwlfIoOjKBR53hrIk9Qmck19zaRT90BPnEIriok8XydeVncwOxAinKFr7Ztn7nhm9IwKZJKUSGZNC5TFYR8VAdWxolknXfGSVWQ0ycgWHk1goo5B6ZMwjzTYeogUWkaA3_OM9OzoKver6slrGBvRi5AaBeVNlsA-HrfJZl3GgIZ7P-oZmw5rnTXHWYM5fsjbnO7VlUyN-YXVfXVgjRoR4vOpXXzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛
سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد اما گاوی در کمال تعجب قبول نکرد و گفت تنها عشق فعلی من بازی فوتباله!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26033" target="_blank">📅 01:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26031">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqnLqFbo1vL8IGjMWAjgyleGG7fV_3RfcxN_9s_1tP_mm8AH9ax8OvCwCDMx6gY9SbVabmQIRSfBfvK9XOqGdN7ZetYRNn6cqwCa_XhERbaDJSbmu9fot28knCWYbuhYA5g7yEnUgQHm8jcd9AJc8B2l-akqogQMHbU_LzjMoXD1w9Qz215b9dF6juAyT87_Wa2Moonepq8fZrJcx3F5VwJDQY3BFmbpjsIClXkgHQVc1SmTlpFkwB4V0c1cxhebZf46NyhZlUSO3qNJHGlIvtFmCNDXqXw02SR2-7M_DmEsLTHQXyaDAHEwhKzpSm_Nc6b1MKw-in4QPCsRSzntBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26031" target="_blank">📅 00:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26029">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=iSmsTmYsEArDd82U3opjnbZd1lIWZEUChAvqdDHqUQ67TyOrGZCnXb7lBqAo5L_Xng4ATGGowqH12G4crdPzGGhYtmoQ5HIfSA6bYOeIyc1OJhe4XPgVw-0TR5Dh0mXpprmucbdNx5XIW9s72r8XyGVb8TdsynQRcqLPzv1CKG9xH-VwIPOystGjwXufuRGBtM7wIVa0-1emOGnr--FeEvBOperblG6GpOUIHq-SLjl4fwKfzeEINK4XXVB00QHWWQj2RKayTSiStcTLlKoczbUOQKjKRkBpIJEWEFNvMIkdY9aWvn9zXcHqMwvny4pI6bUUG8rjsbIJ-s5ZugDMKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=iSmsTmYsEArDd82U3opjnbZd1lIWZEUChAvqdDHqUQ67TyOrGZCnXb7lBqAo5L_Xng4ATGGowqH12G4crdPzGGhYtmoQ5HIfSA6bYOeIyc1OJhe4XPgVw-0TR5Dh0mXpprmucbdNx5XIW9s72r8XyGVb8TdsynQRcqLPzv1CKG9xH-VwIPOystGjwXufuRGBtM7wIVa0-1emOGnr--FeEvBOperblG6GpOUIHq-SLjl4fwKfzeEINK4XXVB00QHWWQj2RKayTSiStcTLlKoczbUOQKjKRkBpIJEWEFNvMIkdY9aWvn9zXcHqMwvny4pI6bUUG8rjsbIJ-s5ZugDMKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره علی کریمی هافبک ملی پوش سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26029" target="_blank">📅 00:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26028">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHZFhLRUxt6tEBckkJx46Al_LpKg0l3E1BBGgNf8Pi6_uI07YmOMqrcgO2fSG-HPr6a-CFSlp96ZV4eZv9uxzHTzlgBlUU9w3Lgu-eVHv7iTRQyiONgAaCq8giCWUFUqdQAIVO9M6ski76CubyHkgmMiqEq4uF9Qa1qRSiPub4KKQ8T8cjqdmpdpIQJTTWT84TmClrMI90cC0XN_wFk1pHROj1XiX7pkINVLUB9xOZuqR89Ju5ngg-dPWQTUJarAfu93HqACjUzytfPXTxwfr34fyXjMPPyTTYSUJ3BVWp5ZLymeJiqSf1eUqBOPBRSsMt9-wka1yMkBITj-Ass3sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌دیدارهای‌امروز؛
کمتر از 22 ساعت تا نبرد تمام‌ عیار آرژانیتن
🆚
اسپانیا در فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26028" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26026">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bC57e7voZQjRPIYtrju4a7pJ_J5tqATxtlrD7kiDkEiMSgROenY4IsBHaawRNkF57vdy6nhC8p0UF0nsJZ9wXLoaBA4gxyJ58ytvOI1NwQTIcuMnplqsUhKmB_3gZmOrbbfYGhPeLZx-1NlnAnT1BX1JpmaQxGIZyA1nDIVWXdNilHdQ0ZRYZ4pa2KxEghzl3ocKz2Ppn7AyIjWIC7A0p-0RkOSIIOdYxpp-TjegZ06Xs1aCRGfcXr-lp0KGCPrDb6lQ7qHzHbqMsTa_b9Kd4CWon717RS9YjMu3IR4RXqsnE2HP2V2zUfMMyCaf3ujLSwEOCMpGbAtf6Sptwq0y8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26026" target="_blank">📅 00:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26025">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhXueAFHCc09eLQt7EPNcWrhw-VYKqLo3veVB8AQFez8rPvwaKRuE-aRe7dlMxC1aUyMW3uKFSfPkGT_XkXHhUhWs0mEl1sqJrkSNgbGdEkMo4kYcGiEqYz6NC6Zrf9Ll8PVXTlf9p5-FMhuCKuiWZvLaWHVAB3KqX2izOFyQBoQ7yJDV7HDJkid9aVEkCbq0-Q1furNfS15lDwYyf6aeKL9EVhSPugxcYKKrjzbLL3kS1hZfuYDG13YZL2XC57_-fwsMMmsvcSi5Wq0wQDZpZSDLWwsy2EoCcuf6T_I5MazHeQIP6GLwvMIVc6rLmMLkf0g_WRNQ1AZ2w0Usj-qXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26025" target="_blank">📅 00:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26024">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=MMUJmdcOQ3EeFqWqlXpDJld7tSdYnwr3x5NisJ9ZfQHFfR3ihdbwl7UPmx2GgwAbnOLxoVBMY0Hl8ygiYuhwCN2iMiKXlF0K2wjDlBt9FdfJsHOAl-t55z08rBIdnvbWyavXE1cNfpEXuS6eSABm_UyuWOX1mbd1ulYul17eCymKMQ2FHx_IZScDwQI1Y6Rk9vdpvSp_ZEpHq0d6hQF5fbUpCsngDPsyHnfN-LvGlQnAKPKX25_Pz1QzlNi-XzfURgRYeBSb3gTEB8hf2-yJV4Pth2Y5i5S2Qzmcm-IsYZ2MB0esCtQPgF5bsWjyWM1ZmMxF4-ta7rx0fnBIuIuFcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=MMUJmdcOQ3EeFqWqlXpDJld7tSdYnwr3x5NisJ9ZfQHFfR3ihdbwl7UPmx2GgwAbnOLxoVBMY0Hl8ygiYuhwCN2iMiKXlF0K2wjDlBt9FdfJsHOAl-t55z08rBIdnvbWyavXE1cNfpEXuS6eSABm_UyuWOX1mbd1ulYul17eCymKMQ2FHx_IZScDwQI1Y6Rk9vdpvSp_ZEpHq0d6hQF5fbUpCsngDPsyHnfN-LvGlQnAKPKX25_Pz1QzlNi-XzfURgRYeBSb3gTEB8hf2-yJV4Pth2Y5i5S2Qzmcm-IsYZ2MB0esCtQPgF5bsWjyWM1ZmMxF4-ta7rx0fnBIuIuFcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26024" target="_blank">📅 23:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26023">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=JGdUIfNhLHzgl4Z_SgtKniSH3D08vFaRvr81KQRMCyCdFoPtr2MJl6yFg3iV6U8jjYIiqk9XCEZvD2CUtkvBxIDC6cwCXPd0LDUSwJJ9eMD3L1cDLplgPE42ACFnWWNu8vgJn7pyvKlgTKhYpaskT9EfTmCcjwfme57h4obS8SadId8dTjzigm3VOD37IG0j8N6gsCLdhe1Vxq90QDJB2sQu-cR12mmKLko70l1FFxpwT6oJViH-7rFNm8G09MahXozXT4PvgOUqC9IDnjjqSEjvL8-HOOGNec-rME4VpPLl1LUDJHq-FiuGz5XlGcoO7HZPnsgpXij-GfqgS9IHXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=JGdUIfNhLHzgl4Z_SgtKniSH3D08vFaRvr81KQRMCyCdFoPtr2MJl6yFg3iV6U8jjYIiqk9XCEZvD2CUtkvBxIDC6cwCXPd0LDUSwJJ9eMD3L1cDLplgPE42ACFnWWNu8vgJn7pyvKlgTKhYpaskT9EfTmCcjwfme57h4obS8SadId8dTjzigm3VOD37IG0j8N6gsCLdhe1Vxq90QDJB2sQu-cR12mmKLko70l1FFxpwT6oJViH-7rFNm8G09MahXozXT4PvgOUqC9IDnjjqSEjvL8-HOOGNec-rME4VpPLl1LUDJHq-FiuGz5XlGcoO7HZPnsgpXij-GfqgS9IHXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب‌شروع‌شد؛ جواد کاظمیان با انتشار این استوری و تگ کردن مونیکا بلوچی تولد او رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26023" target="_blank">📅 23:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26022">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbQZ2CVHKm8u3y3gkpea7VvtQDXznTC48U_b7lrMjl3UuGBNdZyMo8rJsp-kChjTClqNdeu5FAE11M3uO-tgrNLfeuXI_LWRjSLRs9LP8vSDVAsyxjPeqpa2rXs-Zymo4bU7ksi4P0RYtisoumYYAjp_TKkT58rrEh1nOhqiRU7O_-2_a6QObQZzletVumHpnnDG_4nJ0lWs6ffhsLWRLp7ZGe6EgnjrMMPPBZx6W9kxE2k5FvCXti2sRfWTSq7zO5oogzx37jmhGif95dfoTl5etJcb-10JoByo54b0R9vp65YMP662VNJER7G8Bi8q_NfdgU0hjR_CCY-guZMW-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏆
باشگاه اتلتیکومادریداسپانیا برای دومین بار متوالی بیشترین‌تعدادنماینده را در فینال جام جهانی دارد: فینال‌سال2018: 4 بازیکن؛ فینال سال 2022: 4 بازیکن؛ فینال سال 2026: 9 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26022" target="_blank">📅 23:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26020">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A2r7eIW9tJUdqFLdNZ9Z-p5cpazSlDqMN5zXKFx74V2Oc3fwPxoXF9vH2-UrYicuBDjzvDyHT4UGaaY86x1JRkjTIbxYv5r3LhJVmTxJgGVXobwEq0E3X3JOP11y_t7wEZG6M71wSdqyID1b3Y7nX3bOFAvgD8s90p6Jyf4L2z74AZ2j7c1mJ_8Cg8xEGeN2sh5Z7XGiKC2ILAo6cVqjHJnA5r0i0vuhvI4Ym007g4p9VwhdnWNwvL0mbQvfEErd56Ner7JMCEbOZ9kv6vSXEu4v_jdHxX7HqOepC_ekP4Dw4Vv3sYPlSfbxrLikASdkcegdp5NvTiZw-1CefGkMhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NezKWgnIOrZvngACUBn0X5GG8xTTcIa5ESWCXrXNHmCdx22Yt52aQXLUCIGPUWpi7xSXLVCzjXv84LY3y1H_N_SAKSXY7Wcpn2zBDVOt30x-LZPkOUYGqMJ1mYzS3prDA6ChbU7yLD5ZJpPkg2NMTx237KmQ4tk8ww22qLi26YsahY7yT_QDAuoMlSSp3BtzB_PxsIfcJlCvbLytAPTovL_t48YYQaGnvI33uJUurqzmwS5hNiB2fF3Fx5erxYKaqsO0nEBT--NPCpCLQ2oZ9wUH6Vz5jDUmCn6b9BNyVmm6FB6KUFEVoNyxkqlZSr2j1z38j8kfQKd8Iz_-VcvduQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
مسابقه‌رده‌بندی‌ جام‌جهانی 2026
؛ شماتیک ترکیب دوتیم انگلیس
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26020" target="_blank">📅 23:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26019">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvY42Kfg0Kk-_g8BHoIp1lzLKj5davk8xtbmF1ECoq5qVVRxMe1k5phsPPOSiZzCWiB8HqNKasonV_OwjqLxvzvIgsCHlTTk7YC_aH6TFsMEHJLynpnt7HuVDFMLx5j5W1GfjiY3ORPDZSru2UkssbLwEzUpBBj2np3H4yRuqJMFU_s7FVKeY2-wii5Mnyt1z3FdO_KVNUEznO-8BnZMUpwuUrSmBvie0Q2hXdu9rQxWGc1hrSqW0Q5ENDSARNBFGpCnNYzKdfymlUJ-Ugs0hos4cRdRxn3iuLBtvtqiBj7refcYXGDtxp32KI1ABWnbUUInVxey-3MAgeuBJm0mhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26019" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26018">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAPCro-ergyUh_kFqB-g4uLyAJtElTUUrqMXbI5vdAWv1ZyyM_DMk4PxEhkC-B6Uh3VqbIOCqXEar5Fp2QYrd8i9_eD_DwQaW1UViU0RH0lm6wWKdUN5piec0byn0KgA6E9GK6Dj4uqTwQCJ4EOYLgPyEwaB2-3cQACVxmD90MAXohh1xcX9a-FHW_D-k3F6I9nRlRWVy0mJ7svxrg_2eumxA7GgjAR7Ty6CYdz7vK9rWzNbCYLYNs682n2pxnitRPbr_FidA_n-OYdlCji2pK63Q_RoWvQCIC52rpnmMMrqXOErT5QrFJp_FKY7Rnh577_1C3EyQ_4Y56qJJQGR2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26018" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26016">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇪🇸
🔴
هایلایتی‌از عمکرد آلن‌هلیلوویچ ستاره سابق بارسلونا که در آستانه عقد قرار داد با پرسپولیسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26016" target="_blank">📅 22:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26015">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ibq22vmszjZg6ZqsD-WK-CfqgNlNGrkZ1bcXXuob1LGdc3qMYAfWvtwxjM4Bk0T656Gmi2HVDoj5MfZxAdB2vWMeizS2ddCCOM1pPfut2WcxtAZDQmlHDJDBXkwMlVBq44kwRkkdOwxswVGtA8yToWWzLi9OnHbjszLR9BuH0xBqmLLCmLu9N3HXVyQPyJehI1K6tm5NFNpCcP76ZM2Q16TVY6YMHqzRTyGGe_hZS2umptXs2gxwtYUSuQBxhYxKqmGX1wOMAFk69akJaUAe4sSsFHJ1YT82yfnNFgIVC12SvYDHKLdzunn_l0OWjbp2bEYIVih3rEmDYSsUeT2Tyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه‌پرسپولیس به‌درخواست شخص مهدی تارتار با یک‌مهاجم‌کرواسی که سابقه بازی در تیم‌های ملی پایه این کشور درکارنامه‌خود داره وارد مذاکره شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26015" target="_blank">📅 22:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26014">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/othLgfAeHbgDWA5giKjMPpWm2EET_mfN3Dei9SYkvD_jquuL3QrGhglPqSymjKsVf4sjSiVLzeag-xi5xXz4yuIrjf9nVPmEOPH5sk8qod1W5c5nHbHqrkNuzm39Iez6LyTjubB-vM5g4ddmv2w7fLLmfXL672gwIOV_eQLLCyIkbNsu0JdqxZvt-WSNwsvvypSjXGKk4SvgHkPhPLEazYkZIg-zfsa03OyLUbOS6DjWdu_P0sLsnwQdv0fmres7Wbkkca106tGctp2CGBx3Mkwo77yYrO35ttLGB2yTtP4t8-AxkvjRxpEO3AQVwvKB_1KzXrXNTKzSGoCtRzowAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان تری اسطوره باشگاه چلسی انگلیس:
این سوال رو از من می‌پرسن که چطور می‌شه مسی رو متوقف‌کرد؟جوابش‌اینه:هیچجوره نمی‌شه! حتی اگه بخوای با بازی فیزیکی جلوش رو بگیری، فقط باعث بهتر شدن اون می‌شی. مسی فوق‌العاده قدرتمنده، از جنگیدن لذت می‌بره و واقعاً هر چی که فکرشو کنید داره. به نظر من که اون بهترین بازیکن تاریخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26014" target="_blank">📅 22:31 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
