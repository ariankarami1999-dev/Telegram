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
<img src="https://cdn4.telesco.pe/file/tKjgkr8ZBMbrIiHqtyU0w0aT8KExDs-KZueiyBkT5db9_dETSNOJO1lyyTMx0rqG5trob9VxbIfHQHNp_82x-HjZIIOfkLIDOp5VVovkZ0Tdz8Yv_w50K5yexnz9amaDQsBqhxCb7pTsgEzTho_sUQHyl1saUEzUYkMYuBcf-dDBIWPTHl8wsMy-Nedjgemk3ToxSGTgUD3rxTX5fHjE4ygUIzwKVHnnWAWe_N-GAV2GlZ7QT2K05fWAEsO8cYrG_tJVsgDkW-6q32Hsd97xdeZYtlz9_8o-TZl5y3uUirnYa8BoO1bUr-CWQYyX4qppfG_EC1yFjeCWFfkHoCPQxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 18:44:52</div>
<hr>

<div class="tg-post" id="msg-150056">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فوری/هم اکنون گزارش ها از اعزام ناگهانی گروهی جدید از جنگنده های پیشرفته F22 آمریکایی به سمت خاورمیانه،
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/150056" target="_blank">📅 18:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150055">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ترامپ: ایران به شدت در حال شکست است و به زودی از بین خواهد رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/150055" target="_blank">📅 18:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150054">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c82cd4c9.mp4?token=SJRDASObdDdk8_uiaNTVd3AZQiFYHGEMg5VASzOdf9EBs--bI1vDf84fKTE-PtkqFz29GY9IUg9XP0lZjRVMAhBUaf7fmSWw0Xp6bF2BzOGYYmIqBFfr3hv9cDzj2RgzDcQr8sme14eSdp5RgFnCJVyWC9td6lG0tLzhVoxZgjjeDzp1lgTJCnFPYRCpt_mXqJS6w4aI8S4Gs94-vEc6KDQsUc6eU1yq1cJ7XBbnvh0G1ocZ35xoQ3mOFy5JGJd28rKGv7ZbEf8-MExmLrBGnX7T0eoa2c9-Cl8K1eXFntpGjegBUEp8jW5WnIlYry47Sn9j87JZ7LP7TFfHNrXIig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c82cd4c9.mp4?token=SJRDASObdDdk8_uiaNTVd3AZQiFYHGEMg5VASzOdf9EBs--bI1vDf84fKTE-PtkqFz29GY9IUg9XP0lZjRVMAhBUaf7fmSWw0Xp6bF2BzOGYYmIqBFfr3hv9cDzj2RgzDcQr8sme14eSdp5RgFnCJVyWC9td6lG0tLzhVoxZgjjeDzp1lgTJCnFPYRCpt_mXqJS6w4aI8S4Gs94-vEc6KDQsUc6eU1yq1cJ7XBbnvh0G1ocZ35xoQ3mOFy5JGJd28rKGv7ZbEf8-MExmLrBGnX7T0eoa2c9-Cl8K1eXFntpGjegBUEp8jW5WnIlYry47Sn9j87JZ7LP7TFfHNrXIig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
ایران سلاح هسته‌ای نخواهد داشت، و آن‌ها خیلی بد، خیلی بد در حال شکست خوردن هستند. این ماجرا خیلی زود تمام می‌شود.خیلی، خیلی زود تمام می‌شود. آن‌ها سلاح هسته‌ای نخواهند داشت.قیمت نفت به‌شدت سقوط خواهد کرد، درست همان‌طور که قبلاً بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/150054" target="_blank">📅 18:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150053">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/027b715ab2.mp4?token=JbZR2d0b9pki51QOHCxs1WIan6WP5ivzr9-Js4T-OtZQp3ZZ80EfDS5A9K2hYfNF_xR1n2o7Ep3vLpF4rUexHaj77ZrcPWomcT_0AWDsHE8EJ3bDHSvC1BZ6OnFYckxeQe7i1st-XncODd3uEizF93iEv40URfK8PqpfRZ4XwJvAhgiHUwoiTsyHwbDPM1XvpF-f9FhwO08Iu-GLEHafqSEkvzxmsDSwvZdAiwm52Eudf5CYirfIQ5f07rY120LojMhn1HevNYeLK6JjhDse-J1Pt2oPCTMTDAYWVlxYTk77pEMNQ7DDJA7NvwWqjtW-ISMKIXu6BFtfZwqUVoKKGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/027b715ab2.mp4?token=JbZR2d0b9pki51QOHCxs1WIan6WP5ivzr9-Js4T-OtZQp3ZZ80EfDS5A9K2hYfNF_xR1n2o7Ep3vLpF4rUexHaj77ZrcPWomcT_0AWDsHE8EJ3bDHSvC1BZ6OnFYckxeQe7i1st-XncODd3uEizF93iEv40URfK8PqpfRZ4XwJvAhgiHUwoiTsyHwbDPM1XvpF-f9FhwO08Iu-GLEHafqSEkvzxmsDSwvZdAiwm52Eudf5CYirfIQ5f07rY120LojMhn1HevNYeLK6JjhDse-J1Pt2oPCTMTDAYWVlxYTk77pEMNQ7DDJA7NvwWqjtW-ISMKIXu6BFtfZwqUVoKKGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
در سال‌های پیش رو، آن‌ها تاریخ کشور ما را خواهند نوشت و خواهند گفت که جنگ ایران یکی از مهم‌ترین کارهایی است که ما انجام دادیم.
🔴
این در واقع یکی از مهم‌ترین کارهایی است که ما انجام داده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/150053" target="_blank">📅 18:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150052">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ترامپ:
جنگ ایران خیلی، خیلی زود تمام خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/150052" target="_blank">📅 18:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150051">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی مجلس:
اطلاع داریم که کشور های عربی حاشیه خلیج فارس با تأمین مالی آمریکا و اسرائیل برای جنگی تمام عیار علیه ایران موافقت کردند و در حال فشار به روی ترامپ برای آغاز هر چه سریعتر جنگ‌ می‌باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/150051" target="_blank">📅 18:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150050">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
سخنگوی سپاه: ناوهای آمریکایی به ۵۰۰ کیلومتری تنگه هرمز فرار کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/150050" target="_blank">📅 17:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150049">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
نیکزاد: مجلس طرح سه فوریتی خروج از NPT را بررسی می‌کند
🔴
نایب‌رئیس مجلس: ما اصلاً به آژانس و مدیر فعلی آن اعتماد نداریم؛ چرا که وی صرفاً بازدیدهای ظاهری انجام می‌دهد و گزارش‌های منفی علیه ایران ارائه می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/150049" target="_blank">📅 17:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150048">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bccb61d2ea.mp4?token=hD7RL6hvMFXQ_PI1KFZsPd7diyM1XL7vw3lODgqONW1P1X08iJaKbkoqx28TbxGGtEtXnMhohwN4gzMlWcm3BQXMMQ5N6q4FvSSxirsia1m0KIhoeSyk7Klr8yJD7vF669Aw_uQWRNED5VIRNqdlfTiCm4Mc7gyIiqvOEQ6paAuY-xSNuyd46D7GxjvxuBFqwzzXn0-nTGlarjEpCuKdSasmZXMRekkPOvUvlZVIFLk_6lgI1sEbYZtloCLtN6unIfDUMOEzMtLec-dwLWUbf6hBjCoJJ66RIRrR4cyA86rxiUbPIdpkdzUfTMX3EoTmjRypyXnM1TLM1Nq3vn8qfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bccb61d2ea.mp4?token=hD7RL6hvMFXQ_PI1KFZsPd7diyM1XL7vw3lODgqONW1P1X08iJaKbkoqx28TbxGGtEtXnMhohwN4gzMlWcm3BQXMMQ5N6q4FvSSxirsia1m0KIhoeSyk7Klr8yJD7vF669Aw_uQWRNED5VIRNqdlfTiCm4Mc7gyIiqvOEQ6paAuY-xSNuyd46D7GxjvxuBFqwzzXn0-nTGlarjEpCuKdSasmZXMRekkPOvUvlZVIFLk_6lgI1sEbYZtloCLtN6unIfDUMOEzMtLec-dwLWUbf6hBjCoJJ66RIRrR4cyA86rxiUbPIdpkdzUfTMX3EoTmjRypyXnM1TLM1Nq3vn8qfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار دیشب تو شب نشینی‌ها:
چرا به‌جای دزدان/رسایی رفته زندان
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/150048" target="_blank">📅 17:26 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150047">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dnkdxm_vzQgwGI1Sm6MDmP114bfXz75j2XhRE1_yy1URrljbu8McZDwffKHKQ9tTSMXHNCJyrhaIU6PFArwgW-AlNxw9mId9rqosH3eSMwLhTrlnt4FT4jZlrwJ_Oxt3-NP0V-iOuFXnwFhKOfQkK60z13QW6bjx98b1kvZMCmrY3j9ljuoJymNk1WbYFum96KMAltVNb5BIfdSupsC09ioxYydNbr-Jv679VwGkHW580daIi2EDHugwvdQYhgQ4j1GUi2hbrziL0USQnjANpodGEdGFqXhYfJnBCBNvdEB6IG3rehkXtdmSovFxfw2b7MmQjmT0MVvoNwwQLYbcEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز هفتم مهر، تولد پزشکیانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/150047" target="_blank">📅 17:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150046">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ecf3ef8bb.mp4?token=gwRoQxxGQDk4UF7P50t1lRTIVCHe3o-VB_OByT6aJ_uBooodxmFfLQ6RMLWJpsoFazch4BNIL5CuudN3J2wXZ-CYsEaSI9cV8aCOGPYB2arKalTmnAmNkFrs7o4z97WY5nsoIy6SpNdKCTVyrOmkUrIxUCUGYgkJ8zdMy3Y8iaqtLi8hC68s0jvolo-pAV4kc9LoAU15qovcUGM2-_i9erTO7smpCP16P0z3BmZKts6X64ddOAwblWZWVBjs2V0Bx3Br1BLo8LWnf84mp4ORfVRK2TNdaHajwyCU6IxiS6S3eM5SwOOkYUNnFubPvH3UQhoERkd_L7FxLnuCJKl_VAow28Wmq9ugnxmqKAAwrWgNWfkZ_UHCZsoqOkp1XWouclJZmvGsgWuMuJWh2qKperKsn_G6g1A1vFRmA4Qtuua78NpxhGswfmvJVbTfklpkuO8Gq5Zd6T9a7_u9EoaurscLmDoedx8zNlV64aIEqUj2Fq-KpV6_GYCeoiR6jINrvmHLTnzcwt0gFtQtCO2q-chsWdnUxaewLzlLeSrVjSoycccZguFwiUnNsXHMXyHI_bwSyq3POybtWw9QtAZ2eegCSw1qzLaks-8OwhVJw_MXwMNybOHhKfEEa8J-muOL7_MLUZZ8-YIuW8lFZ1X35p22R9jW94SKCxfE89uKmCs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ecf3ef8bb.mp4?token=gwRoQxxGQDk4UF7P50t1lRTIVCHe3o-VB_OByT6aJ_uBooodxmFfLQ6RMLWJpsoFazch4BNIL5CuudN3J2wXZ-CYsEaSI9cV8aCOGPYB2arKalTmnAmNkFrs7o4z97WY5nsoIy6SpNdKCTVyrOmkUrIxUCUGYgkJ8zdMy3Y8iaqtLi8hC68s0jvolo-pAV4kc9LoAU15qovcUGM2-_i9erTO7smpCP16P0z3BmZKts6X64ddOAwblWZWVBjs2V0Bx3Br1BLo8LWnf84mp4ORfVRK2TNdaHajwyCU6IxiS6S3eM5SwOOkYUNnFubPvH3UQhoERkd_L7FxLnuCJKl_VAow28Wmq9ugnxmqKAAwrWgNWfkZ_UHCZsoqOkp1XWouclJZmvGsgWuMuJWh2qKperKsn_G6g1A1vFRmA4Qtuua78NpxhGswfmvJVbTfklpkuO8Gq5Zd6T9a7_u9EoaurscLmDoedx8zNlV64aIEqUj2Fq-KpV6_GYCeoiR6jINrvmHLTnzcwt0gFtQtCO2q-chsWdnUxaewLzlLeSrVjSoycccZguFwiUnNsXHMXyHI_bwSyq3POybtWw9QtAZ2eegCSw1qzLaks-8OwhVJw_MXwMNybOHhKfEEa8J-muOL7_MLUZZ8-YIuW8lFZ1X35p22R9jW94SKCxfE89uKmCs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اندی برنهام، نخست‌وزیر بریتانیا:
افراد راست‌گرا در بریتانیا دربارهٔ بازپس‌گیری کنترل صحبت می‌کنند.
🔴
هرگز اجازه ندهید آن‌ها این را فراموش کنند که خودشان ابتدا این کنترل را از دست دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/150046" target="_blank">📅 17:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150045">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
بنزین سوپر لیتری ۱۱۱ هزار تومان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/150045" target="_blank">📅 17:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150044">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
بر اساس گزارش واشنگتن پست، شبکه‌های CNN، MS NOW و نشریه Politico از یک دادگاه فدرال درخواست کرده‌اند تا دستور ممنوعیت دسترسی رسانه‌ها به کاخ سفید، که توسط رئیس‌جمهور ترامپ صادر شده بود، تمدید شود تا زمانی که دادخواست آن‌ها در جریان باشد.
🔴
ترامپ در تاریخ ۱۸ سپتامبر، دسترسی این سه رسانه را به کاخ سفید قطع کرد و آن‌ها را متهم به انتشار "اخبار دروغین" کرد، اما یک قاضی فدرال به طور موقت دسترسی آن‌ها را به مدت ۱۴ روز بازگرداند. این دستور در تاریخ ۸ اکتبر به پایان می‌رسد.
🔴
این رسانه‌ها اکنون به دنبال صدور یک دستور موقت هستند که به آن‌ها "دسترسی یکسانی" را که قبل از ممنوعیت داشتند، اعطا کند، و استدلال می‌کنند که کاخ سفید این محدودیت‌ها را "به‌طور غیرقابل پیش‌بینی و ناسازگار" اعمال کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/150044" target="_blank">📅 16:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150043">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ایتالیا اعلام کرد که تمام نیروهای خود را به طور کامل از عراق خارج خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/150043" target="_blank">📅 16:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150042">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcff1ecb14.mp4?token=BLsm34_biR-VcMw4dGvBhGiMHwTRWacYkYdhI-k5Ceivarnos7kgzH3EZ2t8-YTc9GbZYP6x95Irel633CXrKek-NuRIUeZI9lyTVyURyEOs4B4SOnqY8XUmfSM5JOG5gd_1AYBNuKpzclxXqyZrmpkte7i0C5Alx2BfOeOJ6RL6LewXa6hD5Pv4-PyEIO7Y8Q9Jkeow21tehJ441gy0tRn7x_Pe7vfrj4T5HBx1Nz58499WmRkdc0HfqaA_J17Lq7OtuEuLEzbZWVu_h9_pjKxdAheTNcrzP-opbfoGKsAoBp7_veGVLlE8Awd8je6W2iExyL349f6H3l5fa5U8PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcff1ecb14.mp4?token=BLsm34_biR-VcMw4dGvBhGiMHwTRWacYkYdhI-k5Ceivarnos7kgzH3EZ2t8-YTc9GbZYP6x95Irel633CXrKek-NuRIUeZI9lyTVyURyEOs4B4SOnqY8XUmfSM5JOG5gd_1AYBNuKpzclxXqyZrmpkte7i0C5Alx2BfOeOJ6RL6LewXa6hD5Pv4-PyEIO7Y8Q9Jkeow21tehJ441gy0tRn7x_Pe7vfrj4T5HBx1Nz58499WmRkdc0HfqaA_J17Lq7OtuEuLEzbZWVu_h9_pjKxdAheTNcrzP-opbfoGKsAoBp7_veGVLlE8Awd8je6W2iExyL349f6H3l5fa5U8PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دوربین نظارتی لحظات پایانی بمب‌افکن راهبردی تی‌یو-۹۵ام‌اس را پیش از سقوط در استان آمور ثبت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/150042" target="_blank">📅 16:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150041">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
دلار هم اکنون 255,000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/150041" target="_blank">📅 16:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150040">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ونس: ایران باید رفتار خود را تغییر دهد تا اساساً امکان هرگونه توافقی وجود داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/150040" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150038">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNLHi0AKPWPxfcltjWUulV5KyNgjNd9th4In9lsamfaGi8YmMWPoMX0Og6XWvpFKjHeO2cH30rOLSoZ93RyTXYAe7T-4XzRWqTVWfVPYa7i-C3yyqGcZGOcEnSEUgOyIioljuz7c8JEqv_g-7Z0s9suj0pBFve0yJF4OAX_29h7IEXEdqlwJf8yp2nOaw68OIqIHyNPa43FHcjMB2RlKPbkur_z0pLNMzrKKWek9vVpSEh23fm8wSdaCL1DIMubtPOFqJjqbuPdxC5Dh5IWIn2p0YDPNXIv7ZBRo4j4-qLVMs2lJHMimkRXW4Z1sXlmYcqiRv6hWMHFYGEiIbxiEFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0587d8651.mp4?token=tJcvPt4U9nvAxSw9IkHheYMvIvpNFVLIX-eEsHgS1pTNrVe3lbPHRZ3pIfzGwtO5W1fY6DvmYJXxMQ2-Ggv4uatBxXsAyA2urwRzwKHxIyz7DKgwEdr5w7an6Brxj4YWakhkim_o-qhx99zRTPZgPtSZo0qR_BocUchJK1_TuHhzroz_EA3kSkZ8fh8YFZyQa2N_T0tpdqqRKz_jpqdH4mbD2NRvqsFimjQHl5y3Vv0z5GmozalUp4A9znnp6aDMpmze-cHS57taHO9gFt591LzHd8mtY3Zgg1hXkii38fm10P1Z0L7IQqI59rZVbT3Ph_xCXuLtbNZ2h2mCJmLKyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0587d8651.mp4?token=tJcvPt4U9nvAxSw9IkHheYMvIvpNFVLIX-eEsHgS1pTNrVe3lbPHRZ3pIfzGwtO5W1fY6DvmYJXxMQ2-Ggv4uatBxXsAyA2urwRzwKHxIyz7DKgwEdr5w7an6Brxj4YWakhkim_o-qhx99zRTPZgPtSZo0qR_BocUchJK1_TuHhzroz_EA3kSkZ8fh8YFZyQa2N_T0tpdqqRKz_jpqdH4mbD2NRvqsFimjQHl5y3Vv0z5GmozalUp4A9znnp6aDMpmze-cHS57taHO9gFt591LzHd8mtY3Zgg1hXkii38fm10P1Z0L7IQqI59rZVbT3Ph_xCXuLtbNZ2h2mCJmLKyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقوط هواپیمای نظامی توپولوف ۱۵۴ در روسیه
🔴
یک فروند هواپیمای نظامی Tu-154 روسیه امروز، در منطقه آمور در شرق این کشور سقوط کرد. برخی گزارش‌های اولیه می‌گویند ۷ نفر در هواپیما حضور داشتند و ۶ نفر جان باخته‌اند و یک نفر زنده مانده و به بیمارستان منتقل شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/150038" target="_blank">📅 16:24 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150037">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا به دولت عراق اجازه می‌دهد پروازها بین عراق و ایران را تحت شرایط آمریکا انجام دهد:
🔴
پروازها فقط از فرودگاه بین‌المللی نجف
🔴
پروازها فقط به مدت یک ماه
🔴
پروازها فقط از طریق هواپیمایی عراق
🔴
باید اطلاعات تعداد مسافرانی که جابه‌جا می‌شوند، نام‌ها و شماره گذرنامه‌های آنها، و مبالغی که هواپیمایی عراق در ایران برای سوخت، تعمیر و نگهداری و سایر خدمات هزینه کرده است، در اختیار آمریکا قرار گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/150037" target="_blank">📅 16:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150036">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
طبق گزارش کانال 14 اسرائیل، که به نقل از یک مقام ارشد اماراتی به این موضوع اشاره کرده است، نمایندگانی از 10 کشور، از جمله امارات متحده عربی، اسرائیل، عربستان سعودی، ایالات متحده آمریکا، مراکش، کویت، بحرین، لیبی (هافتار)، عمان و مصر، در بخش گسترده‌تری از دیدار نتانیاهو و محمد بن زاید که روز یکشنبه برگزار شد، حضور داشتند.
🔴
نتانیاهو و محمد بن زاید در ابتدا به صورت جداگانه ملاقات کردند و سپس مقامات کشورهای دیگر به این جلسه گسترده‌تر پیوستند.
🔴
بحث‌ها بر روی تهدید ایران، همکاری نزدیک‌تر بین اسرائیل و کشورهای خلیج فارس، مسائل اقتصادی و سامان‌های دفاعی اسرائیل متمرکز بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/150036" target="_blank">📅 16:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150035">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siiOjlOyKCfs1hGhUAngRPqZISRsG_xXwKaj-4UH9AXdCnyV0eOIu72Z467gKvS6IQE_KKOvmE9dBjSqw9nDgQEwfAM5zlu7xfX1pW9t8wIajY2f_Yf-8Q2xJwVUi-8iTN66b6mYiegmy0Umu7otjeB-c4jcVmJJPjxpsFKCb4aXzJyIytUCSNlbpNYu6FkXUsKnSgPQu8cDTxwD7RD3wSKricD2jbwlaAJ3lrdtJxRdX912naNtA3TATmvO6FyotfkZ5ASSHW4J1FWtRQgKepRX6K4IEq7v9rklebqMNyL826fycMaLEU757gAVw9hjLlZ4H83Ij7vGkITsLIjuOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش لبنان ۴۷ هاموی و ۵ کامیون از آمریکا دریافت کرد
🔴
ارتش لبنان در چارچوب برنامه‌های کمک نظامی آمریکا، ۴۷ خودروی هاموی و ۵ کامیون دریافت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/150035" target="_blank">📅 16:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150034">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3194b055f.mp4?token=AbUf9ahi1U2tLtOgHtgy_7h1vJQio_AEz6b18A4QE9sHpfjiiW4HF707g9IT1ZzQlEaR9wqPMiGZpT74uIPeE9jlCsULCg4abfm5syRpvcw4lQF-io-zplDjQX8RBb_iCE-U5Meh31FxwgnJqcYVwxHalIzUfQF6ZIkiMvoQAmSDizdbMilpj2qGgfwbwDFkruE3z0VGReOoNMRtbA-gvgKrUWmY_OoXysfJfQhGUO4IPhu0uL8hGIQlMQ2G5cQ4Qd9sKMOmJMAnv-DjKKQzhWYZrwKsQzA-z3qDAHZps9yuuCpdOVhH4phKXc5IYND4qYlNtHC06jF7uZW8ZbFOoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3194b055f.mp4?token=AbUf9ahi1U2tLtOgHtgy_7h1vJQio_AEz6b18A4QE9sHpfjiiW4HF707g9IT1ZzQlEaR9wqPMiGZpT74uIPeE9jlCsULCg4abfm5syRpvcw4lQF-io-zplDjQX8RBb_iCE-U5Meh31FxwgnJqcYVwxHalIzUfQF6ZIkiMvoQAmSDizdbMilpj2qGgfwbwDFkruE3z0VGReOoNMRtbA-gvgKrUWmY_OoXysfJfQhGUO4IPhu0uL8hGIQlMQ2G5cQ4Qd9sKMOmJMAnv-DjKKQzhWYZrwKsQzA-z3qDAHZps9yuuCpdOVhH4phKXc5IYND4qYlNtHC06jF7uZW8ZbFOoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از درگیری فیزیکی مسافرین در یکی از هواپیماهای کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/150034" target="_blank">📅 15:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150033">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80338390ae.mp4?token=X603y5H_mVtvB-IjsbMCV_aMJYEV4mFIcmY38D_riB9cA7e0ylgdFk6JZ_9FvbobpyGnPcSoYMihdxDMYTumuTIgJ-D1nGm7WXqbiDwstr7lSans9762-uU1iYVUCbcS1jV_B0pm7S-_Y9VIMpezvd6KVCAMU-IrEf0-2pajDBl06dR-JU9GYf34rqlx4DtCgXQChiqTGx4mk3grAY2SJpvtS6kI8LwfuUUflET4KNhb3z5VPQ1De3I79Fy0LTD1cvor5w1Zmam17dHzPj6OeDY6h52DEYInsKKU_T4qvydngKeMSh25hF5P0IyZEi9M4UxTwGduhzu22YExJbAUdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80338390ae.mp4?token=X603y5H_mVtvB-IjsbMCV_aMJYEV4mFIcmY38D_riB9cA7e0ylgdFk6JZ_9FvbobpyGnPcSoYMihdxDMYTumuTIgJ-D1nGm7WXqbiDwstr7lSans9762-uU1iYVUCbcS1jV_B0pm7S-_Y9VIMpezvd6KVCAMU-IrEf0-2pajDBl06dR-JU9GYf34rqlx4DtCgXQChiqTGx4mk3grAY2SJpvtS6kI8LwfuUUflET4KNhb3z5VPQ1De3I79Fy0LTD1cvor5w1Zmam17dHzPj6OeDY6h52DEYInsKKU_T4qvydngKeMSh25hF5P0IyZEi9M4UxTwGduhzu22YExJbAUdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: دشمنان ما ممکن است پیش از انتخابات به ما حمله کنند
🔴
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
من در پایگاه نیروی هوایی، در کنار خلبانان قهرمان و نیروهای زمینی فوق‌العاده‌مان هستم. ما به‌طور مداوم در همه جبهه‌ها در حال عملیات هستیم.
🔴
در مجموع، طی چند هفته گذشته بیش از ۱۰۰ تروریست را از بین برده‌ایم و این فقط مربوط به غزه است. البته در لبنان هم در حال عملیات هستیم؛ یادتان هست که در ارتفاعات علی طاهر چه کردیم.
🔴
دستاوردهای بسیار بزرگی داشته‌ایم، اما فشارهای بسیار زیادی هم وجود دارد. این فشارها برای عقب‌نشینی و کنار گذاشتن دستاوردهای بزرگی است که به‌واسطه شجاعت نیروهایمان به دست آمده‌اند.
🔴
من اجازه چنین کاری را نمی‌دهم و نخواهم داد.
🔴
یک نکته دیگر هم وجود دارد: نشانه‌هایی داریم که دشمنان ما ممکن است پیش از انتخابات تلاش کنند به ما حمله کنند.
🔴
بنابراین از اینجا، از پایگاه نیروی هوایی و از بازوی بلند دولت اسرائیل، پیامی برای شما دارم: با ما درنیفتید؛ نه حالا و نه هیچ‌وقت. بازوی بلند ما هر جا و هر زمانی که باشد، به شما خواهد رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/150033" target="_blank">📅 15:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150032">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا به دولت عراق اجازه داده است تا پروازهای بین عراق و ایران را، منحصراً از طریق فرودگاه بین‌المللی نجف، انجام دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/150032" target="_blank">📅 15:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150031">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6MBO-6Tr8iix5QqcTUDyHD7G-e9aKLch6DDLDQfpTVOjedrjrzrUtieNwcVwNxoOlDzMyN4qQ3jO4e0OgGTz3L_0IhsoLNtd7v82_YAI4PMSYY6RhHpZ2JDEUHvYAFjuZnew3v3cNgMOJ9Sb3DpE98QDw0PIuyZySmZCvyxQT3DG9jXxToIAFTSdBAQId72o_RSIEHWvVsF9qKuXS6hq0EcJEzxOCX2Cb2MGShmPiS5jsBUvVfYSdR0QqwEMuQjvc0PdysuTmJsZdx_Ds64KCT4_S5AQixzUwWBlyI7Q8PDfQBy11HZmp5t93gfHoBKzbZjLHdy53I0FLTOjuaqeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر تسنیم از آموزش دخترای جانفدا
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/150031" target="_blank">📅 15:24 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150030">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fed1510120.mp4?token=V9ly7n4z4xyN_FGBGvMy5ShOgte-VhL9MJekH-5AdUjYbmow65umYI9ILJAoUFpyE5w1V8gx8YGGo9XoiNKMCsAfbLCMNUNkIcyrAdPx-fcram9l-tby8xR33UC-3VJXnLDCJqZ6bQGG_jzQG7M12liPLUM0wUwHZVOE69xgstNLdNCdJseuwfog6LCAHjlaUi9CuuEy_MD4rW64WI8niqF3otfsvm-PBw2rKIKvYCvuAlTUZIiZTntfHXdl8xvuNrQlFaig95OICmHgK2fIFktGHO1_n-rZ6XfgYkG0j9q3oTe_98QpVAdsT2HCMSbb4XKSDDxs6zxvTdPuz3mA-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fed1510120.mp4?token=V9ly7n4z4xyN_FGBGvMy5ShOgte-VhL9MJekH-5AdUjYbmow65umYI9ILJAoUFpyE5w1V8gx8YGGo9XoiNKMCsAfbLCMNUNkIcyrAdPx-fcram9l-tby8xR33UC-3VJXnLDCJqZ6bQGG_jzQG7M12liPLUM0wUwHZVOE69xgstNLdNCdJseuwfog6LCAHjlaUi9CuuEy_MD4rW64WI8niqF3otfsvm-PBw2rKIKvYCvuAlTUZIiZTntfHXdl8xvuNrQlFaig95OICmHgK2fIFktGHO1_n-rZ6XfgYkG0j9q3oTe_98QpVAdsT2HCMSbb4XKSDDxs6zxvTdPuz3mA-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده ایران در سازمان ملل : ایران بار دیگر بر حاکمیت کامل خود بر جزایر ابوموسی، بزرگ تونب و کوچک تونب در خلیج فارس تاکید می‌کند.
🔴
این جزایر همواره، اکنون و در آینده بخش جدایی‌ناپذیر از خاک ما بوده‌اند و حاکمیت ما بر آن‌ها غیرقابل مذاکره است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150030" target="_blank">📅 15:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150029">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5A3BKpV8nHdcq2UszXXWngO85Qxj-0lWlQFxQBZ7H8un4MF2SFryaQhKR8FzHRYb1JdLYpEcVVv7CoGudytKKOKP7pXDOW0IBn84zm8CAoAgVFjmNWqpWScfRu0DjIPodN8-ex-VNhBVLmndtFpL3-rT-ccn7kfdfXddiAAlTyX1o_rnLEUptdbejNn1uKGstjYjW0nG6PdANy04J7BW_p5NB6vXzS7iK-J8von4g8LCTR1YKG9ZnIRpp-DaBspdecaOfQ8AWMEngUZPeUZlyrsx7a0s-4SRB3wABo2nSGfWaDhvxCismwbLvI5cCRymXY4n8V80JCNKjUI4DOSsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: آقای اژه‌ای چرا شما پرونده رسایی رسیدگی کردی و بقیه چیزا ول کردی
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150029" target="_blank">📅 15:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150028">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
الحدث به نقل از منابع دیپلماتیک مدعی شد: واشنگتن و تهران "از نتایج مذاکرات فعلی ناامید شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150028" target="_blank">📅 15:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150027">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
منابع دیپلماتیک به «الحدث»: کانال‌های ارتباطی میان واشنگتن و تهران «همچنان باز است»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/150027" target="_blank">📅 14:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150026">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03578ba96b.mp4?token=gw6zWjkSn6S0o9fVBjcZiYvCZNdY8rpkhuHF55by37bzn7Iqzfca-co5PLtJ6S9y0J3qj8l3vSEeKQxPl5qkEUXt2yUKSL5Kntrv2f3HyJtHuBgb7JyLxrCzx7l2G80t_V-G1SxKqH-DbDMvRk6cHcaVGQFJP1HqadRtKlWk9Sv1Pc7FJxqMFX2_nKsCuVDIt0PHaPcvWQ55bpalxB0c6JPZnDY9MZDNQxUVaJB4fZchMfR5NgY-9M8CICvKk4IgCKindoP4s95FomjR4MFvhcYljz2YLgN60Ib2Sho4nF5XMhD5IEzfMrzekgOgccPz5t943PVDoeKJk3pKy4Gymw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03578ba96b.mp4?token=gw6zWjkSn6S0o9fVBjcZiYvCZNdY8rpkhuHF55by37bzn7Iqzfca-co5PLtJ6S9y0J3qj8l3vSEeKQxPl5qkEUXt2yUKSL5Kntrv2f3HyJtHuBgb7JyLxrCzx7l2G80t_V-G1SxKqH-DbDMvRk6cHcaVGQFJP1HqadRtKlWk9Sv1Pc7FJxqMFX2_nKsCuVDIt0PHaPcvWQ55bpalxB0c6JPZnDY9MZDNQxUVaJB4fZchMfR5NgY-9M8CICvKk4IgCKindoP4s95FomjR4MFvhcYljz2YLgN60Ib2Sho4nF5XMhD5IEzfMrzekgOgccPz5t943PVDoeKJk3pKy4Gymw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گویا میلی گلد دفتر مرکزیش رو جمع کرده و کلا رفتن و سرمایه ملت به باد رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150026" target="_blank">📅 14:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150025">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">📌
دلار امریکا در تایم فریم روزانه و هفتگی کاملا ساختار صعودی دارد
🕯
🔔
بعد از شکست سقف کانال صعودی در صورت تثبیت میتواند تا ۲۹۰ هزار تومن صعود کند !   قیمت فعلی ۲۳۴ هزار تومن !   #بازار_مالی #تحلیل_بازار #اقتصاد #فارکس #سرمایه_گذاری
📌</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150025" target="_blank">📅 14:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150024">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
اطلاعیه هواپیمایی کاسپین درباره توقیف هواپیمای ایران در ترکیه
🔴
دیروز دوشنبه 6 مهرماه 1405 (28 سپتامبر 2026) در جریان برنامه عملیاتی پرواز استانبول–تهران، در پی بروز یک موضوع اداری در کشور ترکیه، بهره‌برداری عملیاتی از یک فروند از هواپیماهای بوئینگ این شرکت به‌طور موقت با محدودیت مواجه شد.
🔴
گفته می شود قرار است امروز هواپیمای شرکت هواپیمایی کاسپین از توقیف خارج شده و به کشور باز گردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150024" target="_blank">📅 14:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150023">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bcdb658ca.mp4?token=VRqC2UPJyRoeDPz6VEP415bAU6zGFBcYvBRG1v9elX6jGT80KI9KEUBqWrboUH8pxeAf1_a_2g8dIf6J56GF3mYquffzhMcKQCyNyq9JwkGgpHUrYt62BGWL7BMhVKGQfl-hjvX6x7BClFmhRfv9WWlU38w-m9ATQaG2Rz2ytY9OlfXX0BlcgZ84TleLmo2b6xB_HglicJdt6n1Vr8-5iFp29oIJ0GjNRbzqrESkMwko-iXMENFNUf0XH4Pbu-oK5bEqTIrrdJIfDfce8vQ2FZDb3UPZPdaQdxuaD4Icnvp-tgwsobMfA5gazr8K0S-oaMNgpgkduvg9WHPpj17YkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bcdb658ca.mp4?token=VRqC2UPJyRoeDPz6VEP415bAU6zGFBcYvBRG1v9elX6jGT80KI9KEUBqWrboUH8pxeAf1_a_2g8dIf6J56GF3mYquffzhMcKQCyNyq9JwkGgpHUrYt62BGWL7BMhVKGQfl-hjvX6x7BClFmhRfv9WWlU38w-m9ATQaG2Rz2ytY9OlfXX0BlcgZ84TleLmo2b6xB_HglicJdt6n1Vr8-5iFp29oIJ0GjNRbzqrESkMwko-iXMENFNUf0XH4Pbu-oK5bEqTIrrdJIfDfce8vQ2FZDb3UPZPdaQdxuaD4Icnvp-tgwsobMfA5gazr8K0S-oaMNgpgkduvg9WHPpj17YkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هادی چوپان: یک ساله دارم کابوس میبینم؛ باورم نمیشه دیگه محبوبیت قبل رو ندارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/150023" target="_blank">📅 14:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150022">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvNZNUWQRcgawk-weNkTGGKw4INFgkGjtFrhFcDiJLO4OP14rPpvF2opH9mrfn1glkOG9oxL8dWzzDowd0zeq1JfBGgMTlQqQBc2uuhPc2mfg5w7HvxsWcALCt01gMV5-HF3FgCJy6DyKK7cJ2LSbiIkk54Ws3bsSvCXq6vA5NMe85TQ5BJjofruihMp7I9Gdg9S20bnZD97VQpZ5oJt7QiOwqqUg8TYnpClNKuYmUSHpWyIsvqMinugrIGfi7Hri2sqbI-KlVlMNp7_QpWNrjzHl66OrFEiGVjBlfg7YnwoGS6hj0cwqn3ECcy4Rflm7o0k0PQXgoWRKXqEQ2eR0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۷مهر روز آتشنشان هست و این روز رو به تمام آتش نشان‌های عزیز تبریک میگیم
🔴
و به یاد جاویدنام آتشنشان حمید مهدوی
❤️
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/150022" target="_blank">📅 14:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150021">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
کان نیوز به نقل از مقام اسرائیلی:
هیچ راهی جز انجام یک عملیات نظامی گسترده در خاورمیانه وجود ندارد و از آن گریزی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/150021" target="_blank">📅 14:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150020">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aITamSyX-Nl2WrFC5uVm0sdSjaZitawqck7bI6pvgR7riEdlEIW-yKtoohzIphkAHS_cOpdgpnV5MksnOlQ3I4hhcVVVYnxVC7369DGXw0GMBxk46b6qZw5B6Vgkq0E7nh4LUHljvdH-TPoBvtFozZ_EaPn5EWbfXiEnAq_AxdZY6kKs1vzCTNWhwBtZNMcRSSksPHNKXzNR-T77GE25kf3v_5AVHLdBjxTiCNeWuIvLKt5ZZghYlgRpSN56VGZnlEjPRAc6nACpHXiDXKS4ZfHAcAxP9fSewmzhWTGFjjXCT5alnKTum9SKALFMaYjT9Wqn2HuoWINpjy75dv5uKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گروسی: امیدواریم ایران و آمریکا مذاکرات را از سر بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150020" target="_blank">📅 14:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150019">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ماجد الانصاری، سخنگوی وزارت خارجه قطر: ما در تلاش هستیم زمینه مشترکی میان واشنگتن و تهران ایجاد کنیم.
🔴
هرگونه هدف قرار دادن زیرساخت‌ها از سوی هر طرفی را به‌شدت محکوم می‌کنیم
🔴
به تلاش‌های میانجی‌گرانه خود ادامه می‌دهیم و برای ایجاد زمینه مشترک، پیام‌ها را میان طرف‌های مختلف منتقل می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150019" target="_blank">📅 14:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150018">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا:
گزارشی درباره اصابت یک پرتابه ناشناس به یک شناور، هنگام عبور از تنگه هرمز در شامگاه گذشته دریافت شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150018" target="_blank">📅 14:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150017">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
روسیه: ما نمی‌خواهیم ایران از پیمان منع گسترش سلاح‌های هسته‌ای خارج شود و اظهارات تهران در این مورد نیاز به توضیح بیشتر دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150017" target="_blank">📅 14:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150016">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
شبکه رسمی عربستان: طالبان دچار بحران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150016" target="_blank">📅 14:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150015">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
رویترز به نقل از منابع و داده‌ها: پس از آغاز مجدد فعالیت خط لوله شرق-غرب عربستان، بارگیری نفت از بندر ینبع در دریای سرخ شروع شد
🔴
جریان فعلی نفت در خط لوله مذکور، حدود ۲.۶۵ میلیون بشکه در روز است؛ بازگشت به نرخ حدود ۵.۵ میلیون بشکه نیز شاید یک ماه دیگر زمان ببرد
🔴
ریاض نزدیک به ۱۰ میلیون بشکه نفت خام را در بندر ینبع و پایانه المعجیز بارگیری کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150015" target="_blank">📅 13:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150014">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTchdzcJts59q-LQVXWtYduLTznph7tPu27NHm28dqPSuFSRjlGGAsUOVsJ0JYCTwJ1ZrgACqnUuZJjF-ondFWGx-woe-cPfk-Lp04WiG3s6SUFBvlYIYNxum2aFhpdxWQAPCA091hA4MlFVtTjfeO2gY0tWotz6sX_gMO8eemB2i3u4sV2SG6Suqg9258TIiYbD4qsIMs1Cqzbh5zr_5RL56sL6Evh_Fpyik0lnq7YGcMlI7alQQfV8svfDxf7xB-zOlR9wjhl-uvROoumkay7Dn2mlPM65ssW3qwZ_B7LfHlLXlvoFn4vYHYr0UMKbsYXRnPr-2LCAKjJvCsoreQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که عربستان سعودی مجبور شده است از دو ایستگاه پمپاژ آسیب‌دیده در خط لوله شرق-غرب عبور کند، که این امر ظرفیت انتقال آن را به حداکثر 3.5 میلیون بشکه در روز کاهش داده است تا زمانی که این دو ایستگاه تعمیر شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150014" target="_blank">📅 13:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150013">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a56fef62.mp4?token=bLcixPk6Wk8mE8elKvSIogrrwsZhzPXXujkJbB7x707I9Oe2JFrWXqWrWAylZ1XLv_BJUBAe7dwt-vUFzKl11UWsD2gKYcN-p206WlPtoGjgV2Nqwunp8ZYrpvp1NW8FNEuyMHJbH3jP35pqsuk8tKaa-oSdeJqFQLiUiQr2uHElezKoOWjCK5Q6tQhw1nNGwAHHosADXsV0mSVZlCJPO60kZcgtam9U_QOINta8-kARt5yM9XbU_02tf9cYIpLei4Qptkqk8alTgqIm_6QxetAs8L3Yg3emY_3AcXwG_fh1wqyKeRHNyJpWWARLkhX5TShbT-iR6Z5jTEfFSXhEsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a56fef62.mp4?token=bLcixPk6Wk8mE8elKvSIogrrwsZhzPXXujkJbB7x707I9Oe2JFrWXqWrWAylZ1XLv_BJUBAe7dwt-vUFzKl11UWsD2gKYcN-p206WlPtoGjgV2Nqwunp8ZYrpvp1NW8FNEuyMHJbH3jP35pqsuk8tKaa-oSdeJqFQLiUiQr2uHElezKoOWjCK5Q6tQhw1nNGwAHHosADXsV0mSVZlCJPO60kZcgtam9U_QOINta8-kARt5yM9XbU_02tf9cYIpLei4Qptkqk8alTgqIm_6QxetAs8L3Yg3emY_3AcXwG_fh1wqyKeRHNyJpWWARLkhX5TShbT-iR6Z5jTEfFSXhEsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار:
گفته میشه کالابرگ قراره کلا 300 هزار تومان بیشتر بشه که این افزایش، پول یه پُفک هم نمیشه.
🔴
مهاجرانی، سخنگوی دولت:
خب ما هم کالابرگ رو واسه خرید پفک نمی‌دیم که، هار هار هار هار...
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/150013" target="_blank">📅 13:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150012">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ژاپن بخشی از تحریم‌های خود علیه سوریه را لغو کرد
🔴
این کشور ۱۶ نهاد از جمله مؤسسات مالی و شرکت‌های نفتی را از فهرست تحریم‌ها خارج کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150012" target="_blank">📅 13:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150011">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سخنگوی ارتش: دولت قطر همچنان اعلام می‌کند از وضعیت ۳ خلبان ایرانی خبر ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/150011" target="_blank">📅 13:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150010">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
طبق محاسبات غیرالهی دلار 253شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150010" target="_blank">📅 13:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150009">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6iUUUELW3msE9QlB4UbSmD2C2mIg77z-cyqmvUad70YyCEK2v2adSYfiJbTjF42S2lD-MZMS1vUTozPtrjrYWJ2kDngl-IDGEi5198PMMu-NrgKXO86BtWYvMx5huop9XP5AIRTVsuIudl2AoaKxA54SaYmJ9KdzgwglmRW_nqQIhQ-AL8X8LZ2iciHYtnbYsugrE9EBDlv0kPF35S_Ef6YjW6kb7L0OOgXB11fPJ6P-RkfQcDarhfIuJMCOjdZxcpD7OLfqYxEV7prUpuZ4ZBL7r02G3ixEvjPr8N3XOPALJeqAzbFsRoLkL4WWXKF43SgJNUF7vgrKLAVKWBIJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیر سیاری: جانفداها آماده باشن که اگه آمریکایی‌ها وارد شدن برن بجنگن باهاشون
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/150009" target="_blank">📅 13:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150008">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299316a1b0.mp4?token=KAxgK-b464Lye4t7dtvQmaQK6YvMNyt7-81b40qnEIS8neoAKeFex7qjfFVaX6aZMcpCWKvdgoQcKURhLhE9yrJzdzhoGXmIjU7pqCjhmvL229ad9fxG0duCJNlHiTh1gU_5jRJVqP6UkbhSc2VbcDx2Bq3Af26QW5WiHVJYbx7O9200JlTLZN6bqWiXzZ-HhvOwaNGiRPpJZQBvf8hBQNk28lPDDonHmKEdd9t89Xo8hpnHo44myFobfRHVGKLs2dgeaHqDDDTJBl2SFDjiPsQPa__FsXMZiWov4hNtRrxFrksahdCKDg0AqcHD1Ofqm9yrTRLnGdyEBJFCkN1onUt6fVtfU-5wTvYK5uER0t6r958UUOr1qA6_m6meuUrlXYh46hXD2mmRj9EVML3q5C6QWi0sq2Ri1NzWbqDaGKoAxYcgvGj-f8jVC0KbUHPUxODNMxZXQlQZsfXRknmPA0zbpIGDR3pXgJfbFGsJsTAsCCd-sNs1SXEUaSaiKN9fd0bJyCy0_O5Fqm6TAaH1IPAw9nL4RF7t2_5JHoigzt39Epgk424bXh95oJMcBOuBvZa9pNt0CCSowKk5wqa_cHpBqX-X45zJpbIbcI_9i48PE8s-KisfSA4kHkq1RmDpGUqS2MNpXvt5q-GVvyyOhHviH0S6VOvixg7jTLkerhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299316a1b0.mp4?token=KAxgK-b464Lye4t7dtvQmaQK6YvMNyt7-81b40qnEIS8neoAKeFex7qjfFVaX6aZMcpCWKvdgoQcKURhLhE9yrJzdzhoGXmIjU7pqCjhmvL229ad9fxG0duCJNlHiTh1gU_5jRJVqP6UkbhSc2VbcDx2Bq3Af26QW5WiHVJYbx7O9200JlTLZN6bqWiXzZ-HhvOwaNGiRPpJZQBvf8hBQNk28lPDDonHmKEdd9t89Xo8hpnHo44myFobfRHVGKLs2dgeaHqDDDTJBl2SFDjiPsQPa__FsXMZiWov4hNtRrxFrksahdCKDg0AqcHD1Ofqm9yrTRLnGdyEBJFCkN1onUt6fVtfU-5wTvYK5uER0t6r958UUOr1qA6_m6meuUrlXYh46hXD2mmRj9EVML3q5C6QWi0sq2Ri1NzWbqDaGKoAxYcgvGj-f8jVC0KbUHPUxODNMxZXQlQZsfXRknmPA0zbpIGDR3pXgJfbFGsJsTAsCCd-sNs1SXEUaSaiKN9fd0bJyCy0_O5Fqm6TAaH1IPAw9nL4RF7t2_5JHoigzt39Epgk424bXh95oJMcBOuBvZa9pNt0CCSowKk5wqa_cHpBqX-X45zJpbIbcI_9i48PE8s-KisfSA4kHkq1RmDpGUqS2MNpXvt5q-GVvyyOhHviH0S6VOvixg7jTLkerhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی ارتش: اگر هر بانوی ایرانی یک سرباز آمریکایی اسیر بگیرد  ۱۰ میلیارد تومان جایزه می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150008" target="_blank">📅 13:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150007">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
حسین محبی، سخنگوی سپاه:
در نامه‌ به مردم آمریکا درباره میزان محبوبیت سپاه در ایران و خدماتی که به مردم ایران و منطقه ارائه کرده، توضیح دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150007" target="_blank">📅 13:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150006">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxkDmcbhAk5KzSfQVI6_waCJAIBbdIV-x-yCeU5PxT7Lc2UwKlCFRRNVPpNeJEQipAnSmOgWh6VtgV7G_n9CLSq5ilWmcI25UOlbRLB6utc7J8dZwLrqW_CYyuLkRvq5uo3QFnUpNGSLEkUCWttv5RVWoRKky9QnlWum3WFqoNoqDLbM3NkgEZ1I4FjEOyhqquNZvEzm1-2FEXTCad5PDlS9deMNhtQzHuU75dcnYPZbXYz62BzwbrR6jarXdXilP5W9C9bpj1oWUKohwgJd8pye36u4Y63TvaAsgDBwl1ADpDcS2HtsPSKn9rrxGR6C0tqRVTtNpZ031WTof56qLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد بن زاید:
ایران محترمانه جزایر ۳گانه را تحویل ما دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/150006" target="_blank">📅 12:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150005">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
هم اکنون گزارش کاربران از اختلالات بسیار شدید و گسترده در اینترنت تهران
👍
👎
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/150005" target="_blank">📅 12:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150004">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">چرا هیچکس چیزی نمیگه؟   تتر شده ۲۵۱۰۰۰ تومن !؟  چه وضعیتی شده  @shahab_gold_trading</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150004" target="_blank">📅 12:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150003">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
قوه قضاییه: پرونده ترور سردار سلیمانی در دادگستری تهران تشکیل شد که سه هزار و ۳۱۷ نفر شاکی داشت
🔴
رأی این پرونده دو سال و نیم پیش صادر شد و بر اساس آن، سردمداران دولت آمریکا به پرداخت ۴۸ میلیارد دلار محکوم شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/150003" target="_blank">📅 12:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150002">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
اطلاعات شرکت کبلر دریایی:حجم انتقال نفت از طریق تنگه هرمز، ۹ میلیون بشکه در روز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150002" target="_blank">📅 12:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150001">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSIglnh-fSK4l2Io9agVkhP3BMSpzDt02SdmFRHxerNrleWCzT9DKtHEefron_oD-NsHXloiA7cbXIcG9a_bebvAo-s4Z14qyaphq4EWabIwX690pyIqQjuax0thJebLAZob1l9JTRS9qyrPtze-naoEvYakOchoC-OnLa98kzD6NLU3ax5IBLKn_XHtI_We1JwoXQuWXa4EAN-o9tM9KpxipSq_aqhgitOz8cJlxil5gpfBL4aj_XHvHUWgB5FvZypWy1UgLo60b8lVG9uzLUxWpovgvPBTacOooL5tP6xW9dVEIVNN9ip9xFmXGha-5ZgtJbRNcyB6Ujtu2r3O2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نزدیک ۲ روزه سایت مخابرات adsl از دسترس خارج شده و سامانه ۲۰۲۰ هم پاسخگو نیست. خیلیا اینترنت خط ثابتشون ۲ روزه کلا قطع شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150001" target="_blank">📅 12:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150000">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
هم اکنون حمله جنگنده‌های سعودی به یک خودرو در حجه یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150000" target="_blank">📅 12:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149999">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2rFdP32_WLYPm3JUbCPdQEGYTthbuU1F8SpWN3YvOZ2x5N-IfkviufRwTn_UWK92Vh9g8UjH0E6pGEBKUbV1OtdfMsWoIyUy654MZ9AT1iiwBvm73p0_l1HcY6IvJoSkkkqD7jv3oWTGUfRU8Pc5IIkJnhXseNoi5ekM8yO3dmQf_7NgMjUtPQLAQsxmTpXPgr6MMei-srLQNUrhjuR_BFQdPawrW9SYvP9CXInTPWKSQT-IcsGMuRysuH_5_0fnEg02FUZzKkZMYoKy3uHwGkbljlazIY7HGuspZucVh-6rqAV665twpqiqVk3bIvQcg4EqISa2682FHwxpotv1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخی منابع عربی از توقف پروازها در فرودگاه بین‌المللی ابها در عربستان خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149999" target="_blank">📅 12:26 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149998">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
هر گرم طلا هم اکنون 24,700,000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149998" target="_blank">📅 12:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149997">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3SVBrm86IVkdqcBQcsFwdHlF3RS68ZOMjRs77lp5pdc_MECtHNpxDYHeG8424JYxM3PwuKICIyibOjJX1eo98L27maV8Y6iviWvZMJbZkkbizzphusScvUFO7A_kLWRQlWzLiZIOeXx9Ml2NvhdMq2ziF6qPi--VTR1bQICstg5GOPxsSlatj-ePTjMEUvX0aoNO7x_glSSg-jVXWNb5jdHiNdSd-q3scZP66Hduat95K0AxAoIL5izYtHvsJT3j89kFdMR1wWkcK1GftTd7H7uNDYr0VYbOYaCnBAVDh6SJFgokJyIOPesumVc7etNGXGUm9FINYXwtskp-Ks-qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت دلار هم‌اکنون ۲۵۰هزار تومان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149997" target="_blank">📅 12:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149996">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jC5n_bfU84d33WVFsmGmIsnA7K0gvxd-8GNtEDTMKTZvVoGGkfOPEPTDqg8CcviXKBXtQ0BZ5k-XADPPhMtAtXcJHYXLukvW0bJCjsu6hLuZ5sO7ikiEA7H4VE_QT8wDOta93kdkr-oPlhFhHqvbDZT4w_oEQR3EYBlBWr5HMldED-p144Yx7uWlquVvuaNPcYvbM6eXRkf7XeP5vPY62Z_OXXKRkQ32wZnLXjODNg_pgkJvXAj-v2st7Apfe4zTNf4pHJQ5ekzFfbWZghjud3AgYYYKaIQVgi3XrEqSTvDXm1f2YuanyOZQrwyx8tXiIDLCuJCxoeYO_vxXtDIFpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکارد دیده شده در شب نشینی امت سرخوش در مورد محکومیت رسایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149996" target="_blank">📅 12:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149995">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">به نظرم همتی تو جواب گرونی دلار باید بگه رهبرمون هرچی بگه همونه</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149995" target="_blank">📅 12:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149994">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ایران با اختلاف زیاد بی ارزش ترین پول دنیا رو داره
و نکته جالب اینه مردمش همون پول بی ارزش رو هم ندارن
🕺
🕺
🕺
🕺
🕺
🕺</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149994" target="_blank">📅 12:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149993">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">به نظرتون یه سریا با چه متطقی میگن ما قدرت اول جهانیم؟ خبر ندارن بالا چخبره؟</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149993" target="_blank">📅 12:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149992">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=o2xTXRkST0jyaKgcvAgaGVq_wuGLrrfJvPZXqZBNZwnHrWLygkVzn9HpryeAIohU2WvaH8RulONh54Ye0F_kVT-rY-9CoOR3icBIwu9M68ybIF7qitubaV4ll51Q3v7W8w_Bny1NxqTvZRx5NVhn0Bi_INZFrVfJMqpwqnJrO1kKKBL8Np2ihIhNH2lUlBJKrVN28ERsOtBwajeEP52IHjvUlYuRK2iCE5CkW4X04fzz2fz105neH7yQ_bSWVisPviPfHnHjiLmFH8pqqJd0ZY4dLlCgUnEUs9FQ8wzccnLft1iihRKN8ssiooagD6z0Zw4GM_Bv_YZG4RauMo26VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=o2xTXRkST0jyaKgcvAgaGVq_wuGLrrfJvPZXqZBNZwnHrWLygkVzn9HpryeAIohU2WvaH8RulONh54Ye0F_kVT-rY-9CoOR3icBIwu9M68ybIF7qitubaV4ll51Q3v7W8w_Bny1NxqTvZRx5NVhn0Bi_INZFrVfJMqpwqnJrO1kKKBL8Np2ihIhNH2lUlBJKrVN28ERsOtBwajeEP52IHjvUlYuRK2iCE5CkW4X04fzz2fz105neH7yQ_bSWVisPviPfHnHjiLmFH8pqqJd0ZY4dLlCgUnEUs9FQ8wzccnLft1iihRKN8ssiooagD6z0Zw4GM_Bv_YZG4RauMo26VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حقوق یک کارگر 65 دلار در ماه
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/149992" target="_blank">📅 12:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149991">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سخنگوی دولت: با توجه به شرایطی که در آن قرار داریم، فعلاً تصمیمی برای افزایش حقوق نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/149991" target="_blank">📅 11:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149990">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/933cce337c.mp4?token=NLLjTaxCuXwjsKwDhkBewT1_4M_Qsv4IC2yLo-YuDtQKGybyrT4yGQjmVnp11o2Dgu6ThqUiht1U-XUksMgMwmE8IIOeCfSa8YtWsmHhP_7tJFs9H-ZTaN5_U4ykbaAJTwokESZy68A31rEMAk2VoVDb78ZrxwhfCv2Sl0hX3gdQ0rcmpHmgDmAyMGQU-srs25xzXNvdJS4kYoh9xbP4wXSGN-pUU8q1SP1Mp_2PyJz5TVuHqxx9JOrO1HxVoK3KHgZuCCCmw5f2ByLlGwsZPX3Ey62s4VxYt865Dj88JUzXPt4ugydAkOHLDMeT2wId1BArdGUcA1qR7hsmrEkL6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/933cce337c.mp4?token=NLLjTaxCuXwjsKwDhkBewT1_4M_Qsv4IC2yLo-YuDtQKGybyrT4yGQjmVnp11o2Dgu6ThqUiht1U-XUksMgMwmE8IIOeCfSa8YtWsmHhP_7tJFs9H-ZTaN5_U4ykbaAJTwokESZy68A31rEMAk2VoVDb78ZrxwhfCv2Sl0hX3gdQ0rcmpHmgDmAyMGQU-srs25xzXNvdJS4kYoh9xbP4wXSGN-pUU8q1SP1Mp_2PyJz5TVuHqxx9JOrO1HxVoK3KHgZuCCCmw5f2ByLlGwsZPX3Ey62s4VxYt865Dj88JUzXPt4ugydAkOHLDMeT2wId1BArdGUcA1qR7hsmrEkL6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: افزایش ۳۰۰ هزار تومانی کالابرگ، پول یک پفک هم نمی‌شود!
🔴
سخنگوی دولت: قطعا کالابرگ برای خرید پفک داده نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/149990" target="_blank">📅 11:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149989">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66b62710f4.mp4?token=qtNFOrJvSSZ-snMpZbdwPV8Mde850bP09V0gxZtMKyMpmc7GF7XL413bHqT_mAVEHYzWcSn7IQB0JgGgip3LR4ZOvryxKzDj9SyKkX--tW4Ox_rYRm3jePm4ZYL8QvyStgpdbmIIU3R8CVnaMtmS9hHYlIW_fJkisz36bep4g0Oy2KAv5GBZKbO1KBr_BmERtGqz0JPVWS3EiP0Q_2dlbE-MpP5P9JwwKGAHPAZh7jtc8Ku63b_I-GBH3zqh2svl5Vm0Q1W4N6JRuRWGtA58RH1Llszi85qNqKSt6UFYkGldd6RuKy2YKx70Kyg-9Ucn7Z5eyEZkiGILd6q5_3WTOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66b62710f4.mp4?token=qtNFOrJvSSZ-snMpZbdwPV8Mde850bP09V0gxZtMKyMpmc7GF7XL413bHqT_mAVEHYzWcSn7IQB0JgGgip3LR4ZOvryxKzDj9SyKkX--tW4Ox_rYRm3jePm4ZYL8QvyStgpdbmIIU3R8CVnaMtmS9hHYlIW_fJkisz36bep4g0Oy2KAv5GBZKbO1KBr_BmERtGqz0JPVWS3EiP0Q_2dlbE-MpP5P9JwwKGAHPAZh7jtc8Ku63b_I-GBH3zqh2svl5Vm0Q1W4N6JRuRWGtA58RH1Llszi85qNqKSt6UFYkGldd6RuKy2YKx70Kyg-9Ucn7Z5eyEZkiGILd6q5_3WTOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دود غلیظ مشاهده‌شده در آسمان تهران ناشی از آتش‌سوزی در یک ساختمان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149989" target="_blank">📅 11:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149988">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سخنگوی دولت: احتمالا در استان‌های شمالی مشکل گاز داشته‌ باشيم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/149988" target="_blank">📅 11:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149987">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
نتانیاهو: فرمانده تیپ شمال غزه در گردان‌های قسام ترور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/149987" target="_blank">📅 11:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149986">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
رویترز: روز دوشنبه مقامات آمریکایی و ایرانی با میانجی‌گران دیدار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149986" target="_blank">📅 11:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149985">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUyR22xDCt_nRgufkCJViDRRqYQldCvX3xJMtueia57gUhHDeDiTyqnzz6FBWXFDzzX0XNwd8-9rMVeZzMej1zLtLupSfWG9Vb3dIxbnX5NrirdkiWzztG39nMt0D7CRVJ_B1mzpLlYNYCIrcAn5h9EvtePQDdqN7RqSYIOVKTT8HzspUR04zgiVrJnshTdG1wW9sRmgi72jEoftGoWFDqE4SoVll2P2fELsnhJjWWV0Mpi_9OPtSL4dg8CrAGPRGZGLD0sK5amBMxGCceIiKR5I8cP-hu8Pc2xXRCUMeVfEqU6wSY8xyFvlYwuyxOiaOZFY4Ps4IZTerdUG6l-T0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت بعضی مدل‌های لپ‌تاپ اپل در بازار به حدود یک میلیارد و ۲۰۰ میلیون تومان رسیده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/149985" target="_blank">📅 11:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149984">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/27c8682bb3.mp4?token=PdhsY_Fs_gT52VA7Gvna-_NJmpxfiloz284fJ7LpjrLY1J-SafdjAggThLB4l_mE845kVQk0mic-ceM4oB5moHQxoDahPOhUCct1_7J3MT0fr6eLIvQg-qn1IBP8Fu1VzCcDtJmIqtWw0GcNAt9C14WU6hlQYTlCN4c4hz5E0e1j0yorQ78ms6ki7vBuxQF0idvqZltaswKyRM4ner2it1-Y__Lw6qRBWMvL3wWMgXexgdebwJNcG4XgjujvJ6WKXLPNPEf4ylE4eFrc7yx1Fz0nPTMLRg0afG_VfbwwSuOaVxD4a6qiI5Y3KiQykm-6T0FtwKKXK7OqCqDmLVLAww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/27c8682bb3.mp4?token=PdhsY_Fs_gT52VA7Gvna-_NJmpxfiloz284fJ7LpjrLY1J-SafdjAggThLB4l_mE845kVQk0mic-ceM4oB5moHQxoDahPOhUCct1_7J3MT0fr6eLIvQg-qn1IBP8Fu1VzCcDtJmIqtWw0GcNAt9C14WU6hlQYTlCN4c4hz5E0e1j0yorQ78ms6ki7vBuxQF0idvqZltaswKyRM4ner2it1-Y__Lw6qRBWMvL3wWMgXexgdebwJNcG4XgjujvJ6WKXLPNPEf4ylE4eFrc7yx1Fz0nPTMLRg0afG_VfbwwSuOaVxD4a6qiI5Y3KiQykm-6T0FtwKKXK7OqCqDmLVLAww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام ویدیویی از پرواز جنگنده‌های F/A-18E/F Super Hornet و F-35C Lightning II نیروی دریایی آمریکا از ناو هواپیمابر کلاس نیمیتز USS George Washington منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149984" target="_blank">📅 10:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149983">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
عراقچی: انعطاف ایران در موضوع هسته‌ای را به شدت تکذیب می‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149983" target="_blank">📅 10:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149982">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شرکت Tether:  مبلغ 550 میلیون دلار USDT [معادل 134 تریلیون و 200 ملیارد تومن] مرتبط با ایران را فریز کرديم!  ما در سال 2026 به صورت کامل با نهادهای اجرای قانون و مقامات تحریمی آمریکا برای بلاک کردن پول‌های مرتبط با بانک مرکزی ایران و شبکه‌ های تحت تحریم همکاری…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149982" target="_blank">📅 10:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149981">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
شهردار کرج: من خودم جزء قشر کم درآمد جامعه هستم و حقوقم کلا ۶۰ تومنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/149981" target="_blank">📅 10:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149980">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
قالیباف: تلاش‌های امروز آمریکا برای تحمیل محاصره‌ی دریایی، بستن کریدورهای هوایی و اعمال فشار حداکثری بر شریان‌های تجاری کشور با برنامه ریزی و مدیریت جدی در حوزه‌های اقتصادی و پاسخ های نظامی مشابه سال ۶۰ شکست‌ خواهد خورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/149980" target="_blank">📅 10:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149979">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
قالیباف: ترامپ اخیراً لفاظی‌هایی درباره‌ی تنگه هرمز و عبور کشتی ها از این تنگه مطرح کرد که تکرار ادعاهای پیشین است و حقیقت این مواضع واهی برای همه شناخته شده است.
🔴
هم آمریکایی‌ها و هم سایر کشورها بدانند: همان گونه که قبلا گفته بودیم در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت و اگر امنیت ما تامین نشود، هیچ زیرساختی ایمن نخواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/149979" target="_blank">📅 10:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149978">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
قالیباف به ترامپ: بچرخ تا بچرخیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/149978" target="_blank">📅 10:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149977">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHUBQyccQiePeLo4iQB2n9BlYd_DWM7FWViV-yklkQU9IBHdPvd8qngZc-r3GF1cNUbDlzSSbscsVDNvjUxShNuZwKWwytXw20ZqfHMCeCW0_1KAc7GrDpjLaLVsSkwjmWkQpRKBhPT8WbAf-cqoGDJgRyMPRi2TQjFxAGqeoy1-_4HNzfyFx8yMeBsGtTwnZvwNUr-vnHp1BdG2eMIDLa585wl86HVHGakupGWrX93ivJc2Q0_Kl87AbEHKXFKkd1XvJkuKUjiaUlLxZKxNG2kh6igf71dGnnHn65zsDd9lsZnOZ7Kydk7E7xABUV_pgTPrPHEJEX-dxJgHy1HA5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی: امارات باید به واقعیت‌های تاریخی و حقوقی منطقه پایبند باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149977" target="_blank">📅 10:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149976">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: دو اسکادران جنگنده آمریکایی در ساعات اخیر به پایگاه هوایی عوفدا در جنوب اسرائیل رسیدند و به نیروهای آمریکایی دیگری که از قبل در این منطقه حضور داشتند، پیوستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149976" target="_blank">📅 10:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149975">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95ebd1c763.mp4?token=YVU8EiwQmNKRweh7NJJ8S0YwmeLsWHfZgBknJYPE_L7senHWUyP8Y-77XREcUJYEJH1gRYvqyC5BiS4mhktcVX1RYU4EQicgTdJOuPHDc9DUIgWvwXgawjrOcFCRgPn6dvP5u6fZArr7eYClO6uYTHx-z7M3kJ-tZTB9y9p38jK9Zotb9suI0YWQbEZoNvVTzB9Obp9fgnBxhaITL9aFoPXZNuagNGDK1eLJICwcaF7r66FIxv-5ahjOYKaEXh2LuJERlCcRnGtWPlQc_TV5KUM3b2WUO6hoQsLIAeMfV9Tibr2XRu7EAld9zAOuu4cujWRdVAHSUEI-Uv76Z5WuwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95ebd1c763.mp4?token=YVU8EiwQmNKRweh7NJJ8S0YwmeLsWHfZgBknJYPE_L7senHWUyP8Y-77XREcUJYEJH1gRYvqyC5BiS4mhktcVX1RYU4EQicgTdJOuPHDc9DUIgWvwXgawjrOcFCRgPn6dvP5u6fZArr7eYClO6uYTHx-z7M3kJ-tZTB9y9p38jK9Zotb9suI0YWQbEZoNvVTzB9Obp9fgnBxhaITL9aFoPXZNuagNGDK1eLJICwcaF7r66FIxv-5ahjOYKaEXh2LuJERlCcRnGtWPlQc_TV5KUM3b2WUO6hoQsLIAeMfV9Tibr2XRu7EAld9zAOuu4cujWRdVAHSUEI-Uv76Z5WuwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر خارجه آمریکا:
«کافی است بگویم آنچه در بریتانیا طی آخر هفته رخ داد — و آنچه ممکن بود رخ دهد — بسیار جدی است.
🔴
این حادثه به دست یک عامل خارجی انجام شده است. فعلاً نمی‌خواهم درباره جزئیات بیشتر صحبت کنم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149975" target="_blank">📅 10:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149974">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
مارکو روبیو، وزیر خارجه آمریکا:
«رئیس‌جمهور ترامپ به‌وضوح اعلام کرده است که مسئله گرینلند درباره فتح و تصرف نیست؛ بلکه موضوع امنیت ملی است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149974" target="_blank">📅 10:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149973">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
رویترز:ایالات متحده تا فردا، چهارشنبه، از آخرین پایگاه‌های خود در عراق خارج می‌شود. این کشور جایی است که بیش از ۴۵۰۰ شهروند آمریکایی در طول بیش از دو دهه جنگ، جان خود را از دست دادند. ایران و متحدانش این خروج را به عنوان یک پیروزی جشن می‌گیرند و این امر به آنها آزادی عمل بیشتری می‌دهد، زیرا اکنون نفوذ عمیقی در این کشور دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149973" target="_blank">📅 10:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149972">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/47df547a14.mp4?token=BdBUjHZIOjpq0XfniJCXeMa7VBF0EHcbR8TB3ccGbQw93o84OzcN20cdlYYC4Agbq6F7bzS6UpfJOBUVztrCagqpT-8_9BjipmxWDcftgLfajFUgzhtJqLYXK_nNX8C3WWDPwVTpYOK2mJPrakNe5fYOxBtPIWIStmaemECmRguyv_YtRIqBl4tw9ptxkmm9qwTclKQrAdvf1t70mtLyuVMV8mDcKGcCKMid0aRKbxwd0-B5Dv4GuIKiLLjDNo5QSufuAQbJT_bo5HhqmgV5vh854or0JmyevJZWns2oguVp7LgJ4F1FESiPTh-WEAT9BnukokZf9aQ5qravVvy75w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/47df547a14.mp4?token=BdBUjHZIOjpq0XfniJCXeMa7VBF0EHcbR8TB3ccGbQw93o84OzcN20cdlYYC4Agbq6F7bzS6UpfJOBUVztrCagqpT-8_9BjipmxWDcftgLfajFUgzhtJqLYXK_nNX8C3WWDPwVTpYOK2mJPrakNe5fYOxBtPIWIStmaemECmRguyv_YtRIqBl4tw9ptxkmm9qwTclKQrAdvf1t70mtLyuVMV8mDcKGcCKMid0aRKbxwd0-B5Dv4GuIKiLLjDNo5QSufuAQbJT_bo5HhqmgV5vh854or0JmyevJZWns2oguVp7LgJ4F1FESiPTh-WEAT9BnukokZf9aQ5qravVvy75w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر خارجه آمریکا، درباره زمان برگزاری انتخابات در ونزوئلا: «در ونزوئلا دو اتفاق باید رخ دهد. نخست اینکه اقتصاد این کشور باید به روند بهبود خود ادامه دهد، زیرا مردم ونزوئلا سال‌ها متحمل رنج زیادی شده‌اند.
🔴
ما درباره ۲۵ تا ۳۰ سال فساد و سوءاستفاده مالی صحبت می‌کنیم. اما مسئله دیگری که باید رخ دهد و ما تمرکز زیادی روی آن داریم، گذار دموکراتیک است.
🔴
آنها باید در این کشور انتخابات آزاد و عادلانه برگزار کنند. ما به‌طور جدی با مجلس ملی ونزوئلا در سال ۲۰۱۵ همکاری می‌کنیم تا شرایط لازم برای برگزاری انتخابات آزاد و عادلانه را در سریع‌ترین زمان ممکن فراهم کنیم.
🔴
پس از آن، ونزوئلا می‌تواند وارد مسیر بهبود و رونقی شود که شایسته آن است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149972" target="_blank">📅 09:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149971">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
فوری / فاکس‌نیوز: اسرائیل برای حمله دوباره به ایران در آماده‌باش است
🔴
فاکس‌نیوز: مقام‌های اسرائیلی علناً از آمادگی برای ازسرگیری حملات به ایران سخن گفته‌اند.
🔴
اسرائیل کاتز، وزیر جنگ اسرائیل، اعلام کرده ارتش در حالت آماده‌باش قرار دارد و برای ازسرگیری عملیات و انجام حمله مستقل به ایران آمادگی دارد.
🔴
با این حال، در همین گزارش آمده است که برخی منابع و تحلیلگران اسرائیلی تمایل کمتری به آغاز دوباره جنگ دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149971" target="_blank">📅 09:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149970">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cfb2f478bf.mp4?token=Ybcaq4RbUOuxH_QTPtFHT6Bkri364TjE3aiK8d63KVWnr9iqJ5I7v3Fco7s-hyLAjiO-yaBZkK_6-q3msHro97RI_k-ePJswhRJotDY3u1qP2cZuYeQHNwF9LM-OjqWCQNTre9eZ1NlsrwaKr7aA8Vk98n0eD5NBZe-qj9o_ugHnI2tmR1mhzrZy8F6farTSKxVEPFf4QCIoLTSEimtW1VlDKy_e1UdK_wHTw7HfoNvd7nZB4iCXL4Ett8tbKsetTQXZ6-wDnjIPr4kkY6Fhog-1GWfT8mZx5edUJ8AvIyYDMfTHyhYkNnVrY-k5yUqzij8EleurQuJYDlJUxjL3UZJAd4c5mOOQTqe2TmaKN4SzovtiUljTd8QVkHuaY7McLkFs0W1vIrqQ-ZNEJ9mMLzNPeTYyfGR0vmxQ1J-8d8KOcQL-6Dpt-brJP7Sj8BW82uDF4ISLnK7mlXXCy9GtU4lQuPqvnEtJs-K8_iqbgH48ndX4zGZb6ctH7DzghWlozDno64W1Cg99mldQhZbmnyc4UOwQTZs8tyK_Wd0niu5fdzXG5wDlQmzQH508cNx33KA900mRFjm1s6iwsE5VneNAJZNMnBBav9LFJgXbcJvfkpGjEKqMbqZ_S8bgqqEXLb6hg8mcS2sdRAC7gCgtdOFZ_BileSdSAYNW8hKloTo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cfb2f478bf.mp4?token=Ybcaq4RbUOuxH_QTPtFHT6Bkri364TjE3aiK8d63KVWnr9iqJ5I7v3Fco7s-hyLAjiO-yaBZkK_6-q3msHro97RI_k-ePJswhRJotDY3u1qP2cZuYeQHNwF9LM-OjqWCQNTre9eZ1NlsrwaKr7aA8Vk98n0eD5NBZe-qj9o_ugHnI2tmR1mhzrZy8F6farTSKxVEPFf4QCIoLTSEimtW1VlDKy_e1UdK_wHTw7HfoNvd7nZB4iCXL4Ett8tbKsetTQXZ6-wDnjIPr4kkY6Fhog-1GWfT8mZx5edUJ8AvIyYDMfTHyhYkNnVrY-k5yUqzij8EleurQuJYDlJUxjL3UZJAd4c5mOOQTqe2TmaKN4SzovtiUljTd8QVkHuaY7McLkFs0W1vIrqQ-ZNEJ9mMLzNPeTYyfGR0vmxQ1J-8d8KOcQL-6Dpt-brJP7Sj8BW82uDF4ISLnK7mlXXCy9GtU4lQuPqvnEtJs-K8_iqbgH48ndX4zGZb6ctH7DzghWlozDno64W1Cg99mldQhZbmnyc4UOwQTZs8tyK_Wd0niu5fdzXG5wDlQmzQH508cNx33KA900mRFjm1s6iwsE5VneNAJZNMnBBav9LFJgXbcJvfkpGjEKqMbqZ_S8bgqqEXLb6hg8mcS2sdRAC7gCgtdOFZ_BileSdSAYNW8hKloTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر خارجه آمریکا، درباره تهدید بمب‌گذاری اخیر در نزدیکی پایگاه RAF Fairford: «آنچه در بریتانیا در آخر هفته رخ داد، آنچه نزدیک بود رخ دهد و آنچه می‌توانست رخ دهد، بسیار جدی است. این حادثه به‌وضوح دست یک عامل خارجی را در میان دارد.
🔴
فعلاً نمی‌خواهم درباره جزئیات بیشتر صحبت کنم. می‌خواهم از مقام‌های بریتانیا تشکر کنم که در این زمینه بسیار همکاری کرده‌اند و اوضاع را به‌خوبی مدیریت کرده‌اند.
🔴
می‌دانم خبر آزادی برخی از این افراد با قرار وثیقه، در حالی که تحقیقات درباره آنها ادامه دارد، باعث نگرانی بسیاری شده است.
🔴
ما در حال رایزنی با مقام‌های بریتانیا درباره تمام این مسائل هستیم. اما باید بگویم که آنها در برخورد با این حادثه بسیار جدی، همکاری و کمک قابل توجهی داشته‌اند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149970" target="_blank">📅 09:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149969">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
رسانه‌های عبری: نشستی با محوریت ایران هم‌زمان با سفر نتانیاهو به امارات برگزار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149969" target="_blank">📅 09:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149968">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
انفجار کشتی در تنگه هرمز
‏
🔴
شرکت امنیت دریایی «امبری» اعلام کرد یک کشتی تجاری هنگام عبور از مسیر جنوبی تنگهٔ هرمز، در شمال «خصب» عمان هدف اصابت قرار گرفته و دچار آتش‌سوزی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149968" target="_blank">📅 09:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149967">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
عراقچی نیویورک رو ترک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/149967" target="_blank">📅 09:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149966">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eFj0NOoyYYxcf3XMksJidEUSgNpEn8aPRkjGbwM-l9EPv5ZhRfbvahqQxqZGbUEkYtVzk6z_Ja5DQI9_hEmnHbSo2hTNZ--kufl0VBF2gYL_ipAHzwU0EinMakz5Io79BeoazQpv7YgW8ij_SGBwb-9fCGLkdP2su9Mfu1iEHhC5oXm_hoH8IDd38FoJONjvO1bnB9htFqrzrkpY02nH7rNIEb7ClZATIyUl47ywKL90kS8xP4Zc8M41jllQIAJI6MT2R7a5bc6jp7CCyRX6PXSgXORpBUy1mwsAISAcQmXAsfmTlPQi4mY3OioMdfjbwZ4ALNSXfXDDVl1p2gYw7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال‌استریت ژورنال: عربستان سعودی انتقال نفت خام از طریق خط لوله آسیب‌دیده شرق-غرب را از سر گرفته، اما با حجم کمتری نسبت به ظرفیت معمول.
🔴
در مقابل، ایران از زمان ازسرگیری محاصره تنگه هرمز توسط آمریکا در ماه ژوئیه، نتوانسته نفت خام خود را از طریق این تنگه منتقل کند.
🔴
ذخایر نفتی ایران که پیش از محاصره انباشته شده بود، ممکن است تا اواسط اکتبر به پایان برسد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/149966" target="_blank">📅 09:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149965">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری و رسمی/ دلار 250 هزار تومان
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/149965" target="_blank">📅 09:26 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149964">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blxbpUApnhacVw8-DiZ41Ph0Zm7NO4sO5C7_KA2xLHeI9TMsSta4Htu0LbkdBQ9g4L7s9vHY_a4nNNR3m5MXT4EGPNsApL9-_o0Pug60P_HiIJvkuIKpEZ8QHjPubGQo4VKWAM2OzVEIvzauHTujrKqa9iXx3bVvMNGwxAokbGZVzz8LBdqkjyH7T_vaJaiTHNj5WcZ_Fbdshg9njd55eKcbIxZsTMqmg3uqJoqPAuRsHEMABPrlZ-LYO4rZE6omf2KX73bH-St-wq9Ry-ykRbYJ_CUaYh_P1H_Vh0B-_bmIBAGZ_RnOqVzpj_gNJV4fxB32dAbJKzAiKu77ku3Wxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت خام برنت به 107 دلار برای هر بشکه افزایش یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/149964" target="_blank">📅 09:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149963">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
عراقچی:
امروز (دوشنبه) یکی از واسطه های قطری دیدار مجددی با ما داشت، بحث هایی را انجام دادیم . روی ایده هایی صحبت کرد و اینکه چگونه می شود برای تحقق شروط ایران راهگشایی کرد و چگونه این شروط را محقق کرد.
🔴
ایده هایی داشتند و بحثی را داشتیم که باز با طرف آمریکایی هم مطرح خواهند کرد و بعد پاسخ نهایی طرف آمریکایی پس از آن به ما منتقل می شود که امیدوارم تا فردا (سه شنبه) این کار انجام شود.
🔴
من چند ساعت دیگر به سمت تهران پرواز می کنم و پاسخ را قطری ها هر موقع که داشته باشند، می دانند که چگونه به دست ما برسانند.
🔴
این ارتباطات و پیام هایی که میانجیگران قطری و پاکستانی رد و بدل می کردند، همیشه بوده، الان با توجه به طرحی که ایران ارائه داد، شکل جدی تری به خودش گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/alonews/149963" target="_blank">📅 02:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149962">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03738737a2.mp4?token=k6o9ME9M_cpWPrwUSs84Z7fX1YuqfhWMuojgYC-In9xpgST2ZpY4tFI20blhk4QDmHtzyQFadSUDw0_XvK5sT2pWGwtai31gyNLaBcI6A3rBO-2iRAVaMKHoqEg-xSRT4ijMABg8fEBiJWYrlSAuMr8XB7rzV2FEjgeShS0ETCSpMWRJ1uB61Bo-lIs8gRwy5NpVI2kMwNKakwdfo03dKEEN2DhXwEIInSqaDGdEm73410Ub0GksOs_bRJ0I1KT9MFS9GHg-58u0N1GpwWcKq48PoUecFxXi82vYgHhI_VNLYN0k1VF-ZUi1GMAPWyzPJCnhcZGifSeWRFrchKoLRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03738737a2.mp4?token=k6o9ME9M_cpWPrwUSs84Z7fX1YuqfhWMuojgYC-In9xpgST2ZpY4tFI20blhk4QDmHtzyQFadSUDw0_XvK5sT2pWGwtai31gyNLaBcI6A3rBO-2iRAVaMKHoqEg-xSRT4ijMABg8fEBiJWYrlSAuMr8XB7rzV2FEjgeShS0ETCSpMWRJ1uB61Bo-lIs8gRwy5NpVI2kMwNKakwdfo03dKEEN2DhXwEIInSqaDGdEm73410Ub0GksOs_bRJ0I1KT9MFS9GHg-58u0N1GpwWcKq48PoUecFxXi82vYgHhI_VNLYN0k1VF-ZUi1GMAPWyzPJCnhcZGifSeWRFrchKoLRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بن سبطی از چهره‌های اسرائیلی: مجتبی خامنه‌ای زنده‌ست ولی کسی دستوراتش رو جدی نمیگیره. به گفته او اسرائیل منتظر درگیری بین رهبران ایران یا قیام مردمه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/149962" target="_blank">📅 01:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149961">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBsJYja_sY7Cnt-Lc962hRWgIydRcpyM93vqs-36BBzuN3MltFxZ4HZfEomlB_Klve7KidDEt2ZEBR5NOlAy_fS2ntXYdK6KvQrEzDdBuZirbXXDVR-R0zXuIQwbs-XhzVjlACAhGUIV7HBLcz83T_Uk5bcmsHID5elQPJFrx4clJ6gPMTb30SjrFPOy7-bFCsMv-Gd4jI7iHsDBP3z2VdkvJ1G6CAkOuPI7hzeRKVVNKI6za4WPzE798M2cSujmm8Fd6tHCYMztiT5d4pzspNkGJBcwtiioUERFU6EVBjwpUIYkAfYuo2CiQUul-dZ2bQLVkPatuCbUuzpADNxhdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
آکسیوس به‌تازگی گزارشی منتشر کرده که در آن آمده است "ترامپ" به ایران پیشنهاد رفع تحریم‌ها و آزادسازی دارایی‌های مسدودشده را داده است. این خبر نادرست است. من هیچ پیشنهادی به آنها ندادم!
🔴
گزارش آکسیوس، مانند بسیاری از گزارش‌های دیگر، یک داستان ساختگی است که صرفاً با هدف ارضای "سندروم جنون ترامپ" آنها منتشر شده است. آنها باید فوراً این گزارش جعلی را بردارند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/alonews/149961" target="_blank">📅 01:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149960">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
شلیک موشک کروز از هرمزگان
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/149960" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149959">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">در روستایی دورافتاده، کدخدایی بود که سال‌ها با حاکم شهر دشمنی شخصی داشت.
هر بار نام حاکم می‌آمد، کدخدا می‌گفت: «روزی او را سر جایش می‌نشانم.»
اما به مردم روستا می‌گفت: «روستای ما از همه دنیا قوی‌تر است و هیچ‌کس حریف ما نمی‌شود.»
کینه کدخدا روزبه‌روز بیشتر شد و سرانجام تصمیم گرفت با حاکم درگیر شود.
حاکم هم در پاسخ، راه‌های روستا را بست و نیروهایش را به آنجا فرستاد.
کدخدا که نمی‌خواست شکست خود را بپذیرد، مردم را وارد جنگی کرد که توان پیروزی در آن را نداشتند.
خانه‌ها و زمین‌ها یکی‌یکی از بین رفتند و روستایی که زمانی آباد بود، ویران شد.
مردم مات و حیران به خرابه‌های خانه‌هایشان نگاه می‌کردند.
کدخدا اما هنوز می‌گفت: «ما قوی‌ترین روستای دنیا هستیم!»
پیرمردی از میان جمعیت گفت: «اگر قوی بودیم، چرا خانه‌هایمان را از دست دادیم؟»
آن روز مردم فهمیدند گاهی کسی برای پنهان کردن یک کینه شخصی، غرور جمعی را سپر می‌کند.
و روستا بیش از آنکه از قدرت حاکم شکست خورده باشد، قربانی لجاجت کدخدای خود شده بود.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/alonews/149959" target="_blank">📅 00:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149958">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/teHS220c2tZ4fEwOKD0VAJDtkJTc2TTyiaHFTrNOlGlWZfsSC-W6aR-gr2-kx1U2xCu8LtW0vTw-I8P3wBssRyzNTUaOysaJzOcQH1EQT765nkM1CRcYNf2lW1n9ETwkvWXC-UZguAg_sw6bQPzOP2qii5pADO1C0zeN6hAqT6Iz9MeMtvsk4eNon2g3qIvcNDgXGVc12kEpaAkKI0P3k1IbY63CzjSmYLQNpmk19I4x2uuA24oIVVFXC5aERCOivj-pUF6rRSoutXDbTTDT25tG4vTsSCz34nfhl5_OmGQAV7v0w29tk2xuVHZH_gze04Mu7vOLig66yPZlDyK-VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید:
«ظرف دو هفته چیزی از اقتصاد ایران باقی نخواهد ماند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/alonews/149958" target="_blank">📅 00:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149957">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نکته اصلی اینجاست که دلار داخل و نفت خیلی این حرفارو تا اینجا جدی نگرفتن  هروقت دیدید اینا شروع به تغییر محسوس کردن بدونید ممکنه جدی باشه  نفت ۱۰۵ دلار  تتر ۲۴۴  @shahab_gold_trading</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/149957" target="_blank">📅 00:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149956">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
مهدی محمدی؛ مشاور قالیباف:
روحانی و اصلاح طلبا برای آمریکا پیغام فرستادن که اگه یه لایه دیگه از رهبران و فرماندهان رو ترور کنی؛ احتمالا زمینه تغییرات در ایران به وجود بیاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/alonews/149956" target="_blank">📅 00:14 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
