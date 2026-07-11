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
<img src="https://cdn4.telesco.pe/file/QpmZhgW3Oo61YG57OTGI19WIx3K8XlK3z1QpG-rhYy2ndHUDgbGgVVlzQeqpZOu5C_RRKsEvkrVCand1HpKUyKydVHFK-xPZDEYail3zpYBMKFj76lYopZsNWmF3-y1g0LvWwt4luOBY0aO98KDqit3zpcumvntSXYy0YeALRAq_nW4hNPgxGBx5iVRz08cMTu4DsioFoMKF5hxH_LVyOD8VoQneQzB31ChGjd843hySFuVLX0fCOx3z24US8QXKjX8isnCVuy6Rt8bDpi0DoBz6YO-h4obbIalDXloRrL8HWEEEIaiWu34ylSp4OEDPC_yN13-4JYq_scK_wQRSjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.43M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 02:08:25</div>
<hr>

<div class="tg-post" id="msg-669925">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5NmJ65Dz5kBiYR2eVPUC2VaWAtIJ8YjqVbc4HjZkbBmq02FQUWagwhDBbmMZ2xqnBbsCk7oCA4vRXxz0ewsfGIomI6L4m4vlAnVyK3AroRMVs_5uVCsj9B7HVhd8eH4NATsuHc2gcpLqLu-nhnBt6kau9-lfBDYLgx-sZNijrv0y376bN_GDPCSIsgs-z2mQxzOFEPz4qQG2iJoGzy68t5ngzqRZ8Sasgth1r5lQdesFDgvzxe7ZpnLtLw7ULgJenWH-6Y05s1j1UpHYDJrjtBNZFBOlTuH0U7I1ohC9nkcBEo78MdocVs8FHnlOzEYa5uZh0GFbYxks0lEN3gFSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/669925" target="_blank">📅 01:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669924">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
شنیده شدن انفجار مهیب در غزه
🔹
برخی منابع محلی فلسطینی از وقوع انفجار مهیب در شهر غزه خبر می دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/669924" target="_blank">📅 00:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669923">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2UXh6NlLmornz2iCgMNbcfY8ADeP0lqzV9Pdog_rflRQvGFOzQ87AqxN53-6QJf_UdLwNuDizDLON4I2TF5iw3iZY9EFbzWQBPE98nIWCYNZ4Tz3oKNeNYTNGK_jNiQsGOxVeeNE-oOeE8DlwE1fCCtLuIIiFQv-D5c-wqwcvfBo5c0Z9jHQ7n9KQ6N9Uv2KnCEwKx6FBCGKj4poUeCsNmx3qOTgZx1W74mf0exA6w9SGiVppphP5sLxxutmwV5Vuq3i_WPe6zp_CZ5ACyJTDzFogsx4TziGrJLfiaXPDH0FBXlO26TMEXgYZaKhKSkIdUOIrAmLVPUX6GenaoH3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شگفتی خبرنگار آمریکایی از سرعت بازسازی زیرساخت‌های ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/669923" target="_blank">📅 00:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669922">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8e17dd7a.mp4?token=vwxegqZzHh6wvEgdpKVCZL9k0SrLWF_MRXoH_0GxMy0cFc7d3oaUD10vtJEw6xC7wKqWUOPu5wsOb2E9TUkQaoCpo_iK9G_mpjoijGhDxNl6LnJhUv-NKsk9Fo2dsseNRgYOsebid_7-Yy8S5qQzklvtuwkX2SP5HiBpb72kceeMENNlhRt1Ft11Cfdwu0rxCvLlnaTYzR5970EAAfQODsMkHKE5CNKR-zMy9tawLwcUZsgDNRwYtvWgHUbrLYcM7KEarhF-RHNa7-kWrif3XpNyEkpSXD2BjnVV4hfFweIHdVBMcuDYIqkhuwBMsas_mDL5rciswZagrgykE6juYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8e17dd7a.mp4?token=vwxegqZzHh6wvEgdpKVCZL9k0SrLWF_MRXoH_0GxMy0cFc7d3oaUD10vtJEw6xC7wKqWUOPu5wsOb2E9TUkQaoCpo_iK9G_mpjoijGhDxNl6LnJhUv-NKsk9Fo2dsseNRgYOsebid_7-Yy8S5qQzklvtuwkX2SP5HiBpb72kceeMENNlhRt1Ft11Cfdwu0rxCvLlnaTYzR5970EAAfQODsMkHKE5CNKR-zMy9tawLwcUZsgDNRwYtvWgHUbrLYcM7KEarhF-RHNa7-kWrif3XpNyEkpSXD2BjnVV4hfFweIHdVBMcuDYIqkhuwBMsas_mDL5rciswZagrgykE6juYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو هایی با هوش مصنوعی که بدون حضور بازیگران و کارگردانی ساخته می‌شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/669922" target="_blank">📅 00:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669921">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
مردم بحرین برای دومین روز متوالی، با وجود تهدیدهای رژیم آل خلیفه، در سوگ آقای شهید ایران به عزاداری پرداختند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/669921" target="_blank">📅 00:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669920">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
تداوم تجاوزات صهیونیست‌ها به خاک لبنان
🔹
رسانه‌های لبنانی گزارش دادند یک فروند پهپاد متجاوز اسرائیلی، بمبی صوتی بر فراز شهرک «حداثا» در شهرستان بنت‌جبیل واقع در جنوب لبنان پرتاب کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/669920" target="_blank">📅 00:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669919">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWM8R9bTEyhhB44wqwomBR7-luQS1UD9bOkdAM9RqddmYpJtuCuT9vPqTFRcsQuIdPr8179HQ8LsFQTWznJafpNlNgPuxZ8p2JGTz9dqRt4k2rO8GVftXgJrQ_S3cNcARKpHW_o3Qgj8yxlHxY1LNIaIZuXQbfx-OP_tbtYKCbRXyLJPEVUt7dhaGS6j8gJSZMX0aXErMCoU1XC5xCzAUYGtO9CMmLZZbAuQnsen5tGgbfllY5E3HBl5EPYNS2GQZmZSvf2haCofKD5uqs7yZ7JzU132GwkaRjddfXX4AvGejQFknqjzWfED6O8iweKHmmNxFGLVYgSzLzrANHVnkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/669919" target="_blank">📅 00:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669918">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqOA3DQs3F2GEBJ1R061StTivfygiUbbD1Tpwo14VfKmvlgqaUeKb88oM2qfG0qZFR3MuJzRtLGIeo4Sf4nkB6g1bokfAsEY8AY8dSgAB6zIdUpbWcapGyUsy_hftOc2MzGIivBLh9aTBwqWK7fe1dSLTS-3pLO74gtPooBQKmiz8p19z6SliHRE7eZ0Uf2eyTjA00TgeJM9GW9Q389hWchaFb28w9JylsR9oiODp-AvjvuJ5uocrrdSoZVFB0nU0yPBFXFDrpKbGw9mEF9IqzBBbuiZ6gWD0AkcdQDLaiDXbHdgZIK5F2ZO_gvLno9lvjhOz4sO8Js8IxKklgeSTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معروف‌ترین نمادهای جواهرات که بدون لوگو هم معرف برندشون هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/669918" target="_blank">📅 23:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669917">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f4165199f.mp4?token=AWaNiT6owN1alPdB54BgSPn1d0EyH0_aLRuwbBGOF1ytdggGHJkfpP9GJ74qJf-gFnpp31wFa3ESTXCSgQGz8Yd_AdNiAKLlxPvEMvQ4ujjVZB9nhu9DJMbyOc0GfH7do2uJhBcC2VLSVsDrOVcz0WwQaivQKdxeBRm4_917Pi5L8fzWlDQSXhG3HNFMWm46nDHJhmjK1LLUakEGG20vxgKWTZ1g2_0PXD6b57mWRljJv6ieI7MxQ8xECldwm8PKE3T0aBlAfYhgNJuj3Kz1j2xd0z37iGpOK7OgHY-DcQ0mjLPVX7GahPIbNZQL2LchgpykHqMNjcJ6b3R_Em1pUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f4165199f.mp4?token=AWaNiT6owN1alPdB54BgSPn1d0EyH0_aLRuwbBGOF1ytdggGHJkfpP9GJ74qJf-gFnpp31wFa3ESTXCSgQGz8Yd_AdNiAKLlxPvEMvQ4ujjVZB9nhu9DJMbyOc0GfH7do2uJhBcC2VLSVsDrOVcz0WwQaivQKdxeBRm4_917Pi5L8fzWlDQSXhG3HNFMWm46nDHJhmjK1LLUakEGG20vxgKWTZ1g2_0PXD6b57mWRljJv6ieI7MxQ8xECldwm8PKE3T0aBlAfYhgNJuj3Kz1j2xd0z37iGpOK7OgHY-DcQ0mjLPVX7GahPIbNZQL2LchgpykHqMNjcJ6b3R_Em1pUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کولاک نوجوان گیلانی با تقلید از مداحی معروف حسین ستوده درباره ایران در برنامه محفل ستاره‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/669917" target="_blank">📅 23:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669916">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">«فوکوس»
؛
صریح، بی‌پرده و متفاوت
🔹
وقتی سؤال‌ها تعارف ندارند، پاسخ‌ها هم متفاوت می‌شوند...
🔹
ویژه برنامه «فوکوس» برنامه گفت‌وگوص محور جدید خبرفوری با حضور چهره‌های سیاسی، اجتماعی و اقتصادی کشور
🔹
گفت‌وگوهایی که قرار است حرف‌های ناگفته را به قاب تصویر بیاورند.
♦️
به زودی پخش از طریق رسانه‌های خبرفوری در شبکه‌های اجتماعی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/669916" target="_blank">📅 23:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669915">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddb7774bd4.mp4?token=Yx9CHsvT094OK2x54fuHuPFXKYhj4_0Vl0Ter9ulIf5FTIxT5Dzh2VUHDA0Q4q3G99hrplMfA6VDYRveyfhOFYgymt7Geouo6wkfT-V8tdVMQR6JJMUYIfiKkT1-DdW-OVlhWKY1tz2KCGHAU9BKhZY5-FUe3iXNrytw8SlGs0jhw8uGSfClpo92YPrbVKJU7P4ihC9o8ACuc16M2VIs6lGK_s_l8m29X1cv0Xlg_C9mDp07CCksoHGpXTZP50RpZGa2WIjjvVg4qVOeNgx23qWPGjvtaKYkvz3StMWlCQVCIykbIfbcVKmI6ZmmNO4wuZ6t3rbNGl9pjYnzrlIU_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddb7774bd4.mp4?token=Yx9CHsvT094OK2x54fuHuPFXKYhj4_0Vl0Ter9ulIf5FTIxT5Dzh2VUHDA0Q4q3G99hrplMfA6VDYRveyfhOFYgymt7Geouo6wkfT-V8tdVMQR6JJMUYIfiKkT1-DdW-OVlhWKY1tz2KCGHAU9BKhZY5-FUe3iXNrytw8SlGs0jhw8uGSfClpo92YPrbVKJU7P4ihC9o8ACuc16M2VIs6lGK_s_l8m29X1cv0Xlg_C9mDp07CCksoHGpXTZP50RpZGa2WIjjvVg4qVOeNgx23qWPGjvtaKYkvz3StMWlCQVCIykbIfbcVKmI6ZmmNO4wuZ6t3rbNGl9pjYnzrlIU_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فواید خاکشیر از زبون خودش بشنوید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/669915" target="_blank">📅 23:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669912">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WHy44-YsUuyT39QZPLoxkFQaDREaOHikzVL5FPSeGU1352YRRaslnF4Vn7EygTsuZHL-hp1RejL5_YYCYue0beBbaxHSxn1dAh7B-CGThR7TFSLwwqrcSXTctLBbWUFVjLdx5CYcbTlZaV7RsiAseUYDhBTsQqg9TigHQtkuArTZU4OwPQJEah-O0z7K-iCwmePhI8Thm2sO5EiKfHgTwmdiPIxia6oVnEIgSObmNApQTh5ZvD6j_nxJ-JJWjW2QJv-ulow05hbgA-kg4_-tybH_2My2eyR0FDMpNVmRXfh_XZG8v47rY27z4Bi_gtag-dDs8xEadRkRCIWrOk63Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgRYxfKH0TdrkGLoV9g47l-nov4i79srs53TOvWrGhewQ_sVu_1QGf9tMGTS6QS-b_rUiZ7ZNrajwWD_OB1BQ_KYwkmbY1mf1iZR4rzq3biG1iuz5Px9kAA68UXKAMNX5d5XnjlLgmYlzaCGe08XmvMiwU-oJQsWpntITHSoQf2rei07FxmEu60lrZ8MjkN-m2qQNYnWoB37_dGPAbTF-fEOuqFM_8Ue1D3EnP3gpurQI2_xGBvF9iUriNb-WXICxHu8qIUheid97udxBOVi88Ryl4VctdYDSA54Am5396JPeEZypvz34iI_uD08P4-ZCxuOjuquK5CrtuNkodV0ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MswdHbF_62MbFMMIVtvZdgVzDjqAW6ALm0v8y8zhq9CyjO95FXHCaylyHu2yQ6pjsTJ-kPTpSkpiGQwJtUidXQ47OMrxncIX2IurSD7KgFI34KLGJZ_2OVX_Hu9vwtB9-i4UdmmzwCwvlB6xC7AlfMBKj0O8uxwkZUqN2y9r9KEqCImue_8duJfcdyd3argckE94Egt8gCzcLrnPChdY-R-ywNt5PlzHgDwv31yB0blnhC_R_OhG6vFY8hpZ0qJnbxMuxwhzPO8RHt1IsuOYXfeRMf6jdQocT1uiJE20Lnr7JU_Xwk9Uwtrpt3eVDmxcj9VsDhnEcVPfR_ANJEblMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جدول خاموشی های ساری و بابل برای روز یک‌شنبه ۲۱ تیر ماه اعلام شد
#برق_مردم_کجاست
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/669912" target="_blank">📅 23:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669911">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ادعای اکسیوس: عراقچی پیشنهاد جدید عمان را به تهران برد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/669911" target="_blank">📅 23:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669910">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
تبادل نظر عراقچی با همتای عمانی خود درباره اجرای ماده ۵ تفاهم‌نامه اسلام‌آباد
🔹
سید عباس عراقچی وزیر امور خارجه جمهوری اسلامی ایران که صبح امروز شنبه در راس یک هیات سیاسی-حقوقی به مسقط سفر کرده است، با سید بدر البوسعیدی وزیر امور خارجه سلطنت عمان دیدار و…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/669910" target="_blank">📅 23:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669909">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqdGSyewd8VC2Fpn4PtV3pg4DdmbMZ0XXoNJQoiwDNWjktE7dHYA_tKS7CzL9hg940i8JqUjX-vLVUZS_Dp4fdRxqtywLuHfRWT8MEvg8oaKn_7fi6UxvWXLzXWLi-0lt5ViQJsziUBsBtk7U_7P6zhvcGT4GxY3LzcQmBH2N-OHNKSW12yltZqALIRApjKWySW9pGgWuxSI6D-kB7iO7j9bdCD_3QvZoYpU2_U5vC9FTAcWjIhA21Pzt6qPkaBsWf8kfWJuvQPsnzO3I6gcerpiIfRExo1sRIDA5o6gyQwqgfEhORkmMShKNGIugUcRJL6yR-yBq2e4fKnNTWajSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کف خیابونای کالیفرنیا بیلبورد های ترامپِ فراری از سربازی، یک جنگ‌طلب است در حال چرخواندن است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/669909" target="_blank">📅 23:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669908">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eeece717b.mp4?token=YQX42fcTRw5D_vKc5hhEQAlhDpfO8VH-EDwlSvFtoP9YFb1vXmNU7sSfS-APXMmTaxE9KzUOJdWhIBn9EtjUY9s5Gb2OvawoDCg-HbDI8P_NLbW888LkiRBt369AnyJno1jSunp2vo3ZrSiVrC8Wg-HwBBvWFboN3PF_re2BDf1pYer0PMMoLh9EiiR0zSH09SPXlwrGvL5-BCIaOoxdbv-8HEOTfBGYww3ctQwjX-H1RyYAPRNjVmPXAeZhsd5ss2-dGT64F6BqzuE0Lxzj5SkasRZ76ZvZtW_q8wkorZSYwpn1c2RlCPzVAr9SrYSHRkCl0Nkclh1P6D-6GW5vUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eeece717b.mp4?token=YQX42fcTRw5D_vKc5hhEQAlhDpfO8VH-EDwlSvFtoP9YFb1vXmNU7sSfS-APXMmTaxE9KzUOJdWhIBn9EtjUY9s5Gb2OvawoDCg-HbDI8P_NLbW888LkiRBt369AnyJno1jSunp2vo3ZrSiVrC8Wg-HwBBvWFboN3PF_re2BDf1pYer0PMMoLh9EiiR0zSH09SPXlwrGvL5-BCIaOoxdbv-8HEOTfBGYww3ctQwjX-H1RyYAPRNjVmPXAeZhsd5ss2-dGT64F6BqzuE0Lxzj5SkasRZ76ZvZtW_q8wkorZSYwpn1c2RlCPzVAr9SrYSHRkCl0Nkclh1P6D-6GW5vUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمشیدی، معاون سیاسی دولت شهید رئیسی: صحبت از انتقام رهبری شهید یک موضوع صرفاً عاطفی نیست، بلکه این جریان جنایت‌های دشمن باید متوقف شود
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/669908" target="_blank">📅 23:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669907">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa48803b7.mp4?token=Sgel7JahANOclkTOXNESbXsoggbHxsq7fQUfwuwiM2MSFLJUNewUVkt9o4Kc--7XmWn5OS7r19CXtih3WSTGlmgGOwb9eStnv99KzfNDDrl4Jd4d9DWiCHgW94IBC4lcylSDRVGWh14tH33bTfQCkrQ8CSq6pbffuvxmsPkDmI5EX3nwwpqi5X0Prq2KxdmaIpii9YEukw2BkE-VHIUtyDdLI49B4tn-oBQZEztAGRC4-vgoHx5fcLo42LueyCfb49qHq_ygqshlJOIXIJLApfE55uWzqCcio0kj38EEbx4fr5XupEpDeXreZ2wHe8sVfxc8oqcpCikcaUEVdaMrzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa48803b7.mp4?token=Sgel7JahANOclkTOXNESbXsoggbHxsq7fQUfwuwiM2MSFLJUNewUVkt9o4Kc--7XmWn5OS7r19CXtih3WSTGlmgGOwb9eStnv99KzfNDDrl4Jd4d9DWiCHgW94IBC4lcylSDRVGWh14tH33bTfQCkrQ8CSq6pbffuvxmsPkDmI5EX3nwwpqi5X0Prq2KxdmaIpii9YEukw2BkE-VHIUtyDdLI49B4tn-oBQZEztAGRC4-vgoHx5fcLo42LueyCfb49qHq_ygqshlJOIXIJLApfE55uWzqCcio0kj38EEbx4fr5XupEpDeXreZ2wHe8sVfxc8oqcpCikcaUEVdaMrzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شگرد عجیب فیفا از نمایش همزمان تبلیغ های متفاوت در کشورهای مختلف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/669907" target="_blank">📅 23:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669906">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
آسیا تایمز: آسیا خود را برای شوک‌ دوم شکست احتمالی آتش بس بین ایران و آمریکا آماده می‌کند که افزایش قیمت مواد غذایی در رأس آنها قرار دارد
🔹
در ژاپن مشکل تورم پیچیده‌تر خواهد شد. کره جنوبی که حدود ۷۰٪ نفت خود را از خاورمیانه تأمین می‌کند، در جبهه لجستیکی آسیب‌پذیر است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/669906" target="_blank">📅 22:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669905">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ضرغامی: نباید به تنظیمات کارخانه برگردیم؛ مهمترین سلاح ما وحدت است که باید حفظ شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/669905" target="_blank">📅 22:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669904">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ece85e44f.mp4?token=pNq3wFVpruSva8feCiQGvBpfeY62_Q61-nq9Onz-Y0o7_heiSHUEHKmyTbMera0HGLePDHUaMqRHXHterCJEQBGcA8Q-jiNA6O7RfPP7-wnNTvToegu_IMHMZU9wvQGij4q0yweQwEgORgjyS8rqENfEimb4190zn-O2wSs9cvseXdqFeXSAby-oezZ8bMHW3tOIieBKQKgoXCAhyTbLfgMeKIlv1qgxmyWJ8_wIZCWf6uy4j_w3vDO-xHDEDo3ST8i3E63VBwwhjFnqsYxFZjrHWO8JSHDkN-8JqgIiICO-5PMfGNpyi80j6Alv7hOTkXTRo0itY2RZJC2eLcCbag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ece85e44f.mp4?token=pNq3wFVpruSva8feCiQGvBpfeY62_Q61-nq9Onz-Y0o7_heiSHUEHKmyTbMera0HGLePDHUaMqRHXHterCJEQBGcA8Q-jiNA6O7RfPP7-wnNTvToegu_IMHMZU9wvQGij4q0yweQwEgORgjyS8rqENfEimb4190zn-O2wSs9cvseXdqFeXSAby-oezZ8bMHW3tOIieBKQKgoXCAhyTbLfgMeKIlv1qgxmyWJ8_wIZCWf6uy4j_w3vDO-xHDEDo3ST8i3E63VBwwhjFnqsYxFZjrHWO8JSHDkN-8JqgIiICO-5PMfGNpyi80j6Alv7hOTkXTRo0itY2RZJC2eLcCbag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضرغامی: نباید به تنظیمات کارخانه برگردیم؛ مهمترین سلاح ما وحدت است که باید حفظ شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/669904" target="_blank">📅 22:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669903">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔹
از خبرهای پُربازدید امروز وبسایت خبرفوری غافل نمانید
🔹
🔹
ساعات پایانی اولتیماتوم 24 ساعته ترامپ به ایران و خواسته عجیبش
👇
khabarfoori.com/fa/tiny/news-3229349
🔹
ترامپ تهدید به ترور را جدی گرفت و برای بعد آن برنامه ریزی کرد
👇
khabarfoori.com/fa/tiny/news-3229370
🔹
جزئیات جدید از ترور ۲ بسیجی در مشهد/ اسامی شهدا و تصاویر
👇
khabarfoori.com/fa/tiny/news-3229435
🔹
شوک به فوتبال | ستاره جام جهانی خودکشی کرد
👇
khabarfoori.com/fa/tiny/news-3229524
🔹
شوهرِ وزیر لباس زنانه پوشید؛ وزیر درخواست طلاق داد
👇
khabarfoori.com/fa/tiny/news-3229506
🔹
ویدئوهای جذاب را در آپارات خبرفوری ببینید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/669903" target="_blank">📅 22:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669902">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSsWs7MJ2aNziZdMng5jjtVjpmJ0WiTuzxRMHLIOZ6t-Sb2KEbhKQa52_BbqGx2i2r-oUI2dT_5u34YzRWt_u7c87Aw0U5Xin3-T51XhKV00E29c-ODYgbnNlj3-JZJ7NyuBzQuWnB-JG_I_szQHxegWfp-aE5B0iITsACa4XccxRCDLI8tM-g_PH-0F_p8P8s0CSzBELxpFvEJyzT9hvkRGtRfczcAuMJkCk42BG9SEpJP8HG6mzkZEEj5qfzKuXv5LT_HImQlSPZEKhIaE-8EQW-EqQWsm0BGzLohBUhkP0GteF3ZtmRNjMZ1BBnPP6h65g1aH_Ff1mMoMdD50gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰۰ میانبر کاربردی کامپیوتر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/669902" target="_blank">📅 22:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669901">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d1de6fcdd.mp4?token=Iw5h3CTjjPJj_T5nrAfe8p9q4oz04XdoHdrVDKo7aRuyuzGP9gxHbG_xu-JIZTtlwFWTTgiwHvraI6Wncca3r0w_wHFzY3ngN4_zJJ-huB7y56vrlPTu1pUzliUJ8fM-OiSap4jPcSMdwPWBhjV79L0Cq-9pkkKnPHgdsEqdgKIYK7XYJH0gAZH2UtscJHHpXUuve_puLv7621H4fVDP2XRr67nEZZF6DSo-wU83KEh5k0QGAmFyv9Dn8AmbHKez2D2s33gKByICj9gniXHFlYQyi4DZb7yJhZrRyya_uHFEWekpvmIbF_KWTvadYZsD3QmtycPjSXyWo6oyUh-pXC7wH0PJvixy6YhA1t-ReQzxeR17ttvMAKvIh7UNDI9xuB0jwIve20V5i6za8EDmwfQVG4MU_aRk6lR0ZJ1i3Hlg2ZqCjOdaCxK4JioqxnZHSOvbs6IcXuZ44pKllHrMpKcuB1Z4nL-TYIsPaZpN9-IWhnjZdBwU6tbka-JnHLPjUCorqvefmcDhXtI3gj3qTXEIIBE7g1G1TLsBiD8JMpL5W6sBjKZN99F0toMtmJmXtmqFjiYLiYQBqZ4NxxbTCq3kE76KgApRZLuXQmKxdhys2A7OAskO3nz3EX62Qg1IZivYzKLQ8bwyJGhl_fIJkziTO_NlfIV2HwZY18kFAgc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d1de6fcdd.mp4?token=Iw5h3CTjjPJj_T5nrAfe8p9q4oz04XdoHdrVDKo7aRuyuzGP9gxHbG_xu-JIZTtlwFWTTgiwHvraI6Wncca3r0w_wHFzY3ngN4_zJJ-huB7y56vrlPTu1pUzliUJ8fM-OiSap4jPcSMdwPWBhjV79L0Cq-9pkkKnPHgdsEqdgKIYK7XYJH0gAZH2UtscJHHpXUuve_puLv7621H4fVDP2XRr67nEZZF6DSo-wU83KEh5k0QGAmFyv9Dn8AmbHKez2D2s33gKByICj9gniXHFlYQyi4DZb7yJhZrRyya_uHFEWekpvmIbF_KWTvadYZsD3QmtycPjSXyWo6oyUh-pXC7wH0PJvixy6YhA1t-ReQzxeR17ttvMAKvIh7UNDI9xuB0jwIve20V5i6za8EDmwfQVG4MU_aRk6lR0ZJ1i3Hlg2ZqCjOdaCxK4JioqxnZHSOvbs6IcXuZ44pKllHrMpKcuB1Z4nL-TYIsPaZpN9-IWhnjZdBwU6tbka-JnHLPjUCorqvefmcDhXtI3gj3qTXEIIBE7g1G1TLsBiD8JMpL5W6sBjKZN99F0toMtmJmXtmqFjiYLiYQBqZ4NxxbTCq3kE76KgApRZLuXQmKxdhys2A7OAskO3nz3EX62Qg1IZivYzKLQ8bwyJGhl_fIJkziTO_NlfIV2HwZY18kFAgc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کدام بازار بیشترین سود را ساخته است؟
🔹
بین بورس، سکه، دلار، مسکن و بانک، فقط یک بازار توانسته در بلندمدت هم بازدهی بالاتری بسازد و هم کمتر از تورم شکست بخورد. فکر می‌کنید کدام بازار برنده واقعی این رقابت بوده؟
🔹
در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/669901" target="_blank">📅 22:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669900">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ضرغامی: این مذاکرات مانند خوردن گوشت مردار و میت در مقطع اضطرار است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/669900" target="_blank">📅 22:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669899">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
سفیر آمریکا: اسرائیل، طرح ایران برای کشتن ترامپ را به او خبر داد
🔹
سفیر آمریکا در اراضی اشغالی مایک هاکبی در مصاحبه با فاکس‌نیوز به خبرهای منتشر شده درباره طرح «ترور ترامپ» واکنش نشان داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/669899" target="_blank">📅 22:34 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669898">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkPaI8PCmmtB0cLC-p0Sv5UCzpcv2EZTi6uOEz_S8ccHGoUR7fzZBGSINWTtvs9NFhggL42-88kFYo2BbGN7shKWNBw7saTnHimuYP4d1XnxPch4GBOJaw_QCjs9GYeEwnXnGeRLE4YZbOfNZin7TrdofJHETIBMkKmzP6D-SXPBMc4IRg1WssLHCnK8Ef4RrzlYJpfvd2PUcVc0bD5wy12oC1_Qorhs_eeDzF0CSidBQOIO-QyUXEDqsIsYJTekPLz5bjZBlyQI8jmwtUC1ApO-U7w53-E8ZHWNOfheX08Dgf9P6SGaOEGu8lD3AOkUhApngXfy2_uk4ws8z4GfMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جهش ۳۰ درصدی ایران در شاخص اقتصاد هوش‌ مصنوعی
🔹
ایران در تازه‌ترین شاخص The AI Diffusion Index مایکروسافت با امتیاز ۱۲.۶ درصد در رتبه ۸۵ جهان قرار گرفت. هرچند جایگاه ایران در میانه جدول جهانی است، اما امتیاز کشور نسبت به مدت مشابه سال گذشته حدود ۳۰ درصد رشد کرده است.
🔹
این داده نشان می‌دهد استفاده از هوش مصنوعی در ایران با سرعت قابل‌توجهی در حال افزایش است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/669898" target="_blank">📅 22:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669897">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df84d9c216.mp4?token=NmVXmajW-6Y_d0fHxMoTZptnIM9mJSdi_ImDZR1l4SZti1ZMhll7yTCp5pqlTwiQlT7WR5YmKnB2mux6mrkkbkf6L4EZa9XyOmlYmzo5ekqN7rlZnc0ntxhQeyKDjbxsR99YwOx3apBa-et5hOiIUC5pc4MfRg2gn4L3JdY1sX0vo6i1AJxredLdhGCdP5nxMmCK0g9kVepYCVcyZWWT0JltI0ZqlH9Ybbr61r9nq4tiEwWCM3yq0eNst2GCeYq2g3_i3XyBn5nCydv8I_hjgeDOuOs0IKzS2nZrDZHHRVYrOuXIhapuMqPwnDUqXZQqyZLlJdoWlCLfTEenlHhF0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df84d9c216.mp4?token=NmVXmajW-6Y_d0fHxMoTZptnIM9mJSdi_ImDZR1l4SZti1ZMhll7yTCp5pqlTwiQlT7WR5YmKnB2mux6mrkkbkf6L4EZa9XyOmlYmzo5ekqN7rlZnc0ntxhQeyKDjbxsR99YwOx3apBa-et5hOiIUC5pc4MfRg2gn4L3JdY1sX0vo6i1AJxredLdhGCdP5nxMmCK0g9kVepYCVcyZWWT0JltI0ZqlH9Ybbr61r9nq4tiEwWCM3yq0eNst2GCeYq2g3_i3XyBn5nCydv8I_hjgeDOuOs0IKzS2nZrDZHHRVYrOuXIhapuMqPwnDUqXZQqyZLlJdoWlCLfTEenlHhF0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضرغامی: این مذاکرات مانند خوردن گوشت مردار و میت در مقطع اضطرار است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/669897" target="_blank">📅 22:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669896">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
تشییع رهبر شهید بدون کوچک‌ترین حادثه امنیتی برگزار شد
معاون امنیتی وزیر کشور:
🔹
با وجود تهدیدات امنیتی و گرمی هوا، رویداد عظیم وداع و تشییع رهبر شهید انقلاب با مدیریت مطلوب دستگاه‌های اجرایی و امنیتی و بدون هیچ حادثه‌ای برگزار شد.
🔹
همه دستگاه‌ها وظایف خود را به‌خوبی انجام دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/669896" target="_blank">📅 22:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669895">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1ACWOKEoL5-Drzvzh09WUyYoHZD7jAARNz5ASe4IRd-qxbRNUXHenbz4AC3vjg3JDD1xIpiDaA6zTzQhVAEeDtYCZkc5VuaqmvgwYlM_BzOxhVvQq-jblc-XKZON_-YID8DFoLNvGNMtbpsGAq-3rD89g-clPk82-aKtSNGfHL-NF8wV_QeBMcL0Jw9sDwXrH_FRsmygkv1_weyJP-7xnMWCJBGW5G0PsCUTGpDQyv5K1AhseYyOg5c8g9kVmeh3snDlZqqP31pm7T04Y-snNrbabi8UATLWyLDNC1tlX7WLpPk8SnWg9Zzj_T3-nd85M5UfbOJ-oD-nwePt0ZL6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیکی را بالا ببرید، بدی عقب می‌نشیند
🔹
امام علیه‌السلام می‌فرماید برای بازداشتن گناهکار، فقط مجازات کافی نیست؛ گاهی بهترین راه، پاداش دادن به نیکوکاران است. این تشویق، بدکاران را شرمنده و امیدوار می‌کند تا راه خود را عوض کنند. جامعه نیز با بزرگداشت خوبان،…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/669895" target="_blank">📅 22:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669894">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45f5344508.mp4?token=MngmPhPILevA4F71jEPwhvUfxj_gx2pQA6ORzzYJcgl069bFfSj2mxVR4dy3DEFTGXWo5IEwPphbgyOSy3l9eh0Qsgz-CYVpgar2SLrALFyauml7y5WOzi9eYx3rbq-842o1CssMULlnndWKeGUgrSELspEl75Bhcky5lWps1cH1JOBxkyPvhJcl9evNKiSYoMID02dJNWp_6XskoeCGHwZ4Qa97F247UW9dHWeK8Yhgf8vvDxXQlrl4bAqWN3OOCmnFXm3en7QqDGiPgW4mn6xaYoF8SYj02qFQw_VGXa0CL8luRCV0pMG-JZEuDE4JkYDi0ZbXKhrHo80FS9MWnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45f5344508.mp4?token=MngmPhPILevA4F71jEPwhvUfxj_gx2pQA6ORzzYJcgl069bFfSj2mxVR4dy3DEFTGXWo5IEwPphbgyOSy3l9eh0Qsgz-CYVpgar2SLrALFyauml7y5WOzi9eYx3rbq-842o1CssMULlnndWKeGUgrSELspEl75Bhcky5lWps1cH1JOBxkyPvhJcl9evNKiSYoMID02dJNWp_6XskoeCGHwZ4Qa97F247UW9dHWeK8Yhgf8vvDxXQlrl4bAqWN3OOCmnFXm3en7QqDGiPgW4mn6xaYoF8SYj02qFQw_VGXa0CL8luRCV0pMG-JZEuDE4JkYDi0ZbXKhrHo80FS9MWnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون دبیر شورای‌عالی امنیت ملی: پس از تشییع ۴۳ میلیونی، مسئولیت خونخواهی سنگین‌تر است
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/669894" target="_blank">📅 22:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669893">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
وزارت خارجه عمان: امروز در مسقط، مذاکراتی میان عمان و ایران درباره کشتیرانی در تنگه هرمز و تضمین امنیت و آزادی آن، با توجه به تحولات و پیامدهای ناشی از رویدادهای اخیر، برگزار شد
🔹
دو طرف توافق کردند این گفت‌وگوها را در سطوح فنی و سیاسی ادامه دهند تا بر اساس حقوق بین‌الملل به توافق‌های لازم دست یابند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/669893" target="_blank">📅 22:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669892">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
بازگشت اضطراری هواپیمای اماراتی به فرودگاه دبی
🔹
دقایقی پس از برخاستن یک هواپیمای اماراتی و پرواز بر فراز دریای عمان، خلبان وضعیت اضطراری اعلام کرد و این پرواز ناچار به تغییر مسیر و بازگشت به فرودگاه بین‌المللی دبی شد.
🔹
هنوز جزئیاتی از علت دقیق این نقص فنی یا وضعیت اضطراری اعلام نشده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/669892" target="_blank">📅 22:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669891">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdxT9-9O1S3_t2OJJlbKQQJGaDxsXuVeq-8oKbyo2us6sYg12fbMtpe167-VnzYcbdAJsoMWHnJz61pTsPe4svzDmPoMKQJc17oBOCctA22X9TjQ6v_tjRLeM10he8ZS00v1JzrxIdX3IIEgsVZpG9kMmQ--_wYO7GO_CPABwqFmFSVCB-T0ZhCGg7yw3txWhPUKfuFUggbK_LUe8F0SFTZFQE-ds1asYW2L66mljHMb77Z9N_BaV9ZcO3mS3fot3_UfdkqF4DkBTW2fdQGK-lRK9fUbWvqKhMRp4v4HozEaY98sV_x1PXig12iKxhzpkS1hy0PPphTMLPdLjx5teA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش عجیب تخلفات موتورسیکلت در پایتخت
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/669891" target="_blank">📅 22:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669890">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7BZw4jxVKG4Yxcv_17eZ2-FWqP3mKCi8JpKd_1bdobL774LqxlTBlM60bkQIKNRiFpZ8bLM_gtIGTaFV-fxUhX5K-UEb5rg9R2NYov4PdhwnQk7YEXp3kyobJ74NjpovTwtJBonr_ti7XHPCL5OrirVx6AZ7445xlF6FPAdvQIGsY2Wp2lhmbSl0Ikc_QkPURC-QMaaqZ2YSt5NNmmvyhZJnLU7iP0jVtTiaogIAi3LRuClJfscQyEfItGz2aMT9h6w5Hzi9sVFRJTIJ1MpITFA-8iS1akoCDMWdK6PgzCmLgr6bTcN7OlbvCyb5nUubTBx-pyy3eqIy3gqpZzuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سید علی خمینی همان کودکی هست که در صفحه اول کتب درسی داشت امام رو می‌بوسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/669890" target="_blank">📅 22:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669889">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mit7t6pmwJaRX5D0r-939F4TIWi9oakpJlkFItw0PBHfazySNlk3WUSfIm7X_x1N6JEkapZofmdpDu2gFYsdpht9EdwKYcy23YL2Oq4dxFoD-eNTkDts42T3T_pi5vsUvnTL73uepDVGHculkAOnQ86lKA0ea2kLB2PYt4lwWRZLsUbLA5-5ArnixdRiKsV0if3yAWxOUYbBfrfRi7j7ZNvaJSHLrM8nfNdhX1vPQQSJceWbDNUEdhl_YscvzU3h4z7V9hTSNMvONY3eRIRRLI7KIqPOLCa3pL5pagqw5DO2qe_VCQ9DP9ZTKQsET8YPOZOWA8kVvOrffQb6Gme-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آقای شهید ایران حسینی بود، حسینی اندیشید، حسینی حرکت کرد، حسینی جهاد و مقاومت نمود، حسینی زیست، و حسینی خون خود را در راه مکتب حسین تقدیم کرد و به شهادت رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/669889" target="_blank">📅 22:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669888">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBenelli Motor Iran</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKX_1cfY1GFcaZQAJQ9_rrwLPkKlJ1QldxPUadX7MTt6CpRaH23i_a2vpTlnlqre3JsLNmajVjdT5Q_rOP1rXtYMyMsNhLgZZp8gnNBTjPqughkPVgNEkT5dyuyiw_Q2qFu_dukalle-gn5pF6EB6nJIyT4X1Y5qciH7XWxYJKdSoGfkJdxAUT0CPGe--9dJFtpq_H7aaYcKa2oTN8VkhxXWSEj1BkmXBZwY_3NuAViIh9ha02vRcHKAw4Le0474zswKW4RJ49COce4IosWEKqhHKX_oamO6u8hyPwQtjLp-6NonrsIY5wFHSlhWfwOF8c8WHoEBbwg1c7aIuTN1gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موتورسیکلت بنلی TNT15
✅
در کلاس شهری
✅
انجین بازطراحی‌شده برای یک سواری راحت
⭕
5 درصد تخفیف
⭕
اقساط 24 ماهه
جهت مشاهده قیمت نقد و اقساط روی لینک زیر کلیک نمائید
👇
https://l.nikrun.com/fmr
🏍️</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/669888" target="_blank">📅 22:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669887">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWzz6xnD_X88kpeHRAwD5n5b4XYgj-cBCH2ocSYCSmsLTpIqhRSjPlNwT1RQufEJNGaYiKiI6TrNuhTLtwXps7Rz9Rum1X3OgH2NwVtGVa6OaF3k6IWJDwI4TDaDwh0wpsIFEWIqgMdXlMEUT_IAtxmWGy-RKuiUhnhO2GutvZi8-b7VQDRA03nfAwIO2MdOIXQmGL9kU_J_FhK-B4LjphmkdwI6PpISFMd-ktUnoODF_7vskYWtaxP6tmVX4bb1R8eBEdqMML4MFFVmdfl2WX_8E_qzh-NVACscujuviVUWfg-UXwcHuTsE271IPl3RqtGvALwKAHSr9AJaQVZjYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
فرصت استثنایی سرمایه گذاری در قطعه ممتاز تجاری مسکونی بلوار سجاد مشهد
📐
مساحت: ۵۹۶۴ مترمربع
🏗
کاربری: تجاری - مسکونی
🏢
پروانه:27 طبقه با تراکم 750درصد
💼
شرایط فروش: اقساطی
📅
تاریخ مزایده : 21 الی 24 تیرماه 1405
📍
آدرس ملک: ‌نبش اخوان ثالث ۴
🧭
موقعیت جغرافیایی:
https://nshn.ir/rb1-0tGJG8zR
🌐
اطلاعات بیشتر و شرکت در مزایده و مشاهده سایر فطعات مزایده ؛
https://amlak.razavi.ir/panel/auctions/#auctions
☎️
تماس فوری: ۹۱۰۰۸۰۰۳-۰۵۱
#زمین
#تجاری
#مسکونی</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/669887" target="_blank">📅 22:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669886">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/538713d366.mp4?token=ApyNlvfeZvTEmWbJmuiUsZTq8NM_sVZoiKRVj9ENixIhm9fu78YbDcBbj1V8Zwpu6OMAo2vizHTrI7yVRsXPLS7vz8g9hvOAlx4u8-ZhpW9lPz4nzbTcq_LtrAIluWS2rpfE3LvHOH7ujter7MRTWarFB6klAyqpFEKJyr696I-DwNhn4lstbDR24vMyzc7XU9V43UtX3xqoS9-V7C71bQcl0ubHKTYM4QWzOsYp88XXM7Xc70blA-bu1QCXdlolRJ1OnPE18FYIvfLGm0tttTJZoLcgFfjElsy0ersEMjP6CyoHVEFcu6RMrSYz4sV03kyK26WuAZItfN4qtgSKBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/538713d366.mp4?token=ApyNlvfeZvTEmWbJmuiUsZTq8NM_sVZoiKRVj9ENixIhm9fu78YbDcBbj1V8Zwpu6OMAo2vizHTrI7yVRsXPLS7vz8g9hvOAlx4u8-ZhpW9lPz4nzbTcq_LtrAIluWS2rpfE3LvHOH7ujter7MRTWarFB6klAyqpFEKJyr696I-DwNhn4lstbDR24vMyzc7XU9V43UtX3xqoS9-V7C71bQcl0ubHKTYM4QWzOsYp88XXM7Xc70blA-bu1QCXdlolRJ1OnPE18FYIvfLGm0tttTJZoLcgFfjElsy0ersEMjP6CyoHVEFcu6RMrSYz4sV03kyK26WuAZItfN4qtgSKBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقاد جان بولتون، مشاور سابق امنیت ملی آمریکا از پدوفیلی دیوانه: ترامپ همه را مسخره کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/669886" target="_blank">📅 21:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669885">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef66227064.mp4?token=SckxRth7rWGOiuUbmMAyCkOKoqChjDiPBHhyIv3094H9jjzUW_CI_DpAt-Zj2zQeEEBjP6yvRzByORlSgcbcuxUurfqHJtc4S0mv2Gyw6gwI1Bpk1cjgP_Y5SkzsLpvB7EmkXsOoXbPhF9UrzNodt_xmAzA3auCU-jnN1AYwX1q3MiUJjRGUjcS174E9f-5KMsRdz_XNwUb6ZVgG6aebwajyARDf0Qlr7Ta0kFavX12B-dZC7osdddw5N2kXATp0kAzmwUfInEIsDGoM-rnI8Md985z8st6qYh7FYXdIAKApgc7LV2Ssmv2OKrvv_zu1QZEtV_PZdxdF3PNYsKGU5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef66227064.mp4?token=SckxRth7rWGOiuUbmMAyCkOKoqChjDiPBHhyIv3094H9jjzUW_CI_DpAt-Zj2zQeEEBjP6yvRzByORlSgcbcuxUurfqHJtc4S0mv2Gyw6gwI1Bpk1cjgP_Y5SkzsLpvB7EmkXsOoXbPhF9UrzNodt_xmAzA3auCU-jnN1AYwX1q3MiUJjRGUjcS174E9f-5KMsRdz_XNwUb6ZVgG6aebwajyARDf0Qlr7Ta0kFavX12B-dZC7osdddw5N2kXATp0kAzmwUfInEIsDGoM-rnI8Md985z8st6qYh7FYXdIAKApgc7LV2Ssmv2OKrvv_zu1QZEtV_PZdxdF3PNYsKGU5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل و بارش‌های شدید در منطقه سوغد، خسارات گسترده‌ای به زیرساخت‌ها و منازل مسکونی روستای «دارگ» در بخش «عینی» تاجیکستان وارد کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/669885" target="_blank">📅 21:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669884">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
کاهش مصرف برق در ساعات پیک؛ یک مسئولیت شهروندی
🔹
با افزایش دمای هوا می‌توانیم در ساعات اوج مصرف برق (۱۲ تا ۱۸ و ۲۰ تا ۲۴) با کاهش استفاده از وسایل پرمصرف و مدیریت مصرف، به پایداری شبکه برق کمک کنیم. صرفه‌جویی در این ساعات، علاوه بر جلوگیری از خاموشی‌های…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/669884" target="_blank">📅 21:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669883">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مسکو: اگر موجودیت روسیه به خطر بیفتد از سلاح هسته‌ای استفاده می‌کنیم
🔹
العربیه: ایران با عمان به دنبال توافقی بر سر تنگه هرمز است
🔹
امید عالیشاه و میلاد سرلک با توافقی دوجانبه از پرسپولیس جدا شدند.
🔹
افتتاح پایانه جدید شلمچه عراق با هدف تسهیل تردد زائران اربعین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/669883" target="_blank">📅 21:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669882">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojXcG_ML99VpOjVPLrQSohC54SFy-MsE2DyJ7ykM6w5J7ukKjdD-xsLnSxp1JqK1Rvmvt2HqZwkuxHcX9zmsirSo1rJw89kYqvd19OJBKL1flQN4gRvKs0NwjQutap-pJmlqMW44pLejBZdwHpIfIb-GwaGxE1dKAj4_c_mfbIr7YIqQdMNmVZzLzcJQuDUZ9gyF3qtPR68zf4TiwlAYk0RE-eZlJqa20xF4BNQ-LwAcS_GC6N0hORHNvwmiBzYeL0HF5HlR_uJYrb6SBfC6JUeQcUl7inXnbe53dB88Ih-IuuvKwCA12B0lpRKtA1iaHhuCE4ffXxNxjI-XI1pL3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمام این کودکان به دلیل گازگرفتگی توسط سگ‌های ولگرد جان خود را از دست داده‌اند
🔹
سالانه بالغ بر ۳۰۰ هزار نفر مورد حمله سگ‌ها قرار می‌گیرند و نزدیک به ۵۰ نفر در کشور جان خود را به دلیل سگ‌گزیدگی از دست می‌دهند که بیشتر آن‌ها کودکان هستند. سال‌هاست مسئله سگ‌های ولگرد چالش شهروندان است؛ اما هیچ اقدام موثری توسط مسئولین انجام نمی‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/669882" target="_blank">📅 21:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669881">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TECEAyBXX39lSesWx2p4EaX4MtjcA9QCzT8UsmFOrtwAuPaV5ZjhaNzUPQfhaFnEduiw1ssYpVMSxdDNS5GlpcOQg9HHacMa47gCtvR8NVlEtMfuWZgcIVhGePoK1AKfaofyItonnnA6M6doNjisaaS7C7jQbei02lWcG9cHQfSVDf3QxozOULkCIwlEnG7EutfLklAHmt2GVj0RUqTm5jbg5fIb6wdqu8QvwiuIoH3wKTtDo7mFGpULRSZZuIQ8j0jDXcmUuiBh4IKJavmklyuqgso5LagfJ6qzPDlTPqlPNyweJI_FpY_o_zvFzOO13CfROSHaPr0rC4Ddq_-T9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر قهرمانی، با یک انتخاب درست آغاز می‌شود
🟢
در روزهای پایانی و حساس جام جهانی، انتخاب شما می‌تواند یک ترکیب درست برای رسیدن به ۲۰۰ میلیون تومان صندوق طلای رز ترنج‌ باشد.
🟢
برای اینکه شانس شما افزایش پیدا کند ۳ کار را کامل انجام دهید:
1⃣
از طریق لینک زیر ترکیب خود از صندوق‌های ترنج را بچینید.
2⃣
دوستانتان را به این رقابت دعوت کنید.
3⃣
صندوق طلای رز ترنج را از طریق کارگزاری خود حداقل به میزان ۱۰۰ هزار تومان خریداری کنید. با سرمایه‌گذاری بیشتر شانس شما نیز افزایش پیدا می‌کند.
✅
صندوق طلای رز ترنج؛ بدون اجرت، بدون مالیات، نقدشوندگی بالا، بازدهی بیشتر از طلا
📌
از این لینک در رقابت شرکت کنید.
@Toranjcapital</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/669881" target="_blank">📅 21:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669880">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd5d0e6158.mp4?token=T5qh-fx5JAveMnAEhZJbJ7nBAFPu7fboG2zQCfa8Z9Im_sQ4DgEX4S6dRxLmTgiKp_J0UgsACNzfJURic1_qVZr07OorP6kvFaU2lhjOMgB5MlIarY5-KaSXaYjnAYYjmyM2AJh2YI2ZBlmvREdwAfWNtk6OpJVqdVTdslrC1sGbjXFANX8GgV8ET2kg5iUCg_G_dNg9JsUrHzMGMuFCjYOJIfgawqzh7CsR16_GltOXpsaHvH40Afe-7ud5kjdCXMwMSVvXguOs8H1byXiZVS0Ob8gjx7U7DrIXq4wB_PfBLZFUgYWsrcxjtU-JMqWU9S0h7mw8mUGotKlY0EN3LGEyIUgf2PSuiafCCQ9XF_paA2cGa2ssF9cR1REQgpgqs7voHwF3YF9DaaPYDY7b0M_tyDfrn47ea8xTBDJxGr4qCeM0hcfFOb9GkOFlHOzu5Pc1SQ0NAHnWDDXdpBj77Gk4AEkHrQic71Y9f8lRXCkWOYPcqnQ7XAT1Mfsnkn465aLpzJsw70kQLxbeIiOUsM7OVguEe11bjLaHnuaeInDP5G87PJnh5Og4Eyr6RDysJPv9Xc5GTQz87Id1z7ktOUlMc4SnY7Fn6nQU2mKKFYJgA85r6fDY2iATLClusIKQrVQN09TL2qWI1p6Gl2hWG9lCmKMEnNKfl6HuXzSTcNk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd5d0e6158.mp4?token=T5qh-fx5JAveMnAEhZJbJ7nBAFPu7fboG2zQCfa8Z9Im_sQ4DgEX4S6dRxLmTgiKp_J0UgsACNzfJURic1_qVZr07OorP6kvFaU2lhjOMgB5MlIarY5-KaSXaYjnAYYjmyM2AJh2YI2ZBlmvREdwAfWNtk6OpJVqdVTdslrC1sGbjXFANX8GgV8ET2kg5iUCg_G_dNg9JsUrHzMGMuFCjYOJIfgawqzh7CsR16_GltOXpsaHvH40Afe-7ud5kjdCXMwMSVvXguOs8H1byXiZVS0Ob8gjx7U7DrIXq4wB_PfBLZFUgYWsrcxjtU-JMqWU9S0h7mw8mUGotKlY0EN3LGEyIUgf2PSuiafCCQ9XF_paA2cGa2ssF9cR1REQgpgqs7voHwF3YF9DaaPYDY7b0M_tyDfrn47ea8xTBDJxGr4qCeM0hcfFOb9GkOFlHOzu5Pc1SQ0NAHnWDDXdpBj77Gk4AEkHrQic71Y9f8lRXCkWOYPcqnQ7XAT1Mfsnkn465aLpzJsw70kQLxbeIiOUsM7OVguEe11bjLaHnuaeInDP5G87PJnh5Og4Eyr6RDysJPv9Xc5GTQz87Id1z7ktOUlMc4SnY7Fn6nQU2mKKFYJgA85r6fDY2iATLClusIKQrVQN09TL2qWI1p6Gl2hWG9lCmKMEnNKfl6HuXzSTcNk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برندگان جام جهانی فوتبال از سال ۱۹۳۰ تا ۲۰۲۲ را بشناسید
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/669880" target="_blank">📅 21:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669879">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
اسرائیل هیوم: بر اساس گزارشی در هند، شرکت اسرائیلی رافائل تولید موشک‌های سامانه گنبد آهنین را در هند آغاز خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/669879" target="_blank">📅 21:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669878">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
فریاد مردم برای انتقام یعنی مسئولین مواظب باشید و منافع کشور را نابود نکنید با کوتاه آمدن از امر انتقام
؛
انتقام امری برآمده از عقلانیت است
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/669878" target="_blank">📅 21:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669877">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
دستگیری عامل ترور شهید سرهنگ دوم محسن چهری از کارکنان فراجای کرمانشاه در سردشت
عتباتی:
🔹
فرد دستگیر شده که از تروریست‌ها و اشرار مسلح است در یک عملیات تروریستی در شهرستان کرمانشاه، سرهنگ دوم محسن چهری از کارکنان فراجا استان کرمانشاه را به شهادت رسانده و متواری شده بود.
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/669877" target="_blank">📅 21:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669876">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/500934120b.mp4?token=rI0ucxAzcowgyZKLr091IrTxY1OVnH5o_J7cHMsfjVPSg9KUYfPNBPXyxVFzQN0XMFN9xUTUyi-XOQC9bkW_PvzxCRMwutcKQI0TU9uOZNRivr0RBMTa924Wjx9Ms74ksjvsOxmdkHrm4F-1yJEK62DMjZ5ireo-xy-xd-Erj6gEq1IyDy3pmWR8ugxMyjwK5FB5nDBIsncQFkjTEvhR5QW6HGXojCTLzYv32RpnSJ9XTwpP-xA_nLOCRxbe6D-R8Pjp2uv8EVWgMN8dOIwvZDaN27B4TapAs88eCPmWQ8v_l5Q7bPH7KxB5gAcwrLOTTQtk8aveia91qJ7nr3EDAjv-w6v3gAEknD9crXiZCw7jVbg63ubbxz5W5PC73Po_LVpdWaUXhPykaekPd50ktdhMS4ZurayDTNWMq6e7wbfzGF-1Fd9FuMCxy4CaLgwn9_SzbsWG1R2swJ9aAiRc9uRmDi7Asg0VES0fGqNQ3bGo4AMNsXFVtD71oIQAO5PHE0gnnC016VPx1K-DfStlGsBoTgrLYGF5AaDv9ifveC1sST3YTmeHLWVRlbHaJdJlyqJnltq3lkJTOkhC0ukEilVutR8ZUBDxsAi0nO73JPZzsJSsCqSK08T6VNh6F5Jt__ziKC-9N3NPHFcjaWIhG5zgknPUSivwe2h3JB_3fq8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/500934120b.mp4?token=rI0ucxAzcowgyZKLr091IrTxY1OVnH5o_J7cHMsfjVPSg9KUYfPNBPXyxVFzQN0XMFN9xUTUyi-XOQC9bkW_PvzxCRMwutcKQI0TU9uOZNRivr0RBMTa924Wjx9Ms74ksjvsOxmdkHrm4F-1yJEK62DMjZ5ireo-xy-xd-Erj6gEq1IyDy3pmWR8ugxMyjwK5FB5nDBIsncQFkjTEvhR5QW6HGXojCTLzYv32RpnSJ9XTwpP-xA_nLOCRxbe6D-R8Pjp2uv8EVWgMN8dOIwvZDaN27B4TapAs88eCPmWQ8v_l5Q7bPH7KxB5gAcwrLOTTQtk8aveia91qJ7nr3EDAjv-w6v3gAEknD9crXiZCw7jVbg63ubbxz5W5PC73Po_LVpdWaUXhPykaekPd50ktdhMS4ZurayDTNWMq6e7wbfzGF-1Fd9FuMCxy4CaLgwn9_SzbsWG1R2swJ9aAiRc9uRmDi7Asg0VES0fGqNQ3bGo4AMNsXFVtD71oIQAO5PHE0gnnC016VPx1K-DfStlGsBoTgrLYGF5AaDv9ifveC1sST3YTmeHLWVRlbHaJdJlyqJnltq3lkJTOkhC0ukEilVutR8ZUBDxsAi0nO73JPZzsJSsCqSK08T6VNh6F5Jt__ziKC-9N3NPHFcjaWIhG5zgknPUSivwe2h3JB_3fq8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی مستند: هزار و یک روز انقلاب
🔹
مستند «هزار و یک روز انقلاب» با نگاهی تحلیلی و مبتنی بر بیانات رهبر معظم انقلاب، تفاوت مسیر انقلاب اسلامی ایران با انقلاب‌های بزرگ جهان از جمله آمریکا، فرانسه، روسیه و انگلیس را بررسی می‌کند و نشان می‌دهد چرا انقلاب اسلامی…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/669876" target="_blank">📅 21:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669875">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
ارتش رژیم صهیونیستی ادعا کرد که ساختمانی را که عناصر حزب‌الله وارد آن شده بودند، در داخل منطقه امنیتی هدف قرار داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/669875" target="_blank">📅 21:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669874">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
دستورالعمل تداوم برپایی میادین و تجمعات مردمی
🔹
به‌منظور افزایش شکوه و عظمت مراسم، شایسته است میادینی که در مجاورت یکدیگر قرار دارند، با هماهنگی مسئولان ذی‌ربط با یکدیگر تجمیع و ادغام شوند.
🔹
پایان تمامی برنامه‌ها حداکثر تا ساعت ۲۳ الزامی است؛ همچنین میزان صدای سیستم‌های صوتی و خودروهای مربوطه باید به‌گونه‌ای تنظیم و کنترل شود که هیچ‌گونه مزاحمتی برای ساکنان و همسایگان ایجاد ننماید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/669874" target="_blank">📅 21:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669873">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
استارت اینفانتینو برای ۶۴ تیمی کردن جام جهانی
🔹
جانی اینفانتینو رئیس فیفا، از امکان افزایش تعداد تیم‌های جام جهانی به ۶۴ تیم خبر داد و گفت که این موضوع «قطعا» پس از پایان مسابقات فعلی باید مورد بررسی قرار گیرد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/669873" target="_blank">📅 21:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669872">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtJjHVhMHpiVxmv0DCGBbqd1EOHvBOJTyVZ2iQ7Wmc75_dC9SxC5X5NPTGWMZZFtKkM9tjFrlai9_KsUgAuvFe5-h5tsqrC-VcLKmGlfRpF37qG5QZ3hHJrO8-AkcS46t-OqZ7-g7hItM8jtwHnAIQfuHLC2BB7PAMD48J7rOqkKeDwy5b20KmcMA4qYLJ96_zMEE8dOUS8Cg_uTn7T3NkZlds5Fvw1_95WJmRbF_wMIMKqbV13ZTF0HdLCTKc0yAd6Zg-GaCMmj9mbFqnAdRBHp15LHr1aW7XmGbTKnTI5vgUxxY3c9mDk29qvqJ1DLSdmvJ-2MhGxHYo-1a7qZOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
بازارها بیشتر از جنگ، به احتمال جنگ واکنش نشان می‌دهند.
▪
دلار و طلا در چنین شرایطی می‌توانند به‌سرعت نوسان کنند.
▪
دارایی‌های ریالی در معرض این نوسان قرار دارند.
▪
صندوق درآمد ثابت دلاری الگوراک، راهکاری برای پوشش ریسک ارزی با بازدهی قابل پیش‌بینی.
🔗
https://algr.me/$fix</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/669872" target="_blank">📅 21:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669871">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
سگ زرد از معاینه پزشکی در مرکز درمانی نظامی والتر رید خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/669871" target="_blank">📅 21:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669870">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
خبرگزاری فرانسه: دور بعدی مذاکرات لبنان و اسرائیل ۱۵ و ۱۶ ژوئیه برگزار می‌شود
🔹
آمریکا از ایتالیا خواسته است تا میزبانی این دوره از مذاکرات را بر عهده بگیرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/669870" target="_blank">📅 20:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669869">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e729c031f4.mp4?token=mmYAnXquPEgjJ6qRWPETS_JiynyhbIRE38YBSmHoAfzyhiEZA2wd9MVCZJ4f1pw4D8sh_InuF9RZGr5IT2EKpIdvTUM4Nq7LX9bckxxhZ7u9Vo3-oS50R8G3QRLj_tROMEcOdjmDQIGKiy7ruJy1_2ueYglGBcIbGtBK_f3odDJo1T5oTzGQHqr66EpNg_vU6S3aYgZ3G9T7jDNksb5nTGZrSUeFNdc_7vHbB9OiTl4RBn8Et8eHhJLc0YpFVLygmwP1nnhRqlh-MLQ1vKUul-9hugmjHxn7hFxPg6K1K90oHlPTUDmnr3LDLG7HgXdyhT11PeNto8ccYgwbK8Xxugn9fl8EqU1KwS5392SAEnaCWwf8ToxEERrLV45kZTOtAvXSPe8YuwPRMOniSIYb4LYWJyxHzYdyBOZcKFuxceKI-3AD2aR7jLkFNxaB3AUwzEP6U28mzIN7TykUdOqe3xJ-QtWkj-oIbLEMfHO_QJOrDtwENhjAR4tz81udY96mi_Zz42KGZXLFKOIQQ3tKHnFEr_42f0kfb2PEaDAW2SFJa-3sXglTD_6Dvu8PW30wFhtNJbjWsj7K1UoX5vuxywbXFZD13t1-8zG7Kk3BMi_RW8bKaYJqPHGiUNCixZlXpfBzi-IlJdKnbMswERRJes5UUwvxahOsKbUCBRBPhI8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e729c031f4.mp4?token=mmYAnXquPEgjJ6qRWPETS_JiynyhbIRE38YBSmHoAfzyhiEZA2wd9MVCZJ4f1pw4D8sh_InuF9RZGr5IT2EKpIdvTUM4Nq7LX9bckxxhZ7u9Vo3-oS50R8G3QRLj_tROMEcOdjmDQIGKiy7ruJy1_2ueYglGBcIbGtBK_f3odDJo1T5oTzGQHqr66EpNg_vU6S3aYgZ3G9T7jDNksb5nTGZrSUeFNdc_7vHbB9OiTl4RBn8Et8eHhJLc0YpFVLygmwP1nnhRqlh-MLQ1vKUul-9hugmjHxn7hFxPg6K1K90oHlPTUDmnr3LDLG7HgXdyhT11PeNto8ccYgwbK8Xxugn9fl8EqU1KwS5392SAEnaCWwf8ToxEERrLV45kZTOtAvXSPe8YuwPRMOniSIYb4LYWJyxHzYdyBOZcKFuxceKI-3AD2aR7jLkFNxaB3AUwzEP6U28mzIN7TykUdOqe3xJ-QtWkj-oIbLEMfHO_QJOrDtwENhjAR4tz81udY96mi_Zz42KGZXLFKOIQQ3tKHnFEr_42f0kfb2PEaDAW2SFJa-3sXglTD_6Dvu8PW30wFhtNJbjWsj7K1UoX5vuxywbXFZD13t1-8zG7Kk3BMi_RW8bKaYJqPHGiUNCixZlXpfBzi-IlJdKnbMswERRJes5UUwvxahOsKbUCBRBPhI8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وداع مجری عراقی با رهبر شهید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/669869" target="_blank">📅 20:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669868">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
باید تقاص خون آقا را بگیریم
ذکر علی در مسجدالاقصی بگیریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/669868" target="_blank">📅 20:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669867">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaGwvwT6ryYb-dKc24n5Dbj7zBIJoVv1cqKJZ8AEqDEg4OQJfwcyd3KJ_JDrw2RAt-U1AitaYL4JaJhjjzlu_Tx5zionQ-mZsYZDqhRbO9tWeQ_y_yR53M-OAhNcSWRcl8TCZ6UkgLw6QGKlVa5xU4FqhHkQgYnCf5XiHRTqzuEM8YGqLjoFlW5xGoS8Z2zFjPUHb2RtTMHE370X2hFB2_ZOpVTx9qnMeryJBaVAt4MYm5oyag4Xttl_G2DXy38TGtwPLO1LeXi031jP0WLmDumuclpq4M3dO7X_mZIyfadrrrxUgNHzvPH2BZi-CYhIJ5dhWxdZGeHM2lJbuS3igw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا و رسم پیمان‌شکنی؛ نگاهی به مهمترین معاهداتی که آمریکا از آن خارج شده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/669867" target="_blank">📅 20:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669858">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
از عذاب رباخواران تا راز دو قطره آب؛ ادامه یک تجربه تکان‌دهنده
🔹
00:05:30 گله‌مندی گل مصنوعی از قضاوت و تفکرات من در مورد آن
🔹
00:15:15 ماجرای شنیدنی از مصداق حقیقی نجات فرزند به واسطه دعای مادر
🔹
00:29:40 عظمت و همبستگی بی‌نظیر اجرام آسمانی
🔹
00:34:55 رؤیت حرم امام رضا(ع) در آسمان مانند نگین در آب
🔹
00:42:50 چشیدن طعم تکرارناپذیر دو قطره آب
🔹
00:45:45 علت عذاب عجیب خوردن فضولات و دفع آتش
🔹
00:52:30 بالارفتن از نردبانی در برزخ با کمک به ایتام در دنیا
🔹
01:00:00 علت ارزشمندی گریه برای امام حسین(ع)
🔹
قسمت سی‌ویکم (بی‌نهان)، فصل چهارم
🔹
#تجربه‌گر
: خدیجه مبینی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/669858" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669856">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ytis1oGPf974JeGnG7tJk0LHtUaYc3SI1kYcwH__WB0okdSAI13bZbZxDF_kff-uO_ipxm9fDbulXca-F6mTq825R97MnW4bkLdjgy31cmr5NNK7ag555TTu9QAOly85trG3h_nXx8bQLtVETlamUD2fL56vrGbm4Z8vZW-Wq2QBcalinz-fo7USnUGt8iTexWGou47efDBfcfvovcsCXCvxHeMYmQ91-H6Ic5jQv03pEyz5PdWEGqD7G0dsJgCb-X0VV_6YkGvpJV1GAZ399J5fhrhuYCa-vy_9zC2odJJv2bCMeH4FD75ZwHqhHjVQbvnirSERzuEqGxGksFSl3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شیطان زرد ۳۲ بار اعلام کرده که جنگ با ایران تمام شده است
🔹
بر اساس بررسی انجام شده توسط ان‌بی‌سی‌نیوز، دست‌کم ۳۲ بار ترامپ اعلام کرده که جنگ با ایران تقریباً تمام شده یا پیروز شده است. اما این اظهارات خوش‌بینانه معمولاً با تهدیدهای جدید برای اقدام نظامی همراه بوده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/669856" target="_blank">📅 20:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669854">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkBVRYngbXFzfK3UibrLUm5wyV3Sk78XXihnb-rHp7HtrjFjp4dZ_5E7WAMijwUKGBpU54GA4YIDVf9nhVXEtOPS0WDRVdcc7WndEplzNjSSzWPH8Zk1LauK7CgdxOCwWeAK0RxgT0bSLexpM3ONo3b9lV6JvHD7fhZjphkCi8izHaDwctH5CSusHHYApiWOIeM8EheBLVSul5MNSpgYD89MLegzylJYyPQBl-PNJsd9PpK4RptyR0MPwBiPYf0AhceFws1HlYfJsPyQC4F-cQIgFqS99UPy0U2_zuJ3mVtA1Y4wnPKrHIoVPvO9QBWh9NMQt0jIWztYp7alU4m5MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گذراندن</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/669854" target="_blank">📅 20:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669853">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fn8JZXgWv3u1CMbXtFWC0wZsTO3owP-t05aQdIW-BirRtL6E_DskGu1S3Rvkt2Jmsu43LSmKptbZcCDRuXdIHWWvzHSCkAdESaiuD-_8R2Z2mF6VvgAjrE5yjJjrc9Moim3XI3P0jmLZVn5g-3quRk-GxTQo3GxaG8S0Ugfcs3PddzvdTarrlWBWbPdYvnXclTNq4W8dSr-ifIwXf4LZ7jL3oIygWbd5lL8FybGQX1Fi4qs4h5rfFVRGk_e79hewwYGOU2aeJzoNCfTXUZraY48b3n_LlMndK8inWmvKlKlZBGD-UhTStK9nwUtmgZhEzyMRVfMDyBDvThxYBEsr3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گامی نو در ارتقای خدمات اطلاع‌رسانی شهری؛ بهره‌گیری از تلویزیون‌های مدرن و کیوسک‌های هوشمند برای پوشش رویدادهای ملی و مذهبی در مشهد
🔹
به گزارش روابط عمومی سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی شهرداری مشهد، عارف عباسی، مدیرعامل سازمان، از بهره‌گیری مؤثر از ظرفیت کیوسک‌های هوشمند شهری و تلویزیون‌های جدید و مدرن در سطح شهر مشهد برای اطلاع‌رسانی و پوشش مناسبت‌های ملی و مذهبی خبر داد.
🔹
وی اظهار کرد: در جریان برگزاری مناسبت‌های ملی و مذهبی، به‌ویژه پخش زنده مراسم تشییع در نقاط مختلف شهر، این زیرساخت‌های نوین توانستند نقش مهمی در انتقال سریع، گسترده و مؤثر پیام به شهروندان ایفا کنند و امکان همراهی افرادی را که امکان حضور مستقیم در مراسم را نداشتند، فراهم آورند.
🔹
مدیرعامل سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی شهرداری مشهد افزود: استفاده از این تجهیزات هوشمند، در راستای ارتقای نظام اطلاع‌رسانی شهری، توسعه خدمات نوین و تحقق مؤلفه‌های شهر هوشمند انجام شده و گامی مؤثر در جهت افزایش رضایتمندی شهروندان و تقویت ارتباطات شهری به شمار می‌رود.
ویدیو
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/669853" target="_blank">📅 20:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669852">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0bd0a5a77.mp4?token=PxxIJYYpQquSJyDna0Gf2_tPDmysFjAIIF_S5h3NG_vkIpdo3IHSNO4-DcebP0-oiSM7hnL0aHJvEVxNc7fIDDR5MKXxlCBP_-Vt6Sqr31k45MlKkKdgIrGb12XFpsTcxm5OQrGDbSfzvONUyKPoj2O7tXz1uyck7VgbtHTjoBtt66a-jDnaoGnNr3X16Pq2tPQCJq9hIFQrrOzKii2AKAelSRQSUwrJlKL-0A_pIITbJYWZHW3QClMBY9p5dwgr43aH4WmINOmkgmxvpEYGvaxV77y4QcA6EbcQc2c2OHs5-HhM1BNQLxxdKh1KoxNYDmrm-MXabE4aAbsf1B2DeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0bd0a5a77.mp4?token=PxxIJYYpQquSJyDna0Gf2_tPDmysFjAIIF_S5h3NG_vkIpdo3IHSNO4-DcebP0-oiSM7hnL0aHJvEVxNc7fIDDR5MKXxlCBP_-Vt6Sqr31k45MlKkKdgIrGb12XFpsTcxm5OQrGDbSfzvONUyKPoj2O7tXz1uyck7VgbtHTjoBtt66a-jDnaoGnNr3X16Pq2tPQCJq9hIFQrrOzKii2AKAelSRQSUwrJlKL-0A_pIITbJYWZHW3QClMBY9p5dwgr43aH4WmINOmkgmxvpEYGvaxV77y4QcA6EbcQc2c2OHs5-HhM1BNQLxxdKh1KoxNYDmrm-MXabE4aAbsf1B2DeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی تکان‌دهنده از واکنش مردم تشییع‌کننده رهبر شهید انقلاب در قم
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/669852" target="_blank">📅 20:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669849">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgpxXe3ASx07YQaxslhyXCAOj1Cr84v0nNiZaO__6oWfjxjSdntIx102KuQY5BWUGWga-VJER38_qfDoT4OBa1h1-xH3RtCQuPXy9Ek_x0ig45f9KA410HFVH0-v6ElMn8HuMPHERYUi5VeO1N2qYg9ARZp76Ej02CXpDgw4ywhSDRk8OcA4BX716xOB4BbsMh7od_FWJ94fqhQJ0YdDErhkap-s5aceVuhBM3V3tppL8aF8AZSz3IxIQZP4TABB1jWv_TXwX308ltBbfKPLRzO7CZa7r_ntKwdtZz0eie-vr3QZSyDkFHILUMwalvz68c3XpXbUyz9X_ZW5bCypNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sViK7Wj0QTzqyE1NIcX9kU1OV4M6UvNK4DDog2FAHybDrOPPGflKt7Cqt89w76fMglQwHZ0kymKUkiPyi-yC3Ma4qgxBQoxEh1KKM3VwluzzqiJLXqang45auvGojwTfv5VSb_gIDRFhR5b9yKeZwshZaAC5TGvoRPrNLS3lCaYRkVf3l8cJteerh2z0wo8Uj2_lt7FJ-a1BGido20fxFcxce2MKzmK7Z-fJNtmFEGALxoKlS0Q2MA7ajduBaBsRjoEove9YnzKpJNHD8JncPHyNBsF96Utpu0rKcdip-4CVxFdnZ7wXiMNlq-91nWPpETlGRPnyYZfNBTz3KKTpmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر از زندگی خسته‌ای، قبل از هر کاری این کتاب را بخوان
🔹
«زندگی در پیش رو» شاهکار رومن گاری، داستان پسربچه‌ای است که در کنار زنی سالخورده و بیمار، معنای عشق، انسانیت، فقر، تنهایی و امید را یاد می‌گیرد. رمانی که هم اشکت را درمی‌آورد، هم لبخند روی لبت می‌آورد و تا مدت‌ها رهایت نمی‌کند. این کتاب برنده معتبرترین جایزه ادبی فرانسه شده است.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/669849" target="_blank">📅 20:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669848">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkVlrMCVr4tmR2yPfP5nUjgnXONknlyXs5f9KYWLuyAScGaYI5sHKlQ5484RQqI8OTgxOAZMK7RFCBilNa9RTbn1NbUCmJpSjy92Prw77xd8h193i8F3wMZwPyU6i6NjhDiz7ABDVMj2lrMOe1vXwKLE9SCjIbs9MFo8QUdFD-6jME3m11I_bi1DZrq9utcRtREkIi_wj4aeaPF1BOr36Z5BBfBBxiVr2Pbl1_t0fYxPF3D_PgyMVMnL-yqx41cagHva7BuaiNXAovAkjuewNgSdkcygfTkgj_JUGupCA-X1Ytu-VkqRU2DwmPUWo6gmHgEhGTK_a4LOyP5omSD03Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز با ۵ میلیون شروع کن…
فردا با سرویس عروست بدرخش
🏦
بانک طلا بدون سود و بهره
👰
مناسب خرید تدریجی سرویس عروس
🔄
تعویض طلای سالم با محاسبه عیار ۷۵۰
📲
جدیدترین مدل‌ها داخل کانال
https://t.me/haghgo_gold
ادمین :
@haghgogold
_
__
آدرس شعبه ۱: ستارخان بین فلکه اول و دوم صادقیه پاساژ زرناب طبقه همکف پلاک ۳۲
شعبه ۲: فلکه اول صادقیه زیما مال طبقه B1 واحد۴
برای اطلاع از موجودی تماس بگیرید :
09924100036  ---  09924100039</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/669848" target="_blank">📅 20:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669846">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f955e91b2.mp4?token=TVehj3RQ3HjdNH4flzz2-3jCdTDzXcbTkyVQZ3qlLNmUOfrKWlRWLyjVI9s_o39sojB5VVA8i2Pdyi4xtz-SWyCe5OpniFngU67BXUjQjQxmnDLSDzrWWt4SiwdBTFT6eAvxSwF1_yznztlce8e_4W1f2IXuBbZL-0PVQ0S8JdQwc1TNR_0Nkbi5sf65vkI2VBMS4ftHtBhIiEEqVtype0HCiQE-_KPjQfbUIjFWkzveUBAspcCml4phTeDNjjBNlehIEeEfh2gAqmXfNsS2V1kGMDVNLPnNUp1ZIGnoHcVv8SZvPoaq943ZA4h7EeyjGD65fGkPqvg0ozOj4SYlLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f955e91b2.mp4?token=TVehj3RQ3HjdNH4flzz2-3jCdTDzXcbTkyVQZ3qlLNmUOfrKWlRWLyjVI9s_o39sojB5VVA8i2Pdyi4xtz-SWyCe5OpniFngU67BXUjQjQxmnDLSDzrWWt4SiwdBTFT6eAvxSwF1_yznztlce8e_4W1f2IXuBbZL-0PVQ0S8JdQwc1TNR_0Nkbi5sf65vkI2VBMS4ftHtBhIiEEqVtype0HCiQE-_KPjQfbUIjFWkzveUBAspcCml4phTeDNjjBNlehIEeEfh2gAqmXfNsS2V1kGMDVNLPnNUp1ZIGnoHcVv8SZvPoaq943ZA4h7EeyjGD65fGkPqvg0ozOj4SYlLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین ایرانی که از کشتی‌های خارجی خلیج‌فارس برای عبور پول گرفت، البته قبل از آن پدر و برادرش که مظهر سازش با بیگانه‌ها بودند را کشت!
🔹
ویدئو کامل این روایت تاریخی
👇🏻
https://youtu.be/PkNQz2D9nTY?si=rMrFwnFbp7hcL5r5
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/669846" target="_blank">📅 19:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669845">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvfDjv6xD31a5CN3t76mDkJsh7-zkW5P-NISuYPI6DSf1PqniD7-jeaXidRQ_Rol2X_uU87n4PKAKwIPyUYmD1dV7fifYtjEXLCHCyQcwQ-odLlUTS_H80eW3NgqDDX7bhFP1FDu38DTLPVzfV_tQJ5TNjpP7wXqAP5N5oi20gDkl1_HANp-f1jyDwBoJ1qLYD7j7lkRJ1i_O9HvQsV9A0YI5gIPRWPdGO9hZi2ZVEfanY-yjKac0eNn7nJF_cinGGRWraF_YL7bdAAkFVcbyN6jnpdzXfcnbfimil7f1HFVi8SSsC3-FpPc7qYsU2q32qWPkjZL2ISL6f-KAQ28OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ بیکاری ایران در ۳۴ سال گذشته
🔹
نرخ بیکاری ایران در سال‌های اخیر به حدود ۸ درصد رسیده که نسبت به میانگین تاریخی ایران (حدود ۱۱ درصد) پایین‌تر است، اما در مقایسه با بسیاری از کشورهای هم‌سطح و درحال‌توسعه همچنان بالاست.
🔹
بیشترین افزایش نرخ بیکاری در دهه ۸۰ و اوایل دهه ۹۰ رخ داد؛ عواملی مانند ورود موج جمعیت جوان به بازار کار، رکود اقتصادی و تحریم‌ها باعث افزایش فشار بر اشتغال شدند.
🔹
پیش‌بینی‌ها نشان می‌دهد نرخ بیکاری ایران در سال‌های آینده احتمالاً در محدوده ۸ تا ۹ درصد باقی می‌ماند.
@amarfact</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/669845" target="_blank">📅 19:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669844">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_n0O5zdBtDWF_4p1Vb0VlyM0sU5BQNebPK_L_wXUxpCSotNmd0wLMfeerCrSwQY4XMZSryS-KKGFPp-PV1LtbVYaeK8YEE69K5r9c9l8ErkzdI5peD1oqt64nBAjP6f2g0NVjO68xypI6MtNhIrZdjZKBcE4OvbxOkPsZLoCjOkjpTnuvl6mxL7gNVgofUnL3-VIMKWCnEMswce8_cYYDecrjBrj40HSkgTnCMDW2nPPJ8YXPGV5sanlAuq-CW1QewtVRGQiHaJLwD0y9KOw9ELMscQvmCmVdIyHOSQLGNHxNhU6ioHuww8FkvE3Bnu5qsNr97OytQ8_EH-GHam6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تبادل نظر عراقچی با همتای عمانی خود درباره اجرای ماده ۵ تفاهم‌نامه اسلام‌آباد
🔹
سید عباس عراقچی وزیر امور خارجه جمهوری اسلامی ایران که صبح امروز شنبه در راس یک هیات سیاسی-حقوقی به مسقط سفر کرده است، با سید بدر البوسعیدی وزیر امور خارجه سلطنت عمان دیدار و گفتگو کرد.
🔹
وزیر امور خارجه کشورمان از پیام همدردی سلطنت عمان و حضور رئیس مجلس این کشور در مراسم ادای احترام به مقام رهبر شهید انقلاب اسلامی تقدیر کرد و بر اهتمام جمهوری اسلامی ایران برای تقویت مناسبات دوجانبه ایران-عمان تاکید نمود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/669844" target="_blank">📅 19:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669843">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
سفیر چین: چین دو بار پیش‌نویس قطعنامه مربوط به تنگه هرمز را در شورای امنیت وتو کرد/ در دیپلماسی چین، به‌ندرت از حق وتو استفاده می‌کنیم، اما هر بار که وتو می‌کنیم، تصمیمی بسیار جدی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/669843" target="_blank">📅 19:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669841">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e16b99c1.mp4?token=qNKwfTlutPpnA2pKU8Znh3zi9HDZhaFcw4QYQsPlBqTTN6bCVkgEjZsK-Bfl484JBeDtnYWYBTXOi-VImU2lU7f05x_uqL662QnUwyNS0nnk3EJ9X80DGvksfLt2RsvpP5iarvDdFFkh2MbDl9QE0OP2PPD3VYPhC-EhTrjyHZk0TBXrjXHcrrUiXQ036WxdRHQGsabL8KdI904dMR_-xSY7_R0gdg7h5dpji98OKIwZn016quxJqfAOhFrlUWaNENZFB-BhzdGknqwuq2Tyj7N22KPrfUz5MYsSH5IgZjN1Sbmtvuzp7ZNV2M0WDss-YMrAtJO7kkOHWLt67KFnaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e16b99c1.mp4?token=qNKwfTlutPpnA2pKU8Znh3zi9HDZhaFcw4QYQsPlBqTTN6bCVkgEjZsK-Bfl484JBeDtnYWYBTXOi-VImU2lU7f05x_uqL662QnUwyNS0nnk3EJ9X80DGvksfLt2RsvpP5iarvDdFFkh2MbDl9QE0OP2PPD3VYPhC-EhTrjyHZk0TBXrjXHcrrUiXQ036WxdRHQGsabL8KdI904dMR_-xSY7_R0gdg7h5dpji98OKIwZn016quxJqfAOhFrlUWaNENZFB-BhzdGknqwuq2Tyj7N22KPrfUz5MYsSH5IgZjN1Sbmtvuzp7ZNV2M0WDss-YMrAtJO7kkOHWLt67KFnaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله به تروریست‌های ضد ایرانی در سلیمانیه عراق
🔹
مقرهای متعلق به تروریست‌های تجزیه طلب ضد ایرانی، امروز شنبه، هدف حمله قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/669841" target="_blank">📅 19:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669840">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqEaPavwne63C7IpJlrivDxhbtTq7jozlEx0I6lWjFt-_4KWC0LDlCrYa5XrZEg3puLstlr_HpZGIqqn2wGvpoBTyEGBBg8g0LfattTT2K2M8ujh4l9kR4_j1-n2FN2VvPmPijD09XKjMNPD2XrNm7VVIdE5Fe2mRQMnsJ63Honl6gWIw5nUXP4uDnnhH4sbx_ayshOyK8Ks3bGcPZ4zZYh_98c5yrnRy2FxtkUsqGjCtdp-lQ1k6D3zVf8Hi4vSs8EGuUailq60Xvwnt9S0I8sljDz4XokRkyctvYSFjlIUuP1hdSZnkinU2zJCxrCHiKFcytwciXAihDpFgUk87w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عهد انتقام
رهبر معظم انقلاب اسلامی در پیامی به مناسبت تشییع و تدفین رهبر شهید انقلاب فرمودند:
🔹
اکنون به پیشوای شهیدمان عرض می‌کنم، عهد می‌بندیم که انتقام خون پاک شما و همه‌‌ی شهیدان این دو جنگ را از قاتلین جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملّت ما است و به‌طور حتمی باید صورت بگیرد. این جنایتکاران که فهرستی از صدر تا ذیل‌شان موجود است، آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد. آن‌ها باید بدانند که این امر، متوقّف بر وجود شخص من یا سایر مسئولان نیست. ما باشیم یا نباشیم، این مطلب محقّق خواهد شد و بزودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این مأموریت الهی را انجام خواهند داد.
🔹
هشتصدوششمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/669840" target="_blank">📅 19:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669839">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
اروپا برای اینستاگرام هشدار صادر کرد!
🔹
کمیسیون اروپا به متا هشدار داد در صورت اصلاح نکردن قابلیت‌های اعتیادآور اینستاگرام و فیسبوک، این شرکت ممکن است تا ۶ درصد از درآمد سالانه جهانی خود جریمه شود.
🔹
رگولاتور اروپایی خواستار غیرفعال شدن پیش‌فرض قابلیت‌هایی مانند اسکرول بی‌پایان و پخش خودکار، ایجاد وقفه‌های مؤثر برای کاهش زمان استفاده و اصلاح الگوریتم‌های پیشنهاد محتوا شده است تا از وابستگی بیشتر کاربران به این شبکه‌های اجتماعی جلوگیری شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/669839" target="_blank">📅 19:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669838">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9571b6ead8.mp4?token=gCSPy2Uc49scrrJ7pZ7aw_5WESWX09DWGNbOuNWDgPLjDx1dRse4c8JhFj6ZsGzHIWxv4KL254Gb8tY-xP8l5UFPBPRMijQ-3R8F1uWikXEwihaVzZe5643vxPAcTjHIRzvNU5T15whhXuwkHDXZH8SK3twHy7ezZTpkRHxyXW6Qz2KcnIHOp8rqKYNVnhGnLQOcC8Lc9xLiCSLva-Osr853-MDCZLY6WrRrTnZ11Scy0igjF3Wev_bK3bnoMUA8SwoZrW519_eQU2ImaooYNAVKFKLv-hZ5KiOiPsXZzrDXKeaxx7QDrjfkA9rpcoCBaa8UrPTO0QtX8tN05jKXWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9571b6ead8.mp4?token=gCSPy2Uc49scrrJ7pZ7aw_5WESWX09DWGNbOuNWDgPLjDx1dRse4c8JhFj6ZsGzHIWxv4KL254Gb8tY-xP8l5UFPBPRMijQ-3R8F1uWikXEwihaVzZe5643vxPAcTjHIRzvNU5T15whhXuwkHDXZH8SK3twHy7ezZTpkRHxyXW6Qz2KcnIHOp8rqKYNVnhGnLQOcC8Lc9xLiCSLva-Osr853-MDCZLY6WrRrTnZ11Scy0igjF3Wev_bK3bnoMUA8SwoZrW519_eQU2ImaooYNAVKFKLv-hZ5KiOiPsXZzrDXKeaxx7QDrjfkA9rpcoCBaa8UrPTO0QtX8tN05jKXWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشیش و فعال سیاسی آمریکایی: ترامپ هیچ قصدی برای عمل به وعده‌هایش ندارد. از چه زمانی بزرگ‌ترین شیاد تاریخ به قول و قرارش اهمیت داده؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/669838" target="_blank">📅 19:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669836">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قاضی‌زاده هاشمی: پس از بازگشایی صحن، موارد استیضاح وزیر نیرو پیگیری خواهد شد
احسان قاضی زاده هاشمی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
قطعی برق بدون اطلاع قبلی قابل پذیرش نیست و باید طبق برنامه انجام شود.
🔹
استیضاح وزیر نیرو به عملکرد یک‌ساله این وزارتخانه در حوزه آب و برق مربوط است و پس از بازگشایی صحن مجلس پیگیری خواهد شد.
🔹
قیمت بالای برق در بورس باعث شده برخی صنایع به جای خرید برق، فعالیت خود را متوقف کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/669836" target="_blank">📅 19:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669835">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90b9c1628f.mp4?token=vj_P-T4YKa0LR8HcdLYoW6ySipNekG2cRhD896Mpeg31PBCu8PDjfXw9WmPrTWgI4z40ztVlmXRuRZiQwkGUVvMFDexcRj7PV6Zp3pqeIiJtNkkTz3jIR9mEB5WoPCuFyiQ7OAbIo03B5dQqtWFFtEadH8nYmsgD6Y94RhFsnBUqUdPZIm0onDS3oYZ8To9khSgfeMANxvRNC_m6oIoFPnlvMNiE10yH7xCaO3hHYc3DenJnc90eAEoOj3pn2A0k2rmT2w98G6peWX2W-C2eAEeaVSJu84kqInn2c9JIUN8t-ZO6BstR2gtL6tHBpVVPRmdpwRatWTbF46W9IjJQrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90b9c1628f.mp4?token=vj_P-T4YKa0LR8HcdLYoW6ySipNekG2cRhD896Mpeg31PBCu8PDjfXw9WmPrTWgI4z40ztVlmXRuRZiQwkGUVvMFDexcRj7PV6Zp3pqeIiJtNkkTz3jIR9mEB5WoPCuFyiQ7OAbIo03B5dQqtWFFtEadH8nYmsgD6Y94RhFsnBUqUdPZIm0onDS3oYZ8To9khSgfeMANxvRNC_m6oIoFPnlvMNiE10yH7xCaO3hHYc3DenJnc90eAEoOj3pn2A0k2rmT2w98G6peWX2W-C2eAEeaVSJu84kqInn2c9JIUN8t-ZO6BstR2gtL6tHBpVVPRmdpwRatWTbF46W9IjJQrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دفتر رهبر مسلمانان جهان، یک چفیه و یک انگشتر متبرک رهبر شهید را به پسری اهدا کرد که پیراهنش را بر روی تابوت ایشان در مسیر کربلا انداخت. این پسر اهل شهر تلعفر عراق است و با تلاش‌های انجام شده، پیدا شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/669835" target="_blank">📅 19:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669834">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
طلا در بازار چقدر حباب دارد؟
🔹
بازار طلا امروز شاهد جهش عجیب حباب سکه‌های خرد بود. سکه گرمی با ۲۷.۹۸ درصد و ربع سکه با ۲۲.۴۴ درصد بیشترین رشد را ثبت کردند.
🔹
در مقابل، حباب سکه امامی ۲.۶۷ درصد و بهار آزادی ۰.۸۶ درصد افزایش یافت. حباب طلای آبشده هم منفی ۰.۴۰ درصد شد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/669834" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669832">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
روایت شنیدنی“سیدمحمد سادات‌ اخوی” از زنده‌یاد حاج آقا فرشچی در برنامه «پشت جلد»؛ مداحی که احترام به همکاران را در عمل معنا می‌کرد
🔹
او تا پایان نوحه مداح قبلی پشت در می‌ایستاد تا مبادا حضورش باعث استرس یا برهم خوردن تمرکز او شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/669832" target="_blank">📅 19:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669829">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTzNP7nlL9gmw46fHI3pUHdSKfd7S-P5n-IGWzos-TwT_p0tuz5Mi-NrR4BAXReQbYP5VUYuuAesJKLEGFtEE7RGdhPVyfO5AL9zjgnVvXhoE0JSVrRD0Ak0MyjsRiyKUYAp_ZItJmJXY7EmdgRqP8v4zqjHeUi1JqRQJNDL69DGoPQTCec2ORHk4TZBsHQypvg-ZFGs72s71xu4z7eHAWpK3uky7kzCrTV73nY_AYDQkGpkmdH0xPK0d8RAd9htG8pqx9Xff5gZez-0zZWP_RUu6eDpyXBFsGN6V6rQOcx06tMFDL1qEmzRhBIJ2Bti61g91EHhRXJZizswpdngiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/669829" target="_blank">📅 19:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669828">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVB3O5CZDppv6w-_Klgt5YbZZc-xKEjQN5eyVaXwr1vf67S2QPc1ZiY9iopEv3ZIxxrUrcuSfux6oaTU2dQJeJfnz6n16UDpQ0ZanMm0wEghCg9tolXSlMuqZ-2AD4vTcwTQX5mV0jUmUx8Den8_PInEzoWkCXDFU1qIv8Hjgj4dV3_q5IbM85lvvZ0GKMcF8fTxnv43-HwVv4RtUVYN2mHmxoSmdRGt6KyuGYk-KJIK5CIngNBQtujO2OlClYR7j1uzL-26e1Mzv2RyXJAgq0bCAyhkpYaSA20WImkmFF_rUrnlRY6f7n97DDh-3V-Z_VzePNc6HuJZTnywiH1LFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏨
اقامت لوکس در هتل ۵
⭐
سی نور مشهد با تخفیف ویژه
✨
فقط برای مدت محدود:
✅
تا ۴۰٪ تخفیف واقعی روی انواع اتاق‌ها
✅
اقامت ۳ شب، شب چهارم رایگان
✅
صبحانه، های‌فود و فولبرد
✅
ترانسفر رایگان از منزل در تهران (شرایط ویژه)
✅
استقبال فرودگاهی و راه‌آهن
✅
سرویس رایگان رفت‌وبرگشت به حرم مطهر
✅
شارژ اختصاصی خودروهای برقی
🎁
ظرفیت اتاق‌ها محدود است و رزرو با این قیمت تا تکمیل ظرفیت انجام می‌شود.
📞
همین حالا تماس بگیرید و قیمت ویژه را استعلام کنید:
☎️
مشهد: 05132021021
☎️
تهران: 02144673863</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/669828" target="_blank">📅 19:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669827">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
اکسیوس: ایران و عمان و قطر در حال بررسی بیانیه‌ای احتمالی در مورد بازگشایی کامل «خط میانی» در تنگه هرمز برای تردد کامل و آزاد هستند
🔹
به گفته یک دیپلمات آگاه، مقام‌های قطری نیز در مذاکرات میان ایران و عمان در مسقط درباره تنگه هرمز حضور دارند.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/669827" target="_blank">📅 18:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669826">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e2222860e.mp4?token=vPqZ6-BKBj0rUt9qgYyPFFofCHUSmzzdr6Iw7cgtBirr_Fdaaxqtr9adUKh3M3hC0NWSJkRD58LRw3eK-_y8err56WGTy4SlOrjBb7ktn9GSsIOyvozUHgW2A2Q85tK_DPPqW1ldeXqPotjYSPs8MQ-3_TZGNovIUOvKsMd8zW_0xuVJkmbzEF1Z5dX4HzRUJ64Pqu31wQbDyWD88cWbCUHiNZ6b4r34mAJ491wdPxcTJKjW2bSRvCKNmX6YyPZvRa6mwNAaPf66v4rjYWbqJA-HrMkTXAn3W98uXSyl2oQzxkw5Z4Mbs-mmcWC0Jdh0HQcO6AHuFKvr8GD8cMmE4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e2222860e.mp4?token=vPqZ6-BKBj0rUt9qgYyPFFofCHUSmzzdr6Iw7cgtBirr_Fdaaxqtr9adUKh3M3hC0NWSJkRD58LRw3eK-_y8err56WGTy4SlOrjBb7ktn9GSsIOyvozUHgW2A2Q85tK_DPPqW1ldeXqPotjYSPs8MQ-3_TZGNovIUOvKsMd8zW_0xuVJkmbzEF1Z5dX4HzRUJ64Pqu31wQbDyWD88cWbCUHiNZ6b4r34mAJ491wdPxcTJKjW2bSRvCKNmX6YyPZvRa6mwNAaPf66v4rjYWbqJA-HrMkTXAn3W98uXSyl2oQzxkw5Z4Mbs-mmcWC0Jdh0HQcO6AHuFKvr8GD8cMmE4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند می‌گیری درسم رو پاس کنی؟!
🔹
کلاس‌های مجازی فقط شیوه آموزش را تغییر ندادند؛ یک بازار پنهان هم ساختند. بازاری که در آن بعضی‌ها با دانششان نمره می‌فروشند و بعضی‌ها مدرک می‌خرند.
🔹
این ویدئو را ببین تا با یکی از عجیب‌ترین مشاغل دانشجویی آشنا شوی.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/669826" target="_blank">📅 18:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669825">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
مقام آمریکایی: ونس به عمان نمی‌رود/ مذاکرات از راه دور است
ادعای شبکه آمریکایی سی‌بی‌اس به نقل از یک مقام آمریکایی:
🔹
ونس به عمان سفر نخواهد کرد و روبیو، وویتکوف و کوشنر در مذاکرات آنجا شرکت نخواهند کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/669825" target="_blank">📅 18:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669824">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
نرخ خام ولادت به پایین‌ترین سطح خود رسید
🔹
نرخ خام ولادت در ایران برای نخستین بار در حدود ۷۰ سال گذشته به ۱۰ تولد به ازای هر هزار نفر کاهش یافت. رکوردی که از تغییرات عمیق جمعیتی کشور حکایت دارد.
🔹
هم‌زمان، تعداد موالید سال ۱۴۰۴ نیز با ثبت ۸۹۲ هزار و ۲۸۰ تولد به کمترین سطح در دهه‌های اخیر رسیده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/669824" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669823">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA1uyyeRyY0DZBHZwsS4wsQxvZE2532LsNeqze8-Uhbujd7Y508nzW_QAY7dKNrLNwtLbalkMQuQNfFj3WiHjEVCVYnR9U2aR9wAIOMos8E7rROihg47a7AIffVUAF9GeaCT9__afZ4w5L7SZkanQNMiDFX0TpMhX-w_3UCw8sFGX90weugLc82Q2j9ZRxc2B1v1obcb2gpeaQnrz9XhYYWrf3EiZUrmSrCdnL1ItlwAlPK87dJh4OOWlwlCryvM30rKhFFQY7sBXQtp7lPRjbf31HDIO_ro6QBdJUoOUilwa0BnPyG3GFNioEorOSmCogD-m7wxT8A4ePQx7Ut6GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر انجمن واردکنندگان لوازم خانگی: ممنوعیت واردات، راه قاچاق لوازم خانگی را باز می‌کند
اسماعیل ارغوان، دبیر و عضو هیئت ‌مدیره انجمن واردکنندگان لوازم خانگی در گفتگو با
#خبرفوری
:
🔹
از سال ۱۳۹۷ واردات رسمی لوازم خانگی با هدف حمایت از تولید داخلی ممنوع شد.
🔹
اگرچه این ممنوعیت در ابتدا برای مدت پنج سال در نظر گرفته شده بود، اما پس از پایان این دوره نیز با توجه به شرایط کشور ادامه پیدا کرد.
🔹
تجربه چند سال گذشته نشان داده ممنوعیت واردات، لزوما به معنای جلوگیری از ورود کالا به کشور نیست بلکه بخش قابل توجهی از نیاز بازار از طریق قاچاق تأمین شده است.
🔹
قاچاق لوازم خانگی هم به اقتصاد کشور آسیب می‌زند و هم به مصرف‌کننده. وجود یک مسیر قانونی برای تأمین بخشی از نیاز بازار می‌تواند نقش مهمی در کاهش قاچاق و محدود کردن فعالیت شبکه‌های غیررسمی ایفا کند.
🔹
انجمن خدمات پس از فروش با همکاری سازمان توسعه تجارت و سایر دستگاه‌های مرتبط، در حال پیگیری اجرای گارانتی و خدمات پس از فروش برای کالاهای واردشده از طریق کولبری و ملوانی است.
🔹
امیدواریم پس از پایان این دوره سه‌ماهه، ممنوعیت واردات این اقلام برداشته شود.
🔹
باید توجه داشت که واردات از این مسیر تنها حدود ۱۰ درصد از کل واردات کشور را تشکیل می‌دهد و سهم لوازم خانگی نیز بخش کوچکی از همین میزان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/669823" target="_blank">📅 18:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669822">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc2d18097.mp4?token=hEa1thW_bDk1E2EIm7rPZJzwSfTdrmumHLmF5KMxaWR2qDM1z0zcabcv66L8bTOkbrXp19lW2W7Ky74PKb6bDdusStw09jkGkedvnvFCAqQ2BA1d_eiPSl5Xx-lp4j7sVjPdcgblMpyTQzMnoZVtQj2x280XDpP3LbOK12Z0cywHIIqJs5VWc6jim-W_W3Wv1yFZKYnyMy0ZBXzqqyUtkQua59Mi8CtpSL0e4AVTg98uUQqStLb7cheFdO0Rru_BzHPxPJri-ZQVUwGR5u_cXrRnQE428WEJNcFbZGZ4EKc4n_jEiMN9F62JbW4OS9HFQYyff5umSAPvos_DTQ2XVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc2d18097.mp4?token=hEa1thW_bDk1E2EIm7rPZJzwSfTdrmumHLmF5KMxaWR2qDM1z0zcabcv66L8bTOkbrXp19lW2W7Ky74PKb6bDdusStw09jkGkedvnvFCAqQ2BA1d_eiPSl5Xx-lp4j7sVjPdcgblMpyTQzMnoZVtQj2x280XDpP3LbOK12Z0cywHIIqJs5VWc6jim-W_W3Wv1yFZKYnyMy0ZBXzqqyUtkQua59Mi8CtpSL0e4AVTg98uUQqStLb7cheFdO0Rru_BzHPxPJri-ZQVUwGR5u_cXrRnQE428WEJNcFbZGZ4EKc4n_jEiMN9F62JbW4OS9HFQYyff5umSAPvos_DTQ2XVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی مجلس: در تامین امنیت ملی خودمان با هیچ یک از کشورهای همسایه تعارف نداریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/669822" target="_blank">📅 18:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669821">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8463a2e7d.mp4?token=sY5jPuaAL2z1dvUxjdTb6B6wrj8n3VR36cHiZuzZpGxAdtQu9bmTrGM5Ok-n7BPmbdGMjt_18R1c1coCArDUjxq713R46jMIHIAPhkufaNU8F8RAq8fy-H4oY07IAREvhddyQ473WoS3gvR_kBCkM2HK-juDT_hWANNk4bDdHortEUDDPuzV6QxYpIjdOvQCDJE5pd_CYOITAHtmxGdv-ZVqcUhwntPsTbv_U8y30Vue87kIf5v6YWZF9I3Mqm63yAXakw-pHLmAGnU7zpXOwV43fkiMGSLFW-PGUJtVC-svKpkaxZG_2vnuDEger8sZHzY-zGFEPZyoljU15fminQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8463a2e7d.mp4?token=sY5jPuaAL2z1dvUxjdTb6B6wrj8n3VR36cHiZuzZpGxAdtQu9bmTrGM5Ok-n7BPmbdGMjt_18R1c1coCArDUjxq713R46jMIHIAPhkufaNU8F8RAq8fy-H4oY07IAREvhddyQ473WoS3gvR_kBCkM2HK-juDT_hWANNk4bDdHortEUDDPuzV6QxYpIjdOvQCDJE5pd_CYOITAHtmxGdv-ZVqcUhwntPsTbv_U8y30Vue87kIf5v6YWZF9I3Mqm63yAXakw-pHLmAGnU7zpXOwV43fkiMGSLFW-PGUJtVC-svKpkaxZG_2vnuDEger8sZHzY-zGFEPZyoljU15fminQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر منتسب به محل اصابت موشک
‌
های ایرانی در پایگاه راهبردی آمریکا در اردن
🔹
این در حالی است که پیش از این منابع آمریکایی و اردنی مدعی شده بودند که تمامی پرتابه‌ها رهگیری و منهدم شده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/669821" target="_blank">📅 18:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669819">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522b497bdb.mp4?token=devk4wlPDAZxDFbWrjihHGPAYfHJoENcboTTbggY_i9LoLdQAiIliOGPLPPX26EhERwyQrviGoLr6QI30EeqF1PVvZ6CfaS7TrqaXO0YcJyk8TAnkf1kUIbTYUwQuRbED6VD_2zoIVf0p2wj6AjLu-TZ7QGPLQQo7JKMI3SfQBp46o82rcr-BfY15pr_XnYSAryMQtbweG-IwVa1f5w-m8h3LktWJzOfzgZAUY5EABC-tgw8lz_C1AH2nuw4RaILceOfOLUaaGIj4ngD91Z9_hd1Q_mfUkQUCjmHC-tbMKON-5VxGciDlKC3f07mgnTmmiMFyQnS1jASfI24jq2rQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522b497bdb.mp4?token=devk4wlPDAZxDFbWrjihHGPAYfHJoENcboTTbggY_i9LoLdQAiIliOGPLPPX26EhERwyQrviGoLr6QI30EeqF1PVvZ6CfaS7TrqaXO0YcJyk8TAnkf1kUIbTYUwQuRbED6VD_2zoIVf0p2wj6AjLu-TZ7QGPLQQo7JKMI3SfQBp46o82rcr-BfY15pr_XnYSAryMQtbweG-IwVa1f5w-m8h3LktWJzOfzgZAUY5EABC-tgw8lz_C1AH2nuw4RaILceOfOLUaaGIj4ngD91Z9_hd1Q_mfUkQUCjmHC-tbMKON-5VxGciDlKC3f07mgnTmmiMFyQnS1jASfI24jq2rQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ هوشمندانه به بی‌احترامی؛ سکوت یا مقابله؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/669819" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669818">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVYIv3AMkExYTnCLvFpBpSVpgsNbfAmLYVR7AtLdfhJ3Pq8b0wXXH8lvBNkuxrDUy6AOe8T86ykraW9p9OlGVO8lhS2LodD1wHT3TNQC0ZQNMUnDfwf-1MUQaA-K9e3JHjo7Jo3yL-GHWUVbVathX-vFW3crswoeSfX92MQfc0J4xtZSySvtq6cWzt8OkRUhJL3fuWncZTx9XSOt2D392MQyz7N7YXtvor_Ejp3JrI8MDYme7JkV90j8RTIR1bH6pDi2PwHCXoYP_hZ9WvbcaH256xRexxNkS0n3c8i8rdAPF5lvN7eqZsngFZAHrvhQbMBnzRHFVpRGh0yXgESbOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
ارائه ارز اربعین از سوی شعب منتخب بانک شهر
🔹
فروش ارز اربعین در شعب منتخب بانک شهر آغاز شد و تا هفته اول مردادماه ادامه خواهد داشت.
🔹
به گزارش روابط عمومی بانک شهر، فروش ارز اربعین امسال نیز همانند سال گذشته به صورت دینار عراق انجام می‌شود و نرخ آن بر اساس نرخ اعلامی از سوی بانک شهر خواهد بود. بر این اساس، به هر زائر واجد شرایط، تا سقف۲۰۰ هزار دینار اختصاص می‌یابد.
🔹
در راستای ارائه خدمات هرچه مطلوب‌تر به زائران اربعین حسینی(ع)، بیش از ۱۱۰ شعبه منتخب بانک شهر در سراسر کشور مسئولیت عرضه ارز اربعین را بر عهده دارند.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/669818" target="_blank">📅 18:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669817">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_6yArVzkaBKElqJ0WtGKIZV8v1HeVACdzlb8SNq0WEb4LGlucIulldbZygAVmI-yuy2l-MNBA1_lKEoD9MgpHn5w2p3AFBDTeFSvAn8PzzKEzZNLz9zYC2LQgVOUG007zozkihErHgk2VDiPzAroEcls6E6Bq5fsSl2DmDDQta4u7lFQHNEYvD-u3oqD-bx9ky0o94_rcO9-Ji7r9-3e_QVvtZBWpVvf8Foo0qzxN0LQcXQEgQQRI-mVhHNseJF4urWxbsD00olG9R2bBO6FlGFGFIvBbJNZyNInVqvJhRFofMaLGhLT44PPRYNEPJEKjc_bux2te6Yw1toBru5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکسیوس: ایران و عمان و قطر در حال بررسی بیانیه‌ای احتمالی در مورد بازگشایی کامل «خط میانی» در تنگه هرمز برای تردد کامل و آزاد هستند
🔹
به گفته یک دیپلمات آگاه، مقام‌های قطری نیز در مذاکرات میان ایران و عمان در مسقط درباره تنگه هرمز حضور دارند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/669817" target="_blank">📅 18:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669815">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
شیطان زرد به ونس و روبیو دستور داد تا مذاکرات با ایران را ادامه دهند
🔹
شبکه تلویزیونی سی‌بی‌اس به نقل از یک مقام آمریکایی که نامش فاش نشده گفته که «ترامپ به ونس، دامادش جارد کوشنر، استیو ویتکاف، فرستاده ویژه و تیم او به رهبری روبیو دستور داده است تا مذاکرات را ادامه دهند.»/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/669815" target="_blank">📅 18:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669814">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4c472c476.mp4?token=aKdWreYfHdRcePAS-EwJCb-w9HQI68yh3hImng7i3wo-2jcTWu0iGESnCXS6OM8pOeI-2nBYKmF_eZuHFN23E1alzmjjpNPy-9WO9igY0Ilv7xzB4Hv3-OjBWubEDIo3ITNAmqbCAp2vBKO3meC8-l_QU35N0f3_fRfqfAay6ybnnPovw02xAmkqc9lPwJiRjnVUkK5Bor4an7YNmZOIr8JQIUE0pb5NLpaeozjLx4TMU-8QOefWPidLog12O59YNLNbA-ETRzdhOhIG0aud1K44JXy58ITBvK0273C_wfmqPQBeGp_oRGop2V1Hk4iWmny-nXQsA3L0IsBwIEHhxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4c472c476.mp4?token=aKdWreYfHdRcePAS-EwJCb-w9HQI68yh3hImng7i3wo-2jcTWu0iGESnCXS6OM8pOeI-2nBYKmF_eZuHFN23E1alzmjjpNPy-9WO9igY0Ilv7xzB4Hv3-OjBWubEDIo3ITNAmqbCAp2vBKO3meC8-l_QU35N0f3_fRfqfAay6ybnnPovw02xAmkqc9lPwJiRjnVUkK5Bor4an7YNmZOIr8JQIUE0pb5NLpaeozjLx4TMU-8QOefWPidLog12O59YNLNbA-ETRzdhOhIG0aud1K44JXy58ITBvK0273C_wfmqPQBeGp_oRGop2V1Hk4iWmny-nXQsA3L0IsBwIEHhxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پدر رهبر شهید انقلاب را بیشتر بشناسید
🔹
آیت‌الله سید جواد حسینی خامنه‌ای، فقیه نامدار و از مدرسان برجسته حوزه مشهد، افزون بر جایگاه علمی در شکل‌گیری شخصیت علمی فرزندشان نیز نقشی ماندگار داشتند. ایشان استعداد رهبر شهید انقلاب را از همان سال‌های نوجوانی ستوده…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/669814" target="_blank">📅 18:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669813">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RK3eEYu0xavSCAx3i2On6YcuEExzRP48QFRiCxYLnYfHwgtaxSRzR1gcfXoGkncj-VrjkNwFaJtBv6uxrejnNZXgVagxcDOsJTj5aXyt0qH008MfXVyMbobXVlBKyW7Gyraa-aRewiLcdw1UoX1SzI8D0RKZ0ZUztoEO2zs64T8YilTIWEoJdofjj_Tsya7wCAA-2lTigJ-lF6nsDUhI_UItNLlVs8MQ4wDfPVjkxkp51ySntv0iKuluueX0NDZ2gRKAV_HLepRnx7yJCtPJCeA2ltA96zn8yBi1ioyRRu28KtH3DZVAPyc_BHIAaJgzqm2q1dj0ALEgOXjZi4ZeZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین تحولات در پرونده هسته‌ای و روابط ایران و آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/669813" target="_blank">📅 17:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669811">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYX3rss7pKf6XoQgueuRkk2iheRI7XANW3ZTui_rCYbVVMZx4itwJEL6kieEy15MGjlCIGtnbXjTXaF4eO6nh2a-aN9ch0gemFOnZbJxP6YAZKz24GgLFajciZM95r3DjrGjgmSJdqJkn36XxhR6Grz1YT3NSp7TGl_Vh28KdDn4pE7Kcbe49FXJTD0-tXlFuYEf09qYZMzoj_hJMG6tQCP27aqNnTpPz1-yVA6wPLaoOgYWBZV6AWvU3Vdk_q5Xl5YWkSsylPhfXNYAteTTUr03gsmTunzcZlhLkwKnWfhEzWjNVWz1J6ZvsV8NTTpnt0MbDOuRdPCN58wjBCejJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به چه کسانی می‌توانید خون اهدا کنید؟
🔹
در انتقال خون، سازگاری گروه‌های خونی اهمیت زیادی دارد؛ O منفی می‌تواند به همه گروه‌های خونی اهدا کند و به همین دلیل «اهداکننده جهانی» شناخته می‌شود اما فقط می‌تواند از همان گروه خود خون دریافت کند.
🔹
در مقابل، افراد با گروه خونی +AB می‌توانند از همه گروه‌های خونی خون دریافت کنند و «گیرنده جهانی» محسوب می‌شوند.
@amarfact</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/669811" target="_blank">📅 17:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669808">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-Ob-8ewJlfk_EF-phHpDmFXyfPKEFcs6fpkLJGnjgaikTv6AuuHvWjh_qBv7Wd7FA8HXnUBIElyiB5O0vkZ3qTj0rR1hnR9TzD0QgT6Hr889ykyb79AJccQ9peCXgEZmxBwdNCsWiBo5vegQxn3FMtYItXdpn0D3BNEMT0HntDXFDjuISeI32YMwIbxYuBVrQXwAq9p_ni37OQ-bTraZpl41Kf9Oec5FzJMFs_JcK5shOy9XEVmoyNhKrs1_QOToE-Oxlmv5urvCissuo3Y220B7ghBVLu_YXFN4u81UxWrqLcNUKsFlssy3tCAK6XAZhpk6-aHUoj05O3e17Y54Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار برای اولین بار
دست اتحاد فرماندهان نیروی دریایی ارتش و سپاه برای حفاظت از تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/669808" target="_blank">📅 17:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669806">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قدیری‌ابیانه: برای کشتن ترامپ و نتانیاهو باید جایزه بگذاریم
محمدحسن قدیری ابیانه، کارشناس سیاسی در
#گفتگو
با خبرفوری:
🔹
حتماً باید برای دشمن مجازات تعیین شود و همان‌طور که آن‌ها برای مقامات ما جایزه تعیین کردند، ما هم برای کشتن ترامپ و نتانیاهو جایزه بگذاریم، زیرا دشمن لایق زنده ماندن نیست.
🔹
اگر کسانی که دست به جنایت می‌زنند دچار عقوبت نشوند ممکن است دوباره طمع کنند و دست به جنایت جدیدی بزنند، البته سران کشورهای عربی و حوزه خلیج فارس به غیر از عمان در این جنایات شریک هستند و آن‌ها هم باید مجازات شوند.
🔹
خون‌خواهی از یک سو برای پیشگیری و از سوی دیگر برای مجازات کسانی که دست به جنایت زدند حائز اهمیت است.
🔹
آمریکایی‌ها به هیچ‌یک از تعهداتشان پایبند نبوده و نیستند و حتی برخلاف آن نیز عمل کردند و دیپلمات‌های ما باید در ذهنیت خود و همچنین در انتخاب مشاورانشان تجدیدنظر کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/669806" target="_blank">📅 17:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669805">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxG6obi35SodT1IYbXtg-x_u2zWSapV1cXr01rd5J87OAYhV1rJn0OCG7sHTKph57OZqBJRQBKq4X-fp_0t7k_L6GkECYsi5fWU2yUH8yUc5jj_fwdwryy5iGwt444oi8ZPmhyeyodbU_dIv8jyWhY99G73CkHq7v69P3DjX0ufERwRRUduh3Co2MvN743gprGiohbxuQqMO-wF8TicWwcitwRBJfPuZOwOnC8QCFyUClMfWc31wLMjUg-NmhrI97ifcSfStWSW3EClD9t0MRhCXig0wA4c6vD2jwoM0mVVuymqBB1QSp6A7z2hEpXZyIPbWyWQTWxfV6gJdQzvcoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خودکشی یکی از بازیکنان حاضر در جام‌جهانی| علت: افسردگی!
🔹
«جیدن آدامز» بازیکن ۲۵ ساله تیم ملی آفریقای جنوبی که در جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/669805" target="_blank">📅 17:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669804">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxnoK_G7gy6mBVeyoDePiZHn39v3wxz09X3sC-mWquP7ZyyVXt5bUX3MF3PyQXYErx29FWOWf07v7gPWO3Q9dy_ElivVTatsxo_4fe9C_TW8fuDEc0RLx7SEJf4h51yokeL6VmwtdAyJN0Z4IjooUYFhd9gE5biE-bRiuPztxLj19wp7CRdDO3rO2fNaJ-KZx5iaG7kUmnwPX19Bi4udRGhWv3dUjiot4x6sUkd_-ZYrBjzlSR-TCM1cc6i5PluMmhMBVQ43qptdR-TdM7FWdbR8sXgu_bCzSNW8YNjHNvgYuM55EMVLjsR-Y6HE51TUHILiFfMknyzWU7LptIvVsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ظهوریان در یک توییت، بلاتکلیفی وضعیت مجلس شورای اسلامی را به عنوان یک نمونه آرمانی از آشفتگی اداری و ناتوانی در تصمیم‌گیری کشور معرفی کرده است
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/669804" target="_blank">📅 17:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669803">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
قطعی برق در برخی مناطق تهران
🔹
امروز ۲۰ تیرماه، مناطقی مانند ولیعصر، مطهری و قائم‌مقام فراهانی تهران با خاموشی حدود چهار ساعته روبه‌رو شدند و تاکنون علت این قطعی‌ها از سوی شرکت توزیع برق تهران بزرگ اعلام نشده است.
🔹
پیش‌تر مدیرعامل توانیر درباره احتمال قطعی برق در تابستان گفته بود که به دلیل بالاتر بودن مصرف از تولید، امکان گذراندن تابستان بدون خاموشی وجود ندارد./ ایسنا
#برق_مردم_کجاست
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/669803" target="_blank">📅 17:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669802">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-4GQxjOpTSgqLhQN-0roLbZRnCGaZCjK6N7r58iCsEMEUcdNsEEOW70aic2DTo4Gy8lXI_-KFmpVkfVKmsFwdWJPTWYWMkgoVsxPE9BpC9dvQJfY_i2yY1QzBGLh7JwNIKAptBvtWxYOKyfIGuMn5o1N4_aRrk9ctfQO4YqEopKMZnmB4eHhYyuMkIfcgqnOMr1Nr7zClwXul6JUVpUaLDJDm1QARKPG07ECFWuWKxwgQ5yglPXSQjX3uE0SxcvDpvfphyFD7nU7qRqiNc830sXjoPmfGgLW8A7xFqtKT5rwJXFNyw8ARISOPVPQENaxSTM_05xJGKhc3owrstKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا: توافق با ایران بدون تحویل اورانیوم غنی‌شده ممکن نیست
🔹
شبکه i24NEWS گزارش داد واشنگتن اعلام کرده هیچ توافقی بدون تحویل اورانیوم غنی‌شده ایران ممکن نیست و گزینه نظامی همچنان روی میز است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/669802" target="_blank">📅 17:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669797">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dU2tySBf5KhjD0UwQOtXSBXbvXzmGF3reDSORHYnmtojZo72vQYWihIeKEbdD4ieBZUTaydKAK3eXAGRTDTTqKlfc_w_qQcl7LazKNx7Nk_yDPJjXYaK_FzzD_oXqsts7RqyBMwSIK8wzs_XoUpESxBi_S-kXDDgG2epzWPAQtGDvUJcF4I7YSRKXb8O0puuuHAvAkVxIzH7gWCTDt8b1TqxcEEyGNrlo1SqrlzKfFvRtshSSjEc27O6oCWqTs7AeSlxjFo-0VI2J4k9-jKcaFR0vdUq_fVV9qqupNb9gm_1mcbjKVowHgLrP-2HiQ4mAIe4QDNaU3eiKep8b3KCzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yi7b7NvKfzyjxPyOTpstbE-qhbY4G-oVnXHhnfy-ErMPk9FrCvThdlNz1HeH_emuHVLDp1eyueGF90_e3hdWu2r_SZFPIzmI9IyuePm0x81vaP3sHFX26y5D4v7vwFYUC7JaRgZeBA2dow4m1YkuCxaZUe0VS3ur81cxgVSzWKuESLEG0NrQ4n31zZYk2OnJh9OGyZ95owl_SzQOrjzUVS0regvOVMUvUk7p35R0oyL5gSYY2J1lyDtXE75kgoz3m4MzanN5vJv_G_kVQP0QWVKvAdejObR5aTaQMIZMB_1Kyy2AawXNIwaiDJTHEpfZg8D55EEdTbwH0JIRbbK8HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oTubNk1uTUinOeF-vhCBvG5odFcr-wlxjroDKoeH1C9XrgY8ugIECj0PaPM8EzciZ7srf0EABnWhhRu3dw-0gw-3VZ5doPvaBRkGAb-psfNAFCLpyPQHuwebVSGzSZWTcUkzAT4oSeiInqdYqFeo1s-QvI4p68fXYDr3KfvTlT0FnK_7x7xBPk0gopEy1Iak9vzTStRR6ZCKI1a8MTjJAmfsWr_iBC8JE4y2ylobmzqWrs2maqBznTaH-zLMHwQaKEHns0VEtBYYqka56RMrHp0s3Qkd9m5ZVXTETeJdRiPpU92x74MAspIDU4Icc8LUHJzxsfqds1nkRalHDh6sFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MKp_MuAm49HlNiba9zBG04-o4Pg1ze5SJmAkL55v2tUD1N9SYzBRQ7HJOEktR5LYEuVI_SF7EoZnfZY6AP3Xa374JY2dFUHhMV5b73cx5tH52kSQafiv-4bBnk21zy0NptjuWvGtXt7ojMCPHkJYzDkjagegfMpnnj8V9k9nXmwGt9IeWkry6YTjQCLiPXG7JQWfWjUc7kReO-5midB03-5bakha-ZpScWnBqsuqlGDFY2kICJRsavYKzIHEJqH1RP0Cn4GOkrUqlc5wn45Z2klz0afOlnfo0TkfG5zTKECpqvg_sXynRC9oJNlRHk3G3x6a9Jkdi0I5WOSPZ367HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzzWtFlf8ABZ9u8w-QrHGkrIHUBRmyRHHBI32tyTV0-_wVbbd-bfHwm90XiIoyZrh6wI6DeJTnbXEtMBBQKJfxXBtHF_fTq0msPKP_MiH4YPj_spBgYbVgqsuGUL5Rsn4EigKrKHPJF6FLlsLxgR09OGRS_8fvsCtJZ04ipXtsgErsZEsyVu0O8crr_e3DbT-YIh-FKhQtndcvdVKXCyFBwpw2FsaIRKVRy2G2LqdZNaP6LuQikbGcy1Y6S9Bla8IEbwtLWSWGr1LHWQREHsqIOn264GcELaGFWtr75sdInCMiWFzmr6j3zmRScyhVCVBj7H8VFuIQmtzcK2QI-rXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با این چند روش، در آینده میلیاردر تحویل جامعه بدین #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/669797" target="_blank">📅 16:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669796">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-text">راز یه سرمایه‌گذاری امن و پر‌سود چیه؟
توی این ویدیو، سیر تا پیازِ بیمه‌های زندگي و سرمايه گذاري پروژه‌محور
#بيمه_البرز
رو کامل توضیح دادیم؛
حتماً ببینیدش!
#بيمه_البرز
#چهل_درصد_نرخ_سود</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/669796" target="_blank">📅 16:58 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
