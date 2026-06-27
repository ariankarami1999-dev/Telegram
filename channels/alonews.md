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
<img src="https://cdn4.telesco.pe/file/mztGlRduPcyRrBtusGH3aFM4QE7rNKfGZjDoFiqsmdhof-GTreXVrleH02dbLeAXBcTbYvEsjpiMxAjY65qdRVzC-wy2tsPngoLZdkKBnpXg7XdOS0mRRJ-NHk0xXK_xETHnUYlFZ-isTGKtc2Wh9eDWZpkLSXcG22-QpOuVxWk--L5VaHLTLPS1x6yycXU-yLkpPIW-EG9sMSsCNa5cQYM4BQFn7rxxa8mfmHLbZGZH3hRUsCqrhnkHZrx6VCHnvyTAFFYrXSnUz3WfmY68Q2u1PgCNg7xC4nNW4Tj5Y6Il1Q4pCfuqpLZWlm9PeykVnWKxbaWe8TKM4CNFNzmTXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 935K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 00:21:54</div>
<hr>

<div class="tg-post" id="msg-130596">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOOT09Z4mNcQqdkLXwaogf3RuhDP7YO0M1Yhqw-R23DDiXrvMHh9p5TwYNUGFC2Dv9yFSxJi9lGcVfmonv8eK0Hn4thPcfYdqEKCyK-FBtNwr0KAwOSnHXhqAHdTp6BdDyAAgQXFY6pF-uZleUN0TnM7TOY6GBsEy7FoWBgnA-bnETbrB5nPQFaGWmO4e5ul13qjXWMV-Vy4WX1ZctUHmxgNUQcDhNX2jNH-AIQNGWFfQkz5A36G1uUU8A6STV2NNVfqNTG-rsaLawyaBQ4UCXX9VZiwmRmEDK74P3SSy_QJttvsuthCL5bp5Oo0tZoDLlpiAPs-f72rFKHS5-lwLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محارب‌های حزب الله در خیابان‌ها لاستیک و سطل آشغال سوزاندند
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/130596" target="_blank">📅 00:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130595">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baff5cae92.mp4?token=tBG50sk9mdQjBUo4v3E5d0K5E93IXEkq-csKN1C7-rCqVHrdYTOjdJ7ihnkglxJFahemK0RtOjgrcfyb4EkosHADee9QdAounabiP3PD3MNgUVKTsVgiRoZJ81WfZ81FrTr9qkHnWka_HPgsKbh1Qfa8kH_MwbwdbE2ikzFrpCFhNpBXIaXN-rfIb7Q3esOpZTn4ISL7Sulpe97MSoHq5JYV0P5GzTbNhugQ8sZFr2G9yiD4Tv0JD1qo_FZ7FvmjWebKe_MYVs43HeQwy9yml6iHZF07kgUAjWVkNunrkajsRgE8I9al8Njr7dryu3nOZipsD18_Gvqou5zA3wHdzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baff5cae92.mp4?token=tBG50sk9mdQjBUo4v3E5d0K5E93IXEkq-csKN1C7-rCqVHrdYTOjdJ7ihnkglxJFahemK0RtOjgrcfyb4EkosHADee9QdAounabiP3PD3MNgUVKTsVgiRoZJ81WfZ81FrTr9qkHnWka_HPgsKbh1Qfa8kH_MwbwdbE2ikzFrpCFhNpBXIaXN-rfIb7Q3esOpZTn4ISL7Sulpe97MSoHq5JYV0P5GzTbNhugQ8sZFr2G9yiD4Tv0JD1qo_FZ7FvmjWebKe_MYVs43HeQwy9yml6iHZF07kgUAjWVkNunrkajsRgE8I9al8Njr7dryu3nOZipsD18_Gvqou5zA3wHdzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از اغتشاش امشب طرفداران حزب الله در بیروت
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/alonews/130595" target="_blank">📅 00:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130594">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">تو دنیایی زندگی میکنیم که برای یه وام ساده ضامن بالای ۷۰سال رو قبول نمیکنن اما سرنوشت ۹۰میلیون ایرانی رو پیرمردهای ۹۰ساله‌ای تعیین میکنن که تو رفع نیازهای روزانشون موندن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/130594" target="_blank">📅 00:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130593">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWSzN6F7IqEFApWSGeYbz9JKi7qxhNb5kODCmB9OuKRruUHoSGUV1X4V5PGFVROSuem3eivX038R3wGDk8Ntzfam680HdGEChErPeSHmTpzV3XTHEZrT6jrwsa14JWBxYjAn7pN7LSAK73y8KzxvY3San3I6ekUGIEkBfpUupvzCriFxlBEah1JxRFqp-CbvZzgPnjB-yZ35irKSE3dOOSRT3f5xegDZslf8hrxQTRHfMPXy220HgB6qz3sZffLUUQWvvhPau_y1hFAS2umejfw7vPlTyDrtVF2N-6FwLMoQEWE7Tm-6zmSkWUTZtJej3434-XFRTjUmDFUWkQq3Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگان رهبری: مذاکره کنندگان نباید وارد مسائل اتمی شوند و نباید تنگه هرمز رو از دست بدهند، مذاکره کنندگان باید خطوط قرمز رهبری را رعایت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/130593" target="_blank">📅 00:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130592">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
رئیس‌جمهور صربستان که پس از ماه‌ها اعتراضات ضد دولتی تحت فشار قرار گرفته بود، شامگاه شنبه اعلام کرد که طی چند هفته آینده استعفا خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/130592" target="_blank">📅 23:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130591">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYPEa7UvNywHVaxfbYfY-Tun5wgXN3EnmQpeN_Gew6yeXhhuie6rQOaNIVq0uQYNGNydCu34NFJtDGPx03NM_PlKFm1TSHSvHdeDkaOltWDTNbs-1I2eV6R27HRHjx1wroECXgym3xZdBoobWB61cQruonwin8fnHXNU7twyRbo7XiKtulAuWmeKB2u1WErF6l_RR1UFVdwiJqlZfBUeVCpskZb2kh9RrbqkAOcaJVIkOtSI3Agd8ZyQH6iNeCDdAdknQvrXpcnE-AT2oQBik_io-cNQsvDO9XPEStm1-HnP7vocIhIHNxlYl49CjI1wUA8k1cjNaV_kUWMSiAVExg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: درباره هسته‌ای نباید مذاکره بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/130591" target="_blank">📅 23:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130590">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b6cc76c6.mp4?token=mtUPzNTY8krZ7rWiHgp31g1u8dJGAKNQ58zeYWbB-IyJ5SbiiZEPZgFrg9ZZV7cTJSGmZ4j0iQ43zMy9XsqiC81FOVZSmLSBnHySJkc8xh42HGVHAuWHQRPIOJGSTVxFixaYWw9o7bVyWTOffs5g8BNTdD9kWZdD04reYZzZQzlPdaTvU-BI28EtR7I0GAU1GD9u3w3bTzV4gGtQKiqFK1y8YhAR_4GGXLWK8MszKcNCXq5xOJutotfXgrbv5VVz8Bj22jKUt4n1d4xHWmogNrMnJ2s-Dbz5cOcsEO7j10e3CQRsJCzDYmFCbPDppE4-K0A41k4ioYfYGm-In_4ZOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b6cc76c6.mp4?token=mtUPzNTY8krZ7rWiHgp31g1u8dJGAKNQ58zeYWbB-IyJ5SbiiZEPZgFrg9ZZV7cTJSGmZ4j0iQ43zMy9XsqiC81FOVZSmLSBnHySJkc8xh42HGVHAuWHQRPIOJGSTVxFixaYWw9o7bVyWTOffs5g8BNTdD9kWZdD04reYZzZQzlPdaTvU-BI28EtR7I0GAU1GD9u3w3bTzV4gGtQKiqFK1y8YhAR_4GGXLWK8MszKcNCXq5xOJutotfXgrbv5VVz8Bj22jKUt4n1d4xHWmogNrMnJ2s-Dbz5cOcsEO7j10e3CQRsJCzDYmFCbPDppE4-K0A41k4ioYfYGm-In_4ZOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نبویان: فقط یک نفر از بین ۱۳ عضو شورای عالی امنیت، نظر رهبری را بدرستی تشخیص داد و آن فرد، جلیلی بود
🔴
افرادی که ادعا میکنند ولایی هستند فرمون رو برگردونن نسبت به این تفاهم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/130590" target="_blank">📅 23:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130588">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gN-lCxq5D7UGSI6RrFj4w8TSmBpIeNM2SBUAfkXZmMKTlocoycME85JsZXyfm3_pJTsvvKPiob0w7qLeZ80_Bqw5bvfskoOhM5qUf0zZpHaOGRoNJSQko19pMKHjMYtJ6q8fwQFWgjjbwax8PqQVnGLWKeUnjRidKGFFZY3zS8f55_KLGWkEv1_jhq4kPRPfS9uIykSnbAYamIliiI5woPvbeUxCY2mdKC7L-J0aVyE62qXG1e28S6awLA_1vXsGW67stwfJoGblIqlRPWaZsYEQ1jOCwilLPz-HrvUKDgar4zZSmRCLiJNgWBUH1Tn4jI0-cwlGsEY9G-cWxPxF4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جان سینا : ظرف روزهای آینده برای امضای یک قرارداد اسپانسرینگ مهم با همسرم به ایران و شهر زیبای شیراز سفر می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/130588" target="_blank">📅 23:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130587">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ونزوئلا دوباره زلزله ۵.۶ ریشتری اومد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/130587" target="_blank">📅 23:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130586">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56cc34c4ff.mp4?token=U9GwwzD22eEw2eR9BBhJNj28Cl1QFZiorivCY7I7wtuXgf2M8utQ2Izh0NMmtNg0rA-KeqQI7zkXnDtwB1HXSBUtvmpY34xhSBTBGOuyxaG7HsMadRfnBR-uaSEtLJWpqKNgKfBGJjJdky3jRzXhaMM6jPrwU-nUvM-KmvRcSBgdev8isDRAQPXiSOw2X6y3cp5fIC3Xu_2NCBtOrYrtPWZcF13vJqtuWNNVFzz1Cegfzm3kdPit82IP9TZljjvXiwVUuc77yF7PNVOYQwiRTaUSoF-GzBtWkhLvlHY-tse_2jgK5zsY1G39EMpsR3QF5dTO-1aqviTfz4z09alzBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56cc34c4ff.mp4?token=U9GwwzD22eEw2eR9BBhJNj28Cl1QFZiorivCY7I7wtuXgf2M8utQ2Izh0NMmtNg0rA-KeqQI7zkXnDtwB1HXSBUtvmpY34xhSBTBGOuyxaG7HsMadRfnBR-uaSEtLJWpqKNgKfBGJjJdky3jRzXhaMM6jPrwU-nUvM-KmvRcSBgdev8isDRAQPXiSOw2X6y3cp5fIC3Xu_2NCBtOrYrtPWZcF13vJqtuWNNVFzz1Cegfzm3kdPit82IP9TZljjvXiwVUuc77yF7PNVOYQwiRTaUSoF-GzBtWkhLvlHY-tse_2jgK5zsY1G39EMpsR3QF5dTO-1aqviTfz4z09alzBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم منتشر شده از لحظه حمله به چندین نیروی نظامی در بانه-شب گذشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/130586" target="_blank">📅 23:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130585">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf65d7d28.mp4?token=Zj_PubnU6A0asKU3xp8I9hr7jWbXozhqD3cMmRepC-0kip9SvDTqUf4kZWjuBc28tQeuai8bBu3BLgsWSDSt6TGX5rxMy-ndue-6deevJWMQjizn-34FA6ZlCMIcGPyYRi9iTlE0Y6aXSvbIjb9VSvi78g9W8DbK12cln4ECys96zHxW6EDTpsHiIO4H796P6kj4_NT5ZBLJ8ecLUzjdQB0G5B6U35gQkEyrAXv1gvBEVl7A3Du8rQUXxr_QDL6ZGD5NVnutEBvl9x8c47a41ZLPQ2cggCR6LV52MDk6X8UUAn9OgeAEz7tjjo8-xjaG5bSHoy9TkK15ex30NoqYvl_WqaDMpeZl-53e4-4nAM4lO1Rm8Lj9MyqGVmgcHCXFQhfV7AsDSO3Lq7cf1HxI4T0mFD1Xs6KUKTYG4o_RH1yxmASnWgLwhZJo-CUm8XyQbnDELlT3jVqhY7J52emd8NxDplU-qDN36s0nWd1MekkI8xgCA7ffRMMW7z2H-V1CgE-ATKWCajZ8yaPJZHuUUBDouniHJQpSr0m_2lZ7V4YDCKHUtz1-zKIFhlLzkxJ06V4fG17vMZ3W1Jf-AkDiqyl2bdxdeJ-WLeFWm7C8lcVMILozsKUjx1LfBEbWED18kMUP_gdy-u8-GQi7UTGKMj3Or82kwBRS4n-d0En-S_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf65d7d28.mp4?token=Zj_PubnU6A0asKU3xp8I9hr7jWbXozhqD3cMmRepC-0kip9SvDTqUf4kZWjuBc28tQeuai8bBu3BLgsWSDSt6TGX5rxMy-ndue-6deevJWMQjizn-34FA6ZlCMIcGPyYRi9iTlE0Y6aXSvbIjb9VSvi78g9W8DbK12cln4ECys96zHxW6EDTpsHiIO4H796P6kj4_NT5ZBLJ8ecLUzjdQB0G5B6U35gQkEyrAXv1gvBEVl7A3Du8rQUXxr_QDL6ZGD5NVnutEBvl9x8c47a41ZLPQ2cggCR6LV52MDk6X8UUAn9OgeAEz7tjjo8-xjaG5bSHoy9TkK15ex30NoqYvl_WqaDMpeZl-53e4-4nAM4lO1Rm8Lj9MyqGVmgcHCXFQhfV7AsDSO3Lq7cf1HxI4T0mFD1Xs6KUKTYG4o_RH1yxmASnWgLwhZJo-CUm8XyQbnDELlT3jVqhY7J52emd8NxDplU-qDN36s0nWd1MekkI8xgCA7ffRMMW7z2H-V1CgE-ATKWCajZ8yaPJZHuUUBDouniHJQpSr0m_2lZ7V4YDCKHUtz1-zKIFhlLzkxJ06V4fG17vMZ3W1Jf-AkDiqyl2bdxdeJ-WLeFWm7C8lcVMILozsKUjx1LfBEbWED18kMUP_gdy-u8-GQi7UTGKMj3Or82kwBRS4n-d0En-S_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله مجدد تندروها به جمهوری اسلامی
🔴
چرا روز تشییع آقا با روز استقلال آمریکا تو یک روز هست؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/130585" target="_blank">📅 23:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130584">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
فرمانده سپاه تهران: برای مراسم تشییع رهبر سابق در تهران حضور حداقل بین ۱۲ تا ۱۵ میلیون نفر برآورده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/130584" target="_blank">📅 23:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130583">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vnzzZa-L3Iak-Z7-G3ItFlRbvMl0lzHVUdcRm2U3uIMqZe8b2V9LoXgUxAhNbsaW_0uXloWnquB4uJRV1hnnL-gtK_CP0QXhDP_8iw5mcMGoSymJJBZnf-tD3uKO4_bhVA6tostqPG-1zcGqgmOyFnU0afq5VZUNZJHajHxzms0DzStnq8eX0fYvgk6jb9N1c40aSFWA12Uw8CKWT97ULY2cMi3a5-9HmqMej7e2qTfMeyVFMolrEMZv5BbdJobczIP4ydH3TErQI4jWm8sW_pKHWa8QwVMFLgb0Q1Rs0aYfopbCrfM-12ar-HkL65Rb61Pls2dUuifwON0r62oxwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو هر کشور باید چند روز کار کنی تا بتونی GTA6 بخری:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/130583" target="_blank">📅 23:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130582">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63fcba67c0.mp4?token=ucr0kNKXQNoXQvxcdQwFp8QQ7xwabcqzihLm-I2yu8gI6wLo3Y1FJxVKoX010ylxkspvW3dxsXp2EvnL9oMjcQYwyuCaCuLB0M3ZxzyMX6Ah0aJbNyk6dtYCdsGOfcNyspPuDPudE4U9xYHus4m5TksFAtHQdpKe2z4AQu2i-5cTGT9vyZleZ87SxKx3Tf57j2Np4F1u3RS7rfnhTh3sI-97yXGwJ-MMH6VOqN1xnIw9BfWGz632x117lHow0IVB-WnMhgNoRkxB5m6RuFgMSZCuTNJ5HnhNY7f8esjvreVQSpKp_nr5UeUL_TYH6wGBggMvcOUXY_XkLDGYUK4ueQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63fcba67c0.mp4?token=ucr0kNKXQNoXQvxcdQwFp8QQ7xwabcqzihLm-I2yu8gI6wLo3Y1FJxVKoX010ylxkspvW3dxsXp2EvnL9oMjcQYwyuCaCuLB0M3ZxzyMX6Ah0aJbNyk6dtYCdsGOfcNyspPuDPudE4U9xYHus4m5TksFAtHQdpKe2z4AQu2i-5cTGT9vyZleZ87SxKx3Tf57j2Np4F1u3RS7rfnhTh3sI-97yXGwJ-MMH6VOqN1xnIw9BfWGz632x117lHow0IVB-WnMhgNoRkxB5m6RuFgMSZCuTNJ5HnhNY7f8esjvreVQSpKp_nr5UeUL_TYH6wGBggMvcOUXY_XkLDGYUK4ueQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف به سیم آخر زد!
🔴
یه عده که اسمشونو گذاشتن انقلابی و سوپرانقلابی هیچ غلطی برای این انقلاب نکردن ولی طلبکار از همه هم هستن..
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/130582" target="_blank">📅 23:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130581">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
بنیامین نتانیاهو: ما وعده دادیم که غزه دیگر تهدیدی برای اسرائیل نخواهد بود.
🔴
حماس هنوز برخی از توانایی‌های غیرنظامی را در اختیار دارد.
🔴
ما هنوز کارهایی برای انجام داریم، اما این یک دستاورد بزرگ است. مقایسه وضعیت ما در ۷ اکتبر با وضعیت امروز غیرممکن است.
🔴
چه کسی اهمیت می‌دهد؟ چه یک گورستان سیاسی باشد یا نباشد، هر کاری که برای اطمینان از امنیت و پیروزی دولت اسرائیل لازم باشد، انجام خواهم داد.
🔴
اگر نیاز باشد وارد لبنان شویم، وارد لبنان می‌شویم. اگر نیاز باشد با نیرویی غوغا در آنجا عملیات انجام دهیم، این کار را انجام خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/130581" target="_blank">📅 22:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130580">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a356ac50.mp4?token=H26bS6VJ7xgMMAmJzvMdErkVNisSY6DPtmi4C5OLiVHk7mnxkNgfyAWZZCe8auNjQn3cATw93pnk8s8UUtoi3iMuu8_FViqy5mBimxcv_P20QoVvb60oo6bL0nN4M9yF4ETkBs_9K2mqFm1RTvYCqay2GRFXk5bTbn24z6FS7-nQG2oN1ZV7QJxhJl7f5dTDzOrigCLVE2kQv2TgFhAAYBoLaQkZV4qL3RJ3_v4VC2bQUTyuj0xaaC2xZrKxkm39iHjc6W9yvKGDXmsil293DwNQLagCJcnXyhQyDTXpPDhsZ8hI2QhDpS-RbnbU_HFv0IuzkxnlyjuwKggJLw-xXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a356ac50.mp4?token=H26bS6VJ7xgMMAmJzvMdErkVNisSY6DPtmi4C5OLiVHk7mnxkNgfyAWZZCe8auNjQn3cATw93pnk8s8UUtoi3iMuu8_FViqy5mBimxcv_P20QoVvb60oo6bL0nN4M9yF4ETkBs_9K2mqFm1RTvYCqay2GRFXk5bTbn24z6FS7-nQG2oN1ZV7QJxhJl7f5dTDzOrigCLVE2kQv2TgFhAAYBoLaQkZV4qL3RJ3_v4VC2bQUTyuj0xaaC2xZrKxkm39iHjc6W9yvKGDXmsil293DwNQLagCJcnXyhQyDTXpPDhsZ8hI2QhDpS-RbnbU_HFv0IuzkxnlyjuwKggJLw-xXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سعید لیلاز: آمریکا در بهمن ماه مجدداً به ایران حمله می‌کند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130580" target="_blank">📅 22:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130579">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
لغو مذاکرات فنی در پی حمله آمریکا به سیریک؟
🔴
تیم مذاکره کننده ایران در پی حمله بامداد آمریکا به سیریک درباره بررسی لغو مذاکرات فنی در حال مشورت هستند. یک منبع مطلع در این باره به جماران گفت: مذاکره کنندگان معتقدند نقض صریح ماده یک آتش بس باید واکنشی در سطح توقف مذاکره داشته باشد.
🔴
به گفته این منبع، تیم مذاکره کننده ایران همچنان در حال مشورت در این مورد هستند و رایزنی های خود را ادامه می دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/130579" target="_blank">📅 22:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130578">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ونس: قیمت نفت الان به ۷۳ دلار در هر بشکه بازگشته، در حالی که تا ۱۲۶ دلار رسیده بود؛ این نشانه‌ای است که یک اتفاق واقعی دارد می‌افتد
🔴
آتش‌بس وقتی با ایرانی‌ها طرفی، همیشه کمی آشفته خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/130578" target="_blank">📅 22:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130577">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
گزارش اعتراضات و بستن یک جاده با لاستیک‌ های آتش‌ زده در مسیر بین شهرک ریاق و شهر بعلبک در منطقه بقاع لبنان توسط طرفداران حزب‌الله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/130577" target="_blank">📅 22:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130575">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d63d4338d6.mp4?token=R7A7s9Cli6Im8YXbUCvCOVR_IqybmqHkE7Gn0rWG4LmAf2cAHArXuZKkgYSubK6ffv6FakYO0ribK4VxkEu_PMlIb7YH3eNMibR3qCvt4VW2iSGGi6H_rgZ7BJLjeTSWYa9Wb7PWvSD4iNzSWHMwRV0bO345ASfK6btV8jHGe6URIGn9-bnkZmE47p8nJivFMEFx5cwFmfbKW0WsFl5-W_UWp-fbX8bvpJCexLZsSj1buwwpeH_10VO3i8n1Jo2wINaubj5oiTIx0ovyAcY33Dt_5F-nF9ExUcPWMcJ8z8JSL4pXWqJklqz2c3RgGUVw37l0qVoiobKhn-vPpqClNoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d63d4338d6.mp4?token=R7A7s9Cli6Im8YXbUCvCOVR_IqybmqHkE7Gn0rWG4LmAf2cAHArXuZKkgYSubK6ffv6FakYO0ribK4VxkEu_PMlIb7YH3eNMibR3qCvt4VW2iSGGi6H_rgZ7BJLjeTSWYa9Wb7PWvSD4iNzSWHMwRV0bO345ASfK6btV8jHGe6URIGn9-bnkZmE47p8nJivFMEFx5cwFmfbKW0WsFl5-W_UWp-fbX8bvpJCexLZsSj1buwwpeH_10VO3i8n1Jo2wINaubj5oiTIx0ovyAcY33Dt_5F-nF9ExUcPWMcJ8z8JSL4pXWqJklqz2c3RgGUVw37l0qVoiobKhn-vPpqClNoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: ایرانی‌ها استادان تبلیغات هستند
🔴
تیم مذاکره‌کننده از دولت است و آن‌ها برای مخاطبان سخت‌گیر در تهران بازی می‌کنند.
🔴
دقیقاً همانطور که در سیستم ما سخت‌ گیرانی وجود دارند، در آن‌ها نیز سخت‌گیرانی هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/130575" target="_blank">📅 22:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130574">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
بنیامین نتانیاهو: از همان ابتدا گفتیم که ما طرف توافق بین ایالات متحده و ایران نیستیم.
🔴
اما این به معنای نداشتن منافع نیست. ما منافع خود را داریم و آن‌ها را اعلام خواهیم کرد.
🔴
این در مورد مسئله مرکزی—مسئله هسته‌ای—نیز صادق است. قصد دارم هیأتی به واشنگتن بفرستم تا منافع اسرائیل را توضیح دهم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/130574" target="_blank">📅 22:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130573">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
بنیامین نتانیاهو می‌گوید اسرائیل نیروهای حزب‌الله را حتی قبل از اینکه به آنها شلیک شود، می‌کشد:
🔴
دیروز تهدیدی بسیار دورتر از سربازان ما وجود داشت - نه در برد فوری.
🔴
آن‌ها هفت نفر را دیدند که وارد خانه‌ای می‌شوند. آن‌ها هنوز شلیک نکرده بودند و هنوز خود را سازماندهی نکرده بودند.
🔴
اما آن خانه نابود شد و آن هفت نفر حذف شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/130573" target="_blank">📅 22:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130572">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
عراقچی، فردا در راس یک هیات دیپلماتیک به عراق سفر خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/130572" target="_blank">📅 22:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130571">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
بنیامین نتانیاهو: من نه تنها به دنبال استقلال انرژی هستم که آن را به دست آورده‌ایم، و نه تنها استقلال اقتصادی.
🔴
من همچنین می‌خواهم در صنایع دفاعی و صنایع تسلیحاتی خود، استقلال امنیتی داشته باشیم. صرفاً برای کاهش وابستگی خود به دیگران.
🔴
نتانیاهو در مورد مذاکرات ائتلاف: همه می‌توانند بپیوندند، به شرطی که موافق باشند که اسرائیل دولت-ملت مردم یهود است.
🔴
نتانیاهو: دشمنان بیرونی داریم و قطعاً منتظرند که ما یک جنگ داخلی را آغاز کنیم.
🔴
و می‌گویم، همان‌طور که مناحم بگین گفت، «دیگر جنگ داخلی نیست. اینجا جنگ داخلی نخواهد بود.»
🔴
برای رسیدن به این هدف، قصد دارم یک دولت ملی گسترده تشکیل دهم — نه یک دولت محدود، نه یک دولت چپ‌گرا وابسته به احزاب عربی، بلکه یک دولت ملی گسترده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130571" target="_blank">📅 22:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130570">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ونس: مذاکرات با ایران موفقیت‌آمیز بوده است
🔴
اگر با ایران به توافق نهایی برسیم، عالی می‌شود.
🔴
افزایش جریان نفت از طریق تنگه هرمز نشانه‌ای از وقوع یک اتفاق واقعی است، اما توافق آتش‌بس با ایران همیشه کمی آشفته خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130570" target="_blank">📅 22:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130569">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
بنیامین نتانیاهو:جایی برای دو کشور وجود ندارد.
🔴
از دریا تا اردن، جایی برای دو کشور وجود ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/130569" target="_blank">📅 22:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130568">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
نتانیاهو:ما طرف توافق ایران و آمریکا نبودیم و منافعی داریم که با واشنگتن در مورد آنها گفتگو خواهیم کرد
🔴
ما به عملیات خود در لبنان علیه هرگونه تهدید فوری ادامه می‌دهیم و دیروز ۷ عضو حزب‌الله را که در خانه‌ای دور از نیروهای ما بودند، هدف قرار دادیم.
🔴
ما خروج از مناطق آزمایشی در روستاهای زوتر غربی و فرون در جنوب لبنان را آغاز خواهیم کرد.
🔴
ما به کنترل ۷۰ درصد نوار غزه نزدیک شده‌ایم و حماس را محاصره کرده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/130568" target="_blank">📅 21:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130567">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
نتانیاهو: هیئتی را به واشینگتن اعزام خواهم کرد تا منافع امنیتی اسرائیل را در رابطه با پرونده هسته‌ای ایران تبیین کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/130567" target="_blank">📅 21:53 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130566">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pk-qBWF4kIh0AwLuz211tbq030tMuJ5alahnPhxOZxDPIRDiQYen-Pq5rOPa6bFbcQVTJvDCrkaiBU4UN3VWQcpBRHeE7Feu8IKPrFJPOnzfKE2gZQ4tEY_-Z5ygqi4JGI_sDNnKTa1L8uiAz2SrAhpm6dCgeIvyd1ehTDNKYQtCId-YZ7cro2ymHbECvt5bW9qn1kuJ07gHNXDJo1ZHyv0UGaOQTGTpfQW5rhIrKdNCfgNUEM3VjPaZImu6MCttw7EGxUpNdX1C3EUY6pUmu_XW1LHvBDZUa7Eq-LkgR-Nx9Sr8d0yDbiN1J-AsL3Hc6wBciLgbmf-Xk-WrtXGjdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امنیت ملی اسرائیل بن گویر:
توافق با لبنان اشتباه بزرگی است — من امشب به نخست‌وزیر مراجعه کردم و درخواست کردم که در کابینه رأی‌گیری شود، و هفته‌هاست که علیه این توافق مبارزه می‌کنم.
🔴
در واقع، فعلاً در بیشتر قلمرو باقی می‌مانیم، اما دولت لبنان حزب‌الله را از سلاح‌هایش خلع سلاح نخواهد کرد، وزیران دولت لبنان اعضای حزب‌الله هستند و نمی‌توانیم به لبنان برای گرفتن سلاح‌ها از حزب‌الله اعتماد کنیم — من درخواست رأی‌گیری در کابینه خواهم داد.
🔴
فقط سربازان ارتش اسرائیل حزب‌الله را نابود خواهند کرد — هیچ نهاد دیگری این کار را برای ما انجام نخواهد داد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/130566" target="_blank">📅 21:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130565">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
نتانیاهو درباره ایران: من قویاً با هرگونه تلاشی برای مجبور کردن ایران به عقب‌نشینی مخالفت کردم، و اکنون ایالات متحده و لبنان به ایران می‌گویند که این موضوع به آنها ربطی ندارد.
🔴
ما در حال از بین بردن محور ایران و همچنین محور سیاسی آن هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/130565" target="_blank">📅 21:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130564">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
نتانیاهو درباره لبنان: به یک توافق چارچوبی رسیده‌ایم که به ما امکان می‌دهد به درگیری با لبنان پایان دهیم.
🔴
اسرائیل و لبنان بر سر دو منطقه امنیتی برای آزمایش روند خلع سلاح حزب‌الله توافق کرده‌اند.
🔴
ما به لطف ضربات دردناکی که به حزب‌الله وارد کردیم، توافق با لبنان را نهایی کردیم.
🔴
در حال تلاش برای نابودی زیرساخت‌های حزب‌الله در جنوب لبنان هستیم و هنوز کارهای زیادی برای انجام دادن داریم.
🔴
۹۰ درصد از زرادخانه موشکی حزب‌الله را نابود کردیم
🔴
ایالات متحده و لبنان بر سر ادامه حضور ما در منطقه امنیتی جنوب لبنان توافق کرده‌اند
🔴
به نیروهایمان بر آزادی تحرک برای دفع هرگونه تهدید در لبنان تأکید کردم
🔴
توافق با لبنان می‌تواند به توافق صلح تبدیل شود
🔴
این توافق، اسرائیل و لبنان را تقویت و ایران و حزب‌الله را تضعیف می‌کند.
🔴
از دولت لبنان به خاطر شجاعتی که نشان داده است، تشکر می‌کنم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/130564" target="_blank">📅 21:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130562">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=DynNi3xKABlen4VUAQ__idFymwVijXyN9CFPc5r684srxcIcpdU5sVsVwB6ptXtI9vWlisRW--LcfYovuje7HTJMZ8B6viw_P84WUgEmoJk97TiCFpDZ2rn28dnEUvlYVdBNJ5Cqe281Y3hTykbBUx2ACRwmXTfbFHsuNQGCQStHm-e9yP9RiBeQX2u5dpjyUtmaTKUDGqMbN1hSrkT-h0NxCq_5b-DZbWwlo4h2jTqiVA76hxNXWQRKjr2inhNo6RfyaWSzw9oVOTMoSJg8gpOtAXab0UY0EbN79ANi2m3nWlLzQa-mQDNSH5fayJHZHt3GypQebjtZzGp0bgIFrhAs-gpmnMGw6lROSoTOom0kt4JFGbz1nXEjS6NmFG8VJ6-Q18sIGM78_OPFS48j8_syu3H3o4S8s5lnKs3KsQnhEhRC-vivYBuCN21uGvDr4VWV419ZhCBsU0T68uPluWDHEv9WScuUgRVXlnk_WVA713PkjeFz9UZ50Jw0QeMz9c-aYiset4BImp8nemaQ4983_scL5Ltdj0iCeTKWeNzEXT8Qkug7mnUvQ8yCCcvGwpsAeXReXKktx96ObG2Bc-vuT2qNSPPO1cnvsy950aJvplui15XIIWJcOjwoFFzAVUuf_jbm_DdG5vDWmch9Tog-S6vinrRbxL0cUjiyw18" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=DynNi3xKABlen4VUAQ__idFymwVijXyN9CFPc5r684srxcIcpdU5sVsVwB6ptXtI9vWlisRW--LcfYovuje7HTJMZ8B6viw_P84WUgEmoJk97TiCFpDZ2rn28dnEUvlYVdBNJ5Cqe281Y3hTykbBUx2ACRwmXTfbFHsuNQGCQStHm-e9yP9RiBeQX2u5dpjyUtmaTKUDGqMbN1hSrkT-h0NxCq_5b-DZbWwlo4h2jTqiVA76hxNXWQRKjr2inhNo6RfyaWSzw9oVOTMoSJg8gpOtAXab0UY0EbN79ANi2m3nWlLzQa-mQDNSH5fayJHZHt3GypQebjtZzGp0bgIFrhAs-gpmnMGw6lROSoTOom0kt4JFGbz1nXEjS6NmFG8VJ6-Q18sIGM78_OPFS48j8_syu3H3o4S8s5lnKs3KsQnhEhRC-vivYBuCN21uGvDr4VWV419ZhCBsU0T68uPluWDHEv9WScuUgRVXlnk_WVA713PkjeFz9UZ50Jw0QeMz9c-aYiset4BImp8nemaQ4983_scL5Ltdj0iCeTKWeNzEXT8Qkug7mnUvQ8yCCcvGwpsAeXReXKktx96ObG2Bc-vuT2qNSPPO1cnvsy950aJvplui15XIIWJcOjwoFFzAVUuf_jbm_DdG5vDWmch9Tog-S6vinrRbxL0cUjiyw18" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو درباره لبنان
:
اسرائیل در منطقه امنیتی زرد باقی می‌ماند که ما را ایمن نگه می‌دارد. و این یک دستاورد بزرگ است. بزرگ!
🔴
چون آنها چه کردند؟ آنها تلاش کردند ما را از آنجا با انواع روش‌ها و فشارها بیرون بکشند. البته این اتفاق نیفتاد.
🔴
از رئیس‌جمهور ترامپ و وزیر امور خارجه روبیو برای مشارکت و کمک‌هایشان تشکر می‌کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/130562" target="_blank">📅 21:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130561">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
شبکه عبری کان: فرمانده سنتکام فردا به اسرائیل می‌رود تا بر عقب‌نشینی اسرائیل از دو منطقه در استان نبطیه نظارت کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/130561" target="_blank">📅 21:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130560">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
العربیه به نقل از یک منبع پاکستانی: وزیر خارجه پاکستان در تماس فوری با یک مقام آمریکایی خواسته تنش‌ها کاهش پیدا کنه و ابراز امیدواری کرده آمریکا به اتفاقات اخیر پاسخی نده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/130560" target="_blank">📅 21:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130559">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
جی‌دی ونس: اگر به توافق نهایی نرسیم، آنها هنوز به عنوان یک کشور بسیار ضعیف‌تر هستند و برنامه هسته‌ای شان نابود شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/130559" target="_blank">📅 21:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130558">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
مدتی است که برق شرق تهران قطع شده است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/130558" target="_blank">📅 21:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130557">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lqikzR0x3miyycPPLY6jjUVONVQlOeonOfODusU6zf9cjhkKn570GU93z8PENiT48MZhjm-zd5tQTtM9Jpc-WWKxox8H4hZZsCd_weytifeE1zAbpX3ffpDHPwhVTLH6R51AMNhteCSmZHCkvGC_crfIOvj0ZLTuXN5-FXKBGi_2ptxnmlHkY2uscMmpRDzvNFGPfI9NZVsV9WRonog0zLPIIl7HIuvOlyLuHDihiUxlEd_DN2hWXjTquO8Bp1q7pki9hNn-VEpSQc7Z_AMAYIzmoUpBhunPvoxQgFjhfeUfvd9Qo7jNSBUVfDoiBInmIeF_fOYgRBPEaQQq52Hj1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدتی است که برق شرق تهران قطع شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/130557" target="_blank">📅 20:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130556">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70efb8d7c.mp4?token=IIETPjm1mTYsPcXW381gj_HiQnw7joWXieevKMor2JJMQtmXBl_oSMpCm68p9azV4a_IN38QgZQWnmXa-w5jaFdSxdHfSgju3vqQa-QO7r7DddipsQ_l4eVvlFCf49o3YT5oin39J19uCKyEWvf0kqf6qYupfXtrk1CRsHazSbwXkDi4L6ddKwVUMROrBXei5Kb4Gv8QWH1NFr30O9M3K65XJRrgu1b2GEKdrjTB7WLlZ3cOuUFEHpYs4hZDuJxPi1DUL88p69iGMdT_KMDTa31cLXP4D6JIc6OB6A-tU33DfNdJgI4tHcsyBe4-4tD-vJ_vWeePxTo8QHxHWWWqVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70efb8d7c.mp4?token=IIETPjm1mTYsPcXW381gj_HiQnw7joWXieevKMor2JJMQtmXBl_oSMpCm68p9azV4a_IN38QgZQWnmXa-w5jaFdSxdHfSgju3vqQa-QO7r7DddipsQ_l4eVvlFCf49o3YT5oin39J19uCKyEWvf0kqf6qYupfXtrk1CRsHazSbwXkDi4L6ddKwVUMROrBXei5Kb4Gv8QWH1NFr30O9M3K65XJRrgu1b2GEKdrjTB7WLlZ3cOuUFEHpYs4hZDuJxPi1DUL88p69iGMdT_KMDTa31cLXP4D6JIc6OB6A-tU33DfNdJgI4tHcsyBe4-4tD-vJ_vWeePxTo8QHxHWWWqVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سفیدپوشی سبلان در نخستین روزهای تابستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/130556" target="_blank">📅 20:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130554">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aAq9TfMQ85mpMOqmLIgEzLxbiGpShfk6cZhMAp3u4h5BvrvXXtjwrLKHcQvuOKwkFrgDibUGrgzW4sVr9VgJZNV9iFWtFjFZ65IXEfmdUV1AaUulf2K-batt3QhI_vkQVCfP_6AVtNTqy9VVbRFXptlwr_EiT6gId1ehgjD-leeHfJ63HTCn9rNDzQvJ3xoPnj5P8z-1tTAxCXWGVQzzA23XUbG9rtpKLstSaIwHIg38qFeUeCyRJOikSjFP0B_rNZJ7K7m8uDL43WOaC2K1xvCiNLal3M5eYYwdFNzsoPuqL8b7YPI7YMnkwLVBcKqema7TUTztmiZAjyT4o8xmnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V-BbxSI2GW3gHC_DxGKQKcVEZxKszDPswzlrw31ZrSSz9-iwjAaAuzeCuJ6O1u2Opc-NzsuZMpMuneGSdqR-Fj2L2EXS9SAI6bmMBD4nJir1H6nqrvlSd9L-qD24dg9C5u4Ln5ASJtQ11HviNgfFDULsvMuS0e8kSUrfGiI5eXXGwq5TaDzi2lW4l3_nUweT_Oiau6-e6ZyhIdrBMBiIVyIHKqpVxYa5sDFUJyc1jaV1h9R1rdUPUG411lxJehSxZAitvxAAyUwq52KRaVc7Oz1iL8BKcLnboqPlIkl7qL1sTUL-39hmLM-f7o5o9Lsg8-xQYZ825Lv-yXXbP6E7TQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصویری از حمله اسرائیل به رادار هشدار زودهنگام فتح-۱۴
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/130554" target="_blank">📅 20:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130553">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1zhgEqxwH12iTMbFiHFPNFsKueBagSwJ_pmonasKntQAGnbRDrnSakUzEL1skiHA9PC8z2D25gcfA2ndG_Zqpi6GMvi17YkFnERNEzpRntln926Qe286c4U5W_7TTiDBYUxxR1jxOAv7hoARkGJQz5FmKeM6alZNo0D2NS7dqpj4hZ2cquSAVc76P3gLcLVHS-tE37g4HW5EZPwH5HubHoZEpREbYkPW1QViq3zaon7MAL4D75vW7j8FnnUYOogqe-xbsGpsjHmLfle54ZWC_3GLEdyT6fECDSf9RO_xtiFpdGlby0hSrZ2OQ0YIBXr-dWSD0mToeRHS3OAgPTmuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در Truth Social
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/130553" target="_blank">📅 20:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130552">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjJMQKCGyFEVk1Ae1QiIkFtE98POGAEGiu2XcYQmLi86GhoYadJCHrkVkKF8i03GqSiE1RT1e7UYqef9N8K7c6ouUBIfNTJiZYHDSL8fiovyE24dB-FWOErBRsqm3jDpYuxQ-AxKVci4JjIbNi9437Z_n47kGN9KaUrELP8KkIENOnYxp5hYYsT7F3l1k4dQXFzEb0MENilhUSfOTTJSwDIXqQxaG7UExojrsHA3h6fRTU8ajZM-2LkZ-aa_shvOupT2oPznUN08yT1B5rtu-hALggJyPHw7MeRgdXdDmqNwQei1DLsQuXwX8EjPun8MQkM9KLcS4kjqFgVj5J4QiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره:اختلاف تهران واشنگتن بر سر تنگه هرمز بالا گرفت
🔴
اکنون شاهد آن هستیم که ایران و ایالات متحده در تفسیر مفاد یادداشت تفاهم با یکدیگر اختلاف دارند؛ اختلافی که به‌طور فزاینده تنگه هرمز را به اصلی‌ترین نقطه اختلاف میان دو طرف تبدیل کرده است.
🔴
دو بیانیه اخیر ازجمله بیانیه سپاه مبنی بر نقض ماده ۵ یادداشت تفاهم درباره بازگشایی تنگه هرمز و همچنین بیانیه وزارت خارجه مبنی بر نقض ماده ۱ یادداشت تفاهم درباره توقف فوری درگیری‌ها، شواهد این مدعا هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130552" target="_blank">📅 20:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130551">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9a598c8e4.mp4?token=BxgxzdQLX1pd5EKxG1ePAi7CiFSDCeH2y_Uv8OZvWm1jyWGiVHoBQgx090FZ-JTDpXxKaQSVLoezkYDjnRKhy0FNuC4b4UnUYvPnQFEde2W9Wt8p-qOZ0BENYgS8Gy3zdgZBA1TmVeu20XWWCNamzQ-GW4U2OR6LilTH2qTzh0kW9K3qzjWommc2oycFRKWSYC5gLkAguMERjXw4wLqA627xwlGMhE0Ndo7FWOZno7yjyz9DNgpBQbsEItd2nKRBSIlcy4J-jzsBuBOWrd9nTeVzzueDEcxBaFIHfIcZooJhTbC6ZRF_lkRXQxDew5gSp2GdQk3oZEjB6g8YoYiDSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9a598c8e4.mp4?token=BxgxzdQLX1pd5EKxG1ePAi7CiFSDCeH2y_Uv8OZvWm1jyWGiVHoBQgx090FZ-JTDpXxKaQSVLoezkYDjnRKhy0FNuC4b4UnUYvPnQFEde2W9Wt8p-qOZ0BENYgS8Gy3zdgZBA1TmVeu20XWWCNamzQ-GW4U2OR6LilTH2qTzh0kW9K3qzjWommc2oycFRKWSYC5gLkAguMERjXw4wLqA627xwlGMhE0Ndo7FWOZno7yjyz9DNgpBQbsEItd2nKRBSIlcy4J-jzsBuBOWrd9nTeVzzueDEcxBaFIHfIcZooJhTbC6ZRF_lkRXQxDew5gSp2GdQk3oZEjB6g8YoYiDSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیامدها در نبطیه الفوقا، جنوب لبنان، پس از حملات هوایی اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130551" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130550">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKd5bnGbw_hSYiauWjtKuj8qNM4pnrvP_mlAf4q07-TrcwBamc-bKF4Z-iBevWliM6woiTn1wBfRUXtZp3oVSPrSdEfc0vcCDCDoNBo1tw-L3dj0gb-MiJ0yIy1XakymWQFrAxuIWT-44YsBDl0KCxTfJPVkBV_GZazEFYmsaQMXGx4uFTUqxmNDFLxsy_oemue344xv7dx-qDL4KgWZaJtZcxrs9YI2_Z715nBlc-OGz1DpxPm_Ql5sES9xD9BVZP7Iv1I6yTMccfSA-T7kBtM9mgM1nLyjLtADuIj_L-xeYISm57EfdY3D5hVAJE0H_wzyZ0R5rzp_8xlg1w82Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130550" target="_blank">📅 20:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130549">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8nDJ-fvoi8xAYRBlKfo4Gv6fbu2E1_1o1m2cqPtI9DhWOQm0oS42kJe5vGneEY-oJOHsw9_zW83ABUC0tTpZxacAQwkpQmMYOjIiKhqD4EJUxEWV-C20N1S2EZkH2MT6DaleTx4XR2jLo1mq2IUcIGnpqk4Ssgh-aLDRPO2BMeynpWKOlpB1TohP6tl-0pOY1gPqfvEAxu4BBGstxecHO-Vr88eFvZTjq8zDu9XEM7lDSiqdfqIrFhBf5mYcCdCawb6G8KuzKKRWNgpgLNh5_OUpoXm5kQI6D_xd6HN3sBbISXLGNzvk5WUxUXCwwAUrkAXKPcgMLp59W-ZQhs3RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک پلاکارد در تجمعات شبانه که نوشته ما گشنه میمونیم و یه نون رو ۹۰میلیون نفری میخوریم
🔴
پ.ن: شما از جانب ۹۰میلیون نفر شکر نخور آدم توهمی
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130549" target="_blank">📅 20:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130548">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T46HV2brET9hkcuRaJPr-Sk1tjtyzlZruZ5dpmXHFpyPHSp9KBut4Lu5d3j8qm-4uLIdKZtuAfuYi_gxLMlPqPUy63DeKsQzYHv72nNpFLmRjZR_fm-2PI8U_X0c7GD9FxozsquJsXv9Vhf9hsuSt2nASEHfj1tjzbp1Kbn9WdJ1j5GIbKR8h7Nt-u-wIdWvYEMZv4iA0VVmXHQJyRwjHZTlksG-8QgqSO8LuBpGbBxoS_Ck12hWCZnlARsGQUhQjTmImTytYCAkd0Aya0KmnMT6aApbto-ydj0NfGnTkYUwO5SVOrxVYDHZh_smnUlzG0xaA6rIGWcZtWhtcFU0pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیشب صداوسیما کلی تلاش و سانسور کرد که پرچم رنگارنگ LGBT رو‌نشون نده، بعد رنگارنگ برای اولین بار تبلیغ تلویزیونیش رو دقیقا توی این بازی پخش کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130548" target="_blank">📅 20:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130547">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
پروازهای رامسر به شیراز، مشهد و بغداد برقرار شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130547" target="_blank">📅 20:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130546">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449c854e01.mp4?token=qz1AL1meo8nyb0UHHUAYS0tw5-TFY1RrmnysqNm3aZrpsQtZ7UYWqK0c2nQL7FbTNbi1CgomFTRkqXiMg3qC9XqwIRlMyOvYxQh2le7cNHb__6DCu94tL7vzNO2qCnisz1RFcIl3yfUIM25a_M6NBggyUtJiKxb1x0aazlRiSAGbzml8Z77vDNnPy5NDCB2E3n2ZFZUqgFIniadX3XNbqpke2ozeD2kULiajUOF5A58EgaR7kQzCwxR8cBPE-hkqaa5xgdV6CKPCYNRitPA9x9KLgRtHfqM36OGbn3YUPPrdmZ2OwP7pnVw0wbrgetG5pxH0BEIJh_-CZu9ucpPbFwaUEUshVvPmptAjDOU7X1zGKtDHrfn0tdb53_uEX1OswnZ_cfdjYTD5BcyKgZWJxzxhyXKtBIw9-nLVBgeU6FFeWBFwJrwpMXqeQaqZrHftAhAdahUfn4zbl8IJ07nrwXjXAeTX5HXV5O9d7hXYe5_AURf1ttV1nvqLPOwnpwr3CxWriDkKnFeYigYN-0VuwF4yacP3TN5nKwueTxvXQHq_V6m62ispMRVT3b1g-EL2qlFs-lmogw2HfqXSjHKqNel_FztOAYhKsJ5p7eHzbIzOTtxJSwbWUzrSD0BYpLR1ef5qxQkc3p_M8G47u_xdFff1efw0j2dGASeYtsquRxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449c854e01.mp4?token=qz1AL1meo8nyb0UHHUAYS0tw5-TFY1RrmnysqNm3aZrpsQtZ7UYWqK0c2nQL7FbTNbi1CgomFTRkqXiMg3qC9XqwIRlMyOvYxQh2le7cNHb__6DCu94tL7vzNO2qCnisz1RFcIl3yfUIM25a_M6NBggyUtJiKxb1x0aazlRiSAGbzml8Z77vDNnPy5NDCB2E3n2ZFZUqgFIniadX3XNbqpke2ozeD2kULiajUOF5A58EgaR7kQzCwxR8cBPE-hkqaa5xgdV6CKPCYNRitPA9x9KLgRtHfqM36OGbn3YUPPrdmZ2OwP7pnVw0wbrgetG5pxH0BEIJh_-CZu9ucpPbFwaUEUshVvPmptAjDOU7X1zGKtDHrfn0tdb53_uEX1OswnZ_cfdjYTD5BcyKgZWJxzxhyXKtBIw9-nLVBgeU6FFeWBFwJrwpMXqeQaqZrHftAhAdahUfn4zbl8IJ07nrwXjXAeTX5HXV5O9d7hXYe5_AURf1ttV1nvqLPOwnpwr3CxWriDkKnFeYigYN-0VuwF4yacP3TN5nKwueTxvXQHq_V6m62ispMRVT3b1g-EL2qlFs-lmogw2HfqXSjHKqNel_FztOAYhKsJ5p7eHzbIzOTtxJSwbWUzrSD0BYpLR1ef5qxQkc3p_M8G47u_xdFff1efw0j2dGASeYtsquRxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چندتا از هوادارای ایران و مصر به این شکل پرچم رنگین کمونی رو پاره کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130546" target="_blank">📅 20:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130545">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سازمان دریایی بریتانیا: خدمه نفتکشِ هدف قرار گرفته‌شده در تنگهٔ هرمز در سلامت هستند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130545" target="_blank">📅 19:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130544">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: توافق در حال شکل‌گیری با لبنان، به اسرائیل اجازه می‌دهد تا زمان خلع سلاح حزب‌الله، حضور نظامی خود را در خاک لبنان حفظ کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/130544" target="_blank">📅 19:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130543">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
برگزاری امتحانات نهایی در زمان‌های اعلام‌شده
🔴
وزیر آموزش‌وپرورش: امتحانات نهایی مطابق برنامه زمان‌بندی اعلام‌شده، برگزار خواهد شد.
🔴
جزئیات دقیق زمان‌بندی و اطلاعیه‌های تکمیلی از سوی وزارت آموزش‌وپرورش اعلام می شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130543" target="_blank">📅 19:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130542">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
طی 24 ساعت گذشته،109 نفر دیگر از شهروندان پاریس بر اثر موج گرمای 35 درجه ای جان خود را از دست داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130542" target="_blank">📅 19:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130541">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
عراقچی: ایران همچنان پرچمدار مبارزه با سلاح‌های کشتار جمعی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130541" target="_blank">📅 19:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130540">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
وزیر اقتصاد قزاقستان: قزاقستان در بندرشهید رجایی بندرعباس ترمینال باربری احداث می کند
🔴
این پروژه با هدف توسعه صادرات قزاقستان به بازار‌های جنوب و جنوب شرق آسیا اجرا خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130540" target="_blank">📅 19:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130539">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
رئیس سازمان بازرسی: گرانی خودرو فقط تقصیر خودروسازان نبود
🔴
بخشی از گرانی‌ها ناشی از افزایش هزینه خدمات دولتی و تصمیمات برخی دستگاه‌های اجرایی بوده است
🔴
بخش دیگری از افزایش قیمت‌ها نیز به تخلفات برخی خودروسازان و واردکنندگان مربوط می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130539" target="_blank">📅 19:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130538">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
رویترز: از فروردین ۱۴۰۵ با معافیت ۳۰ روزه آمریکا، هند خرید نفت از ایران را پس از ۷ سال ازسرگرفت.
🔴
سهم ایران از گاز مایع هند از ۱.۶ به ۶.۵ درصد رسید و روزانه ۷۳ هزار بشکه نفت وارد این کشور می‌شود.
🔴
شرکت ملی نفت ایران از طریق کارگزاران و واسطه‌های مستقر در سنگاپور و دبی، با پالایشگاه‌های هندی وارد مذاکره شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130538" target="_blank">📅 19:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130537">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQxt6UgQfqULGcmaEbmLsqHUtROsoLeM7Ld4z9m_9KJXQlqAGjuZPAJEbLY6FbYr5uFUJLBHrJqrNI1yd-kCkcjYZjiZLPZpnld-3MoMnsHJ8kpPLTt1TY28b3FsNxzcH6w78G9JD82XNCoX5scDYDA_9LaY1yJi6aRon_AlemXCVjZKYJ6xsvddQ7-lqA0AF2K5rdOHf6jIXExgmWywq4547v4eziTik5xld-DT2cbdns7LK7uzZszzPg-ftEkL-Kn6FPPOKhJx54OZHxWL0rU8E5eS8IybJ8JV6FqYZJvm8s92czOmjnKXKS5fjrbZCPAYQMue6Y17Brzjo1TfEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چندین حمله پهپادی اسرائیل چند لحظه پیش به نبطیه الفوقا در جنوب لبنان انجام شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130537" target="_blank">📅 19:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130536">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ایندیاتودی
:
وزیر خارجه پاکستان، پس از حملات جدید آمریکا و ایران که تنش‌ها را در منطقه خلیج‌فارس افزایش داد، تلفنی با عباس عراقچی صحبت کرد.
🔴
این تماس پس از آن صورت گرفت که تلاش اخیر برای برقراری صلح در غرب آسیا با شکست مواجه شد.
🔴
اسلام‌آباد اعلام کرد که در جریان این تماس تلفنی، اسحاق‌دار بر تعهد اسلام‌آباد برای ایفای «نقش سازنده» خود در دستیابی به صلح و ثبات پایدار در منطقه تأکید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/130536" target="_blank">📅 19:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130535">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وال‌استریت ژورنال به نقل از یک مقام آمریکایی: دو پهپاد ایرانی بحرین را هدف قرار دادند. یکی از آن‌ها رهگیری و منهدم شد و دیگری در منطقه‌ای دورافتاده در محدوده فرودگاه سقوط کرد. همچنین یک پهپاد دیگر یک نفتکش حامل دو میلیون بشکه نفت را در نزدیکی تنگه هرمز هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130535" target="_blank">📅 18:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130534">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وزیر خارجه ایتالیا: آماده ارائه حمایت دیپلماتیک از توافق لبنان و اسرائیل هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/130534" target="_blank">📅 18:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130533">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFiGOFpwMpTg6NST9intF2oDPqg410XVRqaq2yVBMsztcw8h-Xv4u5sp92Q5ekSl5WjpFbU-ZzYGqnSYmRe6zBHg2ZpqPW4zdWVf4cIe_ylcpNVw2pKWqydaVO9dEqstsGAzQSkG5iDbB5hqlxTi-4x3xcHpZ-mTYGkEDkG67hxsyXS4CEicMFNVyqX3ONgVw_K7MY3WaZpxvMoFBMsZeibJaw9WkEIoT-hu0tdbWQ0FA5CZzd_2jcdPTp7PKphhuFBkvt_Q0y_xQsJ6-tOicEyfPXNdLouT1RaGx5iCp1RJlrXd5qRW9ykLu6ir_EEoPonGZS1l0N6jxuZTbrzmsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شجاع شلیلزاده تبدیل به سوژه جهانی شده
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@AloSport</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/130533" target="_blank">📅 18:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130532">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از یک مقام آمریکایی: یک پهپاد ایرانی به یک نفتکش حامل دو میلیون بشکه نفت خام در نزدیکی تنگه هرمز حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130532" target="_blank">📅 18:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130531">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سفیر روسیه: نیروگاه هسته‌ای جدیدی در ایران احداث می‌کنیم
🔴
الکسی دِدوف: نمایندگان صنایع هسته‌ای ایران و روسیه به زودی در مسکو مذاکراتی برگزار خواهند کرد که طی آن، ساخت نیروگاه هسته‌ای جدید «هرمز» در جمهوری اسلامی ایران مورد بحث قرار خواهد گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130531" target="_blank">📅 18:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130530">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b7f1f3eb7.mp4?token=rB2HDfAe19kamjw6yhIuj6_NLpTyTfvWsKq7sjL55KlPhjLDmHV8F2hQL5VXNvtgscNKHW2AL9d7SGwOu74q8FLO_SSyoyWq2kE0CaUKCePu4-f-51cEg4NY2q0pTGjwjhpHOHCEjnNAWiyO17CB872LrLtbfukkEpBImKBswhdB8x4_-6OKyLHPJ4mR1BbfX62TFMgf_ggu7rEzRtbUJrfCwKprGISzvQenD41LHE4g466xuneFfnOi8WAbRM67NIo1zO5B5ymJA2piBRZC76vfnRnSt9ySXpdhKpFhXoizCbNeRvxEAQi2GtM3KgTefQEAmpM-1VjUWOlaEQOoXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b7f1f3eb7.mp4?token=rB2HDfAe19kamjw6yhIuj6_NLpTyTfvWsKq7sjL55KlPhjLDmHV8F2hQL5VXNvtgscNKHW2AL9d7SGwOu74q8FLO_SSyoyWq2kE0CaUKCePu4-f-51cEg4NY2q0pTGjwjhpHOHCEjnNAWiyO17CB872LrLtbfukkEpBImKBswhdB8x4_-6OKyLHPJ4mR1BbfX62TFMgf_ggu7rEzRtbUJrfCwKprGISzvQenD41LHE4g466xuneFfnOi8WAbRM67NIo1zO5B5ymJA2piBRZC76vfnRnSt9ySXpdhKpFhXoizCbNeRvxEAQi2GtM3KgTefQEAmpM-1VjUWOlaEQOoXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهروندان ونزوئلایی در حال جستجو در میان آوار خانه‌هایشان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/130530" target="_blank">📅 18:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130529">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2cc36462f.mp4?token=K2J1Yw7_aoSIAPVDhCAi6pRwCzVXnWqO7XanNTTSD-QFteG3akW7yb1q1AQ-G6HuBC6IEqWYfmE2TdehFJX_aBMQraZ49regy6NFrKHm7B-r4TNvsROv2jRxZ00ARFrx_IdaU8Qq9w-RBrvFFW1CqYMDeeKfXnVmPWAK5a2q90zFMEXbOtdl9V8XlUZDPEEtM231fKrCWkTsVrreR2RyZVM5RrOdWKnQqc6DMo_3emwZdnVkyYB0a8jR9-8X4ORnXut-W0sc4MbC0Hc5NerLQt8CNEbEm7olHV_d4plOw9d7dX1f2xB-H4qeywX6bqvwgFZj9EJ5v0ZVLnRjpGjNWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2cc36462f.mp4?token=K2J1Yw7_aoSIAPVDhCAi6pRwCzVXnWqO7XanNTTSD-QFteG3akW7yb1q1AQ-G6HuBC6IEqWYfmE2TdehFJX_aBMQraZ49regy6NFrKHm7B-r4TNvsROv2jRxZ00ARFrx_IdaU8Qq9w-RBrvFFW1CqYMDeeKfXnVmPWAK5a2q90zFMEXbOtdl9V8XlUZDPEEtM231fKrCWkTsVrreR2RyZVM5RrOdWKnQqc6DMo_3emwZdnVkyYB0a8jR9-8X4ORnXut-W0sc4MbC0Hc5NerLQt8CNEbEm7olHV_d4plOw9d7dX1f2xB-H4qeywX6bqvwgFZj9EJ5v0ZVLnRjpGjNWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم‌اکنون دود غلیظ ناشی از آتش‌سوزی لندینگ‌کرافت حامل خودرو از مقابل پارک آفتاب ۲ قشم به‌وضوح قابل مشاهده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130529" target="_blank">📅 18:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130528">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
رایزنی وزرای خارجه عمان و مصر درباره دریانوردی در تنگه هرمز و تلاش‌های دیپلماتیک برای پایان تنش و تثبیت آتش‌بس در منطقه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130528" target="_blank">📅 18:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130527">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ارتش روسیه ویدیویی از انهدام کامل یک فروند جنگنده Mig-29 اوکراینی توسط نسخه هدایت شونده پهپاد گران 2 در پایگاهی هوایی در استان میکولائیف اوکراین منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130527" target="_blank">📅 18:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130526">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
بانک مرکزی: ذخایر ارزی بانک مرکزی ۴.۵ میلیارد دلار افزایش یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/130526" target="_blank">📅 17:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130525">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDE_HV2jzUbTGKkGlz_Ygo43N23no5PPpB5AIZFVZskcc7lET5abMkdP0xnfhl8Ip-b2VP8esbyzmOIEcNlkLNKggHIgHmCB-d3_kDEz_1nkHWyYs2eLimajHRrFtbA_xk_A8pmnU6EWO_2-ozCDmcuptrsR4uEwmhwjFPjdxXP_UleFiJL0JjdMzXnzXisWspj2IxFd5EdqFMNR_XPsEPAMiPw28feCe4CXgjRkUpXjdNAE3UezE42hGfwjb3KdZIACt9jFa6U0HOZ43X4e0X3zIKS9cJ9W5nC8fJG2aGXQ0ud_GLjrEY0qAOEwVnDYV7Y0ysgIOnplILc0ZaJFYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اوکراین اعلام کرد یک فروند جنگنده Mig-29 خود در حین ماموریت رزمی بر فراز خاک این کشور سرنگون شده است/منابع روس مدعی هستند پدافند آنها این جنگنده را سرنگون کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130525" target="_blank">📅 17:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130524">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1RLm4RmBeboR0ooqmQML-LX5JcS2ZyLjTva0jwDhgOfkW0bQTNYtE4kG7zPrslOnQQwRnyyWcUmO3PE4wu4K84VKdd6v9RCEAqqeF0qo2dJT9eq3EXR7dsjZ-y9hDskONt_iPeDWmhkH9I6izSx7JP2usBUOzSnOSAZk4a9Y8Vm4fL5UgCRYG0zv_Y_uUg017ExHlpYgue2l82pgi7iAqoZZAvr_RfRBH3U4-_PB7OooTwNyL10RGCJT3eicr--_7SYtUnJUiHIy-Vy31zisll_Kx3edXxMlXC3Lg94t0DQVJJAxurcW_SlvD5loiF180-ViQwBj7tWfZ-NhX39hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گلشهر کرج : گویا آتش سوزی بزرگی رخ داده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130524" target="_blank">📅 17:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130523">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
سی‌ان‌ان: مرکز اطلاعات مشترک نیروی دریایی آمریکا امروز سطح تهدید در تنگه هرمز را به میزان قابل توجهی افزایش داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130523" target="_blank">📅 17:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130522">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
گزارش رسانه تلگراف: حمله به بانک‌های ایرانی کار گروه هکری «گنجشک درنده» است
🔴
رسانه تلگراف در گزارش ۲۳ ژوئن خود مدعی شد حمله سایبری به چهار بانک ایرانی از سوی اسرائیل انجام شده باشد.
🔴
طبق اعلام این گزارش، این حمله بلافاصله پس از اعلام دونالد ترامپ درباره دسترسی ایران به بخش اولیه ۶ میلیارد دلار دارایی نفتی مسدودشده در قطر انجام شده است.
🔴
کارشناسان امنیتی در اسرائیل به تلگراف گفته‌اند گروه هکری «گنجشک درنده» که یک گروه منتسب به عملیات سایبری اسرائیل است، احتمالا مسئول این حمله باشد..
🔴
یک منبع امنیتی دیگر نیز به تلگراف گفته زمان‌بندی عملیات نشان می‌دهد هدف احتمالی، خرابکاری در توافق بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/130522" target="_blank">📅 17:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130521">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۶ ریشتر افغانستان و شمال پاکستان را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130521" target="_blank">📅 17:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130520">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4d474911.mp4?token=NMXW386EEUwCMseTUuYWhBO6Eqhy_IWf-dBvRRLNvGSncGXr0TbQPGXYeqb0hOJjmunjKzQ7hU_rcg7aOZJ2H4G5Nf7jgfzMHPWkinmcJihiG_MiRJHcDVM7C69OEqFEVjS4Ntv0IWPkOCoId-Loj4PsFgnwg5tq0HnUxdOTEiZrxbCCyZiiLiApQr0IRJKn_6XHz-fCm-lch8bqdqitfhOeoIOnVXQA3f3AP3lpz3A4bYu1HOYov8sJBqKJCXHcU2T40e4BTo01yU-x_e0m38Kb2sfG8teG1fuLgSPd2rUn4icRWW5Nb9AlmjEBFkj_VRzsrCUu66kp1nmtZYEY4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4d474911.mp4?token=NMXW386EEUwCMseTUuYWhBO6Eqhy_IWf-dBvRRLNvGSncGXr0TbQPGXYeqb0hOJjmunjKzQ7hU_rcg7aOZJ2H4G5Nf7jgfzMHPWkinmcJihiG_MiRJHcDVM7C69OEqFEVjS4Ntv0IWPkOCoId-Loj4PsFgnwg5tq0HnUxdOTEiZrxbCCyZiiLiApQr0IRJKn_6XHz-fCm-lch8bqdqitfhOeoIOnVXQA3f3AP3lpz3A4bYu1HOYov8sJBqKJCXHcU2T40e4BTo01yU-x_e0m38Kb2sfG8teG1fuLgSPd2rUn4icRWW5Nb9AlmjEBFkj_VRzsrCUu66kp1nmtZYEY4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو پخش زنده ورزش سه از خیابانی انتقاد کردن گفتن چرا اینقدر از تیم ملی انتقاد کردی؟
🔴
خیابانی ام عصبانی شد برنامه رو ول کرد رفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/130520" target="_blank">📅 17:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130519">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
الجزیره : نتانیاهو رسماً اعلام کرده؛
تا وقتی که حزب‌الله خلع سلاح نشه، نیروهای اسرائیلی از جنوب لبنان عقب‌نشینی نمی‌کنن.
🔴
یکی از بندهای مهم توافق ایران و آمریکا؛ عقب نشینی اسرائیل از جنوب لبنانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130519" target="_blank">📅 17:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130518">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
دبیرکل حزب‌الله: سلاح مقاومت هرگز برچیده نخواهد شد.
🔴
توافق دولت لبنان با اسرائیل، مایهٔ ذلت، ننگ و واگذاری حاکمیت لبنان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/130518" target="_blank">📅 17:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130517">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a3a560aea.mp4?token=hZJqoDJV4-rT4b48tosw5fMrPLmmqe8eEFqEiHRatN9b6vg5KHn7njRLU7OsFKCxv0wrhkveQqan4VG4eaK6bV5FNHafPrRz-lbXINJCJqrMxPSRjZY_wJSF-xdYWBGvsCJtmi0uFLpLqnBlaxrQ3xiDFW4CE8ED_wSNWOSZSQrcCmq1fdRkCKt5Ugkq0zBtTzSzr16HffGYJHFnglZW-QlC4V8sn55sqIm8e8MSCDlhDQmAxy7E_aeJ16XhgospoYCgIXB4ivppyrKy27VGLgzvPBal2T6_fzTWo6aVhhYEXExScPyv6uPiwRClkIrqFCTfT4yM6AGsMta25Yd1qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a3a560aea.mp4?token=hZJqoDJV4-rT4b48tosw5fMrPLmmqe8eEFqEiHRatN9b6vg5KHn7njRLU7OsFKCxv0wrhkveQqan4VG4eaK6bV5FNHafPrRz-lbXINJCJqrMxPSRjZY_wJSF-xdYWBGvsCJtmi0uFLpLqnBlaxrQ3xiDFW4CE8ED_wSNWOSZSQrcCmq1fdRkCKt5Ugkq0zBtTzSzr16HffGYJHFnglZW-QlC4V8sn55sqIm8e8MSCDlhDQmAxy7E_aeJ16XhgospoYCgIXB4ivppyrKy27VGLgzvPBal2T6_fzTWo6aVhhYEXExScPyv6uPiwRClkIrqFCTfT4yM6AGsMta25Yd1qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهدی طارمی:
ما به همه آدم های LGBT احترام میزاریم اون انتخاب و نظر خودشونه به ما ربطی نداره ما اینجا هستیم تا فوتبال بازی کنیم.
@AloSport</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/130517" target="_blank">📅 17:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130516">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
دبیرکل حزب‌الله: سلاح مقاومت هرگز برچیده نخواهد شد.
🔴
توافق دولت لبنان با اسرائیل، مایهٔ ذلت، ننگ و واگذاری حاکمیت لبنان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/130516" target="_blank">📅 16:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130515">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
العربیه به نقل از منابع آگاه: دور جدید مذاکرات آمریکا و ایران در ماه ژوئیه در دوحه برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/130515" target="_blank">📅 16:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130514">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nj865wyNduyMfRCiLS28MuEIyWiQgXuD8njy6VvMnevRC3cpvd8nQp_EVbUQQ9fmYsZj6tgWghvzFfGHXVuHpbrMPMbfZdUWk01tRr4EkCAa7FOIl2y0QCwyixYWIibbxLhuhQXKzoanWXtKBMWNLjXnSFyqIczWTWasRRLm4p2xScRI7pE862IpSMPvA90CbJczAvQMmRY-YgSKHtNeIWvaRh8cw7mDP-aU4IAN-XGzxLyeLDfhBbqA_iuXhR8_nGQVhlAt9Ie4r11Q7ct8jAZhoKmfd8HlmrXbcDtPyOsAB0mZ_r_SPWKGhxoqaHeev9szSFJNbB-MoKRkH8T0cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عباس اصلانی خبرنگار تیم مذاکره کننده:
مذاکره‌کنندگان ایرانی پس از حمله بامداد امروز آمریکا به سیریک، در جنوب ایران، در حال بررسی تعلیق مذاکرات فنی با آمریکا در سوئیس هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/130514" target="_blank">📅 16:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130513">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
نتانیاهو: هنوز ماموریت‌های زیادی برای انجام دادن وجود دارد، هنوز کارهای زیادی در برابر ایران باقی مانده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/130513" target="_blank">📅 16:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130512">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سنتکام: حملات ایران به کشتی‌های تجاری را نادیده نخواهیم گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/130512" target="_blank">📅 16:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130511">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=XZ_qIICr3MFetzKJw4k-Kd7W_ToJ7GL-7DvmA5A_6sfiCbtgwSB2EZxftgIlB4a67A7bhXIM3hjaGYt86Gd4564FE11EAurqeKNM1JLVSMkIqVCiRrRZcLNzp4wTxekzlz3o_tIOle-8thcSymleySO3IJIFxevgKDlO1XcG6T3-TsQ0y30gD4U4c7DbLfn13k4V2bz2ausg2Ah7wSwGr-bDhskLsEb8hwbeEbzYa7kY7nT-w8WsqIGowVcKpBaB2k1YIGHQFWdse-zC_OLerFC2jzKa87n0mKabZYUcCb-0c5uX21UcfUI4w2V7inioAK96_2svPnYpLTj2kN9w8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=XZ_qIICr3MFetzKJw4k-Kd7W_ToJ7GL-7DvmA5A_6sfiCbtgwSB2EZxftgIlB4a67A7bhXIM3hjaGYt86Gd4564FE11EAurqeKNM1JLVSMkIqVCiRrRZcLNzp4wTxekzlz3o_tIOle-8thcSymleySO3IJIFxevgKDlO1XcG6T3-TsQ0y30gD4U4c7DbLfn13k4V2bz2ausg2Ah7wSwGr-bDhskLsEb8hwbeEbzYa7kY7nT-w8WsqIGowVcKpBaB2k1YIGHQFWdse-zC_OLerFC2jzKa87n0mKabZYUcCb-0c5uX21UcfUI4w2V7inioAK96_2svPnYpLTj2kN9w8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش تلویزیون الجزیره از خوشحالی مردم غزه بعد از گل مصر به ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/130511" target="_blank">📅 15:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130510">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
منابع العربیه: پاکستان میزبان دور جدیدی از مذاکرات هسته‌ای ایران و آمریکا خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/130510" target="_blank">📅 15:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130509">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f4819f7ba.mp4?token=mgtJAhWBxZf_ow8SR3yr-HeNxP6CLVVTsTyG85UfP1IWzqas222zBACfDgZjrNqrvGzLwzwC0OwW_1oNyHK-HLc3Z7G00rn-_bDnxJnVvOBoQVGSEGjXm-v3-g_zI6ObK5G3lueG2ttFoKhpl1MAgZXr9ZJ0AN9HCE2_XcbAhmeE07U0spgIH6eODOwKo9SumLAaXbog_A8mRPv25DlZ0sqTtfEEdDAHjS-Nbz3gZHOuXPw_FYyK0H3FtqDCIGZKNOvHV4aJ-DOyyd4AxuDMwhF16c8gl3YbLoibScDf0yMJEg3X-ie7TCaY4S07tWIiFpVJGJbmWFpKGB2QhFWDKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f4819f7ba.mp4?token=mgtJAhWBxZf_ow8SR3yr-HeNxP6CLVVTsTyG85UfP1IWzqas222zBACfDgZjrNqrvGzLwzwC0OwW_1oNyHK-HLc3Z7G00rn-_bDnxJnVvOBoQVGSEGjXm-v3-g_zI6ObK5G3lueG2ttFoKhpl1MAgZXr9ZJ0AN9HCE2_XcbAhmeE07U0spgIH6eODOwKo9SumLAaXbog_A8mRPv25DlZ0sqTtfEEdDAHjS-Nbz3gZHOuXPw_FYyK0H3FtqDCIGZKNOvHV4aJ-DOyyd4AxuDMwhF16c8gl3YbLoibScDf0yMJEg3X-ie7TCaY4S07tWIiFpVJGJbmWFpKGB2QhFWDKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمزه صفوی:
سناریوی بسیار خطرناک اسرائیل علیه ایران، سناریوی «قورباغه‌پز» است
🔴
تجویز نخست اسرائیلی‌ها این است که آمریکا را متقاعد به حمله تمام عیار با هدف نابودی تمامی زیرساخت‌های ایران بکنند و هر جوری هم ایران دوست دارد جواب بدهد، چون به زعم آن‌ها بعد از آن، می‌تواند با مرگ تدریجی روبرو شود
🔴
سناریوی دوم اسرائیلی‌ها این است که ایران را وارد یک فرایند مرگ تدریجی بکنند، یعنی حلقه محاصره را تنگ تر کنند و مدام به صورت متناوب درگیرش بکنند
🔴
عقل حکم می‌کند که سناریوی اصلی ما فرسایش‌گریزی از طریق «توافق بزرگ» باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/130509" target="_blank">📅 15:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130508">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmeBE_VpFW9xNs17d4_IqbioSSYRUPV_aB-gY6EC8G2PH_Bk4dwpG2dZKZpotDsYRAIrqUH-r3xr7BuREmeTjjicvybdICKHyBgMRbc4B7PJNbShczDZp8wy43Dpce_rCS21Zb4xfhssNHCajdc9WgwSlqI-Wfi_2es7polhfR7Se4tUbyCA57yUzwN8ItDmqn-CmDVc2gDzlY4dE3Zsu67pg0sd3aMIKVwP1whrCqjH_OkefbFKteQu5KpJi4C1TkfGcePrkicIe0fFpxGEFEwLoaIXQnFzOOVJ2TVeiKPMq0qMoZnFrY7VlswWvdYLV7zYXfWF9BbeBmHnra--cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روی دیوار ماهی فروشی‌های بوشهر نوشتن خدایا همه ما را ببخش جز مهدی طارمی
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/130508" target="_blank">📅 15:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130507">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
خدمات کارت بانکی ملی و صادرات دوباره مختل شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/130507" target="_blank">📅 15:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130506">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWZdACL8iqkthchQH1IPNBkC4itQSeSn7rIqnDOluukTyBbTcwn7x0LVDy14hx5CZTHpX5KIhgYEep1tz9l73XeLrKUZRQ4zhV9cwU0F52wyjokHJ5nXy91N9DYxt8PnSJif_zGUGeOx2vi_Uy0s9YGgZO6zcpMBxyuXRoh-PaJKPArAhYOVlrv8r2GbXsWDCPhGHQTwF_1S3hqwyg3DFbWXc5y6q8oke7Fy45ItdYe0lMQVk8Yy9jJSHG6AdiLOi3fkWjrp2LZd0t_CiYz8OwQjW5tlQRpP1ja8djWZsSkc9sfWkcPzkXSGsnlZZnqij9kP_zmeiDqAPHEBI67MqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شجاع خلیلزاده: دوست داشتم گلم رو به آقای شهیدمون تقدیم کنم اما حیف آفساید شد
@AloSport</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/130506" target="_blank">📅 15:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130505">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMy_CHKvijjRrlBQdpJ357m35HLD9yjVUJjhAtvrDaTqbv2oExYDXXhGCijHxQqvVxIeIRFqdWSoqAKdx6B2ju1xRsgl-LA-PHwgRRxs4b1ZVeUUw1LdzfeMuH6RziN_DwkeJeY9lB7JlnBf1-yViAZ7hk0_jH86RiGmO3e_cpLECqVquoM5RYDuIS3zpVaU9dPtsG-2UWoKftdF-wzpo6fYoDhT8SBU65h-nsf5-hod2wPoZIloi07xifubzJLC6Tp-C83ojWc7P20WHWOg26DBka6VuXqO_eoMrls7HwkwngDW9NjrHXma8w-TpT6VqbbNJCBFOhhmA6-ie7EgrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیر رولکس: با ۵سانت عدالت نیست، شاید خدا داره منو میکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/130505" target="_blank">📅 15:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130504">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2CvlOlh63y1gVSp-8THfGQae392YEDvfCtKPFvfN6NPRSCGsLYiLryDrAvKYjbzA_YucietoRG2U1S2RO09KT6a04FzKlzeVmyaexymW9zHpD1lBxYcdoKd1ehqCFlkdYQoIqXv8rEYUvSBkFNhMcDgi5s7wnih829C4hTzj1WbtDpxRRaB_hziGCJdeSpf1wqA4uv5dZq3ofB-E5Gz6S4Zw24A2GnzZLRLtUCtI2dFRRfYgWeyDcqmxln2-oobmBZ8feze4O5PUBTr2QJTHrbqg8XvGWtGwdHBR9wqX8BiaTXmVt-tZpMIXRt24YctK9p8Fkhod9Qmb63UexAo0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: من و بچه‌ها ۷ تیر میریم مجلس اگه بسته باشه وسط خیابون جلسه میزاریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/130504" target="_blank">📅 15:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130503">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4936499a.mp4?token=s9ft_8SZrpQtG8bGkKFrwWmhWaNJhDiyj9NYzPtWkR7hpTc7i4I-yUqfp0OX9HAaSbQuEvKTbmGAbYoCsUCXeqieqS9csY1zL1Bi9wl7Cwuny0wgOhr8UnOnE4HLyyzCJItexYHRwA43ZLJWpsvDXOIs3-aKDyzV0CA6IeFoEfhDxbl1cWbXTpWP5-xi9thOKyx1eFHhyK3BS7qGFFY7tAi7KaVPhSBpyUuaG4KqbI_ORbxPnLJJjj-b_CPJ4yEBWW6Xdd3aX1JwFWFfBvkbKrWLwiguPYUVFjstlQHhtNnMkEnmVDyMAOtbdXuwCsypZnyn3X_N9aR1WLkY3t1xtDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4936499a.mp4?token=s9ft_8SZrpQtG8bGkKFrwWmhWaNJhDiyj9NYzPtWkR7hpTc7i4I-yUqfp0OX9HAaSbQuEvKTbmGAbYoCsUCXeqieqS9csY1zL1Bi9wl7Cwuny0wgOhr8UnOnE4HLyyzCJItexYHRwA43ZLJWpsvDXOIs3-aKDyzV0CA6IeFoEfhDxbl1cWbXTpWP5-xi9thOKyx1eFHhyK3BS7qGFFY7tAi7KaVPhSBpyUuaG4KqbI_ORbxPnLJJjj-b_CPJ4yEBWW6Xdd3aX1JwFWFfBvkbKrWLwiguPYUVFjstlQHhtNnMkEnmVDyMAOtbdXuwCsypZnyn3X_N9aR1WLkY3t1xtDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا سیما : با هشدار سپاه تقاضای کشتی‌ها برای تردد در تنگهٔ هرمز افزایش یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/130503" target="_blank">📅 14:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130502">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
لحظه عبور سیل سنگین در مرند آذربایجان شرقی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/130502" target="_blank">📅 14:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130501">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
رئیس پلیس راهور منطقه ۱۲ تهران: با اعلام آماده‌باش صددرصدی از بامداد جمعه تا صبح سه‌شنبه، از بسته شدن کامل تمامی ورودی‌های تهران از روز جمعه خبر داد و گفت: با پیش‌بینی حضور ۱۵ تا ۲۰ میلیون نفری، هیچ خودرویی از شهرستان‌ها اجازه ورود به پایتخت را نخواهد داشت و زائران فقط با مترو وارد شهر می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/130501" target="_blank">📅 14:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130500">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وبسایت انگلیسی شبکه Aaj پاکستان امروز گزارش داد که شهباز شریف، نخست‌وزیر این کشور، سوم ژوئیه (جمعه ۱۲ تیر) به ایران سفر می‌کند تا در مراسم تشییع پیکر رهبر سابق ایران شرکت کند و پیام تسلیت دولت و مردم پاکستان را به مقام‌های ایرانی ابلاغ کند.
🔴
بر اساس این گزارش، شهباز شریف در جریان این سفر با مقام‌های ارشد ایران دیدار خواهد کرد و قرار است یک هیأت عالی‌رتبه او را همراهی کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/130500" target="_blank">📅 14:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130499">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
رئیس‌کل دادگستری تهران: حکم ضبط اموال ۲۰۰ همتی برای مؤسسهٔ مولی‌الموحدین صادر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/130499" target="_blank">📅 14:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130498">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
یک هواپیمای سوخت رسان آمریکایی از پایگاهی در انگلستان به بن گوریون آمد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/130498" target="_blank">📅 14:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130497">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
الحدث: وزیر خارجهٔ ایران فردا به بغداد سفر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/130497" target="_blank">📅 14:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130496">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سخنگوی سازمان هواپیمایی کشوری: پروازهای تهران - دبی از ۱۰ تیرماه با مجوزهای سازمان هواپیمایی کشوری و همچنین سازمان هواپیمایی امارات برقرار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/130496" target="_blank">📅 14:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130495">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
شهباز شریف: آزادی دریانوردی یک کالای لوکس نیست بلکه ضرورتی مطلق برای کل جهان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/130495" target="_blank">📅 14:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130494">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb4f7a6ed.mp4?token=l434pifu0sKnlViZqIoUVAcXN9nfgXxnuT7dkXbiaOIEs69S1BEFeJ2CtEcueZk4HoqHGTRqyYL1_BJtN3L4SoByD0OnVe9Kf1uwO1j6Yd9uXzAfpSduNzfpQh2bHJZiGILGdrZNyvDQF4N3Uhgcfga3YbdMwO9FXQIuaPhIlGsD2b6xlRYObssTm5Wr0s8RFIm9shjlyiB0PzFvs5AbPRE19Os4RHgZvJrWPRi0bTPmCEcQx5aFKAGx62oRMdOqH8FLHtHY5Y-iwBEgtiLCl3Kc_BwyQUiNkvIMTZHMgL1mRuAV5wBPa5w_xGkLJyMZ6OIh6d4n8AqC6LsApaiCfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb4f7a6ed.mp4?token=l434pifu0sKnlViZqIoUVAcXN9nfgXxnuT7dkXbiaOIEs69S1BEFeJ2CtEcueZk4HoqHGTRqyYL1_BJtN3L4SoByD0OnVe9Kf1uwO1j6Yd9uXzAfpSduNzfpQh2bHJZiGILGdrZNyvDQF4N3Uhgcfga3YbdMwO9FXQIuaPhIlGsD2b6xlRYObssTm5Wr0s8RFIm9shjlyiB0PzFvs5AbPRE19Os4RHgZvJrWPRi0bTPmCEcQx5aFKAGx62oRMdOqH8FLHtHY5Y-iwBEgtiLCl3Kc_BwyQUiNkvIMTZHMgL1mRuAV5wBPa5w_xGkLJyMZ6OIh6d4n8AqC6LsApaiCfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سلیمی، نماینده مجلس: اگر حزب الله در بیروت نجنگد، ما باید در تهران و کرمانشاه با اسرائیل بجنگیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/130494" target="_blank">📅 14:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130493">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igQdn2YBXUvaVKDLItAEuS9Xe6sfcy8i9pZBIFa_DQGNyir7tnPEKd-eh0guiKpcpXpT0gltE0_7tVZHRwuTw8ERc3U8E55zGqsHTPgZODup6TdJlxNyhN2xqEXlU8pdK1wIQhoJFFhvFn75T7dII_t1XQigkv1IFpB4ouNK84MGYxHeTqeBFcM95dOS2xuinVwgeH8fv2Dh_kbHNTE1_P7N4Ptmlpto0C1YwkiBGbqRrj_LWJyoUvuGuj1PvOPkyBCbYjC7t6ft1d5cbbr_ZvLd8808YhjIwgkl55bCy9WO4Iacfs4TP5I1Nrm5r1_ci52Gc7mmRsI6ur5BD4gm0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حداقل 5 سوخت رسان آمریکایی در منطقه خلیج فارس فعالیت می کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/130493" target="_blank">📅 13:57 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
