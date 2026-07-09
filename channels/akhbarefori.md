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
<img src="https://cdn4.telesco.pe/file/M1FT8c7QyAppcfNGFAocN76S4whyyv0zNJNkUqbnCB8EDfv_lTkjnybNV7U87FsLeEHzMLqev9P7gd3mUxL-NXox7mHQNvZbv6_4uKcSv5BWeRYoRmeB-ZdUmqgBBS50bOfj1Nldj_RMu-dn61AgwFqGXJVIKnjiLXjXfoYvZQtkHVsBIMuH8PX8Uko8slLtqa-kvhrhcvZ9o9OYBwY6gV2j1W9zDQdIKQ_a3e_MmB_kZmCPnMdZS-qZZssxXIavVBHUM5RgCQJfLUgS0pYOMIYtmZZ7F6OY578STl-l_-o-M7prEerRbXq5bL7xTkd_UXZuMWYW-WUD7QLUzVDVBA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.47M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 04:37:41</div>
<hr>

<div class="tg-post" id="msg-668781">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
منابع خبری عربی از اصابت موشک‌های ایرانی به یک پایگاه آمریکایی را در کویت، و ناتوانی سامانه‌های پدافند هوایی این کشور خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24 · <a href="https://t.me/akhbarefori/668781" target="_blank">📅 04:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668780">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c0e9b164c.mp4?token=Jvy7cMO5pJLKGSU1KHPdJvOTo-RhsltsmAhTuhmw9hYcjHFvKbvIxhbsqlCvj1qMf8_vL85iVL7wGoXfcuY2OJIG6bNph6iSssTV5as3p_F4ww6e6FvXM2A3Uu5lIY1twWe__ff3nOEpkn4S-vgjWKGpxQbaTIWmeXpomkNmCjjcq4JM8LtN8I3JB-c8vyadSuAR75oDb6yF26fQRghmNidMwLWs8D-u2HPiVD0vnfoS76R2HhX6jQR-bFEY2FF2ATbZ6Td7t9uPVGulksYrGpREp1fpa568YFYU4vhVF9rTYZluD6ydwHfRBPlDzTYEcJtxkB-wSiqYwHo499M6ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c0e9b164c.mp4?token=Jvy7cMO5pJLKGSU1KHPdJvOTo-RhsltsmAhTuhmw9hYcjHFvKbvIxhbsqlCvj1qMf8_vL85iVL7wGoXfcuY2OJIG6bNph6iSssTV5as3p_F4ww6e6FvXM2A3Uu5lIY1twWe__ff3nOEpkn4S-vgjWKGpxQbaTIWmeXpomkNmCjjcq4JM8LtN8I3JB-c8vyadSuAR75oDb6yF26fQRghmNidMwLWs8D-u2HPiVD0vnfoS76R2HhX6jQR-bFEY2FF2ATbZ6Td7t9uPVGulksYrGpREp1fpa568YFYU4vhVF9rTYZluD6ydwHfRBPlDzTYEcJtxkB-wSiqYwHo499M6ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز اقامه نماز بر پیکر رهبر شهید ایران در حرم حضرت عباس (ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/akhbarefori/668780" target="_blank">📅 04:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668778">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671c38ae1d.mp4?token=atgQ6pdiKWtQi363OQL-Idpq_hfVYnDuUPWxLyPwfnEkwn0Iw-80A0dlVHblITMWEtUUR3nOIIbql_R3cu3DDLnHRtL5P6ZsQ93Agh5SmhtaGE8Tc7-lH1ci0tPvXj6diBKfwFd691ASt5rj-BuhvSQTSSfoouBYa0Fx9QJT8I7DdSNta5ki4IRIgClxaasNBvDByD38Mc3LSfKRCMIX6sUVxFC7p9-GI8-6B3yqsIlFGyRW01lju6CTi7iH9RddXvgOuRjDKEK25IAh3X504UZGl_GDkczttTPFPPI1ngGp-MHuITMb21emVmbwWijKA4nrpQWHduFmxMWz5cLAaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671c38ae1d.mp4?token=atgQ6pdiKWtQi363OQL-Idpq_hfVYnDuUPWxLyPwfnEkwn0Iw-80A0dlVHblITMWEtUUR3nOIIbql_R3cu3DDLnHRtL5P6ZsQ93Agh5SmhtaGE8Tc7-lH1ci0tPvXj6diBKfwFd691ASt5rj-BuhvSQTSSfoouBYa0Fx9QJT8I7DdSNta5ki4IRIgClxaasNBvDByD38Mc3LSfKRCMIX6sUVxFC7p9-GI8-6B3yqsIlFGyRW01lju6CTi7iH9RddXvgOuRjDKEK25IAh3X504UZGl_GDkczttTPFPPI1ngGp-MHuITMb21emVmbwWijKA4nrpQWHduFmxMWz5cLAaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاش سید احمد الصافی، تولیت آستان حضرت عباس برای رسیدن به نزدیکی پیکر رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/akhbarefori/668778" target="_blank">📅 04:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668777">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ارتش کویت اعلام کرد که سامانه‌های پدافندی در این کشور، هم‌اکنون در حال مقابله با موشک‌ها و پهپادهای مهاجم است
🔹
همزمان منابع عراقی می‌گویند که صدای انفجارها در کویت به حدی شدید است که در برخی مناطق این کشور به گوش می‌رسد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/akhbarefori/668777" target="_blank">📅 04:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668776">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10964947d5.mp4?token=ArbWe4UW6AXsCUqJqOCBA8fidBnoeu6FONVOcAyiMZtgvFhmiOZQVittpxX3J4rQ7f4fv34BXndSVSb7lxZV25NaeUCn1isNGhv3vPxYzfgcrOBuCUw0-l35UblFzRpDG8vYlPLtE-VZLYPXG0PJFCHT7EFI6s-n33swNcivgGLQCdkc4Aai2E7rFAe-VQOf-f6oip6EBPnifhMxBWCMDPfkQQv3ZrXuBis8PQZJdM6pFsp_c1dz1PMqgIAtOuRQNbReaSy8eYBdzRBq7C2MmpVRQTZaSMo9oVTwP_A2vb1V1swoKxL3VGw5oFW-bN2GD9uhPHkNGWA0oXZRtJtFfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10964947d5.mp4?token=ArbWe4UW6AXsCUqJqOCBA8fidBnoeu6FONVOcAyiMZtgvFhmiOZQVittpxX3J4rQ7f4fv34BXndSVSb7lxZV25NaeUCn1isNGhv3vPxYzfgcrOBuCUw0-l35UblFzRpDG8vYlPLtE-VZLYPXG0PJFCHT7EFI6s-n33swNcivgGLQCdkc4Aai2E7rFAe-VQOf-f6oip6EBPnifhMxBWCMDPfkQQv3ZrXuBis8PQZJdM6pFsp_c1dz1PMqgIAtOuRQNbReaSy8eYBdzRBq7C2MmpVRQTZaSMo9oVTwP_A2vb1V1swoKxL3VGw5oFW-bN2GD9uhPHkNGWA0oXZRtJtFfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجارهای بسیار شدید ناوگان پنجم ارتش تروریست آمریکا را در بحرین لرزاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/akhbarefori/668776" target="_blank">📅 04:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668775">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8GHL6IR3OTmgIH8YXHE9VEsNeBQe2AJM5jVrHSNlHYZ0lwsQMQcO62bNImj_MYb0OA3c0q8MY_2qv8ythyUEVQFFpqGbNMR5wCD2URhbmMKaSik6JIQs2UqIsPm-HeROyrm36fsdKVMbD-D0qVNUImi3tWTkF2mS3eLPdJKp2mytEevgfJGBRWmE7gBVW99joxJo7bW8_qIgzSgZqY4923XnIWWQGQsX54QTtC1kRP3VkWEPE2GLHUVkwS_R3iVtiw70MKcKqGrGZPQuTXZDLWYs_Cq3oxdCUsLrD3UnAyUdeNamS8SzY99VbLHOvBpgJPtdyG9a7ipDLyfG3yLmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی مجلس: منتظر سیلی سخت ایرانی‌ها باشید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/akhbarefori/668775" target="_blank">📅 04:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668774">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
وزارت کشور قطر: سطح تهدید امنیتی افزایش یافته است و همه باید به باقی ماندن در منازل و اماکن امن پایبند باشند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/akhbarefori/668774" target="_blank">📅 04:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668773">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693ba173db.mp4?token=GR7VaMwpMEKn4-TU7iPFJzZSGMwJlCcZxVfNzNjI-Kvj84P7WwQ_x8_S7WN8C8KHqMC1srJtgidiwOznrg0v3vLK2bm1l0RSiKh3Z-RhYyudGMBNXwBymCxFeimTQa02aU4MjTZSBl3MVJ0FkgkW12OqX7SyYwL2vd3zc6ilbz2V3IU2rqCQOEIcAq13pGXwwWhFa0gxL-PCsptf8oGsLMZkJqWfskP4AJ2lc-sCHn7rlZI0q--0wzLzf4rjtnn9Yaoh4t3kBxx-nxwX4G4T6pTvIU3T3-MT2LhtApaBCX72AIIAibk8gp93veag-vaaxM-Ju5ETTrU0kG_RzTYs-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693ba173db.mp4?token=GR7VaMwpMEKn4-TU7iPFJzZSGMwJlCcZxVfNzNjI-Kvj84P7WwQ_x8_S7WN8C8KHqMC1srJtgidiwOznrg0v3vLK2bm1l0RSiKh3Z-RhYyudGMBNXwBymCxFeimTQa02aU4MjTZSBl3MVJ0FkgkW12OqX7SyYwL2vd3zc6ilbz2V3IU2rqCQOEIcAq13pGXwwWhFa0gxL-PCsptf8oGsLMZkJqWfskP4AJ2lc-sCHn7rlZI0q--0wzLzf4rjtnn9Yaoh4t3kBxx-nxwX4G4T6pTvIU3T3-MT2LhtApaBCX72AIIAibk8gp93veag-vaaxM-Ju5ETTrU0kG_RzTYs-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استقبال عزاداران عراقی در حرم حضرت عباس(ع) از پیکر رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/akhbarefori/668773" target="_blank">📅 04:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668772">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
وقوع انفجارهای مهیب در کویت
🔹
علاوه بر بحرین و قطر، پایگاه‌های نظامیان تروریست آمریکایی در کویت نیز هدف حملات هوایی ایران قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/akhbarefori/668772" target="_blank">📅 04:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668771">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe0a68bb73.mp4?token=XaNZ4BzUN3C_lMgXnlb8jwgfNgzto8tfmr5P50MqYdcZzyWhknxoOJakzDEJRJEAQIaSqlKE-EGvoVulkyyrDLiiGAWfW3i66bWS8zChJq6nGNZ72WPzLedXhA38PYA7p6QcvJzeR8-euHhapEngEPeyUWicqNX5B4iazMIUrlTuBL0prYq1mIob7E_8GlJWjbQfkaindHvpep__Dnl5XUi8ibQG4iEjOXCE3onv9cjhBwikvexRTzEdn0VyGQnUNH-jg-LrWW2MbA9CJsimkmllJHVhsUSrtm4d8rfOXNlZP3a8MBLrqO39_JwvUoardy23KZmaPE26HxF2ErhQ2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe0a68bb73.mp4?token=XaNZ4BzUN3C_lMgXnlb8jwgfNgzto8tfmr5P50MqYdcZzyWhknxoOJakzDEJRJEAQIaSqlKE-EGvoVulkyyrDLiiGAWfW3i66bWS8zChJq6nGNZ72WPzLedXhA38PYA7p6QcvJzeR8-euHhapEngEPeyUWicqNX5B4iazMIUrlTuBL0prYq1mIob7E_8GlJWjbQfkaindHvpep__Dnl5XUi8ibQG4iEjOXCE3onv9cjhBwikvexRTzEdn0VyGQnUNH-jg-LrWW2MbA9CJsimkmllJHVhsUSrtm4d8rfOXNlZP3a8MBLrqO39_JwvUoardy23KZmaPE26HxF2ErhQ2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فعالیت سامانه‌های پدافندی در بحرین
🔹
برخی منابع تصاویری از شلیک سامانه‌های پدافندی در بحرین برای رهگیری موشک‌های ایرانی منتشر کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/akhbarefori/668771" target="_blank">📅 04:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668770">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در شهر آق قلا استان گلستان
🔹
دشمن تروریست آمریکایی به یک پل راه آهن خارج از شهر آق قلا حمله کرد.
🔹
هنوز هیچ منبع رسمی اعلام نظر نکرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/668770" target="_blank">📅 03:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668769">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3udZO0nbTUkrR-DGf7-f7wFfhC1QDL-aoG2-y0uOyYvkXXwTKdVXMVYd3QdrD7c7-cHr-O-bE6DII2rmKxGvV-jLUulr4wDIyyvA8hMiKo-e7C2BsoBTzo4VrvryuZWvykcvLHeBJjwWwpnICNLnqVq4Oi5UwfRw3LeqkJa-G9GKBvfCAX3g2msU1bKTSWjTim0l6eaCXHfTwBSNzEHVR2mRyYnEtxuxuGVZqFZ1MX4vYFeyk-zjWcQ8SN2CqiqkYvFsuMvEkbEYJyz5ElXGp6IFE7WBMh7kDBDNbUWD3CQK9AUZh8ADer4_-iJNo451Xtw1-2tu9J8TdNsCgAe8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیکر رهبر شهید از حرم امام حسین علیه‌السلام خارج و وارد بین‌الحرمین شد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/668769" target="_blank">📅 03:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668768">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9de25f04d4.mp4?token=sXVfBGxxRS71d6lL5t-g428Lx1CdVlkkZjeZNtT-8BMNodc_dLlnCwvNCkgIqqagOviKk_629Y9L3Bs58mGV1eIsfRyTa4hk3WmxFhwjv0NAJWU95v5MGwPPYe2RYsCRLmWyn4g9mDz7UoXJFMawLj4kg4eQrr0HdFHyLkRTzCNewdMUWguLG1weqk-igHtMN_hjjWsMFdXleD0EAFCtJY1erF5l8AW5fZV9ICLT0i2gEbi9RSkGIdnAwfS3xSnOJkLwH6cD20_6DqtqSiAikFvIJta9n5_q-66fTNXHAIgmlTW6uAYZyrK4y5nlWanyQsUn_DQtNIQcRp4TFyU4ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9de25f04d4.mp4?token=sXVfBGxxRS71d6lL5t-g428Lx1CdVlkkZjeZNtT-8BMNodc_dLlnCwvNCkgIqqagOviKk_629Y9L3Bs58mGV1eIsfRyTa4hk3WmxFhwjv0NAJWU95v5MGwPPYe2RYsCRLmWyn4g9mDz7UoXJFMawLj4kg4eQrr0HdFHyLkRTzCNewdMUWguLG1weqk-igHtMN_hjjWsMFdXleD0EAFCtJY1erF5l8AW5fZV9ICLT0i2gEbi9RSkGIdnAwfS3xSnOJkLwH6cD20_6DqtqSiAikFvIJta9n5_q-66fTNXHAIgmlTW6uAYZyrK4y5nlWanyQsUn_DQtNIQcRp4TFyU4ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتمام نماز بر پیکر رهبر شهید انقلاب به امامت شیخ عبدالمهدی الکربلائی، نماینده آیت‌الله سیستانی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/668768" target="_blank">📅 03:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668767">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d0174baf8.mp4?token=RWtSJ1GcaMpXwoTpJsqjrX89ZTH2FBwryY4VtTjcD6FIYrt1s3sYoAVEYMytPW5jqQF8sRYWz74S6l4iCbtoksHUxLZ8PcTRQxhxFvzRkyHb9CDDEhyasanMZ_XIRtaI0EA0NFEOJyG8Lg5WdB1ty98T0BQW-j-NaTkDSfuq73iS3rjWxQqOUt9kt3CzwCHphERci9PGToUUuSyJNWfMM5_NV24v24flf5XNvsVmGPrizTnl5mTqvYf-44_nKO2RibZSIinK8vqVCkz8J3Esrkler3q0baxKkhZhSkgLCQGy54rPnHf4EPVdRBhxArpxS10ON_CeDfWHg6ce1IEK5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d0174baf8.mp4?token=RWtSJ1GcaMpXwoTpJsqjrX89ZTH2FBwryY4VtTjcD6FIYrt1s3sYoAVEYMytPW5jqQF8sRYWz74S6l4iCbtoksHUxLZ8PcTRQxhxFvzRkyHb9CDDEhyasanMZ_XIRtaI0EA0NFEOJyG8Lg5WdB1ty98T0BQW-j-NaTkDSfuq73iS3rjWxQqOUt9kt3CzwCHphERci9PGToUUuSyJNWfMM5_NV24v24flf5XNvsVmGPrizTnl5mTqvYf-44_nKO2RibZSIinK8vqVCkz8J3Esrkler3q0baxKkhZhSkgLCQGy54rPnHf4EPVdRBhxArpxS10ON_CeDfWHg6ce1IEK5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حضور شیخ قیس الخزعلی دبیرکل جنبش عصائب اهل الحق در مراسم تشییع قائد شهید در کربلای معلی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/668767" target="_blank">📅 03:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668765">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UqG2uFGrjS9ZxpLYoVuqZKSJsa3dPC8w-CiI387n7s23nFtVmDPtPdnxrxLjtFDlRNowuKLmwdVRybBULGEh3V3hI6Tagijwt0ZJorbCG3IcviHnQ4CixBg8BxiDes7LS7LMkXbzkhBXJ5hi3NfIDUF6cIFshMsXHy9mrmV_Tjiz2tZCF71uthFM8K4y99hbDQydnj1BwJ4rLzAp3LgdjOfw0Ikln6SCCF7u5j_Er_rAa5sHqoQA9CppUYzEzTm5IwsVQxHazTQEeplCxUb15EYvujJc8URYEnanj3bxDrG965DaGQLg_W7n1ac6HBxDjSTU6c98gXgilaQucISSGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M6OT4WEckcVBkvxz66mDiatYocdqusXPFjVzdBno3ISmmF8ur_ElTLQ0wXJbNCW8ptS5mCQHzhJMFjtDcVODKjhcxIYiGkkIqrO0aiJOpPHwmyHcFyySLs0ebD5g5GwttwrFVYQNeoZ2-SPGB6vg_1AKSsZv4hqxksSEOgZ8onJafh3w6b-WFr6wQ8tfVJKk-bk7uuGQZEPvNRB3_r_NC77BwKNgs7IXO5I44QbwQB5hqVUK4X56CdH1Pb4k_psc5zu5FWtN0qpnU_Am6e43pSPxMjqSr01GqMRvLEWqcLb4dV-tx72oxpDAcjsD_GKwPt7WsFoCuq3Onwq5oXrRwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از لحظۀ ورود پیکر رهبر شهید انقلاب بر دستان مردم عزادار به حرم مطهر سیدالشهدا(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/668765" target="_blank">📅 03:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668764">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در شهر آق قلا استان گلستان
🔹
دشمن تروریست آمریکایی به یک پل راه آهن خارج از شهر آق قلا حمله کرد.
🔹
هنوز هیچ منبع رسمی اعلام نظر نکرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/668764" target="_blank">📅 03:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668763">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550128c2f0.mp4?token=nQJ9Cmm4iNqw308HkVVl0LFDXZ6hOncDmYjjfKdf00yHinhwkjZAf-M3RCi7IID7AEd70lDQVXh_13WUDWBiYQRUNLZ8DXsg1R8z-G9SUM4rHGLLAdccbTOhSQaeHg4UPU09Rr6IUh_aum3XVcfc_3kM4Asko8_5XOCOqVRrekjyksdzcjQdrNu6JEQ3BP8TbHcwfueX4QDAPIl2D9p56-CJ_bdeOT2b1TlTQ2HiCEaav_IQKSH6UBlLuwMqnUKNdbkuudZYNsmMpVBBaWr_9rFOJ2ehnj6tlDnoEWJ5Y4FY0NSXmYiV_YVLDmYdKmv0Zt4Jswo9l9nC4jt0zj0hk7mnLqhFTa2cjDNQ-wnGDX5n6S86cpGC3SGz-uewEdoCXp61NygwQ853_l6KBi65iQ41bf2PBux60QKwuqxad0rgTKsovCrtSWEMirbkEVO5xTtFAWd6swGM_mvO4Kf00KSR3XmngKjM9WkP6leniA0aMWLLXaktgypafOgykF4gt_biIOiu_W0vZxfrzfi8M5iQW3DndIzPvb0pICtOaPDX-C52LaTMH-U-nC4l8P9OZnuY9D0fKHT9TettTSsTUiY2dYQeRHYxjCj8s07djy48n_I4yEqq6nZYvCLHKqfL4NtOmC06jy3zISUra4fVPhaoTuNaJ21mChsveTCwyyU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550128c2f0.mp4?token=nQJ9Cmm4iNqw308HkVVl0LFDXZ6hOncDmYjjfKdf00yHinhwkjZAf-M3RCi7IID7AEd70lDQVXh_13WUDWBiYQRUNLZ8DXsg1R8z-G9SUM4rHGLLAdccbTOhSQaeHg4UPU09Rr6IUh_aum3XVcfc_3kM4Asko8_5XOCOqVRrekjyksdzcjQdrNu6JEQ3BP8TbHcwfueX4QDAPIl2D9p56-CJ_bdeOT2b1TlTQ2HiCEaav_IQKSH6UBlLuwMqnUKNdbkuudZYNsmMpVBBaWr_9rFOJ2ehnj6tlDnoEWJ5Y4FY0NSXmYiV_YVLDmYdKmv0Zt4Jswo9l9nC4jt0zj0hk7mnLqhFTa2cjDNQ-wnGDX5n6S86cpGC3SGz-uewEdoCXp61NygwQ853_l6KBi65iQ41bf2PBux60QKwuqxad0rgTKsovCrtSWEMirbkEVO5xTtFAWd6swGM_mvO4Kf00KSR3XmngKjM9WkP6leniA0aMWLLXaktgypafOgykF4gt_biIOiu_W0vZxfrzfi8M5iQW3DndIzPvb0pICtOaPDX-C52LaTMH-U-nC4l8P9OZnuY9D0fKHT9TettTSsTUiY2dYQeRHYxjCj8s07djy48n_I4yEqq6nZYvCLHKqfL4NtOmC06jy3zISUra4fVPhaoTuNaJ21mChsveTCwyyU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی دیگر از ورود پیکر رهبر شهید انقلاب به حرم مطهر امام حسین علیه‌السلام
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/668763" target="_blank">📅 03:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668762">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
فوری/ نامه رسمی ایران به شورای امنیت درباره تجاوزات آمریکا
🔹
ایران درباره تجاوزات رژیم تروریست آمریکا برای رئیس شورای امنیت و دبیرکل سازمان ملل نامه‌های جداگانه ارسال کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/668762" target="_blank">📅 02:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668761">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7o6dLSqbK5V9V_ypx1s0l1lt6Z42_uKNLKC_0d071OjP0Hcq9zZNF1aXZnm0t2VQEdDsN1VbkWTQf7fbbE5zdNf9s7C2bvMFK9XgNfNDvmDozBzgy05iLV3tXZT5XNX0oxbAJU6H2dwK3Ni225JYLspWGi7UC07ufF0NfCzgRlGC3aps302zMxT00VECOOJ8Ms6XHmrObCxZKI8vLC3usp7zv5sk7dp0KJ7mrD95h8FEsKVdo4JMMzTlEdhA89T88eYKH3viIQP2V7QB82771po9ipEYiU0VPzH5DR57PcmHDGmxITkcoqqFskq5ZYYSBRUfYw1YFfg7NeZi6g5aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری هوایی از جمعیت عزاداران در مراسم تشییع پیکر آقای شهید ایران در کربلا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/668761" target="_blank">📅 02:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668759">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTrW8xgGJZXmlZ-M_DbFLVsrD02OkwH0DMgnxq4P8yplnHoivxkUH5aOAtzWRgghiWZ9y0xSaU6kqjrnQq93nha8O8WxFN5nUCr2228MmJ2J7OFcBjcr8iV3OlZG-bs1houqZd5VwaNhYrASxnEdF_ykz1tfuQ_KTZtTb6hX92f1gQbD8XcxLpK577NWnK114UQlizWVNXMFMNhLTd65gFuaeuEDqGfbcHkSvL3Q_jEXGhAU9XrAhI-rIo5ZUZPXGiCgbLLBsEz2EwHnHGGpCSmrKu94x8UxP44yCt4d6yohK-Da_tb6cQF0uOnSOGgRLTthc2GDAI7Nx5dXQUtWoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ما ترامپ را خواهیم کشت
...
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/668759" target="_blank">📅 02:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668758">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb3e36225.mp4?token=csFQTuZ01eheCxaCunDoHl4VQflNjwVs5E1kKMaUsw_RsT84iUimXfMly_hUF-OAy_36J7GsH17F6RGWKXIsD8k7H8DNEuPqJV3ZnW1odaWxMtICJq6j8ESf3f3-E1f5yyx1pZ6gFWS__2KrU-MVNssj53l6CyZeJhXphO8_eeymv4kq7s9NGX2QP_fJMWfrDdlL0450WNI9xqJwSu5x4ID8XqZSXaWXXEUE7ufY2YpZwvn2LTHWBZTKXnsC0nTh3fJfkFy-W3Xt_tdpjxWr_BUDH922w1KeoDXnsRT5Q2zPpt0GXQXFMX1z0X1kKAongWVBTcdaesWYxg96M0yo-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb3e36225.mp4?token=csFQTuZ01eheCxaCunDoHl4VQflNjwVs5E1kKMaUsw_RsT84iUimXfMly_hUF-OAy_36J7GsH17F6RGWKXIsD8k7H8DNEuPqJV3ZnW1odaWxMtICJq6j8ESf3f3-E1f5yyx1pZ6gFWS__2KrU-MVNssj53l6CyZeJhXphO8_eeymv4kq7s9NGX2QP_fJMWfrDdlL0450WNI9xqJwSu5x4ID8XqZSXaWXXEUE7ufY2YpZwvn2LTHWBZTKXnsC0nTh3fJfkFy-W3Xt_tdpjxWr_BUDH922w1KeoDXnsRT5Q2zPpt0GXQXFMX1z0X1kKAongWVBTcdaesWYxg96M0yo-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای مردم عزادار در جوار پیکر مطهر رهبر شهید انقلاب در نزدیکی بین‌الحرمین
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/668758" target="_blank">📅 02:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668757">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
حال‌وهوای مردم عزادار در جوار پیکر مطهر رهبر شهید انقلاب در نزدیکی بین‌الحرمین
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/668757" target="_blank">📅 02:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668756">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ادعای شیطان زرد درباره ایران: ما همین الان ضربه بسیار سختی به آن‌ها زدیم
🔹
می‌گویم که نسبت ضربه ما ۲۰ به ۱ بود.
هر بار که آن‌ها به ما ضربه بزنند، ما ۲۰ برابر به آن‌ها ضربه خواهیم زد
🔹
وقتی آن‌ها حمله کنند، ما با شدت بسیار بیشتری پاسخ خواهیم داد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/668756" target="_blank">📅 02:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668753">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ubfk4hFIQCpjjvD7kPg60BP6qV2_8lL2TNXnnIPNShAIxrk4XBJmVec1-MEV-BoehGZ0RbcmiKt5GJDOmPalhHMpq2HiTYm3EpE-NQy34gxmr4bp90gq_PUGrXXFl6LAMIIz43hGLWY3Vee7K_u0yBEpy3EpMxaBk59NTRFnaR6CVD2pcqVysVrDrphyNPQcShd4XW3fEDCfZeTwByw3YY5oetyclQtI7yT8aFsFCL4N2QsK1T5tnxXvXl2Z6C7gSKJMXW6TtuVLRhnKzeWkowrw1nR3Hj7ym07iWmTNT_zCQZzS4DdYpdTMDSpkQvyi9Ux9nHkF-_F1UuVitB4oVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uW7RUFgaphgSDyUwly8NO4pX4lSksDMuk6Yve-rrDWSkOVII-_ova2V27ZYz6jd4I1NCRXkhdEn20CGWyQI0NDlUbb8Kn2sXW0KNXVNhqljW0avpiTJ9HlfhuskLZYTA6JToicctxmR8ktRocClv-qx8mawEzKAtCT2Fu7MwRSvAQUMKp4WXuL4zhR0_yjPfMOIaRBFAIlYp8Xe9UP6k3ytf6QGnUwzFHGfK4z3p_SE5xpCuWTbVGPF22IKPJkZfqoUy3svDHjTGxiZieW0_PkVz5VcYEHpfiMupDs7wmL5h8LG1xa8dCuz35k38rKvOEG14wdPfwof8piXI9crCSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K4QzUsHS6yCI2SSxQyWy_3jPhG6iDLrGzRmhSUILCeXofGDIwkSUtcsHhiVLArLBNZPVphz54u5CHhGlwc5s_MeBOZPIH47lbujizcev8YEHym41a_4WjEwQ-2GGGqJtW0lPnORCOhIBof2XLhknbmHKm5Vxl9yAvSJ3JUGoOM_e4LMCEntjg7xlLP--vdLY0OoGHoPJZyjkZUOPPEOeFKtW7Z3H2P3Ck1tCt7o-J92zWZgq8OgT18xZmVc1Bk-FPX-g2pmGM1w9y4NkukhACjMyrJLL16vaN0T0H5jjsXuphSZylwD-a2stid7rzISWq5JCE0XFtAcVQfNJrosNKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
انبوه زائران در بین‌الحرمین در انتظار رسیدن پیکر
رهبر
آزادی خواهان جهان
انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/668753" target="_blank">📅 02:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668752">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
نگرانی اسرائیل از انتقام‌گیری ایران از تجاوز آمریکا
🔹
رسانه‌های صهیونیستی هشدار دادند که احتمال دارد ایران و حزب‌الله در عملیاتی مشترک، به سمت فلسطین اشغالی موشک پرتاب کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/668752" target="_blank">📅 02:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668751">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65366aac01.mp4?token=CP1TnVO5xvOugxH5Ph71gCphMDPyBxF6Yy087ApeuQ8exxXH0k1nrrMB0avo6zKZqR-p1-f62zRsQt3BNIfwPSPwfozu3lpQYFM_SHtF62Oui9DalY4WTsKEYlkjIq3g2vB6E1JiP3gViGL9MW6XXVMsVQ21nT3WtMn05KHaCBWhEBly7FDOMkn6SUt-QjmBUFiJvbuZ76c3_aK8L0U6BzmM7HBI34BHoZveeXb_nBfBgnyFHq1oxPcyM2dzUisOUFAQqd7OGj2y4IFhjEt2P67VIdXGoXgdevg3FaP-RwAiQ7W831K5ipSI59IGLBJ6RcdU2ugQ3KjnFG5-XK9yQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65366aac01.mp4?token=CP1TnVO5xvOugxH5Ph71gCphMDPyBxF6Yy087ApeuQ8exxXH0k1nrrMB0avo6zKZqR-p1-f62zRsQt3BNIfwPSPwfozu3lpQYFM_SHtF62Oui9DalY4WTsKEYlkjIq3g2vB6E1JiP3gViGL9MW6XXVMsVQ21nT3WtMn05KHaCBWhEBly7FDOMkn6SUt-QjmBUFiJvbuZ76c3_aK8L0U6BzmM7HBI34BHoZveeXb_nBfBgnyFHq1oxPcyM2dzUisOUFAQqd7OGj2y4IFhjEt2P67VIdXGoXgdevg3FaP-RwAiQ7W831K5ipSI59IGLBJ6RcdU2ugQ3KjnFG5-XK9yQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎓
فرزند شما فقط برای امتحان آماده می‌شود یا برای آینده؟
🌟
دبیرستان دخترانه هوشمند مدبّران (بارسا)
🏫
✨
در مدبّران، دانش‌آموزان علاوه بر موفقیت تحصیلی، مهارت‌های زندگی، اعتمادبه‌نفس ، تفکر خلاق و آمادگی برای دنیای آینده را نیز می‌آموزند.
🚨
ثبت‌نام آزمون ورودی آغاز شد
🚀
📩
برای دریافت اطلاعات و ثبت‌نام:
🆔
@modaberanschools_bot
📩
یا عدد
۴۴
را به سامانه پیامکی
09982003159
ارسال کنید.
📲
❗️
آشنایی با روش‌های نوین آموزش و موفقیت تحصیلی
👇
🆔
@barsaschools
📍
تهران</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668751" target="_blank">📅 02:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668750">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d2bcb646e.mp4?token=WZsQwwbRP3VrtIbuJd9_4j6ciSgBH8GGwwQlMcgg44kPcgGZpW6T3cpaXaTJKmDhMD1xIjMOqGLorYk62wuRtsX5PwRGth2cNpsCwoZxAZqc9aJa_ABLihB6271xOLsik72v0R0VKJVfsWZ8XgYFNzOjd-6ZFXelaUoOtYjEJPL9q9ihMFnZkZaqpqpnR_4lMCAylAmUZaE7Dhx7vtEKAESMK74N-_euY0cBWK9Fb450IRDLp2gwMr5w1v2ERTh30DCdThperC8pQGrCArhQY34_fmHIv_QTUC5128zXebCbCFQJ90o-lwx963ahFahSXIW2Q7bQlZottIG61D8xAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d2bcb646e.mp4?token=WZsQwwbRP3VrtIbuJd9_4j6ciSgBH8GGwwQlMcgg44kPcgGZpW6T3cpaXaTJKmDhMD1xIjMOqGLorYk62wuRtsX5PwRGth2cNpsCwoZxAZqc9aJa_ABLihB6271xOLsik72v0R0VKJVfsWZ8XgYFNzOjd-6ZFXelaUoOtYjEJPL9q9ihMFnZkZaqpqpnR_4lMCAylAmUZaE7Dhx7vtEKAESMK74N-_euY0cBWK9Fb450IRDLp2gwMr5w1v2ERTh30DCdThperC8pQGrCArhQY34_fmHIv_QTUC5128zXebCbCFQJ90o-lwx963ahFahSXIW2Q7bQlZottIG61D8xAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیابان امام‌رضا(ع) مشهد، ساعت‌ها پیش از آغاز مراسم تشییع پیکر رهبر آزادی خواهان جهان
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/668750" target="_blank">📅 01:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668749">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
حمله آمریکا به برج مراقبت کنترل ترافیک دریایی منطقه آزاد چابهار  مدیرعامل سازمان منطقه آزاد چابهار:
🔹
در جریان حمله ساعتی پیش آمریکا به چابهار، برج مراقبت کنترل ترافیک دریایی منطقه آزاد چابهار هدف قرار گرفت و آسیب دید. در این حملات یکی از انبارهای منطقه…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668749" target="_blank">📅 01:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668748">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d748eb74f9.mp4?token=rpQVNegCCFpV9C6oC7ZLlF_uRnE5LYfhQfB7YJf7UkHNbftVzTr-g6OfKwJt-aYrwrpW_UqV-yXmbALXwoGIBQfZ78Mocz1AAmyX_LJlWkV74A74HqzgWni7mKWHHUdCLxgEvw-AGLH6CrgTTAmzXrnhxjXa5PSiq5cyzb5ERj1BYHrKz-3PDk2_fgegIEAOxt6VCoorcov_BgBRfm4u9e-pdYUSCc6_eA_cZOfC8lFoiiS3glo-v_QRJX9Re5oECfqU7DsoAjdTtTBEwzAdMpAawqABNwz2LMXeTSNIveu-vp7D-QAM61TDl_Or0bVy7auI5PxNzCAkuCZEx4nobw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d748eb74f9.mp4?token=rpQVNegCCFpV9C6oC7ZLlF_uRnE5LYfhQfB7YJf7UkHNbftVzTr-g6OfKwJt-aYrwrpW_UqV-yXmbALXwoGIBQfZ78Mocz1AAmyX_LJlWkV74A74HqzgWni7mKWHHUdCLxgEvw-AGLH6CrgTTAmzXrnhxjXa5PSiq5cyzb5ERj1BYHrKz-3PDk2_fgegIEAOxt6VCoorcov_BgBRfm4u9e-pdYUSCc6_eA_cZOfC8lFoiiS3glo-v_QRJX9Re5oECfqU7DsoAjdTtTBEwzAdMpAawqABNwz2LMXeTSNIveu-vp7D-QAM61TDl_Or0bVy7auI5PxNzCAkuCZEx4nobw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشییع نمادین آقای شهید ایران در بحرین
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/668748" target="_blank">📅 01:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668747">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4481c2c676.mp4?token=vXtUo_fAilhvTs-1OCeR18cNsQGAj5jrOG4qTqc9IHA_l_QajJVqIOSyNC8cU-QEeS3-8xfaNsU6on0aTvb1cFcNAGJ-pizj8xn5Jf9ZlcEw5AGtjfDUVHLklRb7JNKhws93DH2GfqU2SZaXQyqTcFi67UfzuZqO1flquh1z8Mm9mZTngkp0EkF33ztK1NVVschEbn8uAJGCTc46kLqVPGfe7-a4y857PLH4HaiLUI8hKM1fGwnuPCvmJClBKW2ogCoStkKodkZEs30mGVP0M8LrOyeo3AwvJYS8itQd-ZTotjH39P7BFppYH4yXEL1V_nJFMCdTognbN4Hbmmxb_kxak-TEivY6r1GH7CLNdDfg1Os0gux9DFwVH7Q9_iXCa1fntcCEeUPbZIkMmn8AXVvGzFNZOStBBSSxImhhb8TtrT2IaFSn4aQt2WPd8SQ1sLos1ctpbvbq0DLCgBHXX1W8fF0C7rurZsoJHII33ODBPLA0HntNst1g5nSf7LEudal_mZeEGg3Z8AX4_-CKjw5oe1L9T3OpNLdvhsAC2RCOQr2sClPfx5Sx_Rh7lIIJJfh1W3c_VsLu2Ljn0LDO55QRFrENoH8veQ4cKkwoxX2hAkNY3ceB-xROhHxSaBZzLVN2eTlM2uA-L1hp16UtNIygb_khEycyjVZhSi1GFvI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4481c2c676.mp4?token=vXtUo_fAilhvTs-1OCeR18cNsQGAj5jrOG4qTqc9IHA_l_QajJVqIOSyNC8cU-QEeS3-8xfaNsU6on0aTvb1cFcNAGJ-pizj8xn5Jf9ZlcEw5AGtjfDUVHLklRb7JNKhws93DH2GfqU2SZaXQyqTcFi67UfzuZqO1flquh1z8Mm9mZTngkp0EkF33ztK1NVVschEbn8uAJGCTc46kLqVPGfe7-a4y857PLH4HaiLUI8hKM1fGwnuPCvmJClBKW2ogCoStkKodkZEs30mGVP0M8LrOyeo3AwvJYS8itQd-ZTotjH39P7BFppYH4yXEL1V_nJFMCdTognbN4Hbmmxb_kxak-TEivY6r1GH7CLNdDfg1Os0gux9DFwVH7Q9_iXCa1fntcCEeUPbZIkMmn8AXVvGzFNZOStBBSSxImhhb8TtrT2IaFSn4aQt2WPd8SQ1sLos1ctpbvbq0DLCgBHXX1W8fF0C7rurZsoJHII33ODBPLA0HntNst1g5nSf7LEudal_mZeEGg3Z8AX4_-CKjw5oe1L9T3OpNLdvhsAC2RCOQr2sClPfx5Sx_Rh7lIIJJfh1W3c_VsLu2Ljn0LDO55QRFrENoH8veQ4cKkwoxX2hAkNY3ceB-xROhHxSaBZzLVN2eTlM2uA-L1hp16UtNIygb_khEycyjVZhSi1GFvI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین قاب مشترک از پیکر رهبر آزادی خواهان جهان با گنبد حرم مطهر حضرت ابالفضل العباس علیه‌السلام در کربلا هم اکنون
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668747" target="_blank">📅 01:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668746">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOXh2Rb4kZE7q5RiFhfGkG3bYA_95SNYPZzf4uj_AFPL6RVv7YV3GZRED2MX8C-QKdjZxFR4H_-roX1EPiwbYPY8TuHfgrgYwHSG5ikgfWLBjH0V22qTT5nY4qf32F3p0i6rOTwjjSj3rv0jBWzKHHnNamKuf6SQkEUQuN3jCqWsHu-w3cr4NlEksfLcYMAbSj_hp5c9ZOHLHE1fw0Pl3pxfK5hE2nnyvJd0oVOJjFBW_MZyzIZ_X7gPNAxVleLWLENPeV0OfX8N0K15qfMIT_8lMF5kfAJmMglHM0LQkEA3GyWlwyFjlMoSAZLqF2N0q-toKJ-WvJVYQbvQ-joICw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماره مزايده در سامانه ستاد:5005095004000004
موضوع مزايده: بهره برداري تعدادي از بازارهاي ميوه و تره بار سطح شهر مشهد مقدس مطابق ليست هاي مندرج در اسناد مزايده به اشخاص حقيقي و حقوقي واجد شرايط به صورت اجاره .
مدت و مبلغ بهره برداري: به شرح اسناد مزايده
جهت اطلاعات تكميلي به سامانه تداركات الكترونيكي دولت ( ستاد ) به نشاني
www.setadiran.ir
و همچنين جهت اطلاع در روزنامه رسمي به نشاني
www.rrk.ir
مراجعه نمائيد.
#مزایده
#مزایده_عمومی
#مزایده_شهرداری
#سامانه_ستاد
#سرمایه_گذاری_مشهد
#فروشگاه_شهرما
#شهرداری_مشهد
#بازار_میوه_و_تره_بار
#سازمان_ساماندهی_مشاغل_شهری
#واگذاری_فروشگاه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668746" target="_blank">📅 01:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668745">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSAZop9eBdFBbgMiB9ntW0_UzI3y8eV6Elu2MU4czPbBIWTAhxRikFuFIsEEhhgcGRs-WWtKSo8g_kf3dxyoxBLCZkYfmyFPxg2R1xOAp8VIMDwyNuKqq7bXIqy37rpLHrSqO45_DaoRO37queaSqbmfCVDTkAavp2jfri47UmQhCgSU3Gc1v4074HbnQ8DEYeOK_VbQ0MK4kukQuaJgXQFjU3TKZSGZmixIrdKfeeJ_Slv7bI75rffmVp2mWU-Tf5LLA0cKfTXS2x8_GHXHd4L2FpC8nTW7My9k-xWnYNbTf5u5yY8h5YBkW3VB9zedSd-LN9sbd7_Oa7nOR84ZYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود بر ملت و دولت نجیب عراق؛ شما معنای واقعی برادری را به جهان نشان دادید. صمیمانه از شما تشکر می‌کنیم.
تحيةً للشعب العراقي الأصيل وحكومته الكريمة؛ لقد أثبتم للعالم المعنى الحقيقي للأخوّة. نتقدّم إليكم بخالص الشكر والامتنان
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668745" target="_blank">📅 01:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668744">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
پایداری برق در اکثر نقاط شهر چابهار
روابط عمومی شرکت برق چابهار در اطلاعیه ای:
🔹
سه خط برق در شهر چابهار که براثر موج انفجار قطع شده بود، دقایقی قبل دو مورد از این سه خط برق دار شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/668744" target="_blank">📅 01:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668743">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53d112d822.mp4?token=qwkkvxyuOk3IWEvJsgEhJb7oy2gghowbXNMijVbGZvoen-HySxGq3NM-v4EwbWgBZPDMhYvnCLszWEHo_COl8t09JvNjydcefmbKYCCylG8KiVY7LNbXPSzoXqmcJ1ke3pIQm4S0KnhAHx0oZDrjQk1ShdFnoNfH39va-3JjLxGR9e4-jIbump8w-CR6IRcT94km4fvNcblIEhqlQrpPNElI6QG5CeitoF6lQT8--9USy2pxwrEACWhoQlLfsIwvOgANvc2pnbCl7VqBxvyE3Wn9u6FHgD7CBxeXfZk2BJSukcNo2mlBBF391wpJyAVn9xJxK4uLPd-4Ihi2AJ7celA9DmqwAbkqww5kIb95jnMG9Vscpchg74CzgKdRgPUdE9EYOI4O7rNTliid5qq17ThTPQpGtO8UnWrdZZs9a5hh54fUo5hQjBGkekv2sLPjGdD2JYFI9DSrB6RK4yOMR_kb0Yb1KFzRY9At0YLlzh_Auh8CbzYKQzygH-pQAshd3GhNpCezY6_QRrFVOR3igc-7ZJ1buMbjHIBur4EoIumrrcF7FycmTlzhroNLK6DwPqnwkVEnfCjUZuITrk12TPY384PzWYUBkm0cf1M97FvQ214mDmIMB8Xv59s3NVNiAVb62yXVcV2m7jsyPOdiZBAlA4xSuttSURySRJ8CftY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53d112d822.mp4?token=qwkkvxyuOk3IWEvJsgEhJb7oy2gghowbXNMijVbGZvoen-HySxGq3NM-v4EwbWgBZPDMhYvnCLszWEHo_COl8t09JvNjydcefmbKYCCylG8KiVY7LNbXPSzoXqmcJ1ke3pIQm4S0KnhAHx0oZDrjQk1ShdFnoNfH39va-3JjLxGR9e4-jIbump8w-CR6IRcT94km4fvNcblIEhqlQrpPNElI6QG5CeitoF6lQT8--9USy2pxwrEACWhoQlLfsIwvOgANvc2pnbCl7VqBxvyE3Wn9u6FHgD7CBxeXfZk2BJSukcNo2mlBBF391wpJyAVn9xJxK4uLPd-4Ihi2AJ7celA9DmqwAbkqww5kIb95jnMG9Vscpchg74CzgKdRgPUdE9EYOI4O7rNTliid5qq17ThTPQpGtO8UnWrdZZs9a5hh54fUo5hQjBGkekv2sLPjGdD2JYFI9DSrB6RK4yOMR_kb0Yb1KFzRY9At0YLlzh_Auh8CbzYKQzygH-pQAshd3GhNpCezY6_QRrFVOR3igc-7ZJ1buMbjHIBur4EoIumrrcF7FycmTlzhroNLK6DwPqnwkVEnfCjUZuITrk12TPY384PzWYUBkm0cf1M97FvQ214mDmIMB8Xv59s3NVNiAVb62yXVcV2m7jsyPOdiZBAlA4xSuttSURySRJ8CftY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری بی‌نظیر از مهمان نوازی مردم عراق از پیکر رهبر آزادی‌خواهان جهان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/668743" target="_blank">📅 01:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668742">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
حمله آمریکا به برج مراقبت کنترل ترافیک دریایی منطقه آزاد چابهار
مدیرعامل سازمان منطقه آزاد چابهار:
🔹
در جریان حمله ساعتی پیش آمریکا به چابهار، برج مراقبت کنترل ترافیک دریایی منطقه آزاد چابهار هدف قرار گرفت و آسیب دید. در این حملات یکی از انبارهای منطقه آزاد چابهار نیز هدف قرار گرفته است. در حال حاضر خدمات‌رسانی و اجرای عملیات تخلیه خودروهای موجود در انبارها تداوم دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/668742" target="_blank">📅 01:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668741">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
صدای چند انفجار در ایرانشهر شنیده شد
🔹
دقایقی قبل، صدای چند انفجار در شمال شرق شهر ایرانشهر شنیده شد. هنوز ماهیت این صداها مشخص نیست./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/668741" target="_blank">📅 01:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668740">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
یک مقام آمریکایی به سی‌ان‌ان گفته است که آتش‌بس با ایران «دست‌کم به‌طور موقت متوقف شده» است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/668740" target="_blank">📅 01:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668737">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WDWj6FpsiyNdOUi6Y_ultSwudZzBlSpmQqLxbmXFXUE-RGK56NBhc2Qzh-T-o9YCK-jllVviKxdL0PGzT2E73_3nlyBJIeLpM9B518Q9xuFOJU0OUgBsBd8nboY61LiYxEaa89a0MZiZ2mqCeOEV9u9F9Rg_nZ8GZ5v7bFTKZWZ_J8xbktVP32cHxg2Ymfzozg6QYpCx2KiqY2B32kiGRURoZ2l1ZC-DT63gKpuRaW_0fcEDTqNA6bbEy-OggwWwc2-Hmv0ZjxPKq2bs_14pzZkI7BmQ28yb09WefNYd-dv2d2MyNtt4tDkeYzNawP0Pk3Rir6ioMZw7kwdlxwo6Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQNIK4WFB7uQMnZ0uEYbqImpFOS--X1vA22HJ4by0G2TpUHYKxO2wgT677t7n7jiItLOz_hdcTxqPGD3CYK14p3orqpN20NU560WleKZGGaoRfCHIsYEcYjPLzGn-UgHnYVKjGdnKjp5F18U1YRuwvXyIlxiDlBNDoqs3qkrfxlF9PYvXDnQ-7x-YGqZNdTV5AlubcWa-npyDbixmB0vZBvhAaSrzFn26OkbapLEMftquOuyU6hyNiQS9bqMxY2rsPKOhXTxjOeqsvFV4hbCewz_kz0pRW6oLWGLvchkBSaSE7n4chQWFle5nhDqcai5LIP7A9uzmL3J38icFcbbJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDbqa06x_0-RBuYmJ84JIha0sVKOvg3-8sDilkZdnCtEAxxMFisCJxEVxDXAgr-qwPxo47J34DbrdhJp4g2Xr7R_ml8um2xKzv6YpckoqyIrSJGjL43cR1n4sGtiAYG5o5oJ4xjf1Fa-8awqilwpXQ0udtbHlka_lYSMjVwIY7AXwWvgpN3WSHuXpvuLE104WUPa5n9m0NOpLHtAJ42IcFgB0nKwimIqizzGn5XWLaWhxjCpZ-eITso2_WnLkEnvWW9kTJMsP7pNMg0zY2J7t8wUpAJt0FOtaA20iP7zAq-LvPNRJS6j70e6lZobRDl0OsWYwubZKa52xsOBvZtk-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از پیکر رهبر آزادی‌خواهان جهان در شارع العباس کربلا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/668737" target="_blank">📅 01:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668736">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
شبکه العربیه، در گزارشی ادعا کرد بحرین امشب در حملات به ایران شرکت داشته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/668736" target="_blank">📅 01:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668735">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxVWVJR3BfvU4EgWTuk-EL-chgn6_lDgDzqjH2LLFVZDEoXrfYE24juUu0Uw6dIgjl3igpMuHxnz1Q1LtyDb5WGCGNAzQKqWj9ZX9hwRTW4SGhZaMeduIPVZHNX9c0ey0tyPIAmZetnBv99mNPzfeDs0L27dsANww6-AqxfRnKu7eVTfHTdWJhE2EPw8Iac5bjFk0kluyAAiz1XoNxmCGvM5TMP868b8yKmDUcKx2_Fc3MUFE1u0G25sd4pMHyTs9sOzbzMjr_lVDyM2UD1E-S1S1S1C1TNkORmnjFx1yxEw-mf40aR69BGiM_53fEABG2dDDzrKm_TLA1YUrSPdPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید خوک هار: این به تلافی بمباران دیروز کشتی‌ها توسط ایران است. اگر دوباره اتفاق بیفتد، حملات خیلی بدتر خواهد شد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/668735" target="_blank">📅 01:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668734">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
ادعای العربیه به نقل از یک مقام آمریکایی: ممکن است به سمت حملات تهاجمی علیه ایران حرکت کنیم
🔹
نیروی دریایی ما در حملات امشب علیه ایران مشارکت داشته است. ممکن است در زمان دیگری حملات بیشتری علیه ایران انجام دهیم./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/668734" target="_blank">📅 01:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668733">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
ایرنا: بنا بر شواهد میدانی هیچ اصابتی در زاهدان وجود نداشته و اخبار منتشره در فضای مجازی کذب می‌باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/668733" target="_blank">📅 01:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668732">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/afdd27149d.mp4?token=mIDHXbgVEzJXgWWGYuEOEQuq9alBajg2BjsT_4Z8aSLRMXKDL5HJ6iByupsKBgaJ3050Y_yNaKhXpf5054ATuO49Imdhjstpr8GwDmB7YccSFUfMdMSjTTmQnnyQVHGZupBVIX62mBMJlhNCLqt3Gyl1YBGlnmfxqvMJuRcWG7nmkuN-Z6Nf9EECbCYIxBeV7RDSbJ4dn0NU2je6WRvIZOyfPNnAiSxbG9yKMhEMq6RKyHIPjuwiRqx-UVDGK9VMoj3LToeGLWHDyYPipci0fAzHynSpp-ym4at4JkqRFNGhuZRqbZ-kytbGO87EZ3PGoXwkW_qqR_w0EZShLXCbbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/afdd27149d.mp4?token=mIDHXbgVEzJXgWWGYuEOEQuq9alBajg2BjsT_4Z8aSLRMXKDL5HJ6iByupsKBgaJ3050Y_yNaKhXpf5054ATuO49Imdhjstpr8GwDmB7YccSFUfMdMSjTTmQnnyQVHGZupBVIX62mBMJlhNCLqt3Gyl1YBGlnmfxqvMJuRcWG7nmkuN-Z6Nf9EECbCYIxBeV7RDSbJ4dn0NU2je6WRvIZOyfPNnAiSxbG9yKMhEMq6RKyHIPjuwiRqx-UVDGK9VMoj3LToeGLWHDyYPipci0fAzHynSpp-ym4at4JkqRFNGhuZRqbZ-kytbGO87EZ3PGoXwkW_qqR_w0EZShLXCbbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«شارع العباس» غرق در استقبال از پیکر امام شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/668732" target="_blank">📅 01:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668731">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
شبکه سی‌ان‌ان در گزارشی درباره نیروی دریایی آمریکا نوشت: ما حداقل ۱۹ کشتی جنگی در نزدیکی ایران داریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/668731" target="_blank">📅 01:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668727">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
مهر: اصابت ۴ پرتابه به بوموسی و سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/668727" target="_blank">📅 00:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668726">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlNDKIx2Lzv_XHIv--S9ysuFqTKKQB2ivjgFYDLDJMyAjPv8w0V0nkqF8XpPzy9LB9Cyk5ta6uWFuBT3rkSmKxPPZA95SzAAuiMi_0I_0dTerPnK7yTl8FrcwaRMH-u5xtKFBE6UthdJOcGRENqy3GyywyF9KBHhaPb2e2KjEu-FCTejKAqPoFwyfsVtBaBQiAqNiHFDgLI4oQVLD9Wc3SZ-tCDXy2y5l_hrt2zS9Zavl2FPUszol_vUeMrrcSQMqHchrUpTboT9pwDJ07X956P7b0YVGydYGYkWIiEd_YVdDAXn_RN5JYf2yiaUH8HlORXJSKA2uOwB3V3GjS64KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماره مزايده در سامانه ستاد:5005095004000006
موضوع مزايده: بهره برداري از پنج دستگاه كيوسك هوشمند شهري در سطح شهر مشهد مقدس مطابق نشاني هاي مندرج در اسناد مزايده به اشخاص حقيقي و حقوقي واجد شرايط به صورت اجاره .
مدت و مبلغ بهره برداري: به شرح اسناد مزايده
جهت اطلاعات تكميلي به سامانه تداركات الكترونيكي دولت ( ستاد ) به نشاني
www.setadiran.ir
و همچنين جهت اطلاع در روزنامه رسمي به نشاني
www.rrk.ir
مراجعه نمائيد.
#مزایده
#مزایده_عمومی
#کیوسک_شهری_هوشمند
#سامانه_ستاد
#سرمایه_گذاری_مشهد
#شهرداری_مشهد
#سازمان_ساماندهی_مشاغل_شهری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/668726" target="_blank">📅 00:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668725">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9793440cc1.mp4?token=aBTSi5MgFHUbL0oC-lM6FeLTWDlQuff6DDulsQHue3NNiFDIZvODxCjAEWVrS5vAXcAWk9gm5ITbWkVBb03CsNv4090JsK3k3THdmmU-aBmLdpvP8g8tlJn1R4JYZzoo8ZjzEi9rqudfinnTFnIhz416nK--NM9k_N02FrIOoj6LKwUUeJRYqsyY3wQLwLy_H7VDiwQy7faodRla85G34sF1wF9_voNqnIFm6MIM0SCzyG0I__hyvaxDGLJjJ1f-zkH1hNEc_fyD3lfHDbOmbF4-5qbCnmkKwTotp-bNBzRspIR_7hHi08EnP6c7R6pqF61Wr1qxegoQaa1fqGzaPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9793440cc1.mp4?token=aBTSi5MgFHUbL0oC-lM6FeLTWDlQuff6DDulsQHue3NNiFDIZvODxCjAEWVrS5vAXcAWk9gm5ITbWkVBb03CsNv4090JsK3k3THdmmU-aBmLdpvP8g8tlJn1R4JYZzoo8ZjzEi9rqudfinnTFnIhz416nK--NM9k_N02FrIOoj6LKwUUeJRYqsyY3wQLwLy_H7VDiwQy7faodRla85G34sF1wF9_voNqnIFm6MIM0SCzyG0I__hyvaxDGLJjJ1f-zkH1hNEc_fyD3lfHDbOmbF4-5qbCnmkKwTotp-bNBzRspIR_7hHi08EnP6c7R6pqF61Wr1qxegoQaa1fqGzaPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل جمعیت عراقی‌ها در تشییع رهبر شهید انقلاب در شهر کربلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/668725" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668724">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuAxPJlWSWderWx1r9ECFFPoIjXVq7uH685R7lRTsp13juiSYCJz_Bxr24197fY8rVIN-A8fagAes4TXrInFo_ZvvN2qC0ixea0V2yq_zhI868gtK7Ar8xpO5SuPsv4B856bjmWfkMsMJlPUHu17QFqfLLO9NjsXX2XOBpru7aFDAolrAvxlHJ9nW5O2TL50-Qs_3QYyMwivteUGIqoU539rUKLYjIG-189bzS7XPLATTgPDG1cQ1ssddn5OyqwYReLJeQTGc_Uo0fjXOZZUAv2z1IFKQJ-usGfxvDbrkn9S5ZHxazbTXnxTO5AyafMgynK_T5SvnY8n0OYcCwNI7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن رضایی: دشمن به شدت تنبیه خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/668724" target="_blank">📅 00:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668723">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
اصابت ۲ پرتابه به پایگاهی نظامی در جنوب شهر بوشهر
معاون سیاسی و امنیتی استاندار بوشهر:
🔹
دقایقی پیش پایگاهی نظامی در جنوب شهر بوشهر مورد اصابت ۲ پرتابه دشمن آمریکایی قرار گرفت. تاکنون گزارشی از تلفات انسانی ناشی از اصابت این ۲ پرتابه دریافت نشده است‌.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/668723" target="_blank">📅 00:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668722">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
مهر: اصابت ۴ پرتابه به بوموسی و سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/668722" target="_blank">📅 00:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668721">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
مهر: یک پهپاد متخاصم دشمن در جنوب کشور توسط سامانه پدافندی کشور رهگیری و منهدم شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/668721" target="_blank">📅 00:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668720">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
دقایقی پیش مردم در چغادک استان بوشهر ۳ انفجار نسبتا شدید را حس کردند
🔹
هنوز محل دقیق این انفجارها مشخص نیست.
🔹
چغادک در حملات روز گذشته ارتش تروریست رژیم آمریکا نیز هدف قرار گرفته بود./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/668720" target="_blank">📅 00:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668719">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
منبع آگاه نظامی: لحظاتی قبل؛ اصابت دو پرتابه دشمن آمریکایی-صهیونی در شهر بوشهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/668719" target="_blank">📅 00:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668718">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e90accfc73.mp4?token=N68nQnK2bRKygF5RV1-SptWRM0qikagqhKJVeHJCIoTt6QdeeHkLowXY5eTqV2yy_fjVM8DQI5qGZU6KZJKIukAsommMQSE8QWyN8gj2r5Ik1PjCLjZigysa9AbGSxFR6wQfUBFBibzStsVlQmb0xje0eBiu5YvnRW-H3QoXorY1QbkCowzdPEuNz2cmMCXhgZn5Mg7VX-mpNUJQzxm-ld8ksmH-FasuFO8tiZclXOQPxPrdq7ZgFzRuXcH7gMY93MdbBpxxs_Cq7NsFfQUWu1YlP66R3T1_NEpZ7-oREBpB6ZP9C3-3ngf7RydJ5Ln9_9nlYIkkErErT2A2N9lWWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e90accfc73.mp4?token=N68nQnK2bRKygF5RV1-SptWRM0qikagqhKJVeHJCIoTt6QdeeHkLowXY5eTqV2yy_fjVM8DQI5qGZU6KZJKIukAsommMQSE8QWyN8gj2r5Ik1PjCLjZigysa9AbGSxFR6wQfUBFBibzStsVlQmb0xje0eBiu5YvnRW-H3QoXorY1QbkCowzdPEuNz2cmMCXhgZn5Mg7VX-mpNUJQzxm-ld8ksmH-FasuFO8tiZclXOQPxPrdq7ZgFzRuXcH7gMY93MdbBpxxs_Cq7NsFfQUWu1YlP66R3T1_NEpZ7-oREBpB6ZP9C3-3ngf7RydJ5Ln9_9nlYIkkErErT2A2N9lWWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر مطهر رهبر شهید انقلاب، با استقبال مردم عراق وارد شارع‌العباس(ع) شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/668718" target="_blank">📅 00:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668717">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXzHz2Wlme8KohniVOHQDhXLlTaIU4RzgbHz46DFSfL2faSuaOfC66KxSis8Evdg8XczfJkveObL2Ejzuk4qAHxGuFHu0Eqe_3Dkq6LS6V-VKlU8EgmF9YODreTXjIFvjLsgKLaUG9Sl4C9zv0q4aYPvm77PCwlcBfF2THTo2M0BtJN5a4N9wcjx33AdBgTM7YGx1AzomJ1SkcmpQWCkAObR--G6XNFWPkj3VEu2PyOJkh94tOMkUqWayAqt-dULrQZhX7cpO-ZEexuQgOGXNABHFQtW0i2E8bHkBOZL2vwcTTqzHuTT7HJDiP6lpqHJ-SOUIprhjRkFktL7KWjbHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شنبه حداکثر دمای تهران و کرج به ۴۲ درجه میرسد، بالاترین دمای امسال تا الان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/668717" target="_blank">📅 00:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668716">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
یک مقام آمریکایی به رسانه‌های آمریکا ادعا کرده است که حملات جاری ایالات متحده علیه ایران، احتمالاً از حملاتی که روز سه‌شنبه انجام شد، گسترده‌تر خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/668716" target="_blank">📅 00:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668715">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
تجاوز مجدد جنگنده‌های ارتش تروریستی آمریکا به مناطقی در بوشهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/668715" target="_blank">📅 00:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668714">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
تکذیب شایعه حمله به جزیره لاوان/ تأسیسات نفتی در وضعیت عادی هستند
/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/668714" target="_blank">📅 00:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668713">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
تاکنون انفجار در خارگ نداشتیم
🔹
خبرهای منتشر شده در مورد صدای انفجار در خارگ صحت ندارد و تاکنون انفجار در خارگ نداشتیم/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/668713" target="_blank">📅 00:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668712">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
آکسیوس: آمریکا امشب حداقل ۱۵۰ هدف را بمباران کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/668712" target="_blank">📅 00:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668711">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
فعالیت جت‌های جنگنده خودی بر فراز اصفهان
🔹
دقایقی قبل صدای جت‌های جنگنده بر فراز اصفهان شنیده شد که بررسی‌ها نشان می‌دهد جنگنده متعلق به نیروهای مسلح ایران است./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/668711" target="_blank">📅 00:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668706">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
برق بخشی از چابهار قطع شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/668706" target="_blank">📅 00:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668705">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GloQY8txDsLh28oXmeL7YG_zbK-fYJ9EEV03WtQ7g5azLyVjZh2MllDEypQlWElxmdOAmsAo3W784tWTEcU6736RAmCpknLbItqz69SliRI_LuWaN04DgAG4I6kC6A3GFTfx2MKz9Oi1AreFd0VsRVw4naz2uxoXjeEJH3ILO92KZNBk-lMQ16VSc02ROzDEiMhwJpnYt8b9w_rU6ZV2bCDxIRTXgkTnddzyMzcEdosD9QaOVXlXJdGvReYPJ3Fei-pIlLib0r9qK24MyVRhzfXf2w6MAGIGL3zZdcrTkWobDHMdiFbK3cAsZ5hIeCgsj1BNyD8YLYaHCvqZjf9tQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«آگهي مزايده عمومي»
شماره مزايده در سامانه ستاد:5005095004000005
موضوع مزايده: بهره برداري تعدادي از فروشگاه هاي ارزاق عمومي شهرما در سطح شهر مشهد مقدس مطابق ليست هاي مندرج در اسناد مزايده به اشخاص حقيقي و حقوقي واجد شرايط به صورت اجاره
مدت و مبلغ بهره برداري: به شرح اسناد مزايده
جهت اطلاعات تكميلي به سامانه تداركات الكترونيكي دولت ( ستاد ) به نشاني
www.setadiran.ir
و همچنين جهت اطلاع در روزنامه رسمي به نشاني
www.rrk.ir
مراجعه نمائيد.
#مزایده
#مزایده_عمومی
#فروشگاه_شهرما
#شهرداری_مشهد
#سازمان_ساماندهی_مشاغل_شهری
#واگذاری_فروشگاه
#ارزاق_عمومی_مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/668705" target="_blank">📅 00:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668704">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
هم اکنون؛ شنیده شدن صدای چند انفجار در جاسک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/668704" target="_blank">📅 00:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668703">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
برق بخشی از چابهار قطع شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/668703" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668702">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
صداوسیما: شنیده شدن صدای ۲ انفجار در بوموسی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/668702" target="_blank">📅 00:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668701">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7b02a9986.mp4?token=jSG98uhXIxMwHkDcX6MOXoLQ8u_ZpOLIbEUIulet0s-loeS9z1GqMRpLsG_p2UbkzqQsLNwz4sqJJjqG4rGw6ADYGSG-ARApgWjGM8YGzbOaCTp1Yc_aAk-5yHoXGo-rKeCdCJLvJaAfPU4-X4HSrgrhS3ouY4NLav4BxE7Btz7O4v-12yFWClNxNPSu-RsSr3lWGtEDRFjGnD3D1mefAaOw3lqt5-RIhH10Guz2W_rmdGKkKuXS_F9U7DmApsmULZIIOvMzW4LgdqXOYAG-Q40hBR3icyVRmOvU7GOQttT0N72K-U5GHOaJaYPCWbQKSyVMEDGsi2l7xKArJ2-DIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7b02a9986.mp4?token=jSG98uhXIxMwHkDcX6MOXoLQ8u_ZpOLIbEUIulet0s-loeS9z1GqMRpLsG_p2UbkzqQsLNwz4sqJJjqG4rGw6ADYGSG-ARApgWjGM8YGzbOaCTp1Yc_aAk-5yHoXGo-rKeCdCJLvJaAfPU4-X4HSrgrhS3ouY4NLav4BxE7Btz7O4v-12yFWClNxNPSu-RsSr3lWGtEDRFjGnD3D1mefAaOw3lqt5-RIhH10Guz2W_rmdGKkKuXS_F9U7DmApsmULZIIOvMzW4LgdqXOYAG-Q40hBR3icyVRmOvU7GOQttT0N72K-U5GHOaJaYPCWbQKSyVMEDGsi2l7xKArJ2-DIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای ورودی باب‌القبلۀ حرم سیدالشهدا(ع) و مردمی که در انتظار رهبر شهید انقلاب هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/668701" target="_blank">📅 00:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668700">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
برق بخشی از چابهار قطع شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/668700" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668699">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
مهر: تا کنون بالای ۲۰ انفجار در بندر چابهار ثبت شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/668699" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668698">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
تسنیم: براساس برخی اخبار غیررسمی، پایگاه امام علی ندسا در چابهار توسط جنگنده‌های آمریکایی مورد هدف قرار گرفته
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/668698" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668697">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
یک مقام مطلع در استان بوشهر: تجاوز امشب ارتش تروریستی آمریکا به بوشهر آسیبی را متوجه نیروگاه هسته ای نکرده است. جای نگرانی نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/668697" target="_blank">📅 00:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668696">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
شنیده شدن صدای سه انفجار در محدوده روستای طاهرویی سیریک
/صداوسیما
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/668696" target="_blank">📅 00:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668694">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ayf8KbjVElq6uQHZWxn-APhZISLBT6ocIC79JTZEXwYth4Ey-Nt_lJkWuXgAknYUhQyGjyOCn03zk1_CWkRTWkakF8ZVdDwBQcW3ZpdHl8JNEgngTMilfp3xviZRwUH36tqatwmP7-YT3Zc2SfM7ATQocoeT5Ps-HmsLo8GmJl-njeOYK-sWFnamdAcGycm_Tv5aVY9ev3UY8WAK3A6DqQ4eGqrKeP-NvVJdHBVjoB673m6kxWVNEgCflGFD_Rg4RqpvZvVO_18tcXnT4Q6g7czHaezN4qWHOgkoB7OghAVhDphNN4-hOzjXSaZmcBiAiaOc9-C1AyfsomF9ul8lXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B39ZXw56DAvx5G_XHXRZIFITkdUI-b_zMiSbImmfzbfOfYbHkQ_vr8BUvOOI9v3MCxVx4uELPVvI0F6Gks_CYWIeNSiK8dNyvIFLOAzJVc9CzB20Jix008D8jTiDFQy93SLd_jG2W6QMmyu4O2nf247x3qdquWpXkYc9LQi4qYZ0rp74wCrROYspNZ4ZTkIjQ9mC5f52YWnatlhyII6uIPOn5mACb1viV0lr12H6zKpu9fA-0kD0Mn2xoGIhtw2IRa94XMNw0r24MKaNWqTYN8uXTM3P4ax93zmJ5tLvlZAzEZrMjIjWbqTuFesO3m75z4vtVBJzrSa44hOvlw2geA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر منتسب به پایگاه امام علی چابهار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/668694" target="_blank">📅 00:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668693">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی مجلس: آمریکایی ها بدانند پاسخ کوبنده‌ای به آنها خواهیم داد و امنیت را در  هر جای دنیا باشند از آنها سلب خواهیم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/668693" target="_blank">📅 00:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668692">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">عربستان سعودی، انتقال وجه به امارات را مسدود کرد؛ تنش‌ها رو به افزایش است
بانک‌های عربستان سعودی به دلایلی نامشخص، انتقال وجوه به حساب‌های مستقر در امارات را مسدود کرده‌اند که این امر، نگرانی‌های گسترده‌ای را در میان شرکت‌ها در پی افزایش تنش‌های ژئوپلیتیکی بین ریاض و ابوظبی ایجاد کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/668692" target="_blank">📅 00:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668691">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
آکسیوس به نقل از مقام آمریکایی از حملات ارتش آمریکا به اهداف نظامی‌ ایران در جنوب کشور خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/668691" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668690">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
یک منبع نظامی: پاسخ نیروهای مسلح جمهوری اسلامی ایران به تجاوز امشب ارتش تروریستی آمریکا پشیمان کننده خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/668690" target="_blank">📅 00:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668689">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
رویترز: قیمت نفت خام برنت با ۵.۲ درصد افزایش، به ۷۸.۰۲ دلار در هر بشکه رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/668689" target="_blank">📅 00:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668688">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
مهر: تا کنون بالای ۲۰ انفجار در بندر چابهار ثبت شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/668688" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668687">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
صدای انفجار در بخش هایی از استان بوشهر شنیده شده است
🔹
هنوز اطلاع دقیقی از جزئیات و ماهیت صدا موجود نیست./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/668687" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668686">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XF9-KtdqsVXZWO_gPge7hCwAM-9DMeuFr8RqMwASVSwWU64sfebV5n86IpubTETRxwh10LN893YOYuEythOOEVIkcayy21FKDHkXxV_PpPFPm_YU2pBp3L_ctU_KR_cCVv12upkGf57zA7NkwJ2I0xlXR4w3ripXN-zThtz2doUbNhjNbKCpbnOezTh4726WwE0FY_z4r2db60ZwEzuCH8ram3rP-okkvdgE0r1rs7VVkGUp94eZufAtIqftC8WC1kedK8v0prvYzpB-WtcNhijP0kRhyKMIUQfY480QEGrudwzx40bRqDBe3cUvpb4edtT8JA5nyo_m6hMYTGAUMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا بعضی‌ها با نصف توانایی شما، ۱۰ برابر بیشتر درآمد دارند؟
‌
نه چون باهوش‌ترند...
😑
نه چون شانس بیشتری داشته‌اند...
🙄
‌
بلکه چون یک چیز را زودتر از بقیه فهمیده‌اند.
افزایش 10 برابری فروش آنلاین شاپ
👇
https://t.me/+Xot5PGy2C04wMzA0
https://t.me/+Xot5PGy2C04wMzA0
https://t.me/+Xot5PGy2C04wMzA0</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/668686" target="_blank">📅 00:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668685">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sclUzO9r2G2nSyUy_dIsk7ZKt7IUpymGhUa9XxOwtKpiJaq1TzTmOmBHCo_fNfUHsS16Dee9lqIHovRZ8QNRmZrT1W4Tih_aFRGJwVVqjCx75rnhvXjFr4EhqWYpwJxVBfB3QnhT2dMERIUABvUuXo1l5DQAIFXI2rorjOA3JQLT1QHhsmj7gXup_8qQisxtMpdqEez5lyaFMHkd1KNzU1U8hlKeUJqQPj1PU2IVLlJWqmWZHxeTWnPpJpp4mzPHGSGAtMfDCajT_HBtXUEdJksl-2xEf27BWiKA5lB6yr6vtzQ0HBzMYaZGSROEjakeOh7H_1y5w422m1UWTj5L2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قدردانی سردار قاآنی از ملت شریف و غیور عراق در پی تشییع باشکوه رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/668685" target="_blank">📅 00:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668684">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-a0b8zdJodSMG0Q8kublSH53cQeZjz44OwSAENlkvO1jxMhVGfIW5dZ8_FhkbNK8VjZlQd0y4zRxaETVJLEjceO-d4A2Hk3mSYfuSRSCoMuwxHjVBaoRZl3cFQJuidn82KdYtn97cXzZ54H7sZrXjTH5I_R89_Skp-AXqMEgv1ybE9282KL2IO2mXp4wTGCE-zALbtqtmsRcxeq6tSNVUeZp_LYgTv8hEwm6rzHtAMcc2EsoMzM6xjMjyuPF7uhuBcUcRNz1PXOItyZ65xim84PKE9g9flstdnVJxMYIURvnj3aEbQrVAAFvHwdq_MnnZVY8remB27mWquDGetEpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/668684" target="_blank">📅 00:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668683">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
مهر: شنیده شدن صدای مجدد انفجار در بندرعباس
🔹
شدت شنیده شدن صدا در ناحیه غربی شهر بندرعباس بیشتر بوده است.
🔹
همزمان پدافند شهر بندرعباس نیز برای مقابله با اهداف متخاصم فعال شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/668683" target="_blank">📅 00:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668682">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
صدای انفجار در بخش هایی از استان بوشهر شنیده شده است
🔹
هنوز اطلاع دقیقی از جزئیات و ماهیت صدا موجود نیست./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/668682" target="_blank">📅 23:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668681">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
شنیده ‌شدن صدای پرواز هواپیماهای جنگی بر فراز جزیره کیش/
ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/668681" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668680">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: شنیده شدن صدای ۸ انفجار در بندر عباس و فعال شدن پدافند هوایی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/668680" target="_blank">📅 23:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668679">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
منابع محلی از شنیده شدن صدای چند انفجار در بوشهر و هم زمان درگیری آتش‌بارهای پدافند هوایی با اهداف متخاصم خبر داده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/668679" target="_blank">📅 23:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668678">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
مهر: طبق اعلام استانداری هرمزگان هیچ برخورد یا اصابتی در شهرستان بندرعباس، شهرستان قشم و شهرستان سیریک صورت نگرفته است و پیگیری‌ها برای کسب اطلاعات بیشتر ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/668678" target="_blank">📅 23:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668677">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
گزارش‌ها از چندین انفجار شدید در کنارک و چابهار خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/668677" target="_blank">📅 23:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668676">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ارتش آمریکا رسما از حمله به اهداف نظامی ایران در تنگه هرمز خبر داد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/668676" target="_blank">📅 23:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668675">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfwIk5SYWwdaJWfidbJUXe2f-M2KkhDXcU2VZ1Qv9MKXK-GBuzJJMt4_H2bQvhugA3NEdjzzYICkVYKFlz7BpkCBjxgqo3VLzjVfMCsosq1C2NNltaJFgQPMqzvse4Xb--JzxxETQ2l0vIZZCCoOWMgIfMHamzkjnft1XTENzZZIPp6aE2RNC43CM821bDfq8DP3atr6mabwV3qzw7-9g9NTDdIYzyC7zC1D70AnyPsv6AdWtAK-0_URMmAlS4glhWnHceqf-tctDmMiymuzbcGdV7Aj931aOuG8if2btdChlXmsrYt95w7jIdhjGThrGA8_2oF-OlA6vM1xS2h3IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش آمریکا رسما از حمله به اهداف نظامی ایران در تنگه هرمز خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/668675" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668674">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
آکسیوس به نقل از مقام آمریکایی از حملات ارتش آمریکا به اهداف نظامی‌ ایران در جنوب کشور خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/668674" target="_blank">📅 23:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668673">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
گزارش‌ها از چندین انفجار شدید در کنارک و چابهار خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/668673" target="_blank">📅 23:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668672">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dfdfe604d.mp4?token=jOjvLL0EKDL0wFTsK1N0h8aNOEU_OcBgQhpZRkBXBh7H4a-D9fho_Rulv-LhtUCS3LRAPdhiu8o_p2pxS4sNaTVu_31NboTXns_M2nBUVKdXqRS0S_N2APeZ0IbJ6Ml5CAuZb_d65am3kEkiEfV0T6cfVaXL1HMUnGERlG-KLdWUGguQjFo3vORWV54PRkZZV6jUl3_RLhwJfayGhmO-ybG36I6EGL6XQ6GC6gknfbFiuLBMKGEglg4P7Cw1cdQK4N82AviqAzHpHGh_ki5ymhwSWsUfKKE9jqOeyG8ILN4qoO4UTPRp06BJNVB2hjWZb0DISWjUE75KuwS07du8gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dfdfe604d.mp4?token=jOjvLL0EKDL0wFTsK1N0h8aNOEU_OcBgQhpZRkBXBh7H4a-D9fho_Rulv-LhtUCS3LRAPdhiu8o_p2pxS4sNaTVu_31NboTXns_M2nBUVKdXqRS0S_N2APeZ0IbJ6Ml5CAuZb_d65am3kEkiEfV0T6cfVaXL1HMUnGERlG-KLdWUGguQjFo3vORWV54PRkZZV6jUl3_RLhwJfayGhmO-ybG36I6EGL6XQ6GC6gknfbFiuLBMKGEglg4P7Cw1cdQK4N82AviqAzHpHGh_ki5ymhwSWsUfKKE9jqOeyG8ILN4qoO4UTPRp06BJNVB2hjWZb0DISWjUE75KuwS07du8gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهر، قامت بست به احترام رهبر شهید/ چهار قاب، چهار نشانه از عشق و وفاداری...
🔹
معاونت خدمات شهری با آماده‌سازی و نصب چهار المان گل‌آرایی‌ شده از تصویر رهبر شهید، جلوه‌ای از احترام و دلدادگی مردم مشهد را در چهار نقطه شهر به نمایش گذاشتند.
🔹
این المان‌ها، تنها یک سازه شهری نیستند؛ روایتگر عهدی هستند که در حافظه این شهر ماندگار خواهد ماند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/668672" target="_blank">📅 23:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668671">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
الحدث به نقل از یک رسانه اسرائیلی: واشنگتن از قبل به تل‌آویو اطلاع داده بود که امشب حملات شدیدی علیه ایران انجام خواهد داد
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/668671" target="_blank">📅 23:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668670">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بندرعباس/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/668670" target="_blank">📅 23:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668669">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔹
از خبرهای پُربازدید امروز وبسایت خبرفوری غافل نمانید
🔹
🔹
آغاز دور جدید جنگ های ایران و آمریکا/ تفاهم اسلام آباد مرد؛ منتظر «جنگ بزرگ» باشیم؟
👇
khabarfoori.com/fa/tiny/news-3228841
🔹
اولین تصویر از محل احتمالی دفن رهبر انقلاب
👇
khabarfoori.com/fa/tiny/news-3228872
🔹
موج گسترده شلیک موشک از نقاط مختلف ایران
👇
khabarfoori.com/fa/tiny/news-3228652
🔹
احمدی نژاد دستور رهبر شهید را اجرا نکرد
👇
khabarfoori.com/fa/tiny/news-3228861
🔹
تهدید حذف فیزیکی معاون رئیس جمهور توسط گروهی ناشناس
👇
khabarfoori.com/fa/tiny/news-3228696
🔹
ویدئوهای جذاب را در آپارات خبرفوری ببینید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/668669" target="_blank">📅 23:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668668">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار در جنوب کشور
🔹
حوالی ساعت ۱۱:۱۵ صدای چند انفجار در بندرعباس و سیریک به گوش رسیده است
🔹
همچنین صدای برخی انفجارها از سمت دریا در محدوده ساحل غربی سیریک به گوش رسیده است. اخبار تکمیلی متعاقبا اعلام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/668668" target="_blank">📅 23:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668667">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
تغییر ساعت مراسم تشییع رهبر شهید در مشهد
ستاد استقبال و تشییع رهبر شهید در مشهد:
🔹
با توجه به استقبال کم‌نظیر و باشکوه مردم عراق از پیکر مطهر امام مجاهد شهید، زمان ورود پیکرهای مطهر به مشهد مقدس با تأخیر همراه شده و از همین رو مراسم در ساعت ۱۴:۰۰ برگزار خواهد شد.
🔹
مراسم استقبال و تشییع رهبر شهید انقلاب و خانواده شهیدشان روز پنجشنبه ۱۸ تیرماه از خیابان امام رضا به سمت حرم مطهر رضوی برگزار خواهد شد.
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/668667" target="_blank">📅 23:29 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
