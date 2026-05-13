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
<img src="https://cdn4.telesco.pe/file/PacDFczw0TNiEoDSbHiGtbdROD_QH8yTqQ3x-2ExBxFxtx7dBemEP8Rb5JX1nmU9Ay6486L2Q3I7uOlTdcNRTsQt6hR7OqXgrqq0zTXIXoDxypHGePWypKezJ_0xL0Cp4RLzV-JJNgcF7t-LQuzZJ_laFAhj6rLbJm1W80iTVUuz96963A4jC9WMe9qrIyc9tD6DlCvCUSmonExESC_hQS3-kymWfkX_-lNPYJZ-iXVavm602c49-wcGck1BOyOeJtleNgAgt02QHMTfKzqBFFp3dnaT0M9852dgKqL7yBKKMFabDt4IxMW4N21Gx616QZaNf8vdo4WRNI-RDVI-EQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 37.5K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 02:28:21</div>
<hr>

<div class="tg-post" id="msg-8354">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 338 · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTE_c20_BnoqR_3DaZ2lB7ZAooBaKBLNa6OIwJBPgEW1q4OLCfhBBz39_-UL2eqP3Sh9hufqgJbrVWc1w4RGM_AnImtJD9VILootLM5NPTEya2MQedULASOfHAyE73zSEy7lInHGSzbWXiTQ8bjFkngACtR36BnoHfPtDnnH5ML1DekPpAIJQ1Qts-TWiW90BktGY9V3cTmhXK3J-pBlQE_2uQVeSw1RmU9tGKiFlB1BMctDuyq6ieWuT51BNDAScGaFJyUnP9bn38CLAC9wkNSk4gFU8Q0tziO6eNVcCix0Nsv2sIZgnlgozz_JpKo0h9SHB80MtJxS7MUSns5VYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 599 · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 625 · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8350">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=
250
T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=mivrpkM1C9xd-yk4gdJ_Dzs6NoJ9Sill3XNKDcFQLq-JczZORoVvu7Sb3U602uMZmRNnCCcubw6318P7-nz0B1qcOTzxOKEYUI3y1T4bM9-o_Wm_tZr_QLctsG1pz33-3sWP98pHPzTllp6sgwPTyuO7wtg03PzL_32pGICWLb359-_r3qEfPM2x5uGNhyLeWIENFgZfI-cg75Wds4wdgIoxWoVpoRMtxRJ2ew7zOeBqoKsS-6cG6KJ_IyZAHn1k7sm9TERK10B98SLdyGgmWC36SqVJcLjUktBJjvJ1J_Znp9z-qHZCkU4SAGWw1aarbD5mhg2G6LVH0aaw22LfTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=mivrpkM1C9xd-yk4gdJ_Dzs6NoJ9Sill3XNKDcFQLq-JczZORoVvu7Sb3U602uMZmRNnCCcubw6318P7-nz0B1qcOTzxOKEYUI3y1T4bM9-o_Wm_tZr_QLctsG1pz33-3sWP98pHPzTllp6sgwPTyuO7wtg03PzL_32pGICWLb359-_r3qEfPM2x5uGNhyLeWIENFgZfI-cg75Wds4wdgIoxWoVpoRMtxRJ2ew7zOeBqoKsS-6cG6KJ_IyZAHn1k7sm9TERK10B98SLdyGgmWC36SqVJcLjUktBJjvJ1J_Znp9z-qHZCkU4SAGWw1aarbD5mhg2G6LVH0aaw22LfTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینک از وضعیت سرعت کانفیگ ها که بخاین تبدیل کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/IranProxyV2/8345" target="_blank">📅 19:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8344">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن   ایدی ادمین…</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8343">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">محمدرضا عارف از سوی مسعود پزشکیان به‌عنوان رییس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8342">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن
ایدی ادمین
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/IranProxyV2/8342" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8341">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کانفیگ های پروکسیو یه تست بزنید مستقیم وصل بشید بدونه هیچ پروکسی بیایید تل ببنید بالا میاره و اینکه احتمالا ۲.۳ روز دیگ کانفیگ هاتون کلا عوض کنیم  یه تست بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8339">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J-wNxuwfrnINaB065f6Ir1xr8qGmNnLEeDY-wU3AW3YAxVZ5xc6Z0cjTL8EcR5VL0vTno4sxa8z6IbXpqhV9xpxPFZM99YWGP3GOJAyP4duBTu190tn3ST26-CNCho6q3_mVrlFs6ogq0OKkUOBzWxBWxIScvINH6zQf7rAypAz0LL0yg4dh35lauvc-59kF9ITRMgTxEJXnIW9_JAhAhR5HTCp9OA2Od_WgDCURyu257jc3Vzcw9HUtV1mCMyL7UEM7xVjWat4Opi5o9GP22pBXjb_G2FGjnw4RG0pJtljVPF93EolTD_7vGR0nTPInSfBE2dqFbF7woTkOZlH2Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خدایا شکرت؛ دیروز اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/IranProxyV2/8339" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8338">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">معاون ارتباطات شرکت مخابرات ایران: اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/IranProxyV2/8338" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8337">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/IranProxyV2/8337" target="_blank">📅 13:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8336">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/IranProxyV2/8336" target="_blank">📅 11:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8334">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kiuOHcGkAAPS0OV8tSbNqDkaO8zr-kYr-zs5-J5PuSw_WOX-Zq87yWt1zLk3bOo5UTzUxpF3bioc1CxFtjb-mvlchFIgfZ7GL5bM8HKlTqL-Wt7F7vLsuClX5rwKs3adnoeYAkp7Cq8Tm0XJ5Wdhw7leZ8RjEwcuPhZlTbTwv6e6vG-Aiy6UR6RfdgrEorU6ivRgrmBE-glwCt2nw9rpdgu1_LpRO79KDmGCPrKerOKplH2xi4RT9FH3A4qrPysLrYM8TUZOyP_UJ4yPyVp5AnzFkf33hid9lIMxmH4JU9gyeEy1TcVbhhZB-xodCeKXI6TCfwLUUM-RRONs8oBB4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CTY7GW1IrLJjYuXMPj2qOTczpp_XlQnGjpwgBJgGmsnlulqc5nXxM2yc_lqR7DZ1Q0fN5H32rkdyK0ySLG4KhFU5A0bjCV23CRFi_PkqsY62zW4fPzSXgwKqCE1CY12pxuhSxZ2FG33DC818l4g6bxIpHdSDzh_uRISd3owISu_sGnOxXVN1g1ZK59dcEO8gzv1KDu8ssCFepVJpTEzD9J0DbIi3maWfOOi4_ARiNQyNOz-7O3-I3__5-BNJnsTg67j8Re9NBnuahmFGEEm8nFDlIT5YZWrakBW9Fd6fT3UDP_A0xlIOi99PIjnDGTjAKeaoXqUT2MrnLqLZm8fVYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صنف کفاشان و اغذیه فروشان هم شامل دریافت اینترنت پرو شدن.
به‌زودی کل مردم ایران شامل اینترنت پرو میشن که دقیقا همون اینترنت قبل از جنگه فقط به جای گیگی ۵ هزار تومن باید گیگی ۴۰ هزار تومن پول بدید.
و فقط اونایی که توانشو دارن میتونن از این کالای لوکس بهره‌مند بشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/IranProxyV2/8334" target="_blank">📅 11:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8333">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">قیمت‌ «سیمکارت سفید» و «اینترنت پرو» در بازار سیاه چقدر است؟
🔹
اینترنت پرو و دسترسی بدون فیلتر از طریق کانال‌های غیررسمی و بازار سیاه فروخته می‌شود.
🔹
قیمت ۵۰ گیگ اینترنت پرو در بازار سیاه تا حدود ۱۲ میلیون تومان اعلام شده است.
🔹
سیمکارت‌های سفید با وعده اینترنت بدون فیلتر با قیمت‌هایی بین ۴۴ تا ۱۲۰ میلیون تومان فروخته می‌شوند.
🔹
فقط اقشار مرفه توان دسترسی به اینترنت بدون محدودیت را دارند و این مسئله شکاف دیجیتالی را تشدید کرده است.
🔹
کسب‌و کارهای آنلاین و دیجیتال از محدودیت اینترنت و هزینه‌های دسترسی آسیب جدی دیده‌اند /اقتصادنیوز
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/IranProxyV2/8333" target="_blank">📅 10:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8332">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://45cd71df-7b23-4568-8677-fdc4a0daa76e@protectnet.cloudinohost.com:443?security=tls&sni=protectnet.cloudinohost.com&alpn=h2,http/1.1&fp=chrome&type=ws&path=/&host=protectnet.cloudinohost.com&encryption=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/IranProxyV2/8332" target="_blank">📅 03:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8331">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✈️
Slipnet
slipnet-enc://AcwwsvYl4r7DajFRU6wa12enHS94jGWcw63dYwNxwSzZZDO03mNtFG6vROd+UO8opWIgDZkjjnUHlVvSaj/HvKW+p2HLBc4ETWvUWsMZpCwiUmAeEORd+qfA089iU7PBEHuvMqTIeRqwCA6OyylmfHRyIlB+dS4avIQQAJLxeW6G0ZMnp8HZ4VPpuiN2Vs3U7StRqxSwEP7f8wUXQy1DHgcCE9WD74CKd5RxaHADsaaT4Qj56xDB+DTB8l41JtvrbtjUVSNCS349vS8XyPhXi12t/YaAupzBKzSkPCXi8UjM8Ft2AyUuvLKTPgSMjJgI+vBT+16sztR9Q5n88GbrLNNWKD31CXYgjS4YNk8tLooUjYBgOKWmoBPVWCHej1RPyjs3lg64enMfTyX+WKjZ/fxrqH/8uGQZGj7qLjcGhGaohjHujN+ODCfxxAlK+6Y6eQFfld7UtXfyz9cTmhkk7mebn5exSrIv9o1auX6VVjUQ8xLMvhf6wwsD6vwQsblA6QeIvDoD8NUOfeKZFKrraoPjEdJexjOxcn9gbWSEM/QeqZB/lQ4LnfH6zHtP8PmH63PRZJTZUv6VlAovbrtWUp0ziB5fgISZTC4akBfBPTO32WXUTj+Wo1sSSeCH1rfVQAYoMqoQusLWWSHLm5Llfz5jW8qGwROFKxCq6HYzt4gLRZixvL44Dluxo+oyG14jHwsAmPVh05xydwjCI2XcpiJgX5De91xk+x39xMt7AwApPsraUbzuBscA/TU90Ehahp5NbRa0nr1Z44yGL0dC78sWZrPT5XtXbIE+Ydpd5qq3F1Y=
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/IranProxyV2/8331" target="_blank">📅 03:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8330">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
اطلاعیه سرویس سرور های تلگرام
⚠️
به دلیل شرایط پیش امده و قطع سرویس های تلگرام توسط دیتاسنتر خارج سه راه برای برطرف کردن مشکلتون وجود داره، دقت داشته باشین که این مشکل فقط رو سرویس های تلگرام هست و سرویس های تانل تو ربات هیچگونه مشکلی ندارند.
1⃣
- روش اول…</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/IranProxyV2/8330" target="_blank">📅 03:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8329">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/IranProxyV2/8329" target="_blank">📅 23:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8328">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/IranProxyV2/8328" target="_blank">📅 23:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8327">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سوال اینجاس اینا از بازی ها هم میترسن باز نمیکنن حداقل مردم حوصلشون سر نره
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/IranProxyV2/8327" target="_blank">📅 23:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8326">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✈️
علی قلهکی، خبرنگار:
🔻
تا امروز بیش از ۴۹۰ هزار سیمکارت پرو فعال شده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/IranProxyV2/8326" target="_blank">📅 22:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8325">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">💎
𝗩𝟮𝗿𝗮𝘆𝗡𝗚 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻 or MahsaNG ( Psiphon)
vless://799f939b-964b-4416-84ac-18a6ace7fe70@camp.nahidapp.com:443?path=%2FIF_VPN_Bot&security=tls&encryption=none&insecure=0&host=camp.nahidapp.com&type=ws&allowInsecure=0&sni=camp.nahidapp.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/IranProxyV2/8325" target="_blank">📅 21:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8322">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlivU2oSstYDIKqlMVr8aquWffIKKAeKincW7JrNA5o3XPjz6FxQNWA7xCi5fooB87CZOs3scBOeEpetD9YlunNI9H6IgV834FhVYWKphQrd68-acNjBNsuzLTTz4rg5KDrobUZFM9GV2IaDClNBnwwch-59-tSXx1uRcEeVMNuftw81F2Gj9IBW6-YHFG_Fh7ajT2PSpwuiTyRWZ8N4l_Yb1nvWT8327UiNKxlGPK9IoC-Exf4AXyrDlpCyj77TpQQORBllvcs8xJ3U6Eo2c1fZqCX8rJvQXw0oy1DRn-53cLqovPNB-zUeE0FSoxPCyjkMlt_BOxVuJViu_kFYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
وعده پزشکیان بالاخره درباره اینترنت :
◀️
ارتباطات و اینترنت به بخش جدانشدنی زندگی مردم تبدیل شده
‼️
به آقای عارف ماموریت دادم با لحاظ حساسیت‌های حکمرانی، نظر رهبری و وعده‌ای که به مردم داده بودم، در قالب ساختاری چابک موجبات خدمت‌رسانی بهتر دولت و تحقق انتظارات عمومی رو فراهم کنه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/IranProxyV2/8322" target="_blank">📅 21:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8321">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
اطلاعیه سرویس سرور های تلگرام
⚠️
به دلیل شرایط پیش امده و قطع سرویس های تلگرام توسط دیتاسنتر خارج سه راه برای برطرف کردن مشکلتون وجود داره،
دقت داشته باشین که این مشکل فقط رو سرویس های تلگرام هست و سرویس های تانل تو ربات هیچگونه مشکلی ندارند.
1⃣
- روش اول بدین صورته که شما کانفیگتون رو برای پشتیبانی ارسال میکنید و همون حجم باقی مانده براتون با ضریب دیگ چنج میشه به سرور ثابت البته با سرعت کمتری
2⃣
- روش دوم سرورتون تبدیل میشه به سرور تانل با سرعت بالا مث سرویس هایی که درحال حاضر در ربات هستند ولی، ما به تفاوتی باید پرداخت کنید بلا عوض
3⃣
- روش سومم اینه که کانفیگ هاتونو نگه دارین بعد از این شرایط نت از حالت ملی به حالت بین المللی تغییر کرد به ازای هرگیگ، ده برابر اضافه تر حجم دریافت خواهد کرد
🔻
@RUSSIAPROXYY_Admin
📌
به این آیدی جهت رفع مشکل پیام بدین
👆🏻</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/IranProxyV2/8321" target="_blank">📅 20:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8320">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtO60Nk-fh6BSUw1_1DM7_2AElVnHQIF7VUK9gT9y7oYG4N1ncMxh1Ib00swg_SLRQutXY6jJ-p4y1Mbn-rjq72vDMZYPDKDx9sSPcB5Gz0vNtBDXdh8WAmgOtyP1Fo8lLXjH_i4tW-nQJTr1mSHNMO-oB-OAAbcXgNcLrqXGm298eLGw-Rp4zrD5rjtgAn-lb_QXghV4zP8vj5QfqraeIb0QA8dVjx3fsON4tAsXBzn0_EgnTuIBnGPwWCdebw5--tv1tvtUYw8i6p2Z9sDzjfozguw3Rvt6msJo7HEXq3yJuZqu-fzPrynz8KLin34FfwE9sWDDcnZO14mZPTJKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت اینترنت پرو
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/IranProxyV2/8320" target="_blank">📅 20:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8319">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✈️
دوستان نهایت تا امشب سعی میکنیم سرویس سرور تلگرامو اوکی کنیم، هواتونو داریم همونطور که وقتی هیچکس وصل نبود تو دوران جنگ با کمترین قیمت ممکن و کمترین سود ممکن بهتون بهترین سرویس ارائه میدادیم، سعی میکنم از جیب خودم هزینه کنم تا مشکلتونو برطرف کنم نگران نباشید
✈️
سرورای ثابت برای نت بین المللی و کلیه اپلیکیشن ها و سایت ها و... براتون تو ربات با کمترین قیمت ممکنه قرار دادم بازم امروز
قیمت هارو کاهش
دادم که دوستانی که شرایط مالی مناسبی ندارن هم بتونن کانفیگ تهیه کنند.
✈️
🎥
📸
💬
👾
📞
🤖
🔍
🕹
📱
⚡️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/IranProxyV2/8319" target="_blank">📅 18:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8318">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de826422e1.mp4?token=iKRoixCbVCq9T0BzBKw1yG5P6dfaqoFlXBf1xtLmBSaY9HlOVv2cMwLtRbG393pA12oTRs8lISIwLXa6AAmZGnNMxG5NYlyFr3JeQspAjy2ImgaFYL5cavaepLpmmGnIXvQ3YHI_0VQQIy394uElJUzBej5epyhGGhuGOgRWhKWrojPIGoyV-FOa4sDZBvxPQXg6MWGHZ7iYYqwtZDaZUj5WG1EAAhBm96Tw7ZjWQX-Yhw6mMd7Yceyl8bQAbnSZc_qUPlAZ522eit7Sg9429TSWIVrGiZ--grjk4W_PXYEfWmfpeL1ASOKvIk4weqvvZTTl3EpcWnqpOJB-7N1v5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de826422e1.mp4?token=iKRoixCbVCq9T0BzBKw1yG5P6dfaqoFlXBf1xtLmBSaY9HlOVv2cMwLtRbG393pA12oTRs8lISIwLXa6AAmZGnNMxG5NYlyFr3JeQspAjy2ImgaFYL5cavaepLpmmGnIXvQ3YHI_0VQQIy394uElJUzBej5epyhGGhuGOgRWhKWrojPIGoyV-FOa4sDZBvxPQXg6MWGHZ7iYYqwtZDaZUj5WG1EAAhBm96Tw7ZjWQX-Yhw6mMd7Yceyl8bQAbnSZc_qUPlAZ522eit7Sg9429TSWIVrGiZ--grjk4W_PXYEfWmfpeL1ASOKvIk4weqvvZTTl3EpcWnqpOJB-7N1v5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شهبازی مجری صداوسیما خطاب به مردم ایران:
اگه اینترنت 5G که افغانستان داره و مسترکارت که سوریه داره اینقد براتون مهمه؛ خب برین همون افغانستان و سوریه زندگی کنین!
﻿
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/IranProxyV2/8318" target="_blank">📅 16:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8317">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ایران اینترنت ندارد، روز هفتاد و چهارم …
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/IranProxyV2/8317" target="_blank">📅 13:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8316">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⭕️
اطلاعیه:
وزیر ارتباطات گفت در تلاش برای برقراری اینترنت بین‌الملل در اسرع وقت هستیم.
همچنین طی پیگیری‌ از ISP اعلام کردند که اینترنت بین المللی شبکه خانگی متصل شده است اما هنوز زمان مشخصی در مورد اتصال دیتاسنترها به اینترنت بین المللی وجود ندارد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/IranProxyV2/8316" target="_blank">📅 12:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8315">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde1d5a77d.mp4?token=BWUScjPkJKLmoYHcEDE75xCH9OwgjMDXzolgmsqL_r8L5_iFTetTntBd4QA-AqDGJVWBrwc6r1L9WYhABkEFbmBcrVhyE2twuzRc5kdSC-qIglZRZsuqawintCR16j5BPOcW-SHI5N8mnOq2YRZ7jlmAchaiFSt-Qj8Vh3b4UCjcVy2KI7isrFgGo_qOpBHW7VGA3dPNt_ASqIPR0Po2EA9OEBGDuVgjBhSF-QBRBaZOtrdqRmNJN9ZUKWy1OGiTDBELp_Yx8exxtgFnwglK3QchychSCmo7eThTTcnGXDYxoZx_-RcUaFvPT-MbUB2lVRTZGudleo6jMk7Kvgwbaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde1d5a77d.mp4?token=BWUScjPkJKLmoYHcEDE75xCH9OwgjMDXzolgmsqL_r8L5_iFTetTntBd4QA-AqDGJVWBrwc6r1L9WYhABkEFbmBcrVhyE2twuzRc5kdSC-qIglZRZsuqawintCR16j5BPOcW-SHI5N8mnOq2YRZ7jlmAchaiFSt-Qj8Vh3b4UCjcVy2KI7isrFgGo_qOpBHW7VGA3dPNt_ASqIPR0Po2EA9OEBGDuVgjBhSF-QBRBaZOtrdqRmNJN9ZUKWy1OGiTDBELp_Yx8exxtgFnwglK3QchychSCmo7eThTTcnGXDYxoZx_-RcUaFvPT-MbUB2lVRTZGudleo6jMk7Kvgwbaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهاجرانی:
اینترنت حق مردم است؛ عصبانیت مردم کاملا درست است/ عامل این عصبانیت دشمنانی هستند که باعث می‌شوند فضای امنیتی ما مخدوش شود
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8315" target="_blank">📅 11:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8314">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اژه‌ای: اینترنت پرو و سفید مثل پتک در ذهن مردم شده است
🔹
رئیس قوه قضاییه در جلسه با وزیر ارتباطات: مسئله‌ اینترنت پرو و سفید مثل پتک در ذهن مردم شده و باید با موارد خلاف قانون در این موضوع برخورد شود.
🔹
در این جلسه دادستان کل کشور و وزیر ارتباطات به رئیس قوه‌قضائیه گفتند با بررسی‌های صورت‌گرفته، احراز تخلف در قضیهٔ موسوم به «خط‌های سفید و اینترنت‌پرو»، قطعی و حتمی است./جماران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8314" target="_blank">📅 11:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8313">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">vless://8b7dbddf-fe0a-4405-b8e9-bfac4d9439ef@185.143.233.235:8080?path=%2F&security=none&encryption=none&host=MHI.ARTARONA.IR&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/IranProxyV2/8313" target="_blank">📅 11:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8312">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">V2ray + Psiphon:
vless://3728fc28-910c-4a9c-888c-c08c3e2f4a06@snapp.ir:2052?encryption=none&type=ws&path=%2Freq2&host=snapp1.gptpersian.ir#musiclovers85
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/IranProxyV2/8312" target="_blank">📅 10:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8311">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">احتمالا اکه پروکسیا درست نشه با کانفیگ های ثابت جاشو براتون عوض کنیم اطلاع میدیم خدمتتون بابت صبوریتون متشکریم</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/IranProxyV2/8311" target="_blank">📅 00:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8310">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حجم سفارشات ربات بسیار بالاست موجودیش تموم شده بود مجدد شارژ شد، صبور باشین، دارم یکی یکی رسیدارو صحت سنجی و تایید میکنم با تشکر
❤️
💲
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/IranProxyV2/8310" target="_blank">📅 23:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8309">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAq-y2ACaUnVElr48fX5GGFttyafaxryWkS8tn6lPrF4PBeIjqaSm9dIJwgrxH0R1XcJLgJZjfvL03vVMoD3MrLsPdU6scXlcyaveN0ndo8m9cviuGRqq522VdRxOuMCBrHRB91icAM34lzuTCYQk-eDUrA6svbYzxZJ-WKPiQ4WfIa64pexsL3SgQ0O67n_4GYWDZNRLbu4eJHtvf7VrSX8huY4gvHz6txsxVaor6ysev0ITP8_C9PUBcMrMF33VlO0-VaV8Odz8VtE3UwcWBSGllhzk8GSrDS2JrV6M2BoWqd7GgYZIhuVTMg8lLKaz22Xwc6Oz1D_oUytXlKkPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایزه چالش دیشب، برد 2-0 بارسا درست پیش بینی کرده بود
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/IranProxyV2/8309" target="_blank">📅 23:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8308">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
معاون علمی پزشکیان:
حتی در شرایط جنگی هم بستن اینترنت راهکار نیست، زیرا وقتی کامل بسته بود هم ترورها ادامه داشت.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/IranProxyV2/8308" target="_blank">📅 21:00 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8306">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⚠️
ترامپ به فاکس نیوز:
‼️
در حال بررسی از سرگیری عملیات «پروژه آزادی» هستم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/IranProxyV2/8306" target="_blank">📅 18:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8305">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f5f6fd683.mp4?token=FqfMPiDin84PN8XhtSRyNpg8N86cjPVgOOVHskyQF7xx1VpEiEssE5-2IOXviTM1jYA3ailv1CMUv1pv1_HuZtlh9Xdh0aw-jVDInnSNh0f38LeSK7yQVoEYk1au9SHpi_TFIwKeHMnkELk3elHjYnwne9opRWRE8VegaQALXoOVzKUKI2o3cCT8_2hWdeFq-W8vIsZvqj63BMjE_rXjZUqEs5ZxU6-N9Dkg8mk8qlQ6WfQQ1AHSjDkKaNy3npQhVr88bF3pJJUg5uvS0ezow19rl3A0CYpluS6PUcKUYbhiQIwk75JM7cuactZ4x66KDmzM5ioGd7lgiQqcF3qqVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f5f6fd683.mp4?token=FqfMPiDin84PN8XhtSRyNpg8N86cjPVgOOVHskyQF7xx1VpEiEssE5-2IOXviTM1jYA3ailv1CMUv1pv1_HuZtlh9Xdh0aw-jVDInnSNh0f38LeSK7yQVoEYk1au9SHpi_TFIwKeHMnkELk3elHjYnwne9opRWRE8VegaQALXoOVzKUKI2o3cCT8_2hWdeFq-W8vIsZvqj63BMjE_rXjZUqEs5ZxU6-N9Dkg8mk8qlQ6WfQQ1AHSjDkKaNy3npQhVr88bF3pJJUg5uvS0ezow19rl3A0CYpluS6PUcKUYbhiQIwk75JM7cuactZ4x66KDmzM5ioGd7lgiQqcF3qqVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت زندگی مغازه دارا و آنلاین شاپا بعداز ۷۴ روز بسته بودن اینترنت!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/8305" target="_blank">📅 16:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8304">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
تصمیم‌گیری درباره بازگشت اینترنت به وضعیت عادی در دستور کار دولت
افشین، معاون علمی رئیس‌جمهور:
🔹
در دولت یک کارگروه زیر نظر معاونت اول رئیس جمهور برای تعیین تکلیف اینترنت در حال شکل‌گیری است. احتمالاً در این کارگروه تصمیمات قاطع خواهیم گرفت.
🔹
وضعیت اینترنت در دولت در حال پیگیری است. نظر دولت بازگشت اینترنت به وضعیت عادی است. قطعی اینترنت قطعاً به رتبه علمی ما ضربه می‌زند. در زمان قطعی اینترنت رتبه علمی ما پایین می‌آید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/IranProxyV2/8304" target="_blank">📅 16:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8303">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">dalage pezeshkian 2.npvt</div>
  <div class="tg-doc-extra">1.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8303" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/IranProxyV2/8303" target="_blank">📅 15:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8302">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">داریم بروز رسانی هایی میکنیم که  سرور های مخصوص تلگرام مستقیم وصل بشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/IranProxyV2/8302" target="_blank">📅 13:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8301">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_0WPw6NJa4xn2-TYdKmGuMhRPeJ6pr4ttbbzU8IWdH4mnoMzDqRSgqd6qjaNMwyP89t0TNI8i-mY6nWnrLAHP4XsSg0ZuzY-m400IY6ScsBS-HZFBaN8kMJvBkEgBKFYkg8CXFNaTnxyTzp5H87lnWBi_2iVBtU2qzlGPp_rdHb9jJTkwV4pqgWACNjY-S62VvWOcZojaaRlnLfNv85bWuxRIdRN2exfg5ykQ8jY6-iKfNV38qxZkR_hVYc5zuC9IjUDYQQWVFiq9VHeax-k07Hpm2YfJBAwQRCEazLafM8rMoWibiY2GGlL9CYEv4mhxir7ubWNhV9NMBoqFZT7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
جهت اطلاع رسانی مجدد همچنان در تلاشم، که مشکل دیتاسنتر خارجمون رو برطرف کنم برای سرویس سرورای تلگرام، درحال حاضر همچنان فروش سرورای تلگرام از دیروز تو ربات غیرفعال شده، نگران نباشید برطرف خواهد شد
✔️
فعلا درحال حاضر سرویس های تانل با بهترین کیفیت و سرعت ، تنها سرویسمون که روی تمامی اپلیکیشن های
🎥
📸
✈️
💬
📞
🤖
🕹
📱
🔍
قابل استفاده میباشد و برای تمامی دیوایس ها واپلیکیشن ها اوکی هست، در پلن های (1 گیگ، 2 گیگ،3 گیگ و 5 گیگ) تو ربات موجود میباشد برای ثبت سفارش
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8301" target="_blank">📅 03:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8300">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
صدا و سیما:
ایران آخرین پیشنهاد آمریکا را رد کرد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/IranProxyV2/8300" target="_blank">📅 01:43 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8299">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اختلال شدید در اینترنت داخلی
🔵
متاسفانه از دقایق گذشته اختلال بسیار شدیدی در اینترنت ملی ایران رخ داده به طوری که cdn آروان ؛ سیستم شاپرک ؛ سیستم همراه بانک برخی از بانک ها همچون بلو(سامان) و... قطع شدند یا دچار اختلال شدند.
🔵
بسیاری از سایت های ملی و داخلی نیز باز نمیشوند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/IranProxyV2/8299" target="_blank">📅 00:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8298">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رفقا پروکسیا مشکل خوردن مدیر فنیم داره هر جور شده مشکل حل میکنه از صبوریتون متشکریم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/IranProxyV2/8298" target="_blank">📅 00:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8297">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نتیجه رو زیر این پست پیش بینی کنید   @RUSSIAPROXYY
🇷🇺
پیامتون ادیت بخوره، قابل قبول نیست
❤</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/IranProxyV2/8297" target="_blank">📅 00:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8295">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
ترامپ: من همین الان پاسخ به اصطلاح «نمایندگان» ایران را خواندم. این را دوست ندارم — کاملاً غیرقابل قبول است! از توجه شما به این موضوع سپاسگزارم.  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/IranProxyV2/8295" target="_blank">📅 00:14 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8294">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEFBTy-AtJfEF2Wx-H9gVsrfhoa-kk7jtlgn1tt7mEAYM_wrgF3xTHwDjAz7Aokonz32q85bTcsmVizKTRJZByejZyIWvPEw93bA5Sv9CnO5y5x64sWwQgW-77H7e8KrubcnRn6sCcHfZt1LMH-zJmJfJO2hPWAUBa0H9jDemJ_hFl7vWELCtE-MH24EWRDIRTAmAwztLQKhWLm5QPd-SQsDBUnb_vqIF2mChOQyxiamWk-wW1KX1m1EvuduZwlLFOsl2QsLtPzZ3zvF2eXolKmH9mWX4HuTJM4ul1XWMqT3cxJY6xhM1IFzm4-uU7HWnyKYIqD0ZOUWS26GEvXIIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ: من همین الان پاسخ به اصطلاح «نمایندگان» ایران را خواندم. این را دوست ندارم — کاملاً غیرقابل قبول است! از توجه شما به این موضوع سپاسگزارم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/IranProxyV2/8294" target="_blank">📅 23:59 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8293">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نتیجه رو زیر این پست پیش بینی کنید   @RUSSIAPROXYY
🇷🇺
پیامتون ادیت بخوره، قابل قبول نیست
❤</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/IranProxyV2/8293" target="_blank">📅 23:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8292">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=rjnFN8tVFA5R-b6OqLA4L-QK6DSqLOGsX0hPUkGAqV5KNy2Lb2XG7EfO_f4YJ9Coe7ls56zlgZ_0vK89QmpSF2sIISLChzuzNMq9egguigUAJGMg9ayacyMeEICCtdTjXSFooWe13G0Oj82aGdGO_gqLTjSD6IaTlYwIP0dox2OMHhp0O0UJDlW4e2sGpr1fkvAnQhY6tcwSiuOlru6ulxgtSApN8AncXdFNVbS4B5ZYw7f7UFfL-SftuIwJFP0Da3P5in2QV5uuRgzhQ4PYvkOGAGGn3XKHhqa1Ct-v79IYzFwJijYcVOMvRrRui1hUz0V5AdM4jVmvplTrxIPAwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=rjnFN8tVFA5R-b6OqLA4L-QK6DSqLOGsX0hPUkGAqV5KNy2Lb2XG7EfO_f4YJ9Coe7ls56zlgZ_0vK89QmpSF2sIISLChzuzNMq9egguigUAJGMg9ayacyMeEICCtdTjXSFooWe13G0Oj82aGdGO_gqLTjSD6IaTlYwIP0dox2OMHhp0O0UJDlW4e2sGpr1fkvAnQhY6tcwSiuOlru6ulxgtSApN8AncXdFNVbS4B5ZYw7f7UFfL-SftuIwJFP0Da3P5in2QV5uuRgzhQ4PYvkOGAGGn3XKHhqa1Ct-v79IYzFwJijYcVOMvRrRui1hUz0V5AdM4jVmvplTrxIPAwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی و فرماندهای سپاه:
@
RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/IranProxyV2/8292" target="_blank">📅 23:37 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8291">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvCAoqn3hhkZU0_X_HYKowLdXzpNEO-nu1ZFAzfJpWk1qhAT1TPVwAc5HRG12FDQe9NoujG9fJP6Uch3rPSOCfpY70K5ohXitvIRw4fHfUw154oT0W6Vo2hbUPkM-epT1wYVIoUFNNNO3qGxQO234SU34srXXFklsWvyVfsQzIXk8e2nCtAcL5lwvxKTl9sM5kp59ijkvoC0ntY_2DEl7vZxlErqQFMZbYyR6AZ0P8zrglx-kJWzqneRC4BUErD9rPp4js_0amc1aZU4gmgTpIVSjwNrybaYj7b72Aaa7HFfWgfUZswCy8bAYuCt4I2dZ8yPTu4_NimDfbkTuGqxfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ: ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)  و سپس سرانجام وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» آنها رسیدند.   او نه تنها با آنها خوب بود، بلکه عالی بود، واقعاً به طرف آنها رفت، اسرائیل و همه…</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/IranProxyV2/8291" target="_blank">📅 21:55 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8290">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzE6YujdRx-B8FaM20wGuHOc5wkql6MwGOog02ylnipNktiRu694Lm6FShh4kMLp-hZ91N3bBV4HPaS3glIL670IgimXIz6thkQuQR6CqG5OCutGqUG89NAbVtzVsKPFlXYvyFYqhVV9-7RBZMCJ3MZt3vA8ZJ61dN1qbUXfW__AwaLJzsF45cvzY4S6f9VXV6hocO-goRirNS0dYR6JxTxAZ1TW0pepy_v8F8tCrYKGWAY1krDvny4wDWa86ekviIwTDEQv27NNjYcggFGtc4aK7Yki70JSS5mJLuqkgwKH1jzvGv2Zl5OPym014m6L_TgT1c2EghUNVndcvfAHmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ:
ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)
و سپس سرانجام وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» آنها رسیدند.
او نه تنها با آنها خوب بود، بلکه عالی بود، واقعاً به طرف آنها رفت، اسرائیل و همه متحدان دیگر را کنار گذاشت و به ایران یک فرصت جدید و بسیار قدرتمند برای زندگی داد.
صدها میلیارد دلار و ۱.۷ میلیارد دلار پول نقد سبز به تهران منتقل شد و روی یک سینی نقره‌ای به آنها داده شد.
هر بانکی در واشنگتن دی‌سی، ویرجینیا و مریلند خالی شد — اینقدر پول زیاد بود که وقتی رسید، اوباش ایرانی نمی‌دانستند با آن چه کنند.
آنها هرگز چنین پولی ندیده بودند و دیگر هم نخواهند دید. پول‌ها در چمدان‌ها و کیف‌ها از هواپیما خارج شد و ایرانی‌ها نمی‌توانستند خوش‌شانسی خود را باور کنند.
آنها بالاخره بزرگ‌ترین ساده‌لوح را پیدا کردند، به شکل یک رئیس‌جمهور آمریکایی ضعیف و احمق. او به عنوان «رهبر» ما فاجعه بود، اما نه به بدی جو بایدن خواب‌آلود!
به مدت ۴۷ سال ایرانی‌ها ما را «گول زده‌اند»، ما را منتظر نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای کشته‌اند، اعتراضات را سرکوب کرده‌اند و اخیراً ۴۲ هزار معترض بی‌گناه و بی‌سلاح را از بین برده‌اند و به کشور ما که حالا دوباره بزرگ شده است، می‌خندند. آنها دیگر نخواهند خندید!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/IranProxyV2/8290" target="_blank">📅 21:51 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8289">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✈️
جدیدترین آپدیتِ تلگرام
🌐
[ ورژن : 12.7.2 ]
- لینکِ دانلودِ داخلی ( بدونِ فیلتر ) :
✉️
Telegram ( Direct ) [ v 12.7.0 ] :
https://uploadgirl.ir/d/c99c188e-57fe-469c-91ce-843a37e803f3
📌
خیلی مهم : فایلِ آپدیتِ نسخه ی Direct هست و در صورتی که نسخه ی Direct رو نصب دارید دانلود و نصب کنید ،
+ فایلِ نصبی داخلِ یه فایلِ Zip هست که باید استخراج کنید و سپس نصب کنید .
+ اعتبارِ لینکِ دانلود : 3 روز [ لینک آپدیت می‌شود . ]
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/IranProxyV2/8289" target="_blank">📅 20:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8288">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔜
به دلیل مسائل فنی، و ارتقا سرور تا فردا فروش سرور تلگرام بسته خواهد بود، فقط تا فردا بستس،مجدد فردا باز خواهد شد درصورت رفع مشکل و آپدیت همینجا اطلاع رسانی خواهم کرد
✉️
◀️
درضمن توجه داشته باشین که پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات شارژ شده با قیمت…</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/IranProxyV2/8288" target="_blank">📅 20:02 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8287">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_L0JwsWKCY0zfX_m3qkNVPxZPmMGsxf-Og50taVB1ELAaodmRQ6Uc1tjDv1X9Goohs_yJbQN9kko9o12IKfegnln2Dx49_2pc6Ydg6hh3x7l0AmJVoqH0Km3YgQDspbd5FtCiGA8MuPWYRukyocjj0F7pLS2MTOVxE4okojRvHPNFmWTzwN6RJAfbhCXBZil2-tqalltZF_fPXsOyEz1MDCqQCKjj6ked-3mKx_6iiwc7ky4qEWk9-oAlcAbNb1SXI-r_72ijo2-5movNvMEUfSXappEQn8RSua-RApD_osEb_shyUKXLzgxjzE1uQ8KWjG7L-lLEruzXeJf3lQDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔜
به دلیل مسائل فنی، و ارتقا سرور تا فردا فروش سرور تلگرام بسته خواهد بود، فقط تا فردا بستس،مجدد فردا باز خواهد شد درصورت رفع مشکل و آپدیت همینجا اطلاع رسانی خواهم کرد
✉️
◀️
درضمن توجه داشته باشین که پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات شارژ شده با قیمت مناسب قابل سفارش هست، برای استفاده در تمامی اپلیکیشن ها و سایت ها
📹
✉️
📷
🐣
🔻
@RUSSIAPROXYY_Bot
⚠️
پشتیبانی از فردا ظهر ساعت ۱۸ تا ۲ شب پاسخگویی سئوالات و مشکلات شما میباشد
❕
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/IranProxyV2/8287" target="_blank">📅 19:39 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8285">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dq34Vzt-ccHefHEacVqsUrUR41DhuF0IRPtvTj5DPa_kRtqujOc1s53cLoAsprHN70XlLiU2DzJklGpuxvC7emPIJVGbtBEUytv_8-VrEH5fSM3tRlQQMvlh6dAEm9PO9RJQSnjU8jPEOKd6wraaEupBWGVGY7YdPGU9gUWNu9NKP-caS-JdpiQRXkkYdUYT78qD4KcI9XCoBNMpHE6poIONuNpylDmWydUTTrOs45fneG-3bN3CdMZXINfCWCaod-1qiCsHbXFD82g1ZNSew8FPG957M2cySx2n5QFLMBFHif-UCyJDbbqtmWDvsh66FI_Yfo7YGJJOiOLd8g9NBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رییس کمیسیون انرژی اتاق بازرگانی:
سال گذشته هر هفته ۳ تا ۴ روز خاموشی ۲ ساعته داشتیم ولی امسال تمامی روزهای هفته ۲ ساعت قطعی برق خانگی، تجاری و اداری داریم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/IranProxyV2/8285" target="_blank">📅 13:57 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8284">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نتیجه رو زیر این پست پیش بینی کنید
@RUSSIAPROXYY
🇷🇺
پیامتون ادیت بخوره، قابل قبول نیست
❤</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/IranProxyV2/8284" target="_blank">📅 12:32 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8283">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کامنت هارو باز میکنم پست بعد حرف نزنید فقط نتیجه رو بنویسد به نفع کیه
از اونجایی که خودم بارساییم 3.1 به نفع بارسا میشه</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/IranProxyV2/8283" target="_blank">📅 12:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8282">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یه چالش میزاریم هر کس اولین نفر نتیجه امروز الکلاسیکو رو درست بگه بعد بازی جایزه میدیم</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/IranProxyV2/8282" target="_blank">📅 12:24 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8280">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">‎⁨الکلاسیکوو🔥⁩.npvt</div>
  <div class="tg-doc-extra">2.9 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8280" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/IranProxyV2/8280" target="_blank">📅 12:23 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8279">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پزشکیان جوری اومدی ریدی تو نتا جلیلی تو خوابشم نمیتونست همچین چیزی ببینه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/IranProxyV2/8279" target="_blank">📅 10:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8278">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118c9f04cc.mp4?token=uMLDQfNIVf-uI04xQVwvafgSu5SONrWvmzmsR0OZ-MchZCDSHxlW8rq6HrpFndFrRhuoQVcdwiWfXheyILtNCrkhQBcCYDNvoYoPV1IKtextKwDUGj6rDidNzSZZ84YOE4-Z3V_CzheXzj9ERWp__z_2EJwX_BFPIaKCddvxs4awvQi0K4CNK90adxdklFm4rIY6jftNM_rjam3RFXSTW_eEUrReTGfFMOM6lgTD9MNYwkiaeQYXnk0o3VgJ1yLaW4nIR2eyoMK4Qs3F3oK4RMLWOyeHYnsYyITW4e6t_YYr4KTVlAfSuP_ehnpI5taNkZoKjAJbuqGuZGtIj-bxbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118c9f04cc.mp4?token=uMLDQfNIVf-uI04xQVwvafgSu5SONrWvmzmsR0OZ-MchZCDSHxlW8rq6HrpFndFrRhuoQVcdwiWfXheyILtNCrkhQBcCYDNvoYoPV1IKtextKwDUGj6rDidNzSZZ84YOE4-Z3V_CzheXzj9ERWp__z_2EJwX_BFPIaKCddvxs4awvQi0K4CNK90adxdklFm4rIY6jftNM_rjam3RFXSTW_eEUrReTGfFMOM6lgTD9MNYwkiaeQYXnk0o3VgJ1yLaW4nIR2eyoMK4Qs3F3oK4RMLWOyeHYnsYyITW4e6t_YYr4KTVlAfSuP_ehnpI5taNkZoKjAJbuqGuZGtIj-bxbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری علی صبوری که میگه به مرز فروپاشی رسیدم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/IranProxyV2/8278" target="_blank">📅 09:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8277">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOunBABl-Mj_17T-c_cPSm7w0qBzMAdhh6H6oyO2rTDEV-pEbSPMnsx6fnn1yo8RsAYjTeVSOkSqP98w8-5ADROJ-vRSt6O5OIDgXoDkfSuay_y6mSp_3pKyllGh7zmhCydQRiSNMIho992HdaRbSmNB1UXhbbvQ21h0mIoIaHUH7HLoGzyfGNIXAyu7ibFF1sd4bWqh-GWEYuC36hzIA3WgJWpIq3uz-wercI8RRZDdY6A5E0IlLrOwdvBB5Wo-M0aerdOwy6CLhNogApaHVeYzjRr_P6UUnwZrd4_QEgWppVpkwq6frXjb9wmWd6g2JoEagZ5aa6JVz_VxunLQ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی صبوری بعد این که ویدیویی داد و فحش خار مادر به نظامو طرفداراش کشید
الان این استوری رو گذاشته و گفته بیاید منو بگیرید ببرید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/IranProxyV2/8277" target="_blank">📅 09:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8276">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iR9HfYbD3asFIymu2VIglrlvGAX9QMfuxYehfkF4x_OPi5DfziZ8ZNicUvjCwKTsF7ELXkzsOpKD13QfzJPc2CX7O1amFDQVgWLoRTMkX6eoS9Nib2amR0gbiSTM81ugt4q8iZ4_WKSTqvAPYHzVBC1bQW462Obobdqx_gFmBn37B0Gu7eag6npWVy5S5FfJldyzUZycNQTZkWiIbAxVK_23XUfZOAImitb997jWX8FdEh0CFPn1Evs1UaYev8Yrt6qqriOW0NJZjkedXfI9n4KuDSXNZpTwJnfnEaycxbPTnkTNaONkmzDS0gMJcyI_M50qhLqR5p7sQJTxbumUfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔜
به دلیل مسائل فنی، و ارتقا سرور تا فردا فروش سرور تلگرام بسته خواهد بود، فقط تا فردا بستس،مجدد فردا باز خواهد شد درصورت رفع مشکل و آپدیت همینجا اطلاع رسانی خواهم کرد
✉️
◀️
درضمن توجه داشته باشین که پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات شارژ شده با قیمت مناسب قابل سفارش هست، برای استفاده در تمامی اپلیکیشن ها و سایت ها
📹
✉️
📷
🐣
🔻
@RUSSIAPROXYY_Bot
⚠️
پشتیبانی از فردا ظهر ساعت ۱۸ تا ۲ شب پاسخگویی سئوالات و مشکلات شما میباشد
❕
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/IranProxyV2/8276" target="_blank">📅 04:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8275">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رفیقا پروکسیا اختلال دارن تیم فنیم در حال درست کردنه اختلاله. کانفیگ ها اکین مشکلی ندارن  میتونین خرید بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/IranProxyV2/8275" target="_blank">📅 02:18 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8273">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">💎
دوستان سرور های تانل که به اینترنت بین الملل وصلتون میکنه، هیچ مشکلی ندارن و قابل سفارش هستند از ربات
🔥
@RUSSIAPROXYY_Bot
ولی سرورای مختص تلگرام فعلا درحال حاضر سرور خارجمون به مشکل خورده پروکسیا وگرنه سرور خودش اوکیه، یه مقدار طول میکشه اوکی بشه، اطلاع رسانی میکنم همینجا
❤️
✨</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/IranProxyV2/8273" target="_blank">📅 21:56 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8271">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مجدد اختلالی بوجود اومده رو سرورای مخصوص تلگرام، منتظر باشین رفع میکنم اطلاع میدم خدمتتون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/IranProxyV2/8271" target="_blank">📅 18:23 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8269">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bS4eHyUSUbjz5FvNowWOhPr-7ANVE2VcX6GA5m6TstUbN3UYP9qBaq7bGPDRjzp29o5KPS3el9f8mEyzZcz1VYhrzeN-r3GbiR_o9UN40vMWiYwTWG8R-1E4BwW8GxWg40b10aexUtEo52PY6LiuocYVaA90X0l5dJ5M4VdzlvXNTenb10KJV8_6ohqjrOmF1SxHisRUZBvtKwLcqpIXbs3eBCzDPNNMey-UzyhJTigg6H5HsPVuPHO0r5oMVzPBGzYYjFzD6eXYRIqGTmDSCfZngbWj8fXcyLSzVwNy_E4XLOiID1pJGuvgBbap8FLJEF1QbE85fgZXLhO6KecghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز تست خدمات اینترنت 5G در کابل افغانستان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/IranProxyV2/8269" target="_blank">📅 17:05 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8268">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🤖
چند ربات کاربردی تلگرام
لینک مستقیم فایل رو میدی، تو تلگرام میفرسته:
@DirectUpBot
باهاش فایل فشرده zip بسازی:
@zipyourfilesbot
در تلگرام فایلت‌ رو میفرستی یا فوروارد میکنی لینک دانلود داخلیش رو میدن بهت:
@ICESENDBOT
@catuploadbot
ارسال فایل از گیت‌هاب به تلگرام:
@GithubGitlabDownloader_bot
هوش مصنوعی تایپ سپیک:
@TypespaceBot
دانلود از یوتیوب:
@YoutubeFiler_bot
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/IranProxyV2/8268" target="_blank">📅 16:05 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8266">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کارزار اتصال مجدد اینترنت بین‌المللی:
www.karzar.net/291129
شرکت کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/IranProxyV2/8266" target="_blank">📅 13:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8265">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تلگرام
در عراق رفع فیلتر شد
🔻
سازمان رسانه و ارتباطات عراق از لغو ممنوعیت فعالیت اپلیکیشن تلگرام در سراسر این کشور پس از تعهد مدیریت تلگرام به رعایت قوانین داخلی و استانداردهای نظارتی عراق خبر داد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/IranProxyV2/8265" target="_blank">📅 12:04 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8264">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یکم اختلال داریم رو پروکسیا به زودی حل میشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8264" target="_blank">📅 11:35 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8263">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">💎
تخفیف فوق العاده تا اخر فردا روی تمامی پلن ها اعمال شد
✨
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید، درضمن درنظر داشته باشین که سرور هامون پرسرعت تر شدن و بهنیه تر
😁
❤</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/IranProxyV2/8263" target="_blank">📅 03:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8262">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⚡️
𝗣𝘀𝗶𝗽𝗵𝗼𝗻 𝗣𝗿𝗼𝘅𝘆
Host
:
37.152.190.145
Port
:
1082
Host
:
91.222.197.45
Port
:
8001
Host
:
45.148.250.241
Port
:
8080
Host
:
85.9.104.72
Port
:
4040
Host
:
37.152.190.145
Port
:
8080
Host
:
94.101.186.25
Port
:
8080
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/IranProxyV2/8262" target="_blank">📅 02:13 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8261">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f40e23bb.mp4?token=IqytbcRnZvSOgr0O6Mcs8efM2CbWU10BP9wFO4paszevcLRkPKIQJS37lEHjUlYxA_AykMR5b_bgA4O85GYEP1mcRQB8tYhVzyC9QSUQ82wzQdkdJyakFCKNhBOW0_bdN4zoANyE227j7kSCCCUrp2s3PWoTzzqfCXPkdeOEvaAtZ7CP4rtUYo3PZgltX4SRT_HNWt90eR5d2Ah2srrRnW_upI9251smRC6FXDvK9oEjRQk9fa7mNZs9Oci7gnlBcwahPRG9Mv4JuUijv3G-_P9CZhW0s4C5MF9XkOdu6wfqoeem19go2BezyL3Bhk-DgAJKgf-buxogQ0M-O-lRJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f40e23bb.mp4?token=IqytbcRnZvSOgr0O6Mcs8efM2CbWU10BP9wFO4paszevcLRkPKIQJS37lEHjUlYxA_AykMR5b_bgA4O85GYEP1mcRQB8tYhVzyC9QSUQ82wzQdkdJyakFCKNhBOW0_bdN4zoANyE227j7kSCCCUrp2s3PWoTzzqfCXPkdeOEvaAtZ7CP4rtUYo3PZgltX4SRT_HNWt90eR5d2Ah2srrRnW_upI9251smRC6FXDvK9oEjRQk9fa7mNZs9Oci7gnlBcwahPRG9Mv4JuUijv3G-_P9CZhW0s4C5MF9XkOdu6wfqoeem19go2BezyL3Bhk-DgAJKgf-buxogQ0M-O-lRJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شمارو نمیدونم ولی من دیگ از تک تک اینا خستم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/IranProxyV2/8261" target="_blank">📅 02:03 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8260">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYIRs7rr3Ll1c_doSkIxEV0VJ08kSJYDf5O-j7v7oJ2PnJEz8OwF-uVrRhG3lrDulqzxYL-GJTbXCDAjukYhjFMvZiBtfp-VwvOeHxN2LO9B6ehpcpIhCBbEV5eFbueEEHsWV1Q_V_x_PPPQ_vbsIG9kK1FppCiYyFiBIWp-Y3RPaSlO0vdbgUiFCJRbJSky-JNH9MLkZPiHRWV7qVUEodfU9CCV7jdmAb2HL9F94G3qqu1pNamVOlJ6-Z5Q1QNEC-s0h4vne7snNl-399N_qvazRQFkDHWl5oJrZpvV_3h0aFayl5jTgTrpR81WRJX2DP7F1PoyuJfTqPiZyBT2GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس:
- ایران وارد روز 64ام از قطعی اینترنت شد.
47.500 ری‌اکشن فیک:
🤩
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/IranProxyV2/8260" target="_blank">📅 20:25 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8259">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Injector.ehi</div>
  <div class="tg-doc-extra">14.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8259" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ اینجکتور مناسب ایفون و اندروید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/IranProxyV2/8259" target="_blank">📅 20:20 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8258">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دلم برای هدر دادن وقتم تو اکسپلور تنگ شده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/IranProxyV2/8258" target="_blank">📅 20:09 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8257">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmdXnZszAI_eHwN3l_QW3SdtdAhIx4uZUgazTwn5ZzDX4xhqxZ9Z2v0z8utWTP47-hyWXNqs8clVErelPu5R3JdA7WDKKYcoBqHqLvucn7_3KaOClTdBO8otQ6NRU4hl3AX8lwN8fFZ75lqdt1fEGJFHaDJtoQm4yHm3_YdO2vYQXV7zuHAvR6MUx_7aG52osFkKYuujTGDrLiJKuTKvRet-4_mYYrK2-3FOfhSIIeDvEO0G1FkEjJmtKf0pQbQVtNHFEVa9Tb_5AVXGOlnK0y5yDd4sT25dAeyB-ig8SqVK904uQBhm34lma6od8CLilIJHiViMsJesyIa3Eoo83w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نفر سال ٢٠٢٢ پیش‌بینی کرده که سال ٢٠٢۶ هانتا ویروس مثل کرونا شیوع پیدا می‌کنه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8257" target="_blank">📅 19:50 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8256">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آتش‌بسی که نقض نشده رو میشه نقض کرد ولی آتش‌بسی که خودشو میزنه به نقض نشدن رو نه
🙁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/IranProxyV2/8256" target="_blank">📅 19:37 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8255">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzksPuM58kLxNHzoJ9bnwKk2gNG9DUEpULXSUWhGDY31Xy-lixn0IVFBS7D2-D7fr1_stJDrG9GAeXM9Ww-l0lZ6oV-ZfL196EHFbOSfGq12UoI6igJl8rgucLzMscz3b0k9Gd6-Ld2eK1VIUqsVBRmfMftIqr_ouIM67einaGxiF7L7pnvEUPShXuIHCctX_cCeTn5NVKrHMHrAo4ttP7R4VGP1Fc8ifdgfUCxa7qF9im7RM0Rk779ctab6TbFg-Dvmn8Lj8eIeM9UDYsdce7KIuJiLAT4XSFod-I9Mjhfp2IJxhBBTYfjXn_uvKNvw_6GGna8TJsvvsXg3N-NhQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم تحویل جایزه چالش امروز
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/IranProxyV2/8255" target="_blank">📅 18:39 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8254">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-XzOvl1D6ae1RXqNy5FYNVRGQg-PnPxyJBZt-bpX9UU_p127cjRqCZvJYMDeMRKBGuTJUZdkPEuISYHMAn5rFaXNlogFhSCXmMD6FZVcoGt1dfoBCkZ_XiTUwpQRyXFymJkEd1W_nR6OOFhZqpC7nEnl4hZr8I_EnkVM9EgH-kYTnPrcuIWWZnJfVfA_w6dlbhQGLFj5tJWbeH307ceVr_WHuUKzqDCP_7MOECdeXS8DxHxAh17I7TuO_1H_3U--Ej5g2Jh82dcMSbq58EQkKO1Yc5DfLVvZWm7-6RA4HvWO718tcgR_tQWAeZcS9Cy40ajglVVdiCy7ChsAVYX6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
پستی عجیب در پیامرسان های داخلی در مورد فیلترینگ و قطعی اینترنت
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/IranProxyV2/8254" target="_blank">📅 15:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8253">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9deyzy78FOe6mZbOFRXyZdmuIj05s7rhJaKkB5Kcn5G6-glRio0bdC786uJA1R_X-2YLVuFo1ztGAbWlAmY_8SqmKkT-A29JhaBhODB9SYmljjQJlJg25V5oj1EtdV2fntupXQmZVgxgSGfP2wtIgG3bPMOY3-1IV0l2u4wHVE16ROJbjax8IMB4VuJ3aWTV3VaL1AQlUWMWMtTEtN2PwNeYH4BMnnJRkjrkHdyIjEAiDMlzm3HIpnDbrMyrXQq4so8cnmufg7jlx9XjgV5_KBiq-0TYnzunJIqeo8RxTPJYSrAiXrsTYfKYug1GCPZNGrsIH_BSwskrzl4BcwPTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وزارت دفاع امارات متحده عربی اعلام کرد که پدافند هوایی این کشور در چند ساعت گذشته ۳ پهپاد و ۲ موشک بالستیک ایرانی را رصد کرده است.
این حمله منجر به زخمی شدن حداقل ۳ نفر شده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/IranProxyV2/8253" target="_blank">📅 15:06 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8252">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsqzGYE9Q-R99OOd4M2ejo0guQRhvYzmNUBiP--bsfU6yAbnmoFzWIgJAjUlyIGfFrSpb94M87eX53HU9teWhr06XEE_x2J5S4dyOZXdlYWs_u93Z0EruxcyoU90WheuRjqfhPnfcda9_NsfHCPUY1x6VdZA6jU8VSmUZ4MYw8lXG-cOdvz3T--ozpWus40-N2focu1QSYs_ZQ0NMojmUD0SlAN_lPps8J0m8HybVLf627E0F4WxuVhrg47Y97hwYOJsrv-Ghbq2g43Mnmc9wUCz7Qa4n0H7a61FjtsZlOQwE6wK2SoMJIdNqdVvxj7Ysa47Sfxe_MUvu0raouj1-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطعی اینترنت در ایران  به ۷۰ روز رسید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/IranProxyV2/8252" target="_blank">📅 15:01 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8251">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔸
منابع خبری از شنیده شدن صدای ۳ انفجار در امارات خبر میدهند
به گفته این منابع خبری ۲ موشک بالستیک و ۳ پهپاد به سمت امارات شلیک شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/IranProxyV2/8251" target="_blank">📅 14:53 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8250">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ey-xKKft4sRCei7s9WBBjeJpPChFl6L-_hXWfTHh7hzWg6DL1RasrX2j-wBl0rXZwaevPmHraNKwySfRYrA-hJJzIUzBZHqcJbYLTIcIQRJtqsfNlIuHM9hr-fGj61WXDPFaAlwCviXT98mHt1lVe3Qn1cNRwt8FSBeJHGiW_Krbxg-P5orMeXzNGDBapj2Jii9_8jf0uy16j_wRBf9bgu8rAe-MDUSTyzAbhWXl3M-pNBlRw8wbHOBLYmyLqPRtz1-pLJbtL9yEYpKHDNN16521cfOCsy5J6Ax3C_onG6C_E5xjP5KDavYFYatfmB3pTtnoY-PXmGLApf5cw1IeLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال
لیزرها: بوم بوم… رفت هوا!!!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/IranProxyV2/8250" target="_blank">📅 14:50 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8249">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
فوری - حمله موشکی به امارات
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/IranProxyV2/8249" target="_blank">📅 14:48 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8248">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
امروز روز جهانی خره این روز رو به خر های زندگیتون تبریک بگید
🐴
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/IranProxyV2/8248" target="_blank">📅 13:35 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8247">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">https://t.me/IranProxyV2/8243?comment=7857
🔗
https://t.me/IranProxyV2/8243?comment=8191
🔗
https://t.me/IranProxyV2/8243?comment=8409
🔗</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/IranProxyV2/8247" target="_blank">📅 13:10 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8246">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMIlad</strong></div>
<div class="tg-text">https://t.me/IranProxyV2/8243?comment=7857
🔗
https://t.me/IranProxyV2/8243?comment=8191
🔗
https://t.me/IranProxyV2/8243?comment=8409
🔗</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/IranProxyV2/8246" target="_blank">📅 13:09 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8244">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
اینترنت رو تو سکوت بازم گرون کردن
😐
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/IranProxyV2/8244" target="_blank">📅 12:19 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8243">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🎰
هرکی 3بار 777 بیاره توجه کنید 3 بار برندس این بار ربات ایدی هارو خیلی دیر میفرسته
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/IranProxyV2/8243" target="_blank">📅 11:58 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8242">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اکانت خودم 11:16 استارت کردم ایدیشو نداده نمیخام بی عدالتی بشه دیدین یکی ارسال کرد ایدیشو اصلا نفرستاد تو قرعه کشی شرکت داده نشد</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/IranProxyV2/8242" target="_blank">📅 11:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8241">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یه قرعه کشی دیگ میکنیم این ایدی هارو خیلی دیر میفرسته به درد نمیخوره</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/IranProxyV2/8241" target="_blank">📅 11:45 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
