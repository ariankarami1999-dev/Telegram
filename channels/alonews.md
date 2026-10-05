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
<img src="https://cdn4.telesco.pe/file/QDeIvLv3KAu5kkncoJ48Jn__K1Tm3rtzzer5r2MJAVn_eO-E0EzBqDMGJHh3bi6F_XHRgf1EVYrD_Tm4YfjQPBAbfiM4QA7ji7ezkbXXy9Ad0kYlDooYL3PveqMe3KfKtu-QhneeJHbMiBNqjzpo-2I2C1djgZRcC10o_McucTNjLoOxHzT0F1lRKwX0ZnBG-v0yVXcACBszncNNOHHtlYjGdEURDrdZwvFijN2htO6q42jdG0e1CkKos3B3r1cA8G5SkH9Tn-ZdGtWSASPHhVIijjcFZNALFx0HaEI9fbAxA1JHsJPJ4HPZLqZrlIYsMMbWhXRWFcpBgAAa5RCUxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 22:09:04</div>
<hr>

<div class="tg-post" id="msg-151149">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdef78a3d.mp4?token=hPmjyb4pY5betN6uYw-FaTIBUpfIQZ0rXeCSsWSPbO0kzl7I3ysCwkPatXfd_11UxDv9jnVG-XVhrGwwctIGEbCM0WiS9sXD_shMWN-IMOIF_M71NKfqDR55jgPRP7_ZskJuUdbQYSCh-QqufUoowql9n5UhuPyDjqwpkinNitXylvTL4Xgp1oQTCJcT_7pca_87EYTp-V3IzvtElrKDYzIXEJXFlOZ9rykWL7ee7XFYoaMCMJbGDtLhqbhu89QdCXv2s2hvtWpbzvOCP7gVgF24twl8MrnhH0A7C6-Imr508ksyV5oZJTbJ2v1sng26G8sKZjFcDmu1GIMrLtiNow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdef78a3d.mp4?token=hPmjyb4pY5betN6uYw-FaTIBUpfIQZ0rXeCSsWSPbO0kzl7I3ysCwkPatXfd_11UxDv9jnVG-XVhrGwwctIGEbCM0WiS9sXD_shMWN-IMOIF_M71NKfqDR55jgPRP7_ZskJuUdbQYSCh-QqufUoowql9n5UhuPyDjqwpkinNitXylvTL4Xgp1oQTCJcT_7pca_87EYTp-V3IzvtElrKDYzIXEJXFlOZ9rykWL7ee7XFYoaMCMJbGDtLhqbhu89QdCXv2s2hvtWpbzvOCP7gVgF24twl8MrnhH0A7C6-Imr508ksyV5oZJTbJ2v1sng26G8sKZjFcDmu1GIMrLtiNow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسانه های‌‌ خارجی‌ با انتشار این فیلم گفتن بعد از جنگ و تـرور رهبران ارشد حکومت؛ آزادی پوشش در ایران تقریبا به دست اومده و گویا تغییراتی در ایدئولوژی حکومت به وجود اومده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/151149" target="_blank">📅 22:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151148">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
عربستان سعودی اعلام کرد که ائتلاف مکه توافق کرده تا در واکنش به حملات حوثی‌ها به خاک عربستان اقدامات بازدارنده جمعی را به اجرا درآورد
🔴
این تصمیم پس از برگزاری نشست اضطراری «کمیته راهبردی سیاسی و دفاعی» این ائتلاف در ریاض اتخاذ شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/151148" target="_blank">📅 22:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151146">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OAelAw88QRswcw4Xr62XyYN5ve1RY10AwM9_XVGwkrJgiSaRcRyiPa6AGSsa77jH2d-oU5wy0SZyQqFBJSbDzfxxlzIDpF6YIxfLTn9Busn5R-CmVNZk5LmhlxW6bs734RVc7gNiEux2sS-Pe9bw69JiTWxGlfqwZscIIh3v5XzE9R-GlSS8K06K3GhhKtBfRoFM9ep4goqTi__QQ8tJe1a8q27iv9USja1kmeDVmSc6IwYWfAJ25rvMSV-hRlgvs9xUuSO8X2g8Jb4UCYm1AuusHH6SCAuAkzhFlb-0E4sTZfJ9-g0RGN9ARTSqaPkDosheSZ7LG_NxHc9-C-Jvug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aOif2r0srZC48beXjz8EDOZ2Vc0zh4oYLtHZMdshQmPJdy-PhrjRQS285QU6j89NZlbToM4k-5osbITfL17p3P-I1XIEfXTevUO_-rtAlGymw8lFVjti-ZkP1GLIxmCLS9oGfudEhaHJVbMIxSUxmVIrKshtLw9ts0490_XHXAGcI7nmOXUFaYXmenqeeDqwabmL1olrEoPh3cilQ0uz3KH_6JgfIfYsWnvoDA48GR7NkQ1kHuVEJesWtJvvvVC7OcUm-e4PXQE5o1kxVErumViAvQLdt_ZW-8IcuKqoAOIpkKm2XMwlsptf68fL4-jhAagqD6fkDIYem0d4CeIEKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ارسالی مخاطبان از رعد و برق امشب بروجرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/151146" target="_blank">📅 21:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151145">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تحلیل عجیبی که بازار رو شوکه کرد
‼️
👇
👇
👇
👇
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/151145" target="_blank">📅 21:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151144">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
پزشکیان: هر بار که بازرسان آژانس بین‌المللی انرژی اتمی به ایران آمده‌اند، تأسیسات هسته‌ای و دانشمندان ما شناسایی شده‌اند و پس از آن، این تأسیسات بمباران شده و دانشمندان ما ترور شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/151144" target="_blank">📅 21:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151143">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTQkWuY88q1ZxWDU4bxco2ElsU5fWJfSecfAeNbHHqr4zcA0I9Hd7ziqCl1SO1AZIFy4-cCI4_zvyq7wUOOQHGuno90Qb6D22mJlnoiCgULV5Q3WKjWXnwUwu8SqxjCJU9KJ4kAoLHeVHHLe7smkhxyC1ciVF0mMQLJuwyAuNeXLGxgOEC0W_Cr52637YCm_6WLQWxR70ei2sHVNh57wni0kbpJgE_Z23cz-xfCyOfvlkwJ3lW1qHaG87Fm-GoOCahen96np00FN1D9zc159pXBZMPc7Arzb0ENeuIgxesMPT1yF8N-2kEW0SyztCl-BQ0ERDgUrMyfAht8xsciw_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا بخاطر این کامنت زیر پیج تیک‌تاک بستنی دومینو، قراره حامیان حکومت جلوی این کارخونه تجمع کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/151143" target="_blank">📅 21:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151142">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ماشین دست ساز وایرال شده تو مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/151142" target="_blank">📅 21:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151141">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HyZ3mF9ytk0nm5Br--tUj7WL8gj3XfgCyYsjHEqu1PsVutQNs0ajbt2_hwk53WgI6sU4PGcFJRTW4jwk2Qufup55EyXJVUX-T4d9bSowhZUMdKU2mYakUjghGo0J3ZocepGEtYI5tCrGOniHMM5hd9JA2LGahlFCrUTn40TpJUNW5kaRNMaEBjA8OXrf1IM2M4NVSXvRQ64Kvnzwcz6axKtWqWYAbGVWaAOOFFGVsT-CAGH0lbHWfB-1UXsW_28G3OIQFRzMX0FNoqmQR3NVVhw-c8Sh2UmxzjijSpWB4LSRIdPfBddZuWPRsvb9RNMUuHOJZCeEsoO_FsFGim6zsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری حامد بهداد عزیز در حمایت از مهشاد کشانی و جاویدنام علیرضا سپاهی
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/151141" target="_blank">📅 21:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151140">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
اسرائیل آماده شلیک به پرواز فلای دبی شده بود
🔴
شبکه خبری سی‌بی‌اس آمریکا: به گفته دو منبع اسرائیلی، اسرائیل آماده بود تا هواپیمای مسافربری «فلای‌دبی» (FlyDubai) را که حامل بیش از ۱۵۰ اسرائیلی بود، در صورتی که ربوده شدن آن تایید می‌شد و به مسیر خود به سمت اسرائیل ادامه می‌داد، سرنگون کند.
🔴
بر اساس این پروتکل، جنگنده‌ها ابتدا کابین خلبان و کابین مسافران را بررسی کرده و برای برقراری ارتباط تلاش می‌کردند.
🔴
اگر تشخیص داده می‌شد که هواپیما ربوده شده است، پاسخی نمی‌داد و همچنان به سمت اسرائیل پیش می‌رفت، نتانیاهو می‌توانست برای جلوگیری از حمله به هدفی مهم، مجوز سرنگونی آن را صادر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/151140" target="_blank">📅 21:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151139">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
معاون وزیر دفاع یمن: حوثی‌ها رو نابود می‌کنیم
🔴
معاون وزیر دفاع یمن تو یه مصاحبه گفته حوثی‌ها رو نابود می‌کنن. این حرف رو مستقیم زده و برنامه‌شون رو اعلام کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/151139" target="_blank">📅 21:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151138">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
دبیر فضای مجازی: زیرساخت های استارلینک در منطقه هدف مشروعه
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/151138" target="_blank">📅 21:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151137">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">از جمهوری اسلامی انتقاد کنی،
بهت میگن «سطلی»
از رضا پهلوی انتقاد کنی،
بهت میگن «عرزشی»
از جمهوری اسلامی و رضا پهلوی
انتقاد کنی، بهت میگن «چپی و مجاهد»
از جمهوری اسلامی، رضا پهلوی و چپ‌ها
انتقاد کنی، بهت میگن «وسط‌باز و بلا‌تکلیف»
چرا؟
چون برای اکثر افراد، ذهنیت مستقل و شرافتمند
معنایی نداره. حتماً باید مثل گوسفند پیرو و برده‌ی
یکی از جریان‌ها باشی تا عادی جلوه کنی.
اگر تو هم مستقل هستی و فقط
حق و حقیقت برات مهمه، کم نیار؛
تو یک شوالیه در تاریکی هستی.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/151137" target="_blank">📅 21:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151135">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
خبرگزاری فرانسه صدای چند انفجار مهیب در شمال ریاض شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/151135" target="_blank">📅 20:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151134">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
پزشکیان: آمریکا به دنبال گفتگو نیست، به دنبال سرنگونی نظام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/151134" target="_blank">📅 20:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151133">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGnCk03eMuI1hYIexUv3GLps_xI0spvfcIELUwf5EccFxC32K6v8bKYWBxW8Fr87uICgGCCUqCcOy4krVLwqRlLf_nDulUKXCCbpapMIuqavNWKomKo5_d2R0QusZ4d5zMmCncxvJXUvL1lGNfT3-1KuDivlORpAWT_zRUdbGWiTWW-rgoImzcfb-YVdASFBthvzD5Wh9ePBSFjRfQgmD6lkhLlF3HRVEb9ScjqzXRxC-htef6NdC-UK4HiKTmejUUhFB6eKIFsB1f6P3C0jU8jyrCosHVsgH9SeVQ3wYfX0jHJjQZleewYYL7AVdzx6YkQvXvWtW263H3pqZiDPxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اصغر فرهادی:
پشت کشورم هستم و از وطن فروشان بیزارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/151133" target="_blank">📅 20:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151132">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
مقام آمریکایی: ناو جرج بوش برای استراحت به تایلند رفته و به زودی به خاورمیانه برمی‌گرده چون میخوایم محاصره ایران رو تشدید کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/151132" target="_blank">📅 20:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151131">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ql8ALuLR63N5G8qSyIBZG5BixM4Ds_0oEI8GhgyxatvZChcC_118wrCW-lvd9XpSI3QKFYH8PTEPiJPQErOj80kiG6c4CZaBy_M29PJ0auNFC8NcAjh6WQ5dCw5oy0IE7YdFyOYLHSrdoy3Wn3Z6jzkyIqTFJQtNDHzn3j84u2TecvZKfPYlohkFvALYG0I8jnf1cwFw1ghoIahGGWNdZ1Nflj6Cqt_bctgSeP7WcdmwAO7msGuBtcbqWrBRfHxLEMCWONtpgwjhL2ttq32V6ulsoWYN1gO_5yEULviU_jjyzxL0VNGTBk9Bv8fQRd0ojAez0k87yCgPhPLoxQkvoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک موشک شلیک شده از یمن، فرودگاه ریاض را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/151131" target="_blank">📅 20:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151130">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVoa-ObgVjII0pBLQL3wKWu9NIAwrM8oCSkBLNMRUQfhgn3YhVVweyUTggKOk-zMUkzRK44MTNKqDBt2V5tTMYxuvhXQ2K9-AtKJfAwkOtJpCK6RcYG3PTZFz6lqzLmLXvXeA9-50GTo2zUrGzAXXT9slRjiDIYC91UPM9KyRPduQ-IUdZzCe86cgF85WdpxmUaOBkOFxZeoeqqi_a8bUPnyQFxSpb3VNdkbCUcw0ZXeRAd2H9qpMqP0iqltnFRTnRZSmJLkH-PLJdBF8fE2tsLu3DUoUEYTa3_5aaU89a6x7S3QL8frGTSAAvphsndFAShWQ2meLLpdq0-3QTPScg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: تنگه هرمز دیگر عامل افزایش قیمت بنزین نیست
🔴
دونالد ترامپ گفت: «آنچه اکنون قیمت بنزین را بالا می‌برد، دیگر تنگه هرمز نیست؛ چراکه تقریباً هر روز حجم بی‌سابقه‌ای از نفت از این تنگه عبور می‌کند.»
🔴
او افزود: «مشکل اصلی پالایشگاه‌ها هستند؛ پالایشگاه‌های روسیه توسط اوکراین هدف قرار می‌گیرند و پالایشگاه‌های ما نیز در ایالت‌های دموکرات، مانند کالیفرنیا، تعطیل می‌شوند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/151130" target="_blank">📅 20:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151129">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ترامپ: حملات اوکراین به پالایشگاه‌های روسیه عامل افزایش قیمت سوخت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/151129" target="_blank">📅 20:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151128">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
الجزیره به نقل از یک مقام آمریکایی:
نیروهای آمریکایی در جنگ یمن مشارکت ندارند و ما در آنجا اهداف خاصی نداریم.
🔴
عربستان از توانمندی‌های ما در زمینه سوخت‌رسانی هوایی برای حمایت از نیروهای مخالف انصارالله استفاده می‌کند.
🔴
حدود ۲۰۰ مشاور آمریکایی در مراکز برنامه‌ریزی در عربستان حضور دارند و مشاوره ارائه می‌کنند.
🔴
مشاوران آمریکایی به نیروهای سعودی در انجام عملیات هدف‌گیری با کارایی و اثربخشی بیشتر کمک می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/151128" target="_blank">📅 20:21 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151127">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
طبق گزارشات، بندر المخا در یمن از کنترل حوثی‌ها خارج شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/151127" target="_blank">📅 20:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151126">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4d885120.mp4?token=kJRIBkyOeBfoLfc7K0WMKBV4rAhOuGGXbalumaHYfUsJI3VJw0QoYg83uCrbhhRHnZ9I_-zKzlFjQQ1rYwf6SfyBXrb26So66M5Sh4ttoDxm5oJKiqP-hBGoHs3ganZA6PMEQKVg-yjPk1z8dPJlIkTtrTSyGQCjqCg9XuofN8f8WejisBYpIRyrUVAZpDS9QQ8TCVsr4ZrI3ad3Ltg8t9xW_JbrqQwX1pjsU0wQCgsH_w1w-ThCAaP2UQN9rd3-i3iE9fxFd3ZtYxZzFPYzDwTkCnN9uXFepnc4f204ni_YaV98wUb3qVSi1DxGSzk4uuTEVyKLUhACgnoSHJgbxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4d885120.mp4?token=kJRIBkyOeBfoLfc7K0WMKBV4rAhOuGGXbalumaHYfUsJI3VJw0QoYg83uCrbhhRHnZ9I_-zKzlFjQQ1rYwf6SfyBXrb26So66M5Sh4ttoDxm5oJKiqP-hBGoHs3ganZA6PMEQKVg-yjPk1z8dPJlIkTtrTSyGQCjqCg9XuofN8f8WejisBYpIRyrUVAZpDS9QQ8TCVsr4ZrI3ad3Ltg8t9xW_JbrqQwX1pjsU0wQCgsH_w1w-ThCAaP2UQN9rd3-i3iE9fxFd3ZtYxZzFPYzDwTkCnN9uXFepnc4f204ni_YaV98wUb3qVSi1DxGSzk4uuTEVyKLUhACgnoSHJgbxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آجرلو عضو کمیته رسانه تیم مذاکره‌کننده: آقایانی که می‌گفتند نفت ۱۵۰ دلار می‌شود، الان باید بیایند جواب بدهند
🔴
می‌گویند کاری کنیم ترامپ انتخابات کنگره را ببازد، خب ببازه، بعد چه می‌شود؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/151126" target="_blank">📅 20:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151125">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWhdFYMmeI3p3I6Oul4QuXzg-6uFXKWsQptAzPMqUvI-WpRx0KiuAgpJrpxb5267AmNWw-okzObPpScIFlFaV_QAEx3T2dAh2wyaZnxf1XGxuFoW8Z2AJlzvf6J4Tp-eV4dBxNe_waRDSKoxtH7-bzE41-agOcye0KpUcy9fq9d3cdQbhxVz1-2mtEscgZ54mfEhtklWaBY6xBenJ7NHeAD1n9UrctFcWlWo6GmcdblZT5TZAwaXnrogO3Kb88Ij7ATmgY6p-Vvx7P6gFh4b6Ye6fk49p6skXhU5hO5Utl7EFDgBL58TCtDeRmPUI-SzFDV-WUjBDtEpH4zW32zGLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کنسرت علیرضا قربانی در مشهد به دلیل دخالت علم الهدی لغو شد
🔴
علم الهدی معتقد است در مشهد نباید شادی باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/151125" target="_blank">📅 20:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151124">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6VwNSHiWEF2guBuwTWfOK4va-gSEIe5f5jHfTcGNqmU3QKzxDs9Yi6At1dgOx6KFj5yHoUEG7DGXFQkcPMGCNY4hwXw9QnaaquezgORIDyyhokRH3FxjaWveGPm2_bCcJYL7VaqbmCz7YyrsNc_rt_E5lb9EAXoUTR6hVqvHWlWrzpnAkPjBBHd3kZ0r6gsR2raLbUHthBjMXelo0dxv-Zd-ulef8gPeLMD4aJl17byJLMArnfYpH_UDtTpnv91aGZ_6KUuNfBFVbhzNGlKzl_bgaGBlSE2UaliIaROrUmOLtOpPjUqfxaE4pEnROMA6-DfKJnyFUHzW4H5n16rmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ،  از طریق شبکه Truth Social:
آن چیزی که باعث افزایش قیمت بنزین شده، دیگر تنگه هرمز نیست، زیرا در حال حاضر حجم بی‌سابقه‌ای از نفت به طور روزانه تولید می‌شود، بلکه کلمه "پالایشگاه‌ها" است. در روسیه، پالایشگاه‌ها توسط اوکراین تخریب می‌شوند، و در ایالات متحد، پالایشگاه‌های ما در ایالت‌های دموکرات، مانند کالیفرنیا، توسط دموکرات‌ها تعطیل می‌شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/151124" target="_blank">📅 20:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151123">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2f8d87b4f.mp4?token=Elsi7xQqCbyHp0E3dJGn38r3MKVAFMwbK6Tb29rrQ4x1j8i-QeQ07UssDUy2wRBGtCvEGUkUm8FVl16bz8wmkeof5a95155vwzjs_QAhBGmR3EQ30-qZSYOship7nF8KqYXe7uQape3HMqoZJaHmYPA8oX-iplBlCG5eNIaRIEDRXuy-ml75P2b5v6Ag-E89qkvSJ4vC4iUlLM4xJv1RPg6Bq_L5DCP644dOc7ymCjZZdXWHBDmHzKUrp-DXm7U03pAxibb4L7vjUeZHoUdZThicNaCgvwRVfGJSXov_PyJuyfPCtWM8qIxQP6Do407QMxZs9skBNNfcDP3IdZVGKmCGpFBmZB7HJhqsX9Mml5uVz6hKlRTOh7e_tKSdCb2wbIOykfXvO6uDNxrgWTXIwGOxprhWLZEdrhbaCzmljSXIiTfrS5z1e3b3bwBlt56UzOKyFwhIeO3hkJynv--fnJ5_tgrFJUWLAy-sOIsOzKUyYqCFLbT-uUWeXJW9PaWTZlZLjEbfYjq_8kIo5n3Wh2XQllWx1FGO1znkqgn-oHWPmxDZBVwhfZsxpi35GUkPt3-He9ZOCV2U4-skW-x-hECmvkU3L7yvYyVk2WDxYjuqAWG0jDKydPjzVf9Q8BMQn8S4DRltGelQmedvIv6BysVa5pmdcpRQAy_hg6u3YIU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2f8d87b4f.mp4?token=Elsi7xQqCbyHp0E3dJGn38r3MKVAFMwbK6Tb29rrQ4x1j8i-QeQ07UssDUy2wRBGtCvEGUkUm8FVl16bz8wmkeof5a95155vwzjs_QAhBGmR3EQ30-qZSYOship7nF8KqYXe7uQape3HMqoZJaHmYPA8oX-iplBlCG5eNIaRIEDRXuy-ml75P2b5v6Ag-E89qkvSJ4vC4iUlLM4xJv1RPg6Bq_L5DCP644dOc7ymCjZZdXWHBDmHzKUrp-DXm7U03pAxibb4L7vjUeZHoUdZThicNaCgvwRVfGJSXov_PyJuyfPCtWM8qIxQP6Do407QMxZs9skBNNfcDP3IdZVGKmCGpFBmZB7HJhqsX9Mml5uVz6hKlRTOh7e_tKSdCb2wbIOykfXvO6uDNxrgWTXIwGOxprhWLZEdrhbaCzmljSXIiTfrS5z1e3b3bwBlt56UzOKyFwhIeO3hkJynv--fnJ5_tgrFJUWLAy-sOIsOzKUyYqCFLbT-uUWeXJW9PaWTZlZLjEbfYjq_8kIo5n3Wh2XQllWx1FGO1znkqgn-oHWPmxDZBVwhfZsxpi35GUkPt3-He9ZOCV2U4-skW-x-hECmvkU3L7yvYyVk2WDxYjuqAWG0jDKydPjzVf9Q8BMQn8S4DRltGelQmedvIv6BysVa5pmdcpRQAy_hg6u3YIU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر کشور با استقبال رسمی وزیر قطری، وارد دوحه شد
🔴
معاون وزارت خارجه دیروز از آماده‌سازی پاسخ ایران به پیشنهادات آمریکا خبر داده بود
🔴
این پاسخ از طریق میانجی‌ها به آمریکا ارسال خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/151123" target="_blank">📅 20:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151122">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
نیوزنیشن: ایالات متحده آماده یک حمله برق آسا و پرقدرت به ایران است
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/151122" target="_blank">📅 20:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151121">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سازمان سنجش:  هیچکدوم از 30 رتبه برتر کنکور در مدارس عادی دولتی درس نخوندن!
🔴
این در حالیه که 80 درصد دانش آموزای کشور توی مدارس دولتین
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/151121" target="_blank">📅 20:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151120">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
یدیعوت آحارونوت: سفیر بریتانیا به مقام‌های اسرائیلی اطلاع داد که اگر تصمیم به تعطیلی کنسولگری بریتانیا در قدس لغو نشود، لندن ۲۷ دیپلمات اسرائیلی را اخراج خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/151120" target="_blank">📅 19:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151119">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
اسرائیل هیوم: ایالات متحده به اسرائیل مجوز داده است و محدودیت‌های عملیاتی را برای نیروی هوایی اسرائیل در حریم هوایی عراق لغو کرده است. به گفته منابع، این مجوز به اسرائیل اجازه می‌دهد تا به گروه‌های شبه‌نظامی مورد حمایت ایران در منطقه حمله کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/151119" target="_blank">📅 19:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151118">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2720345752.mp4?token=jRM6jE6_OENugbLLmNWp0pzokIIwXgIfQRo4gxHFBq0-0_bLjfW2U44HbheG_FdqHK-kJ0ovpHyeFZtNxQMuLa6fVTkvJnXUKUKyrakMWHmg1BaC5eSjWCXShAXDvw8ch7fg1oYV6oh4mEUp0MQ-A0fmziAvbkGpufCLT8iKXXIF7snw2lzWI5-PAnCv3UlqG6uDOkEG-ckI-bHRCheJCu-_B0e77_k8ZnUilspiaDQ1c5AJqNacqGwkcPpxO3cUtd74DriPkcft1rm411swwsFZ13tJQr0Ms8o5baXWoJ9AZfeLZsv38m_kWm1ciMT4NY8FvcNKWQZVCGVEfghLrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2720345752.mp4?token=jRM6jE6_OENugbLLmNWp0pzokIIwXgIfQRo4gxHFBq0-0_bLjfW2U44HbheG_FdqHK-kJ0ovpHyeFZtNxQMuLa6fVTkvJnXUKUKyrakMWHmg1BaC5eSjWCXShAXDvw8ch7fg1oYV6oh4mEUp0MQ-A0fmziAvbkGpufCLT8iKXXIF7snw2lzWI5-PAnCv3UlqG6uDOkEG-ckI-bHRCheJCu-_B0e77_k8ZnUilspiaDQ1c5AJqNacqGwkcPpxO3cUtd74DriPkcft1rm411swwsFZ13tJQr0Ms8o5baXWoJ9AZfeLZsv38m_kWm1ciMT4NY8FvcNKWQZVCGVEfghLrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنگین‌ترین پرونده مهریه ایران اعلام شد: آقای جراح ۶۳۶۰ سکه مهریه برای خانم با وفاش زده بوده و الانم تو زندانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/151118" target="_blank">📅 19:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151117">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
یک مستشار نظامی پاکستان در حمله پهپادی نیروهای مسلح یمن کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/151117" target="_blank">📅 19:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151116">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
لحظاتی پیش سازمان عملیات تجارت دریایی بریتانیا از حمله موشکی سپاه به 2 نفتکش در تنگه هرمز نزدیکی سواحل عمان خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/151116" target="_blank">📅 19:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151114">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f8d3e496.mp4?token=PTbFIDGwvOqCHZMTUSvSpDTeIJFJvWDNPUlgLM5pqIvIXz0DQdozDYvdzesd6FVBmZAITI3lIQHDWNbiGxbgcuaWdwaRUz2vcYvN70dHNojn5TXQ5azS85km1mTiTwbuRphXQ1FOBQ8hYcUPaI9rphuYCBzw1MndyfOuw3LXJ2Id0Au8jZto3KlEnD-npuaOrZluhHjjaQUESLiTWDGiDNCzSpgbh8lNgFAxR4MR3Cy_EtgYdphs1VnGGGTyOLjKMJKgtQlTYXJbNxikl7eIN9AOYk05UBxDEOvYf4pmYfBz5MyjAye-8xczkxc-3sPX5HCZ2RzMAPrfhY7K3xM0uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f8d3e496.mp4?token=PTbFIDGwvOqCHZMTUSvSpDTeIJFJvWDNPUlgLM5pqIvIXz0DQdozDYvdzesd6FVBmZAITI3lIQHDWNbiGxbgcuaWdwaRUz2vcYvN70dHNojn5TXQ5azS85km1mTiTwbuRphXQ1FOBQ8hYcUPaI9rphuYCBzw1MndyfOuw3LXJ2Id0Au8jZto3KlEnD-npuaOrZluhHjjaQUESLiTWDGiDNCzSpgbh8lNgFAxR4MR3Cy_EtgYdphs1VnGGGTyOLjKMJKgtQlTYXJbNxikl7eIN9AOYk05UBxDEOvYf4pmYfBz5MyjAye-8xczkxc-3sPX5HCZ2RzMAPrfhY7K3xM0uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور جمهوری‌خواه ریک اسکات:
من از قیمت‌های بالای بنزین خوشم نمی‌آید، اما نمی‌خواهم با یک سلاح هسته‌ای کشته شوم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/151114" target="_blank">📅 19:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151113">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
مسئول آمریکایی به الجزیره:
حدود ۲۰۰ مشاور آمریکایی در مراکز برنامه‌ریزی سعودی مشورت می‌دهند.
🔴
مشاوران آمریکایی به نیروهای سعودی در انجام عملیات هدف‌گیری به‌صورت کارآمد و مؤثر کمک می‌کنند.
🔴
نیروهای آمریکایی در جنگ یمن دخیل نیستند و ما هیچ هدف خاصی در آنجا نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/151113" target="_blank">📅 19:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151112">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 300 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/151112" target="_blank">📅 19:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151110">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bec63d65a.mp4?token=rU3eCvkBXwiDRieC3_3FI4vQm6cCt95t-_Y1BxWKjXdG2QK3ToAIeCcmOD9v-nspMBAFViYeRCeClk-cnXo83e3V3QLIVQ71eKvdAGy6uwtA5gbfr5WIBBoyJ37hzgThxKYXdc3p4KArk_jaSNo5oYMEXjLjTZ63UhepxEQ4iX8BFz0qBIfHPvruRU8_Nl-XU6vsfIuIUp66z_APymivmRM1QL8JQj9_sMCtX1LtsRtFVC_K6X9Ymz4Vup0n05YM9__SFyxUXzZQkranI6aviPaQFK4DXpDrc7vL88gSRFJwSDdeRwtYbaksdjNJo3S_FdQILwZT7lTJWLxcBRY1rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bec63d65a.mp4?token=rU3eCvkBXwiDRieC3_3FI4vQm6cCt95t-_Y1BxWKjXdG2QK3ToAIeCcmOD9v-nspMBAFViYeRCeClk-cnXo83e3V3QLIVQ71eKvdAGy6uwtA5gbfr5WIBBoyJ37hzgThxKYXdc3p4KArk_jaSNo5oYMEXjLjTZ63UhepxEQ4iX8BFz0qBIfHPvruRU8_Nl-XU6vsfIuIUp66z_APymivmRM1QL8JQj9_sMCtX1LtsRtFVC_K6X9Ymz4Vup0n05YM9__SFyxUXzZQkranI6aviPaQFK4DXpDrc7vL88gSRFJwSDdeRwtYbaksdjNJo3S_FdQILwZT7lTJWLxcBRY1rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش‌ها از محاصره و کشتار حوثی‌ها در اطراف باب المندب توسط نیروهای دولتی یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/151110" target="_blank">📅 19:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151108">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏جی‌دی ونس:
هنوز هیچ مدرک قطعی مبنی بر ارتباط ایران با حادثه هواپیمای «فلای دبی» مشاهده نکرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151108" target="_blank">📅 18:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151107">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda6abccaa.mp4?token=keQdroMjHbtxy4FSXo4c8prh92pXklnAv7AxWScYxQS1LpW1p-82VqiILyjRFyrV31VwYzlm2wKuJmvWdloVW_0OirXUFe457xtAH7Ojn8wMunCW0gCb4BsCr7U-pFDMKd5kr1SECjC42Bg5mJb4TOwvebhxmZHUuw5HzfYNLVjABmwOUZckRXfqlsIqhN0KSiEcQaVjsDqe3yZZeOhgstDjG9s6A_lpc6U-2y4_dZpi2Nz8aud4ExabjX173GhqHmbc2zEsojx_v4VexXAe_SDUBZOrs842JECQlKKwSDB-Pb-PRROdhT0MaIQyOSW4oD2EFMoQU0LHpzZ20WPEWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda6abccaa.mp4?token=keQdroMjHbtxy4FSXo4c8prh92pXklnAv7AxWScYxQS1LpW1p-82VqiILyjRFyrV31VwYzlm2wKuJmvWdloVW_0OirXUFe457xtAH7Ojn8wMunCW0gCb4BsCr7U-pFDMKd5kr1SECjC42Bg5mJb4TOwvebhxmZHUuw5HzfYNLVjABmwOUZckRXfqlsIqhN0KSiEcQaVjsDqe3yZZeOhgstDjG9s6A_lpc6U-2y4_dZpi2Nz8aud4ExabjX173GhqHmbc2zEsojx_v4VexXAe_SDUBZOrs842JECQlKKwSDB-Pb-PRROdhT0MaIQyOSW4oD2EFMoQU0LHpzZ20WPEWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه آخونده نشسته آموزش پاک کردن مایع منی از روی صفحه گوشی رو نشون میده.
🔴
اخه چرا باید اونجا بریزه؟!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/151107" target="_blank">📅 18:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151106">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
یک منبع میدانی گفت: نیروهای صنعا استقرارهای نظامی عربستان را در راس‌العره با چندین موشک بالستیک هدف قرار دادند که منجر به تلفات و انهدام تعداد زیادی خودرو و خودروهای زرهی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151106" target="_blank">📅 18:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151105">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYUz99jB801RZj72QTXKy18Df-dN9SYMxAWL4ijzbGqfGJtpgj2-qorvafy5ooEcSZNDQcTozJHOCOAfowAQPl3lxLDyXUwc_1ccgMHmMKOOCkezejIUIi_pnKTmzdMxq4qi5twqp_ELZISx7XrX2T98eiJ3px_fZJZBFdOu6Elfa1EfZSVRVFKoGC7yQPWySABR_xEx_ZYHqF4KpFICpWkfzw-hbuYQomNWT-Fc-E4EaTbCqgSgw8tqZG5dXEr9FCfBP4GQ4heAd8TeUdXtD2rLHHHub4Fh8pyo478kjSZmcT-Q8Vkt4vPkUgMSIHXtAffCTXrrZPCCYHwiuj2u2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی:‏
هر خطای محاسباتی دشمن در برابر ایران، شکست سنگینی برایش رقم زده است؛ خطای بعدی، جبهه‌های تازه و غافلگیری‌های بزرگ‌تر را در پی خواهد داشت.
🔴
با رهبری حکیمانه رهبر معظم انقلاب، همراهی ملت تاریخ‌ساز و هماهنگی همه ارکان نظام، ایران مقتدرانه از این شرایط پیچیده عبور خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/151105" target="_blank">📅 18:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151104">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
به گزارش بلومبرگ، وزیر کشور ایران به دوحه سفر می‌کند تا در مذاکرات شرکت کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/151104" target="_blank">📅 18:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151103">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyxWLCIlZ-gz5D5d4qrmF1QGfiqfFbWqV7_6FCG4EMu6-DgXzwiaJOhftWucDizi7r7l-w1GzeVma90_eV_zdPkHhBa407RTT_QE8p9paZ3pSzDuJ_Xpm4YM7xhz1T2d7xSPyIW5Cz3jFVyaRXqaRy3pIrxIHRcxfMpS1q2ABNfyehuqe0kQNRkJVEbRC4ZFb4CWPjjBwaTmHAvR7-5F7oRt9d8HLzgoxlDH-oC8wxyyNtbbEVMs3ZxQtv0ae-B1Z_WzpRmjTQomQPKD3CHO9O0Sn8LIa2yX2D4CvSHsnjt5dsj8mRho4Dbs9cc4BrK6j4Ca3v5ZKrLL6Py6sj3AzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: حالا حالاها با آمریکا کار داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151103" target="_blank">📅 17:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151102">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
لحظاتی پیش معاون دفتر پزشکیان اعلام کرد:
ارزیابی این است که شرایط به سمت افزایش تنش پیش می‌رود و همه بخش‌های کشور باید در حالت آماده‌باش کامل باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/151102" target="_blank">📅 17:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151101">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از یک مقام آمریکایی گزارش داد که ایالات متحده در جریان حمله به حوثی ها از عربستان سعودی حمایت نظامی می کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151101" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151099">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
رویترز: صادرات از طریق خط لوله شرق به غرب عربستان سعودی پس از یک حمله جدید متوقف شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/151099" target="_blank">📅 17:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151098">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDK7nqIeVhy8k12kj91cADC4kbvOxXtOD48H-9hZRALFE6cODA8-nqfu1u75RjJK0Ti1476N0pJ7q6ewAdRQ5HuPaGz2fWOnR7BJtHkl78uXY5kPzhqN0X6WhiYYHhHeScoowew280qLbY_JeLx4F4InQoTl5LCK-a9jVAx4_ORRtFSbl4NWC-x0n3Q3oc6LP0Jcf_MpAn5I6oSvGuGJX8Nym2uuFWyNDeeqg7nGhXDSEHxl7bHPeqBbq30AMzJZiH32QbX_p7bTJ9pHARq7wtvThh54WdkE1nT2NDeEvV5Sr-91C5UYXmr9c_ureEuDibgvM9KBkyK86GJCM56rvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسن روحانی: قدرت سیاسی باید در تصمیم‌گیری‌های جنگ وارد عمل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/151098" target="_blank">📅 17:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151097">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
تحلیل الجزیره: ترامپ قصد دارد حمله‌ای غافلگیرکننده به ایران انجام دهد
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/151097" target="_blank">📅 17:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151096">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8897c902ae.mp4?token=u_Mlf7XaFIsIqABiYmFZnjMTFriOkYsNKAdF2IoeOcKLR_Ded3P3a0KNDiNc1JfRjpnYqBEz7-T9_12deetuGRkr1U9cAL751fAaELn8B3wq9lOBuOxmQ1j-r-xdBES0E5WIBktwP5XC0YrJWlMI2xeLlaw-7u8QFt8MiBdXpwckIiLIzl1zeJ5Xdfsm4RMgziyOq-M47BSApSF2JucwWIdmeZtqx4REEtE_cm5mwTQzERUI-4Ys4rFKBRTkZYIInhwgw3atVTBL2iK5hLP3Ta_Jjt-n47g3OyMKw246FEiI4_CuCYgkYrYZ7LD31Gp8TGHS3mYJygCN_taiY9urHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8897c902ae.mp4?token=u_Mlf7XaFIsIqABiYmFZnjMTFriOkYsNKAdF2IoeOcKLR_Ded3P3a0KNDiNc1JfRjpnYqBEz7-T9_12deetuGRkr1U9cAL751fAaELn8B3wq9lOBuOxmQ1j-r-xdBES0E5WIBktwP5XC0YrJWlMI2xeLlaw-7u8QFt8MiBdXpwckIiLIzl1zeJ5Xdfsm4RMgziyOq-M47BSApSF2JucwWIdmeZtqx4REEtE_cm5mwTQzERUI-4Ys4rFKBRTkZYIInhwgw3atVTBL2iK5hLP3Ta_Jjt-n47g3OyMKw246FEiI4_CuCYgkYrYZ7LD31Gp8TGHS3mYJygCN_taiY9urHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بمباران صنعا،دقایقی قبل
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/151096" target="_blank">📅 17:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151095">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری / قزاقستان، ازبکستان و قرقیزستان به خاطر احتمال شیوع طاعون در روسیه، مرز هاشون با روسیه رو بستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/151095" target="_blank">📅 16:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151094">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
رئیس سازمان هواپیمایی کشوری:
حدود ۱۰۰ هواپیما در جنگ اخیر آسیب دیدند؛ کمتر از ۱۰ فروند به طور کامل از بین رفتند/ ۲۷  فرودگاه آسیب دید
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/151094" target="_blank">📅 16:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151093">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4qsI0boht-KQG8vbrKOIMl3-dlMW-m4Eu04ztzgD77HppuPDQODJKtSmRt54ThnnG4R71fCvXOtPUDM3DJ2jAZPCO2R9wGBgVctaqgkLIvk3Vw4-st2ZPOBQfBJR5664IEYOx9yHHqGiFBsGvu9e4n32TLefdErndcYnuspN10fVP8S-ZoZgLKDpBH6VeFsaty3vfCj5Z-TimYDJZHUULNGLuw0-AZGoJXRbdqpeGUPLfy0Z9-vbXiJgpUVgi6alurnhsryzS8bjS99hn1GmkKn4Nct5iRQBe4MHPZc0oBeKT5G6t9CSjeAz8girefnekbuCdqyiO1A9f0X2LA3-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای نظامی پاکستانی مدل GLF4 امروز در ریاض فرود آمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/151093" target="_blank">📅 16:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151092">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
روبیو درباره یمن: عربستان تحت حملات حوثی‌ها قرار گرفته و حق دفاع از خود را دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151092" target="_blank">📅 16:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151091">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc7144c23.mp4?token=HtieTq4A4Pp0yDgvAkPYXXHUpwm0OsuSLcYIeiEmQiCMySLrQhOAxjODSuK0XWD3TnPFqxAQHuWGM7BrDNTuYcGmDwrpPZzQ6rj0dCTxJ4uaumZHI2AogdIObtjEwmrtIth_LkWAluHzWQcXQPdkSkk3XA7mejQphHqQ68aAbWby70PzaRm1w8HD49UUSBAj9VEjIZr7_STRiaSoNsWQhquZWKsfyqBRQKxbS7KY3iNI6yQbMxs74z-tCczXPGCJSgO0UC1IpTQvqlyA-fMHAkBx5ZdUbiCHB5tXRzjsZXwAT_rt_SDjKfME6b8SpGlAQkVh0qhhoJvKp-rua_hLcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc7144c23.mp4?token=HtieTq4A4Pp0yDgvAkPYXXHUpwm0OsuSLcYIeiEmQiCMySLrQhOAxjODSuK0XWD3TnPFqxAQHuWGM7BrDNTuYcGmDwrpPZzQ6rj0dCTxJ4uaumZHI2AogdIObtjEwmrtIth_LkWAluHzWQcXQPdkSkk3XA7mejQphHqQ68aAbWby70PzaRm1w8HD49UUSBAj9VEjIZr7_STRiaSoNsWQhquZWKsfyqBRQKxbS7KY3iNI6yQbMxs74z-tCczXPGCJSgO0UC1IpTQvqlyA-fMHAkBx5ZdUbiCHB5tXRzjsZXwAT_rt_SDjKfME6b8SpGlAQkVh0qhhoJvKp-rua_hLcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ما به امنیت تمام پایگاه‌هایمان اطمینان داریم، زیرا تمام پایگاه‌های ما می‌توانند در هر لحظه‌ای مورد تهدید قرار گیرند. و به همین دلیل است که امنیت زیادی در اطراف آن‌ها وجود دارد
🔴
و ما با بریتانیایی‌ها، مدت بسیار طولانی است که به طور نزدیک با یکدیگر همکاری می‌کنیم، به ویژه در مورد [پایگاه هوایی فرفورد]، و آن‌ها بسیار همکاری‌کننده بوده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151091" target="_blank">📅 16:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151090">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fdbd24129.mp4?token=VkalL2A0G8Oyw612dNFZhOC5uRuCaWcnWPEkT2JnKoC9MV_dIhdlM1KP57Zqc1XOFXprkp2erwhdA-96RCGWJNrGS_jzG2Xwyxa8X-w5hEzNyb2e5Xfi9R9YN_jxRN2XJ39I-Rx3UM_aZhPzYQgVk4T3foi26NuPmzsJKEkdnmrBxYvrU2Z2B7lEKwIYgO7B2mO5WwnboJhkfD7OBvG9G0aLoNvG-uXn1hByjHy7-cPuNipswHUKi0Zc9Mxo88cHlhjRMaGbpkB1LGO_Z9kCnQJsEr0mcREERpRYOB-YrMlsv8QXm-hG0WAAxdw4Np9hTLt-gdsmaiG5dDby-i89QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fdbd24129.mp4?token=VkalL2A0G8Oyw612dNFZhOC5uRuCaWcnWPEkT2JnKoC9MV_dIhdlM1KP57Zqc1XOFXprkp2erwhdA-96RCGWJNrGS_jzG2Xwyxa8X-w5hEzNyb2e5Xfi9R9YN_jxRN2XJ39I-Rx3UM_aZhPzYQgVk4T3foi26NuPmzsJKEkdnmrBxYvrU2Z2B7lEKwIYgO7B2mO5WwnboJhkfD7OBvG9G0aLoNvG-uXn1hByjHy7-cPuNipswHUKi0Zc9Mxo88cHlhjRMaGbpkB1LGO_Z9kCnQJsEr0mcREERpRYOB-YrMlsv8QXm-hG0WAAxdw4Np9hTLt-gdsmaiG5dDby-i89QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار خطاب به وزیر خارجه آمریکا: چرا بمب‌افکن‌های آمریکایی پایگاه هوایی سلطنتی فرفورد را ترک کردند؟
🔴
مارکو روبیو: مشاهده جابه‌جایی و چرخش نیروها و تجهیزات نظامی اتفاق غیرمعمولی نیست
🔴
ما نسبت به امنیت تمامی پایگاه‌های خود اطمینان داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151090" target="_blank">📅 16:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151089">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08c38827ef.mp4?token=kg0L60quTK-jcPSNVzlWy6PqqFNXszqXB9Xpfq0sgUxvlZ1NWFJDDUm5-XTzZ9enmiXOjEFUDoYfkmHwTCCe8xiskzh968MeHqH3z7e43g8lmVMhMUOK7myjSIJCHb1PGN41qXYnzDlXxgnRGSeMNUlUNYWUet4222n231KKdPPKYTLDw1y3094fwjQ17sirL2WOsh4tben2orbc_v2PbsVC7_aes0mFQqgeMGsbzw3hvJFU25o7HkT-kuv4weAg3HTN06VpMYvVEnRlW0R3mcPkqtOnLpIvC7AgPp54cizfC_Q5hlYzriLT-qH3523EwyAqdjzsLWu0IjpHYDoZs4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08c38827ef.mp4?token=kg0L60quTK-jcPSNVzlWy6PqqFNXszqXB9Xpfq0sgUxvlZ1NWFJDDUm5-XTzZ9enmiXOjEFUDoYfkmHwTCCe8xiskzh968MeHqH3z7e43g8lmVMhMUOK7myjSIJCHb1PGN41qXYnzDlXxgnRGSeMNUlUNYWUet4222n231KKdPPKYTLDw1y3094fwjQ17sirL2WOsh4tben2orbc_v2PbsVC7_aes0mFQqgeMGsbzw3hvJFU25o7HkT-kuv4weAg3HTN06VpMYvVEnRlW0R3mcPkqtOnLpIvC7AgPp54cizfC_Q5hlYzriLT-qH3523EwyAqdjzsLWu0IjpHYDoZs4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسموتریچ، وزیر دارایی اسرائیل: پاکسازی دقیقی که ما اکنون در جنوب لبنان در حال انجام آن هستیم، بی‌سابقه است.
🔴
آن‌ها جایی برای بازگشت ندارند. ببینید چه شکلی شده است
🔴
و در ضمن، دنیا جلوی ما را نمی‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151089" target="_blank">📅 16:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151088">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
کاخ‌سفید به پرونده طاعون روسی ورود زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151088" target="_blank">📅 16:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151087">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10bd25ab1d.mp4?token=aZYZVsNiQJHCgX6OaR561mByX3KYOkB_AyuM2J2RjR_Z-lN25bqMX35vb_ipnHRmsFZ6mloTW5aC0GwXurCr1LZ2tpFnsONhxEr-P6KvIe08L-kAYKjxzsau8PHFeO9NYWZwnwNSh-2-m5kpiSK4zSQ92IWXD7Wl-5Uw8DJtw96z_6O8zZFofrfxOyFkdoM5dOgdlehYL9YPCxfx10Cb865JTFav_NcZCre_p8Ly2Pgz8rcc7GGXRAjbGkx9RY8RpR9NXpgbtM7n3kB4NCbUr5_HDhIArndUIc_6A7W_zBQzhAAipzrp1f-jpJF28vFkqCfJzCDG9AIeGvrmBNniGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10bd25ab1d.mp4?token=aZYZVsNiQJHCgX6OaR561mByX3KYOkB_AyuM2J2RjR_Z-lN25bqMX35vb_ipnHRmsFZ6mloTW5aC0GwXurCr1LZ2tpFnsONhxEr-P6KvIe08L-kAYKjxzsau8PHFeO9NYWZwnwNSh-2-m5kpiSK4zSQ92IWXD7Wl-5Uw8DJtw96z_6O8zZFofrfxOyFkdoM5dOgdlehYL9YPCxfx10Cb865JTFav_NcZCre_p8Ly2Pgz8rcc7GGXRAjbGkx9RY8RpR9NXpgbtM7n3kB4NCbUr5_HDhIArndUIc_6A7W_zBQzhAAipzrp1f-jpJF28vFkqCfJzCDG9AIeGvrmBNniGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسموتریچ، وزیر دارایی اسرائیل: نوار غزه هرگز نباید بازسازی شود — یادبودی از گناه است
🔴
این همان چیزی است که بیشترین تشویق را برای مهاجرت از آنجا ایجاد می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151087" target="_blank">📅 16:09 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151086">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
نتانیاهو: رهبران جهان به من می‌گویند: شما از اعماق فاجعه‌ی هفتم اکتبر برخاستید، شما فرقه‌گرایان مسلمان را شکست دادید و به بشریت امیدی را بخشیدید که نیروهای تاریکی می‌توانند شکست بخورند.
🔴
و سپس بسیاری از آن‌ها این را اضافه می‌کنند: کاش جوانانی مانند این‌ها نیز در میان ما رشد می‌کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151086" target="_blank">📅 15:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151085">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ec4de47b3.mp4?token=QyqvAZ4s6vqxpgyjG08RRHR-5EoGk0LolwwXZFnu1Te0g7WQlaWjbnwe6oV8miJ-8zTUOE7oARScLfqPM_rUaOuSpFlD_tCotdAA4mlspf84EUmF2L_xAWtYlpxQUR94c0vjaeZUUbxo33ZhfIL-YAU-fajKyUVvGUUilnWYoSYqa_jlWkVqVQnCgLRxURbGohHQLIFL98REyJ1kyrfa2NgVF5hs2zw2aGiMK7z2e3p09hd9AR_qRaER79rQQlF04WuS5sDKKIvGBzXziB0Fq03TIy1af5kejaAOmbOyl2scX83vIRhB2IzfNvVl6oMChdeykg7Sl26tSj5aLjLUMAWSz-H57BptSE28S5VSfLDZiJSXfuQRvG1Cj1XVUJsImdHv76oyaxAGLC3q3wnupb-kXqyL-lLjj5AFabx3pmDPrgDapxCwA4TZKkWM1g8_AHWzPWi5s0v6_wYu9IGYmadf2S8_AQOXF2K_Dsnj98YSa68pV4ObpG6N-TixMzK7jfJFLtIjF9E_QxR4IkWkcANVOqK1k9pIuSHxpDAzx1Vo2KInM-w5BZxu165CKSF_hcQuWVvYy1MAKn1WdZU6N-3B5nkBgp7LlrpLw2a2z3r4dGC8dVj_2sabqum5swXF-yALO1A9-NNN260uTSWaLTpX61dGgbSMKiTGKn8REto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ec4de47b3.mp4?token=QyqvAZ4s6vqxpgyjG08RRHR-5EoGk0LolwwXZFnu1Te0g7WQlaWjbnwe6oV8miJ-8zTUOE7oARScLfqPM_rUaOuSpFlD_tCotdAA4mlspf84EUmF2L_xAWtYlpxQUR94c0vjaeZUUbxo33ZhfIL-YAU-fajKyUVvGUUilnWYoSYqa_jlWkVqVQnCgLRxURbGohHQLIFL98REyJ1kyrfa2NgVF5hs2zw2aGiMK7z2e3p09hd9AR_qRaER79rQQlF04WuS5sDKKIvGBzXziB0Fq03TIy1af5kejaAOmbOyl2scX83vIRhB2IzfNvVl6oMChdeykg7Sl26tSj5aLjLUMAWSz-H57BptSE28S5VSfLDZiJSXfuQRvG1Cj1XVUJsImdHv76oyaxAGLC3q3wnupb-kXqyL-lLjj5AFabx3pmDPrgDapxCwA4TZKkWM1g8_AHWzPWi5s0v6_wYu9IGYmadf2S8_AQOXF2K_Dsnj98YSa68pV4ObpG6N-TixMzK7jfJFLtIjF9E_QxR4IkWkcANVOqK1k9pIuSHxpDAzx1Vo2KInM-w5BZxu165CKSF_hcQuWVvYy1MAKn1WdZU6N-3B5nkBgp7LlrpLw2a2z3r4dGC8dVj_2sabqum5swXF-yALO1A9-NNN260uTSWaLTpX61dGgbSMKiTGKn8REto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: هر کسی که در حمله علیه ما دخالت داشته باشد، و هر کسی که گروگان‌های ما را اسیر کرده باشد، در آستانه نابودی قرار دارد.
🔴
ما به آنها خواهیم رسید، درست همانطور که به دیگران رسیدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151085" target="_blank">📅 15:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151084">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e185cf65f.mp4?token=X19aO6k2Im0uWBQI5dDL1w-RhCv0AnUiglQjp-I0p6-x4fTkv3qTkJnjkh3P297wCX35naoaAJM7CSSts_Emyui60DrE-WC3olPxHzZtaXsa0hr_ZXre_ty64NiJdPYAbScfWOjsAKjs23s4SFhApOHn7WikkHYiKwljblcb4cEBFgJm8zRLuNJH1eYAQ01NIiHC1KYZxc-qu6O_q_2mnssseZLbwU5j0T49U7ZbghlaRtRcX5r_5X2xzpCP_VX_Hk79i-0MSmdcQSY2lc-NQqpkWRFvTFY4q0YJk4ILIoojUCWbdBz24zMJ9YVAdrq-e_kdJ21loMG_TsEeUvuYB5U1m-TAJDnWDmv5ihL3DOSnzNOr4WcR_yAErR8PtewBI_GdO-ZPOt73v9b5h6aQnUO46tJNpJKTWed-lbv8zT4jzouefLzzkHmgOGgTsdsK-Sayqx4x0uVVKmXaDxlqw6HpC_QOyV0FwZtvcIwWcTUmD855Pq1wSgpLjUy4UD8ihAAW2Rury4fwTd1NRTdbPApBJcmiylLxIWP1FCv_SIMG_ZWC6axvpbdlaxprjDfrfZSqQ0nseK_PiGtIgMmKyEB3vjFX89WymosHWSXD0oVokif3Fyymoqao3cyxShApAHctdbhTedhUxi3LyuUJFROqz3fZvO8rLMwNAtstSn0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e185cf65f.mp4?token=X19aO6k2Im0uWBQI5dDL1w-RhCv0AnUiglQjp-I0p6-x4fTkv3qTkJnjkh3P297wCX35naoaAJM7CSSts_Emyui60DrE-WC3olPxHzZtaXsa0hr_ZXre_ty64NiJdPYAbScfWOjsAKjs23s4SFhApOHn7WikkHYiKwljblcb4cEBFgJm8zRLuNJH1eYAQ01NIiHC1KYZxc-qu6O_q_2mnssseZLbwU5j0T49U7ZbghlaRtRcX5r_5X2xzpCP_VX_Hk79i-0MSmdcQSY2lc-NQqpkWRFvTFY4q0YJk4ILIoojUCWbdBz24zMJ9YVAdrq-e_kdJ21loMG_TsEeUvuYB5U1m-TAJDnWDmv5ihL3DOSnzNOr4WcR_yAErR8PtewBI_GdO-ZPOt73v9b5h6aQnUO46tJNpJKTWed-lbv8zT4jzouefLzzkHmgOGgTsdsK-Sayqx4x0uVVKmXaDxlqw6HpC_QOyV0FwZtvcIwWcTUmD855Pq1wSgpLjUy4UD8ihAAW2Rury4fwTd1NRTdbPApBJcmiylLxIWP1FCv_SIMG_ZWC6axvpbdlaxprjDfrfZSqQ0nseK_PiGtIgMmKyEB3vjFX89WymosHWSXD0oVokif3Fyymoqao3cyxShApAHctdbhTedhUxi3LyuUJFROqz3fZvO8rLMwNAtstSn0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: اخلاق سربازان ما نظیر ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151084" target="_blank">📅 15:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151083">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90aedaaa0c.mp4?token=DtPOpnCB8SCAX0eHaZblpQPamimyxgSSNerc5LzqIXVSr-rQ46lw9ppK-yhjr3boZafDJt6BX0DUhOjrcYWxqphrSBIQBi5Yx_Ki7js_S6LuD0Y2aGyYUaU5A2ZzlrtzUzwKMDTACoWhJMy770WiLufY_Ri_SuofAW66rOE7yZfOr-574yUCTGSMuc79oZihz5Ov1JFvWfwpi4DDUrGvuAua8u7ZUCT7AK3d5hL8bJ95k2gYmJgO0601MCxCXs-OzJAvWcPjvkq0w737PASNYh3jZGcsxKmZSn2NnSI1bjsEvkE2kUACyVOw7QBHVd8OaUbV718hsra0mUGedKTcsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90aedaaa0c.mp4?token=DtPOpnCB8SCAX0eHaZblpQPamimyxgSSNerc5LzqIXVSr-rQ46lw9ppK-yhjr3boZafDJt6BX0DUhOjrcYWxqphrSBIQBi5Yx_Ki7js_S6LuD0Y2aGyYUaU5A2ZzlrtzUzwKMDTACoWhJMy770WiLufY_Ri_SuofAW66rOE7yZfOr-574yUCTGSMuc79oZihz5Ov1JFvWfwpi4DDUrGvuAua8u7ZUCT7AK3d5hL8bJ95k2gYmJgO0601MCxCXs-OzJAvWcPjvkq0w737PASNYh3jZGcsxKmZSn2NnSI1bjsEvkE2kUACyVOw7QBHVd8OaUbV718hsra0mUGedKTcsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برگزاری رژه‌ همجنسگرایان حامی فلسطین در فرانسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151083" target="_blank">📅 15:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151082">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22b118ab01.mp4?token=GMucXBV6yli3EYcMr47sT2PoYX3BMaRwxg2RWSwE5ZRPM251-ZtrDSQpEfxM7vauudxxCD16Tve30a4hxQJl5F-bVoC8OSL0hSsJht0mhkRK4CANHiEFvC7HWylk48kS7wqVtVjmI3LsX9oh5XQE1xMVoTScUpDX1pd55Ss1T0C1iBk9DLz--a7hvlIMPwwnWRc1pXN0Kgyn1aoe7ATgaUKY48HvFb_EUBPom9D37I-7OoF6C_dO0oum1vOcICcgVT1lXc7ToZnt0UTHVX_ISTmbk1IFdWROnPnAtnsEQS7YUZoSeBXCJG-GIvHKEO9ha-3enz6QhteUW6vy-51-MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22b118ab01.mp4?token=GMucXBV6yli3EYcMr47sT2PoYX3BMaRwxg2RWSwE5ZRPM251-ZtrDSQpEfxM7vauudxxCD16Tve30a4hxQJl5F-bVoC8OSL0hSsJht0mhkRK4CANHiEFvC7HWylk48kS7wqVtVjmI3LsX9oh5XQE1xMVoTScUpDX1pd55Ss1T0C1iBk9DLz--a7hvlIMPwwnWRc1pXN0Kgyn1aoe7ATgaUKY48HvFb_EUBPom9D37I-7OoF6C_dO0oum1vOcICcgVT1lXc7ToZnt0UTHVX_ISTmbk1IFdWROnPnAtnsEQS7YUZoSeBXCJG-GIvHKEO9ha-3enz6QhteUW6vy-51-MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو:ایران با بمب هسته‌ای به دنبال نابودی اسرائیل بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/151082" target="_blank">📅 15:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151080">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات الونیوز</strong></div>
<div class="tg-text">👈
پلن ویژه افزایش ممبر برای کانالهای تحلیلی و اقتصادی داریم جهت اطلاع از شرایط به دایرکت پیام دهید
دایرکت</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/151080" target="_blank">📅 15:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151079">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
معاون وزیر دفاع یمن به الجزیره گفت: ما وارد مرحله جدیدی می شویم و عملیات نظامی که انجام می دهیم همه جانبه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151079" target="_blank">📅 15:25 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151078">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
گزارش سی‌ان‌ان از جزئیات شیوع طاعون در روسیه/ یک بیمارستان قرنطینه شد
🔴
مقام‌های روسیه پس از مرگ یک کارمند آزمایشگاه در مؤسسه‌ای در سیبری که به مطالعه طاعون و دیگر بیماری‌های عفونی اختصاص دارد، در پی ابتلای او به بیماری مرموز، تدابیر «ضدهمه‌گیری» را به اجرا گذاشته‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/151078" target="_blank">📅 15:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151077">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سازمان بودجه: فعلا برنامه‌ای برای افزایش حقوق نداریم و تغییر نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151077" target="_blank">📅 15:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151076">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
اگه از بازار جاموندی اینجارو داشته باش
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151076" target="_blank">📅 15:09 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151075">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
خبرگزاری فارس: وضعیت سیاه اقتصاد آمریکا در زیر سایه افزایش دلار در ایران پنهان شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/151075" target="_blank">📅 15:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151074">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9134c7724b.mp4?token=MQ2vOAf0AJxflKMR21ixULmw1gQzn3vOvztL2NjOs-AfEx_YyxSi8AuBitkSaABJR__RFt4rPqdaEnQf2pPD_LzK2XDTpQNvtkOQEeIvQWkltcDsECcZzYdEBihtBR1lyenLIczSCcsxxFRAhI3tVNmDlZxpaV_SybWUwv3TKCIv7nY7HHVEvzBq8A2fBd7I-hSS1j-kaDhS8_YZ0Yn5aUn2sSvyzz9YA9srlKONVf_e0MFEm86xwsxik7QlCRiA1L6MScE7ktKC_Y2AuSXFxz950HqoKZ9V7HVqhX-0r8-3LCV-u9p_C5VXg01Tr_xiBRS5qTWm4kFjt3hbHLE88g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9134c7724b.mp4?token=MQ2vOAf0AJxflKMR21ixULmw1gQzn3vOvztL2NjOs-AfEx_YyxSi8AuBitkSaABJR__RFt4rPqdaEnQf2pPD_LzK2XDTpQNvtkOQEeIvQWkltcDsECcZzYdEBihtBR1lyenLIczSCcsxxFRAhI3tVNmDlZxpaV_SybWUwv3TKCIv7nY7HHVEvzBq8A2fBd7I-hSS1j-kaDhS8_YZ0Yn5aUn2sSvyzz9YA9srlKONVf_e0MFEm86xwsxik7QlCRiA1L6MScE7ktKC_Y2AuSXFxz950HqoKZ9V7HVqhX-0r8-3LCV-u9p_C5VXg01Tr_xiBRS5qTWm4kFjt3hbHLE88g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پدرو سانچز، نخست‌وزیر اسپانیا، برگزاری انتخابات زودهنگام در ۲۹ نوامبر را اعلام کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/151074" target="_blank">📅 15:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151073">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
صرافی omp فینیکس امروز تمامی پول کاربران خود را بلوکه کرد و دیگر در دسترس نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151073" target="_blank">📅 14:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151072">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sljnlPLYoPCAG1TWx5a6jr2BB0Q5TOdhz96x7JhZOGhyj71pdHj1Ro3EZctasM0XRwhGRQHrGAc89bs1m_C2lhkiW1fQzv3vxqUHX_GLiZkicGiakU3FWJK4h6nBpKa-t1qydNaOn139bKBejbohtet--MPpCCxdJRO9Ca07SzaR0yCz1fzP1Tr1W7Z5zbce-tbwbD9xB0F5DBovYuJ7tV2QIYlwxLw_qLhw4Fthf6qyC7r6v-MHhp3zHhPxXQu3daVCAKv3c2Skd170Ii14yIKKThaXxLam5QBhbmHcsKm-ZXrMEOCbgCj3l5x84m35qufysYrbffO_YiTkPCs_gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: پرچم ایران در تنگه باب‌المندب برافراشته شده است؛ در حالی که حوثی‌ها آماده می‌شوند تا پیش از انتخابات آمریکا، خبر بسته‌شدن این تنگه را اعلام کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/151072" target="_blank">📅 14:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151071">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c201257b1.mp4?token=GTwrMYNinnqKgWdphAalUi6LuFt5-8oMpVkEExEzr9LdyozvVubri0XdGywjHInLnA1sDP64MY6EXmCONe-HTypOmwqsdxiEmDmRWQh6UQb4Z_HoRRC7S2O4rB6949gjaalblmKeEVU8Mq-aEOi9HjOqJ84zX4a2BVNPXUJoSVykMHUkF7wvKzoDN5KCxqCSz2OsvAsOlYQOZI3Yh3oDItetfzfhPid5t9fxC2S_fhmOxDHCTUpVrOM1j2y8vpZpEp3H_w4vwOsEmmCk4EURmGf5TCJ5qGXYexIm0Yi0QNYyKOi7heAb3hZnfl5dwfZu8QQY-HErTj2d0jnDLydOGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c201257b1.mp4?token=GTwrMYNinnqKgWdphAalUi6LuFt5-8oMpVkEExEzr9LdyozvVubri0XdGywjHInLnA1sDP64MY6EXmCONe-HTypOmwqsdxiEmDmRWQh6UQb4Z_HoRRC7S2O4rB6949gjaalblmKeEVU8Mq-aEOi9HjOqJ84zX4a2BVNPXUJoSVykMHUkF7wvKzoDN5KCxqCSz2OsvAsOlYQOZI3Yh3oDItetfzfhPid5t9fxC2S_fhmOxDHCTUpVrOM1j2y8vpZpEp3H_w4vwOsEmmCk4EURmGf5TCJ5qGXYexIm0Yi0QNYyKOi7heAb3hZnfl5dwfZu8QQY-HErTj2d0jnDLydOGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عوستاد خوش چشم: اگر آمریکا بمب اتم بزند، ما هم پدر بمب‌ها را به آمریکا می‌زنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/151071" target="_blank">📅 14:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151070">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
از سرگیری پروازهای مستقیم هواپیمایی عراق به ایران از روز پنجشنبه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151070" target="_blank">📅 14:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151069">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e02dbaf5d.mp4?token=VgQMAxPJEqMkv3qgDu3EuxCDq_ZouUXFjcef_Y6mfg-WiKSENBNUtH6hlPE3XjtVqxGXYrYH36OPbs7Onxxtc-ds3P0Y_xuUu16EnSLS9X5iNXA2d71jj8P14bLfx2fQcsHY6Fq1G93jyEKcl8yCID7jMNWzKCYB458tJojbwRI0SJP8xddNlOm1Na_GEs9VBAWcuFCtCHb4TuPY3IYZRTIO77swEEwY1zmXqGQDBEZ7j_MGdahLkeFqlFuyH3IRE4YISSxFc5_tO-OTBNi5KS4j7o7O_-WBJyIWDgflDvk3pxXpYGfJuie50APYh_zlGtNT11N5-RTTMqc845_t3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e02dbaf5d.mp4?token=VgQMAxPJEqMkv3qgDu3EuxCDq_ZouUXFjcef_Y6mfg-WiKSENBNUtH6hlPE3XjtVqxGXYrYH36OPbs7Onxxtc-ds3P0Y_xuUu16EnSLS9X5iNXA2d71jj8P14bLfx2fQcsHY6Fq1G93jyEKcl8yCID7jMNWzKCYB458tJojbwRI0SJP8xddNlOm1Na_GEs9VBAWcuFCtCHb4TuPY3IYZRTIO77swEEwY1zmXqGQDBEZ7j_MGdahLkeFqlFuyH3IRE4YISSxFc5_tO-OTBNi5KS4j7o7O_-WBJyIWDgflDvk3pxXpYGfJuie50APYh_zlGtNT11N5-RTTMqc845_t3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای؛ حریق گسترده در خط لوله شرق–غرب عربستان
🔴
تصاویر ماهواره‌ای جدید از آتش‌سوزی گسترده در نزدیکی ایستگاه پمپاژ شماره ۲ خط لوله راهبردی شرق–غرب عربستان، در شرق ریاض حکایت دارد؛ بر اساس این تصاویر، ستون دود ناشی از حریق تا حدود ۵۰ کیلومتر امتداد یافته است.
🔴
این خط لوله پیش‌تر در ماه سپتامبر هدف حمله قرار گرفته بود و به گزارش نیویورک‌تایمز، کمتر از یک هفته از بازگشت آن به مدار عملیاتی می‌گذشت.
🔴
در حملات قبلی نیز چند ایستگاه پمپاژ این خط لوله آسیب دیده بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/151069" target="_blank">📅 14:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151068">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3xCTJpC7xMn9ISv2qpx5JsxJmQZU05UBjCVXmyKtPTG_vGgY6eErwLwBTa91GM0HL3Yvlw9r-ApeeDDSGI39I8hsZMoOkzmvApC5ih7s6kY6eo28lQmkPFfVh9eYDKhs-Qf390JmiY9PC5b3iQYeXqDSnZp7CS7DIxWK95RPBE2q7-nbT0MGNfAYwpMiNlCq8eSabwd9kQcvQtxPLI48O27MyqtCnHXmWl66IeU1OYjxkSS5y5hjUfWpzeFn5PgdTcwOHqLkmaAkUZPq1U5lAI1YTGcl5_L3lmzNk7ZZJ2UVjz1MQZz_8UD1wk7MRJvwaa2Zn0afDeXSZ9VPtTDoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برندگان جایزه نوبل پزشکی ۲۰۲۶ معرفی شدند
‏
🔴
«کارل دایسروث»، «پیتر هگمان» و «گئورگ ناگل» برای اکتشاف در زمینه کانال‌های یونی کنترل‌شونده با نور و اپتوژنتیک برنده جایزه نوبل پزشکی ۲۰۲۶ شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151068" target="_blank">📅 14:09 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151067">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از دریافت گزارشی درباره وقوع یک حادثه در ۱۱ مایل دریایی شمال بندر خصب عمان خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151067" target="_blank">📅 13:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151063">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbAM0bQO4pzTCr3agPXuIACJT6lVtkc0s232RS9sPuT9b6RuU0Z-71IaPJq71M0olGvsMBKm-7rJ1UfobVji-cI8Yd6iaKibiTB9X0x4YhWnCPlbNyimvB6s92fjcvNiJjo5i3Nozb4OGqgvqoh_9rOPy1MWDgDmqafQs4ckqwG0x0mp4q865W98kAtBt1ocenF524Pbs3Xo3I0hcIFuklmwjn8il9I-xG1h0aQEvjx6M5ghH05jvL2JUvJOqFVDGWJmy2v09aBD1WvdaNR-ia-tnoKKmhkowUM0sWFqZEPm3dHtKXYKi7nAefozel3560y_PxPIznunPXQob3n8iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46fd92caef.mp4?token=PMDzBF1b4fvQOSh2eVNVbaLZZWQsSKJa3DYF0DdE6IFiMVgjmC2RpUs8BGxwg6KmPy-YFI6oh4i3ulgFSZSSXhp50MY-D2YbZKEnBmNV8zjKusn3k9SwHXIeobNQGgLaQ43mDNmb5_xSazPnMXsVxykJnJflMfJLAHQCZy0nhlywt64wA3N9erP417sDy227hwIBGWlvm66dyxj_tGY3ijHnP0QZRnVW4PiochFtGBrVLFb8zMMFOsAcizCP02MU9QOVByx42O4csWzfNXg0uDFXUtzFF48vdSt8OKbm9OFQYWJdWskZKZrgcYDhW_Gqd1g3dT703XsgWSJD_FkhVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46fd92caef.mp4?token=PMDzBF1b4fvQOSh2eVNVbaLZZWQsSKJa3DYF0DdE6IFiMVgjmC2RpUs8BGxwg6KmPy-YFI6oh4i3ulgFSZSSXhp50MY-D2YbZKEnBmNV8zjKusn3k9SwHXIeobNQGgLaQ43mDNmb5_xSazPnMXsVxykJnJflMfJLAHQCZy0nhlywt64wA3N9erP417sDy227hwIBGWlvm66dyxj_tGY3ijHnP0QZRnVW4PiochFtGBrVLFb8zMMFOsAcizCP02MU9QOVByx42O4csWzfNXg0uDFXUtzFF48vdSt8OKbm9OFQYWJdWskZKZrgcYDhW_Gqd1g3dT703XsgWSJD_FkhVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوهای تکمیلی و نقشه به روز شده از جبهه جنوب غربی یمن پس از بازپسگیری بندر مراد در حاشیه باب المندب و فرودگاه ذوباب توسط نیروهای تحت حمایت ائتلاف عربی
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/151063" target="_blank">📅 13:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151062">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وزارت دفاع عربستان اعلام کرد 100 فروند جنگنده نیروی هوایی این کشور در عملیات امروز در جبهه باب المندب شرکت داشته اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151062" target="_blank">📅 13:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151061">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxq__il0ezZPHFXA2M3i7aFfLlAcFIMdkZy183HnrIRnAsdrqQeZiFS50AVzZHoCGFnEGxzQKwGzxXPnJGncFaENAF85KoqM-F1KTLuAg_CDlV2NZU58IUaEYUpBhwDiMZi0BMYSoSxrXPOKTMhzJxrwFhBAJMuXUCqZRL5hEjCxPBA3S2anQMa84MfoHDIz77d5Ujgx1Ga0zKUvUAYDVuX4-pUc5pNuODZhhge3ghBBDt92wOpZZmH2yo5x9wCo-JNA_QqOrfValB0icfFK_JmtpjNJqRVyvgMfAaMDKGzQWPfXK3h1Q-udredgkUUXLq7AY7zUnl7p5CY8sBrjcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو آپدیت جدید اینستاگرام هرکی پروفایلشو با هوش مصنوعی ساخته باشه زیرش مینویسه که پروفایل با ai ساخته شده، کامنت هم بذاره مینویسه که هوش مصنوعیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/151061" target="_blank">📅 13:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151060">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
رئیس ستادکل نیروهای مسلح: جنگ جدید دامن همه را می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/151060" target="_blank">📅 13:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151059">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
مدیرعامل آرامکو: ذخایر نفتی که به‌عنوان ضربه‌گیر در برابر شوک‌های عرضه، از بازار جهانی محافظت می‌کنند به‌طرز نگران‌کننده‌ای کاهش یافته
🔴
حتی پس از بازگشایی تنگه هرمز، ممکن است کشورهای مصرف‌کننده انرژی تا دو سال زمان نیاز داشته باشند تا ذخایر خود را دوباره پر کنند
🔴
آرامکو در حال بررسی مسیرهای جایگزین برای صادرات نفت خام است
✅
@AloNsws</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/151059" target="_blank">📅 13:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151058">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
نگرانی از وضعیت اضطراری جهانی!
🔴
کاخ سفید، گسترش احتمالی یک بیماری همه‌گیر مرگبار که از روسیه آغاز می‌شود را زیر نظر دارد. یک مقام ارشد دولت ترامپ شب گذشته به Axios گفت: "کاخ سفید، گزارش‌ها در مورد یک مورد مشکوک از یک بیماری همه‌گیر مرگبار را زیر نظر دارد…</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/151058" target="_blank">📅 13:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151057">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
رویترز از توقف کامل انتقال نفت از شرق به غرب عربستان طی عملیات های جدید انجام شده در عربستان خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151057" target="_blank">📅 13:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151055">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/deFEtkqGcpawnEz_FOs_ERDwyWdf0npJ2YTOiow8TdylbYNuXsJtZGAz_Zc_tFnzeX-eBm4cLgo2JhmXvKhcl9LZ_bKJ_YI3JuWhyBR-NP8cH9JYKO5ahwgiSVt3WPde8MgcOZzzXMp6JgiXDzpvJDJ70xe-AsSMqXFGyRrQ6DEHPyH4PgJ2QT977l6w79juAJQ0rGtScjBbAPAeWgRidBz5DsVuY1W4ShYdEmt1zbc48ILFdAR4CdrKIymk-wazUceR4EVbAgK_0q-7wu5EFhBhbuSRKeMIiHdQtGsGXfWtjV9wsxfIYGOxQUnB9mzj3EmqvOSzbSwLJ8noCDAGmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f1xd0xwBi-w6rf2P2dk3eVcF6IbMlhoaDd1Xn_sJuAXPBfdGqUp54rZHb23gN8AqJ2KtZBTgAG66k5cJ5QJ7v47HCq3f8lYW5V2aWF0yltXSltNeXyaDRQKrvljl766sMk1Ib84j4qfwjKnyY2cOie6IhPpUtpELZnJT5Lol6AEK4I6ihxGlwi5b8kTnE865HpW87t9vrk8_M0sj7fLi7s_cIXt-NS7pcPDntOq6BYL0i5lbJqWV3-ckMYh5wugYiuT6Fgg07G7rDu5yAXoaG5V8UhAg3bySPaHaKTyXoDVEevQ0htwRbcBIKojep7Ry_IPX2r0eDnqnqRT7wIGe7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هم‌اکنون ، حمله جنگنده‌های سعودی به صنعا
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/151055" target="_blank">📅 13:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151054">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
نگرانی از وضعیت اضطراری جهانی!
🔴
کاخ سفید، گسترش احتمالی یک بیماری همه‌گیر مرگبار که از روسیه آغاز می‌شود را زیر نظر دارد. یک مقام ارشد دولت ترامپ شب گذشته به Axios گفت: "کاخ سفید، گزارش‌ها در مورد یک مورد مشکوک از یک بیماری همه‌گیر مرگبار را زیر نظر دارد و در نتیجه، تلاش‌هایی برای جداسازی روسیه در آینده نزدیک انجام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151054" target="_blank">📅 13:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151053">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سردار رحیمی: از امروز هر سایتی قیمت ارز را اعلام کند با آن برخورد خواهیم کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151053" target="_blank">📅 13:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151052">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDWn5RywCMW2vo_cqCi0FoHq8xD49bz020w_3Kmm2tItlmfuZQGqCQYNi2FnckN0dEO7DvogVrKw9rzP6MoiRJwTDWmbJvNV-sWB603upcSUDONdRD1w2ddDXTxuyUGI3DtVelAoYaCyn3jGyyy_FClq2sBpB_qW9tF0Ap_6ufKNKGbgnxWP036b1wa8O-u4OpgwBnY6QpokGj-UB0oN2FfxghV1izZvNL9VCvHBFl_3C0Clh5NvyaYl2wWyQghq4M4uzfMPmrdnzDnSyt-uHgLGlh7q0ypOG8-TWg_2eg4St7BlZgYFmJluVJ8xBI2D_51GuGRiYUDpP5eVkQjfRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اعزام سوخت‌رسان ارتش آمریکا از اسرائیل به امارات!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/151052" target="_blank">📅 13:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151051">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7R-px_OqGLnqkCUQ0hCsKGcolkyPZa92trvBVhEkSFSjaFfzakekh4HjyGyYnK-Sg5nSWPJg9sbypfRveEqFtsY9rbmtYmEM7QAl-KGLcevdC9P9nk4w0pNpsVV7AK_rbNJoPM0hKRNFzGBJfq7_5kscs5HDLHz4nhsAcBOjiWi0a3y6-jHWlFfXREFWMwWy1ecE9Jd1QleNu8-bTpJvUPkpwKPJSlziNvb9mm11BAnw6WqZsNW1oYC4v7AaaYgH58-Ya0Wo4zVrNVxDEYb_ZYTrLhvW0U8oVqFyBeASJLKnq5FaroLnmYV4tAvG-TEmZTovYYAjjFFnHGoDwEnTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابراهیم مصطفی سلیمان ابوعمیر، یکی از فرماندهان واحد نوخبه حماس که در 7 اکتبر وارد اسرائیل شد، در یک حمله هوایی در نصیرات، مرکز غزه، در آخر هفته در عملیات مشترک ارتش اسرائیل و شین بت کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/151051" target="_blank">📅 12:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151050">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
رسانه‌های وابسته به انصارالله (حوثی‌ها) اعلام کردند که نیروهای حوثی وارد شهر العین در منطقه المواسط در حومه تعز شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151050" target="_blank">📅 12:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151049">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
رشاد العلیمی، رئیس جمهور یمن گفت که عملیات ضد حوثی ها "طلوع یمن" نامیده می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151049" target="_blank">📅 12:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151048">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
تحلیل الجزیره: ترامپ قصد دارد حمله‌ای غافلگیرکننده به ایران انجام دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/151048" target="_blank">📅 12:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151047">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e7be5e65.mp4?token=GiSwQ-8RVdUP1baJ9WN_lZND6JBWcD80w-GY4glXSXstPTb3SUfNLM3nZLpP7riHUxbP2XG3kl2cmZgOk9kUEAsfzBVZlQuaUJt_1GABXzTTASuTDtF3njkuomL897yiL1udwPZzOp68vc-soIX4fojSjEmCsNUzQYNPsRm9An6oNyczxOzsDy662_SJ7De_jrlsC9Tn_oBbvfyAroWky9-2-jypKQ_I_JNyDWA_R2mPSqFAL-oOJFz6WVX_YkRiLCFI5sO8n9srrXjlJUs7-8L5-xwP_zzAEswutQpa5TOkZNzbgiKxar4WbOkB4ByRU9NFk9dfbkpNOi227XXL-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e7be5e65.mp4?token=GiSwQ-8RVdUP1baJ9WN_lZND6JBWcD80w-GY4glXSXstPTb3SUfNLM3nZLpP7riHUxbP2XG3kl2cmZgOk9kUEAsfzBVZlQuaUJt_1GABXzTTASuTDtF3njkuomL897yiL1udwPZzOp68vc-soIX4fojSjEmCsNUzQYNPsRm9An6oNyczxOzsDy662_SJ7De_jrlsC9Tn_oBbvfyAroWky9-2-jypKQ_I_JNyDWA_R2mPSqFAL-oOJFz6WVX_YkRiLCFI5sO8n9srrXjlJUs7-8L5-xwP_zzAEswutQpa5TOkZNzbgiKxar4WbOkB4ByRU9NFk9dfbkpNOi227XXL-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی جالب از ناظر مسابقات در لیگ افغانستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/151047" target="_blank">📅 12:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151046">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fddr6OnpD9v6ddUnuLTMp_GS2B7MldQU34fZsUEGkgScYE1da2FPE1N7lx4hpKFRZDNxOf_0tDRGuAPOc1SmLGL3IK3HktPwKiABYf695H24AFALqHCkHyekitCT4UugfKsQdAEo0XVU8QaE5RLcyKsNDyu9RxEwY8EVTWc1MHqX_yxAADdn2tth9cHkvNXqvvEPKuTprfOrRp1pQeq6tn7OWp4jV_vYdRdtDeW7ounbXYl_CG9odhRehL_kArDKcR0-A__piZTr7AhXFQhj0LGFZss3wZIqn8D8M6SZUOEzoa_oRWkCykFeAnQPklJNf59Loi1MPZ_S5C6QHTCPXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به نظر می‌رسد که فرانسه نیز در جنگ یمن دخیل است، زیرا یک هواپیمای فرانسوی مدل A330 MRTT در حال حاضر عملیات سوخت‌رسانی در نزدیکی تنگه باب‌المندب را انجام می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/151046" target="_blank">📅 12:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151045">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
نیویورک‌تایمز: محسن رضایی،هشدار داده است که وخامت سریع اوضاع اقتصادی، کشور را به یکی از دشوارترین دوران‌های تاریخ خود سوق داده است!
🔴
این اظهارنظر صریح و کم‌سابقه، روز شنبه و پس از گذشت بیش از هفت ماه از آغاز جنگ، در یک جلسه عالی‌رتبه دولتی بیان شد.
🔴
کارکنان بخش دولتی و خصوصی، از جمله پرستاران و معلمان، با انتشار مطالبی در شبکه‌های اجتماعی اعلام کرده‌اند که به دلیل ناکافی بودن حقوق برای تأمین هزینه‌های زندگی، قصد ترک کار خود را دارند. همچنین، بازنشستگان بخش دولتی در اعتراض به عدم پرداخت مستمری‌هایشان دست به تجمع و اعتراض زده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151045" target="_blank">📅 12:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151044">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJONR2IknsE0ha_M4J8mcRNATaHxUk1X7t3WExllUCbjtWPGJvRlJbsMwPmTcHhwuUS_0G5usAasCl-0MoLsT-LBU56ZWRPhbvw7sqaZdacl0LabIs7egectYTSxX6cWMsW5hI_DTvjlyHE_fHS4M4oaz9XSAtElarqskG_c-LAcsmA5M9ZFAPvkz_abSXyBIVjg_ku4FxV85XVnRRQ32ypL_cW8sNaXvNuAxlxjxKgQHLS_0DIlMpT-HiRa8tQ6jDUmf2GEvN7wXUsQZMpcb1yuH_9VG9nUpcc_83SUMyqW12mbYijkELQgALamp2YbUaAHJbanIxWoF2XO_LePOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فدراسیون فوتبال یه بازی با فلسطین ترتیب داده تا قلعه نویی بالاخره ببره
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/151044" target="_blank">📅 12:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151043">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd2b481530.mp4?token=k27qqSS9Q7ZJYJo7DcDo-L8sdirAVHKs4WNEKwt6hncM9tVLJKIr0QtRd01QCuBBxQy-j9BRGonYnioMTFlx7L-ofrtZ0KSuX03TPOk80-zL5XbAkLb05wKEw38CNAdVWHwN78fs-jh8jnX4rYLscVA2RAwj6IFmGZnAjC_yDz-Y6ik-IhQ1H0W_IWJjA7qpG4gXnHFyRRnhAukU_BBRrBUKb2tQGKBqWUrX6ZpHaM4-WcQmR-I0j6dJue-twUTmGvOynHwGqLsEskdk3jlfcHRvK3Vv8at76mJlyiKhv5ih83BnJrTOsFTTOYQzzv0JDEGOj0z06KnxEVIWcd4X6A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd2b481530.mp4?token=k27qqSS9Q7ZJYJo7DcDo-L8sdirAVHKs4WNEKwt6hncM9tVLJKIr0QtRd01QCuBBxQy-j9BRGonYnioMTFlx7L-ofrtZ0KSuX03TPOk80-zL5XbAkLb05wKEw38CNAdVWHwN78fs-jh8jnX4rYLscVA2RAwj6IFmGZnAjC_yDz-Y6ik-IhQ1H0W_IWJjA7qpG4gXnHFyRRnhAukU_BBRrBUKb2tQGKBqWUrX6ZpHaM4-WcQmR-I0j6dJue-twUTmGvOynHwGqLsEskdk3jlfcHRvK3Vv8at76mJlyiKhv5ih83BnJrTOsFTTOYQzzv0JDEGOj0z06KnxEVIWcd4X6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مدنی وزیر دلقک اقتصاد: درمورد قیمت ارز از همتی سوال بپرسید
🔴
خبرنگار: همتی هم گفت از شما سوال بپرسیم
🔴
مدنی دلقک: نه دروغ میگه از خودش بپرسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151043" target="_blank">📅 11:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151042">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41508d2063.mp4?token=YOKHtoWGGSuPq2lcpbS4-tEYwHgUzkGtzdccrFQV1XRN2iOKL_G18Y6VUMmy_QN8x0Mzks0VMcto5aAJ32F8g9OdyAN3bflnEH-TYTVfIKbGOMXsYNzs8wOxHOzVawKhxjOKAbEqwiw-wfN86J4sMUW_RWmnJGKnmksEfBWkegpwwRnpdlQLwfo9skDP4rPbBLL8oYJv35BEIILnK521KfGUNWUvM63O4CcRFpHrZnuJ_KNoAij60GPyPeXzc3RYZbmaxqjUJqCer6OUtHMJtaFbocfFaThse1t9HFd0IWiLUZ7PzlFzjrAIuSSpPjirOhz6Ee4aNGNY2GXOzit_XA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41508d2063.mp4?token=YOKHtoWGGSuPq2lcpbS4-tEYwHgUzkGtzdccrFQV1XRN2iOKL_G18Y6VUMmy_QN8x0Mzks0VMcto5aAJ32F8g9OdyAN3bflnEH-TYTVfIKbGOMXsYNzs8wOxHOzVawKhxjOKAbEqwiw-wfN86J4sMUW_RWmnJGKnmksEfBWkegpwwRnpdlQLwfo9skDP4rPbBLL8oYJv35BEIILnK521KfGUNWUvM63O4CcRFpHrZnuJ_KNoAij60GPyPeXzc3RYZbmaxqjUJqCer6OUtHMJtaFbocfFaThse1t9HFd0IWiLUZ7PzlFzjrAIuSSpPjirOhz6Ee4aNGNY2GXOzit_XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صرافی omp فینیکس امروز تمامی پول کاربران خود را بلوکه کرد و دیگر در دسترس نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/151042" target="_blank">📅 11:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151041">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
هیمتی: دشمن بازار ارز را هدف قرار داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151041" target="_blank">📅 11:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151040">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
خبر کوتاه بود و دردناک؛ علیرضا سپاهی، امروز همزمان با اذان صبح اعدام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/151040" target="_blank">📅 11:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151039">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BecZjJuf5CS2LfzrP1FWsUkZ0hMBa77H4jUTzccDzNouZXpE9jV0XedKJ62t-f7k_SA5EUDnJOwZVFuA3hXbo1QYlGXrA7lfdS3HIdp-YRnQ71IodzCSuQ0rYgIz9pHQTB8E0sA3T4ntpuRvWJfxzqw5chdrmW6ttvqZLhnJXYMSOEHp5DkB7t19yKtuhZLT7I0iB23mXr9ZrBsZXMiFasgMuouI3h5KBcYJQv62tFn2lwY-dMqGNR0HZmw-D2QnzljjjnQLvvjtdE6La3FOthLTUVhlnjYmAX5bYlrNm_VhZvYKQBJhT0tk9k7KMAkqU4UQ_llqCug8QLzsI1mnlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبر کوتاه بود و دردناک؛ علیرضا سپاهی، امروز همزمان با اذان صبح اعدام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/151039" target="_blank">📅 11:39 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
