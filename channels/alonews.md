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
<img src="https://cdn4.telesco.pe/file/iTP5dEGbN-JKPgO1U0Og-VqIdnEQwGx1lHjREcYd_j76Fn0z0BlKPAdTNEHVPv400Vq5kzpnwPXCPhoUrm8hmleYnm-JBRtj0OCbyQyhiLWmNBfqjfcOv1X5ZrL3C6pQWBle0TCdky2SWoFEVmh1qjwIFlb2HJsU8jwhDn80ZJ9a5Z7aeN_CSKPnw29BwiUM9W6H71td3auhpMZZb0prWgDatshhwRisBFVdYX5WN0UleM2xynIP6lZJsFEPjTpF2ZEGfY0Hst-gWOeGxqaBUuWO4F1pB7kV1KSKPiBBqn7MGiVfW7yoTTMUrR6j7dBLJ935PxL0TDrJCmRM7Gm5aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 970K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 21:15:03</div>
<hr>

<div class="tg-post" id="msg-125863">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: نخست‌وزیر بنیامین نتانیاهو با هیاتی از مشاوران حقوقی دولت ترامپ دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/alonews/125863" target="_blank">📅 21:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125862">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
پزشکیان: گروه مذاکره‌کننده، آدم‌هایی نیستند که جا بزنند در نتیجه ما باید با قدرت وارد صحنه شویم و از حقوق ملت دفاع کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/alonews/125862" target="_blank">📅 21:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125861">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTl2usr9vGHQ4wxDbbZRgSTu0Z8A3kB44qOQ2YZfqNpqI2DClhs6f1IGB1aH0SQT379qFrc8Dq2DC0zuKxQU62XFXV-PN9yzYOWNPK7oICkib3Ns8QX3SDzFcdj0j1kWLPEhsB5dRFMqWyeihwrn6EenhTOxyRdXLiOSfD8XZbtrIv8kfB-gvT92r5P8aimPLLHZjlAXIeKctppDDrpd38I0yjYRA3laCVxdEw7A-C8kyOh2iSXEVbCb3m-k88aSHD1DdNiRPQGCvSNIBAPWt7OZ8TZbh1bp67xjJ4fX8nC2HzavkTCcNu7XSVS-f9NMdv-eVu08gvTI5eZaogdxiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌جی ۱۲۵ موتور اقتصادی بازار ۳۵۰ میلیون تومان!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/125861" target="_blank">📅 21:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125860">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: ما به آن(حمله اسرائیل به جنوب لبنان) رسیدگی می‌کنیم، همانطور که انتظار می‌رود و ایران نباید شلیک کند
🔴
اما در نهایت، ما فکر می‌کنیم یک توافق—یک توافق عالی—احتمالاً به زودی اتفاق خواهد افتاد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/125860" target="_blank">📅 21:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125859">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
همه‌ی شرکت‌های کانادا پرواز‌ها به کوبا رو برای همیشه، لغو کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/125859" target="_blank">📅 20:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125858">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
گارد ساحلی تایوان چندین کشتی چینی را از آب های محدود رهگیری و اخراج کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/125858" target="_blank">📅 20:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125857">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
یک مقام بلندپایه اسرائیلی: اگر ایران به ما حمله کند، واکنشی صورت خواهد گرفت که شعله‌های جنگ را دوباره برافروخته خواهد کرد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125857" target="_blank">📅 20:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125856">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/At2uyl-3Kl9kkcqnOD6LHs2s8piXm2jXy6-Q7n4V3ITwChQf7bz1js_a6TbWR3VJDTnD4-l1HGCAqvbeiZ47owJL07lpVgP1Ux9Cx6E-nBwZzDDs0iXR20oXJQuRKAazrSuGV2P-8BsdjkQYuBD48bG6tfYnUYQvc_nQf6FtwfTeAojCcR8W-ForpZqjuO3vaIHJ4re4qDntutd0tqqg_F2TkQW7MaB9XSijMunp28WWYwLLqNDdcK-26fltMIC7xPvWw4OGIpjFMbHVYUtyplh8h5dVW4eKeXDaZ5UosKrrS9IleixGxNNdRkRFnClyN8eiqkZOnHlCntfA0sq1XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: صدا و سیما نقدهای غیرمنصفانه کند مجبور هستیم پاسخ درخور بدهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125856" target="_blank">📅 20:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125855">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6565069a.mp4?token=KpJxN30WOW4VGOA27bWU7Py4Ftrry32B603gi3Ljc2FEku1jlFzd5AqEbc9-I-FZnmxcwuiD996cEb65H7TeoJ5xzd0YZLSfseQM75OGvafQL_X5HZ4ywTBLV3ZImKLQeSj3Ox_u8aD_7NZhBa0rSHZKRQHPbYoO2knBikSlxn6-b29fetFJmmCoCXTEXeDogxtAlh-8CU6JjSVPn05oJgbhzFIFdVqTJ1J8VgEDLlk_ftjPVEUXCvfdv-0KeRI00gsDVJI0TAmWsMrrcVOFefPrBTx-yGTPR6uKzq9TaTnaq_ibdM4yMQO8f3feSG1fpnrcJLk3fOKTMUYuQ9_5pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6565069a.mp4?token=KpJxN30WOW4VGOA27bWU7Py4Ftrry32B603gi3Ljc2FEku1jlFzd5AqEbc9-I-FZnmxcwuiD996cEb65H7TeoJ5xzd0YZLSfseQM75OGvafQL_X5HZ4ywTBLV3ZImKLQeSj3Ox_u8aD_7NZhBa0rSHZKRQHPbYoO2knBikSlxn6-b29fetFJmmCoCXTEXeDogxtAlh-8CU6JjSVPn05oJgbhzFIFdVqTJ1J8VgEDLlk_ftjPVEUXCvfdv-0KeRI00gsDVJI0TAmWsMrrcVOFefPrBTx-yGTPR6uKzq9TaTnaq_ibdM4yMQO8f3feSG1fpnrcJLk3fOKTMUYuQ9_5pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوی حملهِ به ضاحیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125855" target="_blank">📅 20:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125854">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34153808d9.mp4?token=A247W8G0xMya8MSz8l4lppneQY6v5XcQwGEqStBQKpkDbqAJ2kha75CZ-sK8aetM9jBuhqDzWKzxzD0h4w9TkbjWcmFNW-y3RE6EoYdQC0lbCd9gSewQvAsrQFyT-sppctIhb1tCK8ExmX4IssVwGauMeGIBg_Xm5Z83hncRIZixcNQtTqYw3B0fS7bS7wHwV--9ZbVsX1o8sD9fgSHFotZmKj6010s1LHCAj3mKRr0qxARJYAXmIt4GCZOBLmVYoTMO5QIe1FTv1IBIrCjGlQXf2-nRGF0AW401U9HvYGL74iY7ImqGBZ3ahU2YBPETZK-qU_D1SicVRK66a88kAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34153808d9.mp4?token=A247W8G0xMya8MSz8l4lppneQY6v5XcQwGEqStBQKpkDbqAJ2kha75CZ-sK8aetM9jBuhqDzWKzxzD0h4w9TkbjWcmFNW-y3RE6EoYdQC0lbCd9gSewQvAsrQFyT-sppctIhb1tCK8ExmX4IssVwGauMeGIBg_Xm5Z83hncRIZixcNQtTqYw3B0fS7bS7wHwV--9ZbVsX1o8sD9fgSHFotZmKj6010s1LHCAj3mKRr0qxARJYAXmIt4GCZOBLmVYoTMO5QIe1FTv1IBIrCjGlQXf2-nRGF0AW401U9HvYGL74iY7ImqGBZ3ahU2YBPETZK-qU_D1SicVRK66a88kAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد وعده خود مبنی بر عدم آغاز جنگ‌های جدید: من هیچ وعده‌ای ندادم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125854" target="_blank">📅 20:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125853">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d20dc92a92.mp4?token=NotqOtuVsZgZ64j9bjI2venmAdC3C4x_JDnbYXkJVzoTWTs2eummCmdF5YWWfEScIyFFam6E-eIu1OmcBpqWcZQQuYLu-XbDKExaHyQgHTQT9VS6amt7qdzhO3G6rcF4I0RtG6nbzCF-E_jgRTzV0LY1bSDi14th1ysSjr_RUrjx50j3IjV0ZHMhmzXSLD_oHKEeaO09B0tsMNBPo7CRqAWEqm0A7xVqycq2UthUNkG_v88s99X_8OVoSJZ10MOvxbnrQqcvNHiJL7lRdXdiBoplKmj9tbMeONxJnJO6vUmogIjV1ZT9pAbrKQfDOpXnf49C8XULnp3RsKzi-NZbbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d20dc92a92.mp4?token=NotqOtuVsZgZ64j9bjI2venmAdC3C4x_JDnbYXkJVzoTWTs2eummCmdF5YWWfEScIyFFam6E-eIu1OmcBpqWcZQQuYLu-XbDKExaHyQgHTQT9VS6amt7qdzhO3G6rcF4I0RtG6nbzCF-E_jgRTzV0LY1bSDi14th1ysSjr_RUrjx50j3IjV0ZHMhmzXSLD_oHKEeaO09B0tsMNBPo7CRqAWEqm0A7xVqycq2UthUNkG_v88s99X_8OVoSJZ10MOvxbnrQqcvNHiJL7lRdXdiBoplKmj9tbMeONxJnJO6vUmogIjV1ZT9pAbrKQfDOpXnf49C8XULnp3RsKzi-NZbbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:ما به یک کشور بسیار قدرتمند را مسلط شدیم: ونزوئلا. سربازان زیادی، یک ارتش بزرگ و قوی.
🔴
ما ونزوئلا را در عرض چند دقیقه تصرف کردیم.
🔴
ما توانایی ایران را در عرض چند روز نابود کردیم. هیچ‌کس هرگز چیزی شبیه به این ندیده است. حالا من می‌خواهم آن را تمام کنم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125853" target="_blank">📅 20:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125852">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef44fe5bc.mp4?token=EvPlOeomcWYZsGAbD-nCIqO09xWXNb8Pls53396MVur51AkwFhLZeQVOzORAE-fqP00yYKDoPY8E6pHgIEnuwTcWK3ZsuyOY5ExrWCp3q2w6cscmMhTYrh8lnhMlM3yCw7NXsKjhfKubNSrIE5scETuqGsiSoCgTI4mOBDwYGtYkk9_eC018Air3kRVC7jST3Ql9Pdh0HyAI2JFLiHhmkrT_HX_dMsXCNB_-3JWr57kJipHYDQjJJuBvfH0fAMyB3Vu0SbpIrnrWYOSjV8W03FEyKLCqxjjiY1WPvoYNMSOXGWBjY6ysNrkHhUToUu_GX4sMt3x9CDm0kOsQGffAlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef44fe5bc.mp4?token=EvPlOeomcWYZsGAbD-nCIqO09xWXNb8Pls53396MVur51AkwFhLZeQVOzORAE-fqP00yYKDoPY8E6pHgIEnuwTcWK3ZsuyOY5ExrWCp3q2w6cscmMhTYrh8lnhMlM3yCw7NXsKjhfKubNSrIE5scETuqGsiSoCgTI4mOBDwYGtYkk9_eC018Air3kRVC7jST3Ql9Pdh0HyAI2JFLiHhmkrT_HX_dMsXCNB_-3JWr57kJipHYDQjJJuBvfH0fAMyB3Vu0SbpIrnrWYOSjV8W03FEyKLCqxjjiY1WPvoYNMSOXGWBjY6ysNrkHhUToUu_GX4sMt3x9CDm0kOsQGffAlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث درباره جمهوري اسلامي ایران: کارها در جریان است. حمل و نقل دریایی در حال عبور است. ایران نباید به آن شلیک کند و وقتی این کار را انجام می‌دهند، ما طبق انتظار با آن برخورد می‌کنیم.
🔴
اما در نهایت، ما معتقدیم که یک توافق، یک توافق عالی، به زودی محتمل است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125852" target="_blank">📅 20:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125851">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
شرکت هواپیمای هلندی "KLM" پروازهارو به اسرائیل، تا ۲۷ ژوئیه لغو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125851" target="_blank">📅 20:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125850">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
کانال ۱۲اسرائیل: اسرائیل در حال رصد و آماده شدن برای این احتمال است که ایران پس از هدف قرار دادن ضاحیه جنوب بیروت، تهدیدات خود را عملی کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125850" target="_blank">📅 20:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125849">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
قطر به دلیل تنش‌های منطقه‌ای اعلامیه ناوبری هوایی (NOTAM) صادر کرده و از پروازهایی که تا حد امکان از حریم هوایی این کشور بین 7 تا 13 ژوئن عبور نمی‌کنند، خواسته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125849" target="_blank">📅 20:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125848">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
فیدان وزیر امور خارجه ترکیه: اسرائیل معتقد است که هرگونه توافقی که بین آمریکا و ایران در شکل فعلی آن حاصل شود، به نفع آن نیست و بنابراین به دنبال مانع‌تراشی در روند مذاکرات است.
🔴
ما از جامعه بین‌المللی می‌خواهیم که به اسرائیل فشار بیاورد تا از مختل شدن تلاش‌های صلح و مذاکرات جاری جلوگیری شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125848" target="_blank">📅 20:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125847">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل : نتانیاهو به خاطر تهدیدهای ایران، یه جلسه امنیتی فوری گذاشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125847" target="_blank">📅 20:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125846">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/509058b963.mp4?token=apMkQRPn-8AIkn3A2KAnapvWbzKb1DO6cVf4qujTEm3qs_gAuX2oeyY991XxkevUZJRBKIZ97u1sPMVFcMl_5I02ydxFXmlW9Z9k2ALl8Ji0-Gx-BnIkMHVTD6hvbzmO5OSOWl3KBqzIhbGsW0snXIDdGWBVgAVo7udPo7gTfbz30mp8e6yI_eY3OrbPDfJtY29iwqsXxBbyByn7XSND2XSCY0T6PzecVUl6qeSOOdVKdHVMWbKcUMJunb5qm6l8vBGfDPmYrOET3n2kOlO5vVcOumtm9mZbVbctJBg-6XlGAJMoDhiPc2fQgk0BCzQ9RvI0S3P71fAs8iC7bOaw2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/509058b963.mp4?token=apMkQRPn-8AIkn3A2KAnapvWbzKb1DO6cVf4qujTEm3qs_gAuX2oeyY991XxkevUZJRBKIZ97u1sPMVFcMl_5I02ydxFXmlW9Z9k2ALl8Ji0-Gx-BnIkMHVTD6hvbzmO5OSOWl3KBqzIhbGsW0snXIDdGWBVgAVo7udPo7gTfbz30mp8e6yI_eY3OrbPDfJtY29iwqsXxBbyByn7XSND2XSCY0T6PzecVUl6qeSOOdVKdHVMWbKcUMJunb5qm6l8vBGfDPmYrOET3n2kOlO5vVcOumtm9mZbVbctJBg-6XlGAJMoDhiPc2fQgk0BCzQ9RvI0S3P71fAs8iC7bOaw2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست نتانیاهو فقط همین هفته
:
- نیروهامون قلعه بوفور رو گرفتن و ۳۵۰ نفر از نیروهای دشمن رو از بین بردن. ماجرا هنوز ادامه داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125846" target="_blank">📅 20:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125843">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rm8smyLMAAUZYXmsQYl9H9mgeF4nIO7eIODWsD1FVbVdwYe8BW_FX-a0LveXMEAM_nrswitOqddeWtrKwGjs9RYsl6_Aj9DX-XqZGPxcpLwSHAk-D4eyRi32mO_WUaAvT4nXo6XZq6Edtu04qPhsPfmmqrJyOUz6PfYVlqePq_ZJQ7w99Do3wgkl7yB71UBsvyzOHBGQiRmml1UPWGUp3GCqn9G90cuauU1EbKIJFpFOtG2ooGF6S0Xlo_Z0ddvzNU5zxzVLJUxK16DdCf-yCEbeM-GlBKVrOoX_7zAEDwvL-pLNmMf4nAOa3iGJd-sFHNU2KEBek_Oq9kP7I6lHqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MIkmLnIQFBA2pPakG5LgSarsNUHBqHfRARAjeX5YxpJubf495JCJvC874rPbAtuljCJ9uyV2KogL3bozybg6xBjw1TkLP445f-cD3nGKYfFQJjj2wPbgDdwVAxCDfQCoWCoLSfujw_e4MhM1g6Q1UVGPpASC0Ja5PvIxR2Ddz0CWFHsKf0LmcX75AxrRfyo2JqfGMnRxvRrApI8Ld2Lz1inGsT7-nB8res0UY8WOI6NoyLpQ7lvHiIFr-w_gyc6BBa3vV_URdyE5pRhJghFRQuVWQ7yFnSgmSjYe2QR24egULUJj8EbVKLCkigpG1aB59iz2gy_rHq-Vrx1jr4oUNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4001f02598.mp4?token=mkk8TY4E2PQabBulEiZMaUaUpCiSqwsIHi8IChHKUWwZLogGraWfUmgIrk1SJYcw0FuLg4YG73NMNL7qVLEJO1e8U1M-Lvo3cThOfXTgWdcQEthKFkfRnzkLd3XVfV9Z8YKuIbG9sOra3RgsBpxfojXm1coXjiASBFBv8vYt_mkd3RCIVHrSdrRTFV7wB_fAep7nd64YUutFMD0znOFL_YMybvMP21qZTk-q0PocQMM5hDBoWy1Nme-yGmEkW7oLSUYRuxyCYSIaDb0GkoYUBb5j9_AUEZ6ywkc0qHn59zVS7wR2uJwpihHcZ23Wc_vIRWTd-wrMpxL8HxGnyvfefg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4001f02598.mp4?token=mkk8TY4E2PQabBulEiZMaUaUpCiSqwsIHi8IChHKUWwZLogGraWfUmgIrk1SJYcw0FuLg4YG73NMNL7qVLEJO1e8U1M-Lvo3cThOfXTgWdcQEthKFkfRnzkLd3XVfV9Z8YKuIbG9sOra3RgsBpxfojXm1coXjiASBFBv8vYt_mkd3RCIVHrSdrRTFV7wB_fAep7nd64YUutFMD0znOFL_YMybvMP21qZTk-q0PocQMM5hDBoWy1Nme-yGmEkW7oLSUYRuxyCYSIaDb0GkoYUBb5j9_AUEZ6ywkc0qHn59zVS7wR2uJwpihHcZ23Wc_vIRWTd-wrMpxL8HxGnyvfefg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حملات شدید به لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125843" target="_blank">📅 19:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125842">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXn4P4pzrW9MVE3o-58XIaZvt2ZSzxlPt4HBghr2u33NIcLculxH8HLAnJdXlUVvGK6-aOj5QfJ9daeYe-juwAAvjKkBimlN0YYzpda6JTKH8XfT0u1GNY91B3OT_Boe_c5cr-vulY23jOWKrhUj7KJaQsCBwVDPr9fBsbSNY5OqBWqKgow_BAFy-xUXGLh_ZqJfnmf7TjG7KRs5fa6HJIXW-j71hl9si_vf5v-6K2WLJR1DpLWkNO5lqPK4TltFOcHcrAcU5tMX9b-jcScOW6QFX3V4qWsE1VyQuwFkvxmlCxx8haWv3lkpc0MAusMsOmoayshUUy6u-EDpObGT9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات به لبنان کماکان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125842" target="_blank">📅 19:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125841">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
آکسیوس: «اسرائیل پیش از حمله به ضاحیه بیروت، به دولت ترامپ اطلاع داده بود»
🔴
پایگاه خبری اکسیوس به نقل از مقامات اسرائیلی اعلام کرد: «حمله هوایی به ضاحیه جنوبی بیروت پاسخی به حمله موشکی اخیر حزب الله بود.»
🔴
آکسیوس همچنین به نقل از یک مقام آمریکایی و دو منبع آگاه اعلام کرد: «اسرائیل قبل از حمله هوایی به حومه جنوبی دولت ترامپ را مطلع کرده بود.»
🔴
اکسیوس تصریح کرد: «اسرائیل به دولت ترامپ اطلاع داده که حملات مداوم حزب الله به اسرائیل، به آن حق حمله به بیروت را می‌دهد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125841" target="_blank">📅 19:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125840">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JO_HmmUEnljiuMp6NLZojpfxDdxT6-mgERH9bGZQ-vgkMSuYI-R_S8THlXQZ8HImh4ur0ecTPTH4QPhXaJYaPL3Apv68kJINFa0mD1pY5y6LlpXdZh8HUSecC2FqH1QP_77JYI50Ce_Du2Xydg9hdGsYyFVTHc6J7T-J1XPTCiC4DOORJ1Z4zQXDMzN6jDsgc9eyNBZ3lVCyvsXTAfamk1gcUy18PLhdPHoyT-Y6v_gmvZYYANq1SHP5RpJ9UtuvSHjaoeUvPKoJJ-D83cSLF0CTAKg_I6ykZksNFF83cqGYTzG51ouR0sxfmjxupbM0fgsnlrgErHZKgUTLb15E5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف:
آنها نه به آتش‌بس متعهدند و نه به گفتگو باور دارند، و با نشان دادن از طریق محاصره دریایی و نقض توافقات مربوط به لبنان، تنها زبان قدرت را می‌فهمند.
🔴
محاصره دریایی علیه ملت ایران و چراغ سبز امروز آمریکا به رژیم صهیونیستی، پایگاه‌ها و دارایی‌های آمریکا و رژیم در منطقه را به اهداف مشروع تبدیل می‌کند.
🔴
دست نیروهای مسلح ما، همانند همیشه، باز است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/125840" target="_blank">📅 19:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125839">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
هم اکنون نشست فوری نتانیاهو با فرماندهان نظامی برای بررسی تحولات منطقه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/125839" target="_blank">📅 19:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125838">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
قطر آسمان خود را بست!
🔴
قطر اطلاعیه NOTAM صادر کرده است که پروازها را از طریق فضای هوایی خود هدایت مجدد می‌کند و مسیرهای جایگزین برای هواپیماهای پرواز کننده از دوحه و فرودگاه‌های عربستان سعودی ارائه می‌دهد.
🔴
این اطلاعیه از ۷ ژوئن تا ۱۴ ژوئن معتبر است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/125838" target="_blank">📅 19:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125837">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
رئیس ستاد کل ارتش اسرائیل:
«به ارزیابی وضعیت در مورد ایران ادامه می‌دهیم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/125837" target="_blank">📅 19:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125836">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
صنوبری کارشناسان شبکه خبر هم اکنون: آقای قالیباف،عراقچی، فرمانده خاتم الانبیاء چند روز پیش هشدار دادند که اگر ضاحیه مورد حمله قرار بگیرد ما هم اسرائیل را مورد حمله قرار میدهیم، اکنون وقت عملیاتی کردن این هشدار ها است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/125836" target="_blank">📅 19:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125835">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twscDlmzjNkeqBE6bqNIUmL-0q6ErbfFd0AsNnstuc_BSKY9GBuevR7k4qLV_hAArDpIb0s1qbUDw_wzReTGB8UNOgAbSluPXXa56Kp1IM1PoNWP8H3lhBpoUbiBQPcRfjxEtSNb1l_oOkR6UFBFV0521uIRKRyR74Y15Nh3bCSmuy5SG0AdWcTkdD-feLa3NjhzU8aHe4cCAWMARCKKUQpR_qIcKYLBq7bH8O8xyTUHTaVR1x7E7l5dtTtRtxXKm3FurQ-ogG7UY_eNjy6AmPRaIeufIPy_B2uSJPwYN95augsPmxqJdt7UsZko9jCF5VoVaqkcE6iCSt5Huz3ZKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر جنگ آمریکا:
«ما معتقدیم که
به زودی یک "توافق عالی" با ایران منعقد خواهد شد
.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/125835" target="_blank">📅 19:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125834">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🌐
نامحدود فقط 90 تومن
😍
فقط ۵۰ نفر اول
❤️
✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ   بقیه هنوز VPN حجمی میفروشن اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 90 تومن
🏷️
💥
بدون محدودیت حجم
⬇️
⬇️
⬇️
@NetAazaadBot @NetAazaadBot</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/125834" target="_blank">📅 19:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125833">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V_zef-lCqUUNqXsn3KA-HrSBzMXZIDsPmo4yPmh_hLwsC7K1NUkfKxzWqqruV8bYyhaBSw7wy8wcqx-pixLoArUYPBuy-po0Pf30gsdCVZAkWPjRcvINX7VYTy1IhFlynIJZgBOfPzcGkpDOWpJBsV-iTD1KvQibGKK0LvrZ_mfrv32L4M_MUzKwtDuW5aKReYHyepyFZfCU7XT-4b4ZfY6eRVE0Tw-JX8mYaQeVBrjGZSSxd8v0kJXqZTQzOwTH4qhxZzJsl_GWMMSaK5GOD4xLtb6bq5Mnrl0bDVtYYSEOjLdBreZmC3kdw5yLhgiYXOFLxDeszorIy-A6VvpAPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
نامحدود فقط 90 تومن
😍
فقط ۵۰ نفر اول
❤️
✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 90 تومن
🏷️
💥
بدون محدودیت حجم
⬇️
⬇️
⬇️
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/125833" target="_blank">📅 19:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125832">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7e1602fd2f.mp4?token=nVNkLkQJDpdLDZG76LQ8Qp9HrmEHKsYjBZ000IvPl-DW8kiLmvbTh6QaDXGEIRxLZZEVLA0f4kYxSBHSQxwFtaXAyx4OwUk0w2dkwnKhz_BCqK7KX4ASlrMjI6XlF52eaXU6u57GtEevC6a-kI7sbL-R6WNVqkIqX7b66za8InF7u1mY-oGGgVnNFydOFVOhE4jaCMBsOWfSQQOq-7h4ETfiB_C38AJlTxqVPFHrKTocnz1tJMoWR2P6wNgqycwbF0WyGFZvHS7WwLMTHlYFW_6CnebffbavnxOhkpbDkNRyj-uSbenoqQeR2Q3bihJCeuPDu25IgJC2SeGFagQqPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7e1602fd2f.mp4?token=nVNkLkQJDpdLDZG76LQ8Qp9HrmEHKsYjBZ000IvPl-DW8kiLmvbTh6QaDXGEIRxLZZEVLA0f4kYxSBHSQxwFtaXAyx4OwUk0w2dkwnKhz_BCqK7KX4ASlrMjI6XlF52eaXU6u57GtEevC6a-kI7sbL-R6WNVqkIqX7b66za8InF7u1mY-oGGgVnNFydOFVOhE4jaCMBsOWfSQQOq-7h4ETfiB_C38AJlTxqVPFHrKTocnz1tJMoWR2P6wNgqycwbF0WyGFZvHS7WwLMTHlYFW_6CnebffbavnxOhkpbDkNRyj-uSbenoqQeR2Q3bihJCeuPDu25IgJC2SeGFagQqPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ با مجری دعواش شد و خیلی منطقی وسط مصاحبه ول کرد رفت
مجری: شما هیچ مدرکی برای تقلب در انتخابات ندارین.
ترامپ: من ۹۴ صفحه در مورد این موضوع ارائه کردم، ولی شما رسانه ها همیشه دروغ میگین، خسته شدم دیگه، من میرم.
مجری: ترو خدا نه، کلی راه بخاطر شما اومدم.
ترامپ: به تخمم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/125832" target="_blank">📅 18:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125831">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
خبرگزاری معتبر تسنیم: اسرائیل از ترس واکنش احتمالی ایران به حمله به ضاحیه در حالت آماده باش قرار گرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125831" target="_blank">📅 18:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125830">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
پیش‌نویس در مرز اتمام؟
احمد زیدآبادی در تلگرامش نوشت:
🔴
ظاهراً پیش‌نویس تفاهم‌نامهٔ موقت بین ایران و آمریکا به مرز اتمام رسیده است. اگر اینطور نبود نتانیاهو دستور حمله به ضاحیهٔ بیروت را صادر نمی‌کرد!
🔴
نسبت نتانیاهو با صلح و آرامش در خاورمیانه مثل حس گربه به آب است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/125830" target="_blank">📅 18:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125829">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae34bf9ff.mp4?token=Qkq2CDBeg20o8z_c7EWPMJbT3b_VB4Gqzwit47_K-DoMz6YcPEn6q9AligPIwaeKfbFfzdCQytGDumDPrwD2J2A8AcWAqDN3X81viVVweTBmwsDLWr_pL6R37e-DCTwY3-zPRVXftaBDubifGcsenidzw-Utsc_VQuWw7wDZJAcfZ7IF5SuBzQ5oD8_9_19-7f37fQXqD13qfd6Hiirwy0hAZG5vLr1UGbPa6E0Rt1cBPSzBirVKxrfKJeITRm4Wh5ocIdl0TL7VIYZsJPMuZuRCSADP99xcpDsy1AXjAF_1rKUCxcBjs83v5V7jbSGTmuYa8VCC2-YNPYkHtOUIbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae34bf9ff.mp4?token=Qkq2CDBeg20o8z_c7EWPMJbT3b_VB4Gqzwit47_K-DoMz6YcPEn6q9AligPIwaeKfbFfzdCQytGDumDPrwD2J2A8AcWAqDN3X81viVVweTBmwsDLWr_pL6R37e-DCTwY3-zPRVXftaBDubifGcsenidzw-Utsc_VQuWw7wDZJAcfZ7IF5SuBzQ5oD8_9_19-7f37fQXqD13qfd6Hiirwy0hAZG5vLr1UGbPa6E0Rt1cBPSzBirVKxrfKJeITRm4Wh5ocIdl0TL7VIYZsJPMuZuRCSADP99xcpDsy1AXjAF_1rKUCxcBjs83v5V7jbSGTmuYa8VCC2-YNPYkHtOUIbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
من این جنگ‌های بی‌پایان را دوست ندارم، و این جنگ بی‌پایان نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125829" target="_blank">📅 18:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125828">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seDRVCHpZJgC_itu_EF0CLGu1BKEyQFNTxcUKkRQFvcKB24RerA7JP0XEmTNIg5gsYPv4Cs1pSWUdUjhimt-_-YKWDqGX61FOo24njtRabk3E-Rz2c6gAPV0sNL5ds12Rn7Ccs5c8Am3UtKLkwIQZZoYUM6hkhxiIRYXg1dXlQgUJlCnoQ9l-ob3Er4Gjn9TLvvT1bEHgVrTen8wMXtj3ReLxvAlmCBS2vTPryN3aGsTbxnx4C68Y2b9rZtyx8299hQYoTKITpTwPtp5J6mrLIUOCOcAPRgHBnsu_xpSiHLRLSd5cl3h5b01o4wgi868yUgG-PH7PiQv_dsoHDsZQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125828" target="_blank">📅 18:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125827">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4GX0F4PzGFEPRVkL9B5jkeV3DBbyFwcXB7J0P2eHsZh_yMYNnLqPW2F0PIL1RFrBRfniNL5EjG95vrFiyetcvxQ5Tp1z8G81BImDWWih5A1_h4xb9dZuaq0gpMAZ82JPar-GATm7LP8aQw4VRBxPMpGjjhkY5QMhh-QBs9u7wTbvStJMBiGFMbOYZwiIEWe1pFh6kfyAjk_dSQyY9Qz8tTOo_5yhNyQ_jrdF-akBccGyfeAADmOYo95oGJE8CUhprFgDGbkWFLO3Av4zQXkYzxy2WuQvQ8sP36jSW9va3jnggNvr-1w6TmTBYbWnVGEWkEwf-jDZwTeGXovYVIXiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس تهدید رضایی مبنی بر چشم ها امشب به آسمان باشه ،حملات اسراییل به صور لبنان سنگین تر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125827" target="_blank">📅 18:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125826">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کسی که بخواد بزنه تهدید نمیکنه</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125826" target="_blank">📅 18:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125825">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
آکسیوس به نقل از مقامات اسرائیلی: حمله هوایی به حومه جنوبی بیروت پاسخی به حمله موشکی اخیر حزب الله بود‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/125825" target="_blank">📅 18:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125824">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kv0OHCSHWZpUJ9Zl_QwYvZh3O4xfv-0I2oOto2k8kTE6qbo-5SdQkrPHqn8hz-qgQuemz-Aj6kv8FhEPNonQITlgsS-oQNsuLVOdmxslnGcs1L3YMmjnhzcnqDf56oj_8QAw0XLowRrN2QXqvvrRThUNZ5IM1iG-63VEk0p2fg3cL_8Q7kWwKcVXxuaAVnYpJyl7FqYUXdTqn1fRUzdXZ5fqrVLZHQpjRS5kC6HFdMg8Z5oqklyxtimALzQffUuXyzo5OUBr7thLyxk12u4hLg5RIp4mGQTaLLRoCvE7lebONZ_BQPZVnWZLVa14uc7TwQ_PmI7NfCGtnaCggvArpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی عضو تیم مذاکره‌کننده:
صهیونیست‌ها مجازات خواهند شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/125824" target="_blank">📅 18:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125822">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOUga7NKl6erMYMLX5XvbXkiVeGFwet2ppxbWHXAQuRscqqOYPzc_MKrRLyITvZfrR1AgQ9bx_Hfi14U9dFQMjbr-eMK1U3fTrG4uPRTMtGuaVVeUTAZLaitMyagHR0BrybkIC1H0gbL6251il0wCZ22Lr7fjUPjY1Wby9oXm25KgLQWSsOL-nu3n5ALWEUo0nRkrIRA3PVsu-01zKMD60Kp9HwZrNfpnaUZU8xX5JkdJso4vcJ75lL_m9rusJxZk1XDVYfgdxxq-tJN5VjoKOUj2Fn22hdyvSMzR0HOPT_-A4G8thZtbw1Q33RPy-Mz1JveUfLtJ8ObK9nNTCs_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلسه اضطراری شورای عالی امنیت ملی ایران حدود نیم ساعت پیش به پایان رسید و
«تصمیمی گرفته شده است»،
اما منتشر نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/125822" target="_blank">📅 18:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125821">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
اسرائیل به دره بقاع که از مناطق مهم حزب الله هست هم حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/125821" target="_blank">📅 18:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125820">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
صدا و سیما داره آهنگ تو رستم تهمتنی بزن که خوب میزنی رو نشون میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/125820" target="_blank">📅 18:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125819">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ip6J4da-JFJL5siRT2P-XgjBZOjkRRjBpuHQVhYmuWPAz02iRfXXrJh0jEHSAEQ7_wIwKcC8EAJqlbephybJzUqbJTxbnrB6ExJaRx9eVT2_kJO6zrv2OobUJu5PjETKytvV47fqzesH4EWYSAJkVSPUXFJ0JFPpXwNhKI4CCiTeni9UGmLNe6xOljkmhAKaiCsFi4g8eF7mhv95F297vf7lz2BE4TWTYECoWAJ1l7frON7_gq9tSozUBGspC6w46ui7bqbYPBJXmX7L7g9-TPZtR3OD9t0VNQh8hEGUvK8u9wvu1dtvE-gskIEZIvY9kDlSPDgduiGnjWauEtqYuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار در بندر صور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/125819" target="_blank">📅 18:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125818">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
احتمالا تا ساعاتی دیگه حمله به بحرین انجام بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/125818" target="_blank">📅 18:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125816">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDx889t9H0wsPIbdJmWzfOBj_p_ri5ch_UREVFzUlQbr3v_Dh3KXXsR9a2AvDjQvJweR0bdrZ9co8uxp-ZIcq3MsZdTM4lXJh3JrAN1fGoxTSkpPXhEH9LBpV8T7ZxBzHGSwxwoI4__oL7N-ecoI67Yluq66GWsNL9hXXFi5r2q3FuYJ4T01Kz9v5Aty2BTx-r39GU92j4jrAuhjwRMskLCyslCgUxdDM4Fl9YckqrBpMs4UXQbLeM8S1Lo3BUMv-hOe62HJxumXam6ZYGJuoRC6Wh75q95tusZJmMUIiDWiFU1DbQqamZpBTo9DSfHHy1-mylzZVnyrnZUNwNuewQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zf_yYZ_JNx382xSyoZ9i1TPb8iRVazQ2FPr0l-uRi_xA65i_-s52uhE1DPsXSkHamECCCYXU-pzcitgbnFvQSxyGFHuPLzqR-hH8GPh2rr5SVzFKYZqplehkajaaHMb4Si6pQ_XuID-FWhxhu7J_CylGkte3iFgfetSVYzoTTT_bQz095KITqoVC93qqpXtHZJPtP6976cmXZXclzwV7zRAb2ei76GMwA9UbvxpvBS9qJQqnHtlyW9sKylngEBk1LcC7Ddq9ruIVIk_arFXkmjJgxVbBqgzwSl5LVpq4bXvKlWPg7jfGON0Ti_OS3iH8E4FkbdhItJ3rZmgfueu4PA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بمباران سنگین لبنان کماکان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/125816" target="_blank">📅 18:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125814">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8e6d5591.mp4?token=ez5M4SUof5lZXa8WIZYiKhPb4El9Wdq24bEEem-xNaQDB0EAUVw5wgAOapDlgRHzA5XzeF_vnvFwVA5iJslo2JRVcVFjFt0K4MneFzBHAJGzbYXeBbUd1KcPcLMOGME_fKnsYAGD8HNuj458c8dUVgw2Fvqq5EgbqTGnWVP3zRNjFuXd6nA3ySecK74G-r94YcNIMSmbD5xXfiqWEcA0bpLCF6nfJPYHaMPZ2wJjXzssm1PvRR5E1HB-wbN_5MqDWNx8XuNtPnCogAdU1ZEDiQ0L2f8WSGayDUvWb5iELqGD74S-P2RpiMLhu5V61RwmI0iMlpT_Sox1PCtO5R7ffA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8e6d5591.mp4?token=ez5M4SUof5lZXa8WIZYiKhPb4El9Wdq24bEEem-xNaQDB0EAUVw5wgAOapDlgRHzA5XzeF_vnvFwVA5iJslo2JRVcVFjFt0K4MneFzBHAJGzbYXeBbUd1KcPcLMOGME_fKnsYAGD8HNuj458c8dUVgw2Fvqq5EgbqTGnWVP3zRNjFuXd6nA3ySecK74G-r94YcNIMSmbD5xXfiqWEcA0bpLCF6nfJPYHaMPZ2wJjXzssm1PvRR5E1HB-wbN_5MqDWNx8XuNtPnCogAdU1ZEDiQ0L2f8WSGayDUvWb5iELqGD74S-P2RpiMLhu5V61RwmI0iMlpT_Sox1PCtO5R7ffA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همزمان با تهدید‌های ایران، ارتش اسرائیل موج سنگینی از حملات را به صور انجام داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/125814" target="_blank">📅 18:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125813">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025910fe6e.mp4?token=rQxt55Yf2_UXJLUF5Od_68WCFRfNSw0DcJuzOgP2fljkI7QpXCXJ0LzP3yb6yhD1visOIFLet3sRpiY3Pbf6PjTDuaRPBxTmlz_dAXe6mW_9vPFSbwK6Ys4mDsZhZd8yH1PIsT4pk-WZXBcbbGSA_aCNOtJp3ulMwutqNjSRTEz4k7ampkVttTYNkV032eYl9ZDFQ88IYQh7AURlBQm-kwC9ednfW0OV2Wz8s_e4m0XzlZ9QacQviYJHOz3pOHs4ve5O3ZRBkQFDYBXnHQ25oMOLWODmQt7kXLGrDxDw9orSp8HqYCqQSTTbJfrYXJYDXuykg4L436EAp_vp8BHUqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025910fe6e.mp4?token=rQxt55Yf2_UXJLUF5Od_68WCFRfNSw0DcJuzOgP2fljkI7QpXCXJ0LzP3yb6yhD1visOIFLet3sRpiY3Pbf6PjTDuaRPBxTmlz_dAXe6mW_9vPFSbwK6Ys4mDsZhZd8yH1PIsT4pk-WZXBcbbGSA_aCNOtJp3ulMwutqNjSRTEz4k7ampkVttTYNkV032eYl9ZDFQ88IYQh7AURlBQm-kwC9ednfW0OV2Wz8s_e4m0XzlZ9QacQviYJHOz3pOHs4ve5O3ZRBkQFDYBXnHQ25oMOLWODmQt7kXLGrDxDw9orSp8HqYCqQSTTbJfrYXJYDXuykg4L436EAp_vp8BHUqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات بی امان اسرائیل به لبنان
‼️
🔴
صحنه‌هایی از السکسکیه، جنوب لبنان، پس از یک حمله هوایی اسرائیل.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125813" target="_blank">📅 18:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125812">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">💢
فوووووووووری/پرواز جنگنده‌های اسرائیلی به مقصد نامعلوم
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125812" target="_blank">📅 18:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125811">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMeeBj7S87MV3Xw_Dga5c_jxb6nsmGnIQkQCWVIEWVw3z5UjvDK8dt4eLL0GeOx6x1oGdE6Y_fqfd2OaeFtDVmx-VKhWkqbnw7RVPnfjxbbrkVHrVSuQi78CepiyKre0BHOta2-EenKFlarFWh6ytieHF8KrMDan8BQYexOm1qZCPCkZ-Y6s4uQEp4vONjzvPzcIwoGFtYqTSCVXtcOwg-8igg969sZYIkZAybWf7Ie9mrwh2yq4hKMIcM6-8kDEOHwwZ3gDpfCWxiRzWZXaoZyQpSD0aSffBe7gQWmLhBJXF3V3OvA6a886fyg_aHsAU8w9SpX4jEtUwokTEgMhOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/125811" target="_blank">📅 18:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125810">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/125810" target="_blank">📅 17:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125809">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
اما احتمال اینکه یک عملیات محدود علیه اسرائیل انجام بشه خیلی زیاده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/125809" target="_blank">📅 17:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125808">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
صدا و سیما عملا به یک رسانه زرد تبدیل شده و هرکی از راه میرسه موضع رسمی کشور رو میگه! عملا شده عین میدون انقلاب که مداح‌ها سیاست کلی تعیین میکنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/125808" target="_blank">📅 17:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125807">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
تاکنون قرارگاه خاتم نگفته آماده اجرای وعده ۵ هست و تنها یک کارشناس تو شبکه خبر این حرفو گفته و این کارشناس هم پیشینه متوهمی داره و سالهاست میگه باید جنگ کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/125807" target="_blank">📅 17:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125804">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WViAWsco_IUUil2s9w4_thqySoJQLFcns8SkBzUU-TgNQJHGBGYafZQ_bhECkicP9zNF4S_RvV3VsXTpWNrUMAO83OqXJTeyXrwX9bgAdDxTclzxWT0P6ov89ai0F9uJ76ZfoebVXfnuMaHWR56k7OG5Eni6947LWXP5xtiEst2rs4J0JxK0dBvetagij81P-c-6erqsQFmtVC4qJbJLpCTO8hwYJcYHH-t1fywkU5duK2cOtEqDN_eVN5gUxHNN4Iorp5JnTDw-gmKD2yx7A1eGDF6Rjli3sQquLHqvWBPsy7pHzx0woV3L2IUZqBh1vqSkxLrAdp5sH-pJNua8Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17c821a588.mp4?token=DP1oCwA-4yVWHbKcI0TPWCX9A69OEHHE0o0vlzjhNH84hrR8qWNOF0JY9HS4xlrwEkemD53cnWAh-pxBOZxVdiq7I09ZLNn465udn8diSyMs2VlDD4yq7tynndMCom9sZ_yPe0LGq9r6BoW_Q1ItNmvnMnwC58RI8PmXBwecMdDGQVtm_Vpt87VjRyxAPBdOengkIY9YqcHyHd-rKLA6SNl5DkuKhB9rbGkunjc4bIQ-NEwrAnYz-jPmtgi5ZEa9wjOzhhahE9XmfxHcA14vSLhFkXMwnpMsSINSSAT0m2juvZ6unZFnVNB9akQHiX5bDozq0KhBiq3MD2W6kqPCLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17c821a588.mp4?token=DP1oCwA-4yVWHbKcI0TPWCX9A69OEHHE0o0vlzjhNH84hrR8qWNOF0JY9HS4xlrwEkemD53cnWAh-pxBOZxVdiq7I09ZLNn465udn8diSyMs2VlDD4yq7tynndMCom9sZ_yPe0LGq9r6BoW_Q1ItNmvnMnwC58RI8PmXBwecMdDGQVtm_Vpt87VjRyxAPBdOengkIY9YqcHyHd-rKLA6SNl5DkuKhB9rbGkunjc4bIQ-NEwrAnYz-jPmtgi5ZEa9wjOzhhahE9XmfxHcA14vSLhFkXMwnpMsSINSSAT0m2juvZ6unZFnVNB9akQHiX5bDozq0KhBiq3MD2W6kqPCLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات شدید اسرائیل به صور، لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125804" target="_blank">📅 17:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125803">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
منابع عربی: تحرکات گسترده و انبوه موشکی در ایران مشاهده شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125803" target="_blank">📅 17:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125802">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوری/شبکه خبر: ساعات مهمی در پیش داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125802" target="_blank">📅 17:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125801">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
العربیه:پیش‌نویس قطعنامه علیه ایران در شورای حکام آژانس که ایالات متحده آن را تهیه کرده و پیش از نشست این هفته به دیگر کشورها در شورا ارسال کرده است، ایران را ملزم می‌کند “اطلاعات دقیق” دربارهٔ سایت‌های هسته‌ای بمباران‌شده و ذخایر اورانیوم غنی‌شدهٔ خود ارائه دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125801" target="_blank">📅 17:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125800">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
العربیه: حزب‌الله پس از بمباران حومه جنوبی بیروت شوکه شده زیرا مقامات ایران به رهبران حزب اطمینان داده بودند که اسرائیل این منطقه را بمباران نخواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125800" target="_blank">📅 17:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125799">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5346db6cc.mp4?token=gUR7KYmD_LpeO9x26hI-kYRJxicB4szB2cGY5V7gwtLX1QDXAY_jq5Ljhi972EmxEVvF6KrpB0WclVrj2_A3XfYIVOCn9afAUU_HXluX_27lJYtdskRSN3dZqfUpDcEcREHo7dui74upkX0LQoiDBfXFd7MSmg-X914dvP_PY7SgagarJ6RY3Xclx6VCVQ03s5HfgtLjNxPBWXvrVPtUI-u1Fv0qOG8YA4pRQGCUX2goz8mNl5qWcqsigGx9Q_foAUKZG0c-0_IRc7nTwvJ1_ysw7HKA2hktyu9OyVWCG0Vs5KtOHiqcsocCD-KVBvqSSuDXnVAxyHiN9iYU4dFbJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5346db6cc.mp4?token=gUR7KYmD_LpeO9x26hI-kYRJxicB4szB2cGY5V7gwtLX1QDXAY_jq5Ljhi972EmxEVvF6KrpB0WclVrj2_A3XfYIVOCn9afAUU_HXluX_27lJYtdskRSN3dZqfUpDcEcREHo7dui74upkX0LQoiDBfXFd7MSmg-X914dvP_PY7SgagarJ6RY3Xclx6VCVQ03s5HfgtLjNxPBWXvrVPtUI-u1Fv0qOG8YA4pRQGCUX2goz8mNl5qWcqsigGx9Q_foAUKZG0c-0_IRc7nTwvJ1_ysw7HKA2hktyu9OyVWCG0Vs5KtOHiqcsocCD-KVBvqSSuDXnVAxyHiN9iYU4dFbJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حضور پرتعداد پلیس تیخوانا در اطراف فرودگاه هنگام حضور تیم جمهوری اسلامی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125799" target="_blank">📅 17:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125798">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
خبری تحت عنوان پایان ۶۰روزه ضرب الاجل ترامپ به ایران فیک است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125798" target="_blank">📅 17:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125797">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icpx1ddMR1QPC7H8zvYE_aX4QgEvk9EY_R6BZ_VShEWVGabyaBZZO_V-0dEoFoIDcQkH3K4MGNrJmrtAp1EHG7FFfekyfXuyBqaXPjF-viAHUbHWI0jXXwBxI8USl53jWQsazVxLLvXtHimCM_hLtaGCc9OsPk0-anNRSeknH3Fs_mdVSO0zf57yEhIeDeKBG90LkEvFxXOicR5bYPCt--3tLbFkSLG-OPRN0c5M1fniqXt394ya7hyAFkgUAWXzYLWwqr78eOhp-VpMyn2Vx1eS-lamKrMb82bW3rxxA3liL4RAdxt-rx3sryd_BfVdBvPSIVlokmzq4VxcGCoBLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
👈
نمودار تغییرات قیمت دلار از ابتدای خرداد تا امروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125797" target="_blank">📅 17:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125796">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری/جبهه داخلی اسرائیل: مردم آماده دستورالعمل برای حمله احتمالی باشن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125796" target="_blank">📅 17:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125795">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ به ان بی سی: ایران هنوز با ما توافق نکرده چون برای آن خیلی سخت است‌‌ اما چاره‌ای جز توافق ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125795" target="_blank">📅 17:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125794">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
کانال ۱۴اسرائیل: حمله به بیروت محدود بود و ایران طبق ارزیابی‌ها پاسخ نخواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125794" target="_blank">📅 17:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125793">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c568dbc38.mp4?token=VWkMOFcpbFE5edCiDvszY0EinHUfO-jVuS_pIldxtwNuiue3INzzNAzf2n4BbeK-pQ-ieGQC-aQHxMI4f2l1Z9i3pNDc2kuBkHst0-xD7TiueOinqSA-bmtbod9TQITio8L18K-4zcIaJ3VV4tl6RyW_uMrJl74UZAew5WyzKsCV4Jik6uI261LMBT2JSvzY8lEgX9fX7o9RdsmrM-b8IGGtRSs1V8wBU7J786y2RjmqGJxTWpzqSGNPEAEixuBR-Xs7C88luAYeCjdEo0mz6zsiZEHiFungcxDVCcOuIIpvqlnJx9rsyNz6ginl3PGDR-IkUw6bevADvmSHrxLCXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c568dbc38.mp4?token=VWkMOFcpbFE5edCiDvszY0EinHUfO-jVuS_pIldxtwNuiue3INzzNAzf2n4BbeK-pQ-ieGQC-aQHxMI4f2l1Z9i3pNDc2kuBkHst0-xD7TiueOinqSA-bmtbod9TQITio8L18K-4zcIaJ3VV4tl6RyW_uMrJl74UZAew5WyzKsCV4Jik6uI261LMBT2JSvzY8lEgX9fX7o9RdsmrM-b8IGGtRSs1V8wBU7J786y2RjmqGJxTWpzqSGNPEAEixuBR-Xs7C88luAYeCjdEo0mz6zsiZEHiFungcxDVCcOuIIpvqlnJx9rsyNz6ginl3PGDR-IkUw6bevADvmSHrxLCXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ
: ما یک محاصره برقرار کرده‌ایم و بسیار مؤثر بوده است. دلیلش این است که آن‌ها سعی کردند محاصره ایجاد کنند، و حالا ما آن‌ها را محاصره کرده‌ایم.
آن‌ها محاصره ایجاد کردند، بنابراین ما هم آن‌ها را محاصره کردیم. ما محاصره نهایی را داریم.
من این را جنگ نمی‌دانم، اما اگر کسی بخواهد آن را جنگ تعریف کند، خب شاید بتواند چنین تعریفی داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125793" target="_blank">📅 17:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125792">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ترامپ به ان‌بی‌سی: توافق آتش‌بس با ایران به درخواست برخی افراد بسیار خوب حاصل شد
🔴
ایران ممکن است در طول آتش‌بس، قابلیت‌های نظامی خود را اندکی افزایش داده باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125792" target="_blank">📅 17:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125791">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdVkYeaXaiQoEnbyDwoB9YfSPlGSaUfw5GlYN4xCyJjHtQUyx2cE-a4Sb3meNo1VTLCY1k5_q41idO7MN7ratmIIDcz8hV_rwnX6oWtJrOpl3uRFaEH2VvI4uAjlAQqkguuUGasW_EDuYZbJwEr4hje2aU96ocJFUI7qHZhC0R6n-H5mEm4ZV4_-Lf-0UledCCaUqnaXcKlhG0MIcnlRPLNlSIWHCwh4dedA6ZdBVwY_gW4hGParC4Xg7PTuA4sL83zhzvgUf2Mi2eo5c8Qau_5G_JGbg0qdwY149vsEUVE_M7AuNMSIVIj7tIZDcVJe_Xo0ePzBGyMV_h_mhMYLnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به ان‌بی‌سی: بخشی از چالش در اجرای سریع صلح این است که مستلزم تغییر اساسی در نگرش دیرینه تهران نسبت به ماست.
🔴
ایرانی‌ها قوی هستند و به خودشان افتخار می‌کنند، و کارهایی هست که هرگز انتظار انجامشان را نداشتند، اما مجبور به انجامشان خواهند شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125791" target="_blank">📅 17:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125790">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ترامپ، گفت که او الزامی برای اینکه لبنان بخشی از یک توافق کوتاه‌مدت با ایران باشد، ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125790" target="_blank">📅 17:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125789">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
منابع لبنانی گزارش دادند تعداد کشته و زخمی شدگان حمله هوایی اسرائیل بالاست
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125789" target="_blank">📅 17:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125788">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
دونالد ترامپ به NBC گفت: اگر با ایران به توافق برسیم و روابط دوستانه‌ای داشته باشیم، با همکاری یکدیگر اورانیوم با غنای بالا را جمع‌آوری و نابود خواهیم کرد. تجهیزات متعلق به ما خواهد بود و این مواد را یا در همان محل از بین می‌بریم یا به جای دیگری منتقل کرده و نابود می‌کنیم.
🔴
این کار را با ایران یا بدون ایران انجام خواهیم داد، اما در صورت توافق کسی به سمت ما شلیک نخواهد کرد.
🔴
اما اگر توافقی حاصل نشود، با اقدام نظامی بسیار سخت با آن‌ها برخورد خواهیم کرد. در آن صورت ابتدا آن کار را انجام می‌دهیم و بعد وارد عمل می‌شویم تا از هر جهت امنیت داشته باشیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125788" target="_blank">📅 17:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125787">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ : ما خیلی نزدیکیم، فقط چندتا چیز کوچیک مونده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125787" target="_blank">📅 17:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125786">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ : مجتبی خامنه‌ای به شدت زخمی شده اما بسیار شجاعه
🔴
چون که خیلیا اگه جاش بودن عمرا تو این وضعیت به فکر اینکه با آمریکا چه مذاکره و توافقی داشته باشن اصلا فکر نمیکردن ولی اون براش مهمه پس شجاعه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125786" target="_blank">📅 17:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125785">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c568dbc38.mp4?token=XV2v8MtkHVAm8efXWbsRiaQcfvERj3mZlLrmP4W6xAV9ZU7f_j1NdzIQDqoW6CjLe3V0sTe4aXbl2I1oQgR0-ABWSdd0mUtEutHGdWlaOBvy8wrCmAOg-AriAsLthOK1A81_HNjwUviO_Ck-n9pSeywFpaev-o9nch9Nv4lz1TrzWURBjSYz2eNk4SrxA7_W27g1If-QfpwBwNwoF1IUtPT_3rrgdEW_iq79-XQdeF_b7PnrPeBt9WUDY6UMu2g2CBadSVCI97uX5afPYqO6xqBJMvzstbjfY2ScJKpmmoJXVoCMxKtmUMmNnbNW2Em6gM0CTTEuLWv6amNuMGYgeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c568dbc38.mp4?token=XV2v8MtkHVAm8efXWbsRiaQcfvERj3mZlLrmP4W6xAV9ZU7f_j1NdzIQDqoW6CjLe3V0sTe4aXbl2I1oQgR0-ABWSdd0mUtEutHGdWlaOBvy8wrCmAOg-AriAsLthOK1A81_HNjwUviO_Ck-n9pSeywFpaev-o9nch9Nv4lz1TrzWURBjSYz2eNk4SrxA7_W27g1If-QfpwBwNwoF1IUtPT_3rrgdEW_iq79-XQdeF_b7PnrPeBt9WUDY6UMu2g2CBadSVCI97uX5afPYqO6xqBJMvzstbjfY2ScJKpmmoJXVoCMxKtmUMmNnbNW2Em6gM0CTTEuLWv6amNuMGYgeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما یک محاصره داریم. این بسیار مؤثر بوده است. و دلیل اینکه ما این محاصره را داریم این است که آنها تلاش کردند محاصره کنند، و حالا ما آنها را محاصره کرده‌ایم.
🔴
آنها محاصره‌ای ایجاد کردند، پس ما آنها را محاصره کردیم. ما محاصره نهایی را داریم.
🔴
من این را جنگ نمی‌دانم، اما اگر بخواهید آن را اینگونه تعریف کنید، فکر می‌کنم می‌توانید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125785" target="_blank">📅 17:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125784">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ به ان‌بی‌سی: بخشی از چالش در اجرای سریع صلح این است که مستلزم تغییر اساسی در نگرش دیرینه تهران نسبت به ماست.
🔴
ایرانی‌ها قوی هستند و به خودشان افتخار می‌کنند، و کارهایی هست که هرگز انتظار انجامشان را نداشتند، اما مجبور به انجامشان خواهند شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125784" target="_blank">📅 17:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125783">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e549e15d94.mp4?token=R5MIFA0gbRTr61ajBTJlL-tX0aJN5CIpg6V-SBo8OlJo8BE4mEXbcQIwNl1_7mk6reWbHLskB4DRQ1W8GbXeNXsNnbwTD1Sikm1csEawl2kAImcSv3jXRQZp9bJUyvF-SvwB8sMS2td0ld8J6uMpgzs0KjeYA0BhvhpoZGn7RbKO7jV84xX3ZOgnj3a6yOnAoiXG4zmd5ecNiBkQL89yhwrfKF1ne-H_Sm0nYOZVCtT3fyFJpT_G7tf2ABUNnp17DK69PNVH69xvE1wQElrBPemR8gcrwqo_nV9pR5FuiB-286BTcGRwzA0tqVENQ3-RxCmSWaEMmlSHnX2R2TpA1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e549e15d94.mp4?token=R5MIFA0gbRTr61ajBTJlL-tX0aJN5CIpg6V-SBo8OlJo8BE4mEXbcQIwNl1_7mk6reWbHLskB4DRQ1W8GbXeNXsNnbwTD1Sikm1csEawl2kAImcSv3jXRQZp9bJUyvF-SvwB8sMS2td0ld8J6uMpgzs0KjeYA0BhvhpoZGn7RbKO7jV84xX3ZOgnj3a6yOnAoiXG4zmd5ecNiBkQL89yhwrfKF1ne-H_Sm0nYOZVCtT3fyFJpT_G7tf2ABUNnp17DK69PNVH69xvE1wQElrBPemR8gcrwqo_nV9pR5FuiB-286BTcGRwzA0tqVENQ3-RxCmSWaEMmlSHnX2R2TpA1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ می‌گوید جنگ ایران یک «تمرین نظامی» است و اضافه می‌کند، «این برای ما جنگ بزرگی نیست.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125783" target="_blank">📅 17:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125782">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ: نیروهای آمریکایی را تا رسیدن به توافق نهایی با ایران در منطقه نگه خواهیم داشت
🔴
آمریکایی ها با پایان جنگ احساس آرامش خواهند کرد
🔴
من قصد ندارم نیروهای آمریکایی را حتی در صورت آتش‌بس خارج کنم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125782" target="_blank">📅 16:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125781">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ: نیروهای آمریکایی را تا رسیدن به توافق نهایی با ایران در منطقه نگه خواهیم داشت
🔴
آمریکایی ها با پایان جنگ احساس آرامش خواهند کرد
🔴
من قصد ندارم نیروهای آمریکایی را حتی در صورت آتش‌بس خارج کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/125781" target="_blank">📅 16:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125780">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ترامپ، درباره مجتبی خامنه‌ای :
اگه اون بخواد، منم حاضر به صحبت مستقیم هستم، ولی تا حالا هیچ تماس مستقیمی باهاش نداشتم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/125780" target="_blank">📅 16:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125779">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ در مصاحبه‌ای با برنامه «Meet the Press» شبکه NBC News :
🔴
«اگر به توافقی برسیم و از این به بعد روابط دوستانه‌ای داشته باشیم، همه با هم خواهیم رفت. تجهیزات متعلق به ما خواهد بود. [ذخایر اورانیوم] را خارج می‌کنیم و نابودش می‌کنیم؛ چه در همان محل باشد و چه آن را به محل دیگری منتقل کنیم.»
🔴
او افزود: «و ما یا همراه آن‌ها خواهیم رفت یا بدون آن‌ها. اما اجازه نمی‌دهیم کسی به سمت ما شلیک کند، درست است؟»
🔴
ترامپ مدعی شد: «اگر به توافق نرسیم، آن‌ها را با اقدام نظامی بسیار سخت و شدید از میان خواهیم برد. و در آن صورت، پیش از رفتن ما این کار انجام خواهد شد؛ بنابراین به هر شکلی امنیت خواهیم داشت.»
🔴
ترامپ همچنین ادعا کرد که ایالات متحده می‌تواند این فعالیت‌ها را زیر نظر داشته باشد، زیرا از ظریق «نیروی فضایی» آمریکا، «دوربین‌هایی در فضا» دارد.
🔴
او گفت: «می‌دانید، ما آنجا را زیر نظر داریم؛ کاملاً و از همه جهات. اگر کسی آنجا قدم بزند، حتی اگر خود شما آنجا راه بروید، من می‌توانم نام کوچک شما را روی نشان سینه‌تان بخوانم.»
🔴
ترامپ افزود: «و این‌ها دوربین‌ هایی هستند که در فضا قرار دارند. فناوری واقعاً شگفت‌انگیزی است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/125779" target="_blank">📅 16:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125778">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjqB3oL4KAjGZwmmtLzBpmCivnybC2M1icJG3lIkL5freMbC2--fJ380BQVTg8JAuWjwRu2cziNZS2QFeOxmPN2uakbo4qhFLnLrDeALPrPLDtqHK_oayuy6o0ACy4xYFRmDHngPiDTN0BgvIF4WwG_MBaSbtmea4jwvzAhHOcSrd03cjsJYB_aS8yLBePU8d31hh9D8wxWFZzi6YoZz3pwJIWOEnhViMq0bLRVJZ9dLeQ3_LWfAUOARjRBMqfLulX82C9NBsVISMMLQ1lVv6Wy5lubvZwWyE53DD7ZpxcsspO-merE5qBnx_WYFrZCZ2bBlIVKfqTWzZEYRxkoW0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به ان‌بی‌سی: اگر با ایران به توافقی برای پایان جنگ برسیم، با آنها برای بازیابی و نابودی اورانیوم با درصد غنای بالا اقدام می‌کنیم.
🔴
اگر به توافق نرسیم، به تضعیف ارتش ایران ادامه خواهیم داد تا نیروهایمان بتوانند اورانیوم ایران را با امنیت خارج کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125778" target="_blank">📅 16:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125777">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDC1VPVrm1S12zKICz03E7L7KFGnvsAyIhUzWmK2ymGbQwTpiesid1EkZfijfrrc7W3KaPdMO3NiUgg9f8pmZqDa0ZyeDVfWR_-2OlYAnxY6wq10NhKcEMfonKZpoXgP9MSGDM2fMqcDM1bLRi7czy7OBYOUXwWiDXiOMLkn3eFelESqQiOz-uCZSyOCDNpIcK33sxjSMYQaKaldEWPFzQCAa76VGpLO72L0rSdLedqUVeoopaMUTCUdbSfD9eVPQKLlLYkOJ_-g9MW-pbTRWkRE8zjGUSdFv7ttUuQqqHE5NTpsnB5DpfHlPDCdm5aAMrOBCh2SDD0gfAHN6SezSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کارشناس صداوسیما:  منتظر واکنش قرارگاه خاتم‌الانبیا و حزب‌الله باشید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125777" target="_blank">📅 16:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125776">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
جمهوری اسلامی سقوط خواهد کرد و ملت ایران پیروز خواهند شد.
🤔
حتی یک لحظه هم شک نکنید، از واقعیت نمیشه فرار کرد.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125776" target="_blank">📅 16:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125775">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ترامپ، درباره مکان مجتبی خامنه‌ای :  نمی‌خوام بگم که میدونم اون کجاست یا نه، اما احتمال خوبی وجود داره که بدونم کجاست
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125775" target="_blank">📅 16:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125774">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ترامپ به ان‌بی‌سی: ما و ایران به امضای توافق بسیار نزدیک هستیم، اما من تهران را تحت فشار قرار می‌دهم تا از جاه‌طلبی‌های هسته‌ای خود دست بردارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125774" target="_blank">📅 16:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125773">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISabRe_dWdHsgW42nnOVVExvL3gCgW_9Ve9EZyg3Yarz9-zWpS7_rOv3eybmmWkXCZUMTODwu2NXqicql5ZQPSeu_e4eIV1JdYK1nmV-j4em1tbczwXR-UW8L9gBpKvmO5r-ZPLlfYwx4wln9FQ--n9pT7u2ScjVGKvE2ESaljaf4b3WODsJvIKm8JfNlaUIHzOrLlZyWbmjUIlx0j4TF8hhzAP_XMmecc2FrwLHVtCY3_Z38MDd3_vMMAz-NN34EpPZPfCTax52dn14lEwcYXOPbH5XPB0uRrJHqYp2L7W8MO7CDiTKJefdbJWno1fi-fN_VlpSR7Vt7j61T5JcBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، درباره مکان
مجتبی خامنه‌ای
:  نمی‌خوام بگم که میدونم اون کجاست یا نه، اما احتمال خوبی وجود داره که بدونم کجاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125773" target="_blank">📅 16:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125772">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ترامپ به ان بی سی: هیچ پولی از ایران آزاد نخواهم کرد. تحریم ها هم کاهش پیدا نمی کند
🔴
اگر برای پایان جنگ به توافق برسیم، با ایران برای بازیابی و نابودی اورانیوم غنی‌شده با غنای بالا همکاری خواهیم کرد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125772" target="_blank">📅 16:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125771">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ به ان بی سی: هیچ پولی از ایران آزاد نخواهم کرد. تحریم ها هم کاهش پیدا نمی کند
🔴
اگر برای پایان جنگ به توافق برسیم، با ایران برای بازیابی و نابودی اورانیوم غنی‌شده با غنای بالا همکاری خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125771" target="_blank">📅 16:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125770">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری / ترامپ به ان بی سی: نمی‌خواهم لبنان بخشی از تفاهم با ایران باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125770" target="_blank">📅 16:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125769">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
الحدث: ترامپ از قبل از حمله بیروت مطلع شده بود»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125769" target="_blank">📅 16:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125768">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwh7qVF1SX94qbghPf2gkdHat9YuyJJ1yK7BhiC76pIdsT__pYFZGhvgHGj1Y0kmLOeXH3KGXgbBf_Xa6DCtSXfiHnnEXMVkdisngfY43CMWh14U_LXUSijkjvq3N7Q_actRC6bXB2Kx_B_w0im0txefFtmnCqBKi_YjroWxF5Miap3iTu1PQlzTg8rinD8mj2qt3xAworx1_nN_voWPulARFstOqKV1N5Ca077RKiocM-ZFp4iRaRZbQDDiEMhjlI3ITGmizFD7n_Sbqot36CH4HRjsnEBi2SHrwowJ9F5gliK_kgXe7CrIOdRqtncXiQzYnGo1X1DpqrNnKE_X5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیرحسین ثابتی: راهکار پایان جنگ مذاکره نیست، بلکه قوی‌تر کردن متحدانمان در غزه، لبنان عراق و یمن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125768" target="_blank">📅 16:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125767">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
تخفیف ویژه NETSPIRA VPN فعال شد!  فقط برای 100 نفر اول
⚡️
قیمت هر گیگ فقط 11,000 تومان
🔸
5GB → 55,000
🔸
10GB → 110,000
🔸
25GB → 275,000
🔥
آفر محدود NETSPIRA VPN فقط برای 100 نفر اول  برای ثبت سفارش از طریق بات اقدام کنید
🤖
@NetSpira1bot @NetSpira1bot</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/alonews/125767" target="_blank">📅 16:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125766">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FGjH1fgidfR-xbb1DBOBbLdmyohrd5m-zTAeFy7VwX63yKoP8XsDLNT1rwa55iY411BrK7Dl9AZCzoKRL6rQiGXEEKYGKi_0k4ZRv5ny7U83xBvUzjQFvEvXh57MnKmFc_w8XtinvdWkpmsHFKbLhi8GK9JQSZE_T4_mF1Ev1vj38xkZUiz1aZ4RiWTwIcqNoFXJkFc_acb3a0rpaVy8nr5_9n6b0c6JQN-feRnxf8V3ksf0RYGLbFs1dw-3yjMwM9j9RYvKsH7r4i6OEu8G6hl0d0AlxLA4o_q72ZUJX7znI4vHh37b9Bum4Fe3aN9T3jY0khqt4qA9BLFN7VogPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تخفیف ویژه NETSPIRA VPN فعال شد!
فقط برای 100 نفر اول
⚡️
قیمت هر گیگ فقط 11,000 تومان
🔸
5GB → 55,000
🔸
10GB → 110,000
🔸
25GB → 275,000
🔥
آفر محدود NETSPIRA VPN
فقط برای 100 نفر اول
برای ثبت سفارش از طریق بات اقدام کنید
🤖
@NetSpira1bot
@NetSpira1bot</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/alonews/125766" target="_blank">📅 16:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125765">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
یدیعوت احارونت: اتاق عملیاتی که ارتش اسرائیل در الضاحیه هدف قرار داد، خالی بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125765" target="_blank">📅 16:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125764">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
رسانه‌های عبری: حمله به ضاحیه با ده موشک و با استفاده از دو جنگنده صورت گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125764" target="_blank">📅 16:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125763">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری / خبرنگار الجزیره: یک موشک زمین به هوا به سمت جت‌های جنگنده اسرائیلی در آسمان منطقه نبطیه در جنوب لبنان شلیک شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125763" target="_blank">📅 16:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125762">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
منابع لبنانی گزارش دادند تعداد کشته و زخمی شدگان حمله هوایی اسرائیل بالاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125762" target="_blank">📅 16:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125761">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
در لبنان گزارش می‌شود که شهروندان اکنون در حال تخلیه بیروت هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125761" target="_blank">📅 16:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125760">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل به نقل از یک منبع نظامی: پس از راهنمایی‌های اطلاعاتی، نیروی هوایی به یک هدف با ارزش بالا در حومه جنوبی حمله کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125760" target="_blank">📅 16:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125759">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
کانال ۱۲ سرائیل : اسرائیل قبل از حملِه به بیروت، به آمریکا گفته بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125759" target="_blank">📅 16:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125758">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
محل مورد هدف قرار گرفته در حومه جنوبی شهر است.
🔴
گویا ترور هدفمندی صورت گرفته
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125758" target="_blank">📅 16:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125757">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی : یه حمله محدود تو ضاحیه انجام شده و ارتش اسرائیل هم فکر می‌کنه ایران مستقیم به اسرائیل جواب نمیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125757" target="_blank">📅 16:08 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
