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
<img src="https://cdn4.telesco.pe/file/GF3qY5PHxQrJubVCVnqCBGxJVuDmbjZNpZDpQWCvz4v6KP8LR91hMGs76EOdmBEHKmQ_2dTU_673JQVt-OZ4X6yM88Fcjoi15jLKz0odBD0-LkMpW6L6w4ZjVOmV-w35U9xBVskEvkAg5Aaz--V0vghYMO0Wz4gI1qtyBp7r4dWTyEttM2ks_lpiJeNPQmbvwfMedrMWh9VjicJ_FZZuhtjyP2MwPvOELM_0yxjWcup1Lx2bVUsmFkT2igAzFJjoXqAMJwJqbISNB93xZxbEI5jrhCF5bbcKXGiLKBRw7gnBRg-rHEW6sJJ3X5O3xLuohUGt7smAjsvfU5LrM4XOfg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 939K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 00:42:24</div>
<hr>

<div class="tg-post" id="msg-122191">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_Q1LC1N1ldeGob-ovp9fDkMUpnjfNoNmPX50VOoWT0RyeEyZ7gPnvVLMBjI4Hc7y8Ae4IoPMszNmsthQZi5F5y1F5gpMce4E4MuMukHZefYs5-ZrvW0msIKDF828LREnWHLUQzoyhHCVgGOJJBajvPcFzJbAnzy3HLHmFj6Qw41I3r0Vl-iQe0MBLepH-3u4VIawlQ23z51gGegZE9j2TlH0BXbpx2X6BG5txRZ9T7S33XCQfVCiIqktVBT7raK0ZW6mVzwo6XH-WClePjqyPGWboFTjUORrzXvxYS4teiQhRZ1blJ7W5FF0hFbu8Y9dinYTwOwtttOGkF6EvFiPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون اول ترامپ، بعد جلسه درباره ایران کاخ سفید رو ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/alonews/122191" target="_blank">📅 00:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122190">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">املاکی از تسلیم بی قید و شرط رسید به تنگه هرمز به زودی باز میشه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/alonews/122190" target="_blank">📅 00:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122189">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39125570ad.mp4?token=SON1vYt_R1du4pC6Eh0DJMvwvIWKyw-V64CDnikoZGIK--_HTfgVmsFsXgQGUfYcZj1uBIkRn2yjGuS0iyvzGbmqJBb5WP0GxUgqqZwgDfNAuSBsHAXJ6SVqklX4QR3lO7uT9wq8XtGhyCovVU3k1MuvSdF4OSWYkE9_4SGh-58fxTX-84R_QudVb4McSy4L4B659Hb5Y8_LrsKxSWpDl-vePG8BxbAW0QCagycwmxp0lonDVGLu_wxBSv9nXUTCpB5eMXBe0BoccUhcnMhpdukMc5v5MQ8m6ql1pgn7UvNAMb0qPecQskqdChUSGgWjsWn-U9HUpZmUbEE3S8Ql8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39125570ad.mp4?token=SON1vYt_R1du4pC6Eh0DJMvwvIWKyw-V64CDnikoZGIK--_HTfgVmsFsXgQGUfYcZj1uBIkRn2yjGuS0iyvzGbmqJBb5WP0GxUgqqZwgDfNAuSBsHAXJ6SVqklX4QR3lO7uT9wq8XtGhyCovVU3k1MuvSdF4OSWYkE9_4SGh-58fxTX-84R_QudVb4McSy4L4B659Hb5Y8_LrsKxSWpDl-vePG8BxbAW0QCagycwmxp0lonDVGLu_wxBSv9nXUTCpB5eMXBe0BoccUhcnMhpdukMc5v5MQ8m6ql1pgn7UvNAMb0qPecQskqdChUSGgWjsWn-U9HUpZmUbEE3S8Ql8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چه احساسی دارید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/alonews/122189" target="_blank">📅 00:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122188">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
مارک لوین:
«تاریخ نشون داده که بهترین زمان برای صلح، بعد از شکست یا تسلیم دشمنه.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/alonews/122188" target="_blank">📅 00:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122187">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YayGoaGvaCeAhiT1Qdy37BNCRSahHVVQHC7uaVXwQEpqQ8wyDlBJwepYR4WU6e3_wgZpdCZiGzi-I6gPSudWFOgA2p2xKI9XlLTAb9E3NUSQU_VjAa1bCAiO-JNY3PwunP-IdWsK1lmEHDbpzeT3q0I7ZZNmtelZwiSaicsXxbvoFW3x7fMxlMdvpAr7Qs_DLuKA7-BIsNpS4YE7zg_bBm2t0lYiU_KSq9Pty-FrVnFsV-RJdwFKbKx3Qf2wn0xtJ4KaqaJb4q4Ogn1B07YQoarOLOCrRw64s8BekzFk7wsApcYdJ4sJDWUJGsn22XEwUhYBpr36n70UT5z18KwMEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی
:
تنگه اگه باز بشه جواب اون مردمی که ۸۰روز اومدن تو خیابون رو کی میخواد بده؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/122187" target="_blank">📅 00:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122186">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
تتر هم اکنون به 169000تومان رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/122186" target="_blank">📅 00:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122185">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
هم اکنون ریزش شدید دلار و طلا
🔴
تتر 171000
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/122185" target="_blank">📅 00:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122184">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
طی اتفاقی جالب بازهم پمپ بنزین‌ها شلوغ شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/122184" target="_blank">📅 00:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122183">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ: رژیم ایران را کاملا عوض کردیم
پ.ن:
😂
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/122183" target="_blank">📅 00:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122182">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
بزودی ۳۰روز مذاکرات هسته‌ای با قابلیت تمدید تا ۶۰روز آغاز خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/122182" target="_blank">📅 00:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122181">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوری و رسمی/تنگه هرمز باز میشه و جنگ تمام شد
🔴
مذاکرات بر سر پرونده هسته‌ای و مسائل دیگر بزودی آغاز خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/122181" target="_blank">📅 00:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122180">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فوووری/ ترامپ هم اکنون اعلام کرد که پیش‌نویس تفاهم‌نامه‌ای با ایران تا حد زیادی مذاکره شده، در حال نهایی شدن است و به زودی اعلام خواهد شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/122180" target="_blank">📅 00:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122179">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqMhZWvM1-b8gF3mX-UJNLXbXUdiLPZvUrBaKJpEEuVwgNIIAZc6X7KbxRWqYQejZdC3urflNl51FqF21Jm8pMYrhBTlFlvmasqONDe2JpIDk1CwPvvGGEIK7k_4la5geMufvjPlTpI_S4xhjLZpKN9ImjdyLHwoazepKj_peOXexQ4MnSA9ZIhcUA5V_YwnfKbMCeBqhgwMWeR7WUMgUCNqJPSo63XhVxuyZpLyP_SDEPR1RvLetsBf4eXIBJYsR2oRyoiv7msObZvIBXvp4MCkOB5w7Ww9WEKeGfr1er3eH45O6jiWqJMRprEXFw0ENso6iPTDqEaoebqoYAK2Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووری/ ترامپ هم اکنون اعلام کرد که پیش‌نویس تفاهم‌نامه‌ای با ایران تا حد زیادی مذاکره شده، در حال نهایی شدن است و به زودی اعلام خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/122179" target="_blank">📅 00:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122178">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
کنسول جمهوری آذربایجان در تبریز بر اثر تصادف در اتوبان جلفا-تبریز جان باخت.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/122178" target="_blank">📅 00:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122177">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">💢
فوری/پرواز جنگنده‌های آمریکایی در مرز ایران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/122177" target="_blank">📅 00:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122176">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOGsliKj4QrR43LX-wIH_FIW4AI6bvESybaigeOBKF4xvnQQw6cvzGB8J7ZA2UrHQRQdOgch-Qy3qKnzKrQlDKvTFhrUyM1Ie7-WP229lv7FtSsB4bIo-Zna1ywtzaJ_UtLxptn_JQX7-4nDHmm7FjoDB49DMB3zEz4PuKHJzZw8sd8pCWZdN8u3HstL_uIZG3cCcsuNni_3cGrxPDNa_HA5x4rWJyirJCrcHXkCFMPPPmW53mh0O3k0uz3Ky42cIuTvfik-znuieF1LCI9ohXq4jItP2ZPIYRTYIdqsnHFv1unot8-rjoiIZ3LXBUW6pYwMqSbqUanOihmsmf6MYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت دوباره اتاق جنگ اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/122176" target="_blank">📅 00:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122175">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
پرزيدنت ترامپ از اردوغان تشکر کرد که او را رهبر جهان قرن‌ها منتظر خوانده است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/122175" target="_blank">📅 23:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122174">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
یک منبع منطقه‌ای به Axios گفت که رهبران عرب و مسلمان شرکت‌کننده در تماس امروز با رئیس‌جمهور ترامپ به‌طور یک‌صدا از او خواستند که برای پایان دادن به جنگ و کاهش تنش‌ها در سراسر منطقه، به پیش برود.
🔴
«پیام همه این بود: لطفاً به خاطر منافع کل منطقه جنگ را متوقف کنید»، منبع گفت.
🔴
مذاکرات به‌طور مثبت پیش می‌رود و میانجی‌ها امیدوارند تا فردا یک توافق چارچوب یک‌صفحه‌ای را نهایی و اعلام کنند و سپس چند روز بعد مذاکرات درباره توافقی دقیق‌تر را آغاز کنند.
🔴
در حالی که پاکستان رهبری تلاش‌های میانجی‌گری را بر عهده داشته است، حمایت قطر در هفته گذشته همراه با فشار عربستان سعودی، مصر و ترکیه به کاهش اختلافات بین طرف‌ها کمک کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/122174" target="_blank">📅 23:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122173">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوری/باراک راوید از اکسیوس: امیدواریم فردا یک توافق چارچوبی بین ایران و آمریکا اعلام کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/122173" target="_blank">📅 23:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122172">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوری / هاآرتص به نقل از منابع اسرائیلی: رهبری سیاسی اسرائیل معتقد است ترامپ توافق را بر بازگشت به جنگ ترجیح می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/122172" target="_blank">📅 23:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122171">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej7IyCbp8n85FSHntqJ8y-gaMFF2goqfw0ELqo3zGn2Ehn3GPg-NPdAEvhecCfA2pBgSBMag5a3F4H_omak5a8ojaGx9Z9sOyHFAScx6A7F--GaIAINv0RadFqkCNsjJza1FY81aycT7_ZbHUw5vwgg1DYH09p1b3d3jAvQzmFI_awJMEgh2sgHWdGkGFMId1q8mvLam8AhmFQfM9IslBJv4YyW0e9mvFMog9gnhN__1nm5znkZ7zoCor2i6u1adqhVYvy1nHISXjHUPrNarsqJzxueSLGjRukm1-WB1_RgVFLo8iwXUKx_kMllcMQ7hLZ6WNswxHPhzCMg_89PWsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فایننشال تایمز: آمریکا به ژاپن درباره تأخیرهای شدید در تحویل موشک‌های تاماهاوک به دلیل جنگ با ایران هشدار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/122171" target="_blank">📅 23:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122170">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de621e16c4.mp4?token=HwaUBGLp3s6rWCgF69Z4Ugp_-_NjYggIo2C97wXJsV7d3eDf2N5T-BeHEf9tQNg_NqY5aS3LU2j9s-G9GmbfVNTR0DIrujqAlMBTjcTSYIjWSo6va9GjqYH9TQ5AUZ3NrjgRHm59ArcThV4upad3feQCK6Rm9e7l55XFPOarIIfEHs0qJaYVSApRuBgmgd8JQ7-aT3PrRN__o1LlALF9dxHcsYBEHFMYoZEpM8F6PEJciXSscekTEmkqqlNXz-vcPaOo6hHp6g47f4LVIA-9lqADrpp5-MHNGDWlBCk5iyFn3I3WrDopG4sl40REu3JWwqG6Nwt3qqAceiF28HXVcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de621e16c4.mp4?token=HwaUBGLp3s6rWCgF69Z4Ugp_-_NjYggIo2C97wXJsV7d3eDf2N5T-BeHEf9tQNg_NqY5aS3LU2j9s-G9GmbfVNTR0DIrujqAlMBTjcTSYIjWSo6va9GjqYH9TQ5AUZ3NrjgRHm59ArcThV4upad3feQCK6Rm9e7l55XFPOarIIfEHs0qJaYVSApRuBgmgd8JQ7-aT3PrRN__o1LlALF9dxHcsYBEHFMYoZEpM8F6PEJciXSscekTEmkqqlNXz-vcPaOo6hHp6g47f4LVIA-9lqADrpp5-MHNGDWlBCk5iyFn3I3WrDopG4sl40REu3JWwqG6Nwt3qqAceiF28HXVcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جلسه روزمرگی سران نظام
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/122170" target="_blank">📅 23:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122169">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک منبع اسرائیلی گزارش داد: نتانیاهو در تمام طول شب شنبه با مقامات آمریکایی در تماس بوده و انتظار می‌رود به زودی با ترامپ نیز صحبت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/122169" target="_blank">📅 23:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122168">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
نیویورک تایمز: مقام‌های ایران و آمریکا از پیشرفت در مذاکرات خبر می‌دهند، در حالی که سرنوشت آتش‌بس همچنان در هاله‌ای از ابهام قرار دارد
🔴
در شرایطی که مردم سراسر خاورمیانه خود را برای احتمال ازسرگیری درگیری‌ها آماده می‌کنند، مقام‌های دو طرف اعلام کرده‌اند نشانه‌هایی از پیشرفت و حرکت به سوی یک توافق دیده می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/122168" target="_blank">📅 23:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122165">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f9b1335f6.mp4?token=hElE_yAUAMTgNFYpB85ChnP4mdQHsiQZm7n-w-AyhlStt_oX_E1vxrAJucNIJDnFc7eFECAtgInB0chQlpFML1ENgMDgMICshYicYRLfqw9Wi1_vmfLF8jYTIvrewnWgY2MXI8sdooigtTNTYRV1M3lBsh5SQGjzQU77biLIls-YS3UHSojzzIx4_vBIgXqocVtL2VkzmopryLD11LQceJcIZSEJjszeW1K0CiTCT4QkErUsuNvY8G2wcIVVwHKEWenIRkgHsPbdEH0HyDdIbx-t2-mkkbcuc0mXylzWnW_dB5JhEzqw1bL54e1Ygwj304naPcp_9pHJn7PKKWVe_30Uswe71d8NImxGsfaeucHDTs-DOFu7wCujoXjoa3Lvsl_6BHQ7IXLlkVOh978wVfe4HMar4U8AGsEbhdpsLZ74wqBZFDxSTjCPjTur-2xlTyaGpKtHDvMziNrfWjUX2pyYDMhL1vPp8SXM2QdFP43NcUzPgEr_LIsaGGRrJIxE6BFl6Ll0ngCyQT6O0tVaMlnS70g65IYs1FSJU9Hxj3agAoYNxf9gkeTCjdLQCEODClgom5n1kPdf39sD9ASY9vLdmdsLnDslAhoGOUcEMRrz4sAJa73vSEo_TtxLWlE63QHKvdyuSRobZzbiLc8HNWPVapj29fGODnRtqsmv2Yc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f9b1335f6.mp4?token=hElE_yAUAMTgNFYpB85ChnP4mdQHsiQZm7n-w-AyhlStt_oX_E1vxrAJucNIJDnFc7eFECAtgInB0chQlpFML1ENgMDgMICshYicYRLfqw9Wi1_vmfLF8jYTIvrewnWgY2MXI8sdooigtTNTYRV1M3lBsh5SQGjzQU77biLIls-YS3UHSojzzIx4_vBIgXqocVtL2VkzmopryLD11LQceJcIZSEJjszeW1K0CiTCT4QkErUsuNvY8G2wcIVVwHKEWenIRkgHsPbdEH0HyDdIbx-t2-mkkbcuc0mXylzWnW_dB5JhEzqw1bL54e1Ygwj304naPcp_9pHJn7PKKWVe_30Uswe71d8NImxGsfaeucHDTs-DOFu7wCujoXjoa3Lvsl_6BHQ7IXLlkVOh978wVfe4HMar4U8AGsEbhdpsLZ74wqBZFDxSTjCPjTur-2xlTyaGpKtHDvMziNrfWjUX2pyYDMhL1vPp8SXM2QdFP43NcUzPgEr_LIsaGGRrJIxE6BFl6Ll0ngCyQT6O0tVaMlnS70g65IYs1FSJU9Hxj3agAoYNxf9gkeTCjdLQCEODClgom5n1kPdf39sD9ASY9vLdmdsLnDslAhoGOUcEMRrz4sAJa73vSEo_TtxLWlE63QHKvdyuSRobZzbiLc8HNWPVapj29fGODnRtqsmv2Yc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای FPV حزب‌الله به حملات خود به تجهیزات ارتش اسرائیل در جنوب لبنان ادامه می‌دهند: ویدئوی اول: یک پهپاد FPV به یک خودروی HEMTT ارتش اسرائیل در سایت خربت المناره واقع در مرز جنوبی لبنان حمله می‌کند (۵ مه)
🔴
ویدئوی دوم: یک پهپاد FPV به یک بیل مکانیکی ارتش اسرائیل در خیام حمله می‌کند (۱۵ مه)
🔴
ویدئوی سوم: یک پهپاد FPV به یک خودروی زرهی نامر ارتش اسرائیل در طیبه حمله می‌کند (۱۶ مه)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/122165" target="_blank">📅 23:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122164">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
معاون رئیس‌جمهور جی‌دی ونس، وزیر جنگ هگست، رئیس ستاد مشترک کین و کل شورای امنیت ملی توسط رئیس‌جمهور ترامپ به اتاق وضعیت کاخ سفید برای گفتگو درباره ایران احضار شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/122164" target="_blank">📅 23:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122163">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNJpjZAvNul2YmcoEuIMW2kyhzInB02_xHI5ih_yWbxjED-FI0p7KfUCTuIF0F9GILKcaCwBoDh0OQzOF3f2ikAuKyxxMygbamy8a2iRmivMBmv6ZDXgdxmRexKkIIHJVoeRSva0SynQa24MrVXwErq7i_XGOAYS_XH7P64c__7IZ-qNicx1OshSKNVwe0VpiX_Ee0CdR2bSWWnff6aogp_Lo8BrkCiSGmODYOKnhtlBN6R5N7aPnI45fFcqtEAUjzH9xeDOHLwlEuot0ioN0OuFYYZr8nUiMagyMa48W9QUlF15mAjkZBsP9wU3abOv0PV4TiZtVGIuDdLFCWapaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی گیگی
9️⃣
8️⃣
1️⃣
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
💤
این تخفیف فقط تا ۱۲ شب فعاله
💤
⭐️
@Napsternetiran_bot
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🔶
@Napsternetvirani</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/122163" target="_blank">📅 23:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122162">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
کانال عبری کان: «ساعت‌های حساس: در اسرائیل منتظرند ببینند آیا تلاش‌های دیپلماتیک فشرده، به ویژه از سوی پاکستان و قطر، به امضای یادداشت تفاهم بین ایران و ایالات متحده منجر خواهد شد یا نه.
🔴
این در حالی است که نخست‌وزیر بنیامین نتانیاهو به سمت ازسرگیری جنگ و حملات علیه ایران فشار آورده است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/122162" target="_blank">📅 23:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122161">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJgNq2aEtUlSO6i0Y3PQ9Ely3eMCa5NMtrRjsKUPe30eU1Pd7uZqoGXLPUJ7ItqeBJVKKT0pv9Of3SWTkLJaUV5L4GHsc1zGN0ZWQZ1_xZcHD1J91Afk_ko5MF2QdwHmz_2opvDhHPAabx4PP7ZFpZTTtYhqk3ezFbgwpIeFtSXmQwFEEkFxg1joJPFwXxJ7L3VKFnJr2Z7MSOvUjIKoEvS7mfTi7e_0nYY5MIk24UIFAkkESr504MobWnoHsNgoiLQr8HFRXFsGqKDrHUyCsXjMKK0wvgggzNAJBdSbRdEDaUUyKHoXBzvaOnJPBS8G5ZFEQKCMyvap4ram6c5lxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاکس نیوز:
«
شما نوک نیزه خواهید بود.»
🔴
ارتش اکنون چهار ماه زودتر از برنامه به هدف استخدامی خود در سال ۲۰۲۶ رسیده است، طبق گفته پیت هگست، وزیر جنگ.
🔴
هگستث در سخنرانی فارغ‌التحصیلی در وست پوینت اعلام کرد که ارتش چهار ماه زودتر به این نقطه عطف رسیده و گفت که این نیرو در حال آماده‌سازی برای جذب ۶۱,۵۰۰ سرباز جدید است.
🔴
این اعلامیه در حالی صورت می‌گیرد که پنتاگون با تنش‌های فزاینده جهانی و تمرکز مجدد بر آمادگی نظامی روبرو است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/122161" target="_blank">📅 23:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122160">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
کنسول جمهوری آذربایجان در تبریز بر اثر تصادف در اتوبان جلفا-تبریز جان باخت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/122160" target="_blank">📅 23:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122159">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
خبرنگار لبنانی در شبکه سه: حزب‌الله بر روی نابودکردن گنبد آهنین اسرائیل تمرکز کرده است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/122159" target="_blank">📅 23:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122158">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ادعای رویترز درباره چارچوب سه مرحله‌ای برای مذاکرات آمریکا و ایران
🔴
پایان رسمی جنگ، حل و فصل بن‌بست تنگه هرمز و باز کردن پنجره مذاکره ۳۰ روزه برای توافقی گسترده‌تر. امکان تمدید نیز وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122158" target="_blank">📅 22:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122157">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/54163ee186.mp4?token=RWtB61MH9K9h8mc-r8p9j6TV7yZtN_i1cRZ20958lxYcldFFJxmPvy5-i0eaGpLnoIHzIegVUQriEOzfzAgw1uN4qvO7bT46s9HdDjPlwfucpIUDoNpdX9cm0wEXVIlMw_O2zOW2jc90c76gEre7ZUxqWHCtunM-nj7KdBVR91l0mjpc4CicwC-RSY9Bd0UcIpiGMls3EplRLUViujC8ExmEe9Gy-s-VD-eqpurhsfq5TeclP-TLvp9N5BLdhW_VzxldPq01aB4uozemuzkbX7Q7FkJJR0ApOq0NQejCqDoCfDqgxbp0IODrxLm89sN8H7WnHlF_eo5wgI6t24V3og" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/54163ee186.mp4?token=RWtB61MH9K9h8mc-r8p9j6TV7yZtN_i1cRZ20958lxYcldFFJxmPvy5-i0eaGpLnoIHzIegVUQriEOzfzAgw1uN4qvO7bT46s9HdDjPlwfucpIUDoNpdX9cm0wEXVIlMw_O2zOW2jc90c76gEre7ZUxqWHCtunM-nj7KdBVR91l0mjpc4CicwC-RSY9Bd0UcIpiGMls3EplRLUViujC8ExmEe9Gy-s-VD-eqpurhsfq5TeclP-TLvp9N5BLdhW_VzxldPq01aB4uozemuzkbX7Q7FkJJR0ApOq0NQejCqDoCfDqgxbp0IODrxLm89sN8H7WnHlF_eo5wgI6t24V3og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از حمله پهپادی ایرانی به حزب آزادی کردستان (پاک) در استان اربیل، شمال عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122157" target="_blank">📅 22:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122156">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc07220ddc.mp4?token=iDfY3gQry3E-QAkiUyyb5tD21CU5SYqv3GmynTqF6q4durMIKDUO4ujyINTFydkgmQCzSIxdCXQhSN2_I9S7a7aa2aiCv0ho6-oNbIsp_DSY7kGxZTYhAL_cedakN332CCEX1ACtf_W8YOGzqUxSQxaujHiH-OVYfm1w6En2SHIESxnkmx-LK5C09766Ou1Ga73xVAbqkGQAXGxcp8JMhVQABF4TuQAG_DMn1xyLlXB34sSGG2hOZ8Yj8cvHmcu2EPzuW39L3f_yTKCtbNBMTb0FYsZzXV-Nzo7TMektH8HxXOPrjl3EGtZIev8yKCp1LMTH1wUdCgUJW_JdqCLA3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc07220ddc.mp4?token=iDfY3gQry3E-QAkiUyyb5tD21CU5SYqv3GmynTqF6q4durMIKDUO4ujyINTFydkgmQCzSIxdCXQhSN2_I9S7a7aa2aiCv0ho6-oNbIsp_DSY7kGxZTYhAL_cedakN332CCEX1ACtf_W8YOGzqUxSQxaujHiH-OVYfm1w6En2SHIESxnkmx-LK5C09766Ou1Ga73xVAbqkGQAXGxcp8JMhVQABF4TuQAG_DMn1xyLlXB34sSGG2hOZ8Yj8cvHmcu2EPzuW39L3f_yTKCtbNBMTb0FYsZzXV-Nzo7TMektH8HxXOPrjl3EGtZIev8yKCp1LMTH1wUdCgUJW_JdqCLA3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای ایران مواضع گروه های جدایی طلب در کردستان عراق را هدف قرار دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122156" target="_blank">📅 22:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122155">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
مکرون در تماس با ترامپ و سران خلیج فارس، خواستار راهکار دیپلماتیک و توافق با ایران شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122155" target="_blank">📅 22:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122154">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در اربیل عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/122154" target="_blank">📅 22:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122153">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4943cd2a90.mp4?token=PWr_BoxfMlmM6ypMNIaiDsnGH0dWWsXpikt_CmOSYQ5cx1YgVoxA8IsBZEBzC9v8-jav7QHMMbz_MXDhuJBE8c4Tsqv04A5HkzQIE5LFsnxQWaJfh82Sf5mx16ECFmI7QB9wEOL-ACaux0i_1T9WpnB8rF03YXYhgaW9e9uyEXgIV3LwpoVPgztmIWnlzU6i3dy0LUG2vTg-6u7bVLKDhl7Xmf6iUx8X1Ssm8OueRkhA1yjOEGUKS26pa1-29Z6oowQOEXkp88NJ5tjY4xZFs27zbu-f4aqz5T_dpdTXj2RtNqHfxq77O3bg1pIAG4czAUWYth03oAvCsWozZF86rT1usl-xtEF3YySe2AAMDbl46HIH3o3Okd5pBfjH-n96j-00pK5An0B7ttZ6BZNnKxT23GwVvaFJ5jO3aSEd_zNOffuBxI-7AfxKvplfd2F0Bu_kuhdGc8ZsLs6pPK9stjkr2nknSKT-SGipuaQl5l9YKMERKMMO0ZjbSctE-CIva6zJ1GMbiwdcbTdESh31iE2aq3fcKUPIHXeXYSVAIfLEdV9jbO8c6YWPDrbl_Ib7WSstVVRyIeqQ4WuaoTUoKo0LaSAFff69V-nRibSWsX8kflkJC232985CF6zorEirwpaf-V6PC0eby9rGFn3KAlm-e7WJUWiLBsqYlix1bkY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4943cd2a90.mp4?token=PWr_BoxfMlmM6ypMNIaiDsnGH0dWWsXpikt_CmOSYQ5cx1YgVoxA8IsBZEBzC9v8-jav7QHMMbz_MXDhuJBE8c4Tsqv04A5HkzQIE5LFsnxQWaJfh82Sf5mx16ECFmI7QB9wEOL-ACaux0i_1T9WpnB8rF03YXYhgaW9e9uyEXgIV3LwpoVPgztmIWnlzU6i3dy0LUG2vTg-6u7bVLKDhl7Xmf6iUx8X1Ssm8OueRkhA1yjOEGUKS26pa1-29Z6oowQOEXkp88NJ5tjY4xZFs27zbu-f4aqz5T_dpdTXj2RtNqHfxq77O3bg1pIAG4czAUWYth03oAvCsWozZF86rT1usl-xtEF3YySe2AAMDbl46HIH3o3Okd5pBfjH-n96j-00pK5An0B7ttZ6BZNnKxT23GwVvaFJ5jO3aSEd_zNOffuBxI-7AfxKvplfd2F0Bu_kuhdGc8ZsLs6pPK9stjkr2nknSKT-SGipuaQl5l9YKMERKMMO0ZjbSctE-CIva6zJ1GMbiwdcbTdESh31iE2aq3fcKUPIHXeXYSVAIfLEdV9jbO8c6YWPDrbl_Ib7WSstVVRyIeqQ4WuaoTUoKo0LaSAFff69V-nRibSWsX8kflkJC232985CF6zorEirwpaf-V6PC0eby9rGFn3KAlm-e7WJUWiLBsqYlix1bkY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی مجلس:
در هر توافقی ایران حتما باید غرامت جنگ را دریافت کند/ مطالبه ملت ایران است که از مدیریت تنگه هرمز عقب‌نشینی نشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/122153" target="_blank">📅 22:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122152">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
یک دیپلمات منطقه‌ای به فاکس نیوز:
«تماس سران عرب و ترامپ بسیار مثبت بود. پیشرفت خوبی در حال انجام است. رهبران منطقه از این پیشرفت که ترامپ با مذاکرات به دست آورد، حمایت کردند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122152" target="_blank">📅 22:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122151">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری / هم اکنون جلسه اضطراری امنیت ملی دولت ترامپ در اتاق جنگ کاخ سفید در حال برگزاری است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/122151" target="_blank">📅 22:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122150">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سفیر ایران در پاکستان: چند دقیقه پیش، جناب وزیر محترم کشور پاکستان، برادر عزیزم محسن نقوی، پس از بازگشت از تهران، مرا از دستاوردهای مذاکرات با مقامات کشورم مطلع کردند.
🔴
با خوش‌بینی محتاطانه می‌توان امیدوار بود که در صورت پایبندی کافی طرف مقابل، گام مثبتی در حال شکل‌گیری است که نتیجه مواضع جمهوری اسلامی ایران مبتنی بر عزت، ایستادگی نیروهای مسلح شجاع و مقاومت ملت شجاع ایران، همچنین ابتکار و تلاش‌های فداکارانه میانجی پاکستان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122150" target="_blank">📅 22:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122149">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
۷ نماینده کاندید نایب‌‌رئیسی مجلس شدند
🔴
علی نیکزاد ثمرین نماینده اردبیل
🔴
عبدالرضا مصری نماینده کرمانشاه
🔴
حسینعلی حاجی دلیگانی نماینده شاهین شهر
🔴
حمیدرضا حاجی بابایی نماینده همدان
🔴
رضا جباری نماینده مسجد سلیمان
🔴
علیرضا منادی نماینده تبریز
🔴
پیمان فلسفی نماینده تهران
🔴
انتخابات هیئت رئیسه مجلس دوشنبه این هفته برگزار خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122149" target="_blank">📅 22:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122148">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0PzAOaJ0XfpzvMClKdWmVbd0hu0TaGV50G6J1j4vEz055srVrCOBeBT5D-_anLYWScdxg6PpHzpIfZ12FiZ5xj-a5ZyQ57spX1DkdjRB-BG4AXvlHAAgytp1DYtdGRItEOb1P0R1dXI4lceMpQi9a3miuB6Im4uyeBOHMqtMvl7zaI_rs1ejOPaJihne8Xnmt2QszEnA2EYuGw7WQad-HvX5BIT_0G5FMgwtJ53mkQLWj3tlYHRKy0CeC8PdHY2VV_906YEw3Ued3mxDd2BX2Q4V1l-hbjBTn75It7Gr7HE9POXFZ9zzEeR8KIz3pdLejtVWjcA9kRAHqkcgb8NVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت قیمت تتر بعد از اخبار مذاکرات
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122148" target="_blank">📅 22:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122147">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
سی ان ان به نقل از یک منبع اسرائیلی: نتانیاهو یک نشست امنیتی محدود برای گفتگو درباره تحولات مذاکرات با ایران برگزار خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122147" target="_blank">📅 22:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122146">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
اکسیوس: معاون رئیس جمهور از اوهایو و وزیر جنگ از نیویورک برای جلسه‌ای در مورد این توافق به واشنگتن احضار شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122146" target="_blank">📅 22:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122145">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kS26UoylyETSh7kHn_8_oLe4hkiGWYkDTRt21yqOQGhldumCUvIlbezTFvMqjK1kmcmbYOKtZZJnM7f3gGRbqdo4zvL_qM8R0CeUjAn7MyL8MHUUfR-qI4qa9wNjvpP0zDrh60gT23dkxeLWqfYlaQojFj-0mItB0gJyVGpx72HsX55g1LkulRdy4WdGydTNw6gAym6sUl0TsHJStw8jOMeS-j80ZTBie4pEAitSUvC4CabkzRG3dXK3XL1ShxELQevWnfJq5-Q1dYeuV0-zqZWgSPRj138WYc9NIfnW1-T6hYtMB2RUSE_ljgOsrqeLdUv4a4ts9bTBKqO39Gn6BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احتمال توافق ایران و آمریکا صدای انتقاد سناتور لیندسی گراهام را بلند کرد!
🔴
گراهام اگر توافقی برای پایان دادن به درگیری ایران حاصل شود،زیرا اعتقاد بر این است که تنگه هرمز را نمی‌توان از تروریسم ایران محافظت کرد و ایران هنوز توانایی تخریب زیرساخت‌های اصلی نفتی خلیج فارس را دارد،در آن صورت ایران به عنوان یک نیروی مسلط که نیاز به یک راه حل دیپلماتیک دارد، تلقی خواهد شد.
🔴
این ترکیب از اینکه ایران به عنوان کشوری که توانایی ایجاد رعب و وحشت دائمی در تنگه هرمز را دارد و قادر به وارد کردن خسارات گسترده به زیرساخت‌های نفتی خلیج فارس است،یک تغییر عمده در توازن قدرت در منطقه می‌باشد.و با گذشت زمان برای اسرائیل به یک کابوس تبدیل خواهد شد.
🔴
همچنین،اگر این برداشت‌ها دقیق باشند، باعث تعجب می‌شود که چرا این جنگ آغاز شد.من شخصاً به این ایده که نمی‌توان توانایی ایجاد رعب و وحشت در تنگه هرمز را از ایران سلب کرد و منطقه نمی‌تواند از خود در برابر توانایی نظامی ایران محافظت کند، شک دارم.مهم است که این موضوع را درست درک کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/122145" target="_blank">📅 22:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122144">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
دو منبع پاکستانی به رویترز: انتظار می‌رود پاسخ آمریکا به پیشنهاد توافق فردا یکشنبه اعلام شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/122144" target="_blank">📅 22:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122143">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترامپ با سران منطقه ( رهبران عربستان، قطر، امارات، مصر، ترکیه و پاکستان) گفتگو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122143" target="_blank">📅 22:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122142">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ادعای کانال ۱۴ اسرائیل: چند منبع معتبر تأیید می‌کنند که ایران با برخی از درخواست‌های کلیدی ایالات متحده موافقت کرده است و کمتر از ۲۴ ساعت دیگر اعلام توافق انجام خواهد شد که به تهران چند ماه فرصت می‌دهد تا کاملاً تسلیم شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/122142" target="_blank">📅 22:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122141">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
بلومبرگ: ایران و پاکستان پیشنهاد بازنگری‌شده‌ای را به ایالات متحده برای پایان دادن به درگیری و بازگشایی تنگه هرمز ارسال کرده‌اند؛ دو منبع پاکستانی آگاه از مذاکرات این موضوع را به بلومبرگ گفته‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/122141" target="_blank">📅 22:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122140">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
خبرنگار الجزيرة: ۳ حمله هوایی اسرائیل به شهر دیر قانون النهر در منطقه صور در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/122140" target="_blank">📅 21:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122139">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
هم اکنون تماس تلفنی نتانیاهو و ترامپ!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/122139" target="_blank">📅 21:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122138">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
آکسیوس به گفته یک مقام آگاه آمریکایی: ترامپ هنوز تصمیم نهایی در مورد توافق با ایران نگرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/122138" target="_blank">📅 21:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122137">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری / هم اکنون جلسه اضطراری امنیت ملی دولت ترامپ در اتاق جنگ کاخ سفید در حال برگزاری است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/122137" target="_blank">📅 21:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122136">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ارتش اسرائیل: کشته شدن یک سرباز و زخمی شدن ۲ نفر در انفجار پهپاد در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/122136" target="_blank">📅 21:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122135">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام پاکستانی: نمی توان این موضوع را تمام شده دانست مگر اینکه توافق نهایی شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122135" target="_blank">📅 21:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122134">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
رئیس ستاد مشترک ارتش آمریکا، ژنرال دن کین هم اکنون تو کاخ سفید حضور داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122134" target="_blank">📅 21:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122133">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
شب قبل از حمله تقریباً تمام تیتر خبرها درباره توافق بود و حتی خود ترامپ هم از عالی پیش رفتن مذاکرات و نزدیک بودن توافق صحبت می‌کرد!
🔴
حالا باید دید این‌بار واقعاً توافقی در کار هست یا باز هم فقط بازی رسانه‌ایه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/122133" target="_blank">📅 21:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122132">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
اکسیوس : مقام آمریکایی که تو جریان مذاکره‌هاست به من گفته دولت ترامپ و ایران خیلی نزدیک شدن به یه توافق برای تموم کردن جنگ
🔴
گفته اختلاف‌های باقی‌مونده فقط سر «اینکه چند تا بند چطور نوشته بشه» هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/122132" target="_blank">📅 21:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122131">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
قطر: تماس امیر قطر با محمد بن سلمان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122131" target="_blank">📅 21:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122130">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوری / الحدث به نقل از یک منبع عالی‌رتبه: تنها ساعات کمی تا اعلام توافق بین آمریکا و ایران فاصله است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/122130" target="_blank">📅 21:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122129">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4afc1b07c.mp4?token=qS0ZWk--tK0YuuBpqxloTv2-ZSXiD5xCcK10_RP-zpCOC632ftuA7408F6n0LW-Do_SBRMNoAlA_Pysw3d7-41079BfYDROrJbmqm2wr9e0AXvSiRh-mw8Sd_n2qO9Y5jK2zsBxoaDTjESE9W9w2PEqFjVugqm2G_JKXs_5pe25HdBrlaCW606xiBGGseQ1ggRzF0vI3dxO8T2xa1TSYjLaMMT5mTcH3vtgIIIAMo3DRnQvQVPIeGiGBkZ2hI7ySkizZg9RRN8NmXaUpZl3L-5P651dp-f4jFAe0TUC0dnkofY37FlHDM69ZVkAy-_izlFNVgcdwaJeexq9zLSgX7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4afc1b07c.mp4?token=qS0ZWk--tK0YuuBpqxloTv2-ZSXiD5xCcK10_RP-zpCOC632ftuA7408F6n0LW-Do_SBRMNoAlA_Pysw3d7-41079BfYDROrJbmqm2wr9e0AXvSiRh-mw8Sd_n2qO9Y5jK2zsBxoaDTjESE9W9w2PEqFjVugqm2G_JKXs_5pe25HdBrlaCW606xiBGGseQ1ggRzF0vI3dxO8T2xa1TSYjLaMMT5mTcH3vtgIIIAMo3DRnQvQVPIeGiGBkZ2hI7ySkizZg9RRN8NmXaUpZl3L-5P651dp-f4jFAe0TUC0dnkofY37FlHDM69ZVkAy-_izlFNVgcdwaJeexq9zLSgX7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتیجه همنشینی روبیو با ترامپ
😂
🔴
روبیو: ممکنه امروز بعدا خبری بشه الان خبری برات ندارم ولی ممکنه یه خبری باشه یکم دیگه امیدوارم که باشه ولی ممکنه هم نباشه، ولی هنوز مطمئن نیستم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/122129" target="_blank">📅 21:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122128">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ در مصاحبه با کانال ۱۲ اسرائیل: اگر توافقی برای اسرائیل خوب نباشد، آن را امضا نخواهم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/122128" target="_blank">📅 21:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122127">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ce7c88a80.mp4?token=k7m8CaqfVA9IDDubaUI6EMSE89BxIDDi3wJQU8syxNYYyQfOq67uRdrF7ZR6e2LSjt5FsNY13_DJ3GNcpltoFgJV_1VI9Dk7V0vX0vR-j6SMO5Hjetv3PXZl-59tOt6ikkNJmH1SlTITo4zrV-G8hbhZiwosZpdZ2a-N0jWL8VK-g50quRGoGHk5zin9rFQSAO9wB_Q-4qbalSycWbXwVSYJiwY3M3d1XwL6GCG-0oU0h0HpvEYvnPVOTLNSrL8A1NMZ0kOT49m_m7yZkObaOSqSXDwea9TBy3MYQbkP9tXiPmtth8a9iTDGoRxVb2au4UyistogQ6gCBj7w5iUP5EnZM67tOoU7RABNVWHCNycbtlC41SCrOuFbHoAMMadDooGwuLsU1zGvp0jZqJNNw99PVfE0nsJQNW3NfCNj7wDloUspkzKHbVU6HEPXfh9NKkzepwLJGMfv8LEoTI2du9a0oCA5r22-vaUpH0a9ZxXdJ8Y-OBMs3kUmZCtXNEsRZj-jlFuz5Et81U3KSLhsZz40Kk7Cpvb7fhIEw0CVcUTAqbO7-6SmWnaVcvr5m0cffBCM0d_INW9HqnRq-nSa-IQRbpjuqaAa97oue6pmIJp_DBs0S4srUl4sasyYNd3tBattDOV8ftmJ_1VTivbvV96c07fyoyttoRV-X3yjECs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ce7c88a80.mp4?token=k7m8CaqfVA9IDDubaUI6EMSE89BxIDDi3wJQU8syxNYYyQfOq67uRdrF7ZR6e2LSjt5FsNY13_DJ3GNcpltoFgJV_1VI9Dk7V0vX0vR-j6SMO5Hjetv3PXZl-59tOt6ikkNJmH1SlTITo4zrV-G8hbhZiwosZpdZ2a-N0jWL8VK-g50quRGoGHk5zin9rFQSAO9wB_Q-4qbalSycWbXwVSYJiwY3M3d1XwL6GCG-0oU0h0HpvEYvnPVOTLNSrL8A1NMZ0kOT49m_m7yZkObaOSqSXDwea9TBy3MYQbkP9tXiPmtth8a9iTDGoRxVb2au4UyistogQ6gCBj7w5iUP5EnZM67tOoU7RABNVWHCNycbtlC41SCrOuFbHoAMMadDooGwuLsU1zGvp0jZqJNNw99PVfE0nsJQNW3NfCNj7wDloUspkzKHbVU6HEPXfh9NKkzepwLJGMfv8LEoTI2du9a0oCA5r22-vaUpH0a9ZxXdJ8Y-OBMs3kUmZCtXNEsRZj-jlFuz5Et81U3KSLhsZz40Kk7Cpvb7fhIEw0CVcUTAqbO7-6SmWnaVcvr5m0cffBCM0d_INW9HqnRq-nSa-IQRbpjuqaAa97oue6pmIJp_DBs0S4srUl4sasyYNd3tBattDOV8ftmJ_1VTivbvV96c07fyoyttoRV-X3yjECs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر جنگ پیتر هگستث
:
اولین حمله هوایی که هرگز انجام دادم و یک دسته را در وسط شب در بغداد رهبری کردم. ما ۳۶ ساعت برای آماده‌سازی داشتیم و من هر دقیقه از آن ۳۶ ساعت را صرف آماده‌سازی کردم.
🔴
وقتی خلبان‌ها ما را چند صد متر در نقطه اشتباهی در وسط یک زمین گل‌آلود فرود آوردند و GPS کار نمی‌کرد.
🔴
یک مرد بود که آن دسته به او نگاه می‌کردند و آن مرد من بودم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/122127" target="_blank">📅 21:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122126">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ادعای سازمان رادیو و تلویزیون عبری: اسرائیل سطح آماده‌باش را کاهش داده و برآوردها حاکی از عدم وقوع حمله قریب‌الوقوع به ایران است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/122126" target="_blank">📅 21:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122125">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFoww2hwkoPcXupeOtw7mzN1EQMTc7MhNXmeczC2dXkPlu1PAc7URHqpDt3nMBa3OUVueNhqXL0oUiS2UM0_SYl9apQDSnQSfw5x1UrjA4sY-Sh4JfkriBdDugpS5MjPHspCzpxIEIW90x5kTYVAJblDBeEIjWdnBYZNFJNBuhEdPi9cqrsaZGaGuBvf57SON5DzSBfJ0vp5dt-tvxZ7Wt9xfbc4DZTRyhnu9B_uq_mF798m_0ZRd1gTRjQOM8NWnsLhz8cddN49F1pK7Ia7C1_P-ZvS2TKk6YuJ0Mh6MaGES8Moz_9h06c2Lcklcaw39CgjzwlRz8qy1cAt2GHAAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی گیگی
9️⃣
8️⃣
1️⃣
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
💤
این تخفیف فقط تا ۱۲ شب فعاله
💤
⭐️
@Napsternetiran_bot
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🔶
@Napsternetvirani</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/122125" target="_blank">📅 21:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122124">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1XLJ-_zjp0f8oHbP_NUeZ4XkWROXQs9bQJugaJT4VR6z9sQUhC3j8hO-Tbxk4Cm4FKR3Ilanq_qUOUBwQFn15CQLaMxLE7QjpqNlFLhLkWiZZ8seqGHe1Ijtv-rz8HjU2AOk0TqbicnhGA1-svCjy8ppyvJIIklcFSe0vYRnxYvVG9k3t_E8v8PyApWGf5DLVRQCz34pQX8BkLeB-JjxlKswVfibnXD7L_FI3FywRTVS0UsRICm4v0tutK3xT1urh6tuD-pTfgkpRut6lU_TUDklheUWkaOii1iQ7vzsEv0SBRf-FGqiQl50v7jpDUeZ8gn4ILNTnbl3nNgHwIu1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتظار می‌رود ایالات متحده و ایران تا بعدازظهر یکشنبه توافقنامه صلحی را اعلام کنند که هدف آن پایان دادن به درگیری‌ها در تمام جبهه‌ها است، طبق گزارش واشنگتن تایمز.
🔴
پیش‌نویس پیشنهادی اوایل شنبه نهایی شد و برای تأیید نهایی به رهبران هر دو کشور ارسال گردید.
🔴
شخصیت‌های کلیدی در تأیید این پیش‌نویس شامل محمدباقر قالیباف، رئیس مجلس ایران، معاون رئیس‌جمهور جی‌دی ونس، استیو ویتکاف و جارد کوشنر بودند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/122124" target="_blank">📅 21:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122123">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
هشدارهای پهپاد در منطقه خط تقابل، شمال اسرائیل فعال هستند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/122123" target="_blank">📅 21:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122122">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: اگر آتش‌بس به مدت ۶۰ روز تمدید شود، این گام کاملا مغایر با خواسته‌ها و اهداف اسرائیل خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/122122" target="_blank">📅 20:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122121">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AabzgOicEW6KoWZWuUihkzf8sEsChcDRcBwrAdvbEIZLzCo5-wJ_HWz3ykO8fbclJW9Ese7UOhVBcQ8nxV9FQJIu0z-nxtTELPOpuyl_3-MGz_NAOPfMG75wPaR0SgnMrWQgCVjg6GghU5MSGcavZLTEdQwIoeBOyM6lDPynSqUg35gh0xTlvWW7Moov7MpSAYQtz6T3vlDpluANcMPs98doaOaDjpgJcklPmxz-Ue4UN2WnMY3OyRdCI2h88bqOy-B7DF-53l_Tp2ulo4wHg5uJCBRC5ZQjQVkqU4NNlzXOjSpXNi-CEmVI4u8X1RIzHNaVE4uhXz8YAacPirIRPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدارهای پهپاد در منطقه خط تقابل، شمال اسرائیل فعال هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/122121" target="_blank">📅 20:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122120">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c1ceeaff3.mp4?token=SxC-8qeJpjxZP0YLSIDQPlUpjfQcpu8-qUP5DyyUdLvOLSVeMiJIgDBjZpfTlWAWCDE2S93ZdFLL83HSuvmYLiunSR8jm9aVTwRVWfsaCqsnE1__OSXHJNVExKvRnhS2e3E9RV1rxDzqWECSVj6gmJheeIaTuXRvQVT3kCgQRk4weMqGBx0-EG1ErkgN3hEb2ly7sOBPI_cfYuDTmuJQanSqVIJ9FVz3nRvWT3eUOknDibs6R4PjJ7Rfm6eY4naZPrJxCzUxL_KDd9FTWlKcO1roZwZYug3S1SWk61eYT4mM3dQrd8PMGRABQw-tCXJsQOgkWCy-PufkJAPQ9pBqIY3n1V1A8fIj_sfTe3HN4Gp_J5AMbFFntxQdydv-z19fu8W4yK64RNQntd1xJvxgDchcPLDysz8FTXwmk6aTsUFMY8gM9mblnE9UB79BbDt3-5mh_n5yjwpM2ldQnJOrAyxDdvTzjEFvp49emVNO0Ijz1Kfyv-M1TIghezc0A7xvVkTDFLO01e2h9LLd8mb7iFZsuNjyv1LDyPqSS-rqcMeajY6R5bdE5D0_lzHso28-QZ0gxEbsuZIEFVKNg74UavlY6OLACF2tlU_YGXCdaeo92JMZcBHUf9CWU5HX8nfILSJUL3IE1JlGrlZOuUPltTyi4PN9SMUsv2XBql2qGgE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c1ceeaff3.mp4?token=SxC-8qeJpjxZP0YLSIDQPlUpjfQcpu8-qUP5DyyUdLvOLSVeMiJIgDBjZpfTlWAWCDE2S93ZdFLL83HSuvmYLiunSR8jm9aVTwRVWfsaCqsnE1__OSXHJNVExKvRnhS2e3E9RV1rxDzqWECSVj6gmJheeIaTuXRvQVT3kCgQRk4weMqGBx0-EG1ErkgN3hEb2ly7sOBPI_cfYuDTmuJQanSqVIJ9FVz3nRvWT3eUOknDibs6R4PjJ7Rfm6eY4naZPrJxCzUxL_KDd9FTWlKcO1roZwZYug3S1SWk61eYT4mM3dQrd8PMGRABQw-tCXJsQOgkWCy-PufkJAPQ9pBqIY3n1V1A8fIj_sfTe3HN4Gp_J5AMbFFntxQdydv-z19fu8W4yK64RNQntd1xJvxgDchcPLDysz8FTXwmk6aTsUFMY8gM9mblnE9UB79BbDt3-5mh_n5yjwpM2ldQnJOrAyxDdvTzjEFvp49emVNO0Ijz1Kfyv-M1TIghezc0A7xvVkTDFLO01e2h9LLd8mb7iFZsuNjyv1LDyPqSS-rqcMeajY6R5bdE5D0_lzHso28-QZ0gxEbsuZIEFVKNg74UavlY6OLACF2tlU_YGXCdaeo92JMZcBHUf9CWU5HX8nfILSJUL3IE1JlGrlZOuUPltTyi4PN9SMUsv2XBql2qGgE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس معاون اول رئیس‌جمهور آمریکا سفرهای خود را نیمه‌تمام گذاشته و به طور اضطراری به کاخ سفید بازگشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/122120" target="_blank">📅 20:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122119">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
لیندری گراهام، سناتور ارشد جمهوری‌خواه و دوست نزدیک دونالد ترامپ، به آکسیوس گفت که رهبران منطقه در توصیه‌های خود به دونالد ترامپ اختلاف نظر دارند و برخی از او برای ضربه زدن به ایران برای تضعیف دولتش و دستیابی به توافقی بهتر فشار می‌آورند، در حالی که برخی دیگر به همراه برخی از مشاوران ارشد کاخ سفید از او خواستند که پیشنهاد فعلی را بپذیرد.
🔴
گروه اخیر استدلال کردند که ایران توانایی تخریب زیرساخت های نفتی مهم خلیج فارس را در صورت حمله حفظ می کند و امنیت تنگه هرمز را نمی توان در برابر نفوذ ایران تضمین کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/122119" target="_blank">📅 20:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122118">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkM7xS6_b2kl2HMoZsdlC2xm6e8vqGBHnkH5CrFs-jUG8V-Y31k0OFpftdUWZeb4FS9f-4muWfvnBn32518NfiJsNFMQruwqdbnMRwLjBON2WkihQZRIlcjDJxX44PIC_54Q-pxar8gh4Y8-gE1jEryHHjC36bDfPwbDTp_8cuC6Z5-Qt3rijK2km5OXxtFjXkzqXCQLXfkCGvRNzDy17jkt8rJ3go7Ofe4Kubl04cKuRnkYR8-5ZevnnkfJ_gfM2Aq2GpfIbi-_ZLEXBc2caHao_w6Nj-T8P0f_qJBqWtGd_xIPWrlF9bTrfoM0Ed8emJ7fyMc1wyWn_1UbL4IDFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ بازنشر می‌کند:
تسلط پرزیدنت ترامپ بر بهشت برای آمریکا خوب است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/122118" target="_blank">📅 20:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122117">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rg-ivsZNZ6hl6nvoTJctEgWDsoqfLtnOYnV_7Mxf1dN-Cl0qgUSqjJ2cthZLfLQ_9n-KvAobTylGb9qn1eo2w7oOSgrSt9wSZjzhTZD2CrGVuNrRvgcZhx-ZyJ7LUvnuQ21DWJ4_uDQ3AYv4hfrFuct511jzuWc1n6e-3T9SpmWi1E8brUAJw1UlNw9hD55G2UEh9AGKopDT25sG4w5WtmO5lr5YhAYFbaPOoUc26K85fWZPBRqhQir2KN4GOox0h3w5ku041hxwQ5AxHdGnEraHyKhrjXiQdsfk5vu1Qhd1fAOmkSh509CSY4ldkEnDlyK1RIocbwLAEHT32bzn1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرزيدنت
ترامپ از اردوغان تشکر کرد که او را رهبر جهان قرن‌ها منتظر خوانده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/122117" target="_blank">📅 20:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122116">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وزارت خارجه قطر: وزیر خارجه قطر با وزیر خارجه بریتانیا در مورد تلاش‌های حمایت از میانجی‌گری پاکستان گفت‌وگو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/122116" target="_blank">📅 20:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122115">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
منبعی عالی‌رتبه به العربیه: نشانه‌ها درباره توافق بین آمریکا و ایران بسیار مثبت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/122115" target="_blank">📅 20:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122114">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
آکسیوس: دونالد ترامپ گفته است که فکر نمی‌کند بنیامین نتانیاهو نگران یک توافق احتمالی میان آمریکا و ایران باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/122114" target="_blank">📅 20:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122113">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سفارت ایالات متحده در کی‌یف هشدار داد که ممکن است در ۲۴ ساعت آینده یک حمله بزرگ‌مقیاس رخ دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/122113" target="_blank">📅 20:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122112">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
خبرنگار کانال ۱۵، یوسی یهوشوا، می‌گوید احتمال درگیری مجدد با ایران بالا است مگر اینکه یکی از طرفین انعطاف نشان دهد؛ او نسبت به گزارش‌های مربوط به یک پیشرفت بزرگ شکاک است و با توجه به حجم شایعات در ساعات اخیر، به احتیاط فراخوانده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/122112" target="_blank">📅 20:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122111">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: استیو ویتکوف، نماینده آمریکا، در تلاش است تا به هر قیمتی به یک توافق دست یابد و بر رئیس‌جمهور ترامپ فشار می‌آورد که به جنگ با ایران بازنگردد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/122111" target="_blank">📅 20:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122110">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
گویا چندتا از هواپیماهای ترابری امریکا دارن از خاورمیانه می
ر
ن!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/122110" target="_blank">📅 20:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122109">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام امنیتی پاکستانی: یک یادداشت تفاهم (MOU) در حال نهایی‌سازی برای پایان دادن به جنگ آمریکا و ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/122109" target="_blank">📅 20:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122108">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ادعای کانال ۱۳ اسرائیل: اسرائیل اطلاعاتی دریافت کرده که توافق [آمریکا] با ایران ممکن شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/122108" target="_blank">📅 20:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122107">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
صدای انفجار در استان سلیمانیه، شمال عراق، شنیده و پس از آن ستون‌هایی از دود در این منطقه مشاهده شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/122107" target="_blank">📅 20:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122106">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
آکسیوس: ترامپ امشب علاوه بر کشورهای عربی با اسرائیل هم در رابطه با پیش‌نویس توافق گفتگو خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/122106" target="_blank">📅 20:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122105">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
لیبرمن وزیر دفاع اسبق دفاع و خارجه اسرائیل: هر توافق [آمریکا] با ایران برای ما فاجعه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/122105" target="_blank">📅 20:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122104">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
گفتگوی تلفنی وزرای خارجه  ایران و عربستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/122104" target="_blank">📅 20:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122103">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
معاون رئیس‌جمهور ایالات متحده، جی‌دی ونس، به طور غیرمنتظره‌ای از سینسیناتی به واشنگتن دی‌سی بازگشته است و کاروان او در حال حرکت سریع به سمت کاخ سفید دیده شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/122103" target="_blank">📅 20:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122102">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فوری/  وزیر جنگ آمریکا: ما از نیروهای هوابرد و واکنش سریع خود خواسته‌ایم که در هر لحظه‌ای آماده اعزام به خاورمیانه باشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/122102" target="_blank">📅 20:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122101">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
آکسیوس، به نقل از مقامات اسرائیلی: نتانیاهو عمیقاً نگران توافقی است که در حال حاضر مورد بحث است
🔴
به نقل از مقامات اسرائیلی: نتانیاهو از ترامپ خواسته دور جدیدی از حملات علیه ایران را آغاز کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/122101" target="_blank">📅 20:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122100">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک منبع آگاه: بن‌بست در مذاکرات بین واشنگتن و تهران پایان یافته است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/122100" target="_blank">📅 20:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122099">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل اعلام کرد که تل آویو به دقت پیش‌نویس توافق ایالات متحده و ایران را رصد می‌کند.
🔴
تل آویو نگران است که تهران بدون حل مسائل هسته‌ای بتواند از کاهش تحریم‌ها بهره‌مند شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/122099" target="_blank">📅 20:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122098">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
قطر: در تماس تلفنی میان امیر قطر و رئیس کشور امارات تلاش‌های انجام شده برای تقویت راهکارهای سیاسی مورد بحث قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/122098" target="_blank">📅 20:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122097">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک منبع آگاه: بن‌بست در مذاکرات بین واشنگتن و تهران پایان یافته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/122097" target="_blank">📅 20:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122096">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
آسوشیتدپرس به نقل از مقامات: امیدواریم ظرف ۴۸ ساعت تصمیم نهایی در مورد یادداشت تفاهم ایران-آمریکا را بگیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/122096" target="_blank">📅 20:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122095">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
خبرگزاری آسوشیتدپرس به نقل از مقامات: واشنگتن و تهران به توافق بر سر یادداشت تفاهمی برای پایان دادن به جنگ نزدیک شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/122095" target="_blank">📅 20:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122094">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
خبرنگار الجزیره: دو حمله هوایی اسرائیل به شهرهای مفدون و کفار در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/122094" target="_blank">📅 20:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122093">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از منابع: خوش‌بینی محتاطانه نسبت به مذاکرات بین آمریکا و ایران وجود دارد و امور در مسیر مثبتی در حال حرکت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/122093" target="_blank">📅 20:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122092">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل : نتانیاهو امشب با رهبران ائتلاف دولتیش یه جلسه برگزار می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/122092" target="_blank">📅 20:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122091">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
فارس: یک منبع آگاه و نزدیک به تیم مذاکره‌کننده: آمریکایی‌ها اگرچه از رویکردهای اولیه خود عقب‌نشینی کرده‌اند اما همچنان ۳ موضوع اختلافی پابرجاست که اگر حل نشوند مذاکره انجام نخواهد شد.
🔴
اول: موضوع هسته‌ای ، ایران اعلام کرده که در این دوره وارد مذاکره درباره موضوع هسته‌ای نمی‌شود.
🔴
دوم: پول‌های بلوکه‌شده ، پول‌‌های بلوکه‌شده باید واریز شود
🔴
سوم؛ کنترل ایران بر تنگۀ هرمز؛ کشتی‌ها باید تحت مدیریت ایران و دقیقاً از مسیری که ایران تعیین می‌کند عبور کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/122091" target="_blank">📅 20:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122090">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
آکسیوس به نقل از منابع: تماس تلفنی بین ترامپ و رهبران کشورهای عربی در مورد پیش نویس توافق با ایران ساعت ۵ بعد از ظهر به وقت گرینویچ انجام خواهد شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/122090" target="_blank">📅 19:56 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
