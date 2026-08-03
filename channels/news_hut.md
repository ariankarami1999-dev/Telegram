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
<img src="https://cdn4.telesco.pe/file/YY-4eU9szcio3jYsSIK7XMye_jOm4spUPlrh53aQYlFe7ejE6st-wmMG3t7zWAPtrD6i5JUQsT6RtKzCuNhTW363kHclFjTFCoW4I-91UWM-xGK3m0MpXAOXtjqpBTo_feooY1CC_yyLNhhThs6nujWoybJqdUClhDqk8B-ujRkXiGFTFAiLg7b6xHWIHy5R4z5HRuYgqNl39ptnGxBjWCeG-27lynKW2JWmYWUInte4CMsQTTrpAX2IswXKc-1qWoTBqtp50Ci3mgiL9uy_rXsovP4Mv_gqP6PYYZWlrdl8csm2bclFJv9boB6aAacz-bal6nPZtMEqx-MzM4_FeA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 136K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 15:23:35</div>
<hr>

<div class="tg-post" id="msg-69463">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda203069a.mp4?token=amAzFujkqtaFWjrQDf_-_yA-rkkT5FDudEo1oNATqkwNdjoW6vBZ4eUi31c_SqNVH1gQ7CdT5seusrix8FWYClusmre3SAEQsJOMNwEgfDTF1KdwPrLu84HwPt8OKBExdiUljvf5jO0Xe6MWs8AiypxkwoLYri7i8XsdDeXe4VYUiPsk3sxhPqDJVnkct1xqSsefSSiHXNhLqr7EmV8Tat6vJnKv3cjzx5AsJIH1_E3vCXmWBT7rjPfaG7TA1aPxJTljkei41RCVeX0KorJyy6Aeas13qBnglml7FmrN-yPPnW_5DTA_QtlhToL8q-eEcEYPAWKuR_YSx2i3vbFvzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda203069a.mp4?token=amAzFujkqtaFWjrQDf_-_yA-rkkT5FDudEo1oNATqkwNdjoW6vBZ4eUi31c_SqNVH1gQ7CdT5seusrix8FWYClusmre3SAEQsJOMNwEgfDTF1KdwPrLu84HwPt8OKBExdiUljvf5jO0Xe6MWs8AiypxkwoLYri7i8XsdDeXe4VYUiPsk3sxhPqDJVnkct1xqSsefSSiHXNhLqr7EmV8Tat6vJnKv3cjzx5AsJIH1_E3vCXmWBT7rjPfaG7TA1aPxJTljkei41RCVeX0KorJyy6Aeas13qBnglml7FmrN-yPPnW_5DTA_QtlhToL8q-eEcEYPAWKuR_YSx2i3vbFvzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
میزان شانس بقای جمهوری اسلامی از زبان مراد ویسی:
@News_Hut</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/news_hut/69463" target="_blank">📅 15:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69462">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b293a286.mp4?token=jOp4EzRoxa_ToUclpUrGXmjmWYGmPoMCl2ExupTg61EbRw74hYqbD-ulFnc_p32hXQnTO9o9-s4Fa8Dr0Ua2FzGDsDX8AwGHZE5xb2x0ybUAL42vaIwz7lVauQ30E1lfafOsL2gCS8DD9UYWFz0cMQ5dODieMPLa6V2q8cX-gRbWGNQw6YgD7n8S6UYqjcvfYRmOjZiCsBRMxC6mbHM_nRgIMjjsU0Th4KSp7k1StD3kKfDFRWA9ZtR_Mg5G0LdUozoxEeJWcBbGzF3Ec5BzsFMzA12XaaggwwZ8hOyJ2Wn8Bsoi2XmwBioYEN1RcYyQiGvZ7pmFu_JwXilwEybddg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b293a286.mp4?token=jOp4EzRoxa_ToUclpUrGXmjmWYGmPoMCl2ExupTg61EbRw74hYqbD-ulFnc_p32hXQnTO9o9-s4Fa8Dr0Ua2FzGDsDX8AwGHZE5xb2x0ybUAL42vaIwz7lVauQ30E1lfafOsL2gCS8DD9UYWFz0cMQ5dODieMPLa6V2q8cX-gRbWGNQw6YgD7n8S6UYqjcvfYRmOjZiCsBRMxC6mbHM_nRgIMjjsU0Th4KSp7k1StD3kKfDFRWA9ZtR_Mg5G0LdUozoxEeJWcBbGzF3Ec5BzsFMzA12XaaggwwZ8hOyJ2Wn8Bsoi2XmwBioYEN1RcYyQiGvZ7pmFu_JwXilwEybddg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعترافات عبدالباری عطوان (تحلیلگر سرشناس جهان عرب) رو شنیدید؟ کسی که همیشه به مواضع خاصش معروف بوده، حالا لب به اعتراف باز کرده و از کابوس کشورهای عربی پرده برداشته!
عطوان در تحلیل اخیرش (مارس 2026 )به صراحت میگه:
اگر پسر شاه (شاهزاده رضا پهلوی) به ایران برگرده، با توجه به اتحاد استراتژیکی که با اسرائیل خواهد داشت ،ایران به چنان قدرتی تبدیل میشه که تمام کشورهای عربی منطقه باید جلوی عظمتش زانو بزنند و عملاً به نوکرهای ایران تبدیل میشن!
@News_Hut</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/news_hut/69462" target="_blank">📅 14:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69461">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0c3fd91e0.mp4?token=cA-Eag6gaUCeq76vInKMgi0Rw8z8rZ1NhSsanho9D66z-AM-ydujHkM-BuO9UNyF8bV8ZRW4DKxPz8ThW1-jAhwD1XvaBog2BLXG7Ps3DRKmzeALqmpfipoRFH-M4Ib0Meip2vBQoVrEnHoR-5lKm85b2xE2cjKoAC-f4rp4OBPQRwpQX7sd4VxbL00OPy_n0Bo30C51mzviCRD8oXLDcOPhdgly-BSk0vnxG9jLfm5gXFyxiThQaCF8zEY8H1Jpxjfv-7VYhGFAO8FTYO4WZMZEbtAx0MAt7y0Debzl_hr8qLS-6Zq7lUkIq53A2lJqYpC4Qi5TwavR35S2URvyew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0c3fd91e0.mp4?token=cA-Eag6gaUCeq76vInKMgi0Rw8z8rZ1NhSsanho9D66z-AM-ydujHkM-BuO9UNyF8bV8ZRW4DKxPz8ThW1-jAhwD1XvaBog2BLXG7Ps3DRKmzeALqmpfipoRFH-M4Ib0Meip2vBQoVrEnHoR-5lKm85b2xE2cjKoAC-f4rp4OBPQRwpQX7sd4VxbL00OPy_n0Bo30C51mzviCRD8oXLDcOPhdgly-BSk0vnxG9jLfm5gXFyxiThQaCF8zEY8H1Jpxjfv-7VYhGFAO8FTYO4WZMZEbtAx0MAt7y0Debzl_hr8qLS-6Zq7lUkIq53A2lJqYpC4Qi5TwavR35S2URvyew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
عراقچی داره میره اربعین و ماهم توی تهرانیم.
دوشنبه مذاکره ای نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/news_hut/69461" target="_blank">📅 13:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69460">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⏺
اکرمی‌نیا، سخنگوی ارتش:
از فرصت تفاهم‌نامه و لحظه‌به‌لحظه آتش‌بس نهایت بهره‌برداری انجام شد
در این مدت، واردات تجهیزات جدید، تعمیر و بازسازی سامانه‌های آسیب‌دیده و همچنین تولید سامانه‌های جدید در دستور کار قرار گرفت.
پهپاد‌های جدیدی که اخیراً از آنها استفاده کردیم نیز حاصل بهره‌گیری از فرصت ایجادشده در دوره آتش‌بس بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/69460" target="_blank">📅 13:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69459">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08375903ec.mp4?token=ctwo5ZKLKIevmxe_9jZ8wV2-2KMPwHcbcBTMI6Hf8ygHQajX_sHBkJBLc4vvaIVPl3ryBXIyoSgKkhS5A02MuDe6FcIRrJvK_A116Iz17EKQHlrZKdkdHz3rz1ZvtwHqc7rAEb3lGVmuYppMnhwU1IxFc39BfKm-SW4sHdZTlOKeaAgVzyNUlhDWOByoW5fQTfGMP7yHUUPENeVzyFuqj1rItmd87df5lhPEiVTMqgSzXELVCNC_GJl79rXWoG0kapltWiUmzvmTyTMa-hnJz-6bQgs1peg-Mtf10s1_Yk-VeQJwepRB-e9P6w7oHvWlTOCBZOaCOJ82dr1lGniHZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08375903ec.mp4?token=ctwo5ZKLKIevmxe_9jZ8wV2-2KMPwHcbcBTMI6Hf8ygHQajX_sHBkJBLc4vvaIVPl3ryBXIyoSgKkhS5A02MuDe6FcIRrJvK_A116Iz17EKQHlrZKdkdHz3rz1ZvtwHqc7rAEb3lGVmuYppMnhwU1IxFc39BfKm-SW4sHdZTlOKeaAgVzyNUlhDWOByoW5fQTfGMP7yHUUPENeVzyFuqj1rItmd87df5lhPEiVTMqgSzXELVCNC_GJl79rXWoG0kapltWiUmzvmTyTMa-hnJz-6bQgs1peg-Mtf10s1_Yk-VeQJwepRB-e9P6w7oHvWlTOCBZOaCOJ82dr1lGniHZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
نیروی تفنگداران دریایی آمریکا ویدیویی از تمرین‌های تیراندازی نیروهای خود منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/69459" target="_blank">📅 12:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69458">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyhlkY8AYq9funs8NOug4tksYtptTfekwBFpUOZwlUjaNEsaVdwRMkeffOk_UrREB1qm5_5dV06QtRpRbvhdmSsH2S2imrcWRFAeFKXN9Whm5hmVT86B7bdrn1IyqtpHpVyK8-m0Qh9fSaSaleSDkiaanCXaH9PB76GMs5N9VIbZ1W77mKkZ3HS2-Pb_HkfQIeTHST2hZ0kpDfyPDq9_UMC74SfwHBRJQdiGICF10Zhk5J-UYCJ1rIQKYo8idGJ5flwDikH3_Zl77hvJJ0yUiKVa71SS_Y4vWuFCrJ_m1SaKP9jGhQE8Xz5Lf9xGFwveBQlFYbyX0pxESdMXc32NVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی، سخنگوی وزارت خارجه:
ما در حال حاضر هیچ‌گونه مذاکره‌ای با ایالات متحده نداریم و مذاکرات با عمان بر دستیابی به توافقی پیرامون عبور ایمن کشتی‌ها از تنگه هرمز متمرکز است.
هدف، تعیین مسیری موقت است که ایمنی کشتیرانی در تنگه هرمز را تضمین کند.
تا زمانی که محاصره دریایی و اقدامات ایالات متحده ادامه داشته باشد، هیچ تحول قابل‌توجهی در وضعیت تنگه هرمز رخ نخواهد داد.
🇮🇷
اسماعیل بقایی، در واکنش به ادعای جلوگیری عربستان سعودی از حمله آمریکا به ایران:
اینکه همه کشورهای منطقه اذعان دارند که از تحولات و شرایط آتی منطقه متأثر  شد، امری مثبت است.
جنگ ایالات متحده علیه ایران، جنگی علیه کل منطقه است.
طی پنج ماه گذشته شاهد بوده‌ایم که حضور ایالات متحده در منطقه، موجب افزایش ناامنی و بی‌ثباتی شده است.
طبیعی است که کشورها برای جلوگیری از تشدید ناامنی تلاش کنند، اما تجربه نشان داده است که هیچ‌چیز جز قدرت و توان بازدارندگی ایران، مانع دشمن نمی‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/69458" target="_blank">📅 12:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69457">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5b3706c487.mp4?token=qg_5UzcXVRCXktS90XlIXy2NHWCEvKXEzlp1dBRMvjuQVJn-JvlZP1366oXK_cD-8gvc2EVLUIfKZVQGydIOIsSle0hXweQOHjDGIhgfddhdbevLL2ldiLE2syAlD07hxFCDjHsh7UWqnT4QPToe7ZDcesWvUBECw6QUXArHYG1VZ2dUKn0-MygOWsh4W-rS1OaXNrt8yP7rtVaQLcRRrFJpOtDZtrlizG5m9NzBDmiaG-kz6SazoMFbtqZ_uUknbBnX-jpziBfrSqfbS6zmvrgHXF6lteFGkKtdKjlsjOvdga-z4-or8RUM5dWoeS0YxS89RRn-De0Ek6Ee0Xx1Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5b3706c487.mp4?token=qg_5UzcXVRCXktS90XlIXy2NHWCEvKXEzlp1dBRMvjuQVJn-JvlZP1366oXK_cD-8gvc2EVLUIfKZVQGydIOIsSle0hXweQOHjDGIhgfddhdbevLL2ldiLE2syAlD07hxFCDjHsh7UWqnT4QPToe7ZDcesWvUBECw6QUXArHYG1VZ2dUKn0-MygOWsh4W-rS1OaXNrt8yP7rtVaQLcRRrFJpOtDZtrlizG5m9NzBDmiaG-kz6SazoMFbtqZ_uUknbBnX-jpziBfrSqfbS6zmvrgHXF6lteFGkKtdKjlsjOvdga-z4-or8RUM5dWoeS0YxS89RRn-De0Ek6Ee0Xx1Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حمله پهپادی روز گذشته به مرکز لجستیکی عظیم شرکت وایلدبریز (Wildberries) در نزدیکی سامارا.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/69457" target="_blank">📅 11:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69455">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGUpokH7Ij-jtv-FwGsKpEjaEQ2VKd8pWFrmxDhSIODySUd-toCiPCEgxHhd-cSz7zbh5tK3dUbtUL1p6k2B5BOayKmoy8LLhgbqoqrdSGiSzVJ5i635w5K6a6kAGXa84sb2A3WzxMIxqHjK5LuLS21mlSA83aMsGn2YoySGkDuI1bY_xMvMkhnDgmBGVJIoYkllxzcuSCshH1Ct-zDeASshi9rpBVfMFBxIO8evp-m4aXGLvAtNrGBS0rVtzEJMIkYFFF71SVQYreJg9Lkv1a41kOkC-e4PH_VpbxlLQ2OFIChZAIIsHh-BxnNeKEv48XA0Dmv61AvR32PQ5ACUEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429ab83ad5.mp4?token=NfMJxKI86r_p96HQ7FEYIcVj8ecNwbrQWb63spYYUPHYdHxBdYkceppoPPuG7zxRdBR5u2S_OhEgejHu2RdgmQjbf3_3v31VIHd2jHXemwihnpE_onaQhAsiNOlRby5EGGwi0ufKu4MpGmVDu6CqagSMFwITAMyyaPPcuIWDmzwr8cgrfy81z6XF2A24rPvZghuJQABCnFWLL-eOk1oxHbWhMbZOCwxUbIKXkPgkJCBE5dq8SZWykatMCq2PsC8yhbntW08HzMYX5dY881-jLgbU29O3WbKbEgtdD7oZB1vA5LZn783JOKmcYvXvCFA5aM3QUDgv0Yeav-TSqW87GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429ab83ad5.mp4?token=NfMJxKI86r_p96HQ7FEYIcVj8ecNwbrQWb63spYYUPHYdHxBdYkceppoPPuG7zxRdBR5u2S_OhEgejHu2RdgmQjbf3_3v31VIHd2jHXemwihnpE_onaQhAsiNOlRby5EGGwi0ufKu4MpGmVDu6CqagSMFwITAMyyaPPcuIWDmzwr8cgrfy81z6XF2A24rPvZghuJQABCnFWLL-eOk1oxHbWhMbZOCwxUbIKXkPgkJCBE5dq8SZWykatMCq2PsC8yhbntW08HzMYX5dY881-jLgbU29O3WbKbEgtdD7oZB1vA5LZn783JOKmcYvXvCFA5aM3QUDgv0Yeav-TSqW87GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده مردم در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/69455" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69454">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f06a84a2.mp4?token=XtJaBmYfF_6Xdio9FJjElrpA5kAAdQM0eeiQM_sLKmAblUKxajjbSpB59AsVJof2HGtrVT78XKn5VhOK-N4J0E8wc7RdTTzDXLNcEVswn_YviXNUD8UJkjaWoR4UFREI0-rIraIdAeGF-o1_Ya-dgNplP0QI4uWihuIdAvwRDqZuCTmHuOvvoRDBUEIcu7twrEo30KwATDVClG0adM0SXemcLMQ7DBecrlgJ2oJoM4jTnJKiW-GhUY0SiqniMnUAX0T9_Lxd-Yd03GmX0IhLoUf18uh5XPubaeTwHkvLJZcH1HLrmyoNPyDHYe0qAnLOUYMdhYiFo6yaUE8Pk6EnGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f06a84a2.mp4?token=XtJaBmYfF_6Xdio9FJjElrpA5kAAdQM0eeiQM_sLKmAblUKxajjbSpB59AsVJof2HGtrVT78XKn5VhOK-N4J0E8wc7RdTTzDXLNcEVswn_YviXNUD8UJkjaWoR4UFREI0-rIraIdAeGF-o1_Ya-dgNplP0QI4uWihuIdAvwRDqZuCTmHuOvvoRDBUEIcu7twrEo30KwATDVClG0adM0SXemcLMQ7DBecrlgJ2oJoM4jTnJKiW-GhUY0SiqniMnUAX0T9_Lxd-Yd03GmX0IhLoUf18uh5XPubaeTwHkvLJZcH1HLrmyoNPyDHYe0qAnLOUYMdhYiFo6yaUE8Pk6EnGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای ازجواد موگویی که توی برنامش داره خیلی شیک و مجلسی جای همه فرمانده‌ها و مسئولان رو لو میده:
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69454" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69453">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=gkL6GzPf-jqLQpCs7fKNRQCi06Rp2DdUhF-eAieN52a9Mrqor8I9XvQzMnoTUc_mhdHZiIFML6NCOXU4z80oFHK1C4z9VmPf_cQxnfbYNBQKN4np9HX4BLNVdGUhokSWj1WRJCG68Ys-42HDavLcvjQ4uqE6__9LLVqUblLjaC-U75g8AI8E9tr_Oz7ODNDP0w7algQnb31hKSkHO4_cXmIgpHO1Qavmlj-4URjA9ruED8LbRCMOtPUt1Z_LnxdEmccZkXe6O6z6K_7YlyhlCM7fQepiNPvkTpJxUxB2YrIDhNgYSjcIT_jc9tcVJ8zrQAMJPMuhRURThlnshLkYVFmW8vr1PjKY43PaiTvD3nQkELpD5Z5BD6gnXhLqBrtL1-uWe4quTmAeRKaoHcCgzUaMszioy-IFFvmUoBOJTvFo0mimR8hPwicoUHJ0rgqM12u_yMQzLkKt4ZLMsdVEs_OjoJknJ-KFukh_fWwxhRQ4xlUPKzTLpyQ_42q20Y0wB3NagJKOcATzwghn6IAORUXL4ZbNtW0MqzTTZC8KbqUP1T-CDhYFanq0TlIXQ71DxmLau5N7UWpAHstldpPJNAvO3ZPjKc-c4tkuALgsyobP-XkUfZ5c6b2J4OFARqSYGR_djsfR0kM1pbrUpvQCIpmFy7fKKAm5oMFuseUr8Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=gkL6GzPf-jqLQpCs7fKNRQCi06Rp2DdUhF-eAieN52a9Mrqor8I9XvQzMnoTUc_mhdHZiIFML6NCOXU4z80oFHK1C4z9VmPf_cQxnfbYNBQKN4np9HX4BLNVdGUhokSWj1WRJCG68Ys-42HDavLcvjQ4uqE6__9LLVqUblLjaC-U75g8AI8E9tr_Oz7ODNDP0w7algQnb31hKSkHO4_cXmIgpHO1Qavmlj-4URjA9ruED8LbRCMOtPUt1Z_LnxdEmccZkXe6O6z6K_7YlyhlCM7fQepiNPvkTpJxUxB2YrIDhNgYSjcIT_jc9tcVJ8zrQAMJPMuhRURThlnshLkYVFmW8vr1PjKY43PaiTvD3nQkELpD5Z5BD6gnXhLqBrtL1-uWe4quTmAeRKaoHcCgzUaMszioy-IFFvmUoBOJTvFo0mimR8hPwicoUHJ0rgqM12u_yMQzLkKt4ZLMsdVEs_OjoJknJ-KFukh_fWwxhRQ4xlUPKzTLpyQ_42q20Y0wB3NagJKOcATzwghn6IAORUXL4ZbNtW0MqzTTZC8KbqUP1T-CDhYFanq0TlIXQ71DxmLau5N7UWpAHstldpPJNAvO3ZPjKc-c4tkuALgsyobP-XkUfZ5c6b2J4OFARqSYGR_djsfR0kM1pbrUpvQCIpmFy7fKKAm5oMFuseUr8Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مارک لوین:
تداوم توقیف دارایی‌های متعلق به ایران
ادامه محاصره دریایی برای قطع درآمدهای نفتی و گازی ایران
هدف‌گیری مستمر فرماندهان نظامی
حمله به کارخانه‌های تولید موشک‌های بالستیک و پهپادها در سراسر ایران
هدف قرار دادن ساختمان‌های دولتی و تأسیسات متعلق به سپاه و ارتش
حمله به بانک‌ها و مراکز مالی
دست‌کم تا ۳۰ روز و شاید بیشتر، هیچ آتش‌بسی در کار نباشد.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/69453" target="_blank">📅 10:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69452">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/998caf4317.mp4?token=aIXm5xWibsa_RPwJlHvk1xWy0hmboMDss-87RH7Yexf4WcSulX7IAMh-KFPM0BrtSTvrglh86buNOy3T5nUKTQvPrrx0Kj66DNWWUUPIOeinKC9zIfeu_09E0eTL8WQkfBBQcBFcGsuX5XWIG-tQWd4Wl12_yX43twDZyR3fXmJZiuOTqv5T1hlcDEZ6GEbpShXLr7qp3cmU5JYCmLA7HxuQ9PzmJA8iSS7piLTvCjiordTWyLgHNZda4uQ79G56cXAAMVnJaVl8bU7TBbSKSDtkrzobwCP2NxYz5fdtb4RJLgU82LZuefrbPV9NIHz6-UsPTxUP_5Ig2cDqn2tskXqIS0_oVw7UWkDFIzKlmKkQoVh5VQuVYX3H5UcTRl_bltBA0xLgrZEkwBr84pNLkanCU6D8_9S-Ao3DuPb57x0BjniGFtvw0ULfyPVSQIFqy4TtPNaMMSCHni81RXkdveMO7Ixobs2lsx7vP7asib5WwZ8GycI-jtyJ0OKU08mHr2wt6R8tOLsG4Be0dClFWgjC1SDRAgOdVz2jz9bobKw3fYJBpSOvFXS8qHN_Vq-LYIgLdGgEQvf6vv6C1BGDbp784T3nwXMaCVq6jm1sNRga-gLEWeMjfH7ff3u775AG6U0WsS1i6t4rS1k_9IV5kaqZAWnAMKUFygk6PRYG3BE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/998caf4317.mp4?token=aIXm5xWibsa_RPwJlHvk1xWy0hmboMDss-87RH7Yexf4WcSulX7IAMh-KFPM0BrtSTvrglh86buNOy3T5nUKTQvPrrx0Kj66DNWWUUPIOeinKC9zIfeu_09E0eTL8WQkfBBQcBFcGsuX5XWIG-tQWd4Wl12_yX43twDZyR3fXmJZiuOTqv5T1hlcDEZ6GEbpShXLr7qp3cmU5JYCmLA7HxuQ9PzmJA8iSS7piLTvCjiordTWyLgHNZda4uQ79G56cXAAMVnJaVl8bU7TBbSKSDtkrzobwCP2NxYz5fdtb4RJLgU82LZuefrbPV9NIHz6-UsPTxUP_5Ig2cDqn2tskXqIS0_oVw7UWkDFIzKlmKkQoVh5VQuVYX3H5UcTRl_bltBA0xLgrZEkwBr84pNLkanCU6D8_9S-Ao3DuPb57x0BjniGFtvw0ULfyPVSQIFqy4TtPNaMMSCHni81RXkdveMO7Ixobs2lsx7vP7asib5WwZ8GycI-jtyJ0OKU08mHr2wt6R8tOLsG4Be0dClFWgjC1SDRAgOdVz2jz9bobKw3fYJBpSOvFXS8qHN_Vq-LYIgLdGgEQvf6vv6C1BGDbp784T3nwXMaCVq6jm1sNRga-gLEWeMjfH7ff3u775AG6U0WsS1i6t4rS1k_9IV5kaqZAWnAMKUFygk6PRYG3BE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇮🇱
🇺🇸
ویدیویی جدید از لحظه بمباران خیابان فردوسی در زمان جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69452" target="_blank">📅 09:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69451">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHXFvf14gxyCa4uwNuBQqigDbSZzwNcjl1mJFtV7IGcNhqxvC10N5K8IMeXM60ImltRYxepGipdvhht0CAvehqlBLEvZe3KDySK4EMpMxjZvzqYBgPHAi43gb82cV_mm7OzsUf87hX3knls0mVPWFJGXHkRZBjvYyft4vPvrxlcpqUMBG9rTtb-nUywdk81D2OZtBox8_GTnoc3fA2eKbIQ7we4WESep6zLwe_go5Rf2o0KOIiPo4rNe9Y77mVSr5tRu1NTzM7SC59lZrhgTLx2nasRDcqzsFU456llWY44auYqMy2Y8j3Q4t8JE80yRtzx8XdIdQ16B2STBdYelXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
هگست وزیر جنگ آمریکا:
واقعیت.
وزارت جنگ آماده‌ی حمله بود - و همچنان آماده است - در سطحی که از جنگ جهانی دوم دیده نشده است.
قفل و بارگذاری شده(آماده اقدام).
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69451" target="_blank">📅 03:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69450">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TCzMS5UUZ1BMM78etqNXzlE-bpbage7ASx2FXjT3jLDmTJmxAkw52oijgqgkKCAgrnMAv9Yd6-Gdz4Kael2sVxKK1C9LQeMkVMA3Lh9Pis2J_nCcLYl8pL_0Oj-iXHVxzEaKrqvoOAa9__c2KTcEwnDd3p_QbIOaXLqEeKRUDKRtiQ-ysXRFdCaIeaQeOAs359YaNGkJiVcu67e2z8KMtIXSu_KD52vTTMF2leN0_UpT_QfHepGBKUlO8Gb_ZQ7J42mUHyboIu5XqeIpa-u8XPcyMkoRA8U17FlPb6LcRENNrM4TmF-brNMQQy3tNPjsF9A97TfApSiRRBzZ0rd0tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پست جدید کاخ سفید:
به ترامپ اعتماد کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69450" target="_blank">📅 01:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69449">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQlVjXNY8AM4H02TICyOvXO1FH2DQwXnw5hL8qqGuG0KSTwclleQhVKJ15SYLTLz4ZKwI5ViwirfotJ6J-zhvfkVQvz1E1VwvdI-3eFpe9kAE3uC09FTRB7rMabVcA9zCherditXwJgkJvI031ipfPaINukqX9IESz9HO6PLDc9N1cRnedyVppG_kyzI-ZMvcQVoncgj6j3cGuRBFVNGKQH5_a8LjRYTxo4GPHtgq6xxHSF63pmnVy6imp1Nh19cy77E0VudCLx7ptSSFEEA5xSfr0zH68cqpFkSTO5uFd5GZDscBr9FQGAss0gyK5jX11s8zrYHbirolD2shN2nvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی مبنی بر وقوع یک حادثه در فاصله ۲۰ مایل دریایی شمال‌شرقی خصبِ عمان دریافت شده است. مقامات در حال بررسی موضوع هستند و به شناورهای حاضر در منطقه توصیه شده است که احتیاط کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69449" target="_blank">📅 01:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69448">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
وسط حرفای ترامپ یه کشتی تو تنگه هرمز هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69448" target="_blank">📅 01:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69447">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac4e8fdd53.mp4?token=AWTRENLFkXwEotFpTmvoNi7qoRMUM5PEUmHMUeH63hLgFxykxZmWMPoQJ0dH1zfLu9RMby-y3cDJKl6fgYy8TiivGaxIq8ODnFKUnB8dpiSF2CXZ2ADKL3jFDJpSJ7xQAEBzE-OHYfpegpEKT_-7ggcCxmSocj0hcXZeK2KPmgwiCobP5yDB9TfXzBOUmdHc74L5khuzfZ4IvYtF0oZZJC7rGdrMuQy549Ru4GZSESdhDzVN67MtR2jPel9TW_FYjO0uAedPm1sNwWSPm2zRoEewgmAfgvAkNJfoyL2bGkUF9qhNoVYYixQhndg8A8JrvlY3YZywK_eOOT98mGEDXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac4e8fdd53.mp4?token=AWTRENLFkXwEotFpTmvoNi7qoRMUM5PEUmHMUeH63hLgFxykxZmWMPoQJ0dH1zfLu9RMby-y3cDJKl6fgYy8TiivGaxIq8ODnFKUnB8dpiSF2CXZ2ADKL3jFDJpSJ7xQAEBzE-OHYfpegpEKT_-7ggcCxmSocj0hcXZeK2KPmgwiCobP5yDB9TfXzBOUmdHc74L5khuzfZ4IvYtF0oZZJC7rGdrMuQy549Ru4GZSESdhDzVN67MtR2jPel9TW_FYjO0uAedPm1sNwWSPm2zRoEewgmAfgvAkNJfoyL2bGkUF9qhNoVYYixQhndg8A8JrvlY3YZywK_eOOT98mGEDXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
نمی‌دانید این حملات به کجا ختم می‌شود.
منظورم این است که آیا همسایگان ایران با هجوم سیل‌وار جمعیت به کشورهایشان مواجه خواهند شد؟
یک فاجعه. اتفاقات بد بسیاری ممکن است رخ دهد.
ترجیح می‌دهم توافق کنم. به دنبال کشتن آدم‌ها نیستم.
آدم‌ها می‌میرند؛ خیلی‌ها می‌میرند. ما چنین چیزی نمی‌خواهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69447" target="_blank">📅 01:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69446">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/320bfbc7f8.mp4?token=CVp1UQY7NOZO-G5buANGUMaTS6H8ZdCjPQEaXS7JvGT_X7JdaG6J0bGPv3mwCl4y1XM_K-4vXSTaZt0wclSn_xHKegoEIt7vbc75uY59g6BVtPhd80bdTBZ-8hTf-Fiotr19x4prKo9HjrUxs0r4u4mlUl4pK2TkHRr93Ud_wQnnMoOv1vw8YHamsiNcNcmTg4FYoce4OkGUxfXnRxi6wtuapbIZPW_eUOeEoDyFCtiqHyFZ9KDO9q9s_w-JzLcERKLIHK8OA13HrhPJlYfiQW8RfVlCbyb6-9VnXhFit8fy5DPTqkg8hvTiirfHcRvy5Wf0juGU3lDRZnID2eZ6rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/320bfbc7f8.mp4?token=CVp1UQY7NOZO-G5buANGUMaTS6H8ZdCjPQEaXS7JvGT_X7JdaG6J0bGPv3mwCl4y1XM_K-4vXSTaZt0wclSn_xHKegoEIt7vbc75uY59g6BVtPhd80bdTBZ-8hTf-Fiotr19x4prKo9HjrUxs0r4u4mlUl4pK2TkHRr93Ud_wQnnMoOv1vw8YHamsiNcNcmTg4FYoce4OkGUxfXnRxi6wtuapbIZPW_eUOeEoDyFCtiqHyFZ9KDO9q9s_w-JzLcERKLIHK8OA13HrhPJlYfiQW8RfVlCbyb6-9VnXhFit8fy5DPTqkg8hvTiirfHcRvy5Wf0juGU3lDRZnID2eZ6rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد ایران:
ما حمله‌ای داشتیم که می‌توانست بزرگترین حمله از زمان جنگ جهانی دوم باشد.
این حمله برای آنها فاجعه‌بار می‌بود و آنها نمی‌خواستند ما این کار را انجام دهیم.
صادقانه بگویم، عربستان سعودی هم این را نمی‌خواست.
آنها فکر می‌کردند که توافق قریب‌الوقوع است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69446" target="_blank">📅 01:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69445">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4635f3df1.mp4?token=qU-GdSz8BNNHbwIAeFDz8HzugE1SnQ0hAtURh7qg_bcfmycoLfSXchL9ej53DAa1mzjCGBJOpbmOtJcTCgLx1tQinitxUusez8ybN4GH3rY8g886sclcfbD78mPOFTdwXCJq3QRWJIXgRLolE6-2HTGwoZzfvn7rJCq1yaaDuTAW-7HbQ5bd78e9wW7VdY18YKYaWJ35CM5niyqVMsBIsD_hq18ZVcYm7zfFyuY4xWYQqF1HznYZ0D_rHheD_NR3D9Zhnx0l-Z5bEr4ePzZYHHHZMgDsZ66ThgXv3CGSxvXEtizNy0aT03_zoxFGSx4dxRG1ocdACeIjOjSi06sTDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4635f3df1.mp4?token=qU-GdSz8BNNHbwIAeFDz8HzugE1SnQ0hAtURh7qg_bcfmycoLfSXchL9ej53DAa1mzjCGBJOpbmOtJcTCgLx1tQinitxUusez8ybN4GH3rY8g886sclcfbD78mPOFTdwXCJq3QRWJIXgRLolE6-2HTGwoZzfvn7rJCq1yaaDuTAW-7HbQ5bd78e9wW7VdY18YKYaWJ35CM5niyqVMsBIsD_hq18ZVcYm7zfFyuY4xWYQqF1HznYZ0D_rHheD_NR3D9Zhnx0l-Z5bEr4ePzZYHHHZMgDsZ66ThgXv3CGSxvXEtizNy0aT03_zoxFGSx4dxRG1ocdACeIjOjSi06sTDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
قرار بود حمله‌ای گسترده باشد.
آنها از ما خواستند که این کار را نکنیم. گفتند: "لطفاً این کار را نکنید."
همسایه‌هایشان هم همین را گفتند.
ما فقط می‌خواهیم ببینیم که آیا می‌توانیم به توافق برسیم یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69445" target="_blank">📅 01:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69444">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ad85e5d7.mp4?token=K8ARUyN_azeqFM_MKRHk1okislVINMm99jAacN9ebJ7R5Za3S8fm8rTky9b1JS_CtD0fWWuFD_yFN8loXREr2jfx6dgWM2uuHGdF7bBta4P_qZ0_qVPZun0tmVZiTCbkZeYkiHQCft2MHQjZBMa29aI9_QNwldb8fd7c1ztpzKH3Eks8RLkT92VJLczGZkVzqQWjGQNEwUBxuUVCvIWkeGlKbc-sh9vsIlUSEsPg_9OIQ15ZamM2okjSzBg_aMG4sRU6ZOIIc-vxLKKTOpl83n13NszXEq4_ZP6U0vW8ZsOOh1yIXUJbVbARjaW3U6adWetKk4sBeBBvurywTuiLcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ad85e5d7.mp4?token=K8ARUyN_azeqFM_MKRHk1okislVINMm99jAacN9ebJ7R5Za3S8fm8rTky9b1JS_CtD0fWWuFD_yFN8loXREr2jfx6dgWM2uuHGdF7bBta4P_qZ0_qVPZun0tmVZiTCbkZeYkiHQCft2MHQjZBMa29aI9_QNwldb8fd7c1ztpzKH3Eks8RLkT92VJLczGZkVzqQWjGQNEwUBxuUVCvIWkeGlKbc-sh9vsIlUSEsPg_9OIQ15ZamM2okjSzBg_aMG4sRU6ZOIIc-vxLKKTOpl83n13NszXEq4_ZP6U0vW8ZsOOh1yIXUJbVbARjaW3U6adWetKk4sBeBBvurywTuiLcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره بمباران ایران:
گروهی از افراد هستند که خیلی دوست دارند من این کار را انجام دهم—صرفاً انجامش دهم—و گروه دیگری هم هستند که نمی‌خواهند من این کار را بکنم.
🎙
خبرنگار: آیا ایران برای دستیابی به توافق ضرب‌الاجلی دارد؟
🇺🇸
ترامپ:
خواهیم دید. من به دنبال کشتن مردم نیستم.
از ولیعهد عربستان سعودی پرسیدم: «ترجیح می‌دهید ما چه کار کنیم؟»
او گفت: «ما توافق را به حمله ترجیح می‌دهیم.»
🎙
خبرنگار: گزارشی وجود دارد که می‌گوید شما در حال خارج کردن نیروهای آمریکایی از کویت و بحرین هستید.
⏺
🇺🇸
ترامپ:
نمیخواهم در این باره اظهار نظر کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69444" target="_blank">📅 01:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69443">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098cb6b6b9.mp4?token=NomW06NuG-SA8x2-gsb7FqI41deodzj4op0YriP3LENSrGSGUwJ-7wv16OfFkvxVHr5oHvxtWmYVwB9M2l5FyfJZurFOwL_FXeEnTOfOmntUpG1fn3la0Kfg5TkilITrHj7OLaDQyX1bCDW2O0cDzNJKtifcv1FNtiCImvEt_-AzgHVq8bKLcDrTnedSTde75npcSgBZCAUeWA5R0mU8AV0CJb208w2CIY2YMl3c9TpyVJun4j5TcDqW07y0jZGdgjEz4kMrHL_l5utYSm6VPfOcNGSWi2Yr8klKbZY0CL2GqJ9CjgKG4lLezpQLhkAz4GN-hhRFDeHPsIiagmo88Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098cb6b6b9.mp4?token=NomW06NuG-SA8x2-gsb7FqI41deodzj4op0YriP3LENSrGSGUwJ-7wv16OfFkvxVHr5oHvxtWmYVwB9M2l5FyfJZurFOwL_FXeEnTOfOmntUpG1fn3la0Kfg5TkilITrHj7OLaDQyX1bCDW2O0cDzNJKtifcv1FNtiCImvEt_-AzgHVq8bKLcDrTnedSTde75npcSgBZCAUeWA5R0mU8AV0CJb208w2CIY2YMl3c9TpyVJun4j5TcDqW07y0jZGdgjEz4kMrHL_l5utYSm6VPfOcNGSWi2Yr8klKbZY0CL2GqJ9CjgKG4lLezpQLhkAz4GN-hhRFDeHPsIiagmo88Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: در مورد ایران، حالا چه پیش می‌آید؟
🇺🇸
املاکی:
ما در حال گفتگو با آن‌ها هستیم. این گفتگوها از بعدازظهر فردا آغاز می‌شود. این کار جان‌های بسیاری را نجات خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69443" target="_blank">📅 01:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69442">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992fe6ee4d.mp4?token=PPcQndbI2jLrYmbbRkFn_Cv63l1zycGafZy1tGtN0bdvjjXEWwlQGY9e6q2slhE8X-aU2-YLdw8Vj4ioEnQ1ljwYFbdLcOT5kY1G4fLRA6mfR_k_BiOy1lRvpsTzsdPjFyYchUj-n9t4UohvvH60wk6Yo9nmUIS3mRqE2psryiPOWzAs9mGe1syNMQvB_Up49toWCVD1wwO86rrfrhsLHkeiS53pYERPmg1CGg3WS9rrTFv7NB-ShSJdZQc_ojRHDYKZMk9mcRgh9SeVKrDs0DJRL3VRJiqamUg1vPZmsH2y9BGI-BzwdWNl5NrLFXDP7bNVUO9z_B7iAsHjuK1OWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992fe6ee4d.mp4?token=PPcQndbI2jLrYmbbRkFn_Cv63l1zycGafZy1tGtN0bdvjjXEWwlQGY9e6q2slhE8X-aU2-YLdw8Vj4ioEnQ1ljwYFbdLcOT5kY1G4fLRA6mfR_k_BiOy1lRvpsTzsdPjFyYchUj-n9t4UohvvH60wk6Yo9nmUIS3mRqE2psryiPOWzAs9mGe1syNMQvB_Up49toWCVD1wwO86rrfrhsLHkeiS53pYERPmg1CGg3WS9rrTFv7NB-ShSJdZQc_ojRHDYKZMk9mcRgh9SeVKrDs0DJRL3VRJiqamUg1vPZmsH2y9BGI-BzwdWNl5NrLFXDP7bNVUO9z_B7iAsHjuK1OWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ در مورد ایران:
عربستان سعودی، امارات متحده عربی، قطر و ایران از من خواستند که حملات را متوقف کنم.
حمله بزرگی می‌شد.
وقتی متحدان خواستند که آن را لغو کنیم، باید گفت: "خب، ببینیم چه می‌شود."
متحدان فکر می‌کنند که توافقی حاصل شده است. توافقی در مورد هرمز وجود دارد و توافقی در مورد هسته‌ای خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69442" target="_blank">📅 01:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69441">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/661dbe4eff.mp4?token=gYm8Zwq2tlYclVz707nAiGsy8GhAs2CUEGHYFVi6iPtLynS1I3XR3crZI8ZKrjQ3aOQBPM3nXT8UcQ3PsNhc6r9aHnfHlwOiKozwgyLf7cm7sjETk4fxPK7elk4s3uYhfl62KiTln-2w-CGwfM2QaI1NlTc0XsElrtBEBPM_snWIpb7OMr2CYCk4ImbWiznVFbFT6cQh8wK6oQldzQuvYDqdjO4r0TuQyHXqRORAtbWNuju4tG0SfenWVaXsWyNr9ToSQCpc2diN00Nwnu_-OHcvNCBXA-UGtTqhGEwL-tbBzFSf1LNPQWmrFB6jLlscGHZjYPJ9-kP262CV645iPA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/661dbe4eff.mp4?token=gYm8Zwq2tlYclVz707nAiGsy8GhAs2CUEGHYFVi6iPtLynS1I3XR3crZI8ZKrjQ3aOQBPM3nXT8UcQ3PsNhc6r9aHnfHlwOiKozwgyLf7cm7sjETk4fxPK7elk4s3uYhfl62KiTln-2w-CGwfM2QaI1NlTc0XsElrtBEBPM_snWIpb7OMr2CYCk4ImbWiznVFbFT6cQh8wK6oQldzQuvYDqdjO4r0TuQyHXqRORAtbWNuju4tG0SfenWVaXsWyNr9ToSQCpc2diN00Nwnu_-OHcvNCBXA-UGtTqhGEwL-tbBzFSf1LNPQWmrFB6jLlscGHZjYPJ9-kP262CV645iPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی وقتی می بینه دلار شده 190 هزار تومن و آب و برقم هر روز قطع میشه:
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69441" target="_blank">📅 00:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69440">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93362f281c.mp4?token=Y5NJuv7jOcFx52BWy-W5lW9nBKeO_qRyQ2kjwHvGKfDwcu1KspCPXAnMuaVN926gxkY3ZrEaELfyfT11-ZO2mExiRp4ri_4q7tR4XtuPEGirsGU_air3aGDxeowLRi1rhPn56uVxyd55XjPeD-y9npyX57XKmeklCIT1mf181OqzEY0LXBafYiJvaqM8_HIo4y6ATB2cuSdCHwNPiultJxd94ZE-zxs0NnVn1645QIuC5V3j7ofpBRvH3_JrOjh7wIcyC_de2AYfJoNdAKN9oLHs1SAoVJ_Y5hkSuCsOevYbLpIZz6sG3cI13LiXVVyqx7FTh_53FwD5oX9hzgZ5hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93362f281c.mp4?token=Y5NJuv7jOcFx52BWy-W5lW9nBKeO_qRyQ2kjwHvGKfDwcu1KspCPXAnMuaVN926gxkY3ZrEaELfyfT11-ZO2mExiRp4ri_4q7tR4XtuPEGirsGU_air3aGDxeowLRi1rhPn56uVxyd55XjPeD-y9npyX57XKmeklCIT1mf181OqzEY0LXBafYiJvaqM8_HIo4y6ATB2cuSdCHwNPiultJxd94ZE-zxs0NnVn1645QIuC5V3j7ofpBRvH3_JrOjh7wIcyC_de2AYfJoNdAKN9oLHs1SAoVJ_Y5hkSuCsOevYbLpIZz6sG3cI13LiXVVyqx7FTh_53FwD5oX9hzgZ5hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال:
شوت برنده در مسابقات قهرمانی باشگاه بدمنستر! از تمام کسانی که شرکت کردند، بسیار سپاسگزارم.
من با امتیاز 70 برنده شدم و از این بابت بسیار مفتخرم، زیرا برخلاف سایر شرکت‌کنندگان، زمان بسیار کمی برای تمرین دارم، زیرا تمرکزم روی مسائل دیگری است.
این را "استعداد" می‌گویند و من آن را دارم، در حالی که آنها ندارند!
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69440" target="_blank">📅 23:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69439">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsLd-lYl8htLb5cAZrksQQrvay1Lv9EBY74jh9Db94QYFkh6XjqyKYn0_hdEfzaEwVK7D-lOiVhQTt2fnA_vCzrpA5bvl-gFQ23IWGxaFKKDHqNiIn2PvmfOlx5pfChD1FvtdvhKRAJd1C5VZnl1X-Ywyk0Y0Z-mkkjUNKZtP55aGd_4t46C50r1pY-JoFJ087J727rsB0uLXTlXVJq-4pHTxaS1f_pjps6_XZ99aVciXsHHYCJ_jpACbdtTC_5g3Wt7Qhm_stACSFgTVcML8PJ3K4o8839ZtwvY9uZyMoiHflQIn72mBuU7va0OAjksIc4KO-TXabpxxTEYOU7Q8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پزشکیان:
تفاهم نامه که امضا شد حاصل خرد جمعی اعضای شعام بود
این تفاهم نامه ثقل روابط خارجی ما توی آینده هستش و باید دشمن رو وادار کنیم بهش پایبند باشه
امنیت کشور و منطقه و هم‌پیمانان با این تفاهم نامه ارتقا پیدا میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69439" target="_blank">📅 23:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69438">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⏺
شکار و هدف قرار دادن ۶۷ سرباز روس توسط مولتی روتورهای اوکراینی در اطراف پوکروفسک
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69438" target="_blank">📅 23:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69437">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f93e085c7.mp4?token=rK8JWYgmHB_Bs9ViQ26L9b5GNCli_-ulgpQ0PUbNwJQNVT_lPtq6DEDl6VIIvw5lAAljIMx8LzsYOFevIgnBpyPwUJVMn_xDwnJWC-AU-6Jp0Eb-ZuSohxMKcBmxR9ak_5tRXuQ4kqYEna4UclJFOx-Obzp7du3IhhmablvgDJRfjxTrIvFQ2FsM6TrcIlqcuv76rzTFy9BdhfWlxOOjNH9H5uU9SNeBJoEVn1etdhJKArorV1jnWGLnKIFSag2k7mVfmJIOseePrbKjoegqncKAFNpoxM3013spqBr7PtV_zf82ftF6biI4R5BDFc7m-EFWIpO8ZhXokaiuk-HG5Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f93e085c7.mp4?token=rK8JWYgmHB_Bs9ViQ26L9b5GNCli_-ulgpQ0PUbNwJQNVT_lPtq6DEDl6VIIvw5lAAljIMx8LzsYOFevIgnBpyPwUJVMn_xDwnJWC-AU-6Jp0Eb-ZuSohxMKcBmxR9ak_5tRXuQ4kqYEna4UclJFOx-Obzp7du3IhhmablvgDJRfjxTrIvFQ2FsM6TrcIlqcuv76rzTFy9BdhfWlxOOjNH9H5uU9SNeBJoEVn1etdhJKArorV1jnWGLnKIFSag2k7mVfmJIOseePrbKjoegqncKAFNpoxM3013spqBr7PtV_zf82ftF6biI4R5BDFc7m-EFWIpO8ZhXokaiuk-HG5Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌‌
‼️
روح الله قرهی رئیس حوزه علمیه:
«وقتی ماهواره به فضا می‌فرستیم، می‌توانیم سرش را کج کنیم و خود آمریکا را بزنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69437" target="_blank">📅 22:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69436">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4MEqkCzjjRRxUQUKTk4F5FCbtDXfSFKRCnFGl4cC-sDvN8UXMCxUCGjUPxkepV3cq65zN8CAD2glBg-1-BQfm3w_UH2EcmZ_etJ4r11LNVlzhOH2c43RxzEZRACq8QTIV4IdjYoWEbzYmy_FpHFIr98Y7qhEQ0Kz3CKv9kqcjDBICrj1ugCPZnZDMR4gAQf7mP1aXsD3YmQfJGWv4PylycqG3IxrF4F6VIooIH9UEDcBgBgXZT8KuupQJI0zyJQ1cbXu-FIub4Qt8_v5HBMKjDZwFr0mXmksvWOsNTlg_Co2Svjh86Xqr7KXbr64ZHpHQFOhlKC29ezIVgmNUHQAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
کان‌نیوز به نقل از یک منبع امنیتی:
رفتار دونالد ترامپ — که منجر به لغو حمله گسترده به ایران شد — به توانمندی عملیاتی آسیب می‌زند و آن را تضعیف می‌کند.
این مقام امنیتی گفت: «این دومین بار در طول یک هفته است که ایالات متحده اسرائیل را در جریان حمله‌ای برنامه‌ریزی‌شده قرار می‌دهد که می‌توانست خاورمیانه را تکان دهد، اما آن حمله در آخرین لحظه و بدون هیچ توضیحی لغو شد.»
یک منبع اسرائیلی نیز افزود: «با وجود رفتار رئیس‌جمهور ترامپ، آماده‌سازی و تدوین جدی برنامه‌های آتی دشوار است.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69436" target="_blank">📅 21:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69433">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Dd87kvz72qdAtWSt8xWvTqEzo89w9nH7ZQDBJDlP32Aqe0m_G3dNvVZj2STggXDP_oeh_IEFhd89uXhd-piXa_atmFWrgaR8VNWhNKyFXgAyHsCZJ2COa05BszJ7zT4puq3nNtm573s3y7WhpM8uvJ14ZCt34TJzQAI0gYk3P8Dfdj4spXfg8_be8kZVT4pvEvFV2Res_rU98DCUczlZK6qPMJPGYcO39RbjhT10jT3izJVWtNipaRTFieYdqHYqC1uhwxBt4Lx4z_OeCHLT4pjjje-dPOOqBk2bpD6oVecKfKFINdaxAighfzkaM7zKbgyq8vaCbM7Ej3tdfZb5OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/98190fb3e2.mp4?token=XnEwoNsZ03YX0Z-sAg9F95uBj9FOLVnAPJm4gsKmypLsPulKdjs0NcWI-sTWvSHqHoUO0kVUBmADMofhjV3RmYB9ftRTly_LtwtCLRC3QSRFO-eh_0jDMbYO7kxkzORxBZze8Y6SrQl2Xgst2UMz_cuXWo-rkFX1cQAhvc7EJiP5MhsWhhLaU1xxO2RI66ssLZ93ERzWbrMSCE-aE9bu0uMMeBBpAu5x1T40frc8eH-CRIGhWeRXXWlVAOnepJvVoR15dJoj8ChpWy46bgqooHe7Q2YTeKK0AWVx_Hw-TmBQ4zyyOoi1FERNaHFOsEDAjmTVV2Z8hx4z6HeSPjXbgw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/98190fb3e2.mp4?token=XnEwoNsZ03YX0Z-sAg9F95uBj9FOLVnAPJm4gsKmypLsPulKdjs0NcWI-sTWvSHqHoUO0kVUBmADMofhjV3RmYB9ftRTly_LtwtCLRC3QSRFO-eh_0jDMbYO7kxkzORxBZze8Y6SrQl2Xgst2UMz_cuXWo-rkFX1cQAhvc7EJiP5MhsWhhLaU1xxO2RI66ssLZ93ERzWbrMSCE-aE9bu0uMMeBBpAu5x1T40frc8eH-CRIGhWeRXXWlVAOnepJvVoR15dJoj8ChpWy46bgqooHe7Q2YTeKK0AWVx_Hw-TmBQ4zyyOoi1FERNaHFOsEDAjmTVV2Z8hx4z6HeSPjXbgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
انبار شرکت Wildberries در منطقه سمارا دچار آتش‌سوزی شد، این اتفاق پس از حمله اوکراین رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69433" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69432">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5208110eae.mp4?token=XbBcsf17yCuz1FT8w_LVkwbVvnseEdycyrDJv0fpQ8BrV_n46Znl5KCqsO9GRS7dNh5og60Fb89h2QzGTNIsdHa2jgkSbRQuvcxadW-DS-MZvyJw3Y89CNDPHc_pes6-TsDytw7qz63JIpybqXm9N49_qLeVK3lh-wYTjYZ9fbnBImK7SYi7bxB67JOGicrKW8sl3z86GGD4eLJbNwXqQ7ivODiokPa3bN8b9pI9U26qiLfkVXr7b2nRGgk3n3bPvD33xTn0rWOM_6qewFhhpyyZfzcaYBANnTe-L6DrdTFJb3f-4c2HI7EuK2lnxJ-l0mon7GilvHxi2BZxP0pdmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5208110eae.mp4?token=XbBcsf17yCuz1FT8w_LVkwbVvnseEdycyrDJv0fpQ8BrV_n46Znl5KCqsO9GRS7dNh5og60Fb89h2QzGTNIsdHa2jgkSbRQuvcxadW-DS-MZvyJw3Y89CNDPHc_pes6-TsDytw7qz63JIpybqXm9N49_qLeVK3lh-wYTjYZ9fbnBImK7SYi7bxB67JOGicrKW8sl3z86GGD4eLJbNwXqQ7ivODiokPa3bN8b9pI9U26qiLfkVXr7b2nRGgk3n3bPvD33xTn0rWOM_6qewFhhpyyZfzcaYBANnTe-L6DrdTFJb3f-4c2HI7EuK2lnxJ-l0mon7GilvHxi2BZxP0pdmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی امور خارجه، اسماعیل بقایی:
مدیریت آینده تنگه هرمز توسط ایران و با مشورت عمان انجام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69432" target="_blank">📅 20:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69431">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04acf28261.mp4?token=XEcZSALoPXZIAs2oWloLRMOIXAZ1JFxhGQdbUBPLN8sL6hqNEWYMeKS-YFNAzh_N2WKHGZEq58LGH-whfMsF17GhQNDvUgDEvUrDc0TxCUliY-ptJT20WqwtYRR4tyjbov3WSd5XeO6oNwCZPKJDbZFCIQWbjtq8CFhCQRRo0lUjaO_TzfBVWZZ0keSPut9nVKg3-FyqhbT_4P_yxBhszGfOKS7JgksE0jKe_TJoXVydb0R44u84DNo3MLYewCk2QHRP9MhrjIy2jh1oZkUKCg7W-_X9XatKEf-gn0lWKWDC5a4TuQmkcdFbUpW_DGPqhdOVs3yQCGtvghy1YdqGnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04acf28261.mp4?token=XEcZSALoPXZIAs2oWloLRMOIXAZ1JFxhGQdbUBPLN8sL6hqNEWYMeKS-YFNAzh_N2WKHGZEq58LGH-whfMsF17GhQNDvUgDEvUrDc0TxCUliY-ptJT20WqwtYRR4tyjbov3WSd5XeO6oNwCZPKJDbZFCIQWbjtq8CFhCQRRo0lUjaO_TzfBVWZZ0keSPut9nVKg3-FyqhbT_4P_yxBhszGfOKS7JgksE0jKe_TJoXVydb0R44u84DNo3MLYewCk2QHRP9MhrjIy2jh1oZkUKCg7W-_X9XatKEf-gn0lWKWDC5a4TuQmkcdFbUpW_DGPqhdOVs3yQCGtvghy1YdqGnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی وزارت خارجه اسماعیل بقایی:
توافق ایران و عمان بر سر مسیر جدید هیچ ارتباطی با بازگشایی تنگه هرمز یا حفظ بسته بودن آن ندارد.
مسیر جنوبی از طریق تنگه هرمز با ناامن کردن منطقه و آسیب رساندن به منافع ملی ایران همراه بوده است و تهران آن را نمی‌پذیرد.
مسیر مورد توافق نه مسیر شمالی و نه مسیر جنوبی فعلی خواهد بود. در عوض، مسیر جدیدی خواهد بود که هر دو طرف متقابلاً بر سر آن توافق دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69431" target="_blank">📅 20:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69430">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8dec97ea.mp4?token=KOeMvZI2E5EWKnN4PlLEZnQlFm33F4zNVCuDhGfKb8KjiQt5n9xeRxal381oeCEoQ1V2zFDRHnw6WK2uxcl4OPSVzNolnf64QwLWtci7JYzd8WsBOkaPvuouAxAr1xbc5cVcMDlEdoLKK6C4iF37Gg_SbnMGu-NFZqbo0Xvq3JhuhmNKDaqmMXcv2HcpXryvoq9d0bjgE2MyWTDUJPv4vJ7ptitcZIVrR6ekByzvoNrVkWH39ACyYB7xLy-YNnfqZWdqpsuNwjMKxPnkw_CWbc9x6yR1ijPmV-MBcWWRe1_FzmFDnWbsf1gRvZqLwU6i6VSa_2ti1eicrWxK45Dj2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8dec97ea.mp4?token=KOeMvZI2E5EWKnN4PlLEZnQlFm33F4zNVCuDhGfKb8KjiQt5n9xeRxal381oeCEoQ1V2zFDRHnw6WK2uxcl4OPSVzNolnf64QwLWtci7JYzd8WsBOkaPvuouAxAr1xbc5cVcMDlEdoLKK6C4iF37Gg_SbnMGu-NFZqbo0Xvq3JhuhmNKDaqmMXcv2HcpXryvoq9d0bjgE2MyWTDUJPv4vJ7ptitcZIVrR6ekByzvoNrVkWH39ACyYB7xLy-YNnfqZWdqpsuNwjMKxPnkw_CWbc9x6yR1ijPmV-MBcWWRe1_FzmFDnWbsf1gRvZqLwU6i6VSa_2ti1eicrWxK45Dj2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کارشناس صداسیما:
مسعود رجوی (رئیس سابق مجاهدین خلق) فرد باسواد و کتاب‌خونده‌ای بود و قطعا خیلی باهوش‌تر از رضا پهلوی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69430" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69429">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=TSC0r0MbQruwXFQj5KKRoyXSJHhBrkyY7JaiMjJfNGYnnEWCkTsCe7eZ1ceobWIk293JwDZMzxg8wkGUv8dncP0_L9gzvJ5KOA9nbdPijd__Xmw3oYh5KMDt61oWyc-DGyUfu4qlRqks13pIE-vkmGO_QkADzmGIHym8HHmlm8QbEvBUSyjOreGlh_C0mf4f7aOrq7h932QjnEdg6n-BsC5EnHZtm-W9grVGQTkUnz6omctCQscz-PV34P-le3GiZ40wEORUWnJR0SqdaEzWo-A8sRl8GsF0bKU96zpXDuWbXdTK_eHfe8hYH3pC3FhyoApZJn1N7e8eM0LTRhfZQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=TSC0r0MbQruwXFQj5KKRoyXSJHhBrkyY7JaiMjJfNGYnnEWCkTsCe7eZ1ceobWIk293JwDZMzxg8wkGUv8dncP0_L9gzvJ5KOA9nbdPijd__Xmw3oYh5KMDt61oWyc-DGyUfu4qlRqks13pIE-vkmGO_QkADzmGIHym8HHmlm8QbEvBUSyjOreGlh_C0mf4f7aOrq7h932QjnEdg6n-BsC5EnHZtm-W9grVGQTkUnz6omctCQscz-PV34P-le3GiZ40wEORUWnJR0SqdaEzWo-A8sRl8GsF0bKU96zpXDuWbXdTK_eHfe8hYH3pC3FhyoApZJn1N7e8eM0LTRhfZQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رادان:
من یه مشکلی برام پیش اومد که گفتم نمی‌تونم در جلسه شورای دفاع در نهم اسفندماه شرکت کنم و غلامرضا رضاییان، رییس سازمان اطلاعات فراجا به جای من در جلسه شرکت کرد و کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69429" target="_blank">📅 19:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69426">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=TyfR0YIo30LIG7zScGYGKMHnsvvRo9DkOr5QO18o_uueq3UO4W6lwLPMCRmPoUi0bxfIlPNCvZZmy5D8lK8VR9aD4L6IwJRIa85JpVtJXBBI0FOiwK6AIIdkpQ2JPVaS4c4ukWVjM8r2Vl89EioMShtBbjODR4oU-_3F6jAQlVfAaBOH39Yz6a-6CAl-Ohzxb86Lxe4ezkXNsgHX3Ne8Rx2ozSsLdxpkJVCMnFFlXFNrMaG3_-8-0oPGoA7Lk4NhDDgXiHO26g9JtWE6lzDruyoVkHEo4aQucOuqR4I8l3Ws8-OWmB2-6Sou02CD7t1xK_mMkiZauaMlNCjWl2rS2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=TyfR0YIo30LIG7zScGYGKMHnsvvRo9DkOr5QO18o_uueq3UO4W6lwLPMCRmPoUi0bxfIlPNCvZZmy5D8lK8VR9aD4L6IwJRIa85JpVtJXBBI0FOiwK6AIIdkpQ2JPVaS4c4ukWVjM8r2Vl89EioMShtBbjODR4oU-_3F6jAQlVfAaBOH39Yz6a-6CAl-Ohzxb86Lxe4ezkXNsgHX3Ne8Rx2ozSsLdxpkJVCMnFFlXFNrMaG3_-8-0oPGoA7Lk4NhDDgXiHO26g9JtWE6lzDruyoVkHEo4aQucOuqR4I8l3Ws8-OWmB2-6Sou02CD7t1xK_mMkiZauaMlNCjWl2rS2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💋
🇮🇷
این جنده‌اینستاگرامی که خیلی ماجراش وایرال شده، یک‌شبه تصمیم گرفت بره تو آغوش حکومت و تبلیغ اربعین بکنه، چند ساعت بعدشم ازش یه ویدیو های
🔞
عجیب منتشر شد
🔗
⚠️
مشاهده تصاویر و ویدیو ها
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69426" target="_blank">📅 18:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69425">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae764e4921.mp4?token=pMMvXzjg5EXqNvK-ZDecz1nIgPTGXz2IhTMSP3wGlgpaHsIbWNR-jGOn7WosZKoLdpdyLC69zn3PwUtWD7A_PZ4OZkaItAY_7B7H5ithdnD07Ihj9k3Z18J98XNlU6CUhD2ZDx1tSy9VrQRZ1RNX2Z7vS2PneZHoJI-j77nfy5IdDEgBTfunuLusNUigAye-rXdm--YRRYEqyJUGnmNR78n16HvupcKoLOnWi23IPViJ33vcI09ojeo5sT2XlWGFRTjfkEQhHIJuYrEUW88NpXHR77yX9ccdh-GIjpZfpnLcFqFzjeGUOFBWr7H-YlErHNkiW0t1vBg8jHatuD3zYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae764e4921.mp4?token=pMMvXzjg5EXqNvK-ZDecz1nIgPTGXz2IhTMSP3wGlgpaHsIbWNR-jGOn7WosZKoLdpdyLC69zn3PwUtWD7A_PZ4OZkaItAY_7B7H5ithdnD07Ihj9k3Z18J98XNlU6CUhD2ZDx1tSy9VrQRZ1RNX2Z7vS2PneZHoJI-j77nfy5IdDEgBTfunuLusNUigAye-rXdm--YRRYEqyJUGnmNR78n16HvupcKoLOnWi23IPViJ33vcI09ojeo5sT2XlWGFRTjfkEQhHIJuYrEUW88NpXHR77yX9ccdh-GIjpZfpnLcFqFzjeGUOFBWr7H-YlErHNkiW0t1vBg8jHatuD3zYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوند پناهیان به پزشکیان و قالیباف:
همه پیامبران را مسخره کردند؛ از تمسخر نترسید و با عظمت صحبت کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69425" target="_blank">📅 18:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69424">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🇮🇷
بیانیه سپاه پاسداران :
انتقام خون رهبر شهید و اسماعیل هنیه اجتناب ناپذیره
پاسخ این جنایت بشدت سخت و قاطع و سخت گیرانه خواهد بود
توطئه خلع سلاح حماس به نتیجه نخواهد رسید و از همین الان شکست خورده بدانید
دنیا بداند اراده ضد صهیونیستی ادامه دار خواهد بود و پیروزی نهایی فلسطین خیلی نزدیک است
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69424" target="_blank">📅 18:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69423">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc039adc5b.mp4?token=M0SrIJ2yJf5SAy99gPy0qfJ_vcEuel9LQ0YL4wlMpVNZTwdS8uCS-LNomjozvE-JEyH4Tribhnglt58eskpKIL-sY3JBZLoyME9i971RqdxItsI8akF4oMkSulyN05Bdg8QKCGdWxrf74z7XRVPFAcyR2qiCvA7mELMoRwGsYI2pPT6FXARdWZut3HLfx1XStE-p8tYmHFnSJePcWyIihrUmFHfatIVCIEVhM3YmeQQ48h--eNb0JVW34xu4gDeakuvWAls4zakfRsvqA2KPdnZ3VWYi4tSntA5XzDgmY_2nlpIRsOLeRlWJolRuB1yiC9nIp6QrogNESMkrQ_igxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc039adc5b.mp4?token=M0SrIJ2yJf5SAy99gPy0qfJ_vcEuel9LQ0YL4wlMpVNZTwdS8uCS-LNomjozvE-JEyH4Tribhnglt58eskpKIL-sY3JBZLoyME9i971RqdxItsI8akF4oMkSulyN05Bdg8QKCGdWxrf74z7XRVPFAcyR2qiCvA7mELMoRwGsYI2pPT6FXARdWZut3HLfx1XStE-p8tYmHFnSJePcWyIihrUmFHfatIVCIEVhM3YmeQQ48h--eNb0JVW34xu4gDeakuvWAls4zakfRsvqA2KPdnZ3VWYi4tSntA5XzDgmY_2nlpIRsOLeRlWJolRuB1yiC9nIp6QrogNESMkrQ_igxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو هلیکوپتر آتش‌نشانی در حین مبارزه با آتش‌سوزی جنگلی در نزدیکی پساتا، یونان، در هوا با هم برخورد کرده و سقوط کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69423" target="_blank">📅 17:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69422">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bef1baf0f6.mp4?token=lq8g9JmLPkMkC5dALz2WhK-g6boGXBfx2Ft9XuLXIDIqElxw8MZPcgU1QIw42GulsDCeC14VQfsYGeUJG0h9zCYJ4JaaVGIhmBbJ9zUDGdoQN2gpyTaBbY-HpUd-8vp7mCqcYI3hPBV2wyD0lMXzePTZz1EI9iuySS5hzVoQZzRge_CG2l8a5gW-L0HeaFME1sol4ZnviNjuqsONsIFxx-ggfRsmTCKIXZ-omb_T9tXVicuToVdW4X0_bBy7odvuw3shjmylareX-UOk-JfTfQHfZ_MIkK2mA4PInXXVMHbsgDiTgVsXE-l5EiF5Fbg5W7D26IpZULBaxDnJHnk3LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bef1baf0f6.mp4?token=lq8g9JmLPkMkC5dALz2WhK-g6boGXBfx2Ft9XuLXIDIqElxw8MZPcgU1QIw42GulsDCeC14VQfsYGeUJG0h9zCYJ4JaaVGIhmBbJ9zUDGdoQN2gpyTaBbY-HpUd-8vp7mCqcYI3hPBV2wyD0lMXzePTZz1EI9iuySS5hzVoQZzRge_CG2l8a5gW-L0HeaFME1sol4ZnviNjuqsONsIFxx-ggfRsmTCKIXZ-omb_T9tXVicuToVdW4X0_bBy7odvuw3shjmylareX-UOk-JfTfQHfZ_MIkK2mA4PInXXVMHbsgDiTgVsXE-l5EiF5Fbg5W7D26IpZULBaxDnJHnk3LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلقک بازی اینو ببینید توی پخش‌زنده صداوسیما
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69422" target="_blank">📅 17:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69421">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ga-AUs5v9RbuRd8iXkCJCpqhkw9i825yKhtAuP0LQ-drha4aJHg1EX1WBKQwSA3FAhUnhJPe1hLIzxXXFdTMhDQWVmahpI3hZdE_zy0ib7gS77cL2uFIEUu8amMIc34S3xLOY_fHkA35UVx6dYl7u-wl80nFy2gL7ibSQd90iPAudZ3U-M0_M7TxPbkCr3lh_X82qp_0Ku755s7-GtT9Esj7lC52zgTk-xhfrOJfsKn91HrmLeSqVQ1d2rnaYNZ7F8hud1BX-oJrQSVHzEJkudbb6wscHWRjLnJXLg0k23N9kAjc9aKCM7cZiS1jFQFF7HoALv3g3ZopK-UXOuHlyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
نیویورک پست:به گفته منابع آگاه، در حالی که رهبران اعتراضات در تلاش برای دستیابی به سلاح هستند، انقلاب ایران ممکن است «هر لحظه» رخ دهد.
چهره‌های مخالف حکومت در تهران به نشریه «پست» گفتند که خیابان‌های ایران به دلیل اعدام‌های در ملأعام، فروپاشی اقتصادی و جنگی که بیش از پنج ماه است ادامه دارد، به مرز انفجار رسیده‌اند.
یکی از رهبران اعتراضات با اشاره به سرکوب بی‌رحمانه ماه ژانویه توسط رژیم — که به گفته رئیس‌جمهور ترامپ منجر به کشته شدن ۵۲ هزار نفر شد — گفت: «انقلاب ممکن است هر لحظه رخ دهد؛ مردم خواهان انتقام هستند.»
یک روزنامه‌نگار مستقلِ فعال در جریان‌های زیرزمینی ایران گفت که تدارکات برای خیزش بعدی هم‌اکنون در حال انجام است و فعالانی از تمامی اقشار جامعه مصمم‌اند تا ضربه‌ای نهایی و تعیین‌کننده به رژیم وارد کنند.
این روزنامه‌نگار گفت: «ما در حال بررسی اعتراضات ماه ژانویه و تشخیص این نکته هستیم که چه تاکتیک‌هایی مؤثر بوده‌اند و کدام‌یک نه؛ همچنین نقشه‌ها را تحلیل می‌کنیم تا امن‌ترین و خطرناک‌ترین مناطق برای تجمع را شناسایی کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69421" target="_blank">📅 17:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69420">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7XZuacneHUXrM4yvSwuNanoG9DMnjBgKH2cf1E1D1azDnNUtTSOxCYZHhnhG2cIOZprrrqqNw24bh01rjtYQG5xvdE8Zyd633uzDioDaYYBVD1_eBcl7VNhh8gpfu_3yfIF1zfeWPudmPQwjEZOTUhnb3F54gmKoJaKeDx7P7z5sbacrlGyf0kLKClnCMvaeAfC6rdfumYeRfK3MPuyODMWz_cLMWoA6BUuf8ITxvyf0zCpI6ajXMCd4SPjeLaMtGeerEhj8rNKETWyw0HMs8WqJQMehBLN58UtZ36FpPFyxYNOBhopjX9Emn9H3qi9W727sZrz8oHKdA-13FbM_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
صفحه فارسی وزارت خارجه اسرائیل:
هفته خوبی از اسرائیل برای شما آرزومندیم!
💦
اسرائیل داغ‌تر از همیشه به نظر می‌رسد... و ما فقط در مورد آب و هوا صحبت نمی‌کنیم
😉
🇮🇱
☀️
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69420" target="_blank">📅 16:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69419">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6e5661f181.mp4?token=T35FOnx2OnAffEzBK7342Ou2tcnWHOYFja5GbPOEsMnBClu9jFwr_-AGGXcpcSHUdM2Q09T2GB3Facte2MKslXwYAGSXFvCKDQbz7lisn1CYejtA_sHVd1f5H5kGM_TIDNbSPcI7XFYoEtaeD0E7DL41VOynr6alwuQAt7nD8GOkKb-kEE-eEdhu8LHiJMtWxZamK2wnXmPxtPisXYKCPuMImty2q9WYvaG5JUI5KMNbzakQ4yOtwCVwkYcSDQgm4_fW_cGruOQ-8RZQVM30pe1lD5HQioByzdjt12SduizOJignnn1x1043CTbaibmEt6p0GAz7CUOIwk8hFbThzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6e5661f181.mp4?token=T35FOnx2OnAffEzBK7342Ou2tcnWHOYFja5GbPOEsMnBClu9jFwr_-AGGXcpcSHUdM2Q09T2GB3Facte2MKslXwYAGSXFvCKDQbz7lisn1CYejtA_sHVd1f5H5kGM_TIDNbSPcI7XFYoEtaeD0E7DL41VOynr6alwuQAt7nD8GOkKb-kEE-eEdhu8LHiJMtWxZamK2wnXmPxtPisXYKCPuMImty2q9WYvaG5JUI5KMNbzakQ4yOtwCVwkYcSDQgm4_fW_cGruOQ-8RZQVM30pe1lD5HQioByzdjt12SduizOJignnn1x1043CTbaibmEt6p0GAz7CUOIwk8hFbThzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از نیروهای سرکوبگر: تا تهش پای حکومت وایسادیم، بازم بیاین بیرون بهتون رحم نمی کنیم!
چون داریم دستور خدا رو انجام میدیم، شما اصلا کسی نیستین جلوی جمهوری اسلامی وایسین.
کل دنیا هم جمع بشن نمیتونن کاری کنن، پاینده جمهوری اسلامی!
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69419" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69418">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f215b551.mp4?token=asNV-7bzwpz_GkDGhe_baAUfBrAyhxZLeU3Ds0BV_F7CufO-5EIJT8FqhBUeMIWRF81yRp_4qyYjNJuERj6CHU52X5q5crE1jd-J80dOVuVhUSNpCQ608ln-KeiGLHypzqnuVGpx2j7V-Ev3HBWjwlCzx-6TH9XMXuNysTTuTME4C0G3_TFhkBZVgK4zs_g8faR3CzTEANSdoqJnm8XDpfSCnseazFkK_wrJoGMD4tOSzsodLCaKtesCLc3cI049aREO1DWTMpYlQvYZRtIjXz14J-pUHYg3fGTyAelu_ZcB17E-Q1zhgfFAj9ooctxrk2VryN-a7XS3y72ZHQLbUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f215b551.mp4?token=asNV-7bzwpz_GkDGhe_baAUfBrAyhxZLeU3Ds0BV_F7CufO-5EIJT8FqhBUeMIWRF81yRp_4qyYjNJuERj6CHU52X5q5crE1jd-J80dOVuVhUSNpCQ608ln-KeiGLHypzqnuVGpx2j7V-Ev3HBWjwlCzx-6TH9XMXuNysTTuTME4C0G3_TFhkBZVgK4zs_g8faR3CzTEANSdoqJnm8XDpfSCnseazFkK_wrJoGMD4tOSzsodLCaKtesCLc3cI049aREO1DWTMpYlQvYZRtIjXz14J-pUHYg3fGTyAelu_ZcB17E-Q1zhgfFAj9ooctxrk2VryN-a7XS3y72ZHQLbUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدئو با اختلاف زیاد عجیب‌ترین و دارک ترین چیزیه که تا آخر هفته می‌تونید ببینید؛
هربار یکی از این خانواده رو دنبال کنید تا متوجه عمقِ نفهمیدن بشید...
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69418" target="_blank">📅 15:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69417">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90d8743494.mp4?token=qBRPtY_1Q5n35LqjkEL8uD05KEuvWfFvOEcsQWleTEnbdtqiBPMwbQq2yPiLlLBzFBG97GXyN8ISpd1QVCDtpWxJ0Iwkau4-SsbAaEhbFRmdih1F_a7-pMCM3xR7ku9UPzW9l-FmgL04iQaeg4KXfR37UaiDEybL1nsac1i_EDovI8nEpEbvMU-ywZnhv41HQKFJPqcHu_q70VP-P_9lqh3CqfD8ez02zMeQZXbPehX40FTrpeHATpWGdCGS17Icv0UtiyrgQlyvP2gv4Gk0aF2Jdv2SNZtqndZ2G-r0GBPXt_ROb8EU0Ex_2KEoacH2QETZ8F3E4ruYtv7YuoDKZw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90d8743494.mp4?token=qBRPtY_1Q5n35LqjkEL8uD05KEuvWfFvOEcsQWleTEnbdtqiBPMwbQq2yPiLlLBzFBG97GXyN8ISpd1QVCDtpWxJ0Iwkau4-SsbAaEhbFRmdih1F_a7-pMCM3xR7ku9UPzW9l-FmgL04iQaeg4KXfR37UaiDEybL1nsac1i_EDovI8nEpEbvMU-ywZnhv41HQKFJPqcHu_q70VP-P_9lqh3CqfD8ez02zMeQZXbPehX40FTrpeHATpWGdCGS17Icv0UtiyrgQlyvP2gv4Gk0aF2Jdv2SNZtqndZ2G-r0GBPXt_ROb8EU0Ex_2KEoacH2QETZ8F3E4ruYtv7YuoDKZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بر اساس تصاویر ماهواره‌ای، پایگاه هوایی شیخ عیسی در بحرین که مورد استفاده نیروهای آمریکایی است، اخیراً تخلیه شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69417" target="_blank">📅 15:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69416">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba4d1f7356.mp4?token=AqAI04t9Ph3wbB7Js9XpW86XRwhXNbqkmlb3y0iAJV9RQolNM5g__XLmRfLVK-hnxmpDbNx_5CFZWhIN9-ZWLyfXSEGIxNkf5PkmHaNMdahgjNu1-KOovfh73iO22FIRd9Cgd3IM5_1MhWiDdwQ2FPrTnZUS1D9kX46jnr9l9ZnG-r3R-qa7tTX67NaiSBmbl075d7SDFN7otv49W0T7fQ_sS3Ruqy8c568Hl_iEiLxohd0Pq-w9LXKo-Ra8LH2kvPOuBRvmc5tBmK7BKw94ly13RWMdn8f5D7fSNrqHtWLR61ppOQm3QgpNCRlSdw9Y9ylYvIGLCV7LzYAHqL4GVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba4d1f7356.mp4?token=AqAI04t9Ph3wbB7Js9XpW86XRwhXNbqkmlb3y0iAJV9RQolNM5g__XLmRfLVK-hnxmpDbNx_5CFZWhIN9-ZWLyfXSEGIxNkf5PkmHaNMdahgjNu1-KOovfh73iO22FIRd9Cgd3IM5_1MhWiDdwQ2FPrTnZUS1D9kX46jnr9l9ZnG-r3R-qa7tTX67NaiSBmbl075d7SDFN7otv49W0T7fQ_sS3Ruqy8c568Hl_iEiLxohd0Pq-w9LXKo-Ra8LH2kvPOuBRvmc5tBmK7BKw94ly13RWMdn8f5D7fSNrqHtWLR61ppOQm3QgpNCRlSdw9Y9ylYvIGLCV7LzYAHqL4GVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر مارو خندوندی حاج اقا دارم پاره میشم
👅
👅
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69416" target="_blank">📅 14:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69415">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🇮🇱
بنسالل اسموتریچ، وزیر دارایی اسرائیل:
رژیم ایران در جریان جنگ سقوط نخواهد کرد.
مردم ایران در شرایطی که هواپیماهای اسرائیلی و آمریکایی بر فراز آسمانشان در پرواز بودند، به خیابان‌ها نمی‌آمدند؛ چرا که نمی‌خواستند در نظر دیگران، همدست دشمن به نظر برسند.
تأکید اصلی باید بر این موارد باشد: اقتصاد، اقتصاد، اقتصاد و باز هم اقتصاد. این همان عاملی است که در نهایت موجب سقوط رژیم خواهد شد.
به گمان من، رژیم ممکن است به نقطه‌ای برسد که شهروندان عادی احساس کنند دیگر چیزی برای از دست دادن ندارند.
وقتی چنین وضعیتی پیش بیاید، ترس دیگر مانعی نخواهد بود؛ آنگاه مردم به خیابان‌ها می‌آیند، قیام می‌کنند و رژیم را سرنگون می‌سازند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69415" target="_blank">📅 13:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69414">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
خبرگزاری فارس، وابسته به سپاه:
گزارش‌های حاکی از موافقت ایران با بازگشایی تنگه هرمز نادرست است و هیچ تغییری در سیاست تهران ایجاد نشده.
منابع نظامی گفته‌اند این آبراه راهبردی همچنان بسته است و عبور از آن نیازمند مجوز صریح و هماهنگی با نیروی دریایی سپاه پاسداران است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69414" target="_blank">📅 12:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69413">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835653bd72.mp4?token=uhwLVPTh2F1G1MGUbl2smQe8jFzolyOjCpHIrmNJV6A09VQAmDty2jb66OipUnToziD0Ui64_xkZALnJQid_b8RLfozaD40R_33M72AFY8BC_LEgo0O7LaGuU95LipXZX16CEkhfz1c7ql5qDehADR9XnlCr_lO30TpJlgeYjD1rDwJ3vs2gPdvnTJR-hFvSO-mhEFRnHtM4-ChecPI1Jv3fOc7QRYaQWt8NBCF85f8R6La8AG2T_mLFXKhUI821HQEFr49semzoPhSuNdVW48ZLJfTviYcSl6ItNtKAwGrZ9R4esTRA-eamoRG09_9oJZGqEUg5MLvubUzi2b-KaCBxTGJiarjylQUDfK16zO9RjyMwS2n2VgsSj4J5YylVOMz972pdBxnI2jRWJABafiqg6JR_oGQF-RaUaiyxwjp3qaw4_tVwfBxapUEntF_MdpUFc7upQZzQWHcDzJeMW4PqajxLn1qzTSwR3bkt-qgqGLluT6zQVrYRW5KZ_IPfYTP7WFONdPUYi5qF0xOoMjDE27a10UCi47uoz4iEgY1u5Ez_eOqdADsKwr_Lbgpw2t1keoZXomBhtUi0TFM5wv-dYlX7ATeUzmRA_AQQ1Mi-ti09hkhv2Rpe-aEEyvCAZ-dZSNNtkXvzt9N4XgI_JhMsVsfv5wamAClVRYSwQ7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835653bd72.mp4?token=uhwLVPTh2F1G1MGUbl2smQe8jFzolyOjCpHIrmNJV6A09VQAmDty2jb66OipUnToziD0Ui64_xkZALnJQid_b8RLfozaD40R_33M72AFY8BC_LEgo0O7LaGuU95LipXZX16CEkhfz1c7ql5qDehADR9XnlCr_lO30TpJlgeYjD1rDwJ3vs2gPdvnTJR-hFvSO-mhEFRnHtM4-ChecPI1Jv3fOc7QRYaQWt8NBCF85f8R6La8AG2T_mLFXKhUI821HQEFr49semzoPhSuNdVW48ZLJfTviYcSl6ItNtKAwGrZ9R4esTRA-eamoRG09_9oJZGqEUg5MLvubUzi2b-KaCBxTGJiarjylQUDfK16zO9RjyMwS2n2VgsSj4J5YylVOMz972pdBxnI2jRWJABafiqg6JR_oGQF-RaUaiyxwjp3qaw4_tVwfBxapUEntF_MdpUFc7upQZzQWHcDzJeMW4PqajxLn1qzTSwR3bkt-qgqGLluT6zQVrYRW5KZ_IPfYTP7WFONdPUYi5qF0xOoMjDE27a10UCi47uoz4iEgY1u5Ez_eOqdADsKwr_Lbgpw2t1keoZXomBhtUi0TFM5wv-dYlX7ATeUzmRA_AQQ1Mi-ti09hkhv2Rpe-aEEyvCAZ-dZSNNtkXvzt9N4XgI_JhMsVsfv5wamAClVRYSwQ7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گزارش روزنامه همشهری از دلایل عدم انتشار صدای مجتبی خامنه‌ای :
از طریق صدا میتونن پیدا بکنن چون هر فضای بسته امضای صوتی منحصر به فردی داره و از بازتاب صدا از طریق فرش و دیوار میتونن مکان رو تشخیص بدن و ارتفاع اتاق و فاصله گوینده رو از محل بازتاب رو پیدا بکنن
همچنین از طریق تحلیل شبکه برق میتونن ردیابی بکنن چون همهمه ضعیف الکترومغناطیسی در پس زمینه صدا ضبط میشه و سرویس های اطلاعاتی میتونن از طریق شبکه های اتصال برقی مکان رو ردیابی بکنن
هر میکروفون و دستگاه ضبط اثر متفاوت داره و مختص خود دستگاهه مثل اثر انگشت خود شخص لذا از طریق ردیابی دستگاه میتونن مکان رو پیدا بکنن
صدای پس زمینه مثل خنک کننده ها یا ژنراتور ها و حتی توی مکان باز صدای ترافیک ها و صدای محیط و نوع حشرات و پرندگان میتونن محل جغرافیایی رو لو بدن
😳
😳
ویس ابعاد فیزیکی نای دهان و مجرای صوتی رو نشون میده و حتی فیلتر هم باشه با دستگاه هایی میشه ردیابی کرد و تشخیص داد طرف زنده باشه محل حضورش کجاست
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/69413" target="_blank">📅 12:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69412">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🇺🇸
ویدیو ای که صفحه رسمی وزارت جنگ آمریکا به تازگی منتشر کرده
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69412" target="_blank">📅 11:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69411">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb1d460275.mp4?token=jds5m1SSq0VpzopoTXu9cAMYxahS5BtQFtHuD6f1otMQHuFRq3VxEggcH5ezKBwvIy7mAKZertbaK1ofTtW7K6OXosKixDqBQpP_YoW7yiVLFCsGnystQyow2UnADd_ty_d6xTDse5owgeRLm5FjBbNapMpEEd4LABHyLWccSi-k-COQAva-CWFrfhZuRzNFLGOZqP2lxjw4QTVl6qISzNWVq9TC_nuYnmfaySxZNb4q1rHUsAm-gPVwPT9H4DdgDpYTRzyVRDGug8hOReKEFyTdqgqfEK7QA1ylawjvQg8P7KOZN1OKkkTYWOLzywfe15woTtFokDemruH7SFySuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb1d460275.mp4?token=jds5m1SSq0VpzopoTXu9cAMYxahS5BtQFtHuD6f1otMQHuFRq3VxEggcH5ezKBwvIy7mAKZertbaK1ofTtW7K6OXosKixDqBQpP_YoW7yiVLFCsGnystQyow2UnADd_ty_d6xTDse5owgeRLm5FjBbNapMpEEd4LABHyLWccSi-k-COQAva-CWFrfhZuRzNFLGOZqP2lxjw4QTVl6qISzNWVq9TC_nuYnmfaySxZNb4q1rHUsAm-gPVwPT9H4DdgDpYTRzyVRDGug8hOReKEFyTdqgqfEK7QA1ylawjvQg8P7KOZN1OKkkTYWOLzywfe15woTtFokDemruH7SFySuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
واکنش پزشکیان به تاخیر ۱۰ روزه در  پرداخت حقوق اعضای هیئت علمی دانشگاه‌ها:
این واقعاً قابل قبول نیست، کاری کنید که اساتید بیش از این ناراضی نشوند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69411" target="_blank">📅 11:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69410">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇮🇱
کانال۱۲ اسرائیل:
عراقچی، وزیر امور خارجه ایران، شبانه با یک مصالحه میان قطر و آمریکا برای بازگشایی تنگه هرمز موافقت کرد؛ اقدامی که باعث شد دونالد ترامپ، رئیس‌جمهور آمریکا، حملات تلافی‌جویانه برنامه‌ریزی‌شده را لغو کند.
بر اساس این طرح، کشتی‌های عازم خلیج فارس از طریق آب‌های سرزمینی ایران وارد و از مسیر آب‌های عمان خارج خواهند شد؛ هرچند عمان خواستار تأیید رسمی این موضوع شده است که سپاه پاسداران از این توافق حمایت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69410" target="_blank">📅 11:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69409">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66dc919056.mp4?token=k6vo9uwl_DYoN7CYny6MrNUyXXpemOCDXTgakwL22VM9d7QKe0qfvkDYSJDY1_g6g06RDeq6wOw1ad82yCoLVoKHBl7QOJb89zqJYYVIE8WH5ZIQm6e1r01BsFKHOQcjyZ1G4KgfGhLPhyeuxnAVq7eJ-sp6MPyQJbPwtsiqYb_6719NOW8WUavKwgSnxQpqrCUmmzY8oqVQBYtJeuDnZv54NFo4OXtUzxfKOQpigvGWiKCyVnwTiOOdiokBOG-3VYVrZiCsPaO6i8ZtOMLFX-U8KV-aCjJQV35RW2X1M28Hu125g1LJf7lk9m8vTDWUChsca0IOnbi3XwbSOuDqTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66dc919056.mp4?token=k6vo9uwl_DYoN7CYny6MrNUyXXpemOCDXTgakwL22VM9d7QKe0qfvkDYSJDY1_g6g06RDeq6wOw1ad82yCoLVoKHBl7QOJb89zqJYYVIE8WH5ZIQm6e1r01BsFKHOQcjyZ1G4KgfGhLPhyeuxnAVq7eJ-sp6MPyQJbPwtsiqYb_6719NOW8WUavKwgSnxQpqrCUmmzY8oqVQBYtJeuDnZv54NFo4OXtUzxfKOQpigvGWiKCyVnwTiOOdiokBOG-3VYVrZiCsPaO6i8ZtOMLFX-U8KV-aCjJQV35RW2X1M28Hu125g1LJf7lk9m8vTDWUChsca0IOnbi3XwbSOuDqTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
با این حال، تغییر رژیم هرگز هدف اصلی نبوده است؛ هدف، خلع سلاح هسته‌ای بوده است. آیا می‌توان یکی را بدون دیگری داشت؟
🇺🇸
مارکو روبیو:
هرکاری که توی خاورمیانه و جهان انجام دادیم کسی مانع ما نشده و موفقیت بدست آوردیم
رژیم باید تغییر بکنه شما شاید تغییر رژیم نداشته باشید ولی باید اینا تغییر بکنه
اونا میخان
انقلابشون رو به کل دنیا صادر بکنن و باید این تغییر پیدا بکنه
ایران تابحال با رئیس جمهوری مثل ترامپ که مرد عمل هست رو به رو نشده
اونا هنوزم موشک و پهپاد دارن میتونن صدمه بزنن ولی خب سپری ندارن پشتش قایم بشن
از روی قدرت باهاشون مذاکره میکنیم نه ضعف
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69409" target="_blank">📅 10:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69408">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb72a3070d.mp4?token=OsBoJSaB0X8hJdcjin7koBrW8mEt0w6pe9Ljj-DVsxjrpptKg17pAwcpGmCeNEQR0ncSn1NYGKTn6Y4pWRNuetxd7VBzU8FS5UbLRJXfg_JffHJy78f0Ib8YZhRXQYLS0u8u6qxODGjbPRB0qdjtRKsG154WChZ651N2M1cXWI7wmFuSHUcl5FWhFOGyjMEbGGOlDhGtQ4v-ywGojEsuaqWp3tHJwOX3pIEG6zkIKwj6S84gj8Ugs2X_2K2DSEQJxWnT_tuZG0aVWpqGU-LmDdYB8VBXsn8VTaTvbFk4Or4p2ayJ4O87JYo3-tJh6zdc5k48JMg1gx9cSO0hjLXq2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb72a3070d.mp4?token=OsBoJSaB0X8hJdcjin7koBrW8mEt0w6pe9Ljj-DVsxjrpptKg17pAwcpGmCeNEQR0ncSn1NYGKTn6Y4pWRNuetxd7VBzU8FS5UbLRJXfg_JffHJy78f0Ib8YZhRXQYLS0u8u6qxODGjbPRB0qdjtRKsG154WChZ651N2M1cXWI7wmFuSHUcl5FWhFOGyjMEbGGOlDhGtQ4v-ywGojEsuaqWp3tHJwOX3pIEG6zkIKwj6S84gj8Ugs2X_2K2DSEQJxWnT_tuZG0aVWpqGU-LmDdYB8VBXsn8VTaTvbFk4Or4p2ayJ4O87JYo3-tJh6zdc5k48JMg1gx9cSO0hjLXq2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مرادویسی، تحلیلگر ارشد اینترنشنال:هدف‌های احتمالی آمریکا تو جنگ جدید میتونه شامل این موارد بشه:
1. مراکز نظامی سپاه تو جنوب کشور
2. شهرهای موشکی و پهپادی تو عمق خاک ایران
3. تاسیسات هسته‌ای "کوه کلنگ"
4. مراکز نظامی سراسر کشور
5. سامانه‌های پدافندی و راداری
6. پایگاه‌های هوایی ارتش
7. مراکز و نهادهای حکومتی
8. ساختارهای سرکوب (سپاه، بسیج و نیروی انتظامی)
9. مقامات و فرماندهان ارشد باقی‌مونده
10. مکان‌های نمادین مثل صداوسیما
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/69408" target="_blank">📅 09:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69407">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cbd0e326f.mp4?token=tLwWAI5Me67ZZ8wSau347oO0WQik4kjYlCl2tlakLLA_EV5Fzg3oyGWS-3nMjLlid6QgMEZbFC49UpaWfKDZPVepE6HrH721WXlMG7gblbjMt_TFUBLPBKzGEGV92NNKDar-hgQDrkganeHNsiAPwk_v7xSvvuFhW1nAXFLt32WgDpppv0H7S_VxdgWgKhGkHwSfXlriUAFpZQKEreByQsmJ9wzd4eEk75qC8859lJ_tAhjA8wTcL5bnIryDuXwPKcGvwPOrIBEvrgLT9hpR65lY-EagSdfcPZFNvrNWoIqDJN1VsQQSNktkwDlz_QpUQJD_wEYHLODRCW36UY6ANg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cbd0e326f.mp4?token=tLwWAI5Me67ZZ8wSau347oO0WQik4kjYlCl2tlakLLA_EV5Fzg3oyGWS-3nMjLlid6QgMEZbFC49UpaWfKDZPVepE6HrH721WXlMG7gblbjMt_TFUBLPBKzGEGV92NNKDar-hgQDrkganeHNsiAPwk_v7xSvvuFhW1nAXFLt32WgDpppv0H7S_VxdgWgKhGkHwSfXlriUAFpZQKEreByQsmJ9wzd4eEk75qC8859lJ_tAhjA8wTcL5bnIryDuXwPKcGvwPOrIBEvrgLT9hpR65lY-EagSdfcPZFNvrNWoIqDJN1VsQQSNktkwDlz_QpUQJD_wEYHLODRCW36UY6ANg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
حاکم بحرین:
حضرت محمد (ص) پس از قرن ها تاریکی در ایران به آن عمق روحی، انسانی و معرفتی بخشید، بخاطر تشکر از این کار حداقل دیگه به بحرین حمله نکنید.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/69407" target="_blank">📅 09:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69406">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZ7Gm0gciRyrq5tBaqAaXfyaxTCNHPhyeQb2Yp6NU9ZtUzVPh0ZY6HxLN_6W9QkyO5EvOl9kOpUBE2XgknBMJ4y3dAMxluIctM_V1whBdDYuR93H-A_8Uvef_2UG9H98BbEvW_uUOyhY6fHWruKJ2CzAxbzCz4N7B0x5KCwrURbpxtnzhZt-fuqBFEOSekOBVxYC1SRRGvUIZl3X4weCaJB-X6mwcc_G9UFMrq1Hhr9DrHyvb8RevK410LwnMb7lfhLHFAs6M6NSgqXnXI_stlbyA5XsfyXdNNXv10xFkhln0pWHdPTznF1GrsUdQchKIL2o6Bac4XX4VD9in8JbPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: حمله رو کنسل کردم
!
ایالات متحده آمریکا آماده و مجهز به سلاح است تا علیه جمهوری اسلامی ایران، در سطوحی از ترور نظامی، قدرت و صلابت که از زمان جنگ جهانی دوم دیده نشده است، اقدام کند. با وجود این، ایران و سایر کشورهای خاورمیانه از ما خواسته‌اند که هرگونه حمله‌ای را در چارچوب توافق‌نامه‌ای که مورد توافق قرار گرفته است، متوقف کنیم. این شامل بازگشایی فوری، کامل و تمام‌عیار تنگه هرمز و پایان دادن به تهدید هسته‌ای ایران می‌شود. بر اساس این درخواست، من برای منافع آینده جهان و همچنین بقای یک ایران موفق و مرفه، موافقت کرده‌ام که حمله را لغو کنم، مشروط بر اینکه بتوانم به سرعت به توافق‌نامه‌ای دست یابم. کشور اسرائیل در این تعهد به من می‌پیوندد. همه دست به کار شوید و آن را انجام دهید. از توجه شما به این موضوع متشکرم! رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/news_hut/69406" target="_blank">📅 06:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69405">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpFwcbOlb9BrjAnYl1TGbjd2n-rMEPtIreMr3OtD6jcr6VwYv9hjL_SqRXItiGri3NVX6YsgIYZlbAwB3HeuDfugFzSABVTbxmMyMicmf5s3pmqsDLwnQ0N5lLmgsMJTyhpLBTtcTwEnkJ0g4VCYk9b4VmZRmW7GzDaVydunbJvpTzH0i5X7DmSqibHvOYCsc12ho2gbSCFxWOgt2hXep4CBT8GXH-r0UaWdfhDsT4D7_rhoKDozb9C4Orcjj8kILjnGelo_Xmjhexi-P-JD2ftFeef4rDm61p881YS2W7x6GjramxUYGRxInrI11GGPDDx3W0cYeyVpTClfncRIQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیکه و ترامپ چیزی نگفته.
#hjAly‌</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/69405" target="_blank">📅 02:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69404">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6db9d071b.mp4?token=Ts7IyxsUWvG2Zd7jUykyJrfIS8FvlhIGhFXvdcf26n6hfOdcPTzdsnZCsIxScmBlZ6T37QtTIOD1qVfNp9dkTL_JjryOs1TOOfa3p1wOP8XeT4Zou7JdzdYmDQhXDCKTPDUQoO3u1p-U5in4i9ENg_tnJa--f-WpWYYdAxIVv53k2RQk_oEGRWDftUBswHWFWMunhh6MQXEgSoHVu80jECJAiIJEQV_ku24TRMc_KpnTKlLqAbk8tzENFflTxxwKWEYyy8y9TGet7DRec-c1Q0CKJgnYC5bVS_qvePNFQWHKhsHSJRzvvu3n5Pt4M_kxY9O34R38n62bNYmc4r1AvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6db9d071b.mp4?token=Ts7IyxsUWvG2Zd7jUykyJrfIS8FvlhIGhFXvdcf26n6hfOdcPTzdsnZCsIxScmBlZ6T37QtTIOD1qVfNp9dkTL_JjryOs1TOOfa3p1wOP8XeT4Zou7JdzdYmDQhXDCKTPDUQoO3u1p-U5in4i9ENg_tnJa--f-WpWYYdAxIVv53k2RQk_oEGRWDftUBswHWFWMunhh6MQXEgSoHVu80jECJAiIJEQV_ku24TRMc_KpnTKlLqAbk8tzENFflTxxwKWEYyy8y9TGet7DRec-c1Q0CKJgnYC5bVS_qvePNFQWHKhsHSJRzvvu3n5Pt4M_kxY9O34R38n62bNYmc4r1AvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان سلیمانیه
@News_Hut</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/69404" target="_blank">📅 02:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69403">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5cdd81f13.mp4?token=cJeGyQisL8VMmreks2U0GgdZTBao3LFUpmcn-0Mjeg-JswmkFdx8ABdsomxTjjCn4GzJu07HrjH0qy9w029F9biGuTb_05Uv19JkV_IiO52jnfeF9PpDg75NmOwULtDpvB-QMcG9VhwZm2wyzjaUYCivSWyrvYFaa7_zZjodN7ERLvZgfsUPkhBBNu7nmqb5ktGlXFpCTttXTTgxX7I6yp5ef3dzblAgqEt8vlJ_IC-roLr99mxVsxws47r1nA8A4esAjWZNMHvyGqHCwgoMuCXR-TQdEPVFLGtGhEgi0MTI752JC0OnG3hdfQ-qjWmGeQlzddvcufFGkKt2AKEgjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5cdd81f13.mp4?token=cJeGyQisL8VMmreks2U0GgdZTBao3LFUpmcn-0Mjeg-JswmkFdx8ABdsomxTjjCn4GzJu07HrjH0qy9w029F9biGuTb_05Uv19JkV_IiO52jnfeF9PpDg75NmOwULtDpvB-QMcG9VhwZm2wyzjaUYCivSWyrvYFaa7_zZjodN7ERLvZgfsUPkhBBNu7nmqb5ktGlXFpCTttXTTgxX7I6yp5ef3dzblAgqEt8vlJ_IC-roLr99mxVsxws47r1nA8A4esAjWZNMHvyGqHCwgoMuCXR-TQdEPVFLGtGhEgi0MTI752JC0OnG3hdfQ-qjWmGeQlzddvcufFGkKt2AKEgjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
حملات سپاه به‌ سلیمانیه عراق
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/69403" target="_blank">📅 02:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69399">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aPA-bLwRrla-wRvEfHWzf1TqjR_TXfRkA-SaNYmOgZg-4olf-YQ3e1loVdvfuw2NHLlZA0C_x_O0baWB8Pvtlb4vzmkiH1S9JeE8HDEoj8VWrKAFUHBvidkvC982CN0-rC_ekrLjJH2x3enO5Jnhj1ByHH3B_l7E1Yy-SckUgirA-YtxkmHMccc0cOX-MdpIacyr9KUzlv0PAysPx9tRvxDMEHkYzjOKrgfgPI49TdMXDVMofZktfpjaycJ7rxMBwTMCW0kH3tx7aw-mym8y-admvfeDsed2QtTV721j1epknR8JO6rj8bFtRpOz8euvRB3myT3JLA-cmLsW_zoYpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uTTQnZ46eC7MelxRF-BmcXMLrchHEVH2mVUkH5etwm2WJIGkH225LWDGSQt69N6GBdaRutcKCsnocL1L2lqSSKMCvGMdQtxo9vXPLDQCpqyzawzodGrSC-I9AoniahnllHfjlyf2fSq8IXoK-kBp83P39IPknH7LprKrV5nQJEEFS278v61wE2MHSXTW6HpzFpRfRW8k86Iwq04GQxPxYG1DyoE4S9XEuSka5Vjo9yro4jn600irD4VyBLZp5tS_7eqMCxYoVuHqwOq1zzlqgFAXu4sWoVhzZMqdHlMqAncRQO3GHTOQEWT7eVJEpnYiFP2g_dtiCdH3Df1deDodVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ea496ad43.mp4?token=qIRKtJQMLdnQrouo4g5tNF1UGeBgqz75SMqNCmficGYn5jXMlH132ALbCcN2yVfcWN8NIxVJVXkU5xKsHtb-a_23v_8xHldgMzUCDBaTmwPlBUWz9MREdFnbfb302BJLxLVAELsJ3y0H6Rf55JxPm7zqrl_XcDXEGLamdvaM-vrw4NtNHT2kpch9JdKtwT_gzS-PxhG1pRBsWio9Z06Gf17EjiJHQK9Uz96clwQn5GrMv9F7NQV8-MN-MhXhQxm2LnJzw0G27UJymADTNCr0dUBkMo8gUS94rIGMQqRNIW4P4tUTPWz6XzEZ9FMiCr0UavI3ZDe4lM0SYWgVqFTJIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ea496ad43.mp4?token=qIRKtJQMLdnQrouo4g5tNF1UGeBgqz75SMqNCmficGYn5jXMlH132ALbCcN2yVfcWN8NIxVJVXkU5xKsHtb-a_23v_8xHldgMzUCDBaTmwPlBUWz9MREdFnbfb302BJLxLVAELsJ3y0H6Rf55JxPm7zqrl_XcDXEGLamdvaM-vrw4NtNHT2kpch9JdKtwT_gzS-PxhG1pRBsWio9Z06Gf17EjiJHQK9Uz96clwQn5GrMv9F7NQV8-MN-MhXhQxm2LnJzw0G27UJymADTNCr0dUBkMo8gUS94rIGMQqRNIW4P4tUTPWz6XzEZ9FMiCr0UavI3ZDe4lM0SYWgVqFTJIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇷🇺
ساعاتی پیش یه انفجار تو یه رستوران تو مرکز مسکو رخ داد؛
جایی که به گفته منابع روسی، مراسم عروسی خصوصی با حضور چند نفر از فرماندهان ارشد نظامی در حال برگزاری بود.
کانال‌های تلگرامی روسیه می‌گن "الکساندر چایکو"، فرمانده نیروی هوافضای روسیه هم بین مهمون‌ها بوده.
گزارش‌های اولیه حاکی از کشته شدن دست‌کم 3 نفر و زخمی شدن بیش از 20 نفره!
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/69399" target="_blank">📅 01:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69398">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⏺
المیادین:
بر اساس اطلاعات بدست آمده، گروه‌های کرد حاضر در خاک عراق در حال آمادگی و برنامه‌ریزی برای اجرای عملیات علیه جمهوری اسلامی ایران هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/69398" target="_blank">📅 01:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69397">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پمپ بنزین‌های مملکت بخاطر حملات احتمالی، دوباره شلوغ شدن.  @News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/69397" target="_blank">📅 01:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69396">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff498baa1d.mp4?token=fs7BiMuQmUzUhFaGCHQCHjte-mrPxySgax8AItUzAWF5nXazRa_lk8ulFGUnJUhMYPZLuIYojjOLWUtj3uFSbdwABy9kM0_IxPkF_gBgOlKVv5DGTLDtlYODlrHOast1e_tVuy3hdXWMd_CBXC_vytujH9emAnGS0ptPq2IvLD3qEkfz2sPbW21A3gUmhBsl-q4lQu4ec7tYdyTk1iFpOoi260O2zoifAswV2EVO8Fh7pGIw8yC7vJM0plDXmJeLnhxhLwN40dBrTUOAXokv8nnNIfEyeeabzNnMBuDweNrQJYBUmAliJo0RU1MA1Rlr1tI36dwb0ouH6PawJrMwEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff498baa1d.mp4?token=fs7BiMuQmUzUhFaGCHQCHjte-mrPxySgax8AItUzAWF5nXazRa_lk8ulFGUnJUhMYPZLuIYojjOLWUtj3uFSbdwABy9kM0_IxPkF_gBgOlKVv5DGTLDtlYODlrHOast1e_tVuy3hdXWMd_CBXC_vytujH9emAnGS0ptPq2IvLD3qEkfz2sPbW21A3gUmhBsl-q4lQu4ec7tYdyTk1iFpOoi260O2zoifAswV2EVO8Fh7pGIw8yC7vJM0plDXmJeLnhxhLwN40dBrTUOAXokv8nnNIfEyeeabzNnMBuDweNrQJYBUmAliJo0RU1MA1Rlr1tI36dwb0ouH6PawJrMwEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پمپ بنزین‌های مملکت بخاطر حملات احتمالی، دوباره شلوغ شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/69396" target="_blank">📅 01:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69395">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rixjk4geznYuStWCMt2HC8SyXCOQIxFDTmhgT1_YLo8N8ynda21c33lp7MXs-ptxfdaoZ1J1dico1NJ7DUU4oKZN5XOK_66bDFqk3C5UHXYPJHITQEqPzqvNh6Ng4a_VP-2Lkr79G0DBdP1M_kelFVgXrxG2ka8QHHgeYGfMxcXOsRV9pIsRL4XynSeuBcfaJ3QkbtJKHF-CLxPBKmF135RtGo3k-R6xTzfpgCuKFJFxdd6nwo5STl8aBZx9dCj1GnTRQLfOoSKRgI_9ENMvHcBuuda8GL2wWh7Je6IPIFopNGIBQFRDSifG6b7mSsKFLl2Rv0wddePFuxI33en-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
توییت اتاق جنگ اسرائیل و اون ساعت شنی معروفش
@News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/69395" target="_blank">📅 00:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69394">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b418c0b947.mp4?token=iNPDf_CGHyDwrbxxGFQaiUfcHHbq8z6lfkaum8VlqR7aPzMMd7lfZVeZ9jGpVGjrmmgOzzM-tqmCfhZUCWC4NrVtbcrh-JAxXIgm8gLyBL5QD4OWRy1wcEwELk-UySoSt5vuPqNpHc2xSqs7FuTdjBjs1ygI_0ht7mg-_SvJTwATW6pSGaMKRQAzGhG7TXdLibazMJazd13SqPralDeKwmYl841o2EZaaQmJooiykYWjC7uHG3ZCpmgPrwOyim599wvadPAp7nS3tubxFOphgZ7K2WQjdcBFixn-ULBZFlomxdwlTQchtpkUlSr1ic4SLXtXF2AHQZFMqkkHgo06eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b418c0b947.mp4?token=iNPDf_CGHyDwrbxxGFQaiUfcHHbq8z6lfkaum8VlqR7aPzMMd7lfZVeZ9jGpVGjrmmgOzzM-tqmCfhZUCWC4NrVtbcrh-JAxXIgm8gLyBL5QD4OWRy1wcEwELk-UySoSt5vuPqNpHc2xSqs7FuTdjBjs1ygI_0ht7mg-_SvJTwATW6pSGaMKRQAzGhG7TXdLibazMJazd13SqPralDeKwmYl841o2EZaaQmJooiykYWjC7uHG3ZCpmgPrwOyim599wvadPAp7nS3tubxFOphgZ7K2WQjdcBFixn-ULBZFlomxdwlTQchtpkUlSr1ic4SLXtXF2AHQZFMqkkHgo06eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمود احمدی‌نژاد درباره دستگاه سرکوب جمهوری اسلامی:
نیروهای امنیتی خود افرادی را به میان معترضان می‌فرستند تا با ایجاد تلفات و آسیب به اماکن عمومی، بهانه‌ای برای سرکوب خونین فراهم کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/news_hut/69394" target="_blank">📅 23:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69392">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tM_yX5ifx5jSbo0kkAvUsPLkfFWK76Ufc6o-4VGO8c1w6IaoCMDsVisG5QwXddFt2UcOFFlqZ4WgYqbkEzltwpNGjTAYLk7UU8N0nvMm7SgmKAOd2IPDNdOcp4anS_9GVJGC1RPyT-gcNFpHiVz7k4n7ZAWR62kA7QihBkrmFMyqF7hBN_TRkm0SUKoEA-GPkbbmcimX1mjCkk0LqiHBOF7OlrMNhqqOAcAqVA0Geys9hWcJ5nKnzjGpkvPjmdY_ljDV2gyH1KwzbpxttwTYdjMW3NQp2EdFSbh_OIkLbAi31snW7SnZgbX5TX8FmhV7EPpSMr0a0D1HyD77JC5Ewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82ccfb8ec6.mp4?token=B48SxZphTo4nHgs2r1dNt2j1Fy9SSE5QqiKGHEEq5pAohSQIfLQ70BqNFMgBJfsdOq424ttZ4znnjGTZb8kfbKzrfN5sIs3upBQ72M4laX_lWlfd_f0fuTT1gsYBrRtyPqJZsT3QROgPRWUatquXj0h9WObMtTUG0RT5TezLDRqmrVHvDy-hf3ct_A0JsCGmR5B0sv1tFolG6e-_MZPHr1_SsApjIPM_sXXVFGLKT3o4GnaVjfHSOdFKd5EMNYbB1DvUQgLBA5W76fO73kG4kh_GmW2gNwwqulHpDOXC6g8pxSuJUAH-uR_-fNzigRJhkGJOIm0BwhBkn6okre15DA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82ccfb8ec6.mp4?token=B48SxZphTo4nHgs2r1dNt2j1Fy9SSE5QqiKGHEEq5pAohSQIfLQ70BqNFMgBJfsdOq424ttZ4znnjGTZb8kfbKzrfN5sIs3upBQ72M4laX_lWlfd_f0fuTT1gsYBrRtyPqJZsT3QROgPRWUatquXj0h9WObMtTUG0RT5TezLDRqmrVHvDy-hf3ct_A0JsCGmR5B0sv1tFolG6e-_MZPHr1_SsApjIPM_sXXVFGLKT3o4GnaVjfHSOdFKd5EMNYbB1DvUQgLBA5W76fO73kG4kh_GmW2gNwwqulHpDOXC6g8pxSuJUAH-uR_-fNzigRJhkGJOIm0BwhBkn6okre15DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زهرا کاظمیان از حامیان جمهوری اسلامی در انگلیس که کارش زیرآب زنی مخالفین رژیم بود، دستگیر شد.
حالا فیلم لحظه بازداشتش رو ببینید که پلیس اومده بازداشتش کنه، میگه تروخدا بذارین زنگ بزنم پلیس
@News_Hut</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/69392" target="_blank">📅 23:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69391">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28c29c1e71.mp4?token=pH95UMjIf4sPBjvqQ-N6HMx33G2p378XC74aYSwoV_w6_KZzch2rGZ8OpNX_BJ_g0sD76Yc2z6uY6Sd9mKT54i3s1M6CNbwlDXN08dzTtTfKgAQSbEHAJtDYMz3p8WySUPh2t2cXIKNPtCNhAQ7EM8sx7lSHvwEvEhS34CDxD506yQKcJkLBkj0JppR2eWiSgjP2f-uLhdHMNcjdwhuqcx5yHmGIcKta973d-cxRBWEtSGE9wLcQcqT842ffhoHMq8sjCp_2iiwrcwXIchGQCQasiDpQf-AnypXHiqxHMsaGf7awKd09coEfcAJsjU6yGFrdJFKxJirbGdGKr8nFHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28c29c1e71.mp4?token=pH95UMjIf4sPBjvqQ-N6HMx33G2p378XC74aYSwoV_w6_KZzch2rGZ8OpNX_BJ_g0sD76Yc2z6uY6Sd9mKT54i3s1M6CNbwlDXN08dzTtTfKgAQSbEHAJtDYMz3p8WySUPh2t2cXIKNPtCNhAQ7EM8sx7lSHvwEvEhS34CDxD506yQKcJkLBkj0JppR2eWiSgjP2f-uLhdHMNcjdwhuqcx5yHmGIcKta973d-cxRBWEtSGE9wLcQcqT842ffhoHMq8sjCp_2iiwrcwXIchGQCQasiDpQf-AnypXHiqxHMsaGf7awKd09coEfcAJsjU6yGFrdJFKxJirbGdGKr8nFHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کانال 13 اسرائیل:ترامپ تصمیم خودشو برای حمله گرفته؛
میانجی‌ها که آدم‌های خیلی خوشبینی‌ان و همیشه میگن راه مذاکره بازه، حتی اونا هم میگن حمله‌ی آمریکا از هر وقت دیگه‌ای نزدیکتره.
آمریکا هم از طریق سفارت خونه‌هاش به مردمش تو خاورمیانه هشدارهایی داده که اینم یه نشونه بزرگه برای حمله مگه اینکه ایران همه رو سوپرایز کنه و برگرده به مذاکره.
@News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/69391" target="_blank">📅 22:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69390">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⏺
🇮🇷
نیروی هوایی جمهوری اسلامی هم از دیروز تا الان مشغول آماده‌سازی خودشه تا در صورت نیاز، بعضی از اهداف تو خاورمیانه رو هدف قرار بده:
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/69390" target="_blank">📅 22:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69389">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLygpD8HRMZiPPw6L-TI_12bYmrY98hFsg1sknObWcnN3V2k1EyGHEKLMNeg6ICT1Lnd511DmKWwJ3yUGWbARO7IHqLgHkWhRl2PgYUpW4QdxhrbBFzukZF8MB3z6LgqoN6LiVg4Ad1GMTx87nAK1t26LZ1lgCsUddKmADTI6sKedMTIqpdar7PInlxr-zwwlvnmRP86k9Xd2s2sSw90jJc8ofTHnot3MY0P16KIM4fughEuSM9QCtclgwY8VyozPza1vnFuKVfGIq3HYNy9w_0bOdiHV-xb_oqKx3p--bCPz45o_I19U7ZLpw7F57TJqc2pc03HUwe3qYPNkaiFOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
ترامپ در حال نابود کردن ارزش پول ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/69389" target="_blank">📅 21:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69388">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sudrqBvUvoceimtBrgo5qtmLt4vayg1QZU3vQokII-JkgU66QK4vkWyCVrmvaZAcXe1LzDzlhldn6eiLk4oHGi-29PRm7dgjBO8yMSB6HE4ZZG1WwfN0jimYTNf7DxEemMj7kL3gFTblZ5oYEiFvflLVf_45cFRbgwdSNKtXxxnY4YSxB5b6cxQgSc5BzHCmfjjmKECQ-l7bXSokIsE_T_plv-MaqV1Wy4k8jdr2ozf3wFqfd5tHZnycS1bmUnIVgekIt_kBk8ZZ41o9kc6Rmn8Q8uvec_GWOGS6O845dvg72Cw5We10zMgIqBWPedyxyet-oFtSpTlroXVVqOS7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/69388" target="_blank">📅 21:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69384">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uON0B0B4GA0QJcs7mqs9-_gTa7heJOcr669lG5_VbjePQeV6vXwo7aitZVaGisXqNnjzdxEhNEt4aDnkq_x_sLohgZGn0A4ylApg4Uj9YX_Kc_JcLXiYpNN8x98Rg70Ob3-7ZQFcxBxlzAVrnWGLH_TSY2cLXFA0ABRLKBd5qQZkPgFVlJSiOBhSh5KzK2LpYhRwsO-QbX9QdIm4-VY98JG5WpqEv-zV5S60z_SGViMsUMZYlcuaOlsIUt254flNWdSLPnKgtqfWz4qzwv1w-6DF1AjDa2OXmrxm4TrBYUzdqsBhU9ucB6ZU3oYTSg3F3x4rw6Q7EpSejLsTDHjaRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qzryk0tJYV27JsJ7yRYOp3zbwX1fNJzSyqreGvqQV_C1xH5vFSteQyJA6bxvMno6nV3ok7U9o5ZPPzZbbw3v6zWyx1j0ViUfk4f--1dehmYJ3ziwWo5BH7FkjoL1kpSXqC-XsExYNzOE7Laj_5IV6BprHCE3SmM55SMVi29_dOrcIUCOLt5e0vFSK-1UZSvSNDaMK7EbVQPA855xVJgtdkvuyubMcsStoMgQdEUzhjkBEomaO3yY2vO_mSC8BRgcIA1eeI_4aBw3CZm58Semf0yN5EE_HeSsfq94-bm6RkdEck7bLl5TfJpNZTnlRv1fRW609FRwDWLCVFFtstEmwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QZX4MhjmzhWfkXJ-snX-GrXUFp1uTRge-f4uBPx0AKsAl5M3yKWf7NV2GX0q3qv66m8VWL6GKdAHgfZK-5SIAQ-P86nYKnEsGvrcv4pHKKAQ5jEg0mhDefLAW1EnmqNXlzlFrujuQbvgza1hgpPmtNItcF63oQueqhB0hzD1zIlZKFC0Doyl5TVAB-TZkfOGlicDeua730icHHujKQkOoDtEIQcez99i3vTh0hqQHAgkPena_d8hGfxLioqXC6K0AsO0zBUt79sZlfCPSt0DJiDiczwlrr9YAMFKjJ6w3Ho-IssiNoNb6jwV4NH_FQE_FqSUqDP5TbGfXjhOnzIOrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m5EbPoDLLPVEs65cQu_nkWmN_2xQcqdfPyDMqQZSYbMHfDligTjcNrR7wD2xsr7NbrB_eMvLb8Y5it2DNFeDXz_ygQ-M3rCUo1kECKr-naotDfFFk3wQ6CR8lrRda9-qzEGu5SGKpZmy8EiWEaJPT-1nDf2JMLScSwPyXg72nwS3-1Q72deT-DeaiWNzsz4vcqNRJbfDhWayOFsfY16hLz41Y0QHYl-7ZR-LoU6dmV4kC3ver9IB2dgGYW5l0wVmx-4-oEkyMgyPEXPj774MRKHfGeFBmhRyHqUGbunuXbop5agSm7rWrZsJeATwjIthllbESG3D15U4zcoBIRn82Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
پست های جدید ترامپ
از تصاحب گرینلند تا جنگنده و انهدام ۱۵۹ شناور جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/69384" target="_blank">📅 21:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69383">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEQoO7oo5VpQGbM_7KlCPhnv4roAdRgArO6KJ5DWgmJDKGcBUsVuyiLUkayDeZPmEXR8vdP5dEEqArV4ePQQX0xD01MSdvBTy0JD7MZsmLgbXaO7czHlwByuglB3MOnF0iqzf08X_Bj2FQlNaWl4sOYqOpr-gfSlVUf-f9yS74GTfwjvj7Vvt7v_p7EeJ2SzpwiWJTh0K2Y_NlMX8snWUIBUhmBXg6dfpJBhbWmwJhdlDW9sGinAM2AxNTd21bEu7et0xkl_abYkVpCNuHD2qlL-vt24nyHPr1vtNOezFP3MPHijb0gkH_Rt8Gie2n8c04I0I8CsvA9q08lLtJflTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/69383" target="_blank">📅 21:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69382">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdMpaES_HNKsOjKpBtC5izP4jqnt8Var-pBOyrYackC02vg_daSR7qNMF3yYINsID0S-zA72g8QBrz9fsWSVYdEOKp-HxDF1yzOXUmFZcIyljBsBjh04rDBwWLVmtGmRuU0HXlwgFfvRFM2WIWvVGUCCkRSY0WpZ9C05K3Wl0aZG5ptBpME6rAi6IF1GT5K-hv1hay4RujjyyxhZmnXvAI96ZpCnszGzgnZo93cQwlLyI49daZhfFYSTG2D9HxfVP0dWYLC-cLIvk9dDlgsoxeH55TUPfBygAr_X9f2LVz80fAGY_cIC2cIBZvQdYDnDWoezUfC30pZn422MOqAIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی:
بر اساس اظهارات رژیم ترامپ، کاملاً محتمل به نظر می‌رسد که پس از ماه‌ها تهدیدهای وحشیانه، امشب آخرین شبِ وضعیت عادی در قطر، عربستان سعودی، کویت، بحرین، امارات و احتمالاً عمان باشد.
اگر حملاتی علیه زیرساخت‌های غیرنظامی ایران صورت گیرد، زیرساخت‌های حیاتی این رژیم‌های همدست — به همراه زیرساخت‌های رژیم صهیونیستی و شاید اردن — ویران خواهد شد.
مردم ساکن در قلمرو این رژیم‌ها باید فوراً برای تخلیه آماده شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/69382" target="_blank">📅 21:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69381">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
کانال ۱۲ اسرائیل:
این کشور در بالاترین سطح آماده‌باش قرار گرفته و مقامات ارشد سیاسی و امنیتی در طول تعطیلات آخر هفته مشغول رایزنی بوده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69381" target="_blank">📅 20:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69380">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omYBfJFsM46rgU4ufK5VaaznOb_gzAFHgtQ7Jrfb_XWqzzx7Me1odp4smq22I2vAa08kWqHPZS6y20lXDbI5egVK5JZTQQH3Qcuz28QNGT6G1IhEhXK4cdXUiu4z0dlGkf9Vye_V6LUxUPEBt3_THheCWBmRAFWXIDkOqilbiFKEacy1hx_I5hFFzY71bSDE79yTG6WDf1PKR1jSinV3R_xCs-Is7I1o9V7D63mLeoVa6A2NtdjXRLQCr4JW-GCDi3F6cso3ijFnJND1utyTIVXC_8O4Jjesz7aKrJh-DFuNX9Ke2b2oPSxYSUEWRW57kUxoCKklwk9t-8qDTsZ9Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
🇮🇱
کانال 12 اسرائیل:یک مقام اسرائیلی؛
«تنش‌ها به بالاترین حد خود رسیده است؛ ترامپ بیش از هر زمان دیگری به انجام حمله‌ای بزرگ علیه ایران نزدیک است.»
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/69380" target="_blank">📅 20:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69378">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/799177ea92.mp4?token=j_xmXrkFi5GZEnlPwc5jbldY-jc2kR4ZqWLnWYFaFdUJUheK1wgkaLVXFX3zX5N3VW8YIho45bSu7IhXOmUhAq0yLsU86lGZUC19hdVtkNlZqAgzCNUZHWtx83zjfFNwFChsKVwhjVwpoWC_lv0722gE4k1b3a4wCkM_Llgug3kUfWxXuT7KtDKbcX-PELaxpk8TDov1jyuteE_BoOwhfgOj_T0BMYQUMm36vxXFvgzN194WCEyLEHdDhEJ3U7ortqgYVUI6noowb3alvm6FfjkcCoBMxL0S0cYC4pL724k16Jt31SGqoDnPiLWzppsqbKCQX0ogpvv46ZTZN7H1AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/799177ea92.mp4?token=j_xmXrkFi5GZEnlPwc5jbldY-jc2kR4ZqWLnWYFaFdUJUheK1wgkaLVXFX3zX5N3VW8YIho45bSu7IhXOmUhAq0yLsU86lGZUC19hdVtkNlZqAgzCNUZHWtx83zjfFNwFChsKVwhjVwpoWC_lv0722gE4k1b3a4wCkM_Llgug3kUfWxXuT7KtDKbcX-PELaxpk8TDov1jyuteE_BoOwhfgOj_T0BMYQUMm36vxXFvgzN194WCEyLEHdDhEJ3U7ortqgYVUI6noowb3alvm6FfjkcCoBMxL0S0cYC4pL724k16Jt31SGqoDnPiLWzppsqbKCQX0ogpvv46ZTZN7H1AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تخلیه پایگاه های هوایی آمریکا در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/69378" target="_blank">📅 20:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69377">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/483837b794.mp4?token=dmG0vlmWPj8rbXQlGUmf5Yk2vqs4n7AjqLr0ZKd2_2MQ4DQWXPtOQlahhoac89cBrMYziK0bp-PHKhUvE9zfSdvV_R-ntWPMd9nWNFXLdwAc5lwfvzJIm5a8Z45p8hupz8zhms4TwTgdjw2o8oIAlpPQbYQKK-SMP4xQhdnbHaZ8sWdB9HIQ7_tenLdjSQ-7KLNF8zsiz_13inlI7FLDA5ASX6IKDIW4N12BFJWSxPhy0op5yvHK-dWg_W-ggg7m4oYgsOEgy3SmTRgDv8Qzi8-ntputui_gmgNMZHrcTcQgj8UcoAxlMbaq96E8S3BMFm28Sfi020ADU-DHWXM73w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/483837b794.mp4?token=dmG0vlmWPj8rbXQlGUmf5Yk2vqs4n7AjqLr0ZKd2_2MQ4DQWXPtOQlahhoac89cBrMYziK0bp-PHKhUvE9zfSdvV_R-ntWPMd9nWNFXLdwAc5lwfvzJIm5a8Z45p8hupz8zhms4TwTgdjw2o8oIAlpPQbYQKK-SMP4xQhdnbHaZ8sWdB9HIQ7_tenLdjSQ-7KLNF8zsiz_13inlI7FLDA5ASX6IKDIW4N12BFJWSxPhy0op5yvHK-dWg_W-ggg7m4oYgsOEgy3SmTRgDv8Qzi8-ntputui_gmgNMZHrcTcQgj8UcoAxlMbaq96E8S3BMFm28Sfi020ADU-DHWXM73w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کاخ سفید:خداوند سربازان مارا حفظ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69377" target="_blank">📅 19:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69376">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c746862829.mp4?token=GxFooscgbkpavGMSdlsciNiKXelrr4JaXXpWqsMe-KqgaDLV393ZDgIQKUPhRaA9o6oyq-VWEoSxZsSyC4qc9Wucui-VPaLwND-_cuFREjmk5h7JdCPgxz2ONVZtb52ktjn8utEzmpxYiY2dsaqOX-84OXHB49_-F2mazoif0zEwitTJS9Y2P_-Qu0U0aIVymOedLVaE-GYQEdtbe57gXSFcY9vPIhlCaHXUkLudlg6KjF0Aleerlk69RKxI9RhbZW7jAY7V_s4QUkL4nR_D4Loo0RE0oSVzLBT-RAoj93k06IsiVwxeTXkCn_xY6RCVmV7bCj69l0ys6hPvMQe5ul0O94BBmCOe1cTLihvn02j48Md8XXktaKviuGa3x1Cg4QU5XKkSw_CvgS3BnUIT4nOCm0e0_Ax-HZqHsCkcRqeqSJmWK0IvgKXHWVuCKiZmkGRnO7sGsgqYTkAfDp_LzT0Pm19ZqDpnrhkKqmleYHsmawpvEPqKy3jzM0KcqZIjGSAr_og8WY0BTVLdHIScBAYIrrSOoHJEutZ-eAZVRFNSTq9vjUQGCA14caxo8Eeuyz4M5mhct55m7lBxrO7ylMIIoX8FPTdqdst6qdUm5Kgq43zFDdtCWcXGZfi88u-oNDN96WotaBXhycTrKAqGWVAOmx6YTmHB3Nbd3bZk95c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c746862829.mp4?token=GxFooscgbkpavGMSdlsciNiKXelrr4JaXXpWqsMe-KqgaDLV393ZDgIQKUPhRaA9o6oyq-VWEoSxZsSyC4qc9Wucui-VPaLwND-_cuFREjmk5h7JdCPgxz2ONVZtb52ktjn8utEzmpxYiY2dsaqOX-84OXHB49_-F2mazoif0zEwitTJS9Y2P_-Qu0U0aIVymOedLVaE-GYQEdtbe57gXSFcY9vPIhlCaHXUkLudlg6KjF0Aleerlk69RKxI9RhbZW7jAY7V_s4QUkL4nR_D4Loo0RE0oSVzLBT-RAoj93k06IsiVwxeTXkCn_xY6RCVmV7bCj69l0ys6hPvMQe5ul0O94BBmCOe1cTLihvn02j48Md8XXktaKviuGa3x1Cg4QU5XKkSw_CvgS3BnUIT4nOCm0e0_Ax-HZqHsCkcRqeqSJmWK0IvgKXHWVuCKiZmkGRnO7sGsgqYTkAfDp_LzT0Pm19ZqDpnrhkKqmleYHsmawpvEPqKy3jzM0KcqZIjGSAr_og8WY0BTVLdHIScBAYIrrSOoHJEutZ-eAZVRFNSTq9vjUQGCA14caxo8Eeuyz4M5mhct55m7lBxrO7ylMIIoX8FPTdqdst6qdUm5Kgq43zFDdtCWcXGZfi88u-oNDN96WotaBXhycTrKAqGWVAOmx6YTmHB3Nbd3bZk95c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیستون؛
جایی که سنگ،
به زبان تاریخ سخن می‌گوید.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/69376" target="_blank">📅 19:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69375">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b275487f.mp4?token=kQ_RKfo5GLnnlPKyExWQL-HwCECmndaVMUoSisDoZILLIAThpUd6mZXw08JGSRbRXa95qnj8IMx6SNp7fA57s5i0pCGeIim25n7D459eFnsuSH5XcyjQfgTd4VRaOdKExKoyJ4DTv-E14hyoZE71TSJDYRDKq81AcJK0XcCpL2oYNJ0Sw7jD2By7tY27HxAzvWGbqLfDfKAMBpHoqX9tSiYZxfqm0W7huXYv24HR0aer0DpkX5ZmdvYlVmp3e4MBbvtIfprN6aEG2LFP6zEpTuT7-MWm52j5OaOY-6gnEf2urjBntsaseed7Vt1FyLiEZs5F5AYl_pMeleRzFc94Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b275487f.mp4?token=kQ_RKfo5GLnnlPKyExWQL-HwCECmndaVMUoSisDoZILLIAThpUd6mZXw08JGSRbRXa95qnj8IMx6SNp7fA57s5i0pCGeIim25n7D459eFnsuSH5XcyjQfgTd4VRaOdKExKoyJ4DTv-E14hyoZE71TSJDYRDKq81AcJK0XcCpL2oYNJ0Sw7jD2By7tY27HxAzvWGbqLfDfKAMBpHoqX9tSiYZxfqm0W7huXYv24HR0aer0DpkX5ZmdvYlVmp3e4MBbvtIfprN6aEG2LFP6zEpTuT7-MWm52j5OaOY-6gnEf2urjBntsaseed7Vt1FyLiEZs5F5AYl_pMeleRzFc94Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇷🇺
دونالد ترامپ، رئیس‌جمهور آمریکا، و ولادیمیر پوتین، رئیس‌جمهور روسیه، در قالب «زوج در حال بوسه» در رژه کانال‌های آمستردام:
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/69375" target="_blank">📅 18:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69374">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4517b5c3.mp4?token=m6etFU-p7PBPSAyBJKf43DxdJpjsWJy5vrhA6Blf2assSR_diOi06wi1HLNrdz441mtZyVKjt6hHBUap9xczyrDHx7qnuU1YrAgO5kJfGM_g85XMX2ucanI3Pg59hdQo7n2pkFXORPKHxNjQUt7IIIDAiAr9ZZpD7pfV0T7OL7SYyh_5OaiABumg6lSRXHs5P7V8vxcz9R5RZ7hETnf6fbOwx6xosGmG5osqL4ljIzc767YfUZZd_UJkDSlTmUxHfQxup9wCJYx-2sQN6I8lw9W5kF217A7RmysakrtgDDOCFFWvetg6HooDF0lIvSAIlHuKdAv0o7LZtJpm7Yt_Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4517b5c3.mp4?token=m6etFU-p7PBPSAyBJKf43DxdJpjsWJy5vrhA6Blf2assSR_diOi06wi1HLNrdz441mtZyVKjt6hHBUap9xczyrDHx7qnuU1YrAgO5kJfGM_g85XMX2ucanI3Pg59hdQo7n2pkFXORPKHxNjQUt7IIIDAiAr9ZZpD7pfV0T7OL7SYyh_5OaiABumg6lSRXHs5P7V8vxcz9R5RZ7hETnf6fbOwx6xosGmG5osqL4ljIzc767YfUZZd_UJkDSlTmUxHfQxup9wCJYx-2sQN6I8lw9W5kF217A7RmysakrtgDDOCFFWvetg6HooDF0lIvSAIlHuKdAv0o7LZtJpm7Yt_Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
فاکس نیوز:
رئیس‌جمهور ترامپ در حال تشدید فشارها بر ایران است و می‌گوید در صورتی که مذاکرات دیپلماتیک به نتیجه نرسد، انجام حملات نظامی جدید همچنان یکی از گزینه‌های روی میز است.
ترامپ پس از دیدار با اعضای کابینه خود در «کمپ دیوید» اظهار داشت که توان نظامی ایران به‌طور قابل‌توجهی تضعیف شده، اما این کشور همچنان از برخی قابلیت‌های موشکی برخوردار است.
مقامات آمریکایی می‌گویند این حملات ممکن است حتی در همین آخر هفته انجام شود؛ در مقابل، ایران اعلام کرده است که در صورت هدف قرار گرفتن زیرساخت‌های حیاتی‌اش توسط آمریکا یا اسرائیل، آماده پاسخگویی است.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/69374" target="_blank">📅 18:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69373">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f0734246c.mp4?token=WFi-GiMtTdWcowMBtOcXyoj_55DfG13UVd3iSzg41GDlLPOMT_HSx3rmSXJLGsF2NuXQhWxwMxAp3qw-NMdmRyyb1xRzWYBRL6wSKK4ySfU5wzXP87mZakNCb9M8JfbN9Urv6DEsis2IUhG-T4zIly87oEflHUq8YuM2tC4fX75k6DX5sl1gIiayAVzQNmEw_pH5stP9vURCxTzPbmCAmyPSPSdUhjPVk7yaLANBzSeoAdUEu14hz0hwMKeQaBF6UucfeyfyvIf1TkiDk0VwPUYMGieEBVR4w_5KivDtmJmKcJBybBCcFooXN1blP4p3B_B8RMQCR1mVz92CEhCgjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f0734246c.mp4?token=WFi-GiMtTdWcowMBtOcXyoj_55DfG13UVd3iSzg41GDlLPOMT_HSx3rmSXJLGsF2NuXQhWxwMxAp3qw-NMdmRyyb1xRzWYBRL6wSKK4ySfU5wzXP87mZakNCb9M8JfbN9Urv6DEsis2IUhG-T4zIly87oEflHUq8YuM2tC4fX75k6DX5sl1gIiayAVzQNmEw_pH5stP9vURCxTzPbmCAmyPSPSdUhjPVk7yaLANBzSeoAdUEu14hz0hwMKeQaBF6UucfeyfyvIf1TkiDk0VwPUYMGieEBVR4w_5KivDtmJmKcJBybBCcFooXN1blP4p3B_B8RMQCR1mVz92CEhCgjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک هواپیمای سبک قاچاقچیان کلمبیایی در حال فرار از رهگیری توسط جت جنگنده ونزوئلایی.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/69373" target="_blank">📅 18:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69372">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f45020b76.mp4?token=WhavVHFSlS-tbIqr5FN4IBVwG-Hy2vyGqZ3YByBI59rlu1ljkzvtEWARJdlPvr4AZL7Sa_OgLh7M7XBd8sChTmiDBoWmxzd-0U4YMd26xZ1ZlFm_AHbddcFPymG8CxJQVmH2RV25aHRn90Mx0jSdLKe3nNU7rWQvqr7g7me9tXIgd2ciF1wqZuSy5xXrn9cPKGIU3l8AccpUVVLWeHZPOSUlkRJQ4fUo9a_uNqzGl9sq_k51_2nCvxffCR87jx2Fs7ja7eZtPz8cIiOQwU7i4kHhcbZ8vleNq1NMIqm_p_aXAfZ1ttzY-eftYSrHhUOhHumqkaBEhgSOUjsRYF213Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f45020b76.mp4?token=WhavVHFSlS-tbIqr5FN4IBVwG-Hy2vyGqZ3YByBI59rlu1ljkzvtEWARJdlPvr4AZL7Sa_OgLh7M7XBd8sChTmiDBoWmxzd-0U4YMd26xZ1ZlFm_AHbddcFPymG8CxJQVmH2RV25aHRn90Mx0jSdLKe3nNU7rWQvqr7g7me9tXIgd2ciF1wqZuSy5xXrn9cPKGIU3l8AccpUVVLWeHZPOSUlkRJQ4fUo9a_uNqzGl9sq_k51_2nCvxffCR87jx2Fs7ja7eZtPz8cIiOQwU7i4kHhcbZ8vleNq1NMIqm_p_aXAfZ1ttzY-eftYSrHhUOhHumqkaBEhgSOUjsRYF213Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز صبح تو یکی از حوزه‌های امتحانات نهاییِ اردبيل، 9 تا از بچه‌ها مونده بودن پشت در و داشتن گریه می‌کردن؛
طبق ادعای خودِ دانش‌آموزا، مسئول حوزه ساعت 07:03 در ورودی رو بسته!
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/69372" target="_blank">📅 17:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69371">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
ویدیو وایرال شده از این هموطنمون که در زمان شاه حضور داشته :
زمان شاه به دانشجو هایی که میومدن اینجا درس بخونن ماهی 400 دلار حقوق میداد
اون زمان صدتا نارنگی یک دلار بود
یه اپارتمان سه خوابه تو نیویورک میگرفتیم با سه تا توالت و حمام اجاره اش 210 دلار بود ما ماهی 400 دلار اونوقت حقوق میگرفتیم از شاه
شورلت کامارو یکی از ماشین های اسطوره ای امریکا بود سه هزار و صد دلار
با یک سال تونستم ماشینو بخورم
امریکایی ها میگفتن کجایی هستی میگفتم ایرانی همشون میگفتن شاه شاه شاه
کدوم شاه شما دیدید بیاد تو امریکا براش با کلی عزت مراسم بگیرن که برای شاه ما گرفتن
چه افتخار و عزتی و لوکی بود شاه واقعا نوع بیانش و لباس پوشیدنش هرچیزی نگاه میکردی لذت میبردی
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/69371" target="_blank">📅 16:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69370">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N35rvDad6VBdjmxb8QBjArpQJIP5-Ng06CwbaVoBEu3K-bmmmtA6KvdzB9NsVUONSBPBF1se9pRd_uBsUPEFc8E3xeMlI4rZoBX-hmjqRyqMWJFxxp6jRChSoKTHoHtDmOXCHX42Im6EKQ81M9wpSs-FXqxLPiAFItT9Zq0JeJ_qeC3rdAemRF6qTAuEROUSnguMTC0XbrJD5Az6fZlnuvZVcYD5aKUrrfUFvoIf_Fjq1LbLQd7nsdi2MzxwktDPKlbFwQjhjmUh_ofDbIBoLBeIF3UC0fAFq0xvGTbykZfBOTaV4CN57RcDl6D9rEEvA6F7p9kdAvpKeRasIu30yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سفارت آمریکا در مصر هم برای شهروندان آمریکایی هشدار صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69370" target="_blank">📅 16:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69369">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46327b1ae3.mp4?token=E_4-7QPqXU6IQSgIqtfFu2O_1aBrpMG4YY9YbVoeD66DwazuhrOig22CkHJsbzxf_BTHyW5_hr2uUNIPiuFD2zxpy08wtDfwDjOgsUqt4yiw4YEDeHjSkhmPIF0AAkrY5N0y9yIX9csEGveJbmFAcHrUa8zYhlpvt7O8K3rQLcfOekXI31tFVD8136qmikLqrLAX0_oyW6CZmiqxWOEdZYcjTtNqnXFNGYtVajVC4gQSZjwO0aUNQodT4cUi8W3_dQbkYbB1sF5KlfQeSon2YPZIkD6Zd3nJZ7xaum0OKqvTKhnDQI9UuwyVBC-ucO49Nd0C-79yHTTGra0AXr1tVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46327b1ae3.mp4?token=E_4-7QPqXU6IQSgIqtfFu2O_1aBrpMG4YY9YbVoeD66DwazuhrOig22CkHJsbzxf_BTHyW5_hr2uUNIPiuFD2zxpy08wtDfwDjOgsUqt4yiw4YEDeHjSkhmPIF0AAkrY5N0y9yIX9csEGveJbmFAcHrUa8zYhlpvt7O8K3rQLcfOekXI31tFVD8136qmikLqrLAX0_oyW6CZmiqxWOEdZYcjTtNqnXFNGYtVajVC4gQSZjwO0aUNQodT4cUi8W3_dQbkYbB1sF5KlfQeSon2YPZIkD6Zd3nJZ7xaum0OKqvTKhnDQI9UuwyVBC-ucO49Nd0C-79yHTTGra0AXr1tVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پیرزن ایرانی توی مراسم اربعین، برای اینکه از یه زن عراقی صندلی‌شو بگیره، بهش حمله‌ور شد
😔
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69369" target="_blank">📅 16:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69368">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حالا ما کجا بریم
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69368" target="_blank">📅 15:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69363">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KG_9krxTIV_Cbc_mkXcSW4Vllbk8Iv0nB69C9njnWYH46GAa3Ts6p_xMOFvdRDFu2ClwD9Rhh39RBeiiwYOGQfDu-HPpzgT-Os1-gPmMnpWBBTPqBkqvrCEG70k1yGHVpEcvRxEeUHVRsnXM8yMbuf4XkpatKCMAo_UH703x76u_IWM0UXwrOpX2kMmgxXLkWMGMml-wHh_YExJeU7A0yG63l7ou3ml0dPNVaQBqvRq3QjgxjafiCCqd1ZSinzmARPoPuXmyHmAGq_SR_jJx4er5wVt9wmiaerSa3KYd9FkXY3US0gtecO4-Pkiokh12fyHYplsX0EWvf1HHJscM2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dt5FhOkUd7E6FwcarKNUDwyfd0eZfUI8zsIt_lSMCCsu4240I4PjVayyTTIpJV33Jxn-FctmBA2DM0YYhebCP2uDFV-3G2gIGV1DMKYO6z16VD1zn6OcMyGLem68vBAe0hIfIP1VjJ0JjzHYJoVKDlw9xaj7QBuQo2ShphqfClYuUSSSCbcO0NBdC0SfrYClyEbgquIi-JgfmlmWCB6l_7iFParFkkK4-HoTiVR3xwextvaEWb4nePnr4vgYLub4lljUIvArX1BNFdmpssnoa-TgP8wd6-Roh7jUB-NIAr3_00W93YDoO13Q4KifjVtySM7cwDsz-L47FKv9btegmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K1JLIz0ImJtoEiJXJYLm81czKJ6G2LVVnHYNuyX-TBKXBQCU5Tuso5Y8wNA0EAZmas87au4AV5V_9hMUEmRtBp9drEIplK9ge6Ayblxa7jPwsnWOEZ2NkhU23W2zWmABKlGiNDPPuje1gLiPwKf4UCf9esd71QtdwiMcGq5tDStdcjjBkMBtM3GH92kRkUBjCw1OVVgycXZZOHdpkLgZECqStfLqxDrNTIxk6sKusZetaWHYnpXnQxKCP5e-t-wkGhx4zePX1U-URnM7S4QPLCZLaaXJx_JDp_XV3ukPscMuxjCFli-bHX6cmVaE6Fgdl850QnB08ad8EyKaP46g3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dREnlKYyv5TSNMmOIV0oV4mJ4nbe7Acmsmzh_1IKF9y1to9QHjXeDeMIjTUX4dAcpTIZnbaWEdE1ZeAUbFkivjc4IqDl6o_8KIc_60295UQ3Kwg7eAj3xz0NHDChxAfKANQ292y_rcSOi4wqpXdVQtbqf1x47sudhOLfd-Tr40mw3kIti34yhryDKkfMU_xiWMxjJK1CmeDvPEeYgseYfr-jLwu4d82YaEFhLOYF6HMOjNj7lpT9csqTn-0ZmoI8RQmbOT-xFNt4sy6mFtRpqVIlrZK70CgWU5snFDaMrQtL4VUNgYKiVryj9P4I1KOySu3ciep9JsLlXqD-7MHkyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-GfOoZwSbsLi1MQAq2H9sI2l2PrktcCNt7y2t6CmXruOZ6xQfNBV1dmTN5ohp2jT7Qdh0qxOXcswptGlKgEbnhiyMVilKyMGzH5W8cKLJ00UlC6g7Z7pjkGkHPcceSGwLTct9x3rw2cooXET5_EhtuNAGBF3P8-c13Xa9_nr_BbGOeeZFvG8F2ruTlOB0eOvlRtcm6LMgMsDxbiELehasRLcRqb0RAkfmSuEjCav_vC2q6Dc4mb3VQScBfzr5jgu9hKudv77411jF_RSe0o0ExD7zmGlZWsMVy3wqyQN4bxm26iWnTXAl9XPYoGI5K7gLgqphscoFmX9w8fYEArng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
سفارتخانه‌های آمریکا در خاورمیانه یکی پس از دیگری درحال صدور هشدار به شهروندان خود هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69363" target="_blank">📅 15:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69362">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be758c5d3.mp4?token=jykptGr9-yZIcI6qnFJDowD2cnMGhHqHguvxpHPB5Sfiei9uxNA-xz2Tzw1mw8D0pjNgYqiTr78llx_q0FtKhO3eZ7a45wsyYWlZrahQPnEHVp9T1ZaDhHBxIEkYyHWmgYAgfoUyfNwPwYgxbxMDnGPpcZr1v5Qc8USDXtam-fN7EjEpVjPIzWxhNfN0IAQmEJ1rA4i20goSYxRuqzsrNjs-m3apIfT2acpaagRcsZWirPD3UAeWgdjm7cE-_pugYZE8PC0COdegR2bLoehu-WdAr7u32Fe0nQAkU9z2y_r7xsNieW2l1CqAWh0LBeZUpbjr34JjUqpHR5sG41DMyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be758c5d3.mp4?token=jykptGr9-yZIcI6qnFJDowD2cnMGhHqHguvxpHPB5Sfiei9uxNA-xz2Tzw1mw8D0pjNgYqiTr78llx_q0FtKhO3eZ7a45wsyYWlZrahQPnEHVp9T1ZaDhHBxIEkYyHWmgYAgfoUyfNwPwYgxbxMDnGPpcZr1v5Qc8USDXtam-fN7EjEpVjPIzWxhNfN0IAQmEJ1rA4i20goSYxRuqzsrNjs-m3apIfT2acpaagRcsZWirPD3UAeWgdjm7cE-_pugYZE8PC0COdegR2bLoehu-WdAr7u32Fe0nQAkU9z2y_r7xsNieW2l1CqAWh0LBeZUpbjr34JjUqpHR5sG41DMyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده‌یاد مانوک خدابخشیان: دو شعاری که کار این رژیم را تمام کرد؛
رضاشاه، روحت شاد.
اصلاح طلب اصولگرا دیگه تمومه ماجرا.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69362" target="_blank">📅 15:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69360">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A-O25AjOPId9MClm8FaFBa9ig1yiiy2CpOJD8VKtrTFb-YpbnqHkG3hzurt2PuIPNihLOpKVYk86s22aocmk5MQPq6Ls_3WxB71wN-yFPoN2UcuacnUaOEzEgc5PU75_rFGagWZUZvOAN_UKGqBkGzejXv2SOX-tsl9_Qo408KcgDVZzCYOZ3zJVNHBqOSDf9xUQTJTaIJqFCOyqkD34MsTWOTPlKfhIHp-8xwO_YzPQgOWyRiadjVy08gZmrHJqh5tbNE2NeIJplItyELa_yD7jdwEqsIGit6qP2Kh4137BUFqURdr59Lg8NQy4tb7cIWyw-FJ1vODjxUNYtao-pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ijy-XvJlvHyYr0XmwvBVqXEDTazX7NsA1P9nyxlIqGVoP7I5KUf5BUmA4HECmoCsjkpsGeTaLZfeoCVmWLjVTkpaTn61yFmc6QGRYTQmjCU6S0Euvf8j5sWvsqXrD4swE2Za5M3fFH1lkIHC16memvcCYAuphRe9n1ypNf4iksTYlwkNNA64orbG8YLSiWGMX0D6c5mSXBDU6R2D60SAGi0H17VKN0miAHCfUDAB6swOZCfY-xSj2JKLzdfbn8jG90M-WedhTvH6n7lefw31idZsEsv-orhZ_7Qo2evnl_HMZ5UnoCBj8D02Dalqq5tNo_npLk88bP8f5jrs3ZAuTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
سفارت آمریکا در اسرائیل و عراق:
آمریکایی‌های حاضر در منطقه باید آماده باشند و در صورت تشدید تنش، خروج از منطقه را در نظر بگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69360" target="_blank">📅 14:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69359">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQb5lorT_ZUHNdLQ6t5plDNo_u1VaxRvM0F3_8hSVNrxsH8wZ9WTNQiCE_zxtfTc7wNZzVK6O3loPJkUh4_gGVBwgjNwqPMev7jRXYOPCQ02uA4cqeV-gTEZWGrvR6bKWKetIXFevAj1L8zavK2act98-Y1epwvwQgVkDi0TSPgVVBT_U0H71m-qm700S6CD2fqL1DiA1VAphh910sekK2dx5CWsyRe6v-AvNuc9b_QfiXw-FLFqsDODTDV2KOjnRGEGCkxlnxecG5F0JslKFIquRKr8NIRMGNoz3b2bVe1kNMRRBiQtm0rQR3Dy7DnSPs26ocDntT8bbjGGtNA4gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تسنیم:  بهمون حمله نشده، گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شد.  @News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69359" target="_blank">📅 14:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69358">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
تسنیم:
بهمون حمله نشده، گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/69358" target="_blank">📅 14:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69357">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
دقایقی پیش از حوالی اسلام‌آباد غرب کرمانشاه، صدای چند انفجار شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69357" target="_blank">📅 14:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69356">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c794c22fb.mp4?token=C7eth1B3lk6YzMPB3nUUjEa78OCPJydx3--7OSNnoW0-kO-M76QzybSIKq9eC0aVmJMOMTSzi8Pk3onmCJcsU6dmZoBYryF29EmtGPpj9MO-2qsgPauyI2_0toEIpwUvVeybjd_Abfv_L_5o_Wyx-Hg-s086Yuy6izTBaoduas6FdXt_YXdh_9C7wqwpbbPdgvRUdOBVqagkbX1sHYVVaXa6EBPYeHoZUCsy4tW6YKEwzqaECb77HVLYLinbNQY5Mv2mcAp4o4sb3ytpBWUVYoeLOufoAMTdYO1xX8fklm4LPL-bgCu5kGxFA5eTcohiOp6NLU7KFBomPfR_UmVz3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c794c22fb.mp4?token=C7eth1B3lk6YzMPB3nUUjEa78OCPJydx3--7OSNnoW0-kO-M76QzybSIKq9eC0aVmJMOMTSzi8Pk3onmCJcsU6dmZoBYryF29EmtGPpj9MO-2qsgPauyI2_0toEIpwUvVeybjd_Abfv_L_5o_Wyx-Hg-s086Yuy6izTBaoduas6FdXt_YXdh_9C7wqwpbbPdgvRUdOBVqagkbX1sHYVVaXa6EBPYeHoZUCsy4tW6YKEwzqaECb77HVLYLinbNQY5Mv2mcAp4o4sb3ytpBWUVYoeLOufoAMTdYO1xX8fklm4LPL-bgCu5kGxFA5eTcohiOp6NLU7KFBomPfR_UmVz3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه جوون عرب داشت به زائرا میگفت بیاید آب انگور بخورید که یه ایرانی رسید و بهش گفت:
آب‌انگور نه، بگوآب‌شنگول
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/69356" target="_blank">📅 13:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69355">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917485436c.mp4?token=Qt7vQ1wGhOvtg_N6GUoK-lt7Ju2yQIOnqnxBaEu36bausn5isQ1GFMiIiX16RN4kkv7-knZXNySCsvIe1ahen7_G7z-gZyIH8aleh9IBKgGy40qJJ05usLBRRkFao0OaEqC4_Q0p0c0vRzz0wtNIhumal5wHBfjiuJPzz2QrgQ_SEiLFwrTD9cUgwnTTlOUF592Oik1nWqiBaX3ozV2L3c6Acs_iPitgeHzNQ2A8MPlRCo8rbYOuY2Z0M0Gp7cMdB8hMVMsl_ehSJA86X4LTg3tdxgHrXRWFonk9XA7p_pVeG1JGMXoJeBUaKb0KVv8o7UxiIEukGXfXCvlpFP-ndm8kwZMCjEJd772OeLEklBKcGuPMPCoBNGTsv9c4nCHi0ho8Lw0htozC9qpYJfcfy-_vjXKNfhpi7goN9at_0_3ZZLAeBxJntqLLzov1kcjo-H30l59z5yTnPEwJGc95Wps9j9HJILP1kXbstB6kptg2qNqG7Z_dgAx2xP8uTitVNiJaJlPfM2JnkcFaibI80d2GGL89c9Ph4CnyK8Io2HADzLKWFjCaTv772KyFBbj-p26jPXGWV8c6kuOix6T-KvFc1q7jazYkZZuDsij2RmEjxvZDri9j6n8c4C4GJtwXSYz4dWLf9TLQq1O6ygvv1JEeIh-XXIy7A0QrgYhcnEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917485436c.mp4?token=Qt7vQ1wGhOvtg_N6GUoK-lt7Ju2yQIOnqnxBaEu36bausn5isQ1GFMiIiX16RN4kkv7-knZXNySCsvIe1ahen7_G7z-gZyIH8aleh9IBKgGy40qJJ05usLBRRkFao0OaEqC4_Q0p0c0vRzz0wtNIhumal5wHBfjiuJPzz2QrgQ_SEiLFwrTD9cUgwnTTlOUF592Oik1nWqiBaX3ozV2L3c6Acs_iPitgeHzNQ2A8MPlRCo8rbYOuY2Z0M0Gp7cMdB8hMVMsl_ehSJA86X4LTg3tdxgHrXRWFonk9XA7p_pVeG1JGMXoJeBUaKb0KVv8o7UxiIEukGXfXCvlpFP-ndm8kwZMCjEJd772OeLEklBKcGuPMPCoBNGTsv9c4nCHi0ho8Lw0htozC9qpYJfcfy-_vjXKNfhpi7goN9at_0_3ZZLAeBxJntqLLzov1kcjo-H30l59z5yTnPEwJGc95Wps9j9HJILP1kXbstB6kptg2qNqG7Z_dgAx2xP8uTitVNiJaJlPfM2JnkcFaibI80d2GGL89c9Ph4CnyK8Io2HADzLKWFjCaTv772KyFBbj-p26jPXGWV8c6kuOix6T-KvFc1q7jazYkZZuDsij2RmEjxvZDri9j6n8c4C4GJtwXSYz4dWLf9TLQq1O6ygvv1JEeIh-XXIy7A0QrgYhcnEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
آتش‌سوزی در یکی از پالایشگاه‌های استان اربیل در اقلیم کردستان عراق
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69355" target="_blank">📅 13:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69354">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/532a951287.mp4?token=Hf1p2uYL9skoIKzs2BRI6rBTKtTNQ9N6jtC5HMFT4rE8ihdFtXUci6XeRsyZOgIMUwOoc8ZC8CscC_DLAC4VvXNQzGbY9QqgpmiTt6b5Knb6-ZfRfN0GMK5nzxGuJTSNvSbpkjsGwffX4xHuqH9srccoIVavWpMXZ85UacUPk4bBzJNz9ZnwGnqE6WvbyXX9A9c1qecJe10VQKL_4tDLAm1Uv4jAkSbe1v0_uVwSduDieGMAnhUv_nYncZO-NnYGXgzIH3dEAXkHun63e5LOnDh7LYaXTW6vmpFn185f6vfdghH41wN_9hrTJ83Tc9myOVNxcFO5rRgVFfm8K5z03g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/532a951287.mp4?token=Hf1p2uYL9skoIKzs2BRI6rBTKtTNQ9N6jtC5HMFT4rE8ihdFtXUci6XeRsyZOgIMUwOoc8ZC8CscC_DLAC4VvXNQzGbY9QqgpmiTt6b5Knb6-ZfRfN0GMK5nzxGuJTSNvSbpkjsGwffX4xHuqH9srccoIVavWpMXZ85UacUPk4bBzJNz9ZnwGnqE6WvbyXX9A9c1qecJe10VQKL_4tDLAm1Uv4jAkSbe1v0_uVwSduDieGMAnhUv_nYncZO-NnYGXgzIH3dEAXkHun63e5LOnDh7LYaXTW6vmpFn185f6vfdghH41wN_9hrTJ83Tc9myOVNxcFO5rRgVFfm8K5z03g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه لیلی فیلیپس پورن استار معروف که تو 24 ساعت با 2 هزار نفر سکس کرده بود!
دوس پسر لیلی: من اصلا از این موضوع ناراحت نیستم، چون اون واقعا زحمت می‌کشه.
مهم اینه که آخر شبا میاد پیش من، و اینکه من بوسیدن رو براش ممنوع کردم، اگه با بقیه سکس کنه مشکلی نداره، ولی فقط باید منو بوس کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/69354" target="_blank">📅 13:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69353">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d26851041.mp4?token=eNHfaPzxizbewoQY9z8DiVteaTsjvR0HFOygSI6R4iYAyp6TJo14tgrbg2xALndTfZOFKpjQhV_4lxwYe4bp3KHYyd4JPVVbRqa6bHeM2pcjXT43C2Dzg-iW7GnbTHU0LBPRYygz774TNZOaaTbaKzpxr3BtuYkGIunxz09YoPcYX62g3s8w_n9UelxiOd9pLCLCS9UuuqHuIKzEIjRakhkm83rNYRvJQPyRY9ubOjMeTgfgBy49vU9us89ReEFB8tUpbGsJlmS4MGTj8yCIaR4_BH6lsYuE1bWWgCkwavY4XDFZEmSewhPg8U3PsiFBx6gFPYVvVGFZesoB9y7h3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d26851041.mp4?token=eNHfaPzxizbewoQY9z8DiVteaTsjvR0HFOygSI6R4iYAyp6TJo14tgrbg2xALndTfZOFKpjQhV_4lxwYe4bp3KHYyd4JPVVbRqa6bHeM2pcjXT43C2Dzg-iW7GnbTHU0LBPRYygz774TNZOaaTbaKzpxr3BtuYkGIunxz09YoPcYX62g3s8w_n9UelxiOd9pLCLCS9UuuqHuIKzEIjRakhkm83rNYRvJQPyRY9ubOjMeTgfgBy49vU9us89ReEFB8tUpbGsJlmS4MGTj8yCIaR4_BH6lsYuE1bWWgCkwavY4XDFZEmSewhPg8U3PsiFBx6gFPYVvVGFZesoB9y7h3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از عوارض خوردن ساندیس زیاد
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69353" target="_blank">📅 12:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69352">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e653ac6e6.mp4?token=PZWDuPa41coIyN_mexiXEGe2NjMzQ6_oYCbKRRm21lPsyf_bCzkbasAPDpI25LYEdFCW4ncWQyr-DPXTtT0hraZGtTTuf1TN44uHKGIaq8LdOfflCUKzM94i3Y9HU8DXNKEv6oVC1JPwvI9p4BXUUBWCPNRWGnwTPo3xRdQNJ7qPkV4ppndObt-AaB6zYxolGPeB47xhgnJy3al3y1o1wwJiJLYG3tygW1UHSo1kbd4ezXUpzAAZkt9gsIC4fOJKCmUcjfvrwDx3uUTCxMf4xx2CNwloG_lZ6GqTRnxI-eCjNxY9t2gy3lZt_l8fKxelW6u2SImQD8dLF9_8yOVDbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e653ac6e6.mp4?token=PZWDuPa41coIyN_mexiXEGe2NjMzQ6_oYCbKRRm21lPsyf_bCzkbasAPDpI25LYEdFCW4ncWQyr-DPXTtT0hraZGtTTuf1TN44uHKGIaq8LdOfflCUKzM94i3Y9HU8DXNKEv6oVC1JPwvI9p4BXUUBWCPNRWGnwTPo3xRdQNJ7qPkV4ppndObt-AaB6zYxolGPeB47xhgnJy3al3y1o1wwJiJLYG3tygW1UHSo1kbd4ezXUpzAAZkt9gsIC4fOJKCmUcjfvrwDx3uUTCxMf4xx2CNwloG_lZ6GqTRnxI-eCjNxY9t2gy3lZt_l8fKxelW6u2SImQD8dLF9_8yOVDbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف: میخواستیم خبر شهادت رهبر را ساعت ۸ صبح اعلام کنیم اما تلویزیون‌های خارجی، زودتر اعلام کردند
.
در روز نخست جنگ و تنها یک ساعت پس از بمباران بیت، شهادت رهبر قطعی شده بود.
تا همدیگر را پیدا کنیم و هماهنگ شویم، ساعت ۸ شب شده بود.
قرار شد خبر را فردا ساعت ۸ صبح اعلام کنیم و از مردم بخواهیم به خیابان بیایند. اما تلویزیون‌های خارجی، [ منظور اعلام رسمی ترامپ]  خبر را ساعت ۹ و نیم شب اعلام کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69352" target="_blank">📅 12:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69351">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⏺
سفارت آمریکا در اردن:
از شهروندان آمریکایی مقیم در خاورمیانه درخواست می‌شود که برای ترک در صورت تشدید اوضاع آماده باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69351" target="_blank">📅 11:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69349">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14b8168f8.mp4?token=DsU5Nvywwy3GUshEGGgZw8s3uOxRblf-ASkllMwRlKu9uHoIriu5L1dvH2deyyeqGwGahUoIUq-S4o_rEd-1f-vHMA4ssAy-Z2qp3Y3PO9xO6C7YDEBo21cWI6mBRbXiP2eNo6ixQBzonlkX45A65zJglmm41lETW0ZWsa2kGjys1g4JAPuyjsjNYQf_6ykjn8W9HvnMFaSGgmZsm1Jl5ga9K-TR5-EsezYVe9Gcfj4xfp9sHB-cGGxXu5SxeYMsYdG7HXA25qaGPbfDhf_4iVG3TxjAOnL_kwMq_Od46I7-DTI-Z5uRPpUof3aV83-nAXBaMeqKCsH0K0mMWPDWXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14b8168f8.mp4?token=DsU5Nvywwy3GUshEGGgZw8s3uOxRblf-ASkllMwRlKu9uHoIriu5L1dvH2deyyeqGwGahUoIUq-S4o_rEd-1f-vHMA4ssAy-Z2qp3Y3PO9xO6C7YDEBo21cWI6mBRbXiP2eNo6ixQBzonlkX45A65zJglmm41lETW0ZWsa2kGjys1g4JAPuyjsjNYQf_6ykjn8W9HvnMFaSGgmZsm1Jl5ga9K-TR5-EsezYVe9Gcfj4xfp9sHB-cGGxXu5SxeYMsYdG7HXA25qaGPbfDhf_4iVG3TxjAOnL_kwMq_Od46I7-DTI-Z5uRPpUof3aV83-nAXBaMeqKCsH0K0mMWPDWXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
یک انفجار بسیار بزرگ در یک انبار مهمات در شهر خملنیتسکی، واقع در غرب اوکراین، رخ داده است که پس از آن، انفجارهای ثانویه گسترده‌ای نیز به وقوع پیوسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69349" target="_blank">📅 11:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69348">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71213a605e.mp4?token=iZkI7Iqb3oqXEIy1U9jsL54qPAbsZYBXro4d58JScHtLb1IDTCjfNvJuie1DuihLjsYvO-GkY9Wt3Mqo-X8cyFjzd96G-YrzT41V5a-TU4GIa1mlOrH5NOct81EDfYMJvSzF6Kz32dTX_F1YmiwRPElchz0Djz7tEd4rZYwJxpRI9O3tirrtX2bmlM5d93n5jQxJ3qkUhaTd7_sQorNd_qfoBNCLpKOYarZqJSEii9pMw1ofQwQ9z10pUjaqJ9KDDpEtf0BAop2YwAF7AUPaLiCpKOrPmG3qHWQRUrusaKqOZi_mOX_IyM0quih3eLrzvWpiHZ76lvG-K_ee64Qo2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71213a605e.mp4?token=iZkI7Iqb3oqXEIy1U9jsL54qPAbsZYBXro4d58JScHtLb1IDTCjfNvJuie1DuihLjsYvO-GkY9Wt3Mqo-X8cyFjzd96G-YrzT41V5a-TU4GIa1mlOrH5NOct81EDfYMJvSzF6Kz32dTX_F1YmiwRPElchz0Djz7tEd4rZYwJxpRI9O3tirrtX2bmlM5d93n5jQxJ3qkUhaTd7_sQorNd_qfoBNCLpKOYarZqJSEii9pMw1ofQwQ9z10pUjaqJ9KDDpEtf0BAop2YwAF7AUPaLiCpKOrPmG3qHWQRUrusaKqOZi_mOX_IyM0quih3eLrzvWpiHZ76lvG-K_ee64Qo2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
آمریکا و اسرائیل برای شدیدترین بمباران در روزهای شنبه و یکشنبه آماده شدن و ترامپ دستور حمله رو صادر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69348" target="_blank">📅 11:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69347">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmgXBTh3arxZbYJ3aOtuUZ3T7ERukDNV3HCrrtagwckTUA__CybVXA8iN1KP9C4p0KbPlHeFENFCVJ48MUbOSrHzCXXPJCVjiYJnlzQcTAaHWwfO6v7tFz49X6u6kIVG5CovKTCxzHR_Z1GaOghLD6Nu_TG1H3SAcGI-pvwU4zuPyPM3zEdigGWtOEZ1mGCCMN9j-TEhkcq3pnNUjbSLb9lcZ7z6bJqc7-2IJGznzA7cjghqfQiwSxI8_2erC-1Q3ZYDX9c2SJPa8Una5IepCRyCQsaC10B-vKKvhWtVb24lMKuOqmXcqOD5DQfOeo6VXJ52dIVa4TNjVH7zpJ45hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دقایقی قبل یک کشتی در نزدیکی خصب عمان مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69347" target="_blank">📅 10:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69344">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/383c08fc2d.mp4?token=Crgd1BRmho7EvgX7HZaJPi9wXu2g6zm-hGnwmFwS5fGi_iamPeWMdIgG4FxmvXK74MaoSn9CFqbvj8xePHG2R5VFTIolLtRMcNp75SEMXavfIqF_HT7_3TGSEdUd0yxSrOEfX8Bsb-QsmF0_MmgBT9854olqXoLpH34DpSVA-9MdedYRTs9EJc_k6G0SXdMTC3Ab4Vde6CHKMKNHFZNkOFERHwy3ERjDNukpqWDhNVZFC8MMPx0zaKedbx8kKX74MVIOr4zi2226inr5GwpflWbTGi0uatcLWNvzM6SA_GfYVQDdbMLGJCrOfuEO6OnRj3-mXGCLbGKOlm2jdrKdJA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/383c08fc2d.mp4?token=Crgd1BRmho7EvgX7HZaJPi9wXu2g6zm-hGnwmFwS5fGi_iamPeWMdIgG4FxmvXK74MaoSn9CFqbvj8xePHG2R5VFTIolLtRMcNp75SEMXavfIqF_HT7_3TGSEdUd0yxSrOEfX8Bsb-QsmF0_MmgBT9854olqXoLpH34DpSVA-9MdedYRTs9EJc_k6G0SXdMTC3Ab4Vde6CHKMKNHFZNkOFERHwy3ERjDNukpqWDhNVZFC8MMPx0zaKedbx8kKX74MVIOr4zi2226inr5GwpflWbTGi0uatcLWNvzM6SA_GfYVQDdbMLGJCrOfuEO6OnRj3-mXGCLbGKOlm2jdrKdJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
بروزرسانی از اسپانیا:
نزدیک ۵۰ هزار نفر از مراکش و الجزایر فرار کردن و غیرقانونی ریختن اسپانیا!
برای کنترل این مهاجرای غیرقانونی پلیس فرستادن که پلیس هم کتک زدن.
این مهاجرا ریختن توی فروشگاه‌ها دارن غارت میکنن، از مردم دزدی میکنن و...
مثلا از یه مراکشی رندوم میپرسن چرا اومدی؟ میگه توی مراکش رفیقمو به قتل رسوندم، مردم هم باهام بد رفتار میکردن، منم فرار کردم اومدم اسپانیا.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69344" target="_blank">📅 10:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69343">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/7cd4da48cd.mp4?token=ER9UK8crQK59rJiTY13Zb8gWPoxYTpPAbirnuBry5s07usnVRqREE0IBT_zzLWDiQNX3YqBqWWb0c0zbi_6kvFwfIVWauRvHxxBseJXB-nvWjoHTMzsV4yChniFveOeuTG_dViRYZQavp39f2eBTeUCSpGNDIWTU_JrGW1NePZ4AOCD132QrDdJBrtoJLI1TjpdGXJHtXOCaY2KQjInXYnmtqN65CAszzAIfEAZG2X_qmOTLbrLxoHvUcEZ1G0vTLBWVOeSwSEIa7_XHl59dZ7cTK9FyKT7Bp8n9tlrhY5LaHN7FzkNW6efNMYAFyxwcCYglePnSzPzznq6pSgg3XTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/7cd4da48cd.mp4?token=ER9UK8crQK59rJiTY13Zb8gWPoxYTpPAbirnuBry5s07usnVRqREE0IBT_zzLWDiQNX3YqBqWWb0c0zbi_6kvFwfIVWauRvHxxBseJXB-nvWjoHTMzsV4yChniFveOeuTG_dViRYZQavp39f2eBTeUCSpGNDIWTU_JrGW1NePZ4AOCD132QrDdJBrtoJLI1TjpdGXJHtXOCaY2KQjInXYnmtqN65CAszzAIfEAZG2X_qmOTLbrLxoHvUcEZ1G0vTLBWVOeSwSEIa7_XHl59dZ7cTK9FyKT7Bp8n9tlrhY5LaHN7FzkNW6efNMYAFyxwcCYglePnSzPzznq6pSgg3XTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
صحبت‌های عادل فردوسی‌پور درباره ماجرای دست‌بوسی عباس صالحی :
تو عُمرم دستِ مسئولی رو نبوسیدم!
عباس صالحی وارد مسجد شد و کاملاً اتفاقی روی صندلی کنار من نشست. به شوخی بهش گفتم اگه یه روزی فیلتر 360 برداشته بشه، همه این نشستن شما کنار من رو ربط میدن به رفع فیلتر!
همون موقع که داشتیم دست می‌دادیم و روی صندلی جا‌به‌جا می‌شدیم، شب دیدم یه ویدیو وایرال شده و با یه تیتر زشت نوشتن که من دست عباس صالحی رو بوسیدم.
اگه قرار بود دست‌بوس باشم که الان برنامه 90 رو داشتم و 360 رو هم فیلتر نمی‌کردن.
چطور ممکنه من برم تو اون مسجد، بین اون همه آدم، بیام دست عباس صالحی رو ببوسم و برای خودم حاشیه درست کنم؟
من همین چند روز پیش هم گفتم؛ بله‌قربان‌گو نبودم، نیستم و نخواهم بود!
همیشه روی اصول خودم ایستادم و سعی کردم کنار مردم باشم. واقعاً این حجم از هجمه‌ای که به من وارد میشه حیرت‌آوره.
من عاشق کارمم و اینو خودشون هم می‌دونن، ولی نه به هر قیمتی. اگه شرایطش فراهم باشه، تو فوتبال 360 به کارم ادامه میدم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69343" target="_blank">📅 10:04 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
