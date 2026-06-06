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
<img src="https://cdn4.telesco.pe/file/slUOgzZ26LQzNTPbnAtSW8BTuR8XqeiMFhyGDgZkpFP8Tuz4CsN7IOkscu4IKbYYT493gfVMXVb8UlJAvrUCAdB9tAwQ_-F5hG0-Oph8K2D_ItKCMb9R4Bnif4Vi0qxCLqJwewAmyavF_PLSqVmYqNS9vdCQjbd3bqanD2UjwaVzgulGW3hLx6zjoyuf-rLXu5TXsRh-4ns_NvoiKo3YfKAbPWww1rOejUQ63w9VswM0BhKqCpG5pvgb_7w0LOI9T2oPMt5MHeqevsNTD1MoaJUS3zW1UVtJnL6iqmrrQIfIIslS4NZom2qkS-OVmPbQzW6ic-fv33bkMtf5lTvfCA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 228K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 23:34:57</div>
<hr>

<div class="tg-post" id="msg-65353">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf1fba69e.mp4?token=dTGOGaMhQtFlsKJYwh0nTTkSwosGsFYNhOQqPZMGqPdjyQ1NYdPgSnTKXtdBpPWpjBW9A8Al2bQPo9JBqRRIjJgfkUe8wEiGk9fanla4lSeM0sa2Gpl-VPlf4fX0_Cwg_7GSOr4HfFY7zTJe09Ts_ewKcJTFXM5C5R4UQir5Es_Ld5ONWF7vVelC49HC_K0MgdSRt0fhxMpg_82rdv5Ajp-iL1yoB1151ptCVpbTbmesIe6RG-uahbaxdwgOCOg8Fd9Vd8JzSD2mJEFwHcvmDskl8x8mkRArM1s4BwOQ8blWqSvJ3qzKIiDJuLNE2Cq-Bq8TLPANROJtNpTmjF7ZkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf1fba69e.mp4?token=dTGOGaMhQtFlsKJYwh0nTTkSwosGsFYNhOQqPZMGqPdjyQ1NYdPgSnTKXtdBpPWpjBW9A8Al2bQPo9JBqRRIjJgfkUe8wEiGk9fanla4lSeM0sa2Gpl-VPlf4fX0_Cwg_7GSOr4HfFY7zTJe09Ts_ewKcJTFXM5C5R4UQir5Es_Ld5ONWF7vVelC49HC_K0MgdSRt0fhxMpg_82rdv5Ajp-iL1yoB1151ptCVpbTbmesIe6RG-uahbaxdwgOCOg8Fd9Vd8JzSD2mJEFwHcvmDskl8x8mkRArM1s4BwOQ8blWqSvJ3qzKIiDJuLNE2Cq-Bq8TLPANROJtNpTmjF7ZkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نیکزاد، نایب رییس مجلس: تنگه هرمز طبق قانون مجلس به حالت قبل برنخواهد گشت، تنگه هرمز برای ما از بمب اتم مهم‌تر است
@News_Hut</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/news_hut/65353" target="_blank">📅 22:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65352">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
صدای انفجار در جزیره خارگ
تسنیم: خنثی سازی مهمات عمل نکرده دوران جنگه
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/65352" target="_blank">📅 21:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65351">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZ1UMfH36ralkUN9ZvfXhQn1zvY0fCl_xpgPJS6O9m2aVpL8JTyTtDzFHVtgsZX61D4KIzAP4k-u2wmMsT4w3Lh7zGzDQQHp8tQAemgU5ylpaMavYT8pzlhNhUzDI_iS3Z1-pPfamHYrdrpLB5zt8ynJW6SVBzXEnoQJ17fCFKSmTUiplupj602fgYQTMuM4gs_PrFP8BumLsDBG36sl8bDNiZiB7rzYBsxEyatWPDJ2mlwgeSeo2L5bVLnzn8mLKouB465y4cIR6CRMQNUuet20Wv3ZTiFD1GkiyDHx7QpR1np5PeuJM0qMW21LX68_1mRYN9_Rr9pc8HpejNC7oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تو تروث‌سوشال: کتابخانه باراک حسین اوباما، در ۱۰ سال، وقتی کاملا به بلوغ رسید!
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/65351" target="_blank">📅 21:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65350">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/457010896e.mp4?token=dkQxWNBkiRuI3z5YQFA72TJwvK3xMc3FURpoNrsME7zs5AvzX3nFipwcE3IjvFQkyuH-23OcfNV4uq_UJwtt6hacEln1enI9EXRctXlJzFJRz2UGgbZKnRAbCAGSy9eRBQJJNH-6IvJrE2cRGT4Euc-XcMyXWdZmUR3Lt5n6vj2q3W9H6c60KdjqzanBiXT8ItayO81aAd8GiIALe5SGoGn6YnU0Fe7iUfzKryslMWqDWU9SHL_mhL3MMzm-LxgbXm_0TzykGjBAbu4FqDEnTFo-Qy4V5j19rHgIW7dRbV2lPUYKy4k3TUqmGMAIMQ9lu6mH6M5nwhIthpIHRwA8aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/457010896e.mp4?token=dkQxWNBkiRuI3z5YQFA72TJwvK3xMc3FURpoNrsME7zs5AvzX3nFipwcE3IjvFQkyuH-23OcfNV4uq_UJwtt6hacEln1enI9EXRctXlJzFJRz2UGgbZKnRAbCAGSy9eRBQJJNH-6IvJrE2cRGT4Euc-XcMyXWdZmUR3Lt5n6vj2q3W9H6c60KdjqzanBiXT8ItayO81aAd8GiIALe5SGoGn6YnU0Fe7iUfzKryslMWqDWU9SHL_mhL3MMzm-LxgbXm_0TzykGjBAbu4FqDEnTFo-Qy4V5j19rHgIW7dRbV2lPUYKy4k3TUqmGMAIMQ9lu6mH6M5nwhIthpIHRwA8aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با وجود مثلا وجود اتش‌بس ارتش اسرائیل اعلام کرد که در طول آخر هفته به حدود ۱۵۰ موقعیت زیرساختی حزب‌الله تو جنوب لبنان حمله کرده
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/65350" target="_blank">📅 21:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65349">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65349" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/65349" target="_blank">📅 21:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65348">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fq74Skiwj8lpulBHL_xdJUvNO7jVCh0PPwjxZWjRsfk9wFE4d5Gl05qPZWGW1yK7JikQ3mm3xTX7QYmGV0wowfZOP42Ebu_FNFvlFo3nrlU5AqLrTukacEPAeNiUXhMO_vEFRmI4l2ux3VzP67Kku4Qr_FtjClOKKPVd4GVnB_xByiFfy0TPdPp6X8bYDt8mxRQCOatnQkBJDPN2G35sG4EwD1v5APXk21zrMlJBv9W7hurVkk7bFpFckRIc_ZquTXizewEYvJSD3jG6Vnf4aUBLUyGDj2omnaeikY_LagiCzykWWhC2ON0RppzgM9dZAGCuEiv2zYKExVgGPCj-dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/65348" target="_blank">📅 21:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65347">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6388d22ab.mp4?token=HzA01cLnumOwxlJKzeFnlDD5vN4-Gsm76qiQTI0CG1fdNtd-hokFOMI9ePKZeHbl2ZV9h-BQlxPg8LUTY1_6Osh8ateuPosMeuczfEg8ZWcRzxXE9T-0BF7NqRqmcjIXANg0vrSwDriisiArtdW-xQyo7bsDRY1GhDfpxjDtTAeofpqJiYIbE0gCkaovTQYe-RgAYoBE5dBuL7ObfoDkD1g0yhw2KF3PhvaYdBilVq7PxER1iAODFRJnp0qBiD_sAKmQNd63E33jlOllLo-7C8u7qfWrmO7QMb_dNbsDKZQgTmvqyKHr0rihO7eIdcXXhjvBYOR_H8S90VOlBQRwrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6388d22ab.mp4?token=HzA01cLnumOwxlJKzeFnlDD5vN4-Gsm76qiQTI0CG1fdNtd-hokFOMI9ePKZeHbl2ZV9h-BQlxPg8LUTY1_6Osh8ateuPosMeuczfEg8ZWcRzxXE9T-0BF7NqRqmcjIXANg0vrSwDriisiArtdW-xQyo7bsDRY1GhDfpxjDtTAeofpqJiYIbE0gCkaovTQYe-RgAYoBE5dBuL7ObfoDkD1g0yhw2KF3PhvaYdBilVq7PxER1iAODFRJnp0qBiD_sAKmQNd63E33jlOllLo-7C8u7qfWrmO7QMb_dNbsDKZQgTmvqyKHr0rihO7eIdcXXhjvBYOR_H8S90VOlBQRwrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پخش دیشب برنامه «خیابون انقلاب» بخاطر این حرفا لغو شد.
ما اسرائیل رو تهدید کردیم اگه کوچیک ترین خطایی کنه میزنیمش، الان لبنان رو با خاک یکسان کرده و ما هیچ کاری نمی کنیم.
ما همش الکی تهدید میکنیم اگه فلان کارو کنن مام فلان کارو میکنیم، خب چیشد پس؟ یه بار به دشمن نشون بدین که ترسو نیستین.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/65347" target="_blank">📅 19:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65346">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVlk4X1EUtS8ij1HLOr6uEK1maAUZBw9GQALpf_nfaX4El7lEGwIKLsBJ2dzVGtrghxsMF8iKwMlgiQQASy7-_5WEZUrLRLIRPagLSUiYtOAtr3SpMrxiBq006mLul7rfzCFMUAL_gGRibzHeNtSP76rZmIOozh6zF-BYzwA01iIhDREA28NEzhsqb_MlloQ-ppfQf8aWzVZk-W5iDoi72xZq0UwH0EoRARpSAWrLbh9Q2hH0TgWYnKgrAdTbhML3CnPO1Z-Rth4ae8jGn8TnEJfpQOW8kDaYrCmN-GDu56nmZi3nNuW123DqYP95VDk3gzqsDF2S1dfp33GVFZ89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام وزارت آموزش و پرورش رسما امتحانات نهایی پایه‌های یازدهم و دوازدهم، به صورت نهایی و حضوری از تاریخ ۱۳ تیر برگزار خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65346" target="_blank">📅 17:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65345">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f4e56d3b.mp4?token=BRmcZRcd-5urSXMbXW0BPcjUj72XeyWZ8F3NOak5F7kNBv2AhnYHrRaM0nZE-Zq-bmPaa2MZQ66wCW37r7QB015RY2kbCB0vlIpaLCEJ8ws_3ZK_qbiBcxFXUgxEF_CWgQXGCSqXnm1ABw78WjC8r350G3Jq8IffalCdN2CIDSMWZxdcv9FJcsj4Jwaudd4FEy2c-r_VggD5bPznuC5EyNe4TT7jnfJqiKSAG_PwZAk5mALgx2mAZdroJcAkau4EnbzrZr_i--5Tncnv0EZFI39kEsOakR1y4QONt9L0_lbt2MlVeV9gxJy5pFcKFdAWmZU6QK84pS4mnbZEhSiUng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f4e56d3b.mp4?token=BRmcZRcd-5urSXMbXW0BPcjUj72XeyWZ8F3NOak5F7kNBv2AhnYHrRaM0nZE-Zq-bmPaa2MZQ66wCW37r7QB015RY2kbCB0vlIpaLCEJ8ws_3ZK_qbiBcxFXUgxEF_CWgQXGCSqXnm1ABw78WjC8r350G3Jq8IffalCdN2CIDSMWZxdcv9FJcsj4Jwaudd4FEy2c-r_VggD5bPznuC5EyNe4TT7jnfJqiKSAG_PwZAk5mALgx2mAZdroJcAkau4EnbzrZr_i--5Tncnv0EZFI39kEsOakR1y4QONt9L0_lbt2MlVeV9gxJy5pFcKFdAWmZU6QK84pS4mnbZEhSiUng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این وسط یه آتش‌فشان تو هاوایی امریکا به شکلی آخرالزمانی فوران کرد
الانه که تسلیم تیتر بزنه کائنات انتقام مارو از امریکا گرفت
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65345" target="_blank">📅 16:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65344">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJcIJZoR0nJQFjO3bLILI2behQ6eXgzFAPWu9pVgmSYXOX4FhRXD_4L39tqZrlSZphfMcMLy3goFbKtpwj1I_eGTD0YINJ4FruGH7zgqZ0wiwPO65I9_usrXu7CbzbWjHLXRO8Z7t0_GjgvX0uPLDlxs5QC0GMDkISWp0N4TiBKWEKFSeBrPGK0x2YzCt92iUQ5hpOM-lpeoDsYstRtt7wlH9xuNet0XpKXUkoVu4YvdSud6WeqPlSHp3WfNTn7UX0FYUS1342rsAJTuktGZnEXTa5WYw66WYM7JNuBfASrr9KdIhqosdPFXXE6aZVPYzi012DtUlfl8XLipo7xa7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جمهوری اسلامی پاکستان به دلیل فراخوان اعتراضات مردمی اینترنت منطقه کشمیر رو قطع کرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65344" target="_blank">📅 15:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65343">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01c119656.mp4?token=oK6UOHEdyvk6UM4VYUytC2YIeH3_jScftyrUVZdOnbA6wdX_3pYc7TB3-4vjmPB3IvSGzlB7Sd9-MIOhpZahd4YWIc-EfNZ3yZPavTLPEU6RsrFXk1d-9oCW6lKV4FT_-yBPhllSFHMNlNlmIr9_YVgwkOaXpxIEWMw4MSDYbPIZKtBl2rKHJKUwe1NXx8c7L5A7aqF9VW9BTOcKZ3kMx114wgDT3gGuPSaHSWskskTfcrub3Jxj6_2N0Ct3YKf931GodUyghEVk18KsQhGnpToADYo1r5fvq__9LtAf5_ZAsGMjoJOod2VSVIohGYoDrx9y7bZkANE48zPAxptJ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01c119656.mp4?token=oK6UOHEdyvk6UM4VYUytC2YIeH3_jScftyrUVZdOnbA6wdX_3pYc7TB3-4vjmPB3IvSGzlB7Sd9-MIOhpZahd4YWIc-EfNZ3yZPavTLPEU6RsrFXk1d-9oCW6lKV4FT_-yBPhllSFHMNlNlmIr9_YVgwkOaXpxIEWMw4MSDYbPIZKtBl2rKHJKUwe1NXx8c7L5A7aqF9VW9BTOcKZ3kMx114wgDT3gGuPSaHSWskskTfcrub3Jxj6_2N0Ct3YKf931GodUyghEVk18KsQhGnpToADYo1r5fvq__9LtAf5_ZAsGMjoJOod2VSVIohGYoDrx9y7bZkANE48zPAxptJ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام ویدئوهای حمله به سایت‌های رادار ساحلی‌ایران در سیریک و جزیره قشم را منتشر و اعلام کرد حملات تلافی‌جویانه ایران به بحرین و کویت رهگیری شده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65343" target="_blank">📅 14:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65339">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJoilsnCOSS0hN7TiXSKCk3nH_0REtNYj3C4Sg2qak7bAFn_vcLx1wv0_kkAg0PWwP1XK9FWdpUMrqTEv0XkpHJGYw6h45j-eKr4gnujygo0vhy5ASk_oWQq7QaiaOgVj918awLRYw-SE0Ok2jWj-3SnMenR9UpdAvZ2XZ8jtjT1wqLbvRP078oUNpPL9nDcsTtvhlU4iQHfvnPyop-6l5UIgltP5D0IXspxo-JAYofP24TIQh8oXjsBCbhN7DadmLeJcOLdwepFPqTyaZddNTiH6YrW1DGDOUzixkIjyzctHKPayy81-5bRzYAq8g68Qeo43BwWUciLT8cNoa9X_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KW6xl70wlMU3oa010Y__BnOrBb89Iu7Xe05923jQc_6bFau3WG6dx5ynpKhecqy9Ecxsy5D16LpQ4Q5fPLGSFSiI2HGWFBbwGyIwiF6x-3F1EyInjw6hfT-COdWUhzsthJsHTe-ufMYtQn8yHR5sKqDUu6MbUuWzlSOnFtp5GfwLTrwTcP9rg9qPjOjl7i2KIbUmN3j9YlZNlBhfYnGsh1FxiciAYE1dOP9cwa4eKEe8mua_E1D7XAiUw7bNr12PMnGTKMAzs39g04pOB6ZQ4bzrMPEerHDdZ-Z_5knoxN6NO0uUk6cu4CGEiUxw1ynPJuHfQhSgqTW_rYmZ-RBl6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LxdxCMvUFAhSBM7fsMrP1dnqBrub-MQIfPjWDkB6jtkVxjVLIZvmNoJhrggxSTddapIdvYYtQhoqvU7UdUNgkKR0a3l6GEnggqIDqVKwfGyag3Dl6Lk9Jmie1YfFYFlGNxMlJO9xAcYCuaiStDBjIia-k4Vs5uCzMdEl_Qy32nwP6aAyc9m14mKK3nQ7yodFjaeANlVVLSDZaoggAOUa1jmx2oGTxUSfwpkG52piUxnyeIXdHRcj1YT1_wyBeJg9PYHDgyBPLC2NAEa8v4Nj9L13M7OkZgrgYY7ZcaAYEhJqYXrVvZB826USy-6e8f5DgJtBYqXaWxKkC_nTMxmWFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65aa546373.mp4?token=G_K7kwpThL5yrr18HSrjRqjTAZ3pF4Gmv71JfxsjLcwhPKG7lT8gN2cRkOeNMbOvb2SOzsxBszjAsq7NwigYME-KADWmQAJFxhZWyGbVez6vUkPmT_kirNh5YRdCcD9BKelLcHJs1BsKQrrrotTh2b11yVdw9tns1e4-JJ04FKwC2SVZrLE9ZSPmrvPhTdWnDW5fRdpYOTKIV_2YVzghdCPXfvbe5XhdHtYWNMWrtMOuYq_CebDApcsWH12B4NP3uq8V11U7G_Jk12X1JfEnBj-hcMKlbZxsYDezFMQ1cxPDSINMkeuLrDM6M495A453cz5TKjccVV85KLQcLGbkRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65aa546373.mp4?token=G_K7kwpThL5yrr18HSrjRqjTAZ3pF4Gmv71JfxsjLcwhPKG7lT8gN2cRkOeNMbOvb2SOzsxBszjAsq7NwigYME-KADWmQAJFxhZWyGbVez6vUkPmT_kirNh5YRdCcD9BKelLcHJs1BsKQrrrotTh2b11yVdw9tns1e4-JJ04FKwC2SVZrLE9ZSPmrvPhTdWnDW5fRdpYOTKIV_2YVzghdCPXfvbe5XhdHtYWNMWrtMOuYq_CebDApcsWH12B4NP3uq8V11U7G_Jk12X1JfEnBj-hcMKlbZxsYDezFMQ1cxPDSINMkeuLrDM6M495A453cz5TKjccVV85KLQcLGbkRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بعد از درگیری های دیشب سپاه با چندین پهپاد و موشک به بحرین و کویت حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65339" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65338">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIamXerxess</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65338" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65338" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65337">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIamXerxess</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXMIaXZ8SKnVPVosUb_DseL1nI40jXQf-8zy2OBYE4ow3RJYLCoy3eL-PkULlkMQkV0DVaIg9yxhQpsqGgTyur66pQMOR8XnqoScskdi4LZ-tiD8SZuVhw-qOuS3lkoAM1o0pGholGwvvNIdcHSzjJR-Dqc-Ri51uw-LQrm_7rnU1W6jlg-Rrt5-P_U-KX1fEUeUx2FB3rLGFzHnx2wyu6HpmJdZ62lJ6p8GQnaXIE5VXeXd2aTj0-zjZeuVbMga91v80lmLtU32AKhh5RhfJaz2kjVJw3cgpj99xyD0XhKI2BoY6qaADiF0dJn7nTglTCX-WdqdIleJ06ZoJCw0aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥊
پیش بینی بدون ریسک بر مبارزه
Muhammad
🥊
Bonfim
🥊
🔸
اگر پیش‌بینی شما اشتباه باشد، یک کد شرط رایگان تا سقف 100$ دریافت خواهید کرد!
🎁
💥
با پیش‌بینی بدون ریسک در هر حالتی برنده باشید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65337" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65336">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LladEuRVWOXufEgB68FdTi2sMUZSuuwIsFBDeSv5cYSoLswBgd6yTuSZcKUzwVfq4vI-r_ABEpTb3IQVw4PCzLRsQ28lR0xeDsDbr6vvdk-IMg0MD9U0ub7Zp3kc69YANnfkZZpNO7TIlyBLzVmqUdA9NmbBmXPOvEAVfPffktWY5bkzaVtSWTVMrwzdf5ifbrP2_voE69d4d7aWNS4zB1s50CnmoXnFDUHua0WLxnlUNdPdynMiOqtXF5UAUznasT4u4wz64ybhQJ2af-eJ94SvmyIWiYnXoIboI2oCKYrVDOJOjWRyJMjjBm0UK1MwN4MGwTxE2EDmPdPkOq2wbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
بیانیه فرماندهی مرکزی ایالات متحده(سنتکام) درباره اتفاقات و درگیری‌های دیشب:
چند لحظه پیش، نیروهای سنتکام چهار پهپاد حمله یک‌طرفه ایرانی که به سمت تنگه هرمز پرتاب شده بودند را سرنگون کردند. پهپادهای حمله‌ای تهدیدی فوری برای ترافیک دریایی منطقه ایجاد کرده بودند. نیروهای ایالات متحده پس از آن برای دفاع در برابر حملات بیشتر، سایت‌های راداری نظارتی ساحلی ایران در خارک و در جزیره قشم را هدف قرار دادند.
نیروهای آمریکایی همچنان هوشیار هستند و برای پاسخ به تهاجم بی‌دلیل ایران در دفاع از خود آماده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65336" target="_blank">📅 11:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65335">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQVUZ9qaa8VoL555zTz7uiTTTJ93fYRbriWVe5x-tUay-ybdVp9SCssgmKzdRuqIJs7q8RT7Ct3ndJTSKcDcDp2OriFpewDcoeRWYCPV6rBfOmI-oiykPvO9EPxelkJbxL3voxou9fN1W29kq15jei4EWemhEbQ_u0o14ZGGQPJIiOvchXMZYd0qjtNVnhaOLVy4jPq9RtbDgW1TiyaozJHeoTMXYTmvcQL-ZOjEqqE69ZMRjCVA-U-ElBL70tfMRfIKmD4pUpgYp2tAKnrfgru_N8Emf7grRac5mcZHWkCpvBVaZ0lM4TatjnRo9KWG9ZdnqyJPmGxfIT38MQMjsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم خمینی در سال ۱۴۰۴ Vs مراسم خمینی در سال ۱۴۰۵
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65335" target="_blank">📅 10:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65334">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887b98bc21.mp4?token=hABZHLDuBqfun-vP7isEWkomVco7JuffiIKyl4Er7uo32INI6on98CzM3kGQYiStp_IM017quPbmCf2iyRo5xkOX7XUnRSIx5he0GiJwmD_Frlx4umOYqsJnt31Sbn-2-Uej2YEbyKAEmFyhSVEHX86RIz-B1FVaasNrkDYyqFKqKv5rLyQIQSi3w4J3dNUuR6Ocv4MAtQ8zNHJF4M9qKVKviYrStWaCPvsdmMWRsCNoe-G3gQe-KBCC9nUlq6BHvoLBQ0pjqmjET4SyR7XryU0jf9PZJiRV4gl0tePlXSwKP1vC3n-KAU1PbSQCIv6G11QcpuPNIhWkLLHahyK-Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887b98bc21.mp4?token=hABZHLDuBqfun-vP7isEWkomVco7JuffiIKyl4Er7uo32INI6on98CzM3kGQYiStp_IM017quPbmCf2iyRo5xkOX7XUnRSIx5he0GiJwmD_Frlx4umOYqsJnt31Sbn-2-Uej2YEbyKAEmFyhSVEHX86RIz-B1FVaasNrkDYyqFKqKv5rLyQIQSi3w4J3dNUuR6Ocv4MAtQ8zNHJF4M9qKVKviYrStWaCPvsdmMWRsCNoe-G3gQe-KBCC9nUlq6BHvoLBQ0pjqmjET4SyR7XryU0jf9PZJiRV4gl0tePlXSwKP1vC3n-KAU1PbSQCIv6G11QcpuPNIhWkLLHahyK-Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: ایران با آمریکا به توافق نرسیده است چون رهبرانش «قوی» و «مغرور» هستند اما «آنها چاره‌ای ندارند.»
کمی زمان می‌برد. شما درباره ۴۷ سال فرار از هر کاری که می‌خواستند صحبت می‌کنید.
یعنی، این باید مدت‌ها پیش انجام می‌شد. این باید توسط رؤسای جمهور دیگر یا کشورهای دیگر انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65334" target="_blank">📅 09:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65333">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65333" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65332">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=vBG2qlSXCgi5FzqjjlxS59-SU155wYHqpzosPCJtd1on9QBIWgd1to3woFxSef2ZYfXscs2f8RBo20kKhV4Dt-YQcnnVy1ghtq8DNZ9w-LEffAEvQcXxjlx2wrRC39kArpJVHvYEuR1V6tZAiBLPlHCM69KvNwIDSKbjW4n8QDQgfTUn2FAgiVV0OmY3Yhi5BVq1s22pGjHMY1vhuOUmbI9I12CbyS2I2AbClGNmGg_ND900tbssjhKEiriorv02x1KcjB_G7OCoSRPMWA8Fh1zJJ9nm6osfemxm9aNWrsqA9gfyrVcZ__5s4umJerq-OALKdVy440RXcZp5PUs_ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=vBG2qlSXCgi5FzqjjlxS59-SU155wYHqpzosPCJtd1on9QBIWgd1to3woFxSef2ZYfXscs2f8RBo20kKhV4Dt-YQcnnVy1ghtq8DNZ9w-LEffAEvQcXxjlx2wrRC39kArpJVHvYEuR1V6tZAiBLPlHCM69KvNwIDSKbjW4n8QDQgfTUn2FAgiVV0OmY3Yhi5BVq1s22pGjHMY1vhuOUmbI9I12CbyS2I2AbClGNmGg_ND900tbssjhKEiriorv02x1KcjB_G7OCoSRPMWA8Fh1zJJ9nm6osfemxm9aNWrsqA9gfyrVcZ__5s4umJerq-OALKdVy440RXcZp5PUs_ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
🎯
همین حالا عضو شو و شروع کن
👇
e15
https://t.me/+6ckCmywafrxiYzk0
https://t.me/+6ckCmywafrxiYzk0</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65332" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65331">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4ZD0Y3Efj9HCxDsHNectq2yecEM-BjsYiayyKOI80AB1hFyTkVA3nSpN2EPfy8SEAW_mcR8PTxPZMXUZ8J4yrb5uwiGwEIdxkhtvp54aly1n1d8U_sS1ggmi7CoLWKXn7KQoAvBPFZyMlk02bLYVvj5aPNHkb4uvP1o4iT25L_Qh5SPiNGx4F_eI_SqLddVFwwbnYy_2f87_5Yc_ID7zHGxHKrReFWGB5audEd6Lfs3DFOlSEWA8Kd4nER-RWDNM0moA0klptKYLBd5SdobS69bhp9iv2RSLTKeVcs_ZUGU-L5rCMK7oTh2df1wbYKc7wrFqVTVBUgImJxNol1P2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برزیل
🇧🇷
-
🇪🇬
مصر
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
بامداد یکشنبه ساعت ۰۱:۳۰
🏟
ورزشگاه کلیولند براونز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
برزیل در
۱۰
دیدار اخیر خود،
شش
برد و
یک
تساوی کسب کرده و در
سه
بازی شکست خورده است.
✅
مصر در
۱۰
دیدار اخیر خود،
پنج
برد و
چهار
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر برزیل
۳.۴
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر مصر
۱
.
۹
گل در هر بازی بوده
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب :
۱.۱۹
🧠
اگر مجبور به پنهان‌کاری شدید، مسیر اشتباه است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65331" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65330">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇺🇸
ترامپ:
ما خیلی سریع از ایران خارج خواهیم شد، و این خروج به هر شکلی که باشد، چه به صورت یک توافقنامه و چه به روش بسیار سخت، بسیار قوی خواهد بود. روش بسیار سخت شاید آسان‌تر باشد.
اما ما خارج خواهیم شد، و قیمت کودهای شما به شدت کاهش خواهد یافت، درست مانند چهار ماه پیش. قیمت کودهای شما کاهش یافته است.
انرژی، نفت و گاز شما همگی به شدت کاهش خواهند یافت. و صادقانه بگویم، فکر می‌کردم قیمت‌ها خیلی بالاتر برود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65330" target="_blank">📅 00:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65329">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:  ما یک سلاح هسته‌ای را از بین بردیم. این قرار بود کشوری توانمند باشد که حضور هسته‌ای داشته باشد. ما تا حد زیادی این کار را تمام کرده‌ایم. به هر طریقی، این کار تمام شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65329" target="_blank">📅 00:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65328">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdccc3a3f6.mp4?token=apzN_6CQvjE3Vm6gemZIZjrx_RcXWHl-ARg4-ubogeLezrCs8XFEIQrbF9Lx59ck5lHKO-ge2e43rSxnvVxbiGvFyihBRXnxZXmA1rg-b6o_mRak54MsV0jLh6N64iIxmhpx5x0s1bJV3tmOwafFEKfJO8R0xoQEhoDZ5V83dxQKo-6fKWwCqyAfQHIc81IytBACDezAQTn27bLRlx9lZZEPmiURIIAQyPRn56yp8Kc74wSCq6HGk8qYhh6u03uMTlxxxm5AeWwsfLA38zlM1tTDJkQ0ML3tEc7zHW31JPxuS_B4S0Fsb1X-sV8E_6tRYVqHvh9LTJWpoXmgSYBIzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdccc3a3f6.mp4?token=apzN_6CQvjE3Vm6gemZIZjrx_RcXWHl-ARg4-ubogeLezrCs8XFEIQrbF9Lx59ck5lHKO-ge2e43rSxnvVxbiGvFyihBRXnxZXmA1rg-b6o_mRak54MsV0jLh6N64iIxmhpx5x0s1bJV3tmOwafFEKfJO8R0xoQEhoDZ5V83dxQKo-6fKWwCqyAfQHIc81IytBACDezAQTn27bLRlx9lZZEPmiURIIAQyPRn56yp8Kc74wSCq6HGk8qYhh6u03uMTlxxxm5AeWwsfLA38zlM1tTDJkQ0ML3tEc7zHW31JPxuS_B4S0Fsb1X-sV8E_6tRYVqHvh9LTJWpoXmgSYBIzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:
ما یک سلاح هسته‌ای را از بین بردیم. این قرار بود کشوری توانمند باشد که حضور هسته‌ای داشته باشد.
ما تا حد زیادی این کار را تمام کرده‌ایم. به هر طریقی، این کار تمام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65328" target="_blank">📅 00:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65327">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecba9ea726.mp4?token=GoKK5zir4f8_h3jJxax6gHALFaQSUmcnJcgGyRFn7AEgeEzJ3sT3UINdsfSBhkmLFp7R8jKl3Dm_lG_dv_UMecEcQBVa6K9RC-_pPXgNAi-0_9JgSr6YLQIInVcBZo65TLkMxpqxHbsjEUFwjy7IlpRigrDmasDN6aSLC2H6eJIT_-IyiyrX2UmUG0jmdkOEPKFtj26G_OaEwTEoXAmB03MoFYDSGZ9m5OBe7A7uCeiuC9wM3XghcEY7aUjdgaMXwp_dsby5iC3hetAHKiZPViUHFblq_z-VGHdBOreAbx9MizEPjNTcea3LATvtpZSr-Lhdh6fU8m5r91W6rGcE6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecba9ea726.mp4?token=GoKK5zir4f8_h3jJxax6gHALFaQSUmcnJcgGyRFn7AEgeEzJ3sT3UINdsfSBhkmLFp7R8jKl3Dm_lG_dv_UMecEcQBVa6K9RC-_pPXgNAi-0_9JgSr6YLQIInVcBZo65TLkMxpqxHbsjEUFwjy7IlpRigrDmasDN6aSLC2H6eJIT_-IyiyrX2UmUG0jmdkOEPKFtj26G_OaEwTEoXAmB03MoFYDSGZ9m5OBe7A7uCeiuC9wM3XghcEY7aUjdgaMXwp_dsby5iC3hetAHKiZPViUHFblq_z-VGHdBOreAbx9MizEPjNTcea3LATvtpZSr-Lhdh6fU8m5r91W6rGcE6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
مقدار زیادی نفت وارد کشور ما می‌شود و مقدار زیادی نفت وارد جهان می‌شود که مردم حتی از آن خبر ندارند. و به همین دلیل است که قیمت هر بشکه نفت ۹۷ دلار است نه ۳۰۰ دلار.
وقتی کل این موضوع (ایران) حل شود، نباید زمان زیادی ببرد — به هر حال، این کار انجام خواهد شد.
وقتی همه چیز حل شود، قیمت نفت ممکن است حتی از قبل هم پایین‌تر بیاید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65327" target="_blank">📅 22:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65326">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">«منبع ایرانی: ادعای العربیه مبنی بر موافقت تهران با انتقال ذخایر اورانیوم به کشوری ثالث کذب است
یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایران روز جمعه گزارش یک رسانه سعودی مبنی بر موافقت تهران با انتقال بخشی از ذخایر اورانیوم غنی‌شده خود به کشوری ثالث را رد کرد و آن را نادرست خواند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65326" target="_blank">📅 22:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65323">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Izupdr4F8yflZZkrPgUvu4yCLKRKANQ9XV3t2yCo3gCfrb83pog6mwcHjKciwHGsVvfkWX7o1jAnIWqcIuqsQn-RRlVO1DbOYv3XPX9kcs9AC74LX4i2CT1iZhm_FhIc-77_q_7c1SAmVEsN-_DMTIUcMajmLZkOQ4cG9veHvYCQ-DZYrvmD-yM85DRMJDnc85GhFbEiSK5OlzqZLIDq6Gomz21-Y8-PL4SBtpj32ZUr_quFsfyWaMKCdp_ndquFP2GIRccDA1ZcEZJkgzvbMX9n7RvPW_ER_Bx4dLNOubwFs5bmSn0bazECC1yw8wCQfZUarqFu56MbGE1OfvJWQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
صحبت‌های جوزف عون، رئیس جمهور لبنان بر علیه نعیم قاسم، حزب‌الله، ایران، اسرائیل و امریکا:
به نعیم قاسم(دبیرکل حزب‌الله) می‌گویم مردم لبنان، مردم شما نیستند. شما نماینده مردم لبنان نیستید. مردم لبنان از جنگ بین اسرائیل و حزب الله به ستوه آمده‌اند. دشمنی بین اسرائیل و لبنان باید یک بار برای همیشه پایان یابد!
ایران لبنان را به عنوان اهرم چانه‌زنی در مذاکرات خود با ایالات متحده استفاده می‌کند. این غیرقابل قبول است.
حزب‌ الله باید بفهمد که راه دیگری جز نشستن و گفتگو وجود ندارد. هیچ راه دیگری برای حل این مشکل و نجات آنچه باقی مانده نیست، جز از طریق مذاکره و دیپلماسی.
خطاب به اسرائیل، از جنگ از سال ۱۹۴۸ خسته نشده‌اید؟ واقعاً می‌ خواهید در صلح زندگی کنید؟ بیایید بنشینیم و صحبت کنیم
ما آماده‌ایم. ما مایل هستیم. ما متعهدیم. آیا شما هستید؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65323" target="_blank">📅 21:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65322">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvuTHHLsro0U8qZ0CD62NNnxE3JqgTNvx87D6pmuBPKXj4lLZBxj9xitKFtDQHgeAGJ2FxU4n41Jt9J77pUY9Gb8hA7CsKKyS7QYKx0k6mho5bgKhY9u-QaZONwUIEibJhcAEcyZS9Ij2bProcTP_szcpX8fIluztTwXMxcSkUvgCbZwU9mQNiE5Q33R7v29X6QPmAzLY7Slu5vi-L8eMb_Zci5llmpNhGmuUfNNOoojjY1TlIUZxgBl5zyN1I2Kd-vllyWq9Z-x-2XnwFw7up7T6YUgo9vUbYIo_-T3IX4RVVHJpXhI73HRQgzBgVfje5Ndsb_17-hKZo2L8QOt4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پلی مارکت: صادرات نفت ایران به کمترین حد خودش در ۶ سال اخیر رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65322" target="_blank">📅 20:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65321">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=TyMeINhcXqUmBX17O-DIquSr7IDuBdPLlFfRYggp-h8kzbNHrR7whUS09FLh1Y-GPQcxk4BgmutouyHA9JaF-kXj5HeirnIIgTAAu2fHAR4pzh-A7Md8a7JrAW28FuQi_BIDUPuso0Gv3pc9182rpbYrffSpngqfWxLfk8zWwwv3A5qFgU6PXk9QpgFtK4CAS1RbJhMwIzzTbNlMWlg5StgOHVEf8PtDYZXWz2goNYdFlQbOvPvoDPv03a9AP4ZGxkXyVBzI_RTh7GF7tqCMkSB8i8MgFB78xILdKjzTTDXgBNHh2YNMXiqSMu5PmZ1g0_JSZWeclo8OzdhfFDFsuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=TyMeINhcXqUmBX17O-DIquSr7IDuBdPLlFfRYggp-h8kzbNHrR7whUS09FLh1Y-GPQcxk4BgmutouyHA9JaF-kXj5HeirnIIgTAAu2fHAR4pzh-A7Md8a7JrAW28FuQi_BIDUPuso0Gv3pc9182rpbYrffSpngqfWxLfk8zWwwv3A5qFgU6PXk9QpgFtK4CAS1RbJhMwIzzTbNlMWlg5StgOHVEf8PtDYZXWz2goNYdFlQbOvPvoDPv03a9AP4ZGxkXyVBzI_RTh7GF7tqCMkSB8i8MgFB78xILdKjzTTDXgBNHh2YNMXiqSMu5PmZ1g0_JSZWeclo8OzdhfFDFsuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ثابتی: قالیباف تو مذاکرات اختیارات تام نداره و پیشنهاد پزشکیان بوده. تو مذاکرات اسلام‌آباد اشتباهاتی خلاف خط قرمز رهبری شکل گرفته که باعث شده هیئت تذکر بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65321" target="_blank">📅 20:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65319">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=NnEb_RZe5obYoEbCtcabVqzDCSGR3PUwCWUJO-P9WWXZpT43teR8IEINR_6B0I0p86Sbpkq8hZKtD3aB5G477rK6F2ayiLix-9cbKrCWks1d-bbC1j_cqi-quFz_Fxcmq8IJ4qWEHmqZxSh2WOLqaFav7uAtAWWOUErjs60xxZ20PlX5Yp-qInZ70ci4yfmOIX3ndJtCPgjUo1JZbnDRieZt-8NDf0KqWpLRhJrSPtIjWwlQibn_GDvGqhg5W2BMpHyXfD47XV88DyrEqwVDQPpUFLM1SMhCovsaNY0xBjnNw5gxwALDo9Hnm0pezXl6B0DsKftGmBDJjTjyRqBecA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=NnEb_RZe5obYoEbCtcabVqzDCSGR3PUwCWUJO-P9WWXZpT43teR8IEINR_6B0I0p86Sbpkq8hZKtD3aB5G477rK6F2ayiLix-9cbKrCWks1d-bbC1j_cqi-quFz_Fxcmq8IJ4qWEHmqZxSh2WOLqaFav7uAtAWWOUErjs60xxZ20PlX5Yp-qInZ70ci4yfmOIX3ndJtCPgjUo1JZbnDRieZt-8NDf0KqWpLRhJrSPtIjWwlQibn_GDvGqhg5W2BMpHyXfD47XV88DyrEqwVDQPpUFLM1SMhCovsaNY0xBjnNw5gxwALDo9Hnm0pezXl6B0DsKftGmBDJjTjyRqBecA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شهروند کفن‌پوش اصفهانی خطاب به مسئولان: من رو با همین لباس ببرین توی دولت قول میدم همه مشکلات رو حل میکنم؛ تورم، گرونی، همه رو حل می‌کنم
از پزشکیان هم میخوام حمایتم کنه مگه خودش نگفت هر کی میتونه مشکلاتو حل کنه بیاد؟ تو رو خدا اجازه بدین من بیام.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65319" target="_blank">📅 17:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65315">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/msd3NXBf2dST-XaWbxWvWic_6bUHeaOL5xvM5I4dSWBfNIxOuXnDuK3zvrBs5TZwC-0auma4H9XAiziJaq9Vjkq4YmZZ-9Qy3mvSuemPbSaQZLgMK6V44mY5XlGy01alBgRAbkw5zZ2hlo2EBhHPM4WeJTgveVfuMFRbHSY2NBr0dgEtNZd-UeNDPI2C7HdZpcm-oPnm2bZjxM0ECk20TYaAlrw3Ld08JWKMj5gP0SgolJkXNO5ft4U_UbXVIRMpV1P47ROqsGksMNQV6lkvXc3KTldjppHAGCTmG9WkSGslAcrEkZfRGxiSZf__6Fa7N04cTPQrGh3nUTjIuVGamA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/leJlcr8J2Wbp_2A3b0Dv6rv8FKe4w0HKj3X4VcFtJaOi0IPGWnFAQjFxmCDyDvsAcYj4T3APZ9jkHplTE8PL1i5Fo_NubdNxh2bjT2CZlBEUwhqcxyDyoz9JTDZUh3mqPhF9dyuqFMb5fciJwuke2YVsLiZ2u6JbnoHS1g8yvHXdKLaGWIc5DlTLH1LXC3GMB61udD18cMM2kL8LJLeckG_jaCGSasGAR2APqZ0af6qBs0xaH3Abwd8DinVjBOCLCm6j8_ap7JGabqKDxG453zeZC97sI3tDN5Ivaz_TlK6qkwYl8IdR8A4ubllTLkYfFB-PdqIFx5ByxY12_hDiUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eG_yVcOf6YLEl-BXRzUhpzixVKALZDELTmkYSGvjAARoFBt_93-ngKZmLDms6MYPtCec2J5LizBD0oWgtT9fP41XLfMLyrviw1DNIpA3QqLXhF7nrjxmuKn07gDK1QT15tW6KEFDoQLor8C5j6Q3k9PlhDinc9N4tEk8y54nA_IEK7DcoGAiOzIHfWWbnE5zmdB8px-N_Kc2_MabhfZJ2szabTSeRp7KAbkxWLt-dw1tqIUu2UDtdB6nze2OgfCgQzjKUAqhPeciVRs2KwzECOE9m5voKcppa5_tls7bE1Xlp9zIsSPJUi7jAKj_Yw1xXT5A5pdTXCwAHIdt8A3VAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
فرماندهی-اقیانوس آرام ایالات متحده (INDOPACOM) اعلام کرد که یک کشتی بی‌تابعیت تحریم‌شده متعلق به ناوگان سایه ایران را توقیف کرده است
در طول شب، نیروهای ایالات متحده عملیات بازدارندگی دریایی و حق بازدید و سوار شدن به کشتی تحریم‌شده بی‌تابعیت MT DAVINA را در اقیانوس هند در منطقه مسئولیت INDOPACOM انجام دادند.
ما ادامه اجرای جهانی دریایی برای مختل کردن شبکه‌های غیرقانونی و بازداشت کشتی‌هایی که حمایت مادی به ایران ارائه می‌دهند، هر کجا که عملیات کنند، را ادامه خواهیم داد.
آب‌های بین‌المللی نمی‌توانند به عنوان سپری برای بازیگران تحریم‌شده استفاده شوند. وزارت جنگ ادامه خواهد داد تا عملیات غیرقانونی و کشتی‌های آن‌ها را در حوزه دریایی از آزادی مانور محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65315" target="_blank">📅 16:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65314">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHEB5pYrg4pP0F9aAVqtz-G_73PueWVFr2zeILQQzDCtG5ja3eYmRjPK8GxfOMZ-b92hObFcltHkNCgLR9JGylqIxL7dfJiJsmbfvdQVdbGzza0_sjjAGiBE05P_8JSidar99lFBzVLUuaLI4xrQRJ8xZtHx6fGbiUF67MrpIggt71_mz9_G4jYwQOyhQwh7JksnENrxrPPdVqCvIjBBsrclNY5EaX1FVoXRQtYWWbmq9BDQSGiHJn2a4wBSC4NPNqnEuRMC0eypBduHUHIJ11Mz_nUKtazRvEqnKe-qHsuzMDgIVxJbgH_XIwpTSaLtYnyImv4GToPEaXvigiFMAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
خبرگزاری العربیه : ایران رسما به پاکستان اعلام کرده که با انتقال بخشی از ذخایر اورانیوم غنی شده به یک کشور ثالث که مورد توافق هر دو طرف (ایران و آمریکا) باشد موافقت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65314" target="_blank">📅 15:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65313">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=qL6TND9Y6aBqMMLAYubfRmuvg0OTX-ecP34lS7rdQGfTM69ZxigInOUDdZfbXYFyWt-HIGhM6NOHjwEv09P5228rC4GEbp0wVWrxohQZNY6QQBOD8EJxKbKRYcUeBZ5RRvzM1J6x1GNNFgUbFCmkWYJPqG0YSjk1qipEWR6w7SYNt6xEgKkOoBh5uJ5LHPyFZJIvZrFq1QYE74Ch6hYtYDQE1AFuOD3V_5H7I2xKVBS7tK_JdO39iGFiHfGbwidX_5pf-ayy56t7OBzWVJCLVn973b5q-_apY1j12RTNbZFy2k6VIj8vYCFhsskpnVjUHLkarQzLmJjvzIWSEA9gqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=qL6TND9Y6aBqMMLAYubfRmuvg0OTX-ecP34lS7rdQGfTM69ZxigInOUDdZfbXYFyWt-HIGhM6NOHjwEv09P5228rC4GEbp0wVWrxohQZNY6QQBOD8EJxKbKRYcUeBZ5RRvzM1J6x1GNNFgUbFCmkWYJPqG0YSjk1qipEWR6w7SYNt6xEgKkOoBh5uJ5LHPyFZJIvZrFq1QYE74Ch6hYtYDQE1AFuOD3V_5H7I2xKVBS7tK_JdO39iGFiHfGbwidX_5pf-ayy56t7OBzWVJCLVn973b5q-_apY1j12RTNbZFy2k6VIj8vYCFhsskpnVjUHLkarQzLmJjvzIWSEA9gqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیصر خواننده لس‌انجلسی برای خوشحالی عرزشی‌ها پیک میبره بالا
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65313" target="_blank">📅 14:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65312">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFLKxtYrSRY1bXjdqK5MuMAtTWNQKz5W5ofLsYgVzA3ku7eqqWkY5ZOorMF70CriaM81T9JftMMFOxVQE8hdt558xS5RyrddeNWQH_fGhjGYQnq3JqEwNqTzlLz7kCp60KtAyJH1FW23NSR0m9hF9tihoqh68EiaOtNS6Qzw582_QDTwa-ipHHKH2qWXNaNMqrVFMFFE34wTtKAb_u1M-8WKeGJNNL6Lv1KObviDYQW2-mqIVeEzszW0e_CnBQ-MaDe9uV2_fashJ8yBevAyMT8WtM-JH4FCT06hp-Xhz_OjbvyhOAOD7TnsY2k2FVR3DHZna68lu4xcbh847Snrdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت‌کوین رسما به زیر ۶۲٬۰۰۰ دلار سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65312" target="_blank">📅 13:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65309">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=XQVmaPmp2T1rJN5VPVZxlrZ4zHum1nAjmue8SxNi6pwPXSzC6nvku7_OY8zDMNybAX5YnlF7caUy8fACu9s--K8yBU7VNEUggwVPpvQujcar6S75PdRuEsPfSaKKqv9sSSq2Ay4WanCmncfBIeY41Azy-LDOrZQbgaO6wyN81Z-xIszAqILOwKonJUeS53Jiz7cDJeyOAk_RFvLM7kd3d_IRY9tlIReJa5eVezEbvVEujP6mwZaE-viOifhnGVcntF_mRUYuY3eSAr_zDMDTG7yYTESuIh-x_iP08Y1Lrew3hyfuI9feXEZsHGJdUFMkJEJUQJFChM0kaKALg2uzZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=XQVmaPmp2T1rJN5VPVZxlrZ4zHum1nAjmue8SxNi6pwPXSzC6nvku7_OY8zDMNybAX5YnlF7caUy8fACu9s--K8yBU7VNEUggwVPpvQujcar6S75PdRuEsPfSaKKqv9sSSq2Ay4WanCmncfBIeY41Azy-LDOrZQbgaO6wyN81Z-xIszAqILOwKonJUeS53Jiz7cDJeyOAk_RFvLM7kd3d_IRY9tlIReJa5eVezEbvVEujP6mwZaE-viOifhnGVcntF_mRUYuY3eSAr_zDMDTG7yYTESuIh-x_iP08Y1Lrew3hyfuI9feXEZsHGJdUFMkJEJUQJFChM0kaKALg2uzZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مداحی محمدرضا هلالی مداح حکومتی با زبان چینی برای عید غدیر!!!
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65309" target="_blank">📅 13:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65308">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=b2uFV_cLqWodXwbcoz4l31LPdOZ5_3G4YpAQjbpZwFZjawtBy_a_-uXcli1_md1DiJhK9-nm4Bbu4YU6r1Nu06SlcAzdkWQTd5d99RXGQqzzT3zDORxHPj4Cboqz6BBcmDOjVG47xOPrkwDGJ88SV9JcC_xzVMYgsCC1JaFSfdFQ9qS6JnV_qertuS7wS3sp5yf7guzyDMsTPrRFdiMqb0zaZZz791d5-XqhjC_ml5UUQaGX3nHpRto2SCeBJPYaUEpzYGowmoxfsPHccggJB1ohL_PgJrYwj28Wtv_2ZSv5bljD47aRFtUVtGDTaLKDna6llN_y8WviOqgZBfeA9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=b2uFV_cLqWodXwbcoz4l31LPdOZ5_3G4YpAQjbpZwFZjawtBy_a_-uXcli1_md1DiJhK9-nm4Bbu4YU6r1Nu06SlcAzdkWQTd5d99RXGQqzzT3zDORxHPj4Cboqz6BBcmDOjVG47xOPrkwDGJ88SV9JcC_xzVMYgsCC1JaFSfdFQ9qS6JnV_qertuS7wS3sp5yf7guzyDMsTPrRFdiMqb0zaZZz791d5-XqhjC_ml5UUQaGX3nHpRto2SCeBJPYaUEpzYGowmoxfsPHccggJB1ohL_PgJrYwj28Wtv_2ZSv5bljD47aRFtUVtGDTaLKDna6llN_y8WviOqgZBfeA9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: عملیات خشم حماسی پدر، همسر و فرزند مجتبی خامنه‌ای را کشت.
🇺🇸
ترامپ: من فرد مورد علاقه او نیستم، اما احتمالاً او یک حرفه‌ای هست
در برخی زمینه‌ها آوازه خوبی داره، برخی‌ ازش بد میگن اما خب درباره من هم بد میگن!
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65308" target="_blank">📅 09:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65307">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پرسرعت وصله
👌
👌</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65307" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65306">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.2.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/news_hut/65306" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
بهترین فیلترشکن حال حاضر ایران
👉
💎
با همه نت ها پرسرعت کار میکنه بدون محدودیت
💎
👌
پیشنهاد ما دانلود این فیلترشکنه
🔧
لینک دانلود داخلی با نت ملی با سرعت بالا
👇
https://uploadb.com/plx39j7b72sy/Barko__v2.2.apk.html</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65306" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65305">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=KybJ46J2_hRxO5dtNxJYspctIXuXMvn--1GPYeuUDito2jsGOp9qA2AOXY0nNy1rHOBJNRjvrAnpY3rMs3KuCO89hJuXl866JRCBsill4hmUheJtOwGnUBcQD8xBVRB-o7hCwMUqp_HVQmpWfvmlq6cHredGIMbxpCCeoEzbhpGUYAn11GC5WVahNI752jpqOAfcITDXJtodiRF3vtBIvTfrnKygSgu1FMRb0UroK0DtwH3o6Qff9RghB4laRrSXdOLSoHak0jEzn_2BnT3oHektClk_FFZFYjSEHVu_qVnTyBleEW1M2O8VK3lWsDyzwMIUmB4cbOwVSQ5bNWxR3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=KybJ46J2_hRxO5dtNxJYspctIXuXMvn--1GPYeuUDito2jsGOp9qA2AOXY0nNy1rHOBJNRjvrAnpY3rMs3KuCO89hJuXl866JRCBsill4hmUheJtOwGnUBcQD8xBVRB-o7hCwMUqp_HVQmpWfvmlq6cHredGIMbxpCCeoEzbhpGUYAn11GC5WVahNI752jpqOAfcITDXJtodiRF3vtBIvTfrnKygSgu1FMRb0UroK0DtwH3o6Qff9RghB4laRrSXdOLSoHak0jEzn_2BnT3oHektClk_FFZFYjSEHVu_qVnTyBleEW1M2O8VK3lWsDyzwMIUmB4cbOwVSQ5bNWxR3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم. من محترمانه رفتار می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65305" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65304">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=FYEGfUXmd3cNhsKSKHnKiADilwlTT3NdO8h_cP-s0dlhx4d0ITRn_-G5o5T-KkVtzNh5d7DDBuG7Uc-EKF4zl4ouZ3op1RjbEWcyk6HEtNsCX2jOSLrmP1hkzdz0RPzRFU72Ow_7R79we7wLsqyo-JGeMxTNvwONQxWmlwYlqxtqKuXbFSvfy0ZpDBsBjvDGF7K0aNB5iIr2VFtILWK2V43mLoKxN5GfSRD3IPuSajD2lQr2XuSLKxI8yJ61P8wqgUyCRa3vFNp2V_SSaFPERZWKXqGfhaN8zvJtAXlJ_Y9UwNzI4_bbqVNHA_Kbo73RSgpTVJt8CmpMQpurLkjZdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=FYEGfUXmd3cNhsKSKHnKiADilwlTT3NdO8h_cP-s0dlhx4d0ITRn_-G5o5T-KkVtzNh5d7DDBuG7Uc-EKF4zl4ouZ3op1RjbEWcyk6HEtNsCX2jOSLrmP1hkzdz0RPzRFU72Ow_7R79we7wLsqyo-JGeMxTNvwONQxWmlwYlqxtqKuXbFSvfy0ZpDBsBjvDGF7K0aNB5iIr2VFtILWK2V43mLoKxN5GfSRD3IPuSajD2lQr2XuSLKxI8yJ61P8wqgUyCRa3vFNp2V_SSaFPERZWKXqGfhaN8zvJtAXlJ_Y9UwNzI4_bbqVNHA_Kbo73RSgpTVJt8CmpMQpurLkjZdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران: تمام ۱۵۹ کشتی آن‌ها در کف اقیانوس قرار دارند. ما در واقع از آن‌ها در آنجا عکس گرفتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65304" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65303">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=Fq48_lR1gUllWsZYz4xJWl-L56BFGYWGtYTUuhpQ8QGGruJHwIcBdRizB5qxtkgbGZpWF3OfbFbP4MZdvQFsejawkjiekardjviqd5Jnl4n9h_G6FHO5ENiyzOzld_3UYWCHO6gWw5BpdihqnFL2vbU2Od7iqLIWEZafkSrtZsZGLsJAwqT4kOm-we7VYZhsQ2hGPR7QavIdJlSHv4HbKs8EcgxWfYnp5OzTwDL-iyhHXCNZeLF3_YAfVRDPCmZmPDsWCmZIX3iWA5ScDCugUxDW7DymKCaFv-DB99t-hsoK85KJVZTxaUL2hVXX5XE0BDm5pAvGvvnuseiW2kmEcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=Fq48_lR1gUllWsZYz4xJWl-L56BFGYWGtYTUuhpQ8QGGruJHwIcBdRizB5qxtkgbGZpWF3OfbFbP4MZdvQFsejawkjiekardjviqd5Jnl4n9h_G6FHO5ENiyzOzld_3UYWCHO6gWw5BpdihqnFL2vbU2Od7iqLIWEZafkSrtZsZGLsJAwqT4kOm-we7VYZhsQ2hGPR7QavIdJlSHv4HbKs8EcgxWfYnp5OzTwDL-iyhHXCNZeLF3_YAfVRDPCmZmPDsWCmZIX3iWA5ScDCugUxDW7DymKCaFv-DB99t-hsoK85KJVZTxaUL2hVXX5XE0BDm5pAvGvvnuseiW2kmEcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: حزب‌الله هیچ چیزی را رد نکرد. آنها با ما تماس گرفتند و گفتند، «چطور است که متوقف شویم؟»
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65303" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65302">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=d1f8kVJyBtviPoM17mFi7FQtae2koHetQI89UQ0u0RGFo_ac0DrFAMyTQkdH9FDYi_upIqepL-1N3MrN0fQa5IzNChF8TH8JRD60P75P--ywgtMNz9m3ZPXPRIdZFLCdogY_AZRVc_P3gQvU_zY7KpGfukynM9kuvO4B9xWYy4x0H9mp9mNLFijH2X4mDpvImtP1LMiJP_V2JmDl9xUtJk-gsI_Mbz7RQ3ujfqFpjGSlifywRzb4YBAsxAVgGxaQrHHcOzfpRtyCOFxLRbZJWSIdJ5EhQwDLmIZrDYFaG_7UXz-X_7lgxUb-zNb4TfEGimXFmLN9763TK3O7juFbRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=d1f8kVJyBtviPoM17mFi7FQtae2koHetQI89UQ0u0RGFo_ac0DrFAMyTQkdH9FDYi_upIqepL-1N3MrN0fQa5IzNChF8TH8JRD60P75P--ywgtMNz9m3ZPXPRIdZFLCdogY_AZRVc_P3gQvU_zY7KpGfukynM9kuvO4B9xWYy4x0H9mp9mNLFijH2X4mDpvImtP1LMiJP_V2JmDl9xUtJk-gsI_Mbz7RQ3ujfqFpjGSlifywRzb4YBAsxAVgGxaQrHHcOzfpRtyCOFxLRbZJWSIdJ5EhQwDLmIZrDYFaG_7UXz-X_7lgxUb-zNb4TfEGimXFmLN9763TK3O7juFbRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من تا الان به هشت جنگ پایان دادم و به‌زودی یه جنگ نهم هم تموم میشه
شاید حتی بشه دهمین جنگ. فکر نمی‌کنم هیچ رئیس‌جمهوری تا حالا حتی یه جنگ رو هم تموم کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65302" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65301">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVlyAMerCGP3-pov1Bx-uomc4A2bvRDaXK47ca89FbTrkNXvNoe9BqV9dEX3St57BoqoEoBx9FCqn2fcY9ovD7N2vjr02le6tkDDdsvOnaBNZfYtQpeYcND7N5RGArtrDSmzsVF2Z9Iw1nGLZVLAuUEwjlAUFJIvxC-0_X_MJ6QKQ4iMA2qkCf_y5CI_Cy0N0IB16I1BJmwg5dlRd_kejFcBC6K6D5a8TwRB6tdYYSGNEooGwbPDH1ZGWlO_zpUDef21Qc_dxtQBpoIRZUEzjR5DUB-QQBp7LiJwbrLIh9WDiGkjGa_ee4SUSzGR8GVmp590y3Hrvml_aXZ4SomVnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورم نقطه به نقطه سالانه برخی اقلام اعلامی مرکز آمار: از ۴۳٠ درصد تا ۱٠٠ درصد
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65301" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65300">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgAsKnNn1hrCMQXx_ZSIn86m3T-RBKwMvUVg8RgQ5kSBYko339mfbW_PKkF0sgR9ge9jKr_DYV9SDsVCgnWYw9CBUsU8VEfwt3Tq809kPMdk4jxiMK6Oxd-ct87VJkRgtWiXxjSK2ZsGe6u_6r9oPZ9lGEifKOc1yKdMTBv_A_pjvLCbmBfCUm8G7iLa4feUMT79W15FO6IBqqaeb4umkJ5nmRmDjSmGQa7IIPi8bmWVFAu11okey1PubyzXb1HAENLmUlqBVzELS-1LyOTacDzNLDwiGfD0Kk9cuMzBrbt_RVLVLgYyAvxqNhJLz2IEQCwRDgng_EVaWm8fyRGPpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇨🇱
شیلی
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
شنبه ساعت ۲۱:۱۵
🏟
ورزشگاه ملی لیسبون
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در ۱۰ دیدار اخیر خود، شش برد و سه تساوی کسب کرده و در یک بازی شکست خورده است.
✅
شیلی در ۱۰ دیدار اخیر خود، چهار برد و دو تساوی کسب کرده و در چهار بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پرتغال  ۳.۶ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر شیلی  ۲.۵ گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه: پرتغال - ضریب: ۱.۲۰
🧠
پیش‌بینی آگاهانه، تمرین شناخت خود است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65300" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65299">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8PT0Y4jv3tNVZYLVFwALlsIoPY-Vwtagf7YD8LkEK9W9-Es6I_sj28HBII8MJV0ibkV9GF8qFX78XjTdrVu_HJgbbrFeq0kBGU5iuUQGbjCATvghmY9wnto5ZHdHnUdf_0tZuxiikQDkoIYOeGd3ku52e0gJo4P5FF8VnTuiI5el-Co8BR96K5KtNG0ArL4U8Kfbs4u2n-hAjKg0MGyEO3E-IuZPtNIfLlJUCz2oTLS-JtePiKUQFgpqzEF14skIbUsQhRMyuR3iqCVQtUSlsqRvctc7MZ07hWncxymQLQO6HlpdX73QEpQQnyKCY5Kt0ELFm7RHUzIa4Tx7ZR0sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن های chatgpt، grok و deepseek رفع فیلتر شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65299" target="_blank">📅 22:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65298">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=Dd6s3VpBx-FIezL4OKOqUhmU1ozgIHRMWw6P5OTTSNTIkgOdNu3HwmCEm_uVfJjaRTH3QFYy9i3a2Hat-B-nEl78GRzycsGgcDb5gusX5BSosmsGvmhgLLL1jZ2AZYdZkFscD0aue0NhnMJjCgXa4MITAD3s3KYpdD4uB3S2SAZMeggu8JlvCxsc1RebzEa5nUKU9jMIRwZWiL7IgAoncBH9dSy1LImk34o5w1SILWAF4fzraBA35zhQfADbuCj-YuS_qhNihUYFbKroS7dezZRDPVYYkFRhTm-EWY6I9SfZFpoRv8QlasIs8kLcUtkoOUG5vYvolTcHqz_u280J5g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=Dd6s3VpBx-FIezL4OKOqUhmU1ozgIHRMWw6P5OTTSNTIkgOdNu3HwmCEm_uVfJjaRTH3QFYy9i3a2Hat-B-nEl78GRzycsGgcDb5gusX5BSosmsGvmhgLLL1jZ2AZYdZkFscD0aue0NhnMJjCgXa4MITAD3s3KYpdD4uB3S2SAZMeggu8JlvCxsc1RebzEa5nUKU9jMIRwZWiL7IgAoncBH9dSy1LImk34o5w1SILWAF4fzraBA35zhQfADbuCj-YuS_qhNihUYFbKroS7dezZRDPVYYkFRhTm-EWY6I9SfZFpoRv8QlasIs8kLcUtkoOUG5vYvolTcHqz_u280J5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روز اول جنگ مجری صداوسیما حواسش نبود میکروفونش بازه، میگه همه گذاشتن فرار کردن، هیچکس نمونده
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65298" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65297">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65297" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65296">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQh7zGJ5Ihf58tf1QqelHSQ1I2JtyrmzKBfB7nHg5z8h8ahRFEh2PA4-kQ11zXCi_NxK4g7Ew7JkuvOCt99-8axDBVqj8lJ61hUh65ksJVTsnpkBBV6ngGVSlJh43yBfu0vaRXGiH2XheKtlZySsR2y9rQ5VhHTf8k6fCxpepOswL8CcNlqkqgBsZXsvj4-3xbjZKTTTOv9VBdasIDbhQRY7dBbSwwlCNo5sAxDggHgU6ARh6Dm_KXzS8lZhirszZjVSbG92Y3ZuDsYXSg62PhXAr4tjpfSRlDWXueykZyzoNASBp7dLvIwOwTkCNeGXJEvokh0ta1NJocYBw5-NHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران ، انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
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
14
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65296" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65295">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ:
ایران موافقت کرده اورانیوم ها تو خاک خودش از بین بره
📌
با این حساب ترامپ از یکی دیگه از خواسته هاش که دریافت اورانیوم توسط آمریکا بوده هم کوتاه اومده
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65295" target="_blank">📅 18:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65294">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVy2uEv_00Bv5HixrN-aXkfZUqllAQS6ZJK4fOOvYP2BcrFcf06WLIKZQMWNCxAsdpqhCapouHwyHQ45qz46yE3SeqykZyPXiRUCcKITxnO5-yGkpS4JweEuFPLuZuVpik7zrKMMuGgkg0xv3NxQovMonzXqzNbzmcgjk0AiAF78kGGwS6boG1GuiLjNnsoWB04Otp9qnO6xP18bI9bdEpxoK5Y02QXx7D4XbliQtR_0LTrC1zwbl9J3nRW-6MX_ImtDvpbOOujhzQpGutr2tFiZ8kZvUj_Rv56s8kiwvcv1s3JNuGsd2humxCt3o5Qt6jiKRnJ9JJxNC9NFAZ1q8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: ترامپ به طور خصوصی به دستیاراش گفته که در صورت کشته شدن نیروهای آمریکایی توسط تهران، آتش‌بس با ایران رو تموم و جنگ رو شروع کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65294" target="_blank">📅 17:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65293">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTAHQB7pDDGjVKD00kFMDPhqZC7WxUO_aF8anezedQtaE-Ap_gibiPutASpe16UGWbgfMXyJL30IEWv8pHMuRRLtFjLCvDl9c_UoYnxBh0FYmcypHdgEDr31hQ_mPi-WQOnQwTo7A3H0du0kATkG2PH032m4vRuMYi6Qu3AwKf1tcrxKez81yW1o7LmW26tuTSuwoiWvbaKTfYkIAWkLoixeMsgn2Gs6QR7KTF3ASYjMReFxvxH3aiEWucK525k6ZlaiNUxDrXTQ3wPIBtVo8xmwgkF2yxYJhfw1oOJzvpQRxlbYLZVoy3SNcDbB02d4XpTQA5teqYPGWRL8Jr-8Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65293" target="_blank">📅 16:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65292">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=htQ8MRGzJpBcmVHBDr196R5WT6z6sNvnxvzXDJCMHNdc4uiKVjEcoAeMtnSFLs5UNXCKxSMZTkOBFGz4NbuvTG-m_3NykU1yMdfTICor4qJTDvpgBD6CHhGBdqjyOWetBu1RrtsBE-amhaxqsV3Fb_YHJKwfay1ml2-IKDRFpRqbKT-WWxyEy7MM34ldY1ukEI8P5igvysg-9NE4_1ECinllc647zVVzwYbq_Evw4StRRnRdEM6uiHiBPwv4__o8xSdjmIP3CqadOWWzWxCpGA98HDRGbvOv7Zog2VaI91dk-Yem6E3rn5YDsnHHm0lAy6r8xFFBgGT3KwQdj4d27g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=htQ8MRGzJpBcmVHBDr196R5WT6z6sNvnxvzXDJCMHNdc4uiKVjEcoAeMtnSFLs5UNXCKxSMZTkOBFGz4NbuvTG-m_3NykU1yMdfTICor4qJTDvpgBD6CHhGBdqjyOWetBu1RrtsBE-amhaxqsV3Fb_YHJKwfay1ml2-IKDRFpRqbKT-WWxyEy7MM34ldY1ukEI8P5igvysg-9NE4_1ECinllc647zVVzwYbq_Evw4StRRnRdEM6uiHiBPwv4__o8xSdjmIP3CqadOWWzWxCpGA98HDRGbvOv7Zog2VaI91dk-Yem6E3rn5YDsnHHm0lAy6r8xFFBgGT3KwQdj4d27g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با اینکه آتش‌بس تو اسرائیل و لبنان اعلام شده امروز جنگنده‌های اسرائیلی اهدافی تو تبنین و حاروف تو جنوب لبنان رو منهدم کردند
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65292" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65291">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=EEB9pS6LzmIPpoBWtTwFt26spb8P0Vm2E11L8D0hcSoOOhMx4YGd2Eeopu6LJaBHfjAvmPedOgdBaG71bK3ms1j3f8spGkqeDUm8QEzGpBH0AXH6PTDRycuBSRTq2rFwg4SNlhlNYbLVJs4HqBDEhYQSa5DmfvgP7o6bIgwnHTRleHu_yH7c6ExvNaANsiBKupR5SfdXHzfyvkdt3TG8_mI1QzZoEjfruRua10NCaTPN9DEZW1p5_QXW1PzpXU_CHg-YLuD2hL4gmYQMvuwRr3NbG1yczBhNPMz8i_ZyrgfbhlyzoLvXVZuSC_HjbAZ1w0EFkaT9_Guag1vw1lGJryPXPDkiG80fDMq5tSaKqTQKkmpazgBPGdvoNXxAYcxWREE6_aUnNPwdkbl6Z02UyoCioRWusdvyBKhRzy5GY1NNYSfZFyoXVsVbfdvVOD6b9YBopNdvMcdSvtGLbhuZ9O8vPPmHOkJPC_LVqDpPTmwvfUVaQjZlomGee2PSzkFLJ3Kfy0pogiTqmvOgs4qh9Uq8dXFNRCM-8qEiss-JGrem4-z3iHMxY6YUYq_EABelQoWlJTyUZaoHkA28JlBgm8UnWnsVZunLjp8m-eN-dWlyh_4g49dokWZxonJfLOjKe_MiJQxoyHjTX1-s8_0E6owMwGjJKqWLyXiJqAq7FEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=EEB9pS6LzmIPpoBWtTwFt26spb8P0Vm2E11L8D0hcSoOOhMx4YGd2Eeopu6LJaBHfjAvmPedOgdBaG71bK3ms1j3f8spGkqeDUm8QEzGpBH0AXH6PTDRycuBSRTq2rFwg4SNlhlNYbLVJs4HqBDEhYQSa5DmfvgP7o6bIgwnHTRleHu_yH7c6ExvNaANsiBKupR5SfdXHzfyvkdt3TG8_mI1QzZoEjfruRua10NCaTPN9DEZW1p5_QXW1PzpXU_CHg-YLuD2hL4gmYQMvuwRr3NbG1yczBhNPMz8i_ZyrgfbhlyzoLvXVZuSC_HjbAZ1w0EFkaT9_Guag1vw1lGJryPXPDkiG80fDMq5tSaKqTQKkmpazgBPGdvoNXxAYcxWREE6_aUnNPwdkbl6Z02UyoCioRWusdvyBKhRzy5GY1NNYSfZFyoXVsVbfdvVOD6b9YBopNdvMcdSvtGLbhuZ9O8vPPmHOkJPC_LVqDpPTmwvfUVaQjZlomGee2PSzkFLJ3Kfy0pogiTqmvOgs4qh9Uq8dXFNRCM-8qEiss-JGrem4-z3iHMxY6YUYq_EABelQoWlJTyUZaoHkA28JlBgm8UnWnsVZunLjp8m-eN-dWlyh_4g49dokWZxonJfLOjKe_MiJQxoyHjTX1-s8_0E6owMwGjJKqWLyXiJqAq7FEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
فیلم جدید و ویرال شده از حمله هوایی آمریکا به پل B1 در کرج
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65291" target="_blank">📅 15:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65290">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgUrSj3keoV1a323QQMS22kexe1fEkbYxQONKyc9ySanI169TlVjimy06KMQGj4Q7Zl9hVFd11TQi0d_M75wed1H5D0I4wvkXhIXunfW4XKHGfbcszexGAnh1RXho2732beZV6fgS3is4IfwZYYREDDbZ8UaG4_tZrnqXGThQ5hgev6dzS9f8Z43FcEAeJ4tH0NUBMkywTJCV5O3U-eW-_uyKsRtPKTb28jQZM04qJgn3bKnGJdK0ovzT4uwElzrhSALC16oeY8CEcf_n-N4x9NY-UwsR1KLY90I9TDkQ2_Ceu4kTPuNoXETwrX4lhCbfy-jxl6Mp3ON1ySaYC2yyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تو ۲۴ ساعت گذشته بیش از ۲۰۰ میلیارد دلار از ارزش بازار رمز‌ارزها ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65290" target="_blank">📅 14:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65289">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65289" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🔵
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65289" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65288">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65288" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65287">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f7496394.mp4?token=kA1Jgn82qWWh87v6kX1L4gqjd84KHxhwHPl3vonSwGHHCaJQrGKiWKRFBxye99dIjgJ8yQy_0odMZZdPXqAGOoWyToQTW2ugIGmwp3wPOORlqW019UGA9Rm8gF0zRbmtLAMOAMLT-dXPTZ_scE4D_2mSRWZJzl2qhImnLZDPB-ary5YWWfK6eQAbPFirePlWheFStNlFSfuopHE5ahzO4dDlJ3Ip2BaoDdhtmpSQFedGbkL-asCWgb9pW9ryPK2j3Az8KkkXgKiz0f5LEIQAmCnyu62WoTq7DK9r8hpNobKC92qmPIarzT6dEwLDYUvTfTVZ52_3-1bXGk7kv_klFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f7496394.mp4?token=kA1Jgn82qWWh87v6kX1L4gqjd84KHxhwHPl3vonSwGHHCaJQrGKiWKRFBxye99dIjgJ8yQy_0odMZZdPXqAGOoWyToQTW2ugIGmwp3wPOORlqW019UGA9Rm8gF0zRbmtLAMOAMLT-dXPTZ_scE4D_2mSRWZJzl2qhImnLZDPB-ary5YWWfK6eQAbPFirePlWheFStNlFSfuopHE5ahzO4dDlJ3Ip2BaoDdhtmpSQFedGbkL-asCWgb9pW9ryPK2j3Az8KkkXgKiz0f5LEIQAmCnyu62WoTq7DK9r8hpNobKC92qmPIarzT6dEwLDYUvTfTVZ52_3-1bXGk7kv_klFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئویی آخرالزمانی از بمباران پایگاه چهارم شکاری دزفول در یک فروردین که به تازگی وایرال شده!!
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65287" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65286">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8Fj3UoB4BXfzWiJrcA5b-oRIWwiGHy3GM_j1fHowPuykSdIdfjsxix3vUql9GI8Luj6wL09Muv3b4f8BaDGboNZu7UK8HV-qgJwrcp8U2QLZs5SdIRZeT3A2qNehtem-5-NOtCVWGlmRYZueeIp5_rGygbqCIsJgeIH3sMVaBy9Tuhmw-z11HfKMbdy0j0V9PrJ5JlWCn7-MXVnizG0CcTS246j2aUN0peDOGXVmkwCLuZq8ixG7VUg7ufEfoOPbJ3_-2ps8hKKg4OJffSdftvFQKdEGKKKorpTt3nB5ovLU46QCTyqMh3MJ8eb49ptxWEJoa624e7A3_yrHXppZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال دن کین، رئیس ستاد ارتش امریکا برای اولین بار به کاراکاس پایتخت ونزوئلا سفر کرد و نشون میده روابط دو کشور بعد از افتتاح سفارت داره بهتر و بهتر میشه
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65286" target="_blank">📅 10:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65285">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‼️
کویت تصویر لحظه اولیه حمله با پهپاد شاهد از طرف جمهوری اسلامی به فرودگاه این کشور رو منتشر کرد؛
وزارت بهداشت کویت هم اعلام کرد طی این حمله یه تبعه هندی کشته و ۶۳ نفر هم زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65285" target="_blank">📅 09:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65284">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=TQgpU_uxRQnfc6h-SpGIlmc8AYyk5q5x6vQU38NO6cFeSJ9xTYWeFi7oaTB-7rogn0lOgaQYAzu4x4C0vhwR1HaIR8gFjdUqobbf7MfD3vHEWQgpi_LZ-udjLpTDLHnjJcvcoVcGtWgZ1GTr-C4519I6n3fQsmXrsnYTEssrAR-l2V-vzeWjbDZgQgmvjEpxObQ68wj8APsEovmk8DYFRK5A8sCUJpdYRnfpMkbBB7VvlQzlCQUcTWymLeqFGSNBYKzukLCSzMN6GYFjSj4JXUvz6VoW-7Jb_CoLENBEvbzPfh1zr4EXBPmGTNAOLA-T8eLe-aqw36m1_JupmPZEQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=TQgpU_uxRQnfc6h-SpGIlmc8AYyk5q5x6vQU38NO6cFeSJ9xTYWeFi7oaTB-7rogn0lOgaQYAzu4x4C0vhwR1HaIR8gFjdUqobbf7MfD3vHEWQgpi_LZ-udjLpTDLHnjJcvcoVcGtWgZ1GTr-C4519I6n3fQsmXrsnYTEssrAR-l2V-vzeWjbDZgQgmvjEpxObQ68wj8APsEovmk8DYFRK5A8sCUJpdYRnfpMkbBB7VvlQzlCQUcTWymLeqFGSNBYKzukLCSzMN6GYFjSj4JXUvz6VoW-7Jb_CoLENBEvbzPfh1zr4EXBPmGTNAOLA-T8eLe-aqw36m1_JupmPZEQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مجلس نمایندگان ایالات متحده قطعنامه‌ اختیارات جنگی رئیس جمهور ترامپ رو با رای ۲۱۵ به ۲۰۸ تصویب کرد.
برای اولین بار مجلس نمایندگان تونست رای بیشتر رو بیاره حالا این قطعنامه نیاز به تصویب مجلس سنا رو داره و بعدش میره روی میز ترامپ برای وتو!
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65284" target="_blank">📅 08:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65281">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVertigo</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpzjPw3pIDrptx12HevxbGEAfUnR8SSuKjh8LH9HmyarP1pu5qLl9rr0WAwR4Foc7ZVBYzazwwuCoBkoIe76wp3Z1RAIF4w3z4bnfX_W3ICSc-4bHrHcnArwt7FEp97UgoOvKXD0T3gjOnlvIbgw5vhdG8pcWuKZLh2Rb7kNe5Rfp2J7iFfzYyzl6-h72EV9JByAZFIHJXZz4LPDbJc2ihtp7pMZPjVIJ3bMm-88BeHO_zjcLy_UuwIC12ms59p41nmMJNCxAqg18ld5GfHh4zK9rIIuJzbYSZCjH9DgxASQ3e-Ch8nFwE1mmDx7Tfj3uSae_hBmIrg9Y1JngRkD7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
Vertigo Vpn
⚡️
🔥
آفر ویژه محدود
🔥
♾️
نامحدود تک‌کاربره 739 هزار تومان
♾️
نامحدود دوکاربره  879 هزار تومان
💎
سایر پلن‌ها
🔹
10 گیگ
⬅️
120 تومان
🔹
30 گیگ
⬅️
299 تومان
🎁
طرح معرفی دوستان
هر 2 نفر که معرفی کنی، 10 گیگ هدیه می‌گیری!
✅
سرعت بالا
✅
اتصال پایدار
✅
مناسب گیم و استریم
✅
پشتیبانی سریع
📩
برای خرید و اکانت تست پیام بده
@VertigoSupport
➖
➖
➖
➖
➖
➖
🫆
@Vertigo_Vpn</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65281" target="_blank">📅 00:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65278">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426918b893.mp4?token=eoRks_2inkGG50VOGHKX5LCSPiOURtFRy9I9GlZUASwWa1pWamWGTb08TqIgXLBkt-lk5pynCqq6O0vaHE1gFAixQoYH2SkC-vZBmCtnsUZBcmIZJEfsbIq661pZP95sJrW0zYgQxdM1rvCWQMquHRbUYH9YWGLP_WTkj2iSnjMDYAqpSTjtRHpaw1gI0cKO-vTcUVEWsaiqegD5Lv71-OfoUKnQF39Mci0ptVq-YJu8DHAJ_dncUAx649dpGsnZPTH2b_LWZvjoslMANAgxL2HlmyDkK1BTgei6iXaD7IN0i3W5i-HocSpOhoFRKrc8OorlyOBs8Z8hZgKBd9Bm7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426918b893.mp4?token=eoRks_2inkGG50VOGHKX5LCSPiOURtFRy9I9GlZUASwWa1pWamWGTb08TqIgXLBkt-lk5pynCqq6O0vaHE1gFAixQoYH2SkC-vZBmCtnsUZBcmIZJEfsbIq661pZP95sJrW0zYgQxdM1rvCWQMquHRbUYH9YWGLP_WTkj2iSnjMDYAqpSTjtRHpaw1gI0cKO-vTcUVEWsaiqegD5Lv71-OfoUKnQF39Mci0ptVq-YJu8DHAJ_dncUAx649dpGsnZPTH2b_LWZvjoslMANAgxL2HlmyDkK1BTgei6iXaD7IN0i3W5i-HocSpOhoFRKrc8OorlyOBs8Z8hZgKBd9Bm7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درمورد نقض آتش‌بس: تو اون منطقه از دنیا، آتش‌بس یعنی وقتی دارن با یه شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنن
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65278" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65277">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=VEZE2xPo2RTvgQzghWFb81M0IMJ56dBaOhFWKiDrQMJJ5iDXns2sT-XMbFeEG_rV_EhTVwltDMG_IXWpD25RDPOdlP9kDIbVKRQPs6HWqdcxIZC1HBVsORuEgLWZjN3rS4jydApmufahkvxW0J1WoQIUG9RpXjGEukAGYBv-5xArE-2uS5C7s7wMtoT8Yfskpw2kYSaboRXu3Cf4MPFb3o7KBwTwVHqHtWW0s8ONFi22lzKTHda_iuvvTTunIrWUPn_0YIGgS2rv8ph4TOmHhruXbtdJmyJF7EN5BWkADMyu1wJf4noCnSyGnji_qrDYRoos5w9bd3x2Yv2LoPw9uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=VEZE2xPo2RTvgQzghWFb81M0IMJ56dBaOhFWKiDrQMJJ5iDXns2sT-XMbFeEG_rV_EhTVwltDMG_IXWpD25RDPOdlP9kDIbVKRQPs6HWqdcxIZC1HBVsORuEgLWZjN3rS4jydApmufahkvxW0J1WoQIUG9RpXjGEukAGYBv-5xArE-2uS5C7s7wMtoT8Yfskpw2kYSaboRXu3Cf4MPFb3o7KBwTwVHqHtWW0s8ONFi22lzKTHda_iuvvTTunIrWUPn_0YIGgS2rv8ph4TOmHhruXbtdJmyJF7EN5BWkADMyu1wJf4noCnSyGnji_qrDYRoos5w9bd3x2Yv2LoPw9uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی: مذاکره بسیار خوب پیش می‌رود... ممکن است اتفاق نیفتد، اما اگر بیفتد، احتمال می‌دهم در طول آخر هفته رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65277" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65276">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5jt5VsRey6wPy8VcgLfh-yRnh1CB_e_uuE0urn-ZmpGsmxkBJCOcNvCWJanDo7l8814ZXfD1xEUtJOTyKY-dApH8GQwAzGOOCM955UCYgXR4KgBnnt6emoDKpQbKRPNPDK39mSyNwS8L3LZL0-2-OAhzzzK9cRzkSfeK7gpI8E760LmBZiaPGslGLKquIzsLMKVIceapkJs5gwcCDbeCgr8zybWyAu_rgmObJJtY2U58d80BQYuxHDQFGHOrR3Gj7yJ5D1wNpnS5TX9x9hmBcKHuCqSFtFrBVJKHIewZHmyI5IRzFBb5keqE-8ACuiC_7mOSZkwLBJcQi3lrpHksQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام:
❌
ادعا: ایران امروز ادعا کرد که به ترمینال مسافران فرودگاه بین‌المللی کویت حمله نکرده و خسارات وارد شده در واقع توسط یک موشک رهگیر آمریکایی ایجاد شده است. کاملاً غلط.
✔️
حقیقت: ایران با پهپادها به فرودگاه غیرنظامی حمله کرد؛ این یک حمله عمدی، محاسبه‌شده و بی‌توجیه بود
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65276" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65274">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bac082417.mp4?token=YdPq99NeW4D-WzqbklXgJyalhCFKU5LE_lU3W62tIl5uHnqzh9ZpYoBCBFR3UIdZurOGQ-_Jv7e8VX-nb-DwPtpBOuD5Qw0xsuoH6UGn5zkuQfpzbSJei8uPWP53OFEtukk5YQO1BV0uQwkNvKaMD46uUoVo5KpXf-xHxyD_zW5qLrub6EnAMruVplSiC5S7KjSUQ8e11eAGC5LeI7MNg4VW4gzQ8WvgdI8X4cjA_GhMwzBbgRTg8VyKeycXAUY-ciq0iLeQRj6L4zblb5cH_YEbxnM_rN10is3JpZ1OS6YsTuceKShQv5xNwSaOjboTuuBCduYd04ruItIxODNp0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bac082417.mp4?token=YdPq99NeW4D-WzqbklXgJyalhCFKU5LE_lU3W62tIl5uHnqzh9ZpYoBCBFR3UIdZurOGQ-_Jv7e8VX-nb-DwPtpBOuD5Qw0xsuoH6UGn5zkuQfpzbSJei8uPWP53OFEtukk5YQO1BV0uQwkNvKaMD46uUoVo5KpXf-xHxyD_zW5qLrub6EnAMruVplSiC5S7KjSUQ8e11eAGC5LeI7MNg4VW4gzQ8WvgdI8X4cjA_GhMwzBbgRTg8VyKeycXAUY-ciq0iLeQRj6L4zblb5cH_YEbxnM_rN10is3JpZ1OS6YsTuceKShQv5xNwSaOjboTuuBCduYd04ruItIxODNp0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیده شدن ترامپ تو پارک زرقان شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65274" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65272">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KviWd_pHZz-U4NttcbckEf7uB1MzItfGNTmVX28xlMl_OY0pnuudQfDgpXQL31BB1XkM28k1kdlF1hvl6oHBRrR4zH96Bp7ElDcUqF4FmFCQqa7csoo4wdaOqlE2Q_2-g7PzUi59_d55ev9lGiH1FbUZSjCerDuSrrROuy-BFEymhiJUK8bgJKaqGFgMm_si-9ZcyEskOfWWyP9ESVT1d_aAbiTyi1eAbTM82BT4m_byPFp8ZMdwxrsXT_Ji49UYEpfjuhvyIHfenUeTGXnMdYCbTQMmNPXiqD33Neopyx3SZmnPOxCOoinsTU3eAgHcvUtW52hO6ylcP44VxxWpZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا مامان روبیکا گم شده دست کسیه بره تحویل بده شر نشه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65272" target="_blank">📅 22:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65271">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=ov0fr4qPvHmVcQVCyvVLD6c-mrUORJ6XNJvt8fUW_5aqsG9g2GyTTBCZYMzwWt_428PHG-SbGgidN-GcRcXGZ4-kWaMnAUALC10af2acIaBpUWbGuD1P21VALpJ1CAVcgv_FX5jUc-p0-u-5syZQK-TPLhcfH8tBUSIbXT8qheQhdbJf-aRnsn5yV-ZbzMfK5MvYvd3Lh7amkFvGBHXrZ-JkfMafPvKeuVdj5K44d5VcgfdaSXnLNtvMOoeevAQNiABlrJT0M-rlvpoT082oqe4pcSgEhzJvU2OAJ1VtPpzxn22hN5cakOsx-q4aL3QyRaLxZF4t5uulBKt7juO8hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=ov0fr4qPvHmVcQVCyvVLD6c-mrUORJ6XNJvt8fUW_5aqsG9g2GyTTBCZYMzwWt_428PHG-SbGgidN-GcRcXGZ4-kWaMnAUALC10af2acIaBpUWbGuD1P21VALpJ1CAVcgv_FX5jUc-p0-u-5syZQK-TPLhcfH8tBUSIbXT8qheQhdbJf-aRnsn5yV-ZbzMfK5MvYvd3Lh7amkFvGBHXrZ-JkfMafPvKeuVdj5K44d5VcgfdaSXnLNtvMOoeevAQNiABlrJT0M-rlvpoT082oqe4pcSgEhzJvU2OAJ1VtPpzxn22hN5cakOsx-q4aL3QyRaLxZF4t5uulBKt7juO8hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: شما درباره تغییر رژیم صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
🇮🇱
نتانیاهو: چرا این را می‌گویید؟
🎙
خبرنگار: به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
🇮🇱
نتانیاهو: این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند!
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65271" target="_blank">📅 21:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65268">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ: هنوز افتخار اینکه آیت‌الله خامنه‌ای را ببینم نداشتم، اما دوست دارم با او ملاقات کنم  @News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65268" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65267">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم!  @News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65267" target="_blank">📅 18:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65266">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کاکولدزاده تر و بی‌غیرت تر از اعراب حاشیه خلیج فارس تاریخ به خودش نمی‌بینه، به مادر این اعراب تجاوز کنی شبش بیانیه می‌ده محکومش می‌کنه
#hjAly‌
@News_Huy</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65266" target="_blank">📅 18:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65265">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=EnE4egtzTMz10PLM1dT6N_C6507ngC8cQcgcsZj0VAqhFE_UR6HVOSB_4M2QMVhr7wInEYRjyYUUJ0oqiE5eHEjZ_ITlX0p20qPeV3UPcpqiSmlIHNgwhFi9wd1LjYrKvwL__DyP46VJbPOUUgObZOQsMyRl3kzXbxWf6dacvERYNj2XiQK5i8PhPbelRTLyfZP9tYDfbv2Q8uPcQLQR1Ey6ZSB8g_KkI6VBUXFTS62VS8xN0N5M6jI31qO4ijk08IKwl4onNpoOClgH36apEBwMU1Ngu2ELWDnBBxsq47aIUwhV8odErPTDfnrN_ZYrsYPg7auWtu5oobBjVas3vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=EnE4egtzTMz10PLM1dT6N_C6507ngC8cQcgcsZj0VAqhFE_UR6HVOSB_4M2QMVhr7wInEYRjyYUUJ0oqiE5eHEjZ_ITlX0p20qPeV3UPcpqiSmlIHNgwhFi9wd1LjYrKvwL__DyP46VJbPOUUgObZOQsMyRl3kzXbxWf6dacvERYNj2XiQK5i8PhPbelRTLyfZP9tYDfbv2Q8uPcQLQR1Ey6ZSB8g_KkI6VBUXFTS62VS8xN0N5M6jI31qO4ijk08IKwl4onNpoOClgH36apEBwMU1Ngu2ELWDnBBxsq47aIUwhV8odErPTDfnrN_ZYrsYPg7auWtu5oobBjVas3vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم
!
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65265" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65264">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=Cxc86ZemNvZsOJdZQULUoK0-u_0bGIq_OKnIavEadSQl9Hi4mZ-oZqqZBZjdnD5Il8f5kpiw5RD3gq6oinDb-1RS7bnTf_ztrGP7lI5lsHNAOMZ2G_4r0uh-jbBxoojRr_bE287cB3wmtxferCKhjxtK967gKkOoAIQYMCLrDg9xWZisEPEj3xa9W8aASvVy_9qjmCN30hH-xBP-XqzhQ_ONalCgJA-HSo-CJ0OLZExIscb9_VFP3AzOIlXR7qPfWxSC8gsQSvs_2Nt87VdveM5pt8z0KbZNqZeGV-4JwdGGv83lErefZbr10SRVdzBlz0B-OYBIVjLG3UbI2ssCzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=Cxc86ZemNvZsOJdZQULUoK0-u_0bGIq_OKnIavEadSQl9Hi4mZ-oZqqZBZjdnD5Il8f5kpiw5RD3gq6oinDb-1RS7bnTf_ztrGP7lI5lsHNAOMZ2G_4r0uh-jbBxoojRr_bE287cB3wmtxferCKhjxtK967gKkOoAIQYMCLrDg9xWZisEPEj3xa9W8aASvVy_9qjmCN30hH-xBP-XqzhQ_ONalCgJA-HSo-CJ0OLZExIscb9_VFP3AzOIlXR7qPfWxSC8gsQSvs_2Nt87VdveM5pt8z0KbZNqZeGV-4JwdGGv83lErefZbr10SRVdzBlz0B-OYBIVjLG3UbI2ssCzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
منظورم این است که من کسی هستم که این را شروع کردم.
نمی‌خواهم کسی را خسته کنم، اما من این را شروع کردم زیرا نمی‌توانیم اجازه دهیم که آن‌ها سلاح اتمی داشته باشند.
اگر من نبودم، اسرائیل وجود نداشت
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65264" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65263">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=AMrqF2qkJOMOwspjF3Np4MlyObCNrMUMG0L_CFnwgplObRt7dvezLjJFjCu0Q4mn8-jzNE4-69zTLUfU6TzpMJcPxTZh8DM0CtpT4pbRlHft11Ndk5elxBhpcG3eY4jJfSq3Kr8UoERIZMCWdPz9AnKkdwuqMbKMXarRvfIsH4WedJg3W5o2WeZuLlHYUkMKiCaByY_uFpplbhsslwVR_khSh-JeAC3l4ZfJqMXEhWF-CfFTQDi_UdMMo4k8uXhujQLFJjhPHz90o6aYEBDatmK_B7Kr7wXU310NvJW37jf2dfd2JjXF9XQ9dc855luLVpztgULbFloGH4wpaSlIGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=AMrqF2qkJOMOwspjF3Np4MlyObCNrMUMG0L_CFnwgplObRt7dvezLjJFjCu0Q4mn8-jzNE4-69zTLUfU6TzpMJcPxTZh8DM0CtpT4pbRlHft11Ndk5elxBhpcG3eY4jJfSq3Kr8UoERIZMCWdPz9AnKkdwuqMbKMXarRvfIsH4WedJg3W5o2WeZuLlHYUkMKiCaByY_uFpplbhsslwVR_khSh-JeAC3l4ZfJqMXEhWF-CfFTQDi_UdMMo4k8uXhujQLFJjhPHz90o6aYEBDatmK_B7Kr7wXU310NvJW37jf2dfd2JjXF9XQ9dc855luLVpztgULbFloGH4wpaSlIGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، تحلیلگر صداوسیما: انتقام کشته شدگان رو بخاطر حفظ جان قالیباف نگرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65263" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65262">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65262" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65261">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65261" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65260">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
📰
#فوری؛ نیویورک پست: ترامپ پیش‌بینی میکنه که با رهبر معظم ایران، مجتبی خامنه‌ای که احتمالا همجنسگراست، دیدار خواهد کرد؛ «رابطه بسیار خوبی دارند»!!  رئیس‌جمهور ترامپ در مصاحبه‌ای با «پاد فورس وان» که چهارشنبه منتشر شد، گفت انتظار دارد با رهبر معظم ایران، مجتبی…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65260" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65259">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5ExqLGKDXsivfndU6hzldARopQ8rwLVKitXiJrhZ860dtR1Rx6drUJ0yN2NzAHGyBi5GKv-NDIQYAC9nryWWfBqcG9ppNzO4yuZM9391Q9YuwVypJwyF0NElMiKIBkUK8LaCL7mqi3PP4TBRnAdZbMiRcqGqBnrfz8Obkh3OXC4g7RI-IhnwwrKMG7OS11KuzZ_hxsKpa2xS77TR2M8vjO4mCSDDsYywbaPWkso-TXqw-RQD_bO6_kD_n90URvLsg8Nha4vpHTNo4BY3Xltc7fB_pKsRsaS5nnpDm1Dao6teAFKjXozZ7MAcYD6G6vk-8Y65cuS4SeDL5M-8n1uWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست قیمت جدید و نجومی خودروهای آشغال داخلی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65259" target="_blank">📅 12:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65258">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RevOyoyF5M4o0rSVbB_NNNMRBb1dAswN__zWYSscjIYmigk2Wpmb6-ohN-skQ_3BluMvr6kXdvKh1qWcqmaM3hp28_UBESLg5DEktpfnSCGS9T_lZf5Uqna5AAq1gSpjS5MDyMS0Zg9Pw2_AhkoGbubZh7xr9FAOSZUxQnWizaIWfMiz7cWeOtRPLvEwxb7m4kaFeQgQDmZWim06nFL5L35KoWfODU3poLp9VQD1cmRR7p8zCK2xBhQ1taiSahk9vPiV-4YM5Sdm1TuuvI7kjOV85wvWA8KPzj3lxTC7Pikvq-wycU1L4u8XvYz098RMBF11S8lt-8JwNFQTzta6SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکنا: آخوندای قم پیشنهاد دادن علی‌خامنه‌ای در قم دفن بشه
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65258" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65256">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OtsN7o-A-BkzmTvCpGmhQWFRqtEHXkyaIcktfLxA9TBuSnwVhWnZXr3ujke0PDwgUnZIXSIeB_4RAqfAoPpfnYPZvC5h59dHq41JJ8R_4Ffx-STFaYbWhSH5ZpEIzbB4FOxeV8ibADoh0zDbab8uahlUUDWUXfToJ66eXIh0ZCGNNncJe4d8xQoW0-aMFjbBhhdLZh4zpwhgURGDiuEGpHyrcgQrqQNZKOqfkke0xv6ehaTPEg59buhM_nZDFMAclHscUdtPL1x3JFIF8S7a9DWweNU_SkSqIP657IGU3j8vVTOq6egGc-7WZLYeXyey51p8gVftKuqyFxFWaEHsdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lKKDfF1DEe9vVKQDHDRXYHHQ5M4Ib3h6wg5Gj-GEqdqmxbsrd8j_RhAuVGNbPqn80SiP6iLH-09nIxijw26TDPIhAjFUH-_F41UCCQcGQKujS5JAkdvMiMr0oyv4G9KikX8ZWXC3j5MHnU9CU3WIMQM5Enj-RGoToC1R3tFJDmc-rR9cKxrcKWQUaU5G_-0d9MrosAi8YuNX4pnbBH54oBfJLh_ZtQWzDroPGd23AYxD19FELCacFYyj09bv1xIeKYWPvG_qNQCC_h09CdOajQAskGAH-Zb5Q_veaqg5qv5pfyMIBa2aSnZIk_WtUESaFHYUoKsp4ryCtEZeBEmnxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت فرودگاه کویت که گفته میشه مربوط به حملات دیشب سپاهه
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65256" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65255">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goZbP1YzDLue-961VJf949QqiWljxXy2an35KbJ3eV-tiIMp4bYmebMh-pEjngwQSWU_6qgfrgIh8hkCcZy-VlwhlociT89tl64ZzvLBjyTR8pe-UUPMCbwBTlBvn8yYW7BFqwOCVmB0Je5uJImeUsgoaL2JvWKuk7si0PckOGnd9kC1nylsUrBZxVxWFkHpSSFUlIB44Sxc4wQAec-LLWBjG3ot6P7Ew1_aFv5kOHKyFGCUaBXK7jKk1tfMONruzvc_QOn4kSqeddOseYpoTjwNnqAirhO7xL1aRtnMv4yTrVdbofjH3XExC_W5lYHxouBTWE9QAEMfc2sjp66cYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65255" target="_blank">📅 11:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65254">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">طبق گزارش سنتکام، ایران چندین موشک بالستیک به سمت همسایگان منطقه‌ای شلیک کرد. همه آنها به اهداف مورد نظر خود اصابت نکردند.
دو موشک شلیک شده به کویت در مسیر خود به هدف نرسیدند یا متلاشی شدند.
سه موشک که به سمت بحرین شلیک شده بودند توسط پدافند هوایی ایالات متحده و بحرین رهگیری شدند. هیچ پرسنل آمریکایی آسیب ندی
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65254" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65253">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">هواپیمایی کشوری کویت اعلام کرد که حمله جمهوری اسلامی خسارت شدیدی به تعدادی از تاسیسات فرودگاه شهر کویت وارد کرده و همچنین شماری مجروح بر جای گذاشته است.
هواپیمایی کشوری کویت اعلام کرد که ساختمان تی۱ فرودگاه شهر کویت بامداد چهارشنبه با پهپادها و موشک‌های ایرانی هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65253" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65252">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=CQLskK6wlq-qzBK0tfbbxnKebkq5Nzu_9g6l8BmkGvNCvsKlrbU0faDT1tuQLZiWOvW94eYrzLO4qP5C6mJv_kjwWwbZXKwNfK0Fjodl8onCdeouY5F2zbzXIm9ppyz5iBfhcmxqOzQbxLLCySUBe7hxV1x6osYp2Aso_oQeAgC4_ok5M7afCK2W4oxFWfbW5r3n4Sm8K2fpVQw4FlU6uOPmTuclWzajfjKQxaugYYuufMTv0ktZeDqhM6kXvlil-aRHHlykWBYkR9sbvsjKVVpBZzM10m-Bm9w2DalRf-5XSd-3cPHo-qAt-jwL9TZxpvBIdPANUCj6vmWTbBpxGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=CQLskK6wlq-qzBK0tfbbxnKebkq5Nzu_9g6l8BmkGvNCvsKlrbU0faDT1tuQLZiWOvW94eYrzLO4qP5C6mJv_kjwWwbZXKwNfK0Fjodl8onCdeouY5F2zbzXIm9ppyz5iBfhcmxqOzQbxLLCySUBe7hxV1x6osYp2Aso_oQeAgC4_ok5M7afCK2W4oxFWfbW5r3n4Sm8K2fpVQw4FlU6uOPmTuclWzajfjKQxaugYYuufMTv0ktZeDqhM6kXvlil-aRHHlykWBYkR9sbvsjKVVpBZzM10m-Bm9w2DalRf-5XSd-3cPHo-qAt-jwL9TZxpvBIdPANUCj6vmWTbBpxGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمی از پهپاد شاهد-۱۳۶ که دیشب به سمت آسمان کویت درحال حرکت بود
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65252" target="_blank">📅 10:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65251">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی بحرین،کویت،امارات به طور کامل به روی کلیه ترددهای هوایی بسته شده است
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65251" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65250">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت  @News_Hut</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/65250" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65249">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/65249" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65248">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✔️
اعتبارشو صد درصد تضمین میکنیم
ارزون‌تر، مطمئن‌تر و قوی‌تر از همه جا
🔥
ضمانت بازگشت وجه در صورت عدم رضایت
.
دیگه چی‌ میخوایید؟
😍</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/65248" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65246">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
آمریکا بزرگترین صرافیای ایران یعنی نوبیتکس،بیت‌پین، رمزینکس و والکس رو تحریم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/65246" target="_blank">📅 00:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65242">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/duc3oYrCJRAtm25kVqgFMWN0xd_q7VskuQkunkJKX1yiKqdn0dUrxzlmBA3owkElDc_rXYuklbqOiXOumz6Qvftk5M1cHJ8zH4spyJsLxQKqmWm4uVfF_EUau5xqo3M92aCwcBlAEyFhHgJAEutzpdOUi4SEApm-LnDX6wSkYNux7VBmwI0oVAJ8VVpeNI1fiPzLMaOV-tIeGFePJHWlAIZBrAUHH8X76w5gGOc04Eqd8QwuQeQlfgPOPyHumMkWhwr8yEY-5h7RgmjczhZryS0Y2xk9e8XdY3U6RIcl4SY5CopKivZC2NXaJrY-8zbQoQSyR5BmWTDvXEtYJcg8Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQbFcBybIGzTz1oJv80dnQ52GspeBaSNMIl09LVPYGq64N2f2ZLYIYJlyrLur58itit-2Xpe7-5457AqKY0cpIqIh4bdpi9IFmYVKJsLw1sY08qBcRLOeWXj4J1bR5_rddzqvztgIdV4d7SkcUoyloH_5AgmmeDb9n87gR2qBwWaBWAUzUWOpmV5ww3p83jKnFY1maTXpCxGkWoXYsmSujGNTfd6XCiSk-WoneUcqXHC1sbdNogPss1y6Q4VO8O1cgW063PZbPZeDIZ8API_TQxXc37X_lmyffnLsmZBHejsWYgpM9wX_oFlwVGNdRa_wY-ne2vjgIzYgPzHRBthMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه شرکت به‌نام دکترتور اومده تور آب‌بازی تو چیتگر تهران گذاشته که مردم از جمله دخترا و پسرا میان بهم آب میپاشن و هم‌دیگه رو خیس می‌کنن
ولی خب بعد چند ساعت از بالا دستور دادن همچیزو کنسل کنن
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65242" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65241">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dazRRr3ma-hy0Ma0pCHswbgdCgG8ZOv4PVGdrcCASV1BUdnnTLrKVpr_X51ZFUyQzYTRQjID3hY6nxDU3hkk6tBcKW45TTYda5o9fn6i0rJuzFzzuOCpEX20HgwBTrWplYNinDSA_WxR6fnED_onRrax4fY_hFWmUQ2lsTf9MdyM6K0OXk1DU62o7q-D5vWUeUVHA-FaYXz9N7FLXoyrfvXSiH7pEpsVKfiXLUsK55l71y_RLIvC9f8I6muY7tltAmrzGvQAUf5ktjR_QRmPi6R1EC3iEafbttPpomowSm-6E9R38dpyt_H7Ij6kxFnEtG_YeLNzivnMoy4Jhd4Jdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: ابراهیم لینکلن و نیروها همچنان به محاصره دریایی ایران ادامه میده و تاکنون ۱۲۲ کشتی رو از مسیرشون تغییر دادن
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65241" target="_blank">📅 22:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65240">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGenCpegM0O1g7mkWFsex4XSSDCI9h_Nxbqe7sFOv1qBQ7uiY_mX66O4JxxyqowA8qALudha1PWTufFXjXQIj87R0bFTxAubqhJwConcXlsEvyVRttZi1znTZdbyWH2giZtkQF_f6-OUIzWjh5EChcPy994Y1rAvLf8HTKCNLfY8ysfcB2PpNrEp9vr5Y-EMIlMTkaUjO0vLjslBbN7-Syc0xobTs8X0v8HuuZL_iqyLbPK5NagAoRlZXEQHVkKa4Jfx2Z7lpCC81s_ZALbZkX569Wu8h1vP63_89K2IvxAPCo_Jx4l1hAgeUmpW6qOlfuiCr5RZpdJrjjWsQ_Vt3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق آمار، سالانه 60 هزار ایرانی بر اثر مصرف دخانیات فوت میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65240" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65239">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/news_hut/65239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65239" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65238">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLTib2xz5H-x1VK8XqAFq0nHN1Io1yIxmOHQwDYlYt7BUVnUSQacKYtd4iHfFoSZaLHbkM1kvkM1JvNYv8aeYrX2b59YP67h3Yg7WQpK8ACDrQ0o4aOF1SnM5K5eHdAxqrM89iicEG59ZpBfGtk4usii--tK_jfjVUMECmsMnsucI5TQ0u_trYlFC3OLy3Q6ua16NwZbaFwke7tmLoQ1PBjNPDjfZELgJFfOkLx-k1I4zmuSdLoTLdNjO6eQxsh9uA_bQNthOFwAV0V0E6CuKeV8wHuqptJQ8p3x1KMdCXZPdHW7Atyj-W0qOsYOooO0Q1HLgjGOw_ErBanzT4LrTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65238" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65237">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65236">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWR3j3r9EIJ5HgeUgcGlpSzu7mu3Yj56bUXR5dqcDOMPTucLHsTXdBkIdjfLrLRhbzPVaOiqHC-bKE1U0oOI3VN8Z5YJA7yQzVusjdrZjRso-REg0yEwYZ5K96emohBgnqzFAw4K4yAPUgjqD1pQUqf5FIvKxiE0VU0MmqyamH-7lHXz67hPeNk87EN1hhI3ewtEGh0L3wrRSsadt1_jzpQz7AnCKzVi_wpZ3ZYCh51oOgqiQfGOhjdUYNcvVw0rDPVSM3JY7t9OTFFDRfhFwetuFp2RAJYAU1wEkS6_yqmmAU_R_3axPOHh0gg-5xs--mQ1Nhxy-Gq23BOXcp4PZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داعش با انتشار پوستری، جام جهانی را به بمب‌گذاری و پاپ را به ترور تهدید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65236" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65235">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=N5rI19Olu2UsgpBI8xF2a_eeB89P90dRWMzu7SV73yarKzq2CFjMyUG2XDqYamcUPhUWhucCI0WGKN1k4qbDc3Fw9fcBHy6naQZ1fo8PNWlnizL2w1kmxMg80SfkZoseXyhKn5Lz-WLJP2AjCo43Choj1h-jpSdIzDioQnoXffXZCdrv8whBabN4KZiLVYY5BonRNlGDRVLh_-X0GnplY_t5CMIcBaGRZ7ydPTe4ANtDkeXDeyiP-Z0UBEMP7lHTM-I841gfV3_xl1Nd9pze1baU3szHiKMBW5RYW-9U34VwHpwZQZQDiY7wTt6ZJh6tOEms6rCcKEcpt40uJ6o_9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=N5rI19Olu2UsgpBI8xF2a_eeB89P90dRWMzu7SV73yarKzq2CFjMyUG2XDqYamcUPhUWhucCI0WGKN1k4qbDc3Fw9fcBHy6naQZ1fo8PNWlnizL2w1kmxMg80SfkZoseXyhKn5Lz-WLJP2AjCo43Choj1h-jpSdIzDioQnoXffXZCdrv8whBabN4KZiLVYY5BonRNlGDRVLh_-X0GnplY_t5CMIcBaGRZ7ydPTe4ANtDkeXDeyiP-Z0UBEMP7lHTM-I841gfV3_xl1Nd9pze1baU3szHiKMBW5RYW-9U34VwHpwZQZQDiY7wTt6ZJh6tOEms6rCcKEcpt40uJ6o_9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
علی‌رغم درخواست ترامپ برای آتش‌بس در لبنان، ارتش اسرائیل دقایقی پیش مناطقی از این کشور را که در تصاحب حزب‌الله است، بمباران کرد
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65235" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14e605921.mp4?token=dXJZX3hGYEXbJ6On0ssVV1pP3kc3QjoCnGGqakqHpWl4n_og21o4sGcitEt9Crb_wSmnrup31OwQC9BpUJS-7Bken9mM-CRNJrCBL49u5K4IYmroaPbbhDpYAzsOHbnesi-u69Bmqik6nTmB2Ho3DYDOn-JkjLCtOq3umQ7smDknGkLNi6tTGg1O3xfpBlEYIzkyyMybzdSRDB9FKYRn2U2LRmcc3ERHEDLx2TPbKvA1pNkgvjrgi0SUCdRKn0qsHpbR1HIiASNmMBR8CBqTlqKJbQNqa1VFUl9H0MiFswYgOT_yjCLU3mKUim6yYlST7FeDYsz-yy_wb4Fj95gS7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14e605921.mp4?token=dXJZX3hGYEXbJ6On0ssVV1pP3kc3QjoCnGGqakqHpWl4n_og21o4sGcitEt9Crb_wSmnrup31OwQC9BpUJS-7Bken9mM-CRNJrCBL49u5K4IYmroaPbbhDpYAzsOHbnesi-u69Bmqik6nTmB2Ho3DYDOn-JkjLCtOq3umQ7smDknGkLNi6tTGg1O3xfpBlEYIzkyyMybzdSRDB9FKYRn2U2LRmcc3ERHEDLx2TPbKvA1pNkgvjrgi0SUCdRKn0qsHpbR1HIiASNmMBR8CBqTlqKJbQNqa1VFUl9H0MiFswYgOT_yjCLU3mKUim6yYlST7FeDYsz-yy_wb4Fj95gS7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🔝
دیوید بارنیا رئیس موساد:
تغییر رژیم در ایران یک هدف ممکن و قابل دستیابی است. این یک وظیفه قابل انجام است اما نیازمند تعهد، صبر و فداکاری برای هدف خواهد بود. این وظیفه باید در رأس اولویت‌های ما باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65234" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65233">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=Wj0i4dlEhNHtGUD37qSrxiI63jlTJcUcWd-JDwJ9mkwzU-9_zIYq7TqbESnsoc0WbaWpQ9MW-_TgwMVly5hWPXpSv1MdiRKvAMoXAwxO9rzMtkvWy9O0tFVdOaLdBCUtUEkuQh2icU1P3bF-Uet-9-bbwo3Y85TJUGEPhk5AaOp3HIyFC6BZv0l43hsaqN_lJvrHpym45HdXOTwj6Esj_he1LWE0XdKOG_pAy1F8qfZ-H1720YFR3g1bLqhlqBT_Kb7dTmKEIzNtl_xUzg8-VxdeWCZfI13IZxpGRTnMHXNHJL2lnz1WYWV6ndgG51-qCFPn4HUi2bMn603XynzzrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=Wj0i4dlEhNHtGUD37qSrxiI63jlTJcUcWd-JDwJ9mkwzU-9_zIYq7TqbESnsoc0WbaWpQ9MW-_TgwMVly5hWPXpSv1MdiRKvAMoXAwxO9rzMtkvWy9O0tFVdOaLdBCUtUEkuQh2icU1P3bF-Uet-9-bbwo3Y85TJUGEPhk5AaOp3HIyFC6BZv0l43hsaqN_lJvrHpym45HdXOTwj6Esj_he1LWE0XdKOG_pAy1F8qfZ-H1720YFR3g1bLqhlqBT_Kb7dTmKEIzNtl_xUzg8-VxdeWCZfI13IZxpGRTnMHXNHJL2lnz1WYWV6ndgG51-qCFPn4HUi2bMn603XynzzrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز دانش‌آموزای تهرانی در مخالفت با تاثیر قطعی معدل، جلوی وزارت آموزش و پرورش تجمع کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65232" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65231">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X06labA9-6CSsqZ8Omk11dvfD5Sb1l835WsyFhcSvrZcTA7ZKuoXT-2bUGKHwGxn6l1TLbSTPLNLoonV7Ts-6FIyhKBcsjbe-ZAjQn_5NU0aa_W3p4t0-wKQBc6XHYIL_AD9o-MwTpPN3SN5gaJPRuCHfj9yBbEZUrPCA-3-Ie85C4oHGY-wyGBB_QGod0pLiHdolsP7HlEjDo9qoBELoCOv4GbaweT6OUuxWpzG6gAxszcrYTYY7fNGs1FVjY-1WeMeigxVziDJe61_eKpbAdr0e4WxzB90bhpqf6MukNT-tFugt0kaNtwr8ra6oGKqu_pTFUKrJOrRR5kDcB70Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
روی بهترین مسابقات ورزش های الکترونیک پیش بینی کنید و برنده شوید!
🎮
تنوع گسترده از بازی های انلاین  CSGO, DOTA , FIFA وMORTAL COMBAT ...
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65231" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65229">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=lKDQow-EwEMGMmkFuBxRUbujBR2A0l68veh0q9ecjFdARiRobdsJ5vxasV6LLYQtjDM6jdfYYKfFctM9kj9hotwfXPk1sIomOAOIgGD1XpCX9x93cXjimS3hMxTzFLuZDSbfZopCR4JjlPchcDfKvnnWfyUMGGIPxVKfCqc-z006x3I8LKoK56H9c3kXsut9eBPPP2bWJgXoZ_WH8uhrklnkwEiqTybZpIOyfGE6t8fis6B1d2kc9Er_bbW3dCbg5kkD1qMwjSd7yzcKobrFnaBAXE6a1jbLfude-vC_WrKVoCoSyYaaW6nA1xS4JBF-JuKjp2ytm8XHXYc1HRCTDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=lKDQow-EwEMGMmkFuBxRUbujBR2A0l68veh0q9ecjFdARiRobdsJ5vxasV6LLYQtjDM6jdfYYKfFctM9kj9hotwfXPk1sIomOAOIgGD1XpCX9x93cXjimS3hMxTzFLuZDSbfZopCR4JjlPchcDfKvnnWfyUMGGIPxVKfCqc-z006x3I8LKoK56H9c3kXsut9eBPPP2bWJgXoZ_WH8uhrklnkwEiqTybZpIOyfGE6t8fis6B1d2kc9Er_bbW3dCbg5kkD1qMwjSd7yzcKobrFnaBAXE6a1jbLfude-vC_WrKVoCoSyYaaW6nA1xS4JBF-JuKjp2ytm8XHXYc1HRCTDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
واکنش یک‌عدد ملا در تجمعات شبانه حکومتی مقابل یک ماشین با چند سرنشین زن:
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
