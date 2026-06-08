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
<img src="https://cdn4.telesco.pe/file/UFZFuPpqtpqT17vPpDYcbvd4_m-jOuj-h8lHn3VLkjmDE2_LEzB9IvJYi5qsXUv_U9GbRilzhets7WB2rtCE3NwdMwYxnmFblglfyAUr0jJ3PBHY_Rm7wJBvaHJvweAMFUhVE3J6QxPp7M5rIfRwB-UhRFppFqGSVqWyu81tlyb5-l7aCBdpPF-nP7UyOZO6pAOteLFjD423rRiiELGcGN79GMAIiBNMnnhORec27RNHW-fgi2cSIz1e6Fjm6hkisI0zt80OwNmi8FOz52aQvBa-IH_SXOG-sKzke8VH2wjng-Yu7-VBAbhrscwKesoQONwExcgC6WXFNb3PyWiZxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 170K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 03:12:55</div>
<hr>

<div class="tg-post" id="msg-23032">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9BKKOWpPrn0xAlsesRggXa368rH6NB0TYvs-xbbBtuskhCQQ320xD143xHSPLhb_l7khi--qLKQiQolgX4vA50CfuoZQ4-gVFZe3aBMh9ZSUocqJhb_8N2ZdcnrgY-RQp-e56j216roi5zCOoo2UdCxYILu94BMgFVw2VUy3tfFB6FjM1cy2bp1VYXVeSlCLfOuEr4UwblwiCp5iyFZom4MI2PEQ3jOrawdhsjQ0q0LXqZzh3Hvo7Aiu1HAXuP2KhFxNL2HxQnmyDeIolWzi74x6nOABjfr0GJFhhXGNsaWqgWO4HRLJw8ok9eE9_mVUXBYlEPuswR2WDaEIT0p2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/23032" target="_blank">📅 01:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23031">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8torLvQiBYaqHZl_jscxmntEGCy1ZQo9aEZzY7xgEnl5YHJMWanMlFwCAAI1UJwFgxtZJXQ3o8FNH_xw2dgk96R6iHXYrQvHBaFijywN0A7cfwFHNQLC830FJanb9xAxckhiXtuC4h8bYf6UBlw29LKDqNfqyACzC-7UBLk934nOwUpvo168oRe6Muxj8UOWMslaRVgx2SP8bL0cPHA5ElrwPBGqVjBXu87PLcXXDpzrOxDvrtFr5RbB6zNzS0pZr6baXHdyl0VAKORE17KD7CZOTdp4raGaay6IlWonSGY59KFJs8vQ9-hspl7V19y88swlKzzzd-pcHNMZCHT5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه ‌‌‌دیدارهای ‌‌‌امروز؛
نبرد تدارکاتی ماتادورها مقابل تیم ملی پرو در صبح امروز در فاصله تنها 48 ساعت تا شروع بزرگ ترین تورنمت تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/23031" target="_blank">📅 01:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23030">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_sEoDag8A7Srtv4-x_Zupv-hN0AWk1OiNpIp5FUZSMvbmpYzJCChRZY2dIsdfw1T9g6ehXyi-iJMLDuBjjeOtNkJzTGSVYKkOT_LKlEUm5S1ReDIRkwv8rti39Ta8N29nSIczH8LGWztRhoKdh8ZBUEMCYDrMrQgKkiUkpEk4Nyn7p1_0naIhQhfbX7WwY-2V1WSS9_RNlqcxAktJUXqJzWxJyVxQiMsk5jHpN91zZcb1s3AoIKBizltrAzh6j8XWvNEBnj504dmyrSyiV8m3W1CE8VZRjqFFwDgdqw4oRgmBf1p74PE38ah7cdgFDRY-BDcTANofr3jr-dAAuoqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌دیروز؛
ازبردسخت‌هلندی‌ها مقابل ازبکستان تا برتری خروس‌ها در شب هتریک اولیسه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/23030" target="_blank">📅 01:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23029">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=KMZTRbMbN9JpUT-mrybGjjQtoL6wqI1iZwND5fgqFLx-R7Hw7IC619dj9x0Zf8_7JlxInOfLHsaNsDFkcL8IGk5LAcWyeAD0qD0EvxjBiwEm8PDgrLMw7icdXbPk5ne4i4R2BJ_DFiM7PCoXXfMUxGsQpoQ7y3qRHa30OvnQuPPRg5kbi4r1kJHDo9m46eo_hoXRB5SamKGXQTxkbaUNCsBY76SMtq7twwsyVHN1Iu0fIMeK7ggHLGLDTOC7ErjLEPX0nMP_tBGDEFosM6sPrnxh4zS8B-uqvCBFsI-95BvAwbWTHmpVPFwXIJRQJktGRt6L2PvwmpcmyR-PLfS87g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=KMZTRbMbN9JpUT-mrybGjjQtoL6wqI1iZwND5fgqFLx-R7Hw7IC619dj9x0Zf8_7JlxInOfLHsaNsDFkcL8IGk5LAcWyeAD0qD0EvxjBiwEm8PDgrLMw7icdXbPk5ne4i4R2BJ_DFiM7PCoXXfMUxGsQpoQ7y3qRHa30OvnQuPPRg5kbi4r1kJHDo9m46eo_hoXRB5SamKGXQTxkbaUNCsBY76SMtq7twwsyVHN1Iu0fIMeK7ggHLGLDTOC7ErjLEPX0nMP_tBGDEFosM6sPrnxh4zS8B-uqvCBFsI-95BvAwbWTHmpVPFwXIJRQJktGRt6L2PvwmpcmyR-PLfS87g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/23029" target="_blank">📅 00:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23028">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbZ3T09J7RaB3T8BV9VqRFWhAsQumkN6Gu6TWNXNSQvYna7iJ_tHKmehuW4wNSPzmg0gImO3dleXj1lLgB_kK6jUiQw4eiwx2tjN181mo6BDLXa8640ypwIjaYRoPsoixwkFtUQ5VYjyg4Yh3Sa7o6tlX27fSVH8cZk7hXup9D_iHj6qKa0ZPKRySY4xoCSRDZMPHyPz9leqm1psqAIe2Zvm70V0vImzBIcTMVZNA5CvDg3tYcaU-d8xgt5iCysHLcgbJFFzkjnhJm_k9h29EKgacrzXQ_v8XXmkL3gznfpw-Vqls-iwue_bFPRSymELrBNg_--oDgpzBHFYieXXkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا:
فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/23028" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23027">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=X8hJYnzePk4xaM8jHdZKzjvCJk_FvLOOVungrXR5MhB9nu_Y1AipTMBo7SO6iDSHyfst7YuoUq2p2DoQiQJurdmVpjLeHTWEmVrVa78tyiVIa1YgnXXOFHzuM8CIPeHCKFIwQHw8eqWHiLf5lTsxWcJTuMnucDSjvu89hLYIB1k-eR2_rECYDe_1paq16dvLBHmuTpZ7EoUfLIBDCd1ZNgvTPpAI0HQIbohzVUCc0eD7RTsvhDLQBGHXRmSuh4mI-kusCwXS6w4tECAVT2QXgt2QR_6XlDnKjLejsIry6aJTgG5jONKm_W4qXUbUHfnJ_4ZrWsQJNDI8_FGVQS_jnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=X8hJYnzePk4xaM8jHdZKzjvCJk_FvLOOVungrXR5MhB9nu_Y1AipTMBo7SO6iDSHyfst7YuoUq2p2DoQiQJurdmVpjLeHTWEmVrVa78tyiVIa1YgnXXOFHzuM8CIPeHCKFIwQHw8eqWHiLf5lTsxWcJTuMnucDSjvu89hLYIB1k-eR2_rECYDe_1paq16dvLBHmuTpZ7EoUfLIBDCd1ZNgvTPpAI0HQIbohzVUCc0eD7RTsvhDLQBGHXRmSuh4mI-kusCwXS6w4tECAVT2QXgt2QR_6XlDnKjLejsIry6aJTgG5jONKm_W4qXUbUHfnJ_4ZrWsQJNDI8_FGVQS_jnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
باتاییدرامون‌آلوارز؛
مورینیو سرمربی فصل جدید رئال‌ مادرید برای کنترل‌کامل رختکن تیم رئال، پپه رو بعنوان دستیار خودش انتخاب کرده تا بتونه حواشی بازیکن های داخل رختکن رو کنترل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/23027" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23026">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rW46pvTa-DxQVwlTTU3JsM8itvPNmmnlVJBW8GrAfnnxbME3RyUAE0bqYSFFUkrriN-cAyqd9psLpFG-bwWSW42nu07hi-ahw0z3JCDbYF6iQgjvvqjI1BkRGAEqy6e0D37Eqmx85HQbknqDXT7rTvDWC3JWbB3QixKGG7XBWG-KFxjWChNfSw7ya4HqM_IHZ9ZWwXgeV9Dk2QEXdG4c4iy8nAGqLHLSZfDo3xNmj3NmPUeZAx_z5i93F85qrhTppC1y5zxLht7MPUhg9ArbtcWXAJlczS2xeMNNO-kYH9DVg4GymwSk1S_zatysEo3GUYgcFpuOzS4YM9YYCJmNhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
توم‌میخوای‌ازمسابقات جام جهانی فوتبال پول دربیاری
؟
🥇
✅
کانال
ورسوس بت
کارش تحلیل و پیش بینی مسابقات جام جهانی به صورت حرفه ای
🍑
⚠️
توم‌میتونی‌از پیش‌بینی جام جهانی خیلی راحت پول دربیاری فقط کافیه با کانال ورسوس بت همراه شی
📣
🌐
ادرس عضویت کانالشون:e18
👇
🔪
https://t.me/+vEPd1hF2Y38yMWI0
🔪
https://t.me/+vEPd1hF2Y38yMWI0</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/23026" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23025">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=lJ__Ac87F3B9yXCcq5bl_hOm5tlczZA9ab0hex773P4jvYDxtXYNSXDRAYd5XYf22b28UtdbBmoRFY6fqHSV_kbqlUsOwgZFE8PM8qY7J6L4BBLkwzkeeO7417RVyYxHc0KHH-QAMRMI_b3PxCZcWgcjgunmGgoGDcJAuGlSqlZGiqZmqWNZlp-ZVSpiojypwJw4OC5ylaElTCXF0Y3ggK8WZHmHDsdBhDXMvbE3T98NqzFOsmTcW1nTcZhKMcgvcwbQG2sf-n4mX3ylyDqnfU5_j-qEvTy7YCKQo7HCcNNBEBxA4oByqDyeThOQVXOY0cOsqhKGx102hqN3O23-yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=lJ__Ac87F3B9yXCcq5bl_hOm5tlczZA9ab0hex773P4jvYDxtXYNSXDRAYd5XYf22b28UtdbBmoRFY6fqHSV_kbqlUsOwgZFE8PM8qY7J6L4BBLkwzkeeO7417RVyYxHc0KHH-QAMRMI_b3PxCZcWgcjgunmGgoGDcJAuGlSqlZGiqZmqWNZlp-ZVSpiojypwJw4OC5ylaElTCXF0Y3ggK8WZHmHDsdBhDXMvbE3T98NqzFOsmTcW1nTcZhKMcgvcwbQG2sf-n4mX3ylyDqnfU5_j-qEvTy7YCKQo7HCcNNBEBxA4oByqDyeThOQVXOY0cOsqhKGx102hqN3O23-yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
خوزه فلیکس: فلورنتینو پرز در کنار اینکه 150 میلیون یورو برای جذب مایکل اولیسه کنار گداشته؛ 150 میلیون یورو برای جذب یک فوق ستاره دیگهه کنار گذاشته. پرز میخواد این پنجره دو فوق ستاره به‌ارزش 300 میلیون یورو برای مورینیو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/persiana_Soccer/23025" target="_blank">📅 00:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23024">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=Ha-ANJEzsPqUnyH8xRDjXq41zqJxGxt6zQYh8dFLtKmcmJXcxJnEcrXu5JVlVpi6nz2Y_dx5cxNIG4yk2cCrisyWZ4JkhIYfa_duePkp10hI_yN0BT2k8uT49_j0ANtXoT6aJZZLutyvMGe0ehSBSflDa3RFi6_00eFMjMYHcgw6ATf_ugGok3B2vcJuGzZFg1DhIcJKyN8Ut_kHM_y8-B5bMpyL2zHkEOSG7ljfFkyfeM0ocd9jolUs8DmT6WN-gp_1X5NLRa5Ep-HRXdD4k7W8v1RgKSQarGmUyuEG6XNjatNu9B0R5W0dt5qD3mO69F_iqUUShQKSgq-YBE59FlYF4zZdijW-MbAnv_a76BCaOkxixhOPnVxtwVnKHwYLPBPohQjGgcRPyCO1JxTiPNaZCSdxsme9ID3rz8DE0r7bNYuskZshbd7gFmUdasQMhCnCgq4-AnlAbAoJ2EjRo-WYa-Ez3YOVtCEpZvfLbuthvnnXJMEVFXAYyUlBH9d5B36-9J14jN0JpiItbkgGFDGf-YFL6cV4BkfejtdnAAb_cFXicyuVLHNS0jBNaBx3JPEZtfp4yj9bP1d5d_c1rvQvi-cCIRmnMZl2byzPMLH1h38NbT2YbfbMa5RJlJR4Kl9U9nvFNP90tqcVqHEadfwwEwl_B14N-bzmbzR5hA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=Ha-ANJEzsPqUnyH8xRDjXq41zqJxGxt6zQYh8dFLtKmcmJXcxJnEcrXu5JVlVpi6nz2Y_dx5cxNIG4yk2cCrisyWZ4JkhIYfa_duePkp10hI_yN0BT2k8uT49_j0ANtXoT6aJZZLutyvMGe0ehSBSflDa3RFi6_00eFMjMYHcgw6ATf_ugGok3B2vcJuGzZFg1DhIcJKyN8Ut_kHM_y8-B5bMpyL2zHkEOSG7ljfFkyfeM0ocd9jolUs8DmT6WN-gp_1X5NLRa5Ep-HRXdD4k7W8v1RgKSQarGmUyuEG6XNjatNu9B0R5W0dt5qD3mO69F_iqUUShQKSgq-YBE59FlYF4zZdijW-MbAnv_a76BCaOkxixhOPnVxtwVnKHwYLPBPohQjGgcRPyCO1JxTiPNaZCSdxsme9ID3rz8DE0r7bNYuskZshbd7gFmUdasQMhCnCgq4-AnlAbAoJ2EjRo-WYa-Ez3YOVtCEpZvfLbuthvnnXJMEVFXAYyUlBH9d5B36-9J14jN0JpiItbkgGFDGf-YFL6cV4BkfejtdnAAb_cFXicyuVLHNS0jBNaBx3JPEZtfp4yj9bP1d5d_c1rvQvi-cCIRmnMZl2byzPMLH1h38NbT2YbfbMa5RJlJR4Kl9U9nvFNP90tqcVqHEadfwwEwl_B14N-bzmbzR5hA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیوخفن‌ببینید اززوج‌های‌مخوف‌حاضر در جام جهانی؛ مراحل‌حذفی‌قراره‌بازی‌های‌جذابی رو ببینیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/23024" target="_blank">📅 00:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23023">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7x35l6y5pb0X2_VWxkRrS4PLf1cj3T3NUx-f_DbQdYR_0V_9CTTC5AfFlP7srTCCm66AqK6TMlAHG8xVU6yyWtlPJd6jfFByKCkAIha2rIS4v2Ne2-_KqWtQ7_fJBBZeGeDqWh38SJ6AjbODc0uxvPvHBU8V4VTh2tHZ8CAn-TnLK25hrMiE7mndThessg7MK1Nr5QcVM-oheJMaqAmZ9ZMQ2AnvyQ_ZzljpbM4YZ_s9OGeWKieZea-MU9LpEmFWdBeG34oPQNKuNdFDKBKxHsBvmz1CwdacUE5UQdxlm4QZwq7bMKQ0MZPGqj8hvI9WwYRePoiAjWhkMEZm2uKgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جام‌جهانی‌فوتبال‌قراره از 21 خرداد شروع بشه. لیگ‌ملت‌های‌والیبال هم از 22 خرداد شروع خواهد شد؛ برنامه‌دیدارهای‌هفته‌اول لیگ ملت‌های والیبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/23023" target="_blank">📅 22:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23022">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9su5uUHDZv13ifItH1MDNVxbIL_cyTcbJeIlOkLKhembWD_c0KG3ip0A-EE2Ddp2XUfAPoxj3vPXdU6HleHZXQsqaQEquL-NmYJQj_CYul2R_CCpqZZ9egRjo4jdCbJUVyx0ePYHitVIZtruhz0hvgI1WCKIwNOGGCKQ9rhnkrVENGZRbGoC6qJmwxd334shEssEyPWepPntnbxwEqvh4SPFzDlpZ8lLFt0MfHMode3veECCEmX1mqZcpdp-PdZMIZ6vA4TA6S-VDsupv1Wb3B3O8_PG_3XTn7Wj_PovkjBcul-77EfID_3UxXWAEImEZ7GjkRcBWibHWHmvL9TWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/23022" target="_blank">📅 22:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23021">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eI6dAyJ9M5RdZkvu6C5YI30L1Auv-9-ljqz_BDCa718dqgTxb3bpdfUoOhsAwrEQPDeMAURwnXhh4aRzgdFW-V9dtnM1fEOTsj1XXXbiJ7XFWOhLMJUrfsUKaGvm4BVkVlGuODUH7JYdMiAwBHodTcOtQgHYKZ7Yb-8v-ROJ0q3PvIe916pNUlL9F1vnXrxqEQQt47w1vonc0p1wBpd0ma99q5lRR1yA4koyUFScMpBNhcn9_iC_8ivOGqI9mC2aA7_An4msxJNv6EELI_18RDV8sWEOKhddZKtYo1e0BIbIjgV01nbMaMXA0pGzndJRpD9C6_qogCatjnAaAMw-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/23021" target="_blank">📅 22:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23020">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=My_O1A98D8LJ0ezyM2yD4fgc9PL4SKLsKbbnkCaw6sfq5wgpBI3jTAjKM_P2qE_jA-Qjcu-GgDpQ7BrCdG9i-t0q6lsLfPYXEbdIKyz83FS0sLZVBol3gFPzr3hQVdmQi-scG0ItdlRue9dbQ0IaRM_E8IVMMzldydNg2vAdeyZzLkvS1iPfntVFJRcJBCsVyUjEtPpziLSHQ0nTnCxC7wgbPl_lMZcvfyeKwQ_i5QJzsZRcQSUiEGuvTKTzgUosR7Sodwff2N3o8ZcWQDHqDAuP9msmFX_iwJptRmOvubZlOl7KzlbaEyWwE66sirV99nMowAUtUAmTZgiQcHaBQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=My_O1A98D8LJ0ezyM2yD4fgc9PL4SKLsKbbnkCaw6sfq5wgpBI3jTAjKM_P2qE_jA-Qjcu-GgDpQ7BrCdG9i-t0q6lsLfPYXEbdIKyz83FS0sLZVBol3gFPzr3hQVdmQi-scG0ItdlRue9dbQ0IaRM_E8IVMMzldydNg2vAdeyZzLkvS1iPfntVFJRcJBCsVyUjEtPpziLSHQ0nTnCxC7wgbPl_lMZcvfyeKwQ_i5QJzsZRcQSUiEGuvTKTzgUosR7Sodwff2N3o8ZcWQDHqDAuP9msmFX_iwJptRmOvubZlOl7KzlbaEyWwE66sirV99nMowAUtUAmTZgiQcHaBQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی‌پرشیانا توسط علی تاجرنیا رئیس هیات مدیره استقلال: وکلای ما خبرهای بسیار خوبی درخصوص‌پنجره‌باشگاه به ما دادند و تا هفته آینده پنجره نقل و انتقالاتی باشگاه باز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/23020" target="_blank">📅 22:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23019">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoOk__lUQxzF-um1A9asGb1MxMX9ZaLYYwi1BF3LHS8dy9SQFoMZ4xAoISnnAKgUqHFHx2MLDKMmYw6HuwAXprR9p5W3Rl1tvJ-Fv8GTpe55_xlSLW_Kz7B7PwcOHd4DiDLj1tX0dg8Imv-bIT3cWI8L6aJ-x2qeEhn6wRG242j4KTDkXUH62XZsZ1tPUfYWZmvGcWIuc_1yrtvajLeOTQeeFyWC7AvioyP0KXWLmEUcLFFGfUI-ApGNLo7UARu-BG6q4aiy_N9QZxW_siLvTJUAZWlHhPZP2av9_O5PNSbkoDD9QeRePFI0t3SJZOWKavDdGRcOp-B6SfiI8Kzyxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛نشریه‌مارکا: فلورنتینو پرز عزمش رو برای جذب خولیان آلوارز در همین تابستون جزم کرده و میخواد بزودی 150 میلیون یورو به حساب باشگاه‌اتلتیکومادرید پرداخت کنه و این فوق ستاره آرژانتینی رو از چنگ فلیک و آبی اناری‌ها در بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/23019" target="_blank">📅 22:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23018">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdfUg5RoYL6e8f1KTqwO37rEo5oo6OScHpvuIytu7FraghLeCOJq8Pm3lCEGQ1RaBKivPw3Afrm8tLO6OaDqTZNjSCHG8ErETLiRYPFyG__f4tsmKGU1Ta0NtBzQWyRRWq8CzSpWhQQ-4ifP47V9Fy6LSK7ELY6_2X7GAZB7qm5fv5OxdlBM2xKCgSfYNZITTKwyBkAwX4BmTvPV3o_4er8Y57ZZeXyEfib78IEPffpYU9ZCIh7czJHat9UqMdWX_peylJeKJpi-3lzsBAaa_g2DsGdlU7T3_gH14eaP6TuIcw0AspiaXA94wHWkfVs7sjfI2Ci-dL4xxfouHWWP1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی اسطوره‌داوری ایران در اعتراض به کشتار بیش از ۵۰ هزار نفر توسط نیروی سرکوب جمهوری اسلامی در جریان انقلاب ملی ایرانیان، با بازنشر یک‌ویدیونوشت: «برای بقای کثیف خودتون، جون عزیزانمونو بلعیدید. قرار ما با شما؛ نه دادگاه، نه‌بخشش. رقص و پایکوبی روی…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/23018" target="_blank">📅 21:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23017">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2huXpSMcXWKFDAAzzYxHQ58XrtJRGCTwwPlZnTq4wIlmaN82YeSBUApT0Z8CFqEqQlSSPeoC2TN6neS2Dtoni4Z6Cipjm_HxdnSHGsr0v4qudEwpA35MJ_64KL-jaDyKXzBzL332qGz4EHW-tGVL3EHKPsv4MklDPUos7rT90rwJUbzHHIV1lDBsFvGfGo7NLNf8oEEhNI2reNoYSlQ94BOBNZP2U5XB58c8ZNeAtaSMyqJBzGUUaWXVwF5D7P-1Hz3LUAiRVscO122_FtlfmB5J1ZZ8vwbVd4urKMp2xN0_djcINopcnmUdtVH5RfIAcdqx1JUmClZV9bgUUY2Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇦🇷
جدول رکورداران کسب بیشترین تعداد جام دربین‌بازیکنان؛ لیونل‌مسی بااختلاف درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/23017" target="_blank">📅 21:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23016">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Icg5iHs-Bt91nXWzbCzbgfCIIgt6Y0fID3paa5J2UGA9oU7fDio_IPudUSJ1s9aRALB97TE6PYPy2mZzncRbfrZFqfvDE1ndlK0R14H6BsHeIN2xVLPzwJRvoPahr6tjKJC4mT1RcIuGByJrz6xirPxMfn276cRYWhuI1XoXnhfExldTDy2CD6gbZUF7vMdmoSDLpyLdaPb9QxWpfKdoN7bCcWZi-PXL2PNKMkvboUGtQ7O4oPSZC_YeqZn-QPiDv_fcNBMo5n-Q9QfFCQRcXXLbIiIpjEF8OMJr_wf6IHZ_rwALxQ-NIdpmp4kkJe8r8EiEE_0s4Aw2zh3p66q8mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/23016" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23015">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPMxCMZA8bUJhYvRkCMEaiIDM5MHMjFtI6pCl7bosHnapSiY5LEwLHcotcb7zF0KYJcOrdgvu3YGuC-7EJKD58uZYcKuizaxKphP7pRqiGrJOgcKfvyxuK0E_7szKhsrXE9BpcdIq1ZgZnBMIgQYHg7cWxong26seg_UyLkFzmkQ14gXmaASbczvDW0PhyRlBPwn3J2r8ry_5YHt-FPwAAZD84ldZ1rL6sijXD0r-nlLKeyPnQLwZTTg1NcOQW9oT8ta0_4F1QQpZPBMdzVe3Z6HxNYiEYb0FZIY3kAJr9bYfys_0jjc3R9a2XblJbbSSzaKWDBfZiYXIGw6Ysik-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/23015" target="_blank">📅 20:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23014">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=AldWCLXBTHyyKXqkCEfPfEooKom_XKnPrC8LhQB5OZc52xSQqVTm9BqAHibDTngIUVGiHxaWDiEhu2Cc4-fRbBol36qE5TMlOFwhGW4pxcl03CLDNXdaBKByp-8j0-ttJTymZqTiTNmXNAMFfzHSpeb0xbFCs1yyoXNidcljXyyunRU0gOgfHPIJ2HpE8SgnxAZ_T5q-qQ4hYxADS5x9OYX5PQ5MC3gTBk10htvSxIq6b-fFzlQOQMD4QoeYmBDtaniMjp8eODTj_u-IdAIOT4wWKPy59Y1BnZJlGsDDnybSObR_z1YtXuipGp8X1mdb9yIDa91TEBlqw5I4hP-LbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=AldWCLXBTHyyKXqkCEfPfEooKom_XKnPrC8LhQB5OZc52xSQqVTm9BqAHibDTngIUVGiHxaWDiEhu2Cc4-fRbBol36qE5TMlOFwhGW4pxcl03CLDNXdaBKByp-8j0-ttJTymZqTiTNmXNAMFfzHSpeb0xbFCs1yyoXNidcljXyyunRU0gOgfHPIJ2HpE8SgnxAZ_T5q-qQ4hYxADS5x9OYX5PQ5MC3gTBk10htvSxIq6b-fFzlQOQMD4QoeYmBDtaniMjp8eODTj_u-IdAIOT4wWKPy59Y1BnZJlGsDDnybSObR_z1YtXuipGp8X1mdb9yIDa91TEBlqw5I4hP-LbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ما
مردمی بودیم
عاشق فوتبال، تو فوتبال هیچ دستاوردی نداشتیم ولی باز هم عاشقانه دنبال کننده بودیم و دل‌کنده‌نمیشدیم‌حتی وقتی هربار بعد از یک شکست‌جمله‌کلیشه‌ای "این باخت چیزی از ارزش‌های تیم ما کم نکرد" میشینیدیم. بامردم ایران که در جام‌ جهانی 2018 روسیه بابت خراب کردن اون موقع طلایی مقابل پرتغال اشک ریختن چیکار کردین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/23014" target="_blank">📅 20:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23013">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI2jzO_6c5VZgFdSNKiw0SN-ZKtpKSZwApDsv3F4vzLWxwc1HzG3ewPtQ474rJyzgn_okS12CNw5OlFDjkNuL9qF1ByncVOqKMxPDCV0wuXQXPmvoWPYoGyKFaMbk46T03dL1qqPMqIRVxZT0ulWANb4zgXEuXBDveh0uwYZF1_jv11dtvkTya6TUL27a5SwyOvbIx5Z49pS7pbVDtFMzNwyKDa0BSehhJaRR--WWkt8-QUMSB8FZ2AqCEP0QOZtNkljws1In3fFUb-Ig-IVC8Ydv01RkB4VVtw8_b7NzhkXqPGU8Foc6lcQR10FRzJd93q2fvicN4SwTLYWTDMuYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/23013" target="_blank">📅 20:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23012">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbAp2fx5XydXLenPLnJGUwURU4GAFzyVfJiJ4Qw6qhvw4S6WGlxJinZCOj3AlwD9CbRFWGFwK4z9449QmAxwJ5rGmu7qIsV7FDKFMSF8_jhxRZlSYiWmWhJLCXmpzlShvMXF0gWXwPo0aGkrUG9cg1aiNQHnhjoJPN1Dy64c8ZVEe4GQ55sJq0kCYsQaQK_iZIxl1KNqSe8kGt52hNcuyMdJpcoebXYykCJ3oaujk-KCQMVBNQqF7p20rG0m6mc0fD8gmNkCxRy57W-F9aHJCgR6KZbp7PfIimn26D55Q89oIrOljVB-CtHv6d6mqwskKulQppmOcDIAuAqqbaWfRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/23012" target="_blank">📅 20:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23011">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29259cd165.mp4?token=vRzkHXmncDEQEevXAPfUi7aVElcB9uvTGTuYmycaCe9lrMsibgGSpH47C5lsyRfqMNTtnCh8i-522I4h02FS4U1jLFO-gF_vtx4pYrh8SlDdfzjIAjlxc3qjrHMRSc3wvDGvL_dczfa1ammsS1K84q_gVL1NkLeIQzEq1LKVIYach2R9dDD7HtdSywT6vBBNHWMFd3BtqX6039g6GM0BwAANwO85bhenuAcLcZZRApWWzImn2lRyz1NeBvd9bYbzOIwX4kX6tMElak0_N9-TwrLMKTt1lRyjzlC4wnfLcTBKo-2nZfRhc4Kj4xtj4bc2ax9gC-Eb8PO0tSa9D2sGjlbPoR5U1PBEx47BLTzkNbk4Np983sKkRENjGpoGLD0mGDBvrWndQ3KoPr9-5EdCiUIZFPklka6NJgIyCG2iOREaXfYQKaF9cF-aJd4VSnUemOBdqKb29R8xDrYkUj_HOTA1xTj39zOlZFrRAozk6gLdtu11MQxRASE_KHWloIMAGm1XyhMvvt-7mP-9s9wmbcVCDgd9oMviR21cSpX766S61Q24EplLkNYgn03AUqRZ6KIbG_ITR6rKqQYmsU3Gsn1slaZGLHCS5lJRvwHGgZ2mLHn0V9tlsIJHVrMdwVMfxSeeewoD7OSFlhLwrwAlb9xbcqhk-85Vdq3wd8LVHc8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29259cd165.mp4?token=vRzkHXmncDEQEevXAPfUi7aVElcB9uvTGTuYmycaCe9lrMsibgGSpH47C5lsyRfqMNTtnCh8i-522I4h02FS4U1jLFO-gF_vtx4pYrh8SlDdfzjIAjlxc3qjrHMRSc3wvDGvL_dczfa1ammsS1K84q_gVL1NkLeIQzEq1LKVIYach2R9dDD7HtdSywT6vBBNHWMFd3BtqX6039g6GM0BwAANwO85bhenuAcLcZZRApWWzImn2lRyz1NeBvd9bYbzOIwX4kX6tMElak0_N9-TwrLMKTt1lRyjzlC4wnfLcTBKo-2nZfRhc4Kj4xtj4bc2ax9gC-Eb8PO0tSa9D2sGjlbPoR5U1PBEx47BLTzkNbk4Np983sKkRENjGpoGLD0mGDBvrWndQ3KoPr9-5EdCiUIZFPklka6NJgIyCG2iOREaXfYQKaF9cF-aJd4VSnUemOBdqKb29R8xDrYkUj_HOTA1xTj39zOlZFrRAozk6gLdtu11MQxRASE_KHWloIMAGm1XyhMvvt-7mP-9s9wmbcVCDgd9oMviR21cSpX766S61Q24EplLkNYgn03AUqRZ6KIbG_ITR6rKqQYmsU3Gsn1slaZGLHCS5lJRvwHGgZ2mLHn0V9tlsIJHVrMdwVMfxSeeewoD7OSFlhLwrwAlb9xbcqhk-85Vdq3wd8LVHc8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/23011" target="_blank">📅 20:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23010">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYuy5VYV3-BebA4gB8_S4riHk1yL0RIdMUjld6v9AmYvRm39bcC6rPNyIn5nglZBz_3EekZQHQmNihww_bwI_Hi7xIE_oqW3KYF0ZIE7MtBZYeTesgzjFwXzya3Vw1TYDro3I66jWIUzXE14MSyFiPich3M0vmFGNGmocxTu6MrZlDB3WS2G37qJvpYHL-WCoPKUMqJHJ2xjlDDl_JFsCxE7-49OeYt_RCv1i4nLU3Yn104skW0saC91uw0ISBKr6QuzdkTkadTv0gPFNrWJmz6LDTQJ66vStg1UICj_GSy_nDeDzO07WqBLhlAY0AhqggcoXn_LjctkF_MT7EiXVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/23010" target="_blank">📅 20:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23009">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j92rMftzWhqto5RtBsyTKgz74zgizpLk37Oij546OmIFGfIjbLBBg6P_DXosVfLirQcI8MaFJvCXi0JNJnaw3xkVq83TZ_kmIPSNYjsA_TvRvZRv2gRWnvXlIF93scfW_MDJBZSsTwVtAq9Y3-aGSmyJMiLdnecNc5gDo2jRhu_W982N755GIbXHXfWH87f18_r-S5YxlqKKOIPS-NkKbd75VQmHAo4zReldfeqx2OVOgqORy-Z-laABJK3ianeEjh0HeYrsala8_4GYZivMXiRRUF0fXFtpsXBAiu-hlnOWP3ueeSWRqXiwDP1Yiq_FWTHDEQaY1RjSzGg6i6iT5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
لیست ورودی و خروجی مدنظر اوسمار ویرا برای فصل اینده رقابت‌ها به دستمون رسیده و بزودی کامل پوشش‌خواهیم‌داد. علت اینکه یه چند روز صبر کردیم این بود که همه دوستان عزیز کانال به اینترنت دسترسی پیداکنند. ویو کانال قبل‌جنگ 65 70 کا بود الان با وجود اینکه نت وصله…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/23009" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23008">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=slROzlJYtpUqsKLSw5S7llqc9ebP8-YPX9UbNBrD26krcTg8lm9umE2q0R6QbsoVS8Ua8Fh5UQFMur8u8Hjf3h8wM9Nek2D_pTbdSYvSBdTLwFPfUOfGHw8W5bqwgyvrUFH7Jrq558QeXX3C1_ggllO16Kr-0xnkpwieeXL6TY-Uq2ea766zSZnpIxS3ys34ZbALZqcosXDy-vcr-okytqZE0UeFNYHWohEUJWwu2z6tagek1BECJlFOG8Q5_23AaRtb9O5I22OhxzfJr7L2QvX1Y45v_my8Jmk9EECShTpR0bb-GuFAXBePC9MP8E41C8Jd6fbHvR6sb3Df3rvhcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=slROzlJYtpUqsKLSw5S7llqc9ebP8-YPX9UbNBrD26krcTg8lm9umE2q0R6QbsoVS8Ua8Fh5UQFMur8u8Hjf3h8wM9Nek2D_pTbdSYvSBdTLwFPfUOfGHw8W5bqwgyvrUFH7Jrq558QeXX3C1_ggllO16Kr-0xnkpwieeXL6TY-Uq2ea766zSZnpIxS3ys34ZbALZqcosXDy-vcr-okytqZE0UeFNYHWohEUJWwu2z6tagek1BECJlFOG8Q5_23AaRtb9O5I22OhxzfJr7L2QvX1Y45v_my8Jmk9EECShTpR0bb-GuFAXBePC9MP8E41C8Jd6fbHvR6sb3Df3rvhcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/23008" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23007">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZiJ5b2qhaY4CB_dBCNXXN_uxIZtwLpiTvXxj2ir-JyJM-_ctkUIaDhNCS_pDG4P1R1qUklGVqs8dC_CPL8J9r3pyxQSAnjXS7DZsanswuF5lT1D-roZif7ixcryHK7vnyAIVrNaFEQBXXOVcGq26oJTlNkinsOu6gIAaxeHMYrKNhhpqFF1T0uCFxlFAJV6fDi0ribpAEfeW73HZBaA7SW-8wjt00CJr31Dtkt57ZRtSX4qbe1SHNsFaLul-i7g0ksDZpQoMvIcicJUogW_CgfeAHtSAgtXmzCbEaNiaJN4Z3gdI-Yh6IfqVdKVEcjCUVXx4qhYersMRiuWR6_99Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
باارزدیجیتال‌حسابتو شارژ کن
🅰️
🅰️
🅰️
شارژ اضافی بگیر
✅
🎁
20% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
همراه با درگاه‌
#ریالی
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
18
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23007" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23006">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUws58UoTO8kclUEERXyAJOArfGdK5zt35ijG_CRw37ZHP8TigtYTVnXqrXUf8B1rGc96Mt8pcmLMUaTbyqEgqehsTRa1MYFB8OpoJRZaAuqNXnhALyBiL20_HmrHa0EPJSeuh_OJxE9jP7NvDwwyDJowJPXKhNn4NTuqxYzdqcbuFgbmQjzF7AWjxpDK91J5fp-3bFFy_YPtmYyzh-JtWj0L05v7HlnPEDVRHNsEH-Imy78v51CP1ksj3BcFjH7_gofNcSJgnSDyp84gNdZoyq1fhBgIC-xU9GdUqFGVbpsywuLnLUxYAxiFsNcbGBxKgRJfNzacqwC___2Z0c7TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دبل اولیویه ژیرو ستاره39ساله لیل در بازی شب گذشته این‌تیم‌درلوشامپیونه؛ ژیرو در این دیدار نمره 9.0 دریافت کرد و بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/23006" target="_blank">📅 18:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23005">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiEFI69UkyialnEvwgqA7HUeyldxMovLhzZQ2MYPEV3parpgrhf88mb6HT6_dF0bLUgWR3U8sKDOHsqnCVqbmP2UBwP3wO-Wu0gSGiILdS_fvn33zLXuK6RBDllQxczfM-B5UAd3gCTmTw6wvV29WGBGfix-upVmaIHNALWJvqn7woffoMN3A1i4-ZAC2iqa-3byGRJ0zT_BkAuqNTJNgQosDtSeAtlmo2vOmZAUZh-lWTEEBLzv-v-kCG6YQxV9NSMVn66TlsPS5CwP3nv1T_865lg98BVM49KCBQeCgTcrnMADLKkgPw7yDt__NpPn392MYeaVeDU_hjyyKMBm-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه رسمی فیفا: دیدار دو تیم ایران
🆚
مصر قطعا دیدارافتخارهمجنسگرایان‌خواهدبود و به هیچ عنوان این رویدادلغونخواهدشد.  دراین دیدار ارزش های همجنسگرایی را به جهان نشان خواهیم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23005" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23004">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=q0rnqx0laoY--I-DYOswhpwjlbFX3gGLTqyXX_zV52Uz4Pn4acpVPhqRAS3e8tCtFupJ2kGUkIfsuSlMlRcqC_9n5k21fokMN6xDqK8y97_9ID4abmQx_6OlG1QKknKZ6cvBx33FsgZWeoWdl5gYhsoVBr-LamklUFdVgcM-bXuhFbYGdCty1oROPKRkp9CiyzsoH9V6fYra6n-qhDG8OBVWopqqP9sCpWAYdqYwAZvWUFtCQfNPV2ol1lNI2VT6hIskXhH6tbKHJYKw0NRr9PgOMLsXDA2jZukZCBAqaq6QxjudpC0X0p94Bvs9-CvG51UdoH_kjrWoeKY5rpVZzzVvOEitRpW5K9m3cHDrsKp3LUonEJglf1Tf4eCuAdKLI9RVsS9lEK9fd95tAzVuJKTr4OFXijeftRRCQc5rIdET5VolyrLGw3zifwEJHwEO20aYdZH8sv11UFfvaqIM2XjHOKjtu_FFV2L-fncK7JpciQ0JrnmVYan1c7JNFlMK2Kpo7XINks1zl_apkYzyjHxYPlFszh1qh_IoDcWbqDksSOhw9pkXkKHhq-srxjvOk71R7d20bHVXy3-jw7Xldj0zIXgiEeVUM81Esn9xdGykHi913GnP3SSAKt4rSVBU4-n9if2DlQkHTNgNWeHybC0hDX055YS3mDhX1oTchoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=q0rnqx0laoY--I-DYOswhpwjlbFX3gGLTqyXX_zV52Uz4Pn4acpVPhqRAS3e8tCtFupJ2kGUkIfsuSlMlRcqC_9n5k21fokMN6xDqK8y97_9ID4abmQx_6OlG1QKknKZ6cvBx33FsgZWeoWdl5gYhsoVBr-LamklUFdVgcM-bXuhFbYGdCty1oROPKRkp9CiyzsoH9V6fYra6n-qhDG8OBVWopqqP9sCpWAYdqYwAZvWUFtCQfNPV2ol1lNI2VT6hIskXhH6tbKHJYKw0NRr9PgOMLsXDA2jZukZCBAqaq6QxjudpC0X0p94Bvs9-CvG51UdoH_kjrWoeKY5rpVZzzVvOEitRpW5K9m3cHDrsKp3LUonEJglf1Tf4eCuAdKLI9RVsS9lEK9fd95tAzVuJKTr4OFXijeftRRCQc5rIdET5VolyrLGw3zifwEJHwEO20aYdZH8sv11UFfvaqIM2XjHOKjtu_FFV2L-fncK7JpciQ0JrnmVYan1c7JNFlMK2Kpo7XINks1zl_apkYzyjHxYPlFszh1qh_IoDcWbqDksSOhw9pkXkKHhq-srxjvOk71R7d20bHVXy3-jw7Xldj0zIXgiEeVUM81Esn9xdGykHi913GnP3SSAKt4rSVBU4-n9if2DlQkHTNgNWeHybC0hDX055YS3mDhX1oTchoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیووک اوریگی مهاجم31ساله سابق لیورپول ساعتی‌قبل‌خیلی‌زود از دنیای‌فوتبال خداحافظی کرد. اوریگی با اون گل تاریخی‌اش به بارسا راه قهرمانی لیورپولِ مدل یورگن کلوپ در UCL رو هموار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/23004" target="_blank">📅 18:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23003">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=msS-52qvU-DumVl_IYmAzfeyGo1GCuZ6XYmbKoBfOU7x4Ho4TWOIeGI2o3imDPX2-0Yu1ODHXuPrJoXn8uqcHDGCoSuGbEcsm29bc4ZxM5P_Krw1NGvoEDV6_EQxKCF5XHuE8SNG-PGdAqS8zp3F_2BQ_VYorLp8WZPV1fH2r8ndf-DVsLvIrXPHZyjDTHj6xrWTm0JP5Qedn9rYxR0gdK75I6EVISssU8X85-LZWJrt7mSjhhuzi81z67a67xqZ-a19gDOJEwSPKb8M-1zDy2UU-r2WTjCxKe2knJ8UpVkpvZCCa3lq9LpQs41bb_FcHFGeluhLGOXN0J47rzgTbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=msS-52qvU-DumVl_IYmAzfeyGo1GCuZ6XYmbKoBfOU7x4Ho4TWOIeGI2o3imDPX2-0Yu1ODHXuPrJoXn8uqcHDGCoSuGbEcsm29bc4ZxM5P_Krw1NGvoEDV6_EQxKCF5XHuE8SNG-PGdAqS8zp3F_2BQ_VYorLp8WZPV1fH2r8ndf-DVsLvIrXPHZyjDTHj6xrWTm0JP5Qedn9rYxR0gdK75I6EVISssU8X85-LZWJrt7mSjhhuzi81z67a67xqZ-a19gDOJEwSPKb8M-1zDy2UU-r2WTjCxKe2knJ8UpVkpvZCCa3lq9LpQs41bb_FcHFGeluhLGOXN0J47rzgTbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
رحمان عموزاد شب گذشته در حالی که مسابقه اش‌رو 8 بر 0 از حریف‌بلعارستانی‌خود عقب بود در نهایت با یک کامبک تاریخی 17 بر 10 پیروز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23003" target="_blank">📅 17:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23002">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C78TFYd9rWRqQpFCr69_irg2Qds5CNDPufoEEAa3yBqY25PJQsNE9NQeQ6w-wHVWQsm-UAE157a3-2KCOBI69K9djyhoItu9VJys51tt9UhI55ght7DL7bTMLMB2sW-A9g40UCIHUjDXbzUMKTQ5_eElKo2IcE1q-wEeMifvGlBsgw-5-UJ1wBpFi7pGWGd2mkwRPTeoivOlfladsejjf9ytQqmO_3yt8XZGjCQptM3EvyneWtAF1lwYj386TKStaRuKACfwkJYIxdiCkng2oKVFYTHXjJVKqyme6iSU4czhNEiiqLxpSlHnZPZjPu-mXMeaoY6yOsU-u-FkrZj79w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
پُردرامدترین بازیکنان حاضر در جام جهانی 2026؛
کریس رونالدو با اختلاف در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23002" target="_blank">📅 17:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23001">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUS5oQvLBGceHA7-JkT_PpMcZv5HTPD-aVRYQiExPia6TKm1_y5Fo9_yJgmygzeDqF1K0udac9Vor1hiYk8GC1pIX1jIjo41MxqD1FoMQxdimIzYiOHEnCOsq-EyeW4w-xxP77giE3HMc88oREtkHtNGF2LgBZ3-J2XCDwNzQgQ3mpHX7tJDWdPsdHKYpnGHpqZZ2h2iNKbo_usSbo6EHIO4lcCprOl05wlSszh7c4Kw6X2NnPldzn7eeLcdvOn8Jqtl_loH0e0yBI3Y3Kfavb5yY2OtFFTyeIxgsPnu2Z88qpbmBov0zmXkiLMSAdByswlPD9aIPT6AFr0IeGkj0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌پرسپولیس‌بزودی‌باانتشار بیانیه‌ای جدایی مجتبی فخریان و یاسین سلمانی رو اعلام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23001" target="_blank">📅 17:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23000">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S41UrDQ07KVKIe1R_PNXGjy3e6Mw11N1SquGuNSRNcmuUwgeRxi07rTS4JCvXJHbMqopLIvM3oZ9o3rFtPjSpAj7iyw1fOUJ1zHx4jRTbfbsIBiIohM4bZdogfAV1vzUjjwkacEdUuPqSiQAKV-M4k71izTH2nuE8UXQbqBspiKmlCQuzKfIkFLT5qZtY9aDNG-4GJ82L4ZpLm8ziZheal4143-J0TT2uL8WI3d2miHbusar2uxWw_Stq311sat8eL430WbQgJ9DUyWBsGI6GoCBEjgehltF1CbxCTKz_O9iz0edacyXBZuxNX0a70IBozgy40bNMxEEKjYV3BMYUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در این تیم، همیشه جایی برای پیرمردها هست؛
ایران و پاناما پیرترین تیم‌های جام جهانی ۲۰۲۶
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23000" target="_blank">📅 16:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22999">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvhFn_ILQc21JtcMMfQVw99qCmzukuy2V9Xxi7UmTeQ6vKlSorAhVQwUFIg5nWQH60j3Y6JPtkpfShbbJpQPjGY_pjM8Dh11oy3Cdo-0f6WlOrzRKu-HQxDsFCGrES0oXYTwR9FsnJ-HW255dEN-EjeKQ1J5Szh14CpKpxnBirw8l_lW3cYwpC2motMLMJvDdyR6yqQCxF9BGr048UDB2Ik9ArqMbziNQOUrxD7CtIUxmkSKNGdIuNMmUZgFhZjha1u9rf6iPwwgAkpUnytu19nbwygHiHxqkbKrPQjNeb-METxr_YC4kuVQlAmArU5GUHQms4LjR5AzfDW_pjBvMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22999" target="_blank">📅 15:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22998">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbXD-9APXbkff5q35CVGalgeaEGaNhOIRWKck1tQv4wZ9QLz_wPDK3sPS5aFh6dlYicGd9Vd7wASSIyOeTejZJQ0_aMz2sDVaegM2DsRbi7Ux7TZ9gVFs9Hb4Fks1kbpOlacMZeUldHwDBZu6tXH2mw9qZ_i2hZ-jFUuf-_nlQ9ZNi48YgWO2yuo6My6QhC66pRr2J5ycSWN3E7tC4ptVJ_XYELjXxkQq57dZzsmS6hvZZTSg28fKGLk9F2orEsoNEaQZNOOkT3YZA8c3mztfkqhCNAQJChr95QGC0-v69-DJwSlVmulzzL7deeAhKZBEpG961PvBzYzHk_UBnEvsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22998" target="_blank">📅 15:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22997">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9QhhUIe8ce52IX358JgLGGj-d3Kb0b3IJ2B6kZZP2PmNP4NktrMKXpMI7_4A3O_Y-XAUYoApzsxMLAxAR1ZU38m-F-Ztoml98vRmQm4bdcAvoAUKLilH4-_CLoY9ztveXFp-3A-QyoXFbSHhafnSqwbLTWbi4TeLE4BMxmBGH7y6bdg1HsROQSH6wHZsgiIrOhOpJJxiGsaW8YWVFbiL8Qfjwr_eiW4Qzw28Nv2DiscA8Sqp-8zIJxH0_MwMNe_pdwNtjMBA4kRPy9K4PsyZoZUFz_wsrD-ZCioZAk_T4oMQ4-8E0NXMgFiUhs7buycWKsh_cpZQuKIHVCaUg05rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#تکمیلی؛ رئیس‌اتلتیکومادرید: هر باشگاهی خولیان آلوارز رو میخواهد باید 150 میلیون یورو به حساب باشگاه ما واریز کند. نماینده آلوارز به ما گفته که اولویت او پیوستن به باشگاه بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22997" target="_blank">📅 15:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22996">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=VspZuslhOT7MwuKfhqMI0ACbnUQPuKdOLJc5M7StYAFhjSWI-xBIf6zuwJPOhYNsMXdWgDHy6BRR2RgCAohbFzB_DIYCKnfg9s8m2bMGevnWWwSv5XGnieLTY8dyqxtmwshYTzUaqdYdB45cOUo3YHzGYzNjcdyxgAYvTOzgFctjET9oH97kOakce0pXW4Mza8krYci_YYEvNad8lPcbT8M2wMi1h3yowzTwSA68HzWdNY5ZM0XUQ4ooFtX1dnhdI4mLfCyqtpl6Onr-ikZu-dh6LN7QzvLbhFqv3KEGu8wIG9o8TflDVYjbT_civzKSvXv2st-SPa9XSWb-rkXPTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=VspZuslhOT7MwuKfhqMI0ACbnUQPuKdOLJc5M7StYAFhjSWI-xBIf6zuwJPOhYNsMXdWgDHy6BRR2RgCAohbFzB_DIYCKnfg9s8m2bMGevnWWwSv5XGnieLTY8dyqxtmwshYTzUaqdYdB45cOUo3YHzGYzNjcdyxgAYvTOzgFctjET9oH97kOakce0pXW4Mza8krYci_YYEvNad8lPcbT8M2wMi1h3yowzTwSA68HzWdNY5ZM0XUQ4ooFtX1dnhdI4mLfCyqtpl6Onr-ikZu-dh6LN7QzvLbhFqv3KEGu8wIG9o8TflDVYjbT_civzKSvXv2st-SPa9XSWb-rkXPTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین‌یامال ستاره تیم‌ملی اسپانیا و بارسلونا درباره دلیل بستن باند روی دستش در حین بازی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22996" target="_blank">📅 15:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22995">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLXZtXt0W5uzkdcGaWV371sWkUrfjn2F0Nz4Rc4Dbjc-N-99xdh_HSVT-Z2SKAmHQJ--2IeIwhiEkJLm-YHD9ldGPzx4jWpwNBg4ZScmM4V_rTbJXaRZfzasNcmoXBiy_0OOg51qJAhGJKuX5PYlKFjAKHmulIO1ZQGrxi3QvqSGESD7KcxfZOCkIf1XRHmN80GRoNb2nC2bVSgKM8Xf2Rv8ldAQkc6wb_UrBTJs2E9iYn8Mg-0rNuCZwMJn7mKGrq4MbCGNss6QDGzfT3h_SOB70Y78wcltCqGEc5Cd0T0Zv7DM7rMOPy_jnN0AalGa9UPj_wjoRMkOvYQyYey0rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نقل و انتقالات تابستانی امسال برخلاف تصورات بخاطر بحران‌ مالی‌ باشگاه‌ها؛ بمب های بسیاری زیادی ترکونده خواهدشد. هم پرسپولیس هم استقلال و هم تراکتور و سپاهان خرید های خفنی خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22995" target="_blank">📅 14:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22994">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=fY4JkHFN17ft7KOSV-POy4SzUhUhC0kktKbYrOHHcTf2mL9z3uxeJlrbo-C0FDjF3yS271w6zvfJZsp-1PyHvGdux4ziorl0qFhwNVlxTn97kR21Z5cPfw0Y3qxd3znaBeMSUqEPU_kJxpCPELPeeeH-8Bcy6x9ouQkcfRDvF_j-kaw08RuDxXKNr_0tMTfEk4am8tLpoERe5FaG8RYSy3iHFa70ri6dpC3wcaJNgyDF6mk1syUY5KmdjpY5kmCnRThmgeBNC7-3HEnet23-VAmY6z33It8KIRHt7IvIlmyboygPeXPGRs-_Ytkpx4yMxpi-SpT0jMNL23bj01zVNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=fY4JkHFN17ft7KOSV-POy4SzUhUhC0kktKbYrOHHcTf2mL9z3uxeJlrbo-C0FDjF3yS271w6zvfJZsp-1PyHvGdux4ziorl0qFhwNVlxTn97kR21Z5cPfw0Y3qxd3znaBeMSUqEPU_kJxpCPELPeeeH-8Bcy6x9ouQkcfRDvF_j-kaw08RuDxXKNr_0tMTfEk4am8tLpoERe5FaG8RYSy3iHFa70ri6dpC3wcaJNgyDF6mk1syUY5KmdjpY5kmCnRThmgeBNC7-3HEnet23-VAmY6z33It8KIRHt7IvIlmyboygPeXPGRs-_Ytkpx4yMxpi-SpT0jMNL23bj01zVNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بازیکنای تیم ملی فرانسه بعد دیدن اون عکس و ژست سمی رایان چرکی اداشو درمیارن
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/22994" target="_blank">📅 13:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22993">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7q-rGHBgR5xIrV7cr9jpNUSnCKLtfqAgLMPG_QzjTdHEo9m1g9EGsoa6vCBD15KYvnvnGZL0nZ_q6yU8WJUuYoabt9dmT2TTCWC83oUSX7qeX8rJ_HOLI8t2Vtx2VN7ez7gEYjGd4GA7hcnasFNRfNHecx-Jdp-GLbWldBckT45XjPjqeW-cgX8U3Rrss3C-umQngN6c8CcFcssJ2f6CaG1xghb79l96HQa88OFMw7oiNVr26l7t8SpTmVFNsaP4A10503jYuSIoGVV6gLCDvDV8AzQ-WsdFd9BNj1MJQhP1mr_kYGNSb9cNb7DhvtMX6LcNw7_AIwjUwZCkP_dvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/22993" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22992">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3s7Pqn8dZkWsMbiqN5lgvl2TdRBTxonj38inyyxSbprHaP7iRW1iiaNsu7L4FJ_Ecn9ij8uEV_RwQG2-C7HF5NZLQmEkR0wAXtmomvJlilo_qpqRtrKNcbbXTIVP_bF99zc_QPQmKelEud76HKh6S5UYPLUjUH8_cwGsqsepEen9L-7JOG1zi5Jya8D4y1wLde_2XU8LeSu72iWDs-uPWXzcbmpev_5XYgABSPgfETZwRwLemLskbu2z-Ngy31Br37V-DX1jNSUWZnC1-BBnTyQannFTCXwm67VcfZjxQMjIYowchS33Zm35BUsjQEBheJFgnMqk_TZIT6dC-XJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/22992" target="_blank">📅 13:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22991">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=JXvNiuiMDjfb_X44tygrHD2ETQEXQ6iwtZSfcp65oGrxHxhH93_jmOKdZlIg2jySn8ixUIaQJZvtgndqqs08NPCZVllPkKsdegeAWYDwQFY1XOLBOZ5XjimOyQQw3UgQlnlx3wE4iFaZJ01oZVNpfxS5WB72OwUGp_NkEItu2K-sKHGJlr5mKNBm9ZTh-ARjuA1gDf5p-0mqhj1itJ9YLKOqu5JN7POOQwtAMu8r5WfaJAcNynsbQcp_-LJghUtSi6S6Ucy6YvduusgU6GC8qb575-zkSnibqeBm_PNohJ7Z4BQqtuoTcyFNk34yq5gNr1k50wT5agZ-UD0JjMpc_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=JXvNiuiMDjfb_X44tygrHD2ETQEXQ6iwtZSfcp65oGrxHxhH93_jmOKdZlIg2jySn8ixUIaQJZvtgndqqs08NPCZVllPkKsdegeAWYDwQFY1XOLBOZ5XjimOyQQw3UgQlnlx3wE4iFaZJ01oZVNpfxS5WB72OwUGp_NkEItu2K-sKHGJlr5mKNBm9ZTh-ARjuA1gDf5p-0mqhj1itJ9YLKOqu5JN7POOQwtAMu8r5WfaJAcNynsbQcp_-LJghUtSi6S6Ucy6YvduusgU6GC8qb575-zkSnibqeBm_PNohJ7Z4BQqtuoTcyFNk34yq5gNr1k50wT5agZ-UD0JjMpc_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرد البرز که بهترین خط دفاعی لیگ یک را دارد و هیچوقت دریک دیدار ۲ گل دریافت نکرده بود. اما فرزاد حسین خانی با چای نبات و شاگردانش در مس کرمان موفق شد در ورزشگاه خانگی فرد البرز به این تیم ۲ گل بزند و ۳ یا ۴ گل هم ۱۰۰ درصدی هم نزدند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/22991" target="_blank">📅 12:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22989">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J51L8pvwybOBjv2Leig4GykKBwj4IHde_SQlye_pIahCAU1MIur3w0xGfFRWSk_M-L_kla3RqmuHkOexRu7v1X12Nxm-r6zMipfiK9tWrG47KqGQ58v-txZx_XXPrIaL8fV9bi8zUumhxek2-dVToQzgZUlf9ZW3XQAgEvLaTHipXmTp4IUDosWJArKbwJEOmtFiIEaGK-SZ5Q29Jw3xZszXr1tatK7vBZDGpW4Lvm49VByTas1K3u8-n1zFG-ob17V3a8XGdxnT0T0VACad9SJQYhQDDlS_L2zgJfuzodGsjOT_Dbms4hsuZZuTOK4aWg8DQGZ8WGDv4wc0WLLGdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه‌اتفاق‌خاصی‌رخ‌ندهد؛ اوسمار ویرا برزیلی چهارشنبه یااواخر همین‌هفته‌وارد تهران خواهد شد تا برنامه‌های‌آماده‌سازی‌پرسپولیس‌را از نزدیک دنبال‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22989" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22988">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HroeOGKFzmue2hXxkbEN-2eETIiF5RmjA5G-uHooE54NdKWQKUpdY4a9DNu2MA6FfyJzwDf3PSsAM70e1PK4zGpZbqFBAoLoBiksAjXwrsCS1aziHJw9ETXcZqDkRoztmmiqBEvDxbzG-K8m9JQAPh2P8PJRJ_LSACSIplihPhx7w1aR9DEQeJN0NWBODiDwf76_eH5E-iFwKEfZ6os8wmSrOQ0C-ImIzon3-WH5lNzYU-9JMGh7iFsW9VkYcS7Xvg1PXrKoBavsD_Nq3n3KQPfqjhinhA_woJEoD91bjKUYjrhTRZNQrbTnpjWyXW1_cM-3WAET965VzP12ICa9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22988" target="_blank">📅 11:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22987">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=T5oXp2zTmUfrAyq7lNahAyCxVIJD4lltVa2ixAjkD8TdGrsT2DH5noIMTIRw4pnKc2sNW9fEuv9-GHXaSQXVFEEN3bTodtxCXbC991Bz0KhiMf1fPZSvXTN-6-0f5B9YV2j0kQx94RS8cyw5JetS-SGWF8RMuDmtPFDNCr224lUVJ8OxxjEmFiRMqSEtuWputy6LdUuY4JaK7yoe5LyfKgq0QF0ERUV1zsnpTBCu9lV9Wcjj4duPr_GpFBdwEsvZfxokSuDHBIzKsRqBB3Y1M3OG-f7KKJufBopxmTJ_yWt5pZNWcid8vIdYptzXkQqUDWCj-fZHvgDGO8g7ZL7I7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=T5oXp2zTmUfrAyq7lNahAyCxVIJD4lltVa2ixAjkD8TdGrsT2DH5noIMTIRw4pnKc2sNW9fEuv9-GHXaSQXVFEEN3bTodtxCXbC991Bz0KhiMf1fPZSvXTN-6-0f5B9YV2j0kQx94RS8cyw5JetS-SGWF8RMuDmtPFDNCr224lUVJ8OxxjEmFiRMqSEtuWputy6LdUuY4JaK7yoe5LyfKgq0QF0ERUV1zsnpTBCu9lV9Wcjj4duPr_GpFBdwEsvZfxokSuDHBIzKsRqBB3Y1M3OG-f7KKJufBopxmTJ_yWt5pZNWcid8vIdYptzXkQqUDWCj-fZHvgDGO8g7ZL7I7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نه‌داداش جبر جغرافیایی توی پیشرفت آدما اصلا تاثیر نداره؛ محمدصلاح اگه تو مازندران بدنیا میومد:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22987" target="_blank">📅 10:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22986">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=CEAqr7o5_lCIqdjqiet8iO3W5pMC9qyjUnhTLCyIcSa2Kxjuyl0syyW3gDYvhCeu43hLOGPTTX7bMcxxixsPYPB9Ca0BxMiZ2tiZOq31tk-PdMQcqd7lUe2AT24cNIaOArapTHkhj6c3w4LyGow5AhyEdHg9GCF2GjKheizJS465MS5UUzdr6ctTneRBDf59nOAAT0vVbVf8g1z-5iC_CF4SbVj-Slz3r3jAZJY2CkqIIZ6X0ubDcI36u7ogE3xMqM9pGAx1Ooc2jC7_klC7rZilD2dHUWLbGYR1BQQGTyNNxX09iluudSHJaKnar0M-4gJpwB23CE87hdNwCTmLRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=CEAqr7o5_lCIqdjqiet8iO3W5pMC9qyjUnhTLCyIcSa2Kxjuyl0syyW3gDYvhCeu43hLOGPTTX7bMcxxixsPYPB9Ca0BxMiZ2tiZOq31tk-PdMQcqd7lUe2AT24cNIaOArapTHkhj6c3w4LyGow5AhyEdHg9GCF2GjKheizJS465MS5UUzdr6ctTneRBDf59nOAAT0vVbVf8g1z-5iC_CF4SbVj-Slz3r3jAZJY2CkqIIZ6X0ubDcI36u7ogE3xMqM9pGAx1Ooc2jC7_klC7rZilD2dHUWLbGYR1BQQGTyNNxX09iluudSHJaKnar0M-4gJpwB23CE87hdNwCTmLRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ
؛
مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22986" target="_blank">📅 10:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22984">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PChUvRqqhNa_4Is8T0QoRgpQm8s9rnmu6q3qV5FxN144zetcl0fvrMf2DU2_7MtTqhvPke0QtFy-SDRoQFsHAOheh0pLngdT7CTIO0GNyNAPKr4b0GKnej4CwXnXTM3ARj9SSGcB3mEVb18WHeInYJ38LB8fasG8eGIFkDxAojEfEvEYgsLloci-yfqipPIp5F31Yz9__D1dyKCxs7m3l4vIuI3OvmfsTxxOU2ck-6lEKycDUjFB2GWPKpNJaVb45LQZYxWHGTwok52tsZ6tFe_4A79r0EjRGMZ3i0s2ktnYRTArXs7piBJDzDOJoPHgB1wZjbUBo6C79qZiu_uRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OLY8ETpqL6j60ArT6KyU_UZjSFi3ax-ypQQhTZZd_5ONGb6V8SMcPNo_dZRQ4W67ZxN-krah24qOZ-O533sVrxTGAG1c_6TRXr1xD4I4Ekz-jL62TU8_9huTKMuz7P6NewRtk6I3beVPBkv62bCaZsuTeN8K7ahcZjC8Zk9_vbBHVf1jUDQuYUAhiAL9e1ezTiz4vrSrHc0zceL2t0n0W6b7K1hkLmKyO873OINwTtVPjnHhSaCu38LgJrgUYJKIe5uhDaZ12xg-CXV5MalGl2vzlmYVmcEdpgOie6sdMbGEtEaJg2dF8YfRNhz1sUrP4sHfQ7OH0c1kjoeyvdTwfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بماند به یادگار؛ یه ریاضی‌ دان آلمانی به نام Joachim Klement که قهرمان سه جام جهانی اخیر را با مدل خود درست پیش‌ بینی کرده، معتقده قهرمان جام جهانی ۲۰۲۶ هلنده.  مدل او که عواملی مانند تولید ناخالص داخلی، جمعیت، فرهنگ و رتبه‌بندی را در نظر می‌گیرد سناریوی…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22984" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22983">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa0118288.mp4?token=DbWgm2OZeAkqhDRKFWZm7FMSFhevZ5cErqA1vjyA8Cx7q7lC1Tev8qxa7_Cq7eXuSW8Qv_L_kCeDsst-FdjJCG7Ya-JOv6XYHmCSMHWqtcrgO5a3fKUh319UAyqulVM8JDz0OK20rhdVf6J2mLoD2GKfKtdn17CFCNiUqbNUlIWCSbChkVLSOsKkSuaxSLXsn60UGQlkqXt_PfH2w1puam0PQRa1pKiDUHftK6Am4HW1VRz4irUPJhEFhlHnweX_Hssc7XhrBWfC_P8vvb9FZWt40b-XjRED0P8DikO_IquDQZMe7AyYlRfvAf652FiXepFxMxrprnPtwsdmh7M0qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa0118288.mp4?token=DbWgm2OZeAkqhDRKFWZm7FMSFhevZ5cErqA1vjyA8Cx7q7lC1Tev8qxa7_Cq7eXuSW8Qv_L_kCeDsst-FdjJCG7Ya-JOv6XYHmCSMHWqtcrgO5a3fKUh319UAyqulVM8JDz0OK20rhdVf6J2mLoD2GKfKtdn17CFCNiUqbNUlIWCSbChkVLSOsKkSuaxSLXsn60UGQlkqXt_PfH2w1puam0PQRa1pKiDUHftK6Am4HW1VRz4irUPJhEFhlHnweX_Hssc7XhrBWfC_P8vvb9FZWt40b-XjRED0P8DikO_IquDQZMe7AyYlRfvAf652FiXepFxMxrprnPtwsdmh7M0qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نشریه ESPN: بازی دوتیم ایران - مصر در جام جهانی به احتمال فراوان بازی حمایت از همجنسگرا ها خواهد بود و فیفا نظرش رو تغییر نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22983" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22981">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkEcub53zw5Mge6oc8diXM9GjOWNT3IA8iKDGTlqGEHbkksblMGcZjmNgRjBdzdMrvdWV-ACN2gH2ySomysmXGhFpi85ML393tWFXYXnqQM8jj6PZAv2syKk92D0wG0HlXMO0QZ2GUXCZ5ExPxBf3use4wcQBKKWlHb9Rzx4T0yAcqxFdV79seAgmhr5bZzWNMuNYCtk2k5x5UIV0yi9u7kJdqqTCn2BWzmEmB5w1pBSrgPa4E96tT7JJkkYsn8ATV64Fhghsi1Ymm-DmdUcfDUAdt-DrpxvdjmK-Lj5PdWVWjCCxYMUqJQBF_KuSQWZaVG3mHOeuvwVaYLdXG803g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22981" target="_blank">📅 10:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22980">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGvJiT4hEvzhxrRXYBoPyBIJJzyv_coq696NBP2gUJLo4vMvC10Lfn2PMT3p1UNEIIcNMoVq6YAnLHqhPq-eujhVPA6xaKiYXxeJ91bMjQEMbEZwwc5x41xV82kto7RmuONiHySNFC__IdLoo5nFRu7jkZWG2ndZcUDKOJ4EUaXfnwpFsOwGZE8Tti7M9Z4RGlcdYmcFXmm-XFMWN__Ui3pKx1aKzkGL6uqm07BNLRoNFn1SFuSuv-DmMz1o-YvUitakoc2LROikDWwgK6JGJT8cNffIJA6O_RUpRuhsJaPDtAzDAqPoTmzW-l97xmnVxJ2lcfu6WW1HpPoxf06FqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات
|موندو:
مارک‌کوکوریا به سران چلسی گفته که دراین‌تابستون‌میخواد از این تیم جدا شه. اولویت‌او بازگشت به بارساست. چلسی برای این انتقال حدود 50 میلیون یورو از بارسا میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22980" target="_blank">📅 09:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22979">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epdc2ks1p-cvNdlri8biiNS8QSImu_WN-Cc2_OwzNukt8cdBQa1VEmGz0oc2QZ5IA6OBeiwxyTY0RjNvP2oSKSNmXy3bTkNkY4mSC284kH2xUahuojOPl5cmheb_230hogmZRLjjgekA34fbrAUwysRUFGNTtbTBItC3QiN8JFAfxXNgNpWUSoE92Q4zKPym19BTMuFK0jRj3-xAdQAb7K6eGlET27MtWt92VntUEcqxYm1fdefoj3iSe0zCIepo9vtXt7sH0c8WcVyyNEUvsKwGj_KiNdgQsIVi6FqjVyGgW7dhAbCkxo0ISBeDJ_pA1xwxl7H68uzTccy8HQdXLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تموم شبکه‌ های ماهواره ای مختلف که قراره رقابت‌های جام جهانی رو با کیفیت پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22979" target="_blank">📅 09:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22978">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxNSVSy-hOX5CFUg7GCdPlo4pPQrrkUezG8ThjqzG6bZmZsG5PCsMnoAJd7LTSyOrL3Znhve-qzdq8aq6LpiwN_N4kg7rHUQVWBurXmIF_uLZdfuMfl2ftp6E2kUcGunPW8gb3KEbVsZDwkvq85xQ4zzCK7IQ-2FS8UQ3C37BKM0C9dBPpg23U4NAiHS15mRW9w5LRzF_5tzjKKQe-jdAV7hFAGC4gqnkQO9rqYAh6CH0lb86vs9uo5D9u7ebULSNMz_ZUdIApGu4olgwsZE4vN1eGjdArsS91ZinAEByPCzjeXAiI5IftEXZiY2ORnMUn9RPD_N6CXzwdcuyPYbMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/22978" target="_blank">📅 02:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22977">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkG5eL18H254zRzDE4ddcYiangdJPEwyCWmGv777buRZpjJtWlaENPwQIzsim_f39TdMKgBh_Qd2xB4HxcvrD_gh1B0QmZEhOFc9MTEf2PMpNO2GisC3UOnzAg1nH4VhFO2CM3cEO_R6I1Ic1pM6Qq1HB2vSoG3KQGzvz6paswn1OFqiAwWFO79Z8_mit8rAl9DRH9NUDxc5EtDvbUWQVpb_4-Y7CqZo5__GB8_I8tJ9HWxndMHdWz0vHXsuKgvpzOG00z_xkFe7OTv4p1sxTufzreXhsEQRNap_h-zhZspsjW1Dk5bUl4OeuhUMCluWmTxTX4LbeoDo1H0ed5SUCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/22977" target="_blank">📅 01:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22976">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNzh9v7cMCErAhhcPoq4gUGuRYRfwXB40KGFdV5oNOk1VeFx9P7Pn3iotJrrgY6RRFySu2VrLJAhWQdLM_Kw2MjWYHQVcjwozK5GVUgi7ii7sHdt_f4mvo_Wa_OUaopdaXISOHna05IWfqrZu2kpiizHIst9Nx0_5fr-w3eV1uuFkufIRxNpkWr5KSlbbSLWyJiLNXbrptkc2-OSDQsJy8U78LHMqMsf-5zBm1SsBLy3fWqKHMaTaASKcvaAE-e7pm8sJA1k2aZBzBWC6mXiTT92q5GdK4PJjy0OrY-ld6Ujzo9WPqPXxgooktOoU3-LzG-KXMpYtglxFVdtpYLuPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛پرسپولیسی‌های‌حاضر دراردوی تیم ملی از آریا یوسفی مدافع‌راست سپاهان خواسته‌ اند که برای فصل بعد راهی این تیم شود. یوسفی از پرسپولیس آفر قابل توجهی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22976" target="_blank">📅 01:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22974">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLSvugH4_5If5uepxMwCbg2oxnSFD6UCgYHwu5jzx4rKQn9iDhdnK-UrJ_fapBcpmJPRU9aJIK7W65P4yqdK_7XYgFfIt7-klnuVImD6LuEYFrY4Hb3KRji2wQneA1KDnGkawdTIr6OtqNq1ixf9nd55g1GqXQOK3VtNX91_elzMeU9wlfFpkYVCckPQnlgGKCzmBf-2MgqJxx5HtJeuzrACRAIdhr0zn0drl2vnms0vCvS8CBdMpVDy0SWCJXXT6tHPDPFlDhy5UaLujbBjecK1cJvD-Icncv5DWXU0D3hiv70dkjz7trwh1FXJecCt2biMcexRN_ogAvcp969szg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
از دوئل تدارکاتی شاگردان کومان و کاناوارو تا آخرین بازی فرانسوی‌ها پیش‌ از سفر به کشور آمریکا و جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22974" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22973">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCVArIOPsdc7BOTWD8WKpPjCwf-oi6HA3w3iD_jDtx8C0rmgyasWyXCjIPgXxm3C2RJzwC9qjWnVZxrCpm2Sf-gJoHs00xTXIM3gtw2J4ITRaGBtB-Q0H0yDXhURSO_PdS_Sbv-knP9uGSVlnm3maZI8kWFxRLUTyP8YR-raebv8-m_U9keDUtu2jugseXto3FEWZMW6aAx61_r4Y32N-Wkkiwh3DpV8qfl295WPuAxwhCgoyAGpoiRTU207_jdBDPGRZdBG7R9Cx9l1xJlp6mxbYRdbDZJiuquFMkBZY38Ajmj_oNv-3uFHwLkFz5ONRG3FbPsALMp9N2VHL865lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از برد آرژانتینی‌ها در شب‌‌استراحت‌مسی‌تاتساوی درجدال نروژ و مراکش
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22973" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22972">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgGrOq4ysOW7My_wClz74prwbJN9UVdBNwfqFMIXWnHDvBAylVsF05exVx-PKGU1VkhT10ALp6mQU8PGDoKxJLmJpKu4D7b8Vg2U2bQSJ5rRc2dl8elZKv_dV0RQsM_v9PUrxW5O2VUg8-HQEbHH9hmcTzBUc56JSh1HbOe-ZXhmXT-W87laoTRpB1ELAp1GDo6cCCz1jSuUFxClj6CnXqetnWYnv97dcjxTkk6flgmq8k0z21ewIwa42An0-aYY5h6h1e93Huxyjbd3GIdly0L0B_OwviBjIm3POku2R45xNHLXxkkl_le1CNmmMvs63-1RTtkK_s43ao-kd-X-NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22972" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22971">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=FOOwP2Puhjux3PmdxNQFBPOY9ZtWzNQWDIJIokXBh943DFAMtIjWP0DRghL1eVocQZ0koTT8ULUwTQNupbFrPGgl93u6nEhEBldBk0eTxAG_hrsW_6y6YxkM_ToWsbMzst2iDDJHZF45Ygbw4BCkdjVxwCANncq-E6TFnimM_YbF5l825sWueViYsPXe_76ZiWVBIsbuYsYE2OYv67wFGga6-cXgmEgUjayiTJCZc7F7k3hfywCs9tNHWY5ICU5G6NGq2UvAwmVftA4bc4oOGsIEYbnEcDb7-2FIb1XeJyWjvOzfdvGJeArI32DP9Q5yG4ROe7PJvijecxILxd9rcX96zCeI58Nfto6ss4sZZ52EPahx6dgtK03wWGAqamJdRy3u30456XhoackQU9jjyH0whKPPuZftkXOgRS2UhNbRECJP_xr6X2s6AIoZx-vIOZxxLjOC-SBKCRLY_ZtjTY5D-nJNFJSMpMgelJSpa8JD7gbpYU9EREEr8a8CGtGpduPs0DpJ8cybz5ZA-xYQm7OR6J67EZhExFx8XFs4l_1WrBRB5efA-tSgxANYVyLCSuYqUlAcPZXPhZsZuIqLJpbsV74clDAcJ0n-kA9i_q87LPEdYmMI3rRhYudzpGiKD0ymnoi5-U8ODQehoIK6m4CJxslZBIcfd75fg2wGiGE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=FOOwP2Puhjux3PmdxNQFBPOY9ZtWzNQWDIJIokXBh943DFAMtIjWP0DRghL1eVocQZ0koTT8ULUwTQNupbFrPGgl93u6nEhEBldBk0eTxAG_hrsW_6y6YxkM_ToWsbMzst2iDDJHZF45Ygbw4BCkdjVxwCANncq-E6TFnimM_YbF5l825sWueViYsPXe_76ZiWVBIsbuYsYE2OYv67wFGga6-cXgmEgUjayiTJCZc7F7k3hfywCs9tNHWY5ICU5G6NGq2UvAwmVftA4bc4oOGsIEYbnEcDb7-2FIb1XeJyWjvOzfdvGJeArI32DP9Q5yG4ROe7PJvijecxILxd9rcX96zCeI58Nfto6ss4sZZ52EPahx6dgtK03wWGAqamJdRy3u30456XhoackQU9jjyH0whKPPuZftkXOgRS2UhNbRECJP_xr6X2s6AIoZx-vIOZxxLjOC-SBKCRLY_ZtjTY5D-nJNFJSMpMgelJSpa8JD7gbpYU9EREEr8a8CGtGpduPs0DpJ8cybz5ZA-xYQm7OR6J67EZhExFx8XFs4l_1WrBRB5efA-tSgxANYVyLCSuYqUlAcPZXPhZsZuIqLJpbsV74clDAcJ0n-kA9i_q87LPEdYmMI3rRhYudzpGiKD0ymnoi5-U8ODQehoIK6m4CJxslZBIcfd75fg2wGiGE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22971" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22970">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=B3BQ-YahYVlecjVifLktNCDvEsCrAAOmFtKrw3i3NFk2-w2CjEkiuwE9p3u69o9RWF1s2IODq9jdtUA985-H57_f71zDkd4yM2llKytAcJcB_2gEDuzHTMOxeBk4djHFxXpZmfGJ0Vtpf7vHCNTYF9s6NFfUHij6rZOTLW90Oodj7s_O_SaN8gVkOnT8FIQ47IhQTksnOWP1fjFJW5leqMzk_wZDZd95AmsJDu6Gx-0lzpO4drhMgjdwnwXQxUGURw5vhiPhIQHvjK90LnjUuqA8kV8ulECEvPa1M4-1VL29QPLPd4yII5rI2hUsouRRzZ6Nb_hSaMRoVWk5E8aQdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=B3BQ-YahYVlecjVifLktNCDvEsCrAAOmFtKrw3i3NFk2-w2CjEkiuwE9p3u69o9RWF1s2IODq9jdtUA985-H57_f71zDkd4yM2llKytAcJcB_2gEDuzHTMOxeBk4djHFxXpZmfGJ0Vtpf7vHCNTYF9s6NFfUHij6rZOTLW90Oodj7s_O_SaN8gVkOnT8FIQ47IhQTksnOWP1fjFJW5leqMzk_wZDZd95AmsJDu6Gx-0lzpO4drhMgjdwnwXQxUGURw5vhiPhIQHvjK90LnjUuqA8kV8ulECEvPa1M4-1VL29QPLPd4yII5rI2hUsouRRzZ6Nb_hSaMRoVWk5E8aQdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ایکرکاسیاس گلراسبق رئال‌مادرید در مصاحبه با روماریو: «مسی خواب‌وخوراک‌رو ازم گرفته بود.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22970" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22968">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hA0O2SBUEiaH5MMqswQdmGUzZcsMr833y5sjaGqg73K9mOyoCssaVGHI9S9BcLqN4unuwSZJLvvPrxYM2HU_gaTkBiqjFBIEtnEpAon8It5Q9aZ3UUsZuDRBG6_CDAuv38-lz6TJ2O15ShxJQmE6vaah24z4TLknX0OVSVFe9l_bjL2eEpN7vJoUMYnqQX0GjyF53sPnkpB2xgb11lu0TBL_0K0NEWN_KFqq94qsPoV8jaFTUj7YegN83AzP5-gOxLmpuxxar9zRSBD4zyci8mfWOgF0IWcd7bjTboMctPHml9fDPd6-_RRxsy15DlEO112-3avWzyPDRzlN-w71wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای رسانه‌های روسیه‌ای: دو باشگاه ایرانی خواستار برای جذب کسری طاهری ستاره 20 ساله روبین کازان روسیه به این باشگاه نامه زده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22968" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22967">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca6abec005.mp4?token=XE9xfUtqaHRLj93IN1BvQra84fQQFfE8eHvs8-JAvs4TBDayfJHsduL38xKTR5W7hEoHnKNppfUVgAFeJjPi1gez_d-GVAaVIqwZi69YjRJPssYNquim5xXBpa4EI20LEEyG8wRmENr6MbL_WskIzlOiPhBkCrQC-nf1FTHqyJ7UTeLmYJ6uDc2yYlKWeSicH0ftiAdPy4vtUh_SFcMcbHpWt6zpDmBLB3cGWJfrPDtVL1o1qIRosrSDDPoHpIeSAGj5XTIe_Y2DQk3iSCbSkCkYIHRktr4dcY_mhhSDaMUzpHzq9CRlmMR-NoZOirok6mof90mmd51QdPABhDNRng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca6abec005.mp4?token=XE9xfUtqaHRLj93IN1BvQra84fQQFfE8eHvs8-JAvs4TBDayfJHsduL38xKTR5W7hEoHnKNppfUVgAFeJjPi1gez_d-GVAaVIqwZi69YjRJPssYNquim5xXBpa4EI20LEEyG8wRmENr6MbL_WskIzlOiPhBkCrQC-nf1FTHqyJ7UTeLmYJ6uDc2yYlKWeSicH0ftiAdPy4vtUh_SFcMcbHpWt6zpDmBLB3cGWJfrPDtVL1o1qIRosrSDDPoHpIeSAGj5XTIe_Y2DQk3iSCbSkCkYIHRktr4dcY_mhhSDaMUzpHzq9CRlmMR-NoZOirok6mof90mmd51QdPABhDNRng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🇵🇹
امسال مدعی ترین پرتغال رو پس از سال‌ ها در جام جهانی داریم اما جای یه نفر خیلی خالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22967" target="_blank">📅 00:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22966">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXHKOckie4VeR27s3Hm1Yd4CsWTfQXfrXUZrYYOith5Mbv5yudyb3xJZ8FVVTy-83AwVs9_BefCJUsbJI55sRtHSR-kdymBTGCSOsxI5Kd3ugk4W-eKn7a669JcnnXRdcsbEumSZznsRPrWXW152Rjm8zAJHuJG89DBxuW9pSZNzoOE09ks8DYEsSl8tqPxudgtSvN7c-2RbvP8Q5hVzNyxnONzMHqlwxvXPyucvD0xYsgHKnRmEYHY2upAoSJpd6hZqFf6bdnJZKn-X7-StEIj9npONxevxu9GeJ45o6otXOv1yTw-McQVcGxeW-OH_GTFapWDvWNCkT46Y-MtkHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/22966" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22965">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioXls9000qilazXvPj7G_lf83qBbV9m80FW2s8U4iG41Z3OcEmWUi1jkvmr70SbA0O_vkoGbTxUFaxSzWcpGd5qg-mAwWzEK_ucwoTKpbRJrRUiNOQ8UtDs2DZi3csy4raMT_wsrQITRaYfCEOaKwi8BBhDqP6K9OdEaAbRDVBM2wHjz1uezfar2bfmyEj7fqGnArQ8B_Wumj-q8ZUkfIfzApMPocP79YlM-oZJu0Mtb4IzvE7IhO_mv-O22Ik2J5SwwmZ_JTXnqS7nA62wAMeqj0E03Soe67YdMPcWDno14-ZM1EI8Y-ZzY9VGW60kewd5CBHNOL2lUTfDFUnXHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/22965" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22964">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=Pf00v8JaD2nCbGCDZN3AyucHZLbKeTnp89JRGXIOqHBhxWsGDvSOqoZGz2s_qXQC8VuAgt9M7-7NYM-5xuaVYLIbcUhLbaJKgT1p_Bg9T9XVf662NMLWWTiynW0-IfEh8nj7XdocmwgRU6Ha2rInJIxwRRWd1oeew5rfRBx28eiBdJt-Z1RDwLKrB7xSk6pBeFLQKb8B3Go10YE7UNADtoGWStyh77NYylQp1zSrm-uxcPDGOeuMJD-qAFxcPP3w-h6YJXVwOWItzd20XLkrXN6w5ucj6NV5ATUKtRuUbqzZLTLghbMdgj7GpSE9mZqmJNbGVGBAFFPdzEH-s1KvjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=Pf00v8JaD2nCbGCDZN3AyucHZLbKeTnp89JRGXIOqHBhxWsGDvSOqoZGz2s_qXQC8VuAgt9M7-7NYM-5xuaVYLIbcUhLbaJKgT1p_Bg9T9XVf662NMLWWTiynW0-IfEh8nj7XdocmwgRU6Ha2rInJIxwRRWd1oeew5rfRBx28eiBdJt-Z1RDwLKrB7xSk6pBeFLQKb8B3Go10YE7UNADtoGWStyh77NYylQp1zSrm-uxcPDGOeuMJD-qAFxcPP3w-h6YJXVwOWItzd20XLkrXN6w5ucj6NV5ATUKtRuUbqzZLTLghbMdgj7GpSE9mZqmJNbGVGBAFFPdzEH-s1KvjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/22964" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22963">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇱
🚨
شمال اسرائیل آژیر ها روشن شد دوباره  موشک ها از تبریز و کرمانشاه ارسال شد</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22963" target="_blank">📅 23:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22962">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQrDsM7tqFV4IgcEA0fmUsrCfNW7sUNudimynZyZdhFuPTyHNCOPOoBYGAmx4hK2sGKt7dJmuWRRjKcgDn69cIZ6lJYti7juGsL7dgvQPOgKPBoZ5EfZQW3qeuoWxmXxVOnxGkYCuZJuVBS3HKcglcxttWYTcU7_civXuzLCxAHAaqIDm0Eol52X7winIYGR3898z6nXKPT4GLfMAFzxcXIcTcPX7MrsPV9NRB8LccEG65wXHcbpM2lKAI6EtrY6ZmY1ZUCtgkJVE22VDpEK0S9kkD6vu8VBfC0M-EFEv-x2A2FClgInY_L4fU4JTMVS06gOB5oyMqVX8kRQTsVg_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اتحادیه‌فوتبال دانمارک رسما اعلام کرد کریستین اریکسن هوشیاره و تحت شرایط خوبی قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/22962" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22961">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXVstHBr7Wq9XvHJq5QAYfJMyhMfz5pPMGL3tVCYK8g-QwlczlRS_6-6rSU6XRy3xuopJPRmIA7i_qzeZm1shjAmU_LSUpCwVs1ypBq-qDJHBsvnLZXAjhxTzqalPhPTj_K8JAgtj1QYJIXj-C7S_YTGPp753vZI5ZUqP1hLekOhPliBwr-O0D3RNUFMT2uHD9o96wXHRFlmKXW0KOBS5BYWdKdeSjzlFKb6vDbQ_YALtxyPBjXaifsFpQU2Yw6CsUa4Zqe0FkY4KDNoZRUQh83LsxpXsiVbm_ytfGtyaz2m0cm-7Fi-xwATIkD8ebgACbvMnLmo6_5ccMiPPC2wxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22961" target="_blank">📅 22:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22960">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mx_K9Ieeuuvwngr86kRifq37vv0N6NHm5cDPNrBtO4eqSWLt0xJ1UjZR3-6Osj-Y3dYsrYKV8bW34DNh5yCxHcBCEAwoiJHHxDSdm-FYO4Onatk3-M0vZ9-PjhTIqTMjh1YrtrVDI9IkML5vA3d35TwNu4i_5w98y_uU-GSxq1jVCJY2VdqKD_GKKa7NyVlnWHW2lAzsWuPsCj4hZQGy55DRSE1laS0mJMY6e_zv_LbflQykeKaIFsikLvsNPg7j1Ggc9BVZH2VYrsMquLMH4XZBAtgvQEFgL7nGmBi2Mu0ewbrb0UnBp4ep-9NZ6aYziw5YKGxxzoQZR76E8gZjBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری
؛ شنیده‌میشود محمد عباس زاده مهاجم سابق پرسپولیس، فولاد، نساجی و تراکتور به دلیل مشکل قلبی از دنیای فوتبال خداحافظی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22960" target="_blank">📅 22:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22959">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzyvP6bHjNY9ufoABsBDukcv4I76uAwg4IzAvMVF8LxZx7Ss0SvRMcFg783JXcF1akKDZR9uO5c5I5FP-fJrYMi_I3gongj6OLXEzEBE4GljhitDsuOi2ZebDQsKm7vhz5SySCoQqam5i2qvcZ_gM_LSnipwdw37iD1wY_BygEKWDkx6XP2W4corQv-l2zienneLNX8rXixv5EEQUWW-56iDFkg7o6Vcq2U9KnOkd3eQMqgeUxgGk-EZxHQXfXutWZ09RQDiZfle3TUQ3Jr21XyNi7BR5VJEUiE2wYsy1LSx54tKmHhvi_IWeK2mYYqsJpn5l7mZhvOuHb_yuWslHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22959" target="_blank">📅 22:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22958">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=qNR3zL5T1hIfSJAqP-NBgyvvfraiTNZWPYr3M710BiAnZ0AeRGmLYbwSGtWw5UMLNFo0vecKr04uXKMfAJIoDxiirt1ewfzSVbZV4wpRDS_txcpzYGU7BCoknDt94Dh5YBCP4dpcfga6gCl0Qd1jq-PWvvcmzfnbWVDRqb5Kd2YcPTRVyXfQrTjAY-p9aohM6aM5iMjPJ81wKN3mryCpwnkqhOYmLCyUtgF8Oe8bJv38g3veP6l8NYTjEBiPcFbJN_Y0URaVQBIYKxCGG-ZC6XBxCU1yGd7n7Z1YgmKfNJuMD1Z9yJCVHnuaDLnQVL59J39anCKJA6_QA5rCGvNB5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=qNR3zL5T1hIfSJAqP-NBgyvvfraiTNZWPYr3M710BiAnZ0AeRGmLYbwSGtWw5UMLNFo0vecKr04uXKMfAJIoDxiirt1ewfzSVbZV4wpRDS_txcpzYGU7BCoknDt94Dh5YBCP4dpcfga6gCl0Qd1jq-PWvvcmzfnbWVDRqb5Kd2YcPTRVyXfQrTjAY-p9aohM6aM5iMjPJ81wKN3mryCpwnkqhOYmLCyUtgF8Oe8bJv38g3veP6l8NYTjEBiPcFbJN_Y0URaVQBIYKxCGG-ZC6XBxCU1yGd7n7Z1YgmKfNJuMD1Z9yJCVHnuaDLnQVL59J39anCKJA6_QA5rCGvNB5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22958" target="_blank">📅 22:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22957">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhHjWAuNL_N0sXL4CaxNiHOcd6rO4wRHl77e836nJccfOZzbmuW-oOtXqhR4P4Pzkz3G5uxe0q0I0C03FR9HTxKb1FIveC53rlZKfLP8e6-qnSliR7N1d5j6i2rY5wchl63tmIKD1XlCa7-3-RnexA_TxRPvJ_RO51TzIC7xWxNsuHH5FmumVnygBrSXkuiJELxWicH5b8orjKH4hk6lQk2lKzRRKKIAfl2GevgcROYmUFbFLdBxryEKNKU2n-SKqCNe2M3W6Nwf8VpcrBsqDvgKmDjP0M9ZzCB_TUJzHXXVCsEAkJfgDj7IR2kWgx4WMP1F-CEqUI2_CugQ2dukNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ به‌احتمال فراوان آنتونیو آدان راهی لیگ امارات خواهدشد. او دو آفر از باشگاه‌ های اماراتی‌دریافت‌کرده.همانطور در روزهای‌قبل خبر دادیم جدایی آدان از استقلال قطعی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22957" target="_blank">📅 21:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22956">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=jokKGbMTYbZwhKvbWJKlpkDd0IoV5WI8QUqed-vTYmhJF9o8U8B-FuPIZNdgntna_uZqpMIAB_RouEk2nT18Di171gqe8xru8k3epHbBTZzINjriF_SpDQHa1_citbwkJehX29VIHCKiDKxeX6oqbcRkchpUGLmTmKcve-3fi6oxRP5xT88bZeMyy2fUgvMXCP3HL3Sos9ZviQjRU7CW9jcUb_SAfdvZtIXf3db5taMg_K5FG0DWrzGpPyUf68vmpJk1VH-SCr27t3LEMUYcVMApGEJwOX5TqySGDECUxq1pN18VVb8q1Ax-ypkY5XYjyxkqu2j84nsp7MSSdRCVeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=jokKGbMTYbZwhKvbWJKlpkDd0IoV5WI8QUqed-vTYmhJF9o8U8B-FuPIZNdgntna_uZqpMIAB_RouEk2nT18Di171gqe8xru8k3epHbBTZzINjriF_SpDQHa1_citbwkJehX29VIHCKiDKxeX6oqbcRkchpUGLmTmKcve-3fi6oxRP5xT88bZeMyy2fUgvMXCP3HL3Sos9ZviQjRU7CW9jcUb_SAfdvZtIXf3db5taMg_K5FG0DWrzGpPyUf68vmpJk1VH-SCr27t3LEMUYcVMApGEJwOX5TqySGDECUxq1pN18VVb8q1Ax-ypkY5XYjyxkqu2j84nsp7MSSdRCVeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری
؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22956" target="_blank">📅 21:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22955">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVPqda7aB4pymvgSUuUGlum14E6g4BJVPxOQbst3KOrpQqDAEJnkenM7YXNQHpT58Zi9DwGhrcjsD_RMdoGkihot5NXvJ7nP9TrWNZrv8YDuo2Nf18yByLryzgn1HZ5vX7zxO8llUoMxqmQDiNGOaYv9zK6-fwUoBrbVeGv9vInx73kOeamY5lP9p-DM6SfFFHWMPS6scE9vKYUqlgf241iFok7oJHga49j9EsDe-OglmiId5-ypKDTOHBn-0vHoZqCsbU1SuegIKE6k1G3uI8dafzW3txIbBLbYvZHauTGTas4zVcGa5W5VADCjKoNOgi8oHE4OL8CuhCAswsNIYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ کادناسر: بعیده که‌سرانPSG ویتینیا یا ژائو نوس رو با رقم 150 میلیون یورو بفروشند. برای هرکدوم از این دو نفر حداقل 200M€ میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22955" target="_blank">📅 21:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22953">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nyuelfwjv9aBLfeCB0Hw2DzxiqwyGYq2DIAqwydfdXkEu3O8PgZtI3gzoW8D5p2e0Ys1qCsvWN08-I5L24MeQ0GkKCLi7Gc9p5si-wxmfXNNmFd41w9LjYGb4z7cbhPfqdMrcEl2romQQji1Cgw-3d1i9hoNraiCPSFLf9X_vfvbTddf4DwPLzMYn-E_k-TSOwvI5i9Kiov0fGJT64KJZrrvwMJ53rMdnQ4hcmefXvLI1MzGdpqs2Yc_oyEUg9ao4iDKqU-_J0YTcWZKRTWEifXbRX80u42s0KT47RfzwqQdPeKVDOQ0fYtvENuy7Mn4UAApJKYPOqRnvYVZVkk7xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZKsJ_KvZzS1i5NG6cvnjRPeb6je9LgQKHrzcH7R3Ap4twnw4vQI6uB3KE39olA6Q2GsE97RIFIxlinswKTBvmgUfUZiN_I0sKAMCge6jy3hc_543foDqO_9UOw06ofNBpAju_pbPqhkWb6YP4KoG0rkVso0WFm7bzIDhk0XLREJ4-N-uPOXEQVLMMM2KpDBElXsL_OE2XEkvPj-uY0xJaWzBqTTBvG_nNKn7cUVKKkIsJXk-wog36wrL5PwleJY34n6Zzwy-e2jBfBC1DxGF7dr1dgA07m1nRM2QxWNpubcYSDfqv2uL-QeBltDtEmqu4k-F5UJg1eopw8wC4CtS9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22953" target="_blank">📅 21:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22952">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/le0Y9gMQd5pL7gocEUZ1ZWrh_QU2UgpQqU41b1jvGr-Db4or_4YoteaGL-DPW88RxK-pOl_vx2VztwxZDIUewZbn06eHFXV4LXvW6s6iGuPA3UDn2nCRr7Dk6T9HA8um4rJtJD8i5jakyZ3WBQLydxLCwg8sNvAUld_MYaVwBYsdh3qEl3IOwTPF0nwExsfQEhBL6dIN8yAXEq_2mOiCvPy2MgYjvkNBjISteM_E4LHKplzoTDIe0r-3vnPEnzluEyhCIEysMiFoWuTc3SEojp0Sg-7Q2qAMAZpGnf3Jok9ooTMc1TzjXwlAoZF0AXCxwA2lKRhH2WG_7ruy8HJYNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
حواشی‌ دیدارآینده ایران
🆚
مصر در رقابت‌ های جام جهانی 2026 از نگاه هوش مصنوعی ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22952" target="_blank">📅 21:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22951">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=Avj2BJdPSy5EIuYHQZ_t3ZUBzgfqCo9--c6vHt5PKwI8tJttJX0i39Vq4ePM2f7UCgxoBSp9-BPCIk8uxCzv1sSPlmTW6rWNX1Tdn1Ow7XRdBDHG04Wn8Ldsmw-QSIfo2MQVwt-3HLnoK6G4V3QOuPLi89YWxrZjDSuKUl5dUpMteJHgqE_ZVbMFcOozSxycAsu1IxslCj_tlTgMhy4X2R8SrKxoRUaqqbzpzYol_WoqIAAlkQSo7WXAcqCdJ9xGccJSHJpE0tITAY22knGDp5JZKQxfVoW5UiorGFZ7-vqksrWFU6Q3EJiqb0gU6IjsYm-O-JMTO9dikcxDFQsXKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=Avj2BJdPSy5EIuYHQZ_t3ZUBzgfqCo9--c6vHt5PKwI8tJttJX0i39Vq4ePM2f7UCgxoBSp9-BPCIk8uxCzv1sSPlmTW6rWNX1Tdn1Ow7XRdBDHG04Wn8Ldsmw-QSIfo2MQVwt-3HLnoK6G4V3QOuPLi89YWxrZjDSuKUl5dUpMteJHgqE_ZVbMFcOozSxycAsu1IxslCj_tlTgMhy4X2R8SrKxoRUaqqbzpzYol_WoqIAAlkQSo7WXAcqCdJ9xGccJSHJpE0tITAY22knGDp5JZKQxfVoW5UiorGFZ7-vqksrWFU6Q3EJiqb0gU6IjsYm-O-JMTO9dikcxDFQsXKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تیکه‌های سنگین ابوطالب حسینی به تاج رئیس فدراسیون فوتبال درباره عدم صادر شدن ویزاش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22951" target="_blank">📅 20:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22950">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M62TeCCnkjaaQ_hQeQCUlTfa26T4Rn2pRKpODP_nZ-rZbzAUOUT2TVWZd0il8BpGLKaIO6sIHbscVT1m81zlWH6ynOpUmSqKB82opEqg6lPYNx2yQN2vcDxsS5pxkYkJgsEitZ6_zc_wyxzdsfzezwLTt6azhYWLPi3XfeG1zQhD9lJn02IBycJ_6m5oaXur6PiWjWEE8ti41vUtMfGtkOc83dAqZpPQN0t5kzqEyCVAdUrnrG5zGjc8IKllUWpPBLtlis5xpKg3Hbay2L1EqUvSrdsRSHhNWiwwXSzG0X6wn7GS50FT0mGzdA_TYTGsC_cUVEHWk15bHjsBzSQoRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌فعلی‌آبی‌پوشان موافقت خود را با پذیزفتن دستیاری دراگان اسکوچیچ درصورت عقد قرارداد با استقلال به علی تاجرنیا اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22950" target="_blank">📅 20:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22949">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_tvgOSCc1gcVullC7IyNiR150tlwIMU-vOqafYG5_hg_gnFfKWgTJ72vxuM9Vmw5LfN0baXrlGRm5fWloNUBj9Altu2gAR5syF72yWsu70gFIc34a4DNEMroeo7Vjfg9U8xa3ToxBPv9tVPonoJsTiK3o9moGsW2yZc3qyGzW5sL1SaGzmbnuZlS4xjsPCD-zYLJcluU9yhZFQ8rXTTdGtn-ePibRHFQCnPLly_f8TgGo0_NJrPitRYVXgA_t2wMaBM898hNwnM3UMCO3M2WBzEpfuujVUaR_KugiOIut4TL5oQHbw6SZe-x7QfED_cx_pTlGm-NxaV4H9lBTcMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛ اگه کریس رونالدو در جام جهانی 2026 موفق به گلزنی شود؛ به مسن ترین بازیکن تاریخ این رقابت ها تبدیل خواهد شد که گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22949" target="_blank">📅 19:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22948">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqFEiBOO9DjdEGdZh0ENY3EvtqyjBwpbhi2_gxbukxIv-3gF0cQ0kvCu3Jh5xXQhg_DiTFbLKDTVXQmPe_8eWslQK9jEY1xKc6T8M4Ga6PNxn2EbsFItYD9S7KbKdt905FpRabrR0UouT_2uK_XfcpR_u_BGfah_VS7qk9VK2JJhWuVoYUZsOYI74CK6rtgVwkKGxreTzJmVWKbv4mnhu29wonJREL1UhWMW7WnKXa_8zNUOJ5jDH-aBAsTLB15lvjWG1gq9GtUBg11qU16Z-WGFi6dUp0lwxPDRtsG3O6cRDspVkSHbKwbgZEpdR1F0qa_flwjAV3REOYXmhazVmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22948" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22947">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=jcNmzPUDWoeinspjzloWvYhnrmmsIIQwGAEYToQMRzMBX6R6uCsTrSq55GVXOzbGOIzrFuAsORQS_60KTg7_GnWu0dijX0Ew4O_LA8hpbhOVFG6HKYwiB7rgZ3WzY2F1Hm3-8QzRKWV7UKOheOE1PTogXqUVeKjW7FlLSF6_5uQ_QSBr2HC1t1WpJEQ8pgaJy451Abb-mVdz9RnQwKXVuW28pdxI5jOF8GYGVUkdreFCzj-5o8GQX-F60inRR7QgKiAXqlNTQmiw-0idiqELIyoFm8rU6N87dIx5ig01PMfeqogYHacKUHvmf5-frH7m6vGDq9ALSk4H9F-pQi5Qhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=jcNmzPUDWoeinspjzloWvYhnrmmsIIQwGAEYToQMRzMBX6R6uCsTrSq55GVXOzbGOIzrFuAsORQS_60KTg7_GnWu0dijX0Ew4O_LA8hpbhOVFG6HKYwiB7rgZ3WzY2F1Hm3-8QzRKWV7UKOheOE1PTogXqUVeKjW7FlLSF6_5uQ_QSBr2HC1t1WpJEQ8pgaJy451Abb-mVdz9RnQwKXVuW28pdxI5jOF8GYGVUkdreFCzj-5o8GQX-F60inRR7QgKiAXqlNTQmiw-0idiqELIyoFm8rU6N87dIx5ig01PMfeqogYHacKUHvmf5-frH7m6vGDq9ALSk4H9F-pQi5Qhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
آقای‌ممفیس‌دپای‌هستن مهاجم هلندی اسبق بارسا منچستر و اتلتیکو که داخل و بیرون زمین می‌نوازد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22947" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22945">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBJxVpiMn_APjn7How4X3-Q7XsHoQt9v-zfrqUSsoAcoOL1X9qQLbNKwSMct4v3NnlaEa1f8AxjsbCpd6pm9sd3dqDRpAQWtnCErgi3iJXFvk2NaOFaz0_b-l0WgXUFLaON94gvGni-AepoPOGKz5Vy24JvMkGvkFu5AkL5XwsOrpRo6Dj04rCga4jjNlsf8zUWDxFP0gXN5B6aFNbNVCdQEYF74V8lgQSh-_ZCD9lWA7zQoMjR4z5lP2j81qDwifngXxvK7B2q7hUGP6ejnuiRi9q9BOis2X5hk8-StTGNN0BtMwYmoQlSkbdr8mH_-m7F1LKzunNF539_h8eW9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22945" target="_blank">📅 18:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22944">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drzzpQkPAl2uCMrfSyWLV0fUz1-p9Ldu5o2mbuEi_0kgHLuXGjfQrIt4PPJWWwTKp5zvdmpMbhah3Nln5Yy1hP2L5MiFVGHozwlv-HAe_liVWfORQUwQY3g1usglsZUurq0Qc8iXopUPTLE4e0ab4sDSb579VOrAiwNU5c21VrNJzamVa-ac6f5AP33nd3AeNqVez4ycAAs5GRzbWtGuJ-oO4nWCj_EZwELJIHGlQFsn60fPfoxd6qmNk0DemRSv12OwB1LKx6z8OY6T64R-uVkp3JfvRDRuRww2HiThL3shtjWXrOBacqpu1Llgy8mvngnyAsRIewnhj8Gb0jUDpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: منتظرحمله‌این هفته فلورنتینو پرز برای نهایی کردن قرار داد مایکل اولیسه از بایرن مونیخ باشید. پرز قصد داره به هر قیمتی که شده فوق‌ستاره‌فرانسوی باواریایی‌ها رو جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22944" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22943">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3bZ-7h_L2szyoYg47uupvjSCJTVycZyGO8yC4Gn3dLiVskvEsi218eUV0z9CSRN43QZdOwSdLmE6nXbY-n2FTxE933weUzcLecQExKYrJWDNcp0pbGoAYx_Wwq30Zo2kjqA_gwiiq1QTdJxHe6XnX5wZ5k1oTpWIOBBtc6OpZEWd_CGsnsUj5AKPvk2xn57xlT8MpeIboQTrAkbxL-i4gkHkMaJfNUyytolSGs5dgJfRqmXQKIF0TzCX7RXiN1qoMYohQpB0b5FY3MtmV70jon9BhB0s1PZi9Lb6G18Qzhs9VJgWcNc6gg-HVY2uN7GtAD1HNBeN_wxZiVPp5mHGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22943" target="_blank">📅 18:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22942">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=GTVdwfp-wInb2oBAg0i2FnBJb-y1WsOHlEs5RTDvOVTH5gZ10vqEc2iacwCEYptn7_xd5aYKRu6RONeGqQWo-TYIiWMQwzZZ4yhOpr2zGB6hqnvX5I80-AHTehKjJLSBTtRcUEyPLLPFMNuUS6bWqEHdzNSAxK_2H7LEyl9baQSuimySQE5QUbGCfW1KdUEQQf7CZc3Y6icZtcGue2EJm8bXfuMivMdiKNrsdggNyttdBpPEbGN8y4O8txbHugW0SA4xOmawuPMBw_KWB8OjT0AxrpF6XK7GQrNZYWoFc6v11IO9CdQCF7rjz54ZQTJQqrHrJYb8bnkrWkkgo6A_zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=GTVdwfp-wInb2oBAg0i2FnBJb-y1WsOHlEs5RTDvOVTH5gZ10vqEc2iacwCEYptn7_xd5aYKRu6RONeGqQWo-TYIiWMQwzZZ4yhOpr2zGB6hqnvX5I80-AHTehKjJLSBTtRcUEyPLLPFMNuUS6bWqEHdzNSAxK_2H7LEyl9baQSuimySQE5QUbGCfW1KdUEQQf7CZc3Y6icZtcGue2EJm8bXfuMivMdiKNrsdggNyttdBpPEbGN8y4O8txbHugW0SA4xOmawuPMBw_KWB8OjT0AxrpF6XK7GQrNZYWoFc6v11IO9CdQCF7rjz54ZQTJQqrHrJYb8bnkrWkkgo6A_zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظاتی‌از مسابقه‌کاراته‌معلولین؛ این چه حرکتی بود تو زدی آخه؟ چرا از روی‌ویلچره انداختیش پایین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22942" target="_blank">📅 17:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22941">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIoEolGI8V2osxrEUs2nCh7rQRiNdieJ78cJKfJE7gPdKx_ltB8qT-Ggv8-hKuZN9dXGanOsyPkunwz3Y-pVHM6Pn54Zx0PBxFdH0oCRMTWO3B9dEJ0r3aFVF8ufhtnzeiu6rZQAI-t6zBSWkA1zg3JCKh7EkSS4rTsTBmIHZEFHCdxmOuAF9d0-uy58A-vJFJmydf8jn1Q8vSuG1fOf5RbBAlte6yD8LRCifjyrpjYKpJzcmqhCFlyvTLSIXqBneEGVrHJJf_rsUV7HG6v6IIN_pbDtsATquG7fIzwGniIiCz8fT71dunLqYwGANyaF2x0XTe3gbp9dldsI4nA1Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22941" target="_blank">📅 17:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22940">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiLpq3y34qPZ_MrDuVbpwZYuR3JdqLdDL8Pdslv9GGvynEKVGKHFD73wS71KE3OIyO2WtEJdEio8eeqU_0CD8N7b1DUP_EUs2Enc0UgNS_Ur9YoIPvS_JLX0dx8nWzTbJCoa9s7K5G7bthcekdlzDtSB4Tldk0fCM5tkexUVQZfW5QmbIP47d4QN1elM4B6F3eV0x0oqO79qTpp9RvArT2ljszqgZrlxZrhaMVBybpLzoWIIJERuKrFETKb7XcvGU8DcPvAIoPGwriszegsDuTxENZsFG4Yyu9nkQM60x7OftQBU3eZxFq5cMkB1j_-oi0g6SI4nxn2OlgW33NzvWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ مدیریت باشگاه استقلال به دراگان اسکوچیچ پیشنهادداده‌که تنها دستیاری ایرانی‌اش در فصل آینده سهراب بختیاری‌زاده باشد که درصورتیکه جنگ پیش آمد و اسکوچیچ مجبور به ترک ایران شد بختیاری زاده سکان هدایت تیم رو بر عهده بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22940" target="_blank">📅 17:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22939">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-TUHRiqeuQxamOhHvkfXcagcf8wd3bHLJt42ITGoUhQKsza-BM79awcKoDpvKKFoq4xZM0buA6VBu7j6K-OFNsXp69Qo6Ao327EjKBl-el0YvzmWhpjmXJjKYfpdjLzYFEru_FAec5MetfHD9MHax7sTz1RArEZO4g61lwXfKGsjK7GeyQtxMfli3sINcUS0u94w2VhI1g6uv-LoZZ1Hzjv4xVPPoNXP7JuLRFYjdxR3y_fletF8mU1WYekHeVXbWCCRI4ZfcxfmAntfXKCBDI2RcHNR7eMwDEmkQG3TqqCSYC1lif3R2wrMIEJoYAzSf6hCq2Xfku_ncjcRniCOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌ های رسانه پرشیانا؛ باشگاه پرسپولیس در تلاشه که مجوز فعالیت افشین پیروانی در لیگ برتر رو از نهادهای ذیربط بگیره و در فصل جدید رقابت‌ها به نیمکت سرخپوشان برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22939" target="_blank">📅 17:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22938">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kneR3Dv9Cs9peLJgySFTWZDhguG5p7q6tRl9zKRSj0l5u3j9wcL3fH7pf-Sq_4NJ-xDUoiMVLH-5fafIznx48GmNPuagJ2K7rWRjcThFlUwx9zqRSieSSnhSa1itji_IlZSWoyCsJK4DLmgVlN-LtmZ39h1RAKaC3Gn4VVkmzcZMN2mLojr6hxJaThUgUQ7E2-ynwNh16USxnFe2lXv0xrxqOEvvfSUcGt2FgEsk1FUPX3U1QvRR16dZcKntEBJS7cuc-LZSJLI7fB9U2Dy6tS6pR0RumjhsJHNMNy3TGcIPkmiOFTuaHr14hfRM5R_C5mULdw1uMywKaBre8Ndgvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22938" target="_blank">📅 17:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22937">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7XxaP0BNb_bLIisUhziAskUh2N3tnlA-dkMDxdS45iXqhpSJN2KlLzHLb7hxICZTbn4oPgt32Tv54R6XHOoszabwCD66h5cRh-NLSbTpDq-tJg6R0HafAFOfqQCe_w9xtuyItxz8jGNG0R24lVktrlCd-CbWSt5xgmmfLZv9NHdZoAOMHvu0r7ryIqkf48lmfRGRmNA4aD26DCXzX-sjzuu6Q9jNL5uVx_B4u2Yq6qFjsWLk4_cDChe4YPOWCMptO5GbAZd7i7Q9JrmOtK4OLBhSPa03-FkdYUU-Pj_kYmAN6YITIxOm9YI5RBwoH2cPF-PCujZlZ6zodYRBBATqgDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7XxaP0BNb_bLIisUhziAskUh2N3tnlA-dkMDxdS45iXqhpSJN2KlLzHLb7hxICZTbn4oPgt32Tv54R6XHOoszabwCD66h5cRh-NLSbTpDq-tJg6R0HafAFOfqQCe_w9xtuyItxz8jGNG0R24lVktrlCd-CbWSt5xgmmfLZv9NHdZoAOMHvu0r7ryIqkf48lmfRGRmNA4aD26DCXzX-sjzuu6Q9jNL5uVx_B4u2Yq6qFjsWLk4_cDChe4YPOWCMptO5GbAZd7i7Q9JrmOtK4OLBhSPa03-FkdYUU-Pj_kYmAN6YITIxOm9YI5RBwoH2cPF-PCujZlZ6zodYRBBATqgDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اجرا چالش فوق العاده سخت ورزشکار روسی توسط یک ورزشکار ایرانی با رکورد زنی روسی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22937" target="_blank">📅 16:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22936">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPcqtWUgfs5mcB4rUSs3UXjxWmBnuLWJSMXIMZVDLExkeQEAHTAbgjuBgELY3APNkwaw6it6UVlhP4g_ifCVbp5zc6nlZNtJ7Os-MzL_Smcp4lYrCSZgO9H2AdZ-2z0eKRQETGPmS6Kt31tGyJidIqe4psi088V_ncI5nTg7eksDN_rOA0UarD9GqzKqpieITaCR8SfjMZa9dpHYLh7PwPe-5eCglQhMwUb6ygxPFhQ0ZWae_r2i14-8WgdZ5ZBCtVlWzON1akIeQz-vVjCVXkXNm7Ffu9bXbD5X5mOjEcpkl7T2qeNfsOUGu5Jop02PNgiaEN8M206-hxizdXqHog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22936" target="_blank">📅 16:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22935">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Es061gM4o3IpiYI8iCDOttrDv67lXw-1vtVNFvt7z4zvkJC94484LflEJmSjRfV48C4WroI9jN30RQVUtLIq1mtSFAFq0i1_lpDs5Kpc-_jiWjdtX5zlelTofIVSURVLjdzsLNnC2Qry--mGA6BiJA7AGBSCoyIb3XE_k-sqNHDAs7CZbQc68UBclY2fGcYO-uJWFjpr-X46YTevt4IlSKomT_GsWXGJRnYkbs0EbBqdPNtvlU7xbvuI6l0vaEdiflKTWdsErA5pt4c_n5PILNddLN0tdYc8umjV4TFvlQ7nlnr60TDoqSRGASFPi9w6ImAUQD7AVITVeH0f9bUZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌انتقالات|گستون‌ایدول‌ خبرنگار آرژانتینی: با جرأت بگم که آلوارز درنهایت از اتلتیکومادرید جدا میشه. مقصد بعدی آلوارز صدرصدر بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22935" target="_blank">📅 16:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22934">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CECjkkdRxFL9ae5LYt4appFL9EEccoAmKr5WCCpfwSFC5s_7FKstFNpk6pnJX8YD_qIhYRhgy5QVA69q6L3Raj1LHSL9VrKjSxiYQ80Yr-DdaRH1bgmoctTRGKK3CJID2Fe_gPK40I4HK3uo7DPcGZx91VG78vMKLllxGwwndmQfGIBxhmLXT8wvdwAiq4HCroABjQGwT2bed1wjHGnmwCOdDReEXjKuM_vdvwzU4Mo_zhn2-uvKa3sjNZqrkjQM5DShFVDcM9iBRNyTG7lDzhVC-3jNv7geoli7lwjHij4bjLAYoQ7uzgvmqJ19orM1WuenX3Th4IQ4sJLx_ZHNIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22934" target="_blank">📅 16:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22933">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=S4Ql5ux9MPxCTPtAFwrJZDAwdlqrGKCpJXr45j-7kYG3IRVQG0JLjU3H8lbCwmUDvM4MZ22xn_auEnO-Seh3OQ5UWLtJQN3tn26i4tvkIPJYjB-O37aYQTAAZoeI6Xd7pFkJ-LVepuj2IwjUNs0LM7seoq2esLlJ9dk6nq37D5793mJgQZ9ZYeht6ed47EDBcBqYsZ40wea2NcnNuQyWnG3veer53H3XBrKNCzs-rPw1KTk5ovxyU413NOBfFPKLpMXTiEFYqZ07vkB_wfIC1Ykm-xxAYA-L-fVKXh3qxqFENkWszm_UbHXD_lU0EMaRrY28P77N3KIUydlyW0Otpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=S4Ql5ux9MPxCTPtAFwrJZDAwdlqrGKCpJXr45j-7kYG3IRVQG0JLjU3H8lbCwmUDvM4MZ22xn_auEnO-Seh3OQ5UWLtJQN3tn26i4tvkIPJYjB-O37aYQTAAZoeI6Xd7pFkJ-LVepuj2IwjUNs0LM7seoq2esLlJ9dk6nq37D5793mJgQZ9ZYeht6ed47EDBcBqYsZ40wea2NcnNuQyWnG3veer53H3XBrKNCzs-rPw1KTk5ovxyU413NOBfFPKLpMXTiEFYqZ07vkB_wfIC1Ykm-xxAYA-L-fVKXh3qxqFENkWszm_UbHXD_lU0EMaRrY28P77N3KIUydlyW0Otpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آدریانا اولیوارس مدل مکزیکیم رو بدنش عکس تک تک بازیکنای جام‌جهانی رو چسبوند و از دخترای مکزیکی دیگم خواست این چالشو انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22933" target="_blank">📅 15:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22932">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVZu52wxYJ6TI7nv5EHUW6xYmjt2PYMlO0xGMoZjv4Be8qhDwgVDX3IBXqdUMwL86i05KCoJ7S2Vm2oROG5pIDC0nmcjz9x2I69TMdj19ve9tqEy8oUUsojaQdpwb9gaSo7wUMGMhaLvleH3-AmBACa7cOYGqSA38sVllIk9VaBYS-qBf8MZMfCUOHHx9u7YIceKGCMrXmXFXrBo43pfIYCNfaJnxxDjwIsvxtP0DmSTtN7iHxfIO6TA9jlkvge0LOl5nDLY3LPigfo8JFIq2hNDSPk6I6CVX2BmCcur4vLwsvnx-mdd4CNCXCBkbHLLBAllOc95Q1pt9K2acW8zeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
انتخابات‌ریاست‌باشگاه رئال‌مادرید از دقایقی قبل شروع شده و تاپایان امشب هم مشخص خواهد شد ریاست کهکشانی‌ها به کی خواهد رسید. شانس فلورنتینو پرز بسیار بیشتر از انریکه خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22932" target="_blank">📅 15:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22931">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFECN9t6kgRguZ58KZqSdQyaqB383kKj09pvSe6GXh4znLd-JSbBfQQxJl5rkt7x9Hw_go_WFGgO4qajwesvUSmjEM6L4jXlANRWwqqs0n0vE4FusnJ6NyWkeAyvwkw1rvjzFem2OExgeQ9FHflsROGDcAlXqf-59oCRCb3Pay-4vGYHIXWD8Jv8J7zp64bBWvTHKRmNNK6DkpQ4da9AK6WVsTT2xjBTpvbtg8iVzZy8NmV3RzYCcCrTFFmsiJqhm1vSMuQJuD5M5ucZ9hIwSupGgqSrCZEcdUCAASPcKxRPufKrBFmfmbVwMQ8tAWziscy8RlS8ZScSn5CyQtC0aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22931" target="_blank">📅 15:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22930">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgHQ8saVGLhD8aOKlEsf4rLvmzkgP5moaB0M6aA1Qd5hcjpR1V_YslgMKJq1rLPAp-lZG0HYVFh1OSq-LDJ0ieCXXIhkwBoMSytdldnRLeatv5u0vPZcHEGgPG-xZ_LLyPOlgFvaN49qm4XlfRu8bkvmugAyqlRjwKD_vM4LzGwfDnSS1T0sm2xQ8vsIQcr_sx1lgWzx-fHV_aUj0_sw6omscLOzYnd5PgValkFHhGQyPYeBTR6hYEfY-Q4GZFurVarQ9nhudbhvmzucSoNJQOY7IqQq47fCIW3Vxxal1DUdGeU2QMYtxJo9WUzYgePd4OSDjMKJ2_Xs-LkvHU3NXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22930" target="_blank">📅 14:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22929">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXYHYYjSDI1zWgvYWNC0u2GlrCffEmM7IsIIfWh5-H03tNfeBYDuCRphfyUH3q3tmy-1C8UVOcMpJZFWawBn2Ni2aTaMBwMCapL9Soc21T1FRZ5JdsjiYxA5zpNua56ixhOo7_ytkVnMmAmfWEnj8jUIahrVrjyKf_hlpSvypw-y7jsUSMDTiiAgXzw10v70ja3kSmztc24lF-acSvrgJbEEttboKepBlTULD2q3euoPrkmH900v9NSLsEUjuMQwtxQ3SfBz82SkHfvW77cUFFf6QWeOL4nPauX7XFR7pxcrPSvnMFm--M84DgdJ81XeDYOWgu135wn7zGf8c9sAeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22929" target="_blank">📅 14:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22927">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NGvHue1IBP_YhEnl8alMm2MuI92Nc3gFWEDKu7oLgwt3brtf_7ugsVFYA9XN0HAbpr1dQEfcz4TDF-6XgUINEiq6Pu0ZVKQ-2kz5UBalc3bWhzJUJNB-ER6r60I9pdwpmjMAMzTaNSOAX1sB5tPXI4tx6b8eFazPnD6RHVWOKo-lObGh-evP3mnrchZ4F6pFf2wN64FVACCUXnE64Bt1Ykl9U2AbrQmFqNWmvBRoOk4WcfYDyPceM2oogfdlazSI9ktWWCPVUmytUyoab1X6pcJHDaPs-GKQPskUraHeH_7CQkK9bQM1if7UQUnqhuVAk7ErbOPRPiYYmHtlNzqfsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sMfBohiS_j4FbhlPANdlwElfdPF6hsRySUZoV0_irzWtq7nkOXWkJB1liFCaKbLrCfVtKiG99GJSJwfMWT5JR6m1Q8Ldie9O4OEwzoZJITMxDLqf2izzJkopxjldE0VCu3LP4tmpKpJk1muTuHjPZRk3Rw7omgHHyFR5NehteV2cMxQeD7Ubf1CWNvACkic7TcZ1lvQ9sKdOueyzhVBTqxpoZOxZnUO1JviFreykQ-EEnjIu6V-H0ZPjj2F0xZykA3WDE3yibSYGuae05jFBlEsVdYt3OGvEVbveKdkd0oAFHYzZD0gL4OgRwbBwWTTuej1bhWkVd5C9A2FUwnbLcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22927" target="_blank">📅 14:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22926">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sD9wnX29asSV0j2Dzwwde7F_IazhI423GhdWTdZ7od-E5poOMki4VZiwQjo7FicpZaK7mjEut61lBxc3VG1GpOo_tZQ0XwPIjz4txv8BBClsJalReUl5o3O1bsvsJ4kCDZ0l4vOfyMZpLgO-OX-r3_XjhHjQaTFzEOpC_H_dnEq9TPhR1K0y8_ruMeKqfCGJ3QQNtoTzJ3pwkkyHgstUBQv6jaamFL8dc-wMwFMe5Y9N_YTvoPqjCu5ZODi0O-qgoz2MUH-KJXAia9sRbbwJGkk99ObLpD3BedDg1FnEZEdnkcKMMBnY0pNmh3cMSP5c7ewwqU5v6EJ07TF5rZzRTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22926" target="_blank">📅 13:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22925">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgrG7vWKnjG94LX1BXQXNuIC6xtxdPcem-azJr2zsKgtSw4vSXwdXlrMg8PapogFPQk_XOCKh0k2B1NfG3gVIhS0Y5VQKvwUSakyjVZ7SpX-KAwjE2FyZVZq9vgZp5SePncv1BQzC9a5WUbg6beS6eYBqMMriqNUTiAzVkP0Uot_rvQjVyBJMsoMdfFc1TwBGYtL43uD5RcniLDsM-5FBMco6jgpzWb0jsVX6neMIKTKuRz1iPzw4a14yjcSScqU13xreBROKXHKoduFn7yOZi3SJRwz7DHzFHvTvfBNJVZiGFaCEOMJgrAKqpLIV1zlMh03liUdfVmhzDQB1MFm6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی‌کنیم از این ویویو بسیار قدیمی امیر تتلو درباره استقلالی و پرسپولیسی‌بودنش در زمان‌های مختلف
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22925" target="_blank">📅 12:36 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
