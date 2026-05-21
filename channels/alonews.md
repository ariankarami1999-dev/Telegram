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
<img src="https://cdn4.telesco.pe/file/NaDwbfPmI2EfXR5CuA6pz9kb3wddb3RksZ7gpIj7a4dYGBm3Ma9tBqYcm_OrtAavKcwfAww8OqdhPlccBb7xxL6P4ygm5fS2F7PAgJIQBnodV9WFxudUBO4yXTFNU1ElUaQzt0kbPsOI2hSRyxhkqKOmfJja9TBCbJnUY_mRu2PBdyYHNPY0X34yNIkSBP8Z2L5drA4nk2IuSSkFw-zzINcdYVLAXMuWp4pC1ikMSklWMfM34tI_8_NlR1dESRd2sDFD2_7Tsx3QUyC4d2bCIkg8kogrgc22QGLc7UXA95Kt9-3i92UMKullQjKqdSiam3M9PC6b0hCCW6OJiWM1QQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 943K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 03:03:07</div>
<hr>

<div class="tg-post" id="msg-121680">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
لبنیات از امروز 20% گرون شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/alonews/121680" target="_blank">📅 01:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121679">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AO2mn9U1ZURPSRU6fEyUBJreOOf7jQtwKhg9IsStcVNj_0U2jI9KToeHk_ok1QOb-OAiDivQ0xkV2ZnZqF1DakRz6RaNc7L7AXiQEfdgXcvb-AZK62ueiD1uLl31ohaGN98ZG8lOFrPYjOnHGokRM1HCzHijaSnJO562robnh_lSsGm7YaHEpmsyTd_yB6iqoO-XH1GWgTi_HhJlo6AQ-PXqPNRAFCGqRaBwP5bOgzC3V9qt6y3yvnNBhZyj-2s4__mWXCwVZ5HzhwJCs_Mw368Ajm-QqtEjVOxxonaTsO0zgmmd5M20qUQ4iMB0q1jj-sx6S4_z0vwao4JGDOzx2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بسته چیپس ساده شده 525 هزار تومن!!!
هر دونه چیپسی که میخورین 3 هزار تومن ناقابل.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/alonews/121679" target="_blank">📅 01:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121678">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/288e58579d.mp4?token=XJG_C-uks9JwV6XHCHuQ0UFg0VpURnbhenKy9vFz6UbZoBuFwGqS7SRHxfyodrlk3DgumP1fnGmNsiJtvH5YLAXxVNZva_xX4DncWeU9nmRkXzSdx3q5iQzC5BbhM7w-oBZ_SvOxikFNegRoW7ulswOTVjZqmpl6SCa5fpefTv8H1DVdQDR2vCdOji3QGvYXXNYjqwSOG8QcVd702VOX-umctHK_XbB5D0QposbXAmMhsT2AlYCFt9z7Nak_RjOhg78wqP16zINPctZXyozOJfu6Q41iT0YYVjrOF-9INeGFUJJ4wbT28WQU84z2IhxBGB1CCDVdqJ09yklDpUZSkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/288e58579d.mp4?token=XJG_C-uks9JwV6XHCHuQ0UFg0VpURnbhenKy9vFz6UbZoBuFwGqS7SRHxfyodrlk3DgumP1fnGmNsiJtvH5YLAXxVNZva_xX4DncWeU9nmRkXzSdx3q5iQzC5BbhM7w-oBZ_SvOxikFNegRoW7ulswOTVjZqmpl6SCa5fpefTv8H1DVdQDR2vCdOji3QGvYXXNYjqwSOG8QcVd702VOX-umctHK_XbB5D0QposbXAmMhsT2AlYCFt9z7Nak_RjOhg78wqP16zINPctZXyozOJfu6Q41iT0YYVjrOF-9INeGFUJJ4wbT28WQU84z2IhxBGB1CCDVdqJ09yklDpUZSkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرمله در صدا و سیما: دلم واستون میسوزه ولی دوستون دارم، اما این‌بار بزارین فراخوان بدن ببینیم کت تن کیه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/121678" target="_blank">📅 01:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121677">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGkotWEIlxR-vy-c5zTOZtDzyp8OdKyRZEADGcIbunsT_FHefXEc9VdJA8SS-OhXDyTHyFQZdoSceg1sziujvgtqrCMPlDLQ4UZbsegeOqxQhh4TCFMUwGd3YQouz_xzjZkmY_n06_VInoIW9b-9kXwierkA7-iKwEkmzregU2VJ3Hb4PBE7HUSkx-3we_mqloGCAcUnQd67o5BswJKIEphoqjYft4EqDJoIe_gPS5946NfoPYQW3wuU6WGpqZDwBGFBo0oQCy2-YSiQ2MG2HkdBBIsqA7ZJOxZqcy8j8tH7_ucG3jFBxbKcA3hyKX9erJoSF6zONrqKAc0olk-AxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۱ خرداد تولد ترامپ هست
🔴
بفرست برا خردادی‌های مودی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/121677" target="_blank">📅 01:16 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121676">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
منابع خبری از شنیده‌شدن صدای انفجارهای مهیب در دیرالزور سوریه خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/121676" target="_blank">📅 01:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121675">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ایسنا: منابع پاکستانی به برخی رسانه های مستقر در اسلام آباد اعلام کردند در صورت به نتیجه رسیدن گفت وگوهای وزیر کشور در تهران، فیلد مارشال عاصم منیر فرمانده ارتش این کشور به تهران سفر خواهد کرد اما
آخرین خبرها تا پنجشنبه شب حاکی از آن است که رایزنی ها بر سر معدود اختلافات هنوز نهایی نشده است.
🔴
منابع پاکستانی اعلام کردند
سفر فرمانده ارتش پاکستان در صورت نهایی شدن چارچوب مورد نظر میان دو طرف انجام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121675" target="_blank">📅 00:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121674">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e48e83426.mp4?token=UNFw2Vt7zcgKRYglyYRFSjGZdk2nHenhDtOwW3Z8F_yO3nQpTeMmV2PhbZlfcvGRXOw-KViFGMnrITn_b_kKiew5kg4QMWXXBlOMrJftDRVa69OdNOY4AQWoN0Vg44Vf3t2SKwMuREybV28wSh9_wb2dUuydM7Z8SFeloC7u6mVxlAd3amL6-0tQ69547BkIa6ZEok8nvJP5ht7T8G2byz6qguauEfw6K0sbjlKKRPAMGlBThZS7bIlte5B1Iq0nbMVxoYjheC-aUDMcDqNab1DCKr0pjYTcIJJp1IDsHKj246uu4HmvLkEBiNGi2usEfnI_6SbLlvs9cGjoaVM9Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e48e83426.mp4?token=UNFw2Vt7zcgKRYglyYRFSjGZdk2nHenhDtOwW3Z8F_yO3nQpTeMmV2PhbZlfcvGRXOw-KViFGMnrITn_b_kKiew5kg4QMWXXBlOMrJftDRVa69OdNOY4AQWoN0Vg44Vf3t2SKwMuREybV28wSh9_wb2dUuydM7Z8SFeloC7u6mVxlAd3amL6-0tQ69547BkIa6ZEok8nvJP5ht7T8G2byz6qguauEfw6K0sbjlKKRPAMGlBThZS7bIlte5B1Iq0nbMVxoYjheC-aUDMcDqNab1DCKr0pjYTcIJJp1IDsHKj246uu4HmvLkEBiNGi2usEfnI_6SbLlvs9cGjoaVM9Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوتی بزرگ در صدا و سیما
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/121674" target="_blank">📅 00:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121673">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf33652fc9.mp4?token=QbIYR2znkqKn9sfcJ0DgUsY30qd9Af-kjNHcLTgEj7_cYYHdbx0N9ARKvxsIq8ra0_tBY3UjQnhXoU_8WP39XgWuFaCiE3hQr7sOVuAMLHQh8_1mu4LWAUCr_Wa6X1qYJHsFaV_TTvjShnUZper4ABs7Z3toawz6bJ-OSnD9PJUwPAU2OEk6XB3V7cvHPVZgd_iTLpsB69k7RTf-xuJ6aAztEC7KK2-sZxydViOw_BSgDzXV3CP9PJKdb28ju7VZ2Wods3U-P-08vOMBRil2we2I8qvp_-BktkWNgsOwFzxeZu4hMfD_qoYrPmCWS8JEZJnyVxfTWrkQA3i00AQ1aTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf33652fc9.mp4?token=QbIYR2znkqKn9sfcJ0DgUsY30qd9Af-kjNHcLTgEj7_cYYHdbx0N9ARKvxsIq8ra0_tBY3UjQnhXoU_8WP39XgWuFaCiE3hQr7sOVuAMLHQh8_1mu4LWAUCr_Wa6X1qYJHsFaV_TTvjShnUZper4ABs7Z3toawz6bJ-OSnD9PJUwPAU2OEk6XB3V7cvHPVZgd_iTLpsB69k7RTf-xuJ6aAztEC7KK2-sZxydViOw_BSgDzXV3CP9PJKdb28ju7VZ2Wods3U-P-08vOMBRil2we2I8qvp_-BktkWNgsOwFzxeZu4hMfD_qoYrPmCWS8JEZJnyVxfTWrkQA3i00AQ1aTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه روسیه ماریا زاخاروا: زلنسکی به احتمال اقدام اجباری علیه ترانس‌نیستریا اشاره کرده است.
🔴
او به کل جهان تهدید می‌کند، نه تنها ساکنان ترانس‌نیستریا بلکه فضای اوراسیا را نیز. او فکر می‌کند که شیطان را از شاخ‌ها گرفته و محکم نگه داشته است.
🔴
او قصد دارد با ترانس‌نیستریا برخورد کند — هرگونه تجاوز به هموطنان ما در ترانس‌نیستریا بلافاصله و به طور مناسب پاسخ داده خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121673" target="_blank">📅 00:46 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121672">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/964a3a806a.mp4?token=FNG6n1YsElJhQdpF89OxMO2EGXgn44aU_Vjaer59lSoo5SKzsd0H5m6gV7YG-_PL8g6y-qk-VzeBgLUD_Ta2_d-tN23xYfNjE3fWToXwNcKBW_-j0N9-prCIg8pSsQmo6c1TC-g_Pwuoz45u1w7O799vA6estleBlwa4qhdgeRae8xWvn0XFBMoTt4Je3BgXWlZBXWapKkWbi6IS8TcSm37ou6stKBPVR15Fz-ZKc4KDQQKs_M5nDdGLUWtbx0-PKssjL8zZKEXhy9GG-iozu-TX7i6ThuBWSV-HuxjnsunDcN5K311DR-6rUaGwv2f50xFVP6nxzy0Ibfi7ycjq5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/964a3a806a.mp4?token=FNG6n1YsElJhQdpF89OxMO2EGXgn44aU_Vjaer59lSoo5SKzsd0H5m6gV7YG-_PL8g6y-qk-VzeBgLUD_Ta2_d-tN23xYfNjE3fWToXwNcKBW_-j0N9-prCIg8pSsQmo6c1TC-g_Pwuoz45u1w7O799vA6estleBlwa4qhdgeRae8xWvn0XFBMoTt4Je3BgXWlZBXWapKkWbi6IS8TcSm37ou6stKBPVR15Fz-ZKc4KDQQKs_M5nDdGLUWtbx0-PKssjL8zZKEXhy9GG-iozu-TX7i6ThuBWSV-HuxjnsunDcN5K311DR-6rUaGwv2f50xFVP6nxzy0Ibfi7ycjq5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون رئیس دفتر کاخ سفید در امور سیاست، استیون میلر: تقسیم سیاسی اصلی در آمریکا امروز بین دیدگاهی از آمریکا به عنوان یک کشور جهان اول و دیدگاهی از آمریکا به عنوان یک کشور جهان سوم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121672" target="_blank">📅 00:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121671">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d5f964b2.mp4?token=YmYbkPLBj5pQMLe_AhdZmKvsHjOkGL-9UdpN0GKVcGBTxOUU5W63de6T4Z9oa0o-jakGi2j1v2qiqsB7jpa-_asG62SZyLjF3TU190sBJVJSgaqHj4TGVBjB8LfIr6DHubUp1huYG7o5s1gU-BfyHul2sP7pTXz6v6aY1tqs37qFG9v1oNCkFWmfGU89y953U5ObAIhOxmcb3mEMxN4CdaW9L8RmoMAVSjW4b98Vu3WEeV29c0UiTXUiH7aMeZmW3aj1Yjmt9hTQkWbot9NgibRKu8uDm4bGWf8XTySUwKGOooSDKrA3hvPdpVq4LnBpoGk1ORbdG1cg_u068lmMeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d5f964b2.mp4?token=YmYbkPLBj5pQMLe_AhdZmKvsHjOkGL-9UdpN0GKVcGBTxOUU5W63de6T4Z9oa0o-jakGi2j1v2qiqsB7jpa-_asG62SZyLjF3TU190sBJVJSgaqHj4TGVBjB8LfIr6DHubUp1huYG7o5s1gU-BfyHul2sP7pTXz6v6aY1tqs37qFG9v1oNCkFWmfGU89y953U5ObAIhOxmcb3mEMxN4CdaW9L8RmoMAVSjW4b98Vu3WEeV29c0UiTXUiH7aMeZmW3aj1Yjmt9hTQkWbot9NgibRKu8uDm4bGWf8XTySUwKGOooSDKrA3hvPdpVq4LnBpoGk1ORbdG1cg_u068lmMeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مخبر : اروپایی‌ها چپو راست برای عبور از تنگه هرمز به ما پیام میدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/121671" target="_blank">📅 00:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121670">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
آسوشیتدپرس: احمد وحیدی، فرمانده سپاه پاسداران، به یکی از چهره‌های اصلی در مذاکرات تبدیل شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/121670" target="_blank">📅 00:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121669">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
نیروهای پشتیبانی سریع تحت حمایت امارات متحده عربی فیلمی منتشر کردند که حمله پهپادی به یک سامانه هیسار-آ ساخت ترکیه که توسط نیروهای مسلح سودان در نزدیکی منطقه راهید النوبا در شمال کردفان عملیاتی شده بود را نشان می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/121669" target="_blank">📅 00:30 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121668">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ku1ReLucV4JNsVNwk_XXqinRHI2QpaUYJfhaXEgfvMVakoY5me9R_9Wgb1C8NHYOAi9xHbumOV84fz-7QW1d5TKXazCjIVRTwvTqfYJXilZM5X8trdnoZfiGxaKg_bhcVbSdMFWs6FEDJkmQD3EzPSfKV_sQQrwLUFhDh1j1NgjZsa68fVZJzN0PVCWZgqbQzdTrAYeClnuC0x9OzxriVntkOWbh_V8BEcRTCMDg8WOjb1DedmQbBYvqaUr2VU9Mz3yf8i6yMDzXFdLJMJlSqwUd8fd5v-0ROazM0BBbSg9c1UXNVUPN9_8b1nzL3k-C4XD4zV2CvPguHsENEbCPDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیواری به افتخار رئیس‌جمهور ترامپ، معاون رئیس‌جمهور جی‌دی ونس، و وزیر امور خارجه مارکو روبیو در کنسولگری جدید آمریکا در نوک، گرینلند نصب شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/121668" target="_blank">📅 00:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121667">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
یک مقام ارشد کاخ سفید به پولیتیکو گفت دو هدف اصلی مذاکرات با ایران، جلوگیری از دستیابی ایران به سلاح هسته‌ای و باز بودن تنگه هرمز برای تردد آزاد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/121667" target="_blank">📅 00:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121666">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1oT_VvKQGTaEq0dbcH1bXaKPuItW2DfVHrdt-Y-OwrsPdKjis0rq4FIGeUmFwXYZEwGDHap22gJ_ieHR8lXPF0EdScw8gMXCOKddKFD25oQJJi7_QBdjyD7oNGrYpJYlVSf_wuqGzVNSSSFq8OKGzol-orahCBJv5ck_arqiXaZbTUcBJ30tBcAlNXhY5buI-ZDH30xcvtWQltXkDWJ48vRv2oGUInjwZqMWNkB1ZppW_CUUAZJ1e5Mie0AaZ1qeUnIigocO498jcOvRxH1Y9zz_Filqa6nr3wsFDrT5Iyg9pjvn9i3ncFcgz26U6keD8ubuacb5rKrLd5NyGdrfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : بعد از اینکه کارول ناوروتسکی تو انتخابات لهستان برد و رئیس‌جمهور شد
🔴
و با توجه به رابطه خوبی که باهاش داریم، آمریکا قراره ۵ هزار نیروی اضافه بفرسته لهستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121666" target="_blank">📅 00:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121665">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlwMA_5hOVksezcqBlW0IGIBNlp36ReSNNiHWtvI0NXiKShRzjsrXBF9mdD2te3KceRJz-rt-J9tKT1RxtrACwyjIfesAwxdtpdFPzqmxC2dsDLZ44qQ4k5iLrQk6ozTCRngtmCquVrW88R65cnrZ73rY2t53NKMwmz1zpqzTuxP9w4QL-jWclXygI9qMBDq5MN_iuS4cMgXGKwpObuA8iRgV6ScozSs4gwY43o6uTcQdlBo-xL79b5sHvkgcOb4KvXrbqOorBfL1LYzjNFd7c0sbCnn0O843uUE2lV2e1WUYCh42bcw20zHKuNANtdVgU3dwMJeexhqez4YsZ0KFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گرینلندی‌ها در نوک با پلاکاردهایی که روی آن نوشته شده بود «بله به ناتو، نه به پدوفیلیا» دیده شدند.
🔴
یکی از این پلاکاردها توسط یک معترض در بیرون کنسولگری جدید آمریکا رها شده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121665" target="_blank">📅 00:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121662">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9214fdfc48.mp4?token=NKmzKUHW6bmephLuaf1OagQAKoNuIADqK-9gPEA9afhE92RHuV_wrSjfOZZFeVgg0_X7Y-1f7IUc996UJ94ycGxA50d5ZhlCfIavujWLyHvkwlXJRJiE1th5E4BxAM01LLn9MsaoYHGGha3G7KrkD4EYiawL2yFp-sxC5QXx3jbst0pTiPSTGqNvNRLJS91SEeQ0cT8u_eKHf7zXfS623erert1gRYAR4aaqBaQZwmvWXgMVqaEIcFwW510ieF_P-KhSNKGHKv5JeGvz6TChGo8zM-56-CwlanwN41VsCwIRZkdnFAWRbiZ9AKm17D2E-sPI0mvuBe512EVnHGT1Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9214fdfc48.mp4?token=NKmzKUHW6bmephLuaf1OagQAKoNuIADqK-9gPEA9afhE92RHuV_wrSjfOZZFeVgg0_X7Y-1f7IUc996UJ94ycGxA50d5ZhlCfIavujWLyHvkwlXJRJiE1th5E4BxAM01LLn9MsaoYHGGha3G7KrkD4EYiawL2yFp-sxC5QXx3jbst0pTiPSTGqNvNRLJS91SEeQ0cT8u_eKHf7zXfS623erert1gRYAR4aaqBaQZwmvWXgMVqaEIcFwW510ieF_P-KhSNKGHKv5JeGvz6TChGo8zM-56-CwlanwN41VsCwIRZkdnFAWRbiZ9AKm17D2E-sPI0mvuBe512EVnHGT1Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گرینلندی‌ها امروز در مراسم افتتاحیه کنسولگری جدید آمریکا در نوک تجمع کردند.
🔴
صدای مردم گرینلند شنیده می‌شود که شعار می‌دهند: «برو خانه، آمریکا.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/121662" target="_blank">📅 00:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121661">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RS9dZMfJbe6UdeqKbqKF0Y98PD537Dj9BG3lXJEhTCbvdMc7PtPPfFB-TU_Cqs9i-6tBmK9Zm_fpBwjdWVMFgMWZzGD5Sp82mvpiGpJ5c10-7eTFBMWxRn26rlYPsESUQ7xxVsRXJSpjW2_zy70j3n2rVrBKHFtaFaVlRwXzSZsderf4NSZl3IQ53YtUTUc5Yce0_VS17CsGYK2FHNXEJkpHk0EgNwF2N1jSsl-cYy4eNa8MSh2EGUKu-VE3Aza7g81lPHGBsLX9s208Aezs1q0e7kQYsRT1LD6TLU1Dna7SPguyG-57w0NQSWrVxSuY56rqVmx9KL7FH44zei7E4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس گزارش اکسیوس، تنش اصلی بر سر صلح میان آمریکا و ایران، مخالفت نتانیاهو با هرگونه توافق است. او خواستار ادامه جنگ و شکست کامل ایران است، در حالی که ترامپ از مذاکره و آتش‌بس ۳۰ روزه حمایت می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/121661" target="_blank">📅 23:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121660">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsG5PkoWGFJt5mKpjJ4cJPj5rFxtWI59ROLA8hNk53LEBQwYL2Tdqp6Mp63XJPmaN8Zux2pVEwm_f8Oxh4dEB7Bm4MbKV-MwBMOdDEI8Vc7Xu43bl_a9EcLXiaNcTNMDxMUWapz3QFVMaIXnMMQzgAOQWI2yiN8yWKmCixDc3TaVL2YVweS20hvh3qt-TToUy0bF8r_tpEBgszE-xoa_ny62doInVJSK-yI7fCUemBZ5WcFpjDaZBEZ6JOcR-ebHCu1a3Hr3My2LfojjYMast44UtC6aHzg0A9LZI8I9dAZvkGkD7MHv7LwpdZ19RAoFAog64YUebOfoTPbhRAK5bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رسمییییییی؛ النصر قهرمان لیگ عربستان شد
کریستیانو رونالدو بعد از 3 سال ، اولین جام خودش رو با النصر به دست آورد
😍
@AloSport</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/121660" target="_blank">📅 23:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121659">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
شبکه CNN: ترامپ در کوبا به دنبال چیزی است که در ایران از دستش رفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/121659" target="_blank">📅 23:44 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121658">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🌟
اشتراک v2ray
🗯
گیگی 150,000 تومان
🔗
لینک ساب برا چک کردن مصرف و حجمتون
🔥
سرعت و کیفیت بالا
✅
پشتیبانی دائم
📱
جهت خرید : @v2safeBot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121658" target="_blank">📅 23:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121657">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzBT-_SHkI9BWqSYoKGvmUKjRXBLhsHEX7v7B2arCi9usaTln6NL9oXoDr8j7vJJJBh8zcrAwe1q863HNVcibjjzKA3ki5tpgR3B3B9_tOvS1nABbrdXdQ5mY9ldhH4gpeaUDMSzQLROaQ_t5-M1I156BOpFkC79qJxJx3YbhGsuJ0xg1TdnJxI79gUhF9COxe1Crv-M3SF5tecYjJjNk2oCg-44EJgUc7h2pStEM48Ps9NrT_rtiIkFwLPBRURbiRQ93QXsbyEjvkTUSk3z6EkrRZZkePHB3Jx6XRu6LGsSw-1cQrg2sOpgq3bO9vQ8192bnVRgvmNriN7KXPWVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
اشتراک v2ray
🗯
گیگی
150,000
تومان
🔗
لینک ساب برا چک کردن مصرف و حجمتون
🔥
سرعت و کیفیت بالا
✅
پشتیبانی دائم
📱
جهت خرید :
@v2safeBot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121657" target="_blank">📅 23:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121656">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
یک منبع ارشد ایرانی به رویترز: شکاف‌ها کاهش یافته اما هنوز به توافق نرسیده‌ایم
🔴
غنی‌سازی اورانیوم و تنگه هرمز از جمله نقاط اختلافی درباره توافق هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121656" target="_blank">📅 23:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121655">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyEshKfwoe1d7aJGrjgKGv8WguDWzjW6ruRYsLuwAs4JNYLEYT57xMyEtSAUVxxisIYLaCWZjECUKaPZWphlupg7Pvn58oDKxJTGPd1RReXRxr0fnj_jDFQXcwgn4eCejosYLF5lieEH1R2slir5NdGpOiNaNtkrv0REaARGfv0Fx-nK5dGWbHlZGqjhs4dRW0RgbacnYHIjjk4YFP1x5z7Inq4MV174iFoPI07vxvpuuLc4-OsDKzKb9y2uT8SXh9hSDeHRzBYg0EpoawnBzSgVZY31wK4qth7cyqcLpHUVUecV_P7rc-UnB5UUsHxsphKUvJr8Wr0Or-wfBitjUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: تعویقِ سفرِ «عاصم منیر»، فرمانده ارتش پاکستان به تهران _پس از انتظارِ ۲۴ ساعته_ نشانه‌ی مهمی‌ست!
🔴
«آمریکا» اصرار دارد «بحث هسته‌ای در شرایطِ فعلی، مذاکره و پرونده آن بسته شود» آنهم با «سختگیری هسته‌ای بر ایران!»
🔴
ولی «ایران» مذاکره در بابِ پرونده هسته‌ای را منوطِ به پروسه‌ی اعتمادسازِ ۳۰ روزه‌ی «پایانِ جنگ» و «رفعِ محاصره دریایی» می‌داند!
🔴
در موضوع «تنگه» هم آمریکای‌ها علی‌رغمِ «پذیرشِ مدیریت ایران بر تنگه»، حاضر به پذیرش موضوعِ «اخذ عوارض از تنگه توسط ایران» نیستند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/121655" target="_blank">📅 23:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121654">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
رئیس ارتش پاکستان، عاصم منیر، سفر خود به تهران را لغو کرده است. انتظار می‌رفت که او پیام‌هایی بین ایالات متحده و ایران رد و بدل کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/121654" target="_blank">📅 23:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121653">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
یک مقام ارشد ایرانی به الجزیره گفت که مذاکره‌کنندگان بسیار به حصول توافق نزدیک شده‌اند و در حال حاضر روی پیش‌نویس متن کار می‌کنند.
🔴
همزمان، منبع دیگری به الجزیره گفت که برای قضاوت درباره دستیابی به یک توافق جدی و نهایی، هنوز خیلی زود است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/121653" target="_blank">📅 23:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121652">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
پزشکیان: سر خم نخواهیم کرد، وزرا و کارشناسان ما شبانه روز سرکارند، بدون حتی یک روز تعطیلی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121652" target="_blank">📅 23:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121651">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
مارکو روبیو: کوبا قادر نخواهد بود که ما را منتظر بگذارد یا زمان بخرد.
🔴
همانطور که در مورد ایران گفتم، ترجیح رئیس‌جمهور ترامپ همیشه توافقی مذاکره‌شده و مسالمت‌آمیز است... با کوبا، احتمال وقوع چنین چیزی زیاد نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121651" target="_blank">📅 23:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121650">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
مارکو روبیو: شما درباره ابولا از من سوال می‌کنید. مهم است، اما ابولا در آفریقا است.
🔴
کوبا ۹۰ مایل از سواحل ما فاصله دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/121650" target="_blank">📅 23:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121649">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
پیت هگستث:با بودجه نظامی ۱.۵ تریلیون دلاری رئیس‌جمهور ترامپ، ما غول خفته را بیدار می‌کنیم و زرادخانه آزادی آمریکا را می‌سازیم — و این کار را به‌طور مسئولانه انجام می‌دهیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/121649" target="_blank">📅 23:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121648">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ناتور پاکستانی: مذاکرات ایران و آمریکا در مسیر درستی پیش می‌رود
🔴
«افنان الله خان» در اظهاراتی با اشاره به اینکه اسلام‌آباد به تلاش خود برای دستیابی تهران و واشنگتن به یک توافق ادامه می‌دهد، تاکید کرد: مذاکرات ایران و آمریکا در مسیر درستی پیش می‌رود.
🔴
به گفته این سناتور پاکستانی در جمع خبرنگاران، مذاکرات میان تهران و اسلام‌آباد و همچنین میان پاکستان و آمریکا ادامه دارد و ما هر کاری که بتوانیم انجام می‌دهیم تا طرف‌ها را پشت میز مذاکره بنشانیم، اختلافات را کاهش دهیم، به توافق برسیم و جنگ را متوقف کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/121648" target="_blank">📅 22:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121647">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
الحدث به نقل از یک منبع دیپلماتیک بلندپایه پاکستانی: فرمانده ارتش پاکستان امشب به تهران سفر نخواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/121647" target="_blank">📅 22:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121646">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⭕️
⭕️
اپلیکیشن‌ها را فقط از Google Play یا App Store نصب کنید.
🔴
فایل‌هایی که در تلگرام، کانال‌ها، گروه‌ها یا از طریق لینک مستقیم دانلود منتشر می‌شوند، اگر از منبع معتبر نباشند می‌توانند خطرناک باشند.
🔴
نصب این فایل‌ها ممکن است باعث شود اطلاعات شخصی شما، رمزها،…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/121646" target="_blank">📅 22:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121645">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnK4tkSuQd4v5saERds8h6eTpSh2Qkc8EmnWePTtNycPAtONASe9Ftj_sErHmGjb9lVjys2IPSKDe9PHrNnCHrSXJcWn3ynqWPr2jIDR-MLMMBKutL3z1UWTFQL5voFUO4Yliv_AAxxTZtE2Xg7pZ5cGhHksWj8dMg39bqVQpQJmivPRf56oCU2UIcrNBcaAdIn67cyXseOwGuLt7cQIYjh7Mz8ayynovGDYj29-nDyuQDZZCQMP5hV6DfR-Q25oiHUtFT14n5wYNOejgyqImo2pliWs6OUYCcXJPrKa-FzgAADE7lhKVdKt4gn7e4jw9DO2x2QKZrge22Xd9RFxwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله‌ی تعداد بالای پهپاد اوکراین به روسیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/121645" target="_blank">📅 22:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121644">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
بهاروند، معاون حقوقی پیشین وزارت خارجه: چین محتاط است و تا از نتیجه کاری مطمئن نباشد قدم برنمی‌دارد؛ فعلاً چنین وضعیتی را نمی‌بینم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121644" target="_blank">📅 22:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121643">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وال‌استریت ژورنال: کویت بر اثر جنگ ایران منزوی شده؛ با بسته شدن تنگه هرمز، صادرات ۲ میلیون بشکه نفتی روزانه این کشور متوقف شده و واردات مایحتاج از مسیر زمینی عربستان، ۶ برابر هزینه حمل دریایی تمام می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/121643" target="_blank">📅 22:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121642">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
یدیعوت آحارونوت: تصاویر ماهواره‌ای نشان می‌دهند که پایگاه رامات دیوید اسرائیل آسیب دیده و احتمالاً به پایگاه نواتیم و پایگاه دیگری متعلق به واحد ۸۲۰۰ و پایگاه‌های دیگر بر اثر حملات موشکی ایران خسارت وارد شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121642" target="_blank">📅 22:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121641">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
رایزنی وزرای خارجه قطر و مصر درباره ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121641" target="_blank">📅 22:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121640">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
رئیس سابق میز ایران در سازمان اطلاعات نظامی اسرائیل: اینکه ترامپ به رغم مخالفت صریح نتانیاهو، با ایران مذاکره می‌کند، نکته‌ای قطعی است
🔴
تا زمانی که رئیس‌جمهور آمریکا باور دارد که توافق قابل دستیابی است، اصلا با نخست‌وزیر اسرائیل همسو نیست
🔴
از دیدگاه نتانیاهو، تقریباً هر توافقی با ایران خطرناک تلقی می‌شود، زیرا آزادی عمل تل‌آویو را محدود خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/121640" target="_blank">📅 22:21 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121639">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNQKfd9VaJpny1qEOZbSUvsEYuHVvfuueUOCA8gPYWD_x-7xQNSlcGikdtZUe8LhsinvdJvQkNoRuH-EbDVi0iXTMnr5cDZxO9YRMzcLjSk7RGlnlooLCoyIZ8talxcJ3phtPQd0myW8E9PBgco7844i-6JBXZ-rf-TbjeOXsR9LxZMouSEXtzfkhVeXT1PAyNHmpWD4Y-1uEiiqSeMzJhbW64RbBdS-h96vi16uP9ziHCV8J8TFkT0fQPAnvxWWl-WtuP4vzOGyWcSJw_J7bbISyhLYXXsEgVXU8-gIpliwqrfjoPpxOQo9PWsC9NPqG9Wu-gh6HlIS2e15sUiPrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/121639" target="_blank">📅 22:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121638">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
فایننشال تایمز: بحران خلیجفارس] احتمالاً تازه از الان آغاز می‌شود
🔴
کشتی‌های که پیش از بسته شدن تنگه هرمز از آن عبور کرده بودند، تاکنون عمدتاً به مقصد رسیده‌اند.
🔴
اما از اواخر ماه فوریه دیگر کشتی‌های حاوی نفت، گاز طبیعی مایع، مشتقات نفتی، اوره، هیدروژن، هلیوم و...  از تنگه عبور نکرده‌اند.
🔴
تا به امروز، کمبودها عمدتاً ذهنی و فرضی بوده‌اند؛ اما با کاهش و تخلیه ذخایر انبارها کمبودها واقعی می‌شوند.
🔴
از این پس، جای خالی محموله‌هایی که حرکت نکردند، به شکلی فزاینده‌ای احساس خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121638" target="_blank">📅 22:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121637">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2B1Q3Ax3VqhJcC4nwxBYZwM1mj6_xd6H6B-GgEZ9VVv5JtHTsgLXMk90A0gE-xMqG8cfeV6v_3P9G0CUhPJHo7hQWxu3NkJvjNVfO6hLZ0Nty-0cm85hDtmqhGnxicv6t_bByfWP2Fb9KCDA6SYVkxdL6oLmeudVJ9r1ELmN96M12kg0iHAFuqFwCDfb6OXabPHgiTttS3XeylYfJt8uv2_rqBdAkKUDK-vT0l-_2ju0K5gpDg241lJ62Clzl-YbQrHkrMZsLfSfE4ETh8qvrjKA1WXLBWzRawa-3vy2WaAEn0XVW6rhV8gqAI3zhbSLy_L-yLCVWexMsrdCPAODA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ امضای یک فرمان اجرایی که شرکت‌های هوش مصنوعی را ملزم به اشتراک‌گذاری مدل‌های پیشرفته خود با دولت فدرال برای بررسی می‌کرد، به تعویق انداخت و با استناد به گزارش‌های وال‌استریت ژورنال، نگرانی‌هایی را مطرح کرد که این اقدام ممکن است در رقابت ایالات متحده با چین در زمینه هوش مصنوعی به کندی منجر شود.
🔴
این فرمان نظارت دولت بر صنعت هوش مصنوعی را گسترش می‌داد، اما ترامپ به خبرنگاران گفت که نمی‌خواهد چیزی را تأیید کند که در مسیر حفظ رهبری ایالات متحده در توسعه هوش مصنوعی «ممانعت ایجاد کند».
🔴
کاخ سفید به مدیران اجرایی فناوری اطلاع داد که مراسم امضا مجدداً زمان‌بندی خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/121637" target="_blank">📅 21:59 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121636">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
واشنگتن‌پست: آمریکا نیمی از ذخیره موشک‌های «تاد» را در جریان جنگ علیه ایران مصرف کرد
🔴
آمریکا برای دفاع از اسرائیل بیش از ۲۰۰ موشک سامانه «تاد» شلیک کرده است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/121636" target="_blank">📅 21:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121635">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
واشنگتن‌پست: آمریکا نیمی از ذخیره موشک‌های «تاد» را در جریان جنگ علیه ایران مصرف کرد
🔴
آمریکا برای دفاع از اسرائیل بیش از ۲۰۰ موشک سامانه «تاد» شلیک کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121635" target="_blank">📅 21:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121634">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivoiPe6NX0ktOMaP74t4iUOeBbozeMQo_LrB4l4Eg91ebteHF5LjBtWyd7tpPUmxP9AuKE5qSHKi_l8VWPBybHMH2YAxF94Bxwfa69eH47NrtADxi5rBUfOrjGB8GhhgevmbAvDHXaKcfw-Wla9_7OIJDA_da1Fr1jcQK0bod5t-M9FNABb1squbzALsHdH53Bgp_GkTURJmdCmWdRO1AIJXHatnkAfzt4CJXMNSPe4EiMGoYCHYgFkWivrN2YfEQSFIG_JHelSn1zcXeR3pU6Z4Q9QJyRjiAFvXS4dzJZIO84DMdlK5Qsu-qtM-xfTyAuRyBQOkk8IaKTTVct-M6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان اطلاعات سپاه: جمع‌بندی نهادهای اطلاعاتی آمریکا این است: «گذشت زمان به نفع ما نیست و برای رهایی از مخمصه چندلایه، ابتکار و تهدید ایران را جدی بگیرید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121634" target="_blank">📅 21:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121633">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
دولت فرانسه معتقد است بحران خاورمیانه طولانی‌تر از آنچه سایر کشورها تصور می‌کنند، ادامه خواهد داشت.
🔴
کمک‌های دولتی فرانسه به گاز برای صنایع ماهیگیری و کشاورزی به مدت سه ماه تمدید شده است. فرانسه ۷۱۰ میلیون یورو کمک عمومی اضافی را برای کاهش اثرات بحران گاز اختصاص داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/121633" target="_blank">📅 21:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121632">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا به الجزیره گفت: ما ۹ نفر را به دلیل حمایت از حزب‌الله و تضعیف حاکمیت لبنان تحریم کرده‌ایم.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/121632" target="_blank">📅 21:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121631">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
دبی با 49 ثانیه قطعی برق در طول یک سال،کمترین میزان قطعی برق در سطح جهان رو ثبت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/121631" target="_blank">📅 21:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121630">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
روسیه: آماده‌ایم به اجرای هرگونه توافق هسته‌ای میان ایران و آمریکا کمک کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/121630" target="_blank">📅 21:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121629">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9dcc1f8a.mp4?token=BV3cfHh8jTj72_XKyAqPjIO_IKBsDr98tKC_RaSCq70Tnyc-DbR1mqfZAlNA2h9ZR6oquVm-dxEtpM6cA6DK4JsZoGBtphLPJoylbalo82DR6SmOD_GvsROgu7sAbah75KxXGElJ5TzCaduh09AxtOaGnzpX3sfUI98L7aRaz3EuYPGQowd37EU1q13Qio8uUasSzbBP-v6C-WqImPcto-KPDwAkG9xAQHL1zhxyNEYWFqdmJznc-bmsbFRDenF30nJv43qU5hnaH6DT8sz5z014-tvq9fGtbr6jZiA2YXhnLOhX5GpoVyHBkCXj01GqMevvzn-vxne1uc_KiBQ9nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9dcc1f8a.mp4?token=BV3cfHh8jTj72_XKyAqPjIO_IKBsDr98tKC_RaSCq70Tnyc-DbR1mqfZAlNA2h9ZR6oquVm-dxEtpM6cA6DK4JsZoGBtphLPJoylbalo82DR6SmOD_GvsROgu7sAbah75KxXGElJ5TzCaduh09AxtOaGnzpX3sfUI98L7aRaz3EuYPGQowd37EU1q13Qio8uUasSzbBP-v6C-WqImPcto-KPDwAkG9xAQHL1zhxyNEYWFqdmJznc-bmsbFRDenF30nJv43qU5hnaH6DT8sz5z014-tvq9fGtbr6jZiA2YXhnLOhX5GpoVyHBkCXj01GqMevvzn-vxne1uc_KiBQ9nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی مجلس: احتمال عبور از آتش بس از سوی ایران وجود دارد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/121629" target="_blank">📅 21:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121628">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: در این مرحله تمرکز مذاکرات بر خاتمه جنگ در همه جبهه‌ها به شمول لبنان است و ادعاهایی که درباره مباحث هسته‌ای، از جمله موضوع مواد غنی شده یا بحث غنی‌سازی، در رسانه‌ها مطرح شده، صرفا گمانه‌زنی رسانه‌ای بوده و فاقد اعتبار است.
🔴
هیچ‌یک از گمانه‌زنی‌هایی که در روزهای اخیر راجع به ابعاد مختلف مذاکرات مطرح شده قابل تایید نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/121628" target="_blank">📅 21:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121627">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
دیجیتاتو: محمدرضا فرزانگان، اقتصاددان حوزه خاورمیانه در دانشگاه فیلیپس ماربورگ آلمان، گفته است حدود ۱۰ میلیون شغل در ایران به‌طور مستقیم یا غیرمستقیم به اقتصاد دیجیتال وابسته هستند.
🔴
او به وال‌استریت ژورنال گفته محدودیت گسترده اینترنت باعث کاهش بهره‌وری، تضعیف اعتماد کسب‌وکارها و افزایش نابرابری می‌شود؛ زیرا در چنین شرایطی تنها کاربران ثروتمندتر یا افرادی که به ارتباطات بهتر دسترسی دارند، می‌توانند اتصال پایدار و قابل اتکا داشته باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/121627" target="_blank">📅 21:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121626">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ادعاهای هسته‌ای در مذاکرات فاقد اعتبار است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/121626" target="_blank">📅 20:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121625">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
فیگارو: دولت فرانسه معتقد است که بحران موجود در خاورمیانه طولانی‌تر از آن چیزی خواهد بود که سایر کشورها تصور می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/121625" target="_blank">📅 20:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121624">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا به الجزیره گفت: ما ۹ نفر را به دلیل حمایت از حزب‌الله و تضعیف حاکمیت لبنان تحریم کرده‌ایم.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/121624" target="_blank">📅 20:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121623">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا به الجزیره گفت: ما ۹ نفر را به دلیل حمایت از حزب‌الله و تضعیف حاکمیت لبنان تحریم کرده‌ایم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/121623" target="_blank">📅 20:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121622">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
خبرنگار: آیا در مراسم عروسی پسرتان شرکت می‌کنید؟
🔴
ترامپ: او دوست دارد بروم. سعی می‌کنم. بهش گفتم این زمان‌بندی برای من خوب نیست. من با چیزی به نام ایران و مسائل دیگر سر و کار دارم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/121622" target="_blank">📅 20:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121621">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUBuAFkDTeYvYvwFUGXUvE8yjZ9hWaPreNSutci-8wh4gXCMaUHHU0kkCDKRkHd_kXPjGvNGElr15BjLmpRBzXhXggrqadm0uSlH1eA906GuzEi5snwmUvpukPJQPnNwkiCaznUkN1V0YFFBsf6p1KWo5JUIPHzJRr4si6ZREMFQCtz-HyKFgoLTwhYk6jAA08yJ0CPXpx8Rt_sysZPQqj21PVBmxcLSY9eu2dKQ1TkaarAIqx8rAktk7wVcSxpLsixhqO0UQfBWdUQQsO6Mm70Wrr6pv9G-J0NRs-PCjO-vbBIXJAgDitmDyVCRM9LC46UbJOPRmF-0fYQROPjkgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پوتین: سلاح هسته‌ای آخرین گزینه تضمین امنیت ملی ماست
!
🔴
رؤسای جمهور روسیه و بلاروس طی یک ارتباط ویدئوکنفرانسی، فرمان آغاز نخستین رزمایش مشترک نیروهای هسته‌ای استراتژیک و تاکتیکی دو کشور را صادر کردند. ولادیمیر پوتین در این مراسم، سه‌گانه هسته‌ای را ضامن قابل اعتماد حاکمیت «دولت متحد» دانست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/121621" target="_blank">📅 20:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121620">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
عضو اتاق بازرگانی: همه مسیرها به سمت اتصال مجدد اینترنت بین‌الملل است
🔴
مسعودی، رئیس کمیسیون فاوای اتاق بازرگانی ایران: در تمامی رایزنی‌ها و مذاکرات اخیر با نهادهای مسئول، روند تصمیم‌گیری‌ها به سمت اتصال مجدد اینترنت بین‌الملل برای عموم مردم پیش رفته و تاکنون بحثی درباره اینترنت طبقاتی مطرح نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/121620" target="_blank">📅 20:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121619">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه فرانسه اعلام کرد که این کشور هرگونه نقش احتمالی ناتو در تنگه هرمز را رد و تاکید می‌کند که ماموریت این ائتلاف به خاورمیانه گسترش نمی‌یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/121619" target="_blank">📅 20:21 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121618">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
العربیه: پیش‌نویس نهایی توافق‌نامه ایالات متحده و ایران با میانجیگری پاکستان دست یافته است که قرار است ظرف چند ساعت آینده اعلام شود.
🔴
۱. این پیش‌نویس شامل آتش‌بس فوری و جامع در تمامی جبهه‌ها است.
🔴
۲. طرفین متعهد می‌شوند به‌صورت متقابل از هدف قرار دادن زیرساخت‌ها خودداری کنند.
🔴
۳. آزادی کشتیرانی در خلیج فارس و تنگه هرمز تحت یک سازوکار نظارتی مشترک تضمین می‌شود.
🔴
۴. تحریم‌ها در برابر پایبندی ایران به مفاد توافق، به‌تدریج لغو خواهد شد.
🔴
۵. مذاکرات درباره مسائل معوقه حداکثر ظرف هفت روز آغاز می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121618" target="_blank">📅 20:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121617">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ
:
دولت بایدن «شرکت‌ها را مجبور به استفاده از مبردهای خاص با هزینه بالا کرد که به طور چشمگیری قیمت حمل و نقل و ذخیره‌سازی کالاهای مختلف را افزایش داد... آمریکایی‌ها با قیمت‌های بالاتر مواد غذایی و دسترسی کمتر به تجهیزات پزشکی حیاتی مواجه شدند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/121617" target="_blank">📅 20:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121616">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/221f457652.mp4?token=eH0pqY-xshOQJtCfZzKzEAQc7VV9ww8gTs-PgguzQ1NrO079a0hLuADAGYp4LoCQ25geDjsXnRQ8xrpAvZrLytXiGi-QpWjMt7A3HTbLsmBHFb6QuWPh3G9H31wycLin5DF78mfsq1kEanQwXObTq93bMX25zHZvSSd7XNuyDaMQgBncldbmPFy_otS7PkGw6Zn9hdiC8uhpQhUZo3npip2jc_hexCGduEEwNNI86MUnzm9m5uKxJpSo3q9ODWGOomXqwYsFyClXbPIPh0FAhb0EfoWqUQwXVlU8Dcbvlfvb_Y-PXqDeyy2uqquK4ququzvVCqAzJk8B5gSvdpvngQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/221f457652.mp4?token=eH0pqY-xshOQJtCfZzKzEAQc7VV9ww8gTs-PgguzQ1NrO079a0hLuADAGYp4LoCQ25geDjsXnRQ8xrpAvZrLytXiGi-QpWjMt7A3HTbLsmBHFb6QuWPh3G9H31wycLin5DF78mfsq1kEanQwXObTq93bMX25zHZvSSd7XNuyDaMQgBncldbmPFy_otS7PkGw6Zn9hdiC8uhpQhUZo3npip2jc_hexCGduEEwNNI86MUnzm9m5uKxJpSo3q9ODWGOomXqwYsFyClXbPIPh0FAhb0EfoWqUQwXVlU8Dcbvlfvb_Y-PXqDeyy2uqquK4ququzvVCqAzJk8B5gSvdpvngQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : فکر میکنم اگه دموکرات‌ها کنترل کنگره رو بگیرن و حتی فرض کنیم کل کشور رو بگیرن این کشور تمومه
🔴
این آدما مریضن سندروم ترامپ دارن ولی واقعیت اینه که سیاست‌هاشون بده سیاست‌های وحشتناکی دارن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121616" target="_blank">📅 20:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121615">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
بلومبرگ: ایران در حال رایزنی با عمان درباره نحوه راه‌اندازی نوعی سیستم عوارض دائمی است که کنترل خود بر ترافیک دریایی از طریق تنگه هرمز را رسمیت ببخشد.
🔴
محمدامین‌نژاد، سفیر ایران در فرانسه، روز چهارشنبه در مصاحبه با بلومبرگ در پاریس گفت «ایران و عمان باید تمامی منابع خود را هم برای ارائه خدمات امنیتی و هم برای مدیریت ناوبری به مناسب‌ترین شکل ممکن به کار گیرند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/121615" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121614">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vodsltivP3-HsbF_VUQM3Lb1NE5WkiVQkxyWyBPIQEiYK4eJdJqVhCYSgbt7GY2LWV7-qg4emKB5VlGC8x-j2tAvASmqqmvK5ND0JDn4yOLF4KtAE7lyfabjXwx1n2D7wj7IKpToD4loESOqeOWXBVMu8QbmvITjdG9VwDmoILogRsU42B9H1xk1_VS5__BgROoymcTXk1Oe4bL-H8-f5-uICr7IQxD-TKzEZHXkS8RT9qMp3xIIvPPy6w8iS2yBK55-vLt5nR23IxlO6ygYthTm90Gt6YAA2vClKLs8YksKFOunZqEi7qYgX0hdzFMhNosNLdpm7ycOQy-dFsk5gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت انگلیسی رئیس کمیسیون امنیت ملی در پاسخ به ترامپ: دوران اعتماد به «دیپلماسی» آمریکا به پایان رسیده و اکنون
ما برای هر سناریویی آماده‌ایم.
🔴
هرچند آمریکایی‌ها برای آنچه در انتظارشان است، آماده نیستند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/121614" target="_blank">📅 20:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121613">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnskMCuShN9306cu7Aw3iHGTGytUfU7GNW8gREwg2R6Z4HTnAevq8DFRyREOlM1uuknS0nIBujou2VF78grabs0G7WqnBivhuNCPprOMYs5ogtmSICMl5bqR0P9wsZ-gPGfbFykQXwiuY1sRU58DLipoFizkUFPWAyaO6xy3ZfwUav-hWB0z_CQnnfPDxksuf97Xz7j5vElXUDT-horNzA-T7Auuq9p4j-CfzP7VbSCpPEyj-IGFxTECALxzfB_BZCB4Wqp4fgzvLzcv5v56aEgEGuRdFkvoy5cUcEdo1cinXRyxO8qr7Y4fXSmt2S3KixT3ajWkEXkKB7VwF2rKwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال
:
دولت ترامپ به بزرگترین خریدار نقدی کشتی در جهان برای اوراق، مجوز خرید چهار کشتی تحت تحریم به دلیل حمل محموله‌های ایرانی را اعطا کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/121613" target="_blank">📅 20:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121612">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ترامپ : قیمت بنزین در آمریکا بعد از پایان جنگ ایران تا حدود 1.85 دلار سقوط می‌کنه
🔴
این وضعیت خیلی زود تموم میشه و وقتی تموم بشه قیمت بنزین حتی از قبل هم پایین‌تر میاد
🔴
چند ماه پیش تو آیووا بنزین 1.85 دلار بود و دوباره به همون عددها میرسیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/121612" target="_blank">📅 19:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121611">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ترامپ: ما عوارض‌گیری در تنگه هرمز را قبول نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/121611" target="_blank">📅 19:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121610">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ: ما تنگه هرمز را از طریق محاصره‌ای که یک دیوار فولادی تشکیل می‌دهد، کاملاً کنترل می‌کنیم و ۷۵ درصد از قابلیت‌های موشکی ایران را از بین برده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/121610" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121609">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ: ما تضمین خواهیم کرد که ایران به سلاح هسته‌ای دست پیدا نکند و می‌خواهیم تنگه هرمز بدون تحمیل هزینه باز شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/121609" target="_blank">📅 19:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121608">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ: نیروی دریایی ایالات متحده کار خود را به خوبی انجام می‌دهد؛ به دلیل محاصره دریایی، هیچ کشتی‌ای به ایران وارد نمی‌شود و از آن خارج نمی‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/121608" target="_blank">📅 19:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121607">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ: اورانیوم بسیار غنی شده به دست می آوریم، آن را نابود می کنیم و نمی توانیم اجازه دهیم در ایران بماند
🔴
برآوردها نشان می دهد که ایران روزانه ۵۰۰ میلیون دلار ضرر می کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/121607" target="_blank">📅 19:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121606">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ: درگیری با ایران خیلی زود پایان خواهد یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/121606" target="_blank">📅 19:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121605">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f431a2f476.mp4?token=uFj9jHm5MxWIUocpJj8CAtXPQ7TRC8CU07PZDmmhppkAQEvtS7WfVuM4x-waiUeEwFAUEoffjtHSdUxvdtSzIm1lK66yfOaSuV4RJSB1KSSwwpxwxgIosL_njvtIPVtkBUo77ujGw8XhA3lOIl0UYbvdm-FwzIJQne3g1fGayNg--fVIv2NlvTmelKhqnxLODzCqg_rmFrcCutlI9fNchdrKPX6PqAJsAJXv5tu9-28YdMn2EwL2OzccnI6lD0IQqfpnQcE4QudhdSnNCd35QwIixrI0vRdrkvgZCTBfvUlBCjgOSTEexNNvvg_f77EK3J37tX67Vxs0A-X79KmJxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f431a2f476.mp4?token=uFj9jHm5MxWIUocpJj8CAtXPQ7TRC8CU07PZDmmhppkAQEvtS7WfVuM4x-waiUeEwFAUEoffjtHSdUxvdtSzIm1lK66yfOaSuV4RJSB1KSSwwpxwxgIosL_njvtIPVtkBUo77ujGw8XhA3lOIl0UYbvdm-FwzIJQne3g1fGayNg--fVIv2NlvTmelKhqnxLODzCqg_rmFrcCutlI9fNchdrKPX6PqAJsAJXv5tu9-28YdMn2EwL2OzccnI6lD0IQqfpnQcE4QudhdSnNCd35QwIixrI0vRdrkvgZCTBfvUlBCjgOSTEexNNvvg_f77EK3J37tX67Vxs0A-X79KmJxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما کنترل کامل تنگه هرمز را در دست داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/121605" target="_blank">📅 19:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121604">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ: من می‌خواهم به کوبایی‌ها بر اساس اصول انسانی کمک کنم
🔴
در حال مذاکره درباره ایران هستیم و به هر وسیله ای که باشد به هدف خود خواهیم رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/121604" target="_blank">📅 19:44 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121603">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c6a2a9ae6.mp4?token=WD5oo_5SXweYx8y-EuJwY2bMuqe_IEdSR9hs7zomGoONYs5RXNfoMBpX-e9ab6ezBG1Csv6L1XkqIjaVAKUkINDEkXhqahPXO-g7nhNvFzRZqgas_2dTwjb7aEfOKuVxwVBX5JDs8yZOOgeaRmZ_RxNurdeuAcLo8fXhwmRAJNBDfaC_eeqxDeJRm-vTJXfS4uZo3-Pd2a0g6OyBN-22UGWWU7oil-x3lXUngLPKzFGdeCMtb86ab_-2xIFLhlSdXYKq3p_R0eUJEYYq7s0DZUXNZriKxU-yFpWhwKwF7BlD44Y0ijO1ZLw8ELtgBmUICQS3h10KBOuquG4JfdYJEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c6a2a9ae6.mp4?token=WD5oo_5SXweYx8y-EuJwY2bMuqe_IEdSR9hs7zomGoONYs5RXNfoMBpX-e9ab6ezBG1Csv6L1XkqIjaVAKUkINDEkXhqahPXO-g7nhNvFzRZqgas_2dTwjb7aEfOKuVxwVBX5JDs8yZOOgeaRmZ_RxNurdeuAcLo8fXhwmRAJNBDfaC_eeqxDeJRm-vTJXfS4uZo3-Pd2a0g6OyBN-22UGWWU7oil-x3lXUngLPKzFGdeCMtb86ab_-2xIFLhlSdXYKq3p_R0eUJEYYq7s0DZUXNZriKxU-yFpWhwKwF7BlD44Y0ijO1ZLw8ELtgBmUICQS3h10KBOuquG4JfdYJEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: می‌خواهم به کوبایی‌ها بر اساس ملاحظات بشردوستانه کمک کنم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/121603" target="_blank">📅 19:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121602">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/474b633de8.mp4?token=NuYEhhhL03McXOdISM9cI4HL5hjDOUmrn5MsFbPjE6hLz8Bl3JmpaQ-6WE_qKYp8yqqgCjXHAScxoa_cRvZU5oO3MX_viYxGrzZbpx9E5AfJV0oPSK_RBedjJ8sJ-APN724U0WUYvBv8Z2LaiYwzzQW0w-3OZ3EbEXWwvOGqG7KQoRHFQs9K4Ek9V_Uyrd_MZ9lj0bkjgjSaBbK43HqjkxuPkxCRcF9fEKgdWNJFgaYKt1R6S4xNcfiiR38HNCZAL_NcTvq4beIuOqxjqqmGO4fnaDwIneMaCm9ZrVzuwDSGND3i0t8zSYkhGWQtvGVGTt5AO1sUR9m5_uGzWt6yLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/474b633de8.mp4?token=NuYEhhhL03McXOdISM9cI4HL5hjDOUmrn5MsFbPjE6hLz8Bl3JmpaQ-6WE_qKYp8yqqgCjXHAScxoa_cRvZU5oO3MX_viYxGrzZbpx9E5AfJV0oPSK_RBedjJ8sJ-APN724U0WUYvBv8Z2LaiYwzzQW0w-3OZ3EbEXWwvOGqG7KQoRHFQs9K4Ek9V_Uyrd_MZ9lj0bkjgjSaBbK43HqjkxuPkxCRcF9fEKgdWNJFgaYKt1R6S4xNcfiiR38HNCZAL_NcTvq4beIuOqxjqqmGO4fnaDwIneMaCm9ZrVzuwDSGND3i0t8zSYkhGWQtvGVGTt5AO1sUR9m5_uGzWt6yLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا کنترل سنا را از دست داده‌اید، جمهوری‌خواهان سنا؟
🔴
ترامپ: نمی‌دانم. واقعاً نمی‌دانم. من فقط کار درست را انجام می‌دهم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/121602" target="_blank">📅 19:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121601">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
جمعی از دانش‌آموزان چهارمحال و بختیاری با تجمع در برابر استانداری، لغو امتحانات حضوری را خواستار شدند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/121601" target="_blank">📅 19:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121598">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jOSfnj8Ou1ietzyF-MIfZSBpcRkTbgpBI0-U-1269hfPfC0i4pSd1n3uDlLgtJOR735tYI_dfKpVgucUvNHH2hXThM3HeNvRiGhLY4trXVgUbPgmF5Y30-E3KEWjeFFXS9fblxezONFHtEgLIxWg6m-u5CcZ6eQF1nmbzaoxD5z0aEZKD2-S2oSKjFXL2f5pggGgrjTcn_Ms0v9GKBKCLmorSXGG1ytMYekMd_I4w9O2IA6sEkfzvn5FmGnTmFl-nWg1x2LCgE1egNgkzWJ3XPTa-xMfQXc2kOWRKBr2p10P-QScxfIUJfGyQDhiXQl5bQbwmH3EgJtej6so1QJWrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NswX0D5UB9euEuNAIkZQS7xCHLxa4OrU4zXFNjq-S_GdpBNPvg-uaREx1FwVtviSyTvw0p544zJS3lCC_wyFQyLQakjYGhF5JxBuvGRG1YZdSlXHR-JgkQL9br5p82FWCSv39mlrP4V3ShKhpD4YZ2eKDu_yxOn1hKiOTUCTbgX54WtYlknX5xI7vkwKkNtaIEQ1GnxZcm6TzKmtzLWc1oHyEEPZq46u2shUH_G2oPldXIo7mQzOvAjnVo3ZT2A1awLR2n6kLwHKPE0fWrfrZUXOIfJuC8RobHhvD7MI1hJIkouGzQlsH9KIcYKRlDUNYksJtiqMX8VWGal0X8vsoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jc65LVuiDqJpBJ3qc35rGhG4P_c2yqCDdOS2J92OipsRr0yck5LYbBz2XhqoFYCfWr0BLOZu7unftsTk4WvSofTf2LxJGk07j1L3ctzT5pPq6Q6L3Mv8101aiuHLrDhWXV8mbErS2WDi0sYJQ2Ry2mkTPB1gOaYYPTxhlDwuLY4VqgINlrHuF7XqXJD6IMlPsnivaWtW7_i-2uoq9rS1JZegk5cGxLxdb6nvkm3Z3w3rhj2zMeZH9Hx12nhA2lF_-svDnv1o0-0eMtvvD4tCYZkPF8rXdOqwX_MkKAKqGMR4Ug0mz1OUjWkcvVIPhonbbQoa7zQfR3C-i_YMR8MWhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله‌های ارتش اسرائیل به جنوب لبنان مواضع حزب‌الله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/121598" target="_blank">📅 19:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121597">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
استاندار خوزستان از صدور مجوز نهایی برای عملیاتی شدن مجدد فرودگاه بین‌المللی اهواز و آغاز پروازها به مقاصد مختلف از هفته آینده خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/121597" target="_blank">📅 19:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121596">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
استاندار خوزستان از صدور مجوز نهایی برای عملیاتی شدن مجدد فرودگاه بین‌المللی اهواز و آغاز پروازها به مقاصد مختلف از هفته آینده خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/121596" target="_blank">📅 19:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121595">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745e6e3332.mp4?token=pdOyOgqR_VQrC0yTPoqnJf09zV4fKz26nA3DGGf3qulMiCG3MRUvC3pxkn82JhAFkFnu-gF4YpB-dSeaJE74dHKyrfkXJ_vmZ14GNn6XFqH6l9DPfwxrBNGvXYswusrasV6HkjTHvuMzSs1w7ct0C4X62NXmkS5Uf_uRnew_7JsZIBk-rh4cZ2pDrcERnXr6hAQ9Rs2E1eLBKWfoEdTc3qinttIAjUPV2p8Mpm66M8MO0kkStFAgIGprBUfVCMSawbM5NYE4WfsbS0snipSHOZaXgY-lyjyC_ejTo9Lf0q3hxRNFQRHSrBu_MAEJau82GpK4y85XhO4aOPg34Ndb_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745e6e3332.mp4?token=pdOyOgqR_VQrC0yTPoqnJf09zV4fKz26nA3DGGf3qulMiCG3MRUvC3pxkn82JhAFkFnu-gF4YpB-dSeaJE74dHKyrfkXJ_vmZ14GNn6XFqH6l9DPfwxrBNGvXYswusrasV6HkjTHvuMzSs1w7ct0C4X62NXmkS5Uf_uRnew_7JsZIBk-rh4cZ2pDrcERnXr6hAQ9Rs2E1eLBKWfoEdTc3qinttIAjUPV2p8Mpm66M8MO0kkStFAgIGprBUfVCMSawbM5NYE4WfsbS0snipSHOZaXgY-lyjyC_ejTo9Lf0q3hxRNFQRHSrBu_MAEJau82GpK4y85XhO4aOPg34Ndb_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو : کوبا نمی‌تونه ما رو معطل خودش کنه یا وقت بخره همونطور که درباره ایران گفتم
🔴
ترجیح رئیس‌جمهور همیشه رسیدن به توافق از راه مذاکره و صلحه درباره کوبا احتمال این اتفاق زیاد نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121595" target="_blank">📅 19:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121594">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e2afb4479.mp4?token=Veajmx9OI1LjD0lA1A0ZYWeZpGbZoN2JBCEC94j9vVkGT6nkNCh_SoaOCue4YkHaqALMnf_7NaUrjFDcytA88RLbJUzX0CA8Wk4iLohuhkzKf8naqorB2F3N88ipxu0YG8X097kFzxUnlmo1QfQWMosVXAoRtAskP6Z0I9l6AjwY0_7ettbhIFLWEYjGnbQcIVr4XR0yXCuWfTWMfAlAIoWebweF8Ki_H3qsYwIR6v4dck2x0BQGdu9s7aYAF_sWQes0ajF9OUNqnUqkonEqYGsBz0K4LpM9ye7FQwqOnImxI77IZr-gMo_IUWxN0ieaj2mPregF64QT9BEjPmAgjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e2afb4479.mp4?token=Veajmx9OI1LjD0lA1A0ZYWeZpGbZoN2JBCEC94j9vVkGT6nkNCh_SoaOCue4YkHaqALMnf_7NaUrjFDcytA88RLbJUzX0CA8Wk4iLohuhkzKf8naqorB2F3N88ipxu0YG8X097kFzxUnlmo1QfQWMosVXAoRtAskP6Z0I9l6AjwY0_7ettbhIFLWEYjGnbQcIVr4XR0yXCuWfTWMfAlAIoWebweF8Ki_H3qsYwIR6v4dck2x0BQGdu9s7aYAF_sWQes0ajF9OUNqnUqkonEqYGsBz0K4LpM9ye7FQwqOnImxI77IZr-gMo_IUWxN0ieaj2mPregF64QT9BEjPmAgjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : آیا دولت آمریکا هنوز معتقده متحدای ناتو ترسو هستن؟
🔴
مارکو روبیو : رئیس‌جمهور خیلی ناامید شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/121594" target="_blank">📅 19:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121593">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
وزیر امور خارجه آمریکا: در صورت عدم دستیابی به توافق خوب با ایران، وارد جزئیات گزینه‌های پیش روی رئیس جمهور ترامپ نمی‌شوم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/121593" target="_blank">📅 18:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121592">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
روبیو: ببینیم آیا می‌توانیم با ایران به توافق برسیم، نشانه‌های خوبی وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/121592" target="_blank">📅 18:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121591">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وزیر خارجه آمریکا: مقامات پاکستانی امروز به تهران سفر خواهند کرد؛ نشانه‌های مثبتی وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121591" target="_blank">📅 18:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121590">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وزیر امور خارجه آمریکا: ما در مذاکرات با ایران پیشرفت‌هایی داشته‌ایم
🔴
گزینه ترجیحی رئیس جمهور ترامپ دستیابی به توافق مسالمت آمیز با ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/121590" target="_blank">📅 18:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121589">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
روبیو: سیستم عوارض‌گیری در تنگه هرمز، توافق دیپلماتیک را غیرممکن می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121589" target="_blank">📅 18:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121588">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سی‌ان‌ان: یک منبع گفت که در سطوح بالای دولت اسرائیل، تمایل شدیدی برای اقدام نظامی مجدد وجود دارد و کلافگی فزاینده‌ای از اینکه ترامپ همچنان به آنچه که آنها وقت‌کشی دیپلماتیک ایران می‌گویند اجازه می‌دهد، دیده میشود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/121588" target="_blank">📅 18:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121587">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
وزیر دارایی لبنان: خسارت جنگ به این کشور تا ۲۰ میلیارد دلار تخمین زده می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/121587" target="_blank">📅 18:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121586">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpm-9OYzXfPeMj9ZyFxrfp02h8eb_8oXxBJ2Yvd9G-UG-Bzkd0N2zRK06F_Dv4nSp-njM79v_Qd1CmntSvNDabI-SA5OwSyflKAq3OyYr83Qq5KyFqeSjy6ppmcs1q7y-8nzHXEZZUpdINQGNzZgC3duw7ZYVizHYHhJ2V1JhF1q2hjZ59P8pfujuffns82aODUQLAOZgFCVC1D70vo20jXqMOtPl4U9Bx2l6ueuGGuLVxGKjtNkhMt1yj7fMnUDNJxfPHZVDCoKAYgOu3gTSSLkrc0n6lCEjjaqTx4dlHJ8zLAqhbvCwtLEv7x2N178JfLvIkKGs0ySAmDWjTwPcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر جنگ آمریکا، پیت هگست : "آماده و مسلح"
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/121586" target="_blank">📅 18:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121585">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcbJOV5WU6Z3fKlCDgIyexR6ekMcQHpMNRUPzy70_IliwCqB8QnBfDyoBJVaFi-bxD8w3JlDf6DKub9w5rbuP-wriPfedP6SdcmCq6d_YUFfH6gihMeKX2mzs35c_J8CWUS4m5n4QsrtW4FQFsufjDr4EFtZyC9bcyfOWHNb9wglawZdChJtDRIKXMgVKR2MhbU5Mljx7OHCoWpj29dEaGHYqRUKqMdFD2Is632HQYR97-mFR-9MC617bSpbWJArFlEVZnxe7t385tc0fDwK1g7TVYZjHl0Z44X_-WRetGzTu-MZGjdbDJx8helPvEDzuNp3rKrPZU6YyzEbxdHDZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی سازمان آتش‌نشانی تهران: ساعت ۱۵ امروز، یک مورد آتش‌سوزی در انبار کالا واقع در خیابان ملت، اعلام شد.
🔴
با حضور آتش‌نشانان، عملیات اطفا آغاز شد و خوشبختانه آتش تحت کنترل قرار گرفت و از گسترش بیشتر به اطراف جلوگیری شد.
🔴
این حادثه هیچ گونه مصدوم یا تلفات جانی نداشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/121585" target="_blank">📅 18:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121584">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وزیر موقت نیروی دریایی ایالات متحده: ناوهای هواپیمابر لینکلن و بوش به همراه گروه طرابلس برای محافظت از ناوبری در دریای عرب هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/121584" target="_blank">📅 18:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121583">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
روابط عمومی نیروی دریایی سپاه: طی شبانه روز گذشته ۳۱ فروند کشتی با هماهنگی نیروی دریایی سپاه از تنگه هرمز عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/121583" target="_blank">📅 18:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121582">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
خبرگزاری اینترفکس: پوتین و شی جین‌پینگ درباره نتیجه سفر ترامپ به چین گفتگو کردند
🔴
سران روسیه و چین درباره ایران بحث و تبادل نظر کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/121582" target="_blank">📅 18:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121581">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
انگلیس کاردار اسرائیل را احضار کرد
🔴
دلیل؛ رفتار اهانت آمیز وزیر امنیت ملی اسرائیل با بازداشت‌شدگان ناوگان جهانی صمود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/121581" target="_blank">📅 18:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121580">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وزارت دفاع روسیه فیلمی منتشر کرده که نیروهای هسته‌ای این کشور در حال انجام تمرینات اخیر را نشان می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/121580" target="_blank">📅 18:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121579">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df359f5799.mp4?token=WnjxgHnFlIaEUR6igibSUHHsvhJH94dOROpEaaIlPax5NfE-mvntUVo7HeiLwO5DntwjeRCiPZX-LXx3Qmk-6qpVeEiFgokz7bbWlTQBqtp2Io5mEmNurD5-l4OoPMzP1nK8AsYSxhbbUyC-ozp8DtxFjB_sjBoHeibzAjWyXmFnvt0BAFWwHi4yxiAVcO3q21RIeL9BtwSF-y5hVskQ_dRlZNDbTOFX9V00q1pQdI9yovkdQgbEvoH8LLKlwTE-e7_mGVM4IyI9k3RXyj-FPAnu7HNg8L0HVD1Zqqvsqw2iaYMIEYDjoIzwD06ElSLnTt_7g1ZYReqU_uJfHrYJ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df359f5799.mp4?token=WnjxgHnFlIaEUR6igibSUHHsvhJH94dOROpEaaIlPax5NfE-mvntUVo7HeiLwO5DntwjeRCiPZX-LXx3Qmk-6qpVeEiFgokz7bbWlTQBqtp2Io5mEmNurD5-l4OoPMzP1nK8AsYSxhbbUyC-ozp8DtxFjB_sjBoHeibzAjWyXmFnvt0BAFWwHi4yxiAVcO3q21RIeL9BtwSF-y5hVskQ_dRlZNDbTOFX9V00q1pQdI9yovkdQgbEvoH8LLKlwTE-e7_mGVM4IyI9k3RXyj-FPAnu7HNg8L0HVD1Zqqvsqw2iaYMIEYDjoIzwD06ElSLnTt_7g1ZYReqU_uJfHrYJ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
علی زینی‌وند، سخنگو و معاون سیاسی وزارت کشور : تو مرزا فعلاً مشکل خاصی نداریم و اوضاع کامل تحت کنترله.
🔴
از قبل هم همه چیز پیش‌بینی شده بود، قرارگاه‌ها فعالن و روی همه مرزها تسلط کامل دارن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/121579" target="_blank">📅 18:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121578">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
وزیر خارجه پاکستان:
ما تمام تلاش خود را به کار می‌گیریم تا واشنگتن و تهران را برای رسیدن به یک توافق صلح گرد هم آوریم، چرا که ما میانجی هستیم و در این نقش ادامه خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/121578" target="_blank">📅 18:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121577">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUTWyk3V7quvDfKfH5BCOVoXPEVkL2rGakctPE-__EUebBsy_2KUDDnJfAf4vQHxbLXTozyKmLzCDyNaWDXe6B6m3M627BQrhZxoIh0kd2axLs2Wmgm7DvpvjZACb4lpdvmRjrsiXfq7roafphEV_q6bTe2_miI6UbX0JOUJ_4cieWaA4TafqPa9WPytfEWgekNbcIsZxxWDjRrqxSa8D35dmp-X6HUwojyV9PGWpFleF-CoKZCfOQgftf-4cfqs9-sNG6qHj3FCOwUoiTscstyCi76lBxGQ04QZZUK52PK8g8TH9yc6AbSo92lrxNjYwnjKh7hZtsonKu2mu1AVMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تقاضا برای خودروهای برقی در اروپا به دلیل افزایش قیمت بالای سوخت که ناشی از جنگ ایران است، افزایش یافته و فروش خودروهای برقی نو و دست دوم را تقویت کرده است و به گفته روزنامه لس‌آنجلس پست، این صنعت را جان تازه‌ای بخشیده است.
🔴
این جنگ به طور بنیادی تفکر اروپایی‌ها درباره امنیت انرژی را تغییر داده و خودروهای برقی را از حالت «شاید روزی» به «همین حالا» منتقل کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/121577" target="_blank">📅 18:03 · 31 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
