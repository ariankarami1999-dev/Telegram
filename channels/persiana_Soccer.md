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
<img src="https://cdn4.telesco.pe/file/krTHVLfSwILa3A6ofqvxnbSmOUnlCApvw0E6_4NZE0nfSdNJwJ3MG9iRJhOXgYCGcwT9QMINZNpXe2q30qH9RZk10Qcehla29eejpochP9umZkX6MUk6gkUZVN_CbaUbWrJINHiUv0gh59ZLqm3E1fp2pZrbgV4BkczhGzNSVLBSVv7FRKP2SD5YhdqWHJCTKTIYTzZNe_c_Oem3c8wmKI-eTrTw59riaPa2uLGbBawbv8FUW_AX_G4kWy75otidv4XeDIZQVLdNQhxg-QFi0r4A3SHs9kO79Ex1gZJ1HeLTaORK0z8SP9gjz-I1P4WCFLQete5WEfsWv5-trPKsiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 638K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 21:42:30</div>
<hr>

<div class="tg-post" id="msg-27733">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9ewBlkAGQGdXhJavFK-tThNTGx081jj_1EolGgQPjauHhw4JzEG7ny7ydzzXBBRBqqlOtYVcv0YSSKDUWfyDhlKkBM9ZKEYTag4t0huUAl0i1_O6BSWDlW7pxIf0xss9BM-1b3pTaNZRSv_2YTEvGBVLYs0SLrfU0VW8nYG7S-5wd4w9OSHFPsQ4Zd-RS5gmJ7yFsOsWoKKWCijpXr6M8ndf2yysPjwONp14DI0nyyW4MGPK9j4eVeLx-jPx5ARG19qZtSCy8nJlEf8hirrAvJtLkgRmBKXjW0VcXPfs0Q3PH5hNv7sB6hedMSgW9Lb5cT6nuDxwgQrvXHdoeue_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
طبق شنیده‌های رسانه پرشیانا؛ سید مهدی رحمتی سرمربی گل گهر سیرجان موافقت خود را با فروش امیر جعفری مدافع چپ 24 ساله این باشگاه به‌پرسپولیس اعلام‌کرده‌است. رحمتی در این پست قنبری شاگرد سابق خود در خیبر رو میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/persiana_Soccer/27733" target="_blank">📅 21:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27732">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDhEr_47bFregnQiNqwjjQ2RaxWU5qyg1J6KQwmAiwf722xKVRUF2LdL83BSfqNoTg8DU_vsEDvjLck2siaVnXqKHKs37mJnVJSdVwOrnHhNIzuTYsCS4XgkXRIb8RP4ZU2HeSx48M_XPn-onyA89fiP89GIv37dbjYYg8kHy1ZB_4xzEa4q8GvHt927mrOapiOcfryZQb8DgRn6mY-5seGhZiv2rDT4bw4i4dEwNlBdPMznkZ-Na8tFjYgxC-xgKBkS9laOyr2xURxtwI5rLU5UxjJNBKbSeTbZSisvhl-OKeW8nVuGasQOPjsL1q8rgoPeo4jAqVJWBJZmnICDVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌برتر؛ استارت آبی‌ها در فصل جدید با برد قاطع مقابل مسی‌ها با دبل سعید سحرخیزان؛ فرعباسی با کلین شیت فصل جدید رو شروع کرد.
🔵
استقلال
4️⃣
-
0️⃣
مس شهر بابک
🟠
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/27732" target="_blank">📅 21:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27731">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rs2khp6gGp5QmqDbABQ7Fc_DlhpMBIXs9wwgQDHttQLeURFlA0ZlA9BS5cA3W1EMzu12eo67b-suDkiM7MvIi6optLde4eEQeMrHiV_7OBjoqOUqFFUwIzWLPLuf0tBbIPLqrdz4ixeGAAWIY3CJZCtEoWO78ezJRyKLJd2AIt8LhGeMNvrQ_QkvC30if2OP-AytXzpkeh7R4J7S4z75g9Hb0Y7ePVysy2XjPvhgybWkJSlA5DoI89BSfc7SEx2uIi0kr6eizVBlAdKM1awlt4BohnWGQ4DPwLRQMtjHRn-xG-uGtMbkcuk4ahVR88V2hrOAlRr-niGgvwHCEROQvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دبل‌مهاجم آماده آبی‌ها؛ گل دوم استقلال به مس شهر بابک باز هم توسط سعید سحر خیزان دقیقه 56
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/persiana_Soccer/27731" target="_blank">📅 21:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27730">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d884286cc.mp4?token=iTTOZqogKQkIYsAV7D9cIkkDXG0JBEPDYD03kodhn5ucr9BEyXNBmzkw9arnZuJZ9s5n8u20SAielC2HkZpovSvQc3X0dELtdQGnGylqUgJ4DwDSOP_pLKByyShUA62yt2PXVud_3hpWDuWMPdQ1-d8lqi1pKFnRmzpa_7tIGylF4nHvtUzcn41bN5YqVBp44hg26w9-fQBduPs6-KFFLUkpsgeOQ3IjS6Q_XwUBTpwEsm3CMQ-_zyQUS08DHPa7IlTHSQcudLFbgiPg6dWqf2zLtKv_B8TaOFE7hlMmH4dvYCwWxOx24qMqwhvaiP-TZzBITP6k4kvPvEJqmAFfSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d884286cc.mp4?token=iTTOZqogKQkIYsAV7D9cIkkDXG0JBEPDYD03kodhn5ucr9BEyXNBmzkw9arnZuJZ9s5n8u20SAielC2HkZpovSvQc3X0dELtdQGnGylqUgJ4DwDSOP_pLKByyShUA62yt2PXVud_3hpWDuWMPdQ1-d8lqi1pKFnRmzpa_7tIGylF4nHvtUzcn41bN5YqVBp44hg26w9-fQBduPs6-KFFLUkpsgeOQ3IjS6Q_XwUBTpwEsm3CMQ-_zyQUS08DHPa7IlTHSQcudLFbgiPg6dWqf2zLtKv_B8TaOFE7hlMmH4dvYCwWxOx24qMqwhvaiP-TZzBITP6k4kvPvEJqmAFfSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
تازه‌واردهاگلباران‌شدند؛ گل سوم استقلال به مس شهربابک توسط محمدحسین اسلامی دقیقه 88
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/27730" target="_blank">📅 21:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27729">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3f9408f8.mp4?token=B9gVy9CfCX67RW6ixOpS5wbbDkbr6ZbPFH8w2mGL8JGRmUNNlCDD2bE04JE7hGH0GByK_57L4vwqeTojR9JCsSIu8zrWtPNYNo75vJA1P3xTR7Vs4D4HKf_WCj1Blt3MClGGZtlKBVIGCG5r4DxVLyn06rJDv2TP76MBq7K8wqmxi-1peYJyrTT8eGhYn0UWxT85NutK6LWnOgxsnk7B1I0i88TPNHIV5zqNuMuwk3fxu6IsovWtM1UpqPvU03koT21p6R7AhuobSSFlhVDYWsbsupFdOQmdLH_Y5we207j-NbW4fICVWyrhA9aqfwTQcGnzNTskO6mWCbyq-nL8fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3f9408f8.mp4?token=B9gVy9CfCX67RW6ixOpS5wbbDkbr6ZbPFH8w2mGL8JGRmUNNlCDD2bE04JE7hGH0GByK_57L4vwqeTojR9JCsSIu8zrWtPNYNo75vJA1P3xTR7Vs4D4HKf_WCj1Blt3MClGGZtlKBVIGCG5r4DxVLyn06rJDv2TP76MBq7K8wqmxi-1peYJyrTT8eGhYn0UWxT85NutK6LWnOgxsnk7B1I0i88TPNHIV5zqNuMuwk3fxu6IsovWtM1UpqPvU03koT21p6R7AhuobSSFlhVDYWsbsupFdOQmdLH_Y5we207j-NbW4fICVWyrhA9aqfwTQcGnzNTskO6mWCbyq-nL8fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
دبل‌مهاجم آماده آبی‌ها؛ گل دوم استقلال به مس شهر بابک باز هم توسط سعید سحر خیزان دقیقه 56
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/persiana_Soccer/27729" target="_blank">📅 21:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27728">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a75e1bc211.mp4?token=RkxtptfYdYU0YVCjNmy2H6SvZc6AyBYMMBmET4eoWN37fZ6IrYhGKHnQ-FYpFN_yJiJmjCZpzY9p4CKqqCL1kGtsohAI1xcmUi0xP6wXGGzq2ltF1MeWfmnon6xIKRSskwV6LWKSI9yHAdbhCjHBFvwszGYR-riNWzPoJytbRcps8Hcjf25Jdeh3neKLgsg4d1-X81tahJzJVgN6U6sZ9pi5oiN7etM9kUF4GZ-BG9b7i6bdsxykDHWsED-q1c9sKoZMoetpxecu-anX2X6JgQjkeU2cYrvPV8rHPLaKbgQr4ZDjO3_M0lldanvSWPFwtXNBn-99kY5nfKhdyPS14w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a75e1bc211.mp4?token=RkxtptfYdYU0YVCjNmy2H6SvZc6AyBYMMBmET4eoWN37fZ6IrYhGKHnQ-FYpFN_yJiJmjCZpzY9p4CKqqCL1kGtsohAI1xcmUi0xP6wXGGzq2ltF1MeWfmnon6xIKRSskwV6LWKSI9yHAdbhCjHBFvwszGYR-riNWzPoJytbRcps8Hcjf25Jdeh3neKLgsg4d1-X81tahJzJVgN6U6sZ9pi5oiN7etM9kUF4GZ-BG9b7i6bdsxykDHWsED-q1c9sKoZMoetpxecu-anX2X6JgQjkeU2cYrvPV8rHPLaKbgQr4ZDjO3_M0lldanvSWPFwtXNBn-99kY5nfKhdyPS14w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
رونمایی رسمی باشگاه پرسپولیس از کیت جدید سرخپوشان برای فصل جدید رقابت‌های لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/27728" target="_blank">📅 20:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27727">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a0da2836.mp4?token=HVDGPJ9xFeTYz4EYN6Snj8AA2QLhdDh1wWful3ytZeRsUKWQ1Lo3RryYLMtxRdu7YuomkQg0FTDJR7_AgwsIcCp8G6_5GX2DHZ5YP7pxJKYmWZKsEMqSE33CFcPucfj5NVslAqIftEBjMbFOhGtRiF4m5Xv8cRvdSm3niCiK2IuFEa5O5wnTi9UwNJdkY271-2HwIslyW2qxDtZXW2KmzdJ0heTjyahYew-bGo99kfKWllz_bEADL30hFwyygku7ZoFdyuNt1LphHyuB5Zm4o69EI6ZFuCpjRHpTgJpc4CdlOa1EB8STtdRPgts1MAo0uCbesNoXtImpI9fts2wGFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a0da2836.mp4?token=HVDGPJ9xFeTYz4EYN6Snj8AA2QLhdDh1wWful3ytZeRsUKWQ1Lo3RryYLMtxRdu7YuomkQg0FTDJR7_AgwsIcCp8G6_5GX2DHZ5YP7pxJKYmWZKsEMqSE33CFcPucfj5NVslAqIftEBjMbFOhGtRiF4m5Xv8cRvdSm3niCiK2IuFEa5O5wnTi9UwNJdkY271-2HwIslyW2qxDtZXW2KmzdJ0heTjyahYew-bGo99kfKWllz_bEADL30hFwyygku7ZoFdyuNt1LphHyuB5Zm4o69EI6ZFuCpjRHpTgJpc4CdlOa1EB8STtdRPgts1MAo0uCbesNoXtImpI9fts2wGFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گل‌اول‌استقلال به مس‌شهربابک توسط سعید سحر خیزان در دقیقه 45 روی سوتی گلر مسی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/27727" target="_blank">📅 20:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27726">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWpLb5DNLoncxxuJcCLh8u0YBzO081O7-R7y1gHPoYk-870JBc4WMFJMKC8Nuun0lu72zmnlK4l2JjXPk_5m9zVvdZFtFPgVgcWRl7Tfx_Vcc7voM1BW2n8QmzJ3n8ObO-jJ65hktYXILT3iROOcA70giwQaOxiigLcKAEs5Aw2T6I2AtHSRIGf_DlCA9bYoqRQoOcsGjNUmYPNL6QWtRJOA5m_7dNslrzZ_dhGL2bg8vn1QeJOQ5AzTebk0DyK01qVy2bhQLLPgmVwul8oH85MEvm5ABSCi9K7w1koYtxXr5VTLZ1Y8naQMgAAQdO-bkHzX-4iMfwQb3AzP5rff4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/27726" target="_blank">📅 20:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27725">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e32a2d766b.mp4?token=JuA7SlVw2utYFtb4vow0TL9NyQH1GnhPcUEvNHsXkat4ueuFyk8xYfgVtUO59wusGwshz8fPq4kF3hnTbMgoqtodx4A7nR72zkU16mFB1y9HcrsjbltRdikK2j7NshPAVf1ARu9X0WFtHKZHQ0lOPVOWryY1U4fVEjReM1A5ILTCEqrkhY-HW0D9i0RBiYqmgZKZ_OI5fgC94pSftUkb7hSTNbn5hgS7P_dY7zoHmpIW_4H8Wh2OiLCd1_a0xJ9laH4cYbQ9zowYwX0EhCw9b-DC0S2IOH_7zGL33dzN5nnlL416bJaMm4rtgVNKLhrqSb3NWyGYLvfu5mMfRLb0Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e32a2d766b.mp4?token=JuA7SlVw2utYFtb4vow0TL9NyQH1GnhPcUEvNHsXkat4ueuFyk8xYfgVtUO59wusGwshz8fPq4kF3hnTbMgoqtodx4A7nR72zkU16mFB1y9HcrsjbltRdikK2j7NshPAVf1ARu9X0WFtHKZHQ0lOPVOWryY1U4fVEjReM1A5ILTCEqrkhY-HW0D9i0RBiYqmgZKZ_OI5fgC94pSftUkb7hSTNbn5hgS7P_dY7zoHmpIW_4H8Wh2OiLCd1_a0xJ9laH4cYbQ9zowYwX0EhCw9b-DC0S2IOH_7zGL33dzN5nnlL416bJaMm4rtgVNKLhrqSb3NWyGYLvfu5mMfRLb0Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گل‌اول‌استقلال به مس‌شهربابک توسط سعید سحر خیزان در دقیقه 45 روی سوتی گلر مسی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/27725" target="_blank">📅 20:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27724">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32b2ae1951.mp4?token=IgiULwX2jlZYIIEAwyQkOr3zGrYssQZ4H0r_0DtZMeiBnrWi8pSIAeIK5b4Q2aHtKGNh9wpnzEaJ-qhN7SUiBrdGeQLOCOa5V5YdiwhwKFyMz-8N2y6hp1JtpPz-lw5CFlK0U86hSqA8ea-L0juxl9nDJtoSfz6AJQOIe-l-X3TnTWyRVRGjs5Oal64D6-gpYx_MLAnyXMQeYwJVcQiYOGnw3qDZcgpthBkOyZG7L5NmyERMH93l4My2W2KnDXpqLCNu05M1hpBnLvRjKVVz1uqviT0XJIGafnMvTdT-T30g364As8Kw9dtcKQa9IEDjc8UgItrFs3hcnBjIuxS-oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32b2ae1951.mp4?token=IgiULwX2jlZYIIEAwyQkOr3zGrYssQZ4H0r_0DtZMeiBnrWi8pSIAeIK5b4Q2aHtKGNh9wpnzEaJ-qhN7SUiBrdGeQLOCOa5V5YdiwhwKFyMz-8N2y6hp1JtpPz-lw5CFlK0U86hSqA8ea-L0juxl9nDJtoSfz6AJQOIe-l-X3TnTWyRVRGjs5Oal64D6-gpYx_MLAnyXMQeYwJVcQiYOGnw3qDZcgpthBkOyZG7L5NmyERMH93l4My2W2KnDXpqLCNu05M1hpBnLvRjKVVz1uqviT0XJIGafnMvTdT-T30g364As8Kw9dtcKQa9IEDjc8UgItrFs3hcnBjIuxS-oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شماتیک ترکیب استقلال برای دیدار امشب مقابل مس شهر بانک در هفته اول رقابت‌های لیگ برتر.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/27724" target="_blank">📅 20:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27723">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEE-qxsOgKWOcJzfxYNoXbaTGTwMYwlXvBcnWKBXOAMlM4NegN9rTGrFthoLEPOE3qkNqcy2WTjxChCvnGo48h0x2BiPhYddpHdYE9O633cvHUdqWmcnTp6Z5SYzuGQqjROOwQoo5FP0ib34-s-Lh85eCbYrXXmt73Fp7--EuDYKFyPx-rsFcpBtj0v3XNG_3-9mcthPMdD1MLEBI6Bsmz4CmXmBeZHrxepvQfQxfq2nGpiHjVjxBwzPdRzIusuinFFtSvqhowlTa9XyfG-Z3Wnm-QiCcwKhk6yWJtFhFKM3dhWhDs5z79VzTnI2I_-d4rvP6qlWhK8qmAieqRopUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دبل‌ستاره‌بلندقامت‌پرشورها؛گل دوم تراکتور به پیکان توسط شهریار مغانلو در دقیقه 45+1
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/27723" target="_blank">📅 20:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27722">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TupqVRfSCGQ_ecvtE31yyPS1qxu1bR_x3JWkFEhqHwjXFuItjer4CkrY_IBNvfXFqVki-3bLdp9Xg3qmIdBSHwOljh_HWzTbdJPD-8iASX8Ck8lZoL5PCP5JfMb9nlQXTiEy_QS9Yb0gHDy7OsZlDG8mxqLvNkv3wlusl9FZduXMpuaS67d-UZW0tkCvdETn7xJah4u9iuhncMjtwvm7_moqHPDuWeELpt4mGoOh3axZ_0n09LK4FGWMHq5iCbKd7l4ySzRBASL4B--oOe8kJhfHuTjkZcKGNN9Z6Ra_45PRq2sp2E7id4d9oyUX46ANzFu-Vg5cuavRs58X__w66g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ علاوه بر جذب دانیال ایری و جذب احتمالی محمد قربانی؛ باشگاه پرسپولیس یک بازیکن دیگر نیز جذب خواهد کرد و پرونده نقل و انتقالات تابستانی سرخ‌ها در این فصل بسته خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/27722" target="_blank">📅 19:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27721">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8QoJaeP0qO8oe52OlP59D91nUwPpPpA555bWeKzEGiAXV1gDfjp5-7UglMpsTE2lJTV3Em35CWVqhkv-sRszA57cMrEjxWKxHUPrpZRLfNw_8yF--4BrZbZfn_oZeD5DZhux8SlTtkX64sK0_ETdMRojV10TUOVN6HdDsyKnp8qqJqV7VvT4UrJYpy1XEKl6M9IKYOvz5jf5_rGqtaz4Tzq_v4QQxaKEkul51TBgPEfEYlRpaflcqDRVKbOEXXKh8tozGViKhsk9arvnO-lnTCOMJJKtAscLU25njfGxQJ4QzE1mhn5S3jZ9J9J3gNJCIkV5swb0A4TJQkPuBoboQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
همسر رضا جعفری مهاجم جدید سپاهان که آماده دیدار امشب طلایی پوشان مقابل چادرملو هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/27721" target="_blank">📅 19:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27720">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIYQX-KgAO2QNKHn1zKJ2-Z8uYpNcdDn3KGWXTNuh8l6UAHokTTQLz-UQxkrtO6eUexJcrXYRy7ItC9VoyuHDcIWhd5NPZCaVcO0iE9ghmlgCDViHNpbvw_UYzquZcXqKG1iJruqyzy388EdAGnk-e1LiMhcxR94mTPQnHZKGE6aD7L5pQhFQPHIROgK-mpQmMSvx2KLy4RTUcLaVF0vFh6DMcDjJykbpbmsvy-BPnMYWJSf2BSN5Az-_PVO6jOhiaEO_6GsrMQIfg8--br27o_Tc-FrgOkRj3awnhmmsVQOR7wXFAtEmz591EXYDjKCS53s5WnFngtC-f-if_fuSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریستیانو رونالدو قبل‌ازامضای عقدنامه؛ با جورجینا تفاهم‌نامه‌ای را امضا و حد مالکیت همسرش را مشخص کرد که چه چیزهایی به او تعلق میگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/27720" target="_blank">📅 19:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27719">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUUoZTyzj9yvMHpI5NxXVpN6wf9eavJfpxA55eilkwyII1P3QyU93dO07Au8usEXaVTJEQ4QvNPDoGXXyI-piJyLj04DdsHMGWEwVuUkFNhbA0utO-Yjxh97KcYfTnu3VP85mwlIFeRpzIkgg0lqNKhRARH9hVf88OCqNgWeRVf5B79yD-t_W3Mhjp8h31PrC-ccTePR4vcM1dAcZXelG5_v5cnxVNY2JCZtDMgWNqR-PjtYOmMC0nScNp4c_rBO0dOpwFrCzi4vUTaduPB4o_8SkNjrTlZ-oHSZjCNkxqaF6wJsmGp4t_f1-OgV3NDhUUeK0nXGJDnHMyyjrLkhSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
امار فوق العاده ی کانال ، کافیه هر روز با یک میلیون شروع کنی و اخر شب +15 میلیون بشی
💵
اگه‌نمیدونی‌تو این روزها چطور بازی‌های فوتبال جام جهانی و والییال و تنیس رو پیش‌بینی کنی با مستر تیپستر همراه شو
😍
‼️
میتونی راحت حداقل 10 تا 50 میلیون تومان در روز سود کنی
💎
کسب درامد انلاین ینی زندگی راحت پس این کانال از دست نده
✅
لینک ورود به کانال :
👇
sg23
https://t.me/+q-sIylsuFEtlNGI0</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/27719" target="_blank">📅 19:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27717">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osQPpvrGDY0pSuRECRqlQJSqWsyw9KLMBRN9OEIYd2UALzdbVUeC5OKl0_8I62gPJ3PQwl4SAjEs-rBHX_83eeLFyrPT1yQP2Ro7gyYv44NBNnFW3nyg9qMpMdfMsrc8bbPzZxWEbVCyZdCxtBQLMRDthMSAHO1-uQ8fhCtHopo2Qtvd5VOtjuJl23Qgj9sIniwp1-YD8A7QYjSEfo0Zth05r6YwuYzbLSsKACb1tpInbKX7E72_hLU-BgUG1_Gsh1MdbMozkr3tDyNidn60Z8QiCLDQDkdA3eaDz7r5-uZhEEl1YZwqdpfKramUWvGHw17oLGu1totWu0s5HgzaDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو بمناسبت ازدواج رسمی‌اش با جورجینا یک قصر در عربستان به ارزش 22 میلیون یورو ناقابل به او هدیه داد و به نام خانومش زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/27717" target="_blank">📅 19:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27716">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/342fbf13e8.mp4?token=aqkmvJaCdBp4SkS5e_ic1Sa-ly8_YrcWg7tP93vtxseUhSOibPeeRr5ljiU1toN8w5bLSRsm62SPZhex8Un9eC7WrmIBKlxXg4ZVVxadAcff6w_TOh6tqCW_agd7Kf0119rKmviaToxG_rgeGZz9bFnZUJDdUBqtFgV0HNfdnGcCwIqC6V7CyRr3he5y1AF17S45KUDOuV2MFeV7n7Sb6hkusBGPKjYfIhmk6S9kSWqSjGN34tOqfYWATLBRqR1HRJ1VX7pXjnd9vbDPaBwKjNogaZAUdvX8eHoDbUMj7XGoZKKHzD-NeOZ2iKRSTr_fJTfLo652Qs0-0ks4kno0KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/342fbf13e8.mp4?token=aqkmvJaCdBp4SkS5e_ic1Sa-ly8_YrcWg7tP93vtxseUhSOibPeeRr5ljiU1toN8w5bLSRsm62SPZhex8Un9eC7WrmIBKlxXg4ZVVxadAcff6w_TOh6tqCW_agd7Kf0119rKmviaToxG_rgeGZz9bFnZUJDdUBqtFgV0HNfdnGcCwIqC6V7CyRr3he5y1AF17S45KUDOuV2MFeV7n7Sb6hkusBGPKjYfIhmk6S9kSWqSjGN34tOqfYWATLBRqR1HRJ1VX7pXjnd9vbDPaBwKjNogaZAUdvX8eHoDbUMj7XGoZKKHzD-NeOZ2iKRSTr_fJTfLo652Qs0-0ks4kno0KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
شهریار نیومده‌گلزنی کرد؛ گل اول تراکتور به پیکان روی چرخش دیدنی شهریار مغانلو در دقیقه 36
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/27716" target="_blank">📅 19:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27715">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c3a29973.mp4?token=f9sSgWyu-ls_5TQ7Jl3ZHOvSdwZq1xBKA_3qEnAUQTddIdd-QD5eOFOrRumEVWm7wgnHB7ahb3l08wEND5GUi9q0wazZ9WiqWnchZAr2e7tc7wN7OThAB4J_XvhAhm-0oBYproGDWRAd677J5mIjfrj12f9VYEgJkq7JA8fYItGkmDBzXXAORsXtj9BreGrNHhzgvU3JhocRCYAI0gE3k_-mkLiiOrd3LBJFu3UiXrSLGzl84s0dQP_V74St_OBhK9V3LmyeM5is1JqiBDmfeAYF3UxvkLVujuxxWMOFZZRA3VJKnkUCXxiMdpS5mOQBw5852ljTagtbfRqjfTyVyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c3a29973.mp4?token=f9sSgWyu-ls_5TQ7Jl3ZHOvSdwZq1xBKA_3qEnAUQTddIdd-QD5eOFOrRumEVWm7wgnHB7ahb3l08wEND5GUi9q0wazZ9WiqWnchZAr2e7tc7wN7OThAB4J_XvhAhm-0oBYproGDWRAd677J5mIjfrj12f9VYEgJkq7JA8fYItGkmDBzXXAORsXtj9BreGrNHhzgvU3JhocRCYAI0gE3k_-mkLiiOrd3LBJFu3UiXrSLGzl84s0dQP_V74St_OBhK9V3LmyeM5is1JqiBDmfeAYF3UxvkLVujuxxWMOFZZRA3VJKnkUCXxiMdpS5mOQBw5852ljTagtbfRqjfTyVyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ ترکیب تراکتور برای دیدار امروز مقابل پیکان؛ ساعت 18:00 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/27715" target="_blank">📅 18:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27714">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILRZ32amTt_rPPrXspH8Sv6RQub176K-tdCHq-z7Z2wpmJgfwxUam-yf5p-A8Z8-fLggh80s1dB9T9WJwDrO6r7xBJkevWAjwC8F1H7qR6HXzUtkn-wxX2lla34dM_q5ejRzzMmsBOn0IQcdso-6ahWcb8pDMvIqBAfqxfHn8fn724or0OVgtnQsXK3W7mC85Fz9uyXfUk5L973DMsLWKmpz5ygL7Spd2b3z2Y0GOzw0tQO0ycYDvkRA1_h3ra7H4ufjUIlim2SnRy73RIeYU6orYXY-SlrgIa81bkhVXqLt_BYkYZJ2952-xsQ49S6v9793o_msMTfC-7DcGVS_5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ ترکیب دو تیم استقلال
🆚
مس شهر بابک؛ ساعت 19:30 از شبکه سه سیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/27714" target="_blank">📅 18:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27713">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWk9OEjjpbvieowWLwXezTpgzMZEqTpChYABHkIqEwzJwuNBpfsrnlsRNEM-wXoRVxBhftaXkuwnp_SSHZx17BRhRQcUc02ely9-DAEUpz-W-1aFkKZPW--hAu_96A2YY8I_B-PV3GNoOedevy_uBjC7ACOiRUv4Vt602ejx0I3g431pILZXRjNh-7_1WK3b6wvxwMoTLY_J3pRypRfseOgYloQA7EQLPNbERstU5JBQ1_thzWqVzF6k8_tDdm_a3dgLcN-w_QiJRBmLye_4MNGpQRtoQQtxZJNjTyRqcR20Mnt3XMJv_ot3-l2b2wBzm1CsAD7WT6UBryawUOcbTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
شماتیک ترکیب احتمالی استقلال برای دیدار امروز مقابل تیم تازه لیگ برتری شده مس شهر بابک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/27713" target="_blank">📅 18:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27712">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3436fa84.mp4?token=Ogf_DKdivomqC8hwCq6R-w8dg8H5B98_CqJxrLzADcsoK0d7lhcLa6HNILOv7VvYokc22Jj9FLKlLDXQKLJcVQGAznDtY6HjCAW3AYAKShseoNFHVS-XJvxgRgR4Cwlu3zNpDN0EAsGaR_NnDYd7Q2LdtOkZHrry7QZXDWNFM3kx4dc-cXPNHjGmwMN2tXx66gOJErLozmY-YHz39XvBadzM6tCgHh8I2MGNP7Igz7pN3wfZ62sT-sVSzi3vORUOI3wr5OLs7_Ru3RK524QLMDuk1iOHChW9z9JIb2g7gGVWMJ-ILhdDnbZM5i6NPRcz_ie7HT8bKH5dzpF8B9NP3LYWpAnX13JPeZlrZep26nSwMBnwbsv0-xY-c9wqEdQfkCo67wycqXsaSbH8yKNelQWCNTjBLxSE5ddEd7nL1lOivV5N2ocEeTR_2NfHAMyms6hrFNi_yBoWinFgTFckrQjZZ4eEzJHJ-yyGzZfFwkwmmGjpa_BbkAKTbUAcDyZGGqHOM24HM_fz-3AyqTuUxXHnJOZ5RVdkRlB4ZLLzZa90f7K9vMIsiqogv4vWFzFOueKuL2USn20goCrPK4SkvH9oUvOcDvf7ZZ6fm3n1_rHPlbDmXjLoYDvvDVdESc1qOv7JlOIrBFkqSUTMNeLckDamwTjm1qobFF7bMhGZhk8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3436fa84.mp4?token=Ogf_DKdivomqC8hwCq6R-w8dg8H5B98_CqJxrLzADcsoK0d7lhcLa6HNILOv7VvYokc22Jj9FLKlLDXQKLJcVQGAznDtY6HjCAW3AYAKShseoNFHVS-XJvxgRgR4Cwlu3zNpDN0EAsGaR_NnDYd7Q2LdtOkZHrry7QZXDWNFM3kx4dc-cXPNHjGmwMN2tXx66gOJErLozmY-YHz39XvBadzM6tCgHh8I2MGNP7Igz7pN3wfZ62sT-sVSzi3vORUOI3wr5OLs7_Ru3RK524QLMDuk1iOHChW9z9JIb2g7gGVWMJ-ILhdDnbZM5i6NPRcz_ie7HT8bKH5dzpF8B9NP3LYWpAnX13JPeZlrZep26nSwMBnwbsv0-xY-c9wqEdQfkCo67wycqXsaSbH8yKNelQWCNTjBLxSE5ddEd7nL1lOivV5N2ocEeTR_2NfHAMyms6hrFNi_yBoWinFgTFckrQjZZ4eEzJHJ-yyGzZfFwkwmmGjpa_BbkAKTbUAcDyZGGqHOM24HM_fz-3AyqTuUxXHnJOZ5RVdkRlB4ZLLzZa90f7K9vMIsiqogv4vWFzFOueKuL2USn20goCrPK4SkvH9oUvOcDvf7ZZ6fm3n1_rHPlbDmXjLoYDvvDVdESc1qOv7JlOIrBFkqSUTMNeLckDamwTjm1qobFF7bMhGZhk8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ درشرایطی که ماده شش فیفا به برخی بازیکنان اجازه‌میدهد خارج‌از دوره نقل‌وانتقالات ثبت شوند بندچهارم ماده ۱۷ به صراحت می‌گوید باشگاهی که با محرومیت دو پنجره‌ای روبه‌ رو شده، نمی‌ تواند برای ثبت زودتربازیکنان‌از همین استثناها استفاده کند وبه همین دلیل‌باشگاه…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/27712" target="_blank">📅 18:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27711">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cR0sje3m65gMjkS_GHSWGuLWhBxM-9gItSJFAPFSun1DKKT1ZuPkW0oNyztBgkSn52Qa7r1rkBKRwhcyPammqIpRjiXgZot4b301t_hH1YqTIEAs2A13-QsDKGIEQ7bsG9msvBBjQWavMMHnpO9U-H31ZRWoNG07OW3SVnsNeQShkOKfeHIaEOCLclL3Xnot0IOPX81_EbSgU4Gw02_LXhugI_-VJuQiPFOca8LFf67mbyIAMgeNxnfseBZZ7__O6pc2aov7q9TEmvkuaP6-YM3XRDIZdQKG2h8rIRqGinrwqyyo9J9hdc54WWZiFnrHSsUZ1YPJZtMlGKy_EBKnaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
مهدی ترابی ستاره‌تراکتور از ناحیه کشاله ران مصدوم شد و به‌احتمال‌فراوان همچون مهران احمدی یک ماه دور از میادین خواهد بود و دیدار هفته سوم باپرسپولیس در یادگار تبریز رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/27711" target="_blank">📅 18:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27710">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDGRwbLvii5RbhhN_f0SAp8hQs7IxSSf-0_s5_aobkM8FGPIikbCJ0_UV21ck0ILiyENxluzbsx4kveCG6XEDm4Qka4uGA01BlVFVMgN_0HloXjYJbp41goGE2xj6YUx3-N2A8YZpdE7sF_ddTGHosl1-ZyYWTqYCYCW1uVP99oJcgh6FyqkvBmZMHPmMoyJc8MiXpuc_iknqdSb1jBRXixVSJL1Rgj2lkj5Z4F5Kcndaij5IOTUKmWqneFvG5wDRngyOsz4mqJP2pSltE8rI2P0UAdP2BiohPdYUEJNIOOdNo546tCcCDmsiAaFgQ88DhGlgIACJH_zRD7FU00EsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
استقبال‌ویژه‌بازیکنان وکادرفنی‌تیم النصر از کریس رونالدو بعد از ازدواج رسمی‌اش با جورجینا؛ وایب صورت CR7 خیلی خوبه. حلقه دستش رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/27710" target="_blank">📅 17:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27709">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iza0cJWDzS8xk2_R_Zm01QK8AwcOLNX2NTtn30JR3hqSQ8YNWDlg_sYSESOExQ1ytREkQnSw4hL8_RSSj9HlsTdYz89D44Ch825Wmng7xWF0Mji-Hq7khhm5Y7329-44KHOZK7FE5XSv4uKWxDtoK0HeleFmRn3M2ZgPGbwWe3tfxadwWl6N2ZMFM-ZiHTZ668izm5tG5gDwS_g3n3n4PWWpqq_ISYYIfcoFRApLwM9UP8pmsiIAO-4MKqvYQ3U4FLgTYOYsbvk7-Q1lVAYLgpI1rBQBDBrJG02qMJ93wWoMBRhHUSsOQbLAge1nDSoU0AVCGjXQiap_8GN1rx1Qvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
الگو برداری باشگاه تراکتور از دو باشگاه بایرن مونیخ و منچسترسیتی در طراح کیت جدید این تیم برای فصل جدید لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/27709" target="_blank">📅 17:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27708">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6acf648940.mp4?token=n6ZoAOistRsgVJTeOKPcnEdN6iIA7mW_Ih6SPdQjzVqYerEB0hj5zNNPhUr-ARR3jOBJvkFEvc8NFscpE9Rsi3MSe-Eiu5A6dY-o0zXIqFBshl-nFASKnQnQnc44pfSdLaEGmXSWvRVOkaUn8SWZG_dyF4E541bORjRdxtIPR26LrK4TUNbKw_2UKVK23o-UxsncDsE9-aRztqR0gMvcHuy903MPMNFP2LlBab1gpv3FOIXFDk_kftWVv0GBfK87mBhmWnlkrfDndhu1-Pu75KQUkTSMQd3YJ_LEyFnwVo3nkb6Plz3a4NRLd5vBQ2zav9wGcjaWAFzpvuj6Ny-RuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6acf648940.mp4?token=n6ZoAOistRsgVJTeOKPcnEdN6iIA7mW_Ih6SPdQjzVqYerEB0hj5zNNPhUr-ARR3jOBJvkFEvc8NFscpE9Rsi3MSe-Eiu5A6dY-o0zXIqFBshl-nFASKnQnQnc44pfSdLaEGmXSWvRVOkaUn8SWZG_dyF4E541bORjRdxtIPR26LrK4TUNbKw_2UKVK23o-UxsncDsE9-aRztqR0gMvcHuy903MPMNFP2LlBab1gpv3FOIXFDk_kftWVv0GBfK87mBhmWnlkrfDndhu1-Pu75KQUkTSMQd3YJ_LEyFnwVo3nkb6Plz3a4NRLd5vBQ2zav9wGcjaWAFzpvuj6Ny-RuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌امروز؛شروع لیگ بیست و ششم با مسابقات استقلال، تراکتور و سپاهان مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/27708" target="_blank">📅 17:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27706">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GYAeEoAZ1oy9GeptIt1VIC1u1kCYTgb4rYn5DNXwqrn5nA4qShcke5HZCrUBKTwC4bOCQF1Rcc9RunB7ld5Ybxs4CQAAAAqCGa17RY_3R-3qHcCE0hJS2WFwITD-4QgTZFhXUAXlobqo_wuSKulfRm1Jtw7uhy_SWTJWnbQlJN4LxupUrHGRXgZ_unwqaevt2ZWl_8D9PSzPQrVVy5QB3pvbA-pMT15A61cvXpTFSTzGZ8w5rveg5bKZG-3hxbCDRRt6UstZ7tgiDf6kjsEprzzGcIDSKGUkXLDP6cfK0w-rq3qxTbymmguVtG5pPnmN0OPMyiC6ciOSUU0CvBphEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3g1pvgLjCLi8T0gJhaun1StvGY-IfGBkdQVfkOWFTWOJLv5gYs3YJ3S7azBWqmtoQmMv0bEaWCM81RdvVnWatnYNohvJuutxAx2j4ERroRWtORJmAPN3zYfKNQJRUhF1Z2ouANxFC2WnSRUK46Iq94BLYU8kw_nwiaJKyJqnTK9O4NNCsAhjZq6wiMWB9nyyJSLa2WvMCeB2wsBNFo2TUHVuXfnTJICEHVzZgvhvGTgtK2MB5FxfJML03Ox2oLJhWVnk67eWS_uS5j0a3AodPtXwgPVzziKsro_gQTJgmx_k39r866ZXbFvhxglBmlzqFoWJ2NYEqK5rkfQZlwzUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
الگو برداری باشگاه تراکتور از دو باشگاه بایرن مونیخ و منچسترسیتی در طراح کیت جدید این تیم برای فصل جدید لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/27706" target="_blank">📅 16:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27705">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erDxQ5mpLUfynsK6AxUJoqRD7jjYi2lGx41do4DrUJZRWmz7AT0b_ntubWLvmv759rCniLerYfBvRpsgwazZKqzaqNZ_YFzIYA_Rf9mF_cJIYFpZgTNJMAxodMXsNmwqGdwRESzE0OIa8ezdbLt-gaxvZ7bVp8bCGhfAeYHSkUTL8QdEdgJrIYbTuIYmH5VGyx6ucHEwpkPzTb2itLzU1NkxC2UOflnvUkEm3oTTocCJmKFas8Xbe4rRxiXSk62pzUQDwuJYbWVzHanlRL_AWwIIOvKY4fsznDpTKMFWxgvZI77B2ge38-Z3Gy3FFQIakyu9vSu8kxVhNRj9SXfrQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل کارتال ظرف یک سال اخیر با این دو ترکیب کارکرده. جنگ ۱۲ روزه واسه اسماعیل کارتال خیلی خوب شد. فرارکردپشت‌سرشم نگاه نکرد. الان هم به جای کار با علیپور داره با لوکاکو کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/27705" target="_blank">📅 16:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27704">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdmkrCd2yNRNIrexa0rB9zfRo4RlllfnOZHNUTlSz8FsJ9XKWNMexPoVuEPl9on7gYaosnKH3MuO3hxmnYH5dHbI9mQSuYJ-VNu2lqm_nO4beqDOp4A9HlVYU-WNctl4fm7rQ6aBNx46WXPHpGaXYbsoazcd6iutv8e1mP_jxG_-A1rCNlXmJskEjXPVWqPMHSdPBw8fGAGKex7qNefRBEBWUFt40AnPSSicSw4nl5wYOAgDOZSbhotsBOBCq3mubEaH7PsvsZQ9U-SwIA5yEXIv4G-Qu-R7MaOcv58YTqrnWyopXdePW_MBgynUtY2MSRzEkCx042UZx7XlxMHkjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
هفته اول لیگ برتر ایران
🇮🇷
چادرملو
🆚
سپاهان
🇮🇷
🗓
جمعه ساعت ۲۰:۰۰
🔴
انواع آپشن پیش‌بینی برای این بازی
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/27704" target="_blank">📅 16:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27702">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iuzgNFPAeHxasJX4bG4mTpSnVJoNUtD-Lljb_DZeG-GBVnfxXphIhvvq48C8W6OwdDfJoJLI92oM15veCjDSonVZ8XkV3YA9qTdaWKTB-S9TabMAaJG4vtyE09-P2CKqq2XFUMRHG0D4Medz1G7IvScJV-tufEm--K8kguJk2z2CDY8Eddr5ryaZam3-DUsQOl130CPGURY-9uIX3mV7a2HWWFkOr-otIbWyWUsp6QkAAm26154RdnFybE6vfybjQkjCtKf1m7UwULGi2uxuzyJwt4BqnVYW5KBkChLHkzhXlXQTLI1IvJGJWiz-xh0N7Mp_ltiYfwQfewTQJyovtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kkITcL7a0BS8mBzM812y0o-nKVBJrvTd-miv1ZXTaAFbct5natS4iy61zQHql9iQnp46OJXxlu0Qi7zCiKQbNI6m2IK9OIfW2A-r01dwp8kNrCzQHR4-p_D2VcHEXRNNmvJxmLDdfg_BTck7siUYMo08DZlP6k-yZ4oyHN6mNe4Bs5EFhx1Sl3tLnqRSYYGQgSHE6J2E04WUXyOBIpLsQBLzjOnBaQIVi8ED4P-qOh1HfS-rYVDyrFX8zd1ahh97owaViqB3kiGYJLX9zB2cyvUzGHsQz4gmpEALNTDEz9MTt8ppVoDKsv7NTTbJ8bXy2PnYlAULC6lVpPoUgyK6UQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📹
ویدیویی از مراسم ازدواج نادیا خمز دختر پاکو خمز؛ خودش‌خونسرده ولی پسره چه استرسی داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/27702" target="_blank">📅 16:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27701">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umk9hbz_xeg8GZ134cjLecpdFSFbINSwk-M9rg8CmCM1cPvM419vz0TAOGsjbJomSjrby9GhCyOUaVyWR2_TxAAZ1wn3xMxoQKJ16U63gnbiUULrnyjmCshOBuDsQx6hFZdOiFk2HUil1uvDG8H4izsrMc3EJS_IfChvb-ZSKcSWXt6fibF6-Mzcyl_3NtbWKglT7B9klR37Mh6GpWrZm_32HHFxCoD7lj2MpiYBJLOwoXchhR2m2_Sua5mYv76ARd84a7LM6KxHOggRiZ1xrjB6U1kMzFs9SAeMU8XOTCSnxQvRX8cvcGTr2r3eUrHPR5LlF42AeyoKHB--nhl-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام باشگاه پرسپولیس کوروش اژدها کش پدیده 19 ساله فصل گذشته آلومینیوم با عقد قراردادی پنج ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/27701" target="_blank">📅 16:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27700">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
🇪🇸
🇩🇪
#تقویم؛سال2020 درچنین شبی؛ این نتیجه رخ داد و بایرن مونیخِ هانسی فلیک بانتیجه هشت بر دو بارسلونا رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/27700" target="_blank">📅 15:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27699">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kU1SdeK8MgBmjVHpWEgNqWwxXKUgCV02LlVf9B8B5BYOqtT-5EFhwOxXKAVGnhiaHcJ8PxxloeQkCgKeoQduRR_9Aqib9y234_ir254kwteeq73tDIV4FRNNx_m_hTDygv48Q8QlITN3WhYgRYLWPvHk3KXd7gWnL4n-G5tKt5HkCo10OOA9aLMN2ZHgemQZrgkRN3Mg3cvig1BYZ53sk0cb3s28tqAGPeX6dgPChJ9oeHrEuZ_zihRf9CS6p0GwnEqZMu84U60Os6xts0hCQRgvIrhoV4tG3mpgUiULauIiUuXedkfCkyhlAaBvtsHBPUdJHu4ieEz3GCVPSQHTdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌امروز؛شروع لیگ بیست و ششم با مسابقات استقلال، تراکتور و سپاهان مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/27699" target="_blank">📅 15:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27696">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWrBvLyXetIR8ex8ADHX7jfylzPMchPrjc5CERIE0O1DvR8ppzIzZYKIbOMwYB00W5igkphd1oQA5yXhfdnXlIfaW7o855fLdbuQArFKFNnanrQu5TRUUMgf9WtRnzT0tNbzABXS_q6jeo8iZ2twq6trrAhqWGPfOw7Cocet0AV7blKgxP8Ta_W88m0eTNFsmMiU5wiW3mLTDtCLeM1skQlr3MsFIuZ3R954kc30Vt8pSRRukWGiSK8yQwUTaU2uYy_HuCWMvHlRkaD_D8FARtSvojKPaXqJsGPsWqx9qPCxl27Fdttap8EhEgM5n-CQ5xcN9a2vY1jr7FwoRfGEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ به مناسبت شروع فصل جدید لیگ؛ تمامی قهرمانان رقابت‌های لیگ‌برتر از ابتدا تا کنون
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/27696" target="_blank">📅 15:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27695">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlBsbyE3AIOd7lnlGsxvRXv0kVVLjdeFwfcZhJbZlUV16mKoIVORqBTQBU30kL6RIjYmZ1BVzstShm9m96qUitsuBQXh4SthqA8MJOakznR8WT_vB8Y1-q70KEBg8-DkmXg98pkeo9ko4wEEaKhs2vAk5fCkrv2sV9cWwI8yBW1T3TNchtdhbX_NytUgazf8rzANWB0ulbIe6rF0AKzLdZgMVFdsG-ZyeP0zIMW4bLiRDzHqWYyhKbNnX2IFgJigV-Zk-7Oh1uYboT-13mUzjiZlBGq4uCiqmWT6UTs_CFvYLQRRZgdtnJzyp86M9h_C5xte1oHZOkwPuPGuQSCoDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛ موندو گفته:
چیندو اوزور؛ بازیکن نیجریه‌ای که در بازی دوستانه از هوش رفت و پس از معاینه، پزشکان‌مرگ اون روتایید کردن و حتی باشگاه‌ بیانیه‌ای برای‌مرگش منتشر کرد، در سردخانه به‌هوش اومد و به بخش مراقبت‌های ویژه منتقل شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/27695" target="_blank">📅 14:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27694">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOGeDyYL3hP3aotdBGitSDgR7L6A_vLUGCJbyBk7yXGG5fX-S2vZk_UPrWZvLJPiS5tG22LZszOnQtTHGsrWNJnrwzBvXx5UIcYeoe3D0SS5OYc-G5LNWBAkmpTIirmDNvuEwGIPbF5AAeLOOxL1U5l0UgElOY7PLrw7WJS4O5aDPd1XzAC5pMwxRk8V2W-1drsG-LlWZ7Fm6qSvrPloDgZfbnu6kyBtYZy9PnSpi685fusXj7d-5D6c0i9tsTabqV_k2p8J8del9pYWl4XTY1DUted-4inEKamuZNGbl5p4zaEWZ5ThwkzC2nYL1A8JkW_U6_x6H8hWFYNTpbOCUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ مدیریت باشگاه‌پرسپولیس امروز ظهر به نماینده مهدی طارمی اعلام کرده درصورتیکه این بازیکن‌ تمایل به‌ حضور در لیگ برتر داشته باشد باشگاه پرسپولیس حاضر است بالا ترین رقم قرار داد رو به طارمی پیشنهاد بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/27694" target="_blank">📅 13:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27693">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3094b93ff.mp4?token=TmMks67dG0uqdnJ0IxDEA-y6-lHxb5IMcPMGcWFzDTnoeYtIBOeUhzzwjPugnUUcnq0GqI6lALG0oILjply4Dc89PcoiNEhjxn-J1N6RdotZ5dUmZBZ_8-2O0bC7v1o3xEcsU2SL3vbpoHX-IUdbRDqZ6K0BY_nuYWFcfNLeD1mI_QHHpkAtYHjo1scwdJNwXWgpQ-dKVsQerFYZADx4kqr0PUebexQQvZg8zwgMQgdTAm35hRSwCc4mpjjfCokAfQdogcTamVI7u5F-g_Mt8iQeTNbDScEFQC9IWtWhM_MEE3ULlVeMkS-yn3UxFmpfCf7Ut4LCNACwuIerVHEXZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3094b93ff.mp4?token=TmMks67dG0uqdnJ0IxDEA-y6-lHxb5IMcPMGcWFzDTnoeYtIBOeUhzzwjPugnUUcnq0GqI6lALG0oILjply4Dc89PcoiNEhjxn-J1N6RdotZ5dUmZBZ_8-2O0bC7v1o3xEcsU2SL3vbpoHX-IUdbRDqZ6K0BY_nuYWFcfNLeD1mI_QHHpkAtYHjo1scwdJNwXWgpQ-dKVsQerFYZADx4kqr0PUebexQQvZg8zwgMQgdTAm35hRSwCc4mpjjfCokAfQdogcTamVI7u5F-g_Mt8iQeTNbDScEFQC9IWtWhM_MEE3ULlVeMkS-yn3UxFmpfCf7Ut4LCNACwuIerVHEXZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌سائوپائولو داشته‌ازکشور واسه‌بازی دوستانه خارج میشده که تو اتوبوس تیم 86 کیلو ماری‌جوانا پیدا میکنن؛ حالا سه نفر از اعضای تیم و چندین نفر از کارمندای باشگاه مظنون شدن و در حال بررسین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/27693" target="_blank">📅 13:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27692">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇪🇸
فابریزیو رومانو: هانسی‌فلیک‌به‌سران‌بارسا گفته اگه شرایط جذب خوالیان آلوارز فراهم نشد با لوئیز سوارز مهاجم 28 ساله اسپورتینگ قرارداد ببندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/27692" target="_blank">📅 12:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27691">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWtqaMkv32S0hIWgRIabNtRvjtTbe4D9dcDzqHEhqC2UZdJgTp7d3dNePoshcBEBmB_cjqlJuGp-yk6YZjwkpASKvFt3ZhbeJ6WNaqFULHBORlJrso9fhMjhfAoLMO4_FfbvCGhJ0OAWz-inFsIYbWX5KzFKxQq9emEiJM0x1vDUxn-hXqlKBiQyP5aZBTryzUkGQJaYT3tqFUr3kDL35UW3amDHVV6CApMsZiKHnU3iVRvKf9a_Ls5l_iesdoixtu2r0G-sy-UGH8Mm8yzOnkpwUc0m8jMMF-KwhAryByUzKvwc2goKebFL46Y1bwjKHP8Cb98dWALkQia_g8fD1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇸
🤩
#تکمیلی؛ خولیان آلوارز امروز بار دیگر به مدیریت اتلتیکو گفته هییچ علاقه ای به ماندن در این تیم نداره و از آن‌هاخواهش‌کرده تا با انتقالش به بارسلونا موافقت‌کنند‌. سران بارسا بعد از رونمایی از رودری سراغ نهایی کردن انتقال آلورز خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/27691" target="_blank">📅 12:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27690">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuBJQw0JtpLSGOCm6uySRGfeATiIwfUf-XC3ci6bJ8dWwXGBtj0QmBnSvF7-f7V6Sts-f2MTBJv9izNsCn6QjmoZiOQnATBeTLpvecYHNmrWkbucHHRFHOVeCaK00_zucZdfHKlE8hvT9QPEz-ziNZph0_H8eJDbaeyULKoC1e61-hbPgvvUoaYO0gV0Yk5xbhxsjyiTSA2Bfjno1wDqPf2zaFOmKs8SMoSv9GOAWbG_GtrLmMK3rgC2MMVUi9tfeKzCQFkdN2M3h-02OPh9FVFE4ud9efdQZN9MQqqD6wgvDjyLjKjj5fjVgACTfeRxkXJvJ61d25SZHvxB4dj-NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفا؛ درصورتیکه پنجره استقلال باز نشود این تیم درپایان نقل و انتقالات نمیتواند سه بازیکن آزاد جذب کند و تا نیم فصل حق عقدقرارداد در سازمان‌لیگ‌رو نخواهدداشت. این‌درحالیه‌که رئیس هیات‌مدیره آبی ها امروز عصر گفته بود که حتی اگه پنجره باز نشود ما…</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/27690" target="_blank">📅 12:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27689">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcLqPnXPFxvRfHQFsIZCF8O_mSmy_XECTeBAb70Ggo-LwFA9ScI0TMIAkRy7a77oyOgZnzE39Kf_yG9sFk-s6Amud03r3PrV-OOFM53ohkWnMxZBsQm8TlKpE0UrO-NxZKzbnIMbWD9lN1ErBVhOAHa4TEvXY2-GJoNDGxUfj2m--P9MtNBbSgV5JlT_LC0pAMYeiubhBhVpLNGPZtDMma5vdEhHubXFMl7msWV1MGHOJk05lU1SRFuc5tc7CUfmwubuX9KvCLinTkWoWpcvf0CM6SivqJYguD7dTfbyg4t7NVyxgRUhjTM7g39Fm5vonfvp4eR5OixHzex8A2B-lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩵
تلگرام‌ِ‌عزیز۱۳ ساله‌شد؛
تعداد‌کاربران‌ایرانی چقدر است؟
۱۳ سال پیش در چنین روزی
«تلگرام»، شبکه اجتماعی‌محبوب‌ایرانیان‌متولد شد.  تلگرام بیش از ۴۹ میلیون کاربرایرانی دارد. ایرانی‌ها بیش از دو میلیون و هشتصد هزار کانال دارند که در طول سال بیش از ۹۰۰ میلیون پست منتشر می‌کنند. این تعداد پست در مجموع بیش از ۱۷۰ میلیارد نمایش به خود اختصاص میدهدکه‌نشانگر کاربردهای گسترده تلگرام در ایرانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/27689" target="_blank">📅 12:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27688">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmeGIdA3UQXiiSFbhYyWGjM3ptILlzkQnysJevny2pltODNMwFhnDHeRXYbmmSvqTqoFWEw3XQ6udU6AcsxznIw3y6sAfbZ-dHUQvEZOrUnjm-OKkjnPpdgcg8qUaUJfje6OHpPevgrrfScEx4OzaeC87wapP6G_IRsm_R-wxZ2uxiyLpQBA2xnGcyLAwaEJPFjWsvWEgHh2TJhFMAQtrcMKoF4ha8Pu3xFoaWfNS76yUwhC6b6hUiG21f0IXFI7ACPw6LVmdMEmceoFrb5C41k02f_Dtr4SZqIGrScNbH-Q9UugGE01jnandF3KfC44cj5m-z1KY_cloD5uIyLBkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شروع لیگ برتر ایران با بیمه ی
🤩
🤩
🤩
🤩
وینرو
🎲
⚽️
استقلال
⚽️
✖️
⚽️
مس شهربابک
⏰
فردا ساعت 19:30
🚨
ورزشگاه شهر قدس
🎲
باشارژ حساب کاربری و پیش بینی رقابت های لیگ برتر ایران درصورت پیش بینی اشتباه تا سقف 50 میلیون ریال فری‌بت از وینرو هدیه بگیرید.
🔥
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده ی تمام مسابقات
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr23
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/27688" target="_blank">📅 12:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27687">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPVe17HymHhnEd8u-eylOve1Qj2smAQjw72qsmquIEaDPOWXNF8EH-O346i3EoSa89v3wESRNcLQkZNmFSvdVldEZCuOd88n1NDTE8H4gI7pWZM9h5UXYvQ3zxwMzV4Gc-rY-zQi8G4jxC5tDF03N_lEoOXBPpcMvzT7sU_uxK-V089Sm2JCmKZrYuhh0In9OV7vHvAs8aynvmBn-ZI8tf1iBMVv_2oIDg0IIC1Ua5uC98_9IHtuR2olPf6DqRCNX-Dr-jil1QmhWYN0qazCpKckFZpdZOBqVnxvumXEFwMEyYgbdZJb9_FKkpQYnpex757i1PWbqxB1QreAf05Z-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
صحبت های مهم فتاحی رئیس سازمان فوتبال باشگاه استقلال درباره پنجره و آسانی: پنجره استقلال روزچهار شهریور باز می شود و استقلال میتواند سه‌سهمیه فیفا خریداری کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/27687" target="_blank">📅 12:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27686">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mD3xZ9GhzCfdSe4BRbD019VPkOpzIOk0Tb4FkXAKTZyK3ItxDu97xfb_6lgrNemEEPanmcBaWGHS_Z98T5TWG0ScIGat5BOXHEp2OT9kVlw6atAKhlLB3pqucqM_khQEC3lEmN9NCV0mtrXUZs3EBcIN1gup7E7JUIYyoXWJYmQahAk0uIy9UxKlHD6Ytvt70pZo3VYWge8L9poEupPibqCJ1_du2s_8ZOCYciMR_M3rmR1Pto7BMXX6GCjG26dVwN8m-Zv1Ed0GJUe3jzkz9JMcX_BXImj2EfUH4jFZ5C4lPSDbUOQ_dcTovE2d_iFMFK5R0A7hlWT6JqJb4jY_NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در عکس‌هایی که باشگاه پرسپولیس منتشر کرده علی شیخ الاسلامی آنالیزورسابق‌استقلال دیده میشه که به نظر میرسه به کادرفنی پرسپولیس اضافه شده. البته‌عجیبه‌که‌باشگاه پرسپولیس در مورد اضافه شدن او به کادرفنی اطلاع رسانی نکرده و مشخص نیست شیخ‌الاسلامی بعنوان آنالیزور…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/27686" target="_blank">📅 11:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27684">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7cd0640fc.mp4?token=gNLw1tUAOh41Pf3X5AsgEMq-l92NyxduA2JrXGfPGr22526z6TAsHZEhoxXdn9pNJcsmb02SnihMiUXfu9WYTh8g20Pn7j5x3encN551-t_BBMSiCXNph4wNUhAdH-35EHTxZ0QdGAb-_hriEE1PQIz7POJF0oS4AqlgtoyGhQq1O6J-ZCqXM-a2QQ60H-92fQDwWhY1ffqfBAyxSwOmp9QzQeU7za8oj6z_4azuDWcHwbbupvvKFkdhBu6h5t2OCz2ise90AAXj4oaSVHxBcQKs_hrJYNu01roQMQNNdOkoP6yBUyJu7MAXiJbFTlTFVUmPR2i4z80b5RudlcbZzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7cd0640fc.mp4?token=gNLw1tUAOh41Pf3X5AsgEMq-l92NyxduA2JrXGfPGr22526z6TAsHZEhoxXdn9pNJcsmb02SnihMiUXfu9WYTh8g20Pn7j5x3encN551-t_BBMSiCXNph4wNUhAdH-35EHTxZ0QdGAb-_hriEE1PQIz7POJF0oS4AqlgtoyGhQq1O6J-ZCqXM-a2QQ60H-92fQDwWhY1ffqfBAyxSwOmp9QzQeU7za8oj6z_4azuDWcHwbbupvvKFkdhBu6h5t2OCz2ise90AAXj4oaSVHxBcQKs_hrJYNu01roQMQNNdOkoP6yBUyJu7MAXiJbFTlTFVUmPR2i4z80b5RudlcbZzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#افشاگری؛ علی رغم تاییدیه فیفا مبنی بر اینکه یاسر آسانی هیییچ مشکلی برای همراهی استقلال در فصل جدید نداره و کارت بازی او نیز صادر شده اما علی خطیر مدیر عامل سابق آبی‌ها از مدیران تیم ها خواسته که در پایان هر مسابقه بابت استفاده کردن از یاسر آسانی شکایت کنند…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/27684" target="_blank">📅 11:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27683">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/405e5ce55e.mp4?token=AarMwSVMN4IfD-Cvw7FnEMTdv6ggrM-NaJJKZ4NXe7Nz5-dUr9btCqMObPtL1E5pbfLzh03c2hBi0sD6WLa2CldNT4gLd8c44sooVnpvMvW-V_jNyddDmwoE5VgwFidAmaF0mT0Wr_LXiZQm7Poh9DOGeA2StdOg5KzPd-wa1Ygi9LKuH43mtrP4PTjrBdiZ96eiVK1Xrscfrhz33G4F33SJp03mQT7WuLfJSsBJH3k70G3Wf5KuSheuSbJN80ig9bex-9tiesHFdsWtUahvOPvNAf0U2Aj-k5sbdsu9VrImyP5Vxw6tVFxbG5lKL7qOkezjfMbKOtTd2mtZ1mNJLTRrKcNKrAJjqqKfrzCD5hdUWFpGfTR-ypFepWqvMsZz6slxXcd9EKr4_v6TYxWKkJbC_WjexpTkP4gfClqn1dhMuxqhIpu6mkpGS_XMhAiFYODJ0wULSB0gD5Z459lEXqFREHguvqvGIXAla604Yy_3VgNaG5NdqbVELeGD5BJQjv-3fCIfo3UUe3bsCq-9OC8mQDR4EgW7EzBBjhMg_wtyNh0hZDnbh1a77IAYUUCMp86N5zVCswMCwCUe_RSbWFib36oIVRP5qjTZo9m3pmzhqlTX5AXGSEi0hLilYx2SNkzCy6o8wzY1BZwzgp7F34pxdgEcLb-FfIeXZm6GSTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/405e5ce55e.mp4?token=AarMwSVMN4IfD-Cvw7FnEMTdv6ggrM-NaJJKZ4NXe7Nz5-dUr9btCqMObPtL1E5pbfLzh03c2hBi0sD6WLa2CldNT4gLd8c44sooVnpvMvW-V_jNyddDmwoE5VgwFidAmaF0mT0Wr_LXiZQm7Poh9DOGeA2StdOg5KzPd-wa1Ygi9LKuH43mtrP4PTjrBdiZ96eiVK1Xrscfrhz33G4F33SJp03mQT7WuLfJSsBJH3k70G3Wf5KuSheuSbJN80ig9bex-9tiesHFdsWtUahvOPvNAf0U2Aj-k5sbdsu9VrImyP5Vxw6tVFxbG5lKL7qOkezjfMbKOtTd2mtZ1mNJLTRrKcNKrAJjqqKfrzCD5hdUWFpGfTR-ypFepWqvMsZz6slxXcd9EKr4_v6TYxWKkJbC_WjexpTkP4gfClqn1dhMuxqhIpu6mkpGS_XMhAiFYODJ0wULSB0gD5Z459lEXqFREHguvqvGIXAla604Yy_3VgNaG5NdqbVELeGD5BJQjv-3fCIfo3UUe3bsCq-9OC8mQDR4EgW7EzBBjhMg_wtyNh0hZDnbh1a77IAYUUCMp86N5zVCswMCwCUe_RSbWFib36oIVRP5qjTZo9m3pmzhqlTX5AXGSEi0hLilYx2SNkzCy6o8wzY1BZwzgp7F34pxdgEcLb-FfIeXZm6GSTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب‌ابوطالب‌حسینی درباره صحبت های عجیب‌گزارشگرافغانی حین گزارش بازی دوتیم ملی فوتسال امیدهای ایران
🆚
افغانستان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/27683" target="_blank">📅 09:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27682">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa916cffe.mp4?token=end3D0GZougl-VaDxCVoQcCA6z1hvYZ9wrIQegeP6Vfx0UhSGt5Ahg1pJOMdznVlder3nuCNzs9oOt8b0c_bxmO73gA_56e0u56Bg1qA9YH8g6lyvQPzta7zAg6x0zKZYTbmt1j2u7YXkmT1aqC2W0Rbn5i9Uk56P4gpOZLFMBK3NRueHLYzSwy1r3J3J9CUIgyeW3A5ls8Gu9gKFEPTqtX7zX25tjoLK32yWMaUmuKbs02OoBMdxpNTlvVgAg8VLeKWUAcP-BaZZLzSXZ8IC7Sj3xAXbQu2Hl8J_5ga6p1CL4FJTkgO3iczG6G3zsjVsHHZVdrAIpL5tukftc5sAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa916cffe.mp4?token=end3D0GZougl-VaDxCVoQcCA6z1hvYZ9wrIQegeP6Vfx0UhSGt5Ahg1pJOMdznVlder3nuCNzs9oOt8b0c_bxmO73gA_56e0u56Bg1qA9YH8g6lyvQPzta7zAg6x0zKZYTbmt1j2u7YXkmT1aqC2W0Rbn5i9Uk56P4gpOZLFMBK3NRueHLYzSwy1r3J3J9CUIgyeW3A5ls8Gu9gKFEPTqtX7zX25tjoLK32yWMaUmuKbs02OoBMdxpNTlvVgAg8VLeKWUAcP-BaZZLzSXZ8IC7Sj3xAXbQu2Hl8J_5ga6p1CL4FJTkgO3iczG6G3zsjVsHHZVdrAIpL5tukftc5sAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویویویی‌جالب‌وتامل‌برانگیز درباره داشتن "ادب"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/27682" target="_blank">📅 09:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27681">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc7f8a7f15.mp4?token=YKiRcoBcTX3v4GF2opWg2E3SwfYhHgCAdrMs5ZYCBMwBAtSDWKespLp9fNica-jR3ExJ4009rSAomdJOIqNEaieJMQYLd2FDgrHHAiz20xiiiJMgQt40bdyfpdF4JZ1DYCSIIQaW6jQg424ZsBNDVI8ZwaJaIzsSJPfDisIeq6667GZqBz2_bWDVC0Z9-sVkaNfXN2jzit7MzbDNnsB2X1XPQQp-HvBLO8Ku7wDEXQ4cxSMfrsHDriGVaoK6xL-K9qwyPvQwx0n5ZUKYXa7juiFw82kKMxMtkQzWEtc58obR9-f7_DNSS9AQaZ-jGZCSKej-p5HHzUlV1RUWYIbuyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc7f8a7f15.mp4?token=YKiRcoBcTX3v4GF2opWg2E3SwfYhHgCAdrMs5ZYCBMwBAtSDWKespLp9fNica-jR3ExJ4009rSAomdJOIqNEaieJMQYLd2FDgrHHAiz20xiiiJMgQt40bdyfpdF4JZ1DYCSIIQaW6jQg424ZsBNDVI8ZwaJaIzsSJPfDisIeq6667GZqBz2_bWDVC0Z9-sVkaNfXN2jzit7MzbDNnsB2X1XPQQp-HvBLO8Ku7wDEXQ4cxSMfrsHDriGVaoK6xL-K9qwyPvQwx0n5ZUKYXa7juiFw82kKMxMtkQzWEtc58obR9-f7_DNSS9AQaZ-jGZCSKej-p5HHzUlV1RUWYIbuyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از دوس‌دختر لامین یامال پرسیدن‌چرا نامزدت رو بعد از پنج سال ترک کردی گفته فهمیدم لیاقتم بهتر از اونه و منم حق انتخاب دارم و انتخابم هم یاماله:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27681" target="_blank">📅 09:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27680">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGS5nNYX9F8efzqb4utio77IB9bAPXp0ztwaDDBSljfIZoLUWg2tY_x1FZgxsUVkvt-rjhno2G2WZDCVf-GjIUlmUZNRsku1ALHveVmrS6QfnUn55OO5j35IsgP3WJRIErJo0Q752Jcz8dX6_-pW2Y1nSAaaXJuknAGjDHLXgZngCqNq6-rpH3mFonIRZ2O0hP_t97rOCrT7-eHku3xPr-sHIeNUxbW6TkScgqvaEqhGI9jzwncCTIiR-uMVztO1pqXTRp-sHupqX3Y5kKa9me5FjpIVVFG59eDenYkKpxMcsNqBlRekWzp8zTPn-Pc4UXdtFEBHV3hRX7Uwmiwn1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
سیدمحمدکریمی، محمد عسکری و آریا شفیع دوست سه ستاره سپاهان دیدارهفته سوم با استقلال رو به دلیل مصدومیت از دست دادند. این سه بازیکن فصل گذشته رقابت‌ها رباط صلیبی پاره کرده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27680" target="_blank">📅 09:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27679">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ea083066e.mp4?token=H-lw-0i4-LeY9TC23FjGrDvEb-AR0Bl9WSpnzc8ynAjQWsVGN8fV1nLmK_lBbqvpVKYpIuAtmZugom86U04OkmlF_RxULOYqdi5W-c9r8qnZ9UIyh5pnGsfLt9S-Yc-15CHruv9WyKi6xNpeg_YkTe0neKW8sSRvh3rHC-NnM6-7u4-E3zbcsqIrmdgiQ4rguZCAh2zIBL32rGhnIDShxLWq08JFAd498VOZ2hAVyl51Eyr0QvIhGdeDwkZNdvgZitwDstTKcSj-03R3UufSpa6H-z5kzpDFrSOZhrjqksMnEJcBNK9rkHhGAQ6ufYTFX-uQGz1zyvtPf-0i_cFRKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ea083066e.mp4?token=H-lw-0i4-LeY9TC23FjGrDvEb-AR0Bl9WSpnzc8ynAjQWsVGN8fV1nLmK_lBbqvpVKYpIuAtmZugom86U04OkmlF_RxULOYqdi5W-c9r8qnZ9UIyh5pnGsfLt9S-Yc-15CHruv9WyKi6xNpeg_YkTe0neKW8sSRvh3rHC-NnM6-7u4-E3zbcsqIrmdgiQ4rguZCAh2zIBL32rGhnIDShxLWq08JFAd498VOZ2hAVyl51Eyr0QvIhGdeDwkZNdvgZitwDstTKcSj-03R3UufSpa6H-z5kzpDFrSOZhrjqksMnEJcBNK9rkHhGAQ6ufYTFX-uQGz1zyvtPf-0i_cFRKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌‌تند رضارشیدپور مجری‌سابق صداوسیما به‌‌طرح عجیب بنزین ۸۷ هزار تومنی:
هروقت درآمد روجهانی کردید بنزینم به نرخ جهانی حساب کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27679" target="_blank">📅 01:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27678">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boeMnTu2CmcsTUsWrzvZw9X8puSTpjxu0q1Wyqi5yPtA0VyAzrGxeIFQk_9mhvmh20Owa_GmrAhkJ3gouPTCPKiIbZF6yeAk0Ss-jKlcaICNY2mmLG_RtCVcRov0i9JDACRMZeDBO2z4xfLFygsao9CczHRg318L5P3a1Wa5Qgv2BcdegyjmkbC4sVtG4TldXDgcpi_EEx6PtNVwJ1hMWymJT3RJoJlTjeSMWcZOYg2tZ-2-vvhpcZqEzNO5v92qzM1fDb1XyAQWl72ZUDmTjTYH5BhF9hPlcqKNafKzos-_cYQWRD9AOlb9Zv5dbrdB2PL4QNStQqZtUseCT50Mtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌امروز؛
شروع لیگ بیست و ششم با مسابقات استقلال، تراکتور و سپاهان مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27678" target="_blank">📅 01:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27677">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoH33n3uJSgjp_KPNg6F5BwMY0J5Vs22k3mMMNr4_HQ8uyewGfMWcrZKQjTuzdQLqw5esa6CvDzcisWY3B3T8Y80gtqdcd3yd_SpX2ydZL2vPINOOTyIOeghYTX5JyTzCRbjhGxcHto1v7OZocDakJb3raicqK-GJ6eZ5F3LwbFR_y5CbFGcLVXLAdUcwTd_cHdsjcKS0uBoKw5EWmlJWQuJna00VeiqCLXOGY7YM2q1SMmc-hGpVpPJWfoA75GscuJCDVFwMwWjCdwuYZiZRTd5KXmfAtlxAAJNg-wrCa2OrKG8G8bGPoaT5fjNt8UPrii_uknfQ1uAyy1hALrpVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
حذف‌زودهنگام اینترمیامی ازلیگ‌کاپ درحضور یک‌نیمه‌ای  اسطوره لیونل مسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27677" target="_blank">📅 01:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27676">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H625TuxEfg_UCV-cN5WyvVM0uEvVqzgrFq2S8R_66LSM4qxhlJ9dP8F95hdmHTFQ8ipEzQlxKCCXz-z316DAkWSAsz8ugNIKa4pUYo6YVHwvEbqOsF6SNZGovvWbbks-DCdTjBUwBQd3niOTd_W7r8vJfkOGN3N1tgIRH7y7FUcMbirEmGC6VJMW_iNM7NOJ3kkj3gUQ97m7TEqHtDKzp73GpnALyv8XejKd2dPDhMIpYJLrtxpxE8LXXdrsZeYyi6PbWSIqKj4nAOtiPaoAMAt1DFR3YMpO3wxhSTlnheUtLgQk7OmY7I6sF--7iXmiCePjaNRUQVx6zq2kyiZGyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تمامی قهرمانان لیگ برتر خلیج فارس در فرمت جدید؛ هنوز تکلیف فصل گذشته مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27676" target="_blank">📅 01:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27673">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQOjHerl6sJkQNhXYCNZQDi6pPv9fEqny_IJQMZhf2BUlskSnmrbtoVaDB4LG8yCgTiUFpSAgWiDBJ2hEYM3pMmrneTpta9CKvzIAEFzWUL2ORffZipkINCRi0NPKqfajzUxEuUxrTqyAkY9QA33JtN5TJLLcDJKDNH8RKB_u3J9yS9wXl5qAW71q72JSrVBH1vYC6BJ6g_9kM0oHYGJoi5P7Y3k2Xj2W50t500XzXuPp37KUsfwzWnYOgupvxCaDDmhdWds3QGhrsvX70VPiw-q85U5WOUOuLupEPeTLQGQonjBPWYUpb8cBDDhfYxLmJ25qxQyJ_BJzWTfhsVWbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fe1ugp_URsnAPZJvhEtJZXbpS2cl3oi3cOYih-q3QM1zqO8C511vPPRyOStuqq3Xlg8iNR4OkYVCsOGBUhygOoq9Ccydv2pt4-SPid8sxVSyg_yMOiwuVvj-yTcUfJapvne6KSJ9t6DUNmTzGDs5KGgeNFDTz8u89RCKFSfTxyJ2P-kLzW9Il7YoOe-7XiajYMaSFFjMFka86-ciGsurGSk1aCiWSzUcL80-wkCy6qtjbBHprPzjhtWHduTJGxDgfXbSq8OJ7he5Eg4EGZzPs2_2oKYQIV8TZmLPf5LRjG77FziFfR-wVXDU8nIo1qAmPnH9rF05Chmr7r2NzGANJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
🇪🇸
#تقویم؛ سال 2024 در چنین روزی؛ رئال مادرید تحت‌هدایت آنجلوتی برای ششمین بار در تاریخ خود قهرمان سوپرکاپ اروپا شد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27673" target="_blank">📅 01:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27671">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/op-8QU6u_byo7HFWRN4IUAkpdFuQWR2qDaHdnBNKo0jqMMJ-hIywM6YkumJUbG0FxIfd0qIfvV-GgeCsh79GsKLjjVutt3pU_rzglJMYsRAsIzXgax9IfHhX8sGrofiP5dWuWWoiI9mTX8wgGQlMtuAJO6bkbkWA8YUDPkEw_b54WUf1sF8GlcTUpOyEUzFB9GjDhKXjmJt-MRosuJVijWPVRjibMUh5clsVPJyv6wXd0FMkB9ZXbJjLVbtJaSSiA-MCYZLiPJlN24I8arcQhYZ8MnrnjqEqhc35Xat9VBpTfB9VAi0gOa6_V6f0JzbQwj0OkUsUALQeyU-pvVne7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6583225e2.mp4?token=g3By_mQ4Kps_YdNTJo68OTaLz0ZJ2KWwYt9KzbNEbim8asMEgT5n8QsRhNyD94Fy6ibs4QgqBN_sHkAfWnQ_9RFR7jDWK11hKe7oPMOCezOkV-ldrgl9t8Qt2bCM2TWVFOhi3ySw533sQmH81bEn6C_54TMVMO5HgsiPl1AeqOdX9GYSuxRPRRO51TTeEWgzv6PHhxIbVVKTv-Ek2RXrDmttcG03QjmEjd_QWVfofDA4WygHuLUzg5b1WMEMOMB0nRpoOkxdmbvtlLwmJgsbrkGAqoJw9nNg6ZNIp24gvJqUsatwpfhf7vKuX0ueDuBrVOqKFCvmEjZUbxsJ1ni0sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6583225e2.mp4?token=g3By_mQ4Kps_YdNTJo68OTaLz0ZJ2KWwYt9KzbNEbim8asMEgT5n8QsRhNyD94Fy6ibs4QgqBN_sHkAfWnQ_9RFR7jDWK11hKe7oPMOCezOkV-ldrgl9t8Qt2bCM2TWVFOhi3ySw533sQmH81bEn6C_54TMVMO5HgsiPl1AeqOdX9GYSuxRPRRO51TTeEWgzv6PHhxIbVVKTv-Ek2RXrDmttcG03QjmEjd_QWVfofDA4WygHuLUzg5b1WMEMOMB0nRpoOkxdmbvtlLwmJgsbrkGAqoJw9nNg6ZNIp24gvJqUsatwpfhf7vKuX0ueDuBrVOqKFCvmEjZUbxsJ1ni0sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🇪🇸
#تقویم
؛ سال 2024 در چنین روزی؛
رئال مادرید تحت‌هدایت آنجلوتی برای ششمین بار در تاریخ خود قهرمان سوپرکاپ اروپا شد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27671" target="_blank">📅 00:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27670">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnRl44Ye1Vcy_5EkBJCL4QM0FRDkY5UAb51hmpqxKXCzbspAkjwkd1xdj-DmSq55AXiLw09qIdyMUA9MJdWsww_SraN58YkLBZXZSeNujxCgdZkwCy0vEYyZYX_BafFkjEtt9wxO348KBqx5STsQ-z06q30PdlfuOhMNNoKrtd3FGPpSWST3XDs5fRZLyy9YoAi_NSNpgjDmcdTbHEUFkEE1-YRAJZIALgo29IzxuM2M9KOkRwmZD3ThKPSlsjLkrh8a6AtsvkGN8-X0evA-t_Axn-wdKKmi_o-rvdVVvNAHgvluIJVEVIlnO8PyksbdLS0pkjbGtQlyFBZCypX4yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛باشگاه ریوآوه پرتغال یکی‌از دوپیشنهاد اروپایی محمد محبی ستاره 27 ساله سابق‌باشگاه‌استقلال است اما رقم پیشنهادی این باشگاه 400 هزار دلار کمتر از رقم پیشنهادی تیم استقلال به این ستاره ملی پوش است. ایجنت محمد جواد حسین نژاد و محمد…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27670" target="_blank">📅 00:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27669">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d88b1013a4.mp4?token=IPu5QO3xD7ukBfXH0aA8y72UyKhe9OWsOzUP9YdXnsqQejMeyXSW2qhSV12FIe4jojKY0-imlpa_4rjLJ98hqZpEFf6FUklZD0mfL8GlcsqfUwj7qrd_VEaUhkxYmH6L9PpX6ybGki98U09wOUQsWXY_mN5TiQZIdZz0TOs2MPbh_k6atUEac54TRb3faft05OCMAq0QBI649MJUvABZtJZL3nCam00n4k9S0II1p76tGFaGQKyDyCW6YW5A-lXZgTp3qYK11a7eApUQa5XxMBqULydLwvXA57WudKHpoLCrm9xASn8UUETmGSEqNvjQGKlHHAdnE_pMEaSsKBuQiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d88b1013a4.mp4?token=IPu5QO3xD7ukBfXH0aA8y72UyKhe9OWsOzUP9YdXnsqQejMeyXSW2qhSV12FIe4jojKY0-imlpa_4rjLJ98hqZpEFf6FUklZD0mfL8GlcsqfUwj7qrd_VEaUhkxYmH6L9PpX6ybGki98U09wOUQsWXY_mN5TiQZIdZz0TOs2MPbh_k6atUEac54TRb3faft05OCMAq0QBI649MJUvABZtJZL3nCam00n4k9S0II1p76tGFaGQKyDyCW6YW5A-lXZgTp3qYK11a7eApUQa5XxMBqULydLwvXA57WudKHpoLCrm9xASn8UUETmGSEqNvjQGKlHHAdnE_pMEaSsKBuQiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
استایل‌ومدل‌موی‌جدید رونالدو بعد از ازدواج رسمی‌اس باجورجینا دوس دختر 10 ساله‌اش؛ ویدیو ریپلای شده هم ببینید خیلی سم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27669" target="_blank">📅 00:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27668">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7E0k3IOPn5uasSgIAOTkIXU-cud2vKhrTWuWvDLfXwgRA9iKud0VBxzDEYrzYyrB75eUcHNOrOrg-vJ0MDAa0tHNwpbHUOYXPD5p7YdOQL3dejc9MLORhrY8T_PocGQyhADFuxVg_eY6dMgYxdSIUH7hhLJtfXj0hLC898pCStF7WMfYCBNu2mnRqCsOYVuz2N-M9XAz_4z8anzHPZC3JWgkfZnUqisWUY2BGvsUmvSTvog-268OpciFHY0UKGm9kHlRcYg6sAHtSet5jXDqe9__sXcVYznRBfZvTpf093JxL7emRLIkBmOHb5sIKK8Ap-CBk-vJf0uy3pNnKQtlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛بانک‌شهر قراره روزشنبه‌بودجه200 میلیاردی دراختیار مدیریت تیم پرسپولیس قراربدهد تا اقدامات لازم رو برای جذب محمد قربانی ستاره الوحده انجام بدهند. اگر این بودجه تزریق شود قربانی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27668" target="_blank">📅 00:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27667">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDfPv9T1DEnJ7LZUH_fhe2-fTY_DMqL4hgkPNQ6gr8UN7Jg0Sd1Rd6pnQQujaJ3JfdBk5pvn78wBHAxUgcBEY706KDGtFVdEBflp1-w5NWVK9iWnYIJGccdGE733uje27Y6iqAx1MPmB2npO4nsT6LziuSkkTLoS395beIRGkV5kaisSW1sjhaY7DNgtv3-4jLwJ2vbseCp8z9PS-j3lhXAYGbJCiIy-PQpSEYbu9eGjo5Mx4cfyN9Yqh0QkvXs6vSwuqRvoYgBwMHigrE6NRW_qPuNuSPehWIfgBkIXi-SElGc--AKv447D4MhiOxH88tJRkwXfzPMMRoSmxYl1eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ محمد قربانی صبح امروز از طریق نماینده‌رسمی‌خود به‌مدیریت‌باشگاه پرسپولیس اعلام کرده درصورتیکه تاروزشنبه پیش‌رو رضایت‌نامه‌ام رو از الوحده امارات بگیرید قیدتوافق‌شخصی با تراکتور رو میزنم با پرسپولیس قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27667" target="_blank">📅 23:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27666">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🔴
رونمایی رسمی باشگاه پرسپولیس از کیت جدید خود برای فصل جدید رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27666" target="_blank">📅 23:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27665">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keXq9xARmGHdew6ssJt-3KPiyuAb-1jgdKCJ41SKwQlgA4ZpSN98ylad5EMqbQtKj5XD5gXXfwaOXNEHTcMYGP7CGPNnKGBiatkYxNSAreqSCD1UmgxDe1mUPgyBYgvKd4xSrkCzm-lFfGV8rIaLqRtqI5Rnjs2IG1q81lo1jlWC02LkpaYf_CX-3xFr0AIOcUfS_Ov7o1x6_cNCK4jxQJjZzRpsRvHQWWcYND40qEsJoQFv-HW-YjQvqErxwawKjNrWL4srjM6bDZtmLD8wFiBpKuXdO_Au9M9dH3iGmoYfqLre8hVKXHvO3QIR5f2zx5d2RQGjtCAMEoRTM1KKgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27665" target="_blank">📅 23:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27664">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUTNmP4uzyx4yz5WLz_VE6lTLv4F-BdBBwjHcpwTM-hv_RzlZv9qwo02hCQQah5XK7s3qm8l6zJE7vIoZF-ixcsABgLD3vnxiTAblShfJckM62MgHPCLltWoekoc8BdMvABWdJ6tw1Te4cl1KCW52Gd01zp2KPIIZw1h1VKZ_lmNyu9XFu2awxTMQFepsi4aK0preZmQXJTh55Aw_A0GyFWlKOTqsYQV-3q8fUwjRVlrdHu8T4u5pYMVCr7BIsS6-yDL7XD5Avjd1iCpqlZOjZv5jb-5o3RRaHVCPOZA4cG0ExzzIz05WBrbp2-ktQ2DcdOWCaex3WD2jBB4mrzOXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ علاوه بر جذب دانیال ایری و جذب احتمالی محمد قربانی؛ باشگاه پرسپولیس یک بازیکن دیگر نیز جذب خواهد کرد و پرونده نقل و انتقالات تابستانی سرخ‌ها در این فصل بسته خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27664" target="_blank">📅 22:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27663">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5zes3r8-TlX6nXhEv-0T-Nz9JUOySDyRKTiro80yS9UJdl9z3w2WhvDjV5jfFLjMNsUDA9ytkwdgQpvMk4TWTj74xcP2wzuFM52KECpn1wCVRxUt6BdrYifjShYKum5lhQmna552wtY7imZlQrrorejX-wuvwRPxLv67yZTnyJG4FB4GrqxJ21y-CnBGxtJ-DfGeoyFogxB8mQPJgTrdMosUN6Wk3d8CUXk-ALD3h2ldpXsDiBenSywCOHXrG3kvFVFa7TQCsyFpVx67rof_-Uto-0Iblv7UInTg81nZG5U-jsTQGJBWBGlN35Kxs_tSJkKevq6E-g6d1RLyVYkXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
باشگاه‌سپاهان‌که روزگذشته با کسری طاهری قرارداد امضاکرد به‌خواست‌محرم نویدکیا بار دیگر از فیفا استعلام‌گرفت تا مشکلی برای این تیم در شروع فصل جدید پیش نیاد و با مثبت بودن استعلام فیفا از کسری طاهری رسما رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27663" target="_blank">📅 22:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27662">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVVhf09FP9cJ8arJsqWqz3lNks0v52XjcBxgBA2CSA5ASbQFJGYIazxhRuQIsuPXf_bh1aFrklgcjj1N-Eh_NRrQqjxwTLTd_hlC1KObIrrf1032XZQle9h1p01OBrTps14wXZbQSbcfe_6N4iWZEMRaakYPWhLKR4qvC_3HXfDxmDOP4v9u7ywt_xJgm1OepoivJzW95qLDpvH8c1oz69EiYUXamXDaNqEoPMg8yXTZeVE7N_o7xvAu-8CSg8HgVHn7HExDObSFAkkDrgVOodUmTk_n3itAn8ZkISL-4vedxVwDNcIH93L5p2vCy0U_8VSPyb3C6qEVpQuoSj0ETw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علاوه‌برمهران‌احمدی؛ روزبه‌چشمی و جلال الدین ماشاریپوف دوهافبک باتجربه تیم استقلال به احتمال زیاد دیدار با مس شهر بابک رو دست خواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27662" target="_blank">📅 21:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27661">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsvYqgytngFtZ3GAysiaOfMgeHLsToulrQ9MlVomlk_s8cPRC66Q7RRPXWyfWUebPv5r84_HhzW7VgOJI7ZGPuRBjy7o61jn3bIYqK6f-wMaZO-x5K8Z-Jdx9I9Hj2Sp2O-lm1tiyIgV4Ssgpu1Ar62EjMG8g-E2V5j9dpiSRI6lqjNBwMV1ElkOs_iGOt2FpAMdJxigxKeguF5TACci3y5rCZNg79mpz6Bz_wtT4bkmdlPrkQT4pLCsYMrcZIBvH6RWAj0Fv21u6wGOKug1wkD16EVZhEBEV5FFWKY8an0PJu3CacIlHgz6y4Cl2OUAhiXX17k29MfRU8nslFnzgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
#تکمیلی؛ فران تورس مهاجم 26 بارسلونا با عقد قراردادی چهار ساله به پاری سن ژرمن پیوست. هزینه این انتقال برای پاریسی‌ها 55 میلیون یورو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27661" target="_blank">📅 21:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27660">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WESwmLnlmsXa7J-wRf_4HLC1ijpzOKQrkGxyA9FS9b_JOaNq-B_8uqkDw7Op1ltEdsTMtZxPZKy4VcehOm00WxpBS-4fuDWMD8zyMBRKvgMLzys7lD-DLQR_5HsACQXx__9sUB_nfr3-MNirBMBDa7BXcnchYMOf8U4nkW1lU_wY-yRPZ5aLlWbbt0w67F22ZtZMzz85U4MuTr_qKAtWHNlhVCLzxJwLcNf9d1T3tU6XU3C_ifg5wAlB297lmyji0SIH51ZyRu4DKIDu5-GFIaZUKRj8DsWvLy6T0WrVz5KiSSr60F25u047V4-4agY_PP3vmAxWnaSiZF-EMIbiTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درانتقالی‌برگ‌ریزون کریس رونالدو به شمس آذر پیوست و برای ماه عسل جورجینا رو برده قزوین.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27660" target="_blank">📅 21:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27659">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iO35MRnFPhwuvlKHEP_sU67MK8YoAtfOoNO9Op860blJb8G8CldleMrnf_0M_B5bY7NDmZribnXjrBJVxVfp4Q5t4wH4f5NLm-_OPpktcAY03z5h1oVWEQJvNDdxmreniKEfYPXYb9oSruH0A7e7bnMSAUzhdM7naefGfrOi8LMbPbZ9YeAzadbez27526yvzPGtqclbQrV3RSVRw2fuH-9iPz7wfFMUyFoJ9FNRiWOcIkl5SH1-MGuFPDPURwIZMvD5-2AsQvBCOzD9Ef4nuu8B-t92Mjkn3g10ViPiTcRjIuuILPJaLNj4Fxl7Jt0vG1a02wXgYTUUGGhB66Y-0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی رسمی باشگاه استقلال تهران از کیت اول آبی پوشان پایتخت درفصل‌جدید رقابت‌های لیگ‌برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27659" target="_blank">📅 19:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27658">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9da1140dfb.mp4?token=FqEgZeP77eH7rdzQuN2a61xdET3Fzjl2wvYx4vB2IeeqOircQW0N7wqTzk0DLt2UvuaOWVkKyLaUvNGmOOnwgH_ZioluGjUmi5fdH00Y5q1rfE5cVBKihkhOgo7gkRcBLF7oMT8zCTOizSioW1LQ4FtSo3QwrAsG1qBh5iXG3BCVNNKeVeB4CfS1K9W_E7vobobIHyqtqN1BtYuvT-BQfWy-IRuo-Wgjmo7WY2UFTwp5XR7UcKUQpQ-lonwYzLvnOJdJyhmEGc-GfXuBnGkdjK51ecmWIXLS4_p8We-VIXKKbcfcdoBZ1chbsNTa_pPes2BAmaf7OGS45lR3hNistw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9da1140dfb.mp4?token=FqEgZeP77eH7rdzQuN2a61xdET3Fzjl2wvYx4vB2IeeqOircQW0N7wqTzk0DLt2UvuaOWVkKyLaUvNGmOOnwgH_ZioluGjUmi5fdH00Y5q1rfE5cVBKihkhOgo7gkRcBLF7oMT8zCTOizSioW1LQ4FtSo3QwrAsG1qBh5iXG3BCVNNKeVeB4CfS1K9W_E7vobobIHyqtqN1BtYuvT-BQfWy-IRuo-Wgjmo7WY2UFTwp5XR7UcKUQpQ-lonwYzLvnOJdJyhmEGc-GfXuBnGkdjK51ecmWIXLS4_p8We-VIXKKbcfcdoBZ1chbsNTa_pPes2BAmaf7OGS45lR3hNistw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
کل‌کل‌جالب‌مهیار حسن و مریم ماهور برسر بازی پلی‌‌استیشن؛دختریکهPES و FIFA بازه‌اگه‌زن زندگی نیست پس چیه؟! تو یه بازی هفت تا زده مهیار!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27658" target="_blank">📅 19:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27657">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28cfa38cc4.mp4?token=u30dxROjVVOdszJNY_PuqW2z6d04vjtxcHfnX-aOXhS9rJEweBftsFIjQSg0ade3EEmO2DYcczq78jtlI5yb-hTkREvPxmFe5zKg7-j_5dVDQKNYucJS6LRbPzCuZvOKVYLO9BXo1YExF7aOz2eG6X3p9IEHvXXh2cAmN0VRAqPoJ8KlL4Nku9g8sG8yatDGYfWAwLzsXsK_aVhPTcvTPcFZFi6_tcW62E4cHeU6kN5d57f9GLlOrubzIXnP0bRW3Pui6uG1oZSphz1hx81VFLt6YQEmJWOJv5Xz5PkC4qNdIPymVrmaBBZrIDFWdlvZwJLYKb1mlR-w4SZpsEHSY2Jj8Rv0vh34pEp-NtmZokYdg-bQFK-TATlqkQdszffJwWSc4QH4eNVYob2n3pUAbLsY_4j8-xkRCeioMLqD5hdLNICNi1Uaxg9cl2VlSVRSYJgG3tKOH-UAfH3e0YOpvSMfyUPn0Sm2vFP7X-IehdmvSgY2Uz-5mdtM1HpJj0Wuh-GQLcJxAhGR4fWuK0HgJvmWYNYqUrfrpVQ0Bi2f89dKs9aEtX0gMzXtVNA_UCu_7LLajaYauXaFBWI8YHBQXuuYMYMhd290mco3D1ZlhovlQfjPyqnOJJbW4AuFoquPqkHwz6BKuaV0OyIu9criD-nUcpHO7o1Rj7YEIw4ooyE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28cfa38cc4.mp4?token=u30dxROjVVOdszJNY_PuqW2z6d04vjtxcHfnX-aOXhS9rJEweBftsFIjQSg0ade3EEmO2DYcczq78jtlI5yb-hTkREvPxmFe5zKg7-j_5dVDQKNYucJS6LRbPzCuZvOKVYLO9BXo1YExF7aOz2eG6X3p9IEHvXXh2cAmN0VRAqPoJ8KlL4Nku9g8sG8yatDGYfWAwLzsXsK_aVhPTcvTPcFZFi6_tcW62E4cHeU6kN5d57f9GLlOrubzIXnP0bRW3Pui6uG1oZSphz1hx81VFLt6YQEmJWOJv5Xz5PkC4qNdIPymVrmaBBZrIDFWdlvZwJLYKb1mlR-w4SZpsEHSY2Jj8Rv0vh34pEp-NtmZokYdg-bQFK-TATlqkQdszffJwWSc4QH4eNVYob2n3pUAbLsY_4j8-xkRCeioMLqD5hdLNICNi1Uaxg9cl2VlSVRSYJgG3tKOH-UAfH3e0YOpvSMfyUPn0Sm2vFP7X-IehdmvSgY2Uz-5mdtM1HpJj0Wuh-GQLcJxAhGR4fWuK0HgJvmWYNYqUrfrpVQ0Bi2f89dKs9aEtX0gMzXtVNA_UCu_7LLajaYauXaFBWI8YHBQXuuYMYMhd290mco3D1ZlhovlQfjPyqnOJJbW4AuFoquPqkHwz6BKuaV0OyIu9criD-nUcpHO7o1Rj7YEIw4ooyE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تا ساعات آینده دو باشگاه استقلال و پرسپولیس از کیت های جدید خود رونمایی خواهند کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27657" target="_blank">📅 19:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27656">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3EoVr9t72euM_Vfla7wgvYQN4Rma5wEIABHq3ALuV0SyeVtml431BZ7nzi7Q09lNiVqOuUtEs9XKa9LXJi3RrgfmJdpgDG4_lpW7c_b6YNbaZloGRqLd-MoPJECdAgqy9pGb2-exO6DijKrayVYFXTCwC7YKFGs0GYDw_9zPZ4ohQubnTwxNdnp39Sj51ffhtRDDxCbrZYmCk8Hi9bUrkCI2RA2delCA2z9hQt-JSvHlDDvwRCWBsHPaNQc20DO2UvMpEv3osD6bwkwCzxO7jUIrV5XgS5Si41RfiuttxVUdDyxwC-ILxq_bV-cRi5UMilw8m4pwLg8R4HvCo5Z5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
طبق‌اخبار دریافتی رسانه پرشیانا: محمد محبی از دوباشگاه اروپایی آفر رسمی دریافت کرده و اعلام کرده ظرف 72 ساعت‌آینده‌تکلیف باشگاه جدیدش رو مشخص خواهد کرد. حالا اگر با هیچ کدوم از این دو باشگاه‌به‌توافق نرسد احتمال‌اینکه با استقلال قرارداد امضا کند و قرضی راهی…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27656" target="_blank">📅 19:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27655">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plhsLFAfvMDp9ksoxXsHl3hiFym-uI4q0-AkBd6lyvTO02yACtcUDzaA83XZI3jJUc3RlTJ2H_DTqEyMuzSQTlacKfDLdzmt_xB3QGnZ3Rxt3QaaIw0N_Y6IspySO4iYSpUXZr-Nds1Ye9IVGMAV4-nGt0mMdbrtRn4Rbg_nCMRoWuFGSoT65nKjF7gdcWLFot_CxREDe2xbdVCtxD_esoBIKakUTX1JmvklP9WO8aFjOsv2gAVSM0sxyOEfSr5XOFkkp5zLKLpwaXN6BQgBUSyWG8SBn9qNNsOSrdh2vIXlEJ6_SHBmPF0n-N5_K1nKoJLLxjj874egXx_ScnHmyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛بانک‌شهر قراره روزشنبه‌بودجه200 میلیاردی دراختیار مدیریت تیم پرسپولیس قراربدهد تا اقدامات لازم رو برای جذب محمد قربانی ستاره الوحده انجام بدهند. اگر این بودجه تزریق شود قربانی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27655" target="_blank">📅 19:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27654">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPxB1IlmOLn3dKAJYUVskOc7IlZpa8BlELr3iYs4r2nYYX-zFOO7UpQDM3-XM6mzTFwxkmRCTwZhyCZBLtU1TFU3l7CLyBtZx6ccfDqXLURuA3chX26PSL9u7e95cqctppjzW01zbhf6stEI_Q2CQ0W9vRzCelkm_5rBKDXi8yS-gE5a1v-E96TP_TGy3TGkwA24nNKIDXfYXmRrjRqL-GS1ELOQmNo1Pi42aSxh_hR3iSJ0J_b_og6tHcoGvOLU952FweE24YQFri-IO7kMEVSwYKcthI_r6rjlOY_5vJTYunIBsDq967bffycShwW3njaHG9t8Kw73pRWlA28Frg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
10 ابزار خفن‌وجدید هوش مصنوعی که سرعت تولید محتوا برای اینستاگرام رو بسیار بیشتر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27654" target="_blank">📅 19:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27652">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYmYYvqmy-n5WLsd5jXUPjJCNc_RU9_2dRebHSbzOM72IpXDCW3_fDzcjnhXgkazedopZJpOnkoRAaIQY8wF3Q21bg3y5qz978uHTS2bpUnFOGDXfIZbfz6Dtk8ABQsmNRZcEVGtjp_3KHoT-hXydh8osqToJ1TBLWLpt_94t-PA9_TYdSAtSXWcnZpQ0cJd5ZeCbwGsjUfd9PoiPcZIJCHIcHJP80enTo4wC8B1jTVK7XdzhovX9rIEvZnwvONwb3lrutD82DXqT_d8_0XD7kRgZA1L2lR7PFNcBfAvzL-t-1KdXgD_izuMDzL_6iWixWcG7K8ux1Q39z9gGuzgxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سزار لوئیز مرلو:منچسترسیتی‌پیشنهادی 120 میلیون یورویی به چلسی برای جذب انزو فرناندز ارائه کرده! انزو مارسکا اصرار زیادی داره که این بازیکن رو به هر قیمتی به خدمت بگیره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27652" target="_blank">📅 18:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27651">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nunxVFepI1rJeysM41JoCNxcpZH1YdyrDadHEcsZLU2GqYFjV-JDlXubqIgP_soF8iis1W8AS6kopJu5NbuR-StT_fjYVjHtqa_Z7EGTcLgvPr6w5Q35iBjkn9HLUOfTf1LIev8AIPvpo_0IKAPdADrjOL2GewraouUGWl3DEqglkk4RSaavXUVdOgo-hdSbNLMWCXLh2G3TP1doATP1G1d1p6upN_fjAY1X46HlqsWKZ8cDrcAT9dDAW6nlNtm7or9N5pI09CezHP6-N-JGQsozlwx8Zu9jomhDCzSPGaWMOf2YgwJgYhxYcK5d-jwT8jNetUcfm0dSe5fg5WcJjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکردخیره‌کننده لوئیز انریکه درپاری سن ژرمن: سه قهرمانی لوشامپیونهه، سه قهرمانی جام حذفی، یک قهرمانی سوپرکاپ فرانسه، دو قهرمانی لیگ قهرمانان اروپا، دو قهرمانی سوپرکاپ اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27651" target="_blank">📅 18:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27650">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKlSGiy2UnZOOUXISQvkJYC26YtBATr8CNCba1gFU5QfcSTUO8urgVnwn2BAAbACRE6EcU05GOVRahKi5h9Yyx8NDI0cE9JlBSom0gofQulKBFM9Fd9Hgbj8wWouTqEuk7iTrBKe95uox5_Fz3dYozyg8qRB5jaQkvxirqj94fvPfGRKqFNYR02WVfhWoJKx6CKMyL52gJHrS__3FLuy5gLjznC1UY60ojiFxlw5O_vkYVbHVJK71eKagAlkOtI-2rN5o3tZuj3QrG_AQ8pt9dvc3uwc0Dl9ARo4UAN5fal3uPhH4DjadazOOK_1pE2UO_9Vtf-RPqjc50QIukkQvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرکت یوسف جامه به‌عنوان اسپانسر فصل جدید باشگاه پرسپولیس انتخاب شد. طبق توافقات انجام شده قرار شده این شرکت در سه مرحله 550 میلیاردتومان‌به‌حساب باشگاه‌پرسپولیس واریز کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27650" target="_blank">📅 17:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27649">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbCn0QA1C64jEgibGKZskpAmI59gSJIbjxIgVKDyBxyW6m07hH3xjnME8gL_FiFQn0IkHO3K3it9RtBWJ-1Lp0hMbn2xv3WZb4-t5Kq5-9OYE6T4GLlKSq8S4eMyyASGLlszrHyudyK4YfY_pGwG_-hOCwB4gbl5sm3gaD26uCAUO0BEWfzvzWCw2lAydGNYgiyfiqPsaCaj0N82fx_Ao2R93mCgkbq1wiXQkfuyiMWmgvsI7qywPgQcd_byGTBy1f0s4ipccVhzwVh1H9-8ufJu9g3DXmJxYPdOJ7zbmFcHtUOMZxzGJS1Um9ay6mLLSc5UwDbor5Rm2YYboQTyEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
دوست دختر هکتور فورت ستاره 19 ساله  باشگاه بارسلونا در ورزشگاه سانتیاگو برنابئو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27649" target="_blank">📅 17:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27648">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIvA8axNGsL2low-J3PWPbkLJt_xU3F5W8IjlAPpkNOs2eCXi175R6VOQRmfXzJVtpTp7yIKUhMfUJeMLr3LTP6BQ-QNBXBuxcLrcHClshycBz7Y8tKBsioMizHKQIexoXAAzrEc49ClHPF2fmJhZyymL79w2t5uSZ0U6q9rVQyvYGb99o_2uVBYG7syiACXhAVE9NFct5Z8KiVtjBEAmFogJFW9QMCLzSVU9-3M7l2bS-2FFtjtmUxIjWH3edXvcZV9tdpZ4h-Qx8FO1AiX6ZKM0BItRByPGvJWccV0e2rvt72rbWwgjF69jFNFRDrfRM2W8cRFUobAYxMrCqTuIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ محمد قربانی صبح امروز از طریق نماینده‌رسمی‌خود به‌مدیریت‌باشگاه پرسپولیس اعلام کرده درصورتیکه تاروزشنبه پیش‌رو رضایت‌نامه‌ام رو از الوحده امارات بگیرید قیدتوافق‌شخصی با تراکتور رو میزنم با پرسپولیس قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27648" target="_blank">📅 17:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27647">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kED5ne8HS5FN9LOUySBCY2i7APzmlOmKZ3M07tpfk_FuFxTX_8ccd7cOz6k_0VTPO-_5W5Z9g6B97zhQbJCemniVPMLO05c8lZhs0fD8ATXIgnarZwYdpHhadDtYGc-RYO39IiROjQX3cAZiIC99ojQt-70F_asj9TGQxCo6aoziWCJ1kNhaXyYuoCZeSLWYmR06N_vFwR7JOC99OsgZm7Wmhu9lfYtYXMT3h5NAp0MpVrAOscKEKrIvah0XCrpExpJ0s2PHFmBIcOAfj2fdUXOZZnXI14sHbI3NzyJG3AOlHNhXav0EneLmdYFEY9pTqBipRQbg_9DCmIkcbxUu-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرد پرافتخار کروات روی نیمکت امارات؛ زلاتکو دالیچ سرمربی‌سابق تیم ملی کرواسی با قراردادی سه ساله هدایت تیم ملی امارات را بر عهده گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27647" target="_blank">📅 16:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27646">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwGVFlqc3mzQgqZb-nswkl6z2vX8S7Jc1WoppfVsGc0opHHBQkRfN9ONhK4kwlTb5TNcw4jzMg06HkB7b0JN-kZjq0r6Zz9Kge8hGHeyxC_Rs6qgoz0ZHvi0APrJ4lVVXAKaaobUzDF25yaYlYhvg2lY81qV-HNoPCnQcw5z_5UY16a7cTDxBzpU7eNfhdxo96QZ0IQkFykcAa06rz5N_FoM51nXOw4Ais_CbJaICSVq5NJmCiXLhzBerULZ5qBqCVuGnXmFf0fRZggrqa4vGL6y2KLD5GfyyjA9JWraAJIVdkHCF-IIsNhQf6ZHPXUaXlZ4mCXqsyuNL9SySQLrag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال تاساعات‌آینده 25 هزار دلار به حساب جوئل کوجو واریز خواهد کرد و پرونده او نیز بسته خواهد شد. همچنین سهراب بختیاری‌زاده بخاطراینکه نازون به‌فیفا شکایت نکنه به‌مدیریت استقلال گفته مشکلی برای بازگشت نازون به جمع آبی‌ها…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27646" target="_blank">📅 16:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27645">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HX_YwE3yrrlqhcOD91USlV_sMG7QMDnnTtDihoF2sCSyblJXu-ImiIRVvkIXFm5H3uVW_AWUgB6YvDGfMTyaTHrwsV5stymR864NCIgcw3dCzadgMorkYDSa4_xAvwaX2LcEyEbmQcINCNj8vydheDf6-Pv0Kn1VBAdvvt-mw4JS5gMhBvZcz6kayPZX1DhS2xEyTyx3-sz-e9Y27YIZroKihBML5u02TtoJiucxEt74ZBIGjNPGBo7FKmRJaacil8ypkbNyITGHzlL4lySAe0XkMFS-oh_IHH6Amh17SpO2UGdVA2khocnZgptf5pUoVgdrGloyGcPD1IRwebITvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی‌پرشیانا #فوری؛ کسری طاهری ستاره 19 ساله‌نساجی‌دقایقی‌قبل رسما قرارداد خود را با طلایی‌پوشان زاینده‌رود امضا کرد و به سپاهان پیوست. قرارداد 5 ساله مشروط امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27645" target="_blank">📅 16:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27644">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilBuzA7wGlJYbPrK8OPNpVjDF4Y-v4miOPFSYj2E7V6P7bc7f3FOmrBM3SqiIntaokK_7T4UKce7eipAt67k2If9tzhx88VVECKiMwCWpWyVaf7Qgk1F8Rh9Fh_n2p3FcWo2DHsQPOlcfNXNbscVFp7gLmmo6bGE-doY6wqEAKBh3Oe9N8VeOt6NA0cDZelRsubVBh-V7DdV0crvCA8f5ALC92g8iWOnJUt54A5xhDAFTpKvRxqEl0c83pAJl0yxKc_zU2cZ7Pzjm5MaQL1fN4Y0vq-bJAE84UnXBadgbbDuJowidOo28GxS99UxkxYguIXHZsvZ3UHHD-tq2RaGdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود رضا بابایی ملقب به "بچه" با لابی‌هایی که داشت نذاشت باشگاه‌های ذوب آهن، مس، پیکان و صنعت‌نفت با نکونام قرارداد ببندند اما نمیدونست که زنوزی و حجت کریمی به یه ورشون هم حسابش نمیکنند و تو جلسه یه ساعته با جواد نکونام بستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27644" target="_blank">📅 15:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27643">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oU3nGvaTwurm2bKK94BEKKShQTP9ednKVierLWNpc7lgAzwrkRwZzMQpR0AEEQXHM1eVrt0P9xGoZgA1fIVLaOAC14tElMICAnUSgra9WtS6uncVeMp6zn5ucjFSquMSJ2cXNdDBMbR4jok3l1Z3qOf-M1JMnXJeI9p2Ea6Cn1-6ji6aTjpoK-Jm1Ru6ZcEMskeP1eDEBRZHDMRY92o9yd2O2xns9aJz23pYuedzSazvRrqi-DYGygKSLZTTuUMdfUxAww9QVJsz8qTa6-vwxEuTFgu_VvwpOyTW7-SvnGSG3hbXLuwrUHqyookLF-QiGXarAbcWqWLKxT3o8r0GJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
تموم رسانه ها؛ خبر از رونمایی باشگاه بارسلونا از رودری ظرف 72 ساعت آینده میدهند.
‼️
تموم توافقات بین سه‌طرف انجام شده و انتشار خبر پیوستن رودری به بارسلونا باقی مونده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27643" target="_blank">📅 15:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27641">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttbZQzajTxn9ONxx4ZDO3YuDXtQx-rctxKBMBnSVOEBwlXH1RdryVglvAUlxARIzImMXGUEAGHvx4madpOyshJg-9DcFAYjCqeljM_WGr-Q3u-cuysVtStwTu-yzy5T1oSgDdzOz-A_V1JyAzPSS30NtSFZ-V_iQfxI2SBfLNoUqvGV8gfYPJzN57y1HJ_jfZX4cgiZUSivaQ684jn_heiv9wLgIeV8U2aZmiln30ykCnAw3e6yWSzkf9A6bNEy0m6QiTlDkFCdV7_zV3nF6eQOHjbR184FYY3mEExUFXkqImeoIEC26UgRwqu4gkACBRwOkEK0SGWVu-X7yKCm1Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد وینیسیوس‌جونیور، عثمان‌دمبله، رافینیا دیاز و کواراتسخلیا در بهترین فصل فوتبالیشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27641" target="_blank">📅 15:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27640">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXqnXB1Xc4LK9Xlrld89_pxzE5Z1h-J4CGpdL13cMeldCVr5fFGlCAfz584X0SW2ckmdAl22g7T6_NuDQEi-Ol4d4P0t99b0rK0Z_VwmwV_Dm9ak8x1hem5OZkEoSLFb96tVLALAq6_g-o5vpozFxRHH62fntYPOp3in4dpQySdzkztmeg49Zy-l22o9qxCzcFdRAPPToHczdOcQjsAuM6OMa77lMgQ5e7tV7qYyb9q9JydjN6DVVpk7jP9CcMmseXbwQX13AdIk2C_1AoJktrEO62rYAK4wWZDUMLesu-5CHlLtg5bk3UWTwstjeRACr2nkapGUZ54zAGbcEh5S_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🔵
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ طبق اطلاعات به‌ دست آمده؛ باشگاه تراکتور در روزهای اخیر تلاش‌زیادی‌کرد تا محمد محبی ستاره تیم ملی ایران که بازیکن آزاد است رو به خدمت بگیره و از مدیربرنامه‌های‌او که رابطه اش با زنوزی خوب شده آفرمالی بسیار بالایی رو به او داد که…</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27640" target="_blank">📅 14:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27639">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QC2LIvJxeB9dYElNnecPEz1CJC8fodLPMSoPBYPmgnkI2TfHGcj_2tFqOJb2YAME9B6emSNJ0wHkWs0DgN6qEpPb-6c_-gLulfn0TElEgzu4KdAM864BrozpUqm53L6hrFdchqF3kwMfzGy4WFnciACP_m7Uh13w0FlRH9DGHXnagRQeqhuyHZQxqlp5tgjH7j2d-F19IMDmy4jibQ_LNQFvH7zo8H0W6GHWSolr_x-wobsgzo-RaVPjbNmxGKy9XSRxd9vq0owo_9FoSw6uNoj2iQq-qTpGgPEFPR0ilA3-6DHIZ6YUyLMvkiAAw6aLze2zBJ1HscofA56Zy4eF8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ بعداز حرفای‌دیشب تاج برای اهدای جام قهرمانی فصل گذشته به باشگاه استقلال؛ مدیران دو باشگاه‌سپاهان و تراکتور به فدراسیون اعلام کرده اند یک‌تورنمنت سه‌جانبه برای تعیین قهرمان برگزار کنند. به‌اینصورت‌که تراکتور - سپاهان به مصاف هم برند و برنده اون‌بازی…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27639" target="_blank">📅 14:36 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27638">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nve_9u-phaLuo_iYz0XGQB83RbDktoT5VATXMtkPbUGDnyEAJe6xhlHcxRSSteoTQNcvkxE5KprcvbSyTJbOZdmBON3-LPymJ5Qu0TA1A7ykyTeEw86f82vlF2dSuIaSrJJYlkisvuz0M7z7GEXtkb8fn1t7grAr0dB8cYJIpN1IMceHPYOrp361-OAZPuPNMzHvAy_igkWxBCLmUBfhu7fE2jpyC3jXhXjz75uTG9VlRhnGfUi1DzWvSUwCzWdg9_Xli1oLfGDs6XCUmTsv7EKhTjLgqTwSJfgEIdBeh3BpKX84XrPzZjT_FUS1BEkwzMeh6vMao8-5POToVpxnfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛بانک‌شهر قراره روزشنبه‌بودجه200 میلیاردی دراختیار مدیریت تیم پرسپولیس قراربدهد تا اقدامات لازم رو برای جذب محمد قربانی ستاره الوحده انجام بدهند. اگر این بودجه تزریق شود قربانی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27638" target="_blank">📅 13:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27637">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1I6jWuCC0sqdxXsgXvxehIlibAOwrMzDgs5w29UtEXxRLKroacbChuQ66aGExdJeUG6xPHQi8xSaXzj5yyHO9xPMqLqwa9mGGU0gDoab9lTtEc5cJIcbH7lDxt1qfBWK9K_6xcRgG3l1frSSOzgsNSA4MjLjJ6rBF78e_LWevDHH_Jwpu6i6CcvjCDl4UZWc7H4BtPWbhKdBNrRbbSxm2pAlbbjk3zvRgGAL9S9XvFK4F_MeTFlBMWftkHe2kC-KdsSGYS0HeMo9lRaoGBqJoW3N6ztDM87ci7k06qHqRkJ4HH_-aUBTecMW3I6W3939-75T-FiUES2UPoHuedqow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول مدافع 24 ساله منچسترسیتی قراردادش‌روتاسال 2032 تمدید کرد. سیتیزن ها اعلام‌کرده‌‌اند که هر باشگاهی یوشکو رو میخواهد باید 80 میلیون یورو به ما پرداخت کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27637" target="_blank">📅 13:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27636">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e78NsNgIoBcotPbkaHyYen8lFWcjly_ziXFcbLkWmKwJanRamjKZvRcXES-qCLqzmBXzUEWNFfIlNsQHE3iEv7aby_ZAbhXtWrBl0efn5zzeY_hQuY61uios633TgHVTDELU7NJzPKO9wkZmePv6D73iYUvjDOZ4Kq3il2zcu0rxFjqq3QUmdR3cVemmqe5oYNKCDP__tGQUSKSE_fVi12LxByTMjerIYU6GngERBv10MceaLUoYUCWeIAgMHyY49npRTxDnXd7pOjqLSdWqbuUCtwr7O9j6gqDapI0_wz31C4Z2V6XP6Q-mSwG2e7zREiybF94FxMmPuNVYMOyVHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درحالی باشگاه استقلال تمام کارهای اداری مربوط‌به‌اومدن خواکین گیل به ایران رو انجام داده بود و حتی برای ایشون بلیط تهیه کرده بود شب گذشته‌ناگهان به باشگاه پیغام میده و میگه تا زمانیکه آرامش کامل درمنطقه‌شکل‌نگیره به ایران نمیاد. بدین ترتیب حضور…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27636" target="_blank">📅 13:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27634">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428e46d461.mp4?token=WOLY5xBo6j6Lifld7stGZBNcDWU8UxzDRu1hN6TLyqEgvHxCwk9g4IQSwr9VYa2rwWv3oL0VgM0uaHgvosAolpVYzaGynx-J9fCD4Yyh7qBbCxzCzLBincHa6KxUJg5gN35o7wcmyzYrYxfgSlC5Opx84xMmqFQOym5Cv9JSX_rAboX4vV1V-HWNDJk3ODqJ21ZXub44k5pDPiX6QiKtRRg7PvwNUcf9ILOYw3uyt94dv6peCPO5P79or0VwYhu2fecpO6YwiBzGw4OaT29zFS7DqaF1U3A6D-hDJQxI1zMcVNxk6kRKPC5bOvEOSlBKllLLXRYsIM3tYDUZCklUuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428e46d461.mp4?token=WOLY5xBo6j6Lifld7stGZBNcDWU8UxzDRu1hN6TLyqEgvHxCwk9g4IQSwr9VYa2rwWv3oL0VgM0uaHgvosAolpVYzaGynx-J9fCD4Yyh7qBbCxzCzLBincHa6KxUJg5gN35o7wcmyzYrYxfgSlC5Opx84xMmqFQOym5Cv9JSX_rAboX4vV1V-HWNDJk3ODqJ21ZXub44k5pDPiX6QiKtRRg7PvwNUcf9ILOYw3uyt94dv6peCPO5P79or0VwYhu2fecpO6YwiBzGw4OaT29zFS7DqaF1U3A6D-hDJQxI1zMcVNxk6kRKPC5bOvEOSlBKllLLXRYsIM3tYDUZCklUuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
عملکردخیره‌کننده لوئیز انریکه درپاری سن ژرمن: سه قهرمانی لوشامپیونهه، سه قهرمانی جام حذفی، یک قهرمانی سوپرکاپ فرانسه، دو قهرمانی لیگ قهرمانان اروپا، دو قهرمانی سوپرکاپ اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27634" target="_blank">📅 13:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27633">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6EyeFRAWat9nNQ_As-J5YH6_bqKlylFTn5JqscR5R8qSA2iG26oHRWeyQdBTh0WxgN3NsNsWet7t4w-tNdhjqsKLy-XzIpIAn1MbAa9hS4hsOwzyQxUON30CG1OYBm9BSUvxE0dkY6wKKdO2rvY7mS8ZPf-DWrIWCp7q6DQL5favcdQKe5YNcxj7avI9Fy9JC6k31w5HyzedpMhP1ilpMjhGkBRU8OR1sESkKXc75Quv2lv9w_LWRb72Zi5cOM6ZsXpRE_d_E4_3_q9hN7Y_-nQqeDF9m8iuL1MUtH6n1kkLQJuNy4TcOxbkOnnl47Bw2DjgxtLIs3jLqiqhhNU-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رونمایی‌از کیت‌اول تراکتور در فصل جدید رقابت های لیگ برتر ایران به سبک باشگاه‌های اروپایی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27633" target="_blank">📅 12:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27632">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0ry3vbYErkwkVBMoyMEwM4STTVPVj6tlF5IPRI6pT137OYzMNsWOSBTBuqzhse8Lz1l0dO6tlczUvgWB5gpjh1mKaJeXMVomtlCz61V6qhED6W55T3iVEwlRpaVRb5rNI3ZjBFk-TJ6D80_2TIWnCzoChYty0J-sF2poyc6stnEjvn33CsIUkEbjPekzfN-ZQeeoo40xaPQ5PVr42GjzLgJMl6wxwvkAjXLKOoUsUdlpiynrJatbfa6GLRaQdrN9U6hXncEex79bYkvkdtWX71ibX8pl1DflYgr0ZqKMKdAYi9iyAYL38eYOckkLjWp0GQtfDQMpLIR-Y1HNf-JKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تا ساعات آینده دو باشگاه استقلال و پرسپولیس از کیت های جدید خود رونمایی خواهند کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27632" target="_blank">📅 12:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27631">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVLE7msPjUEvt7eCQ0zqfUA7yPLWgiLuKbEmthqa2TGiyw1jhrkMa-bLWdtDp1VyhXeWQobbIn4fYqP4B4oi3399Fm2BwU3INyogsw5UlSjUVfrreGhWXqvAcX4dbO-SFxRyByOzh16X7gIP_-vPAub11W9Xhpb8XtD8JKmhT3pd4542ogvIWhd7N_p3yhd-63CVk6Kpz1QnAOUONy9sBPlPnCemND1sS7HRWAlaaPqgtxWXizpfxoBq2kIU_JfaaNBQOxMJKlIq437ihHR840zrCsK75ILGqp5rhHk_WxtiZ6zRN1h0intbK2_RuMdaclpDSdF4C9uT0udnLBeteg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال در روزهای‌اخیرمذاکرات مثبتی و فشرده ای با مسعود محبی مدافع میانی22ساله خیبر خرم آباد انجام داده و قصد داره با او قراردادی بلند مدت امضا کنه و نیم فصل به جمع آبی پوشان پایتخت اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27631" target="_blank">📅 12:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27630">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgk3wPuSGF_XXakznDkMaR6nGSGzYN8f_RaGSMfC-DSdztDxSVOnOn-yjzYJUVBLT9f1tHruscqrewNaE7JjABl7hxjQsWDCl6_MHpHrKQFBuatedbincXZzOlukQp85L6px313-SibtoYHvQJdWoR8_0lXc1xc-5Vn2uEH22ozI1As2QXXY7fkbIhs7LVPcYgjQTnGdlNv83hT9Slei2yeaivxHqKgG9sA8KLOOV4pJasxfih_s6ZPqZVEr-hNvF5fu1rXzUfWemwq6Xz8Q7uIsP8x6HkrpoU8ETO-OS537V18rJbnIH1r4FsGLqb_43M-Sfqo89CqwOa5ArrcixA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مالک باشگاه خیبر خرم آباد؛ پیوستن مسعود محبی مدافع‌میانی22ساله این تیم به باشگاه روسی منتفی شده‌است و بزودی به تمرینات خیبر باز خواهد گشت. رضایت نامه محبی 70 میلیارد تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27630" target="_blank">📅 11:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27629">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-48_SNX15KUXA6hGNqPD-UWQrM_WGikHXlq_sLORvMuozdWtaIpBzbEpb7rqwbHFUg_haEVMxcL8kKb2MvkeSOSa1idmWRuYaSwZ1c2FLQsQGQkdA9ZuKT2smdKcChcNOmaQol0Z3DoG8jeJQePajhdZ6dCDS3mgU_CZJzRH7SM-SQlRjua4uec4XWhf_89svLemVR2uhcKaRDv3JHoi9Hi6AMNpevN6l9NPpvxJ32plj48CYnb9YRyQhM1dE32NWb3Aweo2U5eoqVGJ8ftlfqYGCIniEYs54ddi4kAh5MG95qAQlegzJxZR_KIFomCCMsYJrFhEFikQixuI1cYNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی‌پرشیانا #فوری؛ کسری طاهری ستاره 19 ساله‌نساجی‌دقایقی‌قبل رسما قرارداد خود را با طلایی‌پوشان زاینده‌رود امضا کرد و به سپاهان پیوست. قرارداد 5 ساله مشروط امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27629" target="_blank">📅 11:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27628">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9P_1yVsed7QDPX7AFGaf83O1wnlb_VMizXkkRR32XdJ5hRSFDUVZnJQlpQ55-2bxSTsbLrcnjWpVsIPH6gwq4U-aANbWfnsAzqHjBnR6a_sDdg1Blig-TD1jv-ru2CEb1kJELs6VBWfk7DHb1JjRp6RpPJHLOT9_kUnuDbqSofpgxKYrB-AL7kMaGJ5-mo_3vZ1hi3cJw9DRUb_jqxpA4faldHqmuP0_wK2DaF7S9-sntKKoKvVJ6ZD3yw0Z_IRgC-o2AjDcWOTohKbfgTUzQRg0vwEbi984EICGb8UrqPiQmem3giaVzHEv9IYBRIqkF2QP8L7RQ3qSI7Ey8uWBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کوپا آمریکا هر چهار سال یکبار
شد
؛ با اعلام کونمبول، جام ملتهای آمریکای جنوبی به روال قبلی خود بازگشته و به جای هر 2 سال، هر 4 سال یکبار برگزار خواهد شد؛ دوره بعدی سال 2028
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27628" target="_blank">📅 11:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27626">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGE2c-QwLJK2tecajS5QOw6fmqp_BxzzUx5I3gnchrhx77UEpqTDV5v_lgf3zA_QycOc0Vc17Ot1csFGzDQjYzyBm9dxTBG6NoHrOjyf9JQgkegNqT4xv6WlW3guQ8DJuuXV4vznWnOAmrnKOnu7pA4rsaCjfxKvo8RPePFa1u41UqYggPqDUPb7JVlux5VqFSQkA-bNJNmSXY-0nRsP-9PIbWZX_Oo1x9-0lPwoCZBOsKhsHi_7Tms1hk9_qu_RoTEdu6xSRVFUEnaVSyzpGwk9QLSAFCuW_8T-MMbd5RzAaGbZTy8ApNvnTnKsvsuhcwBmpxi1iPiv0e1G6UK3zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای‌اخیر گفتیم؛ دنیل گرا در لیست مازاد مهدی تارتار قرار گرفته و مدیریت باشگاه پرسپولیس در تلاشه ظرف 48 ساعت آینده توافقی با پرداخت مبلغی با این بازیکن فسخ کنه. توجه داشته باشید اگه رضاییان تا قبل از فسخ گرا با تیمی نبندد احتمال بازگشت او به…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27626" target="_blank">📅 11:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27625">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kD4Ge3KIhfNAUZtP0Gp1iqxegYVmtg0mFC-RA6AuQGRtfk-x9ERmNAvMoC3WkczWnEtzXuKM-h-swQuiW2vmBrDf-1OXHblxSdGQvbDCcCp0veyIcPUfHwolykgFrOVfMkV6O9FC8Y7zFZmCfUaPRXO0fMBIv8NtLzP9W97ya-eCPAKxvRaUpB7-yT3zcgqPCg0NaBt3t2xyofCB56ZIw6vUejswDWAndUEtSsYOuL3i_om489MEV8hSTAD_yk6gVaipv4W1Xj3Ur3awRWA_weYsa2rIcxos33BUz32KuvlZDzvEwwGBGK1k_x6ZJZfAKrXeiGDj5Kea_XHIwc0qtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خواکین گیل مربی اسپانیایی جدید تیم استقلال فرداظهر برای‌ عقدقرارداد و رونمایی باپیراهن آبی‌ها وارد تهران‌خواهدشد. خواکین‌اسپانیایی دستیار دوم بختیاری‌زاده و مربی تمرین‌دهنده آبی‌ها خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27625" target="_blank">📅 10:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27624">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‼️
اخیرا دانشجویان رشته علوم ورزشی دانشگاه سنندج به مناسب فارغ التحصیلی این ویدیو زیبا رو ساختن و درپیج‌دانشگاه‌منتشر شد امابلافاصله چنان فشاری به مسئولین دانشگاه از سوی نهادهای امنیتی وارد شد که مجبور به حذف این ویدیو زیبا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27624" target="_blank">📅 10:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27623">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ae0dbca9.mp4?token=qi95m_Sf1cusm5upKr5WT6kMW0Cf7B6YgMqcD92BQJrImuCwLmMdYcuyHRLFAsCvEz9J96PaTw_E_hapiUklqD7EKm9S5-40D8_lKLOOOqf4KzddbstDQVJJ7qN5crO-aJNaZC7nquRBrL8wDak68aQu9ncm3TxBD1n7QeJg7ufTxqwLdq6CqXBBqM_jWgQfGI1MCh6unUtHdMGkqhfeRxljIjj1yVWPhuKUKSzIbOH5Ucn7k0Yo9gNXdCAOvjIcbjKPVRg-vwb4ayWGJQK8_jtkTgEwo_8YziPc0Nc9NmpqjIZ7JtUmrNgLh3TUrZ2wi9KT84SVlX_Vfj_-VaStcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ae0dbca9.mp4?token=qi95m_Sf1cusm5upKr5WT6kMW0Cf7B6YgMqcD92BQJrImuCwLmMdYcuyHRLFAsCvEz9J96PaTw_E_hapiUklqD7EKm9S5-40D8_lKLOOOqf4KzddbstDQVJJ7qN5crO-aJNaZC7nquRBrL8wDak68aQu9ncm3TxBD1n7QeJg7ufTxqwLdq6CqXBBqM_jWgQfGI1MCh6unUtHdMGkqhfeRxljIjj1yVWPhuKUKSzIbOH5Ucn7k0Yo9gNXdCAOvjIcbjKPVRg-vwb4ayWGJQK8_jtkTgEwo_8YziPc0Nc9NmpqjIZ7JtUmrNgLh3TUrZ2wi9KT84SVlX_Vfj_-VaStcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
پیام لیونل مسی به مناسبت درگذشت پدرش: بابای عزیزم راستش باورم‌ نمیشه که دیگه پیشمون نیستی. درواقع من‌نمیخوام باور کنم که تو رو دیگه ندارم. لطفا از اون بالاها مراقب خودم و خانواده‌ام باش. مراقب نوه‌هات باش که راه پدرشون رو برند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/27623" target="_blank">📅 10:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27622">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41aeeb5537.mp4?token=BP5uTHuZrzaAUXd-UGEfFZjvmt5gUg3qjTbvSy4lbaiy9PVZzI_ySJl0fCrNrCbK34v4q3H8dMR9Vb7lL2_bpBvvc05djpWb99i4lOM6SgsDzHzl1m2DARYvQr3sZ05RJ-LOGgRCogpVhhsGRebm4OKzE9Q_UM_0ejnFjduXBfOyiyWNQx5oUi2V_d0i1eWZX6Zn37ypxosLMNDkJdTh_6PxA9RfiINFqFXvfAUVxetgdYrBXOZwXJrK3SRT--70lWceDhkamkWOktMOrl3uAtTQ7jzVyWwYuS0BCROH9bQ6IXWQLM2xj4MShAqxn-03ZIepnYohyr8dEn167HXU7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41aeeb5537.mp4?token=BP5uTHuZrzaAUXd-UGEfFZjvmt5gUg3qjTbvSy4lbaiy9PVZzI_ySJl0fCrNrCbK34v4q3H8dMR9Vb7lL2_bpBvvc05djpWb99i4lOM6SgsDzHzl1m2DARYvQr3sZ05RJ-LOGgRCogpVhhsGRebm4OKzE9Q_UM_0ejnFjduXBfOyiyWNQx5oUi2V_d0i1eWZX6Zn37ypxosLMNDkJdTh_6PxA9RfiINFqFXvfAUVxetgdYrBXOZwXJrK3SRT--70lWceDhkamkWOktMOrl3uAtTQ7jzVyWwYuS0BCROH9bQ6IXWQLM2xj4MShAqxn-03ZIepnYohyr8dEn167HXU7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
#تقویم
؛ 9 سال پیش در چنین روزی؛
در سوپرجام‌اسپانیا، کریس رونالدو بعنوان یار تعویضی برای رئال‌مادرید به‌زمین اومد و این کل استثنایی رو به بارسا زد و زمینه ساز قهرمانی کهگشانی‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/27622" target="_blank">📅 09:36 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27621">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAiyKprwuSDQ3Uu46ksdoLdu6pgTG3uRrcGzF9L4jvQyWXYg5SxA1eIVeZki2yogXyZw4WhtOGVska8QGxT6hdL1Vp09o-0JOOj8mR_ikM8G8iKO-L60cr8iumvM4Ntm1ewt2f0x2CELU8eCUKpvKPohGTeTFoDrp5jpCnTffyBcZfQsArfWYTNOj3AQ3irdbGUQjuc9SNMjr1US6JUGXEvjX58RkVlbn5j8pQt-l47BPq08BzCfEAT_581_VAZaO5NLpDqEziYiR9NWrJN1j_mkI5Ta9p8xUKRRfV0hgLkY2sHeobc9f1KANdrfjfuNJ8Os_CUCiOYOCVzv28j-8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ پیرو خبر شب گذشته پرشیانا؛ امروز صبح مدیریت‌ باشگاه‌استقلال 50 هزار دلار به آلمدین زیلیکیچ بوسنیایی روپرداخت کرد و پرونده‌او قبل از شکایت در فیفا بسته شد. مورد بعدیم طلب 25 هزار دلاری جوئل کوجو هست که‌طبق‌گفته مدیریت آبی‌ها فردا پرداخت‌میشه. باساپینتو،…</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/27621" target="_blank">📅 02:08 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
