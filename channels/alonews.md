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
<img src="https://cdn4.telesco.pe/file/sDsm_-keZKlNr-QSejrR9gTOXDRKiVP4oS_kEgmYxkv5yQ6DrIJxYLxyJw5RNNGVp2N113yJD_U1tQGuoI6phqBSQ8Q--AFGo-FpGzLKHpvrFVvF6eKjCwc5bfcXBOJu7wQ-9y-Jo1Bz1gLBw9NeHbfRe0ahU72475GOkFHgbVNEdN2PeW92HmCpRh3YGI0IgNb3h5IzXiHznyQ7uLQXe-I9pl1EIUmDLFGOI3LEsIhmuLqdix0xQWT2fA3xCXSs0wnQFuMhKfFTwyWXaM6bMuheuDumHYldqGp4sW0UACHKDpT-5LgTEVf0Uuo7DgwAERmSZXsKz0ZJvQNviV7txw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 950K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 02:56:55</div>
<hr>

<div class="tg-post" id="msg-120725">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fouF9S0NRnODqK35BwISQd8HpTw-ncxj9KaY7zzwGt7DSSMZ0AdXFFukUeFxShxkDboOucFLrJmE2Kx3DvwcZgLzq7YUtaswYPMSwE5BJf8sK3eus0kRWmJmGz2_7-tJSQj6nSr075DM7y6zcyoeyvpOElJqsDubiXdVSuiagsTdpdtQj6drRcthYWkkPiPceVMA5DJs62aMVGpmTIdvQ-mp8kstOL9Dc0IWSVaSIWKZlVgJC_pv9wolGRCMoU01C8SlbYhdXxoWZyUPrpivtF1SmARoWdEdADE6VTkpJ8Kz0UzQ0-9oNALcG-K8KaXumfG92OqsHgPbkNP9LQcDdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
💥
اینترنت آزاد و رایگان
🌐
🚫
تنها جایی که کانفیگ
رایگان
میزاره
⬇️
⬇️
@NetAazaadBot
@NetAazaadBot
⚠️
هر ساعت 100گیگ شارژ میشه، رباتو داشته باشید تا مطلع بشید</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/alonews/120725" target="_blank">📅 01:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120724">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftFk48xRUReHEjF0hBIeVNHXnVXHsAVbv2tafd8OUXNOERQrBE3teDcfYAGLpkV-hOgT2a96XUsSFwEOVNE10a8LvoxwmW_7vommlSs_GhidI2jK5Z6Ac6tHYPsGg5nuYyPpA6TuDn-0-SVC76htxDQuCVXw4zLtTFyUrE58lrhVP3guRLi0ShC49dvCCrBIF-X145U_--iokAgtaluSZ7j7mJ-g-mmwrKxEh-HF3os9twkHnOr9LoTsjzXcN7S49sHsofC1kjuuRTqXwXeyUCwrEM1lab6zTA6ROPF7VNykInqqt0WX8Xyz6anIjvJliNDBCwZSIMIqJ_AiaNwcdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست عجیب حسین دهباشی سازنده کلیپ تبلیغاتی حسن روحانی در سال ۱۳۹۶: حملات و ترورهای دشمن تا رهبری حسن روحانی ادامه خواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/120724" target="_blank">📅 01:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120723">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sg8z11rJnmV4NMh5dJZKdTL-zv7O37amvTiHl2Luq6SoQPjnveb87yg14g_eN7qBbSCZ58ThgeNBJN54lw7ezAjM9Mx84IEs_J72HXC5v7QOj65he3wlnFBvRFG5qETpJYfip9GV6DsLX1tS7OKpRA_GNGNqtuuN3tGyKExj-e54PvKqhXmDJozNjHfgxppCOuiv2MusCORIORD_dtk9HinYFhNOG-hqVf2oijSKhZtJUkyvJBAeLEy2xgcjCm5T3UANcwW93oJPI1SWwRlFmnWVEZNQXRRL3A6qEN2ExYJKXy12JpFs5qqiokeehR4GQT-sRRy07iPh7_tk7FOeqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت ایران در روز ارتباطات و روابط عمومی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/alonews/120723" target="_blank">📅 01:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120722">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سفیر ایالات متحده در سازمان ملل: هدف قرار دادن نیروگاه هسته‌ای براکه در امارات متحده عربی، تشدید تنش خطرناک و غیرقابل قبول است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/alonews/120722" target="_blank">📅 01:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120721">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9PkTQLtU8BaCkkk3yOUEVVHzrtVH011vxwQAMivAWIe6AqpUEEf_E-yFOV5hzhyOabqytcmbOocWIs9ICBVWv1vUncqi1FTt5_Occk7JWxba5cmb-_w5CgUekykzb39yn9mseo62Vt4BNgpYvut1NjdEFlsb162mVhqFIqywlhYDOjzl78aSn4rK_nBlU2KaGfsUyI5FjqPR5WAoFZ5wG3sswYVL6CAlw8dptNolRKTFwCtypc6FSCf4UDsE7XCqFk8tvjrX4f6nbFDxEqKq3qZgqY14NzJyaBIIw0jOAYU2a9OwvF85ESVByoQ_HbB7upr_lkZSFbzNNu2RBT3gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش چشم: قالیباف هَوَل مذاکره نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/120721" target="_blank">📅 01:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120720">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ بازم پست گذاشت
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/120720" target="_blank">📅 01:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120719">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ترامپ بازم پست گذاشت
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/120719" target="_blank">📅 01:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120718">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFkxezN3rVcXvoee8FtkiS8jT0wfqZfNvJ_iyiO1ox0vEzaSZ-XH77zj1O8aO1lzWvON2sqYZFIHtTjd6YoiG-KHsUrtUR30t0G3YOKKq66Obg0ft-w_4i6hDMENGy8YaovT8wohE3k_eOEd6Umxkk6SJkYy37ZeZUgUaWRxYTKbARqZIX7_IX8YcUl0hbjYbhdqk7FxE0tf0buf9cGT-dkx5pb8HxyVPNS0JnOkg4E9uQuksIKrSHzW_mBsasz_6Xf45W9JYhVp2EU0eAFrIcdtKOO29i2g4Jw-Tl0xqncveXEaYiGyT19FmDXJA54TmvAG9v46RI7TDmshxv6v_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ بازم پست گذاشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/120718" target="_blank">📅 01:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120717">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtGYQsKeGuVXnW3wlkLDFvBZC-inlq0xx-eKb7fURYEVDvv7vyMVoXPmZnkhEQnrtA-f--4cJ7iGpei4aKiLKpnp3o4Hi5Si5gCh_EWgJgFNUkRkObOd7xHpC7Rj8HmiuoN2PRyEV5ABZbqjhcwGVqBkRDVuTtTnWBesu8FZCPXxRiLBeHI_Kw8anDn50vLCpWgy7FulLz8z5h54YTUFh6MU9mXbW80Y5fbEPgTXUNavyOmKyLwOK3f5hAGINGrkHFOe9E5OVgbViaCv6pTWuGpdNy0grXzUokQrWbGOdNDxNoRKuc1edvTLMDrQnoMaPV4y00PhSqdaonEIZLIQcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ دوباره این عکس رو پست کرد
🔴
دموکرات‌ها عاشق فاضلاب هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/120717" target="_blank">📅 00:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120716">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">💢
هم اکنون تحرکات شدید ارتش ایالات متحده در منطقه
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/120716" target="_blank">📅 00:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120715">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGmnZnIKaKnpBmJ6G0XkcbXeuJxqHS0oA5sKY3V3yjXu1NxYehtrTv6GhzRvr8cSqEA9Z0U6wP1NKgRDcQb85M5UkTOFxc9diyXDZFYBc6QB3MidPYTf4_ln6ZRDLOWaBYqutAvgyAI8Os4HIrCkEDbCcOdQ2acJEmo-85JSPvcfUgXbV4s_QNlOz0Q90gKpPVzDq4gEz83A8WFRHTHAZrtUYnE-ja7dVbsmgG2MBDL7rz-caBPTRJwA_EtZMU7cfwQpekp4-SLXAAFO-P-M_5zM7BoWKHEvG0_gj-x7-8DdFFDLlPFAhXy10jC4v5Mwx62PahPjrodftZ7RzMvMTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس جمهور ترامپ به کانال 13 اسرائیل:
فکر کنم ایرانی ها باید از اتفاقاتی که الان داره میفته بترسن
🔴
اونا بايد از من بترسن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/120715" target="_blank">📅 00:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120714">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F400VktaizL1EeNY_ikKwfo5o6rw5AC27RQERDk1xFug9zKVjyLUX1ZJQTEwBSddqTLXXPhwdxaONGioqQDKTUV8wnSM1leCQSZe0UThxtYHVLGPaFNHo6xo0nWhJmxmSERkqlXWTjSR9DOb07qLqXQvWY8ehKTRruSOFE4G8jbVacYJV5nwQySuyW5gc66OFfgmjR4zL5CMgAGVY4zFYulAu0ghNoBWYQsnchVCvODaG7SnBFJ8y81qdYATnpn0v6t5h1V30IoGFM9CEmIhhEnJvEFjcX7Lt5ioUY1g1hx_iYg4D2gp_zVwqvQVjDHVWBcEug_TyorbrytyOO_HxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ بازم پست گذاشت
🔴
گفت حکیم جفریز، رهبر دموکرات‌های مجلس عقلش کمه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/120714" target="_blank">📅 00:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120713">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
خبرگزاری فارس: در صورت جنگ مجدد آمریکا و اسرائیل شانس پیروزی در مقابل ایران ندارن و دوباره شکست میخورن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/120713" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120712">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtnI2PeG-j-rf27k9ZBynpXPJ930fp874iKmvlR9IBTjWbJdj7tNtEjH-xHLes1JGGAPLJ5J2rGEpat8g152TF8OMJIEsrZJgfr5wl4M6RR2bEpltB8xzT6LTJ4WWG-tr-mV5M1Faa0GU9ghE4SzCZebQ_Bk6T6F_CRFSQNq1YMdQe_jdYHxshQ9-rWZytUUJcOQ1nWoXA5LTSNOLKcpBCWoHZXcG8jzdsj0yLC8TKvqRGkv6ajLU0xUSnL4Fx7G18dzX8ExZKEFwhiOze5_5uKzOYNaQ83-r3d0WvZMdUbnpKuTT4Cc8luOW6rq0gwC6q79G_c-pVaI54Xcj1Vr1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نروژ مرفه‌ترین کشور جهان در سال 2026
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/120712" target="_blank">📅 00:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120711">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2ecfa8c85.mp4?token=vHDaA2APAeB898Uoce3YfWRtU4RlWUn8pPblef5pYs1bahZqCHusQAxpLn6t48F7bTA_lCBtszI3i1O0U6TXnLkEPaE6S3Tv2iwGnAcpp25RddH_sCWFE25FK2pQzRdGznE-i8jyrfrPq3G7_ZZzPvmqIWj5oztMs1ihOW_-RRZWxRCShVxWiE43dm0lBiLo3xr5xDcgwLEcpX1_JGknwNbD8IgmUROIQdPEyB5Mnp1AE9ODO7FzTFKBl7G6u_AGLow0wd4HKvXf9_4OiunexgG4AArW0uo0_oeXZejdTVYM8ll0R1DOM7O19ugptuS1hOe9o2wwfIgeP2n5aOdnBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2ecfa8c85.mp4?token=vHDaA2APAeB898Uoce3YfWRtU4RlWUn8pPblef5pYs1bahZqCHusQAxpLn6t48F7bTA_lCBtszI3i1O0U6TXnLkEPaE6S3Tv2iwGnAcpp25RddH_sCWFE25FK2pQzRdGznE-i8jyrfrPq3G7_ZZzPvmqIWj5oztMs1ihOW_-RRZWxRCShVxWiE43dm0lBiLo3xr5xDcgwLEcpX1_JGknwNbD8IgmUROIQdPEyB5Mnp1AE9ODO7FzTFKBl7G6u_AGLow0wd4HKvXf9_4OiunexgG4AArW0uo0_oeXZejdTVYM8ll0R1DOM7O19ugptuS1hOe9o2wwfIgeP2n5aOdnBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بیشرفی خاصی می‌خواد به مردمی که اینجوری با دستای خالی جلوی رگبار گلوله وایسادن و 40هزار نفر در کمتر از ۴۸ساعت کشته دادن، حرف از بیضه بزنی که طبق معمول فقط از یک چپی برمیاد
🤔
حسابتون بمونه با همین مردم فردای آزادی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/120711" target="_blank">📅 00:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120703">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0ixMNDOWubmvPdPHcEjdgUam3FPPQgsmL1ztyB0AnOBfU6vtGJ0O9oINq0XynRr__2BszxcXHI38jcclNuSn6QDHPyHNqtT09aJq4Pf-e0e_0rTAoMuGS48fK8nnIz_kMImNKTDF-msdEF6-N2Q09wH9bxfPbnJTd36xvRvJVAADoLS8hTsE7-vZ8XAvUE6fv2kOVWrAzdWpNGf_TMiMtFEBfBmnZzZoFu3RU-ZcaZL4-MvEsVcdDC5v1lIpQFDxk1HpuwuZ9jRla1BkPtrM6vb3n0bAhIB3I61ls2puEvh75oJA3xGJwZFczOFhRKAm7ENJSG7YJYzpRZ5H1cLJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NG13vRr4hA3B8ceLnMfZiMGPC3WbfzEqOWHuXz7xAhEVwRoMGLUjRWKcNLlW0Qw7w1kI93Rg2P6XqK0wC8_uET5Kcka6Q15Cn1ouAF1G9oYfzOoA82jxwRx8ad4Xxo5lKh-hk3Wa9Hz-XzaBOXOa1Ude9rRana6wuLZweJXEOJIvI4mN4CY7FWoWMgFVr4i9U8R_GtYz2Qg6WtCJHRcOquNXyNQ2pM2MynrC-q8ufr9slKhZeGn8JtDusHB5HjK6IfvL8P8ubFK1BhHh4TEeya2rH3uVgi4OmUhE0Uw1cp-B87wOwSMrZIWk-1od5SKxWLNYJBf-X9716rd80eJhrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ErM2QrmvJ6_4c7Qak-O5meWpNA0LGazBP9Q6W471j-utY4YK5tXOZLMG14aRVmDVgBtTVr-xugMMTJtdl_JFKC2qOwF0H1-v7x70o64WMJuzmm4liQCNH2Gog5MqthosdFgUulZXF8mkh48Y_3WAddyUbrbxP_LgoxFVfUOkQBDDyZRSPeQpmLvOeg35aF8H17Zj5QwDdOQBNBVVcx2Msm8yY31EdpHlc0LEisyj3MxnKbXDgsz2CqneCh1EYSe3PzuaMsgIMHK1jrFOKd0syuMMP46XmDScFXctDJWgrLz07rIA8LQkCcpDYSSvNyGkaGI9h-J40qCoDGZnkeb3YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Czs2Y1s1iRaLW8kqG_myNzpF37a6WVAlRVkgwZUSwjgBDj9Pht8Ti59SJmqj9ymAN1U4HOZVM07WyMPdTvGjVFTa5spr7TJ4qcFxlbxpwtmxJTZzZZAnmYD5484puWoP0XEncp74QRUGB6Mmt1_3XsvZ8gbzcPqFS6tp4WUW-xSDbCnA5rMRRWb7-RZrvS4EMHUEbA_VIf_GR4uOlWmxLvdN_JKkaqq91fxDshadUlR0lk7e9DULYSkcFA48L3ED_S1FzHfKMLcIAVhVFr0Sr0ZjUuevgqA83PeFu3S0eknPuO5ZTa7sZrhi8iyB8Q6oqHQfujVfkvoUKzuojoA4pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lTWnIcqb7KhV5sEzt1nHKT1PvgCT2DUJlfVioAaQ9XqQrJ-3eMRw2k6nFiqf1U4JmNwSPb7-7z2F5WGc3HaG07o47pdlpdHLN5Ue3CNsvbQVAaElo1t47FctDck7k3nORuu-lvO-oG8KO7fsnJH7KcGW7aXMxstt6-r1xlOWljMrRzjeZVqLUAquFO5hOgeRZAwmevdYo5-B98UulH_i2b01gTSnZUfhW2deNQK8b4D12GbbYFWy_jg20jx9s4wkVFnkxtumClw_YDGg93b2zZ7HWaJbhcQnMctsPWAjbJNM0MweXfMyMmyz9_d2rzZpmB8SmF8OtFGCvha0MbDvkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/exFkGQwIjR-V5L69A07-LI4eh6k6Hmp7O_jibn27tll7CWXFHnwH5Kt5vK3wG33b5k0gnmqldSfO4cxxf2KH_Bziu7tkGSV0xSq_b--G2ZUI80iwVNgOVqnmMTpJ35pBB3qu48fSW3LHl1x-qCYb2WfVAAM7twcg0xDHamPcF771R3ISvkErMXskcCjuK2N_ZT7JdSbNy2tARBPA_I9lCC7ULotGvVohHRLoHmeM944c84I6CReyWH26DAVdxaBHpEOCAY1KgK3q9OmPxnkCUVkf9IVbMaH3f-8wwoLuGYm5Xg4GVbNP1plJGA9xpwR0l70AkdAJGpg_hASWcReHrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wh8YSAeX0V3hufAXpf9_k0bvlGcjCeRJ_lCfhCVdFJ3WwskomhrWqy_kBVebnl5jumxzsFyvGwv4vXfF529KzrnnTOTH33f0tPtXeYxyAkJsQPvVybBUDXORGuM-0I1rkBbpn4ZLNXWOrkGYiDZ78WJQlV3Og52zovFfkilhnKZYPpPkrLBWVzXW4nkOIkUITWWZoWWGWrbe6AAQgR9pvc8v33oyEvzVI1z7ONokKQTaKVE2OMV2LYK4Ge2NI0XfA1Yh4khNxZGNhhBjHJ7bSOK16X-J9ClOpRaqSsnPnZINOQbxL1hR3y_dAwHrDBzm_3YgkWeiRtMHccseV3bmsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QlLr79L5Tbt8F23CjRC5uaAvkKq_n4TiRWMAKLTOB1SIXyDbljPS2XU2zGio4oOkODhmANqBqtATcZPdflpNe_0F6AazGbf30KfrFMSkOfEFkxwqg-2gr6kSNrXRznQu4WMLsT_Rf64gaHjGaEdHSRj2cRD0bVGy60-74tezJZe5R9mId1ug6spS8n-FXIGzOQUg0UM1DxgeFCcfBVdRYWft-4fPicJalQuygSV30GR4sfrWNryzNeHAhlPwj-br-pbxnAGz8viUV0tJAZdT-qCVU_oar-DqNxDSsUC-Zy1rX3pkTIVUgiRfd_p7nuV87aSWkwIAO2vnVWZN8qIwXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ یهو ۸تا پست گذاشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/120703" target="_blank">📅 00:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120702">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDD_LTo3mXoQwZYEQX4rd6-2353R4VbEzj0t41Fc8_zNJIyDFponwvym9R0iQNH-wfvK5vYPvbrGtnguASR5oqjtVtOpsNcTxX-9J9-NemWuu_1gO_8UW-yYX_B27EvcmsH4NKedlooe59Wl7_jWs1Te8BbH6RW6nRC6v6F83rTD8X7fDwUFBMQmoUoO7lTJzlGlYbLkgsx3NdlxO8cp8CKC1tY9118LHOqBqlZdn4HmPu9bI_tUlX5_EbVxZGRGrc-OLI7cfhSmUDeC52grLTTy21QjIi_pDo41Y2vDoMrPmAawSjqG3mwMQca2lfm6z-DO_wxa07xFABhmm9gnJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی
:
اون دسته از مسئولینی که دلسوز کشور هستن در معرض ترور قرار دارن و نباید از موبایل استفاده کنن
🔴
مجری
:
پس چرا شما از موبایل استفاده میکنید؟
🔴
رسایی
:
😐
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/120702" target="_blank">📅 00:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120701">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سی‌ان‌ان: ترامپ به طور فزاینده‌ای نسبت به نحوه مدیریت مذاکرات دیپلماتیک از سوی تهران بی‌صبر شده و همچنان از تداوم بسته بودن تنگه هرمز و تأثیر آن بر قیمت جهانی نفت کلافه است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/120701" target="_blank">📅 00:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120700">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
سی‌ان‌ان: منبعی آگاه گفت که دونالد ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
🔴
این جلسه یک روز قبل از آن برگزار شد که ترامپ ادعا کرد تهران «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/120700" target="_blank">📅 00:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120699">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBfjxzb6ChEu-j2c7NtDY8LPQRSJXPqDtwqx1IL7N5NLH8tFfMQvRfGCfUd7LIn2z5ldv5JVNTV1ceJ4p-GpiH1iDY5ti668QJeJH-Fz2fNzKzcfpFL5GT4IDoYfNs1rSytXX8aJXLDfp1iLHC-ya_lusnzheVvgB0m2bQ9RJiw0ggh26NFmyyh9ZJieBPWG0MzQiKuBa13QPSovQzozxGPnHiPfUX4-J9xv2_bl5JL3nfBNVGLs5De0r4-BT8oLphzwRwy_iakBNCF1oiUyhU2bF5zPwfD1v5VohbUEqE_l9wK-63Lx6FbwkhNxXziz-Xi8CkKnkGvnBJtkwHFxAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌ان‌ان: منبعی آگاه گفت که دونالد ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
🔴
این جلسه یک روز قبل از آن برگزار شد که ترامپ ادعا کرد تهران «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد ماند».
🔴
به گفته این منبع، معاون رئیس‌جمهور، جی‌دی ونس، وزیر خارجه، مارکو روبیو، رئیس سیا، جان رتکلیف، و استیو ویتکاف، فرستاده ویژه، همگی در این نشست در باشگاه گلف ترامپ در ویرجینیا حضور داشتند.
🔴
این جلسه تنها ساعاتی پس از بازگشت ترامپ از سفر به چین، کشوری با روابط نزدیک با ایران، برگزار شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/120699" target="_blank">📅 00:17 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120697">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jIBDObc7xJH0XD35_uIxP_YZaC7yP--LlhksFHYfqHwHV0qn3WjWVaEas8VAvuf1kpq8pMWtlt2j8DHFdch_rCRdvMtOSWS4gXmLEtXaCwJ1pE3xwYA06Lnu96kKSJgX3grRl0jQTVkG2qDnDtk1C7JDVaU7r3277qwiozUaT5-KsFyT7_6QB8bilsc3cl2XNyeH6J4VEs8jpzOade5Qph_sgUjEItqFUp9BW5mXt2SdqzTUxgRKsfLi5VYoP50nEm2bfRLzLdNVpfNWXw_OoONiUQvlBRHkHa7CTos4uCnRsVh2KmcrchTME2dx79-LJL1uZvo8ulduln_UwCdHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33b6744dc9.mp4?token=BZhqecfTcR2XuxbRxCRAytB6v2bNpN7cAD5LsyO_BFBysvGQjBXxcdKkXcAHo8XcFwgX3NV4yr6jcfxiHl5Ov6c4rSgNJGSPu49eIxagTVNAGWL8t6TMj1ZNbTcPnJmBNV0HLzv67lrKU7-bNvtZXnzfDV3KbiWmGKY0TbecdDjpbjedZyA_qmAo_o64-vr9ig9t5dtv9SYdXtud0Wpt7btHvDwtRDEIHpcgTdvjO-aANRY7K09hN6LuJdj4pfPAshfytjv-v-yzs6kTB6v-9YW_PnKJZ-B-cZN7kpINRuiHa5JBGX2MlueTdq-p54IY7gkox3mbRycPXAex8ykSTw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33b6744dc9.mp4?token=BZhqecfTcR2XuxbRxCRAytB6v2bNpN7cAD5LsyO_BFBysvGQjBXxcdKkXcAHo8XcFwgX3NV4yr6jcfxiHl5Ov6c4rSgNJGSPu49eIxagTVNAGWL8t6TMj1ZNbTcPnJmBNV0HLzv67lrKU7-bNvtZXnzfDV3KbiWmGKY0TbecdDjpbjedZyA_qmAo_o64-vr9ig9t5dtv9SYdXtud0Wpt7btHvDwtRDEIHpcgTdvjO-aANRY7K09hN6LuJdj4pfPAshfytjv-v-yzs6kTB6v-9YW_PnKJZ-B-cZN7kpINRuiHa5JBGX2MlueTdq-p54IY7gkox3mbRycPXAex8ykSTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ و نتانیاهو ترور شدن
‼️
🔴
امشب تو پخش زنده شبکه افق، نتانیاهو و ترامپ توسط صدا و سیما ترور شدن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/120697" target="_blank">📅 00:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120696">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d3cdf36e2.mp4?token=fXh0yeAbjxPxvBZc1e0BXseTpVimhbg8PK4t9u-5m-nv7CvkI8uEO2FJs9cjmKjDeExEOUTskz9NRUueako8yvhFaG8Q1lStvXcV5oXVp_UMQttc2txblEIAhgzalhm0BD1jjTMpZhHSV1v-bUD6kMD0IhTC19I7tJOYm-B7vFx9shFbZ8_PywNCLbYi-aAkSWk0_GOBZnAAXrXJPvxnkkZXpaCxeqeKFSlJFWupo09djQpxC8jTD1Dp08UhdFfIXLN6wUZLYxSEzNQs6aw7dihi_mw6H3TfjKbpRE8NEhbgnfhCD9gMcu21XiDpZ-uNvEunlP4xu8h4CHXU5cHPTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d3cdf36e2.mp4?token=fXh0yeAbjxPxvBZc1e0BXseTpVimhbg8PK4t9u-5m-nv7CvkI8uEO2FJs9cjmKjDeExEOUTskz9NRUueako8yvhFaG8Q1lStvXcV5oXVp_UMQttc2txblEIAhgzalhm0BD1jjTMpZhHSV1v-bUD6kMD0IhTC19I7tJOYm-B7vFx9shFbZ8_PywNCLbYi-aAkSWk0_GOBZnAAXrXJPvxnkkZXpaCxeqeKFSlJFWupo09djQpxC8jTD1Dp08UhdFfIXLN6wUZLYxSEzNQs6aw7dihi_mw6H3TfjKbpRE8NEhbgnfhCD9gMcu21XiDpZ-uNvEunlP4xu8h4CHXU5cHPTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
علیه فراموشی: نیزارهای ماهشهر، در 25 آبان 98، 500 نفر توسط، عوامل سرکوب جمهوری اسلامی قتل عام شدند.
🤔
جوان مملکت جونش رو جلوی دوشکا گذاشته، بعد بهزاد فراهانی (پدر گلشیفته فراهانی) که با دیدگاه چپی داره، میگه ما بیضه اش رو داشتیم شاه رو سرنگون کردیم، شما هم اگه دارین انجام بدین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/120696" target="_blank">📅 00:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120695">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf54c97bb9.mp4?token=FRsrX1vffD4qkc_zvNhTabuks4w1f_BtFWVoDYvt2jvsabHsBwM3cGOwBm3Za8lUMZZCd1iwioM-3YGTL0A7ImlgwwxnXHyFf-E20oLpcZk0bGjstv04xAVJ-QUyvmKUxbY4VBVPLAfrbnVowGiCB3zkCERA1mRGtxJCuWytnM584WqmFW-hpqN2I6mB52hb5tH_WfOgqk2uy7usnKWTQMJXVgdsSXIcyAKgiR5tY03pHjrGEMg6K4C_9er6Dp1vIBHVdmZ1qBXI5woJv-4pVTEl5fg96e87pQ3KBZbvmGDaY36TYyKseKdQ9qd0oNThp3ozkwM_6hzNB32_tinxNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf54c97bb9.mp4?token=FRsrX1vffD4qkc_zvNhTabuks4w1f_BtFWVoDYvt2jvsabHsBwM3cGOwBm3Za8lUMZZCd1iwioM-3YGTL0A7ImlgwwxnXHyFf-E20oLpcZk0bGjstv04xAVJ-QUyvmKUxbY4VBVPLAfrbnVowGiCB3zkCERA1mRGtxJCuWytnM584WqmFW-hpqN2I6mB52hb5tH_WfOgqk2uy7usnKWTQMJXVgdsSXIcyAKgiR5tY03pHjrGEMg6K4C_9er6Dp1vIBHVdmZ1qBXI5woJv-4pVTEl5fg96e87pQ3KBZbvmGDaY36TYyKseKdQ9qd0oNThp3ozkwM_6hzNB32_tinxNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رضا پهلوی در مورد مشروعیت خود:
این برای هیچ دولت خارجی نیست که تعیین کند چه کسی باید جایگزین باشد.
🔴
باید مردم ایران تصمیم بگیرند‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/120695" target="_blank">📅 00:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120694">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
رضا پهلوی: در ده سال اول حکومت من در ایران آزاد؛ بیش از یک تریلیون دلار منفعت اقتصادی به آمریکا می رسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/120694" target="_blank">📅 00:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120693">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
مارکو روبیو، وزیرخارجه امریکا: دلیل توقف «پروژه آزادی»، این بود که پاکستان چنین درخواستی کرد. پاکستانی‌ها گفتند: «اگر شما پروژه آزادی را متوقف کنید، فکر می‌کنیم بتوانیم به یک توافق برسیم.»
🔴
ما موافقت کردیم و آن را متوقف کردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/120693" target="_blank">📅 00:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120692">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
هم اکنون گزارش CNN:
ترامپ تیم امنیت ملی ارشد خود را برای بحث در مورد ایران فراخواند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/120692" target="_blank">📅 00:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120691">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5adfd6fc37.mp4?token=iFwCJN41HeQSR-r01whZdU62zEZPtZY_Z6qvtbz32hcsRRGQ5jMq7jpptiu5DxOp8BdiaEO6ns6JmxDo0dEHzIwbL0bGAR2hB0ANUfdUNaMANqxNdfNs-wAMv56Tc7UfOEHw7cYa5epnGdIblVjT6VbB3jiJzztII4VIBwdIoJDGlhj8Mz47mo6o3LSTFTFr7lj6n-hrNhG2tB3buBPBN_UNG9z95wSISbZCd7i7-rI1tnjIhFg6V3iM3oecwXhU4jOPFn3AF0QPqzLQDvH8wDwH2_tXdS1iuff4HrejKepMWMHLU2AziKkAF7aCCelDO3-dVId9F2wwjLtAthCEaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5adfd6fc37.mp4?token=iFwCJN41HeQSR-r01whZdU62zEZPtZY_Z6qvtbz32hcsRRGQ5jMq7jpptiu5DxOp8BdiaEO6ns6JmxDo0dEHzIwbL0bGAR2hB0ANUfdUNaMANqxNdfNs-wAMv56Tc7UfOEHw7cYa5epnGdIblVjT6VbB3jiJzztII4VIBwdIoJDGlhj8Mz47mo6o3LSTFTFr7lj6n-hrNhG2tB3buBPBN_UNG9z95wSISbZCd7i7-rI1tnjIhFg6V3iM3oecwXhU4jOPFn3AF0QPqzLQDvH8wDwH2_tXdS1iuff4HrejKepMWMHLU2AziKkAF7aCCelDO3-dVId9F2wwjLtAthCEaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست جدید ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/120691" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120690">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8E5mTVgY3QQq6Vt6MOUaxp0axq9_IduPkxYyRH06Nw11Sz9pgU89ZiH_AJN8SLnCsUOg8WTJZvM8byYFDrZXXrmX7VY6RxD88p4FJe94ePbDBdLMoEqFgUxifUvWXaalvht-D1YvqnwtkvKobA5-Lq6RXBHI65Hv6MltjymeN_dKTKFYDiECKY38tuF_Deolddp08iSffp_sRq8a9Gr1qKpxZQ9CkNX77z_O0ypR92noysK8rBYDK4VlWzPCV64Gj0dULsNnSstfyO7zqifVMdJbiY2wA7aqP06Imo73bt2hDMF2MkiaDywhlpVlCgbKP0Vaoj-UDP-nqZiDWu_3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی سنتکام، «تیموثی هوکینز» به العربیه : ایران موشک‌هاشو از مناطق شلوغ و پرجمعیت شلیک کرده بود
- ما خیلی دقیق حواسمون به هر چیزی که ایرانی‌ها دارن وارد یا خارج می‌کنن هست
- توان موشکی و پهپادی ایران خیلی شدید کم شده
- توان تولید تسلیحات ایران رو هم نابود کردیم
ما تو زمان آتش‌بس با ایران دوباره مسلح شدیم و نیروهامون رو جابه‌جا و مستقر کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/120690" target="_blank">📅 23:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120689">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">📱
لطفا توییتر الونیوز رو دنبال کنین
🔴
پست های انگلیسی در رابطه با جنایت های حکومت به انگلیسی نوشته شده و افراد مهم منشن و هشتگ های مهم قرار داده شده.
🔴
ریپست کنین. مهمترین کمک این روزها جلوگیری از پروپاگاندا حکومت علیه این قتل عام مردم هستش. خونشون نباید پایمال…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/120689" target="_blank">📅 23:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120688">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0SEC5pdgZP8D-rMJ5ieJXWwEtCMBtCv07r1l5l-yHyJfVoPZiY0uLOc9aTmKVTgsm8kvUIiBMv_d7t5rIl2o52qLOWged2KDIEUPUpSYaDKkg30lT6eP9NxqCzQl8bqLGJDR4z-83H4zi0FxYb4J4faGba5KuvMrIPwqtb5WfkZV8CZDCHjUhgMuh10NEtX2-yxsRSNUcj3Ze6dkDE5lyIHNX_N5ZoaxjTFTr7qwxyDU5xRqdqcszzAAN0RSb2kJworfxCHP15HBjNRN1WJeHvVY9NcKrSGuRHu7ziH2K3Z1xXZYJp20Wawpo6HmmUnB_sLh0jyRSOVsSDIXCoQsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ترامپ لحظه شلیک مجری صداسیما به پرچم امارات را منتشر کرد و گفت خواهیم دید چه خواهد شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/120688" target="_blank">📅 23:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120687">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
وزرای خارجه ایران و فرانسه در خصوص موضوعات دوجانبه، آخرین تحولات منطقه‌ای و روندهای جاری دیپلماتیک رایزنی و تبادل نظر کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/120687" target="_blank">📅 23:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120686">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2yCBSwTvjN6oQ3Tt7CmN1fDCYf8x_y84jBm9WzjKqTZGpNWbnfB9hU7L6kmA7nI4WDbYn3ga3GKZ6F6JERhH8gd-e_i5pQU4iMhN0mxJT6eAtePp2PDckKuRUMNsDSSfAIfn9KRfg_1QE6FF5h-KpC4gbKms_z-SfJtWY0ptsKqPmP1h6DUN8fFxeWQl-v8iQEAtpprPT3oa8cXs4ffq5lP7EYX5o692MgwokBmRTKa5dNtGJZmXNpoPiU3se3kpgoHFBZVupKoT9zzMvvCpu2Q3bgTGvHHYIOMFBhjKLgT3-_fCYuDawQ8uwvRh7RJkYK2QceGqubkEMLeW3apfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال: محاصره دریایی رو میشکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/120686" target="_blank">📅 23:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120685">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سخنگوی وزارت دفاع عربستان: رهگیری ۳ فروند پهپاد که از حریم هوایی عراق آمده بودند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/120685" target="_blank">📅 23:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120684">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9guFapxHwbaIFZMg4McNz5jcyN3_fqlOVZa5-D5DAJdlIL1re1D_3V1BGy4S3I2x_Y5bfTjxp1uw6TETLibiN8XLnCidDJ0JzqB_VgALuzMovk5No_QG7FKCaygmVLr-4tjd1MvJdDssKuLIEhWY0N4UoEAH-aSlTItKpdPLXaoGrI5hqf-4tUNu3J7qxBlegCyTClpNm_NEOJkKxRfVXQl9HoHu_7NuT7iT-rb8eMzbpR8mI7U6yRf189q0yAZaCNB4Fx6FLnbq3K9BwR8TdBRtKY2MMMX-pfDIBSeqCmKxwbj9UfmXKppp6_-Bc_zT0ZH-i0rqHmuUhcMTo6IGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/120684" target="_blank">📅 23:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120683">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
کاتز، وزیر دفاع اسرائیل: به ارتش دستور دادم برای اجرای قانون اعدام تلاش کنن؛ دیگه اونایی که یهودی‌ها رو میکشن قرار نیست تو زندان‌ها راحت بمونن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/120683" target="_blank">📅 23:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120682">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
از دقایقی قبل بنابر گزارشات تایید نشده؛ صدای فعالیت پدافند در اهواز شنیده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/120682" target="_blank">📅 23:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120681">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02686941d8.mp4?token=MPRNLZ61q9VSxjLgZd2xmyTk0YOEjZTSO3DBb9qna0nEHiD_qutConvCdZqW9vJWltdyQkGV1abjcRoDqkubwT-bcU9zlgSn_J_Op0WOLUaZZWf_q-_N1Nkr0amdfxTX-fCU85zBpUDlf1mvp8vk-mFDMOAez0P3H8I2fSwAK3sQB2I8uSC2sPHuRu-v82zdnK2r9hLZZViQc-oEzrcHeo2KcR8H51862ggftXfHn4L1egCv7IQ9TuVx7f6L_-gfgr4lp-GO6IJgXNQwHybaRSjU-hHUIMuvXoRUaBukUqI4X3an1hqVP1fTP_g0KXjNgcEAeyyl9EVESnSXSwKh5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02686941d8.mp4?token=MPRNLZ61q9VSxjLgZd2xmyTk0YOEjZTSO3DBb9qna0nEHiD_qutConvCdZqW9vJWltdyQkGV1abjcRoDqkubwT-bcU9zlgSn_J_Op0WOLUaZZWf_q-_N1Nkr0amdfxTX-fCU85zBpUDlf1mvp8vk-mFDMOAez0P3H8I2fSwAK3sQB2I8uSC2sPHuRu-v82zdnK2r9hLZZViQc-oEzrcHeo2KcR8H51862ggftXfHn4L1egCv7IQ9TuVx7f6L_-gfgr4lp-GO6IJgXNQwHybaRSjU-hHUIMuvXoRUaBukUqI4X3an1hqVP1fTP_g0KXjNgcEAeyyl9EVESnSXSwKh5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقائی، سخنگوی وزارت خارجه ایران، کلیپی از فیلم The Apprentice محصول ۲۰۲۴ را منتشر کرد که بر اساس زندگی دونالد ترامپ، رئیس‌جمهور آمریکا ساخته شده است.
🔴
در این کلیپ، روی کوهن، وکیل دادگستری، به ترامپ جوان می‌گوید: «مهم نیست چقدر کتک خورده‌ای، ادعای پیروزی کن و هرگز شکست را نپذیر. می‌خواهی برنده شوی؟ این همان راه پیروزی است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/120681" target="_blank">📅 23:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120680">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51979debc7.mp4?token=HAAHMzV99WOgvnjEiU2_InjL3spZVYcIoDt3YQEUQmY8l6EJLomNPaw54hLsxBC9Pz4rmwibvRMEZ63d4i7Q4aN4_OoJdJIsEykSQ8jY6kLI8_ojpMN2UToguQBwNeuVKn2TT3b4GTlV975wv-edEkpIZjSpOyJiCnM_Jev9z1Gyz3uJmUZ_iDMH4gQ956H4Llj3cJmIsbf7j3L4oWzRO4BsBYQNl3RAFe5HLyTVjeVKcShTSTEI2eaMxY048NyE85k9b4hxKhEz224sKFCh-QbZIgZGfBbpwJ9gGL7HLaWq-4rmCM3rYk0hTILuWLxEDy8yAWk6SMitvmJ8DabIZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51979debc7.mp4?token=HAAHMzV99WOgvnjEiU2_InjL3spZVYcIoDt3YQEUQmY8l6EJLomNPaw54hLsxBC9Pz4rmwibvRMEZ63d4i7Q4aN4_OoJdJIsEykSQ8jY6kLI8_ojpMN2UToguQBwNeuVKn2TT3b4GTlV975wv-edEkpIZjSpOyJiCnM_Jev9z1Gyz3uJmUZ_iDMH4gQ956H4Llj3cJmIsbf7j3L4oWzRO4BsBYQNl3RAFe5HLyTVjeVKcShTSTEI2eaMxY048NyE85k9b4hxKhEz224sKFCh-QbZIgZGfBbpwJ9gGL7HLaWq-4rmCM3rYk0hTILuWLxEDy8yAWk6SMitvmJ8DabIZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلش ریپورت، رسانه ترک: برخورد دو جنگنده آمریکایی به یکدیگر
🔴
دو جنگنده اف/ای ۱۸ نیروی دریایی ایالات متحده در جریان یک نمایش هوایی در ایالت آیداهو، در هوا با یکدیگر برخورد کردند.
🔴
هر چهار خلبان موفق به خروج اضطراری شدند، اما هر دو جنگنده سقوط کرده و منفجر شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/120680" target="_blank">📅 23:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120679">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9ZNLc3vH3jNmNgGxOnLdzil3s7MGRFBV6ky6l15Mp1CJSSCXCxJfeCGDlzYnVIrKQFz_6SXIt7HmwXi_CJpz_RrF8Ag3LWh-9fq8TtGV2QCkoQ7kJSmoKq_HB5xFgnQK6nFS5d211pXPDcEYBl6R7qDZk8jErgyWUC1jFhYlaSAopI1YqBWgDjhs8XQG8Jgo5C-2m7qU7QjfCWVHkgD1v87rpuMrYi65faYcQVAPQQydAbRmtvHgt31hcFg6kFmNTcNl0kTNDxQUwfqmi6cToRnu_GVHTu5LT5k33kX_4QlQQ2vF0Kl7ufkHPp6RBqbWv9p8jhJ7bxKHpgdOHU8cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایندیپندنت
:
ایران می‌تواند پس از شکست عملیات «خشم حماسی» آمریکا در از بین بردن موشک‌هایش، ماه‌ها به جنگ با آمریکا ادامه دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/120679" target="_blank">📅 23:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120678">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
پرواز جنگنده‌های اسرائیلی در آسمان درعا سوریه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/120678" target="_blank">📅 23:16 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120677">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c39qf4_Woem7ANMEd2FkxgByhsCzsXypID4DYUuZH5y7_-Iaa1nwitjz-IEfTZandWGK_PnNhKj0h9HX2Y_FmFT0HYhp4ny4Ldd2lQWsWwNub4_Yj98itpZwVeoxcEkgWEExDAvPewmureuEQCvwRWOUlQNnKDUDkpgeNOnaUVUj2adGdd9gzbMoOiOzs7rtCVqR-45ISEHK2309Sx_zqhyirpfDix0sE6MFYgu0JIcYk9ff2GqV62L7FfIaLMN_m-TVg2K_2GUANaNG9YSkRhnZUnNXNpUhIaHHFjGjubDKDVutlCSf-Due_pIvozKmbDJBMxUnxF-xHeqisJZKDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: وزیر کشور پاکستان هم آمده بگه یا توافق کنید (با شرایط فعلی یعنی تسلیم) یا جنگ می‌شود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/120677" target="_blank">📅 23:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120673">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cec65a45a.mp4?token=WXQZbcNHIm6fzaqAbEQFNvZxqkTcoFpmY4FjsaBB35i4bUJMw_5zneQCr6nf2H0t7ZYtjMtCk0ZCy40OwmFYFJH_HQSQzSOT0dOgM6uK7vs-yCSn1E-fL_VUI8jHxxLZQEQiaw3h6beICP6vcRdUnYGMrHnXNyvx2tQTOOcDPXSDGmZ9JRdEWM1erY-odwgNpTizw4gHRGgBRbBLwSxvaAUq0GnDDUSDXmUZqVG454GQEIEQQ6L02Qu-IcQADuft5frOj4dIUMVuXolZ_NCCK-3veN7aJN-FsrQCYXXTr-VOsNV09TpoS_djIBKPcz0JU-Wm20rTEseD_BMAy2fyJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cec65a45a.mp4?token=WXQZbcNHIm6fzaqAbEQFNvZxqkTcoFpmY4FjsaBB35i4bUJMw_5zneQCr6nf2H0t7ZYtjMtCk0ZCy40OwmFYFJH_HQSQzSOT0dOgM6uK7vs-yCSn1E-fL_VUI8jHxxLZQEQiaw3h6beICP6vcRdUnYGMrHnXNyvx2tQTOOcDPXSDGmZ9JRdEWM1erY-odwgNpTizw4gHRGgBRbBLwSxvaAUq0GnDDUSDXmUZqVG454GQEIEQQ6L02Qu-IcQADuft5frOj4dIUMVuXolZ_NCCK-3veN7aJN-FsrQCYXXTr-VOsNV09TpoS_djIBKPcz0JU-Wm20rTEseD_BMAy2fyJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله‌های شدیدِ ارتش اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/120673" target="_blank">📅 22:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120671">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
فیلد مارشال: ابوظبی به عربستان تعلق دارد؛ امارات ابوظبی را به عربستان تحویل دهد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/120671" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120670">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
تانکر ترکرز: در روزهای اخیر، سه نفتکش خالی از محموله که تحریمهای آمریکا شامل حال آنهاست، از خط محاصره نیروی دریایی ایالات متحده عبور کرده و وارد محدوده مورد نظر شدند.
🔴
یکی از آنها سامانه AIS خود را برای مدت کوتاهی خاموش کرده بود.
🔴
دیگری پرچم روسیه را برافراشته است.
🔴
سومی نیز در امتداد خط ساحلی عمان حرکت کرد.
🔴
این سه کشتی در مجموع ظرفیت حمل ۱.۹ میلیون بشکه نفت ایران را دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/120670" target="_blank">📅 22:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120669">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
فیلد مارشال ،محسن رضایی : مقاومت ایران تغییرات ژئوپلیتیکی جهان رو سرعت داده
🔴
اتحادهای آمریکا رو ضعیف کرده و باعث تقویت روسیه و چین شده
🔴
جمهوری اسلامی الان تو موقعیت راهبردی جدیدی قرار داره
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/120669" target="_blank">📅 22:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120668">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91e63a4128.mp4?token=K5Z4j1OUANLWag6ce7KX8D_PW1LCImAyibuHXATJliyVo06O_ZeQHNi_j6shkN23hBqtslz70INL4BbFC6wDy1nTIS-LXQsRU2CzE8nZJ9BlnpuUuxEwEpsftURDr-iHcRwf7Xh8vI1ZfFh6L2AuHLpuWImItG5lZZw0z6Nq486yDVdlcM8cLFHqHI8ViKIvJ5rjTnxrTy_ramscCt7PpYm--NrWU5YV6YYKiGaUe_501L1p8d1CatHJQZhPP5709reAJhKzT2rUgv75FstO8chw059oq5rtCEWfbdG5g7sFctsAErsqQI1ANyJWbxSykF4i4ucu_ec7iYx_pT1P8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91e63a4128.mp4?token=K5Z4j1OUANLWag6ce7KX8D_PW1LCImAyibuHXATJliyVo06O_ZeQHNi_j6shkN23hBqtslz70INL4BbFC6wDy1nTIS-LXQsRU2CzE8nZJ9BlnpuUuxEwEpsftURDr-iHcRwf7Xh8vI1ZfFh6L2AuHLpuWImItG5lZZw0z6Nq486yDVdlcM8cLFHqHI8ViKIvJ5rjTnxrTy_ramscCt7PpYm--NrWU5YV6YYKiGaUe_501L1p8d1CatHJQZhPP5709reAJhKzT2rUgv75FstO8chw059oq5rtCEWfbdG5g7sFctsAErsqQI1ANyJWbxSykF4i4ucu_ec7iYx_pT1P8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیمپسون‌ها چیه ما خودمون قهوه‌تلخ‌ داریم
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/alonews/120668" target="_blank">📅 22:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120667">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
فارس: ترامپ با آزادسازی دارایی‌های بلوکه شده مخالفت کرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/120667" target="_blank">📅 22:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120666">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
فیلد مارشال ،محسن رضایی : مقاومت ایران تغییرات ژئوپلیتیکی جهان رو سرعت داده
🔴
اتحادهای آمریکا رو ضعیف کرده و باعث تقویت روسیه و چین شده
🔴
جمهوری اسلامی الان تو موقعیت راهبردی جدیدی قرار داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/120666" target="_blank">📅 22:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120665">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وال استریت ژورنال: ایران یک کشتی پشتیبانی متعلق به یک شرکت امنیتی چین را در نزدیکی تنگه هرمز توقیف کرد.
🔴
این اقدام به نظر می‌رسد نشانه‌ای باشد مبنی بر اینکه ایران حتی برای کشتی‌هایی که از طرف چین حرکت می‌کنند، اجازه حفاظت مسلحانه نمی‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/alonews/120665" target="_blank">📅 22:18 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120664">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
واکنش وزیر صمت به افزایش قیمت خودرو: با افزایش تولید و واردات خودرو آرامش به بازار برمی‌گردد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/120664" target="_blank">📅 22:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120663">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رضایی، سخنگوی کمیسیون امنیت ملی:
آمریکا شرایط ایران را بپذیرد یا منتظر پاسخ موشکی باشد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/alonews/120663" target="_blank">📅 21:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120662">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
اکسیوس به نقل از ترامپ : ما می‌خوایم توافق کنیم، ولی اونا هنوز اونجایی که ما می‌خوایم نرسیدن
🔴
یا باید کوتاه بیان، یا حسابی ضربه می‌خورن و خودشونم اینو نمی‌خوان
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/alonews/120662" target="_blank">📅 21:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120661">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XA6VE8un0OiGJetEuYzZaSwAOTx3piYivaO9Ph5GJH1OH7P-pkpMZOUah-jMYCb0664z_r0Q-8-Ntpj_CcTunaw9OhHti5CjD0QyGWYlJRJSIKZAtu39xwUSVNcp-ylflBWxxpdu44GcW3s39s1g-eu5jS3jmmG6jNynqQa1ooYLO2HHKJaNNkgcLp7_Y8G_YimJ_3fuxVSwK2IEVuH0lmUwxUrn6FuW207bAiur3qx_RO2Lf6Q-mFbG9qHY49YMiGIIJoKvpyF1v2YWKUTeoCd7jwiLN96OLmyuEqupGvVw1Zbu9J5rWussW-264Ny27Ee05VqNzwOZ0vKM7vlcAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکسیوس به نقل از ترامپ : ما می‌خوایم توافق کنیم، ولی اونا هنوز اونجایی که ما می‌خوایم نرسیدن
🔴
یا باید کوتاه بیان، یا حسابی ضربه می‌خورن و خودشونم اینو نمی‌خوان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/120661" target="_blank">📅 21:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120660">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
رئیس اتحادیه فرآورده‌های لبنی: حذف ارز ترجیحی باعث حذف لبنیات از سفره خانوار شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/120660" target="_blank">📅 21:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120659">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ادعای آکسیوس به نقل از منابع خبری در دولت آمریکا: نشست روز گذشته تیم امنیت ملی آمریکا با حضور ونس، ویتکوف، روبیو و رئیس سازمان سیا برگزار شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/120659" target="_blank">📅 21:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120658">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
کان نیوز: هرگونه حمله آینده علیه ایران که به تأیید ترامپ برسد، به‌صورت مشترک توسط نیروهای آمریکا و اسرائیل انجام خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/alonews/120658" target="_blank">📅 21:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120657">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ادعای کانال ۱۵عبری به نقل از مقامات اسرائیلی: پهپادهایی که امروز نیروگاه هسته‌ای ابوظبی را هدف قرار داده بودند، به سوی تأسیسات برق در رآکتور هدایت می‌شدند و هدف، ارسال یک پیام بوده است.
🔴
در امارات، هنوز مشخص نشده است که چه کسی این پهپادها را پرتاب کرده است: ایرانی‌ها یا حوثی‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/alonews/120657" target="_blank">📅 21:18 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120656">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وزیر امور خارجه کوبا برونو رودریگز پاریا: کوبا کشوری صلح‌طلب است، اما اگر به طور نظامی مورد حمله قرار گیرد، حق دفاع مشروع خود را تا آخرین پیامدها با حمایت گسترده مردمش اعمال خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/alonews/120656" target="_blank">📅 21:13 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120655">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
آکسیوس به نقل از مقام‌های آمریکایی گزارش داد مذاکرات با ایران به بن‌بست رسیده، اما ترامپ همچنان خواهان توافق با تهران است و در صورت رد خواسته‌هایش، گزینه نظامی را ترجیح می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/alonews/120655" target="_blank">📅 21:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120654">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
بیانیه قطر: از تلاش های دیپلماتیک پاکستان برای رسیدن به توافقی جامع حمایت میکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/120654" target="_blank">📅 20:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120653">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: در سایه شروع درگیری ها در ایران فرماندهی پشتیبانی اعلام کرد دستورالعمل‌ها عوض نشده، فعلا تا سه‌شنبه همون‌هایی که هستن معتبرن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/120653" target="_blank">📅 20:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120652">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VREKQqonXXxrMyNWnbwmV2-5q6-NWeENhDapurB1OhmKIgdZdUJgUz_Cg6JuhTKBXlulP_Q3f7OnPVedEcjMD2zYq3P70yjhM2_8cFiS6eRCUGNdNfP2o1vqxGwDv6KcGVBjkdJ7gYr3Hg18o7Y9vJehmw3xaw88ymJscPRlWGAP9fTvNqBKl3XOhS8fjhiF39WOLHbap4TWnFQtRcWshsA1xe75_Sugg7ovncwN_zlX3-8zguo9rI0fVmBbkiU9rChC6jfDIAWcgMBo9heju56oO6YZYNLHzv2ylCZvMB9i5IMouuYrKRM3Ga-sjYMymMLtm1jZlN_7CvLkdxnVgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتظار می‌رود ترامپ روز سه‌شنبه جلسه‌ای در اتاق وضعیت با تیم ارشد امنیت ملی خود برگزار کند تا گزینه‌های اقدام نظامی علیه ایران را بررسی کند، به گزارش Axios و به نقل از دو مقام آمریکایی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/alonews/120652" target="_blank">📅 20:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120651">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJhYpoUZN3hkhq8HyFBmJJmeYjfIqe0tVRyWZikkIDoX6X7-pMGPocMh7xHkRKLzfDu1IFtVeCADIvHfoyjFk5dDtyrI0wsiH7gWgS9C-l5OZgxymUCbH6MDv4fTsncH32uWx44k1BR0KRzw1iDWagw9bxKzwM4BcTZj3h91WwX3bXGj91smNi275tkUaPMGvMSCleF2pM2P9jyFQgDcQ19RSKvgdhhqqaybMHQMni2NG5OyfgqoFHKFhKzKtfDCUzwv4MsIm6CPic0QCNcYwhl777GsbnMKKIQtzzASbdduSK44-6oBSHdLlFSFcEvXJDNRZDL0jd1xk35UVGtjZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادامه رفت و آمد هواپیماهای ترابری ارتش آمریکا به خاورمیانه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/120651" target="_blank">📅 20:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120650">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-NN18Glj_ucItBG415bf-CU9vFnHRyY0LE43deSwi-Z9WGvXfNqWPhCIBhN7_42kmh8ZR2RAgrgkG1SdAPK8ekzb1uNMpubjb5zm3zjGBeo0Lzxp1kaVzVGWVhQQeXg_TbDAZiqfXQMI3FCy25lhsQ_vFEzA9jiLRNTB4yQB1ioH8MS8W-yN-EVKjTsaAit2XYbzfkOIYN1OVq_jGMemBHXA1LiR1bX2OAy4b7BDzND2wgeG973n91YP7jibsZ2O99Hx9cy0Y7gjusH6Ov3xDM3veV3UUFi-iuUFOYlP8HvjuDy3BRRKNDrEWGi4NFD4MW6LOD32uoxaO9OcX8Thg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت بعدِ پست جدید ترامپ؛ از ۱۰۵$ رسید به ۱۰۹$
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/120650" target="_blank">📅 20:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120649">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ترامپ: «منتظر یک پیشنهاد دیگر از سوی ایران هستیم، پیش از آن‌که با شدتی بی‌سابقه به آن حمله کنیم.»
🔴
ایران باید از من بترسد و مراقب باشد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/120649" target="_blank">📅 20:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120648">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سازمان ملل: ما خواهان توافق جامع بین ایران و آمریکا هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/alonews/120648" target="_blank">📅 20:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120647">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTaYe9T2ftm2IdD47XcJrE4GbWVZ3ADjuPPcc-zSBnUMyhobEJd6dNCaDHHT4weTPiSKXN6MOGSRxNkmOCNTgYCKclEi4bbWaDqNBqZMgn9NSbY1AoekdXK9JYdMDuX0hytuhAn3uK31deIsELsLKflbIzd77bj4w0XawQu7P2oKie67WaB3IeQxC31HwMDr566usoEP4xCdHeU27f4xruawiVMj9ur4hjIakZe7etnHUlWNqGUtLX19HMfPts0IP_BTVw6r5ivj9jhNeqZguNgkw3Ufe7sFyQYPVcEz3RnUZS0Ng8Q9upj8Lbar6nDcjqXDAOC6zAkNaRl1uTfSMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ترامپ از طریق Truth Social:
برای ایران، ساعت در حال تیک‌تاک است و بهتر است سریع حرکت کنند، وگرنه چیزی از آن‌ها باقی نخواهد ماند.
🔴
زمان اهمیت حیاتی دارد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/alonews/120647" target="_blank">📅 20:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120646">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
نخست‌وزیر قطر با نخست‌وزیر پاکستان درباره ایران صحبت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/120646" target="_blank">📅 20:18 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120645">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وزارت دفاع امارات: ما با ۳ فروند پهپاد که از مرزهای غربی وارد شده بودند، برخورد کرده و با دو فروند از آنها با موفقیت مقابله نمودیم.
🔴
یکی از پهپادها به یک ژنراتور برق در خارج از محیط داخلی نیروگاه هستهای براکه در منطقه الظفره اصابت کرد.
🔴
تحقیقات برای تعیین…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/120645" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120644">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وال‌ استریت ژورنال: جنگ خاورمیانه موجب بازگشت جهان به استفاده از زغال‌سنگ شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/120644" target="_blank">📅 20:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120643">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SL4nW-g1ao-sG3m_HFC4C28JCqTePSAlnfaGBimUIi9bW511CJvdLKxbhY_je2yVnF39FUWlda-ZJfm1D0zpsUGegMyM5NqLxaYbzt_Y1fwK8JTACCFrln0jIhVqv3eHhKBHIBD6JCd5zNCHGRTCCsis6i4OEvzHCqDMFiYXLKJmTi-mQP0W1N4w1hDquuKCyTj6BDEz24q2bOFmERJH569LKpzoipekc3RvhThcUiYlmrPuUarzXOo4xq1cV-IhUl_nVPXbLBOhe69faUpaLJJ0hk4H3jV-ZW8afUBRAm4pK9zheC4qQzRzeCZpC_NMXswxWmOCpf8RvM2P9JeKYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نمونه اولیه جنگنده دو نفره سوخو Su-57D روسیه برای اولین بار در آزمایش‌های زمینی مشاهده شده است.
🔴
اگر تأیید شود، این جنگنده دومین جنگنده دو نفره نسل پنجم جهان پس از Chengdu J-20S ساخته شده توسط چین خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/alonews/120643" target="_blank">📅 19:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120642">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وزارت دفاع امارات: ما با ۳ فروند پهپاد که از مرزهای غربی وارد شده بودند، برخورد کرده و با دو فروند از آنها با موفقیت مقابله نمودیم.
🔴
یکی از پهپادها به یک ژنراتور برق در خارج از محیط داخلی نیروگاه هستهای براکه در منطقه الظفره اصابت کرد.
🔴
تحقیقات برای تعیین منبع این حملات در جریان است و پس از پایان تحقیقات، تحولات جدید اطلاع‌رسانی خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/120642" target="_blank">📅 19:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120641">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ec930db1c.mp4?token=bwYtki9729J3WpNRdUaykHMHDUhp56rmAi3xBakLG3EUos2ShhIlpgAlqjGnd_7S9H14i57ba9i_OvTIbXAeHcBkgziNqzG2CRJFxbT_1Sz7gUGriOPEK-vFKmX4RBrYDIhTW6G9GOtv5unCH1Zlxtf9ioPSzNYcW-z1guO_4C3eSvGgKhQEvqOVrfFNLTNPSatevObD6grh70lx7mTx_1tECGK-EaCMa2OA1rrmwKRHVqIvYzsixmP5TvHAoykIjussLaq2zPvFcIqLTsncjApMXa6XFgWIJxOms0Qz_1lyy9zvdhk6oTm1B2Bs9tKy9j07SRZ0mieHB8q8GkfRuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ec930db1c.mp4?token=bwYtki9729J3WpNRdUaykHMHDUhp56rmAi3xBakLG3EUos2ShhIlpgAlqjGnd_7S9H14i57ba9i_OvTIbXAeHcBkgziNqzG2CRJFxbT_1Sz7gUGriOPEK-vFKmX4RBrYDIhTW6G9GOtv5unCH1Zlxtf9ioPSzNYcW-z1guO_4C3eSvGgKhQEvqOVrfFNLTNPSatevObD6grh70lx7mTx_1tECGK-EaCMa2OA1rrmwKRHVqIvYzsixmP5TvHAoykIjussLaq2zPvFcIqLTsncjApMXa6XFgWIJxOms0Qz_1lyy9zvdhk6oTm1B2Bs9tKy9j07SRZ0mieHB8q8GkfRuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله تو جنوب لبنان با پهپاد FPV به نیروهای اسرائیلی حمله کرد و زدشون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/alonews/120641" target="_blank">📅 19:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120640">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام اسرائیلی: ترامپ و نتانیاهو در تماس تلفنی پرونده ایران را بررسی کردند‌‌
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/120640" target="_blank">📅 19:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120639">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/437d8e22c8.mp4?token=oQ8FgBwJqPYk2HmlfBA2_Ag4-VQw-pavljOyKdnTH2S5yWYOFpygrV5cuNTVN86DcWRPZW20C4v3lJAKjDjd1Yd2Q0vhqOBIX0Owg6zeSUYy_SCLUv0HWKZrt1v6qNzLWuT-Ivy1YcLHAZ3AX3hufYhz4QOA5rbb4nopJon95zCKjFW2rmTWD985k9ohvxMhucY_V-nX-WUw63ZGgCfwMsD6If0a4TbNg1fZwBBsbfeVrwUEuB03BehjPwak5MmIF96D7Vy7Ew5TvNO0UQcnZ3RAd5DiBsxYmfMURC5fb52ylCwPsJg2bzga0C7XMkPYmAcZwLJhuKZWdP_HIOcDYQVxFHWU0xHjL7xyfZ6eEAlY1N3XQIQ2_D0WEtCb7s6wKOJn1h52tsUvUfh_B-M3bZq-QA_8zhvLG6pseB11FPYSSHdJcgFw0S2uV-FYQxLqVoCk3xiDRrt0uXRVw9wLa8CpkvdNKzZUqk1WYcQB4Qslg3xwSFwT8acTY1HjvynP1ZoHIhTFCLKitlL-tFwnx7wqrDE_zJkvv5wv2mtZGBHZCjqqr-nBaylFxxtyMbWRL8eELszcbCG2is4nTHYByAAZEACMvdl23sc5XhBmKWa-ORpLSRRoY4OF-oWT56v77AgGdr4jmO8-T5CyL7JjqzSBOa_ePd_Yqi8tzpY8l4c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/437d8e22c8.mp4?token=oQ8FgBwJqPYk2HmlfBA2_Ag4-VQw-pavljOyKdnTH2S5yWYOFpygrV5cuNTVN86DcWRPZW20C4v3lJAKjDjd1Yd2Q0vhqOBIX0Owg6zeSUYy_SCLUv0HWKZrt1v6qNzLWuT-Ivy1YcLHAZ3AX3hufYhz4QOA5rbb4nopJon95zCKjFW2rmTWD985k9ohvxMhucY_V-nX-WUw63ZGgCfwMsD6If0a4TbNg1fZwBBsbfeVrwUEuB03BehjPwak5MmIF96D7Vy7Ew5TvNO0UQcnZ3RAd5DiBsxYmfMURC5fb52ylCwPsJg2bzga0C7XMkPYmAcZwLJhuKZWdP_HIOcDYQVxFHWU0xHjL7xyfZ6eEAlY1N3XQIQ2_D0WEtCb7s6wKOJn1h52tsUvUfh_B-M3bZq-QA_8zhvLG6pseB11FPYSSHdJcgFw0S2uV-FYQxLqVoCk3xiDRrt0uXRVw9wLa8CpkvdNKzZUqk1WYcQB4Qslg3xwSFwT8acTY1HjvynP1ZoHIhTFCLKitlL-tFwnx7wqrDE_zJkvv5wv2mtZGBHZCjqqr-nBaylFxxtyMbWRL8eELszcbCG2is4nTHYByAAZEACMvdl23sc5XhBmKWa-ORpLSRRoY4OF-oWT56v77AgGdr4jmO8-T5CyL7JjqzSBOa_ePd_Yqi8tzpY8l4c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در ایستگاه پر کردن محصولات نفتی «سونیچنوگورسک» در روستای دوریکینو، منطقه مسکو روسیه، پس از حمله پهپادی اوکراینی در طول شب ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/120639" target="_blank">📅 19:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120637">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aHoexqdPSFAb-R58xyhgS_sRdO4noyuGbb6Sd7KU3yEhurLTXHr_8NJjCFvF6UV_01xVu0GY4UyFY0B5-5HhEWndDeJhQ-bDh1HipRwkbQdnpfkCJqNzlwdhH_OUQQUngudYla_o_FPE2rXOl0xlflulUoEcAGg4Rqnx7oS3IiCzm71VTd_HTynlPCLsJqb1Vx0KY4ZcEM4VY_V5TCsGfEPg2x8DJ_ssLqHxdlM0P3tFuuzMkJSLRnw31fWRM4ASmTBJTt2UElz_l7EzSVEGgXhF-wqLu_u7Z_RBsDz7DbXo1DBHe7ppJMOXInSVaZuAM907EvVy1V-wvMmNuWj7EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ThMO2enalqI-KldVc3XoBPyfQmIkef49ruZfWQLy1ZINZ1FaCyGdDQM_DDmRK9FlNt5h1PIryplfDKfgJD0YmgDJXuZtOsrQb6VU83DZkTMlCJsC_b-coDHjXHEvc_i_Ubu5unwHvan5TcPjBFOZoQOjMC2RkV1mU8Axz4ZzFWNpSl_w_7GOIafoBKUYM51kMaQUwCZAw6TbwzPPV340N8WPXKj-1pbx1sUx6sz83oCLgvF_pJspOFGHE6ku6_tcFNC7fNJ72nZ3B0WwMq0RFnJtvAbHVNrIuvWI-ePi50Y9s50OoAkT0xtgpugchAb8pwc8yXRzmd6ADhexPT3EfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
آنالیز تصاویر ماهواره ای نشان می دهد ناو هواپیمابر آبراهام لینکلن در فاصله ۲۴۵ کیلومتری از ساحل ایران مستقر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/120637" target="_blank">📅 19:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120636">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
شهباز شریف: امیدواریم دور دیگری از مذاکرات ایران و آمریکا را میزبانی کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/120636" target="_blank">📅 19:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120635">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
کانال ۱۲ عبری: تخمین اسرائیلی‌ها این است که آمریکا در طول این هفته به جنگ علیه ایران بازخواهد گشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/120635" target="_blank">📅 19:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120634">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
گفت‌وگوی تلفنی وزرای امور خارجه ایران و قطر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/alonews/120634" target="_blank">📅 19:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120633">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahOADv8dfcMG3tPj_RuwXTST5EbCca4gknYzV1_Hd7d_jTcmb-rMVKnB830Nb4tZK0kX_cKLRDRc9rcBTcdGSE8HGeCgdxZiW1tg3WOR5x6XXXo0CXdlEJH6VaHiCCUp6xsfrBYbA4tcEcBri4JBI_A3UTXR_0ag-4HwGoSHuYx6MtTtaxu7TKjG6AtL4H4_4yXFcfRn2k7hSVgrWCDwWISfBm7r0YI9v443KblAqrP56tCpNB92TFsC3z8jp3wkAhSZIXahezfX8l6sihd0gLiWTMUKc4_dYp7jIfM0CCAzXjEmVOtQUAoFdBtcpifihEIAO8TcMN0fhcDOkDZQvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام اسرائیلی: ترامپ و نتانیاهو در تماس تلفنی پرونده ایران را بررسی کردند‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/alonews/120633" target="_blank">📅 19:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120632">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
الجزیره: هشدار ارتش اسرائیل برای تخلیه روستاهای سحمر در بقاع غربی و رومینه، قصیبه، کفرهونه و بنافول در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/120632" target="_blank">📅 19:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120631">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFlPtI1_PDRnmh3h_4rCIwM7mpBG8HODuK8DjS4yYyUfEPxokmdQOfXL7skjwf3syisRXLW1RPDC62hkNDN3j7E9Sk6fn4AzTUPYh_OYkFizHlVYU7NP8YJUwafUkj94lUYfsTnYhLeRthoN9UCtL_qkXA-EiKsDvdyVmbboDoXr6zjSHJusQeMlVJma60pPno4Ee29qJacILdIWD9MQ7mbwJ7zmQm9arwFsg_FOjMoaxFndzQYlp1kC9XKgUvTQT0vjikHao4oqWhG_nDI29ZDYTyv1K4BwEUdSdE3Hyw85P1O4Gr_V__Gq3MYTBvK_uL0RXMmgD713hQgiGUCnAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
به درخواست شما تمدید شد
🚨
🚨
قیمت استثنایی گیگی
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/120631" target="_blank">📅 19:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120630">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3494a163d.mp4?token=ATnqcDe9sKeaGxFlNiaFgVL2OUgwcqqvgbGr8xVNPerZ2G5VDZUB-2NXcfgnQiQlg55uCbVAyloio1Jm1cBy_6CFLHpeWBDWY512qSBraAVsKc263Znzqe4E3zr5uveWRbZCWrtlzPBJ1Gh27-AhEYGfpT62dOiI1c3az6RwYdJvqDd4-eWW5sbgx-sjIvXvrWXx_65kc6oNUT6DXlPmZzGepSe3apHzAm2VZAHbY_C_oyZ50KEjOINyDJpspm_JVBLTKA-QOQc36q3UB1jakaGSXMvCLqa-6rq7J9aADzLnHRLHGwl5AZYOVsTeJJfN2timy1XdITd_9VeNrVcVAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3494a163d.mp4?token=ATnqcDe9sKeaGxFlNiaFgVL2OUgwcqqvgbGr8xVNPerZ2G5VDZUB-2NXcfgnQiQlg55uCbVAyloio1Jm1cBy_6CFLHpeWBDWY512qSBraAVsKc263Znzqe4E3zr5uveWRbZCWrtlzPBJ1Gh27-AhEYGfpT62dOiI1c3az6RwYdJvqDd4-eWW5sbgx-sjIvXvrWXx_65kc6oNUT6DXlPmZzGepSe3apHzAm2VZAHbY_C_oyZ50KEjOINyDJpspm_JVBLTKA-QOQc36q3UB1jakaGSXMvCLqa-6rq7J9aADzLnHRLHGwl5AZYOVsTeJJfN2timy1XdITd_9VeNrVcVAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریستن ولکر: آیا ارزش از دست دادن انتخابات میان دوره ای را دارد اگر نتیجه یک ایران غیر هسته ای باشد ؟
🔴
ارزش از دست دادن شغلم رو داره اگر مجبور بودم کارم را رها کنم تا مطمئن شوم ایران هرگز سلاح هسته ای نخواهد داشت ، این کار را می کردم.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/120630" target="_blank">📅 18:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120629">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
وزیر کشور پاکستان: پاکستانی‌ها شبانه‌روز برای موفقیت دولت و ملت ایران دعا می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/120629" target="_blank">📅 18:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120628">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=IkNfFI_j0Yf3Pyjw-Jk5n_d22u70Z5NNDUDnUEA7NxhzFnBBN3TaZpQE4zojv0cPGIJ_QJhudT_fACKwCdBhg8ZMEMRKq6fQ8XwNkX0iBbTvcyUWc-MPE_-hpTVx6Zx8aqX1KcH9AGHav9poIS3OLDHcoVp5KdyYeLwSXCf04hjo10lugDsqziH2XqX0GhSQv8ql7EB32JAxNv74yqshXpEIXPfhuVCcAf7ZfAJ8ttCWcjUPFQyzhJsp6cq3S6emReG1Kn9QJM_FvIgbmcklMNBJnDgv7X1TEmhWCTdOhKZVRB714_VyRO-t9a4_aRFkA4R4InpbGwckdfdskbSN8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=IkNfFI_j0Yf3Pyjw-Jk5n_d22u70Z5NNDUDnUEA7NxhzFnBBN3TaZpQE4zojv0cPGIJ_QJhudT_fACKwCdBhg8ZMEMRKq6fQ8XwNkX0iBbTvcyUWc-MPE_-hpTVx6Zx8aqX1KcH9AGHav9poIS3OLDHcoVp5KdyYeLwSXCf04hjo10lugDsqziH2XqX0GhSQv8ql7EB32JAxNv74yqshXpEIXPfhuVCcAf7ZfAJ8ttCWcjUPFQyzhJsp6cq3S6emReG1Kn9QJM_FvIgbmcklMNBJnDgv7X1TEmhWCTdOhKZVRB714_VyRO-t9a4_aRFkA4R4InpbGwckdfdskbSN8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور گراهام درباره ایران:
هر قیمتی که لازم باشد بپردازیم، خواهیم پرداخت.
چرچیل چه گفت؟ «هر قیمتی که لازم باشد برای شکست هیتلر بپردازیم، خواهیم پرداخت.»
همین موضوع درباره ایران هم صدق می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/120628" target="_blank">📅 18:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120627">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3706aba91d.mp4?token=p4JAdS5-584oUQpIgtKxpXL1hARelHVoR0SV9TYqF_hf44hMkItuKVSvKvDYltx6UQr-clgRuM5xS0Z3C9tSHGcDTmjqhZklQz64t5U5Vaaeu2imJdI1X5tv8Z9NWlGA6nYHBTnNiGAgGj0MKL-qzfjTQZ-qnkDMx127tpjYsDcslEWouY6UVn_2lfXz0lm1OTqghhl8vbkRPDgNXm36BujJIuajtM-PlAZejcNw01d8sQjeMFE1GSD_UEbiRaT9owt38mIA85WJXzNVtdXCwlU2AtOOIlTjUyl3dGUsT8Z-lFGcG47W3DoXUJf6L8IInXp1RGHCaktoVW9Zf1UrVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3706aba91d.mp4?token=p4JAdS5-584oUQpIgtKxpXL1hARelHVoR0SV9TYqF_hf44hMkItuKVSvKvDYltx6UQr-clgRuM5xS0Z3C9tSHGcDTmjqhZklQz64t5U5Vaaeu2imJdI1X5tv8Z9NWlGA6nYHBTnNiGAgGj0MKL-qzfjTQZ-qnkDMx127tpjYsDcslEWouY6UVn_2lfXz0lm1OTqghhl8vbkRPDgNXm36BujJIuajtM-PlAZejcNw01d8sQjeMFE1GSD_UEbiRaT9owt38mIA85WJXzNVtdXCwlU2AtOOIlTjUyl3dGUsT8Z-lFGcG47W3DoXUJf6L8IInXp1RGHCaktoVW9Zf1UrVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور گراهام درباره ایران:
بر اساس تحلیل من، هیچ چیزی نشان نمی‌دهد که افرادی که اکنون در قدرت هستند با قبل متفاوت باشند — آنها هنوز هم می‌خواهند جهان را ترور کنند، اسرائیل را نابود کنند و به ما حمله کنند.
پس شما باید آنها را بیشتر تضعیف کنید. کاری که رئیس‌جمهور ترامپ انجام داده از نظر نظامی شگفت‌انگیز بوده است. زیرساخت‌های انرژی نقطه ضعف آنهاست. وقتی به مبارزه برمی‌گردیم، انرژی را در صدر فهرست قرار می‌دهم.
من خواستار آسیب رساندن به این رژیم هستم. بیشتر به آنها آسیب بزنید، شاید آنها معامله‌ای انجام دهند. اما در حال حاضر فکر می‌کنم آنها سعی دارند این وضعیت را تحمل کنند و بازی می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/120627" target="_blank">📅 18:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120626">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJRGNjBuyMiowlaWXkMZc02t2HYdi-GBNCiTIxZUYx7bKVgnMOu5vIh0ezFdcjk0zKIRDw9fbuQevNGS7PXEj3EUR667ewDLyhDkAEbAEH78HMUHe55vjHZsw21nW8LCp707F8dYtmjQRv_ksO6vbUJKonPVbbAdKxNFNcV7EKFoU5dc3BAxRo4FYTZbIhxSFdWTSCy40IOqQhz54KALCN8CBPjlU0xbXGhdvp9uXrqPiSNeoL6RenOaPmjM_ZagJ7bxGnl20thY0pjIeWq2X6RBj8azDDdrEFcGnY1xKRjTiooxCII8KiEyNu0m0LjdDFW6hWmTvgztJmGTcWOM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگارای کاخ سفید رو صدا زدن که برن تو محوطه جنوبی کاخ سفید واسه یه "رویداد نامعلوم"
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/120626" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120625">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AK63fd7XaSXu_xDkxPyShalIJUVpJLHZnDBPzXG_W-1gz7bXLOs3K4B3oMw8bOlw0mne-_Ei_ablS83oHElAKXzYa-MOETRpvaZ1z8M2IE26-87lBH55_OQNiojJuDHULjzElLi8OL6Ff_w6oZFeMJxLRWjQ6NQ8oKDswGl1OtKGFbNVu1p4eQlWRR0g5A5R-7RPus-ZWHzBh845JY7zHoz6lcq1yEm7Nsu2F2xqLnpCHyudB6QVoQ632XpxEgKPp6enAaIEXg-zqw_CErkIsEexa4Xa5RV-WOTKCS237RKCfdRL4419fFHoHvndhf4dKUt09tiaGn1ANhGAFXDIHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بنرهایی که سپاه تو ساحل تنگه هرمز نصب کرده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/120625" target="_blank">📅 18:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120624">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82a4f48946.mp4?token=gxXbeTR8ovspbWSt-wJoPmYWjeomP6fbZZeshIuKYDiF3485P5PIbByw3kHIvI6Q-ppwlJLU8aMoJagXwCx1mXP2-bORAfiowzwafDkc6B9EA7l--mrs6v1G2MAdT3uyBDrqIbauD6SUTG6ZPGcM5QHf73q37r0R66PV-6XeYbfh_SgxqhZ6fb7twWhGOlbYwoh7kvd56jOuNOISTGcwYztCYhnE7zjpmicIrY8A-bXJsppzgxCO8SeCbkVnLBxZu8HeNgUihDPxo-MbY-mN-8tm7Sd1YmMlhN8l1OTxQInpN3PqGKxLEbCdh7hqyF0u13ZRGQ3Z0f196ZM4LblKeg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82a4f48946.mp4?token=gxXbeTR8ovspbWSt-wJoPmYWjeomP6fbZZeshIuKYDiF3485P5PIbByw3kHIvI6Q-ppwlJLU8aMoJagXwCx1mXP2-bORAfiowzwafDkc6B9EA7l--mrs6v1G2MAdT3uyBDrqIbauD6SUTG6ZPGcM5QHf73q37r0R66PV-6XeYbfh_SgxqhZ6fb7twWhGOlbYwoh7kvd56jOuNOISTGcwYztCYhnE7zjpmicIrY8A-bXJsppzgxCO8SeCbkVnLBxZu8HeNgUihDPxo-MbY-mN-8tm7Sd1YmMlhN8l1OTxQInpN3PqGKxLEbCdh7hqyF0u13ZRGQ3Z0f196ZM4LblKeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جلسه دادگاه ساعدی نیا، مدیر کافه زنجیره ای معروف ساعدی نیا به دلیل حمایت از اعتراضات دی برگزار شد.
ساعدی نیا: من بلاتکلیف بودم تا اینکه استوری گذاشتم و مغازه رو تعطیل کردم، بعدش از ترس استوری رو پاک کردم و موبایلمو خاموش کردم، من هیچکسو به حضور در اعتراضات ترغیب نکردم.
منظور من از فروپاشی، فروپاشی اقتصادی بود و نه خیزش علیه نظام. من هیچکدوم از کارکنانم رو برای حضور در اعتراضات مجبور نکردم، از کاری که کردم پشیمونم و از دادگاه می‌خوام فرصت جبران بهم بده.
قاضی: شما با فراخوانی که دادی کلی جوون رو به اعتراضات کشوندین و ضربه زیادی به این نظام زدی، چطوری میخوای جبران کنی؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/120624" target="_blank">📅 18:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120623">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
رئیس مجلس نمایندگان آمریکا:
عملیات «خشم حماسی» به پایان رسیده است و آمریکا در صدد اجرای پروژه‌ای برای بازگشایی مجدد تنگه هرمز است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/120623" target="_blank">📅 18:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120622">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtD6d4_UnUI5yFODN6g5KNAAVLM8DF9SHCYeSTWTzUPZBilTu5MmpAgftsKY6AKVL7sDH8nSSMW-50lc_HwLa9NghtmGckqO2aPxAkU4KFvSjs-yn-YCyQ8udxC3OIG0a-6-NjgxPLVddYT7CukXF--pDwN5Uhvwns-PMHn98y1cCqmxhXPYr4nj6uxeoAottsJ6sAbJXLkGCVcUycJW41eJSD-A4jByTCQbcoXIQqpMDA5vr3pbKdqYQK1EFoMDue7gjaKGjmnxaPFZdADEvC549-VpTqhtwa_qS-vUqAjN8CujTSamgLyU0NeowpxduJ_puJ73Yhr561M96S7F2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇮🇷
شانس قهرمانی ایران در جام‌جهانی چقدر است؟
سایت گل با انتشار پوستری درصد شانس قهرمانی کشورهای حاضر در جام‌جهانی را مشخص کرد.
@AloSport</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/120622" target="_blank">📅 18:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120621">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGAWlkBfcu51HFtvrUfm4DrSmACrNNENhgOI5Fj5zR26kaQc37QUUSypL75A6lYyl0LCvKH6r71A5q8gzh-LyVZEcb7sy2lm9jBQalgeZXHxB_D6R6DRnxZZpH5LVcOEO-V0VbtvLsMQYX-oFlhc0kkzQru9XGdonzzsm1ulKrQDcmNJ8axYvWXFNIj4RhlMDC-e3cvaoR6mw_SGXothU0iRrmUKMnoiS6aEPrqA4-de9uFcFzdVaInqXwsMDpstVOdSwZ1_OSDshT0Ssw7-9r5GMZq72TLEU7omyUmjBqWgbH6z9BO5x3GdBS7uls6mB9sTNWZ16H_VrAWwmCaAdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فووووووووووووووووووری</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/120621" target="_blank">📅 17:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120620">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
فووووووووووووووووووری</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/120620" target="_blank">📅 17:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120619">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOzygS4903m-S4JWx1MdbcEWIeu8s9FUSH7hys1enNbCqS_jWLwiB7INt9RB0e6pNrbb1dCYWGdsqVTrOTSyincY43ufHS1ljocFDOEoZM5ZTUscwGil79llks_ex70h8-jPuKL7Mdm7S-ZsPLXVkbErV4oQteHZMgOJ48EP2qBF_kzwNn0puJJIVXx8z0LevpG86-ki9DggaqHGti8S3woPffFh1s_56ohQV6YoG6z6R_Id3vYA3hG-opkE3XfAnYFqySuw1luFR3Auc8i0TqvsI3Xxl-DwOc6FPKaJt5M1b_HfLKGjF3O-tMVldiBcQyxJEbqFrqHphI-D9PnjVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: تا امروز ۸۱کشتی تجاری را برگرداندیم و ۴کشتی را توقیف کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/120619" target="_blank">📅 17:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120618">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvD4cXjPAOaOlEXaIb5T72u3kuy6AVI1msfBisCmU3rICcCKcy3U8vLCvPZzNW1CHC7fZht11gaDEk5Zf4gDlsO300J5Z1GJlpfyXpoaz6wGZrcF-qPgDapnafskkWota80-xWN7z8Gzl7bz38jA280-am8dPfJnts0htssgzJ0ZuwUuY6gENCLgEmZMu_yclK-JOTQCzDKazwnxzY0MIKaG-YTFyC1VgPfC0W-HTlEj64SAhzBt6kx__lTU2dwOu_O7dtHAobyZC2ih1oC0dz14Nv1jMYKrWEx3fl0r_Dj3ok21qmOo5oah_xwfaTAI6zFctwZz2PaLNBkC0QlvQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای ویژه C-40 Clipper نیروی دریایی ایالات متحده که از یونان حرکت کرده بود
🔴
دقایقی پیش در پایگاه هوایی شاهزاده سلطان در عربستان سعودی فرود آمده است
🔴
هواپیما حامل چندین ژنرال ارشد ارتش آمریکا می‌باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/120618" target="_blank">📅 17:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120617">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/840e1333c8.mp4?token=TN06UYMqlmELM66kK6ZSCQ31n6FzFgdPbTeEd3e5MoxVH7ielC505Rryn6O9UmaTecnPJS7RM93cU4MYbj1g10o4C6G_ek2s00GXCz0XBFXv7vJMlRR2juD1FOc-iTvMrZncxgJqlrGb-Jog4P2F8VZBpArSzH-Rn2dcLiNyCfzJTnL31bnuOqSh9sR61M88PDKqrc_DDIi5aO5WBTCtOyo8s2Fdlt4WU2KyuDLLzPrnZkhLJSH7ORqzK0V_JyxNPEIAHFhjfeCoO_21IxRfr47wiVh8phG5Xbf4FEvL2q_TH3zN5_FE7q43kB8R86gyKcqITMbtzMAuSnJM3VhfjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/840e1333c8.mp4?token=TN06UYMqlmELM66kK6ZSCQ31n6FzFgdPbTeEd3e5MoxVH7ielC505Rryn6O9UmaTecnPJS7RM93cU4MYbj1g10o4C6G_ek2s00GXCz0XBFXv7vJMlRR2juD1FOc-iTvMrZncxgJqlrGb-Jog4P2F8VZBpArSzH-Rn2dcLiNyCfzJTnL31bnuOqSh9sR61M88PDKqrc_DDIi5aO5WBTCtOyo8s2Fdlt4WU2KyuDLLzPrnZkhLJSH7ORqzK0V_JyxNPEIAHFhjfeCoO_21IxRfr47wiVh8phG5Xbf4FEvL2q_TH3zN5_FE7q43kB8R86gyKcqITMbtzMAuSnJM3VhfjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات هوایی گسترده اسرائیل به شوکین در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/120617" target="_blank">📅 17:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120616">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وزارت دفاع امارات: یکی از پهپادها به یک ژنراتور در خارج از محدوده داخلی نیروگاه هسته ای باراکه در الدفرا برخورد کرد‌‌
🔴
تحقیقات برای اطلاع از منبع حملات در حال انجام است و پس از پایان تحقیقات اطلاع رسانی خواهد شد‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/120616" target="_blank">📅 17:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120615">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
صدای انفجار در امارات
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/120615" target="_blank">📅 17:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120614">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
صدای انفجار در امارات
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/120614" target="_blank">📅 17:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120613">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bba9ba238.mp4?token=M5V2WgC2EAqN-vS6q5lRX7k4UyrJjjcNDrgbYWBRZ10jbcac2I3r1L8UvJ8lddk-BcOcg5qwbrZI_3yh_e7ybEJ1w7_81WqdI-rrcnnxrnjOKKL0UVUyXe5K_mp7wW955rfSe-rR_pXh5TrrNE_qm2Dou5Glz-bb7BN9NXlUc7gjLbCLm0fPZArO0NEmJ5cCoraIKg--0Hsl9J_QOtVHi-vCzRog68M6odAhd7SIsbtGeVLzrE__q5mQax0kQcWWO6VPbaNHLpMrtvGtl9LuJQVBm4k8HaxSKNZ3VP9oksIZ-P1HOIAoftJ4a4_IlTtN27vl5tb57lDEx_I4VIkz2hmz0AeHBObHQ2exxqxZZCPJLeLR0kYcb5YK1z3KIXjnW9W21OIwGXrC7dvqmUBbMscRSnUTkStj8Q_MdZlbWY-dEQIhvA3pznXIpMdVGEg1qBvgiysmGFPQ126P_1qZhKKonqarO8H1lym95BQ3qgnbXRwyB8XPFtb7VV7lePMZyeDgiO8WPieiUx0K7oysUflKBb8Z2Ogj16QPaOUqkAXg-6TKBFyX-DXiSbAq13mr9u2v9IwwyVyo9886HY6F2eNR4JMNXZBiovo5YRPHsvCjBKlzo5EnRQCe77AZYSTmtM4imS-W3CK4TE20gPmhSJjhBBw_ZhvsnRjiw7rXgyc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bba9ba238.mp4?token=M5V2WgC2EAqN-vS6q5lRX7k4UyrJjjcNDrgbYWBRZ10jbcac2I3r1L8UvJ8lddk-BcOcg5qwbrZI_3yh_e7ybEJ1w7_81WqdI-rrcnnxrnjOKKL0UVUyXe5K_mp7wW955rfSe-rR_pXh5TrrNE_qm2Dou5Glz-bb7BN9NXlUc7gjLbCLm0fPZArO0NEmJ5cCoraIKg--0Hsl9J_QOtVHi-vCzRog68M6odAhd7SIsbtGeVLzrE__q5mQax0kQcWWO6VPbaNHLpMrtvGtl9LuJQVBm4k8HaxSKNZ3VP9oksIZ-P1HOIAoftJ4a4_IlTtN27vl5tb57lDEx_I4VIkz2hmz0AeHBObHQ2exxqxZZCPJLeLR0kYcb5YK1z3KIXjnW9W21OIwGXrC7dvqmUBbMscRSnUTkStj8Q_MdZlbWY-dEQIhvA3pznXIpMdVGEg1qBvgiysmGFPQ126P_1qZhKKonqarO8H1lym95BQ3qgnbXRwyB8XPFtb7VV7lePMZyeDgiO8WPieiUx0K7oysUflKBb8Z2Ogj16QPaOUqkAXg-6TKBFyX-DXiSbAq13mr9u2v9IwwyVyo9886HY6F2eNR4JMNXZBiovo5YRPHsvCjBKlzo5EnRQCe77AZYSTmtM4imS-W3CK4TE20gPmhSJjhBBw_ZhvsnRjiw7rXgyc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : تو این جنگ معلوم شد ایران اصلاً براش مهم نیست چیو بزنه
- نه اماکن مقدس اسلام براش مهمه، نه مسیحیت، نه حتی مکان‌های مقدس یهودیا. به اینجا موشک شلیک کرد و هم اماکن مقدس رو به خطر انداخت
- هم مردمو، برای همین الان داریم بودجه ویژه می‌ذاریم برای محافظت و تقویت دیوار ندبه و زیرساخت‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/120613" target="_blank">📅 17:20 · 27 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
