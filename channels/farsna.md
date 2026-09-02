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
<img src="https://cdn4.telesco.pe/file/U3aLflqBG6NJyk7q4Vg-PRRqaGwhBzWGwAynLeJHYFY9Kw3iEffaHLjBQbid81CsF7SFK8N2_EREOAPaTRBrwk6yuae6gJ8WmTiQC2HRZz4eCLNAA1KCf0KZDxe3rJ-_RTXQO57AHJ7lf-JPGHzR5desY-6g-h9fu5gWXYq4p029jBNT9oJbsSzsmM0IWHIBHJ_c7fax5WQm-azkknRZWY_ZNCihxadIdLpHqIDahZ76gPnpNylNMPAUhpSf2x81ed4rYkYOgKLd9rlVBj76ZMthsjrCW2vJ9h6DzrU-2QpssMmP6Pyiwf8gYzkJJlGNusvcGneDfP-MqRp4mkLeWg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 15:40:45</div>
<hr>

<div class="tg-post" id="msg-459717">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/farsna/459717" target="_blank">📅 15:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459716">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1iMd170K91LB-whp00iWHVe7NfBS3ErJzWJcOCuGkUP-gHjOSYUS_DzM7fEfJyc02HPN54_fCgAuujPFd7M4IYuP3YwGWtj1z5_YBAmskR8yxzR3EhtbMCA2n5MTyKEm9d1AJ8LY4xN2ToIyWwJtUK_s8PR_264U9X8_-RJAh6KFn4UEo0zZC7FjsPfl1NdvE_sVbDjRS9YPHyZYrlPuz-aYo8k2zZasexAIPRtMPjRyRYXVm4f0A5MKRxbhR0vHiP6MaJImaMTc9vWTgskF76YMuUKtzO-_sMz7itulNiWIoQ23kwSh-w_LGCol9awrsX7U_Sks7dG7IE7fE1how.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی‌دلیگانی: پایگاه‌های آمریکا در اروپا هدف قرار گیرند
🔹
نایب‌رئیس کمیسیون اصل ۹۰ مجلس: در بررسی‌های دقیق و برآوردهای اطلاعاتی، احتمال هرگونه اقدام خصمانه از سوی پایگاه‌های آمریکایی در اروپا مدنظر قرار گیرد و در صورت احراز این احتمال، آن پایگاه‌ها در چارچوب پاسخ متناسب، هدف قرار گیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/farsna/459716" target="_blank">📅 15:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459715">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2rRvVIJ5shsY76b1RaMpQ4W2pfKidmdalyMP0HLOPubaJkxGfVRegnTOA5E5AiAaXzzO4q34I-rWOxgOBNDewGlxEPTRv4fphA47_hA6Ax4KFGGDexNikKLjIw2YBJwEwxTXUiRR313SbexhuUxsrCB9SDZw-ys0rW1fnNW_HOkqSWwpKipKQmB9BrezbQBtFfUbwTE7KS_IEtVphrD-rENxd92nM-fE0bgEkecAVgOXIfapej9jgcGQAjog-OCIQ4d47hFZjk8zDuzaycqFW85x32-m_Nv-p12EWh_UwIcfiUHcsWYehuOVFrWgTQNVs5wbo80I9FHQ3oP5FPMEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرکس این عدد را گنده‌تر بگوید، برنده است!
🔹
وقتی آمار قربانیان یک حادثه از ۴۰ هزار به ۱۰۰ هزار و حالا به ۳۷۸ هزار نفر(!) می‌رسد، دیگر با یک اختلاف آماری ساده طرف نیستیم.
🔹
عددهایی که هر روز بزرگ‌تر می‌شود، بدون آنکه سند و فهرستی برایشان ارائه شود؛ روایتی که ظاهراً قرار است با تکرار، جای واقعیت را بگیرد.
🔗
ادامهٔ خبر را
اینجا
بخوانید
@farsnart</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/459715" target="_blank">📅 14:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459714">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DH7sFy6FyZAyM26jq3gB9DJu1MxPpw4EfmfoLpVfbLYHssSK5qQrZwp_r_MmkAkOZlTNC0HLUa2nQSH86_Y8E0hR0AtzwdDc4HG1WwQmSuZGjwPljPHQklKJyCC0BHjllJgB-3BOEp_pGQOpYUveWY8cMWOy_AStGc6Y5mzGSxmUCPungb1FG6an3_bZUGxFS_k-NJYyd86-oM7vzXG9zrbo4nXrmvHhTzL-98v3wX9pbdGLmgvyIT_RNMmWdYE_8fNmXq0ix-HLOlxvC-NNoUHL8g5oqoDplP6iHfYaD29U0Cj14c_gEOgVoj04dYoJ18F_OHmQbPn6K4f00QCVzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: تمام اقدامات آمریکا به تقلید از شیطان و خود آمریکا شیطان بزرگ است
🔹
رئیس‌مجلس در واکنش به حملات شب گذشتۀ آمریکایی‌ها علیه مراکز غیرنظامی به خصوص شهادت جمعی از هموطنان‌مان در یک مراسم عروسی در جزیرۀ سیریک، با یادآوری جنایت این کشور در میناب و لامرد،…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/459714" target="_blank">📅 14:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459713">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd66906547.mp4?token=JYCQpV1RwUJ3coM_DHSU28Z3WcpHyuYIuj3LPjH7rQBTJM90PFSg4flGLQMW1WSjIQh_mh9kCexSPz3BPvuclDhT9pzpT75LV43SMZMrWUdLSeUZm40hLEzA3TPGDxLIDWneXixqY0V11HVnw8YMqKyEsBpxEGV8LMVldDvEKsS1aqmMXSa_J-x8LTT5HWpFkzpjX-uQClXtUk97EyQc_8iyMsk9SWR_cpalH6UuLLVtZpSaOrL0uOtQxLLaLIVA8goAoULpWgLWeY6nCVZfX5tffnuxn9c5MMytaZMjqJIP4NJQXWdA-hn5ETD630cCoSHX_5bJRc2WubJRjUE6aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd66906547.mp4?token=JYCQpV1RwUJ3coM_DHSU28Z3WcpHyuYIuj3LPjH7rQBTJM90PFSg4flGLQMW1WSjIQh_mh9kCexSPz3BPvuclDhT9pzpT75LV43SMZMrWUdLSeUZm40hLEzA3TPGDxLIDWneXixqY0V11HVnw8YMqKyEsBpxEGV8LMVldDvEKsS1aqmMXSa_J-x8LTT5HWpFkzpjX-uQClXtUk97EyQc_8iyMsk9SWR_cpalH6UuLLVtZpSaOrL0uOtQxLLaLIVA8goAoULpWgLWeY6nCVZfX5tffnuxn9c5MMytaZMjqJIP4NJQXWdA-hn5ETD630cCoSHX_5bJRc2WubJRjUE6aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قیمت نفت با موشک‌های ایران بالا می‌رود
🔹
بازارهای سهام آسیا در معاملات امروز حدود ۲ درصد افت کردند و معاملات آتی شاخص اس‌اندپی آمریکا نیز کاهش یافت.
@Farsna</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/459713" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459712">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0cc9769f7.mp4?token=Tj_Iw7k5YhHu-POZBfuWPfTbUEDCfyf4mtjxwxcsWL7BRqbic3WA1SucJXHYknAF63PCYACC5yzLX4Hzng-OFOk5_iCQuG0l5TkPzV9hpPM4q1hM_iZOzzlbg8Xg-x12L3CR-XF5wLKJqZ-wy5Swupys3MDErstUYrvFMcjl-vm3ItJDb1cPNaNKrQAprKx5vel3i1Co5gWeklozPjE0wvbV-l2FI57eza6JXNEiMY6JpAIscedslompWqRh04bFX1smQARDTUv9d7suj6Po39_Ry8T4Tq05Kv7U5hj2d0Ui69eq1Gcm_E_9gSv2buh6Qj2iXd2L0G3SmB8tElmbPH8bf4oKgjzwL1rLTw6dL8Ab47xea6jBY23pNP2NZ0OXYlXGdDHqr7RVOMr-leza-AQZpkpVcfxANRFkGeIHOZ_rAlA6pkwT_q6_97TUhbRzQw3km4K0t-7Jw64OgFQUQZweQmn_B4UmFCBjPqPVibCsGR-tXZl2vLl-vTeHsWnK_f4XzJD1PxWlDmaf09fFWA_fRaClBBwskRF_jEOzdZFDFXXGVjN3jrpqabIXIhdaQ-IkZDTd9Z6s1EDkmc7WNp_7eFbuyZt2npdmKYoc1O8gKPQMwej4k9Ad4Em8vYZJZZvXt7WfwWu0a384paDOE4g3xtWi3oDfanOlVY_9rbo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0cc9769f7.mp4?token=Tj_Iw7k5YhHu-POZBfuWPfTbUEDCfyf4mtjxwxcsWL7BRqbic3WA1SucJXHYknAF63PCYACC5yzLX4Hzng-OFOk5_iCQuG0l5TkPzV9hpPM4q1hM_iZOzzlbg8Xg-x12L3CR-XF5wLKJqZ-wy5Swupys3MDErstUYrvFMcjl-vm3ItJDb1cPNaNKrQAprKx5vel3i1Co5gWeklozPjE0wvbV-l2FI57eza6JXNEiMY6JpAIscedslompWqRh04bFX1smQARDTUv9d7suj6Po39_Ry8T4Tq05Kv7U5hj2d0Ui69eq1Gcm_E_9gSv2buh6Qj2iXd2L0G3SmB8tElmbPH8bf4oKgjzwL1rLTw6dL8Ab47xea6jBY23pNP2NZ0OXYlXGdDHqr7RVOMr-leza-AQZpkpVcfxANRFkGeIHOZ_rAlA6pkwT_q6_97TUhbRzQw3km4K0t-7Jw64OgFQUQZweQmn_B4UmFCBjPqPVibCsGR-tXZl2vLl-vTeHsWnK_f4XzJD1PxWlDmaf09fFWA_fRaClBBwskRF_jEOzdZFDFXXGVjN3jrpqabIXIhdaQ-IkZDTd9Z6s1EDkmc7WNp_7eFbuyZt2npdmKYoc1O8gKPQMwej4k9Ad4Em8vYZJZZvXt7WfwWu0a384paDOE4g3xtWi3oDfanOlVY_9rbo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیاتی از حملات کوبندهٔ ایران در پاسخ به جنایات دشمن آمریکایی  @Farsna</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/459712" target="_blank">📅 14:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459711">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab6962b2e4.mp4?token=bADQ9rGak9VWtUt3QKd1EP7WpmD0sL176wNocZjjI7KkUdw12mwXMLyAXhezYObIyjApg5mPhLLzs9WuVnh4E5kxopyi5SnwZyMIdDGNzkEtgamMz5XisBcQFwplPagmwL_6bCnP0d0mfJ6RBZtTCoqhShJzCA0R424UvRr_GtWZiBJY3M7ybTZfpXZxurZXucxp7lz5jnPJrP3JuLLKuGjJY1GRpEASmrAs0HEyl2t6kGIP1HLXBVWTohYEwaLufwtcfR40jUxQ0W2p0E17dsojMtTxMBl0eThiiHXUFATohUxme4xrEy70JwOdSpycmVzrNDMzv32MtRu9_5j_Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab6962b2e4.mp4?token=bADQ9rGak9VWtUt3QKd1EP7WpmD0sL176wNocZjjI7KkUdw12mwXMLyAXhezYObIyjApg5mPhLLzs9WuVnh4E5kxopyi5SnwZyMIdDGNzkEtgamMz5XisBcQFwplPagmwL_6bCnP0d0mfJ6RBZtTCoqhShJzCA0R424UvRr_GtWZiBJY3M7ybTZfpXZxurZXucxp7lz5jnPJrP3JuLLKuGjJY1GRpEASmrAs0HEyl2t6kGIP1HLXBVWTohYEwaLufwtcfR40jUxQ0W2p0E17dsojMtTxMBl0eThiiHXUFATohUxme4xrEy70JwOdSpycmVzrNDMzv32MtRu9_5j_Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازتاپ گستردهٔ حملات قاطع ایران به مواضع آمریکا در رسانه‌های دنیا
🔹
بسیاری از رسانه‌ها این حملات را واکنشی از موضع قدرت به جنایت اخیر آمریکا دانستند و از برهم‌خوردن محاسبات واشنگتن در جنگ خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/459711" target="_blank">📅 14:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459710">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd22734b47.mp4?token=aqGToMOjDhfAyBCpnzc2OyvQeqICclS_0W4hGOoNuioCCPr8SqtbgT6ICm_RuIgqcAHvjPuMBFMefOVKO3Ty5YkVMebHx_BUdNCQTqMQHKfEveZ6Xe1zaDL7tpFKWwdnDGDsLpeG96-Rt_nfWGRszfsRoUXkESojqXTYKLw5dRRHbQisFgaCvjxWUeVQxCeZjAuMlf6iRcQ8jbMGAIBJHc5r52AeqjRHxY1ijG5Y3AsUrrhu1wl0XP_FZgDDQSkblR5h-DOnWy9Z9WAUR9BC0pg8QPagV1M5aMV2vUZXGjlL-nPQv7BQrHjlNrxzXk6vZzMbuj-qhPF8-UUN6Hb5-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd22734b47.mp4?token=aqGToMOjDhfAyBCpnzc2OyvQeqICclS_0W4hGOoNuioCCPr8SqtbgT6ICm_RuIgqcAHvjPuMBFMefOVKO3Ty5YkVMebHx_BUdNCQTqMQHKfEveZ6Xe1zaDL7tpFKWwdnDGDsLpeG96-Rt_nfWGRszfsRoUXkESojqXTYKLw5dRRHbQisFgaCvjxWUeVQxCeZjAuMlf6iRcQ8jbMGAIBJHc5r52AeqjRHxY1ijG5Y3AsUrrhu1wl0XP_FZgDDQSkblR5h-DOnWy9Z9WAUR9BC0pg8QPagV1M5aMV2vUZXGjlL-nPQv7BQrHjlNrxzXk6vZzMbuj-qhPF8-UUN6Hb5-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تنگۀ هرمز همچنان بسته است و کشتی‌های مختلف هدف قرار می‌گیرند
🔹
گزارش خبرنگار شبکه سه از جزیره لارک؛ جزیره‌ای که هدف حمله نیروهای متجاوز آمریکایی قرار گرفت و در پی آن تعدادی از نیروهای نیروی دریایی سپاه پاسداران شهید و زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/459710" target="_blank">📅 14:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459709">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5834dd82d3.mp4?token=tBZ2zJZxsNmZJ0zy7GRxYbxqleBVhUDHuZkml4a1_-6egq8gKDV65ZJE1rlBb_LQw9O772kRwi-fF1gCuDVDa1hBJssWh6QHv6YqdyZ-UdLhNJp2hBnX4MnPzWpVjsMbGj2Ue3vx4zLQIjoLSctC9EUoI4NMpSj9WUm0hRbt6B8ruqlFLHYMXWKyw2pgBaSoBwOs37LSxZWdf_UZMCCd42rZqgCNu7KT8vdRgFknUQzpsYoZA2t122wCe0TUFyjTTe3ntW_KrTUL82x_dE5FpIi3un3o-V3jhWPwYU-MaOMd6UjmOs6RGshQfz7Fd9TE5X7HACEvUjBIuVPWJgm_hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5834dd82d3.mp4?token=tBZ2zJZxsNmZJ0zy7GRxYbxqleBVhUDHuZkml4a1_-6egq8gKDV65ZJE1rlBb_LQw9O772kRwi-fF1gCuDVDa1hBJssWh6QHv6YqdyZ-UdLhNJp2hBnX4MnPzWpVjsMbGj2Ue3vx4zLQIjoLSctC9EUoI4NMpSj9WUm0hRbt6B8ruqlFLHYMXWKyw2pgBaSoBwOs37LSxZWdf_UZMCCd42rZqgCNu7KT8vdRgFknUQzpsYoZA2t122wCe0TUFyjTTe3ntW_KrTUL82x_dE5FpIi3un3o-V3jhWPwYU-MaOMd6UjmOs6RGshQfz7Fd9TE5X7HACEvUjBIuVPWJgm_hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه: ۲ نفتکش متخلف با رفتن روی مین منفجر شدند
🔹
روابط عمومی سپاه پاسداران: مردم قهرمان و مقاوم ایران اسلامی؛ ایستادگی شما در میدان الهام‌بخش ملت‌ها شده و جهان شاهد روند بیداری مردم و تنگ شدن عرصه بر مستکبران جنایتکار است.
🔹
شب گذشته ارتش تروریستی آمریکا…</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/459709" target="_blank">📅 14:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459708">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c590c7fad.mp4?token=VhzVFtPW0roFjquAi5FeOm2Ldxix5E3rPCh1kKAI_hLQu7jCeubknyPDo52w8xwmWlKuTt6FVuqbAyXC0Qf0n-W5zjmhU_aDr2QR78eiWKWpsd9803wLPS4l2lGFhm_FA0lQK23xyN5cYnJ0Vy3jQNk93SRdSYI16QhB4x6lLzDJjWmlPxXKS-xuWRw7qWS0LeD7dv5qlWadugW28FY3yPWRq8WFQJJRCb8DDYJ8RgBRj7IA0rDyBZEs4JfVgAPklR819Dp5kUZ3X8chJTmZOYIKd0W8MnCy1HQEjv2FBSEXrswvpi8Rl71xKG0-sz2FSCPuDUkmLwZR0Ps6COtmow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c590c7fad.mp4?token=VhzVFtPW0roFjquAi5FeOm2Ldxix5E3rPCh1kKAI_hLQu7jCeubknyPDo52w8xwmWlKuTt6FVuqbAyXC0Qf0n-W5zjmhU_aDr2QR78eiWKWpsd9803wLPS4l2lGFhm_FA0lQK23xyN5cYnJ0Vy3jQNk93SRdSYI16QhB4x6lLzDJjWmlPxXKS-xuWRw7qWS0LeD7dv5qlWadugW28FY3yPWRq8WFQJJRCb8DDYJ8RgBRj7IA0rDyBZEs4JfVgAPklR819Dp5kUZ3X8chJTmZOYIKd0W8MnCy1HQEjv2FBSEXrswvpi8Rl71xKG0-sz2FSCPuDUkmLwZR0Ps6COtmow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نوجوانان والیبال ایران قهرمان جهان شدند
🔹
تیم ملی والیبال نوجوانان ایران با نمایشی درخشان در فینال مسابقات قهرمانی جهان، فرانسه را ۳ بر یک شکست داد و برای اولین‌بار عنوان قهرمانی جهان در ردهٔ سنی زیر ۱۷ سال را از آن خود کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/459708" target="_blank">📅 14:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459707">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZD5jWyJQCCVT9mjJOHOJW6cZQ71PQQo6dGPuQYlIhUVSFjljXXOKRCOlKz1IMjQVs0FxtygK2nw549rKsUHKitQhcFVibDFE8Posq51EQ1vHfKWDFHkIYmhQHzv2vrMUZlkNZZLTred3OXqcX3DaeFD6rZnHqjoJ9SxxhOfXBx8vonrhu_R9HADLTL6-s6x5ysg5eHjz08Yz-FdjwxENIybTxYlkE5WtOUPAu7xzPziVfay2voFjOH8YO9hKF80n3yRW-tW3LZTJLSeQ20_Am1LaljNSd0jjeLgZVbHxiqGgBV3VGx9cY4XTB5qHA0rm9aqpvSNk2MsiaWHGxfb1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پوستر پرسپولیس و استقلال برای شهرآورد
⚽️
دیدار ۲ تیم ساعت ۱۹:۳۰ در ورزشگاه نقش جهان اصفهان برگزار می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/459707" target="_blank">📅 13:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459706">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGdS7p9K66SslmTPCjcZThp4SyvyUqJmRX6MR5Tr-Rq3ANeE7kEQ4Wz7BqjL6mSrFzm7_aK2lzRHzwYvkiNUWLaA4AD25fNP0D4Ak0EP9uKoBpjgxIxpEbKQcnS1RxCdOAX3pzdj6WS2EVGmt076G7VQpVu0b94H0dSCtQoDhDgjfFp1yW3kAuerRcSGBZj8EG9YyzeNIypoDxCyTkPb7RYgPvIaJRfCjxyrFACKgqugh9PfBaSRRklPwHiNkaPMxhwNBsHrGemn_NqB4t1cbiFFPbg_EZCuYSq9bvMTwNe3pu4Cv80hyIDpD2Mv1QDxdG8KWxqIt7stwaLHkpoHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
جزئيات حملۀ آمریکا به مراسم عروسی در سیریک
🔹
محل عروسی دیشب با ۳ موشک هدف قرار گرفت. در کف یکی از اتاقها گودالی ۱.۵ متری ایجاد شده است.
🔹
۶۸ تن از مجروحین بستری و حال ۶ تن وخیم است و ۴ نفر هم به شهادت رسیده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/459706" target="_blank">📅 13:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459705">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGb5MVquGPIN2JcAxt0_sb6XX35vkDmX__zlVJnpFhZ_R3O-6khLMSOyvcu8LlR6GsrcDFfAqNIqLgJIUN8-oMgLVWBRRat1u1L-JC24x6EygmQPKRpOaWF4QCXVxyUI3hH0NVdy7dqEQqFPCL-Lm9z_qNp6F1EOvZDRS9Y7sFSKe5GrLDQp0ZoBs9vxpPd-YKBKm8LK9lYlcwDaTb4IjkgOoJ6Mpodh9ZRoGuXUXLseGp6l26iKAdIXNAhpMEnt-rEGBbrHMjSmJ_j2qhdskygnwimSPDcrd3YEzRgaeDYWMo9m7Lfcm9TEsv6FGVx4lzLd1FgdT7hpdlvO7A15uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام روس: پوتین و پزشکیان درباره نیروگاه بوشهر گفت‌وگو کردند
🔹
مدیرعامل شرکت دولتی روس‌اتم اعلام کرد روسای‌جمهور روسیه و ایران در دیدار دوجانبه دیروز در بیشکک، درباره وضعیت نیروگاه هسته‌ای بوشهر به‌طور مفصل گفت‌وگو کردند.
🔹
به گزارش ریانووستی به نقل از الکسی لیخاچف، مدیرعامل شرکت دولتی روس‌اتم، متخصصان روس همچنان در حال بازگشت به نیروگاه هسته‌ای بوشهر در ایران هستند و در حال حاضر تعداد کل کارکنان روس حاضر در محل نیروگاه ۴۵ نفر است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/459705" target="_blank">📅 13:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459704">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CedZ6MFDX2wztbnZbRl1FYRqzf4rPMEMu8Rx9gQUhhUlvlSJeHTFU1Ffr1WzWLE3eqqCEHPU9P90ceySFwvZ-77PJZfe1IQ7N3asLwTviwFu_9FxHaeSdfdlgffM1KQ2_iR4gWNLib-yDwZW73j1bfthXfemL5P1VFL-2mKdQDKAvUVmjesSBD57dU8B2dZWyRMZGOQtAJXReqG8pM3jUhrmoKLYSVGblljHNY96Hcxm2ogfu6Cujgs_bem_F3NytuIlJOrfCYu63Q-XZtRCKFGNQY78kU6tq_nZZtMiTaDVgvcMJU873Ev6iuMhmU09tPlwKfZEHU9GndcvV6dQsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
جزئيات حملۀ آمریکا به مراسم عروسی در سیریک
🔹
محل عروسی دیشب با ۳ موشک هدف قرار گرفت. در کف یکی از اتاقها گودالی ۱.۵ متری ایجاد شده است.
🔹
۶۸ تن از مجروحین بستری و حال ۶ تن وخیم است و ۴ نفر هم به شهادت رسیده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/459704" target="_blank">📅 13:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459696">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d242958f52.mp4?token=O6vlQ507_jcy-nl_LJjB_OFigpIBlnZvq2P_C8Zx1Vn4soEzsYrTndbiTSsq3oSobIewkxf49T040FCXA7z9FpG99yn2RA_qxeCySUL1lszOd12b8iaHZwmsg4-rDyXjzQNAJc1osY3bAQQuyJbD4YXjJqfmpRPnUNs3JK0nSCHV5O-c0tI7G1kVLMeaKcbFWk47Phx_iUdYpvMmaBt9wzFPwy40jQdaX3L2tNZwEcxhH-eBP82ruM4SQtsBKsegnj8dsudQy_hP2DxpNZ6uZ6MymxhljrwNQXRTi1GdEbUSZPlhvtl9IKM1iVLa7f3UhPigI_2RGc7310t4wDVuuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d242958f52.mp4?token=O6vlQ507_jcy-nl_LJjB_OFigpIBlnZvq2P_C8Zx1Vn4soEzsYrTndbiTSsq3oSobIewkxf49T040FCXA7z9FpG99yn2RA_qxeCySUL1lszOd12b8iaHZwmsg4-rDyXjzQNAJc1osY3bAQQuyJbD4YXjJqfmpRPnUNs3JK0nSCHV5O-c0tI7G1kVLMeaKcbFWk47Phx_iUdYpvMmaBt9wzFPwy40jQdaX3L2tNZwEcxhH-eBP82ruM4SQtsBKsegnj8dsudQy_hP2DxpNZ6uZ6MymxhljrwNQXRTi1GdEbUSZPlhvtl9IKM1iVLa7f3UhPigI_2RGc7310t4wDVuuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس جبهۀ مقاومت:
مبارزۀ جوانان حزب‌الله در نبرد «علی‌الطاهر» گلچینی از مقاومت مهدی باکری در بدر، حسن باقری در خرمشهر، همت در خیبر و حاج قاسم سلیمانی در حلب است
🔹
حسین پاک: چند جوان عاشورایی شهادت طلب بیش از ۵ ماه است که در محاصره رژیم صهیونسیتی هستند و دشمن را متوقف کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/459696" target="_blank">📅 12:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459695">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دفتر نمایندۀ ویژه ایران در امور چین ادعای شرط‌گذاری پکن برای توسعۀ روابط را تکذیب کرد
🔹
اطلاعیۀ دفتر نمایندهٔ ویژۀ جمهوری اسلامی ایران در امور چین: انتساب چنین شروطی به طرف چینی و ادعای مشروط شدن سفر و توسعه روابط دو کشور به تحقق موارد مطرح‌شده، فاقد صحت است. مخالفت قاطع و صریح جمهوری خلق چین در برابر تحریم‌های یکجانبه آمریکا نشان‌دهنده رویکرد حمایتی چین در قبال جمهوری اسلامی ایران است.
🔹
روابط ایران و جمهوری خلق چین بر پایه احترام متقابل، منافع مشترک و مشارکت جامع راهبردی دو کشور استوار بوده و همکاری‌ها و رایزنی‌های دو طرف در حوزه‌های سیاسی، اقتصادی، تجاری، سرمایه‌گذاری و سایر زمینه‌های مورد توافق، به‌طور مستمر در حال پیگیری و توسعه است.
🔸
مرعشی، دبیرکل حزب کارگزاران سازندگی به‌تازگی در مصاحبه‌ای گفته چین سفر نمایندۀ ویژه ایران (قالیباف) را مشروط به چهار شرط [باز کردن تنگه توسط ایران، دریافت نکردن هیچ‌گونه عوارضی، پایان دادن به اختلافات خود با عربستان و پایان دادن به اختلافات خود با آمریکا] کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/459695" target="_blank">📅 12:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459693">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f879d0348.mp4?token=taOuIU28LjgL-JySNrgoI83WNYG6NjXPGQdHxh_d4H8e855QZAFtS1vrsN9KHvHJKBSv13E3d796Ja3TsT_fwGJMMJ_W7mXypYChU_zBmBgAIRnwddJ_7Qk_OWX4zAfGosCZ70mM9MFzn3T_aVzr_yCbVjHsW5_5qBKz5o7beHZFMSFRE-xsgwyQ3Nks9m0Ux48MBXgjBMyQiOkedTf0bTSpwH6sXaY2XUhyAYUvNKXG74Hbw2RFClToMMzMPbtAiPAiXGYGReJKUFEHv_myV90EqgEC8SVz32E_p6huOg5y61iDYIDQx-vEt4HCMJjfGGsRR4pjAoy8DT3bmPsGlTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f879d0348.mp4?token=taOuIU28LjgL-JySNrgoI83WNYG6NjXPGQdHxh_d4H8e855QZAFtS1vrsN9KHvHJKBSv13E3d796Ja3TsT_fwGJMMJ_W7mXypYChU_zBmBgAIRnwddJ_7Qk_OWX4zAfGosCZ70mM9MFzn3T_aVzr_yCbVjHsW5_5qBKz5o7beHZFMSFRE-xsgwyQ3Nks9m0Ux48MBXgjBMyQiOkedTf0bTSpwH6sXaY2XUhyAYUvNKXG74Hbw2RFClToMMzMPbtAiPAiXGYGReJKUFEHv_myV90EqgEC8SVz32E_p6huOg5y61iDYIDQx-vEt4HCMJjfGGsRR4pjAoy8DT3bmPsGlTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری دیگر از جنایت آمریکا در مراسم عروسی سیریک
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/459693" target="_blank">📅 12:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459692">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3c9ce80af.mp4?token=m8y17-MdEoGNpU3EySWR3Hfzib2NZxbnSU-UJ03yrqMafqRBcHfyLbl_53KSqmrRpQXWEQsg3AYarUperL4Gtj187rV84xi3jBvwiy95rvdJsDluD_921Wh6VUHDyFyh9nEu52H80FkUHReVZcjnorEvxsdeuRYn-4RHCzQ0oLXSYzTYAVegZFelmyAFVt393gi0OLWl3Kvhj76OUCK6rMEoK0uGnnU60edVtLWIEawyTVlAojbWRFUqE_VU5EgnFNlzkCLVDYHyF-LSlxMJnMuB1jbjv7eEE4nNgwUe1RedngaXrYruYGk8M9ahVgXZtCycXwXzrFs-vMZBZuHsoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3c9ce80af.mp4?token=m8y17-MdEoGNpU3EySWR3Hfzib2NZxbnSU-UJ03yrqMafqRBcHfyLbl_53KSqmrRpQXWEQsg3AYarUperL4Gtj187rV84xi3jBvwiy95rvdJsDluD_921Wh6VUHDyFyh9nEu52H80FkUHReVZcjnorEvxsdeuRYn-4RHCzQ0oLXSYzTYAVegZFelmyAFVt393gi0OLWl3Kvhj76OUCK6rMEoK0uGnnU60edVtLWIEawyTVlAojbWRFUqE_VU5EgnFNlzkCLVDYHyF-LSlxMJnMuB1jbjv7eEE4nNgwUe1RedngaXrYruYGk8M9ahVgXZtCycXwXzrFs-vMZBZuHsoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام حاج رضا در برنامه سرآشپز به آمریکا: «اجازه نمی‌دهیم ماهی‌های خلیج فارس را هم بخورید!»
@Farsna</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/459692" target="_blank">📅 12:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459691">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xg1oGYJil1eS9V7zHFo0ndLiYy-EFUA8_Ws7_rTHqCyh93FSYdsXhDUVEVHdS_Aux5CZAuzxevfCSj0NW-ID1ng-n8onJVR4DaKL1cnKIUV5O0QpN4Kj6tLwfROdYLdjRNNZaHwYK3ufmpUzZRmM6cnb8_tWayfm1pm5Hksg6fvrN8yXBC8wdVqMyA_vuPdXt3csXYjMl5JNqamlfBkyK7mySE3GRDw6Bm1Sbp_zbCwlXX3JgWOoZ7SDuzD1t5_pEK9DXcFbh1MTOO-dsIdBrmSz1Rye1gmoftrTJNkiQuDG1isybb0LwQLJ6z8CFJUaSw5VL0x_VU_fS7MnR5-E6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش هزار و 580 میلیارد تومانی زیان «وملل» در سال ۱۴۰۴
بر اساس اعلام مؤسسه اعتباری ملل، زیان خالص این مؤسسه در سال مالی ۱۴۰۴ با کاهش ۵۲ درصدی از ۳ هزار و ۵۵ میلیارد تومان در سال ۱۴۰۳ به یک هزار و ۴۷۵ میلیارد تومان رسید.
مؤسسه اعتباری ملل با نماد معاملاتی «وملل» در اطلاعیه‌ای در سامانه کدال، دلایل تغییر بیش از ۳۰ درصدی زیان خالص خود در سال مالی منتهی به ۲۹ اسفند ۱۴۰۴ در مقایسه با سال قبل را تشریح کرد.
بر اساس این شفاف‌سازی، زیان خالص مؤسسه اعتباری ملل در سال مالی ۱۴۰۴ با کاهش ۵۲ درصدی همراه شده و از ۳ هزار و ۵۵ میلیارد و ۸۲ میلیون تومان در سال ۱۴۰۳ به یک‌هزار و ۴۷۵ میلیارد و ۵۲ میلیون تومان در سال گذشته رسیده است
مطالعه كامل خبر</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/459691" target="_blank">📅 12:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459690">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/459690" target="_blank">📅 12:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459689">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJ-W-XQLU8IDrw1ijJPSGc0ayCtlyaqDFhIoqeleCBb4VqgEz6PcwAyMpR-_bMmodzvrj0voz0AcMMHKItiY4IHcssxjl0b6jUNX9QdoL8kmhAtCNgxwUCo-5WKXMFx2z-qJ7eaPGZPncaH9WR5WhjtoYSn9N6Lbws2cyVhwRKDGeX2AHMQonbs93Y7bw6UZB98NFwdD4rH-0WsJkFtJw2R6heVMeApyvWtk_TU7DEb5UzCnA4C9wFYqI8Xj9l8XrrdWKTGH1dblEDXSzq-fmn-GvEDggf6yJTNn9sQ60QUdMZj9Y9u4vDpYc3EiRzXuuPm6vtzA6V9NYWl-XTRgmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین اجماع گروه ۲۰ بر سر بند تنگه هرمز را ناکام گذاشت
🔹
چین در نشست گروه ۲۰ در برابر فشارهای آمریکا ایستاد و با بند پیشنهادی واشنگتن درباره تنگه هرمز مخالفت کرد؛ مخالفتی که مانع دستیابی اعضای این گروه به اجماع بر سر بیانیه مشترک شد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/459689" target="_blank">📅 12:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459687">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDwqWcSVLOolexsKzpxueNuPYIzYYS3Y1QqL6FBGJUowWEBhh2lwFj6ArWHYCbF5pCNfx6XYQ8guXL_Qc06Q-TKWDQDRImmIm4tNG_2QV9BeGjH6BUvSbYWNIx66Q0UgNFj63uTQkHUxWIWlWbY2NrQjB9ApP9LaiZ8CaLUTU5lPCM9_uRxbM-0DlhMBeHFyqlXUOICDa1m8wjvSUejrh5Ba3fmd7n3AMRb_PbRc4TbMJCiZM1weh3wV7Oy1QtB7SfJEKWRaBKOV7CXHYfM2LktS8vdFlw9ow-Hxa_vKbpeS46thcwE8zqDNLuC15Dq6zBrumT8Hrv7Mzv8eHgWRrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ مجاهد به مرعشی: ای کاش به آمریکا هم بی‌اعتماد بودید
🔹
معاون پیگیری‌های ویژهٔ دولت سیزدهم در واکنش به اظهارات حسین مرعشی دربارهٔ بی‌اعتمادی به چین و روسیه: با وجود فشارهای اقتصادی جدید آمریکا علیه ایران، چین به‌صورت رسمی مخالفت خود را با اقدامات واشنگتن علیه ایران اعلام کرده است.
🔹
روند مبادلات تجاری میان ایران و چین و همچنین فروش نفت ایران به این کشور در اوج جنگ رمضان نه‌تنها کاهش نیافت، بلکه افزایش یافت.
🔹
از منظر غرب‌گرایانی مانند مرعشی، اگر آمریکا صدها بار حتی مدارس ما را بمباران کند و مجالس عروسی ما را به عزا تبدیل کند، باز هم واجب‌التکریم است.
🔹
اما اگر چین و روسیه در مقابل آمریکا و اروپا قطعنامه‌های شورای امنیت را به‌نفع ایران وتو کنند و در جنگ به ایران کمک کنند، همچنان غیرقابل اعتماد تلقی می‌شوند.
🔹
ای کاش همان اندازه که به چین و روسیه بی‌اعتماد هستید، به آمریکا و اروپا نیز بی‌اعتماد بودید؛ سیاست خارجی نیازمند نگاه متوازن و مبتنی‌بر منافع ملی است.
عکس: ناصر جعفری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/459687" target="_blank">📅 11:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459686">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‌
🔴
قرارگاه و محل اسکان فرمانده آمریکایی پایگاه علی‌السالم، آشیانۀ پهپادی و رمپ استقرار پهپادها به آتش کشیده و تعدادی از عناصر دشمن به هلاکت و تعدادی از پهپادها منهدم شدند
🔹
روابط‌عمومی سپاه پاسداران: مردم شریف و کریم کویت؛ شب گذشته فرزندان شیطان که بعضی از…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/459686" target="_blank">📅 11:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459685">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/487dad76d1.mp4?token=qSj1Ck68bEZF_ujItLCUNucXpQoiNQKUwOXuCV2QvAEoc5bXfKRjyAdwCgmsUn7xVMEXeAmcjrh2ZUXjvmz82Y5PhwKDS1ttQuRjHDAg12yExP8FHP7jRYZftHIfl0yDNwA8TUSoeaxly6LciJMm9tyGrpme0yqvl4M3TJw1tjID7a047ug1lsaMAblCZ2vCk_Yt4BVjBo0riSTGGNueQRNyQGIj_sK7QtdcYwpvYV5ZGK5c_eeCfvKhOn3bRfDSf2Z3QXirHRpo7L5pwUpp5uVnxa9KJAI04ly5PbvNttZD4Xm4ZsV4CZAL7QsgNO6t3yTke7GAmRxTSya0tbxPUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/487dad76d1.mp4?token=qSj1Ck68bEZF_ujItLCUNucXpQoiNQKUwOXuCV2QvAEoc5bXfKRjyAdwCgmsUn7xVMEXeAmcjrh2ZUXjvmz82Y5PhwKDS1ttQuRjHDAg12yExP8FHP7jRYZftHIfl0yDNwA8TUSoeaxly6LciJMm9tyGrpme0yqvl4M3TJw1tjID7a047ug1lsaMAblCZ2vCk_Yt4BVjBo0riSTGGNueQRNyQGIj_sK7QtdcYwpvYV5ZGK5c_eeCfvKhOn3bRfDSf2Z3QXirHRpo7L5pwUpp5uVnxa9KJAI04ly5PbvNttZD4Xm4ZsV4CZAL7QsgNO6t3yTke7GAmRxTSya0tbxPUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اسامی شهدای حملۀ آمریکا به مراسم عروسی در سیریک
🔹
محمد ملاحی ۱۶ ساله، زرخاتون طاهری ۵۰ ساله، کلثوم ملاحی نژند‌نیا ۴۳ ساله و امیرعلی کریمی ۴ ساله در جریان این حمله وحشیانه دشمن آمریکایی آسمانی شدند.
🔹
۶۸ نفر نیز در بیمارستان‌های میناب و سیریک و درمانگاه…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/459685" target="_blank">📅 11:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459684">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMWPZvyCuhVYX-tKbOhFf6q-M7_yCaY861eZPyiO4gMXxPexr3v1dbTLP2eHgiVsYn7pBSRAnOcmpN1K0twGtrdTAL6LozKDRB6YMH0XOKnY0A5-dvQFZdP167p28M-EBepaukrEhNfdlePY4ixZvYhHPoQ625tgmPp6xkUYsimUrYmxpNZfSVUf8bcrCFl3nZQhXR9whZJ8bz1IHwDzI9oCqF_jNIAjHwYPCx0v170NT0O3th2wYIwtS6r2fpCgeTQCi3B-DLk_-6nluEWPzNZ6xjN6t34VMl6KQ1gl-YZv4AE6kqo6nJjxb_ymA44IqQAwQvtM46v5J31Zh1tJSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رازهای ناگفته از خانه یوزپلنگ «هلیا» و ۵ توله‌اش
🔹
روزی رسیدن تعداد آهوهای میاندشت به ۲۰۰ رأس، آرزوی مردم و محیط‌بانان بود؛ حالا اما شمار آهوها در این پناهگاه از ۳ هزار رأس گذشته است.
🔹
وقتی در میاندشت حرکت می‌کنید، فقط آهوها نیستند که در دشت دیده می‌شوند. این منطقه زیستگاه حدود ۳۰ گونه پستاندار و بیش از ۱۳۰ گونه پرنده است؛ از کاراکال و گربه وحشی گرفته تا هوبره و عقاب طلایی.
🔹
با این حال، در میان همه این گونه‌ها، میاندشت یک ساکن ویژه هم دارد؛ یوز آسیایی.
🔹
«هلیا» یکی از یوزهای شناخته‌شده این منطقه است که همراه توله‌هایش در همین دشت‌ها زندگی می‌کند.
🔹
با وجود این تنوع، میاندشت همچنان با تهدیدهایی روبه‌روست.
🖼
اما فکر می‌کنید پشت زیبایی دشت میاندشت چه خطرهایی پنهان شده است؟
در
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/459684" target="_blank">📅 11:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459682">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/syqVyOoXV4KzL1htPdfULaf-goYFxW1FqMBqom3AItTfAPiwIsVDYzBArLHwvideceGz3gfVg92DbXmMIZi_d_EbOZ6T8L3KMhKLGEHcvDEnIVLo18uSEZpTcw9rvhhCXm3oaJH21BcSzn332Ne8Wl4vKOpQw4wBNJZp-DRpimI41jkkgjRBbRSpmM9YfJkvoDu7cN7YGdxEsNwZnzexC48DHq31Vmbzh7139U_DAamMCacTcNfKtlbezHIowhgThpmu6-eQeQ_8Tw6tjPrY7QGuKjqe_JRWP77JYnT6LDGyVGhLfdFMIPJerCeuodaj9Ai2Q_1iyAzc8r2JnQtSrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7TTzxNhEl3KtQ2e7DsyR-AFO4ZBIJBH4-C5mGXpTI57nbXBq6vFSl5ezMzk55ZkR5NkchkKeiPI2fpeUKSe9le-yn414m5Ikxdw32FxrmIBIqe0RPJru2vbSB0tYlgtfwHUhfJctraxNg-0lxTe-3soGKaLyokgymRLO4b0VhfS_EBtKZ4hxHDj7x3I-e1Vg6RzB6UD5cnYPPFLrTNF45hAwgKFg2skxZEM24MINwMWqhqbKQbm1N9RVEnuj0oXBqqGQqZTLcuCzlL88A4mDGQMo1GpxuW8a5rTLg7n_ftZ0ZEeGI8QYalYcF5Iwgj5tCUatlaTekreqpM2hcgpeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
پوستر پرسپولیس و استقلال برای شهرآورد
⚽️
دیدار ۲ تیم ساعت ۱۹:۳۰ در ورزشگاه نقش جهان اصفهان برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/459682" target="_blank">📅 11:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459681">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تخلف بین دو دوربین غیرممکن می‌شود
🔹
دوربین‌های ثبت تخلف فعال است؛ مدیرعامل شرکت کنترل ترافیک تهران می‌گوید تا پایان سال ۵۰۰ دوربین جدید هم نصب می‌کنیم.
🔹
در گذشته تعدادی دوربین در بزرگراه‌ها و معابر تهران نصب شده بود که برخی از آنها خراب بودند.
🔹
امروز شهرداری اعلام کرد که تمام دوربین‌ها درست شده و  ۱۷۰ دوربین جدید هم برای ثبت تخلفات رانندگی نصب و ۳۳۰ دوربین دیگر هم به‌زودی نصب می‌شود.
🔹
دوربین‌های هوشمند جدید قرار است متوسط سرعت خودروها را محاسبه کنند و اگر فردی در فاصلۀ بین دو دوربین مرتکب تخلف سرعت شده باشد، این تخلف نیز ثبت و محاسبه ‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/459681" target="_blank">📅 11:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459680">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31ad7edabd.mp4?token=Hnvq5ggkptYcfu8A3g9phtRugfwrLFmCGMCiiRwg6NXy9fN15hPzvTRyLUaUYJJQWSkjOXYAm3sQXQXFGXh4O3MGAEaEv5a7l-CV7YmnpQcu5MS8mLlNls2QmntYbHMhZCOmBMw1mUV6lmxCDtVp6foOoCymdxWejuJhR60herKNr_E6bCaqUw2PE5u2RVobdFHZNwzYZLNjyY96P92KiZ45JNqlqtPZ-4K-4EfCbSsFO9QNZG06GVSh5p0xHhv9SZh-5gZLZRAXnEYvBE7NZqdY1eVb1p0K7P9rWtCl2QloA54WxJB43Hb2Zeyv_KJtsBsqTp8iXMOI132KUrOg0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31ad7edabd.mp4?token=Hnvq5ggkptYcfu8A3g9phtRugfwrLFmCGMCiiRwg6NXy9fN15hPzvTRyLUaUYJJQWSkjOXYAm3sQXQXFGXh4O3MGAEaEv5a7l-CV7YmnpQcu5MS8mLlNls2QmntYbHMhZCOmBMw1mUV6lmxCDtVp6foOoCymdxWejuJhR60herKNr_E6bCaqUw2PE5u2RVobdFHZNwzYZLNjyY96P92KiZ45JNqlqtPZ-4K-4EfCbSsFO9QNZG06GVSh5p0xHhv9SZh-5gZLZRAXnEYvBE7NZqdY1eVb1p0K7P9rWtCl2QloA54WxJB43Hb2Zeyv_KJtsBsqTp8iXMOI132KUrOg0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس جبهۀ مقاومت: خبر قطعی به دستم رسیده که در حملۀ دلاورانۀ سپاه به پایگاه آمریکایی در اردن، تعداد بالایی از سربازان دشمن مجروح و کشته شده‌اند
🔹
حسین پاک: بالگردهای آمریکایی مدام در حال انتقال مجروحین به بیمارستان‌های اسرائیل هستند.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/459680" target="_blank">📅 11:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459679">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWjMc18126X2Myyygzj0gNFGwtJ9WLVt8f6wsCddwAsHLymbWJ-JDLg_63Vb21KTEqy4z81AzMmHP7vZ2px8nO0IP2iCj2lpSKYaOrnvV0SplDmYnpVxGydw79BBI8cMDqT2t8Cy9rs4ObhcnsxETOu-FE3mleC3LKaVMuU7iXukbNi1lnlWteBw8PeP72IEzkDSXWrtTjKXtF2U467yI3zU-Nk8YlrUx1YOHczgE3pV199lnOhnhU60QX7pgPP8wkChQTMOyzNfJWuNYUC6Gs5uSRLBhydAwrFYYylbLxFyFKpHAxGGP8lHuAUBQXM6wzp3EYRpKOafGvll73p63g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: تمام اقدامات آمریکا به تقلید از شیطان و خود آمریکا شیطان بزرگ است
🔹
رئیس‌مجلس در واکنش به حملات شب گذشتۀ آمریکایی‌ها علیه مراکز غیرنظامی به خصوص شهادت جمعی از هموطنان‌مان در یک مراسم عروسی در جزیرۀ سیریک، با یادآوری جنایت این کشور در میناب و لامرد، در متنی به زبان انگلیسی در حساب شخصی خود در شبکه ایکس نوشت:
🔹
مدرسه میناب: کودکان قتل‌عام شدند.
🔹
سالن ورزشی لامرد: بچه‌ها سلاخی شدند.
🔹
عروسی کوهستک: کودکان همراه با خانواده‌هایشان کشته شدند.
🔹
اگر قدرتی مثل شیطان عمل کند، مثل شیطان هدف انتخاب کند و مثل شیطان بکشد، آن قدرت شیطان است.
🔹
اگر همان قدرت، شیطانِ کوچک‌تری را که دقیقاً همین کارها را می‌کند حمایت و سپر کند، آن‌وقت خودش «شیطان بزرگ» است.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/459679" target="_blank">📅 10:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459678">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شهادت ۴ نفر از رزمندگان هوافضا در کرمانشاه
🔹
روابط عمومی سپاه استان کرمانشاه در اطلاعیه‌ای از شهادت ۴ نفر از رزمندگان جان‌برکف هوافضای سپاه استان کرمانشاه در حمله رژیم سفاک و تروریستی آمریکا خبر داد.
🔹
اسامی شهدا: شهید رضا محمدی، شهید شهرام جعفری، شهید علیرضا شکیبا و شهید جعفر کهریزی.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/459678" target="_blank">📅 10:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459676">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4Etg0PKUDcA8fTs9w1p5hIOECY6iSkzxmDwqkuAbFz-oUGkyjR8K2G1PhBlvw-7qqLD-pd_JAUMSVzwM3oVPmESMCDQZUnMZJP7n2XvadAj_k-vMAfvZHSDi82ceP2FZHhNV80oZCHWvDXRZquSDMG7i2ZorWcrcC6QWhFAp3jgNO-_bvudpw9thNXiENEPfB2rxxKYYqAM2zF_5OaM3_djl0zzHn4MgeLf_Ew0v8n_y6SVTrYf2_TpOGnJDmk0ZlrIA0jlhK-FKr-Ipy_MYeBqS3QLuhM1Wwsnh70nvzdLXhHete676l48zNQJHj9sujhw0oUcooC1J7no0ULChQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔶
رکوردشکنی مجتمع فولاد بردسیر؛ تولید فولادسازی از ظرفیت اسمی عبور کرد
مجتمع فولاد بردسیر در ادامه روند رکوردشکنی‌های تولیدی، موفق شد بالاترین میزان تولید یک‌ساله خود را در دو بخش
فولادسازی و احیای مستقیم
به ثبت برساند.
🔹
بر اساس آمار تولید، کارخانه فولادسازی بردسیر در فاصله اول شهریور ۱۴۰۴ تا ۳۱ مرداد ۱۴۰۵، با تولید
۸۸۵ هزار و ۲۱۲ تن فولاد
، رکورد جدید تولید یک‌ساله خود را ثبت کرد؛ رکوردی که با
عبور از ظرفیت اسمی کارخانه
محقق شده است.
🔹
در بخش احیای مستقیم نیز تولید
۹۱ هزار و ۶۷ تن در مردادماه ۱۴۰۵
، رکورد جدید تولید ماهانه این کارخانه را رقم زد. مجموع تولید احیای مستقیم بردسیر در این دوره یک‌ساله نیز به
۸۷۶ هزار و ۵۳۷ تن
رسید که بالاترین میزان تولید ثبت‌شده در یک دوره یک‌ساله است.
🔹
ثبت هم‌زمان این رکوردها در دو بخش فولادسازی و احیای مستقیم، نشان‌دهنده
بهره‌گیری حداکثری از ظرفیت‌های تولیدی، افزایش بهره‌وری و تداوم روند رشد تولید
در مجتمع فولاد بردسیر است.
🔸
این دستاورد با اتکا به ظرفیت‌های موجود، استفاده حداکثری از تجهیزات و تلاش و تخصص کارکنان مجتمع فولاد بردسیر به دست آمده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/459676" target="_blank">📅 10:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459675">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofkiLCmm4OV_CFiVL0MMoWvXdpQMlhnN__ZLOlmAiJagISEd_WhxGz7ryeXoTaga1Ut-XipScuqF-wZwvSrbupw26nszXLaeKE1o6NVFoxIORQLMaRdbzyYuw1BaGZU8z1xoDUviHYYmQYuDBcAtV23rIx_pRpIcTKhXbvfbtw3tZ-xVI5fddQUKSW9N9IkHwsK7JNIPyqzTlVl1waT66urlNLkqNDHiFKxyr7D0I583gwXdbNLkj-vp8xbYgla8FQwv7Ukvbla9ZALAayyLnKW-Qip39lLVhaRQNTjhUJTGAmGE9Wb_YXr3CcKm6WFuoYdbUWQcEaaVUD9rG-WGdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
رونمایی از کارت اعتباری گردشگری ریالی و ارزی بانک رفاه کارگران با حضور وزرای رفاه و‌ میراث فرهنگی
🔹
در راستای رونق صنعت گردشگری و با هدف فراهم‌ کردن امکان دریافت و استفاده سریع از کارت‌های اعتباری گردشگری ریالی و ارزی، بدون نیاز به مراجعه حضوری، سامانه صدور آنی این کارت‌ها، توسط بانک رفاه کارگران رونمایی شد.
🔹
مراسم رونمایی از این سامانه به عنوان نخستین سامانه رسمی صدور کارت‌های مذکور در کشور، با حضور دکتر میدری وزیر تعاون، کار و رفاه اجتماعی، دکتر صالحی ‌امیری وزیر میراث فرهنگی، گردشگری و صنایع دستی، دکتر للـه‌گانی مدیرعامل بانک رفاه در محل این بانک برگزار شد.
🔹
این سامانه در راستای تسهیل پرداخت‌های بین‌المللی و پاسخ به نیاز کاربران برای خریدهای اینترنتی ارزی و ریالی، پرداخت هزینه سرویس‌های آنلاین و استفاده از خدمات جهانی، توسط شرکت دانش رفاه پردیس از شرکت‌های زیرمجموعه این بانک در بستر پلتفرم Payval راه‌اندازی شده است.
🔗
متن کامل خبر
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/459675" target="_blank">📅 10:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459674">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/459674" target="_blank">📅 10:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459673">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMPvJYU8LX-if7qs2I3ApbbodLU80LP_Scaokb2qHeJFOc8Pc3mpbl4YfZH3HXtB5IiA8bkFkUKv1ZAQlehdNlExvt0wT60tFlnLWRz727Xqa1WMrwivqFFPBgk1ncLwxZeYuxavj9xNa2ucfbIoxsrdHBVUqvM5whZiVkToc2Yql2dQhXDqU-24u0Z_Kh_RcVUdOdsROEfDpE_ihokE6MsBk_UPlvasHEX2pjGB-SQIfavISguepeHqv3nQQVNPVz43WP9jZ_IRSPCR-lNs_4aoKjdPFFhRrX5nTaFQXnjdMRRVNVbfIKE3JhU9u-DrQNe-MHiOTwXvM1iTZpu4iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
بقایای موشکی که دیشب عروسی سیریک را به خاک‌وخون کشید  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/459673" target="_blank">📅 10:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459672">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac604a2ddb.mp4?token=GS4S-RuSFpQL5U8kN1FYDXOBUlFXIUrFptdvDFki-xh1DbA7oqieZ94r7rXj0cf764mfSMB7wUIYGtN1hVZE4tgH7NjyI7wibs5f3jGmcNeRc8TOqkic2ZSpPeWJ_XR12mFwor47mqMUg5UbNfxlCvsDTk3-m2cc_uXdR0a-9MwUHVbA96rTOOcsE8zaHyaQQtSXWu8rSEfBylIsZV6YfLh5DEF2qzoTZzfkiKeyF9xnLyFKTNaH1KjYFolKvcTFr-EtzjueESD-itNuF2CYJ2F9t0E6WC3_15op-j-EFXNN3wC3Ar-BkTD1qj1MPqGvrAjG6Cf7oDPTI1vTR3fsXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac604a2ddb.mp4?token=GS4S-RuSFpQL5U8kN1FYDXOBUlFXIUrFptdvDFki-xh1DbA7oqieZ94r7rXj0cf764mfSMB7wUIYGtN1hVZE4tgH7NjyI7wibs5f3jGmcNeRc8TOqkic2ZSpPeWJ_XR12mFwor47mqMUg5UbNfxlCvsDTk3-m2cc_uXdR0a-9MwUHVbA96rTOOcsE8zaHyaQQtSXWu8rSEfBylIsZV6YfLh5DEF2qzoTZzfkiKeyF9xnLyFKTNaH1KjYFolKvcTFr-EtzjueESD-itNuF2CYJ2F9t0E6WC3_15op-j-EFXNN3wC3Ar-BkTD1qj1MPqGvrAjG6Cf7oDPTI1vTR3fsXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عامل درگیری در اتوبان ارتش دستگیر شد
🔹
در پی انتشار تصاویری از درگیری و ضرب‌وشتم یک شهروند و تخریب عمدی خودرو در اتوبان ارتش، پلیس محل اختفای متهم را شناسایی و در عملیاتی ضربتی او را دستگیر کرد.
🔹
متهم در جریان تحقیقات اولیه ضمن پذیرش اقدامات انتسابی، انگیزۀ خود از وقوع درگیری و رفتارهای هنجارشکنانه را عصبانیت عنوان کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/459672" target="_blank">📅 10:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459671">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiwgawsUN3kiVB0BthbFUzANbJ79LURoLG82yLnA16ZQAQs62Gt03xAZ0cy5V9fpENECH9H019MVC9GsP0kmiyShT-w05G43w59lPL5h7kAk4UMC5AVnQB-Q8HSDEbcoxXwFtwmFh6YjxU7FX6hMz0B2SwIXxMdLZ3V3AxuoaEzyv_meq5ialvKx-meiNtxGsRNKVNPj4AqruUqfZT93DjfuNyLZYu7WMQFef46J5rH0tRMYR0uVikOJr1-hLafM5vfPer9egnPeugwQjV3suRYJpZIA6MZEIy47HfkLjeikORbk6goxyKA4CBJoeoyz-EbKf33GlRAPiSG-_1OFOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌‌ جزئیاتی از حادثۀ خونین بلوار وکیل‌آباد مشهد
🔹
رئیس پلیس راهور خراسان‌رضوی: این حادثه زمانی رخ داد که یک دستگاه خودروی هیوندا در مسیر غرب به شرق بلوار وکیل‌آباد با سرعت نسبتاً بالا و غیرمطمئن در حال حرکت بود.
🔹
این خودرو با یک دستگاه خودروی چانگان که در…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/459671" target="_blank">📅 09:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459670">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbhYjTna-yZ0GPYKmHGDffGmV0jeEJk68lazKkEkcxy8zgKHOJ3aUjaknKKKp02dtPOK5fsT9AZncu9G49uz_KZlIeW9PrHO4tzjc0dcar7o3joFyoFmLYnkOqB32cLvrESjvVWVN7drJxD7HWlum6ES8xPCKuBl0mPshsrQ1U0WweDNEERs4_OcOXBFYOtE0raNfpOxjfz4gnDS4icfnj63v9UCllRxBVQxijKSyE-gSpP16vhRRv52ijUTbpbIYEfTeCtTvUS1goh7ryTnz8E8yxmjI9oN3TX9eQ5-eTSmQyBvSUUABUilre_14d9nvpx4RLtTLdzD88h75xddZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/459670" target="_blank">📅 09:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459669">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adbfffaaa9.mp4?token=OhDMfDimzUn1dyQM12Ai0PDi6Q7hK27-s9YpPpYttTXXnfHVbwaAR-f3--o2q9FlE2_eZQRPZ3-Mf2sjrX5Qn7cdyGq_8Bx6GO8fXI8xZndqdx5x2WkDNCetjN67SlCXxzS1yNAia2zyCHSz467rBEbO9MuUXIfr8HlFebW6psiUXZgGKybOQipziwbyyfnEiC4xf2eoWTImPX3d26k1P1fNe1a8LP4RB5YmIARpp3O6qdtBDGLviVAimIjA7np1NQSaReVdxjOPqDtbn_5S7D-ZwRrMMYouQlCZmo1sUvYQL-GwC7g9OJiikBIuuvznzdxCi6LPDu5kqcGLwiL6yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adbfffaaa9.mp4?token=OhDMfDimzUn1dyQM12Ai0PDi6Q7hK27-s9YpPpYttTXXnfHVbwaAR-f3--o2q9FlE2_eZQRPZ3-Mf2sjrX5Qn7cdyGq_8Bx6GO8fXI8xZndqdx5x2WkDNCetjN67SlCXxzS1yNAia2zyCHSz467rBEbO9MuUXIfr8HlFebW6psiUXZgGKybOQipziwbyyfnEiC4xf2eoWTImPX3d26k1P1fNe1a8LP4RB5YmIARpp3O6qdtBDGLviVAimIjA7np1NQSaReVdxjOPqDtbn_5S7D-ZwRrMMYouQlCZmo1sUvYQL-GwC7g9OJiikBIuuvznzdxCi6LPDu5kqcGLwiL6yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اسامی شهدای حملۀ آمریکا به مراسم عروسی در سیریک
🔹
محمد ملاحی ۱۶ ساله، زرخاتون طاهری ۵۰ ساله، کلثوم ملاحی نژند‌نیا ۴۳ ساله و امیرعلی کریمی ۴ ساله در جریان این حمله وحشیانه دشمن آمریکایی آسمانی شدند.
🔹
۶۸ نفر نیز در بیمارستان‌های میناب و سیریک و درمانگاه…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/459669" target="_blank">📅 09:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459663">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KLANrhxEGrZN4WOSik1-QhsIfe5x905azU0gVnhadvN3yfbZ5hxd-2_Xq-nLLtQduRB-HfpoTO54McyT2r9gOrhAQ6vIcN8gyyt90ZbZvuPv-c1TJZ0I4Hi09aUmCsS5S7knmFQZQEVGGJ1nItD9s2B9oIbLI4t6k5hNOXtT1yriDx1LFTJvYXCr7fFt3JCilfxlv4LP5TanzMHLRR9lxSga9abAD-mfP1z416z0H2NNxGsaC_pJivryADJ7bQORxaheTA5q2hmy6iybnIowuP7dxdF_NlsTNm5qZGdl3zHGgB3c4Kr39m7WmkoXLP7mi0oEMPlXqmtleObS6Ntb9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/voeObhCYqgkKrjscodMrdP5ZRzeq-qEhze956eT45RQVeEZXO3VgqMHsulnC1K9ghiIefgXd-7Aa1BeDCGSXqAoAKN83gRIghvPbF5WkrVr-QpduN9MPzS5cj4kSMRBa1YOrUxkWUKf4jgnvqgepJ1fiLIhf0KvppcJQk_ZE65J4_DSlnHkHID-5jaYGcN0sQO1mI-BFkVfMSlDKcgyqevP_K7sWeHxzthe-tTErJwyrxSH7HMKM4to--lD6cbW-lwNuY7vkPJhNtw3XG1dKzl1wAEbYejv4Hjs5JA9idsOBdOB0yLjzIHn9WVCsw8jGyNDu_8WCwhMLCI-qUz0Qtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qkqNTugr0gQJtrMgSvyXvMHPw1up3fpthbZVkRB5OlgT6c1uYpwK1Z7XFKzyjRrHJrv3m82LyFBGD8HB6rzq9bZA9ZFIBNMBkpD9Ra3OF7iMBh93aZYnkr7rG3z6nwi_Q4tInK1sCaewKYNeqWqqyykZN79Y19txqSJmJnMU8yOmefNdv9mDKbVgfG-WssRCLdutGAeIAg6wpZojuo7lAKdx6t-cIoIU4ZvWAEVCCyB6mJEq9P7hm81bzZ_MaZMC0uKcYm-8FLFyCyGuMt3t8XZcbrcroqedlMeiJixXXdwHWlysJ1qCN_WT2avm7flhu_7L4Ji4-eJDTAn96-p5lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcWHy2520MOwCUPmIjGcbSdEDTlQKD8fyxaJ0Zd0OHu_GGk7MeJCIZzFX3NgjhVfL0jwE8I90Z30q5gA-04hguohAkR_bmD2KNeSW66dWblpmO_zB88ypCueSAx0wRP-P3uoR-sT7w2v1WygPucfUoiQO0-ov2kq3Q9R_Fcizq1hUKokaGg4gkIYOTNsn2U1mUyYO9T5A6a9mempJSZD46LVsDO27acrdmoPBrgtjL79UHf4IrqGHdbzMN9utcZMsr8ffLbZaw_9o1o6Y98H6vC_XT9EKYy3YhIlPUu6fPhfMgcM212oc-C5z88WKYGspHVG7K2xRwK44L8bQp9qDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rcSYHVITXPsMXbPy0mKMIORPLKy32lVDYFJjgzKWQjnIROfnj8u2j_sJlLqrz8LbuQDn7g6heLk7cQiyeRabrsEeI38lJOc1t3iG8o6_8lYR6bIYflkSdpcaxKR5mtQT6Yf3f5sWQy_G_IO0-zUJdxm2xBjP0UKadIYDZilFpzgK-2lw0CKFWsEAwR-Hh_ywIP4b_RbhIuL4hoTcd0BCHFWVWogaELj4VYlw4Qj2-adS6KLHSRs1OUnOOEtcXMnQX3-WuIJ7ML8smLr0-qGMtTOlz93XO9RBoIAb4REgh0DoCfPLCn3VpYuY6-vH07aiDmCoyk5ryimzJwr32XJvtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kCFQHV8n9OovI65zI89eY6pO1dErk7mPqfz5jjfJAiI_j1Uj6Uf7x_YZ096ngjuZPbwEZ-kVCI6i-Q_dMmwnqoLJ8QHo9mvCfVjAeG5BMkUQwqCbl3FlfSMPU7yXvBoAgD2Sh8zzQLVtwzJRdR07vAY0e8xvKvG3uGd0MmU-UJr_yM7JvtT6zvAIcHM6O0kDWIPbIoGHIFt8hcMNQVLFJFYn_QMkjcjYCLmosG94aWdJFLx2XPFF1Ux44RB0BXKbrZhcRNyCbaPv4AhP4TPaLKOZ3IhLjIgwutp07JSaWS4_PgkQlGY7Kaf0ioog8EMWVl0ToF8SQdfhUJW3ZhRcJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بقایای موشکی که دیشب عروسی سیریک را به خاک‌وخون کشید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/459663" target="_blank">📅 09:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459661">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmOKPS1xG_akRrku1YIwsDIG2RKPRzZpWE3uL4TwVYRl2vSv8TWT-FMjGEgOpwkkGIJ-2WlUtvFwqVhJv4k_1A9OQuRi9Wo6mRVd_w0eSyZmrI8_UT-dwg7h_4Bh5L8e8UTj8ShcvfZ4B4tOkTjJxfSs7DaG1bAAGHMu-2b4HMdpmqUJGzqrpq_A63fwPDLy0HsnghYkJK552NUP-MGTxMZ3gRTO_sT3GdDZp0mDdAEPJD9j39OyNBOcuqf5NN3zLbkBAXCVxUSKPSIURhwo30Q2SedvdysWokiZDr9pc2fXBSYhtcq93Zf47sWY9X0eVuQTRuZohuNBpmEaXpuE4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85a443f91.mp4?token=PA7A6mPq2zekb3taZxHPPentvEwkg1H-Mlg4tMPGP4euEbtcgKajXxa4LBsd52AuJdamMMAVxLZ-LAaYPNqEHmAz-lpuC4e_3QrLmxJa7SfTPHnUJrcRi9jvwP_zuhfeePqRpMMxUQbYfiMBKat74SD74_gI6Jha5JvxzMeHpi1q2rg4Ino50LezG-cdd67A47PQLT02xlijhBVYru0hYuuoqI6gRqGGnwNExDpVQK2hLy_xyFJvYdh3cYGX_3zBY1E1asx-S3oKE5WsKanqNcEZCQg-bVm6t3PPmiVj3WAEJyELB5NXauNKRbZ1DwQyJT-5nzygNwOuPK-bPL_Xcbf6obtHAymecPZ5qEgc1-s3IfcsHz6Z31nSAWgDVN0kjzDjcus7yH-Oph_VpdD7_bUGzG7ElQPVPEp2J9IOHUscGfDpmWYGAKRTJUrXLukegmCiPYREr2Qka89HbBuToLJvWBVPdSrX5kteANUv0a2Yo2KEVkOgFcIbhNccB_shbT1jdddw9Lc3nQuibTf7ca_Q1729p173m4NqAapd52RzftlHAss8MTy89lw3m_lT6d8MVIB0cWPFnKnmDTVM6TrxePYYbUrG42yy7XVvqDtcY4yxHwKh9b4bAagG0Kjh3jdj4YmY95uM1s-Rr9YRJ2HMUboEP0ZMx7J8fRErTFI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85a443f91.mp4?token=PA7A6mPq2zekb3taZxHPPentvEwkg1H-Mlg4tMPGP4euEbtcgKajXxa4LBsd52AuJdamMMAVxLZ-LAaYPNqEHmAz-lpuC4e_3QrLmxJa7SfTPHnUJrcRi9jvwP_zuhfeePqRpMMxUQbYfiMBKat74SD74_gI6Jha5JvxzMeHpi1q2rg4Ino50LezG-cdd67A47PQLT02xlijhBVYru0hYuuoqI6gRqGGnwNExDpVQK2hLy_xyFJvYdh3cYGX_3zBY1E1asx-S3oKE5WsKanqNcEZCQg-bVm6t3PPmiVj3WAEJyELB5NXauNKRbZ1DwQyJT-5nzygNwOuPK-bPL_Xcbf6obtHAymecPZ5qEgc1-s3IfcsHz6Z31nSAWgDVN0kjzDjcus7yH-Oph_VpdD7_bUGzG7ElQPVPEp2J9IOHUscGfDpmWYGAKRTJUrXLukegmCiPYREr2Qka89HbBuToLJvWBVPdSrX5kteANUv0a2Yo2KEVkOgFcIbhNccB_shbT1jdddw9Lc3nQuibTf7ca_Q1729p173m4NqAapd52RzftlHAss8MTy89lw3m_lT6d8MVIB0cWPFnKnmDTVM6TrxePYYbUrG42yy7XVvqDtcY4yxHwKh9b4bAagG0Kjh3jdj4YmY95uM1s-Rr9YRJ2HMUboEP0ZMx7J8fRErTFI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصویر کودکی که آمریکا دیشب او را در عروسی به شهادت رساند  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/459661" target="_blank">📅 09:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459659">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SkLihmgA3BKTeNR2Q1x5uxHMm48qTIaZtQ0Fsru-c3SxKe2E3HpTvElBIEjQN_047iYIsStXdXsux4_ufzw082jmyeLLS9bqQQrqnlSQt8H-UPg5b3qzYaB0ZoDcUkpsmwMgkjQA0F8Uk6xw-Bniat2yyqFxUnqu3tn6uXRQxKNMpraZWDDpNYrGaBRyESQUv3WXu4kqt3in3oQpinOfF6C4zWzQJG_lWh6hFmwfQYSHdnFGFdDbtYnAV0uuWHSYGwtTkeNN7KOP4C2gn755bfto79KnBVqmf2M8LjjR9eETKvJf4uLXkAFeR0SZZHNmIc4ET6RqC-W-kqJzjJCx4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cq_gQ7yZFqno60cusA7M8T2jyxrTRh_bM4bDMq79W5mAQYDgpu-sTSTGiN2wd334fvThEjTSs3V653qjUqYoSe4QKBfJEbFr5F-CSlRj_RuNR4-IJ22fhAaw57GMKjITXX1Dgs0QhUirvZ9dZbO3LBe35HXFi-do5iEZF5edpRpHawYfp2RBnBzGaga6zkM13DKQdGxr8GB43YrxuAECDX2tqJbJzZFJykgpbYNeiSS02ffZLGxe0MLm6LzEV2_CXEryp55kTqlI_RWST3z9dsqxG6FSbx7bILKAOgZoKQfKrR7YnXwSa56Bdpj7vUIuvbVXWhfjlkSaeExhgT5tww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
عروسی که با اشک تمام شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/459659" target="_blank">📅 09:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459658">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea12086aa.mp4?token=f-UE7LFYCbXKcDJIN6ZlIDesmnPN5lUivbvIxoE8y1Wtl6ujpRa9-L7I3PVtuRXF_sPC2Xzj0tOfxkyfCx-84URXyCpNBlJTFNSP3v4-mNqL1eu2D_c5477v_BNj1YQ2Q502dLPQhYTCZ-_Ej4Y_hXqOt8vr-3gIlZSnIH5fqHP2wRv-KheouZVosp4sMpDUutXNVNiDl8-KDLRL6woafDLN9Yb9-e0PQbmIL3nVC0LI1o1DrtrVvPAXgKF4Db-QwAui7WO7n2MCtMAyLEJdtRSgiAFw45yYsNa6Imhmaz27lTiAdIfg0hZKRBeCLymsZ4hnuTBTAzhkry8bnfHJ6Qnuh5Q-8TdqqHcd_mZqbShmFlTG-QbpZrRSkAJ2GX2u4Fq8hcdds2b8u3CdrusMuos-i4RabDZB-BUb2h15VPS9tHgJDhT2fwLRu1cBYqGLWsLTyK5KH4EA_xipVbPv2R8HlF96OLX6d9HVNfPZjhmx28YKNuDiz7JkLXFb85AB6mPDIOSWIcppPQo6GvLKAiJRol45Bj3DYPA_OCgTwgGHlaSx_4V8ukxlDuG18mAsjb3HG1GgWLo5FLLkVJjGgnbO9v_HLSG9aVDQQPcnWjO9GLLf1JcAWyB4Xi1_YM45cpTiT24u3xNqh-BaHUKyj8XOXTbhvpl4nzIdx9NyQuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea12086aa.mp4?token=f-UE7LFYCbXKcDJIN6ZlIDesmnPN5lUivbvIxoE8y1Wtl6ujpRa9-L7I3PVtuRXF_sPC2Xzj0tOfxkyfCx-84URXyCpNBlJTFNSP3v4-mNqL1eu2D_c5477v_BNj1YQ2Q502dLPQhYTCZ-_Ej4Y_hXqOt8vr-3gIlZSnIH5fqHP2wRv-KheouZVosp4sMpDUutXNVNiDl8-KDLRL6woafDLN9Yb9-e0PQbmIL3nVC0LI1o1DrtrVvPAXgKF4Db-QwAui7WO7n2MCtMAyLEJdtRSgiAFw45yYsNa6Imhmaz27lTiAdIfg0hZKRBeCLymsZ4hnuTBTAzhkry8bnfHJ6Qnuh5Q-8TdqqHcd_mZqbShmFlTG-QbpZrRSkAJ2GX2u4Fq8hcdds2b8u3CdrusMuos-i4RabDZB-BUb2h15VPS9tHgJDhT2fwLRu1cBYqGLWsLTyK5KH4EA_xipVbPv2R8HlF96OLX6d9HVNfPZjhmx28YKNuDiz7JkLXFb85AB6mPDIOSWIcppPQo6GvLKAiJRol45Bj3DYPA_OCgTwgGHlaSx_4V8ukxlDuG18mAsjb3HG1GgWLo5FLLkVJjGgnbO9v_HLSG9aVDQQPcnWjO9GLLf1JcAWyB4Xi1_YM45cpTiT24u3xNqh-BaHUKyj8XOXTbhvpl4nzIdx9NyQuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بفرمائید قهوه یزدی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/459658" target="_blank">📅 09:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459657">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6c1dbf088.mp4?token=WW0ClftM6GUISpjLYyM47E5V0psl__axE7dIEoRMN30uWy2lWc8_6p2nn4wxBzAaTC_WiM_pUsDrYsbiflEkAqewGL1E4FFgD2ua5_rfc8Uc5fflGTFosbVgpdgqB3GpAOZbVWqK2iSOvc3AQ7PiugmGqy2vy1V6DfYNGmM4d0zea5Kh-rK5gBDI3Slt-on3dfocPvjfb8FpUJEqtr77oZ6Fad2S_0J44SAuIZx00pmjbL5wMNtWCZR2GBlfKlPQEeCFfsrVNRefb_2MQMXY1wR9ldxlqEuJxa52GnLnatQdg-RKJDPvgGyhCRcDDhEk7C-FXYUPGeFC4UTwW8K1sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6c1dbf088.mp4?token=WW0ClftM6GUISpjLYyM47E5V0psl__axE7dIEoRMN30uWy2lWc8_6p2nn4wxBzAaTC_WiM_pUsDrYsbiflEkAqewGL1E4FFgD2ua5_rfc8Uc5fflGTFosbVgpdgqB3GpAOZbVWqK2iSOvc3AQ7PiugmGqy2vy1V6DfYNGmM4d0zea5Kh-rK5gBDI3Slt-on3dfocPvjfb8FpUJEqtr77oZ6Fad2S_0J44SAuIZx00pmjbL5wMNtWCZR2GBlfKlPQEeCFfsrVNRefb_2MQMXY1wR9ldxlqEuJxa52GnLnatQdg-RKJDPvgGyhCRcDDhEk7C-FXYUPGeFC4UTwW8K1sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تکذیب حذف شارژ کالابرگ؛ زمان‌بندی جدید اعلام شد
🔹
معاون وزیر  رفاه: زمان‌بندی شارژ کالابرگ از این پس به جای ۱۵، ۲۰ و ۲۵ هر ماه، در تاریخ‌های ۵، ۱۵ و ۲۵ ماه انجام می‌شود.
🔹
شایعۀ حذف یکی از شارژهای ماهانه تکذیب شد؛ شارژ ۵ شهریور مربوط به مردادماه بوده و هیچ گروهی حذف نشده است.
🔹
همۀ دهک‌های درآمدی در سه نوبت ماهانه، شارژ خود را دریافت خواهند کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/459657" target="_blank">📅 09:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459656">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‌
🔴
حملۀ موشکی و پهپادی سپاه به پایگاه‌های آمریکایی در اربیل عراق
🔹
روابط‌عمومی سپاه: رزمندگان شجاع نیروی زمینی سپاه با حملۀ تلفیقی موشکی و پهپادی به پایگاه‌های آمریکایی در اربیل یک مرکز تعمیراتی و انبارهای تجهیزات فنی ارتش تروریست آمریکا را نابود کرده و…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/459656" target="_blank">📅 08:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459655">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf52083b1.mp4?token=Zj6pEeYN9f6tvI0oBno5EklWIwBAceZmZFslUnUvDS2kHVp36xrTaHRz-jFx4Sy7A2_0Mr9ESnKVJfILsXj_3ZxjhNknCmqeeRd-_eLTQPOR1ruZvj-IaBWGlajkalH5jpHrZ7cxHAWIrye-7dellGHxIpoA9ja0ndVQ7Q8JqP9Xt_drPoFh6iWMcJG1X6qv1A6We_x4u-WUxrjY3JkgbcGJJXkzn9UG2rFjp5wRt2EikcPTRpDHH5WqEBFmxrFF2swzyHwIpwoxymqlRQJ9qpvwP-w7D-BEkNsV9E86mB2k9Rrm4OzYgHbtFm4rG0_8kqKSCY5UspRPdO0ydM2GEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf52083b1.mp4?token=Zj6pEeYN9f6tvI0oBno5EklWIwBAceZmZFslUnUvDS2kHVp36xrTaHRz-jFx4Sy7A2_0Mr9ESnKVJfILsXj_3ZxjhNknCmqeeRd-_eLTQPOR1ruZvj-IaBWGlajkalH5jpHrZ7cxHAWIrye-7dellGHxIpoA9ja0ndVQ7Q8JqP9Xt_drPoFh6iWMcJG1X6qv1A6We_x4u-WUxrjY3JkgbcGJJXkzn9UG2rFjp5wRt2EikcPTRpDHH5WqEBFmxrFF2swzyHwIpwoxymqlRQJ9qpvwP-w7D-BEkNsV9E86mB2k9Rrm4OzYgHbtFm4rG0_8kqKSCY5UspRPdO0ydM2GEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ادامۀ حملات پهپادی ارتش به پایگاه‌های آمریکا در بحرین و امارات
🔹
روابط عمومی ارتش: در سی‌امین مرحله از عملیات صاعقه و در پاسخ به هدف قرار دادن مردم بی‌گناه، از بامداد امروز، ده‌ها فروند  پهپاد انهدامی ارتش، سامانه‌های راداری و محل‌ استقرار نیروهای آمریکا در پایگاه‌های الظفره و المنهاد امارات را مورد هدف قرار دادند.
🔹
همچنین، تاسیسات راداری و مراکز تجمع نیروهای تروریست آمریکایی در پایگاه شیخ عیسی بحرین، مجددا مورد هدف حملات پر حجم پهپادهای انهدامی آرش قرار گرفت.
🔹
پایگاه الظفره یکی از مراکز مهم عملیاتی آمریکای جنایتکار در منطقه است و از آن برای عملیات هوایی، شناسایی، مراقبت  و پشتیبانی استفاده می‌کند.
🔹
حمله به مناطق مسکونی و هدف قرار دادن مراسم عروسی از سوی دشمن، مصداق بارز جنایت جنگی و  آشکار کننده ماهیّت پلید «حقوق بشر آمریکایی»است و قطعا پاسخ رزمندگان ارتش به این جنایات دامنه دار و گسترده خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/459655" target="_blank">📅 08:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459654">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teQf6Yrhb11fR1et1gplpryQC7xolVi9GQkIXHPBxaGR1-2PFkY939o8kn1uVV7Rr8cZ1K4eIDNUzbBE-vJZ1jRkbIIdaBzYZC0Lz4USkAzYqaCcS6OzlkQ7JdjQ9277fIBtVmYFh5OO1j9j9W5fjyEc3A42P2_qyZc92DCkYye4pE841W2VMSQIYW8_Vt5-lwJ6ofdpsI8-9fReNYKp27KBMDTg-2Tc0ye8I9l0f3U3GSr8fJcW-6WwpP_xGUV_zFIbDa0rLjktCAuV6UZTQLNObI1pTbZaufrfAJhGiroQ5_3zcbxY3NcoUnR0AcT50g6DUVngunfs0cWtJnR-Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگیری کارشناس رسمی دادگستری اردبیل در حین دریافت رشوه
🔹
رئیس حفاظت‌واطلاعات دادگستری اردبیل: درپی رصد و اقدامات به‌موقع و عملیاتی منسجم حفاظت‌واطلاعات دادگستری استان، یک کارشناس رسمی دادگستری حین دریافت رشوه دستگیر شد.
🔹
رسیدگی به این پرونده در چارچوب قوانین و مقررات در حال انجام است و تمامی ابعاد آن بادقت بررسی خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/459654" target="_blank">📅 08:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459653">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biuyhGXr3LeeF0t3AK7iCh2-_ahAPy0xg2mDpkhIua8Yy1phkrqPdWcyboQ0yAA92_eJsHps3mYevUUDcWjUpq8MvPKjD5_yXeHCRRzTjgNz54skSOL4Nfa773rscZ9LUAfG0aUlnEeAWNoM-Hhb_rG4eEN__9UxdKZyZCmsSiisGMUing3DpPeN60ZbYoDpwTHohcwEEUarmRsX-p53K3flokHXCoBXs6x7gf2clJDnPjQSpl2_YUrlufNZXdSWixWSoX4yljuEhFq8o9j1-Q4RKgl_larowMgVuoBQaTZmncupYSTYmpkeXmIeBERhe3jn1S1Kid8v-YR451KN4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">٨ میلیون دلار برای صفر بازی!
🔹
سفیان الکروانی بدون یک ثانیه بازی برای القادسیۀ عربستان، ۸ میلیون دلار به جیب زد. او ۱۰ برابر درآمدش از کل دوران فوتبالی‌اش را در عرض یک ماه حضور در عربستان درآورد.
🔹
این مدافع مراکشی تابستان از با‌شگاه اوترخت هلند راهی القادسیه عربستان شد، اما تنها یک ماه بعد از امضای قراردادش مربی القادسیه او را در لیست خروج گذاشت.
🔹
حالا او قرار است از باشگاه القادسیه قرضی به بنفیکا برود و برای یک ماه حضورش در عربستان بدون یک ثانیه بازی دستمزد ۸ میلیون دلاری را کسب می‌کند؛ بنفیکا پولی بابت دستمزد به او پرداخت نمی‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/459653" target="_blank">📅 08:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459646">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n_3YvMVIYRbxPyvs5YyDfEAzGTQLQY_asYZbEfZrJNexoJT2_eko9n1Y_0bDtF4M4pAQrIGhpPjjGjAtUMoJmaA92i-CkdXejlfUizr8Urp3O6xaWXFqmHFdOJSrtW1huBYFtblI74XV_WiAb6UtuvWws_ruUmT2T1OvoimgdS5BL-f0T4gb4eHyRzNmz41iyrCyacH_uNiQ5bJXiqrA3S7SbT7jBbzkBNxuVJbzsDnOf_yHNTSuegPaV_SnbNDHFBcmPFMWxBUPHVMvW7KjhmvBNF9V4PTgOF1JHgB74Q5IjNcwOItssN39oHZK27ZVTrKqo6R6XrdwD4V2ZtZYgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R73toUoKKqDxdz4950OFVI5plRaVhTh4ZzI9LN7LkSPwbT8DKCUrSApb_ePgMlNhArHjcRm1PJM2__FKRTJiNq1FFIdV5vqkkOTuQ9UhvXUKfTSOc8VNld-jbKMa92eezr_bpsQouSdycw5LaH0ROHDTv_agPbANmrsRn9QsKyXCNWGPjzAAHG7dw27jhQybFczz9J7GmAl_dXzypIbS8Hr6slNbxRLqYpODQLYGm_5cGN_gzVB5GuzJYDK6Mk89AQT5fCVTu1ZR5Zf-O1erQH-UtYolJPf-o8CKWCrsCO5IABQdH68gYMx2ZPnQSG-mRvMuR4QW2Zwms4yPTL0WEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DK16b4o0Pmc-w6o8xXMXrj2aEV9x6uKNzD8lJcdTuzEZihugmPc8-r_mIxYvE5C6EBeaJlG7_Dx9Me4JkGfx94omHZmx8ET_i0KoaJYL92IifHsuzHN6cJxBI2j-ZWSjD3ed7UnEHsv7R9cwwBEYnZrpThOy2v8Co-YQK0dTbYmVxyXzHK3kFTwBEitU6GCyB_3WY9UGhcpLpsFjoFMtQkDKuVEmQLDvv_L9VS_3cNE0BSqB7TBUFSE_btIXxpPJ2jNw5RMYguZ5ReDahvphIOAGY4cUySFByAw4UWEARQel6F7cPpPqQmFceONWtM-64tfPzEG7Ph-m3sEUwXGLXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nm-KzowKPD3DkxTu4r_mgDktBLHpACEuZdMjH9b40YjpIB25g4DN7m1oS1pJbog7YHlHxOD9yT5FVAYm9Tg_NWV7Y0K-X_bzgxotGOrXD6D1ogaeizXA8S8ed_-dfj6jZe04eiwgfv7EARps3G-XpbLlCDLJ7Kdx6NzPIdcZOVQU5iqpeqvEbzR49LWUAwBlg5mEYF0Exdwg6OmntLbYzmez_l7WlltWsZl1q5PD5soA-vciQbQagYWqFXaBTHeq_TYreRtAlIdqeW_IFxtNlPPaEx-Rp4CYie2MZLfEr8nBi5xvtCaZXBn02EkFLiLt-WrA_CDUXKAduz-ugves9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dERmt0j9vcm1ByggOZBTZK68awuuZWnMToQ9jz2kNpcG1Na_BzPaPKzsM70-XU50VpOJSE7R1t2AbCTlzKj1n8Cp7YZumfEInTiYkh-ZM_U7vItD4W1j9HincTtAruNUoeZOk00yLrQmGrkNswKxjpy1pAap6nxdjCYKUyy4MmcUdnU91kCwXUwiFl3DYlFpg83Aifsu0XldQq_kr9AHlYgkUvSAqzQe9UhF1jpu0XjWazgZ71r8Pycyh6x7ssDI2YJkbdZ3HDTwIb1aMIasbtvRzLlBY7JL1FUeYAShc3DXBZqqrmOXa8sAILyXPsFG7DaMKASOkTiqlIhzG7-HHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t9CHOtDUieBD7bPWOAiJPPHHB1wCdqfcAkATJw-kbJS8E1v-GDost8XwcT9EXpnKBQTOHJxIfN8v97n64NTljkvkQj04_S5f8fuNfNoqIl-RhtZNH6HGrLuPOrOvg7B1Qm0Hri142xfxhpLKIGb-SD_s3NMwY58UwVmz3dcUxr-4oXqVi2SnRg5vYMUum4YMckavHYyKZlZDXeJx8Q1w8PJqiNxTQRR7JPoS-Nnxy00Tq1HBTIoHGQ1odQz9BEOSnLM5uCanWE2smd4oa6R_U9X4ctTlIkVrw50zoOdnUM3r7I_bFfp6g5nXa4wlRCvYOXl1uQWs0y3s_uyJJPrLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dyPkh3_cVgaXt1_Kinh9yNAnYpfo6wQMkdvPiL74--JnYc2iyP9qYINO1koUJjXY31-m1ClLZ1X56nyMMZi9SEQZY8HjsH7Ty_oGrmxdjOwyS69rjwI-cIsTQ-Aw5VYQLqy-a2Il9E65XDhA2GSHiv-m0oknj262vse5oZ7rzT4uPhKxFVjcuOrgeLSFrUHIPWtb0FwWQmN0bL4qiF9dMdL4qGlEh_njgyTuLSZ9CwMN98npLTAIyGHCT2M2xlpF4ZXM4PaM6lXpO02wbSInBdSKMcFOWvwqjsmCtvEVSNNOrG7azUReHv5Y5c-axPj4rD8Rl9AWh3hf_oUO2BorbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید اصحاب رسانه از زیست‌بوم منطقۀ میاندشت
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/459646" target="_blank">📅 07:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459645">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
برای ثبت‌نام دخترم در دبیرستان با مشکل مواجه شده‌ایم. با اینکه معدلش ۱۹٫۵۰ است و در رشته تجربی نمره لازم را آورده، مدرسه می‌گوید ظرفیت رشته تجربی تکمیل شده و آموزش‌وپرورش پیشنهاد می‌کند به رشته فنی برود. دیروز اداره آموزش‌وپرورش بجنورد به‌دلیل همین مشکل بسیار شلوغ بود و مادران زیادی اعتراض داشتند. دخترم آرزوی پزشکی دارد و نمی‌خواهیم برخلاف علاقه و توانایی‌اش رشته‌ای را انتخاب کند.
🔹
لطفاً پیگیر این موضوع باشید که چرا برخی مدیران مدارس خانواده‌ها را مجبور به خرید لباس فرم جدید کرده‌اند. مگر بچه‌ها سال گذشته چقدر به مدرسه رفتند و چقدر از لباس فرم استفاده کردند؟ لباس‌ها هنوز نو و قابل‌استفاده هستند؛ چرا باید دوباره هزینه‌ای به خانواده‌ها تحمیل شود؟ در شرایط اقتصادی سخت، هزینه‌های مدرسه، شهریه و لباس فشار زیادی به خانواده‌ها وارد می‌کند.
🔹
بنده یک سال پیش خودرویی را از شرکت سایپا پیش‌خرید کردم و در قرارداد به‌صراحت ذکر شده که این قرارداد با رعایت مصوبه ۴۷۳ شورای رقابت است. اما اکنون دعوت‌نامه با قیمت کامل و بدون لحاظ مصوبه ۴۷۳ ارسال شده و عملاً شرایط قرارداد یک‌طرفه تغییر کرده است. یک سال پولم را خوابانده‌ام تا با زحمت یک خودروی ساینا بخرم، اما حالا ما خریداران به‌شدت متضرر شده‌ایم.
🔹
مدت‌هاست عملیات حفر کانال و نصب فیبر نوری در روستای زنجیره علیا از توابع شهرستان چرداول در استان ایلام به پایان رسیده، اما تعداد زیادی از خانوارها همچنان به فیبر نوری متصل نشده‌اند و منتظر اقدام مخابرات استان هستند. از سوی دیگر، تمام کوچه‌ها و خیابان‌های اصلی و فرعی روستا که پیش‌تر آسفالت بوده‌اند، برای اجرای فیبر نوری حفاری شده و پس از اتمام کار به همان شکل رها شده‌اند. این موضوع علاوه بر ایجاد مشکلات برای مردم، موجب از بین رفتن بخش زیادی از زحمات انجام‌شده برای آسفالت معابر روستا شده است. با وجود پیگیری‌های فراوان از فرمانداری شهرستان و مخابرات استان، متأسفانه تاکنون پاسخی دریافت نشده است.
🔹
چادر گل‌گلی که بر سر خانم‌های متهم است، لباس رسمی زنان مجرم است یا چادر مقدس برای حجاب و ادای فریضه نماز؟ تا کی این رویه غلط باید ادامه داشته باشد؟ مطالبه جدی داریم که نمادهای مقدس حجاب در انظار عمومی این‌گونه مخدوش نشود.
🔹
تأخیر نتایج نهایی آزمون مهارت‌آموز دانشگاه فرهنگیان و شهید رجایی را پیگیری کنید. ما داوطلبان ماه‌هاست بلاتکلیفیم و به‌دلیل وضعیت مشمولیت خدمت سربازی، آینده‌مان به اعلام این نتایج وابسته است.
🔹
لطفاً پیگیر واریز وام‌های ودیعه مسکن باشید. نزدیک به چهار ماه است که هنوز وام‌ها واریز نشده و واقعاً به این تسهیلات نیاز داریم.
🔹
از مسئولان شهرستان فردیس، شهرداری، شورای شهر و شورای ترافیک درخواست داریم به مشکلات شهری و ترافیکی فردیس رسیدگی کنند. بلوارهای اصلی، به‌ویژه بلوار بیات غربی و بلوار تندرستی، با مشکلاتی مانند آسفالت نامناسب، روشنایی ضعیف، لاین‌های کندرو و دوربرگردان‌های بلااستفاده و رهاشده مواجه‌اند. وضعیت حمل‌ونقل عمومی و ایستگاه‌های اتوبوس نیز مناسب نیست.
🔹
شرایط آب‌وهوایی شهرستان مرزی هیرمند، زندگی مردم را با خطر جدی مواجه کرده است. با وجود این شرایط، چرا مدیریت بحران استانداری اقدام مؤثری انجام نمی‌دهد؟ مردم هیرمند تا چه زمانی باید در این وضعیت رها شوند؟ آیا مردم باید زیر خاک دفن شوند تا فکری به حال این شرایط شود؟
🔹
لطفاً صدای ما را به گوش مسئولان، به‌خصوص مسئولان سنجش و سمپاد، نماینده‌ها و رئیس‌جمهور برسانید. امسال با وجود شرایط جنگی و دور بودن بسیاری از دانش‌آموزان از فضای درس و آموزش و حتی ترک خانه به‌دلیل حملات هوایی و موشکی، آزمون ورودی ششم به هفتم برگزار شد. بسیاری از دانش‌آموزان با اختلاف بسیار اندک، حتی یک یا دو صدم درصد، از قبولی بازماندند. در برخی مراکز استان‌ها نیز فقط یک مدرسه سمپاد وجود دارد و امکان انتخاب اولویت‌های بعدی در شهرستان‌های همان استان فراهم نبوده است. لطفاً با توجه به شرایط خاص امسال، ظرفیت پذیرش را افزایش دهید تا دانش‌آموزان شایسته‌ای که با اختلاف اندک قبول نشده‌اند، فرصت ورود به مدارس سمپاد را پیدا کنند.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/459645" target="_blank">📅 07:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459640">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kRIBijN_uxi_uncCiNOOZMAuSXgo3P-1jmtMGlHRPfmOEgM9TZOriPtVhT0QGhme50tsfHdCTetvg5SUTgq-FX9UuMtJKZUwZgh10qapjMIPBqOq3gzp5wkl-bxiJIsTiDm1cKkI_Vb5pDryXiyf5bziH7nDR3SAyEiz20VsB7y2UWUgRpnEYTC6l2tPy8R8IdfIeZ-XPh4ejjb3vAmw8jj7IPxCfzwPH6drDvO-WKcN6aCW5b4tcKXZRH7HQQGfq7anVhEul8gaamjHXq5-8xCdOjByW2EqRVhixG6_qn_ReZLsPNTCy3jU34cJ9ZuAbKe0uTXegvzBwqMnXZkUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F5LIxXOc0b0Iqi3T0Oixa6YSJ2HkBc14-ps4DU0YQrtDM31uWHJp2T8usdsR86W-da2nFdVnOJg8_IMMY0MxB1AWRR8iwHRssGhC43qPsP7ZxC3IgCOv-x50mX5ao0cyk0dUmYMli1sQxPuj5U6209tNBKjQw2hIWIMpFNYhpsA5WFCcRWZZ9A4OZKG0FKXy9tRCBK24wXHRYHCnS_weZFKc3ekJKo1GVyS7BQuSRDTkKw6srb-e8HBRCrCy53eYPX5Gq6wuvfiXmuONNq91gIzGcLNX7HLIa14l3lrnoH4H7n-6kdHCbjGYKn-F_PJCp27qrnUlYxq8-r_vjLmwTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJTN9to3lYrldL8W783Bu_JYJZoqTkcHIhd1BCTJ-GHDG9mAPj3uqEpTTOjLoGeS0KsCR8MVImXOyTX8AHJlb_UUuL41JbjdAoyLNKaMAvnRKBugOi8cA6U6sdb8lk_J8VXxEnGEJ-tWO0kDOYE1UTyEh3ttTLtI9WDO91LEkMbKWOsWgA-fMzTSb5ta4yeU8E8ooMG_EGG2M62JzErIKAR5vzJP0Zufbf07x30lp_tLB7JWIVeM8p43SwfvPew5DgFuU3Ifwu60nvFgP-GcO0xz2N4q7ehoqmaEYDH2D7jyxAcha2w2TOWBKCdIAjQ-pSMuUWNdBJJLQNnmS2Vheg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/puAIppGsrRdsVXMJIAFxesGp8cEhqkuGNVkzkBC4JmRlxB_ND42JZgOe7b5O3yQ0XLwTfaOsmYrvdpfGj4m_2I6m7QyeyljGe-isK0NDvC0cbUj9epJtcytottRL_Cb7KR5pesKZ9aISXda0gsJivIWZOdSzNtubY8izsZTxWgd75XeX_AtBMdJH_PtY6qcjPizfV4VoaehjDlAOAqSERA6xYQgyU-L3pPhUIE9yDAqsIw9oyWMH3q90r9D-9TKfdH7xdZw30dWYRaj1TMhIPOdcYxyMp5LB0h-b4p1YZpHlgBMGC4-Vkl5_NoLV7bEo26moxrauyoQNudlPsKYomA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X1ZgJGD1_v3e7Vsr8v_lOSKuoI123fp107c2QRzwDn3qgt7tcgdvBSJmS3n-sUZAtEvVKcWsD0XC9ILT1KNlpnryHFWklR18gf8uzsuooPHWGQEnP5KXOYcb8OReu7L3Go7CmEEaxjtvf9U9YCw7ERqUU4-Vjad1Iy3rOs-3DeJrwYv6hISShgj9RfaW95NTepH1W5MHfzy_scGWy2e6mvv7LfPO6RlIRTjGn6cAVPcw9y8lHwUKgKkyCndQwm5OB98N5jiau37LHH4sEY1naNO389ONWoN8uuRb_h5sRjiLAHunoa8AeaMlHj1qgQhnECwFVy7fsF7ZYR5RrwBuGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سفر وزیر کشور به قزوین
عکس:
امیرمهدی زارعی
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/459640" target="_blank">📅 07:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459639">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">هوای پایتخت امروز هم «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۸۸، و در وضعیت قابل‌قبول قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/459639" target="_blank">📅 07:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459638">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">۷ شهید و ۸ مجروح در پی حملات آمریکا به خوزستان
🔹
معاون استانداری خوزستان: در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/459638" target="_blank">📅 07:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459631">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zca7kvL42emhCtdxnoMspvficdSWk2EJNw1dvXEQCT_NVMRDVHxTnlw_9DEMndGpXwzfTyLsUE_h6nwfXqJH64d8DEprCgnIuaoAoK9AnrlXqf1TaVPKgRbtfrWaFX7EjOrNR6bqxjvMk-_J69IcGyE7JVoWePuD3BgYWRX1Ji6BkEy4Iec0YFw5RNiwaRoFAzdrT0Xo-98RQFvwEXygiaLHH6gDO_hhNwwSNEiYwib4LkCHX6Qxfh3lcXMKIW4lwlYgGBx-3JtnvZnZRlcn2wK_5iOFYNsWeMgfAHSXqjeQG3_ZDmaMeWU8wzncO_5uash9lkIBCYejQpt3lPLEqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A1nTIxA_qE23iQy5kqHr6Vg_r7ZgwVtBZzXtuefGgvP-erKsqvKUqdB_IEDLDsf5QLTPLxKh2z8byZj2WtRClvWcySXOlV5H-EmmP42l8PAGxtkuESCCuMMEVKF4rsZaZOdoxW6Ir2ZXF7hlcWNQG566JLwN16JOmUs0DA2Q21QVDjwfrSePyyo5MHBCfGJ11z8oqRurrlA8Vxm2gLr9kPJ_XemMAvZwuebnVBw0DCsldTxJjEk_XY8dT_4x7dMVaDfAgjXU1w0RQLOgrZF3IPqGIpQf-WBxZJUk7CpgtHPCl0NRcWi8fiD1CU4XadsDzxjdKPtpQ97Nwwpmno0v9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QW_0pX_OjBmOQwUvzfWCGzBABCJuz9ktMrr2Pl4-boR2CrHUSgjxDc7WcQKL8bOpbWaKsPo6Vw4ChS_I9qDabu1uf2BFJL_F4eUxivEMJvHPzAtFQ-4PMZ2TuRR1DJX5cRWPBD8ykuYwBRaf1R3lgR_dWmTJrKGijgGKiQHIEGZGyUePP1dA1FHx8X7_M7gq_aOeLSy7kSnvgeFnaCpMGXg9tYJWE-gXkAe4w2EalZxSWp0qjoupzvYftzpoL3VTc6O9DB_uujiHnrWHAXsPBCcbmefwoKkfgRZxWmg3qh8Kqc5_5c5l26wUPc8dGXCvjvQ1HMEC7674gfM863AdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/my3VxFtC2BzTvWp_D9Vs7RbXKwTVhAS68CxYOcJhae13qS6Go_HYH4bKCqJIFppFI9tCilJHcgQCYAlgv7k4nkM57HuxC02w_iZeCxPGedxSXLSsidcWrNcvav19zDyiDj6o5LF4oPND01zr9GFF76xV7jPw-cfx0gAT302CZXnv9mXJ-WeuzE3Cw3ejaLwb8FhF4ySi5TjtzSb6KK7PAlh5s6Ts2GnmLjfTPa73ZFwhkvRl1yUUfT3tc88CX7XQDy_-lR1-4nRubVWIy8QXUB8WdDFeIZLJq_d29Z7zEEih8TyJMRemg0Ttrb7Jd5ujPwLdEte-UoGFoy1ZttSwxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rtLx2aagc3CnPlJF7Wgf0zeq9nl-cYmhNYRfdO7Y9rfdtB1hJxIoGVhM_d3NDt8mSnV8yFc2BmGAtNegn3VeUuDvN-Qgn7bwAhKN-QukjvLBalIFcDyf9fs4kBo9HoPWzjXS0uiUDBHsnbc3yLpABBlmh4Urge-A5skY3Ud7JwYgOErh0NaHa2shYSsXYC_pwtC7GZajLybOPQgtL8-4fBBq6w-qSy3Zd61AXCS82au3hJ_bXxajw96_eN-SRqG1uW6hNZJ6N2EOa--CzUWVBJpvPVFaxT_Hn9WansalLugYs7_Nczv5asLjX38D1sW2ENcAjgYJqPAcVYAa6EKsag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gewIwHy_Y3p5QgszL_JNzD5wjraH2CoYfj8FIdWAdAB7hPOibGRcSPnxHjUHrzELKTsVKhxVTrVmMXHSjcWTLCk1aZNRy2dnSS8bZoZ0bVziazQ_WrPXbvViYjBnSlQZqKCSW0zedspCUp1ybr9ofxzb3SMRcke8gRQ753L5gfqmjE1_0HewrqCRrVMHhlU9_JlYJOJ3WzAbnDgW4J8SaqxccySwookWmu2EriMB2YtE5hewdF2-s_SWBapej92X4ilwQSJNGG9UFuVBynzIne7FjfRBBzwp0SyN1ihka-UPHmmA-n4LAI_nucG-lb_gMKZ66aRKwhaERR-eHq_pyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cucRpvaaYs1hDJbPI1xMHuVdtLYXR_bXFxgU-K53B3DZjGghsU-sUJdGbLLnww858rPfzioBmVZIb8SUudTeUBd4KUhmSGD8ZbWBNBxcWv11MRH8ZkKl3XzxrHolra58iduoLXfJ4O9aK046gI780AUWMa-rY2SoyZWdsgkRINQ18OdYU7rbwolinljcRsJZUgZX9ahybZ4Vznf7DEIHn5DLPMcwoKPIt14zb4mXdXaDOuI3C7l4CIrNzwfYeXJzda6_2OtssvAIzjoO5tP8piugt9lgMBJ4sI6xl4MmkXyckWn6SF0pYGiGacz24Cj9h62nEte8qQpLLeCOEqsIcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌
📷
رقابت پاراگلایدر سواران کشور در آسمان مرند
عکس:
عطا داداشی
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/459631" target="_blank">📅 06:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459630">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef3e53a1a3.mp4?token=vnijdnVoinJTLNCM5pdNK7qOZXQiA_BDvkQk5QyAfT00KAmHbGy_1XgbepeqTNSdrlbb18CGS8ablpGGrGt2Whh7lwOcxtHqIVs3Uz7S23R8iGV90HJCBNtUOKNM8wXcuxq0XF9dHgJHB7QK1fYpdFTtIjBMvCGIAmGgZnj5BYasV75I8-u2JwE1UwW4IGUJ6eiJWjv5MUhkfayT0Puc09cv8cFfgj8_wRKjxYm_PkkN3Z7hAiGbxxcLyDKdPWaNSI053mwNBULp_B3TrXhLBZ1_VNLGo9KS6BGvVAB3tDs7w3F0qhh4iewFXoPhPNf3yZUhn6F79gtKbtDPtdGlHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef3e53a1a3.mp4?token=vnijdnVoinJTLNCM5pdNK7qOZXQiA_BDvkQk5QyAfT00KAmHbGy_1XgbepeqTNSdrlbb18CGS8ablpGGrGt2Whh7lwOcxtHqIVs3Uz7S23R8iGV90HJCBNtUOKNM8wXcuxq0XF9dHgJHB7QK1fYpdFTtIjBMvCGIAmGgZnj5BYasV75I8-u2JwE1UwW4IGUJ6eiJWjv5MUhkfayT0Puc09cv8cFfgj8_wRKjxYm_PkkN3Z7hAiGbxxcLyDKdPWaNSI053mwNBULp_B3TrXhLBZ1_VNLGo9KS6BGvVAB3tDs7w3F0qhh4iewFXoPhPNf3yZUhn6F79gtKbtDPtdGlHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تا می‌توانی فرزندت را در خانه ببین
🎙
هادی زینالی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/459630" target="_blank">📅 05:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459629">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WB3oxZEQ-A0UH5qo2ZylVIdpd5cpyuRfJ80A0YDJRzsd3AdBoAD38us7zih3qnUmLYGQ-mdjR9gEHd9PJhl1OLO-lRvAx0BEC_xsjHjVUfoZbUcDmgmhpT0gzx9v-lx3KwhdSaiH8dYuRPb-UO86574HW_Kpq6xbewjW-iMKTFbNQwB8Qn3hKau0a07xu5QGZZf_kjrvyYbG5pAZLOiN30k88Z-mlMdsRHQJAI4AUuqgojNb_4xfgrgGQYW2IQLlwbREdPWRxNfZ4EqwNZvJ3N1MKZwgbUyC5PttzMk_Qr8acEUm2r086BSmYZIo9RWfzMfPhEewIrWRy7O1-FOXrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از کمپ تیتین چه می‌دانیم ؟ | شاهکار سپاه در عمق مواضع آمریکا
🔹
آمریکا پس از افزایش آسیب‌پذیری پایگاه‌هایش در خلیج فارس، بخشی از آرایش نظامی خود را به سمت مناطق دورتر از تنگه هرمز سوق داد؛ اما حمله موشکی سپاه به کمپ تیتین در ساحل خلیج عقبه نشان داد که فاصله جغرافیایی نیز نمی‌تواند پایگاه‌های آمریکا را از تیررس ایران خارج کند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/459629" target="_blank">📅 05:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459628">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHZhwBpChCzG1O71vBJwVi35YJPMGqRrxTe5rDJCbYbmhLDQJMn9nOiRzpSbrMzkyo5EGP666bpFlE5yzVTOfSjASiHHUIxWZZF54Sgn40GjZ9JgiJlWRO2SqnHdsJem8DzCrqtY7PD8WjhqphX7V4HCk-kndyrCIe0S44tuU71-B5TOPsbTnJhXHg65N9cDD-5_L649qJePjnphdnJFSdtgK5PCvypIOCUPTWeyfq3eKddudHAGlm7XsbjCLoKVZxFwk7a7jqgipbMHa581DKkZZ9shAtSqt8EnWbIWoDQD2ZHuFzAMlH_ckq3e3GIeStnEcwKAntBOpif82cOZfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: نمی‌خواهم ایران را به میز مذاکره بیاورم
🔹
رئیس‌جمهور تروریست آمریکا با تکرار توهم کنترل بر تنگۀ هرمز، سعی در تشویق معاندین به ایجاد آشوب و اغتشاش در ایران کرد.
🔹
وی مدعی شد: برایم اهمیتی ندارد که آن‌ها توافقی را که حتی از نظر خودشان بی‌ارزش است، امضا کنند.
🔹
آن‌ها فقط دارند اتفاق اجتناب‌ناپذیر را تعویق می‌اندازند. مردم ایران کی قرار است قیام کنند و مبارزه کنند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/459628" target="_blank">📅 05:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459627">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbNp0-mCim9SnTF-J7sh70GIl8w_Pbol06uPxlM_ag8NqSIh2TiPWwoGgs62dxmsH9ilFgPSi3CJ0C3jLt3bzMugieCX5F1u_zbnV-UP80VMjfxQkovyvNDs3dEsxqnwwLJLKSnMoTHY4pt3J927kgutA6AUKdzB6GrvMjhKgyaRRwbXmGJcrp7Nfhlog34OfHxpjDeQtJuipPmvBEsmNy3Qg5tmuu73s0XBaJZnZj2GP_G1eTW2_ZtdYcgWiNFGGMS3R3sHc9U2dDxWbEIhUBscQU0Wq7Ro2CN68InbXs01y4poVdHEr_fR9iWf9dY94XIVM1mIy07-zCND1oaJqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آژیر هشدار حملۀ هوایی در شمال فلسطین اشغالی
🔹
رسانه‌های صهیونیستی گزارش دادند که در پی حملۀ پهپادی حزب‌الله، آژیرهای خطر در شهرک‌های شمال فلسطین اشغالی فعال شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/459627" target="_blank">📅 05:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459626">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qktbI7pKz7MW-dWivPZSWZWo9sO6W7x83YaPOEZhDqGIrvXRH39cRTknZRV1PFD6Tui9HKh5JbYIfE72NXC3dDMrMGpzZ_Bz-MUdWqIA-BzKeF3mUy_dC_OgWa4wLvlL0n_miVGph6UjQOE4xR83P3jplakeqbqoxbIkozRSaRVTqE-a3rFpuIZchgVIsEWel-5xaVj-kQyv8B_JMVErgfpdw-8M_Xf8dpuT_dck1AjxUeAsT6bvfNDXocVkvyX7ipeMkM9-ABBppw2WF15oxBBRmhWwThPsbTe8C8qgGNeZ0n8FagzCItvrI2lzOwEB-AJ6UBDPPm0HPuU7Nu0ueg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزلۀ ۳.۶ ریشتری در شنبۀ بوشهر
🔹
ساعت ۰۳:۲۲ بامداد، زمین‌لرزه‌ای به بزرگی ۳.۶ ریشتر حوالی شهر شنبه در استان بوشهر را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/459626" target="_blank">📅 04:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459625">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یمن: رژیم‌هایی که سرزمین‌های خود را به سکوهای آمریکا برای تجاوز علیه ایران تبدیل کرده‌اند، باید هزینۀ اطاعت از آمریکا را بپردازند
🔹
وزارت خارجۀ یمن: ما حمایت یمن از ایران و جمهوری اسلامی را در مواجهه با تجاوز تکرار می‌کنیم.
🔹
پاسخ ایران به تجاوز آمریکا حقی مشروع است که توسط همه هنجارها، کنوانسیون‌ها و قوانین تضمین شده است.
🔹
آمریکا، منطقه را به سمت تنش سوق می‌دهد و به همراه کسانی که در کنار آن ایستاده‌اند، مسئول عواقب ناشی از آن هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/459625" target="_blank">📅 04:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459619">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OWBmMfv3YLGYbY59a5MU2yBoGcWjOguxWOJ3uDXK_t9Fgzt-t81LFjJaaKIgNNLu0QWpHllQFwIM38FR2sNgpQxzIO4gYg4vRU1e4Yhdy-9xKMMQvoWSB7L7GOye7S1ELlLcRkchQy9aS8i1klAobXzCoilGPE-w981gOGqzNmEC1E97PxOciODvDokAgOZ27U9Emndn9LFkMIrm042t1AP3vfPr4IMgp2RvEQJ59q1HqmEx4SEi0uxeqbvg9gDRLAB1r1VUirNfRx4w1JvGNPeXlQNX2xHMFe4Puw1va-IMvvVhUBCAe_qGzc6dGTrbwknuj2kPcWmEgyMFkCQa-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UHDw1ZFmAM3HbPePgY4PL9pH466I5CmSbRSqFgQQ1jWFbdKQfLR943lBtmCgMneKBt7BcbbPxRcd4Uuzo9g0pyQQbxA9tCngjoBulhpLCishzwm2fwbJeTosO5VQStUdni_QpSdlQttg5iKhIFR7ZvaoUNgA3f7TEYSchOyX4OCiRomNLGBqzFFPMpTD9-zoa5atWql5mrAhqLj5xP9o2gzkBiAAsI7HQ7ZmkfdK_w3K3s1iOgJvUBjzW-MmOs2WzPdrXy8sugc2FcLwLW6aTC9124NANsATZ8nLJGwRudYigpoEYIzj8g0IjMJBfmvjErUJIed13CSieZ837D9eyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bX3csgYTmB5bZzHH31W-xtYcIf3mzdHRBujVAAP3R7gDENW4C0UgA9R2zXa_DAF3G-237fFZBmDSAz0x1EZ_dzPURUbxztKNUpzs_ljX2FK839Z3fewOMzpkMB8q1Ipwwc6UAjAU8Y2hV2E5I7s5r3epeVMB_g3_cbMzAzucgtPVJEYIXE6dKNle8VzPSecPW91p9oIqLEmIBCVl6v02as40XRma_gfYREsf06Js0-AjbT0pYPyu8RqbWye8i6YeH7Wllw745uAi_kANc8KigxtV-LpHJBhlSFAlrWweHzuGFz2cYv-iXVvtOw1B0qQbKJsisp3x1ykkj1tPagKGPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFGZZU3VdD6Ecr81dJIrhLnv-tqalvP1Jee4g3Hh3Zcwb5lfVyALbIZZbtQFoHuyO_LqHTWg0UJqEYeOEzDO7wVqLt_WH588mxBldaiMVnK_h6R1CmEe64smsYHH14IrnfyvgK_IwQT340Pmo_EpK9UFvuu39L3G_n6P5n4OIqP63R7n63hdMEW-kdLmGYK_uyhRzIAsyXRrYrRuYS2DUzEowz6CUhPXyLQYk4uvGixK6vaYVHV94F6ZUbEGrjAmTeYLfeEzMvaOYCcp4HLV4Rmo0iqe3GRyhVaXFSswirtfhQuLXKJGuIzx5vamVaFy-PgTnRfZacL4ZZ3ua_MO6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OdMSs09DCueymEWq7PIDQnnX9wbGQCvoygNm3EGzXaiL2CoxFXMw1p8qy6ppEHdzSkjwvkyiKYvVqQ7dBAH5AzleifOeKxqWaWbJszArkAdVtEkqV8Ss7_3R8OHQluN1VluQS-2rMfPN861Xs3xQpxt161azkfsDXcoY1A1V3iPoMy4tqpA0q3QcSMLOSKrCOb-SZa-6iRGOylC0_5WBI-v5TnkOPHwKs0F6-33Ybjnc3jlAe5f_w2Br5Jsh9tECtfKDOK915gtRmN5f6UWrjlT1Eg8Qg8Gecjoka7D_Yk3CPmyTTnUb6NxrAdfBS2-sZntafJOwYzJTx9AwSsvBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dIHWb60z08ppvOoZx1arVWh-9rUiqdZ4eP-Uxxyh8NmFCpr65WxOivVdj-gdKyVsgFns6CRRwhbccd-Q2w3-ZcUfiyEgXyYVcvI0d4lbhGYj61So06sxkgB8vGATJ2zSeaegbOmuBbHWLBDwLjX6jh4kt8u3hVgw7fqmZ_nsHg_VMIcborL0nFQc39-rCeHMEDy1cfKGJLTslqFrPwQcsJFA1wJx27Xf5hhzhUQG4EfhGxHzfklglEIVwCmC3TbXUUO_nIqGUQ8oSn9a04EJJnSJHFGrjMMSLdp5CdWq6UeP__UPmak-JsjAAACjrHxMYMf1GLxWhpJMIvWib4PkfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | چهارشنبه ۱۱ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/459619" target="_blank">📅 04:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459609">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dPYNBvrcmq_CDEhCRXGpB454UGHdFQLcMz85-HIugesmt39zxgQtIC-7mH_gaEQh_5bqN7pL0-h-8ulSgbBEWBc37mLJtOxbB83A7TbOQblOxPG05sA0CZf4XAx8mcgHTqo6AjHM-GK0q3KKqKb2_KP7-X1aar8Lg_0YvQyqO_01aWNf1CpqD_KAyYPg4PdQsiwE_FCyzRD4cCdPn4JhlZHPz9k6a35pbYLF3_94P8Poh6XrcSTLZqXz9Uc--MG-NwCtbqbKP4pFOCHjWnf_vcekSFQ3iBV3Ef72kuC0nAQbebtmzgJkV-4xEUJCvtjfXt9I9Fj2-4hc_9BFsJgumw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BUmlgKnwgjdAU8PVUTiCMuSsfOZtV0GlshADUOYXXDxfgHpQtZPnSQDXLxQR3lhvk9Wzn7nnwExCnnaz6DFeSaAN_Jmoe8bZtE5aGxlQWXU_nILJrRU8gaUHQBxXPw6mGv6ci7GSWtFj4Q6nuSXT1M5NFYntrkXRmCk1NgZuPC3q9iUboabyHL8F9L5k9b5BXqyBFIGXVskKehFe7mj49uNM3aOnGd3b4RNi-yxgHsTExQ0nOfHtQqBL9kThr6XB_BleG2ULB3Mg-UT548LRRoUoePc2liKUnZeyQZSZUtKOxfVX25YALv3EgGFXd5ucH-Pq2WjSYODMH-qDurFtRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lehs9-TmIlWLwZklr0fAptLiqBOTCcL-LF0BaGGlkfGzHg4SHwF4ntRKG1FEJVY3G5PHaxzGIKY-dwCGqmr-Zp9_np1zew8MQnrqcJyjJiyBNvYCRziE0KAWAYdjDC2-7lx57dyie8YLJrK0-D1xS5q5_IcisXDUugtBgdUqCg7jtsYBxe36lt1MLAG6ZFPm2_4lH3ySAe1PfKIecgPgIsxuoAk1iYBI6p_YDsVRwuAnhE_eubD1XsuP55jmr4alE_lkXeaMAktFpSy6ZN75kFV1BN-tMrEXkvYU9WvkHyUhqvyiTF-0ymMyolg3Lwr3ddD8-3WdGwpsTZeNHLnU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eINj0xSZwPGihZ2HtoNJ3qYygwEySUGciGGb_aNiUpgnT6MUObWymguyFxjhwC_Ud52WRnFMSwvOcscDf0lEcMo3AxgGQZJTC6A58TjhOUpLSOWJKhUZbMlV14efZ6GMlGPPpdI-vAN803Z88CCaBxIAirRtvZVCRoILy4hd0CnAO0wg5JeTw2wmyswYONyca004D11UFrYeN4Qw9tg3VBf78EHcgbfWvn32c-K_7rjsN3cxVOBu8md5gmZLcyWOyRUIc92kcuHjnS4iG70bSTaK4fnmX7uOUxA6t5N15GeMiRa2yMZY6tAx3xDnwf3xFCSW305cg-16pJ9SvtVc-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/chBMxe74YWeZqQ4gbALDhIt9LsLq9GECYSZCnZmJ0mnL1Y1YqGeoPxS1j-oL7MNgeq3Ozwwo68dPXqVEpqVUnsrC6Z_33fEZvHmaU0SRBa0PXQI3pVwEMHiuVTPscEdPAG09m2nAc4UqxDWlQbiabAU0Bb1ruBOH1zjD8cy1_NF0fEARJP8cwDwuHZkEYULamDBUaLJ4NZ-esBRxL0gFDroKqARX5_8ogL0PPk9KnbItjPNK2M0iyJuMH7Z-Yqi4QKRVuTTHxrOriB5Om-o5gBKbyMkVFzlKQlRo3MNPEw4qhl2MjRDVgYrXXp3gBRvV1ptxqeYtS4RrCNJr5U_dPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rzPne0ddY7scYGHXasffz8Qt4W1D4VGJnITdycLj9BzE5n13JW_phwxHe__PHj-cPRDlk_a3TBrdWFy5vnLHsVTboAtDURCw9CTmewMWoTjBFVxHUokoq3QXtAd0ZnrM474gUoT6lpr-lrpgwlbuTKbYRrPkfCNS6U0n-ca55dWXPcud6j5bNwYGK_FZAMlH1J2yDyIyv9VMAqM1pnmYT-wFSy8FhXbaG0NvFIj6gg08lQW7Rd3cV1WS7go-5pySv_cJ31jpGLIFuKv1dpOlLXSpgBT2LwC4dkI8fU8r_LhL8Y2I_o-MVrrr7shJIyGZCVEbg4mgqGiNR1agFALu7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ipl4b3pnSJk7FeZC0UpSHg099cfTX4wUReXJE6AmEmlc8qv1tW5MgD_B-9nSuvNtR046p5mUnZNr97xgngUMI5W22VJIZguqnngEsWQNOHi4K8RAfLQPDVx-reUVglGYywKHPrMAPKLsLsdZll3td6h7zBnpe2PrWrfaPq8wz1zBblWWu-ZYXBI-kcuskgAQmFaPhYwRcoS-cwTMkPTNSDxyqO_p0llWiLvws5XiNXB4Uo-R8lDAehEuXOWUnj96_wY_cGOfJIArCnY6t_8QWgdBmid-9bodjo1NkzwZVzO2p4y0hYrJ_t_rt_2GS_LnngaiYUELT0O4j4a0c75muw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tECsfk3oGeaVzAHbCcUvOkajd9EbMwZ4hhl4xkq9MWVkM8DFEZS4CEyoS2hc19b5Kw9_hPmHAOUWUoO2bd_1okOAWN1JfR_K2Cw9h1zOT5DZrXFJ31BvC4nlxCBHu9rEX2cb9wrRxWcPs3nKH_hgetWByT8pq6me0KhzoLR4Mza0wy9Yj8DWONENSWhXUtzbTz565eTwZmAAIN-SCw4M1vaFaYSFVTnUt3XwQcAIbex7ErNnxOyDWitbKEkpld4Ab1yGa_TE42KbAVICo6f-QeGsg9yauAQNW1ZIjr9ftSDyCM9KlqDah0d1vmdlbW2GREOaCMlPNVJDKEYDbud8bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rvskoriLD5OHnjScGrjnfV4p042Nt-1j3ke65Paz_aRHX42p_Dtmz_T55E8Pv7TVuGfBJPPsO3sePjtyQSb07u4MAw3X2A2bFMXrZ0USZLNzpMpAfuwj3Q6BruuxvPj_GJagyrBmh9xrr--nZA8uswFSeoFft6oemXq_0iJtmkbJ1m-HeibypHScO2xPiCaeYF470-Yr3iTKePBNfLJFJXPHc4akIIgZfzYcnZygZguxlQIG1sUPtGsaEO0ApcM4ZlMDg_Pdpk6ly1gGcv0q0Na-t0iTS9fJj0qawAnBsU6aCGgcT3U229VIjFsD44UgqNm5OvYsSOohWhsxc8VKrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sZ9Uo-E_j8IpfZcRxeHgAvpW0dddf6jVmUrvFdAPCBt0EVQz1C50nz8BsVtY9lF9nO75AKzNSq1w_pqaTdbwnh3SinH_s9GGqN0ggdaYg9V2ToOy8DWugqd_ThrYnaJyIm4pogUuP_dlFrJ3Qre2Zy_yb5JmaclBhmgSaL-VE-YvezMQlve7Yc5NdhF98V_33Qbyt7QIdoXJZwDrdGcicRDfr66f0uu429bHtZOYhSrehRobhrK6PKN5pIG7DIFa8iWF2GFAoKseSi7FlWPCGo-N5_-UGnB9gYtvoxDxGGdVWhS_H1LE1F-Rcx4R7kKjLWge7HOmEluubinLgopLgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/459609" target="_blank">📅 04:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459608">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">منابع عراقی از شنیده شدن صدای انفجار در سلیمانیۀ عراق گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/459608" target="_blank">📅 04:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459607">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پزشکیان عازم قرقیزستان شد
🔹
رئیس‌جمهور به منظور شرکت در اجلاس سازمان همکاری شانگهای، عازم بیشکک پایتخت قرقیزستان شد. @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/459607" target="_blank">📅 04:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459606">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016f993372.mp4?token=O4iqW0igvireMMWCXThN6x5AZ8yRJpUm4A1fpyPGJwmjDr4wECn_Pa-C_it_sKE06BHWcXETKJM6ab35or7NVXPOujPiIUCD0MuIMHly5ELAloW6bVUzaE1cymv3yscCMMcdlI8vESKX6l8IsPIyhSiym_us-9q6s4GqUqVjjtUV24EiBd4_zx_JHqjV0HlHqktm_AbKGKZK8TApbCU4vplL1UltmNeXZRSAzYdlYyXBc2bSQz_14v-hL66XWqjs5TC4VFBz_Z-SNjav4-7xVHI_QHMcbfTsfpvj9Yo5fZnUGpYzDLXFo536vPcgbFHHsDpmUy3d-05a0c4xnXlJQkghz6h9-OukmqNZYzbeIeqoqLN_w8jA_38c95qY9nuPCG2PMem8gaa-QxtlN2tXFkYjIKVZl0GRV7-jXHQ0mKVGuPhG8yG5u8l0ifXn0LrjXiMbJbpYNyHnayMCT7kGw4Wlh0lVFHvszERToVTnyAAyb1TOEPVk8Mr-feRYWEurVXHW-q8t5zYfAg3nkCE359xdx5xoNcBvU9DVf0trzJsJnt7octTLhiThRKDE5bS7s3Jrk3yqrm8xn6bk02XQMALSnPV9uDPx8-Z7QIP0LUd_a6SGbtUCPasXEyUt4_GhNsFegjdVx6bfeRQST0toSAKLhz3npR_I3RUbFCZ-p9E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016f993372.mp4?token=O4iqW0igvireMMWCXThN6x5AZ8yRJpUm4A1fpyPGJwmjDr4wECn_Pa-C_it_sKE06BHWcXETKJM6ab35or7NVXPOujPiIUCD0MuIMHly5ELAloW6bVUzaE1cymv3yscCMMcdlI8vESKX6l8IsPIyhSiym_us-9q6s4GqUqVjjtUV24EiBd4_zx_JHqjV0HlHqktm_AbKGKZK8TApbCU4vplL1UltmNeXZRSAzYdlYyXBc2bSQz_14v-hL66XWqjs5TC4VFBz_Z-SNjav4-7xVHI_QHMcbfTsfpvj9Yo5fZnUGpYzDLXFo536vPcgbFHHsDpmUy3d-05a0c4xnXlJQkghz6h9-OukmqNZYzbeIeqoqLN_w8jA_38c95qY9nuPCG2PMem8gaa-QxtlN2tXFkYjIKVZl0GRV7-jXHQ0mKVGuPhG8yG5u8l0ifXn0LrjXiMbJbpYNyHnayMCT7kGw4Wlh0lVFHvszERToVTnyAAyb1TOEPVk8Mr-feRYWEurVXHW-q8t5zYfAg3nkCE359xdx5xoNcBvU9DVf0trzJsJnt7octTLhiThRKDE5bS7s3Jrk3yqrm8xn6bk02XQMALSnPV9uDPx8-Z7QIP0LUd_a6SGbtUCPasXEyUt4_GhNsFegjdVx6bfeRQST0toSAKLhz3npR_I3RUbFCZ-p9E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشدار سخنگوی قرارگاه مرکزی خاتم‌الانبیا: اگر با ارتش آمریکا همکاری کنید باید منتظر عواقب خطرناکش باشید
🔹
نیروهای مسلح جمهوری اسلامی ایران در پاسخ به شرارت‌ها و اقدامات تروریستی، با سرعت و پرقدرت پایگاه‌های آمریکای جنایتکار را در منطقه مورد هجوم مقتدرانۀ موشکی و پهپادی قرار دادند و در هم کوبیدند که ضمن خسارات سنگین به زیرساخت‌ها، تاسیسات، تسلیحات و تجهیزات تعداد قابل‌توجهی از فرماندهان و سربازان آمریکایی کشته یا مجروح شدند.
🔹
این عملیات تهاجمی به‌صورت درس‌آموز علیه آمریکایی ها تا پشیمانی آن‌ها از جنایت ادامه خواهد داشت.
🔹
هشدار می‌دهیم تداوم شرارت آمریکایی‌ها در منطقه با پاسخ‌های سنگین‌تر، گسترده‌تر و ویرانگر روبه‌رو می‌گردد و هر کشوری با ارتش متجاوز آمریکا همکاری نماید بایستی عواقب خطرناک آن را بپذیرد.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/459606" target="_blank">📅 03:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459605">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">برخی منابع عربی از شنیده‌شدن صدای انفجار از پایگاه‌های آمریکایی در اردن خبر می‌دهند
.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/459605" target="_blank">📅 03:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459604">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5589409306.mp4?token=t3GkfvjnSPeTKBOQ2wm0s70y9B-cASlWBo_yNdYhAndjrEMN1GcoQDF1Xnc5jQyDNSJ_R4PdyIgDRgJ63r1aUIsBDyLdgjTvECrZ3a-ec5eA0oBq84I3V3MIL0uD_iaJKotRX2mDWsxsuVzy4FqAdBu6446Je0R1WfL0wHZ0WgRBVk28NyE3epPZfh0NmOGM4exMqbkO6BlFVc3WdSSFupIzHxv-xRYEtle2lyMUNZJXfJjXUa_3JkiwT_j-XrCmORDkKpVaUMPatumPJtiKjGNJgNtgCcMWrfhoItwrH-IhhszvQvz00l3VQIu81DPpESz4tTbCuPzwxV0zlgpH4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5589409306.mp4?token=t3GkfvjnSPeTKBOQ2wm0s70y9B-cASlWBo_yNdYhAndjrEMN1GcoQDF1Xnc5jQyDNSJ_R4PdyIgDRgJ63r1aUIsBDyLdgjTvECrZ3a-ec5eA0oBq84I3V3MIL0uD_iaJKotRX2mDWsxsuVzy4FqAdBu6446Je0R1WfL0wHZ0WgRBVk28NyE3epPZfh0NmOGM4exMqbkO6BlFVc3WdSSFupIzHxv-xRYEtle2lyMUNZJXfJjXUa_3JkiwT_j-XrCmORDkKpVaUMPatumPJtiKjGNJgNtgCcMWrfhoItwrH-IhhszvQvz00l3VQIu81DPpESz4tTbCuPzwxV0zlgpH4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر بیشتری از جنایت آمریکا در حمله به مراسم عروسی
◾️
ساعاتی پیش محل برگزاری مراسم عروسی در کوهستک سیریک مورد حملۀ دشمن آمریکایی قرار گرفت که تاکنون ۵ شهید و ۶۸ مجروح درپی داشته است.  @Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/459604" target="_blank">📅 03:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459603">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‌
🔴
سپاه: حملۀ سنگین موشک‌های بالستیک به آشیانۀ هواپیماهای بدون سرنشین در اردن؛ تعدادی از پهپادها منهدم و تعدادی از خلبانان و خدمۀ فنی پروازی به هلاکت رسیدند
🔹
روابط‌عمومی سپاه: رزمندگان نیروی هوافضای سپاه پاسداران انقلاب اسلامی در یک حمله سنگین با موشک‌های…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/459603" target="_blank">📅 03:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459602">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌ انفجارهای مهیب بحرین را لرزاند
🔹
منابع محلی گزارش دادند که پایگاه‌ها و منافع آمریکا در بحرین هدف حملات موشکی و پهپادی گستردۀ ایران قرار گرفته‌اند. @Farsna - Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/459602" target="_blank">📅 02:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459601">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وزارت کشور بحرین با صدور هشداری از شهروندان خود خواست به نزدیک‌ترین پناهگاه یا مکان امن پناه ببرند. @Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/459601" target="_blank">📅 02:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459600">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وزارت کشور بحرین با صدور هشداری از شهروندان خود خواست به نزدیک‌ترین پناهگاه یا مکان امن پناه ببرند.
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/459600" target="_blank">📅 02:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459599">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/404c7bc669.mp4?token=TUzaRIT7GfaBQ2O4KAgzTGuKTFPKVFdIWDB6znhpMXoawRDNCTAUYGEN6gaNHNakvL-VbbUZAiSyU0J-r5o9elhdq5MXVy2ojrdWhWtLd1PicATAGdLE3SyEHhHogxDopbOEze8axHfTBPs7U1EUcGXZu0abXZYWvERfOlaTFHhrOWNwcA0Q8ahaH1s3Tfr6k823Vy30FNiemiMUspVJaaPJ0XnSq94prerskDTNRb7a7AJDK7IVvvhopuDIorWoHXvQRDCKgzyrAYG4YB37aPYTUlCRB3xv2EQokQAIToO6KxYoIlyVYIuns6cczqpt1BpE36DtLz3f6ZmXHCyXHEuOaz3h3vBRdOJ4qM-YRJm_NxdcWEjWETqEe3bvwxZkujlMdNUnc-4viL6-83V4IIto3cGpLA3j1i82Jnm1Uq2cghq6r89A8WQEnaKd0drL4sbcBRvD7MGgFEpVtVlGzQsB88zblsVM8KFEdyqAVTuYhvKnp88mYg8G4fLlSSQVFjs_7o1QYA2dylYUiBiuRGi9qp4Ky7nRsf0unpDCNOp3ITHVYO4cxx3ByhC8h6kGVN9wv-lLaIh-aYQC9hWck7doWCepsRGB-SGCsEgakQyRfkiH3TxMIpkS8nXS9TDl42N0HDPWWYCVSZ20Wtf0DxhqUSwiiSownjUtnOiZgiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/404c7bc669.mp4?token=TUzaRIT7GfaBQ2O4KAgzTGuKTFPKVFdIWDB6znhpMXoawRDNCTAUYGEN6gaNHNakvL-VbbUZAiSyU0J-r5o9elhdq5MXVy2ojrdWhWtLd1PicATAGdLE3SyEHhHogxDopbOEze8axHfTBPs7U1EUcGXZu0abXZYWvERfOlaTFHhrOWNwcA0Q8ahaH1s3Tfr6k823Vy30FNiemiMUspVJaaPJ0XnSq94prerskDTNRb7a7AJDK7IVvvhopuDIorWoHXvQRDCKgzyrAYG4YB37aPYTUlCRB3xv2EQokQAIToO6KxYoIlyVYIuns6cczqpt1BpE36DtLz3f6ZmXHCyXHEuOaz3h3vBRdOJ4qM-YRJm_NxdcWEjWETqEe3bvwxZkujlMdNUnc-4viL6-83V4IIto3cGpLA3j1i82Jnm1Uq2cghq6r89A8WQEnaKd0drL4sbcBRvD7MGgFEpVtVlGzQsB88zblsVM8KFEdyqAVTuYhvKnp88mYg8G4fLlSSQVFjs_7o1QYA2dylYUiBiuRGi9qp4Ky7nRsf0unpDCNOp3ITHVYO4cxx3ByhC8h6kGVN9wv-lLaIh-aYQC9hWck7doWCepsRGB-SGCsEgakQyRfkiH3TxMIpkS8nXS9TDl42N0HDPWWYCVSZ20Wtf0DxhqUSwiiSownjUtnOiZgiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه: حملۀ سنگین موشک‌های بالستیک به آشیانۀ هواپیماهای بدون سرنشین در اردن؛ تعدادی از پهپادها منهدم و تعدادی از خلبانان و خدمۀ فنی پروازی به هلاکت رسیدند
🔹
روابط‌عمومی سپاه: رزمندگان نیروی هوافضای سپاه پاسداران انقلاب اسلامی در یک حمله سنگین با موشک‌های…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/459599" target="_blank">📅 02:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459598">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
سپاه: پادگان تفنگداران آمریکایی در اردن هدف موشک‌های بالستیک قرار گرفت؛ تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
🔹
روابط عمومی سپاه: ملت قهرمان و بپاخاسته ایران اسلامی، ارتش تروریستی و شکست‌خوردهٔ آمریکا، عاجز از رویارویی مستقیم با رزمندگان اسلام…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/459598" target="_blank">📅 02:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459597">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f143426d42.mp4?token=vhaPUrSG_6svMm4LDfE9GYASSATcYT1PmGMIxL5TiiyBDMXJ_MRUitxDNF8MMKcAHm4XE8JZg8AqTzLrMm3CQuYCxHrce7u1pWK113wcOIIT0QR7i6eHgN4tGsHx5Muvoy6TXt5FzuEJO-8GHT_QdrBWeF2URkNQWealf-KPDA9R7uIoqMKHofOD3U_3T1Oeg09Pl4jfadM0cQcRmF80kJhK3UgVmEDaojTqI9R58VQcWZOUiYnrWdm-qc7Wi_Fvk1L0Nim7d_u2RSD3trlI_Wxjkxr9rjhK13PSeRtPCePMk7D52PBg4RjBvEHackmW35S0M8ZIdvGOoE7zXvzRnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f143426d42.mp4?token=vhaPUrSG_6svMm4LDfE9GYASSATcYT1PmGMIxL5TiiyBDMXJ_MRUitxDNF8MMKcAHm4XE8JZg8AqTzLrMm3CQuYCxHrce7u1pWK113wcOIIT0QR7i6eHgN4tGsHx5Muvoy6TXt5FzuEJO-8GHT_QdrBWeF2URkNQWealf-KPDA9R7uIoqMKHofOD3U_3T1Oeg09Pl4jfadM0cQcRmF80kJhK3UgVmEDaojTqI9R58VQcWZOUiYnrWdm-qc7Wi_Fvk1L0Nim7d_u2RSD3trlI_Wxjkxr9rjhK13PSeRtPCePMk7D52PBg4RjBvEHackmW35S0M8ZIdvGOoE7zXvzRnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت شاهد عینی از لحظۀ حمله به جشن عروسی در کوهستک سیریک   @Farsna - Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/459597" target="_blank">📅 02:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459596">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuMprmcBrmuJz4p5AO_LXhKXdchCJ4FY4qa1rWuf3wG2Viryzf-anaUXCFod-ZOae6_y2BlhcUUvQ8FUWIqd62Hid1E8oHPIlfrMsSoOdo4LB6FXzZMLXjbhZ0ZTJPQ85y0QxvvdsVWDysd9hybeawf3oqhTrcfh_6xg_5CqTiKAwm1UY7u2NyadzJb3F13V3amkeB38zbXRa0yuLKCyxEuM9hAIAGRKQUp_k96uHaoz2guwEz5K3apnphhEpi_W1WdfiyLH60Tmjau1idCaMQwdyJIAvzCkbvMB3zbdeKr3-oDliJb4NJrx2-X8t4Q6HXPeOD_dAE5TvPox4iit5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون سیاسی سپاه خطاب به کشورهای منطقه: یا آمریکا را بیرون کنید یا پاسخ کوبنده بگیرید
🔹
سردار جوانی خطاب به کشورهای عربی: بهتر است آمریکایی‌ها را از کشورهای خود بیرون کنید و پایگاه‌ها را پس بگیرید.
🔹
در غیر اینصورت، نیروهای مسلح ایران ثابت کرده‌اند از هر نقطه‌ای در کویت، بحرین، اردن یا هر کشوری که به ایران تهاجم شود، با پاسخ‌های قاطع و کوبنده مواجه خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/459596" target="_blank">📅 02:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459595">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
منابع عراقی از وقوع انفجار در مواضع آمریکایی‌ها در اربیل خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/459595" target="_blank">📅 01:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459593">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5PbBo8C4chXRviYGG6JcNzGS6BU2zutGlWY8EBzG9Wnlf2xNusVbCxNXzIx3BNlft-FTUtAmwb2SKg7y-4JPgt-Uw0LoRt_ZMTCX02VXc8xNWn1zGZqQOpY57ruOOTYPeZxYu905G_aI447MewRRc_RlCzJtyXzQ6dXh4HQNS0NHT5GgTjEZaddzmHFI1vicdlOydDPt3d3KWBHMqq8EIzMX3uyr2mf7LZzR8BvDt-Ijb1WTbX7HqUhK-kEL8Jv3Niu-Zm6-RtOUyOmCurLD6K6c4Z7OUyYQ-KFiOIhF-iYcyYklPzjmmtJo50PwbKXqArxF-qfRuvyV9KvT8EbWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخابرات هرمزگان: در حال رفع اختلالات ناشی از حملۀ دشمن هستیم
🔹
اداره‌کل مخابرات استان هرمزگان: در جریان حملات آمریکا به مناطق غیرنظامی و زیرساخت‌های خدماتی در بخش‌هایی از مناطق جنوبی کشور، به تعدادی از دکل‌ها و سایت‌های مخابراتی و اینترنتی خسارات جدی وارد شد.
🔹
عملیات تیم‌های اضطراری برای رفع مشکلات پیش آمده و وصل مجدد شبکۀ مخابرات و اینترنت درحال انجام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/459593" target="_blank">📅 01:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459592">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
منابع عراقی از وقوع انفجار در مواضع آمریکایی‌ها در اربیل خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/459592" target="_blank">📅 01:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459591">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7sGQu5_erQkkVD1x9lrayAiQQZZYGRJ8hevTedudG9VFGV2WIPhxQFhp_MxYN5fQ0Ews9EF0kpLQoMcopwUJcHm9G7U6NYhMofswtL0SRxgAEKu7303XjfmJ-FVJx5t9Dl2-V97rkl5Qj1BWGJM54tqaPWzywUL2E130AdXhBCg2ZP1l8EReXOX6oYZFF_rCvxmiVfyQgsxqsryZd5dTkvp0PbwttJo4UdbXnDHokii1HrKTdUKFlXllGHlUOqcqRtFHaEMBdSq5exMs2ITILUo_u3CpEB9IYQJdjBHjR7s-jPSFcMZ1Zcit12P5k98hCEirikQ8Y1Gn4fQZnD-1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش بقائی به حملۀ آمریکا به جشن عروسی: هر روز بر سیاهۀ جنایات آمریکا علیه مردم ایران افزوده می‌شود
🔹
سخنگوی وزارت خارجه: فهرست جنایات آمریکا علیه ملت ایران اکنون کامل‌تر از همیشه شد. امشب یک منزل مسکونی در کوهستکِ سیریک، در حالی هدف حمله قرار گرفت که مردم در آن مشغول برگزاری جشن عروسی بودند. بیش از ۵۰ زن، مرد و کودک بی‌گناه شهید و مجروح شدند.
🔹
این قساوت را نمی‌توان از زنجیرۀ حملاتی که پیش از آن در میناب، لامرد، قشم و دیگر نقاط رخ داده است، جدا کرد؛ همان‌طور که نمی‌توان آن را از حمله به اهداف نظامی جدا دانست؛ حملاتی که با برچسب‌ها و توجیهات فریبنده پوشانده شدند.
🔹
خطرناک‌تر از خودِ بمب، عادی‌شدن بمباران است؛ و خطرناک‌تر از سکوت، آن است که سکوت به معنای مشروعیت تعبیر شود.
🔹
ایران به این جنایات وحشیانه قاطعانه پاسخ خواهد داد. اما دولت‌ها و سازمان‌های بین‌المللی که در برابر چنین بربریتی سکوت می‌کنند یا در پی توجیه آن هستند، باید بدانند که سکوتشان بی‌طرفی نیست. وقتی حملات غیرقانونی و جنایات آشکار، به اقتضای مصلحت سیاسی، تطهیر و توجیه می‌شوند، مرز میان محکوم‌کردن جنایت و عادی‌سازی آن از میان می‌رود.
🔹
کسانی که امروز سکوت می‌کنند، فردا خود نیز از پیامدهای این سکوت در امان نخواهند بود، چراکه چشم‌پوشی نسبت به ظلم و جنایت آن را مهار نمی‌کند، بلکه مرتکبان را در ادامۀ جنایاتشان علیه همه جسورتر می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/459591" target="_blank">📅 01:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459590">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
برخی منابع عربی از شنیده‌شدن صدای انفجار و فعال‌شدن پدافند هوایی در کویت خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/459590" target="_blank">📅 01:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459589">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
برخی منابع عربی از شنیده‌شدن صدای انفجار و فعال‌شدن پدافند هوایی در کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/459589" target="_blank">📅 01:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459588">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9849737611.mp4?token=QOt8jiRJ-zvAYzsfPZtAQI5-Nbrjfx_BaVWoo2S5osuwIa2iH-1nqpt04v-X5YxnEiXq37Ui_lbxUIFONyQvry2g9vadKGz1CzVbzKTPNoicgzmVzs8hSzx6Q1O3sc3jBIKkF-S7RedcRxZ7gN2bNRokjgAcaq5Clz5Ghi4n2lR262N7oOavkPVOyt0l4K2V3HguJyzYhJ6um5VuP0mIYoaMRJqjeuwRT9stsMje_YwHvfMCLtgaNqz8ZHaHX78vhksyYKyJZzfRZttK-UyKJaqB68zPRXHtXvoicys76zpWDrYLMZ_NwmxzRx94_G99evFbfjQKkC71QcM-Tw-nTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9849737611.mp4?token=QOt8jiRJ-zvAYzsfPZtAQI5-Nbrjfx_BaVWoo2S5osuwIa2iH-1nqpt04v-X5YxnEiXq37Ui_lbxUIFONyQvry2g9vadKGz1CzVbzKTPNoicgzmVzs8hSzx6Q1O3sc3jBIKkF-S7RedcRxZ7gN2bNRokjgAcaq5Clz5Ghi4n2lR262N7oOavkPVOyt0l4K2V3HguJyzYhJ6um5VuP0mIYoaMRJqjeuwRT9stsMje_YwHvfMCLtgaNqz8ZHaHX78vhksyYKyJZzfRZttK-UyKJaqB68zPRXHtXvoicys76zpWDrYLMZ_NwmxzRx94_G99evFbfjQKkC71QcM-Tw-nTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ اولیۀ حملۀ دشمن آمریکایی به محل برگزاری مراسم عروسی در بندر کوهستک سیریک  @Farsna - Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/459588" target="_blank">📅 01:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459587">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3969eedd.mp4?token=urxPRzo8G7jRK20Aegf0Pm16teTD0V16-y0yOcb-tNZglFCRaOYFJAwlNNgNOjMxECCI9UVGcyiKe6vzi7Ided4iowpsdJoRD6gvGT6RqQh1eUQgLBuMmo3ZC0utEO65OVXn0QfDlU5IZJ62w1OergxWvB8Ec0Bnu7uwp0SvDPLT2GulDdRaAwD4CxafDtS8aa1xkSFViUAvdSJu0gIy7D2zHZUNUa9WHDLGjeNfoGJcjIVyAEQDwxb0SwI1p8BpJ6qrNnVHj0j_f-FwGNHWGkzZO5ccoqJExV-hWXKyx_sup0-Xkghb0JHIt9htCeRHRECwSP8a2sK2PeDe6vpAHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3969eedd.mp4?token=urxPRzo8G7jRK20Aegf0Pm16teTD0V16-y0yOcb-tNZglFCRaOYFJAwlNNgNOjMxECCI9UVGcyiKe6vzi7Ided4iowpsdJoRD6gvGT6RqQh1eUQgLBuMmo3ZC0utEO65OVXn0QfDlU5IZJ62w1OergxWvB8Ec0Bnu7uwp0SvDPLT2GulDdRaAwD4CxafDtS8aa1xkSFViUAvdSJu0gIy7D2zHZUNUa9WHDLGjeNfoGJcjIVyAEQDwxb0SwI1p8BpJ6qrNnVHj0j_f-FwGNHWGkzZO5ccoqJExV-hWXKyx_sup0-Xkghb0JHIt9htCeRHRECwSP8a2sK2PeDe6vpAHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌شمار مجروحان حمله به عروسی در کوهستک به ۶۸ نفر رسید
🔹
بنابر اعلام هلال‌احمر، شمار مجروحان حملۀ دشمن آمریکایی به مراسم عروسی در کوهستک سیریک به ۶۸ نفر رسید.
🔹
شمار زیادی از مصدومان کودک هستند که به بیمارستان‌های سیریک و میناب منتقل شده‌اند.
◾️
همچنین تاکنون…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/459587" target="_blank">📅 01:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459586">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BI-U3s7BiQA_GyiUN-SkQhPrrHilQNC6QXOtrSAhI2oSXmIDplHH5S2M9ZDavgWeEn8fpfyzr-NzX6gMpoBosBoM95YLVK0W6EYGkzNeb_geKSg7u7S1btuOmWDGlE2MIFCv-vS0OCoiIodbbCKCtxASvqlFlB3Q840TVoZIgkDh-sPGK0jqoyIk0gWJrQIzEYRqpEGsIWOeyg5xDZH_uSWeYPicnQLShsOhSzI23o-SaQh4QdNc8SugPBFVmhVgg2VmvO7BlEoS8mDUJuBPE0CctvVMWwbaOXgpaYD0simYerlvTrzHozlsvZDZX2YwTsqsuBAg34ru0W3m_AFiKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس کمیسیون امنیت ملی: هدف قراردادن یک عروسی و قتل‌عام مردم بی‌گناه در کوهستک، گواه نهایی استیصال مطلق مدافعان دروغین حقوق‌بشر و تکرار جنایات آن‌ها در میناب و لامرد است.
🔹
این جنایات بدون مجازات نخواهند ماند. هیچ‌چیز آن‌ها را از ارادۀ کوبندۀ نیروهای مسلح ایران محافظت نخواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/459586" target="_blank">📅 01:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459584">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xk99dBMYXzve1hT4bTH676PGERmjHebB2xin3myBvtyTP4E-GW0KwRFncoAUuLAQokc4nvJUNchbz9sIxIkSS4Hr-UO3zk64_7pcxhwCT6sLe1sBPwv4zmBJB-asFcsH_TAQkYvst48UuhkahsEifYyx72GVTN8DbnFhTSxIlc80x4Wy8HA-NMtjB_HWndecv-E0rL6XadRhKeofrHECu9rHidia6KZXMMVWmEr7N-TBM5ml_SRUblU6_8M3vUZqXgb02Ufqf65awQncoW7JviuZTw6yF4Tt5etgvulJbxDnrxIZYw6VzPuag2sSCmdIzErl3pxdld-ORK6_1BPhuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j-Hns17GPu2EmA7SIs11Spp5yppsRtr3E_dTiecDjjR1S1lZ5k-LnRddVYgsNe6CM6kkUmpVcZ8lZXUUB9WkZoHa5yWls4l16WMbpECPsUil9xBxVzfexnmdAJBl10PVH9vge9WGZkRrl1Yfje0aPi7EweifHr6_93N_Nvm3E0pLiigrMN6O-NOIU79Tcx1cT1TosjD9H5dSMZDYYbtTImqHMYbtnTdj1mpPaUuPz7PsXnVg7PBrkd7l9-hynpcMhKA47soOcVJLhjUQPyzjJqTwcLVuh6q5UZMrU3HSd6cuQXCTgyHsCSOZEjLYjcp9Vl436JOpB_df43Lo8Bu-fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌ شمار شهدای حمله به عروسی در سیریک به ۵ نفر رسید
🔹
هلال‌احمر: شمار شهدای حملۀ دشمن آمریکایی به مراسم عروسی در کوهستک سیریک به ۵ نفر رسید و ۵۰ نفر مجروح شده‌اند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/459584" target="_blank">📅 01:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459583">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">برق مناطق آسیب‌دیدۀ قشم وصل شد
🔹
فرماندار قشم از رفع قطعی برق در مناطقی از این شهرستان که در پی حملات شامگاه سه‌شنبه آمریکا دچار خاموشی شده بود، خبر داد و گفت جریان برق اکنون در تمامی نقاط قشم برقرار و پایدار است.
🔹
همچنین عوامل شرکت توزیع برق هرمزگان نیز در تلاش برای وصل کردن برق مناطق مورد حمله در کوهستک سیریک هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/459583" target="_blank">📅 01:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459582">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0635efc59d.mp4?token=eV7VpLejfnDu5uWbbFbZU2x2MZ3IH95acvuA01Hbaoj3AIUJSl9MxvGVCaNpfdPpT2Ok2B0u2-wNwJb-pgbMxMWeZSBf4D-dOli8ES8Ypx1cirfGhR-M2Q0shixkoXnFm7Kzc5nA74-5CTGywu0abNvL95VuoMbQqk5prCMZudpTRYLPhaEBtbazsF9xVx9tD-D3gIr5RaTlvBZsZyTeAW_oufWChWlCFgdChQ939F-8amvtJK0YIj7bRkgRAGUzkrUBXM-lh6Z1_XZgD_0QLX5duotFZ0GXy0q98wZkhXqwhp18CPZoMyWk5X2KAExP4UxkuZo1PZlI1Mww-MkyzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0635efc59d.mp4?token=eV7VpLejfnDu5uWbbFbZU2x2MZ3IH95acvuA01Hbaoj3AIUJSl9MxvGVCaNpfdPpT2Ok2B0u2-wNwJb-pgbMxMWeZSBf4D-dOli8ES8Ypx1cirfGhR-M2Q0shixkoXnFm7Kzc5nA74-5CTGywu0abNvL95VuoMbQqk5prCMZudpTRYLPhaEBtbazsF9xVx9tD-D3gIr5RaTlvBZsZyTeAW_oufWChWlCFgdChQ939F-8amvtJK0YIj7bRkgRAGUzkrUBXM-lh6Z1_XZgD_0QLX5duotFZ0GXy0q98wZkhXqwhp18CPZoMyWk5X2KAExP4UxkuZo1PZlI1Mww-MkyzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظهٔ اصابت موشک به اهداف آمریکایی در اردن  @Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/459582" target="_blank">📅 01:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459581">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">۴ فوتی و ۱۰ مصدوم در حادثۀ برخورد خودرو با تجمع‌کنندگان در مشهد
🔹
ساعتی قبل یک دستگاه خودروی جنسیس در بلوار وکیل‌آباد مشهد با سرعت بالا منحرف و پس از آن با تجمع‌کنندگان برخورد کرد.
🔹
در این حادثه ۴ نفر فوت و بیش از ۱۰ نفر زخمی شدند. @Farsna - Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/459581" target="_blank">📅 01:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459580">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93e2b5cb22.mp4?token=VR74fYM4HtbCaEhw859FeHnewlMHU4eoJpcAfmm1dZ_dHrCfK5Z9B4KagWoLkZ4KNrWZ4BWElNFXG2J-QoK0hpOVYfMjLlzFHKeoBDzELiv2ukgHpn2mPJ3CXeyaoK_brGfymfzDuRXty7ZVbIj-9DhV5xiBcgb27l0Cvw5PTg7OcnXdCMZyNccMTuBPHQuINNcaNsmtrR5O4Wm9R38II1FDeEGXLHPKpQVy7iZ_M6DIHjAOyrOvudJii1ztBDgUNEngyv7GBZVjp4x5isnXqOkM8nn3epM9dAnn9CteIPKE6LAsgAXRqqy990NtorGkzJIVKkazzxuZCVsLZc3kzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93e2b5cb22.mp4?token=VR74fYM4HtbCaEhw859FeHnewlMHU4eoJpcAfmm1dZ_dHrCfK5Z9B4KagWoLkZ4KNrWZ4BWElNFXG2J-QoK0hpOVYfMjLlzFHKeoBDzELiv2ukgHpn2mPJ3CXeyaoK_brGfymfzDuRXty7ZVbIj-9DhV5xiBcgb27l0Cvw5PTg7OcnXdCMZyNccMTuBPHQuINNcaNsmtrR5O4Wm9R38II1FDeEGXLHPKpQVy7iZ_M6DIHjAOyrOvudJii1ztBDgUNEngyv7GBZVjp4x5isnXqOkM8nn3epM9dAnn9CteIPKE6LAsgAXRqqy990NtorGkzJIVKkazzxuZCVsLZc3kzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملات پهپادی ارتش به پایگاه‌ آمریکا در بحرین
🔹
روابط‌عمومی ارتش: در بیست‌ونهمین مرحله از عملیات صاعقه و در پاسخ به تجاوز دشمن به مناطق جنوبی کشور، ساعاتی پیش ارتش جمهوری اسلامی ایران، تاسیسات راداری و مراکز تجمع نیروهای تروریست آمریکایی در پایگاه شیخ عیسی بحرین را هدف حملات پر حجم پهپادهای انهدامی قرار داد.
🔹
پایگاه شیخ عیسی بحرین، یکی از مهم‌ترین و حساس‌ترین پایگاه های آمریکا در منطقه خلیج فارس و از مراکز مهم تعمیر و نگهداری بالگردها و قطعات پهپادها و میزبان هواپیماهای شناسایی است.
🔹
رزمندگان ارتش جمهوری اسلامی ایران، به شرارت‌های دشمن، پاسخ کوبنده و گسترده داده و انتقامی سخت و پشیمان کننده از متجاوزان خواهند گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/459580" target="_blank">📅 00:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459579">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🎥
مجروحیت کودکان در حملۀ آمریکا به جشن عروسی در کوهستک
🔹
بیش از ۱۵ کودک حاضر در عروسی کوهستک سیریک در جریان حملۀ آمریکا به این شهر مجروح شدند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/459579" target="_blank">📅 00:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459578">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شایعۀ حمله به کرمانشاه تکذیب شد
🔹
معاون استانداری کرمانشاه با رد شایعات مطرح‌شده گفت هیچ نقطه‌ای از استان کرمانشاه مورد اصابت دشمن قرار نگرفته و وضعیت در استان کاملاً عادی و تحت کنترل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/459578" target="_blank">📅 00:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459577">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a48d0c20.mp4?token=epBb4Kyh2UsTtaAUM31-VH2Rh6CRh4q_moGFxL6ZF2G9VSLbZIAv_pCSmVm_OUyYj8MXueVoLMgsedcCxDRetB0rK6nc90epECLalDLQVvK9RNmWLf0P45mx1nEW4MuO5z4hV9phOy01fResLfN2p7jRrD8lQLyG-6twK9lUggWpXeL-UgEs9TiDucR_VXkbdaNsPcPe-CTqUYooD3bWwLNq9v4pJLMMKMi7eryZPGpQiJqom5g2UObuc8soHSoCZ7CcH4D-8bNckCr5bdKw3eJnB0tzyAQ8TT12PqH1oNa8SL7MAjtZlbDKqILR4Wets93eT61KXVNtLIV7CjzpLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a48d0c20.mp4?token=epBb4Kyh2UsTtaAUM31-VH2Rh6CRh4q_moGFxL6ZF2G9VSLbZIAv_pCSmVm_OUyYj8MXueVoLMgsedcCxDRetB0rK6nc90epECLalDLQVvK9RNmWLf0P45mx1nEW4MuO5z4hV9phOy01fResLfN2p7jRrD8lQLyG-6twK9lUggWpXeL-UgEs9TiDucR_VXkbdaNsPcPe-CTqUYooD3bWwLNq9v4pJLMMKMi7eryZPGpQiJqom5g2UObuc8soHSoCZ7CcH4D-8bNckCr5bdKw3eJnB0tzyAQ8TT12PqH1oNa8SL7MAjtZlbDKqILR4Wets93eT61KXVNtLIV7CjzpLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویری از جنایت آمریکا در سیریک
◾️
ساعاتی پیش مراسم عروسی و دو دکل ارتباطی در کوهستک سیریک مورد حملۀ دشمن آمریکایی قرار گرفت که تاکنون ۴ شهید و ۵۰ مجروح داشته است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farsna/459577" target="_blank">📅 00:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459576">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd0f4552b1.mp4?token=FvscptrOTlNv1G-i0n24BMYZvrhaJO0fmBGKK1C_wnPW3bD5_1MNAhSJxlyvdARtEZyknnHXTL6QlbO13WK2M8m8DmFTdTOF0tzqG-SbIh1IKdAdbdnusKKnJBK-k2ZR2CBPMDyuftE1CDqr87bcXPHb_3bHZu3kVPqr55L9EzHo3thJWs9rWw_2r19epbQ-I0uniUIBb4C3CEBiqqvmqhwYHaEqQGa77O0WaYVsYb7DJAVZejA4R3fUBy674CZt9Gk1lmZ4C2jgAqUb4dtiSitbFxbX_OU7tpqw9KW5yL9Y4NuSCNmxYZiEge4-4Jopx3DVESBUw82SKDVxF-Te_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd0f4552b1.mp4?token=FvscptrOTlNv1G-i0n24BMYZvrhaJO0fmBGKK1C_wnPW3bD5_1MNAhSJxlyvdARtEZyknnHXTL6QlbO13WK2M8m8DmFTdTOF0tzqG-SbIh1IKdAdbdnusKKnJBK-k2ZR2CBPMDyuftE1CDqr87bcXPHb_3bHZu3kVPqr55L9EzHo3thJWs9rWw_2r19epbQ-I0uniUIBb4C3CEBiqqvmqhwYHaEqQGa77O0WaYVsYb7DJAVZejA4R3fUBy674CZt9Gk1lmZ4C2jgAqUb4dtiSitbFxbX_OU7tpqw9KW5yL9Y4NuSCNmxYZiEge4-4Jopx3DVESBUw82SKDVxF-Te_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: پادگان تفنگداران آمریکایی در اردن هدف موشک‌های بالستیک قرار گرفت؛ تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
🔹
روابط عمومی سپاه: ملت قهرمان و بپاخاسته ایران اسلامی، ارتش تروریستی و شکست‌خوردهٔ آمریکا، عاجز از رویارویی مستقیم با رزمندگان اسلام…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/459576" target="_blank">📅 00:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459575">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">۴ فوتی و ۱۰ مصدوم در حادثۀ برخورد خودرو با تجمع‌کنندگان در مشهد
🔹
ساعتی قبل یک دستگاه خودروی جنسیس در بلوار وکیل‌آباد مشهد با سرعت بالا منحرف و پس از آن با تجمع‌کنندگان برخورد کرد.
🔹
در این حادثه ۴ نفر فوت و بیش از ۱۰ نفر زخمی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/459575" target="_blank">📅 00:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459571">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s_PW4mVC6m3ahKunGnus1L9rpYkeybq0gr3-Bl-qeam2Qj9k0S-G6A8OpaBH5SifUrPQhjltm16_Ys7TIZtthf1sBprH_4IQYMrXzeGmSXtIyq43BtUGX_uVTCbqc4DVkWoFkSblhuXlSsx1Seqmgokeitx6WQX-0v6tHIxs5xFS9M5Vj9Bz2NoFujjfcRpVaZBxl8Ad_vZmN1oc5kw-AW4bYA6ORys1uXqp6PapP3X-EK_g2kCWW2rTzWHCNjC25QjThdbRpqclO4vVupISagHQP2xq81uLT3QCltJkJgeXU0AbbA-Q8CNkeZz1sP52xVbjW5EyDfV40bp2OpIglg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S37qn6SVsAMrjoZ4yonlD-8iALhbJiiV7QkiOZJREJgxnMxeJRTjOEiXXchFSntL3SDq82BeGGkv1RA0gKczgctPshIWkUODnw7Cy0cvIl3yULTTy2F4MTXs-9fQ-pfj1FCHSjzqPWNU_fIPra5o5v8NnxzeOPbXXvT0oqH1MGQVvA3OJbs4C4rORWIQd9trOPvp-OKxLJn8k8fXO8xFeqtuSmZ5uk7IjhnpTDXeGCU9DVTOMPTRAh5MKo1ukkblOOs09Vrx7f5Zbbl0aafXkzfXxXCVcvgAN-rmRbtOoHdoVd6KLDjTFXGspZ7CsEgVtsT7hINEjnEnN7HyrDu8kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U6-xIbTEdw9VLyx7rzqWTOjuL6SD363BaQ8Vyt1Kqaxwzy8phCRPl88EGQ567X2wDPFG0Pe5I3U0FvWcZtsYZNcFW5feVZX5y7hPBgJN6BRf2X5SNo4Rp1hfJQDVVeW_4cj8dNWu915QVInJmY109dCe3HfZ-I9TBKqBSB3zvLhXNvbq-e2BBmj5fAu7Z0BTeIfwz-cbOD6roMtQmLRKV2AXkWJQCHwPOb28OE2no0ULBXnaMXqMaTjLn2KZM6Uj4Mo1VBhCpVG0uzLoJROiLkx6d5QmBXB2NJvwszDN343EMrUi-FzPrBpn71GOVJkoCgwB2is5-AmsWkxDHnUhbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fSvH4GHANxufwKTLcIW3MaAhfF5LyoY7bYfWL2DlZI561ixRF338Qa1K5W8hA6jxpiJp6aR1yTK_LgQwArQVdBVQ8saRi0GsKhFMmWROnYhx8XbeLx3JQxgTuJvpgut6lwTIzDjWf1xJXqf9qjVVJBMlONG7oO1gj0M20H6FX4aptHsmQ6wO5F27WRe7Bf5sDUM2sJEDPw2n-cttBCdmFTReWmTomoDe9KlwIoV9mc_0SfHJov5azuU0mo3JH2dVciot3lTtxs5Yv7GrwybmZwBMkTY_LDcbvY44DmKPpRzGJRZJPR5DyeF2FUxmfq3y9M8F8aBNsDsudriaNBVPmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
تصاویر دیگری از جنایت آمریکا در سیریک  @Farsna - Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farsna/459571" target="_blank">📅 00:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459569">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69d034784.mp4?token=KErlguA7UeE1i6NPo0LPFJu27xMA-J65d8ic16MBGx3hKGmZIbB9tWbRRikEAWvLbuFIJulwITsevNTBuDoiXgBo3by56lxSSJVr9J-oJ2HEx-evr7htvX2GFz2xHXdbmPlTqHCs8qaCOsHsYR-PMLFNoxy58bAoaDmPhx3etl1R5yIbw4s-jlUrVxOJmuUllcxgPSlk-Mpxoh6PZ98DBnkNWbuOATKeKllZm1Klo8s0NwpqzpVlU15fm7MdEGI8ZDBae69zuNBZB_eGHAYNtFzhIkSdpFt3oMl3taRq8i3HqEeiT0gOgpD7EZEHYtPQ4vz21lHzpFogL-mj2V3OFhDVCJzhbI6JeTVAiGV8rgIiYRkYtByG_-ystHVUdm-fUCN8fdVLYdTa50aCqmji-vq2cZJWXWp1MXHVuYyHi2ozgLB6DZWo6sAmLOT7R4lybep9n9EvoB1RX3vQKG-lRDAVfR6xCzGHEgkQCk7wj7j5Oj6gFWfMwYLcKu-8lqpgAj1YF8o3GOuUrVkkYJFA-yPgTOKtSlmkkpTkjzImifQAn0RQPTUeXG1YDQ3yqrH3wT0G1zv2UOn27AVlaO5sQgq-wQ7B9IlIL1G65ChO6Ff6qzpziOKFaVJyVkDTicsWty0oDZs46LgUcIUFWhEu9wN1680Rgxzj_-6zqu-1-Y4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69d034784.mp4?token=KErlguA7UeE1i6NPo0LPFJu27xMA-J65d8ic16MBGx3hKGmZIbB9tWbRRikEAWvLbuFIJulwITsevNTBuDoiXgBo3by56lxSSJVr9J-oJ2HEx-evr7htvX2GFz2xHXdbmPlTqHCs8qaCOsHsYR-PMLFNoxy58bAoaDmPhx3etl1R5yIbw4s-jlUrVxOJmuUllcxgPSlk-Mpxoh6PZ98DBnkNWbuOATKeKllZm1Klo8s0NwpqzpVlU15fm7MdEGI8ZDBae69zuNBZB_eGHAYNtFzhIkSdpFt3oMl3taRq8i3HqEeiT0gOgpD7EZEHYtPQ4vz21lHzpFogL-mj2V3OFhDVCJzhbI6JeTVAiGV8rgIiYRkYtByG_-ystHVUdm-fUCN8fdVLYdTa50aCqmji-vq2cZJWXWp1MXHVuYyHi2ozgLB6DZWo6sAmLOT7R4lybep9n9EvoB1RX3vQKG-lRDAVfR6xCzGHEgkQCk7wj7j5Oj6gFWfMwYLcKu-8lqpgAj1YF8o3GOuUrVkkYJFA-yPgTOKtSlmkkpTkjzImifQAn0RQPTUeXG1YDQ3yqrH3wT0G1zv2UOn27AVlaO5sQgq-wQ7B9IlIL1G65ChO6Ff6qzpziOKFaVJyVkDTicsWty0oDZs46LgUcIUFWhEu9wN1680Rgxzj_-6zqu-1-Y4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: پادگان تفنگداران آمریکایی در اردن هدف موشک‌های بالستیک قرار گرفت؛ تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
🔹
روابط عمومی سپاه: ملت قهرمان و بپاخاسته ایران اسلامی، ارتش تروریستی و شکست‌خوردهٔ آمریکا، عاجز از رویارویی مستقیم با رزمندگان اسلام…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/459569" target="_blank">📅 00:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459568">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMoZYnWSoe_62j-M9j-uAimEK5xZ5U0kPYpgxtnNJjoQ3jbIHWNk0731DJK6rTkY5xgxNGndGOFq8Lbn5cl8wDeG_zs_kJ-1reRqVqUo-eNiVK56-Wh8xGLEtxs9q6LwV0cw1Ya_-pxgj9219chgQrT65gdd8WQFgByjEmBKTo6Dz2BrsCQZ3EBpLckG7ZFC1UFMZk64QUim3391wCvjZa2CfCLyOJ4WBMm48yI8N-qK7pjj_FmuC9whfUSeGQPrNGuOQ8yzGM5NOBFhdrtAtfMFTBIFG0aZ91B7Lbc2VY32m4xLFVn-J3nl7KZNwtaYzxmehvEMjHvCX2D0ZEaC1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رهبر انقلاب: ملّت عزیز ایران و جبههٔ مقاومت، درس‌های فراموش‌نشدنی برای دشمن آمریکایی دارد.
@Farsna</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farsna/459568" target="_blank">📅 00:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459567">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
سپاه: پادگان تفنگداران آمریکایی در اردن هدف موشک‌های بالستیک قرار گرفت؛ تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
🔹
روابط عمومی سپاه: ملت قهرمان و بپاخاسته ایران اسلامی، ارتش تروریستی و شکست‌خوردهٔ آمریکا، عاجز از رویارویی مستقیم با رزمندگان اسلام با حمله وحشیانه به یک منزل مسکونی در سیریک، محل مجلس عقد دو جوان پاک را به خاک و خون کشیده و با به شهادت رساندن و مجروح‌کردن نزدیک به ۵۰ نفر از مردم عزیزمان خاطرهٔ وحشیگری مدرسه میناب و ورزشگاه لامرد را زنده کرد.
🔹
رژیم کودک‌کش آمریکا در این حمله جنایتکارانه یک بار دیگر با به شهادت رساندن چندین نفر از جمله یک کودک، عمق کینه‌توزی و دشمنی خود با مردم ایران را آشکار کرد.
🔹
در پاسخ به این شرارت سبعانه، رزمندگان دلیر نیروی هوافضای سپاه در موج دوم عملیات تنبیه متجاوز با رمز مقدس یا رسول‌الله(ص) با حملهٔ سنگین موشک‌های بالستیک به پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تیتین، واقع در سواحل خلیج عقبه، تعداد زیادی از نیروهای آمریکایی را به درک واصل و چند تاسیسات مهم و بالگردهای هجومی دشمن را منهدم نمودند.
🔹
عملیات انتقامی نیروهای اسلام ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/459567" target="_blank">📅 00:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459566">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ad153b05.mp4?token=fBTdem3wQ-e8_upsofxDbR4wLfFiRV96kFsrtqNMdZDXlpxjfRs_ZNKXmCVcyqjK7eL9xYgA3fox4LWrgWasQATEhWj3qRel4Pfv7gFkSnPtUKRzlfVAML_qHiCBSHJjbibDe-BPnoqk7KUUUCnh_4DvdF8GquKmaTBwFr1086i78MaXCBWCKbfpZ2cEjLWTBtXFSl9sJHcn3W1t3_fOvebMCtr8BNcTPSucKdqQT1i0xhNdJ_NUEoiWIgFxYs0WzSfn2f15PTWUBFqn-QOXVf21XSo_32fJscf6a8Cmg8SaRXr5r562jpKRCOh_5ToJiN-BR9acaqjCUXD4-TSnRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ad153b05.mp4?token=fBTdem3wQ-e8_upsofxDbR4wLfFiRV96kFsrtqNMdZDXlpxjfRs_ZNKXmCVcyqjK7eL9xYgA3fox4LWrgWasQATEhWj3qRel4Pfv7gFkSnPtUKRzlfVAML_qHiCBSHJjbibDe-BPnoqk7KUUUCnh_4DvdF8GquKmaTBwFr1086i78MaXCBWCKbfpZ2cEjLWTBtXFSl9sJHcn3W1t3_fOvebMCtr8BNcTPSucKdqQT1i0xhNdJ_NUEoiWIgFxYs0WzSfn2f15PTWUBFqn-QOXVf21XSo_32fJscf6a8Cmg8SaRXr5r562jpKRCOh_5ToJiN-BR9acaqjCUXD4-TSnRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاین در شب ۱۸۵، قرار عاشقانهٔ مردم را رقم زد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/459566" target="_blank">📅 00:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459564">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EcD3DgACwGkXx29_2fELfzKoymcQfFXTamkR0xdiAopSpNIFAP7pWxqaKEjndKQ-p7yfD43c4WRc-1mf87U2fnSujH0Zj0shwY7P5DDTct5GAKOmuSrkjhCDfifis4MC2yA-LTd94zMAW8fOV9ZB2lIvtJh00gzhJEBhMM2-42NL2rJv6C1ErEmed4EmhChYdrcLzJq7kxFN3cX9r4y1i7DCjw7w4vuAAiPLpLtqRbgBfAkmXnvQeYQfwLh5bWkZXJR6c6uoLPvXWv3t9eJwW880Ahhcz51U4ZIdbsYBAY89xfLcDduvt05qjGJLs0cfHCrcaOqj-MkVmMLkjEuecA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AngxF6Dc5x6VzVKaX1n1e5pvEyKcy_iWvw_FiMqsVHZwlSx1Ti-39btKt61oONrk3j9eH7duVg4Ity8jn-RReucZsZ_8RzV2ipmnIT3oTQruu_4yO7zyWwgsUYomc5lEKgQaqyyRNa1Q29X7T4ihmP421jgcQGfcv9E1TZDP_h9rWiprIfEiIuYKJb7ID3Dve-GGJkG8URnMW25Nr--5HGqzor6uAiaKAnNwmhmZLvJOVW19PGjWIleq4Xu6rowtDJbJ_E6YFxlxE85uV-N6OHmuhBSKbl7OPS9ds7S_CmgwdnA9OfbOAgDFzaB0LLD2XM3RCEYu8VIpHxdze78BiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌
🔴
افزایش شمار شهدای جنایت آمریکا در کوهستک به ۴ نفر؛  یک کودک خردسال در بین شهدا
🔹
هلال احمر هرمزگان: در پی حملهٔ موشکی آمریکا و اصابت ترکش به یک منزل مسکونی در روستای کوهستک از توابع شهرستان سیریک در استان هرمزگان، که مراسم جشن عروسی در آن در حال برگزاری…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farsna/459564" target="_blank">📅 00:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459563">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/861251ffab.mp4?token=eityLSgihF0ZtI294-0bgSFK15qIoAJw0viD5SnVztH3Xyp31-cRswWdSszyn1tweYs5o0JKaPvpXpbfv7bfioDjDq3Q3uHhOgraZFnOlQ0zVpCt3bZgANr_9bElQqcac2-q2SvVv1ZpP1RrDpoEgLao1fjRvwfp7TAPs6cSjO5Td_Oytru5sWlOduEjnpKTianVOPldSDDmjB7Wus8b0vxDB0vt7uEpRPjK9mNmtOciaXNrKCp06cPTmYVC9WlecPMuFdin8FSAOJ96ERks-jBY3d62Q6n8vtvg_X7hzphOY6R0COzgefIuNapphJz_QeEjQmuJatfndHKL8jcFAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/861251ffab.mp4?token=eityLSgihF0ZtI294-0bgSFK15qIoAJw0viD5SnVztH3Xyp31-cRswWdSszyn1tweYs5o0JKaPvpXpbfv7bfioDjDq3Q3uHhOgraZFnOlQ0zVpCt3bZgANr_9bElQqcac2-q2SvVv1ZpP1RrDpoEgLao1fjRvwfp7TAPs6cSjO5Td_Oytru5sWlOduEjnpKTianVOPldSDDmjB7Wus8b0vxDB0vt7uEpRPjK9mNmtOciaXNrKCp06cPTmYVC9WlecPMuFdin8FSAOJ96ERks-jBY3d62Q6n8vtvg_X7hzphOY6R0COzgefIuNapphJz_QeEjQmuJatfndHKL8jcFAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خرم‌‌آبادی‌ها: ای ارتش ای سپاه، بزن بزن ماشاءالله
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farsna/459563" target="_blank">📅 23:54 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
